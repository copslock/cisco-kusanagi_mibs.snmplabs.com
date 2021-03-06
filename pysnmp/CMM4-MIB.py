#
# PySNMP MIB module CMM4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CMM4-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Bits, ObjectIdentity, iso, Integer32, MibIdentifier, Counter64, ModuleIdentity, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Bits", "ObjectIdentity", "iso", "Integer32", "MibIdentifier", "Counter64", "ModuleIdentity", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
whispBox, whispCMM4, whispModules = mibBuilder.importSymbols("WHISP-GLOBAL-REG-MIB", "whispBox", "whispCMM4", "whispModules")
EventString, WhispLUID, WhispMACAddress = mibBuilder.importSymbols("WHISP-TCV2-MIB", "EventString", "WhispLUID", "WhispMACAddress")
cmm4MibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 15))
if mibBuilder.loadTexts: cmm4MibModule.setLastUpdated('200603290000Z')
if mibBuilder.loadTexts: cmm4MibModule.setOrganization('Cambium Networks')
cmm4Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1))
cmm4Config = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2))
cmm4Status = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3))
cmm4Gps = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4))
cmm4EventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 5))
cmm4Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6))
cmm4Snmp = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7))
cmm4Event = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8))
cmm4GPSEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8, 1))
cmm4PortCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 1)).setObjects(("CMM4-MIB", "portCfgIndex"), ("CMM4-MIB", "cmm4PortText"), ("CMM4-MIB", "cmm4PortDevType"), ("CMM4-MIB", "cmm4PortPowerCfg"), ("CMM4-MIB", "cmm4PortResetCfg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4PortCfgGroup = cmm4PortCfgGroup.setStatus('current')
cmm4ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 2)).setObjects(("CMM4-MIB", "gpsTimingPulse"), ("CMM4-MIB", "lan1Ip"), ("CMM4-MIB", "lan1SubnetMask"), ("CMM4-MIB", "defaultGateway"), ("CMM4-MIB", "cmm4WebAutoUpdate"), ("CMM4-MIB", "cmm4ExtEthPowerReset"), ("CMM4-MIB", "cmm4IpAccessFilter"), ("CMM4-MIB", "cmm4IpAccess1"), ("CMM4-MIB", "cmm4IpAccess2"), ("CMM4-MIB", "cmm4IpAccess3"), ("CMM4-MIB", "cmm4MgmtPortSpeed"), ("CMM4-MIB", "cmm4NTPServerIp"), ("CMM4-MIB", "sessionTimeout"), ("CMM4-MIB", "vlanEnable"), ("CMM4-MIB", "managementVID"), ("CMM4-MIB", "siteInfoViewable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4ConfigGroup = cmm4ConfigGroup.setStatus('current')
cmm4PortStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 3)).setObjects(("CMM4-MIB", "portStatusIndex"), ("CMM4-MIB", "cmm4PortPowerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4PortStatusGroup = cmm4PortStatusGroup.setStatus('current')
cmm4StatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 4)).setObjects(("CMM4-MIB", "deviceType"), ("CMM4-MIB", "cmm4pldVersion"), ("CMM4-MIB", "cmm4SoftwareVersion"), ("CMM4-MIB", "cmm4SystemTime"), ("CMM4-MIB", "cmm4UpTime"), ("CMM4-MIB", "satellitesVisible"), ("CMM4-MIB", "satellitesTracked"), ("CMM4-MIB", "latitude"), ("CMM4-MIB", "longitude"), ("CMM4-MIB", "height"), ("CMM4-MIB", "trackingMode"), ("CMM4-MIB", "syncStatus"), ("CMM4-MIB", "cmm4MacAddress"), ("CMM4-MIB", "cmm4ExtEthPwrStat"), ("CMM4-MIB", "cmm4FPGAVersion"), ("CMM4-MIB", "cmm4FPGAPlatform"), ("CMM4-MIB", "defaultStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4StatusGroup = cmm4StatusGroup.setStatus('current')
cmm4GPSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 5)).setObjects(("CMM4-MIB", "gpsTrackingMode"), ("CMM4-MIB", "gpsTime"), ("CMM4-MIB", "gpsDate"), ("CMM4-MIB", "gpsSatellitesVisible"), ("CMM4-MIB", "gpsSatellitesTracked"), ("CMM4-MIB", "gpsHeight"), ("CMM4-MIB", "gpsAntennaConnection"), ("CMM4-MIB", "gpsLatitude"), ("CMM4-MIB", "gpsLongitude"), ("CMM4-MIB", "gpsInvalidMsg"), ("CMM4-MIB", "gpsRestartCount"), ("CMM4-MIB", "gpsReceiverInfo"), ("CMM4-MIB", "gpsSyncStatus"), ("CMM4-MIB", "gpsSyncMasterSlave"), ("CMM4-MIB", "gpsLog"), ("CMM4-MIB", "gpsReInitCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4GPSGroup = cmm4GPSGroup.setStatus('current')
cmm4ControlsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 6)).setObjects(("CMM4-MIB", "cmm4Reboot"), ("CMM4-MIB", "cmm4ClearEventLog"), ("CMM4-MIB", "cmm4RebootIfRequired"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4ControlsGroup = cmm4ControlsGroup.setStatus('current')
cmm4SNMPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 7)).setObjects(("CMM4-MIB", "cmm4SnmpComString"), ("CMM4-MIB", "cmm4SnmpAccessSubnet"), ("CMM4-MIB", "cmm4SnmpTrapIp1"), ("CMM4-MIB", "cmm4SnmpTrapIp2"), ("CMM4-MIB", "cmm4SnmpTrapIp3"), ("CMM4-MIB", "cmm4SnmpTrapIp4"), ("CMM4-MIB", "cmm4SnmpTrapIp5"), ("CMM4-MIB", "cmm4SnmpTrapIp6"), ("CMM4-MIB", "cmm4SnmpTrapIp7"), ("CMM4-MIB", "cmm4SnmpTrapIp8"), ("CMM4-MIB", "cmm4SnmpTrapIp9"), ("CMM4-MIB", "cmm4SnmpTrapIp10"), ("CMM4-MIB", "cmm4SnmpReadOnly"), ("CMM4-MIB", "cmm4SnmpGPSSyncTrapEnable"), ("CMM4-MIB", "cmm4SnmpAccessSubnet2"), ("CMM4-MIB", "cmm4SnmpAccessSubnet3"), ("CMM4-MIB", "cmm4SnmpAccessSubnet4"), ("CMM4-MIB", "cmm4SnmpAccessSubnet5"), ("CMM4-MIB", "cmm4SnmpAccessSubnet6"), ("CMM4-MIB", "cmm4SnmpAccessSubnet7"), ("CMM4-MIB", "cmm4SnmpAccessSubnet8"), ("CMM4-MIB", "cmm4SnmpAccessSubnet9"), ("CMM4-MIB", "cmm4SnmpAccessSubnet10"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4SNMPGroup = cmm4SNMPGroup.setStatus('current')
cmm4UserTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 1, 8)).setObjects(("CMM4-MIB", "entryIndex"), ("CMM4-MIB", "userLoginName"), ("CMM4-MIB", "userPswd"), ("CMM4-MIB", "accessLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmm4UserTableGroup = cmm4UserTableGroup.setStatus('current')
gpsTimingPulse = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("master", 1), ("slave", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gpsTimingPulse.setStatus('current')
lan1Ip = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan1Ip.setStatus('current')
lan1SubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan1SubnetMask.setStatus('current')
defaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: defaultGateway.setStatus('current')
cmm4WebAutoUpdate = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 5), Integer32()).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4WebAutoUpdate.setStatus('current')
cmm4ExtEthPowerReset = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4ExtEthPowerReset.setStatus('current')
cmm4IpAccessFilter = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4IpAccessFilter.setStatus('current')
cmm4IpAccess1 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4IpAccess1.setStatus('current')
cmm4IpAccess2 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4IpAccess2.setStatus('current')
cmm4IpAccess3 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4IpAccess3.setStatus('current')
cmm4MgmtPortSpeed = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("autoNegotiate", 1), ("force10Half", 2), ("force10Full", 3), ("force100Half", 4), ("force100Full", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4MgmtPortSpeed.setStatus('current')
cmm4NTPServerIp = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4NTPServerIp.setStatus('current')
sessionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionTimeout.setStatus('current')
vlanEnable = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanEnable.setStatus('current')
managementVID = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementVID.setStatus('current')
siteInfoViewable = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: siteInfoViewable.setStatus('current')
cmm4PortCfgTable = MibTable((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7), )
if mibBuilder.loadTexts: cmm4PortCfgTable.setStatus('current')
cmm4PortCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1), ).setIndexNames((0, "CMM4-MIB", "portCfgIndex"))
if mibBuilder.loadTexts: cmm4PortCfgEntry.setStatus('current')
portCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCfgIndex.setStatus('current')
cmm4PortText = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4PortText.setStatus('current')
cmm4PortDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("canopy", 1), ("canopy56V", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4PortDevType.setStatus('current')
cmm4PortPowerCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("on", 1), ("off", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4PortPowerCfg.setStatus('current')
cmm4PortResetCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 2, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("resetPort", 1), ("resetComplete", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4PortResetCfg.setStatus('current')
deviceType = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('current')
cmm4pldVersion = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4pldVersion.setStatus('current')
cmm4SoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4SoftwareVersion.setStatus('current')
cmm4SystemTime = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4SystemTime.setStatus('current')
cmm4UpTime = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4UpTime.setStatus('current')
satellitesVisible = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satellitesVisible.setStatus('current')
satellitesTracked = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satellitesTracked.setStatus('current')
latitude = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: latitude.setStatus('current')
longitude = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: longitude.setStatus('current')
height = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: height.setStatus('current')
trackingMode = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trackingMode.setStatus('current')
syncStatus = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncStatus.setStatus('current')
cmm4MacAddress = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 14), WhispMACAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4MacAddress.setStatus('current')
cmm4ExtEthPwrStat = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4ExtEthPwrStat.setStatus('current')
cmm4FPGAVersion = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4FPGAVersion.setStatus('current')
cmm4FPGAPlatform = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4FPGAPlatform.setStatus('current')
defaultStatus = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("defaultPlugInserted", 1), ("defaultSwitchActive", 2), ("defaultPlugInsertedAndDefaultSwitchActive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: defaultStatus.setStatus('current')
cmm4PortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1), )
if mibBuilder.loadTexts: cmm4PortStatusTable.setStatus('current')
cmm4PortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1, 1), ).setIndexNames((0, "CMM4-MIB", "portStatusIndex"))
if mibBuilder.loadTexts: cmm4PortStatusEntry.setStatus('current')
portStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portStatusIndex.setStatus('current')
cmm4PortPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, -1))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("powerOverEthernetFault", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmm4PortPowerStatus.setStatus('current')
gpsTrackingMode = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsTrackingMode.setStatus('current')
gpsTime = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsTime.setStatus('current')
gpsDate = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsDate.setStatus('current')
gpsSatellitesVisible = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsSatellitesVisible.setStatus('current')
gpsSatellitesTracked = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsSatellitesTracked.setStatus('current')
gpsHeight = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsHeight.setStatus('current')
gpsAntennaConnection = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsAntennaConnection.setStatus('current')
gpsLatitude = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsLatitude.setStatus('current')
gpsLongitude = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsLongitude.setStatus('current')
gpsInvalidMsg = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsInvalidMsg.setStatus('current')
gpsRestartCount = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsRestartCount.setStatus('current')
gpsReceiverInfo = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsReceiverInfo.setStatus('current')
gpsSyncStatus = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("syncOK", 1), ("noSync", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsSyncStatus.setStatus('current')
gpsSyncMasterSlave = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("cmmIsGPSMaster", 1), ("cmmIsGPSSlave", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsSyncMasterSlave.setStatus('current')
gpsLog = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 15), EventString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsLog.setStatus('current')
gpsReInitCount = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 4, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsReInitCount.setStatus('current')
eventLog = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 5, 1), EventString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLog.setStatus('current')
ntpLog = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 5, 2), EventString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpLog.setStatus('current')
cmm4Reboot = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("reboot", 1), ("finishedReboot", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4Reboot.setStatus('current')
cmm4ClearEventLog = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("clear", 1), ("notClear", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4ClearEventLog.setStatus('current')
cmm4RebootIfRequired = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("rebootifrquired", 1), ("rebootcomplete", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4RebootIfRequired.setStatus('current')
cmm4SnmpComString = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpComString.setStatus('current')
cmm4SnmpAccessSubnet = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet.setStatus('current')
cmm4SnmpTrapIp1 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp1.setStatus('current')
cmm4SnmpTrapIp2 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp2.setStatus('current')
cmm4SnmpTrapIp3 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp3.setStatus('current')
cmm4SnmpTrapIp4 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp4.setStatus('current')
cmm4SnmpTrapIp5 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp5.setStatus('current')
cmm4SnmpTrapIp6 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp6.setStatus('current')
cmm4SnmpTrapIp7 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp7.setStatus('current')
cmm4SnmpTrapIp8 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp8.setStatus('current')
cmm4SnmpTrapIp9 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp9.setStatus('current')
cmm4SnmpTrapIp10 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpTrapIp10.setStatus('current')
cmm4SnmpReadOnly = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("readOnlyPermissions", 1), ("readWritePermissions", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpReadOnly.setStatus('current')
cmm4SnmpGPSSyncTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("gpsSyncTrapDisabled", 0), ("gpsSyncTrapEnabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpGPSSyncTrapEnable.setStatus('current')
cmm4SnmpAccessSubnet2 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet2.setStatus('current')
cmm4SnmpAccessSubnet3 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet3.setStatus('current')
cmm4SnmpAccessSubnet4 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet4.setStatus('current')
cmm4SnmpAccessSubnet5 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet5.setStatus('current')
cmm4SnmpAccessSubnet6 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 19), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet6.setStatus('current')
cmm4SnmpAccessSubnet7 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 20), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet7.setStatus('current')
cmm4SnmpAccessSubnet8 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 21), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet8.setStatus('current')
cmm4SnmpAccessSubnet9 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 22), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet9.setStatus('current')
cmm4SnmpAccessSubnet10 = MibScalar((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 7, 23), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmm4SnmpAccessSubnet10.setStatus('current')
cmm4GPSInSync = NotificationType((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8, 1, 1)).setObjects(("CMM4-MIB", "gpsSyncStatus"), ("CMM4-MIB", "cmm4MacAddress"))
if mibBuilder.loadTexts: cmm4GPSInSync.setStatus('current')
cmm4GPSNoSync = NotificationType((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 8, 1, 2)).setObjects(("CMM4-MIB", "gpsSyncStatus"), ("CMM4-MIB", "cmm4MacAddress"))
if mibBuilder.loadTexts: cmm4GPSNoSync.setStatus('current')
cmm4UserTable = MibTable((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9), )
if mibBuilder.loadTexts: cmm4UserTable.setStatus('current')
cmm4UserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1), ).setIndexNames((0, "CMM4-MIB", "entryIndex"))
if mibBuilder.loadTexts: cmm4UserEntry.setStatus('current')
entryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entryIndex.setStatus('current')
userLoginName = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userLoginName.setStatus('current')
userPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userPswd.setStatus('current')
accessLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 161, 19, 3, 6, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAdmin", 0), ("guest", 1), ("installer", 2), ("administrator", 3), ("technician", 4), ("engineering", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessLevel.setStatus('current')
mibBuilder.exportSymbols("CMM4-MIB", cmm4SystemTime=cmm4SystemTime, cmm4SnmpAccessSubnet10=cmm4SnmpAccessSubnet10, cmm4IpAccess1=cmm4IpAccess1, gpsSatellitesVisible=gpsSatellitesVisible, gpsTimingPulse=gpsTimingPulse, cmm4ClearEventLog=cmm4ClearEventLog, lan1Ip=lan1Ip, cmm4PortText=cmm4PortText, cmm4ExtEthPowerReset=cmm4ExtEthPowerReset, cmm4PortCfgEntry=cmm4PortCfgEntry, cmm4PortCfgTable=cmm4PortCfgTable, cmm4NTPServerIp=cmm4NTPServerIp, cmm4SnmpTrapIp4=cmm4SnmpTrapIp4, cmm4SnmpAccessSubnet7=cmm4SnmpAccessSubnet7, cmm4PortPowerCfg=cmm4PortPowerCfg, cmm4StatusGroup=cmm4StatusGroup, cmm4RebootIfRequired=cmm4RebootIfRequired, cmm4IpAccess2=cmm4IpAccess2, gpsRestartCount=gpsRestartCount, cmm4IpAccessFilter=cmm4IpAccessFilter, gpsInvalidMsg=gpsInvalidMsg, PYSNMP_MODULE_ID=cmm4MibModule, cmm4PortCfgGroup=cmm4PortCfgGroup, cmm4GPSNoSync=cmm4GPSNoSync, cmm4SnmpAccessSubnet=cmm4SnmpAccessSubnet, gpsHeight=gpsHeight, cmm4SnmpComString=cmm4SnmpComString, cmm4Controls=cmm4Controls, cmm4ConfigGroup=cmm4ConfigGroup, cmm4SnmpAccessSubnet3=cmm4SnmpAccessSubnet3, trackingMode=trackingMode, cmm4PortStatusGroup=cmm4PortStatusGroup, cmm4FPGAVersion=cmm4FPGAVersion, cmm4MacAddress=cmm4MacAddress, cmm4SnmpTrapIp8=cmm4SnmpTrapIp8, cmm4IpAccess3=cmm4IpAccess3, defaultStatus=defaultStatus, deviceType=deviceType, cmm4GPSInSync=cmm4GPSInSync, sessionTimeout=sessionTimeout, gpsLongitude=gpsLongitude, cmm4Snmp=cmm4Snmp, height=height, cmm4GPSGroup=cmm4GPSGroup, cmm4SnmpTrapIp10=cmm4SnmpTrapIp10, cmm4SnmpAccessSubnet5=cmm4SnmpAccessSubnet5, portStatusIndex=portStatusIndex, userPswd=userPswd, siteInfoViewable=siteInfoViewable, gpsLatitude=gpsLatitude, cmm4UserEntry=cmm4UserEntry, cmm4pldVersion=cmm4pldVersion, cmm4PortDevType=cmm4PortDevType, cmm4PortResetCfg=cmm4PortResetCfg, satellitesTracked=satellitesTracked, syncStatus=syncStatus, cmm4SnmpTrapIp2=cmm4SnmpTrapIp2, gpsSatellitesTracked=gpsSatellitesTracked, cmm4Gps=cmm4Gps, cmm4UserTableGroup=cmm4UserTableGroup, cmm4MibModule=cmm4MibModule, cmm4SnmpAccessSubnet8=cmm4SnmpAccessSubnet8, longitude=longitude, managementVID=managementVID, gpsDate=gpsDate, entryIndex=entryIndex, cmm4Status=cmm4Status, cmm4SnmpReadOnly=cmm4SnmpReadOnly, gpsReInitCount=gpsReInitCount, cmm4SoftwareVersion=cmm4SoftwareVersion, cmm4MgmtPortSpeed=cmm4MgmtPortSpeed, cmm4PortStatusEntry=cmm4PortStatusEntry, gpsAntennaConnection=gpsAntennaConnection, cmm4SnmpTrapIp7=cmm4SnmpTrapIp7, gpsSyncStatus=gpsSyncStatus, cmm4SnmpTrapIp9=cmm4SnmpTrapIp9, cmm4SnmpAccessSubnet4=cmm4SnmpAccessSubnet4, cmm4SnmpGPSSyncTrapEnable=cmm4SnmpGPSSyncTrapEnable, satellitesVisible=satellitesVisible, portCfgIndex=portCfgIndex, cmm4SnmpTrapIp6=cmm4SnmpTrapIp6, defaultGateway=defaultGateway, cmm4Groups=cmm4Groups, cmm4SnmpTrapIp1=cmm4SnmpTrapIp1, eventLog=eventLog, latitude=latitude, vlanEnable=vlanEnable, cmm4UserTable=cmm4UserTable, gpsReceiverInfo=gpsReceiverInfo, cmm4SNMPGroup=cmm4SNMPGroup, cmm4ExtEthPwrStat=cmm4ExtEthPwrStat, cmm4EventLog=cmm4EventLog, cmm4FPGAPlatform=cmm4FPGAPlatform, gpsLog=gpsLog, cmm4GPSEvent=cmm4GPSEvent, cmm4SnmpTrapIp5=cmm4SnmpTrapIp5, cmm4Event=cmm4Event, accessLevel=accessLevel, userLoginName=userLoginName, cmm4SnmpAccessSubnet9=cmm4SnmpAccessSubnet9, cmm4Config=cmm4Config, cmm4SnmpAccessSubnet2=cmm4SnmpAccessSubnet2, cmm4UpTime=cmm4UpTime, cmm4PortStatusTable=cmm4PortStatusTable, ntpLog=ntpLog, cmm4WebAutoUpdate=cmm4WebAutoUpdate, gpsSyncMasterSlave=gpsSyncMasterSlave, cmm4PortPowerStatus=cmm4PortPowerStatus, gpsTime=gpsTime, cmm4SnmpTrapIp3=cmm4SnmpTrapIp3, gpsTrackingMode=gpsTrackingMode, lan1SubnetMask=lan1SubnetMask, cmm4SnmpAccessSubnet6=cmm4SnmpAccessSubnet6, cmm4Reboot=cmm4Reboot, cmm4ControlsGroup=cmm4ControlsGroup)
