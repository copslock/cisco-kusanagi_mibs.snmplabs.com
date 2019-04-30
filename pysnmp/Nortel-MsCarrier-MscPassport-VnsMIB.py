#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-VnsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-VnsMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
mscRtgIndex, mscRtg = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex", "mscRtg")
RowPointer, StorageType, RowStatus, Unsigned32, InterfaceIndex, DisplayString, Integer32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "RowPointer", "StorageType", "RowStatus", "Unsigned32", "InterfaceIndex", "DisplayString", "Integer32")
Link, PassportCounter64, AsciiStringIndex = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link", "PassportCounter64", "AsciiStringIndex")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, NotificationType, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, IpAddress, MibIdentifier, Integer32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "NotificationType", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vnsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20))
mscRtgVns = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3))
mscRtgVnsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1), )
if mibBuilder.loadTexts: mscRtgVnsRowStatusTable.setStatus('mandatory')
mscRtgVnsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"))
if mibBuilder.loadTexts: mscRtgVnsRowStatusEntry.setStatus('mandatory')
mscRtgVnsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsRowStatus.setStatus('mandatory')
mscRtgVnsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsComponentName.setStatus('mandatory')
mscRtgVnsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsStorageType.setStatus('mandatory')
mscRtgVnsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 12)))
if mibBuilder.loadTexts: mscRtgVnsIndex.setStatus('mandatory')
mscRtgVnsProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10), )
if mibBuilder.loadTexts: mscRtgVnsProvTable.setStatus('mandatory')
mscRtgVnsProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"))
if mibBuilder.loadTexts: mscRtgVnsProvEntry.setStatus('mandatory')
mscRtgVnsLogicalNetworkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 2047))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsLogicalNetworkNumber.setStatus('mandatory')
mscRtgVnsLinkToProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 2), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsLinkToProtocolPort.setStatus('mandatory')
mscRtgVnsMaximumTransmissionUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2048, 65535)).clone(2048)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsMaximumTransmissionUnit.setStatus('mandatory')
mscRtgVnsLoadSharing = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsLoadSharing.setStatus('mandatory')
mscRtgVnsDiscardPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsDiscardPriority.setStatus('obsolete')
mscRtgVnsIlsForwarder = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 10, 1, 6), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsIlsForwarder.setStatus('mandatory')
mscRtgVnsIfEntryTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11), )
if mibBuilder.loadTexts: mscRtgVnsIfEntryTable.setStatus('mandatory')
mscRtgVnsIfEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"))
if mibBuilder.loadTexts: mscRtgVnsIfEntryEntry.setStatus('mandatory')
mscRtgVnsIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsIfAdminStatus.setStatus('mandatory')
mscRtgVnsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 11, 1, 2), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsIfIndex.setStatus('mandatory')
mscRtgVnsCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 12), )
if mibBuilder.loadTexts: mscRtgVnsCidDataTable.setStatus('mandatory')
mscRtgVnsCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"))
if mibBuilder.loadTexts: mscRtgVnsCidDataEntry.setStatus('mandatory')
mscRtgVnsCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscRtgVnsCustomerIdentifier.setStatus('mandatory')
mscRtgVnsStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14), )
if mibBuilder.loadTexts: mscRtgVnsStateTable.setStatus('mandatory')
mscRtgVnsStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"))
if mibBuilder.loadTexts: mscRtgVnsStateEntry.setStatus('mandatory')
mscRtgVnsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsAdminState.setStatus('mandatory')
mscRtgVnsOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsOperationalState.setStatus('mandatory')
mscRtgVnsUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsUsageState.setStatus('mandatory')
mscRtgVnsOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 15), )
if mibBuilder.loadTexts: mscRtgVnsOperTable.setStatus('mandatory')
mscRtgVnsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"))
if mibBuilder.loadTexts: mscRtgVnsOperEntry.setStatus('mandatory')
mscRtgVnsReportedThroughputMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsReportedThroughputMetric.setStatus('mandatory')
mscRtgVnsFwdStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16), )
if mibBuilder.loadTexts: mscRtgVnsFwdStatsTable.setStatus('mandatory')
mscRtgVnsFwdStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"))
if mibBuilder.loadTexts: mscRtgVnsFwdStatsEntry.setStatus('mandatory')
mscRtgVnsUniRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 1), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsUniRxPkts.setStatus('mandatory')
mscRtgVnsUniRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 2), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsUniRxBytes.setStatus('mandatory')
mscRtgVnsUniRxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 3), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsUniRxDiscPkts.setStatus('mandatory')
mscRtgVnsUniTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 4), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsUniTxPkts.setStatus('mandatory')
mscRtgVnsUniTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 5), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsUniTxBytes.setStatus('mandatory')
mscRtgVnsUniTxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 6), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsUniTxDiscPkts.setStatus('mandatory')
mscRtgVnsMultiRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 7), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsMultiRxPkts.setStatus('mandatory')
mscRtgVnsMultiRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 8), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsMultiRxBytes.setStatus('mandatory')
mscRtgVnsMultiRxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 9), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsMultiRxDiscPkts.setStatus('mandatory')
mscRtgVnsMultiTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 10), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsMultiTxPkts.setStatus('mandatory')
mscRtgVnsMultiTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 11), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsMultiTxBytes.setStatus('mandatory')
mscRtgVnsMultiTxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 12), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsMultiTxDiscPkts.setStatus('mandatory')
mscRtgVnsTotalRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 13), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsTotalRxPkts.setStatus('mandatory')
mscRtgVnsTotalRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 14), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsTotalRxBytes.setStatus('mandatory')
mscRtgVnsTotalRxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 15), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsTotalRxDiscPkts.setStatus('mandatory')
mscRtgVnsTotalTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 16), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsTotalTxPkts.setStatus('mandatory')
mscRtgVnsTotalTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 17), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsTotalTxBytes.setStatus('mandatory')
mscRtgVnsTotalTxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 16, 1, 18), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsTotalTxDiscPkts.setStatus('mandatory')
mscRtgVnsNode = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2))
mscRtgVnsNodeRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1), )
if mibBuilder.loadTexts: mscRtgVnsNodeRowStatusTable.setStatus('mandatory')
mscRtgVnsNodeRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsNodeIndex"))
if mibBuilder.loadTexts: mscRtgVnsNodeRowStatusEntry.setStatus('mandatory')
mscRtgVnsNodeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsNodeRowStatus.setStatus('mandatory')
mscRtgVnsNodeComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsNodeComponentName.setStatus('mandatory')
mscRtgVnsNodeStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsNodeStorageType.setStatus('mandatory')
mscRtgVnsNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: mscRtgVnsNodeIndex.setStatus('mandatory')
mscRtgVnsNodeOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10), )
if mibBuilder.loadTexts: mscRtgVnsNodeOperTable.setStatus('mandatory')
mscRtgVnsNodeOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsNodeIndex"))
if mibBuilder.loadTexts: mscRtgVnsNodeOperEntry.setStatus('mandatory')
mscRtgVnsNodeMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsNodeMetric.setStatus('mandatory')
mscRtgVnsNodeNextHopLinkGroup1 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsNodeNextHopLinkGroup1.setStatus('mandatory')
mscRtgVnsNodeNextHopLinkGroup2 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 2, 10, 1, 3), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsNodeNextHopLinkGroup2.setStatus('mandatory')
mscRtgVnsLpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3))
mscRtgVnsLpStatsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1), )
if mibBuilder.loadTexts: mscRtgVnsLpStatsRowStatusTable.setStatus('mandatory')
mscRtgVnsLpStatsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsLpStatsIndex"))
if mibBuilder.loadTexts: mscRtgVnsLpStatsRowStatusEntry.setStatus('mandatory')
mscRtgVnsLpStatsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsRowStatus.setStatus('mandatory')
mscRtgVnsLpStatsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsComponentName.setStatus('mandatory')
mscRtgVnsLpStatsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsStorageType.setStatus('mandatory')
mscRtgVnsLpStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: mscRtgVnsLpStatsIndex.setStatus('mandatory')
mscRtgVnsLpStatsFwdStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2), )
if mibBuilder.loadTexts: mscRtgVnsLpStatsFwdStatsTable.setStatus('mandatory')
mscRtgVnsLpStatsFwdStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-BaseRoutingMIB", "mscRtgIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsIndex"), (0, "Nortel-MsCarrier-MscPassport-VnsMIB", "mscRtgVnsLpStatsIndex"))
if mibBuilder.loadTexts: mscRtgVnsLpStatsFwdStatsEntry.setStatus('mandatory')
mscRtgVnsLpStatsUniRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 1), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsUniRxPkts.setStatus('mandatory')
mscRtgVnsLpStatsUniRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 2), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsUniRxBytes.setStatus('mandatory')
mscRtgVnsLpStatsUniRxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 3), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsUniRxDiscPkts.setStatus('mandatory')
mscRtgVnsLpStatsUniTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 4), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsUniTxPkts.setStatus('mandatory')
mscRtgVnsLpStatsUniTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 5), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsUniTxBytes.setStatus('mandatory')
mscRtgVnsLpStatsUniTxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 6), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsUniTxDiscPkts.setStatus('mandatory')
mscRtgVnsLpStatsMultiRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 7), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsMultiRxPkts.setStatus('mandatory')
mscRtgVnsLpStatsMultiRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 8), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsMultiRxBytes.setStatus('mandatory')
mscRtgVnsLpStatsMultiRxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 9), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsMultiRxDiscPkts.setStatus('mandatory')
mscRtgVnsLpStatsMultiTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 10), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsMultiTxPkts.setStatus('mandatory')
mscRtgVnsLpStatsMultiTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 11), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsMultiTxBytes.setStatus('mandatory')
mscRtgVnsLpStatsMultiTxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 12), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsMultiTxDiscPkts.setStatus('mandatory')
mscRtgVnsLpStatsTotalRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 13), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsTotalRxPkts.setStatus('mandatory')
mscRtgVnsLpStatsTotalRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 14), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsTotalRxBytes.setStatus('mandatory')
mscRtgVnsLpStatsTotalRxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 15), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsTotalRxDiscPkts.setStatus('mandatory')
mscRtgVnsLpStatsTotalTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 16), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsTotalTxPkts.setStatus('mandatory')
mscRtgVnsLpStatsTotalTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 17), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsTotalTxBytes.setStatus('mandatory')
mscRtgVnsLpStatsTotalTxDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 40, 3, 3, 2, 1, 18), PassportCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscRtgVnsLpStatsTotalTxDiscPkts.setStatus('mandatory')
vnsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1))
vnsGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1, 1))
vnsGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1, 1, 3))
vnsGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 1, 1, 3, 2))
vnsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3))
vnsCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3, 1))
vnsCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3, 1, 3))
vnsCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 20, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-VnsMIB", mscRtgVnsLpStatsUniRxDiscPkts=mscRtgVnsLpStatsUniRxDiscPkts, mscRtgVnsLpStatsUniRxPkts=mscRtgVnsLpStatsUniRxPkts, mscRtgVnsLpStatsTotalTxPkts=mscRtgVnsLpStatsTotalTxPkts, mscRtgVnsNodeNextHopLinkGroup2=mscRtgVnsNodeNextHopLinkGroup2, mscRtgVnsUniRxPkts=mscRtgVnsUniRxPkts, mscRtgVnsCidDataEntry=mscRtgVnsCidDataEntry, vnsGroupCA=vnsGroupCA, mscRtgVnsNodeRowStatus=mscRtgVnsNodeRowStatus, mscRtgVnsTotalTxDiscPkts=mscRtgVnsTotalTxDiscPkts, mscRtgVnsMultiTxPkts=mscRtgVnsMultiTxPkts, mscRtgVnsTotalRxPkts=mscRtgVnsTotalRxPkts, mscRtgVnsLpStatsMultiRxDiscPkts=mscRtgVnsLpStatsMultiRxDiscPkts, mscRtgVnsStateTable=mscRtgVnsStateTable, mscRtgVnsLpStatsRowStatus=mscRtgVnsLpStatsRowStatus, mscRtgVnsLpStatsTotalRxDiscPkts=mscRtgVnsLpStatsTotalRxDiscPkts, vnsGroupCA02A=vnsGroupCA02A, mscRtgVnsIlsForwarder=mscRtgVnsIlsForwarder, mscRtgVnsIndex=mscRtgVnsIndex, mscRtgVnsProvTable=mscRtgVnsProvTable, vnsCapabilities=vnsCapabilities, mscRtgVns=mscRtgVns, mscRtgVnsDiscardPriority=mscRtgVnsDiscardPriority, mscRtgVnsRowStatusTable=mscRtgVnsRowStatusTable, mscRtgVnsUniTxBytes=mscRtgVnsUniTxBytes, mscRtgVnsMultiRxPkts=mscRtgVnsMultiRxPkts, mscRtgVnsNodeOperEntry=mscRtgVnsNodeOperEntry, mscRtgVnsMultiTxBytes=mscRtgVnsMultiTxBytes, mscRtgVnsUsageState=mscRtgVnsUsageState, mscRtgVnsCustomerIdentifier=mscRtgVnsCustomerIdentifier, vnsGroup=vnsGroup, mscRtgVnsLpStatsTotalRxPkts=mscRtgVnsLpStatsTotalRxPkts, mscRtgVnsCidDataTable=mscRtgVnsCidDataTable, mscRtgVnsLpStatsFwdStatsTable=mscRtgVnsLpStatsFwdStatsTable, mscRtgVnsIfEntryEntry=mscRtgVnsIfEntryEntry, mscRtgVnsFwdStatsTable=mscRtgVnsFwdStatsTable, mscRtgVnsUniRxBytes=mscRtgVnsUniRxBytes, mscRtgVnsStateEntry=mscRtgVnsStateEntry, mscRtgVnsRowStatusEntry=mscRtgVnsRowStatusEntry, mscRtgVnsNodeIndex=mscRtgVnsNodeIndex, mscRtgVnsFwdStatsEntry=mscRtgVnsFwdStatsEntry, mscRtgVnsLpStatsMultiRxPkts=mscRtgVnsLpStatsMultiRxPkts, mscRtgVnsLpStatsMultiTxPkts=mscRtgVnsLpStatsMultiTxPkts, mscRtgVnsLpStatsTotalTxBytes=mscRtgVnsLpStatsTotalTxBytes, mscRtgVnsMultiTxDiscPkts=mscRtgVnsMultiTxDiscPkts, mscRtgVnsLpStatsMultiTxBytes=mscRtgVnsLpStatsMultiTxBytes, mscRtgVnsRowStatus=mscRtgVnsRowStatus, vnsCapabilitiesCA02A=vnsCapabilitiesCA02A, mscRtgVnsLpStatsTotalTxDiscPkts=mscRtgVnsLpStatsTotalTxDiscPkts, mscRtgVnsTotalTxPkts=mscRtgVnsTotalTxPkts, mscRtgVnsNodeRowStatusEntry=mscRtgVnsNodeRowStatusEntry, mscRtgVnsStorageType=mscRtgVnsStorageType, mscRtgVnsLpStatsTotalRxBytes=mscRtgVnsLpStatsTotalRxBytes, mscRtgVnsLogicalNetworkNumber=mscRtgVnsLogicalNetworkNumber, mscRtgVnsOperationalState=mscRtgVnsOperationalState, mscRtgVnsOperEntry=mscRtgVnsOperEntry, mscRtgVnsNodeOperTable=mscRtgVnsNodeOperTable, mscRtgVnsTotalRxBytes=mscRtgVnsTotalRxBytes, mscRtgVnsLpStatsRowStatusTable=mscRtgVnsLpStatsRowStatusTable, mscRtgVnsTotalRxDiscPkts=mscRtgVnsTotalRxDiscPkts, vnsGroupCA02=vnsGroupCA02, mscRtgVnsLpStatsMultiRxBytes=mscRtgVnsLpStatsMultiRxBytes, mscRtgVnsLpStatsMultiTxDiscPkts=mscRtgVnsLpStatsMultiTxDiscPkts, vnsCapabilitiesCA02=vnsCapabilitiesCA02, mscRtgVnsNode=mscRtgVnsNode, mscRtgVnsLpStatsIndex=mscRtgVnsLpStatsIndex, mscRtgVnsUniRxDiscPkts=mscRtgVnsUniRxDiscPkts, mscRtgVnsIfEntryTable=mscRtgVnsIfEntryTable, mscRtgVnsLpStatsUniTxPkts=mscRtgVnsLpStatsUniTxPkts, mscRtgVnsMultiRxBytes=mscRtgVnsMultiRxBytes, mscRtgVnsProvEntry=mscRtgVnsProvEntry, mscRtgVnsLpStatsUniTxBytes=mscRtgVnsLpStatsUniTxBytes, mscRtgVnsNodeComponentName=mscRtgVnsNodeComponentName, mscRtgVnsLpStatsComponentName=mscRtgVnsLpStatsComponentName, mscRtgVnsLpStatsUniTxDiscPkts=mscRtgVnsLpStatsUniTxDiscPkts, mscRtgVnsReportedThroughputMetric=mscRtgVnsReportedThroughputMetric, mscRtgVnsLoadSharing=mscRtgVnsLoadSharing, mscRtgVnsLpStats=mscRtgVnsLpStats, vnsCapabilitiesCA=vnsCapabilitiesCA, mscRtgVnsIfIndex=mscRtgVnsIfIndex, mscRtgVnsLpStatsFwdStatsEntry=mscRtgVnsLpStatsFwdStatsEntry, mscRtgVnsNodeStorageType=mscRtgVnsNodeStorageType, vnsMIB=vnsMIB, mscRtgVnsMultiRxDiscPkts=mscRtgVnsMultiRxDiscPkts, mscRtgVnsAdminState=mscRtgVnsAdminState, mscRtgVnsNodeNextHopLinkGroup1=mscRtgVnsNodeNextHopLinkGroup1, mscRtgVnsIfAdminStatus=mscRtgVnsIfAdminStatus, mscRtgVnsLpStatsStorageType=mscRtgVnsLpStatsStorageType, mscRtgVnsLinkToProtocolPort=mscRtgVnsLinkToProtocolPort, mscRtgVnsComponentName=mscRtgVnsComponentName, mscRtgVnsUniTxPkts=mscRtgVnsUniTxPkts, mscRtgVnsOperTable=mscRtgVnsOperTable, mscRtgVnsNodeRowStatusTable=mscRtgVnsNodeRowStatusTable, mscRtgVnsUniTxDiscPkts=mscRtgVnsUniTxDiscPkts, mscRtgVnsLpStatsRowStatusEntry=mscRtgVnsLpStatsRowStatusEntry, mscRtgVnsNodeMetric=mscRtgVnsNodeMetric, mscRtgVnsLpStatsUniRxBytes=mscRtgVnsLpStatsUniRxBytes, mscRtgVnsMaximumTransmissionUnit=mscRtgVnsMaximumTransmissionUnit, mscRtgVnsTotalTxBytes=mscRtgVnsTotalTxBytes)