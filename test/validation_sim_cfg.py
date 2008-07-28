import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.csc2DRecHits.wireDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")
process.csc2DRecHits.stripDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCStripDigi")


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/relval/2008/7/13/RelVal-RelValSingleMuPt100-1215820444-IDEAL_V5-2nd/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/CMSSW_2_1_0_pre8-RelVal-1215820444-IDEAL_V5-2nd-IDEAL_V5-unmerged/0000/0E08D594-FA50-DD11-86D2-001617E30CD4.root',
'/store/relval/2008/7/13/RelVal-RelValSingleMuPt100-1215820444-IDEAL_V5-2nd/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/CMSSW_2_1_0_pre8-RelVal-1215820444-IDEAL_V5-2nd-IDEAL_V5-unmerged/0000/527AF9C8-F550-DD11-8D8E-000423D99896.root',
'/store/relval/2008/7/13/RelVal-RelValSingleMuPt100-1215820444-IDEAL_V5-2nd/RelValSingleMuPt100/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/CMSSW_2_1_0_pre8-RelVal-1215820444-IDEAL_V5-2nd-IDEAL_V5-unmerged/0000/F213F543-F550-DD11-9DE0-000423D6CA02.root'
)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.cscValidation = cms.EDFilter("CSCValidation",
    rootFileName = cms.untracked.string('validationHists.root'),
    isSimulation = cms.untracked.bool(True),
    writeTreeToFile = cms.untracked.bool(True),
    makePlots = cms.untracked.bool(False)
)


process.p = cms.Path(process.csc2DRecHits*process.cscSegments*process.cscValidation)

