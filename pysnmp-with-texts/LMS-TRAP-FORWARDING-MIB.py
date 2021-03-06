#
# PySNMP MIB module LMS-TRAP-FORWARDING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LMS-TRAP-FORWARDING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:08:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter32, NotificationType, iso, Gauge32, IpAddress, NotificationType, TimeTicks, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "NotificationType", "iso", "Gauge32", "IpAddress", "NotificationType", "TimeTicks", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lotus = MibIdentifier((1, 3, 6, 1, 4, 1, 334))
notes = MibIdentifier((1, 3, 6, 1, 4, 1, 334, 1))
lcs = MibIdentifier((1, 3, 6, 1, 4, 1, 334, 2))
softswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 334, 3))
common_mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 334, 3, 1)).setLabel("common-mibs")
lms = MibIdentifier((1, 3, 6, 1, 4, 1, 334, 3, 2))
lmsTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 334, 3, 2, 3))
lmsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 334, 3, 2, 2))
class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

eventFwdTableModificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("no-access", 2), ("read-only", 3), ("read-modify", 4), ("read-create", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventFwdTableModificationStatus.setStatus('mandatory')
if mibBuilder.loadTexts: eventFwdTableModificationStatus.setDescription("Indicates the combination of possible functions allowed on the lmsEventFwdTable table, subject to overriding SNMP security attributes and the ACCESS clause restrictions on the objects themselves. The values are: unknown - Managers privileges are unknown. no-access - Managers may neither read nor write to this table. read-only - Managers may only read the table, they cannot add or delete conceptual rows and cannot change the value of any variable, even those with ACCESS of 'read-write'. read-modify - Managers may read the table, and change the value of variables whose ACCESS is 'read-write'. read-create - Managers may read the table, change the value of variables whose ACCESS is 'read-write', and create or delete conceptual rows in the table.")
nextFwdEntryIndex = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextFwdEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nextFwdEntryIndex.setDescription("The index that may be used by a manager on a 'set-request' PDU to create a new conceptual row in the lmsEventFwdTable table.")
trapWindowTime = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 3), TimeInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapWindowTime.setStatus('mandatory')
if mibBuilder.loadTexts: trapWindowTime.setDescription("A control time window, expresses in 1/100ths of a second, used in conjunction with the maxTrapsPerWindow variable to prevent a 'trap storm' caused by a rapidly recurring error condition .")
maxTrapsPerWindow = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxTrapsPerWindow.setStatus('mandatory')
if mibBuilder.loadTexts: maxTrapsPerWindow.setDescription("The maximum number of traps to be forwarded in the time interval expressed in the trapWindowTime variable. Used to prevent a 'trap storm' caused by a rapidly recurring error condition.")
numDroppedMaxPerWindowTraps = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numDroppedMaxPerWindowTraps.setStatus('mandatory')
if mibBuilder.loadTexts: numDroppedMaxPerWindowTraps.setDescription('The number of traps intended for this destination, which were not forwarded due to the maxTrapsPerWindow count being met or exceeded.')
lmsEventFwdTable = MibTable((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6), )
if mibBuilder.loadTexts: lmsEventFwdTable.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEventFwdTable.setDescription('The table holding information to control/administer forwarding of LMS events to SNMP-based management stations or applications.')
lmsEventFwdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1), ).setIndexNames((0, "LMS-TRAP-FORWARDING-MIB", "fwdEntryIndex"))
if mibBuilder.loadTexts: lmsEventFwdEntry.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEventFwdEntry.setDescription('The entry associated with each destination to which LMS events should be forwarded as SNMP traps.')
fwdEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwdEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fwdEntryIndex.setDescription('The integer index into the lmsEventFwdTable table.')
rowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: rowStatus.setDescription('The status of the conceptual row. These are mapped to the same values as the RowStatus textual conversion in SNMPv2 and carry the same semantics.')
destinationNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: destinationNetAddr.setStatus('mandatory')
if mibBuilder.loadTexts: destinationNetAddr.setDescription('The network address of the destination entity for trap forwarding.')
destinationCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: destinationCommunity.setStatus('mandatory')
if mibBuilder.loadTexts: destinationCommunity.setDescription('The community name to be used when sending traps to the destination entity. This variable is non-defined in SNMPv2 implementions.')
destinationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: destinationPort.setStatus('mandatory')
if mibBuilder.loadTexts: destinationPort.setDescription("The UDP port at the 'destinationNetAddr' to which the trap should be sent.")
forwardingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: forwardingEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: forwardingEnabled.setDescription('Indicates whether forwarding is enabled for this destination at the present time. Used to temporarily suspend forwarding.')
forwardingFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: forwardingFilterName.setStatus('mandatory')
if mibBuilder.loadTexts: forwardingFilterName.setDescription('Undefined at the present time - bge.')
lastTrapSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTrapSequenceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: lastTrapSequenceNumber.setDescription("The sequence number of the last trap sent to this destination. All traps sent to a given destination are sequenced via a 32-bit, wrapping counter. A manager may use this variable to determine if any traps for this destination have been 'lost'.")
lastTrapTime = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTrapTime.setStatus('mandatory')
if mibBuilder.loadTexts: lastTrapTime.setDescription('The value of sysUpTime as included in the last trap sent to this destination.')
numDroppedDisabledTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numDroppedDisabledTraps.setStatus('mandatory')
if mibBuilder.loadTexts: numDroppedDisabledTraps.setDescription('The number of traps intended for this destination, which were not forwarded due to the variable forwardingEnabled begin set to disabled(2).')
lmsEvComponentType = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("global", 1), ("switch", 2), ("core", 3), ("mta", 4), ("mta-group", 5), ("queue", 6), ("mea", 7), ("other", 8))))
if mibBuilder.loadTexts: lmsEvComponentType.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEvComponentType.setDescription('Identifies the type of LMS component issuing the event.')
lmsEvComponentDN = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 2), DisplayString())
if mibBuilder.loadTexts: lmsEvComponentDN.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEvComponentDN.setDescription('Identifies the most unique (rightmost) portion of the Spyder Distinguished Name of the component issuing the event. The combination of lmsEvComponentType and lmsEvComponentDN MUST uniquely identify the issuing component.')
lmsEvDbId = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 3), Integer32())
if mibBuilder.loadTexts: lmsEvDbId.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEvDbId.setDescription('Identifies the unique key used to identify this event in the LMS event database.')
lmsEvOID = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 4), Integer32())
if mibBuilder.loadTexts: lmsEvOID.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEvOID.setDescription('Identifies the specific LMS event OID conatined in the LMS event.')
numLmsEvSequences = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 5), Counter32())
if mibBuilder.loadTexts: numLmsEvSequences.setStatus('mandatory')
if mibBuilder.loadTexts: numLmsEvSequences.setDescription('A monotonically increasing, wrapping counter indication the sequence number of this event, relative to the destination of the trap. Events that are not forwarded to a destination (destination temporarily disabled, windowTime exceeded) do not cause this sequence number to increase.')
lmsEvSeverity = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 6), Integer32())
if mibBuilder.loadTexts: lmsEvSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEvSeverity.setDescription('The original severity assigned to the LMS event.')
lmsEvSupportingText = MibScalar((1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 7), DisplayString())
if mibBuilder.loadTexts: lmsEvSupportingText.setStatus('mandatory')
if mibBuilder.loadTexts: lmsEvSupportingText.setDescription('Textual information supporting the event data. The meaning of the brief text must be obvious in the context of the trap - for the sake of brevity it need not be a gramatically correct sentence.')
lmsCritical = NotificationType((1, 3, 6, 1, 4, 1, 334, 3, 2) + (0,1)).setObjects(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"), ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
if mibBuilder.loadTexts: lmsCritical.setDescription('A critical alarm forwarded from the LMS event subsystem.')
lmsMajor = NotificationType((1, 3, 6, 1, 4, 1, 334, 3, 2) + (0,2)).setObjects(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"), ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
if mibBuilder.loadTexts: lmsMajor.setDescription('A major alarm forwarded from the LMS event subsystem.')
lmsMinor = NotificationType((1, 3, 6, 1, 4, 1, 334, 3, 2) + (0,3)).setObjects(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"), ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
if mibBuilder.loadTexts: lmsMinor.setDescription('A minor alarm forwarded from the LMS event subsystem.')
lmsWarning = NotificationType((1, 3, 6, 1, 4, 1, 334, 3, 2) + (0,4)).setObjects(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"), ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
if mibBuilder.loadTexts: lmsWarning.setDescription('A warning or indeterminate forwarded from the LMS event subsystem.')
lmsCleared = NotificationType((1, 3, 6, 1, 4, 1, 334, 3, 2) + (0,5)).setObjects(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"), ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
if mibBuilder.loadTexts: lmsCleared.setDescription('A cleared forwarded from the LMS event subsystem.')
lmsInformational = NotificationType((1, 3, 6, 1, 4, 1, 334, 3, 2) + (0,6)).setObjects(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"), ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"), ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
if mibBuilder.loadTexts: lmsInformational.setDescription('An informational event forwarded from the LMS event subsystem.')
mibBuilder.exportSymbols("LMS-TRAP-FORWARDING-MIB", fwdEntryIndex=fwdEntryIndex, lmsEventFwdTable=lmsEventFwdTable, destinationCommunity=destinationCommunity, forwardingEnabled=forwardingEnabled, eventFwdTableModificationStatus=eventFwdTableModificationStatus, lmsEvSupportingText=lmsEvSupportingText, softswitch=softswitch, lmsEvComponentType=lmsEvComponentType, maxTrapsPerWindow=maxTrapsPerWindow, lmsTrapData=lmsTrapData, lcs=lcs, lastTrapSequenceNumber=lastTrapSequenceNumber, rowStatus=rowStatus, lastTrapTime=lastTrapTime, lmsEvSeverity=lmsEvSeverity, notes=notes, TimeInterval=TimeInterval, lmsEvOID=lmsEvOID, nextFwdEntryIndex=nextFwdEntryIndex, lmsInformational=lmsInformational, lmsMinor=lmsMinor, lmsEvComponentDN=lmsEvComponentDN, lmsMajor=lmsMajor, trapWindowTime=trapWindowTime, numLmsEvSequences=numLmsEvSequences, destinationPort=destinationPort, lmsCleared=lmsCleared, lmsEventFwdEntry=lmsEventFwdEntry, lmsCritical=lmsCritical, lmsEvDbId=lmsEvDbId, numDroppedDisabledTraps=numDroppedDisabledTraps, numDroppedMaxPerWindowTraps=numDroppedMaxPerWindowTraps, lmsTrap=lmsTrap, lms=lms, lotus=lotus, destinationNetAddr=destinationNetAddr, common_mibs=common_mibs, lmsWarning=lmsWarning, forwardingFilterName=forwardingFilterName)
