#
# PySNMP MIB module BTI-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
btiModules, = mibBuilder.importSymbols("BTI-MIB", "btiModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, IpAddress, Gauge32, NotificationType, iso, Unsigned32, Integer32, MibIdentifier, ModuleIdentity, Counter32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "IpAddress", "Gauge32", "NotificationType", "iso", "Unsigned32", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter32", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
btiTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 1, 2))
btiTcMib.setRevisions(('2012-06-01 12:00', '2012-05-02 12:00', '2012-02-10 12:00', '2011-09-26 12:00', '2010-08-06 12:00', '2010-06-18 12:00', '2010-02-12 12:00', '2009-01-19 12:00', '2008-12-19 12:00', '2008-10-10 12:00', '2008-05-30 12:00', '2007-09-14 12:00', '2007-07-16 12:00', '2007-03-09 12:00', '2005-12-05 12:00', '2005-07-25 12:00', '2005-02-07 12:00', '2004-09-23 12:00', '2004-01-29 18:21', '2003-12-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: btiTcMib.setRevisionsDescriptions(('Updated for BTI 7000 Rel 10.2.0: - added new textual convention MirrorConfigType', 'Updated for BTI 7000 Rel 9.3.0: - added new XcvrProtocolType values: tenGeLanFecEPCMF, tenGeLanEFecEPCMF, otu2eFec, otu2eEFec', 'Updated for BTI 7000 Rel 9.2.0: - added value lf to NotifCodeType TC - added new textual convention LoopbackType', 'Updated for BTI 7000 Rel 9.1.0: - added values dla, rob, dcm and d40md to CpType TC - added values lolightRx to replUnitDegrade to NotifCodeType TC - added values osc, odcc, wdm and wch to NotifObjectType TC', 'Updated for BTI 7000 Rel 8.1.0: - changed status of ShelfConfigType TC to deprecated - added value ccm to CpType TC - added value mgmtVLan to PvxPortType TC', 'Updated for BTI 7000 Rel 7.3.2: - added EnvNotifCodeType TC - added environmental condition types unassigned through unsupported to NotifCodeType TC - added value env (environmental) to NotifObjectType TC', 'Updated for BTI 7000 Rel 7.3.0: - added values sts6c through sts72c to StsnType TC - added values vc3c and vc5c to VcnType TC - added values lockProg through tBdwUtlz to NotifCodeType TC - added values vc43c through pereCoS to NotifObjectType TC - added SyncSwEvtType textual convention used by new SONET synchronization event messages - added values gccOtu2 and generic to PvxPortType TC - added AreaID and DesignatedRouterPriority textual conventions to support OSPF feature - inserted copies of InetAddressType, InetAddress, InetAddressIPv4, InetAddressIPv6, InetAddressIPv4z, InetAddressIPv6z and InetAddressDNS TCs from RFC 4001', 'Updated for BTI 7000 Rel 7.2.0: - added values vc24c and vc2c to vcnType TC - renamed subOdu1Mbps155 value to subOdu1, removed unused subOdu1Mbps622 value for OdunType TC - added values default and critical-major to CondSeverity TC - added new TCs NotifCodeType and NotifObjectType to support Enhanced Trap Info and Configurable Alarm Severity features - added values testing, unknown, dormant, notPresent and lowerLayerDown to OperStatus TC - added value wideband1310 to PassivePortType TC - added value odu1otu2Fec to XcvrProtocolType TC - added new ProfileNameType TC for PVX configuration profiles', 'Updated for BTI 7000 Rel 7.1.2: - added new values for ProtSwEvtType TC - removed unused TC OtunType', 'Updated for BTI 7000 Rel 7.1.1: - spelling corrections made to TimeZone value identifiers - added textual conventions SwitchIdxType, ProtocolActionType, PvxPortType, PvxL1PortType, PowerFeedModeType', 'Updated for BTI 7000 Rel 7.1.0: - replaced references to Netstender with BTI 7000 - added tpr and pvx CP types - added tpr XCVR type - added new TCs FCType, OdunType, OtunType - added new values to XcvrProtocolType, BERType and PMMontype', 'Added a number of textual conventions: Unsigned64, InitializeCmd, OcnType, StsnType, StmnType, VcnType, MediaRateType, DuplexModeType, UpgradeCompleteStage, XCType, ProtSwOpCmd, ProtectionStatusType and PMMontype. Added new 10G protocols to XcvrProtocolType.', 'Defined new textual conventions BERType and ProtSwEvtType', 'Added a number of textual conventions: FixedX100, ShelfType, FiberType, WDMGrid, TimeZone, AdminStatus, OperStatus, OperStatQlfr, HoursAndMinutes, PassivePortType, XcvrProtocolType, PMIntervalType, and PMValidity.', 'Updated for Netstender Rel 4.1: - added new d32amd, wlm circuit packs - added new wm transceiver type', 'Updated Contact Info in Module Identity', 'Updated for Netstender Rel. 3.1: - added new SMF, NF, CS, WT and WR circuit packs, - added XcvrType textual convention.', 'Updated for Netstender Rel. 3.0: - Added new textual conventions relocated from NETSTENDER-MIB, - removed obsolete textual conventions; added new pack types', 'Updated for Netstender 2060 Rel. 2.1.3: - Added display hint for FixedX10 textual convention', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: btiTcMib.setLastUpdated('201205021200Z')
if mibBuilder.loadTexts: btiTcMib.setOrganization('BTI Systems Inc.')
if mibBuilder.loadTexts: btiTcMib.setContactInfo('Technical Support BTI Systems Inc. 50 Northside Road Ottawa, Ontario, Canada K2H 5Z6 (613) 248-9154 support@btisystems.com')
if mibBuilder.loadTexts: btiTcMib.setDescription('Textual conventions defined for BTI Systems MIBs.')
class FixedX10(TextualConvention, Integer32):
    description = 'This represents a fixed point number with a single digit after the decimal point. However, because SNMP does not support floats, the value represented is the actual value multiplied by 10. To derive the actual value, divide by 10 and keep the remainder as the value after the decimal point.'
    status = 'current'
    displayHint = 'd-1'

class FixedX100(TextualConvention, Integer32):
    description = 'This represents a fixed point number with two digits after the decimal point. However, because SNMP does not support floats, the value represented is the actual value multiplied by 100. To derive the actual value, divide by 100 and keep the remainder as the value after the decimal point.'
    status = 'current'
    displayHint = 'd-2'

class FixedX1000(TextualConvention, Integer32):
    description = 'This represents a fixed point number with 3 digits after the decimal point. However, because SNMP does not support floats, the value represented is the actual value multiplied by 1000. To derive the actual value, divide by 1000 and keep the remainder as the value after the decimal point.'
    status = 'current'
    displayHint = 'd-3'

class Unsigned64(TextualConvention, Counter64):
    description = 'Used for the transfer of 64-bit unsigned integral values. The value is based on the Counter64 type, but unlike the Counter64, it has 0-based semantics.'
    status = 'current'

class InitializeCmd(TextualConvention, Integer32):
    description = "Used to initialize an integral-valued object to 0. An object defined of this type must have an access of read-write. When read, the object will return the value 'idle'. When the object is set, the only allowable value is 'initialize'. Setting the value to initialize will result in the initialization of an associated integral-valued object."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("initialize", 2))

class ShelfType(TextualConvention, Integer32):
    description = 'An identifier that indicates if a shelf functions as a main shelf or as an expansion shelf.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("main", 1), ("expansion", 2))

class ShelfConfigType(TextualConvention, Integer32):
    description = 'Identifies the configuration for a shelf based on the mix and number of single width and double width slots.'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("twoSlot", 1), ("threeSlot", 2), ("fourSlot", 3), ("fiveSlot", 4), ("sixSlot", 5), ("fourSlotB", 6), ("fourSlotC", 7), ("fiveSlotB", 8), ("fiveSlotC", 9), ("unknown", 10))

