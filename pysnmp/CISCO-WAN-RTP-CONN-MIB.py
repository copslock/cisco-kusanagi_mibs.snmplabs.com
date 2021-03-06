#
# PySNMP MIB module CISCO-WAN-RTP-CONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-RTP-CONN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Counter32, TimeTicks, Gauge32, Unsigned32, MibIdentifier, Bits, iso, ObjectIdentity, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "iso", "ObjectIdentity", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
ciscoWanRtpConnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 20))
ciscoWanRtpConnMIB.setRevisions(('2005-04-12 00:00', '2003-10-20 00:00', '2003-05-23 00:00', '2002-05-20 00:00', '2001-11-28 00:00', '2001-03-15 15:00',))
if mibBuilder.loadTexts: ciscoWanRtpConnMIB.setLastUpdated('200504120000Z')
if mibBuilder.loadTexts: ciscoWanRtpConnMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanRtpConnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 1))
vismRtpConnGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1))
vismRtpBearerStatsGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2))
vismRtpConnGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1), )
if mibBuilder.loadTexts: vismRtpConnGrpTable.setStatus('current')
vismRtpConnGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-RTP-CONN-MIB", "vismRtpConnNum"))
if mibBuilder.loadTexts: vismRtpConnGrpEntry.setStatus('current')
vismRtpConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 248)))
if mibBuilder.loadTexts: vismRtpConnNum.setStatus('current')
vismRtpEndptNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 248))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpEndptNum.setStatus('current')
vismRtpLocPort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(49648, 50142))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpLocPort.setStatus('current')
vismRtpRmtIp = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpRmtIp.setStatus('current')
vismRtpRmtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16384, 50142))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpRmtPort.setStatus('current')
vismRtpConnMode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("sendOnly", 1), ("rcvOnly", 2), ("sendAndRcv", 3), ("inactive", 4))).clone('sendAndRcv')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpConnMode.setStatus('current')
vismRtpBearerTos = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(160)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpBearerTos.setStatus('current')
vismRtpCodecType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("g711u", 1), ("g711a", 2), ("g726r32000", 3), ("g729a", 4), ("g729ab", 5), ("clearChannel", 6), ("g726r16000", 7), ("g726r24000", 8), ("g726r40000", 9), ("g723h", 11), ("g723ah", 12), ("g723l", 13), ("g723al", 14), ("lossless", 15)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpCodecType.setStatus('current')
vismRtpPktPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 20, 30, 40, 60))).clone(namedValues=NamedValues(("tenms", 10), ("twentyms", 20), ("thirtyms", 30), ("fourtyms", 40), ("sixtyms", 60))).clone('tenms')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpPktPeriod.setStatus('current')
vismRtpVadTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(250, 65535)).clone(250)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpVadTimer.setStatus('current')
vismRtpEcanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 11), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpEcanEnable.setStatus('current')
vismRtpTriRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpTriRedundancy.setStatus('current')
vismRtpDtmfTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 13), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpDtmfTransport.setStatus('current')
vismRtpCasTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 14), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpCasTransport.setStatus('current')
vismRtpVad = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpVad.setStatus('current')
vismRtpICSEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpICSEnable.setStatus('current')
vismRtpConnAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("failed", 2))).clone('active')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpConnAlarmState.setStatus('current')
vismRtpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpRowStatus.setStatus('current')
vismRtpLcn = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(131, 510))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpLcn.setStatus('current')
vismRtpFailReason = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("self", 1), ("highLevel", 2), ("both", 3), ("notFail", 4))).clone('notFail')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpFailReason.setStatus('current')
vismRtpPayloadType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismRtpPayloadType.setStatus('current')
vismRtpBearerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1), )
if mibBuilder.loadTexts: vismRtpBearerStatsTable.setStatus('current')
vismRtpBearerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-RTP-CONN-MIB", "vismRtpConnNum"))
if mibBuilder.loadTexts: vismRtpBearerStatsEntry.setStatus('current')
vismRtpPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpPktsSent.setStatus('current')
vismRtpPktsRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpPktsRcv.setStatus('current')
vismRtpOctsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpOctsSent.setStatus('current')
vismRtpOctsRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpOctsRcv.setStatus('current')
vismRtpPktsLost = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpPktsLost.setStatus('current')
vismRtpCntsCleared = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRtpCntsCleared.setStatus('current')
vismRtpInterArrivalJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 7), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpInterArrivalJitter.setStatus('current')
vismRtpLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 8), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRtpLatency.setStatus('current')
vismRtpConnNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 2))
vismRtpConnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 2, 0))
vismRtpConnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 3))
vismRtpConnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 1))
vismRtpConnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2))
vismRtpConnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 1, 1)).setObjects(("CISCO-WAN-RTP-CONN-MIB", "vismRtpConnGroup"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpBearerStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismRtpConnMIBCompliance = vismRtpConnMIBCompliance.setStatus('deprecated')
vismRtpConnMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 1, 2)).setObjects(("CISCO-WAN-RTP-CONN-MIB", "vismRtpConnGroup"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpBearerStatsGroup"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpBearerStatsGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismRtpConnMIBComplianceRev1 = vismRtpConnMIBComplianceRev1.setStatus('current')
vismRtpConnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2, 1)).setObjects(("CISCO-WAN-RTP-CONN-MIB", "vismRtpEndptNum"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLocPort"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpRmtIp"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpRmtPort"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpConnMode"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpBearerTos"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpCodecType"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktPeriod"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpVadTimer"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpEcanEnable"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpTriRedundancy"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpDtmfTransport"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpCasTransport"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpVad"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpICSEnable"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpConnAlarmState"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpRowStatus"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLcn"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpFailReason"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPayloadType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismRtpConnGroup = vismRtpConnGroup.setStatus('current')
vismRtpBearerStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2, 2)).setObjects(("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktsSent"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktsRcv"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpOctsSent"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpOctsRcv"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktsLost"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpCntsCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismRtpBearerStatsGroup = vismRtpBearerStatsGroup.setStatus('current')
vismRtpBearerStatsGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2, 3)).setObjects(("CISCO-WAN-RTP-CONN-MIB", "vismRtpInterArrivalJitter"), ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismRtpBearerStatsGroupSup1 = vismRtpBearerStatsGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-RTP-CONN-MIB", vismRtpBearerTos=vismRtpBearerTos, PYSNMP_MODULE_ID=ciscoWanRtpConnMIB, vismRtpConnMIBCompliances=vismRtpConnMIBCompliances, vismRtpConnAlarmState=vismRtpConnAlarmState, vismRtpConnGrpEntry=vismRtpConnGrpEntry, vismRtpCodecType=vismRtpCodecType, vismRtpBearerStatsGrp=vismRtpBearerStatsGrp, vismRtpFailReason=vismRtpFailReason, vismRtpConnNum=vismRtpConnNum, vismRtpCntsCleared=vismRtpCntsCleared, ciscoWanRtpConnMIB=ciscoWanRtpConnMIB, vismRtpICSEnable=vismRtpICSEnable, vismRtpPktPeriod=vismRtpPktPeriod, vismRtpConnMIBComplianceRev1=vismRtpConnMIBComplianceRev1, vismRtpConnMode=vismRtpConnMode, vismRtpTriRedundancy=vismRtpTriRedundancy, vismRtpLatency=vismRtpLatency, vismRtpDtmfTransport=vismRtpDtmfTransport, vismRtpConnMIBGroups=vismRtpConnMIBGroups, vismRtpConnGrp=vismRtpConnGrp, ciscoWanRtpConnMIBObjects=ciscoWanRtpConnMIBObjects, vismRtpEndptNum=vismRtpEndptNum, vismRtpConnGroup=vismRtpConnGroup, vismRtpLcn=vismRtpLcn, vismRtpLocPort=vismRtpLocPort, vismRtpBearerStatsTable=vismRtpBearerStatsTable, vismRtpVad=vismRtpVad, vismRtpConnMIBCompliance=vismRtpConnMIBCompliance, vismRtpPayloadType=vismRtpPayloadType, vismRtpBearerStatsEntry=vismRtpBearerStatsEntry, vismRtpVadTimer=vismRtpVadTimer, vismRtpBearerStatsGroupSup1=vismRtpBearerStatsGroupSup1, vismRtpPktsRcv=vismRtpPktsRcv, vismRtpCasTransport=vismRtpCasTransport, vismRtpConnGrpTable=vismRtpConnGrpTable, vismRtpRmtIp=vismRtpRmtIp, vismRtpRmtPort=vismRtpRmtPort, vismRtpOctsSent=vismRtpOctsSent, vismRtpOctsRcv=vismRtpOctsRcv, vismRtpConnMIBConformance=vismRtpConnMIBConformance, vismRtpConnNotifications=vismRtpConnNotifications, vismRtpInterArrivalJitter=vismRtpInterArrivalJitter, vismRtpPktsLost=vismRtpPktsLost, vismRtpPktsSent=vismRtpPktsSent, vismRtpBearerStatsGroup=vismRtpBearerStatsGroup, vismRtpRowStatus=vismRtpRowStatus, vismRtpConnNotificationPrefix=vismRtpConnNotificationPrefix, vismRtpEcanEnable=vismRtpEcanEnable)
