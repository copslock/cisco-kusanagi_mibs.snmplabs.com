#
# PySNMP MIB module NOKIAVPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIAVPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
nokiaVPN, = mibBuilder.importSymbols("NOKIA-OID-REGISTRATION-MIB", "nokiaVPN")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, Bits, Unsigned32, TimeTicks, enterprises, Gauge32, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Counter64, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "Bits", "Unsigned32", "TimeTicks", "enterprises", "Gauge32", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter64", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nokiaVPNProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1))
if mibBuilder.loadTexts: nokiaVPNProducts.setStatus('current')
nokiaVPNMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2))
if mibBuilder.loadTexts: nokiaVPNMgmt.setStatus('current')
nokiaVPNExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 3))
if mibBuilder.loadTexts: nokiaVPNExperiment.setStatus('current')
nokiaVPNAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 4))
if mibBuilder.loadTexts: nokiaVPNAdmin.setStatus('current')
nokiaVPNModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 5))
if mibBuilder.loadTexts: nokiaVPNModules.setStatus('current')
nokiaVPNTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 6))
if mibBuilder.loadTexts: nokiaVPNTraps.setStatus('current')
ipsec = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1))
if mibBuilder.loadTexts: ipsec.setStatus('current')
vpn = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2))
if mibBuilder.loadTexts: vpn.setStatus('current')
config = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3))
if mibBuilder.loadTexts: config.setStatus('current')
nokiaHardwareUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 1))
if mibBuilder.loadTexts: nokiaHardwareUnknown.setStatus('current')
nokiaCryptoCluster500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 4))
if mibBuilder.loadTexts: nokiaCryptoCluster500.setStatus('current')
nokiaCryptoCluster5010 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 5))
if mibBuilder.loadTexts: nokiaCryptoCluster5010.setStatus('current')
nokiaCryptoCluster501 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 8))
if mibBuilder.loadTexts: nokiaCryptoCluster501.setStatus('current')
nokiaCryptoCluster5000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 10))
if mibBuilder.loadTexts: nokiaCryptoCluster5000.setStatus('current')
nokiaCryptoCluster2500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 11))
if mibBuilder.loadTexts: nokiaCryptoCluster2500.setStatus('current')
nokiaCryptoCluster2501 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 12))
if mibBuilder.loadTexts: nokiaCryptoCluster2501.setStatus('current')
nokiaCryptoCluster5200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 15))
if mibBuilder.loadTexts: nokiaCryptoCluster5200.setStatus('current')
nokiaCryptoCluster5205 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 16))
if mibBuilder.loadTexts: nokiaCryptoCluster5205.setStatus('current')
nokiaCA200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 18))
if mibBuilder.loadTexts: nokiaCA200.setStatus('current')
nokiaCA600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 19))
if mibBuilder.loadTexts: nokiaCA600.setStatus('current')
nokiaCryptoCluster100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 20))
if mibBuilder.loadTexts: nokiaCryptoCluster100.setStatus('current')
mibBuilder.exportSymbols("NOKIAVPN-MIB", nokiaVPNProducts=nokiaVPNProducts, nokiaCryptoCluster5205=nokiaCryptoCluster5205, nokiaCryptoCluster2501=nokiaCryptoCluster2501, nokiaCryptoCluster100=nokiaCryptoCluster100, config=config, nokiaVPNExperiment=nokiaVPNExperiment, vpn=vpn, nokiaVPNTraps=nokiaVPNTraps, nokiaCryptoCluster5200=nokiaCryptoCluster5200, nokiaVPNAdmin=nokiaVPNAdmin, nokiaVPNModules=nokiaVPNModules, nokiaCryptoCluster5010=nokiaCryptoCluster5010, ipsec=ipsec, nokiaCryptoCluster500=nokiaCryptoCluster500, nokiaCryptoCluster5000=nokiaCryptoCluster5000, nokiaCA200=nokiaCA200, nokiaVPNMgmt=nokiaVPNMgmt, nokiaHardwareUnknown=nokiaHardwareUnknown, nokiaCryptoCluster2500=nokiaCryptoCluster2500, nokiaCryptoCluster501=nokiaCryptoCluster501, nokiaCA600=nokiaCA600)