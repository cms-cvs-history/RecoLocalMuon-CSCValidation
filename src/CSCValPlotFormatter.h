#ifndef RecoLocalMuon_CSCValPlotFormatter_H
#define RecoLocalMuon_CSCValPlotFormatter_H


/** \class CSCValPlotFormatter
 *
 *  Makes gif versions of plots from CSCValidation.
 *  This is an attempt to avoid root macros
 *
 *  Andy Kubik - Northwestern University
 *
 */


// system include files
#include <memory>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <cmath>

#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include "TGraph.h"
#include "TProfile.h"
#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLine.h"
#include "TVector3.h"
#include "DataFormats/MuonDetId/interface/CSCDetId.h"

using namespace std;

class CSCValPlotFormatter{

  public:

  // constructor
  CSCValPlotFormatter();

  // destructor
  ~CSCValPlotFormatter();

  void makePlots(map<string,pair<TH1*,string> > tM);

  void makeComparisonPlots(map<string,pair<TH1*,string> > tM, string refFileName);

  void makeGlobalScatterPlots(TTree* t1, string type);

  void make2DTemperaturePlot(TH1 *plot, string savename);

  void nikolaiMacro(map<string,pair<TH1*,string> > theMap, int flag);

  protected:

  private:

  TStyle* getStyle(int stat=1111);

  void drawChamberLines(int station, int lc1);

  void makeGif(TH1* theHisto, string savename, int stat);

  void makeEffGif(TH1* theHisto, string savename);

  int typeIndex(CSCDetId id);

  // map to hold histograms
  map<string,pair<TH1*,string> > theMap;

  // A struct for creating a Tree/Branch of position info
  struct posRecord {
    int endcap;
    int station;
    int ring;
    int chamber;
    int layer;
    float localx;
    float localy;
    float globalx;
    float globaly;
  } rHpos, segpos, rHposref, segposref;

  // The root tree
  TTree *rHTree;
  TTree *segTree;


};

#endif   
