#
# PySNMP MIB module A3COM-HUAWEI-USERLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-USERLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
huaweiDatacomm, huaweiMgmt, huawei = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiDatacomm", "huaweiMgmt", "huawei")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter64, TimeTicks, Gauge32, NotificationType, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter64", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwUserLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18))
if mibBuilder.loadTexts: hwUserLogMIB.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: hwUserLogMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwUserlogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1))
hwUserlogNatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1))
hwUserlogNatVersion = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatVersion.setStatus('current')
hwUserlogNatSyslog = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatSyslog.setStatus('current')
hwUserlogNatSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatSourceIP.setStatus('current')
hwUserlogNatFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatFlowBegin.setStatus('current')
hwUserlogNatActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatActiveTime.setStatus('current')
hwUserlogNatSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6), )
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoTable.setStatus('current')
hwUserlogNatSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1), ).setIndexNames((0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogNatSlotCfgInfoEntry.setStatus('current')
hwUserlogNatCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatCfgSlotNumber.setStatus('current')
hwUserlogNatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatEnable.setStatus('current')
hwUserlogNatAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatAclNumber.setStatus('current')
hwUserlogNatHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatHostAddress.setStatus('current')
hwUserlogNatUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatUdpPort.setStatus('current')
hwUserlogNatSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7), )
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoTable.setStatus('current')
hwUserlogNatSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1), ).setIndexNames((0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogNatSlotRunInfoEntry.setStatus('current')
hwUserlogNatRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatRunSlotNumber.setStatus('current')
hwUserlogNatTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatTotalEntries.setStatus('current')
hwUserlogNatTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatTotalPackets.setStatus('current')
hwUserlogNatFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatFailedEntries.setStatus('current')
hwUserlogNatFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogNatFailedPackets.setStatus('current')
hwUserlogNatClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 1, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogNatClearRunStat.setStatus('current')
hwUserlogFlowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2))
hwUserlogFlowVersion = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowVersion.setStatus('current')
hwUserlogFlowSyslog = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowSyslog.setStatus('current')
hwUserlogFlowSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowSourceIP.setStatus('current')
hwUserlogFlowFlowBegin = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowFlowBegin.setStatus('current')
hwUserlogFlowActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowActiveTime.setStatus('current')
hwUserlogFlowSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6), )
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoTable.setStatus('current')
hwUserlogFlowSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1), ).setIndexNames((0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogFlowSlotCfgInfoEntry.setStatus('current')
hwUserlogFlowCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowCfgSlotNumber.setStatus('current')
hwUserlogFlowEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowEnable.setStatus('current')
hwUserlogFlowAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowAclNumber.setStatus('current')
hwUserlogFlowHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowHostAddress.setStatus('current')
hwUserlogFlowUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowUdpPort.setStatus('current')
hwUserlogFlowSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7), )
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoTable.setStatus('current')
hwUserlogFlowSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1), ).setIndexNames((0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogFlowSlotRunInfoEntry.setStatus('current')
hwUserlogFlowRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowRunSlotNumber.setStatus('current')
hwUserlogFlowTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowTotalEntries.setStatus('current')
hwUserlogFlowTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowTotalPackets.setStatus('current')
hwUserlogFlowFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowFailedEntries.setStatus('current')
hwUserlogFlowFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogFlowFailedPackets.setStatus('current')
hwUserlogFlowClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 2, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogFlowClearRunStat.setStatus('current')
hwUserlogAccessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3))
hwUserlogAccessVersion = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessVersion.setStatus('current')
hwUserlogAccessSyslog = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessSyslog.setStatus('current')
hwUserlogAccessSourceIP = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessSourceIP.setStatus('current')
hwUserlogAccessSlotCfgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4), )
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoTable.setStatus('current')
hwUserlogAccessSlotCfgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"))
if mibBuilder.loadTexts: hwUserlogAccessSlotCfgInfoEntry.setStatus('current')
hwUserlogAccessCfgSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessCfgSlotNumber.setStatus('current')
hwUserlogAccessEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessEnable.setStatus('current')
hwUserlogAccessHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessHostAddress.setStatus('current')
hwUserlogAccessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessUdpPort.setStatus('current')
hwUserlogAccessSlotRunInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5), )
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoTable.setStatus('current')
hwUserlogAccessSlotRunInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessRunSlotNumber"))
if mibBuilder.loadTexts: hwUserlogAccessSlotRunInfoEntry.setStatus('current')
hwUserlogAccessRunSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessRunSlotNumber.setStatus('current')
hwUserlogAccessTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessTotalEntries.setStatus('current')
hwUserlogAccessTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessTotalPackets.setStatus('current')
hwUserlogAccessFailedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessFailedEntries.setStatus('current')
hwUserlogAccessFailedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUserlogAccessFailedPackets.setStatus('current')
hwUserlogAccessClearRunStat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 1, 3, 5, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserlogAccessClearRunStat.setStatus('current')
hwUserlogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 2))
hwUserlogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3))
hwUserlogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 1))
hwUserlogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 1, 1)).setObjects(("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogCompliance = hwUserlogCompliance.setStatus('current')
hwUserlogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2))
hwUserlogMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2, 1)).setObjects(("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogMandatoryGroup = hwUserlogMandatoryGroup.setStatus('current')
hwUserlogConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2, 2)).setObjects(("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatVersion"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatSyslog"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatSourceIP"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatFlowBegin"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatActiveTime"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatCfgSlotNumber"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatEnable"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatAclNumber"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatHostAddress"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatUdpPort"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowVersion"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowSyslog"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowSourceIP"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowFlowBegin"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowActiveTime"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowCfgSlotNumber"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowEnable"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowAclNumber"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowHostAddress"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowUdpPort"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessVersion"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessSyslog"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessSourceIP"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessCfgSlotNumber"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessEnable"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessHostAddress"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessUdpPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogConfigGroup = hwUserlogConfigGroup.setStatus('current')
hwUserlogInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 18, 3, 2, 3)).setObjects(("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatTotalEntries"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatTotalPackets"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatFailedEntries"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogNatFailedPackets"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalEntries"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowTotalPackets"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedEntries"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogFlowFailedPackets"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalEntries"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessTotalPackets"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedEntries"), ("A3COM-HUAWEI-USERLOG-MIB", "hwUserlogAccessFailedPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserlogInfoGroup = hwUserlogInfoGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-USERLOG-MIB", hwUserlogFlowFlowBegin=hwUserlogFlowFlowBegin, hwUserlogConformance=hwUserlogConformance, hwUserlogFlowFailedPackets=hwUserlogFlowFailedPackets, PYSNMP_MODULE_ID=hwUserLogMIB, hwUserlogAccessObjects=hwUserlogAccessObjects, hwUserlogNotifications=hwUserlogNotifications, hwUserlogNatObjects=hwUserlogNatObjects, hwUserlogFlowSyslog=hwUserlogFlowSyslog, hwUserlogFlowCfgSlotNumber=hwUserlogFlowCfgSlotNumber, hwUserlogCompliances=hwUserlogCompliances, hwUserlogInfoGroup=hwUserlogInfoGroup, hwUserlogAccessVersion=hwUserlogAccessVersion, hwUserlogAccessClearRunStat=hwUserlogAccessClearRunStat, hwUserlogCompliance=hwUserlogCompliance, hwUserlogFlowSlotRunInfoTable=hwUserlogFlowSlotRunInfoTable, hwUserlogFlowUdpPort=hwUserlogFlowUdpPort, hwUserlogNatSlotCfgInfoTable=hwUserlogNatSlotCfgInfoTable, hwUserlogFlowVersion=hwUserlogFlowVersion, hwUserlogFlowSourceIP=hwUserlogFlowSourceIP, hwUserlogConfigGroup=hwUserlogConfigGroup, hwUserlogNatVersion=hwUserlogNatVersion, hwUserlogAccessTotalEntries=hwUserlogAccessTotalEntries, hwUserlogFlowSlotCfgInfoEntry=hwUserlogFlowSlotCfgInfoEntry, hwUserlogNatTotalEntries=hwUserlogNatTotalEntries, hwUserlogNatHostAddress=hwUserlogNatHostAddress, hwUserlogFlowSlotRunInfoEntry=hwUserlogFlowSlotRunInfoEntry, hwUserlogAccessSlotRunInfoTable=hwUserlogAccessSlotRunInfoTable, hwUserlogNatClearRunStat=hwUserlogNatClearRunStat, hwUserlogNatSlotCfgInfoEntry=hwUserlogNatSlotCfgInfoEntry, hwUserlogNatFailedEntries=hwUserlogNatFailedEntries, hwUserlogFlowObjects=hwUserlogFlowObjects, hwUserlogFlowActiveTime=hwUserlogFlowActiveTime, hwUserlogFlowSlotCfgInfoTable=hwUserlogFlowSlotCfgInfoTable, hwUserlogAccessSourceIP=hwUserlogAccessSourceIP, hwUserlogFlowTotalEntries=hwUserlogFlowTotalEntries, hwUserlogAccessEnable=hwUserlogAccessEnable, hwUserlogAccessRunSlotNumber=hwUserlogAccessRunSlotNumber, hwUserlogAccessTotalPackets=hwUserlogAccessTotalPackets, hwUserlogMandatoryGroup=hwUserlogMandatoryGroup, hwUserlogFlowClearRunStat=hwUserlogFlowClearRunStat, hwUserlogNatSourceIP=hwUserlogNatSourceIP, hwUserlogNatFailedPackets=hwUserlogNatFailedPackets, hwUserlogNatUdpPort=hwUserlogNatUdpPort, hwUserlogNatTotalPackets=hwUserlogNatTotalPackets, hwUserlogNatSlotRunInfoEntry=hwUserlogNatSlotRunInfoEntry, hwUserlogAccessUdpPort=hwUserlogAccessUdpPort, hwUserlogNatSyslog=hwUserlogNatSyslog, hwUserlogAccessSyslog=hwUserlogAccessSyslog, hwUserlogFlowFailedEntries=hwUserlogFlowFailedEntries, hwUserlogAccessCfgSlotNumber=hwUserlogAccessCfgSlotNumber, hwUserlogFlowEnable=hwUserlogFlowEnable, hwUserlogAccessSlotCfgInfoEntry=hwUserlogAccessSlotCfgInfoEntry, hwUserlogFlowHostAddress=hwUserlogFlowHostAddress, hwUserlogFlowTotalPackets=hwUserlogFlowTotalPackets, hwUserlogAccessHostAddress=hwUserlogAccessHostAddress, hwUserlogNatRunSlotNumber=hwUserlogNatRunSlotNumber, hwUserlogGroups=hwUserlogGroups, hwUserlogNatCfgSlotNumber=hwUserlogNatCfgSlotNumber, hwUserlogAccessSlotRunInfoEntry=hwUserlogAccessSlotRunInfoEntry, hwUserlogAccessSlotCfgInfoTable=hwUserlogAccessSlotCfgInfoTable, hwUserlogNatAclNumber=hwUserlogNatAclNumber, hwUserlogNatSlotRunInfoTable=hwUserlogNatSlotRunInfoTable, hwUserlogNatActiveTime=hwUserlogNatActiveTime, hwUserlogNatEnable=hwUserlogNatEnable, hwUserlogFlowAclNumber=hwUserlogFlowAclNumber, hwUserlogFlowRunSlotNumber=hwUserlogFlowRunSlotNumber, hwUserlogAccessFailedPackets=hwUserlogAccessFailedPackets, hwUserlogObjects=hwUserlogObjects, hwUserLogMIB=hwUserLogMIB, hwUserlogAccessFailedEntries=hwUserlogAccessFailedEntries, hwUserlogNatFlowBegin=hwUserlogNatFlowBegin)
