#
# PySNMP MIB module DLINK-AUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-AUTH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:34:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
PaeControlledPortStatus, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "PaeControlledPortStatus")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, NotificationType, MibIdentifier, Unsigned32, Counter32, Counter64, Integer32, ModuleIdentity, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "NotificationType", "MibIdentifier", "Unsigned32", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "ObjectIdentity", "TimeTicks")
MacAddress, TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
swDlinkAuthCtrl = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 3))
if mibBuilder.loadTexts: swDlinkAuthCtrl.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swDlinkAuthCtrl.setOrganization('D-Link, Inc.')
swAuthCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 3, 1))
swRadiusCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 3, 2))
swRadiusAuthInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 3, 3))
swRadiusAccountingCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 3, 4))
swRadiusAccountingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 3, 5))
swMacAuthBaseStatsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 3, 6))
swRadiusCommand = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 3, 7))
authProtocol = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authProtocolRadiusEap", 1), ("authProtocolRadiusPap", 2))).clone('authProtocolRadiusEap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authProtocol.setStatus('current')
swAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("portBase", 1), ("macBase", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swAuthMode.setStatus('current')
swFakeAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFakeAuthentication.setStatus('current')
swRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4), )
if mibBuilder.loadTexts: swRadiusServerTable.setStatus('current')
swRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swRadiusServerIndex"))
if mibBuilder.loadTexts: swRadiusServerEntry.setStatus('current')
swRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("swRadiusServerIndex-first", 1), ("swRadiusServerIndex-second", 2), ("swRadiusServerIndex-third", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusServerIndex.setStatus('current')
swRadiusServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusServerIpAddr.setStatus('current')
swRadiusServerKey = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: swRadiusServerKey.setStatus('current')
swRadiusAuthPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 4), Unsigned32().clone(1812)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthPortNumber.setStatus('current')
swRadiusAcctPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 5), Unsigned32().clone(1813)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctPortNumber.setStatus('current')
swRadiusServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 6), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusServerStatus.setStatus('current')
swRadiusAuthClientIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientIdentifier.setStatus('obsolete')
swRadiusAuthClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientInvalidServerAddresses.setStatus('obsolete')
swRadiusAuthServerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3), )
if mibBuilder.loadTexts: swRadiusAuthServerTable.setStatus('obsolete')
swRadiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swRadiusAuthServerIndex"))
if mibBuilder.loadTexts: swRadiusAuthServerEntry.setStatus('obsolete')
swRadiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthServerIndex.setStatus('obsolete')
swRadiusAuthServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthServerAddress.setStatus('obsolete')
swRadiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 3), Unsigned32().clone(1812)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientServerPortNumber.setStatus('obsolete')
swRadiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientRoundTripTime.setStatus('obsolete')
swRadiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientAccessRequests.setStatus('obsolete')
swRadiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientAccessRetransmissions.setStatus('obsolete')
swRadiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientAccessAccepts.setStatus('obsolete')
swRadiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientAccessRejects.setStatus('obsolete')
swRadiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientAccessChallenges.setStatus('obsolete')
swRadiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientMalformedAccessResponses.setStatus('obsolete')
swRadiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientBadAuthenticators.setStatus('obsolete')
swRadiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientPendingRequests.setStatus('obsolete')
swRadiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientTimeouts.setStatus('obsolete')
swRadiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientUnknownTypes.setStatus('obsolete')
swRadiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAuthClientPacketsDropped.setStatus('obsolete')
swRadiusAcctUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRadiusAcctUpdateInterval.setStatus('current')
swRadiusAcctSuppressNullUserName = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRadiusAcctSuppressNullUserName.setStatus('current')
swRadiusAcctServiceTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3), )
if mibBuilder.loadTexts: swRadiusAcctServiceTable.setStatus('current')
swRadiusAcctServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swRadiusAcctServiceIndex"))
if mibBuilder.loadTexts: swRadiusAcctServiceEntry.setStatus('current')
swRadiusAcctServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("acctServiceIndex-network", 1), ("acctServiceIndex-exec", 2), ("acctServiceIndex-system", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctServiceIndex.setStatus('current')
swRadiusAcctServiceMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("swRadiusAcctServiceMethodNone", 1), ("swRadiusAcctServiceMethodRadius", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRadiusAcctServiceMethod.setStatus('current')
swRadiusAcctServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("radiusAcctServiceModeNone", 1), ("radiusAcctServiceModeStartStop", 2), ("radiusAcctServiceModeStopOnly", 3))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRadiusAcctServiceMode.setStatus('current')
swRadiusAcctClientIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientIdentifier.setStatus('obsolete')
swRadiusAcctClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientInvalidServerAddresses.setStatus('obsolete')
swRadiusAcctServerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3), )
if mibBuilder.loadTexts: swRadiusAcctServerTable.setStatus('obsolete')
swRadiusAcctServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swRadiusAcctServerIndex"))
if mibBuilder.loadTexts: swRadiusAcctServerEntry.setStatus('obsolete')
swRadiusAcctServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctServerIndex.setStatus('obsolete')
swRadiusAcctServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctServerAddress.setStatus('obsolete')
swRadiusAcctClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 3), Unsigned32().clone(1813)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientServerPortNumber.setStatus('obsolete')
swRadiusAcctClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientRoundTripTime.setStatus('obsolete')
swRadiusAcctClientRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientRequests.setStatus('obsolete')
swRadiusAcctClientRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientRetransmissions.setStatus('obsolete')
swRadiusAcctClientResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientResponses.setStatus('obsolete')
swRadiusAcctClientMalformedResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientMalformedResponses.setStatus('obsolete')
swRadiusAcctClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientBadAuthenticators.setStatus('obsolete')
swRadiusAcctClientPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientPendingRequests.setStatus('obsolete')
swRadiusAcctClientTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientTimeouts.setStatus('obsolete')
swRadiusAcctClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientUnknownTypes.setStatus('obsolete')
swRadiusAcctClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRadiusAcctClientPacketsDropped.setStatus('obsolete')
swMacAuthStateTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1), )
if mibBuilder.loadTexts: swMacAuthStateTable.setStatus('current')
swMacAuthStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swPaeMacAddr"), (0, "DLINK-AUTH-MIB", "swPaePortNumber"))
if mibBuilder.loadTexts: swMacAuthStateEntry.setStatus('current')
swPaeMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPaeMacAddr.setStatus('current')
swPaePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPaePortNumber.setStatus('current')
swAuthPaeState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthPaeState.setStatus('current')
swAuthBackendAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthBackendAuthState.setStatus('current')
swAuthAuthControlledPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 5), PaeControlledPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthControlledPortStatus.setStatus('current')
swMacAuthStatsTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2), )
if mibBuilder.loadTexts: swMacAuthStatsTable.setStatus('current')
swMacAuthStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swPaeMacAddr"), (0, "DLINK-AUTH-MIB", "swPaePortNumber"))
if mibBuilder.loadTexts: swMacAuthStatsEntry.setStatus('current')
swAuthEapolFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolFramesRx.setStatus('current')
swAuthEapolFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolFramesTx.setStatus('current')
swAuthEapolStartFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolStartFramesRx.setStatus('current')
swAuthEapolLogoffFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolLogoffFramesRx.setStatus('current')
swAuthEapolRespIdFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolRespIdFramesRx.setStatus('current')
swAuthEapolRespFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolRespFramesRx.setStatus('current')
swAuthEapolReqIdFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolReqIdFramesTx.setStatus('current')
swAuthEapolReqFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapolReqFramesTx.setStatus('current')
swAuthInvalidEapolFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthInvalidEapolFramesRx.setStatus('current')
swAuthEapLengthErrorFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapLengthErrorFramesRx.setStatus('current')
swAuthLastEapolFrameVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthLastEapolFrameVersion.setStatus('current')
swAuthLastEapolFrameSource = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthLastEapolFrameSource.setStatus('current')
swMacAuthDiagTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3), )
if mibBuilder.loadTexts: swMacAuthDiagTable.setStatus('current')
swMacAuthDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swPaeMacAddr"), (0, "DLINK-AUTH-MIB", "swPaePortNumber"))
if mibBuilder.loadTexts: swMacAuthDiagEntry.setStatus('current')
swAuthEntersConnecting = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEntersConnecting.setStatus('current')
swAuthEapLogoffsWhileConnecting = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEapLogoffsWhileConnecting.setStatus('current')
swAuthEntersAuthenticating = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthEntersAuthenticating.setStatus('current')
swAuthAuthSuccessWhileAuthenticating = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthSuccessWhileAuthenticating.setStatus('current')
swAuthAuthTimeoutsWhileAuthenticating = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthTimeoutsWhileAuthenticating.setStatus('current')
swAuthAuthFailWhileAuthenticating = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthFailWhileAuthenticating.setStatus('current')
swAuthAuthReauthsWhileAuthenticating = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthReauthsWhileAuthenticating.setStatus('current')
swAuthAuthEapStartsWhileAuthenticating = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthEapStartsWhileAuthenticating.setStatus('current')
swAuthAuthEapLogoffWhileAuthenticating = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthEapLogoffWhileAuthenticating.setStatus('current')
swAuthAuthReauthsWhileAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthReauthsWhileAuthenticated.setStatus('current')
swAuthAuthEapStartsWhileAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthEapStartsWhileAuthenticated.setStatus('current')
swAuthAuthEapLogoffWhileAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthAuthEapLogoffWhileAuthenticated.setStatus('current')
swAuthBackendResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthBackendResponses.setStatus('current')
swAuthBackendAccessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthBackendAccessChallenges.setStatus('current')
swAuthBackendOtherRequestsToSupplicant = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthBackendOtherRequestsToSupplicant.setStatus('current')
swAuthBackendNonNakResponsesFromSupplicant = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthBackendNonNakResponsesFromSupplicant.setStatus('current')
swAuthBackendAuthSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthBackendAuthSuccesses.setStatus('current')
swAuthBackendAuthFails = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthBackendAuthFails.setStatus('current')
swMacAuthSessionStatsTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4), )
if mibBuilder.loadTexts: swMacAuthSessionStatsTable.setStatus('current')
swMacAuthSessionStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1), ).setIndexNames((0, "DLINK-AUTH-MIB", "swPaeMacAddr"), (0, "DLINK-AUTH-MIB", "swPaePortNumber"))
if mibBuilder.loadTexts: swMacAuthSessionStatsEntry.setStatus('current')
swAuthSessionOctetsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionOctetsRx.setStatus('current')
swAuthSessionOctetsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionOctetsTx.setStatus('current')
swAuthSessionFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionFramesRx.setStatus('current')
swAuthSessionFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionFramesTx.setStatus('current')
swAuthSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionId.setStatus('current')
swAuthSessionAuthenticMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("remoteAuthServer", 1), ("localAuthServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionAuthenticMethod.setStatus('current')
swAuthSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionTime.setStatus('current')
swAuthSessionTerminateCause = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 999))).clone(namedValues=NamedValues(("supplicantLogoff", 1), ("portFailure", 2), ("supplicantRestart", 3), ("reauthFailed", 4), ("authControlForceUnauth", 5), ("portReInit", 6), ("portAdminDisabled", 7), ("notTerminatedYet", 999)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionTerminateCause.setStatus('current')
swAuthSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAuthSessionUserName.setStatus('current')
swRadiusForceDownPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 7, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRadiusForceDownPortNumber.setStatus('current')
swRadiusForceDownMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 3, 7, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRadiusForceDownMacAddr.setStatus('current')
mibBuilder.exportSymbols("DLINK-AUTH-MIB", swRadiusAcctServerTable=swRadiusAcctServerTable, swDlinkAuthCtrl=swDlinkAuthCtrl, swAuthBackendAuthFails=swAuthBackendAuthFails, swRadiusAuthClientAccessRequests=swRadiusAuthClientAccessRequests, swMacAuthStatsEntry=swMacAuthStatsEntry, swAuthSessionAuthenticMethod=swAuthSessionAuthenticMethod, swMacAuthStatsTable=swMacAuthStatsTable, swRadiusAuthServerAddress=swRadiusAuthServerAddress, swAuthEntersAuthenticating=swAuthEntersAuthenticating, swRadiusServerIpAddr=swRadiusServerIpAddr, swAuthInvalidEapolFramesRx=swAuthInvalidEapolFramesRx, swRadiusAcctClientRoundTripTime=swRadiusAcctClientRoundTripTime, swAuthBackendOtherRequestsToSupplicant=swAuthBackendOtherRequestsToSupplicant, authProtocol=authProtocol, swRadiusAcctUpdateInterval=swRadiusAcctUpdateInterval, swAuthBackendAuthSuccesses=swAuthBackendAuthSuccesses, swAuthEapolLogoffFramesRx=swAuthEapolLogoffFramesRx, swAuthEapolRespIdFramesRx=swAuthEapolRespIdFramesRx, swRadiusAuthClientAccessChallenges=swRadiusAuthClientAccessChallenges, swRadiusAuthClientPacketsDropped=swRadiusAuthClientPacketsDropped, swAuthEapolRespFramesRx=swAuthEapolRespFramesRx, swRadiusAccountingCtrl=swRadiusAccountingCtrl, swAuthAuthSuccessWhileAuthenticating=swAuthAuthSuccessWhileAuthenticating, swAuthLastEapolFrameVersion=swAuthLastEapolFrameVersion, swAuthEapLogoffsWhileConnecting=swAuthEapLogoffsWhileConnecting, swAuthSessionOctetsRx=swAuthSessionOctetsRx, swMacAuthStateTable=swMacAuthStateTable, swAuthSessionTerminateCause=swAuthSessionTerminateCause, swAuthSessionId=swAuthSessionId, PYSNMP_MODULE_ID=swDlinkAuthCtrl, swRadiusAcctServerIndex=swRadiusAcctServerIndex, swAuthAuthFailWhileAuthenticating=swAuthAuthFailWhileAuthenticating, swPaeMacAddr=swPaeMacAddr, swRadiusAuthClientIdentifier=swRadiusAuthClientIdentifier, swRadiusAuthClientAccessRejects=swRadiusAuthClientAccessRejects, swRadiusAuthServerEntry=swRadiusAuthServerEntry, swAuthAuthReauthsWhileAuthenticating=swAuthAuthReauthsWhileAuthenticating, swRadiusAcctClientBadAuthenticators=swRadiusAcctClientBadAuthenticators, swRadiusAuthClientUnknownTypes=swRadiusAuthClientUnknownTypes, swAuthCtrl=swAuthCtrl, swFakeAuthentication=swFakeAuthentication, swAuthEapLengthErrorFramesRx=swAuthEapLengthErrorFramesRx, swRadiusAuthClientPendingRequests=swRadiusAuthClientPendingRequests, swRadiusCtrl=swRadiusCtrl, swRadiusAcctClientInvalidServerAddresses=swRadiusAcctClientInvalidServerAddresses, swAuthAuthControlledPortStatus=swAuthAuthControlledPortStatus, swAuthEapolStartFramesRx=swAuthEapolStartFramesRx, swRadiusServerKey=swRadiusServerKey, swRadiusAuthServerTable=swRadiusAuthServerTable, swMacAuthSessionStatsTable=swMacAuthSessionStatsTable, swRadiusForceDownMacAddr=swRadiusForceDownMacAddr, swRadiusServerEntry=swRadiusServerEntry, swRadiusAuthClientRoundTripTime=swRadiusAuthClientRoundTripTime, swRadiusAuthClientBadAuthenticators=swRadiusAuthClientBadAuthenticators, swRadiusAuthInfo=swRadiusAuthInfo, swAuthBackendResponses=swAuthBackendResponses, swAuthAuthReauthsWhileAuthenticated=swAuthAuthReauthsWhileAuthenticated, swMacAuthStateEntry=swMacAuthStateEntry, swRadiusAcctServiceIndex=swRadiusAcctServiceIndex, swRadiusAcctClientServerPortNumber=swRadiusAcctClientServerPortNumber, swRadiusAcctClientRetransmissions=swRadiusAcctClientRetransmissions, swAuthEapolReqIdFramesTx=swAuthEapolReqIdFramesTx, swAuthEapolFramesTx=swAuthEapolFramesTx, swRadiusAcctPortNumber=swRadiusAcctPortNumber, swAuthEapolReqFramesTx=swAuthEapolReqFramesTx, swRadiusAcctClientPacketsDropped=swRadiusAcctClientPacketsDropped, swAuthAuthEapLogoffWhileAuthenticated=swAuthAuthEapLogoffWhileAuthenticated, swRadiusAcctClientIdentifier=swRadiusAcctClientIdentifier, swAuthAuthEapStartsWhileAuthenticating=swAuthAuthEapStartsWhileAuthenticating, swRadiusForceDownPortNumber=swRadiusForceDownPortNumber, swAuthAuthEapLogoffWhileAuthenticating=swAuthAuthEapLogoffWhileAuthenticating, swAuthAuthEapStartsWhileAuthenticated=swAuthAuthEapStartsWhileAuthenticated, swRadiusAcctClientTimeouts=swRadiusAcctClientTimeouts, swRadiusAuthClientMalformedAccessResponses=swRadiusAuthClientMalformedAccessResponses, swRadiusAccountingInfo=swRadiusAccountingInfo, swAuthBackendAuthState=swAuthBackendAuthState, swAuthSessionOctetsTx=swAuthSessionOctetsTx, swRadiusServerIndex=swRadiusServerIndex, swMacAuthDiagEntry=swMacAuthDiagEntry, swRadiusAuthClientTimeouts=swRadiusAuthClientTimeouts, swAuthBackendNonNakResponsesFromSupplicant=swAuthBackendNonNakResponsesFromSupplicant, swMacAuthSessionStatsEntry=swMacAuthSessionStatsEntry, swAuthSessionUserName=swAuthSessionUserName, swAuthLastEapolFrameSource=swAuthLastEapolFrameSource, swRadiusAcctServerEntry=swRadiusAcctServerEntry, swRadiusAcctClientPendingRequests=swRadiusAcctClientPendingRequests, swRadiusServerTable=swRadiusServerTable, swAuthSessionFramesRx=swAuthSessionFramesRx, swRadiusAuthPortNumber=swRadiusAuthPortNumber, swRadiusServerStatus=swRadiusServerStatus, swMacAuthDiagTable=swMacAuthDiagTable, swRadiusAuthClientAccessRetransmissions=swRadiusAuthClientAccessRetransmissions, swAuthSessionTime=swAuthSessionTime, swMacAuthBaseStatsInfo=swMacAuthBaseStatsInfo, swRadiusAcctSuppressNullUserName=swRadiusAcctSuppressNullUserName, swAuthSessionFramesTx=swAuthSessionFramesTx, swRadiusAcctClientMalformedResponses=swRadiusAcctClientMalformedResponses, swRadiusAcctClientResponses=swRadiusAcctClientResponses, swRadiusAcctServerAddress=swRadiusAcctServerAddress, swAuthEapolFramesRx=swAuthEapolFramesRx, swAuthPaeState=swAuthPaeState, swRadiusAuthClientServerPortNumber=swRadiusAuthClientServerPortNumber, swAuthAuthTimeoutsWhileAuthenticating=swAuthAuthTimeoutsWhileAuthenticating, swRadiusAcctClientUnknownTypes=swRadiusAcctClientUnknownTypes, swRadiusAuthClientAccessAccepts=swRadiusAuthClientAccessAccepts, swRadiusCommand=swRadiusCommand, swAuthMode=swAuthMode, swRadiusAcctServiceMethod=swRadiusAcctServiceMethod, swRadiusAcctClientRequests=swRadiusAcctClientRequests, swAuthEntersConnecting=swAuthEntersConnecting, swRadiusAuthClientInvalidServerAddresses=swRadiusAuthClientInvalidServerAddresses, swRadiusAcctServiceEntry=swRadiusAcctServiceEntry, swRadiusAcctServiceTable=swRadiusAcctServiceTable, swRadiusAcctServiceMode=swRadiusAcctServiceMode, swPaePortNumber=swPaePortNumber, swAuthBackendAccessChallenges=swAuthBackendAccessChallenges, swRadiusAuthServerIndex=swRadiusAuthServerIndex)
