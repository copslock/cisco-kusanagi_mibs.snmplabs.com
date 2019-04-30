#
# PySNMP MIB module HH3C-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DOMAIN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, MibIdentifier, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, IpAddress, Bits, ObjectIdentity, TimeTicks, Gauge32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "IpAddress", "Bits", "ObjectIdentity", "TimeTicks", "Gauge32", "iso", "ModuleIdentity")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
hh3cDomain = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 46))
if mibBuilder.loadTexts: hh3cDomain.setLastUpdated('200908050000Z')
if mibBuilder.loadTexts: hh3cDomain.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cModeOfDomainScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("local", 2), ("radius", 3), ("tacacs", 4))

class Hh3cAAATypeDomainScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("accounting", 1), ("authentication", 2), ("authorization", 3), ("none", 4))

class Hh3cAccessModeofDomainScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("default", 1), ("login", 2), ("lanAccess", 3), ("portal", 4), ("ppp", 5), ("gcm", 6), ("dvpn", 7), ("dhcp", 8), ("voice", 9), ("superauthen", 10), ("command", 11), ("wapi", 12))

hh3cDomainControl = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 46, 1))
hh3cDomainDefault = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 46, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDomainDefault.setStatus('current')
hh3cDomainTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2))
hh3cDomainInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1), )
if mibBuilder.loadTexts: hh3cDomainInfoTable.setStatus('current')
hh3cDomainInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1), ).setIndexNames((0, "HH3C-DOMAIN-MIB", "hh3cDomainName"))
if mibBuilder.loadTexts: hh3cDomainInfoEntry.setStatus('current')
hh3cDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128)))
if mibBuilder.loadTexts: hh3cDomainName.setStatus('current')
hh3cDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("block", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainState.setStatus('current')
hh3cDomainMaxAccessNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainMaxAccessNum.setStatus('current')
hh3cDomainVlanAssignMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("integer", 1), ("string", 2), ("vlanlist", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainVlanAssignMode.setStatus('current')
hh3cDomainIdleCutEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainIdleCutEnable.setStatus('current')
hh3cDomainIdleCutMaxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainIdleCutMaxTime.setStatus('current')
hh3cDomainIdleCutMinFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10240000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainIdleCutMinFlow.setStatus('current')
hh3cDomainMessengerEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainMessengerEnable.setStatus('current')
hh3cDomainMessengerLimitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainMessengerLimitTime.setStatus('current')
hh3cDomainMessengerSpanTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainMessengerSpanTime.setStatus('current')
hh3cDomainSelfServiceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 11), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainSelfServiceEnable.setStatus('current')
hh3cDomainSelfServiceURL = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainSelfServiceURL.setStatus('current')
hh3cDomainAccFailureAction = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("reject", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainAccFailureAction.setStatus('current')
hh3cDomainRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainRowStatus.setStatus('current')
hh3cDomainCurrentAccessNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDomainCurrentAccessNum.setStatus('current')
hh3cDomainSchemeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2), )
if mibBuilder.loadTexts: hh3cDomainSchemeTable.setStatus('current')
hh3cDomainSchemeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1), ).setIndexNames((0, "HH3C-DOMAIN-MIB", "hh3cDomainName"), (0, "HH3C-DOMAIN-MIB", "hh3cDomainSchemeIndex"))
if mibBuilder.loadTexts: hh3cDomainSchemeEntry.setStatus('current')
hh3cDomainSchemeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cDomainSchemeIndex.setStatus('current')
hh3cDomainSchemeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 2), Hh3cModeOfDomainScheme()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainSchemeMode.setStatus('current')
hh3cDomainAuthSchemeName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainAuthSchemeName.setStatus('current')
hh3cDomainAcctSchemeName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainAcctSchemeName.setStatus('current')
hh3cDomainSchemeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainSchemeRowStatus.setStatus('current')
hh3cDomainSchemeAAAType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 6), Hh3cAAATypeDomainScheme()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainSchemeAAAType.setStatus('current')
hh3cDomainSchemeAAAName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainSchemeAAAName.setStatus('current')
hh3cDomainSchemeAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 8), Hh3cAccessModeofDomainScheme()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainSchemeAccessMode.setStatus('current')
hh3cDomainIpPoolTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3), )
if mibBuilder.loadTexts: hh3cDomainIpPoolTable.setStatus('current')
hh3cDomainIpPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1), ).setIndexNames((0, "HH3C-DOMAIN-MIB", "hh3cDomainName"), (0, "HH3C-DOMAIN-MIB", "hh3cDomainIpPoolNum"))
if mibBuilder.loadTexts: hh3cDomainIpPoolEntry.setStatus('current')
hh3cDomainIpPoolNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)))
if mibBuilder.loadTexts: hh3cDomainIpPoolNum.setStatus('current')
hh3cDomainIpPoolLowIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainIpPoolLowIpAddrType.setStatus('current')
hh3cDomainIpPoolLowIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainIpPoolLowIpAddr.setStatus('current')
hh3cDomainIpPoolLen = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainIpPoolLen.setStatus('current')
hh3cDomainIpPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDomainIpPoolRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-DOMAIN-MIB", hh3cDomainName=hh3cDomainName, hh3cDomainVlanAssignMode=hh3cDomainVlanAssignMode, hh3cDomainIpPoolLowIpAddr=hh3cDomainIpPoolLowIpAddr, hh3cDomainSchemeMode=hh3cDomainSchemeMode, hh3cDomainIpPoolRowStatus=hh3cDomainIpPoolRowStatus, hh3cDomain=hh3cDomain, hh3cDomainIpPoolLowIpAddrType=hh3cDomainIpPoolLowIpAddrType, Hh3cModeOfDomainScheme=Hh3cModeOfDomainScheme, PYSNMP_MODULE_ID=hh3cDomain, hh3cDomainControl=hh3cDomainControl, hh3cDomainSchemeAAAName=hh3cDomainSchemeAAAName, hh3cDomainIdleCutMinFlow=hh3cDomainIdleCutMinFlow, hh3cDomainSchemeEntry=hh3cDomainSchemeEntry, hh3cDomainIdleCutMaxTime=hh3cDomainIdleCutMaxTime, hh3cDomainMessengerEnable=hh3cDomainMessengerEnable, hh3cDomainSelfServiceEnable=hh3cDomainSelfServiceEnable, hh3cDomainRowStatus=hh3cDomainRowStatus, hh3cDomainCurrentAccessNum=hh3cDomainCurrentAccessNum, Hh3cAAATypeDomainScheme=Hh3cAAATypeDomainScheme, hh3cDomainMaxAccessNum=hh3cDomainMaxAccessNum, hh3cDomainIpPoolNum=hh3cDomainIpPoolNum, hh3cDomainTables=hh3cDomainTables, hh3cDomainInfoTable=hh3cDomainInfoTable, hh3cDomainAccFailureAction=hh3cDomainAccFailureAction, hh3cDomainIdleCutEnable=hh3cDomainIdleCutEnable, hh3cDomainDefault=hh3cDomainDefault, hh3cDomainSchemeIndex=hh3cDomainSchemeIndex, hh3cDomainSchemeTable=hh3cDomainSchemeTable, hh3cDomainSchemeAccessMode=hh3cDomainSchemeAccessMode, hh3cDomainMessengerLimitTime=hh3cDomainMessengerLimitTime, hh3cDomainSchemeAAAType=hh3cDomainSchemeAAAType, hh3cDomainAcctSchemeName=hh3cDomainAcctSchemeName, Hh3cAccessModeofDomainScheme=Hh3cAccessModeofDomainScheme, hh3cDomainIpPoolLen=hh3cDomainIpPoolLen, hh3cDomainIpPoolTable=hh3cDomainIpPoolTable, hh3cDomainSchemeRowStatus=hh3cDomainSchemeRowStatus, hh3cDomainMessengerSpanTime=hh3cDomainMessengerSpanTime, hh3cDomainIpPoolEntry=hh3cDomainIpPoolEntry, hh3cDomainInfoEntry=hh3cDomainInfoEntry, hh3cDomainSelfServiceURL=hh3cDomainSelfServiceURL, hh3cDomainAuthSchemeName=hh3cDomainAuthSchemeName, hh3cDomainState=hh3cDomainState)