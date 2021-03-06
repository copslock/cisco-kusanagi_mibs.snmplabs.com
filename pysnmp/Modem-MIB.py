#
# PySNMP MIB module Modem-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Modem-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, Counter64, iso, MibIdentifier, ModuleIdentity, Bits, NotificationType, Integer32, mib_2, Gauge32, IpAddress, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "iso", "MibIdentifier", "ModuleIdentity", "Bits", "NotificationType", "Integer32", "mib-2", "Gauge32", "IpAddress", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mdmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 38, 1))
if mibBuilder.loadTexts: mdmMIB.setLastUpdated('9406120000Z')
if mibBuilder.loadTexts: mdmMIB.setOrganization('IETF Modem Management Working Group')
mdmMib = MibIdentifier((1, 3, 6, 1, 2, 1, 38))
mdmMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 38, 1, 1))
mdmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 38, 1, 2))
mdmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 38, 1, 2, 1))
mdmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 38, 1, 2, 2))
mdmIDGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 1)).setObjects(("Modem-MIB", "mdmIDManufacturerOID"), ("Modem-MIB", "mdmIDProductDetails"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmIDGroup = mdmIDGroup.setStatus('current')
mdmLineInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 2)).setObjects(("Modem-MIB", "mdmLineCarrierLossTime"), ("Modem-MIB", "mdmLineState"), ("Modem-MIB", "mdmLineCapabilitiesID"), ("Modem-MIB", "mdmLineCapabilitiesEnableRequested"), ("Modem-MIB", "mdmLineCapabilitiesEnableGranted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmLineInterfaceGroup = mdmLineInterfaceGroup.setStatus('current')
mdmDTEInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 3)).setObjects(("Modem-MIB", "mdmDTEActionDTROnToOff"), ("Modem-MIB", "mdmDTEActionDTROffToOn"), ("Modem-MIB", "mdmDTESyncTimingSource"), ("Modem-MIB", "mdmDTESyncAsyncMode"), ("Modem-MIB", "mdmDTEInactivityTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmDTEInterfaceGroup = mdmDTEInterfaceGroup.setStatus('current')
mdmCallControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 4)).setObjects(("Modem-MIB", "mdmCCRingsBeforeAnswer"), ("Modem-MIB", "mdmCCCallSetUpFailTimer"), ("Modem-MIB", "mdmCCResultCodeEnable"), ("Modem-MIB", "mdmCCEscapeAction"), ("Modem-MIB", "mdmCCCallDuration"), ("Modem-MIB", "mdmCCConnectionFailReason"), ("Modem-MIB", "mdmCCStoredDialString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmCallControlGroup = mdmCallControlGroup.setStatus('current')
mdmErrorControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 5)).setObjects(("Modem-MIB", "mdmECErrorControlUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmErrorControlGroup = mdmErrorControlGroup.setStatus('current')
mdmDataCompressionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 6)).setObjects(("Modem-MIB", "mdmDCCompressionTypeUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmDataCompressionGroup = mdmDataCompressionGroup.setStatus('current')
mdmSignalConvertorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 7)).setObjects(("Modem-MIB", "mdmSCCurrentLineReceiveRate"), ("Modem-MIB", "mdmSCCurrentLineTransmitRate"), ("Modem-MIB", "mdmSCInitialLineReceiveRate"), ("Modem-MIB", "mdmSCInitialLineTransmitRate"), ("Modem-MIB", "mdmSCModulationSchemeUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmSignalConvertorGroup = mdmSignalConvertorGroup.setStatus('current')
mdmStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 8)).setObjects(("Modem-MIB", "mdmStatsRingNoAnswers"), ("Modem-MIB", "mdmStatsIncomingConnectionFailures"), ("Modem-MIB", "mdmStatsIncomingConnectionCompletions"), ("Modem-MIB", "mdmStatsFailedDialAttempts"), ("Modem-MIB", "mdmStatsOutgoingConnectionFailures"), ("Modem-MIB", "mdmStatsOutgoingConnectionCompletions"), ("Modem-MIB", "mdmStatsRetrains"), ("Modem-MIB", "mdmStats2400OrLessConnections"), ("Modem-MIB", "mdmStats2400To14400Connections"), ("Modem-MIB", "mdmStatsGreaterThan14400Connections"), ("Modem-MIB", "mdmStatsErrorControlledConnections"), ("Modem-MIB", "mdmStatsCompressedConnections"), ("Modem-MIB", "mdmStatsCompressionEfficiency"), ("Modem-MIB", "mdmStatsSentOctets"), ("Modem-MIB", "mdmStatsReceivedOctets"), ("Modem-MIB", "mdmStatsSentDataFrames"), ("Modem-MIB", "mdmStatsReceivedDataFrames"), ("Modem-MIB", "mdmStatsResentFrames"), ("Modem-MIB", "mdmStatsErrorFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmStatisticsGroup = mdmStatisticsGroup.setStatus('current')
mdmNumber = MibScalar((1, 3, 6, 1, 2, 1, 38, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmNumber.setStatus('current')
mdmIDTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 2), )
if mibBuilder.loadTexts: mdmIDTable.setStatus('current')
mdmIDEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1), ).setIndexNames((0, "Modem-MIB", "mdmIndex"))
if mibBuilder.loadTexts: mdmIDEntry.setStatus('current')
mdmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: mdmIndex.setStatus('current')
mdmIDManufacturerOID = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmIDManufacturerOID.setStatus('current')
mdmIDProductDetails = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmIDProductDetails.setStatus('current')
mdmLineTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 3), )
if mibBuilder.loadTexts: mdmLineTable.setStatus('current')
mdmLineEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1), )
mdmIDEntry.registerAugmentions(("Modem-MIB", "mdmLineEntry"))
mdmLineEntry.setIndexNames(*mdmIDEntry.getIndexNames())
if mibBuilder.loadTexts: mdmLineEntry.setStatus('current')
mdmLineCarrierLossTime = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLineCarrierLossTime.setStatus('current')
mdmLineState = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("onHook", 2), ("offHook", 3), ("connected", 4), ("busiedOut", 5), ("reset", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLineState.setStatus('current')
mdmLineCapabilitiesTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 4), )
if mibBuilder.loadTexts: mdmLineCapabilitiesTable.setStatus('current')
mdmLineCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1), ).setIndexNames((0, "Modem-MIB", "mdmIndex"), (0, "Modem-MIB", "mdmLineCapabilitiesIndex"))
if mibBuilder.loadTexts: mdmLineCapabilitiesEntry.setStatus('current')
mdmLineCapabilitiesIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: mdmLineCapabilitiesIndex.setStatus('current')
mdmLineCapabilitiesID = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmLineCapabilitiesID.setStatus('current')
mdmLineCapabilitiesEnableRequested = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("optional", 2), ("preferred", 3))).clone('preferred')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLineCapabilitiesEnableRequested.setStatus('current')
mdmLineCapabilitiesEnableGranted = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("optional", 2), ("preferred", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmLineCapabilitiesEnableGranted.setStatus('current')
mdmLineCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 38, 1, 1, 5))
mdmLineCapabilitiesV21 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 1))
if mibBuilder.loadTexts: mdmLineCapabilitiesV21.setStatus('current')
mdmLineCapabilitiesV22 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 2))
if mibBuilder.loadTexts: mdmLineCapabilitiesV22.setStatus('current')
mdmLineCapabilitiesV22bis = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 3))
if mibBuilder.loadTexts: mdmLineCapabilitiesV22bis.setStatus('current')
mdmLineCapabilitiesV23CC = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 4))
if mibBuilder.loadTexts: mdmLineCapabilitiesV23CC.setStatus('current')
mdmLineCapabilitiesV23SC = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 5))
if mibBuilder.loadTexts: mdmLineCapabilitiesV23SC.setStatus('current')
mdmLineCapabilitiesV25bis = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 6))
if mibBuilder.loadTexts: mdmLineCapabilitiesV25bis.setStatus('current')
mdmLineCapabilitiesV26bis = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 7))
if mibBuilder.loadTexts: mdmLineCapabilitiesV26bis.setStatus('current')
mdmLineCapabilitiesV26ter = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 8))
if mibBuilder.loadTexts: mdmLineCapabilitiesV26ter.setStatus('current')
mdmLineCapabilitiesV27ter = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 9))
if mibBuilder.loadTexts: mdmLineCapabilitiesV27ter.setStatus('current')
mdmLineCapabilitiesV32 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 10))
if mibBuilder.loadTexts: mdmLineCapabilitiesV32.setStatus('current')
mdmLineCapabilitiesV32bis = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 11))
if mibBuilder.loadTexts: mdmLineCapabilitiesV32bis.setStatus('current')
mdmLineCapabilitiesV32terbo = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 12))
if mibBuilder.loadTexts: mdmLineCapabilitiesV32terbo.setStatus('current')
mdmLineCapabilitiesVFC = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 13))
if mibBuilder.loadTexts: mdmLineCapabilitiesVFC.setStatus('current')
mdmLineCapabilitiesV34 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 14))
if mibBuilder.loadTexts: mdmLineCapabilitiesV34.setStatus('current')
mdmLineCapabilitiesV42 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 15))
if mibBuilder.loadTexts: mdmLineCapabilitiesV42.setStatus('current')
mdmLineCapabilitiesV42bis = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 16))
if mibBuilder.loadTexts: mdmLineCapabilitiesV42bis.setStatus('current')
mdmLineCapabilitiesMNP1 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 17))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP1.setStatus('current')
mdmLineCapabilitiesMNP2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 18))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP2.setStatus('current')
mdmLineCapabilitiesMNP3 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 19))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP3.setStatus('current')
mdmLineCapabilitiesMNP4 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 20))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP4.setStatus('current')
mdmLineCapabilitiesMNP5 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 21))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP5.setStatus('current')
mdmLineCapabilitiesMNP6 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 22))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP6.setStatus('current')
mdmLineCapabilitiesMNP7 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 23))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP7.setStatus('current')
mdmLineCapabilitiesMNP8 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 24))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP8.setStatus('current')
mdmLineCapabilitiesMNP9 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 25))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP9.setStatus('current')
mdmLineCapabilitiesMNP10 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 26))
if mibBuilder.loadTexts: mdmLineCapabilitiesMNP10.setStatus('current')
mdmLineCapabilitiesV29 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 27))
if mibBuilder.loadTexts: mdmLineCapabilitiesV29.setStatus('current')
mdmLineCapabilitiesV33 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 28))
if mibBuilder.loadTexts: mdmLineCapabilitiesV33.setStatus('current')
mdmLineCapabilitiesBell208 = ObjectIdentity((1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 29))
if mibBuilder.loadTexts: mdmLineCapabilitiesBell208.setStatus('current')
mdmDTEInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 6), )
if mibBuilder.loadTexts: mdmDTEInterfaceTable.setStatus('current')
mdmDTEInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1), )
mdmIDEntry.registerAugmentions(("Modem-MIB", "mdmDTEInterfaceEntry"))
mdmDTEInterfaceEntry.setIndexNames(*mdmIDEntry.getIndexNames())
if mibBuilder.loadTexts: mdmDTEInterfaceEntry.setStatus('current')
mdmDTEActionDTROnToOff = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ignore", 1), ("escapeToCommandMode", 2), ("disconnectCall", 3), ("resetModem", 4))).clone('disconnectCall')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDTEActionDTROnToOff.setStatus('current')
mdmDTEActionDTROffToOn = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ignore", 1), ("enableDial", 2), ("autoAnswerEnable", 3), ("establishConnection", 4))).clone('autoAnswerEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDTEActionDTROffToOn.setStatus('current')
mdmDTESyncTimingSource = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("loopback", 3), ("network", 4))).clone('internal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDTESyncTimingSource.setStatus('current')
mdmDTESyncAsyncMode = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("async", 1), ("sync", 2), ("syncAfterDial", 3))).clone('async')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDTESyncAsyncMode.setStatus('current')
mdmDTEInactivityTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDTEInactivityTimeout.setStatus('current')
mdmCallControlTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 7), )
if mibBuilder.loadTexts: mdmCallControlTable.setStatus('current')
mdmCallControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1), )
mdmIDEntry.registerAugmentions(("Modem-MIB", "mdmCallControlEntry"))
mdmCallControlEntry.setIndexNames(*mdmIDEntry.getIndexNames())
if mibBuilder.loadTexts: mdmCallControlEntry.setStatus('current')
mdmCCRingsBeforeAnswer = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCCRingsBeforeAnswer.setStatus('current')
mdmCCCallSetUpFailTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCCCallSetUpFailTimer.setStatus('current')
mdmCCResultCodeEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("numericEnabled", 2), ("verboseEnabled", 3))).clone('verboseEnabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCCResultCodeEnable.setStatus('current')
mdmCCEscapeAction = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignoreEscape", 1), ("hangUp", 2), ("enterCommandMode", 3))).clone('ignoreEscape')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCCEscapeAction.setStatus('current')
mdmCCCallDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmCCCallDuration.setStatus('current')
mdmCCConnectionFailReason = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 10, 11, 20, 30, 31, 32, 33, 40, 41, 42))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("managementCommand", 3), ("inactivityTimeout", 4), ("mnpIncompatibility", 5), ("protocolError", 6), ("powerLoss", 10), ("equipmentFailure", 11), ("dtrDrop", 20), ("noDialTone", 30), ("lineBusy", 31), ("noAnswer", 32), ("voiceDetected", 33), ("carrierLost", 40), ("trainingFailed", 41), ("faxDetected", 42)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmCCConnectionFailReason.setStatus('current')
mdmCCStoredDialStringTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 8), )
if mibBuilder.loadTexts: mdmCCStoredDialStringTable.setStatus('current')
mdmCCStoredDialStringEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1), ).setIndexNames((0, "Modem-MIB", "mdmIndex"), (0, "Modem-MIB", "mdmCCStoredDialStringIndex"))
if mibBuilder.loadTexts: mdmCCStoredDialStringEntry.setStatus('current')
mdmCCStoredDialStringIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mdmCCStoredDialStringIndex.setStatus('current')
mdmCCStoredDialString = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCCStoredDialString.setStatus('current')
mdmECTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 9), )
if mibBuilder.loadTexts: mdmECTable.setStatus('current')
mdmECEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 9, 1), )
mdmIDEntry.registerAugmentions(("Modem-MIB", "mdmECEntry"))
mdmECEntry.setIndexNames(*mdmIDEntry.getIndexNames())
if mibBuilder.loadTexts: mdmECEntry.setStatus('current')
mdmECErrorControlUsed = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 9, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmECErrorControlUsed.setStatus('current')
mdmDCTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 10), )
if mibBuilder.loadTexts: mdmDCTable.setStatus('current')
mdmDCEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 10, 1), )
mdmIDEntry.registerAugmentions(("Modem-MIB", "mdmDCEntry"))
mdmDCEntry.setIndexNames(*mdmIDEntry.getIndexNames())
if mibBuilder.loadTexts: mdmDCEntry.setStatus('current')
mdmDCCompressionTypeUsed = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 10, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmDCCompressionTypeUsed.setStatus('current')
mdmSCTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 11), )
if mibBuilder.loadTexts: mdmSCTable.setStatus('current')
mdmSCEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1), )
mdmIDEntry.registerAugmentions(("Modem-MIB", "mdmSCEntry"))
mdmSCEntry.setIndexNames(*mdmIDEntry.getIndexNames())
if mibBuilder.loadTexts: mdmSCEntry.setStatus('current')
mdmSCCurrentLineTransmitRate = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmSCCurrentLineTransmitRate.setStatus('current')
mdmSCCurrentLineReceiveRate = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmSCCurrentLineReceiveRate.setStatus('current')
mdmSCInitialLineTransmitRate = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmSCInitialLineTransmitRate.setStatus('current')
mdmSCInitialLineReceiveRate = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmSCInitialLineReceiveRate.setStatus('current')
mdmSCModulationSchemeUsed = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmSCModulationSchemeUsed.setStatus('current')
mdmStatsTable = MibTable((1, 3, 6, 1, 2, 1, 38, 1, 1, 12), )
if mibBuilder.loadTexts: mdmStatsTable.setStatus('current')
mdmStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1), )
mdmIDEntry.registerAugmentions(("Modem-MIB", "mdmStatsEntry"))
mdmStatsEntry.setIndexNames(*mdmIDEntry.getIndexNames())
if mibBuilder.loadTexts: mdmStatsEntry.setStatus('current')
mdmStatsRingNoAnswers = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsRingNoAnswers.setStatus('current')
mdmStatsIncomingConnectionFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsIncomingConnectionFailures.setStatus('current')
mdmStatsIncomingConnectionCompletions = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsIncomingConnectionCompletions.setStatus('current')
mdmStatsFailedDialAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsFailedDialAttempts.setStatus('current')
mdmStatsOutgoingConnectionFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsOutgoingConnectionFailures.setStatus('current')
mdmStatsOutgoingConnectionCompletions = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsOutgoingConnectionCompletions.setStatus('current')
mdmStatsRetrains = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsRetrains.setStatus('current')
mdmStats2400OrLessConnections = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStats2400OrLessConnections.setStatus('current')
mdmStats2400To14400Connections = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStats2400To14400Connections.setStatus('current')
mdmStatsGreaterThan14400Connections = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsGreaterThan14400Connections.setStatus('current')
mdmStatsErrorControlledConnections = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsErrorControlledConnections.setStatus('current')
mdmStatsCompressedConnections = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsCompressedConnections.setStatus('current')
mdmStatsCompressionEfficiency = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsCompressionEfficiency.setStatus('current')
mdmStatsSentOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsSentOctets.setStatus('current')
mdmStatsReceivedOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsReceivedOctets.setStatus('current')
mdmStatsSentDataFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsSentDataFrames.setStatus('current')
mdmStatsReceivedDataFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsReceivedDataFrames.setStatus('current')
mdmStatsResentFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsResentFrames.setStatus('current')
mdmStatsErrorFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatsErrorFrames.setStatus('current')
mdmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 38, 1, 2, 1, 1)).setObjects(("Modem-MIB", "mdmIDGroup"), ("Modem-MIB", "mdmLineInterfaceGroup"), ("Modem-MIB", "mdmDTEInterfaceGroup"), ("Modem-MIB", "mdmCallControlGroup"), ("Modem-MIB", "mdmSignalConvertorGroup"), ("Modem-MIB", "mdmStatisticsGroup"), ("Modem-MIB", "mdmErrorControlGroup"), ("Modem-MIB", "mdmDataCompressionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdmCompliance = mdmCompliance.setStatus('current')
mibBuilder.exportSymbols("Modem-MIB", mdmDTEInactivityTimeout=mdmDTEInactivityTimeout, mdmNumber=mdmNumber, mdmLineEntry=mdmLineEntry, mdmIDEntry=mdmIDEntry, mdmLineState=mdmLineState, mdmStatsEntry=mdmStatsEntry, mdmSCInitialLineReceiveRate=mdmSCInitialLineReceiveRate, mdmSCTable=mdmSCTable, mdmCompliance=mdmCompliance, mdmCCConnectionFailReason=mdmCCConnectionFailReason, mdmStatsErrorFrames=mdmStatsErrorFrames, mdmLineCapabilitiesEnableRequested=mdmLineCapabilitiesEnableRequested, mdmLineCapabilitiesV21=mdmLineCapabilitiesV21, mdmDCEntry=mdmDCEntry, mdmCallControlTable=mdmCallControlTable, mdmStatsOutgoingConnectionFailures=mdmStatsOutgoingConnectionFailures, mdmDTEInterfaceEntry=mdmDTEInterfaceEntry, mdmECTable=mdmECTable, mdmIDManufacturerOID=mdmIDManufacturerOID, mdmMib=mdmMib, mdmLineCapabilitiesV22=mdmLineCapabilitiesV22, mdmStatsIncomingConnectionCompletions=mdmStatsIncomingConnectionCompletions, mdmCCRingsBeforeAnswer=mdmCCRingsBeforeAnswer, mdmStats2400OrLessConnections=mdmStats2400OrLessConnections, mdmStatsFailedDialAttempts=mdmStatsFailedDialAttempts, mdmCCEscapeAction=mdmCCEscapeAction, mdmSCModulationSchemeUsed=mdmSCModulationSchemeUsed, mdmLineCapabilitiesV22bis=mdmLineCapabilitiesV22bis, mdmDCCompressionTypeUsed=mdmDCCompressionTypeUsed, mdmCCStoredDialStringEntry=mdmCCStoredDialStringEntry, mdmDCTable=mdmDCTable, mdmLineCapabilitiesV23CC=mdmLineCapabilitiesV23CC, mdmLineCapabilitiesMNP6=mdmLineCapabilitiesMNP6, mdmStatisticsGroup=mdmStatisticsGroup, mdmStatsErrorControlledConnections=mdmStatsErrorControlledConnections, mdmMIB=mdmMIB, mdmStatsIncomingConnectionFailures=mdmStatsIncomingConnectionFailures, mdmStatsRetrains=mdmStatsRetrains, mdmDTEInterfaceTable=mdmDTEInterfaceTable, mdmCompliances=mdmCompliances, mdmStatsSentOctets=mdmStatsSentOctets, mdmStatsGreaterThan14400Connections=mdmStatsGreaterThan14400Connections, mdmLineCapabilitiesV32=mdmLineCapabilitiesV32, mdmCCCallDuration=mdmCCCallDuration, mdmLineCapabilitiesMNP2=mdmLineCapabilitiesMNP2, mdmSCCurrentLineTransmitRate=mdmSCCurrentLineTransmitRate, PYSNMP_MODULE_ID=mdmMIB, mdmLineCapabilitiesV25bis=mdmLineCapabilitiesV25bis, mdmStatsReceivedDataFrames=mdmStatsReceivedDataFrames, mdmLineCapabilitiesVFC=mdmLineCapabilitiesVFC, mdmSCInitialLineTransmitRate=mdmSCInitialLineTransmitRate, mdmLineCapabilitiesEntry=mdmLineCapabilitiesEntry, mdmStatsRingNoAnswers=mdmStatsRingNoAnswers, mdmLineCapabilitiesMNP3=mdmLineCapabilitiesMNP3, mdmLineCapabilitiesV29=mdmLineCapabilitiesV29, mdmErrorControlGroup=mdmErrorControlGroup, mdmLineCapabilitiesMNP5=mdmLineCapabilitiesMNP5, mdmDTESyncAsyncMode=mdmDTESyncAsyncMode, mdmCallControlEntry=mdmCallControlEntry, mdmDTEInterfaceGroup=mdmDTEInterfaceGroup, mdmLineCapabilitiesV42bis=mdmLineCapabilitiesV42bis, mdmLineCapabilitiesMNP9=mdmLineCapabilitiesMNP9, mdmLineCarrierLossTime=mdmLineCarrierLossTime, mdmSCCurrentLineReceiveRate=mdmSCCurrentLineReceiveRate, mdmLineCapabilitiesIndex=mdmLineCapabilitiesIndex, mdmLineCapabilitiesMNP1=mdmLineCapabilitiesMNP1, mdmLineCapabilitiesV33=mdmLineCapabilitiesV33, mdmIDTable=mdmIDTable, mdmCCStoredDialStringIndex=mdmCCStoredDialStringIndex, mdmSignalConvertorGroup=mdmSignalConvertorGroup, mdmStats2400To14400Connections=mdmStats2400To14400Connections, mdmLineCapabilitiesV34=mdmLineCapabilitiesV34, mdmConformance=mdmConformance, mdmCCCallSetUpFailTimer=mdmCCCallSetUpFailTimer, mdmLineCapabilitiesMNP7=mdmLineCapabilitiesMNP7, mdmLineTable=mdmLineTable, mdmSCEntry=mdmSCEntry, mdmCCStoredDialString=mdmCCStoredDialString, mdmLineCapabilitiesMNP10=mdmLineCapabilitiesMNP10, mdmLineCapabilitiesMNP4=mdmLineCapabilitiesMNP4, mdmLineCapabilitiesID=mdmLineCapabilitiesID, mdmStatsSentDataFrames=mdmStatsSentDataFrames, mdmLineCapabilitiesBell208=mdmLineCapabilitiesBell208, mdmECEntry=mdmECEntry, mdmLineCapabilitiesV42=mdmLineCapabilitiesV42, mdmLineCapabilitiesV23SC=mdmLineCapabilitiesV23SC, mdmLineInterfaceGroup=mdmLineInterfaceGroup, mdmCCResultCodeEnable=mdmCCResultCodeEnable, mdmIDGroup=mdmIDGroup, mdmLineCapabilitiesV26ter=mdmLineCapabilitiesV26ter, mdmLineCapabilitiesEnableGranted=mdmLineCapabilitiesEnableGranted, mdmStatsCompressedConnections=mdmStatsCompressedConnections, mdmLineCapabilitiesV32terbo=mdmLineCapabilitiesV32terbo, mdmGroups=mdmGroups, mdmIDProductDetails=mdmIDProductDetails, mdmLineCapabilitiesV32bis=mdmLineCapabilitiesV32bis, mdmDTESyncTimingSource=mdmDTESyncTimingSource, mdmLineCapabilitiesTable=mdmLineCapabilitiesTable, mdmIndex=mdmIndex, mdmLineCapabilitiesV27ter=mdmLineCapabilitiesV27ter, mdmStatsCompressionEfficiency=mdmStatsCompressionEfficiency, mdmCallControlGroup=mdmCallControlGroup, mdmCCStoredDialStringTable=mdmCCStoredDialStringTable, mdmDataCompressionGroup=mdmDataCompressionGroup, mdmStatsReceivedOctets=mdmStatsReceivedOctets, mdmStatsTable=mdmStatsTable, mdmLineCapabilities=mdmLineCapabilities, mdmStatsOutgoingConnectionCompletions=mdmStatsOutgoingConnectionCompletions, mdmLineCapabilitiesMNP8=mdmLineCapabilitiesMNP8, mdmECErrorControlUsed=mdmECErrorControlUsed, mdmMIBObjects=mdmMIBObjects, mdmLineCapabilitiesV26bis=mdmLineCapabilitiesV26bis, mdmDTEActionDTROnToOff=mdmDTEActionDTROnToOff, mdmDTEActionDTROffToOn=mdmDTEActionDTROffToOn, mdmStatsResentFrames=mdmStatsResentFrames)
