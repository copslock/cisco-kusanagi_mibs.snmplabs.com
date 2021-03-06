#
# PySNMP MIB module SHIVA-FP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHIVA-FP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:55:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
fastpath, = mibBuilder.importSymbols("SHIVA-MIB", "fastpath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Gauge32, Counter32, Unsigned32, NotificationType, Integer32, Counter64, TimeTicks, MibIdentifier, iso, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Counter32", "Unsigned32", "NotificationType", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "iso", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fpBuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 1))
fpConf = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 2))
k_star = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 3)).setLabel("k-star")
bufferSize = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferSize.setStatus('mandatory')
bufferAvail = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferAvail.setStatus('mandatory')
bufferDrops = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferDrops.setStatus('mandatory')
bufferTypeTable = MibTable((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4), )
if mibBuilder.loadTexts: bufferTypeTable.setStatus('mandatory')
bufferTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1), ).setIndexNames((0, "SHIVA-FP-MIB", "bufferTypeIndex"))
if mibBuilder.loadTexts: bufferTypeEntry.setStatus('mandatory')
bufferTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeIndex.setStatus('mandatory')
bufferTypeType = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("other", 1), ("free", 2), ("localtalk", 3), ("ethernet", 4), ("arp", 5), ("data", 6), ("erbf", 7), ("etbf", 8), ("malloc", 9), ("serial", 10), ("tokenring", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeType.setStatus('mandatory')
bufferTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeDescr.setStatus('mandatory')
bufferTypeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeCount.setStatus('mandatory')
bufferTypeDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeDrops.setStatus('mandatory')
bufferTypeRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeRequests.setStatus('mandatory')
bufferTypeMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeMaximum.setStatus('mandatory')
confReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 1), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confReboot.setStatus('mandatory')
confCheckSum = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confCheckSum.setStatus('mandatory')
codeCheckSum = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: codeCheckSum.setStatus('mandatory')
promVersion = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: promVersion.setStatus('mandatory')
hwStatus = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStatus.setStatus('mandatory')
confWhyReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("hardware", 2), ("firmware", 3), ("software", 4), ("config", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confWhyReboot.setStatus('mandatory')
confWhoReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confWhoReboot.setStatus('mandatory')
confRebootComment = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confRebootComment.setStatus('mandatory')
confHowReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("cold", 1), ("warm", 2), ("ramdl", 3), ("reset", 4), ("romdl", 5), ("dl", 6), ("bstrap", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confHowReboot.setStatus('mandatory')
confSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confSerialNum.setStatus('mandatory')
mibBuilder.exportSymbols("SHIVA-FP-MIB", promVersion=promVersion, confHowReboot=confHowReboot, bufferSize=bufferSize, bufferTypeCount=bufferTypeCount, bufferAvail=bufferAvail, fpConf=fpConf, confWhyReboot=confWhyReboot, k_star=k_star, bufferTypeMaximum=bufferTypeMaximum, confRebootComment=confRebootComment, confReboot=confReboot, bufferTypeDescr=bufferTypeDescr, bufferTypeEntry=bufferTypeEntry, confWhoReboot=confWhoReboot, confSerialNum=confSerialNum, bufferTypeTable=bufferTypeTable, confCheckSum=confCheckSum, bufferTypeIndex=bufferTypeIndex, bufferTypeType=bufferTypeType, bufferTypeDrops=bufferTypeDrops, fpBuffer=fpBuffer, bufferDrops=bufferDrops, bufferTypeRequests=bufferTypeRequests, hwStatus=hwStatus, codeCheckSum=codeCheckSum)
