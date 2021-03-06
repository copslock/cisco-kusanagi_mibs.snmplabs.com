#
# PySNMP MIB module ASCEND-VOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-VOIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
voipGroup, = mibBuilder.importSymbols("ASCEND-MIB", "voipGroup")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, ModuleIdentity, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ObjectIdentity, MibIdentifier, Gauge32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ModuleIdentity", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ObjectIdentity", "MibIdentifier", "Gauge32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
voipCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 28, 1))
voipCfgGkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 28, 1, 1))
voipCfgGwGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 28, 1, 2))
voipCfgGkTable = MibTable((1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1), )
if mibBuilder.loadTexts: voipCfgGkTable.setStatus('mandatory')
if mibBuilder.loadTexts: voipCfgGkTable.setDescription('A list of entries for H323 network Gatekeeper.')
voipCfgGkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1), ).setIndexNames((0, "ASCEND-VOIP-MIB", "voipCfgGkIndex"))
if mibBuilder.loadTexts: voipCfgGkEntry.setStatus('mandatory')
if mibBuilder.loadTexts: voipCfgGkEntry.setDescription('An entry holding information about the Gatekeepers for the system.')
voipCfgGkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipCfgGkIndex.setStatus('mandatory')
if mibBuilder.loadTexts: voipCfgGkIndex.setDescription('This number uniquely identifies the Gatekeeper.')
voipCfgGkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("registered", 1), ("not-registered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipCfgGkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: voipCfgGkStatus.setDescription('This value indicates whether the gateway is registered with the Gatekeeper.')
voipCfgGkIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipCfgGkIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: voipCfgGkIpAddress.setDescription('The IP address of the Gatekeeper.')
voipCfgGwVpnMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 28, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipCfgGwVpnMode.setStatus('mandatory')
if mibBuilder.loadTexts: voipCfgGwVpnMode.setDescription('Virtual Private Network Toggle Switch.')
voipCfgGwPktAudioMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 28, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("g711-ulaw", 2), ("g711-alaw", 3), ("g723", 4), ("g729", 5), ("g723-6-4kps", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voipCfgGwPktAudioMode.setStatus('mandatory')
if mibBuilder.loadTexts: voipCfgGwPktAudioMode.setDescription('Audio Coder to be used for voice packetization.')
mibBuilder.exportSymbols("ASCEND-VOIP-MIB", voipCfgGwPktAudioMode=voipCfgGwPktAudioMode, voipCfgGkIpAddress=voipCfgGkIpAddress, voipCfgGkEntry=voipCfgGkEntry, voipCfgGroup=voipCfgGroup, voipCfgGkGroup=voipCfgGkGroup, voipCfgGkTable=voipCfgGkTable, voipCfgGkIndex=voipCfgGkIndex, voipCfgGwVpnMode=voipCfgGwVpnMode, voipCfgGwGroup=voipCfgGwGroup, voipCfgGkStatus=voipCfgGkStatus)
