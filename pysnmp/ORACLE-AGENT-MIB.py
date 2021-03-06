#
# PySNMP MIB module ORACLE-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ORACLE-AGENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, ObjectIdentity, Bits, MibIdentifier, enterprises, Integer32, ModuleIdentity, Gauge32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits", "MibIdentifier", "enterprises", "Integer32", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 11)

oracle = MibIdentifier((1, 3, 6, 1, 4, 1, 111))
oraAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 12))
oraAgentObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 12, 1))
oraAgentEventTable = MibTable((1, 3, 6, 1, 4, 1, 111, 12, 1, 1), )
if mibBuilder.loadTexts: oraAgentEventTable.setStatus('mandatory')
oraAgentEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1), ).setIndexNames((0, "ORACLE-AGENT-MIB", "oraAgentEventIndex"))
if mibBuilder.loadTexts: oraAgentEventEntry.setStatus('mandatory')
oraAgentEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventIndex.setStatus('mandatory')
oraAgentEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventName.setStatus('mandatory')
oraAgentEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventID.setStatus('mandatory')
oraAgentEventService = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventService.setStatus('mandatory')
oraAgentEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventTime.setStatus('mandatory')
oraAgentEventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, -1))).clone(namedValues=NamedValues(("warning", 1), ("alert", 2), ("clear", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventSeverity.setStatus('mandatory')
oraAgentEventUser = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventUser.setStatus('mandatory')
oraAgentEventAppID = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventAppID.setStatus('mandatory')
oraAgentEventMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventMessage.setStatus('mandatory')
oraAgentEventArguments = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventArguments.setStatus('mandatory')
oraAgentEventResults = MibTableColumn((1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oraAgentEventResults.setStatus('mandatory')
oraAgentTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 111, 12, 2))
oraAgentEventOcc = NotificationType((1, 3, 6, 1, 4, 1, 111, 12, 2) + (0,2)).setObjects(("ORACLE-AGENT-MIB", "oraAgentEventName"), ("ORACLE-AGENT-MIB", "oraAgentEventID"), ("ORACLE-AGENT-MIB", "oraAgentEventService"), ("ORACLE-AGENT-MIB", "oraAgentEventTime"), ("ORACLE-AGENT-MIB", "oraAgentEventSeverity"), ("ORACLE-AGENT-MIB", "oraAgentEventUser"), ("ORACLE-AGENT-MIB", "oraAgentEventAppID"), ("ORACLE-AGENT-MIB", "oraAgentEventMessage"), ("ORACLE-AGENT-MIB", "oraAgentEventArguments"), ("ORACLE-AGENT-MIB", "oraAgentEventResults"))
mibBuilder.exportSymbols("ORACLE-AGENT-MIB", oraAgentEventSeverity=oraAgentEventSeverity, oraAgentEventEntry=oraAgentEventEntry, oraAgentEventUser=oraAgentEventUser, oraAgentEventOcc=oraAgentEventOcc, oraAgentEventAppID=oraAgentEventAppID, oracle=oracle, oraAgentEventResults=oraAgentEventResults, oraAgentEventArguments=oraAgentEventArguments, oraAgent=oraAgent, oraAgentEventService=oraAgentEventService, oraAgentEventTable=oraAgentEventTable, oraAgentEventName=oraAgentEventName, oraAgentEventID=oraAgentEventID, oraAgentEventTime=oraAgentEventTime, DateAndTime=DateAndTime, oraAgentEventMessage=oraAgentEventMessage, oraAgentTraps=oraAgentTraps, oraAgentObjects=oraAgentObjects, oraAgentEventIndex=oraAgentEventIndex)
