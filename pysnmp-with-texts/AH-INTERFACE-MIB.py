#
# PySNMP MIB module AH-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AH-INTERFACE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:15:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
AhNodeID, AhMACProtocol, ahAPInterface, AhString, AhInterfaceMode, AhInterfaceType = mibBuilder.importSymbols("AH-SMI-MIB", "AhNodeID", "AhMACProtocol", "ahAPInterface", "AhString", "AhInterfaceMode", "AhInterfaceType")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, IpAddress, TimeTicks, Gauge32, Counter32, NotificationType, MibIdentifier, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "IpAddress", "TimeTicks", "Gauge32", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Bits")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ahInterface = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: ahInterface.setLastUpdated('200806160000Z')
if mibBuilder.loadTexts: ahInterface.setOrganization('Aerohive Networks, Inc')
if mibBuilder.loadTexts: ahInterface.setContactInfo('info@aerohive.com 330 Gibraltar Drive Sunnyvale CA, 94089')
if mibBuilder.loadTexts: ahInterface.setDescription('This module contains the MIB definition of interface related information.')
class AhAuthenticationMethod(TextualConvention, Integer32):
    description = 'Authentication method supported within Aerohive AP'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("cwp", 0), ("open", 1), ("wep-open", 2), ("wep-shared", 3), ("wpa-psk", 4), ("wpa2-psk", 5), ("wpa-8021x", 6), ("wpa2-8021X", 7), ("wpa-auto-psk", 8), ("wpa-auto-8021x", 9), ("dynamic-wep", 10))

class AhEncrytionMethod(TextualConvention, Integer32):
    description = 'Encryption method supported within Aerohive AP'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("AES", 0), ("TKIP", 1), ("WEP", 2), ("Non", 3))

ahXIfTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: ahXIfTable.setStatus('current')
if mibBuilder.loadTexts: ahXIfTable.setDescription('Table of all the Interface/SSID info not covered by the rfc 2863')
ahXIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1), )
ifEntry.registerAugmentions(("AH-INTERFACE-MIB", "ahXIfEntry"))
ahXIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: ahXIfEntry.setStatus('current')
if mibBuilder.loadTexts: ahXIfEntry.setDescription('Individual entry of Interface/SSID table')
ahIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 1), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfName.setStatus('current')
if mibBuilder.loadTexts: ahIfName.setDescription('Name - uniquely identifies an AP Interface.')
ahSSIDName = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 2), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSSIDName.setStatus('current')
if mibBuilder.loadTexts: ahSSIDName.setDescription('Name - identifies a wireless interface with Access mode. If the interface is not a wireless interface with Access mode, the SSIDName should be set N/A')
ahIfPromiscuous = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfPromiscuous.setStatus('current')
if mibBuilder.loadTexts: ahIfPromiscuous.setDescription('Indicates whether an interface is in promiscuous mode or not.')
ahIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 4), AhInterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfType.setStatus('current')
if mibBuilder.loadTexts: ahIfType.setDescription('Indicates whether an interface is a physical or virtual one.')
ahIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 5), AhInterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfMode.setStatus('current')
if mibBuilder.loadTexts: ahIfMode.setDescription('Indicates whether an interface is used for Access or Backhaul currently.')
ahIfConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 6), AhInterfaceMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahIfConfMode.setStatus('current')
if mibBuilder.loadTexts: ahIfConfMode.setDescription('Indicates whether an interface is configured for Access or Backhaul.')
ahAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2), )
if mibBuilder.loadTexts: ahAssociationTable.setStatus('current')
if mibBuilder.loadTexts: ahAssociationTable.setDescription('Table of directly connected APs')
ahAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "AH-INTERFACE-MIB", "ahClientMac"))
if mibBuilder.loadTexts: ahAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: ahAssociationEntry.setDescription('Individual entry of client table')
ahClientMac = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 1), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientMac.setStatus('current')
if mibBuilder.loadTexts: ahClientMac.setDescription('Uniquely identifies a client.')
ahClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientIP.setStatus('current')
if mibBuilder.loadTexts: ahClientIP.setDescription('The IP address of the client if known. Otherwise, this field should be 0')
ahClientHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 3), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientHostname.setStatus('current')
if mibBuilder.loadTexts: ahClientHostname.setDescription('The host name of the client if known. Otherwise, this field should be empty')
ahClientRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRSSI.setStatus('current')
if mibBuilder.loadTexts: ahClientRSSI.setDescription('An indicator for the RSSI of the client derived from last communication')
ahClientLinkUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLinkUptime.setStatus('current')
if mibBuilder.loadTexts: ahClientLinkUptime.setDescription('Link up time in second')
ahClientCWPUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientCWPUsed.setStatus('current')
if mibBuilder.loadTexts: ahClientCWPUsed.setDescription('The boolean indicating whether Captive Web Portal is used.')
ahClientAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 7), AhAuthenticationMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientAuthMethod.setStatus('current')
if mibBuilder.loadTexts: ahClientAuthMethod.setDescription('The authentication method the client uses to communicated with AP')
ahClientEncryptionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 8), AhEncrytionMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientEncryptionMethod.setStatus('current')
if mibBuilder.loadTexts: ahClientEncryptionMethod.setDescription('The encryption method the client uses to communicated with AP')
ahClientMACProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 9), AhMACProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientMACProtocol.setStatus('current')
if mibBuilder.loadTexts: ahClientMACProtocol.setDescription('The radio mode the client uses to communicated with AP')
ahClientSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 10), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientSSID.setStatus('current')
if mibBuilder.loadTexts: ahClientSSID.setDescription('The SSID used by client to communicated with AP')
ahClientVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientVLAN.setStatus('current')
if mibBuilder.loadTexts: ahClientVLAN.setDescription('The VLAN used by client to communicated with AP')
ahClientUserProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientUserProfId.setStatus('current')
if mibBuilder.loadTexts: ahClientUserProfId.setDescription('The user profile id used by client to communicated with AP')
ahClientChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientChannel.setStatus('current')
if mibBuilder.loadTexts: ahClientChannel.setDescription('The radio channel used by client to communicated with AP')
ahClientLastTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLastTxRate.setStatus('current')
if mibBuilder.loadTexts: ahClientLastTxRate.setDescription('The rate (KBPS) of last transmitting frame to the client.')
ahClientUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 15), AhString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientUsername.setStatus('current')
if mibBuilder.loadTexts: ahClientUsername.setDescription('The client user name to login to the network. It contain empty string if the authentication method is other than EAP (802.1x).')
ahClientRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxDataFrames.setDescription('The number of data frames received from client to AP')
ahClientRxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxDataOctets.setStatus('current')
if mibBuilder.loadTexts: ahClientRxDataOctets.setDescription('The number of data octets received from client to AP')
ahClientRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxMgtFrames.setDescription('The number of mgt frames received from client to AP')
ahClientRxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxUnicastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxUnicastFrames.setDescription('The number of unitcast frames received from client to AP')
ahClientRxMulticastFrames = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxMulticastFrames.setDescription('The number of multicast frames received from client to AP.')
ahClientRxBroadcastFrames = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxBroadcastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientRxBroadcastFrames.setDescription('The number of broadcast frames received from client to AP.')
ahClientRxMICFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxMICFailures.setStatus('current')
if mibBuilder.loadTexts: ahClientRxMICFailures.setDescription('The number of frames dropped due to Message Integrity Check failure from client to AP.')
ahClientTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxDataFrames.setDescription('The number of transmitted data frames from .')
ahClientTxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxMgtFrames.setDescription('The number of transmitted management frames from .')
ahClientTxDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxDataOctets.setStatus('current')
if mibBuilder.loadTexts: ahClientTxDataOctets.setDescription('The number of transmitted data in octets from .')
ahClientTxUnicastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxUnicastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxUnicastFrames.setDescription('The number of unitcast frames transmitted from client to AP')
ahClientTxMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxMulticastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxMulticastFrames.setDescription('The number of multicast frames transmitted from client to AP')
ahClientTxBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBroadcastFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxBroadcastFrames.setDescription('The number of broadcast frames transmitted from client to AP')
ahClientLastRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientLastRxRate.setStatus('current')
if mibBuilder.loadTexts: ahClientLastRxRate.setDescription('The rate (KBPS) of last received frame from client.')
ahClientTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBeDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxBeDataFrames.setDescription('The number of transmitted best effort priority data frames from AP to client.')
ahClientTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxBgDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxBgDataFrames.setDescription('The number of transmitted back ground priority data frames from AP to client.')
ahClientTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxViDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxViDataFrames.setDescription('The number of transmitted video priority data frames from AP to client.')
ahClientTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxVoDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahClientTxVoDataFrames.setDescription('The number of transmitted voice priority data frames from AP to client.')
ahClientTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientTxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahClientTxAirtime.setDescription('The accumulative transmit time in microseconds () from AP to client.')
ahClientRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientRxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahClientRxAirtime.setDescription('The accumulative receive time in microseconds (us) from client to AP.')
ahClientAssociationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientAssociationTime.setStatus('current')
if mibBuilder.loadTexts: ahClientAssociationTime.setDescription('The association time(s) of client connect to AP.')
ahClientBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 37), AhNodeID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientBSSID.setStatus('current')
if mibBuilder.loadTexts: ahClientBSSID.setDescription('It is the basic service set identifier of the client.')
ahRadioStatsTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3), )
if mibBuilder.loadTexts: ahRadioStatsTable.setStatus('current')
if mibBuilder.loadTexts: ahRadioStatsTable.setDescription('Table of radio interface statistics.')
ahRadioStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahRadioStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ahRadioStatsEntry.setDescription('Individual entry of client table')
ahRadioTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxDataFrames.setDescription('The number of transmit data frames for the given interface.')
ahRadioTxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxUnicastDataFrames.setDescription('The number of transmitted unicast frames for the given interface.')
ahRadioTxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxMulticastDataFrames.setDescription('The number of transmitted multicast frames for the given interface.')
ahRadioTxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBroadcastDataFrames.setDescription('The number of transmitted broadcast frames for the given interface.')
ahRadioTxNonBeaconMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxNonBeaconMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxNonBeaconMgtFrames.setDescription('The number of transmit management frames other than beacon for the given interface.')
ahRadioTxBeaconFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBeaconFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBeaconFrames.setDescription('The number of transmit beacon frames for the given interface.')
ahRadioTxTotalRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalRetries.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxTotalRetries.setDescription('The total number of transmit retries for the given interface.')
ahRadioTxTotalFramesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalFramesDropped.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxTotalFramesDropped.setDescription('The number of transmit frames dropped for the given interface.')
ahRadioTxTotalFrameErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxTotalFrameErrors.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxTotalFrameErrors.setDescription('The total number of transmit frames in error for the given interface.')
ahRadioTxFEForExcessiveHWRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxFEForExcessiveHWRetries.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxFEForExcessiveHWRetries.setDescription('The number of transmit frames in error due to excessive hardware retries for the given interface.')
ahRadioRxTotalDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxTotalDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxTotalDataFrames.setDescription('The total number of received data frames for the given interface.')
ahRadioRxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxUnicastDataFrames.setDescription('The number of received unicast frames for the given interface.')
ahRadioRxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxMulticastDataFrames.setDescription('The number of received multicast frames for the given interface.')
ahRadioRxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxBroadcastDataFrames.setDescription('The number of received broadcast frames for the given interface.')
ahRadioRxMgtFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxMgtFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxMgtFrames.setDescription('The number of received management frames for the given interface.')
ahRadioRxTotalFrameDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxTotalFrameDropped.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxTotalFrameDropped.setDescription('The total number of dropped received frames for the given interface.')
ahRadioTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBeDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBeDataFrames.setDescription('The number of transmitted best effort priority data frames from the radio.')
ahRadioTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxBgDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxBgDataFrames.setDescription('The number of transmitted back ground priority data frames from the radio.')
ahRadioTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxViDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxViDataFrames.setDescription('The number of transmitted video priority data frames from the radio.')
ahRadioTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxVoDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxVoDataFrames.setDescription('The number of transmitted voice priority data frames from the radio.')
ahRadioTXRTSFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTXRTSFailures.setStatus('current')
if mibBuilder.loadTexts: ahRadioTXRTSFailures.setDescription('The number of transmitted RTS failures from the Radio.')
ahRadioTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxAirtime.setDescription('The accumulative transmit time in microseconds (us) from the given Radio.')
ahRadioRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioRxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahRadioRxAirtime.setDescription('The accumulative receive time in microseconds (us) to the given radio.')
ahVIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4), )
if mibBuilder.loadTexts: ahVIfStatsTable.setStatus('current')
if mibBuilder.loadTexts: ahVIfStatsTable.setDescription('Table of virtual interface (vif) statistics.')
ahVIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahVIfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ahVIfStatsEntry.setDescription('Individual entry of VIf statistics')
ahVIfRxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxDataFrames.setDescription('The number of received data frames for the given virtual interface.')
ahVIfRxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxUnicastDataFrames.setDescription('The number of received unicast data frames for the given virtual interface.')
ahVIfRxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxMulticastDataFrames.setDescription('The number of received multicast data frames for the given virtual interface.')
ahVIfRxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxBroadcastDataFrames.setDescription('The number of received broadcast data frames for the given virtual interface.')
ahVIfRxErrorFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxErrorFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxErrorFrames.setDescription('The number of received error frames for the given virtual interface.')
ahVIfRxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfRxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfRxDroppedFrames.setDescription('The number of received dropped frames for the given virtual interface.')
ahVIfTxDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxDataFrames.setDescription('The number of trasmitted data frames for the given virtual interface.')
ahVIfTxUnicastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxUnicastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxUnicastDataFrames.setDescription('The number of transmitted unicast data frames for the given virtual interface.')
ahVIfTxMulticastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxMulticastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxMulticastDataFrames.setDescription('The number of transmitted multicast data frames for the given virtual interface.')
ahVIfTxBroadcastDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBroadcastDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxBroadcastDataFrames.setDescription('The number of transmitted broadcast data frames for the given virtual interface.')
ahVIfTxErrorFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxErrorFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxErrorFrames.setDescription('The number of trasmitted frames encontered error for the given virtual interface.')
ahVIfTxDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxDroppedFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxDroppedFrames.setDescription('The number of trasmitted frames dropped due to error condition for the given virtual interface.')
ahVIfTxBeDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBeDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxBeDataFrames.setDescription('The number of transmitted best effort priority data frames from the virtual interface.')
ahVIfTxBgDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxBgDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxBgDataFrames.setDescription('The number of transmitted back ground priority data frames from the virtual interface.')
ahVIfTxViDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxViDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxViDataFrames.setDescription('The number of transmitted video priority data frames from the virtual interface.')
ahVIfTxVoDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVIfTxVoDataFrames.setStatus('current')
if mibBuilder.loadTexts: ahVIfTxVoDataFrames.setDescription('The number of transmitted voice priority data frames from the virtual interface.')
ahVifTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVifTxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahVifTxAirtime.setDescription('The accumulative transmit time in microseconds (us) from the given SSID.')
ahVifRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahVifRxAirtime.setStatus('current')
if mibBuilder.loadTexts: ahVifRxAirtime.setDescription('The accumulative receive time in microseconds (us) to the given SSID.')
ahRadioAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5), )
if mibBuilder.loadTexts: ahRadioAttributeTable.setStatus('current')
if mibBuilder.loadTexts: ahRadioAttributeTable.setDescription('Table of radio interface statistics.')
ahRadioAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ahRadioAttributeEntry.setStatus('current')
if mibBuilder.loadTexts: ahRadioAttributeEntry.setDescription('Individual entry for each Radio')
ahRadioChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioChannel.setStatus('current')
if mibBuilder.loadTexts: ahRadioChannel.setDescription('The channel number currently in use for this radio.')
ahRadioTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioTxPower.setStatus('current')
if mibBuilder.loadTexts: ahRadioTxPower.setDescription('The transmit power currently for the radio in dbm. The range is 0 to 20 dBm')
ahRadioNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahRadioNoiseFloor.setStatus('current')
if mibBuilder.loadTexts: ahRadioNoiseFloor.setDescription('The noise floor for the radio dbm. The range is 0 to 256 dBm. The value of this variable is the actual value plus 256 dBm.')
mibBuilder.exportSymbols("AH-INTERFACE-MIB", ahClientLastTxRate=ahClientLastTxRate, ahInterface=ahInterface, ahVIfTxBroadcastDataFrames=ahVIfTxBroadcastDataFrames, ahRadioTxBeaconFrames=ahRadioTxBeaconFrames, ahClientChannel=ahClientChannel, ahIfMode=ahIfMode, ahRadioNoiseFloor=ahRadioNoiseFloor, ahRadioTxTotalFramesDropped=ahRadioTxTotalFramesDropped, ahRadioTxNonBeaconMgtFrames=ahRadioTxNonBeaconMgtFrames, ahClientRSSI=ahClientRSSI, ahClientMac=ahClientMac, ahClientBSSID=ahClientBSSID, ahClientRxMulticastFrames=ahClientRxMulticastFrames, AhAuthenticationMethod=AhAuthenticationMethod, ahRadioTxMulticastDataFrames=ahRadioTxMulticastDataFrames, ahXIfTable=ahXIfTable, ahXIfEntry=ahXIfEntry, ahClientIP=ahClientIP, ahIfName=ahIfName, ahAssociationEntry=ahAssociationEntry, ahRadioRxMulticastDataFrames=ahRadioRxMulticastDataFrames, ahClientLastRxRate=ahClientLastRxRate, ahRadioTxBeDataFrames=ahRadioTxBeDataFrames, ahVIfRxUnicastDataFrames=ahVIfRxUnicastDataFrames, ahClientLinkUptime=ahClientLinkUptime, ahClientAuthMethod=ahClientAuthMethod, ahRadioChannel=ahRadioChannel, ahClientRxMICFailures=ahClientRxMICFailures, ahClientTxDataFrames=ahClientTxDataFrames, ahRadioTxVoDataFrames=ahRadioTxVoDataFrames, ahClientRxMgtFrames=ahClientRxMgtFrames, ahVIfRxDataFrames=ahVIfRxDataFrames, ahVIfRxDroppedFrames=ahVIfRxDroppedFrames, ahClientVLAN=ahClientVLAN, ahRadioRxMgtFrames=ahRadioRxMgtFrames, ahRadioTxTotalFrameErrors=ahRadioTxTotalFrameErrors, AhEncrytionMethod=AhEncrytionMethod, ahIfType=ahIfType, ahIfConfMode=ahIfConfMode, ahRadioStatsTable=ahRadioStatsTable, ahClientMACProtocol=ahClientMACProtocol, ahClientTxBroadcastFrames=ahClientTxBroadcastFrames, ahClientAssociationTime=ahClientAssociationTime, ahSSIDName=ahSSIDName, ahVIfRxBroadcastDataFrames=ahVIfRxBroadcastDataFrames, ahClientUsername=ahClientUsername, ahRadioTxDataFrames=ahRadioTxDataFrames, ahClientEncryptionMethod=ahClientEncryptionMethod, ahClientSSID=ahClientSSID, ahVIfStatsEntry=ahVIfStatsEntry, ahRadioAttributeTable=ahRadioAttributeTable, ahClientTxDataOctets=ahClientTxDataOctets, ahClientUserProfId=ahClientUserProfId, ahClientTxBeDataFrames=ahClientTxBeDataFrames, ahClientTxViDataFrames=ahClientTxViDataFrames, ahClientCWPUsed=ahClientCWPUsed, ahRadioRxTotalFrameDropped=ahRadioRxTotalFrameDropped, ahRadioTXRTSFailures=ahRadioTXRTSFailures, ahVIfTxVoDataFrames=ahVIfTxVoDataFrames, PYSNMP_MODULE_ID=ahInterface, ahAssociationTable=ahAssociationTable, ahClientRxBroadcastFrames=ahClientRxBroadcastFrames, ahVIfStatsTable=ahVIfStatsTable, ahVIfTxMulticastDataFrames=ahVIfTxMulticastDataFrames, ahVIfRxMulticastDataFrames=ahVIfRxMulticastDataFrames, ahClientTxAirtime=ahClientTxAirtime, ahClientTxVoDataFrames=ahClientTxVoDataFrames, ahIfPromiscuous=ahIfPromiscuous, ahVIfTxDataFrames=ahVIfTxDataFrames, ahClientTxBgDataFrames=ahClientTxBgDataFrames, ahClientRxUnicastFrames=ahClientRxUnicastFrames, ahRadioTxUnicastDataFrames=ahRadioTxUnicastDataFrames, ahVIfTxDroppedFrames=ahVIfTxDroppedFrames, ahRadioTxFEForExcessiveHWRetries=ahRadioTxFEForExcessiveHWRetries, ahClientTxMulticastFrames=ahClientTxMulticastFrames, ahRadioRxUnicastDataFrames=ahRadioRxUnicastDataFrames, ahVIfTxViDataFrames=ahVIfTxViDataFrames, ahRadioTxAirtime=ahRadioTxAirtime, ahClientHostname=ahClientHostname, ahVIfTxBeDataFrames=ahVIfTxBeDataFrames, ahRadioTxTotalRetries=ahRadioTxTotalRetries, ahVIfRxErrorFrames=ahVIfRxErrorFrames, ahClientTxUnicastFrames=ahClientTxUnicastFrames, ahRadioTxPower=ahRadioTxPower, ahClientRxAirtime=ahClientRxAirtime, ahVIfTxErrorFrames=ahVIfTxErrorFrames, ahVifRxAirtime=ahVifRxAirtime, ahRadioRxAirtime=ahRadioRxAirtime, ahClientRxDataFrames=ahClientRxDataFrames, ahRadioStatsEntry=ahRadioStatsEntry, ahClientTxMgtFrames=ahClientTxMgtFrames, ahVifTxAirtime=ahVifTxAirtime, ahVIfTxUnicastDataFrames=ahVIfTxUnicastDataFrames, ahRadioRxTotalDataFrames=ahRadioRxTotalDataFrames, ahRadioAttributeEntry=ahRadioAttributeEntry, ahRadioTxBgDataFrames=ahRadioTxBgDataFrames, ahRadioTxViDataFrames=ahRadioTxViDataFrames, ahRadioTxBroadcastDataFrames=ahRadioTxBroadcastDataFrames, ahVIfTxBgDataFrames=ahVIfTxBgDataFrames, ahRadioRxBroadcastDataFrames=ahRadioRxBroadcastDataFrames, ahClientRxDataOctets=ahClientRxDataOctets)
