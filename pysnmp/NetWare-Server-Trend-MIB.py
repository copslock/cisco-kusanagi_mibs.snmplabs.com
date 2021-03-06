#
# PySNMP MIB module NetWare-Server-Trend-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NetWare-Server-Trend-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InternationalDisplayString, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "InternationalDisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, Counter64, enterprises, NotificationType, ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Gauge32, iso, ModuleIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Counter64", "enterprises", "NotificationType", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Gauge32", "iso", "ModuleIdentity", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
nwTrend = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 26))
nwtControl = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 26, 1))
nwtTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 26, 2))
class NWTime(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Seconds(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

nwtControlTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1), )
if mibBuilder.loadTexts: nwtControlTable.setStatus('mandatory')
nwtControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1), ).setIndexNames((0, "NetWare-Server-Trend-MIB", "nwtControlAttributeClass"), (0, "NetWare-Server-Trend-MIB", "nwtControlIndex"))
if mibBuilder.loadTexts: nwtControlEntry.setStatus('mandatory')
nwtControlAttributeClass = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))).clone(namedValues=NamedValues(("avgLoggedInUsers", 1), ("avgConnections", 2), ("fileReads", 3), ("fileWrites", 4), ("fileReadKBytes", 5), ("fileWriteKBytes", 6), ("lslInPackets", 7), ("lslOutPackets", 8), ("ncpRequests", 9), ("pctCpuUtilization", 10), ("pctCacheBuffers", 11), ("pctCodeAndDataMemory", 12), ("pctAllocatedMemory", 13), ("pctDirtyPacketReceiveBuffers", 14), ("physIfInPackets", 15), ("physIfOutPackets", 16), ("physIfInKBytes", 17), ("physIfOutKBytes", 18), ("queueAvgNumReadyJobs", 19), ("queueAvgNumReadyKBytes", 20), ("queueAvgNextJobWaitTime", 21), ("volumePctFreeSpace", 22), ("pctCacheHitRate", 23), ("diskPctFreeRedirectionArea", 24), ("serverProcesses", 25), ("noECBCount", 26), ("osPktRcvBuffer", 27)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlAttributeClass.setStatus('mandatory')
nwtControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlIndex.setStatus('mandatory')
nwtControlAttributeInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 3), InternationalDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlAttributeInstance.setStatus('mandatory')
nwtControlSampleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("fiveSeconds", 1), ("tenSeconds", 2), ("fifteenSeconds", 3), ("thirtySeconds", 4), ("oneMinute", 5), ("fiveMinutes", 6), ("fifteenMinutes", 7), ("thirtyMinutes", 8), ("oneHour", 9), ("fourHours", 10), ("eightHours", 11), ("oneDay", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwtControlSampleInterval.setStatus('mandatory')
nwtControlSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("averageValue", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlSampleType.setStatus('mandatory')
nwtControlSampleInvalidValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlSampleInvalidValue.setStatus('mandatory')
nwtControlLastSampleValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlLastSampleValue.setStatus('mandatory')
nwtControlReferenceTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 8), NWTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlReferenceTimeStamp.setStatus('mandatory')
nwtControlThresholdState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwtControlThresholdState.setStatus('mandatory')
nwtControlThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlThresholdType.setStatus('mandatory')
nwtControlRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwtControlRisingThreshold.setStatus('mandatory')
nwtControlFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwtControlFallingThreshold.setStatus('mandatory')
nwtControlHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwtControlHistoryState.setStatus('mandatory')
nwtControlHistoryLastSampleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlHistoryLastSampleIndex.setStatus('mandatory')
nwtControlHistoryBucketsRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwtControlHistoryBucketsRequested.setStatus('mandatory')
nwtControlHistoryBucketsGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlHistoryBucketsGranted.setStatus('mandatory')
nwtControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtControlStatus.setStatus('mandatory')
nwtHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2), )
if mibBuilder.loadTexts: nwtHistoryTable.setStatus('mandatory')
nwtHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1), ).setIndexNames((0, "NetWare-Server-Trend-MIB", "nwtHistoryControlIndex"), (0, "NetWare-Server-Trend-MIB", "nwtHistorySampleIndex"))
if mibBuilder.loadTexts: nwtHistoryEntry.setStatus('mandatory')
nwtHistoryControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtHistoryControlIndex.setStatus('mandatory')
nwtHistorySampleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtHistorySampleIndex.setStatus('mandatory')
nwtHistorySampleValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nwtHistorySampleValue.setStatus('mandatory')
nwtServerName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 1), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48)))
if mibBuilder.loadTexts: nwtServerName.setStatus('mandatory')
nwtTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 2), NWTime())
if mibBuilder.loadTexts: nwtTrapTime.setStatus('mandatory')
nwtThreshold = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 3), Integer32())
if mibBuilder.loadTexts: nwtThreshold.setStatus('mandatory')
nwtInterval = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 4), Seconds())
if mibBuilder.loadTexts: nwtInterval.setStatus('mandatory')
nwtInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 5), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: nwtInterfaceName.setStatus('mandatory')
nwtQueueName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 6), InternationalDisplayString())
if mibBuilder.loadTexts: nwtQueueName.setStatus('mandatory')
nwtVolumeName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 7), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: nwtVolumeName.setStatus('mandatory')
nwtDiskName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 8), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: nwtDiskName.setStatus('mandatory')
nwtCPUDescription = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 9), InternationalDisplayString())
if mibBuilder.loadTexts: nwtCPUDescription.setStatus('mandatory')
nwtThresholdLoggedInUsers = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,1)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdConnections = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,2)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdFileReads = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,3)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdFileWrites = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,4)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdFileReadKBytes = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,5)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdFileWriteKBytes = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,6)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdLslInPackets = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,7)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdLslOutPackets = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,8)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdNcpRequests = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,9)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdPctCpuUtilization = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,10)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"), ("NetWare-Server-Trend-MIB", "nwtCPUDescription"))
nwtThresholdPctCacheBuffers = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,11)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"))
nwtThresholdCodeAndDataMemory = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,12)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"))
nwtThresholdAllocatedMemory = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,13)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"))
nwtThresholdPctDirtyCacheBuffers = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,14)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdPhysIfInPackets = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,15)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"), ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
nwtThresholdPhysIfOutPackets = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,16)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"), ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
nwtThresholdPhysIfInKBytes = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,17)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"), ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
nwtThresholdPhysIfOutKBytes = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,18)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"), ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
nwtThresholdQueueNumReadyJobs = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,19)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtQueueName"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdQueueNumReadyKBytes = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,20)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtQueueName"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdQueueNextJobWaitTime = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,21)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtQueueName"))
nwtThresholdVolumePctFreeSpace = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,22)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtVolumeName"))
nwtThresholdPctCacheHitRate = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,23)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"))
nwtThresholdDiskPctFreeRedirectionArea = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,24)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtDiskName"))
nwtThresholdServerProcesses = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,25)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"))
nwtThresholdNoECBCount = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,26)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"), ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
nwtThresholdOsPktRcvBuffer = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 26) + (0,27)).setObjects(("NetWare-Server-Trend-MIB", "nwtServerName"), ("NetWare-Server-Trend-MIB", "nwtTrapTime"), ("NetWare-Server-Trend-MIB", "nwtThreshold"), ("NetWare-Server-Trend-MIB", "nwtInterval"), ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
mibBuilder.exportSymbols("NetWare-Server-Trend-MIB", nwtThresholdPctCacheBuffers=nwtThresholdPctCacheBuffers, nwtThresholdPhysIfOutPackets=nwtThresholdPhysIfOutPackets, nwtTrapTime=nwtTrapTime, nwtHistorySampleIndex=nwtHistorySampleIndex, nwtThresholdNcpRequests=nwtThresholdNcpRequests, nwTrend=nwTrend, nwtInterval=nwtInterval, nwtControlThresholdState=nwtControlThresholdState, nwtVolumeName=nwtVolumeName, nwtThresholdPctCacheHitRate=nwtThresholdPctCacheHitRate, nwtControlReferenceTimeStamp=nwtControlReferenceTimeStamp, nwtControlThresholdType=nwtControlThresholdType, nwtCPUDescription=nwtCPUDescription, novell=novell, nwtThresholdCodeAndDataMemory=nwtThresholdCodeAndDataMemory, nwtThresholdLslInPackets=nwtThresholdLslInPackets, nwtThresholdPctDirtyCacheBuffers=nwtThresholdPctDirtyCacheBuffers, nwtControlRisingThreshold=nwtControlRisingThreshold, nwtThresholdPhysIfInPackets=nwtThresholdPhysIfInPackets, nwtControlSampleInvalidValue=nwtControlSampleInvalidValue, nwtControlAttributeInstance=nwtControlAttributeInstance, nwtControlLastSampleValue=nwtControlLastSampleValue, nwtThresholdQueueNextJobWaitTime=nwtThresholdQueueNextJobWaitTime, nwtThresholdServerProcesses=nwtThresholdServerProcesses, nwtThresholdNoECBCount=nwtThresholdNoECBCount, nwtControlHistoryBucketsGranted=nwtControlHistoryBucketsGranted, nwtThresholdPctCpuUtilization=nwtThresholdPctCpuUtilization, nwtThresholdAllocatedMemory=nwtThresholdAllocatedMemory, nwtThresholdOsPktRcvBuffer=nwtThresholdOsPktRcvBuffer, nwtControlHistoryBucketsRequested=nwtControlHistoryBucketsRequested, nwtInterfaceName=nwtInterfaceName, nwtControlSampleType=nwtControlSampleType, nwtThresholdFileWriteKBytes=nwtThresholdFileWriteKBytes, nwtThresholdQueueNumReadyJobs=nwtThresholdQueueNumReadyJobs, nwtControlHistoryLastSampleIndex=nwtControlHistoryLastSampleIndex, nwtHistoryTable=nwtHistoryTable, nwtServerName=nwtServerName, nwtThresholdLslOutPackets=nwtThresholdLslOutPackets, nwtThresholdVolumePctFreeSpace=nwtThresholdVolumePctFreeSpace, nwtControl=nwtControl, mibDoc=mibDoc, nwtThresholdConnections=nwtThresholdConnections, nwtThreshold=nwtThreshold, nwtDiskName=nwtDiskName, nwtHistorySampleValue=nwtHistorySampleValue, nwtThresholdFileWrites=nwtThresholdFileWrites, NWTime=NWTime, nwtControlTable=nwtControlTable, nwtControlSampleInterval=nwtControlSampleInterval, nwtThresholdDiskPctFreeRedirectionArea=nwtThresholdDiskPctFreeRedirectionArea, nwtThresholdPhysIfOutKBytes=nwtThresholdPhysIfOutKBytes, nwtControlIndex=nwtControlIndex, nwtControlFallingThreshold=nwtControlFallingThreshold, nwtQueueName=nwtQueueName, nwtHistoryControlIndex=nwtHistoryControlIndex, nwtControlAttributeClass=nwtControlAttributeClass, nwtThresholdPhysIfInKBytes=nwtThresholdPhysIfInKBytes, Seconds=Seconds, nwtControlEntry=nwtControlEntry, nwtControlStatus=nwtControlStatus, nwtHistoryEntry=nwtHistoryEntry, nwtTrapInfo=nwtTrapInfo, nwtThresholdFileReads=nwtThresholdFileReads, nwtThresholdFileReadKBytes=nwtThresholdFileReadKBytes, nwtThresholdQueueNumReadyKBytes=nwtThresholdQueueNumReadyKBytes, nwtThresholdLoggedInUsers=nwtThresholdLoggedInUsers, nwtControlHistoryState=nwtControlHistoryState)
