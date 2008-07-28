import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.muonCSCDigis.UseExaminer = True
process.load("Configuration.StandardSequences.Reconstruction_cff")


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

process.cscValidation = cms.EDFilter("CSCValidation",
    rootFileName = cms.untracked.string('validationHists.root'),
    isSimulation = cms.untracked.bool(False),
    writeTreeToFile = cms.untracked.bool(True),
    makePlots = cms.untracked.bool(False)
)

process.p = cms.Path(process.muonCSCDigis*process.csc2DRecHits*process.cscSegments*process.cscValidation)

