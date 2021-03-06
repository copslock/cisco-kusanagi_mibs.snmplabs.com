#
# PySNMP MIB module PGP-UNIVERSAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PGP-UNIVERSAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
products, = mibBuilder.importSymbols("PGP-SMI", "products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Unsigned32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Counter64, ModuleIdentity, IpAddress, Bits, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Unsigned32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Counter64", "ModuleIdentity", "IpAddress", "Bits", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pgpuniversal = ModuleIdentity((1, 3, 6, 1, 4, 1, 17766, 1, 1))
pgpuniversal.setRevisions(('2004-12-08 00:00',))
if mibBuilder.loadTexts: pgpuniversal.setLastUpdated('200412080000Z')
if mibBuilder.loadTexts: pgpuniversal.setOrganization('PGP Corporation')
messaging = ObjectIdentity((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1))
if mibBuilder.loadTexts: messaging.setStatus('current')
messagesProcessedToday = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messagesProcessedToday.setStatus('current')
messagesEncryptedToday = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messagesEncryptedToday.setStatus('current')
messagesDecryptedToday = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messagesDecryptedToday.setStatus('current')
messagesProcessedTotal = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messagesProcessedTotal.setStatus('current')
messagesEncryptedTotal = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messagesEncryptedTotal.setStatus('current')
messagesDecryptedTotal = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messagesDecryptedTotal.setStatus('current')
virusesFoundToday = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virusesFoundToday.setStatus('current')
messagesInQueue = MibScalar((1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messagesInQueue.setStatus('current')
mibBuilder.exportSymbols("PGP-UNIVERSAL-MIB", messagesDecryptedTotal=messagesDecryptedTotal, pgpuniversal=pgpuniversal, messagesProcessedToday=messagesProcessedToday, messagesEncryptedToday=messagesEncryptedToday, messagesDecryptedToday=messagesDecryptedToday, messaging=messaging, messagesInQueue=messagesInQueue, PYSNMP_MODULE_ID=pgpuniversal, messagesEncryptedTotal=messagesEncryptedTotal, messagesProcessedTotal=messagesProcessedTotal, virusesFoundToday=virusesFoundToday)
