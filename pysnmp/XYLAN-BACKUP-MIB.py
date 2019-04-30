#
# PySNMP MIB module XYLAN-BACKUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-BACKUP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, Gauge32, iso, Unsigned32, Counter32, NotificationType, ModuleIdentity, IpAddress, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Gauge32", "iso", "Unsigned32", "Counter32", "NotificationType", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanBackupArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanBackupArch")
backupxConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 16, 1))
backupxConfigTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1), )
if mibBuilder.loadTexts: backupxConfigTable.setStatus('mandatory')
backupxConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1), ).setIndexNames((0, "XYLAN-BACKUP-MIB", "backupxConfigID"))
if mibBuilder.loadTexts: backupxConfigEntry.setStatus('mandatory')
backupxConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupxConfigID.setStatus('mandatory')
backupxConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigDescription.setStatus('mandatory')
backupxConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigAdminStatus.setStatus('mandatory')
backupxConfigPrimaryType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("physicalPort", 1), ("frameRelayPvcDlci", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigPrimaryType.setStatus('mandatory')
backupxConfigPrimaryIndex1 = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigPrimaryIndex1.setStatus('mandatory')
backupxConfigPrimaryIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigPrimaryIndex2.setStatus('mandatory')
backupxConfigPrimaryIndex3 = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigPrimaryIndex3.setStatus('mandatory')
backupxConfigBackupType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("pppPeer", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigBackupType.setStatus('mandatory')
backupxConfigBackupIndex1 = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigBackupIndex1.setStatus('mandatory')
backupxConfigBackupIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigBackupIndex2.setStatus('mandatory')
backupxConfigBackupIndex3 = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigBackupIndex3.setStatus('mandatory')
backupxConfigStartupTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigStartupTimeout.setStatus('mandatory')
backupxConfigActivateTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigActivateTimeout.setStatus('mandatory')
backupxConfigRestoreTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 16, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupxConfigRestoreTimeout.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-BACKUP-MIB", backupxConfigActivateTimeout=backupxConfigActivateTimeout, backupxConfigBackupType=backupxConfigBackupType, backupxConfigTable=backupxConfigTable, backupxConfigEntry=backupxConfigEntry, backupxConfigPrimaryIndex3=backupxConfigPrimaryIndex3, backupxConfigPrimaryType=backupxConfigPrimaryType, backupxConfigDescription=backupxConfigDescription, backupxConfigRestoreTimeout=backupxConfigRestoreTimeout, backupxConfigAdminStatus=backupxConfigAdminStatus, backupxConfigPrimaryIndex2=backupxConfigPrimaryIndex2, backupxConfigBackupIndex2=backupxConfigBackupIndex2, backupxConfigPrimaryIndex1=backupxConfigPrimaryIndex1, backupxConfigStartupTimeout=backupxConfigStartupTimeout, backupxConfigID=backupxConfigID, backupxConfigBackupIndex1=backupxConfigBackupIndex1, backupxConfigGroup=backupxConfigGroup, backupxConfigBackupIndex3=backupxConfigBackupIndex3)