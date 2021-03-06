#
# PySNMP MIB module CENTILLION-SYSTEM-EVENT-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-SYSTEM-EVENT-LOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
PortId, sysEvtLogMgmt, CardId = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "PortId", "sysEvtLogMgmt", "CardId")
TimeIntervalSec, = mibBuilder.importSymbols("S5-TCS-MIB", "TimeIntervalSec")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, Counter32, NotificationType, ModuleIdentity, MibIdentifier, Integer32, Gauge32, Bits, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Counter32", "NotificationType", "ModuleIdentity", "MibIdentifier", "Integer32", "Gauge32", "Bits", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sysEvtLogDuration = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 1), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogDuration.setStatus('mandatory')
sysEvtLogPreFilterEntityMap = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8).clone(hexValue="FFFFFFFFFFFFFFFF")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogPreFilterEntityMap.setStatus('mandatory')
sysEvtLogPreFilterSeverity = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))).clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogPreFilterSeverity.setStatus('mandatory')
sysEvtLogSlotPreFilterTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4), )
if mibBuilder.loadTexts: sysEvtLogSlotPreFilterTable.setStatus('mandatory')
sysEvtLogSlotPreFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4, 1), ).setIndexNames((0, "CENTILLION-SYSTEM-EVENT-LOG-MIB", "sysEvtLogSlotPreFilterCardId"))
if mibBuilder.loadTexts: sysEvtLogSlotPreFilterEntry.setStatus('mandatory')
sysEvtLogSlotPreFilterCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4, 1, 1), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysEvtLogSlotPreFilterCardId.setStatus('mandatory')
sysEvtLogSlotPreFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogSlotPreFilterControl.setStatus('mandatory')
sysEvtLogPortPreFilterTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5), )
if mibBuilder.loadTexts: sysEvtLogPortPreFilterTable.setStatus('mandatory')
sysEvtLogPortPreFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1), ).setIndexNames((0, "CENTILLION-SYSTEM-EVENT-LOG-MIB", "sysEvtLogPortPreFilterCardId"), (0, "CENTILLION-SYSTEM-EVENT-LOG-MIB", "sysEvtLogPortPreFilterPortId"))
if mibBuilder.loadTexts: sysEvtLogPortPreFilterEntry.setStatus('mandatory')
sysEvtLogPortPreFilterCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1, 1), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysEvtLogPortPreFilterCardId.setStatus('mandatory')
sysEvtLogPortPreFilterPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1, 2), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysEvtLogPortPreFilterPortId.setStatus('mandatory')
sysEvtLogPortPreFilterControl = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogPortPreFilterControl.setStatus('mandatory')
sysEvtLogDestMap = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogDestMap.setStatus('mandatory')
sysEvtLogSysLogCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7))
sysEvtLogSysLogHostIp = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7, 1), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogSysLogHostIp.setStatus('mandatory')
sysEvtLogSysLogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("panic", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))).clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogSysLogSeverity.setStatus('mandatory')
sysEvtLogSysLogFacility = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("local0", 1), ("local1", 2), ("local2", 3), ("local3", 4), ("local4", 5), ("local5", 6), ("local6", 7), ("local7", 8))).clone('local0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogSysLogFacility.setStatus('mandatory')
sysEvtLogTftpsaveCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8))
sysEvtLogTftpsaveHostIp = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8, 1), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogTftpsaveHostIp.setStatus('mandatory')
sysEvtLogTftpsaveFileName = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogTftpsaveFileName.setStatus('mandatory')
sysEvtLogTftpsaveMaxMsgCount = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysEvtLogTftpsaveMaxMsgCount.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-SYSTEM-EVENT-LOG-MIB", sysEvtLogSlotPreFilterCardId=sysEvtLogSlotPreFilterCardId, sysEvtLogSysLogFacility=sysEvtLogSysLogFacility, sysEvtLogSlotPreFilterControl=sysEvtLogSlotPreFilterControl, sysEvtLogTftpsaveCfg=sysEvtLogTftpsaveCfg, sysEvtLogPortPreFilterTable=sysEvtLogPortPreFilterTable, sysEvtLogTftpsaveMaxMsgCount=sysEvtLogTftpsaveMaxMsgCount, sysEvtLogSysLogCfg=sysEvtLogSysLogCfg, sysEvtLogPortPreFilterPortId=sysEvtLogPortPreFilterPortId, sysEvtLogPreFilterEntityMap=sysEvtLogPreFilterEntityMap, sysEvtLogPortPreFilterControl=sysEvtLogPortPreFilterControl, sysEvtLogDuration=sysEvtLogDuration, sysEvtLogSlotPreFilterEntry=sysEvtLogSlotPreFilterEntry, sysEvtLogSysLogSeverity=sysEvtLogSysLogSeverity, sysEvtLogPortPreFilterCardId=sysEvtLogPortPreFilterCardId, sysEvtLogSysLogHostIp=sysEvtLogSysLogHostIp, sysEvtLogTftpsaveFileName=sysEvtLogTftpsaveFileName, sysEvtLogPreFilterSeverity=sysEvtLogPreFilterSeverity, sysEvtLogDestMap=sysEvtLogDestMap, sysEvtLogPortPreFilterEntry=sysEvtLogPortPreFilterEntry, sysEvtLogSlotPreFilterTable=sysEvtLogSlotPreFilterTable, sysEvtLogTftpsaveHostIp=sysEvtLogTftpsaveHostIp)
