#
# PySNMP MIB module CENTILLION-LANE-V2-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-LANE-V2-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
atmLane, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "atmLane")
AtmLaneAddress, = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "AtmLaneAddress")
elanConfIndex, lecsConfIndex = mibBuilder.importSymbols("LAN-EMULATION-ELAN-MIB", "elanConfIndex", "lecsConfIndex")
lesConfIndex, = mibBuilder.importSymbols("LAN-EMULATION-LES-MIB", "lesConfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, Gauge32, Counter64, iso, ObjectIdentity, Counter32, TimeTicks, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Gauge32", "Counter64", "iso", "ObjectIdentity", "Counter32", "TimeTicks", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
TruthValue, = mibBuilder.importSymbols("SNMPv2-TC-v1", "TruthValue")
cnLesV2ExtnGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7))
cnLecsV2ExtnGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8))
cnElanV2ExtnGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9))
class CnLesLecDataFrameSize(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("max1516", 2), ("max4544", 3), ("max9234", 4), ("max18190", 5), ("max1580", 6))

cnLesV2ExtnTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1), )
if mibBuilder.loadTexts: cnLesV2ExtnTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLesV2ExtnTable.setDescription('LES LANEv2 extension table')
cnLesV2ExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1), ).setIndexNames((0, "LAN-EMULATION-LES-MIB", "lesConfIndex"))
if mibBuilder.loadTexts: cnLesV2ExtnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnLesV2ExtnEntry.setDescription('An extension to the lesConfEntry which contains objects associated to a LES.')
cnLesV2ExtnV2Capable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLesV2ExtnV2Capable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLesV2ExtnV2Capable.setDescription('LES V2 Capable. Indicates whether this LES is setup to behave as a LANE V2 LES. A setting which will be used for the LEC the next time it joins.')
cnLesV2ExtnElanID = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLesV2ExtnElanID.setStatus('mandatory')
if mibBuilder.loadTexts: cnLesV2ExtnElanID.setDescription('The ELAN-ID associated with this LES.')
cnLesV2ExtnMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1, 3), CnLesLecDataFrameSize()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLesV2ExtnMaxFrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: cnLesV2ExtnMaxFrameSize.setDescription('The maximum AAL-5 SDU size of a data frame that the LE service can guarantee not to drop because it is too large.')
cnLecsV2ExtnTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8, 1), )
if mibBuilder.loadTexts: cnLecsV2ExtnTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsV2ExtnTable.setDescription('LECS LANEv2 extension table')
cnLecsV2ExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8, 1, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"))
if mibBuilder.loadTexts: cnLecsV2ExtnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsV2ExtnEntry.setDescription('An extension to the lecsConfEntry which contains objects associated to a LECS.')
cnLecsV2ExtnWellKnownAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8, 1, 1, 1), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnLecsV2ExtnWellKnownAtmAddress.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsV2ExtnWellKnownAtmAddress.setDescription('LECS LANEv2 well-known ATM Address. For LANEv2: C500790000000000000000000000A03E00000100')
cnElanV2ExtnTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1), )
if mibBuilder.loadTexts: cnElanV2ExtnTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnElanV2ExtnTable.setDescription('ELAN LANEv2 extension table')
cnElanV2ExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"))
if mibBuilder.loadTexts: cnElanV2ExtnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnElanV2ExtnEntry.setDescription('An extension to the elanConfEntry which contains objects associated to an ELAN.')
cnElanV2ExtnV2Capable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnElanV2ExtnV2Capable.setStatus('mandatory')
if mibBuilder.loadTexts: cnElanV2ExtnV2Capable.setDescription('ELAN V2 Capable. Indicates whether this ELAN is setup to behave as a LANE V2 ELAN. A setting which will be used for the LEC the next time it joins.')
cnElanV2ExtnElanID = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnElanV2ExtnElanID.setStatus('mandatory')
if mibBuilder.loadTexts: cnElanV2ExtnElanID.setDescription('The ELAN-ID associated with this ELAN.')
mibBuilder.exportSymbols("CENTILLION-LANE-V2-EXT-MIB", cnLesV2ExtnTable=cnLesV2ExtnTable, cnLesV2ExtnGroup=cnLesV2ExtnGroup, cnLecsV2ExtnGroup=cnLecsV2ExtnGroup, cnLesV2ExtnEntry=cnLesV2ExtnEntry, cnElanV2ExtnEntry=cnElanV2ExtnEntry, cnElanV2ExtnV2Capable=cnElanV2ExtnV2Capable, cnLesV2ExtnMaxFrameSize=cnLesV2ExtnMaxFrameSize, cnLesV2ExtnElanID=cnLesV2ExtnElanID, cnLecsV2ExtnWellKnownAtmAddress=cnLecsV2ExtnWellKnownAtmAddress, cnLesV2ExtnV2Capable=cnLesV2ExtnV2Capable, CnLesLecDataFrameSize=CnLesLecDataFrameSize, cnElanV2ExtnElanID=cnElanV2ExtnElanID, cnLecsV2ExtnTable=cnLecsV2ExtnTable, cnElanV2ExtnTable=cnElanV2ExtnTable, cnLecsV2ExtnEntry=cnLecsV2ExtnEntry, cnElanV2ExtnGroup=cnElanV2ExtnGroup)
