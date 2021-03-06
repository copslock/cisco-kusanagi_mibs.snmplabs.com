#
# PySNMP MIB module H3C-VODIALCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VODIALCONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
CodecType, = mibBuilder.importSymbols("H3C-VO-TYPE-MIB", "CodecType")
h3cVoice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cVoice")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Integer32, Unsigned32, NotificationType, MibIdentifier, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Gauge32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
h3cVoiceDialControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5))
h3cVoiceDialControl.setRevisions(('2005-03-15 00:00',))
if mibBuilder.loadTexts: h3cVoiceDialControl.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: h3cVoiceDialControl.setOrganization('Huawei-3COM Technologies Co., Ltd.')
class FaxProtocolType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("nonstandardCompatible", 1), ("t38", 2), ("h323T38", 3), ("sipT38", 4), ("pcmG711alaw", 5), ("pcmG711ulaw", 6))

class FaxBaudrateType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("disable", 1), ("voice", 2), ("b2400", 3), ("b4800", 4), ("b9600", 5), ("b14400", 6))

class FaxSupportModeType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rtp", 1), ("vt", 2), ("sip-udp", 3))

class FaxTrainMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("ppp", 2))

class PhoneNumberType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("abbreviated", 2), ("international", 3), ("national", 4), ("network", 5), ("reserved", 6), ("subscriber", 7), ("initial", 8))

class PhoneNumberPlan(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("data", 2), ("isdn", 3), ("national", 4), ("private", 5), ("reserved", 6), ("telex", 7), ("initial", 8))

