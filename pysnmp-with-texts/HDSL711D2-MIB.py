#
# PySNMP MIB module HDSL711D2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HDSL711D2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hdsl711D2, = mibBuilder.importSymbols("GDCHDSL-MIB", "hdsl711D2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, TimeTicks, ModuleIdentity, Integer32, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hdsl711D2System = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 1))
hdsl711D2Version = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 1, 1))
gdc711D2SystemMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 11, 30, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdc711D2SystemMIBversion.setStatus('mandatory')
if mibBuilder.loadTexts: gdc711D2SystemMIBversion.setDescription("Identifies the version of the MIB. The format of the version is x.yzT, where 'x' identifies the major revision number, 'y' identifies the minor revision number, 'z' identifies the typographical revision, and T identifies the test revision. Acceptable values for the individual revision components are as follows: x: 1 - 9 y: 0 - 9 z: 0 - 9 T: A - Z Upon formal release, no designation for the test revision will be present.")
hdsl711D2Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2))
hdsl711D2NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 1))
hdsl711D2DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 2))
hdsl711D2PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 3))
hdsl711D2UnitFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 4))
hdsl711D2ChecksumCorrupt = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 5))
hdsl711D2LossofSignal = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 6))
hdsl711D2UnavailableSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 7))
hdsl711D2ErrorSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 8))
hdsl711D2LossofSyncWord = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 9))
hdsl711D2MajorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 10))
hdsl711D2MinorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 30, 2, 11))
mibBuilder.exportSymbols("HDSL711D2-MIB", hdsl711D2UnitFailure=hdsl711D2UnitFailure, hdsl711D2LossofSignal=hdsl711D2LossofSignal, hdsl711D2System=hdsl711D2System, hdsl711D2PowerUpAlm=hdsl711D2PowerUpAlm, hdsl711D2Alarms=hdsl711D2Alarms, hdsl711D2MajorBER=hdsl711D2MajorBER, hdsl711D2ChecksumCorrupt=hdsl711D2ChecksumCorrupt, hdsl711D2LossofSyncWord=hdsl711D2LossofSyncWord, hdsl711D2ErrorSec=hdsl711D2ErrorSec, hdsl711D2UnavailableSec=hdsl711D2UnavailableSec, gdc711D2SystemMIBversion=gdc711D2SystemMIBversion, hdsl711D2MinorBER=hdsl711D2MinorBER, hdsl711D2DiagRxErrAlm=hdsl711D2DiagRxErrAlm, hdsl711D2Version=hdsl711D2Version, hdsl711D2NoResponseAlm=hdsl711D2NoResponseAlm)
