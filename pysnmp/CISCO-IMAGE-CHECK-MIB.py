#
# PySNMP MIB module CISCO-IMAGE-CHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMAGE-CHECK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Counter64, ModuleIdentity, ObjectIdentity, NotificationType, Unsigned32, Counter32, Bits, TimeTicks, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter32", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoImageCheckMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99990))
if mibBuilder.loadTexts: ciscoImageCheckMIB.setLastUpdated('200305150000Z')
if mibBuilder.loadTexts: ciscoImageCheckMIB.setOrganization('Cisco Systems, Inc.')
ciscoImageCheckMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1))
ciscoImageCheck = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1))
ciscoImageCheckOpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoImageCheckOpTable.setStatus('current')
ciscoImageCheckOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckSerialNum"))
if mibBuilder.loadTexts: ciscoImageCheckOpEntry.setStatus('current')
ciscoImageCheckSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ciscoImageCheckSerialNum.setStatus('current')
ciscoImageCheckImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoImageCheckImageName.setStatus('current')
ciscoImageCheckStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("inCompatLoose", 3), ("inCompatStrict", 4), ("compatible", 5), ("noStandby", 6), ("pssErr", 7), ("extractFail", 8), ("fileParseErr", 9), ("getIncompatErr", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImageCheckStatus.setStatus('current')
ciscoImageCheckEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoImageCheckEntryStatus.setStatus('current')
ciscoImgChkResultsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2), )
if mibBuilder.loadTexts: ciscoImgChkResultsTable.setStatus('current')
ciscoImgChkResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckSerialNum"), (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImgChkFeatureIndex"), (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabIndex"))
if mibBuilder.loadTexts: ciscoImgChkResultsEntry.setStatus('current')
ciscoImgChkFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ciscoImgChkFeatureIndex.setStatus('current')
ciscoImgChkCapabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ciscoImgChkCapabIndex.setStatus('current')
ciscoImgChkFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkFeatureName.setStatus('current')
ciscoImgChkCapabilityName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkCapabilityName.setStatus('current')
ciscoImgChkCapabilityReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("loose", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkCapabilityReq.setStatus('current')
ciscoImgChkInCompDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkInCompDescr.setStatus('current')
ciscoImageCheckMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2))
ciscoImageCheckMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 1))
ciscoImageCheckMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2))
ciscoImageCheckMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 1, 1)).setObjects(("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckOpGroup"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkResultsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCheckMIBCompliance = ciscoImageCheckMIBCompliance.setStatus('current')
ciscoImageCheckOpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2, 1)).setObjects(("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckImageName"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckStatus"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCheckOpGroup = ciscoImageCheckOpGroup.setStatus('current')
ciscoImgChkResultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2, 2)).setObjects(("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkFeatureName"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabilityName"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabilityReq"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkInCompDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImgChkResultsGroup = ciscoImgChkResultsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-CHECK-MIB", ciscoImageCheckMIBObjects=ciscoImageCheckMIBObjects, ciscoImageCheckEntryStatus=ciscoImageCheckEntryStatus, ciscoImgChkFeatureIndex=ciscoImgChkFeatureIndex, ciscoImageCheckImageName=ciscoImageCheckImageName, ciscoImageCheckOpGroup=ciscoImageCheckOpGroup, ciscoImageCheckMIB=ciscoImageCheckMIB, ciscoImgChkInCompDescr=ciscoImgChkInCompDescr, ciscoImgChkCapabilityName=ciscoImgChkCapabilityName, PYSNMP_MODULE_ID=ciscoImageCheckMIB, ciscoImageCheck=ciscoImageCheck, ciscoImageCheckSerialNum=ciscoImageCheckSerialNum, ciscoImgChkCapabIndex=ciscoImgChkCapabIndex, ciscoImageCheckStatus=ciscoImageCheckStatus, ciscoImageCheckMIBConformance=ciscoImageCheckMIBConformance, ciscoImageCheckOpTable=ciscoImageCheckOpTable, ciscoImgChkFeatureName=ciscoImgChkFeatureName, ciscoImgChkResultsEntry=ciscoImgChkResultsEntry, ciscoImageCheckMIBCompliances=ciscoImageCheckMIBCompliances, ciscoImgChkResultsGroup=ciscoImgChkResultsGroup, ciscoImgChkCapabilityReq=ciscoImgChkCapabilityReq, ciscoImageCheckMIBCompliance=ciscoImageCheckMIBCompliance, ciscoImageCheckMIBGroups=ciscoImageCheckMIBGroups, ciscoImgChkResultsTable=ciscoImgChkResultsTable, ciscoImageCheckOpEntry=ciscoImageCheckOpEntry)
