#
# PySNMP MIB module Dell-Vendor-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-Vendor-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, MibIdentifier, ModuleIdentity, Unsigned32, Bits, IpAddress, Gauge32, enterprises, NotificationType, iso, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "IpAddress", "Gauge32", "enterprises", "NotificationType", "iso", "TimeTicks", "Counter32")
DisplayString, RowStatus, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
dellLan = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895))
dellLanStandard = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000))
dellLanCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1))
dellLanExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2))
powerConnectVendorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 3000))
powerConnectVendorMIB.setRevisions(('2012-05-07 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: powerConnectVendorMIB.setRevisionsDescriptions(('The private MIB module definition for the Dell PowerConnect Devices. This MIB allows PowerConnect devices to be integrated into Dell ITA management system.',))
if mibBuilder.loadTexts: powerConnectVendorMIB.setLastUpdated('201205071200Z')
if mibBuilder.loadTexts: powerConnectVendorMIB.setOrganization('Dell Inc.')
if mibBuilder.loadTexts: powerConnectVendorMIB.setContactInfo('support.dell.com')
if mibBuilder.loadTexts: powerConnectVendorMIB.setDescription('Adding new objects - Dell PPID, Revision, Express Service Code.')
class EnvMonState(TextualConvention, Integer32):
    description = 'Represents the state of a device being monitored. Valid values are: normal(1): the environment is good, such as low temperature. warning(2): the environment is bad, such as temperature above normal operation range but not too high. critical(3): the environment is very bad, such as temperature much higher than normal operation limit. shutdown(4): the environment is the worst, the system should be shutdown immediately. notPresent(5): the environmental monitor is not present, such as temperature sensors do not exist. notFunctioning(6): the environmental monitor does not function properly, such as a temperature sensor generates a abnormal data like 1000 C. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notPresent", 5), ("notFunctioning", 6))

dellVendorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1))
dellVendorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2))
hardware = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2))
productIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100))
productStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110))
productIdentificationDisplayName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationDisplayName.setStatus('current')
if mibBuilder.loadTexts: productIdentificationDisplayName.setDescription('Name of this product for display purposes.')
productIdentificationDescription = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationDescription.setStatus('current')
if mibBuilder.loadTexts: productIdentificationDescription.setDescription('A short description of this product such as: Ethernet Router Switch.')
productIdentificationVendor = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationVendor.setStatus('current')
if mibBuilder.loadTexts: productIdentificationVendor.setDescription('The name of the product manufacturer, such as: Dell Inc.')
productIdentificationVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationVersion.setStatus('current')
if mibBuilder.loadTexts: productIdentificationVersion.setDescription('The version of this product.')
productIdentificationBuildNumber = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationBuildNumber.setStatus('current')
if mibBuilder.loadTexts: productIdentificationBuildNumber.setDescription('The software build number of the product.')
productIdentificationURL = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationURL.setStatus('current')
if mibBuilder.loadTexts: productIdentificationURL.setDescription('The URL of the web-based application to manage this device, should the device provide one. The format of the value held by this object is: http://<device IP address>.')
productIdentificationDeviceNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationDeviceNetworkName.setStatus('current')
if mibBuilder.loadTexts: productIdentificationDeviceNetworkName.setDescription('Device Name.')
productIdentificationPerUnitTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8), )
if mibBuilder.loadTexts: productIdentificationPerUnitTable.setStatus('current')
if mibBuilder.loadTexts: productIdentificationPerUnitTable.setDescription('Identification specific to product instance and, in case of stackable products, per unit. If the product is not stackable, it will be considered a stack of one unit and therefore this table will contain one conceptual row only.')
productIdentificationPerUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1), ).setIndexNames((0, "Dell-Vendor-MIB", "productIdentificationPerBoxIndex"))
if mibBuilder.loadTexts: productIdentificationPerUnitEntry.setStatus('current')
if mibBuilder.loadTexts: productIdentificationPerUnitEntry.setDescription('This row applies to a unit in a stackable product. ')
productIdentificationPerBoxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationPerBoxIndex.setStatus('current')
if mibBuilder.loadTexts: productIdentificationPerBoxIndex.setDescription("The index of the stack unit to which this conceptual row corresponds. Note that the index will be the same index as the index of a 'chassis' physical entity in the entity MIB of the product.")
productIdentificationSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationSerialNumber.setStatus('current')
if mibBuilder.loadTexts: productIdentificationSerialNumber.setDescription('Serial number of the product.')
productIdentificationAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationAssetTag.setStatus('current')
if mibBuilder.loadTexts: productIdentificationAssetTag.setDescription('Asset tag of the product.')
productIdentificationServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationServiceTag.setStatus('current')
if mibBuilder.loadTexts: productIdentificationServiceTag.setDescription('Service tag of the product.')
productIdentificationChassisServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationChassisServiceTag.setStatus('current')
if mibBuilder.loadTexts: productIdentificationChassisServiceTag.setDescription('Chassis Service tag of the product.')
productIdentificationBootromVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationBootromVersion.setStatus('current')
if mibBuilder.loadTexts: productIdentificationBootromVersion.setDescription('The boot image version of the product.')
productIdentificationPiecePartID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationPiecePartID.setStatus('current')
if mibBuilder.loadTexts: productIdentificationPiecePartID.setDescription('The piece part id of the product.')
productIdentificationPPIDRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationPPIDRevision.setStatus('current')
if mibBuilder.loadTexts: productIdentificationPPIDRevision.setDescription('The PPID revision of the product.')
productIdentificationExpressServiceCode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 8, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIdentificationExpressServiceCode.setStatus('current')
if mibBuilder.loadTexts: productIdentificationExpressServiceCode.setDescription('The express cervice code of the product.')
productIdentificationBannerMotdAckMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 100, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: productIdentificationBannerMotdAckMode.setStatus('current')
if mibBuilder.loadTexts: productIdentificationBannerMotdAckMode.setDescription("If enable is selected, user will be required to acknowledge the banner displayed on the console. The user would have to type 'y' or 'n' to continue to the login prompt. If n is typed, the session is terminated and no future communication is allowed on that session. However, serial connection will not get terminated if user does not enter 'y'. Use disable option to disable banner acknowledge.")
productStatusGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4, 5))).clone(namedValues=NamedValues(("ok", 3), ("non-critical", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productStatusGlobalStatus.setStatus('current')
if mibBuilder.loadTexts: productStatusGlobalStatus.setDescription('Current status of the product.This is a rollup for the entire product. The status is intended to give initiative to a snmp monitor to get further data when this status is abnormal. This variable can take the following values: 3: OK If fans and power supplies are functioning and the system did not reboot because of a HW watchdog failure or a SW fatal error condition. 4: Non-critical If at least one power supply is not functional or the system rebooted at least once because of a HW watchdog failure or a SW fatal error condition. 5: Critical If at least one fan is not functional, possibly causing a dangerous warming up of the device.')
productStatusLastGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4, 5))).clone(namedValues=NamedValues(("ok", 3), ("non-critical", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productStatusLastGlobalStatus.setStatus('current')
if mibBuilder.loadTexts: productStatusLastGlobalStatus.setDescription('The status before the current status which induced an initiative to issue a global status change trap.')
productStatusTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productStatusTimeStamp.setStatus('current')
if mibBuilder.loadTexts: productStatusTimeStamp.setDescription('The last time that the product global status has been updated. The time will be given in TimeTicks')
productStatusGetTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productStatusGetTimeOut.setStatus('current')
if mibBuilder.loadTexts: productStatusGetTimeOut.setDescription('Suggested time out value in milliseconds for how long the SNMP getter should wait while attempting to poll the product SNMP service.')
productStatusRefreshRate = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productStatusRefreshRate.setStatus('current')
if mibBuilder.loadTexts: productStatusRefreshRate.setDescription('Rate in seconds at which the SNMP service cached data is being updated.')
productStatusGeneratingTrapsFlag = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("true", 1), ("false", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productStatusGeneratingTrapsFlag.setStatus('current')
if mibBuilder.loadTexts: productStatusGeneratingTrapsFlag.setDescription('Indicates if this SNMP service is generating SNMP Traps. This variable can take the following values: 1: true - The device is capable and currently configured to generate traps if necessary. 2: false - The device is not capable of generating traps. 3: disabled - The device is capable but not configured to generate traps. ')
productStatusEnvironment = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7))
envMonFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1), )
if mibBuilder.loadTexts: envMonFanStatusTable.setStatus('current')
if mibBuilder.loadTexts: envMonFanStatusTable.setDescription('The table of fan status maintained by the environmental monitor. Not Supported by Dell Modular Blade Server switches.')
envMonFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1), ).setIndexNames((0, "Dell-Vendor-MIB", "envMonFanStatusIndex"))
if mibBuilder.loadTexts: envMonFanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: envMonFanStatusEntry.setDescription('An entry in the fan status table, representing the status of the associated fan maintained by the environmental monitor. Not Supported by Dell Modular Blade Server switches.')
envMonFanStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanStatusIndex.setStatus('current')
if mibBuilder.loadTexts: envMonFanStatusIndex.setDescription('Unique index for the fan being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning. Not Supported by Dell Modular Blade Server switches.')
envMonFanStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanStatusDescr.setStatus('current')
if mibBuilder.loadTexts: envMonFanStatusDescr.setDescription('Textual description of the fan being instrumented. This description is a short textual label, suitable as a human-sensible identification for the rest of the information in the entry. Not Supported by Dell Modular Blade Server switches.')
envMonFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1, 3), EnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanState.setStatus('current')
if mibBuilder.loadTexts: envMonFanState.setDescription('The mandatory state of the fan being instrumented. Not Supported by Dell Modular Blade Server switches.')
envMonFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanSpeed.setStatus('current')
if mibBuilder.loadTexts: envMonFanSpeed.setDescription('Speed of the fan being instrumented. Not Supported by Dell Modular Blade Server switches.')
envMonSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2), )
if mibBuilder.loadTexts: envMonSupplyStatusTable.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyStatusTable.setDescription('The table of power supply status maintained by the environmental monitor card.')
envMonSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1), ).setIndexNames((0, "Dell-Vendor-MIB", "envMonSupplyStatusIndex"))
if mibBuilder.loadTexts: envMonSupplyStatusEntry.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyStatusEntry.setDescription('An entry in the power supply status table, representing the status of the associated power supply maintained by the environmental monitor card.')
envMonSupplyStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonSupplyStatusIndex.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyStatusIndex.setDescription('Unique index for the power supply being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning.')
envMonSupplyStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonSupplyStatusDescr.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyStatusDescr.setDescription('Textual description of the power supply being instrumented. This description is a short textual label, suitable as a human-sensible identification for the rest of the information in the entry.')
envMonSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 3), EnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonSupplyState.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyState.setDescription('The mandatory state of the power supply being instrumented.')
envMonSupplySource = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ac", 2), ("dc", 3), ("externalPowerSupply", 4), ("internalRedundant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonSupplySource.setStatus('current')
if mibBuilder.loadTexts: envMonSupplySource.setDescription('The power supply source. unknown - Power supply source unknown ac - AC power supply dc - DC power supply externalPowerSupply - External power supply internalRedundant - Internal redundant power supply ')
envMonSupplyCurrentPower = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonSupplyCurrentPower.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyCurrentPower.setDescription('Current power consumption of the power supply being instrumented. 0 - indicates that Current power is not available for related supply.')
envMonSupplyAveragePower = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonSupplyAveragePower.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyAveragePower.setDescription('Average power consumption of the power supply being instrumented. 0 - indicates that Average power is not available for related supply.')
envMonSupplyAvgStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 1, 2, 110, 7, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonSupplyAvgStartTime.setStatus('current')
if mibBuilder.loadTexts: envMonSupplyAvgStartTime.setDescription('The power supply data start. 0 - indicates that power and related start time is not available for supply.')
dellVendorTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2, 1))
dellVendorTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2, 1, 0))
productStatusGlobalStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 3000, 2, 1, 0, 1)).setObjects(("Dell-Vendor-MIB", "productStatusGlobalStatus"), ("Dell-Vendor-MIB", "productStatusLastGlobalStatus"), ("Dell-Vendor-MIB", "productStatusTimeStamp"))
if mibBuilder.loadTexts: productStatusGlobalStatusChange.setStatus('current')
if mibBuilder.loadTexts: productStatusGlobalStatusChange.setDescription('This trap is sent when the product global status changes.')
mibBuilder.exportSymbols("Dell-Vendor-MIB", productStatusGlobalStatus=productStatusGlobalStatus, productStatusEnvironment=productStatusEnvironment, envMonSupplyAveragePower=envMonSupplyAveragePower, envMonSupplySource=envMonSupplySource, dellLanExtension=dellLanExtension, envMonSupplyAvgStartTime=envMonSupplyAvgStartTime, productIdentificationDeviceNetworkName=productIdentificationDeviceNetworkName, productStatus=productStatus, envMonSupplyState=envMonSupplyState, productStatusGetTimeOut=productStatusGetTimeOut, envMonFanStatusDescr=envMonFanStatusDescr, dellVendorTrapsPrefix=dellVendorTrapsPrefix, envMonFanState=envMonFanState, productStatusRefreshRate=productStatusRefreshRate, productIdentificationBuildNumber=productIdentificationBuildNumber, productIdentificationServiceTag=productIdentificationServiceTag, EnvMonState=EnvMonState, PYSNMP_MODULE_ID=powerConnectVendorMIB, dell=dell, dellLanStandard=dellLanStandard, productIdentificationPPIDRevision=productIdentificationPPIDRevision, productIdentificationAssetTag=productIdentificationAssetTag, envMonFanStatusEntry=envMonFanStatusEntry, productIdentificationVersion=productIdentificationVersion, productIdentificationBannerMotdAckMode=productIdentificationBannerMotdAckMode, envMonFanStatusTable=envMonFanStatusTable, productStatusGeneratingTrapsFlag=productStatusGeneratingTrapsFlag, envMonFanStatusIndex=envMonFanStatusIndex, envMonSupplyStatusDescr=envMonSupplyStatusDescr, dellVendorTraps=dellVendorTraps, dellLanCommon=dellLanCommon, productIdentificationPerUnitEntry=productIdentificationPerUnitEntry, productStatusTimeStamp=productStatusTimeStamp, productIdentificationURL=productIdentificationURL, productIdentificationVendor=productIdentificationVendor, dellVendorMIBObjects=dellVendorMIBObjects, productIdentificationPerUnitTable=productIdentificationPerUnitTable, productStatusGlobalStatusChange=productStatusGlobalStatusChange, envMonSupplyStatusEntry=envMonSupplyStatusEntry, productIdentificationDescription=productIdentificationDescription, productIdentification=productIdentification, envMonFanSpeed=envMonFanSpeed, dellLan=dellLan, powerConnectVendorMIB=powerConnectVendorMIB, hardware=hardware, envMonSupplyStatusTable=envMonSupplyStatusTable, productIdentificationPerBoxIndex=productIdentificationPerBoxIndex, productIdentificationBootromVersion=productIdentificationBootromVersion, productIdentificationSerialNumber=productIdentificationSerialNumber, productIdentificationPiecePartID=productIdentificationPiecePartID, productIdentificationExpressServiceCode=productIdentificationExpressServiceCode, productIdentificationChassisServiceTag=productIdentificationChassisServiceTag, dellVendorNotifications=dellVendorNotifications, envMonSupplyStatusIndex=envMonSupplyStatusIndex, productIdentificationDisplayName=productIdentificationDisplayName, productStatusLastGlobalStatus=productStatusLastGlobalStatus, envMonSupplyCurrentPower=envMonSupplyCurrentPower)
