#
# PySNMP MIB module DL-SLA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DL-SLA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, enterprises, Bits, Integer32, ObjectIdentity, ModuleIdentity, Counter32, IpAddress, NotificationType, TimeTicks, Counter64, Gauge32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "Bits", "Integer32", "ObjectIdentity", "ModuleIdentity", "Counter32", "IpAddress", "NotificationType", "TimeTicks", "Counter64", "Gauge32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
digital_link = MibIdentifier((1, 3, 6, 1, 4, 1, 300)).setLabel("digital-link")
dl_ServiceLevelAgreement = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260)).setLabel("dl-ServiceLevelAgreement")
dlcSLAConfigurationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 1))
unitSLAConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 1, 1))
configSLA = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configSLA.setStatus('mandatory')
unitSamplingPeriodForFDR_DDR = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setLabel("unitSamplingPeriodForFDR-DDR").setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitSamplingPeriodForFDR_DDR.setStatus('mandatory')
unitSamplingPeriodForDelayMeasurement = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitSamplingPeriodForDelayMeasurement.setStatus('mandatory')
unitThresholdForFDR = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitThresholdForFDR.setStatus('mandatory')
unitThresholdForDDR = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitThresholdForDDR.setStatus('mandatory')
unitDelayMeasurementPacketSize = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 1500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitDelayMeasurementPacketSize.setStatus('mandatory')
unitOamDomainIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitOamDomainIdentifier.setStatus('mandatory')
unitOamLocationIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitOamLocationIdentifier.setStatus('mandatory')
perDLCIConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 1, 2))
configurationPerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1), )
if mibBuilder.loadTexts: configurationPerDLCITable.setStatus('mandatory')
configurationPerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "configurationPerDLCITableIndex"))
if mibBuilder.loadTexts: configurationPerDLCIEntry.setStatus('mandatory')
configurationPerDLCITableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationPerDLCITableIndex.setStatus('mandatory')
commitedInformationRatePerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1536000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commitedInformationRatePerDLCI.setStatus('mandatory')
remoteDLCIPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteDLCIPerDLCI.setStatus('mandatory')
remoteIpAddressPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteIpAddressPerDLCI.setStatus('mandatory')
thresholdForDelayMeasurementsPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thresholdForDelayMeasurementsPerDLCI.setStatus('mandatory')
dlcSLAStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2))
dlcDeliveryRatioStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2, 1))
deliveryRatioPerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1), )
if mibBuilder.loadTexts: deliveryRatioPerDLCITable.setStatus('mandatory')
deliveryRatioPerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "deliveryRatioPerDLCITableIndex"))
if mibBuilder.loadTexts: deliveryRatioPerDLCIEntry.setStatus('mandatory')
deliveryRatioPerDLCITableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deliveryRatioPerDLCITableIndex.setStatus('mandatory')
deliveryTableEncodedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deliveryTableEncodedValue.setStatus('mandatory')
deliveryTableTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deliveryTableTimestamp.setStatus('obsolete')
fTCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTCLperDLCI.setStatus('mandatory')
fTELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTELperDLCI.setStatus('mandatory')
fRCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRCLperDLCI.setStatus('mandatory')
fRELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRELperDLCI.setStatus('mandatory')
fTCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTCRperDLCI.setStatus('mandatory')
fTERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fTERperDLCI.setStatus('mandatory')
fRCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRCRperDLCI.setStatus('mandatory')
fRERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fRERperDLCI.setStatus('mandatory')
fDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fDRNumberOfSamplesTaken.setStatus('obsolete')
fDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fDRNumberOfThresholdViolations.setStatus('obsolete')
dTCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTCLperDLCI.setStatus('mandatory')
dTELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTELperDLCI.setStatus('mandatory')
dRCLperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRCLperDLCI.setStatus('mandatory')
dRELperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRELperDLCI.setStatus('mandatory')
dTCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTCRperDLCI.setStatus('mandatory')
dTERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dTERperDLCI.setStatus('mandatory')
dRCRperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRCRperDLCI.setStatus('mandatory')
dRERperDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dRERperDLCI.setStatus('mandatory')
dDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dDRNumberOfSamplesTaken.setStatus('obsolete')
dDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dDRNumberOfThresholdViolations.setStatus('obsolete')
txFDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFDRTimestamp.setStatus('mandatory')
txFDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFDRNumberOfSamplesTaken.setStatus('mandatory')
txFDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFDRNumberOfThresholdViolations.setStatus('mandatory')
rxFDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFDRTimestamp.setStatus('mandatory')
rxFDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFDRNumberOfSamplesTaken.setStatus('mandatory')
rxFDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFDRNumberOfThresholdViolations.setStatus('mandatory')
txDDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDDRTimestamp.setStatus('mandatory')
txDDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDDRNumberOfSamplesTaken.setStatus('mandatory')
txDDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDDRNumberOfThresholdViolations.setStatus('mandatory')
rxDDRTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDDRTimestamp.setStatus('mandatory')
rxDDRNumberOfSamplesTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDDRNumberOfSamplesTaken.setStatus('mandatory')
rxDDRNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDDRNumberOfThresholdViolations.setStatus('mandatory')
txDiscardEligible = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDiscardEligible.setStatus('mandatory')
rxDiscardEligible = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDiscardEligible.setStatus('mandatory')
txFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFECN.setStatus('mandatory')
rxFECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFECN.setStatus('mandatory')
txBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txBECN.setStatus('mandatory')
rxBECN = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxBECN.setStatus('mandatory')
dlcDelayStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2, 2))
delayPerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1), )
if mibBuilder.loadTexts: delayPerDLCITable.setStatus('mandatory')
delayPerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "delayPerDLCITableIndex"))
if mibBuilder.loadTexts: delayPerDLCIEntry.setStatus('mandatory')
delayPerDLCITableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayPerDLCITableIndex.setStatus('mandatory')
delayTableEncodedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayTableEncodedValue.setStatus('mandatory')
delayTableTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayTableTimestamp.setStatus('mandatory')
totalRoundTripDelayPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalRoundTripDelayPerDLCI.setStatus('mandatory')
maximumRoundTripDelayNSamplesPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumRoundTripDelayNSamplesPerDLCI.setStatus('mandatory')
maximumRoundTripDelay2NSamplesPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumRoundTripDelay2NSamplesPerDLCI.setStatus('mandatory')
maximumRoundTripDelay4NSamplesPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumRoundTripDelay4NSamplesPerDLCI.setStatus('mandatory')
numberOfDelayMeasurementsPerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfDelayMeasurementsPerDLCI.setStatus('mandatory')
delayNumberOfThresholdViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: delayNumberOfThresholdViolations.setStatus('mandatory')
dlcOutageStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 300, 260, 2, 3))
outagePerDLCITable = MibTable((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1), )
if mibBuilder.loadTexts: outagePerDLCITable.setStatus('mandatory')
outagePerDLCIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1), ).setIndexNames((0, "DL-SLA-MIB", "outageTableIndex"))
if mibBuilder.loadTexts: outagePerDLCIEntry.setStatus('mandatory')
outageTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableIndex.setStatus('mandatory')
outageTableEncodedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableEncodedValue.setStatus('mandatory')
outageTableTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableTimestamp.setStatus('mandatory')
outageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("no-outage", 2), ("excluded-outage", 3), ("included-outage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageStatus.setStatus('mandatory')
numberOfOutageCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfOutageCounter.setStatus('mandatory')
periodOfOutages = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: periodOfOutages.setStatus('mandatory')
numberOfExcludedOutageCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfExcludedOutageCounter.setStatus('mandatory')
periodOfExcludedOutages = MibTableColumn((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: periodOfExcludedOutages.setStatus('mandatory')
outageTableLastTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outageTableLastTimestamp.setStatus('mandatory')
fDRThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 300, 260) + (0,1)).setObjects(("DL-SLA-MIB", "deliveryRatioPerDLCITableIndex"))
dDRThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 300, 260) + (0,2)).setObjects(("DL-SLA-MIB", "deliveryRatioPerDLCITableIndex"))
delayThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 300, 260) + (0,3)).setObjects(("DL-SLA-MIB", "delayPerDLCITableIndex"))
mibBuilder.exportSymbols("DL-SLA-MIB", dRCLperDLCI=dRCLperDLCI, fDRNumberOfSamplesTaken=fDRNumberOfSamplesTaken, txFDRTimestamp=txFDRTimestamp, totalRoundTripDelayPerDLCI=totalRoundTripDelayPerDLCI, perDLCIConfiguration=perDLCIConfiguration, rxBECN=rxBECN, outagePerDLCITable=outagePerDLCITable, txFDRNumberOfSamplesTaken=txFDRNumberOfSamplesTaken, configurationPerDLCIEntry=configurationPerDLCIEntry, dlcSLAConfigurationGroup=dlcSLAConfigurationGroup, thresholdForDelayMeasurementsPerDLCI=thresholdForDelayMeasurementsPerDLCI, maximumRoundTripDelay2NSamplesPerDLCI=maximumRoundTripDelay2NSamplesPerDLCI, numberOfOutageCounter=numberOfOutageCounter, fRERperDLCI=fRERperDLCI, dDRNumberOfThresholdViolations=dDRNumberOfThresholdViolations, fRELperDLCI=fRELperDLCI, periodOfExcludedOutages=periodOfExcludedOutages, dTERperDLCI=dTERperDLCI, unitThresholdForDDR=unitThresholdForDDR, fTCLperDLCI=fTCLperDLCI, delayTableTimestamp=delayTableTimestamp, delayNumberOfThresholdViolations=delayNumberOfThresholdViolations, dDRNumberOfSamplesTaken=dDRNumberOfSamplesTaken, deliveryTableEncodedValue=deliveryTableEncodedValue, dlcOutageStatistics=dlcOutageStatistics, dDRThresholdTrap=dDRThresholdTrap, dlcDeliveryRatioStatistics=dlcDeliveryRatioStatistics, delayPerDLCITable=delayPerDLCITable, unitSamplingPeriodForDelayMeasurement=unitSamplingPeriodForDelayMeasurement, unitThresholdForFDR=unitThresholdForFDR, outageStatus=outageStatus, rxDDRNumberOfThresholdViolations=rxDDRNumberOfThresholdViolations, rxDiscardEligible=rxDiscardEligible, remoteIpAddressPerDLCI=remoteIpAddressPerDLCI, configSLA=configSLA, unitDelayMeasurementPacketSize=unitDelayMeasurementPacketSize, outageTableLastTimestamp=outageTableLastTimestamp, maximumRoundTripDelay4NSamplesPerDLCI=maximumRoundTripDelay4NSamplesPerDLCI, commitedInformationRatePerDLCI=commitedInformationRatePerDLCI, rxFDRNumberOfSamplesTaken=rxFDRNumberOfSamplesTaken, configurationPerDLCITable=configurationPerDLCITable, outageTableEncodedValue=outageTableEncodedValue, txDDRTimestamp=txDDRTimestamp, delayPerDLCITableIndex=delayPerDLCITableIndex, deliveryRatioPerDLCIEntry=deliveryRatioPerDLCIEntry, outagePerDLCIEntry=outagePerDLCIEntry, dRELperDLCI=dRELperDLCI, txDiscardEligible=txDiscardEligible, deliveryRatioPerDLCITable=deliveryRatioPerDLCITable, txFDRNumberOfThresholdViolations=txFDRNumberOfThresholdViolations, rxFDRTimestamp=rxFDRTimestamp, rxDDRNumberOfSamplesTaken=rxDDRNumberOfSamplesTaken, fDRThresholdTrap=fDRThresholdTrap, dTCRperDLCI=dTCRperDLCI, outageTableTimestamp=outageTableTimestamp, txDDRNumberOfSamplesTaken=txDDRNumberOfSamplesTaken, numberOfDelayMeasurementsPerDLCI=numberOfDelayMeasurementsPerDLCI, delayPerDLCIEntry=delayPerDLCIEntry, dRERperDLCI=dRERperDLCI, txFECN=txFECN, dTELperDLCI=dTELperDLCI, fRCLperDLCI=fRCLperDLCI, dlcSLAStatisticsGroup=dlcSLAStatisticsGroup, unitSLAConfiguration=unitSLAConfiguration, txBECN=txBECN, numberOfExcludedOutageCounter=numberOfExcludedOutageCounter, fTCRperDLCI=fTCRperDLCI, outageTableIndex=outageTableIndex, dTCLperDLCI=dTCLperDLCI, rxDDRTimestamp=rxDDRTimestamp, fTELperDLCI=fTELperDLCI, unitOamDomainIdentifier=unitOamDomainIdentifier, delayThresholdTrap=delayThresholdTrap, dl_ServiceLevelAgreement=dl_ServiceLevelAgreement, fDRNumberOfThresholdViolations=fDRNumberOfThresholdViolations, dRCRperDLCI=dRCRperDLCI, fRCRperDLCI=fRCRperDLCI, rxFECN=rxFECN, digital_link=digital_link, fTERperDLCI=fTERperDLCI, txDDRNumberOfThresholdViolations=txDDRNumberOfThresholdViolations, periodOfOutages=periodOfOutages, unitSamplingPeriodForFDR_DDR=unitSamplingPeriodForFDR_DDR, unitOamLocationIdentifier=unitOamLocationIdentifier, deliveryRatioPerDLCITableIndex=deliveryRatioPerDLCITableIndex, deliveryTableTimestamp=deliveryTableTimestamp, maximumRoundTripDelayNSamplesPerDLCI=maximumRoundTripDelayNSamplesPerDLCI, configurationPerDLCITableIndex=configurationPerDLCITableIndex, delayTableEncodedValue=delayTableEncodedValue, remoteDLCIPerDLCI=remoteDLCIPerDLCI, dlcDelayStatistics=dlcDelayStatistics, rxFDRNumberOfThresholdViolations=rxFDRNumberOfThresholdViolations)
