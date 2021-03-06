#
# PySNMP MIB module CISCO-SWITCH-RATE-LIMITER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-RATE-LIMITER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:13:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, IpAddress, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, MibIdentifier, iso, TimeTicks, Bits, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "IpAddress", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "MibIdentifier", "iso", "TimeTicks", "Bits", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchRateLimiterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 773))
ciscoSwitchRateLimiterMIB.setRevisions(('2011-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchRateLimiterMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchRateLimiterMIB.setLastUpdated('201105160000Z')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterMIB.setDescription('This MIB module defines management objects for the Switch Rate Limiter features on Cisco Layer 2 and Layer 3 devices. Rate limits prevents redirected control packets for egress exceptions from overwhelming the supervisor module on a device.')
ciscoSwitchRateLimiterMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 0))
ciscoSwitchRateLimiterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1))
ciscoSwitchRateLimiterMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 2))
csrlRateLimiterInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1))
csrlGlobalRateLimiter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2))
csrlLocalRateLimiter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3))
csrlRateLimiterClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1), )
if mibBuilder.loadTexts: csrlRateLimiterClassTable.setStatus('current')
if mibBuilder.loadTexts: csrlRateLimiterClassTable.setDescription('A table containing descriptions of the rate limiter classes supported by the device.')
csrlRateLimiterClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"))
if mibBuilder.loadTexts: csrlRateLimiterClassEntry.setStatus('current')
if mibBuilder.loadTexts: csrlRateLimiterClassEntry.setDescription('A conceptual row containing the description of a particular rate limiter class.')
csrlRateLimiterClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: csrlRateLimiterClassId.setStatus('current')
if mibBuilder.loadTexts: csrlRateLimiterClassId.setDescription('An arbitrary positive integer value that uniquely identifies a rate limiter class.')
csrlRateLimiterClassDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlRateLimiterClassDescr.setStatus('current')
if mibBuilder.loadTexts: csrlRateLimiterClassDescr.setDescription('This object indicates the description of the rate limiter class.')
csrlGlobalRateLimiterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1), )
if mibBuilder.loadTexts: csrlGlobalRateLimiterTable.setStatus('current')
if mibBuilder.loadTexts: csrlGlobalRateLimiterTable.setDescription('A table containing global configuration and statistics of rate limiter classes.')
csrlGlobalRateLimiterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"))
if mibBuilder.loadTexts: csrlGlobalRateLimiterEntry.setStatus('current')
if mibBuilder.loadTexts: csrlGlobalRateLimiterEntry.setDescription('A conceptual row containing global management information of a particular rate limiter class.')
csrlGlobalRateLimiterConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csrlGlobalRateLimiterConfigured.setStatus('current')
if mibBuilder.loadTexts: csrlGlobalRateLimiterConfigured.setDescription('This object specifies the global rate limit configured for this rate limiter class. The global rate limit for this class is applied to every entity which does not have its local rate limit of same class configured, the value of the corresponding csrlLocalRateLimiterConfigured is -2. A value of -1 indicates that the global rate limit for this rate limiter class is disabled. A value of 0 indicates that the system does not allow any packets for this rate limiter class to go through the supervisor.')
csrlGlobalRateLimiterAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 2), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlGlobalRateLimiterAllowed.setStatus('current')
if mibBuilder.loadTexts: csrlGlobalRateLimiterAllowed.setDescription('This object indicates the number of packets allowed globally for this rate limiter class. When the value of csrlGlobalRateLimiterConfigured is -1, the value of this object is always 0.')
csrlGlobalRateLimiterDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 3), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlGlobalRateLimiterDropped.setStatus('current')
if mibBuilder.loadTexts: csrlGlobalRateLimiterDropped.setDescription('This object indicates the number of packets which have been dropped globally for this rate limiter class. When the value of csrlGlobalRateLimiterConfigured is -1, the value of this object is always 0.')
csrlGlobalRateLimiterTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 4), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlGlobalRateLimiterTotal.setStatus('current')
if mibBuilder.loadTexts: csrlGlobalRateLimiterTotal.setDescription('This object indicates the total number of packets have been processed globally for this rate limiter class. When the value of csrlGlobalRateLimiterConfigured is -1, the value of this object is always 0.')
csrlLocalRateLimiterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1), )
if mibBuilder.loadTexts: csrlLocalRateLimiterTable.setStatus('current')
if mibBuilder.loadTexts: csrlLocalRateLimiterTable.setDescription('A table containing local rate limiter configuration and statistics for a specific entity. For Example: A module on the device. A set of rate limiter class entries are added to this table when a rate limiter capable entity comes online. The same set of entries are deleted from this table when the entity goes offline.')
csrlLocalRateLimiterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"))
if mibBuilder.loadTexts: csrlLocalRateLimiterEntry.setStatus('current')
if mibBuilder.loadTexts: csrlLocalRateLimiterEntry.setDescription('A conceptual row containing the local rate limiter management information for a particular rate limiter capable entity.')
csrlLocalRateLimiterConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csrlLocalRateLimiterConfigured.setStatus('current')
if mibBuilder.loadTexts: csrlLocalRateLimiterConfigured.setDescription('This object specifies the local rate limit configured for this rate limiter class on this entity. A value of -2 indicates that the entity does not have local rate limiter configured, and will pick up the configuration from csrlGlobalRateLimiterConfigured. A value of -1 indicates that this rate limiter class is disabled locally for this entity. A value of 0 indicates that the rate limiter does not allow any packets from this entity for this rate limiter class to go through the supervisor.')
csrlLocalRateLimiterAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 2), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlLocalRateLimiterAllowed.setStatus('current')
if mibBuilder.loadTexts: csrlLocalRateLimiterAllowed.setDescription('This object indicates the number of packets allowed on this entity for this rate limiter class. When the value of csrlLocalRateLimiterConfigured is -1, the value of this object is always 0.')
csrlLocalRateLimiterDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 3), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlLocalRateLimiterDropped.setStatus('current')
if mibBuilder.loadTexts: csrlLocalRateLimiterDropped.setDescription('This object indicates the number of packets dropped on this entity for this rate limiter class. When the value of csrlLocalRateLimiterConfigured is -1, the value of this object is always 0.')
csrlLocalRateLimiterTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 4), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: csrlLocalRateLimiterTotal.setStatus('current')
if mibBuilder.loadTexts: csrlLocalRateLimiterTotal.setDescription('This object indicates the number of packets processed on this entity for this rate limiter class. When the value of csrlLocalRateLimiterConfigured is -1, the value of this object is always 0.')
csrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 1))
csrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2))
csrlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 1, 1)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassGroup"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterGroup"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlMIBCompliance = csrlMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: csrlMIBCompliance.setDescription('The compliance statement for CISCO-SWITCH-RATE-LIMITER-MIB.my.')
csrlRateLimiterClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 1)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlRateLimiterClassGroup = csrlRateLimiterClassGroup.setStatus('current')
if mibBuilder.loadTexts: csrlRateLimiterClassGroup.setDescription('A collection of objects providing Rate Limiter Class information.')
csrlGlobalRateLimiterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 2)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterConfigured"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterAllowed"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterDropped"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlGlobalRateLimiterGroup = csrlGlobalRateLimiterGroup.setStatus('current')
if mibBuilder.loadTexts: csrlGlobalRateLimiterGroup.setDescription('A collection of objects providing global rate limiter information.')
csrlLocalRateLimiterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 3)).setObjects(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterConfigured"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterAllowed"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterDropped"), ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csrlLocalRateLimiterGroup = csrlLocalRateLimiterGroup.setStatus('current')
if mibBuilder.loadTexts: csrlLocalRateLimiterGroup.setDescription('A collection of objects providing local rate limiter information.')
mibBuilder.exportSymbols("CISCO-SWITCH-RATE-LIMITER-MIB", csrlRateLimiterClassDescr=csrlRateLimiterClassDescr, csrlGlobalRateLimiterConfigured=csrlGlobalRateLimiterConfigured, csrlMIBCompliances=csrlMIBCompliances, csrlRateLimiterClassId=csrlRateLimiterClassId, csrlLocalRateLimiter=csrlLocalRateLimiter, csrlRateLimiterClassEntry=csrlRateLimiterClassEntry, csrlLocalRateLimiterDropped=csrlLocalRateLimiterDropped, csrlRateLimiterInfo=csrlRateLimiterInfo, ciscoSwitchRateLimiterMIBNotifs=ciscoSwitchRateLimiterMIBNotifs, csrlGlobalRateLimiterDropped=csrlGlobalRateLimiterDropped, csrlGlobalRateLimiter=csrlGlobalRateLimiter, ciscoSwitchRateLimiterMIB=ciscoSwitchRateLimiterMIB, csrlLocalRateLimiterAllowed=csrlLocalRateLimiterAllowed, csrlGlobalRateLimiterTable=csrlGlobalRateLimiterTable, csrlGlobalRateLimiterEntry=csrlGlobalRateLimiterEntry, csrlGlobalRateLimiterTotal=csrlGlobalRateLimiterTotal, csrlMIBGroups=csrlMIBGroups, csrlMIBCompliance=csrlMIBCompliance, csrlLocalRateLimiterGroup=csrlLocalRateLimiterGroup, csrlLocalRateLimiterConfigured=csrlLocalRateLimiterConfigured, csrlLocalRateLimiterTotal=csrlLocalRateLimiterTotal, csrlLocalRateLimiterEntry=csrlLocalRateLimiterEntry, PYSNMP_MODULE_ID=ciscoSwitchRateLimiterMIB, csrlGlobalRateLimiterAllowed=csrlGlobalRateLimiterAllowed, csrlGlobalRateLimiterGroup=csrlGlobalRateLimiterGroup, csrlRateLimiterClassGroup=csrlRateLimiterClassGroup, ciscoSwitchRateLimiterMIBConform=ciscoSwitchRateLimiterMIBConform, ciscoSwitchRateLimiterMIBObjects=ciscoSwitchRateLimiterMIBObjects, csrlLocalRateLimiterTable=csrlLocalRateLimiterTable, csrlRateLimiterClassTable=csrlRateLimiterClassTable)
