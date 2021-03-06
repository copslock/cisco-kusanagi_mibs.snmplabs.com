#
# PySNMP MIB module CYAN-MS64-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-MS64-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
cyanEntityModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules")
CyanSsBitsTc, CyanOpStateQualTc, CyanOpStateTc, CyanChannelIdTc, CyanSecServiceStateTc, CyanAdminStateTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanSsBitsTc", "CyanOpStateQualTc", "CyanOpStateTc", "CyanChannelIdTc", "CyanSecServiceStateTc", "CyanAdminStateTc")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, Counter64, Bits, IpAddress, ModuleIdentity, TimeTicks, Gauge32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "Bits", "IpAddress", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyanMS64Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230))
cyanMS64Module.setRevisions(('2014-12-07 05:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyanMS64Module.setRevisionsDescriptions(('Release 6.0 build 1416362081',))
if mibBuilder.loadTexts: cyanMS64Module.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanMS64Module.setOrganization('Cyan, Inc.')
if mibBuilder.loadTexts: cyanMS64Module.setContactInfo(' E-mail: support@cyaninc.com Postal: Cyan, Inc. 1390 N. McDowell Blvd., # G-327 Petaluma, CA 94954 USA Tel: +1-707-735-2300')
if mibBuilder.loadTexts: cyanMS64Module.setDescription('MIB module for OC-192 Line /STM-64 MS layer')
cyanMS64MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1))
cyanMS64Table = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1), )
if mibBuilder.loadTexts: cyanMS64Table.setStatus('current')
if mibBuilder.loadTexts: cyanMS64Table.setDescription('A list of MS64 entries.')
cyanMS64Entry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1), ).setIndexNames((0, "CYAN-MS64-MIB", "cyanMS64ShelfId"), (0, "CYAN-MS64-MIB", "cyanMS64ModuleId"), (0, "CYAN-MS64-MIB", "cyanMS64MS64Id"))
if mibBuilder.loadTexts: cyanMS64Entry.setStatus('current')
if mibBuilder.loadTexts: cyanMS64Entry.setDescription('An entry of MS64.')
cyanMS64ShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanMS64ShelfId.setStatus('current')
if mibBuilder.loadTexts: cyanMS64ShelfId.setDescription('Shelf Id')
cyanMS64ModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanMS64ModuleId.setStatus('current')
if mibBuilder.loadTexts: cyanMS64ModuleId.setDescription('Module Id')
cyanMS64MS64Id = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cyanMS64MS64Id.setStatus('current')
if mibBuilder.loadTexts: cyanMS64MS64Id.setDescription('MS64 Termination Id')
cyanMS64Accepted = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 4), CyanSsBitsTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64Accepted.setStatus('current')
if mibBuilder.loadTexts: cyanMS64Accepted.setDescription('Receiving SS bits')
cyanMS64AdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 5), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64AdminState.setStatus('current')
if mibBuilder.loadTexts: cyanMS64AdminState.setDescription('Administrative state')
cyanMS64AutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64AutoinserviceSoakTimeSec.setStatus('current')
if mibBuilder.loadTexts: cyanMS64AutoinserviceSoakTimeSec.setDescription('Auto-In-Service soak time')
cyanMS64ChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 7), CyanChannelIdTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64ChannelId.setStatus('current')
if mibBuilder.loadTexts: cyanMS64ChannelId.setDescription('Channel ID')
cyanMS64Inserted = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 8), CyanSsBitsTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64Inserted.setStatus('current')
if mibBuilder.loadTexts: cyanMS64Inserted.setDescription('Transmitting SS bits')
cyanMS64OperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 9), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64OperState.setStatus('current')
if mibBuilder.loadTexts: cyanMS64OperState.setDescription('Primary Operation State')
cyanMS64OperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 10), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64OperStateQual.setStatus('current')
if mibBuilder.loadTexts: cyanMS64OperStateQual.setDescription('Operation state qualifier')
cyanMS64SecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 1, 1, 1, 11), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanMS64SecServState.setStatus('current')
if mibBuilder.loadTexts: cyanMS64SecServState.setDescription('Secondary service state')
cyanMS64ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 20)).setObjects(("CYAN-MS64-MIB", "cyanMS64Accepted"), ("CYAN-MS64-MIB", "cyanMS64AdminState"), ("CYAN-MS64-MIB", "cyanMS64AutoinserviceSoakTimeSec"), ("CYAN-MS64-MIB", "cyanMS64ChannelId"), ("CYAN-MS64-MIB", "cyanMS64Inserted"), ("CYAN-MS64-MIB", "cyanMS64OperState"), ("CYAN-MS64-MIB", "cyanMS64OperStateQual"), ("CYAN-MS64-MIB", "cyanMS64SecServState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanMS64ObjectGroup = cyanMS64ObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cyanMS64ObjectGroup.setDescription('Group of objects that comes with MS64 module')
cyanMS64Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 230, 30)).setObjects(("CYAN-MS64-MIB", "cyanMS64ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanMS64Compliance = cyanMS64Compliance.setStatus('current')
if mibBuilder.loadTexts: cyanMS64Compliance.setDescription('The basic info needed to be a cyan MS64')
mibBuilder.exportSymbols("CYAN-MS64-MIB", cyanMS64MS64Id=cyanMS64MS64Id, cyanMS64Inserted=cyanMS64Inserted, cyanMS64Module=cyanMS64Module, PYSNMP_MODULE_ID=cyanMS64Module, cyanMS64ModuleId=cyanMS64ModuleId, cyanMS64Compliance=cyanMS64Compliance, cyanMS64Table=cyanMS64Table, cyanMS64Entry=cyanMS64Entry, cyanMS64AutoinserviceSoakTimeSec=cyanMS64AutoinserviceSoakTimeSec, cyanMS64ChannelId=cyanMS64ChannelId, cyanMS64SecServState=cyanMS64SecServState, cyanMS64ObjectGroup=cyanMS64ObjectGroup, cyanMS64Accepted=cyanMS64Accepted, cyanMS64OperStateQual=cyanMS64OperStateQual, cyanMS64OperState=cyanMS64OperState, cyanMS64ShelfId=cyanMS64ShelfId, cyanMS64MibObjects=cyanMS64MibObjects, cyanMS64AdminState=cyanMS64AdminState)
