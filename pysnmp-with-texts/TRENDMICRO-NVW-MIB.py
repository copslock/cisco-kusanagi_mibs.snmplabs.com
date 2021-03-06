#
# PySNMP MIB module TRENDMICRO-NVW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRENDMICRO-NVW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, MibIdentifier, Counter32, IpAddress, Bits, NotificationType, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "MibIdentifier", "Counter32", "IpAddress", "Bits", "NotificationType", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tmNVW, = mibBuilder.importSymbols("TRENDMICRO-SMI", "tmNVW")
nvwScanCurrConn = MibScalar((1, 3, 6, 1, 4, 1, 6101, 2500, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvwScanCurrConn.setStatus('mandatory')
if mibBuilder.loadTexts: nvwScanCurrConn.setDescription('Concurrent scan connections (NVE)')
nvwScanCurrMem = MibScalar((1, 3, 6, 1, 4, 1, 6101, 2500, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvwScanCurrMem.setStatus('mandatory')
if mibBuilder.loadTexts: nvwScanCurrMem.setDescription('Current scan memory usage (NVE)')
nvwPolicyCurrConn = MibScalar((1, 3, 6, 1, 4, 1, 6101, 2500, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvwPolicyCurrConn.setStatus('mandatory')
if mibBuilder.loadTexts: nvwPolicyCurrConn.setDescription('Concurrent number of user (Policy Enforcer).')
nvwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6101, 2500, 251))
oppOn = NotificationType((1, 3, 6, 1, 4, 1, 6101, 2500, 251, 1))
if mibBuilder.loadTexts: oppOn.setStatus('current')
if mibBuilder.loadTexts: oppOn.setDescription('')
oppOff = NotificationType((1, 3, 6, 1, 4, 1, 6101, 2500, 251, 2))
if mibBuilder.loadTexts: oppOff.setStatus('current')
if mibBuilder.loadTexts: oppOff.setDescription('')
bootFactory = NotificationType((1, 3, 6, 1, 4, 1, 6101, 2500, 251, 3))
if mibBuilder.loadTexts: bootFactory.setStatus('current')
if mibBuilder.loadTexts: bootFactory.setDescription('Boot to factory default partition.')
bootPrevious = NotificationType((1, 3, 6, 1, 4, 1, 6101, 2500, 251, 4))
if mibBuilder.loadTexts: bootPrevious.setStatus('current')
if mibBuilder.loadTexts: bootPrevious.setDescription('Boot to previous partition.')
haFailover = NotificationType((1, 3, 6, 1, 4, 1, 6101, 2500, 251, 5))
if mibBuilder.loadTexts: haFailover.setStatus('current')
if mibBuilder.loadTexts: haFailover.setDescription('HA role changed.')
mibBuilder.exportSymbols("TRENDMICRO-NVW-MIB", nvwScanCurrConn=nvwScanCurrConn, bootFactory=bootFactory, haFailover=haFailover, bootPrevious=bootPrevious, nvwTraps=nvwTraps, oppOff=oppOff, oppOn=oppOn, nvwPolicyCurrConn=nvwPolicyCurrConn, nvwScanCurrMem=nvwScanCurrMem)
