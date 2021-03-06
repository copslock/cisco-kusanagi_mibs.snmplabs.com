#
# PySNMP MIB module HUAWEI-IPSESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-IPSESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:33:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, ModuleIdentity, Counter32, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks, NotificationType, ObjectIdentity, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "ModuleIdentity", "Counter32", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "Counter64", "MibIdentifier")
TextualConvention, RowStatus, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString", "TruthValue")
hwIpSessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184))
if mibBuilder.loadTexts: hwIpSessionMIB.setLastUpdated('200403041608Z')
if mibBuilder.loadTexts: hwIpSessionMIB.setOrganization('Huawei Technologies Co., Ltd. ')
hwIpSessionMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1))
hwIpSessIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1), )
if mibBuilder.loadTexts: hwIpSessIfCfgTable.setStatus('current')
hwIpSessIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1), ).setIndexNames((0, "HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgIfIndex"))
if mibBuilder.loadTexts: hwIpSessIfCfgEntry.setStatus('current')
hwIpSessIfCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwIpSessIfCfgIfIndex.setStatus('current')
hwIpSessIfCfgAuthDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessIfCfgAuthDomain.setStatus('current')
hwIpSessIfCfgNasPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessIfCfgNasPortType.setStatus('current')
hwIpSessIfCfgArpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 121)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessIfCfgArpInterval.setStatus('current')
hwIpSessIfCfgArpFailTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 11)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessIfCfgArpFailTimes.setStatus('current')
hwIpSessIfCfgOption82Policy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("insert", 2), ("replace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIpSessIfCfgOption82Policy.setStatus('current')
hwIpSessIfCfgServicePolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("option60", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessIfCfgServicePolicy.setStatus('current')
hwIpSessIfCfgVpn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessIfCfgVpn.setStatus('current')
hwIpSessIfCfgIpSessionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 18), EnabledStatus().clone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessIfCfgIpSessionEnable.setStatus('current')
hwIpSessIfCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwIpSessIfCfgRowStatus.setStatus('current')
hwIpSessUserCfgTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2))
hwIpSessUserPasswordType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessUserPasswordType.setStatus('current')
hwIpSessUserPassword = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessUserPassword.setStatus('current')
hwIpSessUserNameOption82 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("first", 2), ("second", 3), ("third", 4), ("fourth", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessUserNameOption82.setStatus('current')
hwIpSessUserNameIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("first", 2), ("second", 3), ("third", 4), ("fourth", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessUserNameIP.setStatus('current')
hwIpSessUserNameSysName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("first", 2), ("second", 3), ("third", 4), ("fourth", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessUserNameSysName.setStatus('current')
hwIpSessUserNameMac = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("first", 2), ("second", 3), ("third", 4), ("fourth", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwIpSessUserNameMac.setStatus('current')
hwIpSessionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3))
hwIpSessionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 1))
hwIpSessionCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 1, 1)).setObjects(("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgGroup"), ("HUAWEI-IPSESSION-MIB", "hwIpSessUserCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpSessionCompliance = hwIpSessionCompliance.setStatus('current')
hwIpSessionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 2))
hwIpSessIfCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 2, 1)).setObjects(("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgAuthDomain"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgNasPortType"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgArpInterval"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgArpFailTimes"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgOption82Policy"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgServicePolicy"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgVpn"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgIpSessionEnable"), ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpSessIfCfgGroup = hwIpSessIfCfgGroup.setStatus('current')
hwIpSessUserCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 2, 2)).setObjects(("HUAWEI-IPSESSION-MIB", "hwIpSessUserPasswordType"), ("HUAWEI-IPSESSION-MIB", "hwIpSessUserPassword"), ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameOption82"), ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameIP"), ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameSysName"), ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpSessUserCfgGroup = hwIpSessUserCfgGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-IPSESSION-MIB", hwIpSessIfCfgRowStatus=hwIpSessIfCfgRowStatus, hwIpSessIfCfgOption82Policy=hwIpSessIfCfgOption82Policy, hwIpSessIfCfgAuthDomain=hwIpSessIfCfgAuthDomain, hwIpSessionCompliances=hwIpSessionCompliances, hwIpSessUserNameSysName=hwIpSessUserNameSysName, hwIpSessUserCfgTable=hwIpSessUserCfgTable, hwIpSessIfCfgTable=hwIpSessIfCfgTable, hwIpSessIfCfgNasPortType=hwIpSessIfCfgNasPortType, hwIpSessionCompliance=hwIpSessionCompliance, hwIpSessUserNameOption82=hwIpSessUserNameOption82, hwIpSessionConformance=hwIpSessionConformance, hwIpSessIfCfgIpSessionEnable=hwIpSessIfCfgIpSessionEnable, hwIpSessionMibObjects=hwIpSessionMibObjects, hwIpSessIfCfgIfIndex=hwIpSessIfCfgIfIndex, hwIpSessIfCfgServicePolicy=hwIpSessIfCfgServicePolicy, hwIpSessUserNameIP=hwIpSessUserNameIP, hwIpSessionMIB=hwIpSessionMIB, hwIpSessUserNameMac=hwIpSessUserNameMac, hwIpSessUserPasswordType=hwIpSessUserPasswordType, hwIpSessIfCfgArpInterval=hwIpSessIfCfgArpInterval, hwIpSessIfCfgArpFailTimes=hwIpSessIfCfgArpFailTimes, hwIpSessIfCfgEntry=hwIpSessIfCfgEntry, hwIpSessUserPassword=hwIpSessUserPassword, hwIpSessIfCfgVpn=hwIpSessIfCfgVpn, hwIpSessIfCfgGroup=hwIpSessIfCfgGroup, hwIpSessionGroups=hwIpSessionGroups, hwIpSessUserCfgGroup=hwIpSessUserCfgGroup, PYSNMP_MODULE_ID=hwIpSessionMIB)
