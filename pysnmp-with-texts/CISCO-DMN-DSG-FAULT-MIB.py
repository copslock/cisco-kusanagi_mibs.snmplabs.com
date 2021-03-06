#
# PySNMP MIB module CISCO-DMN-DSG-FAULT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-FAULT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, NotificationType, Unsigned32, MibIdentifier, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "NotificationType", "Unsigned32", "MibIdentifier", "iso", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGFault = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17))
ciscoDSGFault.setRevisions(('2010-08-30 11:00', '2010-03-22 05:00', '2010-02-12 12:00', '2010-01-08 12:00', '2009-12-20 12:00', '2009-12-07 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGFault.setRevisionsDescriptions(('V01.00.05 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.04 2010-03-22 The Syntax of Unsigned32 MIB objects whose range is within the range of Integer32, is updated to Integer32.', 'V01.00.03 2010-02-12 The Syntax of read-only objects is updated to DisplayString.', 'V01.00.02 2010-01-08 Updated FaultStatus and FaultSetting Table.', 'V01.00.01 2009-12-20 Removed logHistoryTable.', 'V01.00.00 2009-12-07 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGFault.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGFault.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGFault.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGFault.setDescription('Cisco DSG Fault Information MIB.')
faultSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1))
faultAWTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2))
faultSummaryNumActiveAlarms = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: faultSummaryNumActiveAlarms.setStatus('current')
if mibBuilder.loadTexts: faultSummaryNumActiveAlarms.setDescription('Number of system alarms currently in a set state. The range is from 0 to 4294967295.')
faultSummaryNumActiveWarnings = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: faultSummaryNumActiveWarnings.setStatus('current')
if mibBuilder.loadTexts: faultSummaryNumActiveWarnings.setDescription('Number of system Warnings currently in a set state. THe range is from 0 to 4294967295.')
faultSummaryClearAlarms = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeonly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: faultSummaryClearAlarms.setStatus('current')
if mibBuilder.loadTexts: faultSummaryClearAlarms.setDescription('Set this object to yes( 2 ) to clear the system Alarms.')
faultSummaryClearWarnings = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: faultSummaryClearWarnings.setStatus('current')
if mibBuilder.loadTexts: faultSummaryClearWarnings.setDescription('Set this object to yes( 2 ) to clear the system Warnings.')
faultSummaryClearHistory = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: faultSummaryClearHistory.setStatus('current')
if mibBuilder.loadTexts: faultSummaryClearHistory.setDescription('Set this object to yes( 2 ) to clear the system History.')
awFaultActiveListTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1), )
if mibBuilder.loadTexts: awFaultActiveListTable.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListTable.setDescription('Alarms and warnings fault active list table.')
awFaultActiveListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultActiveListPriority"))
if mibBuilder.loadTexts: awFaultActiveListEntry.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListEntry.setDescription('Entry for alarms and warnings fault active list.')
awFaultActiveListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: awFaultActiveListPriority.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListPriority.setDescription('Priority of fault.Higher priority faults are displayed first.')
awFaultActiveListTextID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultActiveListTextID.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListTextID.setDescription('Fault ID.')
awFaultActiveListName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultActiveListName.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListName.setDescription('Faults displayed text.')
awFaultActiveListType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarm", 1), ("warning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultActiveListType.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListType.setDescription('Active list type.')
awFaultActiveListSetDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultActiveListSetDateTime.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListSetDateTime.setDescription('Date and time of fault condition occurred.')
awFaultActiveListDetails = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultActiveListDetails.setStatus('current')
if mibBuilder.loadTexts: awFaultActiveListDetails.setDescription('Fault description.')
awFaultStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2), )
if mibBuilder.loadTexts: awFaultStatusTable.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusTable.setDescription('Alarms and warnings fault status.')
awFaultStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultStatusPriority"))
if mibBuilder.loadTexts: awFaultStatusEntry.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusEntry.setDescription('Entry for Alarms and warnings fault status.')
awFaultStatusPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: awFaultStatusPriority.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusPriority.setDescription('Fault status Priority value.')
awFaultStatusTextId = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusTextId.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusTextId.setDescription('Fault Status Text ID.')
awFaultStatusFaultNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusFaultNum.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusFaultNum.setDescription('Fault Status number.The range is from 0 to 4294967295.')
awFaultStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusName.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusName.setDescription('Fault displayed text.')
awFaultStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarm", 1), ("warning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusType.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusType.setDescription('Fault Status type.')
awFaultStatusSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("major", 1), ("minor", 2), ("warning", 3), ("information", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusSeverity.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusSeverity.setDescription('Fault severity.')
awFaultStatusLastDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusLastDateTime.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusLastDateTime.setDescription('Date&time of faults last state change.')
awFaultStatusTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("set", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusTrapState.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusTrapState.setDescription('Trap state.')
awFaultStatusDetails = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusDetails.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusDetails.setDescription('Faults descriptive reason.')
awFaultStatusRelay = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultStatusRelay.setStatus('current')
if mibBuilder.loadTexts: awFaultStatusRelay.setDescription('Fault Relay control status.The range is from 0 to 8. Indicates which relay output this fault is hardcoded to control. Not used.')
awFaultSettingTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3), )
if mibBuilder.loadTexts: awFaultSettingTable.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingTable.setDescription('Faults settings Table.')
awFaultSettingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1), ).setIndexNames((0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultSettingPriority"))
if mibBuilder.loadTexts: awFaultSettingEntry.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingEntry.setDescription('Entry for Faults settings Table.')
awFaultSettingPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: awFaultSettingPriority.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingPriority.setDescription('Fault Setting Index (Fault Priority value).')
awFaultSettingTextId = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultSettingTextId.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingTextId.setDescription('Fault Setting Text ID.')
awFaultSettingType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarm", 1), ("warning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultSettingType.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingType.setDescription('Fault type.')
awFaultSettingSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("major", 1), ("minor", 2), ("warning", 3), ("information", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultSettingSeverity.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingSeverity.setDescription('Fault severity.')
awFaultSettingName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultSettingName.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingName.setDescription('Fault displayed text.')
awFaultSettingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awFaultSettingEnable.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingEnable.setDescription('Controls overall enabling of this Fault.Affects LEDs, Relays, and Traps. disabled(3) is a read-only value.')
awFaultSettingRelay = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awFaultSettingRelay.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingRelay.setDescription('Controls whether Relays are enabled for the Fault. disabled(3) is a read-only value.')
awFaultSettingTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awFaultSettingTrap.setStatus('current')
if mibBuilder.loadTexts: awFaultSettingTrap.setDescription('Controls whether Traps are enabled for the Fault. disabled(3) is a read-only value.')
awFaultHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5), )
if mibBuilder.loadTexts: awFaultHistoryTable.setStatus('current')
if mibBuilder.loadTexts: awFaultHistoryTable.setDescription('Fault History table.')
awFaultHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1), ).setIndexNames((0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultHistorySequence"))
if mibBuilder.loadTexts: awFaultHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: awFaultHistoryEntry.setDescription('Entry for Fault History table.')
awFaultHistorySequence = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 1), Counter32())
if mibBuilder.loadTexts: awFaultHistorySequence.setStatus('current')
if mibBuilder.loadTexts: awFaultHistorySequence.setDescription('Fault History sequence number.')
awFaultHistoryName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultHistoryName.setStatus('current')
if mibBuilder.loadTexts: awFaultHistoryName.setDescription('Fault displayed text.')
awFaultHistoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarm", 1), ("warning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultHistoryType.setStatus('current')
if mibBuilder.loadTexts: awFaultHistoryType.setDescription('Fault History list Type.')
awFaultHistorySetDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultHistorySetDateTime.setStatus('current')
if mibBuilder.loadTexts: awFaultHistorySetDateTime.setDescription('Faults set date and time.')
awFaultHistoryResetDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultHistoryResetDateTime.setStatus('current')
if mibBuilder.loadTexts: awFaultHistoryResetDateTime.setDescription('Faults reset date and time. If cleared by reset, contains the power-up time.')
awFaultHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("clear", 1), ("set", 2), ("clearByReset", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultHistoryState.setStatus('current')
if mibBuilder.loadTexts: awFaultHistoryState.setDescription('Fault History list state.')
awFaultHistoryDetails = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: awFaultHistoryDetails.setStatus('current')
if mibBuilder.loadTexts: awFaultHistoryDetails.setDescription('Fault descriptive Reason.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-FAULT-MIB", faultSummaryClearHistory=faultSummaryClearHistory, awFaultActiveListName=awFaultActiveListName, awFaultActiveListPriority=awFaultActiveListPriority, awFaultStatusTable=awFaultStatusTable, faultSummaryClearWarnings=faultSummaryClearWarnings, awFaultStatusSeverity=awFaultStatusSeverity, awFaultStatusLastDateTime=awFaultStatusLastDateTime, awFaultSettingRelay=awFaultSettingRelay, awFaultHistoryDetails=awFaultHistoryDetails, faultSummaryNumActiveAlarms=faultSummaryNumActiveAlarms, PYSNMP_MODULE_ID=ciscoDSGFault, faultSummaryNumActiveWarnings=faultSummaryNumActiveWarnings, faultSummaryClearAlarms=faultSummaryClearAlarms, awFaultStatusFaultNum=awFaultStatusFaultNum, awFaultSettingSeverity=awFaultSettingSeverity, awFaultHistoryName=awFaultHistoryName, awFaultStatusDetails=awFaultStatusDetails, awFaultHistorySequence=awFaultHistorySequence, awFaultStatusPriority=awFaultStatusPriority, awFaultActiveListType=awFaultActiveListType, awFaultSettingType=awFaultSettingType, awFaultSettingName=awFaultSettingName, awFaultHistorySetDateTime=awFaultHistorySetDateTime, awFaultSettingTextId=awFaultSettingTextId, awFaultSettingTrap=awFaultSettingTrap, awFaultStatusType=awFaultStatusType, faultSummary=faultSummary, awFaultActiveListTable=awFaultActiveListTable, awFaultSettingEnable=awFaultSettingEnable, awFaultHistoryTable=awFaultHistoryTable, awFaultHistoryState=awFaultHistoryState, awFaultStatusName=awFaultStatusName, awFaultActiveListTextID=awFaultActiveListTextID, awFaultSettingPriority=awFaultSettingPriority, awFaultHistoryEntry=awFaultHistoryEntry, ciscoDSGFault=ciscoDSGFault, awFaultStatusTextId=awFaultStatusTextId, faultAWTable=faultAWTable, awFaultSettingEntry=awFaultSettingEntry, awFaultActiveListDetails=awFaultActiveListDetails, awFaultActiveListEntry=awFaultActiveListEntry, awFaultStatusRelay=awFaultStatusRelay, awFaultSettingTable=awFaultSettingTable, awFaultActiveListSetDateTime=awFaultActiveListSetDateTime, awFaultHistoryType=awFaultHistoryType, awFaultHistoryResetDateTime=awFaultHistoryResetDateTime, awFaultStatusEntry=awFaultStatusEntry, awFaultStatusTrapState=awFaultStatusTrapState)
