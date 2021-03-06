#
# PySNMP MIB module NOKIA-COMMON-MIB-OID-REGISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-COMMON-MIB-OID-REGISTRATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ntcCommon, = mibBuilder.importSymbols("NOKIA-OID-REGISTRATION-MIB", "ntcCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, iso, Unsigned32, MibIdentifier, Gauge32, NotificationType, TimeTicks, Integer32, ModuleIdentity, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "iso", "Unsigned32", "MibIdentifier", "Gauge32", "NotificationType", "TimeTicks", "Integer32", "ModuleIdentity", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcCommonAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 1))
ntcCommonAlarmTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 2))
ntcCommonTrapDest = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 3))
ntcRS = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 4))
ntcCommonModules = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 5))
ntcCommonAgentCaps = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 6))
ntcCommonMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7))
ntcCommonReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8))
ntcHWModule = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 1))
ntcNtpModule = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 2))
ntcHWUnitTypeModule = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 3))
ntcACModule = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 4))
ntcGprsTracingModule = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 5))
ntcHWAgentCap = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 1))
ntcNtpAgentCap = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 2))
ntcHWUnitTypeAgentCap = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 3))
ntcACAgentCap = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 4))
ntcGprsTracingAgentCap = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 5))
ntcHWMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1))
ntcNtpMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2))
ntcHWUnitTypeMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3))
ntcACMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 4))
ntcGprsTracingMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 5))
ntcHWReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1))
ntcNtpReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2))
ntcHWUnitTypeReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 3))
ntcACReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 4))
ntcGprsTracingReqs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 5))
mibBuilder.exportSymbols("NOKIA-COMMON-MIB-OID-REGISTRATION-MIB", ntcCommonModules=ntcCommonModules, ntcHWUnitTypeReqs=ntcHWUnitTypeReqs, ntcCommonTrapDest=ntcCommonTrapDest, ntcHWMibs=ntcHWMibs, ntcNtpMibs=ntcNtpMibs, ntcGprsTracingModule=ntcGprsTracingModule, ntcCommonAgentCaps=ntcCommonAgentCaps, ntcACAgentCap=ntcACAgentCap, ntcACReqs=ntcACReqs, ntcHWModule=ntcHWModule, ntcACModule=ntcACModule, ntcNtpAgentCap=ntcNtpAgentCap, ntcNtpReqs=ntcNtpReqs, ntcCommonReqs=ntcCommonReqs, ntcHWAgentCap=ntcHWAgentCap, ntcCommonAlarm=ntcCommonAlarm, ntcCommonMibs=ntcCommonMibs, ntcGprsTracingReqs=ntcGprsTracingReqs, ntcCommonAlarmTrap=ntcCommonAlarmTrap, ntcACMibs=ntcACMibs, ntcHWUnitTypeModule=ntcHWUnitTypeModule, ntcHWUnitTypeAgentCap=ntcHWUnitTypeAgentCap, ntcRS=ntcRS, ntcGprsTracingAgentCap=ntcGprsTracingAgentCap, ntcGprsTracingMibs=ntcGprsTracingMibs, ntcHWUnitTypeMibs=ntcHWUnitTypeMibs, ntcNtpModule=ntcNtpModule, ntcHWReqs=ntcHWReqs)
