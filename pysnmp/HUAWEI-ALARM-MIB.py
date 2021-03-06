#
# PySNMP MIB module HUAWEI-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ALARM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Counter64, ObjectIdentity, MibIdentifier, IpAddress, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Integer32, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Integer32", "Bits", "TimeTicks", "Gauge32")
DisplayString, TextualConvention, DateAndTime, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime", "RowStatus")
hwAlarmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180))
hwAlarmMIB.setRevisions(('2013-10-28 09:43', '2013-10-18 16:43', '2009-12-05 11:50',))
if mibBuilder.loadTexts: hwAlarmMIB.setLastUpdated('201310280943Z')
if mibBuilder.loadTexts: hwAlarmMIB.setOrganization('Huawei Technologies Co.,Ltd.')
hwAlarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1))
hwSnmpTargetAddrExtTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1), )
if mibBuilder.loadTexts: hwSnmpTargetAddrExtTable.setStatus('current')
hwSnmpTargetAddrExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"))
if mibBuilder.loadTexts: hwSnmpTargetAddrExtEntry.setStatus('current')
hwSnmpTargetAddrExtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSnmpTargetAddrExtIndex.setStatus('current')
hwSnmpTargetSlaveAddressList = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSnmpTargetSlaveAddressList.setStatus('current')
hwSnmpTargetAddrReliability = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSnmpTargetAddrReliability.setStatus('current')
hwSnmpTargetAddrAlarmReliability = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSnmpTargetAddrAlarmReliability.setStatus('current')
hwSnmpTargetAddrEventReliability = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSnmpTargetAddrEventReliability.setStatus('current')
hwSnmpTargetAddrExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSnmpTargetAddrExtRowStatus.setStatus('current')
hwMinAlarmSyncIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMinAlarmSyncIndex.setStatus('current')
hwMaxAlarmSyncIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMaxAlarmSyncIndex.setStatus('current')
hwAlarmSyncTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4), )
if mibBuilder.loadTexts: hwAlarmSyncTable.setStatus('current')
hwAlarmSyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"), (0, "HUAWEI-ALARM-MIB", "hwAlarmSyncIndex"))
if mibBuilder.loadTexts: hwAlarmSyncEntry.setStatus('current')
hwAlarmSyncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hwAlarmSyncIndex.setStatus('current')
hwAlarmSyncId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAlarmSyncId.setStatus('current')
hwAlarmSyncPara = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAlarmSyncPara.setStatus('current')
hwMinEventSyncIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMinEventSyncIndex.setStatus('current')
hwMaxEventSyncIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMaxEventSyncIndex.setStatus('current')
hwEventSyncTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7), )
if mibBuilder.loadTexts: hwEventSyncTable.setStatus('current')
hwEventSyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"), (0, "HUAWEI-ALARM-MIB", "hwEventSyncIndex"))
if mibBuilder.loadTexts: hwEventSyncEntry.setStatus('current')
hwEventSyncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hwEventSyncIndex.setStatus('current')
hwEventSyncId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEventSyncId.setStatus('current')
hwEventSyncPara = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEventSyncPara.setStatus('current')
hwAlarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8), )
if mibBuilder.loadTexts: hwAlarmActiveTable.setStatus('current')
hwAlarmActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"), (0, "HUAWEI-ALARM-MIB", "hwActiveAlarmIndex"))
if mibBuilder.loadTexts: hwAlarmActiveEntry.setStatus('current')
hwActiveAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hwActiveAlarmIndex.setStatus('current')
hwActiveAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwActiveAlarmId.setStatus('current')
hwActiveAlarmPara = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwActiveAlarmPara.setStatus('current')
hwActiveAlarmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwActiveAlarmRowStatus.setStatus('current')
hwEventTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9), )
if mibBuilder.loadTexts: hwEventTable.setStatus('current')
hwEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"), (0, "HUAWEI-ALARM-MIB", "hwEventIndex"))
if mibBuilder.loadTexts: hwEventEntry.setStatus('current')
hwEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hwEventIndex.setStatus('current')
hwEventId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEventId.setStatus('current')
hwEventPara = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEventPara.setStatus('current')
hwEventRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 9, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEventRowStatus.setStatus('current')
hwAlarmDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 18), DateAndTime())
if mibBuilder.loadTexts: hwAlarmDateAndTime.setStatus('current')
hwAlarmOrEventFlag = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarm", 1), ("event", 2))))
if mibBuilder.loadTexts: hwAlarmOrEventFlag.setStatus('current')
hwAlarmReasonInfo = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: hwAlarmReasonInfo.setStatus('current')
hwAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("indeterminate", 5), ("cleared", 6))))
if mibBuilder.loadTexts: hwAlarmSeverity.setStatus('current')
hwSnmpTargetSyncIndexTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28), )
if mibBuilder.loadTexts: hwSnmpTargetSyncIndexTable.setStatus('current')
hwSnmpTargetSyncIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"))
if mibBuilder.loadTexts: hwSnmpTargetSyncIndexEntry.setStatus('current')
hwMinAlmSyncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMinAlmSyncIndex.setStatus('current')
hwMaxAlmSyncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMaxAlmSyncIndex.setStatus('current')
hwMinEvtSyncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMinEvtSyncIndex.setStatus('current')
hwMaxEvtSyncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 28, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMaxEvtSyncIndex.setStatus('current')
hwAlarmActiveVsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 31), )
if mibBuilder.loadTexts: hwAlarmActiveVsTable.setStatus('current')
hwAlarmActiveVsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 31, 1), )
hwAlarmActiveEntry.registerAugmentions(("HUAWEI-ALARM-MIB", "hwAlarmActiveVsEntry"))
hwAlarmActiveVsEntry.setIndexNames(*hwAlarmActiveEntry.getIndexNames())
if mibBuilder.loadTexts: hwAlarmActiveVsEntry.setStatus('current')
hwAlarmActiveVsId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 31, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAlarmActiveVsId.setStatus('current')
hwEventVsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 33), )
if mibBuilder.loadTexts: hwEventVsTable.setStatus('current')
hwEventVsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 33, 1), )
hwEventEntry.registerAugmentions(("HUAWEI-ALARM-MIB", "hwEventVsEntry"))
hwEventVsEntry.setIndexNames(*hwEventEntry.getIndexNames())
if mibBuilder.loadTexts: hwEventVsEntry.setStatus('current')
hwEventVsId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 33, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEventVsId.setStatus('current')
hwAlarmSyncVsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 36), )
if mibBuilder.loadTexts: hwAlarmSyncVsTable.setStatus('current')
hwAlarmSyncVsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 36, 1), )
hwAlarmSyncEntry.registerAugmentions(("HUAWEI-ALARM-MIB", "hwAlarmSyncVsEntry"))
hwAlarmSyncVsEntry.setIndexNames(*hwAlarmSyncEntry.getIndexNames())
if mibBuilder.loadTexts: hwAlarmSyncVsEntry.setStatus('current')
hwAlarmSyncVsId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 36, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAlarmSyncVsId.setStatus('current')
hwEventSyncVsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 39), )
if mibBuilder.loadTexts: hwEventSyncVsTable.setStatus('current')
hwEventSyncVsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 39, 1), )
hwEventSyncEntry.registerAugmentions(("HUAWEI-ALARM-MIB", "hwEventSyncVsEntry"))
hwEventSyncVsEntry.setIndexNames(*hwEventSyncEntry.getIndexNames())
if mibBuilder.loadTexts: hwEventSyncVsEntry.setStatus('current')
hwEvevtSyncVsId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 1, 39, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEvevtSyncVsId.setStatus('current')
hwAlarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 2))
hwAlarmTargetHostDel = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 2, 1)).setObjects(("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"))
if mibBuilder.loadTexts: hwAlarmTargetHostDel.setStatus('current')
hwAlarmStorm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 2, 2))
if mibBuilder.loadTexts: hwAlarmStorm.setStatus('current')
hwAlarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3))
hwAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 1))
hwAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 1, 1)).setObjects(("HUAWEI-ALARM-MIB", "hwAlarmReliabilityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwAlarmCompliance = hwAlarmCompliance.setStatus('current')
hwAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2))
hwAlarmReliabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 1)).setObjects(("HUAWEI-ALARM-MIB", "hwSnmpTargetSlaveAddressList"), ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrEventReliability"), ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrAlarmReliability"), ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrReliability"), ("HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwAlarmReliabilityGroup = hwAlarmReliabilityGroup.setStatus('current')
hwActiveInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 7)).setObjects(("HUAWEI-ALARM-MIB", "hwActiveAlarmId"), ("HUAWEI-ALARM-MIB", "hwActiveAlarmPara"), ("HUAWEI-ALARM-MIB", "hwEventRowStatus"), ("HUAWEI-ALARM-MIB", "hwActiveAlarmRowStatus"), ("HUAWEI-ALARM-MIB", "hwEventId"), ("HUAWEI-ALARM-MIB", "hwEventPara"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwActiveInfoGroup = hwActiveInfoGroup.setStatus('current')
hwTrapInfoSyncGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 8)).setObjects(("HUAWEI-ALARM-MIB", "hwMinAlarmSyncIndex"), ("HUAWEI-ALARM-MIB", "hwMaxAlarmSyncIndex"), ("HUAWEI-ALARM-MIB", "hwAlarmSyncId"), ("HUAWEI-ALARM-MIB", "hwAlarmSyncPara"), ("HUAWEI-ALARM-MIB", "hwMinEventSyncIndex"), ("HUAWEI-ALARM-MIB", "hwMaxEventSyncIndex"), ("HUAWEI-ALARM-MIB", "hwEventSyncId"), ("HUAWEI-ALARM-MIB", "hwEventSyncPara"), ("HUAWEI-ALARM-MIB", "hwAlarmDateAndTime"), ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionRootCauseIndication"), ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionParentSequence"), ("HUAWEI-ALARM-MIB", "hwAlarmReasonInfo"), ("HUAWEI-ALARM-MIB", "hwAlarmSeverity"), ("HUAWEI-ALARM-MIB", "hwAlarmOrEventFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTrapInfoSyncGroup = hwTrapInfoSyncGroup.setStatus('current')
hwActiveInfoVsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 9)).setObjects(("HUAWEI-ALARM-MIB", "hwAlarmActiveVsId"), ("HUAWEI-ALARM-MIB", "hwEventVsId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwActiveInfoVsGroup = hwActiveInfoVsGroup.setStatus('current')
hwTrapSyncVsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 10)).setObjects(("HUAWEI-ALARM-MIB", "hwAlarmSyncVsId"), ("HUAWEI-ALARM-MIB", "hwEvevtSyncVsId"), ("HUAWEI-ALARM-MIB", "hwMinAlmSyncIndex"), ("HUAWEI-ALARM-MIB", "hwMaxAlmSyncIndex"), ("HUAWEI-ALARM-MIB", "hwMinEvtSyncIndex"), ("HUAWEI-ALARM-MIB", "hwMaxEvtSyncIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTrapSyncVsGroup = hwTrapSyncVsGroup.setStatus('current')
hwAlarmTrapInfoGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 11)).setObjects(("HUAWEI-ALARM-MIB", "hwAlarmTargetHostDel"), ("HUAWEI-ALARM-MIB", "hwAlarmStorm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwAlarmTrapInfoGroup = hwAlarmTrapInfoGroup.setStatus('current')
hwTrapSuppressionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 12)).setObjects(("HUAWEI-ALARM-MIB", "hwAlarmDelaySuppressionEnable"), ("HUAWEI-ALARM-MIB", "hwAlarmDelaySuppressionCausePersistPeriod"), ("HUAWEI-ALARM-MIB", "hwAlarmDelaySuppressionClearPersistPeriod"), ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionEnable"), ("HUAWEI-ALARM-MIB", "hwAlarmCorrAnalyzeSuppressionStatus"), ("HUAWEI-ALARM-MIB", "hwEventDelaySuppressionEnable"), ("HUAWEI-ALARM-MIB", "hwEventDelaySuppressionCausePersistPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTrapSuppressionGroup = hwTrapSuppressionGroup.setStatus('current')
hwTrapInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 3, 2, 13)).setObjects(("HUAWEI-ALARM-MIB", "hwAlarmAttrSeverity"), ("HUAWEI-ALARM-MIB", "hwEventAttrSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTrapInfoGroup = hwTrapInfoGroup.setStatus('current')
hwAlarmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5))
hwAlarmAttr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1))
hwAlarmAttrTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1), )
if mibBuilder.loadTexts: hwAlarmAttrTable.setStatus('current')
hwAlarmAttrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwAlarmName"))
if mibBuilder.loadTexts: hwAlarmAttrEntry.setStatus('current')
hwAlarmName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAlarmName.setStatus('current')
hwAlarmAttrSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("indeterminate", 5), ("cleared", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAlarmAttrSeverity.setStatus('current')
hwAlarmMask = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3))
hwAlarmMaskBasedOnIfnameTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1), )
if mibBuilder.loadTexts: hwAlarmMaskBasedOnIfnameTable.setStatus('current')
hwAlarmMaskBasedOnIfnameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwAlarmMaskIfName"))
if mibBuilder.loadTexts: hwAlarmMaskBasedOnIfnameEntry.setStatus('current')
hwAlarmMaskIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAlarmMaskIfName.setStatus('current')
hwAlarmMaskBasedOnIfnameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 1, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwAlarmMaskBasedOnIfnameRowStatus.setStatus('current')
hwAlarmMaskBasedOnEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2), )
if mibBuilder.loadTexts: hwAlarmMaskBasedOnEntityTable.setStatus('current')
hwAlarmMaskBasedOnEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwAlarmMaskEntPhysicalIndex"))
if mibBuilder.loadTexts: hwAlarmMaskBasedOnEntityEntry.setStatus('current')
hwAlarmMaskEntPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAlarmMaskEntPhysicalIndex.setStatus('current')
hwAlarmMaskEntPhysicalName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAlarmMaskEntPhysicalName.setStatus('current')
hwAlarmMaskBasedOnEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 3, 2, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwAlarmMaskBasedOnEntityRowStatus.setStatus('current')
hwAlarmDelay = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4))
hwAlarmDelaySuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAlarmDelaySuppressionEnable.setStatus('current')
hwAlarmDelaySuppressionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2), )
if mibBuilder.loadTexts: hwAlarmDelaySuppressionTable.setStatus('current')
hwAlarmDelaySuppressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwAlarmName"))
if mibBuilder.loadTexts: hwAlarmDelaySuppressionEntry.setStatus('current')
hwAlarmDelaySuppressionCausePersistPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAlarmDelaySuppressionCausePersistPeriod.setStatus('current')
hwAlarmDelaySuppressionClearPersistPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAlarmDelaySuppressionClearPersistPeriod.setStatus('current')
hwAlarmCorrAnalyze = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5))
hwAlarmCorrAnalyzeSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAlarmCorrAnalyzeSuppressionEnable.setStatus('current')
hwAlarmCorrAnalyzeSuppressionRootCauseIndication = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("independent", 0), ("rootcause", 1), ("nonrootcause", 2))))
if mibBuilder.loadTexts: hwAlarmCorrAnalyzeSuppressionRootCauseIndication.setStatus('current')
hwAlarmCorrAnalyzeSuppressionParentSequence = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 3), OctetString())
if mibBuilder.loadTexts: hwAlarmCorrAnalyzeSuppressionParentSequence.setStatus('current')
hwAlarmCorrAnalyzeSuppressionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 4), )
if mibBuilder.loadTexts: hwAlarmCorrAnalyzeSuppressionTable.setStatus('current')
hwAlarmCorrAnalyzeSuppressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 4, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwSnmpTargetAddrExtIndex"))
if mibBuilder.loadTexts: hwAlarmCorrAnalyzeSuppressionEntry.setStatus('current')
hwAlarmCorrAnalyzeSuppressionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 5, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAlarmCorrAnalyzeSuppressionStatus.setStatus('current')
hwEventConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6))
hwEventAttr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1))
hwEventAttrTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1), )
if mibBuilder.loadTexts: hwEventAttrTable.setStatus('current')
hwEventAttrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwEventName"))
if mibBuilder.loadTexts: hwEventAttrEntry.setStatus('current')
hwEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEventName.setStatus('current')
hwEventAttrSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("indeterminate", 5), ("cleared", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEventAttrSeverity.setStatus('current')
hwEventDelay = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4))
hwEventDelaySuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwEventDelaySuppressionEnable.setStatus('current')
hwEventDelaySuppressionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 2), )
if mibBuilder.loadTexts: hwEventDelaySuppressionTable.setStatus('current')
hwEventDelaySuppressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 2, 1), ).setIndexNames((0, "HUAWEI-ALARM-MIB", "hwEventName"))
if mibBuilder.loadTexts: hwEventDelaySuppressionEntry.setStatus('current')
hwEventDelaySuppressionCausePersistPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 180, 6, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwEventDelaySuppressionCausePersistPeriod.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-ALARM-MIB", hwAlarmStorm=hwAlarmStorm, hwAlarmDelay=hwAlarmDelay, hwAlarmMaskEntPhysicalName=hwAlarmMaskEntPhysicalName, hwSnmpTargetSyncIndexTable=hwSnmpTargetSyncIndexTable, hwEventVsTable=hwEventVsTable, hwAlarmCorrAnalyzeSuppressionStatus=hwAlarmCorrAnalyzeSuppressionStatus, hwEventTable=hwEventTable, hwEventAttrTable=hwEventAttrTable, hwAlarmCorrAnalyze=hwAlarmCorrAnalyze, hwTrapSyncVsGroup=hwTrapSyncVsGroup, hwAlarmObjects=hwAlarmObjects, hwEventDelaySuppressionEnable=hwEventDelaySuppressionEnable, hwAlarmReasonInfo=hwAlarmReasonInfo, hwAlarmMaskIfName=hwAlarmMaskIfName, hwAlarmSyncTable=hwAlarmSyncTable, hwSnmpTargetSyncIndexEntry=hwSnmpTargetSyncIndexEntry, hwAlarmReliabilityGroup=hwAlarmReliabilityGroup, hwEventName=hwEventName, hwSnmpTargetAddrAlarmReliability=hwSnmpTargetAddrAlarmReliability, hwAlarmCorrAnalyzeSuppressionParentSequence=hwAlarmCorrAnalyzeSuppressionParentSequence, hwEventAttrSeverity=hwEventAttrSeverity, hwEventAttr=hwEventAttr, hwAlarmMaskBasedOnIfnameTable=hwAlarmMaskBasedOnIfnameTable, hwEvevtSyncVsId=hwEvevtSyncVsId, hwAlarmCorrAnalyzeSuppressionRootCauseIndication=hwAlarmCorrAnalyzeSuppressionRootCauseIndication, hwAlarmSyncEntry=hwAlarmSyncEntry, hwSnmpTargetAddrExtEntry=hwSnmpTargetAddrExtEntry, hwTrapInfoGroup=hwTrapInfoGroup, hwEventConfig=hwEventConfig, hwEventDelaySuppressionEntry=hwEventDelaySuppressionEntry, hwAlarmGroups=hwAlarmGroups, hwAlarmMask=hwAlarmMask, hwSnmpTargetAddrExtIndex=hwSnmpTargetAddrExtIndex, hwEventPara=hwEventPara, hwAlarmMIB=hwAlarmMIB, hwTrapSuppressionGroup=hwTrapSuppressionGroup, hwEventIndex=hwEventIndex, hwAlarmTargetHostDel=hwAlarmTargetHostDel, hwMinAlarmSyncIndex=hwMinAlarmSyncIndex, hwAlarmMaskBasedOnIfnameRowStatus=hwAlarmMaskBasedOnIfnameRowStatus, hwAlarmMaskBasedOnEntityEntry=hwAlarmMaskBasedOnEntityEntry, hwActiveInfoVsGroup=hwActiveInfoVsGroup, hwEventDelaySuppressionCausePersistPeriod=hwEventDelaySuppressionCausePersistPeriod, hwEventSyncEntry=hwEventSyncEntry, hwEventSyncId=hwEventSyncId, hwAlarmSyncId=hwAlarmSyncId, hwAlarmMaskBasedOnEntityRowStatus=hwAlarmMaskBasedOnEntityRowStatus, hwAlarmActiveEntry=hwAlarmActiveEntry, hwAlarmActiveVsEntry=hwAlarmActiveVsEntry, hwEventSyncVsTable=hwEventSyncVsTable, hwAlarmNotifications=hwAlarmNotifications, hwMinEventSyncIndex=hwMinEventSyncIndex, hwAlarmCorrAnalyzeSuppressionEntry=hwAlarmCorrAnalyzeSuppressionEntry, hwEventSyncTable=hwEventSyncTable, hwEventSyncIndex=hwEventSyncIndex, hwEventVsEntry=hwEventVsEntry, hwAlarmTrapInfoGroup=hwAlarmTrapInfoGroup, hwEventEntry=hwEventEntry, hwAlarmActiveVsTable=hwAlarmActiveVsTable, hwAlarmDelaySuppressionEnable=hwAlarmDelaySuppressionEnable, hwEventDelaySuppressionTable=hwEventDelaySuppressionTable, hwEventId=hwEventId, hwAlarmActiveVsId=hwAlarmActiveVsId, hwMinAlmSyncIndex=hwMinAlmSyncIndex, hwEventRowStatus=hwEventRowStatus, hwAlarmSyncVsId=hwAlarmSyncVsId, hwActiveAlarmId=hwActiveAlarmId, hwAlarmMaskBasedOnIfnameEntry=hwAlarmMaskBasedOnIfnameEntry, hwMaxEvtSyncIndex=hwMaxEvtSyncIndex, hwSnmpTargetAddrReliability=hwSnmpTargetAddrReliability, hwSnmpTargetAddrExtRowStatus=hwSnmpTargetAddrExtRowStatus, hwAlarmSeverity=hwAlarmSeverity, hwSnmpTargetAddrEventReliability=hwSnmpTargetAddrEventReliability, hwAlarmAttrTable=hwAlarmAttrTable, hwAlarmCompliance=hwAlarmCompliance, hwAlarmDateAndTime=hwAlarmDateAndTime, hwMinEvtSyncIndex=hwMinEvtSyncIndex, hwAlarmSyncPara=hwAlarmSyncPara, hwAlarmMaskEntPhysicalIndex=hwAlarmMaskEntPhysicalIndex, hwAlarmCorrAnalyzeSuppressionEnable=hwAlarmCorrAnalyzeSuppressionEnable, hwAlarmAttrSeverity=hwAlarmAttrSeverity, hwAlarmAttrEntry=hwAlarmAttrEntry, PYSNMP_MODULE_ID=hwAlarmMIB, hwAlarmSyncVsTable=hwAlarmSyncVsTable, hwAlarmName=hwAlarmName, hwMaxEventSyncIndex=hwMaxEventSyncIndex, hwAlarmCorrAnalyzeSuppressionTable=hwAlarmCorrAnalyzeSuppressionTable, hwAlarmSyncVsEntry=hwAlarmSyncVsEntry, hwSnmpTargetSlaveAddressList=hwSnmpTargetSlaveAddressList, hwEventAttrEntry=hwEventAttrEntry, hwMaxAlarmSyncIndex=hwMaxAlarmSyncIndex, hwAlarmActiveTable=hwAlarmActiveTable, hwAlarmConfig=hwAlarmConfig, hwAlarmDelaySuppressionEntry=hwAlarmDelaySuppressionEntry, hwActiveAlarmPara=hwActiveAlarmPara, hwEventSyncPara=hwEventSyncPara, hwAlarmDelaySuppressionTable=hwAlarmDelaySuppressionTable, hwAlarmDelaySuppressionClearPersistPeriod=hwAlarmDelaySuppressionClearPersistPeriod, hwActiveAlarmIndex=hwActiveAlarmIndex, hwSnmpTargetAddrExtTable=hwSnmpTargetAddrExtTable, hwAlarmMaskBasedOnEntityTable=hwAlarmMaskBasedOnEntityTable, hwAlarmSyncIndex=hwAlarmSyncIndex, hwAlarmOrEventFlag=hwAlarmOrEventFlag, hwAlarmAttr=hwAlarmAttr, hwEventVsId=hwEventVsId, hwEventSyncVsEntry=hwEventSyncVsEntry, hwAlarmConformance=hwAlarmConformance, hwActiveAlarmRowStatus=hwActiveAlarmRowStatus, hwActiveInfoGroup=hwActiveInfoGroup, hwEventDelay=hwEventDelay, hwAlarmDelaySuppressionCausePersistPeriod=hwAlarmDelaySuppressionCausePersistPeriod, hwTrapInfoSyncGroup=hwTrapInfoSyncGroup, hwMaxAlmSyncIndex=hwMaxAlmSyncIndex, hwAlarmCompliances=hwAlarmCompliances)
