#! /usr/bin/env python

from ROOT import TStyle, TF1, TFile, TCanvas, gDirectory, TTree, TH1F, TH2F, THStack, TLegend, gROOT,TGraphErrors
from ROOT import RooRealVar,RooFormulaVar,RooDataHist,RooHistPdf,RooAddPdf,RooArgList,RooFit,RooMinuit,RooAbsData
from CrossSectionTable import *
import ROOT
from array import array


ROOT.gROOT.Macro("rootlogon.C")
#Hist = "nJetsHist"
Hist = "m3Hist"
HistS = "m3HistS"

c = TCanvas("c","c",600,600)
f_ttbar = TFile("plots_ttbar.root", "read") 
f_wjets = TFile("plots_wjets.root", "read") 
f_singletop_t = TFile("plots_singletop_t.root", "read") 
f_zjets = TFile("plots_zjets.root", "read")
f_data = TFile("plots_data.root", "read") 
f_qcd_data = TFile("qcd_plots_data.root", "read") 

h_ttbar_m3Hist = f_ttbar.Get(Hist)
h_wjets_m3Hist = f_wjets.Get(Hist)
h_singletop_t_m3Hist = f_singletop_t.Get(Hist)
h_zjets_m3Hist = f_zjets.Get(Hist)
h_data_m3Hist = f_data.Get(Hist)
h_qcd_data_m3Hist = f_qcd_data.Get(Hist)

h_ttbar_m3HistS = f_ttbar.Get(HistS)
h_wjets_m3HistS = f_wjets.Get(HistS)
h_singletop_t_m3HistS = f_singletop_t.Get(HistS)
h_zjets_m3HistS = f_zjets.Get(HistS)
h_data_m3HistS = f_data.Get(HistS)
h_qcd_data_m3HistS = f_qcd_data.Get(HistS)



lumi_data = 46.48  #data
lumi_ttbar = 38662 / Xsection["TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"] 
lumi_wjets = 9993300 /Xsection["WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"]  
lumi_singletop_t = 6322 / Xsection["ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1"] 
lumi_zjets = 280051 / Xsection["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"]
 
scale_ttbar = lumi_data / lumi_ttbar
scale_wjets = lumi_data / lumi_wjets
scale_singletop_t = lumi_data / lumi_singletop_t
scale_zjets = lumi_data / lumi_zjets
n_qcd =41.03

h_ttbar_m3Hist.Scale(scale_ttbar)
h_wjets_m3Hist.Scale(scale_wjets)
h_singletop_t_m3Hist.Scale(scale_singletop_t)
h_zjets_m3Hist.Scale(scale_zjets)
h_qcd_data_m3Hist.Scale(1/h_qcd_data_m3Hist.Integral()*n_qcd)

h_ttbar_m3HistS.Scale(scale_ttbar)
h_wjets_m3HistS.Scale(scale_wjets)
h_singletop_t_m3HistS.Scale(scale_singletop_t)
h_zjets_m3HistS.Scale(scale_zjets)
h_qcd_data_m3HistS.Scale(1/h_qcd_data_m3HistS.Integral()*n_qcd)



h_ttbar_m3Hist.SetFillColor(ROOT.kRed+1)
h_wjets_m3Hist.SetFillColor(ROOT.kGreen-3)
h_singletop_t_m3Hist.SetFillColor(ROOT.kMagenta)
h_zjets_m3Hist.SetFillColor(ROOT.kAzure-2)
h_qcd_data_m3Hist.SetFillColor(ROOT.kYellow)


s = THStack("hs","")
s.Add(h_ttbar_m3Hist)
s.Add(h_wjets_m3Hist)
s.Add(h_singletop_t_m3Hist)
s.Add(h_zjets_m3Hist)
s.Add(h_qcd_data_m3Hist)
s.Draw()
s.SetMaximum(65)
s.GetXaxis().SetTitle("M3 (GeV)")
s.GetYaxis().SetTitle("Number of Events")

h_data_m3Hist.Draw("sameP")
h_data_m3Hist.SetMarkerStyle(20)
h_data_m3Hist.SetMarkerSize(0.9)

n_ttbar = h_ttbar_m3Hist.Integral()
n_wjets = h_wjets_m3Hist.Integral()
n_singletop_t = h_singletop_t_m3Hist.Integral()
n_zjets = h_zjets_m3Hist.Integral()
n_background = n_ttbar + n_wjets + n_singletop_t + n_zjets
n_data = h_data_m3Hist.Integral()

