#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-PorsTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-PorsTrunksMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:21:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
RowPointer, Unsigned32, RowStatus, StorageType, Integer32, DisplayString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "RowPointer", "Unsigned32", "RowStatus", "StorageType", "Integer32", "DisplayString")
AsciiString, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "AsciiString", "NonReplicated")
mscTrkIndex, mscTrk = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex", "mscTrk")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Gauge32, IpAddress, Counter64, ModuleIdentity, iso, NotificationType, Integer32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Gauge32", "IpAddress", "Counter64", "ModuleIdentity", "iso", "NotificationType", "Integer32", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
porsTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39))
mscTrkPa = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4))
mscTrkPaRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1), )
if mibBuilder.loadTexts: mscTrkPaRowStatusTable.setStatus('mandatory')
mscTrkPaRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"))
if mibBuilder.loadTexts: mscTrkPaRowStatusEntry.setStatus('mandatory')
mscTrkPaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaRowStatus.setStatus('mandatory')
mscTrkPaComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaComponentName.setStatus('mandatory')
mscTrkPaStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaStorageType.setStatus('mandatory')
mscTrkPaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscTrkPaIndex.setStatus('mandatory')
mscTrkPaProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10), )
if mibBuilder.loadTexts: mscTrkPaProvTable.setStatus('mandatory')
mscTrkPaProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"))
if mibBuilder.loadTexts: mscTrkPaProvEntry.setStatus('mandatory')
mscTrkPaMaxLc = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65435)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaMaxLc.setStatus('mandatory')
mscTrkPaMaxReservedBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaMaxReservedBwOut.setStatus('mandatory')
mscTrkPaTrunkSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaTrunkSecurity.setStatus('mandatory')
mscTrkPaSupportedTrafficTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="f8")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaSupportedTrafficTypes.setStatus('mandatory')
mscTrkPaTrunkType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("terrestrial", 0), ("satellite", 1), ("trunkType1", 2), ("trunkType2", 3), ("trunkType3", 4), ("trunkType4", 5), ("trunkType5", 6), ("trunkType6", 7))).clone('terrestrial')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaTrunkType.setStatus('mandatory')
mscTrkPaCustomerParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaCustomerParameter.setStatus('mandatory')
mscTrkPaTrunkCost = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 10, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscTrkPaTrunkCost.setStatus('mandatory')
mscTrkPaOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11), )
if mibBuilder.loadTexts: mscTrkPaOperTable.setStatus('mandatory')
mscTrkPaOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"))
if mibBuilder.loadTexts: mscTrkPaOperEntry.setStatus('mandatory')
mscTrkPaState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaState.setStatus('mandatory')
mscTrkPaUsedLc = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaUsedLc.setStatus('mandatory')
mscTrkPaNegotiatedMaxLc = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedMaxLc.setStatus('mandatory')
mscTrkPaMaxReservableBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaMaxReservableBwOut.setStatus('mandatory')
mscTrkPaOverReservedBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaOverReservedBwOut.setStatus('mandatory')
mscTrkPaUnreservedBwOut = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaUnreservedBwOut.setStatus('mandatory')
mscTrkPaClashCount = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaClashCount.setStatus('mandatory')
mscTrkPaNegotiatedSupportedTrafficTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedSupportedTrafficTypes.setStatus('mandatory')
mscTrkPaNegotiatedTrunkSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedTrunkSecurity.setStatus('mandatory')
mscTrkPaNegotiatedCustomerParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedCustomerParameter.setStatus('mandatory')
mscTrkPaNegotiatedTrunkCost = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedTrunkCost.setStatus('mandatory')
mscTrkPaNegotiatedAtmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("multiplexing", 0), ("mapping", 1), ("notApplicable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedAtmMode.setStatus('mandatory')
mscTrkPaNegotiatedTrunkDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedTrunkDelay.setStatus('mandatory')
mscTrkPaNegotiatedTrunkType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 11, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("terrestrial", 0), ("satellite", 1), ("trunkType1", 2), ("trunkType2", 3), ("trunkType3", 4), ("trunkType4", 5), ("trunkType5", 6), ("trunkType6", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaNegotiatedTrunkType.setStatus('mandatory')
mscTrkPaRbwTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214), )
if mibBuilder.loadTexts: mscTrkPaRbwTable.setStatus('mandatory')
mscTrkPaRbwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaRbwIndex"))
if mibBuilder.loadTexts: mscTrkPaRbwEntry.setStatus('mandatory')
mscTrkPaRbwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: mscTrkPaRbwIndex.setStatus('mandatory')
mscTrkPaRbwValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 214, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaRbwValue.setStatus('mandatory')
mscTrkPaPacntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215), )
if mibBuilder.loadTexts: mscTrkPaPacntTable.setStatus('mandatory')
mscTrkPaPacntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPacntIndex"))
if mibBuilder.loadTexts: mscTrkPaPacntEntry.setStatus('mandatory')
mscTrkPaPacntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: mscTrkPaPacntIndex.setStatus('mandatory')
mscTrkPaPacntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 215, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaPacntValue.setStatus('mandatory')
mscTrkPaPfcntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216), )
if mibBuilder.loadTexts: mscTrkPaPfcntTable.setStatus('mandatory')
mscTrkPaPfcntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPfcntIndex"))
if mibBuilder.loadTexts: mscTrkPaPfcntEntry.setStatus('mandatory')
mscTrkPaPfcntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: mscTrkPaPfcntIndex.setStatus('mandatory')
mscTrkPaPfcntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 216, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaPfcntValue.setStatus('mandatory')
mscTrkPaPccntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217), )
if mibBuilder.loadTexts: mscTrkPaPccntTable.setStatus('mandatory')
mscTrkPaPccntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPccntIndex"))
if mibBuilder.loadTexts: mscTrkPaPccntEntry.setStatus('mandatory')
mscTrkPaPccntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: mscTrkPaPccntIndex.setStatus('mandatory')
mscTrkPaPccntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 217, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaPccntValue.setStatus('mandatory')
mscTrkPaPbcntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218), )
if mibBuilder.loadTexts: mscTrkPaPbcntTable.setStatus('mandatory')
mscTrkPaPbcntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkPaPbcntIndex"))
if mibBuilder.loadTexts: mscTrkPaPbcntEntry.setStatus('mandatory')
mscTrkPaPbcntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: mscTrkPaPbcntIndex.setStatus('mandatory')
mscTrkPaPbcntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 4, 218, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkPaPbcntValue.setStatus('mandatory')
mscTrkLCh = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5))
mscTrkLChRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1), )
if mibBuilder.loadTexts: mscTrkLChRowStatusTable.setStatus('mandatory')
mscTrkLChRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkLChIndex"))
if mibBuilder.loadTexts: mscTrkLChRowStatusEntry.setStatus('mandatory')
mscTrkLChRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChRowStatus.setStatus('mandatory')
mscTrkLChComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChComponentName.setStatus('mandatory')
mscTrkLChStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChStorageType.setStatus('mandatory')
mscTrkLChIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: mscTrkLChIndex.setStatus('mandatory')
mscTrkLChOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10), )
if mibBuilder.loadTexts: mscTrkLChOperTable.setStatus('mandatory')
mscTrkLChOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"), (0, "Nortel-MsCarrier-MscPassport-PorsTrunksMIB", "mscTrkLChIndex"))
if mibBuilder.loadTexts: mscTrkLChOperEntry.setStatus('mandatory')
mscTrkLChNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChNextHop.setStatus('mandatory')
mscTrkLChSetupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChSetupPriority.setStatus('mandatory')
mscTrkLChHoldingPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChHoldingPriority.setStatus('mandatory')
mscTrkLChEmissionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChEmissionPriority.setStatus('mandatory')
mscTrkLChDiscardPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChDiscardPriority.setStatus('mandatory')
mscTrkLChRequiredTxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChRequiredTxBandwidth.setStatus('mandatory')
mscTrkLChRequiredRxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChRequiredRxBandwidth.setStatus('mandatory')
mscTrkLChMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("hdlcFrmMux", 1), ("aal5FrmMux", 2), ("spoFrmMux", 3), ("spoFrmMap", 4), ("aal5FrmMap", 5), ("cellMap", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChMode.setStatus('mandatory')
mscTrkLChMaximumTransmissionUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChMaximumTransmissionUnit.setStatus('mandatory')
mscTrkLChLocalConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 5, 10, 1, 11), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTrkLChLocalConnection.setStatus('mandatory')
porsTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1))
porsTrunksGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1, 1))
porsTrunksGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1, 1, 3))
porsTrunksGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 1, 1, 3, 2))
porsTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3))
porsTrunksCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3, 1))
porsTrunksCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3, 1, 3))
porsTrunksCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 39, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-PorsTrunksMIB", porsTrunksGroupCA02A=porsTrunksGroupCA02A, mscTrkPaState=mscTrkPaState, mscTrkPaPccntTable=mscTrkPaPccntTable, mscTrkPaOperTable=mscTrkPaOperTable, mscTrkPaUsedLc=mscTrkPaUsedLc, porsTrunksGroupCA02=porsTrunksGroupCA02, mscTrkPaMaxReservableBwOut=mscTrkPaMaxReservableBwOut, mscTrkPaStorageType=mscTrkPaStorageType, mscTrkPaNegotiatedMaxLc=mscTrkPaNegotiatedMaxLc, mscTrkPaRowStatus=mscTrkPaRowStatus, mscTrkLChMaximumTransmissionUnit=mscTrkLChMaximumTransmissionUnit, porsTrunksCapabilities=porsTrunksCapabilities, mscTrkLChRowStatusTable=mscTrkLChRowStatusTable, mscTrkPaNegotiatedSupportedTrafficTypes=mscTrkPaNegotiatedSupportedTrafficTypes, mscTrkLCh=mscTrkLCh, mscTrkPaPacntValue=mscTrkPaPacntValue, mscTrkPaRbwEntry=mscTrkPaRbwEntry, mscTrkPaNegotiatedAtmMode=mscTrkPaNegotiatedAtmMode, mscTrkPaNegotiatedTrunkCost=mscTrkPaNegotiatedTrunkCost, mscTrkPaSupportedTrafficTypes=mscTrkPaSupportedTrafficTypes, mscTrkPaComponentName=mscTrkPaComponentName, mscTrkPaPfcntValue=mscTrkPaPfcntValue, mscTrkPaPacntTable=mscTrkPaPacntTable, mscTrkPaRowStatusTable=mscTrkPaRowStatusTable, mscTrkLChSetupPriority=mscTrkLChSetupPriority, mscTrkLChRequiredRxBandwidth=mscTrkLChRequiredRxBandwidth, mscTrkPaOverReservedBwOut=mscTrkPaOverReservedBwOut, mscTrkPaNegotiatedTrunkType=mscTrkPaNegotiatedTrunkType, mscTrkLChEmissionPriority=mscTrkLChEmissionPriority, mscTrkLChIndex=mscTrkLChIndex, mscTrkPaTrunkType=mscTrkPaTrunkType, mscTrkPa=mscTrkPa, porsTrunksCapabilitiesCA02A=porsTrunksCapabilitiesCA02A, mscTrkPaNegotiatedTrunkDelay=mscTrkPaNegotiatedTrunkDelay, porsTrunksCapabilitiesCA=porsTrunksCapabilitiesCA, mscTrkPaOperEntry=mscTrkPaOperEntry, mscTrkPaClashCount=mscTrkPaClashCount, mscTrkPaPacntEntry=mscTrkPaPacntEntry, mscTrkPaRbwTable=mscTrkPaRbwTable, mscTrkPaPbcntTable=mscTrkPaPbcntTable, porsTrunksGroupCA=porsTrunksGroupCA, mscTrkPaUnreservedBwOut=mscTrkPaUnreservedBwOut, mscTrkPaProvEntry=mscTrkPaProvEntry, mscTrkLChNextHop=mscTrkLChNextHop, mscTrkPaPacntIndex=mscTrkPaPacntIndex, mscTrkLChRequiredTxBandwidth=mscTrkLChRequiredTxBandwidth, mscTrkPaRbwValue=mscTrkPaRbwValue, mscTrkPaPfcntEntry=mscTrkPaPfcntEntry, mscTrkPaPbcntIndex=mscTrkPaPbcntIndex, mscTrkPaTrunkCost=mscTrkPaTrunkCost, mscTrkLChComponentName=mscTrkLChComponentName, mscTrkLChDiscardPriority=mscTrkLChDiscardPriority, mscTrkPaPbcntEntry=mscTrkPaPbcntEntry, mscTrkPaMaxLc=mscTrkPaMaxLc, mscTrkPaPccntValue=mscTrkPaPccntValue, mscTrkPaRowStatusEntry=mscTrkPaRowStatusEntry, mscTrkPaPbcntValue=mscTrkPaPbcntValue, porsTrunksMIB=porsTrunksMIB, mscTrkPaCustomerParameter=mscTrkPaCustomerParameter, mscTrkPaPfcntTable=mscTrkPaPfcntTable, mscTrkPaPccntIndex=mscTrkPaPccntIndex, mscTrkPaNegotiatedTrunkSecurity=mscTrkPaNegotiatedTrunkSecurity, mscTrkPaPccntEntry=mscTrkPaPccntEntry, mscTrkLChMode=mscTrkLChMode, porsTrunksGroup=porsTrunksGroup, mscTrkPaRbwIndex=mscTrkPaRbwIndex, mscTrkLChOperTable=mscTrkLChOperTable, mscTrkLChLocalConnection=mscTrkLChLocalConnection, mscTrkPaIndex=mscTrkPaIndex, mscTrkLChHoldingPriority=mscTrkLChHoldingPriority, mscTrkPaNegotiatedCustomerParameter=mscTrkPaNegotiatedCustomerParameter, mscTrkLChOperEntry=mscTrkLChOperEntry, mscTrkPaPfcntIndex=mscTrkPaPfcntIndex, mscTrkLChRowStatus=mscTrkLChRowStatus, mscTrkLChStorageType=mscTrkLChStorageType, mscTrkPaMaxReservedBwOut=mscTrkPaMaxReservedBwOut, mscTrkLChRowStatusEntry=mscTrkLChRowStatusEntry, mscTrkPaProvTable=mscTrkPaProvTable, mscTrkPaTrunkSecurity=mscTrkPaTrunkSecurity, porsTrunksCapabilitiesCA02=porsTrunksCapabilitiesCA02)
