from Keithley import KeithleySMU2400Series
import yaml
import time
from DataPoint import DataPoint
from DataSetAnalysis import DataSet
from VisualizeData import Visualizer
import numpy as np
from transistors_analisis import *

# Collect input
transistor_type=''
chip_number=raw_input('Chip Number (1, 2, or 3): ')

configuration_file = ''
with open('config_deviceHV.yaml', 'r') as file:
    configuration_file = yaml.load(file)

dev_hv = KeithleySMU2400Series(configuration_file,1)
dev_hv.disable_output()
dev_hv.enable_output()

data, number = dev_hv.sweep(dev_hv)

for d in data:
    print 'Vg, Id, Id,errV,errI,   Vd, Ig, Id,errVd,errIg'
    print(d.x, d.y,d.x_err, d.y_err,d.w, d.z,d.w_err, d.z_err)

dset = DataSet(data,'data')
dset.set_transistor_dimensions(4.0, 0.18)
dset.calc_characteristics()

vis = Visualizer('title', '2 1')    
vis.add_plot(dset, ty='rawData', ind='0 0')
vis.add_plot(dset, ty='sqData', ind='1 0')
vis.get_plot()

output_file = 'run/out_hv_iv_chip%s.txt' %(chip_number)
f=time.strftime(output_file)
f=open(f,'w+')
print >> f, time.strftime("[%Y-%m-%d %H:%M:%S]\n"), "<V>,  <Id>,  sd_V,  sd_I, <Vd>,  <Ig>,  sd_Vd,  sd_Ig\n",
for d in data:
    print >> f,d.x, d.y, d.x_err, d.y_err,d.w, d.z,d.w_err, d.z_err
   
f.close()
   
dev_hv.disable_output()
print 'end'
print 'Plots not validated...'
#dataa=np.loadtxt(output_file,unpack=True, skiprows=2) 
#global_plot_single(dataa, transistor= 'PMOS')
print 'Plot drawing done.'
