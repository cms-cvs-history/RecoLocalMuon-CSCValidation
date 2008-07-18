import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("CalibMuon.Configuration.CSC_FakeDBConditions_cff")

process.load("EventFilter.CSCRawToDigi.cscFrontierCablingUnpck_cff")

process.load("EventFilter.CSCRawToDigi.cscUnpacker_cfi")

process.load("RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi")

process.load("RecoLocalMuon.CSCSegment.cscSegments_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/uscms_data/d1/akub19/valData/MTCC/CSCValidation_mtcc_run4318.0.root',
        'file:/uscms_data/d1/akub19/valData/MTCC/CSCValidation_mtcc_run4318.1.root',
        'file:/uscms_data/d1/akub19/valData/MTCC/CSCValidation_mtcc_run4318.2.root',
        'file:/uscms_data/d1/akub19/valData/MTCC/CSCValidation_mtcc_run4318.3.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)
process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")

process.cscValidation = cms.EDFilter("CSCValidation",
    rootFileName = cms.untracked.string('validationHists.root'),
    isSimulation = cms.untracked.bool(False),
    writeTreeToFile = cms.untracked.bool(True),
    makePlots = cms.untracked.bool(False)
)

process.p = cms.Path(process.muonCSCDigis*process.csc2DRecHits*process.cscSegments*process.cscValidation)

