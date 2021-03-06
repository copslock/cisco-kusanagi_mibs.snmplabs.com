#
# PySNMP MIB module CXACTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXACTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
cxACTE, = mibBuilder.importSymbols("CXProduct-SMI", "cxACTE")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Gauge32, TimeTicks, Unsigned32, ModuleIdentity, NotificationType, MibIdentifier, Bits, ObjectIdentity, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Gauge32", "TimeTicks", "Unsigned32", "ModuleIdentity", "NotificationType", "MibIdentifier", "Bits", "ObjectIdentity", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acteDebugTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30), )
if mibBuilder.loadTexts: acteDebugTable.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugTable.setDescription('The DS1 debug table.')
acteDebugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1), ).setIndexNames((0, "CXACTE-MIB", "acteDebugLinkIndex"), (0, "CXACTE-MIB", "acteDebugIndex"))
if mibBuilder.loadTexts: acteDebugEntry.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugEntry.setDescription('An entry in the DS1 Debug Table.')
acteDebugLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acteDebugLinkIndex.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugLinkIndex.setDescription('Identifies the T1/E1 (DS1) interface port.')
acteDebugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acteDebugIndex.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugIndex.setDescription('The index value uniquely identifies the T1/E1 (DS0) channel for which these table entries are applicable.')
acteDebugRegister = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acteDebugRegister.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugRegister.setDescription("Determines which register on the T1/E1 I/O card will be affected by the 'read' or 'write' operation initiated by the acteDebugOperation object.")
acteDebugResult = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 50), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acteDebugResult.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugResult.setDescription("Indicates the values of each of the 8 registers following the address specified for the acteDebugRegister object following a 'get' command.")
acteDebugWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 80), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: acteDebugWrite.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugWrite.setDescription('Determines the value to be written to the T1/E1 I/O card register specified by the acteDebugRegister object. The command is activated by entering a value in this object. ')
acteDebugTvdStat = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 81), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: acteDebugTvdStat.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugTvdStat.setDescription('This object displays the statistics relative to this TVD control block for the specified DS0 channel on the specified DVC card which corresponds to acteDebugCfgIndex. If acteDebugTvdStat is set to 1, nothing occurs, 2 displays the debugging information and 3 clears the counters.')
acteDebugDs1Stat = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 82), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: acteDebugDs1Stat.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugDs1Stat.setDescription('This object displays the statistics relative to this DS1 control block. When acteDebugIndex is set to 1, it displays the port information, 2 displays the counter information for channels 0 to 14 and 3 displays the counter information for channels 15 to 29. If acteDebugDs1Stat is set to 1, nothing occurs, 2 displays the debugging information and 3 clears the counters.')
acteDebugSvdStat = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 83), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: acteDebugSvdStat.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugSvdStat.setDescription('This object displays the statistics relative to this SVD control block for the specified DS0 channel specified by acteDebugIndex. If acteDebugSvdStat is set to 1, nothing occurs, 2 displays the debugging information and 3 clears the counters.')
acteDebugSvdEvt = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1, 30, 1, 84), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: acteDebugSvdEvt.setStatus('mandatory')
if mibBuilder.loadTexts: acteDebugSvdEvt.setDescription('This object displays the timestamps concerning particular events relative to this TVD control block for the specified DS0 channel specified by acteDebugIndex. If acteDebugSvdEvt is set to 1, nothing occurs, 2 displays the debugging information and 3 clears the counters.')
mibBuilder.exportSymbols("CXACTE-MIB", acteDebugWrite=acteDebugWrite, acteDebugTvdStat=acteDebugTvdStat, acteDebugSvdStat=acteDebugSvdStat, acteDebugTable=acteDebugTable, acteDebugRegister=acteDebugRegister, acteDebugResult=acteDebugResult, acteDebugDs1Stat=acteDebugDs1Stat, acteDebugSvdEvt=acteDebugSvdEvt, acteDebugEntry=acteDebugEntry, acteDebugLinkIndex=acteDebugLinkIndex, acteDebugIndex=acteDebugIndex)
