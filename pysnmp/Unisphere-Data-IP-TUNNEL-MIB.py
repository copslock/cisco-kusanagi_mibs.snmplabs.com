#
# PySNMP MIB module Unisphere-Data-IP-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IP-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, IpAddress, TimeTicks, ObjectIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, Bits, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "TimeTicks", "ObjectIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "Bits", "Counter32", "MibIdentifier")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, UsdName = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex", "UsdName")
usdIpTunnelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51))
usdIpTunnelMIB.setRevisions(('2001-07-23 20:57',))
if mibBuilder.loadTexts: usdIpTunnelMIB.setLastUpdated('200107232057Z')
if mibBuilder.loadTexts: usdIpTunnelMIB.setOrganization('Unisphere Networks, Inc.')
usdIpTunnelInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1))
usdIpTunnelNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdIpTunnelNextIfIndex.setStatus('current')
usdIpTunnelInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2), )
if mibBuilder.loadTexts: usdIpTunnelInterfaceTable.setStatus('current')
usdIpTunnelInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelIfIndex"))
if mibBuilder.loadTexts: usdIpTunnelInterfaceEntry.setStatus('current')
usdIpTunnelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdIpTunnelIfIndex.setStatus('current')
usdIpTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelName.setStatus('current')
usdIpTunnelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ipTunnelModeGre", 0), ("ipTunnelModeDvmrp", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelMode.setStatus('current')
usdIpTunnelVirtualRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 4), UsdName().clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelVirtualRouter.setStatus('current')
usdIpTunnelChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelChecksum.setStatus('current')
usdIpTunnelMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1024, 10240)).clone(10240)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelMtu.setStatus('current')
usdIpTunnelDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelDestination.setStatus('current')
usdIpTunnelSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelSource.setStatus('current')
usdIpTunnelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdIpTunnelRowStatus.setStatus('current')
usdIpTunnelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2))
usdIpTunnelCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 1))
usdIpTunnelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 2))
usdIpTunnnelCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 1, 1)).setObjects(("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpTunnnelCompliance = usdIpTunnnelCompliance.setStatus('current')
usdIpTunnelInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 2, 1)).setObjects(("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelNextIfIndex"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelName"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelMode"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelVirtualRouter"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelChecksum"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelMtu"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelSource"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelDestination"), ("Unisphere-Data-IP-TUNNEL-MIB", "usdIpTunnelRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIpTunnelInterfaceGroup = usdIpTunnelInterfaceGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IP-TUNNEL-MIB", usdIpTunnelGroups=usdIpTunnelGroups, usdIpTunnelMIB=usdIpTunnelMIB, usdIpTunnelSource=usdIpTunnelSource, usdIpTunnelInterfaceEntry=usdIpTunnelInterfaceEntry, usdIpTunnnelCompliance=usdIpTunnnelCompliance, usdIpTunnelRowStatus=usdIpTunnelRowStatus, PYSNMP_MODULE_ID=usdIpTunnelMIB, usdIpTunnelInterfaceObjects=usdIpTunnelInterfaceObjects, usdIpTunnelMtu=usdIpTunnelMtu, usdIpTunnelVirtualRouter=usdIpTunnelVirtualRouter, usdIpTunnelConformance=usdIpTunnelConformance, usdIpTunnelDestination=usdIpTunnelDestination, usdIpTunnelNextIfIndex=usdIpTunnelNextIfIndex, usdIpTunnelInterfaceGroup=usdIpTunnelInterfaceGroup, usdIpTunnelName=usdIpTunnelName, usdIpTunnelChecksum=usdIpTunnelChecksum, usdIpTunnelIfIndex=usdIpTunnelIfIndex, usdIpTunnelInterfaceTable=usdIpTunnelInterfaceTable, usdIpTunnelMode=usdIpTunnelMode, usdIpTunnelCompliances=usdIpTunnelCompliances)
