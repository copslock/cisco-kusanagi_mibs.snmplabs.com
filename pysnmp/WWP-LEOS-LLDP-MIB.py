#
# PySNMP MIB module WWP-LEOS-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-LLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, TimeTicks, MibIdentifier, ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, IpAddress, Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TimeStamp, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention", "TruthValue")
wwpModules, wwpModulesLeos = mibBuilder.importSymbols("WWP-SMI", "wwpModules", "wwpModulesLeos")
wwpLeosLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26))
wwpLeosLldpMIB.setRevisions(('2004-04-18 00:00', '2003-04-23 00:00',))
if mibBuilder.loadTexts: wwpLeosLldpMIB.setLastUpdated('200404180000Z')
if mibBuilder.loadTexts: wwpLeosLldpMIB.setOrganization('IEEE 802.1AB Workgroup')
wwpLeosLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1))
wwpLeosLldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1))
wwpLeosLldpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2))
wwpLeosLldpLocalSystemData = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3))
wwpLeosLldpRemoteSystemsData = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4))
wwpLeosLldpExtentions = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 5))
wwpLeosLldpGlobalAtts = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 6))
wwpLeosLldpNotifMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 3))
wwpLeosLldpNotifMIBNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 3, 0))
class TimeFilter(TextualConvention, TimeTicks):
    status = 'deprecated'

class SnmpAdminString(TextualConvention, OctetString):
    status = 'deprecated'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class WwpLeosLldpChassisIdType(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("entPhysicalAlias", 1), ("ifAlias", 2), ("portEntPhysicalAlias", 3), ("backplaneEntPhysicalAlias", 4), ("macAddress", 5), ("networkAddress", 6), ("local", 7))

class WwpLeosLldpChassisId(TextualConvention, OctetString):
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class WwpLeosLldpPortIdType(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ifAlias", 1), ("portEntPhysicalAlias", 2), ("backplaneEntPhysicalAlias", 3), ("macAddress", 4), ("networkAddress", 5), ("local", 6))

class WwpLeosLldpPortId(TextualConvention, OctetString):
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class WwpLeosLldpManAddrIfSubtype(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3))

class WwpLeosLldpManAddress(TextualConvention, OctetString):
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class WwpLeosLldpSystemCapabilitiesMap(TextualConvention, Bits):
    status = 'deprecated'
    namedValues = NamedValues(("repeater", 0), ("bridge", 1), ("accessPoint", 2), ("router", 3), ("telephone", 4), ("wirelessStation", 5), ("stationOnly", 6))

class WwpLeosLldpPortNumber(TextualConvention, Integer32):
    status = 'deprecated'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1024)

class WwpLeosLldpPortList(TextualConvention, OctetString):
    reference = 'description is taken from RFC 2674, Section 5'
    status = 'deprecated'

