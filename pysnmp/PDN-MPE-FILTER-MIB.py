#
# PySNMP MIB module PDN-MPE-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-FILTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_filter, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-filter")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter64, MibIdentifier, NotificationType, iso, NotificationType, Bits, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter64", "MibIdentifier", "NotificationType", "iso", "NotificationType", "Bits", "Integer32", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
mpeSysDevFilterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1))
mpeSysDevFilterMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 2))
mpeSysDevIpFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1))
mpeSysDevIpFilterConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1), )
if mibBuilder.loadTexts: mpeSysDevIpFilterConfigTable.setStatus('mandatory')
mpeSysDevIpFilterConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "PDN-MPE-FILTER-MIB", "mpeSysDevIpFilterName"))
if mibBuilder.loadTexts: mpeSysDevIpFilterConfigTableEntry.setStatus('mandatory')
mpeSysDevIpFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevIpFilterName.setStatus('mandatory')
mpeSysDevIpDefFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpDefFilterAction.setStatus('mandatory')
mpeSysDevIpFilterNumOfDynamicRules = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevIpFilterNumOfDynamicRules.setStatus('mandatory')
mpeSysDevIpFilterNumOfStaticRules = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevIpFilterNumOfStaticRules.setStatus('mandatory')
mpeSysDevIpFilterRefCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevIpFilterRefCount.setStatus('mandatory')
mpeSysDevIpFilterTcpAckFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2), ("noOp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterTcpAckFilterAction.setStatus('mandatory')
mpeSysDevIpFilterDhcpFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2), ("noOp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterDhcpFilterAction.setStatus('mandatory')
mpeSysDevIpFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRowStatus.setStatus('mandatory')
mpeSysDevIpFilterRuleConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2), )
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleConfigTable.setStatus('mandatory')
mpeSysDevIpFilterRuleConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "PDN-MPE-FILTER-MIB", "mpeSysDevIpRuleFilterName"), (0, "PDN-MPE-FILTER-MIB", "mpeSysDevIpFilterRuleNumber"))
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleConfigTableEntry.setStatus('mandatory')
mpeSysDevIpRuleFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevIpRuleFilterName.setStatus('mandatory')
mpeSysDevIpFilterRuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleNumber.setStatus('mandatory')
mpeSysDevIpFilterRuleSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleSrcAddress.setStatus('mandatory')
mpeSysDevIpFilterRuleSrcAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleSrcAddrMask.setStatus('mandatory')
mpeSysDevIpFilterRuleSrcAddrCompEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("noOp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleSrcAddrCompEnable.setStatus('mandatory')
mpeSysDevIpFilterRuleSrcPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleSrcPortNum.setStatus('mandatory')
mpeSysDevIpFilterRuleMaxSrcPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleMaxSrcPortNum.setStatus('mandatory')
mpeSysDevIpFilterRuleSrcCompType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("eq", 2), ("neq", 3), ("gt", 4), ("lt", 5), ("inRange", 6), ("outRange", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleSrcCompType.setStatus('mandatory')
mpeSysDevIpFilterRuleDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleDestAddress.setStatus('mandatory')
mpeSysDevIpFilterRuleDestAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleDestAddrMask.setStatus('mandatory')
mpeSysDevIpFilterRuleDestAddrCompEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("noOp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleDestAddrCompEnable.setStatus('mandatory')
mpeSysDevIpFilterRuleDestPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleDestPortNum.setStatus('mandatory')
mpeSysDevIpFilterRuleMaxDestPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleMaxDestPortNum.setStatus('mandatory')
mpeSysDevIpFilterRuleDestCompType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("eq", 2), ("neq", 3), ("gt", 4), ("lt", 5), ("inRange", 6), ("outRange", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleDestCompType.setStatus('mandatory')
mpeSysDevIpFilterRuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleType.setStatus('mandatory')
mpeSysDevIpFilterRuleProtocolTypeUdp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleProtocolTypeUdp.setStatus('mandatory')
mpeSysDevIpFilterRuleProtocolTypeTcp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleProtocolTypeTcp.setStatus('mandatory')
mpeSysDevIpFilterRuleProtocolTypeIcmp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleProtocolTypeIcmp.setStatus('mandatory')
mpeSysDevIpFilterRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 2, 1, 19), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeSysDevIpFilterRuleRowStatus.setStatus('mandatory')
mpeSysDevMaxNumOfIpFiltersTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3), )
if mibBuilder.loadTexts: mpeSysDevMaxNumOfIpFiltersTable.setStatus('mandatory')
mpeSysDevMaxNumOfIpFiltersTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeSysDevMaxNumOfIpFiltersTableEntry.setStatus('mandatory')
mpeSysDevMaxNumOfInputIpFilters = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevMaxNumOfInputIpFilters.setStatus('mandatory')
mpeSysDevMaxNumOfOutputIpFilters = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 23, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeSysDevMaxNumOfOutputIpFilters.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-MPE-FILTER-MIB", mpeSysDevIpFilterRefCount=mpeSysDevIpFilterRefCount, mpeSysDevIpFilterNumOfStaticRules=mpeSysDevIpFilterNumOfStaticRules, mpeSysDevIpFilterRuleSrcAddress=mpeSysDevIpFilterRuleSrcAddress, mpeSysDevFilterMIBObjects=mpeSysDevFilterMIBObjects, mpeSysDevIpFilterRuleConfigTable=mpeSysDevIpFilterRuleConfigTable, mpeSysDevIpFilterRuleSrcAddrCompEnable=mpeSysDevIpFilterRuleSrcAddrCompEnable, mpeSysDevIpFilterDhcpFilterAction=mpeSysDevIpFilterDhcpFilterAction, mpeSysDevIpFilterRuleProtocolTypeIcmp=mpeSysDevIpFilterRuleProtocolTypeIcmp, mpeSysDevIpFilterRuleSrcPortNum=mpeSysDevIpFilterRuleSrcPortNum, mpeSysDevIpRuleFilterName=mpeSysDevIpRuleFilterName, mpeSysDevMaxNumOfIpFiltersTable=mpeSysDevMaxNumOfIpFiltersTable, mpeSysDevIpFilterRuleConfigTableEntry=mpeSysDevIpFilterRuleConfigTableEntry, mpeSysDevFilterMIBTraps=mpeSysDevFilterMIBTraps, mpeSysDevIpFilterRuleDestAddress=mpeSysDevIpFilterRuleDestAddress, mpeSysDevIpFilterRowStatus=mpeSysDevIpFilterRowStatus, mpeSysDevIpFilterRuleMaxSrcPortNum=mpeSysDevIpFilterRuleMaxSrcPortNum, mpeSysDevMaxNumOfOutputIpFilters=mpeSysDevMaxNumOfOutputIpFilters, mpeSysDevIpFilterConfigTableEntry=mpeSysDevIpFilterConfigTableEntry, mpeSysDevIpFilterRuleDestPortNum=mpeSysDevIpFilterRuleDestPortNum, mpeSysDevIpFilterRuleDestAddrMask=mpeSysDevIpFilterRuleDestAddrMask, mpeSysDevMaxNumOfIpFiltersTableEntry=mpeSysDevMaxNumOfIpFiltersTableEntry, mpeSysDevIpFilterRuleType=mpeSysDevIpFilterRuleType, mpeSysDevIpFilterRuleNumber=mpeSysDevIpFilterRuleNumber, mpeSysDevIpFilterRuleProtocolTypeTcp=mpeSysDevIpFilterRuleProtocolTypeTcp, mpeSysDevIpFilterRuleRowStatus=mpeSysDevIpFilterRuleRowStatus, mpeSysDevIpFilterRuleDestCompType=mpeSysDevIpFilterRuleDestCompType, mpeSysDevIpFilter=mpeSysDevIpFilter, mpeSysDevIpFilterRuleSrcCompType=mpeSysDevIpFilterRuleSrcCompType, mpeSysDevIpFilterConfigTable=mpeSysDevIpFilterConfigTable, mpeSysDevIpFilterTcpAckFilterAction=mpeSysDevIpFilterTcpAckFilterAction, mpeSysDevIpFilterRuleSrcAddrMask=mpeSysDevIpFilterRuleSrcAddrMask, mpeSysDevIpFilterName=mpeSysDevIpFilterName, mpeSysDevIpFilterNumOfDynamicRules=mpeSysDevIpFilterNumOfDynamicRules, mpeSysDevMaxNumOfInputIpFilters=mpeSysDevMaxNumOfInputIpFilters, mpeSysDevIpDefFilterAction=mpeSysDevIpDefFilterAction, mpeSysDevIpFilterRuleMaxDestPortNum=mpeSysDevIpFilterRuleMaxDestPortNum, mpeSysDevIpFilterRuleDestAddrCompEnable=mpeSysDevIpFilterRuleDestAddrCompEnable, mpeSysDevIpFilterRuleProtocolTypeUdp=mpeSysDevIpFilterRuleProtocolTypeUdp)
