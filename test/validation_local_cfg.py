import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("CalibMuon.Configuration.CSC_FakeDBConditions_cff")

process.load("EventFilter.CSCRawToDigi.cscSQLiteCablingUnpck_cff")

process.load("EventFilter.CSCRawToDigi.cscUnpacker_cfi")

process.load("RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi")

process.load("RecoLocalMuon.CSCSegment.cscSegments_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")

process.source = cms.Source("DaqSource",
    readerPluginName = cms.untracked.string('CSCFileReader'),
    readerPset = cms.untracked.PSet(
        RUI05 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI05_Monitor_000.raw'),
        RUI04 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI04_Monitor_000.raw'),
        RUI07 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI07_Monitor_000.raw'),
        RUI06 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI06_Monitor_000.raw'),
        RUI01 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI01_Monitor_000.raw'),
        RUI10 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI10_Monitor_000.raw'),
        RUI03 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI03_Monitor_000.raw'),
        RUI02 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI02_Monitor_000.raw'),
        RUI11 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI11_Monitor_000.raw'),
        RUI09 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI09_Monitor_000.raw'),
        RUI08 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI08_Monitor_000.raw'),
        RUI18 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI18_Monitor_000.raw'),
        FED750 = cms.untracked.vstring('RUI00',
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
            'RUI18'),
        RUI15 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI15_Monitor_000.raw'),
        RUI14 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI14_Monitor_000.raw'),
        RUI17 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI17_Monitor_000.raw'),
        RUI16 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI16_Monitor_000.raw'),
        RUI12 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI12_Monitor_000.raw'),
        RUI13 = cms.untracked.vstring('/uscms_data/d1/akub19/run39098/csc_00039098_EmuRUI13_Monitor_000.raw')
    )
)

process.cscValidation = cms.EDFilter("CSCValidation",
    isSimulation = cms.untracked.bool(False),
    makeComparisonPlots = cms.untracked.bool(False),
    writeTreeToFile = cms.untracked.bool(True),
    refRootFile = cms.untracked.string('validationHists_local.root'),
    rootFileName = cms.untracked.string('validationHists_run39098.root'),
    makePlots = cms.untracked.bool(False)
)

process.p = cms.Path(process.muonCSCDigis*process.csc2DRecHits*process.cscSegments*process.cscValidation)
process.muonCSCDigis.ErrorMask = 0x0
process.muonCSCDigis.ExaminerMask = 0x1FEBF3F6

