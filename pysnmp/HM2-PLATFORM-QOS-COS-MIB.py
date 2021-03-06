#
# PySNMP MIB module HM2-PLATFORM-QOS-COS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-QOS-COS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hm2PlatformQoS, = mibBuilder.importSymbols("HM2-PLATFORM-QOS-MIB", "hm2PlatformQoS")
HmEnabledStatus, = mibBuilder.importSymbols("HM2-TC-MIB", "HmEnabledStatus")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, IpAddress, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, iso, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "IpAddress", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "iso", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2PlatformQosCos = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 3, 3))
hm2PlatformQosCos.setRevisions(('2011-10-12 00:00',))
if mibBuilder.loadTexts: hm2PlatformQosCos.setLastUpdated('201110120000Z')
if mibBuilder.loadTexts: hm2PlatformQosCos.setOrganization('Hirschmann Automation and Control GmbH')
class Percent(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class Sixteenths(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

hm2AgentCosMapCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1))
hm2AgentCosMapIpPrecTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1), )
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecTable.setStatus('current')
hm2AgentCosMapIpPrecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpPrecIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpPrecValue"))
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecEntry.setStatus('current')
hm2AgentCosMapIpPrecIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecIntfIndex.setStatus('current')
hm2AgentCosMapIpPrecValue = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecValue.setStatus('current')
hm2AgentCosMapIpPrecTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecTrafficClass.setStatus('current')
hm2AgentCosMapIpDscpTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2), )
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpTable.setStatus('current')
hm2AgentCosMapIpDscpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpDscpIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpDscpValue"))
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpEntry.setStatus('current')
hm2AgentCosMapIpDscpIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpIntfIndex.setStatus('current')
hm2AgentCosMapIpDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpValue.setStatus('current')
hm2AgentCosMapIpDscpTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpTrafficClass.setStatus('current')
hm2AgentCosMapIntfTrustTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3), )
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustTable.setStatus('current')
hm2AgentCosMapIntfTrustEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIntfTrustIntfIndex"))
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustEntry.setStatus('current')
hm2AgentCosMapIntfTrustIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustIntfIndex.setStatus('current')
hm2AgentCosMapIntfTrustMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("untrusted", 1), ("trustDot1p", 2), ("trustIpPrecedence", 3), ("trustIpDscp", 4))).clone('trustDot1p')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustMode.setStatus('current')
hm2AgentCosMapUntrustedTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosMapUntrustedTrafficClass.setStatus('current')
hm2AgentCosQueueCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2))
hm2AgentCosQueueNumQueuesPerPort = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosQueueNumQueuesPerPort.setStatus('current')
hm2AgentCosQueueNumDropPrecedenceLevels = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosQueueNumDropPrecedenceLevels.setStatus('current')
hm2AgentCosQueueControlTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3), )
if mibBuilder.loadTexts: hm2AgentCosQueueControlTable.setStatus('current')
hm2AgentCosQueueControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"))
if mibBuilder.loadTexts: hm2AgentCosQueueControlEntry.setStatus('current')
hm2AgentCosQueueIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosQueueIntfIndex.setStatus('current')
hm2AgentCosQueueIntfShapingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueIntfShapingRate.setStatus('current')
hm2AgentCosQueueMgmtTypeIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("taildrop", 1), ("wred", 2))).clone('taildrop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTypeIntf.setStatus('current')
hm2AgentCosQueueWredDecayExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(9)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueWredDecayExponent.setStatus('current')
hm2AgentCosQueueDefaultsRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 5), HmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueDefaultsRestore.setStatus('current')
hm2AgentCosQueueIntfShapingRateUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("percent", 1), ("kbps", 2))).clone('percent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosQueueIntfShapingRateUnits.setStatus('current')
hm2AgentCosQueueTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4), )
if mibBuilder.loadTexts: hm2AgentCosQueueTable.setStatus('current')
hm2AgentCosQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIndex"))
if mibBuilder.loadTexts: hm2AgentCosQueueEntry.setStatus('current')
hm2AgentCosQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hm2AgentCosQueueIndex.setStatus('current')
hm2AgentCosQueueSchedulerType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("weighted", 2))).clone('strict')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueSchedulerType.setStatus('current')
hm2AgentCosQueueMinBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 3), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMinBandwidth.setStatus('current')
hm2AgentCosQueueMaxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 4), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMaxBandwidth.setStatus('current')
hm2AgentCosQueueMgmtType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("taildrop", 1), ("wred", 2))).clone('taildrop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtType.setStatus('current')
hm2AgentCosQueueMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5), )
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTable.setStatus('current')
hm2AgentCosQueueMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueDropPrecIndex"))
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtEntry.setStatus('current')
hm2AgentCosQueueDropPrecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hm2AgentCosQueueDropPrecIndex.setStatus('current')
hm2AgentCosQueueMgmtTailDropThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 2), Sixteenths()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTailDropThreshold.setStatus('obsolete')
hm2AgentCosQueueMgmtWredMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 3), Sixteenths()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredMinThreshold.setStatus('obsolete')
hm2AgentCosQueueMgmtWredMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 4), Sixteenths()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredMaxThreshold.setStatus('obsolete')
hm2AgentCosQueueMgmtWredDropProbScale = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredDropProbScale.setStatus('obsolete')
hm2AgentCosQueueMgmtPercentTailDropThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 6), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentTailDropThreshold.setStatus('current')
hm2AgentCosQueueMgmtPercentWredMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 7), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentWredMinThreshold.setStatus('current')
hm2AgentCosQueueMgmtPercentWredMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 8), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentWredMaxThreshold.setStatus('current')
hm2AgentCosQueueMgmtWredDropProbability = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 9), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredDropProbability.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-QOS-COS-MIB", hm2AgentCosQueueDropPrecIndex=hm2AgentCosQueueDropPrecIndex, hm2AgentCosQueueMgmtTable=hm2AgentCosQueueMgmtTable, hm2AgentCosQueueIntfIndex=hm2AgentCosQueueIntfIndex, hm2AgentCosQueueMgmtType=hm2AgentCosQueueMgmtType, hm2AgentCosMapIpPrecTrafficClass=hm2AgentCosMapIpPrecTrafficClass, hm2AgentCosQueueSchedulerType=hm2AgentCosQueueSchedulerType, hm2AgentCosMapIntfTrustIntfIndex=hm2AgentCosMapIntfTrustIntfIndex, hm2AgentCosMapIpPrecValue=hm2AgentCosMapIpPrecValue, hm2AgentCosMapIpDscpTrafficClass=hm2AgentCosMapIpDscpTrafficClass, hm2AgentCosQueueCfgGroup=hm2AgentCosQueueCfgGroup, hm2AgentCosQueueControlTable=hm2AgentCosQueueControlTable, hm2AgentCosMapIpPrecTable=hm2AgentCosMapIpPrecTable, hm2AgentCosQueueMgmtTailDropThreshold=hm2AgentCosQueueMgmtTailDropThreshold, hm2AgentCosMapIntfTrustMode=hm2AgentCosMapIntfTrustMode, hm2AgentCosMapIpDscpEntry=hm2AgentCosMapIpDscpEntry, hm2AgentCosQueueControlEntry=hm2AgentCosQueueControlEntry, hm2AgentCosQueueIntfShapingRate=hm2AgentCosQueueIntfShapingRate, hm2AgentCosQueueIndex=hm2AgentCosQueueIndex, Sixteenths=Sixteenths, hm2AgentCosQueueMgmtTypeIntf=hm2AgentCosQueueMgmtTypeIntf, hm2AgentCosQueueEntry=hm2AgentCosQueueEntry, hm2AgentCosQueueMgmtWredMinThreshold=hm2AgentCosQueueMgmtWredMinThreshold, hm2AgentCosMapCfgGroup=hm2AgentCosMapCfgGroup, hm2AgentCosQueueMgmtWredMaxThreshold=hm2AgentCosQueueMgmtWredMaxThreshold, hm2AgentCosMapIpDscpTable=hm2AgentCosMapIpDscpTable, PYSNMP_MODULE_ID=hm2PlatformQosCos, hm2AgentCosMapIpDscpIntfIndex=hm2AgentCosMapIpDscpIntfIndex, hm2AgentCosQueueTable=hm2AgentCosQueueTable, hm2AgentCosQueueMgmtPercentTailDropThreshold=hm2AgentCosQueueMgmtPercentTailDropThreshold, hm2AgentCosQueueMgmtWredDropProbScale=hm2AgentCosQueueMgmtWredDropProbScale, hm2AgentCosMapIntfTrustEntry=hm2AgentCosMapIntfTrustEntry, hm2AgentCosQueueDefaultsRestore=hm2AgentCosQueueDefaultsRestore, Percent=Percent, hm2AgentCosMapIpPrecEntry=hm2AgentCosMapIpPrecEntry, hm2AgentCosQueueNumQueuesPerPort=hm2AgentCosQueueNumQueuesPerPort, hm2AgentCosQueueMgmtPercentWredMinThreshold=hm2AgentCosQueueMgmtPercentWredMinThreshold, hm2AgentCosQueueIntfShapingRateUnits=hm2AgentCosQueueIntfShapingRateUnits, hm2AgentCosQueueMgmtPercentWredMaxThreshold=hm2AgentCosQueueMgmtPercentWredMaxThreshold, hm2AgentCosQueueWredDecayExponent=hm2AgentCosQueueWredDecayExponent, hm2AgentCosMapUntrustedTrafficClass=hm2AgentCosMapUntrustedTrafficClass, hm2AgentCosQueueMgmtWredDropProbability=hm2AgentCosQueueMgmtWredDropProbability, hm2AgentCosQueueMgmtEntry=hm2AgentCosQueueMgmtEntry, hm2AgentCosMapIntfTrustTable=hm2AgentCosMapIntfTrustTable, hm2AgentCosQueueMinBandwidth=hm2AgentCosQueueMinBandwidth, hm2AgentCosQueueMaxBandwidth=hm2AgentCosQueueMaxBandwidth, hm2AgentCosQueueNumDropPrecedenceLevels=hm2AgentCosQueueNumDropPrecedenceLevels, hm2AgentCosMapIpDscpValue=hm2AgentCosMapIpDscpValue, hm2PlatformQosCos=hm2PlatformQosCos, hm2AgentCosMapIpPrecIntfIndex=hm2AgentCosMapIpPrecIntfIndex)
