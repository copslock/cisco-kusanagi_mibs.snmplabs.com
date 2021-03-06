#
# PySNMP MIB module HH3C-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-IPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ModuleIdentity, Integer32, ObjectIdentity, NotificationType, MibIdentifier, Counter64, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ModuleIdentity", "Integer32", "ObjectIdentity", "NotificationType", "MibIdentifier", "Counter64", "Gauge32", "Counter32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hh3cIpx = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 34))
if mibBuilder.loadTexts: hh3cIpx.setLastUpdated('200412241036Z')
if mibBuilder.loadTexts: hh3cIpx.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hh3cIpxConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1))
hh3cIpxRip = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2))
hh3cIpxSap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3))
hh3cIpxStat = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4))
hh3cIpxStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxStatus.setStatus('current')
hh3cIpxIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2), )
if mibBuilder.loadTexts: hh3cIpxIfConfigTable.setStatus('current')
hh3cIpxIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1), ).setIndexNames((0, "HH3C-IPX-MIB", "hh3cIpxIfIndex"))
if mibBuilder.loadTexts: hh3cIpxIfConfigEntry.setStatus('current')
hh3cIpxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cIpxIfIndex.setStatus('current')
hh3cIpxIfNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfNetId.setStatus('current')
hh3cIpxIfNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfNodeId.setStatus('current')
hh3cIpxIfSplitHorizon = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 4), EnabledStatus().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfSplitHorizon.setStatus('current')
hh3cIPxIfTick = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIPxIfTick.setStatus('current')
hh3cIpxIfUpdateChangeOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 6), EnabledStatus().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfUpdateChangeOnly.setStatus('current')
hh3cIpxIfRipMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(432, 1500)).clone(432)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfRipMtu.setStatus('current')
hh3cIpxIfEncapsuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("dot2", 1), ("dot3", 2), ("ethernet-2", 3), ("snap", 4), ("unkown", 5))).clone('dot3')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfEncapsuleType.setStatus('current')
hh3cIpxIfNetbiosPropagation = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 9), EnabledStatus().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfNetbiosPropagation.setStatus('current')
hh3cIpxIfSapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 10), EnabledStatus().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfSapStatus.setStatus('current')
hh3cIpxIfSapMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(480, 1500)).clone(480)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfSapMtu.setStatus('current')
hh3cIpxIfGnsReply = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 12), EnabledStatus().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfGnsReply.setStatus('current')
hh3cIpxIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxIfRowStatus.setStatus('current')
hh3cIpxRouteMultiplier = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxRouteMultiplier.setStatus('current')
hh3cIpxRouteUpdateTimer = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60000)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxRouteUpdateTimer.setStatus('current')
hh3cIpxRouteImpRouteStatic = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxRouteImpRouteStatic.setStatus('current')
hh3cIpxRouteLoadBalancePaths = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxRouteLoadBalancePaths.setStatus('current')
hh3cIpxRouteMaxResPaths = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxRouteMaxResPaths.setStatus('current')
hh3cIpxRouteTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6), )
if mibBuilder.loadTexts: hh3cIpxRouteTable.setStatus('current')
hh3cIpxRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1), ).setIndexNames((0, "HH3C-IPX-MIB", "hh3cIpxRouteIndex"))
if mibBuilder.loadTexts: hh3cIpxRouteEntry.setStatus('current')
hh3cIpxRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cIpxRouteIndex.setStatus('current')
hh3cIpxRouteDestNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteDestNetId.setStatus('current')
hh3cIpxRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteNextHop.setStatus('current')
hh3cIpxRoutePro = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("direct", 1), ("rip", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRoutePro.setStatus('current')
hh3cIpxRoutePre = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRoutePre.setStatus('current')
hh3cIpxRouteTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteTicks.setStatus('current')
hh3cIpxRouteHops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteHops.setStatus('current')
hh3cIpxRouteTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteTime.setStatus('current')
hh3cIpxRouteOutInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteOutInterface.setStatus('current')
hh3cIpxStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7), )
if mibBuilder.loadTexts: hh3cIpxStaticRouteTable.setStatus('current')
hh3cIpxStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1), ).setIndexNames((0, "HH3C-IPX-MIB", "hh3cIpxStaticRouteDestNetId"), (0, "HH3C-IPX-MIB", "hh3cIpxStaticRouteNextHop"))
if mibBuilder.loadTexts: hh3cIpxStaticRouteEntry.setStatus('current')
hh3cIpxStaticRouteDestNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4))
if mibBuilder.loadTexts: hh3cIpxStaticRouteDestNetId.setStatus('current')
hh3cIpxStaticRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10))
if mibBuilder.loadTexts: hh3cIpxStaticRouteNextHop.setStatus('current')
hh3cIpxStaticRoutePre = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticRoutePre.setStatus('current')
hh3cIpxStaticRouteOutIf = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticRouteOutIf.setStatus('current')
hh3cIpxStaticRouteTicks = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticRouteTicks.setStatus('current')
hh3cIpxStaticRouteHops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticRouteHops.setStatus('current')
hh3cIpxStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticRouteStatus.setStatus('current')
hh3cIpxStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticRouteRowStatus.setStatus('current')
hh3cIpxRouteStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8), )
if mibBuilder.loadTexts: hh3cIpxRouteStatTable.setStatus('current')
hh3cIpxRouteStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1), ).setIndexNames((0, "HH3C-IPX-MIB", "hh3cIpxRouteStatPro"))
if mibBuilder.loadTexts: hh3cIpxRouteStatEntry.setStatus('current')
hh3cIpxRouteStatPro = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("direct", 1), ("static", 2), ("rip", 3), ("default", 4), ("total", 5))))
if mibBuilder.loadTexts: hh3cIpxRouteStatPro.setStatus('current')
hh3cIpxRouteStatRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteStatRoutes.setStatus('current')
hh3cIpxRouteStatActives = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteStatActives.setStatus('current')
hh3cIpxRouteStatAddeds = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteStatAddeds.setStatus('current')
hh3cIpxRouteStatDeleteds = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteStatDeleteds.setStatus('current')
hh3cIpxRouteStatFreeds = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxRouteStatFreeds.setStatus('current')
hh3cIpxSapMultiplier = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxSapMultiplier.setStatus('current')
hh3cIpxSapUpdateTimer = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60000)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxSapUpdateTimer.setStatus('current')
hh3cIpxSapGnsLoadBalance = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 3), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxSapGnsLoadBalance.setStatus('current')
hh3cIpxSapMaxResServers = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)).clone(2048)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpxSapMaxResServers.setStatus('current')
hh3cIpxServiceTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5), )
if mibBuilder.loadTexts: hh3cIpxServiceTable.setStatus('current')
hh3cIpxServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1), ).setIndexNames((0, "HH3C-IPX-MIB", "hh3cIpxServiceIndex"))
if mibBuilder.loadTexts: hh3cIpxServiceEntry.setStatus('current')
hh3cIpxServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cIpxServiceIndex.setStatus('current')
hh3cIpxServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServiceName.setStatus('current')
hh3cIpxServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServiceType.setStatus('current')
hh3cIpxServiceNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServiceNetId.setStatus('current')
hh3cIpxServiceNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServiceNodeId.setStatus('current')
hh3cIpxServiceSocketNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServiceSocketNo.setStatus('current')
hh3cIpxServicePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServicePreference.setStatus('current')
hh3cIpxServiceHops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServiceHops.setStatus('current')
hh3cIpxServiceRecvIf = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxServiceRecvIf.setStatus('current')
hh3cIpxStaticServiceTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6), )
if mibBuilder.loadTexts: hh3cIpxStaticServiceTable.setStatus('current')
hh3cIpxStaticServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1), ).setIndexNames((0, "HH3C-IPX-MIB", "hh3cIpxStaticServiceType"), (0, "HH3C-IPX-MIB", "hh3cIpxStaticServiceName"), (0, "HH3C-IPX-MIB", "hh3cIpxStaticServiceNetId"))
if mibBuilder.loadTexts: hh3cIpxStaticServiceEntry.setStatus('current')
hh3cIpxStaticServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2))
if mibBuilder.loadTexts: hh3cIpxStaticServiceType.setStatus('current')
hh3cIpxStaticServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 47)))
if mibBuilder.loadTexts: hh3cIpxStaticServiceName.setStatus('current')
hh3cIpxStaticServiceNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4))
if mibBuilder.loadTexts: hh3cIpxStaticServiceNetId.setStatus('current')
hh3cIpxStaticServiceNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticServiceNodeId.setStatus('current')
hh3cIpxStatciServiceSocketNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStatciServiceSocketNo.setStatus('current')
hh3cIpxStaticServicePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticServicePreference.setStatus('current')
hh3cIpxStaticServiceHops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticServiceHops.setStatus('current')
hh3cIpxStaticServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticServiceStatus.setStatus('current')
hh3cIpxStaticServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpxStaticServiceRowStatus.setStatus('current')
hh3cIpxStatGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1))
hh3cIpxStatInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2))
hh3cIpxStatTotalReceives = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatTotalReceives.setStatus('current')
hh3cIpxStatPitchs = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatPitchs.setStatus('current')
hh3cIpxStatLenErrors = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatLenErrors.setStatus('current')
hh3cIpxStatFormatErrors = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatFormatErrors.setStatus('current')
hh3cIpxStatBadHops = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatBadHops.setStatus('current')
hh3cIpxStatHopsDiscards = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatHopsDiscards.setStatus('current')
hh3cIpxStatOtherErrors = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatOtherErrors.setStatus('current')
hh3cIpxStatLocalDests = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatLocalDests.setStatus('current')
hh3cIpxStatCantDeals = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatCantDeals.setStatus('current')
hh3cIpxStatForwards = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatForwards.setStatus('current')
hh3cIpxStatGenerates = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatGenerates.setStatus('current')
hh3cIpxStatNoRoutes = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatNoRoutes.setStatus('current')
hh3cIpxStatOutDiscards = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatOutDiscards.setStatus('current')
hh3cIpxStatRipSends = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatRipSends.setStatus('current')
hh3cIpxStatRipReceives = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatRipReceives.setStatus('current')
hh3cIpxStaRipRspSends = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStaRipRspSends.setStatus('current')
hh3cIpxStaRipRspReceives = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStaRipRspReceives.setStatus('current')
hh3cIpxStatRipReqReceives = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatRipReqReceives.setStatus('current')
hh3cIpxStatRipReqDeals = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatRipReqDeals.setStatus('current')
hh3cIpxStatRipReqSends = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatRipReqSends.setStatus('current')
hh3cIpxStatRipPeriUpdates = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatRipPeriUpdates.setStatus('current')
hh3cIpxStatSapGenReqReceives = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapGenReqReceives.setStatus('current')
hh3cIpxStatSapSpecReqReceives = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapSpecReqReceives.setStatus('current')
hh3cIpxStatSapGnsReqReceives = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapGnsReqReceives.setStatus('current')
hh3cIpxStatSapGenRspSends = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapGenRspSends.setStatus('current')
hh3cIpxStatSapSpecRspSends = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapSpecRspSends.setStatus('current')
hh3cIpxStatSapGnsRspSends = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapGnsRspSends.setStatus('current')
hh3cIpxStatSapPeriUpdates = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapPeriUpdates.setStatus('current')
hh3cIpxStatSapInPktErrors = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxStatSapInPktErrors.setStatus('current')
hh3cIpxIfStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1), )
if mibBuilder.loadTexts: hh3cIpxIfStatTable.setStatus('current')
hh3cIpxIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1), ).setIndexNames((0, "HH3C-IPX-MIB", "hh3cIpxIfStatIndex"))
if mibBuilder.loadTexts: hh3cIpxIfStatEntry.setStatus('current')
hh3cIpxIfStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cIpxIfStatIndex.setStatus('current')
hh3cIpxIfStatNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatNetId.setStatus('current')
hh3cIpxIfStatNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatNodeId.setStatus('current')
hh3cIpxIfStatIpxReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatIpxReceives.setStatus('current')
hh3cIpxIfStatIpxSends = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatIpxSends.setStatus('current')
hh3cIpxIfStatIpxRecvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatIpxRecvBytes.setStatus('current')
hh3cIpxIfStatIpxSendBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatIpxSendBytes.setStatus('current')
hh3cIpxIfStatRipReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatRipReceives.setStatus('current')
hh3cIpxIfStatRipSends = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatRipSends.setStatus('current')
hh3cIpxIfStatRipDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatRipDiscards.setStatus('current')
hh3cIpxIfStatRipSpecReqReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatRipSpecReqReceives.setStatus('current')
hh3cIpxIfStatRipSpecRspSends = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatRipSpecRspSends.setStatus('current')
hh3cIpxIfStatRipGenReqReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatRipGenReqReceives.setStatus('current')
hh3cIpxIfStatRipGenRspSends = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatRipGenRspSends.setStatus('current')
hh3cIpxIfStatSapReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatSapReceives.setStatus('current')
hh3cIpxIfStatSapSends = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatSapSends.setStatus('current')
hh3cIpxIfStatSapDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatSapDiscards.setStatus('current')
hh3cIpxIfStatSapGnsReqReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatSapGnsReqReceives.setStatus('current')
hh3cIpxIfStatSapGnsRspSends = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpxIfStatSapGnsRspSends.setStatus('current')
mibBuilder.exportSymbols("HH3C-IPX-MIB", hh3cIpxStaticRouteHops=hh3cIpxStaticRouteHops, hh3cIpxStaticServiceRowStatus=hh3cIpxStaticServiceRowStatus, hh3cIpxStatus=hh3cIpxStatus, hh3cIpxRouteIndex=hh3cIpxRouteIndex, hh3cIpxServicePreference=hh3cIpxServicePreference, hh3cIpxServiceRecvIf=hh3cIpxServiceRecvIf, hh3cIpxServiceSocketNo=hh3cIpxServiceSocketNo, hh3cIpxStatInterface=hh3cIpxStatInterface, hh3cIpxStat=hh3cIpxStat, hh3cIpxSapUpdateTimer=hh3cIpxSapUpdateTimer, hh3cIpxIfStatIpxSendBytes=hh3cIpxIfStatIpxSendBytes, hh3cIpxIfSapStatus=hh3cIpxIfSapStatus, hh3cIpxRoutePro=hh3cIpxRoutePro, hh3cIpxStatGlobal=hh3cIpxStatGlobal, hh3cIpxStatRipReqReceives=hh3cIpxStatRipReqReceives, hh3cIpxStaticServiceType=hh3cIpxStaticServiceType, hh3cIpxStaRipRspSends=hh3cIpxStaRipRspSends, hh3cIpxIfStatRipSends=hh3cIpxIfStatRipSends, PYSNMP_MODULE_ID=hh3cIpx, hh3cIpxServiceHops=hh3cIpxServiceHops, hh3cIpxStatSapGenReqReceives=hh3cIpxStatSapGenReqReceives, hh3cIpxRouteTicks=hh3cIpxRouteTicks, hh3cIpxIfStatRipSpecReqReceives=hh3cIpxIfStatRipSpecReqReceives, hh3cIpxRouteUpdateTimer=hh3cIpxRouteUpdateTimer, hh3cIpxRouteOutInterface=hh3cIpxRouteOutInterface, hh3cIPxIfTick=hh3cIPxIfTick, hh3cIpxStaticServiceNetId=hh3cIpxStaticServiceNetId, hh3cIpxStatciServiceSocketNo=hh3cIpxStatciServiceSocketNo, hh3cIpxSap=hh3cIpxSap, hh3cIpxIfStatNodeId=hh3cIpxIfStatNodeId, hh3cIpxRouteStatAddeds=hh3cIpxRouteStatAddeds, hh3cIpxIfRowStatus=hh3cIpxIfRowStatus, hh3cIpxIfStatSapReceives=hh3cIpxIfStatSapReceives, hh3cIpxServiceNetId=hh3cIpxServiceNetId, hh3cIpxRouteStatTable=hh3cIpxRouteStatTable, hh3cIpxRouteMultiplier=hh3cIpxRouteMultiplier, hh3cIpxRouteStatRoutes=hh3cIpxRouteStatRoutes, hh3cIpxRip=hh3cIpxRip, hh3cIpxStaticRouteTable=hh3cIpxStaticRouteTable, hh3cIpxStatSapPeriUpdates=hh3cIpxStatSapPeriUpdates, hh3cIpxRouteStatEntry=hh3cIpxRouteStatEntry, hh3cIpxServiceTable=hh3cIpxServiceTable, hh3cIpxStatRipReqSends=hh3cIpxStatRipReqSends, hh3cIpxIfRipMtu=hh3cIpxIfRipMtu, hh3cIpxRouteDestNetId=hh3cIpxRouteDestNetId, hh3cIpxIfStatTable=hh3cIpxIfStatTable, hh3cIpx=hh3cIpx, hh3cIpxStatSapGnsReqReceives=hh3cIpxStatSapGnsReqReceives, hh3cIpxStatBadHops=hh3cIpxStatBadHops, hh3cIpxStaticServiceEntry=hh3cIpxStaticServiceEntry, hh3cIpxStatLenErrors=hh3cIpxStatLenErrors, hh3cIpxRouteStatPro=hh3cIpxRouteStatPro, hh3cIpxIfIndex=hh3cIpxIfIndex, hh3cIpxIfStatIpxRecvBytes=hh3cIpxIfStatIpxRecvBytes, hh3cIpxStaRipRspReceives=hh3cIpxStaRipRspReceives, hh3cIpxSapMaxResServers=hh3cIpxSapMaxResServers, hh3cIpxStaticServiceName=hh3cIpxStaticServiceName, hh3cIpxIfStatRipGenReqReceives=hh3cIpxIfStatRipGenReqReceives, hh3cIpxStatLocalDests=hh3cIpxStatLocalDests, hh3cIpxRouteMaxResPaths=hh3cIpxRouteMaxResPaths, hh3cIpxServiceEntry=hh3cIpxServiceEntry, hh3cIpxIfStatSapDiscards=hh3cIpxIfStatSapDiscards, hh3cIpxRouteStatActives=hh3cIpxRouteStatActives, hh3cIpxSapMultiplier=hh3cIpxSapMultiplier, hh3cIpxStaticRouteRowStatus=hh3cIpxStaticRouteRowStatus, hh3cIpxStaticRouteNextHop=hh3cIpxStaticRouteNextHop, hh3cIpxStatRipPeriUpdates=hh3cIpxStatRipPeriUpdates, hh3cIpxIfStatEntry=hh3cIpxIfStatEntry, hh3cIpxRouteTable=hh3cIpxRouteTable, hh3cIpxStaticRouteDestNetId=hh3cIpxStaticRouteDestNetId, hh3cIpxStatCantDeals=hh3cIpxStatCantDeals, hh3cIpxIfUpdateChangeOnly=hh3cIpxIfUpdateChangeOnly, hh3cIpxRouteNextHop=hh3cIpxRouteNextHop, hh3cIpxStatPitchs=hh3cIpxStatPitchs, hh3cIpxStatSapGnsRspSends=hh3cIpxStatSapGnsRspSends, hh3cIpxIfStatNetId=hh3cIpxIfStatNetId, hh3cIpxRouteLoadBalancePaths=hh3cIpxRouteLoadBalancePaths, hh3cIpxStatGenerates=hh3cIpxStatGenerates, hh3cIpxRouteEntry=hh3cIpxRouteEntry, hh3cIpxIfStatSapSends=hh3cIpxIfStatSapSends, hh3cIpxStatForwards=hh3cIpxStatForwards, hh3cIpxIfEncapsuleType=hh3cIpxIfEncapsuleType, hh3cIpxRouteTime=hh3cIpxRouteTime, hh3cIpxStaticRouteOutIf=hh3cIpxStaticRouteOutIf, hh3cIpxIfConfigEntry=hh3cIpxIfConfigEntry, hh3cIpxStatSapInPktErrors=hh3cIpxStatSapInPktErrors, hh3cIpxStatTotalReceives=hh3cIpxStatTotalReceives, hh3cIpxServiceName=hh3cIpxServiceName, hh3cIpxStatRipReqDeals=hh3cIpxStatRipReqDeals, hh3cIpxStaticRoutePre=hh3cIpxStaticRoutePre, hh3cIpxSapGnsLoadBalance=hh3cIpxSapGnsLoadBalance, hh3cIpxIfNodeId=hh3cIpxIfNodeId, hh3cIpxStatOtherErrors=hh3cIpxStatOtherErrors, hh3cIpxStatSapSpecRspSends=hh3cIpxStatSapSpecRspSends, hh3cIpxStatFormatErrors=hh3cIpxStatFormatErrors, hh3cIpxIfConfigTable=hh3cIpxIfConfigTable, EnabledStatus=EnabledStatus, hh3cIpxStaticServiceNodeId=hh3cIpxStaticServiceNodeId, hh3cIpxRoutePre=hh3cIpxRoutePre, hh3cIpxStatRipReceives=hh3cIpxStatRipReceives, hh3cIpxServiceNodeId=hh3cIpxServiceNodeId, hh3cIpxStatOutDiscards=hh3cIpxStatOutDiscards, hh3cIpxStaticServiceHops=hh3cIpxStaticServiceHops, hh3cIpxIfStatRipDiscards=hh3cIpxIfStatRipDiscards, hh3cIpxIfNetId=hh3cIpxIfNetId, hh3cIpxRouteImpRouteStatic=hh3cIpxRouteImpRouteStatic, hh3cIpxRouteHops=hh3cIpxRouteHops, hh3cIpxStaticServiceTable=hh3cIpxStaticServiceTable, hh3cIpxIfStatIndex=hh3cIpxIfStatIndex, hh3cIpxStatRipSends=hh3cIpxStatRipSends, hh3cIpxIfSapMtu=hh3cIpxIfSapMtu, hh3cIpxIfStatRipGenRspSends=hh3cIpxIfStatRipGenRspSends, hh3cIpxRouteStatDeleteds=hh3cIpxRouteStatDeleteds, hh3cIpxServiceIndex=hh3cIpxServiceIndex, hh3cIpxStatSapSpecReqReceives=hh3cIpxStatSapSpecReqReceives, hh3cIpxStaticServiceStatus=hh3cIpxStaticServiceStatus, hh3cIpxStatNoRoutes=hh3cIpxStatNoRoutes, hh3cIpxIfStatRipSpecRspSends=hh3cIpxIfStatRipSpecRspSends, hh3cIpxIfStatIpxSends=hh3cIpxIfStatIpxSends, hh3cIpxServiceType=hh3cIpxServiceType, hh3cIpxIfNetbiosPropagation=hh3cIpxIfNetbiosPropagation, hh3cIpxIfGnsReply=hh3cIpxIfGnsReply, hh3cIpxStaticRouteTicks=hh3cIpxStaticRouteTicks, hh3cIpxStatSapGenRspSends=hh3cIpxStatSapGenRspSends, hh3cIpxIfStatSapGnsRspSends=hh3cIpxIfStatSapGnsRspSends, hh3cIpxStatHopsDiscards=hh3cIpxStatHopsDiscards, hh3cIpxStaticRouteEntry=hh3cIpxStaticRouteEntry, hh3cIpxStaticRouteStatus=hh3cIpxStaticRouteStatus, hh3cIpxConfig=hh3cIpxConfig, hh3cIpxIfStatRipReceives=hh3cIpxIfStatRipReceives, hh3cIpxIfSplitHorizon=hh3cIpxIfSplitHorizon, hh3cIpxIfStatSapGnsReqReceives=hh3cIpxIfStatSapGnsReqReceives, hh3cIpxStaticServicePreference=hh3cIpxStaticServicePreference, hh3cIpxIfStatIpxReceives=hh3cIpxIfStatIpxReceives, hh3cIpxRouteStatFreeds=hh3cIpxRouteStatFreeds)
