#
# PySNMP MIB module CISCO-RFC1407-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RFC1407-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, MibIdentifier, Unsigned32, TimeTicks, iso, Counter32, Counter64, Gauge32, IpAddress, ModuleIdentity, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibIdentifier", "Unsigned32", "TimeTicks", "iso", "Counter32", "Counter64", "Gauge32", "IpAddress", "ModuleIdentity", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRFC1407Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1407Capability.setRevisions(('2001-08-17 00:00', '1996-06-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFC1407Capability.setRevisionsDescriptions(('Support SET operation for dsx3LoopbackConfig object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFC1407Capability.setLastUpdated('200108170000Z')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setDescription('Agent capabilities for RFC1407-MIB (DS3 MIB)')
ciscoRFC1407CapabilityV11R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setProductRelease('Cisco IOS 11.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1407CapabilityV11R02.setDescription('ds3 capabilities')
ciscoRFC1407CapabilityV122R12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1407CapabilityV122R12.setDescription('ds3 capabilities')
mibBuilder.exportSymbols("CISCO-RFC1407-CAPABILITY", ciscoRFC1407Capability=ciscoRFC1407Capability, ciscoRFC1407CapabilityV122R12=ciscoRFC1407CapabilityV122R12, PYSNMP_MODULE_ID=ciscoRFC1407Capability, ciscoRFC1407CapabilityV11R02=ciscoRFC1407CapabilityV11R02)
