#
# PySNMP MIB module HH3C-STORAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-STORAGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:17:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
PhysicalIndex, entPhysicalName, entPhysicalIndex, entPhysicalDescr = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "entPhysicalName", "entPhysicalIndex", "entPhysicalDescr")
hh3cDiskPowerOffReason, = mibBuilder.importSymbols("HH3C-DISK-MIB", "hh3cDiskPowerOffReason")
hh3cEntityExtCriticalLowerTemperatureThreshold, hh3cEntityExtPhysicalIndex, hh3cEntityExtShutdownLowerTemperatureThreshold, hh3cEntityExtOperStatus, hh3cEntityExtTemperature = mibBuilder.importSymbols("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalLowerTemperatureThreshold", "hh3cEntityExtPhysicalIndex", "hh3cEntityExtShutdownLowerTemperatureThreshold", "hh3cEntityExtOperStatus", "hh3cEntityExtTemperature")
hh3cRaidHideState, hh3cRaidRunState, hh3cRaidName, hh3cRaidUuid = mibBuilder.importSymbols("HH3C-RAID-MIB", "hh3cRaidHideState", "hh3cRaidRunState", "hh3cRaidName", "hh3cRaidUuid")
Hh3cStorageLedStateType, Hh3cStorageEnableState, Hh3cWwpnListType, Hh3cStorageCapableState, hh3cStorageRef, Hh3cSoftwareInfoString, Hh3cStorageActionType = mibBuilder.importSymbols("HH3C-STORAGE-REF-MIB", "Hh3cStorageLedStateType", "Hh3cStorageEnableState", "Hh3cWwpnListType", "Hh3cStorageCapableState", "hh3cStorageRef", "Hh3cSoftwareInfoString", "Hh3cStorageActionType")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, NotificationType, MibIdentifier, ModuleIdentity, Integer32, IpAddress, TimeTicks, ObjectIdentity, Unsigned32, Gauge32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "NotificationType", "MibIdentifier", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "ObjectIdentity", "Unsigned32", "Gauge32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cStorageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 10, 1))
if mibBuilder.loadTexts: hh3cStorageMIB.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: hh3cStorageMIB.setOrganization('H3C Technologies Co., Ltd.')
hh3cStorageMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1))
hh3cStorageServerInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1))
hh3cStoragePhysicalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2))
hh3cStorageServerCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1))
hh3cRaidCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 1), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRaidCapability.setStatus('current')
hh3cFcCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 2), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcCapability.setStatus('current')
hh3cNasCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 3), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNasCapability.setStatus('current')
hh3cAdaptiveRepCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 4), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cAdaptiveRepCapability.setStatus('current')
hh3cRemoteRepCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 5), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRemoteRepCapability.setStatus('current')
hh3cSafeCacheCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 6), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSafeCacheCapability.setStatus('current')
hh3cSyncMirrorCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 7), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSyncMirrorCapability.setStatus('current')
hh3cAsyncMirrorCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 8), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cAsyncMirrorCapability.setStatus('current')
hh3cTimeMarkCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 9), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cTimeMarkCapability.setStatus('current')
hh3cSseCapability = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 10), Hh3cStorageCapableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSseCapability.setStatus('current')
hh3cStorageTargetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 2))
hh3ciSCSITargetEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 2, 1), Hh3cStorageEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3ciSCSITargetEnable.setStatus('current')
hh3cFcTargetEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 2, 2), Hh3cStorageEnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcTargetEnable.setStatus('current')
hh3cStorageServerPhysInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3))
hh3cServerLocationLedState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 1), Hh3cStorageLedStateType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cServerLocationLedState.setStatus('current')
hh3cServerResetButtonState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 2), Hh3cStorageEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cServerResetButtonState.setStatus('current')
hh3cServerPowerButtonState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 3), Hh3cStorageEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cServerPowerButtonState.setStatus('current')
hh3cServerPowerState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("online", 1), ("onlinebypass", 2), ("onbattery", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cServerPowerState.setStatus('current')
hh3cDeuTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cDeuTable.setStatus('current')
hh3cDeuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-STORAGE-MIB", "hh3cDeuIndex"))
if mibBuilder.loadTexts: hh3cDeuEntry.setStatus('current')
hh3cDeuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cDeuIndex.setStatus('current')
hh3cDeuIDLed = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1, 2), Hh3cStorageLedStateType().clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDeuIDLed.setStatus('current')
hh3cDeuDiskScan = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1, 3), Hh3cStorageActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDeuDiskScan.setStatus('current')
hh3cStorageInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2), )
if mibBuilder.loadTexts: hh3cStorageInterfaceTable.setStatus('current')
hh3cStorageInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1), ).setIndexNames((0, "HH3C-STORAGE-MIB", "hh3cStorageInterfaceIndex"))
if mibBuilder.loadTexts: hh3cStorageInterfaceEntry.setStatus('current')
hh3cStorageInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cStorageInterfaceIndex.setStatus('current')
hh3cStorageInterfaceGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cStorageInterfaceGateway.setStatus('current')
hh3cStorageInterfaceGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cStorageInterfaceGatewayType.setStatus('current')
hh3cStorageInterfaceMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1500, 9000))).clone(namedValues=NamedValues(("mtu1", 1500), ("mtu2", 9000)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cStorageInterfaceMTU.setStatus('current')
hh3cBondingTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3), )
if mibBuilder.loadTexts: hh3cBondingTable.setStatus('current')
hh3cBondingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3, 1), ).setIndexNames((0, "HH3C-STORAGE-MIB", "hh3cBondingIndex"))
if mibBuilder.loadTexts: hh3cBondingEntry.setStatus('current')
hh3cBondingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cBondingIndex.setStatus('current')
hh3cBondingPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cBondingPortList.setStatus('current')
hh3cScsiAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4), )
if mibBuilder.loadTexts: hh3cScsiAdapterTable.setStatus('current')
hh3cScsiAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "HH3C-STORAGE-MIB", "hh3cAdapterNumber"))
if mibBuilder.loadTexts: hh3cScsiAdapterEntry.setStatus('current')
hh3cAdapterNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cAdapterNumber.setStatus('current')
hh3cAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cAdapterDesc.setStatus('current')
hh3cAdapterType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scsi", 1), ("fc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cAdapterType.setStatus('current')
hh3cFcAdapterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initiator", 1), ("target", 2), ("dual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcAdapterMode.setStatus('current')
hh3cFcAdapterInitiatorWwpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 5), Hh3cWwpnListType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcAdapterInitiatorWwpnName.setStatus('current')
hh3cFcAdapterTargetWwpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 6), Hh3cWwpnListType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcAdapterTargetWwpnName.setStatus('current')
hh3cFcAdapterPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("linkup", 1), ("linkdown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcAdapterPortState.setStatus('current')
hh3cFcAdapterModeSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 8), Hh3cStorageEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcAdapterModeSwitch.setStatus('current')
hh3cExtVoltageTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5), )
if mibBuilder.loadTexts: hh3cExtVoltageTable.setStatus('current')
hh3cExtVoltageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1), ).setIndexNames((0, "HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"))
if mibBuilder.loadTexts: hh3cExtVoltageEntry.setStatus('current')
hh3cExtVoltagePhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cExtVoltagePhysicalIndex.setStatus('current')
hh3cExtVoltagePhysicalName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cExtVoltagePhysicalName.setStatus('current')
hh3cExtVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cExtVoltage.setStatus('current')
hh3cExtVoltageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cExtVoltageLowThreshold.setStatus('current')
hh3cExtVoltageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cExtVoltageHighThreshold.setStatus('current')
hh3cExtCriticalVoltageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cExtCriticalVoltageLowThreshold.setStatus('current')
hh3cExtCriticalVoltageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cExtCriticalVoltageHighThreshold.setStatus('current')
hh3cExtShutdownVoltageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cExtShutdownVoltageLowThreshold.setStatus('current')
hh3cExtShutdownVoltageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cExtShutdownVoltageHighThreshold.setStatus('current')
hh3cStorageTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3))
hh3cStorageTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0))
hh3cStorageTrapsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 1))
hh3cSoftwareInfoString = MibScalar((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 1, 1), Hh3cSoftwareInfoString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSoftwareInfoString.setStatus('current')
hh3cStorCriticalLowerTemperatureThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 1)).setObjects(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"), ("ENTITY-MIB", "entPhysicalName"), ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"), ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalLowerTemperatureThreshold"))
if mibBuilder.loadTexts: hh3cStorCriticalLowerTemperatureThresholdNotification.setStatus('current')
hh3cStorTemperatureTooLow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 2)).setObjects(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"), ("ENTITY-MIB", "entPhysicalName"), ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"), ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtShutdownLowerTemperatureThreshold"))
if mibBuilder.loadTexts: hh3cStorTemperatureTooLow.setStatus('current')
hh3cExtVoltageLowThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 3)).setObjects(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"), ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"), ("HH3C-STORAGE-MIB", "hh3cExtVoltage"), ("HH3C-STORAGE-MIB", "hh3cExtVoltageLowThreshold"))
if mibBuilder.loadTexts: hh3cExtVoltageLowThresholdNotification.setStatus('current')
hh3cExtVoltageHighThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 4)).setObjects(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"), ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"), ("HH3C-STORAGE-MIB", "hh3cExtVoltage"), ("HH3C-STORAGE-MIB", "hh3cExtVoltageHighThreshold"))
if mibBuilder.loadTexts: hh3cExtVoltageHighThresholdNotification.setStatus('current')
hh3cExtCriticalVoltageLowThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 5)).setObjects(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"), ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"), ("HH3C-STORAGE-MIB", "hh3cExtVoltage"), ("HH3C-STORAGE-MIB", "hh3cExtCriticalVoltageLowThreshold"))
if mibBuilder.loadTexts: hh3cExtCriticalVoltageLowThresholdNotification.setStatus('current')
hh3cExtCriticalVoltageHighThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 6)).setObjects(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"), ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"), ("HH3C-STORAGE-MIB", "hh3cExtVoltage"), ("HH3C-STORAGE-MIB", "hh3cExtCriticalVoltageHighThreshold"))
if mibBuilder.loadTexts: hh3cExtCriticalVoltageHighThresholdNotification.setStatus('current')
hh3cExtVoltageTooLow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 7)).setObjects(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"), ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"), ("HH3C-STORAGE-MIB", "hh3cExtVoltage"), ("HH3C-STORAGE-MIB", "hh3cExtShutdownVoltageLowThreshold"))
if mibBuilder.loadTexts: hh3cExtVoltageTooLow.setStatus('current')
hh3cExtVoltageTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 8)).setObjects(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"), ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"), ("HH3C-STORAGE-MIB", "hh3cExtVoltage"), ("HH3C-STORAGE-MIB", "hh3cExtShutdownVoltageHighThreshold"))
if mibBuilder.loadTexts: hh3cExtVoltageTooHigh.setStatus('current')
hh3cExtBatteryStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 9)).setObjects(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"), ("ENTITY-MIB", "entPhysicalName"), ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtOperStatus"))
if mibBuilder.loadTexts: hh3cExtBatteryStateNotification.setStatus('current')
hh3cDiskIOErrorNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 10)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: hh3cDiskIOErrorNotification.setStatus('current')
hh3cRaidCreateNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 11)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidCreateNotification.setStatus('current')
hh3cRaidDeleteNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 12)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidDeleteNotification.setStatus('current')
hh3cRaidHideStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 13)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"), ("HH3C-RAID-MIB", "hh3cRaidHideState"))
if mibBuilder.loadTexts: hh3cRaidHideStateNotification.setStatus('current')
hh3cRaidRunStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 14)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"), ("HH3C-RAID-MIB", "hh3cRaidRunState"))
if mibBuilder.loadTexts: hh3cRaidRunStateNotification.setStatus('current')
hh3cRaidImportNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 15)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidImportNotification.setStatus('current')
hh3cRaidRebuildStartNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 16)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidRebuildStartNotification.setStatus('current')
hh3cRaidRebuildFinishNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 17)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidRebuildFinishNotification.setStatus('current')
hh3cRaidRebuildPauseNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 18)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidRebuildPauseNotification.setStatus('current')
hh3cRaidRebuildInterruptNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 19)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidRebuildInterruptNotification.setStatus('current')
hh3cSoftwareModuleFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 20)).setObjects(("HH3C-STORAGE-MIB", "hh3cSoftwareInfoString"))
if mibBuilder.loadTexts: hh3cSoftwareModuleFailNotification.setStatus('current')
hh3cRaidBatteryExpiredNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 21))
if mibBuilder.loadTexts: hh3cRaidBatteryExpiredNotification.setStatus('current')
hh3cRaidBatteryWillExpireNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 22))
if mibBuilder.loadTexts: hh3cRaidBatteryWillExpireNotification.setStatus('current')
hh3cLvOnlineFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 23)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cLvOnlineFailNotification.setStatus('current')
hh3cLvOfflineFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 24)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cLvOfflineFailNotification.setStatus('current')
hh3cRaidRunNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 25)).setObjects(("HH3C-RAID-MIB", "hh3cRaidUuid"), ("HH3C-RAID-MIB", "hh3cRaidName"))
if mibBuilder.loadTexts: hh3cRaidRunNotification.setStatus('current')
hh3cExtVoltageNormal = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 26)).setObjects(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"), ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"), ("HH3C-STORAGE-MIB", "hh3cExtVoltage"), ("HH3C-STORAGE-MIB", "hh3cExtVoltageLowThreshold"), ("HH3C-STORAGE-MIB", "hh3cExtVoltageHighThreshold"))
if mibBuilder.loadTexts: hh3cExtVoltageNormal.setStatus('current')
hh3cDiskPowerOnNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 27)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: hh3cDiskPowerOnNotification.setStatus('current')
hh3cDiskPowerOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 28)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("HH3C-DISK-MIB", "hh3cDiskPowerOffReason"))
if mibBuilder.loadTexts: hh3cDiskPowerOffNotification.setStatus('current')
mibBuilder.exportSymbols("HH3C-STORAGE-MIB", hh3cStorTemperatureTooLow=hh3cStorTemperatureTooLow, hh3cRaidRebuildInterruptNotification=hh3cRaidRebuildInterruptNotification, hh3cBondingTable=hh3cBondingTable, hh3cAdaptiveRepCapability=hh3cAdaptiveRepCapability, hh3cExtVoltageLowThresholdNotification=hh3cExtVoltageLowThresholdNotification, hh3cStorageInterfaceIndex=hh3cStorageInterfaceIndex, hh3cExtVoltageTooLow=hh3cExtVoltageTooLow, hh3cStorageServerPhysInfo=hh3cStorageServerPhysInfo, hh3cScsiAdapterTable=hh3cScsiAdapterTable, hh3cExtVoltageTooHigh=hh3cExtVoltageTooHigh, hh3cLvOnlineFailNotification=hh3cLvOnlineFailNotification, hh3cNasCapability=hh3cNasCapability, hh3cFcCapability=hh3cFcCapability, hh3cExtVoltageNormal=hh3cExtVoltageNormal, hh3cRaidImportNotification=hh3cRaidImportNotification, hh3cExtVoltageHighThreshold=hh3cExtVoltageHighThreshold, hh3cExtVoltageEntry=hh3cExtVoltageEntry, hh3cFcTargetEnable=hh3cFcTargetEnable, hh3cExtVoltageTable=hh3cExtVoltageTable, hh3cStorageInterfaceGatewayType=hh3cStorageInterfaceGatewayType, hh3cRaidCreateNotification=hh3cRaidCreateNotification, hh3cExtVoltagePhysicalName=hh3cExtVoltagePhysicalName, hh3cStorageInterfaceTable=hh3cStorageInterfaceTable, hh3cRaidRebuildPauseNotification=hh3cRaidRebuildPauseNotification, hh3cSoftwareInfoString=hh3cSoftwareInfoString, hh3cStorageTargetConfig=hh3cStorageTargetConfig, hh3cDiskIOErrorNotification=hh3cDiskIOErrorNotification, hh3cSafeCacheCapability=hh3cSafeCacheCapability, hh3cStorageMibObjects=hh3cStorageMibObjects, hh3cExtBatteryStateNotification=hh3cExtBatteryStateNotification, hh3cFcAdapterInitiatorWwpnName=hh3cFcAdapterInitiatorWwpnName, hh3cStorageServerInfo=hh3cStorageServerInfo, hh3cSyncMirrorCapability=hh3cSyncMirrorCapability, hh3cFcAdapterTargetWwpnName=hh3cFcAdapterTargetWwpnName, hh3cAdapterType=hh3cAdapterType, hh3cExtShutdownVoltageLowThreshold=hh3cExtShutdownVoltageLowThreshold, hh3cExtCriticalVoltageLowThreshold=hh3cExtCriticalVoltageLowThreshold, hh3cExtVoltageHighThresholdNotification=hh3cExtVoltageHighThresholdNotification, hh3cStorageTrapsPrefix=hh3cStorageTrapsPrefix, hh3cDeuTable=hh3cDeuTable, hh3cServerPowerState=hh3cServerPowerState, hh3cDeuDiskScan=hh3cDeuDiskScan, hh3cDiskPowerOnNotification=hh3cDiskPowerOnNotification, hh3cServerPowerButtonState=hh3cServerPowerButtonState, hh3cLvOfflineFailNotification=hh3cLvOfflineFailNotification, hh3cRaidRebuildFinishNotification=hh3cRaidRebuildFinishNotification, hh3cStorCriticalLowerTemperatureThresholdNotification=hh3cStorCriticalLowerTemperatureThresholdNotification, hh3cStoragePhysicalInfo=hh3cStoragePhysicalInfo, hh3cFcAdapterPortState=hh3cFcAdapterPortState, hh3cServerLocationLedState=hh3cServerLocationLedState, hh3ciSCSITargetEnable=hh3ciSCSITargetEnable, hh3cStorageTraps=hh3cStorageTraps, hh3cExtVoltagePhysicalIndex=hh3cExtVoltagePhysicalIndex, hh3cBondingIndex=hh3cBondingIndex, hh3cRaidDeleteNotification=hh3cRaidDeleteNotification, hh3cServerResetButtonState=hh3cServerResetButtonState, hh3cExtShutdownVoltageHighThreshold=hh3cExtShutdownVoltageHighThreshold, hh3cExtVoltageLowThreshold=hh3cExtVoltageLowThreshold, hh3cDeuEntry=hh3cDeuEntry, hh3cStorageInterfaceEntry=hh3cStorageInterfaceEntry, hh3cAdapterDesc=hh3cAdapterDesc, hh3cDeuIDLed=hh3cDeuIDLed, hh3cTimeMarkCapability=hh3cTimeMarkCapability, hh3cStorageTrapsObjects=hh3cStorageTrapsObjects, hh3cSseCapability=hh3cSseCapability, hh3cRaidRunStateNotification=hh3cRaidRunStateNotification, hh3cDeuIndex=hh3cDeuIndex, hh3cExtVoltage=hh3cExtVoltage, hh3cDiskPowerOffNotification=hh3cDiskPowerOffNotification, hh3cRaidBatteryExpiredNotification=hh3cRaidBatteryExpiredNotification, hh3cExtCriticalVoltageLowThresholdNotification=hh3cExtCriticalVoltageLowThresholdNotification, hh3cStorageServerCapability=hh3cStorageServerCapability, hh3cScsiAdapterEntry=hh3cScsiAdapterEntry, hh3cExtCriticalVoltageHighThresholdNotification=hh3cExtCriticalVoltageHighThresholdNotification, hh3cBondingPortList=hh3cBondingPortList, hh3cRaidRunNotification=hh3cRaidRunNotification, hh3cRemoteRepCapability=hh3cRemoteRepCapability, hh3cSoftwareModuleFailNotification=hh3cSoftwareModuleFailNotification, hh3cStorageMIB=hh3cStorageMIB, PYSNMP_MODULE_ID=hh3cStorageMIB, hh3cExtCriticalVoltageHighThreshold=hh3cExtCriticalVoltageHighThreshold, hh3cRaidBatteryWillExpireNotification=hh3cRaidBatteryWillExpireNotification, hh3cAsyncMirrorCapability=hh3cAsyncMirrorCapability, hh3cRaidCapability=hh3cRaidCapability, hh3cStorageInterfaceMTU=hh3cStorageInterfaceMTU, hh3cRaidHideStateNotification=hh3cRaidHideStateNotification, hh3cRaidRebuildStartNotification=hh3cRaidRebuildStartNotification, hh3cBondingEntry=hh3cBondingEntry, hh3cFcAdapterModeSwitch=hh3cFcAdapterModeSwitch, hh3cAdapterNumber=hh3cAdapterNumber, hh3cStorageInterfaceGateway=hh3cStorageInterfaceGateway, hh3cFcAdapterMode=hh3cFcAdapterMode)
