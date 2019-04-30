#
# PySNMP MIB module TIARA-V35-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-V35-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, TimeTicks, Integer32, Counter32, NotificationType, Bits, ObjectIdentity, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "TimeTicks", "Integer32", "Counter32", "NotificationType", "Bits", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tiaraInterfaces, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraInterfaces")
tiaraV35Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3))
tiaraV35Mib.setRevisions(('1900-08-18 00:00',))
if mibBuilder.loadTexts: tiaraV35Mib.setLastUpdated('0008180000Z')
if mibBuilder.loadTexts: tiaraV35Mib.setOrganization('Tiara Networks Inc.')
v35Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3))
v35TrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 1))
v35ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1), )
if mibBuilder.loadTexts: v35ConfigTable.setStatus('current')
v35ConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1), ).setIndexNames((0, "TIARA-V35-MIB", "v35IfIndex"))
if mibBuilder.loadTexts: v35ConfigTableEntry.setStatus('current')
v35IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: v35IfIndex.setStatus('current')
v35ConfigClockRate = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000000, 8000000)).clone(8000000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v35ConfigClockRate.setStatus('current')
v35ConfigClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("line", 2))).clone('line')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v35ConfigClockSource.setStatus('current')
v35ConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dce", 1), ("dte", 2))).clone('dte')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v35ConfigMode.setStatus('current')
v35ConfigCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc16", 1), ("crc32", 2))).clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v35ConfigCRC.setStatus('current')
v35ConfigDataMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v35ConfigDataMode.setStatus('current')
v35ConfigFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: v35ConfigFlowControl.setStatus('current')
v35StatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2), )
if mibBuilder.loadTexts: v35StatsTable.setStatus('current')
v35StatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1), ).setIndexNames((0, "TIARA-V35-MIB", "v35IfIndex"))
if mibBuilder.loadTexts: v35StatsTableEntry.setStatus('current')
v35StatsAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 1), Bits().clone(namedValues=NamedValues(("v35-no-alarms", 0), ("v35-alarms-DTR", 1), ("v35-alarms-DSR", 2), ("v35-alarms-ST", 3), ("v35-alarms-CTS", 4), ("v35-alarms-RTS", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v35StatsAlarmStatus.setStatus('current')
v35StatsFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v35StatsFramesIn.setStatus('current')
v35StatsFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v35StatsFramesOut.setStatus('current')
v35StatsOctetsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v35StatsOctetsIn.setStatus('current')
v35StatsOctetsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v35StatsOctetsOut.setStatus('current')
v35StatsCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v35StatsCRCErrors.setStatus('current')
v35SlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: v35SlotNumber.setStatus('current')
v35AlarmType = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v35-alarm-DTR", 1), ("v35-alarm-DSR", 2), ("v35-alarm-ST", 3), ("v35-alarm-CTS", 4), ("v35-alarm-RTS", 5))))
if mibBuilder.loadTexts: v35AlarmType.setStatus('current')
v35AlarmOnTrap = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3) + (0,1)).setObjects(("TIARA-V35-MIB", "v35IfIndex"), ("TIARA-V35-MIB", "v35AlarmType"))
v35AlarmOffTrap = NotificationType((1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3) + (0,2)).setObjects(("TIARA-V35-MIB", "v35IfIndex"), ("TIARA-V35-MIB", "v35AlarmType"))
mibBuilder.exportSymbols("TIARA-V35-MIB", v35Traps=v35Traps, v35StatsOctetsIn=v35StatsOctetsIn, v35ConfigFlowControl=v35ConfigFlowControl, v35ConfigCRC=v35ConfigCRC, v35StatsTableEntry=v35StatsTableEntry, v35ConfigMode=v35ConfigMode, tiaraV35Mib=tiaraV35Mib, v35TrapVariables=v35TrapVariables, v35AlarmOnTrap=v35AlarmOnTrap, v35IfIndex=v35IfIndex, v35ConfigTable=v35ConfigTable, PYSNMP_MODULE_ID=tiaraV35Mib, v35StatsCRCErrors=v35StatsCRCErrors, v35ConfigClockSource=v35ConfigClockSource, v35AlarmType=v35AlarmType, v35StatsFramesOut=v35StatsFramesOut, v35SlotNumber=v35SlotNumber, v35ConfigTableEntry=v35ConfigTableEntry, v35ConfigDataMode=v35ConfigDataMode, v35ConfigClockRate=v35ConfigClockRate, v35StatsOctetsOut=v35StatsOctetsOut, v35StatsFramesIn=v35StatsFramesIn, v35AlarmOffTrap=v35AlarmOffTrap, v35StatsTable=v35StatsTable, v35StatsAlarmStatus=v35StatsAlarmStatus)