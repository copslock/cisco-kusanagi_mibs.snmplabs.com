#
# PySNMP MIB module ACD-SMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACD-SMAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:57:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, IpAddress, Integer32, Counter32, TimeTicks, Counter64, Gauge32, ObjectIdentity, Bits, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "IpAddress", "Integer32", "Counter32", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "Bits", "MibIdentifier", "Unsigned32")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
acdSmap = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 8))
acdSmap.setRevisions(('2008-10-01 01:00', '2008-06-15 01:00',))
if mibBuilder.loadTexts: acdSmap.setLastUpdated('200810010100Z')
if mibBuilder.loadTexts: acdSmap.setOrganization('Accedian Networks, Inc.')
acdSmapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 0))
acdSmapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1))
acdSmapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2))
acdSmapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1))
acdSmapCoSProfTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1), )
if mibBuilder.loadTexts: acdSmapCoSProfTable.setStatus('current')
acdSmapCoSProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapCoSProfID"))
if mibBuilder.loadTexts: acdSmapCoSProfEntry.setStatus('current')
acdSmapCoSProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSmapCoSProfID.setStatus('current')
acdSmapCoSProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfRowStatus.setStatus('current')
acdSmapCoSProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfName.setStatus('current')
acdSmapCoSProfType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pcp", 1), ("dscp", 2), ("pre", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfType.setStatus('current')
acdSmapCoSProfDecodeDropBit = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfDecodeDropBit.setStatus('current')
acdSmapCoSProfEncodeDropBit = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfEncodeDropBit.setStatus('current')
acdSmapCoSProfCodePointTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2), )
if mibBuilder.loadTexts: acdSmapCoSProfCodePointTable.setStatus('current')
acdSmapCoSProfCodePointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapCoSProfID"), (0, "ACD-SMAP-MIB", "acdSmapCoSProfCodePointID"))
if mibBuilder.loadTexts: acdSmapCoSProfCodePointEntry.setStatus('current')
acdSmapCoSProfCodePointID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdSmapCoSProfCodePointID.setStatus('current')
acdSmapCoSProfCodePointPreMarkingColor = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2))).clone('green')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointPreMarkingColor.setStatus('current')
acdSmapCoSProfCodePointGreenOut = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointGreenOut.setStatus('current')
acdSmapCoSProfCodePointYellowOut = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointYellowOut.setStatus('current')
acdSmapRegSetTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3), )
if mibBuilder.loadTexts: acdSmapRegSetTable.setStatus('current')
acdSmapRegSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapRegSetID"))
if mibBuilder.loadTexts: acdSmapRegSetEntry.setStatus('current')
acdSmapRegSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSmapRegSetID.setStatus('current')
acdSmapRegSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetRowStatus.setStatus('current')
acdSmapRegSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetName.setStatus('current')
acdSmapRegSetType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pcp", 1), ("dscp", 2), ("pre", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetType.setStatus('current')
acdSmapRegSetCodePointTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4), )
if mibBuilder.loadTexts: acdSmapRegSetCodePointTable.setStatus('current')
acdSmapRegSetCodePointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapRegSetID"), (0, "ACD-SMAP-MIB", "acdSmapRegSetCodePointID"))
if mibBuilder.loadTexts: acdSmapRegSetCodePointEntry.setStatus('current')
acdSmapRegSetCodePointID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdSmapRegSetCodePointID.setStatus('current')
acdSmapRegSetCodePointRegulatorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorID.setStatus('current')
acdSmapRegSetCodePointRegulatorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorEnable.setStatus('current')
acdSmapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1))
acdSmapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2))
acdSmapCoSProfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 1)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfRowStatus"), ("ACD-SMAP-MIB", "acdSmapCoSProfName"), ("ACD-SMAP-MIB", "acdSmapCoSProfType"), ("ACD-SMAP-MIB", "acdSmapCoSProfDecodeDropBit"), ("ACD-SMAP-MIB", "acdSmapCoSProfEncodeDropBit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCoSProfGroup = acdSmapCoSProfGroup.setStatus('current')
acdSmapCoSProfCodePointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 2)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfCodePointPreMarkingColor"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGreenOut"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointYellowOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCoSProfCodePointGroup = acdSmapCoSProfCodePointGroup.setStatus('current')
acdSmapRegSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 3)).setObjects(("ACD-SMAP-MIB", "acdSmapRegSetRowStatus"), ("ACD-SMAP-MIB", "acdSmapRegSetName"), ("ACD-SMAP-MIB", "acdSmapRegSetType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapRegSetGroup = acdSmapRegSetGroup.setStatus('current')
acdSmapRegSetCodePointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 4)).setObjects(("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorID"), ("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapRegSetCodePointGroup = acdSmapRegSetCodePointGroup.setStatus('current')
acdSmapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1, 1)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfGroup"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGroup"), ("ACD-SMAP-MIB", "acdSmapRegSetGroup"), ("ACD-SMAP-MIB", "acdSmapRegSetCodePointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCompliance = acdSmapCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-SMAP-MIB", acdSmapRegSetTable=acdSmapRegSetTable, acdSmapCoSProfEncodeDropBit=acdSmapCoSProfEncodeDropBit, acdSmapGroups=acdSmapGroups, acdSmapCoSProfEntry=acdSmapCoSProfEntry, acdSmapMIBObjects=acdSmapMIBObjects, acdSmapRegSetRowStatus=acdSmapRegSetRowStatus, acdSmapCoSProfName=acdSmapCoSProfName, acdSmapCoSProfDecodeDropBit=acdSmapCoSProfDecodeDropBit, acdSmapCoSProfTable=acdSmapCoSProfTable, acdSmapCoSProfType=acdSmapCoSProfType, acdSmapRegSetEntry=acdSmapRegSetEntry, PYSNMP_MODULE_ID=acdSmap, acdSmapRegSetGroup=acdSmapRegSetGroup, acdSmapCoSProfCodePointGroup=acdSmapCoSProfCodePointGroup, acdSmapRegSetCodePointEntry=acdSmapRegSetCodePointEntry, acdSmap=acdSmap, acdSmapRegSetCodePointRegulatorID=acdSmapRegSetCodePointRegulatorID, acdSmapRegSetCodePointRegulatorEnable=acdSmapRegSetCodePointRegulatorEnable, acdSmapCoSProfCodePointID=acdSmapCoSProfCodePointID, acdSmapConfig=acdSmapConfig, acdSmapCoSProfGroup=acdSmapCoSProfGroup, acdSmapRegSetType=acdSmapRegSetType, acdSmapCoSProfCodePointPreMarkingColor=acdSmapCoSProfCodePointPreMarkingColor, acdSmapRegSetCodePointGroup=acdSmapRegSetCodePointGroup, acdSmapCompliances=acdSmapCompliances, acdSmapRegSetName=acdSmapRegSetName, acdSmapCoSProfCodePointYellowOut=acdSmapCoSProfCodePointYellowOut, acdSmapConformance=acdSmapConformance, acdSmapCoSProfID=acdSmapCoSProfID, acdSmapRegSetID=acdSmapRegSetID, acdSmapRegSetCodePointID=acdSmapRegSetCodePointID, acdSmapCoSProfRowStatus=acdSmapCoSProfRowStatus, acdSmapCoSProfCodePointGreenOut=acdSmapCoSProfCodePointGreenOut, acdSmapCompliance=acdSmapCompliance, acdSmapCoSProfCodePointTable=acdSmapCoSProfCodePointTable, acdSmapCoSProfCodePointEntry=acdSmapCoSProfCodePointEntry, acdSmapRegSetCodePointTable=acdSmapRegSetCodePointTable, acdSmapNotifications=acdSmapNotifications)
