from Keithley import KeithleySMU2400Series
import yaml
import time

NMOS_ON=False

configuration_file2=''
with open('config_deviceDrain.yaml', 'r') as file:
    configuration_file2 = yaml.load(file)

dev_drain = KeithleySMU2400Series(configuration_file2,1)

configuration_file3=''
with open('config_deviceTrans.yaml', 'r') as file:
#with open('config_deviceGate.yaml', 'r') as file:    
    configuration_file3 = yaml.load(file)
    
dev_transistor = KeithleySMU2400Series(configuration_file3,1)

configuration_file1=''
with open('config_deviceGate.yaml', 'r') as file:    
    configuration_file1 = yaml.load(file)

dev_gate = KeithleySMU2400Series(configuration_file1,1)
    
drain_voltage=1.8
print 'Drain Voltage set to: ',drain_voltage,'V'
dev_drain.set_voltage(drain_voltage,"V")
if NMOS_ON:
    dev_gate.set_voltage(1.8,"V")
else:
    dev_gate.set_voltage(1.8,"V")
    
dev_transistor.set_voltage(drain_voltage,"V") 

dev_transistor.disable_output()
dev_drain.disable_output()
dev_gate.disable_output()

time.sleep(0.2)

dev_transistor.enable_output()
dev_drain.enable_output()
print dev_drain.get_current("A")

time.sleep(0.2)

dev_gate.set_voltage(1.8,"V")
dev_gate.enable_output()
print dev_gate.get_current("A")

#dev_drain.disable_output()

print 'Drain is ON at ',drain_voltage,' V'
