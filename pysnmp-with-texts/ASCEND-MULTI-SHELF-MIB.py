#
# PySNMP MIB module ASCEND-MULTI-SHELF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MULTI-SHELF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
multiShelf, = mibBuilder.importSymbols("ASCEND-MIB", "multiShelf")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Bits, iso, Counter32, ObjectIdentity, Unsigned32, Integer32, Gauge32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Bits", "iso", "Counter32", "ObjectIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
myShelfNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 19, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myShelfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: myShelfNumber.setDescription('The shelf number associated with the system.')
myShelfOperation = MibScalar((1, 3, 6, 1, 4, 1, 529, 19, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("slave", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myShelfOperation.setStatus('mandatory')
if mibBuilder.loadTexts: myShelfOperation.setDescription('The operation mode of this shelf of a multi-shelf configuration.')
masterShelfNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 19, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: masterShelfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: masterShelfNumber.setDescription('The shelf number of the master of the multi-shelf configuration.')
multiShelfTableSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 19, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfTableSize.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfTableSize.setDescription('The maximum number of entries in the multiShelfTable.')
multiShelfTable = MibTable((1, 3, 6, 1, 4, 1, 529, 19, 5), )
if mibBuilder.loadTexts: multiShelfTable.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfTable.setDescription('The multi-shelf table.')
multiShelfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 19, 5, 1), ).setIndexNames((0, "ASCEND-MULTI-SHELF-MIB", "multiShelfIndex"))
if mibBuilder.loadTexts: multiShelfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfEntry.setDescription('An entry in the multi-shelf table.')
multiShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfIndex.setDescription('The index of the multi-shelf entry. The destination shelf number of the multi-shelf system.')
multiShelfState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("outGoing", 2), ("inComing", 3), ("up", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfState.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfState.setDescription('The state of the destination multi-shelf system.')
multiShelfResentFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfResentFrames.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfResentFrames.setDescription('The number of times frames were resent to the destination shelf number.')
multiShelfNLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfNLinkUp.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfNLinkUp.setDescription('The number of times the data link to the destination shelf number has gone up and down.')
multiShelfTxQs = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfTxQs.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfTxQs.setDescription('The current frames in the transmit queue to the destination shelf number.')
multiShelfTxSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfTxSeq.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfTxSeq.setDescription('The next transmit sequence number to the destination shelf number.')
multiShelfRxSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfRxSeq.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfRxSeq.setDescription('The next receive sequence number from the destination shelf number.')
multiShelfTimerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 19, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multiShelfTimerValue.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfTimerValue.setDescription('The timer value in seconds associated with the data link to the destination shelf number.')
multiShelfStateTrapState = MibScalar((1, 3, 6, 1, 4, 1, 529, 19, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: multiShelfStateTrapState.setStatus('mandatory')
if mibBuilder.loadTexts: multiShelfStateTrapState.setDescription('This variable indicates whether the master system produces the multiShelfStateChange trap.')
mibBuilder.exportSymbols("ASCEND-MULTI-SHELF-MIB", myShelfOperation=myShelfOperation, multiShelfTxQs=multiShelfTxQs, multiShelfRxSeq=multiShelfRxSeq, multiShelfEntry=multiShelfEntry, multiShelfResentFrames=multiShelfResentFrames, multiShelfTableSize=multiShelfTableSize, multiShelfTimerValue=multiShelfTimerValue, multiShelfNLinkUp=multiShelfNLinkUp, multiShelfState=multiShelfState, multiShelfStateTrapState=multiShelfStateTrapState, multiShelfTxSeq=multiShelfTxSeq, multiShelfTable=multiShelfTable, myShelfNumber=myShelfNumber, multiShelfIndex=multiShelfIndex, masterShelfNumber=masterShelfNumber)
