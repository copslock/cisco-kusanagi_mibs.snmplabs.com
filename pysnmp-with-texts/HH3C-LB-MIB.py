#
# PySNMP MIB module HH3C-LB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Counter64, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter64", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cLB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 116))
hh3cLB.setRevisions(('2010-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cLB.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cLB.setLastUpdated('201012010000Z')
if mibBuilder.loadTexts: hh3cLB.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cLB.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cLB.setDescription('The private mib file includes the loadbalance information of the device.')
hh3cLBTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1))
hh3cLBRealServerGroupTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 1), )
if mibBuilder.loadTexts: hh3cLBRealServerGroupTable.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerGroupTable.setDescription('Real server group table for loadbalance.')
hh3cLBRealServerGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 1, 1), ).setIndexNames((0, "HH3C-LB-MIB", "hh3cLBRealServerGroupName"))
if mibBuilder.loadTexts: hh3cLBRealServerGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerGroupEntry.setDescription('An entry contains the information of the real server group.')
hh3cLBRealServerGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLBRealServerGroupName.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerGroupName.setDescription('Real server group name.')
hh3cLBRealServerTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2), )
if mibBuilder.loadTexts: hh3cLBRealServerTable.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerTable.setDescription('Real server table for loadbalance.')
hh3cLBRealServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1), ).setIndexNames((0, "HH3C-LB-MIB", "hh3cLBRealServerGroupName"), (0, "HH3C-LB-MIB", "hh3cLBRealServerName"))
if mibBuilder.loadTexts: hh3cLBRealServerEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerEntry.setDescription('An entry contains the information of the real server.')
hh3cLBRealServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLBRealServerName.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerName.setDescription('Real server name.')
hh3cLBRealServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("slowdown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLBRealServerStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerStatus.setDescription('A list of real server status type. enabled: the real server is enabled. disabled: the real server is disabled, the loadbalance device does not assign any traffic to the real server. slowdown: the real server continues to process the existed session previously assigned to it, but the loadbalance device does not assign any new session to the real server.')
hh3cLBRealServerConnectNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 116, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLBRealServerConnectNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerConnectNumber.setDescription('The connection number of real server.')
hh3cLBTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 116, 2))
hh3cLBTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 116, 2, 0))
hh3cLBRealServerOverLoad = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 116, 2, 0, 1)).setObjects(("HH3C-LB-MIB", "hh3cLBRealServerGroupName"), ("HH3C-LB-MIB", "hh3cLBRealServerName"), ("HH3C-LB-MIB", "hh3cLBRealServerConnectNumber"))
if mibBuilder.loadTexts: hh3cLBRealServerOverLoad.setStatus('current')
if mibBuilder.loadTexts: hh3cLBRealServerOverLoad.setDescription('This trap is sent when the real server is overloaded.')
mibBuilder.exportSymbols("HH3C-LB-MIB", hh3cLBTables=hh3cLBTables, hh3cLBTrap=hh3cLBTrap, hh3cLBRealServerGroupTable=hh3cLBRealServerGroupTable, hh3cLBRealServerEntry=hh3cLBRealServerEntry, hh3cLB=hh3cLB, hh3cLBRealServerStatus=hh3cLBRealServerStatus, hh3cLBRealServerConnectNumber=hh3cLBRealServerConnectNumber, hh3cLBRealServerGroupEntry=hh3cLBRealServerGroupEntry, hh3cLBRealServerOverLoad=hh3cLBRealServerOverLoad, hh3cLBRealServerGroupName=hh3cLBRealServerGroupName, hh3cLBRealServerName=hh3cLBRealServerName, hh3cLBRealServerTable=hh3cLBRealServerTable, hh3cLBTrapPrex=hh3cLBTrapPrex, PYSNMP_MODULE_ID=hh3cLB)
