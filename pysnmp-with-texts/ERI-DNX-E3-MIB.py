#
# PySNMP MIB module ERI-DNX-E3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-E3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:05:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
DecisionType, DataSwitch, LinkPortAddress, devices, LinkCmdStatus, OneByteField, trapSequence, PortStatus, FunctionSwitch = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "DecisionType", "DataSwitch", "LinkPortAddress", "devices", "LinkCmdStatus", "OneByteField", "trapSequence", "PortStatus", "FunctionSwitch")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, iso, Integer32, Unsigned32, NotificationType, Counter64, ModuleIdentity, TimeTicks, Bits, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "iso", "Integer32", "Unsigned32", "NotificationType", "Counter64", "ModuleIdentity", "TimeTicks", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eriDNXE3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 11))
if mibBuilder.loadTexts: eriDNXE3MIB.setLastUpdated('200204080000Z')
if mibBuilder.loadTexts: eriDNXE3MIB.setOrganization('Eastern Research, Inc.')
if mibBuilder.loadTexts: eriDNXE3MIB.setContactInfo('Customer Service Postal: Eastern Research, Inc. 225 Executive Drive Moorestown, NJ 08057 Phone: +1-800-337-4374 Email: support@erinc.com')
if mibBuilder.loadTexts: eriDNXE3MIB.setDescription('The ERI Enterprise MIB Module for the DNX E3 Device.')
dnxE3 = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8))
e3Config = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1))
e3Diag = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2))
e3PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1), )
if mibBuilder.loadTexts: e3PortConfigTable.setStatus('current')
if mibBuilder.loadTexts: e3PortConfigTable.setDescription('This is the E3 Port Configuration table which consists of an entry for each of the E3 cards. The total number of entries depends on the number of E3 cards in the Node.')
e3PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1), ).setIndexNames((0, "ERI-DNX-E3-MIB", "e3PortCfgAddr"))
if mibBuilder.loadTexts: e3PortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: e3PortConfigEntry.setDescription('The conceptual row of the E3 Port Configuration table. A row in this table cannot be added or deleted, only modified.')
e3PortCfgAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PortCfgAddr.setStatus('current')
if mibBuilder.loadTexts: e3PortCfgAddr.setDescription('This number uniquely identifies a E3 port resource. This number will be used throughout the system to identify a unique resource.')
e3PortCfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PortCfgResource.setStatus('current')
if mibBuilder.loadTexts: e3PortCfgResource.setDescription('Uniquely identifies an E3 Port in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
e3Timing = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("internal", 0), ("loop", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3Timing.setStatus('current')
if mibBuilder.loadTexts: e3Timing.setDescription('Determines the mode of E3 transmit timing provided by the receive clock. When internal, timing is provided by an on-board oscillator.')
e3ShortCable = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 4), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3ShortCable.setStatus('current')
if mibBuilder.loadTexts: e3ShortCable.setDescription("Indicates the line build out of the E3 transmitter. 'Yes' when attached to a cable less than 50 feet long.")
e3CmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 1, 1, 5), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3CmdStatus.setStatus('current')
if mibBuilder.loadTexts: e3CmdStatus.setDescription("The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row E3 Link Commands used in SET Command (1..199) update-link-config(1), Change existing Link Configuration Response States used in GET RESPONSE Command (200..399) update-successful (201) Link data has been successfully changed E3 Port Config Error Codes used in GET RESPONSE Command (400..699) err-general-link-config-error (400) Unknown link configuration error occurred err-invalid-link-command (403) Unrecognized link command-action err-invalid-link-rem-loop (408) Remote Loop type not valid for e3 frame type err-invalid-link-ais (409) Unrecognized e3 AIS selection err-device-in-standby (414) Can't change config for designated Standby device err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name. err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big")
e3E1LinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2), )
if mibBuilder.loadTexts: e3E1LinkConfigTable.setStatus('current')
if mibBuilder.loadTexts: e3E1LinkConfigTable.setDescription("This is the E3 E1 Link Configuration table which consists of an entry for each of the card's 16 links. The total number of entries depends on the number of E3 cards in the Node.")
e3E1LinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1), ).setIndexNames((0, "ERI-DNX-E3-MIB", "e3E1CfgLinkAddr"))
if mibBuilder.loadTexts: e3E1LinkConfigEntry.setStatus('current')
if mibBuilder.loadTexts: e3E1LinkConfigEntry.setDescription('The conceptual row of the E3 E1 Link Configuration table. A row in this table cannot be added or deleted, only modified.')
e3E1CfgLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3E1CfgLinkAddr.setStatus('current')
if mibBuilder.loadTexts: e3E1CfgLinkAddr.setDescription('This number uniquely identifies a E3 E1 link resource. This number will be used throughout the system to identify a unique resource.')
e3E1CfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3E1CfgResource.setStatus('current')
if mibBuilder.loadTexts: e3E1CfgResource.setDescription('Uniquely identifies an E3 E1 Channel in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
e3E1CfgLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1CfgLinkName.setStatus('current')
if mibBuilder.loadTexts: e3E1CfgLinkName.setDescription('This is the user friendly text name to identify the link.')
e3E1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 4), PortStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1Status.setStatus('current')
if mibBuilder.loadTexts: e3E1Status.setDescription('Dictates the current status of the link, in-service or out-of-service.')
e3E1Clear = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("framed", 1), ("unframed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1Clear.setStatus('current')
if mibBuilder.loadTexts: e3E1Clear.setDescription('Determines if the port supports E1 unframed clear mode.')
e3E1Framing = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("e1", 0), ("e1Crc", 1), ("e1Cas", 2), ("e1CasCrc", 3), ("e1Unframed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1Framing.setStatus('current')
if mibBuilder.loadTexts: e3E1Framing.setDescription('Determines the type of framing used on the line. When value of e3E1Clear is set to unframed (2), the only valid framing option is: e1Unframed(4).')
e3E1NetLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 7), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1NetLoop.setStatus('current')
if mibBuilder.loadTexts: e3E1NetLoop.setDescription("Determines whether or not the module should respond to loop diagnostic commands received from the network supplier. Select 'enable' unless the commands are to be passed to another E3 device.")
e3E1RAI = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 8), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1RAI.setStatus('current')
if mibBuilder.loadTexts: e3E1RAI.setDescription("Causes the module to discard data and send a yellow alarm if it is in a red alarm condition after a 3 second period. 'Yes' must be chosen if the network supplier is a common carrier, such as a telephone company.")
e3E1UnusedTSs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("busy", 0), ("idle", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1UnusedTSs.setStatus('current')
if mibBuilder.loadTexts: e3E1UnusedTSs.setDescription("Determines the whether the code that will be transmitted over the unused links will be 'idle' or 'busy' (all 1's).")
e3E1NationalBits = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 10), OneByteField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1NationalBits.setStatus('current')
if mibBuilder.loadTexts: e3E1NationalBits.setDescription('Enables E1 National S-bits to be set to zero or one. This single byte field can be changed to set the values of the E1 NFA byte in odd frames as depicted below: sa8 sa7 sa6 sa5 sa4 reserved bits --- --- --- --- --- ------------- 1 1 1 1 1 0 0 0 = F8 (default) Values should be entered in Hex. If reserved bits are changed, an error code (427) will be returned in the command status. ')
e3E1CfgCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 11), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1CfgCmdStatus.setStatus('current')
if mibBuilder.loadTexts: e3E1CfgCmdStatus.setDescription("The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row E3-E1 Link Commands used in SET Command (1..199) update(1) Change existing Link Configuration inServiceAll (7) Change Link Status to in-service for all 16 links. copyToAll (9) Copy E1 Link configuration to all other links within the same device outOfServiceAll (12) Change Link Status to out-of-service for all 16 links. Response States used in GET RESPONSE Command (100..199) update-successful (101) Link data has been successfully changed insvc-successful (107) All Links have been successfully placed In Service copy-successful (109) E1 Link data has been successfully copied to other links oos-successful (112) All Links have been successfully placed Out of Service E3-E1 Link Config Error Codes used in GET RESPONSE Command (400..699) err-general-link-config-error (400) Unknown link configuration error occurred err-invalid-link-status (401) Unrecognized link status setting err-invalid-link-framing (402) Line framing type not valid for link type err-invalid-link-command (403) Unrecognized link command-action err-invalid-network-loop (410) Unrecognized network loop setting err-invalid-yellow-alrm (411) Unrecognized yellow alarm setting err-invalid-idle-code (413) Unrecognized idle code err-device-in-standby (414) Can't change config for designated Standby device err-invalid-link-bits (427) Reserved E1 bits must be left at zero. err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big")
e3E1InterNational = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 1, 2, 1, 12), OneByteField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3E1InterNational.setStatus('current')
if mibBuilder.loadTexts: e3E1InterNational.setDescription('Enables InterNational S(i) Spare bit to be set to zero or one. This single byte field can be changed to set the values of the Bit 1 of TS0 G.704 frame as depicted below: reserved bits S(i) -------------------------- ----- 0 0 0 0 0 0 0 1 = 01 (default) Values should be entered in Hex. If reserved bits are changed, an error code (427) will be returned in the command status. ')
e3FramerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1), )
if mibBuilder.loadTexts: e3FramerStatusTable.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusTable.setDescription("This is the E-3 Framer Status table which consists of a single entry for each card's Framer Display. The total number of entries depends on the number of E3 cards in the nest.")
e3FramerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1), ).setIndexNames((0, "ERI-DNX-E3-MIB", "e3FramerStatusAddr"))
if mibBuilder.loadTexts: e3FramerStatusEntry.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusEntry.setDescription('The conceptual row of the Framer table. A row in this table cannot be added or deleted, only modified.')
e3FramerStatusAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusAddr.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusAddr.setDescription('This number uniquely identifies an e3 Framer resource. This number will be used throughout the system to identify a unique resource.')
e3FramerStatusResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusResource.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusResource.setDescription('This number uniquely identifies an e3 Framer link resource. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table Entry.')
e3FramerStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 8, 32, 64, 2147483647))).clone(namedValues=NamedValues(("ok", 0), ("ais", 8), ("lof", 32), ("los", 64), ("errors", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusState.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusState.setDescription('Determines the current line condition status of the Framer. ok (0) - No Alarm ais (8) - Sending All Ones lof (32) - Loss/Out of Frame los (64) - Loss of Signal errors (2147483647) - Multiple Errors displays raw bit field value ')
e3FramerStatusErrSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusErrSecs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusErrSecs.setDescription('This is the total number of errored seconds.')
e3FramerStatusOOFErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusOOFErrs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusOOFErrs.setDescription('This is the number of seconds an Out Of Frame alignment error was declared.')
e3FramerStatusAISSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusAISSecs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusAISSecs.setDescription('This is the number of seconds an Alarm Indication Signal was declared.')
e3FramerStatusFramingErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusFramingErrs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusFramingErrs.setDescription('Indicates the number of Framing Errors.')
e3FramerStatusLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 37, 38))).clone(namedValues=NamedValues(("off", 0), ("e3-local", 1), ("e3-line", 3), ("e3-payload", 4), ("liu-local", 37), ("liu-line", 38)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3FramerStatusLoop.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusLoop.setDescription('The Loop status for the Framer as well as the Line Interface Unit.')
e3FramerStatusBertState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(50, 61, 62))).clone(namedValues=NamedValues(("bertOff", 50), ("framed-2047", 61), ("framed-2-15th-inv", 62)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3FramerStatusBertState.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusBertState.setDescription(' Indicates the Bert State. bertOff (50) - Turns the BERT off framed-2047 - Framed 2047 framed-2-15th - Framed 2^15-1 Inverted ')
e3FramerStatusBertSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusBertSecs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusBertSecs.setDescription('Indicates the Bert Duration in Seconds.')
e3FramerStatusBertErrSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusBertErrSecs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusBertErrSecs.setDescription('Indicates the number of errored seconds since the Bert is running.')
e3FramerStatusBertSync = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 12), DataSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusBertSync.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusBertSync.setDescription('Indicates the Bert Synchronization as being ON or OFF.')
e3FramerStatusLiuRLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusLiuRLOSs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusLiuRLOSs.setDescription('This is the number of seconds recorded for Receive Loss of Signal.')
e3FramerStatusLiuRLOLs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusLiuRLOLs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusLiuRLOLs.setDescription('This is the number of seconds recorded for Receive Loss of Lock.')
e3FramerStatusLiuLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramerStatusLiuLCVs.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusLiuLCVs.setDescription('This is the number of seconds recorded for the Line Code Violation.')
e3FramerStatusInsErrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2))).clone(namedValues=NamedValues(("frame-alignment", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3FramerStatusInsErrMode.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusInsErrMode.setDescription("Determines the status of the current Insert Error mode associated with the framer. In order to insert an error, the e3FramerStatusCmdStatus must be sent in a SET PDU with a value of 'insertError'.")
e3FramerStatusCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 14, 16, 101, 114, 116, 200, 202, 203, 205, 206, 208, 500, 501, 502))).clone(namedValues=NamedValues(("ready-for-command", 0), ("update", 1), ("clearErrors", 14), ("insertError", 16), ("update-successful", 101), ("clear-successful", 114), ("insert-successful", 116), ("err-general-framer-error", 200), ("err-invalid-loop-type", 202), ("err-invalid-bert-type", 203), ("err-test-in-progress", 205), ("err-field-cannot-be-set", 206), ("err-invalid-command", 208), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3FramerStatusCmdStatus.setStatus('current')
if mibBuilder.loadTexts: e3FramerStatusCmdStatus.setDescription('This is the command status for the Framer Row. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row E3 Framer Action Commands used in SET Command (1..99) update (1) Can be used optionally when activating loops and berts in order to get status code back in response clearErrors (14) Resets all error counters and bert test time to zero insertError (16) Inserts the current invalid bit pattern as indicated by the value of e3FramerStatusCmdStatus. Response States used in GET RESPONSE Command (100..199) update-successful (101) Test action has been successfully performed clear-successful (114) Error counts have been successfully cleared insert-successful (116) Errored bits have been successfully inserted The Error Codes used in GET RESPONSE Command (200..799) err-general-framer-error (200) Unknown request error occurred. err-invalid-loop-type (202) Unrecognized loop selection err-invalid-bert-type (203) Unrecognized bert selection err-test-in-progress (205) Requested action cannot be performed during bert err-field-cannot-be-set (206) Read-only field was included in SET request err-invalid-command (208) Unrecognized framer Command requested err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big')
dnxE3Enterprise = ObjectIdentity((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 0))
if mibBuilder.loadTexts: dnxE3Enterprise.setStatus('current')
if mibBuilder.loadTexts: dnxE3Enterprise.setDescription('ERI DNX E3 Enterprise for Alarms/Events')
e3PortConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 0, 1)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-E3-MIB", "e3PortCfgAddr"), ("ERI-DNX-E3-MIB", "e3CmdStatus"))
if mibBuilder.loadTexts: e3PortConfigTrap.setStatus('current')
if mibBuilder.loadTexts: e3PortConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the configuration for a given E3 Port entry.')
e3E1ConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 8, 0, 2)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-E3-MIB", "e3E1CfgLinkAddr"), ("ERI-DNX-E3-MIB", "e3E1CfgCmdStatus"))
if mibBuilder.loadTexts: e3E1ConfigTrap.setStatus('current')
if mibBuilder.loadTexts: e3E1ConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the Link configuration for a given E3-E1 channel entry.')
mibBuilder.exportSymbols("ERI-DNX-E3-MIB", e3FramerStatusErrSecs=e3FramerStatusErrSecs, dnxE3Enterprise=dnxE3Enterprise, e3E1CfgResource=e3E1CfgResource, e3PortConfigTrap=e3PortConfigTrap, e3E1LinkConfigTable=e3E1LinkConfigTable, e3E1NetLoop=e3E1NetLoop, e3FramerStatusLiuRLOLs=e3FramerStatusLiuRLOLs, e3FramerStatusBertErrSecs=e3FramerStatusBertErrSecs, e3FramerStatusBertSecs=e3FramerStatusBertSecs, e3E1CfgLinkAddr=e3E1CfgLinkAddr, e3FramerStatusResource=e3FramerStatusResource, e3E1UnusedTSs=e3E1UnusedTSs, e3E1ConfigTrap=e3E1ConfigTrap, e3Diag=e3Diag, e3E1NationalBits=e3E1NationalBits, e3FramerStatusState=e3FramerStatusState, e3FramerStatusCmdStatus=e3FramerStatusCmdStatus, e3E1LinkConfigEntry=e3E1LinkConfigEntry, e3E1CfgCmdStatus=e3E1CfgCmdStatus, e3FramerStatusOOFErrs=e3FramerStatusOOFErrs, e3FramerStatusLoop=e3FramerStatusLoop, e3FramerStatusBertState=e3FramerStatusBertState, dnxE3=dnxE3, e3E1Status=e3E1Status, e3E1Clear=e3E1Clear, e3PortConfigTable=e3PortConfigTable, e3FramerStatusAISSecs=e3FramerStatusAISSecs, e3FramerStatusInsErrMode=e3FramerStatusInsErrMode, e3Config=e3Config, e3FramerStatusEntry=e3FramerStatusEntry, PYSNMP_MODULE_ID=eriDNXE3MIB, eriDNXE3MIB=eriDNXE3MIB, e3Timing=e3Timing, e3FramerStatusTable=e3FramerStatusTable, e3CmdStatus=e3CmdStatus, e3E1RAI=e3E1RAI, e3E1CfgLinkName=e3E1CfgLinkName, e3FramerStatusBertSync=e3FramerStatusBertSync, e3E1InterNational=e3E1InterNational, e3E1Framing=e3E1Framing, e3FramerStatusAddr=e3FramerStatusAddr, e3ShortCable=e3ShortCable, e3FramerStatusLiuLCVs=e3FramerStatusLiuLCVs, e3PortCfgAddr=e3PortCfgAddr, e3FramerStatusLiuRLOSs=e3FramerStatusLiuRLOSs, e3FramerStatusFramingErrs=e3FramerStatusFramingErrs, e3PortConfigEntry=e3PortConfigEntry, e3PortCfgResource=e3PortCfgResource)
