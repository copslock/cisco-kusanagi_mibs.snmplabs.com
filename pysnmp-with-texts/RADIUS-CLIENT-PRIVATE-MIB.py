#
# PySNMP MIB module RADIUS-CLIENT-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADIUS-CLIENT-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:44:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, NotificationType, Gauge32, iso, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, TimeTicks, IpAddress, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "NotificationType", "Gauge32", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "TimeTicks", "IpAddress", "Counter32", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
radius = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 8))
if mibBuilder.loadTexts: radius.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: radius.setOrganization('Quanta Computer Inc.')
if mibBuilder.loadTexts: radius.setContactInfo(' Customer Support Postal: Quanta Computer Inc. 4, Wen Ming 1 St., Kuei Shan Hsiang, Tao Yuan Shien, Taiwan, R.O.C. Tel: +886 3 328 0050 E-Mail: strong.chen@quantatw.com')
if mibBuilder.loadTexts: radius.setDescription('The QCI Private MIB for Radius Authentication Client')
agentRadiusConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1))
agentRadiusMaxTransmit = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusMaxTransmit.setStatus('current')
if mibBuilder.loadTexts: agentRadiusMaxTransmit.setDescription('Maximum number of retransmissions of a RADIUS request packet')
agentRadiusTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusTimeout.setStatus('current')
if mibBuilder.loadTexts: agentRadiusTimeout.setDescription('Time out duration (in seconds) before packets are retransmitted')
agentRadiusAccountingMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingMode.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingMode.setDescription('Identifies if RADIUS Accounting has been enabled or not')
agentRadiusStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusStatsClear.setStatus('current')
if mibBuilder.loadTexts: agentRadiusStatsClear.setDescription('When set to enable(1), all Radius statistics will be reset.')
agentRadiusAccountingIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAccountingIndexNextValid.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingIndexNextValid.setDescription('Indicates the next valid index into the agentRadiusAccountingConfigTable for creation. If no additional entries are allowed, this will be 0.')
agentRadiusAccountingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6), )
if mibBuilder.loadTexts: agentRadiusAccountingConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingConfigTable.setDescription('Table with information about Radius Accounting Server IP Addresses, port numbers and shared secret. Only one entry is supported at this time.')
agentRadiusAccountingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1), ).setIndexNames((0, "RADIUS-CLIENT-PRIVATE-MIB", "agentRadiusAccountingServerIndex"))
if mibBuilder.loadTexts: agentRadiusAccountingConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingConfigEntry.setDescription('Entry consisting of configuration data for a Radius Accounting Server.')
agentRadiusAccountingServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusAccountingServerIndex.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingServerIndex.setDescription('Unique index of the configured RADIUS accounting server. The next valid value of this object for creation is specified by agentRadiusAccountingIndexNextValid. ')
agentRadiusAccountingServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerAddress.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingServerAddress.setDescription('IP Address of the configured RADIUS accounting server. This object cannot be changed after creation.')
agentRadiusAccountingServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerAddressType.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingServerAddressType.setDescription('IP Address Type of the configured RADIUS accounting server. This object cannot be changed after creation.')
agentRadiusAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1813)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingPort.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingPort.setDescription('Port number for the RADIUS accounting server.')
agentRadiusAccountingSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingSecret.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingSecret.setDescription('Configured shared sercret for the RADIUS accounting server.')
agentRadiusAccountingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingStatus.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingStatus.setDescription('Creates or destroys a RADIUS accounting server entry. During creation, the next available index is specified by the agentRadiusAccountingIndexNextValid object. Rows creation using a different value for agentRadiusAccountingServerIndex will fail. active(1) - This entry is active. createAndGo(4) - Creates a new entry. destroy(6) - Deletes an entry.')
agentRadiusAccountingServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerName.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingServerName.setDescription('Configured identification name for the RADIUS Accounting server.')
agentRadiusServerIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerIndexNextValid.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerIndexNextValid.setDescription('Indicates the next valid index into the agentRadiusServerConfigTable for creation. If no additional entries are allowed, this will be 0.')
agentRadiusServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8), )
if mibBuilder.loadTexts: agentRadiusServerConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerConfigTable.setDescription('Table with information about Radius Authentication Server IP Addresses, port numbers and shared secret')
agentRadiusServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1), ).setIndexNames((0, "RADIUS-CLIENT-PRIVATE-MIB", "agentRadiusServerIndex"))
if mibBuilder.loadTexts: agentRadiusServerConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerConfigEntry.setDescription('Entry consisting of configuration data for a Radius Authentication Server.')
agentRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusServerIndex.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerIndex.setDescription('Unique index of the configured RADIUS server')
agentRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerAddress.setStatus('obsolete')
if mibBuilder.loadTexts: agentRadiusServerAddress.setDescription('IP Address of the configured RADIUS server. This object cannot be changed after creation.')
agentRadiusServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerAddressType.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerAddressType.setDescription('IP Address Type of the configured RADIUS server. This object cannot be changed after creation.')
agentRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPort.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerPort.setDescription('Port number for the RADIUS server.')
agentRadiusServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerSecret.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerSecret.setDescription('Configured shared sercret for the RADIUS server.')
agentRadiusServerPrimaryMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPrimaryMode.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerPrimaryMode.setDescription('Configure the RADIUS server to be the primary server. If there is any other server that is configured to be primary, that server is set to be a seconday server and this entry is set Primary.')
agentRadiusServerCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerCurrentMode.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerCurrentMode.setDescription('Indicate if the RADIUS server is the current server in user for authentication.')
agentRadiusServerMsgAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerMsgAuth.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerMsgAuth.setDescription('Enable or disable the message authenticator attribute for this RADIUS server.')
agentRadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerRowStatus.setDescription('Creates or destroys a RADIUS Authentication server entry. During creation, the next available index is specified by the agentRadiusServerIndexNextValid object. Rows creation using a different value for agentRadiusServerIndex will fail. active(1) - This entry is active. createAndGo(4) - Creates a new entry. destroy(6) - Deletes an entry.')
agentRadiusServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerName.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerName.setDescription('Configured identification name for the RADIUS server.')
agentRadiusServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 11), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerInetAddress.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerInetAddress.setDescription('IP Address of the configured RADIUS server. This object cannot be changed after creation.')
agentRadiusServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerTimeout.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerTimeout.setDescription('Time out duration (in seconds) before packets are retransmitted')
agentRadiusServerRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerRetransmit.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerRetransmit.setDescription('Maximum number of retransmissions of a RADIUS request packet')
agentRadiusServerDeadtime = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerDeadtime.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerDeadtime.setDescription('Length of time (in minutes) for which a RADIUS server is skipped over by transaction requests.')
agentRadiusServerSourceIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerSourceIPAddr.setStatus('obsolete')
if mibBuilder.loadTexts: agentRadiusServerSourceIPAddr.setDescription('Source IP address that will be used for the communication with RADIUS servers.')
agentRadiusServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPriority.setStatus('obsolete')
if mibBuilder.loadTexts: agentRadiusServerPriority.setDescription('Priority specifies the order in which the servers will be used, where 0 is the highest priority in radius server config mode.')
agentRadiusServerUsageType = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("login", 2), ("dot1x", 3))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerUsageType.setStatus('obsolete')
if mibBuilder.loadTexts: agentRadiusServerUsageType.setDescription('Specify the usage type of the server.')
agentRadiusAuthenticationServers = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAuthenticationServers.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAuthenticationServers.setDescription('Number of RADIUS Authentication Servers that have been configured.')
agentRadiusAccountingServers = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAccountingServers.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingServers.setDescription('Number of RADIUS Accounting Servers that have been configured.')
agentRadiusNamedAuthenticationServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusNamedAuthenticationServerGroups.setStatus('current')
if mibBuilder.loadTexts: agentRadiusNamedAuthenticationServerGroups.setDescription('Number of configured RADIUS named Authentication Server groups.')
agentRadiusNamedAccountingServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusNamedAccountingServerGroups.setStatus('current')
if mibBuilder.loadTexts: agentRadiusNamedAccountingServerGroups.setDescription('Number of configured RADIUS named Accounting Server groups.')
agentRadiusDeadTime = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusDeadTime.setStatus('current')
if mibBuilder.loadTexts: agentRadiusDeadTime.setDescription('Length of time (in minutes) for which a RADIUS server is skipped over by transaction requests.')
agentRadiusServerKey = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerKey.setStatus('obsolete')
if mibBuilder.loadTexts: agentRadiusServerKey.setDescription('RADIUS Server key specifies the authentication and encryption key for all RADIUS communications between the switch and the RADIUS server. This key must match the encryption used on the RADIUS daemon.')
agentRadiusSourceIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusSourceIPAddr.setStatus('obsolete')
if mibBuilder.loadTexts: agentRadiusSourceIPAddr.setDescription('Source IP address that will be used for the communication with RADIUS servers.')
agentRadiusNasIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusNasIpAddress.setStatus('current')
if mibBuilder.loadTexts: agentRadiusNasIpAddress.setDescription('Used to set the NAS-IP address for the radius server. A value of 0.0.0.0 will disable radius attribute 4 mode.')
agentAuthorizationNetworkRadiusMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAuthorizationNetworkRadiusMode.setStatus('current')
if mibBuilder.loadTexts: agentAuthorizationNetworkRadiusMode.setDescription('Used to enable/disable Vlan assignment mode.')
agentRadiusNasIpv6Address = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 18), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusNasIpv6Address.setStatus('current')
if mibBuilder.loadTexts: agentRadiusNasIpv6Address.setDescription('Used to set the NAS-IPv6 address for the radius server. A value of :: will disable radius attribute 95 mode.')
agentRadiusSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 8, 1, 19), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusSourceInterface.setStatus('current')
if mibBuilder.loadTexts: agentRadiusSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates the source-interface un-selection.')
mibBuilder.exportSymbols("RADIUS-CLIENT-PRIVATE-MIB", agentRadiusAccountingServerIndex=agentRadiusAccountingServerIndex, agentRadiusAccountingServerAddress=agentRadiusAccountingServerAddress, agentRadiusServerAddress=agentRadiusServerAddress, agentRadiusServerSourceIPAddr=agentRadiusServerSourceIPAddr, agentRadiusServerSecret=agentRadiusServerSecret, agentRadiusSourceIPAddr=agentRadiusSourceIPAddr, agentRadiusNamedAccountingServerGroups=agentRadiusNamedAccountingServerGroups, agentRadiusAccountingStatus=agentRadiusAccountingStatus, agentRadiusServerMsgAuth=agentRadiusServerMsgAuth, agentRadiusAccountingConfigEntry=agentRadiusAccountingConfigEntry, agentRadiusAccountingSecret=agentRadiusAccountingSecret, agentRadiusServerRowStatus=agentRadiusServerRowStatus, radius=radius, agentRadiusAccountingMode=agentRadiusAccountingMode, agentRadiusStatsClear=agentRadiusStatsClear, agentRadiusServerUsageType=agentRadiusServerUsageType, agentRadiusServerCurrentMode=agentRadiusServerCurrentMode, agentRadiusServerConfigTable=agentRadiusServerConfigTable, agentRadiusAccountingIndexNextValid=agentRadiusAccountingIndexNextValid, agentRadiusAuthenticationServers=agentRadiusAuthenticationServers, agentRadiusAccountingServers=agentRadiusAccountingServers, agentRadiusTimeout=agentRadiusTimeout, agentRadiusServerAddressType=agentRadiusServerAddressType, agentRadiusNamedAuthenticationServerGroups=agentRadiusNamedAuthenticationServerGroups, agentRadiusServerTimeout=agentRadiusServerTimeout, agentRadiusSourceInterface=agentRadiusSourceInterface, agentRadiusServerIndex=agentRadiusServerIndex, agentRadiusNasIpAddress=agentRadiusNasIpAddress, agentRadiusNasIpv6Address=agentRadiusNasIpv6Address, agentRadiusServerPrimaryMode=agentRadiusServerPrimaryMode, agentRadiusAccountingConfigTable=agentRadiusAccountingConfigTable, agentRadiusConfigGroup=agentRadiusConfigGroup, agentRadiusDeadTime=agentRadiusDeadTime, agentRadiusServerPriority=agentRadiusServerPriority, agentRadiusAccountingPort=agentRadiusAccountingPort, agentRadiusServerKey=agentRadiusServerKey, agentRadiusServerIndexNextValid=agentRadiusServerIndexNextValid, agentRadiusMaxTransmit=agentRadiusMaxTransmit, agentRadiusServerName=agentRadiusServerName, agentRadiusServerDeadtime=agentRadiusServerDeadtime, PYSNMP_MODULE_ID=radius, agentRadiusServerInetAddress=agentRadiusServerInetAddress, agentAuthorizationNetworkRadiusMode=agentAuthorizationNetworkRadiusMode, agentRadiusAccountingServerAddressType=agentRadiusAccountingServerAddressType, agentRadiusServerConfigEntry=agentRadiusServerConfigEntry, agentRadiusServerRetransmit=agentRadiusServerRetransmit, agentRadiusServerPort=agentRadiusServerPort, agentRadiusAccountingServerName=agentRadiusAccountingServerName)
