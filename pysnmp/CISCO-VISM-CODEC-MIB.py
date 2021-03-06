#
# PySNMP MIB module CISCO-VISM-CODEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-CODEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
voice, = mibBuilder.importSymbols("BASIS-MIB", "voice")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, MibIdentifier, Integer32, iso, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ObjectIdentity, Bits, Counter64, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Integer32", "iso", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ObjectIdentity", "Bits", "Counter64", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismCodecMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 97))
ciscoVismCodecMIB.setRevisions(('2005-05-24 00:00', '2004-01-07 00:00',))
if mibBuilder.loadTexts: ciscoVismCodecMIB.setLastUpdated('200505240000Z')
if mibBuilder.loadTexts: ciscoVismCodecMIB.setOrganization('Cisco Systems, Inc.')
vismCodecTemplateCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7))
vismCodecCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18))
vismCodecCnfTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1), )
if mibBuilder.loadTexts: vismCodecCnfTable.setStatus('current')
vismCodecCnfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1), ).setIndexNames((0, "CISCO-VISM-CODEC-MIB", "vismCodecCnfIndex"))
if mibBuilder.loadTexts: vismCodecCnfEntry.setStatus('current')
vismCodecCnfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("g711u", 1), ("g711a", 2), ("g726r32000", 3), ("g729a", 4), ("g729ab", 5), ("clearChannel", 6), ("g726r16000", 7), ("g726r24000", 8), ("g726r40000", 9), ("g723h", 11), ("g723ah", 12), ("g723l", 13), ("g723al", 14), ("lossless", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCodecCnfIndex.setStatus('current')
vismCodecName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCodecName.setStatus('current')
vismCodecPktPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 20, 30, 40, 60))).clone(namedValues=NamedValues(("ten", 10), ("twenty", 20), ("thirty", 30), ("fourty", 40), ("sixty", 60)))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCodecPktPeriod.setStatus('current')
vismCodecPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCodecPreference.setStatus('current')
vismCodecString = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCodecString.setStatus('current')
vismCodecIanaType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismCodecIanaType.setStatus('current')
vismAltCodecString1 = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismAltCodecString1.setStatus('current')
vismAltCodecString2 = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismAltCodecString2.setStatus('current')
vismAltCodecString3 = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 18, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismAltCodecString3.setStatus('current')
vismCodecTemplateCnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1), )
if mibBuilder.loadTexts: vismCodecTemplateCnfGrpTable.setStatus('current')
vismCodecTemplateCnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1), ).setIndexNames((0, "CISCO-VISM-CODEC-MIB", "vismCodecTemplateNum"))
if mibBuilder.loadTexts: vismCodecTemplateCnfGrpEntry.setStatus('current')
vismCodecTemplateNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCodecTemplateNum.setStatus('current')
vismCodecSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCodecSupported.setStatus('current')
vismCodecTemplateMaxChanCount = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismCodecTemplateMaxChanCount.setStatus('current')
ciscoVismCodecMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 97, 2))
ciscoVismCodecMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 1))
ciscoVismCodecMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2))
ciscoVismCodecCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 1, 1)).setObjects(("CISCO-VISM-CODEC-MIB", "ciscoVismCodecCnfGroup"), ("CISCO-VISM-CODEC-MIB", "ciscoVismCodecTemplateGrp"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCodecCompliance = ciscoVismCodecCompliance.setStatus('deprecated')
ciscoVismCodecComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 1, 2)).setObjects(("CISCO-VISM-CODEC-MIB", "ciscoVismCodecCnfGroup"), ("CISCO-VISM-CODEC-MIB", "ciscoVismCodecTemplateGrp"), ("CISCO-VISM-CODEC-MIB", "ciscoAltVismCodecCnfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCodecComplianceRev1 = ciscoVismCodecComplianceRev1.setStatus('current')
ciscoVismCodecCnfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2, 1)).setObjects(("CISCO-VISM-CODEC-MIB", "vismCodecCnfIndex"), ("CISCO-VISM-CODEC-MIB", "vismCodecName"), ("CISCO-VISM-CODEC-MIB", "vismCodecPktPeriod"), ("CISCO-VISM-CODEC-MIB", "vismCodecPreference"), ("CISCO-VISM-CODEC-MIB", "vismCodecString"), ("CISCO-VISM-CODEC-MIB", "vismCodecIanaType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCodecCnfGroup = ciscoVismCodecCnfGroup.setStatus('current')
ciscoVismCodecTemplateGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2, 2)).setObjects(("CISCO-VISM-CODEC-MIB", "vismCodecTemplateNum"), ("CISCO-VISM-CODEC-MIB", "vismCodecSupported"), ("CISCO-VISM-CODEC-MIB", "vismCodecTemplateMaxChanCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismCodecTemplateGrp = ciscoVismCodecTemplateGrp.setStatus('current')
ciscoAltVismCodecCnfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 97, 2, 2, 3)).setObjects(("CISCO-VISM-CODEC-MIB", "vismAltCodecString1"), ("CISCO-VISM-CODEC-MIB", "vismAltCodecString2"), ("CISCO-VISM-CODEC-MIB", "vismAltCodecString3"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAltVismCodecCnfGroup = ciscoAltVismCodecCnfGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-CODEC-MIB", vismCodecString=vismCodecString, ciscoVismCodecCompliance=ciscoVismCodecCompliance, vismCodecPktPeriod=vismCodecPktPeriod, vismCodecCnfEntry=vismCodecCnfEntry, ciscoVismCodecTemplateGrp=ciscoVismCodecTemplateGrp, ciscoVismCodecMIBCompliances=ciscoVismCodecMIBCompliances, ciscoVismCodecCnfGroup=ciscoVismCodecCnfGroup, vismAltCodecString2=vismAltCodecString2, ciscoAltVismCodecCnfGroup=ciscoAltVismCodecCnfGroup, vismCodecName=vismCodecName, vismCodecTemplateCnfGrpEntry=vismCodecTemplateCnfGrpEntry, vismCodecTemplateNum=vismCodecTemplateNum, vismCodecCnfIndex=vismCodecCnfIndex, ciscoVismCodecMIBConformance=ciscoVismCodecMIBConformance, ciscoVismCodecMIBGroups=ciscoVismCodecMIBGroups, vismCodecCnfTable=vismCodecCnfTable, vismCodecTemplateCnfGrpTable=vismCodecTemplateCnfGrpTable, vismCodecSupported=vismCodecSupported, ciscoVismCodecComplianceRev1=ciscoVismCodecComplianceRev1, vismCodecPreference=vismCodecPreference, vismCodecIanaType=vismCodecIanaType, PYSNMP_MODULE_ID=ciscoVismCodecMIB, vismCodecCnfGrp=vismCodecCnfGrp, ciscoVismCodecMIB=ciscoVismCodecMIB, vismAltCodecString1=vismAltCodecString1, vismCodecTemplateMaxChanCount=vismCodecTemplateMaxChanCount, vismCodecTemplateCnfGrp=vismCodecTemplateCnfGrp, vismAltCodecString3=vismAltCodecString3)
