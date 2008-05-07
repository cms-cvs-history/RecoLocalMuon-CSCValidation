#ifndef RecoLocalMuon_CSCValidation_H
#define RecoLocalMuon_CSCValidation_H

/** \class CSCValidation
 *
 * Simple package to validate local CSC reconstruction:
 *    DIGIS
 *    recHits
 *    segments
 *
 * This program merely unpacks collections and fills
 * a few simple histograms.  The idea is to compare
 * the histograms for one offline release and another
 * and look for unexpected differences.
 *
 * Michael Schmitt, Northwestern University, July 2007
 */

// system include files
#include <memory>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <iomanip>
#include <fstream>

// user include files
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/CSCDigi/interface/CSCWireDigi.h"
#include "DataFormats/CSCDigi/interface/CSCWireDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCStripDigi.h"
#include "DataFormats/CSCDigi/interface/CSCStripDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCComparatorDigi.h"
#include "DataFormats/CSCDigi/interface/CSCComparatorDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCALCTDigi.h"
#include "DataFormats/CSCDigi/interface/CSCALCTDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTDigi.h"
#include "DataFormats/CSCDigi/interface/CSCCLCTDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCRPCDigi.h"
#include "DataFormats/CSCDigi/interface/CSCRPCDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCCorrelatedLCTDigi.h"
#include "DataFormats/CSCDigi/interface/CSCCorrelatedLCTDigiCollection.h"

#include "DataFormats/MuonDetId/interface/CSCDetId.h"
#include <DataFormats/CSCRecHit/interface/CSCRecHit2D.h>
#include <DataFormats/CSCRecHit/interface/CSCSegmentCollection.h>

#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "Geometry/CSCGeometry/interface/CSCChamber.h"
#include "Geometry/CSCGeometry/interface/CSCLayer.h"
#include "Geometry/CSCGeometry/interface/CSCLayerGeometry.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"

#include "DataFormats/CSCRecHit/interface/CSCRecHit2DCollection.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"

#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/GeometryVector/interface/GlobalVector.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometryVector/interface/LocalVector.h"
#include "DataFormats/CLHEP/interface/AlgebraicObjects.h"
#include "DataFormats/MuonDetId/interface/CSCIndexer.h"

#include "CondFormats/CSCObjects/interface/CSCDBGains.h"
#include "CondFormats/DataRecord/interface/CSCDBGainsRcd.h"
#include "CondFormats/CSCObjects/interface/CSCDBNoiseMatrix.h"
#include "CondFormats/DataRecord/interface/CSCDBNoiseMatrixRcd.h"
#include "CondFormats/CSCObjects/interface/CSCDBCrosstalk.h"
#include "CondFormats/DataRecord/interface/CSCDBCrosstalkRcd.h"
#include "CondFormats/CSCObjects/interface/CSCDBPedestals.h"
#include "CondFormats/DataRecord/interface/CSCDBPedestalsRcd.h"

#include "CommonTools/Statistics/interface/ChiSquaredProbability.h"


#include "RecoLocalMuon/CSCValidation/src/CSCValHists.h"
#include "TVector3.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"
#include "TString.h"
#include "TTree.h"

//namespace edm {
//  class ParameterSet;
// class Event;
//  class EventSetup;
//}

//class PSimHit;
//class TFile;
//class CSCLayer;
//class CSCDetId;

class CSCValidation : public edm::EDAnalyzer {
public:
  /// Constructor
  CSCValidation(const edm::ParameterSet& pset);

  /// Destructor
  virtual ~CSCValidation();

  // Operations

  /// Perform the real analysis
  void analyze(const edm::Event & event, const edm::EventSetup& eventSetup);
  void endJob();

protected:

private: 

