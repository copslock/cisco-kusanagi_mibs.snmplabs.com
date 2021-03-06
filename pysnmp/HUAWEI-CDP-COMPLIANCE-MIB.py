#
# PySNMP MIB module HUAWEI-CDP-COMPLIANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-CDP-COMPLIANCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ZeroBasedCounter32, TimeFilter = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32", "TimeFilter")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, Counter32, IpAddress, iso, NotificationType, ObjectIdentity, ModuleIdentity, Counter64, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Counter32", "IpAddress", "iso", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter64", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32")
TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
hwCdpComplianceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198))
if mibBuilder.loadTexts: hwCdpComplianceMIB.setLastUpdated('200905050000Z')
if mibBuilder.loadTexts: hwCdpComplianceMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwCdpComplianceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1))
hwCdpComplianceNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 2))
hwCdpComplianceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3))
hwCdpComplianceConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1))
hwCdpComplianceStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2))
hwCdpComplianceRemoteSystemsData = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3))
hwCdpComplianceEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 1), EnabledStatus().clone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCdpComplianceEnable.setStatus('current')
hwCdpComplianceNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCdpComplianceNotificationInterval.setStatus('current')
hwCdpCompliancePortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3), )
if mibBuilder.loadTexts: hwCdpCompliancePortConfigTable.setStatus('current')
hwCdpCompliancePortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1), ).setIndexNames((0, "HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigIfIndex"))
if mibBuilder.loadTexts: hwCdpCompliancePortConfigEntry.setStatus('current')
hwCdpCompliancePortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwCdpCompliancePortConfigIfIndex.setStatus('current')
hwCdpCompliancePortConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("rxOnly", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCdpCompliancePortConfigAdminStatus.setStatus('current')
hwCdpCompliancePortConfigHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 254)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCdpCompliancePortConfigHoldTime.setStatus('current')
hwCdpCompliancePortConfigNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCdpCompliancePortConfigNotificationEnable.setStatus('current')
hwCdpCompliancePortStatsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 5), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCdpCompliancePortStatsReset.setStatus('current')
hwCdpComplianceStatsRemTablesLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCdpComplianceStatsRemTablesLastChangeTime.setStatus('current')
hwCdpComplianceStatsRemTablesAgeouts = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 2), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCdpComplianceStatsRemTablesAgeouts.setStatus('current')
hwCdpComplianceStatsRxPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3), )
if mibBuilder.loadTexts: hwCdpComplianceStatsRxPortTable.setStatus('current')
hwCdpComplianceStatsRxPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1), ).setIndexNames((0, "HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRxPortIfIndex"))
if mibBuilder.loadTexts: hwCdpComplianceStatsRxPortEntry.setStatus('current')
hwCdpComplianceStatsRxPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwCdpComplianceStatsRxPortIfIndex.setStatus('current')
hwCdpComplianceStatsRxPortFramesTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCdpComplianceStatsRxPortFramesTotal.setStatus('current')
hwCdpComplianceStatsRxPortAgeoutsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCdpComplianceStatsRxPortAgeoutsTotal.setStatus('current')
hwCdpComplianceRemoteTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1), )
if mibBuilder.loadTexts: hwCdpComplianceRemoteTable.setStatus('current')
hwCdpComplianceRemoteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1), ).setIndexNames((0, "HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemLocalPortIfIndex"))
if mibBuilder.loadTexts: hwCdpComplianceRemoteEntry.setStatus('current')
hwCdpComplianceRemLocalPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwCdpComplianceRemLocalPortIfIndex.setStatus('current')
hwCdpComplianceRemTimeMark = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1, 2), TimeFilter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCdpComplianceRemTimeMark.setStatus('current')
hwCdpComplianceRemoteInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCdpComplianceRemoteInfo.setStatus('current')
hwCdpComplianceNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 2, 1))
hwCdpComplianceRemTablesChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 2, 1, 1)).setObjects(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesLastChangeTime"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesAgeouts"))
if mibBuilder.loadTexts: hwCdpComplianceRemTablesChange.setStatus('current')
hwCdpComplianceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 1))
hwCdpComplianceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2))
hwCdpComplianceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 1, 1)).setObjects(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceConfigGroup"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsGroup"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCdpComplianceCompliance = hwCdpComplianceCompliance.setStatus('current')
hwCdpComplianceConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 1)).setObjects(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceEnable"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceNotificationInterval"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigAdminStatus"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigHoldTime"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCdpComplianceConfigGroup = hwCdpComplianceConfigGroup.setStatus('current')
hwCdpComplianceStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 2)).setObjects(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRxPortFramesTotal"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortStatsReset"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesLastChangeTime"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesAgeouts"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRxPortAgeoutsTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCdpComplianceStatsGroup = hwCdpComplianceStatsGroup.setStatus('current')
hwCdpComplianceRemSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 3)).setObjects(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemoteInfo"), ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemTimeMark"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCdpComplianceRemSysGroup = hwCdpComplianceRemSysGroup.setStatus('current')
hwCdpComplianceTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 4)).setObjects(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemTablesChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCdpComplianceTrapGroup = hwCdpComplianceTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-CDP-COMPLIANCE-MIB", hwCdpComplianceRemoteTable=hwCdpComplianceRemoteTable, hwCdpCompliancePortConfigAdminStatus=hwCdpCompliancePortConfigAdminStatus, hwCdpComplianceRemoteInfo=hwCdpComplianceRemoteInfo, hwCdpComplianceGroups=hwCdpComplianceGroups, hwCdpComplianceRemoteEntry=hwCdpComplianceRemoteEntry, hwCdpCompliancePortConfigIfIndex=hwCdpCompliancePortConfigIfIndex, hwCdpComplianceEnable=hwCdpComplianceEnable, hwCdpComplianceNotifications=hwCdpComplianceNotifications, hwCdpComplianceCompliance=hwCdpComplianceCompliance, hwCdpCompliancePortConfigTable=hwCdpCompliancePortConfigTable, hwCdpComplianceNotificationPrefix=hwCdpComplianceNotificationPrefix, hwCdpComplianceStatsGroup=hwCdpComplianceStatsGroup, hwCdpComplianceStatsRemTablesAgeouts=hwCdpComplianceStatsRemTablesAgeouts, hwCdpComplianceStatsRemTablesLastChangeTime=hwCdpComplianceStatsRemTablesLastChangeTime, hwCdpComplianceStatsRxPortIfIndex=hwCdpComplianceStatsRxPortIfIndex, hwCdpComplianceRemTimeMark=hwCdpComplianceRemTimeMark, hwCdpComplianceRemoteSystemsData=hwCdpComplianceRemoteSystemsData, hwCdpComplianceStatsRxPortAgeoutsTotal=hwCdpComplianceStatsRxPortAgeoutsTotal, hwCdpCompliancePortStatsReset=hwCdpCompliancePortStatsReset, hwCdpComplianceRemTablesChange=hwCdpComplianceRemTablesChange, hwCdpComplianceConfiguration=hwCdpComplianceConfiguration, hwCdpComplianceTrapGroup=hwCdpComplianceTrapGroup, hwCdpComplianceMIB=hwCdpComplianceMIB, hwCdpComplianceRemLocalPortIfIndex=hwCdpComplianceRemLocalPortIfIndex, hwCdpComplianceObjects=hwCdpComplianceObjects, hwCdpComplianceNotificationInterval=hwCdpComplianceNotificationInterval, hwCdpComplianceStatsRxPortEntry=hwCdpComplianceStatsRxPortEntry, hwCdpCompliancePortConfigEntry=hwCdpCompliancePortConfigEntry, PYSNMP_MODULE_ID=hwCdpComplianceMIB, hwCdpComplianceCompliances=hwCdpComplianceCompliances, hwCdpComplianceRemSysGroup=hwCdpComplianceRemSysGroup, hwCdpCompliancePortConfigHoldTime=hwCdpCompliancePortConfigHoldTime, hwCdpComplianceStatsRxPortTable=hwCdpComplianceStatsRxPortTable, hwCdpComplianceConformance=hwCdpComplianceConformance, hwCdpComplianceConfigGroup=hwCdpComplianceConfigGroup, hwCdpComplianceStatistics=hwCdpComplianceStatistics, hwCdpCompliancePortConfigNotificationEnable=hwCdpCompliancePortConfigNotificationEnable, hwCdpComplianceStatsRxPortFramesTotal=hwCdpComplianceStatsRxPortFramesTotal)
