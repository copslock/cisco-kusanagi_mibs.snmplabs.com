#
# PySNMP MIB module ACMEPACKET-PRODUCTS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACMEPACKET-PRODUCTS
# Produced by pysmi-0.3.4 at Mon Apr 29 16:57:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacket, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacket")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, iso, Integer32, Counter64, Unsigned32, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "iso", "Integer32", "Counter64", "Unsigned32", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acmepacketProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 1))
acmepacketProducts.setRevisions(('2012-07-16 00:00', '2007-04-03 15:00',))
if mibBuilder.loadTexts: acmepacketProducts.setLastUpdated('201207160000Z')
if mibBuilder.loadTexts: acmepacketProducts.setOrganization('Acme Packet, Inc.')
apNetNet4000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 1))
if mibBuilder.loadTexts: apNetNet4000Series.setStatus('current')
apNetNet4250 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 1, 1))
if mibBuilder.loadTexts: apNetNet4250.setStatus('current')
apNetNet4500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 1, 2))
if mibBuilder.loadTexts: apNetNet4500.setStatus('current')
apNetNet9000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 2))
if mibBuilder.loadTexts: apNetNet9000Series.setStatus('current')
apNetNet9200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 2, 1))
if mibBuilder.loadTexts: apNetNet9200.setStatus('current')
apNetNet3000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 3))
if mibBuilder.loadTexts: apNetNet3000Series.setStatus('current')
apNetNet3800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 3, 1))
if mibBuilder.loadTexts: apNetNet3800.setStatus('current')
apNetNet3820 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 3, 2))
if mibBuilder.loadTexts: apNetNet3820.setStatus('current')
apNetNetOSSeries = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 4))
if mibBuilder.loadTexts: apNetNetOSSeries.setStatus('current')
apNetNetOS = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 4, 1))
if mibBuilder.loadTexts: apNetNetOS.setStatus('current')
apNetNetOSVM = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 4, 2))
if mibBuilder.loadTexts: apNetNetOSVM.setStatus('current')
apNetNet6000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 5))
if mibBuilder.loadTexts: apNetNet6000Series.setStatus('current')
apNetNet6300 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 5, 1))
if mibBuilder.loadTexts: apNetNet6300.setStatus('current')
mibBuilder.exportSymbols("ACMEPACKET-PRODUCTS", apNetNet9000Series=apNetNet9000Series, apNetNet3820=apNetNet3820, apNetNet4500=apNetNet4500, apNetNet3000Series=apNetNet3000Series, apNetNet4250=apNetNet4250, apNetNetOSVM=apNetNetOSVM, PYSNMP_MODULE_ID=acmepacketProducts, apNetNet4000Series=apNetNet4000Series, apNetNet6000Series=apNetNet6000Series, apNetNet9200=apNetNet9200, acmepacketProducts=acmepacketProducts, apNetNetOS=apNetNetOS, apNetNet6300=apNetNet6300, apNetNet3800=apNetNet3800, apNetNetOSSeries=apNetNetOSSeries)
