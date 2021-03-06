#
# PySNMP MIB module DNOS-MVR-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-MVR-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:51:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, Counter32, TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Integer32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Counter32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Integer32", "Bits", "iso")
TimeInterval, TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
fastpathMvr = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50))
fastpathMvr.setRevisions(('2011-01-26 00:00', '2009-10-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastpathMvr.setRevisionsDescriptions(('Postal address updated.', 'Initial version.',))
if mibBuilder.loadTexts: fastpathMvr.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastpathMvr.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastpathMvr.setContactInfo('')
if mibBuilder.loadTexts: fastpathMvr.setDescription('The Broadcom Private MIB for MVR Configuration')
mvrGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1))
mvrAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrAdminMode.setStatus('current')
if mibBuilder.loadTexts: mvrAdminMode.setDescription('Enable/Disable MVR. The value true(1) indicates that MVR is enabled A value of false(2) indicates that MVR is disabled.')
mvrModeType = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("compatible", 1), ("dynamic", 2))).clone('compatible')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrModeType.setStatus('current')
if mibBuilder.loadTexts: mvrModeType.setDescription('Shows/Changes MVR mode. The value compatible(1) indicates that compatible mode is enabled. A value of dynamic(2) indicates that dynamic mode is enabled.')
mvrMulticastVlanId = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 3), VlanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrMulticastVlanId.setStatus('current')
if mibBuilder.loadTexts: mvrMulticastVlanId.setDescription('Shows/Changes the Multicast Vlan number.')
mvrMaxMulticastGroupsCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrMaxMulticastGroupsCount.setStatus('current')
if mibBuilder.loadTexts: mvrMaxMulticastGroupsCount.setDescription('The maximum number of multicast groups that is supported by MVR.')
mvrCurrentMulticastGroupsCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrCurrentMulticastGroupsCount.setStatus('current')
if mibBuilder.loadTexts: mvrCurrentMulticastGroupsCount.setDescription('The current number of MVR groups allocated.')
mvrQueryTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 1, 6), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrQueryTime.setStatus('current')
if mibBuilder.loadTexts: mvrQueryTime.setDescription('Shows/Changes the MVR Query time, in centiseconds.')
mvrPortTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2), )
if mibBuilder.loadTexts: mvrPortTable.setStatus('current')
if mibBuilder.loadTexts: mvrPortTable.setDescription('A table of MVR control information about every bridge port. This is indexed by mvrBasePort.')
mvrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mvrPortEntry.setStatus('current')
if mibBuilder.loadTexts: mvrPortEntry.setDescription('MVR control information for a bridge port.')
mvrPortMvrEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrPortMvrEnabled.setStatus('current')
if mibBuilder.loadTexts: mvrPortMvrEnabled.setDescription('Enable\\Disable MVR on port. The value true(1) indicates that MVR is enabled. A value of false(2) indicates that MVR is disabled.')
mvrPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("source", 1), ("receiver", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrPortType.setStatus('current')
if mibBuilder.loadTexts: mvrPortType.setDescription('MVR Interface type.')
mvrPortImmediateLeaveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mvrPortImmediateLeaveMode.setStatus('current')
if mibBuilder.loadTexts: mvrPortImmediateLeaveMode.setDescription('Shows/Changes Immediate Leave mode for MVR port. The value true(1) indicates that the port is in Immediate Leave mode. A value of false(2) indicates that the port is not in Immediate Leave mode.')
mvrPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("activeInVlan", 1), ("activeNotInVlan", 2), ("inactiveInVlan", 3), ("inactiveNotInVlan", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrPortStatus.setStatus('current')
if mibBuilder.loadTexts: mvrPortStatus.setDescription('The interface status.')
mvrGroupsTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3), )
if mibBuilder.loadTexts: mvrGroupsTable.setStatus('current')
if mibBuilder.loadTexts: mvrGroupsTable.setDescription('A table of MVR groups.')
mvrGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1), ).setIndexNames((0, "DNOS-MVR-PRIVATE-MIB", "mvrGroupIPAddress"))
if mibBuilder.loadTexts: mvrGroupEntry.setStatus('current')
if mibBuilder.loadTexts: mvrGroupEntry.setDescription('MVR information of membership group.')
mvrGroupIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrGroupIPAddress.setStatus('current')
if mibBuilder.loadTexts: mvrGroupIPAddress.setDescription('The multicast Group IP address.')
mvrGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrGroupStatus.setStatus('current')
if mibBuilder.loadTexts: mvrGroupStatus.setDescription('The status of the specific MVR group.')
mvrGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: mvrGroupRowStatus.setDescription("The status of this conceptual row.To create a row in this table, a manager must set this object to 'createAndGo'(4) .To delete a row in this table, a manager must set this object to `destroy'(6)")
mvrPortMembershipTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4), )
if mibBuilder.loadTexts: mvrPortMembershipTable.setStatus('current')
if mibBuilder.loadTexts: mvrPortMembershipTable.setDescription('A table of MVR membership groups.')
mvrPortMembershipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1), ).setIndexNames((0, "DNOS-MVR-PRIVATE-MIB", "mvrPortMembershipGroupIPAddress"), (0, "DNOS-MVR-PRIVATE-MIB", "mvrPortMembershipPortIfIndex"))
if mibBuilder.loadTexts: mvrPortMembershipEntry.setStatus('current')
if mibBuilder.loadTexts: mvrPortMembershipEntry.setDescription('MVR information of membership group.')
mvrPortMembershipGroupIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrPortMembershipGroupIPAddress.setStatus('current')
if mibBuilder.loadTexts: mvrPortMembershipGroupIPAddress.setDescription('The multicast Group IP address.')
mvrPortMembershipPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrPortMembershipPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: mvrPortMembershipPortIfIndex.setDescription("Interface index in 'ifTable'.")
mvrPortMembershipRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mvrPortMembershipRowStatus.setStatus('current')
if mibBuilder.loadTexts: mvrPortMembershipRowStatus.setDescription("The status of this conceptual row.To create a row in this table, a manager must set this object to 'createAndGo'(4) .To delete a row in this table, a manager must set this object to `destroy'(6)")
mvrStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5))
mvrIGMPQueryReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPQueryReceived.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPQueryReceived.setDescription('Number of received IGMP Queries. ')
mvrIGMPReportV1Received = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV1Received.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPReportV1Received.setDescription('Number of received IGMP Reports V1. ')
mvrIGMPReportV2Received = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV2Received.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPReportV2Received.setDescription('Number of received IGMP Reports V1. ')
mvrIGMPLeaveReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPLeaveReceived.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPLeaveReceived.setDescription('Number of received IGMP Leaves. ')
mvrIGMPQueryTransmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPQueryTransmitted.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPQueryTransmitted.setDescription('Number of transmitted IGMP Queries. ')
mvrIGMPReportV1Transmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV1Transmitted.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPReportV1Transmitted.setDescription('Number of transmitted IGMP Reports V1. ')
mvrIGMPReportV2Transmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPReportV2Transmitted.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPReportV2Transmitted.setDescription('Number of transmitted IGMP Reports V2. ')
mvrIGMPLeaveTransmitted = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPLeaveTransmitted.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPLeaveTransmitted.setDescription('Number of transmitted IGMP Leaves. ')
mvrIGMPPacketReceiveFailures = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPPacketReceiveFailures.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPPacketReceiveFailures.setDescription('Number of failures on receiving the IGMP packets. ')
mvrIGMPPacketTransmitFailures = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 50, 5, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mvrIGMPPacketTransmitFailures.setStatus('current')
if mibBuilder.loadTexts: mvrIGMPPacketTransmitFailures.setDescription('Number of failures on transmitting the IGMP packets. ')
mibBuilder.exportSymbols("DNOS-MVR-PRIVATE-MIB", mvrIGMPReportV2Received=mvrIGMPReportV2Received, mvrGroupsTable=mvrGroupsTable, fastpathMvr=fastpathMvr, mvrPortType=mvrPortType, mvrPortMembershipPortIfIndex=mvrPortMembershipPortIfIndex, mvrIGMPLeaveReceived=mvrIGMPLeaveReceived, mvrQueryTime=mvrQueryTime, mvrMaxMulticastGroupsCount=mvrMaxMulticastGroupsCount, mvrMulticastVlanId=mvrMulticastVlanId, mvrPortMembershipRowStatus=mvrPortMembershipRowStatus, mvrModeType=mvrModeType, mvrPortTable=mvrPortTable, mvrGroupRowStatus=mvrGroupRowStatus, mvrPortMembershipEntry=mvrPortMembershipEntry, mvrIGMPQueryReceived=mvrIGMPQueryReceived, mvrIGMPLeaveTransmitted=mvrIGMPLeaveTransmitted, mvrStatistics=mvrStatistics, mvrPortImmediateLeaveMode=mvrPortImmediateLeaveMode, mvrPortMvrEnabled=mvrPortMvrEnabled, mvrGroupIPAddress=mvrGroupIPAddress, mvrPortStatus=mvrPortStatus, mvrIGMPQueryTransmitted=mvrIGMPQueryTransmitted, mvrIGMPReportV1Received=mvrIGMPReportV1Received, mvrIGMPPacketReceiveFailures=mvrIGMPPacketReceiveFailures, mvrPortMembershipGroupIPAddress=mvrPortMembershipGroupIPAddress, mvrIGMPReportV1Transmitted=mvrIGMPReportV1Transmitted, mvrIGMPPacketTransmitFailures=mvrIGMPPacketTransmitFailures, mvrGlobalConfig=mvrGlobalConfig, PYSNMP_MODULE_ID=fastpathMvr, mvrAdminMode=mvrAdminMode, mvrGroupEntry=mvrGroupEntry, mvrCurrentMulticastGroupsCount=mvrCurrentMulticastGroupsCount, mvrPortMembershipTable=mvrPortMembershipTable, mvrGroupStatus=mvrGroupStatus, mvrPortEntry=mvrPortEntry, mvrIGMPReportV2Transmitted=mvrIGMPReportV2Transmitted)
