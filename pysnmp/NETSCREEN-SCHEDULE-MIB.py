#
# PySNMP MIB module NETSCREEN-SCHEDULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SCHEDULE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
netscreenSchedule, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSchedule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, NotificationType, Unsigned32, IpAddress, Counter64, iso, Gauge32, ObjectIdentity, Bits, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "iso", "Gauge32", "ObjectIdentity", "Bits", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenScheduleMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 14, 0))
netscreenScheduleMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenScheduleMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenScheduleMibModule.setOrganization('Juniper Networks, Inc.')
nsSchOnceTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 14, 1), )
if mibBuilder.loadTexts: nsSchOnceTable.setStatus('current')
nsSchOnceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 14, 1, 1), ).setIndexNames((0, "NETSCREEN-SCHEDULE-MIB", "nsSchOnceIndex"))
if mibBuilder.loadTexts: nsSchOnceEntry.setStatus('current')
nsSchOnceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchOnceIndex.setStatus('current')
nsSchOnceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchOnceName.setStatus('current')
nsSchOnceStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchOnceStartTime.setStatus('current')
nsSchOnceStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchOnceStopTime.setStatus('current')
nsSchOnceComments = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchOnceComments.setStatus('current')
nsSchOnceVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchOnceVsys.setStatus('current')
nsSchRecurTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 14, 2), )
if mibBuilder.loadTexts: nsSchRecurTable.setStatus('current')
nsSchRecurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1), ).setIndexNames((0, "NETSCREEN-SCHEDULE-MIB", "nsSchRecurIndex"))
if mibBuilder.loadTexts: nsSchRecurEntry.setStatus('current')
nsSchRecurIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurIndex.setStatus('current')
nsSchRecurName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurName.setStatus('current')
nsSchRecurWeekday = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("sun", 0), ("mon", 1), ("tue", 2), ("wed", 3), ("thu", 4), ("fri", 5), ("sat", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurWeekday.setStatus('current')
nsSchRecurStartTime1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurStartTime1.setStatus('current')
nsSchRecurStopTime1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurStopTime1.setStatus('current')
nsSchRecurStartTime2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurStartTime2.setStatus('current')
nsSchRecurStopTime2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurStopTime2.setStatus('current')
nsSchRecurComments = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurComments.setStatus('current')
nsSchRecurVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 14, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSchRecurVsys.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SCHEDULE-MIB", nsSchOnceIndex=nsSchOnceIndex, nsSchOnceTable=nsSchOnceTable, PYSNMP_MODULE_ID=netscreenScheduleMibModule, nsSchRecurEntry=nsSchRecurEntry, nsSchRecurComments=nsSchRecurComments, nsSchRecurVsys=nsSchRecurVsys, nsSchRecurWeekday=nsSchRecurWeekday, nsSchOnceName=nsSchOnceName, nsSchOnceVsys=nsSchOnceVsys, nsSchRecurStopTime1=nsSchRecurStopTime1, nsSchRecurTable=nsSchRecurTable, netscreenScheduleMibModule=netscreenScheduleMibModule, nsSchRecurStartTime2=nsSchRecurStartTime2, nsSchOnceEntry=nsSchOnceEntry, nsSchOnceStartTime=nsSchOnceStartTime, nsSchRecurStopTime2=nsSchRecurStopTime2, nsSchOnceComments=nsSchOnceComments, nsSchRecurIndex=nsSchRecurIndex, nsSchRecurName=nsSchRecurName, nsSchRecurStartTime1=nsSchRecurStartTime1, nsSchOnceStopTime=nsSchOnceStopTime)