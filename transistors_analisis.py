import yaml
import time
import array
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import pylab 
from pylab import *
import itertools
import operator
import sys
import collections
import math
#from xtb01_sonia import xtb01
import scipy.stats as stats


def square(list):
    return [sqrt(abs(i)) for i in list]



def max_slope(data):
    y=square(data[1])
    x=data[0]
    point_x0=0
    point_x1=0
    point_y0=0
    point_y1=0
    slope=0
    slope_max=0
    iter=0
    for i in range(len(y)-1):
        slope = (y[i+1] - y[i])/(x[i+1] - x[i])
        if abs(slope) > abs(slope_max):
            slope_max=slope
            point_x0=x[i]
            point_y0=y[i]
            point_x1=x[i+1]
            point_y1=y[i+1]
            iter=iter+1
    points_data=[point_x0, point_y0, point_x1, point_y1]
    return slope_max,points_data, iter

def find_slope(points_data=[]):  #order: x1, y1, x2, y2
    slope=((points_data[3] - points_data[1]) / (points_data[2] - points_data[0]))
    return slope

def find_offset(m, x, y):
    intercept=(y - m * x)
    return intercept

def slope_offset_set1(data,data1,data2,data3,data4,data5,data6,data7):
    slope_max_set=[]
    iter_set=[]
    points_data_set=[]
    offset_set=[]
    #data_set=[data,data1,data2,data3,data4,data5,data6,data7]
    data_set=[data]
    #fig.set_size_inches(18.5,15.5)
    #rcParams['figure.figsize'] = 5, 5
    
    j=0
    for element in data_set:
        slope_max, points_data, iter =max_slope(element)
        slope_max1 = find_slope(points_data)
        if slope_max != slope_max1:
            print 'Error in %i', j
        slope_max_set.append(slope_max) #slope_max of all the data_set (i.e. data, data1, data2 ...) will be saved here
        iter_set.append(iter)
        points_data_set.append(points_data)
        offset=find_offset(slope_max, points_data[0], points_data[1])
        offset_set.append(offset) #offset_set of all the data_set (i.e. data, data1, data2 ...) will be saved here
        j=j+1
    print 'slope_max_set:', slope_max_set  
    print 'offset_set:', offset_set 
    
    return slope_max_set, points_data_set, offset_set
def slope_offset_set(data):
    slope_max_set=[]
    iter_set=[]
    points_data_set=[]
    offset_set=[]
    #data_set=[data,data1,data2,data3,data4,data5,data6,data7]
    data_set=[data]
    #fig.set_size_inches(18.5,15.5)
    #rcParams['figure.figsize'] = 5, 5
    
    j=0
    for element in data_set:
        slope_max, points_data, iter =max_slope(element)
        slope_max1 = find_slope(points_data)
        if slope_max != slope_max1:
            print 'Error in %i', j
        slope_max_set.append(slope_max) #slope_max of all the data_set (i.e. data, data1, data2 ...) will be saved here
        iter_set.append(iter)
        points_data_set.append(points_data)
        offset=find_offset(slope_max, points_data[0], points_data[1])
        offset_set.append(offset) #offset_set of all the data_set (i.e. data, data1, data2 ...) will be saved here
        j=j+1
    print 'slope_max_set:', slope_max_set  
    print 'offset_set:', offset_set 
    
    return slope_max_set, points_data_set, offset_set


def logaritm(y=[]):
    ln_y=[]
    for i in range(len(y)):
        value=0
        value=log10(y[i])
        ln_y.append(value)
    return ln_y

def logaritm_set(data,data1,data2,data3,data4,data5,data6,data7):
    data_set=[data[1],data1[1],data2[1],data3[1],data4[1],data5[1],data6[1],data7[1]]
    ln_y_set=[]
    for element in data_set:
        ln_y=logaritm(abs(element))
        ln_y_set.append(ln_y)
    return ln_y_set
        
        
def derivative (x=[], y=[]):
    i=1
    m=len(y)-1
    derivative_yn=[]
    xn=[]
    for i in range(m):
        dyn=0
        dyn=(y[i+1]-y[i-1])/(x[i+1]-x[i-1])
        derivative_yn.append(dyn)
        xn.append(x[i])
    if len(xn) != len(derivative_yn):
        print' Error in extraction derivative'
    return derivative_yn, xn

#def derivative_set(data,data1,data2,data3,data4,data5,data6,data7):
def derivative_set(data):    
    #data_set=[data,data1,data2,data3,data4,data5,data6,data7]
    derivative_yn_set=[]
    xn_set=[]
    element=data
    #for element in data_set:
    derivative_yn, xn= derivative(element[0], element[1])
    derivative_yn_set.append(derivative_yn)
    xn_set.append(xn)
    return derivative_yn_set, xn_set