wwpLeosLldpMessageTxInterval = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 32768)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpMessageTxInterval.setStatus('deprecated')
wwpLeosLldpMessageTxHoldMultiplier = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpMessageTxHoldMultiplier.setStatus('deprecated')
wwpLeosLldpReinitDelay = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpReinitDelay.setStatus('deprecated')
wwpLeosLldpTxDelay = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)).clone(8)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpTxDelay.setStatus('deprecated')
wwpLeosLldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5), )
if mibBuilder.loadTexts: wwpLeosLldpPortConfigTable.setStatus('deprecated')
wwpLeosLldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigPortNum"))
if mibBuilder.loadTexts: wwpLeosLldpPortConfigEntry.setStatus('deprecated')
wwpLeosLldpPortConfigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 1), WwpLeosLldpPortNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: wwpLeosLldpPortConfigPortNum.setStatus('deprecated')
wwpLeosLldpPortConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4))).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpPortConfigAdminStatus.setStatus('deprecated')
wwpLeosLldpPortConfigTLVsTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 3), Bits().clone(namedValues=NamedValues(("portDesc", 4), ("sysName", 5), ("sysDesc", 6), ("sysCap", 7))).clone(namedValues=NamedValues(("portDesc", 4), ("sysName", 5), ("sysDesc", 6), ("sysCap", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpPortConfigTLVsTxEnable.setStatus('deprecated')
wwpLeosLldpPortConfigStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpPortConfigStatsClear.setStatus('current')
wwpLeosLldpPortConfigOperPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpPortConfigOperPortSpeed.setStatus('current')
wwpLeosLldpPortConfigReqPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpPortConfigReqPortSpeed.setStatus('current')
wwpLeosLldpConfigManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 6), )
if mibBuilder.loadTexts: wwpLeosLldpConfigManAddrTable.setStatus('deprecated')
wwpLeosLldpManAddrPortsTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 6, 1, 1), WwpLeosLldpPortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpManAddrPortsTxEnable.setStatus('deprecated')
wwpLeosLldpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1), )
if mibBuilder.loadTexts: wwpLeosLldpStatsTable.setStatus('deprecated')
wwpLeosLldpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsPortNum"))
if mibBuilder.loadTexts: wwpLeosLldpStatsEntry.setStatus('deprecated')
wwpLeosLldpStatsPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 1), WwpLeosLldpPortNumber())
if mibBuilder.loadTexts: wwpLeosLldpStatsPortNum.setStatus('deprecated')
wwpLeosLldpStatsFramesDiscardedTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpStatsFramesDiscardedTotal.setStatus('deprecated')
wwpLeosLldpStatsFramesInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpStatsFramesInErrors.setStatus('deprecated')
wwpLeosLldpStatsFramesInTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpStatsFramesInTotal.setStatus('deprecated')
wwpLeosLldpStatsFramesOutTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpStatsFramesOutTotal.setStatus('deprecated')
wwpLeosLldpStatsTLVsInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpStatsTLVsInErrors.setStatus('deprecated')
wwpLeosLldpStatsTLVsDiscardedTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpStatsTLVsDiscardedTotal.setStatus('deprecated')
wwpLeosLldpStatsTLVsUnrecognizedTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpStatsTLVsUnrecognizedTotal.setStatus('deprecated')
wwpLeosLldpCounterDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 2, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpCounterDiscontinuityTime.setStatus('deprecated')
wwpLeosLldpLocChassisType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 1), WwpLeosLldpChassisIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocChassisType.setStatus('deprecated')
wwpLeosLldpLocChassisId = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 2), WwpLeosLldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocChassisId.setStatus('deprecated')
wwpLeosLldpLocSysName = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocSysName.setStatus('deprecated')
wwpLeosLldpLocSysDesc = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocSysDesc.setStatus('deprecated')
wwpLeosLldpLocSysCapSupported = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 5), WwpLeosLldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocSysCapSupported.setStatus('deprecated')
wwpLeosLldpLocSysCapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 6), WwpLeosLldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocSysCapEnabled.setStatus('deprecated')
wwpLeosLldpLocPortTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7), )
if mibBuilder.loadTexts: wwpLeosLldpLocPortTable.setStatus('deprecated')
wwpLeosLldpLocPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortNum"))
if mibBuilder.loadTexts: wwpLeosLldpLocPortEntry.setStatus('deprecated')
wwpLeosLldpLocPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 1), WwpLeosLldpPortNumber())
if mibBuilder.loadTexts: wwpLeosLldpLocPortNum.setStatus('deprecated')
wwpLeosLldpLocPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 2), WwpLeosLldpPortIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocPortType.setStatus('deprecated')
wwpLeosLldpLocPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 3), WwpLeosLldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocPortId.setStatus('deprecated')
wwpLeosLldpLocPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 7, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocPortDesc.setStatus('deprecated')
wwpLeosLldpLocManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8), )
if mibBuilder.loadTexts: wwpLeosLldpLocManAddrTable.setStatus('deprecated')
wwpLeosLldpLocManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrType"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddr"))
if mibBuilder.loadTexts: wwpLeosLldpLocManAddrEntry.setStatus('deprecated')
wwpLeosLldpConfigManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 1, 6, 1), )
wwpLeosLldpLocManAddrEntry.registerAugmentions(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpConfigManAddrEntry"))
wwpLeosLldpConfigManAddrEntry.setIndexNames(*wwpLeosLldpLocManAddrEntry.getIndexNames())
if mibBuilder.loadTexts: wwpLeosLldpConfigManAddrEntry.setStatus('deprecated')
wwpLeosLldpLocManAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: wwpLeosLldpLocManAddrType.setStatus('deprecated')
wwpLeosLldpLocManAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 2), WwpLeosLldpManAddress())
if mibBuilder.loadTexts: wwpLeosLldpLocManAddr.setStatus('deprecated')
wwpLeosLldpLocManAddrLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 3), Integer32())
if mibBuilder.loadTexts: wwpLeosLldpLocManAddrLen.setStatus('deprecated')
wwpLeosLldpLocManAddrIfSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 4), WwpLeosLldpManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocManAddrIfSubtype.setStatus('deprecated')
wwpLeosLldpLocManAddrIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocManAddrIfId.setStatus('deprecated')
wwpLeosLldpLocManAddrOID = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 3, 8, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpLocManAddrOID.setStatus('deprecated')
wwpLeosLldpRemTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1), )
if mibBuilder.loadTexts: wwpLeosLldpRemTable.setStatus('deprecated')
wwpLeosLldpRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"))
if mibBuilder.loadTexts: wwpLeosLldpRemEntry.setStatus('deprecated')
wwpLeosLldpRemTimeMark = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: wwpLeosLldpRemTimeMark.setStatus('deprecated')
wwpLeosLldpRemLocalPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 2), WwpLeosLldpPortNumber())
if mibBuilder.loadTexts: wwpLeosLldpRemLocalPortNum.setStatus('deprecated')
wwpLeosLldpRemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: wwpLeosLldpRemIndex.setStatus('deprecated')
wwpLeosLldpRemRemoteChassisType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 4), WwpLeosLldpChassisIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemRemoteChassisType.setStatus('deprecated')
wwpLeosLldpRemRemoteChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 5), WwpLeosLldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemRemoteChassis.setStatus('deprecated')
wwpLeosLldpRemRemotePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 6), WwpLeosLldpPortIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemRemotePortType.setStatus('deprecated')
wwpLeosLldpRemRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 7), WwpLeosLldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemRemotePort.setStatus('deprecated')
wwpLeosLldpRemPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemPortDesc.setStatus('deprecated')
wwpLeosLldpRemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemSysName.setStatus('deprecated')
wwpLeosLldpRemSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemSysDesc.setStatus('deprecated')
wwpLeosLldpRemSysCapSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 11), WwpLeosLldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemSysCapSupported.setStatus('deprecated')
wwpLeosLldpRemSysCapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 1, 1, 12), WwpLeosLldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemSysCapEnabled.setStatus('deprecated')
wwpLeosLldpRemManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2), )
if mibBuilder.loadTexts: wwpLeosLldpRemManAddrTable.setStatus('deprecated')
wwpLeosLldpRemManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrType"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddr"))
if mibBuilder.loadTexts: wwpLeosLldpRemManAddrEntry.setStatus('deprecated')
wwpLeosLldpRemManAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: wwpLeosLldpRemManAddrType.setStatus('deprecated')
wwpLeosLldpRemManAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 2), WwpLeosLldpManAddress())
if mibBuilder.loadTexts: wwpLeosLldpRemManAddr.setStatus('deprecated')
wwpLeosLldpRemManAddrIfSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 3), WwpLeosLldpManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemManAddrIfSubtype.setStatus('deprecated')
wwpLeosLldpRemManAddrIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemManAddrIfId.setStatus('deprecated')
wwpLeosLldpRemManAddrOID = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 2, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemManAddrOID.setStatus('deprecated')
wwpLeosLldpRemUnknownTLVTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3), )
if mibBuilder.loadTexts: wwpLeosLldpRemUnknownTLVTable.setStatus('deprecated')
wwpLeosLldpRemUnknownTLVEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"))
if mibBuilder.loadTexts: wwpLeosLldpRemUnknownTLVEntry.setStatus('deprecated')
wwpLeosLldpRemUnknownTLVType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(9, 126)))
if mibBuilder.loadTexts: wwpLeosLldpRemUnknownTLVType.setStatus('deprecated')
wwpLeosLldpRemUnknownTLVInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemUnknownTLVInfo.setStatus('deprecated')
wwpLeosLldpRemOrgDefInfoTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4), )
if mibBuilder.loadTexts: wwpLeosLldpRemOrgDefInfoTable.setStatus('deprecated')
wwpLeosLldpRemOrgDefInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1), ).setIndexNames((0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemTimeMark"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemLocalPortNum"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemIndex"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfoOUI"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfoSubtype"), (0, "WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfoIndex"))
if mibBuilder.loadTexts: wwpLeosLldpRemOrgDefInfoEntry.setStatus('deprecated')
wwpLeosLldpRemOrgDefInfoOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3))
if mibBuilder.loadTexts: wwpLeosLldpRemOrgDefInfoOUI.setStatus('deprecated')
wwpLeosLldpRemOrgDefInfoSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: wwpLeosLldpRemOrgDefInfoSubtype.setStatus('deprecated')
wwpLeosLldpRemOrgDefInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: wwpLeosLldpRemOrgDefInfoIndex.setStatus('deprecated')
wwpLeosLldpRemOrgDefInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 4, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 507))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLldpRemOrgDefInfo.setStatus('deprecated')
wwpLeosLldpStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 1, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLldpStatsClear.setStatus('current')
wwpLeosLldpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2))
wwpLeosLldpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 1))
wwpLeosLldpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2))
wwpLeosLldpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 1, 1)).setObjects(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpConfigGroup"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsGroup"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysGroup"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysGroup"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpOptLocSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosLldpCompliance = wwpLeosLldpCompliance.setStatus('deprecated')
wwpLeosLldpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 1)).setObjects(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpMessageTxInterval"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpMessageTxHoldMultiplier"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpReinitDelay"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpTxDelay"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigAdminStatus"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigTLVsTxEnable"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpManAddrPortsTxEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosLldpConfigGroup = wwpLeosLldpConfigGroup.setStatus('deprecated')
wwpLeosLldpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 2)).setObjects(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesDiscardedTotal"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesInErrors"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesInTotal"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsFramesOutTotal"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsTLVsInErrors"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsTLVsDiscardedTotal"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpStatsTLVsUnrecognizedTotal"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpCounterDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosLldpStatsGroup = wwpLeosLldpStatsGroup.setStatus('deprecated')
wwpLeosLldpLocSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 3)).setObjects(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocChassisType"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocChassisId"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortType"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosLldpLocSysGroup = wwpLeosLldpLocSysGroup.setStatus('deprecated')
wwpLeosLldpOptLocSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 4)).setObjects(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocPortDesc"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysDesc"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysName"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysCapSupported"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocSysCapEnabled"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrIfSubtype"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrIfId"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpLocManAddrOID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosLldpOptLocSysGroup = wwpLeosLldpOptLocSysGroup.setStatus('deprecated')
wwpLeosLldpRemSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 2, 2, 5)).setObjects(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemoteChassisType"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemoteChassis"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemotePortType"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemRemotePort"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemPortDesc"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysName"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysDesc"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysCapSupported"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemSysCapEnabled"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrIfSubtype"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrIfId"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemManAddrOID"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemUnknownTLVInfo"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpRemOrgDefInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosLldpRemSysGroup = wwpLeosLldpRemSysGroup.setStatus('deprecated')
wwpLeosLldpPortSpeedChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 26, 3, 0, 1)).setObjects(("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigPortNum"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigOperPortSpeed"), ("WWP-LEOS-LLDP-MIB", "wwpLeosLldpPortConfigReqPortSpeed"))
if mibBuilder.loadTexts: wwpLeosLldpPortSpeedChangeTrap.setStatus('current')
mibBuilder.exportSymbols("WWP-LEOS-LLDP-MIB", WwpLeosLldpPortNumber=WwpLeosLldpPortNumber, wwpLeosLldpLocManAddrLen=wwpLeosLldpLocManAddrLen, wwpLeosLldpRemOrgDefInfoOUI=wwpLeosLldpRemOrgDefInfoOUI, wwpLeosLldpLocPortEntry=wwpLeosLldpLocPortEntry, WwpLeosLldpManAddrIfSubtype=WwpLeosLldpManAddrIfSubtype, wwpLeosLldpStatsFramesOutTotal=wwpLeosLldpStatsFramesOutTotal, wwpLeosLldpRemManAddrIfSubtype=wwpLeosLldpRemManAddrIfSubtype, wwpLeosLldpMIB=wwpLeosLldpMIB, wwpLeosLldpLocPortTable=wwpLeosLldpLocPortTable, wwpLeosLldpRemUnknownTLVEntry=wwpLeosLldpRemUnknownTLVEntry, wwpLeosLldpRemSysCapEnabled=wwpLeosLldpRemSysCapEnabled, wwpLeosLldpRemOrgDefInfoSubtype=wwpLeosLldpRemOrgDefInfoSubtype, wwpLeosLldpRemRemoteChassis=wwpLeosLldpRemRemoteChassis, wwpLeosLldpRemSysName=wwpLeosLldpRemSysName, wwpLeosLldpRemUnknownTLVInfo=wwpLeosLldpRemUnknownTLVInfo, wwpLeosLldpRemManAddrEntry=wwpLeosLldpRemManAddrEntry, wwpLeosLldpPortConfigPortNum=wwpLeosLldpPortConfigPortNum, wwpLeosLldpStatsFramesInErrors=wwpLeosLldpStatsFramesInErrors, wwpLeosLldpLocManAddrOID=wwpLeosLldpLocManAddrOID, wwpLeosLldpPortConfigReqPortSpeed=wwpLeosLldpPortConfigReqPortSpeed, wwpLeosLldpReinitDelay=wwpLeosLldpReinitDelay, wwpLeosLldpPortConfigTable=wwpLeosLldpPortConfigTable, wwpLeosLldpConfigGroup=wwpLeosLldpConfigGroup, wwpLeosLldpStatsEntry=wwpLeosLldpStatsEntry, wwpLeosLldpStatsTLVsUnrecognizedTotal=wwpLeosLldpStatsTLVsUnrecognizedTotal, wwpLeosLldpLocalSystemData=wwpLeosLldpLocalSystemData, wwpLeosLldpLocSysCapEnabled=wwpLeosLldpLocSysCapEnabled, wwpLeosLldpRemUnknownTLVTable=wwpLeosLldpRemUnknownTLVTable, wwpLeosLldpStatsFramesDiscardedTotal=wwpLeosLldpStatsFramesDiscardedTotal, wwpLeosLldpPortConfigEntry=wwpLeosLldpPortConfigEntry, wwpLeosLldpCompliances=wwpLeosLldpCompliances, wwpLeosLldpRemRemotePortType=wwpLeosLldpRemRemotePortType, wwpLeosLldpGroups=wwpLeosLldpGroups, wwpLeosLldpOptLocSysGroup=wwpLeosLldpOptLocSysGroup, wwpLeosLldpPortConfigTLVsTxEnable=wwpLeosLldpPortConfigTLVsTxEnable, wwpLeosLldpStatsPortNum=wwpLeosLldpStatsPortNum, wwpLeosLldpRemSysDesc=wwpLeosLldpRemSysDesc, wwpLeosLldpLocPortType=wwpLeosLldpLocPortType, wwpLeosLldpLocSysName=wwpLeosLldpLocSysName, wwpLeosLldpRemRemoteChassisType=wwpLeosLldpRemRemoteChassisType, wwpLeosLldpStatsClear=wwpLeosLldpStatsClear, wwpLeosLldpExtentions=wwpLeosLldpExtentions, wwpLeosLldpMessageTxHoldMultiplier=wwpLeosLldpMessageTxHoldMultiplier, wwpLeosLldpLocManAddrType=wwpLeosLldpLocManAddrType, wwpLeosLldpRemUnknownTLVType=wwpLeosLldpRemUnknownTLVType, wwpLeosLldpStatsTLVsInErrors=wwpLeosLldpStatsTLVsInErrors, wwpLeosLldpPortConfigStatsClear=wwpLeosLldpPortConfigStatsClear, wwpLeosLldpLocManAddrEntry=wwpLeosLldpLocManAddrEntry, wwpLeosLldpRemIndex=wwpLeosLldpRemIndex, WwpLeosLldpPortIdType=WwpLeosLldpPortIdType, wwpLeosLldpConfigManAddrEntry=wwpLeosLldpConfigManAddrEntry, wwpLeosLldpRemTable=wwpLeosLldpRemTable, wwpLeosLldpLocManAddrIfSubtype=wwpLeosLldpLocManAddrIfSubtype, wwpLeosLldpLocPortId=wwpLeosLldpLocPortId, wwpLeosLldpLocPortDesc=wwpLeosLldpLocPortDesc, wwpLeosLldpRemoteSystemsData=wwpLeosLldpRemoteSystemsData, WwpLeosLldpPortId=WwpLeosLldpPortId, WwpLeosLldpChassisId=WwpLeosLldpChassisId, wwpLeosLldpRemTimeMark=wwpLeosLldpRemTimeMark, wwpLeosLldpManAddrPortsTxEnable=wwpLeosLldpManAddrPortsTxEnable, wwpLeosLldpLocPortNum=wwpLeosLldpLocPortNum, wwpLeosLldpRemOrgDefInfo=wwpLeosLldpRemOrgDefInfo, wwpLeosLldpLocSysGroup=wwpLeosLldpLocSysGroup, wwpLeosLldpRemSysGroup=wwpLeosLldpRemSysGroup, SnmpAdminString=SnmpAdminString, wwpLeosLldpLocManAddr=wwpLeosLldpLocManAddr, wwpLeosLldpCompliance=wwpLeosLldpCompliance, WwpLeosLldpChassisIdType=WwpLeosLldpChassisIdType, wwpLeosLldpConfiguration=wwpLeosLldpConfiguration, TimeFilter=TimeFilter, wwpLeosLldpPortConfigAdminStatus=wwpLeosLldpPortConfigAdminStatus, WwpLeosLldpPortList=WwpLeosLldpPortList, wwpLeosLldpRemSysCapSupported=wwpLeosLldpRemSysCapSupported, wwpLeosLldpStatsTable=wwpLeosLldpStatsTable, wwpLeosLldpTxDelay=wwpLeosLldpTxDelay, wwpLeosLldpRemManAddrOID=wwpLeosLldpRemManAddrOID, wwpLeosLldpConformance=wwpLeosLldpConformance, wwpLeosLldpLocSysDesc=wwpLeosLldpLocSysDesc, wwpLeosLldpRemLocalPortNum=wwpLeosLldpRemLocalPortNum, wwpLeosLldpRemPortDesc=wwpLeosLldpRemPortDesc, wwpLeosLldpGlobalAtts=wwpLeosLldpGlobalAtts, wwpLeosLldpRemManAddrIfId=wwpLeosLldpRemManAddrIfId, wwpLeosLldpPortSpeedChangeTrap=wwpLeosLldpPortSpeedChangeTrap, wwpLeosLldpLocChassisType=wwpLeosLldpLocChassisType, PYSNMP_MODULE_ID=wwpLeosLldpMIB, wwpLeosLldpLocChassisId=wwpLeosLldpLocChassisId, wwpLeosLldpRemOrgDefInfoIndex=wwpLeosLldpRemOrgDefInfoIndex, wwpLeosLldpRemManAddrType=wwpLeosLldpRemManAddrType, wwpLeosLldpStatsFramesInTotal=wwpLeosLldpStatsFramesInTotal, wwpLeosLldpLocSysCapSupported=wwpLeosLldpLocSysCapSupported, wwpLeosLldpCounterDiscontinuityTime=wwpLeosLldpCounterDiscontinuityTime, wwpLeosLldpMessageTxInterval=wwpLeosLldpMessageTxInterval, wwpLeosLldpRemManAddrTable=wwpLeosLldpRemManAddrTable, wwpLeosLldpLocManAddrIfId=wwpLeosLldpLocManAddrIfId, wwpLeosLldpRemOrgDefInfoTable=wwpLeosLldpRemOrgDefInfoTable, wwpLeosLldpRemEntry=wwpLeosLldpRemEntry, wwpLeosLldpNotifMIBNotification=wwpLeosLldpNotifMIBNotification, WwpLeosLldpSystemCapabilitiesMap=WwpLeosLldpSystemCapabilitiesMap, wwpLeosLldpStatsGroup=wwpLeosLldpStatsGroup, WwpLeosLldpManAddress=WwpLeosLldpManAddress, wwpLeosLldpStatistics=wwpLeosLldpStatistics, wwpLeosLldpLocManAddrTable=wwpLeosLldpLocManAddrTable, wwpLeosLldpMIBObjects=wwpLeosLldpMIBObjects, wwpLeosLldpConfigManAddrTable=wwpLeosLldpConfigManAddrTable, wwpLeosLldpStatsTLVsDiscardedTotal=wwpLeosLldpStatsTLVsDiscardedTotal, wwpLeosLldpPortConfigOperPortSpeed=wwpLeosLldpPortConfigOperPortSpeed, wwpLeosLldpRemRemotePort=wwpLeosLldpRemRemotePort, wwpLeosLldpNotifMIBNotificationPrefix=wwpLeosLldpNotifMIBNotificationPrefix, wwpLeosLldpRemManAddr=wwpLeosLldpRemManAddr, wwpLeosLldpRemOrgDefInfoEntry=wwpLeosLldpRemOrgDefInfoEntry)
