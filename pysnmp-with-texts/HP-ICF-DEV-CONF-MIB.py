#
# PySNMP MIB module HP-ICF-DEV-CONF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DEV-CONF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:26:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VidList, = mibBuilder.importSymbols("HP-ICF-TC", "VidList")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Gauge32, ObjectIdentity, Counter32, iso, Integer32, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "Counter32", "iso", "Integer32", "Bits", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue", "MacAddress")
hpicfDevConf = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126))
hpicfDevConf.setRevisions(('2017-05-02 00:00', '2016-11-02 00:00', '2016-06-07 00:00', '2016-02-01 00:00', '2016-01-28 00:00', '2015-12-18 00:00', '2015-12-04 00:00', '2015-09-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfDevConf.setRevisionsDescriptions(('Added new object hpSwitchProfTunneledNodeSupport in table hpSwitchDevProfTable.', 'Deprecated the table hpSwitchDevAssociationTable. Created new table hpSwitchDevIdentAssociationTable to have different device under same hpSwitchDevAssociationType. Added deviceIdentity(8) in HpPartnerDeviceType to support device defined in device-identity. Added new object hpSwitchDevPortDeviceName in table hpSwitchDevPortEntry.', 'Updated HpPartnerDeviceType to support new device-profile type.', 'This MIB module has been modified to incoporate device profile feature enhancement to support jumbo parameter', 'Updated zero bit of hpPartnerDeviceTypeList.', 'Updated hpPartnerDevideTypeList to support QoS Trust feature.', 'Updated hpSwitchProfCosPriority MIB to support QoS Trust feature.', 'Initial version.',))
if mibBuilder.loadTexts: hpicfDevConf.setLastUpdated('201705020000Z')
if mibBuilder.loadTexts: hpicfDevConf.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfDevConf.setContactInfo('Hewlett Packard Enterprise Development LP. 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfDevConf.setDescription('This MIB module contains HP proprietary objects for managing the auto-configuration feature.')
hpSwitchDevNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 0))
hpSwitchDevScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 1))
hpSwitchDevGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 2))
hpSwitchDevConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3))
hpSwitchDevConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4))
class HpPartnerDeviceType(TextualConvention, Integer32):
    description = 'This textual convention is an enum that contains the types of devices supported by the auto-configuration and QoS port trust mode features.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("arubaAccessPoint", 2), ("arubaBridgeRouter", 3), ("hpBridgeRouter", 4), ("ciscoBridgeRouter", 5), ("ciscoPhone", 6), ("scsWanCpe", 7), ("deviceIdentity", 8))

class HpPartnerDeviceTypeList(TextualConvention, Bits):
    description = 'This object is to store the list of HP partner devices'
    status = 'current'
    namedValues = NamedValues(("reserved", 0), ("none", 1), ("arubaAccessPoint", 2), ("arubaBridgeRouter", 3), ("hpBridgeRouter", 4), ("ciscoBridgeRouter", 5), ("ciscoPhone", 6), ("scsWanCpe", 7), ("deviceIdentity", 8))

hpSwitchDevProfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1), )
if mibBuilder.loadTexts: hpSwitchDevProfTable.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevProfTable.setDescription('The device profile configuration table.')
hpSwitchDevProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1), ).setIndexNames((0, "HP-ICF-DEV-CONF-MIB", "hpSwitchProfIndex"))
if mibBuilder.loadTexts: hpSwitchDevProfEntry.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevProfEntry.setDescription('The device profile configuration entry.')
hpSwitchProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpSwitchProfIndex.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfIndex.setDescription('The index value which uniquely identifies a row in the profile table.')
hpSwitchProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfRowStatus.setDescription('The row status of this device profile entry. Allows creation/deletion of the device profile entry. Row cannot be deleted if the device profile is associated with a device.')
hpSwitchProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfName.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfName.setDescription('The name of the device profile. The maximum length supported is 32 characters.')
hpSwitchProfUntaggedVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfUntaggedVlanID.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfUntaggedVlanID.setDescription('The untagged VLAN ID associated with this profile.')
hpSwitchProfTaggedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 5), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfTaggedVlanList.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfTaggedVlanList.setDescription('The set of tagged VLANs associated with this profile.')
hpSwitchProfIngressBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfIngressBandwidth.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfIngressBandwidth.setDescription('The bandwidth percentage of ingress traffic allowed on the port associated with this profile.')
hpSwitchProfEgressBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfEgressBandwidth.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfEgressBandwidth.setDescription('The bandwidth percentage of egress traffic allowed on the port associated with this profile.')
hpSwitchProfCosPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfCosPriority.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfCosPriority.setDescription('The Class of Service (CoS) priority for traffic entering the port associated with this profile.')
hpSwitchProfPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("halfDuplex10Mbits", 1), ("halfDuplex100Mbits", 2), ("fullDuplex10Mbits", 3), ("fullDuplex100Mbits", 4), ("autoNeg", 5), ("fullDuplex1000Mbits", 6), ("auto10Mbits", 7), ("auto100Mbits", 8), ("auto1000Mbits", 9), ("auto10Gbits", 10), ("auto10or100Mbits", 11), ("auto40Gbits", 12), ("auto2500Mbits", 13), ("auto5000Mbits", 14), ("auto2500or5000Mbits", 15), ("auto1000or2500Mbits", 16), ("auto1000or2500or5000Mbits", 17)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfPortSpeed.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfPortSpeed.setDescription('The port speed configuration associated with this profile.')
hpSwitchProfPoeMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfPoeMaxPower.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfPoeMaxPower.setDescription('The maximum power allocation measured in watts (W) for the port associated with this profile. This value must be less than or equal to 33W.')
hpSwitchProfPoePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfPoePriority.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfPoePriority.setDescription('The PoE priority defined for the port associated with this profile.')
hpSwitchProfJumboFrameSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfJumboFrameSupport.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfJumboFrameSupport.setDescription('The jumbo frame support status for the port associated with this profile. Applying a profile with jumbo frame support enabled will also enable jumbo frame support for all other member ports of all VLANs the port is a member of. The default value is disable.')
hpSwitchProfTunneledNodeSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 1, 1, 13), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchProfTunneledNodeSupport.setStatus('current')
if mibBuilder.loadTexts: hpSwitchProfTunneledNodeSupport.setDescription('Configuration parameter to (dis)allow tunneled node configuration on port when device profile is applied.')
hpSwitchDevAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2), )
if mibBuilder.loadTexts: hpSwitchDevAssociationTable.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevAssociationTable.setDescription('The device association configuration table. This table has deprecated because it has only hpSwitchDevAssociationType as index.This index can not differentiate different device under same hpSwitchDevAssociationType.')
hpSwitchDevAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1), ).setIndexNames((0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationType"))
if mibBuilder.loadTexts: hpSwitchDevAssociationEntry.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevAssociationEntry.setDescription('The device association configuration entry.')
hpSwitchDevAssociationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 1), HpPartnerDeviceType())
if mibBuilder.loadTexts: hpSwitchDevAssociationType.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevAssociationType.setDescription('The type of the auto-configurable device.')
hpSwitchDevAssociationProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchDevAssociationProfName.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevAssociationProfName.setDescription('The name of the profile associated with this device.')
hpSwitchDevAssociationProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchDevAssociationProfID.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevAssociationProfID.setDescription('The ID of the profile associated with this device.')
hpSwitchDevAssociationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchDevAssociationStatus.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevAssociationStatus.setDescription('The auto-configuration feature status for this device-type. By default, the status is disabled. If enabled, the profile configuration is applied.')
hpSwitchRogueDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3))
hpSwitchRogueDevStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchRogueDevStatus.setStatus('current')
if mibBuilder.loadTexts: hpSwitchRogueDevStatus.setDescription('The rogue AP Isolation feature status.')
hpSwitchRogueDevAction = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("block", 1), ("log", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchRogueDevAction.setStatus('current')
if mibBuilder.loadTexts: hpSwitchRogueDevAction.setDescription('Action to be performed when a rogue AP device is detected.')
hpSwitchRogueDevMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3), )
if mibBuilder.loadTexts: hpSwitchRogueDevMacTable.setStatus('current')
if mibBuilder.loadTexts: hpSwitchRogueDevMacTable.setDescription('The MAC entry table for any rogue AP device.')
hpSwitchRogueDevMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3, 1), ).setIndexNames((0, "HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevMacAddress"))
if mibBuilder.loadTexts: hpSwitchRogueDevMacEntry.setStatus('current')
if mibBuilder.loadTexts: hpSwitchRogueDevMacEntry.setDescription('The MAC entry for the rogue AP device.')
hpSwitchRogueDevMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpSwitchRogueDevMacAddress.setStatus('current')
if mibBuilder.loadTexts: hpSwitchRogueDevMacAddress.setDescription('The MAC address of rogue AP device.')
hpSwitchNeighborDevMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 3, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchNeighborDevMacAddress.setStatus('current')
if mibBuilder.loadTexts: hpSwitchNeighborDevMacAddress.setDescription('The MAC address of the access point that detected the rogue AP device.')
hpSwitchWhitelistMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4), )
if mibBuilder.loadTexts: hpSwitchWhitelistMacTable.setStatus('current')
if mibBuilder.loadTexts: hpSwitchWhitelistMacTable.setDescription('The rogue AP device whitelist table. MAC addresses added to this table are not considered to be rogue devices.')
hpSwitchWhitelistMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4, 1), ).setIndexNames((0, "HP-ICF-DEV-CONF-MIB", "hpSwitchWhitelistMacAddress"))
if mibBuilder.loadTexts: hpSwitchWhitelistMacEntry.setStatus('current')
if mibBuilder.loadTexts: hpSwitchWhitelistMacEntry.setDescription('The whitelist table entry.')
hpSwitchWhitelistMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpSwitchWhitelistMacAddress.setStatus('current')
if mibBuilder.loadTexts: hpSwitchWhitelistMacAddress.setDescription('The MAC address of whitelisted AP device.')
hpSwitchWhitelistRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchWhitelistRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpSwitchWhitelistRowStatus.setDescription('The row status of rogue AP whitelist table.')
hpSwitchDevPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5), )
if mibBuilder.loadTexts: hpSwitchDevPortTable.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevPortTable.setDescription('The table shows per-port connected devices and any profiles associated with them.')
hpSwitchDevPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1), ).setIndexNames((0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortIndex"))
if mibBuilder.loadTexts: hpSwitchDevPortEntry.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevPortEntry.setDescription('The table entry showing the device connected to this port and any profile associated with it.')
hpSwitchDevPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpSwitchDevPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevPortIndex.setDescription('Index of the interface on this switch.')
hpSwitchDevPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 2), HpPartnerDeviceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchDevPortType.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevPortType.setDescription('The type of partner device connected to this port.')
hpSwitchDevPortProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchDevPortProfName.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevPortProfName.setDescription('The name of the profile associated with the partner device connected to this port.')
hpSwitchDevPortDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchDevPortDeviceName.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevPortDeviceName.setDescription('The name of partner device connected to this port.')
hpSwitchDevIdentAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6), )
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationTable.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationTable.setDescription('The device association configuration table.')
hpSwitchDevIdentAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1), ).setIndexNames((0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationType"), (0, "HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationSubType"))
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationEntry.setDescription('The device association configuration entry for device.')
hpSwitchDevIdentAssociationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 1), HpPartnerDeviceType())
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationType.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationType.setDescription('The type of the auto-configurable device.')
hpSwitchDevIdentAssociationSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationSubType.setReference('hpicfDeviceIdentityTable')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationSubType.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationSubType.setDescription("This mib is use to differentiate device under same hpSwitchDevIdentAssociationType. Combination of hpSwitchDevIdentAssociationType and this OID uniquely identifies a row in the device association table. For device type 'deviceidentity(8)' the value of this mib will be one of index from device-identity table. For device 'arubaAccessPoint(2)', 'arubaBridgeRouter(3)' and scsWanCpe(7) value of this mib will be 1.")
hpSwitchDevIdentAssociationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationRowStatus.setDescription("The row status of this device association entry. Allows creation/deletion of the device association entry. For device type 'deviceidentity(8)' row cannot be create if the device is not found in device-identity table. For device 'arubaAccessPoint(2)', 'arubaBridgeRouter(3)' and scsWanCpe(7) row cannot delete. To create a new entry, send an SNMP SET request with a RowStatus of 'createAndGo'. createAndGo - create a new entry. createAndWait - not valid for this table.")
hpSwitchDevIdentAssociationProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationProfName.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationProfName.setDescription('The name of the profile associated with this device.')
hpSwitchDevIdentAssociationProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationProfID.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationProfID.setDescription('The ID of the profile associated with this device.')
hpSwitchDevIdentAssociationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationStatus.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationStatus.setDescription('The auto-configuration feature status for this device-type. By default, the status is disabled. If enabled, the profile configuration is applied.')
hpSwitchDevIdentAssociationDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 4, 6, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationDeviceType.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationDeviceType.setDescription('Device type ID which will be use by profile manager.')
hpSwitchDevCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1))
hpSwitchDevCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1, 1)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevProfileGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchWhitelistGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevCompliance = hpSwitchDevCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevCompliance.setDescription('The compliance statement for switches that support device auto-configuration.')
hpSwitchDevCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1, 2)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchWhitelistGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevProfileGroupNew"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevCompliance1 = hpSwitchDevCompliance1.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevCompliance1.setDescription('The compliance statement for switches that support device auto-configuration.')
hpSwitchDevCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 1, 3)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchWhitelistGroup"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevProfileGroupNew"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortGroupNew"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevCompliance2 = hpSwitchDevCompliance2.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevCompliance2.setDescription('The compliance statement for switches that support device auto-configuration.')
hpSwitchDevConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2))
hpSwitchDevProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 1)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchProfName"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfRowStatus"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfUntaggedVlanID"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfTaggedVlanList"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfIngressBandwidth"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfEgressBandwidth"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfCosPriority"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPortSpeed"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoeMaxPower"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoePriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevProfileGroup = hpSwitchDevProfileGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevProfileGroup.setDescription('A collection of objects containing device profile information.')
hpSwitchDevAssociationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 2)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationProfName"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationProfID"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevAssociationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevAssociationGroup = hpSwitchDevAssociationGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevAssociationGroup.setDescription('A collection of objects containing information about associated devices.')
hpSwitchRogueDevGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 3)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevStatus"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchRogueDevAction"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchNeighborDevMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchRogueDevGroup = hpSwitchRogueDevGroup.setStatus('current')
if mibBuilder.loadTexts: hpSwitchRogueDevGroup.setDescription('A collection of objects containing rogue device information.')
hpSwitchWhitelistGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 4)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchWhitelistRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchWhitelistGroup = hpSwitchWhitelistGroup.setStatus('current')
if mibBuilder.loadTexts: hpSwitchWhitelistGroup.setDescription('A collection of objects containing information about whitelisted devices.')
hpSwitchDevPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 5)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortType"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortProfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevPortGroup = hpSwitchDevPortGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpSwitchDevPortGroup.setDescription('A collection of objects containing per-port device connections and any profiles associated with them.')
hpSwitchDevProfileGroupNew = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 6)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchProfName"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfRowStatus"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfUntaggedVlanID"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfTaggedVlanList"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfIngressBandwidth"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfEgressBandwidth"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfCosPriority"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPortSpeed"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoeMaxPower"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfPoePriority"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfJumboFrameSupport"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchProfTunneledNodeSupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevProfileGroupNew = hpSwitchDevProfileGroupNew.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevProfileGroupNew.setDescription('A collection of objects containing device profile information.')
hpSwitchDevIdentAssociationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 7)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationRowStatus"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationProfName"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationProfID"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationStatus"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevIdentAssociationDeviceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevIdentAssociationGroup = hpSwitchDevIdentAssociationGroup.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevIdentAssociationGroup.setDescription('A collection of objects containing information about associated devices.')
hpSwitchDevPortGroupNew = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126, 3, 2, 8)).setObjects(("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortType"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortProfName"), ("HP-ICF-DEV-CONF-MIB", "hpSwitchDevPortDeviceName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchDevPortGroupNew = hpSwitchDevPortGroupNew.setStatus('current')
if mibBuilder.loadTexts: hpSwitchDevPortGroupNew.setDescription('A collection of objects containing per-port device connections and any profiles associated with them.')
mibBuilder.exportSymbols("HP-ICF-DEV-CONF-MIB", hpSwitchDevCompliance1=hpSwitchDevCompliance1, hpSwitchProfTaggedVlanList=hpSwitchProfTaggedVlanList, hpSwitchProfEgressBandwidth=hpSwitchProfEgressBandwidth, hpSwitchDevProfTable=hpSwitchDevProfTable, hpSwitchProfJumboFrameSupport=hpSwitchProfJumboFrameSupport, hpSwitchDevIdentAssociationGroup=hpSwitchDevIdentAssociationGroup, hpSwitchDevConformance=hpSwitchDevConformance, hpSwitchRogueDevStatus=hpSwitchRogueDevStatus, hpSwitchDevIdentAssociationEntry=hpSwitchDevIdentAssociationEntry, hpSwitchProfUntaggedVlanID=hpSwitchProfUntaggedVlanID, hpSwitchDevIdentAssociationRowStatus=hpSwitchDevIdentAssociationRowStatus, hpSwitchWhitelistMacTable=hpSwitchWhitelistMacTable, hpSwitchWhitelistRowStatus=hpSwitchWhitelistRowStatus, hpSwitchDevCompliance=hpSwitchDevCompliance, hpSwitchDevPortIndex=hpSwitchDevPortIndex, hpSwitchDevAssociationProfID=hpSwitchDevAssociationProfID, hpSwitchProfIndex=hpSwitchProfIndex, hpSwitchRogueDevMacTable=hpSwitchRogueDevMacTable, hpSwitchDevPortGroupNew=hpSwitchDevPortGroupNew, hpSwitchDevScalar=hpSwitchDevScalar, hpSwitchProfPoePriority=hpSwitchProfPoePriority, hpSwitchDevGlobals=hpSwitchDevGlobals, hpSwitchDevAssociationType=hpSwitchDevAssociationType, hpSwitchRogueDevGroup=hpSwitchRogueDevGroup, hpSwitchProfName=hpSwitchProfName, hpSwitchProfCosPriority=hpSwitchProfCosPriority, hpSwitchDevIdentAssociationDeviceType=hpSwitchDevIdentAssociationDeviceType, hpSwitchDevAssociationStatus=hpSwitchDevAssociationStatus, hpSwitchDevPortTable=hpSwitchDevPortTable, hpSwitchProfPortSpeed=hpSwitchProfPortSpeed, hpSwitchRogueDevMacAddress=hpSwitchRogueDevMacAddress, hpSwitchDevProfileGroup=hpSwitchDevProfileGroup, hpSwitchProfPoeMaxPower=hpSwitchProfPoeMaxPower, hpSwitchDevIdentAssociationType=hpSwitchDevIdentAssociationType, hpSwitchDevIdentAssociationProfID=hpSwitchDevIdentAssociationProfID, hpSwitchWhitelistMacAddress=hpSwitchWhitelistMacAddress, hpSwitchRogueDevAction=hpSwitchRogueDevAction, hpicfDevConf=hpicfDevConf, HpPartnerDeviceTypeList=HpPartnerDeviceTypeList, hpSwitchDevProfileGroupNew=hpSwitchDevProfileGroupNew, hpSwitchDevNotifications=hpSwitchDevNotifications, hpSwitchDevCompliances=hpSwitchDevCompliances, hpSwitchDevProfEntry=hpSwitchDevProfEntry, hpSwitchRogueDevice=hpSwitchRogueDevice, hpSwitchDevPortType=hpSwitchDevPortType, hpSwitchDevIdentAssociationTable=hpSwitchDevIdentAssociationTable, hpSwitchDevAssociationTable=hpSwitchDevAssociationTable, hpSwitchWhitelistMacEntry=hpSwitchWhitelistMacEntry, hpSwitchDevCompliance2=hpSwitchDevCompliance2, hpSwitchDevPortDeviceName=hpSwitchDevPortDeviceName, hpSwitchWhitelistGroup=hpSwitchWhitelistGroup, hpSwitchProfIngressBandwidth=hpSwitchProfIngressBandwidth, hpSwitchDevIdentAssociationProfName=hpSwitchDevIdentAssociationProfName, hpSwitchDevAssociationEntry=hpSwitchDevAssociationEntry, PYSNMP_MODULE_ID=hpicfDevConf, hpSwitchRogueDevMacEntry=hpSwitchRogueDevMacEntry, hpSwitchDevIdentAssociationSubType=hpSwitchDevIdentAssociationSubType, hpSwitchProfTunneledNodeSupport=hpSwitchProfTunneledNodeSupport, hpSwitchDevPortGroup=hpSwitchDevPortGroup, hpSwitchDevAssociationProfName=hpSwitchDevAssociationProfName, HpPartnerDeviceType=HpPartnerDeviceType, hpSwitchDevPortProfName=hpSwitchDevPortProfName, hpSwitchProfRowStatus=hpSwitchProfRowStatus, hpSwitchDevIdentAssociationStatus=hpSwitchDevIdentAssociationStatus, hpSwitchDevAssociationGroup=hpSwitchDevAssociationGroup, hpSwitchDevPortEntry=hpSwitchDevPortEntry, hpSwitchDevConfig=hpSwitchDevConfig, hpSwitchDevConfigGroups=hpSwitchDevConfigGroups, hpSwitchNeighborDevMacAddress=hpSwitchNeighborDevMacAddress)
