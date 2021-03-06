#
# PySNMP MIB module HH3C-DHCP-SNOOP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DHCP-SNOOP2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
InetAddressIPv4, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Counter32, MibIdentifier, Counter64, ModuleIdentity, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Integer32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Integer32", "Bits", "TimeTicks")
TruthValue, RowStatus, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "MacAddress", "TextualConvention")
hh3cDhcpSnoop2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 124))
hh3cDhcpSnoop2.setRevisions(('2013-04-15 00:00',))
if mibBuilder.loadTexts: hh3cDhcpSnoop2.setLastUpdated('201304150000Z')
if mibBuilder.loadTexts: hh3cDhcpSnoop2.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cDhcpSnoop2ScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1))
hh3cDhcpSnoop2ConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1))
hh3cDhcpSnoop2Enabled = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2Enabled.setStatus('current')
hh3cDhcpSnoop2BindDbName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindDbName.setStatus('current')
hh3cDhcpSnoop2BindRefreshIntvl = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 864000)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindRefreshIntvl.setStatus('current')
hh3cDhcpSnoop2BindRefresh = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindRefresh.setStatus('current')
hh3cDhcpSnoop2StatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2))
hh3cDhcpSnoop2PktSentNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoop2PktSentNum.setStatus('current')
hh3cDhcpSnoop2PktRcvNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoop2PktRcvNum.setStatus('current')
hh3cDhcpSnoop2PktDropNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoop2PktDropNum.setStatus('current')
hh3cDhcpSnoop2Tables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2))
hh3cDhcpSnoop2BindTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1), )
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindTable.setStatus('current')
hh3cDhcpSnoop2BindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1), ).setIndexNames((0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2BindIpAddr"), (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2BindVlanId"), (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2BindSecVlanId"))
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindEntry.setStatus('current')
hh3cDhcpSnoop2BindIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 1), InetAddressIPv4())
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindIpAddr.setStatus('current')
hh3cDhcpSnoop2BindVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindVlanId.setStatus('current')
hh3cDhcpSnoop2BindSecVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(65535, 65535), )))
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindSecVlanId.setStatus('current')
hh3cDhcpSnoop2BindMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindMacAddr.setStatus('current')
hh3cDhcpSnoop2BindLease = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindLease.setStatus('current')
hh3cDhcpSnoop2BindPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindPortIndex.setStatus('current')
hh3cDhcpSnoop2BindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpSnoop2BindRowStatus.setStatus('current')
hh3cDhcpSnoop2IfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2), )
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfConfigTable.setStatus('current')
hh3cDhcpSnoop2IfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfConfigEntry.setStatus('current')
hh3cDhcpSnoop2IfTrustStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("untrusted", 0), ("trusted", 1))).clone('untrusted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfTrustStatus.setStatus('current')
hh3cDhcpSnoop2IfCheckMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfCheckMac.setStatus('current')
hh3cDhcpSnoop2IfCheckRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfCheckRequest.setStatus('current')
hh3cDhcpSnoop2IfRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfRateLimit.setStatus('current')
hh3cDhcpSnoop2IfRecordBind = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfRecordBind.setStatus('current')
hh3cDhcpSnoop2IfMaxLearnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfMaxLearnNum.setStatus('current')
hh3cDhcpSnoop2IfOpt82Enable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82Enable.setStatus('current')
hh3cDhcpSnoop2IfOpt82Strategy = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("drop", 1), ("keep", 2), ("replace", 3))).clone('replace')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82Strategy.setStatus('current')
hh3cDhcpSnoop2IfOpt82CIDMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("verbose", 2), ("userDefine", 3))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82CIDMode.setStatus('current')
hh3cDhcpSnoop2IfOpt82CIDNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("mac", 2), ("sysname", 3), ("userDefine", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82CIDNodeType.setStatus('current')
hh3cDhcpSnoop2IfOpt82CIDNodeStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82CIDNodeStr.setStatus('current')
hh3cDhcpSnoop2IfOpt82CIDStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 12), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 63), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82CIDStr.setStatus('current')
hh3cDhcpSnoop2IfOpt82CIDFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hex", 1), ("ascii", 2), ("undefine", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82CIDFormat.setStatus('current')
hh3cDhcpSnoop2IfOpt82RIDMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("sysname", 2), ("userDefine", 3))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82RIDMode.setStatus('current')
hh3cDhcpSnoop2IfOpt82RIDStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82RIDStr.setStatus('current')
hh3cDhcpSnoop2IfOpt82RIDFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hex", 1), ("ascii", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfOpt82RIDFormat.setStatus('current')
hh3cDhcpSnoop2IfVlanCIDTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3), )
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanCIDTable.setStatus('current')
hh3cDhcpSnoop2IfVlanCIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2IfVlanCIDVlanIndex"))
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanCIDEntry.setStatus('current')
hh3cDhcpSnoop2IfVlanCIDVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanCIDVlanIndex.setStatus('current')
hh3cDhcpSnoop2IfVlanCIDStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanCIDStr.setStatus('current')
hh3cDhcpSnoop2IfVlanCIDRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanCIDRowStatus.setStatus('current')
hh3cDhcpSnoop2IfVlanRIDTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4), )
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanRIDTable.setStatus('current')
hh3cDhcpSnoop2IfVlanRIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2IfVlanRIDVlanIndex"))
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanRIDEntry.setStatus('current')
hh3cDhcpSnoop2IfVlanRIDVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanRIDVlanIndex.setStatus('current')
hh3cDhcpSnoop2IfVlanRIDMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sysname", 1), ("userDefine", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanRIDMode.setStatus('current')
hh3cDhcpSnoop2IfVlanRIDStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanRIDStr.setStatus('current')
hh3cDhcpSnoop2IfVlanRIDRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpSnoop2IfVlanRIDRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-DHCP-SNOOP2-MIB", hh3cDhcpSnoop2BindSecVlanId=hh3cDhcpSnoop2BindSecVlanId, hh3cDhcpSnoop2IfVlanCIDStr=hh3cDhcpSnoop2IfVlanCIDStr, hh3cDhcpSnoop2IfConfigEntry=hh3cDhcpSnoop2IfConfigEntry, hh3cDhcpSnoop2PktRcvNum=hh3cDhcpSnoop2PktRcvNum, hh3cDhcpSnoop2IfVlanRIDStr=hh3cDhcpSnoop2IfVlanRIDStr, hh3cDhcpSnoop2IfVlanRIDTable=hh3cDhcpSnoop2IfVlanRIDTable, hh3cDhcpSnoop2BindRowStatus=hh3cDhcpSnoop2BindRowStatus, hh3cDhcpSnoop2ConfigGroup=hh3cDhcpSnoop2ConfigGroup, hh3cDhcpSnoop2Tables=hh3cDhcpSnoop2Tables, hh3cDhcpSnoop2IfVlanCIDRowStatus=hh3cDhcpSnoop2IfVlanCIDRowStatus, hh3cDhcpSnoop2BindMacAddr=hh3cDhcpSnoop2BindMacAddr, hh3cDhcpSnoop2BindRefresh=hh3cDhcpSnoop2BindRefresh, hh3cDhcpSnoop2IfRecordBind=hh3cDhcpSnoop2IfRecordBind, hh3cDhcpSnoop2IfTrustStatus=hh3cDhcpSnoop2IfTrustStatus, hh3cDhcpSnoop2IfVlanCIDEntry=hh3cDhcpSnoop2IfVlanCIDEntry, hh3cDhcpSnoop2IfCheckRequest=hh3cDhcpSnoop2IfCheckRequest, hh3cDhcpSnoop2PktSentNum=hh3cDhcpSnoop2PktSentNum, hh3cDhcpSnoop2IfOpt82CIDFormat=hh3cDhcpSnoop2IfOpt82CIDFormat, hh3cDhcpSnoop2IfVlanCIDTable=hh3cDhcpSnoop2IfVlanCIDTable, hh3cDhcpSnoop2IfMaxLearnNum=hh3cDhcpSnoop2IfMaxLearnNum, hh3cDhcpSnoop2ScalarObjects=hh3cDhcpSnoop2ScalarObjects, hh3cDhcpSnoop2BindIpAddr=hh3cDhcpSnoop2BindIpAddr, hh3cDhcpSnoop2IfOpt82CIDMode=hh3cDhcpSnoop2IfOpt82CIDMode, hh3cDhcpSnoop2IfVlanRIDMode=hh3cDhcpSnoop2IfVlanRIDMode, hh3cDhcpSnoop2Enabled=hh3cDhcpSnoop2Enabled, hh3cDhcpSnoop2BindPortIndex=hh3cDhcpSnoop2BindPortIndex, hh3cDhcpSnoop2IfOpt82CIDNodeStr=hh3cDhcpSnoop2IfOpt82CIDNodeStr, hh3cDhcpSnoop2IfConfigTable=hh3cDhcpSnoop2IfConfigTable, hh3cDhcpSnoop2IfOpt82RIDStr=hh3cDhcpSnoop2IfOpt82RIDStr, hh3cDhcpSnoop2=hh3cDhcpSnoop2, hh3cDhcpSnoop2IfCheckMac=hh3cDhcpSnoop2IfCheckMac, hh3cDhcpSnoop2IfVlanRIDRowStatus=hh3cDhcpSnoop2IfVlanRIDRowStatus, hh3cDhcpSnoop2IfOpt82RIDFormat=hh3cDhcpSnoop2IfOpt82RIDFormat, hh3cDhcpSnoop2IfOpt82CIDNodeType=hh3cDhcpSnoop2IfOpt82CIDNodeType, hh3cDhcpSnoop2BindTable=hh3cDhcpSnoop2BindTable, hh3cDhcpSnoop2BindDbName=hh3cDhcpSnoop2BindDbName, hh3cDhcpSnoop2BindVlanId=hh3cDhcpSnoop2BindVlanId, hh3cDhcpSnoop2IfOpt82CIDStr=hh3cDhcpSnoop2IfOpt82CIDStr, hh3cDhcpSnoop2IfRateLimit=hh3cDhcpSnoop2IfRateLimit, hh3cDhcpSnoop2IfOpt82Strategy=hh3cDhcpSnoop2IfOpt82Strategy, hh3cDhcpSnoop2IfOpt82Enable=hh3cDhcpSnoop2IfOpt82Enable, PYSNMP_MODULE_ID=hh3cDhcpSnoop2, hh3cDhcpSnoop2IfVlanCIDVlanIndex=hh3cDhcpSnoop2IfVlanCIDVlanIndex, hh3cDhcpSnoop2IfVlanRIDEntry=hh3cDhcpSnoop2IfVlanRIDEntry, hh3cDhcpSnoop2StatisticsGroup=hh3cDhcpSnoop2StatisticsGroup, hh3cDhcpSnoop2BindEntry=hh3cDhcpSnoop2BindEntry, hh3cDhcpSnoop2BindRefreshIntvl=hh3cDhcpSnoop2BindRefreshIntvl, hh3cDhcpSnoop2PktDropNum=hh3cDhcpSnoop2PktDropNum, hh3cDhcpSnoop2BindLease=hh3cDhcpSnoop2BindLease, hh3cDhcpSnoop2IfOpt82RIDMode=hh3cDhcpSnoop2IfOpt82RIDMode, hh3cDhcpSnoop2IfVlanRIDVlanIndex=hh3cDhcpSnoop2IfVlanRIDVlanIndex)
