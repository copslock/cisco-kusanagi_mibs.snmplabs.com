#
# PySNMP MIB module WWP-MULTI-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-MULTI-DHCP-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, NotificationType, MibIdentifier, Bits, ObjectIdentity, Counter32, ModuleIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "NotificationType", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "ModuleIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpMultiDhcpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 42))
wwpMultiDhcpClientMIB.setRevisions(('2002-11-01 17:00',))
if mibBuilder.loadTexts: wwpMultiDhcpClientMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpMultiDhcpClientMIB.setOrganization('World Wide Packets, Inc')
wwpMultiDhcpClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1))
wwpMultiDhcpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1))
wwpMultiDhcpClientMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 42, 2))
wwpMultiDhcpClientMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 42, 2, 0))
wwpMultiDhcpClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 42, 3))
wwpMultiDhcpClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 42, 3, 1))
wwpMultiDhcpClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 42, 3, 2))
wwpMultiDhcpClientNumber = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMultiDhcpClientNumber.setStatus('current')
wwpMultiDhcpClientTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2), )
if mibBuilder.loadTexts: wwpMultiDhcpClientTable.setStatus('current')
wwpMultiDhcpClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1), ).setIndexNames((0, "WWP-MULTI-DHCP-CLIENT-MIB", "wwpDhcpIfIndex"))
if mibBuilder.loadTexts: wwpMultiDhcpClientEntry.setStatus('current')
wwpDhcpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpIfIndex.setStatus('current')
wwpDhcpIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpIfName.setStatus('current')
wwpDhcpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpStatus.setStatus('current')
wwpDhcpState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("bound", 1), ("disabled", 2), ("inform", 3), ("init", 4), ("rebinding", 5), ("renewing", 6), ("requesting", 7), ("selecting", 8), ("unknown", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpState.setStatus('current')
wwpDhcpLeaseTimeRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(45)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpLeaseTimeRequested.setStatus('current')
wwpDhcpLeaseOffered = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpLeaseOffered.setStatus('current')
wwpDhcpLeaseRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpLeaseRemaining.setStatus('current')
wwpDhcpDiscoveryMsgInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpDiscoveryMsgInterval.setStatus('current')
wwpDhcpRenewalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpRenewalTime.setStatus('current')
wwpDhcpRebindingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpRebindingTime.setStatus('current')
wwpDhcpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpDhcpServerAddress.setStatus('current')
wwpDhcpRenewLease = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpRenewLease.setStatus('current')
wwpDhcpReleaseLease = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 42, 1, 1, 2, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpDhcpReleaseLease.setStatus('current')
mibBuilder.exportSymbols("WWP-MULTI-DHCP-CLIENT-MIB", wwpMultiDhcpClient=wwpMultiDhcpClient, wwpDhcpState=wwpDhcpState, wwpMultiDhcpClientNumber=wwpMultiDhcpClientNumber, wwpMultiDhcpClientMIBConformance=wwpMultiDhcpClientMIBConformance, wwpMultiDhcpClientMIBGroups=wwpMultiDhcpClientMIBGroups, wwpMultiDhcpClientTable=wwpMultiDhcpClientTable, wwpDhcpLeaseTimeRequested=wwpDhcpLeaseTimeRequested, wwpDhcpRebindingTime=wwpDhcpRebindingTime, wwpDhcpIfName=wwpDhcpIfName, wwpMultiDhcpClientMIBNotifications=wwpMultiDhcpClientMIBNotifications, wwpDhcpLeaseOffered=wwpDhcpLeaseOffered, wwpDhcpServerAddress=wwpDhcpServerAddress, wwpDhcpReleaseLease=wwpDhcpReleaseLease, wwpDhcpLeaseRemaining=wwpDhcpLeaseRemaining, wwpMultiDhcpClientEntry=wwpMultiDhcpClientEntry, wwpDhcpIfIndex=wwpDhcpIfIndex, wwpMultiDhcpClientMIBNotificationPrefix=wwpMultiDhcpClientMIBNotificationPrefix, wwpDhcpDiscoveryMsgInterval=wwpDhcpDiscoveryMsgInterval, wwpMultiDhcpClientMIB=wwpMultiDhcpClientMIB, wwpMultiDhcpClientMIBCompliances=wwpMultiDhcpClientMIBCompliances, wwpMultiDhcpClientMIBObjects=wwpMultiDhcpClientMIBObjects, PYSNMP_MODULE_ID=wwpMultiDhcpClientMIB, wwpDhcpRenewalTime=wwpDhcpRenewalTime, wwpDhcpStatus=wwpDhcpStatus, wwpDhcpRenewLease=wwpDhcpRenewLease)
