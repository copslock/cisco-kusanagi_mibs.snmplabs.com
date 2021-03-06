#
# PySNMP MIB module HUAWEI-MDNS-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MDNS-RELAY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Gauge32, Counter32, NotificationType, TimeTicks, Counter64, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Counter32", "NotificationType", "TimeTicks", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwMdnsRelayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326))
hwMdnsRelayMIB.setRevisions(('2014-01-06 11:16', '2014-01-06 11:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwMdnsRelayMIB.setRevisionsDescriptions(('This MIB describes modify mDNS objects.', 'The MIB contains objects of huawei-esap-mDNS.',))
if mibBuilder.loadTexts: hwMdnsRelayMIB.setLastUpdated('201401061116Z')
if mibBuilder.loadTexts: hwMdnsRelayMIB.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwMdnsRelayMIB.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com")
if mibBuilder.loadTexts: hwMdnsRelayMIB.setDescription('This MIB describes mDNS objects used for mDNS relay configuration.')
hwMdnsRelayObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1))
hwMdnsRelayGatewayIPGlobal = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelayGatewayIPGlobal.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayGatewayIPGlobal.setDescription('This item shows the mDNS gateway ip. Users can also set gateway ip through this item ')
hwMdnsRelaySourceIPGlobal = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelaySourceIPGlobal.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelaySourceIPGlobal.setDescription(' This item shows the source ip of mDNS relay. Users can also set source ip through this item. ')
hwMdnsRelayCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3), )
if mibBuilder.loadTexts: hwMdnsRelayCfgTable.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayCfgTable.setDescription('This item shows the configuration of mDNS relay.')
hwMdnsRelayCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1), ).setIndexNames((0, "HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayVlanId"))
if mibBuilder.loadTexts: hwMdnsRelayCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayCfgEntry.setDescription('The mDNS relay configuration table struct.')
hwMdnsRelayVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hwMdnsRelayVlanId.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayVlanId.setDescription('The VLAN-ID or other identifier referring to this VLAN.')
hwMdnsRelayEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelayEnable.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayEnable.setDescription('This item shows the enable status of mDNS relay.')
hwMdnsRelayProbeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 38400), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelayProbeInterval.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayProbeInterval.setDescription('This item shows the service probe interval of mDNS relay. Users can also set service probe interval through this item.')
hwMdnsRelayMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2))
hwMdnsRelayMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 1))
hwMdnsRelayMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 1, 1)).setObjects(("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayGatewayIPGlobal"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelaySourceIPGlobal"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayVlanId"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayEnable"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayProbeInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMdnsRelayMibGroup = hwMdnsRelayMibGroup.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayMibGroup.setDescription('This is the mDNS relay cfg group.')
hwMdnsRelayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 2))
hwMdnsRelayMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 2, 1)).setObjects(("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMdnsRelayMIBCompliance = hwMdnsRelayMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwMdnsRelayMIBCompliance.setDescription('The compliance statement for entities which implement the hwMdnsRelayMIB.')
mibBuilder.exportSymbols("HUAWEI-MDNS-RELAY-MIB", hwMdnsRelayMibGroups=hwMdnsRelayMibGroups, hwMdnsRelayGatewayIPGlobal=hwMdnsRelayGatewayIPGlobal, hwMdnsRelayMIBCompliance=hwMdnsRelayMIBCompliance, hwMdnsRelayCfgEntry=hwMdnsRelayCfgEntry, hwMdnsRelayMibGroup=hwMdnsRelayMibGroup, hwMdnsRelayMIB=hwMdnsRelayMIB, hwMdnsRelaySourceIPGlobal=hwMdnsRelaySourceIPGlobal, hwMdnsRelayVlanId=hwMdnsRelayVlanId, hwMdnsRelayMIBCompliances=hwMdnsRelayMIBCompliances, hwMdnsRelayEnable=hwMdnsRelayEnable, hwMdnsRelayCfgTable=hwMdnsRelayCfgTable, hwMdnsRelayProbeInterval=hwMdnsRelayProbeInterval, hwMdnsRelayObjects=hwMdnsRelayObjects, hwMdnsRelayMibConformance=hwMdnsRelayMibConformance, PYSNMP_MODULE_ID=hwMdnsRelayMIB)
