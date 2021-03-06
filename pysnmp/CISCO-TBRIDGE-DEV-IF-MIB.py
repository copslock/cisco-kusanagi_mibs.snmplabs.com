#
# PySNMP MIB module CISCO-TBRIDGE-DEV-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TBRIDGE-DEV-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, ModuleIdentity, Unsigned32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, iso, TimeTicks, Gauge32, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Unsigned32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "iso", "TimeTicks", "Gauge32", "NotificationType", "Counter32")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
ciscoTBridgeDevIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 269))
ciscoTBridgeDevIfMIB.setRevisions(('2002-04-03 00:01',))
if mibBuilder.loadTexts: ciscoTBridgeDevIfMIB.setLastUpdated('200204030001Z')
if mibBuilder.loadTexts: ciscoTBridgeDevIfMIB.setOrganization('Cisco System Inc.')
ciscoTBridgeDevIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 269, 1))
ctbrDevInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1))
ctbrDevInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1), )
if mibBuilder.loadTexts: ctbrDevInterfaceTable.setStatus('current')
ctbrDevInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctbrDevInterfaceEntry.setStatus('current')
ctbrDefaultPhyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctbrDefaultPhyAddress.setStatus('current')
ctbrPhyAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrPhyAddress.setStatus('current')
ctbrDefaultIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrDefaultIpAddrType.setStatus('current')
ctbrDefaultIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrDefaultIpAddress.setStatus('current')
ctbrDefaultIpMaskType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrDefaultIpMaskType.setStatus('current')
ctbrDefaultIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrDefaultIpMask.setStatus('current')
ctbrIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 7), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrIpAddressType.setStatus('current')
ctbrIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 8), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrIpAddress.setStatus('current')
ctbrIpMaskType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 9), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrIpMaskType.setStatus('current')
ctbrIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 10), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctbrIpMask.setStatus('current')
ctbrMSDUMaxLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 269, 1, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctbrMSDUMaxLength.setStatus('current')
ciscoTBridgeDevIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 269, 2))
ciscoTBridgeDevIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 1))
ciscoTBridgeDevIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 2))
ciscoTBridgeDevIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 1, 1)).setObjects(("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDevIfConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTBridgeDevIfCompliance = ciscoTBridgeDevIfCompliance.setStatus('current')
ctbrDevIfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 269, 2, 2, 1)).setObjects(("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultPhyAddress"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrPhyAddress"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpAddrType"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpAddress"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpMaskType"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrDefaultIpMask"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpAddressType"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpAddress"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpMaskType"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrIpMask"), ("CISCO-TBRIDGE-DEV-IF-MIB", "ctbrMSDUMaxLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctbrDevIfConfigGroup = ctbrDevIfConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-TBRIDGE-DEV-IF-MIB", ctbrDefaultIpAddress=ctbrDefaultIpAddress, ctbrPhyAddress=ctbrPhyAddress, ctbrDefaultIpMask=ctbrDefaultIpMask, ctbrDefaultIpAddrType=ctbrDefaultIpAddrType, ctbrIpMaskType=ctbrIpMaskType, ctbrDevIfConfigGroup=ctbrDevIfConfigGroup, ctbrDefaultPhyAddress=ctbrDefaultPhyAddress, ciscoTBridgeDevIfMIBCompliances=ciscoTBridgeDevIfMIBCompliances, ciscoTBridgeDevIfMIB=ciscoTBridgeDevIfMIB, ctbrMSDUMaxLength=ctbrMSDUMaxLength, ctbrIpAddress=ctbrIpAddress, ciscoTBridgeDevIfMIBGroups=ciscoTBridgeDevIfMIBGroups, ctbrIpAddressType=ctbrIpAddressType, ciscoTBridgeDevIfMIBObjects=ciscoTBridgeDevIfMIBObjects, ctbrDevInterface=ctbrDevInterface, ciscoTBridgeDevIfCompliance=ciscoTBridgeDevIfCompliance, ciscoTBridgeDevIfMIBConformance=ciscoTBridgeDevIfMIBConformance, PYSNMP_MODULE_ID=ciscoTBridgeDevIfMIB, ctbrDevInterfaceEntry=ctbrDevInterfaceEntry, ctbrDevInterfaceTable=ctbrDevInterfaceTable, ctbrDefaultIpMaskType=ctbrDefaultIpMaskType, ctbrIpMask=ctbrIpMask)
