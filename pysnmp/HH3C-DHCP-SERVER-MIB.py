#
# PySNMP MIB module HH3C-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DHCP-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, TimeTicks, Gauge32, iso, Counter64, Unsigned32, MibIdentifier, IpAddress, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "TimeTicks", "Gauge32", "iso", "Counter64", "Unsigned32", "MibIdentifier", "IpAddress", "NotificationType", "Bits")
DisplayString, RowStatus, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "MacAddress", "TextualConvention")
hh3cDHCPServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 101))
hh3cDHCPServer.setRevisions(('2009-05-06 00:00',))
if mibBuilder.loadTexts: hh3cDHCPServer.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: hh3cDHCPServer.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cDHCPServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1))
hh3cDHCPServerIPPoolUsage = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPServerIPPoolUsage.setStatus('current')
hh3cDHCPServerReqTimes = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPServerReqTimes.setStatus('current')
hh3cDHCPServerReqSuccessTimes = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPServerReqSuccessTimes.setStatus('current')
hh3cDHCPServerAvgIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPServerAvgIpUseThreshold.setStatus('current')
hh3cDHCPServerMaxIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPServerMaxIpUseThreshold.setStatus('current')
hh3cDHCPServerAllocateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPServerAllocateThreshold.setStatus('current')
hh3cDHCPServerTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2))
hh3cDHCPServerPoolName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDHCPServerPoolName.setStatus('current')
hh3cDHCPSrvGlobalPoolTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolTable.setStatus('current')
hh3cDHCPSrvGlobalPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolEntry.setStatus('current')
hh3cDHCPSrvGlobalPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolName.setStatus('current')
hh3cDHCPSrvGlobalPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolRowStatus.setStatus('current')
hh3cDHCPSrvGlobalPoolConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolConfigTable.setStatus('current')
hh3cDHCPSrvGlobalPoolConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolConfigEntry.setStatus('current')
hh3cDHCPSrvGlobalPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("host", 1), ("network", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolType.setStatus('current')
hh3cDHCPSrvGlobalPoolNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolNetwork.setStatus('current')
hh3cDHCPSrvGlobalPoolNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolNetworkMask.setStatus('current')
hh3cDHCPSrvGlobalPoolHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostIPAddr.setStatus('current')
hh3cDHCPSrvGlobalPoolHostMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostMask.setStatus('current')
hh3cDHCPSrvGlobalPoolHostHAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 6), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostHAddr.setStatus('current')
hh3cDHCPSrvGlobalPoolCfgUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("undonetworkip", 1), ("undohostip", 2), ("undohosthaddr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus('current')
hh3cDHCPSrvGlobalPoolStartAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStartAddr.setStatus('current')
hh3cDHCPSrvGlobalPoolEndAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolEndAddr.setStatus('current')
hh3cDHCPSrvGlobalPoolParaTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolParaTable.setStatus('current')
hh3cDHCPSrvGlobalPoolParaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolParaEntry.setStatus('current')
hh3cDHCPSrvGlbPoolLeaseDay = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 365)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseDay.setStatus('current')
hh3cDHCPSrvGlbPoolLeaseHour = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseHour.setStatus('current')
hh3cDHCPSrvGlbPoolLeaseMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseMinute.setStatus('current')
hh3cDHCPSrvGlbPoolLeaseUnlimited = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("unlimited", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseUnlimited.setStatus('current')
hh3cDHCPSrvGlbPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolDomainName.setStatus('current')
hh3cDHCPSrvGlbPoolCliGWIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliGWIPStr.setStatus('current')
hh3cDHCPSrvGlbPoolCliGWIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliGWIPUndo.setStatus('current')
hh3cDHCPSrvGlbPoolCliDNSIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliDNSIPStr.setStatus('current')
hh3cDHCPSrvGlbPoolCliDNSIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus('current')
hh3cDHCPSrvGlbPoolCliNetbiosType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("null", 0), ("bnode", 1), ("pnode", 2), ("mnode", 4), ("hnode", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNetbiosType.setStatus('current')
hh3cDHCPSrvGlbPoolCliNbnsIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus('current')
hh3cDHCPSrvGlbPoolCliNbnsIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus('current')
hh3cDHCPSrvGlbPoolParaUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("undoDomain", 1), ("undoLease", 2), ("undoGateway", 3), ("undoDns", 4), ("undoNbns", 5), ("undoNbType", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolParaUndoFlag.setStatus('current')
hh3cDHCPSrvGlbPoolIPInUseReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolIPInUseReset.setStatus('current')
hh3cDHCPSrvGlbPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 15), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseTime.setStatus('current')
hh3cDHCPSrvGlbPoolPrimaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus('current')
hh3cDHCPSrvGlbPoolSecondaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus('current')
hh3cDHCPSrvGlbPoolLeaseSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseSecond.setStatus('current')
hh3cDHCPSrvGlobalPoolOptionTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolOptionTable.setStatus('current')
hh3cDHCPSrvGlobalPoolOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"), (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlbPoolOptCode"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolOptionEntry.setStatus('current')
hh3cDHCPSrvGlbPoolOptCode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptCode.setStatus('current')
hh3cDHCPSrvGlbPoolOptType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ascii", 1), ("hex", 2), ("ip", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptType.setStatus('current')
hh3cDHCPSrvGlbPoolOptAscii = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptAscii.setStatus('current')
hh3cDHCPSrvGlbPoolOptHexString = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 143))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptHexString.setStatus('current')
hh3cDHCPSrvGlbPoolOptIPString = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptIPString.setStatus('current')
hh3cDHCPSrvGlbPoolOptRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptRowStatus.setStatus('current')
hh3cDHCPSrvGlobalPoolStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStatTable.setStatus('current')
hh3cDHCPSrvGlobalPoolStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStatEntry.setStatus('current')
hh3cDHCPSrvGlbPoolIPPoolUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolIPPoolUsage.setStatus('current')
hh3cDHCPSrvGlbPoolReqTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolReqTimes.setStatus('current')
hh3cDHCPSrvGlbPoolSuccessTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolSuccessTimes.setStatus('current')
hh3cDHCPServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3))
hh3cDHCPServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0))
hh3cDHCPServerAddrExhaust = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 1)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerAddrExhaust.setStatus('current')
hh3cDHCPServerAddrExhaustRecover = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 2)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerAddrExhaustRecover.setStatus('current')
hh3cDHCPServerAvgIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 3)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerAvgIpUsageOverflow.setStatus('current')
hh3cDHCPServerMaxIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 4)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerMaxIpUsageOverflow.setStatus('current')
hh3cDHCPServerAllocateOverflow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 5))
if mibBuilder.loadTexts: hh3cDHCPServerAllocateOverflow.setStatus('current')
mibBuilder.exportSymbols("HH3C-DHCP-SERVER-MIB", hh3cDHCPSrvGlobalPoolEntry=hh3cDHCPSrvGlobalPoolEntry, hh3cDHCPSrvGlbPoolCliNbnsIPUndo=hh3cDHCPSrvGlbPoolCliNbnsIPUndo, hh3cDHCPSrvGlobalPoolEndAddr=hh3cDHCPSrvGlobalPoolEndAddr, hh3cDHCPSrvGlobalPoolStatTable=hh3cDHCPSrvGlobalPoolStatTable, hh3cDHCPSrvGlbPoolLeaseUnlimited=hh3cDHCPSrvGlbPoolLeaseUnlimited, hh3cDHCPServerMaxIpUseThreshold=hh3cDHCPServerMaxIpUseThreshold, hh3cDHCPSrvGlbPoolSuccessTimes=hh3cDHCPSrvGlbPoolSuccessTimes, hh3cDHCPSrvGlobalPoolHostIPAddr=hh3cDHCPSrvGlobalPoolHostIPAddr, hh3cDHCPSrvGlobalPoolType=hh3cDHCPSrvGlobalPoolType, hh3cDHCPServerReqTimes=hh3cDHCPServerReqTimes, hh3cDHCPSrvGlbPoolDomainName=hh3cDHCPSrvGlbPoolDomainName, hh3cDHCPSrvGlbPoolLeaseHour=hh3cDHCPSrvGlbPoolLeaseHour, hh3cDHCPSrvGlbPoolLeaseTime=hh3cDHCPSrvGlbPoolLeaseTime, hh3cDHCPSrvGlobalPoolConfigEntry=hh3cDHCPSrvGlobalPoolConfigEntry, hh3cDHCPSrvGlbPoolCliGWIPStr=hh3cDHCPSrvGlbPoolCliGWIPStr, hh3cDHCPSrvGlbPoolParaUndoFlag=hh3cDHCPSrvGlbPoolParaUndoFlag, hh3cDHCPSrvGlbPoolReqTimes=hh3cDHCPSrvGlbPoolReqTimes, hh3cDHCPServerPoolName=hh3cDHCPServerPoolName, hh3cDHCPSrvGlbPoolLeaseMinute=hh3cDHCPSrvGlbPoolLeaseMinute, hh3cDHCPSrvGlbPoolOptCode=hh3cDHCPSrvGlbPoolOptCode, hh3cDHCPServerTraps=hh3cDHCPServerTraps, hh3cDHCPSrvGlbPoolCliNetbiosType=hh3cDHCPSrvGlbPoolCliNetbiosType, hh3cDHCPSrvGlbPoolOptType=hh3cDHCPSrvGlbPoolOptType, hh3cDHCPSrvGlbPoolOptRowStatus=hh3cDHCPSrvGlbPoolOptRowStatus, hh3cDHCPSrvGlbPoolOptHexString=hh3cDHCPSrvGlbPoolOptHexString, hh3cDHCPServerObjects=hh3cDHCPServerObjects, hh3cDHCPServerReqSuccessTimes=hh3cDHCPServerReqSuccessTimes, hh3cDHCPSrvGlobalPoolParaEntry=hh3cDHCPSrvGlobalPoolParaEntry, hh3cDHCPSrvGlobalPoolStatEntry=hh3cDHCPSrvGlobalPoolStatEntry, hh3cDHCPSrvGlobalPoolNetwork=hh3cDHCPSrvGlobalPoolNetwork, hh3cDHCPServerTables=hh3cDHCPServerTables, hh3cDHCPSrvGlbPoolSecondaryDNSIP=hh3cDHCPSrvGlbPoolSecondaryDNSIP, hh3cDHCPSrvGlobalPoolParaTable=hh3cDHCPSrvGlobalPoolParaTable, hh3cDHCPServerAddrExhaust=hh3cDHCPServerAddrExhaust, hh3cDHCPSrvGlobalPoolConfigTable=hh3cDHCPSrvGlobalPoolConfigTable, hh3cDHCPSrvGlbPoolLeaseDay=hh3cDHCPSrvGlbPoolLeaseDay, hh3cDHCPSrvGlbPoolCliDNSIPUndo=hh3cDHCPSrvGlbPoolCliDNSIPUndo, hh3cDHCPSrvGlobalPoolCfgUndoFlag=hh3cDHCPSrvGlobalPoolCfgUndoFlag, hh3cDHCPServerAddrExhaustRecover=hh3cDHCPServerAddrExhaustRecover, hh3cDHCPServerMaxIpUsageOverflow=hh3cDHCPServerMaxIpUsageOverflow, hh3cDHCPSrvGlobalPoolTable=hh3cDHCPSrvGlobalPoolTable, hh3cDHCPSrvGlobalPoolOptionTable=hh3cDHCPSrvGlobalPoolOptionTable, hh3cDHCPSrvGlobalPoolOptionEntry=hh3cDHCPSrvGlobalPoolOptionEntry, hh3cDHCPSrvGlbPoolCliNbnsIPStr=hh3cDHCPSrvGlbPoolCliNbnsIPStr, hh3cDHCPSrvGlbPoolCliGWIPUndo=hh3cDHCPSrvGlbPoolCliGWIPUndo, hh3cDHCPSrvGlbPoolOptIPString=hh3cDHCPSrvGlbPoolOptIPString, hh3cDHCPServerAllocateThreshold=hh3cDHCPServerAllocateThreshold, PYSNMP_MODULE_ID=hh3cDHCPServer, hh3cDHCPSrvGlbPoolLeaseSecond=hh3cDHCPSrvGlbPoolLeaseSecond, hh3cDHCPSrvGlbPoolIPInUseReset=hh3cDHCPSrvGlbPoolIPInUseReset, hh3cDHCPServerIPPoolUsage=hh3cDHCPServerIPPoolUsage, hh3cDHCPServerAvgIpUseThreshold=hh3cDHCPServerAvgIpUseThreshold, hh3cDHCPSrvGlobalPoolHostMask=hh3cDHCPSrvGlobalPoolHostMask, hh3cDHCPSrvGlbPoolPrimaryDNSIP=hh3cDHCPSrvGlbPoolPrimaryDNSIP, hh3cDHCPServer=hh3cDHCPServer, hh3cDHCPSrvGlobalPoolRowStatus=hh3cDHCPSrvGlobalPoolRowStatus, hh3cDHCPSrvGlobalPoolStartAddr=hh3cDHCPSrvGlobalPoolStartAddr, hh3cDHCPSrvGlbPoolOptAscii=hh3cDHCPSrvGlbPoolOptAscii, hh3cDHCPSrvGlbPoolIPPoolUsage=hh3cDHCPSrvGlbPoolIPPoolUsage, hh3cDHCPServerAvgIpUsageOverflow=hh3cDHCPServerAvgIpUsageOverflow, hh3cDHCPSrvGlobalPoolHostHAddr=hh3cDHCPSrvGlobalPoolHostHAddr, hh3cDHCPSrvGlobalPoolNetworkMask=hh3cDHCPSrvGlobalPoolNetworkMask, hh3cDHCPServerTrapPrefix=hh3cDHCPServerTrapPrefix, hh3cDHCPServerAllocateOverflow=hh3cDHCPServerAllocateOverflow, hh3cDHCPSrvGlbPoolCliDNSIPStr=hh3cDHCPSrvGlbPoolCliDNSIPStr, hh3cDHCPSrvGlobalPoolName=hh3cDHCPSrvGlobalPoolName)
