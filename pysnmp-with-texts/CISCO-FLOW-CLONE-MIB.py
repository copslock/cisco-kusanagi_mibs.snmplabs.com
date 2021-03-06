#
# PySNMP MIB module CISCO-FLOW-CLONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FLOW-CLONE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Gauge32, Integer32, ObjectIdentity, IpAddress, Bits, Counter32, MibIdentifier, iso, TimeTicks, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Gauge32", "Integer32", "ObjectIdentity", "IpAddress", "Bits", "Counter32", "MibIdentifier", "iso", "TimeTicks", "ModuleIdentity", "NotificationType")
TextualConvention, RowStatus, DisplayString, TimeStamp, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TimeStamp", "StorageType")
ciscoFlowCloneMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 765))
ciscoFlowCloneMIB.setRevisions(('2010-07-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFlowCloneMIB.setRevisionsDescriptions(('Added: The initial version of the MIB module',))
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setLastUpdated('201010190000Z')
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setDescription("This MIB module defines objects that manages flow cloning feature. A flow cloning can be described as a hardware or software entity, that is responsible to clone (or duplicate) flows to the specified destination port in the device. These cloned packets will be sent to an external device for a more fine-grained analysis of the flows. A typical application of this MIB module will facilitate cloning media flows. However, by no means does the definition of this MIB module prevents other applications from using it. CLONE PROFILE: ============== At the top level, this MIB module describes the notion of flow cloning. Further descriptive texts in this MIB will use clone profile to describe flow cloning. We can think of clone profile as a container for the traffic flows for which it will clone packets and send out on the specified egress interface. Because a device can support more than one clone profile, this MIB defines cfcCloneProfileTable. TRAFFIC FLOW: ============= At the next level, this MIB module describes the notion of a traffic flow associated with the clone profile. A traffic flow is a unidirectional stream of packets conforming to a classifier.For example, packets having a particular source IP address, destination IP address, protocol type, source port number, and destination port number. CLONE TARGET: ============= A clone target may represent an entity that the system provisions with a clone profile. Clone targets include, but are not necessarily limited to, the system, nodes (i.e., an instance of an operating system), interfaces, VRF instances, and bridge domains. IMPLEMENTATION GUIDANCE ======================= It might seem that the concepts presented by this MIB module lend themselves to a profile-based approach. However, this approach provides the most general abstraction and lends itself to implementations that can fall under two categories: global and per-interface. A global level clone profile will clone the specified flows that are monitored in the whole device. Per interface clone profile will clone the specified flows that are monitored on the specified interface. This MIB module can represent the global level clone profile using the following procedure: o Create a row in the cfcCloneProfileTable having the following attributes. Allocate a value for cfcCloneProfileId and a name for cfcCloneProfileName. For sake of discussion, let's say the value is <X> and the name is 'XYZ'. cfcCloneProfileId = <X> cfcCloneProfileName = <XYZ> . . cfcCloneTargetType = 'system' o Similarly per interface level clone profile implementation can be represented as follows. Create a row in the cfcCloneProfileTable having the following attributes. Allocate a value for cfcCloneProfileId and a name for cfcCloneProfileName. For sake of discussion, let's say the value is <Y> and the name is 'ABC'. cfcCloneProfileId = <Y> cfcCloneProfileName = <ABC> . . cfcCloneTargetType = 'interface' cfcCloneTargetIfIndex = <ifindex> While this example illustrates how an implementation may represent global and per-interface configuration data, it is understood that an implementation may have other requirements. In these cases, use this example as a guide in satisfying these requirements.")
ciscoFlowCloneMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 0))
ciscoFlowCloneMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1))
ciscoFlowCloneMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2))
class CloneProfileIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value that uniquely identifies a clone profile.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CloneFlowIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value that uniquely identifies a traffic flow which is associated to a corresponding clone profile.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CloneProfilePointType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    description = "This textual convention represents a point at which a clone profile sends out the cloned flows: 'other' The implementation of the MIB module using this textual convention does not recognize the profile point. 'unknown' The device is unable to ascertain the point at which the clone profile is sending the cloned traffic flow out. 'none' There is no point at which the clone profile can send cloned flows out. 'interface' The profile point is an interface represented by a row in the ifTable (defined by the IF-MIB [RFC2863]. With the exception of the values 'unknown' and 'none', each definition of a concrete CloneProfilePointType value MUST have a corresponding textual convention for use with the particular type of profile point. To support future extensions, a MIB module SHOULD NOT sub-type the CloneProfilePointType textual convention in an object type definition. However, a compliance statement MAY sub-type it in order to require only a subset of the profile point types for a compliant implementation. Implementations must ensure that CloneProfilePointType objects and any dependent objects (e.g., CloneProfilePointIdentifier objects) are consistent. For example, an implementation must respond with an 'inconsistentValue' error if an attempt is made to modify a CloneProfilePointType object without changing the corresponding CloneProfilePointIdentifier object."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("interface", 4))

