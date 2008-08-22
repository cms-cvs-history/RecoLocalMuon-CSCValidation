import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

# specify the global tag to use..
# more info and a list of current tags can be found at
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = 'CRUZET4_V2::All'

# this points to a skimmed (CSC events) CRUZET3 run (51285)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/CRUZET3/EndcapsMuon/RAW/v4/000/051/285/0211AB52-4255-DD11-98AB-001617DC1F70.root',
        '/store/data/CRUZET3/EndcapsMuon/RAW/v4/000/051/285/749F97C6-FA54-DD11-8277-001617C3B710.root',
        '/store/data/CRUZET3/EndcapsMuon/RAW/v4/000/051/285/D25CA102-FE54-DD11-82FB-000423D6CA72.root'
)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# if you want the pretty 2D scatter plots of rechit and segment
# global positions, writeTreeToFile must be set to True, but be careful
# as this will significantly increase the size of the output root file
process.cscValidation = cms.EDFilter("CSCValidation",
    rootFileName = cms.untracked.string('validationHists.root'),
    isSimulation = cms.untracked.bool(False),
    writeTreeToFile = cms.untracked.bool(True),
    makePlots = cms.untracked.bool(False)
)

process.p = cms.Path(process.muonCSCDigis*process.csc2DRecHits*process.cscSegments*process.cscValidation)

