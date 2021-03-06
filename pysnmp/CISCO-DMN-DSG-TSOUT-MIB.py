#
# PySNMP MIB module CISCO-DMN-DSG-TSOUT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-TSOUT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, IpAddress, TimeTicks, ObjectIdentity, iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, MibIdentifier, Counter32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "TimeTicks", "ObjectIdentity", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "MibIdentifier", "Counter32", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGTSOUT = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34))
ciscoDSGTSOUT.setRevisions(('2012-03-20 11:00', '2010-08-24 07:30',))
if mibBuilder.loadTexts: ciscoDSGTSOUT.setLastUpdated('201203201130Z')
if mibBuilder.loadTexts: ciscoDSGTSOUT.setOrganization('Cisco Systems, Inc.')
tsoutTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1), )
if mibBuilder.loadTexts: tsoutTable.setStatus('current')
tsoutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-TSOUT-MIB", "tsoutID"))
if mibBuilder.loadTexts: tsoutEntry.setStatus('current')
tsoutID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutID.setStatus('current')
tsoutInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutInstanceName.setStatus('current')
tsoutOutputMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noOutput", 1), ("passThrough", 2), ("serviceChannelOnly", 3), ("mapPassthrough", 4), ("mapserviceChannelOnly", 5), ("fullDpmControl", 6), ("transcoding", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutOutputMode.setStatus('current')
tsoutDescrambleMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deScrambled", 1), ("scrambled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutDescrambleMode.setStatus('current')
tsoutRateControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("user", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutRateControl.setStatus('current')
tsoutOutputRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 206000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutOutputRate.setStatus('current')
tsoutInsertNullPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutInsertNullPkt.setStatus('current')
tsoutMOIPOutputMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("noOutput", 1), ("passThrough", 2), ("serviceChannelsOnly", 3), ("mapPassthrough", 4), ("mapServiceChannelsOnly", 5), ("fullDpmControl", 6), ("transcoding", 7), ("sptsServiceChannelsOnly", 8), ("sptsMapServiceChannelsOnly", 9), ("sptsFullDpmControl", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsoutMOIPOutputMode.setStatus('current')
tsoutStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2), )
if mibBuilder.loadTexts: tsoutStatusTable.setStatus('current')
tsoutStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-TSOUT-MIB", "tsoutStatusID"))
if mibBuilder.loadTexts: tsoutStatusEntry.setStatus('current')
tsoutStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: tsoutStatusID.setStatus('current')
tsoutStatusInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutStatusInstanceName.setStatus('current')
tsoutStatusRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutStatusRate.setStatus('current')
tsoutStatusFree = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 34, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsoutStatusFree.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-TSOUT-MIB", tsoutID=tsoutID, tsoutDescrambleMode=tsoutDescrambleMode, ciscoDSGTSOUT=ciscoDSGTSOUT, PYSNMP_MODULE_ID=ciscoDSGTSOUT, tsoutStatusTable=tsoutStatusTable, tsoutOutputMode=tsoutOutputMode, tsoutStatusInstanceName=tsoutStatusInstanceName, tsoutOutputRate=tsoutOutputRate, tsoutStatusFree=tsoutStatusFree, tsoutStatusEntry=tsoutStatusEntry, tsoutRateControl=tsoutRateControl, tsoutInsertNullPkt=tsoutInsertNullPkt, tsoutMOIPOutputMode=tsoutMOIPOutputMode, tsoutInstanceName=tsoutInstanceName, tsoutStatusRate=tsoutStatusRate, tsoutStatusID=tsoutStatusID, tsoutEntry=tsoutEntry, tsoutTable=tsoutTable)