def characteristic_plot (data,data1,data2,data3,data4,data5,data6,data7, transistor='NMOS'):
    
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.errorbar(data[0],data[1],data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
    ax.errorbar(data1[0],data1[1],data1[2],data1[3],'b-o',linewidth=2.0, label= '2.0/1.4')
    ax.errorbar(data2[0],data2[1],data2[2],data2[3],'g->',linewidth=2.0, label='2.0/0.72')
    ax.errorbar(data3[0],data3[1],data3[2],data3[3],'k-x',linewidth=2.0, label= '2.0/0.36')
    ax.errorbar(data4[0],data4[1],data4[2],data4[3],'y-<',linewidth=2.0, label= '4.0/0.18')
    ax.errorbar(data5[0],data5[1],data5[2],data5[3],'c-p',linewidth=2.0, label= '2.0/0.18')
    ax.errorbar(data6[0],data6[1],data6[2],data6[3],'m:',linewidth=2.0, label= '0.5/0.18')
    ax.errorbar(data7[0],data7[1],data7[2],data7[3],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
    a=[]
    if transistor == 'NMOS': #none=NMOS
        a.append(max(data[1]));a.append(max(data1[1]));a.append(max(data2[1]));a.append(max(data3[1]));a.append(max(data4[1]));
        a.append(max(data5[1]));a.append(max(data6[1]));a.append(max(data7[1]));
        b=max(a)
        ax.set_xlabel('V_gate [V]')
        ax.set_ylabel('I_drain [A]')
        ax.set_xlim(0,1.8)
        ax.set_ylim((0,b))
    if transistor == 'PMOS':  #PMOS
        a.append(min(data[1]));a.append(min(data1[1]));a.append(min(data2[1]));a.append(min(data3[1]));a.append(min(data4[1]));
        a.append(min(data5[1]));a.append(min(data6[1]));a.append(min(data7[1]));
        b=min(a)
        ax.set_xlabel('V_gate [V]')
        ax.set_ylabel('I_drain [A]')
        ax.set_xlim(0,1.8)
        ax.set_ylim((0,b))
    
    #plt.legend( loc='upper right', bbox_to_anchor=(0.3, 1.05), ncol=1, fancybox=True, shadow=False)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.savefig(time.strftime("/Users/Administrador/Documents/workspace/xtb01/host/plots/transistor_ch/%Y_%m_%d_%H_%M_prueba.pdf"), dpi = 300)
    plt.show()
    
    
    


def Threshold_plot (data,data1,data2,data3,data4,data5,data6,data7):
    
    slope_max_set, points_data_set, offset_set=slope_offset_set(data,data1,data2,data3,data4,data5,data6,data7)
    fig, (ax2) = plt.subplots(nrows=1, sharex=False)

    
    ax2.errorbar(data[0],square(data[1]),data[2],0.5 *data[3]/square(data[1]),color="red", linewidth=2.0,linestyle='--', label='2.7/0.27')
    ax2.errorbar(data1[0],square(data1[1]),data1[2],0.5 *data1[3]/square(data1[1]),'b-o',linewidth=2.0, label= '2.0/1.4')
    ax2.errorbar(data2[0],square(data2[1]),data2[2],0.5 *data2[3]/square(data2[1]),'g->',linewidth=2.0, label='2.0/0.72')
    ax2.errorbar(data3[0],square(data3[1]),data3[2],0.5 *data3[3]/square(data3[1]),'k-x',linewidth=2.0, label= '2.0/0.36')
    ax2.errorbar(data4[0],square(data4[1]),data4[2],0.5 *data4[3]/square(data4[1]),'y-<',linewidth=2.0, label= '4.0/0.18')
    ax2.errorbar(data5[0],square(data5[1]),data5[2],0.5 *data5[3]/square(data5[1]),'c-p',linewidth=2.0, label= '2.0/0.18')
    ax2.errorbar(data6[0],square(data6[1]),data6[2],0.5 *data6[3]/square(data6[1]),'m:',linewidth=2.0, label= '0.5/0.18')
    ax2.errorbar(data7[0],square(data7[1]),data7[2],0.5 *data7[3]/square(data7[1]),color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
    x = np.linspace(0,1.8)        
    ax2.plot(x,(slope_max_set[0] *x)+ offset_set[0], color="red",linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[0]/slope_max_set[0]))
    ax2.plot(x,(slope_max_set[1] *x)+ offset_set[1], 'b',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[1]/slope_max_set[1]))
    ax2.plot(x,(slope_max_set[2] *x)+ offset_set[2], 'g',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[2]/slope_max_set[2]))
    ax2.plot(x,(slope_max_set[3] *x)+ offset_set[3],'k', linewidth=2.0,label = 'Vthr %.3fV' %(-offset_set[3]/slope_max_set[3]))
    ax2.plot(x,(slope_max_set[4] *x)+ offset_set[4], 'y',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[4]/slope_max_set[4]))
    ax2.plot(x,(slope_max_set[5] *x)+ offset_set[5], 'c', linewidth=2.0,label = 'Vthr %.3fV' %(-offset_set[5]/slope_max_set[5]))
    ax2.plot(x,(slope_max_set[6] *x)+ offset_set[6], 'm', linewidth=2.0,label = 'Vthr %.3fV' %(-offset_set[6]/slope_max_set[6]))
    ax2.plot(x,(slope_max_set[7] *x)+ offset_set[7], color='Peru',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[7]/slope_max_set[7]))  
    a1=[]
    a1.append(max(square(data[1])));a1.append(max(square(data1[1])));a1.append(max(square(data2[1])));a1.append(max(square(data3[1])));a1.append(max(square(data4[1])));
    a1.append(max(square(data5[1])));a1.append(max(square(data6[1])));a1.append(max(square(data7[1])));
    b1=max(a1)
    ax2.set_xlabel('V_gate [V]')
    ax2.set_ylabel('sqrt(I_drain) [A]')
    ax2.set_xlim((0,1.8))
    ax2.set_ylim((0,b1))
    # Shrink current axis by 20%
    box2 = ax2.get_position()
    ax2.set_position([box2.x0, box2.y0, box2.width * 0.7, box2.height])
    # Put a legend to the right of the current axis
    ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5),ncol=2,fontsize='small')
    #plt.savefig(time.strftime("/Users/Administrador/Documents/workspace/xtb01/host/plots/transistor_ch/%Y_%m_%d_%H_%M_NMOSprueba.png"), dpi = 600)

    plt.show()
    

