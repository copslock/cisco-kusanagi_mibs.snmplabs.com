#
# PySNMP MIB module HUAWEI-ENERGYMNGT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ENERGYMNGT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:44:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
huaweiUtility, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiUtility")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, ObjectIdentity, ModuleIdentity, iso, Counter32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, TimeTicks, MibIdentifier, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "TimeTicks", "MibIdentifier", "Counter64", "Gauge32")
DateAndTime, RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
hwEnergyMngt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 157))
hwEnergyMngt.setRevisions(('2015-05-30 00:00', '2014-01-23 00:00', '2011-07-01 00:00', '2011-03-14 15:30', '2011-03-14 00:00', '2011-03-10 00:00', '2011-02-10 00:00', '2010-08-06 00:00', '2010-08-05 00:00', '2010-08-03 00:00', '2010-07-12 00:00', '2010-07-07 00:00', '2010-06-29 00:00', '2010-06-23 00:00', '2010-06-18 00:00', '2010-06-17 00:00', '2010-06-08 00:00', '2010-05-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwEnergyMngt.setRevisionsDescriptions(('V2.03. Add enum of hwEnergySavingMode:optimal. This is a draft version.', 'V2.02. Add hwEnergyDevId, hwEnergyDevChangeToSleep. This is a draft version.', 'V0.114. Add hwPoEType, hwPSEPower. Modify FTPC table. This is a draft version.', 'V0.113, add hwEnergyFtpcIpv4TransMode and hwEnergyFtpcTransMode. This is a draft version.', 'V0.112, modify hwEnergyFtpcTransFileIpv4Table and hwEnergyFtpcTransFileTable. This is a draft version.', 'V0.111, add hwEnergyFtpcObjects, including hwEnergyFtpcTransFileIpv4Table and hwEnergyFtpcTransFileTable. This is a draft version.', 'V0.11, add hwEnergySavingDescReqMode.', 'V0.10, modify hwBoardIndex.', 'V0.09, modify hwBoardType.', 'V0.08, modify watt to milliwatt. Modify enumeration of hwEnergySavingMode. Add boardType and boardDescription.', 'V0.08, modify hwPowerStatPeriod.', 'V0.06, modify hwPowerStatPeriod.', "V0.05, modify hwEnergySavingMethodEnable value list. Delete hwEnergySavingParameterTable first index 'hwEnergySavingMethodIndex'", 'V0.05, modify hwEnergySavingCapabilityMngtEntry, modify hwEnergySavingMethodTable', 'V0.04, modify hwEnergySavingCapabilityMngtEntry', 'V0.03, modify description for all MIB table', 'V0.02, add hwEnergySavingMethodEntry, add hwEnergySavingCapabilityMngt', 'V0.01 mib initial',))
if mibBuilder.loadTexts: hwEnergyMngt.setLastUpdated('201505300000Z')
if mibBuilder.loadTexts: hwEnergyMngt.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwEnergyMngt.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwEnergyMngt.setDescription('huawei energy management MIB.')
hwSysPowerMgnt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1))
hwPowerConsumption = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPowerConsumption.setStatus('current')
if mibBuilder.loadTexts: hwPowerConsumption.setDescription('NE total power consumption, counted from equipment first used. Joule(Watt * second). Note: If the device is a power supplier(PSE), the power consumption includes the outputs.')
hwPowerStatPeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fifteenMinutes", 1), ("thirtyMinutes", 2), ("oneHour", 3), ("oneDay", 4), ("oneWeek", 5), ("oneMonth", 6))).clone('oneHour')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPowerStatPeriod.setStatus('current')
if mibBuilder.loadTexts: hwPowerStatPeriod.setDescription('NE power statistics period: fifteenMinutes(1): The power statistics generated every 15 minutes. thirtyMinutes(2): The power statistics generated every 30 minutes. oneHour(3): The power statistics generated every hour. oneDay(4): The power statistics generated every day. oneWeek(5): The power statistics generated every week. oneMonth(6): The power statistics generated every month. The defaut statistics intervalue is one hour.')
hwAveragePower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAveragePower.setStatus('current')
if mibBuilder.loadTexts: hwAveragePower.setDescription('NE average power consumtion during a period: milliwatt')
hwRatedPower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRatedPower.setStatus('current')
if mibBuilder.loadTexts: hwRatedPower.setDescription('NE rated power: milliwatt')
hwThresholdOfPower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwThresholdOfPower.setStatus('current')
if mibBuilder.loadTexts: hwThresholdOfPower.setDescription('NE threshold power: milliwatt')
hwCurrentPower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCurrentPower.setStatus('current')
if mibBuilder.loadTexts: hwCurrentPower.setDescription('NE current power: milliwatt')
hwPoEType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("pse", 1), ("pd", 2), ("noPoe", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoEType.setStatus('current')
if mibBuilder.loadTexts: hwPoEType.setDescription('powered type: PSE(1): power supplier. PD(2): powered deivce. noPoe(255): not PSE or PD')
hwPSEPower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPSEPower.setStatus('current')
if mibBuilder.loadTexts: hwPSEPower.setDescription('The output power(milliwatt) by a PSE. For a non-PSE device, the value is zero.')
hwBoardPowerMngt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2))
hwBoardPowerMngtTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1), )
if mibBuilder.loadTexts: hwBoardPowerMngtTable.setStatus('current')
if mibBuilder.loadTexts: hwBoardPowerMngtTable.setDescription('This table describes current power and rated power of boards. The index is hwBoardIndex.')
hwBoardPowerMngtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1), ).setIndexNames((0, "HUAWEI-ENERGYMNGT-MIB", "hwBoardIndex"))
if mibBuilder.loadTexts: hwBoardPowerMngtEntry.setStatus('current')
if mibBuilder.loadTexts: hwBoardPowerMngtEntry.setDescription('The entry of hwBoardPowerMngtTable.')
hwBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBoardIndex.setStatus('current')
if mibBuilder.loadTexts: hwBoardIndex.setDescription('Index: reserved/shelf/frame/slot. The index is format by 4 bytes(8bit for 1 byte): reservedByte(0xFF), shelfID, frameID, slotID. e.g. shlef=1, frame=2, slot=17, the index is 0xFF010211(66065). If no shelfID or frameID, the corresponding byte is set to be 0xFF. e.g. no shlefID, no frameID, slot=17, the index is 0xFFFFFF11(4294967057). ')
hwBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBoardType.setStatus('current')
if mibBuilder.loadTexts: hwBoardType.setDescription('hwBoardType describes main type of board: LPU/SFU/ADSL/PSTN, etc. ')
hwBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBoardName.setStatus('current')
if mibBuilder.loadTexts: hwBoardName.setDescription('hwBoardName describes full name of board: CR52LPUA/CR57SFU40A/H805ADGG, etc. ')
hwBoardCurrentPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBoardCurrentPower.setStatus('current')
if mibBuilder.loadTexts: hwBoardCurrentPower.setDescription('current power of board(slot): milliwatt')
hwBoardRatedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBoardRatedPower.setStatus('current')
if mibBuilder.loadTexts: hwBoardRatedPower.setDescription('rated power of board(slot): milliwatt')
hwBoardThresholdOfPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBoardThresholdOfPower.setStatus('current')
if mibBuilder.loadTexts: hwBoardThresholdOfPower.setDescription('Threshold power of board(slot): milliwatt')
hwEnergySavingMngt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3))
hwEnergySavingMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("userDefined", 1), ("standard", 2), ("basic", 3), ("deep", 4), ("optimal", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwEnergySavingMode.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingMode.setDescription('Power saving mode: UserDefined(1): UserDined energy-saving mode, user can define energy-saving strategy. Standard(2): standard energy-saving mode Basic(3): basic energy-saving mode, many basic energy-saving strategy included. Deep(4): Deep energy-saving mode, many complex energy-saving strategy included, which may effect service. Optimal(5): Optimal energy-saving mode, many complex energy-saving strategy included, which may effect service. ')
hwEnergySavingMethodTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2), )
if mibBuilder.loadTexts: hwEnergySavingMethodTable.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingMethodTable.setDescription('hwEnergySavingMethodTable defines energy-saving Method for all mode. User can set a method with its parameter. The index of this table is hwEnergySavingMethodIndex. ')
hwEnergySavingMethodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2, 1), ).setIndexNames((0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMethodIndex"))
if mibBuilder.loadTexts: hwEnergySavingMethodEntry.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingMethodEntry.setDescription('Entry of energy-saveing method table.')
hwEnergySavingMethodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEnergySavingMethodIndex.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingMethodIndex.setDescription('The index of method in use. ')
hwEnergySavingMethodEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwEnergySavingMethodEnable.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingMethodEnable.setDescription('hwEnergySaveingMethodEnable describes the status of energy-saving method: enableed or disabled. ')
hwEnergySavingParameterTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3), )
if mibBuilder.loadTexts: hwEnergySavingParameterTable.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingParameterTable.setDescription('hwEnergySavingParameterTable defines parameters for all energy-saving methods. User can set parameter for a method. The index of this table: hwEnergySavingMethodIndex, hwEnergySavingParameterIndex.')
hwEnergySavingParameterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3, 1), ).setIndexNames((0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMethodIndex"), (0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingParameterIndex"))
if mibBuilder.loadTexts: hwEnergySavingParameterEntry.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingParameterEntry.setDescription('Entry of energy-saveing parameter table.')
hwEnergySavingParameterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEnergySavingParameterIndex.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingParameterIndex.setDescription('The second index of hwEnergySavingParameterTable. An energy-saving method might have more than one parameter. This index is used to identify the parameter for a method.')
hwEnergySavingParameterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwEnergySavingParameterValue.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingParameterValue.setDescription("The value of an energy-saveing method's parameter. The parameter is a format string. When NMS sets integer 12 as a parameter for a energy-saving method, the value is a string '12'. ")
hwEnergySavingCapabilityMngtTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4), )
if mibBuilder.loadTexts: hwEnergySavingCapabilityMngtTable.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingCapabilityMngtTable.setDescription('This table describes the energy-saving capability, including energy-saving methods and parameters. The index is hwEnergySavingCapabilityDescIndex. ')
hwEnergySavingCapabilityMngtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1), ).setIndexNames((0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingCapabilityDescIndex"))
if mibBuilder.loadTexts: hwEnergySavingCapabilityMngtEntry.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingCapabilityMngtEntry.setDescription('The entry of hwBoardPowerMngtTable.')
hwEnergySavingCapabilityDescIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEnergySavingCapabilityDescIndex.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingCapabilityDescIndex.setDescription('The index of hwEnergySavingCapabilityMngtTable. ')
hwEnergySavingCapabilityDescLanguage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEnergySavingCapabilityDescLanguage.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingCapabilityDescLanguage.setDescription("The language of EnergySavingCapabilityDescription file. 'en-gb'(English-GreatBraitain) 'zh-cn'(Chinese) ")
hwEnergySavingCapabilityDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10240))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEnergySavingCapabilityDesc.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingCapabilityDesc.setDescription('User can get the description string from hwEnergySavingCapabilityDesc. An XML file which is compressed by ZIP to less than 10240 bytes, describes the energy-saving capability, including all energy-saving methods and parameters. ')
hwEnergySavingDescReqMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("snmp", 1), ("ftp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEnergySavingDescReqMode.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingDescReqMode.setDescription('The mode describes how to get energy saving capability description file : snmp(1): Get the file using hwEnergySavingCapabilityDesc. ftp(2): Get the file using FTP, which described by hwEnergyFtpclientReqTable. ')
hwEnergyFtpcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4))
hwEnergyFtpcTransFileTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1), )
if mibBuilder.loadTexts: hwEnergyFtpcTransFileTable.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcTransFileTable.setDescription('This table is used to configure transfer file feature related parameters.')
hwEnergyFtpcTransFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1), ).setIndexNames((0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSetName"))
if mibBuilder.loadTexts: hwEnergyFtpcTransFileEntry.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcTransFileEntry.setDescription('Name identifying Transfer configuration')
hwEnergyFtpcSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hwEnergyFtpcSetName.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcSetName.setDescription('Name identifying FTPC Transfer configuration')
hwEnergyFtpcSrcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcSrcAddrType.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcSrcAddrType.setDescription('Source IP address Type: ipv4(1) ipv6(2)')
hwEnergyFtpcSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcSrcAddr.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcSrcAddr.setDescription('Source IP address')
hwEnergyFtpcVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcVpnName.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcVpnName.setDescription('VPN name used for the corresponding connection')
hwEnergyFtpcHostAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcHostAddrType.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcHostAddrType.setDescription('Server address type: ipv4(1) ipv6(2)')
hwEnergyFtpcHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcHostAddr.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcHostAddr.setDescription('Server IP address')
hwEnergyFtpcServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(21, 21), ValueRangeConstraint(1025, 55535), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcServerPort.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcServerPort.setDescription('Server port used for connection')
hwEnergyFtpcUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 85))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcUserName.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcUserName.setDescription('User Name used for user validation')
hwEnergyFtpcPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcPassword.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcPassword.setDescription('Password used for user validation. Password Length while setting should not be more than 16 characters, while querying password will be cipher text')
hwEnergyFtpcDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcDirectory.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcDirectory.setDescription('Local working directory')
hwEnergyFtpcSrcIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcSrcIfName.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcSrcIfName.setDescription('Interface Name')
hwEnergyFtpcTransCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwEnergyFtpcTransCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcTransCfgRowStatus.setDescription('The object specifies the status of this table entry. When the status is createAndGo, it allows to create and when value is destroy it allows to delete the record in the table')
hwEnergyFtpcAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("get", 1), ("put", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwEnergyFtpcAction.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcAction.setDescription('The type of request. get(1): To request a file from the FTP server. put(2): To send a file to the FTP server.')
hwEnergyFtpcTransMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ftp", 1), ("sftp", 2), ("tftp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwEnergyFtpcTransMode.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcTransMode.setDescription('The file transfer protocol. Default: FTP.')
hwEnergyFtpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("opInProgress", 1), ("opSuccess", 2), ("opInvalid", 3), ("opInvalidProtocol", 4), ("opInvalidSourceName", 5), ("opInvalidDestName", 6), ("opInvalidServerAddress", 7), ("opDeviceBusy", 8), ("opDeviceError", 9), ("opFileOpenError", 10), ("opFileTransferError", 11), ("opFileChecksumError", 12), ("opAuthFail", 13), ("opUnknownFailure", 14), ("opAbort", 15), ("opInvalidSourceAddress", 16), ("opInvalidSourceInterface", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwEnergyFtpOperStatus.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpOperStatus.setDescription('The OperStatus: opInProgress(1): the operation is in process. opSuccess(2): the operation has been completed successfully. opInvalid(3): the command is invalid or command-protocol-device combination is unsupported by the system. opInvalidProtocol(4): invalid protocol is specified opInvalidSourceName(5) :invalid source file name is specified. opInvalidDestName(6): invalid target name is specified. opInvalidServerAddress(7): invalid server address is specified opDeviceBusy(8): the device is in use and locked by another process opDeviceError(9): device read, write or erase error opFileOpenError(10) :invalid file name; file not found in partition opFileTransferError(11) :file transfer was unsuccessfull opFileChecksumError(12) :file checksum in Flash is invalid opAuthFail(13) :authentication failure opUnknownFailure(14) :failure which is unknown opAbort(15) : transfer operation has been aborted opInvalidSourceAddress(16): invalid source IP is specified. opInvalidSourceInterface(17): invalid source interface is specified. ')
hwEnergyTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 10))
hwEnergyDevId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 157, 10, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwEnergyDevId.setStatus('current')
if mibBuilder.loadTexts: hwEnergyDevId.setDescription('This object identifies the device ID.')
hwEnergyNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 11))
hwEnergyDevChangeToSleep = NotificationType((1, 3, 6, 1, 4, 1, 2011, 6, 157, 11, 1)).setObjects(("HUAWEI-ENERGYMNGT-MIB", "hwEnergyDevId"))
if mibBuilder.loadTexts: hwEnergyDevChangeToSleep.setStatus('current')
if mibBuilder.loadTexts: hwEnergyDevChangeToSleep.setDescription('This notification indicates device entering in the sleeping status.')
hwEnergyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6))
hwEnergyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 1))
hwEnergyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 1, 1)).setObjects(("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwEnergyCompliance = hwEnergyCompliance.setStatus('current')
if mibBuilder.loadTexts: hwEnergyCompliance.setDescription('Description.')
hwEnergyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2))
hwEnergyFtpcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 1)).setObjects(("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSrcAddrType"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSrcAddr"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcVpnName"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcHostAddrType"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcHostAddr"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcServerPort"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcUserName"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcPassword"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcDirectory"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSrcIfName"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcTransCfgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwEnergyFtpcGroup = hwEnergyFtpcGroup.setStatus('current')
if mibBuilder.loadTexts: hwEnergyFtpcGroup.setDescription('Description.')
hwSysPowerMgntGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 2)).setObjects(("HUAWEI-ENERGYMNGT-MIB", "hwThresholdOfPower"), ("HUAWEI-ENERGYMNGT-MIB", "hwPowerConsumption"), ("HUAWEI-ENERGYMNGT-MIB", "hwPowerStatPeriod"), ("HUAWEI-ENERGYMNGT-MIB", "hwAveragePower"), ("HUAWEI-ENERGYMNGT-MIB", "hwRatedPower"), ("HUAWEI-ENERGYMNGT-MIB", "hwCurrentPower"), ("HUAWEI-ENERGYMNGT-MIB", "hwPSEPower"), ("HUAWEI-ENERGYMNGT-MIB", "hwPoEType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSysPowerMgntGroup = hwSysPowerMgntGroup.setStatus('current')
if mibBuilder.loadTexts: hwSysPowerMgntGroup.setDescription('Description.')
hwEnergySavingMngtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 3)).setObjects(("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMode"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMethodIndex"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingParameterIndex"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingCapabilityDescIndex"), ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingDescReqMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwEnergySavingMngtGroup = hwEnergySavingMngtGroup.setStatus('current')
if mibBuilder.loadTexts: hwEnergySavingMngtGroup.setDescription('Description.')
hwEnergyNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 4)).setObjects(("HUAWEI-ENERGYMNGT-MIB", "hwEnergyDevChangeToSleep"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwEnergyNotificationGroup = hwEnergyNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwEnergyNotificationGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-ENERGYMNGT-MIB", hwEnergySavingParameterTable=hwEnergySavingParameterTable, hwBoardPowerMngtTable=hwBoardPowerMngtTable, hwEnergyFtpcGroup=hwEnergyFtpcGroup, hwEnergySavingMethodEnable=hwEnergySavingMethodEnable, hwBoardRatedPower=hwBoardRatedPower, hwCurrentPower=hwCurrentPower, hwEnergyFtpcTransFileTable=hwEnergyFtpcTransFileTable, hwEnergyFtpcUserName=hwEnergyFtpcUserName, hwEnergySavingParameterValue=hwEnergySavingParameterValue, hwBoardName=hwBoardName, hwSysPowerMgntGroup=hwSysPowerMgntGroup, hwBoardIndex=hwBoardIndex, hwPoEType=hwPoEType, hwEnergySavingMethodIndex=hwEnergySavingMethodIndex, hwEnergySavingCapabilityDesc=hwEnergySavingCapabilityDesc, hwEnergySavingCapabilityMngtTable=hwEnergySavingCapabilityMngtTable, hwEnergyCompliances=hwEnergyCompliances, hwEnergyFtpcAction=hwEnergyFtpcAction, hwEnergyTrapObjects=hwEnergyTrapObjects, hwBoardCurrentPower=hwBoardCurrentPower, hwSysPowerMgnt=hwSysPowerMgnt, hwEnergyFtpcSrcAddrType=hwEnergyFtpcSrcAddrType, hwEnergyFtpcSrcIfName=hwEnergyFtpcSrcIfName, hwEnergyDevChangeToSleep=hwEnergyDevChangeToSleep, hwEnergyNotification=hwEnergyNotification, hwEnergySavingParameterIndex=hwEnergySavingParameterIndex, hwEnergyFtpcPassword=hwEnergyFtpcPassword, hwThresholdOfPower=hwThresholdOfPower, hwEnergySavingMode=hwEnergySavingMode, hwBoardThresholdOfPower=hwBoardThresholdOfPower, hwEnergyFtpcHostAddrType=hwEnergyFtpcHostAddrType, hwEnergyFtpcDirectory=hwEnergyFtpcDirectory, PYSNMP_MODULE_ID=hwEnergyMngt, hwEnergySavingMngtGroup=hwEnergySavingMngtGroup, hwEnergyDevId=hwEnergyDevId, hwEnergyMngt=hwEnergyMngt, hwEnergyCompliance=hwEnergyCompliance, hwEnergySavingMethodEntry=hwEnergySavingMethodEntry, hwEnergyFtpcSetName=hwEnergyFtpcSetName, hwEnergyNotificationGroup=hwEnergyNotificationGroup, hwEnergyFtpcSrcAddr=hwEnergyFtpcSrcAddr, hwEnergySavingMethodTable=hwEnergySavingMethodTable, hwEnergySavingParameterEntry=hwEnergySavingParameterEntry, hwEnergyFtpcVpnName=hwEnergyFtpcVpnName, hwPowerStatPeriod=hwPowerStatPeriod, hwRatedPower=hwRatedPower, hwBoardPowerMngtEntry=hwBoardPowerMngtEntry, hwAveragePower=hwAveragePower, hwEnergyFtpcTransCfgRowStatus=hwEnergyFtpcTransCfgRowStatus, hwEnergyFtpcHostAddr=hwEnergyFtpcHostAddr, hwEnergyFtpcServerPort=hwEnergyFtpcServerPort, hwEnergyFtpOperStatus=hwEnergyFtpOperStatus, hwEnergySavingCapabilityMngtEntry=hwEnergySavingCapabilityMngtEntry, hwEnergyFtpcObjects=hwEnergyFtpcObjects, hwEnergySavingCapabilityDescIndex=hwEnergySavingCapabilityDescIndex, hwEnergySavingCapabilityDescLanguage=hwEnergySavingCapabilityDescLanguage, hwBoardType=hwBoardType, hwEnergyGroups=hwEnergyGroups, hwEnergyConformance=hwEnergyConformance, hwEnergySavingMngt=hwEnergySavingMngt, hwEnergySavingDescReqMode=hwEnergySavingDescReqMode, hwEnergyFtpcTransFileEntry=hwEnergyFtpcTransFileEntry, hwBoardPowerMngt=hwBoardPowerMngt, hwPSEPower=hwPSEPower, hwPowerConsumption=hwPowerConsumption, hwEnergyFtpcTransMode=hwEnergyFtpcTransMode)
