import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

# specify the global tag to use..
# more info and a list of current tags can be found at
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = 'STARTUP_V7::All'


# points to CMSSW_2_1_2 single muon (Pt = 100) relval sample.  Sim data must contain
# digis and RECO or else expect an error from CSCValidation.
# Look for DIGI and RECO in the dataset name...
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
       '/store/relval/CMSSW_2_1_2/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V6_10TeV_v1/0001/2CEA4EBD-CF6A-DD11-8D3F-000423D94C68.root',
       '/store/relval/CMSSW_2_1_2/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V6_10TeV_v1/0001/363D75C1-CF6A-DD11-805C-000423D99658.root',
       '/store/relval/CMSSW_2_1_2/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V6_10TeV_v1/0001/563315A7-E36A-DD11-B3AF-000423D94990.root',
       '/store/relval/CMSSW_2_1_2/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V6_10TeV_v1/0004/FAE42B0C-AD6B-DD11-A0CE-001617DBD556.root'
)
)

# recommend at least 10k events (single Muon Simulation)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.cscValidation = cms.EDFilter("CSCValidation",
    # name of file which will contain output
    rootFileName = cms.untracked.string('validationHists_sim.root'),
    # basically turns on/off residual plots which use simhits
    isSimulation = cms.untracked.bool(True),
    # stores a tree of info for the first 1.5M rechits and 2M segments
    # used to make 2D scatter plots of global positions.  Significantly increases
    # size of output root file, so beware...
    writeTreeToFile = cms.untracked.bool(True),
    # mostly for MC and RECO files which may have dropped the digis
    useDigis = cms.untracked.bool(True),
    # lots of extra, more detailed plots
    detailedAnalysis = cms.untracked.bool(False),
    # Input tags for various collections CSCValidation looks at
    stripDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi"),
    compDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    cscRecHitTag = cms.InputTag("csc2DRecHits"),
    cscSegTag = cms.InputTag("cscSegments"),
    # do you want to look at trigger info?
    makeTriggerPlots = cms.untracked.bool(False),
    # do you want to look at STA muons?
    makeStandalonePlots = cms.untracked.bool(False),
    # STA tag for cosmics
    saMuonTag = cms.InputTag("cosmicMuonsEndCapsOnly"),
    l1aTag = cms.InputTag("gtDigis"),
    simHitTag = cms.InputTag("g4SimHits", "MuonCSCHits")
)

# for RECO or SIM  (if digis were not saved, make sure to set useDigis = False)
process.p = cms.Path(process.cscValidation)
# for RAW with just local level CSC Stuff
#process.p = cms.Path(process.muonCSCDigis * process.csc2DRecHits * process.cscSegments *
#                     process.cscValidation)
# for RAW (Cosmics) if you want to look at Trigger and Standalone info
#process.p = cms.Path(process.gtDigis *
#                     process.muonCSCDigis * process.csc2DRecHits * process.cscSegments *
#                     process.muonRPCDigis * process.rpcRecHits *
#                     process.offlineBeamSpot * process.CosmicMuonSeedEndCapsOnly*process.cosmicMuonsEndCapsOnly *
#                     process.cscValidation)

