#
# PySNMP MIB module AI193TX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AI193TX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Counter32, enterprises, ObjectIdentity, TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Counter32", "enterprises", "ObjectIdentity", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSystemOID = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2))
aiTX1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 14))
if mibBuilder.loadTexts: aiTX1.setLastUpdated('9505081700Z')
if mibBuilder.loadTexts: aiTX1.setOrganization('Applied Innovation Incorporated')
aiTX1System = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 14, 1))
aiTX1Calls = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 14, 2))
ai193 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193))
ai193Ver7 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7))
ai193Ver71 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 1))
ai193Ver72 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 2))
ai193Ver73 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 3))
ai193Ver74 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 4))
ai193Ver75 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 5))
ai193Ver76 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 6))
ai193Ver77 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 7))
ai193Ver78 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 8))
ai193Ver79 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 9))
ai193Ver710 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 10))
aiTX1Interface = MibScalar((1, 3, 6, 1, 4, 1, 539, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("irb", 1), ("frontpanel", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1Interface.setStatus('mandatory')
aiTX1NumCalls = MibScalar((1, 3, 6, 1, 4, 1, 539, 14, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1NumCalls.setStatus('mandatory')
aiTX1CallTable = MibTable((1, 3, 6, 1, 4, 1, 539, 14, 2, 2), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallTable.setStatus('mandatory')
aiTX1CallTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1), ).setMaxAccess("readonly").setIndexNames((0, "AI193TX-MIB", "aiTX1CallIndex"))
if mibBuilder.loadTexts: aiTX1CallTableEntry.setStatus('mandatory')
aiTX1CallIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallIndex.setStatus('mandatory')
aiTX1CallStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 9))).clone(namedValues=NamedValues(("active", 1), ("inactive", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallStatus.setStatus('mandatory')
aiTX1CallSource = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("incoming", 1), ("outgoing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallSource.setStatus('mandatory')
aiTX1CallSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallSrcAddress.setStatus('mandatory')
aiTX1CallDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallDestAddress.setStatus('mandatory')
aiTX1CallPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallPacketsSent.setStatus('mandatory')
aiTX1CallPktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallPktsRcvd.setStatus('mandatory')
aiTX1CalledPort = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CalledPort.setStatus('mandatory')
aiTX1CallingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallingPort.setStatus('mandatory')
aiTX1CallUserData = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiTX1CallUserData.setStatus('mandatory')
mibBuilder.exportSymbols("AI193TX-MIB", ai193Ver7=ai193Ver7, ai193Ver74=ai193Ver74, ai193Ver73=ai193Ver73, ai193Ver72=ai193Ver72, PYSNMP_MODULE_ID=aiTX1, aiTX1CallUserData=aiTX1CallUserData, ai193Ver77=ai193Ver77, aiTX1CallPktsRcvd=aiTX1CallPktsRcvd, aii=aii, aiTX1CallSrcAddress=aiTX1CallSrcAddress, aiTX1CallTableEntry=aiTX1CallTableEntry, aiTX1Calls=aiTX1Calls, aiTX1CallIndex=aiTX1CallIndex, aiTX1CallTable=aiTX1CallTable, ai193Ver71=ai193Ver71, aiTX1CallSource=aiTX1CallSource, ai193Ver75=ai193Ver75, aiTX1CallingPort=aiTX1CallingPort, ai193Ver79=ai193Ver79, aiTX1CallDestAddress=aiTX1CallDestAddress, aiTX1CalledPort=aiTX1CalledPort, aiTX1NumCalls=aiTX1NumCalls, aiTX1CallStatus=aiTX1CallStatus, ai193Ver76=ai193Ver76, aiSystemOID=aiSystemOID, aiTX1CallPacketsSent=aiTX1CallPacketsSent, aiTX1Interface=aiTX1Interface, ai193Ver78=ai193Ver78, ai193Ver710=ai193Ver710, aiTX1System=aiTX1System, aiTX1=aiTX1, ai193=ai193)