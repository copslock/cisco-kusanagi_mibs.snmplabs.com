#
# PySNMP MIB module Wellfleet-MPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-MPLS-LDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:34:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, Integer32, MibIdentifier, ObjectIdentity, iso, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Integer32", "MibIdentifier", "ObjectIdentity", "iso", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfMplsLdpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfMplsLdpGroup")
wfMplsLdpSessCfgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1), )
if mibBuilder.loadTexts: wfMplsLdpSessCfgTable.setStatus('mandatory')
wfMplsLdpSessCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgSlot"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgCircuit"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgIndex"))
if mibBuilder.loadTexts: wfMplsLdpSessCfgEntry.setStatus('mandatory')
wfMplsLdpSessCfgCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgCreate.setStatus('mandatory')
wfMplsLdpSessCfgEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgEnable.setStatus('mandatory')
wfMplsLdpSessCfgSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessCfgSlot.setStatus('mandatory')
wfMplsLdpSessCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessCfgIndex.setStatus('mandatory')
wfMplsLdpSessCfgCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessCfgCircuit.setStatus('mandatory')
wfMplsLdpSessCfgLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgLocalIpAddress.setStatus('mandatory')
wfMplsLdpSessCfgLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(8192)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgLocalTcpPort.setStatus('mandatory')
wfMplsLdpSessCfgRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgRemoteIpAddress.setStatus('mandatory')
wfMplsLdpSessCfgRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(8192)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgRemoteTcpPort.setStatus('mandatory')
wfMplsLdpSessCfgRoutesConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgRoutesConfigMode.setStatus('mandatory')
wfMplsLdpSessCfgHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgHoldTime.setStatus('mandatory')
wfMplsLdpSessCfgProto = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ospf", 1), ("rip", 2), ("hybridospf", 3), ("hybridrip", 4))).clone('ospf')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgProto.setStatus('mandatory')
wfMplsLdpSessCfgAggregation = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgAggregation.setStatus('mandatory')
wfMplsLdpSessCfgDebugLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("three", 3), ("debug", 4))).clone('two')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgDebugLevel.setStatus('mandatory')
wfMplsLdpSessCfgReqBindRetryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgReqBindRetryTime.setStatus('mandatory')
wfMplsLdpSessCfgReqBindRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)).clone(240)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgReqBindRetries.setStatus('mandatory')
wfMplsLdpSessActualTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2), )
if mibBuilder.loadTexts: wfMplsLdpSessActualTable.setStatus('mandatory')
wfMplsLdpSessActualEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessActualCircuit"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessActualIndex"))
if mibBuilder.loadTexts: wfMplsLdpSessActualEntry.setStatus('mandatory')
wfMplsLdpSessActualIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualIndex.setStatus('mandatory')
wfMplsLdpSessActualCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualCircuit.setStatus('mandatory')
wfMplsLdpSessActualState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualState.setStatus('mandatory')
wfMplsLdpSessActualPeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initialized", 1), ("opensend", 2), ("openrec", 3), ("operational", 4))).clone('initialized')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualPeerState.setStatus('mandatory')
wfMplsLdpSessActualLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualLocalIpAddress.setStatus('mandatory')
wfMplsLdpSessActualLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualLocalTcpPort.setStatus('mandatory')
wfMplsLdpSessActualRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualRemoteIpAddress.setStatus('mandatory')
wfMplsLdpSessActualRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualRemoteTcpPort.setStatus('mandatory')
wfMplsLdpSessActualHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualHoldTime.setStatus('mandatory')
wfMplsLdpSessActualRoutesConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualRoutesConfigMode.setStatus('mandatory')
wfMplsLdpSessActualTCPConnectionRole = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("passive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualTCPConnectionRole.setStatus('mandatory')
wfMplsLdpSessActualSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualSlot.setStatus('mandatory')
wfMplsLdpCfgRouteTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3), )
if mibBuilder.loadTexts: wfMplsLdpCfgRouteTable.setStatus('mandatory')
wfMplsLdpCfgRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteCct"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteSessId"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteIndex"))
if mibBuilder.loadTexts: wfMplsLdpCfgRouteEntry.setStatus('mandatory')
wfMplsLdpCfgRouteCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteCreate.setStatus('mandatory')
wfMplsLdpCfgRouteEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteEnable.setStatus('mandatory')
wfMplsLdpCfgRouteCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteCct.setStatus('mandatory')
wfMplsLdpCfgRouteSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteSessId.setStatus('mandatory')
wfMplsLdpCfgRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteIndex.setStatus('mandatory')
wfMplsLdpCfgRouteDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteDestination.setStatus('mandatory')
wfMplsLdpCfgRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteMask.setStatus('mandatory')
wfMplsLdpCfgRouteState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteState.setStatus('mandatory')
wfMplsLdpLibTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4), )
if mibBuilder.loadTexts: wfMplsLdpLibTable.setStatus('mandatory')
wfMplsLdpLibEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibCct"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibSessId"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibDest"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibMid"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibIndex"))
if mibBuilder.loadTexts: wfMplsLdpLibEntry.setStatus('mandatory')
wfMplsLdpLibCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibCct.setStatus('mandatory')
wfMplsLdpLibSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibSessId.setStatus('mandatory')
wfMplsLdpLibDest = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibDest.setStatus('mandatory')
wfMplsLdpLibMid = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibMid.setStatus('mandatory')
wfMplsLdpLibLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibLabel.setStatus('mandatory')
wfMplsLdpLibEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llcsnap", 1), ("null", 2))).clone('llcsnap')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibEncaps.setStatus('mandatory')
wfMplsLdpLibDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("bidirectional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibDirection.setStatus('mandatory')
wfMplsLdpLibSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibSlot.setStatus('mandatory')
wfMplsLdpLibIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibIndex.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-MPLS-LDP-MIB", wfMplsLdpSessCfgRemoteIpAddress=wfMplsLdpSessCfgRemoteIpAddress, wfMplsLdpSessActualTable=wfMplsLdpSessActualTable, wfMplsLdpSessActualPeerState=wfMplsLdpSessActualPeerState, wfMplsLdpLibCct=wfMplsLdpLibCct, wfMplsLdpSessCfgProto=wfMplsLdpSessCfgProto, wfMplsLdpSessCfgHoldTime=wfMplsLdpSessCfgHoldTime, wfMplsLdpLibDest=wfMplsLdpLibDest, wfMplsLdpLibSlot=wfMplsLdpLibSlot, wfMplsLdpSessCfgReqBindRetryTime=wfMplsLdpSessCfgReqBindRetryTime, wfMplsLdpSessCfgEntry=wfMplsLdpSessCfgEntry, wfMplsLdpSessCfgLocalTcpPort=wfMplsLdpSessCfgLocalTcpPort, wfMplsLdpLibEncaps=wfMplsLdpLibEncaps, wfMplsLdpSessActualRemoteTcpPort=wfMplsLdpSessActualRemoteTcpPort, wfMplsLdpSessActualRoutesConfigMode=wfMplsLdpSessActualRoutesConfigMode, wfMplsLdpSessActualLocalTcpPort=wfMplsLdpSessActualLocalTcpPort, wfMplsLdpCfgRouteIndex=wfMplsLdpCfgRouteIndex, wfMplsLdpLibIndex=wfMplsLdpLibIndex, wfMplsLdpSessCfgRoutesConfigMode=wfMplsLdpSessCfgRoutesConfigMode, wfMplsLdpSessCfgEnable=wfMplsLdpSessCfgEnable, wfMplsLdpSessCfgRemoteTcpPort=wfMplsLdpSessCfgRemoteTcpPort, wfMplsLdpSessCfgDebugLevel=wfMplsLdpSessCfgDebugLevel, wfMplsLdpSessActualLocalIpAddress=wfMplsLdpSessActualLocalIpAddress, wfMplsLdpCfgRouteCct=wfMplsLdpCfgRouteCct, wfMplsLdpCfgRouteEnable=wfMplsLdpCfgRouteEnable, wfMplsLdpLibMid=wfMplsLdpLibMid, wfMplsLdpLibEntry=wfMplsLdpLibEntry, wfMplsLdpSessCfgTable=wfMplsLdpSessCfgTable, wfMplsLdpSessCfgAggregation=wfMplsLdpSessCfgAggregation, wfMplsLdpSessActualRemoteIpAddress=wfMplsLdpSessActualRemoteIpAddress, wfMplsLdpSessActualEntry=wfMplsLdpSessActualEntry, wfMplsLdpSessCfgCreate=wfMplsLdpSessCfgCreate, wfMplsLdpCfgRouteEntry=wfMplsLdpCfgRouteEntry, wfMplsLdpSessActualCircuit=wfMplsLdpSessActualCircuit, wfMplsLdpSessCfgCircuit=wfMplsLdpSessCfgCircuit, wfMplsLdpSessCfgIndex=wfMplsLdpSessCfgIndex, wfMplsLdpLibTable=wfMplsLdpLibTable, wfMplsLdpCfgRouteState=wfMplsLdpCfgRouteState, wfMplsLdpSessActualState=wfMplsLdpSessActualState, wfMplsLdpCfgRouteCreate=wfMplsLdpCfgRouteCreate, wfMplsLdpLibSessId=wfMplsLdpLibSessId, wfMplsLdpSessActualHoldTime=wfMplsLdpSessActualHoldTime, wfMplsLdpSessCfgSlot=wfMplsLdpSessCfgSlot, wfMplsLdpCfgRouteDestination=wfMplsLdpCfgRouteDestination, wfMplsLdpCfgRouteMask=wfMplsLdpCfgRouteMask, wfMplsLdpSessActualSlot=wfMplsLdpSessActualSlot, wfMplsLdpCfgRouteTable=wfMplsLdpCfgRouteTable, wfMplsLdpSessActualIndex=wfMplsLdpSessActualIndex, wfMplsLdpLibLabel=wfMplsLdpLibLabel, wfMplsLdpSessActualTCPConnectionRole=wfMplsLdpSessActualTCPConnectionRole, wfMplsLdpLibDirection=wfMplsLdpLibDirection, wfMplsLdpSessCfgReqBindRetries=wfMplsLdpSessCfgReqBindRetries, wfMplsLdpSessCfgLocalIpAddress=wfMplsLdpSessCfgLocalIpAddress, wfMplsLdpCfgRouteSessId=wfMplsLdpCfgRouteSessId)