print "ttbar = " + str(n_ttbar) 
print "wjets = " + str(n_wjets) 
print "singletop_t = " + str(n_singletop_t) 
print "zjets = " + str(n_zjets) 
print "background = " + str(n_background)
print "Data = " + str(n_data) 
print "QCD = " + str(n_qcd) 

l = TLegend(0.60,0.58,0.82,0.88)
l.AddEntry(h_ttbar_m3Hist,"ttbar","F")
l.AddEntry(h_wjets_m3Hist,"wjets","F")
l.AddEntry(h_singletop_t_m3Hist,"singletop","F")
l.AddEntry(h_zjets_m3Hist,"zjets","F")
l.AddEntry(h_qcd_data_m3Hist,"qcd","F")
l.AddEntry(h_data_m3Hist,"data","P")
l.SetTextSize(0.05);
l.SetLineColor(0);
l.SetFillColor(0);
l.Draw()

hmctotqcd = h_ttbar_m3HistS.Clone("hmctotqcd")
hmctotqcd.Add(h_wjets_m3HistS)
hmctotqcd.Add(h_singletop_t_m3HistS)
hmctotqcd.Add(h_zjets_m3HistS)
hmctotqcd.Add(h_qcd_data_m3HistS)

xx=[]
xxer=[]
yy=[]
yyer=[]
for i in range(0, hmctotqcd.GetNbinsX()+2 ):
  yy.append(  float(hmctotqcd.GetBinContent(i)))
  yyer.append(float(hmctotqcd.GetBinError(i)))
  xx.append(  float(hmctotqcd.GetBinCenter(i)))
  xxer.append(float(hmctotqcd.GetBinWidth(i)/2))

x_   = array("d",xx)
xer = array("d",xxer)
y_   = array("d",yy)
yer = array("d",yyer)
gr = TGraphErrors(len(x_), x_,y_,xer,yer)
gr.SetFillColor(ROOT.kBlack);
#gr.SetFillStyle(3144);
gr.SetFillStyle(3244);
gr.Draw("same,2")


c.Print("m3Hist.png")

h_background_m3Hist=h_wjets_m3HistS.Clone("h_background_m3Hist")
#h_background_m3Hist.Add(h_wjets_m3Hist)
h_background_m3Hist.Add(h_singletop_t_m3HistS)
h_background_m3Hist.Add(h_zjets_m3HistS)

rttbar = n_ttbar/(n_ttbar+n_background)#+n_qcd)

x=RooRealVar("x","x",h_zjets_m3Hist.GetXaxis().GetXmin(),h_zjets_m3Hist.GetXaxis().GetXmax()) 
k2=RooRealVar("k2","normalization factor", 1.0, 0.5, 1.5) 
k1 =RooRealVar("k1","k1",rttbar,0.,0.5);
#k2 =RooRealVar("k2","k2",rQCD,0.0,0.2);

nttbar =RooRealVar("nttbar","number of ttbar events", n_ttbar , n_ttbar, n_ttbar)
k1nttbar=RooFormulaVar("k1nttbar","number of ttbar events after fitting","k*nttbar",RooArgList(k1,nttbar) )

n_mc = n_ttbar+n_background
nmc = RooRealVar("nmc","number of mc events", n_mc , n_mc, n_mc)
k2nmc = RooFormulaVar("k2nmc","number of mc events"," ",RooArgList(k2,nmc))
#RooRealVar    nbackground("nbackground","number of background events", n_background , n_background, n_background);
#RooFormulaVar k2background("k2background","number of background events after fitting","k2*nbackground",RooArgList(k2,nbackground) );
nqcd = RooRealVar("nqcd","number of qcd events", n_qcd , n_qcd, n_qcd)
#k2nqcd = RooFormulaVar("k2nqcd","number of qcd events"," ",RooArgList(k2,nqcd))

data       = RooDataHist("data",      "data set with (x)", RooArgList(x), h_data_m3HistS)
ttbar      = RooDataHist("ttbar",     "data set with (x)", RooArgList(x), h_ttbar_m3HistS)
background = RooDataHist("background","data set with (x)", RooArgList(x), h_background_m3Hist)

