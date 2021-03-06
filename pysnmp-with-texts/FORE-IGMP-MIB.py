#
# PySNMP MIB module FORE-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORE-IGMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
preDot1qVlanMIB, = mibBuilder.importSymbols("Fore-Common-MIB", "preDot1qVlanMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, MibIdentifier, Counter64, Gauge32, TimeTicks, ModuleIdentity, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "MibIdentifier", "Counter64", "Gauge32", "TimeTicks", "ModuleIdentity", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
foreIgmpModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 8, 3))
if mibBuilder.loadTexts: foreIgmpModule.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreIgmpModule.setOrganization('MARCONI')
if mibBuilder.loadTexts: foreIgmpModule.setContactInfo(' Postal: Marconi plc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.marconi.com')
if mibBuilder.loadTexts: foreIgmpModule.setDescription('Fore ethernet igmp mib.')
igmpIpmcTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1), )
if mibBuilder.loadTexts: igmpIpmcTable.setStatus('current')
if mibBuilder.loadTexts: igmpIpmcTable.setDescription('Table that contains information IP Multicast addresses and the associated ports in a given vlan.')
igmpIpmcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1, 1), ).setIndexNames((0, "FORE-IGMP-MIB", "vlan"), (0, "FORE-IGMP-MIB", "ipMulticastAddress"))
if mibBuilder.loadTexts: igmpIpmcEntry.setStatus('current')
if mibBuilder.loadTexts: igmpIpmcEntry.setDescription('A list of information maintained for each IP Multicast address.')
ipMulticastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMulticastAddress.setStatus('current')
if mibBuilder.loadTexts: ipMulticastAddress.setDescription('The IP multicast address for which the port group is needed.')
ipmcPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipmcPortGroup.setStatus('current')
if mibBuilder.loadTexts: ipmcPortGroup.setDescription('The port group for which this entry contains IP multicast info.')
igmpRouterTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2), )
if mibBuilder.loadTexts: igmpRouterTable.setStatus('current')
if mibBuilder.loadTexts: igmpRouterTable.setDescription('Table that contains multicast router port groups.')
igmpRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2, 1), ).setIndexNames((0, "FORE-IGMP-MIB", "vlan"))
if mibBuilder.loadTexts: igmpRouterEntry.setStatus('current')
if mibBuilder.loadTexts: igmpRouterEntry.setDescription('A list of information maintained for each vlan.')
vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlan.setStatus('current')
if mibBuilder.loadTexts: vlan.setDescription('The vlan name for which the router port group is needed.')
routerPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: routerPortGroup.setStatus('current')
if mibBuilder.loadTexts: routerPortGroup.setDescription('The port group consisting all the multicast routers.')
mibBuilder.exportSymbols("FORE-IGMP-MIB", foreIgmpModule=foreIgmpModule, routerPortGroup=routerPortGroup, PYSNMP_MODULE_ID=foreIgmpModule, igmpRouterTable=igmpRouterTable, ipmcPortGroup=ipmcPortGroup, ipMulticastAddress=ipMulticastAddress, vlan=vlan, igmpRouterEntry=igmpRouterEntry, igmpIpmcEntry=igmpIpmcEntry, igmpIpmcTable=igmpIpmcTable)
