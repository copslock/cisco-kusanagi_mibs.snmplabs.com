#
# PySNMP MIB module MANTRA-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MANTRA-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
minutes, devName, mateHost, host, myHost, pepName, oldFile, snName, result, unknownDeviceTrapContents, newFile, group, reason, myPort, sbProducerHost, sbProducerPort, runStatus, name, file, matePort, domain, port, deviceType = mibBuilder.importSymbols("AGGREGATED-EXT-MIB", "minutes", "devName", "mateHost", "host", "myHost", "pepName", "oldFile", "snName", "result", "unknownDeviceTrapContents", "newFile", "group", "reason", "myPort", "sbProducerHost", "sbProducerPort", "runStatus", "name", "file", "matePort", "domain", "port", "deviceType")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, ObjectIdentity, IpAddress, ObjectName, Unsigned32, enterprises, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Gauge32, NotificationType, snmpModules, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "IpAddress", "ObjectName", "Unsigned32", "enterprises", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Gauge32", "NotificationType", "snmpModules", "Integer32")
DisplayString, RowStatus, TestAndIncr, TimeStamp, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TestAndIncr", "TimeStamp", "TextualConvention", "TruthValue")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
mantraTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0))
if mibBuilder.loadTexts: mantraTraps.setLastUpdated('240701')
if mibBuilder.loadTexts: mantraTraps.setOrganization('Lucent Technologies')
lssProcessUnstartable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 0)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessUnstartable.setStatus('current')
lssProcessCreated = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 1)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessCreated.setStatus('current')
lssProcessDied = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 2)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessDied.setStatus('current')
lssProcessKilled = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 3)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessKilled.setStatus('current')
lssProcessStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 4)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessStateChange.setStatus('current')
lssInternalError = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 5)).setObjects(("AGGREGATED-EXT-MIB", "unknownDeviceTrapContents"))
if mibBuilder.loadTexts: lssInternalError.setStatus('current')
lssElementSuccessfulConnection = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 6)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"))
if mibBuilder.loadTexts: lssElementSuccessfulConnection.setStatus('current')
lssElementFileUnReadable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 7)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"))
if mibBuilder.loadTexts: lssElementFileUnReadable.setStatus('current')
lssElementDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 8)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"))
if mibBuilder.loadTexts: lssElementDisconnect.setStatus('current')
lssElementUnReachable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 9)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"), ("AGGREGATED-EXT-MIB", "minutes"))
if mibBuilder.loadTexts: lssElementUnReachable.setStatus('current')
logFileChanged = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 10)).setObjects(("AGGREGATED-EXT-MIB", "oldFile"), ("AGGREGATED-EXT-MIB", "newFile"), ("AGGREGATED-EXT-MIB", "result"), ("AGGREGATED-EXT-MIB", "reason"))
if mibBuilder.loadTexts: logFileChanged.setStatus('current')
lssFTMateConnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 11)).setObjects(("AGGREGATED-EXT-MIB", "snName"), ("AGGREGATED-EXT-MIB", "myHost"), ("AGGREGATED-EXT-MIB", "myPort"), ("AGGREGATED-EXT-MIB", "mateHost"), ("AGGREGATED-EXT-MIB", "matePort"))
if mibBuilder.loadTexts: lssFTMateConnect.setStatus('current')
lssFTMateDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 12)).setObjects(("AGGREGATED-EXT-MIB", "snName"), ("AGGREGATED-EXT-MIB", "myHost"), ("AGGREGATED-EXT-MIB", "myPort"), ("AGGREGATED-EXT-MIB", "mateHost"), ("AGGREGATED-EXT-MIB", "matePort"))
if mibBuilder.loadTexts: lssFTMateDisconnect.setStatus('current')
sbProducerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 13)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerUnreachable.setStatus('current')
sbProducerConnected = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 14)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerConnected.setStatus('current')
sbProducerRegistered = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 15)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerRegistered.setStatus('current')
sbProducerDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 16)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerDisconnected.setStatus('current')
sbProducerCannotRegister = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 17)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerCannotRegister.setStatus('current')
sbProducerCannotDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 18)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerCannotDisconnect.setStatus('current')
mibBuilder.exportSymbols("MANTRA-TRAP-MIB", softSwitch=softSwitch, sbProducerCannotDisconnect=sbProducerCannotDisconnect, logFileChanged=logFileChanged, sbProducerDisconnected=sbProducerDisconnected, lssProcessDied=lssProcessDied, sbProducerRegistered=sbProducerRegistered, products=products, lssProcessUnstartable=lssProcessUnstartable, lssFTMateConnect=lssFTMateConnect, lucent=lucent, PYSNMP_MODULE_ID=mantraTraps, lssElementUnReachable=lssElementUnReachable, lssProcessStateChange=lssProcessStateChange, lssElementDisconnect=lssElementDisconnect, sbProducerCannotRegister=sbProducerCannotRegister, lssProcessCreated=lssProcessCreated, lssElementSuccessfulConnection=lssElementSuccessfulConnection, lssElementFileUnReadable=lssElementFileUnReadable, mantraTraps=mantraTraps, sbProducerUnreachable=sbProducerUnreachable, lssProcessKilled=lssProcessKilled, lssFTMateDisconnect=lssFTMateDisconnect, lssInternalError=lssInternalError, sbProducerConnected=sbProducerConnected)
