#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-DCX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-DCX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoInetAddressMask, CiscoNetworkAddress, TimeIntervalSec, CiscoAlarmSeverity, Unsigned64 = mibBuilder.importSymbols("CISCO-TC", "CiscoInetAddressMask", "CiscoNetworkAddress", "TimeIntervalSec", "CiscoAlarmSeverity", "Unsigned64")
CucsManagedObjectDn, CucsManagedObjectId, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "CucsManagedObjectId", "ciscoUnifiedComputingMIBObjects")
CucsDcxAdminState, CucsDcxState, CucsDpsecForgedTransmit, CucsNwctrlLldpAdminStateBitmask, CucsNetworkPortType, CucsFabricTrafficDirection, CucsDcxOperState, CucsNetworkSwitchId, CucsNetworkLocale, CucsDcxNsAllocStatus, CucsDcxProtState, CucsNetworkPortRole, CucsDcxVIfProtRole, CucsNwctrlRegistrationMode, CucsNwctrlLinkFailAction, CucsAdaptorLinkState, CucsNetworkConnectionType, CucsVnicInstantiation, CucsNwctrlAdminState, CucsFsmLifecycle, CucsNetworkSide, CucsNetworkTransport, CucsQosHostControl = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsDcxAdminState", "CucsDcxState", "CucsDpsecForgedTransmit", "CucsNwctrlLldpAdminStateBitmask", "CucsNetworkPortType", "CucsFabricTrafficDirection", "CucsDcxOperState", "CucsNetworkSwitchId", "CucsNetworkLocale", "CucsDcxNsAllocStatus", "CucsDcxProtState", "CucsNetworkPortRole", "CucsDcxVIfProtRole", "CucsNwctrlRegistrationMode", "CucsNwctrlLinkFailAction", "CucsAdaptorLinkState", "CucsNetworkConnectionType", "CucsVnicInstantiation", "CucsNwctrlAdminState", "CucsFsmLifecycle", "CucsNetworkSide", "CucsNetworkTransport", "CucsQosHostControl")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Counter32, TimeTicks, ModuleIdentity, MibIdentifier, Gauge32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Counter32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Gauge32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Integer32", "Counter64")
RowPointer, TimeInterval, MacAddress, TextualConvention, TruthValue, TimeStamp, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TimeInterval", "MacAddress", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString", "DateAndTime")
cucsDcxObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10))
if mibBuilder.loadTexts: cucsDcxObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsDcxObjects.setOrganization('Cisco Systems Inc.')
cucsDcxFcoeVifEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6), )
if mibBuilder.loadTexts: cucsDcxFcoeVifEpTable.setStatus('current')
cucsDcxFcoeVifEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxFcoeVifEpInstanceId"))
if mibBuilder.loadTexts: cucsDcxFcoeVifEpEntry.setStatus('current')
cucsDcxFcoeVifEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDcxFcoeVifEpInstanceId.setStatus('current')
cucsDcxFcoeVifEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxFcoeVifEpDn.setStatus('current')
cucsDcxFcoeVifEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxFcoeVifEpRn.setStatus('current')
cucsDcxFcoeVifEpId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 6, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxFcoeVifEpId.setStatus('current')
cucsDcxNsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1), )
if mibBuilder.loadTexts: cucsDcxNsTable.setStatus('current')
cucsDcxNsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxNsInstanceId"))
if mibBuilder.loadTexts: cucsDcxNsEntry.setStatus('current')
cucsDcxNsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDcxNsInstanceId.setStatus('current')
cucsDcxNsDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxNsDn.setStatus('current')
cucsDcxNsRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxNsRn.setStatus('current')
cucsDcxNsAllocStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 4), CucsDcxNsAllocStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxNsAllocStatus.setStatus('current')
cucsDcxNsSide = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 5), CucsNetworkSide()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxNsSide.setStatus('current')
cucsDcxNsSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxNsSize.setStatus('current')
cucsDcxNsSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 7), CucsNetworkSwitchId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxNsSwitchId.setStatus('current')
cucsDcxNsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxNsUsed.setStatus('current')
cucsDcxUniverseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2), )
if mibBuilder.loadTexts: cucsDcxUniverseTable.setStatus('current')
cucsDcxUniverseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxUniverseInstanceId"))
if mibBuilder.loadTexts: cucsDcxUniverseEntry.setStatus('current')
cucsDcxUniverseInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDcxUniverseInstanceId.setStatus('current')
cucsDcxUniverseDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxUniverseDn.setStatus('current')
cucsDcxUniverseRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxUniverseRn.setStatus('current')
cucsDcxVIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3), )
if mibBuilder.loadTexts: cucsDcxVIfTable.setStatus('current')
cucsDcxVIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxVIfInstanceId"))
if mibBuilder.loadTexts: cucsDcxVIfEntry.setStatus('current')
cucsDcxVIfInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDcxVIfInstanceId.setStatus('current')
cucsDcxVIfDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfDn.setStatus('current')
cucsDcxVIfRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfRn.setStatus('current')
cucsDcxVIfAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 4), CucsDcxAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfAdminState.setStatus('current')
cucsDcxVIfCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 5), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfCookie.setStatus('current')
cucsDcxVIfEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfEpDn.setStatus('current')
cucsDcxVIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfId.setStatus('current')
cucsDcxVIfIfRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 8), CucsNetworkPortRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfIfRole.setStatus('current')
cucsDcxVIfIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 9), CucsNetworkPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfIfType.setStatus('current')
cucsDcxVIfInstType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 10), CucsVnicInstantiation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfInstType.setStatus('current')
cucsDcxVIfLc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 11), CucsFsmLifecycle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfLc.setStatus('current')
cucsDcxVIfLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 12), CucsAdaptorLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfLinkState.setStatus('current')
cucsDcxVIfLocale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 13), CucsNetworkLocale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfLocale.setStatus('current')
cucsDcxVIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfName.setStatus('current')
cucsDcxVIfOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 15), CucsDcxOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfOperState.setStatus('current')
cucsDcxVIfPeerDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfPeerDn.setStatus('current')
cucsDcxVIfProtPeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfProtPeerId.setStatus('current')
cucsDcxVIfProtRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 18), CucsDcxVIfProtRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfProtRole.setStatus('current')
cucsDcxVIfProtState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 19), CucsDcxProtState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfProtState.setStatus('current')
cucsDcxVIfQosControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 20), CucsQosHostControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfQosControl.setStatus('current')
cucsDcxVIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 21), CucsDcxState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfState.setStatus('current')
cucsDcxVIfSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 22), CucsNetworkSwitchId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfSwitchId.setStatus('current')
cucsDcxVIfTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfTag.setStatus('current')
cucsDcxVIfTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 24), CucsNetworkTransport()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfTransport.setStatus('current')
cucsDcxVIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 3, 1, 25), CucsNetworkConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVIfType.setStatus('current')
cucsDcxVcTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4), )
if mibBuilder.loadTexts: cucsDcxVcTable.setStatus('current')
cucsDcxVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxVcInstanceId"))
if mibBuilder.loadTexts: cucsDcxVcEntry.setStatus('current')
cucsDcxVcInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDcxVcInstanceId.setStatus('current')
cucsDcxVcDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcDn.setStatus('current')
cucsDcxVcRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcRn.setStatus('current')
cucsDcxVcAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 4), CucsDcxAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcAdminState.setStatus('current')
cucsDcxVcBorderPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcBorderPortId.setStatus('current')
cucsDcxVcBorderSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcBorderSlotId.setStatus('current')
cucsDcxVcCdp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 8), CucsNwctrlAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcCdp.setStatus('current')
cucsDcxVcCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 9), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcCookie.setStatus('current')
cucsDcxVcCos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcCos.setStatus('current')
cucsDcxVcDerivedFromId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcDerivedFromId.setStatus('current')
cucsDcxVcEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcEncap.setStatus('current')
cucsDcxVcFcoeId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcFcoeId.setStatus('current')
cucsDcxVcFltAggr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 14), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcFltAggr.setStatus('current')
cucsDcxVcForgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 15), CucsDpsecForgedTransmit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcForgeMac.setStatus('current')
cucsDcxVcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcId.setStatus('current')
cucsDcxVcInstType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 17), CucsVnicInstantiation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcInstType.setStatus('current')
cucsDcxVcLc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 18), CucsFsmLifecycle()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcLc.setStatus('current')
cucsDcxVcLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 19), CucsAdaptorLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcLinkState.setStatus('current')
cucsDcxVcLocale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 20), CucsNetworkLocale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcLocale.setStatus('current')
cucsDcxVcMonTrafDir = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 21), CucsFabricTrafficDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcMonTrafDir.setStatus('current')
cucsDcxVcName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 22), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcName.setStatus('current')
cucsDcxVcOperBorderPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 23), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcOperBorderPortId.setStatus('current')
cucsDcxVcOperBorderSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcOperBorderSlotId.setStatus('current')
cucsDcxVcOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 25), CucsDcxOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcOperState.setStatus('current')
cucsDcxVcProtState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 26), CucsDcxProtState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcProtState.setStatus('current')
cucsDcxVcQosPolicyId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 27), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcQosPolicyId.setStatus('current')
cucsDcxVcRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 29), CucsNetworkPortRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcRole.setStatus('current')
cucsDcxVcState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 30), CucsDcxState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcState.setStatus('current')
cucsDcxVcStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 31), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcStateQual.setStatus('current')
cucsDcxVcSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 32), CucsNetworkSwitchId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcSwitchId.setStatus('current')
cucsDcxVcTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 33), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcTag.setStatus('current')
cucsDcxVcTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 34), CucsNetworkTransport()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcTransport.setStatus('current')
cucsDcxVcType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 35), CucsNetworkConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcType.setStatus('current')
cucsDcxVcUplinkFailAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 36), CucsNwctrlLinkFailAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcUplinkFailAction.setStatus('current')
cucsDcxVcVnic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 37), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcVnic.setStatus('current')
cucsDcxVcPeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 38), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcPeerId.setStatus('current')
cucsDcxVcQosPolicyDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 39), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcQosPolicyDn.setStatus('current')
cucsDcxVcMacRegisterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 40), CucsNwctrlRegistrationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcMacRegisterMode.setStatus('current')
cucsDcxVcBorderVfcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 41), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcBorderVfcId.setStatus('current')
cucsDcxVcLldp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 42), CucsNwctrlLldpAdminStateBitmask()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcLldp.setStatus('current')
cucsDcxVcBorderAggrPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 43), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcBorderAggrPortId.setStatus('current')
cucsDcxVcOperBorderAggrPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 4, 1, 44), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVcOperBorderAggrPortId.setStatus('current')
cucsDcxVifEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5), )
if mibBuilder.loadTexts: cucsDcxVifEpTable.setStatus('current')
cucsDcxVifEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DCX-MIB", "cucsDcxVifEpInstanceId"))
if mibBuilder.loadTexts: cucsDcxVifEpEntry.setStatus('current')
cucsDcxVifEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDcxVifEpInstanceId.setStatus('current')
cucsDcxVifEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVifEpDn.setStatus('current')
cucsDcxVifEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVifEpRn.setStatus('current')
cucsDcxVifEpId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 10, 5, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDcxVifEpId.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-DCX-MIB", cucsDcxVcPeerId=cucsDcxVcPeerId, cucsDcxVcEncap=cucsDcxVcEncap, cucsDcxVIfSwitchId=cucsDcxVIfSwitchId, cucsDcxUniverseRn=cucsDcxUniverseRn, cucsDcxUniverseTable=cucsDcxUniverseTable, cucsDcxVIfLc=cucsDcxVIfLc, cucsDcxVcInstType=cucsDcxVcInstType, cucsDcxUniverseDn=cucsDcxUniverseDn, cucsDcxVcMacRegisterMode=cucsDcxVcMacRegisterMode, cucsDcxUniverseEntry=cucsDcxUniverseEntry, cucsDcxVcBorderPortId=cucsDcxVcBorderPortId, PYSNMP_MODULE_ID=cucsDcxObjects, cucsDcxVcCos=cucsDcxVcCos, cucsDcxVcBorderSlotId=cucsDcxVcBorderSlotId, cucsDcxVifEpRn=cucsDcxVifEpRn, cucsDcxVcBorderVfcId=cucsDcxVcBorderVfcId, cucsDcxVcLc=cucsDcxVcLc, cucsDcxVifEpEntry=cucsDcxVifEpEntry, cucsDcxVIfPeerDn=cucsDcxVIfPeerDn, cucsDcxVcSwitchId=cucsDcxVcSwitchId, cucsDcxVcOperBorderSlotId=cucsDcxVcOperBorderSlotId, cucsDcxVcCookie=cucsDcxVcCookie, cucsDcxVifEpDn=cucsDcxVifEpDn, cucsDcxVcLocale=cucsDcxVcLocale, cucsDcxVcTable=cucsDcxVcTable, cucsDcxNsUsed=cucsDcxNsUsed, cucsDcxNsSwitchId=cucsDcxNsSwitchId, cucsDcxVcRn=cucsDcxVcRn, cucsDcxVIfProtRole=cucsDcxVIfProtRole, cucsDcxNsSide=cucsDcxNsSide, cucsDcxFcoeVifEpRn=cucsDcxFcoeVifEpRn, cucsDcxObjects=cucsDcxObjects, cucsDcxVIfLinkState=cucsDcxVIfLinkState, cucsDcxVIfAdminState=cucsDcxVIfAdminState, cucsDcxVcFltAggr=cucsDcxVcFltAggr, cucsDcxFcoeVifEpInstanceId=cucsDcxFcoeVifEpInstanceId, cucsDcxVcLinkState=cucsDcxVcLinkState, cucsDcxNsEntry=cucsDcxNsEntry, cucsDcxVIfIfRole=cucsDcxVIfIfRole, cucsDcxNsAllocStatus=cucsDcxNsAllocStatus, cucsDcxNsSize=cucsDcxNsSize, cucsDcxVIfEpDn=cucsDcxVIfEpDn, cucsDcxVcOperState=cucsDcxVcOperState, cucsDcxVcTransport=cucsDcxVcTransport, cucsDcxVIfName=cucsDcxVIfName, cucsDcxVifEpInstanceId=cucsDcxVifEpInstanceId, cucsDcxVcDn=cucsDcxVcDn, cucsDcxVcUplinkFailAction=cucsDcxVcUplinkFailAction, cucsDcxVcLldp=cucsDcxVcLldp, cucsDcxVIfState=cucsDcxVIfState, cucsDcxVcEntry=cucsDcxVcEntry, cucsDcxUniverseInstanceId=cucsDcxUniverseInstanceId, cucsDcxVcQosPolicyId=cucsDcxVcQosPolicyId, cucsDcxVcOperBorderAggrPortId=cucsDcxVcOperBorderAggrPortId, cucsDcxVcType=cucsDcxVcType, cucsDcxVIfQosControl=cucsDcxVIfQosControl, cucsDcxFcoeVifEpEntry=cucsDcxFcoeVifEpEntry, cucsDcxVIfRn=cucsDcxVIfRn, cucsDcxFcoeVifEpId=cucsDcxFcoeVifEpId, cucsDcxVIfTransport=cucsDcxVIfTransport, cucsDcxVIfCookie=cucsDcxVIfCookie, cucsDcxNsRn=cucsDcxNsRn, cucsDcxVcId=cucsDcxVcId, cucsDcxVcProtState=cucsDcxVcProtState, cucsDcxVcAdminState=cucsDcxVcAdminState, cucsDcxVcStateQual=cucsDcxVcStateQual, cucsDcxVcCdp=cucsDcxVcCdp, cucsDcxVIfOperState=cucsDcxVIfOperState, cucsDcxVIfInstType=cucsDcxVIfInstType, cucsDcxVcMonTrafDir=cucsDcxVcMonTrafDir, cucsDcxVcInstanceId=cucsDcxVcInstanceId, cucsDcxVcRole=cucsDcxVcRole, cucsDcxVcName=cucsDcxVcName, cucsDcxVIfProtPeerId=cucsDcxVIfProtPeerId, cucsDcxVIfTable=cucsDcxVIfTable, cucsDcxVIfId=cucsDcxVIfId, cucsDcxNsTable=cucsDcxNsTable, cucsDcxVcForgeMac=cucsDcxVcForgeMac, cucsDcxFcoeVifEpTable=cucsDcxFcoeVifEpTable, cucsDcxFcoeVifEpDn=cucsDcxFcoeVifEpDn, cucsDcxVIfType=cucsDcxVIfType, cucsDcxVcBorderAggrPortId=cucsDcxVcBorderAggrPortId, cucsDcxVcTag=cucsDcxVcTag, cucsDcxNsDn=cucsDcxNsDn, cucsDcxVIfIfType=cucsDcxVIfIfType, cucsDcxNsInstanceId=cucsDcxNsInstanceId, cucsDcxVIfLocale=cucsDcxVIfLocale, cucsDcxVIfTag=cucsDcxVIfTag, cucsDcxVcFcoeId=cucsDcxVcFcoeId, cucsDcxVcVnic=cucsDcxVcVnic, cucsDcxVcDerivedFromId=cucsDcxVcDerivedFromId, cucsDcxVifEpId=cucsDcxVifEpId, cucsDcxVcState=cucsDcxVcState, cucsDcxVcQosPolicyDn=cucsDcxVcQosPolicyDn, cucsDcxVcOperBorderPortId=cucsDcxVcOperBorderPortId, cucsDcxVIfInstanceId=cucsDcxVIfInstanceId, cucsDcxVIfDn=cucsDcxVIfDn, cucsDcxVIfProtState=cucsDcxVIfProtState, cucsDcxVifEpTable=cucsDcxVifEpTable, cucsDcxVIfEntry=cucsDcxVIfEntry)
