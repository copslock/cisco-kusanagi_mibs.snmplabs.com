#
# PySNMP MIB module ZYXEL-LEGACY-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-LEGACY-PRIVATE-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Counter64, ObjectIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Unsigned32, Bits, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Counter64", "ObjectIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Unsigned32", "Bits", "iso", "Integer32", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLegacyPrivateVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41))
if mibBuilder.loadTexts: zyxelLegacyPrivateVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLegacyPrivateVlan.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelLegacyPrivateVlan.setContactInfo('')
if mibBuilder.loadTexts: zyxelLegacyPrivateVlan.setDescription('The subtree for legacy private VLAN')
zyxelLegacyPrivateVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1))
zyLegacyPrivateVlanMaxNumberOfVlans = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyLegacyPrivateVlanMaxNumberOfVlans.setStatus('current')
if mibBuilder.loadTexts: zyLegacyPrivateVlanMaxNumberOfVlans.setDescription('The maximum number of legacy private VLAN that can be created.')
zyxelLegacyPrivateVlanTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2), )
if mibBuilder.loadTexts: zyxelLegacyPrivateVlanTable.setStatus('current')
if mibBuilder.loadTexts: zyxelLegacyPrivateVlanTable.setDescription('The table contains legacy private VLAN configuration.')
zyxelLegacyPrivateVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1), ).setIndexNames((0, "ZYXEL-LEGACY-PRIVATE-VLAN-MIB", "zyLegacyPrivateVlanVid"))
if mibBuilder.loadTexts: zyxelLegacyPrivateVlanEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelLegacyPrivateVlanEntry.setDescription('An entry contains legacy private VLAN configuration.')
zyLegacyPrivateVlanVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: zyLegacyPrivateVlanVid.setStatus('current')
if mibBuilder.loadTexts: zyLegacyPrivateVlanVid.setDescription('Private VLAN ID from 1 to 4094. This is the VLAN to which this rule applies.')
zyLegacyPrivateVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLegacyPrivateVlanName.setStatus('current')
if mibBuilder.loadTexts: zyLegacyPrivateVlanName.setDescription('Private VLAN name for identification purpose.')
zyLegacyPrivateVlanPromiscuousPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLegacyPrivateVlanPromiscuousPorts.setStatus('current')
if mibBuilder.loadTexts: zyLegacyPrivateVlanPromiscuousPorts.setDescription('Promiscuous ports of private VLAN can communicate with any ports within this private VLAN. The other ports of this VLAN, which are not defined as promiscuous ports, will be added to the isolation list.')
zyLegacyPrivateVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 41, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyLegacyPrivateVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyLegacyPrivateVlanRowStatus.setDescription('This object allows entries to be created and deleted from the legacy private VLAN table.')
mibBuilder.exportSymbols("ZYXEL-LEGACY-PRIVATE-VLAN-MIB", PYSNMP_MODULE_ID=zyxelLegacyPrivateVlan, zyLegacyPrivateVlanPromiscuousPorts=zyLegacyPrivateVlanPromiscuousPorts, zyLegacyPrivateVlanName=zyLegacyPrivateVlanName, zyxelLegacyPrivateVlan=zyxelLegacyPrivateVlan, zyLegacyPrivateVlanMaxNumberOfVlans=zyLegacyPrivateVlanMaxNumberOfVlans, zyLegacyPrivateVlanRowStatus=zyLegacyPrivateVlanRowStatus, zyxelLegacyPrivateVlanSetup=zyxelLegacyPrivateVlanSetup, zyLegacyPrivateVlanVid=zyLegacyPrivateVlanVid, zyxelLegacyPrivateVlanEntry=zyxelLegacyPrivateVlanEntry, zyxelLegacyPrivateVlanTable=zyxelLegacyPrivateVlanTable)
