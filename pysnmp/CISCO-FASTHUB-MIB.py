#
# PySNMP MIB module CISCO-FASTHUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FASTHUB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ModuleIdentity, Bits, TimeTicks, Counter32, Integer32, MibIdentifier, ObjectIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ModuleIdentity", "Bits", "TimeTicks", "Counter32", "Integer32", "MibIdentifier", "ObjectIdentity", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoFastHubMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 11))
ciscoFastHubMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 11, 1))
class VisualLEDMap(OctetString):
    pass

mrStack = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1))
mrSupervisorLog = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2))
mrStackUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3))
mrNetMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4))
mrUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5))
mrStackUnitCapacity = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitCapacity.setStatus('mandatory')
mrStackNumberOfUnitsPresent = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackNumberOfUnitsPresent.setStatus('mandatory')
mrStackSelectPrimarySupervisorUnit = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrStackSelectPrimarySupervisorUnit.setStatus('mandatory')
mrStackPOSTSelect = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("abbreviated", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrStackPOSTSelect.setStatus('mandatory')
mrStackReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrStackReset.setStatus('mandatory')
mrStackDefaultReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrStackDefaultReset.setStatus('mandatory')
mrStackClearStatistics = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("noClear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrStackClearStatistics.setStatus('obsolete')
mrStackShortJabberLoopCorrections = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackShortJabberLoopCorrections.setStatus('mandatory')
mrSupervisorLogTableClear = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("noClear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrSupervisorLogTableClear.setStatus('mandatory')
mrSupervisorLogTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2), )
if mibBuilder.loadTexts: mrSupervisorLogTable.setStatus('mandatory')
mrSupervisorLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-FASTHUB-MIB", "mrSupervisorLogIndex"))
if mibBuilder.loadTexts: mrSupervisorLogEntry.setStatus('mandatory')
mrSupervisorLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrSupervisorLogIndex.setStatus('mandatory')
mrSupervisorLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrSupervisorLogTime.setStatus('obsolete')
mrSupervisorLogInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrSupervisorLogInfo.setStatus('mandatory')
mrSupervisorLogRelativeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrSupervisorLogRelativeTime.setStatus('mandatory')
mrStackUnitTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1), )
if mibBuilder.loadTexts: mrStackUnitTable.setStatus('mandatory')
mrStackUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-FASTHUB-MIB", "mrStackUnitIndex"))
if mibBuilder.loadTexts: mrStackUnitEntry.setStatus('mandatory')
mrStackUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitIndex.setStatus('mandatory')
mrStackUnitPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitPresent.setStatus('mandatory')
mrStackUnitFirstGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitFirstGroupIndex.setStatus('mandatory')
mrStackUnitLastGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitLastGroupIndex.setStatus('mandatory')
mrStackUnitSupervisorPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitSupervisorPresent.setStatus('mandatory')
mrStackUnitSupervisorMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitSupervisorMajorVersion.setStatus('mandatory')
mrStackUnitSupervisorMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitSupervisorMinorVersion.setStatus('mandatory')
mrStackUnitSupervisorBootstrapMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitSupervisorBootstrapMajorVersion.setStatus('mandatory')
mrStackUnitSupervisorBootstrapMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitSupervisorBootstrapMinorVersion.setStatus('mandatory')
mrStackUnitPOSTResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitPOSTResult.setStatus('mandatory')
mrStackUnitSupervisorIsPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitSupervisorIsPrimary.setStatus('mandatory')
mrStackUnitExpansionModulePresent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitExpansionModulePresent.setStatus('mandatory')
mrStackUnitPortVisualIndicatorSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("portStatus", 1), ("unitNumber", 2), ("utilization", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitPortVisualIndicatorSelect.setStatus('mandatory')
mrStackUnitBasePortVisualIndicatorGreenMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 14), VisualLEDMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitBasePortVisualIndicatorGreenMap.setStatus('mandatory')
mrStackUnitBasePortVisualIndicatorAmberMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 15), VisualLEDMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitBasePortVisualIndicatorAmberMap.setStatus('mandatory')
mrStackUnitExpansionPortVisualIndicatorGreenMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 16), VisualLEDMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitExpansionPortVisualIndicatorGreenMap.setStatus('mandatory')
mrStackUnitExpansionPortVisualIndicatorAmberMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 17), VisualLEDMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitExpansionPortVisualIndicatorAmberMap.setStatus('mandatory')
mrStackUnitActivityVisualIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitActivityVisualIndicator.setStatus('mandatory')
mrStackUnitCollisionVisualIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitCollisionVisualIndicator.setStatus('mandatory')
mrStackUnitRPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notPresent", 1), ("connectedFunctional", 2), ("connectedNotFunctional", 3), ("functionalPrimaryFailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitRPSStatus.setStatus('mandatory')
mrStackUnitRPSVisualIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("green", 2), ("amber", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitRPSVisualIndicator.setStatus('mandatory')
mrStackUnitSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrStackUnitSerialNumber.setStatus('mandatory')
mrNetMgmtIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtIpAddress.setStatus('mandatory')
mrNetMgmtIpSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtIpSubnetMask.setStatus('mandatory')
mrNetMgmtDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtDefaultGateway.setStatus('mandatory')
mrNetMgmtEnableAuthenTraps = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtEnableAuthenTraps.setStatus('mandatory')
mrNetMgmtEnableRIP = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtEnableRIP.setStatus('mandatory')
mrNetMgmtConsoleInactTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtConsoleInactTime.setStatus('mandatory')
mrNetMgmtConsolePasswordThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtConsolePasswordThreshold.setStatus('mandatory')
mrNetMgmtConsoleSilentTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtConsoleSilentTime.setStatus('mandatory')
mrNetMgmtModemInitString = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtModemInitString.setStatus('mandatory')
mrNetMgmtModemDialString = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtModemDialString.setStatus('mandatory')
mrNetMgmtModemDialDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtModemDialDelay.setStatus('mandatory')
mrNetMgmtModemAutoAnswer = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtModemAutoAnswer.setStatus('mandatory')
mrNetMgmtDomainServer1IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtDomainServer1IpAddress.setStatus('mandatory')
mrNetMgmtDomainServer2IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtDomainServer2IpAddress.setStatus('mandatory')
mrNetMgmtDefaultSearchDomain = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtDefaultSearchDomain.setStatus('mandatory')
mrNetMgmtSetClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17), )
if mibBuilder.loadTexts: mrNetMgmtSetClientTable.setStatus('mandatory')
mrNetMgmtSetClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1), ).setIndexNames((0, "CISCO-FASTHUB-MIB", "mrNetMgmtSetClientIndex"))
if mibBuilder.loadTexts: mrNetMgmtSetClientEntry.setStatus('mandatory')
mrNetMgmtSetClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrNetMgmtSetClientIndex.setStatus('mandatory')
mrNetMgmtSetClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtSetClientName.setStatus('mandatory')
mrNetMgmtSetClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtSetClientStatus.setStatus('mandatory')
mrNetMgmtTrapClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18), )
if mibBuilder.loadTexts: mrNetMgmtTrapClientTable.setStatus('mandatory')
mrNetMgmtTrapClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1), ).setIndexNames((0, "CISCO-FASTHUB-MIB", "mrNetMgmtTrapClientIndex"))
if mibBuilder.loadTexts: mrNetMgmtTrapClientEntry.setStatus('mandatory')
mrNetMgmtTrapClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrNetMgmtTrapClientIndex.setStatus('mandatory')
mrNetMgmtTrapClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtTrapClientName.setStatus('mandatory')
mrNetMgmtTrapClientComm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtTrapClientComm.setStatus('mandatory')
mrNetMgmtTrapClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrNetMgmtTrapClientStatus.setStatus('mandatory')
mrUpgradeFlashSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrUpgradeFlashSize.setStatus('mandatory')
mrUpgradeLastUpgradeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrUpgradeLastUpgradeTime.setStatus('obsolete')
mrUpgradeLastUpgradeSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrUpgradeLastUpgradeSource.setStatus('mandatory')
mrUpgradeLastUpgradeStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("success", 3), ("failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrUpgradeLastUpgradeStatus.setStatus('mandatory')
mrUpgradeTFTPServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrUpgradeTFTPServerAddress.setStatus('mandatory')
mrUpgradeTFTPLoadFilename = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrUpgradeTFTPLoadFilename.setStatus('mandatory')
mrUpgradeTFTPInitiate = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upgrade", 1), ("noUpgrade", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrUpgradeTFTPInitiate.setStatus('mandatory')
mrUpgradeTFTPAccept = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrUpgradeTFTPAccept.setStatus('mandatory')
logonIntruder = NotificationType((1, 3, 6, 1, 4, 1, 9, 2, 11, 1) + (0,0)).setObjects(("SNMPv2-MIB", "sysName"))
hubStackDiagnostic = NotificationType((1, 3, 6, 1, 4, 1, 9, 2, 11, 1) + (0,1)).setObjects(("SNMPv2-MIB", "sysName"))
rpsFailed = NotificationType((1, 3, 6, 1, 4, 1, 9, 2, 11, 1) + (0,2)).setObjects(("SNMPv2-MIB", "sysName"))
ipAddressChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 2, 11, 1) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"))
mibBuilder.exportSymbols("CISCO-FASTHUB-MIB", mrSupervisorLogEntry=mrSupervisorLogEntry, mrNetMgmtIpAddress=mrNetMgmtIpAddress, mrStackUnitLastGroupIndex=mrStackUnitLastGroupIndex, mrStackUnitPOSTResult=mrStackUnitPOSTResult, mrNetMgmtSetClientIndex=mrNetMgmtSetClientIndex, mrStackUnitSupervisorIsPrimary=mrStackUnitSupervisorIsPrimary, mrNetMgmtTrapClientEntry=mrNetMgmtTrapClientEntry, mrStackUnitActivityVisualIndicator=mrStackUnitActivityVisualIndicator, mrNetMgmtTrapClientName=mrNetMgmtTrapClientName, mrStackNumberOfUnitsPresent=mrStackNumberOfUnitsPresent, mrUpgradeTFTPInitiate=mrUpgradeTFTPInitiate, mrNetMgmtModemDialString=mrNetMgmtModemDialString, mrStackUnitFirstGroupIndex=mrStackUnitFirstGroupIndex, mrUpgradeTFTPAccept=mrUpgradeTFTPAccept, mrUpgradeTFTPServerAddress=mrUpgradeTFTPServerAddress, mrStackPOSTSelect=mrStackPOSTSelect, mrStackClearStatistics=mrStackClearStatistics, mrNetMgmtIpSubnetMask=mrNetMgmtIpSubnetMask, mrNetMgmtSetClientTable=mrNetMgmtSetClientTable, ciscoFastHubMIB=ciscoFastHubMIB, mrStackUnitSupervisorMinorVersion=mrStackUnitSupervisorMinorVersion, mrSupervisorLogTime=mrSupervisorLogTime, mrNetMgmtModemInitString=mrNetMgmtModemInitString, mrUpgradeLastUpgradeStatus=mrUpgradeLastUpgradeStatus, mrNetMgmtConsoleInactTime=mrNetMgmtConsoleInactTime, mrNetMgmtTrapClientStatus=mrNetMgmtTrapClientStatus, mrSupervisorLogIndex=mrSupervisorLogIndex, mrSupervisorLogTable=mrSupervisorLogTable, mrSupervisorLogInfo=mrSupervisorLogInfo, mrUpgradeLastUpgradeTime=mrUpgradeLastUpgradeTime, mrUpgrade=mrUpgrade, mrNetMgmtSetClientStatus=mrNetMgmtSetClientStatus, mrStackUnitPortVisualIndicatorSelect=mrStackUnitPortVisualIndicatorSelect, mrStackUnitBasePortVisualIndicatorGreenMap=mrStackUnitBasePortVisualIndicatorGreenMap, mrStackReset=mrStackReset, mrNetMgmtSetClientEntry=mrNetMgmtSetClientEntry, mrStackUnitPresent=mrStackUnitPresent, mrNetMgmtModemDialDelay=mrNetMgmtModemDialDelay, mrStackUnitBasePortVisualIndicatorAmberMap=mrStackUnitBasePortVisualIndicatorAmberMap, rpsFailed=rpsFailed, mrStackUnitSupervisorBootstrapMinorVersion=mrStackUnitSupervisorBootstrapMinorVersion, mrNetMgmtEnableAuthenTraps=mrNetMgmtEnableAuthenTraps, mrStackUnitExpansionPortVisualIndicatorAmberMap=mrStackUnitExpansionPortVisualIndicatorAmberMap, mrNetMgmtSetClientName=mrNetMgmtSetClientName, mrNetMgmtDomainServer2IpAddress=mrNetMgmtDomainServer2IpAddress, mrNetMgmtDomainServer1IpAddress=mrNetMgmtDomainServer1IpAddress, mrNetMgmtConsolePasswordThreshold=mrNetMgmtConsolePasswordThreshold, mrNetMgmtDefaultGateway=mrNetMgmtDefaultGateway, mrSupervisorLogRelativeTime=mrSupervisorLogRelativeTime, VisualLEDMap=VisualLEDMap, mrNetMgmtTrapClientIndex=mrNetMgmtTrapClientIndex, mrStackUnitCapacity=mrStackUnitCapacity, mrNetMgmt=mrNetMgmt, hubStackDiagnostic=hubStackDiagnostic, logonIntruder=logonIntruder, ipAddressChange=ipAddressChange, mrStackUnitExpansionPortVisualIndicatorGreenMap=mrStackUnitExpansionPortVisualIndicatorGreenMap, mrStackUnitSupervisorMajorVersion=mrStackUnitSupervisorMajorVersion, mrStackUnitRPSStatus=mrStackUnitRPSStatus, mrStackUnit=mrStackUnit, mrStack=mrStack, mrStackUnitIndex=mrStackUnitIndex, mrStackUnitSupervisorBootstrapMajorVersion=mrStackUnitSupervisorBootstrapMajorVersion, mrUpgradeLastUpgradeSource=mrUpgradeLastUpgradeSource, mrStackDefaultReset=mrStackDefaultReset, mrSupervisorLog=mrSupervisorLog, mrStackUnitEntry=mrStackUnitEntry, mrUpgradeFlashSize=mrUpgradeFlashSize, mrUpgradeTFTPLoadFilename=mrUpgradeTFTPLoadFilename, mrNetMgmtTrapClientTable=mrNetMgmtTrapClientTable, mrStackShortJabberLoopCorrections=mrStackShortJabberLoopCorrections, mrSupervisorLogTableClear=mrSupervisorLogTableClear, mrNetMgmtEnableRIP=mrNetMgmtEnableRIP, mrNetMgmtDefaultSearchDomain=mrNetMgmtDefaultSearchDomain, mrNetMgmtTrapClientComm=mrNetMgmtTrapClientComm, mrStackUnitExpansionModulePresent=mrStackUnitExpansionModulePresent, ciscoFastHubMIBObjects=ciscoFastHubMIBObjects, mrStackUnitCollisionVisualIndicator=mrStackUnitCollisionVisualIndicator, mrStackUnitRPSVisualIndicator=mrStackUnitRPSVisualIndicator, mrStackUnitTable=mrStackUnitTable, mrNetMgmtModemAutoAnswer=mrNetMgmtModemAutoAnswer, mrStackSelectPrimarySupervisorUnit=mrStackSelectPrimarySupervisorUnit, mrStackUnitSerialNumber=mrStackUnitSerialNumber, mrNetMgmtConsoleSilentTime=mrNetMgmtConsoleSilentTime, mrStackUnitSupervisorPresent=mrStackUnitSupervisorPresent)
