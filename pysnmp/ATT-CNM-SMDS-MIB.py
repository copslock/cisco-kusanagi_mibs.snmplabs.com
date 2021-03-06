#
# PySNMP MIB module ATT-CNM-SMDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATT-CNM-SMDS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, Unsigned32, Counter32, MibIdentifier, Integer32, IpAddress, enterprises, NotificationType, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "enterprises", "NotificationType", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
att_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 74)).setLabel("att-2")
att_products = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1)).setLabel("att-products")
att_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2)).setLabel("att-mgmt")
att_cnmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1, 9)).setLabel("att-cnmAgent")
att_cnm = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15)).setLabel("att-cnm")
att_cnm_smds = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15, 6)).setLabel("att-cnm-smds")
class SMDSAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

attCNMsmdsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1), )
if mibBuilder.loadTexts: attCNMsmdsConfigTable.setStatus('mandatory')
attCNMsmdsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsConfigIndex"))
if mibBuilder.loadTexts: attCNMsmdsConfigEntry.setStatus('mandatory')
attCNMsmdsConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsConfigIndex.setStatus('mandatory')
attCNMsmdsAccessClass = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noClass", 1), ("accessClass1", 2), ("accessClass2", 3), ("accessClass3", 4), ("accessClass4", 5), ("accessClass5", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsAccessClass.setStatus('mandatory')
attCNMsmdsMCDUsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mcdusIn1", 1), ("mcdusIn16", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsMCDUsIn.setStatus('mandatory')
attCNMsmdsMCDUsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mcdusOut1", 1), ("mcdusOut16", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsMCDUsOut.setStatus('mandatory')
attCNMsmdsIndivScreenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allowed", 1), ("disallowed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsIndivScreenMode.setStatus('mandatory')
attCNMsmdsGroupScreenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allowed", 1), ("disallowed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsGroupScreenMode.setStatus('mandatory')
attCNMsmdsAddrIndexDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsAddrIndexDescr.setStatus('mandatory')
attCNMsmdsDisagreeMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeMaxIntervals.setStatus('mandatory')
attCNMsmdsDisagreeIntervalLen = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeIntervalLen.setStatus('mandatory')
attCNMsmdsAddrTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2), )
if mibBuilder.loadTexts: attCNMsmdsAddrTable.setStatus('mandatory')
attCNMsmdsAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsAddrCountryIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsAddrAreaIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsAddrSubscriberIndex"))
if mibBuilder.loadTexts: attCNMsmdsAddrEntry.setStatus('mandatory')
attCNMsmdsAddrCountryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: attCNMsmdsAddrCountryIndex.setStatus('mandatory')
attCNMsmdsAddrAreaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: attCNMsmdsAddrAreaIndex.setStatus('mandatory')
attCNMsmdsAddrSubscriberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 3), Integer32())
if mibBuilder.loadTexts: attCNMsmdsAddrSubscriberIndex.setStatus('mandatory')
attCNMsmdsAddressOnSNI = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 4), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsAddressOnSNI.setStatus('mandatory')
attCNMsmdsInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsInterfaceIndex.setStatus('mandatory')
attCNMsmdsIndScrTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3), )
if mibBuilder.loadTexts: attCNMsmdsIndScrTable.setStatus('mandatory')
attCNMsmdsIndScrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrCountryIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrAreaIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrSubscriberIndex"))
if mibBuilder.loadTexts: attCNMsmdsIndScrEntry.setStatus('mandatory')
attCNMsmdsIndScrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsIndScrIndex.setStatus('mandatory')
attCNMsmdsIndScrCountryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: attCNMsmdsIndScrCountryIndex.setStatus('mandatory')
attCNMsmdsIndScrAreaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: attCNMsmdsIndScrAreaIndex.setStatus('mandatory')
attCNMsmdsIndScrSubscriberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 4), Integer32())
if mibBuilder.loadTexts: attCNMsmdsIndScrSubscriberIndex.setStatus('mandatory')
attCNMsmdsIndivScreenAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 5), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsIndivScreenAddress.setStatus('mandatory')
attCNMsmdsGrpScrTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4), )
if mibBuilder.loadTexts: attCNMsmdsGrpScrTable.setStatus('mandatory')
attCNMsmdsGrpScrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrCountryIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrAreaIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrSubscriberIndex"))
if mibBuilder.loadTexts: attCNMsmdsGrpScrEntry.setStatus('mandatory')
attCNMsmdsGrpScrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsGrpScrIndex.setStatus('mandatory')
attCNMsmdsGrpScrCountryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpScrCountryIndex.setStatus('mandatory')
attCNMsmdsGrpScrAreaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 3), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpScrAreaIndex.setStatus('mandatory')
attCNMsmdsGrpScrSubscriberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 4), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpScrSubscriberIndex.setStatus('mandatory')
attCNMsmdsGroupScreenAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 5), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsGroupScreenAddress.setStatus('mandatory')
attCNMsmdsMemGrpTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5), )
if mibBuilder.loadTexts: attCNMsmdsMemGrpTable.setStatus('mandatory')
attCNMsmdsMemGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpMemberCountryIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpMemberAreaIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpMemberSubscriberIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpGroupCountryIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpGroupAreaIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpGroupSubscriberIndex"))
if mibBuilder.loadTexts: attCNMsmdsMemGrpEntry.setStatus('mandatory')
attCNMsmdsMemGrpMemberCountryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: attCNMsmdsMemGrpMemberCountryIndex.setStatus('mandatory')
attCNMsmdsMemGrpMemberAreaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: attCNMsmdsMemGrpMemberAreaIndex.setStatus('mandatory')
attCNMsmdsMemGrpMemberSubscriberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: attCNMsmdsMemGrpMemberSubscriberIndex.setStatus('mandatory')
attCNMsmdsMemGrpGroupCountryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 4), Integer32())
if mibBuilder.loadTexts: attCNMsmdsMemGrpGroupCountryIndex.setStatus('mandatory')
attCNMsmdsMemGrpGroupAreaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 5), Integer32())
if mibBuilder.loadTexts: attCNMsmdsMemGrpGroupAreaIndex.setStatus('mandatory')
attCNMsmdsMemGrpGroupSubscriberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 6), Integer32())
if mibBuilder.loadTexts: attCNMsmdsMemGrpGroupSubscriberIndex.setStatus('mandatory')
attCNMsmdsMemberAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 7), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsMemberAddress.setStatus('mandatory')
attCNMsmdsAssociatedGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 8), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsAssociatedGroup.setStatus('mandatory')
attCNMsmdsGrpMemTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6), )
if mibBuilder.loadTexts: attCNMsmdsGrpMemTable.setStatus('mandatory')
attCNMsmdsGrpMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemGroupCountryIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemGroupAreaIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemGroupSubscriberIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemMemberCountryIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemMemberAreaIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemMemberSubscriberIndex"))
if mibBuilder.loadTexts: attCNMsmdsGrpMemEntry.setStatus('mandatory')
attCNMsmdsGrpMemGroupCountryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpMemGroupCountryIndex.setStatus('mandatory')
attCNMsmdsGrpMemGroupAreaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 2), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpMemGroupAreaIndex.setStatus('mandatory')
attCNMsmdsGrpMemGroupSubscriberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpMemGroupSubscriberIndex.setStatus('mandatory')
attCNMsmdsGrpMemMemberCountryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 4), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpMemMemberCountryIndex.setStatus('mandatory')
attCNMsmdsGrpMemMemberAreaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 5), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpMemMemberAreaIndex.setStatus('mandatory')
attCNMsmdsGrpMemMemberSubscriberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 6), Integer32())
if mibBuilder.loadTexts: attCNMsmdsGrpMemMemberSubscriberIndex.setStatus('mandatory')
attCNMsmdsGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 7), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsGroupAddress.setStatus('mandatory')
attCNMsmdsGroupMember = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 8), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsGroupMember.setStatus('mandatory')
attCNMsmdsDisagreeTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7), )
if mibBuilder.loadTexts: attCNMsmdsDisagreeTable.setStatus('mandatory')
attCNMsmdsDisagreeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeInterval"))
if mibBuilder.loadTexts: attCNMsmdsDisagreeEntry.setStatus('mandatory')
attCNMsmdsDisagreeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeIndex.setStatus('mandatory')
attCNMsmdsDisagreeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeInterval.setStatus('mandatory')
attCNMsmdsDisagreeTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeTimeStamp.setStatus('mandatory')
attCNMsmdsDisagreeLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeLocalTime.setStatus('mandatory')
attCNMsmdsAccessClassExceededCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsAccessClassExceededCounts.setStatus('mandatory')
attCNMsmdsMCDUsExceededAtIngressCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsMCDUsExceededAtIngressCounts.setStatus('mandatory')
attCNMsmdsMCDUsExceededAtEgressCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsMCDUsExceededAtEgressCounts.setStatus('mandatory')
attCNMsmdsSAScreenViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsSAScreenViolations.setStatus('mandatory')
attCNMsmdsDAScreenViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDAScreenViolations.setStatus('mandatory')
attCNMsmdsUnassignedSAs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsUnassignedSAs.setStatus('mandatory')
attCNMsmdsDestinationSNIUnavailableCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDestinationSNIUnavailableCounts.setStatus('mandatory')
attCNMsmdsDisagreeLogTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8), )
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogTable.setStatus('mandatory')
attCNMsmdsDisagreeLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1), ).setIndexNames((0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeLogIndex"), (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeLogType"))
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogEntry.setStatus('mandatory')
attCNMsmdsDisagreeLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogIndex.setStatus('mandatory')
attCNMsmdsDisagreeLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("sourceAddressScreenViolation", 1), ("destinationAddressScreenViolation", 2), ("invalidSourceAddressForSNI", 3), ("destSNInotAvailable", 4), ("accessClassExceeded", 5), ("mcduExceededAtIngress", 6), ("mcduExceededAtEgress", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogType.setStatus('mandatory')
attCNMsmdsDisagreeLogSA = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 3), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogSA.setStatus('mandatory')
attCNMsmdsDisagreeLogDA = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 4), SMDSAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogDA.setStatus('mandatory')
attCNMsmdsDisagreeLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogTimeStamp.setStatus('mandatory')
attCNMsmdsDisagreeLogLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMsmdsDisagreeLogLocalTime.setStatus('mandatory')
mibBuilder.exportSymbols("ATT-CNM-SMDS-MIB", attCNMsmdsDisagreeLogType=attCNMsmdsDisagreeLogType, attCNMsmdsIndScrAreaIndex=attCNMsmdsIndScrAreaIndex, attCNMsmdsMemGrpGroupCountryIndex=attCNMsmdsMemGrpGroupCountryIndex, attCNMsmdsGrpMemGroupSubscriberIndex=attCNMsmdsGrpMemGroupSubscriberIndex, attCNMsmdsAddressOnSNI=attCNMsmdsAddressOnSNI, attCNMsmdsGroupMember=attCNMsmdsGroupMember, attCNMsmdsMemGrpGroupAreaIndex=attCNMsmdsMemGrpGroupAreaIndex, attCNMsmdsGrpScrTable=attCNMsmdsGrpScrTable, attCNMsmdsGrpScrCountryIndex=attCNMsmdsGrpScrCountryIndex, attCNMsmdsAssociatedGroup=attCNMsmdsAssociatedGroup, attCNMsmdsDisagreeLogEntry=attCNMsmdsDisagreeLogEntry, attCNMsmdsMemGrpMemberCountryIndex=attCNMsmdsMemGrpMemberCountryIndex, attCNMsmdsDisagreeLogIndex=attCNMsmdsDisagreeLogIndex, attCNMsmdsMemGrpMemberSubscriberIndex=attCNMsmdsMemGrpMemberSubscriberIndex, attCNMsmdsDisagreeLocalTime=attCNMsmdsDisagreeLocalTime, attCNMsmdsConfigTable=attCNMsmdsConfigTable, attCNMsmdsMCDUsExceededAtEgressCounts=attCNMsmdsMCDUsExceededAtEgressCounts, attCNMsmdsDisagreeLogLocalTime=attCNMsmdsDisagreeLogLocalTime, attCNMsmdsDisagreeTimeStamp=attCNMsmdsDisagreeTimeStamp, attCNMsmdsMCDUsIn=attCNMsmdsMCDUsIn, attCNMsmdsGrpScrIndex=attCNMsmdsGrpScrIndex, attCNMsmdsAccessClass=attCNMsmdsAccessClass, attCNMsmdsDisagreeTable=attCNMsmdsDisagreeTable, attCNMsmdsUnassignedSAs=attCNMsmdsUnassignedSAs, attCNMsmdsGroupAddress=attCNMsmdsGroupAddress, attCNMsmdsDisagreeEntry=attCNMsmdsDisagreeEntry, attCNMsmdsInterfaceIndex=attCNMsmdsInterfaceIndex, attCNMsmdsIndScrCountryIndex=attCNMsmdsIndScrCountryIndex, attCNMsmdsGrpScrEntry=attCNMsmdsGrpScrEntry, attCNMsmdsGrpScrSubscriberIndex=attCNMsmdsGrpScrSubscriberIndex, attCNMsmdsDisagreeLogTable=attCNMsmdsDisagreeLogTable, attCNMsmdsMemGrpEntry=attCNMsmdsMemGrpEntry, attCNMsmdsAddrSubscriberIndex=attCNMsmdsAddrSubscriberIndex, attCNMsmdsDisagreeLogTimeStamp=attCNMsmdsDisagreeLogTimeStamp, attCNMsmdsMemberAddress=attCNMsmdsMemberAddress, attCNMsmdsDisagreeLogSA=attCNMsmdsDisagreeLogSA, att_mgmt=att_mgmt, SMDSAddress=SMDSAddress, attCNMsmdsAddrIndexDescr=attCNMsmdsAddrIndexDescr, attCNMsmdsDisagreeInterval=attCNMsmdsDisagreeInterval, attCNMsmdsMemGrpMemberAreaIndex=attCNMsmdsMemGrpMemberAreaIndex, attCNMsmdsDisagreeLogDA=attCNMsmdsDisagreeLogDA, attCNMsmdsDestinationSNIUnavailableCounts=attCNMsmdsDestinationSNIUnavailableCounts, attCNMsmdsDisagreeMaxIntervals=attCNMsmdsDisagreeMaxIntervals, attCNMsmdsMCDUsExceededAtIngressCounts=attCNMsmdsMCDUsExceededAtIngressCounts, attCNMsmdsGrpMemMemberSubscriberIndex=attCNMsmdsGrpMemMemberSubscriberIndex, attCNMsmdsGroupScreenMode=attCNMsmdsGroupScreenMode, attCNMsmdsAddrTable=attCNMsmdsAddrTable, attCNMsmdsIndScrSubscriberIndex=attCNMsmdsIndScrSubscriberIndex, attCNMsmdsMemGrpGroupSubscriberIndex=attCNMsmdsMemGrpGroupSubscriberIndex, attCNMsmdsGrpMemEntry=attCNMsmdsGrpMemEntry, att_cnm=att_cnm, attCNMsmdsIndScrTable=attCNMsmdsIndScrTable, attCNMsmdsIndScrIndex=attCNMsmdsIndScrIndex, attCNMsmdsAddrCountryIndex=attCNMsmdsAddrCountryIndex, attCNMsmdsIndivScreenMode=attCNMsmdsIndivScreenMode, attCNMsmdsDisagreeIndex=attCNMsmdsDisagreeIndex, attCNMsmdsGrpMemMemberAreaIndex=attCNMsmdsGrpMemMemberAreaIndex, att_cnm_smds=att_cnm_smds, attCNMsmdsMemGrpTable=attCNMsmdsMemGrpTable, attCNMsmdsDisagreeIntervalLen=attCNMsmdsDisagreeIntervalLen, attCNMsmdsGrpMemGroupCountryIndex=attCNMsmdsGrpMemGroupCountryIndex, attCNMsmdsSAScreenViolations=attCNMsmdsSAScreenViolations, attCNMsmdsIndivScreenAddress=attCNMsmdsIndivScreenAddress, attCNMsmdsGrpMemGroupAreaIndex=attCNMsmdsGrpMemGroupAreaIndex, attCNMsmdsConfigIndex=attCNMsmdsConfigIndex, att_products=att_products, attCNMsmdsMCDUsOut=attCNMsmdsMCDUsOut, attCNMsmdsGrpMemMemberCountryIndex=attCNMsmdsGrpMemMemberCountryIndex, attCNMsmdsGrpScrAreaIndex=attCNMsmdsGrpScrAreaIndex, attCNMsmdsIndScrEntry=attCNMsmdsIndScrEntry, attCNMsmdsGrpMemTable=attCNMsmdsGrpMemTable, att_cnmAgent=att_cnmAgent, attCNMsmdsAccessClassExceededCounts=attCNMsmdsAccessClassExceededCounts, attCNMsmdsDAScreenViolations=attCNMsmdsDAScreenViolations, attCNMsmdsGroupScreenAddress=attCNMsmdsGroupScreenAddress, attCNMsmdsConfigEntry=attCNMsmdsConfigEntry, attCNMsmdsAddrEntry=attCNMsmdsAddrEntry, attCNMsmdsAddrAreaIndex=attCNMsmdsAddrAreaIndex, att_2=att_2)
