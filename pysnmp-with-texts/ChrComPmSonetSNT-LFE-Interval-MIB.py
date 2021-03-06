#
# PySNMP MIB module ChrComPmSonetSNT-LFE-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmSonetSNT-LFE-Interval-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:36:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmSonet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, Counter64, NotificationType, Bits, Counter32, ObjectIdentity, ModuleIdentity, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Counter64", "NotificationType", "Bits", "Counter32", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmSonetSNT_LFE_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8), ).setLabel("chrComPmSonetSNT-LFE-IntervalTable")
if mibBuilder.loadTexts: chrComPmSonetSNT_LFE_IntervalTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSNT_LFE_IntervalTable.setDescription('')
chrComPmSonetSNT_LFE_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1), ).setLabel("chrComPmSonetSNT-LFE-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmSonetSNT-LFE-Interval-MIB", "chrComPmSonetIntervalNumber"))
if mibBuilder.loadTexts: chrComPmSonetSNT_LFE_IntervalEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSNT_LFE_IntervalEntry.setDescription('')
chrComPmSonetIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetIntervalNumber.setDescription('')
chrComPmSonetSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setDescription('')
chrComPmSonetElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setDescription('')
chrComPmSonetSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setDescription('')
chrComPmSonetES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetES.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetES.setDescription('')
chrComPmSonetSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSES.setDescription('')
chrComPmSonetCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetCV.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetCV.setDescription('')
chrComPmSonetUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 8, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetUAS.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetUAS.setDescription('')
mibBuilder.exportSymbols("ChrComPmSonetSNT-LFE-Interval-MIB", chrComPmSonetIntervalNumber=chrComPmSonetIntervalNumber, chrComPmSonetES=chrComPmSonetES, chrComPmSonetSuppressedIntrvls=chrComPmSonetSuppressedIntrvls, chrComPmSonetSNT_LFE_IntervalTable=chrComPmSonetSNT_LFE_IntervalTable, chrComPmSonetCV=chrComPmSonetCV, chrComPmSonetSES=chrComPmSonetSES, chrComPmSonetSuspectedInterval=chrComPmSonetSuspectedInterval, chrComPmSonetSNT_LFE_IntervalEntry=chrComPmSonetSNT_LFE_IntervalEntry, chrComPmSonetUAS=chrComPmSonetUAS, chrComPmSonetElapsedTime=chrComPmSonetElapsedTime)
