#
# PySNMP MIB module HP-ICF-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-UDLD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, NotificationType, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, MibIdentifier, Integer32, Gauge32, ModuleIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "MibIdentifier", "Integer32", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks")
TruthValue, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "MacAddress")
hpicfUdldMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33))
hpicfUdldMIB.setRevisions(('2014-06-15 00:00', '2009-08-07 00:00', '2006-04-10 00:00',))
if mibBuilder.loadTexts: hpicfUdldMIB.setLastUpdated('201406150000Z')
if mibBuilder.loadTexts: hpicfUdldMIB.setOrganization('HP Networking')
hpicfUdldNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0))
hpicfUdldObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1))
hpicfUdldConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2))
hpicfUdldConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1))
hpicfUdldStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2))
hpicfUdldConfigTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigTimeInterval.setStatus('current')
hpicfUdldConfigMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigMaxRetries.setStatus('current')
hpicfUdldConfigForwardMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("verifyThenForward", 1), ("forwardThenVerify", 2))).clone('forwardThenVerify')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigForwardMode.setStatus('current')
hpicfUdldConfigTimeIntervalMs = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(5000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldConfigTimeIntervalMs.setStatus('current')
hpicfUdldPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfUdldPortConfigTable.setStatus('current')
hpicfUdldPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldPortConfigEntry.setStatus('current')
hpicfUdldPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldPortAdminStatus.setStatus('current')
hpicfUdldPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldPortVlanId.setStatus('current')
hpicfUdldPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1), )
if mibBuilder.loadTexts: hpicfUdldPortStatsTable.setStatus('current')
hpicfUdldPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldPortStatsEntry.setStatus('current')
hpicfUdldStatsPortCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("offline", 1), ("failure", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortCurrentState.setStatus('current')
hpicfUdldStatsPortNeighborMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortNeighborMAC.setStatus('current')
hpicfUdldStatsPortNeighborPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortNeighborPort.setStatus('current')
hpicfUdldStatsPortTotalTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortTotalTx.setStatus('current')
hpicfUdldStatsPortTotalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortTotalRx.setStatus('current')
hpicfUdldStatsPortNumStateChange = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortNumStateChange.setStatus('current')
hpicfUdldStatsPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUdldStatsPortStatus.setStatus('current')
hpicfUdldStatsClearAll = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 1, 2, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUdldStatsClearAll.setStatus('current')
hpicfUdldNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0))
hpicfUdldLinkfault = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldLinkfault.setStatus('current')
hpicfUdldLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 0, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfUdldLinkUp.setStatus('current')
hpicfUdldCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1))
hpicfUdldGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2))
hpicfUdldCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 1)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldPortConfigGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortStatsGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldNotificationGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldCompliance = hpicfUdldCompliance.setStatus('deprecated')
hpicfUdldCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 2)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldCompliance2 = hpicfUdldCompliance2.setStatus('current')
hpicfUdldCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 1, 3)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldPortConfigGroup1"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortStatsGroup"), ("HP-ICF-UDLD-MIB", "hpicfUdldNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldCompliance3 = hpicfUdldCompliance3.setStatus('current')
hpicfUdldPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 1)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeInterval"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigMaxRetries"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortAdminStatus"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldPortConfigGroup = hpicfUdldPortConfigGroup.setStatus('deprecated')
hpicfUdldPortStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 2)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortCurrentState"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNeighborMAC"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNeighborPort"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortTotalTx"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortTotalRx"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortNumStateChange"), ("HP-ICF-UDLD-MIB", "hpicfUdldStatsPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldPortStatsGroup = hpicfUdldPortStatsGroup.setStatus('current')
hpicfUdldNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 3)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldLinkfault"), ("HP-ICF-UDLD-MIB", "hpicfUdldLinkUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldNotificationGroup = hpicfUdldNotificationGroup.setStatus('current')
hpicfUdldStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 4)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldStatsClearAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldStatsGroup = hpicfUdldStatsGroup.setStatus('current')
hpicfUdldPortConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33, 2, 2, 5)).setObjects(("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeInterval"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigMaxRetries"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortAdminStatus"), ("HP-ICF-UDLD-MIB", "hpicfUdldPortVlanId"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigForwardMode"), ("HP-ICF-UDLD-MIB", "hpicfUdldConfigTimeIntervalMs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUdldPortConfigGroup1 = hpicfUdldPortConfigGroup1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-UDLD-MIB", hpicfUdldPortConfigEntry=hpicfUdldPortConfigEntry, hpicfUdldCompliance3=hpicfUdldCompliance3, hpicfUdldConfigMaxRetries=hpicfUdldConfigMaxRetries, hpicfUdldGroups=hpicfUdldGroups, hpicfUdldCompliances=hpicfUdldCompliances, hpicfUdldNotifications=hpicfUdldNotifications, hpicfUdldPortAdminStatus=hpicfUdldPortAdminStatus, hpicfUdldPortVlanId=hpicfUdldPortVlanId, hpicfUdldConfigForwardMode=hpicfUdldConfigForwardMode, hpicfUdldStatsClearAll=hpicfUdldStatsClearAll, hpicfUdldLinkUp=hpicfUdldLinkUp, hpicfUdldPortStatsEntry=hpicfUdldPortStatsEntry, hpicfUdldPortStatsTable=hpicfUdldPortStatsTable, hpicfUdldCompliance=hpicfUdldCompliance, hpicfUdldObjects=hpicfUdldObjects, hpicfUdldNotificationGroup=hpicfUdldNotificationGroup, hpicfUdldStatsPortCurrentState=hpicfUdldStatsPortCurrentState, hpicfUdldPortConfigGroup=hpicfUdldPortConfigGroup, hpicfUdldConfigTimeInterval=hpicfUdldConfigTimeInterval, hpicfUdldCompliance2=hpicfUdldCompliance2, hpicfUdldPortConfigGroup1=hpicfUdldPortConfigGroup1, hpicfUdldStatsPortTotalTx=hpicfUdldStatsPortTotalTx, hpicfUdldConformance=hpicfUdldConformance, hpicfUdldLinkfault=hpicfUdldLinkfault, hpicfUdldStatsPortNumStateChange=hpicfUdldStatsPortNumStateChange, PYSNMP_MODULE_ID=hpicfUdldMIB, hpicfUdldConfig=hpicfUdldConfig, hpicfUdldPortStatsGroup=hpicfUdldPortStatsGroup, hpicfUdldStatsGroup=hpicfUdldStatsGroup, hpicfUdldMIB=hpicfUdldMIB, hpicfUdldStatsPortTotalRx=hpicfUdldStatsPortTotalRx, hpicfUdldStatsPortStatus=hpicfUdldStatsPortStatus, hpicfUdldNotificationPrefix=hpicfUdldNotificationPrefix, hpicfUdldPortConfigTable=hpicfUdldPortConfigTable, hpicfUdldStatsPortNeighborMAC=hpicfUdldStatsPortNeighborMAC, hpicfUdldStats=hpicfUdldStats, hpicfUdldConfigTimeIntervalMs=hpicfUdldConfigTimeIntervalMs, hpicfUdldStatsPortNeighborPort=hpicfUdldStatsPortNeighborPort)
