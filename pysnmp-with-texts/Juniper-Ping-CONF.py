#
# PySNMP MIB module Juniper-Ping-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Ping-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Integer32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, ObjectIdentity, iso, TimeTicks, MibIdentifier, Gauge32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "ObjectIdentity", "iso", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPingAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30))
juniPingAgent.setRevisions(('2002-09-06 16:54', '2001-03-29 14:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPingAgent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniPingAgent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniPingAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPingAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniPingAgent.setDescription('The agent capabilities definitions for the Ping component of the SNMP agent in the Juniper E-series family of products.')
juniPingAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 30, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPingAgentV1 = juniPingAgentV1.setProductRelease('Version 1 of the Ping component of the JUNOSe SNMP agent.  This version\n        of the Ping component is supported in JUNOSe 3.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPingAgentV1 = juniPingAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniPingAgentV1.setDescription('The MIB supported by the SNMP agent for the Ping application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Ping-CONF", juniPingAgentV1=juniPingAgentV1, PYSNMP_MODULE_ID=juniPingAgent, juniPingAgent=juniPingAgent)
