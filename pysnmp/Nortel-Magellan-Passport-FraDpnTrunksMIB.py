#
# PySNMP MIB module Nortel-Magellan-Passport-FraDpnTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-FraDpnTrunksMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:17:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dpnGateIndex, dpnGate = mibBuilder.importSymbols("Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex", "dpnGate")
StorageType, RowStatus, Gauge32, RowPointer, Counter32, Unsigned32, DisplayString = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "StorageType", "RowStatus", "Gauge32", "RowPointer", "Counter32", "Unsigned32", "DisplayString")
NonReplicated, Link = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "NonReplicated", "Link")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, TimeTicks, Gauge32, Counter32, Bits, Integer32, Unsigned32, NotificationType, ModuleIdentity, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "TimeTicks", "Gauge32", "Counter32", "Bits", "Integer32", "Unsigned32", "NotificationType", "ModuleIdentity", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fraDpnTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68))
dpnGateFrAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4))
dpnGateFrAccessRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1), )
if mibBuilder.loadTexts: dpnGateFrAccessRowStatusTable.setStatus('mandatory')
dpnGateFrAccessRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessRowStatusEntry.setStatus('mandatory')
dpnGateFrAccessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateFrAccessRowStatus.setStatus('mandatory')
dpnGateFrAccessComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessComponentName.setStatus('mandatory')
dpnGateFrAccessStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessStorageType.setStatus('mandatory')
dpnGateFrAccessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dpnGateFrAccessIndex.setStatus('mandatory')
dpnGateFrAccessProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10), )
if mibBuilder.loadTexts: dpnGateFrAccessProvTable.setStatus('mandatory')
dpnGateFrAccessProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessProvEntry.setStatus('mandatory')
dpnGateFrAccessMaximumErroredInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateFrAccessMaximumErroredInterval.setStatus('mandatory')
dpnGateFrAccessReceiveErrorSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateFrAccessReceiveErrorSensitivity.setStatus('mandatory')
dpnGateFrAccessStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11), )
if mibBuilder.loadTexts: dpnGateFrAccessStateTable.setStatus('mandatory')
dpnGateFrAccessStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessStateEntry.setStatus('mandatory')
dpnGateFrAccessAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessAdminState.setStatus('mandatory')
dpnGateFrAccessOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessOperationalState.setStatus('mandatory')
dpnGateFrAccessUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessUsageState.setStatus('mandatory')
dpnGateFrAccessAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessAvailabilityStatus.setStatus('mandatory')
dpnGateFrAccessProceduralStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessProceduralStatus.setStatus('mandatory')
dpnGateFrAccessControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessControlStatus.setStatus('mandatory')
dpnGateFrAccessAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessAlarmStatus.setStatus('mandatory')
dpnGateFrAccessStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 15))).clone(namedValues=NamedValues(("hotStandby", 0), ("coldStandby", 1), ("providingService", 2), ("notSet", 15))).clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessStandbyStatus.setStatus('mandatory')
dpnGateFrAccessUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessUnknownStatus.setStatus('mandatory')
dpnGateFrAccessOpTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 12), )
if mibBuilder.loadTexts: dpnGateFrAccessOpTable.setStatus('mandatory')
dpnGateFrAccessOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessOpEntry.setStatus('mandatory')
dpnGateFrAccessRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 12, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessRoundTripDelay.setStatus('mandatory')
dpnGateFrAccessStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13), )
if mibBuilder.loadTexts: dpnGateFrAccessStatsTable.setStatus('mandatory')
dpnGateFrAccessStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessStatsEntry.setStatus('mandatory')
dpnGateFrAccessReceivedBytesFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessReceivedBytesFromIf.setStatus('mandatory')
dpnGateFrAccessLostFramesFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessLostFramesFromIf.setStatus('mandatory')
dpnGateFrAccessDiscardBadFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessDiscardBadFromIf.setStatus('mandatory')
dpnGateFrAccessDiscardExcessToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessDiscardExcessToIf.setStatus('mandatory')
dpnGateFrAccessFrMuxSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2))
dpnGateFrAccessFrMuxSetupRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1), )
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupRowStatusTable.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupRowStatusEntry.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupRowStatus.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupComponentName.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupStorageType.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupIndex.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupTrafficDescrTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10), )
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupTrafficDescrTable.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupTrafficDescrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupTrafficDescrEntry.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupCommittedInformationRate = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4800, 2048000)).clone(64000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupCommittedInformationRate.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupCommittedBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048000)).clone(64000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupCommittedBurstSize.setStatus('obsolete')
dpnGateFrAccessFrMuxSetupMaximumFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupMaximumFrameSize.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupDlciCompNameOpTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 11), )
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupDlciCompNameOpTable.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupDlciCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 11, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupDlciCompName.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2))
dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1), )
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupPvcSetupIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupRowStatus.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupComponentName.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupStorageType.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupIndex.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 10), )
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupProvTable.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"), (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupPvcSetupIndex"))
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupProvEntry.setStatus('mandatory')
dpnGateFrAccessFrMuxSetupPvcSetupDlciName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpnGateFrAccessFrMuxSetupPvcSetupDlciName.setStatus('mandatory')
fraDpnTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1))
fraDpnTrunksGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1, 5))
fraDpnTrunksGroupBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1, 5, 1))
fraDpnTrunksGroupBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1, 5, 1, 2))
fraDpnTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3))
fraDpnTrunksCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3, 5))
fraDpnTrunksCapabilitiesBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3, 5, 1))
fraDpnTrunksCapabilitiesBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3, 5, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-FraDpnTrunksMIB", dpnGateFrAccessDiscardBadFromIf=dpnGateFrAccessDiscardBadFromIf, fraDpnTrunksCapabilities=fraDpnTrunksCapabilities, dpnGateFrAccessFrMuxSetupTrafficDescrTable=dpnGateFrAccessFrMuxSetupTrafficDescrTable, fraDpnTrunksMIB=fraDpnTrunksMIB, dpnGateFrAccessFrMuxSetupMaximumFrameSize=dpnGateFrAccessFrMuxSetupMaximumFrameSize, dpnGateFrAccessFrMuxSetupDlciCompName=dpnGateFrAccessFrMuxSetupDlciCompName, dpnGateFrAccessFrMuxSetupPvcSetupIndex=dpnGateFrAccessFrMuxSetupPvcSetupIndex, dpnGateFrAccessReceiveErrorSensitivity=dpnGateFrAccessReceiveErrorSensitivity, dpnGateFrAccessFrMuxSetupPvcSetupComponentName=dpnGateFrAccessFrMuxSetupPvcSetupComponentName, dpnGateFrAccessAlarmStatus=dpnGateFrAccessAlarmStatus, dpnGateFrAccessFrMuxSetupCommittedBurstSize=dpnGateFrAccessFrMuxSetupCommittedBurstSize, dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable=dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable, dpnGateFrAccessStateTable=dpnGateFrAccessStateTable, dpnGateFrAccessReceivedBytesFromIf=dpnGateFrAccessReceivedBytesFromIf, dpnGateFrAccessFrMuxSetupStorageType=dpnGateFrAccessFrMuxSetupStorageType, dpnGateFrAccessLostFramesFromIf=dpnGateFrAccessLostFramesFromIf, dpnGateFrAccessFrMuxSetupRowStatus=dpnGateFrAccessFrMuxSetupRowStatus, dpnGateFrAccessComponentName=dpnGateFrAccessComponentName, dpnGateFrAccessFrMuxSetupPvcSetupProvEntry=dpnGateFrAccessFrMuxSetupPvcSetupProvEntry, fraDpnTrunksCapabilitiesBE00A=fraDpnTrunksCapabilitiesBE00A, dpnGateFrAccessOperationalState=dpnGateFrAccessOperationalState, dpnGateFrAccessFrMuxSetupIndex=dpnGateFrAccessFrMuxSetupIndex, fraDpnTrunksGroupBE00A=fraDpnTrunksGroupBE00A, dpnGateFrAccessAvailabilityStatus=dpnGateFrAccessAvailabilityStatus, dpnGateFrAccessFrMuxSetupTrafficDescrEntry=dpnGateFrAccessFrMuxSetupTrafficDescrEntry, dpnGateFrAccessMaximumErroredInterval=dpnGateFrAccessMaximumErroredInterval, dpnGateFrAccessFrMuxSetupPvcSetup=dpnGateFrAccessFrMuxSetupPvcSetup, dpnGateFrAccessFrMuxSetup=dpnGateFrAccessFrMuxSetup, dpnGateFrAccessOpEntry=dpnGateFrAccessOpEntry, fraDpnTrunksGroup=fraDpnTrunksGroup, dpnGateFrAccessProceduralStatus=dpnGateFrAccessProceduralStatus, fraDpnTrunksCapabilitiesBE=fraDpnTrunksCapabilitiesBE, dpnGateFrAccessRowStatusEntry=dpnGateFrAccessRowStatusEntry, dpnGateFrAccessUnknownStatus=dpnGateFrAccessUnknownStatus, dpnGateFrAccessProvTable=dpnGateFrAccessProvTable, dpnGateFrAccessFrMuxSetupPvcSetupDlciName=dpnGateFrAccessFrMuxSetupPvcSetupDlciName, fraDpnTrunksCapabilitiesBE00=fraDpnTrunksCapabilitiesBE00, dpnGateFrAccessStatsTable=dpnGateFrAccessStatsTable, dpnGateFrAccess=dpnGateFrAccess, dpnGateFrAccessOpTable=dpnGateFrAccessOpTable, dpnGateFrAccessStateEntry=dpnGateFrAccessStateEntry, dpnGateFrAccessFrMuxSetupRowStatusEntry=dpnGateFrAccessFrMuxSetupRowStatusEntry, dpnGateFrAccessStatsEntry=dpnGateFrAccessStatsEntry, dpnGateFrAccessDiscardExcessToIf=dpnGateFrAccessDiscardExcessToIf, dpnGateFrAccessUsageState=dpnGateFrAccessUsageState, dpnGateFrAccessProvEntry=dpnGateFrAccessProvEntry, dpnGateFrAccessFrMuxSetupPvcSetupProvTable=dpnGateFrAccessFrMuxSetupPvcSetupProvTable, dpnGateFrAccessControlStatus=dpnGateFrAccessControlStatus, dpnGateFrAccessFrMuxSetupCommittedInformationRate=dpnGateFrAccessFrMuxSetupCommittedInformationRate, fraDpnTrunksGroupBE00=fraDpnTrunksGroupBE00, dpnGateFrAccessIndex=dpnGateFrAccessIndex, fraDpnTrunksGroupBE=fraDpnTrunksGroupBE, dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry=dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry, dpnGateFrAccessFrMuxSetupPvcSetupStorageType=dpnGateFrAccessFrMuxSetupPvcSetupStorageType, dpnGateFrAccessFrMuxSetupRowStatusTable=dpnGateFrAccessFrMuxSetupRowStatusTable, dpnGateFrAccessFrMuxSetupPvcSetupRowStatus=dpnGateFrAccessFrMuxSetupPvcSetupRowStatus, dpnGateFrAccessRowStatus=dpnGateFrAccessRowStatus, dpnGateFrAccessStorageType=dpnGateFrAccessStorageType, dpnGateFrAccessFrMuxSetupComponentName=dpnGateFrAccessFrMuxSetupComponentName, dpnGateFrAccessFrMuxSetupDlciCompNameOpTable=dpnGateFrAccessFrMuxSetupDlciCompNameOpTable, dpnGateFrAccessAdminState=dpnGateFrAccessAdminState, dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry=dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry, dpnGateFrAccessStandbyStatus=dpnGateFrAccessStandbyStatus, dpnGateFrAccessRowStatusTable=dpnGateFrAccessRowStatusTable, dpnGateFrAccessRoundTripDelay=dpnGateFrAccessRoundTripDelay)