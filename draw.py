import ROOT
import sys,math
from array import array
from DataPoint import DataPoint
from DataSetAnalysis import DataSet
from VisualizeData import Visualizer
import numpy as np
PMOS=False
#-----------------------------------------
def Style():
    ROOT.gROOT.LoadMacro('/Users/schae/testarea/CAFAna/HWWMVACode/atlasstyle-00-03-05/AtlasStyle.C')                   
    ROOT.gROOT.LoadMacro('/Users/schae/testarea/CAFAna/HWWMVACode/atlasstyle-00-03-05/AtlasUtils.C')
    ROOT.SetAtlasStyle()
#-----------------------------------------------------------------------------
# Load necessary shared libraries
#
def setPlotDefaults(root, options = None):

    #root.gROOT.SetStyle('Plain')

    root.gStyle.SetFillColor(10)           
    root.gStyle.SetFrameFillColor(10)      
    root.gStyle.SetCanvasColor(10)         
    root.gStyle.SetPadColor(10)            
    root.gStyle.SetTitleFillColor(0)       
    root.gStyle.SetStatColor(10)   
    
    root.gStyle.SetCanvasBorderMode(0)
    root.gStyle.SetFrameBorderMode(0) 
    root.gStyle.SetPadBorderMode(0)   
    root.gStyle.SetDrawBorder(0)      
    root.gStyle.SetTitleBorderSize(0)
    
    root.gStyle.SetFuncWidth(2)
    root.gStyle.SetHistLineWidth(2)
    root.gStyle.SetFuncColor(2)
    
    root.gStyle.SetPadTopMargin(0.08)
    root.gStyle.SetPadBottomMargin(0.16)
    root.gStyle.SetPadLeftMargin(0.16)
    root.gStyle.SetPadRightMargin(0.12)
  
    # set axis ticks on top and right
    root.gStyle.SetPadTickX(1)         
    root.gStyle.SetPadTickY(1)         
  
    # Set the background color to white
    root.gStyle.SetFillColor(10)           
    root.gStyle.SetFrameFillColor(10)      
    root.gStyle.SetCanvasColor(10)         
    root.gStyle.SetPadColor(10)            
    root.gStyle.SetTitleFillColor(0)       
    root.gStyle.SetStatColor(10)           
  
  
    # Turn off all borders
    root.gStyle.SetCanvasBorderMode(0)
    root.gStyle.SetFrameBorderMode(0) 
    root.gStyle.SetPadBorderMode(0)   
    root.gStyle.SetDrawBorder(0)      
    root.gStyle.SetTitleBorderSize(0) 
  
    # Set the size of the default canvas
    root.gStyle.SetCanvasDefH(400)          
    root.gStyle.SetCanvasDefW(650)          
    #gStyle->SetCanvasDefX(10)
    #gStyle->SetCanvasDefY(10)   
  
    # Set fonts
    font = 42
    #root.gStyle.SetLabelFont(font,'xyz')
    #root.gStyle.SetStatFont(font)       
    #root.gStyle.SetTitleFont(font)      
    #root.gStyle.SetTitleFont(font,'xyz')
    #root.gStyle.SetTextFont(font)       
    #root.gStyle.SetTitleX(0.3)        
    #root.gStyle.SetTitleW(0.4)        
  
   # Set Line Widths
   #gStyle->SetFrameLineWidth(0)
   #root.gStyle.SetFuncWidth(2)
   #root.gStyle.SetHistLineWidth(2)
   #root.gStyle.SetFuncColor(2)
   #
   # Set tick marks and turn off grids
    root.gStyle.SetNdivisions(505,'xyz')
   #
   # Set Data/Stat/... and other options
   #root.gStyle.SetOptDate(0)
   #root.gStyle.SetDateX(0.1)
   #root.gStyle.SetDateY(0.1)
   #gStyle->SetOptFile(0)
   ##root.gStyle.SetOptStat(1110)
    root.gStyle.SetOptStat(1111)
    #root.gStyle.SetOptFit(111)
    root.gStyle.SetStatFormat('4.3f')
    root.gStyle.SetFitFormat('4.3f')
   #gStyle->SetStatTextColor(1)
   #gStyle->SetStatColor(1)
   #gStyle->SetOptFit(1)
   #gStyle->SetStatH(0.20)
   #gStyle->SetStatStyle(0)
   #gStyle->SetStatW(0.30)
   #gStyle -SetStatLineColor(0)
   #root.gStyle.SetStatX(0.919)
   #root.gStyle.SetStatY(0.919)
   #root.gStyle.SetOptTitle(0)
   #gStyle->SetStatStyle(0000)    # transparent mode of Stats PaveLabel
   #root.gStyle.SetStatBorderSize(0)
   #
    #root.gStyle.SetLabelSize(0.065,'xyz')
    #gStyle -> SetLabelOffset(0.005,'xyz')
    #root.gStyle.SetTitleY(.5)
    root.gStyle.SetTitleOffset(1.0,'xz')
    root.gStyle.SetTitleOffset(1.1,'y')
    root.gStyle.SetTitleSize(0.065, 'xyz')
    root.gStyle.SetLabelSize(0.065, 'xyz')
    #root.gStyle.SetTextAlign(22)
    root.gStyle.SetTextSize(0.1)
   #
   ##root.gStyle.SetPaperSize(root.TStyle.kA4)  
    root.gStyle.SetPalette(1)
   #
   ##root.gStyle.SetHistMinimumZero(True)
   
    root.gROOT.ForceStyle()
