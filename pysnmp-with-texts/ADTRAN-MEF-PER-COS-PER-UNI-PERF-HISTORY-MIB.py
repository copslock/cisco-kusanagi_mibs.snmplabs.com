#
# PySNMP MIB module ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:14:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
HCPerfInvalidIntervals, HCPerfTotalCount, HCPerfValidIntervals, HCPerfTimeElapsed, HCPerfIntervalCount, HCPerfCurrentCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfInvalidIntervals", "HCPerfTotalCount", "HCPerfValidIntervals", "HCPerfTimeElapsed", "HCPerfIntervalCount", "HCPerfCurrentCount")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Gauge32, Counter32, Bits, TimeTicks, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, Unsigned32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Counter32", "Bits", "TimeTicks", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "Unsigned32", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAosMefPerCosPerUniPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 2))
adGenAosMefPerCosPerUniPerfHistoryMib.setRevisions(('2014-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryMib.setOrganization('ADTRAN Inc.')
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryMib.setContactInfo('Info: www.adtran.com Postal: ADTRAN, Inc. 901 Explorer Blvd. Huntsville, AL 35806 Tel: +1 888 423-8726 E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryMib.setDescription('This MIB module defines high capacity performance statistics per COS per UNI within an AOS product. Copyright (C) ADTRAN, Inc. (2014).')
adGenAosMefPerCosPerUniPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2))
adMefPerCosPerUniPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1), )
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTable.setDescription('This table contains current performance history information that has been recorded since the last 15 minute interval ended and from when the last 1 day interval ended. This table is indexed by ifIndex and adMefPerCosPerUniPhCurQueueNumber.')
adMefPerCosPerUniPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurQueueNumber"))
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEntry.setDescription("This specifies the information contained in one entry of the adMefPerCosPerUniPhCurTable. It is indexed by an interface's ifIndex, and the queue number.")
adMefPerCosPerUniPhCurQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurQueueNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurQueueNumber.setDescription('UNI Interface queue number.')
adMefPerCosPerUniPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 2), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTimeElapsed15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTimeElapsed15Min.setDescription('Total elapsed seconds in the current 15 minute interval.')
adMefPerCosPerUniPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 3), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurValidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurValidIntervals15Min.setDescription('Number of valid 15 minute intervals over the last 24 hours.')
adMefPerCosPerUniPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 4), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurInvalidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurInvalidIntervals15Min.setDescription('Number of invalid 15 minute intervals over the last 24 hours.')
adMefPerCosPerUniPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctets15Min.setDescription('Count of ingress green octets in the current 15 minute interval.')
adMefPerCosPerUniPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrames15Min.setDescription('Count of ingress green frames in the current 15 minute interval.')
adMefPerCosPerUniPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctets15Min.setDescription('Count of egress green frames in the current 15 minute interval.')
adMefPerCosPerUniPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrames15Min.setDescription('Count of egress green frames in the current 15 minute interval.')
adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min.setDescription('Count of ingress green frames discarded in the current 15 minute interval.')
adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min.setDescription('Count of egress green frames discarded in the current 15 minute interval.')
adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min.setDescription('Count of ingress green octets discarded in the current 15 minute interval.')
adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min.setDescription('Count of egress green octets discarded in the current 15 minute interval.')
adMefPerCosPerUniPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 13), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTimeElapsed1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTimeElapsed1Day.setDescription('Total elapsed seconds in the current 1 day interval.')
adMefPerCosPerUniPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 14), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurValidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurValidIntervals1Day.setDescription('Number of valid 1 day intervals available.')
adMefPerCosPerUniPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 15), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurInvalidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurInvalidIntervals1Day.setDescription('Number of invalid 1 day intervals available.')
adMefPerCosPerUniPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctets1Day.setDescription('Count of ingress green octets in the current 1 day interval.')
adMefPerCosPerUniPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrames1Day.setDescription('Count of ingress green frames in the current 1 day interval.')
adMefPerCosPerUniPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctets1Day.setDescription('Count of egress green octets in the current 1 day interval.')
adMefPerCosPerUniPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrames1Day.setDescription('Count of egress green frames in the current 1 day interval.')
adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day.setDescription('Count of ingress green frames discarded in the current 1 day interval.')
adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day.setDescription('Count of egress green frames discarded in the current 1 day interval.')
adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day.setDescription('Count of ingress green octets discarded in the current 1 day interval.')
adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day.setDescription('Count of egress green octets discarded in the current 1 day interval.')
adMefPerCosPerUniPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2), )
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalTable.setDescription('This table contains performance history information for each valid 15 minute interval. This table is indexed by ifIndex, the queue number, and the interval number.')
adMefPerCosPerUniPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalEntry.setDescription('An entry in the adMefPerCosPerUniPh15MinIntervalTable.')
adMefPerCosPerUniPh15MinQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinQueueNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinQueueNumber.setDescription('UNI Interface queue number.')
adMefPerCosPerUniPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalNumber.setDescription('Performance history interval number. Interval 1 is the most recent previous interval; interval 96 is 24 hours ago. Intervals 2..96 are optional.')
adMefPerCosPerUniPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenOctets.setDescription('Count of ingress green octets in the 15 minute interval.')
adMefPerCosPerUniPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenFrames.setDescription('Count of ingress green frames in the 15 minute interval.')
adMefPerCosPerUniPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenOctets.setDescription('Count of egress green octets in the 15 minute interval.')
adMefPerCosPerUniPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenFrames.setDescription('Count of egress green frames in the 15 minute interval.')
adMefPerCosPerUniPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 15 minute interval.')
adMefPerCosPerUniPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 15 minute interval.')
adMefPerCosPerUniPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenOctetDiscards.setDescription('Count of ingress green octets discarded in the 15 minute interval.')
adMefPerCosPerUniPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 15 minute interval.')
adMefPerCosPerUniPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3), )
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalTable.setDescription('This table contains performance history information for each valid 1 day interval. This table is indexed by by ifIndex, the queue number, and the interval number.')
adMefPerCosPerUniPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalEntry.setDescription('An entry in the adMefPerCosPerUniPh1DayIntervalTable.')
adMefPerCosPerUniPh1DayQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayQueueNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayQueueNumber.setDescription('UNI Interface queue number.')
adMefPerCosPerUniPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalNumber.setDescription('Performance history interval number. Interval 1 is the most recent previous day; interval 7 is 7 days ago. Intervals 2..30 are optional.')
adMefPerCosPerUniPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenOctets.setDescription('Count of ingress green octets in the 1 day interval.')
adMefPerCosPerUniPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenFrames.setDescription('Count of ingress green frames in the 1 day interval.')
adMefPerCosPerUniPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenOctets.setDescription('Count of egress green octets in the 1 day interval.')
adMefPerCosPerUniPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenFrames.setDescription('Count of egress green frames in the 1 day interval.')
adMefPerCosPerUniPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 1 day interval.')
adMefPerCosPerUniPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 1 day interval.')
adMefPerCosPerUniPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenOctetDiscards.setDescription('Count of ingress green octets discarded in the 1 day interval.')
adMefPerCosPerUniPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 1 day interval.')
adGenAosMefPerCosPerUniPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21))
adGenAosMefPerCosPerUniPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1))
adGenAosMefPerCosPerUniPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 2))
adGenAosMefPerCosPerUniPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 2, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurGroup"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerCosPerUniPerfHistoryCompliance = adGenAosMefPerCosPerUniPerfHistoryCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryCompliance.setDescription('The compliance statement for SNMPv2 entities which implement UNI interface per-queue performance history.')
adMefPerCosPerUniPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerUniPhCurGroup = adMefPerCosPerUniPhCurGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurGroup.setDescription('The Current Group.')
adMefPerCosPerUniPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 2)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerUniPh15MinIntervalGroup = adMefPerCosPerUniPh15MinIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalGroup.setDescription('The 15 minute interval group.')
adMefPerCosPerUniPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 3)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerUniPh1DayIntervalGroup = adMefPerCosPerUniPh1DayIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalGroup.setDescription('The 1 day interval group.')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", adMefPerCosPerUniPh15MinEgressGreenOctetDiscards=adMefPerCosPerUniPh15MinEgressGreenOctetDiscards, adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day=adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day, adMefPerCosPerUniPhCurIngressGreenOctets1Day=adMefPerCosPerUniPhCurIngressGreenOctets1Day, adMefPerCosPerUniPhCurGroup=adMefPerCosPerUniPhCurGroup, adMefPerCosPerUniPh15MinIntervalGroup=adMefPerCosPerUniPh15MinIntervalGroup, adMefPerCosPerUniPhCurEgressGreenOctets15Min=adMefPerCosPerUniPhCurEgressGreenOctets15Min, adMefPerCosPerUniPh1DayIngressGreenOctetDiscards=adMefPerCosPerUniPh1DayIngressGreenOctetDiscards, adMefPerCosPerUniPh15MinIngressGreenFrameDiscards=adMefPerCosPerUniPh15MinIngressGreenFrameDiscards, adMefPerCosPerUniPh15MinIntervalTable=adMefPerCosPerUniPh15MinIntervalTable, adMefPerCosPerUniPh1DayQueueNumber=adMefPerCosPerUniPh1DayQueueNumber, adMefPerCosPerUniPhCurValidIntervals1Day=adMefPerCosPerUniPhCurValidIntervals1Day, adGenAosMefPerCosPerUniPerfHistoryCompliance=adGenAosMefPerCosPerUniPerfHistoryCompliance, adMefPerCosPerUniPhCurEgressGreenFrames15Min=adMefPerCosPerUniPhCurEgressGreenFrames15Min, adMefPerCosPerUniPhCurTimeElapsed1Day=adMefPerCosPerUniPhCurTimeElapsed1Day, adMefPerCosPerUniPhCurValidIntervals15Min=adMefPerCosPerUniPhCurValidIntervals15Min, adMefPerCosPerUniPh1DayEgressGreenOctets=adMefPerCosPerUniPh1DayEgressGreenOctets, adMefPerCosPerUniPh1DayIntervalEntry=adMefPerCosPerUniPh1DayIntervalEntry, adMefPerCosPerUniPh1DayEgressGreenFrameDiscards=adMefPerCosPerUniPh1DayEgressGreenFrameDiscards, adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day=adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day, adGenAosMefPerCosPerUniPerfHistory=adGenAosMefPerCosPerUniPerfHistory, adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day=adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day, adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min=adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min, adMefPerCosPerUniPh15MinIngressGreenOctetDiscards=adMefPerCosPerUniPh15MinIngressGreenOctetDiscards, adMefPerCosPerUniPhCurIngressGreenFrames1Day=adMefPerCosPerUniPhCurIngressGreenFrames1Day, adMefPerCosPerUniPhCurEntry=adMefPerCosPerUniPhCurEntry, adMefPerCosPerUniPh1DayIntervalNumber=adMefPerCosPerUniPh1DayIntervalNumber, adGenAosMefPerCosPerUniPerfHistoryGroups=adGenAosMefPerCosPerUniPerfHistoryGroups, adMefPerCosPerUniPhCurEgressGreenFrames1Day=adMefPerCosPerUniPhCurEgressGreenFrames1Day, adMefPerCosPerUniPh1DayIntervalGroup=adMefPerCosPerUniPh1DayIntervalGroup, adMefPerCosPerUniPh15MinIntervalNumber=adMefPerCosPerUniPh15MinIntervalNumber, adMefPerCosPerUniPh15MinQueueNumber=adMefPerCosPerUniPh15MinQueueNumber, adGenAosMefPerCosPerUniPerfHistoryConformance=adGenAosMefPerCosPerUniPerfHistoryConformance, adMefPerCosPerUniPh15MinIngressGreenOctets=adMefPerCosPerUniPh15MinIngressGreenOctets, adMefPerCosPerUniPhCurEgressGreenOctets1Day=adMefPerCosPerUniPhCurEgressGreenOctets1Day, adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day=adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day, adMefPerCosPerUniPhCurTable=adMefPerCosPerUniPhCurTable, adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min=adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min, adMefPerCosPerUniPh1DayIngressGreenFrameDiscards=adMefPerCosPerUniPh1DayIngressGreenFrameDiscards, adMefPerCosPerUniPh15MinEgressGreenFrames=adMefPerCosPerUniPh15MinEgressGreenFrames, adMefPerCosPerUniPh1DayIntervalTable=adMefPerCosPerUniPh1DayIntervalTable, adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min=adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min, adMefPerCosPerUniPh15MinEgressGreenOctets=adMefPerCosPerUniPh15MinEgressGreenOctets, adMefPerCosPerUniPh1DayEgressGreenFrames=adMefPerCosPerUniPh1DayEgressGreenFrames, adMefPerCosPerUniPhCurTimeElapsed15Min=adMefPerCosPerUniPhCurTimeElapsed15Min, adMefPerCosPerUniPhCurInvalidIntervals15Min=adMefPerCosPerUniPhCurInvalidIntervals15Min, adMefPerCosPerUniPh1DayEgressGreenOctetDiscards=adMefPerCosPerUniPh1DayEgressGreenOctetDiscards, adMefPerCosPerUniPh15MinIngressGreenFrames=adMefPerCosPerUniPh15MinIngressGreenFrames, adMefPerCosPerUniPh1DayIngressGreenOctets=adMefPerCosPerUniPh1DayIngressGreenOctets, adMefPerCosPerUniPh1DayIngressGreenFrames=adMefPerCosPerUniPh1DayIngressGreenFrames, adMefPerCosPerUniPh15MinIntervalEntry=adMefPerCosPerUniPh15MinIntervalEntry, adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min=adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min, adMefPerCosPerUniPhCurIngressGreenFrames15Min=adMefPerCosPerUniPhCurIngressGreenFrames15Min, PYSNMP_MODULE_ID=adGenAosMefPerCosPerUniPerfHistoryMib, adGenAosMefPerCosPerUniPerfHistoryMib=adGenAosMefPerCosPerUniPerfHistoryMib, adMefPerCosPerUniPhCurIngressGreenOctets15Min=adMefPerCosPerUniPhCurIngressGreenOctets15Min, adMefPerCosPerUniPh15MinEgressGreenFrameDiscards=adMefPerCosPerUniPh15MinEgressGreenFrameDiscards, adMefPerCosPerUniPhCurInvalidIntervals1Day=adMefPerCosPerUniPhCurInvalidIntervals1Day, adMefPerCosPerUniPhCurQueueNumber=adMefPerCosPerUniPhCurQueueNumber, adGenAosMefPerCosPerUniPerfHistoryCompliances=adGenAosMefPerCosPerUniPerfHistoryCompliances)
