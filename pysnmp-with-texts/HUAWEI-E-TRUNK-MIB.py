#
# PySNMP MIB module HUAWEI-E-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-E-TRUNK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:44:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
huaweiMgmt, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, iso, MibIdentifier, IpAddress, Integer32, Gauge32, NotificationType, Bits, Counter64, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "MibIdentifier", "IpAddress", "Integer32", "Gauge32", "NotificationType", "Bits", "Counter64", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString, TimeStamp, TruthValue, RowStatus, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "TruthValue", "RowStatus", "PhysAddress")
hwETrunkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178))
if mibBuilder.loadTexts: hwETrunkMIB.setLastUpdated('200810211010Z')
if mibBuilder.loadTexts: hwETrunkMIB.setOrganization('Organization.')
if mibBuilder.loadTexts: hwETrunkMIB.setContactInfo('Contact-info.')
if mibBuilder.loadTexts: hwETrunkMIB.setDescription('Description.')
hwDatacomm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25))
hwETrunkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1))
hwETrunkTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1), )
if mibBuilder.loadTexts: hwETrunkTable.setStatus('current')
if mibBuilder.loadTexts: hwETrunkTable.setDescription('The E-Trunk table.')
hwETrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1), ).setIndexNames((0, "HUAWEI-E-TRUNK-MIB", "hwETrunkId"))
if mibBuilder.loadTexts: hwETrunkEntry.setStatus('current')
if mibBuilder.loadTexts: hwETrunkEntry.setDescription('E-Trunk entry.')
hwETrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hwETrunkId.setStatus('current')
if mibBuilder.loadTexts: hwETrunkId.setDescription('The index of the E-Trunk.')
hwETrunkSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkSystemId.setStatus('current')
if mibBuilder.loadTexts: hwETrunkSystemId.setDescription('The system ID of the E-Trunk. It is a physical address.')
hwETrunkPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkPri.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPri.setDescription('The priority of the E-Trunk. The default value is 100.')
hwETrunkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkStatus.setStatus('current')
if mibBuilder.loadTexts: hwETrunkStatus.setDescription('The status of the E-Trunk. 1:initialize. 2:backup. 3:master. ')
hwETrunkStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("pri", 1), ("timeout", 2), ("bfdDown", 3), ("peerTimeout", 4), ("peerBfdDown", 5), ("allMemberDown", 6), ("init", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkStatusReason.setStatus('current')
if mibBuilder.loadTexts: hwETrunkStatusReason.setDescription('The reason for the E-Trunk being in the current status. pri(1):Priority calculation. timeout(2):The receiving timer timed out. bfdDown(3):BFD detected the control link between the PE and peer down. peerTimeout(4):The receiving timer of the peer timed out. peerBfdDown(5):BFD of the peer detected the control link between the PE and peer down. allMemberDown(6):All members of the E-Trunk were down. init(7):Initiated the E-Trunk. ')
hwETrunkPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkPeerIpAddr.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPeerIpAddr.setDescription('The peer IP address of the E-Trunk.')
hwETrunkSourceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSourceIpAddr.setStatus('current')
if mibBuilder.loadTexts: hwETrunkSourceIpAddr.setDescription('The source IP address of the E-Trunk.')
hwETrunkReceiveFailTimeMultiple = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 300))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkReceiveFailTimeMultiple.setStatus('current')
if mibBuilder.loadTexts: hwETrunkReceiveFailTimeMultiple.setDescription('The detection time multiplier for failure detection. It is the multiple of the sending period.')
hwETrunkSendPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSendPeriod.setStatus('current')
if mibBuilder.loadTexts: hwETrunkSendPeriod.setDescription('The period for sending packets of the E-Trunk. The unit is 100ms. ')
hwETrunkPacketReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketReceive.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPacketReceive.setDescription('The number of received packets.')
hwETrunkPacketSend = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketSend.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPacketSend.setDescription('The number of sent packets.')
hwETrunkPacketRecDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketRecDrop.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPacketRecDrop.setDescription('The number of the dropped packets when the packets are received.')
hwETrunkPacketSndDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketSndDrop.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPacketSndDrop.setDescription('The number of the dropped packets when the packets are sent.')
hwETrunkPeerSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 14), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPeerSystemId.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPeerSystemId.setDescription('The system ID of the peer E-Trunk. It is a physical address.')
hwETrunkPeerPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPeerPri.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPeerPri.setDescription('The priority of the peer E-Trunk.')
hwETrunkPeerReceiveFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPeerReceiveFailTime.setStatus('current')
if mibBuilder.loadTexts: hwETrunkPeerReceiveFailTime.setDescription('The failure time for the peer E-Trunk to receive packets. The unit is 100ms. ')
hwETrunkSecurityKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSecurityKeyType.setStatus('current')
if mibBuilder.loadTexts: hwETrunkSecurityKeyType.setDescription('The type of the security key. 1:The simple encrypt type. 2:The cipher encrypt type. ')
hwETrunkSecurityKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 392))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSecurityKey.setStatus('current')
if mibBuilder.loadTexts: hwETrunkSecurityKey.setDescription('This object can be set to a simple password with a string of 0 to 255 characters or a encrypted password with a string less than 392 characters. For security purposes, a get on this returns a zero length string.')
hwETrunkBfdSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkBfdSessId.setStatus('current')
if mibBuilder.loadTexts: hwETrunkBfdSessId.setDescription("The ID of a BFD session which is bound to the E-Trunk. When the status of the BFD session is changed, the status of the E-Trunk is also changed with BFD's status.")
hwETrunkResetCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkResetCounter.setStatus('current')
if mibBuilder.loadTexts: hwETrunkResetCounter.setDescription('Reset hwETrunkPacketReceive,hwETrunkPacketSend,hwETrunkPacketRecDrop,hwETrunkPacketSndDrop.')
hwETrunkRevertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkRevertTime.setStatus('current')
if mibBuilder.loadTexts: hwETrunkRevertTime.setDescription('The delay time to revert. The unit is second. The default is 120. ')
hwETrunkBfdSessName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkBfdSessName.setStatus('current')
if mibBuilder.loadTexts: hwETrunkBfdSessName.setDescription("The name of a BFD session which is bound to the E-Trunk. And BFD session name is composed of octet string which is 1 to 15 octet and can't contain space within it. When the status of the BFD session is changed, the status of the E-Trunk is also changed with BFD's status.")
hwETrunkDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 23), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 242))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkDescription.setStatus('current')
if mibBuilder.loadTexts: hwETrunkDescription.setDescription('The description of the E-Trunk. The default is NULL')
hwETrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwETrunkRowStatus.setDescription('Current operation status of the row. It is used to manage the creation and deletion of conceptual rows.')
hwETrunkMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2), )
if mibBuilder.loadTexts: hwETrunkMemberTable.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberTable.setDescription('The member table of the E-Trunk.')
hwETrunkMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1), ).setIndexNames((0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberParentId"), (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberType"), (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberId"))
if mibBuilder.loadTexts: hwETrunkMemberEntry.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberEntry.setDescription('Member Entry.')
hwETrunkMemberParentId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hwETrunkMemberParentId.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberParentId.setDescription('The ID of the E-Trunk to which the member belongs.')
hwETrunkMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hwETrunkMemberType.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberType.setDescription('The type of the member. Now it is Eth-Trunk only. 1:EthTrunk')
hwETrunkMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: hwETrunkMemberId.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberId.setDescription('The ID of the member.')
hwETrunkMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkMemberStatus.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberStatus.setDescription('The member status. 1:backup. 2:master. ')
hwETrunkMemberStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("forceBackup", 1), ("forceMaster", 2), ("etrunkInit", 3), ("etrunkBackup", 4), ("etrunkMaster", 5), ("peerMemberDown", 6), ("peerMemberUp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkMemberStatusReason.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberStatusReason.setDescription('The reason for the member being in the current status. forceBackup(1):The work mode of the member is force-backup. forceMaster(2):The work mode of the member is force-master. etrunkInit(3):The work mode of the member is auto. The status of E-Trunk is initialize. etrunkBackup(4):The work mode of the member is auto. The status of E-Trunk is backup. etrunkMaster(5):The work mode of the member is auto. The status of E-Trunk is master. peerMemberDown(6):The status of the member belonging to the peer E-Trunk is down. peerMemberUp(7):The status of the member belonging to the peer E-Trunk is up. ')
hwETrunkMemberWorkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("forceBackup", 2), ("forceMaster", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkMemberWorkMode.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberWorkMode.setDescription('The work mode of the member. 1:auto. 2:forceBackup. 3:forceMaster. ')
hwETrunkMemberPhyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkMemberPhyStatus.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberPhyStatus.setDescription('The physical status of the member. 1:up. 2:down. ')
hwETrunkMemberRemoteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkMemberRemoteId.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberRemoteId.setDescription('Indicates the ID of a remote E-Trunk member. By default, the ID of a remote E-Trunk member is the same as the ID of the local E-Trunk member. When both ends have E-Trunk member with different IDs, you need to specify the ID of a remote E-Trunk member.')
hwETrunkMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberRowStatus.setDescription('Current operation status of the row. It is used to manage the creation and deletion of conceptual rows.')
hwETrunkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2))
hwETrunkStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 1)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusReason"))
if mibBuilder.loadTexts: hwETrunkStatusChange.setStatus('current')
if mibBuilder.loadTexts: hwETrunkStatusChange.setDescription('The trap is generated when the status of the E-Trunk is changed or the status reason of the E-Trunk is changed.')
hwETrunkMemberStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 2)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusReason"))
if mibBuilder.loadTexts: hwETrunkMemberStatusChange.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberStatusChange.setDescription('The trap is generated when the status of the memeber is changed or the status reason of the memeber is changed.')
hwETrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3))
hwETrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1))
hwETrunkFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1, 1)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkGroup"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberGroup"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkFullCompliance = hwETrunkFullCompliance.setStatus('current')
if mibBuilder.loadTexts: hwETrunkFullCompliance.setDescription('Description.')
hwETrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2))
hwETrunkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 1)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkSystemId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPri"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusReason"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerIpAddr"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSourceIpAddr"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkReceiveFailTimeMultiple"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSendPeriod"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketReceive"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketSend"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketRecDrop"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketSndDrop"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerSystemId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerPri"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerReceiveFailTime"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSecurityKeyType"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSecurityKey"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkBfdSessId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkResetCounter"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkRevertTime"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkBfdSessName"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkDescription"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkGroup = hwETrunkGroup.setStatus('current')
if mibBuilder.loadTexts: hwETrunkGroup.setDescription('Description.')
hwETrunkMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 2)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusReason"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberWorkMode"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberPhyStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberRemoteId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkMemberGroup = hwETrunkMemberGroup.setStatus('current')
if mibBuilder.loadTexts: hwETrunkMemberGroup.setDescription('Description.')
hwETrunkNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 3)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusChange"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkNotificationGroup = hwETrunkNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwETrunkNotificationGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-E-TRUNK-MIB", hwETrunkId=hwETrunkId, hwETrunkNotificationGroup=hwETrunkNotificationGroup, hwETrunkStatus=hwETrunkStatus, hwETrunkMemberWorkMode=hwETrunkMemberWorkMode, hwETrunkDescription=hwETrunkDescription, hwETrunkMemberEntry=hwETrunkMemberEntry, hwETrunkPeerReceiveFailTime=hwETrunkPeerReceiveFailTime, hwETrunkStatusReason=hwETrunkStatusReason, hwETrunkGroups=hwETrunkGroups, hwETrunkPacketRecDrop=hwETrunkPacketRecDrop, hwETrunkMemberTable=hwETrunkMemberTable, hwETrunkSourceIpAddr=hwETrunkSourceIpAddr, hwETrunkMIB=hwETrunkMIB, hwETrunkPeerPri=hwETrunkPeerPri, PYSNMP_MODULE_ID=hwETrunkMIB, hwETrunkStatusChange=hwETrunkStatusChange, hwETrunkMemberGroup=hwETrunkMemberGroup, hwETrunkSystemId=hwETrunkSystemId, hwETrunkTable=hwETrunkTable, hwETrunkSecurityKey=hwETrunkSecurityKey, hwETrunkMemberRowStatus=hwETrunkMemberRowStatus, hwETrunkReceiveFailTimeMultiple=hwETrunkReceiveFailTimeMultiple, hwDatacomm=hwDatacomm, hwETrunkSecurityKeyType=hwETrunkSecurityKeyType, hwETrunkPri=hwETrunkPri, hwETrunkMemberStatusReason=hwETrunkMemberStatusReason, hwETrunkBfdSessName=hwETrunkBfdSessName, hwETrunkGroup=hwETrunkGroup, hwETrunkObjects=hwETrunkObjects, hwETrunkPacketSndDrop=hwETrunkPacketSndDrop, hwETrunkRowStatus=hwETrunkRowStatus, hwETrunkConformance=hwETrunkConformance, hwETrunkMemberStatusChange=hwETrunkMemberStatusChange, hwETrunkTraps=hwETrunkTraps, hwETrunkBfdSessId=hwETrunkBfdSessId, hwETrunkMemberId=hwETrunkMemberId, hwETrunkPeerIpAddr=hwETrunkPeerIpAddr, hwETrunkMemberPhyStatus=hwETrunkMemberPhyStatus, hwETrunkPeerSystemId=hwETrunkPeerSystemId, hwETrunkMemberStatus=hwETrunkMemberStatus, hwETrunkCompliances=hwETrunkCompliances, hwETrunkFullCompliance=hwETrunkFullCompliance, hwETrunkSendPeriod=hwETrunkSendPeriod, hwETrunkPacketSend=hwETrunkPacketSend, hwETrunkMemberParentId=hwETrunkMemberParentId, hwETrunkRevertTime=hwETrunkRevertTime, hwETrunkMemberType=hwETrunkMemberType, hwETrunkResetCounter=hwETrunkResetCounter, hwETrunkEntry=hwETrunkEntry, hwETrunkMemberRemoteId=hwETrunkMemberRemoteId, hwETrunkPacketReceive=hwETrunkPacketReceive)
