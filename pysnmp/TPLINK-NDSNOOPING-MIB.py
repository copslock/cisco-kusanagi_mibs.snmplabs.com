#
# PySNMP MIB module TPLINK-NDSNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-NDSNOOPING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Unsigned32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Bits, Counter64, Integer32, MibIdentifier, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Unsigned32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Bits", "Counter64", "Integer32", "MibIdentifier", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkNdSnoopingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 92))
tplinkNdSnoopingMIB.setRevisions(('2012-12-17 10:14',))
if mibBuilder.loadTexts: tplinkNdSnoopingMIB.setLastUpdated('201212171014Z')
if mibBuilder.loadTexts: tplinkNdSnoopingMIB.setOrganization('TPLINK')
tplinkNdSnoopingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1))
tplinkNdSnoopingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 2))
ndSnoopingGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1))
ndSnoopingPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3))
ndSnoopingEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndSnoopingEnable.setStatus('current')
ndSnoopingVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2), )
if mibBuilder.loadTexts: ndSnoopingVlanConfigTable.setStatus('current')
ndSnoopingVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1), ).setIndexNames((0, "TPLINK-NDSNOOPING-MIB", "ndSnoopingVlanId"))
if mibBuilder.loadTexts: ndSnoopingVlanConfigEntry.setStatus('current')
ndSnoopingVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ndSnoopingVlanId.setStatus('current')
ndSnoopingVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ndSnoopingVlanStatus.setStatus('current')
ndSnoopingPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1), )
if mibBuilder.loadTexts: ndSnoopingPortConfigTable.setStatus('current')
ndSnoopingPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ndSnoopingPortConfigEntry.setStatus('current')
ndSnoopingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndSnoopingPort.setStatus('current')
ndSnoopingPortConfigMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndSnoopingPortConfigMaxEntry.setStatus('current')
ndSnoopingPortConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndSnoopingPortConfigPortLag.setStatus('current')
mibBuilder.exportSymbols("TPLINK-NDSNOOPING-MIB", tplinkNdSnoopingNotifications=tplinkNdSnoopingNotifications, tplinkNdSnoopingMIBObjects=tplinkNdSnoopingMIBObjects, ndSnoopingPortConfigTable=ndSnoopingPortConfigTable, ndSnoopingGlobalConfig=ndSnoopingGlobalConfig, ndSnoopingVlanStatus=ndSnoopingVlanStatus, ndSnoopingPortConfigEntry=ndSnoopingPortConfigEntry, ndSnoopingPort=ndSnoopingPort, PYSNMP_MODULE_ID=tplinkNdSnoopingMIB, ndSnoopingPortConfigMaxEntry=ndSnoopingPortConfigMaxEntry, ndSnoopingPortConfigPortLag=ndSnoopingPortConfigPortLag, ndSnoopingEnable=ndSnoopingEnable, ndSnoopingVlanConfigEntry=ndSnoopingVlanConfigEntry, ndSnoopingVlanConfigTable=ndSnoopingVlanConfigTable, ndSnoopingVlanId=ndSnoopingVlanId, tplinkNdSnoopingMIB=tplinkNdSnoopingMIB, ndSnoopingPortConfig=ndSnoopingPortConfig)
