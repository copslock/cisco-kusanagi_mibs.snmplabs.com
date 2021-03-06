#
# PySNMP MIB module VPLS-GENERIC-DRAFT-01-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPLS-GENERIC-DRAFT-01-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
jnxExperiment, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, NotificationType, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, Counter32, TimeTicks, Counter64, MibIdentifier, IpAddress, ObjectIdentity, iso, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "Counter32", "TimeTicks", "Counter64", "MibIdentifier", "IpAddress", "ObjectIdentity", "iso", "Unsigned32", "Integer32")
DisplayString, TextualConvention, TruthValue, StorageType, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "StorageType", "RowStatus")
VPNIdOrZero, = mibBuilder.importSymbols("VPN-TC-STD-MIB", "VPNIdOrZero")
jnxVplsGenericDraft01MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 5, 8))
jnxVplsGenericDraft01MIB.setRevisions(('2011-03-26 12:00', '2006-08-30 12:00', '2006-06-04 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxVplsGenericDraft01MIB.setRevisionsDescriptions(('Removed inline definition of VPNIdOrZero in favor of importing the definition from VPN-TC-STD-MIB. ', 'Changes from previous version: 1) Moved LDP Specific information to VPLS-LDP-DRAFT-01-MIB 2) Created the vplsStatusTable to store status information. 3) ', 'Initial version published as part of RFC YYYY.',))
if mibBuilder.loadTexts: jnxVplsGenericDraft01MIB.setLastUpdated('201103261200Z')
if mibBuilder.loadTexts: jnxVplsGenericDraft01MIB.setOrganization('Layer 2 Virtual Private Networks (L2VPN) Working Group')
if mibBuilder.loadTexts: jnxVplsGenericDraft01MIB.setContactInfo(' Thomas D. Nadeau Email: tnadeau@cisco.com The L2VPN Working Group (email distribution l2vpn@ietf.org, http://www.ietf.org/html.charters/l2vpn-charter.html) ')
if mibBuilder.loadTexts: jnxVplsGenericDraft01MIB.setDescription('Copyright (C) The IETF Trust (2010). The initial version of this MIB module was published in RFC XXXX. -- RFC Editor: Please replace XXXX with RFC number & remove -- this note. For full legal notices see the RFC itself or see: http://www.ietf.org/copyrights/ianamib.html This MIB module contains generic managed object definitions for Virtual Private LAN Services as in [RFC4762] and [RFC4761] This MIB module enables the use of any underlying PseudoWire network.')
class PwIndexType(TextualConvention, Unsigned32):
    description = 'Pseudowire Index. A unique value, greater than zero, for each locally-defined PW for indexing several MIB tables associated with the particular PW. It is recommended that values are assigned contiguously starting from 1. The value for each PW MUST remain constant at least from one re-initialization to the next re-initialization. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class JnxVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = 'Syntax for a route distinguisher. For a complete definition of a route distinguisher, see [RFC4364]. For more details on use of a route distinguisher for a VPLS service, see [RFC4761]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class JnxVplsBgpRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = 'Syntax for a route target. For a complete definition of a route target, see [RFC4364].'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class JnxVplsBgpRouteTargetType(TextualConvention, Integer32):
    reference = '[RFC4364]'
    description = 'Used to define the type of a route target usage. Route targets can be specified to be imported, exported, or both. For a complete definition of a route target, see [RFC4364].'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

jnxVplsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 8, 0))
jnxVplsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1))
jnxVplsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 8, 2))
jnxVplsConfigIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigIndexNext.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigIndexNext.setDescription('This object contains an appropriate value to be used for jnxVplsConfigIndex when creating entries in the jnxVplsConfigTable. The value 0 indicates that no unassigned entries are available. To obtain the value of jnxVplsConfigIndex for a new entry in the jnxVplsConfigTable, the manager issues a management protocol retrieval operation to obtain the current value of jnxVplsConfigIndex. After each retrieval operation, the agent should modify the value to reflect the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse.')
jnxVplsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2), )
if mibBuilder.loadTexts: jnxVplsConfigTable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigTable.setDescription('This table specifies information for configuring and monitoring Virtual Private Lan Services(VPLS). ')
jnxVplsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1), ).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"))
if mibBuilder.loadTexts: jnxVplsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigEntry.setDescription('A row in this table represents a Virtual Private Lan Service(VPLS) in a packet network. It is indexed by jnxVplsConfigIndex, which uniquely identifies a single VPLS. A row is created by the operator or by the agent if a VPLS service is created by non-SNMP application or due to autodiscovery process. None of the read-create objects values can be changed when jnxVplsConfigRowStatus is in the active(1) state. Changes are allowed when the jnxVplsConfigRowStatus is in notInService(2) or notReady(3) states only. If the operator need to change one of the values for an active row the jnxVplsConfigRowStatus should be first changed to notInService(2), the objects may be changed now, and later to active(1) in order to re-initiate the signaling process with the new values in effect. ')
jnxVplsConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigIndex.setDescription('Unique index for the conceptual row identifying a VPLS service.')
jnxVplsConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigName.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigName.setDescription('A textual name of the VPLS. If there is no local name, or this object is otherwise not applicable, then this object MUST contain a zero-length octet string.')
jnxVplsConfigDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigDescr.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigDescr.setDescription('A textual string containing information about the VPLS service. If there is no information for this VPLS service, then this object MUST contain a zero-length octet string.')
jnxVplsConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigAdminStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigAdminStatus.setDescription('The desired administrative state of the VPLS service. If the administrative status of the Vpls service is changed to enable then this service is able to utilize the pseudo wire to perform the tasks of a VPLS service. The testing(3) state indicates that no operational packets can be passed. ')
jnxVplsConfigMacLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigMacLearning.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigMacLearning.setDescription('This object specifies if MAC Learning is enabled in this service. If this object is true then Mac Learning is enabled. If false, then Mac Learning is disabled.')
jnxVplsConfigDiscardUnknownDest = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigDiscardUnknownDest.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigDiscardUnknownDest.setDescription("If the value of this object is 'true', then frames received with an unknown destination MAC are discarded in this VPLS. If 'false', then the packets are processed.")
jnxVplsConfigMacAging = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 8), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigMacAging.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigMacAging.setDescription("If the value of this object is 'true' then the MAC ageing process is enabled in this VPLS. If 'false', then the MAC ageing process is disabled")
jnxVplsConfigFwdFullHighWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(95)).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigFwdFullHighWatermark.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigFwdFullHighWatermark.setDescription('This object specifies the utilization of the forwarding database for this VPLS instance at which the jnxVplsFwdFullAlarmRaised notification will be sent.')
jnxVplsConfigFwdFullLowWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(90)).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigFwdFullLowWatermark.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigFwdFullLowWatermark.setDescription('This object specifies the utilization of the forwarding database for this VPLS instance at which the jnxVplsFwdFullAlarmCleared notification will be sent.')
jnxVplsConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 12), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigRowStatus.setDescription('For creating, modifying, and deleting this row. None of the read-create objects in the conceptual rows may be changed when this object is in the active(1) state.')
jnxVplsConfigMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(64, 1518)).clone(1518)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigMtu.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigMtu.setDescription('The value of this object specifies the MTU of this vpls instance.')
jnxVplsConfigVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 14), VPNIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigVpnId.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigVpnId.setDescription('This objects indicates the IEEE 802-1990 VPN ID of the associated VPLS service.')
jnxVplsConfigServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("ethernet", 2))).clone('vlan')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigServiceType.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigServiceType.setDescription('The value of this object specifies the type of service emulated by this vpls instance.')
jnxVplsConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 16), StorageType().clone('volatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: jnxVplsConfigStorageType.setDescription('This variable indicates the storage type for this row.')
jnxVplsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3), )
if mibBuilder.loadTexts: jnxVplsStatusTable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsStatusTable.setDescription('This table provides information for monitoring Virtual Private Lan Services(VPLS). ')
jnxVplsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3, 1), ).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"))
if mibBuilder.loadTexts: jnxVplsStatusEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVplsStatusEntry.setDescription('A row in this table represents a Virtual Private Lan Service(VPLS) in a packet network. It is indexed by jnxVplsConfigIndex, which uniquely identifies a single VPLS. A row in this table is automatically created by the agent when a VPLS service is configured. ')
jnxVplsStatusOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("other", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsStatusOperStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVplsStatusOperStatus.setDescription('The current operational state of this VPLS Service.')
jnxVplsStatusPeerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsStatusPeerCount.setStatus('current')
if mibBuilder.loadTexts: jnxVplsStatusPeerCount.setDescription('This objects specifies the number of peers present in this vpls instance.')
jnxVplsPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4), )
if mibBuilder.loadTexts: jnxVplsPwBindTable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsPwBindTable.setDescription('This table provides an association between a VPLS service and the corresponding Pseudo Wires. A service can have more than one Pseudo Wire association. Pseudo Wires are defined in the pwTable')
jnxVplsPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1), ).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"), (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"))
if mibBuilder.loadTexts: jnxVplsPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVplsPwBindEntry.setDescription('Each row represents an association between a VPLS instance and one or more Pseudo Wires defined in the pwTable. Each index is unique in describing an entry in this table. However both indexes are required to define the one to many association of service to pseudowire.')
jnxVplsPwBindConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("autodiscovery", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsPwBindConfigType.setStatus('current')
if mibBuilder.loadTexts: jnxVplsPwBindConfigType.setDescription('The value of this object indicates whether the Pseudo Wire binding was created manually or via autodiscovery. The value of this object must be specifed when the row is created and cannot be changed while the row status is active(1)')
jnxVplsPwBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mesh", 1), ("spoke", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsPwBindType.setStatus('current')
if mibBuilder.loadTexts: jnxVplsPwBindType.setDescription('The value of this object indicates whether the Pseudo Wire binding is of type mesh or spoke. The value of this object must be specifed when the row is created and cannot be changed while the row status is active(1)')
jnxVplsPwBindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsPwBindRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVplsPwBindRowStatus.setDescription('For creating, modifying, and deleting this row. None of the read-create objects in the conceptual rows may be changed when this object is in the active(1) state')
jnxVplsPwBindStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 4), StorageType().clone('volatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsPwBindStorageType.setStatus('current')
if mibBuilder.loadTexts: jnxVplsPwBindStorageType.setDescription('This variable indicates the storage type for this row.')
jnxVplsPwBindIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 5), PwIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsPwBindIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVplsPwBindIndex.setDescription("Secondary Index for the conceptual row identifying a pseudowire within the PwEntry which MUST match an entry from the PW-STD-MIB's PwTable which represents an already-provisioned pseudowire that is then associated with this VPLS instance. ")
jnxVplsBgpADConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5), )
if mibBuilder.loadTexts: jnxVplsBgpADConfigTable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpADConfigTable.setDescription('This table specifies information for configuring BGP Auto-discovery parameters for a given Vpls service. ')
jnxVplsBgpADConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1), ).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"))
if mibBuilder.loadTexts: jnxVplsBgpADConfigEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpADConfigEntry.setDescription('A row in this table represents BGP based autodiscovery is in use for this instance of Vpls. A row in this table is indexed by jnxVplsConfigIndex, which uniquely identifies a single VPLS. None of the read-create objects can be changed when jnxVplsBGPADConfigRowStatus is in active(1) state. Changes are allowed when the jnxVplsBGPADConfigRowStatus is in notInService(2) or notReady(3) states only. If the operator need to change one of the values for an active row the jnxVplsConfigRowStatus should be first changed to notInService(2), the objects may be changed now, and later to active(1) in order to re-initiate the signaling process with the new values in effect. ')
jnxVplsBgpADConfigRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 1), JnxVplsBgpRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpADConfigRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpADConfigRouteDistinguisher.setDescription(' The route distinguisher for this VPLS. See [RFC4364] for a complete definition of a route distinguisher. for more details on use of a route distinguisher for a VPLS service, see [RFC4761] ')
jnxVplsBgpADConfigPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpADConfigPrefix.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpADConfigPrefix.setDescription(' In case of auto-discovery the default prefix advertised is the ip address of the loopback. In case the user wants to override the loopback address, jnxVplsBgpADConfigPrefix should be set. When this value if non-zero it is used as the advertised IP address in the NLRI. ')
jnxVplsBgpADConfigVplsId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 3), JnxVplsBgpRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpADConfigVplsId.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpADConfigVplsId.setDescription(' VplsId is a unique identifier for all VSIs belonging to the same VPLS. It is advertised as an extended community ')
jnxVplsBgpADConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpADConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpADConfigRowStatus.setDescription(' For creating, modifying, and deleting this row. None of the read-create objects in the conceptual rows may be changed when this object is in the active(1) state. ')
jnxVplsBgpRteTargetTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6), )
if mibBuilder.loadTexts: jnxVplsBgpRteTargetTable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpRteTargetTable.setDescription(' This table specifies the list of Route Targets imported or exported by BGP during auto-discovery of VPLS. ')
jnxVplsBgpRteTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1), ).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"), (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsBgpRteTargetIndex"))
if mibBuilder.loadTexts: jnxVplsBgpRteTargetEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpRteTargetEntry.setDescription('An entry in this table specifies the value of the Route Target being used by BGP. Depending on the value of jnxVplsBgpRteTargetType an RT might be exported or imported or both. Every VPLS which uses auto-discovery for finding peer nodes can import and export multiple Route Targets. This representation allows support for hierarchical VPLS. ')
jnxVplsBgpRteTargetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxVplsBgpRteTargetIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpRteTargetIndex.setDescription('This index along with jnxVplsConfigIndex,identifies one entry in the jnxVplsBgpRteTargetTable. By keeping jnxVplsConfigIndex constant and using new value of jnxVplsBgpRteTargetIndex user can configure multiple Route Targets for the same Vpls. ')
jnxVplsBgpRteTargetRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 2), JnxVplsBgpRouteTargetType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpRteTargetRTType.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpRteTargetRTType.setDescription(' Used to define the type of a route target usage. Route targets can be specified to be imported, exported, or both. For a complete definition of a route target, see [RFC4364]. ')
jnxVplsBgpRteTargetRT = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 3), JnxVplsBgpRouteTarget()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpRteTargetRT.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpRteTargetRT.setDescription(' The route target associated with the VPLS service. For more details on use of route targets for a VPLS service, see [RFC4761] ')
jnxVplsBgpRteTargetRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpRteTargetRTRowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxVplsBgpRteTargetRTRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table. When a row in this table is in active(1) state, no objects in that row can be modified ')
jnxVplsStatusNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jnxVplsStatusNotifEnable.setReference('See also [RFC3413] for explanation that notifications are under the ultimate control of the MIB module in this document.')
if mibBuilder.loadTexts: jnxVplsStatusNotifEnable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsStatusNotifEnable.setDescription('If this object is set to true(1), then it enables the emission of jnxVplsStatusChanged notification; otherwise this notification is not emitted.')
jnxVplsNotificationMaxRate = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jnxVplsNotificationMaxRate.setStatus('current')
if mibBuilder.loadTexts: jnxVplsNotificationMaxRate.setDescription('This object indicates the maximum number of notifications issued per second. If events occur more rapidly, the implementation may simply fail to emit these notifications during that period, or may queue them until an appropriate time. A value of 0 means no throttling is applied and events may be notified at the rate at which they occur.')
jnxVplsStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 8, 0, 1)).setObjects(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigVpnId"), ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigAdminStatus"), ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsStatusOperStatus"))
if mibBuilder.loadTexts: jnxVplsStatusChanged.setStatus('current')
if mibBuilder.loadTexts: jnxVplsStatusChanged.setDescription('The jnxVplsStatusChanged notification is generated when there is a change in the administrative or operating status of a VPLS service.')
jnxVplsFwdFullAlarmRaised = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 8, 0, 2)).setObjects(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigVpnId"), ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullHighWatermark"), ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullLowWatermark"))
if mibBuilder.loadTexts: jnxVplsFwdFullAlarmRaised.setStatus('current')
if mibBuilder.loadTexts: jnxVplsFwdFullAlarmRaised.setDescription('The jnxVplsFwdFullAlarmRaised notification is generated when the utilization of the Forwarding database is above the value specified by jnxVplsConfigFwdFullHighWatermark.')
jnxVplsFwdFullAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 8, 0, 3)).setObjects(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigVpnId"), ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullHighWatermark"), ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullLowWatermark"))
if mibBuilder.loadTexts: jnxVplsFwdFullAlarmCleared.setStatus('current')
if mibBuilder.loadTexts: jnxVplsFwdFullAlarmCleared.setDescription('The jnxVplsFwdFullAlarmCleared notification is generated when the utilization of the Forwarding database is below the value specified by jnxVplsConfigFwdFullLowWatermark.')
mibBuilder.exportSymbols("VPLS-GENERIC-DRAFT-01-MIB", jnxVplsPwBindTable=jnxVplsPwBindTable, jnxVplsPwBindIndex=jnxVplsPwBindIndex, jnxVplsFwdFullAlarmCleared=jnxVplsFwdFullAlarmCleared, jnxVplsConfigVpnId=jnxVplsConfigVpnId, jnxVplsConfigTable=jnxVplsConfigTable, jnxVplsBgpADConfigRowStatus=jnxVplsBgpADConfigRowStatus, jnxVplsConfigMtu=jnxVplsConfigMtu, jnxVplsPwBindEntry=jnxVplsPwBindEntry, JnxVplsBgpRouteTarget=JnxVplsBgpRouteTarget, PwIndexType=PwIndexType, jnxVplsPwBindConfigType=jnxVplsPwBindConfigType, jnxVplsBgpADConfigEntry=jnxVplsBgpADConfigEntry, jnxVplsConfigFwdFullLowWatermark=jnxVplsConfigFwdFullLowWatermark, jnxVplsConfigFwdFullHighWatermark=jnxVplsConfigFwdFullHighWatermark, jnxVplsStatusPeerCount=jnxVplsStatusPeerCount, jnxVplsStatusEntry=jnxVplsStatusEntry, JnxVplsBgpRouteTargetType=JnxVplsBgpRouteTargetType, jnxVplsBgpRteTargetRTType=jnxVplsBgpRteTargetRTType, jnxVplsStatusNotifEnable=jnxVplsStatusNotifEnable, PYSNMP_MODULE_ID=jnxVplsGenericDraft01MIB, jnxVplsStatusTable=jnxVplsStatusTable, jnxVplsNotifications=jnxVplsNotifications, jnxVplsConfigDiscardUnknownDest=jnxVplsConfigDiscardUnknownDest, jnxVplsBgpRteTargetTable=jnxVplsBgpRteTargetTable, jnxVplsConfigMacLearning=jnxVplsConfigMacLearning, jnxVplsBgpRteTargetRT=jnxVplsBgpRteTargetRT, jnxVplsBgpRteTargetEntry=jnxVplsBgpRteTargetEntry, jnxVplsConfigAdminStatus=jnxVplsConfigAdminStatus, jnxVplsConfigServiceType=jnxVplsConfigServiceType, jnxVplsStatusChanged=jnxVplsStatusChanged, jnxVplsNotificationMaxRate=jnxVplsNotificationMaxRate, jnxVplsBgpADConfigPrefix=jnxVplsBgpADConfigPrefix, jnxVplsConfigName=jnxVplsConfigName, jnxVplsPwBindStorageType=jnxVplsPwBindStorageType, jnxVplsFwdFullAlarmRaised=jnxVplsFwdFullAlarmRaised, jnxVplsConfigDescr=jnxVplsConfigDescr, jnxVplsConfigEntry=jnxVplsConfigEntry, jnxVplsBgpADConfigVplsId=jnxVplsBgpADConfigVplsId, jnxVplsPwBindRowStatus=jnxVplsPwBindRowStatus, jnxVplsConfigStorageType=jnxVplsConfigStorageType, jnxVplsPwBindType=jnxVplsPwBindType, jnxVplsConfigRowStatus=jnxVplsConfigRowStatus, jnxVplsStatusOperStatus=jnxVplsStatusOperStatus, jnxVplsBgpADConfigTable=jnxVplsBgpADConfigTable, jnxVplsBgpRteTargetIndex=jnxVplsBgpRteTargetIndex, jnxVplsGenericDraft01MIB=jnxVplsGenericDraft01MIB, jnxVplsConformance=jnxVplsConformance, jnxVplsObjects=jnxVplsObjects, jnxVplsConfigIndexNext=jnxVplsConfigIndexNext, jnxVplsConfigIndex=jnxVplsConfigIndex, jnxVplsBgpRteTargetRTRowStatus=jnxVplsBgpRteTargetRTRowStatus, JnxVplsBgpRouteDistinguisher=JnxVplsBgpRouteDistinguisher, jnxVplsBgpADConfigRouteDistinguisher=jnxVplsBgpADConfigRouteDistinguisher, jnxVplsConfigMacAging=jnxVplsConfigMacAging)
