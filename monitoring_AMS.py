from Keithley import KeithleySMU2400Series
import yaml
from DataPoint import DataPoint
from DataSetAnalysis import DataSet
from VisualizeData import Visualizer
import time
import numpy as np
import pylab as pl

configuration_file = ''
with open('config_keithley_AMS.yaml', 'r') as file:
    configuration_file = yaml.load(file)

dev1 = KeithleySMU2400Series(configuration_file)



dev1.disable_output()
dev1.enable_output()
iter=1

#while 1:
for i in range(3):
    
    print '--------------------Starting an IV measurements'
    
    data, number = dev1.sweep()
        
    print 'Starting IV data storing'
    for d in data:
        print(d.x, d.y, d.x_err, d.y_err)
    
    f=time.strftime("/Users/Administrador/Desktop/IRRADIATIONS_PS/iv_ams_try%s.txt" %iter) 
    f=open(f,'w+')
    print >>f, time.strftime("[%Y-%m-%d %H:%M:%S]\n"), "<V>,  <I>, sd_V, sd_I,\n",
    for d in data:
        print >> f,d.x, d.y, d.x_err, d.y_err    
    f.close()
    
    
    
    print '--------------------Monitoring Current-time'

    data,number=dev1.currenttime()
    print 'done'
    f=time.strftime("/Users/Administrador/Desktop/IRRADIATIONS_PS/monitoring_ams_try.txt") 
    f=open(f,'a+')
    #print >>f, time.strftime("[%Y-%m-%d %H:%M:%S]\n"), "<V>,  <I>, sd_I, time\n",
    for d in data:
        print >> f,d.x, d.y, d.y_err, d.unixtime     
    f.close()
    
    print '--------------------ramping down'
    dev1.ramping_down()
    
    print 'end of iteration:' , iter
    iter=iter+1
    #####================================
    
  

   

