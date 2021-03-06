#
# PySNMP MIB module ARISTA-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Gauge32, Integer32, ModuleIdentity, Counter32, Counter64, Bits, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Gauge32", "Integer32", "ModuleIdentity", "Counter32", "Counter64", "Bits", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 15))
aristaIfMIB.setRevisions(('2014-10-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaIfMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: aristaIfMIB.setLastUpdated('201410090000Z')
if mibBuilder.loadTexts: aristaIfMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaIfMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaIfMIB.setDescription('The MIB module for reporting additional interface statistics on Arista devices.')
aristaIf = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1))
aristaIfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1), )
if mibBuilder.loadTexts: aristaIfTable.setStatus('current')
if mibBuilder.loadTexts: aristaIfTable.setDescription('This table contains additional interface statistics not contained in the IF-MIB.')
aristaIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: aristaIfEntry.setStatus('current')
if mibBuilder.loadTexts: aristaIfEntry.setDescription('An entry containing statistics for a given interface.')
aristaIfCounterLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfCounterLastUpdated.setStatus('current')
if mibBuilder.loadTexts: aristaIfCounterLastUpdated.setDescription('The value of sysUpTime at which the counters in the ifTable and ifXTable were sampled from the hardware.')
aristaIfRateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfRateInterval.setStatus('current')
if mibBuilder.loadTexts: aristaIfRateInterval.setDescription('The amount of time over which the aristaIf*Rate values are averaged for this interface.')
aristaIfInPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInPktRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfInPktRate.setDescription('The rate, in packets per second, of packets inbound on this interface, averaged over aristaIfRateInterval.')
aristaIfOutPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOutPktRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfOutPktRate.setDescription('The rate, in packets per second, of packets outbound on this interface, averaged over aristaIfRateInterval.')
aristaIfInOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfInOctetRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfInOctetRate.setDescription('The rate, in octets per second, of data inbound on this interface, averaged over aristaIfRateInterval.')
aristaIfOutOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 6), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOutOctetRate.setStatus('current')
if mibBuilder.loadTexts: aristaIfOutOctetRate.setDescription('The rate, in octets per second, of data inbound on this interface, averaged over aristaIfRateInterval.')
aristaIfRatesLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfRatesLastUpdated.setStatus('current')
if mibBuilder.loadTexts: aristaIfRatesLastUpdated.setDescription('The value of sysUpTime at which the aristaIf*Rate gauges were last calculated.')
aristaIfOperStatusChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 15, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaIfOperStatusChanges.setStatus('current')
if mibBuilder.loadTexts: aristaIfOperStatusChanges.setDescription('The number of times since system boot that ifOperStatus has changed.')
aristaIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2))
aristaIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1))
aristaIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2))
aristaIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 2, 1)).setObjects(("ARISTA-IF-MIB", "aristaIfAdditionalInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaIfCompliance = aristaIfCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaIfCompliance.setDescription('The compliance statement for Arista devices that implement the IF-MIB')
aristaIfAdditionalInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 15, 2, 1, 1)).setObjects(("ARISTA-IF-MIB", "aristaIfCounterLastUpdated"), ("ARISTA-IF-MIB", "aristaIfRateInterval"), ("ARISTA-IF-MIB", "aristaIfInPktRate"), ("ARISTA-IF-MIB", "aristaIfOutPktRate"), ("ARISTA-IF-MIB", "aristaIfInOctetRate"), ("ARISTA-IF-MIB", "aristaIfOutOctetRate"), ("ARISTA-IF-MIB", "aristaIfRatesLastUpdated"), ("ARISTA-IF-MIB", "aristaIfOperStatusChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaIfAdditionalInformationGroup = aristaIfAdditionalInformationGroup.setStatus('current')
if mibBuilder.loadTexts: aristaIfAdditionalInformationGroup.setDescription('A collection of objects providing additional information above and beyond what the IF-MIB provides, applicable to all network interfaces.')
mibBuilder.exportSymbols("ARISTA-IF-MIB", aristaIfRatesLastUpdated=aristaIfRatesLastUpdated, aristaIfRateInterval=aristaIfRateInterval, aristaIfInPktRate=aristaIfInPktRate, aristaIfEntry=aristaIfEntry, aristaIfConformance=aristaIfConformance, aristaIfCounterLastUpdated=aristaIfCounterLastUpdated, aristaIfCompliance=aristaIfCompliance, aristaIfCompliances=aristaIfCompliances, aristaIfGroups=aristaIfGroups, aristaIfTable=aristaIfTable, aristaIfOperStatusChanges=aristaIfOperStatusChanges, aristaIf=aristaIf, aristaIfOutPktRate=aristaIfOutPktRate, aristaIfMIB=aristaIfMIB, PYSNMP_MODULE_ID=aristaIfMIB, aristaIfOutOctetRate=aristaIfOutOctetRate, aristaIfInOctetRate=aristaIfInOctetRate, aristaIfAdditionalInformationGroup=aristaIfAdditionalInformationGroup)
