#
# PySNMP MIB module CABH-CAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CABH-CAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
clabProjCableHome, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjCableHome")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, ObjectIdentity, ModuleIdentity, iso, Counter32, TimeTicks, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32", "TimeTicks", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "MibIdentifier", "Bits")
RowStatus, TimeStamp, TextualConvention, PhysAddress, DateAndTime, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "TextualConvention", "PhysAddress", "DateAndTime", "DisplayString", "TruthValue")
cabhCapMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3))
cabhCapMib.setRevisions(('2005-02-11 00:00',))
if mibBuilder.loadTexts: cabhCapMib.setLastUpdated('200502110000Z')
if mibBuilder.loadTexts: cabhCapMib.setOrganization('CableLabs Broadband Access Department')
cabhCapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1))
cabhCapBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1))
cabhCapMap = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2))
cabhCapTcpTimeWait = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 1), Unsigned32().clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCapTcpTimeWait.setStatus('current')
cabhCapUdpTimeWait = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 2), Unsigned32().clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCapUdpTimeWait.setStatus('current')
cabhCapIcmpTimeWait = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 3), Unsigned32().clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCapIcmpTimeWait.setStatus('current')
cabhCapPrimaryMode = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("napt", 1), ("nat", 2), ("passthrough", 3))).clone('napt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCapPrimaryMode.setStatus('current')
cabhCapSetToFactory = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCapSetToFactory.setStatus('current')
cabhCapLastSetToFactory = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCapLastSetToFactory.setStatus('current')
cabhCapUpnpPortForwardingEnable = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 7), TruthValue().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCapUpnpPortForwardingEnable.setStatus('current')
cabhCapUpnpTimeWait = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cabhCapUpnpTimeWait.setStatus('current')
cabhCapMappingTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1), )
if mibBuilder.loadTexts: cabhCapMappingTable.setStatus('current')
cabhCapMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1), ).setIndexNames((0, "CABH-CAP-MIB", "cabhCapMappingIndex"))
if mibBuilder.loadTexts: cabhCapMappingEntry.setStatus('current')
cabhCapMappingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cabhCapMappingIndex.setStatus('current')
cabhCapMappingWanAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingWanAddrType.setStatus('current')
cabhCapMappingWanAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingWanAddr.setStatus('current')
cabhCapMappingWanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingWanPort.setStatus('current')
cabhCapMappingLanAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 5), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingLanAddrType.setStatus('current')
cabhCapMappingLanAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingLanAddr.setStatus('current')
cabhCapMappingLanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 7), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingLanPort.setStatus('current')
cabhCapMappingMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("upnp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCapMappingMethod.setStatus('current')
cabhCapMappingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("other", 1), ("icmp", 2), ("udp", 3), ("tcp", 4), ("all", 255)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingProtocol.setStatus('current')
cabhCapMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingRowStatus.setStatus('current')
cabhCapMappingNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingNumPorts.setStatus('current')
cabhCapMappingRowDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingRowDescr.setStatus('current')
cabhCapMappingCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCapMappingCreateTime.setStatus('current')
cabhCapMappingLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 14), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCapMappingLastUpdateTime.setStatus('current')
cabhCapMappingDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapMappingDuration.setStatus('current')
cabhCapMappingRemoteHostAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 16), InetAddressType().clone('ipv4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCapMappingRemoteHostAddrType.setStatus('current')
cabhCapMappingRemoteHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 17), InetAddress().clone(hexValue="00000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCapMappingRemoteHostAddr.setStatus('current')
cabhCapMappingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 1, 1, 18), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cabhCapMappingEnable.setStatus('current')
cabhCapPassthroughTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2), )
if mibBuilder.loadTexts: cabhCapPassthroughTable.setStatus('current')
cabhCapPassthroughEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1), ).setIndexNames((0, "CABH-CAP-MIB", "cabhCapPassthroughIndex"))
if mibBuilder.loadTexts: cabhCapPassthroughEntry.setStatus('current')
cabhCapPassthroughIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cabhCapPassthroughIndex.setStatus('current')
cabhCapPassthroughMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1, 2), PhysAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapPassthroughMacAddr.setStatus('current')
cabhCapPassthroughRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cabhCapPassthroughRowStatus.setStatus('current')
cabhCapNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 2, 0))
cabhCapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3))
cabhCapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 1))
cabhCapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 2))
cabhCapBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 1, 1)).setObjects(("CABH-CAP-MIB", "cabhCapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cabhCapBasicCompliance = cabhCapBasicCompliance.setStatus('current')
cabhCapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 4, 3, 3, 2, 1)).setObjects(("CABH-CAP-MIB", "cabhCapTcpTimeWait"), ("CABH-CAP-MIB", "cabhCapUdpTimeWait"), ("CABH-CAP-MIB", "cabhCapIcmpTimeWait"), ("CABH-CAP-MIB", "cabhCapPrimaryMode"), ("CABH-CAP-MIB", "cabhCapSetToFactory"), ("CABH-CAP-MIB", "cabhCapLastSetToFactory"), ("CABH-CAP-MIB", "cabhCapMappingWanAddrType"), ("CABH-CAP-MIB", "cabhCapMappingWanAddr"), ("CABH-CAP-MIB", "cabhCapMappingWanPort"), ("CABH-CAP-MIB", "cabhCapMappingLanAddrType"), ("CABH-CAP-MIB", "cabhCapMappingLanAddr"), ("CABH-CAP-MIB", "cabhCapMappingLanPort"), ("CABH-CAP-MIB", "cabhCapMappingMethod"), ("CABH-CAP-MIB", "cabhCapMappingProtocol"), ("CABH-CAP-MIB", "cabhCapMappingRowStatus"), ("CABH-CAP-MIB", "cabhCapPassthroughMacAddr"), ("CABH-CAP-MIB", "cabhCapPassthroughRowStatus"), ("CABH-CAP-MIB", "cabhCapMappingNumPorts"), ("CABH-CAP-MIB", "cabhCapMappingRowDescr"), ("CABH-CAP-MIB", "cabhCapMappingCreateTime"), ("CABH-CAP-MIB", "cabhCapMappingLastUpdateTime"), ("CABH-CAP-MIB", "cabhCapMappingDuration"), ("CABH-CAP-MIB", "cabhCapUpnpPortForwardingEnable"), ("CABH-CAP-MIB", "cabhCapUpnpTimeWait"), ("CABH-CAP-MIB", "cabhCapMappingRemoteHostAddrType"), ("CABH-CAP-MIB", "cabhCapMappingRemoteHostAddr"), ("CABH-CAP-MIB", "cabhCapMappingEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cabhCapGroup = cabhCapGroup.setStatus('current')
mibBuilder.exportSymbols("CABH-CAP-MIB", cabhCapNotification=cabhCapNotification, cabhCapGroups=cabhCapGroups, cabhCapPrimaryMode=cabhCapPrimaryMode, cabhCapGroup=cabhCapGroup, cabhCapMappingRemoteHostAddr=cabhCapMappingRemoteHostAddr, cabhCapMappingTable=cabhCapMappingTable, cabhCapPassthroughIndex=cabhCapPassthroughIndex, cabhCapMappingNumPorts=cabhCapMappingNumPorts, cabhCapMappingRowDescr=cabhCapMappingRowDescr, cabhCapUdpTimeWait=cabhCapUdpTimeWait, cabhCapMib=cabhCapMib, cabhCapLastSetToFactory=cabhCapLastSetToFactory, cabhCapConformance=cabhCapConformance, cabhCapMappingMethod=cabhCapMappingMethod, PYSNMP_MODULE_ID=cabhCapMib, cabhCapUpnpPortForwardingEnable=cabhCapUpnpPortForwardingEnable, cabhCapMappingLanAddr=cabhCapMappingLanAddr, cabhCapMappingWanAddr=cabhCapMappingWanAddr, cabhCapMappingLanPort=cabhCapMappingLanPort, cabhCapMappingWanPort=cabhCapMappingWanPort, cabhCapMappingLastUpdateTime=cabhCapMappingLastUpdateTime, cabhCapMappingDuration=cabhCapMappingDuration, cabhCapPassthroughMacAddr=cabhCapPassthroughMacAddr, cabhCapMappingIndex=cabhCapMappingIndex, cabhCapPassthroughEntry=cabhCapPassthroughEntry, cabhCapMappingProtocol=cabhCapMappingProtocol, cabhCapCompliances=cabhCapCompliances, cabhCapBasicCompliance=cabhCapBasicCompliance, cabhCapMappingLanAddrType=cabhCapMappingLanAddrType, cabhCapTcpTimeWait=cabhCapTcpTimeWait, cabhCapBase=cabhCapBase, cabhCapObjects=cabhCapObjects, cabhCapMappingRowStatus=cabhCapMappingRowStatus, cabhCapMappingEntry=cabhCapMappingEntry, cabhCapMap=cabhCapMap, cabhCapMappingRemoteHostAddrType=cabhCapMappingRemoteHostAddrType, cabhCapUpnpTimeWait=cabhCapUpnpTimeWait, cabhCapIcmpTimeWait=cabhCapIcmpTimeWait, cabhCapMappingWanAddrType=cabhCapMappingWanAddrType, cabhCapSetToFactory=cabhCapSetToFactory, cabhCapMappingCreateTime=cabhCapMappingCreateTime, cabhCapMappingEnable=cabhCapMappingEnable, cabhCapPassthroughRowStatus=cabhCapPassthroughRowStatus, cabhCapPassthroughTable=cabhCapPassthroughTable)
