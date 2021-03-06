#
# PySNMP MIB module TAILF-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TAILF-ALARM-MIB
# Produced by pysmi-0.3.4 at Thu Aug  8 14:21:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.7.0 by user davwang4
# Using Python version 2.7.15 (default, May  1 2018, 16:44:08) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
IANAItuEventType, = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuEventType")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
TruthValue, DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "DateAndTime")
TfAlarmOperatorState, TfUtf8String, TfYANGResource, TfProbableCause, TfAlarmIndex = mibBuilder.importSymbols("TAILF-ALARM-TC-MIB", "TfAlarmOperatorState", "TfUtf8String", "TfYANGResource", "TfProbableCause", "TfAlarmIndex")
tfModules, = mibBuilder.importSymbols("TAILF-TOP-MIB", "tfModules")
tfAlarmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 24961, 2, 103))
tfAlarmMIB.setRevisions(('2012-08-30 00:00', '2011-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tfAlarmMIB.setRevisionsDescriptions(('Released as part of NCS-2.0. Changed tfAlarmType to be a string. Added tfAlarmObjectStr. Added tfAlarmSpecificProblem.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: tfAlarmMIB.setLastUpdated('201208300000Z')
if mibBuilder.loadTexts: tfAlarmMIB.setOrganization('Tail-f Systems AB')
if mibBuilder.loadTexts: tfAlarmMIB.setContactInfo('support@tail-f.com')
if mibBuilder.loadTexts: tfAlarmMIB.setDescription('Alarm MIB for Tail-f Systems. This MIB represents alarms as states, where a row in the alarm table corresponds to a device, an object within the device and an unique alarm type. If the severity of an alarm or a the clear state is changed this is an update to an existing alarm entry and not a new. When the resource reports a clear on the alarm the alarm entry still exists until administrative processes purges the alarm list. These procedures are out of the scope for this module.')
tfAlarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1))
tfAlarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2))
tfAlarmNotifsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0))
tfAlarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 24961, 2, 103, 10))
tfAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1))
tfAlarmNumber = MibScalar((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmNumber.setStatus('current')
if mibBuilder.loadTexts: tfAlarmNumber.setDescription('This object shows the total number of of entries in the tfAlarmTable.')
tfAlarmLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmLastChanged.setStatus('current')
if mibBuilder.loadTexts: tfAlarmLastChanged.setDescription('A timestamp when the active alarm table was last changed. The value can be used by a manager to initiate an alarm resynchronization procedure. NOTE: All fields of the DateAndTime MUST be filled out, including the hours and minutes from UTC. As such, the value should be 11 octets long.')
tfAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5), )
if mibBuilder.loadTexts: tfAlarmTable.setStatus('current')
if mibBuilder.loadTexts: tfAlarmTable.setDescription('This table list all alarms in the system. Entries are created when a resource has a new alarm state. If the same resource has several active alarms, with different Alarm Types, this will be represented as separate rows. Rows disappear based on administrative procedures outside the scope of this module. Note that this means that cleared alarms exist in the table. Rows can be changed when an alarm changes severity, additional text or clearance state.')
tfAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1), ).setIndexNames((0, "TAILF-ALARM-MIB", "tfAlarmIndex"))
if mibBuilder.loadTexts: tfAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: tfAlarmEntry.setDescription('One entry in the table holds one alarm for a given resource. Entries are created by the system when a resource has a new alarm state. Entries are deleted by alarm pruning actions. An alarm that is cleared by a resource is still kept in the alarm list until pruned by a user. Alarm severity and additional text can later be changed in a row.')
tfAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 1), TfAlarmIndex())
if mibBuilder.loadTexts: tfAlarmIndex.setStatus('current')
if mibBuilder.loadTexts: tfAlarmIndex.setDescription('A unique value, greater than zero, for each alarm. The value for each alarm must remain constant at least from one re-initialization of the entity to the next re-initialization.')
tfAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmType.setStatus('current')
if mibBuilder.loadTexts: tfAlarmType.setDescription('This provides an identification of the alarm type. Together with tfAlarmSpecificProblem, this is a unique identification of the alarm. Different managed object types and instances can share alarm types, but if the same managed object reports the same alarm type, it is to be considered as the same alarm state. The alarm type is a simplification of the different X.733 and 3GPP alarm IRP alarm correlation mechanisms based on EventType, ProbableCause, SpecificProblem and NotificationId.')
tfAlarmDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmDevice.setStatus('current')
if mibBuilder.loadTexts: tfAlarmDevice.setDescription('The name of the managed device. May also be the system itself for self-management alarms. Note that this object is not fine-grained enough to pinpoint the alarming resource. The alarm object within the device is the exact alarming resource.')
tfAlarmObject = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 4), TfYANGResource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmObject.setStatus('current')
if mibBuilder.loadTexts: tfAlarmObject.setDescription('Name of alarm object within a device based on YANG naming. Note that the granularity must be good enough to guarantee unique alarm states and relevant resource identification to the operator.')
tfAlarmObjectOID = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmObjectOID.setStatus('current')
if mibBuilder.loadTexts: tfAlarmObjectOID.setDescription('Name of alarm object based on SNMP naming. Note that the granularity must be good enough to guarantee unique alarm states and relevant resource identification to the operator.')
tfAlarmObjectStr = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 6), TfUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmObjectStr.setStatus('current')
if mibBuilder.loadTexts: tfAlarmObjectStr.setDescription('Name of alarm object based on any other naming. Note that the granularity must be good enough to guarantee unique alarm states and relevant resource identification to the operator.')
tfAlarmSpecificProblem = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 7), TfUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmSpecificProblem.setStatus('current')
if mibBuilder.loadTexts: tfAlarmSpecificProblem.setDescription("This object is used when the 'tfAlarmType' object cannot uniquely identify the alarm type. Normally, this is not the case, and this leaf is the empty string.")
tfAlarmEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 8), IANAItuEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmEventType.setReference("ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992")
if mibBuilder.loadTexts: tfAlarmEventType.setStatus('current')
if mibBuilder.loadTexts: tfAlarmEventType.setDescription('The event type as defined in X.733/X.736.')
tfAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 9), TfProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmProbableCause.setReference("ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992")
if mibBuilder.loadTexts: tfAlarmProbableCause.setStatus('current')
if mibBuilder.loadTexts: tfAlarmProbableCause.setDescription('The probable cause as defined in X.733/X.736.')
tfAlarmOrigTime = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmOrigTime.setStatus('current')
if mibBuilder.loadTexts: tfAlarmOrigTime.setDescription('Time for alarm raise')
tfAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmTime.setReference("ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992")
if mibBuilder.loadTexts: tfAlarmTime.setStatus('current')
if mibBuilder.loadTexts: tfAlarmTime.setDescription('A time stamp of the alarm state change event. Note that this variable represents the last change of the alarm state, like changed severity or additional text. If the alarm has not changed state this variable represents the alarm raise time and will be the same as tfAlarmOrigTime. NOTE: All fields of the DateAndTime MUST be filled out, including the hours and minutes from UTC. As such, the value should be 11 octets long.')
tfAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 12), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmSeverity.setReference("ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992")
if mibBuilder.loadTexts: tfAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: tfAlarmSeverity.setDescription('The severity of the alarm as defined by X.733. Note that this may not be the original severity since the alarm may have changed severity. For cleared alarms, this is the last severity that is not equal to cleared.')
tfAlarmCleared = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmCleared.setStatus('current')
if mibBuilder.loadTexts: tfAlarmCleared.setDescription('Indicates if the alarm is cleared or not.')
tfAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 14), TfUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmText.setReference("ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992")
if mibBuilder.loadTexts: tfAlarmText.setStatus('current')
if mibBuilder.loadTexts: tfAlarmText.setDescription('A user friendly text describing the alarm. Intended for human consumption.')
tfAlarmOperatorState = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 15), TfAlarmOperatorState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmOperatorState.setStatus('current')
if mibBuilder.loadTexts: tfAlarmOperatorState.setDescription('The operator state of the alarm.')
tfAlarmOperatorNote = MibTableColumn((1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 16), TfUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tfAlarmOperatorNote.setStatus('current')
if mibBuilder.loadTexts: tfAlarmOperatorNote.setDescription('Operator note for the alarm.')
tfAlarmIndeterminate = NotificationType((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 1)).setObjects(("TAILF-ALARM-MIB", "tfAlarmType"), ("TAILF-ALARM-MIB", "tfAlarmDevice"), ("TAILF-ALARM-MIB", "tfAlarmObject"), ("TAILF-ALARM-MIB", "tfAlarmObjectOID"), ("TAILF-ALARM-MIB", "tfAlarmObjectStr"), ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"), ("TAILF-ALARM-MIB", "tfAlarmEventType"), ("TAILF-ALARM-MIB", "tfAlarmProbableCause"), ("TAILF-ALARM-MIB", "tfAlarmTime"), ("TAILF-ALARM-MIB", "tfAlarmText"))
if mibBuilder.loadTexts: tfAlarmIndeterminate.setStatus('current')
if mibBuilder.loadTexts: tfAlarmIndeterminate.setDescription('Indeterminate alarms are sent when errors occur for which the severity level cannot be determined.')
tfAlarmWarning = NotificationType((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 2)).setObjects(("TAILF-ALARM-MIB", "tfAlarmType"), ("TAILF-ALARM-MIB", "tfAlarmDevice"), ("TAILF-ALARM-MIB", "tfAlarmObject"), ("TAILF-ALARM-MIB", "tfAlarmObjectOID"), ("TAILF-ALARM-MIB", "tfAlarmObjectStr"), ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"), ("TAILF-ALARM-MIB", "tfAlarmEventType"), ("TAILF-ALARM-MIB", "tfAlarmProbableCause"), ("TAILF-ALARM-MIB", "tfAlarmTime"), ("TAILF-ALARM-MIB", "tfAlarmText"))
if mibBuilder.loadTexts: tfAlarmWarning.setStatus('current')
if mibBuilder.loadTexts: tfAlarmWarning.setDescription("Warning alarms are sent for potential problems that haven't yet caused any significant effects.")
tfAlarmMinor = NotificationType((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 3)).setObjects(("TAILF-ALARM-MIB", "tfAlarmType"), ("TAILF-ALARM-MIB", "tfAlarmDevice"), ("TAILF-ALARM-MIB", "tfAlarmObject"), ("TAILF-ALARM-MIB", "tfAlarmObjectOID"), ("TAILF-ALARM-MIB", "tfAlarmObjectStr"), ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"), ("TAILF-ALARM-MIB", "tfAlarmEventType"), ("TAILF-ALARM-MIB", "tfAlarmProbableCause"), ("TAILF-ALARM-MIB", "tfAlarmTime"), ("TAILF-ALARM-MIB", "tfAlarmText"))
if mibBuilder.loadTexts: tfAlarmMinor.setStatus('current')
if mibBuilder.loadTexts: tfAlarmMinor.setDescription('Minor alarms are sent for non-service affecting problems, and indicate that corrective action should be taken to prevent a more serious fault.')
tfAlarmMajor = NotificationType((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 4)).setObjects(("TAILF-ALARM-MIB", "tfAlarmType"), ("TAILF-ALARM-MIB", "tfAlarmDevice"), ("TAILF-ALARM-MIB", "tfAlarmObject"), ("TAILF-ALARM-MIB", "tfAlarmObjectOID"), ("TAILF-ALARM-MIB", "tfAlarmObjectStr"), ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"), ("TAILF-ALARM-MIB", "tfAlarmEventType"), ("TAILF-ALARM-MIB", "tfAlarmProbableCause"), ("TAILF-ALARM-MIB", "tfAlarmTime"), ("TAILF-ALARM-MIB", "tfAlarmText"))
if mibBuilder.loadTexts: tfAlarmMajor.setStatus('current')
if mibBuilder.loadTexts: tfAlarmMajor.setDescription('Major alarms are sent for service affecting problems that require urgent corrective action.')
tfAlarmCritical = NotificationType((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 5)).setObjects(("TAILF-ALARM-MIB", "tfAlarmType"), ("TAILF-ALARM-MIB", "tfAlarmDevice"), ("TAILF-ALARM-MIB", "tfAlarmObject"), ("TAILF-ALARM-MIB", "tfAlarmObjectOID"), ("TAILF-ALARM-MIB", "tfAlarmObjectStr"), ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"), ("TAILF-ALARM-MIB", "tfAlarmEventType"), ("TAILF-ALARM-MIB", "tfAlarmProbableCause"), ("TAILF-ALARM-MIB", "tfAlarmTime"), ("TAILF-ALARM-MIB", "tfAlarmText"))
if mibBuilder.loadTexts: tfAlarmCritical.setStatus('current')
if mibBuilder.loadTexts: tfAlarmCritical.setDescription('Critical alarms are sent for service affecting problems that require immediate corrective action.')
tfAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 6)).setObjects(("TAILF-ALARM-MIB", "tfAlarmType"), ("TAILF-ALARM-MIB", "tfAlarmDevice"), ("TAILF-ALARM-MIB", "tfAlarmObject"), ("TAILF-ALARM-MIB", "tfAlarmObjectOID"), ("TAILF-ALARM-MIB", "tfAlarmObjectStr"), ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"), ("TAILF-ALARM-MIB", "tfAlarmEventType"), ("TAILF-ALARM-MIB", "tfAlarmProbableCause"), ("TAILF-ALARM-MIB", "tfAlarmTime"), ("TAILF-ALARM-MIB", "tfAlarmText"))
if mibBuilder.loadTexts: tfAlarmClear.setStatus('current')
if mibBuilder.loadTexts: tfAlarmClear.setDescription('A clear alarm indicates that a previously reported alarm is now cleared by the underlying resource.')
tfAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 1))
tfAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 1, 1)).setObjects(("TAILF-ALARM-MIB", "tfAlarmNotifs"), ("TAILF-ALARM-MIB", "tfAlarmObjs"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tfAlarmCompliance = tfAlarmCompliance.setStatus('current')
if mibBuilder.loadTexts: tfAlarmCompliance.setDescription('Compliance information for this MIB module')
tfAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 2))
tfAlarmNotifs = NotificationGroup((1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 2, 1)).setObjects(("TAILF-ALARM-MIB", "tfAlarmIndeterminate"), ("TAILF-ALARM-MIB", "tfAlarmWarning"), ("TAILF-ALARM-MIB", "tfAlarmMinor"), ("TAILF-ALARM-MIB", "tfAlarmMajor"), ("TAILF-ALARM-MIB", "tfAlarmCritical"), ("TAILF-ALARM-MIB", "tfAlarmClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tfAlarmNotifs = tfAlarmNotifs.setStatus('current')
if mibBuilder.loadTexts: tfAlarmNotifs.setDescription('The alarm notifications that can be sent from the system.')
tfAlarmObjs = ObjectGroup((1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 2, 2)).setObjects(("TAILF-ALARM-MIB", "tfAlarmType"), ("TAILF-ALARM-MIB", "tfAlarmNumber"), ("TAILF-ALARM-MIB", "tfAlarmLastChanged"), ("TAILF-ALARM-MIB", "tfAlarmEventType"), ("TAILF-ALARM-MIB", "tfAlarmProbableCause"), ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"), ("TAILF-ALARM-MIB", "tfAlarmCleared"), ("TAILF-ALARM-MIB", "tfAlarmOperatorState"), ("TAILF-ALARM-MIB", "tfAlarmOperatorNote"), ("TAILF-ALARM-MIB", "tfAlarmDevice"), ("TAILF-ALARM-MIB", "tfAlarmObject"), ("TAILF-ALARM-MIB", "tfAlarmObjectOID"), ("TAILF-ALARM-MIB", "tfAlarmObjectStr"), ("TAILF-ALARM-MIB", "tfAlarmOrigTime"), ("TAILF-ALARM-MIB", "tfAlarmTime"), ("TAILF-ALARM-MIB", "tfAlarmSeverity"), ("TAILF-ALARM-MIB", "tfAlarmText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tfAlarmObjs = tfAlarmObjs.setStatus('current')
if mibBuilder.loadTexts: tfAlarmObjs.setDescription('The alarm objects.')
mibBuilder.exportSymbols("TAILF-ALARM-MIB", tfAlarmNotifsPrefix=tfAlarmNotifsPrefix, tfAlarmObjects=tfAlarmObjects, tfAlarmTable=tfAlarmTable, tfAlarmCompliances=tfAlarmCompliances, tfAlarmIndeterminate=tfAlarmIndeterminate, tfAlarmLastChanged=tfAlarmLastChanged, tfAlarmNotifications=tfAlarmNotifications, tfAlarmText=tfAlarmText, tfAlarmMIB=tfAlarmMIB, tfAlarmMajor=tfAlarmMajor, tfAlarmEventType=tfAlarmEventType, tfAlarmCritical=tfAlarmCritical, tfAlarmEntry=tfAlarmEntry, tfAlarmOrigTime=tfAlarmOrigTime, PYSNMP_MODULE_ID=tfAlarmMIB, tfAlarms=tfAlarms, tfAlarmDevice=tfAlarmDevice, tfAlarmMinor=tfAlarmMinor, tfAlarmCompliance=tfAlarmCompliance, tfAlarmObjectStr=tfAlarmObjectStr, tfAlarmNumber=tfAlarmNumber, tfAlarmSpecificProblem=tfAlarmSpecificProblem, tfAlarmWarning=tfAlarmWarning, tfAlarmObject=tfAlarmObject, tfAlarmClear=tfAlarmClear, tfAlarmConformance=tfAlarmConformance, tfAlarmType=tfAlarmType, tfAlarmNotifs=tfAlarmNotifs, tfAlarmGroups=tfAlarmGroups, tfAlarmTime=tfAlarmTime, tfAlarmCleared=tfAlarmCleared, tfAlarmObjectOID=tfAlarmObjectOID, tfAlarmIndex=tfAlarmIndex, tfAlarmSeverity=tfAlarmSeverity, tfAlarmObjs=tfAlarmObjs, tfAlarmOperatorState=tfAlarmOperatorState, tfAlarmOperatorNote=tfAlarmOperatorNote, tfAlarmProbableCause=tfAlarmProbableCause)
