#
# PySNMP MIB module HH3C-VMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-VMAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:17:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ModuleIdentity, ObjectIdentity, TimeTicks, Gauge32, iso, NotificationType, Counter64, IpAddress, Counter32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Counter64", "IpAddress", "Counter32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
hh3cVmap = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 138))
hh3cVmap.setRevisions(('2013-03-08 00:00',))
if mibBuilder.loadTexts: hh3cVmap.setLastUpdated('201303080000Z')
if mibBuilder.loadTexts: hh3cVmap.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cVMAPNNITable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 138, 1), )
if mibBuilder.loadTexts: hh3cVMAPNNITable.setStatus('current')
hh3cVMAPNNIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 138, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cVMAPNNIEntry.setStatus('current')
hh3cVMAPNNIState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cVMAPNNIState.setStatus('current')
hh3cVMAP1to1Table = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 138, 2), )
if mibBuilder.loadTexts: hh3cVMAP1to1Table.setStatus('current')
hh3cVMAP1to1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-VMAP-MIB", "hh3cVMAP1to1Vlan"))
if mibBuilder.loadTexts: hh3cVMAP1to1Entry.setStatus('current')
hh3cVMAP1to1Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cVMAP1to1Vlan.setStatus('current')
hh3cVMAP1to1TranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP1to1TranslatedVlan.setStatus('current')
hh3cVMAP1to1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP1to1RowStatus.setStatus('current')
hh3cVMAPNto1RangeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 138, 3), )
if mibBuilder.loadTexts: hh3cVMAPNto1RangeTable.setStatus('current')
hh3cVMAPNto1RangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-VMAP-MIB", "hh3cVMAPNto1StartVlan"))
if mibBuilder.loadTexts: hh3cVMAPNto1RangeEntry.setStatus('current')
hh3cVMAPNto1StartVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cVMAPNto1StartVlan.setStatus('current')
hh3cVMAPNto1EndVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAPNto1EndVlan.setStatus('current')
hh3cVMAPNto1RangeTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAPNto1RangeTranslatedVlan.setStatus('current')
hh3cVMAPNto1RangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAPNto1RangeRowStatus.setStatus('current')
hh3cVMAPNto1SingleTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 138, 4), )
if mibBuilder.loadTexts: hh3cVMAPNto1SingleTable.setStatus('current')
hh3cVMAPNto1SingleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-VMAP-MIB", "hh3cVMAPNto1Vlan"))
if mibBuilder.loadTexts: hh3cVMAPNto1SingleEntry.setStatus('current')
hh3cVMAPNto1Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cVMAPNto1Vlan.setStatus('current')
hh3cVMAPNto1SingleTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAPNto1SingleTranslatedVlan.setStatus('current')
hh3cVMAPNto1SingleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAPNto1SingleRowStatus.setStatus('current')
hh3cVMAP1to2RangeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 138, 5), )
if mibBuilder.loadTexts: hh3cVMAP1to2RangeTable.setStatus('current')
hh3cVMAP1to2RangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-VMAP-MIB", "hh3cVMAP1to2StartVlan"))
if mibBuilder.loadTexts: hh3cVMAP1to2RangeEntry.setStatus('current')
hh3cVMAP1to2StartVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cVMAP1to2StartVlan.setStatus('current')
hh3cVMAP1to2EndVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP1to2EndVlan.setStatus('current')
hh3cVMAP1to2RangeNestedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP1to2RangeNestedVlan.setStatus('current')
hh3cVMAP1to2RangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP1to2RangeRowStatus.setStatus('current')
hh3cVMAP1to2SingleTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 138, 6), )
if mibBuilder.loadTexts: hh3cVMAP1to2SingleTable.setStatus('current')
hh3cVMAP1to2SingleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-VMAP-MIB", "hh3cVMAP1to2Vlan"))
if mibBuilder.loadTexts: hh3cVMAP1to2SingleEntry.setStatus('current')
hh3cVMAP1to2Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cVMAP1to2Vlan.setStatus('current')
hh3cVMAP1to2SingleNestedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP1to2SingleNestedVlan.setStatus('current')
hh3cVMAP1to2SingleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP1to2SingleRowStatus.setStatus('current')
hh3cVMAP2to2Table = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 138, 7), )
if mibBuilder.loadTexts: hh3cVMAP2to2Table.setStatus('current')
hh3cVMAP2to2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-VMAP-MIB", "hh3cVMAP2to2OuterVlan"), (0, "HH3C-VMAP-MIB", "hh3cVMAP2to2InnerVlan"))
if mibBuilder.loadTexts: hh3cVMAP2to2Entry.setStatus('current')
hh3cVMAP2to2OuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cVMAP2to2OuterVlan.setStatus('current')
hh3cVMAP2to2InnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cVMAP2to2InnerVlan.setStatus('current')
hh3cVMAP2to2TranslatedOuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP2to2TranslatedOuterVlan.setStatus('current')
hh3cVMAP2to2TranslatedInnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP2to2TranslatedInnerVlan.setStatus('current')
hh3cVMAP2to2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 138, 7, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVMAP2to2RowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-VMAP-MIB", hh3cVMAPNto1StartVlan=hh3cVMAPNto1StartVlan, hh3cVMAP1to2RangeRowStatus=hh3cVMAP1to2RangeRowStatus, hh3cVMAPNto1Vlan=hh3cVMAPNto1Vlan, hh3cVMAP1to2RangeNestedVlan=hh3cVMAP1to2RangeNestedVlan, hh3cVMAPNto1RangeTable=hh3cVMAPNto1RangeTable, hh3cVMAPNto1SingleRowStatus=hh3cVMAPNto1SingleRowStatus, hh3cVMAPNto1RangeRowStatus=hh3cVMAPNto1RangeRowStatus, hh3cVMAPNNITable=hh3cVMAPNNITable, hh3cVMAP1to2StartVlan=hh3cVMAP1to2StartVlan, hh3cVMAP2to2TranslatedOuterVlan=hh3cVMAP2to2TranslatedOuterVlan, PYSNMP_MODULE_ID=hh3cVmap, hh3cVMAP1to2SingleNestedVlan=hh3cVMAP1to2SingleNestedVlan, hh3cVMAPNto1RangeTranslatedVlan=hh3cVMAPNto1RangeTranslatedVlan, hh3cVMAP1to1Vlan=hh3cVMAP1to1Vlan, hh3cVMAP2to2RowStatus=hh3cVMAP2to2RowStatus, hh3cVMAP1to2Vlan=hh3cVMAP1to2Vlan, hh3cVMAP2to2TranslatedInnerVlan=hh3cVMAP2to2TranslatedInnerVlan, hh3cVMAP1to2SingleEntry=hh3cVMAP1to2SingleEntry, hh3cVMAPNto1RangeEntry=hh3cVMAPNto1RangeEntry, hh3cVMAP2to2OuterVlan=hh3cVMAP2to2OuterVlan, hh3cVMAP1to2SingleTable=hh3cVMAP1to2SingleTable, hh3cVMAP1to2RangeEntry=hh3cVMAP1to2RangeEntry, hh3cVMAP1to1RowStatus=hh3cVMAP1to1RowStatus, hh3cVMAP1to2SingleRowStatus=hh3cVMAP1to2SingleRowStatus, hh3cVMAP1to1Table=hh3cVMAP1to1Table, hh3cVMAP2to2Entry=hh3cVMAP2to2Entry, hh3cVMAPNNIState=hh3cVMAPNNIState, hh3cVMAP1to1Entry=hh3cVMAP1to1Entry, hh3cVMAPNto1SingleTranslatedVlan=hh3cVMAPNto1SingleTranslatedVlan, hh3cVMAP1to2RangeTable=hh3cVMAP1to2RangeTable, hh3cVMAPNto1EndVlan=hh3cVMAPNto1EndVlan, hh3cVmap=hh3cVmap, hh3cVMAPNto1SingleTable=hh3cVMAPNto1SingleTable, hh3cVMAP2to2Table=hh3cVMAP2to2Table, hh3cVMAPNto1SingleEntry=hh3cVMAPNto1SingleEntry, hh3cVMAPNNIEntry=hh3cVMAPNNIEntry, hh3cVMAP1to2EndVlan=hh3cVMAP1to2EndVlan, hh3cVMAP1to1TranslatedVlan=hh3cVMAP1to1TranslatedVlan, hh3cVMAP2to2InnerVlan=hh3cVMAP2to2InnerVlan)
