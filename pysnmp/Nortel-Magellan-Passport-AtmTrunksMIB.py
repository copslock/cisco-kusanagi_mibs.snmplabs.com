#
# PySNMP MIB module Nortel-Magellan-Passport-AtmTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-AtmTrunksMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
RowStatus, Gauge32, Unsigned32, StorageType, DisplayString = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "RowStatus", "Gauge32", "Unsigned32", "StorageType", "DisplayString")
Link, FixedPoint1, NonReplicated = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "Link", "FixedPoint1", "NonReplicated")
trkIndex, trk = mibBuilder.importSymbols("Nortel-Magellan-Passport-TrunksMIB", "trkIndex", "trk")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, ModuleIdentity, Counter32, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Unsigned32, TimeTicks, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Unsigned32", "TimeTicks", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59))
trkAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3))
trkAtmRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1), )
if mibBuilder.loadTexts: trkAtmRowStatusTable.setStatus('mandatory')
trkAtmRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"))
if mibBuilder.loadTexts: trkAtmRowStatusEntry.setStatus('mandatory')
trkAtmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmRowStatus.setStatus('mandatory')
trkAtmComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmComponentName.setStatus('mandatory')
trkAtmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmStorageType.setStatus('mandatory')
trkAtmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: trkAtmIndex.setStatus('mandatory')
trkAtmProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10), )
if mibBuilder.loadTexts: trkAtmProvTable.setStatus('mandatory')
trkAtmProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"))
if mibBuilder.loadTexts: trkAtmProvEntry.setStatus('mandatory')
trkAtmMaximumErroredInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmMaximumErroredInterval.setStatus('obsolete')
trkAtmReceiveErrorSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmReceiveErrorSensitivity.setStatus('mandatory')
trkAtmAtmAccMaximumErroredInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 10, 1, 3), FixedPoint1().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(15, 15), ValueRangeConstraint(20, 20), ValueRangeConstraint(25, 25), ValueRangeConstraint(30, 30), ValueRangeConstraint(35, 35), ValueRangeConstraint(40, 40), ValueRangeConstraint(45, 45), ValueRangeConstraint(50, 50), ValueRangeConstraint(60, 60), ValueRangeConstraint(70, 70), ValueRangeConstraint(80, 80), ValueRangeConstraint(90, 90), ValueRangeConstraint(100, 100), ValueRangeConstraint(110, 110), ValueRangeConstraint(120, 120), ValueRangeConstraint(130, 130), ValueRangeConstraint(140, 140), ValueRangeConstraint(150, 150), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmAtmAccMaximumErroredInterval.setStatus('mandatory')
trkAtmInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11), )
if mibBuilder.loadTexts: trkAtmInterfaceTable.setStatus('mandatory')
trkAtmInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"))
if mibBuilder.loadTexts: trkAtmInterfaceEntry.setStatus('mandatory')
trkAtmAtmConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmAtmConnection.setStatus('mandatory')
trkAtmBwElastic = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmBwElastic.setStatus('mandatory')
trkAtmVccReportingBw = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("pcr", 0), ("acr", 1))).clone('pcr')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmVccReportingBw.setStatus('mandatory')
trkAtmStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12), )
if mibBuilder.loadTexts: trkAtmStateTable.setStatus('mandatory')
trkAtmStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"))
if mibBuilder.loadTexts: trkAtmStateEntry.setStatus('mandatory')
trkAtmAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmAdminState.setStatus('mandatory')
trkAtmOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmOperationalState.setStatus('mandatory')
trkAtmUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmUsageState.setStatus('mandatory')
trkAtmAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmAvailabilityStatus.setStatus('mandatory')
trkAtmProceduralStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmProceduralStatus.setStatus('mandatory')
trkAtmControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmControlStatus.setStatus('mandatory')
trkAtmAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmAlarmStatus.setStatus('mandatory')
trkAtmStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 15))).clone(namedValues=NamedValues(("hotStandby", 0), ("coldStandby", 1), ("providingService", 2), ("notSet", 15))).clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmStandbyStatus.setStatus('mandatory')
trkAtmUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 12, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmUnknownStatus.setStatus('mandatory')
trkAtmUtilTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14), )
if mibBuilder.loadTexts: trkAtmUtilTable.setStatus('mandatory')
trkAtmUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"))
if mibBuilder.loadTexts: trkAtmUtilEntry.setStatus('mandatory')
trkAtmMinorVccUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(75)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmMinorVccUtilAlarmThreshold.setStatus('mandatory')
trkAtmMajorVccUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(85)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmMajorVccUtilAlarmThreshold.setStatus('mandatory')
trkAtmCriticalVccUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(95)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmCriticalVccUtilAlarmThreshold.setStatus('mandatory')
trkAtmVccUtilAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 14, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkAtmVccUtilAlarmStatus.setStatus('mandatory')
trkAtmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15), )
if mibBuilder.loadTexts: trkAtmStatsTable.setStatus('mandatory')
trkAtmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-AtmTrunksMIB", "trkAtmIndex"))
if mibBuilder.loadTexts: trkAtmStatsEntry.setStatus('mandatory')
trkAtmLastCalculatedVccUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmLastCalculatedVccUtilization.setStatus('mandatory')
trkAtmLastCalculatedTxVccUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 3, 15, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkAtmLastCalculatedTxVccUtilization.setStatus('mandatory')
atmTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1))
atmTrunksGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1, 5))
atmTrunksGroupBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1, 5, 2))
atmTrunksGroupBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 1, 5, 2, 2))
atmTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3))
atmTrunksCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3, 5))
atmTrunksCapabilitiesBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3, 5, 2))
atmTrunksCapabilitiesBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 59, 3, 5, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-AtmTrunksMIB", trkAtmMinorVccUtilAlarmThreshold=trkAtmMinorVccUtilAlarmThreshold, trkAtmProvEntry=trkAtmProvEntry, trkAtmStatsTable=trkAtmStatsTable, trkAtmRowStatusTable=trkAtmRowStatusTable, trkAtmStandbyStatus=trkAtmStandbyStatus, trkAtmStateTable=trkAtmStateTable, atmTrunksGroupBE=atmTrunksGroupBE, trkAtmVccUtilAlarmStatus=trkAtmVccUtilAlarmStatus, trkAtmProceduralStatus=trkAtmProceduralStatus, atmTrunksCapabilities=atmTrunksCapabilities, trkAtmReceiveErrorSensitivity=trkAtmReceiveErrorSensitivity, atmTrunksCapabilitiesBE01A=atmTrunksCapabilitiesBE01A, atmTrunksGroup=atmTrunksGroup, trkAtmUnknownStatus=trkAtmUnknownStatus, trkAtmAtmAccMaximumErroredInterval=trkAtmAtmAccMaximumErroredInterval, trkAtmRowStatusEntry=trkAtmRowStatusEntry, atmTrunksGroupBE01A=atmTrunksGroupBE01A, trkAtmUsageState=trkAtmUsageState, trkAtmIndex=trkAtmIndex, trkAtmUtilTable=trkAtmUtilTable, trkAtmAvailabilityStatus=trkAtmAvailabilityStatus, trkAtmOperationalState=trkAtmOperationalState, trkAtmMajorVccUtilAlarmThreshold=trkAtmMajorVccUtilAlarmThreshold, atmTrunksCapabilitiesBE=atmTrunksCapabilitiesBE, atmTrunksCapabilitiesBE01=atmTrunksCapabilitiesBE01, trkAtmComponentName=trkAtmComponentName, trkAtmAlarmStatus=trkAtmAlarmStatus, trkAtmAdminState=trkAtmAdminState, trkAtmStatsEntry=trkAtmStatsEntry, trkAtmInterfaceTable=trkAtmInterfaceTable, atmTrunksGroupBE01=atmTrunksGroupBE01, trkAtmUtilEntry=trkAtmUtilEntry, trkAtmBwElastic=trkAtmBwElastic, trkAtmLastCalculatedVccUtilization=trkAtmLastCalculatedVccUtilization, atmTrunksMIB=atmTrunksMIB, trkAtmRowStatus=trkAtmRowStatus, trkAtmAtmConnection=trkAtmAtmConnection, trkAtmCriticalVccUtilAlarmThreshold=trkAtmCriticalVccUtilAlarmThreshold, trkAtmProvTable=trkAtmProvTable, trkAtmInterfaceEntry=trkAtmInterfaceEntry, trkAtmStateEntry=trkAtmStateEntry, trkAtmStorageType=trkAtmStorageType, trkAtmVccReportingBw=trkAtmVccReportingBw, trkAtmLastCalculatedTxVccUtilization=trkAtmLastCalculatedTxVccUtilization, trkAtmControlStatus=trkAtmControlStatus, trkAtmMaximumErroredInterval=trkAtmMaximumErroredInterval, trkAtm=trkAtm)