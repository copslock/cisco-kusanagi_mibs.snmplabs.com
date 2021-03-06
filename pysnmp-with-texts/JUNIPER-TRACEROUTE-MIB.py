#
# PySNMP MIB module JUNIPER-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-TRACEROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Unsigned32, NotificationType, TimeTicks, Counter32, MibIdentifier, ObjectIdentity, Integer32, iso, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Unsigned32", "NotificationType", "TimeTicks", "Counter32", "MibIdentifier", "ObjectIdentity", "Integer32", "iso", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxTraceRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 8))
if mibBuilder.loadTexts: jnxTraceRouteMIB.setLastUpdated('200307182154Z')
if mibBuilder.loadTexts: jnxTraceRouteMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxTraceRouteMIB.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxTraceRouteMIB.setDescription("This is Juniper Networks' implementation of enterprise specific portions of traceRouteMib. Any data stored in this MIB has directly related entries in mib-2, traceRouteMIB.")
jnxTraceRouteObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1))
jnxTraceRouteCtlTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2), )
if mibBuilder.loadTexts: jnxTraceRouteCtlTable.setStatus('current')
if mibBuilder.loadTexts: jnxTraceRouteCtlTable.setDescription('Defines the jnxTraceRoute Control Table for providing enterprise specific options to the corresponding traceRouteCtlTable entry.')
jnxTraceRouteCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1), ).setIndexNames((0, "JUNIPER-TRACEROUTE-MIB", "jnxTRCtlOwnerIndex"), (0, "JUNIPER-TRACEROUTE-MIB", "jnxTRCtlTestName"))
if mibBuilder.loadTexts: jnxTraceRouteCtlEntry.setStatus('current')
if mibBuilder.loadTexts: jnxTraceRouteCtlEntry.setDescription('Defines an entry in the jnxTraceRouteCtlTable. The first index element, jnxTraceRouteCtlOwnerIndex, is of type SnmpAdminString, a textual convention that allows for use of the SNMPv3 View-Based Access Control Model (RFC 2575 [11], VACM) and allows an management application to identify its entries. The second index, jnxTraceRouteCtlTestName (also an SnmpAdminString), enables the same management application to have multiple outstanding requests. Entries are created in the traceRouteCtlTable and mirrored here.')
jnxTRCtlOwnerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: jnxTRCtlOwnerIndex.setStatus('current')
if mibBuilder.loadTexts: jnxTRCtlOwnerIndex.setDescription("To facilitate the provisioning of access control by a security administrator using the View-Based Access Control Model (RFC 2575, VACM) for tables in which multiple users may need to independently create or modify entries, the initial index is used as an 'owner index'. Such an initial index has a syntax of SnmpAdminString, and can thus be trivially mapped to a securityName or groupName as defined in VACM, in accordance with a security policy. When used in conjunction with such a security policy all entries in the table belonging to a particular user (or group) will have the same value for this initial index. For a given user's entries in a particular table, the object identifiers for the information in these entries will have the same subidentifiers (except for the 'column' subidentifier) up to the end of the encoded owner index. To configure VACM to permit access to this portion of the table, one would create vacmViewTreeFamilyTable entries with the value of vacmViewTreeFamilySubtree including the owner index portion, and vacmViewTreeFamilyMask 'wildcarding' the column subidentifier. More elaborate configurations are possible.")
jnxTRCtlTestName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: jnxTRCtlTestName.setStatus('current')
if mibBuilder.loadTexts: jnxTRCtlTestName.setDescription('The name of the traceRoute test. This is locally unique, within the scope of an traceRouteCtlOwnerIndex.')
jnxTRCtlIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: jnxTRCtlIfName.setStatus('current')
if mibBuilder.loadTexts: jnxTRCtlIfName.setDescription('Setting this object to an interface name prior to starting a remote traceRoute operation directs the traceRoute probes to be transmitted over the specified interface. To specify the interface index instead, see traceRouteCtlIfIndex. The interface name must be specified under interfaces statement of the JUNOS configuration. A zero length string value for this object means that this option is not enabled. The following values may be set simultaneously, however, only one value is used. The precedence order is a follows: traceRouteCtlIfIndex (see traceRouteCtlTable in traceRouteMIB) jnxTRCtlIfName jnxTRCtlRoutingInstanceName')
jnxTRCtlRoutingInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: jnxTRCtlRoutingInstanceName.setStatus('current')
if mibBuilder.loadTexts: jnxTRCtlRoutingInstanceName.setDescription('Use this option to specify the name of the routing instance used when directing outgoing traceRoute packets. The instance name specified must be configured under routing-instances of the JUNOS configuration.')
mibBuilder.exportSymbols("JUNIPER-TRACEROUTE-MIB", jnxTRCtlOwnerIndex=jnxTRCtlOwnerIndex, jnxTraceRouteCtlTable=jnxTraceRouteCtlTable, PYSNMP_MODULE_ID=jnxTraceRouteMIB, jnxTraceRouteObjects=jnxTraceRouteObjects, jnxTRCtlIfName=jnxTRCtlIfName, jnxTraceRouteCtlEntry=jnxTraceRouteCtlEntry, jnxTraceRouteMIB=jnxTraceRouteMIB, jnxTRCtlRoutingInstanceName=jnxTRCtlRoutingInstanceName, jnxTRCtlTestName=jnxTRCtlTestName)
