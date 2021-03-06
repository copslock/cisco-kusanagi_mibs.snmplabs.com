#
# PySNMP MIB module ZhoneDsl-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZhoneDsl-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:52:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, IpAddress, NotificationType, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ObjectIdentity, iso, ModuleIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "IpAddress", "NotificationType", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ObjectIdentity", "iso", "ModuleIdentity", "TimeTicks", "MibIdentifier")
VariablePointer, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "VariablePointer", "TextualConvention", "DisplayString")
zhoneDsl, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneDsl", "zhoneModules")
ZhoneRowStatus, ZhoneAdminString = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus", "ZhoneAdminString")
zhoneDsl_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 3)).setLabel("zhoneDsl-MIB")
zhoneDsl_MIB.setRevisions(('2000-04-26 17:53',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zhoneDsl_MIB.setRevisionsDescriptions(('strawman structure',))
if mibBuilder.loadTexts: zhoneDsl_MIB.setLastUpdated('200005111753Z')
if mibBuilder.loadTexts: zhoneDsl_MIB.setOrganization('Zhone')
if mibBuilder.loadTexts: zhoneDsl_MIB.setContactInfo(' Postal: xxx Zhone Technologies, Inc. xxx address. Fremont, Ca. Toll-Free: 877-ZHONE20 (+1 877-946-6320) Tel: +1 978-452-0571 Fax: +1 978-xxx-xxxx E-mail: xxx@zhone.com ')
if mibBuilder.loadTexts: zhoneDsl_MIB.setDescription('The MIB module to describe the Zhone specific implementation of HDSL, HDSL2, SDSL and G.SHDSL')
zhoneDslLineTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1), )
if mibBuilder.loadTexts: zhoneDslLineTable.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineTable.setDescription('This table contains common attributes describing DSL physical line interfaces for DSLs without a MIB standard.')
zhoneDslLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zhoneDslLineEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineEntry.setDescription('An entry in the zhoneDslLine Table.')
zhoneDslLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 96))).clone(namedValues=NamedValues(("hdsl", 1), ("hdsl2", 2), ("shdsl", 3), ("sdsl", 96))).clone('hdsl2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDslLineType.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineType.setDescription('The DSL type. Many modem vendors allow software selection between HDSL, HDSL2, SDSL and SHDSL. Using zhoneDslLineTypeSupported the user can see what dsl option is available on this interface.')
zhoneDslLineCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 2), Bits().clone(namedValues=NamedValues(("hdsl", 1), ("hdsl2", 2), ("shdsl", 4), ("sdsl", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslLineCapabilities.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineCapabilities.setDescription('The DSL types supported on this interface. This is a bit-map of possible types. This variable can be used to determine zhoneDslLineType.')
zhoneDslLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("down", 1), ("downloading", 2), ("activated", 3), ("training", 4), ("up", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslLineStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineStatus.setDescription('The DSL modem status. Detailed modem state maybe available in the status table. ')
zhoneDslUpLineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 4), Gauge32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslUpLineRate.setStatus('current')
if mibBuilder.loadTexts: zhoneDslUpLineRate.setDescription('The DSL upstream (cpe->co) line rate on this interface.')
zhoneDslDownLineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 5), Gauge32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslDownLineRate.setStatus('current')
if mibBuilder.loadTexts: zhoneDslDownLineRate.setDescription('The DSL downstream (co->cpe) line rate on this interface.')
zhoneDslLineConfigProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 6), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDslLineConfigProfile.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineConfigProfile.setDescription("The value of this object identifies the row in the respective dsl configuration profile table. (Ex: if zhoneDslLineType is HDSL2, then the profile identifies an HDSL2 configuration profile.) It is assumed that all profile names are unique to the system. In the case which the configuration profile has not been set, the value will be set to `ZhoneDefault'. This is a profile (by type) which will be persisted and then able to be modified by a management station in order to modify the DEFAULT values. ")
zhoneDslLineAlarmProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 7), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDslLineAlarmProfile.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineAlarmProfile.setDescription("The value of this object identifies the row in the respective dsl alarm profile table. (Ex: if zhoneDslLineType is HDSL2 then the profile identifies an HDSL2 alarm profile.) It is assumed that all profile names are unique to the system. In the case where the configuration profile has not been set, the value will be set to `ZhoneDefault'. ")
zhoneDslLineRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 8), ZhoneRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneDslLineRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneDslLineRowStatus.setDescription('Row status in order to add an entry in this table. The required fields to be added are: (ARE ALL THE DEFAULTS OKAY) ')
zhoneHdsl2ConfigProfileTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3), )
if mibBuilder.loadTexts: zhoneHdsl2ConfigProfileTable.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigProfileTable.setDescription('This table contains information for HDSL2 configuration.')
zhoneHdsl2ConfigProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1), ).setIndexNames((1, "ZhoneDsl-MIB", "zhoneHdsl2ConfigProfileName"))
if mibBuilder.loadTexts: zhoneHdsl2ConfigProfileEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigProfileEntry.setDescription('An entry in the zhoneHdsl2ConfigProfile Table.')
zhoneHdsl2ConfigProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 1), ZhoneAdminString())
if mibBuilder.loadTexts: zhoneHdsl2ConfigProfileName.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigProfileName.setDescription("Configuration profile name. Used by the zhoneHdsl2LineConfigProfile entry to map zhoneDslLine Entry to the appropriate profile. When `dynamic' profiles are implemented, the profile name is user specified. Also, the system will always provide a default profile whose name is `DEFVAL'. When `static' profiles are implemented, there is an one-to-one relationship between each line and its profile. In which case, the profile name will need to algorithmically represent the Line's ifIndex. Therefore, the profile's name is a decimal zed string of the ifIndex that is fixed-length (i.e., 10) with leading zero(s). For example, the profile name for ifIndex which equals '15' will be '0000000015'.")
zhoneHdsl2ConfigUnitMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("co", 1), ("cpe", 2))).clone('co')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneHdsl2ConfigUnitMode.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigUnitMode.setDescription('Unit is configured as the CO(central office)or CPE (customer premise)side.')
zhoneHdsl2ConfigTransmitPowerbackoffMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("backoff-disable", 1), ("backoff-enable", 2), ("no-change-backoff", 3))).clone('backoff-disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneHdsl2ConfigTransmitPowerbackoffMode.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigTransmitPowerbackoffMode.setDescription('Determines if the transmit power backoff defined in HDSL2 standard is used.')
zhoneHdsl2ConfigDecoderCoeffA = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 4), Integer32().clone(970752)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneHdsl2ConfigDecoderCoeffA.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigDecoderCoeffA.setDescription('21 bit value corresponding to the decoder coefficient A. The default is the ANSI HDSL2 default.')
zhoneHdsl2ConfigDecoderCoeffB = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 5), Integer32().clone(970752)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneHdsl2ConfigDecoderCoeffB.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigDecoderCoeffB.setDescription('21 bit value corresponding to the decoder coefficient A. The default is the ANSI HDSL2 default.')
zhoneHdsl2ConfigFrameSyncWord = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 6), Integer32().clone(45)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneHdsl2ConfigFrameSyncWord.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigFrameSyncWord.setDescription('10 bit frame sync word. The default is the HDSL2 standard.')
zhoneHdsl2ConfigStuffBits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneHdsl2ConfigStuffBits.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigStuffBits.setDescription('4 bit stuff pattern. The default is the HDSL2 standard.')
zhoneHdsl2ConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 8), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneHdsl2ConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2ConfigRowStatus.setDescription('Status in order to create/delete rows. For creation the following fields are required:')
zhoneHdsl2StatusTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4), )
if mibBuilder.loadTexts: zhoneHdsl2StatusTable.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2StatusTable.setDescription('This table contains HDSL2 specific line status information. An entry into this table is automatically created whenever a zhoneDslLineEntry is created and the type is HDSL2.')
zhoneHdsl2StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1), )
ifIndex.registerAugmentions(("ZhoneDsl-MIB", "zhoneHdsl2StatusEntry"))
zhoneHdsl2StatusEntry.setIndexNames(*ifIndex.getIndexNames())
if mibBuilder.loadTexts: zhoneHdsl2StatusEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2StatusEntry.setDescription('An entry in the zhoneHdsl2Status Table.')
zhoneHdsl2DriftAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("rx-clk-alarm", 1), ("tx-clk-alarm", 2), ("tx-rx-clk-alarm", 3), ("no-drift-alarm", 4), ("not-applicable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2DriftAlarm.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2DriftAlarm.setDescription(' Indicates that the framer automatically attempted to adjust for clock drift. This is not applicable for ATM.')
zhoneHdsl2FramerIBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2FramerIBStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2FramerIBStatus.setDescription('Returns the segd,sega,uib and losd bits. The format of the octet is: x x x x segd sega uib losd.')
zhoneHdsl2LocalPSDMaskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2LocalPSDMaskStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2LocalPSDMaskStatus.setDescription('Returns a number corresponding to the transmit power backoff requested by the local unit.')
zhoneHdsl2LoopAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 4), Integer32()).setUnits('tenth DB').setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2LoopAttenuation.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2LoopAttenuation.setDescription('Estimation of the loop attenuation in tenths of a DB. by the local unit.')
zhoneHdsl2LossWordStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no-lossw-defect", 1), ("lossw-defect", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2LossWordStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2LossWordStatus.setDescription('This indicates loss of sync.')
zhoneHdsl2RmtPSDMaskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2RmtPSDMaskStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2RmtPSDMaskStatus.setDescription('Returns a number corresponding to the transmit power backoff requested by the remote unit.')
zhoneHdsl2RmtCountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2RmtCountryCode.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2RmtCountryCode.setDescription('ANSI HDSL2 Country code of the remote unit.')
zhoneHdsl2RmtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2RmtVersion.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2RmtVersion.setDescription('HDSL2 version of the remote unit.')
zhoneHdsl2RmtProviderCode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2RmtProviderCode.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2RmtProviderCode.setDescription('Provider word of the remote unit.')
zhoneHdsl2RmtVendorData = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2RmtVendorData.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2RmtVendorData.setDescription("The remote unit's vendor-provided data.")
zhoneHdsl2RmtTxEncoderA = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2RmtTxEncoderA.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2RmtTxEncoderA.setDescription("The remote unit's 21 bit encoder coefficient A")
zhoneHdsl2RmtTxEncoderB = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2RmtTxEncoderB.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2RmtTxEncoderB.setDescription("The remote unit's 21 bit encoder coefficient B")
zhoneHdsl2TipRingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reverse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2TipRingStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2TipRingStatus.setDescription('Indicates whether the tip and ring points from the local unit match the tip and ring points of the remote.')
zhoneHdsl2FrameSyncWord = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2FrameSyncWord.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2FrameSyncWord.setDescription('A 10 bit number indicating the frame sync word used. LSB justified')
zhoneHdsl2StuffBits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneHdsl2StuffBits.setStatus('current')
if mibBuilder.loadTexts: zhoneHdsl2StuffBits.setDescription('A 4 bit number for the stuff bits. LSB justified.')
zhoneDslPerfDataTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5), )
if mibBuilder.loadTexts: zhoneDslPerfDataTable.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfDataTable.setDescription('This table provides one row for each modem interface.')
zhoneDslPerfDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1), )
zhoneDslLineEntry.registerAugmentions(("ZhoneDsl-MIB", "zhoneDslPerfDataEntry"))
zhoneDslPerfDataEntry.setIndexNames(*zhoneDslLineEntry.getIndexNames())
if mibBuilder.loadTexts: zhoneDslPerfDataEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfDataEntry.setDescription('An entry in zhoneDslPerfDataTable.')
zhoneDslPerfLofs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfLofs.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfLofs.setDescription('Count of the number of Loss of Framing failures since agent reset.')
zhoneDslPerfLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfLoss.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfLoss.setDescription('Count of the number of Loss of Signal failures since agent reset.')
zhoneDslPerfLols = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfLols.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfLols.setDescription('Count of the number of Loss of Link failures since agent reset.')
zhoneDslPerfInits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfInits.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfInits.setDescription('Count of the line initialization attempts since agent reset. Includes both successful and failed attempts.')
zhoneDslPerfCur15MinTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 5), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfCur15MinTimeElapsed.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfCur15MinTimeElapsed.setDescription('The number of seconds elapsed since the start of the current measurement period.')
zhoneDslPerfCur15MinLofs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 6), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfCur15MinLofs.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfCur15MinLofs.setDescription('Count of the number of Loss of Framing failures in the current 15 minute interval.')
zhoneDslPerfCur15MinLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 7), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfCur15MinLoss.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfCur15MinLoss.setDescription('Count of seconds in the current 15 minute interval when there was a Loss of Signal.')
zhoneDslPerfCur15MinLols = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 8), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfCur15MinLols.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfCur15MinLols.setDescription('Count of seconds in the current 15 minute interval when there was of Loss of Link.')
zhoneDslPerfCur15MinInits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneDslPerfCur15MinInits.setStatus('current')
if mibBuilder.loadTexts: zhoneDslPerfCur15MinInits.setDescription('Count of the line initialization attempts in the current 15 minute interval. Includes both successful and failed attempts.')
zhoneDslAlarmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 4, 6), )
if mibBuilder.loadTexts: zhoneDslAlarmProfileTable.setStatus('current')
if mibBuilder.loadTexts: zhoneDslAlarmProfileTable.setDescription('This table contains information for Alarm conditions. One entry in this table reflects a profile defined by a manager which can be used to define alarm conditions for a modem.')
zhoneDslAlarmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1), ).setIndexNames((1, "ZhoneDsl-MIB", "zhoneDslAlarmProfileName"))
if mibBuilder.loadTexts: zhoneDslAlarmProfileEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneDslAlarmProfileEntry.setDescription('An entry in the zhoneDslAlarmProfile Table.')
zhoneDslAlarmProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 1), ZhoneAdminString())
if mibBuilder.loadTexts: zhoneDslAlarmProfileName.setStatus('current')
if mibBuilder.loadTexts: zhoneDslAlarmProfileName.setDescription("Configuration profile name. Used by the zhoneDslLineConfigProfile entry to map zhoneDslLine Entry to the appropriate profile. When `dynamic' profiles are implemented, the profile name is user specified. Also, the system will always provide a default profile whose name is `DEFVAL'. When `static' profiles are implemented, there is an one-to-one relationship between each line and its profile. In which case, the profile name will need to algorithmically represent the Line's ifIndex. Therefore, the profile's name is a decimal zed string of the ifIndex that is fixed-length (i.e., 10) with leading zero(s). For example, the profile name for ifIndex which equals '15' will be '0000000015'.")
zhoneDslThreshold15MinLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDslThreshold15MinLoss.setStatus('current')
if mibBuilder.loadTexts: zhoneDslThreshold15MinLoss.setDescription('The number of Loss of signal seconds on a DSL interface within any given 15 minutes performance data collection period, which causes the SNMP agent to send a TRAP. 0 will disable the trap.')
zhoneDslThreshold15MinLols = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDslThreshold15MinLols.setStatus('current')
if mibBuilder.loadTexts: zhoneDslThreshold15MinLols.setDescription('The number of Loss of link seconds on a DSL interface within any given 15 minutes performance data collection period, which causes the SNMP agent to send a TRAP. 0 will disable the trap.')
zhoneDslThreshold15MinLofs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneDslThreshold15MinLofs.setStatus('current')
if mibBuilder.loadTexts: zhoneDslThreshold15MinLofs.setDescription('The number of Loss of framing seconds on a DSL interface within any given 15 minutes performance data collection period, which causes the SNMP agent to send a TRAP. 0 will disable the trap.')
zhoneDslAlarmProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 5), ZhoneAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zhoneDslAlarmProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneDslAlarmProfileRowStatus.setDescription("RowStatus field to control deletion/addition of entries in this table. Minimal fields to be 'set' for a creation is:")
mibBuilder.exportSymbols("ZhoneDsl-MIB", zhoneDslLineType=zhoneDslLineType, zhoneDslPerfCur15MinLoss=zhoneDslPerfCur15MinLoss, zhoneHdsl2LocalPSDMaskStatus=zhoneHdsl2LocalPSDMaskStatus, zhoneDslThreshold15MinLofs=zhoneDslThreshold15MinLofs, zhoneHdsl2ConfigProfileName=zhoneHdsl2ConfigProfileName, zhoneDslLineRowStatus=zhoneDslLineRowStatus, zhoneDslLineConfigProfile=zhoneDslLineConfigProfile, zhoneDslPerfCur15MinLofs=zhoneDslPerfCur15MinLofs, zhoneHdsl2RmtProviderCode=zhoneHdsl2RmtProviderCode, zhoneHdsl2ConfigDecoderCoeffA=zhoneHdsl2ConfigDecoderCoeffA, zhoneDslPerfLoss=zhoneDslPerfLoss, zhoneDslPerfLols=zhoneDslPerfLols, zhoneDslAlarmProfileEntry=zhoneDslAlarmProfileEntry, zhoneHdsl2RmtTxEncoderA=zhoneHdsl2RmtTxEncoderA, PYSNMP_MODULE_ID=zhoneDsl_MIB, zhoneDslPerfCur15MinLols=zhoneDslPerfCur15MinLols, zhoneHdsl2StatusTable=zhoneHdsl2StatusTable, zhoneDslPerfLofs=zhoneDslPerfLofs, zhoneDslPerfCur15MinTimeElapsed=zhoneDslPerfCur15MinTimeElapsed, zhoneHdsl2ConfigProfileEntry=zhoneHdsl2ConfigProfileEntry, zhoneHdsl2ConfigFrameSyncWord=zhoneHdsl2ConfigFrameSyncWord, zhoneDslPerfDataEntry=zhoneDslPerfDataEntry, zhoneDslPerfCur15MinInits=zhoneDslPerfCur15MinInits, zhoneDslAlarmProfileTable=zhoneDslAlarmProfileTable, zhoneHdsl2ConfigRowStatus=zhoneHdsl2ConfigRowStatus, zhoneDslLineTable=zhoneDslLineTable, zhoneHdsl2ConfigUnitMode=zhoneHdsl2ConfigUnitMode, zhoneDslPerfInits=zhoneDslPerfInits, zhoneHdsl2FramerIBStatus=zhoneHdsl2FramerIBStatus, zhoneHdsl2DriftAlarm=zhoneHdsl2DriftAlarm, zhoneHdsl2RmtPSDMaskStatus=zhoneHdsl2RmtPSDMaskStatus, zhoneDslLineEntry=zhoneDslLineEntry, zhoneHdsl2ConfigTransmitPowerbackoffMode=zhoneHdsl2ConfigTransmitPowerbackoffMode, zhoneHdsl2RmtCountryCode=zhoneHdsl2RmtCountryCode, zhoneHdsl2RmtVersion=zhoneHdsl2RmtVersion, zhoneDslDownLineRate=zhoneDslDownLineRate, zhoneHdsl2ConfigProfileTable=zhoneHdsl2ConfigProfileTable, zhoneDslAlarmProfileRowStatus=zhoneDslAlarmProfileRowStatus, zhoneHdsl2StuffBits=zhoneHdsl2StuffBits, zhoneHdsl2ConfigStuffBits=zhoneHdsl2ConfigStuffBits, zhoneDsl_MIB=zhoneDsl_MIB, zhoneDslPerfDataTable=zhoneDslPerfDataTable, zhoneDslLineStatus=zhoneDslLineStatus, zhoneHdsl2RmtVendorData=zhoneHdsl2RmtVendorData, zhoneHdsl2RmtTxEncoderB=zhoneHdsl2RmtTxEncoderB, zhoneHdsl2LossWordStatus=zhoneHdsl2LossWordStatus, zhoneDslLineCapabilities=zhoneDslLineCapabilities, zhoneDslUpLineRate=zhoneDslUpLineRate, zhoneHdsl2LoopAttenuation=zhoneHdsl2LoopAttenuation, zhoneHdsl2StatusEntry=zhoneHdsl2StatusEntry, zhoneHdsl2FrameSyncWord=zhoneHdsl2FrameSyncWord, zhoneDslLineAlarmProfile=zhoneDslLineAlarmProfile, zhoneDslThreshold15MinLoss=zhoneDslThreshold15MinLoss, zhoneHdsl2TipRingStatus=zhoneHdsl2TipRingStatus, zhoneHdsl2ConfigDecoderCoeffB=zhoneHdsl2ConfigDecoderCoeffB, zhoneDslAlarmProfileName=zhoneDslAlarmProfileName, zhoneDslThreshold15MinLols=zhoneDslThreshold15MinLols)
