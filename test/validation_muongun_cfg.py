import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("CalibMuon.Configuration.CSC_FakeDBConditions_cff")

process.load("RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi")

process.load("RecoLocalMuon.CSCSegment.cscSegments_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/uscms_data/d1/akub19/valData/MC/CSCValidation_muongun_100GeV.0.root',
        'file:/uscms_data/d1/akub19/valData/MC/CSCValidation_muongun_100GeV.1.root',
        'file:/uscms_data/d1/akub19/valData/MC/CSCValidation_muongun_100GeV.2.root',
        'file:/uscms_data/d1/akub19/valData/MC/CSCValidation_muongun_100GeV.3.root',
        'file:/uscms_data/d1/akub19/valData/MC/CSCValidation_muongun_100GeV.4.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(25000)
)
process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")

process.cscValidation = cms.EDFilter("CSCValidation",
    isSimulation = cms.untracked.bool(True),
    makeComparisonPlots = cms.untracked.bool(False),
    writeTreeToFile = cms.untracked.bool(True),
    refRootFile = cms.untracked.string('validationHists_muongun.root'),
    rootFileName = cms.untracked.string('validationHists_muongun.root'),
    makePlots = cms.untracked.bool(False)
)

process.p = cms.Path(process.csc2DRecHits*process.cscSegments*process.cscValidation)

