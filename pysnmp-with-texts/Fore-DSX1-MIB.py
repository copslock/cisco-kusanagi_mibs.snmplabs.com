#
# PySNMP MIB module Fore-DSX1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-DSX1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, TimeTicks, Counter64, IpAddress, Counter32, NotificationType, ObjectIdentity, MibIdentifier, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "TimeTicks", "Counter64", "IpAddress", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
foreDsx1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10))
if mibBuilder.loadTexts: foreDsx1.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreDsx1.setOrganization('FORE')
if mibBuilder.loadTexts: foreDsx1.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreDsx1.setDescription('MIB module for supporting the DSX1 port module.')
dsx1ForeConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1))
dsx1ForeStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2))
dsx1ForeConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1), )
if mibBuilder.loadTexts: dsx1ForeConfTable.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeConfTable.setDescription('A table of DSX1 switch port configuration information.')
dsx1ForeConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1), ).setIndexNames((0, "Fore-DSX1-MIB", "dsx1ForeLineIndex"))
if mibBuilder.loadTexts: dsx1ForeConfEntry.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeConfEntry.setDescription('A table entry containing DSX1 configuration information for each port. Not all RFC1406 configuration table variables are included, and some are modified.')
dsx1ForeLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeLineIndex.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeLineIndex.setDescription('This object is the identifier of a DS1 Inter- face on a managed device. If there is an ifEn- try that is directly associated with this and only this DS1 interface, it should have the same value as ifIndex. Otherwise, the value exceeds ifNumber, and is a unique identifier following this rule: inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g., network side) with odd numbers.')
dsx1ForeReceiveCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("dsx1ReceiveNoCode", 1), ("dsx1ReceiveLineCode", 2), ("dsx1ReceivePayloadCode", 3), ("dsx1ReceiveResetCode", 4), ("dsx1ReceiveQRS", 5), ("dsx1Receive511Pattern", 6), ("dsx1Receive3in24Pattern", 7), ("dsx1ReceiveOtherTestPattern", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeReceiveCode.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeReceiveCode.setDescription('This variable indicates the type of code that was received across the DSX interface. The values mean: dsx1ReceiveNoCode receiving looped or normal data dsx1ReceiveLineCode receiving request for a line loopback dsx1ReceivePayloadCode receiving a request for a payload loopback dsx1ReceiveResetCode receiving a loopback deactivation request dsx1ReceiveQRS receiving a Quasi-Random Signal (QRS) test pattern dsx1Receive511Pattern receiving a 511 bit fixed test pattern dsx1Receive3in24Pattern receiving a fixed test pattern of 3 bits set in 24 dsx1ReceiveTestPattern receiving a test pattern other than the above.')
dsx1ForeLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("dsx1LineLt40", 1), ("dsx1Line40-80", 2), ("dsx1Line80-120", 3), ("dsx1Line120-160", 4), ("dsx1Line160-200", 5), ("dsx1LineE1Coax", 6), ("dsx1LineTwistedPair", 7))).clone('dsx1LineLt40')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ForeLineLength.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeLineLength.setDescription('This variable represents the length of the physical cable connected to the dsx1 port. The user has to set this object to match the physical cable in order to get the netmod to receive the signal on the cable. The different values are: dsx1LineLt40 (1) means the line is shorter than 40m, dsx1Line40-80 (2) means the line length is between 40m and 80m, dsx1Line80-120 (3) means the line length is between 80m and 120m, dsx1Line120-160 (4) means the line length is between 120m and 160m, dsx1Line160-200 (5) means the line length is between 160m and 200m, dsx1LineE1Coax (6) means E1 Coax line, not applicable for T1, dsx1LineTwistedPair (7) means E1 Twisted Pair line, not applicable for T1. ')
dsx1ForeFdlConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2))).clone('network')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ForeFdlConfiguration.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFdlConfiguration.setDescription('This varialbe indicate whether the FDL state machine acts as network or user side')
dsx1ForeLineImpedance = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 5), Integer32().clone(75)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ForeLineImpedance.setStatus('deprecated')
if mibBuilder.loadTexts: dsx1ForeLineImpedance.setDescription('The default line impedance of the E1 line. Note that this is not applicable for T1')
dsx1ForeFdlPerfConf = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ForeFdlPerfConf.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFdlPerfConf.setDescription('This variable indicate whether the FDL state machine is enabled or turned off for performance reports. See T1.403 for details. ')
dsx1ForeFdlBomConf = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ForeFdlBomConf.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFdlBomConf.setDescription('This variable indicate whether Bit Oriented Messages will be generated and transmitted. See T1.403 for details.')
dsx1ForeUpStreamAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ForeUpStreamAIS.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeUpStreamAIS.setDescription('The upsteam AIS alarm generation flag enabled: the upstream AIS is generated disabled: the upstream AIS is not generated')
dsx1ForePortModel = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForePortModel.setStatus('current')
if mibBuilder.loadTexts: dsx1ForePortModel.setDescription('The underlying hardware port model. The value corresponds to the hwPortModel mib variable.')
dsx1ForeAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1ForeAdminStatus.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeAdminStatus.setDescription('The desired state of the interface. The testing(3) state indicates that no operational packets can be passed. When a managed system initializes, all interfaces start with adminStatus in the down(2) state. As a result of either explicit management action or per configuration information retained by the managed system, adminStatus is then changed to either the up(1) or testing(3) states (or remains in the down(2) state).')
dsx1ForeFramingTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1), )
if mibBuilder.loadTexts: dsx1ForeFramingTable.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingTable.setDescription('A table of DSX1 framing statistics information.')
dsx1ForeFramingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1), ).setIndexNames((0, "Fore-DSX1-MIB", "dsx1ForeFramingIndex"))
if mibBuilder.loadTexts: dsx1ForeFramingEntry.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingEntry.setDescription('A table entry containing DSX1 framing statistics information.')
dsx1ForeFramingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingIndex.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingIndex.setDescription('The number of this port.')
dsx1ForeFramingLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingLOSs.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingLOSs.setDescription('The number of secondsx in which Loss Of Signal (LOS) errors have been detected.')
dsx1ForeFramingLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingLCVs.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingLCVs.setDescription('The number of Line Code Violations (LCV) that have been detected.')
dsx1ForeFramingFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingFERRs.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingFERRs.setDescription('The number of Framing ERRor (FERR) events that have been detected.')
dsx1ForeFramingOOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingOOFs.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingOOFs.setDescription('The number of Out Of Frame (OOF) error events that have been detected.')
dsx1ForeFramingAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingAISs.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingAISs.setDescription('The number of secondsx in which Alarm Indication Signals (AIS) have been detected. AIS indicates that an upstream failure has been detected by the far end.')
dsx1ForeFramingB8ZSPatterns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingB8ZSPatterns.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingB8ZSPatterns.setDescription('The number of seconds in which B8ZS Pattern events have been detected.')
dsx1ForeFraming8Zeros = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFraming8Zeros.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFraming8Zeros.setDescription('The number of seconds in which 8 Zeros events have been detected.')
dsx1ForeFraming16Zeros = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFraming16Zeros.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFraming16Zeros.setDescription('The number of seconds in which 16 Zeros events have been detected.')
dsx1ForeFramingYellowAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingYellowAlarms.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingYellowAlarms.setDescription('The number of secondsx in which Yellow Alarm events have been detected.')
dsx1ForeFramingRedAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingRedAlarms.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingRedAlarms.setDescription('The number of secondsx in which Red Alarm events have been detected.')
dsx1ForeFramingBEEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeFramingBEEs.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeFramingBEEs.setDescription('The number of Bit Encoding Error (BEE) events that have been detected.')
dsx1ForeAtmTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2), )
if mibBuilder.loadTexts: dsx1ForeAtmTable.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeAtmTable.setDescription('A table of DSX1 ATM statistics information.')
dsx1ForeAtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1), ).setIndexNames((0, "Fore-DSX1-MIB", "dsx1ForeAtmIndex"))
if mibBuilder.loadTexts: dsx1ForeAtmEntry.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeAtmEntry.setDescription('A table entry containing DSX1 ATM statistics information.')
dsx1ForeAtmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeAtmIndex.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeAtmIndex.setDescription("The ifIndex of this port, actually it's currently the ifIndex of the associaated dsx1 port not the ATM port as currently they are assumed to be the same thing which of course they are not")
dsx1ForeAtmRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeAtmRxCells.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeAtmRxCells.setDescription('Number of ATM cells that were received.')
dsx1ForeAtmTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1ForeAtmTxCells.setStatus('current')
if mibBuilder.loadTexts: dsx1ForeAtmTxCells.setDescription('Number of non-null ATM cells that were transmitted.')
mibBuilder.exportSymbols("Fore-DSX1-MIB", dsx1ForeLineLength=dsx1ForeLineLength, dsx1ForePortModel=dsx1ForePortModel, dsx1ForeConfTable=dsx1ForeConfTable, dsx1ForeReceiveCode=dsx1ForeReceiveCode, dsx1ForeFdlBomConf=dsx1ForeFdlBomConf, dsx1ForeUpStreamAIS=dsx1ForeUpStreamAIS, dsx1ForeFdlConfiguration=dsx1ForeFdlConfiguration, dsx1ForeFdlPerfConf=dsx1ForeFdlPerfConf, dsx1ForeFramingAISs=dsx1ForeFramingAISs, dsx1ForeFramingFERRs=dsx1ForeFramingFERRs, dsx1ForeStatsGroup=dsx1ForeStatsGroup, dsx1ForeLineImpedance=dsx1ForeLineImpedance, dsx1ForeFramingLCVs=dsx1ForeFramingLCVs, dsx1ForeConfGroup=dsx1ForeConfGroup, dsx1ForeAtmEntry=dsx1ForeAtmEntry, dsx1ForeFramingLOSs=dsx1ForeFramingLOSs, dsx1ForeAtmIndex=dsx1ForeAtmIndex, dsx1ForeAtmRxCells=dsx1ForeAtmRxCells, dsx1ForeLineIndex=dsx1ForeLineIndex, dsx1ForeFramingIndex=dsx1ForeFramingIndex, dsx1ForeFramingEntry=dsx1ForeFramingEntry, dsx1ForeAdminStatus=dsx1ForeAdminStatus, dsx1ForeFramingRedAlarms=dsx1ForeFramingRedAlarms, dsx1ForeAtmTxCells=dsx1ForeAtmTxCells, dsx1ForeFraming8Zeros=dsx1ForeFraming8Zeros, PYSNMP_MODULE_ID=foreDsx1, dsx1ForeConfEntry=dsx1ForeConfEntry, dsx1ForeFramingTable=dsx1ForeFramingTable, dsx1ForeFramingYellowAlarms=dsx1ForeFramingYellowAlarms, dsx1ForeFramingB8ZSPatterns=dsx1ForeFramingB8ZSPatterns, dsx1ForeFraming16Zeros=dsx1ForeFraming16Zeros, foreDsx1=foreDsx1, dsx1ForeFramingBEEs=dsx1ForeFramingBEEs, dsx1ForeAtmTable=dsx1ForeAtmTable, dsx1ForeFramingOOFs=dsx1ForeFramingOOFs)
