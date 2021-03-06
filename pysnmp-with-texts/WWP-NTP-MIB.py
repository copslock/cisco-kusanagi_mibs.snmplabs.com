#
# PySNMP MIB module WWP-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-NTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, Unsigned32, NotificationType, iso, Counter64, TimeTicks, ObjectIdentity, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Unsigned32", "NotificationType", "iso", "Counter64", "TimeTicks", "ObjectIdentity", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 5))
wwpNtpMIB.setRevisions(('2003-03-11 00:00', '2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpNtpMIB.setRevisionsDescriptions(('The description of wwpNtpPollFreq is updated.', 'Initial creation.',))
if mibBuilder.loadTexts: wwpNtpMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpNtpMIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpNtpMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpNtpMIB.setDescription('This MIB module defines the generic managed objects for NTP on WWP devices.')
wwpNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1))
wwpNtp = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1))
wwpNtpMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 5, 2))
wwpNtpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 5, 2, 0))
wwpNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 5, 3))
wwpNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 5, 3, 1))
wwpNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 5, 3, 2))
wwpNtpRcvBroadcasts = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpNtpRcvBroadcasts.setStatus('current')
if mibBuilder.loadTexts: wwpNtpRcvBroadcasts.setDescription('Enables or disables the reception of NTP broadcasts from a host. WWP products will only accept broadcasts from those NTP servers listed in the NTP table below.')
wwpNtpEnablePolling = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpNtpEnablePolling.setStatus('current')
if mibBuilder.loadTexts: wwpNtpEnablePolling.setDescription('Enables or disables NTP polling.')
wwpNtpPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpNtpPollFreq.setStatus('current')
if mibBuilder.loadTexts: wwpNtpPollFreq.setDescription('WWP products can also be configured to poll a server for the current time every x seconds. pollTime is in seconds.')
wwpNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4), )
if mibBuilder.loadTexts: wwpNtpServerTable.setStatus('current')
if mibBuilder.loadTexts: wwpNtpServerTable.setDescription('Table of NTP server information.')
wwpNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4, 1), ).setIndexNames((0, "WWP-NTP-MIB", "wwpNtpServerIpAddr"))
if mibBuilder.loadTexts: wwpNtpServerEntry.setStatus('current')
if mibBuilder.loadTexts: wwpNtpServerEntry.setDescription('An entry for each NTP server that the switch should be aware of.')
wwpNtpServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpNtpServerIpAddr.setStatus('current')
if mibBuilder.loadTexts: wwpNtpServerIpAddr.setDescription('The IP address of the NTP server.')
wwpNtpServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 5, 1, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpNtpServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: wwpNtpServerRowStatus.setDescription("To create a row in this table, a manager must set this object to 'createAndGo'.")
mibBuilder.exportSymbols("WWP-NTP-MIB", wwpNtpServerEntry=wwpNtpServerEntry, wwpNtpMIBNotificationPrefix=wwpNtpMIBNotificationPrefix, wwpNtpMIBNotifications=wwpNtpMIBNotifications, wwpNtpMIBConformance=wwpNtpMIBConformance, wwpNtpServerRowStatus=wwpNtpServerRowStatus, wwpNtpPollFreq=wwpNtpPollFreq, PYSNMP_MODULE_ID=wwpNtpMIB, wwpNtpMIBObjects=wwpNtpMIBObjects, wwpNtp=wwpNtp, wwpNtpServerIpAddr=wwpNtpServerIpAddr, wwpNtpServerTable=wwpNtpServerTable, wwpNtpMIB=wwpNtpMIB, wwpNtpMIBCompliances=wwpNtpMIBCompliances, wwpNtpRcvBroadcasts=wwpNtpRcvBroadcasts, wwpNtpMIBGroups=wwpNtpMIBGroups, wwpNtpEnablePolling=wwpNtpEnablePolling)
