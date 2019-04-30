#
# PySNMP MIB module DNOS-POWER-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-POWER-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
pethMainPseEntry, pethPsePortEntry = mibBuilder.importSymbols("POWER-ETHERNET-MIB", "pethMainPseEntry", "pethPsePortEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, iso, MibIdentifier, Gauge32, Integer32, Counter64, ObjectIdentity, TimeTicks, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "iso", "MibIdentifier", "Gauge32", "Integer32", "Counter64", "ObjectIdentity", "TimeTicks", "NotificationType", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
fastPathpowerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15))
fastPathpowerEthernetMIB.setRevisions(('2016-09-26 20:00', '2007-08-19 12:00', '2007-05-23 00:00', '2003-11-10 12:00',))
if mibBuilder.loadTexts: fastPathpowerEthernetMIB.setLastUpdated('200708191200Z')
if mibBuilder.loadTexts: fastPathpowerEthernetMIB.setOrganization('Broadcom Corporation')
agentPethObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1))
agentPethPsePortTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1), )
if mibBuilder.loadTexts: agentPethPsePortTable.setStatus('current')
agentPethPsePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1), )
pethPsePortEntry.registerAugmentions(("DNOS-POWER-ETHERNET-MIB", "agentPethPsePortEntry"))
agentPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
if mibBuilder.loadTexts: agentPethPsePortEntry.setStatus('current')
agentPethPowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 1), Gauge32()).setUnits('Milliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethPowerLimit.setStatus('current')
agentPethOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 2), Gauge32()).setUnits('Milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPethOutputPower.setStatus('current')
agentPethOutputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 3), Gauge32()).setUnits('Milliamps').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPethOutputCurrent.setStatus('current')
agentPethOutputVolts = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 4), Gauge32()).setUnits('Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPethOutputVolts.setStatus('current')
agentPethTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 5), Gauge32()).setUnits('DEGREES').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPethTemperature.setStatus('current')
agentPethPowerLimitType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot3af", 1), ("user", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethPowerLimitType.setStatus('current')
agentPethHighPowerEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethHighPowerEnable.setStatus('current')
agentPethPowerDetectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("legacy", 1), ("fourPtdot3afonly", 2), ("fourPtdot3afandlegacy", 3), ("twoPtdot3afonly", 4), ("twoPtdot3afandlegacy", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethPowerDetectionType.setStatus('current')
agentPethFaultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("mpsAbsent", 1), ("short", 2), ("overload", 3), ("powerDenied", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPethFaultStatus.setStatus('current')
agentPethPortReset = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethPortReset.setStatus('current')
agentPethMainPseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2))
agentPethMainPseTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2, 1), )
if mibBuilder.loadTexts: agentPethMainPseTable.setStatus('current')
agentPethMainPseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2, 1, 1), )
pethMainPseEntry.registerAugmentions(("DNOS-POWER-ETHERNET-MIB", "agentPethMainPseEntry"))
agentPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
if mibBuilder.loadTexts: agentPethMainPseEntry.setStatus('current')
agentPethMainPseLegacy = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethMainPseLegacy.setStatus('current')
agentPethPseTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3), )
if mibBuilder.loadTexts: agentPethPseTable.setStatus('current')
agentPethPseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3, 1), )
pethMainPseEntry.registerAugmentions(("DNOS-POWER-ETHERNET-MIB", "agentPethPseEntry"))
agentPethPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
if mibBuilder.loadTexts: agentPethPseEntry.setStatus('current')
agentPethPsePowerManagementMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("dynamic", 1), ("static", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethPsePowerManagementMode.setStatus('current')
agentPethPseAutoResetEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 15, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentPethPseAutoResetEnable.setStatus('current')
mibBuilder.exportSymbols("DNOS-POWER-ETHERNET-MIB", PYSNMP_MODULE_ID=fastPathpowerEthernetMIB, agentPethMainPseObjects=agentPethMainPseObjects, agentPethPseTable=agentPethPseTable, agentPethTemperature=agentPethTemperature, agentPethPortReset=agentPethPortReset, agentPethPsePortTable=agentPethPsePortTable, agentPethMainPseEntry=agentPethMainPseEntry, agentPethPseEntry=agentPethPseEntry, agentPethPowerLimit=agentPethPowerLimit, agentPethPowerDetectionType=agentPethPowerDetectionType, agentPethMainPseTable=agentPethMainPseTable, agentPethMainPseLegacy=agentPethMainPseLegacy, agentPethPseAutoResetEnable=agentPethPseAutoResetEnable, agentPethOutputCurrent=agentPethOutputCurrent, agentPethObjects=agentPethObjects, agentPethFaultStatus=agentPethFaultStatus, agentPethHighPowerEnable=agentPethHighPowerEnable, agentPethPsePowerManagementMode=agentPethPsePowerManagementMode, fastPathpowerEthernetMIB=fastPathpowerEthernetMIB, agentPethPowerLimitType=agentPethPowerLimitType, agentPethPsePortEntry=agentPethPsePortEntry, agentPethOutputVolts=agentPethOutputVolts, agentPethOutputPower=agentPethOutputPower)