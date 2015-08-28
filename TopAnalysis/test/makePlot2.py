#! /usr/bin/env python

from ROOT import TStyle, TF1, TFile, TCanvas, gDirectory, TTree, TH1F, TH2F, THStack, TLegend, gROOT 
from CrossSectionTable import *
import ROOT
ROOT.gROOT.Macro("rootlogon.C")

f_ttbar = TFile("plots_ttbar.root", "read") 
f_wjets = TFile("plots_wjets.root", "read") 
f_singletop_t = TFile("plots_singletop_t.root", "read") 
f_zjets = TFile("plots_zjets.root", "read")
f_data = TFile("plots_data.root", "read") 
f_qcd = TFile("qcd_plots_data.root", "read") 

histname="metVsIso"
h_ttbar_m3Hist = f_ttbar.Get(histname)
h_wjets_m3Hist = f_wjets.Get(histname)
h_singletop_t_m3Hist = f_singletop_t.Get(histname)
h_zjets_m3Hist = f_zjets.Get(histname)
h_data_m3Hist = f_data.Get(histname)
h_qcd_data_m3Hist = f_qcd.Get(histname)

lumi_data = 46.48  #data
lumi_ttbar = 38662 / Xsection["TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"] 
lumi_wjets = 9993300 /Xsection["WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"]  
lumi_singletop_t = 6322 / Xsection["ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1"] 
lumi_zjets = 280051 / Xsection["DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"]

h_ttbar_m3Hist.SetTitle("ttbar")
h_wjets_m3Hist.SetTitle("wjet")
h_singletop_t_m3Hist.SetTitle("single top")
h_zjets_m3Hist.SetTitle("zjets")
h_data_m3Hist.SetTitle("DATA")
h_qcd_data_m3Hist.SetTitle("qcd")

scale_ttbar = lumi_data / lumi_ttbar
scale_wjets = lumi_data / lumi_wjets
scale_singletop_t = lumi_data / lumi_singletop_t
scale_zjets = lumi_data / lumi_zjets

h_ttbar_m3Hist.Scale(scale_ttbar)
h_wjets_m3Hist.Scale(scale_wjets)
h_singletop_t_m3Hist.Scale(scale_singletop_t)
h_zjets_m3Hist.Scale(scale_zjets)

#h_ttbar_m3Hist.SetFillColor(ROOT.kRed+1)
#h_wjets_m3Hist.SetFillColor(ROOT.kGreen-3)
#h_singletop_t_m3Hist.SetFillColor(ROOT.kMagenta)
#h_zjets_m3Hist.SetFillColor(ROOT.kAzure-2)

#s = THStack("hs","")
#s.Add(h_ttbar_m3Hist)
#s.Add(h_wjets_m3Hist)
#s.Add(h_singletop_t_m3Hist)
#s.Add(h_zjets_m3Hist)
#s.Draw()
#s.SetMaximum(65)
#s.GetXaxis().SetTitle("M3 (GeV)")
#s.GetYaxis().SetTitle("Number of Events")

#h_data_m3Hist.Draw("sameP")
#h_data_m3Hist.SetMarkerStyle(20)
#h_data_m3Hist.SetMarkerSize(0.9)

c = TCanvas("c","c",900,600)
c.Divide(3,2)
c.cd(1)
h_ttbar_m3Hist.Draw()
c.cd(2)
h_wjets_m3Hist.Draw()
c.cd(3)
h_singletop_t_m3Hist.Draw()
c.cd(4)
h_zjets_m3Hist.Draw()
c.cd(5)
h_qcd_data_m3Hist.Draw()
c.cd(6)
h_data_m3Hist.Draw()

AminX=h_data_m3Hist.GetXaxis().FindBin(20)+1
AmaxX=h_data_m3Hist.GetXaxis().FindBin(150)
AminY=h_data_m3Hist.GetYaxis().FindBin(0)
AmaxY=h_data_m3Hist.GetYaxis().FindBin(0.12)

BminX=h_data_m3Hist.GetXaxis().FindBin(0)
BmaxX=h_data_m3Hist.GetXaxis().FindBin(20)
BminY=h_data_m3Hist.GetYaxis().FindBin(0)
BmaxY=h_data_m3Hist.GetYaxis().FindBin(0.12)

CminX=h_data_m3Hist.GetXaxis().FindBin(20)+1
CmaxX=h_data_m3Hist.GetXaxis().FindBin(150)
CminY=h_data_m3Hist.GetYaxis().FindBin(0.12)+1
CmaxY=h_data_m3Hist.GetYaxis().FindBin(2.5)

DminX=h_data_m3Hist.GetXaxis().FindBin(0)
DmaxX=h_data_m3Hist.GetXaxis().FindBin(20)
DminY=h_data_m3Hist.GetYaxis().FindBin(0.12)+1
DmaxY=h_data_m3Hist.GetYaxis().FindBin(2.5)

n_ttbarA = h_ttbar_m3Hist.Integral(AminX,AmaxY,AminY,AmaxY)
n_ttbarB = h_ttbar_m3Hist.Integral(BminX,BmaxY,BminY,BmaxY)
n_ttbarC = h_ttbar_m3Hist.Integral(CminX,CmaxY,CminY,CmaxY)
n_ttbarD = h_ttbar_m3Hist.Integral(DminX,DmaxY,DminY,DmaxY)

