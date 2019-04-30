#
# PySNMP MIB module HPN-ICF-MCDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-MCDR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, Bits, IpAddress, Unsigned32, iso, Gauge32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Bits", "IpAddress", "Unsigned32", "iso", "Gauge32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "ObjectIdentity", "Integer32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
hpnicfMultCDR = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86))
hpnicfMultCDR.setRevisions(('2007-12-15 00:00',))
if mibBuilder.loadTexts: hpnicfMultCDR.setLastUpdated('200712150000Z')
if mibBuilder.loadTexts: hpnicfMultCDR.setOrganization('')
hpnicfMultCDRCfgObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1))
hpnicfMultCDRStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRStatus.setStatus('current')
hpnicfMultCDRReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRReportInterval.setStatus('current')
hpnicfMultCDRCacheLimit = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRCacheLimit.setStatus('current')
hpnicfMultCDRRecordDelay = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRRecordDelay.setStatus('current')
hpnicfMultCDRRecordSend = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("send", 1), ("caching", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMultCDRRecordSend.setStatus('current')
hpnicfMultUserOnlineInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2), )
if mibBuilder.loadTexts: hpnicfMultUserOnlineInfoTable.setStatus('current')
hpnicfMultUserOnlineInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-MCDR-MIB", "hpnicfMultUserRecordID"))
if mibBuilder.loadTexts: hpnicfMultUserOnlineInfoEntry.setStatus('current')
hpnicfMultUserRecordID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfMultUserRecordID.setStatus('current')
hpnicfMultUserSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserSubIfIndex.setStatus('current')
hpnicfMultUserVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 3), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserVlanID.setStatus('current')
hpnicfMultUserJoinGAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinGAddrType.setStatus('current')
hpnicfMultUserJoinGAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinGAddr.setStatus('current')
hpnicfMultUserJoinSAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinSAddrType.setStatus('current')
hpnicfMultUserJoinSAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinSAddr.setStatus('current')
hpnicfMultUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("preview", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserStatus.setStatus('current')
hpnicfMultUserJoinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserJoinTime.setStatus('current')
hpnicfMultUserPreviewTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserPreviewTimes.setStatus('current')
hpnicfMultUserPreviewRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfMultUserPreviewRemain.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-MCDR-MIB", hpnicfMultUserSubIfIndex=hpnicfMultUserSubIfIndex, hpnicfMultUserJoinSAddrType=hpnicfMultUserJoinSAddrType, hpnicfMultCDRStatus=hpnicfMultCDRStatus, hpnicfMultUserJoinSAddr=hpnicfMultUserJoinSAddr, hpnicfMultCDR=hpnicfMultCDR, hpnicfMultCDRCfgObject=hpnicfMultCDRCfgObject, hpnicfMultUserJoinTime=hpnicfMultUserJoinTime, hpnicfMultUserRecordID=hpnicfMultUserRecordID, PYSNMP_MODULE_ID=hpnicfMultCDR, hpnicfMultUserPreviewTimes=hpnicfMultUserPreviewTimes, hpnicfMultUserStatus=hpnicfMultUserStatus, hpnicfMultUserJoinGAddrType=hpnicfMultUserJoinGAddrType, hpnicfMultUserJoinGAddr=hpnicfMultUserJoinGAddr, hpnicfMultUserVlanID=hpnicfMultUserVlanID, hpnicfMultUserPreviewRemain=hpnicfMultUserPreviewRemain, hpnicfMultCDRReportInterval=hpnicfMultCDRReportInterval, hpnicfMultCDRCacheLimit=hpnicfMultCDRCacheLimit, hpnicfMultCDRRecordDelay=hpnicfMultCDRRecordDelay, hpnicfMultCDRRecordSend=hpnicfMultCDRRecordSend, hpnicfMultUserOnlineInfoTable=hpnicfMultUserOnlineInfoTable, hpnicfMultUserOnlineInfoEntry=hpnicfMultUserOnlineInfoEntry)