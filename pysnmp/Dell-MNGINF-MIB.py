#
# PySNMP MIB module Dell-MNGINF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-MNGINF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:41:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, Gauge32, ModuleIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, MibIdentifier, IpAddress, ObjectIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "ModuleIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "MibIdentifier", "IpAddress", "ObjectIdentity", "iso", "TimeTicks")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
rlMngInf = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 89))
rlMngInf.setRevisions(('2003-09-21 00:00',))
if mibBuilder.loadTexts: rlMngInf.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlMngInf.setOrganization('Dell')
class RlMngInfServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("dontCare", 0), ("telnet", 1), ("snmp", 2), ("http", 3), ("https", 4), ("ssh", 5))

class RlMngInfActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("permit", 0), ("deny", 1))

rlMngInfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfMibVersion.setStatus('current')
rlMngInfEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfEnable.setStatus('current')
rlMngInfActiveListName = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfActiveListName.setStatus('current')
rlMngInfListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 89, 4), )
if mibBuilder.loadTexts: rlMngInfListTable.setStatus('current')
rlMngInfListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 89, 4, 1), ).setIndexNames((0, "Dell-MNGINF-MIB", "rlMngInfListName"), (0, "Dell-MNGINF-MIB", "rlMngInfListPriority"))
if mibBuilder.loadTexts: rlMngInfListEntry.setStatus('current')
rlMngInfListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListName.setStatus('current')
rlMngInfListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListPriority.setStatus('current')
rlMngInfListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIfIndex.setStatus('current')
rlMngInfListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIpAddr.setStatus('current')
rlMngInfListIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIpNetMask.setStatus('current')
rlMngInfListService = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 6), RlMngInfServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListService.setStatus('current')
rlMngInfListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 7), RlMngInfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListAction.setStatus('current')
rlMngInfListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListRowStatus.setStatus('current')
rlMngInfAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfAuditingEnable.setStatus('current')
rlMngInfListInetTable = MibTable((1, 3, 6, 1, 4, 1, 89, 89, 6), )
if mibBuilder.loadTexts: rlMngInfListInetTable.setStatus('current')
rlMngInfListInetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 89, 6, 1), ).setIndexNames((0, "Dell-MNGINF-MIB", "rlMngInfListInetName"), (0, "Dell-MNGINF-MIB", "rlMngInfListInetPriority"))
if mibBuilder.loadTexts: rlMngInfListInetEntry.setStatus('current')
rlMngInfListInetName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListInetName.setStatus('current')
rlMngInfListInetPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListInetPriority.setStatus('current')
rlMngInfListInetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetIfIndex.setStatus('current')
rlMngInfListInetIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetIpAddrType.setStatus('current')
rlMngInfListInetIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 5), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetIpAddr.setStatus('current')
rlMngInfListInetIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetIpNetMask.setStatus('current')
rlMngInfListInetService = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 7), RlMngInfServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetService.setStatus('current')
rlMngInfListInetAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 8), RlMngInfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetAction.setStatus('current')
rlMngInfListInetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetRowStatus.setStatus('current')
rlMngInfListInetIPv6PrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListInetIPv6PrefixLength.setStatus('current')
mibBuilder.exportSymbols("Dell-MNGINF-MIB", RlMngInfServiceType=RlMngInfServiceType, rlMngInfListInetService=rlMngInfListInetService, rlMngInfListInetIfIndex=rlMngInfListInetIfIndex, rlMngInfMibVersion=rlMngInfMibVersion, rlMngInfListName=rlMngInfListName, rlMngInfListInetIPv6PrefixLength=rlMngInfListInetIPv6PrefixLength, rlMngInfListInetRowStatus=rlMngInfListInetRowStatus, rlMngInfListEntry=rlMngInfListEntry, rlMngInfListRowStatus=rlMngInfListRowStatus, rlMngInfListInetPriority=rlMngInfListInetPriority, rlMngInfListAction=rlMngInfListAction, rlMngInfActiveListName=rlMngInfActiveListName, rlMngInfListPriority=rlMngInfListPriority, rlMngInfListInetIpNetMask=rlMngInfListInetIpNetMask, rlMngInf=rlMngInf, rlMngInfListInetTable=rlMngInfListInetTable, rlMngInfListIpAddr=rlMngInfListIpAddr, PYSNMP_MODULE_ID=rlMngInf, rlMngInfEnable=rlMngInfEnable, rlMngInfListInetEntry=rlMngInfListInetEntry, rlMngInfAuditingEnable=rlMngInfAuditingEnable, rlMngInfListIfIndex=rlMngInfListIfIndex, rlMngInfListInetIpAddr=rlMngInfListInetIpAddr, rlMngInfListTable=rlMngInfListTable, rlMngInfListInetIpAddrType=rlMngInfListInetIpAddrType, rlMngInfListIpNetMask=rlMngInfListIpNetMask, rlMngInfListInetName=rlMngInfListInetName, rlMngInfListService=rlMngInfListService, RlMngInfActionType=RlMngInfActionType, rlMngInfListInetAction=rlMngInfListInetAction)
