#
# PySNMP MIB module JUNIPER-PW-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-PW-ATM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
AtmVcIdentifier, AtmVpIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVcIdentifier", "AtmVpIdentifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
jnxVpnPwIndex, jnxVpnPwVpnType, jnxVpnPwVpnName = mibBuilder.importSymbols("JUNIPER-VPN-MIB", "jnxVpnPwIndex", "jnxVpnPwVpnType", "jnxVpnPwVpnName")
PerfIntervalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfCurrentCount")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, Counter32, Bits, TimeTicks, ObjectIdentity, Integer32, NotificationType, Gauge32, IpAddress, Unsigned32, mib_2, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Bits", "TimeTicks", "ObjectIdentity", "Integer32", "NotificationType", "Gauge32", "IpAddress", "Unsigned32", "mib-2", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
RowStatus, RowPointer, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "RowPointer", "TextualConvention", "DisplayString", "TruthValue")
jnxPWAtmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 57))
jnxPWAtmMIB.setRevisions(('2009-09-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxPWAtmMIB.setRevisionsDescriptions((' This mib is a modified version of RFC 5605',))
if mibBuilder.loadTexts: jnxPWAtmMIB.setLastUpdated('200909010000Z')
if mibBuilder.loadTexts: jnxPWAtmMIB.setOrganization('Pseudo-Wire Emulation Edge-to-Edge (PWE3) Working Group')
if mibBuilder.loadTexts: jnxPWAtmMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxPWAtmMIB.setDescription('This MIB module defines objects used for managing the atm pseudowires in Juniper products.')
jnxpwAtmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 57, 0))
jnxpwAtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1))
jnxpwAtmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 57, 2))
jnxpwAtmCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1), )
if mibBuilder.loadTexts: jnxpwAtmCfgTable.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmCfgTable.setDescription('This table specifies generic information for an ATM PW to be carried over PSN in any mode.')
jnxpwAtmCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmCfgEntry.setReference('See [PWMIB] ')
if mibBuilder.loadTexts: jnxpwAtmCfgEntry.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmCfgEntry.setDescription('This table contains a set of parameters for the ATM PW that needs to be adapted and carried over PSN. This table is indexed by pwIndex from pwTable. An entry is created for every newly ATM type associated pwIndex in the pwTable. Unless otherwise specified, all read-write objects in this table MAY be changed when the PW is defined as not active and all RW objects values must persist after reboot')
jnxpwAtmCfgMaxCellConcatenation = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 29))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmCfgMaxCellConcatenation.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmCfgMaxCellConcatenation.setDescription('The maximum number of ATM cells that can be concatenated into one PW packet towards PSN. In non LDP or other signaling protocol environment, this object MAY be changed at anytime, but traffic might be interuppted, otherwise, it may be changed when PW is not active.')
jnxpwAtmCfgFarEndMaxCellConcatenation = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 29))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmCfgFarEndMaxCellConcatenation.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmCfgFarEndMaxCellConcatenation.setDescription('The maximum number of ATM cells that can be concatenated into one PW packet towards PSN as reported by the far end. If no LDP in use, the object will either return value 0 or allow setting it for calculating protocol overhead.')
jnxpwAtmCfgTimeoutMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmCfgTimeoutMode.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmCfgTimeoutMode.setDescription('This objects determines whether a packet can be transmitted to the PSN based on time out expiration for collecting cells or not. The actual handling of the time out is implementation specific-as such this object may be changed at any time under proper consideration of traffic interupption effect.')
jnxpwAtmClpQosMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmClpQosMapping.setReference('See [ATMENCAP] section 12')
if mibBuilder.loadTexts: jnxpwAtmClpQosMapping.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmClpQosMapping.setDescription('This Object indicates whether the CLP bits should be considered when setting the value in the Quality of Service fields of the encapsulating protocol (e.g. EXP fields of the MPLS Label Stack). Selecting True allows the drop precedence to be preserved across the PSN. In transparent cell transport, the value of this object MUST be false(2), in other cases it can be changed at any time.')
jnxpwAtmOutboundNto1Table = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2), )
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Table.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Table.setDescription('This table specifies the information for an ATM PW to be carried over PSN in the outbound direction. Up to N entries can be created in this table for every entry in the pwTable with a pwType equal to: atmCellNto1Vcc(9), or atmCellNto1Vpc(10). An entry can be created only when the VP/VC are known. A single entry will be created in this table for every entry in the pwTable with a pwType equal to one of the following: atmCell1to1Vcc(12), or atmCell1to1Vpc(13), or atmAal5PduVcc(14), or atmAal5SduVcc(2), or atmTransparent(3). ')
jnxpwAtmOutboundNto1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Entry.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Entry.setDescription('A row in this table represents an ATM PW that needs to be adapted and carried over PSN. This table is indexed by pwIndex from pwTable and the ATM interface with VPL/ VCLs. In atmTransparent(3), Vpi and VCi will be 0xFFFF during set operation. Unless otherwise specified, all read-create objects in this table MUST NOT be changed after row activation and SHOULD remain unchanged after reboot.')
jnxpwAtmOutboundNto1AtmIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1AtmIf.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1AtmIf.setDescription('The ATM Interface that receives cells from the ATM network.')
jnxpwAtmOutboundNto1Vpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Vpi.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Vpi.setDescription('VPI value of this ATM PW. In atmTransparent(3), Vpi will be the equivalent of 0xFFFF')
jnxpwAtmOutboundNto1Vci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Vci.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1Vci.setDescription('VCI value of this ATM PW. In atmTransparent(3), or VP case, the value will be the equivalent of 0xFFFF')
jnxpwAtmOutboundNto1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1RowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1RowStatus.setDescription('This Object is used to create, modify or delete a row in this table.')
jnxpwAtmOutboundNto1TrafficParamDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1TrafficParamDescr.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1TrafficParamDescr.setDescription('This object represents a pointer to a ATM traffic parameter specific row in either private or standard table which will be employed while receiving cells from the ATM network. This table should contain a set of self-consistent ATM traffic parameters including the ATM traffic service category. A value of 0.0 indicates Best Effort.')
jnxpwAtmOutboundNto1MappedVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 6), AtmVpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1MappedVpi.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1MappedVpi.setDescription('The egress generated VPI value of this ATM PW. The entry is valid for PW type of atmCellNto1Vcc(9), atmCellNto1Vpc(10), atmCell1to1Vcc(12), or atmCell1to1Vpc(13). In other types, the value will be the equivalent of 0xFFFF. Value MAY be changed when the PW is defined as not active ')
jnxpwAtmOutboundNto1MappedVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 2, 1, 7), AtmVcIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1MappedVci.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmOutboundNto1MappedVci.setDescription('The egress generated VCI value of this ATM PW. The entry is valid for PW type of atmCellNto1Vcc(9), atmCellNto1Vpc(10), atmCell1to1Vcc(12), or atmCell1to1Vpc(13. In VP case or other types, the value will be the equivalent of 0xFFFF. Value MAY be changed when the PW is defined as not active.')
jnxpwAtmInboundNto1Table = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3), )
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Table.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Table.setDescription('This table specifies the information for an ATM PW to be carried over PSN in the Inbound direction. Up to N entries can be created in this table for every entry in the pwTable with a pwType equal to: atmCellNto1Vcc(9), or atmCellNto1Vpc(10). An entry can be created only when the VP/VC are known. A single entry will be created in this table for every entry in the pwTable with a pwType equal to one of the following:atmCell1to1Vcc(12), or atmCell1to1Vpc(13), or atmAal5PduVcc(14), or atmAal5SduVcc(2), or atmTransparent(3).')
jnxpwAtmInboundNto1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Entry.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Entry.setDescription('A row in this table represents an ATM PW that needs to be adapted and carried over PSN. This table is indexed by pwIndex from pwTable and the ATM interface with VPL/ VCLs. In atmTransparent(3), Vpi and VCi will be 0xFFFF during set operation. Unless otherwise specified, all Read-Creat objects in this table MUST NOT be changed after row activation and SHOULD remain unchanged after reboot.')
jnxpwAtmInboundNto1AtmIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxpwAtmInboundNto1AtmIf.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1AtmIf.setDescription('The ATM Interface that receives cells from the ATM network.')
jnxpwAtmInboundNto1Vpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 2), AtmVpIdentifier())
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Vpi.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Vpi.setDescription('VPI value of this ATM PW. In atmTransparent(3), Vpi will be the equivalent of 0xFFFF.')
jnxpwAtmInboundNto1Vci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 3), AtmVcIdentifier())
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Vci.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1Vci.setDescription('VCI value of this ATM PW. In atmTransparent(3), or VP case, the value will be the equivalent of 0xFFFF')
jnxpwAtmInboundNto1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1RowStatus.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1RowStatus.setDescription('This Object is used to create, modify or delete a row in this table.')
jnxpwAtmInboundNto1TrafficParamDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1TrafficParamDescr.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1TrafficParamDescr.setDescription('This object represents a pointer to a ATM traffic parameter specific row in either private or standard table which will be employed while receiving cells from the ATM network. This table should contain a set of self-consistent ATM traffic parameters including the ATM traffic service category. A value of 0.0 indicates Best Effort.')
jnxpwAtmInboundNto1MappedVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 6), AtmVpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1MappedVpi.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1MappedVpi.setDescription('The generated VPI value of this ATM PW. The entry is valid for PW type of atmCellNto1Vcc(9), atmCellNto1Vpc(10), atmCell1to1Vcc(12), or atmCell1to1Vpc(13). In other types, the value will be the equivalent of 0xFFFF. Value MAY be changed when the PW is defined as not active.')
jnxpwAtmInboundNto1MappedVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 3, 1, 7), AtmVcIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmInboundNto1MappedVci.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmInboundNto1MappedVci.setDescription('The generated VCI value of this ATM PW. The entry is valid for PW type of atmCellNto1Vcc(9), atmCellNto1Vpc(10), atmCell1to1Vcc(12), or atmCell1to1Vpc(13. In VP case or other types, the value will be the equivalent of 0xFFFF. Value MAY be changed when the PW is defined as not active.')
jnxpwAtmPerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4), )
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentTable.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentTable.setDescription('The current 15 minute interval counts are in this table. This table provides performance information per ATM PW.')
jnxpwAtmPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"))
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentEntry.setDescription('An entry in this table is created by the agent for every pwAtmCfgTable entry. After 15 minutes, the contents of this table entry are copied to a new entry in the pwAtmPerfInterval table and the counts in this entry are reset to zero.')
jnxpwAtmPerfCurrentMissingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentMissingPkts.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentMissingPkts.setDescription('Number of missing packets (as detected via control word sequence number gaps).')
jnxpwAtmPerfCurrentPktsReOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsReOrder.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsReOrder.setDescription('Number of packets detected out of sequence (via control word sequence number), but successfully re-ordered. Note: some implementations may not support this Feature.')
jnxpwAtmPerfCurrentPktsMisOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsMisOrder.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsMisOrder.setDescription('Number of packets detected out of order (via control word sequence numbers).')
jnxpwAtmPerfCurrentPktsTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsTimeout.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsTimeout.setDescription('Number of packets transmitted due to timeout expiration while attempting to collect cells.')
jnxpwAtmPerfCurrentPktsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsXmit.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsXmit.setDescription('Number of transmitted packets.')
jnxpwAtmPerfCurrentCellsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentCellsDropped.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentCellsDropped.setDescription('Number of dropped cells.')
jnxpwAtmPerfCurrentPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsReceived.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentPktsReceived.setDescription('Number of received packets.')
jnxpwAtmPerfCurrentUnknownCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentUnknownCells.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfCurrentUnknownCells.setDescription('Number of cells received from the PSN with unknown VPI or VCI values. This object is relevant only in N:1 mode.')
jnxpwAtmPerfIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5), )
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalTable.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalTable.setDescription('This table provides performance information per ATM PW similar to the pwAtmPerfCurrentTable above. However, these counts represent historical 15 minute intervals. Typically, this table will have a maximum of 96 entries for a 24 hour period. ')
jnxpwAtmPerfIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"), (0, "JUNIPER-PW-ATM-MIB", "jnxpwAtmPerfIntervalNumber"))
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalEntry.setDescription('An entry in this table is created by the agent for every pwAtmPerfCurrentEntry that is 15 minutes old. The contents of the Current entry are copied to the new entry here. The Current entry, then resets its counts to zero for the next current 15 minute interval. ')
jnxpwAtmPerfIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalNumber.setDescription('A number (normally between 1 and 96 to cover a 24 hour period) which identifies the interval for which the set of statistics is available. The interval identified by 1 is the most recently completed 15 minute interval, and the interval identified by N is the interval immediately preceding the one identified by N-1. The minimum range of N is 1 through 4. The default range is 1 through 32. The maximum value of N is 96.')
jnxpwAtmPerfIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalValidData.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalValidData.setDescription('This variable indicates if the data for this interval is valid.')
jnxpwAtmPerfIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalDuration.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalDuration.setDescription("The duration of a particular interval in seconds, Adjustments in the system's time-of-day clock, may cause the interval to be greater or less than, the normal value. Therefore this actual interval value is provided.")
jnxpwAtmPerfIntervalMissingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalMissingPkts.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalMissingPkts.setDescription('Number of missing packets (as detected via control word sequence number gaps).')
jnxpwAtmPerfIntervalPktsReOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsReOrder.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsReOrder.setDescription('Number of packets detected out of sequence (via control word sequence number), but successfully re-ordered. Note: some implementations may not support this Feature.')
jnxpwAtmPerfIntervalPktsMisOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsMisOrder.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsMisOrder.setDescription('Number of packets detected out of order (via control word sequence numbers).')
jnxpwAtmPerfIntervalPktsTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 7), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsTimeout.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsTimeout.setDescription('Number of packets transmitted due to timeout expiration.')
jnxpwAtmPerfIntervalPktsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsXmit.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsXmit.setDescription('Number of transmitted packets.')
jnxpwAtmPerfIntervalCellsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalCellsDropped.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalCellsDropped.setDescription('Number of dropped cells.')
jnxpwAtmPerfIntervalPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsReceived.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalPktsReceived.setDescription('Number of received packets.')
jnxpwAtmPerfIntervalUnknownCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalUnknownCells.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerfIntervalUnknownCells.setDescription('Number of cells received from the PSN with unknown VPI or VCI values. This object is relevant only in N:1 mode.')
jnxpwAtmPerf1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6), )
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalTable.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalTable.setDescription('This table provides performance information per ATM PW similar to the pwAtmPerfIntervalTable above. However, these counters represent historical 1 day intervals up to one full month.')
jnxpwAtmPerf1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1), ).setIndexNames((0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnType"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwVpnName"), (0, "JUNIPER-VPN-MIB", "jnxVpnPwIndex"), (0, "JUNIPER-PW-ATM-MIB", "jnxpwAtmPerf1DayIntervalNumber"))
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalEntry.setDescription('An entry is created in this table by the agent for every entry in the pwAtmCfgTable table.')
jnxpwAtmPerf1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 365)))
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalNumber.setDescription('The number of interval, where 1 indicates current day measured period and 2 and above indicate previous days respectively')
jnxpwAtmPerf1DayIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalValidData.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalValidData.setDescription('This object indicates if the data for this interval is valid.')
jnxpwAtmPerf1DayIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalDuration.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalDuration.setDescription("The duration of a particular interval in seconds, Adjustments in the system's time-of-day clock, may cause the interval to be greater or less than, the normal value. Therefore this actual interval value is provided.")
jnxpwAtmPerf1DayIntervalMissingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalMissingPkts.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalMissingPkts.setDescription('Number of missing packets (as detected via control word sequence number gaps).')
jnxpwAtmPerf1DayIntervalPktsReOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsReOrder.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsReOrder.setDescription('Number of packets detected out of sequence (via control word sequence number), but successfully re-ordered. Note: some implementations may not support this feature.')
jnxpwAtmPerf1DayIntervalPktsMisOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsMisOrder.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsMisOrder.setDescription('Number of packets detected out of order(via control word sequence numbers), and could not be re-ordered.')
jnxpwAtmPerf1DayIntervalPktsTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsTimeout.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsTimeout.setDescription('Number of packets transmitted due to timeout expiration.')
jnxpwAtmPerf1DayIntervalPktsXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsXmit.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsXmit.setDescription('Number of transmitted packets.')
jnxpwAtmPerf1DayIntervalCellsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalCellsDropped.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalCellsDropped.setDescription('Number of dropped cells.')
jnxpwAtmPerf1DayIntervalPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsReceived.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalPktsReceived.setDescription('Number of received packets.')
jnxpwAtmPerf1DayIntervalUnknownCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 57, 1, 6, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalUnknownCells.setStatus('current')
if mibBuilder.loadTexts: jnxpwAtmPerf1DayIntervalUnknownCells.setDescription('Number of cells received from the PSN with unknown VPI or VCI value. This object is relevant only in N:1 mode.')
mibBuilder.exportSymbols("JUNIPER-PW-ATM-MIB", jnxpwAtmPerfIntervalMissingPkts=jnxpwAtmPerfIntervalMissingPkts, jnxpwAtmPerfIntervalTable=jnxpwAtmPerfIntervalTable, jnxpwAtmOutboundNto1TrafficParamDescr=jnxpwAtmOutboundNto1TrafficParamDescr, jnxpwAtmPerf1DayIntervalPktsMisOrder=jnxpwAtmPerf1DayIntervalPktsMisOrder, jnxpwAtmOutboundNto1Entry=jnxpwAtmOutboundNto1Entry, jnxpwAtmInboundNto1Vci=jnxpwAtmInboundNto1Vci, jnxpwAtmPerfIntervalPktsXmit=jnxpwAtmPerfIntervalPktsXmit, jnxpwAtmClpQosMapping=jnxpwAtmClpQosMapping, jnxpwAtmOutboundNto1MappedVpi=jnxpwAtmOutboundNto1MappedVpi, jnxpwAtmNotifications=jnxpwAtmNotifications, jnxpwAtmPerf1DayIntervalValidData=jnxpwAtmPerf1DayIntervalValidData, jnxpwAtmPerfIntervalPktsReOrder=jnxpwAtmPerfIntervalPktsReOrder, jnxpwAtmPerf1DayIntervalEntry=jnxpwAtmPerf1DayIntervalEntry, jnxpwAtmPerfCurrentCellsDropped=jnxpwAtmPerfCurrentCellsDropped, jnxpwAtmPerfIntervalPktsMisOrder=jnxpwAtmPerfIntervalPktsMisOrder, jnxpwAtmCfgMaxCellConcatenation=jnxpwAtmCfgMaxCellConcatenation, jnxpwAtmOutboundNto1RowStatus=jnxpwAtmOutboundNto1RowStatus, jnxpwAtmPerfIntervalNumber=jnxpwAtmPerfIntervalNumber, jnxpwAtmOutboundNto1MappedVci=jnxpwAtmOutboundNto1MappedVci, jnxpwAtmInboundNto1Vpi=jnxpwAtmInboundNto1Vpi, jnxpwAtmOutboundNto1AtmIf=jnxpwAtmOutboundNto1AtmIf, jnxpwAtmPerfCurrentPktsXmit=jnxpwAtmPerfCurrentPktsXmit, jnxpwAtmPerf1DayIntervalUnknownCells=jnxpwAtmPerf1DayIntervalUnknownCells, jnxpwAtmPerfIntervalPktsReceived=jnxpwAtmPerfIntervalPktsReceived, jnxpwAtmPerf1DayIntervalPktsReOrder=jnxpwAtmPerf1DayIntervalPktsReOrder, jnxpwAtmCfgTimeoutMode=jnxpwAtmCfgTimeoutMode, jnxpwAtmInboundNto1AtmIf=jnxpwAtmInboundNto1AtmIf, jnxpwAtmPerfCurrentMissingPkts=jnxpwAtmPerfCurrentMissingPkts, jnxpwAtmConformance=jnxpwAtmConformance, jnxpwAtmPerf1DayIntervalDuration=jnxpwAtmPerf1DayIntervalDuration, jnxpwAtmPerf1DayIntervalNumber=jnxpwAtmPerf1DayIntervalNumber, jnxpwAtmInboundNto1Table=jnxpwAtmInboundNto1Table, jnxpwAtmOutboundNto1Vci=jnxpwAtmOutboundNto1Vci, jnxpwAtmPerfIntervalDuration=jnxpwAtmPerfIntervalDuration, jnxpwAtmPerfIntervalEntry=jnxpwAtmPerfIntervalEntry, jnxpwAtmInboundNto1MappedVpi=jnxpwAtmInboundNto1MappedVpi, jnxpwAtmInboundNto1RowStatus=jnxpwAtmInboundNto1RowStatus, PYSNMP_MODULE_ID=jnxPWAtmMIB, jnxpwAtmOutboundNto1Vpi=jnxpwAtmOutboundNto1Vpi, jnxpwAtmPerfCurrentEntry=jnxpwAtmPerfCurrentEntry, jnxpwAtmPerf1DayIntervalCellsDropped=jnxpwAtmPerf1DayIntervalCellsDropped, jnxpwAtmInboundNto1Entry=jnxpwAtmInboundNto1Entry, jnxpwAtmInboundNto1TrafficParamDescr=jnxpwAtmInboundNto1TrafficParamDescr, jnxpwAtmPerfCurrentPktsMisOrder=jnxpwAtmPerfCurrentPktsMisOrder, jnxpwAtmPerfIntervalCellsDropped=jnxpwAtmPerfIntervalCellsDropped, jnxpwAtmCfgFarEndMaxCellConcatenation=jnxpwAtmCfgFarEndMaxCellConcatenation, jnxPWAtmMIB=jnxPWAtmMIB, jnxpwAtmPerf1DayIntervalPktsReceived=jnxpwAtmPerf1DayIntervalPktsReceived, jnxpwAtmObjects=jnxpwAtmObjects, jnxpwAtmPerfIntervalUnknownCells=jnxpwAtmPerfIntervalUnknownCells, jnxpwAtmCfgEntry=jnxpwAtmCfgEntry, jnxpwAtmPerf1DayIntervalTable=jnxpwAtmPerf1DayIntervalTable, jnxpwAtmPerf1DayIntervalMissingPkts=jnxpwAtmPerf1DayIntervalMissingPkts, jnxpwAtmInboundNto1MappedVci=jnxpwAtmInboundNto1MappedVci, jnxpwAtmCfgTable=jnxpwAtmCfgTable, jnxpwAtmPerf1DayIntervalPktsTimeout=jnxpwAtmPerf1DayIntervalPktsTimeout, jnxpwAtmPerfCurrentPktsReOrder=jnxpwAtmPerfCurrentPktsReOrder, jnxpwAtmPerfIntervalPktsTimeout=jnxpwAtmPerfIntervalPktsTimeout, jnxpwAtmPerfCurrentPktsTimeout=jnxpwAtmPerfCurrentPktsTimeout, jnxpwAtmPerfCurrentTable=jnxpwAtmPerfCurrentTable, jnxpwAtmOutboundNto1Table=jnxpwAtmOutboundNto1Table, jnxpwAtmPerfCurrentPktsReceived=jnxpwAtmPerfCurrentPktsReceived, jnxpwAtmPerfCurrentUnknownCells=jnxpwAtmPerfCurrentUnknownCells, jnxpwAtmPerf1DayIntervalPktsXmit=jnxpwAtmPerf1DayIntervalPktsXmit, jnxpwAtmPerfIntervalValidData=jnxpwAtmPerfIntervalValidData)
