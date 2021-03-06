#
# PySNMP MIB module CISCOSB-DEVICEPARAMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-DEVICEPARAMS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, Counter64, ObjectIdentity, MibIdentifier, Gauge32, Counter32, NotificationType, iso, Bits, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter32", "NotificationType", "iso", "Bits", "IpAddress", "Unsigned32")
PhysAddress, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention", "TruthValue")
rndDeviceParams = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2))
rndDeviceParams.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rndDeviceParams.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rndDeviceParams.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rndDeviceParams.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rndDeviceParams.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rndDeviceParams.setDescription('This private MIB module defines general Parameters private MIBs.')
rndBridgeType = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48))).clone(namedValues=NamedValues(("reb", 1), ("ceb", 2), ("ceblb", 3), ("xeb", 4), ("xeb1", 5), ("rebsx", 6), ("rtb", 7), ("ltb", 8), ("tre", 9), ("rtre", 10), ("xtb", 11), ("ete", 12), ("rete", 13), ("ielb", 30), ("leb", 31), ("openGate12", 32), ("openGate4", 33), ("ran", 34), ("itlb", 35), ("gatelinx", 36), ("openGate2", 37), ("ogRanTR", 38), ("rdapter", 39), ("ogVan", 40), ("wanGate", 41), ("ogRubE", 42), ("ogRubT", 43), ("wanGateI", 44), ("vGate4", 45), ("lre", 46), ("mrt", 47), ("vGate2", 48)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndBridgeType.setStatus('current')
if mibBuilder.loadTexts: rndBridgeType.setDescription('Identification of the switch001 bridge type.')
rndInactiveArpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndInactiveArpTimeOut.setStatus('current')
if mibBuilder.loadTexts: rndInactiveArpTimeOut.setDescription('This variable defines the maximum time period that can pass between ARP requests concerning an entry in the ARP table. After this time period, the entry is deleted from the table.')
rndBridgeAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 3))
rndErrorDesc = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndErrorDesc.setStatus('current')
if mibBuilder.loadTexts: rndErrorDesc.setDescription('A textual description of the enterprise-specific trap sent to the Network Management Station by the switch001 managed device.')
rndErrorSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("info", 0), ("warning", 1), ("error", 2), ("fatal-error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndErrorSeverity.setStatus('current')
if mibBuilder.loadTexts: rndErrorSeverity.setDescription('The severity type of the enterprise-specific trap sent to the Network Management Station by the switch001 managed device.')
rndBrgVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndBrgVersion.setStatus('current')
if mibBuilder.loadTexts: rndBrgVersion.setDescription('The bridge version.')
rndBrgFeatures = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndBrgFeatures.setStatus('current')
if mibBuilder.loadTexts: rndBrgFeatures.setDescription('A bit mask that defines the features supported by a particular configuration of this network element: __________________________________________ | Byte 1|Byte 2 |Byte 3 | ....|Byte 20 | |87654321| | 87654321| |________|_______________________________| Byte1 : bit1: TX Block mask bit2: Source Routing Encapulation bit3: SNA/SDLC bit4: Frame Relay bit5: SNMP bit6: LAN Manager bit7: High Performance bit8: Translation Byte2 : bit1: DEC Router bit2: IPX Router bit3: IP Router Byte3 : bit1: Dial Up Backup bit2: COD bit3: FACS bit4: Load Balance bit5: Remote Configuration bit6: RIP 2 bit7: OSPF bit8: IPX RIP/SAP Filter Byte4 : bit1: BootP Server bit2: BootP Client bit3: Compression bit4: V25.bis bit5: ISDN bit6: CODv2 bit7: NSPF bit8: UDP Relay Byte5 bit1:VirtualLAN bit2:Static IP Multicast bit3:IP Redundancy bit4:CCM2 bit5:ISDN Bonding bit6:Backup Link Selection -- for the VAN/Rdapter ver 4.0 bit7:IP/IPX Forwarding -- for the WANgate ver 4.0 bit8:Improved COD Byte6 bit1: Server Disptacher bit2: ISDN_US -- for the VANSX/WANGATE ver 5.0 bit3: PPP bit4: IP Rip Filter -- for Vgate3 bit5: Zero Hop Routing -- for Vgate3 bit6: ISDN Japan bit7: PPP-Security Byte7 bit1: With unmanaged Switch bit2: 2 LANs bit3: OSPF Ver 2.0 bit4: FACS Ver 2.0 bit5: Multiple WEB Farm bit6: Backup Server bit7: Check Connectivity bit8: WSD multiplexing Byte8 bit1: MRT3 bit2: WSD Redundancy bit3: DHCP Server bit4: WSD Connection Limit bit5: WSD Distributed System bit6: WSD Load Report bit7: WSD super farm bit8: RadWiz leased line Byte9 bit1: PPP IP address negotiaton bit2: DNS bit3: Nat bit4: WSD Static proximity bit5: WSD Dynamic proximity bit6: WSD Proxy bit7: WSD Proximity client bit8: MAC Load balancing Byte10 bit1: Unnum Inf bit2: Power Supply redundancy bit3: MRT PPP Compression bit4: ZHR Apolo bit5: Copy port bit6: UDP Relay 2.0 bit7: NVRAM bit8: URL table Byte11 bit1: URL super farm bit2: NAT on LAN bit3: Remote Con bit4: AP5000 bit5: Session tracking bit6: Mirroring bit7: Alias IP bit8: CSD Nat Byte12 bit1: content check bit2: mlb virtual ip bit3: reserved CISCOSB bit4: csd nat exception bit5: statistics monitor bit6: reserved-for-radware ')
rndBrgLicense = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndBrgLicense.setStatus('current')
if mibBuilder.loadTexts: rndBrgLicense.setDescription('This parameter is used for entering a s/w license number for a device. A separate license number is supplied for each device.')
rndIpHost = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7))
rndCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2), )
if mibBuilder.loadTexts: rndCommunityTable.setStatus('current')
if mibBuilder.loadTexts: rndCommunityTable.setDescription('The community table of the agent')
rndCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1), ).setIndexNames((0, "CISCOSB-DEVICEPARAMS-MIB", "rndCommunityMngStationAddr"), (1, "CISCOSB-DEVICEPARAMS-MIB", "rndCommunityString"))
if mibBuilder.loadTexts: rndCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: rndCommunityEntry.setDescription(' The row definition for this table.')
rndCommunityMngStationAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityMngStationAddr.setStatus('current')
if mibBuilder.loadTexts: rndCommunityMngStationAddr.setDescription('The management station that will be allowed to communicate with the agent IP address')
rndCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityString.setStatus('current')
if mibBuilder.loadTexts: rndCommunityString.setDescription('The community string with which the management station will communicate with the agent')
rndCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2), ("super", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityAccess.setStatus('current')
if mibBuilder.loadTexts: rndCommunityAccess.setDescription('The allowed access to this management station')
rndCommunityTrapsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("snmpV1", 1), ("snmpV2", 2), ("snmpV3", 3), ("trapsDisable", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityTrapsEnable.setStatus('current')
if mibBuilder.loadTexts: rndCommunityTrapsEnable.setDescription('Should the agent send traps to the management station, and what version is required')
rndCommunityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("invalid", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityStatus.setStatus('current')
if mibBuilder.loadTexts: rndCommunityStatus.setDescription('The status of this entry. If the status is invalid the community entry will be deleted')
rndCommunityPortSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityPortSecurity.setStatus('current')
if mibBuilder.loadTexts: rndCommunityPortSecurity.setDescription('If enabled the device will only receive SNMP messages from the port, through which this NMS is reachable from the device.')
rndCommunityOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityOwner.setStatus('current')
if mibBuilder.loadTexts: rndCommunityOwner.setDescription('The owner of this community')
rndCommunityTrapDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rndCommunityTrapDestPort.setStatus('current')
if mibBuilder.loadTexts: rndCommunityTrapDestPort.setDescription('The transport protocol (usually UDP) port to which traps to the management station represebted by this entry will be sent. The default is the well-known IANA assigned port number for SNMP traps. This object is relevant only if rndCommunityTrapsEnable has a value different from trapsDisable.')
rlMridTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 3), )
if mibBuilder.loadTexts: rlMridTable.setStatus('current')
if mibBuilder.loadTexts: rlMridTable.setDescription('The MRID related configurations table of the agent')
rlMridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 3, 1), ).setIndexNames((0, "CISCOSB-DEVICEPARAMS-MIB", "rndCommunityMngStationAddr"), (1, "CISCOSB-DEVICEPARAMS-MIB", "rndCommunityString"))
if mibBuilder.loadTexts: rlMridEntry.setStatus('current')
if mibBuilder.loadTexts: rlMridEntry.setDescription(' The row definition for this table.')
rlMridConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMridConnection.setStatus('current')
if mibBuilder.loadTexts: rlMridConnection.setDescription('The router instance connecting the NMS who accessed the agent through the community table entry corresponding to the keys of this entry.')
rlManagedMrid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlManagedMrid.setStatus('current')
if mibBuilder.loadTexts: rlManagedMrid.setDescription('The router instance currently managed by the NMS who accessed the agent through the community table entry corresponding to the keys of this entry ')
rndManagedTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndManagedTime.setStatus('current')
if mibBuilder.loadTexts: rndManagedTime.setDescription('The time will be sent in the format hhmmss')
rndManagedDate = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndManagedDate.setStatus('current')
if mibBuilder.loadTexts: rndManagedDate.setDescription('The date will be sent in the format ddmmyy')
rndBaseBootVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndBaseBootVersion.setStatus('current')
if mibBuilder.loadTexts: rndBaseBootVersion.setDescription('Defines the boot version of the product.')
rndIpHostManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 4))
rndIpHostManagementSupported = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 4, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndIpHostManagementSupported.setStatus('current')
if mibBuilder.loadTexts: rndIpHostManagementSupported.setDescription('ifindex manage supported.')
rndIpHostManagementIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 7, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndIpHostManagementIfIndex.setStatus('current')
if mibBuilder.loadTexts: rndIpHostManagementIfIndex.setDescription('if supported manage , indicate ifindex, if 0 thaen disable')
genGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 11))
genGroupHWVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 11, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genGroupHWVersion.setStatus('current')
if mibBuilder.loadTexts: genGroupHWVersion.setDescription('Defines the HW version of the product.')
genGroupConfigurationSymbol = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 11, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: genGroupConfigurationSymbol.setStatus('current')
if mibBuilder.loadTexts: genGroupConfigurationSymbol.setDescription('Defines the Configuration Symbol attached to any hardware module manufactured by LANNET. One single character A..Z defines the CS version.')
genGroupHWStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ok", 1), ("hardwareProblems", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genGroupHWStatus.setStatus('current')
if mibBuilder.loadTexts: genGroupHWStatus.setDescription('This attribute describes the status of the group hardware as detected by the sensors software.')
rndBasePhysicalAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 12), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndBasePhysicalAddress.setStatus('current')
if mibBuilder.loadTexts: rndBasePhysicalAddress.setDescription('The Base physical (MAC) address of the device.')
class RlImageIdType(TextualConvention, Integer32):
    description = 'SW images enumeration'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("image1", 1), ("image2", 2))

