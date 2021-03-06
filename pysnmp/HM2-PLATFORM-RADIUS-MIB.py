#
# PySNMP MIB module HM2-PLATFORM-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-RADIUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hm2PlatformMibs, HmEnabledStatus = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs", "HmEnabledStatus")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, Counter64, Unsigned32, Gauge32, ModuleIdentity, Counter32, iso, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Counter64", "Unsigned32", "Gauge32", "ModuleIdentity", "Counter32", "iso", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "NotificationType")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hm2PlatformRadius = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 8))
hm2PlatformRadius.setRevisions(('2013-06-05 00:00', '2013-03-01 00:00', '2011-06-21 00:00',))
if mibBuilder.loadTexts: hm2PlatformRadius.setLastUpdated('201306050000Z')
if mibBuilder.loadTexts: hm2PlatformRadius.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentRadiusConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 8, 1))
hm2AgentRadiusMaxTransmit = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusMaxTransmit.setStatus('current')
hm2AgentRadiusTimeout = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusTimeout.setStatus('current')
hm2AgentRadiusAccountingMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 3), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingMode.setStatus('current')
hm2AgentRadiusStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 4), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusStatsClear.setStatus('current')
hm2AgentRadiusAccountingIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingIndexNextValid.setStatus('current')
hm2AgentRadiusAccountingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6), )
if mibBuilder.loadTexts: hm2AgentRadiusAccountingConfigTable.setStatus('current')
hm2AgentRadiusAccountingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1), ).setIndexNames((0, "HM2-PLATFORM-RADIUS-MIB", "hm2AgentRadiusAccountingServerIndex"))
if mibBuilder.loadTexts: hm2AgentRadiusAccountingConfigEntry.setStatus('current')
hm2AgentRadiusAccountingServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerIndex.setStatus('current')
hm2AgentRadiusAccountingServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddress.setStatus('deprecated')
hm2AgentRadiusAccountingServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddressType.setStatus('deprecated')
hm2AgentRadiusAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1813)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingPort.setStatus('current')
hm2AgentRadiusAccountingSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 5), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 64), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingSecret.setStatus('current')
hm2AgentRadiusAccountingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingStatus.setStatus('current')
hm2AgentRadiusAccountingServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerName.setStatus('current')
hm2AgentRadiusAccountingServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 248), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddrType.setStatus('current')
hm2AgentRadiusAccountingServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 249), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServerAddr.setStatus('current')
hm2AgentRadiusServerIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusServerIndexNextValid.setStatus('current')
hm2AgentRadiusServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8), )
if mibBuilder.loadTexts: hm2AgentRadiusServerConfigTable.setStatus('current')
hm2AgentRadiusServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1), ).setIndexNames((0, "HM2-PLATFORM-RADIUS-MIB", "hm2AgentRadiusServerIndex"))
if mibBuilder.loadTexts: hm2AgentRadiusServerConfigEntry.setStatus('current')
hm2AgentRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hm2AgentRadiusServerIndex.setStatus('current')
hm2AgentRadiusServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerAddressType.setStatus('deprecated')
hm2AgentRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerPort.setStatus('current')
hm2AgentRadiusServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 5), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 64), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerSecret.setStatus('current')
hm2AgentRadiusServerPrimaryMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 6), HmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerPrimaryMode.setStatus('current')
hm2AgentRadiusServerCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusServerCurrentMode.setStatus('current')
hm2AgentRadiusServerMsgAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 8), HmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerMsgAuth.setStatus('current')
hm2AgentRadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerRowStatus.setStatus('current')
hm2AgentRadiusServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerName.setStatus('current')
hm2AgentRadiusServerInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 11), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddress.setStatus('deprecated')
hm2AgentRadiusServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerTimeout.setStatus('current')
hm2AgentRadiusServerRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerRetransmit.setStatus('current')
hm2AgentRadiusServerDeadtime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerDeadtime.setStatus('current')
hm2AgentRadiusServerSourceIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerSourceIPAddr.setStatus('current')
hm2AgentRadiusServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerPriority.setStatus('current')
hm2AgentRadiusServerUsageType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("login", 2), ("dot1x", 3))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusServerUsageType.setStatus('current')
hm2AgentRadiusServerInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 248), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddrType.setStatus('current')
hm2AgentRadiusServerInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 249), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentRadiusServerInetAddr.setStatus('current')
hm2AgentRadiusAuthenticationServers = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusAuthenticationServers.setStatus('current')
hm2AgentRadiusAccountingServers = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusAccountingServers.setStatus('current')
hm2AgentRadiusNamedAuthenticationServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusNamedAuthenticationServerGroups.setStatus('current')
hm2AgentRadiusNamedAccountingServerGroups = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentRadiusNamedAccountingServerGroups.setStatus('current')
hm2AgentRadiusDeadTime = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusDeadTime.setStatus('current')
hm2AgentRadiusSourceIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 15), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusSourceIPAddr.setStatus('current')
hm2AgentRadiusNasIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 16), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusNasIpAddress.setStatus('current')
hm2AgentAuthorizationNetworkRadiusMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 17), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentAuthorizationNetworkRadiusMode.setStatus('current')
hm2AgentRadiusSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 18), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentRadiusSourceInterface.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-RADIUS-MIB", hm2AgentRadiusServerIndexNextValid=hm2AgentRadiusServerIndexNextValid, hm2AgentRadiusAccountingConfigEntry=hm2AgentRadiusAccountingConfigEntry, hm2AgentRadiusServerDeadtime=hm2AgentRadiusServerDeadtime, hm2AgentRadiusNamedAuthenticationServerGroups=hm2AgentRadiusNamedAuthenticationServerGroups, hm2AgentRadiusAuthenticationServers=hm2AgentRadiusAuthenticationServers, hm2AgentRadiusAccountingServerAddressType=hm2AgentRadiusAccountingServerAddressType, hm2AgentRadiusServerPort=hm2AgentRadiusServerPort, hm2AgentRadiusServerName=hm2AgentRadiusServerName, hm2AgentRadiusSourceIPAddr=hm2AgentRadiusSourceIPAddr, hm2AgentRadiusConfigGroup=hm2AgentRadiusConfigGroup, PYSNMP_MODULE_ID=hm2PlatformRadius, hm2AgentRadiusServerRetransmit=hm2AgentRadiusServerRetransmit, hm2AgentRadiusServerSourceIPAddr=hm2AgentRadiusServerSourceIPAddr, hm2AgentRadiusServerIndex=hm2AgentRadiusServerIndex, hm2AgentRadiusServerInetAddress=hm2AgentRadiusServerInetAddress, hm2AgentRadiusAccountingServerIndex=hm2AgentRadiusAccountingServerIndex, hm2AgentRadiusAccountingServerAddress=hm2AgentRadiusAccountingServerAddress, hm2AgentRadiusServerPriority=hm2AgentRadiusServerPriority, hm2AgentRadiusServerTimeout=hm2AgentRadiusServerTimeout, hm2AgentRadiusStatsClear=hm2AgentRadiusStatsClear, hm2AgentRadiusAccountingSecret=hm2AgentRadiusAccountingSecret, hm2AgentRadiusSourceInterface=hm2AgentRadiusSourceInterface, hm2AgentRadiusServerMsgAuth=hm2AgentRadiusServerMsgAuth, hm2AgentRadiusServerRowStatus=hm2AgentRadiusServerRowStatus, hm2AgentRadiusAccountingServerName=hm2AgentRadiusAccountingServerName, hm2AgentRadiusMaxTransmit=hm2AgentRadiusMaxTransmit, hm2AgentRadiusAccountingPort=hm2AgentRadiusAccountingPort, hm2AgentRadiusServerPrimaryMode=hm2AgentRadiusServerPrimaryMode, hm2AgentRadiusAccountingServerAddrType=hm2AgentRadiusAccountingServerAddrType, hm2AgentRadiusServerSecret=hm2AgentRadiusServerSecret, hm2AgentRadiusServerUsageType=hm2AgentRadiusServerUsageType, hm2AgentRadiusAccountingIndexNextValid=hm2AgentRadiusAccountingIndexNextValid, hm2AgentRadiusServerInetAddrType=hm2AgentRadiusServerInetAddrType, hm2AgentRadiusNamedAccountingServerGroups=hm2AgentRadiusNamedAccountingServerGroups, hm2AgentRadiusServerConfigEntry=hm2AgentRadiusServerConfigEntry, hm2AgentRadiusAccountingServers=hm2AgentRadiusAccountingServers, hm2AgentRadiusServerAddressType=hm2AgentRadiusServerAddressType, hm2AgentRadiusAccountingStatus=hm2AgentRadiusAccountingStatus, hm2AgentRadiusAccountingServerAddr=hm2AgentRadiusAccountingServerAddr, hm2AgentRadiusAccountingMode=hm2AgentRadiusAccountingMode, hm2AgentRadiusServerConfigTable=hm2AgentRadiusServerConfigTable, hm2AgentRadiusNasIpAddress=hm2AgentRadiusNasIpAddress, hm2AgentRadiusServerInetAddr=hm2AgentRadiusServerInetAddr, hm2PlatformRadius=hm2PlatformRadius, hm2AgentRadiusAccountingConfigTable=hm2AgentRadiusAccountingConfigTable, hm2AgentRadiusDeadTime=hm2AgentRadiusDeadTime, hm2AgentRadiusTimeout=hm2AgentRadiusTimeout, hm2AgentRadiusServerCurrentMode=hm2AgentRadiusServerCurrentMode, hm2AgentAuthorizationNetworkRadiusMode=hm2AgentAuthorizationNetworkRadiusMode)
