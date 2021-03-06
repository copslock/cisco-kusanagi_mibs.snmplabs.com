#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MODULE-AUTO-SHUTDOWN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:07:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalModelName, entPhysicalName, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalModelName", "entPhysicalName", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter32, ModuleIdentity, Bits, ObjectIdentity, Unsigned32, IpAddress, Integer32, Counter64, MibIdentifier, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter32", "ModuleIdentity", "Bits", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType")
TextualConvention, DisplayString, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "DateAndTime")
ciscoModuleAutoShutdownMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 386))
ciscoModuleAutoShutdownMIB.setRevisions(('2008-03-12 00:00', '2003-12-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setRevisionsDescriptions(('Added the TC CiscoModuleAutoShutSysAction and the groups cmasModuleSysActionGroup and cmasNotificationsGroup2.', 'Initial revision of this MIB module.',))
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setLastUpdated('200803120000Z')
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setDescription('The CISCO-MODULE-AUTO-SHUTDOWN-MIB is used to configure the module automatic shutdown feature. Modules will be reset by the system when they become faulty. The module auto shutdown feature will shutdown such faulty modules when the resets occur too often. Once the modules are shutdown by this feature, they will stay shutdown until the administrator manually brings them back up. This will prevent the system from constantly resetting the faulty modules. This MIB module also covers the system initiated action occuring on a module.')
cmasMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 0))
cmasMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1))
cmasMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2))
cmasGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1))
cmasNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2))
cmasModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3))
cmasModuleSysActionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4))
class CiscoModuleAutoShutSysAction(TextualConvention, Integer32):
    description = 'The type of system initiated action. Valid values are: other(1): none of the below. reset(2): reset the module. powerCycle(3): power cycle the module. powerDown(4): power down the module.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("reset", 2), ("powerCycle", 3), ("powerDown", 4))

cmasFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasFrequency.setStatus('current')
if mibBuilder.loadTexts: cmasFrequency.setDescription("This indicates the threshold of the number of times the system can reset a faulty module, within the period specified by 'cmasPeriod'. Once the number of these system initiated resets exceeds this threshold, the module auto shutdown feature will shut down the module.")
cmasPeriod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 2), Unsigned32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasPeriod.setStatus('current')
if mibBuilder.loadTexts: cmasPeriod.setDescription('This indicates the period of time over which the number of system initiated module resets is monitored. In order for the module to be automatically shutdown, the number of times the system must reset the module has to exceed cmasFreqency times, in a span of cmasPeriod.')
cmasMIBEnableNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasMIBEnableNotification.setStatus('current')
if mibBuilder.loadTexts: cmasMIBEnableNotification.setDescription('This object indicates whether the system produces the cmasModuleAutoShutdown notification.')
cmasModuleSysActionNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleSysActionNotifEnable.setStatus('current')
if mibBuilder.loadTexts: cmasModuleSysActionNotifEnable.setDescription('This object indicates whether the system produces the cmasModuleSysActionNotif notification.')
cmasModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1), )
if mibBuilder.loadTexts: cmasModuleTable.setStatus('current')
if mibBuilder.loadTexts: cmasModuleTable.setDescription('This table contains information regarding the module auto shutdown feature.')
cmasModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cmasModuleEntry.setStatus('current')
if mibBuilder.loadTexts: cmasModuleEntry.setDescription("This entry contains information about the module auto shutdown feature. Each entry represents whether the feature is enabled, the number of resets, the last reset reason and the last reset time. Each entry is applicable for the modules capable of this feature and are identified by 'entPhysicalIndex' with entPhysicalClass value 'module'.")
cmasModuleEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleEnable.setStatus('current')
if mibBuilder.loadTexts: cmasModuleEnable.setDescription('This object enables or disables the auto shutdown feature on a module. When the object is true(1), auto shutdown is enabled for that module. The feature will start monitoring system initiated module resets, and initiate a shutdown operation on the module if the number of resets, cmasModuleNumResets, exceeds the cmasFrequency within the previous cmasPeriod of time. When the object is false(2), auto shutdown is disabled for that module.')
cmasModuleNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleNumResets.setStatus('current')
if mibBuilder.loadTexts: cmasModuleNumResets.setDescription('This indicates the number of system initiated module resets that have occurred. This does not include user initiated module resets.')
cmasModuleLastResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetReason.setStatus('current')
if mibBuilder.loadTexts: cmasModuleLastResetReason.setDescription('This object identifies the reason for the last module reset initiated by the system. This object will contain a zero-length string if no such resets have occurred.')
cmasModuleLastResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetTime.setStatus('current')
if mibBuilder.loadTexts: cmasModuleLastResetTime.setDescription('This object corresponds to the date and time when the last system initiated module reset occurred. This object will contain 0-1-1,00:00:00:0 if no system initiated resets have occurred.')
cmasModuleSysAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 1), CiscoModuleAutoShutSysAction()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysAction.setStatus('current')
if mibBuilder.loadTexts: cmasModuleSysAction.setDescription('This object identifies the system initiated action which is applied to a module.')
cmasModuleSysActionReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysActionReason.setStatus('current')
if mibBuilder.loadTexts: cmasModuleSysActionReason.setDescription('This object identifies the reason of system initiated action which is applied to a module.')
cmasModuleAutoShutdown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"))
if mibBuilder.loadTexts: cmasModuleAutoShutdown.setStatus('current')
if mibBuilder.loadTexts: cmasModuleAutoShutdown.setDescription('This notification is generated when the module auto shutdown feature shuts down a module.')
cmasModuleSysActionNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if mibBuilder.loadTexts: cmasModuleSysActionNotif.setStatus('current')
if mibBuilder.loadTexts: cmasModuleSysActionNotif.setDescription('This notification is generated when a system initiated action occurs on a module.')
cmasMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1))
cmasMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2))
cmasMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance = cmasMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cmasMIBCompliance.setDescription('The compliance statement for the CISCO-MODULE-AUTO-SHUTDOWN-MIB')
cmasMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance2 = cmasMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: cmasMIBCompliance2.setDescription('The compliance statement for the CISCO-MODULE-AUTO-SHUTDOWN-MIB')
cmasModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasFrequency"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasPeriod"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleGroup = cmasModuleGroup.setStatus('current')
if mibBuilder.loadTexts: cmasModuleGroup.setDescription('A collection of objects which are used to configure as well as show information regarding the module auto shutdown feature.')
cmasNotificationEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasMIBEnableNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationEnableGroup = cmasNotificationEnableGroup.setStatus('current')
if mibBuilder.loadTexts: cmasNotificationEnableGroup.setDescription('A collection of objects which are used to enable notifications.')
cmasNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 3)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleAutoShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup = cmasNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: cmasNotificationsGroup.setDescription('A collection of notifications for the module auto shutdown feature.')
cmasModuleSysActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 4)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotifEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleSysActionGroup = cmasModuleSysActionGroup.setStatus('current')
if mibBuilder.loadTexts: cmasModuleSysActionGroup.setDescription('A collection of objects which are related with the notification cmasModuleSysActionNotif. They are either used to enable and disable this notification or included in this notification PDU.')
cmasNotificationsGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 5)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup2 = cmasNotificationsGroup2.setStatus('current')
if mibBuilder.loadTexts: cmasNotificationsGroup2.setDescription('A collection of notifications for the system initiated module action feature.')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-MIB", ciscoModuleAutoShutdownMIB=ciscoModuleAutoShutdownMIB, cmasMIBCompliance2=cmasMIBCompliance2, PYSNMP_MODULE_ID=ciscoModuleAutoShutdownMIB, cmasMIBObjects=cmasMIBObjects, cmasModuleSysActionNotif=cmasModuleSysActionNotif, cmasModuleNumResets=cmasModuleNumResets, cmasModuleAutoShutdown=cmasModuleAutoShutdown, cmasModuleLastResetTime=cmasModuleLastResetTime, cmasMIBEnableNotification=cmasMIBEnableNotification, cmasNotificationEnableGroup=cmasNotificationEnableGroup, cmasMIBCompliances=cmasMIBCompliances, cmasNotificationsGroup=cmasNotificationsGroup, cmasPeriod=cmasPeriod, cmasModule=cmasModule, cmasModuleLastResetReason=cmasModuleLastResetReason, CiscoModuleAutoShutSysAction=CiscoModuleAutoShutSysAction, cmasModuleSysActionObjects=cmasModuleSysActionObjects, cmasModuleEnable=cmasModuleEnable, cmasModuleSysAction=cmasModuleSysAction, cmasNotifObjects=cmasNotifObjects, cmasMIBCompliance=cmasMIBCompliance, cmasModuleSysActionGroup=cmasModuleSysActionGroup, cmasMIBGroups=cmasMIBGroups, cmasGlobal=cmasGlobal, cmasMIBNotifs=cmasMIBNotifs, cmasNotificationsGroup2=cmasNotificationsGroup2, cmasModuleSysActionReason=cmasModuleSysActionReason, cmasMIBConformance=cmasMIBConformance, cmasFrequency=cmasFrequency, cmasModuleGroup=cmasModuleGroup, cmasModuleTable=cmasModuleTable, cmasModuleEntry=cmasModuleEntry, cmasModuleSysActionNotifEnable=cmasModuleSysActionNotifEnable)
