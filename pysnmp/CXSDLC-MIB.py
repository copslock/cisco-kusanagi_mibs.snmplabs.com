#
# PySNMP MIB module CXSDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXSDLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
Alias, cxSDLC, SapIndex = mibBuilder.importSymbols("CXProduct-SMI", "Alias", "cxSDLC", "SapIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Counter64, Unsigned32, IpAddress, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Bits, NotificationType, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter64", "Unsigned32", "IpAddress", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Bits", "NotificationType", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class CuAddress(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 254)

sdlcSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1), )
if mibBuilder.loadTexts: sdlcSapTable.setStatus('mandatory')
sdlcSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1), ).setIndexNames((0, "CXSDLC-MIB", "sdlcSapNumber"))
if mibBuilder.loadTexts: sdlcSapEntry.setStatus('mandatory')
sdlcSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapNumber.setStatus('mandatory')
sdlcSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapRowStatus.setStatus('mandatory')
sdlcSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lower", 1), ("upper", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapType.setStatus('mandatory')
sdlcSapCuType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("terminalInterfaceUnit", 1), ("hostInterfaceUnit", 2))).clone('terminalInterfaceUnit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapCuType.setStatus('mandatory')
sdlcSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 5), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapAlias.setStatus('mandatory')
sdlcSapCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 6), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapCompanionAlias.setStatus('mandatory')
sdlcSapSnalcRef = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapSnalcRef.setStatus('mandatory')
sdlcSapDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fullduplex", 1), ("halfduplex", 2))).clone('fullduplex')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapDuplex.setStatus('mandatory')
sdlcSapRaiseDtrOnConnectReq = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapRaiseDtrOnConnectReq.setStatus('mandatory')
sdlcPollIntAfterAckTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcPollIntAfterAckTimer.setStatus('mandatory')
sdlcSapLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standard", 1), ("negotiable", 2), ("switched", 3), ("switched-negotiable", 4))).clone('negotiable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcSapLineType.setStatus('mandatory')
sdlcSapControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: sdlcSapControl.setStatus('mandatory')
sdlcSapOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("offline", 1), ("online", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapOperationalMode.setStatus('mandatory')
sdlcSapLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapLinkStatus.setStatus('mandatory')
sdlcSapLinkChange = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapLinkChange.setStatus('mandatory')
sdlcSapTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapTxDataFrames.setStatus('mandatory')
sdlcSapRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapRxDataFrames.setStatus('mandatory')
sdlcSapConnectRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapConnectRequest.setStatus('mandatory')
sdlcSapDisconnectRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapDisconnectRequest.setStatus('mandatory')
sdlcSapDisconnectIndication = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcSapDisconnectIndication.setStatus('mandatory')
sdlcCuTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2), )
if mibBuilder.loadTexts: sdlcCuTable.setStatus('mandatory')
sdlcCuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1), ).setIndexNames((0, "CXSDLC-MIB", "sdlcCuSap"), (0, "CXSDLC-MIB", "sdlcCuId"))
if mibBuilder.loadTexts: sdlcCuEntry.setStatus('mandatory')
sdlcCuSap = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuSap.setStatus('mandatory')
sdlcCuId = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 2), CuAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuId.setStatus('mandatory')
sdlcCuRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuRowStatus.setStatus('mandatory')
sdlcCuMaxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(521)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuMaxFrameLength.setStatus('mandatory')
sdlcCuTransmitWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuTransmitWindow.setStatus('mandatory')
sdlcCuPollRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuPollRetry.setStatus('mandatory')
sdlcCuMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuMaxRetry.setStatus('mandatory')
sdlcCuWaitForNextSnrmOrXid = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuWaitForNextSnrmOrXid.setStatus('mandatory')
sdlcCuSendDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('yes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuSendDisconnect.setStatus('mandatory')
sdlcCuPollAckTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 10), TimeTicks().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuPollAckTimer.setStatus('mandatory')
sdlcCuSlowPollTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 11), TimeTicks().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuSlowPollTimer.setStatus('mandatory')
sdlcCuWaitForUaFromSnalcTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 13), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sdlcCuWaitForUaFromSnalcTimer.setStatus('mandatory')
sdlcCuControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: sdlcCuControl.setStatus('mandatory')
sdlcCuState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("normalDiscMode", 1), ("waitForSnrm", 2), ("receivedSnrm", 3), ("normalResponseMode", 4), ("waitForDisc", 5), ("receivedDisc", 6), ("snrmSent", 7), ("discSent", 8), ("remoteDiscReceived", 9), ("xidExchange", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuState.setStatus('mandatory')
sdlcCuOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("offline", 1), ("online", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuOperationalMode.setStatus('mandatory')
sdlcCuDiscReasonCode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 42), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuDiscReasonCode.setStatus('mandatory')
sdlcCuSnalcDiscReasonCode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 43), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuSnalcDiscReasonCode.setStatus('mandatory')
sdlcCuConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuConnectionStatus.setStatus('mandatory')
sdlcCuFramesInTransmitQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuFramesInTransmitQueue.setStatus('mandatory')
sdlcCuTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuTxFrames.setStatus('mandatory')
sdlcCuRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuRxFrames.setStatus('mandatory')
sdlcCuTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuTimeOuts.setStatus('mandatory')
sdlcCuSnrmCount = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuSnrmCount.setStatus('mandatory')
sdlcCuXidCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuXidCommand.setStatus('mandatory')
sdlcCuXidResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuXidResponse.setStatus('mandatory')
sdlcCuUnnumberedAcks = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuUnnumberedAcks.setStatus('mandatory')
sdlcCuRetransmission = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuRetransmission.setStatus('mandatory')
sdlcCuDisconnectCount = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuDisconnectCount.setStatus('mandatory')
sdlcCuDisconnectModeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuDisconnectModeCount.setStatus('mandatory')
sdlcCuTransmittedRNR = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuTransmittedRNR.setStatus('mandatory')
sdlcCuReceivedRNR = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuReceivedRNR.setStatus('mandatory')
sdlcCuFrameRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuFrameRejects.setStatus('mandatory')
sdlcCuRemoteDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuRemoteDisc.setStatus('mandatory')
sdlcCuConnectionRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 67), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuConnectionRequest.setStatus('mandatory')
sdlcCuDisconnectionRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 68), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuDisconnectionRequest.setStatus('mandatory')
sdlcCuDisconnectionIndication = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 69), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdlcCuDisconnectionIndication.setStatus('mandatory')
mibBuilder.exportSymbols("CXSDLC-MIB", sdlcCuRowStatus=sdlcCuRowStatus, sdlcCuDisconnectionRequest=sdlcCuDisconnectionRequest, sdlcSapLinkStatus=sdlcSapLinkStatus, sdlcSapTable=sdlcSapTable, sdlcSapOperationalMode=sdlcSapOperationalMode, sdlcCuConnectionRequest=sdlcCuConnectionRequest, sdlcCuDisconnectModeCount=sdlcCuDisconnectModeCount, sdlcCuDisconnectionIndication=sdlcCuDisconnectionIndication, sdlcCuSnalcDiscReasonCode=sdlcCuSnalcDiscReasonCode, sdlcCuRemoteDisc=sdlcCuRemoteDisc, sdlcSapLinkChange=sdlcSapLinkChange, sdlcCuFrameRejects=sdlcCuFrameRejects, CuAddress=CuAddress, sdlcCuTransmitWindow=sdlcCuTransmitWindow, sdlcSapSnalcRef=sdlcSapSnalcRef, sdlcCuTransmittedRNR=sdlcCuTransmittedRNR, sdlcCuMaxRetry=sdlcCuMaxRetry, sdlcPollIntAfterAckTimer=sdlcPollIntAfterAckTimer, sdlcSapDisconnectRequest=sdlcSapDisconnectRequest, sdlcSapCuType=sdlcSapCuType, sdlcCuEntry=sdlcCuEntry, sdlcSapAlias=sdlcSapAlias, sdlcSapRaiseDtrOnConnectReq=sdlcSapRaiseDtrOnConnectReq, sdlcCuSlowPollTimer=sdlcCuSlowPollTimer, sdlcCuId=sdlcCuId, sdlcCuControl=sdlcCuControl, sdlcCuRetransmission=sdlcCuRetransmission, sdlcSapLineType=sdlcSapLineType, sdlcCuPollRetry=sdlcCuPollRetry, sdlcCuFramesInTransmitQueue=sdlcCuFramesInTransmitQueue, sdlcSapType=sdlcSapType, sdlcSapRowStatus=sdlcSapRowStatus, sdlcCuXidResponse=sdlcCuXidResponse, sdlcCuWaitForNextSnrmOrXid=sdlcCuWaitForNextSnrmOrXid, sdlcCuDiscReasonCode=sdlcCuDiscReasonCode, sdlcCuDisconnectCount=sdlcCuDisconnectCount, sdlcSapControl=sdlcSapControl, sdlcCuWaitForUaFromSnalcTimer=sdlcCuWaitForUaFromSnalcTimer, sdlcSapNumber=sdlcSapNumber, sdlcCuState=sdlcCuState, sdlcCuPollAckTimer=sdlcCuPollAckTimer, sdlcCuRxFrames=sdlcCuRxFrames, sdlcCuSap=sdlcCuSap, sdlcCuTxFrames=sdlcCuTxFrames, sdlcCuUnnumberedAcks=sdlcCuUnnumberedAcks, sdlcCuSendDisconnect=sdlcCuSendDisconnect, sdlcSapDuplex=sdlcSapDuplex, sdlcSapTxDataFrames=sdlcSapTxDataFrames, sdlcSapCompanionAlias=sdlcSapCompanionAlias, sdlcSapConnectRequest=sdlcSapConnectRequest, sdlcCuTable=sdlcCuTable, sdlcSapDisconnectIndication=sdlcSapDisconnectIndication, sdlcCuConnectionStatus=sdlcCuConnectionStatus, sdlcCuTimeOuts=sdlcCuTimeOuts, sdlcCuSnrmCount=sdlcCuSnrmCount, sdlcCuReceivedRNR=sdlcCuReceivedRNR, sdlcSapRxDataFrames=sdlcSapRxDataFrames, sdlcCuOperationalMode=sdlcCuOperationalMode, sdlcCuXidCommand=sdlcCuXidCommand, sdlcCuMaxFrameLength=sdlcCuMaxFrameLength, sdlcSapEntry=sdlcSapEntry)