#
# PySNMP MIB module ARTEM-COMPOINT-BLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARTEM-COMPOINT-BLD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, MibIdentifier, Integer32, NotificationType, IpAddress, Counter32, Counter64, ModuleIdentity, enterprises, TimeTicks, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "MibIdentifier", "Integer32", "NotificationType", "IpAddress", "Counter32", "Counter64", "ModuleIdentity", "enterprises", "TimeTicks", "iso", "Bits")
DisplayString, MacAddress, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TruthValue", "TextualConvention", "RowStatus")
artem = ModuleIdentity((1, 3, 6, 1, 4, 1, 4280))
artem.setRevisions(('2005-06-10 12:17', '2005-05-24 13:24', '2005-04-29 12:05',))
if mibBuilder.loadTexts: artem.setLastUpdated('200506101217Z')
if mibBuilder.loadTexts: artem.setOrganization('Funkwerk Enterprise Communications.')
artemBLD = ObjectIdentity((1, 3, 6, 1, 4, 1, 4280, 6))
if mibBuilder.loadTexts: artemBLD.setStatus('current')
artemBLDAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4280, 6, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: artemBLDAdminStatus.setStatus('current')
artemBLDLinkState = MibScalar((1, 3, 6, 1, 4, 1, 4280, 6, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artemBLDLinkState.setStatus('current')
artemBLDTargetAddress = MibScalar((1, 3, 6, 1, 4, 1, 4280, 6, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: artemBLDTargetAddress.setStatus('current')
artemBLDTargetIf = MibScalar((1, 3, 6, 1, 4, 1, 4280, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: artemBLDTargetIf.setStatus('current')
artemBLDCheckInterval = MibScalar((1, 3, 6, 1, 4, 1, 4280, 6, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: artemBLDCheckInterval.setStatus('current')
artemBLDTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4280, 6, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: artemBLDTimeout.setStatus('current')
artemBLDRetries = MibScalar((1, 3, 6, 1, 4, 1, 4280, 6, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: artemBLDRetries.setStatus('current')
artemBLDIfTable = MibTable((1, 3, 6, 1, 4, 1, 4280, 6, 8), )
if mibBuilder.loadTexts: artemBLDIfTable.setStatus('current')
artemBLDIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4280, 6, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: artemBLDIfEntry.setStatus('current')
artemBLDIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4280, 6, 8, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: artemBLDIfRowStatus.setStatus('current')
artemBLDNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4280, 6, 9))
artemBLDConnection = NotificationType((1, 3, 6, 1, 4, 1, 4280, 6, 9, 1)).setObjects(("IF-MIB", "ifIndex"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDLinkState"))
if mibBuilder.loadTexts: artemBLDConnection.setStatus('current')
artemBLDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4280, 6, 10)).setObjects(("ARTEM-COMPOINT-BLD-MIB", "artemBLDAdminStatus"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDLinkState"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDTargetAddress"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDTargetIf"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDCheckInterval"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDTimeout"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDRetries"), ("ARTEM-COMPOINT-BLD-MIB", "artemBLDIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    artemBLDGroup = artemBLDGroup.setStatus('current')
artemBLDNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4280, 6, 11)).setObjects(("ARTEM-COMPOINT-BLD-MIB", "artemBLDConnection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    artemBLDNotificationGroup = artemBLDNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ARTEM-COMPOINT-BLD-MIB", PYSNMP_MODULE_ID=artem, artemBLDNotificationGroup=artemBLDNotificationGroup, artemBLDConnection=artemBLDConnection, artemBLDRetries=artemBLDRetries, artemBLDTimeout=artemBLDTimeout, artem=artem, artemBLDTargetIf=artemBLDTargetIf, artemBLDIfTable=artemBLDIfTable, artemBLD=artemBLD, artemBLDLinkState=artemBLDLinkState, artemBLDGroup=artemBLDGroup, artemBLDCheckInterval=artemBLDCheckInterval, artemBLDIfEntry=artemBLDIfEntry, artemBLDIfRowStatus=artemBLDIfRowStatus, artemBLDTargetAddress=artemBLDTargetAddress, artemBLDAdminStatus=artemBLDAdminStatus, artemBLDNotification=artemBLDNotification)
