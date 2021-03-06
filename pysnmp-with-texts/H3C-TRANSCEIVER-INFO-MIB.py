#
# PySNMP MIB module H3C-TRANSCEIVER-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-TRANSCEIVER-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, NotificationType, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ObjectIdentity, Unsigned32, TimeTicks, iso, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "NotificationType", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "TimeTicks", "iso", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cTransceiver = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70))
if mibBuilder.loadTexts: h3cTransceiver.setLastUpdated('200601101452Z')
if mibBuilder.loadTexts: h3cTransceiver.setOrganization('Huawei-3COM Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cTransceiver.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cTransceiver.setDescription('The objects in this MIB module are used to display the information of transceiver on interface.')
h3cTransceiverInfoAdm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1))
h3cTransceiverInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1), )
if mibBuilder.loadTexts: h3cTransceiverInfoTable.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverInfoTable.setDescription('This table show the information of transceiver on interface.')
h3cTransceiverInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cTransceiverInfoEntry.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverInfoEntry.setDescription('The entry of the h3cTransceiverInfoTable.')
h3cTransceiverHardwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverHardwareType.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverHardwareType.setDescription('Hardware type of the interface, such as SM(single mode).')
h3cTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverType.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverType.setDescription('Type of the interface, such as SFP/XFP/GBIC.')
h3cTransceiverWaveLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverWaveLength.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverWaveLength.setDescription('Wave length of the interface, measured in nanometer.')
h3cTransceiverVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverVendorName.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverVendorName.setDescription('Vendor name of the interface.')
h3cTransceiverSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverSerialNumber.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverSerialNumber.setDescription('Serial number of the interface.')
h3cTransceiverFiberDiameterType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("fiber9", 1), ("fiber50", 2), ("fiber625", 3), ("copper", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverFiberDiameterType.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverFiberDiameterType.setDescription('The diameter of the fiber, measured in micron. fiber9 - 9 micron multi-mode fiber fiber50 - 50 micron multi-mode fiber fiber625 - 62.5 micron multi-mode fiber copper - copper cable.')
h3cTransceiverTransferDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 70, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cTransceiverTransferDistance.setStatus('current')
if mibBuilder.loadTexts: h3cTransceiverTransferDistance.setDescription('The max distance which the interface could transmit, measured in micron.')
mibBuilder.exportSymbols("H3C-TRANSCEIVER-INFO-MIB", h3cTransceiverFiberDiameterType=h3cTransceiverFiberDiameterType, h3cTransceiverHardwareType=h3cTransceiverHardwareType, h3cTransceiverTransferDistance=h3cTransceiverTransferDistance, h3cTransceiver=h3cTransceiver, h3cTransceiverInfoTable=h3cTransceiverInfoTable, h3cTransceiverVendorName=h3cTransceiverVendorName, h3cTransceiverType=h3cTransceiverType, PYSNMP_MODULE_ID=h3cTransceiver, h3cTransceiverInfoEntry=h3cTransceiverInfoEntry, h3cTransceiverWaveLength=h3cTransceiverWaveLength, h3cTransceiverInfoAdm=h3cTransceiverInfoAdm, h3cTransceiverSerialNumber=h3cTransceiverSerialNumber)
