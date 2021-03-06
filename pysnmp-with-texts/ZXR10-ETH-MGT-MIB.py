#
# PySNMP MIB module ZXR10-ETH-MGT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-ETH-MGT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, ModuleIdentity, Counter64, TimeTicks, Counter32, Unsigned32, ObjectIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "ModuleIdentity", "Counter64", "TimeTicks", "Counter32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Bits")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
zxr10interfaces, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10interfaces")
zxr10EthMgtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2))
zxr10EthMgtMIB.setRevisions(('2005-04-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zxr10EthMgtMIB.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: zxr10EthMgtMIB.setLastUpdated('200504120000Z')
if mibBuilder.loadTexts: zxr10EthMgtMIB.setOrganization('ZTE Corporation')
if mibBuilder.loadTexts: zxr10EthMgtMIB.setContactInfo('ZTE Corporation Nanjing Institute of ZTE Corporation No.68 Zijinghua Rd. Yuhuatai District, Nanjing, China Tel: +86-25-52870000')
if mibBuilder.loadTexts: zxr10EthMgtMIB.setDescription('ZXROS v4.6.03 ethnet query and configuration MIB')
zxr10EthMgtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1))
zxr10EthQuery = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1))
zxr10EthConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2))
zxr10EthStats = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3))
class DisplayString(OctetString):
    pass

class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or interface sub-layer in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class EthEncapsulationType(TextualConvention, Integer32):
    description = 'Ethnet encapsulation type such as 802.1Q'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("encap-802dot1Q", 1))

class IfSpeedType(TextualConvention, Integer32):
    description = 'Ethnet encapsulation type such as 802.1Q'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4))
    namedValues = NamedValues(("speed-auto", 0), ("speed-1000mbps", 2), ("speed-100mbps", 3), ("speed-10mbps", 4))

class EthPhyFrameType(TextualConvention, Integer32):
    description = 'Ethnet encapsulation type such as 802.1Q'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ethernet-II", 1))

class EthPhyWorkType(TextualConvention, Integer32):
    description = 'Ethnet encapsulation type such as 802.1Q'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("full-duplex", 1), ("half-duplex", 2))

class EthNegotiationType(TextualConvention, Integer32):
    description = 'Ethnet encapsulation type such as 802.1Q'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 0))
    namedValues = NamedValues(("auto", 1), ("no-auto", 0))

