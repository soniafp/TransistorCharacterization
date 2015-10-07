import serial
from serial import Serial
import time
from DataPoint import DataPoint
from DataPoint1 import DataPoint1
# :-)
Units = { 
          'Voltage' :
          { 'mV' : 0.001,
             'V' : 1.0},
         
          'Current' :
          { 'nA' : 0.000000001,
            'uA' : 0.000001,
            'mA' : 0.001,
             'A' : 1.0}
         }

Modi = {
         'Source' :
         { 'V' : 'VOLT',
            'v' : 'VOLT',
            'A' : 'CURR',
            'a' : 'CURR'
         },
         'Measure' :
         { 'V' : 'VOLT',
          'v' : 'VOLT',
           'A' : 'CURR',
           'a' : 'CURR'}
         }

##################################################
##################################################
## Class definitions
##################################################
##################################################

# class SourceError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)

#Class for the Keithley SMU 2400/2410 series
class KeithleySMU2400Series:
    ser = None
    
    def __init__(self, conf, OUTPUT_LVL):
        self.configuration_file = conf
        self.set_device_configuration()
        self.OUTPUT_LVL = OUTPUT_LVL
    #===========================================================================
    # Open serial interface
    #===========================================================================
    def open_device_interface(self):
        self._ser.open()
        print ("Device Ready at Port %s"%(self.configuration_file["Device"]["Configuration"]["Port"]))
    
    #===========================================================================
    # Switch on the output
    #===========================================================================
    def enable_output(self):
        self._ser.write(':OUTPUT ON\r\n')
        print ("Output On")
    
    def disable_output(self):
        self._ser.write(':OUTPUT OFF\r\n')
        print ("Output Off")
    
    #===========================================================================
    # Close serial interface
    #===========================================================================
    def close_device_interface(self):
        self._ser.close()
        print ("Device Closed at Port %s"%(self.configuration_file["Device"]["Configuration"]["Port"]))
    
    
    def set_device_configuration(self):
        #Initialization of the Serial interface
        try:
            self._ser = Serial(
                                 port = self.configuration_file["Device"]["Configuration"]["Port"],
                                 baudrate = self.configuration_file["Device"]["Configuration"]["Baudrate"],
                                 timeout = 2
                                 )
            self._source = Modi['Source'][self.configuration_file["Device"]["Configuration"]["Source"]]
            self._measure = Modi['Measure'][self.configuration_file["Device"]["Configuration"]["Measure"]]    
            
            #Specifies the size of data buffer
            self._triggerCount = self.configuration_file["Device"]["Configuration"]["TriggerCount"]
            
            #Specifies trigger delay in seconds
            self._triggerDelay = self.configuration_file["Device"]["Configuration"]["TriggerDelay"]
            
            
            self._autorangeMeasure = self.configuration_file["Device"]["Configuration"]["AutoRangeMeasure"]
            self._autorangeSource = self.configuration_file["Device"]["Configuration"]["AutoRangeSource"]
            
            self._complianceSource = self.configuration_file["Device"]["Configuration"]["ComplianceSource"] 
            self._complianceMeasure = self.configuration_file["Device"]["Configuration"]["ComplianceMeasure"]
            
            self._sourceRange = self.configuration_file["Device"]["Configuration"]["RangeSource"]
            
            
            #Setup the source
            self._ser.write('*RST\r\n')
            
            self._ser.write(':SYST:BEEP:STAT OFF\r\n')
            
            self._ser.write(':SOUR:CLEar:IMMediate\r\n')
            self._ser.write(':SOUR:FUNC:MODE %s\r\n'%(self._source))
            #self._ser.write(':SOUR:CLEar:IMMediate\r\n')
            self._ser.write(':SOUR:%s:MODE FIX\r\n'%(self._source))
            self._ser.write(':SOUR:%s:RANG:AUTO %s\r\n'%(self._source, self._autorangeSource))
            self._ser.write(':SOUR:%s:PROT:LEV %s\r\n'%(self._source, self._complianceSource))
            if(self._autorangeSource == 'OFF'):
                self._ser.write(':SOUR:%s:RANG %s\r\n'%(self._source, self._sourceRange))
            else:
                None
            
            #Setup the sensing
            self._ser.write(':SENS:FUNC \"%s\"\r\n'%(self._measure))
            self._ser.write(':SENS:%s:PROT:LEV %s\r\n'%(self._measure, self._complianceMeasure))
            self._ser.write(':SENS:%s:RANG:AUTO %s\r\n'%(self._measure, self._autorangeMeasure))
            
            #Setup the buffer
            self._ser.write(':TRAC:FEED:CONT NEVer\r\n')
            self._ser.write(':TRAC:FEED SENSE\r\n')  
            self._ser.write(':TRAC:POIN %s\r\n'%(self._triggerCount))
            self._ser.write(':TRAC:CLEar\r\n')
            self._ser.write(':TRAC:FEED:CONT NEXT\r\n')                
            
            #Setup the data format
            self._ser.write(':FORMat:DATA ASCii\r\n')
            self._ser.write(':FORMat:ELEM VOLTage, CURRent\r\n')
             
            #Setup the trigger
            self._ser.write(':TRIG:COUN %s\r\n'%(self._triggerCount))
            self._ser.write(':TRIG:DELay %s\r\n'%(self._triggerDelay))
            
            print ("Device at Port %s Configured"%(self.configuration_file["Device"]["Configuration"]["Port"]))
        
        except ValueError:
            print('ERROR: No serial connection. Chech cable!')
        
    
    def enable_auto_range(self):
        self._ser.write(':SENS:RANG:AUTO ON\r\n')
       
    def disable_auto_range(self):
        self._ser.write(':SENS:RANG:AUTO OFF\r\n')
    
    def reset(self):
        self._ser.write('*RST\r\n')
       
    def set_value(self, source_value):
        if(source_value > self._complianceSource):
            print("ERROR: Source value is higher than Compliance!")
        else:
            self._ser.write(':SOUR:%s:LEVel %s\r\n'%(self._source, source_value))
            time.sleep(self.configuration_file["Device"]["Configuration"]["SettlingTime"])
      
    def set_voltage(self, voltage_value, unit):
        val = voltage_value*Units['Voltage'][unit]
        if(val > self._complianceSource):
            print("ERROR: Source value is higher than Compliance!")
        else:
            val = voltage_value*Units['Voltage'][unit]
            self._ser.write(':SOUR:%s:LEVel %s\r\n'%(self._source, val))
            time.sleep(self.configuration_file["Device"]["Configuration"]["SettlingTime"])
        
    def set_source_upper_range(self, senseUpperRange):
        self._ser.write(':SENSE:%s:RANG:UPP %s\r\n'%(self._source, senseUpperRange))
          
    def sample(self):  #When I store the data in the buffer (measuring)
        #time.sleep(2)
        self._ser.write(':TRAC:FEED:CONT NEVer\r\n') #NEVER= disable buffer
        self._ser.write(':TRACe:CLEar\r\n') #Clear buffer
        self._ser.write(':TRAC:FEED:CONT NEXT\r\n')  #NEXT= fill buffer and stop
        self._ser.write(':INIT\r\n') #start (so, I have not clear how many points it takes..I know until fill the buffer
    
    def get_raw_values(self):
        self._ser.write(':TRACe:DATA?\r\n') #read the contents of the buffer
       
    def get_mean(self): 
        self._ser.write(':CALC3:FORM MEAN\r\n')
        self._ser.write(':CALC3:DATA?\r\n')
     
    def get_std(self):
        self._ser.write(':CALC3:FORM SDEV\r\n')
        self._ser.write(':CALC3:DATA?\r\n')
      
    def read(self, time_to_wait):    
        while ( self._ser.inWaiting() <= 2 ):   
            pass       
        time.sleep(time_to_wait)    
        data = self._ser.read(self._ser.inWaiting()) 
        return data
    
    #===========================================================================
    # Returns a list with format [voltage,current]
    #===========================================================================
    def get_value(self, with_error = False):
        self.sample()
        self.get_mean()
        dmean = eval(self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"]))
        if(with_error == True):    
            self.get_std()
            dstd = eval(self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"]))
            return dmean, dstd
        else: 
            return dmean
        
    def get_voltage(self, unit, with_error = False):
        self.sample()
        
        self.get_mean()
        d = eval(self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"]))
        if(with_error == True):
            self.get_std()
            derr = eval(self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"]))    
            return d[0]/Units['Voltage'][unit], derr[0]/Units['Voltage'][unit]
        else:
            return d[0]/Units['Voltage'][unit]
            
    def get_current(self, unit, with_error = False):
        self.sample()
        self.get_mean()
        d = eval(self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"]))
        if(with_error == True):
            self.get_std()
            derr = eval(self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"]))    
            return d[1]/Units['Current'][unit], derr[1]/Units['Current'][unit]
        else:
            return d[1]/Units['Current'][unit]
        
    #-----3 sweep types-------
    #linear
    #SenseOptimized
    #CurvatureOptimized
    def sweep(self, measureDev=None):
        counter = 0
        dataSample = []
            
        if (measureDev is not None):
            number_of_points = self.configuration_file["Device"]["Sweep"]["Points"]
            if self.OUTPUT_LVL<2:
                print 'Running ',number_of_points,' Voltages'
            for i in range(0,self.configuration_file["Device"]["Sweep"]["Points"]+1):
                #Settings and ramping up
                low = self.configuration_file["Device"]["Sweep"]["LowValue"]
                high = self.configuration_file["Device"]["Sweep"]["HighValue"]
                points = self.configuration_file["Device"]["Sweep"]["Points"]
                val = low+i*(high-low)/points
                if self.OUTPUT_LVL<2:
                    print 'Setting sweep: ',val,' V ',i,' of ',number_of_points
                self.set_value(val)   #inside set_value, there is time.sleep() that you control by the variable SettlingTime 
                #in the config_keithley.yalm. This has the same effect that add directly here a sleep.time(). i.e. in between 
                #the set value and sample(data taking)       
                
                #Measuring the values that are set
                
                self.sample() #data taking, you fill the buffer.
                self.get_mean()
                sourceData = self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
                sourceMean = eval(sourceData)
                
                self.get_std()
                sourceData = self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
                sourceStd = eval(sourceData)
                
                #Measuring the values
                measureDev.sample()
                measureDev.get_mean()
                measureData = measureDev.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
                measureMean = eval(measureData)
                
                measureDev.get_std()
                measureData = measureDev.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
                measureStd = eval(measureData)
                
                d = DataPoint(sourceMean[0], measureMean[1],sourceStd[0], measureStd[1],sourceMean[1],sourceStd[1],measureMean[0],measureStd[0])
                dataSample.append(d)
                counter += 1
            #Ramping down
            print "Measurement ended. Ramping down"
            if self.OUTPUT_LVL<2:
                print 'Running ',self.configuration_file["Device"]["Sweep"]["Points_down"],' Voltages'
            a= range(0,self.configuration_file["Device"]["Sweep"]["Points_down"]+1)
            a.reverse()
            for i in a:
                
                low = self.configuration_file["Device"]["Sweep"]["LowValue"]
                high = self.configuration_file["Device"]["Sweep"]["HighValue"]
                points = self.configuration_file["Device"]["Sweep"]["Points_down"]
                val = low+i*(high-low)/points

                if self.OUTPUT_LVL<2:
                    print 'Setting sweep: ',val,' V ',i,' of ',self.configuration_file["Device"]["Sweep"]["Points_down"]
                self.set_value(val) 
                time.sleep(1)

        
        else:
            
            for i in range(0,self.configuration_file["Device"]["Sweep"]["Points"]+1):
                low = self.configuration_file["Device"]["Sweep"]["LowValue"]
                high = self.configuration_file["Device"]["Sweep"]["HighValue"]
                points = self.configuration_file["Device"]["Sweep"]["Points"]
                val = low+i*(high-low)/points
                self.set_value(val) 
                time.sleep(1)           
                self.sample()
        
                self.get_mean()
                sourceData = self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
                sourceMean = eval(sourceData)
                
                self.get_std()
                sourceData = self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
                sourceStd = eval(sourceData)
                
                d = DataPoint(sourceMean[0], sourceMean[1], sourceStd[0], sourceStd[1])
                dataSample.append(d)
                counter += 1
            #Ramping down
            print "Measurement ended. Ramping down"
            #print "low", low
            #print "self",self.configuration_file["Device"]["Sweep"]["Points_down"]+1
            a= range(low,self.configuration_file["Device"]["Sweep"]["Points_down"]+1)
            
            #print "a", a
            a.reverse()
            for i in a:
                
                low = self.configuration_file["Device"]["Sweep"]["LowValue"]
                high = self.configuration_file["Device"]["Sweep"]["HighValue"]
                points = self.configuration_file["Device"]["Sweep"]["Points_down"]
                val = low+i*(high-low)/points
                self.set_value(val) 
                time.sleep(1)
        
        return dataSample, counter
       
        #Add other sweeping types if needed
        
    ## S.Fernandez, monitoring current versus time
    def currenttime(self): 
        counter = 0
        dataSample = []
# #         low = self.configuration_file["Device"]["Sweep"]["LowValue"]
# #         self.set_value(low)
        
        freq = self.configuration_file["Device"]["monitoring"]["frequency"]
        iter = self.configuration_file["Device"]["monitoring"]["iterations"]
        for i in range(0,iter):
            time.sleep(1)           
            self.sample()
    
            self.get_mean()
            sourceData = self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
            sourceMean = eval(sourceData)
            
            self.get_std()
            sourceData = self.read(self.configuration_file["Device"]["Configuration"]["WaitRead"])
            sourceStd = eval(sourceData)
            t=time.time()
            
            
            d = DataPoint1(sourceMean[0],sourceMean[1],sourceStd[1],t)
            dataSample.append(d)
            counter += 1 
            time.sleep(freq)
        return dataSample, counter
    
    def ramping_down(self):
        print "Measurement ended. Ramping down"
        a= range(0,self.configuration_file["Device"]["Sweep"]["Points_down"]+1)
        a.reverse()
        for i in a:
             
            low = self.configuration_file["Device"]["Sweep"]["LowValue"]
            high = self.configuration_file["Device"]["Sweep"]["HighValue"]
            points = self.configuration_file["Device"]["Sweep"]["Points_down"]
            val = low+i*(high-low)/points
            self.set_value(val) 
            time.sleep(1)
            
    def ramping_up(self):
        print "Ramping up"
        a= range(0,self.configuration_file["Device"]["Sweep"]["Points"]+1)
        for i in a:
            low = self.configuration_file["Device"]["Sweep"]["LowValue"]
            high = self.configuration_file["Device"]["Sweep"]["HighValue"]
            points = self.configuration_file["Device"]["Sweep"]["Points"]
            val = low+i*(high-low)/points
            self.set_value(val) 
            time.sleep(1)           
            self.sample()
            

            
            
                       
# # # # To store readings to the buffer the TRACE commands must be used. For example use the following commands.
# # # # :TRACE:CLEAR
# # # # :TRACE:POINTS 1000
# # # # :TRIG:COUNT 1000
# # # # :TRACE:FEED:CONT NEXT
# # # # Now send 
# # # # :INIT
# # # # That should store 1000 readings.
# # # # Now send TRACE:DATA?
# # # # and read the data.               
                       
                      
                       
    