class CloneProfilePointIdentifier(InterfaceIndexOrZero):
    description = "This textual convention specifies an ifindex value that identifies a point at which a clone profile sends out the cloned flows. Implementations must ensure that a CloneProfilePointIdentifier object remains consistent with the CloneProfilePointType object providing the context. For example, an implementation must respond with an 'inconsistentValue' error if an attempt is made to modify a CloneProfilePointIdentifier object without changing the corresponding CloneProfilePointType object. The value of a CloneProfilePointIdentifier object MUST BE 0, if the value of CloneProfilePointType object providing the context is 'unknown' or 'none'."
    status = 'current'

cfcCloneProfiles = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1))
cfcCloneProfileIdNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 1), CloneProfileIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileIdNext.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileIdNext.setDescription('This object specifies a value which is used as an index value for a new clone profile entry in cfcCloneProfileTable. Whenever read, the agent will get the next available non-conflicting value. This is to reduce the probability of errors during creation of new clone profile table entries')
cfcCloneProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2), )
if mibBuilder.loadTexts: cfcCloneProfileTable.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileTable.setDescription('This table lists the clone profiles contained by the device.')
cfcCloneProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"))
if mibBuilder.loadTexts: cfcCloneProfileEntry.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileEntry.setDescription("A peer SNMP entity may create a clone profile by setting an instance of cfcCloneProfileId to the value that is read from cfcCloneProfileIdNext, cfcCloneProfileName to the entry name and an instance of cfcCloneProfileStatus to 'createAndWait' or 'createAndGo'. Observe that an implementation that does not support these options must specify these limitations in an agent capabilities statement. Other management entities (e.g., the local console) may create a clone profile. In these cases, the system must automatically create a row in the cfcCloneProfileTable. A peer SNMP entity may destroy a clone profile by setting the corresponding instance of cfcCloneProfileStatus to 'destroy'. Observe that an implementation that does not support this option must specify this limitation in an agent capabilities statement. Other management entities may destroy a clone profile. In these cases, the system must automatically destroy the corresponding row in the cfcCloneProfileTable.")
cfcCloneProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 1), CloneProfileIdentifier())
if mibBuilder.loadTexts: cfcCloneProfileId.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileId.setDescription('This object indicates an arbitrary integer-value that uniquely identifies a clone profile. An application using this MIB is responsible for making sure these are unique, although the SNMP RowStatus row creation process will help by not allowing it to create conflicting entries. Before creating a new entry, a value for this variable may be obtained by reading cfcCloneProfileIdNext to reduce the probability of a value collision. Observe that the value assigned to a clone profile does not necessarily persist across restarts.')
cfcCloneProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileStatus.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileStatus.setDescription("The status of this conceptual row. This object manages creation, modification, and deletion of rows in this table. The following columns must be valid before activating a row: - cfcCloneProfileName - cfcCloneProfileStorageType - cfcCloneTargetType - cfcCloneTargetIfIndex cfcCloneTargetIfIndex is mandatory ONLY if cfcCloneTargetType is specified as 'interface'. Other writable objects in this table may be modified at any time, even while the row is 'active'. The entry may be deleted by setting the value to 'destroy', and if there are any associated traffic flow entries in the corresponding flow tables (cfcFlowIpTable in case of IP flows) they will also be deleted with this operation.")
cfcCloneProfileStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileStorageType.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileStorageType.setDescription('This object specifies the memory realization of the row.')
cfcCloneProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileName.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileName.setDescription('This object specifies an arbitrary name that uniquely identifies the clone profile.')
cfcCloneProfileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileDescription.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileDescription.setDescription('This object specifies a human-readable description configured to the clone profile. This object is optional while creating a row in this table and specifies a null string if no description is configured.')
cfcCloneProfileCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileCreateTime.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileCreateTime.setDescription('This object provides the value of sysUpTime when the row was created.')
cfcCloneProfileFlowCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 7), Gauge32()).setUnits('traffic flows').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileFlowCount.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileFlowCount.setDescription('This object provides the number of traffic flows currently associated with the clone profile.')
cfcCloneProfileFlowType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ip", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileFlowType.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileFlowType.setDescription("Identifies the type of flows associated with the clone profile. Based on type the corresponding flow table will represent the traffic flows associated with the clone profile. Note that a clone profile can clone only one type of traffic flows. For example, if the cfcCloneProfileFlowType is set to 'ip' than all the IP flows ONLY can be associated (using cfcFlowIpTable) and cloned by this clone profile. New flow types can be added to this based on the requirement and hardware or software capability. For each new cfcCloneProfileFlowType defined in cfcCloneProfileTable a separate table can be added to this MIB to hold the corresponding flow entries. The following types of flows are supported: 'ip' IP flows are associated with this clone profile.")
cfcCloneTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("system", 2), ("interface", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneTargetType.setStatus('current')
if mibBuilder.loadTexts: cfcCloneTargetType.setDescription("This object specifies the clone profile target. Following targets are supported today 'other' The implementation of the MIB module using this textual convention does not recognize the clone profile target. 'system' The clone profile target is global or the entire system. 'interface' The clone profile target is an interface represented by a row in the ifTable defined by the IF-MIB [RFC2863].")
cfcCloneTargetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneTargetIfIndex.setStatus('current')
if mibBuilder.loadTexts: cfcCloneTargetIfIndex.setDescription("This object specifies the ifindex of an interface over which traffic flow to be cloned is received or transmitted. The interface may be physical or virtual. The value of a cfcCloneTargetIfIndex object MUST BE 0 if the value of the cfcCloneTargetType object providing the context is 'system' or 'other'.")
cfcCloneProfileEgressIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 11), CloneProfilePointType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileEgressIfType.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileEgressIfType.setDescription('This object specifies the type of port/interface configured to the clone profile.')
cfcCloneProfileEgressIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 12), CloneProfilePointIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileEgressIf.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileEgressIf.setDescription('This object specifies the ifindex of an interface that is configured to the corresponding clone profile. All the flows configured within this profile set will be cloned to this interface.')
cfcCloneProfileTableChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileTableChanged.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileTableChanged.setDescription('This object provides the value of sysUpTime the last time the device created or destroyed a row in cfcCloneProfileTable.')
cfcFlows = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2))
cfcFlowIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1), )
if mibBuilder.loadTexts: cfcFlowIpTable.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpTable.setDescription('This table lists the IP traffic flows that are cloned by corresponding clone profile supported by the device. This table has an expansion dependent relationship on the cfcCloneProfileTable, containing zero or more rows for each clone profile. Below is an example, where multiple IP flows are associated with the single clone profile. +----------------------------+ | cfcFlowIpTable | | | +----------------------+ +--------------------------------+ | cfcCloneProfileId = 3----->| +-------------------------+ | +----------------------+ | | cfcCloneProfileId = 3 | | | | cfcFlowIndex = 3 | | | +-------------------------+ | | +-------------------------+ | | | cfcCloneProfileId = 3 | | | | cfcFlowIndex = 5 | | | +-------------------------+ | | : | | : | | +-------------------------+ | | | cfcCloneProfileId = 3 | | | | cfcFlowIndex = 10 | | | +-------------------------+ | +--------------------------------+ | | +----------------------+ +--------------------------------+ | cfcCloneProfileId = 4----->| +-------------------------+ | +----------------------+ | | cfcCloneProfileId = 4 | | | | cfcFlowIndex = 2 | | | +-------------------------+ | | +-------------------------+ | | | cfcCloneProfileId = 4 | | | | cfcFlowIndex = 6 | | | +-------------------------+ | | : | | : | | +-------------------------+ | | | cfcCloneProfileId = 4 | | | | cfcFlowIndex = 7 | | | +-------------------------+ | +--------------------------------+')
cfcFlowIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"), (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"))
if mibBuilder.loadTexts: cfcFlowIpEntry.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpEntry.setDescription("An entry describes a IP traffic flow that are cloned by the corresponding clone profile. The device creates a row in the cfcFlowIpTable when a IP flow is associated with a clone profile to clone the monitored flows and send it to the configured egress interface. Likewise, the device destroys a row in the cfcFlowIpTable when a traffic flow disassociated with a clone profile. Note that the corresponding clone profile must make sure cfcCloneProfileFlowType is set to 'IP' before creating an entry in this table else the creation will fail.")
cfcFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 1), CloneFlowIdentifier())
if mibBuilder.loadTexts: cfcFlowIndex.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIndex.setDescription('This object indicates an arbitrary integer-value that uniquely identifies a configured traffic flow within a clone profile. While adding an entry in this table, application is responsible for making sure these are unique, although the SNMP RowStatus row creation process will help by not allowing it to create conflicting entries. Observe that the value assigned to a traffic flow does not necessarily persist across restarts or the removal-insertion of a physical entity supporting clone profile(s).')
cfcFlowIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpStatus.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpStatus.setDescription("The status of this conceptual row. This object manages creation, and deletion of rows in this table. The following columns must be valid before activating a row: - cfcFlowIpStorageType - cfcFlowIpAddrSrcType - cfcFlowIpAddrSrc - cfcFlowIpAddrDstType - cfcFlowIpAddrDst Once the row is active, object in this table can not be modified at any time. The entry may be deleted by setting the value to 'destroy'.")
cfcFlowIpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpStorageType.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpStorageType.setDescription('This object specifies the memory realization of the row.')
cfcFlowIpAddrSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrSrcType.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpAddrSrcType.setDescription('This object specifies the type of IP address indicated by the corresponding instances of cfcFlowIpAddrSrc.')
cfcFlowIpAddrSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrSrc.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpAddrSrc.setDescription('This object specifies the source IP address of the corresponding traffic flow. This address will be of the type specified in cfcFlowIpAddrSrcType.')
cfcFlowIpAddrDstType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrDstType.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpAddrDstType.setDescription('This object specifies the type of IP address indicated by the corresponding instances of cfcFlowIpAddrDst.')
cfcFlowIpAddrDst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrDst.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpAddrDst.setDescription('This object specifies the destination IP address of the corresponding traffic flow. This address will be of the type specified in cfcFlowIpAddrDstType.')
cfcFlowIpCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowIpCreateTime.setStatus('current')
if mibBuilder.loadTexts: cfcFlowIpCreateTime.setDescription('This object provides the value of sysUpTime when the row was created.')
cfcFlowStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3))
cfcFlowStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1), )
if mibBuilder.loadTexts: cfcFlowStatsTable.setStatus('current')
if mibBuilder.loadTexts: cfcFlowStatsTable.setDescription('This table contains data relating to the collection of statistics for the flows cloned by the corresponding clone profiles supported by the device. This table has a sparse dependent relationship on the flow tables, containing a row for each row in the flow table (cfcFlowIpTable in case of IP flows) for which the device is actively cloning the packets.')
cfcFlowStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"), (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"))
if mibBuilder.loadTexts: cfcFlowStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cfcFlowStatsEntry.setDescription('An entry contains collection of statistics for a corresponding traffic flow. The device creates a row in the cfcFlowStatsTable when a clone profile is configured with a traffic flow and actively cloning the packets of that flow to the specified egress interface. Likewise, the device destroys a row in the cfcFlowStatsTable when the corresponding flow is removed from the clone profile.')
cfcFlowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 1), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowPkts.setStatus('current')
if mibBuilder.loadTexts: cfcFlowPkts.setDescription('This object provides the total number of packets that are cloned for a traffic flow by the corresponding clone profile.')
cfcFlowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 2), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowOctets.setStatus('current')
if mibBuilder.loadTexts: cfcFlowOctets.setDescription('This object provides the total number of octets contained by the packets that are cloned for a traffic flow by the corresponding clone profile.')
ciscoFlowCloneMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1))
ciscoFlowCloneMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2))
ciscoCloneFlowCompliance01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1, 1)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileGroup"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowGroup"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCloneFlowCompliance01 = ciscoCloneFlowCompliance01.setStatus('current')
if mibBuilder.loadTexts: ciscoCloneFlowCompliance01.setDescription('This compliance statement specifies the minimal requirements an implementation must meet in order to claim full compliance with the definition of the CISCO-FLOW-CLONE-MIB.')
cfcCloneProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 1)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileIdNext"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStatus"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStorageType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileName"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileDescription"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileCreateTime"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowCount"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetIfIndex"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIfType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIf"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileTableChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcCloneProfileGroup = cfcCloneProfileGroup.setStatus('current')
if mibBuilder.loadTexts: cfcCloneProfileGroup.setDescription('This group contains objects describing clone profiles.')
cfcFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 2)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStatus"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStorageType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrcType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrc"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDstType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDst"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpCreateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFlowGroup = cfcFlowGroup.setStatus('current')
if mibBuilder.loadTexts: cfcFlowGroup.setDescription('This group contains objects describing traffic flows.')
cfcFlowStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 3)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcFlowPkts"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFlowStatsGroup = cfcFlowStatsGroup.setStatus('current')
if mibBuilder.loadTexts: cfcFlowStatsGroup.setDescription('This group contains objects describing traffic flow metrics.')
mibBuilder.exportSymbols("CISCO-FLOW-CLONE-MIB", cfcCloneProfileTableChanged=cfcCloneProfileTableChanged, CloneProfileIdentifier=CloneProfileIdentifier, cfcFlowIpEntry=cfcFlowIpEntry, cfcCloneProfileGroup=cfcCloneProfileGroup, cfcFlowStats=cfcFlowStats, cfcCloneProfileDescription=cfcCloneProfileDescription, cfcFlowIpStatus=cfcFlowIpStatus, cfcCloneProfileCreateTime=cfcCloneProfileCreateTime, cfcFlowIpAddrSrc=cfcFlowIpAddrSrc, cfcCloneProfileStorageType=cfcCloneProfileStorageType, cfcCloneProfileEgressIfType=cfcCloneProfileEgressIfType, cfcFlowIpAddrSrcType=cfcFlowIpAddrSrcType, cfcCloneProfileTable=cfcCloneProfileTable, ciscoFlowCloneMIB=ciscoFlowCloneMIB, ciscoCloneFlowCompliance01=ciscoCloneFlowCompliance01, cfcCloneProfileEgressIf=cfcCloneProfileEgressIf, cfcFlowStatsGroup=cfcFlowStatsGroup, cfcCloneProfiles=cfcCloneProfiles, PYSNMP_MODULE_ID=ciscoFlowCloneMIB, cfcFlowIpStorageType=cfcFlowIpStorageType, cfcFlowIpAddrDst=cfcFlowIpAddrDst, cfcCloneProfileName=cfcCloneProfileName, cfcCloneProfileId=cfcCloneProfileId, cfcFlowIpAddrDstType=cfcFlowIpAddrDstType, CloneProfilePointIdentifier=CloneProfilePointIdentifier, cfcFlowOctets=cfcFlowOctets, cfcCloneProfileFlowType=cfcCloneProfileFlowType, cfcCloneTargetIfIndex=cfcCloneTargetIfIndex, cfcFlowIpCreateTime=cfcFlowIpCreateTime, cfcFlowStatsTable=cfcFlowStatsTable, cfcCloneProfileIdNext=cfcCloneProfileIdNext, ciscoFlowCloneMIBGroups=ciscoFlowCloneMIBGroups, ciscoFlowCloneMIBCompliances=ciscoFlowCloneMIBCompliances, cfcCloneProfileEntry=cfcCloneProfileEntry, CloneFlowIdentifier=CloneFlowIdentifier, CloneProfilePointType=CloneProfilePointType, cfcCloneProfileFlowCount=cfcCloneProfileFlowCount, ciscoFlowCloneMIBObjects=ciscoFlowCloneMIBObjects, ciscoFlowCloneMIBNotifications=ciscoFlowCloneMIBNotifications, cfcCloneTargetType=cfcCloneTargetType, ciscoFlowCloneMIBConformance=ciscoFlowCloneMIBConformance, cfcFlowStatsEntry=cfcFlowStatsEntry, cfcFlows=cfcFlows, cfcFlowGroup=cfcFlowGroup, cfcFlowIpTable=cfcFlowIpTable, cfcFlowPkts=cfcFlowPkts, cfcFlowIndex=cfcFlowIndex, cfcCloneProfileStatus=cfcCloneProfileStatus)