class SlotType(TextualConvention, Integer32):
    description = 'An identifier that is used to indicate a type of slot on a network element shelf. The slots are differentiated based on the type of replaceable unit they accomodate. Regular slots are where most circuit packs are installed. The other types of slots are the dedicated locations for the shelf interface card and for the cooling unit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("regular", 1), ("shelfInterface", 2), ("coolingUnit", 3), ("acPowerUnit", 4))

class CpType(TextualConvention, Integer32):
    description = 'A categorization of types of circuit packs available for BTI Systems equipment based on functionality provided.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 20, 25, 29, 32, 33, 34, 35, 36, 37, 38, 39, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72))
    namedValues = NamedValues(("scp", 1), ("oba", 2), ("ola", 3), ("olam", 4), ("opa", 5), ("smf60", 6), ("smf80", 7), ("pmt1", 12), ("pmt2", 13), ("msi", 14), ("esi", 15), ("cu", 16), ("fllr", 17), ("smf40", 18), ("osc", 20), ("c8md", 25), ("c1adm", 29), ("cdsc", 32), ("d32md1", 33), ("d32md2", 34), ("d32md3", 35), ("d32md4", 36), ("d1adm", 37), ("d2adm", 38), ("d4adm", 39), ("spa", 41), ("oct", 43), ("sba", 44), ("smf30", 45), ("nf", 46), ("wt", 47), ("wr", 48), ("cs", 49), ("smf5", 50), ("smf10", 51), ("smf15", 52), ("smf20", 53), ("d32amd1", 54), ("d32amd2", 55), ("d32amd3", 56), ("d32amd4", 57), ("wm", 58), ("c8md1", 59), ("c8md2", 60), ("mxp", 61), ("c4md", 62), ("c2adm", 63), ("tpr", 64), ("pvx", 65), ("ccm", 66), ("wc200", 67), ("dla", 68), ("rob", 69), ("dcm", 70), ("d40md", 71), ("d96md", 72))

class OaType(TextualConvention, Integer32):
    description = 'A categorization of types of optical amplifiers available for the BTI Systems equipment based on amplification application.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 10, 11))
    namedValues = NamedValues(("oba", 1), ("ola", 2), ("opa", 3), ("olam", 4), ("spa", 10), ("sba", 11))

class XcvrType(TextualConvention, Integer32):
    description = 'A categorization of types of transceiver ports on wavelength translator, regenerator or manager cards based on wavelength management application.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("wt", 1), ("wr", 2), ("wm", 3), ("tpr", 4))

class AmdType(TextualConvention, Integer32):
    description = 'A categorization of types of Active Multiplexer-Demultiplexer facilities, based on type of AMD module type.'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("d32amd1", 1), ("d32amd2", 2), ("d32amd3", 3), ("d32amd4", 4))

class AmdPortType(TextualConvention, Integer32):
    description = 'A categorization of types of ports on an Active Multiplexer-Demultiplexer circuit pack.'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))
    namedValues = NamedValues(("line", 1), ("channel1", 2), ("channel2", 3), ("channel3", 4), ("channel4", 5), ("channel5", 6), ("channel6", 7), ("channel7", 8), ("channel8", 9), ("channel9", 10), ("channel10", 11), ("channel11", 12), ("channel12", 13), ("channel13", 14), ("channel14", 15), ("channel15", 16), ("channel16", 17), ("channel17", 18), ("channel18", 19), ("channel19", 20), ("channel20", 21), ("channel21", 22), ("channel22", 23), ("channel23", 24), ("channel24", 25), ("channel25", 26), ("channel26", 27), ("channel27", 28), ("channel28", 29), ("channel29", 30), ("channel30", 31), ("channel31", 32), ("channel32", 33), ("expansion", 34))

class OcnType(TextualConvention, Integer32):
    description = 'A categorization of types of SONET OC-N facility ports based on signal rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("oc1", 1), ("oc3", 2), ("oc12", 3), ("oc48", 4), ("oc192", 5), ("oc768", 6))

class StsnType(TextualConvention, Integer32):
    description = 'A categorization of types of SONET STS-N facilities based on signal rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("sts1", 1), ("sts3c", 2), ("sts12c", 3), ("sts48c", 4), ("sts192c", 5), ("sts768c", 6), ("sts6c", 7), ("sts9c", 8), ("sts15c", 9), ("sts18c", 10), ("sts21c", 11), ("sts24c", 12), ("sts30c", 13), ("sts36c", 14), ("sts72c", 15))

class StmnType(TextualConvention, Integer32):
    description = 'A categorization of types of SDH STM-N facility ports based on signal rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("stm1", 1), ("stm4", 2), ("stm16", 3), ("stm64", 4), ("stm246", 5))

class VcnType(TextualConvention, Integer32):
    description = 'A categorization of types of SDH VC-N facilities based on signal rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("vc2", 1), ("vc3", 2), ("vc4", 3), ("vc11", 4), ("vc12", 5), ("vc4c", 6), ("vc6c", 7), ("vc7c", 8), ("vc8c", 9), ("vc12c", 10), ("vc16c", 11), ("vc24c", 12), ("vc2c", 13), ("vc10c", 14), ("vc3c", 15), ("vc5c", 16))

class FcType(TextualConvention, Integer32):
    description = 'A categorization of types of Fiber Channel facility ports based on signal rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fc1g", 1), ("fc2g", 2), ("fc4g", 3))

class OdunType(TextualConvention, Integer32):
    description = 'A categorization of types of OTN ODU-N facility ports based on signal rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("odu1", 1), ("odu2", 2), ("odu3", 3), ("subOdu1", 4))

class CondReportType(TextualConvention, Integer32):
    description = "An object of this type is associated with active conditions reported in Trap messages. The condition report type is a coarse qualifier of the significance of the event that is being reported. The values defined are: - 'condition': reports non-alarmed conditions: events that are of general interest, and do not require immediate attention by an operator. - 'alarm': alarmed-conditions generally report a fault condition detected on the NE. Such events generally require immediate attention by an apropriate operator."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("condition", 1), ("alarm", 2))

class CondSeverity(TextualConvention, Integer32):
    description = "An object of this type is associated with active conditions reported in Trap messages. The condition severity is a more specific qualifier of the urgency of the event that is being reported. The values defined are: - 'minor': attributed to the least severe alarm conditions reported - 'major': attributed to somewhat more severe alarms - 'critical': attributed to the most severe alarm conditions - 'notAlarmed': for conditions that are of significance, but do not require follow-up action - 'notReported': for conditions that are of note, but are not reported by way of notification, and are only viewable as entries in the actCondTable - 'default': used only for setting the severity of a trap back to its original value. - 'critical-major': visible only when retrieving the current setting for severity. It indicates that the severity changes. If the corresponding entity is provisioned then the trap will be raised as critical otherwise it will be raised as major. This severity may not be set directly only by resetting a alarm to its default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("minor", 2), ("major", 3), ("critical", 4), ("notAlarmed", 5), ("notReported", 6), ("default", 7), ("critical-major", 8))

class CondServiceAffecting(TextualConvention, Integer32):
    description = "An object of this type is associated with active conditions reported bin Trap messages. A service affecting indicator provides a clear indication of whether or not the condition being reported has impacted the system's ability to continue to carry traffic."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("nonServiceAffecting", 1), ("serviceAffecting", 2))

