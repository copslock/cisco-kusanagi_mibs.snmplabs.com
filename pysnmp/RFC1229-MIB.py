#
# PySNMP MIB module RFC1229-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1229-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:48:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, MibIdentifier, ModuleIdentity, iso, Integer32, Counter64, Gauge32, ObjectIdentity, Counter32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "MibIdentifier", "ModuleIdentity", "iso", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "Unsigned32", "IpAddress")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
ifExtensions = MibIdentifier((1, 3, 6, 1, 2, 1, 12))
ifExtnsTable = MibTable((1, 3, 6, 1, 2, 1, 12, 1), )
if mibBuilder.loadTexts: ifExtnsTable.setStatus('mandatory')
ifExtnsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 12, 1, 1), ).setIndexNames((0, "RFC1229-MIB", "ifExtnsIfIndex"))
if mibBuilder.loadTexts: ifExtnsEntry.setStatus('mandatory')
ifExtnsIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsIfIndex.setStatus('mandatory')
ifExtnsChipSet = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsChipSet.setStatus('mandatory')
ifExtnsRevWare = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsRevWare.setStatus('mandatory')
ifExtnsMulticastsTransmittedOks = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsMulticastsTransmittedOks.setStatus('mandatory')
ifExtnsBroadcastsTransmittedOks = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsBroadcastsTransmittedOks.setStatus('mandatory')
ifExtnsMulticastsReceivedOks = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsMulticastsReceivedOks.setStatus('mandatory')
ifExtnsBroadcastsReceivedOks = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsBroadcastsReceivedOks.setStatus('mandatory')
ifExtnsPromiscuous = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsPromiscuous.setStatus('mandatory')
ifExtnsTestTable = MibTable((1, 3, 6, 1, 2, 1, 12, 2), )
if mibBuilder.loadTexts: ifExtnsTestTable.setStatus('mandatory')
ifExtnsTestEntry = MibTableRow((1, 3, 6, 1, 2, 1, 12, 2, 1), ).setIndexNames((0, "RFC1229-MIB", "ifExtnsTestIfIndex"))
if mibBuilder.loadTexts: ifExtnsTestEntry.setStatus('mandatory')
ifExtnsTestIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsTestIfIndex.setStatus('mandatory')
ifExtnsTestCommunity = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsTestCommunity.setStatus('mandatory')
ifExtnsTestRequestId = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsTestRequestId.setStatus('mandatory')
ifExtnsTestType = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 2, 1, 4), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtnsTestType.setStatus('mandatory')
wellKnownTests = MibIdentifier((1, 3, 6, 1, 2, 1, 12, 4))
testFullDuplexLoopBack = MibIdentifier((1, 3, 6, 1, 2, 1, 12, 4, 1))
ifExtnsTestResult = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("notSupported", 4), ("unAbleToRun", 5), ("aborted", 6), ("failed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsTestResult.setStatus('mandatory')
ifExtnsTestCode = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 2, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsTestCode.setStatus('mandatory')
ifExtnsRcvAddrTable = MibTable((1, 3, 6, 1, 2, 1, 12, 3), )
if mibBuilder.loadTexts: ifExtnsRcvAddrTable.setStatus('mandatory')
ifExtnsRcvAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 12, 3, 1), ).setIndexNames((0, "RFC1229-MIB", "ifExtnsRcvAddrIfIndex"), (0, "RFC1229-MIB", "ifExtnsRcvAddress"))
if mibBuilder.loadTexts: ifExtnsRcvAddrEntry.setStatus('mandatory')
ifExtnsRcvAddrIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsRcvAddrIfIndex.setStatus('mandatory')
ifExtnsRcvAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 3, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtnsRcvAddress.setStatus('mandatory')
ifExtnsRcvAddrStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 12, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("volatile", 3), ("nonVolatile", 4))).clone('volatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtnsRcvAddrStatus.setStatus('mandatory')
mibBuilder.exportSymbols("RFC1229-MIB", ifExtnsTestIfIndex=ifExtnsTestIfIndex, ifExtnsRcvAddrEntry=ifExtnsRcvAddrEntry, ifExtnsTestRequestId=ifExtnsTestRequestId, ifExtnsRcvAddrIfIndex=ifExtnsRcvAddrIfIndex, ifExtnsChipSet=ifExtnsChipSet, ifExtnsEntry=ifExtnsEntry, ifExtnsRcvAddrStatus=ifExtnsRcvAddrStatus, ifExtnsIfIndex=ifExtnsIfIndex, testFullDuplexLoopBack=testFullDuplexLoopBack, ifExtnsRcvAddrTable=ifExtnsRcvAddrTable, ifExtnsRevWare=ifExtnsRevWare, ifExtnsTable=ifExtnsTable, ifExtnsMulticastsTransmittedOks=ifExtnsMulticastsTransmittedOks, ifExtnsTestCode=ifExtnsTestCode, ifExtnsRcvAddress=ifExtnsRcvAddress, wellKnownTests=wellKnownTests, ifExtnsBroadcastsTransmittedOks=ifExtnsBroadcastsTransmittedOks, ifExtnsBroadcastsReceivedOks=ifExtnsBroadcastsReceivedOks, ifExtnsTestEntry=ifExtnsTestEntry, ifExtnsPromiscuous=ifExtnsPromiscuous, ifExtnsMulticastsReceivedOks=ifExtnsMulticastsReceivedOks, ifExtnsTestTable=ifExtnsTestTable, ifExtensions=ifExtensions, ifExtnsTestCommunity=ifExtnsTestCommunity, ifExtnsTestResult=ifExtnsTestResult, ifExtnsTestType=ifExtnsTestType)
