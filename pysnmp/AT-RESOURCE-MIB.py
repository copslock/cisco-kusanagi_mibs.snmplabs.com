#
# PySNMP MIB module AT-RESOURCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-RESOURCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Integer32, Gauge32, MibIdentifier, Counter64, NotificationType, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Integer32", "Gauge32", "MibIdentifier", "Counter64", "NotificationType", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
resource = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21))
resource.setRevisions(('2012-09-21 00:00', '2012-05-22 03:00', '2010-06-15 00:15', '2009-10-22 23:00', '2008-10-20 10:00', '1920-08-09 04:00',))
if mibBuilder.loadTexts: resource.setLastUpdated('201209210000Z')
if mibBuilder.loadTexts: resource.setOrganization('Allied Telesis, Inc.')
rscBoardTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1), )
if mibBuilder.loadTexts: rscBoardTable.setStatus('current')
rscBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1), ).setIndexNames((0, "AT-RESOURCE-MIB", "rscStkId"), (0, "AT-RESOURCE-MIB", "rscResourceId"))
if mibBuilder.loadTexts: rscBoardEntry.setStatus('current')
rscStkId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: rscStkId.setStatus('current')
rscResourceId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)))
if mibBuilder.loadTexts: rscResourceId.setStatus('current')
rscBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardType.setStatus('current')
rscBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardName.setStatus('current')
rscBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardID.setStatus('current')
rscBoardBay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rscBoardBay.setStatus('current')
rscBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardRevision.setStatus('current')
rscBoardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rscBoardSerialNumber.setStatus('current')
hostInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2), )
if mibBuilder.loadTexts: hostInfoTable.setStatus('current')
hostInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1), ).setIndexNames((0, "AT-RESOURCE-MIB", "rscStkId"))
if mibBuilder.loadTexts: hostInfoEntry.setStatus('current')
hostInfoDRAM = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoDRAM.setStatus('current')
hostInfoFlash = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoFlash.setStatus('current')
hostInfoUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoUptime.setStatus('current')
hostInfoBootloaderVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 21, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInfoBootloaderVersion.setStatus('current')
mibBuilder.exportSymbols("AT-RESOURCE-MIB", rscBoardID=rscBoardID, resource=resource, hostInfoUptime=hostInfoUptime, rscStkId=rscStkId, hostInfoBootloaderVersion=hostInfoBootloaderVersion, rscBoardName=rscBoardName, hostInfoTable=hostInfoTable, rscBoardBay=rscBoardBay, hostInfoDRAM=hostInfoDRAM, rscBoardSerialNumber=rscBoardSerialNumber, rscBoardTable=rscBoardTable, hostInfoFlash=hostInfoFlash, rscBoardRevision=rscBoardRevision, rscResourceId=rscResourceId, rscBoardType=rscBoardType, PYSNMP_MODULE_ID=resource, hostInfoEntry=hostInfoEntry, rscBoardEntry=rscBoardEntry)
