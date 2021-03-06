#
# PySNMP MIB module ATM-ADAPTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-ADAPTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Counter32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Integer32, MibIdentifier, enterprises, TimeTicks, NotificationType, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Integer32", "MibIdentifier", "enterprises", "TimeTicks", "NotificationType", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
atmAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29))
atmAdapterAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1))
atmAdapterMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2))
atmfTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1))
atmfTransmissionTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2))
atmfMediaTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3))
atmfTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4))
atmfUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 1))
atmfSonetSTS3c = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 2))
atmfDs3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 3))
atmf4B5B = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 4))
atmf8B10B = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 2, 5))
atmfMediaUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 1))
atmfMediaCoaxCable = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 2))
atmfMediaSingleMode = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 3))
atmfMediaMultiMode = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 4))
atmfMediaStp = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 5))
atmfMediaUtp = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 3, 6))
atmfUnknownAdapterType = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4, 1))
atmfTurbowaysATM_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 4, 2)).setLabel("atmfTurbowaysATM-100")
muxatmTrap = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxatmTrap.setStatus('mandatory')
if mibBuilder.loadTexts: muxatmTrap.setDescription('An enterprise-specific trap is generated when this MIB variable is read. If the trap is generated, the value of the MIB variable is 1. If the trap fails, the value of the MIB variable is 0.')
muxatmString = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 29, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxatmString.setStatus('mandatory')
if mibBuilder.loadTexts: muxatmString.setDescription('A simple string. It is the title of the ATM MIB.')
atmfAdapterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1))
atmfAtmLayerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2))
atmfAtmStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3))
atmfAdapterTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1), )
if mibBuilder.loadTexts: atmfAdapterTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterTable.setDescription('A table containing all information about the adapter.')
atmfAdapterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1), ).setIndexNames((0, "ATM-ADAPTER-MIB", "atmfAdapterIndex"))
if mibBuilder.loadTexts: atmfAdapterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterEntry.setDescription('An entry in the table containing information about the adapter.')
atmfAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterIndex.setDescription('A unique value which identifies this ATM adapter.')
atmfAdapterSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterSerialNumber.setDescription('The serial number from the VPD of the ATM adapter.')
atmfAdapterDiagVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterDiagVersion.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterDiagVersion.setDescription('The diagnostic version number from the VPD of the ATM adapter.')
atmfAdapterSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterSoftwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterSoftwareVersion.setDescription('The software version number from the VPD of the ATM adapter.')
atmfAdapterTransmitBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9180))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterTransmitBufSize.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterTransmitBufSize.setDescription('The maximum transmit buffer size in bytes.')
atmfAdapterReceiveBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9180))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterReceiveBufSize.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterReceiveBufSize.setDescription('The maximum receive buffer size in bytes.')
atmfAdapterTransmissionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterTransmissionType.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterTransmissionType.setDescription('The Transmission type of this adapter. For example, for a adapter using the Sonet STS-3c physical layer at 155.52 Mbs, this object would have the Object Identifier Value:atmfSonetSTS3c. For the Turboways ATM 100 adapter this value shall be: atmf4B5B.')
atmfAdapterMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 8), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterMediaType.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterMediaType.setDescription('The type of media used on this port. For example, for a adapter using coaxial cable, this object would have the Object Identifier value: atmfMediaCoaxCable. For the Turboways ATM 100 adapter the media type shall be: atmfMediaMultiMode')
atmfAdapterOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("inService", 2), ("outOfService", 3), ("loopBack", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterOperStatus.setDescription('The operational (i.e., actual) state of this adapter. An alarm should not be generated on physical interface when the value of this object is outOfService(3). This capability is useful if equipment is to be disconnected, or for trouble shooting purposes. A value of loopBack(4) indicates that a local loopback is in place.')
atmfAdapterType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 1, 1, 1, 10), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAdapterType.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAdapterType.setDescription('The hardware type of this adapter. For example if the adapter is 100 Mbits MultiMode fiber adapter, then this object would have the Object Identifier value: atmfTurbowaysATM-100')
atmfAtmLayerTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1), )
if mibBuilder.loadTexts: atmfAtmLayerTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerTable.setDescription('A table containing ATM layer configuration information')
atmfAtmLayerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1), ).setIndexNames((0, "ATM-ADAPTER-MIB", "atmfAtmLayerIndex"))
if mibBuilder.loadTexts: atmfAtmLayerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerEntry.setDescription('An entry in the table containing configuration information about the adapter.')
atmfAtmLayerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerIndex.setDescription('A unique value which identifies this ATM adapter.')
atmfAtmLayerMaxVPCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVPCs.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerMaxVPCs.setDescription('The maximum number of VPCs supported on this User to Network Interface.')
atmfAtmLayerMaxVCCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVCCs.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerMaxVCCs.setDescription('The maximum number of VCCs supported on this User to Network Interface.')
atmfAtmLayerConfiguredVPCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVPCs.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVPCs.setDescription('The number of VPCs configured for use on this User to Network Interface.')
atmfAtmLayerConfiguredVCCs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVCCs.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVCCs.setDescription('The number of VCCs configured for use on this User to Network Interface.')
atmfAtmLayerMaxVpiBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVpiBits.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerMaxVpiBits.setDescription('The number of active VPI bits on this interface.')
atmfAtmLayerMaxVciBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVciBits.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerMaxVciBits.setDescription('The number of active VCI bits on this interface.')
atmfAtmLayerUniType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("public", 1), ("private", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerUniType.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmLayerUniType.setDescription('The type of the ATM User to Network Interface, either public or private.')
atmfAtmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1), )
if mibBuilder.loadTexts: atmfAtmStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmStatsTable.setDescription('A table containing ATM layer statistics information.')
atmfAtmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1), ).setIndexNames((0, "ATM-ADAPTER-MIB", "atmfAtmStatsIndex"))
if mibBuilder.loadTexts: atmfAtmStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmStatsEntry.setDescription('An entry in the table containing information about statistics.')
atmfAtmStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmStatsIndex.setDescription('A unique value which identifies this ATM adapter.')
atmfAtmStatsReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsReceivedCells.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmStatsReceivedCells.setDescription('The accumulated number of ATM cells received on this interface which were assigned and not dropped.')
atmfAtmStatsDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsDroppedPackets.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmStatsDroppedPackets.setDescription('The accumulated number of ATM packets which were dropped due to errors in the cell formatting.')
atmfAtmStatsTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 29, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsTransmittedCells.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAtmStatsTransmittedCells.setDescription('The accumulated number of assigned ATM cells which were transmitted across this interface.')
mibBuilder.exportSymbols("ATM-ADAPTER-MIB", atmfAtmLayerMaxVPCs=atmfAtmLayerMaxVPCs, atmfTypes=atmfTypes, atmfTrap=atmfTrap, atmfAdapterTransmitBufSize=atmfAdapterTransmitBufSize, atmfAtmLayerConfiguredVPCs=atmfAtmLayerConfiguredVPCs, atmfAtmStatsEntry=atmfAtmStatsEntry, atmf4B5B=atmf4B5B, atmfSonetSTS3c=atmfSonetSTS3c, ibm=ibm, atmfAtmLayerGroup=atmfAtmLayerGroup, atmfAdapterTable=atmfAdapterTable, atmfAtmLayerTable=atmfAtmLayerTable, atmfAtmLayerConfiguredVCCs=atmfAtmLayerConfiguredVCCs, atmfMediaSingleMode=atmfMediaSingleMode, atmAdapterMib=atmAdapterMib, atmfAtmLayerUniType=atmfAtmLayerUniType, atmfMediaUnknownType=atmfMediaUnknownType, atmfMediaUtp=atmfMediaUtp, atmfAdapterEntry=atmfAdapterEntry, atmfAtmStatsDroppedPackets=atmfAtmStatsDroppedPackets, atmfAtmLayerIndex=atmfAtmLayerIndex, atmfTurbowaysATM_100=atmfTurbowaysATM_100, atmfAtmLayerMaxVCCs=atmfAtmLayerMaxVCCs, atmfAdapterType=atmfAdapterType, atmfUnknownAdapterType=atmfUnknownAdapterType, atmf8B10B=atmf8B10B, atmfUnknownType=atmfUnknownType, atmfAtmStatsTransmittedCells=atmfAtmStatsTransmittedCells, atmfAdapterTransmissionType=atmfAdapterTransmissionType, atmfMediaMultiMode=atmfMediaMultiMode, atmfTransmissionTypes=atmfTransmissionTypes, atmfAdapterIndex=atmfAdapterIndex, atmfAdapterSerialNumber=atmfAdapterSerialNumber, atmfAtmLayerMaxVpiBits=atmfAtmLayerMaxVpiBits, atmfAdapterDiagVersion=atmfAdapterDiagVersion, atmfDs3=atmfDs3, atmfAdapterGroup=atmfAdapterGroup, atmAdapterAdmin=atmAdapterAdmin, muxatmTrap=muxatmTrap, atmfAtmStatsReceivedCells=atmfAtmStatsReceivedCells, atmAdapter=atmAdapter, atmfAtmStatsGroup=atmfAtmStatsGroup, atmfAdapterMediaType=atmfAdapterMediaType, atmfAdapterSoftwareVersion=atmfAdapterSoftwareVersion, atmfAtmLayerEntry=atmfAtmLayerEntry, atmfAtmStatsIndex=atmfAtmStatsIndex, ibmProd=ibmProd, muxatmString=muxatmString, atmfAdapterReceiveBufSize=atmfAdapterReceiveBufSize, atmfAtmLayerMaxVciBits=atmfAtmLayerMaxVciBits, atmfMediaTypes=atmfMediaTypes, atmfMediaCoaxCable=atmfMediaCoaxCable, atmfAtmStatsTable=atmfAtmStatsTable, atmfAdapterOperStatus=atmfAdapterOperStatus, atmfMediaStp=atmfMediaStp)
