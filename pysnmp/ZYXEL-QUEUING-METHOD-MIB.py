#
# PySNMP MIB module ZYXEL-QUEUING-METHOD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-QUEUING-METHOD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Unsigned32, Counter32, ModuleIdentity, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, NotificationType, Bits, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "Counter32", "ModuleIdentity", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "NotificationType", "Bits", "TimeTicks", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelQueuingMethod = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70))
if mibBuilder.loadTexts: zyxelQueuingMethod.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelQueuingMethod.setOrganization('Enterprise Solution ZyXEL')
zyxelQueuingMethodSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1))
zyxelQueuingMethodPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1), )
if mibBuilder.loadTexts: zyxelQueuingMethodPortTable.setStatus('current')
zyxelQueuingMethodPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "ZYXEL-QUEUING-METHOD-MIB", "zyQueuingMethodPortQueue"))
if mibBuilder.loadTexts: zyxelQueuingMethodPortEntry.setStatus('current')
zyQueuingMethodPortQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyQueuingMethodPortQueue.setStatus('current')
zyQueuingMethodPortWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyQueuingMethodPortWeight.setStatus('current')
zyQueuingMethodPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("strictlyPriority", 0), ("weightedFairScheduling", 1), ("weightedRoundRobin", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyQueuingMethodPortMode.setStatus('current')
zyxelQueuingMethodHybridSpqPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 2), )
if mibBuilder.loadTexts: zyxelQueuingMethodHybridSpqPortTable.setStatus('current')
zyxelQueuingMethodHybridSpqPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelQueuingMethodHybridSpqPortEntry.setStatus('current')
zyQueuingMethodHybridSpqPortQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("q0", 1), ("q1", 2), ("q2", 3), ("q3", 4), ("q4", 5), ("q5", 6), ("q6", 7), ("q7", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyQueuingMethodHybridSpqPortQueue.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-QUEUING-METHOD-MIB", zyxelQueuingMethodPortTable=zyxelQueuingMethodPortTable, zyxelQueuingMethod=zyxelQueuingMethod, zyxelQueuingMethodPortEntry=zyxelQueuingMethodPortEntry, zyxelQueuingMethodHybridSpqPortEntry=zyxelQueuingMethodHybridSpqPortEntry, zyQueuingMethodPortQueue=zyQueuingMethodPortQueue, zyQueuingMethodPortWeight=zyQueuingMethodPortWeight, zyQueuingMethodPortMode=zyQueuingMethodPortMode, zyxelQueuingMethodHybridSpqPortTable=zyxelQueuingMethodHybridSpqPortTable, PYSNMP_MODULE_ID=zyxelQueuingMethod, zyQueuingMethodHybridSpqPortQueue=zyQueuingMethodHybridSpqPortQueue, zyxelQueuingMethodSetup=zyxelQueuingMethodSetup)
