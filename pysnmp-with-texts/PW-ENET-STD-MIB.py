#
# PySNMP MIB module PW-ENET-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PW-ENET-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
pwIndex, = mibBuilder.importSymbols("PW-STD-MIB", "pwIndex")
VlanIdOrAnyOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrAnyOrNone")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, NotificationType, Integer32, MibIdentifier, Counter64, IpAddress, Gauge32, Unsigned32, mib_2, ObjectIdentity, Bits, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Integer32", "MibIdentifier", "Counter64", "IpAddress", "Gauge32", "Unsigned32", "mib-2", "ObjectIdentity", "Bits", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString, StorageType, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "StorageType", "RowStatus")
pwEnetStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 180))
pwEnetStdMIB.setRevisions(('2009-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pwEnetStdMIB.setRevisionsDescriptions(('Initial version published as part of RFC 5603.',))
if mibBuilder.loadTexts: pwEnetStdMIB.setLastUpdated('200906150000Z')
if mibBuilder.loadTexts: pwEnetStdMIB.setOrganization('Pseudowire Edge-to-Edge Emulation (PWE3) Working Group')
if mibBuilder.loadTexts: pwEnetStdMIB.setContactInfo('David Zelig Email: davidz@oversi.com Thomas D. Nadeau Email: tom.nadeau@bt.com ')
if mibBuilder.loadTexts: pwEnetStdMIB.setDescription("This MIB module describes a model for managing Ethernet point-to-point pseudowire services over a Packet Switched Network (PSN). Copyright (c) 2009 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: - Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. - Neither the name of Internet Society, IETF or IETF Trust, nor the names of specific contributors, may be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. This version of this MIB module is part of RFC 5603; see the RFC itself for full legal notices.")
pwEnetObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 180, 1))
pwEnetConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 180, 2))
pwEnetTable = MibTable((1, 3, 6, 1, 2, 1, 180, 1, 1), )
if mibBuilder.loadTexts: pwEnetTable.setStatus('current')
if mibBuilder.loadTexts: pwEnetTable.setDescription('This table contains the index to the Ethernet tables associated with this Ethernet PW, the VLAN configuration, and the VLAN mode.')
pwEnetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 180, 1, 1, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"), (0, "PW-ENET-STD-MIB", "pwEnetPwInstance"))
if mibBuilder.loadTexts: pwEnetEntry.setStatus('current')
if mibBuilder.loadTexts: pwEnetEntry.setDescription("This table is indexed by the same index that was created for the associated entry in the PW generic table in the PW-STD-MIB module. The pwIndex and the pwEnetPwInstance are used as indexes to allow multiple VLANs to exist on the same PW. An entry is created in this table by the agent for every entry in the pwTable with a pwType of 'ethernetTagged' or 'ethernet'. Additional rows may be created by the operator or the agent if multiple entries are required for the same PW. The value of pwEnetPwInstance can be arbitrarily selected to make the row unique; however, implementations that know the VLAN field value when the row is created MAY use the value of the VLAN itself for better readability and backward compatibility with older versions of this MIB module. This table provides Ethernet port mapping and VLAN configuration for each Ethernet PW. All read-create objects in this table MAY be changed at any time; however, change of some objects (for example, pwEnetVlanMode) during the PW forwarding state MAY cause traffic disruption. Manual entries in this table SHOULD be preserved after a reboot, and the agent MUST ensure the integrity of those entries. If the set of entries of a specific row is found to be inconsistent after reboot, the PW pwOperStatus MUST be declared as notPresent(5). ")
pwEnetPwInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pwEnetPwInstance.setStatus('current')
if mibBuilder.loadTexts: pwEnetPwInstance.setDescription('If multiple rows are mapped to the same PW, this index is used to uniquely identify the individual row. If the value of the VLAN field is known at the time of row creation, the value of pwEnetPwVlan MAY be used for better readability and backward compatibility with older versions of this MIB module. Otherwise, the value 1 SHOULD be set to the first row for each pwIndex for better readability and in order that the management application will know in advance how to access the first row when it was created by the agent. ')
pwEnetPwVlan = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 2), VlanIdOrAnyOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwEnetPwVlan.setStatus('current')
if mibBuilder.loadTexts: pwEnetPwVlan.setDescription("This object defines the (service-delimiting) VLAN field value on the PW. The value 4095 MUST be used if the object is not applicable, for example, when mapping all packets from an Ethernet port to this PW (raw mode). The value 0 MUST be set to indicate untagged frames (from the PW point of view), i.e., when pwEnetVlanMode equals 'noChange' and pwEnetPortVlan equals 0.")
pwEnetVlanMode = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 0), ("portBased", 1), ("noChange", 2), ("changeVlan", 3), ("addVlan", 4), ("removeVlan", 5))).clone('noChange')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwEnetVlanMode.setStatus('current')
if mibBuilder.loadTexts: pwEnetVlanMode.setDescription("This object indicates the mode of VLAN handling between the port or the virtual port associated with the PW and the PW encapsulation. - 'other' indicates an operation that is not defined by this MIB module. - 'portBased' indicates that the forwarder will forward packets between the port and the PW independent of their structure (i.e., there are no service-delimiting VLAN tags from the PE standpoint). - 'noChange' indicates that the PW contains the original user VLAN, as specified in pwEnetPortVlan; i.e., the VLAN on the PE-CE link is the service-delimiting tag and is kept 'as is' on the PW. - 'changeVlan' indicates that the VLAN field on the PW may be different than the VLAN field on the user's port. The VLAN on the PE-CE link is the service-delimiting tag but has a different value on the PW. - 'addVlan' indicates that a VLAN field will be added on the PSN-bound direction (i.e., on the PW). pwEnetPwVlan indicates the value that will be added. - 'removeVlan' indicates that the encapsulation on the PW does not include the service-delimiting VLAN field. Note that PRI bits transparency is lost in this case. - Implementation of 'portsbased', 'removeVlan', 'addVlan' 'other', and 'changeVlan' is OPTIONAL. ")
pwEnetPortVlan = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 4), VlanIdOrAnyOrNone().clone(4095)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwEnetPortVlan.setStatus('current')
if mibBuilder.loadTexts: pwEnetPortVlan.setDescription("This object defines if the mapping between the original port (physical port or VPLS virtual port) to the PW is VLAN based or not. In case of VLAN mapping, this object indicates the VLAN value on the original port. The value of '4095' MUST be used if the whole original port traffic is mapped to the same PW. Note that a pwType of 'ethernetTagged' can still be used if service-delimiting tag is added on the PW (pwEnetVlanMode equals 'addVlan'). This object MUST be equal to pwEnetPwVlan if pwEnetVlanMode equals 'noChange'. The value 0 indicates that packets without a VLAN field (i.e., untagged frames) on the port are associated to this PW. This allows the same behavior as assigning 'Default VLAN' to untagged frames. ")
pwEnetPortIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwEnetPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: pwEnetPortIfIndex.setDescription('This object is used to specify the ifIndex of the Ethernet port associated with this PW for point-to-point Ethernet service, or the ifIndex of the virtual interface of the VPLS instance associated with the PW if the service is VPLS. Two rows in this table can point to the same ifIndex only if there is no overlap of VLAN values specified in pwEnetPortVlan that are associated with this port. A value of zero indicates that association to an ifIndex is not yet known.')
pwEnetPwIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwEnetPwIfIndex.setStatus('current')
if mibBuilder.loadTexts: pwEnetPwIfIndex.setDescription("If the PW is modeled as an ifIndex in the ifTable, this object indicates the value of the ifIndex representing the Ethernet PW on the PSN side in the Etherlike-MIB. Note that this value may be different from the value of pwIfIndex that represents the ifIndex of the PW for ifType 'pw'.")
pwEnetRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwEnetRowStatus.setStatus('current')
if mibBuilder.loadTexts: pwEnetRowStatus.setDescription('This object enables creating, deleting, and modifying this row.')
pwEnetStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 1, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwEnetStorageType.setStatus('current')
if mibBuilder.loadTexts: pwEnetStorageType.setDescription('This object indicates the storage type of this row.')
pwEnetStatsTable = MibTable((1, 3, 6, 1, 2, 1, 180, 1, 2), )
if mibBuilder.loadTexts: pwEnetStatsTable.setStatus('current')
if mibBuilder.loadTexts: pwEnetStatsTable.setDescription('This table contains statistical counters specific for Ethernet PW.')
pwEnetStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 180, 1, 2, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: pwEnetStatsEntry.setStatus('current')
if mibBuilder.loadTexts: pwEnetStatsEntry.setDescription('Each entry represents the statistics gathered for the PW carrying the Ethernet.')
pwEnetStatsIllegalVlan = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 2, 1, 1), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwEnetStatsIllegalVlan.setStatus('current')
if mibBuilder.loadTexts: pwEnetStatsIllegalVlan.setDescription('The number of packets received (from the PSN) on this PW with either an illegal VLAN field, a missing VLAN field when one was expected, or an excessive VLAN field when it was not expected. This counter may not be applicable in some cases, and MUST return the value of zero in such a case.')
pwEnetStatsIllegalLength = MibTableColumn((1, 3, 6, 1, 2, 1, 180, 1, 2, 1, 2), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwEnetStatsIllegalLength.setStatus('current')
if mibBuilder.loadTexts: pwEnetStatsIllegalLength.setDescription('The number of packets that were received with an illegal Ethernet packet length on this PW. An illegal length is defined as being greater than the value in the advertised MTU supported, or shorter than the allowed Ethernet packet size.')
pwEnetGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 180, 2, 1))
pwEnetCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 180, 2, 2))
pwEnetModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 180, 2, 2, 1)).setObjects(("PW-ENET-STD-MIB", "pwEnetGroup"), ("PW-ENET-STD-MIB", "pwEnetStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwEnetModuleFullCompliance = pwEnetModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: pwEnetModuleFullCompliance.setDescription('The compliance statement for agents that provides full support for the PW-ENET-STD-MIB module. Such devices can then be monitored and also be configured using this MIB module.')
pwEnetModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 180, 2, 2, 2)).setObjects(("PW-ENET-STD-MIB", "pwEnetGroup"), ("PW-ENET-STD-MIB", "pwEnetStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwEnetModuleReadOnlyCompliance = pwEnetModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: pwEnetModuleReadOnlyCompliance.setDescription('The compliance statement for agents that provide read- only support for the PW-ENET-STD-MIB module. Such devices can then be monitored but cannot be configured using this MIB module.')
pwEnetGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 180, 2, 1, 1)).setObjects(("PW-ENET-STD-MIB", "pwEnetPwVlan"), ("PW-ENET-STD-MIB", "pwEnetVlanMode"), ("PW-ENET-STD-MIB", "pwEnetPortVlan"), ("PW-ENET-STD-MIB", "pwEnetPortIfIndex"), ("PW-ENET-STD-MIB", "pwEnetPwIfIndex"), ("PW-ENET-STD-MIB", "pwEnetRowStatus"), ("PW-ENET-STD-MIB", "pwEnetStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwEnetGroup = pwEnetGroup.setStatus('current')
if mibBuilder.loadTexts: pwEnetGroup.setDescription('Collection of objects for basic Ethernet PW configuration.')
pwEnetStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 180, 2, 1, 2)).setObjects(("PW-ENET-STD-MIB", "pwEnetStatsIllegalVlan"), ("PW-ENET-STD-MIB", "pwEnetStatsIllegalLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwEnetStatsGroup = pwEnetStatsGroup.setStatus('current')
if mibBuilder.loadTexts: pwEnetStatsGroup.setDescription('Collection of objects counting various PW level errors.')
mibBuilder.exportSymbols("PW-ENET-STD-MIB", pwEnetStorageType=pwEnetStorageType, pwEnetStatsEntry=pwEnetStatsEntry, pwEnetStatsIllegalVlan=pwEnetStatsIllegalVlan, pwEnetModuleReadOnlyCompliance=pwEnetModuleReadOnlyCompliance, pwEnetPortIfIndex=pwEnetPortIfIndex, pwEnetRowStatus=pwEnetRowStatus, pwEnetPwVlan=pwEnetPwVlan, pwEnetEntry=pwEnetEntry, pwEnetStdMIB=pwEnetStdMIB, pwEnetPortVlan=pwEnetPortVlan, pwEnetVlanMode=pwEnetVlanMode, pwEnetPwInstance=pwEnetPwInstance, pwEnetStatsGroup=pwEnetStatsGroup, pwEnetCompliances=pwEnetCompliances, pwEnetGroups=pwEnetGroups, pwEnetConformance=pwEnetConformance, PYSNMP_MODULE_ID=pwEnetStdMIB, pwEnetModuleFullCompliance=pwEnetModuleFullCompliance, pwEnetGroup=pwEnetGroup, pwEnetTable=pwEnetTable, pwEnetStatsTable=pwEnetStatsTable, pwEnetObjects=pwEnetObjects, pwEnetStatsIllegalLength=pwEnetStatsIllegalLength, pwEnetPwIfIndex=pwEnetPwIfIndex)
