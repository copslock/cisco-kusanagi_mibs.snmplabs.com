#
# PySNMP MIB module CISCOSB-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-TRUNK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
dot3adAggPortIndex, dot3adAggIndex = mibBuilder.importSymbols("IEEE8023-LAG-MIB", "dot3adAggPortIndex", "dot3adAggIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, ModuleIdentity, iso, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Bits, TimeTicks, Counter64, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Bits", "TimeTicks", "Counter64", "Integer32", "Unsigned32")
PhysAddress, TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
rlDot3adAgg = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65))
rlDot3adAgg.setRevisions(('2006-12-02 00:00',))
if mibBuilder.loadTexts: rlDot3adAgg.setLastUpdated('200612020000Z')
if mibBuilder.loadTexts: rlDot3adAgg.setOrganization('Cisco Small Business')
rlDot3adAggMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggMibVersion.setStatus('current')
rlDot3adAggBalanceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2), )
if mibBuilder.loadTexts: rlDot3adAggBalanceTable.setStatus('current')
rlDot3adAggBalanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"), (0, "CISCOSB-TRUNK-MIB", "rlDot3adAggBalanceForwardType"))
if mibBuilder.loadTexts: rlDot3adAggBalanceEntry.setStatus('current')
rlDot3adAggBalanceForwardType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bridging", 1), ("routing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggBalanceForwardType.setStatus('current')
rlDot3adAggBalanceLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggBalanceLayer.setStatus('current')
rlDot3adAggBalanceUsedAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplied", 0), ("dstAddr", 1), ("srcAddr", 2), ("dstAndSrcAddr", 3), ("vlanId", 4), ("ethType", 5))).clone('dstAddr')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggBalanceUsedAddresses.setStatus('current')
rlDot3adAggBalanceBroadcastType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("common", 0), ("dedicated", 1))).clone('common')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggBalanceBroadcastType.setStatus('current')
rlDot3adAggNumOfTrunks = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggNumOfTrunks.setStatus('current')
rlDot3adAggMaxPortsInTrunks = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggMaxPortsInTrunks.setStatus('current')
rlDot3adAggTrunkCreationSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notSupported", 0), ("supportsTrunkOrLacp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggTrunkCreationSupport.setStatus('current')
rlDot3adAggCreationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6), )
if mibBuilder.loadTexts: rlDot3adAggCreationTable.setStatus('current')
rlDot3adAggCreationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: rlDot3adAggCreationEntry.setStatus('current')
rlDot3adAggCreationTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggCreationTrunk.setStatus('current')
rlDot3adAggCreationLacp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggCreationLacp.setStatus('current')
rlDot3adAggLoadBalancingPerTrunk = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggLoadBalancingPerTrunk.setStatus('current')
rlDot3adAggPortLacpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8), )
if mibBuilder.loadTexts: rlDot3adAggPortLacpTable.setStatus('current')
rlDot3adAggPortLacpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: rlDot3adAggPortLacpEntry.setStatus('current')
rlDot3adAggPortLacpPdusRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPdusRx.setStatus('current')
rlDot3adAggPortLacpPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPDUsTx.setStatus('current')
rlDot3adAggPortLacpRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("current", 1), ("expired", 2), ("defaulted", 3), ("initialize", 4), ("portDisabled", 5), ("lacpDisabled", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpRxState.setStatus('current')
rlDot3adAggPortLacpMuxState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("detached", 1), ("waiting", 2), ("attached", 3), ("collecting", 4), ("distributing", 5), ("collectingDistributing", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpMuxState.setStatus('current')
rlDot3adAggPortLacpPeriodicState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noPeriodic", 1), ("fastPeriodic", 2), ("slowPeriodic", 3), ("periodicTx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPeriodicState.setStatus('current')
rlDot3adAggPortLacpSelected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unselected", 1), ("selected", 2), ("waiting", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpSelected.setStatus('current')
rlDot3adAggPortLacpReady = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpReady.setStatus('current')
rlDot3adAggPortLacpPortMoved = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPortMoved.setStatus('current')
rlDot3adAggPortLacpNNT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpNNT.setStatus('current')
rlDot3adAggPortLacpPeriodicTxTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPeriodicTxTimer.setStatus('current')
rlDot3adAggPortLacpCurrentWhileTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpCurrentWhileTimer.setStatus('current')
rlDot3adAggPortLacpWaitWhileTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpWaitWhileTimer.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsSupport.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10), )
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsTable.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsEntry.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 3), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority.setStatus('current')
rlDot3adAggLacpMembershipRestrictionsIndividualAggregator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsIndividualAggregator.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-TRUNK-MIB", rlDot3adAggBalanceEntry=rlDot3adAggBalanceEntry, rlDot3adAggLacpMembershipRestrictionsTable=rlDot3adAggLacpMembershipRestrictionsTable, rlDot3adAggBalanceForwardType=rlDot3adAggBalanceForwardType, rlDot3adAggPortLacpNNT=rlDot3adAggPortLacpNNT, rlDot3adAggPortLacpReady=rlDot3adAggPortLacpReady, rlDot3adAggLacpMembershipRestrictionsIndividualAggregator=rlDot3adAggLacpMembershipRestrictionsIndividualAggregator, rlDot3adAggPortLacpPeriodicTxTimer=rlDot3adAggPortLacpPeriodicTxTimer, rlDot3adAggMibVersion=rlDot3adAggMibVersion, rlDot3adAggPortLacpTable=rlDot3adAggPortLacpTable, rlDot3adAggLacpMembershipRestrictionsSupport=rlDot3adAggLacpMembershipRestrictionsSupport, rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey=rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey, rlDot3adAggBalanceUsedAddresses=rlDot3adAggBalanceUsedAddresses, rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority=rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority, rlDot3adAggPortLacpPdusRx=rlDot3adAggPortLacpPdusRx, rlDot3adAggPortLacpPortMoved=rlDot3adAggPortLacpPortMoved, PYSNMP_MODULE_ID=rlDot3adAgg, rlDot3adAggLacpMembershipRestrictionsEntry=rlDot3adAggLacpMembershipRestrictionsEntry, rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId=rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId, rlDot3adAggBalanceBroadcastType=rlDot3adAggBalanceBroadcastType, rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode=rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode, rlDot3adAggCreationEntry=rlDot3adAggCreationEntry, rlDot3adAggPortLacpPDUsTx=rlDot3adAggPortLacpPDUsTx, rlDot3adAggPortLacpMuxState=rlDot3adAggPortLacpMuxState, rlDot3adAggTrunkCreationSupport=rlDot3adAggTrunkCreationSupport, rlDot3adAggPortLacpWaitWhileTimer=rlDot3adAggPortLacpWaitWhileTimer, rlDot3adAgg=rlDot3adAgg, rlDot3adAggPortLacpPeriodicState=rlDot3adAggPortLacpPeriodicState, rlDot3adAggPortLacpCurrentWhileTimer=rlDot3adAggPortLacpCurrentWhileTimer, rlDot3adAggPortLacpRxState=rlDot3adAggPortLacpRxState, rlDot3adAggNumOfTrunks=rlDot3adAggNumOfTrunks, rlDot3adAggPortLacpSelected=rlDot3adAggPortLacpSelected, rlDot3adAggBalanceLayer=rlDot3adAggBalanceLayer, rlDot3adAggMaxPortsInTrunks=rlDot3adAggMaxPortsInTrunks, rlDot3adAggLoadBalancingPerTrunk=rlDot3adAggLoadBalancingPerTrunk, rlDot3adAggCreationLacp=rlDot3adAggCreationLacp, rlDot3adAggCreationTable=rlDot3adAggCreationTable, rlDot3adAggBalanceTable=rlDot3adAggBalanceTable, rlDot3adAggCreationTrunk=rlDot3adAggCreationTrunk, rlDot3adAggPortLacpEntry=rlDot3adAggPortLacpEntry)
