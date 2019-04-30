#
# PySNMP MIB module NOKIA-RATESHAPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-RATESHAPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
enterprises, Integer32, Gauge32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, Counter32, ObjectIdentity, iso, MibIdentifier, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "Gauge32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "Counter32", "ObjectIdentity", "iso", "MibIdentifier", "NotificationType", "IpAddress")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ntcRS = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 16, 4))
ntcRS.setRevisions(('1900-01-14 00:00',))
if mibBuilder.loadTexts: ntcRS.setLastUpdated('0001300000Z')
if mibBuilder.loadTexts: ntcRS.setOrganization('Nokia')
nokia = MibIdentifier((1, 3, 6, 1, 4, 1, 94))
nokiaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1))
ntcCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16))
class PacketSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

class RateLimitAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("drop", 1), ("accept", 2), ("reject", 3), ("condition", 4), ("skip", 5), ("prioritize", 6))

rsAccessLists = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAccessListIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListDirection"), ("NOKIA-RATESHAPE-MIB", "rsAccessListName"), ("NOKIA-RATESHAPE-MIB", "rsAccessListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAccessLists = rsAccessLists.setStatus('current')
rsAccessListTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1), )
if mibBuilder.loadTexts: rsAccessListTable.setStatus('current')
rsAccessListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAccessListIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListDirection"))
if mibBuilder.loadTexts: rsAccessListEntry.setStatus('current')
rsAccessListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListIfIndex.setStatus('current')
rsAccessListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListIndex.setStatus('current')
rsAccessListDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListDirection.setStatus('current')
rsAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAccessListName.setStatus('current')
rsAccessListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAccessListRowStatus.setStatus('current')
rsRules = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2)).setObjects(("NOKIA-RATESHAPE-MIB", "rsRuleIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleDirection"), ("NOKIA-RATESHAPE-MIB", "rsRuleTOS"), ("NOKIA-RATESHAPE-MIB", "rsRuleAction"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcAddress"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcAddrMask"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestAddress"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestAddrMask"), ("NOKIA-RATESHAPE-MIB", "rsRuleIpProtocol"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcStartingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleSrcEndingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestStartingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleDestEndingPort"), ("NOKIA-RATESHAPE-MIB", "rsRuleAggregationClassIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleEstablished"), ("NOKIA-RATESHAPE-MIB", "rsRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRules = rsRules.setStatus('current')
rsRuleTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1), )
if mibBuilder.loadTexts: rsRuleTable.setStatus('current')
rsRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsRuleIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleDirection"))
if mibBuilder.loadTexts: rsRuleEntry.setStatus('current')
rsRuleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleIfIndex.setStatus('current')
rsRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleIndex.setStatus('current')
rsRuleDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleDirection.setStatus('current')
rsRuleTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleTOS.setStatus('current')
rsRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 5), RateLimitAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleAction.setStatus('current')
rsRuleSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleSrcAddress.setStatus('current')
rsRuleSrcAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleSrcAddrMask.setStatus('current')
rsRuleDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleDestAddress.setStatus('current')
rsRuleDestAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleDestAddrMask.setStatus('current')
rsRuleIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleIpProtocol.setStatus('current')
rsRuleSrcStartingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleSrcStartingPort.setStatus('current')
rsRuleSrcEndingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleSrcEndingPort.setStatus('current')
rsRuleDestStartingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleDestStartingPort.setStatus('current')
rsRuleDestEndingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleDestEndingPort.setStatus('current')
rsRuleAggregationClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleAggregationClassIndex.setStatus('current')
rsRuleEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("established", 1), ("notEstablished", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleEstablished.setStatus('current')
rsRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 2, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRuleRowStatus.setStatus('current')
rsAggregationClasses = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAggregationClassIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassDirection"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassName"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassMeanRate"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassBurstSize"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAggregationClasses = rsAggregationClasses.setStatus('current')
rsAggregationClassTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1), )
if mibBuilder.loadTexts: rsAggregationClassTable.setStatus('current')
rsAggregationClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassDirection"))
if mibBuilder.loadTexts: rsAggregationClassEntry.setStatus('current')
rsAggregationClassIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassIfIndex.setStatus('current')
rsAggregationClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassIndex.setStatus('current')
rsAggregationClassDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassDirection.setStatus('current')
rsAggregationClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassName.setStatus('current')
rsAggregationClassMeanRate = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassMeanRate.setStatus('current')
rsAggregationClassBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1500, 150000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassBurstSize.setStatus('current')
rsAggregationClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 3, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsAggregationClassRowStatus.setStatus('current')
rsAccessListStats = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAccessListStatIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatIndex"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatDirection"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsAccessListStatBytesPassed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAccessListStats = rsAccessListStats.setStatus('current')
rsAccessListStatTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1), )
if mibBuilder.loadTexts: rsAccessListStatTable.setStatus('current')
rsAccessListStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAccessListStatDirection"))
if mibBuilder.loadTexts: rsAccessListStatEntry.setStatus('current')
rsAccessListStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatIfIndex.setStatus('current')
rsAccessListStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatIndex.setStatus('current')
rsAccessListStatDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatDirection.setStatus('current')
rsAccessListStatPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatPktsPassed.setStatus('current')
rsAccessListStatBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAccessListStatBytesPassed.setStatus('current')
rsRuleStats = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6)).setObjects(("NOKIA-RATESHAPE-MIB", "rsRuleStatIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatIndex"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatDirection"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatDropPkts"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatDropOctets"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsRuleStatBytesPassed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRuleStats = rsRuleStats.setStatus('current')
rsRuleStatTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1), )
if mibBuilder.loadTexts: rsRuleStatTable.setStatus('current')
rsRuleStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsRuleStatIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleStatIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsRuleStatDirection"))
if mibBuilder.loadTexts: rsRuleStatEntry.setStatus('current')
rsRuleStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatIfIndex.setStatus('current')
rsRuleStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatIndex.setStatus('current')
rsRuleStatDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatDirection.setStatus('current')
rsRuleStatDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatDropPkts.setStatus('current')
rsRuleStatDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatDropOctets.setStatus('current')
rsRuleStatPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatPktsPassed.setStatus('current')
rsRuleStatBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 6, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRuleStatBytesPassed.setStatus('current')
rsAggregationClassStats = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5)).setObjects(("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIfIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIndex"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDirection"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatShapedPkts"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatShapedOctets"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatEnqueuedPkts"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatEnqueuedOctets"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDroppedPkts"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDroppedOctets"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatInputPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatOutputPktsPassed"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatInputBytesPassed"), ("NOKIA-RATESHAPE-MIB", "rsAggregationClassStatOutputBytesPassed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAggregationClassStats = rsAggregationClassStats.setStatus('current')
rsAggregationClassStatTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1), )
if mibBuilder.loadTexts: rsAggregationClassStatTable.setStatus('current')
rsAggregationClassStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1), ).setIndexNames((0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIfIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatIndex"), (0, "NOKIA-RATESHAPE-MIB", "rsAggregationClassStatDirection"))
if mibBuilder.loadTexts: rsAggregationClassStatEntry.setStatus('current')
rsAggregationClassStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatIfIndex.setStatus('current')
rsAggregationClassStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatIndex.setStatus('current')
rsAggregationClassStatDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 3), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatDirection.setStatus('current')
rsAggregationClassStatShapedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatShapedPkts.setStatus('current')
rsAggregationClassStatShapedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatShapedOctets.setStatus('current')
rsAggregationClassStatEnqueuedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatEnqueuedPkts.setStatus('current')
rsAggregationClassStatEnqueuedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatEnqueuedOctets.setStatus('current')
rsAggregationClassStatDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatDroppedPkts.setStatus('current')
rsAggregationClassStatDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatDroppedOctets.setStatus('current')
rsAggregationClassStatInputPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatInputPktsPassed.setStatus('current')
rsAggregationClassStatOutputPktsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatOutputPktsPassed.setStatus('current')
rsAggregationClassStatInputBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatInputBytesPassed.setStatus('current')
rsAggregationClassStatOutputBytesPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 4, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAggregationClassStatOutputBytesPassed.setStatus('current')
mibBuilder.exportSymbols("NOKIA-RATESHAPE-MIB", rsAggregationClassMeanRate=rsAggregationClassMeanRate, rsAggregationClassStatIndex=rsAggregationClassStatIndex, rsAccessListStatDirection=rsAccessListStatDirection, rsAggregationClassTable=rsAggregationClassTable, rsRuleStatBytesPassed=rsRuleStatBytesPassed, rsAccessListStatTable=rsAccessListStatTable, rsAggregationClassEntry=rsAggregationClassEntry, rsAggregationClassDirection=rsAggregationClassDirection, rsAccessListStatPktsPassed=rsAccessListStatPktsPassed, rsAggregationClassStatOutputBytesPassed=rsAggregationClassStatOutputBytesPassed, rsRuleStatDropPkts=rsRuleStatDropPkts, rsRuleIndex=rsRuleIndex, rsAggregationClassName=rsAggregationClassName, RateLimitAction=RateLimitAction, rsRuleSrcAddress=rsRuleSrcAddress, rsAggregationClassStatDroppedOctets=rsAggregationClassStatDroppedOctets, rsAggregationClassIndex=rsAggregationClassIndex, rsRuleStatIfIndex=rsRuleStatIfIndex, rsAggregationClassStatEntry=rsAggregationClassStatEntry, rsRuleTOS=rsRuleTOS, rsRuleAggregationClassIndex=rsRuleAggregationClassIndex, rsRuleTable=rsRuleTable, rsAccessListName=rsAccessListName, rsAccessListStats=rsAccessListStats, rsRuleSrcEndingPort=rsRuleSrcEndingPort, rsAggregationClassStats=rsAggregationClassStats, nokiaProducts=nokiaProducts, rsRuleDestStartingPort=rsRuleDestStartingPort, rsAggregationClassIfIndex=rsAggregationClassIfIndex, PYSNMP_MODULE_ID=ntcRS, rsAccessListStatIfIndex=rsAccessListStatIfIndex, rsAccessListIndex=rsAccessListIndex, rsRuleStatPktsPassed=rsRuleStatPktsPassed, rsRuleStatEntry=rsRuleStatEntry, rsAccessListEntry=rsAccessListEntry, rsAccessListStatBytesPassed=rsAccessListStatBytesPassed, rsRuleIfIndex=rsRuleIfIndex, rsRuleEstablished=rsRuleEstablished, rsAggregationClasses=rsAggregationClasses, rsRuleStatDropOctets=rsRuleStatDropOctets, rsRuleIpProtocol=rsRuleIpProtocol, rsAccessListStatEntry=rsAccessListStatEntry, rsRuleStatIndex=rsRuleStatIndex, rsAggregationClassStatInputPktsPassed=rsAggregationClassStatInputPktsPassed, rsAggregationClassStatTable=rsAggregationClassStatTable, rsAccessListIfIndex=rsAccessListIfIndex, rsAggregationClassStatEnqueuedPkts=rsAggregationClassStatEnqueuedPkts, rsRuleSrcStartingPort=rsRuleSrcStartingPort, rsAggregationClassRowStatus=rsAggregationClassRowStatus, rsRuleAction=rsRuleAction, rsAccessListTable=rsAccessListTable, rsAccessListRowStatus=rsAccessListRowStatus, rsRuleDirection=rsRuleDirection, rsRuleDestEndingPort=rsRuleDestEndingPort, rsRuleEntry=rsRuleEntry, ntcCommon=ntcCommon, rsAggregationClassStatIfIndex=rsAggregationClassStatIfIndex, rsRuleDestAddress=rsRuleDestAddress, rsRuleDestAddrMask=rsRuleDestAddrMask, rsRuleSrcAddrMask=rsRuleSrcAddrMask, rsAggregationClassStatShapedOctets=rsAggregationClassStatShapedOctets, rsRuleStats=rsRuleStats, nokia=nokia, rsAggregationClassStatDirection=rsAggregationClassStatDirection, rsAccessListStatIndex=rsAccessListStatIndex, rsRuleStatDirection=rsRuleStatDirection, rsAggregationClassStatEnqueuedOctets=rsAggregationClassStatEnqueuedOctets, rsAccessLists=rsAccessLists, rsAggregationClassStatOutputPktsPassed=rsAggregationClassStatOutputPktsPassed, rsAccessListDirection=rsAccessListDirection, rsAggregationClassStatDroppedPkts=rsAggregationClassStatDroppedPkts, rsAggregationClassBurstSize=rsAggregationClassBurstSize, ntcRS=ntcRS, PacketSource=PacketSource, rsRules=rsRules, rsRuleStatTable=rsRuleStatTable, rsAggregationClassStatInputBytesPassed=rsAggregationClassStatInputBytesPassed, rsAggregationClassStatShapedPkts=rsAggregationClassStatShapedPkts, rsRuleRowStatus=rsRuleRowStatus)