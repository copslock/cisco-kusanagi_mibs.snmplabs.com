#
# PySNMP MIB module TIARA-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Unsigned32, Gauge32, ObjectIdentity, iso, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Unsigned32", "Gauge32", "ObjectIdentity", "iso", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Bits")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
tiaraIpIfIndex, = mibBuilder.importSymbols("TIARA-IP-MIB", "tiaraIpIfIndex")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraQosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 17))
tiaraQosMib.setRevisions(('1900-02-07 00:00',))
if mibBuilder.loadTexts: tiaraQosMib.setLastUpdated('0006100000Z')
if mibBuilder.loadTexts: tiaraQosMib.setOrganization('Tiara Networks Inc.')
tiaraRedConfigTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1), )
if mibBuilder.loadTexts: tiaraRedConfigTable.setStatus('current')
tiaraRedConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"))
if mibBuilder.loadTexts: tiaraRedConfigEntry.setStatus('current')
redTxMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxMaxThreshold.setStatus('current')
redTxMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxMinThreshold.setStatus('current')
redTxWqBiasFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxWqBiasFactor.setStatus('current')
redTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxEnable.setStatus('current')
tiaraRedStatTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2), )
if mibBuilder.loadTexts: tiaraRedStatTable.setStatus('current')
tiaraRedStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"))
if mibBuilder.loadTexts: tiaraRedStatEntry.setStatus('current')
redTxLoanedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxLoanedCount.setStatus('current')
redTxMaxLoanedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMaxLoanedCount.setStatus('current')
redTxAvgQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxAvgQueueSize.setStatus('current')
redTxMaxAvgQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMaxAvgQueueSize.setStatus('current')
redTxDropRate = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxDropRate.setStatus('current')
redTxMinThresholdSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMinThresholdSuccess.setStatus('current')
redTxMaxThresholdFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMaxThresholdFailure.setStatus('current')
redTxMinMaxRangeSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMinMaxRangeSuccess.setStatus('current')
redTxMinMaxRangeFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMinMaxRangeFailure.setStatus('current')
redTxControlSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxControlSuccess.setStatus('current')
tiaraCbqConfigTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3), )
if mibBuilder.loadTexts: tiaraCbqConfigTable.setStatus('current')
tiaraCbqConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"), (0, "TIARA-QOS-MIB", "cbqClassIndex"))
if mibBuilder.loadTexts: tiaraCbqConfigEntry.setStatus('current')
cbqClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassIndex.setStatus('current')
cbqClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassName.setStatus('current')
cbqClassParentName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassParentName.setStatus('current')
cbqClassBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBandwidth.setStatus('current')
cbqClassBurstTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBurstTolerance.setStatus('current')
cbqClassKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("cbqClassifyTypeNotSet", 1), ("cbqClassifySrcIp", 2), ("cbqClassifyDestIp", 3), ("cbqClassifySrcPort", 4), ("cbqClassifyDestPort", 5), ("cbqClassifyProtocolType", 6), ("cbqClassifyVlanId", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyType.setStatus('current')
cbqClassIsDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassIsDefault.setStatus('current')
cbqClassAverageBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassAverageBandwidth.setStatus('current')
tiaraCbqClassKeyTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4), )
if mibBuilder.loadTexts: tiaraCbqClassKeyTable.setStatus('current')
tiaraCbqClassKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"), (0, "TIARA-QOS-MIB", "cbqClassIndex"), (0, "TIARA-QOS-MIB", "cbqClassKeyIndex"))
if mibBuilder.loadTexts: tiaraCbqClassKeyTableEntry.setStatus('current')
cbqClassKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyIndex.setStatus('current')
cbqKeyClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqKeyClassName.setStatus('current')
cbqClassKeyVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyVlanId.setStatus('current')
cbqClassKeyIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyIpAddress.setStatus('current')
cbqClassKeyIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyIpNetMask.setStatus('current')
cbqClassKeyPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyPort.setStatus('current')
cbqClassKeyProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyProtocolType.setStatus('current')
tiaraCbqStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5), )
if mibBuilder.loadTexts: tiaraCbqStatsTable.setStatus('current')
tiaraCbqStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"), (0, "TIARA-QOS-MIB", "cbqClassIndex"))
if mibBuilder.loadTexts: tiaraCbqStatsEntry.setStatus('current')
cbqStatsClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqStatsClassName.setStatus('current')
cbqClassPacketsForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassPacketsForwarded.setStatus('current')
cbqClassBytesForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBytesForwarded.setStatus('current')
cbqClassPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassPacketsDropped.setStatus('current')
cbqClassBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBytesDropped.setStatus('current')
cbqClassBurstExceedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBurstExceedCount.setStatus('current')
mibBuilder.exportSymbols("TIARA-QOS-MIB", redTxWqBiasFactor=redTxWqBiasFactor, tiaraCbqStatsEntry=tiaraCbqStatsEntry, cbqClassIsDefault=cbqClassIsDefault, redTxMaxThresholdFailure=redTxMaxThresholdFailure, redTxMinThresholdSuccess=redTxMinThresholdSuccess, tiaraCbqConfigTable=tiaraCbqConfigTable, cbqClassBytesDropped=cbqClassBytesDropped, redTxAvgQueueSize=redTxAvgQueueSize, redTxMaxLoanedCount=redTxMaxLoanedCount, cbqClassBurstTolerance=cbqClassBurstTolerance, tiaraRedConfigEntry=tiaraRedConfigEntry, cbqClassKeyVlanId=cbqClassKeyVlanId, redTxControlSuccess=redTxControlSuccess, cbqClassBandwidth=cbqClassBandwidth, cbqStatsClassName=cbqStatsClassName, cbqClassPacketsForwarded=cbqClassPacketsForwarded, cbqClassPacketsDropped=cbqClassPacketsDropped, tiaraCbqClassKeyTableEntry=tiaraCbqClassKeyTableEntry, cbqClassKeyIpNetMask=cbqClassKeyIpNetMask, redTxLoanedCount=redTxLoanedCount, tiaraQosMib=tiaraQosMib, redTxDropRate=redTxDropRate, cbqKeyClassName=cbqKeyClassName, cbqClassKeyProtocolType=cbqClassKeyProtocolType, cbqClassKeyIndex=cbqClassKeyIndex, PYSNMP_MODULE_ID=tiaraQosMib, cbqClassBytesForwarded=cbqClassBytesForwarded, cbqClassAverageBandwidth=cbqClassAverageBandwidth, cbqClassName=cbqClassName, tiaraCbqStatsTable=tiaraCbqStatsTable, redTxMinMaxRangeFailure=redTxMinMaxRangeFailure, redTxMinMaxRangeSuccess=redTxMinMaxRangeSuccess, redTxMaxThreshold=redTxMaxThreshold, redTxMaxAvgQueueSize=redTxMaxAvgQueueSize, cbqClassBurstExceedCount=cbqClassBurstExceedCount, redTxMinThreshold=redTxMinThreshold, cbqClassKeyType=cbqClassKeyType, tiaraRedStatTable=tiaraRedStatTable, tiaraRedConfigTable=tiaraRedConfigTable, cbqClassParentName=cbqClassParentName, tiaraRedStatEntry=tiaraRedStatEntry, redTxEnable=redTxEnable, tiaraCbqClassKeyTable=tiaraCbqClassKeyTable, cbqClassKeyIpAddress=cbqClassKeyIpAddress, cbqClassKeyPort=cbqClassKeyPort, tiaraCbqConfigEntry=tiaraCbqConfigEntry, cbqClassIndex=cbqClassIndex)
