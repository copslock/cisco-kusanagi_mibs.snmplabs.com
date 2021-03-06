#
# PySNMP MIB module CISCO-WAN-FR-X21-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-FR-X21-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
frPortCnfX21PortGrp, x21 = mibBuilder.importSymbols("BASIS-MIB", "frPortCnfX21PortGrp", "x21")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, ModuleIdentity, Gauge32, Unsigned32, IpAddress, iso, TimeTicks, Counter64, NotificationType, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "ModuleIdentity", "Gauge32", "Unsigned32", "IpAddress", "iso", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanFrX21MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 49))
ciscoWanFrX21MIB.setRevisions(('2002-09-19 00:00',))
if mibBuilder.loadTexts: ciscoWanFrX21MIB.setLastUpdated('200209190000Z')
if mibBuilder.loadTexts: ciscoWanFrX21MIB.setOrganization('Cisco Systems, Inc.')
x21CnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1))
x21AlmCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2))
x21AlmGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3))
x21CnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1), )
if mibBuilder.loadTexts: x21CnfGrpTable.setStatus('current')
x21CnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-FR-X21-MIB", "x21LineNum"))
if mibBuilder.loadTexts: x21CnfGrpEntry.setStatus('current')
x21LineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21LineNum.setStatus('current')
x21LineEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("modify", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21LineEnable.setStatus('current')
x21LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2), ("dteST", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21LineType.setStatus('current')
x21LineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108))).clone(namedValues=NamedValues(("r48Kbps", 1), ("r56Kbps", 2), ("r64Kbps", 3), ("r112Kbps", 4), ("r128Kbps", 5), ("r168Kbps", 6), ("r192Kbps", 7), ("r224Kbps", 8), ("r256Kbps", 9), ("r280Kbps", 10), ("r320Kbps", 11), ("r336Kbps", 12), ("r384Kbps", 13), ("r392Kbps", 14), ("r448Kbps", 15), ("r512Kbps", 16), ("r768Kbps", 17), ("r1024Kbps", 18), ("r1536Kbps", 19), ("r1544Kbps", 20), ("r1792Kbps", 21), ("r1920Kbps", 22), ("r1984Kbps", 23), ("r2048Kbps", 24), ("r3097Kbps", 25), ("r3157Kbps", 26), ("r4096Kbps", 27), ("r4645Kbps", 28), ("r4736Kbps", 29), ("r6195Kbps", 30), ("r6315Kbps", 31), ("r7744Kbps", 32), ("r7899Kbps", 33), ("r8192Kbps", 34), ("r9289Kbps", 35), ("r9472Kbps", 36), ("r10240Kbps", 37), ("r10890Kbps", 38), ("r11060Kbps", 39), ("r12390Kbps", 40), ("r12630Kbps", 41), ("r13900Kbps", 42), ("r14220Kbps", 43), ("r14340Kbps", 44), ("r15490Kbps", 45), ("r15800Kbps", 46), ("r16380Kbps", 47), ("r20030Kbps", 48), ("r24990Kbps", 49), ("r52Mbps", 50), ("r17370Kbps", 51), ("r18950Kbps", 52), ("r20530Kbps", 53), ("r22100Kbps", 54), ("r23680Kbps", 55), ("r3088Kbps", 56), ("r4632Kbps", 57), ("r6176Kbps", 58), ("r7720Kbps", 59), ("r9264Kbps", 60), ("r10808Kbps", 61), ("r12352Kbps", 62), ("r13896Kbps", 63), ("r15440Kbps", 64), ("r16984Kbps", 65), ("r18528Kbps", 66), ("r20072Kbps", 67), ("r21616Kbps", 68), ("r23160Kbps", 69), ("r24704Kbps", 70), ("r26248Kbps", 71), ("r27792Kbps", 72), ("r29336Kbps", 73), ("r30880Kbps", 74), ("r32424Kbps", 75), ("r33968Kbps", 76), ("r35512Kbps", 77), ("r37056Kbps", 78), ("r38600Kbps", 79), ("r40144Kbps", 80), ("r41688Kbps", 81), ("r43232Kbps", 82), ("r44776Kbps", 83), ("r46320Kbps", 84), ("r47864Kbps", 85), ("r49408Kbps", 86), ("r50952Kbps", 87), ("r6144Kbps", 88), ("r12288Kbps", 89), ("r14336Kbps", 90), ("r16384Kbps", 91), ("r18432Kbps", 92), ("r20480Kbps", 93), ("r22528Kbps", 94), ("r24576Kbps", 95), ("r26624Kbps", 96), ("r28672Kbps", 97), ("r30720Kbps", 98), ("r32768Kbps", 99), ("r34816Kbps", 100), ("r36864Kbps", 101), ("r38912Kbps", 102), ("r40960Kbps", 103), ("r43008Kbps", 104), ("r45056Kbps", 105), ("r47104Kbps", 106), ("r49152Kbps", 107), ("r51200Kbps", 108)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21LineRate.setStatus('current')
x21LineLoopbackCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("x21NoLoop", 1), ("x21DiagnosticMetallicLoop", 2), ("x21DiagnosticFrontcardLoop", 3), ("x21RemoteLoop", 4), ("v35MetallicLoop", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21LineLoopbackCommand.setStatus('current')
x21LineSendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("x21NoCode", 1), ("x21SendLoopACode", 2), ("x21SendLoopBCode", 3), ("x21SendLocalLoopCode", 4), ("x21SendRemoteLoopCode", 5), ("x21SendUnLoopCode", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21LineSendCode.setStatus('current')
x21LineLoopbackCodeDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("codeDetectDisabled", 1), ("codeDetectEnabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21LineLoopbackCodeDetection.setStatus('current')
x21ConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("x21Backcard", 1), ("hssiBackcard", 2), ("v35Backcard", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21ConnectorType.setStatus('current')
x21InvertClock = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nonInvertedAndNotLooped", 1), ("invertedAndNotLooped", 2), ("nonInvertedAndLooped", 3), ("invertedAndLooped", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21InvertClock.setStatus('current')
x21LineInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hssi", 1), ("x21", 2), ("v35", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21LineInterfaceType.setStatus('current')
x21ClkFrequencyThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21ClkFrequencyThreshold.setStatus('current')
serialLineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(48000, 51840000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialLineRate.setStatus('current')
serialLineRateVariation = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialLineRateVariation.setStatus('current')
x21LineNumofValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21LineNumofValidEntries.setStatus('current')
frPortCnfX21PortGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: frPortCnfX21PortGrpTable.setStatus('current')
frPortCnfX21PortGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-WAN-FR-X21-MIB", "x21portNum"))
if mibBuilder.loadTexts: frPortCnfX21PortGrpEntry.setStatus('current')
x21portNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portNum.setStatus('current')
x21portLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portLineNum.setStatus('current')
x21portRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portRowStatus.setStatus('current')
x21portFlagsBetweenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portFlagsBetweenFrames.setStatus('current')
x21portEqueueServiceRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portEqueueServiceRatio.setStatus('current')
x21portSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portSpeed.setStatus('current')
x21portAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("write-Only", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portAdmin.setStatus('current')
x21portType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("frame-relay", 1), ("frFUNI", 2), ("frame-forward", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portType.setStatus('current')
x21portSvcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portSvcStatus.setStatus('current')
x21portSvcInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-use", 1), ("in-use", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portSvcInUse.setStatus('current')
x21portSvcShareLcn = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port-based", 1), ("card-based", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portSvcShareLcn.setStatus('current')
x21portSvcLcnLow = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 271))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portSvcLcnLow.setStatus('current')
x21portSvcLcnHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 271))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portSvcLcnHigh.setStatus('current')
x21portSvcDlciLow = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portSvcDlciLow.setStatus('current')
x21portSvcDlciHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portSvcDlciHigh.setStatus('current')
x21portDeleteSvcs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("delete", 1), ("other", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21portDeleteSvcs.setStatus('current')
x21portIngrSvcBandW = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portIngrSvcBandW.setStatus('current')
x21portEgrSvcBandW = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21portEgrSvcBandW.setStatus('current')
x21AlmCnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1), )
if mibBuilder.loadTexts: x21AlmCnfGrpTable.setStatus('current')
x21AlmCnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-FR-X21-MIB", "x21AlmCnfLineNum"))
if mibBuilder.loadTexts: x21AlmCnfGrpEntry.setStatus('current')
x21AlmCnfLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21AlmCnfLineNum.setStatus('current')
x21Severity = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("minor", 1), ("major", 2), ("dontcare", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21Severity.setStatus('current')
x21AlmGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1), )
if mibBuilder.loadTexts: x21AlmGrpTable.setStatus('current')
x21AlmGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1), ).setIndexNames((0, "CISCO-WAN-FR-X21-MIB", "x21AlmLineNum"))
if mibBuilder.loadTexts: x21AlmGrpEntry.setStatus('current')
x21AlmLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21AlmLineNum.setStatus('current')
x21LineAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21LineAlarmState.setStatus('current')
x21LineEIAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: x21LineEIAStatus.setStatus('current')
x21AlarmClrButton = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 5, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noaction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x21AlarmClrButton.setStatus('current')
cwfX21MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 49, 2))
cwfX21MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1))
cwfX21MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 2))
cwfX21Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 2, 1)).setObjects(("CISCO-WAN-FR-X21-MIB", "ciscoWanFrX21LineGroup"), ("CISCO-WAN-FR-X21-MIB", "ciscoWanFrX21PortGroup"), ("CISCO-WAN-FR-X21-MIB", "ciscoWanFrX21AlarmConfGroup"), ("CISCO-WAN-FR-X21-MIB", "ciscoWanFrX21AlarmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwfX21Compliance = cwfX21Compliance.setStatus('current')
ciscoWanFrX21PortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 1)).setObjects(("CISCO-WAN-FR-X21-MIB", "x21portNum"), ("CISCO-WAN-FR-X21-MIB", "x21portLineNum"), ("CISCO-WAN-FR-X21-MIB", "x21portRowStatus"), ("CISCO-WAN-FR-X21-MIB", "x21portFlagsBetweenFrames"), ("CISCO-WAN-FR-X21-MIB", "x21portEqueueServiceRatio"), ("CISCO-WAN-FR-X21-MIB", "x21portSpeed"), ("CISCO-WAN-FR-X21-MIB", "x21portAdmin"), ("CISCO-WAN-FR-X21-MIB", "x21portType"), ("CISCO-WAN-FR-X21-MIB", "x21portSvcStatus"), ("CISCO-WAN-FR-X21-MIB", "x21portSvcInUse"), ("CISCO-WAN-FR-X21-MIB", "x21portSvcShareLcn"), ("CISCO-WAN-FR-X21-MIB", "x21portSvcLcnLow"), ("CISCO-WAN-FR-X21-MIB", "x21portSvcLcnHigh"), ("CISCO-WAN-FR-X21-MIB", "x21portSvcDlciLow"), ("CISCO-WAN-FR-X21-MIB", "x21portSvcDlciHigh"), ("CISCO-WAN-FR-X21-MIB", "x21portDeleteSvcs"), ("CISCO-WAN-FR-X21-MIB", "x21portIngrSvcBandW"), ("CISCO-WAN-FR-X21-MIB", "x21portEgrSvcBandW"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrX21PortGroup = ciscoWanFrX21PortGroup.setStatus('current')
ciscoWanFrX21LineGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 2)).setObjects(("CISCO-WAN-FR-X21-MIB", "x21LineNum"), ("CISCO-WAN-FR-X21-MIB", "x21LineEnable"), ("CISCO-WAN-FR-X21-MIB", "x21LineType"), ("CISCO-WAN-FR-X21-MIB", "x21LineRate"), ("CISCO-WAN-FR-X21-MIB", "x21LineLoopbackCommand"), ("CISCO-WAN-FR-X21-MIB", "x21LineSendCode"), ("CISCO-WAN-FR-X21-MIB", "x21LineLoopbackCodeDetection"), ("CISCO-WAN-FR-X21-MIB", "x21ConnectorType"), ("CISCO-WAN-FR-X21-MIB", "x21InvertClock"), ("CISCO-WAN-FR-X21-MIB", "x21LineInterfaceType"), ("CISCO-WAN-FR-X21-MIB", "x21ClkFrequencyThreshold"), ("CISCO-WAN-FR-X21-MIB", "serialLineRate"), ("CISCO-WAN-FR-X21-MIB", "serialLineRateVariation"), ("CISCO-WAN-FR-X21-MIB", "x21LineNumofValidEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrX21LineGroup = ciscoWanFrX21LineGroup.setStatus('current')
ciscoWanFrX21AlarmConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 3)).setObjects(("CISCO-WAN-FR-X21-MIB", "x21AlmCnfLineNum"), ("CISCO-WAN-FR-X21-MIB", "x21Severity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrX21AlarmConfGroup = ciscoWanFrX21AlarmConfGroup.setStatus('current')
ciscoWanFrX21AlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 49, 2, 1, 4)).setObjects(("CISCO-WAN-FR-X21-MIB", "x21AlmLineNum"), ("CISCO-WAN-FR-X21-MIB", "x21LineAlarmState"), ("CISCO-WAN-FR-X21-MIB", "x21LineEIAStatus"), ("CISCO-WAN-FR-X21-MIB", "x21AlarmClrButton"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanFrX21AlarmGroup = ciscoWanFrX21AlarmGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-FR-X21-MIB", ciscoWanFrX21AlarmGroup=ciscoWanFrX21AlarmGroup, x21CnfGrpEntry=x21CnfGrpEntry, PYSNMP_MODULE_ID=ciscoWanFrX21MIB, serialLineRateVariation=serialLineRateVariation, x21CnfGrp=x21CnfGrp, x21portSvcStatus=x21portSvcStatus, x21AlmGrp=x21AlmGrp, x21AlmCnfGrpTable=x21AlmCnfGrpTable, x21LineLoopbackCommand=x21LineLoopbackCommand, x21portType=x21portType, x21portSvcInUse=x21portSvcInUse, x21InvertClock=x21InvertClock, x21portSvcDlciHigh=x21portSvcDlciHigh, x21AlmGrpTable=x21AlmGrpTable, x21LineSendCode=x21LineSendCode, x21portFlagsBetweenFrames=x21portFlagsBetweenFrames, x21AlmGrpEntry=x21AlmGrpEntry, x21LineType=x21LineType, x21portSvcShareLcn=x21portSvcShareLcn, x21LineNumofValidEntries=x21LineNumofValidEntries, x21LineAlarmState=x21LineAlarmState, x21LineLoopbackCodeDetection=x21LineLoopbackCodeDetection, x21AlmLineNum=x21AlmLineNum, ciscoWanFrX21LineGroup=ciscoWanFrX21LineGroup, x21portEqueueServiceRatio=x21portEqueueServiceRatio, x21LineNum=x21LineNum, cwfX21Compliance=cwfX21Compliance, serialLineRate=serialLineRate, x21portSpeed=x21portSpeed, x21portEgrSvcBandW=x21portEgrSvcBandW, x21ConnectorType=x21ConnectorType, x21Severity=x21Severity, cwfX21MIBCompliances=cwfX21MIBCompliances, x21AlarmClrButton=x21AlarmClrButton, x21CnfGrpTable=x21CnfGrpTable, x21portSvcDlciLow=x21portSvcDlciLow, x21portAdmin=x21portAdmin, x21LineInterfaceType=x21LineInterfaceType, x21portDeleteSvcs=x21portDeleteSvcs, x21LineRate=x21LineRate, ciscoWanFrX21AlarmConfGroup=ciscoWanFrX21AlarmConfGroup, x21portSvcLcnLow=x21portSvcLcnLow, x21AlmCnfGrp=x21AlmCnfGrp, x21AlmCnfLineNum=x21AlmCnfLineNum, x21portLineNum=x21portLineNum, frPortCnfX21PortGrpTable=frPortCnfX21PortGrpTable, frPortCnfX21PortGrpEntry=frPortCnfX21PortGrpEntry, x21portNum=x21portNum, ciscoWanFrX21MIB=ciscoWanFrX21MIB, x21portIngrSvcBandW=x21portIngrSvcBandW, ciscoWanFrX21PortGroup=ciscoWanFrX21PortGroup, x21LineEIAStatus=x21LineEIAStatus, x21LineEnable=x21LineEnable, cwfX21MIBConformance=cwfX21MIBConformance, cwfX21MIBGroups=cwfX21MIBGroups, x21portRowStatus=x21portRowStatus, x21AlmCnfGrpEntry=x21AlmCnfGrpEntry, x21portSvcLcnHigh=x21portSvcLcnHigh, x21ClkFrequencyThreshold=x21ClkFrequencyThreshold)