def gm_plot(data,data1,data2,data3,data4,data5,data6,data7):
    
    derivative_yn_set, xn_set =derivative_set(data,data1,data2,data3,data4,data5,data6,data7)
    fig, (ax2) = plt.subplots(nrows=1, sharex=False)
    
    ax2.plot(xn_set[0], derivative_yn_set[0], color="red",linewidth=2.0,linestyle="--", label ='2.7/0.27')
    ax2.plot(xn_set[1], derivative_yn_set[1], 'b-o',linewidth=2.0, label = '2.0/1.4')
    ax2.plot(xn_set[2], derivative_yn_set[2], 'g->',linewidth=2.0, label = '2.0/0.72')
    ax2.plot(xn_set[3], derivative_yn_set[3],'k-x', linewidth=2.0,label = '2.0/0.36')
    ax2.plot(xn_set[4], derivative_yn_set[4], 'y-<',linewidth=2.0, label = '4.0/0.18')
    ax2.plot(xn_set[5], derivative_yn_set[5], 'c-p', linewidth=2.0,label = '2.0/0.18')
    ax2.plot(xn_set[6], derivative_yn_set[6], 'm:', linewidth=2.0,label = '0.5/0.18')
    ax2.plot(xn_set[7], derivative_yn_set[7], color='Peru',linewidth=2.0,  linestyle='--',label = '0.22/0.18')  
    a1=[]
    a1.append(max(derivative_yn_set[0]));a1.append(max(derivative_yn_set[1]));a1.append(max(derivative_yn_set[2]));a1.append(max(derivative_yn_set[3]));a1.append(max(derivative_yn_set[4]));
    a1.append(max(derivative_yn_set[5]));a1.append(max(derivative_yn_set[6]));a1.append(max(derivative_yn_set[7]));
    b1=max(a1)
    ax2.set_xlabel('V_gate [V]')
    ax2.set_ylabel('Gm ')
    ax2.set_xlim((0,1.8))
    ax2.set_ylim((0,b1))
    # Shink current axis by 20%
    box2 = ax2.get_position()
    ax2.set_position([box2.x0, box2.y0, box2.width * 0.85, box2.height])
    # Put a legend to the right of the current axis
    ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.savefig(time.strftime("/Users/Administrador/Documents/workspace/xtb01/host/plots/transistor_ch/%Y_%m_%d_%H_%M_NMOSprueba.png"), dpi = 600)
    plt.show()

