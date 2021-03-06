#
# PySNMP MIB module AVAYA-SAA-TRACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAYA-SAA-TRACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
avGatewayMibs, = mibBuilder.importSymbols("AVAYAGEN-MIB", "avGatewayMibs")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Integer32, ObjectIdentity, Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Gauge32, IpAddress, MibIdentifier, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "Unsigned32", "TimeTicks")
RowStatus, MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
avayaSaaTrackMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2))
avayaSaaTrackMib.setRevisions(('2007-01-08 16:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avayaSaaTrackMib.setRevisionsDescriptions(('Shlomi Biton - Add avstrRtrDestHostName and avstrRtrResolvedIp for rtr configuration with destination hostname. Add avstrTrackerPermanentTrackState for keeping track status after reboot. ',))
if mibBuilder.loadTexts: avayaSaaTrackMib.setLastUpdated('200701081657Z')
if mibBuilder.loadTexts: avayaSaaTrackMib.setOrganization('Avaya, Inc.')
if mibBuilder.loadTexts: avayaSaaTrackMib.setContactInfo(' Avaya Customer Services Postal: Avaya, Inc. 211 Mt Airy Rd. Basking Ridge, NJ 07920 USA Tel: +1 908 953 6000 E-mail: executiveoffic@avaya.com WWW: http://www.avaya.com')
if mibBuilder.loadTexts: avayaSaaTrackMib.setDescription('The MIB module for configuring SAA and Object Tracking functionality in Avaya converged Gateways.')
avstrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1))
avstrRtrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1))
avstrRtrTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1), )
if mibBuilder.loadTexts: avstrRtrTable.setStatus('current')
if mibBuilder.loadTexts: avstrRtrTable.setDescription("This table contains all the rtr's configured on the device.")
avstrRtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1), ).setIndexNames((0, "AVAYA-SAA-TRACK-MIB", "avstrRtrId"))
if mibBuilder.loadTexts: avstrRtrEntry.setStatus('current')
if mibBuilder.loadTexts: avstrRtrEntry.setDescription('A specific entry.')
avstrRtrId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: avstrRtrId.setStatus('current')
if mibBuilder.loadTexts: avstrRtrId.setDescription('The ID of the RTR. This is also the index component of this table.')
avstrRtrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ipIcmpEcho", 2), ("tcpConnect", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrType.setStatus('current')
if mibBuilder.loadTexts: avstrRtrType.setDescription('The type of test this rtr object maintains.')
avstrRtrDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrDestIp.setStatus('current')
if mibBuilder.loadTexts: avstrRtrDestIp.setDescription('The destination IP address of SAA probes generated by this entry.')
avstrRtrDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrDestPort.setStatus('current')
if mibBuilder.loadTexts: avstrRtrDestPort.setDescription('The destination port of SAA probes generated by this entry. This object is meaningfull only when avstrRtrType is set to tcpConnect(3).')
avstrRtrFrequencyMs = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 5), Unsigned32().clone(5000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrFrequencyMs.setStatus('current')
if mibBuilder.loadTexts: avstrRtrFrequencyMs.setDescription('The frequency, in milliseconds, between one SAA probe and the next.')
avstrRtrWaitIntervalMs = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 6), Unsigned32().clone(5000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrWaitIntervalMs.setStatus('current')
if mibBuilder.loadTexts: avstrRtrWaitIntervalMs.setDescription('The interval, in milliseconds, from the time an SAA probe is sent until the device waits for a reply for that SAA probe.')
avstrRtrFailRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 7), Unsigned32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrFailRetries.setStatus('current')
if mibBuilder.loadTexts: avstrRtrFailRetries.setDescription("When the current state of this entry is 'up', the value of this object determines the number of successive failed probes after which the state of this entry moves to 'down'.")
avstrRtrSuccessRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 8), Unsigned32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrSuccessRetries.setStatus('current')
if mibBuilder.loadTexts: avstrRtrSuccessRetries.setDescription("When the current state of this entry is 'down', the value of this object determines the number of successive successful probes after which the state of this entry moves to 'up'.")
avstrRtrProbeDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrProbeDscp.setStatus('current')
if mibBuilder.loadTexts: avstrRtrProbeDscp.setDescription('The DSCP value of SAA probes generated by this entry.')
avstrRtrProbeSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 10), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrProbeSrcIpAddr.setStatus('current')
if mibBuilder.loadTexts: avstrRtrProbeSrcIpAddr.setDescription("The source IP address of SAA probes sent by this entry. The value 0.0.0.0 means that this address shall be taken from the probe's egress interface's address.")
avstrRtrProbeNextHopIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 11), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrProbeNextHopIf.setStatus('current')
if mibBuilder.loadTexts: avstrRtrProbeNextHopIf.setDescription("This node is valid only if avstrRtrProbeNextHopIp is set to '0.0.0.0'. The interface on which SAA probes generated by this entry shall exit, bypassing normal routing. A value of '0' means the probes will undergo routing normally. NOTES: 1. In order to set this object, you must first move avstrRtrRowStatus to notInService. When finished setting this object and avstrRtrProbeNextHopMac - move it back to active. 2. When setting this object to an Ethernet type interface which does not employ DHCP client, you must also specify the next-hop MAC address by setting avstrRtrProbeNextHopMac. When a DHCP client is used, if the MAC address is not specified, the default Gateway received from the DHCP server shall be used as the next hop.")
avstrRtrProbeNextHopMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 12), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrProbeNextHopMac.setStatus('current')
if mibBuilder.loadTexts: avstrRtrProbeNextHopMac.setDescription('Use this object in conjunction with avstrRtrProbeNextHopIf to manually set the next-hop of SAA probes generated by this entry. This object is meaningfull only when the value of avstrRtrProbeNextHopIf is valid and set to an Ethernet type interface. NOTE: In order to set this object, you must first move avstrRtrRowStatus to notInService. When finished setting this object and avstrRtrProbeNextHopIf - move it back to active.')
avstrRtrSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrSchedule.setStatus('current')
if mibBuilder.loadTexts: avstrRtrSchedule.setDescription('This object specifies the scheduling status of this row. inactive(1) - This entry is currently not scheduled to run. active(2) - This entry is currently running.')
avstrRtrOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrRtrOperState.setStatus('current')
if mibBuilder.loadTexts: avstrRtrOperState.setDescription("The conceptual operational state of this entry: inactive(1) - the entry is not operating yet. up(2) - the entry is up. This is also the initial state of the entry when it starts operating (i.e. moves out of the 'inactive' state). down(3) - the entry is down. NOTE: Refer to avstrRtrFailRetries and avstrRtrSuccessRetries to understand how the entry transitions between 'up' and 'down' states.")
avstrRtrOperStateLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrRtrOperStateLastChange.setStatus('current')
if mibBuilder.loadTexts: avstrRtrOperStateLastChange.setDescription('sysUpTime when the last change in avstrRtrOperState occured, in hundredths of a second.')
avstrRtrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 16), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrRowStatus.setStatus('current')
if mibBuilder.loadTexts: avstrRtrRowStatus.setDescription('This object indicates the conceptual status of this row. The value of this object has no effect on whether other objects in this conceptual row can be modified. If active, this object must remain active if it is referenced by a row in another table. Use createAndWait (not createAndGo) to create this row. In order for this row to be active(1) avstrRtrType and (avstrRtrDestIp or avstrRtrDestHostName) must be set to a valid value.')
avstrRtrProbeNextHopIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 17), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrProbeNextHopIp.setStatus('current')
if mibBuilder.loadTexts: avstrRtrProbeNextHopIp.setDescription("The IP address of the next-hop to which SAA probes generated by this entry shall be routed, bypassing normal routing. A value of '0.0.0.0' means that the value in avstrRtrProbeNextHopIf is valid instead. Note: Setting this node to '0.0.0.0' and avstrRtrProbeNextHopIf to '0' will result in the probes undergoing routing normally. ")
avstrRtrIfKpaliveBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrIfKpaliveBypass.setStatus('current')
if mibBuilder.loadTexts: avstrRtrIfKpaliveBypass.setDescription("This node controls whether or not SAA probes generated by this rtr will undergo normal path internally (False), in the Gateway's network stack, or will undergo a special bypass path (True) that is required when this rtr is used in conjunction with the interface keepalive feature. NOTE: This node is valid only if avstrRtrProbeNextHopIf is valid and set to a value != '0'.")
avstrRtrDestHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrRtrDestHostName.setStatus('current')
if mibBuilder.loadTexts: avstrRtrDestHostName.setDescription('The hostname shall follow RFC 1035 Host name convention. Note that while upper and lower case letters are allowed in domain names, no significance is attached to the case. That is, two names with the same spelling but different case are to be treated as if identical. The labels must start with a letter or digit, end with a letter or digit, and have as interior characters only letters, digits, and hyphen. There are also some restrictions on the length. Labels must be 63 characters or less. There are up to 4 labels per hostname. ')
avstrRtrResolvedIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 20), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrRtrResolvedIp.setStatus('current')
if mibBuilder.loadTexts: avstrRtrResolvedIp.setDescription('The Resolved destination IP address of SAA probes generated by this entry. The value 0.0.0.0 will be presented if avstrRtrDestHostName is not configured or if avstrRtrDestHostName is not resolved.')
avstrTrackerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2))
avstrTrackerTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1), )
if mibBuilder.loadTexts: avstrTrackerTable.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerTable.setDescription('This table contains all the object-trackers configured on the device.')
avstrTrackerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1), ).setIndexNames((0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerId"))
if mibBuilder.loadTexts: avstrTrackerEntry.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerEntry.setDescription('A specific entry.')
avstrTrackerId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: avstrTrackerId.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerId.setDescription('The ID of the object-tracker object. This is also the index component of this table.')
avstrTrackerDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 2), DisplayString().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerDescription.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerDescription.setDescription('Free text describing this row.')
avstrTrackerType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("list", 1), ("rtr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerType.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerType.setDescription('The type of object to be tracked by this object-tracker. The value list(1) is reserved for specifying an entry that tracks a list of object-trackers.')
avstrTrackerRtrId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerRtrId.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerRtrId.setDescription('This object has a meaning only when avstrTrackerType is set to rtr(2). The avstrRtrId of the tracked rtr.')
avstrTrackerListType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("boolAnd", 1), ("boolOr", 2), ("threshCount", 3))).clone('boolAnd')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerListType.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListType.setDescription("This object has a meaning only when avstrTrackerType is set to list(1). The value of this object determines how the states of the object-trackers in the tracked list are analyzed in order to determine the state of this object-tracker entry. Possible values are: boolAnd(1) - The entry is 'up' if all object-trackers are 'up', or 'down' if one or more object-trackers are 'down'. boolOr(2) - The entry is 'up' if at least one object-tracker in the list is 'up'. threshCount(3) - When the entry is in the 'down' state it switches to the 'up' state if the number of 'up' object-trackers is greater or equal then the number specified in avstrTrackerThresholdUp. When the entry is in the 'up' state it switches to the 'down' state if the number of 'up' objects is less then or equal to the number specified in avstrTrackerThresholdDown.")
avstrTrackerListThresholdUp = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerListThresholdUp.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListThresholdUp.setDescription("This object has a meaning only when avstrTrackerType is set to list(1), and avstrTrackerListType is set to threshXxx. When the current state of this entry is 'down', the value of this object determines the number of 'up' object-trackers in the list that will cause a transition of this entry to the 'up' state.")
avstrTrackerListThresholdDown = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerListThresholdDown.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListThresholdDown.setDescription("This object has a meaning only when avstrTrackType is set to list(1), and avstrTrackListType is set to threshXxx. When the current state of this entry is 'up', the value of this object determines the number of 'down' object-trackers in the list that will cause a transition of this entry to the 'down' state.")
avstrTrackerOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reserved", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrTrackerOperState.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerOperState.setDescription("The conceptual operational state of this entry: reserved(1) - this value is currently reserved. up(2) - the monitored object is 'up'. down(3) - the monitored object is 'down' or 'inactive'. NOTE: Refer to avstrTrackerListType, avstrTrackerThresholdUp and avstrTrackerThresholdDown to understand how the entry transitions between 'up' and 'down' states.")
avstrTrackerOperStateLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrTrackerOperStateLastChange.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerOperStateLastChange.setDescription('sysUpTime when the last change in avstrTrackerOperState occured, in hundredths of a second.')
avstrTrackerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerRowStatus.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerRowStatus.setDescription('This object indicates the conceptual status of this row. The value of this object has no effect on whether other objects in this conceptual row can be modified. If active, this object must remain active if it is referenced by a row in another table. Use createAndWait (not createAndGo) to create this row. In order for this row to be active(1) either the following must hold: o Set avstrTrackerType to list(1). o Set avstrTrackerType to rtr(2), and set avstrTrackerRtrId to an avstrRtrId of an active(1) rtr entry.')
avstrTrackerPermanentTrackState = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerPermanentTrackState.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPermanentTrackState.setDescription('Enable/Disable for storing the track state or not in permanent memory to be available after reboot. The default mode is of not keeping the track state after reboot and therefore starting as track is down.')
avstrTrackerListObjsTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2), )
if mibBuilder.loadTexts: avstrTrackerListObjsTable.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListObjsTable.setDescription('This table contains the associations between object-tracker lists and the object-tracker objects they contain.')
avstrTrackerListObjsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1), ).setIndexNames((0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsParentTrackId"), (0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsChildTrackId"))
if mibBuilder.loadTexts: avstrTrackerListObjsEntry.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListObjsEntry.setDescription('A specific entry.')
avstrTrackerListObjsParentTrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: avstrTrackerListObjsParentTrackId.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListObjsParentTrackId.setDescription('The avstrTrackerId of the object-tracker list object.')
avstrTrackerListObjsChildTrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: avstrTrackerListObjsChildTrackId.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListObjsChildTrackId.setDescription('The avstrTrackerId of the object-tracker that is part of the tracked list.')
avstrTrackerListObjsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerListObjsRowStatus.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListObjsRowStatus.setDescription('This object indicates the conceptual status of this row. The value of this object has no effect on whether other objects in this conceptual row can be modified. If active, this object must remain active if it is referenced by a row in another table. Use createAndGo (not createAndWait) to create this row.')
avstrTrackerListObjsReverseState = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avstrTrackerListObjsReverseState.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerListObjsReverseState.setDescription("This object determines whether the state of object being tracked is reversed or not. When a state is reversed 'up' is considered as 'down', and vice-versa. The default value is 'false', which means the state is not reversed.")
avstrTrackerPtrsTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3), )
if mibBuilder.loadTexts: avstrTrackerPtrsTable.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPtrsTable.setDescription('This table is an informational read-only table that contains a list of all the objects that are currently pointing to each object-tracker in the system. This table is provided for convenience only. An alternative equivalent method is to walk over all the variuos ojects in the system that may point to object-trackers.')
avstrTrackerPtrsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1), ).setIndexNames((0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsTrackId"), (0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsIndex"))
if mibBuilder.loadTexts: avstrTrackerPtrsEntry.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPtrsEntry.setDescription('A specific entry.')
avstrTrackerPtrsTrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: avstrTrackerPtrsTrackId.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPtrsTrackId.setDescription('An ID of the object-tracker, taken from avstrTrackerId.')
avstrTrackerPtrsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: avstrTrackerPtrsIndex.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPtrsIndex.setDescription('A running-index to distinguish between multiple objects pointing to the same object-tracker.')
avstrTrackerPtrsDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrTrackerPtrsDescription.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPtrsDescription.setDescription("A user-friendly string that identifies the object that points to this object-tracker. E.g. 'Interface FastEthernet 10/2'. The string is equivalent to the one displayed when issuing the 'show track detail' CLI command.")
avstrTrackerPtrsType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("trackerList", 2), ("ifIndex", 3), ("isakmpPeer", 4), ("ipStaticRoute", 5), ("ipPbrNhListEntry", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrTrackerPtrsType.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPtrsType.setDescription('This column together with the next column - avstrTrackerPtrsValue uniquely identify the object pointing to this object-tracker, in a machine-friendly manner. This column provides the semantics for interpreting the contents of the next column - avstrTrackerPtrsValue: none(1) - next column is N/A trackerList(2) - next column is taken from avstrTrackerId of the object-tracker list that points to this object-tracker. ifIndex(3) - next column is InterfaceIndex TC (IF-MIB) isakmpPeer(4) - next column is avipsIsakmpPeerIdType followed by avipsIsakmpPeerId (AVAYA-IPSEC-MIB). ipStaticRoute(5) - next column is the following OIDs in the following order: {ipCidrRouteStaticDest, ipCidrRouteStaticMask, ipCidrRouteStaticIfIndex, ipCidrRouteStaticNextHop, ipCidrRouteStaticPreference} (CROUTE-MIB). ipPbrNhListEntry(6) - next column is the following OIDs in the following order: {nextHopListIndex, nextHopIndex} (CROUTE-MIB). ')
avstrTrackerPtrsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avstrTrackerPtrsValue.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerPtrsValue.setDescription('This column together with the previous column - avstrTrackerPtrsType uniquely identify the object pointing to this object-tracker, in a machine-friendly manner. See description of avstrTrackerPtrsType for more details.')
avstrMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 2))
avstrMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 2, 0))
avstrTrackerOperStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 2, 0, 1)).setObjects(("AVAYA-SAA-TRACK-MIB", "avstrTrackerOperState"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerDescription"))
if mibBuilder.loadTexts: avstrTrackerOperStateChangeNotification.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerOperStateChangeNotification.setDescription('This notification is sent whenever a state transition for an object-tracker occurs, i.e. whenever avstrTrackerOperState changes.')
avstrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3))
avstrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1))
avstrRtrConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 1)).setObjects(("AVAYA-SAA-TRACK-MIB", "avstrRtrType"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrFrequencyMs"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrWaitIntervalMs"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrFailRetries"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrSuccessRetries"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeDscp"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeSrcIpAddr"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeNextHopIf"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeNextHopMac"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrSchedule"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrDestPort"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrIfKpaliveBypass"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeNextHopIp"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrRowStatus"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrDestIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    avstrRtrConfigGroup = avstrRtrConfigGroup.setStatus('current')
if mibBuilder.loadTexts: avstrRtrConfigGroup.setDescription('This group consists of all the SAA configuration items.')
avstrRtrMonitoringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 2)).setObjects(("AVAYA-SAA-TRACK-MIB", "avstrRtrOperState"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrOperStateLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    avstrRtrMonitoringGroup = avstrRtrMonitoringGroup.setStatus('current')
if mibBuilder.loadTexts: avstrRtrMonitoringGroup.setDescription('This group consists of all the SAA monitoring items.')
avstrTrackerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 3)).setObjects(("AVAYA-SAA-TRACK-MIB", "avstrTrackerType"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerRtrId"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListType"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerRowStatus"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsRowStatus"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsReverseState"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListThresholdUp"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerDescription"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListThresholdDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    avstrTrackerConfigGroup = avstrTrackerConfigGroup.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerConfigGroup.setDescription('This group consists of all the Object Tracking configuration items.')
avstrTrackerMonitoringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 4)).setObjects(("AVAYA-SAA-TRACK-MIB", "avstrTrackerOperState"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerOperStateLastChange"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsDescription"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsType"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    avstrTrackerMonitoringGroup = avstrTrackerMonitoringGroup.setStatus('current')
if mibBuilder.loadTexts: avstrTrackerMonitoringGroup.setDescription('This group consists of all the Object Tracking monitoring items.')
avstrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 2))
avstrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 2, 1)).setObjects(("AVAYA-SAA-TRACK-MIB", "avstrRtrConfigGroup"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerConfigGroup"), ("AVAYA-SAA-TRACK-MIB", "avstrRtrMonitoringGroup"), ("AVAYA-SAA-TRACK-MIB", "avstrTrackerMonitoringGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    avstrMIBCompliance = avstrMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: avstrMIBCompliance.setDescription('The compliance statement for SNMP entities of the SAA and Object Tracking MIB.')
mibBuilder.exportSymbols("AVAYA-SAA-TRACK-MIB", avstrTrackerConfigGroup=avstrTrackerConfigGroup, avstrMIBNotifications=avstrMIBNotifications, avstrRtrSuccessRetries=avstrRtrSuccessRetries, avstrTrackerListThresholdUp=avstrTrackerListThresholdUp, avstrTrackerMIBObjects=avstrTrackerMIBObjects, avstrTrackerPtrsTrackId=avstrTrackerPtrsTrackId, avstrTrackerListObjsTable=avstrTrackerListObjsTable, avstrTrackerPtrsValue=avstrTrackerPtrsValue, avstrRtrMonitoringGroup=avstrRtrMonitoringGroup, avstrTrackerEntry=avstrTrackerEntry, avstrTrackerOperStateLastChange=avstrTrackerOperStateLastChange, avstrTrackerPtrsIndex=avstrTrackerPtrsIndex, avstrRtrProbeDscp=avstrRtrProbeDscp, avstrRtrDestHostName=avstrRtrDestHostName, avstrRtrIfKpaliveBypass=avstrRtrIfKpaliveBypass, avstrTrackerListThresholdDown=avstrTrackerListThresholdDown, avstrMIBObjects=avstrMIBObjects, avstrRtrProbeSrcIpAddr=avstrRtrProbeSrcIpAddr, avstrRtrFailRetries=avstrRtrFailRetries, avstrTrackerDescription=avstrTrackerDescription, avstrRtrType=avstrRtrType, avstrRtrId=avstrRtrId, avstrTrackerRtrId=avstrTrackerRtrId, avstrTrackerListType=avstrTrackerListType, avstrRtrProbeNextHopIf=avstrRtrProbeNextHopIf, avstrTrackerPtrsTable=avstrTrackerPtrsTable, avstrTrackerId=avstrTrackerId, avstrTrackerPermanentTrackState=avstrTrackerPermanentTrackState, avstrTrackerTable=avstrTrackerTable, avstrRtrTable=avstrRtrTable, avstrRtrResolvedIp=avstrRtrResolvedIp, avstrRtrMIBObjects=avstrRtrMIBObjects, avstrMIBCompliances=avstrMIBCompliances, avstrRtrOperStateLastChange=avstrRtrOperStateLastChange, avstrRtrProbeNextHopMac=avstrRtrProbeNextHopMac, avstrMIBConformance=avstrMIBConformance, avstrTrackerOperState=avstrTrackerOperState, avayaSaaTrackMib=avayaSaaTrackMib, avstrTrackerListObjsParentTrackId=avstrTrackerListObjsParentTrackId, avstrRtrProbeNextHopIp=avstrRtrProbeNextHopIp, avstrTrackerPtrsType=avstrTrackerPtrsType, avstrTrackerPtrsDescription=avstrTrackerPtrsDescription, avstrRtrOperState=avstrRtrOperState, avstrMIBCompliance=avstrMIBCompliance, avstrRtrWaitIntervalMs=avstrRtrWaitIntervalMs, avstrTrackerListObjsRowStatus=avstrTrackerListObjsRowStatus, avstrRtrEntry=avstrRtrEntry, avstrTrackerType=avstrTrackerType, avstrTrackerRowStatus=avstrTrackerRowStatus, avstrRtrSchedule=avstrRtrSchedule, avstrRtrFrequencyMs=avstrRtrFrequencyMs, avstrTrackerListObjsEntry=avstrTrackerListObjsEntry, avstrTrackerListObjsChildTrackId=avstrTrackerListObjsChildTrackId, avstrMIBNotificationPrefix=avstrMIBNotificationPrefix, avstrRtrDestIp=avstrRtrDestIp, avstrRtrConfigGroup=avstrRtrConfigGroup, avstrTrackerListObjsReverseState=avstrTrackerListObjsReverseState, PYSNMP_MODULE_ID=avayaSaaTrackMib, avstrRtrDestPort=avstrRtrDestPort, avstrTrackerPtrsEntry=avstrTrackerPtrsEntry, avstrTrackerOperStateChangeNotification=avstrTrackerOperStateChangeNotification, avstrTrackerMonitoringGroup=avstrTrackerMonitoringGroup, avstrMIBGroups=avstrMIBGroups, avstrRtrRowStatus=avstrRtrRowStatus)
