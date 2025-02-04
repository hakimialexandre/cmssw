import FWCore.ParameterSet.Config as cms

process = cms.Process("HcalGeometryTest")

process.load("Geometry.HcalCommonData.hcalDDDSimConstants_cff")
process.load("Geometry.HcalCommonData.hcalDDDRecConstants_cfi")
process.load("Geometry.EcalCommonData.ecalSimulationParameters_cff")
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load("Geometry.CaloEventSetup.CaloGeometry_cff")
process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")
process.load("Geometry.EcalMapping.EcalMapping_cfi")
process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")
process.load("Geometry.HcalTowerAlgo.hcalCellParameterDump_cfi")

process.DDDetectorESProducer = cms.ESSource("DDDetectorESProducer",
                                            confGeomXMLFiles = cms.FileInPath('Geometry/HcalAlgo/data/cmsExtendedGeometry2021.xml'),
                                            appendToDataLabel = cms.string('')
)

process.DDCompactViewESProducer = cms.ESProducer("DDCompactViewESProducer",
                                                appendToDataLabel = cms.string('')
)

process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
    )

process.Timing = cms.Service("Timing")

process.hcalParameters.fromDD4hep = cms.bool(True)
process.caloSimulationParameters.fromDD4hep = cms.bool(True)
process.CaloGeometryBuilder.SelectedCalos = ['HCAL']
process.ecalSimulationParametersEB.fromDD4hep = cms.bool(True)
process.ecalSimulationParametersEE.fromDD4hep = cms.bool(True)
process.ecalSimulationParametersES.fromDD4hep = cms.bool(True)
process.hcalSimulationParameters.fromDD4hep = cms.bool(True)

process.p1 = cms.Path(process.hcalCellParameterDump)
