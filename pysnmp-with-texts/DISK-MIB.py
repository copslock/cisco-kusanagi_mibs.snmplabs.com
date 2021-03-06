#
# PySNMP MIB module DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DISK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:47:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, NotificationType, Gauge32, Unsigned32, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, iso, Bits, TimeTicks, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Gauge32", "Unsigned32", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "iso", "Bits", "TimeTicks", "ModuleIdentity", "MibIdentifier")
TruthValue, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention")
deviceDiskMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 2))
if mibBuilder.loadTexts: deviceDiskMIB.setLastUpdated('0211060300Z')
if mibBuilder.loadTexts: deviceDiskMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceDiskMIB.setContactInfo('support@bluecoat.com')
if mibBuilder.loadTexts: deviceDiskMIB.setDescription('The deviceDiskMIB is used to monitor the status of the device disks')
deviceDiskMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1))
deviceDiskMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 2))
deviceDiskMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0))
class DiskStatus(TextualConvention, Integer32):
    description = 'Indicates the operational status of the disk. present means the agent disk is operational. initializing the disk is being formatted by the device for use. inserted the disk has been inserted into the device. offline the disk has been taken offline by the system. removed the disk is being removed from the drive slot. not-present no disk is present in drive slot. empty the drive slot is not in use. bad the drive is in an error state unknown cannot determine disk status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("present", 1), ("initializing", 2), ("inserted", 3), ("offline", 4), ("removed", 5), ("not-present", 6), ("empty", 7), ("bad", 8), ("unknown", 9))

deviceDiskValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1))
deviceDiskValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1), )
if mibBuilder.loadTexts: deviceDiskValueTable.setStatus('current')
if mibBuilder.loadTexts: deviceDiskValueTable.setDescription('Table of disks.')
deviceDiskValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1), ).setIndexNames((0, "DISK-MIB", "deviceDiskIndex"))
if mibBuilder.loadTexts: deviceDiskValueEntry.setStatus('current')
if mibBuilder.loadTexts: deviceDiskValueEntry.setDescription('An deviceDiskValueTable entry describes the characteristics and operational status of a disk.')
deviceDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceDiskIndex.setStatus('current')
if mibBuilder.loadTexts: deviceDiskIndex.setDescription('An arbitrary value which uniquely identifies the disk.')
deviceDiskTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceDiskTrapEnabled.setStatus('current')
if mibBuilder.loadTexts: deviceDiskTrapEnabled.setDescription('This variable controls generation of deviceDiskTrap for this disk. When this variable is true(1), generation of deviceDiskTrap is enabled. When this variable is false(2), generation of deviceDiskTrap is disabled. The default start-up value is true(1).')
deviceDiskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 3), DiskStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskStatus.setStatus('current')
if mibBuilder.loadTexts: deviceDiskStatus.setDescription('This variable indicates the present operational status of the disk.')
deviceDiskTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskTimeStamp.setStatus('current')
if mibBuilder.loadTexts: deviceDiskTimeStamp.setDescription('This variable indicates when the value of deviceDiskStatus was last reported.')
deviceDiskVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskVendor.setStatus('current')
if mibBuilder.loadTexts: deviceDiskVendor.setDescription('The Vendor name.')
deviceDiskProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskProduct.setStatus('current')
if mibBuilder.loadTexts: deviceDiskProduct.setDescription('The product name.')
deviceDiskRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskRevision.setStatus('current')
if mibBuilder.loadTexts: deviceDiskRevision.setDescription('Revision code.')
deviceDiskSerialN = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskSerialN.setStatus('current')
if mibBuilder.loadTexts: deviceDiskSerialN.setDescription('Serial number of disk.')
deviceDiskBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskBlockSize.setStatus('current')
if mibBuilder.loadTexts: deviceDiskBlockSize.setDescription('Block size drive has been formatted to in bytes.')
deviceDiskBlockCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskBlockCount.setStatus('current')
if mibBuilder.loadTexts: deviceDiskBlockCount.setDescription('The number of blocks on the drive.')
deviceDiskTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0, 1)).setObjects(("DISK-MIB", "deviceDiskStatus"))
if mibBuilder.loadTexts: deviceDiskTrap.setStatus('current')
if mibBuilder.loadTexts: deviceDiskTrap.setDescription('The disk status warrants a notification.')
mibBuilder.exportSymbols("DISK-MIB", deviceDiskTrap=deviceDiskTrap, DiskStatus=DiskStatus, deviceDiskValueTable=deviceDiskValueTable, deviceDiskMIBNotifications=deviceDiskMIBNotifications, PYSNMP_MODULE_ID=deviceDiskMIB, deviceDiskMIBNotificationsPrefix=deviceDiskMIBNotificationsPrefix, deviceDiskMIBObjects=deviceDiskMIBObjects, deviceDiskStatus=deviceDiskStatus, deviceDiskBlockSize=deviceDiskBlockSize, deviceDiskValueEntry=deviceDiskValueEntry, deviceDiskTimeStamp=deviceDiskTimeStamp, deviceDiskTrapEnabled=deviceDiskTrapEnabled, deviceDiskProduct=deviceDiskProduct, deviceDiskMIB=deviceDiskMIB, deviceDiskBlockCount=deviceDiskBlockCount, deviceDiskRevision=deviceDiskRevision, deviceDiskVendor=deviceDiskVendor, deviceDiskSerialN=deviceDiskSerialN, deviceDiskValues=deviceDiskValues, deviceDiskIndex=deviceDiskIndex)
