#
# PySNMP MIB module AT-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-IGMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Counter32, iso, IpAddress, ModuleIdentity, Counter64, Bits, Unsigned32, NotificationType, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Counter32", "iso", "IpAddress", "ModuleIdentity", "Counter64", "Bits", "Unsigned32", "NotificationType", "MibIdentifier", "Integer32")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
igmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139))
igmp.setRevisions(('2007-08-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: igmp.setRevisionsDescriptions(('Initial version, to support IGMP membership status polling.',))
if mibBuilder.loadTexts: igmp.setLastUpdated('200708080000Z')
if mibBuilder.loadTexts: igmp.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: igmp.setContactInfo(' Stan Xiang,Hamish Kellahan Allied Telesis EMail: support@alliedtelesis.co.nz')
if mibBuilder.loadTexts: igmp.setDescription('The MIB module for IGMP Management.')
igmpIntInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1))
igmpIntMember = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9))
igmpSnooping = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10))
igmpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1), )
if mibBuilder.loadTexts: igmpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceTable.setDescription('The (conceptual) table listing IGMP capable IP interfaces.')
igmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1), ).setIndexNames((0, "AT-IGMP-MIB", "igmpInterface"))
if mibBuilder.loadTexts: igmpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceEntry.setDescription('An entry (conceptual row) in the igmpInterfaceTable.')
igmpInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterface.setStatus('current')
if mibBuilder.loadTexts: igmpInterface.setDescription('The index value of the interface for which IGMP is enabled. This table is indexed by this value.')
igmpInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceName.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceName.setDescription('The name of the interface for which IGMP or MLD is enabled.')
igmpQueryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpQueryTimeout.setStatus('current')
if mibBuilder.loadTexts: igmpQueryTimeout.setDescription('It represents the maximum expected time interval, in seconds, between successive IGMP general query messages arriving on the interface. A vlaue of zero means there is no limits.')
igmpProxy = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("upstream", 1), ("downstream", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpProxy.setStatus('current')
if mibBuilder.loadTexts: igmpProxy.setDescription('The object represents states of igmp proxy. When it has a value of 0 then it means the inteface proxy is currently disabled. When it has a value of 1 then it means IGMP is performing upstream inteface proxying. When it has a value of 2 then it means IGMP is performing downstream inteface proxying.')
igmpIntStatsTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2), )
if mibBuilder.loadTexts: igmpIntStatsTable.setStatus('current')
if mibBuilder.loadTexts: igmpIntStatsTable.setDescription('The (conceptual) table listing statistics for IGMP capable IP interfaces.')
igmpIntStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1), ).setIndexNames((0, "AT-IGMP-MIB", "igmpInterface"))
if mibBuilder.loadTexts: igmpIntStatsEntry.setStatus('current')
if mibBuilder.loadTexts: igmpIntStatsEntry.setDescription('An entry (conceptual row) in the igmpIntStatsTable.')
igmpInQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInQuery.setStatus('current')
if mibBuilder.loadTexts: igmpInQuery.setDescription('The number of IGMP Query messages received by the interface.')
igmpInReportV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInReportV1.setStatus('current')
if mibBuilder.loadTexts: igmpInReportV1.setDescription('The number of IGMP version 1 Report messages received by the interface.')
igmpInReportV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInReportV2.setStatus('current')
if mibBuilder.loadTexts: igmpInReportV2.setDescription('The number of IGMP version 2 Report messages received by the interface.')
igmpInLeave = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInLeave.setStatus('current')
if mibBuilder.loadTexts: igmpInLeave.setDescription('The number of IGMP Leave Group messages received by the interface.')
igmpInTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInTotal.setStatus('current')
if mibBuilder.loadTexts: igmpInTotal.setDescription('The total number of IGMP messages received by the interface.')
igmpOutQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpOutQuery.setStatus('current')
if mibBuilder.loadTexts: igmpOutQuery.setDescription('The total number of IGMP Query messages that were transmitted by the switch over the interface.')
igmpOutTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpOutTotal.setStatus('current')
if mibBuilder.loadTexts: igmpOutTotal.setDescription('The total number of IGMP messages that were transmitted by the switch over the interface.')
igmpBadQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpBadQuery.setStatus('current')
if mibBuilder.loadTexts: igmpBadQuery.setDescription('The number of IGMP membership query messages with errors that were received by the interface.')
igmpBadReportV1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpBadReportV1.setStatus('current')
if mibBuilder.loadTexts: igmpBadReportV1.setDescription('The number of IGMP Version 1 membership report messages with errors that were received by the interface.')
igmpBadReportV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpBadReportV2.setStatus('current')
if mibBuilder.loadTexts: igmpBadReportV2.setDescription('The number of IGMP Version 2 membership report messages with errors that were received by the interface.')
igmpBadLeave = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpBadLeave.setStatus('current')
if mibBuilder.loadTexts: igmpBadLeave.setDescription('The number of IGMP Leave Group messages with errors that were received by the interface.')
igmpBadTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpBadTotal.setStatus('current')
if mibBuilder.loadTexts: igmpBadTotal.setDescription('The total number of IGMP messages with errors that were received by the interface..')
igmpIntGroupTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1), )
if mibBuilder.loadTexts: igmpIntGroupTable.setStatus('current')
if mibBuilder.loadTexts: igmpIntGroupTable.setDescription('The (conceptual) table listing the IP multicast groups of which there are members on a particular interface.')
igmpIntGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1), ).setIndexNames((0, "AT-IGMP-MIB", "igmpInterface"))
if mibBuilder.loadTexts: igmpIntGroupEntry.setStatus('current')
if mibBuilder.loadTexts: igmpIntGroupEntry.setDescription('An entry (conceptual row) in the igmpGroupTable.')
igmpIntGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpIntGroupAddress.setStatus('current')
if mibBuilder.loadTexts: igmpIntGroupAddress.setDescription('The IP multicast group address for which this entry contains information.')
igmpLastHost = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpLastHost.setStatus('current')
if mibBuilder.loadTexts: igmpLastHost.setDescription('The IP address of the last host reporting a membership. If it is static, then 0.0.0.0 presents.')
igmpRefreshTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRefreshTime.setStatus('current')
if mibBuilder.loadTexts: igmpRefreshTime.setDescription('The time in seconds until the membership group is deleted if another membership report is not received. A value of 0xffffffff means infinity.')
igmpSnoopAdminInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 1))
igmpSnoopAdminEnabled = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopAdminEnabled.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopAdminEnabled.setDescription('Indicates whether IGMP Snooping is globally enabled.')
igmpSnoopVlanTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2), )
if mibBuilder.loadTexts: igmpSnoopVlanTable.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopVlanTable.setDescription('The (conceptual) table listing the layer 2 interfaces performing IGMP snooping.')
igmpSnoopVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1), ).setIndexNames((0, "AT-IGMP-MIB", "igmpSnoopVID"))
if mibBuilder.loadTexts: igmpSnoopVlanEntry.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopVlanEntry.setDescription('An entry (conceptual row) in the IGMP Snooping Vlan Table.')
igmpSnoopVID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopVID.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopVID.setDescription('The 802.1 VLAN ID of the layer 2 interface performing IGMP snooping.')
igmpSnoopVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopVlanName.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopVlanName.setDescription('The name of the layer 2 interface performing IGMP snooping.')
igmpSnoopFastLeave = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("single", 1), ("multi", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopFastLeave.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopFastLeave.setDescription('Indicates whether FastLeave is enabled, and operating in Single-Host or Multi-Host mode.')
igmpSnoopQuerySolicit = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopQuerySolicit.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopQuerySolicit.setDescription('Indicates whether query solicitation is on')
igmpSnoopStaticRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopStaticRouterPorts.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopStaticRouterPorts.setDescription('Indicates the configured static multicast router ports.')
igmpSnoopGroupTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3), )
if mibBuilder.loadTexts: igmpSnoopGroupTable.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopGroupTable.setDescription('The (conceptual) table of IGMP Groups snooped on a layer 2 interface.')
igmpSnoopGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3, 1), ).setIndexNames((0, "AT-IGMP-MIB", "igmpSnoopVID"), (0, "AT-IGMP-MIB", "igmpSnoopGroupAddress"))
if mibBuilder.loadTexts: igmpSnoopGroupEntry.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopGroupEntry.setDescription('A (conceptual) row in the IGMP Snooping Group table.')
igmpSnoopGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopGroupAddress.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopGroupAddress.setDescription('The Multicast Group IP Address detected on a layer 2 interface.')
igmpSnoopGroupTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopGroupTimer.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopGroupTimer.setDescription('The time remaining before the multicast group is deleted from the layer 2 interface.')
igmpSnoopPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4), )
if mibBuilder.loadTexts: igmpSnoopPortTable.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopPortTable.setDescription('A (conceptual) table of ports in a layer 2 interface that are currently members of a multicast group.')
igmpSnoopPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1), ).setIndexNames((0, "AT-IGMP-MIB", "igmpSnoopVID"), (0, "AT-IGMP-MIB", "igmpSnoopGroupAddress"), (0, "AT-IGMP-MIB", "igmpSnoopPortNumber"))
if mibBuilder.loadTexts: igmpSnoopPortEntry.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopPortEntry.setDescription('A (conceptual) row in the IGMP Snooping Port Table.')
igmpSnoopPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopPortNumber.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopPortNumber.setDescription('Provides the number of a port in a multicast group.')
igmpSnoopPortIsStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopPortIsStatic.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopPortIsStatic.setDescription('Indicates whether a port has been administratively added to a multicast group.')
igmpSnoopPortTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopPortTimer.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopPortTimer.setDescription('Indicates the time remaining before the port is removed.')
igmpSnoopHostTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5), )
if mibBuilder.loadTexts: igmpSnoopHostTable.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopHostTable.setDescription('A (conceptual) table of hosts receiving multicast data.')
igmpSnoopHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1), ).setIndexNames((0, "AT-IGMP-MIB", "igmpSnoopVID"), (0, "AT-IGMP-MIB", "igmpSnoopGroupAddress"), (0, "AT-IGMP-MIB", "igmpSnoopPortNumber"), (0, "AT-IGMP-MIB", "igmpSnoopHostMAC"))
if mibBuilder.loadTexts: igmpSnoopHostEntry.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopHostEntry.setDescription('A (conceptual) row in the IGMP Snooping Host Table.')
igmpSnoopHostMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopHostMAC.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopHostMAC.setDescription('Provides the Media Access Control Address of an IGMP Host.')
igmpSnoopHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopHostIpAddress.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopHostIpAddress.setDescription('Provides the Internet Protocol Address of an IGMP Host.')
igmpSnoopHostTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpSnoopHostTimer.setStatus('current')
if mibBuilder.loadTexts: igmpSnoopHostTimer.setDescription('Indicates the time remaining before the host times out.')
mibBuilder.exportSymbols("AT-IGMP-MIB", igmpInReportV1=igmpInReportV1, igmpSnoopQuerySolicit=igmpSnoopQuerySolicit, igmpBadQuery=igmpBadQuery, igmpOutQuery=igmpOutQuery, igmpInterfaceEntry=igmpInterfaceEntry, igmpIntStatsTable=igmpIntStatsTable, igmpProxy=igmpProxy, igmpIntGroupTable=igmpIntGroupTable, igmpSnoopAdminEnabled=igmpSnoopAdminEnabled, igmpSnoopFastLeave=igmpSnoopFastLeave, igmpIntMember=igmpIntMember, igmpRefreshTime=igmpRefreshTime, igmpSnoopPortTimer=igmpSnoopPortTimer, igmpIntInfo=igmpIntInfo, igmpSnoopGroupAddress=igmpSnoopGroupAddress, igmpSnoopVlanName=igmpSnoopVlanName, igmpIntGroupEntry=igmpIntGroupEntry, igmpSnoopAdminInfo=igmpSnoopAdminInfo, igmpInQuery=igmpInQuery, igmpBadTotal=igmpBadTotal, igmpBadReportV1=igmpBadReportV1, igmp=igmp, igmpSnoopGroupEntry=igmpSnoopGroupEntry, igmpBadReportV2=igmpBadReportV2, igmpInterface=igmpInterface, igmpIntGroupAddress=igmpIntGroupAddress, PYSNMP_MODULE_ID=igmp, igmpSnoopVlanTable=igmpSnoopVlanTable, igmpSnoopGroupTimer=igmpSnoopGroupTimer, igmpSnoopHostTable=igmpSnoopHostTable, igmpSnoopHostIpAddress=igmpSnoopHostIpAddress, igmpIntStatsEntry=igmpIntStatsEntry, igmpBadLeave=igmpBadLeave, igmpSnoopPortEntry=igmpSnoopPortEntry, igmpLastHost=igmpLastHost, igmpQueryTimeout=igmpQueryTimeout, igmpSnoopGroupTable=igmpSnoopGroupTable, igmpSnoopHostMAC=igmpSnoopHostMAC, igmpSnoopPortIsStatic=igmpSnoopPortIsStatic, igmpInTotal=igmpInTotal, igmpInterfaceName=igmpInterfaceName, igmpSnoopPortNumber=igmpSnoopPortNumber, igmpSnoopHostEntry=igmpSnoopHostEntry, igmpSnoopStaticRouterPorts=igmpSnoopStaticRouterPorts, igmpSnoopVID=igmpSnoopVID, igmpSnoopHostTimer=igmpSnoopHostTimer, igmpSnoopPortTable=igmpSnoopPortTable, igmpInReportV2=igmpInReportV2, igmpInLeave=igmpInLeave, igmpSnooping=igmpSnooping, igmpSnoopVlanEntry=igmpSnoopVlanEntry, igmpOutTotal=igmpOutTotal, igmpInterfaceTable=igmpInterfaceTable)
