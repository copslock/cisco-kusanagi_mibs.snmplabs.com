#
# PySNMP MIB module CBS-VAPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CBS-VAPGROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
cbsHwModuleID, ModuleState = mibBuilder.importSymbols("CBS-HARDWARE-MIB", "cbsHwModuleID", "ModuleState")
cbsTraps, cbsMIBs, cbsMgmt = mibBuilder.importSymbols("CROSSBEAM-SYSTEMS-MIB", "cbsTraps", "cbsMIBs", "cbsMgmt")
ProductID, KBytes = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "ProductID", "KBytes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, IpAddress, NotificationType, ModuleIdentity, TimeTicks, ObjectIdentity, Gauge32, Integer32, Unsigned32, Counter64, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "IpAddress", "NotificationType", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Gauge32", "Integer32", "Unsigned32", "Counter64", "Bits", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
cbsVapGroupsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6848, 3, 4))
cbsVapGroupsMIB.setRevisions(('2008-09-02 00:00', '2009-12-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cbsVapGroupsMIB.setRevisionsDescriptions(('Obsoleted cbsVgRemoteBoxBackup since vapGroupTable on the device changed.', 'Add cbsVgIpv6Forward.',))
if mibBuilder.loadTexts: cbsVapGroupsMIB.setLastUpdated('200912080000Z')
if mibBuilder.loadTexts: cbsVapGroupsMIB.setOrganization('Crossbeam Systems, Inc.')
if mibBuilder.loadTexts: cbsVapGroupsMIB.setContactInfo('Email: mib-admin@crossbeamsys.com Postal: 80 Central Street Boxborough MA 01719')
if mibBuilder.loadTexts: cbsVapGroupsMIB.setDescription('XOS, Release 9.5: This MIB module defines the objects related to VAPs and VAP groups.')
cbsVapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 2, 4))
cbsVapGroupsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 4, 3))
cbsVapGroupTable = MibTable((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1), )
if mibBuilder.loadTexts: cbsVapGroupTable.setStatus('current')
if mibBuilder.loadTexts: cbsVapGroupTable.setDescription('This table contains information about the VAP groups.')
cbsVapGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1), ).setIndexNames((0, "CBS-VAPGROUP-MIB", "cbsVgVapGroupID"))
if mibBuilder.loadTexts: cbsVapGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cbsVapGroupEntry.setDescription('An entry in the VAP group table.')
cbsVgVapGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgVapGroupID.setStatus('current')
if mibBuilder.loadTexts: cbsVgVapGroupID.setDescription('The unique Group ID for the VAP group.')
cbsVgVapGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgVapGroupName.setStatus('current')
if mibBuilder.loadTexts: cbsVgVapGroupName.setDescription('The VAP group name')
cbsVgLoadPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgLoadPriority.setStatus('current')
if mibBuilder.loadTexts: cbsVgLoadPriority.setDescription('Defines relative priority while loading VAPs to hardware modules.')
cbsVgPreempPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgPreempPriority.setStatus('current')
if mibBuilder.loadTexts: cbsVgPreempPriority.setDescription('If this VAP group requires additional APMs to load its VAPs, this priority is used to determine if APMs can be taken from another group. If the preemption priority for this group is higher than the load priority for a currently running VAP, that VAP is thrown out and this VAP is loaded instead. A zero value sets the lowest priority level.')
cbsVgApmList = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgApmList.setStatus('current')
if mibBuilder.loadTexts: cbsVgApmList.setDescription('The APMs that are potentially assigned to support this VAP group.')
cbsVgVapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgVapCount.setStatus('current')
if mibBuilder.loadTexts: cbsVgVapCount.setDescription('The number of VAPs to load in this group.')
cbsVgMaxLoadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgMaxLoadCount.setStatus('current')
if mibBuilder.loadTexts: cbsVgMaxLoadCount.setDescription('The maximum number of VAPs in this group.')
cbsVgLBList = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgLBList.setStatus('current')
if mibBuilder.loadTexts: cbsVgLBList.setDescription('The list of VAPs to be load balanced.')
cbsVgBackUpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("pair", 1), ("group", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgBackUpMode.setStatus('current')
if mibBuilder.loadTexts: cbsVgBackUpMode.setDescription('Specifies how to perform a backup in case an APM fails. None - no backup Pair - VAPs are paired to provide backup functionality Group - all VAPs in the group back up each other.')
cbsVgIpForward = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgIpForward.setStatus('current')
if mibBuilder.loadTexts: cbsVgIpForward.setDescription('Specifies if IP forwarding is enabled or not.')
cbsVgRpFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgRpFilter.setStatus('current')
if mibBuilder.loadTexts: cbsVgRpFilter.setDescription('Specifies if RP filter is enabled or not.')
cbsVgLogMartians = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgLogMartians.setStatus('current')
if mibBuilder.loadTexts: cbsVgLogMartians.setDescription('Specifies if log martians is enabled or not.')
cbsVgReloadTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgReloadTimer.setStatus('current')
if mibBuilder.loadTexts: cbsVgReloadTimer.setDescription('Specifies the timeout for reloading this VAP group.')
cbsVgRemoteBoxBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgRemoteBoxBackup.setStatus('obsolete')
if mibBuilder.loadTexts: cbsVgRemoteBoxBackup.setDescription('Specifies if failover of this VAP group to a remote system is enabled or not.')
cbsVgDelayFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgDelayFlow.setStatus('current')
if mibBuilder.loadTexts: cbsVgDelayFlow.setDescription('Specifies the delay time, in seconds, after the VAP has come up before starting to load balance traffic to this VAP.')
cbsVgIpv6Forward = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVgIpv6Forward.setStatus('current')
if mibBuilder.loadTexts: cbsVgIpv6Forward.setDescription('Specifies if IPv6 forwarding is enabled or not.')
cbsVapMappingTable = MibTable((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2), )
if mibBuilder.loadTexts: cbsVapMappingTable.setStatus('current')
if mibBuilder.loadTexts: cbsVapMappingTable.setDescription('This table contains information about how the individual VAPs are mapped to hardware modules.')
cbsVapMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1), ).setIndexNames((0, "CBS-VAPGROUP-MIB", "cbsVmVapGroupID"), (0, "CBS-VAPGROUP-MIB", "cbsVmVapIndex"))
if mibBuilder.loadTexts: cbsVapMappingEntry.setStatus('current')
if mibBuilder.loadTexts: cbsVapMappingEntry.setDescription('An entry in the vap mapping table.')
cbsVmVapGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVmVapGroupID.setStatus('current')
if mibBuilder.loadTexts: cbsVmVapGroupID.setDescription('The VAP group ID.')
cbsVmVapGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVmVapGroupName.setStatus('current')
if mibBuilder.loadTexts: cbsVmVapGroupName.setDescription('The VAP group name')
cbsVmVapName = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVmVapName.setStatus('current')
if mibBuilder.loadTexts: cbsVmVapName.setDescription('The VAP name, i.e. cbsVmVapGroupName-cbsVmVapIndex')
cbsVmVapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVmVapIndex.setStatus('current')
if mibBuilder.loadTexts: cbsVmVapIndex.setDescription('Unique index value of a specific VAP within the VAP group.')
cbsVmVapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 5), ModuleState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVmVapStatus.setStatus('current')
if mibBuilder.loadTexts: cbsVmVapStatus.setDescription('The current operational status of the VAP.')
cbsVmSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsVmSlotNumber.setStatus('current')
if mibBuilder.loadTexts: cbsVmSlotNumber.setDescription('The hardware module ID (slot number) that this VAP is currently mapped to.')
cbsVapStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 3, 1)).setObjects(("CBS-VAPGROUP-MIB", "cbsVmVapStatus"), ("CBS-VAPGROUP-MIB", "cbsVmVapName"))
if mibBuilder.loadTexts: cbsVapStatusChanged.setStatus('current')
if mibBuilder.loadTexts: cbsVapStatusChanged.setDescription('The VAP status for the given VAP changed.')
mibBuilder.exportSymbols("CBS-VAPGROUP-MIB", cbsVgLogMartians=cbsVgLogMartians, cbsVgLoadPriority=cbsVgLoadPriority, cbsVmVapGroupID=cbsVmVapGroupID, cbsVgRemoteBoxBackup=cbsVgRemoteBoxBackup, PYSNMP_MODULE_ID=cbsVapGroupsMIB, cbsVgDelayFlow=cbsVgDelayFlow, cbsVgVapGroupID=cbsVgVapGroupID, cbsVgReloadTimer=cbsVgReloadTimer, cbsVapGroupEntry=cbsVapGroupEntry, cbsVgBackUpMode=cbsVgBackUpMode, cbsVmVapIndex=cbsVmVapIndex, cbsVgIpv6Forward=cbsVgIpv6Forward, cbsVgLBList=cbsVgLBList, cbsVmVapStatus=cbsVmVapStatus, cbsVapGroupsTraps=cbsVapGroupsTraps, cbsVgRpFilter=cbsVgRpFilter, cbsVgVapCount=cbsVgVapCount, cbsVgVapGroupName=cbsVgVapGroupName, cbsVmVapName=cbsVmVapName, cbsVapGroupTable=cbsVapGroupTable, cbsVapGroups=cbsVapGroups, cbsVgMaxLoadCount=cbsVgMaxLoadCount, cbsVapMappingTable=cbsVapMappingTable, cbsVgPreempPriority=cbsVgPreempPriority, cbsVmSlotNumber=cbsVmSlotNumber, cbsVgApmList=cbsVgApmList, cbsVgIpForward=cbsVgIpForward, cbsVapGroupsMIB=cbsVapGroupsMIB, cbsVapStatusChanged=cbsVapStatusChanged, cbsVapMappingEntry=cbsVapMappingEntry, cbsVmVapGroupName=cbsVmVapGroupName)
