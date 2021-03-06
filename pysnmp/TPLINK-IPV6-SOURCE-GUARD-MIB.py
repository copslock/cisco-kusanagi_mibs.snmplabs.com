#
# PySNMP MIB module TPLINK-IPV6-SOURCE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-IPV6-SOURCE-GUARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Gauge32, ModuleIdentity, Counter64, iso, MibIdentifier, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64", "iso", "MibIdentifier", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkIpv6SourceGuardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 94))
tplinkIpv6SourceGuardMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkIpv6SourceGuardMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkIpv6SourceGuardMIB.setOrganization('TPLINK')
tplinkIpv6SourceGuardMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1))
tplinkIpv6SourceGuardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 94, 2))
tpIpv6SourceGuardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1))
tpIpv6SourceGuardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1), )
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigTable.setStatus('current')
tpIpv6SourceGuardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigEntry.setStatus('current')
tpIpv6SourceGuardConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigPort.setStatus('current')
tpIpv6SourceGuardConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("disable", 0), ("sipv6-mac", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigType.setStatus('current')
tpIpv6SourceGuardConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigPortLag.setStatus('current')
mibBuilder.exportSymbols("TPLINK-IPV6-SOURCE-GUARD-MIB", tpIpv6SourceGuardConfigTable=tpIpv6SourceGuardConfigTable, tpIpv6SourceGuardConfigPortLag=tpIpv6SourceGuardConfigPortLag, tplinkIpv6SourceGuardMIBObjects=tplinkIpv6SourceGuardMIBObjects, tpIpv6SourceGuardConfigEntry=tpIpv6SourceGuardConfigEntry, tpIpv6SourceGuardConfigPort=tpIpv6SourceGuardConfigPort, tplinkIpv6SourceGuardNotifications=tplinkIpv6SourceGuardNotifications, tpIpv6SourceGuardConfigType=tpIpv6SourceGuardConfigType, PYSNMP_MODULE_ID=tplinkIpv6SourceGuardMIB, tplinkIpv6SourceGuardMIB=tplinkIpv6SourceGuardMIB, tpIpv6SourceGuardConfig=tpIpv6SourceGuardConfig)
