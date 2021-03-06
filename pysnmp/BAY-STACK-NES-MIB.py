#
# PySNMP MIB module BAY-STACK-NES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-NES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:19:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, TimeTicks, Counter32, Counter64, Gauge32, IpAddress, Unsigned32, iso, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "TimeTicks", "Counter32", "Counter64", "Gauge32", "IpAddress", "Unsigned32", "iso", "ObjectIdentity", "MibIdentifier")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackNesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 34))
bayStackNesMib.setRevisions(('2014-08-22 00:00', '2009-05-19 00:00',))
if mibBuilder.loadTexts: bayStackNesMib.setLastUpdated('201408220000Z')
if mibBuilder.loadTexts: bayStackNesMib.setOrganization('Avaya')
bayStackNesNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 0))
bayStackNesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 1))
bayStackNesNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 2))
bsnesScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1))
bsnesEnergySaverEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesEnergySaverEnabled.setStatus('current')
bsnesPoePowerSavingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesPoePowerSavingEnabled.setStatus('current')
bsnesEfficiencyModeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesEfficiencyModeEnabled.setStatus('current')
bsnesEnergySaverActive = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesEnergySaverActive.setStatus('current')
bsnesScheduleTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2), )
if mibBuilder.loadTexts: bsnesScheduleTable.setStatus('current')
bsnesScheduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-NES-MIB", "bsnesScheduleDay"), (0, "BAY-STACK-NES-MIB", "bsnesScheduleHour"), (0, "BAY-STACK-NES-MIB", "bsnesScheduleMinute"))
if mibBuilder.loadTexts: bsnesScheduleEntry.setStatus('current')
bsnesScheduleDay = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7))))
if mibBuilder.loadTexts: bsnesScheduleDay.setStatus('current')
bsnesScheduleHour = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: bsnesScheduleHour.setStatus('current')
bsnesScheduleMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59)))
if mibBuilder.loadTexts: bsnesScheduleMinute.setStatus('current')
bsnesScheduleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activate", 1), ("deactivate", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsnesScheduleAction.setStatus('current')
bsnesScheduleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsnesScheduleRowStatus.setStatus('current')
bsnesInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3), )
if mibBuilder.loadTexts: bsnesInterfaceTable.setStatus('current')
bsnesInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-NES-MIB", "bsnesInterfaceIndex"))
if mibBuilder.loadTexts: bsnesInterfaceEntry.setStatus('current')
bsnesInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsnesInterfaceIndex.setStatus('current')
bsnesInterfaceEnergySaverEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesInterfaceEnergySaverEnabled.setStatus('current')
bsnesInterfaceEnergySaverPoeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsnesInterfaceEnergySaverPoeStatus.setStatus('current')
bsnesSavingsTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4), )
if mibBuilder.loadTexts: bsnesSavingsTable.setStatus('current')
bsnesSavingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1), ).setIndexNames((0, "BAY-STACK-NES-MIB", "bsnesSavingsUnitIndex"))
if mibBuilder.loadTexts: bsnesSavingsEntry.setStatus('current')
bsnesSavingsUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: bsnesSavingsUnitIndex.setStatus('current')
bsnesSavingsUnitSavings = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsnesSavingsUnitSavings.setStatus('current')
bsnesSavingsPoeSavings = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsnesSavingsPoeSavings.setStatus('current')
bsnesGloballyEnabled = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 1))
if mibBuilder.loadTexts: bsnesGloballyEnabled.setStatus('current')
bsnesGloballyDisabled = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 2))
if mibBuilder.loadTexts: bsnesGloballyDisabled.setStatus('current')
bsnesManuallyActivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 3))
if mibBuilder.loadTexts: bsnesManuallyActivated.setStatus('current')
bsnesManuallyDeactivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 4))
if mibBuilder.loadTexts: bsnesManuallyDeactivated.setStatus('current')
bsnesScheduleNotApplied = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 5))
if mibBuilder.loadTexts: bsnesScheduleNotApplied.setStatus('current')
bsnesScheduleApplied = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 6))
if mibBuilder.loadTexts: bsnesScheduleApplied.setStatus('current')
bsnesActivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 7))
if mibBuilder.loadTexts: bsnesActivated.setStatus('current')
bsnesDeactivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 8))
if mibBuilder.loadTexts: bsnesDeactivated.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-NES-MIB", bayStackNesObjects=bayStackNesObjects, bayStackNesNotifications=bayStackNesNotifications, bayStackNesMib=bayStackNesMib, bsnesScheduleRowStatus=bsnesScheduleRowStatus, bsnesSavingsPoeSavings=bsnesSavingsPoeSavings, bsnesScheduleNotApplied=bsnesScheduleNotApplied, bsnesGloballyEnabled=bsnesGloballyEnabled, bsnesSavingsUnitSavings=bsnesSavingsUnitSavings, bsnesScheduleDay=bsnesScheduleDay, bsnesScheduleTable=bsnesScheduleTable, bsnesInterfaceTable=bsnesInterfaceTable, bsnesScheduleAction=bsnesScheduleAction, bsnesActivated=bsnesActivated, bsnesScheduleHour=bsnesScheduleHour, bsnesInterfaceIndex=bsnesInterfaceIndex, bsnesScalars=bsnesScalars, PYSNMP_MODULE_ID=bayStackNesMib, bsnesEnergySaverActive=bsnesEnergySaverActive, bsnesEfficiencyModeEnabled=bsnesEfficiencyModeEnabled, bsnesInterfaceEntry=bsnesInterfaceEntry, bsnesScheduleEntry=bsnesScheduleEntry, bsnesSavingsTable=bsnesSavingsTable, bsnesSavingsUnitIndex=bsnesSavingsUnitIndex, bsnesInterfaceEnergySaverEnabled=bsnesInterfaceEnergySaverEnabled, bsnesInterfaceEnergySaverPoeStatus=bsnesInterfaceEnergySaverPoeStatus, bsnesDeactivated=bsnesDeactivated, bsnesScheduleMinute=bsnesScheduleMinute, bsnesGloballyDisabled=bsnesGloballyDisabled, bsnesManuallyDeactivated=bsnesManuallyDeactivated, bsnesScheduleApplied=bsnesScheduleApplied, bsnesPoePowerSavingEnabled=bsnesPoePowerSavingEnabled, bsnesSavingsEntry=bsnesSavingsEntry, bsnesEnergySaverEnabled=bsnesEnergySaverEnabled, bayStackNesNotificationObjects=bayStackNesNotificationObjects, bsnesManuallyActivated=bsnesManuallyActivated)