class NotifCodeType(TextualConvention, Integer32):
    description = 'A list of the types of conditions, alarms and events that may be raised on the system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256), SingleValueConstraint(257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296))
    namedValues = NamedValues(("acpuFail", 1), ("acpuMiss", 2), ("acpuPlugin", 3), ("acpuUnk", 4), ("acpuUnplug", 5), ("actLpbkF", 6), ("actLpbkT", 7), ("ais", 8), ("aisL", 9), ("aisP", 10), ("ampCond", 11), ("ampTrans", 12), ("applDbRstPass", 13), ("autoProvFail", 14), ("bwMism", 15), ("cMism", 16), ("cmmtUpgrdPass", 17), ("connMea", 18), ("contBus", 19), ("contCom", 20), ("cuFail", 21), ("cuFail1uMj", 22), ("cuFail1uMn", 23), ("cuFeedFailMj", 24), ("cuFeedFailMn", 25), ("cuMiss", 26), ("cuPlugin", 27), ("cuUnk", 28), ("cuUnplug", 29), ("dbBkupFail", 30), ("dbBkupPass", 31), ("dbBkupProg", 32), ("dbDltProg", 33), ("dbLoadFail", 34), ("dbLoadPass", 35), ("dbRecvryFail", 36), ("dbRstProg", 37), ("dspCommFail", 38), ("eol", 39), ("esiMiss", 40), ("expShComDevUns", 41), ("expShComLnkDwn", 42), ("expShComLos", 43), ("feedAFail", 44), ("feedBFail", 45), ("frcdWkSwBk", 46), ("frcdWkSwPr", 47), ("fuseAlarm", 48), ("gfpPlm", 49), ("hiTemp", 50), ("invkDbDltFail", 51), ("invkDbDltPass", 52), ("invkDbRstFail", 53), ("invkDbRstPass", 54), ("invProv", 55), ("ipLckOut", 56), ("linkDown", 57), ("litChn", 58), ("loa", 59), ("lockoutOfPr", 60), ("lockoutOfWk", 61), ("lof", 62), ("lol", 63), ("lom", 64), ("lopP", 65), ("los", 66), ("loSync", 67), ("loTmRef", 68), ("lpbk", 69), ("manWkSwBk", 70), ("manWkSwPr", 71), ("normal", 72), ("obrhtso", 73), ("oscLos", 74), ("otnPlm", 75), ("packUpgrdFail", 76), ("portMea", 77), ("powerFail", 78), ("pwrBrwnt", 79), ("release", 80), ("relNumMea", 81), ("replUnitFail", 82), ("replUnitIdMea", 83), ("replUnitMea", 84), ("replUnitMiss", 85), ("replUnitPlugin", 86), ("replUnitUnk", 87), ("replUnitUnplug", 88), ("replUnitUns", 89), ("rfi", 90), ("rpf", 91), ("scpRestart", 92), ("scpRNChgFail", 93), ("scpRNChgPass", 94), ("scpRNChgProg", 95), ("sd", 96), ("siFail", 97), ("siMiss", 98), ("siPlugin", 99), ("siUnk", 100), ("siUnplug", 101), ("sqm", 102), ("swBnkAFail", 103), ("swBnkBFail", 104), ("syncPri", 105), ("syncSec", 106), ("sysChkFail", 107), ("sysChkPass", 108), ("sysCom", 109), ("sysLoadFail", 110), ("sysLoadPass", 111), ("sysUpgrdFail", 112), ("sysUpgrdPass", 113), ("sysUpgrdProg", 114), ("tCv", 115), ("tCvL", 116), ("tCvOtu", 117), ("tCvP", 118), ("tCvS", 119), ("tEb", 120), ("tEs", 121), ("tEsL", 122), ("tEsP", 123), ("tEsS", 124), ("tFcP", 125), ("tFcseRx", 126), ("tFrdr", 127), ("tFrer", 128), ("tFrgt", 129), ("tHpBbe", 130), ("tHpEb", 131), ("tHpEs", 132), ("tHpSes", 133), ("tHpUas", 134), ("tInvBlk", 135), ("tJabr", 136), ("tMsBbe", 137), ("tMsEb", 138), ("tMsEs", 139), ("tMsSes", 140), ("tMsUas", 141), ("tNumBitsCr", 142), ("tNumBytesCr", 143), ("tOsize", 145), ("tOtuBbe", 146), ("tOtuEb", 147), ("tOtuEs", 148), ("tOtuOfs", 149), ("tOtuSes", 150), ("tOtuUas", 151), ("tRsBbe", 152), ("tRsEb", 153), ("tRsEs", 154), ("tRsOfs", 155), ("tRsSes", 156), ("tRsUas", 157), ("tSefs", 158), ("tSefsOtu", 159), ("tSefsS", 160), ("tSemOtu", 161), ("tSes", 162), ("tSesL", 163), ("tSesP", 164), ("tSesS", 165), ("tTfrcRx", 166), ("tTfrcTx", 167), ("tUas", 168), ("tUasL", 169), ("tUasS", 170), ("tUasP", 171), ("tUncrCdWrd", 172), ("tUsize", 173), ("tWavelength", 174), ("talna", 175), ("tCtempHt", 176), ("tCtempHts", 177), ("tim", 178), ("tLtempHts", 179), ("tLtempLts", 180), ("tMsLossHt", 181), ("tObrHt", 182), ("tObrHts", 183), ("tOprBht", 184), ("tOprHt", 185), ("tOprLt", 186), ("tOprRht", 187), ("tOptBht", 188), ("tOptBlt", 189), ("tOptHt", 190), ("tOptLt", 191), ("tOptRht", 192), ("tOptRlt", 193), ("tplna", 194), ("tSSIOprHt", 195), ("tTempHt", 196), ("uneqP", 197), ("upgrdProg", 198), ("usrLckout", 199), ("wkSwBk", 200), ("wkSwPr", 201), ("wna", 202), ("oduPlm", 203), ("oci", 204), ("srvrUnReachable", 205), ("srvrUnRspsive", 206), ("authenFailed", 207), ("otuTti", 208), ("bdi", 209), ("lockProg", 210), ("syncSwitchPri", 211), ("syncSwitchSec", 212), ("syncSwitchInt", 213), ("tBdwUtlz", 214), ("unassigned", 215), ("airCompr", 216), ("airCond", 217), ("airDryr", 218), ("batDschrd", 219), ("battery", 220), ("clFan", 221), ("cpMajor", 222), ("cpMinor", 223), ("doorOpen", 224), ("engine", 225), ("engOprg", 226), ("explGs", 227), ("firDetr", 228), ("fire", 229), ("flood", 230), ("fuse", 231), ("gen", 232), ("generic", 233), ("hiAir", 234), ("hiHum", 235), ("hiWind", 236), ("hiWtr", 237), ("iceBuildup", 238), ("intruder", 239), ("lwBatvg", 240), ("lwFuel", 241), ("lwHum", 242), ("lwPres", 243), ("lwTemp", 244), ("lwWtr", 245), ("misc", 246), ("openDr", 247), ("power", 248), ("pump", 249), ("rect", 250), ("rectHi", 251), ("rectLo", 252), ("smoke", 253), ("toxicGas", 254), ("ventn", 255), ("unsupported", 256)) + NamedValues(("flFarEnd", 257), ("flNearEnd", 258), ("delayMax", 259), ("delayAvg", 260), ("delayVarMax", 261), ("delayVarAvg", 262), ("lolightRx", 263), ("lolightTx", 264), ("feim", 265), ("feci", 266), ("contComS", 267), ("contComE", 268), ("loSpecRx", 269), ("tLossRxHt", 270), ("iaocp", 271), ("iaocm", 272), ("iaocb", 273), ("apsd", 274), ("pmi", 275), ("uneqO", 276), ("aisO", 277), ("posRx", 278), ("posTx", 279), ("tObros", 280), ("chnDfc", 281), ("replUnitDegrade", 282), ("lf", 283), ("cnxMea", 284), ("cnxVldTmout", 285), ("posRxHigh", 286), ("posRxLow", 287), ("oprHighFail", 288), ("feedAFuseFail", 289), ("feedBFuseFail", 290), ("packPowerFail", 291), ("hts", 292), ("htThreshExceeded", 293), ("htsThreshExceeded", 294), ("htasUnsupported", 295), ("rcvdLockout", 296))

