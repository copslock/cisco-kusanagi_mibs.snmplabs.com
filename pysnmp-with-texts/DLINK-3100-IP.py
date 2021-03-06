#
# PySNMP MIB module DLINK-3100-IP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-IP
# Produced by pysmi-0.3.4 at Wed May  1 12:48:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ipCidrRouteTos, ipCidrRouteMask, ipCidrRouteEntry, ipCidrRouteDest, ipCidrRouteNextHop = mibBuilder.importSymbols("IP-FORWARD-MIB", "ipCidrRouteTos", "ipCidrRouteMask", "ipCidrRouteEntry", "ipCidrRouteDest", "ipCidrRouteNextHop")
ipAddrEntry, = mibBuilder.importSymbols("IP-MIB", "ipAddrEntry")
rip2IfConfEntry, = mibBuilder.importSymbols("RFC1389-MIB", "rip2IfConfEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Bits, Gauge32, MibIdentifier, Unsigned32, iso, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Bits", "Gauge32", "MibIdentifier", "Unsigned32", "iso", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
ipSpec = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26))
ipSpec.setRevisions(('2006-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipSpec.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ipSpec.setLastUpdated('200606220000Z')
if mibBuilder.loadTexts: ipSpec.setOrganization('Dlink, Inc.')
if mibBuilder.loadTexts: ipSpec.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: ipSpec.setDescription('The private MIB module definition for IP MIB.')
rsIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1), )
if mibBuilder.loadTexts: rsIpAddrTable.setStatus('current')
if mibBuilder.loadTexts: rsIpAddrTable.setDescription('This table is parralel to MIB II IpAddrTable, and is used to add/delete entries to/from that table. In addition it contains private objects.')
rsIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1), ).setIndexNames((0, "DLINK-3100-IP", "rsIpAdEntAddr"))
if mibBuilder.loadTexts: rsIpAddrEntry.setStatus('current')
if mibBuilder.loadTexts: rsIpAddrEntry.setDescription("The addressing information for one of this entity's IP addresses.")
rsIpAdEntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpAdEntAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntAddr.setDescription("The IP address to which this entry's addressing information pertains.")
rsIpAdEntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntIfIndex.setDescription('The index value which uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
rsIpAdEntNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntNetMask.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntNetMask.setDescription('The subnet mask associated with the IP address of this entry. The value of the mask is an IP address with all the network bits set to 1 and all the hosts bits set to 0.')
rsIpAdEntForwardIpBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntForwardIpBroadcast.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntForwardIpBroadcast.setDescription(' This variable controls forwarding of IP (sub)net-directed broadcasts destined for an attached sub(net). ')
rsIpAdEntBackupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntBackupAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntBackupAddr.setDescription('In case there are two IP routers in the domain, the address of the second IP router.')
rsIpAdEntStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntStatus.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntStatus.setDescription(' The validity of this entry. Invalid indicates that this entry is invalid in IpAddrTable (MIB II).')
rsIpAdEntBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntBcastAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntBcastAddr.setDescription(' Indicates how the host part of ip subnet broadcast messages will be filled: 0 - host part will be filled by 0 1 - host part will be filled by 1.')
rsIpAdEntArpServer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntArpServer.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntArpServer.setDescription('Indicates whether the router will reply to incoming ARP requests on this interface, providing the physical address corresponding to this IP interface.')
rsIpAdEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntName.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntName.setDescription('The IP Interface name')
rsIpAdEntOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2), ("internal", 3), ("default", 4))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntOwner.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntOwner.setDescription('The IP Interface owner. Static if interface defined by user, dhcp if received by boot protocol like DHCP and internal for internal usage.')
rsIpAdEntAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntAdminStatus.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntAdminStatus.setDescription('The IP Interface admin status.')
rsIpAdEntOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpAdEntOperStatus.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntOperStatus.setDescription('If active the interface can be used to send and receive frames.')
rsIpAdEntPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIpAdEntPrecedence.setStatus('current')
if mibBuilder.loadTexts: rsIpAdEntPrecedence.setDescription('The IP preference, to be selected as source IP for rsIpAdEntIfIndex. this source IP selection is first by preference value. if more than one IP has the same preference the one with the lowest IP is selected. (higher value -> higher preference)')
icmpSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2))
rsIcmpGenErrMsgEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpGenErrMsgEnable.setStatus('current')
if mibBuilder.loadTexts: rsIcmpGenErrMsgEnable.setDescription('This variable controlls the ability to generate ICMP error messages')
rsIcmpRdTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2), )
if mibBuilder.loadTexts: rsIcmpRdTable.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdTable.setDescription('This table contains ICMP Router Discovery parameters configurated per IP interface.')
rsIcmpRdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1), ).setIndexNames((0, "DLINK-3100-IP", "rsIcmpRdIpAddr"))
if mibBuilder.loadTexts: rsIcmpRdEntry.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdEntry.setDescription('The ICMP parameters configurated for IP interface.')
rsIcmpRdIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIcmpRdIpAddr.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdIpAddr.setDescription("The IP address to which this entry's information pertains.")
rsIcmpRdIpAdvertAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 2), IpAddress().clone(hexValue="E0000001")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpRdIpAdvertAddr.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdIpAdvertAddr.setDescription(' The IP destination address to be used for multicast Router Advertisements sent from the interface. The only permissible values are the all-systems multicast address, 224.0.0.1, or the limited-broadcast address, 255.255.255.255.')
rsIcmpRdMaxAdvertInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 1800)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpRdMaxAdvertInterval.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdMaxAdvertInterval.setDescription('The maximum time allowed between sending multicast Router Advertisements from the interface, in seconds. Must be no less than 4 seconds and no greater than 1800 seconds.')
rsIcmpRdMinAdvertInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpRdMinAdvertInterval.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdMinAdvertInterval.setDescription('The minimum time allowed between sending unsolicited multicast Router Advertisements from the interface, in seconds. Must be no less than 3 seconds and no greater than rsIcmpRdMaxAdvertInterval. Default: 0.75 * rsIcmpRdMaxAdvertInterval.')
rsIcmpRdAdvertLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpRdAdvertLifetime.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdAdvertLifetime.setDescription('The maximum length of time that the advertised addresses are to be considered as valid. Must be no less than rsIcmpRdMaxAdvertInterval and no greater than 9000 seconds. Default: 3 * rsIcmpRdMaxAdvertInterval.')
rsIcmpRdAdvertise = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpRdAdvertise.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdAdvertise.setDescription('A flag indicating whether or not the address is to be advertised.')
rsIcmpRdPreferenceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpRdPreferenceLevel.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdPreferenceLevel.setDescription('The preferability of the address as a default router address, relative to other router addresses on the same subnet.')
rsIcmpRdEntStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 2, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsIcmpRdEntStatus.setStatus('current')
if mibBuilder.loadTexts: rsIcmpRdEntStatus.setDescription('Setting of any value to this object set values of all fields to the default values.')
rip2Spec = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 3))
arpSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4))
rsArpDeleteTable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 0), ("deleteArpTab", 1), ("deleteIpArpDynamicEntries", 2), ("deleteIpArpStaticEntries", 3), ("deleteIpArpDelDynamicRefreshStatic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsArpDeleteTable.setStatus('current')
if mibBuilder.loadTexts: rsArpDeleteTable.setDescription('Setting to value deleteArpTab(1): deletes the arp table - static and dynamic entries deleteIpArpDynamicEntries(2): delete all dynamic entries deleteIpArpStaticEntries(3): delete all static entries deleteIpArpDelDynamicRefreshStatic(4) - delete all dynamic - refresh static, thus refrashing FFT. on get returns the last action')
rsArpInactiveTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 40000000)).clone(60000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsArpInactiveTimeOut.setStatus('current')
if mibBuilder.loadTexts: rsArpInactiveTimeOut.setDescription('This variable defines the maximum time period (in second) that can pass between ARP requests concerning an entry in the ARP table. After this time period, the entry is deleted from the table.')
rsArpProxy = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsArpProxy.setStatus('current')
if mibBuilder.loadTexts: rsArpProxy.setDescription('When ARP Proxy is enabled, the router can respond to ARP requests for nodes located on a different sub-net, provided they are it its network table. The router responds with its own MAC address. When ARP Proxy is disabled, the router responds only to ARP requests for its own IP addresses.')
rsArpRequestsSent = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsArpRequestsSent.setStatus('current')
if mibBuilder.loadTexts: rsArpRequestsSent.setDescription('Displays how many ARP requests have been sent out to an ARP server for address resolution.')
rsArpRepliesSent = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsArpRepliesSent.setStatus('current')
if mibBuilder.loadTexts: rsArpRepliesSent.setDescription('Displays how many ARP replies have been sent out to an ARP client in response to request packets.')
rsArpProxyRepliesSent = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsArpProxyRepliesSent.setStatus('current')
if mibBuilder.loadTexts: rsArpProxyRepliesSent.setDescription('Displays how many proxy ARP replies have been sent out in response to request packets. A proxy router serving as a gateway to a subnet would respond with a proxy reply.')
rsArpUnresolveTimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsArpUnresolveTimer.setStatus('current')
if mibBuilder.loadTexts: rsArpUnresolveTimer.setDescription('Specifies the frequency in seconds in which to send out ARP requests to resolve the Next Hop MAC address.')
rsArpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsArpMibVersion.setStatus('current')
if mibBuilder.loadTexts: rsArpMibVersion.setDescription("MIB's version, the current version is 2. Version 1: rsArpDeleteTable Setting this object to any not-null value has the effect of deleting all entries of the ARP table. Version 2: rsArpDeleteTable Setting to value deleteArpTab(1): deletes the arp table - static and dynamic entries deleteIpArpDynamicEntries(2): delete all dynamic entries deleteIpArpStaticEntries(3): delete all static entries deleteIpArpDelDynamicRefreshStatic(4): delete all dynamic - refresh static, thus refrashing FFT. on get returns the last action. New MIB variables support: rsArpRequestsSent rsArpRepliesSent rsArpProxyRepliesSent rsArpUnresolveTimer rsArpMibVersion")
tftp = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5))
rsTftpRetryTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 1), Integer32().clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTftpRetryTimeOut.setStatus('current')
if mibBuilder.loadTexts: rsTftpRetryTimeOut.setDescription(' General Retransmission time-out value (seconds) ')
rsTftpTotalTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 2), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTftpTotalTimeOut.setStatus('current')
if mibBuilder.loadTexts: rsTftpTotalTimeOut.setDescription(' Total Retransmission time-out value (seconds) ')
rsSendConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsSendConfigFile.setStatus('current')
if mibBuilder.loadTexts: rsSendConfigFile.setDescription('The file name include path where the Router Server will put the full configuration. The default destination address will be the sender address.')
rsGetConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsGetConfigFile.setStatus('current')
if mibBuilder.loadTexts: rsGetConfigFile.setDescription('The file name include path where the Router Server will get the full configuration from. The default destination address will be the sender address.')
rsLoadSoftware = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsLoadSoftware.setStatus('current')
if mibBuilder.loadTexts: rsLoadSoftware.setDescription('The file name include path where the Router Server will get the software. The default source address will be the sender address.')
rsFileServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsFileServerAddress.setStatus('current')
if mibBuilder.loadTexts: rsFileServerAddress.setDescription('The IP address of the configuration / sw server.')
rsSoftwareDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsSoftwareDeviceName.setStatus('current')
if mibBuilder.loadTexts: rsSoftwareDeviceName.setDescription('The Software Device Name specifies a device name, using this Software')
rsSoftwareFileAction = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 5, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("download", 1), ("upload", 2))).clone('download')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsSoftwareFileAction.setStatus('current')
if mibBuilder.loadTexts: rsSoftwareFileAction.setDescription('Holds the current action done on the software file ')
ipRedundancy = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 6))
ipRouteLeaking = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 7))
ipRipFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 8))
rsRipEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsRipEnable.setStatus('current')
if mibBuilder.loadTexts: rsRipEnable.setDescription('Enables or disables RIP.')
rsTelnetPassword = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 11), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTelnetPassword.setStatus('current')
if mibBuilder.loadTexts: rsTelnetPassword.setDescription('')
rlTranslationNameToIpTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 12), )
if mibBuilder.loadTexts: rlTranslationNameToIpTable.setStatus('current')
if mibBuilder.loadTexts: rlTranslationNameToIpTable.setDescription("This table translates IP interfaces's name to IP interface's address")
rlTranslationNameToIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 12, 1), ).setIndexNames((1, "DLINK-3100-IP", "rlTranslationNameToIpName"))
if mibBuilder.loadTexts: rlTranslationNameToIpEntry.setStatus('current')
if mibBuilder.loadTexts: rlTranslationNameToIpEntry.setDescription('The row definition for this table.')
rlTranslationNameToIpName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 12, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTranslationNameToIpName.setStatus('current')
if mibBuilder.loadTexts: rlTranslationNameToIpName.setDescription('The IP Interface name')
rlTranslationNameToIpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 12, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTranslationNameToIpIpAddr.setStatus('current')
if mibBuilder.loadTexts: rlTranslationNameToIpIpAddr.setDescription('The IP Interface address')
rlIpRoutingProtPreference = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 13))
rlOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 14))
rlIpAddrTableMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpAddrTableMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlIpAddrTableMibVersion.setDescription("The IpAddrTable MIB's version.")
rlIpCidrRouteExtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 16), )
if mibBuilder.loadTexts: rlIpCidrRouteExtTable.setStatus('current')
if mibBuilder.loadTexts: rlIpCidrRouteExtTable.setDescription('Augmenting ipCidrRouteTable (ip forwarfing information table) for added info as read only')
rlIpCidrRouteExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 16, 1), )
ipCidrRouteEntry.registerAugmentions(("DLINK-3100-IP", "rlIpCidrRouteExtEntry"))
rlIpCidrRouteExtEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
if mibBuilder.loadTexts: rlIpCidrRouteExtEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpCidrRouteExtEntry.setDescription('A row of the table ipCidrRouteTable Extended by this definition.')
rlIpCidrRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 16, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("local", 1), ("netmgmt", 2), ("rip", 3), ("ospfInternal", 4), ("ospfExternal", 5), ("ospfAggregateNetRange", 6), ("bgp4Internal", 7), ("bgp4External", 8), ("aggregateRoute", 9), ("other", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpCidrRouteProto.setStatus('current')
if mibBuilder.loadTexts: rlIpCidrRouteProto.setDescription('Added infor for ipCidrRouteTable. extends the info of ipCidrRouteProto to show the route inner protocol. Allowes the user to see which type of route in the protocol e.g. ospf internal, ospf external.')
rlIpStaticRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17))
rlIpStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1), )
if mibBuilder.loadTexts: rlIpStaticRouteTable.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteTable.setDescription("This entity's static (user configured) IP Routing table. entries are MAX-ACCESSible even if not used for forwarding ")
rlIpStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1), ).setIndexNames((0, "DLINK-3100-IP", "rlIpStaticRouteDest"), (0, "DLINK-3100-IP", "rlIpStaticRouteMask"), (0, "DLINK-3100-IP", "rlIpStaticRouteTos"), (0, "DLINK-3100-IP", "rlIpStaticRouteNextHop"))
if mibBuilder.loadTexts: rlIpStaticRouteEntry.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteEntry.setDescription('A particular Static(user configured) route to a particular destina- tion, under a particular policy.')
rlIpStaticRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpStaticRouteDest.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteDest.setDescription('The destination IP address of this route. This object may not take a Multicast (Class D) address value. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the rlIpStaticRouteMask object is not equal to x.')
rlIpStaticRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpStaticRouteMask.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteMask.setDescription('Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the rlIpStaticRouteDest field. For those systems that do not support arbitrary subnet masks, an agent constructs the value of the rlIpStaticRouteMask by reference to the IP Ad- dress Class. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the rlIpStaticRouteDest object is not equal to ipCidrRoute- Dest.')
rlIpStaticRouteTos = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpStaticRouteTos.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteTos.setDescription('See ipCidrRouteTos definition For now only value 0 is valid')
rlIpStaticRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpStaticRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteNextHop.setDescription('On remote routes, the address of the next sys- tem en route; Otherwise, 0.0.0.0.')
rlIpStaticRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpStaticRouteMetric.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteMetric.setDescription('The routing metric for this route. The semantics of this metric are determined by the user. normal semantic will be next hop count or some administarative distance to create routing policy.')
rlIpStaticRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reject", 1), ("local", 2), ("remote", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpStaticRouteType.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteType.setDescription('The type of route. Note that local(3) refers to a route for which the next hop is the final destination this is the case when user overides the a local interface entry to change it parameters; remote(4) refers to a route for which the next hop is not the final destina- tion. reject (2) refers to a route which, if matched, discards the message as unreachable. This is may be used as a means of correctly aggregating routes, When static routes are distributed (leaked) to other protocols.')
rlIpStaticRouteNextHopAS = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpStaticRouteNextHopAS.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteNextHopAS.setDescription("The Autonomous System Number of the Next Hop. The semantics of this object are determined by the routing-protocol specified in the route's ipCidrRouteProto value. When this object is unknown or not relevant its value should be set to zero.")
rlIpStaticRouteForwardingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpStaticRouteForwardingStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteForwardingStatus.setDescription('active - An indication that the route has implication on routing inactive - the route is a backup route or it is down. It is not used in forwarding decision. Down means that the Ip interface on which it is configured is down. (Note: ip interface down may be for two reason - its admin status or the L2 interface , on which the ip interface is configured, status')
rlIpStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpStaticRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteRowStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
rlIpStaticRouteOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 17, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2), ("default", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpStaticRouteOwner.setStatus('current')
if mibBuilder.loadTexts: rlIpStaticRouteOwner.setDescription('Static - The route is configured over Static IP. This route is written to configuration files. Dhcp - The route is Configured by DHCP (received as part of DHCP configuration) This route IS NOT written to configuration files Dhcp - The route is Configured default system config exist till any other configuration is applied')
rlIpRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 26, 18))
mibBuilder.exportSymbols("DLINK-3100-IP", rlIpAddrTableMibVersion=rlIpAddrTableMibVersion, rlIpStaticRouteTable=rlIpStaticRouteTable, rsIcmpRdEntry=rsIcmpRdEntry, rlTranslationNameToIpIpAddr=rlTranslationNameToIpIpAddr, rsFileServerAddress=rsFileServerAddress, rsIpAdEntAdminStatus=rsIpAdEntAdminStatus, icmpSpec=icmpSpec, rsRipEnable=rsRipEnable, rsIcmpRdAdvertise=rsIcmpRdAdvertise, rlIpStaticRouteMetric=rlIpStaticRouteMetric, rsIpAdEntNetMask=rsIpAdEntNetMask, rlTranslationNameToIpTable=rlTranslationNameToIpTable, ipRouteLeaking=ipRouteLeaking, rlIpStaticRouteForwardingStatus=rlIpStaticRouteForwardingStatus, rsArpRepliesSent=rsArpRepliesSent, rsTftpRetryTimeOut=rsTftpRetryTimeOut, rlIpRoutingProtPreference=rlIpRoutingProtPreference, rsArpMibVersion=rsArpMibVersion, rsIpAdEntOwner=rsIpAdEntOwner, arpSpec=arpSpec, rlIpStaticRoute=rlIpStaticRoute, rsIcmpRdAdvertLifetime=rsIcmpRdAdvertLifetime, rsArpUnresolveTimer=rsArpUnresolveTimer, rlTranslationNameToIpEntry=rlTranslationNameToIpEntry, rsIcmpGenErrMsgEnable=rsIcmpGenErrMsgEnable, rsIpAdEntBackupAddr=rsIpAdEntBackupAddr, ipRipFilter=ipRipFilter, rsIpAddrEntry=rsIpAddrEntry, rsIcmpRdMinAdvertInterval=rsIcmpRdMinAdvertInterval, rlIpStaticRouteNextHopAS=rlIpStaticRouteNextHopAS, rsIpAdEntAddr=rsIpAdEntAddr, rlIpStaticRouteTos=rlIpStaticRouteTos, rsIpAdEntName=rsIpAdEntName, rsIcmpRdIpAdvertAddr=rsIcmpRdIpAdvertAddr, rsIcmpRdEntStatus=rsIcmpRdEntStatus, rlIpStaticRouteRowStatus=rlIpStaticRouteRowStatus, rlOspf=rlOspf, rlIpCidrRouteProto=rlIpCidrRouteProto, rsIpAdEntBcastAddr=rsIpAdEntBcastAddr, rsIpAdEntIfIndex=rsIpAdEntIfIndex, rlIpCidrRouteExtEntry=rlIpCidrRouteExtEntry, rlIpStaticRouteDest=rlIpStaticRouteDest, rlIpStaticRouteType=rlIpStaticRouteType, rip2Spec=rip2Spec, rlIpCidrRouteExtTable=rlIpCidrRouteExtTable, PYSNMP_MODULE_ID=ipSpec, rsLoadSoftware=rsLoadSoftware, rsIpAdEntForwardIpBroadcast=rsIpAdEntForwardIpBroadcast, rsIpAdEntOperStatus=rsIpAdEntOperStatus, rsIcmpRdTable=rsIcmpRdTable, rsArpInactiveTimeOut=rsArpInactiveTimeOut, rsArpProxy=rsArpProxy, rsIpAdEntArpServer=rsIpAdEntArpServer, rlIpStaticRouteMask=rlIpStaticRouteMask, ipSpec=ipSpec, rsIpAddrTable=rsIpAddrTable, rlIpStaticRouteOwner=rlIpStaticRouteOwner, rsArpProxyRepliesSent=rsArpProxyRepliesSent, rsIpAdEntPrecedence=rsIpAdEntPrecedence, ipRedundancy=ipRedundancy, rsIcmpRdMaxAdvertInterval=rsIcmpRdMaxAdvertInterval, rsSoftwareFileAction=rsSoftwareFileAction, rsIpAdEntStatus=rsIpAdEntStatus, rlIpRouter=rlIpRouter, rsIcmpRdIpAddr=rsIcmpRdIpAddr, rsIcmpRdPreferenceLevel=rsIcmpRdPreferenceLevel, rlIpStaticRouteEntry=rlIpStaticRouteEntry, rsGetConfigFile=rsGetConfigFile, rsSoftwareDeviceName=rsSoftwareDeviceName, rsSendConfigFile=rsSendConfigFile, rsTftpTotalTimeOut=rsTftpTotalTimeOut, rsArpDeleteTable=rsArpDeleteTable, rsArpRequestsSent=rsArpRequestsSent, rlIpStaticRouteNextHop=rlIpStaticRouteNextHop, tftp=tftp, rlTranslationNameToIpName=rlTranslationNameToIpName, rsTelnetPassword=rsTelnetPassword)
