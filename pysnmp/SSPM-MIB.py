#
# PySNMP MIB module SSPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SSPM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
AppLocalIndex, = mibBuilder.importSymbols("APM-MIB", "AppLocalIndex")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
OwnerString, rmon = mibBuilder.importSymbols("RMON-MIB", "OwnerString", "rmon")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, ModuleIdentity, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, IpAddress, Gauge32, TimeTicks, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "ModuleIdentity", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "IpAddress", "Gauge32", "TimeTicks", "Bits", "NotificationType", "ObjectIdentity")
StorageType, DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
Utf8String, = mibBuilder.importSymbols("SYSAPPL-MIB", "Utf8String")
sspmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 28))
sspmMIB.setRevisions(('2005-07-28 00:00',))
if mibBuilder.loadTexts: sspmMIB.setLastUpdated('200507280000Z')
if mibBuilder.loadTexts: sspmMIB.setOrganization('IETF RMON MIB working group')
sspmMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 1))
sspmMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 2))
sspmMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 3))
class SspmMicroSeconds(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class SspmClockSource(TextualConvention, Integer32):
    reference = 'RFC1305.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class SspmClockMaxSkew(TextualConvention, Integer32):
    reference = 'RFC1305.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

sspmGeneral = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 1, 1))
sspmGeneralClockResolution = MibScalar((1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 1), SspmMicroSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmGeneralClockResolution.setStatus('current')
sspmGeneralClockMaxSkew = MibScalar((1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 2), SspmClockMaxSkew()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmGeneralClockMaxSkew.setStatus('current')
sspmGeneralClockSource = MibScalar((1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 3), SspmClockSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmGeneralClockSource.setStatus('current')
sspmGeneralMinFrequency = MibScalar((1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 4), SspmMicroSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmGeneralMinFrequency.setStatus('current')
sspmCapabilitiesTable = MibTable((1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5), )
if mibBuilder.loadTexts: sspmCapabilitiesTable.setStatus('current')
sspmCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5, 1), ).setIndexNames((0, "SSPM-MIB", "sspmCapabilitiesInstance"))
if mibBuilder.loadTexts: sspmCapabilitiesEntry.setStatus('current')
sspmCapabilitiesInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5, 1, 1), AppLocalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmCapabilitiesInstance.setStatus('current')
sspmSource = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 1, 2))
sspmSourceProfileTable = MibTable((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1), )
if mibBuilder.loadTexts: sspmSourceProfileTable.setStatus('current')
sspmSourceProfileEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1), ).setIndexNames((0, "SSPM-MIB", "sspmSourceProfileInstance"))
if mibBuilder.loadTexts: sspmSourceProfileEntry.setStatus('current')
sspmSourceProfileInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: sspmSourceProfileInstance.setStatus('current')
sspmSourceProfileType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 2), AppLocalIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileType.setStatus('current')
sspmSourceProfilePacketSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfilePacketSize.setStatus('current')
sspmSourceProfilePacketFillType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("random", 1), ("pattern", 2), ("url", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfilePacketFillType.setStatus('current')
sspmSourceProfilePacketFillValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfilePacketFillValue.setStatus('current')
sspmSourceProfileTOS = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileTOS.setStatus('current')
sspmSourceProfileFlowLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileFlowLabel.setStatus('current')
sspmSourceProfileLooseSrcRteFill = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 240))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileLooseSrcRteFill.setStatus('current')
sspmSourceProfileLooseSrcRteLen = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileLooseSrcRteLen.setStatus('current')
sspmSourceProfileTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileTTL.setStatus('current')
sspmSourceProfileNoFrag = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 11), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileNoFrag.setStatus('current')
sspmSourceProfile8021Tagging = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfile8021Tagging.setStatus('current')
sspmSourceProfileUsername = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 13), Utf8String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileUsername.setStatus('current')
sspmSourceProfilePassword = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 14), Utf8String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfilePassword.setStatus('current')
sspmSourceProfileParameter = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileParameter.setStatus('current')
sspmSourceProfileOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 16), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileOwner.setStatus('current')
sspmSourceProfileStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 17), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileStorageType.setStatus('current')
sspmSourceProfileStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceProfileStatus.setStatus('current')
sspmSourceControlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2), )
if mibBuilder.loadTexts: sspmSourceControlTable.setStatus('current')
sspmSourceControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1), ).setIndexNames((0, "SSPM-MIB", "sspmSourceControlInstance"))
if mibBuilder.loadTexts: sspmSourceControlEntry.setStatus('current')
sspmSourceControlInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: sspmSourceControlInstance.setStatus('current')
sspmSourceControlProfile = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlProfile.setStatus('current')
sspmSourceControlSrc = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlSrc.setStatus('current')
sspmSourceControlDestAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlDestAddrType.setStatus('current')
sspmSourceControlDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlDestAddr.setStatus('current')
sspmSourceControlEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlEnabled.setStatus('current')
sspmSourceControlTimeOut = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 7), SspmMicroSeconds()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlTimeOut.setStatus('current')
sspmSourceControlSamplingDist = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deterministic", 1), ("poisson", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlSamplingDist.setStatus('current')
sspmSourceControlFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 9), SspmMicroSeconds()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlFrequency.setStatus('current')
sspmSourceControlFirstSeqNum = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlFirstSeqNum.setStatus('current')
sspmSourceControlLastSeqNum = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmSourceControlLastSeqNum.setStatus('current')
sspmSourceControlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 12), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlOwner.setStatus('current')
sspmSourceControlStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 13), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlStorageType.setStatus('current')
sspmSourceControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSourceControlStatus.setStatus('current')
sspmSink = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 1, 5))
sspmSinkTable = MibTable((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1), )
if mibBuilder.loadTexts: sspmSinkTable.setStatus('current')
sspmSinkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1), ).setIndexNames((0, "SSPM-MIB", "sspmSinkInstance"))
if mibBuilder.loadTexts: sspmSinkEntry.setStatus('current')
sspmSinkInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: sspmSinkInstance.setStatus('current')
sspmSinkType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 2), AppLocalIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkType.setStatus('current')
sspmSinkSourceAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkSourceAddressType.setStatus('current')
sspmSinkSourceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkSourceAddress.setStatus('current')
sspmSinkExpectedRate = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 5), SspmMicroSeconds()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkExpectedRate.setStatus('current')
sspmSinkEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkEnable.setStatus('current')
sspmSinkExpectedFirstSequenceNum = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkExpectedFirstSequenceNum.setStatus('current')
sspmSinkLastSequenceNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmSinkLastSequenceNumber.setStatus('current')
sspmSinkLastSequenceInvalid = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sspmSinkLastSequenceInvalid.setStatus('current')
sspmSinkStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 10), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkStorageType.setStatus('current')
sspmSinkStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sspmSinkStatus.setStatus('current')
sspmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 3, 1))
sspmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 28, 3, 2))
sspmGeneralCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 28, 3, 1, 1)).setObjects(("SSPM-MIB", "sspmGeneralGroup"), ("SSPM-MIB", "sspmSourceGroup"), ("SSPM-MIB", "sspmSinkGroup"), ("SSPM-MIB", "sspmUserPassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sspmGeneralCompliance = sspmGeneralCompliance.setStatus('current')
sspmSourceFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 28, 3, 1, 2)).setObjects(("SSPM-MIB", "sspmGeneralGroup"), ("SSPM-MIB", "sspmSourceGroup"), ("SSPM-MIB", "sspmUserPassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sspmSourceFullCompliance = sspmSourceFullCompliance.setStatus('current')
sspmSinkFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 28, 3, 1, 3)).setObjects(("SSPM-MIB", "sspmGeneralGroup"), ("SSPM-MIB", "sspmSinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sspmSinkFullCompliance = sspmSinkFullCompliance.setStatus('current')
sspmGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 1)).setObjects(("SSPM-MIB", "sspmGeneralClockResolution"), ("SSPM-MIB", "sspmGeneralClockMaxSkew"), ("SSPM-MIB", "sspmGeneralClockSource"), ("SSPM-MIB", "sspmGeneralMinFrequency"), ("SSPM-MIB", "sspmCapabilitiesInstance"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sspmGeneralGroup = sspmGeneralGroup.setStatus('current')
sspmSourceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 2)).setObjects(("SSPM-MIB", "sspmSourceProfileType"), ("SSPM-MIB", "sspmSourceProfilePacketSize"), ("SSPM-MIB", "sspmSourceProfilePacketFillType"), ("SSPM-MIB", "sspmSourceProfilePacketFillValue"), ("SSPM-MIB", "sspmSourceProfileTOS"), ("SSPM-MIB", "sspmSourceProfileFlowLabel"), ("SSPM-MIB", "sspmSourceProfileLooseSrcRteFill"), ("SSPM-MIB", "sspmSourceProfileLooseSrcRteLen"), ("SSPM-MIB", "sspmSourceProfileTTL"), ("SSPM-MIB", "sspmSourceProfileNoFrag"), ("SSPM-MIB", "sspmSourceProfile8021Tagging"), ("SSPM-MIB", "sspmSourceProfileUsername"), ("SSPM-MIB", "sspmSourceProfilePassword"), ("SSPM-MIB", "sspmSourceProfileParameter"), ("SSPM-MIB", "sspmSourceProfileOwner"), ("SSPM-MIB", "sspmSourceProfileStorageType"), ("SSPM-MIB", "sspmSourceProfileStatus"), ("SSPM-MIB", "sspmSourceControlProfile"), ("SSPM-MIB", "sspmSourceControlSrc"), ("SSPM-MIB", "sspmSourceControlDestAddrType"), ("SSPM-MIB", "sspmSourceControlDestAddr"), ("SSPM-MIB", "sspmSourceControlEnabled"), ("SSPM-MIB", "sspmSourceControlTimeOut"), ("SSPM-MIB", "sspmSourceControlSamplingDist"), ("SSPM-MIB", "sspmSourceControlFrequency"), ("SSPM-MIB", "sspmSourceControlFirstSeqNum"), ("SSPM-MIB", "sspmSourceControlLastSeqNum"), ("SSPM-MIB", "sspmSourceControlOwner"), ("SSPM-MIB", "sspmSourceControlStorageType"), ("SSPM-MIB", "sspmSourceControlStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sspmSourceGroup = sspmSourceGroup.setStatus('current')
sspmUserPassGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 3)).setObjects(("SSPM-MIB", "sspmSourceProfileUsername"), ("SSPM-MIB", "sspmSourceProfilePassword"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sspmUserPassGroup = sspmUserPassGroup.setStatus('current')
sspmSinkGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 4)).setObjects(("SSPM-MIB", "sspmSinkType"), ("SSPM-MIB", "sspmSinkSourceAddressType"), ("SSPM-MIB", "sspmSinkSourceAddress"), ("SSPM-MIB", "sspmSinkExpectedRate"), ("SSPM-MIB", "sspmSinkEnable"), ("SSPM-MIB", "sspmSinkExpectedFirstSequenceNum"), ("SSPM-MIB", "sspmSinkLastSequenceNumber"), ("SSPM-MIB", "sspmSinkLastSequenceInvalid"), ("SSPM-MIB", "sspmSinkStorageType"), ("SSPM-MIB", "sspmSinkStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sspmSinkGroup = sspmSinkGroup.setStatus('current')
mibBuilder.exportSymbols("SSPM-MIB", sspmSinkInstance=sspmSinkInstance, sspmSinkLastSequenceNumber=sspmSinkLastSequenceNumber, sspmMIBNotifications=sspmMIBNotifications, sspmGeneralMinFrequency=sspmGeneralMinFrequency, sspmSourceControlSrc=sspmSourceControlSrc, sspmSinkFullCompliance=sspmSinkFullCompliance, sspmSourceProfileLooseSrcRteFill=sspmSourceProfileLooseSrcRteFill, sspmSourceControlDestAddr=sspmSourceControlDestAddr, sspmGeneralClockMaxSkew=sspmGeneralClockMaxSkew, sspmSourceProfileType=sspmSourceProfileType, sspmUserPassGroup=sspmUserPassGroup, sspmMIBObjects=sspmMIBObjects, SspmMicroSeconds=SspmMicroSeconds, sspmGeneralClockResolution=sspmGeneralClockResolution, sspmSinkStorageType=sspmSinkStorageType, sspmSourceProfilePacketFillType=sspmSourceProfilePacketFillType, sspmSinkEntry=sspmSinkEntry, sspmSourceProfilePacketSize=sspmSourceProfilePacketSize, sspmSourceControlInstance=sspmSourceControlInstance, sspmSourceProfileEntry=sspmSourceProfileEntry, sspmSinkTable=sspmSinkTable, sspmSourceProfileFlowLabel=sspmSourceProfileFlowLabel, sspmSourceControlFrequency=sspmSourceControlFrequency, sspmSinkStatus=sspmSinkStatus, sspmSinkGroup=sspmSinkGroup, sspmGeneral=sspmGeneral, sspmSourceControlLastSeqNum=sspmSourceControlLastSeqNum, sspmSource=sspmSource, sspmSourceProfileTTL=sspmSourceProfileTTL, sspmSourceProfileOwner=sspmSourceProfileOwner, sspmSink=sspmSink, sspmSourceControlSamplingDist=sspmSourceControlSamplingDist, sspmCapabilitiesTable=sspmCapabilitiesTable, sspmMIB=sspmMIB, sspmGeneralCompliance=sspmGeneralCompliance, sspmSinkSourceAddressType=sspmSinkSourceAddressType, sspmMIBConformance=sspmMIBConformance, sspmSourceControlOwner=sspmSourceControlOwner, sspmCapabilitiesEntry=sspmCapabilitiesEntry, sspmSinkType=sspmSinkType, sspmSinkExpectedFirstSequenceNum=sspmSinkExpectedFirstSequenceNum, sspmSourceFullCompliance=sspmSourceFullCompliance, sspmSourceProfileInstance=sspmSourceProfileInstance, sspmSourceProfilePassword=sspmSourceProfilePassword, sspmSinkEnable=sspmSinkEnable, sspmGeneralGroup=sspmGeneralGroup, sspmSourceControlEnabled=sspmSourceControlEnabled, sspmSourceProfileStatus=sspmSourceProfileStatus, sspmSourceProfileNoFrag=sspmSourceProfileNoFrag, sspmSourceControlStorageType=sspmSourceControlStorageType, sspmSourceProfileTOS=sspmSourceProfileTOS, sspmCapabilitiesInstance=sspmCapabilitiesInstance, sspmSourceControlStatus=sspmSourceControlStatus, sspmSourceControlTable=sspmSourceControlTable, sspmSinkLastSequenceInvalid=sspmSinkLastSequenceInvalid, PYSNMP_MODULE_ID=sspmMIB, sspmCompliances=sspmCompliances, sspmSourceProfileParameter=sspmSourceProfileParameter, sspmSourceProfilePacketFillValue=sspmSourceProfilePacketFillValue, sspmSourceProfileTable=sspmSourceProfileTable, sspmSourceProfileLooseSrcRteLen=sspmSourceProfileLooseSrcRteLen, sspmSourceControlEntry=sspmSourceControlEntry, sspmSinkExpectedRate=sspmSinkExpectedRate, sspmSourceProfileStorageType=sspmSourceProfileStorageType, sspmSourceControlProfile=sspmSourceControlProfile, sspmSourceControlFirstSeqNum=sspmSourceControlFirstSeqNum, sspmGroups=sspmGroups, sspmSinkSourceAddress=sspmSinkSourceAddress, sspmSourceGroup=sspmSourceGroup, sspmSourceControlTimeOut=sspmSourceControlTimeOut, SspmClockSource=SspmClockSource, sspmSourceProfileUsername=sspmSourceProfileUsername, sspmSourceControlDestAddrType=sspmSourceControlDestAddrType, sspmSourceProfile8021Tagging=sspmSourceProfile8021Tagging, SspmClockMaxSkew=SspmClockMaxSkew, sspmGeneralClockSource=sspmGeneralClockSource)
