#
# PySNMP MIB module HPN-ICF-EVB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-EVB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
IEEE8021BridgePortNumber, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, MibIdentifier, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, iso, TimeTicks, ObjectIdentity, ModuleIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "iso", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Bits", "Integer32")
TextualConvention, TruthValue, DisplayString, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus", "MacAddress")
hpnicfEvb = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134))
hpnicfEvb.setRevisions(('2012-12-21 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfEvb.setRevisionsDescriptions(('Created by Guo Xiangbin.',))
if mibBuilder.loadTexts: hpnicfEvb.setLastUpdated('201212211200Z')
if mibBuilder.loadTexts: hpnicfEvb.setOrganization('')
if mibBuilder.loadTexts: hpnicfEvb.setContactInfo('')
if mibBuilder.loadTexts: hpnicfEvb.setDescription('EVB management information base for managing devices that support Ethernet Virtual Bridging. This MIB is an extension of IEEE8021-EVB-MIB.')
hpnicfEvbSysObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1))
hpnicfEvbPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2))
hpnicfFlex10Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3))
hpnicfEvbSetResult = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("processing", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEvbSetResult.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbSetResult.setDescription('If a set operation on EVB-MIB-tables returns success, this object indicates the actual result of this operation. Otherwise, it is meaningless. unknown: The set operation on the node has been completed, but the result could only be got from the table which the set operation happended. processing: The set operation is in process. Another set operation cannot be performed at this time. success: The set operation has succeeded. failed: The set operation has failed.')
hpnicfEvbDefaultManagerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2), )
if mibBuilder.loadTexts: hpnicfEvbDefaultManagerTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbDefaultManagerTable.setDescription('A table that contains configuration information for the default Virtual Station Interface (VSI) manager.')
hpnicfEvbDefaultManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbManagerIndex"))
if mibBuilder.loadTexts: hpnicfEvbDefaultManagerEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbDefaultManagerEntry.setDescription('A list of objects containing information for the default VSI manager.')
hpnicfEvbManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbManagerIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbManagerIndex.setDescription('Index of the default manager table.')
hpnicfEvbManagerType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ("name", 3), ("local", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerType.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbManagerType.setDescription('Type of the default VSI manager. ipv4: Specifies the IPv4 address of the default VSI manager. ipv6: Specifies the IPv6 address of the default VSI manager. name: Specifies the name of the default VSI manager, a case-insensitive string of 1 to 127 characters. local: Specifies the device as the default VSI manager.')
hpnicfEvbManagerID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerID.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbManagerID.setDescription("Default VSI manager. The value is zero-length string when the VSI manager type is 'local'.")
hpnicfEvbManagerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(8080)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbManagerPort.setDescription("Port number of the default VSI manager. Optional when the VSI manager type is not 'local'. If the VSI manager type is 'local', it returns zero.")
hpnicfEvbManagerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbManagerRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbManagerRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hpnicfEvbPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1), )
if mibBuilder.loadTexts: hpnicfEvbPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbPortConfigTable.setDescription('A table that contains configuration information for the EVB bridge port.')
hpnicfEvbPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbPortNumber"))
if mibBuilder.loadTexts: hpnicfEvbPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbPortConfigEntry.setDescription('A list of objects containing information for the EVB bridge port.')
hpnicfEvbPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hpnicfEvbPortNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbPortNumber.setDescription('Port number.')
hpnicfEvbRWD = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 31)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbRWD.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbRWD.setDescription('VDP resource wait delay exponent.')
hpnicfEvbRKA = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(14, 31)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbRKA.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbRKA.setDescription('VDP keepalive exponent.')
hpnicfEvbSchannelConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2), )
if mibBuilder.loadTexts: hpnicfEvbSchannelConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbSchannelConfigTable.setDescription('A table that contains configuration information for the S-channel.')
hpnicfEvbSchannelConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbPortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"))
if mibBuilder.loadTexts: hpnicfEvbSchannelConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbSchannelConfigEntry.setDescription('A list of objects containing information for the S-channel.')
hpnicfEvbSchannelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbSchannelID.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbSchannelID.setDescription('S-channel ID.')
hpnicfEvbSchannelSVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbSchannelSVLAN.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbSchannelSVLAN.setDescription('S-VLAN ID. 0 means that the S-channel is not bound to any S-VLAN. 1 represents the SVID for the default S-channel S-channel 1.')
hpnicfEvbMacLearningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbMacLearningStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbMacLearningStatus.setDescription('The MAC address learning function is enabled or not.')
hpnicfEvbRRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbRRStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbRRStatus.setDescription('The RR mode for the S-channel is enabled or not.')
hpnicfEvbSchannelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbSchannelRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbSchannelRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hpnicfEvbVSIConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3), )
if mibBuilder.loadTexts: hpnicfEvbVSIConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIConfigTable.setDescription('A table that contains configuration information for the VSI.')
hpnicfEvbVSIConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbSBPPortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSILocalID"))
if mibBuilder.loadTexts: hpnicfEvbVSIConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIConfigEntry.setDescription('A list of objects containing information for the VSI.')
hpnicfEvbSBPPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hpnicfEvbSBPPortNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbSBPPortNumber.setDescription('The Station-facing Bridge Port (SBP) port number.')
hpnicfEvbVSILocalID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbVSILocalID.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSILocalID.setDescription('VSI local ID.')
hpnicfEvbVSICommand = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("preAssociate", 1), ("preAssociateWithRsrcReservation", 2), ("associate", 3), ("deAssociate", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbVSICommand.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSICommand.setDescription('This object indicates the association or pre-associate property of the VSI.')
hpnicfEvbVSIIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEvbVSIIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIIfIndex.setDescription('VSI interface index.')
hpnicfEvbVSIIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfEvbVSIIsActive.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIIsActive.setDescription('The VSI is activated or not. Activate a VSI after configuring a VSI filter, and deactivate a VSI before removing a VSI filter.')
hpnicfEvbVSIRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbVSIRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hpnicfEvbVSIFilterConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4), )
if mibBuilder.loadTexts: hpnicfEvbVSIFilterConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIFilterConfigTable.setDescription('A table that contains configuration information for filters of the VSI.')
hpnicfEvbVSIFilterConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfEvbSBPPortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSILocalID"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbGroupID"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSIMac"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSIVlanId"))
if mibBuilder.loadTexts: hpnicfEvbVSIFilterConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIFilterConfigEntry.setDescription('A list of objects containing information for filters of the VSI.')
hpnicfEvbGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfEvbGroupID.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbGroupID.setDescription('Group ID.')
hpnicfEvbVSIMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: hpnicfEvbVSIMac.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIMac.setDescription('The MAC address part of the MAC/VLANs for a VSI.')
hpnicfEvbVSIVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 3), VlanIndex())
if mibBuilder.loadTexts: hpnicfEvbVSIVlanId.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIVlanId.setDescription('The VLAN ID part of the MAC/VLANs for a VSI.')
hpnicfEvbVSIFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEvbVSIFilterRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEvbVSIFilterRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hpnicfFlex10PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1), )
if mibBuilder.loadTexts: hpnicfFlex10PortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10PortConfigTable.setDescription('A table that contains configuration information for the flex10 bridge port.')
hpnicfFlex10PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"))
if mibBuilder.loadTexts: hpnicfFlex10PortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10PortConfigEntry.setDescription('A list of objects containing information for the flex10 bridge port.')
hpnicfFlex10PortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hpnicfFlex10PortNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10PortNumber.setDescription('Port number.')
hpnicfFlex10PortEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFlex10PortEnableStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10PortEnableStatus.setDescription('The flex10 function is enabled or not.')
hpnicfFlex10RemoteSchannelTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2), )
if mibBuilder.loadTexts: hpnicfFlex10RemoteSchannelTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemoteSchannelTable.setDescription('A table that contains remote S-channel details.')
hpnicfFlex10RemoteSchannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"))
if mibBuilder.loadTexts: hpnicfFlex10RemoteSchannelEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemoteSchannelEntry.setDescription('A list of objects describing remote S-channels.')
hpnicfFlex10RemSchDesFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 1), Bits().clone(namedValues=NamedValues(("format0", 0), ("format1", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchDesFormat.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemSchDesFormat.setDescription('Description format of the remote S-channel.')
hpnicfFlex10RemSchTerminationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchTerminationType.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemSchTerminationType.setDescription('Termination type of the remote S-channel. 0: PCI Physical Function (Primary). 1: SRIOV Virtual Function. 2: PCI Physical Function (Secondary). 3: Virtual Switch Port. 4: NCSI Port. 2147483647: This value means a Description TLV with format 0 has not been received. other: Unknown termination type.')
hpnicfFlex10RemSchTerminationCap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 3), Bits().clone(namedValues=NamedValues(("ethernet", 0), ("fCOE", 1), ("iSCSI", 2), ("roCEE", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchTerminationCap.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemSchTerminationCap.setDescription('Termination capabilities of the remote S-channel. If a Description TLV with format 0 has not been received, it returns all zeros.')
hpnicfFlex10RemSchTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 4), Bits().clone(namedValues=NamedValues(("class0", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6), ("class7", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchTrafficClass.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemSchTrafficClass.setDescription('Traffic classes of the remote S-channel. If a Description TLV with format 0 has not been received, it returns all zeros.')
hpnicfFlex10RemSchCir = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 5), Integer32()).setUnits('mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchCir.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemSchCir.setDescription('Committed Information Rate (CIR) of the remote S-channel. If a Description TLV with format 0 has not been received, it returns 0.')
hpnicfFlex10RemSchPir = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 6), Integer32()).setUnits('mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchPir.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemSchPir.setDescription('Peak Information Rate (PIR) of the remote S-channel. If a Description TLV with format 0 has not been received, it returns 0.')
hpnicfFlex10RemSchConnectionID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10RemSchConnectionID.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10RemSchConnectionID.setDescription('Connection instance ID of the remote S-channel. The value is a zero-length string if a Description TLV with format 1 has not been received. Otherwise it returns a string with length 16.')
hpnicfFlex10SchannelLinkCtlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3), )
if mibBuilder.loadTexts: hpnicfFlex10SchannelLinkCtlTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10SchannelLinkCtlTable.setDescription('A table that contains link status information for the S-channel.')
hpnicfFlex10SchannelLinkCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1), ).setIndexNames((0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"), (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"))
if mibBuilder.loadTexts: hpnicfFlex10SchannelLinkCtlEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10SchannelLinkCtlEntry.setDescription('A list of objects containing information for the S-channel.')
hpnicfFlex10SchannelSVID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 1), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10SchannelSVID.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10SchannelSVID.setDescription('S-VLAN ID for the S-channel.')
hpnicfFlex10SchannelLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10SchannelLocalStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10SchannelLocalStatus.setDescription('Link status of the local S-channel.')
hpnicfFlex10SchannelRemoteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFlex10SchannelRemoteStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfFlex10SchannelRemoteStatus.setDescription('Link status of the remote S-channel.')
mibBuilder.exportSymbols("HPN-ICF-EVB-MIB", hpnicfEvbRRStatus=hpnicfEvbRRStatus, hpnicfEvbSchannelID=hpnicfEvbSchannelID, hpnicfEvbPortConfigTable=hpnicfEvbPortConfigTable, hpnicfEvbGroupID=hpnicfEvbGroupID, hpnicfEvbVSIVlanId=hpnicfEvbVSIVlanId, PYSNMP_MODULE_ID=hpnicfEvb, hpnicfEvb=hpnicfEvb, hpnicfEvbMacLearningStatus=hpnicfEvbMacLearningStatus, hpnicfEvbVSILocalID=hpnicfEvbVSILocalID, hpnicfEvbVSICommand=hpnicfEvbVSICommand, hpnicfFlex10RemSchPir=hpnicfFlex10RemSchPir, hpnicfEvbManagerRowStatus=hpnicfEvbManagerRowStatus, hpnicfFlex10PortEnableStatus=hpnicfFlex10PortEnableStatus, hpnicfEvbSBPPortNumber=hpnicfEvbSBPPortNumber, hpnicfFlex10SchannelSVID=hpnicfFlex10SchannelSVID, hpnicfFlex10RemoteSchannelEntry=hpnicfFlex10RemoteSchannelEntry, hpnicfFlex10Objects=hpnicfFlex10Objects, hpnicfEvbVSIConfigEntry=hpnicfEvbVSIConfigEntry, hpnicfFlex10RemoteSchannelTable=hpnicfFlex10RemoteSchannelTable, hpnicfFlex10RemSchDesFormat=hpnicfFlex10RemSchDesFormat, hpnicfFlex10PortConfigTable=hpnicfFlex10PortConfigTable, hpnicfEvbSysObjects=hpnicfEvbSysObjects, hpnicfEvbPortNumber=hpnicfEvbPortNumber, hpnicfEvbRWD=hpnicfEvbRWD, hpnicfFlex10SchannelLocalStatus=hpnicfFlex10SchannelLocalStatus, hpnicfEvbVSIConfigTable=hpnicfEvbVSIConfigTable, hpnicfEvbPortObjects=hpnicfEvbPortObjects, hpnicfEvbSchannelSVLAN=hpnicfEvbSchannelSVLAN, hpnicfEvbRKA=hpnicfEvbRKA, hpnicfEvbVSIMac=hpnicfEvbVSIMac, hpnicfFlex10SchannelLinkCtlEntry=hpnicfFlex10SchannelLinkCtlEntry, hpnicfFlex10PortNumber=hpnicfFlex10PortNumber, hpnicfEvbSchannelConfigTable=hpnicfEvbSchannelConfigTable, hpnicfEvbDefaultManagerEntry=hpnicfEvbDefaultManagerEntry, hpnicfEvbManagerID=hpnicfEvbManagerID, hpnicfEvbVSIIfIndex=hpnicfEvbVSIIfIndex, hpnicfEvbVSIFilterRowStatus=hpnicfEvbVSIFilterRowStatus, hpnicfFlex10RemSchTerminationType=hpnicfFlex10RemSchTerminationType, hpnicfEvbVSIIsActive=hpnicfEvbVSIIsActive, hpnicfFlex10RemSchCir=hpnicfFlex10RemSchCir, hpnicfFlex10RemSchConnectionID=hpnicfFlex10RemSchConnectionID, hpnicfFlex10SchannelLinkCtlTable=hpnicfFlex10SchannelLinkCtlTable, hpnicfEvbManagerIndex=hpnicfEvbManagerIndex, hpnicfEvbManagerPort=hpnicfEvbManagerPort, hpnicfFlex10RemSchTrafficClass=hpnicfFlex10RemSchTrafficClass, hpnicfFlex10SchannelRemoteStatus=hpnicfFlex10SchannelRemoteStatus, hpnicfEvbSetResult=hpnicfEvbSetResult, hpnicfEvbDefaultManagerTable=hpnicfEvbDefaultManagerTable, hpnicfEvbPortConfigEntry=hpnicfEvbPortConfigEntry, hpnicfEvbVSIRowStatus=hpnicfEvbVSIRowStatus, hpnicfEvbSchannelConfigEntry=hpnicfEvbSchannelConfigEntry, hpnicfFlex10RemSchTerminationCap=hpnicfFlex10RemSchTerminationCap, hpnicfEvbVSIFilterConfigEntry=hpnicfEvbVSIFilterConfigEntry, hpnicfEvbVSIFilterConfigTable=hpnicfEvbVSIFilterConfigTable, hpnicfEvbManagerType=hpnicfEvbManagerType, hpnicfEvbSchannelRowStatus=hpnicfEvbSchannelRowStatus, hpnicfFlex10PortConfigEntry=hpnicfFlex10PortConfigEntry)
