#
# PySNMP MIB module CPQGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQGEN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
enterprises, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, NotificationType, ModuleIdentity, Gauge32, iso, TimeTicks, Counter32, NotificationType, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Counter32", "NotificationType", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
cpqGenUnreg = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151))
cpqGenComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151, 2))
cpqTrapVarBind = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151, 2, 2))
cpqGenEntOIDStr = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqGenEntOIDStr.setStatus('mandatory')
if mibBuilder.loadTexts: cpqGenEntOIDStr.setDescription('Enterprise OID String.')
cpqGenTrapID = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqGenTrapID.setStatus('mandatory')
if mibBuilder.loadTexts: cpqGenTrapID.setDescription('Generic Trap ID.')
cpqSpecTrapID = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSpecTrapID.setStatus('mandatory')
if mibBuilder.loadTexts: cpqSpecTrapID.setDescription('Specific Trap ID.')
cpqGenericUnregistered = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,99999)).setObjects(("CPQGEN-MIB", "cpqGenEntOIDStr"), ("CPQGEN-MIB", "cpqGenTrapID"), ("CPQGEN-MIB", "cpqSpecTrapID"))
if mibBuilder.loadTexts: cpqGenericUnregistered.setDescription('A genericUnregistered trap signifies that a system has sent a trap to the management server for a MIB that has not yet been compiled. Try compiling any MIBs from the vendor for this system to obtain additional information. See Details for more information.')
mibBuilder.exportSymbols("CPQGEN-MIB", cpqGenericUnregistered=cpqGenericUnregistered, cpqGenTrapID=cpqGenTrapID, cpqGenUnreg=cpqGenUnreg, cpqGenEntOIDStr=cpqGenEntOIDStr, cpqSpecTrapID=cpqSpecTrapID, cpqGenComponent=cpqGenComponent, cpqTrapVarBind=cpqTrapVarBind, compaq=compaq)
