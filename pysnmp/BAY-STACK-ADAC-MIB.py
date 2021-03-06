#
# PySNMP MIB module BAY-STACK-ADAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-ADAC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
VlanIdOrNone, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, ObjectIdentity, iso, MibIdentifier, Unsigned32, TimeTicks, Gauge32, IpAddress, NotificationType, Integer32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "ObjectIdentity", "iso", "MibIdentifier", "Unsigned32", "TimeTicks", "Gauge32", "IpAddress", "NotificationType", "Integer32", "Counter64", "Counter32")
TruthValue, MacAddress, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "RowStatus", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackAdacMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 9))
bayStackAdacMib.setRevisions(('2014-04-14 00:00', '2009-05-20 00:00', '2006-10-16 00:00', '2006-05-24 00:00', '2006-03-13 00:00', '2005-04-12 00:00', '2004-12-13 00:00',))
if mibBuilder.loadTexts: bayStackAdacMib.setLastUpdated('201404140000Z')
if mibBuilder.loadTexts: bayStackAdacMib.setOrganization('Avaya')
bsAdacNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 9, 0))
bsAdacObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 9, 1))
bsAdacScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1))
bsAdacAdminEnable = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacAdminEnable.setStatus('current')
bsAdacOperatingMode = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("untaggedFramesBasic", 1), ("untaggedFramesAdvanced", 2), ("taggedFrames", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacOperatingMode.setStatus('current')
bsAdacCallServerPort = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacCallServerPort.setStatus('current')
bsAdacUplinkPort = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacUplinkPort.setStatus('current')
bsAdacVoiceVlan = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 6), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacVoiceVlan.setStatus('current')
bsAdacNotificationControlEnable = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacNotificationControlEnable.setStatus('current')
bsAdacMacAddrRangeControl = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("clearTable", 2), ("defaultTable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacMacAddrRangeControl.setStatus('current')
bsAdacOperEnable = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsAdacOperEnable.setStatus('current')
bsAdacCallServerPortList = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 10), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacCallServerPortList.setStatus('current')
bsAdacUplinkPortList = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 11), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacUplinkPortList.setStatus('current')
bsAdacUplinkType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port", 1), ("spbm", 2))).clone('port')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacUplinkType.setStatus('current')
bsAdacPortTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2), )
if mibBuilder.loadTexts: bsAdacPortTable.setStatus('current')
bsAdacPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-ADAC-MIB", "bsAdacPortIndex"))
if mibBuilder.loadTexts: bsAdacPortEntry.setStatus('current')
bsAdacPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsAdacPortIndex.setStatus('current')
bsAdacPortAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacPortAdminEnable.setStatus('current')
bsAdacPortConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configApplied", 1), ("configNotApplied", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsAdacPortConfigStatus.setStatus('current')
bsAdacPortTaggedFramesPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacPortTaggedFramesPvid.setStatus('current')
bsAdacPortTaggedFramesTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tagAll", 1), ("tagPvidOnly", 2), ("untagPvidOnly", 3), ("noChange", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacPortTaggedFramesTagging.setStatus('current')
bsAdacPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("telephony", 1), ("callServer", 2), ("uplink", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsAdacPortType.setStatus('current')
bsAdacPortOperEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsAdacPortOperEnable.setStatus('current')
bsAdacPortMacDetectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacPortMacDetectionEnable.setStatus('current')
bsAdacPortLldpDetectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsAdacPortLldpDetectionEnable.setStatus('current')
bsAdacMacAddrRangeTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3), )
if mibBuilder.loadTexts: bsAdacMacAddrRangeTable.setStatus('current')
bsAdacMacAddrRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-ADAC-MIB", "bsAdacMacAddrRangeLowEndIndex"), (0, "BAY-STACK-ADAC-MIB", "bsAdacMacAddrRangeHighEndIndex"))
if mibBuilder.loadTexts: bsAdacMacAddrRangeEntry.setStatus('current')
bsAdacMacAddrRangeLowEndIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: bsAdacMacAddrRangeLowEndIndex.setStatus('current')
bsAdacMacAddrRangeHighEndIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1, 2), MacAddress())
if mibBuilder.loadTexts: bsAdacMacAddrRangeHighEndIndex.setStatus('current')
bsAdacMacAddrRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsAdacMacAddrRangeRowStatus.setStatus('current')
bsAdacPortConfigNotification = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 9, 0, 1)).setObjects(("BAY-STACK-ADAC-MIB", "bsAdacPortConfigStatus"))
if mibBuilder.loadTexts: bsAdacPortConfigNotification.setStatus('current')
bsAdacPortOperDisabledNotification = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 9, 0, 2)).setObjects(("BAY-STACK-ADAC-MIB", "bsAdacPortOperEnable"))
if mibBuilder.loadTexts: bsAdacPortOperDisabledNotification.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-ADAC-MIB", bsAdacPortTaggedFramesTagging=bsAdacPortTaggedFramesTagging, bsAdacPortConfigStatus=bsAdacPortConfigStatus, bsAdacPortLldpDetectionEnable=bsAdacPortLldpDetectionEnable, bsAdacNotifications=bsAdacNotifications, bsAdacMacAddrRangeTable=bsAdacMacAddrRangeTable, bsAdacScalars=bsAdacScalars, bsAdacPortMacDetectionEnable=bsAdacPortMacDetectionEnable, bsAdacOperatingMode=bsAdacOperatingMode, bsAdacAdminEnable=bsAdacAdminEnable, bsAdacVoiceVlan=bsAdacVoiceVlan, bsAdacUplinkType=bsAdacUplinkType, bsAdacUplinkPortList=bsAdacUplinkPortList, bsAdacPortAdminEnable=bsAdacPortAdminEnable, bsAdacPortEntry=bsAdacPortEntry, bsAdacMacAddrRangeHighEndIndex=bsAdacMacAddrRangeHighEndIndex, bsAdacPortConfigNotification=bsAdacPortConfigNotification, bsAdacPortOperEnable=bsAdacPortOperEnable, bsAdacMacAddrRangeEntry=bsAdacMacAddrRangeEntry, bsAdacNotificationControlEnable=bsAdacNotificationControlEnable, PYSNMP_MODULE_ID=bayStackAdacMib, bsAdacCallServerPort=bsAdacCallServerPort, bayStackAdacMib=bayStackAdacMib, bsAdacMacAddrRangeControl=bsAdacMacAddrRangeControl, bsAdacOperEnable=bsAdacOperEnable, bsAdacCallServerPortList=bsAdacCallServerPortList, bsAdacMacAddrRangeRowStatus=bsAdacMacAddrRangeRowStatus, bsAdacPortType=bsAdacPortType, bsAdacPortIndex=bsAdacPortIndex, bsAdacObjects=bsAdacObjects, bsAdacPortOperDisabledNotification=bsAdacPortOperDisabledNotification, bsAdacMacAddrRangeLowEndIndex=bsAdacMacAddrRangeLowEndIndex, bsAdacPortTaggedFramesPvid=bsAdacPortTaggedFramesPvid, bsAdacUplinkPort=bsAdacUplinkPort, bsAdacPortTable=bsAdacPortTable)
