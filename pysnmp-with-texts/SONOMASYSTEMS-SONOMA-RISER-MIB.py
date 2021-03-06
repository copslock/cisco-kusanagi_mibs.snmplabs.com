#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-RISER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-RISER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, iso, TimeTicks, Bits, ObjectIdentity, ModuleIdentity, IpAddress, Counter32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "iso", "TimeTicks", "Bits", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonomaSeries, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaSeries")
sonomaRiser = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 12))
riserFanTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1), )
if mibBuilder.loadTexts: riserFanTable.setStatus('mandatory')
if mibBuilder.loadTexts: riserFanTable.setDescription('A table that records the status of all fans in the chassis. This is a read only table. SNMP management application cannot add or remove any rows. The number of rows in this table is determined by the number of fans installed in the chassis.')
riserFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-RISER-MIB", "riserFanIndex"))
if mibBuilder.loadTexts: riserFanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: riserFanEntry.setDescription('A list of information for each fan.')
riserFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: riserFanIndex.setStatus('mandatory')
if mibBuilder.loadTexts: riserFanIndex.setDescription('The value of this object uniquely identifies the fan in a device chassis.')
riserFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: riserFanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: riserFanStatus.setDescription('Status of the fan: ok(1) if no problems, fail(2) if something is wrong with the fan.')
thermalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 12, 2))
riserTemperatureC = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 12, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: riserTemperatureC.setStatus('mandatory')
if mibBuilder.loadTexts: riserTemperatureC.setDescription('This object is the system temperature measured in Celsius.')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-RISER-MIB", thermalGroup=thermalGroup, riserFanIndex=riserFanIndex, riserFanStatus=riserFanStatus, riserTemperatureC=riserTemperatureC, riserFanEntry=riserFanEntry, riserFanTable=riserFanTable, sonomaRiser=sonomaRiser)