def log_plot (data,data1,data2,data3,data4,data5,data6,data7, transistor='NMOS'):  #aplico escala logaritmica al eje y
    fig = plt.figure()
    ax = plt.subplot(111)
    if transistor == 'NMOS': #none=nmos
        ax.errorbar(data[0],data[1],data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
        ax.errorbar(data1[0],data1[1],data1[2],data1[3],'b-o',linewidth=2.0, label= '2.0/1.4')
        ax.errorbar(data2[0],data2[1],data2[2],data2[3],'g->',linewidth=2.0, label='2.0/0.72')
        ax.errorbar(data3[0],data3[1],data3[2],data3[3],'k-x',linewidth=2.0, label= '2.0/0.36')
        ax.errorbar(data4[0],data4[1],data4[2],data4[3],'y-<',linewidth=2.0, label= '4.0/0.18')
        ax.errorbar(data5[0],data5[1],data5[2],data5[3],'c-p',linewidth=2.0, label= '2.0/0.18')
        ax.errorbar(data6[0],data6[1],data6[2],data6[3],'m:',linewidth=2.0, label= '0.5/0.18')
        ax.errorbar(data7[0],data7[1],data7[2],data7[3],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
    if transistor == 'PMOS':
        ax.errorbar(data[0],fabs(data[1]),data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
        ax.errorbar(data1[0],fabs(data1[1]),data1[2],data1[3],'b-o',linewidth=2.0, label= '2.0/1.4')
        ax.errorbar(data2[0],fabs(data2[1]),data2[2],data2[3],'g->',linewidth=2.0, label='2.0/0.72')
        ax.errorbar(data3[0],fabs(data3[1]),data3[2],data3[3],'k-x',linewidth=2.0, label= '2.0/0.36')
        ax.errorbar(data4[0],fabs(data4[1]),data4[2],data4[3],'y-<',linewidth=2.0, label= '4.0/0.18')
        ax.errorbar(data5[0],fabs(data5[1]),data5[2],data5[3],'c-p',linewidth=2.0, label= '2.0/0.18')
        ax.errorbar(data6[0],fabs(data6[1]),data6[2],data6[3],'m:',linewidth=2.0, label= '0.5/0.18')
        ax.errorbar(data7[0],fabs(data7[1]),data7[2],data7[3],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
        
    ax.set_xlabel('V_gate [V]')
    ax.set_ylabel('I_drain [A]')
    ax.set_xlim(0,1.8)
    ax.set_yscale('log')
    ax.set_ylim(10e-13,10e-3)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.savefig(time.strftime("/Users/Administrador/Documents/workspace/xtb01/host/plots/transistor_ch/%Y_%m_%d_%H_%M_prueba.pdf"), dpi = 300)
    plt.show()  
       
# # # # def log_plot1(data,data1,data2,data3,data4,data5,data6,data7):   #Calculo el logaritmo de cada valor
# # # #     ln_y_set = logaritm_set(data,data1,data2,data3,data4,data5,data6,data7)
# # # #      
# # # #     fig, (ax2) = plt.subplots(nrows=1, sharex=False)
# # # #      
# # # #     ax2.plot(data[0],ln_y_set[0], color="red",linewidth=2.0, label ='2.7/0.27')
# # # #     ax2.plot(data1[0],ln_y_set[1], 'b',linewidth=2.0, label = '2.0/1.4')
# # # #     ax2.plot(data2[0],ln_y_set[2], 'g',linewidth=2.0, label = '2.0/0.72')
# # # #     ax2.plot(data3[0],ln_y_set[3],'k', linewidth=2.0,label = '2.0/0.36')
# # # #     ax2.plot(data4[0],ln_y_set[4], 'y',linewidth=2.0, label = '4.0/0.0.18')
# # # #     ax2.plot(data5[0],ln_y_set[5], 'c', linewidth=2.0,label = '2.0/0.18')
# # # #     ax2.plot(data6[0],ln_y_set[6], 'm', linewidth=2.0,label = '0.5/0.18')
# # # #     ax2.plot(data7[0],ln_y_set[7], color='Peru',linewidth=2.0, label = '0.22/0.18')  
# # # # 
# # # #     ax2.set_xlabel('V_gate [V]')
# # # #     ax2.set_ylabel('ln(I_drain) ')
# # # #     ax2.set_xlim((0,1.8))
# # # #     box2 = ax2.get_position()
# # # #     ax2.set_position([box2.x0, box2.y0, box2.width * 0.85, box2.height])
# # # #     # Put a legend to the right of the current axis
# # # #     ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# # # #     #plt.savefig(time.strftime("/Users/Administrador/Documents/workspace/xtb01/host/plots/transistor_ch/%Y_%m_%d_%H_%M_NMOSprueba.png"), dpi = 600)
# # # #     plt.show()
     
     
       


    
def global_analysis_plot (data,data1,data2,data3,data4,data5,data6,data7, transistor= 'NMOS'):
     
     
    data_set=[data,data1,data2,data3,data4,data5,data6,data7]
    fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2, sharex=False, sharey=False)

     
   # ax1 = plt.subplot(211)
    #================ax1
    ax1.errorbar(data[0],data[1],data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
    ax1.errorbar(data1[0],data1[1],data1[2],data1[3],'b-o',linewidth=2.0, label= '2.0/1.4')
    ax1.errorbar(data2[0],data2[1],data2[2],data2[3],'g->',linewidth=2.0, label='2.0/0.72')
    ax1.errorbar(data3[0],data3[1],data3[2],data3[3],'k-x',linewidth=2.0, label= '2.0/0.36')
    ax1.errorbar(data4[0],data4[1],data4[2],data4[3],'y-<',linewidth=2.0, label= '4.0/0.18')
    ax1.errorbar(data5[0],data5[1],data5[2],data5[3],'c-p',linewidth=2.0, label= '2.0/0.18')
    ax1.errorbar(data6[0],data6[1],data6[2],data6[3],'m:',linewidth=2.0, label= '0.5/0.18')
    ax1.errorbar(data7[0],data7[1],data7[2],data7[3],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
    a=[]
    if transistor == 'NMOS': #none=NMOS
        a.append(max(data[1]));a.append(max(data1[1]));a.append(max(data2[1]));a.append(max(data3[1]));a.append(max(data4[1]));
        a.append(max(data5[1]));a.append(max(data6[1]));a.append(max(data7[1]));
        b=max(a)

        ax1.set_ylim((0,b))
        ax1.legend(loc='upper left')
    if transistor == 'PMOS':  #PMOS
        a.append(min(data[1]));a.append(min(data1[1]));a.append(min(data2[1]));a.append(min(data3[1]));a.append(min(data4[1]));
        a.append(min(data5[1]));a.append(min(data6[1]));a.append(min(data7[1]));
        b=min(a)
        ax1.set_ylim((0,b))
        ax1.legend(loc='upper right')
    ax1.set_xlabel('V_gate [V]')
    ax1.set_ylabel('I_drain [A]')
    ax1.set_xlim(0,1.8)
# # # #======================  
    #ax2 = plt.subplot(212)
    slope_max_set, points_data_set, offset_set = slope_offset_set(data,data1,data2,data3,data4,data5,data6,data7)
     
    ax2.errorbar(data[0],square(data[1]),data[2],0.5 *data[3]/square(data[1]),color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
    ax2.errorbar(data1[0],square(data1[1]),data1[2],0.5 *data1[3]/square(data1[1]),'b-o',linewidth=2.0, label= '2.0/1.4')
    ax2.errorbar(data2[0],square(data2[1]),data2[2],0.5 *data2[3]/square(data2[1]),'g->',linewidth=2.0, label='2.0/0.72')
    ax2.errorbar(data3[0],square(data3[1]),data3[2],0.5 *data3[3]/square(data3[1]),'k-x',linewidth=2.0, label= '2.0/0.36')
    ax2.errorbar(data4[0],square(data4[1]),data4[2],0.5 *data4[3]/square(data4[1]),'y-<',linewidth=2.0, label= '4.0/0.18')
    ax2.errorbar(data5[0],square(data5[1]),data5[2],0.5 *data5[3]/square(data5[1]),'c-p',linewidth=2.0, label= '2.0/0.18')
    ax2.errorbar(data6[0],square(data6[1]),data6[2],0.5 *data6[3]/square(data6[1]),'m:',linewidth=2.0, label= '0.5/0.18')
    ax2.errorbar(data7[0],square(data7[1]),data7[2],0.5 *data7[3]/square(data7[1]),color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
    x = np.linspace(0,1.8)        
    ax2.plot(x,(slope_max_set[0] *x)+ offset_set[0], color="red",linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[0]/slope_max_set[0]))
    ax2.plot(x,(slope_max_set[1] *x)+ offset_set[1], 'b',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[1]/slope_max_set[1]))
    ax2.plot(x,(slope_max_set[2] *x)+ offset_set[2], 'g',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[2]/slope_max_set[2]))
    ax2.plot(x,(slope_max_set[3] *x)+ offset_set[3],'k', linewidth=2.0,label = 'Vthr %.3fV' %(-offset_set[3]/slope_max_set[3]))
    ax2.plot(x,(slope_max_set[4] *x)+ offset_set[4], 'y',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[4]/slope_max_set[4]))
    ax2.plot(x,(slope_max_set[5] *x)+ offset_set[5], 'c', linewidth=2.0,label = 'Vthr %.3fV' %(-offset_set[5]/slope_max_set[5]))
    ax2.plot(x,(slope_max_set[6] *x)+ offset_set[6], 'm', linewidth=2.0,label = 'Vthr %.3fV' %(-offset_set[6]/slope_max_set[6]))
    ax2.plot(x,(slope_max_set[7] *x)+ offset_set[7], color='Peru',linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[7]/slope_max_set[7]))  
    a1=[]
    a1.append(max(square(data[1])));a1.append(max(square(data1[1])));a1.append(max(square(data2[1])));a1.append(max(square(data3[1])));a1.append(max(square(data4[1])));
    a1.append(max(square(data5[1])));a1.append(max(square(data6[1])));a1.append(max(square(data7[1])));
    b1=max(a1)
    ax2.set_xlabel('V_gate [V]')
    ax2.set_ylabel('sqrt(I_drain) [A]')
    ax2.set_xlim((0,1.8))
    ax2.set_ylim((0,b1))
    
    if transistor == 'NMOS': #none=NMOS
        ax2.legend(loc='upper left',ncol=2,fontsize='small')
       
    if transistor == 'PMOS':  #PMOS
        ax2.legend(loc='upper right',ncol=2,fontsize='small')
    #====================== ax3
    derivative_yn_set, xn_set =derivative_set(data,data1,data2,data3,data4,data5,data6,data7)
    
    ax3.plot(xn_set[0], derivative_yn_set[0], color="red",linewidth=2.0,linestyle="--", label ='2.7/0.27')
    ax3.plot(xn_set[1], derivative_yn_set[1], 'b-o',linewidth=2.0, label = '2.0/1.4')
    ax3.plot(xn_set[2], derivative_yn_set[2], 'g->',linewidth=2.0, label = '2.0/0.72')
    ax3.plot(xn_set[3], derivative_yn_set[3],'k-x', linewidth=2.0,label = '2.0/0.36')
    ax3.plot(xn_set[4], derivative_yn_set[4], 'y-<',linewidth=2.0, label = '4.0/0.0.18')
    ax3.plot(xn_set[5], derivative_yn_set[5], 'c-p', linewidth=2.0,label = '2.0/0.18')
    ax3.plot(xn_set[6], derivative_yn_set[6], 'm:', linewidth=2.0,label = '0.5/0.18')
    ax3.plot(xn_set[7], derivative_yn_set[7], color='Peru',linewidth=2.0,linestyle='--', label = '0.22/0.18')  
    a2=[]
    a2.append(max(derivative_yn_set[0]));a2.append(max(derivative_yn_set[1]));a2.append(max(derivative_yn_set[2]));a2.append(max(derivative_yn_set[3]));a2.append(max(derivative_yn_set[4]));
    a2.append(max(derivative_yn_set[5]));a2.append(max(derivative_yn_set[6]));a2.append(max(derivative_yn_set[7]));
    b2=max(a2)
    ax3.set_xlabel('V_gate [V]')
    ax3.set_ylabel('Gm')
    ax3.set_xlim((0,1.8))
    ax3.set_ylim((0,b2))
    if transistor == 'NMOS': #none=NMOS
        ax3.legend(loc='upper left')
       
    if transistor == 'PMOS':  #PMOS
        ax3.legend(loc='upper right')
    
    #========================
    
    if transistor == 'NMOS': #none=nmos
        ax4.errorbar(data[0],data[1],data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
        ax4.errorbar(data1[0],data1[1],data1[2],data1[3],'b-o',linewidth=2.0, label= '2.0/1.4')
        ax4.errorbar(data2[0],data2[1],data2[2],data2[3],'g->',linewidth=2.0, label='2.0/0.72')
        ax4.errorbar(data3[0],data3[1],data3[2],data3[3],'k-x',linewidth=2.0, label= '2.0/0.36')
        ax4.errorbar(data4[0],data4[1],data4[2],data4[3],'y-<',linewidth=2.0, label= '4.0/0.18')
        ax4.errorbar(data5[0],data5[1],data5[2],data5[3],'c-p',linewidth=2.0, label= '2.0/0.18')
        ax4.errorbar(data6[0],data6[1],data6[2],data6[3],'m:',linewidth=2.0, label= '0.5/0.18')
        ax4.errorbar(data7[0],data7[1],data7[2],data7[3],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
        ax4.legend(loc='lower right')
    if transistor == 'PMOS':
        ax4.errorbar(data[0],fabs(data[1]),data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
        ax4.errorbar(data1[0],fabs(data1[1]),data1[2],data1[3],'b-o',linewidth=2.0, label= '2.0/1.4')
        ax4.errorbar(data2[0],fabs(data2[1]),data2[2],data2[3],'g->',linewidth=2.0, label='2.0/0.72')
        ax4.errorbar(data3[0],fabs(data3[1]),data3[2],data3[3],'k-x',linewidth=2.0, label= '2.0/0.36')
        ax4.errorbar(data4[0],fabs(data4[1]),data4[2],data4[3],'y-<',linewidth=2.0, label= '4.0/0.18')
        ax4.errorbar(data5[0],fabs(data5[1]),data5[2],data5[3],'c-p',linewidth=2.0, label= '2.0/0.18')
        ax4.errorbar(data6[0],fabs(data6[1]),data6[2],data6[3],'m:',linewidth=2.0, label= '0.5/0.18')
        ax4.errorbar(data7[0],fabs(data7[1]),data7[2],data7[3],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
        ax4.legend(loc='lower left')
        
    ax4.set_xlabel('V_gate [V]')
    ax4.set_ylabel('ln (I_drain)')
    ax4.set_xlim(0,1.8)
    ax4.set_ylim(10e-13,10e-3)
    ax4.set_yscale('log')
    plt.show()     
def global_plot_single (data, transistor= 'NMOS'):
     
     
    fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2, sharex=False, sharey=False)

     
   # ax1 = plt.subplot(211)
    #================ax1
    ax1.errorbar(data[0],data[1],data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='')
    a=[]
    if transistor == 'NMOS': #none=NMOS
        a.append(max(data[1]))
        b=max(a)

        ax1.set_ylim((0,b))
        ax1.legend(loc='upper left')
    if transistor == 'PMOS':  #PMOS
        a.append(min(data[1]))
        b=min(a)
        ax1.set_ylim((0,b))
        ax1.legend(loc='upper right')
    ax1.set_xlabel('V_gate [V]')
    ax1.set_ylabel('I_drain [A]')
    ax1.set_xlim(0,1.8)
# # # #======================  
    #ax2 = plt.subplot(212)
    slope_max_set, points_data_set, offset_set = slope_offset_set(data)
     
    ax2.errorbar(data[0],square(data[1]),data[2],0.5 *data[3]/square(data[1]),color="red", linewidth=2.0, linestyle="--", label='')
   
    x = np.linspace(0,1.8)        
    ax2.plot(x,(slope_max_set[0] *x)+ offset_set[0], color="red",linewidth=2.0, label = 'Vthr %.3fV' %(-offset_set[0]/slope_max_set[0]))
    
    a1=[]
    a1.append(max(square(data[1])))
    b1=max(a1)
    ax2.set_xlabel('V_gate [V]')
    ax2.set_ylabel('sqrt(I_drain) [A]')
    ax2.set_xlim((0,1.8))
    ax2.set_ylim((0,b1))
    
    if transistor == 'NMOS': #none=NMOS
        ax2.legend(loc='upper left',ncol=2,fontsize='small')
       
    if transistor == 'PMOS':  #PMOS
        ax2.legend(loc='upper right',ncol=2,fontsize='small')
    #====================== ax3
    derivative_yn_set, xn_set =derivative_set(data)
    
    ax3.plot(xn_set[0], derivative_yn_set[0], color="red",linewidth=2.0,linestyle="--", label ='')
   
    a2=[]
    a2.append(max(derivative_yn_set[0]));
    b2=max(a2)
    ax3.set_xlabel('V_gate [V]')
    ax3.set_ylabel('Gm')
    ax3.set_xlim((0,1.8))
    ax3.set_ylim((0,b2))
    if transistor == 'NMOS': #none=NMOS
        ax3.legend(loc='upper left')
       
    if transistor == 'PMOS':  #PMOS
        ax3.legend(loc='upper right')
    
    #========================
    
    if transistor == 'NMOS': #none=nmos
        ax4.errorbar(data[0],data[1],data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='')
        
        ax4.legend(loc='lower right')
    if transistor == 'PMOS':
        ax4.errorbar(data[0],fabs(data[1]),data[2],data[3],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
        
        ax4.legend(loc='lower left')
        
    ax4.set_xlabel('V_gate [V]')
    ax4.set_ylabel('ln (I_drain)')
    ax4.set_xlim(0,1.8)
    ax4.set_ylim(10e-13,10e-3)
    ax4.set_yscale('log')
    plt.show()     
def variable_evolution(x):   #It can be Threshold evolution, or gm or leakage. AVthr,Agm...
    variation_thr=[]
    for i in x[1]:
        variation_x1=0
        variation_x1=x[1][i]-x[1][0]
        variation_thr.append(variation_x1)
    return x[0], variation_thr

def variable_evolution_set(data_set):
    variation_thr_set=[]
    x0_set=[]
    for i in data_set:
        variation_x1_set=0
        x0val=0
        x0, variation_thr = variable_evolution(i)
        x0val=x0
        variation_x1_set=variation_thr
        x0_set.append(x0val)
        variation_thr_set.append(variation_x1_set)
    return x0_set, variation_thr_set

def variable_evolution_plot(data_set, transistor='NMOS', plot='THRESHOLD'):
    x0_set, variation_thr_set = variable_evolution_set(data_set)
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(x0_set[0], variation_thr_set[0],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
    ax.plot(x0_set[1], variation_thr_set[1],'b-o',linewidth=2.0, label= '2.0/1.4')
    ax.plot(x0_set[2], variation_thr_set[2],'g->',linewidth=2.0, label='2.0/0.72')
    ax.plot(x0_set[3], variation_thr_set[3],'k-x',linewidth=2.0, label= '2.0/0.36')
    ax.plot(x0_set[4], variation_thr_set[4],'y-<',linewidth=2.0, label= '4.0/0.18')
    ax.plot(x0_set[5], variation_thr_set[5],'c-p',linewidth=2.0, label= '2.0/0.18')
    ax.plot(x0_set[6], variation_thr_set[6],'m:',linewidth=2.0, label= '0.5/0.18')
    ax.plot(x0_set[7], variation_thr_set[7],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
    ax.set_xlabel('TID [rad]')
    ax.set_xscale('log')
##  ax.set_xlim(0,1.8)
    if plot== 'THRESHOLD': 
        ax.set_ylabel(' AVth (V)') 
    if plot== 'GM':
            ax.set_ylabel(' AGm (V)')
    if transistor == 'NMOS': #none=NMOS
# #           a=[]            
# #         a.append(max(data[1]));a.append(max(data1[1]));a.append(max(data2[1]));a.append(max(data3[1]));a.append(max(data4[1]));
# #         a.append(max(data5[1]));a.append(max(data6[1]));a.append(max(data7[1]));
# #         b=max(a)
        ax.set_ylim((-0.160, 0.000))
    if transistor == 'PMOS':  #PMOS
# #         a.append(min(data[1]));a.append(min(data1[1]));a.append(min(data2[1]));a.append(min(data3[1]));a.append(min(data4[1]));
# #         a.append(min(data5[1]));a.append(min(data6[1]));a.append(min(data7[1]));
# #         b=min(a)
        ax.set_ylim((-0.010,0.060))
    
    #plt.legend( loc='upper right', bbox_to_anchor=(0.3, 1.05), ncol=1, fancybox=True, shadow=False)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.savefig(time.strftime("/Users/Administrador/Documents/workspace/xtb01/host/plots/transistor_ch/%Y_%m_%d_%H_%M_prueba.pdf"), dpi = 300)
    plt.show()
    
def xy_set_plot(data,data1,data2,data3,data4,data5,data6,data7):
    
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(data[0],data[1],color="red", linewidth=2.0, linestyle="--", label='2.7/0.27')
    ax.plot(data1[0],data1[1],'b-o',linewidth=2.0, label= '2.0/1.4')
    ax.plot(data2[0],data2[1],'g->',linewidth=2.0, label='2.0/0.72')
    ax.plot(data3[0],data3[1],'k-x',linewidth=2.0, label= '2.0/0.36')
    ax.plot(data4[0],data4[1],'y-<',linewidth=2.0, label= '4.0/0.18')
    ax.plot(data5[0],data5[1],'c-p',linewidth=2.0, label= '2.0/0.18')
    ax.plot(data6[0],data6[1],'m:',linewidth=2.0, label= '0.5/0.18')
    ax.plot(data7[0],data7[1],color='Peru', linestyle='--',linewidth=2.0, label= '0.22/0.18')
    a=[]
    
        
        
        
    
       
    
