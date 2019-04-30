#
# PySNMP MIB module BDCOM-SYS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BDCOM-SYS
# Produced by pysmi-0.3.4 at Mon Apr 29 17:19:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
bdlocal, = mibBuilder.importSymbols("BDCOM-SMI", "bdlocal")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, ObjectIdentity, ModuleIdentity, NotificationType, Counter32, Counter64, Bits, Gauge32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter32", "Counter64", "Bits", "Gauge32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bdlsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 2, 1))
bdromId = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdromId.setStatus('mandatory')
bdwhyReload = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdwhyReload.setStatus('mandatory')
bdhostName = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdhostName.setStatus('mandatory')
bddomainName = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bddomainName.setStatus('mandatory')
bdauthAddr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdauthAddr.setStatus('mandatory')
bdbootHost = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbootHost.setStatus('mandatory')
bdping = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdping.setStatus('obsolete')
bdfreeMem = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdfreeMem.setStatus('obsolete')
bdbufferElFree = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferElFree.setStatus('mandatory')
bdbufferElMax = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferElMax.setStatus('mandatory')
bdbufferElHit = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferElHit.setStatus('mandatory')
bdbufferElMiss = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferElMiss.setStatus('mandatory')
bdbufferElCreate = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferElCreate.setStatus('mandatory')
bdbufferSmSize = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmSize.setStatus('mandatory')
bdbufferSmTotal = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmTotal.setStatus('mandatory')
bdbufferSmFree = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmFree.setStatus('mandatory')
bdbufferSmMax = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmMax.setStatus('mandatory')
bdbufferSmHit = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmHit.setStatus('mandatory')
bdbufferSmMiss = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmMiss.setStatus('mandatory')
bdbufferSmTrim = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmTrim.setStatus('mandatory')
bdbufferSmCreate = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferSmCreate.setStatus('mandatory')
bdbufferMdSize = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdSize.setStatus('mandatory')
bdbufferMdTotal = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdTotal.setStatus('mandatory')
bdbufferMdFree = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdFree.setStatus('mandatory')
bdbufferMdMax = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdMax.setStatus('mandatory')
bdbufferMdHit = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdHit.setStatus('mandatory')
bdbufferMdMiss = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdMiss.setStatus('mandatory')
bdbufferMdTrim = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdTrim.setStatus('mandatory')
bdbufferMdCreate = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferMdCreate.setStatus('mandatory')
bdbufferBgSize = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgSize.setStatus('mandatory')
bdbufferBgTotal = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgTotal.setStatus('mandatory')
bdbufferBgFree = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgFree.setStatus('mandatory')
bdbufferBgMax = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgMax.setStatus('mandatory')
bdbufferBgHit = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgHit.setStatus('mandatory')
bdbufferBgMiss = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgMiss.setStatus('mandatory')
bdbufferBgTrim = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgTrim.setStatus('mandatory')
bdbufferBgCreate = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferBgCreate.setStatus('mandatory')
bdbufferLgSize = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgSize.setStatus('mandatory')
bdbufferLgTotal = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 39), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgTotal.setStatus('mandatory')
bdbufferLgFree = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgFree.setStatus('mandatory')
bdbufferLgMax = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgMax.setStatus('mandatory')
bdbufferLgHit = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 42), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgHit.setStatus('mandatory')
bdbufferLgMiss = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgMiss.setStatus('mandatory')
bdbufferLgTrim = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgTrim.setStatus('mandatory')
bdbufferLgCreate = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferLgCreate.setStatus('mandatory')
bdbufferFail = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferFail.setStatus('mandatory')
bdbufferNoMem = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferNoMem.setStatus('mandatory')
bdnetConfigAddr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 48), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdnetConfigAddr.setStatus('mandatory')
bdnetConfigName = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 49), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdnetConfigName.setStatus('mandatory')
bdnetConfigSet = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 50), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bdnetConfigSet.setStatus('mandatory')
bdhostConfigAddr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 51), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdhostConfigAddr.setStatus('obsolete')
bdhostConfigName = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 52), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdhostConfigName.setStatus('obsolete')
bdhostConfigSet = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 53), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bdhostConfigSet.setStatus('obsolete')
bdwriteMem = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 54), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bdwriteMem.setStatus('mandatory')
bdwriteNet = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 55), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bdwriteNet.setStatus('mandatory')
bdbusyPer = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbusyPer.setStatus('mandatory')
bdavgBusy1 = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdavgBusy1.setStatus('mandatory')
bdavgBusy5 = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdavgBusy5.setStatus('mandatory')
bdidleCount = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 59), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdidleCount.setStatus('mandatory')
bdidleWired = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdidleWired.setStatus('mandatory')
bdContactInfo = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 61), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdContactInfo.setStatus('mandatory')
bdbufferHgSize = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 62), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgSize.setStatus('mandatory')
bdbufferHgTotal = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 63), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgTotal.setStatus('mandatory')
bdbufferHgFree = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 64), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgFree.setStatus('mandatory')
bdbufferHgMax = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 65), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgMax.setStatus('mandatory')
bdbufferHgHit = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 66), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgHit.setStatus('mandatory')
bdbufferHgMiss = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 67), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgMiss.setStatus('mandatory')
bdbufferHgTrim = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 68), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgTrim.setStatus('mandatory')
bdbufferHgCreate = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 69), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdbufferHgCreate.setStatus('mandatory')
bdnetConfigProto = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 70), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdnetConfigProto.setStatus('mandatory')
bdhostConfigProto = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 71), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdhostConfigProto.setStatus('mandatory')
bdsysConfigAddr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 72), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdsysConfigAddr.setStatus('mandatory')
bdsysConfigName = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 73), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdsysConfigName.setStatus('mandatory')
bdsysConfigProto = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 74), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdsysConfigProto.setStatus('mandatory')
bdsysClearARP = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 75), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bdsysClearARP.setStatus('mandatory')
bdsysClearInt = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 76), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bdsysClearInt.setStatus('mandatory')
bdenvPresent = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 77), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvPresent.setStatus('mandatory')
bdenvTestPt1Descr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 78), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt1Descr.setStatus('mandatory')
bdenvTestPt1Measure = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 79), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt1Measure.setStatus('mandatory')
bdenvTestPt2Descr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 80), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt2Descr.setStatus('mandatory')
bdenvTestPt2Measure = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 81), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt2Measure.setStatus('mandatory')
bdenvTestPt3Descr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 82), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt3Descr.setStatus('mandatory')
bdenvTestPt3Measure = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 83), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt3Measure.setStatus('mandatory')
bdenvTestPt4Descr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 84), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt4Descr.setStatus('mandatory')
bdenvTestPt4Measure = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 85), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt4Measure.setStatus('mandatory')
bdenvTestPt5Descr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 86), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt5Descr.setStatus('mandatory')
bdenvTestPt5Measure = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 87), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt5Measure.setStatus('mandatory')
bdenvTestPt6Descr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 88), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt6Descr.setStatus('mandatory')
bdenvTestPt6Measure = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 89), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt6Measure.setStatus('mandatory')
bdenvTestPt1MarginVal = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 90), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt1MarginVal.setStatus('mandatory')
bdenvTestPt2MarginVal = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 91), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt2MarginVal.setStatus('mandatory')
bdenvTestPt3MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 92), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt3MarginPercent.setStatus('mandatory')
bdenvTestPt4MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 93), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt4MarginPercent.setStatus('mandatory')
bdenvTestPt5MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 94), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt5MarginPercent.setStatus('mandatory')
bdenvTestPt6MarginPercent = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 95), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt6MarginPercent.setStatus('mandatory')
bdenvTestPt1last = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 96), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt1last.setStatus('mandatory')
bdenvTestPt2last = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 97), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt2last.setStatus('mandatory')
bdenvTestPt3last = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 98), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt3last.setStatus('mandatory')
bdenvTestPt4last = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 99), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt4last.setStatus('mandatory')
bdenvTestPt5last = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt5last.setStatus('mandatory')
bdenvTestPt6last = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 101), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt6last.setStatus('mandatory')
bdenvTestPt1warn = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 102), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt1warn.setStatus('mandatory')
bdenvTestPt2warn = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 103), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt2warn.setStatus('mandatory')
bdenvTestPt3warn = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 104), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt3warn.setStatus('mandatory')
bdenvTestPt4warn = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 105), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt4warn.setStatus('mandatory')
bdenvTestPt5warn = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 106), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt5warn.setStatus('mandatory')
bdenvTestPt6warn = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 107), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warning", 1), ("noWarning", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTestPt6warn.setStatus('mandatory')
bdenvFirmVersion = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 108), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvFirmVersion.setStatus('mandatory')
bdenvTechnicianID = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 109), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvTechnicianID.setStatus('mandatory')
bdenvType = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 110), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvType.setStatus('mandatory')
bdenvBurnDate = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 111), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvBurnDate.setStatus('mandatory')
bdenvSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 3320, 2, 1, 112), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdenvSerialNumber.setStatus('mandatory')
mibBuilder.exportSymbols("BDCOM-SYS", bdbusyPer=bdbusyPer, bdbufferSmSize=bdbufferSmSize, bdbufferSmCreate=bdbufferSmCreate, bdbufferBgMiss=bdbufferBgMiss, bdbufferLgCreate=bdbufferLgCreate, bdsysConfigAddr=bdsysConfigAddr, bdbufferLgHit=bdbufferLgHit, bdidleWired=bdidleWired, bdbufferElHit=bdbufferElHit, bdsysClearInt=bdsysClearInt, bdbufferHgTotal=bdbufferHgTotal, bdbufferHgMax=bdbufferHgMax, bdbufferElMiss=bdbufferElMiss, bdenvFirmVersion=bdenvFirmVersion, bdwriteNet=bdwriteNet, bdnetConfigName=bdnetConfigName, bdbufferElFree=bdbufferElFree, bdbufferLgFree=bdbufferLgFree, bdenvTestPt3MarginPercent=bdenvTestPt3MarginPercent, bdhostConfigName=bdhostConfigName, bdenvType=bdenvType, bdsysConfigName=bdsysConfigName, bdenvTestPt5Descr=bdenvTestPt5Descr, bdenvTestPt6last=bdenvTestPt6last, bdenvSerialNumber=bdenvSerialNumber, bdenvTestPt6Descr=bdenvTestPt6Descr, bdnetConfigProto=bdnetConfigProto, bdbufferBgMax=bdbufferBgMax, bdhostConfigProto=bdhostConfigProto, bdenvTestPt5Measure=bdenvTestPt5Measure, bddomainName=bddomainName, bdbufferLgMiss=bdbufferLgMiss, bdsysConfigProto=bdsysConfigProto, bdbufferSmFree=bdbufferSmFree, bdbufferMdMax=bdbufferMdMax, bdbootHost=bdbootHost, bdenvTestPt2Descr=bdenvTestPt2Descr, bdenvTestPt5warn=bdenvTestPt5warn, bdenvTechnicianID=bdenvTechnicianID, bdbufferNoMem=bdbufferNoMem, bdbufferMdHit=bdbufferMdHit, bdenvTestPt1warn=bdenvTestPt1warn, bdenvTestPt2Measure=bdenvTestPt2Measure, bdbufferMdSize=bdbufferMdSize, bdenvTestPt2MarginVal=bdenvTestPt2MarginVal, bdenvTestPt4MarginPercent=bdenvTestPt4MarginPercent, bdbufferMdFree=bdbufferMdFree, bdbufferLgTotal=bdbufferLgTotal, bdenvTestPt6warn=bdenvTestPt6warn, bdContactInfo=bdContactInfo, bdhostConfigSet=bdhostConfigSet, bdbufferSmTrim=bdbufferSmTrim, bdbufferElMax=bdbufferElMax, bdenvTestPt5MarginPercent=bdenvTestPt5MarginPercent, bdbufferMdMiss=bdbufferMdMiss, bdbufferHgTrim=bdbufferHgTrim, bdavgBusy1=bdavgBusy1, bdbufferMdTrim=bdbufferMdTrim, bdbufferLgTrim=bdbufferLgTrim, bdenvTestPt2warn=bdenvTestPt2warn, bdbufferBgTrim=bdbufferBgTrim, bdenvTestPt6Measure=bdenvTestPt6Measure, bdping=bdping, bdsysClearARP=bdsysClearARP, bdbufferLgSize=bdbufferLgSize, bdenvTestPt4Measure=bdenvTestPt4Measure, bdbufferHgHit=bdbufferHgHit, bdbufferBgCreate=bdbufferBgCreate, bdbufferSmTotal=bdbufferSmTotal, bdhostConfigAddr=bdhostConfigAddr, bdbufferElCreate=bdbufferElCreate, bdbufferSmHit=bdbufferSmHit, bdbufferHgCreate=bdbufferHgCreate, bdenvTestPt4Descr=bdenvTestPt4Descr, bdenvTestPt1Measure=bdenvTestPt1Measure, bdavgBusy5=bdavgBusy5, bdenvTestPt3last=bdenvTestPt3last, bdbufferBgHit=bdbufferBgHit, bdwriteMem=bdwriteMem, bdenvTestPt4last=bdenvTestPt4last, bdenvTestPt1last=bdenvTestPt1last, bdbufferFail=bdbufferFail, bdbufferLgMax=bdbufferLgMax, bdenvPresent=bdenvPresent, bdidleCount=bdidleCount, bdbufferSmMiss=bdbufferSmMiss, bdenvTestPt3warn=bdenvTestPt3warn, bdenvTestPt6MarginPercent=bdenvTestPt6MarginPercent, bdenvTestPt4warn=bdenvTestPt4warn, bdenvTestPt1MarginVal=bdenvTestPt1MarginVal, bdwhyReload=bdwhyReload, bdbufferMdTotal=bdbufferMdTotal, bdbufferSmMax=bdbufferSmMax, bdenvTestPt3Descr=bdenvTestPt3Descr, bdlsystem=bdlsystem, bdenvBurnDate=bdenvBurnDate, bdhostName=bdhostName, bdbufferBgTotal=bdbufferBgTotal, bdromId=bdromId, bdenvTestPt5last=bdenvTestPt5last, bdauthAddr=bdauthAddr, bdfreeMem=bdfreeMem, bdbufferHgMiss=bdbufferHgMiss, bdbufferBgSize=bdbufferBgSize, bdbufferHgFree=bdbufferHgFree, bdbufferBgFree=bdbufferBgFree, bdnetConfigAddr=bdnetConfigAddr, bdenvTestPt1Descr=bdenvTestPt1Descr, bdenvTestPt2last=bdenvTestPt2last, bdnetConfigSet=bdnetConfigSet, bdbufferMdCreate=bdbufferMdCreate, bdbufferHgSize=bdbufferHgSize, bdenvTestPt3Measure=bdenvTestPt3Measure)