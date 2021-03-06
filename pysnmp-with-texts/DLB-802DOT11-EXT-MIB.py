#
# PySNMP MIB module DLB-802DOT11-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLB-802DOT11-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:47:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
dlbMgmt, = mibBuilder.importSymbols("DELIBERANT-MIB", "dlbMgmt")
ifPhysAddress, InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifPhysAddress", "InterfaceIndex", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
NotificationType, Bits, ModuleIdentity, Counter64, MibIdentifier, IpAddress, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "Counter64", "MibIdentifier", "IpAddress", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "iso", "Gauge32")
DisplayString, TruthValue, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "MacAddress")
dlb802dot11ExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761, 3, 5))
dlb802dot11ExtMIB.setRevisions(('2010-03-31 00:00', '2009-05-15 00:00', '2008-12-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlb802dot11ExtMIB.setRevisionsDescriptions(('Added dlbDot11IfAssocNodeCount.', 'Added dlbDot11RemoteNodeStatsTable and dlbRemoteNodeConnected, dlbRemoteNodeDisconnected notifications.', 'First revision.',))
if mibBuilder.loadTexts: dlb802dot11ExtMIB.setLastUpdated('201003310000Z')
if mibBuilder.loadTexts: dlb802dot11ExtMIB.setOrganization('Deliberant')
if mibBuilder.loadTexts: dlb802dot11ExtMIB.setContactInfo(' Deliberant Customer Support E-mail: support@deliberant.com')
if mibBuilder.loadTexts: dlb802dot11ExtMIB.setDescription('The Deliberant 802.11 Extension MIB.')
dlb802dot11ExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1))
dlbDot11Notifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0))
dlbDot11Info = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 1))
dlbDot11Conf = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2))
dlbDot11Stats = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3))
dlbDot11IfConfTable = MibTable((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1), )
if mibBuilder.loadTexts: dlbDot11IfConfTable.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfConfTable.setDescription('Wireless interface configuration table.')
dlbDot11IfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dlbDot11IfConfEntry.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfConfEntry.setDescription('Wireless interface configuration table entry.')
dlbDot11IfParentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfParentIndex.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfParentIndex.setDescription("Wireless interface's parent index, which corresponds to ifIndex in MIB-II interfaces table. This is only applicable if the interface is virtual and it is created under some other interface, like it is for Atheros cards when using MadWiFi driver, where parent interfaces are wifi0, wifi1, etc.")
dlbDot11IfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfProtocol.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfProtocol.setDescription("Protocol string, for example 'IEEE 802.11g'.")
dlbDot11IfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("adhoc", 1), ("managed", 2), ("master", 3), ("repeater", 4), ("secondary", 5), ("monitor", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfMode.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfMode.setDescription('Wireless interface operation mode')
dlbDot11IfESSID = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfESSID.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfESSID.setDescription('ESSID')
dlbDot11IfAccessPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfAccessPoint.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfAccessPoint.setDescription("Access point's MAC address if working in managed mode and connected. Current interface's MAC address, when working in master mode.")
dlbDot11IfCountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfCountryCode.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfCountryCode.setDescription('Country code.')
dlbDot11IfFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 7), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfFrequency.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfFrequency.setDescription('Current frequency as reported by driver.')
dlbDot11IfChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfChannel.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfChannel.setDescription('Channel number.')
dlbDot11IfChannelBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 9), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfChannelBandwidth.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfChannelBandwidth.setDescription('Channel bandwidth.')
dlbDot11IfTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 10), Gauge32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfTxPower.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfTxPower.setDescription('Transmit power in dBm.')
dlbDot11IfBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 11), Gauge32()).setUnits('kbit/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfBitRate.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfBitRate.setDescription('Transmission bitrate.')
dlbDot11IfLinkQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfLinkQuality.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfLinkQuality.setDescription('Link quality value.')
dlbDot11IfMaxLinkQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfMaxLinkQuality.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfMaxLinkQuality.setDescription('Maximum possible link quality value for current wireless card.')
dlbDot11IfSignalLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 14), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfSignalLevel.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfSignalLevel.setDescription('Signal level.')
dlbDot11IfNoiseLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 15), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfNoiseLevel.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfNoiseLevel.setDescription('Noise level.')
dlbDot11IfAssocNodeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfAssocNodeCount.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfAssocNodeCount.setDescription('Number of associated nodes when working in access point mode. 1 - if associated to remote access point in client mode.')
dlbDot11IfErrStatsTable = MibTable((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1), )
if mibBuilder.loadTexts: dlbDot11IfErrStatsTable.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfErrStatsTable.setDescription('Wireless interface statistics table.')
dlbDot11IfErrStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dlbDot11IfErrStatsEntry.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfErrStatsEntry.setDescription('Wireless interface statistics table entry.')
dlbDot11IfRxInvalidNWID = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfRxInvalidNWID.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfRxInvalidNWID.setDescription('Number of received packets with invalid NWID/ESSID. Increasing value usually means that there are other stations transmitting on the same channel or adjacent channels.')
dlbDot11IfRxInvalidCrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfRxInvalidCrypt.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfRxInvalidCrypt.setDescription('Number of received packets the hardware was unable to decrypt.')
dlbDot11IfRxInvalidFrag = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfRxInvalidFrag.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfRxInvalidFrag.setDescription('Number of received packets that were missing link layer fragments for complete re-assembly.')
dlbDot11IfTxExcessiveRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfTxExcessiveRetries.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfTxExcessiveRetries.setDescription('Number of packets hardware failed to deliver.')
dlbDot11IfInvalidMisc = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfInvalidMisc.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfInvalidMisc.setDescription('Other packets lost in relation with specific wireless operations.')
dlbDot11IfMissedBeacons = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11IfMissedBeacons.setStatus('current')
if mibBuilder.loadTexts: dlbDot11IfMissedBeacons.setDescription('Number of beacons that should have been sent by remote access point but were not received. Increasing number usually means that communicating peers moved out of range.')
dlbDot11RemoteNodeStatsTable = MibTable((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2), )
if mibBuilder.loadTexts: dlbDot11RemoteNodeStatsTable.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RemoteNodeStatsTable.setDescription('Remote node statistics table. This table shows statistics for associated or already disconnected clients on wireless interfaces which are operating in access point mode. For interfaces operating in client mode and associated to remote access point information about access point is shown.')
dlbDot11RemoteNodeStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DLB-802DOT11-EXT-MIB", "dlbDot11RmtNodeMacAddress"))
if mibBuilder.loadTexts: dlbDot11RemoteNodeStatsEntry.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RemoteNodeStatsEntry.setDescription('Wireless remote node statistics table entry.')
dlbDot11RmtNodeMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11RmtNodeMacAddress.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RmtNodeMacAddress.setDescription('Remote node MAC address.')
dlbDot11RmtNodeAssociated = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11RmtNodeAssociated.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RmtNodeAssociated.setDescription('Remote node is currently associated.')
dlbDot11RmtNodeTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 3), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11RmtNodeTxBytes.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RmtNodeTxBytes.setDescription('Bytes transmitted to remote node. This object is optional.')
dlbDot11RmtNodeRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11RmtNodeRxBytes.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RmtNodeRxBytes.setDescription('Bytes received from remote node. This object is optional.')
dlbDot11RmtNodeAssocTime = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11RmtNodeAssocTime.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RmtNodeAssocTime.setDescription('UNIX timestamp of the association. This object is optional.')
dlbDot11RmtNodeDisassocTime = MibTableColumn((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlbDot11RmtNodeDisassocTime.setStatus('current')
if mibBuilder.loadTexts: dlbDot11RmtNodeDisassocTime.setDescription('UNIX timestamp of the disassociation (if remote node recently dissasociated). This object is optional.')
dlbFrequencyChange = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("DLB-802DOT11-EXT-MIB", "dlbDot11IfFrequency"))
if mibBuilder.loadTexts: dlbFrequencyChange.setStatus('current')
if mibBuilder.loadTexts: dlbFrequencyChange.setDescription('This notification is sent on frequency change.')
dlbNoiseThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("DLB-802DOT11-EXT-MIB", "dlbDot11IfNoiseLevel"))
if mibBuilder.loadTexts: dlbNoiseThresholdReached.setStatus('current')
if mibBuilder.loadTexts: dlbNoiseThresholdReached.setDescription('This notification is sent when noise becomes bigger than threshold.')
dlbRemoteNodeConnected = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 3)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifPhysAddress"), ("IF-MIB", "ifIndex"), ("DLB-802DOT11-EXT-MIB", "dlbDot11RmtNodeMacAddress"))
if mibBuilder.loadTexts: dlbRemoteNodeConnected.setStatus('current')
if mibBuilder.loadTexts: dlbRemoteNodeConnected.setDescription('This notification is sent when remote node associates.')
dlbRemoteNodeDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 4)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifPhysAddress"), ("IF-MIB", "ifIndex"), ("DLB-802DOT11-EXT-MIB", "dlbDot11RmtNodeMacAddress"))
if mibBuilder.loadTexts: dlbRemoteNodeDisconnected.setStatus('current')
if mibBuilder.loadTexts: dlbRemoteNodeDisconnected.setDescription('This notification is sent when remote node dissasociates.')
dlbLinkQualThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 5)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("DLB-802DOT11-EXT-MIB", "dlbDot11IfLinkQuality"))
if mibBuilder.loadTexts: dlbLinkQualThresholdReached.setStatus('current')
if mibBuilder.loadTexts: dlbLinkQualThresholdReached.setDescription('This notification is sent when link quality crosses the specified threshold.')
mibBuilder.exportSymbols("DLB-802DOT11-EXT-MIB", dlbDot11IfProtocol=dlbDot11IfProtocol, dlbDot11IfInvalidMisc=dlbDot11IfInvalidMisc, dlb802dot11ExtMIB=dlb802dot11ExtMIB, dlbDot11RemoteNodeStatsTable=dlbDot11RemoteNodeStatsTable, dlbDot11RemoteNodeStatsEntry=dlbDot11RemoteNodeStatsEntry, dlbDot11Stats=dlbDot11Stats, dlbRemoteNodeDisconnected=dlbRemoteNodeDisconnected, dlbDot11IfLinkQuality=dlbDot11IfLinkQuality, dlbDot11IfChannelBandwidth=dlbDot11IfChannelBandwidth, dlbDot11IfMissedBeacons=dlbDot11IfMissedBeacons, dlbDot11RmtNodeTxBytes=dlbDot11RmtNodeTxBytes, dlbDot11IfFrequency=dlbDot11IfFrequency, dlbDot11IfESSID=dlbDot11IfESSID, dlbDot11IfChannel=dlbDot11IfChannel, dlbDot11Info=dlbDot11Info, dlbLinkQualThresholdReached=dlbLinkQualThresholdReached, dlbDot11IfMode=dlbDot11IfMode, dlbDot11RmtNodeRxBytes=dlbDot11RmtNodeRxBytes, dlbDot11IfTxExcessiveRetries=dlbDot11IfTxExcessiveRetries, dlbDot11IfSignalLevel=dlbDot11IfSignalLevel, dlbRemoteNodeConnected=dlbRemoteNodeConnected, dlbDot11Conf=dlbDot11Conf, dlbDot11IfTxPower=dlbDot11IfTxPower, dlbDot11IfErrStatsEntry=dlbDot11IfErrStatsEntry, dlbNoiseThresholdReached=dlbNoiseThresholdReached, dlbDot11IfNoiseLevel=dlbDot11IfNoiseLevel, dlbDot11IfBitRate=dlbDot11IfBitRate, dlbDot11IfRxInvalidNWID=dlbDot11IfRxInvalidNWID, dlbDot11RmtNodeAssocTime=dlbDot11RmtNodeAssocTime, dlbDot11IfConfTable=dlbDot11IfConfTable, dlbDot11Notifs=dlbDot11Notifs, dlbDot11IfAccessPoint=dlbDot11IfAccessPoint, dlbDot11IfParentIndex=dlbDot11IfParentIndex, dlbFrequencyChange=dlbFrequencyChange, dlbDot11IfConfEntry=dlbDot11IfConfEntry, dlbDot11IfErrStatsTable=dlbDot11IfErrStatsTable, dlbDot11IfRxInvalidCrypt=dlbDot11IfRxInvalidCrypt, dlbDot11IfAssocNodeCount=dlbDot11IfAssocNodeCount, PYSNMP_MODULE_ID=dlb802dot11ExtMIB, dlbDot11IfRxInvalidFrag=dlbDot11IfRxInvalidFrag, dlbDot11RmtNodeAssociated=dlbDot11RmtNodeAssociated, dlbDot11IfCountryCode=dlbDot11IfCountryCode, dlbDot11RmtNodeMacAddress=dlbDot11RmtNodeMacAddress, dlbDot11RmtNodeDisassocTime=dlbDot11RmtNodeDisassocTime, dlbDot11IfMaxLinkQuality=dlbDot11IfMaxLinkQuality, dlb802dot11ExtMIBObjects=dlb802dot11ExtMIBObjects)
