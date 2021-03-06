#
# PySNMP MIB module H3C-QOS-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-QOS-PROFILE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, IpAddress, iso, Integer32, Bits, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "iso", "Integer32", "Bits", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "TimeTicks")
MacAddress, TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
h3cQosProfile = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17))
if mibBuilder.loadTexts: h3cQosProfile.setLastUpdated('200407060000Z')
if mibBuilder.loadTexts: h3cQosProfile.setOrganization('Huawei-3com Technologies co.,Ltd.')
class H3cQoSDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("invalid", 0), ("input", 1), ("ouput", 2))

h3cQoSProfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1))
h3cQoSProf = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 1))
h3cQoSProfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 1, 1), )
if mibBuilder.loadTexts: h3cQoSProfTable.setStatus('current')
h3cQoSProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 1, 1, 1), ).setIndexNames((0, "H3C-QOS-PROFILE-MIB", "h3cQoSProfIndex"))
if mibBuilder.loadTexts: h3cQoSProfEntry.setStatus('current')
h3cQoSProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSProfIndex.setStatus('current')
h3cQoSProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSProfName.setStatus('current')
h3cQoSProfActionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSProfActionNumber.setStatus('current')
h3cQoSProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSProfRowStatus.setStatus('current')
h3cQoSAction = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2))
h3cQoSTrafficLimitTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1), )
if mibBuilder.loadTexts: h3cQoSTrafficLimitTable.setStatus('current')
h3cQoSTrafficLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1), ).setIndexNames((0, "H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtProfIndex"), (0, "H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtActionIndex"))
if mibBuilder.loadTexts: h3cQoSTrafficLimitEntry.setStatus('current')
h3cQoSTrafLmtProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSTrafLmtProfIndex.setStatus('current')
h3cQoSTrafLmtActionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSTrafLmtActionIndex.setStatus('current')
h3cQoSTrafLmtDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 3), H3cQoSDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtDirection.setStatus('current')
h3cQoSTrafLmtUserAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 5999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtUserAclNum.setStatus('current')
h3cQoSTrafLmtUserAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtUserAclRule.setStatus('current')
h3cQoSTrafLmtIpAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtIpAclNum.setStatus('current')
h3cQoSTrafLmtIpAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtIpAclRule.setStatus('current')
h3cQoSTrafLmtLinkAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(4000, 4999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtLinkAclNum.setStatus('current')
h3cQoSTrafLmtLinkAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtLinkAclRule.setStatus('current')
h3cQoSTrafLmtTargetRateMbps = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtTargetRateMbps.setStatus('current')
h3cQoSTrafLmtTargetRateKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtTargetRateKbps.setStatus('current')
h3cQoSTrafLmtPeakRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 8388608), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtPeakRate.setStatus('current')
h3cQoSTrafLmtCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 34120000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtCIR.setStatus('current')
h3cQoSTrafLmtCBS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtCBS.setStatus('current')
h3cQoSTrafLmtEBS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtEBS.setStatus('current')
h3cQoSTrafLmtPIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 34120000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtPIR.setStatus('current')
h3cQoSTrafLmtConformLocalPre = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtConformLocalPre.setStatus('current')
h3cQoSTrafLmtConformActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 0), ("remark-cos", 1), ("remark-drop-priority", 2), ("remark-cos-drop-priority", 3), ("remark-policed-service", 4), ("remark-dscp", 5))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtConformActionType.setStatus('current')
h3cQoSTrafLmtExceedActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 0), ("forward", 1), ("drop", 2), ("remarkdscp", 3), ("exceed-cos", 4))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtExceedActionType.setStatus('current')
h3cQoSTrafLmtExceedDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 63), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtExceedDscp.setStatus('current')
h3cQoSTrafLmtExceedCos = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtExceedCos.setStatus('current')
h3cQoSTrafLmtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 22), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtRowStatus.setStatus('current')
h3cQoSTrafLmtConformCos = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtConformCos.setStatus('current')
h3cQoSTrafLmtConformDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 63), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafLmtConformDscp.setStatus('current')
h3cQoSTrafficPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2), )
if mibBuilder.loadTexts: h3cQoSTrafficPriorityTable.setStatus('current')
h3cQoSTrafficPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1), ).setIndexNames((0, "H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioProfIndex"), (0, "H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioActionIndex"))
if mibBuilder.loadTexts: h3cQoSTrafficPriorityEntry.setStatus('current')
h3cQoSTrafPrioProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSTrafPrioProfIndex.setStatus('current')
h3cQoSTrafPrioActionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSTrafPrioActionIndex.setStatus('current')
h3cQoSTrafPrioDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 3), H3cQoSDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioDirection.setStatus('current')
h3cQoSTrafPrioUserAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 5999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioUserAclNum.setStatus('current')
h3cQoSTrafPrioUserAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioUserAclRule.setStatus('current')
h3cQoSTrafPrioIpAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioIpAclNum.setStatus('current')
h3cQoSTrafPrioIpAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioIpAclRule.setStatus('current')
h3cQoSTrafPrioLinkAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(4000, 4999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioLinkAclNum.setStatus('current')
h3cQoSTrafPrioLinkAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioLinkAclRule.setStatus('current')
h3cQoSTrafPrioDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 63), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioDscp.setStatus('current')
h3cQoSTrafPrioIpPre = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioIpPre.setStatus('current')
h3cQoSTrafPrioIpPreFromCos = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 12), TruthValue().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioIpPreFromCos.setStatus('current')
h3cQoSTrafPrioCos = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioCos.setStatus('current')
h3cQoSTrafPrioCosFromIpPre = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 14), TruthValue().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioCosFromIpPre.setStatus('current')
h3cQoSTrafPrioLocalPre = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioLocalPre.setStatus('current')
h3cQoSTrafPrioPolicedServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 0), ("trust-dscp", 2), ("new-dscp", 3), ("untrusted", 4))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioPolicedServiceType.setStatus('current')
h3cQoSTrafPrioPolicedServiceDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 63), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioPolicedServiceDscp.setStatus('current')
h3cQoSTrafPrioPolicedServiceExp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioPolicedServiceExp.setStatus('current')
h3cQoSTrafPrioPolicedServiceCos = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioPolicedServiceCos.setStatus('current')
h3cQoSTrafPrioPolicedServiceLoaclPre = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioPolicedServiceLoaclPre.setStatus('current')
h3cQoSTrafPrioPolicedServiceDropPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 2), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioPolicedServiceDropPriority.setStatus('current')
h3cQoSTrafPrioRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 2, 1, 22), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafPrioRowStatus.setStatus('current')
h3cQoSTrafficFilterTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3), )
if mibBuilder.loadTexts: h3cQoSTrafficFilterTable.setStatus('current')
h3cQoSTrafficFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1), ).setIndexNames((0, "H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterProfIndex"), (0, "H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterActionIndex"))
if mibBuilder.loadTexts: h3cQoSTrafficFilterEntry.setStatus('current')
h3cQoSTrafFilterProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSTrafFilterProfIndex.setStatus('current')
h3cQoSTrafFilterActionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSTrafFilterActionIndex.setStatus('current')
h3cQoSTrafFilterDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 3), H3cQoSDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterDirection.setStatus('current')
h3cQoSTrafFilterUserAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 5999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterUserAclNum.setStatus('current')
h3cQoSTrafFilterUserAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterUserAclRule.setStatus('current')
h3cQoSTrafFilterIpAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterIpAclNum.setStatus('current')
h3cQoSTrafFilterIpAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterIpAclRule.setStatus('current')
h3cQoSTrafFilterLinkAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(4000, 4999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterLinkAclNum.setStatus('current')
h3cQoSTrafFilterLinkAclRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterLinkAclRule.setStatus('current')
h3cQoSTrafFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 2, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSTrafFilterRowStatus.setStatus('current')
h3cQoSProfPortMapping = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3))
h3cQoSProfPortMappingTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 1), )
if mibBuilder.loadTexts: h3cQoSProfPortMappingTable.setStatus('current')
h3cQoSProfPortMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 1, 1), ).setIndexNames((0, "H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingIfIndex"), (0, "H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingProfIndex"))
if mibBuilder.loadTexts: h3cQoSProfPortMappingEntry.setStatus('current')
h3cQoSProfPortMappingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cQoSProfPortMappingIfIndex.setStatus('current')
h3cQoSProfPortMappingProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cQoSProfPortMappingProfIndex.setStatus('current')
h3cQoSProfPortMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cQoSProfPortMappingRowStatus.setStatus('current')
h3cQoSProfPortMappingModeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 2), )
if mibBuilder.loadTexts: h3cQoSProfPortMappingModeTable.setStatus('current')
h3cQoSProfPortMappingModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 2, 1), ).setIndexNames((0, "H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingModeIfIndex"))
if mibBuilder.loadTexts: h3cQoSProfPortMappingModeEntry.setStatus('current')
h3cQoSProfPortMappingModeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cQoSProfPortMappingModeIfIndex.setStatus('current')
h3cQoSProfPortMappingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("user-based", 1), ("port-based", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cQoSProfPortMappingMode.setStatus('current')
h3cQoSProfDynPortMappingTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3), )
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingTable.setStatus('current')
h3cQoSProfDynPortMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3, 1), ).setIndexNames((0, "H3C-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingIfIndex"), (0, "H3C-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserSrcMAC"))
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingEntry.setStatus('current')
h3cQoSProfDynPortMappingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingIfIndex.setStatus('current')
h3cQoSProfDynPortMappingUserSrcMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3, 1, 2), MacAddress())
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingUserSrcMAC.setStatus('current')
h3cQoSProfDynPortMappingUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingUserName.setStatus('current')
h3cQoSProfDynPortMappingUserIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingUserIPAddr.setStatus('current')
h3cQoSProfDynPortMappingUserVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingUserVLANID.setStatus('current')
h3cQoSProfDynPortMappingUserProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 1, 3, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cQoSProfDynPortMappingUserProfName.setStatus('current')
h3cQoSProfPortMappingTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 2))
h3cQoSProfPortMappingError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 2, 1))
if mibBuilder.loadTexts: h3cQoSProfPortMappingError.setStatus('current')
h3cQoSProfMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3))
h3cQoSProfMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3, 1))
h3cQoSProfMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3, 1, 1)).setObjects(("H3C-QOS-PROFILE-MIB", "h3cQoSProfGroup"), ("H3C-QOS-PROFILE-MIB", "h3cQoSActionGroup"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingGroup"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingTrapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cQoSProfMibCompliance = h3cQoSProfMibCompliance.setStatus('current')
h3cQoSProfMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3, 2))
h3cQoSProfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3, 2, 1)).setObjects(("H3C-QOS-PROFILE-MIB", "h3cQoSProfName"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfActionNumber"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cQoSProfGroup = h3cQoSProfGroup.setStatus('current')
h3cQoSActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3, 2, 2)).setObjects(("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtDirection"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtUserAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtUserAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtIpAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtIpAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtLinkAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtLinkAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtTargetRateMbps"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtTargetRateKbps"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtPeakRate"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtCIR"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtCBS"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtEBS"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtPIR"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformLocalPre"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformActionType"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtExceedActionType"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtExceedDscp"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtExceedCos"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtRowStatus"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformCos"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformDscp"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioDirection"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioUserAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioUserAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioLinkAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioLinkAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioDscp"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpPre"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpPreFromCos"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioCos"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioCosFromIpPre"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioLocalPre"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceType"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceDscp"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceExp"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceCos"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceLoaclPre"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceDropPriority"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafPrioRowStatus"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterDirection"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterUserAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterUserAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterIpAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterIpAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterLinkAclNum"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterLinkAclRule"), ("H3C-QOS-PROFILE-MIB", "h3cQoSTrafFilterRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cQoSActionGroup = h3cQoSActionGroup.setStatus('current')
h3cQoSProfPortMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3, 2, 3)).setObjects(("H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingRowStatus"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingMode"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserName"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserIPAddr"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserVLANID"), ("H3C-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserProfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cQoSProfPortMappingGroup = h3cQoSProfPortMappingGroup.setStatus('current')
h3cQoSProfPortMappingTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 17, 3, 2, 4)).setObjects(("H3C-QOS-PROFILE-MIB", "h3cQoSProfPortMappingError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cQoSProfPortMappingTrapsGroup = h3cQoSProfPortMappingTrapsGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-QOS-PROFILE-MIB", h3cQoSTrafficFilterTable=h3cQoSTrafficFilterTable, h3cQoSProfMibGroups=h3cQoSProfMibGroups, h3cQoSProfPortMappingIfIndex=h3cQoSProfPortMappingIfIndex, h3cQoSTrafLmtIpAclRule=h3cQoSTrafLmtIpAclRule, h3cQoSTrafLmtTargetRateKbps=h3cQoSTrafLmtTargetRateKbps, h3cQoSTrafFilterDirection=h3cQoSTrafFilterDirection, h3cQoSTrafLmtDirection=h3cQoSTrafLmtDirection, h3cQoSTrafPrioPolicedServiceLoaclPre=h3cQoSTrafPrioPolicedServiceLoaclPre, h3cQoSProfPortMappingProfIndex=h3cQoSProfPortMappingProfIndex, h3cQoSAction=h3cQoSAction, h3cQoSTrafPrioUserAclRule=h3cQoSTrafPrioUserAclRule, h3cQoSTrafFilterProfIndex=h3cQoSTrafFilterProfIndex, h3cQoSTrafPrioCosFromIpPre=h3cQoSTrafPrioCosFromIpPre, h3cQoSTrafPrioDscp=h3cQoSTrafPrioDscp, h3cQoSProfIndex=h3cQoSProfIndex, h3cQoSTrafFilterIpAclRule=h3cQoSTrafFilterIpAclRule, h3cQosProfile=h3cQosProfile, h3cQoSTrafficPriorityEntry=h3cQoSTrafficPriorityEntry, h3cQoSTrafLmtTargetRateMbps=h3cQoSTrafLmtTargetRateMbps, h3cQoSProfPortMappingRowStatus=h3cQoSProfPortMappingRowStatus, h3cQoSProfMibCompliance=h3cQoSProfMibCompliance, h3cQoSTrafLmtPIR=h3cQoSTrafLmtPIR, h3cQoSTrafPrioIpAclRule=h3cQoSTrafPrioIpAclRule, h3cQoSTrafLmtUserAclNum=h3cQoSTrafLmtUserAclNum, h3cQoSTrafPrioLinkAclRule=h3cQoSTrafPrioLinkAclRule, h3cQoSTrafLmtActionIndex=h3cQoSTrafLmtActionIndex, h3cQoSProfPortMappingMode=h3cQoSProfPortMappingMode, h3cQoSTrafPrioLocalPre=h3cQoSTrafPrioLocalPre, PYSNMP_MODULE_ID=h3cQosProfile, h3cQoSTrafLmtConformCos=h3cQoSTrafLmtConformCos, h3cQoSTrafFilterActionIndex=h3cQoSTrafFilterActionIndex, h3cQoSTrafLmtProfIndex=h3cQoSTrafLmtProfIndex, h3cQoSTrafFilterLinkAclNum=h3cQoSTrafFilterLinkAclNum, h3cQoSTrafFilterRowStatus=h3cQoSTrafFilterRowStatus, h3cQoSProfPortMappingError=h3cQoSProfPortMappingError, h3cQoSTrafficLimitTable=h3cQoSTrafficLimitTable, h3cQoSTrafLmtExceedActionType=h3cQoSTrafLmtExceedActionType, h3cQoSProfMibCompliances=h3cQoSProfMibCompliances, h3cQoSTrafPrioPolicedServiceExp=h3cQoSTrafPrioPolicedServiceExp, h3cQoSTrafPrioActionIndex=h3cQoSTrafPrioActionIndex, h3cQoSProfDynPortMappingEntry=h3cQoSProfDynPortMappingEntry, h3cQoSTrafLmtConformLocalPre=h3cQoSTrafLmtConformLocalPre, h3cQoSProfRowStatus=h3cQoSProfRowStatus, h3cQoSProfPortMappingTrapsGroup=h3cQoSProfPortMappingTrapsGroup, h3cQoSProfDynPortMappingUserVLANID=h3cQoSProfDynPortMappingUserVLANID, h3cQoSProfActionNumber=h3cQoSProfActionNumber, h3cQoSTrafLmtExceedCos=h3cQoSTrafLmtExceedCos, h3cQoSTrafLmtUserAclRule=h3cQoSTrafLmtUserAclRule, h3cQoSTrafFilterUserAclNum=h3cQoSTrafFilterUserAclNum, h3cQoSProfDynPortMappingUserIPAddr=h3cQoSProfDynPortMappingUserIPAddr, h3cQoSProfDynPortMappingUserSrcMAC=h3cQoSProfDynPortMappingUserSrcMAC, h3cQoSProfName=h3cQoSProfName, h3cQoSTrafLmtRowStatus=h3cQoSTrafLmtRowStatus, h3cQoSTrafPrioPolicedServiceDscp=h3cQoSTrafPrioPolicedServiceDscp, h3cQoSTrafPrioPolicedServiceType=h3cQoSTrafPrioPolicedServiceType, h3cQoSTrafLmtLinkAclNum=h3cQoSTrafLmtLinkAclNum, h3cQoSTrafPrioDirection=h3cQoSTrafPrioDirection, h3cQoSProfDynPortMappingUserProfName=h3cQoSProfDynPortMappingUserProfName, h3cQoSProfDynPortMappingUserName=h3cQoSProfDynPortMappingUserName, h3cQoSTrafLmtIpAclNum=h3cQoSTrafLmtIpAclNum, h3cQoSTrafficFilterEntry=h3cQoSTrafficFilterEntry, h3cQoSProfPortMappingTraps=h3cQoSProfPortMappingTraps, h3cQoSTrafLmtConformActionType=h3cQoSTrafLmtConformActionType, h3cQoSTrafFilterUserAclRule=h3cQoSTrafFilterUserAclRule, h3cQoSTrafPrioPolicedServiceDropPriority=h3cQoSTrafPrioPolicedServiceDropPriority, h3cQoSTrafLmtLinkAclRule=h3cQoSTrafLmtLinkAclRule, h3cQoSTrafficPriorityTable=h3cQoSTrafficPriorityTable, h3cQoSTrafPrioIpPre=h3cQoSTrafPrioIpPre, h3cQoSProf=h3cQoSProf, h3cQoSTrafLmtCIR=h3cQoSTrafLmtCIR, h3cQoSTrafPrioUserAclNum=h3cQoSTrafPrioUserAclNum, h3cQoSProfObjects=h3cQoSProfObjects, h3cQoSActionGroup=h3cQoSActionGroup, h3cQoSTrafLmtPeakRate=h3cQoSTrafLmtPeakRate, h3cQoSTrafPrioIpPreFromCos=h3cQoSTrafPrioIpPreFromCos, h3cQoSProfEntry=h3cQoSProfEntry, h3cQoSTrafFilterIpAclNum=h3cQoSTrafFilterIpAclNum, h3cQoSTrafLmtConformDscp=h3cQoSTrafLmtConformDscp, h3cQoSTrafPrioLinkAclNum=h3cQoSTrafPrioLinkAclNum, h3cQoSTrafPrioCos=h3cQoSTrafPrioCos, h3cQoSProfPortMappingModeTable=h3cQoSProfPortMappingModeTable, h3cQoSTrafLmtExceedDscp=h3cQoSTrafLmtExceedDscp, h3cQoSProfTable=h3cQoSProfTable, h3cQoSProfPortMappingModeIfIndex=h3cQoSProfPortMappingModeIfIndex, h3cQoSProfPortMappingEntry=h3cQoSProfPortMappingEntry, h3cQoSTrafFilterLinkAclRule=h3cQoSTrafFilterLinkAclRule, h3cQoSTrafPrioProfIndex=h3cQoSTrafPrioProfIndex, h3cQoSProfPortMappingGroup=h3cQoSProfPortMappingGroup, h3cQoSProfDynPortMappingIfIndex=h3cQoSProfDynPortMappingIfIndex, h3cQoSProfDynPortMappingTable=h3cQoSProfDynPortMappingTable, h3cQoSProfGroup=h3cQoSProfGroup, h3cQoSTrafLmtCBS=h3cQoSTrafLmtCBS, h3cQoSProfPortMappingModeEntry=h3cQoSProfPortMappingModeEntry, h3cQoSTrafPrioRowStatus=h3cQoSTrafPrioRowStatus, h3cQoSProfPortMappingTable=h3cQoSProfPortMappingTable, h3cQoSTrafficLimitEntry=h3cQoSTrafficLimitEntry, h3cQoSProfMibConformance=h3cQoSProfMibConformance, h3cQoSTrafPrioIpAclNum=h3cQoSTrafPrioIpAclNum, H3cQoSDirection=H3cQoSDirection, h3cQoSProfPortMapping=h3cQoSProfPortMapping, h3cQoSTrafLmtEBS=h3cQoSTrafLmtEBS, h3cQoSTrafPrioPolicedServiceCos=h3cQoSTrafPrioPolicedServiceCos)
