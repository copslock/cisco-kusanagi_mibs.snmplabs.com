#
# PySNMP MIB module SCTE-HMS-PS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCTE-HMS-PS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
psIdent, = mibBuilder.importSymbols("SCTE-HMS-ROOTS", "psIdent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, Unsigned32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, ModuleIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "ModuleIdentity", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
psMonitored = MibScalar((1, 3, 6, 1, 4, 1, 5591, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMonitored.setStatus('mandatory')
psDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2), )
if mibBuilder.loadTexts: psDeviceTable.setStatus('mandatory')
psDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psDeviceAddress"))
if mibBuilder.loadTexts: psDeviceEntry.setStatus('mandatory')
psDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceAddress.setStatus('mandatory')
psProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProtocolVersion.setStatus('mandatory')
psSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSoftwareVersion.setStatus('mandatory')
psDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceId.setStatus('mandatory')
psBatteries = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteries.setStatus('mandatory')
psBatteryStrings = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryStrings.setStatus('mandatory')
psTempSensors = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTempSensors.setStatus('mandatory')
psOutputs = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputs.setStatus('mandatory')
psBatteryCurrentSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryCurrentSupport.setStatus('mandatory')
psFloatCurrentSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFloatCurrentSupport.setStatus('mandatory')
psOutputVoltageSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputVoltageSupport.setStatus('mandatory')
psInputVoltageSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("binary", 2), ("analog", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputVoltageSupport.setStatus('mandatory')
psPowerSupplyTest = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerSupplyTest.setStatus('mandatory')
psMajorAlarmSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMajorAlarmSupport.setStatus('mandatory')
psMinorAlarmSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMinorAlarmSupport.setStatus('mandatory')
psTamperSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTamperSupport.setStatus('mandatory')
psBatteryVoltageSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noMonitoring", 1), ("totalString", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryVoltageSupport.setStatus('mandatory')
psOutputPowerSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputPowerSupport.setStatus('mandatory')
psOutputFrequencySupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputFrequencySupport.setStatus('mandatory')
psInputCurrentSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputCurrentSupport.setStatus('mandatory')
psInputPowerSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputPowerSupport.setStatus('mandatory')
psOutputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputVoltage.setStatus('mandatory')
psInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputVoltage.setStatus('optional')
psInverterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 1), ("lineFail", 2), ("testCycle", 3), ("testStarted", 4), ("testFailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInverterStatus.setStatus('optional')
psMajorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarm", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMajorAlarm.setStatus('optional')
psMinorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarm", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMinorAlarm.setStatus('optional')
psTamper = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("closed", 1), ("open", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTamper.setStatus('optional')
psTotalStringVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTotalStringVoltage.setStatus('optional')
psEquipmentControl = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stopTest", 1), ("startTest", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psEquipmentControl.setStatus('optional')
psPowerOut = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerOut.setStatus('optional')
psFrequencyOut = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFrequencyOut.setStatus('optional')
psRMSCurrentIn = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psRMSCurrentIn.setStatus('optional')
psPowerIn = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerIn.setStatus('optional')
psInputVoltagePresence = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lost", 1), ("ok", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputVoltagePresence.setStatus('optional')
psFrequencyIn = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fiftyHz", 1), ("sixtyHz", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFrequencyIn.setStatus('mandatory')
psStringTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3), )
if mibBuilder.loadTexts: psStringTable.setStatus('mandatory')
psStringEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psStringDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psString"))
if mibBuilder.loadTexts: psStringEntry.setStatus('mandatory')
psStringDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringDeviceAddress.setStatus('mandatory')
psString = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psString.setStatus('mandatory')
psStringChargeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringChargeCurrent.setStatus('optional')
psStringDischargeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringDischargeCurrent.setStatus('optional')
psStringFloat = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringFloat.setStatus('optional')
psBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4), )
if mibBuilder.loadTexts: psBatteryTable.setStatus('mandatory')
psBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psBatteryDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psBatteryString"), (0, "SCTE-HMS-PS-MIB", "psBattery"))
if mibBuilder.loadTexts: psBatteryEntry.setStatus('mandatory')
psBatteryDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryDeviceAddress.setStatus('mandatory')
psBatteryString = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryString.setStatus('mandatory')
psBattery = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBattery.setStatus('mandatory')
psBatteryVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryVoltage.setStatus('optional')
psOutputTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5), )
if mibBuilder.loadTexts: psOutputTable.setStatus('mandatory')
psOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psOutputDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psOutput"))
if mibBuilder.loadTexts: psOutputEntry.setStatus('mandatory')
psOutputDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputDeviceAddress.setStatus('mandatory')
psOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutput.setStatus('mandatory')
psOutputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputCurrent.setStatus('optional')
psTemperatureSensorTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6), )
if mibBuilder.loadTexts: psTemperatureSensorTable.setStatus('mandatory')
psTemperatureSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psTempDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psTemperatureSensor"))
if mibBuilder.loadTexts: psTemperatureSensorEntry.setStatus('mandatory')
psTempDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTempDeviceAddress.setStatus('mandatory')
psTemperatureSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTemperatureSensor.setStatus('mandatory')
psTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTemperature.setStatus('optional')
mibBuilder.exportSymbols("SCTE-HMS-PS-MIB", psProtocolVersion=psProtocolVersion, psInputPowerSupport=psInputPowerSupport, psStringFloat=psStringFloat, psBatteryEntry=psBatteryEntry, psTemperatureSensorTable=psTemperatureSensorTable, psFrequencyOut=psFrequencyOut, psTamper=psTamper, psTotalStringVoltage=psTotalStringVoltage, psPowerOut=psPowerOut, psSoftwareVersion=psSoftwareVersion, psPowerSupplyTest=psPowerSupplyTest, psMinorAlarmSupport=psMinorAlarmSupport, psBatteries=psBatteries, psStringDischargeCurrent=psStringDischargeCurrent, psOutputDeviceAddress=psOutputDeviceAddress, psTemperature=psTemperature, psOutputTable=psOutputTable, psOutputEntry=psOutputEntry, psBatteryVoltage=psBatteryVoltage, psTempDeviceAddress=psTempDeviceAddress, psBatteryDeviceAddress=psBatteryDeviceAddress, psOutputPowerSupport=psOutputPowerSupport, psInverterStatus=psInverterStatus, psMinorAlarm=psMinorAlarm, psMonitored=psMonitored, psString=psString, psBatteryCurrentSupport=psBatteryCurrentSupport, psBatteryTable=psBatteryTable, psTamperSupport=psTamperSupport, psDeviceEntry=psDeviceEntry, psMajorAlarmSupport=psMajorAlarmSupport, psMajorAlarm=psMajorAlarm, psStringChargeCurrent=psStringChargeCurrent, psStringTable=psStringTable, psBattery=psBattery, psDeviceId=psDeviceId, psOutputVoltage=psOutputVoltage, psInputVoltage=psInputVoltage, psOutputVoltageSupport=psOutputVoltageSupport, psPowerIn=psPowerIn, psFrequencyIn=psFrequencyIn, psOutput=psOutput, psInputVoltageSupport=psInputVoltageSupport, psFloatCurrentSupport=psFloatCurrentSupport, psTemperatureSensor=psTemperatureSensor, psStringEntry=psStringEntry, psTempSensors=psTempSensors, psBatteryStrings=psBatteryStrings, psDeviceAddress=psDeviceAddress, psDeviceTable=psDeviceTable, psBatteryVoltageSupport=psBatteryVoltageSupport, psOutputs=psOutputs, psStringDeviceAddress=psStringDeviceAddress, psOutputFrequencySupport=psOutputFrequencySupport, psTemperatureSensorEntry=psTemperatureSensorEntry, psRMSCurrentIn=psRMSCurrentIn, psInputCurrentSupport=psInputCurrentSupport, psOutputCurrent=psOutputCurrent, psBatteryString=psBatteryString, psEquipmentControl=psEquipmentControl, psInputVoltagePresence=psInputVoltagePresence)