zxr10EthSubIfQueryTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1), )
if mibBuilder.loadTexts: zxr10EthSubIfQueryTable.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfQueryTable.setDescription('Ethnet sub interface query table')
zxr10EthSubIfQueryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1), ).setIndexNames((0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfParentIfIndex"), (0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfIndex"))
if mibBuilder.loadTexts: zxr10EthSubIfQueryEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfQueryEntry.setDescription('')
zxr10EthSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfIndex.setDescription('Sub interface ifIndex ')
zxr10EthSubIfParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfParentIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfParentIfIndex.setDescription("Sub interface's parent interface ifIndex")
zxr10EthSubIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfName.setDescription("Sub interface's name")
zxr10EthSubIfParentIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfParentIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfParentIfName.setDescription("Parent interface's name")
zxr10EthSubIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1), )
if mibBuilder.loadTexts: zxr10EthSubIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigTable.setDescription('Sub interface cnfigration table')
zxr10EthSubIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1), ).setIndexNames((0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfConfigParentIfIndex"), (0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfConfigSubIfName"))
if mibBuilder.loadTexts: zxr10EthSubIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigEntry.setDescription('')
zxr10EthSubIfConfigParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfConfigParentIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigParentIfIndex.setDescription('Parent interface ifIndex')
zxr10EthSubIfConfigParentIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfConfigParentIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigParentIfName.setDescription(' Parent interface name')
zxr10EthSubIfConfigSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfConfigSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigSubIfIndex.setDescription('Sub interface ifIndex ')
zxr10EthSubIfConfigSubIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSubIfConfigSubIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigSubIfName.setDescription('Sub interface name')
zxr10EthSubIfConfigVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthSubIfConfigVlanID.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigVlanID.setDescription('Vlan ID of this sub interface')
zxr10EthSubIfConfigEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 6), EthEncapsulationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthSubIfConfigEncapType.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigEncapType.setDescription('Ethnet encapsulation type such as 802.1Q')
zxr10EthSubIfConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthSubIfConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSubIfConfigRowStatus.setDescription("This object is used to manage creation and deletion of rows in this table. zxr10SecondaryIpAddrRowStatus must be set to 'creatAndGo' to create an entry and set to 'destroy' to delete an entry. The value in any column may be modified any time even the value of this entry rowStatus object is 'active'. Caution has to be taken before destroying any entry. Example: Need to change the IP address of an interface, which provides sole network connectivity. This has to be done by destroying the entry and creating a new one. The device would loose network connectivity after the entry is destroyed. In this case, the destroy of the old entry and the creation on the new entry should be packed in the same PDU.")
zxr10EthPhyIfTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3), )
if mibBuilder.loadTexts: zxr10EthPhyIfTable.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyIfTable.setDescription('Ethnet configuration table')
zxr10EthPhyIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1), ).setIndexNames((0, "ZXR10-ETH-MGT-MIB", "zxr10EthPhyIfIndex"))
if mibBuilder.loadTexts: zxr10EthPhyIfEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyIfEntry.setDescription('')
zxr10EthPhyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthPhyIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyIfIndex.setDescription('Physical Ethnet interface ifIndex')
zxr10EthPhyIfFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 2), EthPhyFrameType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthPhyIfFrameType.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyIfFrameType.setDescription(' ')
zxr10EthPhyIfNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 3), EthNegotiationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthPhyIfNegotiation.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyIfNegotiation.setDescription('')
zxr10EthPhyWorkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 4), EthPhyWorkType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthPhyWorkType.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyWorkType.setDescription('')
zxr10EthPhyIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 5), IfSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthPhyIfSpeed.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyIfSpeed.setDescription('')
zxr10EthPhyIfMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthPhyIfMTU.setStatus('current')
if mibBuilder.loadTexts: zxr10EthPhyIfMTU.setDescription('Ethnet encapsulation type such as 802.1Q')
zxr10EthRecvStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1), )
if mibBuilder.loadTexts: zxr10EthRecvStatsTable.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvStatsTable.setDescription('Ethnet configuration table')
zxr10EthRecvStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1), ).setIndexNames((0, "ZXR10-ETH-MGT-MIB", "zxr10EthPhyIfIndex"))
if mibBuilder.loadTexts: zxr10EthRecvStatsEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvStatsEntry.setDescription('')
zxr10EthRecvStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvStatsIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvStatsIfIndex.setDescription('Physical Ethnet interface ifIndex')
zxr10EthRecvPktsUnder64Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPktsUnder64Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPktsUnder64Octects.setDescription(' ')
zxr10EthRecvPkts64Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPkts64Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPkts64Octects.setDescription('')
zxr10EthRecvPkts65to127Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPkts65to127Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPkts65to127Octects.setDescription('')
zxr10EthRecvPkts128to255Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPkts128to255Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPkts128to255Octects.setDescription('')
zxr10EthRecvPkts255to511Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPkts255to511Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPkts255to511Octects.setDescription('')
zxr10EthRecvPkts512to1023Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPkts512to1023Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPkts512to1023Octects.setDescription('')
zxr10EthRecvPkts1024to1518Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPkts1024to1518Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPkts1024to1518Octects.setDescription('')
zxr10EthRecvPktsOverSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPktsOverSize.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPktsOverSize.setDescription('')
zxr10EthRecvPktsCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthRecvPktsCRCError.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvPktsCRCError.setDescription('')
zxr10EthRecvClearCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthRecvClearCounts.setStatus('current')
if mibBuilder.loadTexts: zxr10EthRecvClearCounts.setDescription(' If set value to 1 ,clear interface counters')
zxr10EthSndStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2), )
if mibBuilder.loadTexts: zxr10EthSndStatsTable.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndStatsTable.setDescription('Ethnet configuration table')
zxr10EthSndStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1), ).setIndexNames((0, "ZXR10-ETH-MGT-MIB", "zxr10EthPhyIfIndex"))
if mibBuilder.loadTexts: zxr10EthSndStatsEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndStatsEntry.setDescription('')
zxr10EthSndStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndStatsIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndStatsIfIndex.setDescription('Physical Ethnet interface ifIndex')
zxr10EthSndPktsUnder64Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPktsUnder64Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPktsUnder64Octects.setDescription(' ')
zxr10EthSndPkts64Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPkts64Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPkts64Octects.setDescription('')
zxr10EthSndPkts65to127Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPkts65to127Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPkts65to127Octects.setDescription('')
zxr10EthSndPkts128to255Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPkts128to255Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPkts128to255Octects.setDescription('')
zxr10EthSndPkts255to511Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPkts255to511Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPkts255to511Octects.setDescription('')
zxr10EthSndPkts512to1023Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPkts512to1023Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPkts512to1023Octects.setDescription('')
zxr10EthSndPkts1024to1518Octects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPkts1024to1518Octects.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPkts1024to1518Octects.setDescription('')
zxr10EthSndPktsOverSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthSndPktsOverSize.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndPktsOverSize.setDescription('')
zxr10EthSndClearCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthSndClearCounts.setStatus('current')
if mibBuilder.loadTexts: zxr10EthSndClearCounts.setDescription('If set value to 1,clear interface counters')
zxr10EthLoopBackTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4), )
if mibBuilder.loadTexts: zxr10EthLoopBackTable.setStatus('current')
if mibBuilder.loadTexts: zxr10EthLoopBackTable.setDescription('Ethnet loopback interface table')
zxr10EthLoopBackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1), ).setIndexNames((0, "ZXR10-ETH-MGT-MIB", "zxr10EthLoopBackNo"))
if mibBuilder.loadTexts: zxr10EthLoopBackEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10EthLoopBackEntry.setDescription('')
zxr10EthLoopBackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthLoopBackIfIndex.setStatus('current')
if mibBuilder.loadTexts: zxr10EthLoopBackIfIndex.setDescription('')
zxr10EthLoopBackIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthLoopBackIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10EthLoopBackIfName.setDescription('')
zxr10EthLoopBackNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10EthLoopBackNo.setStatus('current')
if mibBuilder.loadTexts: zxr10EthLoopBackNo.setDescription('')
zxr10EthLoopBackRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10EthLoopBackRowStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10EthLoopBackRowStatus.setDescription('')
mibBuilder.exportSymbols("ZXR10-ETH-MGT-MIB", InterfaceIndex=InterfaceIndex, zxr10EthRecvPktsOverSize=zxr10EthRecvPktsOverSize, zxr10EthSndPktsOverSize=zxr10EthSndPktsOverSize, zxr10EthRecvPktsUnder64Octects=zxr10EthRecvPktsUnder64Octects, EthPhyWorkType=EthPhyWorkType, zxr10EthSubIfConfigTable=zxr10EthSubIfConfigTable, zxr10EthPhyIfIndex=zxr10EthPhyIfIndex, zxr10EthRecvPkts128to255Octects=zxr10EthRecvPkts128to255Octects, zxr10EthSubIfQueryEntry=zxr10EthSubIfQueryEntry, zxr10EthSubIfQueryTable=zxr10EthSubIfQueryTable, zxr10EthMgtMIB=zxr10EthMgtMIB, zxr10EthSndPkts64Octects=zxr10EthSndPkts64Octects, zxr10EthSubIfParentIfIndex=zxr10EthSubIfParentIfIndex, zxr10EthPhyIfEntry=zxr10EthPhyIfEntry, EthEncapsulationType=EthEncapsulationType, zxr10EthRecvPkts1024to1518Octects=zxr10EthRecvPkts1024to1518Octects, EthPhyFrameType=EthPhyFrameType, zxr10EthSndPktsUnder64Octects=zxr10EthSndPktsUnder64Octects, zxr10EthSndStatsTable=zxr10EthSndStatsTable, zxr10EthSubIfConfigParentIfIndex=zxr10EthSubIfConfigParentIfIndex, zxr10EthRecvPktsCRCError=zxr10EthRecvPktsCRCError, zxr10EthRecvClearCounts=zxr10EthRecvClearCounts, zxr10EthLoopBackIfName=zxr10EthLoopBackIfName, zxr10EthSubIfConfigRowStatus=zxr10EthSubIfConfigRowStatus, IfSpeedType=IfSpeedType, zxr10EthSubIfConfigSubIfIndex=zxr10EthSubIfConfigSubIfIndex, zxr10EthSubIfConfigVlanID=zxr10EthSubIfConfigVlanID, zxr10EthLoopBackTable=zxr10EthLoopBackTable, zxr10EthSndStatsIfIndex=zxr10EthSndStatsIfIndex, zxr10EthConfiguration=zxr10EthConfiguration, zxr10EthSubIfConfigParentIfName=zxr10EthSubIfConfigParentIfName, zxr10EthSndPkts512to1023Octects=zxr10EthSndPkts512to1023Octects, zxr10EthSndPkts1024to1518Octects=zxr10EthSndPkts1024to1518Octects, zxr10EthSubIfConfigEncapType=zxr10EthSubIfConfigEncapType, zxr10EthSndPkts255to511Octects=zxr10EthSndPkts255to511Octects, zxr10EthLoopBackNo=zxr10EthLoopBackNo, zxr10EthPhyIfTable=zxr10EthPhyIfTable, zxr10EthSndClearCounts=zxr10EthSndClearCounts, zxr10EthSubIfName=zxr10EthSubIfName, zxr10EthSubIfIndex=zxr10EthSubIfIndex, zxr10EthRecvStatsTable=zxr10EthRecvStatsTable, zxr10EthSubIfParentIfName=zxr10EthSubIfParentIfName, zxr10EthSubIfConfigSubIfName=zxr10EthSubIfConfigSubIfName, zxr10EthRecvPkts65to127Octects=zxr10EthRecvPkts65to127Octects, zxr10EthLoopBackRowStatus=zxr10EthLoopBackRowStatus, zxr10EthPhyIfSpeed=zxr10EthPhyIfSpeed, zxr10EthSubIfConfigEntry=zxr10EthSubIfConfigEntry, zxr10EthRecvPkts255to511Octects=zxr10EthRecvPkts255to511Octects, zxr10EthPhyIfNegotiation=zxr10EthPhyIfNegotiation, PYSNMP_MODULE_ID=zxr10EthMgtMIB, zxr10EthRecvPkts64Octects=zxr10EthRecvPkts64Octects, zxr10EthRecvStatsIfIndex=zxr10EthRecvStatsIfIndex, zxr10EthSndPkts128to255Octects=zxr10EthSndPkts128to255Octects, zxr10EthSndStatsEntry=zxr10EthSndStatsEntry, zxr10EthSndPkts65to127Octects=zxr10EthSndPkts65to127Octects, zxr10EthQuery=zxr10EthQuery, zxr10EthStats=zxr10EthStats, zxr10EthLoopBackEntry=zxr10EthLoopBackEntry, zxr10EthRecvPkts512to1023Octects=zxr10EthRecvPkts512to1023Octects, zxr10EthPhyIfMTU=zxr10EthPhyIfMTU, zxr10EthPhyIfFrameType=zxr10EthPhyIfFrameType, EthNegotiationType=EthNegotiationType, zxr10EthPhyWorkType=zxr10EthPhyWorkType, zxr10EthMgtMIBObjects=zxr10EthMgtMIBObjects, zxr10EthLoopBackIfIndex=zxr10EthLoopBackIfIndex, DisplayString=DisplayString, zxr10EthRecvStatsEntry=zxr10EthRecvStatsEntry)
