#
# PySNMP MIB module ChrComPmAtmATM-VP-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmAtmATM-VP-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
atmVplVpi, = mibBuilder.importSymbols("ATM-MIB", "atmVplVpi")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmAtm, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmAtm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, iso, TimeTicks, ObjectIdentity, IpAddress, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "iso", "TimeTicks", "ObjectIdentity", "IpAddress", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmAtmATM_VP_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5), ).setLabel("chrComPmAtmATM-VP-IntervalTable")
if mibBuilder.loadTexts: chrComPmAtmATM_VP_IntervalTable.setStatus('current')
chrComPmAtmATM_VP_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5, 1), ).setLabel("chrComPmAtmATM-VP-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ATM-MIB", "atmVplVpi"), (0, "ChrComPmAtmATM-VP-Interval-MIB", "chrComPmAtmIntervalNumber"))
if mibBuilder.loadTexts: chrComPmAtmATM_VP_IntervalEntry.setStatus('current')
chrComPmAtmIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmIntervalNumber.setStatus('current')
chrComPmAtmSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setStatus('current')
chrComPmAtmElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setStatus('current')
chrComPmAtmSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setStatus('current')
chrComPmAtmReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setStatus('current')
chrComPmAtmTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 5, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setStatus('current')
mibBuilder.exportSymbols("ChrComPmAtmATM-VP-Interval-MIB", chrComPmAtmSuppressedIntrvls=chrComPmAtmSuppressedIntrvls, chrComPmAtmATM_VP_IntervalTable=chrComPmAtmATM_VP_IntervalTable, chrComPmAtmIntervalNumber=chrComPmAtmIntervalNumber, chrComPmAtmSuspectedInterval=chrComPmAtmSuspectedInterval, chrComPmAtmElapsedTime=chrComPmAtmElapsedTime, chrComPmAtmReceivedCells=chrComPmAtmReceivedCells, chrComPmAtmATM_VP_IntervalEntry=chrComPmAtmATM_VP_IntervalEntry, chrComPmAtmTransmittedCells=chrComPmAtmTransmittedCells)
