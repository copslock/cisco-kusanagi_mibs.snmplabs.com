#
# PySNMP MIB module CISCO-PROP-ATM-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PROP-ATM-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, MibIdentifier, Counter32, iso, Integer32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "iso", "Integer32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPropAtmIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 319))
ciscoPropAtmIfMIB.setRevisions(('2002-12-04 00:00',))
if mibBuilder.loadTexts: ciscoPropAtmIfMIB.setLastUpdated('200212040000Z')
if mibBuilder.loadTexts: ciscoPropAtmIfMIB.setOrganization('Cisco Systems, Inc.')
ciscoPropAtmIfMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 319, 0))
ciscoPropAtmIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 319, 1))
cpAtmIfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1))
cpAtmIfVirtualPortStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2))
cpAtmIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1, 1), )
if mibBuilder.loadTexts: cpAtmIfConfigTable.setStatus('current')
cpAtmIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpAtmIfConfigEntry.setStatus('current')
cpAtmIfMaxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(7000000)).setUnits('cells-per-second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpAtmIfMaxBandwidth.setStatus('current')
cpAtmIfStatsEgressTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1), )
if mibBuilder.loadTexts: cpAtmIfStatsEgressTable.setStatus('current')
cpAtmIfStatsEgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpAtmIfStatsEgressEntry.setStatus('current')
cpAtmIfEgrRcvClp0Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfEgrRcvClp0Cells.setStatus('current')
cpAtmIfEgrRcvClp1Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfEgrRcvClp1Cells.setStatus('current')
cpAtmIfEgrClp0DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfEgrClp0DiscCells.setStatus('current')
cpAtmIfEgrClp1DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfEgrClp1DiscCells.setStatus('current')
cpAtmIfEgrRcvOAMCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfEgrRcvOAMCells.setStatus('current')
cpAtmIfEgrRcvEFCICells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfEgrRcvEFCICells.setStatus('current')
cpAtmIfHCEgrRcvClp0Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCEgrRcvClp0Cells.setStatus('current')
cpAtmIfHCEgrRcvClp1Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCEgrRcvClp1Cells.setStatus('current')
cpAtmIfHCEgrClp0DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCEgrClp0DiscCells.setStatus('current')
cpAtmIfHCEgrClp1DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCEgrClp1DiscCells.setStatus('current')
cpAtmIfHCEgrRcvOAMCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCEgrRcvOAMCells.setStatus('current')
cpAtmIfHCEgrRcvEFCICells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCEgrRcvEFCICells.setStatus('current')
cpAtmIfEgressIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2), )
if mibBuilder.loadTexts: cpAtmIfEgressIntervalTable.setStatus('current')
cpAtmIfEgressIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgressIntervalNumber"))
if mibBuilder.loadTexts: cpAtmIfEgressIntervalEntry.setStatus('current')
cpAtmIfEgressIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: cpAtmIfEgressIntervalNumber.setStatus('current')
cpAtmIfIntEgrRcvClp0Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIntEgrRcvClp0Cells.setStatus('current')
cpAtmIfIntEgrRcvClp1Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIntEgrRcvClp1Cells.setStatus('current')
cpAtmIfIntEgrClp0DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIntEgrClp0DiscCells.setStatus('current')
cpAtmIfIntEgrClp1DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIntEgrClp1DiscCells.setStatus('current')
cpAtmIfIntEgrRcvOAMCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIntEgrRcvOAMCells.setStatus('current')
cpAtmIfIntEgrRcvEFCICells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIntEgrRcvEFCICells.setStatus('current')
cpAtmIfHCIntEgrRcvClp0Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIntEgrRcvClp0Cells.setStatus('current')
cpAtmIfHCIntEgrRcvClp1Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIntEgrRcvClp1Cells.setStatus('current')
cpAtmIfHCIntEgrClp0DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIntEgrClp0DiscCells.setStatus('current')
cpAtmIfHCIntEgrClp1DiscCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIntEgrClp1DiscCells.setStatus('current')
cpAtmIfHCIntEgrRcvOAMCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIntEgrRcvOAMCells.setStatus('current')
cpAtmIfHCIntEgrRcvEFCICells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIntEgrRcvEFCICells.setStatus('current')
cpAtmIfStatsIngressTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3), )
if mibBuilder.loadTexts: cpAtmIfStatsIngressTable.setStatus('current')
cpAtmIfStatsIngressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cpAtmIfStatsIngressEntry.setStatus('current')
cpAtmIfIngXmtClp0Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIngXmtClp0Cells.setStatus('current')
cpAtmIfIngXmtClp1Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIngXmtClp1Cells.setStatus('current')
cpAtmIfIngXmtEFCICells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIngXmtEFCICells.setStatus('current')
cpAtmIfIngXmtOAMCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfIngXmtOAMCells.setStatus('current')
cpAtmIfHCIngXmtClp0Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIngXmtClp0Cells.setStatus('current')
cpAtmIfHCIngXmtClp1Cells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIngXmtClp1Cells.setStatus('current')
cpAtmIfHCIngXmtEFCICells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIngXmtEFCICells.setStatus('current')
cpAtmIfHCIngXmtOAMCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 319, 1, 2, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpAtmIfHCIngXmtOAMCells.setStatus('current')
cpAtmIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 319, 2))
cpAtmIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 1))
cpAtmIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2))
cpAtmIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 1, 1)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfConfigGroup"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgressStatMIBGroup"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgressIntervalMIBGroup"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngressStatMIBGroup"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgressStatMIBGroup"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgressIntervalMIBGroup"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngressStatMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfMIBCompliance = cpAtmIfMIBCompliance.setStatus('current')
cpAtmIfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 1)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfMaxBandwidth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfConfigGroup = cpAtmIfConfigGroup.setStatus('current')
cpAtmIfEgressStatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 2)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvClp0Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvClp1Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrClp0DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrClp1DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvOAMCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfEgrRcvEFCICells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfEgressStatMIBGroup = cpAtmIfEgressStatMIBGroup.setStatus('current')
cpAtmIfEgressIntervalMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 3)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvClp0Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvClp1Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrClp0DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrClp1DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvOAMCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIntEgrRcvEFCICells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfEgressIntervalMIBGroup = cpAtmIfEgressIntervalMIBGroup.setStatus('current')
cpAtmIfIngressStatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 4)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtClp0Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtClp1Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtEFCICells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfIngXmtOAMCells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfIngressStatMIBGroup = cpAtmIfIngressStatMIBGroup.setStatus('current')
cpAtmIfHCEgressStatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 5)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvClp0Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvClp1Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrClp0DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrClp1DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvOAMCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCEgrRcvEFCICells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfHCEgressStatMIBGroup = cpAtmIfHCEgressStatMIBGroup.setStatus('current')
cpAtmIfHCEgressIntervalMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 6)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvClp0Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvClp1Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrClp0DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrClp1DiscCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvOAMCells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIntEgrRcvEFCICells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfHCEgressIntervalMIBGroup = cpAtmIfHCEgressIntervalMIBGroup.setStatus('current')
cpAtmIfHCIngressStatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 319, 2, 2, 7)).setObjects(("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtClp0Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtClp1Cells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtEFCICells"), ("CISCO-PROP-ATM-IF-MIB", "cpAtmIfHCIngXmtOAMCells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpAtmIfHCIngressStatMIBGroup = cpAtmIfHCIngressStatMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PROP-ATM-IF-MIB", cpAtmIfIntEgrRcvOAMCells=cpAtmIfIntEgrRcvOAMCells, cpAtmIfHCIntEgrRcvClp0Cells=cpAtmIfHCIntEgrRcvClp0Cells, cpAtmIfHCEgrRcvOAMCells=cpAtmIfHCEgrRcvOAMCells, cpAtmIfIngXmtOAMCells=cpAtmIfIngXmtOAMCells, cpAtmIfHCIntEgrRcvClp1Cells=cpAtmIfHCIntEgrRcvClp1Cells, cpAtmIfHCEgressIntervalMIBGroup=cpAtmIfHCEgressIntervalMIBGroup, cpAtmIfEgressStatMIBGroup=cpAtmIfEgressStatMIBGroup, cpAtmIfHCIngXmtEFCICells=cpAtmIfHCIngXmtEFCICells, cpAtmIfMIBCompliances=cpAtmIfMIBCompliances, cpAtmIfHCEgrClp0DiscCells=cpAtmIfHCEgrClp0DiscCells, cpAtmIfConfigGroup=cpAtmIfConfigGroup, cpAtmIfIntEgrRcvClp0Cells=cpAtmIfIntEgrRcvClp0Cells, cpAtmIfHCIngXmtClp0Cells=cpAtmIfHCIngXmtClp0Cells, cpAtmIfMIBCompliance=cpAtmIfMIBCompliance, cpAtmIfEgrClp1DiscCells=cpAtmIfEgrClp1DiscCells, cpAtmIfStatsIngressTable=cpAtmIfStatsIngressTable, cpAtmIfStatsEgressEntry=cpAtmIfStatsEgressEntry, cpAtmIfHCIntEgrRcvEFCICells=cpAtmIfHCIntEgrRcvEFCICells, cpAtmIfEgressIntervalMIBGroup=cpAtmIfEgressIntervalMIBGroup, ciscoPropAtmIfMIBObjects=ciscoPropAtmIfMIBObjects, cpAtmIfStatsIngressEntry=cpAtmIfStatsIngressEntry, ciscoPropAtmIfMIB=ciscoPropAtmIfMIB, ciscoPropAtmIfMIBNotifs=ciscoPropAtmIfMIBNotifs, cpAtmIfEgrRcvClp1Cells=cpAtmIfEgrRcvClp1Cells, cpAtmIfEgressIntervalNumber=cpAtmIfEgressIntervalNumber, cpAtmIfIntEgrRcvClp1Cells=cpAtmIfIntEgrRcvClp1Cells, cpAtmIfIntEgrClp0DiscCells=cpAtmIfIntEgrClp0DiscCells, cpAtmIfConfigEntry=cpAtmIfConfigEntry, cpAtmIfHCIntEgrRcvOAMCells=cpAtmIfHCIntEgrRcvOAMCells, cpAtmIfHCIntEgrClp1DiscCells=cpAtmIfHCIntEgrClp1DiscCells, cpAtmIfIntEgrRcvEFCICells=cpAtmIfIntEgrRcvEFCICells, cpAtmIfHCEgressStatMIBGroup=cpAtmIfHCEgressStatMIBGroup, cpAtmIfConfig=cpAtmIfConfig, cpAtmIfIntEgrClp1DiscCells=cpAtmIfIntEgrClp1DiscCells, cpAtmIfMIBGroups=cpAtmIfMIBGroups, cpAtmIfEgrRcvEFCICells=cpAtmIfEgrRcvEFCICells, cpAtmIfHCIntEgrClp0DiscCells=cpAtmIfHCIntEgrClp0DiscCells, PYSNMP_MODULE_ID=ciscoPropAtmIfMIB, cpAtmIfEgressIntervalTable=cpAtmIfEgressIntervalTable, cpAtmIfIngXmtClp0Cells=cpAtmIfIngXmtClp0Cells, cpAtmIfIngressStatMIBGroup=cpAtmIfIngressStatMIBGroup, cpAtmIfHCIngressStatMIBGroup=cpAtmIfHCIngressStatMIBGroup, cpAtmIfStatsEgressTable=cpAtmIfStatsEgressTable, cpAtmIfEgressIntervalEntry=cpAtmIfEgressIntervalEntry, cpAtmIfVirtualPortStats=cpAtmIfVirtualPortStats, cpAtmIfHCEgrClp1DiscCells=cpAtmIfHCEgrClp1DiscCells, cpAtmIfEgrRcvOAMCells=cpAtmIfEgrRcvOAMCells, cpAtmIfIngXmtClp1Cells=cpAtmIfIngXmtClp1Cells, cpAtmIfHCEgrRcvClp1Cells=cpAtmIfHCEgrRcvClp1Cells, cpAtmIfHCEgrRcvClp0Cells=cpAtmIfHCEgrRcvClp0Cells, cpAtmIfEgrClp0DiscCells=cpAtmIfEgrClp0DiscCells, cpAtmIfHCIngXmtOAMCells=cpAtmIfHCIngXmtOAMCells, cpAtmIfIngXmtEFCICells=cpAtmIfIngXmtEFCICells, cpAtmIfHCIngXmtClp1Cells=cpAtmIfHCIngXmtClp1Cells, cpAtmIfEgrRcvClp0Cells=cpAtmIfEgrRcvClp0Cells, cpAtmIfMaxBandwidth=cpAtmIfMaxBandwidth, cpAtmIfConfigTable=cpAtmIfConfigTable, cpAtmIfMIBConformance=cpAtmIfMIBConformance, cpAtmIfHCEgrRcvEFCICells=cpAtmIfHCEgrRcvEFCICells)