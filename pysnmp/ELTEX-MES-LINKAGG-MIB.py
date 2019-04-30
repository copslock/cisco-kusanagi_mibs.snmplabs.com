#
# PySNMP MIB module ELTEX-MES-LINKAGG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-LINKAGG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
eltMesLinkAgg, = mibBuilder.importSymbols("ELTEX-MES", "eltMesLinkAgg")
dot3adAggPortEntry, = mibBuilder.importSymbols("IEEE8023-LAG-MIB", "dot3adAggPortEntry")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rlDot3adAggBalanceEntry, = mibBuilder.importSymbols("RADLAN-TRUNK-MIB", "rlDot3adAggBalanceEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter64, Gauge32, ObjectIdentity, iso, NotificationType, Counter32, MibIdentifier, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "iso", "NotificationType", "Counter32", "MibIdentifier", "Integer32", "Bits")
TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
eltMesLagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1))
if mibBuilder.loadTexts: eltMesLagMIB.setLastUpdated('201408310000Z')
if mibBuilder.loadTexts: eltMesLagMIB.setOrganization('Eltex Ltd.')
eltMesLagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1))
eltMesLinkAggGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 1))
eltMesLinkAggPort = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2))
eltAggPortTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 1), )
if mibBuilder.loadTexts: eltAggPortTable.setStatus('current')
eltAggPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 1, 1), )
dot3adAggPortEntry.registerAugmentions(("ELTEX-MES-LINKAGG-MIB", "eltAggPortEntry"))
eltAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
if mibBuilder.loadTexts: eltAggPortEntry.setStatus('current')
eltAggPortPassive = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltAggPortPassive.setStatus('current')
eltAggBalanceTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 2), )
if mibBuilder.loadTexts: eltAggBalanceTable.setStatus('current')
eltAggBalanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 2, 1), )
rlDot3adAggBalanceEntry.registerAugmentions(("ELTEX-MES-LINKAGG-MIB", "eltAggBalanceEntry"))
eltAggBalanceEntry.setIndexNames(*rlDot3adAggBalanceEntry.getIndexNames())
if mibBuilder.loadTexts: eltAggBalanceEntry.setStatus('current')
eltAggBalanceMplsAware = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltAggBalanceMplsAware.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-LINKAGG-MIB", eltMesLagMIBObjects=eltMesLagMIBObjects, eltAggBalanceMplsAware=eltAggBalanceMplsAware, eltAggBalanceTable=eltAggBalanceTable, eltMesLinkAggPort=eltMesLinkAggPort, eltAggPortTable=eltAggPortTable, eltAggPortPassive=eltAggPortPassive, eltAggBalanceEntry=eltAggBalanceEntry, eltAggPortEntry=eltAggPortEntry, eltMesLinkAggGlobal=eltMesLinkAggGlobal, eltMesLagMIB=eltMesLagMIB, PYSNMP_MODULE_ID=eltMesLagMIB)