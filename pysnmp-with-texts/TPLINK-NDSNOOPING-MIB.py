#
# PySNMP MIB module TPLINK-NDSNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-NDSNOOPING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, Counter64, Integer32, ObjectIdentity, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, MibIdentifier, Unsigned32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Counter64", "Integer32", "ObjectIdentity", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "MibIdentifier", "Unsigned32", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkNdSnoopingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 92))
tplinkNdSnoopingMIB.setRevisions(('2012-12-17 10:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkNdSnoopingMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkNdSnoopingMIB.setLastUpdated('201212171014Z')
if mibBuilder.loadTexts: tplinkNdSnoopingMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkNdSnoopingMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkNdSnoopingMIB.setDescription('Private MIB for ND Snooping configuration.')
tplinkNdSnoopingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1))
tplinkNdSnoopingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 2))
ndSnoopingGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1))
ndSnoopingPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3))
ndSnoopingEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndSnoopingEnable.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingEnable.setDescription('0. disable 1. enable Enable or disable the ND Snooping function globally.')
ndSnoopingVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2), )
if mibBuilder.loadTexts: ndSnoopingVlanConfigTable.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingVlanConfigTable.setDescription('Here you can view and modify the ND Snooping VLAN config table.')
ndSnoopingVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1), ).setIndexNames((0, "TPLINK-NDSNOOPING-MIB", "ndSnoopingVlanId"))
if mibBuilder.loadTexts: ndSnoopingVlanConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingVlanConfigEntry.setDescription('An entry contains of the ND Snooping function enable status information of a VLAN.')
ndSnoopingVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ndSnoopingVlanId.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingVlanId.setDescription('Enter the ID number of VLAN,1-4094.')
ndSnoopingVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ndSnoopingVlanStatus.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingVlanStatus.setDescription('0. disable 1. enable Enable or disable ND Snooping function in specified VLAN. ')
ndSnoopingPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1), )
if mibBuilder.loadTexts: ndSnoopingPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingPortConfigTable.setDescription('A list of ND Snooping port config entries. Here you can configure the port parameters for the ND Snooping.')
ndSnoopingPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ndSnoopingPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingPortConfigEntry.setDescription('An entry contains of the information of ND Snooping port config.')
ndSnoopingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndSnoopingPort.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingPort.setDescription('Display port number')
ndSnoopingPortConfigMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ndSnoopingPortConfigMaxEntry.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingPortConfigMaxEntry.setDescription('Set the maxinum entry of the interface.')
ndSnoopingPortConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 92, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ndSnoopingPortConfigPortLag.setStatus('current')
if mibBuilder.loadTexts: ndSnoopingPortConfigPortLag.setDescription('The LAG to which the port belongs to.')
mibBuilder.exportSymbols("TPLINK-NDSNOOPING-MIB", ndSnoopingEnable=ndSnoopingEnable, ndSnoopingPortConfigMaxEntry=ndSnoopingPortConfigMaxEntry, ndSnoopingVlanStatus=ndSnoopingVlanStatus, ndSnoopingPort=ndSnoopingPort, ndSnoopingPortConfig=ndSnoopingPortConfig, ndSnoopingPortConfigEntry=ndSnoopingPortConfigEntry, PYSNMP_MODULE_ID=tplinkNdSnoopingMIB, ndSnoopingPortConfigTable=ndSnoopingPortConfigTable, ndSnoopingVlanId=ndSnoopingVlanId, tplinkNdSnoopingMIBObjects=tplinkNdSnoopingMIBObjects, tplinkNdSnoopingMIB=tplinkNdSnoopingMIB, ndSnoopingPortConfigPortLag=ndSnoopingPortConfigPortLag, tplinkNdSnoopingNotifications=tplinkNdSnoopingNotifications, ndSnoopingVlanConfigTable=ndSnoopingVlanConfigTable, ndSnoopingGlobalConfig=ndSnoopingGlobalConfig, ndSnoopingVlanConfigEntry=ndSnoopingVlanConfigEntry)
