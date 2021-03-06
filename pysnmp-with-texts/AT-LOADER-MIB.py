#
# PySNMP MIB module AT-LOADER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-LOADER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
modules, DisplayStringUnsized = mibBuilder.importSymbols("AT-SMI-MIB", "modules", "DisplayStringUnsized")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, TimeTicks, Integer32, Bits, IpAddress, ModuleIdentity, iso, ObjectIdentity, MibIdentifier, Counter64, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "TimeTicks", "Integer32", "Bits", "IpAddress", "ModuleIdentity", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "Counter32", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
loader = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48))
loader.setRevisions(('2007-02-07 10:10', '2006-06-28 12:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: loader.setRevisionsDescriptions(('This MIB file contains definitions of managed objects for the LOAD module. ', 'Initial Revision',))
if mibBuilder.loadTexts: loader.setLastUpdated('200702071010Z')
if mibBuilder.loadTexts: loader.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: loader.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: loader.setDescription('To handle upload, object loadStatus is upgraded, as well as the description for objects loadServer and loadFilename.')
loadTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1), )
if mibBuilder.loadTexts: loadTable.setStatus('current')
if mibBuilder.loadTexts: loadTable.setDescription('The table of load parameters, dynamic and static.')
loadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1), ).setIndexNames((0, "AT-LOADER-MIB", "loadIndex"))
if mibBuilder.loadTexts: loadEntry.setStatus('current')
if mibBuilder.loadTexts: loadEntry.setDescription('A single entry of load parameters. This contains the parameters required to perform a load from the router.')
loadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadIndex.setStatus('current')
if mibBuilder.loadTexts: loadIndex.setDescription('There are two sets of load information, dynamic and static. The dynamic information is used once, then cleared. The static information is used whenever the dynamic information is not available. The dynamic information is also used to indicate the current load parameters when a load is in progress.')
loadServer = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadServer.setStatus('current')
if mibBuilder.loadTexts: loadServer.setDescription('The IP address from which load will load or upload.')
loadDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("undefined", 1), ("nvs", 2), ("flash", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadDestination.setStatus('current')
if mibBuilder.loadTexts: loadDestination.setDescription('The destination of the file loaded, either flash or nvs memory, or undefined.')
loadFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadFilename.setStatus('current')
if mibBuilder.loadTexts: loadFilename.setDescription('The file name of the file being loaded or uploaded.')
loadDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadDelay.setStatus('current')
if mibBuilder.loadTexts: loadDelay.setDescription('A delay in seconds between the initiation of the load and the start of the load. This allows for time to set up TFTP servers in cases where the terminal and TFTP server are using the same piece of equipment but will not work simultaneously.')
loadStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("idle", 1), ("wait", 2), ("loading", 3), ("complete", 4), ("reset", 5), ("actionload", 6), ("actionstop", 7), ("actionupload", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadStatus.setStatus('current')
if mibBuilder.loadTexts: loadStatus.setDescription("Status and action object for the load module. The values 1 to 5 are read-only values and reflect the state of the load module. Values 4 and 5 (complete and reset) are 'read-once', that is, if their values are read, either by SNMP or by manager console command, then they will be changed back to idle(1). The action values (6,7,8) cause a start and stop of the load/upload process respectively. Starting the load/upload can only occur if this field has the values 1, 4, or 5. Stopping the load can only occur is this field has the values 2 or 3. Reading the value of the loadStatus after one of actionstart or actionstop has been set will give one of the values 1 to 5. Note: A single exception to the above rules is that if the value of loadStatus is idle(1), then a write of 1 to this variable will succeed without generating an error. This exception is to allow certain SNMP test suites to test this variable without throwing up errors.")
mibBuilder.exportSymbols("AT-LOADER-MIB", loadEntry=loadEntry, loadTable=loadTable, loadIndex=loadIndex, loadFilename=loadFilename, loadServer=loadServer, loadDelay=loadDelay, loadStatus=loadStatus, loader=loader, PYSNMP_MODULE_ID=loader, loadDestination=loadDestination)
