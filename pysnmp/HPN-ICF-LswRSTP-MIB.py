#
# PySNMP MIB module HPN-ICF-LswRSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswRSTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
dot1dStpPortEntry, dot1dStpPort = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPortEntry", "dot1dStpPort")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, IpAddress, Bits, Integer32, MibIdentifier, ModuleIdentity, Gauge32, iso, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "IpAddress", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
hpnicfLswRstpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6))
hpnicfLswRstpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hpnicfLswRstpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswRstpMib.setOrganization('')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hpnicfLswRstpMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1))
hpnicfdot1dStpStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpStatus.setStatus('current')
hpnicfdot1dStpForceVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpForceVersion.setStatus('current')
hpnicfdot1dStpDiameter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpDiameter.setStatus('current')
hpnicfdot1dStpRootBridgeAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRootBridgeAddress.setStatus('current')
hpnicfDot1dStpBpduGuard = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 6), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dStpBpduGuard.setStatus('current')
hpnicfDot1dStpRootType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("primary", 2), ("secondary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dStpRootType.setStatus('current')
hpnicfDot1dTimeOutFactor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dTimeOutFactor.setStatus('current')
hpnicfDot1dStpPathCostStandard = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot1d-1998", 1), ("dot1t", 2), ("legacy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dStpPathCostStandard.setStatus('current')
hpnicfdot1dStpPortXTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5), )
if mibBuilder.loadTexts: hpnicfdot1dStpPortXTable.setStatus('current')
hpnicfdot1dStpPortXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1), )
dot1dStpPortEntry.registerAugmentions(("HPN-ICF-LswRSTP-MIB", "hpnicfdot1dStpPortXEntry"))
hpnicfdot1dStpPortXEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
if mibBuilder.loadTexts: hpnicfdot1dStpPortXEntry.setStatus('current')
hpnicfdot1dStpPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpPortStatus.setStatus('current')
hpnicfdot1dStpPortEdgeport = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpPortEdgeport.setStatus('current')
hpnicfdot1dStpPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forceTrue", 1), ("forceFalse", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpPortPointToPoint.setStatus('current')
hpnicfdot1dStpMcheck = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpMcheck.setStatus('current')
hpnicfdot1dStpTransLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpTransLimit.setStatus('current')
hpnicfdot1dStpRXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXStpBPDU.setStatus('current')
hpnicfdot1dStpTXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpTXStpBPDU.setStatus('current')
hpnicfdot1dStpRXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXTCNBPDU.setStatus('current')
hpnicfdot1dStpTXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpTXTCNBPDU.setStatus('current')
hpnicfdot1dStpRXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXRSTPBPDU.setStatus('current')
hpnicfdot1dStpTXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpTXRSTPBPDU.setStatus('current')
hpnicfdot1dStpClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpClearStatistics.setStatus('current')
hpnicfdot1dSetStpDefaultPortCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dSetStpDefaultPortCost.setStatus('current')
hpnicfdot1dStpRootGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 14), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpRootGuard.setStatus('current')
hpnicfdot1dStpLoopGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 15), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpLoopGuard.setStatus('current')
hpnicfdot1dStpPortBlockedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notBlock", 1), ("blockForProtocol", 2), ("blockForRootGuard", 3), ("blockForBPDUGuard", 4), ("blockForLoopGuard", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpPortBlockedReason.setStatus('current')
hpnicfdot1dStpRXTCBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXTCBPDU.setStatus('current')
hpnicfdot1dStpPortSendingBPDUType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpPortSendingBPDUType.setStatus('current')
hpnicfdot1dStpOperPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpOperPortPointToPoint.setStatus('current')
hpnicfRstpEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0))
if mibBuilder.loadTexts: hpnicfRstpEventsV2.setStatus('current')
hpnicfRstpBpduGuarded = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 1)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hpnicfRstpBpduGuarded.setStatus('current')
hpnicfRstpRootGuarded = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 2)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hpnicfRstpRootGuarded.setStatus('current')
hpnicfRstpBridgeLostRootPrimary = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 3))
if mibBuilder.loadTexts: hpnicfRstpBridgeLostRootPrimary.setStatus('current')
hpnicfRstpLoopGuarded = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 4)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hpnicfRstpLoopGuarded.setStatus('current')
hpnicfdot1dStpIgnoredVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10), )
if mibBuilder.loadTexts: hpnicfdot1dStpIgnoredVlanTable.setStatus('current')
hpnicfdot1dStpIgnoredVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10, 1), ).setIndexNames((0, "HPN-ICF-LswRSTP-MIB", "hpnicfdot1dVlan"))
if mibBuilder.loadTexts: hpnicfdot1dStpIgnoredVlanEntry.setStatus('current')
hpnicfdot1dVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dVlan.setStatus('current')
hpnicfdot1dStpIgnore = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpIgnore.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LswRSTP-MIB", hpnicfdot1dStpTXStpBPDU=hpnicfdot1dStpTXStpBPDU, hpnicfRstpBridgeLostRootPrimary=hpnicfRstpBridgeLostRootPrimary, hpnicfdot1dStpRootGuard=hpnicfdot1dStpRootGuard, hpnicfdot1dStpPortSendingBPDUType=hpnicfdot1dStpPortSendingBPDUType, hpnicfdot1dStpForceVersion=hpnicfdot1dStpForceVersion, hpnicfdot1dStpOperPortPointToPoint=hpnicfdot1dStpOperPortPointToPoint, hpnicfdot1dSetStpDefaultPortCost=hpnicfdot1dSetStpDefaultPortCost, hpnicfdot1dStpTXRSTPBPDU=hpnicfdot1dStpTXRSTPBPDU, hpnicfdot1dStpIgnoredVlanTable=hpnicfdot1dStpIgnoredVlanTable, hpnicfdot1dStpLoopGuard=hpnicfdot1dStpLoopGuard, hpnicfDot1dStpBpduGuard=hpnicfDot1dStpBpduGuard, hpnicfRstpEventsV2=hpnicfRstpEventsV2, EnabledStatus=EnabledStatus, hpnicfRstpBpduGuarded=hpnicfRstpBpduGuarded, hpnicfdot1dStpRXTCNBPDU=hpnicfdot1dStpRXTCNBPDU, hpnicfdot1dStpPortStatus=hpnicfdot1dStpPortStatus, hpnicfRstpRootGuarded=hpnicfRstpRootGuarded, hpnicfdot1dStpPortEdgeport=hpnicfdot1dStpPortEdgeport, hpnicfdot1dStpStatus=hpnicfdot1dStpStatus, hpnicfdot1dStpTXTCNBPDU=hpnicfdot1dStpTXTCNBPDU, hpnicfDot1dTimeOutFactor=hpnicfDot1dTimeOutFactor, PYSNMP_MODULE_ID=hpnicfLswRstpMib, hpnicfLswRstpMib=hpnicfLswRstpMib, hpnicfdot1dVlan=hpnicfdot1dVlan, hpnicfdot1dStpDiameter=hpnicfdot1dStpDiameter, hpnicfdot1dStpRXRSTPBPDU=hpnicfdot1dStpRXRSTPBPDU, hpnicfdot1dStpMcheck=hpnicfdot1dStpMcheck, hpnicfLswRstpMibObject=hpnicfLswRstpMibObject, hpnicfdot1dStpRootBridgeAddress=hpnicfdot1dStpRootBridgeAddress, hpnicfdot1dStpTransLimit=hpnicfdot1dStpTransLimit, hpnicfDot1dStpPathCostStandard=hpnicfDot1dStpPathCostStandard, hpnicfdot1dStpPortXTable=hpnicfdot1dStpPortXTable, hpnicfdot1dStpPortXEntry=hpnicfdot1dStpPortXEntry, hpnicfdot1dStpIgnoredVlanEntry=hpnicfdot1dStpIgnoredVlanEntry, hpnicfdot1dStpPortBlockedReason=hpnicfdot1dStpPortBlockedReason, hpnicfdot1dStpPortPointToPoint=hpnicfdot1dStpPortPointToPoint, hpnicfRstpLoopGuarded=hpnicfRstpLoopGuarded, hpnicfdot1dStpIgnore=hpnicfdot1dStpIgnore, hpnicfdot1dStpClearStatistics=hpnicfdot1dStpClearStatistics, hpnicfdot1dStpRXTCBPDU=hpnicfdot1dStpRXTCBPDU, hpnicfDot1dStpRootType=hpnicfDot1dStpRootType, hpnicfdot1dStpRXStpBPDU=hpnicfdot1dStpRXStpBPDU)
