#
# PySNMP MIB module RTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RTM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
stratacom, = mibBuilder.importSymbols("CISCOWAN-SMI", "stratacom")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, TimeTicks, Gauge32, Unsigned32, MibIdentifier, Bits, iso, ObjectIdentity, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "iso", "ObjectIdentity", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rtm = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 120))
trapsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 120, 1))
trapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 1), )
if mibBuilder.loadTexts: trapConfigTable.setStatus('mandatory')
trapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1), ).setIndexNames((0, "RTM-MIB", "managerIPaddress"))
if mibBuilder.loadTexts: trapConfigEntry.setStatus('mandatory')
managerIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIPaddress.setStatus('mandatory')
managerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerPortNumber.setStatus('mandatory')
managerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("addRow", 1), ("delRow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerRowStatus.setStatus('mandatory')
readingTrapsFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: readingTrapsFlag.setStatus('mandatory')
nextTrapSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nextTrapSeqNum.setStatus('mandatory')
managerNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 120, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: managerNumOfValidEntries.setStatus('mandatory')
lastSequenceNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 120, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSequenceNumber.setStatus('mandatory')
trapUploadTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 4), )
if mibBuilder.loadTexts: trapUploadTable.setStatus('mandatory')
trapUploadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1), ).setIndexNames((0, "RTM-MIB", "trapManagerIPaddress"))
if mibBuilder.loadTexts: trapUploadEntry.setStatus('mandatory')
trapManagerIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerIPaddress.setStatus('mandatory')
trapSequenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapSequenceNum.setStatus('mandatory')
trapPduString = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapPduString.setStatus('mandatory')
endOfQueueFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: endOfQueueFlag.setStatus('mandatory')
recoverTrapTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 5), )
if mibBuilder.loadTexts: recoverTrapTable.setStatus('mandatory')
recoverTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1), ).setIndexNames((0, "RTM-MIB", "recoverTrapSequenceNum"))
if mibBuilder.loadTexts: recoverTrapEntry.setStatus('mandatory')
recoverTrapSequenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: recoverTrapSequenceNum.setStatus('mandatory')
recoverTrapPduString = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: recoverTrapPduString.setStatus('mandatory')
mibBuilder.exportSymbols("RTM-MIB", nextTrapSeqNum=nextTrapSeqNum, endOfQueueFlag=endOfQueueFlag, managerIPaddress=managerIPaddress, lastSequenceNumber=lastSequenceNumber, readingTrapsFlag=readingTrapsFlag, recoverTrapEntry=recoverTrapEntry, trapConfigTable=trapConfigTable, rtm=rtm, trapsConfig=trapsConfig, trapManagerIPaddress=trapManagerIPaddress, trapUploadTable=trapUploadTable, trapUploadEntry=trapUploadEntry, trapPduString=trapPduString, managerRowStatus=managerRowStatus, trapConfigEntry=trapConfigEntry, recoverTrapPduString=recoverTrapPduString, managerPortNumber=managerPortNumber, trapSequenceNum=trapSequenceNum, recoverTrapSequenceNum=recoverTrapSequenceNum, recoverTrapTable=recoverTrapTable, managerNumOfValidEntries=managerNumOfValidEntries)
