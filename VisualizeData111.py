from matplotlib import pyplot as plt
import math


class Visualizer():
    def __init__(self, title, size):    
        self._fig, self._axarr = plt.subplots(int(size.split()[0]),int(size.split()[1]), sharex=True)
        self._fig.suptitle(title, fontsize=18, fontweight='bold')
        self._size = size.split()
        #self.add_plot(data)
        #self.get_plot()
    
    def add_plot(self, d, ty, ind):
        idx = int(ind.split()[0])
        idy = int(ind.split()[1])
        self._plots = { 'rawData' : { 'title'   : r'$I_d(V_{gs})$',
                                      'data'    : { 'x' : [m.x for m in d.get_data()],
                                                    'y' : [m.y for m in d.get_data()],
                                                    'xerr' : [m.x_err for m in d.get_data()],
                                                    'yerr' : [m.y_err for m in d.get_data()]},
                                                    
                                      'limits'  : { 'x' :
                                                     { 'min' : min([m.x for m in d.get_data()]),
                                                       'max' : max([m.x for m in d.get_data()])},
                                                    'y' :
                                                     { 'min' : min([m.y for m in d.get_data()]),
                                                       'max' : max([m.y for m in d.get_data()])}}},
                       
                       'sqData'   : { 'title'   : r'$\sqrt{I_d}(V_{gs})$',
                                      'data'    : { 'x' : [m.x for m in d.get_data_sq()],
                                                    'y' : [m.y for m in d.get_data_sq()],
                                                    'xerr' : [m.x_err for m in d.get_data_sq()],
                                                    'yerr' : [m.y_err for m in d.get_data_sq()]},
                                      'limits'  : { 'x' :
                                                     { 'min' : min([m.x for m in d.get_data_sq()]),
                                                       'max' : max([m.x for m in d.get_data_sq()])},
                                                    'y' :
                                                     { 'min' : min([m.y for m in d.get_data_sq()]),
                                                       'max' : max([m.y for m in d.get_data_sq()])}}},
                           
                       'gmData'   : { 'title'   : r'$g_m(V_{gs})$',
                                      'data'    : { 'x' : [m.x for m in d.get_slope()],
                                                    'y' : [m.y for m in d.get_slope()],
                                                    'xerr' : [m.x_err for m in d.get_slope()],
                                                    'yerr' : [m.y_err for m in d.get_slope()]},
                                      'limits'  : { 'x' :
                                                     { 'min' : min([m.x for m in d.get_slope()]),
                                                       'max' : max([m.x for m in d.get_slope()])},
                                                    'y' :
                                                     { 'min' : min([m.y for m in d.get_slope()]),
                                                       'max' : max([m.y for m in d.get_slope()])}}},
                       
                       'curvData' : { 'title'   : r'$Curv(V_{gs})$',
                                      'data'    : { 'x' : [m.x for m in d.get_curvature()],
                                                    'y' : [m.y for m in d.get_curvature()],
                                                    'xerr' : [m.x_err for m in d.get_curvature()],
                                                    'yerr' : [m.y_err for m in d.get_curvature()]},
                                      'limits'  : { 'x' :
                                                     { 'min' : min([m.x for m in d.get_curvature()]),
                                                       'max' : max([m.x for m in d.get_curvature()])},
                                                    'y' :
                                                     { 'min' : min([m.y for m in d.get_curvature()]),
                                                       'max' : max([m.y for m in d.get_curvature()])}}}
                   }
       
        if self._size[0] == '1':
            self._axarr[idy].set_xlim(self._plots[ty]['limits']['x']['min'],self._plots[ty]['limits']['x']['max'])
            self._axarr[idy].set_ylim(self._plots[ty]['limits']['y']['min'],self._plots[ty]['limits']['y']['max'])
            self._axarr[idy].errorbar(self._plots[ty]['data']['x'], self._plots[ty]['data']['y'], self._plots[ty]['data']['xerr'], self._plots[ty]['data']['yerr'], marker='x', linestyle='None', label = d.get_name())
           
            if ty == 'sqData':      
                A = math.sqrt(d.get_muCox()[0]/2.0*d.get_characteristics()[3]/d.get_characteristics()[2])
                self._axarr[idy].errorbar([self._plots[ty]['limits']['x']['min'], self._plots[ty]['limits']['x']['max']], [A*(self._plots[ty]['limits']['x']['min']-d.get_characteristics()[0][0]), A*(self._plots[ty]['limits']['x']['max']-d.get_characteristics()[0][0])], label = 'Vthr %.3f V'%d.get_vthreshold()[0])
            
            
            self._axarr[idy].text(0.5,0.9,self._plots[ty]['title'], horizontalalignment='center', transform=self._axarr[idy].transAxes, fontsize=14)
            self._axarr[idy].legend(loc='upper left', numpoints=1)
        
        else:   
            if self._size[1] == '1':
                self._axarr[idx].set_xlim(self._plots[ty]['limits']['x']['min'],self._plots[ty]['limits']['x']['max'])
                self._axarr[idx].set_ylim(self._plots[ty]['limits']['y']['min'],self._plots[ty]['limits']['y']['max'])
                self._axarr[idx].errorbar(self._plots[ty]['data']['x'], self._plots[ty]['data']['y'], self._plots[ty]['data']['xerr'], self._plots[ty]['data']['yerr'], marker='x', linestyle='None', label = d.get_name())
               
                if ty == 'sqData':      
                    A = math.sqrt(d.get_muCox()[0]/2.0*d.get_characteristics()[3]/d.get_characteristics()[2])
                    self._axarr[idx].errorbar([self._plots[ty]['limits']['x']['min'], self._plots[ty]['limits']['x']['max']], [A*(self._plots[ty]['limits']['x']['min']-d.get_characteristics()[0][0]), A*(self._plots[ty]['limits']['x']['max']-d.get_characteristics()[0][0])], label = 'Vthr %.3f V'%d.get_vthreshold()[0])
                
                
                self._axarr[idx].text(0.5,0.9,self._plots[ty]['title'], horizontalalignment='center', transform=self._axarr[idx].transAxes, fontsize=14)
                self._axarr[idx].legend(loc='upper left', numpoints=1)
            
            else:
                self._axarr[idx,idy].set_xlim(self._plots[ty]['limits']['x']['min'],self._plots[ty]['limits']['x']['max'])
                self._axarr[idx,idy].set_ylim(self._plots[ty]['limits']['y']['min'],self._plots[ty]['limits']['y']['max'])
                self._axarr[idx,idy].errorbar(self._plots[ty]['data']['x'], self._plots[ty]['data']['y'], self._plots[ty]['data']['xerr'], self._plots[ty]['data']['yerr'], marker='x', linestyle='None', label = d.get_name())
               
                if ty == 'sqData':      
                    A = math.sqrt(d.get_muCox()[0]/2.0*d.get_characteristics()[3]/d.get_characteristics()[2])
                    self._axarr[idx,idy].errorbar([self._plots[ty]['limits']['x']['min'], self._plots[ty]['limits']['x']['max']], [A*(self._plots[ty]['limits']['x']['min']-d.get_characteristics()[0][0]), A*(self._plots[ty]['limits']['x']['max']-d.get_characteristics()[0][0])], label = 'Vthr %.3f V'%d.get_vthreshold()[0])
                
                self._axarr[idx,idy].text(0.5,0.9,self._plots[ty]['title'], horizontalalignment='center', transform=self._axarr[idx,idy].transAxes, fontsize=14)
                self._axarr[idx,idy].legend(loc='upper left', numpoints=1)
                
    
    
        
    def get_plot(self):
        plt.show()
        

        