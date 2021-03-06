#
# PySNMP MIB module Wellfleet-SIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-SIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Opaque, Unsigned32, IpAddress, NotificationType, Counter64, ModuleIdentity, TimeTicks, Gauge32, Integer32, mgmt, mib_2, enterprises, ObjectIdentity, Counter32, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Opaque", "Unsigned32", "IpAddress", "NotificationType", "Counter64", "ModuleIdentity", "TimeTicks", "Gauge32", "Integer32", "mgmt", "mib-2", "enterprises", "ObjectIdentity", "Counter32", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfSipGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSipGroup")
wfSipPlcpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2))
wfSipL2 = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1), )
if mibBuilder.loadTexts: wfSipL2.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2.setDescription('The SIP L2 Table')
wfSipL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1), ).setIndexNames((0, "Wellfleet-SIP-MIB", "wfSipL2Index"))
if mibBuilder.loadTexts: wfSipL2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2Entry.setDescription('per circuit SIP Level 2 objects - wfSipL2Index corresponds to Wellfleet circuit number')
wfSipL2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2Index.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2Index.setDescription('this corresponds to the Wellfleet circuit number')
wfSipL2ReceivedCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2ReceivedCounts.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2ReceivedCounts.setDescription('total of unerrored received SIP L2 PDUs')
wfSipL2SentCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2SentCounts.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2SentCounts.setDescription("total of unerrored SIP L2 PDU's sent across the SNI")
wfSipHcsOrCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipHcsOrCRCErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipHcsOrCRCErrors.setDescription('total SIP L2 PDUs with HCS or CRC errors')
wfSipL2PayloadLengthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2PayloadLengthErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2PayloadLengthErrors.setDescription('total SIP L2 PDUs with length errors')
wfSipL2SequenceNumberErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2SequenceNumberErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2SequenceNumberErrors.setDescription('total SIP L2 PDUs with unexpected sequence numbers')
wfSipL2MidCurrentlyActiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2MidCurrentlyActiveErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2MidCurrentlyActiveErrors.setDescription('number of SIP L2 PDUs with BOMs previously started')
wfSipL2BomOrSSMsMIDErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2BomOrSSMsMIDErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2BomOrSSMsMIDErrors.setDescription('number of SIP L2 PDUs with zero BOMs or SSMs not zero')
wfSipL2EomsMIDErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2EomsMIDErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipL2EomsMIDErrors.setDescription('number of SIP L2 PDUs with zero EOMs or EOMs without BOMs')
wfSipDs1Plcp = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1), )
if mibBuilder.loadTexts: wfSipDs1Plcp.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs1Plcp.setDescription('The SIP DS1 PLCP Table')
wfSipDs1PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1), ).setIndexNames((0, "Wellfleet-SIP-MIB", "wfSipDs1PlcpIndex"))
if mibBuilder.loadTexts: wfSipDs1PlcpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs1PlcpEntry.setDescription('per circuit DS1 PLCP objects - wfSipDs1PlcpIndex corresponds to Wellfleet circuit number')
wfSipDs1PlcpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs1PlcpIndex.setDescription('this corresponds to the Wellfleet circuit number')
wfSipDs1PlcpSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpSEFs.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs1PlcpSEFs.setDescription('number of second intervals containing one or more severely errored seconds')
wfSipDs1PlcpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noalarm", 1), ("receivedfarendalarm", 2), ("incominglof", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs1PlcpAlarmState.setDescription('alarm state')
wfSipDs1PlcpUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpUASs.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs1PlcpUASs.setDescription('number of second intervals containing one or more unavailable seconds')
wfSipDs3Plcp = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2), )
if mibBuilder.loadTexts: wfSipDs3Plcp.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs3Plcp.setDescription('The SIP DS3 PLCP Table')
wfSipDs3PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1), ).setIndexNames((0, "Wellfleet-SIP-MIB", "wfSipDs3PlcpIndex"))
if mibBuilder.loadTexts: wfSipDs3PlcpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs3PlcpEntry.setDescription('per circuit DS3 PLCP objects - wfSipDs3PlcpIndex corresponds to Wellfleet circuit number')
wfSipDs3PlcpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs3PlcpIndex.setDescription('this corresponds to the Wellfleet circuit number')
wfSipDs3PlcpSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpSEFs.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs3PlcpSEFs.setDescription('number of second intervals containing one or more severely errored seconds')
wfSipDs3PlcpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noalarm", 1), ("receivedfarendalarm", 2), ("incominglof", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs3PlcpAlarmState.setDescription('alarm state')
wfSipDs3PlcpUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpUASs.setStatus('mandatory')
if mibBuilder.loadTexts: wfSipDs3PlcpUASs.setDescription('number of second intervals containing one or more unavailable seconds')
mibBuilder.exportSymbols("Wellfleet-SIP-MIB", wfSipL2=wfSipL2, wfSipDs3PlcpSEFs=wfSipDs3PlcpSEFs, wfSipDs1PlcpUASs=wfSipDs1PlcpUASs, wfSipL2PayloadLengthErrors=wfSipL2PayloadLengthErrors, wfSipL2BomOrSSMsMIDErrors=wfSipL2BomOrSSMsMIDErrors, wfSipL2EomsMIDErrors=wfSipL2EomsMIDErrors, wfSipL2SentCounts=wfSipL2SentCounts, wfSipL2MidCurrentlyActiveErrors=wfSipL2MidCurrentlyActiveErrors, wfSipL2SequenceNumberErrors=wfSipL2SequenceNumberErrors, wfSipL2Entry=wfSipL2Entry, wfSipHcsOrCRCErrors=wfSipHcsOrCRCErrors, wfSipDs1Plcp=wfSipDs1Plcp, wfSipDs3PlcpIndex=wfSipDs3PlcpIndex, wfSipDs1PlcpSEFs=wfSipDs1PlcpSEFs, wfSipDs1PlcpAlarmState=wfSipDs1PlcpAlarmState, wfSipL2Index=wfSipL2Index, wfSipPlcpGroup=wfSipPlcpGroup, wfSipDs3PlcpEntry=wfSipDs3PlcpEntry, wfSipDs1PlcpEntry=wfSipDs1PlcpEntry, wfSipDs3PlcpAlarmState=wfSipDs3PlcpAlarmState, wfSipDs3PlcpUASs=wfSipDs3PlcpUASs, wfSipDs3Plcp=wfSipDs3Plcp, wfSipDs1PlcpIndex=wfSipDs1PlcpIndex, wfSipL2ReceivedCounts=wfSipL2ReceivedCounts)
