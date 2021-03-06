#
# PySNMP MIB module IPV4-RIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV4-RIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apIpv4Rip, = mibBuilder.importSymbols("APENT-MIB", "apIpv4Rip")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, TimeTicks, NotificationType, Unsigned32, ObjectIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ModuleIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "ObjectIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ModuleIdentity", "MibIdentifier", "iso")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
apIpv4RipMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 1))
if mibBuilder.loadTexts: apIpv4RipMib.setLastUpdated('9805112000Z')
if mibBuilder.loadTexts: apIpv4RipMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apIpv4RipMib.setContactInfo('Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apIpv4RipMib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for the Routing Information Protocol')
apIpv4RipRedistributeStatic = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipRedistributeStatic.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipRedistributeStatic.setDescription('If enabled, static routes will be advertised by RIP.')
apIpv4RipStaticMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipStaticMetric.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipStaticMetric.setDescription('If static routes are advertised by RIP, this is the metric to use when advertising the routes.')
apIpv4RipRedistributeOspf = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipRedistributeOspf.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipRedistributeOspf.setDescription('If enabled, OSPF routes will be advertised by RIP.')
apIpv4RipOspfMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipOspfMetric.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipOspfMetric.setDescription('If OSPF routes are advertised by RIP, this is the metric to use when advertising the routes.')
apIpv4RipRedistributeLocal = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipRedistributeLocal.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipRedistributeLocal.setDescription('If enabled, local routes will be advertised by RIP.')
apIpv4RipLocalMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipLocalMetric.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipLocalMetric.setDescription('If local routes are advertised by RIP, this is the metric to use when advertising the routes.')
apIpv4RipEqualCostRoutes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipEqualCostRoutes.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipEqualCostRoutes.setDescription('The maximum number of equal-cost routes RIP can use.')
apIpv4RipRedistributeFirewall = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipRedistributeFirewall.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipRedistributeFirewall.setDescription('If enabled, firewall routes will be advertised by RIP.')
apIpv4RipFirewallMetric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4RipFirewallMetric.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipFirewallMetric.setDescription('If firewall routes are advertised by RIP, this is the metric to use when advertising the routes.')
apIpv4RipAdvRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8), )
if mibBuilder.loadTexts: apIpv4RipAdvRouteTable.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipAdvRouteTable.setDescription('A list of routes that are advertised via all RIP interfaces.')
apIpv4RipAdvRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1), ).setIndexNames((0, "IPV4-RIP-MIB", "apIpv4RipAdvRoutePrefix"), (0, "IPV4-RIP-MIB", "apIpv4RipAdvRoutePrefixLen"))
if mibBuilder.loadTexts: apIpv4RipAdvRouteEntry.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipAdvRouteEntry.setDescription('A single route to advertise via all RIP interfaces.')
apIpv4RipAdvRoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RipAdvRoutePrefix.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipAdvRoutePrefix.setDescription('The route prefix to be advertised.')
apIpv4RipAdvRoutePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RipAdvRoutePrefixLen.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipAdvRoutePrefixLen.setDescription('The network prefix length associated with this route.')
apIpv4RipAdvRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RipAdvRouteMetric.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipAdvRouteMetric.setDescription('The metric to use when advertising this route.')
apIpv4RipAdvRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RipAdvRouteStatus.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipAdvRouteStatus.setDescription('(fill in later)')
apIpv4RipIfAdvRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9), )
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteTable.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteTable.setDescription('A list of routes that are advertised via a specific RIP interface.')
apIpv4RipIfAdvRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1), ).setIndexNames((0, "IPV4-RIP-MIB", "apIpv4RipIfAdvRouteAddress"), (0, "IPV4-RIP-MIB", "apIpv4RipIfAdvRoutePrefix"), (0, "IPV4-RIP-MIB", "apIpv4RipIfAdvRoutePrefixLen"))
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteEntry.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteEntry.setDescription('A single route to advertise via a specific RIP interface.')
apIpv4RipIfAdvRouteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteAddress.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteAddress.setDescription('The address of the RIP interface. If this is a valid unicast IP address, the interface is numbered. Otherwise, it indicates the ifIndex of an unnumbered interface.')
apIpv4RipIfAdvRoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RipIfAdvRoutePrefix.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAdvRoutePrefix.setDescription('The route prefix to be advertised.')
apIpv4RipIfAdvRoutePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RipIfAdvRoutePrefixLen.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAdvRoutePrefixLen.setDescription('The network prefix length associated with this route.')
apIpv4RipIfAdvRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteMetric.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteMetric.setDescription('The metric to use when advertising this route.')
apIpv4RipIfAdvRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 9, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteStatus.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAdvRouteStatus.setDescription('(fill in later)')
apIpv4RipIfTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10), )
if mibBuilder.loadTexts: apIpv4RipIfTable.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfTable.setDescription('Per-interface RIP information.')
apIpv4RipIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1), ).setIndexNames((0, "IPV4-RIP-MIB", "apIpv4RipIfAddress"))
if mibBuilder.loadTexts: apIpv4RipIfEntry.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfEntry.setDescription('Information for a single RIP interface.')
apIpv4RipIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4RipIfAddress.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfAddress.setDescription('The address of the RIP interface. If this is a valid unicast IP address, the interface is numbered. Otherwise, it indicates the ifIndex of an unnumbered interface.')
apIpv4RipIfLogTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RipIfLogTx.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfLogTx.setDescription('If true, information will be written to the system log for each RIP packet transmitted.')
apIpv4RipIfLogRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 3, 1, 10, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4RipIfLogRx.setStatus('current')
if mibBuilder.loadTexts: apIpv4RipIfLogRx.setDescription('If true, information will be written to the system log for each RIP packet received.')
mibBuilder.exportSymbols("IPV4-RIP-MIB", apIpv4RipIfTable=apIpv4RipIfTable, apIpv4RipIfAdvRouteTable=apIpv4RipIfAdvRouteTable, apIpv4RipIfAdvRouteAddress=apIpv4RipIfAdvRouteAddress, apIpv4RipLocalMetric=apIpv4RipLocalMetric, apIpv4RipRedistributeOspf=apIpv4RipRedistributeOspf, apIpv4RipIfEntry=apIpv4RipIfEntry, apIpv4RipAdvRouteMetric=apIpv4RipAdvRouteMetric, apIpv4RipIfLogTx=apIpv4RipIfLogTx, apIpv4RipRedistributeFirewall=apIpv4RipRedistributeFirewall, apIpv4RipAdvRouteStatus=apIpv4RipAdvRouteStatus, apIpv4RipRedistributeLocal=apIpv4RipRedistributeLocal, apIpv4RipAdvRouteTable=apIpv4RipAdvRouteTable, apIpv4RipRedistributeStatic=apIpv4RipRedistributeStatic, PYSNMP_MODULE_ID=apIpv4RipMib, apIpv4RipEqualCostRoutes=apIpv4RipEqualCostRoutes, apIpv4RipIfAdvRouteMetric=apIpv4RipIfAdvRouteMetric, apIpv4RipIfAdvRouteStatus=apIpv4RipIfAdvRouteStatus, apIpv4RipStaticMetric=apIpv4RipStaticMetric, apIpv4RipIfAdvRouteEntry=apIpv4RipIfAdvRouteEntry, apIpv4RipMib=apIpv4RipMib, apIpv4RipAdvRouteEntry=apIpv4RipAdvRouteEntry, apIpv4RipOspfMetric=apIpv4RipOspfMetric, apIpv4RipIfAddress=apIpv4RipIfAddress, apIpv4RipFirewallMetric=apIpv4RipFirewallMetric, apIpv4RipIfLogRx=apIpv4RipIfLogRx, apIpv4RipAdvRoutePrefix=apIpv4RipAdvRoutePrefix, apIpv4RipIfAdvRoutePrefix=apIpv4RipIfAdvRoutePrefix, apIpv4RipAdvRoutePrefixLen=apIpv4RipAdvRoutePrefixLen, apIpv4RipIfAdvRoutePrefixLen=apIpv4RipIfAdvRoutePrefixLen)
