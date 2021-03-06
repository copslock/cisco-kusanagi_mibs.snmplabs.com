#
# PySNMP MIB module HM2-PLATFORM-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-RADIUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:32:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
HmEnabledStatus, hm2PlatformMibs = mibBuilder.importSymbols("HM2-TC-MIB", "HmEnabledStatus", "hm2PlatformMibs")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, MibIdentifier, Gauge32, ModuleIdentity, Integer32, Counter64, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "MibIdentifier", "Gauge32", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hm2PlatformRadius = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 8))
hm2PlatformRadius.setRevisions(('2013-06-05 00:00', '2013-03-01 00:00', '2011-06-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2PlatformRadius.setRevisionsDescriptions(('Range of hm2AgentRadiusServerRetransmit adjusted. Behavior of hm2AgentRadiusServerTimeout, hm2AgentRadiusServerRetransmit, hm2AgentRadiusServerDeadtime and hm2AgentRadiusServerSourceIPAddr clarified.', 'Shared secret key length updated. Radius source interface related object added.', 'Initial version.',))
if mibBuilder.loadTexts: hm2PlatformRadius.setLastUpdated('201306050000Z')
if mibBuilder.loadTexts: hm2PlatformRadius.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2PlatformRadius.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2PlatformRadius.setDescription('The Hirschmann Private Platform2 MIB for Client Radius Authentication and Accounting. Copyright (C) 2011-2013. All Rights Reserved.')
hm2AgentRadiusConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 8, 1))
hm2AgentRadiusMaxTransmit = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusMaxTransmit.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusMaxTransmit.setDescription('Maximum number of retransmissions of a RADIUS request packet')
hm2AgentRadiusTimeout = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusTimeout.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusTimeout.setDescription('Time out duration (in seconds) before packets are retransmitted.')
hm2AgentRadiusAccountingMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 3), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingMode.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingMode.setDescription('Identifies if RADIUS accounting has been enabled or not.')
hm2AgentRadiusStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 4), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusStatsClear.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusStatsClear.setDescription('When set to enable(1), all RADIUS statistics will be reset.')
hm2AgentRadiusAccountingIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingIndexNextValid.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingIndexNextValid.setDescription('Indicates the next valid index into the hm2AgentRadiusAccountingConfigTable for creation. If no additional entries are allowed, this will be 0.')
hm2AgentRadiusAccountingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6), )
if mibBuilder.loadTexts: hm2AgentRadiusAccountingConfigTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingConfigTable.setDescription('Table with information about RADIUS accounting server IP addresses, port numbers and shared secrets. Only one entry is supported at this time.')
hm2AgentRadiusAccountingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1), ).setIndexNames((0, "HM2-PLATFORM-RADIUS-MIB", "hm2AgentRadiusAccountingServerIndex"))
if mibBuilder.loadTexts: hm2AgentRadiusAccountingConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingConfigEntry.setDescription('Entry consisting of configuration data for a RADIUS accounting server.')
hm2AgentRadiusAccountingServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerIndex.setDescription('Unique index of the configured RADIUS accounting server. The next valid value of this object for creation is specified by hm2AgentRadiusAccountingIndexNextValid.')
hm2AgentRadiusAccountingServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddress.setStatus('deprecated')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddress.setDescription('This object is deprecated in favour of hm2AgentRadiusAccountingServerAddr. IP Address of the configured RADIUS accounting server. This object cannot be changed after creation.')
hm2AgentRadiusAccountingServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddressType.setStatus('deprecated')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddressType.setDescription('This object is deprecated in favour of hm2AgentRadiusAccountingServerAddrType. IP Address Type of the configured RADIUS accounting server. This object cannot be changed after creation.')
hm2AgentRadiusAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1813)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingPort.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingPort.setDescription('Port number for the RADIUS accounting server.')
hm2AgentRadiusAccountingSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 5), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 64), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingSecret.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingSecret.setDescription('Configured shared sercret for the RADIUS accounting server.')
hm2AgentRadiusAccountingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingStatus.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingStatus.setDescription('Creates or destroys a RADIUS accounting server entry. During creation, the next available index is specified by the hm2AgentRadiusAccountingIndexNextValid object. Rows creation using a different value for hm2AgentRadiusAccountingServerIndex will fail. active(1) - This entry is active. notInService(2) - This entry is administratively disabled. notReady(3) - DNS resolution of host name has failed. createAndGo(4) - Creates a new entry. createAndWait(5)- Creates a new entry. destroy(6) - Deletes an entry.')
hm2AgentRadiusAccountingServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerName.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerName.setDescription('Configured identification name for the RADIUS accounting server.')
hm2AgentRadiusAccountingServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 248), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddrType.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddrType.setDescription('Inet address type of the configured RADIUS accounting server. This object cannot be changed after creation.')
hm2AgentRadiusAccountingServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 249), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddr.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddr.setDescription('Inet address of the configured RADIUS accounting server. This object cannot be changed after creation.')
hm2AgentRadiusServerIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusServerIndexNextValid.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerIndexNextValid.setDescription('Indicates the next valid index into the hm2AgentRadiusServerConfigTable for creation. If no additional entries are allowed, this will be 0.')
hm2AgentRadiusServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8), )
if mibBuilder.loadTexts: hm2AgentRadiusServerConfigTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerConfigTable.setDescription('Table with information about RADIUS authentication server IP addresses, port numbers and shared secrets.')
hm2AgentRadiusServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1), ).setIndexNames((0, "HM2-PLATFORM-RADIUS-MIB", "hm2AgentRadiusServerIndex"))
if mibBuilder.loadTexts: hm2AgentRadiusServerConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerConfigEntry.setDescription('Entry consisting of configuration data for a RADIUS authentication server.')
hm2AgentRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hm2AgentRadiusServerIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerIndex.setDescription('Unique index of the configured RADIUS server')
hm2AgentRadiusServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerAddressType.setStatus('deprecated')
if mibBuilder.loadTexts: hm2AgentRadiusServerAddressType.setDescription('This object is deprecated in favour of hm2AgentRadiusServerInetAddrType. IP Address Type of the configured RADIUS server. This object cannot be changed after creation.')
hm2AgentRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerPort.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerPort.setDescription('Port number for the RADIUS server.')
hm2AgentRadiusServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 5), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 64), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerSecret.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerSecret.setDescription('Configured shared sercret for the RADIUS server.')
hm2AgentRadiusServerPrimaryMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 6), HmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerPrimaryMode.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerPrimaryMode.setDescription('Configure the RADIUS server to be the primary server. If there is any other server that is configured to be primary, that server is set to be a seconday server and this entry is set primary.')
hm2AgentRadiusServerCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusServerCurrentMode.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerCurrentMode.setDescription('Indicate if the RADIUS server is the current server in use for authentication.')
hm2AgentRadiusServerMsgAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 8), HmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerMsgAuth.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerMsgAuth.setDescription('Enable or disable the message authenticator attribute for this RADIUS server.')
hm2AgentRadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerRowStatus.setDescription('Creates or destroys a RADIUS authentication server entry. During creation, the next available index is specified by the hm2AgentRadiusServerIndexNextValid object. Rows creation using a different value for hm2AgentRadiusServerIndex will fail. active(1) - This entry is active. notInService(2) - This entry is administratively disabled. notReady(3) - DNS resolution of host name has failed. createAndGo(4) - Creates a new entry. createAndWait(5)- Creates a new entry. destroy(6) - Deletes an entry.')
hm2AgentRadiusServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerName.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerName.setDescription('Configured identification name for the RADIUS server.')
hm2AgentRadiusServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 11), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddress.setStatus('deprecated')
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddress.setDescription('This object is deprecated in favour of hm2AgentRadiusServerInetAddr. IP Address of the configured RADIUS server. This object cannot be changed after creation.')
hm2AgentRadiusServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerTimeout.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerTimeout.setDescription('Time out duration (in seconds) before packets are retransmitted. Note that hm2AgentRadiusTimeout will override this MIB object: - During row creation, hm2AgentRadiusTimeout specifies the default value. - Writing to hm2AgentRadiusTimeout will also update the value of this MIB object for all existing rows.')
hm2AgentRadiusServerRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerRetransmit.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerRetransmit.setDescription('Maximum number of retransmissions of a RADIUS request packet Note that hm2AgentRadiusMaxTransmit will override this MIB object: - During row creation, hm2AgentRadiusMaxTransmit specifies the default value. - Writing to hm2AgentRadiusMaxTransmit will also update the value of this MIB object for all existing rows.')
hm2AgentRadiusServerDeadtime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerDeadtime.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerDeadtime.setDescription('Length of time (in minutes) for which a RADIUS server is skipped over by transaction requests. Note that hm2AgentRadiusDeadTime will override this MIB object: - During row creation, hm2AgentRadiusDeadTime specifies the default value. - Writing to hm2AgentRadiusDeadTime will also update the value of this MIB object for all existing rows.')
hm2AgentRadiusServerSourceIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerSourceIPAddr.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerSourceIPAddr.setDescription('Source IP address that will be used for the communication with RADIUS servers. Note that hm2AgentRadiusSourceIPAddr will override this MIB object: - During row creation, hm2AgentRadiusSourceIPAddr specifies the default value. - Writing to hm2AgentRadiusSourceIPAddr will also update the value of this MIB object for all existing rows.')
hm2AgentRadiusServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerPriority.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerPriority.setDescription('Priority specifies the order in which the servers will be used, where 0 is the highest priority in radius server config mode.')
hm2AgentRadiusServerUsageType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("login", 2), ("dot1x", 3))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerUsageType.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerUsageType.setDescription('Specify the usage type of the server.')
hm2AgentRadiusServerInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 248), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddrType.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddrType.setDescription('Inet address type of the configured RADIUS server. This object cannot be changed after creation.')
hm2AgentRadiusServerInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 249), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddr.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddr.setDescription('Inet address of the configured RADIUS server. This object cannot be changed after creation.')
hm2AgentRadiusAuthenticationServers = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusAuthenticationServers.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAuthenticationServers.setDescription('Number of RADIUS authentication servers that have been configured.')
hm2AgentRadiusAccountingServers = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServers.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServers.setDescription('Number of RADIUS accounting servers that have been configured.')
hm2AgentRadiusNamedAuthenticationServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusNamedAuthenticationServerGroups.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusNamedAuthenticationServerGroups.setDescription('Number of configured RADIUS named authentication server groups.')
hm2AgentRadiusNamedAccountingServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusNamedAccountingServerGroups.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusNamedAccountingServerGroups.setDescription('Number of configured RADIUS named accounting server groups.')
hm2AgentRadiusDeadTime = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusDeadTime.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusDeadTime.setDescription('Length of time (in minutes) for which a RADIUS server is skipped over by transaction requests.')
hm2AgentRadiusSourceIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 15), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusSourceIPAddr.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusSourceIPAddr.setDescription('Source IP address that will be used for the communication with RADIUS servers.')
hm2AgentRadiusNasIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 16), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusNasIpAddress.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusNasIpAddress.setDescription('Used to set the NAS-IP address for the radius server.')
hm2AgentAuthorizationNetworkRadiusMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 17), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentAuthorizationNetworkRadiusMode.setStatus('current')
if mibBuilder.loadTexts: hm2AgentAuthorizationNetworkRadiusMode.setDescription('Used to enable/disable VLAN assignment mode.')
hm2AgentRadiusSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 18), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusSourceInterface.setStatus('current')
if mibBuilder.loadTexts: hm2AgentRadiusSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates the source-interface un-selection. The frames will not necessarily be sent on this interface, only the IP address of the interface will be used as source.')
mibBuilder.exportSymbols("HM2-PLATFORM-RADIUS-MIB", hm2AgentRadiusDeadTime=hm2AgentRadiusDeadTime, hm2AgentRadiusAccountingConfigEntry=hm2AgentRadiusAccountingConfigEntry, hm2AgentRadiusAccountingServerName=hm2AgentRadiusAccountingServerName, hm2AgentRadiusServerConfigEntry=hm2AgentRadiusServerConfigEntry, hm2AgentRadiusAccountingConfigTable=hm2AgentRadiusAccountingConfigTable, hm2AgentRadiusAccountingServers=hm2AgentRadiusAccountingServers, hm2AgentRadiusServerSecret=hm2AgentRadiusServerSecret, hm2AgentRadiusServerDeadtime=hm2AgentRadiusServerDeadtime, hm2AgentRadiusAccountingServerAddrType=hm2AgentRadiusAccountingServerAddrType, hm2AgentRadiusServerIndexNextValid=hm2AgentRadiusServerIndexNextValid, hm2AgentRadiusAccountingMode=hm2AgentRadiusAccountingMode, hm2AgentRadiusServerIndex=hm2AgentRadiusServerIndex, hm2AgentRadiusServerPrimaryMode=hm2AgentRadiusServerPrimaryMode, hm2AgentRadiusServerRowStatus=hm2AgentRadiusServerRowStatus, hm2AgentRadiusServerInetAddr=hm2AgentRadiusServerInetAddr, hm2AgentRadiusNasIpAddress=hm2AgentRadiusNasIpAddress, hm2AgentRadiusAccountingServerAddressType=hm2AgentRadiusAccountingServerAddressType, hm2AgentRadiusAuthenticationServers=hm2AgentRadiusAuthenticationServers, hm2AgentRadiusTimeout=hm2AgentRadiusTimeout, hm2AgentRadiusMaxTransmit=hm2AgentRadiusMaxTransmit, hm2PlatformRadius=hm2PlatformRadius, hm2AgentRadiusServerSourceIPAddr=hm2AgentRadiusServerSourceIPAddr, hm2AgentRadiusServerConfigTable=hm2AgentRadiusServerConfigTable, hm2AgentRadiusServerPort=hm2AgentRadiusServerPort, hm2AgentRadiusServerName=hm2AgentRadiusServerName, hm2AgentRadiusServerUsageType=hm2AgentRadiusServerUsageType, hm2AgentRadiusNamedAuthenticationServerGroups=hm2AgentRadiusNamedAuthenticationServerGroups, hm2AgentAuthorizationNetworkRadiusMode=hm2AgentAuthorizationNetworkRadiusMode, hm2AgentRadiusServerTimeout=hm2AgentRadiusServerTimeout, hm2AgentRadiusServerInetAddress=hm2AgentRadiusServerInetAddress, hm2AgentRadiusConfigGroup=hm2AgentRadiusConfigGroup, hm2AgentRadiusSourceIPAddr=hm2AgentRadiusSourceIPAddr, hm2AgentRadiusAccountingServerAddr=hm2AgentRadiusAccountingServerAddr, hm2AgentRadiusServerRetransmit=hm2AgentRadiusServerRetransmit, hm2AgentRadiusAccountingServerIndex=hm2AgentRadiusAccountingServerIndex, hm2AgentRadiusAccountingServerAddress=hm2AgentRadiusAccountingServerAddress, hm2AgentRadiusNamedAccountingServerGroups=hm2AgentRadiusNamedAccountingServerGroups, hm2AgentRadiusAccountingStatus=hm2AgentRadiusAccountingStatus, hm2AgentRadiusServerInetAddrType=hm2AgentRadiusServerInetAddrType, hm2AgentRadiusServerMsgAuth=hm2AgentRadiusServerMsgAuth, hm2AgentRadiusStatsClear=hm2AgentRadiusStatsClear, hm2AgentRadiusServerPriority=hm2AgentRadiusServerPriority, hm2AgentRadiusServerAddressType=hm2AgentRadiusServerAddressType, PYSNMP_MODULE_ID=hm2PlatformRadius, hm2AgentRadiusAccountingIndexNextValid=hm2AgentRadiusAccountingIndexNextValid, hm2AgentRadiusSourceInterface=hm2AgentRadiusSourceInterface, hm2AgentRadiusAccountingPort=hm2AgentRadiusAccountingPort, hm2AgentRadiusAccountingSecret=hm2AgentRadiusAccountingSecret, hm2AgentRadiusServerCurrentMode=hm2AgentRadiusServerCurrentMode)
