#
# PySNMP MIB module ASCEND-MIBVDSLNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBVDSLNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Integer32, Bits, TimeTicks, ObjectIdentity, Unsigned32, iso, NotificationType, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Integer32", "Bits", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibvdslNetworkProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 9))
mibvdslNetworkProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 9, 1), )
if mibBuilder.loadTexts: mibvdslNetworkProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibvdslNetworkProfileTable.setDescription('A list of mibvdslNetworkProfile profile entries.')
mibvdslNetworkProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1), ).setIndexNames((0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Shelf-o"), (0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Slot-o"), (0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Item-o"))
if mibBuilder.loadTexts: mibvdslNetworkProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibvdslNetworkProfileEntry.setDescription('A mibvdslNetworkProfile entry containing objects that maps to the parameters of mibvdslNetworkProfile profile.')
vdslNetworkProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 1), Integer32()).setLabel("vdslNetworkProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslNetworkProfile_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_Shelf_o.setDescription('')
vdslNetworkProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 2), Integer32()).setLabel("vdslNetworkProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslNetworkProfile_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_Slot_o.setDescription('')
vdslNetworkProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 3), Integer32()).setLabel("vdslNetworkProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslNetworkProfile_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_Item_o.setDescription('')
vdslNetworkProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 4), DisplayString()).setLabel("vdslNetworkProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_Name.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_Name.setDescription('For future use. The current design does not use the name field but instead references Vdsl lines by the physical address; we may in the future support referencing Vdsl lines by name as well as by address. The name consists of a null terminated ascii string supplied by the user; it defaults to the ascii form of the Vdsl line physical address.')
vdslNetworkProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("vdslNetworkProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
vdslNetworkProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("vdslNetworkProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
vdslNetworkProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 13), Integer32()).setLabel("vdslNetworkProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
vdslNetworkProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("vdslNetworkProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_Enabled.setDescription('TRUE if the line is enabled, otherwise FALSE.')
vdslNetworkProfile_SparingMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("manual", 2), ("automatic", 3)))).setLabel("vdslNetworkProfile-SparingMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_SparingMode.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_SparingMode.setDescription('Port sparing operational mode for this port.')
vdslNetworkProfile_IgnoreLineup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("systemDefined", 1), ("no", 2), ("yes", 3)))).setLabel("vdslNetworkProfile-IgnoreLineup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_IgnoreLineup.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_IgnoreLineup.setDescription('Ignore line up value for this port.')
vdslNetworkProfile_LineConfig_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 19), Integer32()).setLabel("vdslNetworkProfile-LineConfig-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_NailedGroup.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_NailedGroup.setDescription('A number that identifies the this unique physical DSL line.')
vdslNetworkProfile_LineConfig_VpSwitchingVpi = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 20), Integer32()).setLabel("vdslNetworkProfile-LineConfig-VpSwitchingVpi").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_VpSwitchingVpi.setDescription('The Vpi to be used for the VP switching. Rest of the VPIs within valid vpi-vci-range will be used for the VC switching. Changes in this range will take effect immediately. THE USER SHOULD BE VERY CAREFUL WHILE CHANGING THIS VALUE BECAUSE ALL CONNECTIONS ON THE LIM WHERE THIS PORT BELONGS WILL BE DROPPED IN ORDER TO MAKE THIS NEW VALUE EFFECTIVE IMMEDIATELY.')
vdslNetworkProfile_LineConfig_UpStreamFixedRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("n-1206667", 1), ("n-965333", 2), ("n-1930667", 3), ("n-3861333", 4)))).setLabel("vdslNetworkProfile-LineConfig-UpStreamFixedRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_UpStreamFixedRate.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_UpStreamFixedRate.setDescription('The following Up/Down stream rate relationships are supported: (0.965Mbps/19.306Mbps); (1.930Mbps/11.463Mbps); (3.861Mbps/11.463Mbps); (3.861Mbps/15.626Mbps). Up Stream range: 0.965Mbps - 3.861Mbps.')
vdslNetworkProfile_LineConfig_DownStreamFixedRate = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("n-1206667", 1), ("n-11463333", 2), ("n-15626333", 3), ("n-19306667", 4)))).setLabel("vdslNetworkProfile-LineConfig-DownStreamFixedRate").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_DownStreamFixedRate.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_DownStreamFixedRate.setDescription('The following Up/Down stream rate relationships are supported: (0.965Mbps/19.306Mbps); (1.930Mbps/11.463Mbps); (3.861Mbps/11.463Mbps); (3.861Mbps/15.626Mbps). Down Stream range: 11.463Mbps - 15.626Mbps.')
vdslNetworkProfile_LineConfig_ConfigLoopback = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("digital", 2), ("analog", 3)))).setLabel("vdslNetworkProfile-LineConfig-ConfigLoopback").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_ConfigLoopback.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_ConfigLoopback.setDescription('Configuration of different modem loopbacks.')
vdslNetworkProfile_LineConfig_PsdValue = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("n-53dbm", 1), ("n-60dbm", 2)))).setLabel("vdslNetworkProfile-LineConfig-PsdValue").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_PsdValue.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_PsdValue.setDescription('Configuration of PSD parameter. It defines the power that is allowed to be sent to the line.')
vdslNetworkProfile_LineConfig_LinkStatecmd = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("autoConnectCmd", 16), ("disconnectState", 1), ("connectState", 2), ("quietState", 3), ("idleReqState", 4), ("backToServState", 5), ("changeIdleParamState", 6), ("changeWarmStartParamState", 7), ("changeCurrentParamState", 8)))).setLabel("vdslNetworkProfile-LineConfig-LinkStatecmd").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_LinkStatecmd.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_LineConfig_LinkStatecmd.setDescription('Sets the link connect state. Use this to control status of the VDSL link connect state machine. The auto-connect-cmd will train modem up to the final service. All the other commands are used to manualy operate the VDSL link connect state machine.')
vdslNetworkProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("vdslNetworkProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: vdslNetworkProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: vdslNetworkProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBVDSLNET-MIB", vdslNetworkProfile_Slot_o=vdslNetworkProfile_Slot_o, vdslNetworkProfile_Name=vdslNetworkProfile_Name, vdslNetworkProfile_LineConfig_LinkStatecmd=vdslNetworkProfile_LineConfig_LinkStatecmd, vdslNetworkProfile_LineConfig_VpSwitchingVpi=vdslNetworkProfile_LineConfig_VpSwitchingVpi, vdslNetworkProfile_PhysicalAddress_Slot=vdslNetworkProfile_PhysicalAddress_Slot, vdslNetworkProfile_PhysicalAddress_Shelf=vdslNetworkProfile_PhysicalAddress_Shelf, mibvdslNetworkProfileTable=mibvdslNetworkProfileTable, vdslNetworkProfile_IgnoreLineup=vdslNetworkProfile_IgnoreLineup, vdslNetworkProfile_SparingMode=vdslNetworkProfile_SparingMode, vdslNetworkProfile_PhysicalAddress_ItemNumber=vdslNetworkProfile_PhysicalAddress_ItemNumber, vdslNetworkProfile_LineConfig_PsdValue=vdslNetworkProfile_LineConfig_PsdValue, vdslNetworkProfile_LineConfig_DownStreamFixedRate=vdslNetworkProfile_LineConfig_DownStreamFixedRate, vdslNetworkProfile_Enabled=vdslNetworkProfile_Enabled, vdslNetworkProfile_LineConfig_NailedGroup=vdslNetworkProfile_LineConfig_NailedGroup, DisplayString=DisplayString, vdslNetworkProfile_Action_o=vdslNetworkProfile_Action_o, vdslNetworkProfile_Shelf_o=vdslNetworkProfile_Shelf_o, mibvdslNetworkProfile=mibvdslNetworkProfile, mibvdslNetworkProfileEntry=mibvdslNetworkProfileEntry, vdslNetworkProfile_Item_o=vdslNetworkProfile_Item_o, vdslNetworkProfile_LineConfig_UpStreamFixedRate=vdslNetworkProfile_LineConfig_UpStreamFixedRate, vdslNetworkProfile_LineConfig_ConfigLoopback=vdslNetworkProfile_LineConfig_ConfigLoopback)
