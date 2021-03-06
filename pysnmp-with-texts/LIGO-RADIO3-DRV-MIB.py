#
# PySNMP MIB module LIGO-RADIO3-DRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIGO-RADIO3-DRV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:07:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ligoMgmt, = mibBuilder.importSymbols("LIGOWAVE-MIB", "ligoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
NotificationType, iso, Integer32, TimeTicks, Bits, IpAddress, Counter64, ModuleIdentity, Gauge32, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Integer32", "TimeTicks", "Bits", "IpAddress", "Counter64", "ModuleIdentity", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
ligoRadio3DrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32750, 3, 8))
ligoRadio3DrvMIB.setRevisions(('2010-01-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ligoRadio3DrvMIB.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: ligoRadio3DrvMIB.setLastUpdated('201001060000Z')
if mibBuilder.loadTexts: ligoRadio3DrvMIB.setOrganization('LigoWave')
if mibBuilder.loadTexts: ligoRadio3DrvMIB.setContactInfo(' LigoWave Customer Support E-mail: support@ligowave.com')
if mibBuilder.loadTexts: ligoRadio3DrvMIB.setDescription('LigoWave 3 series radio driver MIB.')
ligoRadio3DrvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1))
ligoRdo3DrvNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0))
ligoRdo3DrvInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 1))
ligoRdo3DrvConf = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 2))
ligoRdo3DrvStats = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3))
ligoRdo3StatsTable = MibTable((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1), )
if mibBuilder.loadTexts: ligoRdo3StatsTable.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3StatsTable.setDescription("Radio driver's information and network traffic statistics table.")
ligoRdo3StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "LIGO-RADIO3-DRV-MIB", "ligoRdo3Endpoint"))
if mibBuilder.loadTexts: ligoRdo3StatsEntry.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3StatsEntry.setDescription("Radio driver's information and network traffic statistics table entry.")
ligoRdo3Endpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ligoRdo3Endpoint.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3Endpoint.setDescription('Peer index. Local device has index 0.')
ligoRdo3LastUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3LastUpdate.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3LastUpdate.setDescription('sysUptime value of time point when statistics was gathered.')
ligoRdo3MacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3MacAddress.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3MacAddress.setDescription("Device's MAC address.")
ligoRdo3IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3IpAddress.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3IpAddress.setDescription("Device's IP address.")
ligoRdo3CountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3CountryCode.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3CountryCode.setDescription('Country code.')
ligoRdo3Encryption = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Encryption.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3Encryption.setDescription('Encryption type.')
ligoRdo3Parameters = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Parameters.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3Parameters.setDescription('Radio parameters.')
ligoRdo3Capabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Capabilities.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3Capabilities.setDescription('Radio capabilities.')
ligoRdo3TxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPower.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxPower.setDescription('Transmission power.')
ligoRdo3TxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPackets.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxPackets.setDescription('Number of transmitted packets.')
ligoRdo3TxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxBytes.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxBytes.setDescription('Number of transmitted bytes.')
ligoRdo3TxXmitFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxXmitFailed.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxXmitFailed.setDescription('Number of packets failing initial checks before sending them to radio hardware.')
ligoRdo3TxXmitDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxXmitDropped.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxXmitDropped.setDescription('Number of packets dropped because radio was offline or in reset state.')
ligoRdo3TxOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxOverruns.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxOverruns.setDescription('Number of transmission overruns.')
ligoRdo3TxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxSuccess.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxSuccess.setDescription('Number of successfully transmitted packets.')
ligoRdo3TxFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxFailed.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxFailed.setDescription('Number of transmission failures.')
ligoRdo3TxRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxRetried.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxRetried.setDescription('Number of transmission retries.')
ligoRdo3TxNotRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxNotRetried.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxNotRetried.setDescription('Number of packets sent without retries.')
ligoRdo3TxPacketsPerMcs = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPacketsPerMcs.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxPacketsPerMcs.setDescription('Number of packets sent using each of Modulation and Coding Schemes.')
ligoRdo3TxMsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxMsdus.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxMsdus.setDescription('Number of transmitted MAC Service Data Units.')
ligoRdo3TxNotAggregated = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxNotAggregated.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxNotAggregated.setDescription('Number of packets transmitted without aggregation.')
ligoRdo3TxAckRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAckRequired.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxAckRequired.setDescription('Number of packets transmitted which required acknowledgment.')
ligoRdo3TxNoAckRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxNoAckRequired.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxNoAckRequired.setDescription('Number of packets transmitted which did not require acknowledgment.')
ligoRdo3TxAltRate = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAltRate.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxAltRate.setDescription('Number of data rate alterations.')
ligoRdo3TxManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxManagement.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxManagement.setDescription('Number of transmitted management frames.')
ligoRdo3TxLegacy = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxLegacy.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxLegacy.setDescription('Number of transmitted legacy packets.')
ligoRdo3TxLegacyBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxLegacyBytes.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxLegacyBytes.setDescription('Number of bytes transmitted in legacy mode.')
ligoRdo3TxAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAmsdus.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxAmsdus.setDescription('Number of transmitted aggregated MAC Service Data Units.')
ligoRdo3TxPktsInAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxPktsInAmsdus.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxPktsInAmsdus.setDescription('Number of packets contained in transmitted aggregated MAC Service Data Units.')
ligoRdo3TxAmsduBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxAmsduBytes.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxAmsduBytes.setDescription('Number of bytes transmitted in aggregated MAC Service Data Units.')
ligoRdo3TxMpdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxMpdus.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxMpdus.setDescription('Number of transmitted MAC Protocol Data Units.')
ligoRdo3TxMpduBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxMpduBytes.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxMpduBytes.setDescription('Number of bytes transmitted in MAC Protocol Data Units.')
ligoRdo3TxFragmented = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxFragmented.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxFragmented.setDescription('Number of transmitted fragmented packets.')
ligoRdo3TxFragBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3TxFragBytes.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxFragBytes.setDescription('Number of bytes transmitted in fragmented packets.')
ligoRdo3RxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxPackets.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxPackets.setDescription('Number of received packets.')
ligoRdo3RxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxBytes.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxBytes.setDescription('Number of received bytes.')
ligoRdo3RxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxDropped.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxDropped.setDescription('Number of dropped packets.')
ligoRdo3RxCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxCrcErrors.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxCrcErrors.setDescription('Number of received packets that failed CRC check.')
ligoRdo3RxIcvErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxIcvErrors.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxIcvErrors.setDescription('Number of received packets with invalid Integrity Check Value.')
ligoRdo3RxMicErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxMicErrors.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxMicErrors.setDescription('Number of received packets failing Message Integrity Code check.')
ligoRdo3RxKeyNotValid = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxKeyNotValid.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxKeyNotValid.setDescription('Number of received packets with encryption key errors.')
ligoRdo3RxAclDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxAclDiscarded.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxAclDiscarded.setDescription('Number of received packets discarded by Access Control List check.')
ligoRdo3RxManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxManagement.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxManagement.setDescription('Number of received management packets.')
ligoRdo3RxControl = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxControl.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxControl.setDescription('Number of received control packets.')
ligoRdo3RxData = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxData.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxData.setDescription('Number of received data packets.')
ligoRdo3RxUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxUnknown.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxUnknown.setDescription('Number of received packets of unknown type.')
ligoRdo3RxNullData = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxNullData.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxNullData.setDescription('Number of received NULL DATA frames.')
ligoRdo3RxBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxBroadcast.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxBroadcast.setDescription('Number of received broadcast packets.')
ligoRdo3RxMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxMulticast.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxMulticast.setDescription('Number of received multicast packets.')
ligoRdo3RxUnicast = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxUnicast.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxUnicast.setDescription('Number of received unicast packets.')
ligoRdo3RxCck = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxCck.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxCck.setDescription('Number of packets received using Complementary Code Keying modulation.')
ligoRdo3RxOfdm = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 52), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxOfdm.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxOfdm.setDescription('Number of packets received using Orthogonal Frequency-Division Multiplexing modulation.')
ligoRdo3RxHtMixedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 53), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxHtMixedMode.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxHtMixedMode.setDescription('Number of packets received using High Throughput mixed mode.')
ligoRdo3RxHtGreenfield = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 54), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxHtGreenfield.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxHtGreenfield.setDescription('Number of packets received using High Throughput Greenfield mode.')
ligoRdo3RxAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 55), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxAmsdus.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxAmsdus.setDescription('Number of received aggregated MAC Service Data Units.')
ligoRdo3RxPacketsInAmsdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 56), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxPacketsInAmsdus.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxPacketsInAmsdus.setDescription('Number of packets received in aggregated MAC Service Data Units.')
ligoRdo3RxAmpdus = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 57), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxAmpdus.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxAmpdus.setDescription('Number of received aggregated MAC Protocol Data Units.')
ligoRdo3RxMpduBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 58), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxMpduBytes.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxMpduBytes.setDescription('Number of bytes received in MAC Protocol Data Units.')
ligoRdo3RxRoBufTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 59), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufTotal.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufTotal.setDescription('Total number of received packets moved into reordering buffer.')
ligoRdo3RxRoBufInSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufInSeq.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufInSeq.setDescription('Number of packets in reordering buffer which are in sequence.')
ligoRdo3RxRoBufDup = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufDup.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufDup.setDescription('Number of duplicate packets in reordering buffer.')
ligoRdo3RxRoBufExpired = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufExpired.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufExpired.setDescription('Number of expired packets in reordering buffer.')
ligoRdo3RxRoBufBuffered = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufBuffered.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufBuffered.setDescription('Number of packets held in reordering buffer.')
ligoRdo3RxRoBufReordered = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufReordered.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufReordered.setDescription('Number of packets reordered in reordering buffer.')
ligoRdo3RxRoBufFlushed = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufFlushed.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufFlushed.setDescription('Number of packets flushed from reordering buffer.')
ligoRdo3RxRoBufTooBig = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxRoBufTooBig.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxRoBufTooBig.setDescription('Number of oversized packets dropped from reordering buffer.')
ligoRdo3RxL2Pad = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 67), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxL2Pad.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxL2Pad.setDescription('Number of packets received with padding between header and payload.')
ligoRdo3RxBlockAcks = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 68), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxBlockAcks.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxBlockAcks.setDescription('Number of received block acknowledgments.')
ligoRdo3RxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 69), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxFragments.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxFragments.setDescription('Number of received fragmented packets.')
ligoRdo3RxStbc = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 70), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxStbc.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxStbc.setDescription('Number of packets received using Space-Time Block Coding technique.')
ligoRdo3RxShortGuardInt = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 71), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxShortGuardInt.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxShortGuardInt.setDescription('Number of packets received with Short Guard Interval.')
ligoRdo3Rx40MhzBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 72), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3Rx40MhzBandwidth.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3Rx40MhzBandwidth.setDescription('Number of packets received using 40MHz bandwidth.')
ligoRdo3RxHtControl = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 73), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxHtControl.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxHtControl.setDescription('Number of packets received using High Throughput encoding.')
ligoRdo3RxPacketsPerMcs = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 74), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxPacketsPerMcs.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxPacketsPerMcs.setDescription('Number of packets received using each of Modulation and Coding Schemes.')
ligoRdo3RxLastSigLevel0 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 75), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel0.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel0.setDescription('Reception signal level on antenna 0.')
ligoRdo3RxLastSigLevel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 76), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel1.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel1.setDescription('Reception signal level on antenna 1.')
ligoRdo3RxLastSigLevel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 77), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel2.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxLastSigLevel2.setDescription('Reception signal level on antenna 2.')
ligoRdo3RxNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 78), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxNoise.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxNoise.setDescription('Reception noise.')
ligoRdo3RxLastSnr0 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 79), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSnr0.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxLastSnr0.setDescription('Last registered signal-to-noise level on antenna 0.')
ligoRdo3RxLastSnr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 3, 1, 1, 80), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoRdo3RxLastSnr1.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxLastSnr1.setDescription('Last registered signal-to-noise level on antenna 1.')
ligoRdo3RxDropsThreshold = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3MacAddress"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3RxDropped"))
if mibBuilder.loadTexts: ligoRdo3RxDropsThreshold.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3RxDropsThreshold.setDescription('This notification is sent when percentage of frames dropped in relation to number of frames received over the same time period reaches the threshold.')
ligoRdo3TxRetriesThreshold = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 8, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3MacAddress"), ("LIGO-RADIO3-DRV-MIB", "ligoRdo3TxRetried"))
if mibBuilder.loadTexts: ligoRdo3TxRetriesThreshold.setStatus('current')
if mibBuilder.loadTexts: ligoRdo3TxRetriesThreshold.setDescription('This notification is sent when percentage of transmission retries in relation to number of frames transmitted over the same time period reaches the threshold.')
mibBuilder.exportSymbols("LIGO-RADIO3-DRV-MIB", ligoRdo3MacAddress=ligoRdo3MacAddress, ligoRdo3RxHtControl=ligoRdo3RxHtControl, ligoRdo3TxNotAggregated=ligoRdo3TxNotAggregated, ligoRdo3TxAckRequired=ligoRdo3TxAckRequired, ligoRdo3DrvStats=ligoRdo3DrvStats, ligoRadio3DrvMIB=ligoRadio3DrvMIB, ligoRdo3StatsTable=ligoRdo3StatsTable, ligoRdo3RxDropped=ligoRdo3RxDropped, ligoRdo3RxUnicast=ligoRdo3RxUnicast, ligoRdo3TxFailed=ligoRdo3TxFailed, ligoRdo3RxDropsThreshold=ligoRdo3RxDropsThreshold, ligoRdo3TxPacketsPerMcs=ligoRdo3TxPacketsPerMcs, ligoRdo3RxControl=ligoRdo3RxControl, ligoRdo3RxData=ligoRdo3RxData, ligoRdo3RxLastSnr0=ligoRdo3RxLastSnr0, ligoRdo3IpAddress=ligoRdo3IpAddress, ligoRdo3DrvInfo=ligoRdo3DrvInfo, ligoRdo3TxFragBytes=ligoRdo3TxFragBytes, ligoRdo3RxMulticast=ligoRdo3RxMulticast, ligoRdo3RxRoBufInSeq=ligoRdo3RxRoBufInSeq, ligoRdo3TxManagement=ligoRdo3TxManagement, ligoRdo3RxManagement=ligoRdo3RxManagement, ligoRdo3CountryCode=ligoRdo3CountryCode, ligoRdo3RxUnknown=ligoRdo3RxUnknown, ligoRdo3RxBlockAcks=ligoRdo3RxBlockAcks, ligoRdo3RxLastSigLevel2=ligoRdo3RxLastSigLevel2, ligoRdo3StatsEntry=ligoRdo3StatsEntry, ligoRdo3TxMpdus=ligoRdo3TxMpdus, ligoRdo3RxPacketsPerMcs=ligoRdo3RxPacketsPerMcs, ligoRdo3TxSuccess=ligoRdo3TxSuccess, ligoRdo3RxShortGuardInt=ligoRdo3RxShortGuardInt, ligoRdo3Parameters=ligoRdo3Parameters, ligoRdo3RxRoBufTotal=ligoRdo3RxRoBufTotal, ligoRdo3TxBytes=ligoRdo3TxBytes, ligoRdo3TxMpduBytes=ligoRdo3TxMpduBytes, ligoRdo3RxPacketsInAmsdus=ligoRdo3RxPacketsInAmsdus, ligoRdo3RxLastSigLevel1=ligoRdo3RxLastSigLevel1, ligoRdo3DrvNotifs=ligoRdo3DrvNotifs, ligoRdo3Encryption=ligoRdo3Encryption, ligoRdo3RxLastSnr1=ligoRdo3RxLastSnr1, ligoRdo3RxLastSigLevel0=ligoRdo3RxLastSigLevel0, ligoRdo3RxCrcErrors=ligoRdo3RxCrcErrors, ligoRdo3RxRoBufTooBig=ligoRdo3RxRoBufTooBig, ligoRdo3RxAmpdus=ligoRdo3RxAmpdus, ligoRdo3RxNullData=ligoRdo3RxNullData, ligoRadio3DrvMIBObjects=ligoRadio3DrvMIBObjects, ligoRdo3TxLegacy=ligoRdo3TxLegacy, ligoRdo3RxOfdm=ligoRdo3RxOfdm, ligoRdo3RxRoBufFlushed=ligoRdo3RxRoBufFlushed, ligoRdo3TxAltRate=ligoRdo3TxAltRate, ligoRdo3TxXmitFailed=ligoRdo3TxXmitFailed, ligoRdo3RxL2Pad=ligoRdo3RxL2Pad, ligoRdo3RxMicErrors=ligoRdo3RxMicErrors, ligoRdo3RxRoBufReordered=ligoRdo3RxRoBufReordered, ligoRdo3RxAclDiscarded=ligoRdo3RxAclDiscarded, ligoRdo3TxAmsduBytes=ligoRdo3TxAmsduBytes, ligoRdo3LastUpdate=ligoRdo3LastUpdate, ligoRdo3TxPackets=ligoRdo3TxPackets, ligoRdo3TxAmsdus=ligoRdo3TxAmsdus, ligoRdo3Capabilities=ligoRdo3Capabilities, PYSNMP_MODULE_ID=ligoRadio3DrvMIB, ligoRdo3RxBytes=ligoRdo3RxBytes, ligoRdo3TxRetriesThreshold=ligoRdo3TxRetriesThreshold, ligoRdo3RxNoise=ligoRdo3RxNoise, ligoRdo3RxKeyNotValid=ligoRdo3RxKeyNotValid, ligoRdo3TxPktsInAmsdus=ligoRdo3TxPktsInAmsdus, ligoRdo3RxRoBufDup=ligoRdo3RxRoBufDup, ligoRdo3RxHtGreenfield=ligoRdo3RxHtGreenfield, ligoRdo3RxStbc=ligoRdo3RxStbc, ligoRdo3TxFragmented=ligoRdo3TxFragmented, ligoRdo3RxAmsdus=ligoRdo3RxAmsdus, ligoRdo3RxHtMixedMode=ligoRdo3RxHtMixedMode, ligoRdo3TxNotRetried=ligoRdo3TxNotRetried, ligoRdo3RxIcvErrors=ligoRdo3RxIcvErrors, ligoRdo3TxXmitDropped=ligoRdo3TxXmitDropped, ligoRdo3TxRetried=ligoRdo3TxRetried, ligoRdo3TxMsdus=ligoRdo3TxMsdus, ligoRdo3RxMpduBytes=ligoRdo3RxMpduBytes, ligoRdo3RxRoBufExpired=ligoRdo3RxRoBufExpired, ligoRdo3TxPower=ligoRdo3TxPower, ligoRdo3RxRoBufBuffered=ligoRdo3RxRoBufBuffered, ligoRdo3DrvConf=ligoRdo3DrvConf, ligoRdo3RxBroadcast=ligoRdo3RxBroadcast, ligoRdo3TxOverruns=ligoRdo3TxOverruns, ligoRdo3TxNoAckRequired=ligoRdo3TxNoAckRequired, ligoRdo3TxLegacyBytes=ligoRdo3TxLegacyBytes, ligoRdo3Endpoint=ligoRdo3Endpoint, ligoRdo3RxFragments=ligoRdo3RxFragments, ligoRdo3RxCck=ligoRdo3RxCck, ligoRdo3Rx40MhzBandwidth=ligoRdo3Rx40MhzBandwidth, ligoRdo3RxPackets=ligoRdo3RxPackets)
