#
# PySNMP MIB module SWL3MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWL3MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:06:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
TOSType, AreaID, Metric = mibBuilder.importSymbols("OSPF-MIB", "TOSType", "AreaID", "Metric")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ObjectIdentity, Counter32, TimeTicks, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, Gauge32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Gauge32", "NotificationType", "iso")
PhysAddress, TruthValue, TimeStamp, RowStatus, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TruthValue", "TimeStamp", "RowStatus", "TextualConvention", "MacAddress", "DisplayString")
privateMgmt, = mibBuilder.importSymbols("SWPRIMGMT-MIB", "privateMgmt")
swL3MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3))
if mibBuilder.loadTexts: swL3MgmtMIB.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swL3MgmtMIB.setOrganization('enterprise, Inc.')
class NodeAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NetAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

swL3DevMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1))
swL3IpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2))
swL3RelayMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3))
swL3IpCtrlMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1))
swL3IpFdbMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2))
swL3IpFilterMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3))
swL3RelayBootpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1))
swL3RelayDnsMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2))
swL3DevCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1))
swL3DevCtrlRIPState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3DevCtrlRIPState.setStatus('current')
swL3DevCtrlOSPFState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3DevCtrlOSPFState.setStatus('current')
swL3DevCtrlDVMRPState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3DevCtrlDVMRPState.setStatus('current')
swL3DevCtrlVRRPState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3DevCtrlVRRPState.setStatus('current')
swL3DevCtrlVRRPPingVirtualAddrState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3DevCtrlVRRPPingVirtualAddrState.setStatus('current')
swL3IpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1), )
if mibBuilder.loadTexts: swL3IpCtrlTable.setStatus('current')
swL3IpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3IpCtrlInterfaceName"))
if mibBuilder.loadTexts: swL3IpCtrlEntry.setStatus('current')
swL3IpCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setStatus('current')
swL3IpCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIfIndex.setStatus('current')
swL3IpCtrlIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpAddr.setStatus('current')
swL3IpCtrlIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpSubnetMask.setStatus('current')
swL3IpCtrlVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlVlanName.setStatus('current')
swL3IpCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("manual", 2), ("bootp", 3), ("dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlMode.setStatus('current')
swL3IpCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpCtrlState.setStatus('current')
swL3IpCtrlOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlOperState.setStatus('current')
swL3IpFdbInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1), )
if mibBuilder.loadTexts: swL3IpFdbInfoTable.setStatus('current')
swL3IpFdbInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3IpFdbInfoIpAddr"))
if mibBuilder.loadTexts: swL3IpFdbInfoEntry.setStatus('current')
swL3IpFdbInfoIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoIpAddr.setStatus('current')
swL3IpFdbInfoIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoIpSubnetMask.setStatus('current')
swL3IpFdbInfoPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoPort.setStatus('current')
swL3IpFdbInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("dynamic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoType.setStatus('current')
swL3IpFilterAddrConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1))
swL3IpFilterAddrMaxSupportedEntries = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFilterAddrMaxSupportedEntries.setStatus('current')
swL3IpFilterAddrCurrentTotalEntries = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFilterAddrCurrentTotalEntries.setStatus('current')
swL3IpFilterAddrCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3), )
if mibBuilder.loadTexts: swL3IpFilterAddrCtrlTable.setStatus('current')
swL3IpFilterAddrCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3IpFilterAddrIpAddr"))
if mibBuilder.loadTexts: swL3IpFilterAddrCtrlEntry.setStatus('current')
swL3IpFilterAddrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFilterAddrIpAddr.setStatus('current')
swL3IpFilterAddrCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("dst-addr", 2), ("src-addr", 3), ("dst-src-addr", 4), ("invalid", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpFilterAddrCtrlState.setStatus('current')
swL3IpArpAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpArpAgingTime.setStatus('current')
swL3IpStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5), )
if mibBuilder.loadTexts: swL3IpStaticRouteTable.setStatus('current')
swL3IpStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3IpStaticRouteDest"), (0, "SWL3MGMT-MIB", "swL3IpStaticRouteMask"), (0, "SWL3MGMT-MIB", "swL3IpStaticRouteNextHop"))
if mibBuilder.loadTexts: swL3IpStaticRouteEntry.setStatus('current')
swL3IpStaticRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpStaticRouteDest.setStatus('current')
swL3IpStaticRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpStaticRouteMask.setStatus('current')
swL3IpStaticRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpStaticRouteNextHop.setStatus('current')
swL3IpStaticRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpStaticRouteMetric.setStatus('current')
swL3IpStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpStaticRouteStatus.setStatus('current')
swL3IpArpTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6), )
if mibBuilder.loadTexts: swL3IpArpTable.setStatus('current')
swL3IpArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3IpArpIfIndex"), (0, "SWL3MGMT-MIB", "swL3IpArpNetAddress"))
if mibBuilder.loadTexts: swL3IpArpEntry.setStatus('current')
swL3IpArpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpArpIfIndex.setStatus('current')
swL3IpArpNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpArpNetAddress.setStatus('current')
swL3IpArpPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpArpPhysAddress.setStatus('current')
swL3IpArpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("dynamic", 3), ("static", 4), ("local", 5), ("local-broadcast", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpArpType.setStatus('current')
swL3IpArpDynamicAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpArpDynamicAgingTime.setStatus('current')
swL3IpArpReqRateLimitState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpArpReqRateLimitState.setStatus('current')
swL3IpArpReqRateLimitValue = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpArpReqRateLimitValue.setStatus('current')
swL3RelayBootpState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayBootpState.setStatus('current')
swL3RelayBootpHopCount = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayBootpHopCount.setStatus('current')
swL3RelayBootpTimeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayBootpTimeThreshold.setStatus('current')
swL3RelayBootpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4), )
if mibBuilder.loadTexts: swL3RelayBootpCtrlTable.setStatus('current')
swL3RelayBootpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3RelayBootpCtrlInterfaceName"), (0, "SWL3MGMT-MIB", "swL3RelayBootpCtrlServer"))
if mibBuilder.loadTexts: swL3RelayBootpCtrlEntry.setStatus('current')
swL3RelayBootpCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3RelayBootpCtrlInterfaceName.setStatus('current')
swL3RelayBootpCtrlServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3RelayBootpCtrlServer.setStatus('current')
swL3RelayBootpCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayBootpCtrlState.setStatus('current')
swL3RelayDnsState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayDnsState.setStatus('current')
swL3RelayDnsPrimaryServer = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayDnsPrimaryServer.setStatus('current')
swL3RelayDnsSecondaryServer = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayDnsSecondaryServer.setStatus('current')
swL3RelayDnsCacheState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayDnsCacheState.setStatus('current')
swL3RelayDnsStaticTableState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayDnsStaticTableState.setStatus('current')
swL3RelayDnsCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6), )
if mibBuilder.loadTexts: swL3RelayDnsCtrlTable.setStatus('current')
swL3RelayDnsCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3RelayDnsCtrlDomainName"), (0, "SWL3MGMT-MIB", "swL3RelayDnsCtrlIpAddr"))
if mibBuilder.loadTexts: swL3RelayDnsCtrlEntry.setStatus('current')
swL3RelayDnsCtrlDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3RelayDnsCtrlDomainName.setStatus('current')
swL3RelayDnsCtrlIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3RelayDnsCtrlIpAddr.setStatus('current')
swL3RelayDnsCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 3, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RelayDnsCtrlState.setStatus('current')
swL3Md5Table = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4), )
if mibBuilder.loadTexts: swL3Md5Table.setStatus('current')
swL3Md5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3Md5KeyId"))
if mibBuilder.loadTexts: swL3Md5Entry.setStatus('current')
swL3Md5KeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Md5KeyId.setStatus('current')
swL3Md5Key = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Md5Key.setStatus('current')
swL3Md5State = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Md5State.setStatus('current')
swL3RouteRedistriTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5), )
if mibBuilder.loadTexts: swL3RouteRedistriTable.setStatus('current')
swL3RouteRedistriEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3RouteRedistriSrcProtocol"), (0, "SWL3MGMT-MIB", "swL3RouteRedistriDstProtocol"))
if mibBuilder.loadTexts: swL3RouteRedistriEntry.setStatus('current')
swL3RouteRedistriSrcProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("rip", 2), ("ospf", 3), ("static", 4), ("local", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3RouteRedistriSrcProtocol.setStatus('current')
swL3RouteRedistriDstProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("rip", 2), ("ospf", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3RouteRedistriDstProtocol.setStatus('current')
swL3RouteRedistriType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("all", 2), ("type-1", 3), ("type-2", 4), ("internal", 5), ("external", 6), ("inter-E1", 7), ("inter-E2", 8), ("extType1", 9), ("extType2", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RouteRedistriType.setStatus('current')
swL3RouteRedistriMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777214))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RouteRedistriMetric.setStatus('current')
swL3RouteRedistriState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RouteRedistriState.setStatus('current')
swL3OspfHostTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6), )
if mibBuilder.loadTexts: swL3OspfHostTable.setStatus('current')
swL3OspfHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3OspfHostIpAddress"), (0, "SWL3MGMT-MIB", "swL3OspfHostTOS"))
if mibBuilder.loadTexts: swL3OspfHostEntry.setStatus('current')
swL3OspfHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3OspfHostIpAddress.setStatus('current')
swL3OspfHostTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 2), TOSType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3OspfHostTOS.setStatus('current')
swL3OspfHostMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 3), Metric()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3OspfHostMetric.setStatus('current')
swL3OspfHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3OspfHostStatus.setStatus('current')
swL3OspfHostAreaID = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 6, 1, 5), AreaID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3OspfHostAreaID.setStatus('current')
swL3VrrpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7))
swL3VrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1), )
if mibBuilder.loadTexts: swL3VrrpOperTable.setStatus('current')
swL3VrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SWL3MGMT-MIB", "swL3VrrpOperVrId"))
if mibBuilder.loadTexts: swL3VrrpOperEntry.setStatus('current')
swL3VrrpOperVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: swL3VrrpOperVrId.setStatus('current')
swL3VrrpOperCriticalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3VrrpOperCriticalIpAddr.setStatus('current')
swL3VrrpOperCriticalIpState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3VrrpOperCriticalIpState.setStatus('current')
swL3VrrpOperHoldDownTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 21600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3VrrpOperHoldDownTimer.setStatus('current')
swL3RoutePrefTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8), )
if mibBuilder.loadTexts: swL3RoutePrefTable.setStatus('current')
swL3RoutePrefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3RoutePrefProtocol"))
if mibBuilder.loadTexts: swL3RoutePrefEntry.setStatus('current')
swL3RoutePrefProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("isis", 1), ("rip", 2), ("ospfIntra", 3), ("static", 4), ("local", 5), ("bgp", 6), ("staticLow", 7), ("ospfInter", 8), ("ospfExternal", 9), ("ospfExternal1", 10), ("ospfExternal2", 11), ("ospfNssa1", 12), ("ospfNssa2", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3RoutePrefProtocol.setStatus('current')
swL3RoutePrefValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3RoutePrefValue.setStatus('current')
swL3DvmrpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9), )
if mibBuilder.loadTexts: swL3DvmrpInterfaceTable.setStatus('current')
swL3DvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1), ).setIndexNames((0, "SWL3MGMT-MIB", "swL3DvmrpInterfaceIfIndex"))
if mibBuilder.loadTexts: swL3DvmrpInterfaceEntry.setStatus('current')
swL3DvmrpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: swL3DvmrpInterfaceIfIndex.setStatus('current')
swL3DvmrpInterfaceNeighborTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(35)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3DvmrpInterfaceNeighborTimeout.setStatus('current')
swL3DvmrpInterfaceProbe = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 3, 9, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3DvmrpInterfaceProbe.setStatus('current')
mibBuilder.exportSymbols("SWL3MGMT-MIB", swL3IpFdbInfoType=swL3IpFdbInfoType, swL3IpCtrlInterfaceName=swL3IpCtrlInterfaceName, swL3DevMgmt=swL3DevMgmt, swL3IpArpAgingTime=swL3IpArpAgingTime, swL3IpFdbInfoEntry=swL3IpFdbInfoEntry, swL3IpFilterAddrIpAddr=swL3IpFilterAddrIpAddr, swL3IpFilterAddrCtrlEntry=swL3IpFilterAddrCtrlEntry, swL3OspfHostTable=swL3OspfHostTable, swL3OspfHostIpAddress=swL3OspfHostIpAddress, swL3IpArpDynamicAgingTime=swL3IpArpDynamicAgingTime, swL3RelayDnsCacheState=swL3RelayDnsCacheState, swL3IpArpEntry=swL3IpArpEntry, swL3IpStaticRouteMetric=swL3IpStaticRouteMetric, swL3RelayBootpHopCount=swL3RelayBootpHopCount, swL3IpCtrlState=swL3IpCtrlState, swL3IpStaticRouteMask=swL3IpStaticRouteMask, swL3Md5State=swL3Md5State, swL3RelayBootpState=swL3RelayBootpState, swL3IpFilterAddrConfig=swL3IpFilterAddrConfig, swL3IpArpType=swL3IpArpType, swL3IpCtrlMode=swL3IpCtrlMode, swL3RoutePrefProtocol=swL3RoutePrefProtocol, swL3IpFilterAddrCtrlState=swL3IpFilterAddrCtrlState, swL3OspfHostEntry=swL3OspfHostEntry, swL3IpCtrlIfIndex=swL3IpCtrlIfIndex, swL3IpFdbInfoTable=swL3IpFdbInfoTable, swL3RouteRedistriSrcProtocol=swL3RouteRedistriSrcProtocol, swL3IpArpTable=swL3IpArpTable, swL3RelayBootpTimeThreshold=swL3RelayBootpTimeThreshold, swL3RelayDnsCtrlIpAddr=swL3RelayDnsCtrlIpAddr, swL3RoutePrefValue=swL3RoutePrefValue, swL3IpCtrlIpSubnetMask=swL3IpCtrlIpSubnetMask, swL3IpFilterAddrCtrlTable=swL3IpFilterAddrCtrlTable, swL3IpStaticRouteNextHop=swL3IpStaticRouteNextHop, swL3RouteRedistriEntry=swL3RouteRedistriEntry, swL3RoutePrefEntry=swL3RoutePrefEntry, swL3VrrpOperEntry=swL3VrrpOperEntry, swL3DevCtrl=swL3DevCtrl, swL3IpArpReqRateLimitValue=swL3IpArpReqRateLimitValue, swL3RelayDnsSecondaryServer=swL3RelayDnsSecondaryServer, swL3RelayBootpCtrlEntry=swL3RelayBootpCtrlEntry, swL3RelayDnsCtrlEntry=swL3RelayDnsCtrlEntry, swL3IpCtrlOperState=swL3IpCtrlOperState, NodeAddress=NodeAddress, swL3IpMgmt=swL3IpMgmt, swL3IpCtrlTable=swL3IpCtrlTable, swL3IpCtrlEntry=swL3IpCtrlEntry, PYSNMP_MODULE_ID=swL3MgmtMIB, swL3RelayDnsState=swL3RelayDnsState, swL3DevCtrlRIPState=swL3DevCtrlRIPState, swL3IpFilterMgmt=swL3IpFilterMgmt, swL3OspfHostMetric=swL3OspfHostMetric, swL3RelayBootpCtrlServer=swL3RelayBootpCtrlServer, swL3RelayDnsMgmt=swL3RelayDnsMgmt, swL3RelayBootpCtrlState=swL3RelayBootpCtrlState, swL3DvmrpInterfaceEntry=swL3DvmrpInterfaceEntry, swL3RelayMgmt=swL3RelayMgmt, swL3IpStaticRouteTable=swL3IpStaticRouteTable, swL3RouteRedistriType=swL3RouteRedistriType, swL3VrrpOperTable=swL3VrrpOperTable, swL3IpStaticRouteDest=swL3IpStaticRouteDest, swL3RouteRedistriState=swL3RouteRedistriState, swL3RelayDnsCtrlState=swL3RelayDnsCtrlState, swL3RouteRedistriDstProtocol=swL3RouteRedistriDstProtocol, swL3RoutePrefTable=swL3RoutePrefTable, swL3IpFilterAddrMaxSupportedEntries=swL3IpFilterAddrMaxSupportedEntries, swL3IpArpNetAddress=swL3IpArpNetAddress, swL3MgmtMIB=swL3MgmtMIB, swL3Md5Entry=swL3Md5Entry, swL3VrrpMgmt=swL3VrrpMgmt, swL3IpFilterAddrCurrentTotalEntries=swL3IpFilterAddrCurrentTotalEntries, swL3OspfHostAreaID=swL3OspfHostAreaID, swL3Md5Table=swL3Md5Table, swL3IpStaticRouteStatus=swL3IpStaticRouteStatus, swL3IpCtrlMgmt=swL3IpCtrlMgmt, swL3RelayDnsPrimaryServer=swL3RelayDnsPrimaryServer, swL3DevCtrlVRRPPingVirtualAddrState=swL3DevCtrlVRRPPingVirtualAddrState, swL3RelayDnsCtrlDomainName=swL3RelayDnsCtrlDomainName, NetAddress=NetAddress, swL3DevCtrlVRRPState=swL3DevCtrlVRRPState, swL3IpFdbMgmt=swL3IpFdbMgmt, swL3VrrpOperCriticalIpState=swL3VrrpOperCriticalIpState, swL3OspfHostStatus=swL3OspfHostStatus, swL3DvmrpInterfaceIfIndex=swL3DvmrpInterfaceIfIndex, swL3VrrpOperHoldDownTimer=swL3VrrpOperHoldDownTimer, swL3RelayBootpCtrlTable=swL3RelayBootpCtrlTable, swL3RelayBootpMgmt=swL3RelayBootpMgmt, swL3IpCtrlVlanName=swL3IpCtrlVlanName, swL3RelayBootpCtrlInterfaceName=swL3RelayBootpCtrlInterfaceName, swL3IpCtrlIpAddr=swL3IpCtrlIpAddr, swL3Md5Key=swL3Md5Key, swL3VrrpOperCriticalIpAddr=swL3VrrpOperCriticalIpAddr, swL3VrrpOperVrId=swL3VrrpOperVrId, swL3IpStaticRouteEntry=swL3IpStaticRouteEntry, swL3RelayDnsStaticTableState=swL3RelayDnsStaticTableState, swL3RelayDnsCtrlTable=swL3RelayDnsCtrlTable, swL3IpFdbInfoIpSubnetMask=swL3IpFdbInfoIpSubnetMask, swL3IpArpPhysAddress=swL3IpArpPhysAddress, swL3DevCtrlOSPFState=swL3DevCtrlOSPFState, swL3IpArpReqRateLimitState=swL3IpArpReqRateLimitState, swL3IpFdbInfoPort=swL3IpFdbInfoPort, swL3IpFdbInfoIpAddr=swL3IpFdbInfoIpAddr, swL3DvmrpInterfaceNeighborTimeout=swL3DvmrpInterfaceNeighborTimeout, swL3Md5KeyId=swL3Md5KeyId, swL3OspfHostTOS=swL3OspfHostTOS, swL3DevCtrlDVMRPState=swL3DevCtrlDVMRPState, swL3RouteRedistriTable=swL3RouteRedistriTable, swL3RouteRedistriMetric=swL3RouteRedistriMetric, swL3IpArpIfIndex=swL3IpArpIfIndex, swL3DvmrpInterfaceProbe=swL3DvmrpInterfaceProbe, swL3DvmrpInterfaceTable=swL3DvmrpInterfaceTable)
