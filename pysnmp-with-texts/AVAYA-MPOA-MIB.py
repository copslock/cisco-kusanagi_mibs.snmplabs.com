#
# PySNMP MIB module AVAYA-MPOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAYA-MPOA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
lsg, = mibBuilder.importSymbols("AVAYAGEN-MIB", "lsg")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, enterprises, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, IpAddress, Counter64, Bits, Counter32, NotificationType, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "enterprises", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Unsigned32", "Integer32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
atmAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4))
mpoa = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1))
mpoa.setRevisions(('1901-10-10 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mpoa.setRevisionsDescriptions(('Initial version of the AVAYA-MPOA-MIB.',))
if mibBuilder.loadTexts: mpoa.setLastUpdated('0110101700Z')
if mibBuilder.loadTexts: mpoa.setOrganization('Avaya Communications, Inc.')
if mibBuilder.loadTexts: mpoa.setContactInfo(' Technical Support Avaya Communications, Inc. Telephone from US: 800-237-0016 Telephone from North America: 1-800-242-2121')
if mibBuilder.loadTexts: mpoa.setDescription('The MIB module to implement RFC1483,MPOA/AAL5 protocol')
marconi = MibIdentifier((1, 3, 6, 1, 4, 1, 1012))
esrLsg = MibIdentifier((1, 3, 6, 1, 4, 1, 1012, 44))
class MpoaEnabledValue(TextualConvention, Integer32):
    description = 'Represents either enabled or disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class MpoaYesorNoValue(TextualConvention, Integer32):
    description = 'Represents either YES or NO.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

class MpoaOperValue(TextualConvention, Integer32):
    description = 'Represents the operational status of the vsp or link. The value of initial is used when the VSP/link was administratively enabled but the configuration is incorrect, and the VSP/ link cannot be activated.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("initial", 3))

class MpoaResourceId(TextualConvention, Integer32):
    description = 'Represents the resource id of either an MPOA link or PVC. Before creating a link or PVC, a valid resource id is obtained via GETs for variables in the mpoaResourceMgmtGroup. The resource id is one of the indicies in the mpoaAtmLinkTable and the mpoaPvcTable.'
    status = 'current'

mpoaResourceMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 1))
mpoaNextLinkResourceId = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaNextLinkResourceId.setStatus('current')
if mibBuilder.loadTexts: mpoaNextLinkResourceId.setDescription('This variable contains the next available Resource Id to be used when creating a link. Before creating a link, a GET of this variable must be requested. This value should be used in the mpoaAtmLinkIndex variable.')
mpoaNextPvcResourceId = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaNextPvcResourceId.setStatus('current')
if mibBuilder.loadTexts: mpoaNextPvcResourceId.setDescription('This variable contains the next available Resource Id to be used when creating a PVC. Before creating a PVC, a GET of this variable must be requested. This value should be used in mpoaPvcResIndex variable.')
mpoaVirtualSwitchPortTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2), )
if mibBuilder.loadTexts: mpoaVirtualSwitchPortTable.setStatus('current')
if mibBuilder.loadTexts: mpoaVirtualSwitchPortTable.setDescription('A table of all the VSPs created for aal5 traffic on the atm module. The maximum number of expected entries is 128.')
mpoaVirtualSwitchPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1), ).setIndexNames((0, "AVAYA-MPOA-MIB", "mpoaVspIndex"))
if mibBuilder.loadTexts: mpoaVirtualSwitchPortEntry.setStatus('current')
if mibBuilder.loadTexts: mpoaVirtualSwitchPortEntry.setDescription('An entry containing management information pertaining to an mpoa VSP.')
mpoaVspIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaVspIndex.setStatus('current')
if mibBuilder.loadTexts: mpoaVspIndex.setDescription('The VSP Id number in the range of 1 to 128.')
mpoaVspAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 2), MpoaEnabledValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mpoaVspAdminStatus.setDescription('This variable is used to administratively enable or disable the VSP. This variable must not be included with any other variables in a SET. To modify or delete the VSP, the admin state must first be changed to disable. Then a second PDU must be sent to handle the modify or delete.')
mpoaVspOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 3), MpoaOperValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaVspOperStatus.setStatus('current')
if mibBuilder.loadTexts: mpoaVspOperStatus.setDescription('This variable gives the operational status of the vsp. The value of initial is used when the VSP was administratively enabled but the configuration is incorrect, and the VSP cannot be activated.')
mpoaVspName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspName.setStatus('current')
if mibBuilder.loadTexts: mpoaVspName.setDescription('A unique 31-character ascii string used to name the VSP.')
mpoaVspEncapsulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("routed", 1), ("simpleBridge", 2), ("llcBridge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspEncapsulationType.setStatus('current')
if mibBuilder.loadTexts: mpoaVspEncapsulationType.setDescription('The type of packets used on this VSP.')
mpoaVspPktReplication = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 6), MpoaYesorNoValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspPktReplication.setStatus('current')
if mibBuilder.loadTexts: mpoaVspPktReplication.setDescription('This value can only be configured at the time of VSP creation. Packet replication simulates multi- casting by sending a single packet to a default VC that copies the packet to multiple PVCs. Choose yes only if there are multiple ATM links, with more than 1 remote destination.')
mpoaVspLoadShare = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 7), MpoaYesorNoValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspLoadShare.setStatus('current')
if mibBuilder.loadTexts: mpoaVspLoadShare.setDescription('This value should be yes if load-sharing is desired between PVCs. If load-sharing is desired, then both default PVCs should be configured for this VSP.')
mpoaVspDefaultPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspDefaultPort.setStatus('current')
if mibBuilder.loadTexts: mpoaVspDefaultPort.setDescription('This variable contains the preferred default port. In case of fail-over or load-sharing, this port is the primary port.')
mpoaVspDefaultVc_port1 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 9), MpoaResourceId()).setLabel("mpoaVspDefaultVc-port1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspDefaultVc_port1.setStatus('current')
if mibBuilder.loadTexts: mpoaVspDefaultVc_port1.setDescription('This variable is only applicable for non-replicating ports and should be ignored for replicating ports. This variable contains the pvc resource id of the primary default VC if the default physical port is port 1. It contains the pvc resource id of the secondary default VC if load-sharing or fail-over has been chosen and the default physical port is port 2. A secondary default VC must be configured if either load-sharing or fail-over has been chosen. The default VC is used to send packets with unknown unicast and broadcast destination MAC addresses.')
mpoaVspDefaultVc_port2 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 10), MpoaResourceId()).setLabel("mpoaVspDefaultVc-port2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspDefaultVc_port2.setStatus('current')
if mibBuilder.loadTexts: mpoaVspDefaultVc_port2.setDescription('This variable is only applicable for non-replicating ports and should be ignored for replicating ports. This variable contains the pvc resource id of the primary default VC if the default physical port is port 2. It contains the pvc resource id of the secondary default VC if load-sharing or fail-over has been chosen and the default physical port is port 1. A secondary default VC must be configured if either load-sharing or fail-over has been chosen.')
mpoaVspMulticastChan_port1 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 11), Integer32()).setLabel("mpoaVspMulticastChan-port1").setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaVspMulticastChan_port1.setStatus('current')
if mibBuilder.loadTexts: mpoaVspMulticastChan_port1.setDescription('This variable is only applicable for replicating ports and should be ignored for non-replicating ports. This variable contains the channel id of the primary default multicast channel if the default physical port is port 1. It contains the channel id of the secondary multicast channel if load-sharing or fail-over has been chosen and the default physical port is port 2.')
mpoaVspMulticastChan_port2 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 12), Integer32()).setLabel("mpoaVspMulticastChan-port2").setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaVspMulticastChan_port2.setStatus('current')
if mibBuilder.loadTexts: mpoaVspMulticastChan_port2.setDescription('This variable is only applicable for replicating ports and should be ignored for non-replicating ports. This variable contains the channel id of the primary default multicast channel if the default physical port is port 2. It contains the channel id of the secondary multicast channel if load-sharing or fail-over has been chosen and the default physical port is port 1.')
mpoaVspRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 2, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaVspRowStatus.setStatus('current')
if mibBuilder.loadTexts: mpoaVspRowStatus.setDescription('This variable is included with every SET PDU to indicate whether the SET PDU contains a create or delete transaction type.')
mpoaAtmLinkTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3), )
if mibBuilder.loadTexts: mpoaAtmLinkTable.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkTable.setDescription('A table of all the ATM links created for MPOA traffic on the ATM module. The maximum number of expected entries is 16k.')
mpoaAtmLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1), ).setIndexNames((0, "AVAYA-MPOA-MIB", "mpoaAtmLinkVspIndex"), (0, "AVAYA-MPOA-MIB", "mpoaAtmLinkIndex"))
if mibBuilder.loadTexts: mpoaAtmLinkEntry.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkEntry.setDescription('An entry containing management information pertaining to an mpoa ATM Link. This table is doubly- indexed by the VSP id (index) and the link id (index).')
mpoaAtmLinkVspIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaAtmLinkVspIndex.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkVspIndex.setDescription('Index of the VSP that this link is associated with.')
mpoaAtmLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 2), MpoaResourceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaAtmLinkIndex.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkIndex.setDescription('The ATM link id number. This variable comprises the second index in the link row entry. To get a valid link index, application must first get value of mpoaNextLinkResourceId, before creating a new entry.')
mpoaAtmLinkAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 3), MpoaEnabledValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkAdminStatus.setDescription('This variable is used to administratively enable or disable the link. This variable must not be included with any other variables in a SET. To modify or delete the link, the admin state must first be changed to disable. Then a second PDU must be sent to handle the modify or delete.')
mpoaAtmLinkOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 4), MpoaOperValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaAtmLinkOperStatus.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOperStatus.setDescription('This variable gives the operational status of the link. The value of initial is used when the link was administratively enabled but the configuration is incorrect, and the link cannot be activated.')
mpoaAtmLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkName.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkName.setDescription('A unique 31-character ascii string used to name the link.')
mpoaAtmLinkDefaultVc = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 6), MpoaResourceId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkDefaultVc.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkDefaultVc.setDescription('Index of the PVC to be used as the default channel for broadcast destination and unicast traffic. Not valid to set if the VSP is a non-replicating port.')
mpoaAtmLinkFailOverLink = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 8), MpoaResourceId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkFailOverLink.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkFailOverLink.setDescription('This variable contains the link id (link resource id) of the link to be used for fail over mode. This variable must not be set unless fail over mode is desired. The fail over link must have PVCs that are associated with another physical port, not the default port.')
mpoaAtmLinkOutPriority_0 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 9), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-0").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_0.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_0.setDescription('This variable contains the PVC Resource id (index) of the PVC assigned to outbound priority level 0. In total, there are 8 priority levels and 8 PVCs to be assigned. The same PVC can be specified for all levels.')
mpoaAtmLinkOutPriority_1 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 10), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_1.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_1.setDescription('This variable contains the PVC resource id (index) of the PVC assigned to outbound priority level 1.')
mpoaAtmLinkOutPriority_2 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 11), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_2.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_2.setDescription('This variable contains the PVC resource id (index) of the PVC assigned to outbound priority level 2.')
mpoaAtmLinkOutPriority_3 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 12), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_3.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_3.setDescription('This variable contains the PVC resource id (index) of the PVC assigned to outbound priority level 3.')
mpoaAtmLinkOutPriority_4 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 13), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-4").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_4.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_4.setDescription('This variable contains the PVC resource id (index) of the PVC assigned to outbound priority level 4.')
mpoaAtmLinkOutPriority_5 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 14), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-5").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_5.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_5.setDescription('This variable contains the PVC resource id (index) of the PVC assigned to outbound priority level 5.')
mpoaAtmLinkOutPriority_6 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 15), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-6").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_6.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_6.setDescription('This variable contains the PVC resource id (index) of the PVC assigned to outbound priority level 6.')
mpoaAtmLinkOutPriority_7 = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 16), MpoaResourceId()).setLabel("mpoaAtmLinkOutPriority-7").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_7.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkOutPriority_7.setDescription('This variable contains the PVC resource id (index) of the PVC assigned to outbound priority level 7.')
mpoaAtmLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 3, 1, 17), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaAtmLinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: mpoaAtmLinkRowStatus.setDescription('This variable is included with every SET PDU to indicate whether the SET PDU contains a create or delete transaction type.')
mpoaPvcTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4), )
if mibBuilder.loadTexts: mpoaPvcTable.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcTable.setDescription('A table of all the PVCs created for MPOA traffic on the ATM module. The maximum number of expected entries is 128k.')
mpoaPvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1), ).setIndexNames((0, "AVAYA-MPOA-MIB", "mpoaPvcVspIndex"), (0, "AVAYA-MPOA-MIB", "mpoaPvcLinkIndex"), (0, "AVAYA-MPOA-MIB", "mpoaPvcResIndex"))
if mibBuilder.loadTexts: mpoaPvcEntry.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcEntry.setDescription('An entry containing management information pertaining to an MPOA PVC. This table has 3 indicies: vsp id, link id and resource id.')
mpoaPvcVspIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaPvcVspIndex.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcVspIndex.setDescription('Index of the VSP that this link and PVC is associated with.')
mpoaPvcLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 2), MpoaResourceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaPvcLinkIndex.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcLinkIndex.setDescription('The Link Id number of the link associated with this PVC.')
mpoaPvcResIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 3), MpoaResourceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpoaPvcResIndex.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcResIndex.setDescription('The Resource Id associated with the PVC. It is associated with a port,vpi, and vci. Resource Ids are re-assigned each time the switch is re-booted. To get a valid resource id, application must first get value of mpoaNextPvcResourceId, before creating a new entry.')
mpoaPvcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcPort.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcPort.setDescription('Physical port that this PVC is associated with. This variable is only modifiable at CREATE time.')
mpoaPvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcVpi.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcVpi.setDescription('The PVC virtual path identifier(VPI). Must be unique among all VPIs configured for the ATM module. This variable is only modifiable at CREATE time.')
mpoaPvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcVci.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcVci.setDescription('The PVC virtual circuit identifier(VCI). Must be unique among all VCIs configured for the ATM module. This variable is only modifiable at CREATE time.')
mpoaPvcInPriorityMap = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcInPriorityMap.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcInPriorityMap.setDescription('The inbound priority map is the priority to be assigned to frames received on this PVC as they are passed on to the local VLAN segment.')
mpoaPvcTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ubr", 1), ("rtVbr", 2), ("nrtVbr", 3), ("cbr", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcTrafficClass.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcTrafficClass.setDescription('The assigned service category for the PVC. This variable is only modifiable at CREATE time.')
mpoaPvcCDVT = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcCDVT.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcCDVT.setDescription('Cell Delay Variation Tolerance.')
mpoaPvcPCR = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1412830))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcPCR.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcPCR.setDescription('Peak cell rate in cells per second.')
mpoaPvcSCR = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1412830))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcSCR.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcSCR.setDescription('Sustainable cell rate in cells per second. Ignored for UBR and CBR.')
mpoaPvcMBS = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 1048576))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcMBS.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcMBS.setDescription('Maximum Burst Size.')
mpoaPvcRandomEarlyDetPktId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcRandomEarlyDetPktId.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcRandomEarlyDetPktId.setDescription('Random Early Detection Packet Id.')
mpoaPvcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 4, 1, 14), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpoaPvcRowStatus.setStatus('current')
if mibBuilder.loadTexts: mpoaPvcRowStatus.setDescription('This variable must be included with every SET PDU to indicate whether the PDU contains a CREATE, DELETE, or MODIFY transaction type.')
mpoaTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5))
mpoaVspId = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mpoaVspId.setStatus('current')
if mibBuilder.loadTexts: mpoaVspId.setDescription('Used in the mpoaTrapLinkChange trap. Index of the VSP that the trap represents. If the link Id is non-zero than the vspId is the Id of the VSP associated with the link whose operational state has changed. If the link Id is zero, then the vspId represents the VSP whose operational state has changed.')
mpoaLinkId = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 2), MpoaResourceId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mpoaLinkId.setStatus('current')
if mibBuilder.loadTexts: mpoaLinkId.setDescription('Used in the mpoaTrapLinkChange trap. Index of the link that the trap represents. If the link Id is non-zero than it is the Id of the link whose operational state has changed. If the link Id is zero, then it should be ignored.')
mpoaOperState = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 3), MpoaOperValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mpoaOperState.setStatus('current')
if mibBuilder.loadTexts: mpoaOperState.setDescription('This variable gives the operational status of the link or VSP. The value of initial is used when the link/VSP was administratively enabled but the configuration is incorrect, and the link/VSP cannot be activated.')
mpoaTrapLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 4, 1, 5, 4)).setObjects(("AVAYA-MPOA-MIB", "mpoaVspId"), ("AVAYA-MPOA-MIB", "mpoaLinkId"), ("AVAYA-MPOA-MIB", "mpoaOperState"))
if mibBuilder.loadTexts: mpoaTrapLinkChange.setStatus('current')
if mibBuilder.loadTexts: mpoaTrapLinkChange.setDescription('A mpoaTrapLinkChange trap is generated when a VSP or ATM link changes operational state.')
mibBuilder.exportSymbols("AVAYA-MPOA-MIB", mpoaPvcVci=mpoaPvcVci, mpoaVspId=mpoaVspId, mpoaAtmLinkVspIndex=mpoaAtmLinkVspIndex, mpoaPvcVspIndex=mpoaPvcVspIndex, mpoaAtmLinkTable=mpoaAtmLinkTable, mpoaResourceMgmtGroup=mpoaResourceMgmtGroup, mpoaVspRowStatus=mpoaVspRowStatus, mpoaPvcInPriorityMap=mpoaPvcInPriorityMap, mpoaAtmLinkOutPriority_3=mpoaAtmLinkOutPriority_3, mpoa=mpoa, mpoaPvcPort=mpoaPvcPort, mpoaAtmLinkOutPriority_2=mpoaAtmLinkOutPriority_2, mpoaVspLoadShare=mpoaVspLoadShare, esrLsg=esrLsg, mpoaAtmLinkFailOverLink=mpoaAtmLinkFailOverLink, PYSNMP_MODULE_ID=mpoa, mpoaVspDefaultPort=mpoaVspDefaultPort, mpoaVspMulticastChan_port1=mpoaVspMulticastChan_port1, mpoaAtmLinkOperStatus=mpoaAtmLinkOperStatus, mpoaPvcEntry=mpoaPvcEntry, mpoaAtmLinkRowStatus=mpoaAtmLinkRowStatus, mpoaNextLinkResourceId=mpoaNextLinkResourceId, mpoaPvcVpi=mpoaPvcVpi, mpoaPvcRandomEarlyDetPktId=mpoaPvcRandomEarlyDetPktId, mpoaOperState=mpoaOperState, mpoaVspAdminStatus=mpoaVspAdminStatus, mpoaVspMulticastChan_port2=mpoaVspMulticastChan_port2, MpoaOperValue=MpoaOperValue, mpoaVspName=mpoaVspName, mpoaPvcPCR=mpoaPvcPCR, mpoaLinkId=mpoaLinkId, mpoaVirtualSwitchPortTable=mpoaVirtualSwitchPortTable, mpoaAtmLinkOutPriority_4=mpoaAtmLinkOutPriority_4, mpoaVspPktReplication=mpoaVspPktReplication, mpoaAtmLinkDefaultVc=mpoaAtmLinkDefaultVc, mpoaVspEncapsulationType=mpoaVspEncapsulationType, mpoaAtmLinkOutPriority_7=mpoaAtmLinkOutPriority_7, mpoaPvcResIndex=mpoaPvcResIndex, mpoaNextPvcResourceId=mpoaNextPvcResourceId, mpoaVspIndex=mpoaVspIndex, mpoaAtmLinkOutPriority_0=mpoaAtmLinkOutPriority_0, mpoaAtmLinkOutPriority_6=mpoaAtmLinkOutPriority_6, marconi=marconi, mpoaPvcTrafficClass=mpoaPvcTrafficClass, mpoaPvcRowStatus=mpoaPvcRowStatus, MpoaEnabledValue=MpoaEnabledValue, mpoaPvcLinkIndex=mpoaPvcLinkIndex, mpoaAtmLinkAdminStatus=mpoaAtmLinkAdminStatus, mpoaPvcMBS=mpoaPvcMBS, mpoaAtmLinkEntry=mpoaAtmLinkEntry, mpoaPvcSCR=mpoaPvcSCR, mpoaPvcTable=mpoaPvcTable, mpoaAtmLinkOutPriority_1=mpoaAtmLinkOutPriority_1, mpoaAtmLinkName=mpoaAtmLinkName, mpoaTrapLinkChange=mpoaTrapLinkChange, mpoaTraps=mpoaTraps, mpoaVspDefaultVc_port2=mpoaVspDefaultVc_port2, mpoaVspDefaultVc_port1=mpoaVspDefaultVc_port1, MpoaYesorNoValue=MpoaYesorNoValue, MpoaResourceId=MpoaResourceId, mpoaAtmLinkOutPriority_5=mpoaAtmLinkOutPriority_5, mpoaVspOperStatus=mpoaVspOperStatus, mpoaPvcCDVT=mpoaPvcCDVT, mpoaAtmLinkIndex=mpoaAtmLinkIndex, mpoaVirtualSwitchPortEntry=mpoaVirtualSwitchPortEntry, atmAccess=atmAccess)
