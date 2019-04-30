#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-AtmTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-AtmTrunksMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:19:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
StorageType, RowStatus, Gauge32, DisplayString, Unsigned32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "StorageType", "RowStatus", "Gauge32", "DisplayString", "Unsigned32")
FixedPoint1, Link, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "FixedPoint1", "Link", "NonReplicated")
mscTrkIndex, mscTrk = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex", "mscTrk")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Integer32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ObjectIdentity, TimeTicks, Counter32, Bits, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Integer32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Counter32", "Bits", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59))
mscTrkAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3))
mscTrkAtmRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1), )
if mibBuilder.loadTexts: mscTrkAtmRowStatusTable.setStatus('mandatory')
mscTrkAtmRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"))
if mibBuilder.loadTexts: mscTrkAtmRowStatusEntry.setStatus('mandatory')
mscTrkAtmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmRowStatus.setStatus('mandatory')
mscTrkAtmComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmComponentName.setStatus('mandatory')
mscTrkAtmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmStorageType.setStatus('mandatory')
mscTrkAtmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscTrkAtmIndex.setStatus('mandatory')
mscTrkAtmProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10), )
if mibBuilder.loadTexts: mscTrkAtmProvTable.setStatus('mandatory')
mscTrkAtmProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"))
if mibBuilder.loadTexts: mscTrkAtmProvEntry.setStatus('mandatory')
mscTrkAtmMaximumErroredInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmMaximumErroredInterval.setStatus('obsolete')
mscTrkAtmReceiveErrorSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmReceiveErrorSensitivity.setStatus('mandatory')
mscTrkAtmAtmAccMaximumErroredInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 10, 1, 3), FixedPoint1().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(15, 15), ValueRangeConstraint(20, 20), ValueRangeConstraint(25, 25), ValueRangeConstraint(30, 30), ValueRangeConstraint(35, 35), ValueRangeConstraint(40, 40), ValueRangeConstraint(45, 45), ValueRangeConstraint(50, 50), ValueRangeConstraint(60, 60), ValueRangeConstraint(70, 70), ValueRangeConstraint(80, 80), ValueRangeConstraint(90, 90), ValueRangeConstraint(100, 100), ValueRangeConstraint(110, 110), ValueRangeConstraint(120, 120), ValueRangeConstraint(130, 130), ValueRangeConstraint(140, 140), ValueRangeConstraint(150, 150), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmAtmAccMaximumErroredInterval.setStatus('mandatory')
mscTrkAtmInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11), )
if mibBuilder.loadTexts: mscTrkAtmInterfaceTable.setStatus('mandatory')
mscTrkAtmInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"))
if mibBuilder.loadTexts: mscTrkAtmInterfaceEntry.setStatus('mandatory')
mscTrkAtmAtmConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmAtmConnection.setStatus('mandatory')
mscTrkAtmBwElastic = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmBwElastic.setStatus('mandatory')
mscTrkAtmVccReportingBw = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("pcr", 0), ("acr", 1))).clone('pcr')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmVccReportingBw.setStatus('mandatory')
mscTrkAtmStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12), )
if mibBuilder.loadTexts: mscTrkAtmStateTable.setStatus('mandatory')
mscTrkAtmStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"))
if mibBuilder.loadTexts: mscTrkAtmStateEntry.setStatus('mandatory')
mscTrkAtmAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmAdminState.setStatus('mandatory')
mscTrkAtmOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmOperationalState.setStatus('mandatory')
mscTrkAtmUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmUsageState.setStatus('mandatory')
mscTrkAtmAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmAvailabilityStatus.setStatus('mandatory')
mscTrkAtmProceduralStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmProceduralStatus.setStatus('mandatory')
mscTrkAtmControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmControlStatus.setStatus('mandatory')
mscTrkAtmAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmAlarmStatus.setStatus('mandatory')
mscTrkAtmStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 15))).clone(namedValues=NamedValues(("hotStandby", 0), ("coldStandby", 1), ("providingService", 2), ("notSet", 15))).clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmStandbyStatus.setStatus('mandatory')
mscTrkAtmUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 12, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmUnknownStatus.setStatus('mandatory')
mscTrkAtmUtilTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14), )
if mibBuilder.loadTexts: mscTrkAtmUtilTable.setStatus('mandatory')
mscTrkAtmUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"))
if mibBuilder.loadTexts: mscTrkAtmUtilEntry.setStatus('mandatory')
mscTrkAtmMinorVccUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(75)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmMinorVccUtilAlarmThreshold.setStatus('mandatory')
mscTrkAtmMajorVccUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(85)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmMajorVccUtilAlarmThreshold.setStatus('mandatory')
mscTrkAtmCriticalVccUtilAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(95)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmCriticalVccUtilAlarmThreshold.setStatus('mandatory')
mscTrkAtmVccUtilAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 14, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkAtmVccUtilAlarmStatus.setStatus('mandatory')
mscTrkAtmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15), )
if mibBuilder.loadTexts: mscTrkAtmStatsTable.setStatus('mandatory')
mscTrkAtmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmTrunksMIB", "mscTrkAtmIndex"))
if mibBuilder.loadTexts: mscTrkAtmStatsEntry.setStatus('mandatory')
mscTrkAtmLastCalculatedVccUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmLastCalculatedVccUtilization.setStatus('mandatory')
mscTrkAtmLastCalculatedTxVccUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 3, 15, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkAtmLastCalculatedTxVccUtilization.setStatus('mandatory')
atmTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1))
atmTrunksGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1, 1))
atmTrunksGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1, 1, 3))
atmTrunksGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 1, 1, 3, 2))
atmTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3))
atmTrunksCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3, 1))
atmTrunksCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3, 1, 3))
atmTrunksCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 59, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-AtmTrunksMIB", mscTrkAtmControlStatus=mscTrkAtmControlStatus, mscTrkAtmStateEntry=mscTrkAtmStateEntry, mscTrkAtmAlarmStatus=mscTrkAtmAlarmStatus, atmTrunksGroupCA=atmTrunksGroupCA, atmTrunksCapabilitiesCA=atmTrunksCapabilitiesCA, mscTrkAtmProvEntry=mscTrkAtmProvEntry, mscTrkAtmUtilTable=mscTrkAtmUtilTable, atmTrunksMIB=atmTrunksMIB, mscTrkAtmStateTable=mscTrkAtmStateTable, mscTrkAtmInterfaceEntry=mscTrkAtmInterfaceEntry, mscTrkAtmRowStatusTable=mscTrkAtmRowStatusTable, mscTrkAtmInterfaceTable=mscTrkAtmInterfaceTable, mscTrkAtmComponentName=mscTrkAtmComponentName, mscTrkAtmAvailabilityStatus=mscTrkAtmAvailabilityStatus, atmTrunksCapabilitiesCA02=atmTrunksCapabilitiesCA02, mscTrkAtmBwElastic=mscTrkAtmBwElastic, mscTrkAtm=mscTrkAtm, mscTrkAtmMajorVccUtilAlarmThreshold=mscTrkAtmMajorVccUtilAlarmThreshold, mscTrkAtmProvTable=mscTrkAtmProvTable, atmTrunksGroup=atmTrunksGroup, mscTrkAtmUsageState=mscTrkAtmUsageState, mscTrkAtmOperationalState=mscTrkAtmOperationalState, mscTrkAtmVccUtilAlarmStatus=mscTrkAtmVccUtilAlarmStatus, mscTrkAtmAdminState=mscTrkAtmAdminState, mscTrkAtmStatsEntry=mscTrkAtmStatsEntry, mscTrkAtmIndex=mscTrkAtmIndex, atmTrunksGroupCA02A=atmTrunksGroupCA02A, mscTrkAtmVccReportingBw=mscTrkAtmVccReportingBw, atmTrunksGroupCA02=atmTrunksGroupCA02, mscTrkAtmUnknownStatus=mscTrkAtmUnknownStatus, mscTrkAtmRowStatusEntry=mscTrkAtmRowStatusEntry, mscTrkAtmStorageType=mscTrkAtmStorageType, mscTrkAtmMinorVccUtilAlarmThreshold=mscTrkAtmMinorVccUtilAlarmThreshold, mscTrkAtmRowStatus=mscTrkAtmRowStatus, mscTrkAtmMaximumErroredInterval=mscTrkAtmMaximumErroredInterval, mscTrkAtmProceduralStatus=mscTrkAtmProceduralStatus, mscTrkAtmLastCalculatedVccUtilization=mscTrkAtmLastCalculatedVccUtilization, mscTrkAtmLastCalculatedTxVccUtilization=mscTrkAtmLastCalculatedTxVccUtilization, mscTrkAtmReceiveErrorSensitivity=mscTrkAtmReceiveErrorSensitivity, mscTrkAtmStandbyStatus=mscTrkAtmStandbyStatus, mscTrkAtmAtmConnection=mscTrkAtmAtmConnection, mscTrkAtmAtmAccMaximumErroredInterval=mscTrkAtmAtmAccMaximumErroredInterval, atmTrunksCapabilities=atmTrunksCapabilities, atmTrunksCapabilitiesCA02A=atmTrunksCapabilitiesCA02A, mscTrkAtmUtilEntry=mscTrkAtmUtilEntry, mscTrkAtmCriticalVccUtilAlarmThreshold=mscTrkAtmCriticalVccUtilAlarmThreshold, mscTrkAtmStatsTable=mscTrkAtmStatsTable)