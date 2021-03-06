#
# PySNMP MIB module PACEMAKER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACEMAKER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
netSnmp, = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmp")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Counter64, TimeTicks, ObjectIdentity, ModuleIdentity, Integer32, MibIdentifier, Bits, iso, Gauge32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Counter64", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Integer32", "MibIdentifier", "Bits", "iso", "Gauge32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises")
StorageType, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TextualConvention", "DisplayString", "RowStatus")
pacemaker = ModuleIdentity((1, 3, 6, 1, 4, 1, 32723))
pacemaker.setRevisions(('2009-10-05 11:15', '2009-10-06 21:15',))
if mibBuilder.loadTexts: pacemaker.setLastUpdated('200901051115Z')
if mibBuilder.loadTexts: pacemaker.setOrganization('www.clusterlabs.org')
pacemakerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 32723, 1))
pacemakerNotificationNode = MibScalar((1, 3, 6, 1, 4, 1, 32723, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pacemakerNotificationNode.setStatus('current')
pacemakerNotificationResource = MibScalar((1, 3, 6, 1, 4, 1, 32723, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pacemakerNotificationResource.setStatus('current')
pacemakerNotificationOperation = MibScalar((1, 3, 6, 1, 4, 1, 32723, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pacemakerNotificationOperation.setStatus('current')
pacemakerNotificationDescription = MibScalar((1, 3, 6, 1, 4, 1, 32723, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pacemakerNotificationDescription.setStatus('current')
pacemakerNotificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 32723, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pacemakerNotificationStatus.setStatus('current')
pacemakerNotificationReturnCode = MibScalar((1, 3, 6, 1, 4, 1, 32723, 1, 6), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pacemakerNotificationReturnCode.setStatus('current')
pacemakerNotificationTargetReturnCode = MibScalar((1, 3, 6, 1, 4, 1, 32723, 1, 7), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pacemakerNotificationTargetReturnCode.setStatus('current')
mibBuilder.exportSymbols("PACEMAKER-MIB", pacemakerNotificationNode=pacemakerNotificationNode, pacemakerNotificationStatus=pacemakerNotificationStatus, PYSNMP_MODULE_ID=pacemaker, pacemaker=pacemaker, pacemakerNotificationOperation=pacemakerNotificationOperation, pacemakerNotification=pacemakerNotification, pacemakerNotificationReturnCode=pacemakerNotificationReturnCode, pacemakerNotificationDescription=pacemakerNotificationDescription, pacemakerNotificationResource=pacemakerNotificationResource, pacemakerNotificationTargetReturnCode=pacemakerNotificationTargetReturnCode)
