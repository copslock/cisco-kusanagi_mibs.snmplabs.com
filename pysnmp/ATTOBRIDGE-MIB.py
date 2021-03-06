#
# PySNMP MIB module ATTOBRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATTOBRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, TimeTicks, Gauge32, Bits, ModuleIdentity, IpAddress, Integer32, enterprises, Counter32, Counter64, Unsigned32, experimental, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "TimeTicks", "Gauge32", "Bits", "ModuleIdentity", "IpAddress", "Integer32", "enterprises", "Counter32", "Counter64", "Unsigned32", "experimental", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
attotech = MibIdentifier((1, 3, 6, 1, 4, 1, 4547))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1))
bridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 4547, 1, 2))
if mibBuilder.loadTexts: bridge.setLastUpdated('200509200000Z')
if mibBuilder.loadTexts: bridge.setOrganization('ATTO Technology, Inc.')
bridgeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 2, 1))
bridgeStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2))
bridgeTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3))
trapsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4547, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapsEnabled.setStatus('mandatory')
snmpUpdatesEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4547, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUpdatesEnabled.setStatus('mandatory')
snmpExtendedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4547, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpExtendedEnabled.setStatus('mandatory')
tempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1), )
if mibBuilder.loadTexts: tempSensorTable.setStatus('mandatory')
tempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1), ).setIndexNames((0, "ATTOBRIDGE-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: tempSensorEntry.setStatus('mandatory')
tempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorIndex.setStatus('mandatory')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('mandatory')
temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('mandatory')
voltageSensorTable = MibTable((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2), )
if mibBuilder.loadTexts: voltageSensorTable.setStatus('mandatory')
voltageSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1), ).setIndexNames((0, "ATTOBRIDGE-MIB", "voltageSensorIndex"))
if mibBuilder.loadTexts: voltageSensorEntry.setStatus('mandatory')
voltageSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSensorIndex.setStatus('mandatory')
voltageSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSensorStatus.setStatus('mandatory')
voltage = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage.setStatus('mandatory')
deviceCount = MibScalar((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceCount.setStatus('mandatory')
deviceCacheTable = MibTable((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5), )
if mibBuilder.loadTexts: deviceCacheTable.setStatus('mandatory')
deviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1), ).setIndexNames((0, "ATTOBRIDGE-MIB", "deviceCacheIndex"))
if mibBuilder.loadTexts: deviceEntry.setStatus('mandatory')
deviceCacheIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceCacheIndex.setStatus('mandatory')
deviceSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSource.setStatus('mandatory')
deviceDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDestination.setStatus('mandatory')
deviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('mandatory')
deviceVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceVendor.setStatus('mandatory')
deviceProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceProduct.setStatus('mandatory')
deviceRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceRevision.setStatus('mandatory')
deviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("offline", 0), ("online", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceState.setStatus('mandatory')
errorCount = MibScalar((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorCount.setStatus('mandatory')
errorsSinceUpdate = MibScalar((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorsSinceUpdate.setStatus('mandatory')
errorTable = MibTable((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8), )
if mibBuilder.loadTexts: errorTable.setStatus('mandatory')
errorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1), ).setIndexNames((0, "ATTOBRIDGE-MIB", "errorIndex"))
if mibBuilder.loadTexts: errorEntry.setStatus('mandatory')
errorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorIndex.setStatus('mandatory')
errorDateStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorDateStamp.setStatus('mandatory')
errorTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorTimeStamp.setStatus('mandatory')
errorInitiator = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorInitiator.setStatus('mandatory')
errorSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorSource.setStatus('mandatory')
errorOpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorOpCode.setStatus('mandatory')
errorSenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorSenseKey.setStatus('mandatory')
errorASC = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorASC.setStatus('mandatory')
errorASCQ = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorASCQ.setStatus('mandatory')
errorLogSense = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorLogSense.setStatus('mandatory')
trapMaxClients = MibScalar((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapMaxClients.setStatus('mandatory')
trapClientTable = MibTable((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3), )
if mibBuilder.loadTexts: trapClientTable.setStatus('mandatory')
trapClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1), ).setIndexNames((0, "ATTOBRIDGE-MIB", "trapClientIndex"))
if mibBuilder.loadTexts: trapClientEntry.setStatus('mandatory')
trapClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapClientIndex.setStatus('mandatory')
trapClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapClientIpAddress.setStatus('mandatory')
trapClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapClientPort.setStatus('mandatory')
trapClientFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("critical", 2), ("warning", 3), ("informational", 4), ("all", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapClientFilter.setStatus('mandatory')
trapClientRowState = MibTableColumn((1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rowDestroy", 1), ("rowInactive", 2), ("rowActive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapClientRowState.setStatus('mandatory')
bridgeTempStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 4547) + (0,1)).setObjects(("ATTOBRIDGE-MIB", "tempSensorIndex"), ("ATTOBRIDGE-MIB", "tempSensorStatus"), ("ATTOBRIDGE-MIB", "temperature"))
bridgeVoltageStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 4547) + (0,2)).setObjects(("ATTOBRIDGE-MIB", "voltageSensorIndex"), ("ATTOBRIDGE-MIB", "voltageSensorStatus"), ("ATTOBRIDGE-MIB", "voltage"))
bridgeDeviceTransition = NotificationType((1, 3, 6, 1, 4, 1, 4547) + (0,4)).setObjects(("ATTOBRIDGE-MIB", "deviceCacheIndex"), ("ATTOBRIDGE-MIB", "deviceSource"), ("ATTOBRIDGE-MIB", "deviceState"))
bridgeDeviceError = NotificationType((1, 3, 6, 1, 4, 1, 4547) + (0,5)).setObjects(("ATTOBRIDGE-MIB", "errorSource"), ("ATTOBRIDGE-MIB", "errorOpCode"), ("ATTOBRIDGE-MIB", "errorSenseKey"), ("ATTOBRIDGE-MIB", "errorASC"), ("ATTOBRIDGE-MIB", "errorASCQ"), ("ATTOBRIDGE-MIB", "errorsSinceUpdate"))
mibBuilder.exportSymbols("ATTOBRIDGE-MIB", errorIndex=errorIndex, bridgeStatus=bridgeStatus, deviceCacheTable=deviceCacheTable, voltageSensorStatus=voltageSensorStatus, trapClientTable=trapClientTable, tempSensorEntry=tempSensorEntry, deviceRevision=deviceRevision, voltageSensorIndex=voltageSensorIndex, voltageSensorTable=voltageSensorTable, errorTimeStamp=errorTimeStamp, errorDateStamp=errorDateStamp, errorCount=errorCount, bridgeDeviceError=bridgeDeviceError, bridgeDeviceTransition=bridgeDeviceTransition, trapMaxClients=trapMaxClients, errorTable=errorTable, snmpUpdatesEnabled=snmpUpdatesEnabled, bridge=bridge, deviceSource=deviceSource, voltageSensorEntry=voltageSensorEntry, trapClientRowState=trapClientRowState, bridgeTempStatusChanged=bridgeTempStatusChanged, trapsEnabled=trapsEnabled, tempSensorStatus=tempSensorStatus, tempSensorTable=tempSensorTable, trapClientIndex=trapClientIndex, trapClientIpAddress=trapClientIpAddress, errorInitiator=errorInitiator, deviceProduct=deviceProduct, errorASCQ=errorASCQ, errorOpCode=errorOpCode, errorSource=errorSource, trapClientFilter=trapClientFilter, products=products, deviceType=deviceType, voltage=voltage, errorEntry=errorEntry, trapClientEntry=trapClientEntry, deviceVendor=deviceVendor, temperature=temperature, tempSensorIndex=tempSensorIndex, errorSenseKey=errorSenseKey, trapClientPort=trapClientPort, errorLogSense=errorLogSense, PYSNMP_MODULE_ID=bridge, bridgeVoltageStatusChanged=bridgeVoltageStatusChanged, snmpExtendedEnabled=snmpExtendedEnabled, deviceCount=deviceCount, deviceCacheIndex=deviceCacheIndex, deviceEntry=deviceEntry, deviceDestination=deviceDestination, attotech=attotech, errorsSinceUpdate=errorsSinceUpdate, bridgeConfig=bridgeConfig, errorASC=errorASC, deviceState=deviceState, bridgeTrapInfo=bridgeTrapInfo)
