#
# PySNMP MIB module A3COM-HUAWEI-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
IPv6FlowLabelOrAny, = mibBuilder.importSymbols("IPV6-FLOW-LABEL-MIB", "IPv6FlowLabelOrAny")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, TimeTicks, ModuleIdentity, IpAddress, NotificationType, Gauge32, Integer32, iso, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "IpAddress", "NotificationType", "Gauge32", "Integer32", "iso", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Bits")
TextualConvention, StorageType, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "RowStatus", "DisplayString")
h3cTunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53))
h3cTunnel.setRevisions(('2005-06-04 00:00',))
if mibBuilder.loadTexts: h3cTunnel.setLastUpdated('200506040000Z')
if mibBuilder.loadTexts: h3cTunnel.setOrganization('Huawei 3Com Technologies Co., Ltd. ')
class H3cTunnelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50))
    namedValues = NamedValues(("other", 1), ("direct", 2), ("gre", 3), ("minimal", 4), ("l2tp", 5), ("pptp", 6), ("l2f", 7), ("udp", 8), ("atmp", 9), ("msdp", 10), ("sixToFour", 11), ("sixOverFour", 12), ("isatap", 13), ("teredo", 14), ("tunnelModeReserve", 35), ("tunnelModeIPv4Gre", 36), ("tunnelModeIPv6Gre", 37), ("tunnelModeIPv4IPv4", 38), ("tunnelModeIPv4IPv6Config", 39), ("tunnelModeIPv4IPv6Auto", 40), ("tunnelModeIPv4IPv66to4", 41), ("tunnelModeIPv4IPv6Isatap", 42), ("tunnelModeIPv6IPv4", 43), ("tunnelModeIPv6IPv6", 44), ("tunnelModeIPv4UdpDVPN", 45), ("tunnelModeIPv4GreDVPN", 46), ("tunnelModeIPv6UdpDVPN", 47), ("tunnelModeIPv6GreDVPN", 48), ("tunnelModeCrLsp", 49), ("tunnelModeMax", 50))

h3cTunnelMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1))
h3cTunnelTables = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1))
h3cTunnelIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1), )
if mibBuilder.loadTexts: h3cTunnelIfTable.setStatus('current')
h3cTunnelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cTunnelIfEntry.setStatus('current')
h3cTunnelIfEncapsMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 3), H3cTunnelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cTunnelIfEncapsMethod.setStatus('current')
h3cTunnelIfHopLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTunnelIfHopLimit.setStatus('current')
h3cTunnelIfSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ipsec", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTunnelIfSecurity.setStatus('current')
h3cTunnelIfTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTunnelIfTOS.setStatus('current')
h3cTunnelIfFlowLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 7), IPv6FlowLabelOrAny()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTunnelIfFlowLabel.setStatus('current')
h3cTunnelIfAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 8), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cTunnelIfAddressType.setStatus('current')
h3cTunnelIfLocalInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 9), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cTunnelIfLocalInetAddress.setStatus('current')
h3cTunnelIfRemoteInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 10), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cTunnelIfRemoteInetAddress.setStatus('current')
h3cTunnelIfEncapsLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTunnelIfEncapsLimit.setStatus('current')
h3cTunnelInetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 3), )
if mibBuilder.loadTexts: h3cTunnelInetConfigTable.setStatus('current')
h3cTunnelInetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-TUNNEL-MIB", "h3cTunnelInetConfigSlot"), (0, "A3COM-HUAWEI-TUNNEL-MIB", "h3cTunnelInetConfigSubSlot"), (0, "A3COM-HUAWEI-TUNNEL-MIB", "h3cTunnelInetConfigTunnNum"))
if mibBuilder.loadTexts: h3cTunnelInetConfigEntry.setStatus('current')
h3cTunnelInetConfigSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: h3cTunnelInetConfigSlot.setStatus('current')
h3cTunnelInetConfigSubSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: h3cTunnelInetConfigSubSlot.setStatus('current')
h3cTunnelInetConfigTunnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: h3cTunnelInetConfigTunnNum.setStatus('current')
h3cTunnelInetConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 3, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTunnelInetConfigIfIndex.setStatus('current')
h3cTunnelInetConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 53, 1, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cTunnelInetConfigStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-TUNNEL-MIB", h3cTunnelInetConfigStatus=h3cTunnelInetConfigStatus, PYSNMP_MODULE_ID=h3cTunnel, h3cTunnelInetConfigIfIndex=h3cTunnelInetConfigIfIndex, h3cTunnelIfFlowLabel=h3cTunnelIfFlowLabel, h3cTunnel=h3cTunnel, h3cTunnelIfHopLimit=h3cTunnelIfHopLimit, h3cTunnelIfTable=h3cTunnelIfTable, h3cTunnelIfRemoteInetAddress=h3cTunnelIfRemoteInetAddress, h3cTunnelIfEncapsMethod=h3cTunnelIfEncapsMethod, h3cTunnelIfEntry=h3cTunnelIfEntry, h3cTunnelInetConfigTable=h3cTunnelInetConfigTable, h3cTunnelMIBObjects=h3cTunnelMIBObjects, h3cTunnelIfTOS=h3cTunnelIfTOS, h3cTunnelInetConfigTunnNum=h3cTunnelInetConfigTunnNum, h3cTunnelInetConfigSlot=h3cTunnelInetConfigSlot, h3cTunnelIfLocalInetAddress=h3cTunnelIfLocalInetAddress, h3cTunnelInetConfigSubSlot=h3cTunnelInetConfigSubSlot, h3cTunnelIfSecurity=h3cTunnelIfSecurity, H3cTunnelType=H3cTunnelType, h3cTunnelIfAddressType=h3cTunnelIfAddressType, h3cTunnelTables=h3cTunnelTables, h3cTunnelInetConfigEntry=h3cTunnelInetConfigEntry, h3cTunnelIfEncapsLimit=h3cTunnelIfEncapsLimit)
