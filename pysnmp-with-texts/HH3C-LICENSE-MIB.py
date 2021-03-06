#
# PySNMP MIB module HH3C-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LICENSE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
PhysicalIndex, PhysicalIndexOrZero = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "PhysicalIndexOrZero")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Counter64, TimeTicks, NotificationType, IpAddress, Bits, Counter32, MibIdentifier, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter64", "TimeTicks", "NotificationType", "IpAddress", "Bits", "Counter32", "MibIdentifier", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32")
RowStatus, DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
hh3cLicense = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 145))
hh3cLicense.setRevisions(('2013-09-18 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cLicense.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hh3cLicense.setLastUpdated('201309181000Z')
if mibBuilder.loadTexts: hh3cLicense.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cLicense.setContactInfo('Platform Team H3C Technologies Co., Ltd. Haidian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cLicense.setDescription('This MIB is used to manage license, including license key, activation key and activation file.')
hh3cLicenseScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 145, 1))
hh3cLicenseTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2))
hh3cLicenseNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3))
hh3cLicenseNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 145, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLicenseNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseNotifyEnable.setDescription('This object indicates whether the notifications of license should be generated.')
hh3cLicenseOpEntryMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 145, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLicenseOpEntryMaxNum.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpEntryMaxNum.setDescription('This object indicates the maximum number of entries that may be held in hh3cLicenseOpEntry. When the number of entries in hh3cLicenseOpEntry reached the value of this object, the oldest entry would be destroyed automatic after executing a new operation.')
hh3cLicenseNextFreeOpIndex = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 145, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseNextFreeOpIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseNextFreeOpIndex.setDescription('This object indicates the appropriate value for hh3cLicenseOpIndex that can be used to create an entry in hh3cLicenseOpTable.')
hh3cLicenseDevInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1), )
if mibBuilder.loadTexts: hh3cLicenseDevInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseDevInfoTable.setDescription('A table that displays device information which use to apply license.')
hh3cLicenseDevInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1), ).setIndexNames((0, "HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"))
if mibBuilder.loadTexts: hh3cLicenseDevInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseDevInfoEntry.setDescription('A set of objects that displays device information of license.')
hh3cLicensePhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLicensePhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cLicensePhysicalIndex.setDescription('The entPhysicalIndex of the device. The meaning of this object is associated with the management state which from hh3cLicenseInstallType. Note that: 1) hh3cLicenseInstallType is installInChassis. This object represents the entPhysicalIndex of the local active MPU. 2) hh3cLicenseInstallType is installInSlot. This object represents the entPhysicalIndex of MPU boards. 3) hh3cLicenseInstallType is installInCPU. This object represents the entPhysicalIndex of the CPUs on an MPU board. ')
hh3cLicenseSN = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseSN.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseSN.setDescription('The serial number of the device.')
hh3cLicenseDeviceIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("keyString", 2), ("file", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseDeviceIDType.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseDeviceIDType.setDescription('The types of device ID. invalid - The device ID is invalid. keyString - The device ID is a string. file - The device ID is a file.')
hh3cLicenseDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseDeviceID.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseDeviceID.setDescription('A string represents the device ID. For example: Device ID: XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX This object can not be read when hh3cLicenseDeviceIDType is invalid, and a file name with full path while hh3cLicenseDeviceIDType is file. For example: Device ID: flash:/xxx.did')
hh3cLicenseHardwareInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseHardwareInfo.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseHardwareInfo.setDescription('The information of the device hardware.')
hh3cLicenseMaxNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseMaxNum.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseMaxNum.setDescription('The max number of licenses that can be installed in device.')
hh3cLicenseUsedNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseUsedNum.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseUsedNum.setDescription('The number of installed licenses.')
hh3cLicenseRecyclableNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseRecyclableNum.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseRecyclableNum.setDescription('The number of recyclable storage for licenses.')
hh3cLicenseInstallType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 1), ("installInChassis", 2), ("installInSlot", 3), ("installInCPU", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseInstallType.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseInstallType.setDescription('The state of license management. This object determines the instance of hh3cLicensePhysicalIndex and hh3cLicenseOpPhysicalIndex. invalid - The state is invalid as driver fault. installInChassis - License is chassis locked. installInSlot - License is MPU locked. installInCPU - License is CPU locked.')
hh3cLicenseFileStoragePath = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseFileStoragePath.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseFileStoragePath.setDescription('The storage path of the installed license files.')
hh3cLicenseGeneralTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2), )
if mibBuilder.loadTexts: hh3cLicenseGeneralTable.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseGeneralTable.setDescription('A table that displays general information of installed license.')
hh3cLicenseGeneralEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1), ).setIndexNames((0, "HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"), (0, "HH3C-LICENSE-MIB", "hh3cLicenseIndex"))
if mibBuilder.loadTexts: hh3cLicenseGeneralEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseGeneralEntry.setDescription('A set of objects that displays general information of installed license.')
hh3cLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLicenseIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseIndex.setDescription('ID that can be used to uniquely identify a license. It may use a stable storage index.')
hh3cLicenseFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseFeature.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseFeature.setDescription('The name of the licensed feature. When there multiple features, this object will display with space as delimiter.')
hh3cLicenseProductDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseProductDescr.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseProductDescr.setDescription('The product description in a license.')
hh3cLicenseFileDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseFileDescr.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseFileDescr.setDescription('The file description in activation file.')
hh3cLicenseState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("invalid", 1), ("inuse", 2), ("usable", 3), ("expired", 4), ("uninstalled", 5), ("unusable", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseState.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseState.setDescription("The state of an installed license. invalid - The license is invalid and cannot be used. inuse - The license is being used. usable - The license is available for use. 1. If multiple days-restricted licenses for one feature are installed, only one license is in 'inuse' state and the rest licenses are in 'usable' state. 2. A date-restricted license is in this state if its start date is not reached. expired - The license has expired. uninstalled - The license has been uninstalled. unusable - The license cannot be used.")
hh3cLicenseActivationFile = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseActivationFile.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseActivationFile.setDescription('The name of an installed activation file, with device name and file name. For example: flash:/license/210231A1V0A1290000012013032718261184345.ak ')
hh3cLicenseActivationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseActivationKey.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseActivationKey.setDescription('The activation key that has been installed. For example: Activation Key: dyKT-x3vc-W@Ca-n4gn-Yo83-rVY3-C8:7-e3pg')
hh3cLicenseLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseLicenseKey.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseLicenseKey.setDescription('The license key that has been installed.')
hh3cLicenseUninstActivationFile = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseUninstActivationFile.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseUninstActivationFile.setDescription('If an activation file is uninstalled, the system creates an uninstall file. Use this file together with the SN and DID of the transfer destination to register the license for the transfer destination.')
hh3cLicenseUninstActivationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseUninstActivationKey.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseUninstActivationKey.setDescription('If an activation key is uninstalled, the system creates an uninstall key. Use this key together with the SN and DID of the transfer destination to register the license for the transfer destination.')
hh3cLicenseType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unknown", 1), ("permanent", 2), ("daysRestricted", 3), ("trialDaysRestricted", 4), ("dateRestricted", 5), ("trialDateRestricted", 6), ("countRestricted", 7), ("trialCountRestricted", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseType.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseType.setDescription('License type by validity period. unknown - The system cannot obtain the license type. permanent - Purchased license that never expires and is always valid. daysRestricted - Purchased license that is valid for a period in days. trialDaysRestricted - Free trial license that is valid for a period in days. dateRestricted - Purchased license that is valid for an absolute date range. trialDateRestricted - Free trial license that is valid for an absolute date range. countRestricted - Purchased license that is valid for several useing times. trialCountRestricted - Free trial license that is valid for several useing times. ')
hh3cLicenseInstalledTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseInstalledTime.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseInstalledTime.setDescription('Time when the license was installed. For example, it would be displayed as: 2013-9-20,13:30:15.0 ')
hh3cLicenseUninstalledTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseUninstalledTime.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseUninstalledTime.setDescription('The time when the license was uninstalled. For example, it would be displayed as: 2013-9-26,15:12:20.0 ')
hh3cLicenseDaysLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseDaysLeft.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseDaysLeft.setDescription('Remaining days of the license. This object is available for a days-restricted license.')
hh3cLicenseValidityStart = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 15), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseValidityStart.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseValidityStart.setDescription('Start date for a date-restricted license. This object is available for a date-restricted license. But if the start date is not limited, this object is unavailable. For example, it would be displayed as: 2013-9-26,15:12:20.0 ')
hh3cLicenseValidityEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 16), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseValidityEnd.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseValidityEnd.setDescription('End date for a date-restricted license. This object is available for a date-restricted license. But if the end date is not limited, this object is unavailable. For example, it would be displayed as: 2014-9-26,15:12:20.0 ')
hh3cLicenseExpiredDays = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseExpiredDays.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseExpiredDays.setDescription('Passed days after a license has been expired.')
hh3cLicenseCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 2, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseCount.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseCount.setDescription('The effective number of license. This object is available for a count-restricted license.')
hh3cLicenseFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3), )
if mibBuilder.loadTexts: hh3cLicenseFeatureTable.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseFeatureTable.setDescription('A table that displays installed licenses for features.')
hh3cLicenseFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3, 1), ).setIndexNames((0, "HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"), (1, "HH3C-LICENSE-MIB", "hh3cLicenseFeatureName"))
if mibBuilder.loadTexts: hh3cLicenseFeatureEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseFeatureEntry.setDescription('A set of objects that displays installed licenses for features.')
hh3cLicenseFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseFeatureName.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseFeatureName.setDescription('Feature that must be licensed before being used.')
hh3cLicenseFeatureState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notLicensed", 1), ("trialLicense", 2), ("formalLicense", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseFeatureState.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseFeatureState.setDescription('License type by purchasing state. notLicensed - The feature is not licensed. trialLicense - The feature is using trial license. formalLicense - The feature is using purchased license.')
hh3cLicenseOpTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4), )
if mibBuilder.loadTexts: hh3cLicenseOpTable.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpTable.setDescription('A table that used to install or uninstall license.')
hh3cLicenseOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1), ).setIndexNames((0, "HH3C-LICENSE-MIB", "hh3cLicenseOpIndex"))
if mibBuilder.loadTexts: hh3cLicenseOpEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpEntry.setDescription('A set of objects used to install or uninstall license.')
hh3cLicenseOpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLicenseOpIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpIndex.setDescription('ID that can be used to uniquely identify an operation.')
hh3cLicenseOpPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 2), PhysicalIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLicenseOpPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpPhysicalIndex.setDescription('This object indicates that the entPhysicalIndex of the device where the operation is being executed. The meaning of this object is associated with the management state from hh3cLicenseInstallType. Note that: 1) hh3cLicenseInstallType is installInChassis. This object represents the entPhysicalIndex of chassis local master. 2) hh3cLicenseInstallType is installInSlot. This object represents the entPhysicalIndex of MPU boards. 3) hh3cLicenseInstallType is installInCPU. This object represents the entPhysicalIndex of CPUs. This object must be set and can not be set to zero when executing an operation. ')
hh3cLicenseOpType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("compress", 1), ("delete", 2), ("installActivationFile", 3), ("installActivationKey", 4), ("installLicenseKey", 5), ("uninstallActivationFile", 6), ("uninstallActivationKey", 7), ("uninstallLicenseKey", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLicenseOpType.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpType.setDescription('The type of this operation. compress - Compress the license storage if the free license storage is not sufficient. Note that: 1) After compressing, the expired licenses and uninstalled licenses in the storage area will be cleared. 2) The DID changes each time the license storage is compressed. 3) Before performing a compression, make sure all activation files generated based on the old DID have been installed. They cannot be installed after the compression. delete - Compress one license storage only. installActivationFile - Install an activation file. installActivationKey - Install an activation key. installLicenseKey - Install a license key. uninstallActivationFile - Uninstall an activation file. uninstallActivationKey - Uninstall an activation key. uninstallLicenseKey - Uninstall a license key.')
hh3cLicenseOpString = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLicenseOpString.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpString.setDescription('This object might be an activation file name, an activation key or a license key that is to be installed, uninstalled or deleted. The operation type is specified in hh3cLicenseOpType. For compressing, this object must not be bound when creating a row. For deletion, this object could be an activation file, an activation key or a license key. For installActivationFile and uninstallActivationFile, this object must be a name of an activation file, with full path. Such as: flash:/license/210231A1V0A1290000012013032718261184345.ak For installActivationKey and uninstallActivationKey, this object must be an activation key. For installLicenseKey and uninstallLicenseKey, this object must be a license key.')
hh3cLicenseOpNotifyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLicenseOpNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpNotifyEnable.setDescription("This object indicates whether 'hh3cLicenseOpCompletion' notifications will be generated after this operation is completed. Note that, this object is meaningless if the value of 'hh3cLicenseNotifyEnable' is 'false'.")
hh3cLicenseOpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLicenseOpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpRowStatus.setDescription('The status of this conceptual row. When an entry was in active status, values of any object in this entry are forbidden to be changed.')
hh3cLicenseOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("opInProgress", 1), ("opSuccessful", 2), ("opFailed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseOpState.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpState.setDescription("The state of this operation. opInProgress - This operation is in progress. opSuccessful - Successful to execute this operation. opFailed - Failed to execute this operation, and 'hh3cLicenseOpFailedReason' will indicate the detailed cause of the failure.")
hh3cLicenseOpFailedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseOpFailedReason.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpFailedReason.setDescription('This object indicates the detailed cause of the failure when this operation failed.')
hh3cLicenseOpEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 145, 2, 4, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLicenseOpEndTime.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpEndTime.setDescription('The value of sysUpTime when the operation is done.')
hh3cLicenseNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0))
hh3cLicenseOpCompletion = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 1)).setObjects(("HH3C-LICENSE-MIB", "hh3cLicenseOpIndex"), ("HH3C-LICENSE-MIB", "hh3cLicenseOpPhysicalIndex"), ("HH3C-LICENSE-MIB", "hh3cLicenseOpType"), ("HH3C-LICENSE-MIB", "hh3cLicenseOpString"), ("HH3C-LICENSE-MIB", "hh3cLicenseOpState"), ("HH3C-LICENSE-MIB", "hh3cLicenseOpFailedReason"))
if mibBuilder.loadTexts: hh3cLicenseOpCompletion.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseOpCompletion.setDescription('This notification is generated when a license operation completed.')
hh3cLicenseActivationFileLost = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 2)).setObjects(("HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"), ("HH3C-LICENSE-MIB", "hh3cLicenseActivationFile"))
if mibBuilder.loadTexts: hh3cLicenseActivationFileLost.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseActivationFileLost.setDescription('This notification is generated when the activation file has been lost.')
hh3cLicenseActivationFileRestored = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 3)).setObjects(("HH3C-LICENSE-MIB", "hh3cLicensePhysicalIndex"), ("HH3C-LICENSE-MIB", "hh3cLicenseActivationFile"))
if mibBuilder.loadTexts: hh3cLicenseActivationFileRestored.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseActivationFileRestored.setDescription('This notification is generated when the activation file restored successfully.')
hh3cLicenseExpired = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 4)).setObjects(("HH3C-LICENSE-MIB", "hh3cLicenseFeatureName"), ("HH3C-LICENSE-MIB", "hh3cLicenseFeatureState"))
if mibBuilder.loadTexts: hh3cLicenseExpired.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseExpired.setDescription('This notification is generated when the license expires.')
hh3cLicenseExpireWarning = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 0, 5)).setObjects(("HH3C-LICENSE-MIB", "hh3cLicenseFeatureName"), ("HH3C-LICENSE-MIB", "hh3cLicenseFeatureState"), ("HH3C-LICENSE-MIB", "hh3cLicenseBindValidityPeriodRemaining"))
if mibBuilder.loadTexts: hh3cLicenseExpireWarning.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseExpireWarning.setDescription('This notification is generated when is about to expire.')
hh3cLicenseNotificationBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 1))
hh3cLicenseBindValidityPeriodRemaining = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 145, 3, 1, 1), Unsigned32()).setUnits('days').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLicenseBindValidityPeriodRemaining.setStatus('current')
if mibBuilder.loadTexts: hh3cLicenseBindValidityPeriodRemaining.setDescription("This object indicates the remaining days before the feature's license expires.")
mibBuilder.exportSymbols("HH3C-LICENSE-MIB", hh3cLicenseOpState=hh3cLicenseOpState, hh3cLicenseMaxNum=hh3cLicenseMaxNum, hh3cLicenseActivationFile=hh3cLicenseActivationFile, hh3cLicenseOpTable=hh3cLicenseOpTable, hh3cLicenseActivationFileRestored=hh3cLicenseActivationFileRestored, hh3cLicenseGeneralEntry=hh3cLicenseGeneralEntry, hh3cLicenseUninstActivationKey=hh3cLicenseUninstActivationKey, hh3cLicenseOpType=hh3cLicenseOpType, hh3cLicenseOpIndex=hh3cLicenseOpIndex, hh3cLicenseRecyclableNum=hh3cLicenseRecyclableNum, hh3cLicenseOpString=hh3cLicenseOpString, hh3cLicensePhysicalIndex=hh3cLicensePhysicalIndex, hh3cLicenseUninstalledTime=hh3cLicenseUninstalledTime, hh3cLicenseValidityEnd=hh3cLicenseValidityEnd, hh3cLicenseValidityStart=hh3cLicenseValidityStart, hh3cLicenseLicenseKey=hh3cLicenseLicenseKey, hh3cLicenseOpEntry=hh3cLicenseOpEntry, hh3cLicenseNotificationPrefix=hh3cLicenseNotificationPrefix, hh3cLicenseExpireWarning=hh3cLicenseExpireWarning, hh3cLicenseExpiredDays=hh3cLicenseExpiredDays, hh3cLicenseBindValidityPeriodRemaining=hh3cLicenseBindValidityPeriodRemaining, hh3cLicenseFeatureEntry=hh3cLicenseFeatureEntry, hh3cLicenseDevInfoEntry=hh3cLicenseDevInfoEntry, hh3cLicenseActivationKey=hh3cLicenseActivationKey, hh3cLicenseFeatureState=hh3cLicenseFeatureState, hh3cLicenseFeatureTable=hh3cLicenseFeatureTable, hh3cLicenseNotifyEnable=hh3cLicenseNotifyEnable, hh3cLicenseFileDescr=hh3cLicenseFileDescr, hh3cLicenseType=hh3cLicenseType, hh3cLicenseOpRowStatus=hh3cLicenseOpRowStatus, hh3cLicenseUsedNum=hh3cLicenseUsedNum, hh3cLicenseDaysLeft=hh3cLicenseDaysLeft, hh3cLicenseActivationFileLost=hh3cLicenseActivationFileLost, hh3cLicenseGeneralTable=hh3cLicenseGeneralTable, hh3cLicense=hh3cLicense, hh3cLicenseDeviceIDType=hh3cLicenseDeviceIDType, hh3cLicenseSN=hh3cLicenseSN, hh3cLicenseFeature=hh3cLicenseFeature, hh3cLicenseExpired=hh3cLicenseExpired, hh3cLicenseNotifications=hh3cLicenseNotifications, hh3cLicenseNotificationBindings=hh3cLicenseNotificationBindings, hh3cLicenseState=hh3cLicenseState, hh3cLicenseInstallType=hh3cLicenseInstallType, hh3cLicenseScalarObjects=hh3cLicenseScalarObjects, hh3cLicenseTables=hh3cLicenseTables, hh3cLicenseHardwareInfo=hh3cLicenseHardwareInfo, hh3cLicenseFeatureName=hh3cLicenseFeatureName, hh3cLicenseOpCompletion=hh3cLicenseOpCompletion, hh3cLicenseOpNotifyEnable=hh3cLicenseOpNotifyEnable, hh3cLicenseFileStoragePath=hh3cLicenseFileStoragePath, hh3cLicenseInstalledTime=hh3cLicenseInstalledTime, hh3cLicenseOpEndTime=hh3cLicenseOpEndTime, hh3cLicenseOpEntryMaxNum=hh3cLicenseOpEntryMaxNum, hh3cLicenseDeviceID=hh3cLicenseDeviceID, PYSNMP_MODULE_ID=hh3cLicense, hh3cLicenseDevInfoTable=hh3cLicenseDevInfoTable, hh3cLicenseCount=hh3cLicenseCount, hh3cLicenseUninstActivationFile=hh3cLicenseUninstActivationFile, hh3cLicenseOpPhysicalIndex=hh3cLicenseOpPhysicalIndex, hh3cLicenseOpFailedReason=hh3cLicenseOpFailedReason, hh3cLicenseNextFreeOpIndex=hh3cLicenseNextFreeOpIndex, hh3cLicenseIndex=hh3cLicenseIndex, hh3cLicenseProductDescr=hh3cLicenseProductDescr)
