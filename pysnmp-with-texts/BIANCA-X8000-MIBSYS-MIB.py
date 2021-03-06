#
# PySNMP MIB module BIANCA-X8000-MIBSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-X8000-MIBSYS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
DisplayString, = mibBuilder.importSymbols("RFC1158-MIB", "DisplayString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, IpAddress, Gauge32, Integer32, Unsigned32, NotificationType, Bits, NotificationType, enterprises, Counter32, MibIdentifier, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "IpAddress", "Gauge32", "Integer32", "Unsigned32", "NotificationType", "Bits", "NotificationType", "enterprises", "Counter32", "MibIdentifier", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
sys = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17))
x8 = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17, 3))
sysX8Config = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1))
sysX8Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2))
sysX8ConfigPowerSupply1State = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("missing", 1), ("off", 2), ("running", 3), ("fail", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1State.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1State.setDescription('This variable shows the state of the power supply.')
sysX8ConfigPowerSupply1Temp = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1Temp.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1Temp.setDescription('This variable shows the actual power supply temperature in the unit Celsius.')
sysX8ConfigPowerSupply1TempAlarmThreshold = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 250)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1TempAlarmThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1TempAlarmThreshold.setDescription('Power supply 1 temperature threshold.')
sysX8ConfigPowerSupply1TempAlarmTrap = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("critical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1TempAlarmTrap.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply1TempAlarmTrap.setDescription('If the power supply temperature raises above the threshold, a alarm trap is generated every 60 seconds.')
sysX8ConfigPowerSupply2State = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("missing", 1), ("off", 2), ("running", 3), ("fail", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2State.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2State.setDescription('This variable show the the state of the power supply.')
sysX8ConfigPowerSupply2Temp = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2Temp.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2Temp.setDescription('This variable shows the actual power supply temperature in the unit Celsius.')
sysX8ConfigPowerSupply2TempAlarmThreshold = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 250)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2TempAlarmThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2TempAlarmThreshold.setDescription('Power supply 2 temperature threshold.')
sysX8ConfigPowerSupply2TempAlarmTrap = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("critical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2TempAlarmTrap.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigPowerSupply2TempAlarmTrap.setDescription('If the power supply temperature raises above the threshold, a alarm trap is generated every 60 seconds.')
sysX8ConfigFanControl = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("high", 2))).clone('high')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysX8ConfigFanControl.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigFanControl.setDescription("This variable defines automatic fan control. In mode 'auto' the fans are automatically adjusted depending on the current temperature. In mode 'high' all fans remain at maximum speed.")
sysX8ConfigFanVersion = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigFanVersion.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigFanVersion.setDescription('This variable shows the firmware version of the fan unit.')
sysX8ConfigFan1 = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigFan1.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigFan1.setDescription('This variable shows the current turning speed.')
sysX8ConfigFan2 = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigFan2.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigFan2.setDescription('This variable shows the current turning speed.')
sysX8ConfigFan3 = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigFan3.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigFan3.setDescription('This variable shows the current turning speed.')
sysX8ConfigFan4 = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysX8ConfigFan4.setStatus('mandatory')
if mibBuilder.loadTexts: sysX8ConfigFan4.setDescription('This variable shows the current turning speed.')
sysX8TrapPowerSupply1Missing = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,1)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply1Missing.setDescription('This trap signifies that the power supply 1 has been removed')
sysX8TrapPowerSupply1PowerOff = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,2)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply1PowerOff.setDescription('This trap signifies that the power supply 1 has no power-good signal (no power input)')
sysX8TrapPowerSupply1PowerFail = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,3)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply1PowerFail.setDescription('This trap signifies that the power supply 1 has been in the failure (bad DC output)')
sysX8TrapPowerSupply1PowerGood = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,4)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmTrap"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply1PowerGood.setDescription('This trap signifies that the power supply 1 is running (supplying power)')
sysX8TrapPowerSupply1TempCritical = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,5)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply1TempCritical.setDescription('This trap signifies that the power supply 1 temperature raises above the critical alarm-threshold')
sysX8TrapPowerSupply1TempOk = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,6)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply1TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply1TempOk.setDescription('A normal power supply 1 temperature has been restored.')
sysX8TrapPowerSupply2Missing = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,7)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply2Missing.setDescription('This trap signifies that the power supply 2 has been removed')
sysX8TrapPowerSupply2PowerOff = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,8)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply2PowerOff.setDescription('This trap signifies that the power supply 2 has no power-good signal (no power input)')
sysX8TrapPowerSupply2PowerFail = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,9)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply2PowerFail.setDescription('This trap signifies that the power supply 2 has been in the failure (bad DC output)')
sysX8TrapPowerSupply2PowerGood = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,10)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply2PowerGood.setDescription('This trap signifies that the power supply 2 is running (supplying power)')
sysX8TrapPowerSupply2TempCritical = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,11)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply2TempCritical.setDescription('This trap signifies that the power supply 2 temperature raises above the critical alarm-threshold')
sysX8TrapPowerSupply2TempOk = NotificationType((1, 3, 6, 1, 4, 1, 272, 4, 17, 3, 2) + (0,12)).setObjects(("BIANCA-X8000-MIBSYS-MIB", "sysDescr"), ("BIANCA-X8000-MIBSYS-MIB", "sysName"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2State"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2Temp"), ("BIANCA-X8000-MIBSYS-MIB", "sysX8ConfigPowerSupply2TempAlarmThreshold"))
if mibBuilder.loadTexts: sysX8TrapPowerSupply2TempOk.setDescription('A normal power supply 2 temperature has been restored.')
mibBuilder.exportSymbols("BIANCA-X8000-MIBSYS-MIB", sysX8ConfigFan2=sysX8ConfigFan2, x8=x8, bibo=bibo, sys=sys, sysX8TrapPowerSupply1TempCritical=sysX8TrapPowerSupply1TempCritical, sysX8TrapPowerSupply1PowerGood=sysX8TrapPowerSupply1PowerGood, sysX8ConfigPowerSupply2TempAlarmTrap=sysX8ConfigPowerSupply2TempAlarmTrap, sysX8TrapPowerSupply1TempOk=sysX8TrapPowerSupply1TempOk, sysX8TrapPowerSupply2TempOk=sysX8TrapPowerSupply2TempOk, bintec=bintec, sysX8ConfigFan3=sysX8ConfigFan3, sysX8ConfigPowerSupply1Temp=sysX8ConfigPowerSupply1Temp, sysX8TrapPowerSupply1Missing=sysX8TrapPowerSupply1Missing, sysX8ConfigFanControl=sysX8ConfigFanControl, sysX8TrapPowerSupply2Missing=sysX8TrapPowerSupply2Missing, sysX8Traps=sysX8Traps, sysX8ConfigPowerSupply1TempAlarmThreshold=sysX8ConfigPowerSupply1TempAlarmThreshold, sysX8TrapPowerSupply2TempCritical=sysX8TrapPowerSupply2TempCritical, sysX8TrapPowerSupply2PowerOff=sysX8TrapPowerSupply2PowerOff, sysX8ConfigFan1=sysX8ConfigFan1, sysX8ConfigFanVersion=sysX8ConfigFanVersion, sysX8ConfigFan4=sysX8ConfigFan4, sysX8TrapPowerSupply1PowerOff=sysX8TrapPowerSupply1PowerOff, sysX8TrapPowerSupply2PowerGood=sysX8TrapPowerSupply2PowerGood, sysX8ConfigPowerSupply2TempAlarmThreshold=sysX8ConfigPowerSupply2TempAlarmThreshold, sysX8ConfigPowerSupply1TempAlarmTrap=sysX8ConfigPowerSupply1TempAlarmTrap, sysX8TrapPowerSupply1PowerFail=sysX8TrapPowerSupply1PowerFail, sysX8Config=sysX8Config, sysX8ConfigPowerSupply2State=sysX8ConfigPowerSupply2State, sysX8ConfigPowerSupply2Temp=sysX8ConfigPowerSupply2Temp, sysX8TrapPowerSupply2PowerFail=sysX8TrapPowerSupply2PowerFail, sysX8ConfigPowerSupply1State=sysX8ConfigPowerSupply1State)
