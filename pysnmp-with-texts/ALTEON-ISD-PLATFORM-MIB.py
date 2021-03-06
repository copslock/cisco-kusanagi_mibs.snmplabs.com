#
# PySNMP MIB module ALTEON-ISD-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTEON-ISD-PLATFORM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
platform, = mibBuilder.importSymbols("ALTEON-ROOT-MIB", "platform")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Bits, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter32, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Bits", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter32", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "NotificationType")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
alteonPlatformISDModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 1))
alteonPlatformISDModule.setRevisions(('1902-05-13 00:00', '1901-02-09 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alteonPlatformISDModule.setRevisionsDescriptions(('MIB unification across the various Alteon iSD platforms.', 'The initial revision of MIB module ALTEON-ISD-PLATFORM-MIB.',))
if mibBuilder.loadTexts: alteonPlatformISDModule.setLastUpdated('0205130000Z')
if mibBuilder.loadTexts: alteonPlatformISDModule.setOrganization('Alteon Web Systems Inc.')
if mibBuilder.loadTexts: alteonPlatformISDModule.setContactInfo('Contact: Alteon Support E-mail: support@alteon.com')
if mibBuilder.loadTexts: alteonPlatformISDModule.setDescription('MIB Module for object and notification definitions for event and alarms common to Alteon iSD products.')
alteonISDPlatformMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2))
if mibBuilder.loadTexts: alteonISDPlatformMIB.setStatus('current')
if mibBuilder.loadTexts: alteonISDPlatformMIB.setDescription('Toplevel ID of Alteon Platform ISD MIB.')
isdObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1))
if mibBuilder.loadTexts: isdObjects.setStatus('current')
if mibBuilder.loadTexts: isdObjects.setDescription('Object definitions for the Alteon ISD Platform MIB.')
isdCluster = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1))
if mibBuilder.loadTexts: isdCluster.setStatus('current')
if mibBuilder.loadTexts: isdCluster.setDescription('A collection of objects to configure and monitor the iSDs in the system.')
currentAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3))
if mibBuilder.loadTexts: currentAlarm.setStatus('current')
if mibBuilder.loadTexts: currentAlarm.setDescription('A collection of objects for monitoring of active alarms in the iSD system.')
isdMonitor = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5))
if mibBuilder.loadTexts: isdMonitor.setStatus('current')
if mibBuilder.loadTexts: isdMonitor.setDescription('A collection of objects for monitoring the performance and resource utilization of the iSDs in the system.')
class AlarmSeverity(TextualConvention, Integer32):
    reference = 'X.733, ITU Alarm Reporting Function'
    description = 'The AlarmSeverity defines four severity levels, which provide an indication of how it is perceived that the capability of the managed object has been affected. Those severity levels which represent service affecting conditions ordered from most severe to least severe are critical, major, minor and warning. The levels used are a subset of the levels found in X.733, ITU Alarm Reporting Function: o The Indeterminate severity level indicates that the severity level cannot be determined. o The Critical severity level indicates that a service affecting condition has occurred and an immediate corrective action is required. Such a severity can be reported, for example, when a managed object becomes totally out of service and its capability must be restored. o The Major severity level indicates that a service affecting condition has developed and an urgent corrective action is required. Such a severity can be reported, for example, when there is a severe degradation in the capability of the managed object and its full capability must be restored. o The Warning severity level indicates the detection of a potential or impending service affecting fault, before any significant effects have been felt. Action should be taken to further diagnose (if necessary) and correct the problem in order to prevent it from becoming a more serious service affecting fault. When an alarm is cleared, an alarmCleared event is generated. This event clears the alarm with the currentAlarmFaultId contained in the event. It is not required that the clearing of previously reported alarms are reported. Therefore, a managing system cannot assume that the absence of an alarmedCleared event for a fault means that the condition that caused the generation of previous alarms is still present. Managed object definers shall state if, and under which conditions, the alarmedCleared event is used. The clear value of AlarmSeverity is an action which is used when a management station wants to clear an active alarm. This is not possible on all systems, and thus an agent does not have support write access for this value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5))
    namedValues = NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("warning", 4), ("clear", 5))

isdClusterTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1), )
if mibBuilder.loadTexts: isdClusterTable.setStatus('current')
if mibBuilder.loadTexts: isdClusterTable.setDescription('Table of iSDs in this iSD cluster.')
isdClusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "isdIndex"))
if mibBuilder.loadTexts: isdClusterEntry.setStatus('current')
if mibBuilder.loadTexts: isdClusterEntry.setDescription('')
isdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: isdIndex.setStatus('current')
if mibBuilder.loadTexts: isdIndex.setDescription('A unique index for this iSD.')
isdIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdIP.setStatus('current')
if mibBuilder.loadTexts: isdIP.setDescription('The IP address of the iSD box')
isdType = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdType.setStatus('current')
if mibBuilder.loadTexts: isdType.setDescription('Defines if a iSD is a master in the cluster, or a slave. Note that there must be at least one master in the cluster. A master iSD keeps copies of the configuration database and software on its flash disk. Slave iSDs reads this info from the masters.')
isdOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdOperStatus.setStatus('current')
if mibBuilder.loadTexts: isdOperStatus.setDescription("The current operational status of the iSD. 'swMismatch' means that the iSD is up, but the software version does not match the rest of the system. The correct software version must be installed on this iSD to make it enter the 'up' state. 'appError' means that the iSD is up, but the applicaion is not functioning, i.e. the iSD does not handle traffic correctly. Check the application specific MIBs for further diagnostics.")
isdMIPOwner = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdMIPOwner.setStatus('current')
if mibBuilder.loadTexts: isdMIPOwner.setDescription('The IP address of the iSD that currently holds the MIP.')
isdCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdCurrentTime.setStatus('current')
if mibBuilder.loadTexts: isdCurrentTime.setDescription('The current time on the cluster.')
isdVersion = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdVersion.setStatus('current')
if mibBuilder.loadTexts: isdVersion.setDescription('The version of the image on the cluster.')
isdImageTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5), )
if mibBuilder.loadTexts: isdImageTable.setStatus('current')
if mibBuilder.loadTexts: isdImageTable.setDescription('A table with resource utilization metrics for the running iSDs. This table extends isdClusterTable.')
isdImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "isdImageIndex"))
if mibBuilder.loadTexts: isdImageEntry.setStatus('current')
if mibBuilder.loadTexts: isdImageEntry.setDescription('A set of Resource utilization metrics for the iSDs.')
isdImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: isdImageIndex.setStatus('current')
if mibBuilder.loadTexts: isdImageIndex.setDescription('A unique index for the images installed on the cluster.')
isdImageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdImageVersion.setStatus('current')
if mibBuilder.loadTexts: isdImageVersion.setDescription('Version of the installed image')
isdImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdImageName.setStatus('current')
if mibBuilder.loadTexts: isdImageName.setDescription('Name of the installed image')
isdImageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("permanent", 1), ("current", 2), ("old", 3), ("unpacked", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdImageStatus.setStatus('current')
if mibBuilder.loadTexts: isdImageStatus.setDescription('Status of the installed images 1 - Image that has been verified to work correctly. 2 - Image that is starting up for the first time; it will eventually become permanent. 2 - Previously installed image 3 - Newly downloaded image')
isdClusterMIP = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdClusterMIP.setStatus('current')
if mibBuilder.loadTexts: isdClusterMIP.setDescription('The Management IPaddress of the cluster.')
isdClusterMask = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdClusterMask.setStatus('current')
if mibBuilder.loadTexts: isdClusterMask.setDescription('Network mask of the cluster.')
isdResourceTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1), )
if mibBuilder.loadTexts: isdResourceTable.setStatus('current')
if mibBuilder.loadTexts: isdResourceTable.setDescription('A table with resource utilization metrics for the running iSDs. This table extends isdClusterTable.')
isdResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "isdIndex"))
if mibBuilder.loadTexts: isdResourceEntry.setStatus('current')
if mibBuilder.loadTexts: isdResourceEntry.setDescription('A set of Resource utilization metrics for the iSDs.')
isdResourceUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceUptime.setStatus('current')
if mibBuilder.loadTexts: isdResourceUptime.setDescription('Uptime of the iSD.')
isdResourceCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceCpu.setStatus('current')
if mibBuilder.loadTexts: isdResourceCpu.setDescription('Resource load in percent.')
isdResourceMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceMemory.setStatus('current')
if mibBuilder.loadTexts: isdResourceMemory.setDescription('Memory utilization in percent.')
isdResourceDisk = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceDisk.setStatus('current')
if mibBuilder.loadTexts: isdResourceDisk.setDescription('Disk utilization in percent. This value is the utilization of the partition with the least percentage of free space.')
isdNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3))
if mibBuilder.loadTexts: isdNotifications.setStatus('current')
if mibBuilder.loadTexts: isdNotifications.setDescription('Notification definitions for the Alteon ISD Platform MIB.')
isdNotificationObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4))
if mibBuilder.loadTexts: isdNotificationObjects.setStatus('current')
if mibBuilder.loadTexts: isdNotificationObjects.setDescription('Notification objects for the Alteon ISD Platform MIB.')
numberOfCurrentAlarms = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfCurrentAlarms.setStatus('current')
if mibBuilder.loadTexts: numberOfCurrentAlarms.setDescription('Number of currently active alarms in the system.')
currentAlarmLastTimeChanged = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmLastTimeChanged.setStatus('current')
if mibBuilder.loadTexts: currentAlarmLastTimeChanged.setDescription('The time an entry in the currentAlarmTable was changed. It may be used by a management station as a value to poll. If the value is changed, the management station knows that the currentAlarmTable has been updated. This will have the value of sysUpTime at the time which alarm table was last updated.')
currentAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3), )
if mibBuilder.loadTexts: currentAlarmTable.setStatus('current')
if mibBuilder.loadTexts: currentAlarmTable.setDescription('A list of currently active alarms in the system.')
currentAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "currentAlarmIndex"))
if mibBuilder.loadTexts: currentAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: currentAlarmEntry.setDescription('A set of parameters that describe a currently active alarm.')
currentAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: currentAlarmIndex.setStatus('current')
if mibBuilder.loadTexts: currentAlarmIndex.setDescription('An id that uniquely identifies an alarm. Each active alarm is represented as one an entry in the currentAlarmTable.')
currentAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 2), AlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currentAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: currentAlarmSeverity.setDescription("The perceived severity of the fault. A manager can set this value to clear only. When set to clear, the alarm is removed from this table, and a 'clearAlarm' event is generated.")
currentAlarmOid = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmOid.setStatus('current')
if mibBuilder.loadTexts: currentAlarmOid.setDescription('The SNMP Notification which was sent to represent the alarm.')
currentAlarmObject = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmObject.setStatus('current')
if mibBuilder.loadTexts: currentAlarmObject.setDescription('The alarming object.')
currentAlarmCause = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmCause.setStatus('current')
if mibBuilder.loadTexts: currentAlarmCause.setDescription('The probable cause of the alarm.')
currentAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmTime.setStatus('current')
if mibBuilder.loadTexts: currentAlarmTime.setDescription('The time the fault was detected.')
isdEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1))
if mibBuilder.loadTexts: isdEvents.setStatus('current')
if mibBuilder.loadTexts: isdEvents.setDescription('This group lists events generated by iSDs in the cluster.')
isdAlarms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2))
if mibBuilder.loadTexts: isdAlarms.setStatus('current')
if mibBuilder.loadTexts: isdAlarms.setDescription('This group lists alarms generates by iSDs in the cluster. An alarm is a special form of event which represents a fault in the system that needs to be reported.')
isdAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 1)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmOid"))
if mibBuilder.loadTexts: isdAlarmCleared.setStatus('current')
if mibBuilder.loadTexts: isdAlarmCleared.setDescription('This event is sent when an alarm has been cleared, either by the system or by an operator. Note that the currentAlarmIndex is implicitly sent as the instance identifier for currentAlarmOid. All alarm-specific variables sent in the alarm notification is also sent in this notifications.')
isdTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 2)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"), ("ALTEON-ISD-PLATFORM-MIB", "isdEventDescription"))
if mibBuilder.loadTexts: isdTopologyChange.setStatus('current')
if mibBuilder.loadTexts: isdTopologyChange.setDescription('This event signals that the topology of the iSD cluster has changed.')
isdAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 4)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"))
if mibBuilder.loadTexts: isdAuthenticationFailure.setStatus('current')
if mibBuilder.loadTexts: isdAuthenticationFailure.setDescription('This event signals that an authentication failure has occurred.')
isdMipMigration = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 5)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
if mibBuilder.loadTexts: isdMipMigration.setStatus('current')
if mibBuilder.loadTexts: isdMipMigration.setDescription('This event signals that the master IP has migrated to another iSD.')
isdDown = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 1)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
if mibBuilder.loadTexts: isdDown.setStatus('current')
if mibBuilder.loadTexts: isdDown.setDescription('This alarm is sent when the iSD goes down.')
isdUp = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 2)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
if mibBuilder.loadTexts: isdUp.setStatus('current')
if mibBuilder.loadTexts: isdUp.setDescription('This alarm is sent when the iSD comes back online.')
isdSingleMaster = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 3)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"))
if mibBuilder.loadTexts: isdSingleMaster.setStatus('current')
if mibBuilder.loadTexts: isdSingleMaster.setDescription('This alarm is sent when there is just a sindle iSD master left in the system. The fault tolerance level of the system is severly degraded - if the last master fails, the system cannot be reconfigured. This alarm is only set if there are more than two masters configured in the system.')
isdMemoryStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 4)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"), ("ALTEON-ISD-PLATFORM-MIB", "isdUtilization"))
if mibBuilder.loadTexts: isdMemoryStateChange.setStatus('current')
if mibBuilder.loadTexts: isdMemoryStateChange.setDescription('This alarm is sent when there is a change in the current status of the memory. It is expected that the user will be able to configure this. The defaults could be that 75% would signal a warning and 90% would be an error. The user would be able to specify these values themselves as well as be able to rearm the system.')
isdCpuStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 5)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"), ("ALTEON-ISD-PLATFORM-MIB", "isdLoad"))
if mibBuilder.loadTexts: isdCpuStateChange.setStatus('current')
if mibBuilder.loadTexts: isdCpuStateChange.setDescription('This alarm is sent when there is a change in the current status of the CPU. It is expected that the user will be able to configure this. The defaults could be that 75% would signal a warning and 90% would be an error. The user would be able to specify these values themselves as well as be able to rearm the system.')
isdDiskStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 6)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"), ("ALTEON-ISD-PLATFORM-MIB", "isdUtilization"))
if mibBuilder.loadTexts: isdDiskStateChange.setStatus('current')
if mibBuilder.loadTexts: isdDiskStateChange.setDescription('This alarm is sent when there is a change in the current status of the Disk. The partition with the greatest utilization is examined. It is expected that the user will be able to configure this. The defaults could be that 75% would signal a warning and 90% would be an error. The user would be able to specify these values themselves as well as be able to rearm the system.')
isdEventTime = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 1), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdEventTime.setStatus('current')
if mibBuilder.loadTexts: isdEventTime.setDescription('This object may be included in a notification definition for an event. It specifies the time the event was generated.')
isdEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdEventDescription.setStatus('current')
if mibBuilder.loadTexts: isdEventDescription.setDescription('This object may be included in a notification definition for an event. It specifies extra information.')
isdUtilization = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdUtilization.setStatus('current')
if mibBuilder.loadTexts: isdUtilization.setDescription('Resource utilization in percent.')
isdLoad = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 4), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdLoad.setStatus('current')
if mibBuilder.loadTexts: isdLoad.setDescription('Resource load. 200 means in essence 2 processes want the CPU; this is considered a warning level. 300 means three processes want the CPU; this is considered a critical level.')
mibBuilder.exportSymbols("ALTEON-ISD-PLATFORM-MIB", isdCpuStateChange=isdCpuStateChange, isdMipMigration=isdMipMigration, isdEvents=isdEvents, isdAlarms=isdAlarms, PYSNMP_MODULE_ID=alteonPlatformISDModule, isdVersion=isdVersion, isdNotifications=isdNotifications, currentAlarmLastTimeChanged=currentAlarmLastTimeChanged, currentAlarmTime=currentAlarmTime, isdMIPOwner=isdMIPOwner, isdIndex=isdIndex, isdObjects=isdObjects, isdSingleMaster=isdSingleMaster, isdResourceUptime=isdResourceUptime, currentAlarmCause=currentAlarmCause, isdImageTable=isdImageTable, isdCluster=isdCluster, isdResourceEntry=isdResourceEntry, numberOfCurrentAlarms=numberOfCurrentAlarms, alteonISDPlatformMIB=alteonISDPlatformMIB, currentAlarmTable=currentAlarmTable, isdUp=isdUp, isdUtilization=isdUtilization, currentAlarmIndex=currentAlarmIndex, isdTopologyChange=isdTopologyChange, isdClusterEntry=isdClusterEntry, currentAlarmObject=currentAlarmObject, isdImageVersion=isdImageVersion, isdClusterMask=isdClusterMask, isdOperStatus=isdOperStatus, isdImageName=isdImageName, isdClusterTable=isdClusterTable, isdClusterMIP=isdClusterMIP, currentAlarmEntry=currentAlarmEntry, isdImageEntry=isdImageEntry, isdNotificationObjects=isdNotificationObjects, isdAlarmCleared=isdAlarmCleared, AlarmSeverity=AlarmSeverity, isdLoad=isdLoad, isdMemoryStateChange=isdMemoryStateChange, isdResourceMemory=isdResourceMemory, isdResourceTable=isdResourceTable, isdDown=isdDown, isdCurrentTime=isdCurrentTime, isdImageStatus=isdImageStatus, isdDiskStateChange=isdDiskStateChange, isdEventTime=isdEventTime, isdResourceDisk=isdResourceDisk, currentAlarmSeverity=currentAlarmSeverity, alteonPlatformISDModule=alteonPlatformISDModule, currentAlarmOid=currentAlarmOid, isdEventDescription=isdEventDescription, isdType=isdType, isdResourceCpu=isdResourceCpu, currentAlarm=currentAlarm, isdAuthenticationFailure=isdAuthenticationFailure, isdMonitor=isdMonitor, isdIP=isdIP, isdImageIndex=isdImageIndex)