rndSoftwareFile = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 13))
rndActiveSoftwareFileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 13, 1), )
if mibBuilder.loadTexts: rndActiveSoftwareFileTable.setStatus('current')
if mibBuilder.loadTexts: rndActiveSoftwareFileTable.setDescription(' The (conceptual) table listing the active software file of the requested unit.')
rndActiveSoftwareFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 13, 1, 1), ).setIndexNames((0, "CISCOSB-DEVICEPARAMS-MIB", "rndUnitNumber"))
if mibBuilder.loadTexts: rndActiveSoftwareFileEntry.setStatus('current')
if mibBuilder.loadTexts: rndActiveSoftwareFileEntry.setDescription(' An entry (conceptual row) in the rndActiveSoftwareFileTable.')
rndUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 13, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndUnitNumber.setStatus('current')
if mibBuilder.loadTexts: rndUnitNumber.setDescription("The unit number (for stackable devices) or 1 for 'stand alone' device.")
rndActiveSoftwareFile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 13, 1, 1, 2), RlImageIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndActiveSoftwareFile.setStatus('current')
if mibBuilder.loadTexts: rndActiveSoftwareFile.setDescription('Indicates the current active software file, image1 or image2.')
rndActiveSoftwareFileAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 13, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("image1", 1), ("image2", 2), ("invalidImage", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndActiveSoftwareFileAfterReset.setStatus('current')
if mibBuilder.loadTexts: rndActiveSoftwareFileAfterReset.setDescription("Indicates the software file that will be active after reset (image1 or image2). If an error occurred in the download process, resulting in the corruption of the single software file, The value 'invalidImage' will be returned. This value can not be set by the user.")
rlResetStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 13, 2), Bits().clone(namedValues=NamedValues(("ok", 0), ("no-stack-integrity", 1), ("downgrade", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlResetStatus.setStatus('current')
if mibBuilder.loadTexts: rlResetStatus.setDescription('A bit mask that specifies system status before reset action is preformed. Reset is prohibited in stackable products if the images selected after reboot are not of the same release version in ALL stack units. Downgrade status specifies that there are some actions to be preformed on the CDB file before reset is preformed. 0x0 - OK 0x1 - noStackIntegrity 0x2 - downgrade')
rndImageSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImageSize.setStatus('current')
if mibBuilder.loadTexts: rndImageSize.setDescription('Max number of sectors currently allocated for image(s).')
rndBackupConfigurationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndBackupConfigurationEnabled.setStatus('current')
if mibBuilder.loadTexts: rndBackupConfigurationEnabled.setDescription('Specifies whether the device supports backup-config parameters in lcli commands.')
rndImageInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16))
rndImageInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1), )
if mibBuilder.loadTexts: rndImageInfoTable.setStatus('current')
if mibBuilder.loadTexts: rndImageInfoTable.setDescription(' The table contains information about images.')
rndImageInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1), ).setIndexNames((0, "CISCOSB-DEVICEPARAMS-MIB", "rndStackUnitNumber"))
if mibBuilder.loadTexts: rndImageInfoEntry.setStatus('current')
if mibBuilder.loadTexts: rndImageInfoEntry.setDescription(' An entry in the rndImageInfoTable.')
rndStackUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndStackUnitNumber.setStatus('current')
if mibBuilder.loadTexts: rndStackUnitNumber.setDescription("The unit number (for stackable devices) or 1 for 'stand alone' device.")
rndImage1Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage1Name.setStatus('current')
if mibBuilder.loadTexts: rndImage1Name.setDescription('Indicates the file name of image-1 in the system.')
rndImage2Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage2Name.setStatus('current')
if mibBuilder.loadTexts: rndImage2Name.setDescription("Indicates the file name of image-2 (if present) in the system.If image-2 is not present show 'no info' text")
rndImage1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage1Version.setStatus('current')
if mibBuilder.loadTexts: rndImage1Version.setDescription('Indicates the version of image-1 in the system.')
rndImage2Version = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage2Version.setStatus('current')
if mibBuilder.loadTexts: rndImage2Version.setDescription("Indicates the version of image-2 (if present) in the system.If image-2 is not present show 'no info' text")
rndImage1Date = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage1Date.setStatus('current')
if mibBuilder.loadTexts: rndImage1Date.setDescription('Indicates the compilation date of image-1 in the system.')
rndImage2Date = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage2Date.setStatus('current')
if mibBuilder.loadTexts: rndImage2Date.setDescription("Indicates the compilation date of image-2 (if present) in the system.If image-2 is not present show 'no info' text")
rndImage1Time = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage1Time.setStatus('current')
if mibBuilder.loadTexts: rndImage1Time.setDescription('Indicates the compilation time of image-1 in the system.')
rndImage2Time = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndImage2Time.setStatus('current')
if mibBuilder.loadTexts: rndImage2Time.setDescription("Indicates the compilation time of image-2 (if present) in the system.If image-2 is not present show 'no info' text")
rndImage1Description = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndImage1Description.setStatus('current')
if mibBuilder.loadTexts: rndImage1Description.setDescription('Indicates the description of image-1 in the system.')
rndImage2Description = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 1, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndImage2Description.setStatus('current')
if mibBuilder.loadTexts: rndImage2Description.setDescription('Indicates the description of image-2 in the system.')
rlComponentsInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 2), )
if mibBuilder.loadTexts: rlComponentsInfoTable.setStatus('current')
if mibBuilder.loadTexts: rlComponentsInfoTable.setDescription('The table contains information about components, their streams and baselines in the device images.')
rlComponentsInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 2, 1), ).setIndexNames((0, "CISCOSB-DEVICEPARAMS-MIB", "rlComponentsInfoStackUnitNumber"), (0, "CISCOSB-DEVICEPARAMS-MIB", "rlComponentsInfoImageId"), (1, "CISCOSB-DEVICEPARAMS-MIB", "rlComponentsInfoComponent"))
if mibBuilder.loadTexts: rlComponentsInfoEntry.setStatus('current')
if mibBuilder.loadTexts: rlComponentsInfoEntry.setDescription('An entry in the rlComponentsInfoTable.')
rlComponentsInfoStackUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlComponentsInfoStackUnitNumber.setStatus('current')
if mibBuilder.loadTexts: rlComponentsInfoStackUnitNumber.setDescription("The unit number (for stackable devices) or 1 for 'stand alone' device.")
rlComponentsInfoImageId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 2, 1, 2), RlImageIdType())
if mibBuilder.loadTexts: rlComponentsInfoImageId.setStatus('current')
if mibBuilder.loadTexts: rlComponentsInfoImageId.setDescription('Indicates the image id in the unit')
rlComponentsInfoComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40)))
if mibBuilder.loadTexts: rlComponentsInfoComponent.setStatus('current')
if mibBuilder.loadTexts: rlComponentsInfoComponent.setDescription('Indicates the SW component name.')
rlComponentsInfoBaseline = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2, 16, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlComponentsInfoBaseline.setStatus('current')
if mibBuilder.loadTexts: rlComponentsInfoBaseline.setDescription('Indicates the version control baseline of the SW component name.')
mibBuilder.exportSymbols("CISCOSB-DEVICEPARAMS-MIB", rndIpHost=rndIpHost, rndCommunityOwner=rndCommunityOwner, rndIpHostManagement=rndIpHostManagement, rndStackUnitNumber=rndStackUnitNumber, PYSNMP_MODULE_ID=rndDeviceParams, rndActiveSoftwareFile=rndActiveSoftwareFile, rndBrgLicense=rndBrgLicense, rlComponentsInfoEntry=rlComponentsInfoEntry, rndCommunityEntry=rndCommunityEntry, rndDeviceParams=rndDeviceParams, rndCommunityTable=rndCommunityTable, rndActiveSoftwareFileEntry=rndActiveSoftwareFileEntry, rndImageInfoEntry=rndImageInfoEntry, rlComponentsInfoComponent=rlComponentsInfoComponent, rndImage1Time=rndImage1Time, rlComponentsInfoBaseline=rlComponentsInfoBaseline, rndBasePhysicalAddress=rndBasePhysicalAddress, rndImage2Version=rndImage2Version, rndImage2Description=rndImage2Description, rndBridgeType=rndBridgeType, rndBaseBootVersion=rndBaseBootVersion, rndImageInfoTable=rndImageInfoTable, rlMridEntry=rlMridEntry, rndManagedTime=rndManagedTime, rlResetStatus=rlResetStatus, rndCommunityMngStationAddr=rndCommunityMngStationAddr, rlManagedMrid=rlManagedMrid, rndIpHostManagementSupported=rndIpHostManagementSupported, rndSoftwareFile=rndSoftwareFile, rndImage1Version=rndImage1Version, rndImage1Description=rndImage1Description, rlComponentsInfoTable=rlComponentsInfoTable, rndManagedDate=rndManagedDate, rndImageSize=rndImageSize, rndCommunityAccess=rndCommunityAccess, rndInactiveArpTimeOut=rndInactiveArpTimeOut, rndImage1Date=rndImage1Date, rndCommunityStatus=rndCommunityStatus, rndImageInfo=rndImageInfo, rndCommunityTrapDestPort=rndCommunityTrapDestPort, rlComponentsInfoStackUnitNumber=rlComponentsInfoStackUnitNumber, rndErrorDesc=rndErrorDesc, rlMridConnection=rlMridConnection, genGroup=genGroup, rndErrorSeverity=rndErrorSeverity, rndBackupConfigurationEnabled=rndBackupConfigurationEnabled, rndImage1Name=rndImage1Name, rndActiveSoftwareFileAfterReset=rndActiveSoftwareFileAfterReset, rndBrgFeatures=rndBrgFeatures, rndImage2Date=rndImage2Date, rndCommunityTrapsEnable=rndCommunityTrapsEnable, genGroupConfigurationSymbol=genGroupConfigurationSymbol, rndActiveSoftwareFileTable=rndActiveSoftwareFileTable, RlImageIdType=RlImageIdType, genGroupHWVersion=genGroupHWVersion, rndIpHostManagementIfIndex=rndIpHostManagementIfIndex, rndImage2Time=rndImage2Time, genGroupHWStatus=genGroupHWStatus, rlComponentsInfoImageId=rlComponentsInfoImageId, rlMridTable=rlMridTable, rndUnitNumber=rndUnitNumber, rndImage2Name=rndImage2Name, rndCommunityPortSecurity=rndCommunityPortSecurity, rndBrgVersion=rndBrgVersion, rndCommunityString=rndCommunityString, rndBridgeAlarm=rndBridgeAlarm)
