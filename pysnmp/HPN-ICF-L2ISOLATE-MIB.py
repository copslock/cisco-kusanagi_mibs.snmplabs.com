#
# PySNMP MIB module HPN-ICF-L2ISOLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-L2ISOLATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Counter32, ModuleIdentity, NotificationType, Bits, Counter64, MibIdentifier, ObjectIdentity, iso, Gauge32, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter32", "ModuleIdentity", "NotificationType", "Bits", "Counter64", "MibIdentifier", "ObjectIdentity", "iso", "Gauge32", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, RowStatus, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention", "MacAddress")
hpnicfL2Isolate = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103))
hpnicfL2Isolate.setRevisions(('2009-05-06 00:00',))
if mibBuilder.loadTexts: hpnicfL2Isolate.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: hpnicfL2Isolate.setOrganization('')
hpnicfL2IsolateObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1))
hpnicfL2IsolateEnableTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1), )
if mibBuilder.loadTexts: hpnicfL2IsolateEnableTable.setStatus('current')
hpnicfL2IsolateEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-L2ISOLATE-MIB", "hpnicfL2IsolateVLANIndex"))
if mibBuilder.loadTexts: hpnicfL2IsolateEnableEntry.setStatus('current')
hpnicfL2IsolateVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hpnicfL2IsolateVLANIndex.setStatus('current')
hpnicfL2IsolateEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfL2IsolateEnable.setStatus('current')
hpnicfL2IsolatePermitMACTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2), )
if mibBuilder.loadTexts: hpnicfL2IsolatePermitMACTable.setStatus('current')
hpnicfL2IsolatePermitMACEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-L2ISOLATE-MIB", "hpnicfL2IsolateVLANIndex"), (0, "HPN-ICF-L2ISOLATE-MIB", "hpnicfL2IsoLatePermitMAC"))
if mibBuilder.loadTexts: hpnicfL2IsolatePermitMACEntry.setStatus('current')
hpnicfL2IsoLatePermitMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfL2IsoLatePermitMAC.setStatus('current')
hpnicfL2IsoLatePermitMACRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfL2IsoLatePermitMACRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-L2ISOLATE-MIB", hpnicfL2IsolatePermitMACTable=hpnicfL2IsolatePermitMACTable, hpnicfL2IsolateObject=hpnicfL2IsolateObject, hpnicfL2IsolateEnableTable=hpnicfL2IsolateEnableTable, hpnicfL2IsoLatePermitMACRowStatus=hpnicfL2IsoLatePermitMACRowStatus, hpnicfL2IsolateEnable=hpnicfL2IsolateEnable, hpnicfL2IsoLatePermitMAC=hpnicfL2IsoLatePermitMAC, PYSNMP_MODULE_ID=hpnicfL2Isolate, hpnicfL2IsolateEnableEntry=hpnicfL2IsolateEnableEntry, hpnicfL2IsolateVLANIndex=hpnicfL2IsolateVLANIndex, hpnicfL2IsolatePermitMACEntry=hpnicfL2IsolatePermitMACEntry, hpnicfL2Isolate=hpnicfL2Isolate)
