#
# PySNMP MIB module ZHONE-GEN-WTN-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-GEN-WTN-MONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneModules, zhoneGenWtn = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneGenWtn")
zhoneGenWtnMonitorModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 102))
zhoneGenWtnMonitorModule.setRevisions(('1901-05-25 21:36',))
if mibBuilder.loadTexts: zhoneGenWtnMonitorModule.setLastUpdated('0009281216Z')
if mibBuilder.loadTexts: zhoneGenWtnMonitorModule.setOrganization('Zhone Technologies, Inc.')
wtnMonitor = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 9, 1))
if mibBuilder.loadTexts: wtnMonitor.setStatus('current')
wtnLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 9, 1, 1), Bits().clone(namedValues=NamedValues(("diag", 0), ("operational", 1), ("lineInterface", 2), ("radio", 3), ("local", 4), ("remote", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wtnLedStatus.setStatus('current')
wtnAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 9, 1, 2), Bits().clone(namedValues=NamedValues(("minorAlarm", 0), ("criticalAlarm", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wtnAlarmStatus.setStatus('current')
radioLinkConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 9, 2))
if mibBuilder.loadTexts: radioLinkConfiguration.setStatus('current')
wtnLinkName = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 9, 2, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wtnLinkName.setStatus('current')
mibBuilder.exportSymbols("ZHONE-GEN-WTN-MONITOR-MIB", radioLinkConfiguration=radioLinkConfiguration, wtnAlarmStatus=wtnAlarmStatus, PYSNMP_MODULE_ID=zhoneGenWtnMonitorModule, zhoneGenWtnMonitorModule=zhoneGenWtnMonitorModule, wtnLinkName=wtnLinkName, wtnLedStatus=wtnLedStatus, wtnMonitor=wtnMonitor)
