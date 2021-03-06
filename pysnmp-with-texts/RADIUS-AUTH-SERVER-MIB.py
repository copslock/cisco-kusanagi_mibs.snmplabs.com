#
# PySNMP MIB module RADIUS-AUTH-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADIUS-AUTH-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:44:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, NotificationType, ObjectIdentity, TimeTicks, Bits, Integer32, MibIdentifier, Gauge32, IpAddress, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "Bits", "Integer32", "MibIdentifier", "Gauge32", "IpAddress", "experimental")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
radiusAuthServMIB = ModuleIdentity((1, 3, 6, 1, 3, 79, 1, 1))
if mibBuilder.loadTexts: radiusAuthServMIB.setLastUpdated('9802121659Z')
if mibBuilder.loadTexts: radiusAuthServMIB.setOrganization('IETF RADIUS Working Group.')
if mibBuilder.loadTexts: radiusAuthServMIB.setContactInfo(' Glen Zorn Microsoft One Microsoft Way Redmond, WA 98052 US Phone: +1 425 703 1559 EMail: glennz@microsoft.com')
if mibBuilder.loadTexts: radiusAuthServMIB.setDescription('The MIB module for entities implementing the server side of the Remote Access Dialin User Service (RADIUS) authentication protocol.')
radius = ObjectIdentity((1, 3, 6, 1, 3, 79))
if mibBuilder.loadTexts: radius.setStatus('current')
if mibBuilder.loadTexts: radius.setDescription('The OID assigned to RADIUS MIB work by the IANA.')
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 3, 79, 1))
radiusAuthServMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 1))
radiusAuthServ = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 1, 1))
class RadiusTime(TextualConvention, Gauge32):
    description = 'RadiusTime values are 32-bit unsigned integers which measure time in seconds.'
    status = 'current'
    displayHint = '4d'

