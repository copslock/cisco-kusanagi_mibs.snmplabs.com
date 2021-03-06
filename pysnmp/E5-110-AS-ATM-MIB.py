#
# PySNMP MIB module E5-110-AS-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/E5-110-AS-ATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
accessSwitchCommonATM, = mibBuilder.importSymbols("E5-110-MIB", "accessSwitchCommonATM")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, IpAddress, iso, Gauge32, Bits, Integer32, ModuleIdentity, TimeTicks, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "IpAddress", "iso", "Gauge32", "Bits", "Integer32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
asMaxNumOfChannels = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asMaxNumOfChannels.setStatus('mandatory')
asChannelTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2), )
if mibBuilder.loadTexts: asChannelTable.setStatus('mandatory')
asChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "E5-110-AS-ATM-MIB", "asChannelVpi"), (0, "E5-110-AS-ATM-MIB", "asChannelVci"))
if mibBuilder.loadTexts: asChannelEntry.setStatus('mandatory')
asChannelVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: asChannelVpi.setStatus('mandatory')
asChannelVci = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: asChannelVci.setStatus('mandatory')
asChannelPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 3), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelPvid.setStatus('mandatory')
asChannelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelPriority.setStatus('mandatory')
asChannelProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfile.setStatus('mandatory')
asChannelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelRowStatus.setStatus('mandatory')
asMaxNumOfChannelProfiles = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asMaxNumOfChannelProfiles.setStatus('mandatory')
asChannelProfileTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6), )
if mibBuilder.loadTexts: asChannelProfileTable.setStatus('mandatory')
asChannelProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1), ).setIndexNames((1, "E5-110-AS-ATM-MIB", "asChannelProfileName"))
if mibBuilder.loadTexts: asChannelProfileEntry.setStatus('mandatory')
asChannelProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: asChannelProfileName.setStatus('mandatory')
asChannelProfileEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llc", 1), ("vc", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileEncap.setStatus('mandatory')
asChannelProfileAAL = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileAAL.setStatus('mandatory')
asChannelProfileClass = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cbr", 1), ("rt-vbr", 2), ("nrt-vbr", 3), ("ubr", 4), ("abr", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileClass.setStatus('mandatory')
asChannelProfilePcr = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfilePcr.setStatus('mandatory')
asChannelProfileCdvt = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileCdvt.setStatus('mandatory')
asChannelProfileScrMcr = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileScrMcr.setStatus('mandatory')
asChannelProfileBt = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileBt.setStatus('mandatory')
asChannelProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileRowStatus.setStatus('mandatory')
asChannelStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7), )
if mibBuilder.loadTexts: asChannelStatusTable.setStatus('mandatory')
asChannelStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "E5-110-AS-ATM-MIB", "asChannelVpi"), (0, "E5-110-AS-ATM-MIB", "asChannelVci"))
if mibBuilder.loadTexts: asChannelStatusEntry.setStatus('mandatory')
asChannelTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelTxPackets.setStatus('mandatory')
asChannelRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelRxPackets.setStatus('mandatory')
asChannelTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelTxCells.setStatus('mandatory')
asChannelRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelRxCells.setStatus('mandatory')
asMaxNumOfIpqosProfiles = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asMaxNumOfIpqosProfiles.setStatus('mandatory')
asIpqosProfileTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9), )
if mibBuilder.loadTexts: asIpqosProfileTable.setStatus('mandatory')
asIpqosProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1), ).setIndexNames((1, "E5-110-AS-ATM-MIB", "asIpqosProfileName"))
if mibBuilder.loadTexts: asIpqosProfileEntry.setStatus('mandatory')
asIpqosProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asIpqosProfileName.setStatus('mandatory')
asIpqosProfileEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llc", 1), ("vc", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileEncap.setStatus('mandatory')
asIpqosProfileQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("four", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileQueueNumber.setStatus('mandatory')
asIpqosProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asIpqosProfileRowStatus.setStatus('mandatory')
asIpqosProfileQueueTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10), )
if mibBuilder.loadTexts: asIpqosProfileQueueTable.setStatus('mandatory')
asIpqosProfileQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1), ).setIndexNames((0, "E5-110-AS-ATM-MIB", "asIpqosProfileName"), (1, "E5-110-AS-ATM-MIB", "asIpqosProfileQueueIndex"))
if mibBuilder.loadTexts: asIpqosProfileQueueEntry.setStatus('mandatory')
asIpqosProfileQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asIpqosProfileQueueIndex.setStatus('mandatory')
asIpqosProfileAAL = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileAAL.setStatus('mandatory')
asIpqosProfileLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ubr", 0), ("nrt-vbr", 1), ("rt-vbr", 2), ("cbr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileLevel.setStatus('mandatory')
asIpqosProfileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileRate.setStatus('mandatory')
asShapingMode = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("atm", 1), ("packet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asShapingMode.setStatus('mandatory')
mibBuilder.exportSymbols("E5-110-AS-ATM-MIB", asIpqosProfileQueueTable=asIpqosProfileQueueTable, asChannelProfileEntry=asChannelProfileEntry, asChannelProfileTable=asChannelProfileTable, asChannelProfileScrMcr=asChannelProfileScrMcr, asChannelProfileBt=asChannelProfileBt, asIpqosProfileEntry=asIpqosProfileEntry, asChannelPriority=asChannelPriority, asChannelTable=asChannelTable, asIpqosProfileQueueIndex=asIpqosProfileQueueIndex, asIpqosProfileName=asIpqosProfileName, asIpqosProfileEncap=asIpqosProfileEncap, asChannelPvid=asChannelPvid, asChannelTxCells=asChannelTxCells, asChannelVci=asChannelVci, asChannelStatusEntry=asChannelStatusEntry, asIpqosProfileQueueNumber=asIpqosProfileQueueNumber, asChannelRowStatus=asChannelRowStatus, asChannelStatusTable=asChannelStatusTable, asIpqosProfileTable=asIpqosProfileTable, asChannelTxPackets=asChannelTxPackets, asMaxNumOfIpqosProfiles=asMaxNumOfIpqosProfiles, asChannelProfileEncap=asChannelProfileEncap, asMaxNumOfChannelProfiles=asMaxNumOfChannelProfiles, asChannelProfileName=asChannelProfileName, asIpqosProfileAAL=asIpqosProfileAAL, asIpqosProfileRate=asIpqosProfileRate, asShapingMode=asShapingMode, asMaxNumOfChannels=asMaxNumOfChannels, asChannelProfileAAL=asChannelProfileAAL, asChannelRxPackets=asChannelRxPackets, asChannelEntry=asChannelEntry, asChannelProfilePcr=asChannelProfilePcr, asIpqosProfileQueueEntry=asIpqosProfileQueueEntry, asChannelProfileCdvt=asChannelProfileCdvt, asIpqosProfileRowStatus=asIpqosProfileRowStatus, asChannelProfileRowStatus=asChannelProfileRowStatus, asChannelVpi=asChannelVpi, asChannelProfile=asChannelProfile, asIpqosProfileLevel=asIpqosProfileLevel, asChannelProfileClass=asChannelProfileClass, asChannelRxCells=asChannelRxCells)
