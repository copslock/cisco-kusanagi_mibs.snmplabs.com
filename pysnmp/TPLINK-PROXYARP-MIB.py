#
# PySNMP MIB module TPLINK-PROXYARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-PROXYARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, TimeTicks, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ModuleIdentity, Counter32, ObjectIdentity, Unsigned32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "TimeTicks", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ModuleIdentity", "Counter32", "ObjectIdentity", "Unsigned32", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkProxyArpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 37))
tplinkProxyArpMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkProxyArpMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkProxyArpMIB.setOrganization('TPLINK')
tplinkProxyArpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1))
tplinkProxyArpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 2))
tpProxyArpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1))
tpProxyArpTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1), )
if mibBuilder.loadTexts: tpProxyArpTable.setStatus('current')
tpProxyArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1), ).setIndexNames((0, "TPLINK-PROXYARP-MIB", "tpProxyArpVlanId"))
if mibBuilder.loadTexts: tpProxyArpEntry.setStatus('current')
tpProxyArpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpVlanId.setStatus('current')
tpProxyArpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpIpAddr.setStatus('current')
tpProxyArpIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpIpMask.setStatus('current')
tpProxyArpInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpInterfaceName.setStatus('current')
tpProxyArpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpProxyArpEnable.setStatus('current')
mibBuilder.exportSymbols("TPLINK-PROXYARP-MIB", tpProxyArpTable=tpProxyArpTable, tpProxyArpEnable=tpProxyArpEnable, tplinkProxyArpNotifications=tplinkProxyArpNotifications, tpProxyArpInterfaceName=tpProxyArpInterfaceName, tplinkProxyArpMIB=tplinkProxyArpMIB, tpProxyArpEntry=tpProxyArpEntry, tplinkProxyArpMIBObjects=tplinkProxyArpMIBObjects, PYSNMP_MODULE_ID=tplinkProxyArpMIB, tpProxyArpConfig=tpProxyArpConfig, tpProxyArpIpAddr=tpProxyArpIpAddr, tpProxyArpIpMask=tpProxyArpIpMask, tpProxyArpVlanId=tpProxyArpVlanId)