class EnvNotifCodeType(TextualConvention, Integer32):
    description = 'A list of the types of environmental conditions and alarms that may be raised on the system. It is a subset of the list of all alarms, conditions and event types identified in the NotifCodeType textual convention.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(50, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255))
    namedValues = NamedValues(("hiTemp", 50), ("unassigned", 215), ("airCompr", 216), ("airCond", 217), ("airDryr", 218), ("batDschrd", 219), ("battery", 220), ("clFan", 221), ("cpMajor", 222), ("cpMinor", 223), ("doorOpen", 224), ("engine", 225), ("engOprg", 226), ("explGs", 227), ("firDetr", 228), ("fire", 229), ("flood", 230), ("fuse", 231), ("gen", 232), ("generic", 233), ("hiAir", 234), ("hiHum", 235), ("hiWind", 236), ("hiWtr", 237), ("iceBuildup", 238), ("intruder", 239), ("lwBatvg", 240), ("lwFuel", 241), ("lwHum", 242), ("lwPres", 243), ("lwTemp", 244), ("lwWtr", 245), ("misc", 246), ("openDr", 247), ("power", 248), ("pump", 249), ("rect", 250), ("rectHi", 251), ("rectLo", 252), ("smoke", 253), ("toxicGas", 254), ("ventn", 255))

class NotifObjectType(TextualConvention, Integer32):
    description = 'A list of the types of objects on the system against which conditions, alarms and events may be raised.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58))
    namedValues = NamedValues(("amd", 1), ("eqpt", 2), ("fc", 3), ("fe", 4), ("ge", 5), ("ip", 6), ("oc12", 7), ("oc192", 8), ("oc3", 9), ("oc48", 10), ("oa", 11), ("ospf", 12), ("port", 13), ("stm1", 14), ("stm16", 15), ("stm4", 16), ("stm64", 17), ("sts1", 18), ("sts12c", 19), ("sts3c", 20), ("sts48c", 21), ("vc4", 22), ("vc412c", 23), ("vc416c", 24), ("vc424c", 25), ("vc44c", 26), ("vc46c", 27), ("vc47c", 28), ("vc48c", 29), ("xcvr", 30), ("lag", 31), ("secu", 32), ("xge", 33), ("bri", 34), ("odu1", 35), ("subodu1", 36), ("vc42c", 37), ("vc410c", 38), ("vc43c", 39), ("vc45c", 40), ("sts6c", 41), ("sts9c", 42), ("sts15c", 43), ("sts18c", 44), ("sts21c", 45), ("sts24c", 46), ("sts30c", 47), ("sts36c", 48), ("sts72c", 49), ("perEvc", 50), ("perCos", 51), ("env", 52), ("slaMsmt", 53), ("osc", 54), ("odcc", 55), ("wdm", 56), ("wch", 57), ("ntpassoc", 58))

class FiberType(TextualConvention, Integer32):
    description = 'The types of optical fiber that may be used in fiber optic system networks.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("dsf", 2), ("ndsf", 3), ("nzdsf", 4), ("multimode", 5))

class WDMGrid(TextualConvention, Integer32):
    description = 'The types of optical grid schemes that may be in use for wavelength division multiplexing according to spacing of optical wavelengths.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("ghz50", 2), ("ghz100", 3), ("ghz200", 4), ("nm20", 5))

