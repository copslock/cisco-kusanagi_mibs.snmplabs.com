#
# PySNMP MIB module INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
chassis, = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassis")
groups, regModule = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "groups", "regModule")
FaultLedStates, Power, PowerLedStates, Presence, IdromBinary16, PresenceLedStates, Index = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-TC", "FaultLedStates", "Power", "PowerLedStates", "Presence", "IdromBinary16", "PresenceLedStates", "Index")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, IpAddress, Bits, TimeTicks, Integer32, iso, Counter32, ObjectIdentity, NotificationType, MibIdentifier, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Bits", "TimeTicks", "Integer32", "iso", "Counter32", "ObjectIdentity", "NotificationType", "MibIdentifier", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
multiFlexServerCmmMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 11))
multiFlexServerCmmMibModule.setRevisions(('2007-08-16 13:30', '2007-07-11 12:30', '2007-06-07 20:30', '2007-06-07 13:30', '2007-05-29 20:00', '2007-05-09 11:30', '2007-04-09 10:30', '2007-03-12 18:00', '2007-03-06 10:30', '2007-02-22 17:00', '2006-11-07 07:01', '2006-09-29 15:29',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: multiFlexServerCmmMibModule.setRevisionsDescriptions(('Reordered Revision to reverse chronological as some browsers choke, cleaned up some other simple nit-picky errors', 'Dropped cmmSoftwareVersion as it is superfluous (currently the same as the firmwareBundleID). Dropped cmmBmcVersion as there is no BMC version.', 'Added the IdromBinary16 to represent the asset tag, part number, and serial number fields within the IDROM fields.', 'Corrected maximum/nominal IDROM parameters and comments', 'Moved presence to first column passed index to be consistent with other tables', 'Dropped support for the GUEL as it will be accessible directly via the web', 'Renamed cmmFirmwareVersion to cmmBmcFirmwareVersion to clarify which firmware', 'Moved FirmwareBundleId from chassis to CMM Tree. cmmTable data now complies with IDROM (DID/DSD) information. Added cmmPowerLedStates, cmmFaultLedStates, & cmmPresenceLedStates to cmmTable. Added ebfFirmwareVersion. Added cmmFirmwareVersion. Renumbered / reorganized accordingly', "Changed Mask representation from an Opaque to a DisplayString at the request of the architects such that it now is an ASCII representation of bit string reflecting the presence with the left most 'bit' being bit 1 and max* bits being represented.", 'Renamed MIB file and updated internal relevance to formal product name Multi-Flex Server', "Consolidated use of Presence datatype and changed 'theChassis' to 'chassis'", "Partitioned off and created as it's own module",))
if mibBuilder.loadTexts: multiFlexServerCmmMibModule.setLastUpdated('200708161330Z')
if mibBuilder.loadTexts: multiFlexServerCmmMibModule.setOrganization('Intel Corporation')
if mibBuilder.loadTexts: multiFlexServerCmmMibModule.setContactInfo('Brian Kurle Intel Corporation JF5-2-C3 Tel: 503-712-5032 E-Mail: brianx.j.kurle@intel.com')
if mibBuilder.loadTexts: multiFlexServerCmmMibModule.setDescription('CMM Module of the Multi-Flex Server')
maxCmms = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxCmms.setStatus('current')
if mibBuilder.loadTexts: maxCmms.setDescription('Maximum number of CMMs possible in this chassis.')
numOfCmms = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numOfCmms.setStatus('current')
if mibBuilder.loadTexts: numOfCmms.setDescription("The number of CMMs in the system. This is a bit of overkill as the first version doesn't have more than one CMM, but as there is talk of future revisions containing a second, this is designed in to be consistent with the other modules.")
cmmPresenceMask = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmPresenceMask.setStatus('current')
if mibBuilder.loadTexts: cmmPresenceMask.setDescription("ASCII representation of bit string reflecting the presence of the CMMs with the left most 'bit' being bit 1 and maxCmms bits being represented. Thus, '1' would express that CMM 1 (of the only one CMM) is present")
cmms = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201))
if mibBuilder.loadTexts: cmms.setStatus('current')
if mibBuilder.loadTexts: cmms.setDescription('Container for CMM specific information as well as all components logically contained within.')
firmwareBundleId = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareBundleId.setStatus('current')
if mibBuilder.loadTexts: firmwareBundleId.setDescription('Firmware bundle identification (Tag of all firmware/software versions on all FRUs)')
cmmTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2), )
if mibBuilder.loadTexts: cmmTable.setStatus('current')
if mibBuilder.loadTexts: cmmTable.setDescription('Each row describes a CMM in the chassis')
cmmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmIndex"))
if mibBuilder.loadTexts: cmmEntry.setStatus('current')
if mibBuilder.loadTexts: cmmEntry.setDescription('..')
cmmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 1), Index()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIndex.setStatus('current')
if mibBuilder.loadTexts: cmmIndex.setDescription('column used to identify a particular CMM.')
cmmPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 2), Presence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmPresence.setStatus('current')
if mibBuilder.loadTexts: cmmPresence.setDescription('Flag whether this CMM is present (forward thinking for future products that will contain redundant CMMs)')
cmmVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmVendor.setStatus('current')
if mibBuilder.loadTexts: cmmVendor.setDescription('Device manufacturer')
cmmMfgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmMfgDate.setStatus('current')
if mibBuilder.loadTexts: cmmMfgDate.setDescription('Manufacture date/time')
cmmDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmDeviceName.setStatus('current')
if mibBuilder.loadTexts: cmmDeviceName.setDescription('Device Name')
cmmPart = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 6), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmPart.setStatus('current')
if mibBuilder.loadTexts: cmmPart.setDescription('Device Part Number')
cmmSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 7), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmSerialNo.setStatus('current')
if mibBuilder.loadTexts: cmmSerialNo.setDescription('Device Serial Number')
cmmMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 8), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmMaximumPower.setStatus('current')
if mibBuilder.loadTexts: cmmMaximumPower.setDescription('Static maximum power generation / consumption (in watts): <0 - Negative numbers indicate device consumes power (in watts) >0 - Positive numbers indicate device generates power (in watts) 0 - Device is passive (does not not consume or generate power) -1 - Maximum power generation/consumption not known or specified')
cmmNominalPower = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 9), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmNominalPower.setStatus('current')
if mibBuilder.loadTexts: cmmNominalPower.setDescription('Static Nominal power generation / consumption (in watts): <0 - Negative numbers indicate device consumes power (in watts) >0 - Positive numbers indicate device generates power (in watts) 0 - Device is passive (does not not consume or generate power) -1 - Nominal power generation/consumption not known or specified')
cmmAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 10), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmAssetTag.setStatus('current')
if mibBuilder.loadTexts: cmmAssetTag.setDescription('Asset Tag # of device')
cmmExternalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 11), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmExternalMac.setStatus('current')
if mibBuilder.loadTexts: cmmExternalMac.setDescription('MAC Address of external (front panel) Ethernet interface')
cmmChassisMac = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 12), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmChassisMac.setStatus('current')
if mibBuilder.loadTexts: cmmChassisMac.setDescription('MAC Address of internal (chassis) Ethernet interface')
cmmPowerLed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 13), PowerLedStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmPowerLed.setStatus('current')
if mibBuilder.loadTexts: cmmPowerLed.setDescription('State of the Power LED on the CMM')
cmmFaultLed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 14), FaultLedStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmFaultLed.setStatus('current')
if mibBuilder.loadTexts: cmmFaultLed.setDescription('State of the Fault LED on the CMM')
cmmPresenceLed = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 15), PresenceLedStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmPresenceLed.setStatus('current')
if mibBuilder.loadTexts: cmmPresenceLed.setDescription('State of the Presence LED on the CMM (and optionally intiate identification)')
cmmEbfFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmEbfFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: cmmEbfFirmwareVersion.setDescription('Firmware version of the EBF')
cmmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 11)).setObjects(("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "maxCmms"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "numOfCmms"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPresenceMask"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "firmwareBundleId"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmIndex"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPresence"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmVendor"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmMfgDate"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmDeviceName"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPart"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmSerialNo"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmMaximumPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmNominalPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmAssetTag"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmExternalMac"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmChassisMac"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPowerLed"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmFaultLed"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPresenceLed"), ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmEbfFirmwareVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmGroup = cmmGroup.setStatus('current')
if mibBuilder.loadTexts: cmmGroup.setDescription('Description.')
mibBuilder.exportSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", cmmMfgDate=cmmMfgDate, cmmPresenceLed=cmmPresenceLed, cmmIndex=cmmIndex, cmmTable=cmmTable, multiFlexServerCmmMibModule=multiFlexServerCmmMibModule, cmmPart=cmmPart, cmmDeviceName=cmmDeviceName, cmmChassisMac=cmmChassisMac, cmmPowerLed=cmmPowerLed, cmmVendor=cmmVendor, cmmGroup=cmmGroup, cmmPresenceMask=cmmPresenceMask, cmmMaximumPower=cmmMaximumPower, cmmEbfFirmwareVersion=cmmEbfFirmwareVersion, maxCmms=maxCmms, cmmSerialNo=cmmSerialNo, cmmFaultLed=cmmFaultLed, cmmExternalMac=cmmExternalMac, PYSNMP_MODULE_ID=multiFlexServerCmmMibModule, firmwareBundleId=firmwareBundleId, cmms=cmms, cmmNominalPower=cmmNominalPower, cmmAssetTag=cmmAssetTag, numOfCmms=numOfCmms, cmmEntry=cmmEntry, cmmPresence=cmmPresence)
