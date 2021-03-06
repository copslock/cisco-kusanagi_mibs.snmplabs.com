#
# PySNMP MIB module CISCO-IKE-FLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IKE-FLOW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
cisgIpsSgFailRemoteAddress, cisgIpsSgTunHistIndex, cisgIpsSgTunIndex, cisgIpsSgProtocol, cisgIpsSgFailLocalAddress = mibBuilder.importSymbols("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress", "cisgIpsSgTunHistIndex", "cisgIpsSgTunIndex", "cisgIpsSgProtocol", "cisgIpsSgFailLocalAddress")
CIPsecDiffHellmanGrp, CIPsecIkeNegoMode = mibBuilder.importSymbols("CISCO-IPSEC-TC", "CIPsecDiffHellmanGrp", "CIPsecIkeNegoMode")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, Unsigned32, Counter64, Bits, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ModuleIdentity, Gauge32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Unsigned32", "Counter64", "Bits", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ModuleIdentity", "Gauge32", "IpAddress", "NotificationType")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoIkeFlowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 429))
ciscoIkeFlowMIB.setRevisions(('2004-09-14 00:00',))
if mibBuilder.loadTexts: ciscoIkeFlowMIB.setLastUpdated('200409140000Z')
if mibBuilder.loadTexts: ciscoIkeFlowMIB.setOrganization('Cisco Systems')
ciscoIkeFlowMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 0))
ciscoIkeFlowMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 1))
ciscoIkeFlowMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 2))
cifIkeCurrentActivity = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1))
cifIkeHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2))
cifIkeNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 3))
cifIkeGlobalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1), )
if mibBuilder.loadTexts: cifIkeGlobalStatsTable.setStatus('current')
cifIkeGlobalStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"))
if mibBuilder.loadTexts: cifIkeGlobalStatsEntry.setStatus('current')
cifIkeGlobalInP2Exchgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 1), Counter64()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalInP2Exchgs.setStatus('current')
cifIkeGlobalInP2ExchgInvalids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 2), Counter64()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalInP2ExchgInvalids.setStatus('current')
cifIkeGlobalInP2ExchgRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 3), Counter64()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalInP2ExchgRejects.setStatus('current')
cifIkeGlobalOutP2Exchgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 4), Counter64()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalOutP2Exchgs.setStatus('current')
cifIkeGlobalOutP2ExchgInvalids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 5), Counter64()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalOutP2ExchgInvalids.setStatus('current')
cifIkeGlobalOutP2ExchgRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 6), Counter64()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalOutP2ExchgRejects.setStatus('current')
cifIkeGlobalInXauths = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 7), Counter64()).setUnits('Failures').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalInXauths.setStatus('current')
cifIkeGlobalInXauthFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 8), Counter64()).setUnits('Failures').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalInXauthFailures.setStatus('current')
cifIkeGlobalOutXauthFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 9), Counter64()).setUnits('Failures').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalOutXauthFailures.setStatus('current')
cifIkeGlobalInNewGrpReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 10), Counter64()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalInNewGrpReqs.setStatus('current')
cifIkeGlobalOutNewGrpReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 11), Counter64()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalOutNewGrpReqs.setStatus('current')
cifIkeGlobalInNewGrpRejectReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 12), Counter64()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalInNewGrpRejectReqs.setStatus('current')
cifIkeGlobalOutNewGrpRejectReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 1, 1, 13), Counter64()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeGlobalOutNewGrpRejectReqs.setStatus('current')
cifIkeTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3), )
if mibBuilder.loadTexts: cifIkeTunnelTable.setStatus('current')
cifIkeTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"), (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunIndex"))
if mibBuilder.loadTexts: cifIkeTunnelEntry.setStatus('current')
cifIkeTunNegoMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 1), CIPsecIkeNegoMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunNegoMode.setStatus('current')
cifIkeTunDHGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 2), CIPsecDiffHellmanGrp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunDHGrp.setStatus('current')
cifIkeTunSaRefreshThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunSaRefreshThreshold.setStatus('current')
cifIkeTunTotalRefreshes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 4), Counter32()).setUnits('QM Exchanges').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunTotalRefreshes.setStatus('current')
cifIkeTunInP2Exchgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 5), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInP2Exchgs.setStatus('current')
cifIkeTunInP2ExchgInvalids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 6), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInP2ExchgInvalids.setStatus('current')
cifIkeTunInP2ExchgRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 7), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInP2ExchgRejects.setStatus('current')
cifIkeTunInP2SaDelRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 8), Counter32()).setUnits('Notification Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInP2SaDelRequests.setStatus('current')
cifIkeTunOutP2Exchgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 9), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunOutP2Exchgs.setStatus('current')
cifIkeTunOutP2ExchgInvalids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 10), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunOutP2ExchgInvalids.setStatus('current')
cifIkeTunOutP2ExchgRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 11), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunOutP2ExchgRejects.setStatus('current')
cifIkeTunInNewGrpReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 12), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInNewGrpReqs.setStatus('current')
cifIkeTunOutNewGrpReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 13), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunOutNewGrpReqs.setStatus('current')
cifIkeTunInNewGrpRejectedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 14), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInNewGrpRejectedReqs.setStatus('current')
cifIkeTunOutNewGrpRejectedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 15), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunOutNewGrpRejectedReqs.setStatus('current')
cifIkeTunInConfigs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 16), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInConfigs.setStatus('current')
cifIkeTunOutConfigs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 17), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunOutConfigs.setStatus('current')
cifIkeTunInConfigRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 18), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunInConfigRejects.setStatus('current')
cifIkeTunOutConfigRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 1, 3, 1, 19), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunOutConfigRejects.setStatus('current')
cifIkeTunnelHistTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1), )
if mibBuilder.loadTexts: cifIkeTunnelHistTable.setStatus('current')
cifIkeTunnelHistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"), (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistIndex"))
if mibBuilder.loadTexts: cifIkeTunnelHistEntry.setStatus('current')
cifIkeTunHistNegoMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 1), CIPsecIkeNegoMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistNegoMode.setStatus('current')
cifIkeTunHistDHGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 2), CIPsecDiffHellmanGrp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistDHGrp.setStatus('current')
cifIkeTunHistTotalRefreshes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 3), Counter32()).setUnits('QM Exchanges').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistTotalRefreshes.setStatus('current')
cifIkeTunHistTotalSas = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 4), Counter32()).setUnits('SAs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistTotalSas.setStatus('current')
cifIkeTunHistInP2Exchgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 5), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistInP2Exchgs.setStatus('current')
cifIkeTunHistInP2ExchgInvalids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 6), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistInP2ExchgInvalids.setStatus('current')
cifIkeTunHistInP2ExchgRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 7), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistInP2ExchgRejects.setStatus('current')
cifIkeTunHistOutP2Exchgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 8), Counter32()).setUnits('Notification Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistOutP2Exchgs.setStatus('current')
cifIkeTunHistOutP2ExchgInvalids = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 9), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistOutP2ExchgInvalids.setStatus('current')
cifIkeTunHistOutP2ExchgRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 10), Counter32()).setUnits('SA Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistOutP2ExchgRejects.setStatus('current')
cifIkeTunHistInNewGrpReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 11), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistInNewGrpReqs.setStatus('current')
cifIkeTunHistOutNewGrpReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 12), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistOutNewGrpReqs.setStatus('current')
cifIkeTunHistInNewGrpRejectReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 13), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistInNewGrpRejectReqs.setStatus('current')
cifIkeTunHistOutNewGrpRejectReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 14), Counter32()).setUnits('Negotiations').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistOutNewGrpRejectReqs.setStatus('current')
cifIkeTunHistInConfigs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 15), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistInConfigs.setStatus('current')
cifIkeTunHistOutConfigs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 16), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistOutConfigs.setStatus('current')
cifIkeTunHistInConfigsRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 17), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistInConfigsRejects.setStatus('current')
cifIkeTunHistOutConfigsRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 2, 1, 1, 18), Counter32()).setUnits('Mode Configuration Setting Payloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cifIkeTunHistOutConfigsRejects.setStatus('current')
cifIkeNotifCntlInNewGrpRejected = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cifIkeNotifCntlInNewGrpRejected.setStatus('current')
cifIkeNotifCntlOutNewGrpRejected = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 429, 1, 3, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cifIkeNotifCntlOutNewGrpRejected.setStatus('current')
ciscoIkeFlowInNewGrpRejected = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 429, 0, 1)).setObjects(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalAddress"), ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress"))
if mibBuilder.loadTexts: ciscoIkeFlowInNewGrpRejected.setStatus('current')
ciscoIkeFlowOutNewGrpRejected = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 429, 0, 2)).setObjects(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalAddress"), ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress"))
if mibBuilder.loadTexts: ciscoIkeFlowOutNewGrpRejected.setStatus('current')
ciscoIkeFlowMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 1))
ciscoIkeFlowMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2))
ciscoIkeFlowMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 1, 1)).setObjects(("CISCO-IKE-FLOW-MIB", "ciscoIkeFlowActivityGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowNewGroupGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowXauthGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowModeConfigGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowHistoryGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowNewGroupHistoryGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowModeConfigHistoryGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowNotificationGroup"), ("CISCO-IKE-FLOW-MIB", "cifIkeFlowNotifCntlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowMIBCompliance = ciscoIkeFlowMIBCompliance.setStatus('current')
ciscoIkeFlowActivityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 1)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInP2Exchgs"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInP2ExchgInvalids"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInP2ExchgRejects"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutP2Exchgs"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutP2ExchgInvalids"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutP2ExchgRejects"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunNegoMode"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunDHGrp"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunSaRefreshThreshold"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunTotalRefreshes"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2Exchgs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2ExchgInvalids"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2ExchgRejects"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunInP2SaDelRequests"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutP2Exchgs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutP2ExchgInvalids"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutP2ExchgRejects"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowActivityGroup = ciscoIkeFlowActivityGroup.setStatus('current')
cifIkeFlowNewGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 2)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInNewGrpReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutNewGrpReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInNewGrpRejectReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutNewGrpRejectReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunInNewGrpReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutNewGrpReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunInNewGrpRejectedReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutNewGrpRejectedReqs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowNewGroupGroup = cifIkeFlowNewGroupGroup.setStatus('current')
cifIkeFlowXauthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 3)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInXauths"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalInXauthFailures"), ("CISCO-IKE-FLOW-MIB", "cifIkeGlobalOutXauthFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowXauthGroup = cifIkeFlowXauthGroup.setStatus('current')
cifIkeFlowModeConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 4)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeTunInConfigs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutConfigs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunInConfigRejects"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunOutConfigRejects"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowModeConfigGroup = cifIkeFlowModeConfigGroup.setStatus('current')
cifIkeFlowHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 5)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeTunHistNegoMode"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistDHGrp"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistTotalRefreshes"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistTotalSas"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInP2Exchgs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInP2ExchgInvalids"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInP2ExchgRejects"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutP2Exchgs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutP2ExchgInvalids"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutP2ExchgRejects"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowHistoryGroup = cifIkeFlowHistoryGroup.setStatus('current')
cifIkeFlowNewGroupHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 6)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInNewGrpReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutNewGrpReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInNewGrpRejectReqs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutNewGrpRejectReqs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowNewGroupHistoryGroup = cifIkeFlowNewGroupHistoryGroup.setStatus('current')
cifIkeFlowModeConfigHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 7)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInConfigs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutConfigs"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistInConfigsRejects"), ("CISCO-IKE-FLOW-MIB", "cifIkeTunHistOutConfigsRejects"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowModeConfigHistoryGroup = cifIkeFlowModeConfigHistoryGroup.setStatus('current')
cifIkeFlowNotifCntlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 8)).setObjects(("CISCO-IKE-FLOW-MIB", "cifIkeNotifCntlInNewGrpRejected"), ("CISCO-IKE-FLOW-MIB", "cifIkeNotifCntlOutNewGrpRejected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowNotifCntlGroup = cifIkeFlowNotifCntlGroup.setStatus('current')
cifIkeFlowNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 429, 2, 2, 9)).setObjects(("CISCO-IKE-FLOW-MIB", "ciscoIkeFlowInNewGrpRejected"), ("CISCO-IKE-FLOW-MIB", "ciscoIkeFlowOutNewGrpRejected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifIkeFlowNotificationGroup = cifIkeFlowNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-MIB", ciscoIkeFlowOutNewGrpRejected=ciscoIkeFlowOutNewGrpRejected, cifIkeTunnelTable=cifIkeTunnelTable, cifIkeNotifControl=cifIkeNotifControl, cifIkeTunHistNegoMode=cifIkeTunHistNegoMode, cifIkeGlobalStatsTable=cifIkeGlobalStatsTable, cifIkeFlowXauthGroup=cifIkeFlowXauthGroup, cifIkeTunDHGrp=cifIkeTunDHGrp, ciscoIkeFlowMIBCompliance=ciscoIkeFlowMIBCompliance, cifIkeTunHistInP2Exchgs=cifIkeTunHistInP2Exchgs, cifIkeGlobalInP2Exchgs=cifIkeGlobalInP2Exchgs, cifIkeTunInNewGrpReqs=cifIkeTunInNewGrpReqs, cifIkeFlowNotificationGroup=cifIkeFlowNotificationGroup, cifIkeTunHistOutNewGrpReqs=cifIkeTunHistOutNewGrpReqs, cifIkeTunOutConfigRejects=cifIkeTunOutConfigRejects, ciscoIkeFlowMIBCompliances=ciscoIkeFlowMIBCompliances, cifIkeTunHistTotalSas=cifIkeTunHistTotalSas, cifIkeFlowModeConfigGroup=cifIkeFlowModeConfigGroup, cifIkeFlowModeConfigHistoryGroup=cifIkeFlowModeConfigHistoryGroup, cifIkeTunHistInNewGrpReqs=cifIkeTunHistInNewGrpReqs, cifIkeTunOutNewGrpReqs=cifIkeTunOutNewGrpReqs, cifIkeGlobalOutXauthFailures=cifIkeGlobalOutXauthFailures, cifIkeFlowNewGroupHistoryGroup=cifIkeFlowNewGroupHistoryGroup, cifIkeGlobalInXauthFailures=cifIkeGlobalInXauthFailures, ciscoIkeFlowActivityGroup=ciscoIkeFlowActivityGroup, cifIkeGlobalOutP2ExchgInvalids=cifIkeGlobalOutP2ExchgInvalids, cifIkeNotifCntlInNewGrpRejected=cifIkeNotifCntlInNewGrpRejected, cifIkeFlowHistoryGroup=cifIkeFlowHistoryGroup, cifIkeGlobalInXauths=cifIkeGlobalInXauths, cifIkeTunHistInP2ExchgInvalids=cifIkeTunHistInP2ExchgInvalids, cifIkeTunNegoMode=cifIkeTunNegoMode, cifIkeTunHistOutConfigs=cifIkeTunHistOutConfigs, cifIkeTunnelEntry=cifIkeTunnelEntry, cifIkeCurrentActivity=cifIkeCurrentActivity, cifIkeTunHistOutNewGrpRejectReqs=cifIkeTunHistOutNewGrpRejectReqs, cifIkeGlobalOutNewGrpRejectReqs=cifIkeGlobalOutNewGrpRejectReqs, cifIkeGlobalOutP2Exchgs=cifIkeGlobalOutP2Exchgs, cifIkeTunHistOutP2ExchgRejects=cifIkeTunHistOutP2ExchgRejects, cifIkeFlowNotifCntlGroup=cifIkeFlowNotifCntlGroup, ciscoIkeFlowMIBObjects=ciscoIkeFlowMIBObjects, cifIkeGlobalInP2ExchgRejects=cifIkeGlobalInP2ExchgRejects, cifIkeTunHistTotalRefreshes=cifIkeTunHistTotalRefreshes, cifIkeTunHistInConfigsRejects=cifIkeTunHistInConfigsRejects, cifIkeGlobalInNewGrpReqs=cifIkeGlobalInNewGrpReqs, cifIkeTunInP2SaDelRequests=cifIkeTunInP2SaDelRequests, ciscoIkeFlowMIB=ciscoIkeFlowMIB, cifIkeTunOutP2Exchgs=cifIkeTunOutP2Exchgs, cifIkeNotifCntlOutNewGrpRejected=cifIkeNotifCntlOutNewGrpRejected, cifIkeGlobalOutP2ExchgRejects=cifIkeGlobalOutP2ExchgRejects, ciscoIkeFlowInNewGrpRejected=ciscoIkeFlowInNewGrpRejected, cifIkeTunHistOutP2Exchgs=cifIkeTunHistOutP2Exchgs, cifIkeTunSaRefreshThreshold=cifIkeTunSaRefreshThreshold, cifIkeGlobalStatsEntry=cifIkeGlobalStatsEntry, cifIkeTunOutConfigs=cifIkeTunOutConfigs, cifIkeGlobalInNewGrpRejectReqs=cifIkeGlobalInNewGrpRejectReqs, cifIkeTunHistOutConfigsRejects=cifIkeTunHistOutConfigsRejects, cifIkeTunInP2ExchgInvalids=cifIkeTunInP2ExchgInvalids, cifIkeTunInConfigs=cifIkeTunInConfigs, ciscoIkeFlowMIBGroups=ciscoIkeFlowMIBGroups, cifIkeTunTotalRefreshes=cifIkeTunTotalRefreshes, cifIkeTunInP2Exchgs=cifIkeTunInP2Exchgs, cifIkeTunInNewGrpRejectedReqs=cifIkeTunInNewGrpRejectedReqs, ciscoIkeFlowMIBConform=ciscoIkeFlowMIBConform, cifIkeTunnelHistEntry=cifIkeTunnelHistEntry, cifIkeGlobalOutNewGrpReqs=cifIkeGlobalOutNewGrpReqs, cifIkeTunHistInNewGrpRejectReqs=cifIkeTunHistInNewGrpRejectReqs, cifIkeTunOutNewGrpRejectedReqs=cifIkeTunOutNewGrpRejectedReqs, cifIkeHistory=cifIkeHistory, ciscoIkeFlowMIBNotifs=ciscoIkeFlowMIBNotifs, cifIkeTunOutP2ExchgRejects=cifIkeTunOutP2ExchgRejects, cifIkeTunHistInP2ExchgRejects=cifIkeTunHistInP2ExchgRejects, cifIkeTunHistInConfigs=cifIkeTunHistInConfigs, cifIkeTunOutP2ExchgInvalids=cifIkeTunOutP2ExchgInvalids, cifIkeTunHistDHGrp=cifIkeTunHistDHGrp, cifIkeFlowNewGroupGroup=cifIkeFlowNewGroupGroup, PYSNMP_MODULE_ID=ciscoIkeFlowMIB, cifIkeTunInConfigRejects=cifIkeTunInConfigRejects, cifIkeTunnelHistTable=cifIkeTunnelHistTable, cifIkeTunInP2ExchgRejects=cifIkeTunInP2ExchgRejects, cifIkeTunHistOutP2ExchgInvalids=cifIkeTunHistOutP2ExchgInvalids, cifIkeGlobalInP2ExchgInvalids=cifIkeGlobalInP2ExchgInvalids)
