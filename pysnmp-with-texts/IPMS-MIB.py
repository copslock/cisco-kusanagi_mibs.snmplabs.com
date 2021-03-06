#
# PySNMP MIB module IPMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPMS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Bits, ObjectIdentity, Counter64, IpAddress, Integer32, MibIdentifier, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "Counter64", "IpAddress", "Integer32", "MibIdentifier", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylanIpmsArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanIpmsArch")
ipmsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 14, 1))
ipmsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1))
class DisplayString(OctetString):
    pass

ipmsGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 1))
ipmsVersion = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsVersion.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsVersion.setDescription('The current version of IPMS.')
ipmsState = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipmsState.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsState.setDescription('The current state of IPMS. When read this flag indicates whether IPMS is enabled or disabled. Setting this flag to enabled causes the IPMS software to be loaded. Setting this flag to disabled causes the IPMS software to be unloaded. If this flag indicates that IPMS is disabled, then no other objects within the IPMS MIB can be accessed (because the IPMS software is not loaded on the switch). In other words, the full IPMS MIB is available only when this flag indicates that IPMS is enabled.')
ipmsDIPAddressPortTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2), )
if mibBuilder.loadTexts: ipmsDIPAddressPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPAddressPortTable.setDescription('This table contains entries that list which switch ports have requested membership in a specific IP Multicast Group. There are several slot/port combinations for each IP Multicast Group.')
ipmsDIPAddressPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1), ).setIndexNames((0, "IPMS-MIB", "ipmsDIPAddress"), (0, "IPMS-MIB", "ipmsDIPDstVlan"), (0, "IPMS-MIB", "ipmsDIPSlotNumber"), (0, "IPMS-MIB", "ipmsDIPPortNumber"), (0, "IPMS-MIB", "ipmsDIPPortInstance"), (0, "IPMS-MIB", "ipmsDIPPortService"))
if mibBuilder.loadTexts: ipmsDIPAddressPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPAddressPortEntry.setDescription('This defines an entry in the Destination IP Address/Port table.')
ipmsDIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPAddress.setDescription('This field defines the Destination IP Multicast address for the fields that follow.')
ipmsDIPDstVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPDstVlan.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPDstVlan.setDescription('This field contains the VlanId of which the port is a member.')
ipmsDIPDstVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPDstVlanMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPDstVlanMask.setDescription('This field contains the Vlan Mask for the afforementioned Vlan.')
ipmsDIPSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPSlotNumber.setDescription('This field contains the slot number of the port that corresponds to the IP Multicast group that it has joined.')
ipmsDIPPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPPortNumber.setDescription('This value contains the port number for this virtual port.')
ipmsDIPPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPPortType.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPPortType.setDescription('This value contains the type of this port.')
ipmsDIPPortInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPPortInstance.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPPortInstance.setDescription('This value contains the instance for this port.')
ipmsDIPPortService = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPPortService.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPPortService.setDescription('This value contains the service for this port.')
ipmsDIPSrcIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPSrcIPAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPSrcIPAddr.setDescription('This value contains the IP address of the station sending the membership report.')
ipmsDIPPortTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsDIPPortTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsDIPPortTimeout.setDescription('This value contains the timeout value in seconds for this port.')
ipmsNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3), )
if mibBuilder.loadTexts: ipmsNeighborTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNeighborTable.setDescription('This table contains entries that list all known external or neighboring routers.')
ipmsNeighborTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1), ).setIndexNames((0, "IPMS-MIB", "ipmsNbrVlanID"), (0, "IPMS-MIB", "ipmsNbrSIPAddress"))
if mibBuilder.loadTexts: ipmsNeighborTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNeighborTableEntry.setDescription('This defines an entry in the Neighbor table.')
ipmsNbrVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrVlanID.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrVlanID.setDescription('This field contains the VlanId of the neighboring router.')
ipmsNbrVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrVlanMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrVlanMask.setDescription('This field contains the Vlan Mask of the neighboring router.')
ipmsNbrSIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrSIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrSIPAddress.setDescription('This field defines the IP address of the neighboring router.')
ipmsNbrSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrSlotNumber.setDescription('This field contains the slot number of the neighboring router.')
ipmsNbrPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrPortNumber.setDescription('This value contains the port number of the neighboring router.')
ipmsNbrPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrPortType.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrPortType.setDescription('This value contains the type of the neighboring router.')
ipmsNbrPortInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrPortInstance.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrPortInstance.setDescription('This value contains the instance of the neighboring router.')
ipmsNbrPortService = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrPortService.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrPortService.setDescription('This value contains the service of the neighboring router.')
ipmsNbrPortTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsNbrPortTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsNbrPortTimeout.setDescription('This value contains the timeout value in seconds of the neighboring router.')
ipmsStatsTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4), )
if mibBuilder.loadTexts: ipmsStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsTable.setDescription('This table contains entries that supply statistical information about the IP Multicast traffic that is being switched and forwarded by this router.')
ipmsStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1), ).setIndexNames((0, "IPMS-MIB", "ipmsStatsDIPAddress"), (0, "IPMS-MIB", "ipmsStatsSIPAddress"), (0, "IPMS-MIB", "ipmsStatsVlanID"))
if mibBuilder.loadTexts: ipmsStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsEntry.setDescription('This table entry describes the entries included in the above tables.')
ipmsStatsDIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsStatsDIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsDIPAddress.setDescription('This field contains the Destinatin IP address of the dest/source entry value. There can be many IP source addresses for a given Destination IP address.')
ipmsStatsSIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsStatsSIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsSIPAddress.setDescription('This field contains the Source IP Address for a given Destination IP address.')
ipmsStatsVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsStatsVlanID.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsVlanID.setDescription('This field contains the VlanID of the entry.')
ipmsStatsVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsStatsVlanMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsVlanMask.setDescription('This field contains the Vlan mask of the entry.')
ipmsStatsPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsStatsPacketsOut.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsPacketsOut.setDescription('This field contains the number of packets that have been sent for a given Destination IP/source IP address pair.')
ipmsStatsSecsSinceZeroed = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsStatsSecsSinceZeroed.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsSecsSinceZeroed.setDescription('This field contains the number seconds that have elapsed since the statistics have been zeroed.')
ipmsStatsAveragePPS = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsStatsAveragePPS.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsStatsAveragePPS.setDescription('This field contains the average number of packets per second for this data flow.')
ipmsZeroStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 5))
ipmsZeroStatsFlag = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("zeroStats", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipmsZeroStatsFlag.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsZeroStatsFlag.setDescription('Seting this flag to one causes statistics counters to be zeroed.')
ipmsForwardingTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6), )
if mibBuilder.loadTexts: ipmsForwardingTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsForwardingTable.setDescription('This table contains entries that represent the contents of IPMS forwarding table. For each source and destination IP address pair, several slot/port combinations can be assigned.')
ipmsFwdTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1), ).setIndexNames((0, "IPMS-MIB", "ipmsFwdDestIP"), (0, "IPMS-MIB", "ipmsFwdSourceIP"), (0, "IPMS-MIB", "ipmsFwdEntryType"), (0, "IPMS-MIB", "ipmsFwdSrcVlan"), (0, "IPMS-MIB", "ipmsFwdDstSlotNumber"), (0, "IPMS-MIB", "ipmsFwdDstPortNumber"), (0, "IPMS-MIB", "ipmsFwdDstPortInstance"), (0, "IPMS-MIB", "ipmsFwdDstPortService"))
if mibBuilder.loadTexts: ipmsFwdTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdTableEntry.setDescription('This defines an entry in the Forwarding table.')
ipmsFwdDestIP = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDestIP.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDestIP.setDescription('This field defines the Dest IP Multicast address for the fields that follow.')
ipmsFwdSourceIP = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSourceIP.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSourceIP.setDescription('This field defines the Source IP Multicast address for the fields that follow.')
ipmsFwdEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("switched", 1), ("switchedError", 2), ("switchedPrimary", 3), ("routed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdEntryType.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdEntryType.setDescription('This field contains the type of this forwarding entry.')
ipmsFwdSrcVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSrcVlan.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSrcVlan.setDescription('This field contains the source VlanID of this stream.')
ipmsFwdSrcVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSrcVlanMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSrcVlanMask.setDescription('This field contains the source VlanID Mask of this stream.')
ipmsFwdSrcSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSrcSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSrcSlotNumber.setDescription('This field contains the slot number of the svpn that is emitting this multicast stream.')
ipmsFwdSrcPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSrcPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSrcPortNumber.setDescription('This field contains the port number of the aforementioned svpn.')
ipmsFwdSrcPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSrcPortType.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSrcPortType.setDescription('This field contains the port type.')
ipmsFwdSrcPortInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSrcPortInstance.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSrcPortInstance.setDescription('This field contains the port instance.')
ipmsFwdSrcPortService = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdSrcPortService.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdSrcPortService.setDescription('This field contains the port service.')
ipmsFwdDstVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstVlan.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstVlan.setDescription('This field contains the destination VlanID of this port.')
ipmsFwdDstVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstVlanMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstVlanMask.setDescription('This field contains the destination VlanID Mask of this port.')
ipmsFwdDstSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstSlotNumber.setDescription('This field contains the slot number of the svpn that has requested the multicast stream.')
ipmsFwdDstPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstPortNumber.setDescription('This field contains the port number of the destination svpn.')
ipmsFwdDstPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstPortType.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstPortType.setDescription('This field contains the port type.')
ipmsFwdDstPortInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstPortInstance.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstPortInstance.setDescription('This field contains the port instance.')
ipmsFwdDstPortService = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstPortService.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstPortService.setDescription('This field contains the port service.')
ipmsFwdDstPortMbrFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("membershipRequested", 1), ("membershipNotRequested", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstPortMbrFlag.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstPortMbrFlag.setDescription('This field contains a flag indicating whether or not this port is in the forwarding table due to the reception of an IGMP membership report.')
ipmsFwdDstPortNbrFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portIsNeighbor", 1), ("portIsNotNeighbor", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstPortNbrFlag.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstPortNbrFlag.setDescription('This field contains a flag indicating whether or not this port is in the forwarding table because their is a neighboring router present on the port.')
ipmsFwdDstPortRteFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portIsRouted", 1), ("portIsNotRouted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsFwdDstPortRteFlag.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsFwdDstPortRteFlag.setDescription('This field contains a flag indicating whether or not this port is in the forwarding table because it is being routed to or not.')
ipmsPolManParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7))
ipmsPolManDefaultPolicy = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permitted", 1), ("denied", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipmsPolManDefaultPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManDefaultPolicy.setDescription('The default policy for IPMS.')
ipmsPolManActiveTimer = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipmsPolManActiveTimer.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManActiveTimer.setDescription("The time in seconds that entries in the IPMS Policy Manager cache table remain active before being flagged as 'stale'.")
ipmsPolManDeleteTimer = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipmsPolManDeleteTimer.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManDeleteTimer.setDescription('The time in seconds that entries in the IPMS Policy Manager cache table remain stale before being deleted from the table.')
ipmsPolManCacheTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8), )
if mibBuilder.loadTexts: ipmsPolManCacheTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManCacheTable.setDescription('This table contains entries that represent the contents of IPMS policy manager cache table.')
ipmsPolManCacheTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1), ).setIndexNames((0, "IPMS-MIB", "ipmsPolManMCGroup"), (0, "IPMS-MIB", "ipmsPolManSlot"), (0, "IPMS-MIB", "ipmsPolManPort"), (0, "IPMS-MIB", "ipmsPolManType"), (0, "IPMS-MIB", "ipmsPolManInstance"), (0, "IPMS-MIB", "ipmsPolManService"))
if mibBuilder.loadTexts: ipmsPolManCacheTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManCacheTableEntry.setDescription('This defines an entry in the Forwarding table.')
ipmsPolManMCGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManMCGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManMCGroup.setDescription('This field defines the Dest IP Multicast address for the fields that follow.')
ipmsPolManSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManSlot.setDescription('This field defines the slot for this entry.')
ipmsPolManPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManPort.setDescription('This field defines the port for this entry.')
ipmsPolManType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManType.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManType.setDescription('This field defines the type for this entry.')
ipmsPolManInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManInstance.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManInstance.setDescription('This field defines the instance for this entry.')
ipmsPolManService = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManService.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManService.setDescription('This field defines the service for this entry.')
ipmsPolManVlanGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManVlanGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManVlanGroup.setDescription('This field defines the vlan group for this entry.')
ipmsPolManStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permitted", 1), ("denied", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManStatus.setDescription('This field defines the status of this entry.')
ipmsPolManState = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("stale", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManState.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManState.setDescription('This field defines the status for this entry. An entry is active if a response has been received from policy manager before the active timer expires. If the active timer expires, the entry will go into a stale state. If stale for longer than the delete timer, the entry will be deleted.')
ipmsPolManTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmsPolManTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipmsPolManTimeout.setDescription('This field defines the timeout value for this entry.')
mibBuilder.exportSymbols("IPMS-MIB", ipmsPolManVlanGroup=ipmsPolManVlanGroup, ipmsStatsDIPAddress=ipmsStatsDIPAddress, ipmsNbrPortService=ipmsNbrPortService, ipmsDIPPortService=ipmsDIPPortService, ipmsPolManType=ipmsPolManType, ipmsFwdDstPortInstance=ipmsFwdDstPortInstance, ipmsDIPSrcIPAddr=ipmsDIPSrcIPAddr, ipmsFwdSrcPortNumber=ipmsFwdSrcPortNumber, ipmsNbrPortNumber=ipmsNbrPortNumber, ipmsDIPAddressPortEntry=ipmsDIPAddressPortEntry, ipmsFwdDstPortNbrFlag=ipmsFwdDstPortNbrFlag, ipmsFwdSourceIP=ipmsFwdSourceIP, ipmsDIPPortType=ipmsDIPPortType, ipmsDIPPortInstance=ipmsDIPPortInstance, ipmsFwdSrcPortInstance=ipmsFwdSrcPortInstance, ipmsNbrSIPAddress=ipmsNbrSIPAddress, ipmsPolManCacheTable=ipmsPolManCacheTable, ipmsDIPDstVlanMask=ipmsDIPDstVlanMask, ipmsFwdSrcPortService=ipmsFwdSrcPortService, ipmsFwdSrcVlan=ipmsFwdSrcVlan, ipmsPolManParameters=ipmsPolManParameters, ipmsState=ipmsState, ipmsFwdSrcVlanMask=ipmsFwdSrcVlanMask, ipmsDIPDstVlan=ipmsDIPDstVlan, ipmsStatsAveragePPS=ipmsStatsAveragePPS, ipmsFwdDstVlanMask=ipmsFwdDstVlanMask, ipmsPolManService=ipmsPolManService, ipmsFwdDstPortService=ipmsFwdDstPortService, ipmsPolManTimeout=ipmsPolManTimeout, ipmsFwdTableEntry=ipmsFwdTableEntry, ipmsStatsEntry=ipmsStatsEntry, ipmsPolManInstance=ipmsPolManInstance, ipmsNbrPortInstance=ipmsNbrPortInstance, ipmsPolManSlot=ipmsPolManSlot, ipmsStatsSIPAddress=ipmsStatsSIPAddress, ipmsFwdDstPortRteFlag=ipmsFwdDstPortRteFlag, ipmsFwdDstSlotNumber=ipmsFwdDstSlotNumber, ipmsFwdEntryType=ipmsFwdEntryType, ipmsFwdDstPortMbrFlag=ipmsFwdDstPortMbrFlag, ipmsFwdSrcSlotNumber=ipmsFwdSrcSlotNumber, ipmsNbrPortTimeout=ipmsNbrPortTimeout, ipmsFwdDstVlan=ipmsFwdDstVlan, ipmsZeroStatsGroup=ipmsZeroStatsGroup, ipmsPolManMCGroup=ipmsPolManMCGroup, ipmsMIBObjects=ipmsMIBObjects, ipmsNeighborTable=ipmsNeighborTable, ipmsPolManStatus=ipmsPolManStatus, ipmsPolManDeleteTimer=ipmsPolManDeleteTimer, ipmsDIPAddress=ipmsDIPAddress, ipmsDIPAddressPortTable=ipmsDIPAddressPortTable, ipmsPolManCacheTableEntry=ipmsPolManCacheTableEntry, ipmsPolManPort=ipmsPolManPort, ipmsForwardingTable=ipmsForwardingTable, ipmsStatsSecsSinceZeroed=ipmsStatsSecsSinceZeroed, ipmsDIPSlotNumber=ipmsDIPSlotNumber, ipmsNbrVlanID=ipmsNbrVlanID, ipmsPolManState=ipmsPolManState, ipmsFwdDstPortNumber=ipmsFwdDstPortNumber, ipmsDIPPortTimeout=ipmsDIPPortTimeout, ipmsNbrPortType=ipmsNbrPortType, ipmsStatsVlanID=ipmsStatsVlanID, ipmsDIPPortNumber=ipmsDIPPortNumber, DisplayString=DisplayString, ipmsFwdDstPortType=ipmsFwdDstPortType, ipmsNeighborTableEntry=ipmsNeighborTableEntry, ipmsStatsTable=ipmsStatsTable, ipmsVersion=ipmsVersion, ipmsGeneralGroup=ipmsGeneralGroup, ipmsStatsPacketsOut=ipmsStatsPacketsOut, ipmsNbrSlotNumber=ipmsNbrSlotNumber, ipmsMIB=ipmsMIB, ipmsPolManActiveTimer=ipmsPolManActiveTimer, ipmsFwdDestIP=ipmsFwdDestIP, ipmsNbrVlanMask=ipmsNbrVlanMask, ipmsFwdSrcPortType=ipmsFwdSrcPortType, ipmsZeroStatsFlag=ipmsZeroStatsFlag, ipmsStatsVlanMask=ipmsStatsVlanMask, ipmsPolManDefaultPolicy=ipmsPolManDefaultPolicy)
