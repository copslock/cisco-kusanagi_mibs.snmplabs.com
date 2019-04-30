#
# PySNMP MIB module DLGSRPRF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLGSRPRF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
dlgPerformanceInfo, = mibBuilder.importSymbols("DLGC-GLOBAL-REG", "dlgPerformanceInfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity, MibIdentifier, ObjectIdentity, iso, NotificationType, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "iso", "NotificationType", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlgPiSram = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1))
dlgPsCurrentStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4))
dlgPsTotalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5))
dlgPiSramMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 6))
dlgPiSramMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPiSramMibRevMajor.setStatus('mandatory')
dlgPiSramMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPiSramMibRevMinor.setStatus('mandatory')
dlgPsStatsEnableMask = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlgPsStatsEnableMask.setStatus('mandatory')
dlgPsPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlgPsPollingInterval.setStatus('mandatory')
dlgPsElapsedTime = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsElapsedTime.setStatus('mandatory')
dlgPsCurrentInterrupts = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentInterrupts.setStatus('mandatory')
dlgPsCurrentDrvCommands = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentDrvCommands.setStatus('mandatory')
dlgPsCurrentFWCommands = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentFWCommands.setStatus('mandatory')
dlgPsCurrentUnSolEvents = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentUnSolEvents.setStatus('mandatory')
dlgPsCurrentBytesRead = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentBytesRead.setStatus('mandatory')
dlgPsCurrentBytesWritten = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentBytesWritten.setStatus('mandatory')
dlgPsCurrentLostMsgToFW = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentLostMsgToFW.setStatus('mandatory')
dlgPsCurrentLostMsgFromFW = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentLostMsgFromFW.setStatus('mandatory')
dlgPsCurrentFWErrorMsgs = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentFWErrorMsgs.setStatus('mandatory')
dlgPsCurrentDrvErrorMsgs = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 4, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsCurrentDrvErrorMsgs.setStatus('mandatory')
dlgPsTotalInterrupts = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalInterrupts.setStatus('mandatory')
dlgPsTotalDrvCommands = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalDrvCommands.setStatus('mandatory')
dlgPsTotalFWCommands = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalFWCommands.setStatus('mandatory')
dlgPsTotalUnSolEvents = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalUnSolEvents.setStatus('mandatory')
dlgPsTotalBytesRead = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalBytesRead.setStatus('mandatory')
dlgPsTotalBytesWritten = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalBytesWritten.setStatus('mandatory')
dlgPsTotalLostMsgToFW = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalLostMsgToFW.setStatus('mandatory')
dlgPsTotalLostMsgFromFW = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalLostMsgFromFW.setStatus('mandatory')
dlgPsTotalFWErrorMsgs = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalFWErrorMsgs.setStatus('mandatory')
dlgPsTotalDrvErrorMsgs = MibScalar((1, 3, 6, 1, 4, 1, 3028, 1, 2, 1, 5, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlgPsTotalDrvErrorMsgs.setStatus('mandatory')
mibBuilder.exportSymbols("DLGSRPRF-MIB", dlgPsTotalBytesRead=dlgPsTotalBytesRead, dlgPsCurrentUnSolEvents=dlgPsCurrentUnSolEvents, dlgPsTotalStats=dlgPsTotalStats, dlgPsTotalBytesWritten=dlgPsTotalBytesWritten, dlgPsCurrentInterrupts=dlgPsCurrentInterrupts, dlgPsCurrentDrvErrorMsgs=dlgPsCurrentDrvErrorMsgs, dlgPsCurrentFWErrorMsgs=dlgPsCurrentFWErrorMsgs, dlgPsPollingInterval=dlgPsPollingInterval, dlgPsCurrentLostMsgToFW=dlgPsCurrentLostMsgToFW, dlgPsCurrentDrvCommands=dlgPsCurrentDrvCommands, dlgPsTotalLostMsgToFW=dlgPsTotalLostMsgToFW, dlgPsCurrentLostMsgFromFW=dlgPsCurrentLostMsgFromFW, dlgPiSram=dlgPiSram, dlgPsTotalUnSolEvents=dlgPsTotalUnSolEvents, dlgPsCurrentStats=dlgPsCurrentStats, dlgPsStatsEnableMask=dlgPsStatsEnableMask, dlgPsTotalFWErrorMsgs=dlgPsTotalFWErrorMsgs, dlgPsCurrentBytesWritten=dlgPsCurrentBytesWritten, dlgPiSramMibRev=dlgPiSramMibRev, dlgPsCurrentBytesRead=dlgPsCurrentBytesRead, dlgPsTotalDrvCommands=dlgPsTotalDrvCommands, dlgPsTotalLostMsgFromFW=dlgPsTotalLostMsgFromFW, dlgPsElapsedTime=dlgPsElapsedTime, dlgPsTotalFWCommands=dlgPsTotalFWCommands, dlgPiSramMibRevMinor=dlgPiSramMibRevMinor, dlgPsTotalDrvErrorMsgs=dlgPsTotalDrvErrorMsgs, dlgPiSramMibRevMajor=dlgPiSramMibRevMajor, dlgPsTotalInterrupts=dlgPsTotalInterrupts, dlgPsCurrentFWCommands=dlgPsCurrentFWCommands)