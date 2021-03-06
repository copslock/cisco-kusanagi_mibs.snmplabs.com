#
# PySNMP MIB module LLDP-EXT-DOT1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LLDP-EXT-DOT1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
lldpLocPortNum, lldpExtensions, lldpRemIndex, lldpRemLocalPortNum, lldpPortConfigEntry, lldpRemTimeMark = mibBuilder.importSymbols("LLDP-MIB", "lldpLocPortNum", "lldpExtensions", "lldpRemIndex", "lldpRemLocalPortNum", "lldpPortConfigEntry", "lldpRemTimeMark")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, iso, Gauge32, ObjectIdentity, NotificationType, Bits, Unsigned32, Counter32, TimeTicks, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "iso", "Gauge32", "ObjectIdentity", "NotificationType", "Bits", "Unsigned32", "Counter32", "TimeTicks", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
lldpXdot1MIB = ModuleIdentity((1, 0, 8802, 1, 1, 2, 1, 5, 32962))
lldpXdot1MIB.setRevisions(('2005-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lldpXdot1MIB.setRevisionsDescriptions(('Published as part of IEEE Std 802.1AB-2005 initial version.',))
if mibBuilder.loadTexts: lldpXdot1MIB.setLastUpdated('200505060000Z')
if mibBuilder.loadTexts: lldpXdot1MIB.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: lldpXdot1MIB.setContactInfo(' WG-URL: http://grouper.ieee.org/groups/802/1/index.html WG-EMail: stds-802-1@ieee.org Contact: Paul Congdon Postal: Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747 USA Tel: +1-916-785-5753 E-mail: paul_congdon@hp.com')
if mibBuilder.loadTexts: lldpXdot1MIB.setDescription("The LLDP Management Information Base extension module for IEEE 802.1 organizationally defined discovery information. In order to assure the uniqueness of the LLDP-MIB, lldpXdot1MIB is branched from lldpExtensions using OUI value as the node. An OUI/'company_id' is a 24 bit globally unique assigned number referenced by various standards. Copyright (C) IEEE (2005). This version of this MIB module is published as Annex F.7.1 of IEEE Std 802.1AB-2005; see the standard itself for full legal notices.")
lldpXdot1Objects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1))
lldpXdot1Config = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1))
lldpXdot1LocalData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2))
lldpXdot1RemoteData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3))
lldpXdot1ConfigPortVlanTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 1), )
if mibBuilder.loadTexts: lldpXdot1ConfigPortVlanTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigPortVlanTable.setDescription('A table that controls selection of LLDP Port VLAN-ID TLVs to be transmitted on individual ports.')
lldpXdot1ConfigPortVlanEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 1, 1), )
lldpPortConfigEntry.registerAugmentions(("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigPortVlanEntry"))
lldpXdot1ConfigPortVlanEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot1ConfigPortVlanEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigPortVlanEntry.setDescription('LLDP configuration information that controls the transmission of IEEE 802.1 organizationally defined Port VLAN-ID TLV on LLDP transmission capable ports. This configuration object augments the lldpPortConfigEntry of the LLDP-MIB, therefore it is only present along with the port configuration defined by the associated lldpPortConfigEntry entry. Each active lldpConfigEntry must be restored from non-volatile storage (along with the corresponding lldpPortConfigEntry) after a re-initialization of the management system.')
lldpXdot1ConfigPortVlanTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1ConfigPortVlanTxEnable.setReference('IEEE 802.1AB-2005 10.2.1.1')
if mibBuilder.loadTexts: lldpXdot1ConfigPortVlanTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigPortVlanTxEnable.setDescription('The lldpXdot1ConfigPortVlanTxEnable, which is defined as a truth value and configured by the network management, determines whether the IEEE 802.1 organizationally defined port VLAN TLV transmission is allowed on a given LLDP transmission capable port. The value of this object must be restored from non-volatile storage after a re-initialization of the management system.')
lldpXdot1ConfigVlanNameTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 2), )
if mibBuilder.loadTexts: lldpXdot1ConfigVlanNameTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigVlanNameTable.setDescription('The table that controls selection of LLDP VLAN name TLV instances to be transmitted on individual ports.')
lldpXdot1ConfigVlanNameTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1ConfigVlanNameTxEnable.setReference('IEEE 802.1AB-2005 10.2.1.1')
if mibBuilder.loadTexts: lldpXdot1ConfigVlanNameTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigVlanNameTxEnable.setDescription('The boolean value that indicates whether the corresponding Local System VLAN name instance will be transmitted on the port defined by the given lldpXdot1LocVlanNameEntry. The value of this object must be restored from non-volatile storage after a re-initialization of the management system.')
lldpXdot1ConfigProtoVlanTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 3), )
if mibBuilder.loadTexts: lldpXdot1ConfigProtoVlanTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigProtoVlanTable.setDescription('The table that controls selection of LLDP Port and Protocol VLAN ID TLV instances to be transmitted on individual ports.')
lldpXdot1ConfigProtoVlanTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 3, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1ConfigProtoVlanTxEnable.setReference('IEEE 802.1AB-2005 10.2.1.1')
if mibBuilder.loadTexts: lldpXdot1ConfigProtoVlanTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigProtoVlanTxEnable.setDescription('The boolean value that indicates whether the corresponding Local System Port and Protocol VLAN instance will be transmitted on the port defined by the given lldpXdot1LocProtoVlanEntry. The value of this object must be restored from non-volatile storage after a re-initialization of the management system.')
lldpXdot1ConfigProtocolTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 4), )
if mibBuilder.loadTexts: lldpXdot1ConfigProtocolTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigProtocolTable.setDescription('The table that controls selection of LLDP Protocol TLV instances to be transmitted on individual ports.')
lldpXdot1ConfigProtocolTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 4, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1ConfigProtocolTxEnable.setReference('IEEE 802.1AB-2005 10.2.1.1')
if mibBuilder.loadTexts: lldpXdot1ConfigProtocolTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigProtocolTxEnable.setDescription('The boolean value that indicates whether the corresponding Local System Protocol Identity instance will be transmitted on the port defined by the given lldpXdot1LocProtocolEntry. The value of this object must be restored from non-volatile storage after a re-initialization of the management system.')
lldpXdot1LocTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 1), )
if mibBuilder.loadTexts: lldpXdot1LocTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocTable.setDescription('This table contains one row per port for IEEE 802.1 organizationally defined LLDP extension on the local system known to this agent.')
lldpXdot1LocEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXdot1LocEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocEntry.setDescription('Information about IEEE 802.1 organizationally defined LLDP extension.')
lldpXdot1LocPortVlanId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1LocPortVlanId.setReference('IEEE 802.1AB-2005 F.2.1')
if mibBuilder.loadTexts: lldpXdot1LocPortVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocPortVlanId.setDescription("The integer value used to identify the port's VLAN identifier associated with the local system. A value of zero shall be used if the system either does not know the PVID or does not support port-based VLAN operation.")
lldpXdot1LocProtoVlanTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2), )
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanTable.setDescription('This table contains one or more rows per Port and Protocol VLAN information about the local system.')
lldpXdot1LocProtoVlanEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"), (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtoVlanId"))
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanEntry.setDescription('Port and protocol VLAN ID Information about a particular port component. There may be multiple port and protocol VLANs, identified by a particular lldpXdot1LocProtoVlanId, configured on the given port.')
lldpXdot1ConfigProtoVlanEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 3, 1), )
lldpXdot1LocProtoVlanEntry.registerAugmentions(("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigProtoVlanEntry"))
lldpXdot1ConfigProtoVlanEntry.setIndexNames(*lldpXdot1LocProtoVlanEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot1ConfigProtoVlanEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigProtoVlanEntry.setDescription('LLDP configuration information that specifies the set of ports (represented as a PortList) on which the Local System Protocol VLAN instance will be transmitted. This configuration object augments the lldpXdot1LocVlanEntry, therefore it is only present along with the Port and Protocol VLAN ID instance contained in the associated lldpXdot1LocVlanEntry entry. Each active lldpXdot1ConfigProtoVlanEntry must be restored from non-volatile storage (along with the corresponding lldpXdot1LocProtoVlanEntry) after a re-initialization of the management system.')
lldpXdot1LocProtoVlanId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), )))
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanId.setReference('IEEE 802.1AB-2005 F.3.2')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanId.setDescription('The integer value used to identify the port and protocol VLANs associated with the given port associated with the local system. A value of zero shall be used if the system either does not know the protocol VLAN ID (PPVID) or does not support port and protocol VLAN operation.')
lldpXdot1LocProtoVlanSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanSupported.setReference('IEEE 802.1AB-2005 F.3.1')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanSupported.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanSupported.setDescription('The truth value used to indicate whether the given port (associated with the local system) supports port and protocol VLANs.')
lldpXdot1LocProtoVlanEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanEnabled.setReference('IEEE 802.1AB-2005 F.3.1')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanEnabled.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtoVlanEnabled.setDescription('The truth value used to indicate whether the port and protocol VLANs are enabled on the given port associated with the local system.')
lldpXdot1LocVlanNameTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3), )
if mibBuilder.loadTexts: lldpXdot1LocVlanNameTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocVlanNameTable.setDescription('This table contains one or more rows per IEEE 802.1Q VLAN name information on the local system known to this agent.')
lldpXdot1LocVlanNameEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"), (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1LocVlanId"))
if mibBuilder.loadTexts: lldpXdot1LocVlanNameEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocVlanNameEntry.setDescription('VLAN name Information about a particular port component. There may be multiple VLANs, identified by a particular lldpXdot1LocVlanId, configured on the given port.')
lldpXdot1ConfigVlanNameEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 2, 1), )
lldpXdot1LocVlanNameEntry.registerAugmentions(("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigVlanNameEntry"))
lldpXdot1ConfigVlanNameEntry.setIndexNames(*lldpXdot1LocVlanNameEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot1ConfigVlanNameEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigVlanNameEntry.setDescription('LLDP configuration information that specifies the set of ports (represented as a PortList) on which the Local System VLAN name instance will be transmitted. This configuration object augments the lldpLocVlanEntry, therefore it is only present along with the VLAN Name instance contained in the associated lldpLocVlanNameEntry entry. Each active lldpXdot1ConfigVlanNameEntry must be restored from non-volatile storage (along with the corresponding lldpXdot1LocVlanNameEntry) after a re-initialization of the management system.')
lldpXdot1LocVlanId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3, 1, 1), VlanId())
if mibBuilder.loadTexts: lldpXdot1LocVlanId.setReference('IEEE 802.1AB-2005 F.4.2')
if mibBuilder.loadTexts: lldpXdot1LocVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocVlanId.setDescription('The integer value used to identify the IEEE 802.1Q VLAN IDs with which the given port is compatible.')
lldpXdot1LocVlanName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1LocVlanName.setReference('IEEE 802.1AB-2005 F.4.4')
if mibBuilder.loadTexts: lldpXdot1LocVlanName.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocVlanName.setDescription('The string value used to identify VLAN name identified by the Vlan Id associated with the given port on the local system. This object should contain the value of the dot1QVLANStaticName object (defined in IETF RFC 2674) identified with the given lldpXdot1LocVlanId.')
lldpXdot1LocProtocolTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4), )
if mibBuilder.loadTexts: lldpXdot1LocProtocolTable.setReference('IEEE 802.1AB-2005 F.5')
if mibBuilder.loadTexts: lldpXdot1LocProtocolTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtocolTable.setDescription('This table contains one or more rows per protocol identity information on the local system known to this agent.')
lldpXdot1LocProtocolEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"), (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtocolIndex"))
if mibBuilder.loadTexts: lldpXdot1LocProtocolEntry.setReference('IEEE 802.1AB-2005 F.5')
if mibBuilder.loadTexts: lldpXdot1LocProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtocolEntry.setDescription('Information about particular protocols that are accessible through the given port component. There may be multiple protocols, identified by particular lldpXdot1ProtocolIndex, and lldpLocPortNum.')
lldpXdot1ConfigProtocolEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 1, 4, 1), )
lldpXdot1LocProtocolEntry.registerAugmentions(("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigProtocolEntry"))
lldpXdot1ConfigProtocolEntry.setIndexNames(*lldpXdot1LocProtocolEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot1ConfigProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigProtocolEntry.setDescription('LLDP configuration information that specifies the set of ports (represented as a PortList) on which the Local System Protocol instance will be transmitted. This configuration object augments the lldpXdot1LocProtoEntry, therefore it is only present along with the Protocol instance contained in the associated lldpXdot1LocProtoEntry entry. Each active lldpXdot1ConfigProtocolEntry must be restored from non-volatile storage (along with the corresponding lldpXdot1LocProtocolEntry) after a re-initialization of the management system.')
lldpXdot1LocProtocolIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpXdot1LocProtocolIndex.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtocolIndex.setDescription('This object represents an arbitrary local integer value used by this agent to identify a particular protocol identity.')
lldpXdot1LocProtocolId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1LocProtocolId.setReference('IEEE 802.1AB-2005 F.5.3')
if mibBuilder.loadTexts: lldpXdot1LocProtocolId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocProtocolId.setDescription('The octet string value used to identify the protocols associated with the given port of the local system.')
lldpXdot1RemTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 1), )
if mibBuilder.loadTexts: lldpXdot1RemTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemTable.setDescription('This table contains one or more rows per physical network connection known to this agent. The agent may wish to ensure that only one lldpXdot1RemEntry is present for each local port, or it may choose to maintain multiple lldpXdot1RemEntries for the same local port.')
lldpXdot1RemEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXdot1RemEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemEntry.setDescription('Information about a particular port component.')
lldpXdot1RemPortVlanId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1RemPortVlanId.setReference('IEEE 802.1AB-2005 F.2.1')
if mibBuilder.loadTexts: lldpXdot1RemPortVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemPortVlanId.setDescription("The integer value used to identify the port's VLAN identifier associated with the remote system. if the remote system either does not know the PVID or does not support port-based VLAN operation, the value of lldpXdot1RemPortVlanId should be zero.")
lldpXdot1RemProtoVlanTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2), )
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanTable.setDescription('This table contains one or more rows per Port and Protocol VLAN information about the remote system, received on the given port.')
lldpXdot1RemProtoVlanEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanId"))
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanEntry.setDescription('Port and protocol VLAN name Information about a particular port component. There may be multiple protocol VLANs, identified by a particular lldpXdot1RemProtoVlanId, configured on the remote system.')
lldpXdot1RemProtoVlanId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), )))
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanId.setReference('IEEE 802.1AB-2005 F.3.2')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanId.setDescription('The integer value used to identify the port and protocol VLANs associated with the given port associated with the remote system. If port and protocol VLANs are not supported on the given port associated with the remote system, or if the port is not enabled with any port and protocol VLAN, the value of lldpXdot1RemProtoVlanId should be zero.')
lldpXdot1RemProtoVlanSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanSupported.setReference('IEEE 802.1AB-2005 F.3.1')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanSupported.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanSupported.setDescription('The truth value used to indicate whether the given port (associated with the remote system) is capable of supporting port and protocol VLANs.')
lldpXdot1RemProtoVlanEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanEnabled.setReference('IEEE 802.1AB-2005 F.3.1')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanEnabled.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtoVlanEnabled.setDescription('The truth value used to indicate whether the port and protocol VLANs are enabled on the given port associated with the remote system.')
lldpXdot1RemVlanNameTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3), )
if mibBuilder.loadTexts: lldpXdot1RemVlanNameTable.setReference('IEEE 802.1AB-2005 F.4')
if mibBuilder.loadTexts: lldpXdot1RemVlanNameTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemVlanNameTable.setDescription('This table contains one or more rows per IEEE 802.1Q VLAN name information about the remote system, received on the given port.')
lldpXdot1RemVlanNameEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1RemVlanId"))
if mibBuilder.loadTexts: lldpXdot1RemVlanNameEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemVlanNameEntry.setDescription('VLAN name Information about a particular port component. There may be multiple VLANs, identified by a particular lldpXdot1RemVlanId, received on the given port.')
lldpXdot1RemVlanId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3, 1, 1), VlanId())
if mibBuilder.loadTexts: lldpXdot1RemVlanId.setReference('IEEE 802.1AB-2005 F.4.2')
if mibBuilder.loadTexts: lldpXdot1RemVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemVlanId.setDescription('The integer value used to identify the IEEE 802.1Q VLAN IDs with which the given port of the remote system is compatible.')
lldpXdot1RemVlanName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1RemVlanName.setReference('IEEE 802.1AB-2005 F.4.4')
if mibBuilder.loadTexts: lldpXdot1RemVlanName.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemVlanName.setDescription('The string value used to identify VLAN name identified by the VLAN Id associated with the remote system.')
lldpXdot1RemProtocolTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4), )
if mibBuilder.loadTexts: lldpXdot1RemProtocolTable.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtocolTable.setDescription('This table contains one or more rows per protocol information about the remote system, received on the given port.')
lldpXdot1RemProtocolEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtocolIndex"))
if mibBuilder.loadTexts: lldpXdot1RemProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtocolEntry.setDescription('Protocol information about a particular port component. There may be multiple protocols, identified by a particular lldpXdot1ProtocolIndex, received on the given port.')
lldpXdot1RemProtocolIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpXdot1RemProtocolIndex.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtocolIndex.setDescription('This object represents an arbitrary local integer value used by this agent to identify a particular protocol identity.')
lldpXdot1RemProtocolId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 1, 3, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot1RemProtocolId.setReference('IEEE 802.1AB-2005 F.5.3')
if mibBuilder.loadTexts: lldpXdot1RemProtocolId.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemProtocolId.setDescription('The octet string value used to identify the protocols associated with the given port of remote system.')
lldpXdot1Conformance = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2))
lldpXdot1Compliances = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 1))
lldpXdot1Groups = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2))
lldpXdot1Compliance = ModuleCompliance((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 1, 1)).setObjects(("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigGroup"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocSysGroup"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1Compliance = lldpXdot1Compliance.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1Compliance.setDescription('The compliance statement for SNMP entities which implement the IEEE 802.1 organizationally defined LLDP extension MIB.')
lldpXdot1ConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2, 1)).setObjects(("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigPortVlanTxEnable"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigVlanNameTxEnable"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigProtoVlanTxEnable"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1ConfigProtocolTxEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1ConfigGroup = lldpXdot1ConfigGroup.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1ConfigGroup.setDescription('The collection of objects which are used to configure the IEEE 802.1 organizationally defined LLDP extension implementation behavior. This group is mandatory for agents which implement the IEEE 802.1 organizationally defined LLDP extension.')
lldpXdot1LocSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2, 2)).setObjects(("LLDP-EXT-DOT1-MIB", "lldpXdot1LocPortVlanId"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtoVlanSupported"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtoVlanEnabled"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocVlanName"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1LocProtocolId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1LocSysGroup = lldpXdot1LocSysGroup.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1LocSysGroup.setDescription('The collection of objects which are used to represent IEEE 802.1 organizationally defined LLDP extension associated with the Local Device Information. This group is mandatory for agents which implement the IEEE 802.1 organizationally defined LLDP extension in the TX mode.')
lldpXdot1RemSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 32962, 2, 2, 3)).setObjects(("LLDP-EXT-DOT1-MIB", "lldpXdot1RemPortVlanId"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanSupported"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtoVlanEnabled"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemVlanName"), ("LLDP-EXT-DOT1-MIB", "lldpXdot1RemProtocolId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1RemSysGroup = lldpXdot1RemSysGroup.setStatus('current')
if mibBuilder.loadTexts: lldpXdot1RemSysGroup.setDescription('The collection of objects which are used to represent LLDP 802.1 organizational extension Local Device Information. This group is mandatory for agents which implement the LLDP 802.1 organizational extension in the RX mode.')
mibBuilder.exportSymbols("LLDP-EXT-DOT1-MIB", lldpXdot1ConfigProtoVlanTxEnable=lldpXdot1ConfigProtoVlanTxEnable, lldpXdot1ConfigVlanNameTxEnable=lldpXdot1ConfigVlanNameTxEnable, lldpXdot1LocEntry=lldpXdot1LocEntry, lldpXdot1RemPortVlanId=lldpXdot1RemPortVlanId, lldpXdot1RemVlanNameEntry=lldpXdot1RemVlanNameEntry, lldpXdot1LocVlanName=lldpXdot1LocVlanName, lldpXdot1LocProtoVlanEntry=lldpXdot1LocProtoVlanEntry, lldpXdot1LocProtocolEntry=lldpXdot1LocProtocolEntry, lldpXdot1RemProtoVlanId=lldpXdot1RemProtoVlanId, lldpXdot1LocTable=lldpXdot1LocTable, lldpXdot1ConfigPortVlanTxEnable=lldpXdot1ConfigPortVlanTxEnable, lldpXdot1LocProtoVlanId=lldpXdot1LocProtoVlanId, lldpXdot1LocProtoVlanEnabled=lldpXdot1LocProtoVlanEnabled, lldpXdot1ConfigGroup=lldpXdot1ConfigGroup, lldpXdot1LocProtoVlanSupported=lldpXdot1LocProtoVlanSupported, lldpXdot1RemEntry=lldpXdot1RemEntry, lldpXdot1Compliance=lldpXdot1Compliance, lldpXdot1RemProtocolEntry=lldpXdot1RemProtocolEntry, lldpXdot1RemProtocolIndex=lldpXdot1RemProtocolIndex, lldpXdot1ConfigProtoVlanTable=lldpXdot1ConfigProtoVlanTable, lldpXdot1ConfigPortVlanEntry=lldpXdot1ConfigPortVlanEntry, lldpXdot1ConfigVlanNameTable=lldpXdot1ConfigVlanNameTable, lldpXdot1RemSysGroup=lldpXdot1RemSysGroup, lldpXdot1ConfigPortVlanTable=lldpXdot1ConfigPortVlanTable, lldpXdot1Conformance=lldpXdot1Conformance, lldpXdot1RemProtocolId=lldpXdot1RemProtocolId, lldpXdot1ConfigProtocolTable=lldpXdot1ConfigProtocolTable, lldpXdot1RemProtoVlanSupported=lldpXdot1RemProtoVlanSupported, lldpXdot1RemProtoVlanTable=lldpXdot1RemProtoVlanTable, lldpXdot1ConfigProtocolEntry=lldpXdot1ConfigProtocolEntry, lldpXdot1ConfigProtoVlanEntry=lldpXdot1ConfigProtoVlanEntry, lldpXdot1RemVlanId=lldpXdot1RemVlanId, lldpXdot1LocalData=lldpXdot1LocalData, lldpXdot1LocSysGroup=lldpXdot1LocSysGroup, lldpXdot1MIB=lldpXdot1MIB, lldpXdot1RemProtoVlanEnabled=lldpXdot1RemProtoVlanEnabled, lldpXdot1ConfigProtocolTxEnable=lldpXdot1ConfigProtocolTxEnable, lldpXdot1RemProtoVlanEntry=lldpXdot1RemProtoVlanEntry, PYSNMP_MODULE_ID=lldpXdot1MIB, lldpXdot1RemTable=lldpXdot1RemTable, lldpXdot1LocProtoVlanTable=lldpXdot1LocProtoVlanTable, lldpXdot1LocProtocolTable=lldpXdot1LocProtocolTable, lldpXdot1LocPortVlanId=lldpXdot1LocPortVlanId, lldpXdot1LocVlanId=lldpXdot1LocVlanId, lldpXdot1LocProtocolId=lldpXdot1LocProtocolId, lldpXdot1Config=lldpXdot1Config, lldpXdot1Objects=lldpXdot1Objects, lldpXdot1ConfigVlanNameEntry=lldpXdot1ConfigVlanNameEntry, lldpXdot1LocVlanNameTable=lldpXdot1LocVlanNameTable, lldpXdot1Compliances=lldpXdot1Compliances, lldpXdot1RemProtocolTable=lldpXdot1RemProtocolTable, lldpXdot1LocProtocolIndex=lldpXdot1LocProtocolIndex, lldpXdot1RemVlanNameTable=lldpXdot1RemVlanNameTable, lldpXdot1Groups=lldpXdot1Groups, lldpXdot1LocVlanNameEntry=lldpXdot1LocVlanNameEntry, lldpXdot1RemoteData=lldpXdot1RemoteData, lldpXdot1RemVlanName=lldpXdot1RemVlanName)
