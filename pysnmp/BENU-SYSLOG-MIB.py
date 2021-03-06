#
# PySNMP MIB module BENU-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BENU-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:20:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, MibIdentifier, IpAddress, iso, TimeTicks, ObjectIdentity, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "iso", "TimeTicks", "ObjectIdentity", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 3))
benuSyslog.setRevisions(('2015-01-09 00:00', '2014-11-06 00:00', '2013-11-22 00:00',))
if mibBuilder.loadTexts: benuSyslog.setLastUpdated('201501090000Z')
if mibBuilder.loadTexts: benuSyslog.setOrganization('Benu Networks')
bSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 3, 0))
bSyslogSize = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSyslogSize.setStatus('current')
bSyslogMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4096, 5242880)).clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogMaxSize.setStatus('current')
bSyslogServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogServerEnable.setStatus('current')
bSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4), )
if mibBuilder.loadTexts: bSyslogServerTable.setStatus('current')
bSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1), ).setIndexNames((0, "BENU-SYSLOG-MIB", "bSyslogServerIndex"))
if mibBuilder.loadTexts: bSyslogServerEntry.setStatus('current')
bSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bSyslogServerIndex.setStatus('current')
bSyslogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSyslogServerAddress.setStatus('current')
bSyslogServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 3), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSyslogServerPort.setStatus('current')
bSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergencies", 0), ("alerts", 1), ("critical", 2), ("errors", 3), ("warnings", 4), ("notifications", 5), ("informational", 6), ("debugging", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogSeverity.setStatus('current')
bSyslogConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergencies", 0), ("alerts", 1), ("critical", 2), ("errors", 3), ("warnings", 4), ("notifications", 5), ("informational", 6), ("debugging", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogConsoleSeverity.setStatus('current')
bSyslogClear = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogClear.setStatus('current')
mibBuilder.exportSymbols("BENU-SYSLOG-MIB", bSyslogSeverity=bSyslogSeverity, benuSyslog=benuSyslog, bSyslogConsoleSeverity=bSyslogConsoleSeverity, bSyslogMaxSize=bSyslogMaxSize, bSyslogServerEnable=bSyslogServerEnable, bSyslogServerIndex=bSyslogServerIndex, bSyslogSize=bSyslogSize, bSyslogClear=bSyslogClear, bSyslogServerAddress=bSyslogServerAddress, bSyslogNotifications=bSyslogNotifications, bSyslogServerEntry=bSyslogServerEntry, bSyslogServerPort=bSyslogServerPort, PYSNMP_MODULE_ID=benuSyslog, bSyslogServerTable=bSyslogServerTable)
