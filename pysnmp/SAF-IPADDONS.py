#
# PySNMP MIB module SAF-IPADDONS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAF-IPADDONS
# Produced by pysmi-0.3.4 at Mon Apr 29 20:51:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, ModuleIdentity, Counter64, enterprises, TimeTicks, Unsigned32, Gauge32, ObjectIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "ModuleIdentity", "Counter64", "enterprises", "TimeTicks", "Unsigned32", "Gauge32", "ObjectIdentity", "Counter32", "NotificationType")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
saf = MibIdentifier((1, 3, 6, 1, 4, 1, 7571))
tehnika = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100))
microwaveRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1))
pointToPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1))
safip = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5))
safipaddons = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15))
ipaddSys = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1))
ipaddIfB = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2))
ipaddIfM = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3))
modemTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemTemperature.setStatus('mandatory')
iduInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iduInputVoltage.setStatus('mandatory')
iduInputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iduInputCurrent.setStatus('mandatory')
iduPowerConsumption = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iduPowerConsumption.setStatus('mandatory')
oduTemperature = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTemperature.setStatus('mandatory')
oduPsuState = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("init", 1), ("off", 2), ("idle", 3), ("ok", 4), ("overload", 5), ("short", 6), ("fault", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduPsuState.setStatus('mandatory')
iduOutputVoltageToOdu = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iduOutputVoltageToOdu.setStatus('mandatory')
iduOutputCurrentToOdu = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iduOutputCurrentToOdu.setStatus('mandatory')
oduPowerConsumption = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduPowerConsumption.setStatus('mandatory')
oduCableAttenuation = MibScalar((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduCableAttenuation.setStatus('mandatory')
ipaddIfBTable = MibTable((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2), )
if mibBuilder.loadTexts: ipaddIfBTable.setStatus('current')
ipaddIfBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1), ).setIndexNames((0, "SAF-IPADDONS", "ipaddIfBIndex"))
if mibBuilder.loadTexts: ipaddIfBEntry.setStatus('current')
ipaddIfBIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBIndex.setStatus('mandatory')
ipaddIfBduplex = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("full", 1), ("half", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBduplex.setStatus('mandatory')
ipaddIfBRxFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxFlow.setStatus('mandatory')
ipaddIfBTxFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBTxFlow.setStatus('mandatory')
ipaddIfBRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxState.setStatus('mandatory')
ipaddIfBTxTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBTxTxState.setStatus('mandatory')
ipaddIfBTxQ0PKT = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBTxQ0PKT.setStatus('mandatory')
ipaddIfBTxCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBTxCollisions.setStatus('mandatory')
ipaddIfBTxSingleCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBTxSingleCollision.setStatus('mandatory')
ipaddIfBTxMultiCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBTxMultiCollision.setStatus('mandatory')
ipaddIfBRxPausePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxPausePkts.setStatus('mandatory')
ipaddIfBRxFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxFCSErrors.setStatus('mandatory')
ipaddIfBRxGoodOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxGoodOctets.setStatus('mandatory')
ipaddIfBRxSAChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxSAChanges.setStatus('mandatory')
ipaddIfBRxExcessSizeDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxExcessSizeDisc.setStatus('mandatory')
ipaddIfBRxSymbolError = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxSymbolError.setStatus('mandatory')
ipaddIfBRxPkts1523to2047Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxPkts1523to2047Octets.setStatus('mandatory')
ipaddIfBRxPkts2048to4095Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxPkts2048to4095Octets.setStatus('mandatory')
ipaddIfBRxPkts4096to8191Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxPkts4096to8191Octets.setStatus('mandatory')
ipaddIfBRxPkts8192to9728Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfBRxPkts8192to9728Octets.setStatus('mandatory')
ipaddIfMTable = MibTable((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2), )
if mibBuilder.loadTexts: ipaddIfMTable.setStatus('current')
ipaddIfMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1), ).setIndexNames((0, "SAF-IPADDONS", "ipaddIfMIndex"))
if mibBuilder.loadTexts: ipaddIfMEntry.setStatus('current')
ipaddIfMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMIndex.setStatus('mandatory')
ipaddIfMduplex = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("full", 1), ("half", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMduplex.setStatus('mandatory')
ipaddIfMFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMFlowControl.setStatus('mandatory')
ipaddIfMRxLoPriorityByte = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMRxLoPriorityByte.setStatus('mandatory')
ipaddIfMRxHiPriorityByte = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMRxHiPriorityByte.setStatus('mandatory')
ipaddIfMRxSymbolError = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMRxSymbolError.setStatus('mandatory')
ipaddIfMRxCRCerror = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMRxCRCerror.setStatus('mandatory')
ipaddIfMRxControl8808Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMRxControl8808Pkts.setStatus('mandatory')
ipaddIfMRxPausePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMRxPausePkts.setStatus('mandatory')
ipaddIfMTxLoPriorityByte = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxLoPriorityByte.setStatus('mandatory')
ipaddIfMTxHiPriorityByte = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxHiPriorityByte.setStatus('mandatory')
ipaddIfMTxLateCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxLateCollision.setStatus('mandatory')
ipaddIfMTxPausePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxPausePkts.setStatus('mandatory')
ipaddIfMTxDeferred = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxDeferred.setStatus('mandatory')
ipaddIfMTxTotalCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxTotalCollision.setStatus('mandatory')
ipaddIfMTxExcessiveCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxExcessiveCollision.setStatus('mandatory')
ipaddIfMTxSingleCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxSingleCollision.setStatus('mandatory')
ipaddIfMTxMultipleCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipaddIfMTxMultipleCollision.setStatus('mandatory')
mibBuilder.exportSymbols("SAF-IPADDONS", microwaveRadio=microwaveRadio, ipaddIfMFlowControl=ipaddIfMFlowControl, ipaddIfBRxPkts4096to8191Octets=ipaddIfBRxPkts4096to8191Octets, ipaddIfMRxControl8808Pkts=ipaddIfMRxControl8808Pkts, ipaddIfBTxFlow=ipaddIfBTxFlow, ipaddIfMTxLoPriorityByte=ipaddIfMTxLoPriorityByte, saf=saf, ipaddIfMTxSingleCollision=ipaddIfMTxSingleCollision, ipaddIfBTxCollisions=ipaddIfBTxCollisions, oduPsuState=oduPsuState, ipaddIfMTxMultipleCollision=ipaddIfMTxMultipleCollision, tehnika=tehnika, oduTemperature=oduTemperature, iduInputCurrent=iduInputCurrent, ipaddIfBRxFlow=ipaddIfBRxFlow, ipaddIfBRxSAChanges=ipaddIfBRxSAChanges, ipaddIfMEntry=ipaddIfMEntry, ipaddIfMTxPausePkts=ipaddIfMTxPausePkts, ipaddIfMTxTotalCollision=ipaddIfMTxTotalCollision, iduOutputVoltageToOdu=iduOutputVoltageToOdu, ipaddIfBIndex=ipaddIfBIndex, oduPowerConsumption=oduPowerConsumption, oduCableAttenuation=oduCableAttenuation, ipaddIfMduplex=ipaddIfMduplex, ipaddIfMRxCRCerror=ipaddIfMRxCRCerror, ipaddSys=ipaddSys, safipaddons=safipaddons, ipaddIfBRxState=ipaddIfBRxState, ipaddIfBEntry=ipaddIfBEntry, ipaddIfBTable=ipaddIfBTable, ipaddIfMTable=ipaddIfMTable, ipaddIfMRxLoPriorityByte=ipaddIfMRxLoPriorityByte, ipaddIfMTxDeferred=ipaddIfMTxDeferred, ipaddIfMTxHiPriorityByte=ipaddIfMTxHiPriorityByte, ipaddIfBRxPausePkts=ipaddIfBRxPausePkts, pointToPoint=pointToPoint, ipaddIfBRxExcessSizeDisc=ipaddIfBRxExcessSizeDisc, ipaddIfBTxSingleCollision=ipaddIfBTxSingleCollision, ipaddIfBRxSymbolError=ipaddIfBRxSymbolError, ipaddIfBTxMultiCollision=ipaddIfBTxMultiCollision, ipaddIfMTxExcessiveCollision=ipaddIfMTxExcessiveCollision, iduOutputCurrentToOdu=iduOutputCurrentToOdu, ipaddIfBduplex=ipaddIfBduplex, ipaddIfBRxGoodOctets=ipaddIfBRxGoodOctets, ipaddIfBRxPkts8192to9728Octets=ipaddIfBRxPkts8192to9728Octets, modemTemperature=modemTemperature, ipaddIfBRxPkts2048to4095Octets=ipaddIfBRxPkts2048to4095Octets, ipaddIfB=ipaddIfB, safip=safip, iduInputVoltage=iduInputVoltage, ipaddIfBRxFCSErrors=ipaddIfBRxFCSErrors, ipaddIfBRxPkts1523to2047Octets=ipaddIfBRxPkts1523to2047Octets, ipaddIfMRxSymbolError=ipaddIfMRxSymbolError, ipaddIfMRxHiPriorityByte=ipaddIfMRxHiPriorityByte, ipaddIfBTxTxState=ipaddIfBTxTxState, ipaddIfMIndex=ipaddIfMIndex, ipaddIfMTxLateCollision=ipaddIfMTxLateCollision, ipaddIfBTxQ0PKT=ipaddIfBTxQ0PKT, iduPowerConsumption=iduPowerConsumption, ipaddIfMRxPausePkts=ipaddIfMRxPausePkts, ipaddIfM=ipaddIfM)
