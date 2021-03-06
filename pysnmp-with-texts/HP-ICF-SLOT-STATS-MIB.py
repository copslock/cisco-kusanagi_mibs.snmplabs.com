#
# PySNMP MIB module HP-ICF-SLOT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-SLOT-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitchStatistics, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitchStatistics")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Unsigned32, IpAddress, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, ObjectIdentity, NotificationType, TimeTicks, Counter32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "IpAddress", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "ObjectIdentity", "NotificationType", "TimeTicks", "Counter32", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfSlotStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20))
hpicfSlotStatsMIB.setRevisions(('2012-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfSlotStatsMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setLastUpdated('201201050000Z')
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setDescription('This MIB module describes objects for module related statistics in the HP Integrated Communication Facility product line.')
hpicfSlotStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1))
hpicfSlotStatsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2))
hpicfSlotStatsModuleCpuStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1), )
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatTable.setDescription('A list of CPU load statistics for the modules in the switch.')
hpicfSlotStatsModuleCpuStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatEntry.setDescription('An entry for CPU load statistics for the modules in the switch.')
hpicfSlotStatsModuleHwModel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleHwModel.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsModuleHwModel.setDescription('The model number of the Module.')
hpicfSlotStatsModuleSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleSerialNum.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsModuleSerialNum.setDescription('The serial number of the Module.')
hpicfSlotStatsModuleCpuStatCurrentPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatCurrentPercent.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatCurrentPercent.setDescription('CPU utilization in percent(%), over a short time span, updated at the interval hpicfSlotStatsModuleCpuStatUpdateFrequency. Current time span is 1 second.')
hpicfSlotStatsModuleCpuStatAveragePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatAveragePercent.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatAveragePercent.setDescription('The average CPU utilization in percent(%), over a long time span, updated at the interval hpicfSlotStatsModuleCpuStatUpdateFrequency. Current time span is 90 seconds.')
hpicfSlotStatsModuleCpuStatUpdateFrequency = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatUpdateFrequency.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatUpdateFrequency.setDescription('The interval in seconds in which the hpicfSlotStatsModuleCpuStatTable is updated.')
hpicfSlotStatsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1))
hpicfSlotStatsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2))
hpicfSlotStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1, 1)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleHwModel"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleSerialNum"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatCurrentPercent"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatAveragePercent"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatUpdateFrequency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSlotStatsGroup = hpicfSlotStatsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsGroup.setDescription('A collection of objects for SlotStat.')
hpicfSlotStatsFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 1)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSlotStatsFullCompliance1 = hpicfSlotStatsFullCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfSlotStatsFullCompliance1.setDescription('The compliance statement for SNMP entities which implement the HP-ICF-SLOT-STATS-MIB. Such an implementation can be monitored via SNMP. ')
hpicfModuleSlotStatsReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 2)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfModuleSlotStatsReadOnlyCompliance1 = hpicfModuleSlotStatsReadOnlyCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfModuleSlotStatsReadOnlyCompliance1.setDescription('The compliance statement for SNMP entities which implement the HP-ICF-SLOT-STATS-MIB without support for read-write (i.e. in read-only mode). ')
mibBuilder.exportSymbols("HP-ICF-SLOT-STATS-MIB", hpicfSlotStatsObjects=hpicfSlotStatsObjects, PYSNMP_MODULE_ID=hpicfSlotStatsMIB, hpicfSlotStatsMIB=hpicfSlotStatsMIB, hpicfSlotStatsModuleCpuStatEntry=hpicfSlotStatsModuleCpuStatEntry, hpicfSlotStatsModuleCpuStatUpdateFrequency=hpicfSlotStatsModuleCpuStatUpdateFrequency, hpicfSlotStatsGroups=hpicfSlotStatsGroups, hpicfSlotStatsGroup=hpicfSlotStatsGroup, hpicfSlotStatsModuleHwModel=hpicfSlotStatsModuleHwModel, hpicfSlotStatsModuleCpuStatAveragePercent=hpicfSlotStatsModuleCpuStatAveragePercent, hpicfSlotStatsCompliances=hpicfSlotStatsCompliances, hpicfModuleSlotStatsReadOnlyCompliance1=hpicfModuleSlotStatsReadOnlyCompliance1, hpicfSlotStatsModuleCpuStatTable=hpicfSlotStatsModuleCpuStatTable, hpicfSlotStatsFullCompliance1=hpicfSlotStatsFullCompliance1, hpicfSlotStatsConformance=hpicfSlotStatsConformance, hpicfSlotStatsModuleCpuStatCurrentPercent=hpicfSlotStatsModuleCpuStatCurrentPercent, hpicfSlotStatsModuleSerialNum=hpicfSlotStatsModuleSerialNum)
