#
# PySNMP MIB module HH3C-RCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-RCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hh3cRCP, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRCP")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, TimeTicks, MibIdentifier, ModuleIdentity, IpAddress, Bits, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "TimeTicks", "MibIdentifier", "ModuleIdentity", "IpAddress", "Bits", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "iso", "Integer32")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
hh3cRCPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1))
hh3cRCPMIB.setRevisions(('2006-09-20 00:00',))
if mibBuilder.loadTexts: hh3cRCPMIB.setLastUpdated('200609200000Z')
if mibBuilder.loadTexts: hh3cRCPMIB.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cRCPLeaf = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1))
hh3cRCPServerEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRCPServerEnableStatus.setStatus('current')
hh3cRCPConnTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRCPConnTimeout.setStatus('current')
hh3cRCPRuleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRCPRuleTimeout.setStatus('current')
hh3cRCPServerMaxConn = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRCPServerMaxConn.setStatus('current')
hh3cRCPServerCurConn = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPServerCurConn.setStatus('current')
hh3cRCPConnTimeoutMaxValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPConnTimeoutMaxValue.setStatus('current')
hh3cRCPRuleTimeoutMaxValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPRuleTimeoutMaxValue.setStatus('current')
hh3cRCPServerMaxConnMaxValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPServerMaxConnMaxValue.setStatus('current')
hh3cRCPBalanceGroupIdMinValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPBalanceGroupIdMinValue.setStatus('current')
hh3cRCPBalanceGroupIdMaxValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPBalanceGroupIdMaxValue.setStatus('current')
hh3cRCPTotalUsers = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPTotalUsers.setStatus('current')
hh3cRCPTotalClientIPs = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPTotalClientIPs.setStatus('current')
hh3cRCPTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2))
hh3cRCPUserTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cRCPUserTable.setStatus('current')
hh3cRCPUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-RCP-MIB", "hh3cRCPUserName"))
if mibBuilder.loadTexts: hh3cRCPUserEntry.setStatus('current')
hh3cRCPUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: hh3cRCPUserName.setStatus('current')
hh3cRCPUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRCPUserPassword.setStatus('current')
hh3cRCPUserRedirectInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRCPUserRedirectInterface.setStatus('current')
hh3cRCPUserRedirectBalanceGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRCPUserRedirectBalanceGroup.setStatus('current')
hh3cRCPUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRCPUserRowStatus.setStatus('current')
hh3cRCPClientIPTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2), )
if mibBuilder.loadTexts: hh3cRCPClientIPTable.setStatus('current')
hh3cRCPClientIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1), ).setIndexNames((0, "HH3C-RCP-MIB", "hh3cRCPClientIPType"), (0, "HH3C-RCP-MIB", "hh3cRCPClientIP"))
if mibBuilder.loadTexts: hh3cRCPClientIPEntry.setStatus('current')
hh3cRCPClientIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hh3cRCPClientIPType.setStatus('current')
hh3cRCPClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: hh3cRCPClientIP.setStatus('current')
hh3cRCPClientIPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRCPClientIPRowStatus.setStatus('current')
hh3cRCPSessionTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3), )
if mibBuilder.loadTexts: hh3cRCPSessionTable.setStatus('current')
hh3cRCPSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1), ).setIndexNames((0, "HH3C-RCP-MIB", "hh3cRCPSessionId"))
if mibBuilder.loadTexts: hh3cRCPSessionEntry.setStatus('current')
hh3cRCPSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cRCPSessionId.setStatus('current')
hh3cRCPSessionClientIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPSessionClientIPType.setStatus('current')
hh3cRCPSessionClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPSessionClientIP.setStatus('current')
hh3cRCPSessionRunningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("operational", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPSessionRunningStatus.setStatus('current')
hh3cRCPSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 73, 1, 2, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRCPSessionUserName.setStatus('current')
mibBuilder.exportSymbols("HH3C-RCP-MIB", hh3cRCPRuleTimeout=hh3cRCPRuleTimeout, hh3cRCPServerMaxConn=hh3cRCPServerMaxConn, hh3cRCPServerCurConn=hh3cRCPServerCurConn, hh3cRCPSessionTable=hh3cRCPSessionTable, PYSNMP_MODULE_ID=hh3cRCPMIB, hh3cRCPMIB=hh3cRCPMIB, hh3cRCPSessionRunningStatus=hh3cRCPSessionRunningStatus, hh3cRCPSessionClientIPType=hh3cRCPSessionClientIPType, hh3cRCPClientIPEntry=hh3cRCPClientIPEntry, hh3cRCPUserRedirectBalanceGroup=hh3cRCPUserRedirectBalanceGroup, hh3cRCPTotalUsers=hh3cRCPTotalUsers, hh3cRCPUserName=hh3cRCPUserName, hh3cRCPSessionClientIP=hh3cRCPSessionClientIP, hh3cRCPRuleTimeoutMaxValue=hh3cRCPRuleTimeoutMaxValue, hh3cRCPClientIPTable=hh3cRCPClientIPTable, hh3cRCPServerMaxConnMaxValue=hh3cRCPServerMaxConnMaxValue, hh3cRCPBalanceGroupIdMaxValue=hh3cRCPBalanceGroupIdMaxValue, hh3cRCPLeaf=hh3cRCPLeaf, hh3cRCPTotalClientIPs=hh3cRCPTotalClientIPs, hh3cRCPClientIPRowStatus=hh3cRCPClientIPRowStatus, hh3cRCPSessionEntry=hh3cRCPSessionEntry, hh3cRCPSessionUserName=hh3cRCPSessionUserName, hh3cRCPUserTable=hh3cRCPUserTable, hh3cRCPUserPassword=hh3cRCPUserPassword, hh3cRCPConnTimeoutMaxValue=hh3cRCPConnTimeoutMaxValue, hh3cRCPUserEntry=hh3cRCPUserEntry, hh3cRCPServerEnableStatus=hh3cRCPServerEnableStatus, hh3cRCPClientIP=hh3cRCPClientIP, hh3cRCPBalanceGroupIdMinValue=hh3cRCPBalanceGroupIdMinValue, hh3cRCPUserRedirectInterface=hh3cRCPUserRedirectInterface, hh3cRCPSessionId=hh3cRCPSessionId, hh3cRCPClientIPType=hh3cRCPClientIPType, hh3cRCPConnTimeout=hh3cRCPConnTimeout, hh3cRCPUserRowStatus=hh3cRCPUserRowStatus, hh3cRCPTable=hh3cRCPTable)