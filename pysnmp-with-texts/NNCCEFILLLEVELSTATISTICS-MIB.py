#
# PySNMP MIB module NNCCEFILLLEVELSTATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCCEFILLLEVELSTATISTICS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:22:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nncExtensions, = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, TimeTicks, iso, Unsigned32, MibIdentifier, Integer32, Gauge32, IpAddress, ObjectIdentity, Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "iso", "Unsigned32", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nncCEFillLevelStatistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 47))
if mibBuilder.loadTexts: nncCEFillLevelStatistics.setLastUpdated('9708271200Z')
if mibBuilder.loadTexts: nncCEFillLevelStatistics.setOrganization('Newbridge Networks Corporation')
if mibBuilder.loadTexts: nncCEFillLevelStatistics.setContactInfo('Newbridge Networks Corporation Postal: 600 March Road Kanata, Ontario Canada K2K 2E6 Phone: +1 613 591 3600 Fax: +1 613 591 3680')
if mibBuilder.loadTexts: nncCEFillLevelStatistics.setDescription('This module contains definitions for monitoring aal1 fill level statistics.')
nncCEFillLevelStatisticsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 47, 1))
nncCEFillLevelStatisticsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 47, 2))
nncCEFillLevelStatisticsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 47, 3))
nncCEFillLevelStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1), )
if mibBuilder.loadTexts: nncCEFillLevelStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: nncCEFillLevelStatisticsTable.setDescription('The nncCEFillLevelStatisticsTable contains objects for monitoring the maximum and minimum fill levels reached by the playout buffer')
nncCEFillLevelStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncCEFillLevelStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: nncCEFillLevelStatisticsEntry.setDescription('An entry in the nncCEFillLevelStatisticsTable.')
nncCEMinFillLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncCEMinFillLevel.setStatus('current')
if mibBuilder.loadTexts: nncCEMinFillLevel.setDescription('This value represents the minimum fill level reached by the playout buffer measured in micro seconds.')
nncCEMaxFillLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncCEMaxFillLevel.setStatus('current')
if mibBuilder.loadTexts: nncCEMaxFillLevel.setDescription('This value represents the maximum fill level reached by the playout buffer measured in micro seconds.')
nncCERawFillLevelStatisticsGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 47, 2, 1)).setObjects(("NNCCEFILLLEVELSTATISTICS-MIB", "nncCEMinFillLevel"), ("NNCCEFILLLEVELSTATISTICS-MIB", "nncCEMaxFillLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncCERawFillLevelStatisticsGroups = nncCERawFillLevelStatisticsGroups.setStatus('current')
if mibBuilder.loadTexts: nncCERawFillLevelStatisticsGroups.setDescription('Collection of objects providing raw fill stats.')
nncCEFillLevelStatisticsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 123, 3, 47, 3, 1)).setObjects(("NNCCEFILLLEVELSTATISTICS-MIB", "nncCERawFillLevelStatisticsGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncCEFillLevelStatisticsCompliance = nncCEFillLevelStatisticsCompliance.setStatus('current')
if mibBuilder.loadTexts: nncCEFillLevelStatisticsCompliance.setDescription('The compliance statement for Newbridge SNMP.')
mibBuilder.exportSymbols("NNCCEFILLLEVELSTATISTICS-MIB", nncCEFillLevelStatisticsCompliance=nncCEFillLevelStatisticsCompliance, nncCEMinFillLevel=nncCEMinFillLevel, nncCEFillLevelStatisticsCompliances=nncCEFillLevelStatisticsCompliances, nncCEFillLevelStatisticsTable=nncCEFillLevelStatisticsTable, nncCEFillLevelStatistics=nncCEFillLevelStatistics, nncCEFillLevelStatisticsObjects=nncCEFillLevelStatisticsObjects, nncCEMaxFillLevel=nncCEMaxFillLevel, PYSNMP_MODULE_ID=nncCEFillLevelStatistics, nncCEFillLevelStatisticsGroups=nncCEFillLevelStatisticsGroups, nncCEFillLevelStatisticsEntry=nncCEFillLevelStatisticsEntry, nncCERawFillLevelStatisticsGroups=nncCERawFillLevelStatisticsGroups)
