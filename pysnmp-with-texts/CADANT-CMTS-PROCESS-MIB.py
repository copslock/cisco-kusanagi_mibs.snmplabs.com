#
# PySNMP MIB module CADANT-CMTS-PROCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-PROCESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:45:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
cardNumber, trapSeverity, trapCounter = mibBuilder.importSymbols("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber", "trapSeverity", "trapCounter")
cadSystem, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadSystem")
OverloadStatus, CardId = mibBuilder.importSymbols("CADANT-TC", "OverloadStatus", "CardId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Unsigned32, Counter64, MibIdentifier, TimeTicks, Gauge32, ModuleIdentity, Integer32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Unsigned32", "Counter64", "MibIdentifier", "TimeTicks", "Gauge32", "ModuleIdentity", "Integer32", "IpAddress", "NotificationType")
TimeInterval, TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
cadProcessMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3))
cadProcessMib.setRevisions(('2013-07-02 00:00', '2011-05-22 00:00', '2010-12-20 00:00', '2005-10-20 00:00', '2003-03-29 00:00', '2003-03-20 00:00', '2002-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadProcessMib.setRevisionsDescriptions(('Add trapSeverity to Notification cardOverloadNotification and sysOverloadNotification', 'Add notification support for overload.', 'Deprecate unused memory status.', 'Add support for percentage idle time.', 'Promoted cadProcessMib from cadExperimental.7 to cadSystem.3', 'Add more support for card overload status and remove support for the process table.', 'Add support for card overload status.',))
if mibBuilder.loadTexts: cadProcessMib.setLastUpdated('201307020000Z')
if mibBuilder.loadTexts: cadProcessMib.setOrganization('Arris International, Inc.')
if mibBuilder.loadTexts: cadProcessMib.setContactInfo('Arris Technical Support Postal: ARRIS E-Mail: support@arrisi.com')
if mibBuilder.loadTexts: cadProcessMib.setDescription(' This MIB module contains information on the process table and memory usage of the C4. ')
cadProcessTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 0))
cadProcessGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1))
cadCpu = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1), )
if mibBuilder.loadTexts: cadCpu.setStatus('current')
if mibBuilder.loadTexts: cadCpu.setDescription('A conceptual row containing information about the cpu and system statistics. ')
cadCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1), ).setIndexNames((0, "CADANT-CMTS-PROCESS-MIB", "cadCpuCardId"))
if mibBuilder.loadTexts: cadCpuEntry.setStatus('current')
if mibBuilder.loadTexts: cadCpuEntry.setDescription('A conceptual row containing information about the cpu and system statistics. ')
cadCpuCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 1), CardId())
if mibBuilder.loadTexts: cadCpuCardId.setStatus('current')
if mibBuilder.loadTexts: cadCpuCardId.setDescription('Index of slot')
cadCpuRecentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 2), Counter64()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCpuRecentTime.setStatus('current')
if mibBuilder.loadTexts: cadCpuRecentTime.setDescription('Total CPU time consumed in the last reporting cycle.')
cadCpuTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 3), Counter64()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCpuTotalTime.setStatus('current')
if mibBuilder.loadTexts: cadCpuTotalTime.setDescription('Total CPU time consumed since the card was initialized.')
cadIdleCpuRecentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 4), Counter64()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIdleCpuRecentTime.setStatus('current')
if mibBuilder.loadTexts: cadIdleCpuRecentTime.setDescription('CPU time consumed by non-critical tasks in the last reporting cycle.')
cadIdleCpuTotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 5), Counter64()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIdleCpuTotalTime.setStatus('current')
if mibBuilder.loadTexts: cadIdleCpuTotalTime.setDescription('CPU time consumed by non-critical tasks since the card was initialized.')
cadSwitchRecentCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSwitchRecentCount.setStatus('current')
if mibBuilder.loadTexts: cadSwitchRecentCount.setDescription('Number of task switches in the last reporting cycle.')
cadSwitchTotalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadSwitchTotalCount.setStatus('current')
if mibBuilder.loadTexts: cadSwitchTotalCount.setDescription('Number of task switches since the card was initialized.')
cadIdleCpuRecentPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIdleCpuRecentPercent.setStatus('current')
if mibBuilder.loadTexts: cadIdleCpuRecentPercent.setDescription('Percentage of idle CPU time in last reporting cycle.')
cadMemoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2))
cadMemory = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1), )
if mibBuilder.loadTexts: cadMemory.setStatus('current')
if mibBuilder.loadTexts: cadMemory.setDescription('A table that contains information on the memory present on the C4 line cards. ')
cadMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1), ).setIndexNames((0, "CADANT-CMTS-PROCESS-MIB", "cadMeCardId"))
if mibBuilder.loadTexts: cadMemoryEntry.setStatus('current')
if mibBuilder.loadTexts: cadMemoryEntry.setDescription('A conceptual row containing information about processes and their configuration and operating parameters. ')
cadMeCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1, 1), CardId())
if mibBuilder.loadTexts: cadMeCardId.setStatus('current')
if mibBuilder.loadTexts: cadMeCardId.setDescription('Index of slot')
cadMeHeapSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1, 2), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMeHeapSize.setStatus('current')
if mibBuilder.loadTexts: cadMeHeapSize.setDescription('Total size of the dynamic heap. ')
cadMeHeapRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 2, 1, 1, 3), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadMeHeapRemaining.setStatus('current')
if mibBuilder.loadTexts: cadMeHeapRemaining.setDescription('Size of the dynamic currently unallocated.')
cadOverloadGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3))
cadOverload = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1), )
if mibBuilder.loadTexts: cadOverload.setStatus('current')
if mibBuilder.loadTexts: cadOverload.setDescription('A table that contains information on the overload status of the C4 line cards. ')
cadOverloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1), ).setIndexNames((0, "CADANT-CMTS-PROCESS-MIB", "cadOvCardId"))
if mibBuilder.loadTexts: cadOverloadEntry.setStatus('current')
if mibBuilder.loadTexts: cadOverloadEntry.setDescription('A conceptual row containing information about processes and their configuration and operating parameters. ')
cadOvCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1, 1), CardId())
if mibBuilder.loadTexts: cadOvCardId.setStatus('current')
if mibBuilder.loadTexts: cadOvCardId.setDescription(' Slot number of card ')
cadOvCpuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1, 2), OverloadStatus().clone('normal')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadOvCpuStatus.setStatus('current')
if mibBuilder.loadTexts: cadOvCpuStatus.setDescription(' Overload status of card ')
cadOvMemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 1, 1, 3), OverloadStatus().clone('normal')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadOvMemStatus.setStatus('deprecated')
if mibBuilder.loadTexts: cadOvMemStatus.setDescription(' Memory Overload status of card ')
cadOvSysCpuStatus = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 2), OverloadStatus().clone('normal')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadOvSysCpuStatus.setStatus('current')
if mibBuilder.loadTexts: cadOvSysCpuStatus.setDescription(' Overload status of E6 ')
cadOvSysMemStatus = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 3, 3), OverloadStatus().clone('normal')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadOvSysMemStatus.setStatus('current')
if mibBuilder.loadTexts: cadOvSysMemStatus.setDescription(' Memory Overload status of card ')
cadProcessTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 4))
cadProcessOverloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 4, 1), OverloadStatus().clone('normal')).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cadProcessOverloadStatus.setStatus('current')
if mibBuilder.loadTexts: cadProcessOverloadStatus.setDescription(' Overload status of C4 ')
cardOverloadNotification = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 0, 1)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"), ("CADANT-CMTS-PROCESS-MIB", "cadProcessOverloadStatus"))
if mibBuilder.loadTexts: cardOverloadNotification.setStatus('current')
if mibBuilder.loadTexts: cardOverloadNotification.setDescription('This trap is sent when the card changes overload state (controlled by cardTrapInh).')
sysOverloadNotification = NotificationType((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 0, 2)).setObjects(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"), ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"), ("CADANT-CMTS-PROCESS-MIB", "cadProcessOverloadStatus"))
if mibBuilder.loadTexts: sysOverloadNotification.setStatus('current')
if mibBuilder.loadTexts: sysOverloadNotification.setDescription('This trap is sent when the system changes overload state.')
cadProcessMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5))
cadProcessCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5, 1))
cadProcessGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5, 2))
cadProcessCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 3, 5, 1, 1)).setObjects(("CADANT-CMTS-PROCESS-MIB", "cadProcessGroup"), ("CADANT-CMTS-PROCESS-MIB", "cadMemoryGroup"), ("CADANT-CMTS-PROCESS-MIB", "cadOverloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadProcessCompliance = cadProcessCompliance.setStatus('current')
if mibBuilder.loadTexts: cadProcessCompliance.setDescription(' Compliance statement for entities implementing the Cadant Process Mib. ')
mibBuilder.exportSymbols("CADANT-CMTS-PROCESS-MIB", cadCpuTotalTime=cadCpuTotalTime, cadCpuEntry=cadCpuEntry, cadIdleCpuRecentTime=cadIdleCpuRecentTime, cadSwitchTotalCount=cadSwitchTotalCount, cadOvSysMemStatus=cadOvSysMemStatus, cadProcessTrapInfo=cadProcessTrapInfo, cadProcessMib=cadProcessMib, cadProcessCompliance=cadProcessCompliance, cadProcessGroups=cadProcessGroups, cadProcessCompliances=cadProcessCompliances, cadOvCardId=cadOvCardId, cadOvCpuStatus=cadOvCpuStatus, cadProcessGroup=cadProcessGroup, cadIdleCpuTotalTime=cadIdleCpuTotalTime, cadOvSysCpuStatus=cadOvSysCpuStatus, cadCpuRecentTime=cadCpuRecentTime, cadOverload=cadOverload, cadCpuCardId=cadCpuCardId, cadMemoryGroup=cadMemoryGroup, cadMemoryEntry=cadMemoryEntry, cadSwitchRecentCount=cadSwitchRecentCount, cadProcessOverloadStatus=cadProcessOverloadStatus, cadMeHeapRemaining=cadMeHeapRemaining, cadProcessMibConformance=cadProcessMibConformance, cardOverloadNotification=cardOverloadNotification, cadOverloadEntry=cadOverloadEntry, cadIdleCpuRecentPercent=cadIdleCpuRecentPercent, cadCpu=cadCpu, cadProcessTraps=cadProcessTraps, cadOverloadGroup=cadOverloadGroup, cadOvMemStatus=cadOvMemStatus, sysOverloadNotification=sysOverloadNotification, cadMeHeapSize=cadMeHeapSize, cadMemory=cadMemory, cadMeCardId=cadMeCardId, PYSNMP_MODULE_ID=cadProcessMib)
