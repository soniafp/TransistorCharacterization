import numpy as np
import pylab as pl
import time
import Tkinter
from Tkinter import * 




################################
###IV plot ISEQ - KEITHLEY #####
################################

# # pl.title('IV curve 100um2 ring')
# # ax = pl.subplot(111)
# # data=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix100_20degrees.txt',skiprows=2)
# # ax.errorbar(abs(data[:,0]),abs(data[:,1])*1e9,data[:,3],data[:,2]*1e9,color="red", linewidth=3, linestyle="--", label='T=20')
# # data1=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix100_10degrees.txt',skiprows=2)
# # ax.errorbar(abs(data1[:,0]),abs(data1[:,1])*1e9,data1[:,3],data1[:,2]*1e9,color="blue", linewidth=3, linestyle="--", label='T=10')
# # data2=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix100_0degrees.txt',skiprows=2)
# # ax.errorbar(abs(data2[:,0]),abs(data2[:,1])*1e9,data2[:,3],data2[:,2]*1e9,color="green", linewidth=3, linestyle="o", label='T=0')
# # data3=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix100_m10degrees.txt',skiprows=2)
# # pl.errorbar(abs(data3[:,0]),abs(data3[:,1])*1e9,data3[:,3],data3[:,2]*1e9,color="yellow", linewidth=3, linestyle="x", label='T=-10')
# # data4=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix100_m20degrees.txt',skiprows=2)
# # pl.errorbar(abs(data4[:,0]),abs(data4[:,1])*1e9,data4[:,3],data4[:,2]*1e9,color="black", linewidth=3, linestyle="<", label='T=-20')
# # ####################################

# pl.title('IV curve 50v2 (50 x 50 um2) ring')
# ax = pl.subplot(111)
# data=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix50v2_20degrees.txt',skiprows=2)
# ax.errorbar(abs(data[:,0]),abs(data[:,1])*1e9,data[:,3],data[:,2]*1e9,color="red", linewidth=3, linestyle="--", label='T=20')
# data1=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix50v2_10degrees.txt',skiprows=2)
# ax.errorbar(abs(data1[:,0]),abs(data1[:,1])*1e9,data1[:,3],data1[:,2]*1e9,color="blue", linewidth=3, linestyle="--", label='T=10')
# data2=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix50v2_0degrees.txt',skiprows=2)
# ax.errorbar(abs(data2[:,0]),abs(data2[:,1])*1e9,data2[:,3],data2[:,2]*1e9,color="green", linewidth=3, linestyle="o", label='T=0')
# data3=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix50v2_m10degrees.txt',skiprows=2)
# pl.errorbar(abs(data3[:,0]),abs(data3[:,1])*1e9,data3[:,3],data3[:,2]*1e9,color="yellow", linewidth=3, linestyle="x", label='T=-10')
# data4=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix_m20degrees.txt',skiprows=2)
# pl.errorbar(abs(data4[:,0]),abs(data4[:,1])*1e9,data4[:,3],data4[:,2]*1e9,color="black", linewidth=3, linestyle="<", label='T=-20')
# ####################################

