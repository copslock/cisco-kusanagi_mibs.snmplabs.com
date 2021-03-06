#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-HuntGroupMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-HuntGroupMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:21:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
Integer32, DisplayString, Unsigned32, StorageType, Counter32, RowStatus = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "Integer32", "DisplayString", "Unsigned32", "StorageType", "Counter32", "RowStatus")
AsciiString, Link = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "AsciiString", "Link")
mscComponents, mscPassportMIBs = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscComponents", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, MibIdentifier, Bits, Unsigned32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, NotificationType, Counter32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibIdentifier", "Bits", "Unsigned32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "NotificationType", "Counter32", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
huntGroupMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130))
mscHg = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131))
mscHgRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1), )
if mibBuilder.loadTexts: mscHgRowStatusTable.setStatus('mandatory')
mscHgRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgRowStatusEntry.setStatus('mandatory')
mscHgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgRowStatus.setStatus('mandatory')
mscHgComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgComponentName.setStatus('mandatory')
mscHgStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgStorageType.setStatus('mandatory')
mscHgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: mscHgIndex.setStatus('mandatory')
mscHgCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10), )
if mibBuilder.loadTexts: mscHgCidDataTable.setStatus('mandatory')
mscHgCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgCidDataEntry.setStatus('mandatory')
mscHgCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgCustomerIdentifier.setStatus('mandatory')
mscHgNsapAddressTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11), )
if mibBuilder.loadTexts: mscHgNsapAddressTable.setStatus('mandatory')
mscHgNsapAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgNsapAddressEntry.setStatus('mandatory')
mscHgAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgAddress.setStatus('mandatory')
mscHgProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12), )
if mibBuilder.loadTexts: mscHgProvTable.setStatus('mandatory')
mscHgProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgProvEntry.setStatus('mandatory')
mscHgLogicalProcessor = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgLogicalProcessor.setStatus('mandatory')
mscHgSelectionPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("startFromZero", 0), ("rotary", 1), ("mostAvailable", 2))).clone('mostAvailable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgSelectionPolicy.setStatus('mandatory')
mscHgMaxHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)).clone(63)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgMaxHuntAttempts.setStatus('mandatory')
mscHgAppendSuffixDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1))).clone('yes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgAppendSuffixDigits.setStatus('mandatory')
mscHgStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20), )
if mibBuilder.loadTexts: mscHgStateTable.setStatus('mandatory')
mscHgStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgStateEntry.setStatus('mandatory')
mscHgAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgAdminState.setStatus('mandatory')
mscHgOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgOperationalState.setStatus('mandatory')
mscHgUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 20, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgUsageState.setStatus('mandatory')
mscHgOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21), )
if mibBuilder.loadTexts: mscHgOperationalTable.setStatus('mandatory')
mscHgOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"))
if mibBuilder.loadTexts: mscHgOperationalEntry.setStatus('mandatory')
mscHgHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHuntAttempts.setStatus('mandatory')
mscHgFailedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgFailedCalls.setStatus('mandatory')
mscHgInitialHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgInitialHuntAttempts.setStatus('mandatory')
mscHgAvailabilityUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgAvailabilityUpdates.setStatus('mandatory')
mscHgMaxAddrLenExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgMaxAddrLenExceeded.setStatus('mandatory')
mscHgBadPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 21, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgBadPackets.setStatus('mandatory')
mscHgHgM = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2))
mscHgHgMRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1), )
if mibBuilder.loadTexts: mscHgHgMRowStatusTable.setStatus('mandatory')
mscHgHgMRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMRowStatusEntry.setStatus('mandatory')
mscHgHgMRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgHgMRowStatus.setStatus('mandatory')
mscHgHgMComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMComponentName.setStatus('mandatory')
mscHgHgMStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMStorageType.setStatus('mandatory')
mscHgHgMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)))
if mibBuilder.loadTexts: mscHgHgMIndex.setStatus('mandatory')
mscHgHgMProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10), )
if mibBuilder.loadTexts: mscHgHgMProvTable.setStatus('mandatory')
mscHgHgMProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMProvEntry.setStatus('mandatory')
mscHgHgMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgHgMAddress.setStatus('mandatory')
mscHgHgMStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11), )
if mibBuilder.loadTexts: mscHgHgMStateTable.setStatus('mandatory')
mscHgHgMStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMStateEntry.setStatus('mandatory')
mscHgHgMAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMAdminState.setStatus('mandatory')
mscHgHgMOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMOperationalState.setStatus('mandatory')
mscHgHgMUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMUsageState.setStatus('mandatory')
mscHgHgMOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12), )
if mibBuilder.loadTexts: mscHgHgMOperationalTable.setStatus('mandatory')
mscHgHgMOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupMIB", "mscHgHgMIndex"))
if mibBuilder.loadTexts: mscHgHgMOperationalEntry.setStatus('mandatory')
mscHgHgMAvailability = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)).clone(4095)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscHgHgMAvailability.setStatus('mandatory')
mscHgHgMAvailabilityUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMAvailabilityUpdates.setStatus('mandatory')
mscHgHgMCallsRefused = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 131, 2, 12, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscHgHgMCallsRefused.setStatus('mandatory')
huntGroupGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1))
huntGroupGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1))
huntGroupGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1, 3))
huntGroupGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 1, 1, 3, 2))
huntGroupCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3))
huntGroupCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1))
huntGroupCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1, 3))
huntGroupCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 130, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-HuntGroupMIB", huntGroupGroup=huntGroupGroup, mscHgSelectionPolicy=mscHgSelectionPolicy, mscHgMaxHuntAttempts=mscHgMaxHuntAttempts, mscHgHgMCallsRefused=mscHgHgMCallsRefused, mscHgRowStatus=mscHgRowStatus, mscHgFailedCalls=mscHgFailedCalls, mscHgHgMOperationalEntry=mscHgHgMOperationalEntry, mscHgStorageType=mscHgStorageType, mscHgHgMOperationalTable=mscHgHgMOperationalTable, huntGroupCapabilities=huntGroupCapabilities, mscHgHgMUsageState=mscHgHgMUsageState, mscHgAvailabilityUpdates=mscHgAvailabilityUpdates, mscHgHgMRowStatusTable=mscHgHgMRowStatusTable, huntGroupGroupCA=huntGroupGroupCA, mscHgHgM=mscHgHgM, mscHgOperationalEntry=mscHgOperationalEntry, mscHgHgMRowStatusEntry=mscHgHgMRowStatusEntry, mscHgHgMStateTable=mscHgHgMStateTable, huntGroupCapabilitiesCA=huntGroupCapabilitiesCA, mscHgHgMComponentName=mscHgHgMComponentName, huntGroupGroupCA02A=huntGroupGroupCA02A, mscHgHgMIndex=mscHgHgMIndex, mscHgInitialHuntAttempts=mscHgInitialHuntAttempts, mscHgIndex=mscHgIndex, mscHgHgMRowStatus=mscHgHgMRowStatus, mscHgHgMProvTable=mscHgHgMProvTable, huntGroupGroupCA02=huntGroupGroupCA02, mscHgBadPackets=mscHgBadPackets, mscHgRowStatusTable=mscHgRowStatusTable, mscHgMaxAddrLenExceeded=mscHgMaxAddrLenExceeded, mscHgLogicalProcessor=mscHgLogicalProcessor, mscHgOperationalTable=mscHgOperationalTable, mscHgHgMAddress=mscHgHgMAddress, mscHgHgMProvEntry=mscHgHgMProvEntry, mscHgNsapAddressTable=mscHgNsapAddressTable, mscHgHgMStateEntry=mscHgHgMStateEntry, mscHgStateEntry=mscHgStateEntry, mscHgHgMAvailability=mscHgHgMAvailability, huntGroupMIB=huntGroupMIB, mscHgOperationalState=mscHgOperationalState, huntGroupCapabilitiesCA02A=huntGroupCapabilitiesCA02A, mscHgAdminState=mscHgAdminState, mscHgProvTable=mscHgProvTable, mscHgCidDataEntry=mscHgCidDataEntry, mscHg=mscHg, mscHgCidDataTable=mscHgCidDataTable, mscHgUsageState=mscHgUsageState, mscHgAddress=mscHgAddress, mscHgHgMOperationalState=mscHgHgMOperationalState, mscHgHuntAttempts=mscHgHuntAttempts, mscHgHgMAdminState=mscHgHgMAdminState, mscHgHgMAvailabilityUpdates=mscHgHgMAvailabilityUpdates, huntGroupCapabilitiesCA02=huntGroupCapabilitiesCA02, mscHgProvEntry=mscHgProvEntry, mscHgNsapAddressEntry=mscHgNsapAddressEntry, mscHgHgMStorageType=mscHgHgMStorageType, mscHgCustomerIdentifier=mscHgCustomerIdentifier, mscHgStateTable=mscHgStateTable, mscHgAppendSuffixDigits=mscHgAppendSuffixDigits, mscHgRowStatusEntry=mscHgRowStatusEntry, mscHgComponentName=mscHgComponentName)
