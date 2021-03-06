#
# PySNMP MIB module SONUS-ALARM-CONTACT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-ALARM-CONTACT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Counter32, IpAddress, ModuleIdentity, Bits, TimeTicks, Unsigned32, Gauge32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Counter32", "IpAddress", "ModuleIdentity", "Bits", "TimeTicks", "Unsigned32", "Gauge32", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonusShelfIndex, sonusEventClass, sonusEventDescription, sonusEventLevel = mibBuilder.importSymbols("SONUS-COMMON-MIB", "sonusShelfIndex", "sonusEventClass", "sonusEventDescription", "sonusEventLevel")
sonusSystemMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusSystemMIBs")
SonusBoolean, SonusShelfIndex, SonusAdminState = mibBuilder.importSymbols("SONUS-TC", "SonusBoolean", "SonusShelfIndex", "SonusAdminState")
sonusAlarmManagerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6))
if mibBuilder.loadTexts: sonusAlarmManagerMIB.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: sonusAlarmManagerMIB.setOrganization('Sonus Networks, Inc.')
sonusAlarmManagerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1))
sonusAlarmOutAdmnTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1), )
if mibBuilder.loadTexts: sonusAlarmOutAdmnTable.setStatus('current')
sonusAlarmOutAdmnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1), ).setIndexNames((0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutAdmnShelfIndex"), (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutAdmnRelayIndex"))
if mibBuilder.loadTexts: sonusAlarmOutAdmnEntry.setStatus('current')
sonusAlarmOutAdmnShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 1), SonusShelfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmOutAdmnShelfIndex.setStatus('current')
sonusAlarmOutAdmnRelayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("shelfpwr-1", 1), ("critical-2", 2), ("major-3", 3), ("minor-4", 4), ("user-5", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmOutAdmnRelayIndex.setStatus('current')
sonusAlarmOutAdmnOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 3), SonusAdminState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAlarmOutAdmnOperState.setStatus('current')
sonusAlarmOutAdmnValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("alarm", 2))).clone('clear')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAlarmOutAdmnValue.setStatus('current')
sonusAlarmOutAdmnSense = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAlarmOutAdmnSense.setStatus('current')
sonusAlarmOutAdmnStartDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAlarmOutAdmnStartDelay.setStatus('current')
sonusAlarmOutAdmnCutoff = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusAlarmOutAdmnCutoff.setStatus('current')
sonusAlarmOutStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2), )
if mibBuilder.loadTexts: sonusAlarmOutStatTable.setStatus('current')
sonusAlarmOutStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1), ).setIndexNames((0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutStatShelfIndex"), (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmOutStatRelayIndex"))
if mibBuilder.loadTexts: sonusAlarmOutStatEntry.setStatus('current')
sonusAlarmOutStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 1), SonusShelfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmOutStatShelfIndex.setStatus('current')
sonusAlarmOutStatRelayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("shelfpwr-1", 1), ("critical-2", 2), ("major-3", 3), ("minor-4", 4), ("user-5", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmOutStatRelayIndex.setStatus('current')
sonusAlarmOutStatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmOutStatStatus.setStatus('current')
sonusAlarmOutStatStartDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 2, 1, 4), SonusBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmOutStatStartDelay.setStatus('current')
sonusAlarmInStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3), )
if mibBuilder.loadTexts: sonusAlarmInStatTable.setStatus('current')
sonusAlarmInStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1), ).setIndexNames((0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmInStatShelfIndex"), (0, "SONUS-ALARM-CONTACT-MIB", "sonusAlarmInStatPort"))
if mibBuilder.loadTexts: sonusAlarmInStatEntry.setStatus('current')
sonusAlarmInStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1, 1), SonusShelfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmInStatShelfIndex.setStatus('current')
sonusAlarmInStatPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmInStatPort.setStatus('current')
sonusAlarmInStatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("closed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmInStatStatus.setStatus('current')
sonusAlarmManagerMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2))
sonusAlarmManagerMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 0))
sonusAlarmManagerMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 1))
sonusAlarmPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmPortIndex.setStatus('current')
sonusAlarmPortState = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("closed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAlarmPortState.setStatus('current')
sonusAlarmManagerInboundNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 1, 6, 2, 0, 1)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-ALARM-CONTACT-MIB", "sonusAlarmPortIndex"), ("SONUS-ALARM-CONTACT-MIB", "sonusAlarmPortState"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAlarmManagerInboundNotification.setStatus('current')
mibBuilder.exportSymbols("SONUS-ALARM-CONTACT-MIB", sonusAlarmPortIndex=sonusAlarmPortIndex, sonusAlarmOutStatTable=sonusAlarmOutStatTable, sonusAlarmOutAdmnRelayIndex=sonusAlarmOutAdmnRelayIndex, sonusAlarmManagerInboundNotification=sonusAlarmManagerInboundNotification, sonusAlarmInStatStatus=sonusAlarmInStatStatus, sonusAlarmOutAdmnValue=sonusAlarmOutAdmnValue, sonusAlarmOutStatStartDelay=sonusAlarmOutStatStartDelay, sonusAlarmOutAdmnTable=sonusAlarmOutAdmnTable, sonusAlarmManagerMIBNotificationsPrefix=sonusAlarmManagerMIBNotificationsPrefix, sonusAlarmInStatEntry=sonusAlarmInStatEntry, sonusAlarmOutAdmnCutoff=sonusAlarmOutAdmnCutoff, sonusAlarmInStatTable=sonusAlarmInStatTable, sonusAlarmOutAdmnStartDelay=sonusAlarmOutAdmnStartDelay, sonusAlarmInStatShelfIndex=sonusAlarmInStatShelfIndex, sonusAlarmManagerMIBObjects=sonusAlarmManagerMIBObjects, sonusAlarmOutStatStatus=sonusAlarmOutStatStatus, sonusAlarmOutStatRelayIndex=sonusAlarmOutStatRelayIndex, sonusAlarmOutStatEntry=sonusAlarmOutStatEntry, sonusAlarmManagerMIBNotificationsObjects=sonusAlarmManagerMIBNotificationsObjects, sonusAlarmOutAdmnShelfIndex=sonusAlarmOutAdmnShelfIndex, sonusAlarmManagerMIB=sonusAlarmManagerMIB, sonusAlarmInStatPort=sonusAlarmInStatPort, sonusAlarmPortState=sonusAlarmPortState, PYSNMP_MODULE_ID=sonusAlarmManagerMIB, sonusAlarmManagerMIBNotifications=sonusAlarmManagerMIBNotifications, sonusAlarmOutAdmnEntry=sonusAlarmOutAdmnEntry, sonusAlarmOutAdmnSense=sonusAlarmOutAdmnSense, sonusAlarmOutAdmnOperState=sonusAlarmOutAdmnOperState, sonusAlarmOutStatShelfIndex=sonusAlarmOutStatShelfIndex)