class TimeZone(TextualConvention, Integer32):
    description = 'A list of world time zones based on geo-political identifiers.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255), SingleValueConstraint(256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328))
    namedValues = NamedValues(("afghanistan", 1), ("albania", 2), ("algeria", 3), ("americanSamoa", 4), ("andorra", 5), ("argentina", 6), ("argentinaWesternProv", 7), ("anguilla", 8), ("antarctica", 9), ("antarcticaDavis", 10), ("antarcticaDumontDurville", 11), ("antarcticaMawson", 12), ("antigua", 13), ("armenia", 14), ("aruba", 15), ("ascension", 16), ("australiaAustralianCapitalTerritory", 17), ("australiaLordHoweIsland", 18), ("australiaNewSouthWales", 19), ("australiaNorthernTerritory", 20), ("australiaQueensland", 21), ("australiaSouth", 22), ("australiaTasmania", 23), ("australiaVictoria", 24), ("australiaWestern", 25), ("austria", 26), ("azerbaijan", 27), ("azores", 28), ("bahamas", 29), ("bahrain", 30), ("balearicIslands", 31), ("bangladesh", 32), ("barbados", 33), ("belarus", 34), ("belgium", 35), ("belize", 36), ("benin", 37), ("bermuda", 38), ("bhutan", 39), ("bolivia", 40), ("bonaire", 41), ("bosniaHercegovina", 42), ("botswana", 43), ("brazilAcre", 44), ("brazilAtlanticIslands", 45), ("brazilEast", 46), ("brazilWest", 47), ("britishIndianOceanTerritoryChagos", 48), ("britishVirginIslands", 49), ("brunei", 50), ("bulgaria", 51), ("burkinaFaso", 52), ("burundi", 53), ("cambodia", 54), ("cameroon", 55), ("canadaAtlantic", 56), ("canadaCentral", 57), ("canadaEastern", 58), ("canadaMountain", 59), ("canadaNewfoundland", 60), ("canadaPacificYukon", 61), ("canadaSaskatchewan", 62), ("canaryIslands", 63), ("cantonEnderburyIslands", 64), ("capeVerde", 65), ("carolineIslands", 66), ("caymanIslands", 67), ("centralAfricanRepublic", 68), ("chad", 69), ("channelIslands", 70), ("chathamIsland", 71), ("chile", 72), ("chinaPeoplesRepublic", 73), ("christmasIslands", 74), ("cocosIslands", 75), ("colombia", 76), ("congo", 77), ("cookIslands", 78), ("costaRica", 79), ("coteDivoire", 80), ("croatia", 81), ("cuba", 82), ("curacao", 83), ("cyprus", 84), ("czechRepublic", 85), ("denmark", 86), ("djibouti", 87), ("dominica", 88), ("dominicanRepublic", 89), ("easterIsland", 90), ("ecuador", 91), ("egypt", 92), ("elSalvador", 93), ("england", 94), ("equatorialGuinea", 95), ("eritrea", 96), ("estonia", 97), ("ethiopia", 98), ("falklandIslands", 99), ("faroeIsland", 100), ("fiji", 101), ("finland", 102), ("france", 103), ("francePierreMiquelon", 104), ("frenchGuiana", 105), ("frenchPolynesia", 106), ("gabon", 107), ("galapagos", 108), ("gambia", 109), ("gambierIsland", 110), ("georgia", 111), ("germany", 112), ("ghana", 113), ("gibraltar", 114), ("greece", 115), ("greenland", 116), ("greenlandScoresbysun", 117), ("greenlandThule", 118), ("greenwichMeanTimeUtc", 119), ("grenada", 120), ("grenadines", 121), ("guadeloupe", 122), ("guam", 123), ("guatemala", 124), ("guinea", 125), ("guineaBissau", 126), ("guyana", 127), ("haiti", 128), ("honduras", 129), ("hongKong", 130), ("hungary", 131), ("iceland", 132), ("india", 133), ("indonesiaCentral", 134), ("indonesiaEast", 135), ("indonesiaWest", 136), ("iraq", 137), ("iran", 138), ("irelandRepublicOf", 139), ("israel", 140), ("italy", 141), ("jamaica", 142), ("japan", 143), ("johnstonIsland", 144), ("jordan", 145), ("kazakhstan", 146), ("kenya", 147), ("kiribati", 148), ("kiribatiPhoenixIslands", 149), ("koreaDemRepublicOf", 150), ("koreaRepublicOf", 151), ("kosrae", 152), ("kuwait", 153), ("kwajalein", 154), ("kyrgyzstan", 155), ("laos", 156), ("latvia", 157), ("lebanon", 158), ("leewardIslands", 159), ("lesotho", 160), ("liberia", 161), ("libya", 162), ("liechtenstein", 163), ("lithuania", 164), ("luxembourg", 165), ("macedonia", 166), ("madagascar", 167), ("madeira", 168), ("malawi", 169), ("malaysia", 170), ("maldives", 171), ("mali", 172), ("mallorcaIsland", 173), ("malta", 174), ("marianaIsland", 175), ("marquesasIslands", 176), ("marshallIsland", 177), ("martinique", 178), ("mauritania", 179), ("mauritius", 180), ("mayotte", 181), ("melilla", 182), ("mexico", 183), ("mexicoBajaCalifnorte", 184), ("mexicoNayarit", 185), ("mexicoSinaloa", 186), ("mexicoSonora", 187), ("midwayIsland", 188), ("moldova", 189), ("moldovianreppridnestrovye", 190), ("moluccas", 191), ("monaco", 192), ("mongolia", 193), ("morocco", 194), ("mozambique", 195), ("myanmar", 196), ("namibia", 197), ("nauruRepublicOf", 198), ("nepal", 199), ("netherlands", 200), ("netherlandsAntilles", 201), ("nevisMontserrat", 202), ("newCaledonia", 203), ("newHebrides", 204), ("newZealand", 205), ("newZealandTokelauIslands", 206), ("nicaragua", 207), ("niger", 208), ("nigeria", 209), ("niueIsland", 210), ("norfolkIsland", 211), ("northernIreland", 212), ("northernMarianaIslands", 213), ("northSumatra", 214), ("norway", 215), ("oman", 216), ("pakistan", 217), ("palau", 218), ("panama", 219), ("papuaNewGuinea", 220), ("paraguay", 221), ("peru", 222), ("philippines", 223), ("pingelap", 224), ("poland", 225), ("ponapeIsland", 226), ("portugal", 227), ("principeIsland", 228), ("puertoRico", 229), ("qatar", 230), ("reunion", 231), ("romania", 232), ("russianFederationChitayakutsk", 233), ("russianFederationIrkutskulanude", 234), ("russianFederationKaliningrad", 235), ("russianFederationKamchatkaanadyr", 236), ("russianFederationKrasnoyarsktomsk", 237), ("russianFederationMagadankolyma", 238), ("russianFederationMoscowStPetersburg", 239), ("russianFederationNovosibirskomsk", 240), ("russianFederationSamaraizhevsk", 241), ("russianFederationVladivostokkhabarovsk", 242), ("russianFederationYekaterinburgperm", 243), ("rwanda", 244), ("saba", 245), ("samoa", 246), ("sanMarino", 247), ("saotomePrincipe", 248), ("saudiArabia", 249), ("scotland", 250), ("senegal", 251), ("seychelles", 252), ("sierraLeone", 253), ("singapore", 254), ("slovakia", 255)) + NamedValues(("slovenia", 256), ("societyIsland", 257), ("solomonIslands", 258), ("somalia", 259), ("southAfrica", 260), ("southSumatra", 261), ("spain", 262), ("sriLanka", 263), ("stChristopher", 264), ("stCroix", 265), ("stHelena", 266), ("stJohn", 267), ("stKittsNevis", 268), ("stLucia", 269), ("stMaarten", 270), ("stPierreMiquelon", 271), ("stThomas", 272), ("stVincent", 273), ("sudan", 274), ("suriname", 275), ("swaziland", 276), ("sweden", 277), ("switzerland", 278), ("syria", 279), ("tahiti", 280), ("taiwan", 281), ("tajikistan", 282), ("tanzania", 283), ("thailand", 284), ("togo", 285), ("tonga", 286), ("trinidadAndTobago", 287), ("tuamotuIsland", 288), ("tubuaiIsland", 289), ("tunisia", 290), ("turkey", 291), ("turkmenistan", 292), ("turksAndCaicosIslands", 293), ("tuvalu", 294), ("uganda", 295), ("ukraine", 296), ("unitedArabEmirates", 297), ("unitedKingdom", 298), ("uruguay", 299), ("usaAlaska", 300), ("usaAleutian", 301), ("usaArizona", 302), ("usaCentral", 303), ("usaEastern", 304), ("usaHawaii", 305), ("usaIndianaEast", 306), ("usaMountain", 307), ("usaPacific", 308), ("uzbekistan", 309), ("vanuatu", 310), ("vaticanCity", 311), ("venezuela", 312), ("vietnam", 313), ("virginIslands", 314), ("wakeIsland", 315), ("wales", 316), ("wallisAndFutunaIslands", 317), ("westernSahara", 318), ("windwardIslands", 319), ("yemen", 320), ("yugoslavia", 321), ("zaireHautZaire", 322), ("zaireKasai", 323), ("zaireKinshasaMbandaka", 324), ("zaireKivu", 325), ("zaireShaba", 326), ("zambia", 327), ("zimbabwe", 328))

class AdminStatus(TextualConvention, Integer32):
    description = 'An indicator of the status of a resource according to whether or not the resource has been administratively enabled or disabled to perform its provisioned function.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("autoEnabled", 3))

class OperStatus(TextualConvention, Integer32):
    description = 'An indicator of the status of a resource according to whether or not it is both enabled to perform its function and capable of performing its function.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class OperStatQlfr(TextualConvention, OctetString):
    description = 'A qualification of the operational status of a resource. The information is in the form of a textual display string, which lists 0 or more comma-delimited qualification identifiers. The set of qualifiers includes: - nr: Normal - anr: Abnormal - au: Autonomous - auma: Autonomous Management - ma: Management - maanr: Management Abnormal - ains: Auto In-service (Auto-enabled) - flt: Fault - mea: Mismatch - swdl: Software Download - mt: Maintenance - sgeo: Supporting Entity Outage - ueq: Unequipped - wrk: Working - comm: Communication Failure - lpbk: Loopback - stdby: Standby - frcd: Forced - lkdo: Locked Out'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 65)

class HoursAndMinutes(TextualConvention, OctetString):
    description = "A textual string representation of a time duration value expressed as the number of hours and minutes. The format of the string is to be HHH-MM, where - HHH is the number of hours and can be 0 to 999 - MM is the number of minutes and can be 0 to 59. The '-' character must be used to separate the hours and minutes values, and the string is expected to be NULL-terminated."
    status = 'current'
    displayHint = '7a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 7)

class PassivePortType(TextualConvention, Integer32):
    description = 'A listing of port types found on passive circuit packs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45))
    namedValues = NamedValues(("channel1", 1), ("channel2", 2), ("channel3", 3), ("channel4", 4), ("channel5", 5), ("channel6", 6), ("channel7", 7), ("channel8", 8), ("channel9", 9), ("channel10", 10), ("channel11", 11), ("channel12", 12), ("channel13", 13), ("channel14", 14), ("channel15", 15), ("channel16", 16), ("channel17", 17), ("channel18", 18), ("channel19", 19), ("channel20", 20), ("channel21", 21), ("channel22", 22), ("channel23", 23), ("channel24", 24), ("channel25", 25), ("channel26", 26), ("channel27", 27), ("channel28", 28), ("channel29", 29), ("channel30", 30), ("channel31", 31), ("channel32", 32), ("line", 33), ("cband", 34), ("passthru", 35), ("upgrade", 36), ("cwdm", 37), ("dwdm", 38), ("blue", 39), ("red", 40), ("channel53", 41), ("channel55", 42), ("channel57", 43), ("channel59", 44), ("wideband1310", 45))

