from DataPoint import DataPoint
import math
#import yaml

def get_list_from_DataSet(data):
    ls = []
    for m in data:
        ls.append([m.x, m.y, m.x_err, m.y_err])
    return ls

class DataSet():
    def __init__(self, data, name):
        self._shift = min([d.y for d in data])-1E-12
        if self._shift > 0:
            self._shift = 0
        else:
            None
            
        self._dataPoint = data
        self._dataPointSq = [DataPoint(d.x, math.sqrt(d.y-self._shift), d.x_err, 0.5*d.y_err/math.sqrt(d.y-self._shift)) for d in self._dataPoint]
        
        self._slope_dataPoint = []
        self._slope_dataPointSq = []
        self._curvature_dataPoint = []
        self._maxSlope_sq = []
        self._maxSlope = []
        self._transistorLength = 1
        self._transistorWidth = 1
        self._vthr = []
        self._cmu = []
        self._name = name
    
    def set_transistor_dimensions(self, length, width):
        self._transistorLength = length
        self._transistorWidth = width
    
    def get_data(self):
        return self._dataPoint
    
    def get_data_sq(self):
        return self._dataPointSq
    
    def get_slope_sq(self):
        return self._slope_dataPointSq
    
    def calc_slope_sq(self):
        for it in range( len(self._dataPointSq) ):
            if( (it > 0) and (it < len(self._dataPointSq)-1) ):
                dY = (self._dataPointSq[it+1].y - self._dataPointSq[it-1].y)
                dX = (self._dataPointSq[it+1].x - self._dataPointSq[it-1].x)
                deltaSlope = -dY/(dX*dX)*(self._dataPointSq[it+1].x_err - self._dataPointSq[it-1].x_err) + (self._dataPointSq[it+1].y_err - self._dataPointSq[it-1].y_err)/dX 
                self._slope_dataPointSq.append(DataPoint(self._dataPointSq[it].x, dY/dX, self._dataPointSq[it].x_err, deltaSlope))
                
            else:
                if(it == 0):
                    dY = (self._dataPointSq[it+1].y - self._dataPointSq[it].y)
                    dX = (self._dataPointSq[it+1].x - self._dataPointSq[it].x) 
                    deltaSlope = -dY/(dX*dX)*(self._dataPointSq[it+1].x_err - self._dataPointSq[it].x_err) + (self._dataPointSq[it+1].y_err - self._dataPointSq[it].y_err)/dX 
                    self._slope_dataPointSq.append(DataPoint(self._dataPointSq[it].x, dY/dX, self._dataPointSq[it].x_err, deltaSlope))
                    
                if(it == (len(self._dataPointSq)-1) ):
                    dY = (self._dataPointSq[it].y - self._dataPointSq[it-1].y)
                    dX = (self._dataPointSq[it].x - self._dataPointSq[it-1].x) 
                    deltaSlope = -dY/(dX*dX)*(self._dataPointSq[it].x_err - self._dataPointSq[it-1].x_err) + (self._dataPointSq[it].y_err - self._dataPointSq[it-1].y_err)/dX 
                    self._slope_dataPointSq.append(DataPoint(self._dataPointSq[it].x, dY/dX, self._dataPointSq[it].x_err, deltaSlope))
    
    def calc_slope(self):
        for it in range( len(self._dataPoint) ):
            if( (it > 0) and (it < len(self._dataPoint)-1) ):
                dY = (self._dataPoint[it+1].y - self._dataPoint[it-1].y)
                dX = (self._dataPoint[it+1].x - self._dataPoint[it-1].x)
                deltaSlope = math.sqrt(math.fabs((dY/(dX*dX))*(dY/(dX*dX))*(self._dataPoint[it+1].x_err*self._dataPoint[it+1].x_err - self._dataPoint[it-1].x_err*self._dataPoint[it-1].x_err) + (self._dataPoint[it+1].y_err*self._dataPoint[it+1].y_err - self._dataPoint[it-1].y_err*self._dataPoint[it-1].y_err)/(dX*dX))) 
                self._slope_dataPoint.append(DataPoint(self._dataPoint[it].x, dY/dX, self._dataPoint[it].x_err, deltaSlope))
                
            else:
                if(it == 0):
                    dY = (self._dataPoint[it+1].y - self._dataPoint[it].y)
                    dX = (self._dataPoint[it+1].x - self._dataPoint[it].x) 
                    deltaSlope = math.sqrt(math.fabs((dY/(dX*dX))*(dY/(dX*dX))*(self._dataPoint[it+1].x_err*self._dataPoint[it+1].x_err - self._dataPoint[it].x_err*self._dataPoint[it].x_err) + (self._dataPoint[it+1].y_err*self._dataPoint[it+1].y_err - self._dataPoint[it].y_err*self._dataPoint[it].y_err)/(dX*dX)))
                    self._slope_dataPoint.append(DataPoint(self._dataPoint[it].x, dY/dX, self._dataPoint[it].x_err, deltaSlope))
                    
                if(it == (len(self._dataPoint)-1) ):
                    dY = (self._dataPoint[it].y - self._dataPoint[it-1].y)
                    dX = (self._dataPoint[it].x - self._dataPoint[it-1].x) 
                    deltaSlope = math.sqrt(math.fabs((dY/(dX*dX))*(dY/(dX*dX))*(self._dataPoint[it].x_err*self._dataPoint[it].x_err - self._dataPoint[it-1].x_err*self._dataPoint[it-1].x_err) + (self._dataPoint[it].y_err*self._dataPoint[it].y_err - self._dataPoint[it-1].y_err*self._dataPoint[it-1].y_err)/(dX*dX)))
                    self._slope_dataPoint.append(DataPoint(self._dataPoint[it].x, dY/dX, self._dataPoint[it].x_err, deltaSlope))
                
    def get_slope(self):
        return self._slope_dataPoint
              
    def calc_curvature(self):
        for it in range( len(self._dataPoint)-3 ):
            if( (it > 30) and (it < len(self._dataPoint)-1) ):
                dY = (self._dataPoint[it+1].y + self._dataPoint[it-1].y - 2*self._dataPoint[it].y)
                dX = (self._dataPoint[it+1].x - self._dataPoint[it-1].x)
                deltaCurv = -8/(dX*dX*dX)*(self._dataPoint[it+1].x_err - self._dataPoint[it-1].x_err)*dY + 4/(dX*dX)*(self._dataPoint[it+1].y_err + self._dataPoint[it-1].y_err - 2*self._dataPoint[it].y_err) 
                self._curvature_dataPoint.append(DataPoint(self._dataPoint[it].x, dY/(dX*dX/4.0), self._dataPoint[it].x_err, deltaCurv))
            else: None

    def get_curvature(self):        
        return self._curvature_dataPoint
    
    def calc_max_slope_sq(self):
        #remember sos has two entries less than the data set!!!!! the first and last datapoint is missing
        self.calc_curvature()
        soslist = get_list_from_DataSet(self._curvature_dataPoint)
        temp = [list(s) for s in zip(*soslist)]
        maxCurvature = max(temp[1]) 
        idxshift = temp[1].index(maxCurvature)
        
        if ( len(self._slope_dataPointSq) == 0):
            self.calc_slope_sq()
        else:
            None
            
        d = get_list_from_DataSet(self._slope_dataPointSq)
        dd = [d[it] for it in range(idxshift+1,len(d))]
        temp = [list(s) for s in zip(*dd)]
        maxSlope = max(temp[1])
        idx = temp[1].index(maxSlope)+idxshift
        self._maxSlope_sq = [self._dataPointSq[idx].x, self._dataPointSq[idx].x_err, self._dataPointSq[idx].y, self._dataPointSq[idx].y_err, maxSlope, self._slope_dataPointSq[idx].y_err]
        
    def calc_max_slope(self):
        if ( len(self._slope_dataPoint) == 0):
            self.calc_slope()
        else:
            None
            
        d = get_list_from_DataSet(self._slope_dataPoint)
        temp = [list(s) for s in zip(*d)]
        maxSlope = max(temp[1])
        idx = temp[1].index(maxSlope)
        self._maxSlope = [self._dataPoint[idx].x, self._dataPoint[idx].x_err, self._dataPoint[idx].y, self._dataPoint[idx].y_err, maxSlope, self._slope_dataPoint[idx].y_err]
        
    def get_max_slope(self):
        return self._maxSlope    

    def get_max_slope_sq(self):
        return self._maxSlope_sq     

    def get_muCox(self):
        return [2*self._maxSlope_sq[4]*self._maxSlope_sq[4]*self._transistorLength/self._transistorWidth, math.fabs(4*self._maxSlope_sq[4]*self._maxSlope_sq[5]*self._transistorLength/self._transistorWidth)]
        
    def get_vthreshold(self):
        return [-1*(self._maxSlope_sq[2]+self._shift)/self._maxSlope_sq[4] + self._maxSlope_sq[0], math.fabs(-self._maxSlope_sq[3]/self._maxSlope_sq[4] + self._maxSlope_sq[2]*self._maxSlope_sq[5]/(self._maxSlope_sq[4]*self._maxSlope_sq[4]) + self._maxSlope_sq[1])]
    
    def calc_characteristics(self):
        self.calc_max_slope_sq()
        self.calc_max_slope()
        self._vthr = self.get_vthreshold()
        self._cmu = self.get_muCox()
        
    def get_characteristics(self):
        return [self._vthr, self._cmu, self._transistorLength, self._transistorWidth]
    
    def get_property(self):
        self._property = {   self._name : {
                                    'Vthr' : {'mean' : self._vthr[0], 'error' : self._vthr[1]},
                                    'Cmuox' : {'mean' : self._cmu[0], 'error' : self._cmu[1]},
                                    'Gm' : {'mean' : self._maxSlope[0], 'error' : self._maxSlope[1]},
                                    'Length' : self._transistorLength,
                                    'Width' : self._transistorWidth
                                    }
                         }            
        return self._property
    
    def get_name(self):
        return self._name
    
    def save_data(self, filename):
        data = { self._name :
                    { 'raw data' : { 'V_gs' : { 'mean' : [d.x for d in self._dataPoint],
                                                'error' : [d.x_err for d in self._dataPoint]},
                                     'I_d' : {'mean' : [d.y for d in self._dataPoint],
                                                'error' : [d.y_err for d in self._dataPoint]}},
                      'sqrt data' : { 'V_gs' : { 'mean' : [d.x for d in self._dataPoint],
                                                'error' : [d.x_err for d in self._dataPoint]},
                                     'sqrt I_d' : {'mean' : [d.y for d in self._dataPointSq],
                                                'error' : [d.y_err for d in self._dataPointSq]}},
                     'gm data' : { 'V_gs' : { 'mean' : [d.x for d in self._dataPoint],
                                                'error' : [d.x_err for d in self._dataPoint]},
                                     'gm' : {'mean' : [d.y for d in self._slope_dataPoint],
                                                'error' : [d.y_err for d in self._slope_dataPoint]}},
                     'curvature' : { 'V_gs' : { 'mean' : [d.x for d in self._dataPoint],
                                                'error' : [d.x_err for d in self._dataPoint]},
                                     'curv' : {'mean' : [d.y for d in self._curvature_dataPoint],
                                                'error' : [d.y_err for d in self._curvature_dataPoint]}},
                     'Vthr' : {'mean' : self._vthr[0], 'error' : self._vthr[1]},
                     'Cmuox' : {'mean' : self._cmu[0], 'error' : self._cmu[1]},
                     'Gm' : {'mean' : self._maxSlope[0], 'error' : self._maxSlope[1]},
                     'Length' : self._transistorLength,
                     'Width' : self._transistorWidth
                     
                     }
                }
        
        #with open('%s_data.yaml'%filename, 'w') as file:
        #    file.write( yaml.dump( data, default_flow_style=False) )
