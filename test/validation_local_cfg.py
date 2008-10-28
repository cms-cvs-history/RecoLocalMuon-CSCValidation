import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

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

# Recommend around 50k events for local CSC Runing
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50000)
)

# this is just an example.  Local data must be copied locally and the paths below
# replaced with wherever you put the files
process.source = cms.Source("DaqSource",
    readerPluginName = cms.untracked.string('CSCFileReader'),
    readerPset = cms.untracked.PSet(
        RUI01 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI01_Monitor_000.raw'),
        RUI02 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI02_Monitor_000.raw'),
        RUI03 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI03_Monitor_000.raw'),
        RUI04 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI04_Monitor_000.raw'),
        RUI05 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI05_Monitor_000.raw'),
        RUI06 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI06_Monitor_000.raw'),
        RUI07 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI07_Monitor_000.raw'),
        RUI08 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI08_Monitor_000.raw'),
        RUI09 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI09_Monitor_000.raw'),
        RUI10 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI10_Monitor_000.raw'),
        RUI11 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI11_Monitor_000.raw'),
        RUI12 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI12_Monitor_000.raw'),
        RUI13 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI13_Monitor_000.raw'),
        RUI14 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI14_Monitor_000.raw'),
        RUI15 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI15_Monitor_000.raw'),
        RUI16 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI16_Monitor_000.raw'),
        RUI17 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI17_Monitor_000.raw'),
        RUI18 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI18_Monitor_000.raw'),
        RUI19 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI19_Monitor_000.raw'),
        RUI20 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI20_Monitor_000.raw'),
        RUI21 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI21_Monitor_000.raw'),
        RUI22 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI22_Monitor_000.raw'),
        RUI23 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI23_Monitor_000.raw'),
        RUI24 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI24_Monitor_000.raw'),
        RUI25 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI25_Monitor_000.raw'),
        RUI26 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI26_Monitor_000.raw'),
        RUI27 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI27_Monitor_000.raw'),
        RUI28 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI28_Monitor_000.raw'),
        RUI29 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI29_Monitor_000.raw'),
        RUI30 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI30_Monitor_000.raw'),
        RUI31 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI31_Monitor_000.raw'),
        RUI32 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI32_Monitor_000.raw'),
        RUI33 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI33_Monitor_000.raw'),
        RUI34 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI34_Monitor_000.raw'),
        RUI35 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI35_Monitor_000.raw'),
        RUI36 = cms.untracked.vstring('/tmp/akub19/csc_00064012_EmuRUI36_Monitor_000.raw'),
        FED750 = cms.untracked.vstring(
            'RUI01',
            'RUI02',
            'RUI03',
            'RUI04',
            'RUI05',
            'RUI06',
            'RUI07',
            'RUI08',
            'RUI09',
            'RUI10',
            'RUI11',
            'RUI12',
            'RUI13',
            'RUI14',
            'RUI15',
            'RUI16',
            'RUI17',
            'RUI18',
            'RUI19',
            'RUI20',
            'RUI21',
            'RUI22',
            'RUI23',
            'RUI24',
            'RUI25',
            'RUI26',
            'RUI27',
            'RUI28',
            'RUI29',
            'RUI30',
            'RUI31',
            'RUI32',
            'RUI33',
            'RUI34',
            'RUI35',
            'RUI36'
        )
    )
)

process.cscValidation = cms.EDFilter("CSCValidation",
    # name of file which will contain output
    rootFileName = cms.untracked.string('validationHists_local.root'),
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

# for RAW with just local level CSC Stuff
process.p = cms.Path(process.muonCSCDigis * process.csc2DRecHits * process.cscSegments *
                     process.cscValidation)
