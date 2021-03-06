#
# PySNMP MIB module ZYXEL-DIFFSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DIFFSERV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, Bits, Counter32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, NotificationType, Unsigned32, MibIdentifier, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Bits", "Counter32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDiffserv = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22))
if mibBuilder.loadTexts: zyxelDiffserv.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDiffserv.setOrganization('Enterprise Solution ZyXEL')
zyxelDiffservSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1))
zyDiffservState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDiffservState.setStatus('current')
zyxelDiffservMapTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2), )
if mibBuilder.loadTexts: zyxelDiffservMapTable.setStatus('current')
zyxelDiffservMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2, 1), ).setIndexNames((0, "ZYXEL-DIFFSERV-MIB", "zyDiffservMapDscp"))
if mibBuilder.loadTexts: zyxelDiffservMapEntry.setStatus('current')
zyDiffservMapDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zyDiffservMapDscp.setStatus('current')
zyDiffservMapPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDiffservMapPriority.setStatus('current')
zyxelDiffservPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 3), )
if mibBuilder.loadTexts: zyxelDiffservPortTable.setStatus('current')
zyxelDiffservPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDiffservPortEntry.setStatus('current')
zyDiffservPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 22, 1, 3, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDiffservPortState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DIFFSERV-MIB", zyxelDiffservMapTable=zyxelDiffservMapTable, zyxelDiffservPortEntry=zyxelDiffservPortEntry, PYSNMP_MODULE_ID=zyxelDiffserv, zyxelDiffservSetup=zyxelDiffservSetup, zyxelDiffserv=zyxelDiffserv, zyxelDiffservMapEntry=zyxelDiffservMapEntry, zyDiffservMapPriority=zyDiffservMapPriority, zyxelDiffservPortTable=zyxelDiffservPortTable, zyDiffservState=zyDiffservState, zyDiffservMapDscp=zyDiffservMapDscp, zyDiffservPortState=zyDiffservPortState)