class XcvrProtocolType(TextualConvention, Integer32):
    description = 'A listing of the types of communication protocols that a optical transceiver port can be configured to carry.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("none", 1), ("autodetect", 2), ("escon", 3), ("fc100", 4), ("fc200", 5), ("fddi", 6), ("fe", 7), ("ge", 8), ("oc3", 9), ("oc12", 10), ("oc48", 11), ("oc48fec", 12), ("smpte259", 13), ("smpte344", 14), ("smpte292", 15), ("stm1", 16), ("stm4", 17), ("stm16", 18), ("tenGeLan", 19), ("tenGeLanFec", 20), ("oc192", 21), ("oc192Fec", 22), ("stm64", 23), ("stm64Fec", 24), ("fc400", 25), ("fc1200", 26), ("tenGeLanEFec", 27), ("oc192EFec", 28), ("stm64EFec", 29), ("odu1otu2Fec", 30), ("tenGeLanFecEPCMF", 31), ("tenGeLanEFecEPCMF", 32), ("otu2eFec", 33), ("otu2eEFec", 34), ("tenGeLanFecEPV3", 35), ("tenGeLanEFecEPV3", 36))

class PMIntervalType(TextualConvention, Integer32):
    description = 'The type of time interval used to collect performance monitoring statistics.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("min15", 1), ("day1", 2), ("untimed", 3))

class PMValidity(TextualConvention, Integer32):
    description = 'An indicator of the degree of validity attributed to a reported performance monitoring value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("complete", 1), ("notAvailable", 2), ("partialCount", 3))

class BERType(TextualConvention, Integer32):
    description = 'A measure of the bit error rate in a received signal, expressed as an exponential.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 1), ("tenExpMinus9", 2), ("tenExpMinus8", 3), ("tenExpMinus7", 4), ("tenExpMinus6", 5), ("tenExpMinus5", 6), ("tenExpMinus4", 7), ("tenExpMinus3", 8), ("tenExpMinus10", 9), ("tenExpMinus11", 10), ("tenExpMinus12", 11))

class ProtSwEvtType(TextualConvention, Integer32):
    description = 'When a notification is generated to signal that a protection switching event occurred, an object of this type is used to indicate which type of protection switching event occurred.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("autoWorkSwProt", 1), ("autoWorkSwBack", 2), ("manWorkSwProt", 3), ("manWorkSwBack", 4), ("frcdWorkSwProt", 5), ("frcdWorkSwBack", 6), ("lockoutOfWork", 7), ("lockoutOfProt", 8), ("releaseProtSw", 9))

class SyncSwEvtType(TextualConvention, Integer32):
    description = 'When a notification is generated to signal that a synchronization switching event occurred, an object of this type is used to indicate which type of switching event occurred.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("syncSwToPrimaryRef", 1), ("syncSwToSecondaryRef", 2), ("syncSwToInternal", 3))

class MediaRateType(TextualConvention, Integer32):
    description = 'The media rate for a data interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("autoNegotiated", 2), ("fd100", 3), ("hd100", 4), ("fd10", 5), ("hd10", 6), ("fd1000", 7), ("hd1000", 8))

class DuplexModeType(TextualConvention, Integer32):
    description = 'The duplex operational mode for a data interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("halfDuplex", 1), ("fullDuplex", 2))

class MirrorConfigType(TextualConvention, Integer32):
    description = 'Mirror configuration as applied on a physical ethernet interface'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("mtp", 2), ("mfp-ingress", 3), ("mfp-egress", 4), ("mfp-both", 5))

class UpgradeCompleteStage(TextualConvention, Integer32):
    description = 'A list of stages involved in the software upgrade procedure used on the network element. Notifications are provided during the course of a software upgrade, making reference to one of the values in this list to indicate the progress of upgrade.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("inactive", 1), ("started", 2), ("loadStarted", 3), ("loadDone", 4), ("reboot", 5), ("done", 6), ("systemDone", 7), ("autoNr", 8))

class XCType(TextualConvention, Integer32):
    description = 'The types of cross connections that can be provisioned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("oneWay", 1), ("twoWay", 2), ("oneWayPr", 3), ("twoWayPr", 4), ("oneWayBr", 5), ("twoWayBr", 6))

class ProtSwOpCmd(TextualConvention, Integer32):
    description = 'Used to perform a protection switch operation on a facility configured as part of a protection group or pairing.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("noOp", 1), ("manProtSw", 2), ("frcdProtSw", 3), ("lockout", 4), ("release", 5))

class ProtectionStatusType(TextualConvention, Integer32):
    description = 'A status indicator for a facility involved in a protection switching grouping.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("active", 2), ("standby", 3), ("forced", 4), ("lockout", 5))

class PMMontype(TextualConvention, Integer32):
    description = 'A list of performance monitoring monitored types supported for various monitored entites on the system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76))
    namedValues = NamedValues(("caseTemp", 1), ("laser1Temp", 2), ("laser2Temp", 3), ("opr", 4), ("ssiopr", 5), ("opt", 6), ("msInsLoss", 7), ("effectiveGain", 8), ("fsoopt", 9), ("laser1Current", 10), ("laser2Current", 11), ("laser1Power", 12), ("laser2Power", 13), ("obr", 14), ("voa", 15), ("temp", 16), ("supplyVoltage", 17), ("lbc", 18), ("cvs", 19), ("ess", 20), ("sess", 21), ("sefss", 22), ("rseb", 23), ("rsbbe", 24), ("rses", 25), ("rsses", 26), ("rsofs", 27), ("cv", 28), ("es", 29), ("ses", 30), ("invblk", 31), ("nbitcr", 32), ("nbytcr", 33), ("uncrcdw", 34), ("cvp", 35), ("esp", 36), ("sesp", 37), ("uasp", 38), ("fcp", 39), ("hpeb", 40), ("hpbbe", 41), ("hpes", 42), ("hpses", 43), ("hpuas", 44), ("tfrcrx", 45), ("tfrctx", 46), ("frdr", 47), ("fcse", 48), ("usize", 49), ("osize", 50), ("frgt", 51), ("jabr", 52), ("cvl", 53), ("esl", 54), ("sesl", 55), ("uasl", 56), ("mseb", 57), ("msbbe", 58), ("mses", 59), ("msses", 60), ("msuas", 61), ("otueb", 62), ("otubbe", 63), ("otues", 64), ("otuses", 65), ("otuofs", 66), ("uass", 67), ("rsuas", 68), ("uas", 69), ("otuuas", 70), ("farEndFL", 71), ("nearEndFL", 72), ("delayMax", 73), ("delayAvg", 74), ("delayVarMax", 75), ("delayVarAvg", 76))

class SwitchIdxType(TextualConvention, Integer32):
    description = 'An object of this type is associated with the index range of switch module. Switch module is a logical entity which can contail multiple circuit packs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 12)

class ProtocolActionType(TextualConvention, Integer32):
    description = 'This it behavior of the packets on the switch'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("discard", 1), ("peer", 2), ("tunnel", 3))

class PvxPortType(TextualConvention, Integer32):
    description = 'The identifying characteristic of the port. Ports are numbers sequentially for each port type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("gigE", 1), ("xGigE", 2), ("lag", 3), ("gccOtu2", 4), ("generic", 5), ("mgmtVLan", 6))

class PvxL1PortType(TextualConvention, Integer32):
    description = 'L2 port type: gigbit ethernet or 10 gigbit ethernet'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gigE", 1), ("xGigE", 2))

class MonitorPeriodType(TextualConvention, Integer32):
    description = 'SLA measurement monitor period type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("min15", 1), ("hour24", 2))

class CommandStateType(TextualConvention, Integer32):
    description = 'SLA measurement command state type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("ready", 1), ("start", 2), ("inProgress", 3), ("testFailed", 4), ("stop", 5), ("notSet", 6), ("rmepNotReady", 7))

class SlaTestRole(TextualConvention, Integer32):
    description = 'SLA measurement test role.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("initiator", 1), ("responder", 2))

