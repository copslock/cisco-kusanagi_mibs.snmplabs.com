#
# PySNMP MIB module NETSCREEN-RESOURCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-RESOURCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
netscreenResource, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenResource")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Counter32, Unsigned32, TimeTicks, NotificationType, ObjectIdentity, MibIdentifier, iso, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Counter32", "Unsigned32", "TimeTicks", "NotificationType", "ObjectIdentity", "MibIdentifier", "iso", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenResourceMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 16, 0))
netscreenResourceMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2002-05-05 00:00', '2001-04-30 00:00',))
if mibBuilder.loadTexts: netscreenResourceMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenResourceMibModule.setOrganization('Juniper Networks, Inc.')
nsResCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 16, 1))
nsResCpuAvg = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuAvg.setStatus('current')
nsResCpuLast1Min = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuLast1Min.setStatus('current')
nsResCpuLast5Min = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuLast5Min.setStatus('current')
nsResCpuLast15Min = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuLast15Min.setStatus('current')
nsResMem = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 16, 2))
nsResMemAllocate = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResMemAllocate.setStatus('current')
nsResMemLeft = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResMemLeft.setStatus('current')
nsResMemFrag = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResMemFrag.setStatus('current')
nsResSession = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 16, 3))
nsResSessAllocate = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResSessAllocate.setStatus('current')
nsResSessMaxium = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResSessMaxium.setStatus('current')
nsResSessFailed = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResSessFailed.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-RESOURCE-MIB", nsResCpuAvg=nsResCpuAvg, netscreenResourceMibModule=netscreenResourceMibModule, nsResMem=nsResMem, nsResMemFrag=nsResMemFrag, nsResCpuLast1Min=nsResCpuLast1Min, nsResCpuLast15Min=nsResCpuLast15Min, nsResSessAllocate=nsResSessAllocate, nsResMemLeft=nsResMemLeft, nsResSessFailed=nsResSessFailed, nsResMemAllocate=nsResMemAllocate, nsResSession=nsResSession, PYSNMP_MODULE_ID=netscreenResourceMibModule, nsResCPU=nsResCPU, nsResSessMaxium=nsResSessMaxium, nsResCpuLast5Min=nsResCpuLast5Min)
