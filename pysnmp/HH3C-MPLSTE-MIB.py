#
# PySNMP MIB module HH3C-MPLSTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MPLSTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Counter32, Gauge32, Counter64, IpAddress, ObjectIdentity, iso, NotificationType, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity", "iso", "NotificationType", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
hh3cMplsTe = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 143))
hh3cMplsTe.setRevisions(('2013-06-13 18:00',))
if mibBuilder.loadTexts: hh3cMplsTe.setLastUpdated('201306131800Z')
if mibBuilder.loadTexts: hh3cMplsTe.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cMplsTeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1))
hh3cMplsTeScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 1))
hh3cMplsTeStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMplsTeStatus.setStatus('current')
hh3cMplsTeRsvpStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMplsTeRsvpStatus.setStatus('current')
hh3cMplsTeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2), )
if mibBuilder.loadTexts: hh3cMplsTeTable.setStatus('current')
hh3cMplsTeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1), ).setIndexNames((0, "HH3C-MPLSTE-MIB", "hh3cMplsTeIndex"))
if mibBuilder.loadTexts: hh3cMplsTeEntry.setStatus('current')
hh3cMplsTeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: hh3cMplsTeIndex.setStatus('current')
hh3cMplsTeCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsTeCapability.setStatus('current')
hh3cMplsTeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsTeRowStatus.setStatus('current')
hh3cMplsTeRsvpTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3), )
if mibBuilder.loadTexts: hh3cMplsTeRsvpTable.setStatus('current')
hh3cMplsTeRsvpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1), ).setIndexNames((0, "HH3C-MPLSTE-MIB", "hh3cMplsTeRsvpIndex"))
if mibBuilder.loadTexts: hh3cMplsTeRsvpEntry.setStatus('current')
hh3cMplsTeRsvpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: hh3cMplsTeRsvpIndex.setStatus('current')
hh3cMplsTeRsvpCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsTeRsvpCapability.setStatus('current')
hh3cMplsTeRsvpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 143, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMplsTeRsvpRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-MPLSTE-MIB", hh3cMplsTeEntry=hh3cMplsTeEntry, hh3cMplsTeRowStatus=hh3cMplsTeRowStatus, hh3cMplsTeCapability=hh3cMplsTeCapability, hh3cMplsTeRsvpTable=hh3cMplsTeRsvpTable, hh3cMplsTeIndex=hh3cMplsTeIndex, hh3cMplsTeRsvpIndex=hh3cMplsTeRsvpIndex, hh3cMplsTeObjects=hh3cMplsTeObjects, hh3cMplsTeStatus=hh3cMplsTeStatus, hh3cMplsTeRsvpEntry=hh3cMplsTeRsvpEntry, hh3cMplsTeTable=hh3cMplsTeTable, hh3cMplsTeScalarGroup=hh3cMplsTeScalarGroup, hh3cMplsTe=hh3cMplsTe, PYSNMP_MODULE_ID=hh3cMplsTe, hh3cMplsTeRsvpCapability=hh3cMplsTeRsvpCapability, hh3cMplsTeRsvpRowStatus=hh3cMplsTeRsvpRowStatus, hh3cMplsTeRsvpStatus=hh3cMplsTeRsvpStatus)
