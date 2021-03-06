#
# PySNMP MIB module H3C-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DISK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cStorageRef, H3cStorageEnableState, H3cStorageActionType = mibBuilder.importSymbols("H3C-STORAGE-REF-MIB", "h3cStorageRef", "H3cStorageEnableState", "H3cStorageActionType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, ModuleIdentity, IpAddress, ObjectIdentity, TimeTicks, Gauge32, Integer32, Bits, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ModuleIdentity", "IpAddress", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "Bits", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cDisk = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3))
if mibBuilder.loadTexts: h3cDisk.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: h3cDisk.setOrganization('H3C Technologies Co., Ltd.')
h3cDiskMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1))
h3cDiskTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1), )
if mibBuilder.loadTexts: h3cDiskTable.setStatus('current')
h3cDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1), ).setIndexNames((0, "H3C-DISK-MIB", "h3cDiskIndex"))
if mibBuilder.loadTexts: h3cDiskEntry.setStatus('current')
h3cDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDiskIndex.setStatus('current')
h3cDiskPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("sata", 1), ("pata", 2), ("sas", 3), ("scsi", 4), ("ieee1394", 5), ("fcal", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskPortType.setStatus('current')
h3cDiskPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 3), Integer32()).setUnits('MB/second').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskPortSpeed.setStatus('current')
h3cDiskSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 4), Integer32()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskSize.setStatus('current')
h3cDiskFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 5), Integer32()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskFreeSpace.setStatus('current')
h3cDiskLocationState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 6), H3cStorageEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDiskLocationState.setStatus('current')
h3cDiskRunLedState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("blink", 2), ("fastblink", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskRunLedState.setStatus('current')
h3cDiskFaultLedState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("blink", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskFaultLedState.setStatus('current')
h3cDiskInitialize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 9), H3cStorageActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDiskInitialize.setStatus('current')
h3cDiskGlobalSpare = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("globalSpare", 1), ("nonglobalSpare", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDiskGlobalSpare.setStatus('current')
h3cDiskLocalSpare = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localSpare", 1), ("nonlocalSpare", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskLocalSpare.setStatus('current')
h3cDiskReadCache = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 12), H3cStorageEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDiskReadCache.setStatus('current')
h3cDiskWriteCache = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 13), H3cStorageEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDiskWriteCache.setStatus('current')
h3cDiskPowerOffReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("environmentUnstable", 1), ("mediumError", 2), ("smartCheckError", 3), ("generalError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDiskPowerOffReason.setStatus('current')
mibBuilder.exportSymbols("H3C-DISK-MIB", h3cDisk=h3cDisk, h3cDiskPowerOffReason=h3cDiskPowerOffReason, h3cDiskLocationState=h3cDiskLocationState, h3cDiskPortSpeed=h3cDiskPortSpeed, h3cDiskIndex=h3cDiskIndex, h3cDiskWriteCache=h3cDiskWriteCache, h3cDiskPortType=h3cDiskPortType, h3cDiskFaultLedState=h3cDiskFaultLedState, h3cDiskTable=h3cDiskTable, h3cDiskSize=h3cDiskSize, h3cDiskEntry=h3cDiskEntry, PYSNMP_MODULE_ID=h3cDisk, h3cDiskReadCache=h3cDiskReadCache, h3cDiskGlobalSpare=h3cDiskGlobalSpare, h3cDiskMibObjects=h3cDiskMibObjects, h3cDiskFreeSpace=h3cDiskFreeSpace, h3cDiskRunLedState=h3cDiskRunLedState, h3cDiskInitialize=h3cDiskInitialize, h3cDiskLocalSpare=h3cDiskLocalSpare)
