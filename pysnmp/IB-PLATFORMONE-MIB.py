#
# PySNMP MIB module IB-PLATFORMONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IB-PLATFORMONE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
IbString, ibPlatformOne, IbIpAddr = mibBuilder.importSymbols("IB-SMI-MIB", "IbString", "ibPlatformOne", "IbIpAddr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, Bits, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Integer32, TimeTicks, Gauge32, iso, Counter64, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Bits", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "iso", "Counter64", "enterprises", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibPlatformModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1))
ibPlatformModule.setRevisions(('2010-11-15 00:00', '2010-10-19 00:00', '2010-07-28 00:00', '2009-06-05 00:00', '2008-09-29 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))
if mibBuilder.loadTexts: ibPlatformModule.setLastUpdated('201011150000Z')
if mibBuilder.loadTexts: ibPlatformModule.setOrganization('Infoblox')
ibCPUTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibCPUTemperature.setStatus('current')
ibClusterReplicationStatusTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2), )
if mibBuilder.loadTexts: ibClusterReplicationStatusTable.setStatus('current')
ibClusterReplicationStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1), ).setIndexNames((0, "IB-PLATFORMONE-MIB", "ibNodeIPAddress"))
if mibBuilder.loadTexts: ibClusterReplicationStatusEntry.setStatus('current')
ibNodeIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 1), IbIpAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNodeIPAddress.setStatus('current')
ibNodeReplicationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 2), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNodeReplicationStatus.setStatus('current')
ibNodeQueueFromMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNodeQueueFromMaster.setStatus('current')
ibNodeLastRepTimeFromMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 4), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNodeLastRepTimeFromMaster.setStatus('current')
ibNodeQueueToMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNodeQueueToMaster.setStatus('current')
ibNodeLastRepTimeToMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 2, 1, 6), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNodeLastRepTimeToMaster.setStatus('current')
ibNetworkMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3))
ibHardwareType = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 4), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibHardwareType.setStatus('current')
ibHardwareId = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 5), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibHardwareId.setStatus('current')
ibSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 6), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibSerialNumber.setStatus('current')
ibNiosVersion = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 7), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNiosVersion.setStatus('current')
ibSystemMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8))
ibSystemMonitorCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 1))
ibSystemMonitorMem = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 2))
ibSystemMonitorCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibSystemMonitorCpuUsage.setStatus('current')
ibSystemMonitorMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 8, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibSystemMonitorMemUsage.setStatus('current')
ibNetworkMonitorDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1))
ibNetworkMonitorDNSActive = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nonactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSActive.setStatus('current')
ibNetworkMonitorDNSNonAA = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2))
ibNetworkMonitorDNSNonAAT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1))
ibNetworkMonitorDNSNonAAT5 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2))
ibNetworkMonitorDNSNonAAT15 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3))
ibNetworkMonitorDNSNonAAT60 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4))
ibNetworkMonitorDNSNonAAT1440 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5))
ibNetworkMonitorDNSAA = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3))
ibNetworkMonitorDNSAAT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1))
ibNetworkMonitorDNSAAT5 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2))
ibNetworkMonitorDNSAAT15 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3))
ibNetworkMonitorDNSAAT60 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4))
ibNetworkMonitorDNSAAT1440 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5))
ibNetworkMonitorDNSNonAAT1AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT1AvgLatency.setStatus('current')
ibNetworkMonitorDNSNonAAT1Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT1Count.setStatus('current')
ibNetworkMonitorDNSNonAAT5AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT5AvgLatency.setStatus('current')
ibNetworkMonitorDNSNonAAT5Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT5Count.setStatus('current')
ibNetworkMonitorDNSNonAAT15AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT15AvgLatency.setStatus('current')
ibNetworkMonitorDNSNonAAT15Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT15Count.setStatus('current')
ibNetworkMonitorDNSNonAAT60AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT60AvgLatency.setStatus('current')
ibNetworkMonitorDNSNonAAT60Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT60Count.setStatus('current')
ibNetworkMonitorDNSNonAAT1440AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT1440AvgLatency.setStatus('current')
ibNetworkMonitorDNSNonAAT1440Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 2, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSNonAAT1440Count.setStatus('current')
ibNetworkMonitorDNSAAT1AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT1AvgLatency.setStatus('current')
ibNetworkMonitorDNSAAT1Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT1Count.setStatus('current')
ibNetworkMonitorDNSAAT5AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT5AvgLatency.setStatus('current')
ibNetworkMonitorDNSAAT5Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT5Count.setStatus('current')
ibNetworkMonitorDNSAAT15AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT15AvgLatency.setStatus('current')
ibNetworkMonitorDNSAAT15Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT15Count.setStatus('current')
ibNetworkMonitorDNSAAT60AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT60AvgLatency.setStatus('current')
ibNetworkMonitorDNSAAT60Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT60Count.setStatus('current')
ibNetworkMonitorDNSAAT1440AvgLatency = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT1440AvgLatency.setStatus('current')
ibNetworkMonitorDNSAAT1440Count = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 3, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSAAT1440Count.setStatus('current')
ibNetworkMonitorDNSSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4))
ibNetworkMonitorDNSSecurityInvalidPort = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1))
ibNetworkMonitorDNSSecurityInvalidPort1 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidPort1.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidPort5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidPort5.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidPort15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidPort15.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidPort60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidPort60.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidPort1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidPort1440.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidPortCount = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidPortCount.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxid = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2))
ibNetworkMonitorDNSSecurityInvalidTxid1 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxid1.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxid5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxid5.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxid15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxid15.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxid60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxid60.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxid1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxid1440.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxidCount = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxidCount.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidPortOnly = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidPortOnly.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxidOnly = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxidOnly.setStatus('current')
ibNetworkMonitorDNSSecurityInvalidTxidAndPort = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 3, 1, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNetworkMonitorDNSSecurityInvalidTxidAndPort.setStatus('current')
class IbServiceStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("working", 1), ("warning", 2), ("failed", 3), ("inactive", 4), ("unknown", 5))

