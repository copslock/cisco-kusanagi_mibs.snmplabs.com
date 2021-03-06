#
# PySNMP MIB module ZHNSYSMON (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHNSYSMON
# Produced by pysmi-0.3.4 at Mon Apr 29 21:40:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, ObjectIdentity, Bits, Counter64, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, IpAddress, Gauge32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter64", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "IpAddress", "Gauge32", "TimeTicks", "NotificationType")
DisplayString, DateAndTime, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "RowStatus")
zhoneWtn, = mibBuilder.importSymbols("Zhone", "zhoneWtn")
zhnSysMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1))
zhnSysMon.setRevisions(('2010-09-24 00:00', '2010-06-21 00:00', '2009-12-14 00:00', '2009-05-20 00:00', '2009-04-06 00:00', '2009-01-06 00:00', '2008-05-21 00:00', '2007-11-26 00:00', '2006-12-26 00:00', '2006-12-12 00:00', '2006-11-17 00:00', '2006-08-31 00:00',))
if mibBuilder.loadTexts: zhnSysMon.setLastUpdated('201009240000Z')
if mibBuilder.loadTexts: zhnSysMon.setOrganization('Zhone Technologies MIB Working Group Other information about group editing the MIB')
zhnSysMonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0))
zhnSysMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1))
zhnSysMonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 2))
zhnSysMonAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1), )
if mibBuilder.loadTexts: zhnSysMonAlarmTable.setStatus('current')
zhnSysMonAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1), ).setIndexNames((0, "ZHNSYSMON", "zhnSysMonAlarmType"), (0, "ZHNSYSMON", "zhnSysMonAlarmSeverity"), (0, "ZHNSYSMON", "zhnSysMonAlarmInterfaceName"))
if mibBuilder.loadTexts: zhnSysMonAlarmEntry.setStatus('current')
zhnSysMonAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 99))).clone(namedValues=NamedValues(("tempThresholdExceeded", 1), ("mainPowerLoss", 2), ("secondaryPowerLoss", 3), ("lowPowerMode", 4), ("selftestFailed", 5), ("interfaceDown", 6), ("processFailed", 7), ("pwDown", 8), ("pwDeleted", 9), ("pwMisconnected", 10), ("pwLOP", 11), ("pwLateFrame", 12), ("pwMalformedFrame", 13), ("pwJitterBufferOverrun", 14), ("dsx1RcvYellow", 15), ("dsx1XmtYellow", 16), ("dsx1RcvAIS", 17), ("dsx1XmtAIS", 18), ("dsx1LossOfFrame", 19), ("dsx1LossOfSignal", 20), ("dsx1LoopbackState", 21), ("dsx1TestingState", 22), ("pwClockStability", 23), ("pwClockHoldover", 24), ("pwClockStabilityIdle", 25), ("pwClockStabilityAcquisition", 26), ("pwClockStabilityTracking1", 27), ("pwClockStabilityRecovery", 28), ("onBatteryPower", 29), ("batteryPowerLow", 30), ("replaceBattery", 31), ("batteryRemoved", 32), ("onBatteryPower2", 33), ("batteryPowerLow2", 34), ("replaceBattery2", 35), ("batteryRemoved2", 36), ("doorOpened", 37), ("other", 99)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonAlarmType.setStatus('current')
zhnSysMonAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("minor", 1), ("major", 2), ("critical", 3), ("wanData", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonAlarmSeverity.setStatus('current')
zhnSysMonAlarmInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonAlarmInterfaceName.setStatus('current')
zhnSysMonAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonAlarmDescription.setStatus('current')
zhnSysMonAlarmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonAlarmRowStatus.setStatus('current')
zhnSysMonTestTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2), )
if mibBuilder.loadTexts: zhnSysMonTestTable.setStatus('current')
zhnSysMonTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1), ).setIndexNames((0, "ZHNSYSMON", "zhnSysMonTestType"), (0, "ZHNSYSMON", "zhnSysMonTestInterfaceName"))
if mibBuilder.loadTexts: zhnSysMonTestEntry.setStatus('current')
zhnSysMonTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopback", 1), ("led", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonTestType.setStatus('current')
zhnSysMonTestInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonTestInterfaceName.setStatus('current')
zhnSysMonTestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonTestRowStatus.setStatus('current')
zhnSysMonTempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3), )
if mibBuilder.loadTexts: zhnSysMonTempSensorTable.setStatus('current')
zhnSysMonTempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1), ).setIndexNames((0, "ZHNSYSMON", "zhnSysMonTempSensorId"))
if mibBuilder.loadTexts: zhnSysMonTempSensorEntry.setStatus('current')
zhnSysMonTempSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonTempSensorId.setStatus('current')
zhnSysMonTempSensorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonTempSensorRowStatus.setStatus('current')
zhnSysMonTempSensorCurr = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhnSysMonTempSensorCurr.setStatus('current')
zhnSysMonTempSensorOS = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhnSysMonTempSensorOS.setStatus('current')
zhnSysMonTempSensorHyst = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhnSysMonTempSensorHyst.setStatus('current')
zhnSysMonTempSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhnSysMonTempSensorName.setStatus('current')
zhnSysMonLinePowerTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4), )
if mibBuilder.loadTexts: zhnSysMonLinePowerTable.setStatus('current')
zhnSysMonLinePowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1), ).setIndexNames((0, "ZHNSYSMON", "zhnSysMonLinePowerLineNumber"))
if mibBuilder.loadTexts: zhnSysMonLinePowerEntry.setStatus('current')
zhnSysMonLinePowerLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonLinePowerLineNumber.setStatus('current')
zhnSysMonLinePowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonLinePowerStatus.setStatus('current')
zhnSysMonLinePowerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhnSysMonLinePowerRowStatus.setStatus('current')
zhnSysMonAlarmSetEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 1)).setObjects(("ZHNSYSMON", "zhnSysMonAlarmType"), ("ZHNSYSMON", "zhnSysMonAlarmSeverity"), ("ZHNSYSMON", "zhnSysMonAlarmInterfaceName"), ("ZHNSYSMON", "zhnSysMonAlarmDescription"))
if mibBuilder.loadTexts: zhnSysMonAlarmSetEvent.setStatus('current')
zhnSysMonAlarmClearEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 2)).setObjects(("ZHNSYSMON", "zhnSysMonAlarmType"), ("ZHNSYSMON", "zhnSysMonAlarmSeverity"), ("ZHNSYSMON", "zhnSysMonAlarmInterfaceName"), ("ZHNSYSMON", "zhnSysMonAlarmDescription"))
if mibBuilder.loadTexts: zhnSysMonAlarmClearEvent.setStatus('current')
zhnSysMonTestStartEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 3)).setObjects(("ZHNSYSMON", "zhnSysMonTestType"), ("ZHNSYSMON", "zhnSysMonTestInterfaceName"))
if mibBuilder.loadTexts: zhnSysMonTestStartEvent.setStatus('current')
zhnSysMonTestStopEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 4)).setObjects(("ZHNSYSMON", "zhnSysMonTestType"), ("ZHNSYSMON", "zhnSysMonTestInterfaceName"))
if mibBuilder.loadTexts: zhnSysMonTestStopEvent.setStatus('current')
zhnSysMonTempSensorCfgUpdateEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 5)).setObjects(("ZHNSYSMON", "zhnSysMonTempSensorId"), ("ZHNSYSMON", "zhnSysMonTempSensorOS"), ("ZHNSYSMON", "zhnSysMonTempSensorHyst"))
if mibBuilder.loadTexts: zhnSysMonTempSensorCfgUpdateEvent.setStatus('current')
zhnSysMonLinePowerCfgUpdateEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 6)).setObjects(("ZHNSYSMON", "zhnSysMonLinePowerLineNumber"), ("ZHNSYSMON", "zhnSysMonLinePowerStatus"))
if mibBuilder.loadTexts: zhnSysMonLinePowerCfgUpdateEvent.setStatus('current')
zhnSysMonReadyEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 7))
if mibBuilder.loadTexts: zhnSysMonReadyEvent.setStatus('current')
zhnSysMonConfigChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 5504, 2, 5, 1, 0, 8))
if mibBuilder.loadTexts: zhnSysMonConfigChangeEvent.setStatus('current')
mibBuilder.exportSymbols("ZHNSYSMON", zhnSysMonAlarmClearEvent=zhnSysMonAlarmClearEvent, PYSNMP_MODULE_ID=zhnSysMon, zhnSysMonTempSensorId=zhnSysMonTempSensorId, zhnSysMonTempSensorCurr=zhnSysMonTempSensorCurr, zhnSysMonLinePowerStatus=zhnSysMonLinePowerStatus, zhnSysMonTempSensorEntry=zhnSysMonTempSensorEntry, zhnSysMonTempSensorHyst=zhnSysMonTempSensorHyst, zhnSysMonTempSensorRowStatus=zhnSysMonTempSensorRowStatus, zhnSysMonObjects=zhnSysMonObjects, zhnSysMonAlarmDescription=zhnSysMonAlarmDescription, zhnSysMonTestStartEvent=zhnSysMonTestStartEvent, zhnSysMonAlarmEntry=zhnSysMonAlarmEntry, zhnSysMonNotifications=zhnSysMonNotifications, zhnSysMonTestRowStatus=zhnSysMonTestRowStatus, zhnSysMonAlarmTable=zhnSysMonAlarmTable, zhnSysMonLinePowerCfgUpdateEvent=zhnSysMonLinePowerCfgUpdateEvent, zhnSysMon=zhnSysMon, zhnSysMonTestStopEvent=zhnSysMonTestStopEvent, zhnSysMonTestTable=zhnSysMonTestTable, zhnSysMonAlarmSetEvent=zhnSysMonAlarmSetEvent, zhnSysMonAlarmSeverity=zhnSysMonAlarmSeverity, zhnSysMonLinePowerTable=zhnSysMonLinePowerTable, zhnSysMonReadyEvent=zhnSysMonReadyEvent, zhnSysMonLinePowerRowStatus=zhnSysMonLinePowerRowStatus, zhnSysMonConfigChangeEvent=zhnSysMonConfigChangeEvent, zhnSysMonTempSensorTable=zhnSysMonTempSensorTable, zhnSysMonTempSensorCfgUpdateEvent=zhnSysMonTempSensorCfgUpdateEvent, zhnSysMonLinePowerEntry=zhnSysMonLinePowerEntry, zhnSysMonAlarmInterfaceName=zhnSysMonAlarmInterfaceName, zhnSysMonTestType=zhnSysMonTestType, zhnSysMonTestEntry=zhnSysMonTestEntry, zhnSysMonConformance=zhnSysMonConformance, zhnSysMonLinePowerLineNumber=zhnSysMonLinePowerLineNumber, zhnSysMonAlarmRowStatus=zhnSysMonAlarmRowStatus, zhnSysMonTestInterfaceName=zhnSysMonTestInterfaceName, zhnSysMonTempSensorOS=zhnSysMonTempSensorOS, zhnSysMonTempSensorName=zhnSysMonTempSensorName, zhnSysMonAlarmType=zhnSysMonAlarmType)
