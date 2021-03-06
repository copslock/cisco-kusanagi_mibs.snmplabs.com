#
# PySNMP MIB module GWPOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GWPOA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, NotificationType, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, MibIdentifier, Bits, Gauge32, NotificationType, Counter32, Unsigned32, ModuleIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "NotificationType", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "Gauge32", "NotificationType", "Counter32", "Unsigned32", "ModuleIdentity", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
gwpoa = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38))
poa = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38, 1))
poaTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38, 2))
poaTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 38, 3))
poaTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1), )
if mibBuilder.loadTexts: poaTable.setStatus('mandatory')
poaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1), ).setIndexNames((0, "GWPOA-MIB", "poaIndex"))
if mibBuilder.loadTexts: poaEntry.setStatus('mandatory')
poaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaIndex.setStatus('mandatory')
poaPostOfficeName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaPostOfficeName.setStatus('mandatory')
poaTotalMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaTotalMsgs.setStatus('mandatory')
poaProblemMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaProblemMsgs.setStatus('mandatory')
poaStatuses = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaStatuses.setStatus('mandatory')
poaDeliveredUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaDeliveredUsers.setStatus('mandatory')
poaExecutedRules = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaExecutedRules.setStatus('mandatory')
poaUndeliverableMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaUndeliverableMsgs.setStatus('mandatory')
poaPriorityQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaPriorityQueues.setStatus('mandatory')
poaNormalQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaNormalQueues.setStatus('mandatory')
poaUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaUptime.setStatus('mandatory')
poaCurrentLogFile = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCurrentLogFile.setStatus('mandatory')
poaLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("verbose", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaLogLevel.setStatus('mandatory')
poaFileLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaFileLogging.setStatus('mandatory')
poaMaxLogFileAge = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaMaxLogFileAge.setStatus('mandatory')
poaMaxLogDiskSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaMaxLogDiskSpace.setStatus('mandatory')
poaCSRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSRequests.setStatus('mandatory')
poaCSRequestsPending = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSRequestsPending.setStatus('mandatory')
poaCSUserTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSUserTimeouts.setStatus('mandatory')
poaCSFileQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSFileQueues.setStatus('mandatory')
poaCSUsersConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaCSUsersConnected.setStatus('mandatory')
poaGUID = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 36))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaGUID.setStatus('mandatory')
poaOS = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaOS.setStatus('mandatory')
poaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaVersion.setStatus('mandatory')
poaAdmThreadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmThreadStatus.setStatus('mandatory')
poaAdmCompletedMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmCompletedMsgs.setStatus('mandatory')
poaAdmErrorMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmErrorMsgs.setStatus('mandatory')
poaAdmInQueueMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 28), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmInQueueMsgs.setStatus('mandatory')
poaAdmDBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmDBStatus.setStatus('mandatory')
poaAdmDBSortLang = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmDBSortLang.setStatus('mandatory')
poaAdmDBRecoverCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAdmDBRecoverCnt.setStatus('mandatory')
poaDN = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaDN.setStatus('mandatory')
poaAvailDiskSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaAvailDiskSpace.setStatus('mandatory')
poaHTTPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 34), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaHTTPPort.setStatus('mandatory')
poaAdmDBStatusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("normal", 0), ("error", 1), ("recovering", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaAdmDBStatusNumber.setStatus('mandatory')
poaMTPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("closed", 1), ("open", 2), ("sendopen", 3), ("receiveopen", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poaMTPStatus.setStatus('mandatory')
poaUptimeInSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 38, 1, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poaUptimeInSeconds.setStatus('mandatory')
poaTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 38, 2, 1), Integer32())
if mibBuilder.loadTexts: poaTrapTime.setStatus('mandatory')
poaStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 38, 3) + (0,1)).setObjects(("GWPOA-MIB", "poaTrapTime"), ("GWPOA-MIB", "poaPostOfficeName"), ("GWPOA-MIB", "poaGUID"))
poaShutdownTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 38, 3) + (0,2)).setObjects(("GWPOA-MIB", "poaTrapTime"), ("GWPOA-MIB", "poaPostOfficeName"), ("GWPOA-MIB", "poaGUID"))
mibBuilder.exportSymbols("GWPOA-MIB", poaAdmDBStatusNumber=poaAdmDBStatusNumber, poa=poa, poaAdmDBRecoverCnt=poaAdmDBRecoverCnt, poaMaxLogFileAge=poaMaxLogFileAge, poaTotalMsgs=poaTotalMsgs, poaDN=poaDN, poaEntry=poaEntry, poaAdmDBStatus=poaAdmDBStatus, poaVersion=poaVersion, poaTrapTime=poaTrapTime, poaMTPStatus=poaMTPStatus, poaIndex=poaIndex, poaExecutedRules=poaExecutedRules, poaFileLogging=poaFileLogging, poaUndeliverableMsgs=poaUndeliverableMsgs, poaDeliveredUsers=poaDeliveredUsers, poaLogLevel=poaLogLevel, poaStartTrap=poaStartTrap, poaCSRequestsPending=poaCSRequestsPending, poaCSUsersConnected=poaCSUsersConnected, poaTable=poaTable, gwpoa=gwpoa, poaPostOfficeName=poaPostOfficeName, poaCSUserTimeouts=poaCSUserTimeouts, mibDoc=mibDoc, poaMaxLogDiskSpace=poaMaxLogDiskSpace, poaOS=poaOS, poaAvailDiskSpace=poaAvailDiskSpace, poaUptimeInSeconds=poaUptimeInSeconds, poaShutdownTrap=poaShutdownTrap, poaAdmCompletedMsgs=poaAdmCompletedMsgs, novell=novell, poaStatuses=poaStatuses, poaAdmErrorMsgs=poaAdmErrorMsgs, poaAdmDBSortLang=poaAdmDBSortLang, poaAdmInQueueMsgs=poaAdmInQueueMsgs, poaUptime=poaUptime, poaGUID=poaGUID, poaHTTPPort=poaHTTPPort, poaCSRequests=poaCSRequests, poaTraps=poaTraps, poaPriorityQueues=poaPriorityQueues, poaNormalQueues=poaNormalQueues, poaCurrentLogFile=poaCurrentLogFile, poaAdmThreadStatus=poaAdmThreadStatus, poaTrapInfo=poaTrapInfo, poaProblemMsgs=poaProblemMsgs, poaCSFileQueues=poaCSFileQueues)