h3cVoPeerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1))
h3cVoPeerCommonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1), )
if mibBuilder.loadTexts: h3cVoPeerCommonConfigTable.setStatus('current')
h3cVoPeerCommonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1), ).setIndexNames((0, "H3C-VODIALCONTROL-MIB", "h3cVoPeerCfgIndex"))
if mibBuilder.loadTexts: h3cVoPeerCommonConfigEntry.setStatus('current')
h3cVoPeerCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoPeerCfgIndex.setStatus('current')
h3cVoPeerCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgRowStatus.setStatus('current')
h3cVoPeerCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pots", 1), ("voip", 2), ("vofr", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgType.setStatus('current')
h3cVoPeerCfgDesPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgDesPattern.setStatus('current')
h3cVoPeerCfgCodec1st = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 5), CodecType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCodec1st.setStatus('current')
h3cVoPeerCfgCodec2nd = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 6), CodecType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCodec2nd.setStatus('current')
h3cVoPeerCfgCodec3rd = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 7), CodecType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCodec3rd.setStatus('current')
h3cVoPeerCfgCodec4th = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 8), CodecType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCodec4th.setStatus('current')
h3cVoPeerCfgDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgDSCP.setStatus('current')
h3cVoPeerCfgShutDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgShutDown.setStatus('current')
h3cVoPeerCfgVADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgVADEnable.setStatus('current')
h3cVoPeerCfgOutbandMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("h245", 1), ("voice", 2), ("sip", 3), ("h225", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgOutbandMode.setStatus('current')
h3cVoPeerCfgFaxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxLevel.setStatus('current')
h3cVoPeerCfgFaxBaudrate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 14), FaxBaudrateType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxBaudrate.setStatus('current')
h3cVoPeerCfgFaxLocalTrainPara = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxLocalTrainPara.setStatus('current')
h3cVoPeerCfgFaxProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 16), FaxProtocolType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxProtocol.setStatus('current')
h3cVoPeerCfgT38FaxHRPackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgT38FaxHRPackNum.setStatus('current')
h3cVoPeerCfgT38FaxLRPackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgT38FaxLRPackNum.setStatus('current')
h3cVoPeerCfgFaxSendNSFEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxSendNSFEnable.setStatus('current')
h3cVoPeerCfgFaxSupportMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 20), FaxSupportModeType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxSupportMode.setStatus('current')
h3cVoPeerCfgFaxTrainMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 21), FaxTrainMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxTrainMode.setStatus('current')
h3cVoPeerCfgFaxEcm = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disalbe", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgFaxEcm.setStatus('current')
h3cVoPeerCfgPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 23), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgPriority.setStatus('current')
h3cVoPeerCfgDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 24), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgDescription.setStatus('current')
h3cVoPeerCfgCallingNumberType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 25), PhoneNumberType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCallingNumberType.setStatus('current')
h3cVoPeerCfgCalledNumberType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 26), PhoneNumberType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCalledNumberType.setStatus('current')
h3cVoPeerCfgCallingNumberPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 27), PhoneNumberPlan()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCallingNumberPlan.setStatus('current')
h3cVoPeerCfgCalledNumberPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 28), PhoneNumberPlan()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCalledNumberPlan.setStatus('current')
h3cVoPeerCfgSelectStop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgSelectStop.setStatus('current')
h3cVoPeerCfgCallingNumSubstRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCallingNumSubstRule.setStatus('current')
h3cVoPeerCfgCalledNumSubstRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgCalledNumSubstRule.setStatus('current')
h3cVoPeerCfgMaxCall = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCfgMaxCall.setStatus('current')
h3cVoPOTSPeerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 2), )
if mibBuilder.loadTexts: h3cVoPOTSPeerConfigTable.setStatus('current')
h3cVoPOTSPeerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 2, 1), ).setIndexNames((0, "H3C-VODIALCONTROL-MIB", "h3cVoPOTSPeerConfigIndex"))
if mibBuilder.loadTexts: h3cVoPOTSPeerConfigEntry.setStatus('current')
h3cVoPOTSPeerConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoPOTSPeerConfigIndex.setStatus('current')
h3cVoPOTSPeerConfigPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSPeerConfigPrefix.setStatus('current')
h3cVoPOTSPeerConfigSubLine = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 2, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSPeerConfigSubLine.setStatus('current')
h3cVoPOTSPeerConfigSendNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPOTSPeerConfigSendNum.setStatus('current')
h3cVoVoIPPeerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3), )
if mibBuilder.loadTexts: h3cVoVoIPPeerConfigTable.setStatus('current')
h3cVoVoIPPeerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1), ).setIndexNames((0, "H3C-VODIALCONTROL-MIB", "h3cVoVoIPPeerCfgIndex"))
if mibBuilder.loadTexts: h3cVoVoIPPeerConfigEntry.setStatus('current')
h3cVoVoIPPeerCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgIndex.setStatus('current')
h3cVoVoIPPeerCfgTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ras", 2), ("h323IpAddress", 3), ("sipIpAddress", 4), ("sipProxy", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgTargetType.setStatus('current')
h3cVoVoIPPeerCfgTargetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgTargetAddrType.setStatus('current')
h3cVoVoIPPeerCfgTargetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgTargetAddr.setStatus('current')
h3cVoVoIPPeerCfgFastStart = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgFastStart.setStatus('current')
h3cVoVoIPPeerCfgTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgTunnel.setStatus('current')
h3cVoVoIPPeerCfgAreaID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgAreaID.setStatus('current')
h3cVoVoIPPeerCfgSendRing = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoVoIPPeerCfgSendRing.setStatus('current')
h3cVoPeerDefaultConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4))
h3cVoPeerDefault1stCodecLevel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 2), CodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefault1stCodecLevel.setStatus('current')
h3cVoPeerDefault2ndCodecLevel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 3), CodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefault2ndCodecLevel.setStatus('current')
h3cVoPeerDefault3rdCodecLevel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 4), CodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefault3rdCodecLevel.setStatus('current')
h3cVoPeerDefault4thCodecLevel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 5), CodecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefault4thCodecLevel.setStatus('current')
h3cVoPeerDefaultVADOn = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultVADOn.setStatus('current')
h3cVoPeerDefaultFaxTransLevel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxTransLevel.setStatus('current')
h3cVoPeerDefaultFaxLocalTrain = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxLocalTrain.setStatus('current')
h3cVoPeerDefaultFaxProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 9), FaxProtocolType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxProtocol.setStatus('current')
h3cVoPeerDefaultFaxHSRedunNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxHSRedunNum.setStatus('current')
h3cVoPeerDefaultFaxLSRedunNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxLSRedunNum.setStatus('current')
h3cVoPeerDefaultFaxBaudrate = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 12), FaxBaudrateType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxBaudrate.setStatus('current')
h3cVoPeerDefaultFaxNSF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxNSF.setStatus('current')
h3cVoPeerDefaultFaxSupportMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 14), FaxSupportModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxSupportMode.setStatus('current')
h3cVoPeerDefaultFaxTrainMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 15), FaxTrainMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxTrainMode.setStatus('current')
h3cVoPeerDefaultFaxECM = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 4, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoPeerDefaultFaxECM.setStatus('current')
h3cVoPeerCfgCallerPermitTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 5), )
if mibBuilder.loadTexts: h3cVoPeerCfgCallerPermitTable.setStatus('current')
h3cVoPeerCfgCallerPermitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 5, 1), ).setIndexNames((0, "H3C-VODIALCONTROL-MIB", "h3cVoPeerCfgIndex"), (0, "H3C-VODIALCONTROL-MIB", "h3cVoPeerCfgCallerPermitNum"))
if mibBuilder.loadTexts: h3cVoPeerCfgCallerPermitEntry.setStatus('current')
h3cVoPeerCfgCallerPermitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 5, 1, 1), OctetString())
if mibBuilder.loadTexts: h3cVoPeerCfgCallerPermitNum.setStatus('current')
h3cVoPeerCallerPermitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 5, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoPeerCallerPermitRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-VODIALCONTROL-MIB", h3cVoPeerCfgCodec2nd=h3cVoPeerCfgCodec2nd, h3cVoPeerDefaultFaxNSF=h3cVoPeerDefaultFaxNSF, h3cVoPOTSPeerConfigIndex=h3cVoPOTSPeerConfigIndex, h3cVoPeerDefaultVADOn=h3cVoPeerDefaultVADOn, h3cVoPeerCfgDSCP=h3cVoPeerCfgDSCP, h3cVoPeerDefaultFaxProtocol=h3cVoPeerDefaultFaxProtocol, h3cVoPeerCfgCodec4th=h3cVoPeerCfgCodec4th, h3cVoPeerCfgCallingNumberPlan=h3cVoPeerCfgCallingNumberPlan, h3cVoPeerDefault4thCodecLevel=h3cVoPeerDefault4thCodecLevel, h3cVoPeerCfgPriority=h3cVoPeerCfgPriority, h3cVoPeerDefaultFaxBaudrate=h3cVoPeerDefaultFaxBaudrate, PhoneNumberType=PhoneNumberType, h3cVoVoIPPeerConfigEntry=h3cVoVoIPPeerConfigEntry, h3cVoPeerCfgCodec1st=h3cVoPeerCfgCodec1st, h3cVoVoIPPeerCfgTunnel=h3cVoVoIPPeerCfgTunnel, h3cVoVoIPPeerCfgFastStart=h3cVoVoIPPeerCfgFastStart, h3cVoPeerCfgMaxCall=h3cVoPeerCfgMaxCall, h3cVoPOTSPeerConfigSubLine=h3cVoPOTSPeerConfigSubLine, FaxSupportModeType=FaxSupportModeType, h3cVoVoIPPeerCfgSendRing=h3cVoVoIPPeerCfgSendRing, h3cVoPeerDefaultFaxLSRedunNum=h3cVoPeerDefaultFaxLSRedunNum, FaxBaudrateType=FaxBaudrateType, h3cVoVoIPPeerCfgAreaID=h3cVoVoIPPeerCfgAreaID, h3cVoPeerCfgSelectStop=h3cVoPeerCfgSelectStop, h3cVoPeerObjects=h3cVoPeerObjects, h3cVoPOTSPeerConfigPrefix=h3cVoPOTSPeerConfigPrefix, h3cVoPeerCfgT38FaxHRPackNum=h3cVoPeerCfgT38FaxHRPackNum, h3cVoPeerCfgDescription=h3cVoPeerCfgDescription, h3cVoPeerCfgCodec3rd=h3cVoPeerCfgCodec3rd, h3cVoPeerCfgT38FaxLRPackNum=h3cVoPeerCfgT38FaxLRPackNum, h3cVoPeerCfgShutDown=h3cVoPeerCfgShutDown, h3cVoPeerCfgCalledNumberType=h3cVoPeerCfgCalledNumberType, h3cVoPOTSPeerConfigSendNum=h3cVoPOTSPeerConfigSendNum, h3cVoVoIPPeerCfgIndex=h3cVoVoIPPeerCfgIndex, h3cVoPeerCommonConfigTable=h3cVoPeerCommonConfigTable, h3cVoVoIPPeerCfgTargetType=h3cVoVoIPPeerCfgTargetType, h3cVoPeerCallerPermitRowStatus=h3cVoPeerCallerPermitRowStatus, h3cVoPeerCfgFaxSupportMode=h3cVoPeerCfgFaxSupportMode, h3cVoPeerDefaultFaxHSRedunNum=h3cVoPeerDefaultFaxHSRedunNum, h3cVoVoIPPeerCfgTargetAddr=h3cVoVoIPPeerCfgTargetAddr, h3cVoPeerCfgFaxSendNSFEnable=h3cVoPeerCfgFaxSendNSFEnable, h3cVoPeerDefaultFaxTransLevel=h3cVoPeerDefaultFaxTransLevel, PhoneNumberPlan=PhoneNumberPlan, FaxProtocolType=FaxProtocolType, h3cVoPeerCfgFaxBaudrate=h3cVoPeerCfgFaxBaudrate, h3cVoVoIPPeerConfigTable=h3cVoVoIPPeerConfigTable, h3cVoPeerCfgCallingNumSubstRule=h3cVoPeerCfgCallingNumSubstRule, h3cVoPeerCfgFaxLevel=h3cVoPeerCfgFaxLevel, h3cVoPOTSPeerConfigEntry=h3cVoPOTSPeerConfigEntry, h3cVoPeerDefault3rdCodecLevel=h3cVoPeerDefault3rdCodecLevel, h3cVoPeerDefault2ndCodecLevel=h3cVoPeerDefault2ndCodecLevel, h3cVoPeerCfgOutbandMode=h3cVoPeerCfgOutbandMode, h3cVoPeerCfgType=h3cVoPeerCfgType, h3cVoPeerCfgRowStatus=h3cVoPeerCfgRowStatus, h3cVoPeerCfgCallerPermitTable=h3cVoPeerCfgCallerPermitTable, h3cVoPeerCommonConfigEntry=h3cVoPeerCommonConfigEntry, h3cVoPeerDefaultFaxLocalTrain=h3cVoPeerDefaultFaxLocalTrain, h3cVoPeerCfgCallingNumberType=h3cVoPeerCfgCallingNumberType, h3cVoPeerDefaultFaxECM=h3cVoPeerDefaultFaxECM, h3cVoPeerCfgCallerPermitEntry=h3cVoPeerCfgCallerPermitEntry, h3cVoPeerDefaultFaxSupportMode=h3cVoPeerDefaultFaxSupportMode, h3cVoPeerCfgFaxLocalTrainPara=h3cVoPeerCfgFaxLocalTrainPara, h3cVoPeerCfgDesPattern=h3cVoPeerCfgDesPattern, h3cVoPeerCfgVADEnable=h3cVoPeerCfgVADEnable, h3cVoPeerDefaultFaxTrainMode=h3cVoPeerDefaultFaxTrainMode, h3cVoPeerDefault1stCodecLevel=h3cVoPeerDefault1stCodecLevel, h3cVoPeerCfgCalledNumberPlan=h3cVoPeerCfgCalledNumberPlan, h3cVoPeerCfgCallerPermitNum=h3cVoPeerCfgCallerPermitNum, h3cVoiceDialControl=h3cVoiceDialControl, h3cVoPeerDefaultConfigObjects=h3cVoPeerDefaultConfigObjects, h3cVoPOTSPeerConfigTable=h3cVoPOTSPeerConfigTable, h3cVoPeerCfgFaxEcm=h3cVoPeerCfgFaxEcm, h3cVoPeerCfgIndex=h3cVoPeerCfgIndex, PYSNMP_MODULE_ID=h3cVoiceDialControl, h3cVoPeerCfgFaxProtocol=h3cVoPeerCfgFaxProtocol, h3cVoVoIPPeerCfgTargetAddrType=h3cVoVoIPPeerCfgTargetAddrType, FaxTrainMode=FaxTrainMode, h3cVoPeerCfgFaxTrainMode=h3cVoPeerCfgFaxTrainMode, h3cVoPeerCfgCalledNumSubstRule=h3cVoPeerCfgCalledNumSubstRule)
