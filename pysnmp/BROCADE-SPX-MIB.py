#
# PySNMP MIB module BROCADE-SPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-SPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
DisplayString, = mibBuilder.importSymbols("FOUNDRY-SN-AGENT-MIB", "DisplayString")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, Integer32, Bits, Counter64, NotificationType, ObjectIdentity, iso, Unsigned32, IpAddress, TimeTicks, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Integer32", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "iso", "Unsigned32", "IpAddress", "TimeTicks", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
brcdSPXMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40))
brcdSPXMIB.setRevisions(('2015-05-12 00:00',))
if mibBuilder.loadTexts: brcdSPXMIB.setLastUpdated('201505120000Z')
if mibBuilder.loadTexts: brcdSPXMIB.setOrganization('Brocade Communications Systems, Inc')
brcdSPXGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 1))
brcdSPXTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2))
brcdSPXGlobalConfigCBState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXGlobalConfigCBState.setStatus('current')
brcdSPXGlobalConfigPEState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXGlobalConfigPEState.setStatus('current')
brcdSPXConfigUnitTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1), )
if mibBuilder.loadTexts: brcdSPXConfigUnitTable.setStatus('current')
brcdSPXConfigUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1), ).setIndexNames((0, "BROCADE-SPX-MIB", "brcdSPXConfigUnitIndex"))
if mibBuilder.loadTexts: brcdSPXConfigUnitEntry.setStatus('current')
brcdSPXConfigUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: brcdSPXConfigUnitIndex.setStatus('current')
brcdSPXConfigUnitPEName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXConfigUnitPEName.setStatus('current')
brcdSPXConfigUnitPESPXPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXConfigUnitPESPXPort1.setStatus('current')
brcdSPXConfigUnitPESPXPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXConfigUnitPESPXPort2.setStatus('current')
brcdSPXConfigUnitPESPXLag1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXConfigUnitPESPXLag1.setStatus('current')
brcdSPXConfigUnitPESPXLag2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXConfigUnitPESPXLag2.setStatus('current')
brcdSPXConfigUnitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXConfigUnitRowStatus.setStatus('current')
brcdSPXConfigUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXConfigUnitType.setStatus('current')
brcdSPXConfigUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("local", 1), ("remote", 2), ("reserved", 3), ("empty", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXConfigUnitState.setStatus('current')
brcdSPXOperUnitTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2), )
if mibBuilder.loadTexts: brcdSPXOperUnitTable.setStatus('current')
brcdSPXOperUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1), ).setIndexNames((0, "BROCADE-SPX-MIB", "brcdSPXOperUnitIndex"))
if mibBuilder.loadTexts: brcdSPXOperUnitEntry.setStatus('current')
brcdSPXOperUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: brcdSPXOperUnitIndex.setStatus('current')
brcdSPXOperUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitType.setStatus('current')
brcdSPXOperUnitRole = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("standby", 3), ("member", 4), ("standalone", 5), ("spx-pe", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitRole.setStatus('current')
brcdSPXOperUnitMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitMac.setStatus('current')
brcdSPXOperUnitPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitPriority.setStatus('current')
brcdSPXOperUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("local", 1), ("remote", 2), ("reserved", 3), ("empty", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitState.setStatus('current')
brcdSPXOperUnitDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitDescription.setStatus('current')
brcdSPXOperUnitImgVer = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitImgVer.setStatus('current')
brcdSPXOperUnitBuildlVer = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXOperUnitBuildlVer.setStatus('current')
brcdSPXCBSPXPortTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3), )
if mibBuilder.loadTexts: brcdSPXCBSPXPortTable.setStatus('current')
brcdSPXCBSPXPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1), ).setIndexNames((0, "BROCADE-SPX-MIB", "brcdSPXCBSPXPortPort"))
if mibBuilder.loadTexts: brcdSPXCBSPXPortEntry.setStatus('current')
brcdSPXCBSPXPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: brcdSPXCBSPXPortPort.setStatus('current')
brcdSPXCBSPXPortPEGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXCBSPXPortPEGroup.setStatus('current')
brcdSPXCBSPXPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXCBSPXPortRowStatus.setStatus('current')
brcdSPXCBSPXLagTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4), )
if mibBuilder.loadTexts: brcdSPXCBSPXLagTable.setStatus('current')
brcdSPXCBSPXLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1), ).setIndexNames((0, "BROCADE-SPX-MIB", "brcdSPXCBSPXLagPrimaryPort"))
if mibBuilder.loadTexts: brcdSPXCBSPXLagEntry.setStatus('current')
brcdSPXCBSPXLagPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: brcdSPXCBSPXLagPrimaryPort.setStatus('current')
brcdSPXCBSPXLagLagIflist = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXCBSPXLagLagIflist.setStatus('current')
brcdSPXCBSPXLagPEGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXCBSPXLagPEGroup.setStatus('current')
brcdSPXCBSPXLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brcdSPXCBSPXLagRowStatus.setStatus('current')
brcdSPXPEGroupTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5), )
if mibBuilder.loadTexts: brcdSPXPEGroupTable.setStatus('current')
brcdSPXPEGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1), ).setIndexNames((0, "BROCADE-SPX-MIB", "brcdSPXPEGroupCBSPXPort"))
if mibBuilder.loadTexts: brcdSPXPEGroupEntry.setStatus('current')
brcdSPXPEGroupCBSPXPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: brcdSPXPEGroupCBSPXPort.setStatus('current')
brcdSPXPEGroupPEGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXPEGroupPEGroup.setStatus('current')
brcdSPXPEGroupPEIdList = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXPEGroupPEIdList.setStatus('current')
brcdSPXPEGroupCBSPXEndPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 40, 2, 5, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSPXPEGroupCBSPXEndPort.setStatus('current')
mibBuilder.exportSymbols("BROCADE-SPX-MIB", brcdSPXCBSPXPortEntry=brcdSPXCBSPXPortEntry, brcdSPXOperUnitRole=brcdSPXOperUnitRole, brcdSPXPEGroupCBSPXPort=brcdSPXPEGroupCBSPXPort, brcdSPXMIB=brcdSPXMIB, brcdSPXConfigUnitPESPXLag2=brcdSPXConfigUnitPESPXLag2, brcdSPXCBSPXLagPEGroup=brcdSPXCBSPXLagPEGroup, brcdSPXCBSPXLagPrimaryPort=brcdSPXCBSPXLagPrimaryPort, brcdSPXPEGroupPEIdList=brcdSPXPEGroupPEIdList, brcdSPXOperUnitType=brcdSPXOperUnitType, brcdSPXGlobalConfigPEState=brcdSPXGlobalConfigPEState, brcdSPXCBSPXPortPort=brcdSPXCBSPXPortPort, brcdSPXCBSPXPortRowStatus=brcdSPXCBSPXPortRowStatus, brcdSPXConfigUnitRowStatus=brcdSPXConfigUnitRowStatus, brcdSPXPEGroupEntry=brcdSPXPEGroupEntry, brcdSPXCBSPXLagTable=brcdSPXCBSPXLagTable, brcdSPXConfigUnitState=brcdSPXConfigUnitState, brcdSPXOperUnitDescription=brcdSPXOperUnitDescription, brcdSPXOperUnitBuildlVer=brcdSPXOperUnitBuildlVer, brcdSPXCBSPXPortPEGroup=brcdSPXCBSPXPortPEGroup, brcdSPXOperUnitMac=brcdSPXOperUnitMac, PYSNMP_MODULE_ID=brcdSPXMIB, brcdSPXOperUnitImgVer=brcdSPXOperUnitImgVer, brcdSPXConfigUnitEntry=brcdSPXConfigUnitEntry, brcdSPXConfigUnitPESPXPort2=brcdSPXConfigUnitPESPXPort2, brcdSPXConfigUnitPEName=brcdSPXConfigUnitPEName, brcdSPXConfigUnitIndex=brcdSPXConfigUnitIndex, brcdSPXOperUnitState=brcdSPXOperUnitState, brcdSPXConfigUnitPESPXPort1=brcdSPXConfigUnitPESPXPort1, brcdSPXConfigUnitTable=brcdSPXConfigUnitTable, brcdSPXOperUnitEntry=brcdSPXOperUnitEntry, brcdSPXOperUnitPriority=brcdSPXOperUnitPriority, brcdSPXGlobalObjects=brcdSPXGlobalObjects, brcdSPXOperUnitTable=brcdSPXOperUnitTable, brcdSPXPEGroupPEGroup=brcdSPXPEGroupPEGroup, brcdSPXCBSPXLagLagIflist=brcdSPXCBSPXLagLagIflist, brcdSPXCBSPXLagRowStatus=brcdSPXCBSPXLagRowStatus, brcdSPXOperUnitIndex=brcdSPXOperUnitIndex, brcdSPXConfigUnitType=brcdSPXConfigUnitType, brcdSPXPEGroupTable=brcdSPXPEGroupTable, brcdSPXPEGroupCBSPXEndPort=brcdSPXPEGroupCBSPXEndPort, brcdSPXCBSPXLagEntry=brcdSPXCBSPXLagEntry, brcdSPXConfigUnitPESPXLag1=brcdSPXConfigUnitPESPXLag1, brcdSPXGlobalConfigCBState=brcdSPXGlobalConfigCBState, brcdSPXTableObjects=brcdSPXTableObjects, brcdSPXCBSPXPortTable=brcdSPXCBSPXPortTable)
