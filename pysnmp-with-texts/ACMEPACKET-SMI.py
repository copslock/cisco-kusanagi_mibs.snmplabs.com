#
# PySNMP MIB module ACMEPACKET-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACMEPACKET-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:13:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, iso, enterprises, ObjectIdentity, Unsigned32, Bits, Counter32, Counter64, IpAddress, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "enterprises", "ObjectIdentity", "Unsigned32", "Bits", "Counter32", "Counter64", "IpAddress", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acmepacket = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148))
acmepacket.setRevisions(('2012-02-02 18:00', '2004-02-26 18:00', '2001-09-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acmepacket.setRevisionsDescriptions(('Updated new contact info.', 'The Structure of Management Information for the Acme Packet enterprise. Add acmepacketModules.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: acmepacket.setLastUpdated('201202021800Z')
if mibBuilder.loadTexts: acmepacket.setOrganization('Acme Packet, Inc.')
if mibBuilder.loadTexts: acmepacket.setContactInfo(' Customer Service Postal: Acme Packet, Inc 100 Crosby Drive Bedford, MA 01730 US Tel: 1-781-328-4400 E-mail: support@acmepacket.com')
if mibBuilder.loadTexts: acmepacket.setDescription('Structure of Managed Information for Acme Packet Inc.')
acmepacketProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1))
if mibBuilder.loadTexts: acmepacketProducts.setStatus('current')
if mibBuilder.loadTexts: acmepacketProducts.setDescription('acmepacketProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. This is reserved for future use.')
acmepacketAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 2))
if mibBuilder.loadTexts: acmepacketAgentCapability.setStatus('current')
if mibBuilder.loadTexts: acmepacketAgentCapability.setDescription('acmepacketAgentCapability provides a root object identifier from which AGENT-CAPABILITIES values may be assigned.')
acmepacketMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 3))
if mibBuilder.loadTexts: acmepacketMgmt.setStatus('current')
if mibBuilder.loadTexts: acmepacketMgmt.setDescription('acmepacketMgmt is the main subtree for the management.')
acmepacketConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 4))
if mibBuilder.loadTexts: acmepacketConfig.setStatus('current')
if mibBuilder.loadTexts: acmepacketConfig.setDescription('acmepacketConfig is the subtree for configuration mibs. This is reserved for future use.')
acmepacketExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 5))
if mibBuilder.loadTexts: acmepacketExperiment.setStatus('current')
if mibBuilder.loadTexts: acmepacketExperiment.setDescription('acmepacketExperiment provides a root object identifier from which experimental mibs may be temporarily based. support for mibs in the acmepacketExperiment subtree will be deleted when a permanent object identifier assignment is made. This is reserved for future use.')
acmepacketModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 6))
if mibBuilder.loadTexts: acmepacketModules.setStatus('current')
if mibBuilder.loadTexts: acmepacketModules.setDescription('acmepacketModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
mibBuilder.exportSymbols("ACMEPACKET-SMI", acmepacket=acmepacket, acmepacketModules=acmepacketModules, acmepacketMgmt=acmepacketMgmt, acmepacketProducts=acmepacketProducts, acmepacketConfig=acmepacketConfig, PYSNMP_MODULE_ID=acmepacket, acmepacketAgentCapability=acmepacketAgentCapability, acmepacketExperiment=acmepacketExperiment)