  // these are the "modules"
  // if you would like to add code to CSCValidation, please do so by adding an
  // extra module in the form of an additional private member function
  void  doOccupancies(edm::Handle<CSCStripDigiCollection> strips, edm::Handle<CSCWireDigiCollection> wires,
                      edm::Handle<CSCRecHit2DCollection> recHits, edm::Handle<CSCSegmentCollection> cscSegments);
  void  doStripDigis(edm::Handle<CSCStripDigiCollection> strips);
  void  doWireDigis(edm::Handle<CSCWireDigiCollection> wires);
  void  doRecHits(edm::Handle<CSCRecHit2DCollection> recHits,edm::Handle<CSCStripDigiCollection> strips,
                  edm::ESHandle<CSCGeometry> cscGeom);
  void  doSimHits(edm::Handle<CSCRecHit2DCollection> recHits, edm::Handle<edm::PSimHitContainer> simHits);
  void  doPedestalNoise(edm::Handle<CSCStripDigiCollection> strips);
  void  doSegments(edm::Handle<CSCSegmentCollection> cscSegments, edm::ESHandle<CSCGeometry> cscGeom);
  void  doEfficiencies(edm::Handle<CSCRecHit2DCollection> recHits, edm::Handle<CSCSegmentCollection> cscSegments);
  void  doGasGain(const CSCWireDigiCollection &, const CSCStripDigiCollection &, const CSCRecHit2DCollection &);
  void  doCalibrations(const edm::EventSetup& eventSetup);

  // some useful functions
  float  fitX(HepMatrix sp, HepMatrix ep);
  float  getTiming(const CSCStripDigiCollection& stripdigis, CSCDetId idRH, int centerStrip);
  float  getSignal(const CSCStripDigiCollection& stripdigis, CSCDetId idRH, int centerStrip);

  // these functions handle Stoyan's efficiency code
  void  fillEfficiencyHistos(int bin, int flag);
  void  getEfficiency(float bin, float Norm, std::vector<float> &eff);
  void  histoEfficiency(TH1F *readHisto, TH1F *writeHisto);

  // counter
  int nEventsAnalyzed;

  //
  //
  // The root file for the histograms.
  TFile *theFile;

  //
  //
  // input parameters for this module
  bool makePlots;
  bool makeComparisonPlots;
  std::string refRootFile;
  bool writeTreeToFile;
  bool isSimulation;
  std::string rootFileName;

  bool makeOccupancyPlots;
  bool makeStripPlots;
  bool makeWirePlots;
  bool makeRecHitPlots;
  bool makeSimHitPlots;
  bool makeSegmentPlots;
  bool makePedNoisePlots;
  bool makeEfficiencyPlots;
  bool makeGasGainPlots;

  // The histo managing object
  CSCValHists *histos;

  // tmp histos for Efficiency
  TH1F *hSSTE;
  TH1F *hRHSTE;
  TH1F *hSEff;
  TH1F *hRHEff;

  /// Vectors of stored pointers to TH1 and TH2
                                                                                
  std::vector<TH1*>   th1;
  std::vector<TH2*>   th2;
  /// Book histograms
  void bookForId(int casenmb, const int& idint,const std::string& ids);
 
  /// Fill 1D histograms
  void hf1ForId(std::map<int, TH1*>& mp, std::vector<TH1*>& th1,
                int casenmb, const int& id, float& x, float w);
 
  /// Fill 2D histograms
  void hf2ForId(std::map<int, TH2*>& mp,  std::vector<TH2*>& th2,
                int casenmb, const int& id, float& x, float& y, float w);
 
  /// Vectors of stored pointers to TH1 and TH2 in their maps in gas gain

  std::vector<TH1*>   th1_gas_gain;
  std::vector<TH2*>   th2_gas_gain;

  /// Histogram maps for gas gain
  std::map<int, TH1*> mh_gas_gain_wires_strips_rechits_present;
  std::map<int, TH1*> mh_gas_gain_wires_per_layer;
  std::map<int, TH1*> mh_gas_gain_rechits_per_layer;
  std::map<int, TH2*> mh_gas_gain_rechit_adc_3_3_sum_location;
  std::map<int, TH2*> mh_gas_gain_mean;
  std::map<int, TH2*> mh_gas_gain_entries;

  std::map<int, TH2*> mh_wire_timing_mean;
  std::map<int, TH2*> mh_wire_timing_entries;

  /// Maps and vectors for gas gain
  std::vector<int>     nmbhvsegm;
  std::map<int, std::vector<int> >   m_wire_hvsegm;
  std::map<int, int>   m_single_wire_layer;
  std::map<int, int>   m_nmbrechit_layer;
  std::map<int, float> m_rechit_adc_3_3_sum;
  std::map<int, int>   m_rechit_strip;
  std::map<int, float> m_mean_adc_3_3_sum;
  std::map<int, float> m_nmb_adc_3_3_sum;
  std::map<int, int>   m_csc_type;
  std::map<int, int>   m_index_csc;

  std::map<int, float> m_mean_wire_timing;
  std::map<int, float> m_nmb_wire_timing;

};
#endif
