#
# PySNMP MIB module CXOperatingSystem-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXOperatingSystem-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
cxOperatingSystem, = mibBuilder.importSymbols("CXProduct-SMI", "cxOperatingSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, NotificationType, Integer32, MibIdentifier, Counter32, Bits, ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "Bits", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxOsParameter = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1))
cxOsNbBufs = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 1), Integer32().clone(1200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsNbBufs.setStatus('mandatory')
cxOsBufSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 2), Integer32().clone(292)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsBufSize.setStatus('mandatory')
cxOsNbBufsAvail = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxOsNbBufsAvail.setStatus('mandatory')
cxOsNbBufsFree = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxOsNbBufsFree.setStatus('mandatory')
cxOsNbSystemMsg = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 16), Integer32().clone(1320)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsNbSystemMsg.setStatus('mandatory')
cxOsNbSystemMsgFree = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxOsNbSystemMsgFree.setStatus('mandatory')
cxOsOptions = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("data", 1), ("inst", 2), ("data-inst", 3), ("pipeline", 4), ("p-data", 5), ("p-inst", 6), ("p-data-inst", 7), ("none", 8))).clone('p-data-inst')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxOsOptions.setStatus('mandatory')
mibBuilder.exportSymbols("CXOperatingSystem-MIB", cxOsNbBufsFree=cxOsNbBufsFree, cxOsParameter=cxOsParameter, cxOsOptions=cxOsOptions, cxOsNbBufsAvail=cxOsNbBufsAvail, cxOsNbSystemMsgFree=cxOsNbSystemMsgFree, cxOsNbBufs=cxOsNbBufs, cxOsNbSystemMsg=cxOsNbSystemMsg, cxOsBufSize=cxOsBufSize)
