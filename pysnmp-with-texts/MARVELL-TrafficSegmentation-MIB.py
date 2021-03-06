#
# PySNMP MIB module MARVELL-TrafficSegmentation-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-TrafficSegmentation-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, MibIdentifier, ModuleIdentity, ObjectIdentity, NotificationType, Gauge32, Unsigned32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Integer32")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
rlTrafficSeg = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 138))
rlTrafficSeg.setRevisions(('2008-05-03 12:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlTrafficSeg.setRevisionsDescriptions(('The private MIB module definition Traffic Segmentation MIB.',))
if mibBuilder.loadTexts: rlTrafficSeg.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlTrafficSeg.setOrganization('MARVELL Semiconductor, Inc.')
if mibBuilder.loadTexts: rlTrafficSeg.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlTrafficSeg.setDescription('<description>')
rlTrafficSegConfigTable = MibTable((1, 3, 6, 1, 4, 1, 89, 138, 1), )
if mibBuilder.loadTexts: rlTrafficSegConfigTable.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegConfigTable.setDescription('A table containing entries to configure the traffic segmentation information table')
rlTrafficSegConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 138, 1, 1), ).setIndexNames((0, "MARVELL-TrafficSegmentation-MIB", "rlTrafficSegConfigIndex"))
if mibBuilder.loadTexts: rlTrafficSegConfigEntry.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegConfigEntry.setDescription('A table entry of configuration for traffic segmentation information table')
rlTrafficSegConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: rlTrafficSegConfigIndex.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegConfigIndex.setDescription('Running index of the entry.')
rlTrafficSegConfigIngressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTrafficSegConfigIngressPorts.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegConfigIngressPorts.setDescription('List of ingress ports to configure in rlTrafficSegTable')
rlTrafficSegConfigEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTrafficSegConfigEgressPorts.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegConfigEgressPorts.setDescription('List of egress ports to configure in rlTrafficSegTable')
rlTrafficSegConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTrafficSegConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegConfigRowStatus.setDescription('This object indicates the status of this entry.')
rlTrafficSegTable = MibTable((1, 3, 6, 1, 4, 1, 89, 138, 2), )
if mibBuilder.loadTexts: rlTrafficSegTable.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegTable.setDescription('A table containing entries of traffic segmentation configuration information')
rlTrafficSegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 138, 2, 1), ).setIndexNames((0, "MARVELL-TrafficSegmentation-MIB", "rlTrafficSegIndex"))
if mibBuilder.loadTexts: rlTrafficSegEntry.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegEntry.setDescription('A table entry of traffic segmentation information table')
rlTrafficSegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: rlTrafficSegIndex.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegIndex.setDescription('Index to the table entry, analogue to source ID')
rlTrafficSegIngressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTrafficSegIngressPorts.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegIngressPorts.setDescription('List of the ingress ports of the entry')
rlTrafficSegEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTrafficSegEgressPorts.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegEgressPorts.setDescription(' List of the ingress ports of the entry')
rlTrafficSegRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTrafficSegRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlTrafficSegRowStatus.setDescription('This object indicates the status of this entry.')
mibBuilder.exportSymbols("MARVELL-TrafficSegmentation-MIB", rlTrafficSegEntry=rlTrafficSegEntry, rlTrafficSegRowStatus=rlTrafficSegRowStatus, rlTrafficSegEgressPorts=rlTrafficSegEgressPorts, rlTrafficSegIndex=rlTrafficSegIndex, rlTrafficSeg=rlTrafficSeg, rlTrafficSegConfigRowStatus=rlTrafficSegConfigRowStatus, rlTrafficSegIngressPorts=rlTrafficSegIngressPorts, rlTrafficSegConfigIngressPorts=rlTrafficSegConfigIngressPorts, rlTrafficSegConfigIndex=rlTrafficSegConfigIndex, rlTrafficSegConfigEntry=rlTrafficSegConfigEntry, rlTrafficSegTable=rlTrafficSegTable, rlTrafficSegConfigTable=rlTrafficSegConfigTable, rlTrafficSegConfigEgressPorts=rlTrafficSegConfigEgressPorts, PYSNMP_MODULE_ID=rlTrafficSeg)
