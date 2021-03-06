#
# PySNMP MIB module CYAN-AUG64-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-AUG64-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cyanEntityModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules")
CyanAdminStateTc, CyanSecServiceStateTc, CyanAugStructureTc, CyanOpStateTc, CyanOpStateQualTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanAdminStateTc", "CyanSecServiceStateTc", "CyanAugStructureTc", "CyanOpStateTc", "CyanOpStateQualTc")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, IpAddress, NotificationType, iso, Unsigned32, Counter64, MibIdentifier, ModuleIdentity, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "iso", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyanAUG64Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240))
cyanAUG64Module.setRevisions(('2014-12-07 05:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyanAUG64Module.setRevisionsDescriptions(('Release 6.0 build 1416362081',))
if mibBuilder.loadTexts: cyanAUG64Module.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanAUG64Module.setOrganization('Cyan, Inc.')
if mibBuilder.loadTexts: cyanAUG64Module.setContactInfo(' E-mail: support@cyaninc.com Postal: Cyan, Inc. 1390 N. McDowell Blvd., # G-327 Petaluma, CA 94954 USA Tel: +1-707-735-2300')
if mibBuilder.loadTexts: cyanAUG64Module.setDescription('MIB module for STS-192/AUG-64 layer')
cyanAUG64MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1))
cyanAUG64Table = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1), )
if mibBuilder.loadTexts: cyanAUG64Table.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64Table.setDescription('A list of AUG64 entries.')
cyanAUG64Entry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1), ).setIndexNames((0, "CYAN-AUG64-MIB", "cyanAUG64ShelfId"), (0, "CYAN-AUG64-MIB", "cyanAUG64ModuleId"), (0, "CYAN-AUG64-MIB", "cyanAUG64AUG64Id"))
if mibBuilder.loadTexts: cyanAUG64Entry.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64Entry.setDescription('An entry of AUG64.')
cyanAUG64ShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanAUG64ShelfId.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64ShelfId.setDescription('Shelf Id')
cyanAUG64ModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanAUG64ModuleId.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64ModuleId.setDescription('Module Id')
cyanAUG64AUG64Id = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cyanAUG64AUG64Id.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64AUG64Id.setDescription('AUG64 Termination Id')
cyanAUG64AdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 4), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64AdminState.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64AdminState.setDescription('Administrative state')
cyanAUG64AutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64AutoinserviceSoakTimeSec.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64AutoinserviceSoakTimeSec.setDescription('Auto-In-Service soak time')
cyanAUG64Description = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64Description.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64Description.setDescription('Description')
cyanAUG64OperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 7), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64OperState.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64OperState.setDescription('Primary Operation State')
cyanAUG64OperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 8), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64OperStateQual.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64OperStateQual.setDescription('Operation state qualifier')
cyanAUG64SecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 9), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64SecServState.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64SecServState.setDescription('Secondary service state')
cyanAUG64StsaugStructure = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 1, 1, 1, 10), CyanAugStructureTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanAUG64StsaugStructure.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64StsaugStructure.setDescription('AUG structure')
cyanAUG64ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 20)).setObjects(("CYAN-AUG64-MIB", "cyanAUG64AdminState"), ("CYAN-AUG64-MIB", "cyanAUG64AutoinserviceSoakTimeSec"), ("CYAN-AUG64-MIB", "cyanAUG64Description"), ("CYAN-AUG64-MIB", "cyanAUG64OperState"), ("CYAN-AUG64-MIB", "cyanAUG64OperStateQual"), ("CYAN-AUG64-MIB", "cyanAUG64SecServState"), ("CYAN-AUG64-MIB", "cyanAUG64StsaugStructure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanAUG64ObjectGroup = cyanAUG64ObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64ObjectGroup.setDescription('Group of objects that comes with AUG64 module')
cyanAUG64Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 240, 30)).setObjects(("CYAN-AUG64-MIB", "cyanAUG64ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanAUG64Compliance = cyanAUG64Compliance.setStatus('current')
if mibBuilder.loadTexts: cyanAUG64Compliance.setDescription('The basic info needed to be a cyan AUG64')
mibBuilder.exportSymbols("CYAN-AUG64-MIB", cyanAUG64Module=cyanAUG64Module, cyanAUG64ModuleId=cyanAUG64ModuleId, cyanAUG64AUG64Id=cyanAUG64AUG64Id, cyanAUG64AdminState=cyanAUG64AdminState, cyanAUG64SecServState=cyanAUG64SecServState, cyanAUG64MibObjects=cyanAUG64MibObjects, cyanAUG64ObjectGroup=cyanAUG64ObjectGroup, cyanAUG64OperStateQual=cyanAUG64OperStateQual, cyanAUG64Entry=cyanAUG64Entry, cyanAUG64StsaugStructure=cyanAUG64StsaugStructure, PYSNMP_MODULE_ID=cyanAUG64Module, cyanAUG64Description=cyanAUG64Description, cyanAUG64Compliance=cyanAUG64Compliance, cyanAUG64ShelfId=cyanAUG64ShelfId, cyanAUG64OperState=cyanAUG64OperState, cyanAUG64Table=cyanAUG64Table, cyanAUG64AutoinserviceSoakTimeSec=cyanAUG64AutoinserviceSoakTimeSec)
