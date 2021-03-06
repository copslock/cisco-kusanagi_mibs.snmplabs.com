#
# PySNMP MIB module FASTPATH-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-INVENTORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, NotificationType, Integer32, TimeTicks, Gauge32, IpAddress, ModuleIdentity, MibIdentifier, Counter64, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "TimeTicks", "Gauge32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter64", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
fastPathInventory = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13))
fastPathInventory.setRevisions(('2007-05-23 00:00', '2004-10-28 20:37', '2003-05-26 19:30',))
if mibBuilder.loadTexts: fastPathInventory.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathInventory.setOrganization('Broadcom Corporation')
class AgentInventoryUnitPreference(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("unsassigned", 1), ("assigned", 2))

class AgentInventoryUnitType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

class AgentInventoryCardType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

agentInventoryStackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1))
agentInventoryStackReplicateSTK = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackReplicateSTK.setStatus('current')
agentInventoryStackReload = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackReload.setStatus('current')
agentInventoryStackMaxUnitNumber = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackMaxUnitNumber.setStatus('current')
agentInventoryStackReplicateSTKStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("notInProgress", 2), ("finishedWithSuccess", 3), ("finishedWithError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackReplicateSTKStatus.setStatus('current')
agentInventoryStackSTKname = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unconfigured", 1), ("image1", 2), ("image2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackSTKname.setStatus('current')
agentInventoryStackActivateSTK = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackActivateSTK.setStatus('current')
agentInventoryStackDeleteSTK = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackDeleteSTK.setStatus('current')
agentInventoryUnitGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2))
agentInventorySupportedUnitTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 1), )
if mibBuilder.loadTexts: agentInventorySupportedUnitTable.setStatus('current')
agentInventorySupportedUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 1, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventorySupportedUnitIndex"))
if mibBuilder.loadTexts: agentInventorySupportedUnitEntry.setStatus('current')
agentInventorySupportedUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: agentInventorySupportedUnitIndex.setStatus('current')
agentInventorySupportedUnitModelIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySupportedUnitModelIdentifier.setStatus('current')
agentInventorySupportedUnitDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySupportedUnitDescription.setStatus('current')
agentInventorySupportedUnitExpectedCodeVer = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySupportedUnitExpectedCodeVer.setStatus('current')
agentInventoryUnitTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2), )
if mibBuilder.loadTexts: agentInventoryUnitTable.setStatus('current')
agentInventoryUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventoryUnitNumber"))
if mibBuilder.loadTexts: agentInventoryUnitEntry.setStatus('current')
agentInventoryUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryUnitNumber.setStatus('current')
agentInventoryUnitAssignNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitAssignNumber.setStatus('current')
agentInventoryUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 3), AgentInventoryUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitType.setStatus('current')
agentInventoryUnitSupportedUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitSupportedUnitIndex.setStatus('current')
agentInventoryUnitMgmtAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mgmtUnit", 1), ("stackUnit", 2), ("mgmtUnassigned", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitMgmtAdmin.setStatus('current')
agentInventoryUnitHWMgmtPref = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 7), AgentInventoryUnitPreference()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitHWMgmtPref.setStatus('current')
agentInventoryUnitHWMgmtPrefValue = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitHWMgmtPrefValue.setStatus('current')
agentInventoryUnitAdminMgmtPref = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 9), AgentInventoryUnitPreference()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitAdminMgmtPref.setStatus('current')
agentInventoryUnitAdminMgmtPrefValue = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitAdminMgmtPrefValue.setStatus('current')
agentInventoryUnitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ok", 1), ("unsupported", 2), ("codeMismatch", 3), ("configMismatch", 4), ("notPresent", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitStatus.setStatus('current')
agentInventoryUnitDetectedCodeVer = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitDetectedCodeVer.setStatus('current')
agentInventoryUnitDetectedCodeInFlashVer = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitDetectedCodeInFlashVer.setStatus('current')
agentInventoryUnitUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitUpTime.setStatus('current')
agentInventoryUnitDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitDescription.setStatus('current')
agentInventoryUnitReplicateSTK = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitReplicateSTK.setStatus('current')
agentInventoryUnitReload = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitReload.setStatus('current')
agentInventoryUnitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitRowStatus.setStatus('current')
agentInventoryUnitSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitSerialNumber.setStatus('current')
agentInventoryUnitImage1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitImage1Version.setStatus('current')
agentInventoryUnitImage2Version = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitImage2Version.setStatus('current')
agentInventoryUnitSTKname = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("image1", 2), ("image2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitSTKname.setStatus('current')
agentInventoryUnitActivateSTK = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitActivateSTK.setStatus('current')
agentInventoryUnitDeleteSTK = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitDeleteSTK.setStatus('current')
agentInventoryUnitReplicateSTKStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("notInProgress", 2), ("finishedWithSuccess", 3), ("finishedWithError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitReplicateSTKStatus.setStatus('current')
agentInventoryUnitStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 2, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unassigned", 1), ("standby-opr", 2), ("standby-cfg", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitStandby.setStatus('current')
agentInventorySlotGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3))
agentInventorySlotTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1), )
if mibBuilder.loadTexts: agentInventorySlotTable.setStatus('current')
agentInventorySlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventoryUnitNumber"), (0, "FASTPATH-INVENTORY-MIB", "agentInventorySlotNumber"))
if mibBuilder.loadTexts: agentInventorySlotEntry.setStatus('current')
agentInventorySlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventorySlotNumber.setStatus('current')
agentInventorySlotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("empty", 1), ("full", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySlotStatus.setStatus('current')
agentInventorySlotPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySlotPowerMode.setStatus('current')
agentInventorySlotAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySlotAdminMode.setStatus('current')
agentInventorySlotInsertedCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1, 6), AgentInventoryCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySlotInsertedCardType.setStatus('current')
agentInventorySlotConfiguredCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1, 7), AgentInventoryCardType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySlotConfiguredCardType.setStatus('current')
agentInventorySlotCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 3, 1, 1, 8), Bits().clone(namedValues=NamedValues(("pluggable", 0), ("power-down", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySlotCapabilities.setStatus('current')
agentInventoryCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 4))
agentInventoryCardTypeTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 4, 1), )
if mibBuilder.loadTexts: agentInventoryCardTypeTable.setStatus('current')
agentInventoryCardTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 4, 1, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventoryCardIndex"))
if mibBuilder.loadTexts: agentInventoryCardTypeEntry.setStatus('current')
agentInventoryCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 4, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryCardIndex.setStatus('current')
agentInventoryCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 4, 1, 1, 2), AgentInventoryCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardType.setStatus('current')
agentInventoryCardModelIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardModelIdentifier.setStatus('current')
agentInventoryCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardDescription.setStatus('current')
agentInventoryComponentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 5))
agentInventoryComponentTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 5, 1), )
if mibBuilder.loadTexts: agentInventoryComponentTable.setStatus('current')
agentInventoryComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 5, 1, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventoryComponentIndex"))
if mibBuilder.loadTexts: agentInventoryComponentEntry.setStatus('current')
agentInventoryComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 5, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryComponentIndex.setStatus('current')
agentInventoryComponentMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentMnemonic.setStatus('current')
agentInventoryComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 5, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentName.setStatus('current')
agentInventoryStackPortGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7))
agentInventoryStackPortIpTelephonyQOSSupport = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackPortIpTelephonyQOSSupport.setStatus('current')
agentInventoryStackPortTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2), )
if mibBuilder.loadTexts: agentInventoryStackPortTable.setStatus('current')
agentInventoryStackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventoryStackPortIndex"))
if mibBuilder.loadTexts: agentInventoryStackPortEntry.setStatus('current')
agentInventoryStackPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryStackPortIndex.setStatus('current')
agentInventoryStackPortUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortUnit.setStatus('current')
agentInventoryStackPortTag = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortTag.setStatus('current')
agentInventoryStackPortConfiguredStackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stack", 1), ("ethernet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackPortConfiguredStackMode.setStatus('current')
agentInventoryStackPortRunningStackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stack", 1), ("ethernet", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortRunningStackMode.setStatus('current')
agentInventoryStackPortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortLinkStatus.setStatus('current')
agentInventoryStackPortLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortLinkSpeed.setStatus('current')
agentInventoryStackPortDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortDataRate.setStatus('current')
agentInventoryStackPortErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortErrorRate.setStatus('current')
agentInventoryStackPortTotalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 7, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortTotalErrors.setStatus('current')
agentInventoryTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 0))
agentInventoryCardMismatch = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 0, 1)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventoryUnitNumber"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotNumber"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotInsertedCardType"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotConfiguredCardType"))
if mibBuilder.loadTexts: agentInventoryCardMismatch.setStatus('current')
agentInventoryCardUnsupported = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 0, 2)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventoryUnitNumber"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotNumber"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotInsertedCardType"))
if mibBuilder.loadTexts: agentInventoryCardUnsupported.setStatus('current')
agentInventoryStackPortLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 0, 3)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventoryStackPortUnit"), ("FASTPATH-INVENTORY-MIB", "agentInventoryStackPortTag"))
if mibBuilder.loadTexts: agentInventoryStackPortLinkUp.setStatus('current')
agentInventoryStackPortLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 0, 4)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventoryStackPortUnit"), ("FASTPATH-INVENTORY-MIB", "agentInventoryStackPortTag"))
if mibBuilder.loadTexts: agentInventoryStackPortLinkDown.setStatus('current')
fastPathInventoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6))
fastPathInventoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 1))
fastPathInventoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 2))
fastPathInventoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 1, 1)).setObjects(("FASTPATH-INVENTORY-MIB", "fastPathInventorySlotGroup"), ("FASTPATH-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("FASTPATH-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("FASTPATH-INVENTORY-MIB", "fastPathInventoryUnitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryCompliance = fastPathInventoryCompliance.setStatus('obsolete')
fastPathInventoryCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 1, 2)).setObjects(("FASTPATH-INVENTORY-MIB", "fastPathInventorySlotGroup"), ("FASTPATH-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("FASTPATH-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("FASTPATH-INVENTORY-MIB", "fastPathInventoryUnitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryCompliance2 = fastPathInventoryCompliance2.setStatus('current')
fastPathInventorySupportedUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 2, 1)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventorySupportedUnitIndex"), ("FASTPATH-INVENTORY-MIB", "agentInventorySupportedUnitModelIdentifier"), ("FASTPATH-INVENTORY-MIB", "agentInventorySupportedUnitDescription"), ("FASTPATH-INVENTORY-MIB", "agentInventorySupportedUnitExpectedCodeVer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventorySupportedUnitGroup = fastPathInventorySupportedUnitGroup.setStatus('current')
fastPathInventoryUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 2, 2)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventoryUnitNumber"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitAssignNumber"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitType"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitMgmtAdmin"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitHWMgmtPref"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitAdminMgmtPref"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitStatus"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitDetectedCodeVer"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitDetectedCodeInFlashVer"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitUpTime"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitDescription"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitReplicateSTK"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitRowStatus"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitImage1Version"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitImage2Version"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitSTKname"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitActivateSTK"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitDeleteSTK"), ("FASTPATH-INVENTORY-MIB", "agentInventoryUnitSTKname"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryUnitGroup = fastPathInventoryUnitGroup.setStatus('current')
fastPathInventorySlotGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 2, 3)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventorySlotNumber"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotStatus"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotPowerMode"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotAdminMode"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotInsertedCardType"), ("FASTPATH-INVENTORY-MIB", "agentInventorySlotConfiguredCardType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventorySlotGroup = fastPathInventorySlotGroup.setStatus('current')
fastPathInventoryCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 2, 4)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventoryCardIndex"), ("FASTPATH-INVENTORY-MIB", "agentInventoryCardType"), ("FASTPATH-INVENTORY-MIB", "agentInventoryCardModelIdentifier"), ("FASTPATH-INVENTORY-MIB", "agentInventoryCardDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryCardGroup = fastPathInventoryCardGroup.setStatus('current')
fastPathInventoryNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 13, 6, 2, 5)).setObjects(("FASTPATH-INVENTORY-MIB", "agentInventoryCardMismatch"), ("FASTPATH-INVENTORY-MIB", "agentInventoryCardUnsupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryNotificationsGroup = fastPathInventoryNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-INVENTORY-MIB", fastPathInventoryCompliance2=fastPathInventoryCompliance2, agentInventoryCardUnsupported=agentInventoryCardUnsupported, agentInventoryStackPortConfiguredStackMode=agentInventoryStackPortConfiguredStackMode, agentInventoryStackMaxUnitNumber=agentInventoryStackMaxUnitNumber, agentInventorySlotGroup=agentInventorySlotGroup, agentInventorySlotNumber=agentInventorySlotNumber, agentInventoryCardMismatch=agentInventoryCardMismatch, agentInventoryUnitType=agentInventoryUnitType, agentInventoryStackPortLinkSpeed=agentInventoryStackPortLinkSpeed, agentInventorySlotTable=agentInventorySlotTable, agentInventoryUnitHWMgmtPrefValue=agentInventoryUnitHWMgmtPrefValue, PYSNMP_MODULE_ID=fastPathInventory, AgentInventoryUnitPreference=AgentInventoryUnitPreference, agentInventoryStackPortErrorRate=agentInventoryStackPortErrorRate, agentInventorySupportedUnitEntry=agentInventorySupportedUnitEntry, fastPathInventoryGroups=fastPathInventoryGroups, agentInventoryUnitNumber=agentInventoryUnitNumber, agentInventoryUnitMgmtAdmin=agentInventoryUnitMgmtAdmin, agentInventoryStackPortLinkDown=agentInventoryStackPortLinkDown, agentInventoryCardType=agentInventoryCardType, agentInventoryStackReload=agentInventoryStackReload, agentInventoryUnitTable=agentInventoryUnitTable, agentInventorySlotConfiguredCardType=agentInventorySlotConfiguredCardType, agentInventoryUnitAdminMgmtPrefValue=agentInventoryUnitAdminMgmtPrefValue, fastPathInventory=fastPathInventory, agentInventoryTraps=agentInventoryTraps, agentInventoryComponentEntry=agentInventoryComponentEntry, agentInventoryUnitStandby=agentInventoryUnitStandby, agentInventorySupportedUnitDescription=agentInventorySupportedUnitDescription, fastPathInventoryCardGroup=fastPathInventoryCardGroup, agentInventoryUnitStatus=agentInventoryUnitStatus, agentInventoryStackPortIndex=agentInventoryStackPortIndex, agentInventoryUnitSTKname=agentInventoryUnitSTKname, agentInventoryUnitAssignNumber=agentInventoryUnitAssignNumber, agentInventoryUnitRowStatus=agentInventoryUnitRowStatus, agentInventoryStackSTKname=agentInventoryStackSTKname, agentInventoryUnitSerialNumber=agentInventoryUnitSerialNumber, agentInventoryUnitUpTime=agentInventoryUnitUpTime, agentInventoryStackPortTag=agentInventoryStackPortTag, agentInventoryCardTypeEntry=agentInventoryCardTypeEntry, agentInventoryUnitImage2Version=agentInventoryUnitImage2Version, agentInventoryUnitEntry=agentInventoryUnitEntry, agentInventoryUnitReplicateSTKStatus=agentInventoryUnitReplicateSTKStatus, fastPathInventoryConformance=fastPathInventoryConformance, agentInventoryUnitSupportedUnitIndex=agentInventoryUnitSupportedUnitIndex, agentInventoryStackPortGroup=agentInventoryStackPortGroup, agentInventoryStackReplicateSTK=agentInventoryStackReplicateSTK, fastPathInventoryCompliance=fastPathInventoryCompliance, agentInventoryStackActivateSTK=agentInventoryStackActivateSTK, agentInventoryStackPortLinkStatus=agentInventoryStackPortLinkStatus, agentInventoryCardModelIdentifier=agentInventoryCardModelIdentifier, agentInventoryUnitDescription=agentInventoryUnitDescription, agentInventoryUnitDetectedCodeVer=agentInventoryUnitDetectedCodeVer, agentInventoryStackPortTable=agentInventoryStackPortTable, agentInventoryStackPortDataRate=agentInventoryStackPortDataRate, agentInventorySupportedUnitExpectedCodeVer=agentInventorySupportedUnitExpectedCodeVer, agentInventoryCardDescription=agentInventoryCardDescription, agentInventoryCardIndex=agentInventoryCardIndex, agentInventoryUnitAdminMgmtPref=agentInventoryUnitAdminMgmtPref, agentInventoryComponentName=agentInventoryComponentName, agentInventoryStackReplicateSTKStatus=agentInventoryStackReplicateSTKStatus, AgentInventoryCardType=AgentInventoryCardType, fastPathInventoryCompliances=fastPathInventoryCompliances, agentInventoryStackPortRunningStackMode=agentInventoryStackPortRunningStackMode, agentInventoryStackPortTotalErrors=agentInventoryStackPortTotalErrors, agentInventoryCardTypeTable=agentInventoryCardTypeTable, agentInventoryStackPortLinkUp=agentInventoryStackPortLinkUp, agentInventorySupportedUnitTable=agentInventorySupportedUnitTable, agentInventoryStackPortEntry=agentInventoryStackPortEntry, agentInventoryComponentGroup=agentInventoryComponentGroup, agentInventorySupportedUnitModelIdentifier=agentInventorySupportedUnitModelIdentifier, agentInventoryComponentIndex=agentInventoryComponentIndex, agentInventoryComponentTable=agentInventoryComponentTable, agentInventoryComponentMnemonic=agentInventoryComponentMnemonic, agentInventoryUnitHWMgmtPref=agentInventoryUnitHWMgmtPref, fastPathInventoryUnitGroup=fastPathInventoryUnitGroup, agentInventorySlotCapabilities=agentInventorySlotCapabilities, agentInventoryStackPortUnit=agentInventoryStackPortUnit, agentInventoryCardGroup=agentInventoryCardGroup, agentInventorySlotAdminMode=agentInventorySlotAdminMode, agentInventoryStackDeleteSTK=agentInventoryStackDeleteSTK, fastPathInventorySlotGroup=fastPathInventorySlotGroup, agentInventoryStackPortIpTelephonyQOSSupport=agentInventoryStackPortIpTelephonyQOSSupport, agentInventoryStackGroup=agentInventoryStackGroup, agentInventoryUnitImage1Version=agentInventoryUnitImage1Version, AgentInventoryUnitType=AgentInventoryUnitType, agentInventorySupportedUnitIndex=agentInventorySupportedUnitIndex, agentInventorySlotEntry=agentInventorySlotEntry, agentInventoryUnitDetectedCodeInFlashVer=agentInventoryUnitDetectedCodeInFlashVer, agentInventoryUnitActivateSTK=agentInventoryUnitActivateSTK, agentInventorySlotStatus=agentInventorySlotStatus, fastPathInventorySupportedUnitGroup=fastPathInventorySupportedUnitGroup, agentInventorySlotInsertedCardType=agentInventorySlotInsertedCardType, fastPathInventoryNotificationsGroup=fastPathInventoryNotificationsGroup, agentInventoryUnitReload=agentInventoryUnitReload, agentInventoryUnitDeleteSTK=agentInventoryUnitDeleteSTK, agentInventorySlotPowerMode=agentInventorySlotPowerMode, agentInventoryUnitReplicateSTK=agentInventoryUnitReplicateSTK, agentInventoryUnitGroup=agentInventoryUnitGroup)
