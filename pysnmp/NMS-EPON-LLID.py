#
# PySNMP MIB module NMS-EPON-LLID (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-LLID
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, iso, Integer32, ModuleIdentity, Unsigned32, IpAddress, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "iso", "Integer32", "ModuleIdentity", "Unsigned32", "IpAddress", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "Counter32")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
nmsEponLlid = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9))
nmseponllidTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1), )
if mibBuilder.loadTexts: nmseponllidTable.setStatus('mandatory')
nmsEponLlidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1), ).setIndexNames((0, "NMS-EPON-LLID", "llidIfIndex"))
if mibBuilder.loadTexts: nmsEponLlidEntry.setStatus('mandatory')
llidIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidIfIndex.setStatus('mandatory')
llidToEponPortDiid = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidToEponPortDiid.setStatus('mandatory')
llidsequenceNo = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidsequenceNo.setStatus('mandatory')
llidEncrypStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidEncrypStatus.setStatus('mandatory')
llidCtcOamExtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidCtcOamExtStatus.setStatus('mandatory')
llidCtcOamExtOui = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidCtcOamExtOui.setStatus('mandatory')
llidCtcOamExtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidCtcOamExtVersion.setStatus('mandatory')
llidIfPIR = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfPIR.setStatus('mandatory')
llidIfCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfCIR.setStatus('mandatory')
llidIfFIR = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfFIR.setStatus('mandatory')
llidIfConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llidIfConfigRowStatus.setStatus('mandatory')
llidIfDynamicMacLearningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfDynamicMacLearningStatus.setStatus('mandatory')
llidIfDynamicMacLearningLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfDynamicMacLearningLimit.setStatus('mandatory')
llidIfDynamicMacLearningNumberLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfDynamicMacLearningNumberLimit.setStatus('mandatory')
llidIfQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 15), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfQosPolicy.setStatus('mandatory')
llidIfACL = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 16), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfACL.setStatus('mandatory')
llidDownStreamPir = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidDownStreamPir.setStatus('mandatory')
llidDownStreamCir = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidDownStreamCir.setStatus('mandatory')
llidDownStreamFir = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidDownStreamFir.setStatus('mandatory')
llidDownStreamIfRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llidDownStreamIfRowstatus.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-LLID", nmsEponLlidEntry=nmsEponLlidEntry, llidsequenceNo=llidsequenceNo, llidIfDynamicMacLearningLimit=llidIfDynamicMacLearningLimit, llidIfACL=llidIfACL, llidDownStreamCir=llidDownStreamCir, nmseponllidTable=nmseponllidTable, llidIfCIR=llidIfCIR, llidToEponPortDiid=llidToEponPortDiid, llidDownStreamIfRowstatus=llidDownStreamIfRowstatus, llidIfIndex=llidIfIndex, llidCtcOamExtOui=llidCtcOamExtOui, llidIfConfigRowStatus=llidIfConfigRowStatus, llidEncrypStatus=llidEncrypStatus, llidIfDynamicMacLearningNumberLimit=llidIfDynamicMacLearningNumberLimit, llidIfDynamicMacLearningStatus=llidIfDynamicMacLearningStatus, llidIfPIR=llidIfPIR, llidCtcOamExtStatus=llidCtcOamExtStatus, llidDownStreamFir=llidDownStreamFir, llidIfQosPolicy=llidIfQosPolicy, nmsEponLlid=nmsEponLlid, llidDownStreamPir=llidDownStreamPir, llidCtcOamExtVersion=llidCtcOamExtVersion, llidIfFIR=llidIfFIR)