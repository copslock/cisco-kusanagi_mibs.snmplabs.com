#
# PySNMP MIB module CISCO-IMAGE-LICENSE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMAGE-LICENSE-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, iso, TimeTicks, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "TimeTicks", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoImageLicenseMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 640))
ciscoImageLicenseMgmtMIB.setRevisions(('2007-10-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setLastUpdated('200710160000Z')
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoImageLicenseMgmtMIB.setDescription("The MIB module for managing the running image level of a Cisco device. Cisco's licensing mechanism provides flexibility to run a device on a chosen image level. This mechanism is referred to as image level licensing. Image level licensing leverages the universal image based licensing solution. The image level licensing mechanism works as follows - A universal image that contains all levels of software packages is loaded on to the device. At boot time, the device determines the highest level of license and brings up the appropriate software features or subsystems. The user can configure the image level with which the device has to boot. The system will verify whether the appropriate license is available for the configured image level. The image level for the next boot will be determined based on the availability of the license. The following scenarios explains some use-cases of image level licensing: Scenario 1: - Customer selects advsecurityk9 based image. - Manufacturing installs advsecurity license on the device. - This device will run all features that are part of the base advsecurity license. - Customer upgrades to advipservicesk9 license. - The next boot level is set to advipservicesk9. - The device will run advsecurityk9 feature until the next reboot. After reboot the device will run advipservicesk9 features. Scenario 2: - Customer selects advipservicesk9 based image. - Manufacturing installs advipservices and advsecurity license on the device. - This device will run all features that are part of the base advipservices license. - No upgrades available for advipservices license. The user has to accept the End User License Agreement(EULA) before using this MIB to configure the image level. This MIB should be used in conjuntion with CISCO-LICENSE-MGMT-MIB module to achieve the image level licensing functionality. This MIB module defines objects which provides the different image levels supported by the device and the license required to enable a particular image level. It also defines objects to let the user configure the required image level. The MIB module contains notification which will be triggered when the user changes the image level for next boot. The CISCO-LICENSE-MGMT-MIB module should be used to export the EULA and to configure the required license. This MIB module is defined generically so it can be used for both stand-alone as well as stackable devices. The entPhysicalIndex imported from ENTITY-MIB is used to identify the device uniquely.")
ciscoImageLicenseMgmtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 0))
ciscoImageLicenseMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 1))
ciscoImageLicenseMgmtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2))
class BootImageLevel(TextualConvention, OctetString):
    description = "This textual convention is used to define the image level. If the device is running at advipservices image level, then the boot image level will be 'advipservices'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class LicenseNameList(TextualConvention, OctetString):
    description = "This textual convention is used to define the list of license names. If multiple licenses are present then this string will contain all the licenses seperated by the ',' character. If the license required to run a device at advipservices image level is advipservices and advsecurity, then the license name list will be 'advipservices,advsecurity'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

cilmBootImageLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1), )
if mibBuilder.loadTexts: cilmBootImageLevelTable.setStatus('current')
if mibBuilder.loadTexts: cilmBootImageLevelTable.setDescription('A table that contains the configuration information of current and next boot image level. This table contains entries for each software module running in an image loaded in the device. The software module is identified by cilmModuleName and the device is identified by entPhysicalIndex.')
cilmBootImageLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"))
if mibBuilder.loadTexts: cilmBootImageLevelEntry.setStatus('current')
if mibBuilder.loadTexts: cilmBootImageLevelEntry.setDescription('An entry in the table for each module containing the list of objects that define the configuration of next boot level. The following information is specified by the objects present in the table. - Current image level. - Configured image level for the next boot. - Actual image level for the next boot. - License store index for the current license. - License index of the current license. - License store index for the next boot license. - License index of the next boot license.')
cilmModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: cilmModuleName.setStatus('current')
if mibBuilder.loadTexts: cilmModuleName.setDescription('This object is used as one of the two indices in cilmBootImageLevelTable. This object indicates the module name of the software package. There can be multiple modules in an image performing specific functionality. For example, in a wireless image there can be two modules - a base image module and a wireless module.')
cilmCurrentImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 2), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentImageLevel.setStatus('current')
if mibBuilder.loadTexts: cilmCurrentImageLevel.setDescription('This object indicates the current image level that the module is running.')
cilmConfiguredBootImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 3), BootImageLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmConfiguredBootImageLevel.setStatus('current')
if mibBuilder.loadTexts: cilmConfiguredBootImageLevel.setDescription('This object indicates the configured image level of the module for the next boot. Note: The configured next boot image level may not be the actual next boot image level. The actual next boot image level is denoted by cilmNextBootImageLevel which is determined based on the license availability.')
cilmNextBootImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 4), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootImageLevel.setStatus('current')
if mibBuilder.loadTexts: cilmNextBootImageLevel.setDescription('This object indicates the next boot image level. The next boot image level can be different from configured level. The next boot image level is determined based on the availability of required license.')
cilmCurrentLicenseStoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentLicenseStoreIndex.setStatus('current')
if mibBuilder.loadTexts: cilmCurrentLicenseStoreIndex.setDescription("This object indicates the license store index where the currently used license is stored. This object has the same value as clmgmtLicenseStoreIndex object and uniquely identifies an entry in clmgmtLicenseStoreInfoTable in CISCO-LICENSE-MGMT-MIB. Note: The license store index can be '0' if no license is installed and device is running base image.")
cilmCurrentLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmCurrentLicenseIndex.setStatus('current')
if mibBuilder.loadTexts: cilmCurrentLicenseIndex.setDescription("This object indicates the license index of the currently used license. This object has the same value as clmgmtLicenseIndex and uniquely identifies an entry in clmgmtLicenseInfoTable in CISCO-LICENSE-MGMT-MIB. Note: The license index can be '0' if no license is installed and device is running base image.")
cilmNextBootLicenseStoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootLicenseStoreIndex.setStatus('current')
if mibBuilder.loadTexts: cilmNextBootLicenseStoreIndex.setDescription("This object indicates the license store index where the next boot license is stored. This object has the same value as clmgmtLicenseStoreIndex object and uniquely identifies an entry in clmgmtLicenseStoreInfoTable in CISCO-LICENSE-MGMT-MIB. Note: The license store index can be '0' if no license is installed for the next boot.")
cilmNextBootLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmNextBootLicenseIndex.setStatus('current')
if mibBuilder.loadTexts: cilmNextBootLicenseIndex.setDescription("This object indicates the license index of the next boot license. This object has the same value as clmgmtLicenseIndex and uniquely identifies an entry in clmgmtLicenseInfoTable in CISCO-LICENSE-MGMT-MIB. Note: The license index can be '0' if no license is installed for the next boot.")
cilmImageLevelToLicenseMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2), )
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapTable.setStatus('current')
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapTable.setDescription('This table contains the mapping between different image levels of each modules in the image and the license required to run the modules at a particular image level. This table can be used to identify the different image levels and the appropriate licenses required for each.')
cilmImageLevelToLicenseMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmModuleName"), (0, "CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseMapIndex"))
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapEntry.setStatus('current')
if mibBuilder.loadTexts: cilmImageLevelToLicenseMapEntry.setDescription('An entry in the table containing the following information. - The image levels at the which the modules can be run. - The license required to the run a module at a particular image level. - The priority of the license.')
cilmImageLicenseMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cilmImageLicenseMapIndex.setStatus('current')
if mibBuilder.loadTexts: cilmImageLicenseMapIndex.setDescription('This is a running index used to identify an entry of this table.')
cilmImageLicenseImageLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 2), BootImageLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicenseImageLevel.setStatus('current')
if mibBuilder.loadTexts: cilmImageLicenseImageLevel.setDescription('This object indicates the image level at which a module can be run. A module can be run at different image levels. An entry will be created in this table for every module and image level combination.')
cilmImageLicenseName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 3), LicenseNameList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicenseName.setStatus('current')
if mibBuilder.loadTexts: cilmImageLicenseName.setDescription('This object indicates the list of licenses needed to be installed for the module to run at the image level mentioned by cilmImageLicenseImageLevel object of this entry.')
cilmImageLicensePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cilmImageLicensePriority.setStatus('current')
if mibBuilder.loadTexts: cilmImageLicensePriority.setDescription('This object indicates the priority of the image level mentioned by cilmImageLicenseImageLevel object of this entry. The image level with the highest priority license will be considered as the default level in the absense of next boot image level configuration. For example if there are three licenses l1, l2 and l3 in the ascending order of priority, then by default l1 will be the level at which the module will be running. If the next boot level is configured then the configuration will override the priority. The highest priority license supports a feature set which is a super set of all other licenses.')
cilmEULAAccepted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmEULAAccepted.setStatus('current')
if mibBuilder.loadTexts: cilmEULAAccepted.setDescription('This object when set to TRUE means that the user has accepted the END USER LICENSE AGREEMENT. This object has to be set to TRUE by the user before using the objects in the cilmBootImageLevelTable to configure the license.')
cilmNotifCntl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4))
cilmImageLevelChangedNotif = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 640, 1, 4, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cilmImageLevelChangedNotif.setReference('See also RFC3413 for explanation that notifications are under the ultimate control of the MIB module in this document.')
if mibBuilder.loadTexts: cilmImageLevelChangedNotif.setStatus('current')
if mibBuilder.loadTexts: cilmImageLevelChangedNotif.setDescription('Specify whether or not a notification should be generated on the detection of change in next boot image level. If set to TRUE, cilmBootImageLevelChanged notification will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered.')
cilmBootImageLevelChanged = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 640, 0, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"))
if mibBuilder.loadTexts: cilmBootImageLevelChanged.setStatus('current')
if mibBuilder.loadTexts: cilmBootImageLevelChanged.setDescription('This notification is triggered when next boot image level is changed in the management entity. The current and configured image level are indicated by cilmCurrentImageLevel and cilmConfiguredBootImageLevel objects respectively.')
cilmModuleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1))
cilmModuleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2))
cilmModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 1, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmAdminGroup"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNotifGroup"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmOperGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmModuleCompliance = cilmModuleCompliance.setStatus('current')
if mibBuilder.loadTexts: cilmModuleCompliance.setDescription('Compliance statement for Cisco Image level license mgmt MIB.')
cilmAdminGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 1)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmConfiguredBootImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseStoreIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmCurrentLicenseIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseStoreIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmNextBootLicenseIndex"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmEULAAccepted"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLevelChangedNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmAdminGroup = cilmAdminGroup.setStatus('current')
if mibBuilder.loadTexts: cilmAdminGroup.setDescription('Objects for performing license set operation for setting next boot level.')
cilmOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 2)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseImageLevel"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicenseName"), ("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmImageLicensePriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmOperGroup = cilmOperGroup.setStatus('current')
if mibBuilder.loadTexts: cilmOperGroup.setDescription('Objects for getting current image level configuration data.')
cilmNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 640, 2, 2, 3)).setObjects(("CISCO-IMAGE-LICENSE-MGMT-MIB", "cilmBootImageLevelChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilmNotifGroup = cilmNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cilmNotifGroup.setDescription('Objects for getting current image level configuration data.')
mibBuilder.exportSymbols("CISCO-IMAGE-LICENSE-MGMT-MIB", cilmCurrentImageLevel=cilmCurrentImageLevel, cilmCurrentLicenseStoreIndex=cilmCurrentLicenseStoreIndex, cilmAdminGroup=cilmAdminGroup, cilmEULAAccepted=cilmEULAAccepted, cilmImageLicenseImageLevel=cilmImageLicenseImageLevel, cilmBootImageLevelChanged=cilmBootImageLevelChanged, cilmNotifGroup=cilmNotifGroup, cilmBootImageLevelEntry=cilmBootImageLevelEntry, cilmConfiguredBootImageLevel=cilmConfiguredBootImageLevel, BootImageLevel=BootImageLevel, cilmImageLevelChangedNotif=cilmImageLevelChangedNotif, cilmModuleGroups=cilmModuleGroups, cilmBootImageLevelTable=cilmBootImageLevelTable, ciscoImageLicenseMgmtMIBObjects=ciscoImageLicenseMgmtMIBObjects, cilmModuleName=cilmModuleName, cilmImageLicensePriority=cilmImageLicensePriority, cilmNextBootImageLevel=cilmNextBootImageLevel, cilmImageLevelToLicenseMapEntry=cilmImageLevelToLicenseMapEntry, PYSNMP_MODULE_ID=ciscoImageLicenseMgmtMIB, cilmNextBootLicenseIndex=cilmNextBootLicenseIndex, ciscoImageLicenseMgmtMIBConform=ciscoImageLicenseMgmtMIBConform, cilmImageLicenseMapIndex=cilmImageLicenseMapIndex, cilmModuleCompliance=cilmModuleCompliance, ciscoImageLicenseMgmtMIB=ciscoImageLicenseMgmtMIB, ciscoImageLicenseMgmtMIBNotifs=ciscoImageLicenseMgmtMIBNotifs, cilmImageLicenseName=cilmImageLicenseName, cilmNotifCntl=cilmNotifCntl, cilmModuleCompliances=cilmModuleCompliances, cilmCurrentLicenseIndex=cilmCurrentLicenseIndex, cilmImageLevelToLicenseMapTable=cilmImageLevelToLicenseMapTable, cilmOperGroup=cilmOperGroup, cilmNextBootLicenseStoreIndex=cilmNextBootLicenseStoreIndex, LicenseNameList=LicenseNameList)
