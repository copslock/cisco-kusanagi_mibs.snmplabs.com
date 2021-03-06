#
# PySNMP MIB module ASCEND-MIBREDUNDANCYSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBREDUNDANCYSTATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, Gauge32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Unsigned32, Integer32, ModuleIdentity, TimeTicks, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Unsigned32", "Integer32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibredundancyStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 104))
mibredundancyStatsProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 17))
mibredundancyStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 104, 1), )
if mibBuilder.loadTexts: mibredundancyStatisticsTable.setStatus('mandatory')
mibredundancyStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1), ).setIndexNames((0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatistics-Index-o"))
if mibBuilder.loadTexts: mibredundancyStatisticsEntry.setStatus('mandatory')
redundancyStatistics_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1, 1), Integer32()).setLabel("redundancyStatistics-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatistics_Index_o.setStatus('mandatory')
redundancyStatistics_SerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1, 2), Integer32()).setLabel("redundancyStatistics-SerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatistics_SerialNumber.setStatus('mandatory')
redundancyStatistics_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("redundancyStatistics-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redundancyStatistics_Action_o.setStatus('mandatory')
mibredundancyStatsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 17, 1), )
if mibBuilder.loadTexts: mibredundancyStatsProfileTable.setStatus('mandatory')
mibredundancyStatsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 17, 1, 1), ).setIndexNames((0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatsProfile-Index-o"))
if mibBuilder.loadTexts: mibredundancyStatsProfileEntry.setStatus('mandatory')
redundancyStatsProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 1, 1, 1), Integer32()).setLabel("redundancyStatsProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_Index_o.setStatus('mandatory')
redundancyStatsProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("redundancyStatsProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: redundancyStatsProfile_Action_o.setStatus('mandatory')
mibredundancyStatsProfile_ContextStatsTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 17, 2), ).setLabel("mibredundancyStatsProfile-ContextStatsTable")
if mibBuilder.loadTexts: mibredundancyStatsProfile_ContextStatsTable.setStatus('mandatory')
mibredundancyStatsProfile_ContextStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1), ).setLabel("mibredundancyStatsProfile-ContextStatsEntry").setIndexNames((0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatsProfile-ContextStats-Index-o"), (0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatsProfile-ContextStats-Index1-o"))
if mibBuilder.loadTexts: mibredundancyStatsProfile_ContextStatsEntry.setStatus('mandatory')
redundancyStatsProfile_ContextStats_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 1), Integer32()).setLabel("redundancyStatsProfile-ContextStats-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_Index_o.setStatus('mandatory')
redundancyStatsProfile_ContextStats_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 2), Integer32()).setLabel("redundancyStatsProfile-ContextStats-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_Index1_o.setStatus('mandatory')
redundancyStatsProfile_ContextStats_State = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("initial", 1), ("loadContext", 2), ("startPost", 3), ("localPost", 4), ("remotePost", 5), ("selecting", 6), ("selectionComplete", 7), ("inauguration", 8), ("primaryToOperational", 9), ("loading", 10), ("secondaryToOperational", 11), ("monitoring", 12), ("dead", 13), ("restrictRedundancy", 14)))).setLabel("redundancyStatsProfile-ContextStats-State").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_State.setStatus('mandatory')
redundancyStatsProfile_ContextStats_Function = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noFunction", 1), ("primary", 2), ("secondary", 3)))).setLabel("redundancyStatsProfile-ContextStats-Function").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_Function.setStatus('mandatory')
redundancyStatsProfile_ContextStats_SelectReason = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32))).clone(namedValues=NamedValues(("noReason", 1), ("deferToRunningPrimary", 2), ("noRunningPrimary", 3), ("singleControllerOperation", 4), ("localPrimaryPreference", 5), ("remotePrimaryPreference", 6), ("localCrash", 7), ("remoteCrash", 8), ("localLocalLocalError", 9), ("remoteLocalLocalError", 10), ("localRemoteLocalError", 11), ("remoteRemoteLocalError", 12), ("localMatchesChassis", 13), ("remoteMatchesChassis", 14), ("priorPairFunction", 15), ("localPrimaryResources", 16), ("remotePrimaryResources", 17), ("localSecondaryResources", 18), ("remoteSecondaryResources", 19), ("priorLocalPrimary", 20), ("priorRemotePrimary", 21), ("localCrashHistory", 22), ("remoteCrashHistory", 23), ("localLocalLocalErrorHistory", 24), ("remoteLocalLocalErrorHistory", 25), ("localRemoteLocalErrorHistory", 26), ("remoteRemoteLocalErrorHistory", 27), ("localSlotNumber", 28), ("remoteSlotNumber", 29), ("contentionResolution", 30), ("unableToAcquireBuses", 31), ("communicationLoss", 32)))).setLabel("redundancyStatsProfile-ContextStats-SelectReason").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_SelectReason.setStatus('mandatory')
redundancyStatsProfile_ContextStats_PriorFunction = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noFunction", 1), ("primary", 2), ("secondary", 3)))).setLabel("redundancyStatsProfile-ContextStats-PriorFunction").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_PriorFunction.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LastReboot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("crash", 1), ("localReportLocalError", 2), ("remoteReportLocalError", 3), ("localReportRemoteError", 4), ("remoteReportRemoteError", 5), ("localManualReboot", 6), ("remoteManualReboot", 7), ("redundantControllerSwitchCmd", 8), ("numberOfRebootTypes", 9), ("primaryOperationalReboot", 10), ("secondaryOperationalReboot", 11)))).setLabel("redundancyStatsProfile-ContextStats-LastReboot").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LastReboot.setStatus('mandatory')
redundancyStatsProfile_ContextStats_Local_SerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 8), Integer32()).setLabel("redundancyStatsProfile-ContextStats-Local-SerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_Local_SerialNumber.setStatus('mandatory')
redundancyStatsProfile_ContextStats_Pair_SerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 9), Integer32()).setLabel("redundancyStatsProfile-ContextStats-Pair-SerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_Pair_SerialNumber.setStatus('mandatory')
redundancyStatsProfile_ContextStats_ChassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 11), Integer32()).setLabel("redundancyStatsProfile-ContextStats-ChassisSerialNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_ChassisSerialNumber.setStatus('mandatory')
redundancyStatsProfile_ContextStats_InitializationTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 12), Integer32()).setLabel("redundancyStatsProfile-ContextStats-InitializationTime").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_InitializationTime.setStatus('mandatory')
redundancyStatsProfile_ContextStats_PostStart = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 13), Integer32()).setLabel("redundancyStatsProfile-ContextStats-PostStart").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_PostStart.setStatus('mandatory')
redundancyStatsProfile_ContextStats_PostEnd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 14), Integer32()).setLabel("redundancyStatsProfile-ContextStats-PostEnd").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_PostEnd.setStatus('mandatory')
redundancyStatsProfile_ContextStats_SelectionStart = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 15), Integer32()).setLabel("redundancyStatsProfile-ContextStats-SelectionStart").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_SelectionStart.setStatus('mandatory')
redundancyStatsProfile_ContextStats_SelectionEnd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 16), Integer32()).setLabel("redundancyStatsProfile-ContextStats-SelectionEnd").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_SelectionEnd.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LoadStart = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 17), Integer32()).setLabel("redundancyStatsProfile-ContextStats-LoadStart").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LoadStart.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LoadEnd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 18), Integer32()).setLabel("redundancyStatsProfile-ContextStats-LoadEnd").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LoadEnd.setStatus('mandatory')
redundancyStatsProfile_ContextStats_InaugurationTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 19), Integer32()).setLabel("redundancyStatsProfile-ContextStats-InaugurationTime").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_InaugurationTime.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LastSent = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 20), Integer32()).setLabel("redundancyStatsProfile-ContextStats-LastSent").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LastSent.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LastReceived = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 21), Integer32()).setLabel("redundancyStatsProfile-ContextStats-LastReceived").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LastReceived.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LastProfileSync = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 22), Integer32()).setLabel("redundancyStatsProfile-ContextStats-LastProfileSync").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LastProfileSync.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LastCodeSync = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 23), Integer32()).setLabel("redundancyStatsProfile-ContextStats-LastCodeSync").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LastCodeSync.setStatus('mandatory')
redundancyStatsProfile_ContextStats_LastLogRecv = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 24), Integer32()).setLabel("redundancyStatsProfile-ContextStats-LastLogRecv").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_LastLogRecv.setStatus('mandatory')
redundancyStatsProfile_ContextStats_UpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 25), Integer32()).setLabel("redundancyStatsProfile-ContextStats-UpdateTime").setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyStatsProfile_ContextStats_UpdateTime.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBREDUNDANCYSTATS-MIB", redundancyStatsProfile_Index_o=redundancyStatsProfile_Index_o, redundancyStatistics_SerialNumber=redundancyStatistics_SerialNumber, mibredundancyStatsProfileTable=mibredundancyStatsProfileTable, redundancyStatsProfile_ContextStats_InitializationTime=redundancyStatsProfile_ContextStats_InitializationTime, redundancyStatsProfile_ContextStats_SelectReason=redundancyStatsProfile_ContextStats_SelectReason, redundancyStatsProfile_ContextStats_LastProfileSync=redundancyStatsProfile_ContextStats_LastProfileSync, redundancyStatsProfile_ContextStats_SelectionEnd=redundancyStatsProfile_ContextStats_SelectionEnd, redundancyStatsProfile_ContextStats_InaugurationTime=redundancyStatsProfile_ContextStats_InaugurationTime, redundancyStatsProfile_ContextStats_LastLogRecv=redundancyStatsProfile_ContextStats_LastLogRecv, redundancyStatsProfile_ContextStats_PostStart=redundancyStatsProfile_ContextStats_PostStart, mibredundancyStatsProfileEntry=mibredundancyStatsProfileEntry, redundancyStatsProfile_ContextStats_State=redundancyStatsProfile_ContextStats_State, redundancyStatsProfile_ContextStats_LastSent=redundancyStatsProfile_ContextStats_LastSent, redundancyStatsProfile_ContextStats_Index_o=redundancyStatsProfile_ContextStats_Index_o, redundancyStatistics_Action_o=redundancyStatistics_Action_o, redundancyStatsProfile_ContextStats_LastReboot=redundancyStatsProfile_ContextStats_LastReboot, DisplayString=DisplayString, mibredundancyStatisticsTable=mibredundancyStatisticsTable, redundancyStatsProfile_ContextStats_Function=redundancyStatsProfile_ContextStats_Function, redundancyStatsProfile_ContextStats_LoadStart=redundancyStatsProfile_ContextStats_LoadStart, mibredundancyStatsProfile=mibredundancyStatsProfile, redundancyStatsProfile_ContextStats_PostEnd=redundancyStatsProfile_ContextStats_PostEnd, redundancyStatsProfile_ContextStats_Local_SerialNumber=redundancyStatsProfile_ContextStats_Local_SerialNumber, redundancyStatsProfile_ContextStats_LastReceived=redundancyStatsProfile_ContextStats_LastReceived, mibredundancyStatisticsEntry=mibredundancyStatisticsEntry, redundancyStatsProfile_ContextStats_SelectionStart=redundancyStatsProfile_ContextStats_SelectionStart, redundancyStatsProfile_ContextStats_Index1_o=redundancyStatsProfile_ContextStats_Index1_o, mibredundancyStatsProfile_ContextStatsEntry=mibredundancyStatsProfile_ContextStatsEntry, mibredundancyStatistics=mibredundancyStatistics, redundancyStatsProfile_ContextStats_LoadEnd=redundancyStatsProfile_ContextStats_LoadEnd, redundancyStatsProfile_ContextStats_UpdateTime=redundancyStatsProfile_ContextStats_UpdateTime, redundancyStatsProfile_ContextStats_Pair_SerialNumber=redundancyStatsProfile_ContextStats_Pair_SerialNumber, redundancyStatistics_Index_o=redundancyStatistics_Index_o, redundancyStatsProfile_Action_o=redundancyStatsProfile_Action_o, redundancyStatsProfile_ContextStats_LastCodeSync=redundancyStatsProfile_ContextStats_LastCodeSync, redundancyStatsProfile_ContextStats_ChassisSerialNumber=redundancyStatsProfile_ContextStats_ChassisSerialNumber, redundancyStatsProfile_ContextStats_PriorFunction=redundancyStatsProfile_ContextStats_PriorFunction, mibredundancyStatsProfile_ContextStatsTable=mibredundancyStatsProfile_ContextStatsTable)
