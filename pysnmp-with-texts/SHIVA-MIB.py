#
# PySNMP MIB module SHIVA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHIVA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:02:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("RFC1158-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, ModuleIdentity, NotificationType, Counter32, ObjectIdentity, NotificationType, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso, enterprises, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "NotificationType", "Counter32", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso", "enterprises", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
shiva = MibIdentifier((1, 3, 6, 1, 4, 1, 166))
sSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 1))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2))
protocols = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 3))
temporary = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4))
messageLog = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 1, 1))
scc = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 1, 2))
fastpath = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1))
nmV32e = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 2))
fpBuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 1))
fpConf = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 2))
k_star = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 3)).setLabel("k-star")
tBap = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 1))
tATalk = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 2))
tIP = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 3))
tCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 4))
tEther = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 5))
mLogEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 166, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogEntryCount.setStatus('mandatory')
if mibBuilder.loadTexts: mLogEntryCount.setDescription('The number of entries currently in the message log buffer.')
mLogNewMessageTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 166, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("err", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mLogNewMessageTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: mLogNewMessageTrapEnable.setDescription('Enables or disables the generation of mLogNewMessage Traps of a priority numerically equal or lower than the value of this variable.')
mLogBuffer = MibTable((1, 3, 6, 1, 4, 1, 166, 1, 1, 3), )
if mibBuilder.loadTexts: mLogBuffer.setStatus('mandatory')
if mibBuilder.loadTexts: mLogBuffer.setDescription('A list of message log entries.')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1) + (1000, ), Integer32())
mLogMessage = MibTableRow((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1), ).setIndexNames((0, "SHIVA-MIB", "pysmiFakeCol1000"))
if mibBuilder.loadTexts: mLogMessage.setStatus('mandatory')
if mibBuilder.loadTexts: mLogMessage.setDescription('An entry in the message log. Entries are indexed by counting integers. Since the earliest messages are dropped from the log when it overflows, the first row in the table is not necessarily row 1. Therefore, a Get-Next request should be issued to determine the index of the first row.')
mLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: mLogTimeStamp.setDescription('The time the message was generated, measured in number of ticks since the device started.')
mLogPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("not-possible", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("err", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogPriority.setStatus('mandatory')
if mibBuilder.loadTexts: mLogPriority.setDescription("The priority of the log message. This field is for future use. All messages are currently logged at priority 'notice'")
mLogMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogMessageText.setStatus('mandatory')
if mibBuilder.loadTexts: mLogMessageText.setDescription('The text of the log message.')
mLogTimeOfDay = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogTimeOfDay.setStatus('mandatory')
if mibBuilder.loadTexts: mLogTimeOfDay.setDescription('The time of day at which the message is logged. This is expressed in seconds.')
sccTable = MibTable((1, 3, 6, 1, 4, 1, 166, 1, 2, 1), )
if mibBuilder.loadTexts: sccTable.setStatus('mandatory')
if mibBuilder.loadTexts: sccTable.setDescription('Each row of this table describes a (Zilog) 8530 Serial Communications Controller.')
sccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1), ).setIndexNames((0, "RFC1158-MIB", "ifIndex"))
if mibBuilder.loadTexts: sccEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sccEntry.setDescription("The object type of the rows in sccTable. If an interface does not have an SCC there will not be a row in the table for that interface's value of ifIndex.")
sccInterrupts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccInterrupts.setStatus('mandatory')
if mibBuilder.loadTexts: sccInterrupts.setDescription('Number of receive interrupts generated by the SCC.')
sccAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccAborts.setStatus('mandatory')
if mibBuilder.loadTexts: sccAborts.setDescription('The number of abort interrupts generated by the SCC.')
sccSpuriousInts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccSpuriousInts.setStatus('mandatory')
if mibBuilder.loadTexts: sccSpuriousInts.setDescription('The number of spurious interrupts generated by the SCC.')
sccDeferTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccDeferTimeouts.setStatus('mandatory')
if mibBuilder.loadTexts: sccDeferTimeouts.setDescription('Total number of defer timeouts. A defer timeout is the condition in which the line did not become idle for one and a half packet times, while the SCC was waiting to transmit, forcing a reset of the receiver. This event could indicate a misbehaving localtalk device.')
sccOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: sccOverruns.setDescription('Total receive overruns.')
sccUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: sccUnderruns.setDescription('Total receive underruns.')
bufferSize = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferSize.setStatus('mandatory')
if mibBuilder.loadTexts: bufferSize.setDescription('The size of the buffers in the buffer pool. All buffers are the same size.')
bufferAvail = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferAvail.setStatus('mandatory')
if mibBuilder.loadTexts: bufferAvail.setDescription('The total number of buffers initialized. This does not indicate the number of currently free buffers. Rather it is the total number of buffers which were created and made free at boot time.')
bufferDrops = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferDrops.setStatus('mandatory')
if mibBuilder.loadTexts: bufferDrops.setDescription('The total number of times that a buffer was requested when none was available.')
bufferTypeTable = MibTable((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4), )
if mibBuilder.loadTexts: bufferTypeTable.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeTable.setDescription('Each row of this table describes statistics on buffers allocated for a specific purpose. The sum of bufferTypeCount for all rows should always equal the bufferAvail count.')
bufferTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1), ).setIndexNames((0, "SHIVA-MIB", "bufferTypeIndex"))
if mibBuilder.loadTexts: bufferTypeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeEntry.setDescription('The object type of the rows in bufferTypeTable.')
bufferTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeIndex.setDescription('The enumeration of each buffer type row.')
bufferTypeType = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("free", 2), ("localtalk", 3), ("ethernet", 4), ("arp", 5), ("data", 6), ("erbf", 7), ("etbf", 8), ("malloc", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeType.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeType.setDescription('enumerated type of buffer type.')
bufferTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeDescr.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeDescr.setDescription('Text description of buffer type.')
bufferTypeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeCount.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeCount.setDescription('The number of buffers of the type which is described by the value of bufferTypeType for this row.')
bufferTypeDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeDrops.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeDrops.setDescription('The number of requests for buffers this type which were not fulfilled because no free buffers were available.')
bufferTypeRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeRequests.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeRequests.setDescription('The number of times buffers of this type were requested.')
bufferTypeMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeMaximum.setStatus('mandatory')
if mibBuilder.loadTexts: bufferTypeMaximum.setDescription('A high water mark for buffers of this type. This number represents the greatest number of buffers of this type ever allocated concurrently.')
confReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 1), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confReboot.setStatus('mandatory')
if mibBuilder.loadTexts: confReboot.setDescription('The amount of time, in hundredths of a second, until the device reboots itself.')
confCheckSum = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confCheckSum.setStatus('mandatory')
if mibBuilder.loadTexts: confCheckSum.setDescription("Indicates the validity of the FastPath's configuration. If written to, allows the management station to flush the configuration (by setting invalid), or to protect it (by setting valid).")
codeCheckSum = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: codeCheckSum.setStatus('mandatory')
if mibBuilder.loadTexts: codeCheckSum.setDescription("Indicates the validity of the FastPath's downloaded image. If written to, allows the management station to flush the downloaded image (by setting invalid), or to protect the it (by setting valid).")
promVersion = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: promVersion.setStatus('mandatory')
if mibBuilder.loadTexts: promVersion.setDescription('The version number of the PROM multiplied by 100, for instance, PROM version 4.1 would return 410.')
hwStatus = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStatus.setStatus('mandatory')
if mibBuilder.loadTexts: hwStatus.setDescription('This integer is a bit mask which holds the following flags: 0x000001 - LocalTalk failed tests 0x000002 - Ethernet controller failed tests 0x000004 - FP4: The battery is low 0x000008 - Expansion RAM is present 0x000010 - FP4: Ethernet 12V Fuse blown 0x000020 - Expansion RAM failed tests 0x000040 - FP4: Disable Enet CRS jumper installed 0x000080 - FP4: Disable Enet SQE jumper installed 0x000100 - Software Jumper 1 installed 0x000200 - Software Jumper 2 installed 0x000400 - Software Jumper 3 installed 0x000800 - Software Jumper 4 installed 0x007000 - FP5: EtherModule type field 0x008000 - FP5: EtherModule type field is valid 0x010000 - FP5: RAM Bank 3 is present 0x020000 - FP5: RAM Bank 3 failed tests 0x040000 - FP5: RAM Bank 4 is present 0x080000 - FP5: RAM Bank 4 failed tests 0x100000 - FP5: Downloader mode 0x200000 - FP5: Software Jumper 5 installed 0x400000 - FP5: Hardware has LocalTalk IOP')
confWhyReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("hardware", 2), ("firmware", 3), ("software", 4), ("config", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confWhyReboot.setStatus('mandatory')
if mibBuilder.loadTexts: confWhyReboot.setDescription('Reason code for reboot scheduled by confReboot')
confWhoReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confWhoReboot.setStatus('mandatory')
if mibBuilder.loadTexts: confWhoReboot.setDescription('Person responsible for reboot scheduled by confReboot')
confRebootComment = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confRebootComment.setStatus('mandatory')
if mibBuilder.loadTexts: confRebootComment.setDescription('Comment string for reboot scheduled by confReboot')
confHowReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("restart", 1), ("go", 2), ("pause", 3), ("reset", 4), ("bootprom", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confHowReboot.setStatus('mandatory')
if mibBuilder.loadTexts: confHowReboot.setDescription('Action taken when reboot scheduled by confReboot occurs')
tRTMPEntryTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryTimeouts.setStatus('mandatory')
if mibBuilder.loadTexts: tRTMPEntryTimeouts.setDescription('The number of entries which were removed from routing table because the aging algorithm indicated that they were invalid.')
tRTMPEntryDeletes = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryDeletes.setStatus('mandatory')
if mibBuilder.loadTexts: tRTMPEntryDeletes.setDescription('The number of entries which were removed from the routing table for any reason other than aging, for instance, due to a command from a Network Management station.')
tRTMPEntryEqualReplaces = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryEqualReplaces.setStatus('mandatory')
if mibBuilder.loadTexts: tRTMPEntryEqualReplaces.setDescription('The number of entries whose route was replaced by another route with the same hop count.')
tRTMPEntryBetterReplaces = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryBetterReplaces.setStatus('mandatory')
if mibBuilder.loadTexts: tRTMPEntryBetterReplaces.setDescription('The number of entries whose route was replaced by another route with a lower hop count.')
tRTMPEntryAdds = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryAdds.setStatus('mandatory')
if mibBuilder.loadTexts: tRTMPEntryAdds.setDescription('The number of new entries which have been added to the table.')
tRTMPZeroCounters = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("zero", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tRTMPZeroCounters.setStatus('mandatory')
if mibBuilder.loadTexts: tRTMPZeroCounters.setDescription('Writing this variable causes all the RTMP variables in this group to be set to zero.')
tZIPDeletes = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tZIPDeletes.setStatus('mandatory')
if mibBuilder.loadTexts: tZIPDeletes.setDescription('The number of Zones which have been deleted from the Zone Table.')
tZIPAdds = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tZIPAdds.setStatus('mandatory')
if mibBuilder.loadTexts: tZIPAdds.setDescription('The number of Zones which have been added to the Zone Table.')
tZIPZeroCounters = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("zero", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tZIPZeroCounters.setStatus('mandatory')
if mibBuilder.loadTexts: tZIPZeroCounters.setDescription('Writing this variable causes all the ZIP variables in this group to be set to zero.')
tAARPClearCache = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tAARPClearCache.setStatus('mandatory')
if mibBuilder.loadTexts: tAARPClearCache.setDescription('Writing this variable clears the AARP Cache.')
tKIPRoutesValid = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tKIPRoutesValid.setStatus('mandatory')
if mibBuilder.loadTexts: tKIPRoutesValid.setDescription('This variable can be used to force KIP to reacquire its configuration information.')
tARPClearCache = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tARPClearCache.setStatus('mandatory')
if mibBuilder.loadTexts: tARPClearCache.setDescription('Writing this variable clears the ARP Cache.')
tIPClearRoutingTable = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tIPClearRoutingTable.setStatus('mandatory')
if mibBuilder.loadTexts: tIPClearRoutingTable.setDescription('Writing this variable clears the entire IP routing table.')
tCommunityTrapHostType = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unconfigured", 1), ("ip", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapHostType.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapHostType.setDescription('This is the address family of the trap host. The Trap Host is the host to which the device sends all traps.')
tCommunityTrapHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapHostAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapHostAddress.setDescription('This is the Network Address of the host. It is interpreted according to the value of tCommunityTrapHostType.')
tCommunitySetHostType = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unconfigured", 1), ("ip", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunitySetHostType.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunitySetHostType.setDescription('This is the address family of the set host. The Set Host is a host which is privileged to change any MIB variable.')
tCommunitySetHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunitySetHostAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunitySetHostAddress.setDescription('This is the Network Address of the Set Host. It is interpreted according to the value of tCommunityTrapHostType.')
tCommunityList = MibTable((1, 3, 6, 1, 4, 1, 166, 4, 4, 5), )
if mibBuilder.loadTexts: tCommunityList.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityList.setDescription('The Communities Table describes the various communities known to the the device.')
pysmiFakeCol1001 = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1) + (1001, ), Integer32())
tCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1), ).setIndexNames((0, "SHIVA-MIB", "pysmiFakeCol1001"))
if mibBuilder.loadTexts: tCommunityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityEntry.setDescription('The type of a row object in the community table. This represents a single SNMP Community. Community entries are indexed by counting integers starting with 1.')
tCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityName.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityName.setDescription('The name of this community.')
tCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-access", 1), ("read-only-access", 2), ("clear-statistics", 3), ("configure", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityAccess.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityAccess.setDescription("This defines the privilege of the community. A 'read-only' community can examine any readable variable. A 'clear-statistics' community can reset non-critical counters. A 'configure' community has complete privileges. By setting the community access to 'no-access', a management station can deny all access by that community.")
tEtherTable = MibTable((1, 3, 6, 1, 4, 1, 166, 4, 5, 1), )
if mibBuilder.loadTexts: tEtherTable.setStatus('mandatory')
if mibBuilder.loadTexts: tEtherTable.setDescription('Table of statistics for the ethernet interfaces of a device.')
tEtherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1), ).setIndexNames((0, "RFC1158-MIB", "ifIndex"))
if mibBuilder.loadTexts: tEtherEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tEtherEntry.setDescription("The type of a row object in the ethernet table. This represents a single Ethernet Interface. If an interface is not an Ethernet interface, there will not be a row in this table for that interface's value of ifIndex.")
etherCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCRCErrors.setStatus('mandatory')
if mibBuilder.loadTexts: etherCRCErrors.setDescription('The total number of CRC errors on this ethernet interface')
etherAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherAlignErrors.setStatus('mandatory')
if mibBuilder.loadTexts: etherAlignErrors.setDescription('The total number of alignment errors on this ethernet interface.')
etherResourceErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherResourceErrors.setStatus('mandatory')
if mibBuilder.loadTexts: etherResourceErrors.setDescription('The total number of errors due to lack of resources on this ethernet interface.')
etherOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOverrunErrors.setStatus('mandatory')
if mibBuilder.loadTexts: etherOverrunErrors.setDescription('The total number of overrun errors on this ethernet interface.')
etherInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherInPackets.setStatus('mandatory')
if mibBuilder.loadTexts: etherInPackets.setDescription('The total number of input packets on this ethernet interface.')
etherOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOutPackets.setStatus('mandatory')
if mibBuilder.loadTexts: etherOutPackets.setDescription('The total number of output packets on this ethernet interface.')
etherBadTransmits = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBadTransmits.setStatus('mandatory')
if mibBuilder.loadTexts: etherBadTransmits.setDescription('The total number of transmission errors on this ethernet interface.')
etherOversizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOversizeFrames.setStatus('mandatory')
if mibBuilder.loadTexts: etherOversizeFrames.setDescription('The total number of oversize frame errors on this ethernet interface.')
etherSpurRUReadys = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurRUReadys.setStatus('mandatory')
if mibBuilder.loadTexts: etherSpurRUReadys.setDescription('The total number of spurious RU Ready interrupts on this ethernet interface.')
etherSpurCUActives = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurCUActives.setStatus('mandatory')
if mibBuilder.loadTexts: etherSpurCUActives.setDescription('The total number of spurious CU Active interrupts on this ethernet interface.')
etherSpurUnknowns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurUnknowns.setStatus('mandatory')
if mibBuilder.loadTexts: etherSpurUnknowns.setDescription('The total number of unknown spurious interrupts on this ethernet interface.')
etherBcastDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBcastDrops.setStatus('mandatory')
if mibBuilder.loadTexts: etherBcastDrops.setDescription('The total number of broadcast packets dropped to free resources on this ethernet interface.')
etherReceiverRestarts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherReceiverRestarts.setStatus('mandatory')
if mibBuilder.loadTexts: etherReceiverRestarts.setDescription('The total number of receiver restarts on this ethernet interface.')
etherReinterrupts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherReinterrupts.setStatus('mandatory')
if mibBuilder.loadTexts: etherReinterrupts.setDescription('The total number of reinterrupts on this ethernet interface.')
etherBufferReroutes = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBufferReroutes.setStatus('mandatory')
if mibBuilder.loadTexts: etherBufferReroutes.setDescription('The total number of buffers taken off of queues to service incoming packets on this ethernet interface.')
etherBufferDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBufferDrops.setStatus('mandatory')
if mibBuilder.loadTexts: etherBufferDrops.setDescription('The total number of buffers dropped on this ethernet interface.')
etherCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: etherCollisions.setDescription('The total number of collisions encountered on this ethernet interface.')
etherDefers = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherDefers.setStatus('mandatory')
if mibBuilder.loadTexts: etherDefers.setDescription('The total number of deferrals encountered on this ethernet interface.')
etherDMAUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherDMAUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: etherDMAUnderruns.setDescription('The total number of DMA Underruns on this ethernet interface.')
etherMaxCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherMaxCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: etherMaxCollisions.setDescription('The total number of packets dropped on this ethernet interface because they encountered more than 16 collisions.')
etherNoCarriers = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoCarriers.setStatus('mandatory')
if mibBuilder.loadTexts: etherNoCarriers.setDescription('The total number of no carrier errors experienced on this ethernet interface.')
etherNoCTSs = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoCTSs.setStatus('mandatory')
if mibBuilder.loadTexts: etherNoCTSs.setDescription('The total number of no CTS errors experienced on this ethernet interface.')
etherNoSQEs = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoSQEs.setStatus('mandatory')
if mibBuilder.loadTexts: etherNoSQEs.setDescription('The total number of no SQE errors experienced on this ethernet interface.')
mibBuilder.exportSymbols("SHIVA-MIB", mLogMessage=mLogMessage, bufferAvail=bufferAvail, etherInPackets=etherInPackets, sSystems=sSystems, bufferTypeMaximum=bufferTypeMaximum, bufferTypeIndex=bufferTypeIndex, etherOverrunErrors=etherOverrunErrors, protocols=protocols, tAARPClearCache=tAARPClearCache, pysmiFakeCol1000=pysmiFakeCol1000, tZIPZeroCounters=tZIPZeroCounters, tCommunityList=tCommunityList, bufferTypeDescr=bufferTypeDescr, etherCollisions=etherCollisions, pysmiFakeCol1001=pysmiFakeCol1001, bufferTypeEntry=bufferTypeEntry, confWhyReboot=confWhyReboot, etherNoCarriers=etherNoCarriers, nmV32e=nmV32e, tRTMPEntryTimeouts=tRTMPEntryTimeouts, confReboot=confReboot, products=products, etherCRCErrors=etherCRCErrors, mLogMessageText=mLogMessageText, sccDeferTimeouts=sccDeferTimeouts, tEtherTable=tEtherTable, confRebootComment=confRebootComment, etherResourceErrors=etherResourceErrors, etherDefers=etherDefers, temporary=temporary, mLogBuffer=mLogBuffer, tRTMPEntryBetterReplaces=tRTMPEntryBetterReplaces, bufferTypeType=bufferTypeType, fpConf=fpConf, fpBuffer=fpBuffer, sccTable=sccTable, sccOverruns=sccOverruns, hwStatus=hwStatus, bufferTypeDrops=bufferTypeDrops, confWhoReboot=confWhoReboot, shiva=shiva, bufferDrops=bufferDrops, etherOutPackets=etherOutPackets, tCommunityTrapHostType=tCommunityTrapHostType, tCommunityName=tCommunityName, tKIPRoutesValid=tKIPRoutesValid, etherBufferReroutes=etherBufferReroutes, etherDMAUnderruns=etherDMAUnderruns, sccEntry=sccEntry, tIPClearRoutingTable=tIPClearRoutingTable, tARPClearCache=tARPClearCache, tCommunitySetHostType=tCommunitySetHostType, tEtherEntry=tEtherEntry, etherBufferDrops=etherBufferDrops, etherSpurRUReadys=etherSpurRUReadys, confHowReboot=confHowReboot, mLogTimeOfDay=mLogTimeOfDay, confCheckSum=confCheckSum, etherMaxCollisions=etherMaxCollisions, sccAborts=sccAborts, bufferSize=bufferSize, mLogNewMessageTrapEnable=mLogNewMessageTrapEnable, tBap=tBap, etherReinterrupts=etherReinterrupts, tCommunityTrapHostAddress=tCommunityTrapHostAddress, tRTMPZeroCounters=tRTMPZeroCounters, codeCheckSum=codeCheckSum, mLogTimeStamp=mLogTimeStamp, bufferTypeRequests=bufferTypeRequests, tCommunityAccess=tCommunityAccess, etherOversizeFrames=etherOversizeFrames, tRTMPEntryAdds=tRTMPEntryAdds, mLogEntryCount=mLogEntryCount, tRTMPEntryDeletes=tRTMPEntryDeletes, tCommunity=tCommunity, etherSpurUnknowns=etherSpurUnknowns, etherNoSQEs=etherNoSQEs, tATalk=tATalk, tZIPDeletes=tZIPDeletes, etherBadTransmits=etherBadTransmits, bufferTypeCount=bufferTypeCount, tRTMPEntryEqualReplaces=tRTMPEntryEqualReplaces, sccInterrupts=sccInterrupts, etherReceiverRestarts=etherReceiverRestarts, tCommunityEntry=tCommunityEntry, sccSpuriousInts=sccSpuriousInts, etherNoCTSs=etherNoCTSs, mLogPriority=mLogPriority, scc=scc, tIP=tIP, fastpath=fastpath, k_star=k_star, tEther=tEther, promVersion=promVersion, etherSpurCUActives=etherSpurCUActives, tZIPAdds=tZIPAdds, bufferTypeTable=bufferTypeTable, sccUnderruns=sccUnderruns, etherAlignErrors=etherAlignErrors, messageLog=messageLog, tCommunitySetHostAddress=tCommunitySetHostAddress, etherBcastDrops=etherBcastDrops)
