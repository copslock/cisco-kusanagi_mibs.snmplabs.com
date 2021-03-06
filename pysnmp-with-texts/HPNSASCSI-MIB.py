#
# PySNMP MIB module HPNSASCSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPNSASCSI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, enterprises, Bits, ObjectIdentity, NotificationType, Integer32, TimeTicks, ModuleIdentity, MibIdentifier, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "enterprises", "Bits", "ObjectIdentity", "NotificationType", "Integer32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaScsi = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 14))
hpnsaScsiMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 1))
hpnsaScsiAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2))
hpnsaScsiHba = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3))
hpnsaScsiDev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4))
hpnsaScsiMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiMibRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiMibRevMajor.setDescription('The major revision level of the MIB. A change in the major revision level represents a major change in the architecture or functions of the MIB.')
hpnsaScsiMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiMibRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiMibRevMinor.setDescription('The minor revision level of the MIB. A change in the minor revision level may represent some minor additional support, no changes to any pre-existing information has occurred.')
hpnsaScsiAgentModuleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1), )
if mibBuilder.loadTexts: hpnsaScsiAgentModuleTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiAgentModuleTable.setDescription('A table of SNMP Agents that satisfy request pertaining to this MIB.')
hpnsaScsiAgentModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1), ).setIndexNames((0, "HPNSASCSI-MIB", "hpnsaScsiAgentModuleIndex"))
if mibBuilder.loadTexts: hpnsaScsiAgentModuleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiAgentModuleEntry.setDescription('A description of the Agents that access system information.')
hpnsaScsiAgentModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiAgentModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiAgentModuleIndex.setDescription('A unique index for this module description.')
hpnsaScsiAgentModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiAgentModuleName.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiAgentModuleName.setDescription('The module name.')
hpnsaScsiAgentModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiAgentModuleVersion.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiAgentModuleVersion.setDescription('The module version in XX.YY format. Where XX is the major version number and YY is the minor version number. This field will be a null (size 0) string if the agent cannot provide the module version.')
hpnsaScsiAgentModuleDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiAgentModuleDate.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiAgentModuleDate.setDescription('The module date. field octets contents range _________________________________________________ 1 1-2 year 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minute 0..59 6 7 second 0..60 (use 60 for leap-second) This field will be set to year = 0 if the agent cannot provide the module date. The hour, minute, and second field will be set to zero (0) if they are not relevant. The year field is set with the most significant octet first.')
hpnsaScsiHbaTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1), )
if mibBuilder.loadTexts: hpnsaScsiHbaTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiHbaTable.setDescription('A list of SCSI Host Bus Adapter entries.')
hpnsaScsiHbaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1), ).setIndexNames((0, "HPNSASCSI-MIB", "hpnsaScsiHbaIndex"))
if mibBuilder.loadTexts: hpnsaScsiHbaEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiHbaEntry.setDescription('A description of an SCSI device/function.')
hpnsaScsiHbaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiHbaIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiHbaIndex.setDescription('The SCSI HBA number that this entry describes.')
hpnsaScsiHbaTargetId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiHbaTargetId.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiHbaTargetId.setDescription('The SCSI target ID or SCSI address for this HBA.')
hpnsaScsiHbaManagerId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiHbaManagerId.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiHbaManagerId.setDescription('String that describes the SCSI Manager.')
hpnsaScsiHbaHostAdapterId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiHbaHostAdapterId.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiHbaHostAdapterId.setDescription('String that describes the SCSI host adapter.')
hpnsaScsiDevTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1), )
if mibBuilder.loadTexts: hpnsaScsiDevTable.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevTable.setDescription('A list of SCSI device entries.')
hpnsaScsiDevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1), ).setIndexNames((0, "HPNSASCSI-MIB", "hpnsaScsiDevHbaIndex"), (0, "HPNSASCSI-MIB", "hpnsaScsiDevTargIdIndex"), (0, "HPNSASCSI-MIB", "hpnsaScsiDevLunIndex"))
if mibBuilder.loadTexts: hpnsaScsiDevEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevEntry.setDescription('A description of a SCSI device.')
hpnsaScsiDevHbaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevHbaIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevHbaIndex.setDescription('The SCSI HBA number that this entry describes.')
hpnsaScsiDevTargIdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevTargIdIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevTargIdIndex.setDescription('The SCSI target ID or SCSI address for this HBA.')
hpnsaScsiDevLunIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevLunIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevLunIndex.setDescription('The SCSI LUN for this HBA.')
hpnsaScsiDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevType.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevType.setDescription('Identifies the type of SCSI device: Code Description ---- ----------- 00h Direct-access device (e.g. magnetic disk) 01h Sequential-access device (e.g. magnetic tape) 02h Printer device 03h Processor device 04h Write-once read-multiple device (e.g. some optical disks) 05h CD-ROM device 06h Scanner device 07h Optical Memory device (e.g. some optical disks) 08h Medium Changer device (e.g. jukeboxes) 09h Communications device 0A-1Eh Reserved 1Fh Unknown or no device type')
hpnsaScsiDevRmb = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevRmb.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevRmb.setDescription('Identifies whether the medium is removable or not. 0 = medium is not removable 1 = medium is removable')
hpnsaScsiDevAnsiVer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevAnsiVer.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevAnsiVer.setDescription('Indicates the implemented ANSI version of this device. 0 = might or might not comply to an ANSI standard 1 = complies to ANSI X3.131-1986 (SCSI-1) 2 = comples to ANSI ?????? (SCSI-II) 3-7 = reserved')
hpnsaScsiDevEcmaVer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevEcmaVer.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevEcmaVer.setDescription('Indicates the implemented ECMA version of this device. Zero code indicates that this device does not comply with this standard.')
hpnsaScsiDevIsoVer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevIsoVer.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevIsoVer.setDescription('Indicates the implemented ISO version of this device. Zero code indicates that this device does not comply with this standard.')
hpnsaScsiDevVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevVendorId.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevVendorId.setDescription('Identifies the vendor of the product.')
hpnsaScsiDevProductId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevProductId.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevProductId.setDescription('Identifies the product as defined by the vendor.')
hpnsaScsiDevProductRev = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevProductRev.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevProductRev.setDescription('Identifies the product revision level.')
hpnsaScsiDevLogicalBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevLogicalBlocks.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevLogicalBlocks.setDescription('A 32-bit value that represents the total number of logical blocks for this device. Octet 1 is the LSB, and octet 4 is the MSB.')
hpnsaScsiDevBlockLength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevBlockLength.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevBlockLength.setDescription('A 32-bit value that represents the size of a logical block for this device. Octet 1 is the LSB, and octet 4 is the MSB.')
hpnsaScsiDevCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 23, 14, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaScsiDevCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: hpnsaScsiDevCapacity.setDescription('A value that represents the capacity of the device in megabytes. One megabyte equals to 1,048,576 when calculating this value.')
mibBuilder.exportSymbols("HPNSASCSI-MIB", hpnsaScsiDevLunIndex=hpnsaScsiDevLunIndex, hpnsaScsiDevBlockLength=hpnsaScsiDevBlockLength, hpnsaScsiHbaHostAdapterId=hpnsaScsiHbaHostAdapterId, hpnsaScsiAgentModuleEntry=hpnsaScsiAgentModuleEntry, hpnsaScsi=hpnsaScsi, hpnsaScsiHbaManagerId=hpnsaScsiHbaManagerId, hpnsaScsiAgentModuleTable=hpnsaScsiAgentModuleTable, hpnsaScsiDev=hpnsaScsiDev, hpnsaScsiDevVendorId=hpnsaScsiDevVendorId, hpnsaScsiHbaIndex=hpnsaScsiHbaIndex, hpnsaScsiAgent=hpnsaScsiAgent, hpnsaScsiAgentModuleIndex=hpnsaScsiAgentModuleIndex, hpnsaScsiDevProductRev=hpnsaScsiDevProductRev, hpnsaScsiDevTargIdIndex=hpnsaScsiDevTargIdIndex, hpnsa=hpnsa, hpnsaScsiDevLogicalBlocks=hpnsaScsiDevLogicalBlocks, hpnsaScsiMibRevMinor=hpnsaScsiMibRevMinor, hpnsaScsiDevHbaIndex=hpnsaScsiDevHbaIndex, hp=hp, hpnsaScsiHba=hpnsaScsiHba, hpnsaScsiAgentModuleName=hpnsaScsiAgentModuleName, hpnsaScsiDevRmb=hpnsaScsiDevRmb, hpnsaScsiMibRev=hpnsaScsiMibRev, hpnsaScsiAgentModuleDate=hpnsaScsiAgentModuleDate, hpnsaScsiHbaTargetId=hpnsaScsiHbaTargetId, hpnsaScsiDevCapacity=hpnsaScsiDevCapacity, hpnsaScsiDevTable=hpnsaScsiDevTable, hpnsaScsiDevEcmaVer=hpnsaScsiDevEcmaVer, hpnsaScsiDevProductId=hpnsaScsiDevProductId, hpnsaScsiMibRevMajor=hpnsaScsiMibRevMajor, hpnsaScsiDevType=hpnsaScsiDevType, nm=nm, hpnsaScsiHbaTable=hpnsaScsiHbaTable, hpnsaScsiDevIsoVer=hpnsaScsiDevIsoVer, hpnsaScsiDevAnsiVer=hpnsaScsiDevAnsiVer, hpnsaScsiDevEntry=hpnsaScsiDevEntry, hpnsaScsiHbaEntry=hpnsaScsiHbaEntry, hpnsaScsiAgentModuleVersion=hpnsaScsiAgentModuleVersion)
