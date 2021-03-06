#
# PySNMP MIB module CISCO-FCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FCC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VsanIndex, FcAddressId = mibBuilder.importSymbols("CISCO-ST-TC", "VsanIndex", "FcAddressId")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Gauge32, MibIdentifier, iso, NotificationType, IpAddress, Integer32, Counter32, ModuleIdentity, Counter64, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Gauge32", "MibIdentifier", "iso", "NotificationType", "IpAddress", "Integer32", "Counter32", "ModuleIdentity", "Counter64", "Bits", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "TimeStamp")
ciscoFCCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 365))
ciscoFCCMIB.setRevisions(('2004-07-08 00:00', '2004-02-25 00:00', '2003-08-06 00:00', '2003-05-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFCCMIB.setRevisionsDescriptions(("Added the following objects to the 'cFCCPortTable' : - 'cFCCLastCongestionStartTime' and - 'cFCCIsRateLimitingApplied'.", "Changed the cFCCNotificationEnable DEFVAL to 'false' instead of 1.", 'Changed cFCCCongestionSourceID and cFCCCongestionDestinationID to be FC_IDs instead of WWNs and added cFCCCongestionNotifyVSANIndex', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoFCCMIB.setLastUpdated('200407080000Z')
if mibBuilder.loadTexts: ciscoFCCMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFCCMIB.setContactInfo(' Cisco Systems Customer Service Postal 170 W Tasman Drive San Jose, CA 95134 USA Tel +1 800 553-NETS E-mail cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoFCCMIB.setDescription('The MIB module for the management of Fibre Channel Congestion Control(FCC). FCC is a Cisco proprietary flow control mechanism that alleviates congestion on Fibre Channel networks. This MIB enables managers to configure the FCC mechanism on the switch, provides statistics of the congestion control packets, notification of congestion state changes of the FC port and monitoring of the congestion state of the FC port.')
ciscoFCCMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 0))
ciscoFCCMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1))
ciscoFCCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 2))
cFCCConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1))
cFCCPortEntries = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2))
cFCCNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3))
class CiscoFCCCongestionState(TextualConvention, Integer32):
    description = 'The FCC Congestion state. This is to indicate the severity of the Congestion noCongestion(1) - No Congestion Congested(2) - Congested SeverelyCongested(3) - Severely Congested.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCongestion", 1), ("congested", 2), ("severelyCongested", 3))

cFCCEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cFCCEnable.setStatus('current')
if mibBuilder.loadTexts: cFCCEnable.setDescription('To enable/disable FCC on the device.')
cFCCPacketPriority = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cFCCPacketPriority.setStatus('current')
if mibBuilder.loadTexts: cFCCPacketPriority.setDescription('The traffic Priority for the FCC packets. The generated FCC quench packets should be granted high, but not highest priority, so that the FCC packet priority is higher than the normal data traffic priority but lower than control and critical traffic priority. This ensures that the packets of the protocols guaranteeing the proper behavior of the fabric are not disturbed by quench packets. 0 is the lowest priority and 7 is the highest.')
cFCCNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cFCCNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: cFCCNotificationEnable.setDescription("This object specifies whether the agent should generate the notifications defined in this MIB module. If the value of this object is 'true', then the notifications are generated. If the value of this object is 'false', then the notifications are not generated.")
cFCCPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1), )
if mibBuilder.loadTexts: cFCCPortTable.setStatus('current')
if mibBuilder.loadTexts: cFCCPortTable.setDescription('A table providing statistics and status for FCC on a per FC Port basis.')
cFCCPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cFCCPortEntry.setStatus('current')
if mibBuilder.loadTexts: cFCCPortEntry.setDescription('Each entry contains the FCC statistics and status for a particular FC port identified by the value of ifIndex.')
cFCCEdgeQuenchPktsRecd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCEdgeQuenchPktsRecd.setStatus('current')
if mibBuilder.loadTexts: cFCCEdgeQuenchPktsRecd.setDescription('The number of Edge Quench packets received and processed on this Port.')
cFCCEdgeQuenchPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCEdgeQuenchPktsSent.setStatus('current')
if mibBuilder.loadTexts: cFCCEdgeQuenchPktsSent.setDescription('The number of Edge Quench packets generated on this Port as result of congestion.')
cFCCPathQuenchPktsRecd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCPathQuenchPktsRecd.setStatus('current')
if mibBuilder.loadTexts: cFCCPathQuenchPktsRecd.setDescription('The number of Path Quench packets recieved and processed on this Port.')
cFCCPathQuenchPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCPathQuenchPktsSent.setStatus('current')
if mibBuilder.loadTexts: cFCCPathQuenchPktsSent.setDescription('The number of Path Quench packets generated on this Port as result of congestion.')
cFCCCurrentCongestionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 5), CiscoFCCCongestionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCCurrentCongestionState.setStatus('current')
if mibBuilder.loadTexts: cFCCCurrentCongestionState.setDescription('The current FCC congestion state of this Port indicating the severity of the congestion.')
cFCCLastCongestedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCLastCongestedTime.setStatus('current')
if mibBuilder.loadTexts: cFCCLastCongestedTime.setDescription('The value of sysUpTime at the most recent time the congestion state of the Port changed to noCongestion(1) from some other value. 0 if the congestion state of the Port has never transitioned to noCongestion(1) since the last restart of the device.')
cFCCLastCongestionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCLastCongestionStartTime.setStatus('current')
if mibBuilder.loadTexts: cFCCLastCongestionStartTime.setDescription("The value of sysUpTime at the most recent time the congestion state (value of corresponding instance of 'cFCCCurrentCongestionState') of the Port changed from 'noCongestion' to some other value. 0 if the congestion state of the Port has never transitioned from 'noCongestion' to some other value since the last restart of the device.")
cFCCIsRateLimitingApplied = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCIsRateLimitingApplied.setStatus('current')
if mibBuilder.loadTexts: cFCCIsRateLimitingApplied.setDescription("The value of this object indicates if the rate limiting is currently being applied on this Port. If the value of this object is 'true', the rate limiting is currently being applied on this Port. If the value of this object is 'false', the rate limiting is not being applied currently on this Port.")
cFCCCongestionSourceID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 1), FcAddressId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionSourceID.setStatus('current')
if mibBuilder.loadTexts: cFCCCongestionSourceID.setDescription('The FC_ID associated with the Source causing the congestion. The value is extracted from the FCC congestion quench packet.')
cFCCCongestionDestinationID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 2), FcAddressId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionDestinationID.setStatus('current')
if mibBuilder.loadTexts: cFCCCongestionDestinationID.setDescription('The FC_ID associated with the Destination that is part of Source-Destination Flow causing the congestion. The value is extracted from the FCC congestion quench packet.')
cFCCCongestionNotifyVSANIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 3), VsanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionNotifyVSANIndex.setStatus('current')
if mibBuilder.loadTexts: cFCCCongestionNotifyVSANIndex.setDescription('Id of the VSAN containing the Source-Destination flow causing the congestion. The value is extracted from the FCC congestion quench packet. This along with cFCCCongestionSourceID and cFCCCongestionDestinationID gives the Flow causing the congestion.')
cFCCCongestionState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 4), CiscoFCCCongestionState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionState.setStatus('current')
if mibBuilder.loadTexts: cFCCCongestionState.setDescription('This is to indicate the congestion state of the port.')
ciscoFCCCongestionStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-FCC-MIB", "cFCCCongestionState"))
if mibBuilder.loadTexts: ciscoFCCCongestionStateChange.setStatus('current')
if mibBuilder.loadTexts: ciscoFCCCongestionStateChange.setDescription('Notification to indicate that the congestion state of this port has changed. cFCCCongestionState indicates the new state of the port.')
ciscoFCCCongestionRateLimitStart = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-FCC-MIB", "cFCCCongestionSourceID"), ("CISCO-FCC-MIB", "cFCCCongestionDestinationID"), ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"))
if mibBuilder.loadTexts: ciscoFCCCongestionRateLimitStart.setStatus('current')
if mibBuilder.loadTexts: ciscoFCCCongestionRateLimitStart.setDescription('Notification to indicate that the rate limiting has begun on this port for a source-destination pair.')
ciscoFCCCongestionRateLimitEnd = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-FCC-MIB", "cFCCCongestionSourceID"), ("CISCO-FCC-MIB", "cFCCCongestionDestinationID"), ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"))
if mibBuilder.loadTexts: ciscoFCCCongestionRateLimitEnd.setStatus('current')
if mibBuilder.loadTexts: ciscoFCCCongestionRateLimitEnd.setDescription('Notification to indicate that the rate limiting has been stopped on this port for a source-destination pair.')
ciscoFCCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1))
ciscoFCCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2))
ciscoFCCMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1, 1)).setObjects(("CISCO-FCC-MIB", "cFCCConfigurationGroup"), ("CISCO-FCC-MIB", "cFCCPortEntriesGroup"), ("CISCO-FCC-MIB", "cFCCNotificationObjectsGroup"), ("CISCO-FCC-MIB", "cFCCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFCCMIBCompliance = ciscoFCCMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoFCCMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-FCC-MIB.')
ciscoFCCMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1, 2)).setObjects(("CISCO-FCC-MIB", "cFCCConfigurationGroup"), ("CISCO-FCC-MIB", "cFCCPortEntriesGroupRev1"), ("CISCO-FCC-MIB", "cFCCNotificationObjectsGroup"), ("CISCO-FCC-MIB", "cFCCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFCCMIBComplianceRev1 = ciscoFCCMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoFCCMIBComplianceRev1.setDescription('The compliance statement for entities which implement the CISCO-FCC-MIB.')
cFCCConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 1)).setObjects(("CISCO-FCC-MIB", "cFCCEnable"), ("CISCO-FCC-MIB", "cFCCPacketPriority"), ("CISCO-FCC-MIB", "cFCCNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCConfigurationGroup = cFCCConfigurationGroup.setStatus('current')
if mibBuilder.loadTexts: cFCCConfigurationGroup.setDescription('A collection of objects for FCC configuration.')
cFCCPortEntriesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 2)).setObjects(("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCCurrentCongestionState"), ("CISCO-FCC-MIB", "cFCCLastCongestedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCPortEntriesGroup = cFCCPortEntriesGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cFCCPortEntriesGroup.setDescription('A collection of objects for FCC Statistics and Status.')
cFCCNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 3)).setObjects(("CISCO-FCC-MIB", "cFCCCongestionDestinationID"), ("CISCO-FCC-MIB", "cFCCCongestionSourceID"), ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"), ("CISCO-FCC-MIB", "cFCCCongestionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCNotificationObjectsGroup = cFCCNotificationObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: cFCCNotificationObjectsGroup.setDescription('A collection of objects defined for notification only.')
cFCCNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 4)).setObjects(("CISCO-FCC-MIB", "ciscoFCCCongestionStateChange"), ("CISCO-FCC-MIB", "ciscoFCCCongestionRateLimitStart"), ("CISCO-FCC-MIB", "ciscoFCCCongestionRateLimitEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCNotificationGroup = cFCCNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cFCCNotificationGroup.setDescription('A collection of notifications for Congestion Monitoring.')
cFCCPortEntriesGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 5)).setObjects(("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCCurrentCongestionState"), ("CISCO-FCC-MIB", "cFCCLastCongestedTime"), ("CISCO-FCC-MIB", "cFCCLastCongestionStartTime"), ("CISCO-FCC-MIB", "cFCCIsRateLimitingApplied"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCPortEntriesGroupRev1 = cFCCPortEntriesGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cFCCPortEntriesGroupRev1.setDescription('A collection of objects for FCC Statistics and Status.')
mibBuilder.exportSymbols("CISCO-FCC-MIB", ciscoFCCMIB=ciscoFCCMIB, cFCCCongestionState=cFCCCongestionState, cFCCLastCongestedTime=cFCCLastCongestedTime, ciscoFCCCongestionRateLimitEnd=ciscoFCCCongestionRateLimitEnd, CiscoFCCCongestionState=CiscoFCCCongestionState, cFCCEdgeQuenchPktsSent=cFCCEdgeQuenchPktsSent, cFCCPacketPriority=cFCCPacketPriority, cFCCPathQuenchPktsRecd=cFCCPathQuenchPktsRecd, ciscoFCCCongestionStateChange=ciscoFCCCongestionStateChange, cFCCNotificationEnable=cFCCNotificationEnable, cFCCCongestionNotifyVSANIndex=cFCCCongestionNotifyVSANIndex, cFCCPortEntriesGroup=cFCCPortEntriesGroup, cFCCNotifObjects=cFCCNotifObjects, cFCCCurrentCongestionState=cFCCCurrentCongestionState, ciscoFCCMIBComplianceRev1=ciscoFCCMIBComplianceRev1, ciscoFCCMIBCompliances=ciscoFCCMIBCompliances, cFCCNotificationObjectsGroup=cFCCNotificationObjectsGroup, cFCCPortEntry=cFCCPortEntry, cFCCConfigurationGroup=cFCCConfigurationGroup, ciscoFCCMIBCompliance=ciscoFCCMIBCompliance, cFCCLastCongestionStartTime=cFCCLastCongestionStartTime, cFCCPathQuenchPktsSent=cFCCPathQuenchPktsSent, ciscoFCCMIBGroups=ciscoFCCMIBGroups, cFCCCongestionSourceID=cFCCCongestionSourceID, PYSNMP_MODULE_ID=ciscoFCCMIB, ciscoFCCMIBConformance=ciscoFCCMIBConformance, cFCCNotificationGroup=cFCCNotificationGroup, cFCCEnable=cFCCEnable, cFCCIsRateLimitingApplied=cFCCIsRateLimitingApplied, ciscoFCCMIBObjects=ciscoFCCMIBObjects, ciscoFCCCongestionRateLimitStart=ciscoFCCCongestionRateLimitStart, ciscoFCCMIBNotifs=ciscoFCCMIBNotifs, cFCCCongestionDestinationID=cFCCCongestionDestinationID, cFCCPortTable=cFCCPortTable, cFCCConfig=cFCCConfig, cFCCPortEntries=cFCCPortEntries, cFCCPortEntriesGroupRev1=cFCCPortEntriesGroupRev1, cFCCEdgeQuenchPktsRecd=cFCCEdgeQuenchPktsRecd)