class IbServiceNames(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("dhcp", 1), ("dns", 2), ("ntp", 3), ("radius", 4), ("tftp", 5), ("http-file-dist", 6), ("ftp", 7), ("bloxtools-move", 8), ("bloxtools", 9), ("node-status", 10), ("disk-usage", 11), ("enet-lan", 12), ("enet-lan2", 13), ("enet-ha", 14), ("enet-mgmt", 15), ("lcd", 16), ("memory", 17), ("replication", 18), ("db-object", 19), ("raid-summary", 20), ("raid-disk1", 21), ("raid-disk2", 22), ("raid-disk3", 23), ("raid-disk4", 24), ("fan1", 25), ("fan2", 26), ("fan3", 27), ("power-supply", 28), ("ntp-sync", 29), ("cpu1-temp", 30), ("cpu2-temp", 31), ("sys-temp", 32), ("raid-battery", 33), ("cpu-usage", 34), ("ospf", 35), ("bgp", 36))

ibMemberServiceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9), )
if mibBuilder.loadTexts: ibMemberServiceStatusTable.setStatus('current')
ibMemberServiceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1), ).setIndexNames((0, "IB-PLATFORMONE-MIB", "ibServiceName"))
if mibBuilder.loadTexts: ibMemberServiceStatusEntry.setStatus('current')
ibServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 1), IbServiceNames()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibServiceName.setStatus('current')
ibServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 2), IbServiceStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibServiceStatus.setStatus('current')
ibServiceDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 9, 1, 3), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibServiceDesc.setStatus('current')
ibMemberNode1ServiceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10), )
if mibBuilder.loadTexts: ibMemberNode1ServiceStatusTable.setStatus('current')
ibMemberNode1ServiceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1), ).setIndexNames((0, "IB-PLATFORMONE-MIB", "ibNode1ServiceName"))
if mibBuilder.loadTexts: ibMemberNode1ServiceStatusEntry.setStatus('current')
ibNode1ServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 1), IbServiceNames()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNode1ServiceName.setStatus('current')
ibNode1ServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 2), IbServiceStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNode1ServiceStatus.setStatus('current')
ibNode1ServiceDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 10, 1, 3), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNode1ServiceDesc.setStatus('current')
ibMemberNode2ServiceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11), )
if mibBuilder.loadTexts: ibMemberNode2ServiceStatusTable.setStatus('current')
ibMemberNode2ServiceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1), ).setIndexNames((0, "IB-PLATFORMONE-MIB", "ibNode2ServiceName"))
if mibBuilder.loadTexts: ibMemberNode2ServiceStatusEntry.setStatus('current')
ibNode2ServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 1), IbServiceNames()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNode2ServiceName.setStatus('current')
ibNode2ServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 2), IbServiceStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNode2ServiceStatus.setStatus('current')
ibNode2ServiceDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2, 1, 11, 1, 3), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibNode2ServiceDesc.setStatus('current')
mibBuilder.exportSymbols("IB-PLATFORMONE-MIB", ibNetworkMonitorDNSNonAAT1AvgLatency=ibNetworkMonitorDNSNonAAT1AvgLatency, ibNodeQueueFromMaster=ibNodeQueueFromMaster, ibNetworkMonitorDNSNonAAT1440=ibNetworkMonitorDNSNonAAT1440, ibClusterReplicationStatusTable=ibClusterReplicationStatusTable, ibServiceName=ibServiceName, ibNetworkMonitorDNSSecurityInvalidPort60=ibNetworkMonitorDNSSecurityInvalidPort60, ibNetworkMonitorDNSNonAAT60AvgLatency=ibNetworkMonitorDNSNonAAT60AvgLatency, ibNodeReplicationStatus=ibNodeReplicationStatus, ibMemberServiceStatusEntry=ibMemberServiceStatusEntry, ibSystemMonitorCpu=ibSystemMonitorCpu, ibPlatformModule=ibPlatformModule, ibNetworkMonitorDNSAAT60=ibNetworkMonitorDNSAAT60, ibNetworkMonitorDNSSecurityInvalidPort1=ibNetworkMonitorDNSSecurityInvalidPort1, ibNetworkMonitorDNSNonAAT1Count=ibNetworkMonitorDNSNonAAT1Count, ibNetworkMonitorDNSSecurityInvalidTxid15=ibNetworkMonitorDNSSecurityInvalidTxid15, ibNetworkMonitorDNSSecurityInvalidPort=ibNetworkMonitorDNSSecurityInvalidPort, ibServiceDesc=ibServiceDesc, ibMemberNode2ServiceStatusEntry=ibMemberNode2ServiceStatusEntry, ibNodeIPAddress=ibNodeIPAddress, ibNode1ServiceDesc=ibNode1ServiceDesc, ibNetworkMonitorDNSAAT15=ibNetworkMonitorDNSAAT15, ibNetworkMonitorDNSSecurityInvalidTxid1=ibNetworkMonitorDNSSecurityInvalidTxid1, ibNetworkMonitorDNS=ibNetworkMonitorDNS, ibNetworkMonitorDNSNonAAT1=ibNetworkMonitorDNSNonAAT1, ibNetworkMonitorDNSSecurity=ibNetworkMonitorDNSSecurity, ibNetworkMonitorDNSSecurityInvalidTxid5=ibNetworkMonitorDNSSecurityInvalidTxid5, ibNetworkMonitorDNSAAT5Count=ibNetworkMonitorDNSAAT5Count, ibNetworkMonitorDNSSecurityInvalidTxidOnly=ibNetworkMonitorDNSSecurityInvalidTxidOnly, ibNetworkMonitorDNSAAT15AvgLatency=ibNetworkMonitorDNSAAT15AvgLatency, ibNetworkMonitor=ibNetworkMonitor, ibMemberNode1ServiceStatusEntry=ibMemberNode1ServiceStatusEntry, ibServiceStatus=ibServiceStatus, ibNetworkMonitorDNSSecurityInvalidPortCount=ibNetworkMonitorDNSSecurityInvalidPortCount, ibSystemMonitorCpuUsage=ibSystemMonitorCpuUsage, ibNodeLastRepTimeFromMaster=ibNodeLastRepTimeFromMaster, ibNodeLastRepTimeToMaster=ibNodeLastRepTimeToMaster, ibNetworkMonitorDNSSecurityInvalidTxidAndPort=ibNetworkMonitorDNSSecurityInvalidTxidAndPort, ibNetworkMonitorDNSSecurityInvalidTxid1440=ibNetworkMonitorDNSSecurityInvalidTxid1440, ibNetworkMonitorDNSAAT1Count=ibNetworkMonitorDNSAAT1Count, ibNetworkMonitorDNSNonAA=ibNetworkMonitorDNSNonAA, ibNetworkMonitorDNSSecurityInvalidTxidCount=ibNetworkMonitorDNSSecurityInvalidTxidCount, ibNetworkMonitorDNSAAT1AvgLatency=ibNetworkMonitorDNSAAT1AvgLatency, ibNetworkMonitorDNSNonAAT15AvgLatency=ibNetworkMonitorDNSNonAAT15AvgLatency, ibNetworkMonitorDNSAAT1440Count=ibNetworkMonitorDNSAAT1440Count, ibNetworkMonitorDNSSecurityInvalidTxid60=ibNetworkMonitorDNSSecurityInvalidTxid60, ibNetworkMonitorDNSSecurityInvalidPort1440=ibNetworkMonitorDNSSecurityInvalidPort1440, ibNetworkMonitorDNSAAT5AvgLatency=ibNetworkMonitorDNSAAT5AvgLatency, ibMemberNode2ServiceStatusTable=ibMemberNode2ServiceStatusTable, ibNetworkMonitorDNSActive=ibNetworkMonitorDNSActive, ibNetworkMonitorDNSNonAAT60Count=ibNetworkMonitorDNSNonAAT60Count, ibNiosVersion=ibNiosVersion, ibNetworkMonitorDNSAAT1=ibNetworkMonitorDNSAAT1, ibHardwareId=ibHardwareId, ibSystemMonitorMem=ibSystemMonitorMem, ibNetworkMonitorDNSNonAAT1440Count=ibNetworkMonitorDNSNonAAT1440Count, IbServiceStates=IbServiceStates, ibNetworkMonitorDNSNonAAT15=ibNetworkMonitorDNSNonAAT15, ibNetworkMonitorDNSAAT60AvgLatency=ibNetworkMonitorDNSAAT60AvgLatency, ibNetworkMonitorDNSAAT15Count=ibNetworkMonitorDNSAAT15Count, ibNetworkMonitorDNSNonAAT5=ibNetworkMonitorDNSNonAAT5, ibNode1ServiceName=ibNode1ServiceName, ibClusterReplicationStatusEntry=ibClusterReplicationStatusEntry, ibNetworkMonitorDNSNonAAT15Count=ibNetworkMonitorDNSNonAAT15Count, ibNode2ServiceName=ibNode2ServiceName, ibNetworkMonitorDNSAAT1440=ibNetworkMonitorDNSAAT1440, ibSerialNumber=ibSerialNumber, ibNetworkMonitorDNSNonAAT60=ibNetworkMonitorDNSNonAAT60, ibNode2ServiceDesc=ibNode2ServiceDesc, ibHardwareType=ibHardwareType, ibNetworkMonitorDNSNonAAT5Count=ibNetworkMonitorDNSNonAAT5Count, ibMemberNode1ServiceStatusTable=ibMemberNode1ServiceStatusTable, ibNetworkMonitorDNSAAT5=ibNetworkMonitorDNSAAT5, ibNetworkMonitorDNSAA=ibNetworkMonitorDNSAA, ibCPUTemperature=ibCPUTemperature, ibNode2ServiceStatus=ibNode2ServiceStatus, ibSystemMonitorMemUsage=ibSystemMonitorMemUsage, ibMemberServiceStatusTable=ibMemberServiceStatusTable, ibNetworkMonitorDNSNonAAT1440AvgLatency=ibNetworkMonitorDNSNonAAT1440AvgLatency, ibNetworkMonitorDNSAAT60Count=ibNetworkMonitorDNSAAT60Count, ibNetworkMonitorDNSAAT1440AvgLatency=ibNetworkMonitorDNSAAT1440AvgLatency, ibNetworkMonitorDNSSecurityInvalidPort15=ibNetworkMonitorDNSSecurityInvalidPort15, ibNodeQueueToMaster=ibNodeQueueToMaster, ibNetworkMonitorDNSSecurityInvalidPort5=ibNetworkMonitorDNSSecurityInvalidPort5, PYSNMP_MODULE_ID=ibPlatformModule, IbServiceNames=IbServiceNames, ibNode1ServiceStatus=ibNode1ServiceStatus, ibSystemMonitor=ibSystemMonitor, ibNetworkMonitorDNSSecurityInvalidTxid=ibNetworkMonitorDNSSecurityInvalidTxid, ibNetworkMonitorDNSNonAAT5AvgLatency=ibNetworkMonitorDNSNonAAT5AvgLatency, ibNetworkMonitorDNSSecurityInvalidPortOnly=ibNetworkMonitorDNSSecurityInvalidPortOnly)
