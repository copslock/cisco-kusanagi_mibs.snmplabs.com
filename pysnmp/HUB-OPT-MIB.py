#
# PySNMP MIB module HUB-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUB-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, ModuleIdentity, Counter64, Unsigned32, iso, enterprises, ObjectIdentity, Bits, Gauge32, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "ModuleIdentity", "Counter64", "Unsigned32", "iso", "enterprises", "ObjectIdentity", "Bits", "Gauge32", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class DisplayString(OctetString):
    pass

cdx6500PPCTHUBPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22), )
if mibBuilder.loadTexts: cdx6500PPCTHUBPortTable.setStatus('mandatory')
cdx6500PPCTHUBPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22, 1), ).setIndexNames((0, "HUB-OPT-MIB", "cdx6500HUBCfgPortNumber"))
if mibBuilder.loadTexts: cdx6500PPCTHUBPortEntry.setStatus('mandatory')
cdx6500HUBCfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(13, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500HUBCfgPortNumber.setStatus('mandatory')
cdx6500HUBCfgPortLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 22, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reduced", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500HUBCfgPortLevel.setStatus('mandatory')
cdx6500PPSTHUBPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23), )
if mibBuilder.loadTexts: cdx6500PPSTHUBPortStatTable.setStatus('mandatory')
cdx6500HUBPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1), ).setIndexNames((0, "HUB-OPT-MIB", "cdx6500HUBStatPortNumber"))
if mibBuilder.loadTexts: cdx6500HUBPortStatEntry.setStatus('mandatory')
cdx6500HUBStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(13, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500HUBStatPortNumber.setStatus('mandatory')
cdx6500HUBPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500HUBPortStatus.setStatus('mandatory')
cdx6500HUBPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500HUBPortState.setStatus('mandatory')
cdx6500HUBPortLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reduced", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500HUBPortLevel.setStatus('mandatory')
cdx6500HUBPortPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 23, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonInverted", 1), ("inverted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500HUBPortPolarity.setStatus('mandatory')
mibBuilder.exportSymbols("HUB-OPT-MIB", cdx6500Configuration=cdx6500Configuration, cdx6500HUBCfgPortLevel=cdx6500HUBCfgPortLevel, cdx6500HUBCfgPortNumber=cdx6500HUBCfgPortNumber, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500HUBPortStatEntry=cdx6500HUBPortStatEntry, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500HUBPortLevel=cdx6500HUBPortLevel, codex=codex, cdx6500HUBPortStatus=cdx6500HUBPortStatus, cdx6500HUBPortState=cdx6500HUBPortState, cdx6500Statistics=cdx6500Statistics, cdxProductSpecific=cdxProductSpecific, cdx6500=cdx6500, cdx6500Controls=cdx6500Controls, cdx6500HUBPortPolarity=cdx6500HUBPortPolarity, cdx6500PPSTHUBPortStatTable=cdx6500PPSTHUBPortStatTable, DisplayString=DisplayString, cdx6500PPCTHUBPortEntry=cdx6500PPCTHUBPortEntry, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500PPCTHUBPortTable=cdx6500PPCTHUBPortTable, cdx6500HUBStatPortNumber=cdx6500HUBStatPortNumber)
