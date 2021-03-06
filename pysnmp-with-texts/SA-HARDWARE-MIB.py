#
# PySNMP MIB module SA-HARDWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SA-HARDWARE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:59:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ObjectIdentity, ModuleIdentity, TimeTicks, IpAddress, Integer32, Unsigned32, Counter32, MibIdentifier, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "IpAddress", "Integer32", "Unsigned32", "Counter32", "MibIdentifier", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sa = MibIdentifier((1, 3, 6, 1, 4, 1, 1429))
saVoip = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 78))
saHardware = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 78, 4))
saHardware.setRevisions(('2015-05-11 00:00', '2015-04-13 00:00', '2015-04-03 00:00', '2015-01-14 00:00', '1901-12-15 00:00', '2014-11-20 00:00', '2014-07-31 00:00', '1904-06-14 00:00', '1914-02-11 00:00', '2014-01-13 00:00', '2014-01-10 00:00', '1913-10-17 00:00', '1913-07-04 00:00', '1913-06-07 00:00', '1913-05-30 00:00', '1913-02-06 00:00', '1912-12-05 00:00', '1912-11-28 00:00', '1912-11-07 00:00', '1912-08-23 00:00', '1912-05-08 00:00', '1912-04-10 00:00', '1911-09-02 00:00', '1911-08-19 00:00', '1911-06-13 00:00', '1910-11-16 00:00', '1910-10-26 00:00', '1910-10-18 00:00', '1910-04-27 00:00', '1910-04-07 00:00', '1909-11-05 00:00', '1909-10-05 00:00', '1908-01-17 00:00', '1907-09-20 00:00', '1907-07-16 00:00', '1906-09-11 00:00', '1906-08-07 00:00', '1905-12-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: saHardware.setRevisionsDescriptions(('Add europe-5-85 to saHwDescrDiplexer. More details added to the current available options', 'Changed le9562 to le9652(13) in saHwDescrSlic Corrected UTC dates that give compile warnings', 'Added le9562 (13) to saHwDescrSlic Added en2810 (8) to saHwDescrMocaType', 'Updated MIB Copyright Banner', 'Added clr240-cl2330 to saHwDescrWirelessChip Added usb30wBCM to saHwDescrUsbType Added moca20wBCM to saHwDescrMocaType Added internalBCM to saHwDescrEthSwitch Added bcm33843E(22), bcm3385(23), puma6-D(24), puma6MG-D(25) to saHwDescrMainProcessor', 'Added two new fields (mxl265d (11) and mxl267d (12)) to saHwDescrTuner', 'Added le9541d(12) to saHwDescrSlic', 'Moving bcm43228hp-5ghz(22) to (32) and changing bcm43217-bcm4360hp(32) to (22)', 'Add bcm3384 to saHwDescrMainProcessor', 'Remove ath9880-ath9580 from saHwDescrWirelessChip as it is not being used and replace (32) with bcm43217-bcm4360hp', 'Changed 3 lines: north-america-85/108(5) to north-america-85-108(5)puma6_B2(19), to puma6-B2(19), puma6MG_B2(20) to puma6MG-B2(20)', 'Updated saHwDescrMainProcessor for B2 chipset from Intel; updated saHwDescrDiplexer to include high US split', 'Added bcm33843 to saHwDescrMainProcessor, Added bcm6803 and ad9965 to saHwDescrMocaType, Added ath9880-ath9580 to saHwDescrWirelessChip', 'Updated saHwDescrWirelessType to reflect dual wifi card combination, changed saHwDescrWirelessChip combo bcm4331sp-bcm4360sp(19) to bcm4331sp-bcm4360hp(19)', 'Updated for Puma6MG: saHwDescrMainProcessor, saHwDescrTuner, saHwDescrWirelessType, saHwDescrWirelessChip, saHwDescrUsbType', 'Updated saHwDescrWirelessChip due to compilation issues', 'Updated saHwDescrWirelessChip description and values', 'Updated saHwDescrTuner and saHwDescrMocaType for the USGv2 products', 'Updated saHwDescrWirelessChip for the 3383-based products', ' Updated saHwDescrWirelessChip (13) to ath9381 from ath9380 as instructed by HW team', 'Updated HW nonvols for USGv2 based products: saHwDescrMainProcessor, saHwDescrTuner, saHwDescrSlic, saHwDescrWirelessChip saHwDescrUsbType, saHwDescrEthSwitch', 'Updated HW nonvols for 3383 based products - CR 19170 bcm53125 was changed to 53124 and bcm43227 was changed to bcm43217', 'Updated le9531d for D2R2 SL products', 'Updated Ethernet switch type with bcm53101e and bcm53125s. Corrected ar8316 from ar3816.', 'Updated MainProcessor Type, Wireless Chip Type, SlicType, MocaType and Ethernet switch type for new products', 'Added le9520S for single line DPC2420', 'Added le9500s new slictype for DPC2203', 'Added bcm3382 to the MainProcessor object', 'Added usb203380G(5) value to saHwUsbType', 'Added tipuma5Tc4800 for saHwDescrMainProcessor', 'Added singleBand and dualBand names to WirelessChip type', 'Added items for Ethernet Switch type Wireless chip type diplexer type ( korea) main processor ( 3380) tuner type modified usb type', 'Added items for DOCSIS3.0 products Added DMS tree', 'Added le9520ddtc to saHwDescrSlic (1868)', 'Added saHwDescrDmsType (1637) Added saHwDescrMocaType (1637) Added saHwDescrEthSwitch (1637)', 'Added bcm3349ipbg to saHwDescrMainProcessor Added bcm3420iml to saHwDescrTuner Added bcm4318 to saHwDescrWirelessChip Added saHwDescrFactoryId (928)', 'Added bcm3381A1 and bcm3381A2 to saHwDescrMainProcessor Added bcm3420x3 to saHwDescrTuner Added usb20w3381 to saHwDescrUsbType Changed usb20 to usb20wPLX in saHwDescrUsbType', 'Initial release',))
if mibBuilder.loadTexts: saHardware.setLastUpdated('201505110000Z')
if mibBuilder.loadTexts: saHardware.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: saHardware.setContactInfo('http://support.cisco.com')
if mibBuilder.loadTexts: saHardware.setDescription('This tree can be read from any IP in a device.')
saHwDescr = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1))
saHwDescrModel = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrModel.setStatus('current')
if mibBuilder.loadTexts: saHwDescrModel.setDescription('')
saHwDescrHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrHardwareVersion.setStatus('current')
if mibBuilder.loadTexts: saHwDescrHardwareVersion.setDescription('')
saHwDescrSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrSerialNumber.setStatus('current')
if mibBuilder.loadTexts: saHwDescrSerialNumber.setDescription('')
saHwDescrCmMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrCmMacAddress.setStatus('current')
if mibBuilder.loadTexts: saHwDescrCmMacAddress.setDescription('')
saHwDescrManufactureDate = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrManufactureDate.setStatus('current')
if mibBuilder.loadTexts: saHwDescrManufactureDate.setDescription('')
saHwDescrPowerSupply = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal-switching", 1), ("external", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrPowerSupply.setStatus('current')
if mibBuilder.loadTexts: saHwDescrPowerSupply.setDescription('')
saHwDescrDiplexer = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 0), ("north-america-5-42", 1), ("europe-5-65", 2), ("japan", 3), ("korea", 4), ("north-america-85-108", 5), ("europe-5-85", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrDiplexer.setStatus('current')
if mibBuilder.loadTexts: saHwDescrDiplexer.setDescription('')
saHwDescrMainProcessor = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))).clone(namedValues=NamedValues(("bcm3349", 1), ("bcm3349kfb", 2), ("bcm3368", 3), ("bcm3381A1", 4), ("bcm3381A2", 5), ("bcm3349ipbg", 6), ("tipuma5", 7), ("bcm3361", 8), ("bcm3378", 9), ("bcm3380", 10), ("tipuma5Tc4800", 11), ("bcm3382", 12), ("bcm3371", 13), ("bcm3379", 14), ("bcm3383", 15), ("puma6", 16), ("puma6MG", 17), ("bcm33843Z", 18), ("puma6-B2", 19), ("puma6MG-B2", 20), ("bcm3384", 21), ("bcm33843E", 22), ("bcm3385", 23), ("puma6-D", 24), ("puma6MG-D", 25), ("bcm3384ZU", 26)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrMainProcessor.setStatus('current')
if mibBuilder.loadTexts: saHwDescrMainProcessor.setDescription('tipuma5Tc4800(11) value will represent TI chips 4800zdw, 4800zdwg, 4800zdwgu. and original tipuma5(7)value will represent TI chips 4830zdw, 4830zdwg and 4830zdwgu ')
saHwDescrTuner = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("none", 0), ("bcm3419", 1), ("bcm3420", 2), ("bcm3420x3", 3), ("bcm3420iml", 4), ("mt2170", 5), ("bcm3421", 6), ("bcmInternal", 7), ("mxl265", 8), ("mxl265v2", 9), ("mxl267", 10), ("mxl265d", 11), ("mxl267d", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrTuner.setStatus('current')
if mibBuilder.loadTexts: saHwDescrTuner.setDescription('')
saHwDescrSlic = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("none", 0), ("le9500b", 1), ("le9500c", 2), ("le9500d", 3), ("le9520ddtc", 4), ("le88276", 5), ("le9530d", 6), ("le9500s", 7), ("le9520s", 8), ("le9540d", 9), ("le9531d", 10), ("zl88702", 11), ("le9541d", 12), ("le9652", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrSlic.setStatus('current')
if mibBuilder.loadTexts: saHwDescrSlic.setDescription('')
saHwDescrMemoryMain = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 11), Integer32()).setUnits('Megabytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrMemoryMain.setStatus('current')
if mibBuilder.loadTexts: saHwDescrMemoryMain.setDescription('')
saHwDescrMemoryFlash = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 12), Integer32()).setUnits('Megabytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrMemoryFlash.setStatus('current')
if mibBuilder.loadTexts: saHwDescrMemoryFlash.setDescription('')
saHwDescrWirelessType = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("ieee80211b", 1), ("ieee80211g", 2), ("ieee80211n", 3), ("ieee80211ac", 4), ("ieee80211n-ieee80211ac", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrWirelessType.setStatus('current')
if mibBuilder.loadTexts: saHwDescrWirelessType.setDescription('')
saHwDescrWirelessChip = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33))).clone(namedValues=NamedValues(("none", 0), ("bcm4306", 1), ("bcm4318", 2), ("bcm4318E", 3), ("bcm4322", 4), ("bcm43224-dualBand", 5), ("bcm43225-singleBand", 6), ("bcm4313", 7), ("bcm43217", 8), ("bcm43228", 9), ("bcm43217sp-bcm43228sp", 10), ("ath9380", 11), ("ath9580", 12), ("ath9381sp-ath9580sp", 13), ("bcm43228sp-5ghz", 14), ("bcm4331sp", 15), ("bcm43217sp-bcm4331sp", 16), ("bcm4331sp-bcm4331sp", 17), ("bcm43217sp-bcm4360sp", 18), ("bcm4331sp-bcm4360hp", 19), ("bcm43217hp", 20), ("bcm43228hp", 21), ("bcm43217-bcm4360hp", 22), ("bcm43217hp-bcm4331sp", 23), ("bcm43217hp-bcm4360sp", 24), ("bcm4331hp-bcm43217sp", 25), ("bcm4331hp-bcm43228sp", 26), ("bcm4331hp-bcm4331sp", 27), ("bcm4331hp-bcm4331hp", 28), ("bcm4331hp-bcm4360sp", 29), ("bcm4331hp-bcm4360hp", 30), ("ath9381sp-qca9880", 31), ("bcm43228hp-5ghz", 32), ("clr240-cl2330", 33)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrWirelessChip.setStatus('current')
if mibBuilder.loadTexts: saHwDescrWirelessChip.setDescription('Wireless chip hardware configuration. SP stands for Standard Power HP stands for High Power For two-chip configurations, the chip on the left is 2.4GHz, the other is 5 GHz. The following chips are dual-band capable: 4331, 43224, 43228. The following chips are 5GHz capable: 4360. The following chips support up to 3x3: 9380, 9580, 9381, 4331. The following chips support up to 2x2: 43224, 43225, 43217, 43228.')
saHwDescrDectType = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("north-america", 1), ("europe", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrDectType.setStatus('current')
if mibBuilder.loadTexts: saHwDescrDectType.setDescription('')
saHwDescrUsbType = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("usb11", 1), ("usb20wPLX", 2), ("usb20w3381", 3), ("usb20wPuma5", 4), ("usb203380G", 5), ("usb20wPuma6", 6), ("usb20wPuma6MG", 7), ("usb30wBCM", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrUsbType.setStatus('current')
if mibBuilder.loadTexts: saHwDescrUsbType.setDescription('')
saHwDescrFactoryId = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrFactoryId.setStatus('current')
if mibBuilder.loadTexts: saHwDescrFactoryId.setDescription('')
saHwDescrDmsType = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("dms1", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrDmsType.setStatus('current')
if mibBuilder.loadTexts: saHwDescrDmsType.setDescription('')
saHwDescrMocaType = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("en2210", 1), ("en2510", 2), ("en2710", 3), ("vxc1030", 4), ("bcm6803", 5), ("ad9965", 6), ("moca20wBCM", 7), ("en2810", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrMocaType.setStatus('current')
if mibBuilder.loadTexts: saHwDescrMocaType.setDescription('')
saHwDescrEthSwitch = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("none", 0), ("bcm5325m", 1), ("marv6095f", 2), ("bcm5325e", 3), ("bcm53115s", 4), ("ar8316", 5), ("bcm53101e", 6), ("bcm53124s", 7), ("marv6172", 8), ("internalBCM", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrEthSwitch.setStatus('current')
if mibBuilder.loadTexts: saHwDescrEthSwitch.setDescription('')
saHwDescrIntCount = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101))
saHwDescrIntCountEthernet = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrIntCountEthernet.setStatus('current')
if mibBuilder.loadTexts: saHwDescrIntCountEthernet.setDescription('')
saHwDescrIntCountUsb = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrIntCountUsb.setStatus('current')
if mibBuilder.loadTexts: saHwDescrIntCountUsb.setDescription('')
saHwDescrIntCountPhoneLine = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrIntCountPhoneLine.setStatus('current')
if mibBuilder.loadTexts: saHwDescrIntCountPhoneLine.setDescription('')
saHwDescrIntCountMaxBattery = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrIntCountMaxBattery.setStatus('current')
if mibBuilder.loadTexts: saHwDescrIntCountMaxBattery.setDescription('')
saHwDescrIntCountWireless = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrIntCountWireless.setStatus('current')
if mibBuilder.loadTexts: saHwDescrIntCountWireless.setDescription('')
saHwDescrIntCountDect = MibScalar((1, 3, 6, 1, 4, 1, 1429, 78, 4, 1, 101, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: saHwDescrIntCountDect.setStatus('current')
if mibBuilder.loadTexts: saHwDescrIntCountDect.setDescription('')
mibBuilder.exportSymbols("SA-HARDWARE-MIB", saHwDescrIntCountEthernet=saHwDescrIntCountEthernet, saHwDescrUsbType=saHwDescrUsbType, saHwDescrModel=saHwDescrModel, saHwDescrIntCountDect=saHwDescrIntCountDect, saHwDescrCmMacAddress=saHwDescrCmMacAddress, saHwDescrSlic=saHwDescrSlic, saHwDescrEthSwitch=saHwDescrEthSwitch, saHwDescrDmsType=saHwDescrDmsType, saHwDescrIntCount=saHwDescrIntCount, saHwDescrWirelessType=saHwDescrWirelessType, saHwDescrTuner=saHwDescrTuner, saHwDescrIntCountPhoneLine=saHwDescrIntCountPhoneLine, saHwDescrMainProcessor=saHwDescrMainProcessor, saHwDescr=saHwDescr, saHwDescrIntCountMaxBattery=saHwDescrIntCountMaxBattery, saHwDescrDiplexer=saHwDescrDiplexer, saHwDescrDectType=saHwDescrDectType, saHwDescrFactoryId=saHwDescrFactoryId, saVoip=saVoip, saHwDescrWirelessChip=saHwDescrWirelessChip, saHwDescrHardwareVersion=saHwDescrHardwareVersion, saHwDescrSerialNumber=saHwDescrSerialNumber, saHwDescrIntCountUsb=saHwDescrIntCountUsb, saHwDescrMemoryMain=saHwDescrMemoryMain, saHwDescrPowerSupply=saHwDescrPowerSupply, saHwDescrManufactureDate=saHwDescrManufactureDate, saHwDescrIntCountWireless=saHwDescrIntCountWireless, sa=sa, saHwDescrMocaType=saHwDescrMocaType, saHardware=saHardware, saHwDescrMemoryFlash=saHwDescrMemoryFlash, PYSNMP_MODULE_ID=saHardware)
