#
# PySNMP MIB module BAY-STACK-IPV6-MLD-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-IPV6-MLD-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressIPv6, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
PortSet, = mibBuilder.importSymbols("RAPID-CITY", "PortSet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, iso, Integer32, TimeTicks, Gauge32, MibIdentifier, ModuleIdentity, Counter32, Unsigned32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "iso", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier", "ModuleIdentity", "Counter32", "Unsigned32", "ObjectIdentity", "NotificationType")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackIpv6MldSnoopingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 44))
bayStackIpv6MldSnoopingMib.setRevisions(('2015-05-29 00:00', '2015-01-22 00:00', '2014-10-23 00:00', '2014-08-11 00:00', '2014-01-16 00:00', '2013-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackIpv6MldSnoopingMib.setRevisionsDescriptions(('Ver 6: Corrected MIB compiling errors.', 'Ver 5: Inverted the syntaxes for bsIpv6MldSnoopingProxyCacheType and bsIpv6MldSnoopingProxyCacheMode objects', 'Ver 4: Added bsIpv6MldSnoopingInterfaceFlushPorts object, bsIpv6MldSnoopingFlushPorts scalar object', 'Ver 3: Added bsIpv6MldSnoopingProxyCacheTable, bsIpv6MldSnoopingInterfaceFlush object, bsIpv6MldSnoopingFlush scalar object; Updated bsIpv6MldSnoopingInterfaceOperationalVersion, bsIpv6MldSnoopingInterfaceSendQuery, bsIpv6MldSnoopingInterfaceProxy objects descriptions', 'Ver 2: Added bsIpv6MldSnoopingInterfaceOperationalVersion, bsIpv6MldSnoopingInterfaceSendQuery, bsIpv6MldSnoopingInterfaceProxy', 'Ver 1: Initial version.',))
if mibBuilder.loadTexts: bayStackIpv6MldSnoopingMib.setLastUpdated('201505290000Z')
if mibBuilder.loadTexts: bayStackIpv6MldSnoopingMib.setOrganization('Avaya')
if mibBuilder.loadTexts: bayStackIpv6MldSnoopingMib.setContactInfo('avaya.com')
if mibBuilder.loadTexts: bayStackIpv6MldSnoopingMib.setDescription('This MIB module is used for IPv6 MLD Snooping configuration.')
bsIpv6MldSnoopingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 44, 0))
bsIpv6MldSnoopingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 44, 1))
bsIpv6MldSnoopingScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 44, 2))
bsIpv6MldSnoopingInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1), )
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceTable.setDescription('The (conceptual) table listing IPv6 MLD Snooping interfaces.')
bsIpv6MldSnoopingInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingInterfaceIfIndex"))
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceEntry.setDescription('An entry (conceptual row) representing an IPv6 MLD Snooping interface.')
bsIpv6MldSnoopingInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIfIndex.setDescription('The internetwork-layer interface value of the interface for which IPv6 MLD Snooping is enabled.')
bsIpv6MldSnoopingInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 2), Unsigned32().clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQueryInterval.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQueryInterval.setDescription('The frequency at which IPv6 MLD Snooping Host-Query packets are transmitted on this interface.')
bsIpv6MldSnoopingInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceStatus.setDescription('Row status for create/delete.')
bsIpv6MldSnoopingInterfaceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 4), Unsigned32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceVersion.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceVersion.setDescription('The version of IPv6 MLD Snooping which is running on this interface. This object is a place holder to allow for new versions of MLD to be introduced. Version 1 of MLD is defined in RFC 2710.')
bsIpv6MldSnoopingInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 5), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQuerier.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQuerier.setDescription('The address of the IPv6 MLD Snooping Querier on the IPv6 subnet to which this interface is attached.')
bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 6), Unsigned32().clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay.setDescription('The maximum query response time advertised in IPv6 MLD Snooping queries on this interface.')
bsIpv6MldSnoopingInterfaceJoins = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceJoins.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceJoins.setDescription('The number of times a group membership has been added on this interface; that is, the number of times an entry for this interface has been added to the Cache Table. This object gives an indication of the amount of MLD activity over time.')
bsIpv6MldSnoopingInterfaceGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceGroups.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceGroups.setDescription('The current number of entries for this interface in the Cache Table.')
bsIpv6MldSnoopingInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 9), Unsigned32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceRobustness.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceRobustness.setDescription('The Robustness Variable allows tuning for the expected packet loss on a subnet. If a subnet is expected to be lossy, the Robustness Variable may be increased. IPv6 MLD Snooping is robust to (Robustness Variable-1) packet losses. The discussion of the Robustness Variable is in Section 7.1 of RFC 2710.')
bsIpv6MldSnoopingInterfaceLastListenQueryIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 10), Unsigned32().clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceLastListenQueryIntvl.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceLastListenQueryIntvl.setDescription('The Last Member Query Interval is the Max Response Delay inserted into Group-Specific Queries sent in response to Leave Group messages, and is also the amount of time between Group-Specific Query messages. This value may be tuned to modify the leave latency of the network. A reduced value results in reduced time to detect the loss of the last member of a group.')
bsIpv6MldSnoopingInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 11), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceProxyIfIndex.setDescription('Some devices implement a form of MLD proxying whereby memberships learned on the interface represented by this row, cause MLD Multicast Listener Reports to be sent on the internetwork-layer interface identified by this object. Such a device would implement mldRouterMIBGroup only on its router interfaces (those interfaces with non-zero mldInterfaceProxyIfIndex). Typically, the value of this object is 0, indicating that no proxying is being done.')
bsIpv6MldSnoopingInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQuerierUpTime.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQuerierUpTime.setDescription('The time since mldInterfaceQuerier was last changed.')
bsIpv6MldSnoopingInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQuerierExpiryTime.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceQuerierExpiryTime.setDescription('The time remaining before the Other Querier Present Timer expires. If the local system is the querier, the value of this object is zero.')
bsIpv6MldSnoopingInterfaceEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceEnabled.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceEnabled.setDescription('This object controls whether IPv6 MLD Snooping is enabled on this interface.')
bsIpv6MldSnoopingInterfaceIgmpMRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 15), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIgmpMRouterPorts.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIgmpMRouterPorts.setDescription('The set of ports in this interface that provide connectivity to an IPv6 Multicast router.')
bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 16), PortSet()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts.setDescription('The set of active ports in this interface that provide connectivity to an IPv6 Multicast router.')
bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration.setDescription('Multicast querier router aging time out.')
bsIpv6MldSnoopingInterfaceOperationalVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceOperationalVersion.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceOperationalVersion.setDescription('The operational version of IPv6 MLD Snooping which is running on this interface at the moment.')
bsIpv6MldSnoopingInterfaceSendQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceSendQuery.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceSendQuery.setDescription('This object controls whether IPv6 MLD Send-Query is enabled on this interface.')
bsIpv6MldSnoopingInterfaceProxy = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceProxy.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceProxy.setDescription('This object controls whether IPv6 MLD Proxy is enabled on this interface.')
bsIpv6MldSnoopingInterfaceFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("groups", 2), ("mrouters", 3), ("all", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceFlush.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceFlush.setDescription('This object is used to remove MLD members from this interface. noAction(1) value is returned at read. all(4) value is used to flush groups and mrouters.')
bsIpv6MldSnoopingInterfaceFlushPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 22), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceFlushPorts.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingInterfaceFlushPorts.setDescription('The set of ports in this interface that are going to be flushed. An empty port set is returned at read.')
bsIpv6MldSnoopingCacheTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2), )
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheTable.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheTable.setDescription('The (conceptual) table listing the IPv6 multicast groups for which there are members on a particular interface.')
bsIpv6MldSnoopingCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingCacheAddress"), (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingCacheIfIndex"))
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheEntry.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheEntry.setDescription('An entry (conceptual row) in the bsIpv6MldSnoopingCacheTable.')
bsIpv6MldSnoopingCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 1), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheAddress.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheAddress.setDescription('The IPv6 multicast group address for which this entry contains information.')
bsIpv6MldSnoopingCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheIfIndex.setDescription('The internetwork-layer interface for which this entry contains information for an IPv6 multicast group address.')
bsIpv6MldSnoopingCacheSelf = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheSelf.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheSelf.setDescription('An indication of whether the local system is a member of this group address on this interface.')
bsIpv6MldSnoopingCacheLastReporter = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 4), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheLastReporter.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheLastReporter.setDescription('The IPv6 address of the source of the last membership report received for this IPv6 Multicast group address on this interface. If no membership report has been received, this object has the value 0::0.')
bsIpv6MldSnoopingCacheUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheUpTime.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheUpTime.setDescription('The time elapsed since this entry was created.')
bsIpv6MldSnoopingCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheExpiryTime.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheExpiryTime.setDescription('The minimum amount of time remaining before this entry will be aged out. A value of 0 indicates that the entry is only present because bsIpv6MldSnoopingCacheSelf is true and that if the router left the group, this entry would be aged out immediately. Note that some implementations may process Membership Reports from the local system in the same way as reports from other hosts, so a value of 0 is not required.')
bsIpv6MldSnoopingCacheStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheStatus.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheStatus.setDescription('The status of this row, by which new entries may be created, or existing entries deleted from this table.')
bsIpv6MldSnoopingCacheType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dynamic", 2), ("static", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheType.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingCacheType.setDescription('The type of this entry.')
bsIpv6MldSnoopingIgmpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3), )
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupTable.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupTable.setDescription('The (conceptual) table listing IPv6 MLD Snooping IGMP groups.')
bsIpv6MldSnoopingIgmpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupIpv6Address"), (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupMembers"), (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupSourceAddress"), (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupIfIndex"))
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupEntry.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupEntry.setDescription('An entry (conceptual row) representing an IPv6 MLD Snooping IGMP group.')
bsIpv6MldSnoopingIgmpGroupIpv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 1), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupIpv6Address.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupIpv6Address.setDescription('Multicast group Address (Class D) that others want to join. A group address can be the same for many incoming ports.')
bsIpv6MldSnoopingIgmpGroupMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 2), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupMembers.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupMembers.setDescription('IPv6 Address of a source that has sent group report wishing to join this group.')
bsIpv6MldSnoopingIgmpGroupSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 3), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupSourceAddress.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupSourceAddress.setDescription('IPv6 Address of the source.')
bsIpv6MldSnoopingIgmpGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupIfIndex.setDescription('An unique value to identify a physical interface or a logical interface (VLAN), which has received Group reports from various sources.')
bsIpv6MldSnoopingIgmpGroupInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupInPort.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupInPort.setDescription('Value to identify physical interfaces or logical interfaces (VLANs), which has received Group reports from various sources.')
bsIpv6MldSnoopingIgmpGroupExpiration = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupExpiration.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupExpiration.setDescription('Time left before the group report expired on this port. Only one of this variable port. This variable is updated upon receiving a group report.')
bsIpv6MldSnoopingIgmpGroupUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupUserId.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupUserId.setDescription('User-id sending this group.')
bsIpv6MldSnoopingIgmpGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dynamic", 2), ("static", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupType.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupType.setDescription('The type of this entry.')
bsIpv6MldSnoopingIgmpGroupMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("received", 1), ("include", 2), ("exclude", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupMode.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupMode.setDescription('Address mode.')
bsIpv6MldSnoopingIgmpGroupVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2))).clone('version1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupVersion.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingIgmpGroupVersion.setDescription('Group version.')
bsIpv6MldSnoopingProxyCacheTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4), )
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheTable.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheTable.setDescription('The (conceptual) table listing the IPv6 multicast groups for which the switch is registered in order to receive the multicast traffic.')
bsIpv6MldSnoopingProxyCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1), ).setIndexNames((0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingProxyCacheIfIndex"), (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingProxyCacheGroupAddress"), (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingProxyCacheSourceAddress"))
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheEntry.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheEntry.setDescription('An entry (conceptual row) in the bsIpv6MldSnoopingProxyCacheTable.')
bsIpv6MldSnoopingProxyCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheIfIndex.setDescription('An unique value to identify a logical interface (VLAN) which is registered as MLD host for receiving multicast traffic')
bsIpv6MldSnoopingProxyCacheGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 2), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheGroupAddress.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheGroupAddress.setDescription('The IPv6 destination address of the multicast traffic that the interface is registered for receiving it.')
bsIpv6MldSnoopingProxyCacheSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 3), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheSourceAddress.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheSourceAddress.setDescription('The IPv6 source address of the multicast traffic that the interface is registered for receiving it.')
bsIpv6MldSnoopingProxyCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheVersion.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheVersion.setDescription('Interface proxy version.')
bsIpv6MldSnoopingProxyCacheType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheType.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheType.setDescription('The entry registration type (static or dynamic).')
bsIpv6MldSnoopingProxyCacheMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version1", 1), ("include", 2), ("exclude", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheMode.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingProxyCacheMode.setDescription('Proxy mode for MLDv2 entries. version1(1) value is returned for MLDv1 entries')
bsIpv6MldSnoopingFlush = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 44, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("groups", 2), ("mrouters", 3), ("all", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingFlush.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingFlush.setDescription('This object is used to remove MLD members from all the interfaces. noAction(1) value is returned at read. all(4) value is used to flush groups and mrouters.')
bsIpv6MldSnoopingFlushPorts = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 44, 2, 2), PortSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsIpv6MldSnoopingFlushPorts.setStatus('current')
if mibBuilder.loadTexts: bsIpv6MldSnoopingFlushPorts.setDescription('The set of ports from all interfaces that are going to be flushed. An empty port set is returned at read.')
mibBuilder.exportSymbols("BAY-STACK-IPV6-MLD-SNOOPING-MIB", bsIpv6MldSnoopingObjects=bsIpv6MldSnoopingObjects, bsIpv6MldSnoopingInterfaceSendQuery=bsIpv6MldSnoopingInterfaceSendQuery, bsIpv6MldSnoopingProxyCacheTable=bsIpv6MldSnoopingProxyCacheTable, bsIpv6MldSnoopingProxyCacheEntry=bsIpv6MldSnoopingProxyCacheEntry, bsIpv6MldSnoopingIgmpGroupIpv6Address=bsIpv6MldSnoopingIgmpGroupIpv6Address, bsIpv6MldSnoopingProxyCacheMode=bsIpv6MldSnoopingProxyCacheMode, bsIpv6MldSnoopingIgmpGroupInPort=bsIpv6MldSnoopingIgmpGroupInPort, bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration=bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration, bsIpv6MldSnoopingInterfaceFlushPorts=bsIpv6MldSnoopingInterfaceFlushPorts, bsIpv6MldSnoopingCacheTable=bsIpv6MldSnoopingCacheTable, bsIpv6MldSnoopingInterfaceVersion=bsIpv6MldSnoopingInterfaceVersion, bsIpv6MldSnoopingInterfaceEnabled=bsIpv6MldSnoopingInterfaceEnabled, bayStackIpv6MldSnoopingMib=bayStackIpv6MldSnoopingMib, bsIpv6MldSnoopingFlushPorts=bsIpv6MldSnoopingFlushPorts, bsIpv6MldSnoopingIgmpGroupEntry=bsIpv6MldSnoopingIgmpGroupEntry, bsIpv6MldSnoopingCacheIfIndex=bsIpv6MldSnoopingCacheIfIndex, bsIpv6MldSnoopingIgmpGroupMembers=bsIpv6MldSnoopingIgmpGroupMembers, bsIpv6MldSnoopingCacheLastReporter=bsIpv6MldSnoopingCacheLastReporter, bsIpv6MldSnoopingIgmpGroupVersion=bsIpv6MldSnoopingIgmpGroupVersion, bsIpv6MldSnoopingInterfaceQuerier=bsIpv6MldSnoopingInterfaceQuerier, bsIpv6MldSnoopingInterfaceQuerierUpTime=bsIpv6MldSnoopingInterfaceQuerierUpTime, bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay=bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay, bsIpv6MldSnoopingCacheType=bsIpv6MldSnoopingCacheType, bsIpv6MldSnoopingInterfaceOperationalVersion=bsIpv6MldSnoopingInterfaceOperationalVersion, bsIpv6MldSnoopingInterfaceProxy=bsIpv6MldSnoopingInterfaceProxy, bsIpv6MldSnoopingInterfaceQueryInterval=bsIpv6MldSnoopingInterfaceQueryInterval, bsIpv6MldSnoopingInterfaceIgmpMRouterPorts=bsIpv6MldSnoopingInterfaceIgmpMRouterPorts, bsIpv6MldSnoopingCacheEntry=bsIpv6MldSnoopingCacheEntry, bsIpv6MldSnoopingIgmpGroupTable=bsIpv6MldSnoopingIgmpGroupTable, bsIpv6MldSnoopingNotifications=bsIpv6MldSnoopingNotifications, bsIpv6MldSnoopingIgmpGroupExpiration=bsIpv6MldSnoopingIgmpGroupExpiration, bsIpv6MldSnoopingCacheAddress=bsIpv6MldSnoopingCacheAddress, bsIpv6MldSnoopingCacheExpiryTime=bsIpv6MldSnoopingCacheExpiryTime, bsIpv6MldSnoopingIgmpGroupType=bsIpv6MldSnoopingIgmpGroupType, bsIpv6MldSnoopingInterfaceJoins=bsIpv6MldSnoopingInterfaceJoins, bsIpv6MldSnoopingInterfaceStatus=bsIpv6MldSnoopingInterfaceStatus, bsIpv6MldSnoopingInterfaceGroups=bsIpv6MldSnoopingInterfaceGroups, bsIpv6MldSnoopingProxyCacheSourceAddress=bsIpv6MldSnoopingProxyCacheSourceAddress, bsIpv6MldSnoopingInterfaceTable=bsIpv6MldSnoopingInterfaceTable, bsIpv6MldSnoopingIgmpGroupSourceAddress=bsIpv6MldSnoopingIgmpGroupSourceAddress, bsIpv6MldSnoopingIgmpGroupMode=bsIpv6MldSnoopingIgmpGroupMode, bsIpv6MldSnoopingInterfaceEntry=bsIpv6MldSnoopingInterfaceEntry, bsIpv6MldSnoopingInterfaceFlush=bsIpv6MldSnoopingInterfaceFlush, bsIpv6MldSnoopingCacheStatus=bsIpv6MldSnoopingCacheStatus, bsIpv6MldSnoopingCacheUpTime=bsIpv6MldSnoopingCacheUpTime, bsIpv6MldSnoopingIgmpGroupUserId=bsIpv6MldSnoopingIgmpGroupUserId, bsIpv6MldSnoopingInterfaceLastListenQueryIntvl=bsIpv6MldSnoopingInterfaceLastListenQueryIntvl, bsIpv6MldSnoopingProxyCacheGroupAddress=bsIpv6MldSnoopingProxyCacheGroupAddress, bsIpv6MldSnoopingInterfaceRobustness=bsIpv6MldSnoopingInterfaceRobustness, bsIpv6MldSnoopingInterfaceProxyIfIndex=bsIpv6MldSnoopingInterfaceProxyIfIndex, bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts=bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts, bsIpv6MldSnoopingProxyCacheVersion=bsIpv6MldSnoopingProxyCacheVersion, bsIpv6MldSnoopingFlush=bsIpv6MldSnoopingFlush, bsIpv6MldSnoopingInterfaceIfIndex=bsIpv6MldSnoopingInterfaceIfIndex, bsIpv6MldSnoopingInterfaceQuerierExpiryTime=bsIpv6MldSnoopingInterfaceQuerierExpiryTime, bsIpv6MldSnoopingScalars=bsIpv6MldSnoopingScalars, bsIpv6MldSnoopingProxyCacheIfIndex=bsIpv6MldSnoopingProxyCacheIfIndex, bsIpv6MldSnoopingIgmpGroupIfIndex=bsIpv6MldSnoopingIgmpGroupIfIndex, bsIpv6MldSnoopingProxyCacheType=bsIpv6MldSnoopingProxyCacheType, PYSNMP_MODULE_ID=bayStackIpv6MldSnoopingMib, bsIpv6MldSnoopingCacheSelf=bsIpv6MldSnoopingCacheSelf)
