#
# PySNMP MIB module TPLINK-MAC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-MAC-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, ModuleIdentity, Counter32, IpAddress, TimeTicks, MibIdentifier, ObjectIdentity, iso, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "ModuleIdentity", "Counter32", "IpAddress", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso", "Gauge32", "Unsigned32")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkMacVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 15))
tplinkMacVlanMIB.setRevisions(('2009-08-03 00:00',))
if mibBuilder.loadTexts: tplinkMacVlanMIB.setLastUpdated('200812160000Z')
if mibBuilder.loadTexts: tplinkMacVlanMIB.setOrganization('TPLINK')
tplinkMacVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1))
tplinkMacVlanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 2))
macVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1))
macVlanPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2))
macVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1), )
if mibBuilder.loadTexts: macVlanConfigTable.setStatus('current')
macVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-MAC-VLAN-MIB", "macAddr"))
if mibBuilder.loadTexts: macVlanEntry.setStatus('current')
macAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 1), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macAddr.setStatus('current')
macDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macDescription.setStatus('current')
macVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macVlanId.setStatus('current')
macVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 4), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macVlanStatus.setStatus('current')
macVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1), )
if mibBuilder.loadTexts: macVlanPortTable.setStatus('current')
macVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: macVlanPortEntry.setStatus('current')
macVlanPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: macVlanPortNumber.setStatus('current')
macVlanPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macVlanPortEnable.setStatus('current')
macVlanPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: macVlanPortLag.setStatus('current')
mibBuilder.exportSymbols("TPLINK-MAC-VLAN-MIB", tplinkMacVlanMIBObjects=tplinkMacVlanMIBObjects, tplinkMacVlanNotifications=tplinkMacVlanNotifications, macVlanPortEntry=macVlanPortEntry, macVlanPortEnable=macVlanPortEnable, PYSNMP_MODULE_ID=tplinkMacVlanMIB, macVlanPortTable=macVlanPortTable, macVlanEntry=macVlanEntry, macAddr=macAddr, macVlanPort=macVlanPort, macVlanConfigTable=macVlanConfigTable, macVlanPortNumber=macVlanPortNumber, macVlanPortLag=macVlanPortLag, macDescription=macDescription, macVlanStatus=macVlanStatus, macVlanId=macVlanId, macVlanConfig=macVlanConfig, tplinkMacVlanMIB=tplinkMacVlanMIB)
