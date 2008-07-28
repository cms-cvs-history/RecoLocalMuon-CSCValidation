import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.muonCSCDigis.UseExaminer = True
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("DaqSource",
    readerPluginName = cms.untracked.string('CSCFileReader'),
    readerPset = cms.untracked.PSet(
        RUI01 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI01_Monitor_000.raw'),
        RUI02 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI02_Monitor_000.raw'),
        RUI03 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI03_Monitor_000.raw'),
        RUI04 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI04_Monitor_000.raw'),
        RUI05 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI05_Monitor_000.raw'),
        RUI06 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI06_Monitor_000.raw'),
        RUI07 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI07_Monitor_000.raw'),
        RUI08 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI08_Monitor_000.raw'),
        RUI09 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI09_Monitor_000.raw'),
        RUI10 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI10_Monitor_000.raw'),
        RUI11 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI11_Monitor_000.raw'),
        RUI12 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI12_Monitor_000.raw'),
        RUI13 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI13_Monitor_000.raw'),
        RUI14 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI14_Monitor_000.raw'),
        RUI15 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI15_Monitor_000.raw'),
        RUI16 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI16_Monitor_000.raw'),
        RUI17 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI17_Monitor_000.raw'),
        RUI18 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI18_Monitor_000.raw'),
        RUI19 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI19_Monitor_000.raw'),
        RUI20 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI20_Monitor_000.raw'),
        RUI21 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI21_Monitor_000.raw'),
        RUI22 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI22_Monitor_000.raw'),
        RUI23 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI23_Monitor_000.raw'),
        RUI24 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI24_Monitor_000.raw'),
        RUI25 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI25_Monitor_000.raw'),
        RUI26 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI26_Monitor_000.raw'),
        RUI27 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI27_Monitor_000.raw'),
        RUI28 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI28_Monitor_000.raw'),
        RUI29 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI29_Monitor_000.raw'),
        RUI30 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI30_Monitor_000.raw'),
        RUI31 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI31_Monitor_000.raw'),
        RUI32 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI32_Monitor_000.raw'),
        RUI33 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI33_Monitor_000.raw'),
        RUI34 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI34_Monitor_000.raw'),
        RUI35 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI35_Monitor_000.raw'),
        RUI36 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI36_Monitor_000.raw'),
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
    rootFileName = cms.untracked.string('validationHists.root'),
    isSimulation = cms.untracked.bool(False),
    writeTreeToFile = cms.untracked.bool(True),
    makePlots = cms.untracked.bool(False)
)

process.p = cms.Path(process.muonCSCDigis*process.csc2DRecHits*process.cscSegments*process.cscValidation)

