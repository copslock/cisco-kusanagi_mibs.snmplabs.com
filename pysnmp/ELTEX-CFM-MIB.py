#
# PySNMP MIB module ELTEX-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-CFM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
Dot1agCfmMpDirection, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMpDirection")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
VlanId, VlanIdOrNone = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "VlanIdOrNone")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Bits, Integer32, IpAddress, NotificationType, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Integer32", "IpAddress", "NotificationType", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Counter32", "ObjectIdentity")
MacAddress, TextualConvention, DisplayString, RowStatus, TAddress, TDomain, TimeInterval, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus", "TAddress", "TDomain", "TimeInterval", "TimeStamp", "TruthValue")
eltexCfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 36))
eltexCfmMIB.setRevisions(('2013-03-19 00:00',))
if mibBuilder.loadTexts: eltexCfmMIB.setLastUpdated('201303190000Z')
if mibBuilder.loadTexts: eltexCfmMIB.setOrganization('Eltex, Ent.')
eltexCfmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 36, 0))
eltexCfmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 36, 1))
eltexCfmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 36, 2))
eltexCfmMd = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 36, 1, 1))
eltexCfmMa = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 36, 1, 2))
eltexCfmMdTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1), )
if mibBuilder.loadTexts: eltexCfmMdTable.setStatus('current')
eltexCfmMdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1), ).setIndexNames((0, "ELTEX-CFM-MIB", "eltexCfmMdName"))
if mibBuilder.loadTexts: eltexCfmMdEntry.setStatus('current')
eltexCfmMdName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: eltexCfmMdName.setStatus('current')
eltexCfmMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltexCfmMdIndex.setStatus('current')
eltexCfmMdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 36, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltexCfmMdRowStatus.setStatus('current')
eltexCfmMaTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1), )
if mibBuilder.loadTexts: eltexCfmMaTable.setStatus('current')
eltexCfmMaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1), ).setIndexNames((0, "ELTEX-CFM-MIB", "eltexCfmMdIndex"), (0, "ELTEX-CFM-MIB", "eltexCfmMaIndex"))
if mibBuilder.loadTexts: eltexCfmMaEntry.setStatus('current')
eltexCfmMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: eltexCfmMaIndex.setStatus('current')
eltexCfmMaDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1, 2), Dot1agCfmMpDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltexCfmMaDirection.setStatus('current')
eltexCfmMaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 36, 1, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltexCfmMaRowStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-CFM-MIB", eltexCfmMIBObjects=eltexCfmMIBObjects, eltexCfmMdTable=eltexCfmMdTable, eltexCfmMdEntry=eltexCfmMdEntry, eltexCfmMaTable=eltexCfmMaTable, eltexCfmMaIndex=eltexCfmMaIndex, eltexCfmMd=eltexCfmMd, eltexCfmMa=eltexCfmMa, eltexCfmMdRowStatus=eltexCfmMdRowStatus, eltexCfmMdName=eltexCfmMdName, eltexCfmMaDirection=eltexCfmMaDirection, eltexCfmNotifications=eltexCfmNotifications, eltexCfmMaRowStatus=eltexCfmMaRowStatus, eltexCfmMaEntry=eltexCfmMaEntry, eltexCfmConformance=eltexCfmConformance, PYSNMP_MODULE_ID=eltexCfmMIB, eltexCfmMIB=eltexCfmMIB, eltexCfmMdIndex=eltexCfmMdIndex)
