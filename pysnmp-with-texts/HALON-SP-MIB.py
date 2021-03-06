#
# PySNMP MIB module HALON-SP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HALON-SP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, MibIdentifier, Gauge32, Counter32, Bits, IpAddress, TimeTicks, Integer32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "MibIdentifier", "Gauge32", "Counter32", "Bits", "IpAddress", "TimeTicks", "Integer32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
halonSecuritySP = ModuleIdentity((1, 3, 6, 1, 4, 1, 33234, 1, 1))
halonSecuritySP.setRevisions(('2013-02-07 11:32',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: halonSecuritySP.setRevisionsDescriptions(('Initial release',))
if mibBuilder.loadTexts: halonSecuritySP.setLastUpdated('201302061107Z')
if mibBuilder.loadTexts: halonSecuritySP.setOrganization('Halon Security')
if mibBuilder.loadTexts: halonSecuritySP.setContactInfo('http://www.halon.se')
if mibBuilder.loadTexts: halonSecuritySP.setDescription('SNMP MIB for Halon')
halonSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 33234))
halonSecurityProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 33234, 1))
halonSecuritySPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1))
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('Serial number')
configurationRevision = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationRevision.setStatus('current')
if mibBuilder.loadTexts: configurationRevision.setDescription('Running configuration revision')
mailQueueLength = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mailQueueLength.setStatus('current')
if mibBuilder.loadTexts: mailQueueLength.setDescription('Length of mail queue to be delivered')
quarantinedMessages = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quarantinedMessages.setStatus('current')
if mibBuilder.loadTexts: quarantinedMessages.setDescription('Messages in quarantine')
statTable = MibTable((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5), )
if mibBuilder.loadTexts: statTable.setStatus('current')
if mibBuilder.loadTexts: statTable.setDescription('Table containing statistics')
statEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1), ).setIndexNames((0, "HALON-SP-MIB", "statKey1Index"), (0, "HALON-SP-MIB", "statKey2Index"), (0, "HALON-SP-MIB", "statKey3Index"))
if mibBuilder.loadTexts: statEntry.setStatus('current')
if mibBuilder.loadTexts: statEntry.setDescription('Statistic entry')
statKey1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey1Index.setStatus('current')
if mibBuilder.loadTexts: statKey1Index.setDescription('Key1')
statKey2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey2Index.setStatus('current')
if mibBuilder.loadTexts: statKey2Index.setDescription('Key2')
statKey3Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey3Index.setStatus('current')
if mibBuilder.loadTexts: statKey3Index.setDescription('Key3')
statCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statCount.setStatus('current')
if mibBuilder.loadTexts: statCount.setDescription('Counter value')
statCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statCreated.setStatus('current')
if mibBuilder.loadTexts: statCreated.setDescription('Unix timestamp when created')
statUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statUpdated.setStatus('current')
if mibBuilder.loadTexts: statUpdated.setDescription('Unix timestamp when last updated')
mibBuilder.exportSymbols("HALON-SP-MIB", configurationRevision=configurationRevision, serialNumber=serialNumber, statUpdated=statUpdated, PYSNMP_MODULE_ID=halonSecuritySP, statKey2Index=statKey2Index, halonSecuritySP=halonSecuritySP, statKey1Index=statKey1Index, statCount=statCount, statTable=statTable, mailQueueLength=mailQueueLength, halonSecuritySPObjects=halonSecuritySPObjects, statEntry=statEntry, halonSecurity=halonSecurity, statKey3Index=statKey3Index, quarantinedMessages=quarantinedMessages, statCreated=statCreated, halonSecurityProducts=halonSecurityProducts)
