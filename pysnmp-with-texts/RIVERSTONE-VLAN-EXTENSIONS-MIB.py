#
# PySNMP MIB module RIVERSTONE-VLAN-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-VLAN-EXTENSIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
dot1qVlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Integer32, ModuleIdentity, iso, ObjectIdentity, Counter64, TimeTicks, MibIdentifier, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Integer32", "ModuleIdentity", "iso", "ObjectIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Counter32", "NotificationType")
TruthValue, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention")
rsVlanExtensionsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 65))
rsVlanExtensionsMIB.setRevisions(('2004-12-06 00:00', '2002-08-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsVlanExtensionsMIB.setRevisionsDescriptions(('Added: rsPortCustomerVlanStatsTable per-port, per-customer, per-vlan statistics rsPortHCCustomerVlanStatsTable High-Capacity version of rsPortCustomerVlanStatsTable rsCustomerVlanStatsTable per-customer, per-vlan cumulative statistics rsCustomerHCVlanStatsTable High-Capacity version of rsCustomerVlanStatsTable ', 'Initial version of Riverstone VLAN extensions.',))
if mibBuilder.loadTexts: rsVlanExtensionsMIB.setLastUpdated('200412060000Z')
if mibBuilder.loadTexts: rsVlanExtensionsMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rsVlanExtensionsMIB.setContactInfo('Riverstone Networks Customer Service Postal: Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA 95054 USA PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsVlanExtensionsMIB.setDescription('This module complements VLAN information in qBridgeMIB from RFC2674.')
rsVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1))
rsVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2))
rsVlanStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10))
rsVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 1))
rsVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2))
rsPortVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1), )
if mibBuilder.loadTexts: rsPortVlanStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanStatsTable.setDescription('A table that has statistics not defined in dot1qPortVlanStatisticsTable.')
rsPortVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortVlanStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanStatsEntry.setDescription('More traffic statistics for a VLAN on a physical interface.')
rsPortVlanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 101), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanInOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanInOctets.setDescription('The number of octets of the frames received by this port from its segment that were classified as belonging to this VLAN. Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortVlanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 102), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanOutOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanOutOctets.setDescription('The number of octets of the valid frames transmitted by this port from its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortVlanInOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 103), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanInOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanInOverflowOctets.setDescription('The number of times the associated rsPortVlanInOctets counter has overflowed.')
rsPortVlanOutOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 1, 1, 104), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanOutOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanOutOverflowOctets.setDescription('The number of times the associated rsPortVlanOutOctets counter has overflowed.')
rsPortVlanHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2), )
if mibBuilder.loadTexts: rsPortVlanHCStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanHCStatsTable.setDescription('A table that has statistics not defined in dot1qPortVlanHCStatisticsTable.')
rsPortVlanHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortVlanHCStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanHCStatsEntry.setDescription('More traffic statistics for a VLAN on a physical interface.')
rsPortVlanHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1, 101), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanHCInOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanHCInOctets.setDescription('The number of octets of the frames received by this port from its segment that were classified as belonging to this VLAN. Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortVlanHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 2, 1, 102), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortVlanHCOutOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanHCOutOctets.setDescription('The number of octets of the valid frames transmitted by this port from its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3), )
if mibBuilder.loadTexts: rsPortCustomerVlanStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanStatsTable.setDescription('A table that has statistics not defined in dot1qPortVlanStatsTable. This table provides statistics per-port, per-customer, per-vlan. Transparent VLAN is shown as dot1qVlanIndex of 0x7000 (28672). ')
rsPortCustomerVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortCustomerVlanStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanStatsEntry.setDescription('More traffic statistics for a VLAN on a physical interface per customer.')
rsPortCustomerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rsPortCustomerIndex.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerIndex.setDescription('Customer Index under which this vlan falls')
rsPortCustomerVlanInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(a)')
if mibBuilder.loadTexts: rsPortCustomerVlanInFrames.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanInFrames.setDescription('The number of valid frames received by this port from its segment which were classified as belonging to this VLAN. Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(d)')
if mibBuilder.loadTexts: rsPortCustomerVlanOutFrames.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanOutFrames.setDescription('The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInDiscards.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3')
if mibBuilder.loadTexts: rsPortCustomerVlanInDiscards.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanInDiscards.setDescription('The number of valid frames received by this port from its segment which were classified as belonging to this VLAN which were discarded due to VLAN related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering.')
rsPortCustomerVlanInOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowFrames.setReference('ISO/IEC 15802-3 Section 14.6.1.1.3')
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowFrames.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowFrames.setDescription('The number of times the associated rsPortCustomerVlanPortInFrames counter has overflowed.')
rsPortCustomerVlanOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutOverflowFrames.setReference('ISO/IEC 15802-3 Section 14.6.1.1.3')
if mibBuilder.loadTexts: rsPortCustomerVlanOutOverflowFrames.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanOutOverflowFrames.setDescription('The number of times the associated rsPortCustomerVlanPortOutFrames counter has overflowed.')
rsPortCustomerVlanInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowDiscards.setReference('ISO/IEC 15802-3 Section 14.6.1.1.3')
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowDiscards.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowDiscards.setDescription('The number of times the associated rsPortCustomerVlanPortInDiscards counter has overflowed.')
rsPortCustomerVlanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanInOctets.setDescription('The number of octets of the frames received by this port from its segment that were classified as belonging to this VLAN. Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanOutOctets.setDescription('The number of octets of the valid frames transmitted by this port from its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanInOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanInOverflowOctets.setDescription('The number of times the associated rsPortCustomerVlanInOctets counter has overflowed.')
rsPortCustomerVlanOutOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanOutOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanOutOverflowOctets.setDescription('The number of times the associated rsPortCustomerVlanOutOctets counter has overflowed.')
rsPortCustomerVlanHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4), )
if mibBuilder.loadTexts: rsPortCustomerVlanHCStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCStatsTable.setDescription('A table that has statistics not defined in dot1qPortVlanHCStatsTable. This table provides statistics per-port, per-customer, per-vlan. Transparent VLAN is shown as dot1qVlanIndex of 0x7000 (28672). ')
rsPortCustomerVlanHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsPortCustomerVlanHCStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCStatsEntry.setDescription('More traffic statistics for a VLAN on a physical interface per-customer.')
rsPortCustomerVlanHCInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCInFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(a)')
if mibBuilder.loadTexts: rsPortCustomerVlanHCInFrames.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCInFrames.setDescription('The number of valid frames received by this port from its segment which were classified as belonging to this VLAN. Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanHCOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCOutFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(d)')
if mibBuilder.loadTexts: rsPortCustomerVlanHCOutFrames.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCOutFrames.setDescription('The number of valid frames transmitted by this port to its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanHCInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCInDiscards.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3')
if mibBuilder.loadTexts: rsPortCustomerVlanHCInDiscards.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCInDiscards.setDescription('The number of valid frames received by this port from its segment which were classified as belonging to this VLAN which were discarded due to VLAN related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering.')
rsPortCustomerVlanHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCInOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCInOctets.setDescription('The number of octets of the frames received by this port from its segment that were classified as belonging to this VLAN. Note that a frame received on this port is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsPortCustomerVlanHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPortCustomerVlanHCOutOctets.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCOutOctets.setDescription('The number of octets of the valid frames transmitted by this port from its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5), )
if mibBuilder.loadTexts: rsCustomerVlanStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanStatsTable.setDescription('A table that has statistics not defined in dot1qPortVlanStatsTable. This table provides cumulative statistics per-customer, per-vlan from all the physical-ports. Transparent VLAN is shown as dot1qVlanIndex of 0x7000 (28672). ')
rsCustomerVlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1), ).setIndexNames((0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsCustomerVlanStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanStatsEntry.setDescription('Cumulative traffic statistics for a VLAN from physical interfaces per-customer.')
rsCustomerVlanInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(a)')
if mibBuilder.loadTexts: rsCustomerVlanInFrames.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanInFrames.setDescription('The number of valid frames received by the ports from its segment which were classified as belonging to this VLAN. Note that a frame received on the ports is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(d)')
if mibBuilder.loadTexts: rsCustomerVlanOutFrames.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanOutFrames.setDescription('The number of valid frames transmitted by the ports to its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInDiscards.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3')
if mibBuilder.loadTexts: rsCustomerVlanInDiscards.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanInDiscards.setDescription('The number of valid frames received by the ports from its segment which were classified as belonging to this VLAN which were discarded due to VLAN related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering.')
rsCustomerVlanInOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOverflowFrames.setReference('ISO/IEC 15802-3 Section 14.6.1.1.3')
if mibBuilder.loadTexts: rsCustomerVlanInOverflowFrames.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanInOverflowFrames.setDescription('The number of times the associated rsCustomerVlanPortInFrames counter has overflowed.')
rsCustomerVlanOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutOverflowFrames.setReference('ISO/IEC 15802-3 Section 14.6.1.1.3')
if mibBuilder.loadTexts: rsCustomerVlanOutOverflowFrames.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanOutOverflowFrames.setDescription('The number of times the associated rsCustomerVlanPortOutFrames counter has overflowed.')
rsCustomerVlanInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOverflowDiscards.setReference('ISO/IEC 15802-3 Section 14.6.1.1.3')
if mibBuilder.loadTexts: rsCustomerVlanInOverflowDiscards.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanInOverflowDiscards.setDescription('The number of times the associated rsCustomerVlanPortInDiscards counter has overflowed.')
rsCustomerVlanInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOctets.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanInOctets.setDescription('The number of octets of the frames received by the ports from its segment that were classified as belonging to this VLAN. Note that a frame received on the ports is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutOctets.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanOutOctets.setDescription('The number of octets of the valid frames transmitted by the ports from its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanInOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanInOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanInOverflowOctets.setDescription('The number of times the associated rsCustomerVlanInOctets counter has overflowed.')
rsCustomerVlanOutOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanOutOverflowOctets.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanOutOverflowOctets.setDescription('The number of times the associated rsCustomerVlanOutOctets counter has overflowed.')
rsCustomerVlanHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6), )
if mibBuilder.loadTexts: rsCustomerVlanHCStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCStatsTable.setDescription('A table that has statistics not defined in dot1qPortVlanHCStatsTable. This table provides cumulative statistics per-customer, per-vlan from all the physical-ports. Transparent VLAN is shown as dot1qVlanIndex of 0x7000 (28672). ')
rsCustomerVlanHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1), ).setIndexNames((0, "RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerIndex"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rsCustomerVlanHCStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCStatsEntry.setDescription('Cumulative traffic statistics for a VLAN from physical interfaces per-customer.')
rsCustomerVlanHCInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCInFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(a)')
if mibBuilder.loadTexts: rsCustomerVlanHCInFrames.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCInFrames.setDescription('The number of valid frames received by the ports from its segment which were classified as belonging to this VLAN. Note that a frame received on the ports is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanHCOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCOutFrames.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3(d)')
if mibBuilder.loadTexts: rsCustomerVlanHCOutFrames.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCOutFrames.setDescription('The number of valid frames transmitted by the ports to its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanHCInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCInDiscards.setReference('IEEE 802.1Q/D11 Section 12.6.1.1.3')
if mibBuilder.loadTexts: rsCustomerVlanHCInDiscards.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCInDiscards.setDescription('The number of valid frames received by the ports from its segment which were classified as belonging to this VLAN which were discarded due to VLAN related reasons. Specifically, the IEEE 802.1Q counters for Discard Inbound and Discard on Ingress Filtering.')
rsCustomerVlanHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCInOctets.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCInOctets.setDescription('The number of octets of the frames received by the ports from its segment that were classified as belonging to this VLAN. Note that a frame received on the ports is counted by this object if and only if it is for a protocol being processed by the local forwarding process for this VLAN. This object includes received bridge management frames classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsCustomerVlanHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 65, 1, 10, 6, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCustomerVlanHCOutOctets.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCOutOctets.setDescription('The number of octets of the valid frames transmitted by the ports from its segment from the local forwarding process for this VLAN. This includes bridge management frames originated by this device which are classified as belonging to this VLAN (e.g. GMRP, but not GVRP or STP).')
rsVlanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 1, 1)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanStatsOverflowGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanStatsOverflowGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanStatsGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanStatsOverflowGroup"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsVlanCompliance = rsVlanCompliance.setStatus('current')
if mibBuilder.loadTexts: rsVlanCompliance.setDescription('The compliance statement for RIVERSTONE-VLAN-EXTENSIONS-MIB.')
rsPortVlanStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 1)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortVlanStatsGroup = rsPortVlanStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanStatsGroup.setDescription('A collection of additional objects providing per-port packet statistics for all VLANs currently configured on this device.')
rsPortVlanStatsOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 2)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanInOverflowOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanOutOverflowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortVlanStatsOverflowGroup = rsPortVlanStatsOverflowGroup.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanStatsOverflowGroup.setDescription('A collection of additional objects providing overflow counters for per-port packet statistics for all VLANs currently configured on this device for high capacity interfaces, defined as those that have the value of the corresponding instance of ifSpeed greater than 20,000,000 bits/second.')
rsPortVlanHCStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 3)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortVlanHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortVlanHCStatsGroup = rsPortVlanHCStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsPortVlanHCStatsGroup.setDescription('A collection of additional objects providing per-port packet statistics for all VLANs currently configured on this device for high capacity interfaces, defined as those that have the value of the corresponding instance of ifSpeed greater than 20,000,000 bits/second.')
rsPortCustomerVlanStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 4)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortCustomerVlanStatsGroup = rsPortCustomerVlanStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanStatsGroup.setDescription('A collection of additional objects providing per-port statistics for all VLANs currently configured on this device.')
rsPortCustomerVlanStatsOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 5)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanInOverflowOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanOutOverflowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortCustomerVlanStatsOverflowGroup = rsPortCustomerVlanStatsOverflowGroup.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanStatsOverflowGroup.setDescription('A collection of additional objects providing overflow counters for per-port statistics for all VLANs currently configured on this device for high capacity interfaces, defined as those that have the value of the corresponding cumulative instance of ifSpeed greater than 20,000,000 bits/second.')
rsPortCustomerVlanHCStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 6)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsPortCustomerVlanHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsPortCustomerVlanHCStatsGroup = rsPortCustomerVlanHCStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsPortCustomerVlanHCStatsGroup.setDescription('A collection of additional objects providing per-port, per-customer statistics for all VLANs currently configured on this device for high capacity interfaces, defined as those that have the value of the corresponding instance of ifSpeed greater than 20,000,000 bits/second.')
rsCustomerVlanStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 7)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCustomerVlanStatsGroup = rsCustomerVlanStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanStatsGroup.setDescription('A collection of additional objects providing cumulative (all physical ports) statistics for all VLANs currently configured on this device.')
rsCustomerVlanStatsOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 8)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanInOverflowOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanOutOverflowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCustomerVlanStatsOverflowGroup = rsCustomerVlanStatsOverflowGroup.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanStatsOverflowGroup.setDescription('A collection of additional objects providing overflow counters for cumulative statistics for all VLANs currently configured on this device for high capacity interfaces, defined as those that have the value of the corresponding instance of ifSpeed greater than 20,000,000 bits/second.')
rsCustomerVlanHCStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 65, 2, 2, 9)).setObjects(("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCInOctets"), ("RIVERSTONE-VLAN-EXTENSIONS-MIB", "rsCustomerVlanHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCustomerVlanHCStatsGroup = rsCustomerVlanHCStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsCustomerVlanHCStatsGroup.setDescription('A collection of additional objects providing cumulative statistics for all VLANs currently configured on this device for high capacity interfaces, defined as those that have the value of the corresponding instance of ifSpeed greater than 20,000,000 bits/second.')
mibBuilder.exportSymbols("RIVERSTONE-VLAN-EXTENSIONS-MIB", rsPortCustomerVlanInOverflowDiscards=rsPortCustomerVlanInOverflowDiscards, rsVlanGroups=rsVlanGroups, rsCustomerVlanHCInFrames=rsCustomerVlanHCInFrames, rsPortCustomerVlanHCInFrames=rsPortCustomerVlanHCInFrames, rsCustomerVlanHCInOctets=rsCustomerVlanHCInOctets, rsVlanCompliances=rsVlanCompliances, rsCustomerVlanInOverflowDiscards=rsCustomerVlanInOverflowDiscards, rsPortCustomerVlanStatsGroup=rsPortCustomerVlanStatsGroup, rsVlanStats=rsVlanStats, rsCustomerVlanStatsGroup=rsCustomerVlanStatsGroup, rsPortCustomerVlanHCInOctets=rsPortCustomerVlanHCInOctets, rsCustomerVlanHCOutOctets=rsCustomerVlanHCOutOctets, rsCustomerVlanInOverflowFrames=rsCustomerVlanInOverflowFrames, rsPortCustomerVlanInOverflowOctets=rsPortCustomerVlanInOverflowOctets, rsCustomerVlanInOctets=rsCustomerVlanInOctets, rsPortCustomerVlanHCOutFrames=rsPortCustomerVlanHCOutFrames, rsCustomerVlanHCStatsEntry=rsCustomerVlanHCStatsEntry, rsPortVlanHCStatsTable=rsPortVlanHCStatsTable, rsPortVlanOutOctets=rsPortVlanOutOctets, rsPortCustomerVlanHCInDiscards=rsPortCustomerVlanHCInDiscards, rsCustomerVlanInFrames=rsCustomerVlanInFrames, rsCustomerVlanInOverflowOctets=rsCustomerVlanInOverflowOctets, rsPortVlanStatsOverflowGroup=rsPortVlanStatsOverflowGroup, rsPortVlanInOctets=rsPortVlanInOctets, rsPortCustomerVlanStatsTable=rsPortCustomerVlanStatsTable, rsPortCustomerVlanInFrames=rsPortCustomerVlanInFrames, rsPortCustomerVlanOutOctets=rsPortCustomerVlanOutOctets, rsPortVlanHCStatsEntry=rsPortVlanHCStatsEntry, rsPortCustomerVlanHCOutOctets=rsPortCustomerVlanHCOutOctets, rsCustomerVlanInDiscards=rsCustomerVlanInDiscards, rsPortVlanStatsEntry=rsPortVlanStatsEntry, rsCustomerVlanOutOverflowFrames=rsCustomerVlanOutOverflowFrames, rsPortVlanOutOverflowOctets=rsPortVlanOutOverflowOctets, rsPortCustomerVlanHCStatsEntry=rsPortCustomerVlanHCStatsEntry, rsCustomerVlanStatsOverflowGroup=rsCustomerVlanStatsOverflowGroup, rsCustomerVlanStatsTable=rsCustomerVlanStatsTable, rsPortCustomerVlanOutOverflowFrames=rsPortCustomerVlanOutOverflowFrames, rsPortVlanInOverflowOctets=rsPortVlanInOverflowOctets, rsCustomerVlanOutOctets=rsCustomerVlanOutOctets, rsCustomerVlanStatsEntry=rsCustomerVlanStatsEntry, rsCustomerVlanOutOverflowOctets=rsCustomerVlanOutOverflowOctets, rsPortCustomerVlanStatsOverflowGroup=rsPortCustomerVlanStatsOverflowGroup, rsPortCustomerVlanHCStatsGroup=rsPortCustomerVlanHCStatsGroup, rsPortVlanHCOutOctets=rsPortVlanHCOutOctets, rsPortCustomerVlanHCStatsTable=rsPortCustomerVlanHCStatsTable, rsPortCustomerVlanOutFrames=rsPortCustomerVlanOutFrames, rsVlanCompliance=rsVlanCompliance, rsPortVlanStatsGroup=rsPortVlanStatsGroup, PYSNMP_MODULE_ID=rsVlanExtensionsMIB, rsPortCustomerVlanStatsEntry=rsPortCustomerVlanStatsEntry, rsVlanExtensionsMIB=rsVlanExtensionsMIB, rsVlanConformance=rsVlanConformance, rsCustomerVlanHCStatsTable=rsCustomerVlanHCStatsTable, rsPortCustomerVlanInOverflowFrames=rsPortCustomerVlanInOverflowFrames, rsVlanObjects=rsVlanObjects, rsPortVlanStatsTable=rsPortVlanStatsTable, rsPortVlanHCStatsGroup=rsPortVlanHCStatsGroup, rsCustomerVlanHCOutFrames=rsCustomerVlanHCOutFrames, rsPortCustomerVlanInOctets=rsPortCustomerVlanInOctets, rsCustomerVlanHCStatsGroup=rsCustomerVlanHCStatsGroup, rsPortCustomerVlanInDiscards=rsPortCustomerVlanInDiscards, rsCustomerVlanOutFrames=rsCustomerVlanOutFrames, rsCustomerVlanHCInDiscards=rsCustomerVlanHCInDiscards, rsPortVlanHCInOctets=rsPortVlanHCInOctets, rsPortCustomerIndex=rsPortCustomerIndex, rsPortCustomerVlanOutOverflowOctets=rsPortCustomerVlanOutOverflowOctets)
