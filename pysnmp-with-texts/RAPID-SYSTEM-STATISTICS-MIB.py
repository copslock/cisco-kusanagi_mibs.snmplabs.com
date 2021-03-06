#
# PySNMP MIB module RAPID-SYSTEM-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPID-SYSTEM-STATISTICS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, Gauge32, ModuleIdentity, IpAddress, TimeTicks, enterprises, iso, Bits, NotificationType, Counter64, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "TimeTicks", "enterprises", "iso", "Bits", "NotificationType", "Counter64", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-05-16 12:00', '2002-11-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsInfoModule.setRevisionsDescriptions(('Initial revision.', 'Changed CONTACT-INFO.',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0105161200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsInfoModule.setContactInfo(' Ella Yu WatchGuard Technologies, Inc. 1841 Zanker Road San Jose, CA 95112 USA 408-519-4888 ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsInfoModule.setDescription('The MIB module describes various system statistics information of RapidStream system.')
rsSystemStatisticsMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 3))
if mibBuilder.loadTexts: rsSystemStatisticsMIB.setStatus('current')
if mibBuilder.loadTexts: rsSystemStatisticsMIB.setDescription('This is the base system information for all system related statistical counters.')
rsSystemCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil.setStatus('current')
if mibBuilder.loadTexts: rsSystemCpuUtil.setDescription('CPU utilization of the system in last 5 seconds. The value is measured in 0.01%. For example, if the value is 234, then CPU utilization is 2.34%.')
rsSystemTotalSendBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalSendBytes.setStatus('current')
if mibBuilder.loadTexts: rsSystemTotalSendBytes.setDescription('The total number of bytes sent since system is up. This number includes both cut through traffic and host traffic.')
rsSystemTotalRecvBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalRecvBytes.setStatus('current')
if mibBuilder.loadTexts: rsSystemTotalRecvBytes.setDescription('The total number of bytes received since system is up. This number includes both cut through traffic and host traffic.')
rsSystemTotalSendPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalSendPackets.setStatus('current')
if mibBuilder.loadTexts: rsSystemTotalSendPackets.setDescription('The total number of the packets sent since system is up. This number includes both cut through traffic and host traffic.')
rsSystemTotalRecvPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalRecvPackets.setStatus('current')
if mibBuilder.loadTexts: rsSystemTotalRecvPackets.setDescription('The total number of the packets received since system is up. The number includes both cut through traffic and host traffic.')
rsSystemStreamReqTotal = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemStreamReqTotal.setStatus('current')
if mibBuilder.loadTexts: rsSystemStreamReqTotal.setDescription('The total number of the connection requests since system is up.')
rsSystemStreamReqDrop = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemStreamReqDrop.setStatus('current')
if mibBuilder.loadTexts: rsSystemStreamReqDrop.setDescription('The total number of the connection requests being dropped since system is up.')
rsSystemCpuUtil1 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 77), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil1.setStatus('current')
if mibBuilder.loadTexts: rsSystemCpuUtil1.setDescription('CPU utilization of the system in last 1 minute. The value is measured in 0.01%. For example, if the value is 234, then CPU utilization is 2.34%.')
rsSystemCpuUtil5 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 78), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil5.setStatus('current')
if mibBuilder.loadTexts: rsSystemCpuUtil5.setDescription('CPU utilization of the system in last 5 minutes. The value is measured in 0.01%. For example, if the value is 234, then CPU utilization is 2.34%.')
rsSystemCpuUtil15 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 79), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil15.setStatus('current')
if mibBuilder.loadTexts: rsSystemCpuUtil15.setDescription('CPU utilization of the system in last 15 minutes. The value is measured in 0.01%. For example, if the value is 234, then CPU utilization is 2.34%.')
mibBuilder.exportSymbols("RAPID-SYSTEM-STATISTICS-MIB", rsSystemStreamReqDrop=rsSystemStreamReqDrop, rsSystemCpuUtil15=rsSystemCpuUtil15, rsSystemTotalSendPackets=rsSystemTotalSendPackets, rsSystemCpuUtil1=rsSystemCpuUtil1, rsSystemCpuUtil=rsSystemCpuUtil, rsSystemTotalRecvBytes=rsSystemTotalRecvBytes, rsSystemTotalRecvPackets=rsSystemTotalRecvPackets, rsSystemCpuUtil5=rsSystemCpuUtil5, PYSNMP_MODULE_ID=rsInfoModule, rsSystemStatisticsMIB=rsSystemStatisticsMIB, rsSystemStreamReqTotal=rsSystemStreamReqTotal, rsInfoModule=rsInfoModule, rsSystemTotalSendBytes=rsSystemTotalSendBytes)