def Parse(fname):

    f=open(fname,'r')
    info = []
    for i in f:
        if i and not i.count('I') and not i.count('['):
            tmp = i.rstrip('\n').split(' ')
            stmp=[]
            for t in tmp:
                #print 'var: ',t
                try:
                    stmp+=[float(t)]
                except:
                    print 'Could not convert to a float: ',t
                    sys.exit(0)
            info+=[stmp]
            #print info
    return info

def GetTGraph(info,name='gr1',color=1):
    # Create histogram of trigger rate vs. run#
    #bins = sorted([148864, 149291, 146436, 148822, 149063])
    #runArray = array('d',bins)
    #histogram = TH1F("hist", "HLT Rate", len(runArray)-1, runArray)
    max_y = 0.0
    max_ysq = 0.0    
    
    bins_Id=[]
    bins_Idsq=[]    
    bins_Vg=[]
    bins_Iderr=[]
    bins_Idsqerr=[]    
    bins_Vgerr=[]

    
    if PMOS:
        max_vg=0.0
        for i in info:
            if i[0]>max_vg:
                max_vg = i[0]
        print 'PMOS we are subtracting the following: ',max_vg
        for i in info:
            i[0]=max_vg-i[0]
            #i[2]=1.5-i[2]
            #i[0]=1.5-i[0]
    for i in info:
        if i[1]>max_y:
            max_y = i[1]
        if math.sqrt(i[1])>max_ysq:
            max_ysq = math.sqrt(i[1])
        if True:
            bins_Vg+=[i[0]]
            bins_Id+=[i[1]]
            bins_Idsq+=[math.sqrt(i[1])]
            bins_Vgerr+=[i[2]]
            bins_Iderr+=[i[3]]
            bins_Idsqerr+=[math.sqrt(i[3])]
        else:
            bins_Vg=[i[0]]+bins_Vg
            bins_Id+=[i[1]]
            bins_Idsq+=[math.sqrt(i[1])]
            bins_Vgerr=[i[2]]+bins_Vgerr
            bins_Iderr+=[i[3]]
            bins_Idsqerr+=[math.sqrt(i[3])]
        
    runArray_Id = array('d',bins_Id)
    runArray_Idsq = array('d',bins_Idsq)    
    runArray_Vg = array('d',bins_Vg)    
    runArray_Iderr = array('d',bins_Iderr)
    runArray_Idsqerr = array('d',bins_Idsqerr)
    runArray_Vgerr = array('d',bins_Vgerr)
    
    gr1 = ROOT.TGraphErrors(int(len(bins_Id)-1),runArray_Vg,runArray_Id,runArray_Vgerr,runArray_Iderr);
    gr1.SetName(name);
    gr1.SetTitle("Drain Current Vs Gate Bias");
    gr1.GetYaxis().SetTitleOffset(1.60);
    gr1.GetXaxis().SetTitle("Gate Voltage [V]");
    gr1.GetYaxis().SetTitle("Drain Current [A]");
    gr1.GetYaxis().SetRangeUser(0.0,1.3*max_y);
    gr1.GetXaxis().SetRangeUser(0.0,2.0);    
    gr1.SetMarkerColor(color);
    gr1.SetLineColor(color);
    gr1.SetFillColor(0);
    
    gr1.SetLineWidth(2);
    gr1.SetMarkerStyle(22);

    grsq = ROOT.TGraphErrors(int(len(bins_Id)-1),runArray_Vg,runArray_Idsq,runArray_Vgerr,runArray_Idsqerr);
    grsq.SetName(name+'sq');
    grsq.SetTitle("Drain Current Vs Gate Bias");
    grsq.GetYaxis().SetTitleOffset(1.60);
    grsq.GetXaxis().SetTitle("Gate Voltage [V]");
    grsq.GetYaxis().SetTitle("#sqrt{Drain Current [A]}");
    grsq.GetYaxis().SetRangeUser(0.0,1.3*max_ysq);
    grsq.GetXaxis().SetRangeUser(0.0,2.0);    
    grsq.SetMarkerColor(color);
    grsq.SetLineColor(color);
    grsq.SetFillColor(0);

    grsq.SetLineWidth(2);
    grsq.SetMarkerStyle(22);      
    return gr1,grsq

