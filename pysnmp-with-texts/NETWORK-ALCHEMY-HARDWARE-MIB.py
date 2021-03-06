#
# PySNMP MIB module NETWORK-ALCHEMY-HARDWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETWORK-ALCHEMY-HARDWARE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
hardware, netalModules = mibBuilder.importSymbols("NETAL-SMI", "hardware", "netalModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, NotificationType, MibIdentifier, Integer32, Gauge32, IpAddress, ObjectIdentity, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "ObjectIdentity", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
networkAlchemyHardwareMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2972, 5, 4))
networkAlchemyHardwareMIB.setRevisions(('2000-10-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: networkAlchemyHardwareMIB.setRevisionsDescriptions(('Four-digit year in dates.',))
if mibBuilder.loadTexts: networkAlchemyHardwareMIB.setLastUpdated('200010250000Z')
if mibBuilder.loadTexts: networkAlchemyHardwareMIB.setOrganization('Network Alchemy, Inc.')
if mibBuilder.loadTexts: networkAlchemyHardwareMIB.setContactInfo(' Network Alchemy Customer Support Postal: 1538 Pacific Av. Santa Cruz, CA 95060 USA E-Mail: snmp-contact@network-alchemy.com')
if mibBuilder.loadTexts: networkAlchemyHardwareMIB.setDescription('Hardware (and version) MIB module.')
hardwarePrimaryCPU = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwarePrimaryCPU.setStatus('current')
if mibBuilder.loadTexts: hardwarePrimaryCPU.setDescription('Percent idle')
hardwaresecondarycpu = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwaresecondarycpu.setStatus('current')
if mibBuilder.loadTexts: hardwaresecondarycpu.setDescription('percent')
hardwarehifnloadave = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwarehifnloadave.setStatus('current')
if mibBuilder.loadTexts: hardwarehifnloadave.setDescription('percent')
hardwarememoryusage = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwarememoryusage.setStatus('current')
if mibBuilder.loadTexts: hardwarememoryusage.setDescription('Percent of memory currently in use.')
hardwarioload = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwarioload.setStatus('current')
if mibBuilder.loadTexts: hardwarioload.setDescription('PPS')
hardwareuptime = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareuptime.setStatus('current')
if mibBuilder.loadTexts: hardwareuptime.setDescription('Uptime in Seconds')
hardwareosname = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareosname.setStatus('current')
if mibBuilder.loadTexts: hardwareosname.setDescription('Operating system name.')
hardwareosversion = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareosversion.setStatus('current')
if mibBuilder.loadTexts: hardwareosversion.setDescription('Operating system (kernel) version.')
hardwarecompileuser = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwarecompileuser.setStatus('current')
if mibBuilder.loadTexts: hardwarecompileuser.setDescription('What user compiled this kernel.')
hardwarecompiledate = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwarecompiledate.setStatus('current')
if mibBuilder.loadTexts: hardwarecompiledate.setDescription('Compile date and time.')
hardwarecompilehost = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwarecompilehost.setStatus('current')
if mibBuilder.loadTexts: hardwarecompilehost.setDescription('Computer where this build was made.')
hardwareconfigversion = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareconfigversion.setStatus('current')
if mibBuilder.loadTexts: hardwareconfigversion.setDescription('Version of config file (number of config saves).')
mibBuilder.exportSymbols("NETWORK-ALCHEMY-HARDWARE-MIB", PYSNMP_MODULE_ID=networkAlchemyHardwareMIB, hardwarioload=hardwarioload, networkAlchemyHardwareMIB=networkAlchemyHardwareMIB, hardwareuptime=hardwareuptime, hardwareosname=hardwareosname, hardwarehifnloadave=hardwarehifnloadave, hardwareconfigversion=hardwareconfigversion, hardwarecompileuser=hardwarecompileuser, hardwarememoryusage=hardwarememoryusage, hardwareosversion=hardwareosversion, hardwaresecondarycpu=hardwaresecondarycpu, hardwarecompiledate=hardwarecompiledate, hardwarecompilehost=hardwarecompilehost, hardwarePrimaryCPU=hardwarePrimaryCPU)