qcd        = RooDataHist("qcd",      "data set with (x)", RooArgList(x), h_qcd_data_m3HistS)
# RooHistPdf::RooHistPdf(const char* name, const char* title, const RooArgSet& vars, const RooDataHist& dhist, int intOrder = 0) =>
#print "ttbar type: "+str(type(ttbar))
#print "rooArglist(x):"+str(type(RooArgList(x)))

ttbarpdf      = RooHistPdf("ttbarpdf",     "ttbarpdf",      RooArgList(x), RooArgList(x), ttbar)
backgroundpdf = RooHistPdf("backgroundpdf","backgroundpdf", RooArgList(x), RooArgList(x), background)
qcdpdf        = RooHistPdf("qcdpdf",       "qcdpdf",        RooArgList(x), RooArgList(x), qcd)

#ttbarpdf      = RooHistPdf(ttbar,"ttbarpdf")
#backgroundpdf = RooHistPdf(background,"backgroundpdf")

model = RooAddPdf("model", "model",RooArgList( ttbarpdf, backgroundpdf), RooArgList(k1))
model2 = RooAddPdf("model2", "model2",RooArgList( model), RooArgList(k2nmc))
model3 = RooAddPdf("model3", "model3",RooArgList( model2, qcdpdf), RooArgList(k2nmc,nqcd))
#model3 = RooAddPdf("model3", "model3",RooArgList( model, qcdpdf), RooArgList(k2nmc,k2nqcd))

model3.fitTo(data)

#nk1 = model3.createNLL(data)
#RooMinuit(nk1).migrad() 
#Rk1 = k2.frame()

#nk1.plotOn(Rk1,RooFit.ShiftToZero()) 
#cRcc = TCanvas("Rcc", "Rcc", 500, 500)

#Rk1.SetMaximum(4.);Rk1.SetMinimum(0)
#Rk1.GetXaxis().SetTitle("nttbar/nmc")
#Rk1.SetTitle("")
#Rk1.Draw()

cR11 = TCanvas("R11", "R", 500, 500)
xframe = x.frame()
data.plotOn(xframe, RooFit.DataError(RooAbsData.SumW2) ) 
model3.paramOn(xframe, RooFit.Layout(0.65,0.9,0.9) )
model3.plotOn(xframe)
chi2 = xframe.chiSquare(2)
ndof = xframe.GetNbinsX()
print "chi2 = "+ str(chi2)
print "ndof = "+ str(ndof)
xframe.Draw()



print "k1:"+str(k1.getVal())+", err:"+str(k1.getError())+", init:"+str(rttbar)
print "k2:"+str(k2.getVal())+", err:"+str(k2.getError())
n_mctotal = n_ttbar+n_background

print "####################"
print "ttbar = " + str(n_ttbar) 
print "wjets = " + str(n_wjets) 
print "singletop_t = " + str(n_singletop_t) 
print "zjets = " + str(n_zjets) 
print "background = " + str(n_background)
print "mctotal = " +str(n_mctotal)
print "Data = " + str(n_data) 
print "QCD = " + str(n_qcd) 
print "####################"

n_ttbar2 = ((n_ttbar+n_background)*k1.getVal())*k2.getVal()
n_wjets2 = (n_wjets/n_background)*(n_ttbar+n_background)*(1-k1.getVal())*k2.getVal()
n_singletop_t2 = (n_singletop_t/n_background)*(n_ttbar+n_background)*(1-k1.getVal())*k2.getVal()
n_zjets2 = (n_zjets/n_background)*(n_ttbar+n_background)*(1-k1.getVal())*k2.getVal()
n_background2 = (n_ttbar+n_background)*(1-k1.getVal())*k2.getVal()
n_mctotal2 = n_ttbar2+n_background2
print "ttbar = " + str(n_ttbar2) 
print "wjets = " + str(n_wjets2) 
print "singletop_t = " + str(n_singletop_t2) 
print "zjets = " + str(n_zjets2) 
print "background = " + str(n_background2)
print "mctotal = " +str(n_mctotal2)
print "Data = " + str(n_data) 
print "QCD = " + str(n_qcd) 
print "####################"

h_ttbar_m3Hist2       =h_ttbar_m3Hist      .Clone("ttbarN")
h_wjets_m3Hist2       =h_wjets_m3Hist      .Clone("wjetsN")
h_singletop_t_m3Hist2 =h_singletop_t_m3Hist.Clone("stopN")
h_zjets_m3Hist2       =h_zjets_m3Hist      .Clone("zjetsN")
h_qcd_data_m3Hist2    =h_qcd_data_m3Hist   .Clone("qcdN")

