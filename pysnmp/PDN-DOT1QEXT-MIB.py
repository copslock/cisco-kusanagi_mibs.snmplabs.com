#
# PySNMP MIB module PDN-DOT1QEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DOT1QEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_dot1q, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-dot1q")
TblCmd, = mibBuilder.importSymbols("PDN-TC", "TblCmd")
dot1qVlanStaticEntry, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStaticEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Gauge32, ModuleIdentity, Bits, IpAddress, iso, TimeTicks, Counter32, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Gauge32", "ModuleIdentity", "Bits", "IpAddress", "iso", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnDot1qExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1))
pdnDot1qExt.setRevisions(('2005-07-26 00:00', '2003-11-12 00:00', '2002-11-30 00:00',))
if mibBuilder.loadTexts: pdnDot1qExt.setLastUpdated('200507260000Z')
if mibBuilder.loadTexts: pdnDot1qExt.setOrganization('Paradyne Corp MIB Working Group')
pdnDot1qExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1))
pdnDot1qVlanStaticExtTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1), )
if mibBuilder.loadTexts: pdnDot1qVlanStaticExtTable.setStatus('current')
pdnDot1qVlanStaticExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticExtEntry"))
pdnDot1qVlanStaticExtEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: pdnDot1qVlanStaticExtEntry.setStatus('current')
pdnDot1qVlanStaticSecureModeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1qVlanStaticSecureModeStatus.setStatus('current')
pdnDot1qVlanStaticProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1qVlanStaticProxyArpStatus.setStatus('current')
pdnDot1qVlanStaticUplink = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1qVlanStaticUplink.setStatus('current')
pdnDot1qVlanStaticDefaultNHR = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1qVlanStaticDefaultNHR.setStatus('current')
pdnDot1qVlanStaticOuterTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1qVlanStaticOuterTag.setStatus('current')
pdnDot1qVlanStaticOuterDefaultPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1qVlanStaticOuterDefaultPriority.setStatus('current')
pdnDot1qVlanStaticOuterEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(33024)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1qVlanStaticOuterEthertype.setStatus('current')
pdnDot1BasePortPIWGTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2), )
if mibBuilder.loadTexts: pdnDot1BasePortPIWGTable.setStatus('current')
pdnDot1BasePortPIWGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-DOT1QEXT-MIB", "pdnDot1BasePort"))
if mibBuilder.loadTexts: pdnDot1BasePortPIWGEntry.setStatus('current')
pdnDot1BasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: pdnDot1BasePort.setStatus('current')
pdnDot1BasePortPIWGId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDot1BasePortPIWGId.setStatus('current')
pdnDot1BasePortPIWGCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDot1BasePortPIWGCircuit.setStatus('current')
pdnDot1TpFdbClear = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 3), TblCmd()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDot1TpFdbClear.setStatus('current')
pdnDot1qExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2))
pdnDot1qExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1))
pdnDot1qExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 2))
pdnDot1qExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 2, 1)).setObjects(("PDN-DOT1QEXT-MIB", "pdnDot1qVlanExtGroup"), ("PDN-DOT1QEXT-MIB", "pdnDot1BasePortPIWGGroup"), ("PDN-DOT1QEXT-MIB", "pdnDot1GeneralGroup"), ("PDN-DOT1QEXT-MIB", "pdnDot1dVlanStackingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDot1qExtCompliance = pdnDot1qExtCompliance.setStatus('current')
pdnDot1qVlanExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 1)).setObjects(("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticSecureModeStatus"), ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticProxyArpStatus"), ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticUplink"), ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticDefaultNHR"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDot1qVlanExtGroup = pdnDot1qVlanExtGroup.setStatus('current')
pdnDot1BasePortPIWGGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 2)).setObjects(("PDN-DOT1QEXT-MIB", "pdnDot1BasePortPIWGId"), ("PDN-DOT1QEXT-MIB", "pdnDot1BasePortPIWGCircuit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDot1BasePortPIWGGroup = pdnDot1BasePortPIWGGroup.setStatus('current')
pdnDot1GeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 3)).setObjects(("PDN-DOT1QEXT-MIB", "pdnDot1TpFdbClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDot1GeneralGroup = pdnDot1GeneralGroup.setStatus('current')
pdnDot1dVlanStackingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 4)).setObjects(("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticOuterTag"), ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticOuterDefaultPriority"), ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticOuterEthertype"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDot1dVlanStackingGroup = pdnDot1dVlanStackingGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-DOT1QEXT-MIB", pdnDot1BasePortPIWGGroup=pdnDot1BasePortPIWGGroup, pdnDot1BasePortPIWGEntry=pdnDot1BasePortPIWGEntry, pdnDot1qVlanStaticUplink=pdnDot1qVlanStaticUplink, pdnDot1BasePortPIWGTable=pdnDot1BasePortPIWGTable, PYSNMP_MODULE_ID=pdnDot1qExt, pdnDot1BasePort=pdnDot1BasePort, pdnDot1qExtGroups=pdnDot1qExtGroups, pdnDot1qExtCompliance=pdnDot1qExtCompliance, pdnDot1dVlanStackingGroup=pdnDot1dVlanStackingGroup, pdnDot1qExt=pdnDot1qExt, pdnDot1qVlanStaticExtTable=pdnDot1qVlanStaticExtTable, pdnDot1qVlanStaticOuterDefaultPriority=pdnDot1qVlanStaticOuterDefaultPriority, pdnDot1BasePortPIWGId=pdnDot1BasePortPIWGId, pdnDot1GeneralGroup=pdnDot1GeneralGroup, pdnDot1qExtObjects=pdnDot1qExtObjects, pdnDot1qExtConformance=pdnDot1qExtConformance, pdnDot1qVlanStaticOuterTag=pdnDot1qVlanStaticOuterTag, pdnDot1qVlanStaticOuterEthertype=pdnDot1qVlanStaticOuterEthertype, pdnDot1qVlanStaticProxyArpStatus=pdnDot1qVlanStaticProxyArpStatus, pdnDot1BasePortPIWGCircuit=pdnDot1BasePortPIWGCircuit, pdnDot1TpFdbClear=pdnDot1TpFdbClear, pdnDot1qVlanExtGroup=pdnDot1qVlanExtGroup, pdnDot1qVlanStaticDefaultNHR=pdnDot1qVlanStaticDefaultNHR, pdnDot1qVlanStaticExtEntry=pdnDot1qVlanStaticExtEntry, pdnDot1qExtCompliances=pdnDot1qExtCompliances, pdnDot1qVlanStaticSecureModeStatus=pdnDot1qVlanStaticSecureModeStatus)
