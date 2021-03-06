#
# PySNMP MIB module BAY-STACK-SOURCE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-SOURCE-GUARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:19:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, TimeTicks, NotificationType, ModuleIdentity, Counter32, Integer32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter32", "Integer32", "Gauge32", "IpAddress")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackSourceGuardMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 20))
bayStackSourceGuardMib.setRevisions(('2008-10-30 00:00', '2008-03-31 00:00', '2007-05-07 00:00', '2007-03-23 00:00',))
if mibBuilder.loadTexts: bayStackSourceGuardMib.setLastUpdated('200810300000Z')
if mibBuilder.loadTexts: bayStackSourceGuardMib.setOrganization('Nortel Ltd.')
bsSourceGuardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 20, 0))
bsSourceGuardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 20, 1))
bsSourceGuardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1), )
if mibBuilder.loadTexts: bsSourceGuardConfigTable.setStatus('current')
bsSourceGuardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigIfIndex"))
if mibBuilder.loadTexts: bsSourceGuardConfigEntry.setStatus('current')
bsSourceGuardConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsSourceGuardConfigIfIndex.setStatus('current')
bsSourceGuardConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("ip", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsSourceGuardConfigMode.setStatus('current')
bsSourceGuardAddrTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2), )
if mibBuilder.loadTexts: bsSourceGuardAddrTable.setStatus('current')
bsSourceGuardAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrIndex"), (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrType"), (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrAddress"), (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrMACAddr"))
if mibBuilder.loadTexts: bsSourceGuardAddrEntry.setStatus('current')
bsSourceGuardAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsSourceGuardAddrIndex.setStatus('current')
bsSourceGuardAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: bsSourceGuardAddrType.setStatus('current')
bsSourceGuardAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: bsSourceGuardAddrAddress.setStatus('current')
bsSourceGuardAddrMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 4), MacAddress())
if mibBuilder.loadTexts: bsSourceGuardAddrMACAddr.setStatus('current')
bsSourceGuardAddrSource = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dhcpSnooping", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsSourceGuardAddrSource.setStatus('current')
bsSourceGuardStatsTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3), )
if mibBuilder.loadTexts: bsSourceGuardStatsTable.setStatus('current')
bsSourceGuardStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardStatsIfIndex"))
if mibBuilder.loadTexts: bsSourceGuardStatsEntry.setStatus('current')
bsSourceGuardStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsSourceGuardStatsIfIndex.setStatus('current')
bsSourceGuardStatsDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsSourceGuardStatsDroppedPackets.setStatus('current')
bsSourceGuardReachedMaxIpEntries = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 20, 0, 1)).setObjects(("BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigMode"))
if mibBuilder.loadTexts: bsSourceGuardReachedMaxIpEntries.setStatus('current')
bsSourceGuardCannotEnablePort = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 20, 0, 2)).setObjects(("BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigMode"))
if mibBuilder.loadTexts: bsSourceGuardCannotEnablePort.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-SOURCE-GUARD-MIB", bsSourceGuardConfigTable=bsSourceGuardConfigTable, bsSourceGuardAddrEntry=bsSourceGuardAddrEntry, bsSourceGuardCannotEnablePort=bsSourceGuardCannotEnablePort, bsSourceGuardAddrMACAddr=bsSourceGuardAddrMACAddr, bsSourceGuardAddrTable=bsSourceGuardAddrTable, bsSourceGuardAddrType=bsSourceGuardAddrType, bsSourceGuardAddrSource=bsSourceGuardAddrSource, bsSourceGuardStatsIfIndex=bsSourceGuardStatsIfIndex, bsSourceGuardNotifications=bsSourceGuardNotifications, bsSourceGuardStatsDroppedPackets=bsSourceGuardStatsDroppedPackets, PYSNMP_MODULE_ID=bayStackSourceGuardMib, bayStackSourceGuardMib=bayStackSourceGuardMib, bsSourceGuardAddrAddress=bsSourceGuardAddrAddress, bsSourceGuardAddrIndex=bsSourceGuardAddrIndex, bsSourceGuardReachedMaxIpEntries=bsSourceGuardReachedMaxIpEntries, bsSourceGuardConfigIfIndex=bsSourceGuardConfigIfIndex, bsSourceGuardConfigMode=bsSourceGuardConfigMode, bsSourceGuardStatsTable=bsSourceGuardStatsTable, bsSourceGuardStatsEntry=bsSourceGuardStatsEntry, bsSourceGuardObjects=bsSourceGuardObjects, bsSourceGuardConfigEntry=bsSourceGuardConfigEntry)
