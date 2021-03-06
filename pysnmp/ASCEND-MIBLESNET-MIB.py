#
# PySNMP MIB module ASCEND-MIBLESNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBLESNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, Bits, iso, Gauge32, ModuleIdentity, IpAddress, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "iso", "Gauge32", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

miblesNetworkProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 178))
miblesNetworkProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 178, 1), )
if mibBuilder.loadTexts: miblesNetworkProfileTable.setStatus('mandatory')
miblesNetworkProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1), ).setIndexNames((0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-Shelf-o"), (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-Slot-o"), (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-Item-o"))
if mibBuilder.loadTexts: miblesNetworkProfileEntry.setStatus('mandatory')
lesNetworkProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 1), Integer32()).setLabel("lesNetworkProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lesNetworkProfile_Shelf_o.setStatus('mandatory')
lesNetworkProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 2), Integer32()).setLabel("lesNetworkProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lesNetworkProfile_Slot_o.setStatus('mandatory')
lesNetworkProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 3), Integer32()).setLabel("lesNetworkProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lesNetworkProfile_Item_o.setStatus('mandatory')
lesNetworkProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 4), DisplayString()).setLabel("lesNetworkProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_Name.setStatus('mandatory')
lesNetworkProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("lesNetworkProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PhysicalAddress_Shelf.setStatus('mandatory')
lesNetworkProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("lesNetworkProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PhysicalAddress_Slot.setStatus('mandatory')
lesNetworkProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 7), Integer32()).setLabel("lesNetworkProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
lesNetworkProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("lesNetworkProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_Enabled.setStatus('mandatory')
lesNetworkProfile_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 9), Integer32()).setLabel("lesNetworkProfile-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_NailedGroup.setStatus('mandatory')
lesNetworkProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("lesNetworkProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_Action_o.setStatus('mandatory')
miblesNetworkProfile_PotsLineConfigTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 178, 2), ).setLabel("miblesNetworkProfile-PotsLineConfigTable")
if mibBuilder.loadTexts: miblesNetworkProfile_PotsLineConfigTable.setStatus('mandatory')
miblesNetworkProfile_PotsLineConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1), ).setLabel("miblesNetworkProfile-PotsLineConfigEntry").setIndexNames((0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Shelf-o"), (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Slot-o"), (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Item-o"), (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Index-o"))
if mibBuilder.loadTexts: miblesNetworkProfile_PotsLineConfigEntry.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 1), Integer32()).setLabel("lesNetworkProfile-PotsLineConfig-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_Shelf_o.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 2), Integer32()).setLabel("lesNetworkProfile-PotsLineConfig-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_Slot_o.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 3), Integer32()).setLabel("lesNetworkProfile-PotsLineConfig-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_Item_o.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 4), Integer32()).setLabel("lesNetworkProfile-PotsLineConfig-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_Index_o.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("lesNetworkProfile-PotsLineConfig-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_Enabled.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_Mode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("groundStart", 1), ("loopStart", 2)))).setLabel("lesNetworkProfile-PotsLineConfig-Mode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_Mode.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_EncodingFormatProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 7), Integer32()).setLabel("lesNetworkProfile-PotsLineConfig-EncodingFormatProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_EncodingFormatProfile.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_FwdDisc = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("lesNetworkProfile-PotsLineConfig-FwdDisc").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_FwdDisc.setStatus('mandatory')
lesNetworkProfile_PotsLineConfig_OverRideCid = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 9), Integer32()).setLabel("lesNetworkProfile-PotsLineConfig-OverRideCid").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesNetworkProfile_PotsLineConfig_OverRideCid.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBLESNET-MIB", lesNetworkProfile_PotsLineConfig_Mode=lesNetworkProfile_PotsLineConfig_Mode, lesNetworkProfile_PotsLineConfig_FwdDisc=lesNetworkProfile_PotsLineConfig_FwdDisc, miblesNetworkProfile_PotsLineConfigEntry=miblesNetworkProfile_PotsLineConfigEntry, lesNetworkProfile_Item_o=lesNetworkProfile_Item_o, miblesNetworkProfileTable=miblesNetworkProfileTable, lesNetworkProfile_PotsLineConfig_Index_o=lesNetworkProfile_PotsLineConfig_Index_o, miblesNetworkProfileEntry=miblesNetworkProfileEntry, lesNetworkProfile_PotsLineConfig_Enabled=lesNetworkProfile_PotsLineConfig_Enabled, lesNetworkProfile_PotsLineConfig_Shelf_o=lesNetworkProfile_PotsLineConfig_Shelf_o, miblesNetworkProfile=miblesNetworkProfile, lesNetworkProfile_PotsLineConfig_Item_o=lesNetworkProfile_PotsLineConfig_Item_o, lesNetworkProfile_Enabled=lesNetworkProfile_Enabled, lesNetworkProfile_Name=lesNetworkProfile_Name, lesNetworkProfile_PotsLineConfig_Slot_o=lesNetworkProfile_PotsLineConfig_Slot_o, lesNetworkProfile_PotsLineConfig_EncodingFormatProfile=lesNetworkProfile_PotsLineConfig_EncodingFormatProfile, DisplayString=DisplayString, lesNetworkProfile_Action_o=lesNetworkProfile_Action_o, lesNetworkProfile_Shelf_o=lesNetworkProfile_Shelf_o, lesNetworkProfile_PotsLineConfig_OverRideCid=lesNetworkProfile_PotsLineConfig_OverRideCid, lesNetworkProfile_PhysicalAddress_ItemNumber=lesNetworkProfile_PhysicalAddress_ItemNumber, lesNetworkProfile_PhysicalAddress_Slot=lesNetworkProfile_PhysicalAddress_Slot, lesNetworkProfile_NailedGroup=lesNetworkProfile_NailedGroup, lesNetworkProfile_PhysicalAddress_Shelf=lesNetworkProfile_PhysicalAddress_Shelf, miblesNetworkProfile_PotsLineConfigTable=miblesNetworkProfile_PotsLineConfigTable, lesNetworkProfile_Slot_o=lesNetworkProfile_Slot_o)
