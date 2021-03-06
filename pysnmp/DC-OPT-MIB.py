#
# PySNMP MIB module DC-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DC-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Counter32, ObjectIdentity, IpAddress, MibIdentifier, enterprises, Integer32, TimeTicks, NotificationType, ModuleIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "enterprises", "Integer32", "TimeTicks", "NotificationType", "ModuleIdentity", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatOtherStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class DisplayString(OctetString):
    pass

cdx6500DCStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10))
cdx6500DCGenStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1))
cdx6500DCGenStatTableEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1))
cdx6500DCGenStatDSPStatus = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("missing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatDSPStatus.setStatus('mandatory')
cdx6500DCGenStatHndlrSWRev = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatHndlrSWRev.setStatus('mandatory')
cdx6500DCGenStatFnctnSWRev = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatFnctnSWRev.setStatus('mandatory')
cdx6500DCGenStatMaxChannels = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxChannels.setStatus('mandatory')
cdx6500DCGenStatChanInUse = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatChanInUse.setStatus('mandatory')
cdx6500DCGenStatMaxSmltChanUse = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxSmltChanUse.setStatus('mandatory')
cdx6500DCGenStatRejectConn = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatRejectConn.setStatus('mandatory')
cdx6500DCGenStatAggCRatio = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatAggCRatio.setStatus('mandatory')
cdx6500DCGenStatCurrEncQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatCurrEncQDepth.setStatus('mandatory')
cdx6500DCGenStatMaxEncQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxEncQDepth.setStatus('mandatory')
cdx6500DCGenStatTmOfMaxEncQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatTmOfMaxEncQDepth.setStatus('mandatory')
cdx6500DCGenStatCurrDecQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatCurrDecQDepth.setStatus('mandatory')
cdx6500DCGenStatMaxDecQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatMaxDecQDepth.setStatus('mandatory')
cdx6500DCGenStatTmOfMaxDecQDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCGenStatTmOfMaxDecQDepth.setStatus('mandatory')
cdx6500DCChanStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2), )
if mibBuilder.loadTexts: cdx6500DCChanStatTable.setStatus('mandatory')
cdx6500DCChanStatTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1), ).setIndexNames((0, "DC-OPT-MIB", "cdx6500DCChanStatChanNum"))
if mibBuilder.loadTexts: cdx6500DCChanStatTableEntry.setStatus('mandatory')
cdx6500DCChanStatChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatChanNum.setStatus('mandatory')
cdx6500DCChanStatTmOfLastStatRst = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatTmOfLastStatRst.setStatus('mandatory')
cdx6500DCChanStatChanState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("dspDown", 1), ("idle", 2), ("negotiating", 3), ("dataPassing", 4), ("flushingData", 5), ("flushingDCRing", 6), ("apClearing", 7), ("npClearing", 8), ("clearingCall", 9), ("flushingOnClr", 10), ("clearing", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatChanState.setStatus('mandatory')
cdx6500DCChanStatSourceChan = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatSourceChan.setStatus('mandatory')
cdx6500DCChanStatDestChan = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDestChan.setStatus('mandatory')
cdx6500DCChanStatXmitCRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatXmitCRatio.setStatus('mandatory')
cdx6500DCChanStatNumOfEncFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfEncFrames.setStatus('mandatory')
cdx6500DCChanStatNumOfCharInToEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharInToEnc.setStatus('mandatory')
cdx6500DCChanStatNumOfCharOutOfEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharOutOfEnc.setStatus('mandatory')
cdx6500DCChanStatNumOfDecFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfDecFrames.setStatus('mandatory')
cdx6500DCChanStatNumOfCharInToDec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharInToDec.setStatus('mandatory')
cdx6500DCChanStatNumOfCharOutOfDec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatNumOfCharOutOfDec.setStatus('mandatory')
cdx6500DCChanStatEncAETrnstnCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatEncAETrnstnCnt.setStatus('mandatory')
cdx6500DCChanStatEncAEFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatEncAEFrameCnt.setStatus('mandatory')
cdx6500DCChanStatEncAEModeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatEncAEModeStatus.setStatus('mandatory')
cdx6500DCChanStatDecAETrnstnCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDecAETrnstnCnt.setStatus('mandatory')
cdx6500DCChanStatDecAEFrameCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDecAEFrameCnt.setStatus('mandatory')
cdx6500DCChanStatDecAEModeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDecAEModeStatus.setStatus('mandatory')
cdx6500DCChanStatDSWithBadFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDSWithBadFrames.setStatus('mandatory')
cdx6500DCChanStatDSWithBadHeaders = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDSWithBadHeaders.setStatus('mandatory')
cdx6500DCChanStatDSDueToRstOrCng = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 10, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500DCChanStatDSDueToRstOrCng.setStatus('mandatory')
cdx6500ContDC = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9))
cdx6500ContResetAllDCStats = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noreset", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContResetAllDCStats.setStatus('mandatory')
cdx6500ContDCTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2), )
if mibBuilder.loadTexts: cdx6500ContDCTable.setStatus('mandatory')
cdx6500ContDCTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1), ).setIndexNames((0, "DC-OPT-MIB", "cdx6500ContDCChanNum"))
if mibBuilder.loadTexts: cdx6500ContDCTableEntry.setStatus('mandatory')
cdx6500ContDCChanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500ContDCChanNum.setStatus('mandatory')
cdx6500ContResetDCChanStats = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noreset", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContResetDCChanStats.setStatus('mandatory')
cdx6500ContResetDCChanVocab = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noreset", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContResetDCChanVocab.setStatus('mandatory')
mibBuilder.exportSymbols("DC-OPT-MIB", cdx6500DCGenStatCurrDecQDepth=cdx6500DCGenStatCurrDecQDepth, cdx6500DCChanStatDecAEFrameCnt=cdx6500DCChanStatDecAEFrameCnt, cdx6500DCGenStatMaxEncQDepth=cdx6500DCGenStatMaxEncQDepth, cdx6500DCGenStatMaxDecQDepth=cdx6500DCGenStatMaxDecQDepth, cdx6500DCChanStatNumOfCharOutOfEnc=cdx6500DCChanStatNumOfCharOutOfEnc, cdx6500DCChanStatTmOfLastStatRst=cdx6500DCChanStatTmOfLastStatRst, cdx6500DCGenStatDSPStatus=cdx6500DCGenStatDSPStatus, cdx6500DCGenStatFnctnSWRev=cdx6500DCGenStatFnctnSWRev, cdx6500DCGenStatTmOfMaxDecQDepth=cdx6500DCGenStatTmOfMaxDecQDepth, cdx6500DCChanStatDSWithBadHeaders=cdx6500DCChanStatDSWithBadHeaders, cdx6500ContResetDCChanStats=cdx6500ContResetDCChanStats, cdx6500DCGenStatTable=cdx6500DCGenStatTable, cdx6500DCChanStatEncAEModeStatus=cdx6500DCChanStatEncAEModeStatus, cdx6500DCGenStatMaxSmltChanUse=cdx6500DCGenStatMaxSmltChanUse, cdx6500DCChanStatNumOfCharOutOfDec=cdx6500DCChanStatNumOfCharOutOfDec, cdx6500DCChanStatNumOfCharInToEnc=cdx6500DCChanStatNumOfCharInToEnc, cdx6500DCGenStatHndlrSWRev=cdx6500DCGenStatHndlrSWRev, codex=codex, cdx6500DCStatTable=cdx6500DCStatTable, cdx6500DCChanStatNumOfDecFrames=cdx6500DCChanStatNumOfDecFrames, cdx6500ContDCTableEntry=cdx6500ContDCTableEntry, cdx6500DCChanStatDSDueToRstOrCng=cdx6500DCChanStatDSDueToRstOrCng, cdx6500DCGenStatTmOfMaxEncQDepth=cdx6500DCGenStatTmOfMaxEncQDepth, cdx6500DCChanStatDecAETrnstnCnt=cdx6500DCChanStatDecAETrnstnCnt, cdx6500DCChanStatNumOfCharInToDec=cdx6500DCChanStatNumOfCharInToDec, cdx6500DCChanStatXmitCRatio=cdx6500DCChanStatXmitCRatio, cdx6500DCChanStatDestChan=cdx6500DCChanStatDestChan, cdx6500DCChanStatDSWithBadFrames=cdx6500DCChanStatDSWithBadFrames, cdx6500DCChanStatChanState=cdx6500DCChanStatChanState, cdx6500DCGenStatTableEntry=cdx6500DCGenStatTableEntry, cdx6500DCGenStatAggCRatio=cdx6500DCGenStatAggCRatio, DisplayString=DisplayString, cdxProductSpecific=cdxProductSpecific, cdx6500DCGenStatCurrEncQDepth=cdx6500DCGenStatCurrEncQDepth, cdx6500DCChanStatNumOfEncFrames=cdx6500DCChanStatNumOfEncFrames, cdx6500DCChanStatEncAEFrameCnt=cdx6500DCChanStatEncAEFrameCnt, cdx6500DCGenStatRejectConn=cdx6500DCGenStatRejectConn, cdx6500Statistics=cdx6500Statistics, cdx6500DCGenStatMaxChannels=cdx6500DCGenStatMaxChannels, cdx6500DCChanStatDecAEModeStatus=cdx6500DCChanStatDecAEModeStatus, cdx6500Controls=cdx6500Controls, cdx6500ContDCTable=cdx6500ContDCTable, cdx6500=cdx6500, cdx6500DCChanStatChanNum=cdx6500DCChanStatChanNum, cdx6500DCChanStatEncAETrnstnCnt=cdx6500DCChanStatEncAETrnstnCnt, cdx6500ContDC=cdx6500ContDC, cdx6500DCChanStatTableEntry=cdx6500DCChanStatTableEntry, cdx6500DCGenStatChanInUse=cdx6500DCGenStatChanInUse, cdx6500ContResetAllDCStats=cdx6500ContResetAllDCStats, cdx6500ContDCChanNum=cdx6500ContDCChanNum, cdx6500ContResetDCChanVocab=cdx6500ContResetDCChanVocab, cdx6500DCChanStatSourceChan=cdx6500DCChanStatSourceChan, cdx6500DCChanStatTable=cdx6500DCChanStatTable, cdx6500StatOtherStatsGroup=cdx6500StatOtherStatsGroup)