radiusAuthServIdent = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServIdent.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServIdent.setDescription("The implementation identification string for the RADIUS authentication server software in use on the system, for example; `FNS-2.1'")
radiusAuthServUpTime = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 2), RadiusTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServUpTime.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServUpTime.setDescription('If the server has a persistent state (e.g., a process), this value will be the time elapsed since it started. For software without persistent state, this value will be zero.')
radiusAuthServResetTime = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 3), RadiusTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServResetTime.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServResetTime.setDescription("If the server has a persistent state (e.g., a process) and supports a `reset' operation (e.g., can be told to re-read configuration files), this value will be the time elapsed since the last time the name server was `reset.' For software that does not have persistence or does not support a `reset' operation, this value will be zero.")
radiusAuthServConfigReset = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusAuthServConfigReset.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServConfigReset.setDescription('Status/action object to reinitialize any persistent server state. When set to reset(2), any persistent server state (such as a process) is reinitialized as if the server had just been started. This value will never be returned by a read operation. When read, one of the following values will be returned: other(1) - server in some unknown state; initializing(3) - server (re)initializing; running(4) - server currently running.')
radiusAuthServTotalAccessRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalAccessRequests.setDescription('The total number of RADIUS Access-Request packets received since server start-up.')
radiusAuthServTotalInvalidRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalInvalidRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalInvalidRequests.setDescription('The total number of RADIUS Access-Request packets received from unknown addresses since server start-up.')
radiusAuthServTotalDupAccessRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalDupAccessRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalDupAccessRequests.setDescription('The total number of duplicate RADIUS Access-Request packets received since server start-up.')
radiusAuthServTotalAccessAccepts = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessAccepts.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalAccessAccepts.setDescription('The total number of RADIUS Access-Accept packets sent since server start-up.')
radiusAuthServTotalAccessRejects = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessRejects.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalAccessRejects.setDescription('The total number of RADIUS Access-Reject packets sent since server start-up.')
radiusAuthServTotalAccessChallenges = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalAccessChallenges.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalAccessChallenges.setDescription('The total number of RADIUS Access-Challenge packets sent since server start-up.')
radiusAuthServTotalMalformedAccessRequests = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalMalformedAccessRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalMalformedAccessRequests.setDescription('The total number of malformed RADIUS Access-Request packets received since server start-up. Bad authenticators are not included as malformed Access-Requests.')
radiusAuthServTotalBadAuthenticators = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalBadAuthenticators.setDescription('The total number of RADIUS Authentication-Request packets which contained invalid Signature attributes received since server start-up.')
radiusAuthServTotalPacketsDropped = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalPacketsDropped.setDescription('The total number of packets dropped with no reply sent.')
radiusAuthServTotalUnknownType = MibScalar((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServTotalUnknownType.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServTotalUnknownType.setDescription('The total number of RADIUS packets of unknown type which were received since server start-up.')
radiusAuthClientTable = MibTable((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15), )
if mibBuilder.loadTexts: radiusAuthClientTable.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientTable.setDescription('The (conceptual) table listing the RADIUS authentication clients with which the server shares a secret.')
radiusAuthClientEntry = MibTableRow((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1), ).setIndexNames((0, "RADIUS-AUTH-SERVER-MIB", "radiusAuthClientIndex"))
if mibBuilder.loadTexts: radiusAuthClientEntry.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientEntry.setDescription('An entry (conceptual row) representing a RADIUS authentication client with which the server shares a secret.')
radiusAuthClientIndex = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 1), Integer32())
if mibBuilder.loadTexts: radiusAuthClientIndex.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientIndex.setDescription('A number uniquely identifying each RADIUS authentication client with which this server communicates.')
radiusAuthClientAddress = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAddress.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientAddress.setDescription('The NAS-IP-Address of the RADIUS authentication client referred to in this table entry.')
radiusAuthClientID = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientID.setStatus('current')
if mibBuilder.loadTexts: radiusAuthClientID.setDescription('The NAS-Identifier of the RADIUS authentication client referred to in this table entry. This is not necessarily the same as sysName in MIB II.')
radiusAuthServAccessRequests = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServAccessRequests.setDescription('The total number of RADIUS Access-Request packets received from this client since server start-up.')
radiusAuthServDupAccessRequests = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServDupAccessRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServDupAccessRequests.setDescription('The total number of duplicate RADIUS Access-Request packets received from this client since server start-up.')
radiusAuthServAccessAccepts = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessAccepts.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServAccessAccepts.setDescription('The total number of RADIUS Access-Accept packets sent to this client since server start-up.')
radiusAuthServAccessRejects = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessRejects.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServAccessRejects.setDescription('The total number of RADIUS Access-Reject packets sent to this client since server start-up.')
radiusAuthServAccessChallenges = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServAccessChallenges.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServAccessChallenges.setDescription('The total number of RADIUS Access-Challenge packets sent to this client since server start-up.')
radiusAuthServMalformedAccessRequests = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServMalformedAccessRequests.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServMalformedAccessRequests.setDescription('The total number of malformed RADIUS Access-Request packets received from this client since server start-up. Bad authenticators are not included as malformed Access-Requests.')
radiusAuthServBadAuthenticators = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServBadAuthenticators.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServBadAuthenticators.setDescription('The total number of RADIUS Authentication-Request packets which contained invalid Signature attributes received from this client since server start-up.')
radiusAuthServPacketsDropped = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServPacketsDropped.setDescription('The total number of packets dropped from this client, with no reply sent.')
radiusAuthServUnknownType = MibTableColumn((1, 3, 6, 1, 3, 79, 1, 1, 1, 1, 15, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServUnknownType.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServUnknownType.setDescription('The total number of RADIUS packets of unknown type which were received from this client since authentication server start-up.')
radiusAuthServMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 2))
radiusAuthServMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 2, 1))
radiusAuthServMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 79, 1, 1, 2, 2))
radiusAuthServMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 79, 1, 1, 2, 1, 1)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthServMIBCompliance = radiusAuthServMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServMIBCompliance.setDescription('The compliance statement for authentication servers implementing the RADIUS Authentication Server MIB.')
radiusAuthServMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 79, 1, 1, 2, 2, 1)).setObjects(("RADIUS-AUTH-SERVER-MIB", "radiusAuthServIdent"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUpTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServResetTime"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServConfigReset"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalInvalidRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServTotalUnknownType"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientAddress"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthClientID"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServDupAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessAccepts"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessRejects"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServAccessChallenges"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServMalformedAccessRequests"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServBadAuthenticators"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServPacketsDropped"), ("RADIUS-AUTH-SERVER-MIB", "radiusAuthServUnknownType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthServMIBGroup = radiusAuthServMIBGroup.setStatus('current')
if mibBuilder.loadTexts: radiusAuthServMIBGroup.setDescription('The collection of objects providing management of a RADIUS Authentication Server.')
mibBuilder.exportSymbols("RADIUS-AUTH-SERVER-MIB", radiusAuthServResetTime=radiusAuthServResetTime, radiusAuthServTotalBadAuthenticators=radiusAuthServTotalBadAuthenticators, RadiusTime=RadiusTime, radiusAuthClientIndex=radiusAuthClientIndex, radiusAuthServBadAuthenticators=radiusAuthServBadAuthenticators, radiusAuthClientID=radiusAuthClientID, radiusAuthServTotalInvalidRequests=radiusAuthServTotalInvalidRequests, radiusAuthServPacketsDropped=radiusAuthServPacketsDropped, radiusAuthServTotalUnknownType=radiusAuthServTotalUnknownType, radiusAuthServDupAccessRequests=radiusAuthServDupAccessRequests, radiusAuthServMIBObjects=radiusAuthServMIBObjects, radiusAuthServConfigReset=radiusAuthServConfigReset, radiusAuthServTotalAccessChallenges=radiusAuthServTotalAccessChallenges, radiusAuthServMIBConformance=radiusAuthServMIBConformance, radiusAuthServMalformedAccessRequests=radiusAuthServMalformedAccessRequests, radiusAuthServMIBCompliances=radiusAuthServMIBCompliances, radiusAuthServAccessAccepts=radiusAuthServAccessAccepts, radiusAuthServTotalMalformedAccessRequests=radiusAuthServTotalMalformedAccessRequests, radiusAuthClientAddress=radiusAuthClientAddress, radiusAuthServMIBCompliance=radiusAuthServMIBCompliance, radiusAuthServ=radiusAuthServ, radiusAuthServUnknownType=radiusAuthServUnknownType, radiusAuthServUpTime=radiusAuthServUpTime, radius=radius, radiusAuthServMIB=radiusAuthServMIB, radiusAuthServIdent=radiusAuthServIdent, radiusAuthClientTable=radiusAuthClientTable, radiusAuthServAccessChallenges=radiusAuthServAccessChallenges, radiusAuthServTotalAccessAccepts=radiusAuthServTotalAccessAccepts, radiusAuthServTotalAccessRejects=radiusAuthServTotalAccessRejects, radiusAuthServMIBGroups=radiusAuthServMIBGroups, radiusAuthServAccessRejects=radiusAuthServAccessRejects, radiusAuthServTotalPacketsDropped=radiusAuthServTotalPacketsDropped, radiusAuthServMIBGroup=radiusAuthServMIBGroup, radiusAuthClientEntry=radiusAuthClientEntry, PYSNMP_MODULE_ID=radiusAuthServMIB, radiusAuthServTotalAccessRequests=radiusAuthServTotalAccessRequests, radiusAuthServTotalDupAccessRequests=radiusAuthServTotalDupAccessRequests, radiusAuthentication=radiusAuthentication, radiusAuthServAccessRequests=radiusAuthServAccessRequests)
