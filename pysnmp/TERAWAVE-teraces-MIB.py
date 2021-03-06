#
# PySNMP MIB module TERAWAVE-teraces-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-teraces-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, NotificationType, Counter64, ModuleIdentity, Integer32, IpAddress, enterprises, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "NotificationType", "Counter64", "ModuleIdentity", "Integer32", "IpAddress", "enterprises", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
bandwidthGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 9))
teraCESConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 1), )
if mibBuilder.loadTexts: teraCESConfigTable.setStatus('mandatory')
teraCESConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 1, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"))
if mibBuilder.loadTexts: teraCESConfigTableEntry.setStatus('mandatory')
teraCesSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aal1-signalling", 1), ("aal1-no-signalling", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraCesSignalling.setStatus('mandatory')
teraCesCheckParity = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aal1-no-parity", 1), ("aal1-parity", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraCesCheckParity.setStatus('mandatory')
teraCesTestLine = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-action", 1), ("line-test-relay-off", 2), ("line-test-relay-on", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraCesTestLine.setStatus('mandatory')
teraCesSRTSSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 511))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraCesSRTSSize.setStatus('mandatory')
teraCESStatTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 2), )
if mibBuilder.loadTexts: teraCESStatTable.setStatus('mandatory')
teraCESStatTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 2, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"))
if mibBuilder.loadTexts: teraCESStatTableEntry.setStatus('mandatory')
teraCESTCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTCellCount.setStatus('mandatory')
teraCESRLostCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESRLostCellCount.setStatus('mandatory')
teraCESRReplacedCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESRReplacedCellCount.setStatus('mandatory')
teraCESIntervalStatTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 3), )
if mibBuilder.loadTexts: teraCESIntervalStatTable.setStatus('mandatory')
teraCESIntervalStatTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 3, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"), (0, "TERAWAVE-teraces-MIB", "teraCESIntervalNumber"))
if mibBuilder.loadTexts: teraCESIntervalStatTableEntry.setStatus('mandatory')
teraCESIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESIntervalNumber.setStatus('mandatory')
teraCESIntervalTCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESIntervalTCellCount.setStatus('mandatory')
teraCESIntervalRLostCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESIntervalRLostCellCount.setStatus('mandatory')
teraCESIntervalRReplacedCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESIntervalRReplacedCellCount.setStatus('mandatory')
teraCESTotalStatTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 4), )
if mibBuilder.loadTexts: teraCESTotalStatTable.setStatus('mandatory')
teraCESTotalStatTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 4, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"))
if mibBuilder.loadTexts: teraCESTotalStatTableEntry.setStatus('mandatory')
teraCESTotalTCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTotalTCellCount.setStatus('mandatory')
teraCESTotalRLostCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTotalRLostCellCount.setStatus('mandatory')
teraCESTotalRReplacedCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTotalRReplacedCellCount.setStatus('mandatory')
teraCESTotalStatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraCESTotalStatStatus.setStatus('mandatory')
teraAtmfCESIntervalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 5), )
if mibBuilder.loadTexts: teraAtmfCESIntervalStatsTable.setStatus('mandatory')
teraAtmfCESIntervalStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"), (0, "TERAWAVE-teraces-MIB", "teraAtmfCESIntervalNumber"))
if mibBuilder.loadTexts: teraAtmfCESIntervalStatsTableEntry.setStatus('mandatory')
teraAtmfCESIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalNumber.setStatus('mandatory')
teraAtmfCESIntervalReassCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalReassCells.setStatus('mandatory')
teraAtmfCESIntervalHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalHdrErrors.setStatus('mandatory')
teraAtmfCESIntervalPointerReframes = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalPointerReframes.setStatus('mandatory')
teraAtmfCESIntervalPointerParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalPointerParityErrors.setStatus('mandatory')
teraAtmfCESIntervalAal1SeqErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalAal1SeqErrors.setStatus('mandatory')
teraAtmfCESIntervalLostCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalLostCells.setStatus('mandatory')
teraAtmfCESIntervalMisinsertedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalMisinsertedCells.setStatus('mandatory')
teraAtmfCESIntervalBufUnderflows = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalBufUnderflows.setStatus('mandatory')
teraAtmfCESIntervalBufOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalBufOverflows.setStatus('mandatory')
teraAtmfCESIntervalCellLossStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noloss", 1), ("loss", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESIntervalCellLossStatus.setStatus('mandatory')
teraAtmfCESTotalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 6), )
if mibBuilder.loadTexts: teraAtmfCESTotalStatsTable.setStatus('mandatory')
teraAtmfCESTotalStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"))
if mibBuilder.loadTexts: teraAtmfCESTotalStatsTableEntry.setStatus('mandatory')
teraAtmfCESTotalReassCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalReassCells.setStatus('mandatory')
teraAtmfCESTotalHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalHdrErrors.setStatus('mandatory')
teraAtmfCESTotalPointerReframes = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalPointerReframes.setStatus('mandatory')
teraAtmfCESTotalPointerParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalPointerParityErrors.setStatus('mandatory')
teraAtmfCESTotalAal1SeqErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalAal1SeqErrors.setStatus('mandatory')
teraAtmfCESTotalLostCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalLostCells.setStatus('mandatory')
teraAtmfCESTotalMisinsertedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalMisinsertedCells.setStatus('mandatory')
teraAtmfCESTotalBufUnderflows = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalBufUnderflows.setStatus('mandatory')
teraAtmfCESTotalBufOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalBufOverflows.setStatus('mandatory')
teraAtmfCESTotalCellLossStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noloss", 1), ("loss", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESTotalCellLossStatus.setStatus('mandatory')
teraAtmfCESTotalStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("clear", 2), ("clrall", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraAtmfCESTotalStatsStatus.setStatus('mandatory')
teraAtmfCESStandard7DayTotalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 7), )
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalStatsTable.setStatus('mandatory')
teraAtmfCESStandard7DayTotalStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"), (0, "TERAWAVE-teraces-MIB", "teraAtmfCESStandard7DayTotalNumber"))
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalStatsTableEntry.setStatus('mandatory')
teraAtmfCESStandard7DayTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalNumber.setStatus('mandatory')
teraAtmfCESStandard7DayTotalReassCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalReassCells.setStatus('mandatory')
teraAtmfCESStandard7DayTotalHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalHdrErrors.setStatus('mandatory')
teraAtmfCESStandard7DayTotalPointerReframes = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalPointerReframes.setStatus('mandatory')
teraAtmfCESStandard7DayTotalPointerParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalPointerParityErrors.setStatus('mandatory')
teraAtmfCESStandard7DayTotalAal1SeqErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalAal1SeqErrors.setStatus('mandatory')
teraAtmfCESStandard7DayTotalLostCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalLostCells.setStatus('mandatory')
teraAtmfCESStandard7DayTotalMisinsertedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalMisinsertedCells.setStatus('mandatory')
teraAtmfCESStandard7DayTotalBufUnderflows = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalBufUnderflows.setStatus('mandatory')
teraAtmfCESStandard7DayTotalBufOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalBufOverflows.setStatus('mandatory')
teraAtmfCESStandard7DayTotalCellLossStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noloss", 1), ("loss", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayTotalCellLossStatus.setStatus('mandatory')
teraAtmfCESStandard7DayDayTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 7, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraAtmfCESStandard7DayDayTotalValidData.setStatus('mandatory')
teraCESTera7DayTotalStatTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 9, 8), )
if mibBuilder.loadTexts: teraCESTera7DayTotalStatTable.setStatus('mandatory')
teraCESTera7DayTotalStatTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 9, 8, 1), ).setIndexNames((0, "TERAWAVE-teraces-MIB", "atmfCESCbrIndex"), (0, "TERAWAVE-teraces-MIB", "teraCESTera7DayTotalNumber"))
if mibBuilder.loadTexts: teraCESTera7DayTotalStatTableEntry.setStatus('mandatory')
teraCESTera7DayTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTera7DayTotalNumber.setStatus('mandatory')
teraCESTera7DayTotalTCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTera7DayTotalTCellCount.setStatus('mandatory')
teraCESTera7DayTotalRLostCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTera7DayTotalRLostCellCount.setStatus('mandatory')
teraCESTera7DayTotalRReplacedCellCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTera7DayTotalRReplacedCellCount.setStatus('mandatory')
teraCESTera7DayDayTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 9, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraCESTera7DayDayTotalValidData.setStatus('mandatory')
mibBuilder.exportSymbols("TERAWAVE-teraces-MIB", teraCESStatTable=teraCESStatTable, teraAtmfCESStandard7DayTotalLostCells=teraAtmfCESStandard7DayTotalLostCells, teraAtmfCESIntervalPointerParityErrors=teraAtmfCESIntervalPointerParityErrors, teraAtmfCESIntervalBufOverflows=teraAtmfCESIntervalBufOverflows, teraAtmfCESTotalHdrErrors=teraAtmfCESTotalHdrErrors, teraAtmfCESTotalPointerParityErrors=teraAtmfCESTotalPointerParityErrors, teraAtmfCESIntervalPointerReframes=teraAtmfCESIntervalPointerReframes, teraAtmfCESStandard7DayTotalAal1SeqErrors=teraAtmfCESStandard7DayTotalAal1SeqErrors, teraAtmfCESStandard7DayTotalStatsTable=teraAtmfCESStandard7DayTotalStatsTable, teraCESTera7DayTotalTCellCount=teraCESTera7DayTotalTCellCount, teraCESRReplacedCellCount=teraCESRReplacedCellCount, bandwidthGroup=bandwidthGroup, teraCESConfigTableEntry=teraCESConfigTableEntry, teraCESIntervalNumber=teraCESIntervalNumber, teraCESRLostCellCount=teraCESRLostCellCount, teraAtmfCESIntervalNumber=teraAtmfCESIntervalNumber, teraAtmfCESIntervalCellLossStatus=teraAtmfCESIntervalCellLossStatus, teraAtmfCESTotalLostCells=teraAtmfCESTotalLostCells, teraAtmfCESTotalBufOverflows=teraAtmfCESTotalBufOverflows, teraAtmfCESTotalBufUnderflows=teraAtmfCESTotalBufUnderflows, teraCESTera7DayTotalNumber=teraCESTera7DayTotalNumber, teraCESTera7DayTotalStatTableEntry=teraCESTera7DayTotalStatTableEntry, teraCesTestLine=teraCesTestLine, teraAtmfCESStandard7DayTotalReassCells=teraAtmfCESStandard7DayTotalReassCells, teraAtmfCESTotalStatsTable=teraAtmfCESTotalStatsTable, teraAtmfCESIntervalBufUnderflows=teraAtmfCESIntervalBufUnderflows, teraAtmfCESTotalReassCells=teraAtmfCESTotalReassCells, teraCESIntervalRReplacedCellCount=teraCESIntervalRReplacedCellCount, teraAtmfCESIntervalStatsTableEntry=teraAtmfCESIntervalStatsTableEntry, teraCesCheckParity=teraCesCheckParity, teraCESIntervalStatTable=teraCESIntervalStatTable, teraAtmfCESTotalStatsTableEntry=teraAtmfCESTotalStatsTableEntry, teraAtmfCESIntervalLostCells=teraAtmfCESIntervalLostCells, teraAtmfCESTotalCellLossStatus=teraAtmfCESTotalCellLossStatus, teraAtmfCESStandard7DayTotalCellLossStatus=teraAtmfCESStandard7DayTotalCellLossStatus, teraAtmfCESStandard7DayDayTotalValidData=teraAtmfCESStandard7DayDayTotalValidData, teraAtmfCESStandard7DayTotalHdrErrors=teraAtmfCESStandard7DayTotalHdrErrors, teraAtmfCESStandard7DayTotalBufUnderflows=teraAtmfCESStandard7DayTotalBufUnderflows, teraCesSRTSSize=teraCesSRTSSize, teraCESTotalStatTableEntry=teraCESTotalStatTableEntry, teraCESIntervalTCellCount=teraCESIntervalTCellCount, teraCESStatTableEntry=teraCESStatTableEntry, teraAtmfCESStandard7DayTotalMisinsertedCells=teraAtmfCESStandard7DayTotalMisinsertedCells, teraAtmfCESStandard7DayTotalStatsTableEntry=teraAtmfCESStandard7DayTotalStatsTableEntry, teraCesSignalling=teraCesSignalling, teraCESTotalRReplacedCellCount=teraCESTotalRReplacedCellCount, teraCESTotalTCellCount=teraCESTotalTCellCount, teraCESTera7DayTotalRLostCellCount=teraCESTera7DayTotalRLostCellCount, teraCESTera7DayTotalRReplacedCellCount=teraCESTera7DayTotalRReplacedCellCount, teraAtmfCESIntervalStatsTable=teraAtmfCESIntervalStatsTable, teraAtmfCESIntervalMisinsertedCells=teraAtmfCESIntervalMisinsertedCells, teraAtmfCESTotalStatsStatus=teraAtmfCESTotalStatsStatus, terawave=terawave, teraAtmfCESStandard7DayTotalBufOverflows=teraAtmfCESStandard7DayTotalBufOverflows, teraCESConfigTable=teraCESConfigTable, teraCESTotalStatTable=teraCESTotalStatTable, teraCESIntervalRLostCellCount=teraCESIntervalRLostCellCount, teraAtmfCESTotalAal1SeqErrors=teraAtmfCESTotalAal1SeqErrors, teraAtmfCESTotalPointerReframes=teraAtmfCESTotalPointerReframes, teraCESIntervalStatTableEntry=teraCESIntervalStatTableEntry, teraCESTera7DayTotalStatTable=teraCESTera7DayTotalStatTable, teraCESTotalRLostCellCount=teraCESTotalRLostCellCount, teraCESTera7DayDayTotalValidData=teraCESTera7DayDayTotalValidData, teraAtmfCESIntervalHdrErrors=teraAtmfCESIntervalHdrErrors, teraAtmfCESTotalMisinsertedCells=teraAtmfCESTotalMisinsertedCells, teraCESTCellCount=teraCESTCellCount, teraAtmfCESIntervalReassCells=teraAtmfCESIntervalReassCells, teraAtmfCESStandard7DayTotalNumber=teraAtmfCESStandard7DayTotalNumber, teraAtmfCESStandard7DayTotalPointerReframes=teraAtmfCESStandard7DayTotalPointerReframes, teraAtmfCESStandard7DayTotalPointerParityErrors=teraAtmfCESStandard7DayTotalPointerParityErrors, teraCESTotalStatStatus=teraCESTotalStatStatus, teraAtmfCESIntervalAal1SeqErrors=teraAtmfCESIntervalAal1SeqErrors)
