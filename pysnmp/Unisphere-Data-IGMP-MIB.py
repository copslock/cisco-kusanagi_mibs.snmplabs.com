#
# PySNMP MIB module Unisphere-Data-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IGMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Counter32, MibIdentifier, ObjectIdentity, IpAddress, Unsigned32, NotificationType, Integer32, Gauge32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Counter32", "MibIdentifier", "ObjectIdentity", "IpAddress", "Unsigned32", "NotificationType", "Integer32", "Gauge32", "TimeTicks", "iso")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
usdIgmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40))
usdIgmpMIB.setRevisions(('2000-09-26 18:50',))
if mibBuilder.loadTexts: usdIgmpMIB.setLastUpdated('200009261850Z')
if mibBuilder.loadTexts: usdIgmpMIB.setOrganization('Unisphere Networks, Inc.')
class UsdIgmpProxyGroupState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("usdIgmpProxyGroupUnknown", 0), ("usdIgmpProxyGroupIdleMember", 1), ("usdIgmpProxyGroupDelayingMember", 2))

class UsdIgmpProxyInterfaceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("usdIgmpProxyInterfaceUnknown", 0), ("usdIgmpProxyInterfaceStateV1RouterPresent", 1), ("usdIgmpProxyInterfaceStateNonV1RouterPresent", 2))

