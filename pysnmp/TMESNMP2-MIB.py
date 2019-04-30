#
# PySNMP MIB module TMESNMP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TMESNMP2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
tme, = mibBuilder.importSymbols("Papouch-SMI", "tme")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ModuleIdentity, iso, Gauge32, NotificationType, ObjectIdentity, IpAddress, Bits, Integer32, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ModuleIdentity", "iso", "Gauge32", "NotificationType", "ObjectIdentity", "IpAddress", "Bits", "Integer32", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vars = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 1, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 1, 2))
int_temperature = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: int_temperature.setStatus('current')
string_temperature = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: string_temperature.setStatus('current')
device_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: device_name.setStatus('current')
int_temperature_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: int_temperature_t.setStatus('current')
string_temperature_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: string_temperature_t.setStatus('current')
device_name_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: device_name_t.setStatus('current')
warning_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: warning_t.setStatus('current')
mibBuilder.exportSymbols("TMESNMP2-MIB", warning_t=warning_t, string_temperature=string_temperature, traps=traps, string_temperature_t=string_temperature_t, vars=vars, device_name_t=device_name_t, int_temperature=int_temperature, int_temperature_t=int_temperature_t, device_name=device_name)