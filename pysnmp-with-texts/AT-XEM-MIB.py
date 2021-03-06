#
# PySNMP MIB module AT-XEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-XEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Bits, Gauge32, iso, Counter64, Unsigned32, IpAddress, ObjectIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "iso", "Counter64", "Unsigned32", "IpAddress", "ObjectIdentity", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xem = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11))
xem.setRevisions(('2010-09-07 00:00', '2010-06-15 00:15', '2009-07-15 00:00', '2008-02-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: xem.setRevisionsDescriptions(('Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Corret a complier warning.', 'Initial version.',))
if mibBuilder.loadTexts: xem.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: xem.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: xem.setContactInfo(' http://www.alliedtelesis.com')
if mibBuilder.loadTexts: xem.setDescription('The AT-XEM MIB contains objects for monitoring XEMs installed in the device.')
xemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0))
xemInserted = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 1)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInserted.setStatus('current')
if mibBuilder.loadTexts: xemInserted.setDescription('A trap generated when a XEM is inserted into the device.')
xemRemoved = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 2)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemRemoved.setStatus('current')
if mibBuilder.loadTexts: xemRemoved.setDescription('A trap generated when a XEM is removed from the device.')
xemInsertedFail = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 3)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInsertedFail.setStatus('current')
if mibBuilder.loadTexts: xemInsertedFail.setDescription('A trap generated when the insertion of a XEM into the device fails.')
xemNumOfXem = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemNumOfXem.setStatus('current')
if mibBuilder.loadTexts: xemNumOfXem.setDescription('The total number of XEMs installed in the device. If devices are stacked, it is the total number of XEMs installed in the stacked devices.')
xemInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2), )
if mibBuilder.loadTexts: xemInfoTable.setStatus('current')
if mibBuilder.loadTexts: xemInfoTable.setDescription('A table of information about XEMs. Each entry in the table represents a XEM installed in the system.')
xemInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1), ).setIndexNames((0, "AT-XEM-MIB", "xemInfoMemberId"), (0, "AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInfoEntry.setStatus('current')
if mibBuilder.loadTexts: xemInfoEntry.setDescription('Information about a single XEM.')
xemInfoMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoMemberId.setStatus('current')
if mibBuilder.loadTexts: xemInfoMemberId.setDescription('The ID of the stack member where the XEM is installed.')
xemInfoBayId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBayId.setStatus('current')
if mibBuilder.loadTexts: xemInfoBayId.setDescription('The bay number where the XEM is installed.')
xemInfoXemId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoXemId.setStatus('current')
if mibBuilder.loadTexts: xemInfoXemId.setDescription('The board identity of the XEM.')
xemInfoBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBoardType.setStatus('current')
if mibBuilder.loadTexts: xemInfoBoardType.setDescription('The board type of the XEM.')
xemInfoBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBoardName.setStatus('current')
if mibBuilder.loadTexts: xemInfoBoardName.setDescription('The board name of the XEM.')
xemInfoRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoRevision.setStatus('current')
if mibBuilder.loadTexts: xemInfoRevision.setDescription('The board revision number of the XEM.')
xemInfoSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoSerialNumber.setStatus('current')
if mibBuilder.loadTexts: xemInfoSerialNumber.setDescription('The board serial number of the XEM.')
mibBuilder.exportSymbols("AT-XEM-MIB", xemInfoMemberId=xemInfoMemberId, xemNumOfXem=xemNumOfXem, xemInserted=xemInserted, xemInfoBayId=xemInfoBayId, xemInfoRevision=xemInfoRevision, xemTraps=xemTraps, xemInfoSerialNumber=xemInfoSerialNumber, xemInfoEntry=xemInfoEntry, xem=xem, xemInfoBoardName=xemInfoBoardName, xemInfoXemId=xemInfoXemId, xemRemoved=xemRemoved, xemInfoTable=xemInfoTable, xemInsertedFail=xemInsertedFail, PYSNMP_MODULE_ID=xem, xemInfoBoardType=xemInfoBoardType)
