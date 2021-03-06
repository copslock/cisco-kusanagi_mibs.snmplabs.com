#
# PySNMP MIB module EXTREME-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ClientAuthType, extremeAgent = mibBuilder.importSymbols("EXTREME-BASE-MIB", "ClientAuthType", "extremeAgent")
extremeVlanIfIndex, = mibBuilder.importSymbols("EXTREME-VLAN-MIB", "extremeVlanIfIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Counter64, Counter32, NotificationType, Integer32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress", "TimeTicks")
RowStatus, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TextualConvention")
extremePort = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 4))
if mibBuilder.loadTexts: extremePort.setLastUpdated('0007240000Z')
if mibBuilder.loadTexts: extremePort.setOrganization('Extreme Networks, Inc.')
extremePortLoadshareTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 1), )
if mibBuilder.loadTexts: extremePortLoadshareTable.setStatus('deprecated')
extremePortLoadshareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1), ).setIndexNames((0, "EXTREME-PORT-MIB", "extremePortLoadshareMasterIfIndex"), (0, "EXTREME-PORT-MIB", "extremePortLoadshareSlaveIfIndex"))
if mibBuilder.loadTexts: extremePortLoadshareEntry.setStatus('deprecated')
extremePortLoadshareMasterIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortLoadshareMasterIfIndex.setStatus('deprecated')
extremePortLoadshareSlaveIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortLoadshareSlaveIfIndex.setStatus('deprecated')
extremePortLoadshareGrouping = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("other", 1), ("pair", 2), ("quad", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortLoadshareGrouping.setStatus('deprecated')
extremePortLoadshareStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortLoadshareStatus.setStatus('deprecated')
extremePortSummitlinkTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 2), )
if mibBuilder.loadTexts: extremePortSummitlinkTable.setStatus('deprecated')
extremePortSummitlinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremePortSummitlinkEntry.setStatus('deprecated')
extremePortSummitlinkAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernetOnly", 1), ("summitlinkOnly", 2))).clone('ethernetOnly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremePortSummitlinkAdminMode.setStatus('deprecated')
extremePortSummitlinkOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernetOnly", 1), ("summitlinkOnly", 2))).clone('ethernetOnly')).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortSummitlinkOperMode.setStatus('deprecated')
extremePortSummitlinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortSummitlinkState.setStatus('deprecated')
extremePortSummitlinkRejectReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("stackMisconnected", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortSummitlinkRejectReason.setStatus('deprecated')
extremePortLoadshare2Table = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 3), )
if mibBuilder.loadTexts: extremePortLoadshare2Table.setStatus('current')
extremePortLoadshare2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1), ).setIndexNames((0, "EXTREME-PORT-MIB", "extremePortLoadshare2MasterIfIndex"), (0, "EXTREME-PORT-MIB", "extremePortLoadshare2SlaveIfIndex"))
if mibBuilder.loadTexts: extremePortLoadshare2Entry.setStatus('current')
extremePortLoadshare2MasterIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: extremePortLoadshare2MasterIfIndex.setStatus('current')
extremePortLoadshare2SlaveIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: extremePortLoadshare2SlaveIfIndex.setStatus('current')
extremePortLoadshare2Algorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingressPortOffset", 1), ("hash", 2), ("roundRobin", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortLoadshare2Algorithm.setStatus('current')
extremePortLoadshare2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortLoadshare2Status.setStatus('current')
extremePortRateShapeTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 4), )
if mibBuilder.loadTexts: extremePortRateShapeTable.setStatus('current')
extremePortRateShapeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"))
if mibBuilder.loadTexts: extremePortRateShapeEntry.setStatus('current')
extremePortRateShapePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rateLimited", 1), ("loopBack", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortRateShapePortType.setStatus('current')
extremePortRateShapeLoopbackTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortRateShapeLoopbackTag.setStatus('current')
extremePortRateShapeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremePortRateShapeStatus.setStatus('current')
extremePortUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 5), )
if mibBuilder.loadTexts: extremePortUtilizationTable.setStatus('current')
extremePortUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremePortUtilizationEntry.setStatus('current')
extremePortUtilizationAvgTxBw = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortUtilizationAvgTxBw.setStatus('current')
extremePortUtilizationAvgRxBw = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortUtilizationAvgRxBw.setStatus('current')
extremePortUtilizationPeakTxBw = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortUtilizationPeakTxBw.setStatus('current')
extremePortUtilizationPeakRxBw = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortUtilizationPeakRxBw.setStatus('current')
extremePortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 6), )
if mibBuilder.loadTexts: extremePortInfoTable.setStatus('current')
extremePortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremePortInfoEntry.setStatus('current')
extremePortInfoFilterUpCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremePortInfoFilterUpCounter.setStatus('current')
extremePortInfoFilterDownCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremePortInfoFilterDownCounter.setStatus('current')
extremePortXenpakVendorTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 7), )
if mibBuilder.loadTexts: extremePortXenpakVendorTable.setStatus('current')
extremePortXenpakVendorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremePortXenpakVendorEntry.setStatus('current')
extremePortXenpakVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 7, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortXenpakVendorName.setStatus('current')
extremePortIngressStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8))
extremePortIngressStatsPortTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1), )
if mibBuilder.loadTexts: extremePortIngressStatsPortTable.setStatus('current')
extremePortIngressPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremePortIngressPortStatsEntry.setStatus('current')
extremePortIngressStatsLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ready", 1), ("active", 2), ("disabled", 3), ("notPresent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsLinkStatus.setStatus('current')
extremePortIngressStatsPortHighPriBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsPortHighPriBytes.setStatus('current')
extremePortIngressStatsPortLowPriBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsPortLowPriBytes.setStatus('current')
extremePortIngressStatsPortDroppedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsPortDroppedBytes.setStatus('current')
extremePortIngressStatsTxXoff = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsTxXoff.setStatus('current')
extremePortIngressStatsQueueTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2), )
if mibBuilder.loadTexts: extremePortIngressStatsQueueTable.setStatus('current')
extremePortIngressQueueStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "EXTREME-PORT-MIB", "extremePortIngressStatsQueueIndex"))
if mibBuilder.loadTexts: extremePortIngressQueueStatsEntry.setStatus('current')
extremePortIngressStatsQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsQueueIndex.setStatus('current')
extremePortIngressStatsQueueHighPriBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsQueueHighPriBytes.setStatus('current')
extremePortIngressStatsQueueLowPriBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsQueueLowPriBytes.setStatus('current')
extremePortIngressStatsQueuePercentDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortIngressStatsQueuePercentDropped.setStatus('current')
extremePortEgressRateLimitTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 9), )
if mibBuilder.loadTexts: extremePortEgressRateLimitTable.setStatus('current')
extremePortEgressRateLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremePortEgressRateLimitEntry.setStatus('current')
extremePortEgressRateLimitType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("percentage", 1), ("kbps", 2), ("mbps", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortEgressRateLimitType.setStatus('current')
extremePortEgressRateLimitValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremePortEgressRateLimitValue.setStatus('current')
extremeWiredClientTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10), )
if mibBuilder.loadTexts: extremeWiredClientTable.setStatus('current')
extremeWiredClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "EXTREME-PORT-MIB", "extremeWiredClientID"))
if mibBuilder.loadTexts: extremeWiredClientEntry.setStatus('current')
extremeWiredClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeWiredClientID.setStatus('current')
extremeWiredClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authenticated", 1), ("unauthenticated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeWiredClientState.setStatus('current')
extremeWiredClientVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeWiredClientVLAN.setStatus('current')
extremeWiredClientPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeWiredClientPriority.setStatus('current')
extremeWiredClientAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 5), ClientAuthType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeWiredClientAuthType.setStatus('current')
extremeWiredClientLastStateChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeWiredClientLastStateChangeTime.setStatus('current')
extremeWiredClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeWiredClientIP.setStatus('current')
mibBuilder.exportSymbols("EXTREME-PORT-MIB", extremePortInfoFilterDownCounter=extremePortInfoFilterDownCounter, extremePortIngressStatsQueueLowPriBytes=extremePortIngressStatsQueueLowPriBytes, extremePortIngressStatsPortDroppedBytes=extremePortIngressStatsPortDroppedBytes, extremePortUtilizationPeakRxBw=extremePortUtilizationPeakRxBw, extremePortSummitlinkOperMode=extremePortSummitlinkOperMode, extremePortXenpakVendorEntry=extremePortXenpakVendorEntry, extremePortLoadshareTable=extremePortLoadshareTable, extremePortSummitlinkEntry=extremePortSummitlinkEntry, extremePortRateShapeTable=extremePortRateShapeTable, extremePortUtilizationAvgTxBw=extremePortUtilizationAvgTxBw, extremePortIngressStatsPortTable=extremePortIngressStatsPortTable, extremePortInfoFilterUpCounter=extremePortInfoFilterUpCounter, extremePortIngressStatsQueueIndex=extremePortIngressStatsQueueIndex, extremePortInfoTable=extremePortInfoTable, extremePortUtilizationPeakTxBw=extremePortUtilizationPeakTxBw, extremePortLoadshare2SlaveIfIndex=extremePortLoadshare2SlaveIfIndex, extremePortEgressRateLimitType=extremePortEgressRateLimitType, extremeWiredClientState=extremeWiredClientState, extremePortIngressStats=extremePortIngressStats, extremePortIngressStatsPortHighPriBytes=extremePortIngressStatsPortHighPriBytes, extremePortSummitlinkTable=extremePortSummitlinkTable, extremePortIngressStatsQueueTable=extremePortIngressStatsQueueTable, extremePortEgressRateLimitEntry=extremePortEgressRateLimitEntry, extremePortRateShapeEntry=extremePortRateShapeEntry, extremePortXenpakVendorName=extremePortXenpakVendorName, extremePortLoadshare2Status=extremePortLoadshare2Status, extremePortRateShapePortType=extremePortRateShapePortType, extremePortRateShapeStatus=extremePortRateShapeStatus, extremeWiredClientAuthType=extremeWiredClientAuthType, extremeWiredClientVLAN=extremeWiredClientVLAN, extremePortLoadshareMasterIfIndex=extremePortLoadshareMasterIfIndex, extremePortIngressStatsTxXoff=extremePortIngressStatsTxXoff, extremePortLoadshare2Entry=extremePortLoadshare2Entry, extremeWiredClientTable=extremeWiredClientTable, extremePortIngressStatsQueuePercentDropped=extremePortIngressStatsQueuePercentDropped, PYSNMP_MODULE_ID=extremePort, extremePortUtilizationAvgRxBw=extremePortUtilizationAvgRxBw, extremeWiredClientLastStateChangeTime=extremeWiredClientLastStateChangeTime, extremePortLoadshare2Algorithm=extremePortLoadshare2Algorithm, extremePortIngressQueueStatsEntry=extremePortIngressQueueStatsEntry, extremePortSummitlinkRejectReason=extremePortSummitlinkRejectReason, extremeWiredClientPriority=extremeWiredClientPriority, extremePortSummitlinkAdminMode=extremePortSummitlinkAdminMode, extremePort=extremePort, extremePortLoadshare2Table=extremePortLoadshare2Table, extremePortUtilizationEntry=extremePortUtilizationEntry, extremeWiredClientEntry=extremeWiredClientEntry, extremePortLoadshare2MasterIfIndex=extremePortLoadshare2MasterIfIndex, extremeWiredClientID=extremeWiredClientID, extremePortIngressStatsQueueHighPriBytes=extremePortIngressStatsQueueHighPriBytes, extremeWiredClientIP=extremeWiredClientIP, extremePortLoadshareGrouping=extremePortLoadshareGrouping, extremePortInfoEntry=extremePortInfoEntry, extremePortLoadshareSlaveIfIndex=extremePortLoadshareSlaveIfIndex, extremePortEgressRateLimitTable=extremePortEgressRateLimitTable, extremePortIngressPortStatsEntry=extremePortIngressPortStatsEntry, extremePortLoadshareStatus=extremePortLoadshareStatus, extremePortRateShapeLoopbackTag=extremePortRateShapeLoopbackTag, extremePortIngressStatsLinkStatus=extremePortIngressStatsLinkStatus, extremePortIngressStatsPortLowPriBytes=extremePortIngressStatsPortLowPriBytes, extremePortSummitlinkState=extremePortSummitlinkState, extremePortXenpakVendorTable=extremePortXenpakVendorTable, extremePortLoadshareEntry=extremePortLoadshareEntry, extremePortEgressRateLimitValue=extremePortEgressRateLimitValue, extremePortUtilizationTable=extremePortUtilizationTable)
