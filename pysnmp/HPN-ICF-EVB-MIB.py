#
# PySNMP MIB module HPN-ICF-EVB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-EVB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
IEEE8021BridgePortNumber, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Bits, Gauge32, iso, MibIdentifier, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Bits", "Gauge32", "iso", "MibIdentifier", "IpAddress", "Integer32")
MacAddress, TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
hpnicfEvb = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134))
hpnicfEvb.setRevisions(('2012-12-21 12:00',))
if mibBuilder.loadTexts: hpnicfEvb.setLastUpdated('201212211200Z')
if mibBuilder.loadTexts: hpnicfEvb.setOrganization('')
hpnicfEvbSysObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1))
hpnicfEvbPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2))
hpnicfFlex10Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3))
hpnicfEvbSetResult = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("processing", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEvbSetResult.setStatus('current')
hpnicfEvbDefaultManagerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2), )
if mibBuilder.loadTexts: hpnicfEvbDefaultManagerTable.setStatus('current')
hpnicfEvbDefaultManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbManagerIndex"))
if mibBuilder.loadTexts: hpnicfEvbDefaultManagerEntry.setStatus('current')
hpnicfEvbManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbManagerIndex.setStatus('current')
hpnicfEvbManagerType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ("name", 3), ("local", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerType.setStatus('current')
hpnicfEvbManagerID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerID.setStatus('current')
hpnicfEvbManagerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(8080)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerPort.setStatus('current')
hpnicfEvbManagerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerRowStatus.setStatus('current')
hpnicfEvbPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1), )
if mibBuilder.loadTexts: hpnicfEvbPortConfigTable.setStatus('current')
hpnicfEvbPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbPortNumber"))
if mibBuilder.loadTexts: hpnicfEvbPortConfigEntry.setStatus('current')
hpnicfEvbPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hpnicfEvbPortNumber.setStatus('current')
hpnicfEvbRWD = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 31)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbRWD.setStatus('current')
hpnicfEvbRKA = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(14, 31)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbRKA.setStatus('current')
hpnicfEvbSchannelConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2), )
if mibBuilder.loadTexts: hpnicfEvbSchannelConfigTable.setStatus('current')
hpnicfEvbSchannelConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbPortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"))
if mibBuilder.loadTexts: hpnicfEvbSchannelConfigEntry.setStatus('current')
hpnicfEvbSchannelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbSchannelID.setStatus('current')
hpnicfEvbSchannelSVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbSchannelSVLAN.setStatus('current')
hpnicfEvbMacLearningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbMacLearningStatus.setStatus('current')
hpnicfEvbRRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbRRStatus.setStatus('current')
hpnicfEvbSchannelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbSchannelRowStatus.setStatus('current')
hpnicfEvbVSIConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3), )
if mibBuilder.loadTexts: hpnicfEvbVSIConfigTable.setStatus('current')
hpnicfEvbVSIConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbSBPPortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSILocalID"))
if mibBuilder.loadTexts: hpnicfEvbVSIConfigEntry.setStatus('current')
hpnicfEvbSBPPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hpnicfEvbSBPPortNumber.setStatus('current')
hpnicfEvbVSILocalID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbVSILocalID.setStatus('current')
hpnicfEvbVSICommand = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("preAssociate", 1), ("preAssociateWithRsrcReservation", 2), ("associate", 3), ("deAssociate", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbVSICommand.setStatus('current')
hpnicfEvbVSIIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEvbVSIIfIndex.setStatus('current')
hpnicfEvbVSIIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbVSIIsActive.setStatus('current')
hpnicfEvbVSIRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbVSIRowStatus.setStatus('current')
hpnicfEvbVSIFilterConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4), )
if mibBuilder.loadTexts: hpnicfEvbVSIFilterConfigTable.setStatus('current')
hpnicfEvbVSIFilterConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbSBPPortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSILocalID"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbGroupID"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSIMac"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSIVlanId"))
if mibBuilder.loadTexts: hpnicfEvbVSIFilterConfigEntry.setStatus('current')
hpnicfEvbGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbGroupID.setStatus('current')
hpnicfEvbVSIMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: hpnicfEvbVSIMac.setStatus('current')
hpnicfEvbVSIVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 3), VlanIndex())
if mibBuilder.loadTexts: hpnicfEvbVSIVlanId.setStatus('current')
hpnicfEvbVSIFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbVSIFilterRowStatus.setStatus('current')
hpnicfFlex10PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1), )
if mibBuilder.loadTexts: hpnicfFlex10PortConfigTable.setStatus('current')
hpnicfFlex10PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"))
if mibBuilder.loadTexts: hpnicfFlex10PortConfigEntry.setStatus('current')
hpnicfFlex10PortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hpnicfFlex10PortNumber.setStatus('current')
hpnicfFlex10PortEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFlex10PortEnableStatus.setStatus('current')
hpnicfFlex10RemoteSchannelTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2), )
if mibBuilder.loadTexts: hpnicfFlex10RemoteSchannelTable.setStatus('current')
hpnicfFlex10RemoteSchannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"))
if mibBuilder.loadTexts: hpnicfFlex10RemoteSchannelEntry.setStatus('current')
hpnicfFlex10RemSchDesFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 1), Bits().clone(namedValues=NamedValues(("format0", 0), ("format1", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchDesFormat.setStatus('current')
hpnicfFlex10RemSchTerminationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchTerminationType.setStatus('current')
hpnicfFlex10RemSchTerminationCap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 3), Bits().clone(namedValues=NamedValues(("ethernet", 0), ("fCOE", 1), ("iSCSI", 2), ("roCEE", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchTerminationCap.setStatus('current')
hpnicfFlex10RemSchTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 4), Bits().clone(namedValues=NamedValues(("class0", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6), ("class7", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchTrafficClass.setStatus('current')
hpnicfFlex10RemSchCir = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 5), Integer32()).setUnits('mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchCir.setStatus('current')
hpnicfFlex10RemSchPir = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 6), Integer32()).setUnits('mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchPir.setStatus('current')
hpnicfFlex10RemSchConnectionID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchConnectionID.setStatus('current')
hpnicfFlex10SchannelLinkCtlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3), )
if mibBuilder.loadTexts: hpnicfFlex10SchannelLinkCtlTable.setStatus('current')
hpnicfFlex10SchannelLinkCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"))
if mibBuilder.loadTexts: hpnicfFlex10SchannelLinkCtlEntry.setStatus('current')
hpnicfFlex10SchannelSVID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 1), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10SchannelSVID.setStatus('current')
hpnicfFlex10SchannelLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10SchannelLocalStatus.setStatus('current')
hpnicfFlex10SchannelRemoteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10SchannelRemoteStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-EVB-MIB", hpnicfEvbVSICommand=hpnicfEvbVSICommand, hpnicfEvbManagerID=hpnicfEvbManagerID, hpnicfFlex10RemSchTrafficClass=hpnicfFlex10RemSchTrafficClass, hpnicfEvbVSIIsActive=hpnicfEvbVSIIsActive, hpnicfFlex10PortConfigEntry=hpnicfFlex10PortConfigEntry, hpnicfEvbVSIConfigEntry=hpnicfEvbVSIConfigEntry, hpnicfEvbSetResult=hpnicfEvbSetResult, hpnicfEvbVSIConfigTable=hpnicfEvbVSIConfigTable, hpnicfEvbGroupID=hpnicfEvbGroupID, hpnicfEvbPortConfigTable=hpnicfEvbPortConfigTable, hpnicfEvbSchannelSVLAN=hpnicfEvbSchannelSVLAN, hpnicfEvbVSIIfIndex=hpnicfEvbVSIIfIndex, hpnicfFlex10RemoteSchannelEntry=hpnicfFlex10RemoteSchannelEntry, hpnicfFlex10PortConfigTable=hpnicfFlex10PortConfigTable, hpnicfEvbVSIFilterConfigTable=hpnicfEvbVSIFilterConfigTable, hpnicfFlex10RemSchDesFormat=hpnicfFlex10RemSchDesFormat, hpnicfFlex10SchannelSVID=hpnicfFlex10SchannelSVID, hpnicfEvbVSILocalID=hpnicfEvbVSILocalID, hpnicfEvbSysObjects=hpnicfEvbSysObjects, hpnicfEvbSchannelConfigTable=hpnicfEvbSchannelConfigTable, hpnicfEvbRKA=hpnicfEvbRKA, hpnicfEvbRWD=hpnicfEvbRWD, hpnicfEvbSchannelID=hpnicfEvbSchannelID, hpnicfEvbManagerRowStatus=hpnicfEvbManagerRowStatus, hpnicfEvbVSIMac=hpnicfEvbVSIMac, hpnicfFlex10SchannelLinkCtlEntry=hpnicfFlex10SchannelLinkCtlEntry, hpnicfFlex10RemSchPir=hpnicfFlex10RemSchPir, hpnicfFlex10SchannelLocalStatus=hpnicfFlex10SchannelLocalStatus, hpnicfEvbVSIFilterConfigEntry=hpnicfEvbVSIFilterConfigEntry, hpnicfEvbDefaultManagerEntry=hpnicfEvbDefaultManagerEntry, hpnicfEvbManagerIndex=hpnicfEvbManagerIndex, hpnicfFlex10RemSchTerminationCap=hpnicfFlex10RemSchTerminationCap, hpnicfEvbManagerPort=hpnicfEvbManagerPort, hpnicfFlex10SchannelLinkCtlTable=hpnicfFlex10SchannelLinkCtlTable, hpnicfEvbPortConfigEntry=hpnicfEvbPortConfigEntry, hpnicfFlex10SchannelRemoteStatus=hpnicfFlex10SchannelRemoteStatus, hpnicfEvbVSIVlanId=hpnicfEvbVSIVlanId, hpnicfFlex10PortEnableStatus=hpnicfFlex10PortEnableStatus, hpnicfEvbRRStatus=hpnicfEvbRRStatus, hpnicfEvbMacLearningStatus=hpnicfEvbMacLearningStatus, hpnicfFlex10RemSchTerminationType=hpnicfFlex10RemSchTerminationType, hpnicfEvbSchannelRowStatus=hpnicfEvbSchannelRowStatus, hpnicfEvbVSIRowStatus=hpnicfEvbVSIRowStatus, hpnicfFlex10RemSchConnectionID=hpnicfFlex10RemSchConnectionID, hpnicfEvbSBPPortNumber=hpnicfEvbSBPPortNumber, hpnicfEvbVSIFilterRowStatus=hpnicfEvbVSIFilterRowStatus, hpnicfFlex10PortNumber=hpnicfFlex10PortNumber, hpnicfEvbPortObjects=hpnicfEvbPortObjects, hpnicfFlex10RemSchCir=hpnicfFlex10RemSchCir, PYSNMP_MODULE_ID=hpnicfEvb, hpnicfEvbManagerType=hpnicfEvbManagerType, hpnicfFlex10Objects=hpnicfFlex10Objects, hpnicfEvbPortNumber=hpnicfEvbPortNumber, hpnicfEvbSchannelConfigEntry=hpnicfEvbSchannelConfigEntry, hpnicfFlex10RemoteSchannelTable=hpnicfFlex10RemoteSchannelTable, hpnicfEvb=hpnicfEvb, hpnicfEvbDefaultManagerTable=hpnicfEvbDefaultManagerTable)
