#
# PySNMP MIB module Wellfleet-BOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-BOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:32:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Unsigned32, Gauge32, Counter64, TimeTicks, Bits, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Unsigned32", "Gauge32", "Counter64", "TimeTicks", "Bits", "MibIdentifier", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfBotGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfBotGroup")
wfBot = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1))
wfBotDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotDelete.setStatus('mandatory')
wfBotDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotDisable.setStatus('mandatory')
wfBotState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotState.setStatus('mandatory')
wfBotInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2), )
if mibBuilder.loadTexts: wfBotInterfaceTable.setStatus('mandatory')
wfBotInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1), ).setIndexNames((0, "Wellfleet-BOT-MIB", "wfBotInterfaceSlotNumber"), (0, "Wellfleet-BOT-MIB", "wfBotInterfaceCctNumber"))
if mibBuilder.loadTexts: wfBotInterfaceEntry.setStatus('mandatory')
wfBotInterfaceDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceDelete.setStatus('mandatory')
wfBotInterfaceDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceDisable.setStatus('mandatory')
wfBotInterfaceCctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfaceCctNumber.setStatus('mandatory')
wfBotInterfaceSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfaceSlotNumber.setStatus('mandatory')
wfBotInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfaceState.setStatus('mandatory')
wfBotInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("singledrop", 1), ("multidrop", 2))).clone('singledrop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceType.setStatus('mandatory')
wfBotInterfaceAttachedTo = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceAttachedTo.setStatus('mandatory')
wfBotInterfacePktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfacePktCnt.setStatus('mandatory')
wfBotKeepaliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotKeepaliveInterval.setStatus('mandatory')
wfBotKeepaliveRto = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotKeepaliveRto.setStatus('mandatory')
wfBotKeepaliveMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotKeepaliveMaxRetry.setStatus('mandatory')
wfBotPeerTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3), )
if mibBuilder.loadTexts: wfBotPeerTable.setStatus('mandatory')
wfBotPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1), ).setIndexNames((0, "Wellfleet-BOT-MIB", "wfBotPeerSlotNumber"), (0, "Wellfleet-BOT-MIB", "wfBotPeerCctNumber"), (0, "Wellfleet-BOT-MIB", "wfBotPeerRemoteIpAddr"), (0, "Wellfleet-BOT-MIB", "wfBotPeerLocalTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotPeerRemoteTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotConnOriginator"))
if mibBuilder.loadTexts: wfBotPeerEntry.setStatus('mandatory')
wfBotPeerEntryDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotPeerEntryDelete.setStatus('mandatory')
wfBotPeerEntryDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotPeerEntryDisable.setStatus('mandatory')
wfBotPeerSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerSlotNumber.setStatus('mandatory')
wfBotPeerCctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerCctNumber.setStatus('mandatory')
wfBotPeerRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerRemoteIpAddr.setStatus('mandatory')
wfBotConnOriginator = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("self", 1), ("partner", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotConnOriginator.setStatus('mandatory')
wfBotPeerLocalTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerLocalTcpListenPort.setStatus('mandatory')
wfBotPeerRemoteTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerRemoteTcpListenPort.setStatus('mandatory')
wfBotPeerLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerLocalTcpPort.setStatus('mandatory')
wfBotPeerRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerRemoteTcpPort.setStatus('mandatory')
wfBotCUTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4), )
if mibBuilder.loadTexts: wfBotCUTable.setStatus('mandatory')
wfBotCUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1), ).setIndexNames((0, "Wellfleet-BOT-MIB", "wfBotCUSlotNumber"), (0, "Wellfleet-BOT-MIB", "wfBotCUCctNumber"), (0, "Wellfleet-BOT-MIB", "wfBotCURemoteIpAddr"), (0, "Wellfleet-BOT-MIB", "wfBotCULocalTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotCURemoteTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotCUAddrReachable"))
if mibBuilder.loadTexts: wfBotCUEntry.setStatus('mandatory')
wfBotCUEntryDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotCUEntryDelete.setStatus('mandatory')
wfBotCUEntryDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotCUEntryDisable.setStatus('mandatory')
wfBotCUSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCUSlotNumber.setStatus('mandatory')
wfBotCUCctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCUCctNumber.setStatus('mandatory')
wfBotCURemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCURemoteIpAddr.setStatus('mandatory')
wfBotCULocalTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCULocalTcpListenPort.setStatus('mandatory')
wfBotCURemoteTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCURemoteTcpListenPort.setStatus('mandatory')
wfBotCUAddrReachable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(254))).clone(namedValues=NamedValues(("address", 254)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCUAddrReachable.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-BOT-MIB", wfBotKeepaliveMaxRetry=wfBotKeepaliveMaxRetry, wfBotDelete=wfBotDelete, wfBotPeerEntry=wfBotPeerEntry, wfBotInterfaceState=wfBotInterfaceState, wfBotPeerTable=wfBotPeerTable, wfBotConnOriginator=wfBotConnOriginator, wfBotInterfaceAttachedTo=wfBotInterfaceAttachedTo, wfBotInterfaceCctNumber=wfBotInterfaceCctNumber, wfBotCULocalTcpListenPort=wfBotCULocalTcpListenPort, wfBotInterfaceDisable=wfBotInterfaceDisable, wfBotState=wfBotState, wfBotInterfaceEntry=wfBotInterfaceEntry, wfBotPeerSlotNumber=wfBotPeerSlotNumber, wfBotPeerCctNumber=wfBotPeerCctNumber, wfBotCUEntryDelete=wfBotCUEntryDelete, wfBotInterfaceSlotNumber=wfBotInterfaceSlotNumber, wfBotPeerRemoteIpAddr=wfBotPeerRemoteIpAddr, wfBotPeerEntryDelete=wfBotPeerEntryDelete, wfBotKeepaliveRto=wfBotKeepaliveRto, wfBotCUTable=wfBotCUTable, wfBotInterfaceType=wfBotInterfaceType, wfBotCUEntryDisable=wfBotCUEntryDisable, wfBotInterfacePktCnt=wfBotInterfacePktCnt, wfBot=wfBot, wfBotInterfaceDelete=wfBotInterfaceDelete, wfBotCUAddrReachable=wfBotCUAddrReachable, wfBotPeerRemoteTcpListenPort=wfBotPeerRemoteTcpListenPort, wfBotCURemoteIpAddr=wfBotCURemoteIpAddr, wfBotPeerLocalTcpPort=wfBotPeerLocalTcpPort, wfBotCUSlotNumber=wfBotCUSlotNumber, wfBotPeerRemoteTcpPort=wfBotPeerRemoteTcpPort, wfBotCURemoteTcpListenPort=wfBotCURemoteTcpListenPort, wfBotCUCctNumber=wfBotCUCctNumber, wfBotPeerEntryDisable=wfBotPeerEntryDisable, wfBotKeepaliveInterval=wfBotKeepaliveInterval, wfBotDisable=wfBotDisable, wfBotPeerLocalTcpListenPort=wfBotPeerLocalTcpListenPort, wfBotInterfaceTable=wfBotInterfaceTable, wfBotCUEntry=wfBotCUEntry)
