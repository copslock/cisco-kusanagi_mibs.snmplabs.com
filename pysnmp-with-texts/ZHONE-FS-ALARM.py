#
# PySNMP MIB module ZHONE-FS-ALARM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-FS-ALARM
# Produced by pysmi-0.3.4 at Wed May  1 15:47:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, iso, Counter32, NotificationType, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Unsigned32, IpAddress, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "iso", "Counter32", "NotificationType", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Unsigned32", "IpAddress", "ModuleIdentity", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
zhoneTrapsSequenceNumber, zhoneTrapVersion, zhoneTrapsSeverity = mibBuilder.importSymbols("ZHONE-SYSTEM-MIB", "zhoneTrapsSequenceNumber", "zhoneTrapVersion", "zhoneTrapsSeverity")
zhoneZmsProduct, = mibBuilder.importSymbols("Zhone", "zhoneZmsProduct")
faultServiceAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1))
faultServiceAlarm.setRevisions(('2013-04-21 16:29', '2009-04-29 13:47', '2001-07-27 16:55',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: faultServiceAlarm.setRevisionsDescriptions(('Correct binding order in alarmReceived and alarmCleared', 'Add bindings to notifications.', '01.00.00 - Initial version',))
if mibBuilder.loadTexts: faultServiceAlarm.setLastUpdated('201304211711Z')
if mibBuilder.loadTexts: faultServiceAlarm.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: faultServiceAlarm.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: faultServiceAlarm.setDescription('MIB module to define a trap, that will be used to forward alarms generated Fault Service.')
faultServiceDefinitions = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1))
if mibBuilder.loadTexts: faultServiceDefinitions.setStatus('current')
if mibBuilder.loadTexts: faultServiceDefinitions.setDescription('Variable bindings contained in a Fault Service trap are defined here.')
alarmName = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 45))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmName.setStatus('current')
if mibBuilder.loadTexts: alarmName.setDescription('Alarm name.')
alarmDescription = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmDescription.setStatus('current')
if mibBuilder.loadTexts: alarmDescription.setDescription('Alarm description.')
alarmType = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmType.setStatus('current')
if mibBuilder.loadTexts: alarmType.setDescription('Entity type on which the alarm was generated.')
alarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("informational", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmSeverity.setDescription('Severity of alarm.')
alarmTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 5), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmTimestamp.setStatus('current')
if mibBuilder.loadTexts: alarmTimestamp.setDescription('Date and Time when the alarm was received or cleared.')
alarmDevice = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 6), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmDevice.setStatus('current')
if mibBuilder.loadTexts: alarmDevice.setDescription('IP address of the device on which alarm was generated.')
alarmShelf = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32768))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmShelf.setStatus('current')
if mibBuilder.loadTexts: alarmShelf.setDescription('Shelf number on which the alarm was generated.')
alarmSlot = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmSlot.setStatus('current')
if mibBuilder.loadTexts: alarmSlot.setDescription('Slot number on which the alarm was generated.')
alarmPort = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 9), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmPort.setStatus('current')
if mibBuilder.loadTexts: alarmPort.setDescription('Port number on which the alarm was generated.')
alarmSubPort = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmSubPort.setStatus('current')
if mibBuilder.loadTexts: alarmSubPort.setDescription('SubPort number on which the alarm was generated.')
alarmDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmDeviceName.setStatus('current')
if mibBuilder.loadTexts: alarmDeviceName.setDescription('Device name on which the alarm was generated.')
alarmCpeInternal = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 12), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmCpeInternal.setStatus('current')
if mibBuilder.loadTexts: alarmCpeInternal.setDescription('For alarms on CPEs. True if alarm was reported by the CPE itself in response to a physical condition on the CPE or on one of its ports.')
alarmCpePortType = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 13), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmCpePortType.setStatus('current')
if mibBuilder.loadTexts: alarmCpePortType.setDescription('For alarms on CPE ports. This is the type of port for which the alarm is being reported. For OMCI ONTs, the is the ME id.')
alarmCpePortId = MibScalar((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 1, 14), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmCpePortId.setStatus('current')
if mibBuilder.loadTexts: alarmCpePortId.setDescription('For alarms on CPE ports. This is the identifier of the CPE port for which the alarm is being generated.')
faultServiceTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2))
if mibBuilder.loadTexts: faultServiceTraps.setStatus('current')
if mibBuilder.loadTexts: faultServiceTraps.setDescription('Traps that will be generated by Fault Service are defined here.')
faultServiceV2Traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2, 0))
if mibBuilder.loadTexts: faultServiceV2Traps.setStatus('current')
if mibBuilder.loadTexts: faultServiceV2Traps.setDescription('Definition for specification of v2 traps.')
alarmReceived = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2, 0, 1)).setObjects(("ZHONE-SYSTEM-MIB", "zhoneTrapVersion"), ("ZHONE-SYSTEM-MIB", "zhoneTrapsSequenceNumber"), ("ZHONE-SYSTEM-MIB", "zhoneTrapsSeverity"), ("ZHONE-FS-ALARM", "alarmName"), ("ZHONE-FS-ALARM", "alarmDescription"), ("ZHONE-FS-ALARM", "alarmType"), ("ZHONE-FS-ALARM", "alarmSeverity"), ("ZHONE-FS-ALARM", "alarmTimestamp"), ("ZHONE-FS-ALARM", "alarmDevice"), ("ZHONE-FS-ALARM", "alarmShelf"), ("ZHONE-FS-ALARM", "alarmSlot"), ("ZHONE-FS-ALARM", "alarmPort"), ("ZHONE-FS-ALARM", "alarmSubPort"), ("ZHONE-FS-ALARM", "alarmDeviceName"), ("ZHONE-FS-ALARM", "alarmCpeInternal"), ("ZHONE-FS-ALARM", "alarmCpePortType"), ("ZHONE-FS-ALARM", "alarmCpePortId"))
if mibBuilder.loadTexts: alarmReceived.setStatus('current')
if mibBuilder.loadTexts: alarmReceived.setDescription('Alarm received definition')
alarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 2, 0, 2)).setObjects(("ZHONE-SYSTEM-MIB", "zhoneTrapVersion"), ("ZHONE-SYSTEM-MIB", "zhoneTrapsSequenceNumber"), ("ZHONE-SYSTEM-MIB", "zhoneTrapsSeverity"), ("ZHONE-FS-ALARM", "alarmName"), ("ZHONE-FS-ALARM", "alarmDescription"), ("ZHONE-FS-ALARM", "alarmType"), ("ZHONE-FS-ALARM", "alarmSeverity"), ("ZHONE-FS-ALARM", "alarmTimestamp"), ("ZHONE-FS-ALARM", "alarmDevice"), ("ZHONE-FS-ALARM", "alarmShelf"), ("ZHONE-FS-ALARM", "alarmSlot"), ("ZHONE-FS-ALARM", "alarmPort"), ("ZHONE-FS-ALARM", "alarmSubPort"), ("ZHONE-FS-ALARM", "alarmDeviceName"), ("ZHONE-FS-ALARM", "alarmCpeInternal"), ("ZHONE-FS-ALARM", "alarmCpePortType"), ("ZHONE-FS-ALARM", "alarmCpePortId"))
if mibBuilder.loadTexts: alarmCleared.setStatus('current')
if mibBuilder.loadTexts: alarmCleared.setDescription('Alarm clearing trap.')
faultServiceCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3))
if mibBuilder.loadTexts: faultServiceCompliances.setStatus('current')
if mibBuilder.loadTexts: faultServiceCompliances.setDescription('Group definition for V2 compliance.')
faultServiceGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3, 1))
if mibBuilder.loadTexts: faultServiceGroups.setStatus('current')
if mibBuilder.loadTexts: faultServiceGroups.setDescription('Group specifications for fault service.')
faultServiceAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3, 1, 1)).setObjects(("ZHONE-FS-ALARM", "alarmName"), ("ZHONE-FS-ALARM", "alarmDescription"), ("ZHONE-FS-ALARM", "alarmType"), ("ZHONE-FS-ALARM", "alarmSeverity"), ("ZHONE-FS-ALARM", "alarmTimestamp"), ("ZHONE-FS-ALARM", "alarmDevice"), ("ZHONE-FS-ALARM", "alarmShelf"), ("ZHONE-FS-ALARM", "alarmSlot"), ("ZHONE-FS-ALARM", "alarmPort"), ("ZHONE-FS-ALARM", "alarmSubPort"), ("ZHONE-FS-ALARM", "alarmDeviceName"), ("ZHONE-FS-ALARM", "alarmCpeInternal"), ("ZHONE-FS-ALARM", "alarmCpePortType"), ("ZHONE-FS-ALARM", "alarmCpePortId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faultServiceAlarmGroup = faultServiceAlarmGroup.setStatus('current')
if mibBuilder.loadTexts: faultServiceAlarmGroup.setDescription('Fault Service Group.')
faultServiceTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 3, 1, 2)).setObjects(("ZHONE-FS-ALARM", "alarmReceived"), ("ZHONE-FS-ALARM", "alarmCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faultServiceTrapGroup = faultServiceTrapGroup.setStatus('current')
if mibBuilder.loadTexts: faultServiceTrapGroup.setDescription('Description.')
faultServiceImports = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 7, 1, 4))
if mibBuilder.loadTexts: faultServiceImports.setStatus('current')
if mibBuilder.loadTexts: faultServiceImports.setDescription('Objects imported from other mibs to serve as bindings in the ZMS traps')
mibBuilder.exportSymbols("ZHONE-FS-ALARM", PYSNMP_MODULE_ID=faultServiceAlarm, faultServiceTrapGroup=faultServiceTrapGroup, faultServiceGroups=faultServiceGroups, alarmDeviceName=alarmDeviceName, alarmSlot=alarmSlot, faultServiceCompliances=faultServiceCompliances, faultServiceTraps=faultServiceTraps, alarmDescription=alarmDescription, alarmType=alarmType, alarmSubPort=alarmSubPort, faultServiceAlarm=faultServiceAlarm, alarmCpeInternal=alarmCpeInternal, alarmReceived=alarmReceived, alarmPort=alarmPort, alarmCpePortType=alarmCpePortType, alarmCleared=alarmCleared, faultServiceAlarmGroup=faultServiceAlarmGroup, faultServiceDefinitions=faultServiceDefinitions, alarmName=alarmName, alarmShelf=alarmShelf, alarmTimestamp=alarmTimestamp, alarmSeverity=alarmSeverity, faultServiceV2Traps=faultServiceV2Traps, faultServiceImports=faultServiceImports, alarmCpePortId=alarmCpePortId, alarmDevice=alarmDevice)
