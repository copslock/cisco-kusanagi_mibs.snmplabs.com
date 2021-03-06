#
# PySNMP MIB module AP-SYSTEM-NETWORK (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AP-SYSTEM-NETWORK
# Produced by pysmi-0.3.4 at Wed May  1 11:22:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, iso, Bits, Counter32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter64, TimeTicks, NotificationType, Gauge32, MibIdentifier, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Bits", "Counter32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "MibIdentifier", "ModuleIdentity", "Integer32")
TruthValue, MacAddress, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "RowStatus", "TextualConvention")
pepwave = MibIdentifier((1, 3, 6, 1, 4, 1, 27662))
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200))
apMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1))
apGeneralMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1))
ap_system_network_mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2)).setLabel("ap-system-network-mib")
if mibBuilder.loadTexts: ap_system_network_mib.setLastUpdated('2011081900Z')
if mibBuilder.loadTexts: ap_system_network_mib.setOrganization('PEPWAVE')
if mibBuilder.loadTexts: ap_system_network_mib.setContactInfo('')
if mibBuilder.loadTexts: ap_system_network_mib.setDescription('The MIB module for PEPWAVE Enterprise WiFi AP. iso(1).org(3).dod(6).internet(1).private(4). enterprises(1).pepwave(27662).productID(200).apMib(1).apGeneralMib(1).ap-system-network-mib(2)')
apNetworkInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1))
apWanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1))
apCurrentIpAddressMode = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("automatic", 0), ("manual", 1), ("pppoe", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCurrentIpAddressMode.setStatus('current')
if mibBuilder.loadTexts: apCurrentIpAddressMode.setDescription('This attribute indicates the current IP address mode of the AP.')
apCurrentIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCurrentIpAddress.setStatus('current')
if mibBuilder.loadTexts: apCurrentIpAddress.setDescription('This attribute indicates the current IP address of the AP.')
apCurrentSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCurrentSubnetMask.setStatus('current')
if mibBuilder.loadTexts: apCurrentSubnetMask.setDescription('This attribute indicates the current subnet mask of the AP.')
apCurrentGateway = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCurrentGateway.setStatus('current')
if mibBuilder.loadTexts: apCurrentGateway.setDescription('This attribute indicates the current default gateway of the AP.')
apCurrentDns = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apCurrentDns.setStatus('current')
if mibBuilder.loadTexts: apCurrentDns.setDescription('This attribute indicates the current dns of the AP.')
apPppoeInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 4))
apPppoeStatus = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("connecting", 1), ("connected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apPppoeStatus.setStatus('current')
if mibBuilder.loadTexts: apPppoeStatus.setDescription('This attribute indicates the status of PPPoE.')
apPppoeStatusMessage = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 1, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apPppoeStatusMessage.setStatus('current')
if mibBuilder.loadTexts: apPppoeStatusMessage.setDescription('This attribute indicates the status message of PPPoE.')
apNetworkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2))
apWanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1))
apKeepDefaultIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apKeepDefaultIp.setStatus('current')
if mibBuilder.loadTexts: apKeepDefaultIp.setDescription('This attribute indicates the keep default IP status of AP.')
apIpAddressMode = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("automatic", 0), ("manual", 1), ("pppoe", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpAddressMode.setStatus('current')
if mibBuilder.loadTexts: apIpAddressMode.setDescription('This attribute indicates the IP address mode of the AP.')
apIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpAddress.setStatus('current')
if mibBuilder.loadTexts: apIpAddress.setDescription('This attribute indicates the static management IP address of the AP.')
apSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSubnetMask.setStatus('current')
if mibBuilder.loadTexts: apSubnetMask.setDescription('This attribute indicates the static netmask of the management interface.')
apGateway = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apGateway.setStatus('current')
if mibBuilder.loadTexts: apGateway.setDescription('This attribute indicates the static gateway IP address for the management interface.')
apDns = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDns.setStatus('current')
if mibBuilder.loadTexts: apDns.setDescription('This attribute indicates the static DNS for the management interface.')
apLanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2))
apLanIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanIpAddress.setStatus('current')
if mibBuilder.loadTexts: apLanIpAddress.setDescription('This attribute indicates the IP address of the LAN interface.')
apLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanSubnetMask.setStatus('current')
if mibBuilder.loadTexts: apLanSubnetMask.setDescription('This attribute indicates the subnet mask of the LAN interface.')
apLanDhcpServer = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServer.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServer.setDescription('This attribute indicates the status of the LAN DHCP Server.')
apLanDhcpServerStartRange = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerStartRange.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerStartRange.setDescription('This attribute indicates the start range of the LAN DHCP Server.')
apLanDhcpServerStopRange = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerStopRange.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerStopRange.setDescription('This attribute indicates the stop range of the LAN DHCP Server.')
apLanDhcpServerSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerSubnetMask.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerSubnetMask.setDescription('This attribute indicates the subnet mask of the LAN DHCP Server.')
apLanDhcpServerBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerBroadcast.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerBroadcast.setDescription('This attribute indicates the broadcast address of the LAN DHCP Server.')
apLanDhcpServerGateway = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerGateway.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerGateway.setDescription('This attribute indicates the gateway of the LAN DHCP Server.')
apLanDhcpServerDns1 = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerDns1.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerDns1.setDescription('This attribute indicates the first DNS server of the LAN DHCP Server.')
apLanDhcpServerDns2 = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerDns2.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerDns2.setDescription('This attribute indicates the second DNS server of the LAN DHCP Server.')
apLanDhcpServerDns3 = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpServerDns3.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpServerDns3.setDescription('This attribute indicates the third DNS server of the LAN DHCP Server.')
apLanDhcpDomain = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: apLanDhcpDomain.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpDomain.setDescription('This attribute indicates the domain of the LAN DHCP Server.')
apLanDhcpRelease = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 9999999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanDhcpRelease.setStatus('current')
if mibBuilder.loadTexts: apLanDhcpRelease.setDescription('This attribute indicates the lease time of the LAN DHCP Server.')
apLanReservationTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14), )
if mibBuilder.loadTexts: apLanReservationTable.setStatus('current')
if mibBuilder.loadTexts: apLanReservationTable.setDescription('LAN Reservation Table.')
apLanReservationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1), ).setIndexNames((0, "AP-SYSTEM-NETWORK", "apLanReservationIndex"))
if mibBuilder.loadTexts: apLanReservationEntry.setStatus('current')
if mibBuilder.loadTexts: apLanReservationEntry.setDescription('An entry in the apLanReservationTable.')
apLanReservationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apLanReservationIndex.setStatus('current')
if mibBuilder.loadTexts: apLanReservationIndex.setDescription('This attribute indicates the LAN Reservation index')
apLanReservationRowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apLanReservationRowControl.setStatus('current')
if mibBuilder.loadTexts: apLanReservationRowControl.setDescription('The LAN Reservation status. Supported values: active(1) - valid entry notReady(3) - non-valid entry createAndGo(4) - used to create a new entry destroy(6) - removes the entry')
apLanReservationMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanReservationMacAddress.setStatus('current')
if mibBuilder.loadTexts: apLanReservationMacAddress.setDescription("This field indicates a MAC address entry in the LAN Reservation. Remarks: Input format: 0xXX 0xXX 0xXX 0xXX 0xXX 0xXX OR XX:XX:XX:XX:XX:XX OR XX-XX-XX-XX-XX-XX (examples: 0xab 0xcd 0xef 0x01 0x02 0x03 OR ab:cd:ef:01:02:03 OR ab-cd-ef-01-02-03) X: [0:9] or [a:f] or [A:F] *** Please don 't enter duplicate MAC address. ***")
apLanReservationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 2, 14, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apLanReservationIp.setStatus('current')
if mibBuilder.loadTexts: apLanReservationIp.setDescription('This field indicates a IP address entry in the LAN Reservation.')
apPppoeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3))
apPppoeUsername = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPppoeUsername.setStatus('current')
if mibBuilder.loadTexts: apPppoeUsername.setDescription('This attribute indicates the username of PPPoE.')
apPppoePassword = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPppoePassword.setStatus('current')
if mibBuilder.loadTexts: apPppoePassword.setDescription('This attribute indicates the password of PPPoE.')
apPppoeServiceName = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPppoeServiceName.setStatus('current')
if mibBuilder.loadTexts: apPppoeServiceName.setDescription('This attribute indicates the service name of PPPoE.')
apDmzConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 4))
apDmzStatus = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDmzStatus.setStatus('current')
if mibBuilder.loadTexts: apDmzStatus.setDescription('This attribute indicates the status of DMZ.')
apDmzIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apDmzIp.setStatus('current')
if mibBuilder.loadTexts: apDmzIp.setDescription('This attribute indicates the IP address of DMZ.')
apPortForwardTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5), )
if mibBuilder.loadTexts: apPortForwardTable.setStatus('current')
if mibBuilder.loadTexts: apPortForwardTable.setDescription('LAN Port Forward Table.')
apPortForwardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1), ).setIndexNames((0, "AP-SYSTEM-NETWORK", "apPortForwardIndex"))
if mibBuilder.loadTexts: apPortForwardEntry.setStatus('current')
if mibBuilder.loadTexts: apPortForwardEntry.setDescription('An entry in the apPortForwardTable.')
apPortForwardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apPortForwardIndex.setStatus('current')
if mibBuilder.loadTexts: apPortForwardIndex.setDescription('This attribute indicates the port forward index')
apPortForwardRowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apPortForwardRowControl.setStatus('current')
if mibBuilder.loadTexts: apPortForwardRowControl.setDescription('The port forward status. Supported values: active(1) - valid entry notReady(3) - non-valid entry createAndGo(4) - used to create a new entry destroy(6) - removes the entry')
apPortForwardName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPortForwardName.setStatus('current')
if mibBuilder.loadTexts: apPortForwardName.setDescription('This field indicates the name of port forward.')
apPortForwardToIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPortForwardToIp.setStatus('current')
if mibBuilder.loadTexts: apPortForwardToIp.setDescription('This field indicates the to IP address of port forward.')
apPortForwardPortProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("tcp", 0), ("udp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPortForwardPortProtocol.setStatus('current')
if mibBuilder.loadTexts: apPortForwardPortProtocol.setDescription('This field indicates the protocol of port forward.')
apPortForwardAppServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 80, 443, 143, 110, 3389, 25, 22, 23, 5190, 113, 1494, 53, 21, 389, 1352, 1434, 1433, 123, 1812, 1813, 554, 161, 162, 514, 33434))).clone(namedValues=NamedValues(("na", 0), ("http", 80), ("https", 443), ("iamp", 143), ("pop3", 110), ("rdp", 3389), ("smtp", 25), ("ssh", 22), ("telnet", 23), ("aol", 5190), ("auth", 113), ("citrix", 1494), ("dns", 53), ("ftp", 21), ("ldap", 389), ("loctusnotes", 1352), ("ms-sql-monitor", 1434), ("ms-sql-server", 1433), ("ntp", 123), ("radius", 1812), ("radius-acct", 1813), ("rtsp", 554), ("snmp", 161), ("snmp-trap", 162), ("syslog", 514), ("traceroute", 33434)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPortForwardAppServiceType.setStatus('current')
if mibBuilder.loadTexts: apPortForwardAppServiceType.setDescription('This field indicates the service type of port forward.')
apPortForwardPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("single-port", 0), ("port-range", 1), ("port-mapping", 2), ("range-mapping", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPortForwardPortType.setStatus('current')
if mibBuilder.loadTexts: apPortForwardPortType.setDescription('This field indicates the port type of port forward.')
apPortForwardFromPort = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPortForwardFromPort.setStatus('current')
if mibBuilder.loadTexts: apPortForwardFromPort.setDescription('This field indicates the from port of port forward.')
apPortForwardToPort = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 2, 2, 5, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apPortForwardToPort.setStatus('current')
if mibBuilder.loadTexts: apPortForwardToPort.setDescription('This field indicates the to port of port forward.')
mibBuilder.exportSymbols("AP-SYSTEM-NETWORK", apNetworkConfig=apNetworkConfig, apMib=apMib, productID=productID, apPppoeStatusMessage=apPppoeStatusMessage, apCurrentDns=apCurrentDns, apPortForwardEntry=apPortForwardEntry, apPppoeConfig=apPppoeConfig, PYSNMP_MODULE_ID=ap_system_network_mib, apPortForwardPortType=apPortForwardPortType, apGateway=apGateway, pepwave=pepwave, apPortForwardAppServiceType=apPortForwardAppServiceType, apLanDhcpServerDns3=apLanDhcpServerDns3, apLanReservationRowControl=apLanReservationRowControl, apDmzConfig=apDmzConfig, apLanDhcpServerStopRange=apLanDhcpServerStopRange, apPortForwardIndex=apPortForwardIndex, apIpAddress=apIpAddress, apCurrentIpAddressMode=apCurrentIpAddressMode, apLanDhcpDomain=apLanDhcpDomain, apPortForwardToIp=apPortForwardToIp, apDns=apDns, apLanReservationMacAddress=apLanReservationMacAddress, apPortForwardRowControl=apPortForwardRowControl, apPppoeServiceName=apPppoeServiceName, apPortForwardTable=apPortForwardTable, apLanReservationIp=apLanReservationIp, apLanDhcpServerDns2=apLanDhcpServerDns2, apGeneralMib=apGeneralMib, apLanDhcpServerSubnetMask=apLanDhcpServerSubnetMask, apPppoeStatus=apPppoeStatus, apLanDhcpServerBroadcast=apLanDhcpServerBroadcast, apWanConfig=apWanConfig, apPortForwardToPort=apPortForwardToPort, apDmzIp=apDmzIp, apLanSubnetMask=apLanSubnetMask, apSubnetMask=apSubnetMask, apLanIpAddress=apLanIpAddress, apLanConfig=apLanConfig, apCurrentIpAddress=apCurrentIpAddress, apNetworkInfo=apNetworkInfo, apLanDhcpServerStartRange=apLanDhcpServerStartRange, apLanDhcpServerGateway=apLanDhcpServerGateway, apLanReservationTable=apLanReservationTable, apPppoeUsername=apPppoeUsername, apPppoePassword=apPppoePassword, apWanInfo=apWanInfo, apPortForwardFromPort=apPortForwardFromPort, apCurrentGateway=apCurrentGateway, apLanDhcpServer=apLanDhcpServer, apLanReservationEntry=apLanReservationEntry, apPortForwardPortProtocol=apPortForwardPortProtocol, ap_system_network_mib=ap_system_network_mib, apIpAddressMode=apIpAddressMode, apPortForwardName=apPortForwardName, apLanReservationIndex=apLanReservationIndex, apPppoeInfo=apPppoeInfo, apLanDhcpRelease=apLanDhcpRelease, apDmzStatus=apDmzStatus, apKeepDefaultIp=apKeepDefaultIp, apLanDhcpServerDns1=apLanDhcpServerDns1, apCurrentSubnetMask=apCurrentSubnetMask)
