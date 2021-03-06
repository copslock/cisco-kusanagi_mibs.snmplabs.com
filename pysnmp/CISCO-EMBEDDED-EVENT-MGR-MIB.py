#
# PySNMP MIB module CISCO-EMBEDDED-EVENT-MGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-EMBEDDED-EVENT-MGR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Counter64, Unsigned32, Counter32, ModuleIdentity, Bits, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, TimeTicks, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Unsigned32", "Counter32", "ModuleIdentity", "Bits", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier")
TruthValue, TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "DateAndTime")
cEventMgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 134))
cEventMgrMIB.setRevisions(('2006-11-07 00:00', '2003-04-16 00:00',))
if mibBuilder.loadTexts: cEventMgrMIB.setLastUpdated('200611070000Z')
if mibBuilder.loadTexts: cEventMgrMIB.setOrganization('Cisco Systems, Inc.')
cEventMgrMIBNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 0))
cEventMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 1))
cEventMgrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 3))
ceemEventMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1))
ceemHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2))
ceemRegisteredPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3))
class NotifySource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("server", 1), ("policy", 2))

ceemEventMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1), )
if mibBuilder.loadTexts: ceemEventMapTable.setStatus('current')
ceemEventMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemEventIndex"))
if mibBuilder.loadTexts: ceemEventMapEntry.setStatus('current')
ceemEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ceemEventIndex.setStatus('current')
ceemEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemEventName.setStatus('current')
ceemEventDescrText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemEventDescrText.setStatus('current')
ceemHistoryMaxEventEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceemHistoryMaxEventEntries.setStatus('current')
ceemHistoryLastEventEntry = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryLastEventEntry.setStatus('current')
ceemHistoryEventTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3), )
if mibBuilder.loadTexts: ceemHistoryEventTable.setStatus('current')
ceemHistoryEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventIndex"))
if mibBuilder.loadTexts: ceemHistoryEventEntry.setStatus('current')
ceemHistoryEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ceemHistoryEventIndex.setStatus('current')
ceemHistoryEventType1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType1.setStatus('current')
ceemHistoryEventType2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType2.setStatus('current')
ceemHistoryEventType3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType3.setStatus('current')
ceemHistoryEventType4 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType4.setStatus('current')
ceemHistoryPolicyPath = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryPolicyPath.setStatus('current')
ceemHistoryPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryPolicyName.setStatus('current')
ceemHistoryPolicyExitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryPolicyExitStatus.setStatus('current')
ceemHistoryPolicyIntData1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryPolicyIntData1.setStatus('current')
ceemHistoryPolicyIntData2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryPolicyIntData2.setStatus('current')
ceemHistoryPolicyStrData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryPolicyStrData.setStatus('current')
ceemHistoryNotifyType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 12), NotifySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryNotifyType.setStatus('current')
ceemHistoryEventType5 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType5.setStatus('current')
ceemHistoryEventType6 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType6.setStatus('current')
ceemHistoryEventType7 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType7.setStatus('current')
ceemHistoryEventType8 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 2, 3, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemHistoryEventType8.setStatus('current')
ceemRegisteredPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1), )
if mibBuilder.loadTexts: ceemRegisteredPolicyTable.setStatus('current')
ceemRegisteredPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyIndex"))
if mibBuilder.loadTexts: ceemRegisteredPolicyEntry.setStatus('current')
ceemRegisteredPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ceemRegisteredPolicyIndex.setStatus('current')
ceemRegisteredPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyName.setStatus('current')
ceemRegisteredPolicyEventType1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType1.setStatus('current')
ceemRegisteredPolicyEventType2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType2.setStatus('current')
ceemRegisteredPolicyEventType3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType3.setStatus('current')
ceemRegisteredPolicyEventType4 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType4.setStatus('current')
ceemRegisteredPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyStatus.setStatus('current')
ceemRegisteredPolicyType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("user", 1), ("system", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyType.setStatus('current')
ceemRegisteredPolicyNotifFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyNotifFlag.setStatus('current')
ceemRegisteredPolicyRegTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyRegTime.setStatus('current')
ceemRegisteredPolicyEnabledTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEnabledTime.setStatus('current')
ceemRegisteredPolicyRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyRunTime.setStatus('current')
ceemRegisteredPolicyRunCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyRunCount.setStatus('current')
ceemRegisteredPolicyEventType5 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType5.setStatus('current')
ceemRegisteredPolicyEventType6 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType6.setStatus('current')
ceemRegisteredPolicyEventType7 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType7.setStatus('current')
ceemRegisteredPolicyEventType8 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 134, 1, 3, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceemRegisteredPolicyEventType8.setStatus('current')
cEventMgrServerEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 134, 0, 1)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType1"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType2"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType3"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType4"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyPath"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyName"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyExitStatus"))
if mibBuilder.loadTexts: cEventMgrServerEvent.setStatus('current')
cEventMgrPolicyEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 134, 0, 2)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType1"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType2"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType3"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType4"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyPath"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyName"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData1"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData2"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyStrData"))
if mibBuilder.loadTexts: cEventMgrPolicyEvent.setStatus('current')
cEventMgrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 1))
cEventMgrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2))
cEventMgrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 1, 1)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrDescrGroup"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrNotificationsGroup"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrRegisteredPolicyGroup"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrCompliance = cEventMgrCompliance.setStatus('deprecated')
cEventMgrComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 1, 2)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrDescrGroup"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrNotificationsGroup"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrRegisteredPolicyGroup"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrRegisteredPolicyGroupSup1"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrHistoryGroup"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrHistoryGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrComplianceRev1 = cEventMgrComplianceRev1.setStatus('current')
cEventMgrDescrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 1)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemEventName"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemEventDescrText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrDescrGroup = cEventMgrDescrGroup.setStatus('current')
cEventMgrHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 2)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryMaxEventEntries"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryLastEventEntry"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType1"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType2"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType3"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType4"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyPath"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyName"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyExitStatus"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData1"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyIntData2"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryPolicyStrData"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryNotifyType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrHistoryGroup = cEventMgrHistoryGroup.setStatus('current')
cEventMgrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 3)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrServerEvent"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "cEventMgrPolicyEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrNotificationsGroup = cEventMgrNotificationsGroup.setStatus('current')
cEventMgrRegisteredPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 4)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyName"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType1"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType2"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType3"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType4"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyStatus"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyType"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyNotifFlag"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyRegTime"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEnabledTime"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyRunTime"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyRunCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrRegisteredPolicyGroup = cEventMgrRegisteredPolicyGroup.setStatus('current')
cEventMgrHistoryGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 5)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType5"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType6"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType7"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemHistoryEventType8"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrHistoryGroupSup1 = cEventMgrHistoryGroupSup1.setStatus('current')
cEventMgrRegisteredPolicyGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 134, 3, 2, 6)).setObjects(("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType5"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType6"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType7"), ("CISCO-EMBEDDED-EVENT-MGR-MIB", "ceemRegisteredPolicyEventType8"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEventMgrRegisteredPolicyGroupSup1 = cEventMgrRegisteredPolicyGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-EMBEDDED-EVENT-MGR-MIB", ceemEventDescrText=ceemEventDescrText, ceemHistoryEventType5=ceemHistoryEventType5, ceemRegisteredPolicyEventType4=ceemRegisteredPolicyEventType4, ceemEventName=ceemEventName, ceemHistoryPolicyIntData1=ceemHistoryPolicyIntData1, ceemRegisteredPolicyEntry=ceemRegisteredPolicyEntry, ceemHistoryPolicyExitStatus=ceemHistoryPolicyExitStatus, ceemRegisteredPolicyRunTime=ceemRegisteredPolicyRunTime, cEventMgrDescrGroup=cEventMgrDescrGroup, ceemHistory=ceemHistory, cEventMgrNotificationsGroup=cEventMgrNotificationsGroup, cEventMgrRegisteredPolicyGroup=cEventMgrRegisteredPolicyGroup, ceemRegisteredPolicyEventType3=ceemRegisteredPolicyEventType3, ceemRegisteredPolicyStatus=ceemRegisteredPolicyStatus, ceemEventIndex=ceemEventIndex, cEventMgrConformance=cEventMgrConformance, ceemRegisteredPolicyEventType6=ceemRegisteredPolicyEventType6, cEventMgrServerEvent=cEventMgrServerEvent, cEventMgrHistoryGroup=cEventMgrHistoryGroup, ceemHistoryPolicyStrData=ceemHistoryPolicyStrData, NotifySource=NotifySource, cEventMgrPolicyEvent=cEventMgrPolicyEvent, ceemRegisteredPolicyEventType8=ceemRegisteredPolicyEventType8, cEventMgrMIBNotif=cEventMgrMIBNotif, ceemHistoryEventType2=ceemHistoryEventType2, ceemEventMap=ceemEventMap, cEventMgrGroups=cEventMgrGroups, ceemHistoryEventType6=ceemHistoryEventType6, PYSNMP_MODULE_ID=cEventMgrMIB, ceemRegisteredPolicyRegTime=ceemRegisteredPolicyRegTime, cEventMgrRegisteredPolicyGroupSup1=cEventMgrRegisteredPolicyGroupSup1, cEventMgrMIB=cEventMgrMIB, ceemHistoryPolicyIntData2=ceemHistoryPolicyIntData2, ceemRegisteredPolicyEventType7=ceemRegisteredPolicyEventType7, ceemHistoryEventEntry=ceemHistoryEventEntry, ceemHistoryEventTable=ceemHistoryEventTable, cEventMgrMIBObjects=cEventMgrMIBObjects, ceemEventMapEntry=ceemEventMapEntry, ceemRegisteredPolicyName=ceemRegisteredPolicyName, ceemRegisteredPolicy=ceemRegisteredPolicy, ceemHistoryEventType3=ceemHistoryEventType3, ceemHistoryEventType8=ceemHistoryEventType8, ceemHistoryEventIndex=ceemHistoryEventIndex, cEventMgrCompliance=cEventMgrCompliance, ceemRegisteredPolicyNotifFlag=ceemRegisteredPolicyNotifFlag, ceemRegisteredPolicyRunCount=ceemRegisteredPolicyRunCount, ceemRegisteredPolicyEventType1=ceemRegisteredPolicyEventType1, ceemRegisteredPolicyIndex=ceemRegisteredPolicyIndex, ceemHistoryEventType1=ceemHistoryEventType1, ceemHistoryPolicyName=ceemHistoryPolicyName, ceemHistoryNotifyType=ceemHistoryNotifyType, ceemRegisteredPolicyEventType5=ceemRegisteredPolicyEventType5, ceemRegisteredPolicyType=ceemRegisteredPolicyType, ceemHistoryMaxEventEntries=ceemHistoryMaxEventEntries, ceemEventMapTable=ceemEventMapTable, ceemHistoryPolicyPath=ceemHistoryPolicyPath, cEventMgrHistoryGroupSup1=cEventMgrHistoryGroupSup1, ceemRegisteredPolicyEventType2=ceemRegisteredPolicyEventType2, ceemHistoryEventType4=ceemHistoryEventType4, ceemRegisteredPolicyTable=ceemRegisteredPolicyTable, ceemHistoryLastEventEntry=ceemHistoryLastEventEntry, cEventMgrCompliances=cEventMgrCompliances, ceemRegisteredPolicyEnabledTime=ceemRegisteredPolicyEnabledTime, ceemHistoryEventType7=ceemHistoryEventType7, cEventMgrComplianceRev1=cEventMgrComplianceRev1)
