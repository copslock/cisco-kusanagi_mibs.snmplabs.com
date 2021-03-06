#
# PySNMP MIB module CTRON-SFPS-SIZE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SFPS-SIZE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:15:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
sfpsSizeService, sfpsSizeServiceAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsSizeService", "sfpsSizeServiceAPI")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, NotificationType, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter64, Counter32, Integer32, ObjectIdentity, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter64", "Counter32", "Integer32", "ObjectIdentity", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sfpsSizeServiceTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1), )
if mibBuilder.loadTexts: sfpsSizeServiceTable.setStatus('mandatory')
sfpsSizeServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-SIZE-MIB", "sfpsSizeServiceName"))
if mibBuilder.loadTexts: sfpsSizeServiceEntry.setStatus('mandatory')
sfpsSizeServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceName.setStatus('mandatory')
sfpsSizeServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceId.setStatus('mandatory')
sfpsSizeServiceElemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceElemSize.setStatus('mandatory')
sfpsSizeServiceDesired = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceDesired.setStatus('mandatory')
sfpsSizeServiceGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceGranted.setStatus('mandatory')
sfpsSizeServiceIncrement = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceIncrement.setStatus('mandatory')
sfpsSizeServiceTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceTotalBytes.setStatus('mandatory')
sfpsSizeServiceNbrCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceNbrCalls.setStatus('mandatory')
sfpsSizeServiceRtnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ok", 1), ("nvramOk", 2), ("unknown", 3), ("notAllowed", 4), ("nonApiOk", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceRtnStatus.setStatus('mandatory')
sfpsSizeServiceHowGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("elements", 1), ("memory", 2), ("other", 3), ("notAllowed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceHowGranted.setStatus('mandatory')
sfpsSizeServiceAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("next", 2), ("prev", 3), ("set", 4), ("clear", 5), ("clearAll", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIVerb.setStatus('mandatory')
sfpsSizeServiceAPIName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIName.setStatus('mandatory')
sfpsSizeServiceAPIId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIId.setStatus('mandatory')
sfpsSizeServiceAPIGrant = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIGrant.setStatus('mandatory')
sfpsSizeServiceAPIIncrement = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSizeServiceAPIIncrement.setStatus('mandatory')
sfpsSizeServiceAPINumberSet = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceAPINumberSet.setStatus('mandatory')
sfpsSizeServiceAPIVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 14, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSizeServiceAPIVersion.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-SIZE-MIB", sfpsSizeServiceAPIIncrement=sfpsSizeServiceAPIIncrement, sfpsSizeServiceTable=sfpsSizeServiceTable, sfpsSizeServiceDesired=sfpsSizeServiceDesired, sfpsSizeServiceElemSize=sfpsSizeServiceElemSize, sfpsSizeServiceEntry=sfpsSizeServiceEntry, sfpsSizeServiceAPIId=sfpsSizeServiceAPIId, sfpsSizeServiceRtnStatus=sfpsSizeServiceRtnStatus, sfpsSizeServiceAPIVerb=sfpsSizeServiceAPIVerb, sfpsSizeServiceId=sfpsSizeServiceId, sfpsSizeServiceAPIGrant=sfpsSizeServiceAPIGrant, sfpsSizeServiceAPINumberSet=sfpsSizeServiceAPINumberSet, sfpsSizeServiceNbrCalls=sfpsSizeServiceNbrCalls, sfpsSizeServiceHowGranted=sfpsSizeServiceHowGranted, sfpsSizeServiceAPIName=sfpsSizeServiceAPIName, sfpsSizeServiceTotalBytes=sfpsSizeServiceTotalBytes, sfpsSizeServiceAPIVersion=sfpsSizeServiceAPIVersion, sfpsSizeServiceName=sfpsSizeServiceName, sfpsSizeServiceGranted=sfpsSizeServiceGranted, sfpsSizeServiceIncrement=sfpsSizeServiceIncrement)