usdIgmpMIBObject = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1))
usdIgmpProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1))
usdIgmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2))
usdIgmpProxyInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1), )
if mibBuilder.loadTexts: usdIgmpProxyInterfaceTable.setStatus('current')
usdIgmpProxyInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1), ).setIndexNames((0, "Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceIfIndex"))
if mibBuilder.loadTexts: usdIgmpProxyInterfaceEntry.setStatus('current')
usdIgmpProxyInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdIgmpProxyInterfaceIfIndex.setStatus('current')
usdIgmpProxyInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceAddress.setStatus('current')
usdIgmpProxyInterfaceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceMask.setStatus('current')
usdIgmpProxyInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 4), UsdIgmpProxyInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceState.setStatus('current')
usdIgmpProxyInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceStatus.setStatus('current')
usdIgmpProxyInterfaceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceVersion.setStatus('current')
usdIgmpProxyInterfaceV1RoutePresentTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(400)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceV1RoutePresentTimeout.setStatus('current')
usdIgmpProxyInterfaceUnsolicitedReportInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceUnsolicitedReportInterval.setStatus('current')
usdIgmpProxyInterfaceTotalGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceTotalGroupCount.setStatus('current')
usdIgmpProxyInterfaceWrongVersionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceWrongVersionCount.setStatus('current')
usdIgmpProxyInterfaceV1QueryReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceV1QueryReceiveCount.setStatus('current')
usdIgmpProxyInterfaceV2QueryReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceV2QueryReceiveCount.setStatus('current')
usdIgmpProxyInterfaceV1ReportReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceV1ReportReceiveCount.setStatus('current')
usdIgmpProxyInterfaceV2ReportReceiveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceV2ReportReceiveCount.setStatus('current')
usdIgmpProxyInterfaceV1JoinReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceV1JoinReportCount.setStatus('current')
usdIgmpProxyInterfaceV2JoinReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceV2JoinReportCount.setStatus('current')
usdIgmpProxyInterfaceLeaveReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyInterfaceLeaveReportCount.setStatus('current')
usdIgmpProxyCacheTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2), )
if mibBuilder.loadTexts: usdIgmpProxyCacheTable.setStatus('current')
usdIgmpProxyCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1), ).setIndexNames((0, "Unisphere-Data-IGMP-MIB", "usdIgmpProxyIfIndex"), (0, "Unisphere-Data-IGMP-MIB", "usdIgmpProxyAddress"))
if mibBuilder.loadTexts: usdIgmpProxyCacheEntry.setStatus('current')
usdIgmpProxyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdIgmpProxyIfIndex.setStatus('current')
usdIgmpProxyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: usdIgmpProxyAddress.setStatus('current')
usdIgmpProxyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 3), UsdIgmpProxyGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIgmpProxyStatus.setStatus('current')
usdIgmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4))
usdIgmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1))
usdIgmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2))
usdIgmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 1)).setObjects(("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceGroup"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyCacheGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIgmpCompliance = usdIgmpCompliance.setStatus('current')
usdIgmpProxyInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 1)).setObjects(("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceAddress"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceMask"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceState"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceStatus"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceVersion"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1RoutePresentTimeout"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceUnsolicitedReportInterval"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceTotalGroupCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceWrongVersionCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1QueryReceiveCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV2QueryReceiveCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1ReportReceiveCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV2ReportReceiveCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV1JoinReportCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceV2JoinReportCount"), ("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceLeaveReportCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIgmpProxyInterfaceGroup = usdIgmpProxyInterfaceGroup.setStatus('current')
usdIgmpProxyCacheGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 2)).setObjects(("Unisphere-Data-IGMP-MIB", "usdIgmpProxyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIgmpProxyCacheGroup = usdIgmpProxyCacheGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IGMP-MIB", usdIgmpProxyStatus=usdIgmpProxyStatus, usdIgmpGroups=usdIgmpGroups, usdIgmpProxyInterfaceV1QueryReceiveCount=usdIgmpProxyInterfaceV1QueryReceiveCount, usdIgmpProxyInterfaceWrongVersionCount=usdIgmpProxyInterfaceWrongVersionCount, usdIgmpProxyInterfaceMask=usdIgmpProxyInterfaceMask, usdIgmpProxy=usdIgmpProxy, usdIgmpCompliances=usdIgmpCompliances, usdIgmpProxyInterfaceIfIndex=usdIgmpProxyInterfaceIfIndex, usdIgmpProxyInterfaceV1RoutePresentTimeout=usdIgmpProxyInterfaceV1RoutePresentTimeout, usdIgmpMIB=usdIgmpMIB, PYSNMP_MODULE_ID=usdIgmpMIB, usdIgmpProxyInterfaceV1JoinReportCount=usdIgmpProxyInterfaceV1JoinReportCount, usdIgmpProxyInterfaceV2QueryReceiveCount=usdIgmpProxyInterfaceV2QueryReceiveCount, usdIgmpProxyInterfaceTotalGroupCount=usdIgmpProxyInterfaceTotalGroupCount, usdIgmpProxyCacheEntry=usdIgmpProxyCacheEntry, usdIgmpProxyInterfaceTable=usdIgmpProxyInterfaceTable, usdIgmpProxyIfIndex=usdIgmpProxyIfIndex, usdIgmpProxyAddress=usdIgmpProxyAddress, UsdIgmpProxyGroupState=UsdIgmpProxyGroupState, usdIgmpProxyInterfaceAddress=usdIgmpProxyInterfaceAddress, usdIgmpProxyCacheTable=usdIgmpProxyCacheTable, UsdIgmpProxyInterfaceState=UsdIgmpProxyInterfaceState, usdIgmpProxyInterfaceV1ReportReceiveCount=usdIgmpProxyInterfaceV1ReportReceiveCount, usdIgmpProxyInterfaceLeaveReportCount=usdIgmpProxyInterfaceLeaveReportCount, usdIgmpProxyInterfaceState=usdIgmpProxyInterfaceState, usdIgmpProxyInterfaceV2JoinReportCount=usdIgmpProxyInterfaceV2JoinReportCount, usdIgmpProxyInterfaceV2ReportReceiveCount=usdIgmpProxyInterfaceV2ReportReceiveCount, usdIgmpProxyInterfaceStatus=usdIgmpProxyInterfaceStatus, usdIgmpProxyInterfaceEntry=usdIgmpProxyInterfaceEntry, usdIgmpConformance=usdIgmpConformance, usdIgmpProtocol=usdIgmpProtocol, usdIgmpProxyInterfaceVersion=usdIgmpProxyInterfaceVersion, usdIgmpMIBObject=usdIgmpMIBObject, usdIgmpProxyCacheGroup=usdIgmpProxyCacheGroup, usdIgmpProxyInterfaceGroup=usdIgmpProxyInterfaceGroup, usdIgmpProxyInterfaceUnsolicitedReportInterval=usdIgmpProxyInterfaceUnsolicitedReportInterval, usdIgmpCompliance=usdIgmpCompliance)
