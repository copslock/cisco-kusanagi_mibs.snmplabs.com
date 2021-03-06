#
# PySNMP MIB module CADANT-SW-MEAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-SW-MEAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:46:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
cadExperimental, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadExperimental")
CardId, = mibBuilder.importSymbols("CADANT-TC", "CardId")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, NotificationType, ObjectIdentity, iso, TimeTicks, Gauge32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "NotificationType", "ObjectIdentity", "iso", "TimeTicks", "Gauge32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "Counter64")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
cadSoftwareMeasMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9))
cadSoftwareMeasMib.setRevisions(('2014-09-04 00:00', '2012-07-07 00:00', '2006-12-14 00:00', '2006-04-14 00:00', '2006-02-08 00:00', '2006-01-30 00:00', '2006-01-24 00:00', '2006-01-10 00:00', '2005-10-11 00:00', '2005-08-18 00:00', '2003-12-22 00:00', '2001-10-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadSoftwareMeasMib.setRevisionsDescriptions(('Add global scaling counts and cadCamScaleTable.', 'Remove cadUpChannelULBOverride.', 'Modify the index of cadSWUChannelMeasEntry.', 'Removed cadUpChannelAvgContSlots. (moved to CADANT-HW-MEAS-MIB)', 'Added additional UGS measurements.', 'Added implementation per utilization interval for cadUpChannelAvgContSlots, cadUpChannelAvgUtil.', 'Add delta count implementation .', 'Added UGS count / measurements for Time Warner.', 'Added support for intelligent channel optimization.', 'Added cadUpChannelIngressCancellationBandwidth.', 'added cadUpChannelRequestSizeMslots and cadUpChannelInitialMaintSizeMslots', 'created',))
if mibBuilder.loadTexts: cadSoftwareMeasMib.setLastUpdated('201409040000Z')
if mibBuilder.loadTexts: cadSoftwareMeasMib.setOrganization('Arris International, Inc.')
if mibBuilder.loadTexts: cadSoftwareMeasMib.setContactInfo('Arris Technical Support Postal: ARRIS E-Mail: support@arrisi.com')
if mibBuilder.loadTexts: cadSoftwareMeasMib.setDescription('This Mib Module contains all of the soft counts associated with software in the Arris C4 CMTS.')
cadChassisScaleGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1))
cadantTotalDevices = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalDevices.setStatus('current')
if mibBuilder.loadTexts: cadantTotalDevices.setDescription('The current total number of devices in the E6000 CER.')
cadantDsBondedDevices = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantDsBondedDevices.setStatus('current')
if mibBuilder.loadTexts: cadantDsBondedDevices.setDescription('The current total number of DS bonded devices in the E6000 CER.')
cadantUsBondedDevices = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantUsBondedDevices.setStatus('current')
if mibBuilder.loadTexts: cadantUsBondedDevices.setDescription('The current total number of US bonded devices in the E6000 CER.')
cadantTotalServiceFlows = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalServiceFlows.setStatus('current')
if mibBuilder.loadTexts: cadantTotalServiceFlows.setDescription('The current total number of SFs in the E6000 CER.')
cadantTotalClassifiers = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalClassifiers.setStatus('current')
if mibBuilder.loadTexts: cadantTotalClassifiers.setDescription('The current total number of classifiers in the E6000 CER.')
cadantTotalArpEntries = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalArpEntries.setStatus('current')
if mibBuilder.loadTexts: cadantTotalArpEntries.setDescription('The current total number of ARP table entries for IPv4 addresses in the E6000 CER.')
cadantTotalIpv4Routes = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalIpv4Routes.setStatus('current')
if mibBuilder.loadTexts: cadantTotalIpv4Routes.setDescription('The current total number of IPv4 routes in the E6000 CER.')
cadantTotalNdEntries = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalNdEntries.setStatus('current')
if mibBuilder.loadTexts: cadantTotalNdEntries.setDescription('The current total number of Neighbor Discovery entries for IPv6 addresses in the E6000 CER.')
cadantTotalIpv6Routes = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalIpv6Routes.setStatus('current')
if mibBuilder.loadTexts: cadantTotalIpv6Routes.setDescription('The current total number of IPv6 routes in the E6000 CER.')
cadantDocsisMulticastStreams = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantDocsisMulticastStreams.setStatus('current')
if mibBuilder.loadTexts: cadantDocsisMulticastStreams.setDescription('The current total number of DOCSIS multicast streams that are currently joined.')
cadantVideoMulticastStreams = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantVideoMulticastStreams.setStatus('current')
if mibBuilder.loadTexts: cadantVideoMulticastStreams.setDescription('The current total number of IEQ video multicast streams that are currently joined.')
cadantTotalCpe = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalCpe.setStatus('current')
if mibBuilder.loadTexts: cadantTotalCpe.setDescription('The current total number of cpe devices in the E6000 CER.')
cadSWUChannelMeasTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2), )
if mibBuilder.loadTexts: cadSWUChannelMeasTable.setStatus('current')
if mibBuilder.loadTexts: cadSWUChannelMeasTable.setDescription(' This table contains software counts in the upstream channels.')
cadSWUChannelMeasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadSWUChannelMeasEntry.setStatus('current')
if mibBuilder.loadTexts: cadSWUChannelMeasEntry.setDescription('List of counts or measurements for a single upstream channel. For Docsis 2.0 CMTSs, an entry in this table exists for each ifEntry with an ifType of docsCableUpstreamChannel (205). For Docsis 1.x CM/CMTSs and Docsis 2.0 CMs, an entry in this table exists for each ifEntry with an ifType of docsCableUpstreamInterface (129).')
cadUpChannelRequestSizeMslots = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelRequestSizeMslots.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelRequestSizeMslots.setDescription('')
cadUpChannelInitialMaintSizeMslots = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelInitialMaintSizeMslots.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelInitialMaintSizeMslots.setDescription('')
cadUpChannelIngressCancellationBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelIngressCancellationBandwidth.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelIngressCancellationBandwidth.setDescription('The utilization index is a percentage expressing the ratio between minislots reserved for ingress cancellation analysis versus the total number of minislots for upstream transmission. Formula: ingress cancellation bandwidth = (cancellation_minislots_per_second / total_minislots_per_second) * 100% ')
cadUpChannelAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelAttenuation.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelAttenuation.setDescription('RF input amplifier attenuation')
cadUpChannelRFCalibration = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelRFCalibration.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelRFCalibration.setDescription('Factory RF calibration settings.')
cadUpChannelTScale = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTScale.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelTScale.setDescription('TDMA nominal burst gain adjusting factor')
cadUpChannelSScale = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelSScale.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelSScale.setDescription('SCDMA nominal burst gain adjusting factor')
cadUpChannelStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3), )
if mibBuilder.loadTexts: cadUpChannelStatsTable.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelStatsTable.setDescription('A table of counts and measurements for a logical upstream channel.')
cadUpChannelStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadUpChannelStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelStatsEntry.setDescription('The measurements for a logical upstream channel.')
cadUpChannelMaxUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMaxUGSLastOneHour.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelMaxUGSLastOneHour.setDescription('This object indicates the maximum number of Unsolicited Grant Service (UGS) allocated on a given upstream in the last one hour. This would be used for the user to evaluate traffic load at any given time of the day.')
cadUpChannelAvgUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelAvgUGSLastOneHour.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelAvgUGSLastOneHour.setDescription('This object indicates the average number of Unsolicited Grant Service (UGS) allocated on a given upstream in the last one hour. This would be used for the user to evaluate traffic load at any given time of the day.')
cadUpChannelMinUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMinUGSLastOneHour.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelMinUGSLastOneHour.setDescription('This object indicates the minimum number of Unsolicited Grant Service (UGS) allocated on a given upstream in the last one hour. This would be used for the user to evaluate traffic load at any given time of the day.')
cadUpChannelMaxUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMaxUGSLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelMaxUGSLastFiveMins.setDescription('This object indicates the maximum number of Unsolicited Grant Service (UGS) allocated on a given upstream in the last five minutes. This would be used for the user to evaluate traffic load at any given time of the day.')
cadUpChannelAvgUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelAvgUGSLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelAvgUGSLastFiveMins.setDescription('This object indicates the average number of Unsolicited Grant Service (UGS) allocated on a given upstream in the last five minutes. This would be used for the user to evaluate traffic load at any given time of the day.')
cadUpChannelMinUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMinUGSLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelMinUGSLastFiveMins.setDescription('This object indicates the minimum number of Unsolicited Grant Service (UGS) allocated on a given upstream in the last five minutes. This would be used for the user to evaluate traffic load at any given time of the day.')
cadUpChannelNormalUGSDeniedLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelNormalUGSDeniedLastOneHour.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelNormalUGSDeniedLastOneHour.setDescription('This object indicates the total normal calls that were denied in the last one hour.')
cadUpChannelNormalUGSDeniedLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelNormalUGSDeniedLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelNormalUGSDeniedLastFiveMins.setDescription('This object indicates the total normal calls that were denied in the last 5 minutes.')
cadUpChannelEmergencyUGSDeniedLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelEmergencyUGSDeniedLastOneHour.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelEmergencyUGSDeniedLastOneHour.setDescription('This object indicates the total emergency calls that were denied in the last one hour.')
cadUpChannelEmergencyUGSDeniedLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelEmergencyUGSDeniedLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelEmergencyUGSDeniedLastFiveMins.setDescription('This object indicates the total emergency calls that were denied in the last 5 minutes.')
cadUpChannelTotalNormalUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalNormalUGSLastOneHour.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelTotalNormalUGSLastOneHour.setDescription('This object indicates the total normal calls in the last one hour.')
cadUpChannelTotalNormalUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalNormalUGSLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelTotalNormalUGSLastFiveMins.setDescription('This object indicates the total normal calls in the last 5 minutes.')
cadUpChannelTotalEmergencyUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalEmergencyUGSLastOneHour.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelTotalEmergencyUGSLastOneHour.setDescription('This object indicates the total emergency calls in the last one hour.')
cadUpChannelTotalEmergencyUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalEmergencyUGSLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: cadUpChannelTotalEmergencyUGSLastFiveMins.setDescription('This object indicates the total emergency calls in the last 5 minutes.')
cadCamScaleTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4), )
if mibBuilder.loadTexts: cadCamScaleTable.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleTable.setDescription('This table contains scale counts per non-spare CAM.')
cadCamScaleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1), ).setIndexNames((0, "CADANT-SW-MEAS-MIB", "cadCamScaleCardId"))
if mibBuilder.loadTexts: cadCamScaleEntry.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleEntry.setDescription('The current scale counts for this non-spare CAM.')
cadCamScaleCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 1), CardId().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 6), ValueRangeConstraint(9, 14), )))
if mibBuilder.loadTexts: cadCamScaleCardId.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleCardId.setDescription('Card Id of the Cam. There is no row for spare CAM slots.')
cadCamScaleDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleDevices.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleDevices.setDescription('Current number of devices on the CAM.')
cadCamScaleBondedDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleBondedDevices.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleBondedDevices.setDescription('Current number of bonded devices on the CAM.')
cadCamScaleServiceFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleServiceFlows.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleServiceFlows.setDescription('Current number of DS SFs on a DCAM. Current number US SFs on a UCAM.')
cadCamScaleClassifiers = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleClassifiers.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleClassifiers.setDescription('Current number of Classifiers in use on the CAM.')
cadCamScaleIpv4Addresses = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleIpv4Addresses.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleIpv4Addresses.setDescription('Current number of IPv4 addresses on the CAM.')
cadCamScaleIpv6Addresses = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleIpv6Addresses.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleIpv6Addresses.setDescription('Current number of IPv6 Addresses on the CAM.')
cadCamScaleUsRangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleUsRangeCount.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleUsRangeCount.setDescription('Total US channels requiring ranging. Each CM with N channels in-service to this UCAM adds N to the count (e.g., a 4 US bonded CM adds 4 to this count). Unbonded modems add one to the count. For DCAMs, this count is always zero.')
cadCamScaleTotalCpe = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleTotalCpe.setStatus('current')
if mibBuilder.loadTexts: cadCamScaleTotalCpe.setDescription('The current total number of cpe devices on this CAM.')
mibBuilder.exportSymbols("CADANT-SW-MEAS-MIB", cadantTotalDevices=cadantTotalDevices, cadUpChannelAvgUGSLastOneHour=cadUpChannelAvgUGSLastOneHour, cadUpChannelTotalNormalUGSLastFiveMins=cadUpChannelTotalNormalUGSLastFiveMins, cadUpChannelMaxUGSLastOneHour=cadUpChannelMaxUGSLastOneHour, cadCamScaleEntry=cadCamScaleEntry, cadantTotalIpv4Routes=cadantTotalIpv4Routes, cadantTotalCpe=cadantTotalCpe, cadantDsBondedDevices=cadantDsBondedDevices, cadUpChannelRequestSizeMslots=cadUpChannelRequestSizeMslots, cadUpChannelEmergencyUGSDeniedLastOneHour=cadUpChannelEmergencyUGSDeniedLastOneHour, cadantTotalIpv6Routes=cadantTotalIpv6Routes, cadantDocsisMulticastStreams=cadantDocsisMulticastStreams, cadUpChannelEmergencyUGSDeniedLastFiveMins=cadUpChannelEmergencyUGSDeniedLastFiveMins, cadUpChannelInitialMaintSizeMslots=cadUpChannelInitialMaintSizeMslots, cadantTotalServiceFlows=cadantTotalServiceFlows, cadUpChannelRFCalibration=cadUpChannelRFCalibration, cadUpChannelTotalEmergencyUGSLastOneHour=cadUpChannelTotalEmergencyUGSLastOneHour, cadCamScaleTable=cadCamScaleTable, cadantUsBondedDevices=cadantUsBondedDevices, cadUpChannelMinUGSLastFiveMins=cadUpChannelMinUGSLastFiveMins, cadUpChannelTotalNormalUGSLastOneHour=cadUpChannelTotalNormalUGSLastOneHour, cadUpChannelNormalUGSDeniedLastOneHour=cadUpChannelNormalUGSDeniedLastOneHour, cadCamScaleCardId=cadCamScaleCardId, cadUpChannelTotalEmergencyUGSLastFiveMins=cadUpChannelTotalEmergencyUGSLastFiveMins, cadCamScaleUsRangeCount=cadCamScaleUsRangeCount, cadCamScaleIpv6Addresses=cadCamScaleIpv6Addresses, cadantTotalArpEntries=cadantTotalArpEntries, cadantTotalNdEntries=cadantTotalNdEntries, PYSNMP_MODULE_ID=cadSoftwareMeasMib, cadUpChannelStatsEntry=cadUpChannelStatsEntry, cadantTotalClassifiers=cadantTotalClassifiers, cadCamScaleTotalCpe=cadCamScaleTotalCpe, cadUpChannelIngressCancellationBandwidth=cadUpChannelIngressCancellationBandwidth, cadUpChannelMaxUGSLastFiveMins=cadUpChannelMaxUGSLastFiveMins, cadUpChannelAttenuation=cadUpChannelAttenuation, cadSoftwareMeasMib=cadSoftwareMeasMib, cadUpChannelSScale=cadUpChannelSScale, cadChassisScaleGroup=cadChassisScaleGroup, cadUpChannelMinUGSLastOneHour=cadUpChannelMinUGSLastOneHour, cadCamScaleDevices=cadCamScaleDevices, cadUpChannelTScale=cadUpChannelTScale, cadSWUChannelMeasTable=cadSWUChannelMeasTable, cadUpChannelNormalUGSDeniedLastFiveMins=cadUpChannelNormalUGSDeniedLastFiveMins, cadCamScaleIpv4Addresses=cadCamScaleIpv4Addresses, cadCamScaleBondedDevices=cadCamScaleBondedDevices, cadSWUChannelMeasEntry=cadSWUChannelMeasEntry, cadCamScaleServiceFlows=cadCamScaleServiceFlows, cadCamScaleClassifiers=cadCamScaleClassifiers, cadUpChannelStatsTable=cadUpChannelStatsTable, cadantVideoMulticastStreams=cadantVideoMulticastStreams, cadUpChannelAvgUGSLastFiveMins=cadUpChannelAvgUGSLastFiveMins)
