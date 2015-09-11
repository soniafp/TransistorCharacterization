from Keithley import KeithleySMU2400Series
import yaml
from DataPoint import DataPoint
from DataSetAnalysis import DataSet
from VisualizeData import Visualizer
import time
import numpy as np
import pylab as pl

configuration_file = ''
with open('config_keithley.yaml', 'r') as file:
    configuration_file = yaml.load(file)

dev1 = KeithleySMU2400Series(configuration_file)



dev1.disable_output()
dev1.enable_output()
dev1.enable_output()


print 'before sweep funtion'
data, number = dev1.sweep()
  
print 'after sweep funtion'
for d in data:
    print(d.x, d.y, d.x_err, d.y_err)
  
  
f=time.strftime("/Users/Administrador/Documents/MAPS/XTB02/IVcurves/chip_I/data/060715_17-09-autorange-chipI_NWELLS-GND_Nring-GND_pfield-BIASED_grfield-floating_roomT.txt") 
f=open(f,'w+')
print >>f, time.strftime("[%Y-%m-%d %H:%M:%S]\n"), "<V>,  <I>,  sd_V,  sd_I\n",
for d in data:
    print >> f,d.x, d.y, d.x_err, d.y_err    
f.close()
  
  
dev1.disable_output()

pl.title('I-V')
ax = pl.subplot(111)
data=np.loadtxt("/Users/Administrador/Documents/MAPS/XTB02/IVcurves/chip_I/data/060715_17-09-autorange-chipI_NWELLS-GND_Nring-GND_pfield-BIASED_grfield-floating_roomT.txt",skiprows=2)
ax.errorbar(abs(data[:,0]),abs(data[:,1])*1e9,data[:,3],data[:,2]*1e9,color="red", linewidth=3, linestyle="--")
pl.ylabel('Current [nA]')
pl.xlabel('Voltage [V]')
pl.xlim(0, -300)
pl.legend('leakage', loc='upper left', numpoints = 1 )
pl.show()