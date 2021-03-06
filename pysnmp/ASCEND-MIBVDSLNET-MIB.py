#
# PySNMP MIB module ASCEND-MIBVDSLNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBVDSLNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Integer32, iso, IpAddress, Gauge32, Counter64, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Integer32", "iso", "IpAddress", "Gauge32", "Counter64", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibvdslNetworkProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 9))
mibvdslNetworkProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 9, 1), )
if mibBuilder.loadTexts: mibvdslNetworkProfileTable.setStatus('mandatory')
mibvdslNetworkProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1), ).setIndexNames((0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Shelf-o"), (0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Slot-o"), (0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Item-o"))
if mibBuilder.loadTexts: mibvdslNetworkProfileEntry.setStatus('mandatory')
vdslNetworkProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 1), Integer32()).setLabel("vdslNetworkProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslNetworkProfile_Shelf_o.setStatus('mandatory')
vdslNetworkProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 2), Integer32()).setLabel("vdslNetworkProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslNetworkProfile_Slot_o.setStatus('mandatory')
vdslNetworkProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 3), Integer32()).setLabel("vdslNetworkProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslNetworkProfile_Item_o.setStatus('mandatory')
vdslNetworkProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 4), DisplayString()).setLabel("vdslNetworkProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_Name.setStatus('mandatory')
vdslNetworkProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("vdslNetworkProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_Shelf.setStatus('mandatory')
vdslNetworkProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("vdslNetworkProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_Slot.setStatus('mandatory')
vdslNetworkProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 13), Integer32()).setLabel("vdslNetworkProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
vdslNetworkProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("vdslNetworkProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_Enabled.setStatus('mandatory')
vdslNetworkProfile_SparingMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("manual", 2), ("automatic", 3)))).setLabel("vdslNetworkProfile-SparingMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_SparingMode.setStatus('mandatory')
vdslNetworkProfile_IgnoreLineup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("systemDefined", 1), ("no", 2), ("yes", 3)))).setLabel("vdslNetworkProfile-IgnoreLineup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_IgnoreLineup.setStatus('mandatory')
vdslNetworkProfile_LineConfig_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 19), Integer32()).setLabel("vdslNetworkProfile-LineConfig-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_NailedGroup.setStatus('mandatory')
vdslNetworkProfile_LineConfig_VpSwitchingVpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 20), Integer32()).setLabel("vdslNetworkProfile-LineConfig-VpSwitchingVpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus('mandatory')
vdslNetworkProfile_LineConfig_UpStreamFixedRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("n-1206667", 1), ("n-965333", 2), ("n-1930667", 3), ("n-3861333", 4)))).setLabel("vdslNetworkProfile-LineConfig-UpStreamFixedRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_UpStreamFixedRate.setStatus('mandatory')
vdslNetworkProfile_LineConfig_DownStreamFixedRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("n-1206667", 1), ("n-11463333", 2), ("n-15626333", 3), ("n-19306667", 4)))).setLabel("vdslNetworkProfile-LineConfig-DownStreamFixedRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_DownStreamFixedRate.setStatus('mandatory')
vdslNetworkProfile_LineConfig_ConfigLoopback = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("digital", 2), ("analog", 3)))).setLabel("vdslNetworkProfile-LineConfig-ConfigLoopback").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_ConfigLoopback.setStatus('mandatory')
vdslNetworkProfile_LineConfig_PsdValue = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("n-53dbm", 1), ("n-60dbm", 2)))).setLabel("vdslNetworkProfile-LineConfig-PsdValue").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_PsdValue.setStatus('mandatory')
vdslNetworkProfile_LineConfig_LinkStatecmd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("autoConnectCmd", 16), ("disconnectState", 1), ("connectState", 2), ("quietState", 3), ("idleReqState", 4), ("backToServState", 5), ("changeIdleParamState", 6), ("changeWarmStartParamState", 7), ("changeCurrentParamState", 8)))).setLabel("vdslNetworkProfile-LineConfig-LinkStatecmd").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_LinkStatecmd.setStatus('mandatory')
vdslNetworkProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("vdslNetworkProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBVDSLNET-MIB", mibvdslNetworkProfileEntry=mibvdslNetworkProfileEntry, vdslNetworkProfile_LineConfig_UpStreamFixedRate=vdslNetworkProfile_LineConfig_UpStreamFixedRate, vdslNetworkProfile_Action_o=vdslNetworkProfile_Action_o, vdslNetworkProfile_SparingMode=vdslNetworkProfile_SparingMode, DisplayString=DisplayString, vdslNetworkProfile_Shelf_o=vdslNetworkProfile_Shelf_o, vdslNetworkProfile_PhysicalAddress_Slot=vdslNetworkProfile_PhysicalAddress_Slot, mibvdslNetworkProfile=mibvdslNetworkProfile, vdslNetworkProfile_Enabled=vdslNetworkProfile_Enabled, vdslNetworkProfile_IgnoreLineup=vdslNetworkProfile_IgnoreLineup, vdslNetworkProfile_LineConfig_PsdValue=vdslNetworkProfile_LineConfig_PsdValue, mibvdslNetworkProfileTable=mibvdslNetworkProfileTable, vdslNetworkProfile_Item_o=vdslNetworkProfile_Item_o, vdslNetworkProfile_PhysicalAddress_ItemNumber=vdslNetworkProfile_PhysicalAddress_ItemNumber, vdslNetworkProfile_Name=vdslNetworkProfile_Name, vdslNetworkProfile_Slot_o=vdslNetworkProfile_Slot_o, vdslNetworkProfile_PhysicalAddress_Shelf=vdslNetworkProfile_PhysicalAddress_Shelf, vdslNetworkProfile_LineConfig_VpSwitchingVpi=vdslNetworkProfile_LineConfig_VpSwitchingVpi, vdslNetworkProfile_LineConfig_ConfigLoopback=vdslNetworkProfile_LineConfig_ConfigLoopback, vdslNetworkProfile_LineConfig_NailedGroup=vdslNetworkProfile_LineConfig_NailedGroup, vdslNetworkProfile_LineConfig_LinkStatecmd=vdslNetworkProfile_LineConfig_LinkStatecmd, vdslNetworkProfile_LineConfig_DownStreamFixedRate=vdslNetworkProfile_LineConfig_DownStreamFixedRate)
