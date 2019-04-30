#
# PySNMP MIB module TPT-NGFW-PERFORMANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-NGFW-PERFORMANCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Bits, Integer32, ObjectIdentity, IpAddress, Counter64, Unsigned32, NotificationType, MibIdentifier, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "Integer32", "ObjectIdentity", "IpAddress", "Counter64", "Unsigned32", "NotificationType", "MibIdentifier", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_ngfw_groups, tpt_ngfw_objs, tpt_ngfw_compls = mibBuilder.importSymbols("TPT-NGFW-REG-MIB", "tpt-ngfw-groups", "tpt-ngfw-objs", "tpt-ngfw-compls")
tptNgfwPerformance = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3))
tptNgfwPerformance.setRevisions(('2016-05-25 18:54', '2013-01-03 17:39',))
if mibBuilder.loadTexts: tptNgfwPerformance.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tptNgfwPerformance.setOrganization('Trend Micro, Inc.')
class TptNgfwPerfPacketSizeGrouping(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("bytes64", 0), ("bytes65to127", 1), ("bytes128to255", 2), ("bytes256to511", 3), ("bytes512to1023", 4), ("bytes1024to1518", 5), ("bytes1519to4095", 6), ("bytes4096to9216", 7), ("bytes9217to16383", 8), ("undersize", 9), ("oversize", 10))

tptNgfwPerformanceObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1))
if mibBuilder.loadTexts: tptNgfwPerformanceObjs.setStatus('current')
tptNgfwPerfPacketsIn = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfPacketsIn.setStatus('current')
tptNgfwPerfPacketsOut = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfPacketsOut.setStatus('current')
tptNgfwPerfBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfBytesIn.setStatus('current')
tptNgfwPerfBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfBytesOut.setStatus('current')
tptNgfwPerfFragmentsIn = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfFragmentsIn.setStatus('current')
tptNgfwPerfFragmentsOut = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfFragmentsOut.setStatus('current')
tptNgfwPerfPacketDistTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7), )
if mibBuilder.loadTexts: tptNgfwPerfPacketDistTable.setStatus('current')
tptNgfwPerfPacketDistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1), ).setIndexNames((0, "TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketDistEntryIndex"))
if mibBuilder.loadTexts: tptNgfwPerfPacketDistEntry.setStatus('current')
tptNgfwPerfPacketDistEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1, 1), Unsigned32())
if mibBuilder.loadTexts: tptNgfwPerfPacketDistEntryIndex.setStatus('current')
tptNgfwPerfPacketDistSizeGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1, 2), TptNgfwPerfPacketSizeGrouping()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfPacketDistSizeGrp.setStatus('current')
tptNgfwPerfPacketDistSizeGrpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 1, 7, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfPacketDistSizeGrpCount.setStatus('current')
tptNgfwPerfFWObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2))
if mibBuilder.loadTexts: tptNgfwPerfFWObjs.setStatus('current')
tptNgfwPerfFWBlocks = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfFWBlocks.setStatus('current')
tptNgfwPerfFWPermits = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfFWPermits.setStatus('current')
tptNgfwPerfFWSessions = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfFWSessions.setStatus('current')
tptNgfwPerfIPSObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3))
if mibBuilder.loadTexts: tptNgfwPerfIPSObjs.setStatus('current')
tptNgfwPerfIPSManagedStreams = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfIPSManagedStreams.setStatus('current')
tptNgfwPerfIPSQuarantineCount = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfIPSQuarantineCount.setStatus('current')
tptNgfwPerfIPSRateLimitCount = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfIPSRateLimitCount.setStatus('current')
tptNgfwPerfIPSAfcEntries = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfIPSAfcEntries.setStatus('current')
tptNgfwPerfIPSAfcAppEntries = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfIPSAfcAppEntries.setStatus('current')
tptNgfwPerfIPSBlockedStreams = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfIPSBlockedStreams.setStatus('current')
tptNgfwPerfIPSTrustedStreams = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 3, 3, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwPerfIPSTrustedStreams.setStatus('current')
tptNgfwPerformanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 6)).setObjects(("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketsIn"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketsOut"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfBytesIn"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfBytesOut"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFragmentsIn"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFragmentsOut"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFWBlocks"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFWPermits"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfFWSessions"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSManagedStreams"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSQuarantineCount"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSRateLimitCount"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSAfcEntries"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSAfcAppEntries"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSBlockedStreams"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfIPSTrustedStreams"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketDistSizeGrp"), ("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerfPacketDistSizeGrpCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwPerformanceGroup = tptNgfwPerformanceGroup.setStatus('current')
tptNgfwPerformanceCompl = ModuleCompliance((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 3)).setObjects(("TPT-NGFW-PERFORMANCE-MIB", "tptNgfwPerformanceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwPerformanceCompl = tptNgfwPerformanceCompl.setStatus('current')
mibBuilder.exportSymbols("TPT-NGFW-PERFORMANCE-MIB", TptNgfwPerfPacketSizeGrouping=TptNgfwPerfPacketSizeGrouping, tptNgfwPerfIPSManagedStreams=tptNgfwPerfIPSManagedStreams, tptNgfwPerfIPSRateLimitCount=tptNgfwPerfIPSRateLimitCount, PYSNMP_MODULE_ID=tptNgfwPerformance, tptNgfwPerfFWObjs=tptNgfwPerfFWObjs, tptNgfwPerfPacketsOut=tptNgfwPerfPacketsOut, tptNgfwPerfPacketDistEntryIndex=tptNgfwPerfPacketDistEntryIndex, tptNgfwPerfPacketDistSizeGrp=tptNgfwPerfPacketDistSizeGrp, tptNgfwPerfFragmentsOut=tptNgfwPerfFragmentsOut, tptNgfwPerfFWBlocks=tptNgfwPerfFWBlocks, tptNgfwPerfPacketDistSizeGrpCount=tptNgfwPerfPacketDistSizeGrpCount, tptNgfwPerfIPSQuarantineCount=tptNgfwPerfIPSQuarantineCount, tptNgfwPerfPacketsIn=tptNgfwPerfPacketsIn, tptNgfwPerformanceObjs=tptNgfwPerformanceObjs, tptNgfwPerfFWSessions=tptNgfwPerfFWSessions, tptNgfwPerformanceGroup=tptNgfwPerformanceGroup, tptNgfwPerfFWPermits=tptNgfwPerfFWPermits, tptNgfwPerfIPSAfcAppEntries=tptNgfwPerfIPSAfcAppEntries, tptNgfwPerfBytesIn=tptNgfwPerfBytesIn, tptNgfwPerfFragmentsIn=tptNgfwPerfFragmentsIn, tptNgfwPerfIPSTrustedStreams=tptNgfwPerfIPSTrustedStreams, tptNgfwPerfPacketDistEntry=tptNgfwPerfPacketDistEntry, tptNgfwPerfPacketDistTable=tptNgfwPerfPacketDistTable, tptNgfwPerfIPSAfcEntries=tptNgfwPerfIPSAfcEntries, tptNgfwPerfIPSBlockedStreams=tptNgfwPerfIPSBlockedStreams, tptNgfwPerformanceCompl=tptNgfwPerformanceCompl, tptNgfwPerformance=tptNgfwPerformance, tptNgfwPerfIPSObjs=tptNgfwPerfIPSObjs, tptNgfwPerfBytesOut=tptNgfwPerfBytesOut)