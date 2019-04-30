#
# PySNMP MIB module URQLEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/URQLEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
urqlExt, = mibBuilder.importSymbols("APENT-MIB", "urqlExt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, ObjectIdentity, Bits, Counter32, MibIdentifier, Unsigned32, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "Unsigned32", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "ModuleIdentity", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
apUrqlExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 49, 1))
if mibBuilder.loadTexts: apUrqlExtMib.setLastUpdated('9906221000Z')
if mibBuilder.loadTexts: apUrqlExtMib.setOrganization('ArrowPoint Communications Inc.')
apUrqlTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2), )
if mibBuilder.loadTexts: apUrqlTable.setStatus('current')
apUrqlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1), ).setIndexNames((0, "URQLEXT-MIB", "apUrqlName"))
if mibBuilder.loadTexts: apUrqlEntry.setStatus('current')
apUrqlName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlName.setStatus('current')
apUrqlDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlDescription.setStatus('current')
apUrqlCreateType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apUrqlCreateType.setStatus('current')
apUrqlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlStatus.setStatus('current')
apUrqlEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlEnable.setStatus('current')
apUrqlDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlDomain.setStatus('current')
apUrqlExtTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 49, 3), )
if mibBuilder.loadTexts: apUrqlExtTable.setStatus('current')
apUrqlExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1), ).setIndexNames((0, "URQLEXT-MIB", "apUrqlName"), (0, "URQLEXT-MIB", "apUrqlExtUrlNumber"))
if mibBuilder.loadTexts: apUrqlExtEntry.setStatus('current')
apUrqlExtUrlNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlExtUrlNumber.setStatus('current')
apUrqlExtUrlName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 251))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlExtUrlName.setStatus('current')
apUrqlExtUrlDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlExtUrlDescription.setStatus('current')
apUrqlExtUrlCreateType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apUrqlExtUrlCreateType.setStatus('current')
apUrqlExtUrlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apUrqlExtUrlStatus.setStatus('current')
mibBuilder.exportSymbols("URQLEXT-MIB", apUrqlEnable=apUrqlEnable, apUrqlExtUrlStatus=apUrqlExtUrlStatus, apUrqlExtEntry=apUrqlExtEntry, apUrqlExtUrlCreateType=apUrqlExtUrlCreateType, apUrqlExtTable=apUrqlExtTable, apUrqlExtUrlNumber=apUrqlExtUrlNumber, apUrqlEntry=apUrqlEntry, apUrqlStatus=apUrqlStatus, apUrqlExtMib=apUrqlExtMib, apUrqlExtUrlDescription=apUrqlExtUrlDescription, apUrqlCreateType=apUrqlCreateType, apUrqlTable=apUrqlTable, apUrqlDomain=apUrqlDomain, apUrqlName=apUrqlName, apUrqlDescription=apUrqlDescription, apUrqlExtUrlName=apUrqlExtUrlName, PYSNMP_MODULE_ID=apUrqlExtMib)