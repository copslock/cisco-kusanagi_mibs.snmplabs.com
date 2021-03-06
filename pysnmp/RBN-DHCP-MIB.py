#
# PySNMP MIB module RBN-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnSlot, = mibBuilder.importSymbols("RBN-TC", "RbnSlot")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, ObjectIdentity, MibIdentifier, Unsigned32, Integer32, Counter32, TimeTicks, Counter64, Bits, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Integer32", "Counter32", "TimeTicks", "Counter64", "Bits", "ModuleIdentity", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rbnDhcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 30))
rbnDhcpMib.setRevisions(('2010-03-10 17:00', '2005-10-14 17:00', '2004-05-03 17:00',))
if mibBuilder.loadTexts: rbnDhcpMib.setLastUpdated('201003101700Z')
if mibBuilder.loadTexts: rbnDhcpMib.setOrganization('Redback Networks, Inc.')
rbnDhcpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0))
rbnDhcpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1))
rbnDhcpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2))
rbnDhcpIntfThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1), )
if mibBuilder.loadTexts: rbnDhcpIntfThresholdTable.setStatus('current')
rbnDhcpIntfThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1), ).setIndexNames((1, "RBN-DHCP-MIB", "rbnDhcpIntfThresholdName"))
if mibBuilder.loadTexts: rbnDhcpIntfThresholdEntry.setStatus('current')
rbnDhcpIntfThresholdName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80)))
if mibBuilder.loadTexts: rbnDhcpIntfThresholdName.setStatus('current')
rbnDhcpIntfThresholdContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdContextName.setStatus('current')
rbnDhcpIntfThresholdSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdSize.setStatus('current')
rbnDhcpIntfThresholdAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdAvailable.setStatus('current')
rbnDhcpIntfThresholdInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdInuse.setStatus('current')
rbnDhcpIntfThresholdFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 196608))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdFallingThreshold.setStatus('current')
rbnDhcpIntfThresholdFallingSendTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdFallingSendTrap.setStatus('current')
rbnDhcpIntfThresholdFallingLogMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdFallingLogMessage.setStatus('current')
rbnDhcpIntfThresholdRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 196608))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdRisingThreshold.setStatus('current')
rbnDhcpIntfThresholdRisingSendTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdRisingSendTrap.setStatus('current')
rbnDhcpIntfThresholdRisingLogMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpIntfThresholdRisingLogMessage.setStatus('current')
rbnDhcpRangeThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3), )
if mibBuilder.loadTexts: rbnDhcpRangeThresholdTable.setStatus('current')
rbnDhcpRangeThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1), ).setIndexNames((0, "RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceIdx"), (0, "RBN-DHCP-MIB", "rbnDhcpRangeThresholdAddr"))
if mibBuilder.loadTexts: rbnDhcpRangeThresholdEntry.setStatus('current')
rbnDhcpRangeThresholdInterfaceIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rbnDhcpRangeThresholdInterfaceIdx.setStatus('current')
rbnDhcpRangeThresholdAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: rbnDhcpRangeThresholdAddr.setStatus('current')
rbnDhcpRangeThresholdEndAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdEndAddr.setStatus('current')
rbnDhcpRangeThresholdContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdContextName.setStatus('current')
rbnDhcpRangeThresholdInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdInterfaceName.setStatus('current')
rbnDhcpRangeThresholdSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdSize.setStatus('current')
rbnDhcpRangeThresholdAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdAvailable.setStatus('current')
rbnDhcpRangeThresholdInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdInuse.setStatus('current')
rbnDhcpRangeThresholdFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 196608))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdFallingThreshold.setStatus('current')
rbnDhcpRangeThresholdFallingSendTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdFallingSendTrap.setStatus('current')
rbnDhcpRangeThresholdFallingLogMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdFallingLogMessage.setStatus('current')
rbnDhcpRangeThresholdRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 196608))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdRisingThreshold.setStatus('current')
rbnDhcpRangeThresholdRisingSendTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdRisingSendTrap.setStatus('current')
rbnDhcpRangeThresholdRisingLogMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 3, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpRangeThresholdRisingLogMessage.setStatus('current')
rbnDhcpCtxThreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2))
rbnDhcpCtxThresholdName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdName.setStatus('current')
rbnDhcpCtxThresholdSize = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdSize.setStatus('current')
rbnDhcpCtxThresholdAvailable = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdAvailable.setStatus('current')
rbnDhcpCtxThresholdInuse = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdInuse.setStatus('current')
rbnDhcpCtxThresholdFallingThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 196608))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdFallingThreshold.setStatus('current')
rbnDhcpCtxThresholdFallingSendTrap = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdFallingSendTrap.setStatus('current')
rbnDhcpCtxThresholdFallingLogMessage = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdFallingLogMessage.setStatus('current')
rbnDhcpCtxThresholdRisingThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 196608))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdRisingThreshold.setStatus('current')
rbnDhcpCtxThresholdRisingSendTrap = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdRisingSendTrap.setStatus('current')
rbnDhcpCtxThresholdRisingLogMessage = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 2, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDhcpCtxThresholdRisingLogMessage.setStatus('current')
rbnDhcpLeaseFileStorageSlot = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 4), RbnSlot()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnDhcpLeaseFileStorageSlot.setStatus('current')
rbnDhcpLeaseFileErrorType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 30, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("storageDeviceDegraded", 1), ("storageDeviceFailed", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnDhcpLeaseFileErrorType.setStatus('current')
rbnDhcpIntfThresholdFallingThresholdMet = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 1)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdContextName"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThreshold"))
if mibBuilder.loadTexts: rbnDhcpIntfThresholdFallingThresholdMet.setStatus('current')
rbnDhcpIntfThresholdRisingThresholdMet = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 2)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdContextName"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThreshold"))
if mibBuilder.loadTexts: rbnDhcpIntfThresholdRisingThresholdMet.setStatus('current')
rbnDhcpCtxThresholdFallingThresholdMet = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 3)).setObjects(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThreshold"))
if mibBuilder.loadTexts: rbnDhcpCtxThresholdFallingThresholdMet.setStatus('current')
rbnDhcpCtxThresholdRisingThresholdMet = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 4)).setObjects(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThreshold"))
if mibBuilder.loadTexts: rbnDhcpCtxThresholdRisingThresholdMet.setStatus('current')
rbnDhcpRangeThresholdFallingThresholdMet = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 5)).setObjects(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdContextName"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceName"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdEndAddr"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingThreshold"))
if mibBuilder.loadTexts: rbnDhcpRangeThresholdFallingThresholdMet.setStatus('current')
rbnDhcpRangeThresholdRisingThresholdMet = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 6)).setObjects(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdContextName"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceName"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdEndAddr"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingThreshold"))
if mibBuilder.loadTexts: rbnDhcpRangeThresholdRisingThresholdMet.setStatus('current')
rbnDhcpLeaseFileFailure = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 30, 0, 7)).setObjects(("RBN-DHCP-MIB", "rbnDhcpLeaseFileStorageSlot"), ("RBN-DHCP-MIB", "rbnDhcpLeaseFileErrorType"))
if mibBuilder.loadTexts: rbnDhcpLeaseFileFailure.setStatus('current')
rbnDhcpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1))
rbnDhcpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2))
rbnDhcpThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 1)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdContextName"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdSize"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdInuse"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingLogMessage"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingLogMessage"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdSize"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdInuse"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingLogMessage"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingLogMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpThresholdGroup = rbnDhcpThresholdGroup.setStatus('current')
rbnDhcpThresholdNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 2)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThresholdMet"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThresholdMet"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThresholdMet"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThresholdMet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpThresholdNotifyGroup = rbnDhcpThresholdNotifyGroup.setStatus('current')
rbnDhcpIntfThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 3)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdSize"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdInuse"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingLogMessage"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingLogMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpIntfThresholdGroup = rbnDhcpIntfThresholdGroup.setStatus('current')
rbnDhcpCtxThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 4)).setObjects(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdName"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdSize"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdInuse"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingLogMessage"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingLogMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpCtxThresholdGroup = rbnDhcpCtxThresholdGroup.setStatus('current')
rbnDhcpRangeThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 5)).setObjects(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdEndAddr"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdContextName"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInterfaceName"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdSize"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdInuse"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdAvailable"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingLogMessage"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingThreshold"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingSendTrap"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingLogMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpRangeThresholdGroup = rbnDhcpRangeThresholdGroup.setStatus('current')
rbnDhcpIntfThresholdNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 6)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdFallingThresholdMet"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdRisingThresholdMet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpIntfThresholdNotifyGroup = rbnDhcpIntfThresholdNotifyGroup.setStatus('current')
rbnDhcpCtxThresholdNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 7)).setObjects(("RBN-DHCP-MIB", "rbnDhcpCtxThresholdFallingThresholdMet"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdRisingThresholdMet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpCtxThresholdNotifyGroup = rbnDhcpCtxThresholdNotifyGroup.setStatus('current')
rbnDhcpRangeThresholdNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 8)).setObjects(("RBN-DHCP-MIB", "rbnDhcpRangeThresholdFallingThresholdMet"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdRisingThresholdMet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpRangeThresholdNotifyGroup = rbnDhcpRangeThresholdNotifyGroup.setStatus('current')
rbnDhcpLeaseFileFailureTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 9)).setObjects(("RBN-DHCP-MIB", "rbnDhcpLeaseFileStorageSlot"), ("RBN-DHCP-MIB", "rbnDhcpLeaseFileErrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpLeaseFileFailureTrapGroup = rbnDhcpLeaseFileFailureTrapGroup.setStatus('current')
rbnDhcpLeaseFileFailureNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 2, 10)).setObjects(("RBN-DHCP-MIB", "rbnDhcpLeaseFileFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpLeaseFileFailureNotifyGroup = rbnDhcpLeaseFileFailureNotifyGroup.setStatus('current')
rbnDhcpThresholdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1, 1)).setObjects(("RBN-DHCP-MIB", "rbnDhcpThresholdGroup"), ("RBN-DHCP-MIB", "rbnDhcpThresholdNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpThresholdCompliance = rbnDhcpThresholdCompliance.setStatus('current')
rbnDhcpThresholdCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1, 2)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdGroup"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdGroup"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdGroup"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdNotifyGroup"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdNotifyGroup"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpThresholdCompliance2 = rbnDhcpThresholdCompliance2.setStatus('deprecated')
rbnDhcpThresholdCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 30, 2, 1, 3)).setObjects(("RBN-DHCP-MIB", "rbnDhcpIntfThresholdGroup"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdGroup"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdGroup"), ("RBN-DHCP-MIB", "rbnDhcpIntfThresholdNotifyGroup"), ("RBN-DHCP-MIB", "rbnDhcpCtxThresholdNotifyGroup"), ("RBN-DHCP-MIB", "rbnDhcpRangeThresholdNotifyGroup"), ("RBN-DHCP-MIB", "rbnDhcpLeaseFileFailureTrapGroup"), ("RBN-DHCP-MIB", "rbnDhcpLeaseFileFailureNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDhcpThresholdCompliance3 = rbnDhcpThresholdCompliance3.setStatus('current')
mibBuilder.exportSymbols("RBN-DHCP-MIB", rbnDhcpCtxThresholdRisingThreshold=rbnDhcpCtxThresholdRisingThreshold, rbnDhcpLeaseFileFailureTrapGroup=rbnDhcpLeaseFileFailureTrapGroup, rbnDhcpThresholdCompliance2=rbnDhcpThresholdCompliance2, rbnDhcpThresholdCompliance3=rbnDhcpThresholdCompliance3, rbnDhcpCtxThresholdFallingThresholdMet=rbnDhcpCtxThresholdFallingThresholdMet, rbnDhcpRangeThresholdFallingSendTrap=rbnDhcpRangeThresholdFallingSendTrap, rbnDhcpRangeThresholdEntry=rbnDhcpRangeThresholdEntry, rbnDhcpCtxThresholdRisingThresholdMet=rbnDhcpCtxThresholdRisingThresholdMet, rbnDhcpRangeThresholdInterfaceName=rbnDhcpRangeThresholdInterfaceName, rbnDhcpIntfThresholdRisingSendTrap=rbnDhcpIntfThresholdRisingSendTrap, rbnDhcpRangeThresholdGroup=rbnDhcpRangeThresholdGroup, rbnDhcpLeaseFileFailure=rbnDhcpLeaseFileFailure, rbnDhcpLeaseFileStorageSlot=rbnDhcpLeaseFileStorageSlot, rbnDhcpMib=rbnDhcpMib, rbnDhcpCtxThresholdAvailable=rbnDhcpCtxThresholdAvailable, rbnDhcpCtxThresholdFallingLogMessage=rbnDhcpCtxThresholdFallingLogMessage, rbnDhcpMIBObjects=rbnDhcpMIBObjects, rbnDhcpCtxThresholdFallingSendTrap=rbnDhcpCtxThresholdFallingSendTrap, rbnDhcpIntfThresholdTable=rbnDhcpIntfThresholdTable, rbnDhcpRangeThresholdRisingThreshold=rbnDhcpRangeThresholdRisingThreshold, rbnDhcpIntfThresholdRisingLogMessage=rbnDhcpIntfThresholdRisingLogMessage, rbnDhcpThresholdNotifyGroup=rbnDhcpThresholdNotifyGroup, rbnDhcpRangeThresholdRisingThresholdMet=rbnDhcpRangeThresholdRisingThresholdMet, rbnDhcpIntfThresholdFallingLogMessage=rbnDhcpIntfThresholdFallingLogMessage, rbnDhcpCtxThresholdSize=rbnDhcpCtxThresholdSize, rbnDhcpRangeThresholdAddr=rbnDhcpRangeThresholdAddr, rbnDhcpIntfThresholdFallingThreshold=rbnDhcpIntfThresholdFallingThreshold, rbnDhcpCtxThresholdRisingSendTrap=rbnDhcpCtxThresholdRisingSendTrap, rbnDhcpRangeThresholdSize=rbnDhcpRangeThresholdSize, rbnDhcpIntfThresholdAvailable=rbnDhcpIntfThresholdAvailable, rbnDhcpIntfThresholdRisingThreshold=rbnDhcpIntfThresholdRisingThreshold, rbnDhcpRangeThresholdRisingLogMessage=rbnDhcpRangeThresholdRisingLogMessage, rbnDhcpRangeThresholdInuse=rbnDhcpRangeThresholdInuse, rbnDhcpCtxThresholdName=rbnDhcpCtxThresholdName, rbnDhcpIntfThresholdFallingThresholdMet=rbnDhcpIntfThresholdFallingThresholdMet, rbnDhcpIntfThresholdGroup=rbnDhcpIntfThresholdGroup, rbnDhcpCtxThreshold=rbnDhcpCtxThreshold, rbnDhcpRangeThresholdTable=rbnDhcpRangeThresholdTable, rbnDhcpRangeThresholdEndAddr=rbnDhcpRangeThresholdEndAddr, rbnDhcpCompliances=rbnDhcpCompliances, rbnDhcpMIBNotifications=rbnDhcpMIBNotifications, rbnDhcpIntfThresholdInuse=rbnDhcpIntfThresholdInuse, rbnDhcpCtxThresholdRisingLogMessage=rbnDhcpCtxThresholdRisingLogMessage, rbnDhcpLeaseFileErrorType=rbnDhcpLeaseFileErrorType, rbnDhcpRangeThresholdRisingSendTrap=rbnDhcpRangeThresholdRisingSendTrap, PYSNMP_MODULE_ID=rbnDhcpMib, rbnDhcpRangeThresholdFallingThresholdMet=rbnDhcpRangeThresholdFallingThresholdMet, rbnDhcpIntfThresholdContextName=rbnDhcpIntfThresholdContextName, rbnDhcpRangeThresholdAvailable=rbnDhcpRangeThresholdAvailable, rbnDhcpRangeThresholdFallingThreshold=rbnDhcpRangeThresholdFallingThreshold, rbnDhcpGroups=rbnDhcpGroups, rbnDhcpIntfThresholdRisingThresholdMet=rbnDhcpIntfThresholdRisingThresholdMet, rbnDhcpMIBConformance=rbnDhcpMIBConformance, rbnDhcpThresholdGroup=rbnDhcpThresholdGroup, rbnDhcpRangeThresholdFallingLogMessage=rbnDhcpRangeThresholdFallingLogMessage, rbnDhcpCtxThresholdGroup=rbnDhcpCtxThresholdGroup, rbnDhcpIntfThresholdNotifyGroup=rbnDhcpIntfThresholdNotifyGroup, rbnDhcpIntfThresholdSize=rbnDhcpIntfThresholdSize, rbnDhcpCtxThresholdInuse=rbnDhcpCtxThresholdInuse, rbnDhcpRangeThresholdInterfaceIdx=rbnDhcpRangeThresholdInterfaceIdx, rbnDhcpRangeThresholdContextName=rbnDhcpRangeThresholdContextName, rbnDhcpCtxThresholdFallingThreshold=rbnDhcpCtxThresholdFallingThreshold, rbnDhcpLeaseFileFailureNotifyGroup=rbnDhcpLeaseFileFailureNotifyGroup, rbnDhcpThresholdCompliance=rbnDhcpThresholdCompliance, rbnDhcpIntfThresholdName=rbnDhcpIntfThresholdName, rbnDhcpCtxThresholdNotifyGroup=rbnDhcpCtxThresholdNotifyGroup, rbnDhcpIntfThresholdFallingSendTrap=rbnDhcpIntfThresholdFallingSendTrap, rbnDhcpRangeThresholdNotifyGroup=rbnDhcpRangeThresholdNotifyGroup, rbnDhcpIntfThresholdEntry=rbnDhcpIntfThresholdEntry)
