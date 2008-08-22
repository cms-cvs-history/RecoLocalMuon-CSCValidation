import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")

# specify the global tag to use..
# more info and a list of current tags can be found at
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
process.GlobalTag.globaltag = 'IDEAL_V6::All'


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

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# if you want the pretty 2D scatter plots of rechit and segment
# global positions, writeTreeToFile must be set to True, but be careful
# as this will significantly increase the size of the output root file
process.cscValidation = cms.EDFilter("CSCValidation",
    rootFileName = cms.untracked.string('validationHists.root'),
    isSimulation = cms.untracked.bool(True),
    writeTreeToFile = cms.untracked.bool(True),
    makePlots = cms.untracked.bool(False)
)


process.p = cms.Path(process.cscValidation)

