import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

# Standard stuff needed for the unpacking and local reco
process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
# for Beam
#process.load("Configuration.StandardSequences.Reconstruction_cff")
# for Cosmics
process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

# specify the global tag to use..
# more info and a list of current tags can be found at
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = 'CRAFT_V3P::All'

# this points to a CRAFT run (66423) as an example
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/data/Commissioning08/Cosmics/RAW/v1/000/066/423/5C05C5CC-329B-DD11-8793-000423D98930.root',
'/store/data/Commissioning08/Cosmics/RAW/v1/000/066/423/9C7A6536-329B-DD11-8254-0019DB29C5FC.root',
'/store/data/Commissioning08/Cosmics/RAW/v1/000/066/423/92ACD2CD-329B-DD11-AF07-000423D998BA.root',
'/store/data/Commissioning08/Cosmics/RAW/v1/000/066/423/02C92F80-329B-DD11-9C57-000423D94700.root',
'/store/data/Commissioning08/Cosmics/RAW/v1/000/066/423/568F9A5A-329B-DD11-BC88-000423D6B2D8.root'
)
)

# recommend at least 100k events (normal Cosmic running)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50000)
)

# This is the CSCValidation package minimum block.  There are more input variables which
# can be set.  Check src/CSCValidation.cc to see what they are.
process.cscValidation = cms.EDFilter("CSCValidation",
    # name of file which will contain output
    rootFileName = cms.untracked.string('validationHists_global.root'),
    # basically turns on/off residual plots which use simhits
    isSimulation = cms.untracked.bool(False),
    # stores a tree of info for the first 1.5M rechits and 2M segments
    # used to make 2D scatter plots of global positions.  Significantly increases
    # size of output root file, so beware...
    writeTreeToFile = cms.untracked.bool(True),
    # mostly for MC and RECO files which may have dropped the digis
    useDigis = cms.untracked.bool(True),
    # lots of extra, more detailed plots
    detailedAnalysis = cms.untracked.bool(False),
    # Input tags for various collections CSCValidation looks at
    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
    compDigiTag = cms.InputTag("muonCSCDigis","MuonCSCComparatorDigi"),
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

# for RECO (if digis were not saved, make sure to set useDigis = False)
#process.p = cms.Path(process.cscValidation)
# for RAW with just local level CSC Stuff
process.p = cms.Path(process.muonCSCDigis * process.csc2DRecHits * process.cscSegments *
                     process.cscValidation)
# for RAW (Cosmics) if you want to look at Trigger and Standalone info
#process.p = cms.Path(process.gtDigis *
#                     process.muonCSCDigis * process.csc2DRecHits * process.cscSegments *
#                     process.muonRPCDigis * process.rpcRecHits *
#                     process.offlineBeamSpot * process.CosmicMuonSeedEndCapsOnly*process.cosmicMuonsEndCapsOnly *
#                     process.cscValidation)

