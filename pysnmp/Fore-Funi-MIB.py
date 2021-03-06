#
# PySNMP MIB module Fore-Funi-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Funi-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
frameInternetworking, = mibBuilder.importSymbols("Fore-Common-MIB", "frameInternetworking")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Unsigned32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, iso, Integer32, MibIdentifier, NotificationType, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Unsigned32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "iso", "Integer32", "MibIdentifier", "NotificationType", "Gauge32", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
funi = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 16, 6))
if mibBuilder.loadTexts: funi.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: funi.setOrganization('FORE')
funiConnTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1), )
if mibBuilder.loadTexts: funiConnTable.setStatus('current')
funiConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1), ).setIndexNames((0, "Fore-Funi-MIB", "funiConnFuniServiceIfIndex"), (0, "Fore-Funi-MIB", "funiConnFuniVpi"), (0, "Fore-Funi-MIB", "funiConnFuniVci"))
if mibBuilder.loadTexts: funiConnEntry.setStatus('current')
funiConnFuniServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiConnFuniServiceIfIndex.setStatus('current')
funiConnFuniVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiConnFuniVpi.setStatus('current')
funiConnFuniVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiConnFuniVci.setStatus('current')
funiConnFabricServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiConnFabricServiceIfIndex.setStatus('current')
funiConnFabricVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiConnFabricVpi.setStatus('current')
funiConnFabricVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiConnFabricVci.setStatus('current')
funiConnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: funiConnRowStatus.setStatus('current')
funiConnName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: funiConnName.setStatus('current')
funiConnAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: funiConnAdminStatus.setStatus('current')
funiConnOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiConnOperStatus.setStatus('current')
funiConnProfileEpdPpdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: funiConnProfileEpdPpdIndex.setStatus('current')
funiIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2), )
if mibBuilder.loadTexts: funiIfExtTable.setStatus('current')
funiIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: funiIfExtEntry.setStatus('current')
funiIfExtProfileFuniIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: funiIfExtProfileFuniIndex.setStatus('current')
funiIfExtProfileServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: funiIfExtProfileServiceIndex.setStatus('current')
funiIfExtStatsMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: funiIfExtStatsMonitor.setStatus('current')
funiIfExtNeighborIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: funiIfExtNeighborIpAddress.setStatus('current')
funiIfExtStatsEnabledTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiIfExtStatsEnabledTimeStamp.setStatus('current')
funiIfExtSigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exist", 1), ("nonexist", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: funiIfExtSigStatus.setStatus('current')
mibBuilder.exportSymbols("Fore-Funi-MIB", funiIfExtStatsMonitor=funiIfExtStatsMonitor, funiIfExtNeighborIpAddress=funiIfExtNeighborIpAddress, funiConnFabricVpi=funiConnFabricVpi, funiConnRowStatus=funiConnRowStatus, funiConnAdminStatus=funiConnAdminStatus, funiConnName=funiConnName, funiConnProfileEpdPpdIndex=funiConnProfileEpdPpdIndex, funi=funi, funiConnTable=funiConnTable, funiConnOperStatus=funiConnOperStatus, funiIfExtProfileFuniIndex=funiIfExtProfileFuniIndex, funiIfExtStatsEnabledTimeStamp=funiIfExtStatsEnabledTimeStamp, funiIfExtTable=funiIfExtTable, funiConnEntry=funiConnEntry, funiConnFabricVci=funiConnFabricVci, funiIfExtSigStatus=funiIfExtSigStatus, PYSNMP_MODULE_ID=funi, funiIfExtProfileServiceIndex=funiIfExtProfileServiceIndex, funiConnFabricServiceIfIndex=funiConnFabricServiceIfIndex, funiConnFuniVpi=funiConnFuniVpi, funiIfExtEntry=funiIfExtEntry, funiConnFuniServiceIfIndex=funiConnFuniServiceIfIndex, funiConnFuniVci=funiConnFuniVci)
