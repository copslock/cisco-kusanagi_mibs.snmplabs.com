#
# PySNMP MIB module ADTRAN-AOSUNIT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOSUNIT
# Produced by pysmi-0.3.4 at Wed May  1 11:14:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, IpAddress, NotificationType, TimeTicks, Bits, Counter64, iso, Gauge32, Unsigned32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "IpAddress", "NotificationType", "TimeTicks", "Bits", "Counter64", "iso", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32")
DisplayString, TAddress, TextualConvention, TDomain, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TAddress", "TextualConvention", "TDomain", "RowStatus")
adGenAOSUnitMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 1))
adGenAOSUnitMib.setRevisions(('2004-09-28 00:00', '2005-05-12 00:00', '2008-07-30 00:00', '2010-04-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSUnitMib.setRevisionsDescriptions(('Initial version of this MIB module.', 'Added OIDs for primary and backup image name and part number', 'Changed syntax range for adAOSBootRevision because the revision string length has increased. This change will maintain compatibility with older revisions.', 'Changed the syntax size for adAOSCurrentImage. The syntax size now includes a range.',))
if mibBuilder.loadTexts: adGenAOSUnitMib.setLastUpdated('200409240000Z')
if mibBuilder.loadTexts: adGenAOSUnitMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSUnitMib.setContactInfo('Technical Support Dept. Postal: ADTRAN, Inc. 901 Explorer Blvd. Huntsville, AL 35806 Tel: +1 800 726-8663 Fax: +1 256 963 6217 E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSUnitMib.setDescription('This MIB contains device information, contact information, and overall system health information.')
adGenAOSUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1))
class Utf8String(TextualConvention, OctetString):
    description = 'To facilitate internationalization, this TC represents information taken from the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 character encoding scheme described in RFC 2044 [10]. For strings in 7-bit US-ASCII, there is no impact since the UTF-8 representation is identical to the US-ASCII encoding.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

adAOSBootRevision = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSBootRevision.setStatus('current')
if mibBuilder.loadTexts: adAOSBootRevision.setDescription('Unit boot PROM revision.')
adAOSCurrentImage = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSCurrentImage.setStatus('current')
if mibBuilder.loadTexts: adAOSCurrentImage.setDescription('Filename for current firmware image.')
adAOSRunConfigChecksum = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSRunConfigChecksum.setStatus('current')
if mibBuilder.loadTexts: adAOSRunConfigChecksum.setDescription('MD5 Digest of the running configuration')
adAOSStartConfigChecksum = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSStartConfigChecksum.setStatus('current')
if mibBuilder.loadTexts: adAOSStartConfigChecksum.setDescription('MD5 Digest of the startup configuration')
adAOSDeviceIndex = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceIndex.setDescription('The unique device identification within the instance of this Mib.')
adAOSDeviceGlobalUniqueID = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 6), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceGlobalUniqueID.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceGlobalUniqueID.setDescription('This represents a globally unique ID for the device. This MUST be the ordered combination of the Manufacturer, product name, AND any other text that is necessary to guarantee global uniqueness. This value may not be null. Could use serial number. e.g. AD123456789')
adAOSDeviceHealth = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("unused", 2), ("ok", 3), ("warning", 4), ("critical", 5), ("nonrecoverable", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceHealth.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceHealth.setDescription('Overall health of the device. The goal of this object is to be the single poll point to check the status of the device.')
adAOSDeviceSysObjID = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 8), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceSysObjID.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceSysObjID.setDescription('System Object ID for this Device entity. This should be an ASCII integer format. (i.e. 1.3.6.1.4.1.11.2.36.1.1) The value may not be null.')
adAOSDeviceManagementURL = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 9), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceManagementURL.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceManagementURL.setDescription("This object contains the URL for the device's management software. If it does not exist the value is empty string. If write is not supported, then return invalid. This value is retained across boots.")
adAOSDeviceManagementURLLabel = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 10), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceManagementURLLabel.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceManagementURLLabel.setDescription("The label that a management application should use for the hyperlink to the entity's URL.")
adAOSDeviceManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 11), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceManufacturer.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceManufacturer.setDescription("The device's manufacturer name. Will return 'ADTRAN' ")
adAOSDeviceProductName = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 12), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceProductName.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceProductName.setDescription("The device's product name. Null is NOT a valid value. (i.e. D1234A)")
adAOSDeviceSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 13), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceSerialNumber.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceSerialNumber.setDescription('The serial number for the device. This can return a NULL string.')
adAOSDeviceVersion = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 14), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceVersion.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceVersion.setDescription('Version number for this device.')
adAOSDeviceHWVersion = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 15), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceHWVersion.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceHWVersion.setDescription("Version number for this device's hardware.")
adAOSDeviceContactPerson = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 16), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactPerson.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceContactPerson.setDescription('Identifies the name of the person responsible for the operation of this device. If write is not supported then return invalid.')
adAOSDeviceContactPhone = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 17), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactPhone.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceContactPhone.setDescription('Phone number of the contact person for this device.')
adAOSDeviceContactEmail = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 18), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactEmail.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceContactEmail.setDescription('e-mail address of the contact person for this device.')
adAOSDeviceContactPagerNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 19), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactPagerNumber.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceContactPagerNumber.setDescription('Pager number of the contact person for this device.')
adAOSDeviceLocation = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 20), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceLocation.setStatus('current')
if mibBuilder.loadTexts: adAOSDeviceLocation.setDescription('Identifies the location for the this device. If write is not supported then return invalid.')
adGenAOSSaveConfig = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("saveconfig", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSSaveConfig.setStatus('current')
if mibBuilder.loadTexts: adGenAOSSaveConfig.setDescription('Set value to 1 to copy running config to startup config.')
adGenAOSReloadSystem = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSReloadSystem.setStatus('current')
if mibBuilder.loadTexts: adGenAOSReloadSystem.setDescription('Set to 0 to initiate immediate system reload. Any non-zero value is the number of seconds until reload')
adGenAOSCancelReload = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("cancelreload", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSCancelReload.setStatus('current')
if mibBuilder.loadTexts: adGenAOSCancelReload.setDescription('Writing any value to this element will cancel a scheduled reload')
adAOSPrimaryImage = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSPrimaryImage.setStatus('current')
if mibBuilder.loadTexts: adAOSPrimaryImage.setDescription('Filename for primary firmware image.')
adAOSBackupImage = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSBackupImage.setStatus('current')
if mibBuilder.loadTexts: adAOSBackupImage.setDescription('Filename for backup firmware image.')
adAOSDevicePartNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 26), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDevicePartNumber.setStatus('current')
if mibBuilder.loadTexts: adAOSDevicePartNumber.setDescription("The device's part number. Null is NOT a valid value. (i.e. 1202860L1)")
adGenAOSUnitConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1))
adAOSUnitCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 1))
adAOSUnitGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 2))
adAOSCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 1, 1)).setObjects(("ADTRAN-AOSUNIT", "adGenAOSUnitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSCompliance = adAOSCompliance.setStatus('current')
if mibBuilder.loadTexts: adAOSCompliance.setDescription('The compliance statement for SNMPv2 entities which implement the AOS Unit MIB.')
adGenAOSUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 2, 1)).setObjects(("ADTRAN-AOSUNIT", "adAOSBootRevision"), ("ADTRAN-AOSUNIT", "adAOSCurrentImage"), ("ADTRAN-AOSUNIT", "adAOSRunConfigChecksum"), ("ADTRAN-AOSUNIT", "adAOSStartConfigChecksum"), ("ADTRAN-AOSUNIT", "adAOSDeviceIndex"), ("ADTRAN-AOSUNIT", "adAOSDeviceGlobalUniqueID"), ("ADTRAN-AOSUNIT", "adAOSDeviceHealth"), ("ADTRAN-AOSUNIT", "adAOSDeviceSysObjID"), ("ADTRAN-AOSUNIT", "adAOSDeviceManagementURL"), ("ADTRAN-AOSUNIT", "adAOSDeviceManufacturer"), ("ADTRAN-AOSUNIT", "adAOSDeviceProductName"), ("ADTRAN-AOSUNIT", "adAOSDeviceSerialNumber"), ("ADTRAN-AOSUNIT", "adAOSDeviceVersion"), ("ADTRAN-AOSUNIT", "adAOSDeviceHWVersion"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactPerson"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactPhone"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactEmail"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactPagerNumber"), ("ADTRAN-AOSUNIT", "adAOSDeviceLocation"), ("ADTRAN-AOSUNIT", "adGenAOSSaveConfig"), ("ADTRAN-AOSUNIT", "adGenAOSReloadSystem"), ("ADTRAN-AOSUNIT", "adGenAOSCancelReload"), ("ADTRAN-AOSUNIT", "adAOSPrimaryImage"), ("ADTRAN-AOSUNIT", "adAOSBackupImage"), ("ADTRAN-AOSUNIT", "adAOSDevicePartNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSUnitGroup = adGenAOSUnitGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSUnitGroup.setDescription('The Unit SNMP Config Group.')
mibBuilder.exportSymbols("ADTRAN-AOSUNIT", adAOSDeviceContactPhone=adAOSDeviceContactPhone, adAOSUnitCompliances=adAOSUnitCompliances, adAOSDeviceManagementURL=adAOSDeviceManagementURL, adGenAOSUnitConformance=adGenAOSUnitConformance, adAOSStartConfigChecksum=adAOSStartConfigChecksum, adGenAOSUnit=adGenAOSUnit, adGenAOSUnitGroup=adGenAOSUnitGroup, adAOSBackupImage=adAOSBackupImage, adAOSCurrentImage=adAOSCurrentImage, PYSNMP_MODULE_ID=adGenAOSUnitMib, adAOSDeviceManagementURLLabel=adAOSDeviceManagementURLLabel, adAOSCompliance=adAOSCompliance, adAOSDevicePartNumber=adAOSDevicePartNumber, adAOSDeviceHWVersion=adAOSDeviceHWVersion, adAOSDeviceSerialNumber=adAOSDeviceSerialNumber, adAOSDeviceIndex=adAOSDeviceIndex, adAOSBootRevision=adAOSBootRevision, adGenAOSSaveConfig=adGenAOSSaveConfig, adAOSDeviceContactPagerNumber=adAOSDeviceContactPagerNumber, adAOSUnitGroups=adAOSUnitGroups, adAOSDeviceSysObjID=adAOSDeviceSysObjID, adAOSDeviceProductName=adAOSDeviceProductName, adGenAOSReloadSystem=adGenAOSReloadSystem, adAOSDeviceHealth=adAOSDeviceHealth, adAOSDeviceVersion=adAOSDeviceVersion, Utf8String=Utf8String, adAOSRunConfigChecksum=adAOSRunConfigChecksum, adAOSDeviceGlobalUniqueID=adAOSDeviceGlobalUniqueID, adAOSDeviceContactPerson=adAOSDeviceContactPerson, adAOSDeviceManufacturer=adAOSDeviceManufacturer, adAOSPrimaryImage=adAOSPrimaryImage, adGenAOSUnitMib=adGenAOSUnitMib, adAOSDeviceLocation=adAOSDeviceLocation, adGenAOSCancelReload=adGenAOSCancelReload, adAOSDeviceContactEmail=adAOSDeviceContactEmail)
