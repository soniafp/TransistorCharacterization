from Keithley import KeithleySMU2400Series
import yaml
import time
from DataPoint import DataPoint
from DataSetAnalysis import DataSet
from VisualizeData import Visualizer
import numpy as np
#import transistors_analisis
#from transistors_analisis import *
from transistors_analisis import *

configuration_file = ''
with open('config_deviceGate.yaml', 'r') as file:
    configuration_file = yaml.load(file)

dev_gate = KeithleySMU2400Series(configuration_file,1)

with open('config_deviceDrain.yaml', 'r') as file:
    configuration_file2 = yaml.load(file)

dev_drain = KeithleySMU2400Series(configuration_file2,1)

dev_gate.disable_output()
dev_drain.disable_output()
dev_gate.enable_output()
dev_drain.enable_output()
drain_voltage=1.5
print 'Drain Voltage set to: ',drain_voltage,'V'
dev_drain.set_voltage(drain_voltage,"V") 
#dev_gate.set_voltage(0,"V") 

data, number = dev_gate.sweep(dev_drain)
#data, number = dev1.sweep(dev2)

for d in data:
    print 'Vg, Id, Id,errV,errI,   Vd, Ig, Id,errVd,errIg'
    print(d.x, d.y,d.x_err, d.y_err,d.w, d.z,d.w_err, d.z_err)

dset = DataSet(data,'data')
dset.set_transistor_dimensions(4.0, 0.18)
dset.calc_characteristics()
#print(dset.get_property())

vis = Visualizer('title', '2 1')    
vis.add_plot(dset, ty='rawData', ind='0 0')
vis.add_plot(dset, ty='sqData', ind='1 0')
vis.get_plot()
#output_file = "/Users/Administrador/Desktop/test1.txt"
output_file = "run/test1.txt"
f=time.strftime(output_file)
f=open(f,'w+')
print >> f, time.strftime("[%Y-%m-%d %H:%M:%S]\n"), "<V>,  <Id>,  sd_V,  sd_I, <Vd>,  <Ig>,  sd_Vd,  sd_Ig\n",
for d in data:
    #print >> f,d.x, d.y, d.x_err, d.y_err,d.w, d.z,d.w_err, d.z_err
    print >> f,d.x, d.y, d.x_err, d.y_err,d.w, d.z,d.w_err, d.z_err
   
f.close()
   
dev_gate.disable_output()
dev_drain.disable_output()
print 'end'
print 'Plots not validated...'
dataa=np.loadtxt(output_file,unpack=True, skiprows=2) 
global_plot_single(dataa, transistor= 'PMOS')
print 'Plot drawing done.'
