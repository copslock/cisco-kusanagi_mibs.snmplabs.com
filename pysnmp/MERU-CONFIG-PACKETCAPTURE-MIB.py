#
# PySNMP MIB module MERU-CONFIG-PACKETCAPTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-PACKETCAPTURE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlRxTxOption, MwlEncapsulationType, MwlPacketCaptureMode, MwlRateLimitMode, MwlEnableDisableOption, MwlOnOffSwitch = mibBuilder.importSymbols("MERU-TC", "MwlRxTxOption", "MwlEncapsulationType", "MwlPacketCaptureMode", "MwlRateLimitMode", "MwlEnableDisableOption", "MwlOnOffSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Counter32, enterprises, TimeTicks, NotificationType, Unsigned32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Counter32", "enterprises", "TimeTicks", "NotificationType", "Unsigned32", "Counter64", "Integer32")
DisplayString, RowStatus, DateAndTime, TimeInterval, TimeStamp, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TimeInterval", "TimeStamp", "MacAddress", "TruthValue", "TextualConvention")
mwConfigPacketCapture = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17))
if mibBuilder.loadTexts: mwConfigPacketCapture.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigPacketCapture.setOrganization('Meru Networks')
mwPacketCaptureProfileTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1), )
if mibBuilder.loadTexts: mwPacketCaptureProfileTable.setStatus('current')
mwPacketCaptureProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1), ).setIndexNames((0, "MERU-CONFIG-PACKETCAPTURE-MIB", "mwPacketCaptureProfileTableIndex"))
if mibBuilder.loadTexts: mwPacketCaptureProfileEntry.setStatus('current')
mwPacketCaptureProfileTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwPacketCaptureProfileTableIndex.setStatus('current')
mwPacketCaptureProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileName.setStatus('current')
mwPacketCaptureProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 3), MwlEnableDisableOption()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileStatus.setStatus('current')
mwPacketCaptureProfileConnectivityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 4), MwlPacketCaptureMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileConnectivityMode.setStatus('current')
mwPacketCaptureProfileDestinationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileDestinationIp.setStatus('current')
mwPacketCaptureProfileUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileUDPPort.setStatus('current')
mwPacketCaptureProfileDestinationMac = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileDestinationMac.setStatus('current')
mwPacketCaptureProfileRxTx = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 8), MwlRxTxOption()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwPacketCaptureProfileRxTx.setStatus('current')
mwPacketCaptureProfileRateLimitMode = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 9), MwlRateLimitMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileRateLimitMode.setStatus('current')
mwPacketCaptureProfileTokenBucketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileTokenBucketRate.setStatus('current')
mwPacketCaptureProfileTokenBucketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileTokenBucketSize.setStatus('current')
mwPacketCaptureProfileApList = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileApList.setStatus('current')
mwPacketCaptureProfileFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileFilter.setStatus('current')
mwPacketCaptureProfileInterfaceList = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileInterfaceList.setStatus('current')
mwPacketCaptureProfilePacketTruncationLength = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfilePacketTruncationLength.setStatus('current')
mwPacketCaptureProfileRateLimiting = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 16), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileRateLimiting.setStatus('current')
mwPacketCaptureProfileCaptureSiblingFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 17), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileCaptureSiblingFrames.setStatus('current')
mwPacketCaptureProfileEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 18), MwlEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileEncapsulation.setStatus('current')
mwPacketCaptureProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 17, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwPacketCaptureProfileRowStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-PACKETCAPTURE-MIB", mwPacketCaptureProfileTokenBucketRate=mwPacketCaptureProfileTokenBucketRate, mwPacketCaptureProfileFilter=mwPacketCaptureProfileFilter, mwPacketCaptureProfileTableIndex=mwPacketCaptureProfileTableIndex, mwPacketCaptureProfileConnectivityMode=mwPacketCaptureProfileConnectivityMode, mwPacketCaptureProfileUDPPort=mwPacketCaptureProfileUDPPort, mwPacketCaptureProfileInterfaceList=mwPacketCaptureProfileInterfaceList, mwPacketCaptureProfileEncapsulation=mwPacketCaptureProfileEncapsulation, mwPacketCaptureProfileTable=mwPacketCaptureProfileTable, mwPacketCaptureProfileEntry=mwPacketCaptureProfileEntry, mwPacketCaptureProfileName=mwPacketCaptureProfileName, mwPacketCaptureProfileDestinationMac=mwPacketCaptureProfileDestinationMac, mwPacketCaptureProfileTokenBucketSize=mwPacketCaptureProfileTokenBucketSize, mwPacketCaptureProfileRateLimiting=mwPacketCaptureProfileRateLimiting, PYSNMP_MODULE_ID=mwConfigPacketCapture, mwConfigPacketCapture=mwConfigPacketCapture, mwPacketCaptureProfileCaptureSiblingFrames=mwPacketCaptureProfileCaptureSiblingFrames, mwPacketCaptureProfilePacketTruncationLength=mwPacketCaptureProfilePacketTruncationLength, mwPacketCaptureProfileRxTx=mwPacketCaptureProfileRxTx, mwPacketCaptureProfileApList=mwPacketCaptureProfileApList, mwPacketCaptureProfileRateLimitMode=mwPacketCaptureProfileRateLimitMode, mwPacketCaptureProfileRowStatus=mwPacketCaptureProfileRowStatus, mwPacketCaptureProfileDestinationIp=mwPacketCaptureProfileDestinationIp, mwPacketCaptureProfileStatus=mwPacketCaptureProfileStatus)
