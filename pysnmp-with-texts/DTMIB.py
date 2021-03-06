#
# PySNMP MIB module DTMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DTMIB
# Produced by pysmi-0.3.4 at Wed May  1 12:54:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, NotificationType, Gauge32, NotificationType, iso, Counter64, enterprises, Bits, IpAddress, Counter32, TimeTicks, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "NotificationType", "Gauge32", "NotificationType", "iso", "Counter64", "enterprises", "Bits", "IpAddress", "Counter32", "TimeTicks", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nsi = MibIdentifier((1, 3, 6, 1, 4, 1, 2592))
nsiDoubleTake = MibIdentifier((1, 3, 6, 1, 4, 1, 2592, 3))
dtTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2592, 3, 1))
dtGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2592, 3, 2))
dtSource = MibIdentifier((1, 3, 6, 1, 4, 1, 2592, 3, 3))
dtTarget = MibIdentifier((1, 3, 6, 1, 4, 1, 2592, 3, 4))
dtSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 2592, 3, 5))
dtConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 2592, 3, 6))
dtUpTime = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: dtUpTime.setDescription('Time (in seconds) since Double-Take was last started.')
dtCurrentMemoryUsage = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtCurrentMemoryUsage.setStatus('mandatory')
if mibBuilder.loadTexts: dtCurrentMemoryUsage.setDescription('Current amount of memory allocated (in bytes) from the Double-Take memory pool.')
dtMirOpsGenerated = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtMirOpsGenerated.setStatus('mandatory')
if mibBuilder.loadTexts: dtMirOpsGenerated.setDescription('Number of mirror ops generated by the mirror driver.')
dtMirBytesGenerated = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtMirBytesGenerated.setStatus('mandatory')
if mibBuilder.loadTexts: dtMirBytesGenerated.setDescription('Total bytes mirrored by the mirror driver.')
dtRepOpsGenerated = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtRepOpsGenerated.setStatus('mandatory')
if mibBuilder.loadTexts: dtRepOpsGenerated.setDescription('Number of ops generated by the file system driver.')
dtRepBytesGenerated = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtRepBytesGenerated.setStatus('mandatory')
if mibBuilder.loadTexts: dtRepBytesGenerated.setDescription('Total bytes generated by the file system driver.')
dtSourceState = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notLoaded", 0), ("loadedNoDriver", 1), ("loadedWithDriver", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtSourceState.setStatus('mandatory')
if mibBuilder.loadTexts: dtSourceState.setDescription('0:Source not running, 1:Source running no driver, 2:Source running with driver')
dtTargetState = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notLoaded", 0), ("loaded", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtTargetState.setStatus('mandatory')
if mibBuilder.loadTexts: dtTargetState.setDescription('0:Target not running, 1:Target running')
dtRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtRetryCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtRetryCount.setDescription('Number of file operations that have been retried.')
dtOpsDroppedCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtOpsDroppedCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtOpsDroppedCount.setDescription('Number of file operations that have failed and will not be retried.')
dtLoginCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtLoginCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtLoginCount.setDescription('Number of successful logins.')
dtFailedLoginCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 5, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtFailedLoginCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtFailedLoginCount.setDescription('Number of un-successful logins.')
dtFailedMirrorCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtFailedMirrorCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtFailedMirrorCount.setDescription("Number of files and Ops that failed to mirror because they couldn't be read on the source.")
dtFailedRepCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtFailedRepCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtFailedRepCount.setDescription("Number of Ops that failed to replicate because they couldn't be read on the source.")
dtActFailCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtActFailCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtActFailCount.setDescription('Number of activation code errors.')
dtAutoDisCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtAutoDisCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtAutoDisCount.setDescription('Number of Auto-Disconnects.')
dtAutoReCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtAutoReCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtAutoReCount.setDescription('Number of Auto-Reconnects.')
dtDriverQueuePercent = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtDriverQueuePercent.setStatus('mandatory')
if mibBuilder.loadTexts: dtDriverQueuePercent.setDescription('Percentage of the driver queue that is currently in use.')
dtConnectionCount = MibScalar((1, 3, 6, 1, 4, 1, 2592, 3, 6, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtConnectionCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtConnectionCount.setDescription('The number of connections currently active.')
dtConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2), )
if mibBuilder.loadTexts: dtConnectionTable.setStatus('mandatory')
if mibBuilder.loadTexts: dtConnectionTable.setDescription('The entries in the table are defined below, one row per connection.')
dtConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1), ).setIndexNames((0, "DTMIB", "dtConnectionIndex"))
if mibBuilder.loadTexts: dtConnectionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dtConnectionEntry.setDescription('An entry in the table dtConnectionTable.')
dtConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dtConnectionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dtConnectionIndex.setDescription('An index to uniquely identify the entry.')
dtconIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dtconIpAddress.setDescription('Address of the machine on the other end of the connection, this is the key column in the table.')
dtconConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconConnectTime.setStatus('mandatory')
if mibBuilder.loadTexts: dtconConnectTime.setDescription('Amount of time (in seconds) connection has been active.')
dtconState = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("conError", 0), ("conActive", 1), ("conPaused", 2), ("conScheduled", 3), ("conNone", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconState.setStatus('mandatory')
if mibBuilder.loadTexts: dtconState.setDescription('Integer coded for the current state of the connection.')
dtconOpsInCmdQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconOpsInCmdQueue.setStatus('mandatory')
if mibBuilder.loadTexts: dtconOpsInCmdQueue.setDescription('The number of ops in the command/retransmit queue.')
dtconOpsInAckQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconOpsInAckQueue.setStatus('mandatory')
if mibBuilder.loadTexts: dtconOpsInAckQueue.setDescription('The number of ops awaiting acknowledgements.')
dtconOpsInRepQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconOpsInRepQueue.setStatus('mandatory')
if mibBuilder.loadTexts: dtconOpsInRepQueue.setDescription('The number of replication ops queued.')
dtconOpsInMirQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconOpsInMirQueue.setStatus('mandatory')
if mibBuilder.loadTexts: dtconOpsInMirQueue.setDescription('The number of mirror ops queued.')
dtconBytesInRepQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconBytesInRepQueue.setStatus('mandatory')
if mibBuilder.loadTexts: dtconBytesInRepQueue.setDescription('The number of bytes of data associated with the queued replication ops.')
dtconBytesInMirQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconBytesInMirQueue.setStatus('mandatory')
if mibBuilder.loadTexts: dtconBytesInMirQueue.setDescription('The number of bytes of data associated with the queued mirror ops.')
dtconOpsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconOpsTx.setStatus('mandatory')
if mibBuilder.loadTexts: dtconOpsTx.setDescription('Total number of ops transmitted.')
dtconBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconBytesTx.setStatus('mandatory')
if mibBuilder.loadTexts: dtconBytesTx.setDescription('Total number of bytes transmitted.')
dtconOpsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconOpsRx.setStatus('mandatory')
if mibBuilder.loadTexts: dtconOpsRx.setDescription('Total number of ops received.')
dtconBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconBytesRx.setStatus('mandatory')
if mibBuilder.loadTexts: dtconBytesRx.setDescription('Total number of bytes received.')
dtconResentOpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2592, 3, 6, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtconResentOpCount.setStatus('mandatory')
if mibBuilder.loadTexts: dtconResentOpCount.setDescription('Number of Ops that were resent because of ack errors.')
dttrapKernelStarted = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,1))
if mibBuilder.loadTexts: dttrapKernelStarted.setDescription('The Double-Take kernel has started.')
dttrapKernelStopped = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,2))
if mibBuilder.loadTexts: dttrapKernelStopped.setDescription('The Double-Take kernel has stopped.')
dttrapLicenseViolationStartingSource = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,3))
if mibBuilder.loadTexts: dttrapLicenseViolationStartingSource.setDescription('Double-Take source or target cannot be started due to a license violation.')
dttrapLicenseViolationOnNetwork = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,4))
if mibBuilder.loadTexts: dttrapLicenseViolationOnNetwork.setDescription('A Double-Take serial number conflict was identified on the network.')
dttrapSourceStarted = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,5))
if mibBuilder.loadTexts: dttrapSourceStarted.setDescription('The Double-Take source module has started.')
dttrapSourceStopped = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,6))
if mibBuilder.loadTexts: dttrapSourceStopped.setDescription('The Double-Take source module has stopped.')
dttrapTargetStarted = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,7))
if mibBuilder.loadTexts: dttrapTargetStarted.setDescription('The Double-Take target module has started.')
dttrapTargetStopped = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,8))
if mibBuilder.loadTexts: dttrapTargetStopped.setDescription('The Double-Take target module is stopped.')
dttrapConnectionRequested = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,9))
if mibBuilder.loadTexts: dttrapConnectionRequested.setDescription('A NetOriginator has attempted to connect to a NetResponder normally.')
dttrapConnectionRequestReceived = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,10))
if mibBuilder.loadTexts: dttrapConnectionRequestReceived.setDescription('A NetController received a request to start a new connection.')
dttrapConnectionSucceded = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,11))
if mibBuilder.loadTexts: dttrapConnectionSucceded.setDescription('A NetOriginator successfully achieved a connection.')
dttrapConnectionPause = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,12))
if mibBuilder.loadTexts: dttrapConnectionPause.setDescription('A Transmission was paused.')
dttrapConnectionResume = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,13))
if mibBuilder.loadTexts: dttrapConnectionResume.setDescription('A Transmission was resumed.')
dttrapConnectionFailed = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,14))
if mibBuilder.loadTexts: dttrapConnectionFailed.setDescription('A NetOriginator was not successful in achieving a connection.')
dttrapConnectionLost = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,15))
if mibBuilder.loadTexts: dttrapConnectionLost.setDescription('A connection was lost by the NetOriginator or NetResponder.')
dttrapMemoryLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,16))
if mibBuilder.loadTexts: dttrapMemoryLimitReached.setDescription('The Double-Take memory pool limit was exceeded.')
dttrapMemoryLimitRemedied = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,17))
if mibBuilder.loadTexts: dttrapMemoryLimitRemedied.setDescription('Memory has been freed to bring the Double-Take memory pool usage below the limit.')
dttrapAutoReconnect = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,18))
if mibBuilder.loadTexts: dttrapAutoReconnect.setDescription('Auto reconnect needs to make a new connection.')
dttrapScheduledConnectStart = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,19))
if mibBuilder.loadTexts: dttrapScheduledConnectStart.setDescription('Start of a scheduled connect period.')
dttrapScheduledConnectEnd = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,20))
if mibBuilder.loadTexts: dttrapScheduledConnectEnd.setDescription('End of a scheduled connect period.')
dttrapAutoDisconnectWriteQueue = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,21))
if mibBuilder.loadTexts: dttrapAutoDisconnectWriteQueue.setDescription('Auto disconnect forced a queue to be written to disk.')
dttrapAutoDisconnectPauseTransmission = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,22))
if mibBuilder.loadTexts: dttrapAutoDisconnectPauseTransmission.setDescription('Auto disconnect requested a source to pause sending ops.')
dttrapAutoDisconnectEndConnection = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,23))
if mibBuilder.loadTexts: dttrapAutoDisconnectEndConnection.setDescription('Auto disconnect dropped a connection.')
dttrapAutoDisconnectShutdown = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,24))
if mibBuilder.loadTexts: dttrapAutoDisconnectShutdown.setDescription('Auto disconnect was forced to shut down Double-Take.')
dttrapReplicationStart = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,25))
if mibBuilder.loadTexts: dttrapReplicationStart.setDescription('Replication was started on a connection.')
dttrapReplicationStop = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,26))
if mibBuilder.loadTexts: dttrapReplicationStop.setDescription('Replication was stopped on a connection.')
dttrapMirrorStart = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,27))
if mibBuilder.loadTexts: dttrapMirrorStart.setDescription('Mirroring was started on a connection.')
dttrapMirrorStop = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,28))
if mibBuilder.loadTexts: dttrapMirrorStop.setDescription('Mirroring was stopped on a connection.')
dttrapMirrorPause = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,29))
if mibBuilder.loadTexts: dttrapMirrorPause.setDescription('Mirroring was paused on a connection.')
dttrapMirrorResume = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,30))
if mibBuilder.loadTexts: dttrapMirrorResume.setDescription('Mirroring was resumed on a connection.')
dttrapMirrorEnd = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,31))
if mibBuilder.loadTexts: dttrapMirrorEnd.setDescription('Mirroring has ended on a connection.')
dttrapVerificationStart = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,32))
if mibBuilder.loadTexts: dttrapVerificationStart.setDescription('Verification was started.')
dttrapVerificationEnd = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,33))
if mibBuilder.loadTexts: dttrapVerificationEnd.setDescription('Verification is finished.')
dttrapVerficationFailure = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,34))
if mibBuilder.loadTexts: dttrapVerficationFailure.setDescription('Verification found the source and target out of sync.')
dttrapRestoreStarted = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,35))
if mibBuilder.loadTexts: dttrapRestoreStarted.setDescription('Restoration has begun.')
dttrapRestoreComplete = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,36))
if mibBuilder.loadTexts: dttrapRestoreComplete.setDescription('Restoration has finished.')
dttrapRepSetModified = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,37))
if mibBuilder.loadTexts: dttrapRepSetModified.setDescription('The replication set was modified.')
dttrapFailoverConditionMet = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,38))
if mibBuilder.loadTexts: dttrapFailoverConditionMet.setDescription('A Failover Condition has been met. User intervention is necessary!')
dttrapFailoverInProgress = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,39))
if mibBuilder.loadTexts: dttrapFailoverInProgress.setDescription('Failover is in progress!')
dttrapTargetFull = NotificationType((1, 3, 6, 1, 4, 1, 2592) + (0,40))
if mibBuilder.loadTexts: dttrapTargetFull.setDescription('Target is full.')
mibBuilder.exportSymbols("DTMIB", dttrapKernelStarted=dttrapKernelStarted, dttrapMirrorResume=dttrapMirrorResume, dttrapMirrorStop=dttrapMirrorStop, dtConnectionIndex=dtConnectionIndex, dtRepOpsGenerated=dtRepOpsGenerated, dttrapAutoDisconnectWriteQueue=dttrapAutoDisconnectWriteQueue, dtLoginCount=dtLoginCount, dttrapScheduledConnectStart=dttrapScheduledConnectStart, dttrapVerificationEnd=dttrapVerificationEnd, dttrapMirrorEnd=dttrapMirrorEnd, dtSecurity=dtSecurity, dtConnection=dtConnection, dttrapConnectionRequested=dttrapConnectionRequested, dttrapMemoryLimitReached=dttrapMemoryLimitReached, dttrapRestoreStarted=dttrapRestoreStarted, dttrapSourceStarted=dttrapSourceStarted, dtconState=dtconState, dtDriverQueuePercent=dtDriverQueuePercent, dttrapConnectionRequestReceived=dttrapConnectionRequestReceived, dtconOpsInMirQueue=dtconOpsInMirQueue, nsiDoubleTake=nsiDoubleTake, dttrapTargetFull=dttrapTargetFull, dttrapTargetStarted=dttrapTargetStarted, dttrapFailoverConditionMet=dttrapFailoverConditionMet, dttrapMemoryLimitRemedied=dttrapMemoryLimitRemedied, dttrapRepSetModified=dttrapRepSetModified, dtAutoReCount=dtAutoReCount, dttrapScheduledConnectEnd=dttrapScheduledConnectEnd, dttrapLicenseViolationStartingSource=dttrapLicenseViolationStartingSource, dttrapTargetStopped=dttrapTargetStopped, dtFailedRepCount=dtFailedRepCount, dttrapAutoDisconnectShutdown=dttrapAutoDisconnectShutdown, dtOpsDroppedCount=dtOpsDroppedCount, dttrapConnectionSucceded=dttrapConnectionSucceded, dttrapMirrorStart=dttrapMirrorStart, dtFailedMirrorCount=dtFailedMirrorCount, dtTargetState=dtTargetState, dttrapReplicationStop=dttrapReplicationStop, dtconResentOpCount=dtconResentOpCount, dtTarget=dtTarget, dtRepBytesGenerated=dtRepBytesGenerated, dtconBytesInRepQueue=dtconBytesInRepQueue, dtMirOpsGenerated=dtMirOpsGenerated, dtconOpsRx=dtconOpsRx, dtGeneral=dtGeneral, dtFailedLoginCount=dtFailedLoginCount, dttrapFailoverInProgress=dttrapFailoverInProgress, dtconOpsInCmdQueue=dtconOpsInCmdQueue, dttrapConnectionFailed=dttrapConnectionFailed, dtRetryCount=dtRetryCount, dtconOpsTx=dtconOpsTx, dtconBytesTx=dtconBytesTx, dttrapReplicationStart=dttrapReplicationStart, dttrapKernelStopped=dttrapKernelStopped, dtAutoDisCount=dtAutoDisCount, dttrapConnectionLost=dttrapConnectionLost, dtconOpsInRepQueue=dtconOpsInRepQueue, dttrapConnectionPause=dttrapConnectionPause, dtConnectionCount=dtConnectionCount, dtSource=dtSource, dttrapRestoreComplete=dttrapRestoreComplete, dtconIpAddress=dtconIpAddress, dttrapAutoDisconnectPauseTransmission=dttrapAutoDisconnectPauseTransmission, dtconBytesRx=dtconBytesRx, dtMirBytesGenerated=dtMirBytesGenerated, dtConnectionTable=dtConnectionTable, dtconConnectTime=dtconConnectTime, dtActFailCount=dtActFailCount, nsi=nsi, dtTraps=dtTraps, dtCurrentMemoryUsage=dtCurrentMemoryUsage, dtSourceState=dtSourceState, dttrapMirrorPause=dttrapMirrorPause, dttrapVerficationFailure=dttrapVerficationFailure, dttrapLicenseViolationOnNetwork=dttrapLicenseViolationOnNetwork, dtConnectionEntry=dtConnectionEntry, dttrapSourceStopped=dttrapSourceStopped, dtconBytesInMirQueue=dtconBytesInMirQueue, dttrapAutoReconnect=dttrapAutoReconnect, dtconOpsInAckQueue=dtconOpsInAckQueue, dttrapConnectionResume=dttrapConnectionResume, dtUpTime=dtUpTime, dttrapAutoDisconnectEndConnection=dttrapAutoDisconnectEndConnection, dttrapVerificationStart=dttrapVerificationStart)
