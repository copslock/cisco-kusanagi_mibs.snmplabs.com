#
# PySNMP MIB module MSIPRIP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSIPRIP2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:15:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
microsoft, software = mibBuilder.importSymbols("MSFT-MIB", "microsoft", "software")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, Unsigned32, Counter32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, iso, MibIdentifier, enterprises, ModuleIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Unsigned32", "Counter32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "iso", "MibIdentifier", "enterprises", "ModuleIdentity", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
msiprip2 = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 11))
pysmi_global = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 11, 1)).setLabel("global")
interface = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 11, 2))
peer = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 11, 3))
globalSystemRouteChanges = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalSystemRouteChanges.setStatus('mandatory')
if mibBuilder.loadTexts: globalSystemRouteChanges.setDescription('Number of changes RIP has made to the system routing tables.')
globalTotalResponseSends = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalTotalResponseSends.setStatus('mandatory')
if mibBuilder.loadTexts: globalTotalResponseSends.setDescription('Number of request messages for which responses have been sent.')
globalLoggingLevel = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("error", 2), ("warning", 3), ("information", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalLoggingLevel.setStatus('mandatory')
if mibBuilder.loadTexts: globalLoggingLevel.setDescription('Information logged can be None, Error only, Error + Warning, Error + Warn + Logging. This variable controls the amount of information logged')
globalMaxRecQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalMaxRecQueueSize.setStatus('mandatory')
if mibBuilder.loadTexts: globalMaxRecQueueSize.setDescription('Maximum size to use for queueing incoming packets.')
globalMaxSendQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalMaxSendQueueSize.setStatus('mandatory')
if mibBuilder.loadTexts: globalMaxSendQueueSize.setDescription('Maximum size to use for queueing outgoing packets.')
globalMinTriggeredUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 6), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalMinTriggeredUpdateInterval.setStatus('mandatory')
if mibBuilder.loadTexts: globalMinTriggeredUpdateInterval.setDescription('Minimum lag time before sending a triggered update. Used to consolidate updates to the route table and reduce number of updates sent.')
globalPeerFilterMode = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("include", 2), ("exclude", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalPeerFilterMode.setStatus('mandatory')
if mibBuilder.loadTexts: globalPeerFilterMode.setDescription('Controls the use of update messages from the list of peers in the peer filter table. If set to include routes will be only be accepted if they are from the routers in the peer array. If set to exclude routes will be rejected that come from the routers whose addresses are in the peer array, and all other routers will be accepted.')
globalPeerFilterCount = MibScalar((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalPeerFilterCount.setStatus('mandatory')
if mibBuilder.loadTexts: globalPeerFilterCount.setDescription('Number of entries in the peer filter table')
globalPeerFilterTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9), )
if mibBuilder.loadTexts: globalPeerFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: globalPeerFilterTable.setDescription('Table of peer routers communicating with this router via RIP')
globalPeerFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "globalPFAddr"))
if mibBuilder.loadTexts: globalPeerFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: globalPeerFilterEntry.setDescription('Peer router entry. Contains the IP address of peer router')
globalPFAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalPFAddr.setStatus('mandatory')
if mibBuilder.loadTexts: globalPFAddr.setDescription('IP Address of peer router')
globalPFTag = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: globalPFTag.setStatus('mandatory')
if mibBuilder.loadTexts: globalPFTag.setDescription('create : Creates an entry in the Global Peer Filter table delete : Deletes an entry in the Global Peer Filter table ')
ifStatsTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1), )
if mibBuilder.loadTexts: ifStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifStatsTable.setDescription('Table of RIP statistics for interfaces')
ifStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifSEIndex"))
if mibBuilder.loadTexts: ifStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifStatsEntry.setDescription('RIP interface statistics entry. Each entry contains counts of send/receive failures, requests/resposes sent/received, bad packets/entries reveived and triggered updates sent')
ifSEIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifSEIndex.setDescription('Index for the RIP interface Statistics table')
ifSEState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("bound", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEState.setStatus('mandatory')
if mibBuilder.loadTexts: ifSEState.setDescription('Current state of RIP on this interface.')
ifSESendFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSESendFailures.setStatus('mandatory')
if mibBuilder.loadTexts: ifSESendFailures.setDescription('Number of times a failure occurred while attempting to send a packet on this interface.')
ifSEReceiveFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEReceiveFailures.setStatus('mandatory')
if mibBuilder.loadTexts: ifSEReceiveFailures.setDescription('Number of times a failure occurred while attempting to receive a packet on this interface.')
ifSERequestSends = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSERequestSends.setStatus('mandatory')
if mibBuilder.loadTexts: ifSERequestSends.setDescription('Number of RIP REQUEST packets sent on this interface.')
ifSERequestReceiveds = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSERequestReceiveds.setStatus('mandatory')
if mibBuilder.loadTexts: ifSERequestReceiveds.setDescription('Number of RIP REQUEST packets received on this interface.')
ifSEResponseSends = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEResponseSends.setStatus('mandatory')
if mibBuilder.loadTexts: ifSEResponseSends.setDescription('Number of RIP RESPONSE packets sent on this interface.')
ifSEResponseReceiveds = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEResponseReceiveds.setStatus('mandatory')
if mibBuilder.loadTexts: ifSEResponseReceiveds.setDescription('Number of RIP RESPONSE packets received on this interface.')
ifSEBadResponsePacketReceiveds = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEBadResponsePacketReceiveds.setStatus('mandatory')
if mibBuilder.loadTexts: ifSEBadResponsePacketReceiveds.setDescription('Number of RIP RESPONSE packets discarded due to errors in the header.')
ifSEBadResponseEntriesReceiveds = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSEBadResponseEntriesReceiveds.setStatus('mandatory')
if mibBuilder.loadTexts: ifSEBadResponseEntriesReceiveds.setDescription('Number of RIP RESPONSE routes ignored due to errors in the entry.')
ifSETriggeredUpdateSends = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSETriggeredUpdateSends.setStatus('mandatory')
if mibBuilder.loadTexts: ifSETriggeredUpdateSends.setDescription('Count of triggered updates sent. ')
ifConfigTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2), )
if mibBuilder.loadTexts: ifConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifConfigTable.setDescription('RIP Interface configuration table. List of subnets that require separate configuration in RIP.')
ifConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifCEIndex"))
if mibBuilder.loadTexts: ifConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifConfigEntry.setDescription('RIP configuration entry for an interface. A single routing domain in a single subnet.')
ifCEIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCEIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEIndex.setDescription('Index for RIP interface config. table.')
ifCEState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("bound", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCEState.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEState.setDescription('Current state of RIP on this interface.')
ifCEMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEMetric.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEMetric.setDescription('Metric for the network connected to this interface.')
ifCEUpdateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("periodic", 1), ("demand", 2))).clone('periodic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEUpdateMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEUpdateMode.setDescription('Mode for sending update messages. If set to periodic, then messages are sent based on the value of ifCEFullUpdateInterval. Otherwise update messages are sent only on demand.')
ifCEAcceptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disable", 1), ("rip1", 2), ("rip1Compat", 3), ("rip2", 4))).clone('rip1Compat')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAcceptMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAcceptMode.setDescription('Specifies the type of RIP messages that will be accepted by this router disable : No RIP messages wil be accepted rip1 : Only RIP-1 messages will be accepted rip1Compat : Both RIP-1 and RIP-2 messages will be accepted rip2 : Only RIP-2 messages will be accepted')
ifCEAnnounceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disable", 1), ("rip1", 2), ("rip1Compat", 3), ("rip2", 4))).clone('rip1Compat')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAnnounceMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAnnounceMode.setDescription('Specifies the type of RIP messages that will be sent by this router. disable : No RIP messages wil be sent rip1 : Only RIP-1 messages will be sent in compliance with RFC 1058. rip1Compat : RIP-2 messages will be broadcast using RFC 1058 subsumption rules. rip2 : RIP-2 messages will be multicast')
ifCEProtocolFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 7), Integer32().clone(240)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEProtocolFlags.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEProtocolFlags.setDescription('Options for control of RIP operation. These options can be used in combination. Option value -------------------------------------------------- 1. ACCEPT_HOST_ROUTES 0x00000001 2. ANNOUNCE_HOST_ROUTES 0x00000002 3. ACCEPT_DEFAULT_ROUTES 0x00000004 4. ANNOUNCE_DEFAULT_ROUTES 0x00000008 5. SPLIT_HORIZON 0x00000010 6. POISON_REVERSE 0x00000020 7. GRACEFUL_SHUTDOWN 0x00000040 8. TRIGGERED_UPDATES 0x00000080 9. OVERWRITE_STATIC_ROUTES 0x00000100 ')
ifCERouteExpirationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 8), TimeTicks().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCERouteExpirationInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ifCERouteExpirationInterval.setDescription('Interval after which route is marked for deletion.')
ifCERouteRemovalInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 9), TimeTicks().clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCERouteRemovalInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ifCERouteRemovalInterval.setDescription('Interval after which a route marked for deletion is removed.')
ifCEFullUpdateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 10), TimeTicks().clone(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCEFullUpdateInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEFullUpdateInterval.setDescription('Interval between route table annoucements.')
ifCEAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuthentication", 1), ("simplePassword", 2), ("md5", 3))).clone('noAuthentication')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAuthenticationType.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAuthenticationType.setDescription('Type of authentication to be used on this interface.')
ifCEAuthenticationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAuthenticationKey.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAuthenticationKey.setDescription('The value to be used as the Authentication key whenever the corresponding instance of ifCEAuthenticationType has a value other than noAuthentication. A modification of the corresponding instance of ifCEAuthentiationType does not modify the ifCEAuthenticationKey value. If a string shorter than 16 octects is supplied, it will be left-justified and padded to 16 octects, on the right with nulls (0x00). Reading this object always results in an OCTET STRING of length zero; authentication may not be bypasssed by reading the MIB object')
ifCERouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCERouteTag.setStatus('mandatory')
if mibBuilder.loadTexts: ifCERouteTag.setDescription('Value inserted into the Routing Domain field of all RIP packets sent on this interface.')
ifCEUnicastPeerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("peerAlso", 2), ("peerOnly", 3))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEUnicastPeerMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEUnicastPeerMode.setDescription('Determines the unicast behavior when route update messages are sent. If set to peerAlso, updates are sent to those peers in the RIP unicast peer table corresponding to this interace as well as being sent via broadcast/multicast. If set to peerOnly, updates are sent only those peers listed in in the RIP Unicast peer table corresponding to this interface.')
ifCEAcceptFilterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("include", 2), ("exclude", 3))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAcceptFilterMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAcceptFilterMode.setDescription('Determines the accept behaviour of the RIP router. If set to include the entries in the Accept Filter Table corresponding to this interface specify the routes to be included. All other routes are excluded. If set to exclude the entries in the Accept Filter Table corresponding to this interface specify the routes to be excluded.')
ifCEAnnounceFilterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("include", 2), ("exclude", 3))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAnnounceFilterMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAnnounceFilterMode.setDescription('Determines the annouce behaviour of the RIP router. If set to include the entries in the Announce Filter Table corresponding to this interface specify the routes to be included. All other routes are excluded. If set to exclude the entries in the Announce Filter Table corresponding to this interface specify the routes to be excluded.')
ifCEUnicastPeerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEUnicastPeerCount.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEUnicastPeerCount.setDescription('Number of entries in the Unicast Peer Table corresponding to this interface entry.')
ifCEAcceptFilterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAcceptFilterCount.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAcceptFilterCount.setDescription('Number of entries in the Accept Filter Table corresponding to this interface entry.')
ifCEAnnounceFilterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCEAnnounceFilterCount.setStatus('mandatory')
if mibBuilder.loadTexts: ifCEAnnounceFilterCount.setDescription('Number of entries in the Announce Filter Table corresponding to this interface entry.')
ifUnicastPeersTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3), )
if mibBuilder.loadTexts: ifUnicastPeersTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifUnicastPeersTable.setDescription('Table of the peers routers to which update messages need to be unicast')
ifUnicastPeersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifUPIfIndex"), (0, "MSIPRIP2-MIB", "ifUPAddress"))
if mibBuilder.loadTexts: ifUnicastPeersEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifUnicastPeersEntry.setDescription('Entry for a peer router for an interface')
ifUPIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifUPIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifUPIfIndex.setDescription('Interface index corresponding to the interface with which this peer router is associated.')
ifUPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifUPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifUPAddress.setDescription('IP Address of a peer router.')
ifUPTag = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifUPTag.setStatus('mandatory')
if mibBuilder.loadTexts: ifUPTag.setDescription('create : Creates an entry in the unicast peer table delete : Deletes an entry in the unicast peer table ')
ifAcceptRouteFilterTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4), )
if mibBuilder.loadTexts: ifAcceptRouteFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifAcceptRouteFilterTable.setDescription('Table of the route filters used to filter the set of routes accepted over an interface.')
ifAcceptRouteFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifAcceptRFIfIndex"), (0, "MSIPRIP2-MIB", "ifAcceptRFLoAddress"), (0, "MSIPRIP2-MIB", "ifAcceptRFHiAddress"), (0, "MSIPRIP2-MIB", "ifAcceptRFTag"))
if mibBuilder.loadTexts: ifAcceptRouteFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifAcceptRouteFilterEntry.setDescription('Entry for a route filter for an interface')
ifAcceptRFIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAcceptRFIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifAcceptRFIfIndex.setDescription('Interface index corresponding to the interface to which this route filter entry corresponds')
ifAcceptRFLoAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAcceptRFLoAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifAcceptRFLoAddress.setDescription('Lowest address in the range of routes covered by this filter.')
ifAcceptRFHiAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAcceptRFHiAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifAcceptRFHiAddress.setDescription('Higher address in the range routes covered by this filter.')
ifAcceptRFTag = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAcceptRFTag.setStatus('mandatory')
if mibBuilder.loadTexts: ifAcceptRFTag.setDescription('create : Creates an entry in the Accept Route Filter table delete : Deletes an entry in the Accept Route Filter table ')
ifAnnounceRouteFilterTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5), )
if mibBuilder.loadTexts: ifAnnounceRouteFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifAnnounceRouteFilterTable.setDescription('Table of the route filters used to filter the set of routes annouced over an interface.')
ifAnnounceRouteFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifAnnounceRFIfIndex"), (0, "MSIPRIP2-MIB", "ifAnnounceRFLoAddress"), (0, "MSIPRIP2-MIB", "ifAnnounceRFHiAddress"))
if mibBuilder.loadTexts: ifAnnounceRouteFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifAnnounceRouteFilterEntry.setDescription('Entry for a route filter for an interface.')
ifAnnounceRFIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAnnounceRFIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifAnnounceRFIfIndex.setDescription('Interface index corresponding to the interface to which this route filter entry corresponds')
ifAnnounceRFLoAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAnnounceRFLoAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifAnnounceRFLoAddress.setDescription('Lowest address in the range of routes covered by this filter.')
ifAnnounceRFHiAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAnnounceRFHiAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifAnnounceRFHiAddress.setDescription('Higher address in the range routes covered by this filter.')
ifAnnounceRFTag = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAnnounceRFTag.setStatus('mandatory')
if mibBuilder.loadTexts: ifAnnounceRFTag.setDescription('create : Creates an entry in the Announce Route Filter table delete : Deletes an entry in the Announce Route Filter table ')
ifBindingTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6), )
if mibBuilder.loadTexts: ifBindingTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifBindingTable.setDescription('Table containing binding information for each interface.')
ifBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifBindingIndex"))
if mibBuilder.loadTexts: ifBindingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifBindingEntry.setDescription('Binding information entry for an interface')
ifBindingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBindingIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifBindingIndex.setDescription('Index corresponding to an interface entry in the binding table')
ifBindingState = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("bound", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBindingState.setStatus('mandatory')
if mibBuilder.loadTexts: ifBindingState.setDescription('State of the interface binding')
ifBindingCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBindingCounts.setStatus('mandatory')
if mibBuilder.loadTexts: ifBindingCounts.setDescription('Number of IP address bound to this interface. This is also the number of entries in the Interface Address Table corresponding to this interface.')
ifAddressTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7), )
if mibBuilder.loadTexts: ifAddressTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifAddressTable.setDescription('Table of IP addresses bound to interfaces')
ifAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifAEIfIndex"), (0, "MSIPRIP2-MIB", "ifAEAddress"), (0, "MSIPRIP2-MIB", "ifAEMask"))
if mibBuilder.loadTexts: ifAddressEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifAddressEntry.setDescription('Entry for an IP address for an interface')
ifAEIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAEIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifAEIfIndex.setDescription('Index corresponding to the Interface with which this entry is associated.')
ifAEAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAEAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifAEAddress.setDescription('Ip address bound to the associated interface.')
ifAEMask = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAEMask.setStatus('mandatory')
if mibBuilder.loadTexts: ifAEMask.setDescription('Address Mask associated with the IP address contained in the corresponding ifAEAddress field.')
ifPeerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1), )
if mibBuilder.loadTexts: ifPeerStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifPeerStatsTable.setDescription('Table of peer router statistics')
ifPeerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1), ).setIndexNames((0, "MSIPRIP2-MIB", "ifPSAddress"))
if mibBuilder.loadTexts: ifPeerStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifPeerStatsEntry.setDescription('Entry corresponding to a peer router.')
ifPSAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPSAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifPSAddress.setDescription('IP Address that the peer is using as its source address.')
ifPSLastPeerRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPSLastPeerRouteTag.setStatus('mandatory')
if mibBuilder.loadTexts: ifPSLastPeerRouteTag.setDescription('The route-tag of the last route in the last RIP RESPONSE received from this peer.')
ifPSLastPeerUpdateTickCount = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPSLastPeerUpdateTickCount.setStatus('mandatory')
if mibBuilder.loadTexts: ifPSLastPeerUpdateTickCount.setDescription('The tick-count in milliseconds at the time of the last RIP RESPONSE received from this peer.')
ifPSLastPeerUpdateVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPSLastPeerUpdateVersion.setStatus('mandatory')
if mibBuilder.loadTexts: ifPSLastPeerUpdateVersion.setDescription('The update version of the last RIP RESPONSE received from this peer.')
ifPSPeerBadResponsePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPSPeerBadResponsePackets.setStatus('mandatory')
if mibBuilder.loadTexts: ifPSPeerBadResponsePackets.setDescription('The number of RIP RESPONSE packets which were received from this peer and subsequently discarded.')
ifPSPeerBadResponseEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPSPeerBadResponseEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ifPSPeerBadResponseEntries.setDescription('The number of routes in RIP RESPONSE packets which were received from this peer and subsequently discarded.')
mibBuilder.exportSymbols("MSIPRIP2-MIB", ifCEAuthenticationKey=ifCEAuthenticationKey, ifAcceptRFHiAddress=ifAcceptRFHiAddress, ifAcceptRFIfIndex=ifAcceptRFIfIndex, ifPSAddress=ifPSAddress, ifUPTag=ifUPTag, ifAcceptRouteFilterEntry=ifAcceptRouteFilterEntry, ifPeerStatsEntry=ifPeerStatsEntry, ifBindingTable=ifBindingTable, ifSEState=ifSEState, ifAcceptRouteFilterTable=ifAcceptRouteFilterTable, ifAcceptRFLoAddress=ifAcceptRFLoAddress, ifCEAnnounceMode=ifCEAnnounceMode, ifCERouteRemovalInterval=ifCERouteRemovalInterval, ifCEUnicastPeerCount=ifCEUnicastPeerCount, ifSEBadResponsePacketReceiveds=ifSEBadResponsePacketReceiveds, globalPeerFilterMode=globalPeerFilterMode, ifAnnounceRFLoAddress=ifAnnounceRFLoAddress, globalPFTag=globalPFTag, ifAcceptRFTag=ifAcceptRFTag, ifSEBadResponseEntriesReceiveds=ifSEBadResponseEntriesReceiveds, ifConfigEntry=ifConfigEntry, ifCEUnicastPeerMode=ifCEUnicastPeerMode, ifCEMetric=ifCEMetric, ifBindingIndex=ifBindingIndex, ifAnnounceRFIfIndex=ifAnnounceRFIfIndex, ifPSLastPeerUpdateTickCount=ifPSLastPeerUpdateTickCount, ifSERequestReceiveds=ifSERequestReceiveds, globalMinTriggeredUpdateInterval=globalMinTriggeredUpdateInterval, ifCERouteExpirationInterval=ifCERouteExpirationInterval, ifAEAddress=ifAEAddress, ifCEAnnounceFilterCount=ifCEAnnounceFilterCount, ifBindingEntry=ifBindingEntry, ifSEIndex=ifSEIndex, ifSETriggeredUpdateSends=ifSETriggeredUpdateSends, ifCEAcceptMode=ifCEAcceptMode, globalSystemRouteChanges=globalSystemRouteChanges, globalPeerFilterCount=globalPeerFilterCount, ifSEResponseSends=ifSEResponseSends, globalMaxSendQueueSize=globalMaxSendQueueSize, ifPSPeerBadResponseEntries=ifPSPeerBadResponseEntries, ifAnnounceRouteFilterEntry=ifAnnounceRouteFilterEntry, ifUPAddress=ifUPAddress, ifCERouteTag=ifCERouteTag, ifStatsEntry=ifStatsEntry, ifPeerStatsTable=ifPeerStatsTable, ifCEUpdateMode=ifCEUpdateMode, ifSESendFailures=ifSESendFailures, ifAddressEntry=ifAddressEntry, ifAnnounceRFHiAddress=ifAnnounceRFHiAddress, peer=peer, ifCEProtocolFlags=ifCEProtocolFlags, globalPeerFilterEntry=globalPeerFilterEntry, ifPSLastPeerUpdateVersion=ifPSLastPeerUpdateVersion, ifStatsTable=ifStatsTable, ifCEState=ifCEState, ifPSPeerBadResponsePackets=ifPSPeerBadResponsePackets, ifCEAuthenticationType=ifCEAuthenticationType, globalPeerFilterTable=globalPeerFilterTable, ifCEFullUpdateInterval=ifCEFullUpdateInterval, globalPFAddr=globalPFAddr, ifPSLastPeerRouteTag=ifPSLastPeerRouteTag, globalLoggingLevel=globalLoggingLevel, ifSEReceiveFailures=ifSEReceiveFailures, ifCEAnnounceFilterMode=ifCEAnnounceFilterMode, msiprip2=msiprip2, ifAEIfIndex=ifAEIfIndex, ifCEAcceptFilterCount=ifCEAcceptFilterCount, ifUnicastPeersEntry=ifUnicastPeersEntry, ifAnnounceRFTag=ifAnnounceRFTag, ifBindingState=ifBindingState, ifAddressTable=ifAddressTable, ifUnicastPeersTable=ifUnicastPeersTable, ifCEAcceptFilterMode=ifCEAcceptFilterMode, pysmi_global=pysmi_global, ifSEResponseReceiveds=ifSEResponseReceiveds, ifAnnounceRouteFilterTable=ifAnnounceRouteFilterTable, ifAEMask=ifAEMask, interface=interface, ifCEIndex=ifCEIndex, ifBindingCounts=ifBindingCounts, globalTotalResponseSends=globalTotalResponseSends, ifSERequestSends=ifSERequestSends, ifUPIfIndex=ifUPIfIndex, globalMaxRecQueueSize=globalMaxRecQueueSize, ifConfigTable=ifConfigTable)
