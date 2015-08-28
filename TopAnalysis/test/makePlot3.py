#! /usr/bin/env python

from ROOT import TStyle, TF1, TFile, TCanvas, gDirectory, TTree, TH1F, TH2F, THStack, TLegend, gROOT 
from ROOT import RooRealVar,RooFormulaVar,RooDataHist,RooHistPdf,RooAddPdf,RooArgList,RooFit,RooMinuit
from CrossSectionTable import *
import ROOT
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
lumi_wjets = 2859761 /Xsection["WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"]  
lumi_singletop_t = 6322 / Xsection["ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1"] 
lumi_zjets = 280051 / Xsection["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"]
 
scale_ttbar = lumi_data / lumi_ttbar
scale_wjets = lumi_data / lumi_wjets
scale_singletop_t = lumi_data / lumi_singletop_t
scale_zjets = lumi_data / lumi_zjets
n_qcd =37.03

h_ttbar_m3Hist.Scale(scale_ttbar)
h_wjets_m3Hist.Scale(scale_wjets)
h_singletop_t_m3Hist.Scale(scale_singletop_t)
h_zjets_m3Hist.Scale(scale_zjets)
h_qcd_data_m3Hist.Scale(1/h_qcd_data_m3Hist.Integral()*n_qcd)

h_ttbar_m3HistS.Scale(scale_ttbar)
h_wjets_m3HistS.Scale(scale_wjets)
h_singletop_t_m3HistS.Scale(scale_singletop_t)
h_zjets_m3HistS.Scale(scale_zjets)
h_qcd_data_m3HistS.Scale(1/h_qcd_data_m3Hist.Integral()*n_qcd)

h_ttbar_m3Hist.SetFillColor(ROOT.kRed+1)
h_wjets_m3Hist.SetFillColor(ROOT.kGreen-3)
h_singletop_t_m3Hist.SetFillColor(ROOT.kMagenta)
h_zjets_m3Hist.SetFillColor(ROOT.kAzure-2)
h_qcd_data_m3Hist.SetFillColor(ROOT.kYellow)


s = THStack("hs","")
#s.Add(h_ttbar_m3Hist)
s.Add(h_wjets_m3Hist)
s.Add(h_singletop_t_m3Hist)
s.Add(h_zjets_m3Hist)
s.Add(h_qcd_data_m3Hist)
s.Draw()
#s.SetMaximum(65)
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
print "QCD = " + str(37.03) 

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
background = RooDataHist("background","data set with (x)", RooArgList(x), h_background_m3HistS)

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


print "k1:"+str(k1.getVal())+", err:"+str(k1.getError())+", init:"+str(rttbar)
print "k2:"+str(k2.getVal())+", err:"+str(k2.getError())


