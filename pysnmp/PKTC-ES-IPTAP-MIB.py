#
# PySNMP MIB module PKTC-ES-IPTAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PKTC-ES-IPTAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
pktcESSupportMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcESSupportMibs")
InetAddressPrefixLength, InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetPortNumber", "InetAddress", "InetAddressType")
pktcEScTapStreamIndex, pktcEScTapMediationContentId = mibBuilder.importSymbols("PKTC-ES-TAP-MIB", "pktcEScTapStreamIndex", "pktcEScTapMediationContentId")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, TimeTicks, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Gauge32, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Gauge32", "Counter32", "Integer32", "iso")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
pktcESIpTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2))
pktcESIpTapMIB.setRevisions(('2008-04-25 00:00',))
if mibBuilder.loadTexts: pktcESIpTapMIB.setLastUpdated('200804250000Z')
if mibBuilder.loadTexts: pktcESIpTapMIB.setOrganization('Cable Television Laboratories, Inc.')
pktcESIpTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 0))
pktcESIpTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1))
pktcESIpTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2))
pktcESTapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1))
pktcESTapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("ipV4", 2), ("ipV6", 3), ("l4Port", 4), ("dscp", 5), ("voip", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcESTapStreamCapabilities.setStatus('current')
pktcESTapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2), )
if mibBuilder.loadTexts: pktcESTapStreamTable.setStatus('current')
pktcESTapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1), ).setIndexNames((0, "PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId"), (0, "PKTC-ES-TAP-MIB", "pktcEScTapStreamIndex"))
if mibBuilder.loadTexts: pktcESTapStreamEntry.setStatus('current')
pktcESTapStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamInterface.setStatus('current')
pktcESTapStreamAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamAddrType.setStatus('current')
pktcESTapStreamDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 3), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamDestinationAddress.setStatus('current')
pktcESTapStreamDestinationLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 4), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamDestinationLength.setStatus('current')
pktcESTapStreamSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 5), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamSourceAddress.setStatus('current')
pktcESTapStreamSourceLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 6), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamSourceLength.setStatus('current')
pktcESTapStreamTosByte = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamTosByte.setStatus('current')
pktcESTapStreamTosByteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamTosByteMask.setStatus('current')
pktcESTapStreamFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamFlowId.setStatus('current')
pktcESTapStreamProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamProtocol.setStatus('current')
pktcESTapStreamDestL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 11), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamDestL4PortMin.setStatus('current')
pktcESTapStreamDestL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 12), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamDestL4PortMax.setStatus('current')
pktcESTapStreamSourceL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 13), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamSourceL4PortMin.setStatus('current')
pktcESTapStreamSourceL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 14), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamSourceL4PortMax.setStatus('current')
pktcESTapStreamVRF = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 15), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamVRF.setStatus('current')
pktcESTapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcESTapStreamStatus.setStatus('current')
pktcESIpTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 1))
pktcESIpTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 2))
pktcESIpTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 1, 1)).setObjects(("PKTC-ES-IPTAP-MIB", "pktcESIpTapStreamComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcESIpTapMIBCompliance = pktcESIpTapMIBCompliance.setStatus('current')
pktcESIpTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 2, 1)).setObjects(("PKTC-ES-IPTAP-MIB", "pktcESTapStreamCapabilities"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamInterface"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamAddrType"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestinationAddress"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestinationLength"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceAddress"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceLength"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamTosByte"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamTosByteMask"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamFlowId"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamProtocol"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestL4PortMin"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestL4PortMax"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceL4PortMin"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceL4PortMax"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamVRF"), ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcESIpTapStreamComplianceGroup = pktcESIpTapStreamComplianceGroup.setStatus('current')
mibBuilder.exportSymbols("PKTC-ES-IPTAP-MIB", pktcESTapStreamAddrType=pktcESTapStreamAddrType, pktcESTapStreamProtocol=pktcESTapStreamProtocol, pktcESTapStreamVRF=pktcESTapStreamVRF, pktcESIpTapMIBGroups=pktcESIpTapMIBGroups, pktcESTapStreamDestinationLength=pktcESTapStreamDestinationLength, pktcESIpTapStreamComplianceGroup=pktcESIpTapStreamComplianceGroup, pktcESTapStreamCapabilities=pktcESTapStreamCapabilities, pktcESTapStreamSourceL4PortMax=pktcESTapStreamSourceL4PortMax, pktcESIpTapMIBNotifs=pktcESIpTapMIBNotifs, pktcESIpTapMIB=pktcESIpTapMIB, pktcESTapStreamTosByte=pktcESTapStreamTosByte, pktcESTapStreamEncodePacket=pktcESTapStreamEncodePacket, pktcESTapStreamTable=pktcESTapStreamTable, pktcESTapStreamFlowId=pktcESTapStreamFlowId, pktcESIpTapMIBConform=pktcESIpTapMIBConform, pktcESTapStreamDestL4PortMin=pktcESTapStreamDestL4PortMin, pktcESTapStreamInterface=pktcESTapStreamInterface, pktcESTapStreamSourceL4PortMin=pktcESTapStreamSourceL4PortMin, pktcESIpTapMIBCompliances=pktcESIpTapMIBCompliances, pktcESTapStreamTosByteMask=pktcESTapStreamTosByteMask, pktcESTapStreamDestL4PortMax=pktcESTapStreamDestL4PortMax, pktcESTapStreamSourceAddress=pktcESTapStreamSourceAddress, pktcESTapStreamDestinationAddress=pktcESTapStreamDestinationAddress, pktcESTapStreamSourceLength=pktcESTapStreamSourceLength, pktcESIpTapMIBCompliance=pktcESIpTapMIBCompliance, pktcESTapStreamEntry=pktcESTapStreamEntry, pktcESIpTapMIBObjects=pktcESIpTapMIBObjects, PYSNMP_MODULE_ID=pktcESIpTapMIB, pktcESTapStreamStatus=pktcESTapStreamStatus)