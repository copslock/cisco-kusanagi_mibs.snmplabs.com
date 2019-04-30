#
# PySNMP MIB module DHCP-RELAY-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DHCP-RELAY-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:31:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Counter64, Unsigned32, IpAddress, TimeTicks, MibIdentifier, Gauge32, Integer32, Bits, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Counter64", "Unsigned32", "IpAddress", "TimeTicks", "MibIdentifier", "Gauge32", "Integer32", "Bits", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, MacAddress, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "RowStatus")
swDHCPRelayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 42))
if mibBuilder.loadTexts: swDHCPRelayMIB.setLastUpdated('201005280000Z')
if mibBuilder.loadTexts: swDHCPRelayMIB.setOrganization('D-Link Corp.')
swDHCPRelayCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 42, 1))
swDHCPRelayInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 42, 2))
swDHCPRelayMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 42, 3))
swDHCPLocalRelayMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 42, 4))
swDHCPRelayOption82 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2))
swDHCPRelayOption60 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3))
swDHCPRelayOption61 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4))
swDHCPRelayState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayState.setStatus('current')
swDHCPRelayHopCount = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayHopCount.setStatus('current')
swDHCPRelayTimeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayTimeThreshold.setStatus('current')
swDHCPRelayCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1), )
if mibBuilder.loadTexts: swDHCPRelayCtrlTable.setStatus('current')
swDHCPRelayCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1), ).setIndexNames((0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayCtrlInterfaceName"), (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayCtrlServer"))
if mibBuilder.loadTexts: swDHCPRelayCtrlEntry.setStatus('current')
swDHCPRelayCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDHCPRelayCtrlInterfaceName.setStatus('current')
swDHCPRelayCtrlServer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDHCPRelayCtrlServer.setStatus('current')
swDHCPRelayCtrlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayCtrlRowStatus.setStatus('current')
swDHCPRelayOption82State = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption82State.setStatus('current')
swDHCPRelayOption82CheckState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption82CheckState.setStatus('current')
swDHCPRelayOption82Policy = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("replace", 1), ("drop", 2), ("keep", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption82Policy.setStatus('current')
swDHCPRelayOption82RemoteIDType = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("user-defined", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption82RemoteIDType.setStatus('current')
swDHCPRelayOption82RemoteID = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption82RemoteID.setStatus('current')
swDHCPRelayOption60State = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption60State.setStatus('current')
swDHCPRelayOption60DefMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("relay", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption60DefMode.setStatus('current')
swDHCPRelayOption60DefTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3), )
if mibBuilder.loadTexts: swDHCPRelayOption60DefTable.setStatus('current')
swDHCPRelayOption60DefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3, 1), ).setIndexNames((0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption60DefRelayIp"))
if mibBuilder.loadTexts: swDHCPRelayOption60DefEntry.setStatus('current')
swDHCPRelayOption60DefRelayIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDHCPRelayOption60DefRelayIp.setStatus('current')
swDHCPRelayOption60DefRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayOption60DefRowStatus.setStatus('current')
swDHCPRelayOption60Table = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4), )
if mibBuilder.loadTexts: swDHCPRelayOption60Table.setStatus('current')
swDHCPRelayOption60Entry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1), ).setIndexNames((0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption60String"), (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption60RelayIp"))
if mibBuilder.loadTexts: swDHCPRelayOption60Entry.setStatus('current')
swDHCPRelayOption60String = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDHCPRelayOption60String.setStatus('current')
swDHCPRelayOption60RelayIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDHCPRelayOption60RelayIp.setStatus('current')
swDHCPRelayOption60MatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exact", 1), ("partial", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayOption60MatchType.setStatus('current')
swDHCPRelayOption60RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayOption60RowStatus.setStatus('current')
swDHCPRelayOption61State = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption61State.setStatus('current')
swDHCPRelayOption61DefMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("relay", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption61DefMode.setStatus('current')
swDHCPRelayOption61DefRelayIp = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPRelayOption61DefRelayIp.setStatus('current')
swDHCPRelayOption61Table = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4), )
if mibBuilder.loadTexts: swDHCPRelayOption61Table.setStatus('current')
swDHCPRelayOption61Entry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1), ).setIndexNames((0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption61ClientType"), (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption61ClientID"))
if mibBuilder.loadTexts: swDHCPRelayOption61Entry.setStatus('current')
swDHCPRelayOption61ClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mac", 1), ("string", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDHCPRelayOption61ClientType.setStatus('current')
swDHCPRelayOption61ClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDHCPRelayOption61ClientID.setStatus('current')
swDHCPRelayOption61Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("relay", 1), ("drop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayOption61Mode.setStatus('current')
swDHCPRelayOption61RelayIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayOption61RelayIp.setStatus('current')
swDHCPRelayOption61RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayOption61RowStatus.setStatus('current')
swDHCPRelayVlanCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5), )
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlTable.setStatus('current')
swDHCPRelayVlanCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1), ).setIndexNames((0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayVlanCtrlServer"))
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlEntry.setStatus('current')
swDHCPRelayVlanCtrlServer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlServer.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList1to64 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList1to64.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList65to128 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList65to128.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList129to192 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList129to192.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList193to256 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList193to256.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList257to320 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList257to320.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList321to384 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList321to384.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList385to448 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList385to448.setStatus('current')
swDHCPRelayVlanCtrlVlanRangeList449to512 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlVlanRangeList449to512.setStatus('current')
swDHCPRelayVlanCtrlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swDHCPRelayVlanCtrlRowStatus.setStatus('current')
swDHCPLocalRelayGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPLocalRelayGlobalState.setStatus('current')
swDHCPLocalRelayVlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2), )
if mibBuilder.loadTexts: swDHCPLocalRelayVlanTable.setStatus('current')
swDHCPLocalRelayVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2, 1), ).setIndexNames((0, "DHCP-RELAY-MGMT-MIB", "swDHCPLocalRelayVlanID"))
if mibBuilder.loadTexts: swDHCPLocalRelayVlanEntry.setStatus('current')
swDHCPLocalRelayVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: swDHCPLocalRelayVlanID.setStatus('current')
swDHCPLocalRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDHCPLocalRelayState.setStatus('current')
mibBuilder.exportSymbols("DHCP-RELAY-MGMT-MIB", swDHCPRelayVlanCtrlServer=swDHCPRelayVlanCtrlServer, swDHCPRelayOption61DefRelayIp=swDHCPRelayOption61DefRelayIp, swDHCPLocalRelayState=swDHCPLocalRelayState, swDHCPRelayHopCount=swDHCPRelayHopCount, swDHCPLocalRelayVlanID=swDHCPLocalRelayVlanID, swDHCPRelayOption60Table=swDHCPRelayOption60Table, swDHCPRelayOption60=swDHCPRelayOption60, swDHCPRelayOption61=swDHCPRelayOption61, swDHCPRelayCtrlRowStatus=swDHCPRelayCtrlRowStatus, swDHCPRelayOption60DefMode=swDHCPRelayOption60DefMode, swDHCPRelayOption61RelayIp=swDHCPRelayOption61RelayIp, swDHCPRelayOption61State=swDHCPRelayOption61State, swDHCPRelayVlanCtrlEntry=swDHCPRelayVlanCtrlEntry, swDHCPRelayOption82Policy=swDHCPRelayOption82Policy, swDHCPRelayVlanCtrlRowStatus=swDHCPRelayVlanCtrlRowStatus, swDHCPRelayState=swDHCPRelayState, swDHCPRelayOption60MatchType=swDHCPRelayOption60MatchType, swDHCPRelayCtrlServer=swDHCPRelayCtrlServer, swDHCPRelayVlanCtrlVlanRangeList193to256=swDHCPRelayVlanCtrlVlanRangeList193to256, swDHCPRelayVlanCtrlVlanRangeList449to512=swDHCPRelayVlanCtrlVlanRangeList449to512, swDHCPRelayCtrl=swDHCPRelayCtrl, swDHCPRelayInfo=swDHCPRelayInfo, swDHCPRelayVlanCtrlVlanRangeList257to320=swDHCPRelayVlanCtrlVlanRangeList257to320, swDHCPLocalRelayVlanTable=swDHCPLocalRelayVlanTable, swDHCPRelayMgmt=swDHCPRelayMgmt, swDHCPRelayOption60String=swDHCPRelayOption60String, swDHCPRelayVlanCtrlVlanRangeList385to448=swDHCPRelayVlanCtrlVlanRangeList385to448, swDHCPLocalRelayVlanEntry=swDHCPLocalRelayVlanEntry, swDHCPLocalRelayMgmt=swDHCPLocalRelayMgmt, swDHCPRelayOption60DefRowStatus=swDHCPRelayOption60DefRowStatus, swDHCPRelayOption60RowStatus=swDHCPRelayOption60RowStatus, swDHCPRelayOption61ClientID=swDHCPRelayOption61ClientID, swDHCPRelayOption61RowStatus=swDHCPRelayOption61RowStatus, swDHCPRelayOption82=swDHCPRelayOption82, swDHCPRelayOption60RelayIp=swDHCPRelayOption60RelayIp, swDHCPRelayMIB=swDHCPRelayMIB, swDHCPRelayOption82RemoteID=swDHCPRelayOption82RemoteID, swDHCPRelayOption61Mode=swDHCPRelayOption61Mode, swDHCPRelayOption60DefEntry=swDHCPRelayOption60DefEntry, swDHCPRelayOption61Table=swDHCPRelayOption61Table, swDHCPRelayOption61Entry=swDHCPRelayOption61Entry, swDHCPRelayCtrlInterfaceName=swDHCPRelayCtrlInterfaceName, swDHCPRelayVlanCtrlVlanRangeList129to192=swDHCPRelayVlanCtrlVlanRangeList129to192, swDHCPRelayOption82RemoteIDType=swDHCPRelayOption82RemoteIDType, swDHCPRelayOption60State=swDHCPRelayOption60State, swDHCPRelayCtrlEntry=swDHCPRelayCtrlEntry, swDHCPRelayOption61DefMode=swDHCPRelayOption61DefMode, swDHCPRelayVlanCtrlVlanRangeList1to64=swDHCPRelayVlanCtrlVlanRangeList1to64, swDHCPRelayOption60DefTable=swDHCPRelayOption60DefTable, swDHCPRelayVlanCtrlVlanRangeList321to384=swDHCPRelayVlanCtrlVlanRangeList321to384, swDHCPLocalRelayGlobalState=swDHCPLocalRelayGlobalState, swDHCPRelayVlanCtrlTable=swDHCPRelayVlanCtrlTable, PYSNMP_MODULE_ID=swDHCPRelayMIB, swDHCPRelayOption61ClientType=swDHCPRelayOption61ClientType, swDHCPRelayOption60DefRelayIp=swDHCPRelayOption60DefRelayIp, swDHCPRelayOption82CheckState=swDHCPRelayOption82CheckState, swDHCPRelayVlanCtrlVlanRangeList65to128=swDHCPRelayVlanCtrlVlanRangeList65to128, swDHCPRelayOption82State=swDHCPRelayOption82State, swDHCPRelayCtrlTable=swDHCPRelayCtrlTable, swDHCPRelayTimeThreshold=swDHCPRelayTimeThreshold, swDHCPRelayOption60Entry=swDHCPRelayOption60Entry)