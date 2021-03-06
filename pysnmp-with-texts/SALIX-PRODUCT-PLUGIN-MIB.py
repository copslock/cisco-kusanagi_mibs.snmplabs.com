#
# PySNMP MIB module SALIX-PRODUCT-PLUGIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-PRODUCT-PLUGIN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:00:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
atmfM4PlugInUnitEntry, atmfM4CellProtoHistIndex = mibBuilder.importSymbols("ATM-FORUM-M4-MIB", "atmfM4PlugInUnitEntry", "atmfM4CellProtoHistIndex")
entPhysicalIndex, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "PhysicalIndex")
platform1, = mibBuilder.importSymbols("SALIX-MIB", "platform1")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, NotificationType, Integer32, IpAddress, Counter64, MibIdentifier, TimeTicks, iso, ObjectIdentity, ModuleIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "Integer32", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "iso", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
salixProductPlugInMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5))
if mibBuilder.loadTexts: salixProductPlugInMIB.setLastUpdated('9810130000Z')
if mibBuilder.loadTexts: salixProductPlugInMIB.setOrganization('SALIX Technologies')
if mibBuilder.loadTexts: salixProductPlugInMIB.setContactInfo('904 Wind River Lane Suite 101 Gaithersburg, MD 20878 (301)-417-0017')
if mibBuilder.loadTexts: salixProductPlugInMIB.setDescription('The MIB describing SALIX specific extensions to the M4-MIB')
salixProductPlugInMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1))
salixProductPlugInMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 2))
salixProductPlugInMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3))
salixProductPlugInMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 2, 0))
class SalixPlugInUnitType(TextualConvention, Integer32):
    description = 'HNE hardware plug-in unit types: unknown(0) - Unknown plug-in unit type mpu(1) - Management Processor Unit dpu(2) - Data Processor Unit smu(3) - Sync Module Unit liu(4) - Line Interface Unit hsf(5) - Hybrid Switch Fabric Unit powerSupply(6) - Power supply fan(7) - Fan Unit hardDrive(8) - Hard drive xcoder(9) - Transcoder ds3Liu(10) - Ds3 LIU softwarePacketLiu(11) - Software Packet LIU packetLiu(12)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("unknown", 0), ("mpu", 1), ("dpu", 2), ("smu", 3), ("liu", 4), ("hsf", 5), ("powerSupply", 6), ("fan", 7), ("hardDrive", 8), ("xcoder", 9), ("ds3Liu", 10), ("softwarePacketLiu", 11), ("packetLiu", 12))

salixPlugInUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1))
salixPlugInUnitDpuTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 1), )
if mibBuilder.loadTexts: salixPlugInUnitDpuTable.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitDpuTable.setDescription('The HNE Data Processor Unit (DPU) plug-in unit table.')
salixPlugInUnitDpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: salixPlugInUnitDpuEntry.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitDpuEntry.setDescription('An entry in the HNE DPU plug-in unit table. An entry contains HNE specific plug-in information for a Data Processor Unit. This table parallels the salixAtmfM4PlugInUnitTable. However, only valid LIU indices of the salixAtmfM4PlugInUnitTable will contain information pertinent to a DPU.')
salixDpuProcessorType = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("mipsR4700", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixDpuProcessorType.setStatus('current')
if mibBuilder.loadTexts: salixDpuProcessorType.setDescription('The type of processor installed on the Data Processor Unit. mipsR4700(1) - MIPS R4700 RISC processor.')
salixPlugInUnitLiuTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2), )
if mibBuilder.loadTexts: salixPlugInUnitLiuTable.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitLiuTable.setDescription('The HNE Line Interface Unit (LIU) plug-in unit table.')
salixPlugInUnitLiuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: salixPlugInUnitLiuEntry.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitLiuEntry.setDescription('An entry in the HNE LIU plug-in unit table. An entry contains HNE specific plug-in information for an LIU. This table is indexed the same as the salixAtmfM4PlugInUnitTable. However, only valid LIU indices of the salixAtmfM4PlugInUnitTable will contain information pertinent to an LIU.')
salixLiuOrderwireEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixLiuOrderwireEnabled.setStatus('current')
if mibBuilder.loadTexts: salixLiuOrderwireEnabled.setDescription('Indication of whether the orderwire is enabled. true(1) - the orderwire is enabled false(2) - the orderwire is not-enabled')
salixLiuOrderwireSonetLine = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixLiuOrderwireSonetLine.setStatus('current')
if mibBuilder.loadTexts: salixLiuOrderwireSonetLine.setDescription('Identifies which of the SONET lines on the plug-in unit to take the orderwire from for drop to the handset.')
salixLiuOrderwireSonetLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("section", 1), ("line", 2))).clone('section')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixLiuOrderwireSonetLayer.setStatus('current')
if mibBuilder.loadTexts: salixLiuOrderwireSonetLayer.setDescription('Identifies which of the two orderwire signals in the selected SONET line should be routed to the handset on the plug-in unit.')
salixPlugInUnitSyncTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 3), )
if mibBuilder.loadTexts: salixPlugInUnitSyncTable.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitSyncTable.setDescription('The HNE Sync module plug-in unit table.')
salixPlugInUnitSyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: salixPlugInUnitSyncEntry.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitSyncEntry.setDescription('An entry in the HNE Sync module plug-in unit table. An entry contains HNE specific plug-in information for a Sync module. This table is indexed the same as the salixAtmfM4PlugInUnitTable. However, only valid Sync module indices of the salixAtmfM4PlugInUnitTable will contain information pertinent to a Sync module.')
salixSyncSlotIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSyncSlotIdentifier.setStatus('current')
if mibBuilder.loadTexts: salixSyncSlotIdentifier.setDescription('Indicates whether the Sync module is installed in the primary or secondary plug-in unit slot.')
salixPlugInUnitXcdrTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6), )
if mibBuilder.loadTexts: salixPlugInUnitXcdrTable.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitXcdrTable.setDescription('The Transcoder (xcoder) plug-in unit table.')
salixPlugInUnitXcdrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: salixPlugInUnitXcdrEntry.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitXcdrEntry.setDescription('An entry in the XCDR table. On entry exists for each Transcoder in the system. Each entry contains information and configuration about the Transcoder')
salixPlugInUnitXcdrPercentWorkingDsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixPlugInUnitXcdrPercentWorkingDsp.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitXcdrPercentWorkingDsp.setDescription("Represents the percentage of the Dsp's on the Transcoder that are currently working. The exact Dsp's that have failed can be found in the itxDspConfigTable from the SALIX-ITX-MIB")
salixPlugInUnitXcdrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("voipServer", 1), ("toneAndAnnouncementServer", 2), ("universalServer", 3))).clone('universalServer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixPlugInUnitXcdrType.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitXcdrType.setDescription('This object describes the Type of Transcoder described by the entry. voipServer(1) - A Transcoder that is limited to VOIP calls toneAndAnnouncementServer(2) - A Transcoder that is limited to announcements and tones universalServer(3) - A Transcoder that can do both Annoucements and VOIP calls')
salixPlugInUnitDs3LiuTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 7), )
if mibBuilder.loadTexts: salixPlugInUnitDs3LiuTable.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitDs3LiuTable.setDescription('The DS3 Line Interface Unit (DS3LIU) plug-in unit table.')
salixPlugInUnitDs3LiuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 7, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: salixPlugInUnitDs3LiuEntry.setStatus('current')
if mibBuilder.loadTexts: salixPlugInUnitDs3LiuEntry.setDescription('An entry in the SALIX Ds3Liu Plugin Unit Table. One entry exists for each DS3LIU in the system, and contains information specific to DS3LIUs.')
salixDs3LiuGroupNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDs3LiuGroupNumber.setStatus('current')
if mibBuilder.loadTexts: salixDs3LiuGroupNumber.setDescription('The group that the DS3LIU corresponding to this entry belongs to. Valid groups are numbered from 1 to 4. A value of 0 indicates that the DS3LIU does not belong in a group.')
salixPPIGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 1))
salixPPICompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 2))
salixPPIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 1)).setObjects(("SALIX-PRODUCT-PLUGIN-MIB", "salixDpuProcessorType"), ("SALIX-PRODUCT-PLUGIN-MIB", "salixLiuOrderwireEnabled"), ("SALIX-PRODUCT-PLUGIN-MIB", "salixLiuOrderwireSonetLine"), ("SALIX-PRODUCT-PLUGIN-MIB", "salixLiuOrderwireSonetLayer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixPPIGroup = salixPPIGroup.setStatus('current')
if mibBuilder.loadTexts: salixPPIGroup.setDescription('Salix M4 Plug-In Objects Group')
salixPPICompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 2)).setObjects(("SALIX-PRODUCT-PLUGIN-MIB", "salixPPIGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixPPICompliance = salixPPICompliance.setStatus('current')
if mibBuilder.loadTexts: salixPPICompliance.setDescription('The basic implementation requirements for the SALIX-M4-MIB.')
mibBuilder.exportSymbols("SALIX-PRODUCT-PLUGIN-MIB", salixPlugInUnitDs3LiuTable=salixPlugInUnitDs3LiuTable, salixDs3LiuGroupNumber=salixDs3LiuGroupNumber, salixPlugInUnitSyncTable=salixPlugInUnitSyncTable, salixProductPlugInMIB=salixProductPlugInMIB, salixPPIGroups=salixPPIGroups, salixPlugInUnitDpuTable=salixPlugInUnitDpuTable, salixPPICompliance=salixPPICompliance, salixPlugInUnitSyncEntry=salixPlugInUnitSyncEntry, salixLiuOrderwireEnabled=salixLiuOrderwireEnabled, salixPlugInUnitXcdrEntry=salixPlugInUnitXcdrEntry, salixPlugInUnitXcdrPercentWorkingDsp=salixPlugInUnitXcdrPercentWorkingDsp, salixPPIGroup=salixPPIGroup, salixProductPlugInMIBTraps=salixProductPlugInMIBTraps, salixPlugInUnitLiuEntry=salixPlugInUnitLiuEntry, salixPlugInUnitDs3LiuEntry=salixPlugInUnitDs3LiuEntry, salixPlugInUnit=salixPlugInUnit, salixPlugInUnitDpuEntry=salixPlugInUnitDpuEntry, salixPlugInUnitXcdrType=salixPlugInUnitXcdrType, salixProductPlugInMIBTrapPrefix=salixProductPlugInMIBTrapPrefix, salixDpuProcessorType=salixDpuProcessorType, salixProductPlugInMIBCompliance=salixProductPlugInMIBCompliance, salixSyncSlotIdentifier=salixSyncSlotIdentifier, salixLiuOrderwireSonetLine=salixLiuOrderwireSonetLine, salixPlugInUnitXcdrTable=salixPlugInUnitXcdrTable, salixPPICompliances=salixPPICompliances, salixProductPlugInMIBObjects=salixProductPlugInMIBObjects, salixLiuOrderwireSonetLayer=salixLiuOrderwireSonetLayer, salixPlugInUnitLiuTable=salixPlugInUnitLiuTable, PYSNMP_MODULE_ID=salixProductPlugInMIB, SalixPlugInUnitType=SalixPlugInUnitType)
