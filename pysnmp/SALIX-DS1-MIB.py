#
# PySNMP MIB module SALIX-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
atmfM4TrapAlarmSeverity, = mibBuilder.importSymbols("ATM-FORUM-M4-MIB", "atmfM4TrapAlarmSeverity")
dsx1ConfigEntry, = mibBuilder.importSymbols("DS1-MIB", "dsx1ConfigEntry")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
DateAndTime, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "DateAndTime")
salixGeneric, = mibBuilder.importSymbols("SALIX-MIB", "salixGeneric")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, TimeTicks, Counter32, Gauge32, ObjectIdentity, Counter64, iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
salixDsx1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 2, 7))
if mibBuilder.loadTexts: salixDsx1MIB.setLastUpdated('9907080000Z')
if mibBuilder.loadTexts: salixDsx1MIB.setOrganization('SALIX Technologies')
salixDsx1MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1))
salixDsx1MIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 7, 2))
salixDsx1MIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 7, 3))
salixDsx1MIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 7, 2, 0))
salixDsx1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1), )
if mibBuilder.loadTexts: salixDsx1ConfigTable.setStatus('current')
salixDsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1), )
dsx1ConfigEntry.registerAugmentions(("SALIX-DS1-MIB", "salixDsx1ConfigEntry"))
salixDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: salixDsx1ConfigEntry.setStatus('current')
salixDsx1ContinuityTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopback", 1), ("transponder", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDsx1ContinuityTestType.setStatus('current')
salixDsx1DChannelPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDsx1DChannelPresent.setStatus('current')
salixDsx1AutoInitiateState = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDsx1AutoInitiateState.setStatus('current')
salixDsx1DChannelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("userMode", 1), ("networkMode", 2))).clone('userMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDsx1DChannelMode.setStatus('current')
salixDsx1RobbedBitSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("onHook", 1), ("offHook", 2), ("ringing", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDsx1RobbedBitSignalling.setStatus('current')
salixDsx1TDMEchoCancellation = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("echoCancel16ms", 1), ("echoCancel32ms", 2), ("echoCancel63ms", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixDsx1TDMEchoCancellation.setStatus('current')
salixDs1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 1))
salixDs1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 2))
salixDs1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 1, 1)).setObjects(("SALIX-DS1-MIB", "salixDsx1ContinuityTestType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixDs1Group = salixDs1Group.setStatus('current')
salixDs1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 2, 1)).setObjects(("SALIX-DS1-MIB", "salixDs1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixDs1Compliance = salixDs1Compliance.setStatus('current')
mibBuilder.exportSymbols("SALIX-DS1-MIB", salixDs1Compliances=salixDs1Compliances, salixDsx1MIBObjects=salixDsx1MIBObjects, PYSNMP_MODULE_ID=salixDsx1MIB, salixDsx1MIBTraps=salixDsx1MIBTraps, salixDsx1DChannelMode=salixDsx1DChannelMode, salixDsx1MIB=salixDsx1MIB, salixDsx1MIBTrapPrefix=salixDsx1MIBTrapPrefix, salixDsx1TDMEchoCancellation=salixDsx1TDMEchoCancellation, salixDs1Groups=salixDs1Groups, salixDs1Compliance=salixDs1Compliance, salixDs1Group=salixDs1Group, salixDsx1ConfigEntry=salixDsx1ConfigEntry, salixDsx1RobbedBitSignalling=salixDsx1RobbedBitSignalling, salixDsx1MIBCompliance=salixDsx1MIBCompliance, salixDsx1AutoInitiateState=salixDsx1AutoInitiateState, salixDsx1DChannelPresent=salixDsx1DChannelPresent, salixDsx1ContinuityTestType=salixDsx1ContinuityTestType, salixDsx1ConfigTable=salixDsx1ConfigTable)
