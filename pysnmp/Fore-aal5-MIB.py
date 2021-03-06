#
# PySNMP MIB module Fore-aal5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-aal5-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
frameInternetworking, = mibBuilder.importSymbols("Fore-Common-MIB", "frameInternetworking")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Bits, IpAddress, Unsigned32, NotificationType, Counter64, iso, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Bits", "IpAddress", "Unsigned32", "NotificationType", "Counter64", "iso", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aal5 = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 16, 5))
if mibBuilder.loadTexts: aal5.setLastUpdated('9706100906Z')
if mibBuilder.loadTexts: aal5.setOrganization('FORE')
aal5VccTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1), )
if mibBuilder.loadTexts: aal5VccTable.setStatus('current')
aal5VccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5VccAtmFabServiceIfIndex"), (0, "Fore-aal5-MIB", "aal5VccFabVpi"), (0, "Fore-aal5-MIB", "aal5VccFabVci"))
if mibBuilder.loadTexts: aal5VccEntry.setStatus('current')
aal5VccAtmFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccAtmFabServiceIfIndex.setStatus('current')
aal5VccFabVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccFabVpi.setStatus('current')
aal5VccFabVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccFabVci.setStatus('current')
aal5VccCrcErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccCrcErrs.setStatus('current')
aal5VccSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccSarTimeOuts.setStatus('current')
aal5VccOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccOverSizedPDUs.setStatus('current')
aal5VccLengthErrPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccLengthErrPDUs.setStatus('current')
aal5VccCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccCPIErrs.setStatus('current')
aal5VccInPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccInPDUs.setStatus('current')
aal5VccOutPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccOutPDUs.setStatus('current')
aal5VccInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccInOctets.setStatus('current')
aal5VccOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5VccOutOctets.setStatus('current')
aal5CpcsCurrTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2), )
if mibBuilder.loadTexts: aal5CpcsCurrTable.setStatus('current')
aal5CpcsCurrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5CpcsFabServiceIfIndex"))
if mibBuilder.loadTexts: aal5CpcsCurrEntry.setStatus('current')
aal5CpcsFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsFabServiceIfIndex.setStatus('current')
aal5CpcsCurrCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrCRCErrs.setStatus('current')
aal5CpcsCurrSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrSarTimeOuts.setStatus('current')
aal5CpcsCurrOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrOverSizedPDUs.setStatus('current')
aal5CpcsCurrLengthErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrLengthErrs.setStatus('current')
aal5CpcsCurrCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsCurrCPIErrs.setStatus('current')
aal5CpcsIntvlTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3), )
if mibBuilder.loadTexts: aal5CpcsIntvlTable.setStatus('current')
aal5CpcsIntvlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5CpcsIntvlFabServiceIfIndex"), (0, "Fore-aal5-MIB", "aal5CpcsIntvlNumber"))
if mibBuilder.loadTexts: aal5CpcsIntvlEntry.setStatus('current')
aal5CpcsIntvlFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlFabServiceIfIndex.setStatus('current')
aal5CpcsIntvlNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlNumber.setStatus('current')
aal5CpcsIntvlCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlCRCErrs.setStatus('current')
aal5CpcsIntvlSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlSarTimeOuts.setStatus('current')
aal5CpcsIntvlOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlOverSizedPDUs.setStatus('current')
aal5CpcsIntvlLengthErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlLengthErrs.setStatus('current')
aal5CpcsIntvlCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsIntvlCPIErrs.setStatus('current')
aal5CpcsTotalTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4), )
if mibBuilder.loadTexts: aal5CpcsTotalTable.setStatus('current')
aal5CpcsTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5CpcsTotalFabServiceIfIndex"))
if mibBuilder.loadTexts: aal5CpcsTotalEntry.setStatus('current')
aal5CpcsTotalFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalFabServiceIfIndex.setStatus('current')
aal5CpcsTotalValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalValidIntervals.setStatus('current')
aal5CpcsTotalCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalCRCErrs.setStatus('current')
aal5CpcsTotalSarTimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalSarTimeOuts.setStatus('current')
aal5CpcsTotalOverSizedPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalOverSizedPDUs.setStatus('current')
aal5CpcsTotalLengthErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalLengthErrs.setStatus('current')
aal5CpcsTotalCPIErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5CpcsTotalCPIErrs.setStatus('current')
aal5EpdPpdVccTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5), )
if mibBuilder.loadTexts: aal5EpdPpdVccTable.setStatus('current')
aal5EpdPpdVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1), ).setIndexNames((0, "Fore-aal5-MIB", "aal5EpdPpdAtmFabServiceIfIndex"), (0, "Fore-aal5-MIB", "aal5EpdPpdVccFabVpi"), (0, "Fore-aal5-MIB", "aal5EpdPpdVccFabVci"))
if mibBuilder.loadTexts: aal5EpdPpdVccEntry.setStatus('current')
aal5EpdPpdAtmFabServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdAtmFabServiceIfIndex.setStatus('current')
aal5EpdPpdVccFabVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccFabVpi.setStatus('current')
aal5EpdPpdVccFabVci = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccFabVci.setStatus('current')
aal5EpdPpdVccDroppedCellsClp1 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccDroppedCellsClp1.setStatus('current')
aal5EpdPpdVccForwardedCellsClp1 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccForwardedCellsClp1.setStatus('current')
aal5EpdPpdVccDroppedCellsClp0 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccDroppedCellsClp0.setStatus('current')
aal5EpdPpdVccForwardedCellsClp0 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal5EpdPpdVccForwardedCellsClp0.setStatus('current')
mibBuilder.exportSymbols("Fore-aal5-MIB", aal5VccTable=aal5VccTable, aal5VccFabVpi=aal5VccFabVpi, aal5CpcsIntvlLengthErrs=aal5CpcsIntvlLengthErrs, aal5EpdPpdAtmFabServiceIfIndex=aal5EpdPpdAtmFabServiceIfIndex, aal5CpcsIntvlCRCErrs=aal5CpcsIntvlCRCErrs, aal5=aal5, aal5CpcsTotalEntry=aal5CpcsTotalEntry, aal5VccCPIErrs=aal5VccCPIErrs, aal5VccOutOctets=aal5VccOutOctets, aal5CpcsIntvlCPIErrs=aal5CpcsIntvlCPIErrs, aal5EpdPpdVccTable=aal5EpdPpdVccTable, aal5VccAtmFabServiceIfIndex=aal5VccAtmFabServiceIfIndex, aal5EpdPpdVccFabVci=aal5EpdPpdVccFabVci, aal5CpcsIntvlNumber=aal5CpcsIntvlNumber, aal5EpdPpdVccEntry=aal5EpdPpdVccEntry, aal5CpcsIntvlEntry=aal5CpcsIntvlEntry, aal5CpcsTotalSarTimeOuts=aal5CpcsTotalSarTimeOuts, aal5CpcsCurrCRCErrs=aal5CpcsCurrCRCErrs, aal5CpcsIntvlOverSizedPDUs=aal5CpcsIntvlOverSizedPDUs, aal5CpcsIntvlFabServiceIfIndex=aal5CpcsIntvlFabServiceIfIndex, aal5CpcsTotalTable=aal5CpcsTotalTable, aal5VccSarTimeOuts=aal5VccSarTimeOuts, aal5VccOverSizedPDUs=aal5VccOverSizedPDUs, aal5EpdPpdVccDroppedCellsClp1=aal5EpdPpdVccDroppedCellsClp1, aal5CpcsCurrTable=aal5CpcsCurrTable, aal5CpcsCurrOverSizedPDUs=aal5CpcsCurrOverSizedPDUs, aal5CpcsTotalValidIntervals=aal5CpcsTotalValidIntervals, aal5VccCrcErrs=aal5VccCrcErrs, aal5CpcsTotalCRCErrs=aal5CpcsTotalCRCErrs, PYSNMP_MODULE_ID=aal5, aal5CpcsCurrLengthErrs=aal5CpcsCurrLengthErrs, aal5EpdPpdVccDroppedCellsClp0=aal5EpdPpdVccDroppedCellsClp0, aal5VccFabVci=aal5VccFabVci, aal5EpdPpdVccFabVpi=aal5EpdPpdVccFabVpi, aal5CpcsCurrEntry=aal5CpcsCurrEntry, aal5VccInPDUs=aal5VccInPDUs, aal5VccOutPDUs=aal5VccOutPDUs, aal5CpcsIntvlTable=aal5CpcsIntvlTable, aal5EpdPpdVccForwardedCellsClp1=aal5EpdPpdVccForwardedCellsClp1, aal5EpdPpdVccForwardedCellsClp0=aal5EpdPpdVccForwardedCellsClp0, aal5VccLengthErrPDUs=aal5VccLengthErrPDUs, aal5CpcsIntvlSarTimeOuts=aal5CpcsIntvlSarTimeOuts, aal5CpcsCurrSarTimeOuts=aal5CpcsCurrSarTimeOuts, aal5CpcsCurrCPIErrs=aal5CpcsCurrCPIErrs, aal5CpcsTotalFabServiceIfIndex=aal5CpcsTotalFabServiceIfIndex, aal5CpcsTotalLengthErrs=aal5CpcsTotalLengthErrs, aal5VccEntry=aal5VccEntry, aal5VccInOctets=aal5VccInOctets, aal5CpcsTotalCPIErrs=aal5CpcsTotalCPIErrs, aal5CpcsFabServiceIfIndex=aal5CpcsFabServiceIfIndex, aal5CpcsTotalOverSizedPDUs=aal5CpcsTotalOverSizedPDUs)
