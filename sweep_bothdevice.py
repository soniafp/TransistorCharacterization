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
import os,sys

# Collect input
transistor_type=''
chip_number=raw_input('Chip Number (1, 2, or 3): ')
transistor_number=raw_input('Transistor Number (1-8): ')
radiation_amount=raw_input('Radiation Amount (100Krad, 1Mrad): ')
while transistor_type!='pmos' and  transistor_type!='nmos':
    transistor_type = raw_input('input the transistor type (pmos or nmos): ')

configuration_file = ''
if ( transistor_number=='7' and chip_number=='1') or ( transistor_number=='7' and chip_number=='3'):
    with open('config_deviceGate7.yaml', 'r') as file:
        configuration_file = yaml.load(file)
elif ( transistor_number=='2' and chip_number=='3'):
    with open('config_deviceGate2.yaml', 'r') as file:
        configuration_file = yaml.load(file)    
else:
    with open('config_deviceGate.yaml', 'r') as file:
        configuration_file = yaml.load(file)
        
dev_gate = KeithleySMU2400Series(configuration_file,1)

configuration_file2=''
with open('config_deviceDrain.yaml', 'r') as file:
    configuration_file2 = yaml.load(file)

dev_drain = KeithleySMU2400Series(configuration_file2,1)

configuration_file3=''
with open('config_deviceTrans.yaml', 'r') as file:
    configuration_file3 = yaml.load(file)

dev_transistor = KeithleySMU2400Series(configuration_file3,1)

drain_voltage=1.5
print 'Drain Voltage set to: ',drain_voltage,'V'
dev_drain.set_voltage(drain_voltage,"V")
dev_transistor.set_voltage(drain_voltage,"V") 

dev_gate.disable_output()
dev_drain.disable_output()
dev_transistor.disable_output()
dev_gate.enable_output()
dev_drain.enable_output()
dev_transistor.enable_output()
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
#out_chip%s_%s%s_drain1_5v_vddat1_5v_gnadtgrounded.txt %(chip_number,transistor_type,transistor_number)
#output_file = "run/test1.txt"
out_dir='run'
if not os.path.exists(out_dir):
    os.mkdir('mkdir '+out_dir)
    
output_file = out_dir+'/out_chip%s_%s%s_drain1_5v_vddat1_5v_gnadtgrounded_rad%s.txt' %(chip_number,transistor_type,transistor_number,radiation_amount)
f=time.strftime(output_file)
f=open(f,'w+')
print >> f, time.strftime("[%Y-%m-%d %H:%M:%S]\n"), "<V>,  <Id>,  sd_V,  sd_I, <Vd>,  <Ig>,  sd_Vd,  sd_Ig\n",
for d in data:
    #print >> f,d.x, d.y, d.x_err, d.y_err,d.w, d.z,d.w_err, d.z_err
    print >> f,d.x, d.y, d.x_err, d.y_err,d.w, d.z,d.w_err, d.z_err
   
f.close()
   
dev_gate.disable_output()
dev_drain.disable_output()
dev_transistor.disable_output()
print 'end'
print 'Plots not validated...'
dataa=np.loadtxt(output_file,unpack=True, skiprows=2) 
global_plot_single(dataa, transistor= 'PMOS')
print 'Plot drawing done.'
