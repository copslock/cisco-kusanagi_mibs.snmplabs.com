#
# PySNMP MIB module CADANT-CMTS-DHCPRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-DHCPRA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:27:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
cadIfUpChannelId, cadIfUpChannelCardNumber = mibBuilder.importSymbols("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelId", "cadIfUpChannelCardNumber")
cadLayer3, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadLayer3")
InetAddressIPv4or6, CadCpeDeviceTypes, CadBridgePortType = mibBuilder.importSymbols("CADANT-TC", "InetAddressIPv4or6", "CadCpeDeviceTypes", "CadBridgePortType")
cadVrInterfaceIfIndex, = mibBuilder.importSymbols("CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceIfIndex")
InterfaceIndexOrZero, ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex", "InterfaceIndex")
InetAddressType, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressIPv6")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, iso, Integer32, Bits, TimeTicks, IpAddress, NotificationType, MibIdentifier, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "iso", "Integer32", "Bits", "TimeTicks", "IpAddress", "NotificationType", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
TextualConvention, RowStatus, DisplayString, MacAddress, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "MacAddress", "DateAndTime", "TruthValue")
cadDhcpRaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6))
cadDhcpRaMib.setRevisions(('2015-04-22 00:00', '2014-09-16 00:00', '2013-10-17 00:00', '2011-11-16 00:00', '2011-10-27 00:00', '2011-07-05 00:00', '2010-11-01 00:00', '2010-10-19 00:00', '2010-04-22 00:00', '2010-04-15 00:00', '2010-03-09 00:00', '2010-03-05 00:00', '2009-11-04 00:00', '2009-10-01 00:00', '2009-09-21 00:00', '2009-09-17 00:00', '2009-08-27 00:00', '2006-12-06 00:00', '2006-11-22 00:00', '2006-10-18 00:00', '2006-08-22 00:00', '2006-01-27 00:00', '2004-01-18 00:00', '2003-08-18 00:00', '2003-07-30 00:00',))
if mibBuilder.loadTexts: cadDhcpRaMib.setLastUpdated('201504220000Z')
if mibBuilder.loadTexts: cadDhcpRaMib.setOrganization('ARRIS Group, Inc.')
class CadDhcpRelayAgentOptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mac-ifindex", 1), ("us-ifindex", 2), ("octet-string-text", 3), ("octet-string-hex", 4))

class CadDhcpPDPreActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("clear", 1), ("restore", 2))

class CadDhcpPDPreActionDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("all", 0), ("prefixOrIp", 1), ("cableMacInterface", 2))

class CadDhcpRaOptionMSOTextType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("octet-string-text", 1), ("hostname", 2))

cadVrDhcpServerTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4), )
if mibBuilder.loadTexts: cadVrDhcpServerTable.setStatus('current')
cadVrDhcpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1), ).setIndexNames((0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceIfIndex"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpServerIPAddress"))
if mibBuilder.loadTexts: cadVrDhcpServerEntry.setStatus('current')
cadVrDhcpServerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 1), InetAddressIPv4or6())
if mibBuilder.loadTexts: cadVrDhcpServerIPAddress.setStatus('current')
cadVrDhcpServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadVrDhcpServerRowStatus.setStatus('current')
cadVrDhcpServerIPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 4), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadVrDhcpServerIPAddressType.setStatus('current')
cadVrDhcpServerTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 4, 1, 5), CadCpeDeviceTypes()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadVrDhcpServerTypes.setStatus('current')
cadDhcpThrottle = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5))
cadDhcpThrottleEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpThrottleEnable.setStatus('current')
cadDhcpThrottleBurstSize = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpThrottleBurstSize.setStatus('current')
cadDhcpThrottleRate = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpThrottleRate.setStatus('current')
cadArpThrottleEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadArpThrottleEnable.setStatus('current')
cadDhcpV6ThrottleEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpV6ThrottleEnable.setStatus('current')
cadNdThrottleEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 5, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadNdThrottleEnable.setStatus('current')
cadDhcpRaOption = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6))
cadDhcpRaOptionType = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 1), CadDhcpRelayAgentOptionType().clone('mac-ifindex')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpRaOptionType.setStatus('current')
cadDhcpRaOptionString = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpRaOptionString.setStatus('current')
cadDhcpRaOptionUpstreamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3), )
if mibBuilder.loadTexts: cadDhcpRaOptionUpstreamChannelTable.setStatus('current')
cadDhcpRaOptionUpstreamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadDhcpRaOptionUpstreamChannelEntry.setStatus('current')
cadDhcpRaOptUpChannelOptionType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1, 1), CadDhcpRelayAgentOptionType().clone('us-ifindex')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDhcpRaOptUpChannelOptionType.setStatus('current')
cadDhcpRaOptUpChannelOptionString = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDhcpRaOptUpChannelOptionString.setStatus('current')
cadDhcpRaOptUpChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDhcpRaOptUpChannelStatus.setStatus('current')
cadVrDhcpRelaySrcInterfaceIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadVrDhcpRelaySrcInterfaceIndex.setStatus('current')
cadVrDhcpRelaySrcInterfaceLinkAddrEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadVrDhcpRelaySrcInterfaceLinkAddrEnabled.setStatus('current')
cadVrDhcpRaOptionScnEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadVrDhcpRaOptionScnEnable.setStatus('current')
cadDhcpRaOptionMSOTextType = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 7), CadDhcpRaOptionMSOTextType().clone('octet-string-text')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpRaOptionMSOTextType.setStatus('current')
cadDhcpRaOptionMSOTextString = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpRaOptionMSOTextString.setStatus('current')
cadDhcpRaOptionChannelMSOTextTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9), )
if mibBuilder.loadTexts: cadDhcpRaOptionChannelMSOTextTable.setStatus('current')
cadDhcpRaOptionChannelMSOTextEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadDhcpRaOptionChannelMSOTextEntry.setStatus('current')
cadDhcpRaOptionChannelMSOTextType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1, 1), CadDhcpRaOptionMSOTextType().clone('octet-string-text')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDhcpRaOptionChannelMSOTextType.setStatus('current')
cadDhcpRaOptionChannelMSOTextString = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDhcpRaOptionChannelMSOTextString.setStatus('current')
cadDhcpRaOptionChannelMSOTextStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 9, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDhcpRaOptionChannelMSOTextStatus.setStatus('current')
cadVrDhcpRaOptionFanoutDisabled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 6, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadVrDhcpRaOptionFanoutDisabled.setStatus('current')
cadDhcpRaLeaseQuery = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 7))
cadDhcpRaLeasequeryVersion = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5, 11))).clone(namedValues=NamedValues(("draft-0", 1), ("draft-2", 3), ("draft-4", 5), ("rfc-4388", 11))).clone('draft-0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpRaLeasequeryVersion.setStatus('current')
cadDhcpRaLeasequeryMessageType = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(9, 13)).clone(13)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpRaLeasequeryMessageType.setStatus('current')
cadVrDhcpLinkAddressTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8), )
if mibBuilder.loadTexts: cadVrDhcpLinkAddressTable.setStatus('current')
cadVrDhcpLinkAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1), ).setIndexNames((0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceIfIndex"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpLinkAddressType"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpLinkAddress"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpLinkType"))
if mibBuilder.loadTexts: cadVrDhcpLinkAddressEntry.setStatus('current')
cadVrDhcpLinkAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cadVrDhcpLinkAddressType.setStatus('current')
cadVrDhcpLinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 2), InetAddressIPv4or6())
if mibBuilder.loadTexts: cadVrDhcpLinkAddress.setStatus('current')
cadVrDhcpLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 3), CadBridgePortType())
if mibBuilder.loadTexts: cadVrDhcpLinkType.setStatus('current')
cadVrDhcpLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadVrDhcpLinkRowStatus.setStatus('current')
cadDhcpPd = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 9))
cadDhcpPdRiEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 9, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpPdRiEnabled.setStatus('current')
cadDhcpPdPrefixStabilityEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 9, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpPdPrefixStabilityEnabled.setStatus('current')
cadVrDhcpPdTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10), )
if mibBuilder.loadTexts: cadVrDhcpPdTable.setStatus('current')
cadVrDhcpPdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1), ).setIndexNames((0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdClientIpv6Addr"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdClientIaid"))
if mibBuilder.loadTexts: cadVrDhcpPdEntry.setStatus('current')
cadVrDhcpPdClientIpv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 1), InetAddressIPv6())
if mibBuilder.loadTexts: cadVrDhcpPdClientIpv6Addr.setStatus('current')
cadVrDhcpPdClientIaid = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cadVrDhcpPdClientIaid.setStatus('current')
cadVrDhcpPdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdIfIndex.setStatus('current')
cadVrDhcpPdClientDuid = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdClientDuid.setStatus('current')
cadVrDhcpPdCmMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdCmMacAddress.setStatus('current')
cadVrDhcpPdT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdT1.setStatus('current')
cadVrDhcpPdT2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 10, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdT2.setStatus('current')
cadVrDhcpPdPrefixTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11), )
if mibBuilder.loadTexts: cadVrDhcpPdPrefixTable.setStatus('current')
cadVrDhcpPdPrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1), ).setIndexNames((0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPreClientIpv6Addr"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPreClientIaid"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPrePrefix"), (0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpPdPrePrefixLength"))
if mibBuilder.loadTexts: cadVrDhcpPdPrefixEntry.setStatus('current')
cadVrDhcpPdPreClientIpv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 1), InetAddressIPv6())
if mibBuilder.loadTexts: cadVrDhcpPdPreClientIpv6Addr.setStatus('current')
cadVrDhcpPdPreClientIaid = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cadVrDhcpPdPreClientIaid.setStatus('current')
cadVrDhcpPdPrePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 3), InetAddressIPv6())
if mibBuilder.loadTexts: cadVrDhcpPdPrePrefix.setStatus('current')
cadVrDhcpPdPrePrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)))
if mibBuilder.loadTexts: cadVrDhcpPdPrePrefixLength.setStatus('current')
cadVrDhcpPdPrePreferredLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdPrePreferredLifetime.setStatus('current')
cadVrDhcpPdPreValidLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdPreValidLifetime.setStatus('current')
cadVrDhcpPdPreRouteInject = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdPreRouteInject.setStatus('current')
cadVrDhcpPdPreExpirytime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 11, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadVrDhcpPdPreExpirytime.setStatus('current')
cadVrDhcpRelayEgressIfTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12), )
if mibBuilder.loadTexts: cadVrDhcpRelayEgressIfTable.setStatus('current')
cadVrDhcpRelayEgressIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12, 1), ).setIndexNames((0, "CADANT-CMTS-DHCPRA-MIB", "cadVrDhcpRelayEgressIfIndex"))
if mibBuilder.loadTexts: cadVrDhcpRelayEgressIfEntry.setStatus('current')
cadVrDhcpRelayEgressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadVrDhcpRelayEgressIfIndex.setStatus('current')
cadVrDhcpRelayEgressIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 12, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadVrDhcpRelayEgressIfRowStatus.setStatus('current')
cadDhcpPdPrefixAction = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13))
cadDhcpPdPrefixActionType = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 1), CadDhcpPDPreActionType().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpPdPrefixActionType.setStatus('current')
cadDhcpPdPrefixActionDataType = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 2), CadDhcpPDPreActionDataType().clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpPdPrefixActionDataType.setStatus('current')
cadDhcpPdPrefixActionDataIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 3), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpPdPrefixActionDataIfIndex.setStatus('current')
cadDhcpPdPrefixActionDataPrefixOrIp = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 4), InetAddressIPv6()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpPdPrefixActionDataPrefixOrIp.setStatus('current')
cadDhcpPdPrefixActionDataPrefixOrIpLen = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 13, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDhcpPdPrefixActionDataPrefixOrIpLen.setStatus('current')
cadDhcpPdBLQFailedGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14))
cadDhcpPdBLQFailedTCPSIP = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 1), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDhcpPdBLQFailedTCPSIP.setStatus('current')
cadDhcpPdBLQFailedTCPDIP = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 2), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDhcpPdBLQFailedTCPDIP.setStatus('current')
cadDhcpPdBLQFailedTCPTime = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDhcpPdBLQFailedTCPTime.setStatus('current')
cadDhcpPdBLQFailedTCPNum = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 6, 14, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDhcpPdBLQFailedTCPNum.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-DHCPRA-MIB", cadVrDhcpRelaySrcInterfaceLinkAddrEnabled=cadVrDhcpRelaySrcInterfaceLinkAddrEnabled, cadDhcpRaOptionChannelMSOTextString=cadDhcpRaOptionChannelMSOTextString, cadDhcpThrottleRate=cadDhcpThrottleRate, cadVrDhcpServerIPAddressType=cadVrDhcpServerIPAddressType, cadDhcpRaOption=cadDhcpRaOption, cadVrDhcpLinkAddressType=cadVrDhcpLinkAddressType, cadVrDhcpPdClientDuid=cadVrDhcpPdClientDuid, cadVrDhcpPdClientIaid=cadVrDhcpPdClientIaid, cadDhcpPdPrefixActionDataIfIndex=cadDhcpPdPrefixActionDataIfIndex, cadVrDhcpPdEntry=cadVrDhcpPdEntry, cadVrDhcpRaOptionFanoutDisabled=cadVrDhcpRaOptionFanoutDisabled, cadVrDhcpPdCmMacAddress=cadVrDhcpPdCmMacAddress, cadVrDhcpPdPrePrefix=cadVrDhcpPdPrePrefix, CadDhcpRelayAgentOptionType=CadDhcpRelayAgentOptionType, cadVrDhcpPdT1=cadVrDhcpPdT1, cadDhcpThrottleEnable=cadDhcpThrottleEnable, cadDhcpPdBLQFailedTCPTime=cadDhcpPdBLQFailedTCPTime, cadDhcpPd=cadDhcpPd, cadNdThrottleEnable=cadNdThrottleEnable, cadDhcpPdPrefixAction=cadDhcpPdPrefixAction, cadDhcpRaOptionChannelMSOTextStatus=cadDhcpRaOptionChannelMSOTextStatus, cadDhcpRaOptionMSOTextType=cadDhcpRaOptionMSOTextType, cadVrDhcpServerRowStatus=cadVrDhcpServerRowStatus, cadDhcpRaLeasequeryMessageType=cadDhcpRaLeasequeryMessageType, cadDhcpThrottleBurstSize=cadDhcpThrottleBurstSize, cadVrDhcpRelayEgressIfRowStatus=cadVrDhcpRelayEgressIfRowStatus, cadDhcpRaLeaseQuery=cadDhcpRaLeaseQuery, cadDhcpRaOptUpChannelStatus=cadDhcpRaOptUpChannelStatus, cadDhcpPdPrefixActionType=cadDhcpPdPrefixActionType, cadVrDhcpRelayEgressIfTable=cadVrDhcpRelayEgressIfTable, cadDhcpV6ThrottleEnable=cadDhcpV6ThrottleEnable, cadDhcpRaOptionChannelMSOTextEntry=cadDhcpRaOptionChannelMSOTextEntry, cadVrDhcpServerTable=cadVrDhcpServerTable, cadDhcpRaOptUpChannelOptionType=cadDhcpRaOptUpChannelOptionType, cadDhcpPdRiEnabled=cadDhcpPdRiEnabled, cadVrDhcpLinkType=cadVrDhcpLinkType, cadVrDhcpPdClientIpv6Addr=cadVrDhcpPdClientIpv6Addr, cadVrDhcpRelayEgressIfEntry=cadVrDhcpRelayEgressIfEntry, cadDhcpPdPrefixActionDataPrefixOrIp=cadDhcpPdPrefixActionDataPrefixOrIp, cadDhcpRaOptionString=cadDhcpRaOptionString, cadDhcpRaOptionChannelMSOTextTable=cadDhcpRaOptionChannelMSOTextTable, CadDhcpRaOptionMSOTextType=CadDhcpRaOptionMSOTextType, cadArpThrottleEnable=cadArpThrottleEnable, cadVrDhcpServerEntry=cadVrDhcpServerEntry, cadVrDhcpPdPrePrefixLength=cadVrDhcpPdPrePrefixLength, CadDhcpPDPreActionType=CadDhcpPDPreActionType, cadDhcpRaOptionType=cadDhcpRaOptionType, cadDhcpPdBLQFailedTCPSIP=cadDhcpPdBLQFailedTCPSIP, cadVrDhcpRaOptionScnEnable=cadVrDhcpRaOptionScnEnable, cadVrDhcpPdTable=cadVrDhcpPdTable, cadVrDhcpPdPrePreferredLifetime=cadVrDhcpPdPrePreferredLifetime, cadVrDhcpLinkRowStatus=cadVrDhcpLinkRowStatus, cadVrDhcpPdPreClientIpv6Addr=cadVrDhcpPdPreClientIpv6Addr, CadDhcpPDPreActionDataType=CadDhcpPDPreActionDataType, cadDhcpRaOptionUpstreamChannelTable=cadDhcpRaOptionUpstreamChannelTable, cadDhcpPdPrefixActionDataType=cadDhcpPdPrefixActionDataType, cadVrDhcpPdPreClientIaid=cadVrDhcpPdPreClientIaid, cadVrDhcpPdPreExpirytime=cadVrDhcpPdPreExpirytime, cadVrDhcpPdPrefixEntry=cadVrDhcpPdPrefixEntry, cadDhcpRaLeasequeryVersion=cadDhcpRaLeasequeryVersion, cadDhcpPdPrefixActionDataPrefixOrIpLen=cadDhcpPdPrefixActionDataPrefixOrIpLen, cadDhcpPdBLQFailedTCPNum=cadDhcpPdBLQFailedTCPNum, cadDhcpRaMib=cadDhcpRaMib, cadVrDhcpLinkAddress=cadVrDhcpLinkAddress, cadVrDhcpServerIPAddress=cadVrDhcpServerIPAddress, cadDhcpRaOptionMSOTextString=cadDhcpRaOptionMSOTextString, cadDhcpPdPrefixStabilityEnabled=cadDhcpPdPrefixStabilityEnabled, cadVrDhcpPdPreRouteInject=cadVrDhcpPdPreRouteInject, PYSNMP_MODULE_ID=cadDhcpRaMib, cadVrDhcpPdPrefixTable=cadVrDhcpPdPrefixTable, cadVrDhcpLinkAddressEntry=cadVrDhcpLinkAddressEntry, cadVrDhcpRelayEgressIfIndex=cadVrDhcpRelayEgressIfIndex, cadVrDhcpRelaySrcInterfaceIndex=cadVrDhcpRelaySrcInterfaceIndex, cadVrDhcpPdT2=cadVrDhcpPdT2, cadDhcpRaOptionUpstreamChannelEntry=cadDhcpRaOptionUpstreamChannelEntry, cadDhcpPdBLQFailedTCPDIP=cadDhcpPdBLQFailedTCPDIP, cadDhcpThrottle=cadDhcpThrottle, cadDhcpRaOptUpChannelOptionString=cadDhcpRaOptUpChannelOptionString, cadVrDhcpPdIfIndex=cadVrDhcpPdIfIndex, cadDhcpPdBLQFailedGrp=cadDhcpPdBLQFailedGrp, cadVrDhcpPdPreValidLifetime=cadVrDhcpPdPreValidLifetime, cadVrDhcpLinkAddressTable=cadVrDhcpLinkAddressTable, cadDhcpRaOptionChannelMSOTextType=cadDhcpRaOptionChannelMSOTextType, cadVrDhcpServerTypes=cadVrDhcpServerTypes)
