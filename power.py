from Keithley import KeithleySMU2400Series
import yaml
import time

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

dev_transistor.disable_output()
dev_drain.disable_output()
dev_transistor.enable_output()
dev_drain.enable_output()


#dev_drain.disable_output()

print 'Drain is ON at ',drain_voltage,' V'
