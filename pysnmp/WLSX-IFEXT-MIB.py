#
# PySNMP MIB module WLSX-IFEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WLSX-IFEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:29:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ArubaPoeState, ArubaPortSpeed, ArubaPortDuplex, ArubaDot1dState, ArubaPortMode, ArubaIfType, ArubaOperStateValue, ArubaVlanValidRange, ArubaEnableValue, ArubaPortType = mibBuilder.importSymbols("ARUBA-TC", "ArubaPoeState", "ArubaPortSpeed", "ArubaPortDuplex", "ArubaDot1dState", "ArubaPortMode", "ArubaIfType", "ArubaOperStateValue", "ArubaVlanValidRange", "ArubaEnableValue", "ArubaPortType")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, iso, Integer32, Unsigned32, MibIdentifier, Gauge32, Bits, snmpModules, ModuleIdentity, TimeTicks, ObjectIdentity, Counter32, TextualConvention, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "Bits", "snmpModules", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter32", "TextualConvention", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64")
TestAndIncr, TimeInterval, RowStatus, DisplayString, PhysAddress, TAddress, TruthValue, MacAddress, TextualConvention, StorageType, TDomain = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "TimeInterval", "RowStatus", "DisplayString", "PhysAddress", "TAddress", "TruthValue", "MacAddress", "TextualConvention", "StorageType", "TDomain")
wlsxIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3))
wlsxIfExtMIB.setRevisions(('2012-07-12 00:00', '1910-01-26 18:06',))
if mibBuilder.loadTexts: wlsxIfExtMIB.setLastUpdated('201207120000Z')
if mibBuilder.loadTexts: wlsxIfExtMIB.setOrganization('Aruba Wireless Networks')
wlsxIfExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1))
wlsxIfExtPortTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1), )
if mibBuilder.loadTexts: wlsxIfExtPortTable.setStatus('deprecated')
wlsxIfExtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtSlotNumber"), (0, "WLSX-IFEXT-MIB", "ifExtPortNumber"))
if mibBuilder.loadTexts: wlsxIfExtPortEntry.setStatus('deprecated')
ifExtSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ifExtSlotNumber.setStatus('deprecated')
ifExtPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: ifExtPortNumber.setStatus('deprecated')
ifExtPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortIfIndex.setStatus('deprecated')
ifExtAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 4), ArubaEnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtAdminState.setStatus('deprecated')
ifExtOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtOperState.setStatus('deprecated')
ifExtPoeState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 6), ArubaPoeState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtPoeState.setStatus('deprecated')
ifExtIsTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsTrusted.setStatus('deprecated')
ifExtDot1DState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 8), ArubaDot1dState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtDot1DState.setStatus('deprecated')
ifExtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 9), ArubaPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtMode.setStatus('deprecated')
ifExtAccessVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 10), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtAccessVlanId.setStatus('deprecated')
ifExtTrunkNativeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 11), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkNativeVlanId.setStatus('deprecated')
ifExtTrunkIsAllowedAll = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkIsAllowedAll.setStatus('deprecated')
ifExtTrunkAllowedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkAllowedVlanList.setStatus('deprecated')
ifExtIngressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIngressACLName.setStatus('deprecated')
ifExtEgressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtEgressACLName.setStatus('deprecated')
ifExtSessionACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtSessionACLName.setStatus('deprecated')
ifExtXsecVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 17), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtXsecVlan.setStatus('deprecated')
ifExtIsMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsMonitoring.setStatus('deprecated')
ifExtIsMux = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsMux.setStatus('deprecated')
ifExtUserSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserSlotNumber.setStatus('deprecated')
ifExtUserPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserPortNumber.setStatus('deprecated')
ifExtPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 22), ArubaPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortSpeed.setStatus('deprecated')
ifExtPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 23), ArubaPortDuplex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortDuplex.setStatus('deprecated')
ifExtPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 24), ArubaPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortType.setStatus('deprecated')
ifExtDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtDescr.setStatus('deprecated')
ifExtUserModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserModuleNumber.setStatus('deprecated')
wlsxIfExtVlanTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2), )
if mibBuilder.loadTexts: wlsxIfExtVlanTable.setStatus('current')
wlsxIfExtVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"))
if mibBuilder.loadTexts: wlsxIfExtVlanEntry.setStatus('current')
ifExtVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 1), ArubaVlanValidRange())
if mibBuilder.loadTexts: ifExtVlanId.setStatus('current')
ifExtVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanName.setStatus('current')
ifExtVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanStatus.setStatus('current')
wlsxIfExtVlanMemberTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3), )
if mibBuilder.loadTexts: wlsxIfExtVlanMemberTable.setStatus('current')
wlsxIfExtVlanMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: wlsxIfExtVlanMemberEntry.setStatus('current')
ifExtVlanMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanMemberStatus.setStatus('current')
ifExtVlanMemberSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberSlot.setStatus('current')
ifExtVlanMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberPort.setStatus('current')
ifExtVlanMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 4), ArubaIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberType.setStatus('current')
wlsxIfExtVlanInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4), )
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceTable.setStatus('current')
wlsxIfExtVlanInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"))
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceEntry.setStatus('current')
ifExtVlanInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIfIndex.setStatus('current')
ifExtVlanInterfaceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceDescription.setStatus('current')
ifExtVlanInterfaceBWContract = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceBWContract.setStatus('current')
ifExtVlanInterfaceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 4), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceAdminState.setStatus('current')
ifExtVlanInterfaceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 5), ArubaOperStateValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceOperState.setStatus('current')
ifExtVlanInterfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpAddress.setStatus('current')
ifExtVlanInterfaceIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpMask.setStatus('current')
ifExtVlanInterfaceIsLocalArp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 8), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIsLocalArp.setStatus('current')
ifExtVlanInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceStatus.setStatus('current')
ifExtVlanInterfaceIpRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 10), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpRouting.setStatus('current')
ifExtVlanInterfaceIpNatInside = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 11), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpNatInside.setStatus('current')
ifExtVlanInterfaceIpIgmpSnooping = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 12), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpIgmpSnooping.setStatus('current')
wlsxIfExtNPortTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5), )
if mibBuilder.loadTexts: wlsxIfExtNPortTable.setStatus('current')
wlsxIfExtNPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtNSlotNumber"), (0, "WLSX-IFEXT-MIB", "ifExtNModuleNumber"), (0, "WLSX-IFEXT-MIB", "ifExtNPortNumber"))
if mibBuilder.loadTexts: wlsxIfExtNPortEntry.setStatus('current')
ifExtNSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: ifExtNSlotNumber.setStatus('current')
ifExtNModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: ifExtNModuleNumber.setStatus('current')
ifExtNPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: ifExtNPortNumber.setStatus('current')
ifExtNPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortIfIndex.setStatus('current')
ifExtNAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 5), ArubaEnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNAdminState.setStatus('current')
ifExtNOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNOperState.setStatus('current')
ifExtNPoeState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 7), ArubaPoeState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNPoeState.setStatus('current')
ifExtNIsTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsTrusted.setStatus('current')
ifExtNDot1DState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 9), ArubaDot1dState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNDot1DState.setStatus('current')
ifExtNMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 10), ArubaPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNMode.setStatus('current')
ifExtNAccessVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 11), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNAccessVlanId.setStatus('current')
ifExtNTrunkNativeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 12), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkNativeVlanId.setStatus('current')
ifExtNTrunkIsAllowedAll = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkIsAllowedAll.setStatus('current')
ifExtNTrunkAllowedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkAllowedVlanList.setStatus('current')
ifExtNIngressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIngressACLName.setStatus('current')
ifExtNEgressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNEgressACLName.setStatus('current')
ifExtNSessionACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNSessionACLName.setStatus('current')
ifExtNXsecVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 18), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNXsecVlan.setStatus('current')
ifExtNIsMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsMonitoring.setStatus('current')
ifExtNIsMux = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsMux.setStatus('current')
ifExtNPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 21), ArubaPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortSpeed.setStatus('current')
ifExtNPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 22), ArubaPortDuplex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortDuplex.setStatus('current')
ifExtNPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 23), ArubaPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortType.setStatus('current')
ifExtNDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNDescr.setStatus('current')
mibBuilder.exportSymbols("WLSX-IFEXT-MIB", ifExtNDescr=ifExtNDescr, wlsxIfExtVlanEntry=wlsxIfExtVlanEntry, ifExtVlanMemberPort=ifExtVlanMemberPort, ifExtAccessVlanId=ifExtAccessVlanId, ifExtSessionACLName=ifExtSessionACLName, ifExtVlanMemberType=ifExtVlanMemberType, wlsxIfExtVlanMemberTable=wlsxIfExtVlanMemberTable, ifExtTrunkNativeVlanId=ifExtTrunkNativeVlanId, ifExtMode=ifExtMode, wlsxIfExtGroup=wlsxIfExtGroup, ifExtNAccessVlanId=ifExtNAccessVlanId, ifExtVlanInterfaceIpRouting=ifExtVlanInterfaceIpRouting, ifExtNMode=ifExtNMode, ifExtVlanStatus=ifExtVlanStatus, ifExtNXsecVlan=ifExtNXsecVlan, ifExtUserModuleNumber=ifExtUserModuleNumber, ifExtUserSlotNumber=ifExtUserSlotNumber, ifExtNTrunkNativeVlanId=ifExtNTrunkNativeVlanId, ifExtNPortNumber=ifExtNPortNumber, ifExtSlotNumber=ifExtSlotNumber, wlsxIfExtPortEntry=wlsxIfExtPortEntry, ifExtDot1DState=ifExtDot1DState, ifExtVlanInterfaceDescription=ifExtVlanInterfaceDescription, ifExtVlanName=ifExtVlanName, ifExtVlanId=ifExtVlanId, ifExtXsecVlan=ifExtXsecVlan, ifExtDescr=ifExtDescr, ifExtVlanInterfaceIsLocalArp=ifExtVlanInterfaceIsLocalArp, ifExtPortNumber=ifExtPortNumber, wlsxIfExtNPortEntry=wlsxIfExtNPortEntry, ifExtNIsMonitoring=ifExtNIsMonitoring, wlsxIfExtVlanInterfaceTable=wlsxIfExtVlanInterfaceTable, ifExtEgressACLName=ifExtEgressACLName, ifExtNPortType=ifExtNPortType, ifExtVlanInterfaceOperState=ifExtVlanInterfaceOperState, wlsxIfExtMIB=wlsxIfExtMIB, wlsxIfExtVlanTable=wlsxIfExtVlanTable, PYSNMP_MODULE_ID=wlsxIfExtMIB, ifExtNPortDuplex=ifExtNPortDuplex, ifExtVlanInterfaceIpAddress=ifExtVlanInterfaceIpAddress, ifExtNPortSpeed=ifExtNPortSpeed, ifExtIngressACLName=ifExtIngressACLName, ifExtVlanInterfaceIpMask=ifExtVlanInterfaceIpMask, ifExtNDot1DState=ifExtNDot1DState, ifExtVlanInterfaceIpNatInside=ifExtVlanInterfaceIpNatInside, ifExtIsTrusted=ifExtIsTrusted, ifExtOperState=ifExtOperState, ifExtNModuleNumber=ifExtNModuleNumber, ifExtPortType=ifExtPortType, ifExtNPoeState=ifExtNPoeState, ifExtNIsTrusted=ifExtNIsTrusted, ifExtUserPortNumber=ifExtUserPortNumber, ifExtVlanInterfaceIfIndex=ifExtVlanInterfaceIfIndex, ifExtVlanMemberSlot=ifExtVlanMemberSlot, ifExtIsMonitoring=ifExtIsMonitoring, ifExtNIngressACLName=ifExtNIngressACLName, ifExtNAdminState=ifExtNAdminState, ifExtPortDuplex=ifExtPortDuplex, ifExtTrunkIsAllowedAll=ifExtTrunkIsAllowedAll, ifExtPortSpeed=ifExtPortSpeed, ifExtNEgressACLName=ifExtNEgressACLName, ifExtVlanInterfaceIpIgmpSnooping=ifExtVlanInterfaceIpIgmpSnooping, ifExtNSlotNumber=ifExtNSlotNumber, wlsxIfExtNPortTable=wlsxIfExtNPortTable, ifExtTrunkAllowedVlanList=ifExtTrunkAllowedVlanList, ifExtVlanInterfaceStatus=ifExtVlanInterfaceStatus, ifExtNSessionACLName=ifExtNSessionACLName, ifExtNTrunkIsAllowedAll=ifExtNTrunkIsAllowedAll, ifExtNOperState=ifExtNOperState, ifExtAdminState=ifExtAdminState, ifExtPoeState=ifExtPoeState, ifExtNIsMux=ifExtNIsMux, ifExtVlanInterfaceBWContract=ifExtVlanInterfaceBWContract, wlsxIfExtVlanInterfaceEntry=wlsxIfExtVlanInterfaceEntry, wlsxIfExtPortTable=wlsxIfExtPortTable, ifExtPortIfIndex=ifExtPortIfIndex, ifExtNPortIfIndex=ifExtNPortIfIndex, ifExtVlanMemberStatus=ifExtVlanMemberStatus, ifExtNTrunkAllowedVlanList=ifExtNTrunkAllowedVlanList, ifExtVlanInterfaceAdminState=ifExtVlanInterfaceAdminState, ifExtIsMux=ifExtIsMux, wlsxIfExtVlanMemberEntry=wlsxIfExtVlanMemberEntry)