class PmTestCmdState(TextualConvention, Integer32):
    description = 'SLA measurement test command state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("enable", 1), ("pmSetupInProgress", 2), ("pmSetupFailed", 3), ("pmIsRunning", 4), ("disable", 5))

class CirTestResult(TextualConvention, Integer32):
    description = 'CIR test result.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pass", 1), ("fail", 2))

class PowerFeedModeType(TextualConvention, Integer32):
    description = 'This determines the power feed mode for a given shelf.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ac", 1), ("dc", 2), ("none", 3), ("both", 4))

class ProfileNameType(TextualConvention, OctetString):
    description = "Profile Names are restricted to the character set of upper case ASCII characters, the digits 0-9 and the '_' (underscore) character, e.g. [A-Z0-9_]. Any row creation operation for a profile name containing any character outside this set will be rejected with a 'noCreation' error code."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class AreaID(TextualConvention, IpAddress):
    description = 'An OSPF Area Identifier.'
    status = 'current'

class DesignatedRouterPriority(TextualConvention, Integer32):
    description = 'The values defined for the priority of a system for becoming the designated router.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class LoopbackType(TextualConvention, Integer32):
    description = 'The type of loopback on a port'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noLoopback", 0), ("facilityLpbk", 1), ("terminalLpbk", 2))

class InetAddressType(TextualConvention, Integer32):
    description = 'A value that represents a type of Internet address. unknown(0) An unknown address type. This value MUST be used if the value of the corresponding InetAddress object is a zero-length string. It may also be used to indicate an IP address that is not in one of the formats defined below. ipv4(1) An IPv4 address as defined by the InetAddressIPv4 textual convention. ipv6(2) An IPv6 address as defined by the InetAddressIPv6 textual convention. ipv4z(3) A non-global IPv4 address including a zone index as defined by the InetAddressIPv4z textual convention. ipv6z(4) A non-global IPv6 address including a zone index as defined by the InetAddressIPv6z textual convention. dns(16) A DNS domain name as defined by the InetAddressDNS textual convention. Each definition of a concrete InetAddressType value must be accompanied by a definition of a textual convention for use with that InetAddressType. To support future extensions, the InetAddressType textual convention SHOULD NOT be sub-typed in object type definitions. It MAY be sub-typed in compliance statements in order to require only a subset of these address types for a compliant implementation. Implementations must ensure that InetAddressType objects and any dependent objects (e.g., InetAddress objects) are consistent. An inconsistentValue error must be generated if an attempt to change an InetAddressType object would, for example, lead to an undefined InetAddress value. In particular, InetAddressType/InetAddress pairs must be changed together if the address type changes (e.g., from ipv6(2) to ipv4(1)).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), ("dns", 16))

class InetAddress(TextualConvention, OctetString):
    description = "Denotes a generic Internet address. An InetAddress value is always interpreted within the context of an InetAddressType value. Every usage of the InetAddress textual convention is required to specify the InetAddressType object that provides the context. It is suggested that the InetAddressType object be logically registered before the object(s) that use the InetAddress textual convention, if they appear in the same logical row. The value of an InetAddress object must always be consistent with the value of the associated InetAddressType object. Attempts to set an InetAddress object to a value inconsistent with the associated InetAddressType must fail with an inconsistentValue error. When this textual convention is used as the syntax of an index object, there may be issues with the limit of 128 sub-identifiers specified in SMIv2, STD 58. In this case, the object definition MUST include a 'SIZE' clause to limit the number of potential instance sub-identifiers; otherwise the applicable constraints MUST be stated in the appropriate conceptual row DESCRIPTION clauses, or in the surrounding documentation if there is no single DESCRIPTION clause that is appropriate."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class InetAddressIPv4(TextualConvention, OctetString):
    description = 'Represents an IPv4 network address: Octets Contents Encoding 1-4 IPv4 address network-byte order The corresponding InetAddressType value is ipv4(1). This textual convention SHOULD NOT be used directly in object definitions, as it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with InetAddressType, as a pair.'
    status = 'current'
    displayHint = '1d.1d.1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class InetAddressIPv6(TextualConvention, OctetString):
    description = 'Represents an IPv6 network address: Octets Contents Encoding 1-16 IPv6 address network-byte order The corresponding InetAddressType value is ipv6(2). This textual convention SHOULD NOT be used directly in object definitions, as it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with InetAddressType, as a pair.'
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class InetAddressIPv4z(TextualConvention, OctetString):
    description = 'Represents a non-global IPv4 network address, together with its zone index: Octets Contents Encoding 1-4 IPv4 address network-byte order 5-8 zone index network-byte order The corresponding InetAddressType value is ipv4z(3). The zone index (bytes 5-8) is used to disambiguate identical address values on nodes that have interfaces attached to different zones of the same scope. The zone index may contain the special value 0, which refers to the default zone for each scope. This textual convention SHOULD NOT be used directly in object definitions, as it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with InetAddressType, as a pair.'
    status = 'current'
    displayHint = '1d.1d.1d.1d%4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class InetAddressIPv6z(TextualConvention, OctetString):
    description = 'Represents a non-global IPv6 network address, together with its zone index: Octets Contents Encoding 1-16 IPv6 address network-byte order 17-20 zone index network-byte order The corresponding InetAddressType value is ipv6z(4). The zone index (bytes 17-20) is used to disambiguate identical address values on nodes that have interfaces attached to different zones of the same scope. The zone index may contain the special value 0, which refers to the default zone for each scope. This textual convention SHOULD NOT be used directly in object definitions, as it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with InetAddressType, as a pair.'
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x%4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class InetAddressDNS(TextualConvention, OctetString):
    description = 'Represents a DNS domain name. The name SHOULD be fully qualified whenever possible. The corresponding InetAddressType is dns(16). The DESCRIPTION clause of InetAddress objects that may have InetAddressDNS values MUST fully describe how (and when) these names are to be resolved to IP addresses. The resolution of an InetAddressDNS value may require to query multiple DNS records (e.g., A for IPv4 and AAAA for IPv6). The order of the resolution process and which DNS record takes precedence depends on the configuration of the resolver. This textual convention SHOULD NOT be used directly in object definitions, as it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with InetAddressType, as a pair.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class ZeroBasedCounter32(TextualConvention, Gauge32):
    description = 'This TC describes an object that counts events with the following semantics: objects of this type will be set to zero(0) on creation and will thereafter count appropriate events, wrapping back to zero(0) when the value 2^32 is reached. Provided that an application discovers the new object within the minimum time to wrap, it can use the initial value as a delta since it last polled the table of which this object is part. It is important for a management station to be aware of this minimum time and the actual time between polls, and to discard data if the actual time is too long or there is no defined minimum time. Typically, this TC is used in tables where the INDEX space is constantly changing and/or the TimeFilter mechanism is in use.'
    status = 'current'

class LldpChassisIdSubtype(TextualConvention, Integer32):
    description = "This TC describes the source of a chassis identifier. The enumeration 'chassisComponent(1)' represents a chassis identifier based on the value of entPhysicalAlias object (defined in IETF RFC 2737) for a chassis component (i.e., an entPhysicalClass value of 'chassis(3)'). The enumeration 'interfaceAlias(2)' represents a chassis identifier based on the value of ifAlias object (defined in IETF RFC 2863) for an interface on the containing chassis. The enumeration 'portComponent(3)' represents a chassis identifier based on the value of entPhysicalAlias object (defined in IETF RFC 2737) for a port or backplane component (i.e., entPhysicalClass value of 'port(10)' or 'backplane(4)'), within the containing chassis. The enumeration 'macAddress(4)' represents a chassis identifier based on the value of a unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order), of a port on the containing chassis as defined in IEEE Std 802-2001. The enumeration 'networkAddress(5)' represents a chassis identifier based on a network address, associated with a particular chassis. The encoded address is actually composed of two fields. The first field is a single octet, representing the IANA AddressFamilyNumbers value for the specific address type, and the second field is the network address value. The enumeration 'interfaceName(6)' represents a chassis identifier based on the value of ifName object (defined in IETF RFC 2863) for an interface on the containing chassis. The enumeration 'local(7)' represents a chassis identifier based on a locally defined value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7), ("notPresent", 8))

