#
# PySNMP MIB module H150E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H150E-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Unsigned32, enterprises, Counter64, NotificationType, Bits, ObjectIdentity, Gauge32, Integer32, MibIdentifier, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Unsigned32", "enterprises", "Counter64", "NotificationType", "Bits", "ObjectIdentity", "Gauge32", "Integer32", "MibIdentifier", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
siemensUnits = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7))
pn = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2))
h150eOffice = ModuleIdentity((1, 3, 6, 1, 4, 1, 231, 7, 2, 9))
if mibBuilder.loadTexts: h150eOffice.setLastUpdated('0606080000Z')
if mibBuilder.loadTexts: h150eOffice.setOrganization('Siemens Communications')
h150eControlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1))
h150eErrorHistoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2))
h150eSystemInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3))
h150eStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4))
h150eCdrConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5))
h150eTrapSpecifications = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6))
umProxyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8))
class DisplayString(OctetString):
    pass

class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class ReadWrite(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("readWrite", 1), ("readOnly", 2))

h150eSysState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eSysState.setStatus('current')
tftpSwitchoverDateTime = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 2), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpSwitchoverDateTime.setStatus('current')
tftpDownloadAction = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notDownloading", 1), ("downloadAndImmediateSwitchover", 2), ("downloadAndDelayedSwitchover", 3), ("downloadWithoutSwitchover", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpDownloadAction.setStatus('current')
h150eResetControl = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("warmBoot", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eResetControl.setStatus('current')
h150eSwitchoverState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("readyForSwitchover", 1), ("notReadyForSwitchover", 2), ("initSwitchoverNow", 3), ("initSwitchoverDelayed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eSwitchoverState.setStatus('current')
h150eShadowFlashState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("flashDeleted", 1), ("flashNotDeleted", 2), ("flashWriteProtected", 3), ("flashTooSmall", 4), ("deleteFlashNow", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eShadowFlashState.setStatus('current')
h150eLoadLevel = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eLoadLevel.setStatus('current')
h150eTrapRepetitions = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eTrapRepetitions.setStatus('current')
h150eCdrBufferState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("accounting", 1), ("deleteBufferNow", 2), ("notAccounting", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrBufferState.setStatus('current')
h150eLogBufferState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("logging", 1), ("deleteBufferNow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eLogBufferState.setStatus('current')
numberOfErrorHistoryEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberOfErrorHistoryEntries.setStatus('current')
h150eErrorHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2), )
if mibBuilder.loadTexts: h150eErrorHistoryTable.setStatus('current')
h150eErrorHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1), ).setIndexNames((0, "H150E-MIB", "h150eErrorIndex"))
if mibBuilder.loadTexts: h150eErrorHistoryEntry.setStatus('current')
h150eErrorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eErrorIndex.setStatus('current')
h150eErrorDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eErrorDateTime.setStatus('current')
h150eErrorClass = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eErrorClass.setStatus('current')
h150eErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eErrorCode.setStatus('current')
h150eAccessSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eAccessSlot.setStatus('current')
h150eAccessPort = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eAccessPort.setStatus('current')
h150eErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eErrorDescription.setStatus('current')
h150eErrorSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eErrorSeverity.setStatus('current')
sysHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHardwareVersion.setStatus('current')
sysSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareVersion.setStatus('current')
sysCodeNumber = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysCodeNumber.setStatus('current')
sysSoftwareLocation = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lower", 1), ("upper", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareLocation.setStatus('current')
numberOfSlotTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfSlotTableEntries.setStatus('current')
h150eSlotTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6), )
if mibBuilder.loadTexts: h150eSlotTable.setStatus('current')
h150eSlotTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1), ).setIndexNames((0, "H150E-MIB", "cardIndex"))
if mibBuilder.loadTexts: h150eSlotTableEntry.setStatus('current')
cardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardIndex.setStatus('current')
cardBoxNum = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBoxNum.setStatus('current')
cardSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSlotNum.setStatus('current')
cardType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardType.setStatus('current')
cardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardDescription.setStatus('current')
cardCodeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCodeNumber.setStatus('current')
cardState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardState.setStatus('current')
numberOfPortTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfPortTableEntries.setStatus('current')
h150ePortTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8), )
if mibBuilder.loadTexts: h150ePortTable.setStatus('current')
h150ePortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1), ).setIndexNames((0, "H150E-MIB", "portIndex"))
if mibBuilder.loadTexts: h150ePortTableEntry.setStatus('current')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('current')
portCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCardIndex.setStatus('current')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portType.setStatus('current')
portState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portState.setStatus('current')
portLock = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unlocked", 1), ("lockedBySoftware", 2), ("lockedByHardware", 3), ("lockedBySoftAndHardware", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLock.setStatus('current')
portLogicalPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portLogicalPortNumber.setStatus('current')
numberOfExtensionTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfExtensionTableEntries.setStatus('current')
h150eExtensionTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10), )
if mibBuilder.loadTexts: h150eExtensionTable.setStatus('current')
h150eExtensionTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1), ).setIndexNames((0, "H150E-MIB", "extensionIndex"))
if mibBuilder.loadTexts: h150eExtensionTableEntry.setStatus('current')
extensionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensionIndex.setStatus('current')
extensionDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensionDescription.setStatus('current')
extensionCodeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensionCodeNumber.setStatus('current')
numberOfLanConnTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfLanConnTableEntries.setStatus('current')
h150eLanConnTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12), )
if mibBuilder.loadTexts: h150eLanConnTable.setStatus('current')
h150eLanConnTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1), ).setIndexNames((0, "H150E-MIB", "lanConnIndex"))
if mibBuilder.loadTexts: h150eLanConnTableEntry.setStatus('current')
lanConnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnIndex.setStatus('current')
lanConnDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnDescription.setStatus('current')
lanConnIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnIpAddress.setStatus('current')
lanConnSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnSubnetMask.setStatus('current')
lanConnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnStatus.setStatus('current')
hiPathAllServeServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hiPathAllServeServerIpAddress.setStatus('current')
indexOfLastPortStatusNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: indexOfLastPortStatusNotificationTrap.setStatus('current')
sysSnmpAgentVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSnmpAgentVersion.setStatus('current')
sysShadowSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysShadowSoftwareVersion.setStatus('current')
sysHiPathSymbolSubInfo = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHiPathSymbolSubInfo.setStatus('current')
sysHiPathBranding = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHiPathBranding.setStatus('current')
sysTimezoneOffset = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1440, 1440))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTimezoneOffset.setStatus('current')
numberOfFeatureStatTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfFeatureStatTableEntries.setStatus('current')
h150eFeatureStatTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2), )
if mibBuilder.loadTexts: h150eFeatureStatTable.setStatus('current')
h150eFeatureStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1), ).setIndexNames((0, "H150E-MIB", "featureIndex"))
if mibBuilder.loadTexts: h150eFeatureStatEntry.setStatus('current')
featureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureIndex.setStatus('current')
featureDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureDescription.setStatus('current')
featureCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureCounter.setStatus('current')
featureStatTableReset = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("counting", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: featureStatTableReset.setStatus('current')
h150eCdrSeparator = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dosMode", 1), ("unixMode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrSeparator.setStatus('current')
h150eCdrElementSeparator = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(124, 59, 32))).clone(namedValues=NamedValues(("pipe", 124), ("semicolon", 59), ("blank", 32)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrElementSeparator.setStatus('current')
h150eCdrThresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrThresholdValue.setStatus('current')
h150eCdrTftpFileCounter = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrTftpFileCounter.setStatus('current')
h150eCdrTftpServerDestAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrTftpServerDestAddress.setStatus('current')
h150eCdrTftpServerAlternateDestAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrTftpServerAlternateDestAddress.setStatus('current')
h150eCdrTftpClientTimer = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrTftpClientTimer.setStatus('current')
h150eCdrTcpServerDestAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrTcpServerDestAddress.setStatus('current')
h150eCdrTcpServerDestPort = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrTcpServerDestPort.setStatus('current')
h150eCdrOutputMode = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("v24port", 1), ("uPNport", 2), ("pCVPLport", 3), ("tftpClient", 4), ("tftpServer", 5), ("tcpClient", 6), ("noOutput", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eCdrOutputMode.setStatus('current')
h150eIndexOfLastCdrNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h150eIndexOfLastCdrNotificationTrap.setStatus('current')
h150etypeOfLastCdrNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150etypeOfLastCdrNotificationTrap.setStatus('current')
h150eDescriptionOfLastCdrNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h150eDescriptionOfLastCdrNotificationTrap.setStatus('current')
sendAlarm = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 1)).setObjects(("H150E-MIB", "h150eErrorIndex"), ("H150E-MIB", "h150eErrorDateTime"), ("H150E-MIB", "h150eErrorClass"), ("H150E-MIB", "h150eErrorCode"), ("H150E-MIB", "h150eAccessSlot"), ("H150E-MIB", "h150eAccessPort"), ("H150E-MIB", "h150eErrorDescription"), ("H150E-MIB", "h150eSysState"), ("H150E-MIB", "h150eErrorSeverity"))
if mibBuilder.loadTexts: sendAlarm.setStatus('current')
sendCdrNotification = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 2)).setObjects(("H150E-MIB", "h150eIndexOfLastCdrNotificationTrap"), ("H150E-MIB", "h150etypeOfLastCdrNotificationTrap"), ("H150E-MIB", "h150eDescriptionOfLastCdrNotificationTrap"))
if mibBuilder.loadTexts: sendCdrNotification.setStatus('current')
sendPortStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 3)).setObjects(("H150E-MIB", "indexOfLastPortStatusNotificationTrap"))
if mibBuilder.loadTexts: sendPortStatusNotification.setStatus('current')
sendUmRelatedChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 4)).setObjects(("H150E-MIB", "umTrapIdentifier"), ("H150E-MIB", "umTrapType"), ("H150E-MIB", "umTrapLogicalPortNumber"), ("H150E-MIB", "umNetworkElementKey"))
if mibBuilder.loadTexts: sendUmRelatedChangeNotification.setStatus('current')
umNodeNumber = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: umNodeNumber.setStatus('current')
umSrsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umSrsEnabled.setStatus('current')
umDefaultLanguage = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("german", 1), ("english", 2), ("french", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umDefaultLanguage.setStatus('current')
umNumberOfSubscriberEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umNumberOfSubscriberEntries.setStatus('current')
umSubscriberTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5), )
if mibBuilder.loadTexts: umSubscriberTable.setStatus('current')
umSubscriberTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1), ).setIndexNames((0, "H150E-MIB", "umLogicalPortNumber"))
if mibBuilder.loadTexts: umSubscriberTableEntry.setStatus('current')
umLogicalPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umLogicalPortNumber.setStatus('current')
umInternalCallNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: umInternalCallNumber.setStatus('current')
umDIDNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: umDIDNumber.setStatus('current')
umE164Number = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: umE164Number.setStatus('current')
umDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: umDisplayName.setStatus('current')
umStationType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("s0", 0), ("up0", 1), ("hfa", 2), ("analog", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umStationType.setStatus('current')
umPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umPortStatus.setStatus('current')
umClassOfService = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umClassOfService.setStatus('current')
umDisplayLanguage = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("german", 1), ("english", 2), ("french", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umDisplayLanguage.setStatus('current')
umCfssTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 5, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: umCfssTarget.setStatus('current')
umNumberOfUnconfirmedTraps = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umNumberOfUnconfirmedTraps.setStatus('current')
umUnconfirmedTrapTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7), )
if mibBuilder.loadTexts: umUnconfirmedTrapTable.setStatus('current')
umUnconfirmedTrapTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1), ).setIndexNames((0, "H150E-MIB", "umTrapIdentifier"))
if mibBuilder.loadTexts: umUnconfirmedTrapTableEntry.setStatus('current')
umTrapIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umTrapIdentifier.setStatus('current')
umTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("startup", 0), ("modifyGeneral", 1), ("modifySubscriber", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umTrapType.setStatus('current')
umTrapLogicalPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: umTrapLogicalPortNumber.setStatus('current')
umNetworkElementKey = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 8, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: umNetworkElementKey.setStatus('current')
mibBuilder.exportSymbols("H150E-MIB", umUnconfirmedTrapTable=umUnconfirmedTrapTable, h150etypeOfLastCdrNotificationTrap=h150etypeOfLastCdrNotificationTrap, sysCodeNumber=sysCodeNumber, cardState=cardState, umInternalCallNumber=umInternalCallNumber, sysHardwareVersion=sysHardwareVersion, DisplayString=DisplayString, umStationType=umStationType, featureCounter=featureCounter, ReadWrite=ReadWrite, sendCdrNotification=sendCdrNotification, h150eSysState=h150eSysState, extensionDescription=extensionDescription, umClassOfService=umClassOfService, umTrapLogicalPortNumber=umTrapLogicalPortNumber, umTrapIdentifier=umTrapIdentifier, sysSoftwareVersion=sysSoftwareVersion, h150eCdrElementSeparator=h150eCdrElementSeparator, cardDescription=cardDescription, extensionIndex=extensionIndex, h150eLanConnTable=h150eLanConnTable, numberOfFeatureStatTableEntries=numberOfFeatureStatTableEntries, cardSlotNum=cardSlotNum, h150eErrorHistoryTable=h150eErrorHistoryTable, DateAndTime=DateAndTime, h150eTrapRepetitions=h150eTrapRepetitions, pn=pn, umLogicalPortNumber=umLogicalPortNumber, umDisplayName=umDisplayName, umNetworkElementKey=umNetworkElementKey, numberOfLanConnTableEntries=numberOfLanConnTableEntries, h150eSlotTableEntry=h150eSlotTableEntry, h150eCdrTcpServerDestPort=h150eCdrTcpServerDestPort, umSubscriberTable=umSubscriberTable, sendUmRelatedChangeNotification=sendUmRelatedChangeNotification, h150eControlGroup=h150eControlGroup, lanConnSubnetMask=lanConnSubnetMask, h150eOffice=h150eOffice, hiPathAllServeServerIpAddress=hiPathAllServeServerIpAddress, h150eSlotTable=h150eSlotTable, umProxyGroup=umProxyGroup, h150eErrorIndex=h150eErrorIndex, h150eErrorHistoryEntry=h150eErrorHistoryEntry, sendAlarm=sendAlarm, h150eAccessPort=h150eAccessPort, h150ePortTableEntry=h150ePortTableEntry, portType=portType, sysHiPathBranding=sysHiPathBranding, sysTimezoneOffset=sysTimezoneOffset, umNumberOfSubscriberEntries=umNumberOfSubscriberEntries, tftpSwitchoverDateTime=tftpSwitchoverDateTime, indexOfLastPortStatusNotificationTrap=indexOfLastPortStatusNotificationTrap, siemensUnits=siemensUnits, umNumberOfUnconfirmedTraps=umNumberOfUnconfirmedTraps, h150eIndexOfLastCdrNotificationTrap=h150eIndexOfLastCdrNotificationTrap, cardIndex=cardIndex, umTrapType=umTrapType, sysSoftwareLocation=sysSoftwareLocation, h150eExtensionTable=h150eExtensionTable, h150eCdrThresholdValue=h150eCdrThresholdValue, extensionCodeNumber=extensionCodeNumber, umPortStatus=umPortStatus, h150eErrorHistoryGroup=h150eErrorHistoryGroup, h150eErrorDescription=h150eErrorDescription, umUnconfirmedTrapTableEntry=umUnconfirmedTrapTableEntry, numberOfPortTableEntries=numberOfPortTableEntries, lanConnStatus=lanConnStatus, featureStatTableReset=featureStatTableReset, h150eCdrSeparator=h150eCdrSeparator, h150eCdrTftpFileCounter=h150eCdrTftpFileCounter, h150eCdrTcpServerDestAddress=h150eCdrTcpServerDestAddress, cardType=cardType, h150eTrapSpecifications=h150eTrapSpecifications, h150eCdrTftpServerDestAddress=h150eCdrTftpServerDestAddress, umCfssTarget=umCfssTarget, h150eCdrConfigGroup=h150eCdrConfigGroup, cardCodeNumber=cardCodeNumber, numberOfErrorHistoryEntries=numberOfErrorHistoryEntries, portLogicalPortNumber=portLogicalPortNumber, portLock=portLock, h150eDescriptionOfLastCdrNotificationTrap=h150eDescriptionOfLastCdrNotificationTrap, sysHiPathSymbolSubInfo=sysHiPathSymbolSubInfo, h150eSwitchoverState=h150eSwitchoverState, featureIndex=featureIndex, h150eLogBufferState=h150eLogBufferState, cardBoxNum=cardBoxNum, numberOfExtensionTableEntries=numberOfExtensionTableEntries, PYSNMP_MODULE_ID=h150eOffice, numberOfSlotTableEntries=numberOfSlotTableEntries, umDIDNumber=umDIDNumber, h150eErrorDateTime=h150eErrorDateTime, sysSnmpAgentVersion=sysSnmpAgentVersion, h150eAccessSlot=h150eAccessSlot, h150eErrorCode=h150eErrorCode, h150eFeatureStatEntry=h150eFeatureStatEntry, umDisplayLanguage=umDisplayLanguage, h150eCdrTftpClientTimer=h150eCdrTftpClientTimer, h150eCdrBufferState=h150eCdrBufferState, featureDescription=featureDescription, umSrsEnabled=umSrsEnabled, h150eFeatureStatTable=h150eFeatureStatTable, h150eCdrOutputMode=h150eCdrOutputMode, h150eResetControl=h150eResetControl, h150eErrorSeverity=h150eErrorSeverity, portIndex=portIndex, lanConnIpAddress=lanConnIpAddress, h150eLanConnTableEntry=h150eLanConnTableEntry, umNodeNumber=umNodeNumber, h150eSystemInfoGroup=h150eSystemInfoGroup, h150eShadowFlashState=h150eShadowFlashState, sni=sni, h150eErrorClass=h150eErrorClass, h150eExtensionTableEntry=h150eExtensionTableEntry, umE164Number=umE164Number, umSubscriberTableEntry=umSubscriberTableEntry, h150eLoadLevel=h150eLoadLevel, lanConnDescription=lanConnDescription, umDefaultLanguage=umDefaultLanguage, tftpDownloadAction=tftpDownloadAction, h150ePortTable=h150ePortTable, lanConnIndex=lanConnIndex, portCardIndex=portCardIndex, sysShadowSoftwareVersion=sysShadowSoftwareVersion, h150eCdrTftpServerAlternateDestAddress=h150eCdrTftpServerAlternateDestAddress, sendPortStatusNotification=sendPortStatusNotification, h150eStatisticsGroup=h150eStatisticsGroup, portState=portState)