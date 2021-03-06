#
# PySNMP MIB module CISCO-LWAPP-ROGUE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-ROGUE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
cLApName, = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApName")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, NotificationType, Unsigned32, iso, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Bits, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "NotificationType", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Bits", "Counter64", "TimeTicks")
MacAddress, StorageType, RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "StorageType", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
ciscoLwappRogueMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 610))
ciscoLwappRogueMIB.setRevisions(('2014-07-14 00:00', '2011-09-07 00:00', '2011-03-11 00:00', '2010-07-17 00:00', '2007-02-06 00:00',))
if mibBuilder.loadTexts: ciscoLwappRogueMIB.setLastUpdated('201407140000Z')
if mibBuilder.loadTexts: ciscoLwappRogueMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappRogueMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 0))
ciscoLwappRogueMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 1))
ciscoLwappRogueMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 2))
cLRogueConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1))
cLRoguePolicyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1))
cLRogueRuleConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3))
cLRogueIgnoreListConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4))
cLRldpAutoContainConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5))
cLRogueApConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6))
class CLAutoContainActions(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("alarmOnly", 1), ("contain", 2))

cLRogueAdhocRogueReportEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueAdhocRogueReportEnable.setStatus('current')
cLRogueReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 300))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueReportInterval.setStatus('current')
cLRogueMinimumRssi = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, -70))).setUnits('dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueMinimumRssi.setStatus('current')
cLRogueTransientInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(120, 1800), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueTransientInterval.setStatus('current')
cLRogueClientNumThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueClientNumThreshold.setStatus('current')
cLRogueDetectionSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("low", 1), ("high", 2), ("critical", 3), ("custom", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueDetectionSecurityLevel.setStatus('current')
cLRogueValidateRogueClientsAgainstMse = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueValidateRogueClientsAgainstMse.setStatus('current')
cLRogueAdhocRogueNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRogueAdhocRogueNotifEnabled.setStatus('current')
cLRogueAdhocRogueDetected = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 610, 0, 1)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"))
if mibBuilder.loadTexts: cLRogueAdhocRogueDetected.setStatus('current')
cLRuleConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1), )
if mibBuilder.loadTexts: cLRuleConfigTable.setStatus('current')
cLRuleConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"))
if mibBuilder.loadTexts: cLRuleConfigEntry.setStatus('current')
cLRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cLRuleName.setStatus('current')
cLRuleRogueType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("friendly", 1), ("malicious", 2), ("unclassified", 3), ("custom", 4))).clone('custom')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRuleRogueType.setStatus('current')
cLRuleConditionsMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("all", 1), ("any", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRuleConditionsMatch.setStatus('current')
cLRulePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRulePriority.setStatus('current')
cLRuleEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRuleEnable.setStatus('current')
cLRuleStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRuleStorageType.setStatus('current')
cLRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRuleRowStatus.setStatus('current')
cLConditionConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2), )
if mibBuilder.loadTexts: cLConditionConfigTable.setStatus('current')
cLConditionConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"), (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionName"))
if mibBuilder.loadTexts: cLConditionConfigEntry.setStatus('current')
cLConditionName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cLConditionName.setStatus('current')
cLConditionType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("managedSsid", 1), ("rssi", 2), ("duration", 3), ("clientCount", 4), ("noEncryption", 5), ("userConfigSsid", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionType.setStatus('current')
cLConditionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionValue.setStatus('current')
cLConditionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionEnable.setStatus('current')
cLConditionStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionStorageType.setStatus('current')
cLConditionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionRowStatus.setStatus('current')
cLConditionRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionRssi.setStatus('current')
cLConditionClientCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionClientCount.setStatus('current')
cLConditionNoEncryptionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 9), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionNoEncryptionEnabled.setStatus('current')
cLConditionManagedSsidEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionManagedSsidEnabled.setStatus('current')
cLConditionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 2, 1, 11), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionDuration.setStatus('current')
cLConditionSsidConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3), )
if mibBuilder.loadTexts: cLConditionSsidConfigTable.setStatus('current')
cLConditionSsidConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1), ).setIndexNames((0, "CISCO-LWAPP-ROGUE-MIB", "cLRuleName"), (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionName"), (0, "CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidValue"))
if mibBuilder.loadTexts: cLConditionSsidConfigEntry.setStatus('current')
cLConditionSsidValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cLConditionSsidValue.setStatus('current')
cLConditionSsidStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionSsidStorageType.setStatus('current')
cLConditionSsidRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 3, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLConditionSsidRowStatus.setStatus('current')
cLRogueIgnoreListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1), )
if mibBuilder.loadTexts: cLRogueIgnoreListTable.setStatus('current')
cLRogueIgnoreListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListMACAddress"))
if mibBuilder.loadTexts: cLRogueIgnoreListEntry.setStatus('current')
cLRogueIgnoreListMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: cLRogueIgnoreListMACAddress.setStatus('current')
cLRogueIgnoreListStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRogueIgnoreListStorageType.setStatus('current')
cLRogueIgnoreListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRogueIgnoreListRowStatus.setStatus('current')
cLRldpAutoContainFeatureOnWiredNetwork = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRldpAutoContainFeatureOnWiredNetwork.setStatus('current')
cLRldpAutoContainRoguesAdvertisingSsid = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 2), CLAutoContainActions().clone('alarmOnly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRldpAutoContainRoguesAdvertisingSsid.setStatus('current')
cLRldpAutoContainAdhocNetworks = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 3), CLAutoContainActions().clone('alarmOnly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRldpAutoContainAdhocNetworks.setStatus('current')
cLRldpAutoContainTrustedClientsOnRogueAps = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 4), CLAutoContainActions().clone('alarmOnly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRldpAutoContainTrustedClientsOnRogueAps.setStatus('current')
cLRldpAutoContainLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRldpAutoContainLevel.setStatus('current')
cLRldpAutoContainOnlyforMonitorModeAps = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 5, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLRldpAutoContainOnlyforMonitorModeAps.setStatus('current')
cLRogueApTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1), )
if mibBuilder.loadTexts: cLRogueApTable.setStatus('current')
cLRogueApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-ROGUE-MIB", "cLRogueApMACAddress"))
if mibBuilder.loadTexts: cLRogueApEntry.setStatus('current')
cLRogueApMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: cLRogueApMACAddress.setStatus('current')
cLRogueApClassType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("friendly", 1), ("malicious", 2), ("unclassified", 3), ("custom", 4))).clone('custom')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRogueApClassType.setStatus('current')
cLRogueApState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("pending", 1), ("alert", 2), ("detectedLrad", 3), ("known", 4), ("acknowledge", 5), ("contained", 6), ("threat", 7), ("containedPending", 8), ("knownContained", 9), ("trustedMissing", 10), ("initializing", 11))).clone('alert')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRogueApState.setStatus('current')
cLRogueApStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRogueApStorageType.setStatus('current')
cLRogueApRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 610, 1, 1, 6, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLRogueApRowStatus.setStatus('current')
ciscoLwappRogueMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1))
ciscoLwappRogueMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2))
ciscoLwappRogueMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 1)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueMIBCompliance = ciscoLwappRogueMIBCompliance.setStatus('deprecated')
ciscoLwappRogueMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 2)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueMIBComplianceRev1 = ciscoLwappRogueMIBComplianceRev1.setStatus('deprecated')
ciscoLwappRogueMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 3)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup2Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueMIBComplianceRev2 = ciscoLwappRogueMIBComplianceRev2.setStatus('deprecated')
ciscoLwappRogueMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 4)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueMIBComplianceRev3 = ciscoLwappRogueMIBComplianceRev3.setStatus('deprecated')
ciscoLwappRogueMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 1, 5)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueNotifsGroup"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup3Group"), ("CISCO-LWAPP-ROGUE-MIB", "ciscoLwappRogueConfigSup4Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueMIBComplianceRev4 = ciscoLwappRogueMIBComplianceRev4.setStatus('current')
ciscoLwappRogueConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 1)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueReportEnable"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueConfigGroup = ciscoLwappRogueConfigGroup.setStatus('current')
ciscoLwappRogueNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 2)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "cLRogueAdhocRogueDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueNotifsGroup = ciscoLwappRogueNotifsGroup.setStatus('current')
ciscoLwappRogueConfigSup1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 3)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"), ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueConfigSup1Group = ciscoLwappRogueConfigSup1Group.setStatus('deprecated')
ciscoLwappRogueConfigSup2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 4)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"), ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainLevel"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainOnlyforMonitorModeAps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueConfigSup2Group = ciscoLwappRogueConfigSup2Group.setStatus('deprecated')
ciscoLwappRogueConfigSup3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 5)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueIgnoreListRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRogueType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleConditionsMatch"), ("CISCO-LWAPP-ROGUE-MIB", "cLRulePriority"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleEnable"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRuleRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionValue"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionEnable"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionSsidRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainFeatureOnWiredNetwork"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainRoguesAdvertisingSsid"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainAdhocNetworks"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainTrustedClientsOnRogueAps"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainLevel"), ("CISCO-LWAPP-ROGUE-MIB", "cLRldpAutoContainOnlyforMonitorModeAps"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueReportInterval"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueMinimumRssi"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueTransientInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueConfigSup3Group = ciscoLwappRogueConfigSup3Group.setStatus('current')
ciscoLwappRogueConfigSup4Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 610, 2, 2, 6)).setObjects(("CISCO-LWAPP-ROGUE-MIB", "cLRogueApClassType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApState"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApStorageType"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueApRowStatus"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueClientNumThreshold"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueDetectionSecurityLevel"), ("CISCO-LWAPP-ROGUE-MIB", "cLRogueValidateRogueClientsAgainstMse"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionRssi"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionClientCount"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionNoEncryptionEnabled"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionManagedSsidEnabled"), ("CISCO-LWAPP-ROGUE-MIB", "cLConditionDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRogueConfigSup4Group = ciscoLwappRogueConfigSup4Group.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-ROGUE-MIB", ciscoLwappRogueConfigSup3Group=ciscoLwappRogueConfigSup3Group, cLConditionRowStatus=cLConditionRowStatus, ciscoLwappRogueConfigSup1Group=ciscoLwappRogueConfigSup1Group, ciscoLwappRogueMIBCompliance=ciscoLwappRogueMIBCompliance, ciscoLwappRogueConfigSup2Group=ciscoLwappRogueConfigSup2Group, cLRuleName=cLRuleName, cLRogueIgnoreListRowStatus=cLRogueIgnoreListRowStatus, cLRogueValidateRogueClientsAgainstMse=cLRogueValidateRogueClientsAgainstMse, cLRogueApState=cLRogueApState, ciscoLwappRogueConfigGroup=ciscoLwappRogueConfigGroup, cLRoguePolicyConfig=cLRoguePolicyConfig, ciscoLwappRogueMIBConform=ciscoLwappRogueMIBConform, cLConditionNoEncryptionEnabled=cLConditionNoEncryptionEnabled, cLConditionSsidRowStatus=cLConditionSsidRowStatus, cLRldpAutoContainAdhocNetworks=cLRldpAutoContainAdhocNetworks, cLRuleConditionsMatch=cLRuleConditionsMatch, cLRldpAutoContainOnlyforMonitorModeAps=cLRldpAutoContainOnlyforMonitorModeAps, cLRogueIgnoreListStorageType=cLRogueIgnoreListStorageType, cLRldpAutoContainLevel=cLRldpAutoContainLevel, cLRogueApMACAddress=cLRogueApMACAddress, cLRogueIgnoreListTable=cLRogueIgnoreListTable, cLRogueIgnoreListMACAddress=cLRogueIgnoreListMACAddress, cLRogueClientNumThreshold=cLRogueClientNumThreshold, cLRogueApTable=cLRogueApTable, cLConditionClientCount=cLConditionClientCount, cLConditionEnable=cLConditionEnable, cLConditionDuration=cLConditionDuration, ciscoLwappRogueMIB=ciscoLwappRogueMIB, cLConditionSsidConfigTable=cLConditionSsidConfigTable, cLRulePriority=cLRulePriority, cLRogueAdhocRogueDetected=cLRogueAdhocRogueDetected, cLConditionValue=cLConditionValue, cLRldpAutoContainFeatureOnWiredNetwork=cLRldpAutoContainFeatureOnWiredNetwork, cLRogueApStorageType=cLRogueApStorageType, cLRuleStorageType=cLRuleStorageType, cLRuleConfigTable=cLRuleConfigTable, cLRuleEnable=cLRuleEnable, cLConditionRssi=cLConditionRssi, cLConditionManagedSsidEnabled=cLConditionManagedSsidEnabled, cLRogueApClassType=cLRogueApClassType, cLRogueDetectionSecurityLevel=cLRogueDetectionSecurityLevel, cLRldpAutoContainTrustedClientsOnRogueAps=cLRldpAutoContainTrustedClientsOnRogueAps, cLConditionSsidConfigEntry=cLConditionSsidConfigEntry, CLAutoContainActions=CLAutoContainActions, ciscoLwappRogueMIBNotifs=ciscoLwappRogueMIBNotifs, cLRogueApEntry=cLRogueApEntry, cLConditionStorageType=cLConditionStorageType, PYSNMP_MODULE_ID=ciscoLwappRogueMIB, ciscoLwappRogueMIBComplianceRev1=ciscoLwappRogueMIBComplianceRev1, cLConditionSsidValue=cLConditionSsidValue, ciscoLwappRogueMIBComplianceRev4=ciscoLwappRogueMIBComplianceRev4, cLConditionType=cLConditionType, cLRuleConfigEntry=cLRuleConfigEntry, ciscoLwappRogueMIBObjects=ciscoLwappRogueMIBObjects, cLRogueMinimumRssi=cLRogueMinimumRssi, ciscoLwappRogueMIBComplianceRev2=ciscoLwappRogueMIBComplianceRev2, ciscoLwappRogueConfigSup4Group=ciscoLwappRogueConfigSup4Group, cLRuleRogueType=cLRuleRogueType, cLRogueApConfig=cLRogueApConfig, ciscoLwappRogueMIBComplianceRev3=ciscoLwappRogueMIBComplianceRev3, cLRogueAdhocRogueNotifEnabled=cLRogueAdhocRogueNotifEnabled, cLRogueApRowStatus=cLRogueApRowStatus, ciscoLwappRogueMIBGroups=ciscoLwappRogueMIBGroups, cLRldpAutoContainRoguesAdvertisingSsid=cLRldpAutoContainRoguesAdvertisingSsid, cLRogueRuleConfig=cLRogueRuleConfig, cLRuleRowStatus=cLRuleRowStatus, cLRldpAutoContainConfig=cLRldpAutoContainConfig, cLRogueIgnoreListEntry=cLRogueIgnoreListEntry, cLConditionName=cLConditionName, ciscoLwappRogueNotifsGroup=ciscoLwappRogueNotifsGroup, cLConditionConfigTable=cLConditionConfigTable, ciscoLwappRogueMIBCompliances=ciscoLwappRogueMIBCompliances, cLRogueConfig=cLRogueConfig, cLRogueIgnoreListConfig=cLRogueIgnoreListConfig, cLRogueAdhocRogueReportEnable=cLRogueAdhocRogueReportEnable, cLConditionSsidStorageType=cLConditionSsidStorageType, cLConditionConfigEntry=cLConditionConfigEntry, cLRogueReportInterval=cLRogueReportInterval, cLRogueTransientInterval=cLRogueTransientInterval)