# pl.title('IV curve 25/50 ring')
# ax = pl.subplot(111)
# data=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix2550_20degrees.txt',skiprows=2)
# ax.errorbar(abs(data[:,0]),abs(data[:,1])*1e9,data[:,3],data[:,2]*1e9,color="red", linewidth=3, linestyle="--", label='T=20')
# data1=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix2550_10degrees.txt',skiprows=2)
# ax.errorbar(abs(data1[:,0]),abs(data1[:,1])*1e9,data1[:,3],data1[:,2]*1e9,color="blue", linewidth=3, linestyle="--", label='T=10')
# data2=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix2550_0degrees.txt',skiprows=2)
# ax.errorbar(abs(data2[:,0]),abs(data2[:,1])*1e9,data2[:,3],data2[:,2]*1e9,color="green", linewidth=3, linestyle="o", label='T=0')
# data3=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix2550_m10degrees.txt',skiprows=2)
# pl.errorbar(abs(data3[:,0]),abs(data3[:,1])*1e9,data3[:,3],data3[:,2]*1e9,color="yellow", linewidth=3, linestyle="x", label='T=-10')
# data4=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix2550_m20degrees.txt',skiprows=2)
# pl.errorbar(abs(data4[:,0]),abs(data4[:,1])*1e9,data4[:,3],data4[:,2]*1e9,color="black", linewidth=3, linestyle="<", label='T=-20')
# ####################################
# # 
# # pl.title('IV curve outside ring')
ax = pl.subplot(111)
data=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_no-irradiated/iv_hvring2550ring_290914.txt',skiprows=2)
ax.errorbar(abs(data[:,0]),abs(data[:,1])*1e9,data[:,3],data[:,2]*1e9,color="red", linewidth=3, linestyle="-", label='outer+2550ring (no_irrad)')
data1=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_no-irradiated/iv_hvring50ring_290914.txt',skiprows=2)
ax.errorbar(abs(data1[:,0]),abs(data1[:,1])*1e9,data1[:,3],data1[:,2]*1e9,color="blue", linewidth=3, linestyle="-", label='outer+50ring (no_irrad)')
data2=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_no-irradiated/iv_hvring100ring_290914.txt',skiprows=2)
ax.errorbar(abs(data2[:,0]),abs(data2[:,1])*1e9,data2[:,3],data2[:,2]*1e9,color="green", linewidth=3, linestyle="-", label='outer+100ring (no_irrad)')
data3=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_no-irradiated/iv_hvring_290914.txt',skiprows=2)
pl.errorbar(abs(data3[:,0]),abs(data3[:,1])*1e9,data3[:,3],data3[:,2]*1e9,color="yellow", linewidth=3, linestyle="-", label='outer ring (no_irrad)')
data4=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_after700Mrad/iv_hvring2550ring_290914.txt',skiprows=2)
pl.scatter(abs(data4[:,0]),abs(data4[:,1])*1e9,color="red", linewidth=1.5, linestyle="--",drawstyle='steps', label='2550ring (after700Mrad)')
data5=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_after700Mrad/iv_hvring50ring_290914.txt',skiprows=2)
pl.errorbar(abs(data5[:,0]),abs(data5[:,1])*1e9,data5[:,3],data5[:,2]*1e9,color="blue", linewidth=1.5, linestyle="--",drawstyle='steps', label='50ring (after700Mrad)')
data6=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_after700Mrad/iv_hvring100ring_290914.txt',skiprows=2)
pl.errorbar(abs(data6[:,0]),abs(data6[:,1])*1e9,data6[:,3],data6[:,2]*1e9,color="green", linewidth=1.5, linestyle="--", drawstyle='steps',label='outer+100ring (after700Mrad)')
data7=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/roomT_after700Mrad/iv_hvring_290914.txt',skiprows=2)
pl.errorbar(abs(data7[:,0]),abs(data7[:,1])*1e9,data7[:,3],data7[:,2]*1e9,color="yellow", linewidth=1.5, linestyle="--",drawstyle='steps', label='outer ring (after700Mrad)')
data8=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/0degrees_after700Mrad/iv_hvring2550ring_031014_0degrees.txt',skiprows=2)
pl.errorbar(abs(data8[:,0]),abs(data8[:,1])*1e9,data8[:,3],data8[:,2]*1e9,color="red", linewidth=0.5, marker="d",drawstyle='steps', label='2550ring (after700Mrad -0 degrees)')
data9=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/0degrees_after700Mrad/iv_hvring50ring_031014_0degrees.txt',skiprows=2)
pl.errorbar(abs(data9[:,0]),abs(data9[:,1])*1e9,data9[:,3],data9[:,2]*1e9,color="blue", linewidth=0.5, marker="d",drawstyle='steps', label='50ring (after700Mrad -0 degrees)')
data10=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/0degrees_after700Mrad/iv_hvring100ring_031014_0degrees.txt',skiprows=2)
pl.errorbar(abs(data10[:,0]),abs(data10[:,1])*1e9,data10[:,3],data10[:,2]*1e9,color="green", linewidth=0.5, marker="d", drawstyle='steps',label='outer+100ring (after700Mrad -0 degrees)')
data11=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/cern/0degrees_after700Mrad/iv_hvring_031014_0degrees.txt',skiprows=2)
pl.errorbar(abs(data11[:,0]),abs(data11[:,1])*1e9,data11[:,3],data11[:,2]*1e9,color="yellow", linewidth=0.5, marker="d",drawstyle='steps', label='outer ring (after700Mrad -0 degrees)')

# # ####################################

# pl.title('IV all rings')
# ax = pl.subplot(111)
# data=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/bigring_20degrees.txt',skiprows=2)
# ax.errorbar(abs(data[:,0]),abs(data[:,1])*1e9,data[:,3],data[:,2]*1e9,color="red", linewidth=3, linestyle="--", label='Outside ring')
# data1=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix100_20degrees1.txt',skiprows=2)
# ax.errorbar(abs(data1[:,0]),abs(data1[:,1])*1e9,data1[:,3],data1[:,2]*1e9,color="blue", linewidth=3, linestyle="-", label='ring 100 x 100 matrix')
# data2=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix50v2_20degrees1.txt',skiprows=2)
# ax.errorbar(abs(data2[:,0]),abs(data2[:,1])*1e9,data2[:,3],data2[:,2]*1e9,color="green", linewidth=3, linestyle="-", label='ring 50x50 matrix(AU50V2)')
# data3=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_TEMP/cern-keithley/matrix2550_20degrees.txt',skiprows=2)
# pl.errorbar(abs(data3[:,0]),abs(data3[:,1])*1e9,data3[:,3],data3[:,2]*1e9,color="yellow", linewidth=3, linestyle="-", label='ring 25X25/50x50 matrix')
#  
# # ####################################

################################
###IV plot ISEQ - KEITHLEY #####
################################
# # # # pl.title('IV curve')
# # # # data=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/2014_05_14_16-08_outsidering.txt',skiprows=2)
# # # # pl.errorbar(abs(data[:,0]),abs(data[:,1])*1e9,data[:,3],data[:,2]*1e9,color="red", linewidth=3, linestyle="--", label='HV ring keithley')
# # # # data1=np.loadtxt('/Users/Administrador/Documents/workspace/xtb01/host/FILES/IV_RING/2014_05_14_16-08_outsidering.txt',skiprows=2)
# # # # pl.errorbar(abs(data1[:,0]),abs(data1[:,1])*1e9,data1[:,3],data1[:,2]*1e9,color="blue", linewidth=3, linestyle="o", label='HV ring keithley')

###################################

pl.xlabel('')
pl.ylabel('')
pl.xlim(0, 220)
#ax.set_yscale('log')
#ax.set_ylim(1e0,10e4)


# Put a legend to the right of the current axis
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis

pl.legend(ncol=3,loc='upper center',bbox_to_anchor=(0.5, -0.05),prop={'size':10})

pl.show()
