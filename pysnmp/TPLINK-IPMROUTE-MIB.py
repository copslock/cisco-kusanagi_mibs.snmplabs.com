#
# PySNMP MIB module TPLINK-IPMROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-IPMROUTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, ModuleIdentity, MibIdentifier, iso, Counter32, Gauge32, Bits, Unsigned32, NotificationType, TimeTicks, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "Gauge32", "Bits", "Unsigned32", "NotificationType", "TimeTicks", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkIpMrouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 78))
tplinkIpMrouteMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkIpMrouteMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkIpMrouteMIB.setOrganization('TPLINK')
tplinkIpMrouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1))
tplinkIpMrouteNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 78, 2))
tpIpMRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1))
tpIpMRouteEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIpMRouteEnable.setStatus('current')
tpIpMRouteSGTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2), )
if mibBuilder.loadTexts: tpIpMRouteSGTable.setStatus('current')
tpIpMRouteSGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1), ).setIndexNames((0, "TPLINK-IPMROUTE-MIB", "tpIpMRouteSGGroup"), (0, "TPLINK-IPMROUTE-MIB", "tpIpMRouteSGSource"))
if mibBuilder.loadTexts: tpIpMRouteSGEntry.setStatus('current')
tpIpMRouteSGGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGGroup.setStatus('current')
tpIpMRouteSGSource = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGSource.setStatus('current')
tpIpMRouteSGIncomingInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGIncomingInterface.setStatus('current')
tpIpMRouteSGOutgoingInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGOutgoingInterface.setStatus('current')
tpIpMRouteSGRpfNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGRpfNeighbor.setStatus('current')
tpIpMRouteSGUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGUpTime.setStatus('current')
tpIpMRouteSGExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGExpiryTime.setStatus('current')
tpIpMRouteSGProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pimDenseMode", 1), ("pimSparseMode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGProtocol.setStatus('current')
tpIpMRouteSGFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("spt", 1), ("rpt", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteSGFlags.setStatus('current')
tpIpMRouteStarGTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3), )
if mibBuilder.loadTexts: tpIpMRouteStarGTable.setStatus('current')
tpIpMRouteStarGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1), ).setIndexNames((0, "TPLINK-IPMROUTE-MIB", "tpIpMRouteStarGGroup"))
if mibBuilder.loadTexts: tpIpMRouteStarGEntry.setStatus('current')
tpIpMRouteStarGGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGGroup.setStatus('current')
tpIpMRouteStarGSource = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGSource.setStatus('current')
tpIpMRouteStarGIncomingInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGIncomingInterface.setStatus('current')
tpIpMRouteStarGOutgoingInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGOutgoingInterface.setStatus('current')
tpIpMRouteStarGRpfNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGRpfNeighbor.setStatus('current')
tpIpMRouteStarGUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGUpTime.setStatus('current')
tpIpMRouteStarGExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGExpiryTime.setStatus('current')
tpIpMRouteStarGProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pimDenseMode", 1), ("pimSparseMode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGProtocol.setStatus('current')
tpIpMRouteStarGFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("spt", 1), ("rpt", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpMRouteStarGFlags.setStatus('current')
mibBuilder.exportSymbols("TPLINK-IPMROUTE-MIB", tpIpMRouteStarGOutgoingInterface=tpIpMRouteStarGOutgoingInterface, tpIpMRouteStarGGroup=tpIpMRouteStarGGroup, tpIpMRoute=tpIpMRoute, tpIpMRouteStarGTable=tpIpMRouteStarGTable, tpIpMRouteStarGEntry=tpIpMRouteStarGEntry, tpIpMRouteStarGExpiryTime=tpIpMRouteStarGExpiryTime, tpIpMRouteStarGIncomingInterface=tpIpMRouteStarGIncomingInterface, tpIpMRouteSGFlags=tpIpMRouteSGFlags, tplinkIpMrouteMIBObjects=tplinkIpMrouteMIBObjects, tplinkIpMrouteMIB=tplinkIpMrouteMIB, tpIpMRouteSGSource=tpIpMRouteSGSource, tpIpMRouteStarGFlags=tpIpMRouteStarGFlags, PYSNMP_MODULE_ID=tplinkIpMrouteMIB, tpIpMRouteSGUpTime=tpIpMRouteSGUpTime, tpIpMRouteStarGUpTime=tpIpMRouteStarGUpTime, tpIpMRouteStarGRpfNeighbor=tpIpMRouteStarGRpfNeighbor, tpIpMRouteSGOutgoingInterface=tpIpMRouteSGOutgoingInterface, tpIpMRouteSGTable=tpIpMRouteSGTable, tpIpMRouteSGEntry=tpIpMRouteSGEntry, tplinkIpMrouteNotifications=tplinkIpMrouteNotifications, tpIpMRouteStarGProtocol=tpIpMRouteStarGProtocol, tpIpMRouteSGGroup=tpIpMRouteSGGroup, tpIpMRouteEnable=tpIpMRouteEnable, tpIpMRouteSGIncomingInterface=tpIpMRouteSGIncomingInterface, tpIpMRouteSGRpfNeighbor=tpIpMRouteSGRpfNeighbor, tpIpMRouteSGProtocol=tpIpMRouteSGProtocol, tpIpMRouteStarGSource=tpIpMRouteStarGSource, tpIpMRouteSGExpiryTime=tpIpMRouteSGExpiryTime)