n_wjetsA = h_wjets_m3Hist.Integral(AminX,AmaxY,AminY,AmaxY)
n_wjetsB = h_wjets_m3Hist.Integral(BminX,BmaxY,BminY,BmaxY)
n_wjetsC = h_wjets_m3Hist.Integral(CminX,CmaxY,CminY,CmaxY)
n_wjetsD = h_wjets_m3Hist.Integral(DminX,DmaxY,DminY,DmaxY)

n_singletop_tA = h_singletop_t_m3Hist.Integral(AminX,AmaxY,AminY,AmaxY)
n_singletop_tB = h_singletop_t_m3Hist.Integral(BminX,BmaxY,BminY,BmaxY)
n_singletop_tC = h_singletop_t_m3Hist.Integral(CminX,CmaxY,CminY,CmaxY)
n_singletop_tD = h_singletop_t_m3Hist.Integral(DminX,DmaxY,DminY,DmaxY)

n_zjetsA = h_zjets_m3Hist.Integral(AminX,AmaxY,AminY,AmaxY)
n_zjetsB = h_zjets_m3Hist.Integral(BminX,BmaxY,BminY,BmaxY)
n_zjetsC = h_zjets_m3Hist.Integral(CminX,CmaxY,CminY,CmaxY)
n_zjetsD = h_zjets_m3Hist.Integral(DminX,DmaxY,DminY,DmaxY)

n_backgroundA = n_ttbarA + n_wjetsA + n_singletop_tA + n_zjetsA
n_backgroundB = n_ttbarB + n_wjetsB + n_singletop_tB + n_zjetsB
n_backgroundC = n_ttbarC + n_wjetsC + n_singletop_tC + n_zjetsC
n_backgroundD = n_ttbarD + n_wjetsD + n_singletop_tD + n_zjetsD

n_dataA = h_data_m3Hist.Integral(AminX,AmaxY,AminY,AmaxY)
n_dataB = h_data_m3Hist.Integral(BminX,BmaxY,BminY,BmaxY)
n_dataC = h_data_m3Hist.Integral(CminX,CmaxY,CminY,CmaxY)
n_dataD = h_data_m3Hist.Integral(DminX,DmaxY,DminY,DmaxY)

n_qcd_dataA = h_qcd_data_m3Hist.Integral(AminX,AmaxY,AminY,AmaxY)
n_qcd_dataB = h_qcd_data_m3Hist.Integral(BminX,BmaxY,BminY,BmaxY)
n_qcd_dataC = h_qcd_data_m3Hist.Integral(CminX,CmaxY,CminY,CmaxY)
n_qcd_dataD = h_qcd_data_m3Hist.Integral(DminX,DmaxY,DminY,DmaxY)


print "ttbar =      (" + str(round(n_ttbarA))       + ", " + str(round(n_ttbarB)      ) + ", "+ str(round(n_ttbarC)      ) + ", "+ str(round(n_ttbarD)      ) + ") "
print "wjets =      (" + str(round(n_wjetsA))       + ", " + str(round(n_wjetsB)      ) + ", "+ str(round(n_wjetsC)      ) + ", "+ str(round(n_wjetsD)      ) + ") "
print "singletop_t =(" + str(round(n_singletop_tA)) + ", " + str(round(n_singletop_tB)) + ", "+ str(round(n_singletop_tC)) + ", "+ str(round(n_singletop_tD)) + ") "
print "zjets =      (" + str(round(n_zjetsA))       + ", " + str(round(n_zjetsB)      ) + ", "+ str(round(n_zjetsC)      ) + ", "+ str(round(n_zjetsD)      ) + ") "
print "background = (" + str(round(n_backgroundA))  + ", " + str(round(n_backgroundB) ) + ", "+ str(round(n_backgroundC) ) + ", "+ str(round(n_backgroundD) ) + ") " 
print "Data =       (" + str(round(n_dataA))        + ", " + str(round(n_dataB)       ) + ", "+ str(round(n_dataC)       ) + ", "+ str(round(n_dataD)       ) + ") " 
print "QCD =        (" + str(round( (n_dataB-n_backgroundB)/(n_dataD-n_backgroundD)*(n_dataC-n_backgroundC)*100)/100) + ") "

#N_qcd = (Nb;data - Nb;mc)/(Nd;data-Nd;mc)*(Nc;Data-Nc;mc)

#l = TLegend(0.60,0.58,0.82,0.88)
#l.AddEntry(h_ttbar_m3Hist,"ttbar","F")
#l.AddEntry(h_wjets_m3Hist,"wjets","F")
#l.AddEntry(h_singletop_t_m3Hist,"singletop","F")
#l.AddEntry(h_zjets_m3Hist,"zjets","F")
#l.AddEntry(h_data_m3Hist,"data","P")
#l.SetTextSize(0.05);
#l.SetLineColor(0);
#l.SetFillColor(0);
#l.Draw()

c.Print("m3Hist.png")


