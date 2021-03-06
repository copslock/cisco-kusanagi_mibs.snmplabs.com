#
# PySNMP MIB module CXAsync-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXAsync-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
Alias, SapIndex, cxAsync, ThruputClass = mibBuilder.importSymbols("CXProduct-SMI", "Alias", "SapIndex", "cxAsync", "ThruputClass")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, NotificationType, TimeTicks, Counter32, NotificationType, ModuleIdentity, MibIdentifier, ObjectIdentity, Unsigned32, Bits, IpAddress, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "NotificationType", "TimeTicks", "Counter32", "NotificationType", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PacketSize(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("bytes16", 4), ("bytes32", 5), ("bytes64", 6), ("bytes128", 7), ("bytes256", 8), ("bytes512", 9), ("bytes1024", 10), ("bytes2048", 11), ("bytes4096", 12))

class YesNo(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("no", 1), ("yes", 2))

class ProfIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class DteIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

asyX25TxQThreshold = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyX25TxQThreshold.setStatus('mandatory')
asyPadIdBanner = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)).clone('Async PAD')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyPadIdBanner.setStatus('mandatory')
asyAlarms = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enable", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyAlarms.setStatus('mandatory')
asySapStatusEvent = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("noEvent", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapStatusEvent.setStatus('mandatory')
asySoftwareVersions = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySoftwareVersions.setStatus('mandatory')
asyMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asyMibLevel.setStatus('mandatory')
asySapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20), )
if mibBuilder.loadTexts: asySapTable.setStatus('mandatory')
asySapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1), ).setIndexNames((0, "CXAsync-MIB", "asySapNumber"))
if mibBuilder.loadTexts: asySapEntry.setStatus('mandatory')
asySapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapNumber.setStatus('mandatory')
asySapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapRowStatus.setStatus('mandatory')
asySapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapAlias.setStatus('mandatory')
asySapMCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 4), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapMCompanionAlias.setStatus('mandatory')
asySapNCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 5), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapNCompanionAlias.setStatus('mandatory')
asySapX3Profile = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(92)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapX3Profile.setStatus('mandatory')
asySapNUI = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapNUI.setStatus('mandatory')
asySapAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapAddress.setStatus('mandatory')
asySapDisconnectRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 9), YesNo().clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapDisconnectRequest.setStatus('mandatory')
asySapRxThruputClass = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 10), ThruputClass().clone('bps9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapRxThruputClass.setStatus('mandatory')
asySapTxThruputClass = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 11), ThruputClass().clone('bps9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapTxThruputClass.setStatus('mandatory')
asySapTxPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 12), PacketSize().clone('bytes128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapTxPacketSize.setStatus('mandatory')
asySapRxPacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 13), PacketSize().clone('bytes128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapRxPacketSize.setStatus('mandatory')
asySapTxWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapTxWindowSize.setStatus('mandatory')
asySapRxWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapRxWindowSize.setStatus('mandatory')
asySapYTTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapYTTimer.setStatus('mandatory')
asySapSRTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapSRTimer.setStatus('mandatory')
asySapNUILength = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapNUILength.setStatus('obsolete')
asySapReverseChargingAcceptance = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 19), YesNo().clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapReverseChargingAcceptance.setStatus('mandatory')
asySapChargingInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 20), YesNo().clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapChargingInformation.setStatus('mandatory')
asySapSubscriptionCUG = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 21), YesNo().clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapSubscriptionCUG.setStatus('mandatory')
asySapSubscriptionCUGOA = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 22), YesNo().clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapSubscriptionCUGOA.setStatus('mandatory')
asySapSubscriptionCUGIA = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 23), YesNo().clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapSubscriptionCUGIA.setStatus('mandatory')
asySapPreferentialCUGIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapPreferentialCUGIndex.setStatus('mandatory')
asySapReceiptConfirmation = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAck", 1), ("dBit", 2), ("localAck", 3), ("xmitAck", 4))).clone('noAck')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapReceiptConfirmation.setStatus('mandatory')
asySapEnableProtocolId = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 26), YesNo().clone('yes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapEnableProtocolId.setStatus('mandatory')
asySapProtocolId = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(7, 11)).clone('01,00,00,00')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProtocolId.setStatus('mandatory')
asySapPromptSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone('*')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapPromptSignal.setStatus('mandatory')
asySapAutoConnectDteId = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 29), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapAutoConnectDteId.setStatus('mandatory')
asySapAutoConnectRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapAutoConnectRetry.setStatus('mandatory')
asySapAutoConnectDelayTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapAutoConnectDelayTimer.setStatus('mandatory')
asySapHardwareFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 32), YesNo().clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapHardwareFlowControl.setStatus('mandatory')
asySapProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("iocProtocol", 2), ("modifiedudf", 3))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProtocolType.setStatus('mandatory')
asySapControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("clearStats", 1), ("enableSap", 2), ("disableSapImmediately", 3), ("disableSapGracefully", 4)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: asySapControl.setStatus('mandatory')
asySapState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disconnected", 1), ("enabled", 2), ("connecting", 3), ("dataTransfer", 4), ("resetting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapState.setStatus('mandatory')
asySapAsyncFlowControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flowControlOff", 1), ("flowControlOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapAsyncFlowControlState.setStatus('mandatory')
asySapNetworkFlowControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flowControlOff", 1), ("flowControlOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapNetworkFlowControlState.setStatus('mandatory')
asySapAsyncTxQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapAsyncTxQueueSize.setStatus('mandatory')
asySapX25TxQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapX25TxQueueSize.setStatus('mandatory')
asySapNumberConnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapNumberConnects.setStatus('mandatory')
asySapNumberDisconnects = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapNumberDisconnects.setStatus('mandatory')
asySapTxDataCharacters = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapTxDataCharacters.setStatus('mandatory')
asySapRxDataCharacters = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapRxDataCharacters.setStatus('mandatory')
asySapParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 54), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapParityErrors.setStatus('mandatory')
asySapOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapOverruns.setStatus('mandatory')
asySapFlowControlByUser = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapFlowControlByUser.setStatus('mandatory')
asySapFlowControlByX25 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapFlowControlByX25.setStatus('mandatory')
asySapFlowControlToUser = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapFlowControlToUser.setStatus('mandatory')
asySapFlowControlToX25 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapFlowControlToX25.setStatus('mandatory')
asySapRxReset = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapRxReset.setStatus('mandatory')
asySapRxBreak = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapRxBreak.setStatus('mandatory')
asySapTxBreak = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapTxBreak.setStatus('mandatory')
asySapRxDiscardCharacters = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 20, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapRxDiscardCharacters.setStatus('mandatory')
asyProfTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21), )
if mibBuilder.loadTexts: asyProfTable.setStatus('mandatory')
asyProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1), ).setIndexNames((0, "CXAsync-MIB", "asyProfNumber"))
if mibBuilder.loadTexts: asyProfEntry.setStatus('mandatory')
asyProfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 1), ProfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asyProfNumber.setStatus('mandatory')
asyProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfRowStatus.setStatus('mandatory')
asyProfAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfAlias.setStatus('mandatory')
asyProfParameter1 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 126))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter1.setStatus('mandatory')
asyProfParameter2 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter2.setStatus('mandatory')
asyProfParameter3 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 126))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter3.setStatus('mandatory')
asyProfParameter4 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter4.setStatus('mandatory')
asyProfParameter5 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter5.setStatus('mandatory')
asyProfParameter6 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter6.setStatus('mandatory')
asyProfParameter7 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 21))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter7.setStatus('mandatory')
asyProfParameter8 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter8.setStatus('mandatory')
asyProfParameter9 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter9.setStatus('mandatory')
asyProfParameter10 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter10.setStatus('mandatory')
asyProfParameter11 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asyProfParameter11.setStatus('mandatory')
asyProfParameter12 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter12.setStatus('mandatory')
asyProfParameter13 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter13.setStatus('mandatory')
asyProfParameter14 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter14.setStatus('mandatory')
asyProfParameter15 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter15.setStatus('mandatory')
asyProfParameter16 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter16.setStatus('mandatory')
asyProfParameter17 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter17.setStatus('mandatory')
asyProfParameter18 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter18.setStatus('mandatory')
asyProfParameter19 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter19.setStatus('mandatory')
asyProfParameter20 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter20.setStatus('mandatory')
asyProfParameter21 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter21.setStatus('mandatory')
asyProfParameter22 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter22.setStatus('mandatory')
asyProfParameter23 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter23.setStatus('mandatory')
asyProfParameter24 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter24.setStatus('mandatory')
asyProfParameter25 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter25.setStatus('mandatory')
asyProfParameter26 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter26.setStatus('mandatory')
asyProfParameter27 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter27.setStatus('mandatory')
asyProfParameter28 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 21, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyProfParameter28.setStatus('mandatory')
asySapProfTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22), )
if mibBuilder.loadTexts: asySapProfTable.setStatus('mandatory')
asySapProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1), ).setIndexNames((0, "CXAsync-MIB", "asySapProfSapNumber"))
if mibBuilder.loadTexts: asySapProfEntry.setStatus('mandatory')
asySapProfSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapProfSapNumber.setStatus('mandatory')
asySapProfParameter1 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 126))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter1.setStatus('mandatory')
asySapProfParameter2 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter2.setStatus('mandatory')
asySapProfParameter3 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 126))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter3.setStatus('mandatory')
asySapProfParameter4 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter4.setStatus('mandatory')
asySapProfParameter5 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter5.setStatus('mandatory')
asySapProfParameter6 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter6.setStatus('mandatory')
asySapProfParameter7 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 21))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter7.setStatus('mandatory')
asySapProfParameter8 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter8.setStatus('mandatory')
asySapProfParameter9 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter9.setStatus('mandatory')
asySapProfParameter10 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter10.setStatus('mandatory')
asySapProfParameter11 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asySapProfParameter11.setStatus('mandatory')
asySapProfParameter12 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter12.setStatus('mandatory')
asySapProfParameter13 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter13.setStatus('mandatory')
asySapProfParameter14 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter14.setStatus('mandatory')
asySapProfParameter15 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter15.setStatus('mandatory')
asySapProfParameter16 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter16.setStatus('mandatory')
asySapProfParameter17 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter17.setStatus('mandatory')
asySapProfParameter18 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter18.setStatus('mandatory')
asySapProfParameter19 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter19.setStatus('mandatory')
asySapProfParameter20 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter20.setStatus('mandatory')
asySapProfParameter21 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter21.setStatus('mandatory')
asySapProfParameter22 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter22.setStatus('mandatory')
asySapProfParameter23 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter23.setStatus('mandatory')
asySapProfParameter24 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter24.setStatus('mandatory')
asySapProfParameter25 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter25.setStatus('mandatory')
asySapProfParameter26 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter26.setStatus('mandatory')
asySapProfParameter27 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter27.setStatus('mandatory')
asySapProfParameter28 = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 22, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asySapProfParameter28.setStatus('mandatory')
asyDteTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23), )
if mibBuilder.loadTexts: asyDteTable.setStatus('mandatory')
asyDteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1), ).setIndexNames((0, "CXAsync-MIB", "asyDteNumber"))
if mibBuilder.loadTexts: asyDteEntry.setStatus('mandatory')
asyDteNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 1), DteIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asyDteNumber.setStatus('mandatory')
asyDteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyDteRowStatus.setStatus('mandatory')
asyDteAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyDteAlias.setStatus('mandatory')
asyDteCalledAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyDteCalledAddress.setStatus('mandatory')
asyDteFacilityField = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyDteFacilityField.setStatus('mandatory')
asyDteUserDataField = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyDteUserDataField.setStatus('mandatory')
asyDteX3Profile = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30, 23, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asyDteX3Profile.setStatus('mandatory')
asySapAlarm = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30) + (0,1)).setObjects(("CXAsync-MIB", "asySapNumber"), ("CXAsync-MIB", "asySapStatusEvent"))
mibBuilder.exportSymbols("CXAsync-MIB", asyProfParameter26=asyProfParameter26, asySapNumberConnects=asySapNumberConnects, asySapAlarm=asySapAlarm, asyProfParameter13=asyProfParameter13, asySapProfParameter8=asySapProfParameter8, asySapFlowControlToUser=asySapFlowControlToUser, asySapParityErrors=asySapParityErrors, asyProfParameter20=asyProfParameter20, asyProfRowStatus=asyProfRowStatus, asyProfParameter14=asyProfParameter14, asyDteEntry=asyDteEntry, asySapX3Profile=asySapX3Profile, asySapSRTimer=asySapSRTimer, asyDteTable=asyDteTable, asySapAlias=asySapAlias, asyProfParameter19=asyProfParameter19, asySapNumberDisconnects=asySapNumberDisconnects, asySapMCompanionAlias=asySapMCompanionAlias, asyProfParameter8=asyProfParameter8, asySapProfTable=asySapProfTable, asySapProfParameter16=asySapProfParameter16, asySapProfParameter20=asySapProfParameter20, asySapNUILength=asySapNUILength, asySapProfParameter18=asySapProfParameter18, asySapSubscriptionCUG=asySapSubscriptionCUG, YesNo=YesNo, asySapTable=asySapTable, asySapSubscriptionCUGOA=asySapSubscriptionCUGOA, asySapStatusEvent=asySapStatusEvent, asySapRxWindowSize=asySapRxWindowSize, asyPadIdBanner=asyPadIdBanner, asyProfParameter15=asyProfParameter15, asySapTxWindowSize=asySapTxWindowSize, asySapProfSapNumber=asySapProfSapNumber, asySapRxDiscardCharacters=asySapRxDiscardCharacters, asyProfEntry=asyProfEntry, asySapAsyncFlowControlState=asySapAsyncFlowControlState, asyAlarms=asyAlarms, asySapFlowControlToX25=asySapFlowControlToX25, asySapTxDataCharacters=asySapTxDataCharacters, asyProfParameter4=asyProfParameter4, asyDteNumber=asyDteNumber, asySapSubscriptionCUGIA=asySapSubscriptionCUGIA, asyProfParameter23=asyProfParameter23, asySapAutoConnectRetry=asySapAutoConnectRetry, asySapProfParameter5=asySapProfParameter5, asyProfParameter3=asyProfParameter3, asySapProfParameter2=asySapProfParameter2, asyDteX3Profile=asyDteX3Profile, asyProfParameter28=asyProfParameter28, asySoftwareVersions=asySoftwareVersions, asySapTxThruputClass=asySapTxThruputClass, asyProfParameter11=asyProfParameter11, asySapProfParameter26=asySapProfParameter26, asySapPromptSignal=asySapPromptSignal, asySapRxBreak=asySapRxBreak, asySapAddress=asySapAddress, asySapHardwareFlowControl=asySapHardwareFlowControl, asySapAutoConnectDelayTimer=asySapAutoConnectDelayTimer, asySapProfParameter10=asySapProfParameter10, asyMibLevel=asyMibLevel, asyProfParameter21=asyProfParameter21, asySapProfParameter24=asySapProfParameter24, asyProfParameter12=asyProfParameter12, asySapFlowControlByUser=asySapFlowControlByUser, asySapRxThruputClass=asySapRxThruputClass, asySapNetworkFlowControlState=asySapNetworkFlowControlState, asyProfParameter25=asyProfParameter25, asyProfParameter9=asyProfParameter9, asySapProfParameter13=asySapProfParameter13, asySapProfParameter22=asySapProfParameter22, asySapProfParameter9=asySapProfParameter9, asySapProfParameter27=asySapProfParameter27, asySapProfParameter7=asySapProfParameter7, asyProfParameter7=asyProfParameter7, asySapFlowControlByX25=asySapFlowControlByX25, asySapDisconnectRequest=asySapDisconnectRequest, asySapProfParameter6=asySapProfParameter6, asySapX25TxQueueSize=asySapX25TxQueueSize, asyProfParameter2=asyProfParameter2, asyProfParameter5=asyProfParameter5, asyProfParameter18=asyProfParameter18, asySapTxBreak=asySapTxBreak, asyProfParameter6=asyProfParameter6, asyDteFacilityField=asyDteFacilityField, asySapControl=asySapControl, asySapYTTimer=asySapYTTimer, asySapProfParameter21=asySapProfParameter21, asyProfAlias=asyProfAlias, asySapNCompanionAlias=asySapNCompanionAlias, asySapReceiptConfirmation=asySapReceiptConfirmation, asyProfParameter24=asyProfParameter24, asyDteRowStatus=asyDteRowStatus, asySapProtocolId=asySapProtocolId, asySapProfParameter17=asySapProfParameter17, asySapEntry=asySapEntry, asyProfNumber=asyProfNumber, asySapRxPacketSize=asySapRxPacketSize, ProfIndex=ProfIndex, asySapAutoConnectDteId=asySapAutoConnectDteId, asyProfParameter10=asyProfParameter10, asySapNUI=asySapNUI, asySapRxReset=asySapRxReset, asySapRxDataCharacters=asySapRxDataCharacters, asySapProfEntry=asySapProfEntry, asySapProfParameter25=asySapProfParameter25, asySapAsyncTxQueueSize=asySapAsyncTxQueueSize, asySapProfParameter4=asySapProfParameter4, asyProfParameter1=asyProfParameter1, asyProfParameter16=asyProfParameter16, asySapProfParameter12=asySapProfParameter12, asySapState=asySapState, asySapPreferentialCUGIndex=asySapPreferentialCUGIndex, asySapReverseChargingAcceptance=asySapReverseChargingAcceptance, asyProfParameter22=asyProfParameter22, asySapOverruns=asySapOverruns, asySapNumber=asySapNumber, asyProfTable=asyProfTable, asyDteAlias=asyDteAlias, asySapRowStatus=asySapRowStatus, asySapProfParameter1=asySapProfParameter1, asySapChargingInformation=asySapChargingInformation, asySapProfParameter11=asySapProfParameter11, asyProfParameter27=asyProfParameter27, asySapEnableProtocolId=asySapEnableProtocolId, asySapTxPacketSize=asySapTxPacketSize, asySapProtocolType=asySapProtocolType, asyDteUserDataField=asyDteUserDataField, asySapProfParameter19=asySapProfParameter19, asyDteCalledAddress=asyDteCalledAddress, DteIndex=DteIndex, asySapProfParameter28=asySapProfParameter28, asySapProfParameter23=asySapProfParameter23, asyProfParameter17=asyProfParameter17, asySapProfParameter3=asySapProfParameter3, asySapProfParameter14=asySapProfParameter14, asyX25TxQThreshold=asyX25TxQThreshold, asySapProfParameter15=asySapProfParameter15, PacketSize=PacketSize)