h_ttbar_m3Hist2      .Scale(1/h_ttbar_m3Hist2      .Integral()*n_ttbar2)
h_wjets_m3Hist2      .Scale(1/h_wjets_m3Hist2      .Integral()*n_wjets2)  
h_singletop_t_m3Hist2.Scale(1/h_singletop_t_m3Hist2.Integral()*n_singletop_t2)
h_zjets_m3Hist2      .Scale(1/h_zjets_m3Hist2      .Integral()*n_zjets2)

c2 = TCanvas("c2","c",600,600)
s = THStack("hs","")
s.Add(h_ttbar_m3Hist2      )
s.Add(h_wjets_m3Hist2      )
s.Add(h_singletop_t_m3Hist2)
s.Add(h_zjets_m3Hist2      )
s.Add(h_qcd_data_m3Hist2   ) 
s.Draw()
s.SetMaximum(65)
s.GetXaxis().SetTitle("M3 (GeV)")
s.GetYaxis().SetTitle("Number of Events")

h_data_m3Hist.Draw("sameP")
h_data_m3Hist.SetMarkerStyle(20)
h_data_m3Hist.SetMarkerSize(0.9)

l = TLegend(0.60,0.58,0.82,0.88)
l.AddEntry(h_ttbar_m3Hist2,"ttbar","F")
l.AddEntry(h_wjets_m3Hist2,"wjets","F")
l.AddEntry(h_singletop_t_m3Hist2,"singletop","F")
l.AddEntry(h_zjets_m3Hist2,"zjets","F")
l.AddEntry(h_qcd_data_m3Hist2,"qcd","F")
l.AddEntry(h_data_m3Hist,"data","P")
l.SetTextSize(0.05);
l.SetLineColor(0);
l.SetFillColor(0);
l.Draw()

h_ttbar_m3Hist2S       =h_ttbar_m3HistS      .Clone("ttbarNS")
h_wjets_m3Hist2S       =h_wjets_m3HistS      .Clone("wjetsNS")
h_singletop_t_m3Hist2S =h_singletop_t_m3HistS.Clone("stopNS")
h_zjets_m3Hist2S       =h_zjets_m3HistS      .Clone("zjetsNS")
h_qcd_data_m3Hist2S    =h_qcd_data_m3HistS   .Clone("qcdNS")

h_ttbar_m3Hist2S      .Scale(1/h_ttbar_m3Hist2S      .Integral()*n_ttbar2)
h_wjets_m3Hist2S      .Scale(1/h_wjets_m3Hist2S      .Integral()*n_wjets2)  
h_singletop_t_m3Hist2S.Scale(1/h_singletop_t_m3Hist2S.Integral()*n_singletop_t2)
h_zjets_m3Hist2S      .Scale(1/h_zjets_m3Hist2S      .Integral()*n_zjets2)

hmctotqcd2 = h_ttbar_m3Hist2S.Clone("hmctotqcd")
hmctotqcd2.Add(h_wjets_m3Hist2S)
hmctotqcd2.Add(h_singletop_t_m3Hist2S)
hmctotqcd2.Add(h_zjets_m3Hist2S)
hmctotqcd2.Add(h_qcd_data_m3HistS)

xx2=[]
xxer2=[]
yy2=[]
yyer2=[]
for i in range(0, hmctotqcd2.GetNbinsX()+2 ):
  yy2.append(  float(hmctotqcd2.GetBinContent(i)))
  yyer2.append(float(hmctotqcd2.GetBinError(i)))
  xx2.append(  float(hmctotqcd2.GetBinCenter(i)))
  xxer2.append(float(hmctotqcd2.GetBinWidth(i)/2))

x2_   = array("d",xx2)
xer2 = array("d",xxer2)
y2_   = array("d",yy2)
yer2 = array("d",yyer2)
gr2 = TGraphErrors(len(x2_), x2_,y2_,xer2,yer2)
gr2.SetFillColor(ROOT.kBlack);
#gr2.SetFillStyle(3144);
gr2.SetFillStyle(3244);
gr2.Draw("same,2")

c.Print("m3HistNew.png")