class LldpChassisId(TextualConvention, OctetString):
    description = "This TC describes the format of a chassis identifier string. Objects of this type are always used with an associated LldpChassisIdSubtype object, which identifies the format of the particular LldpChassisId object instance. If the associated LldpChassisIdSubtype object has a value of 'chassisComponent(1)', then the octet string identifies a particular instance of the entPhysicalAlias object (defined in IETF RFC 2737) for a chassis component (i.e., an entPhysicalClass value of 'chassis(3)'). If the associated LldpChassisIdSubtype object has a value of 'interfaceAlias(2)', then the octet string identifies a particular instance of the ifAlias object (defined in IETF RFC 2863) for an interface on the containing chassis. If the particular ifAlias object does not contain any values, another chassis identifier type should be used. If the associated LldpChassisIdSubtype object has a value of 'portComponent(3)', then the octet string identifies a particular instance of the entPhysicalAlias object (defined in IETF RFC 2737) for a port or backplane component within the containing chassis. If the associated LldpChassisIdSubtype object has a value of 'macAddress(4)', then this string identifies a particular unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order), of a port on the containing chassis as defined in IEEE Std 802-2001. If the associated LldpChassisIdSubtype object has a value of 'networkAddress(5)', then this string identifies a particular network address, encoded in network byte order, associated with one or more ports on the containing chassis. The first octet contains the IANA Address Family Numbers enumeration value for the specific address type, and octets 2 through N contain the network address value in network byte order. If the associated LldpChassisIdSubtype object has a value of 'interfaceName(6)', then the octet string identifies a particular instance of the ifName object (defined in IETF RFC 2863) for an interface on the containing chassis. If the particular ifName object does not contain any values, another chassis identifier type should be used. If the associated LldpChassisIdSubtype object has a value of 'local(7)', then this string identifies a locally assigned Chassis ID."
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class LldpPortIdSubtype(TextualConvention, Integer32):
    description = "This TC describes the source of a particular type of port identifier used in the LLDP MIB. The enumeration 'interfaceAlias(1)' represents a port identifier based on the ifAlias MIB object, defined in IETF RFC 2863. The enumeration 'portComponent(2)' represents a port identifier based on the value of entPhysicalAlias (defined in IETF RFC 2737) for a port component (i.e., entPhysicalClass value of 'port(10)'), within the containing chassis. The enumeration 'macAddress(3)' represents a port identifier based on a unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order), which has been detected by the agent and associated with a particular port (IEEE Std 802-2001). The enumeration 'networkAddress(4)' represents a port identifier based on a network address, detected by the agent and associated with a particular port. The enumeration 'interfaceName(5)' represents a port identifier based on the ifName MIB object, defined in IETF RFC 2863. The enumeration 'agentCircuitId(6)' represents a port identifier based on the agent-local identifier of the circuit (defined in RFC 3046), detected by the agent and associated with a particular port. The enumeration 'local(7)' represents a port identifier based on a value locally assigned."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7), ("notPresent", 8))

class LldpPortId(TextualConvention, OctetString):
    description = "This TC describes the format of a port identifier string. Objects of this type are always used with an associated LldpPortIdSubtype object, which identifies the format of the particular LldpPortId object instance. If the associated LldpPortIdSubtype object has a value of 'interfaceAlias(1)', then the octet string identifies a particular instance of the ifAlias object (defined in IETF RFC 2863). If the particular ifAlias object does not contain any values, another port identifier type should be used. If the associated LldpPortIdSubtype object has a value of 'portComponent(2)', then the octet string identifies a particular instance of the entPhysicalAlias object (defined in IETF RFC 2737) for a port or backplane component. If the associated LldpPortIdSubtype object has a value of 'macAddress(3)', then this string identifies a particular unicast source address (encoded in network byte order and IEEE 802.3 canonical bit order) associated with the port (IEEE Std 802-2001). If the associated LldpPortIdSubtype object has a value of 'networkAddress(4)', then this string identifies a network address associated with the port. The first octet contains the IANA AddressFamilyNumbers enumeration value for the specific address type, and octets 2 through N contain the networkAddress address value in network byte order. If the associated LldpPortIdSubtype object has a value of 'interfaceName(5)', then the octet string identifies a particular instance of the ifName object (defined in IETF RFC 2863). If the particular ifName object does not contain any values, another port identifier type should be used. If the associated LldpPortIdSubtype object has a value of 'agentCircuitId(6)', then this string identifies a agent-local identifier of the circuit (defined in RFC 3046). If the associated LldpPortIdSubtype object has a value of 'local(7)', then this string identifies a locally assigned port ID."
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

mibBuilder.exportSymbols("BTI-TC-MIB", ProtocolActionType=ProtocolActionType, PvxPortType=PvxPortType, AmdPortType=AmdPortType, PMMontype=PMMontype, btiTcMib=btiTcMib, CpType=CpType, PassivePortType=PassivePortType, NotifCodeType=NotifCodeType, SlotType=SlotType, OperStatus=OperStatus, FixedX1000=FixedX1000, AmdType=AmdType, FixedX100=FixedX100, SyncSwEvtType=SyncSwEvtType, MirrorConfigType=MirrorConfigType, MonitorPeriodType=MonitorPeriodType, XcvrType=XcvrType, InetAddressIPv4=InetAddressIPv4, PowerFeedModeType=PowerFeedModeType, WDMGrid=WDMGrid, OperStatQlfr=OperStatQlfr, PmTestCmdState=PmTestCmdState, XcvrProtocolType=XcvrProtocolType, UpgradeCompleteStage=UpgradeCompleteStage, LldpChassisId=LldpChassisId, InetAddressIPv6z=InetAddressIPv6z, TimeZone=TimeZone, HoursAndMinutes=HoursAndMinutes, InetAddress=InetAddress, Unsigned64=Unsigned64, PMIntervalType=PMIntervalType, AdminStatus=AdminStatus, ProtSwOpCmd=ProtSwOpCmd, InetAddressType=InetAddressType, FcType=FcType, DuplexModeType=DuplexModeType, ProtectionStatusType=ProtectionStatusType, StsnType=StsnType, EnvNotifCodeType=EnvNotifCodeType, CommandStateType=CommandStateType, LldpChassisIdSubtype=LldpChassisIdSubtype, LldpPortId=LldpPortId, LoopbackType=LoopbackType, FiberType=FiberType, ShelfConfigType=ShelfConfigType, PvxL1PortType=PvxL1PortType, InetAddressIPv6=InetAddressIPv6, ZeroBasedCounter32=ZeroBasedCounter32, CondServiceAffecting=CondServiceAffecting, InetAddressDNS=InetAddressDNS, XCType=XCType, VcnType=VcnType, MediaRateType=MediaRateType, LldpPortIdSubtype=LldpPortIdSubtype, PMValidity=PMValidity, CirTestResult=CirTestResult, OaType=OaType, NotifObjectType=NotifObjectType, ShelfType=ShelfType, DesignatedRouterPriority=DesignatedRouterPriority, CondSeverity=CondSeverity, AreaID=AreaID, CondReportType=CondReportType, InitializeCmd=InitializeCmd, SwitchIdxType=SwitchIdxType, FixedX10=FixedX10, OdunType=OdunType, ProfileNameType=ProfileNameType, InetAddressIPv4z=InetAddressIPv4z, PYSNMP_MODULE_ID=btiTcMib, StmnType=StmnType, OcnType=OcnType, SlaTestRole=SlaTestRole, BERType=BERType, ProtSwEvtType=ProtSwEvtType)