def Plot(fname1='run/out_chip2_nmos2_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
         fname2='run/beforeIrradiation/test_chip2_pmos5_drain1_5v_vddat1_5v_gnadtfloating.txt'):
    # Process
    info = Parse(fname1)
    #info = Parse('run/out_chip1_pmos8_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradproper.txt')
    info2 = Parse(fname2)
    #info = Parse('run/beforeIrradiation/test_chip3_pmos5_drain1_5v_vddat1_5v_gnadtfloating.txt')
    #setPlotDefaults(ROOT)
    Style()
    c1 = ROOT.TCanvas("c1","testbeam efficiency",50,50,600,600);
    mg = ROOT.TMultiGraph();
    
    gr1,gr1sq = GetTGraph(info,color=1)
    gr2,gr2sq = GetTGraph(info2,'gr2',color=2)
    gr1sq.Draw();
    #gr2.Draw('same')
    
    leg = ROOT.TLegend(0.45, 0.2, 0.85, 0.4);
    leg.SetBorderSize(0);
    leg.SetFillStyle(0);
    #leg.AddEntry(gr3, "60V Bias");        
    #leg.AddEntry(gr2, "90V Bias");    
    leg.AddEntry(gr1, "PMOS");
    leg.Draw();
    
    c1.Update();
    c1.WaitPrimitive();
    
    data=[]
    for i in info:
        d = DataPoint(i[0],i[1],i[2],i[3])
        data+=[d]
    dset = DataSet(data,'data')
    dset.set_transistor_dimensions(4.0, 0.18)
    dset.calc_characteristics()
    
    print 'Vthr: ',dset._vthr
    print dset.get_characteristics()
    
    vis = Visualizer('title', '2 1')    
    vis.add_plot(dset, ty='rawData', ind='0 0')
    vis.add_plot(dset, ty='sqData', ind='1 0')
    vis.get_plot()
    #raw_input('wait')   
    
    #h = ROOT.TFile.

flist = [
#'run/out_chip1_nmos1_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip1_nmos2_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip1_nmos3_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip1_nmos4_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip1_pmos5_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradproper.txt',
#'run/out_chip1_pmos6_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradproper.txt',
#'run/out_chip1_pmos7_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange2.txt', 
#'run/out_chip1_pmos8_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradproper.txt',

#'run/out_chip2_nmos1_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange.txt',
#'run/out_chip2_nmos2_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange.txt',
#'run/out_chip2_nmos3_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip2_nmos4_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip2_pmos5_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange.txt',
#'run/out_chip2_pmos6_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip2_pmos7_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange2.txt', 
#'run/out_chip2_pmos8_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#
'run/out_chip3_pmos5_drain1_5v_vddat1_5v_gnadtgrounded_rad0KradTest.txt',
#'run/beforeIrr2/out_chip3_nmos1_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/beforeIrr2/out_chip3_nmos2_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip3_nmos1_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip3_nmos2_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip3_nmos3_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip3_nmos4_drain1_5v_vddat1_5v_gnadtgrounded_rad0Krad.txt',
#'run/out_chip3_pmos5_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange.txt',
#'run/out_chip3_pmos6_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange.txt',
#'run/out_chip3_pmos7_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange.txt', 
#'run/out_chip3_pmos8_drain1_5v_vddat1_5v_gnadtgrounded_rad0Kradrange.txt',
        ]
    
for i in flist:
    print i
    if i.count('pmos'):
        PMOS=True
    else:
        PMOS=False
    Plot(fname1=i,
        fname2='run/beforeIrradiation/test_chip2_pmos5_drain1_5v_vddat1_5v_gnadtfloating.txt')
