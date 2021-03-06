#
# PySNMP MIB module CISCO-LWAPP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, NotificationType, iso, Counter32, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, Bits, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "NotificationType", "iso", "Counter32", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "Bits", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLwappTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 514))
ciscoLwappTextualConventions.setRevisions(('2011-09-13 00:00', '2007-10-30 00:00', '2007-02-05 00:00', '2006-10-31 00:00', '2006-04-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappTextualConventions.setRevisionsDescriptions(('Added new textual conventions CcxServiceVersion.', 'Added new textual conventions CLApEthernetIfStatus and CLApDot11RadioSubband.', 'Added new textual conventions CLDot11ChannelBandwidth, CLDot11Band and CLApAssocFailureReason.', 'Added new textual conventions CLMfpEventSource, CLCdpAdvtVersionType and CLDot11ClientStatus.', 'Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setLastUpdated('201109130000Z')
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappTextualConventions.setDescription("This module defines textual conventions used throughout the Cisco enterprise MIBs designed for implementation on Central Controllers that terminate the Light Weight Access Point Protocol from LWAPP Access Points. The relationship between CC and the LWAPP APs can be depicted as follows: +......+ +......+ +......+ +......+ + + + + + + + + + CC + + CC + + CC + + CC + + + + + + + + + +......+ +......+ +......+ +......+ .. . . . .. . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + AP + + AP + + AP + + AP + + AP + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + MN + + MN + + MN + + MN + + MN + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and the controller pushes the configuration, that includes the WLAN parameters, to the LWAPP APs. The APs then encapsulate all the 802.11 frames from wireless clients inside LWAPP frames and forward the LWAPP frames to the controller. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends it to the controller to which it is logically connected. Advanced Encryption Standard ( AES ) In cryptography, the Advanced Encryption Standard (AES), also known as Rijndael, is a block cipher adopted as an encryption standard by the US government. It is expected to be used worldwide and analysed extensively, as was the case with its predecessor, the Data Encryption Standard (DES). AES was adopted by National Institute of Standards and Technology (NIST) as US FIPS PUB 197 in November 2001 after a 5-year standardisation process. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity is also referred to as 'controller'. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central Controller. Management Frame Protection ( MFP ) A proprietary mechanism devised to integrity protect the otherwise unprotected management frames of the 802.11 protocol specification. Message Integrity Check ( MIC ) A checksum computed on a sequence of bytes and made known to the receiving party in a data communication, to let the receiving party make sure the bytes received were not compromised enroute. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. Temporal Key Integrity Protocol ( TKIP ) A security protocol defined to enhance the limitations of WEP. Message Integrity Check and per-packet keying on all WEP-encrypted frames are two significant enhancements provided by TKIP to WEP. Wired Equivalent Privacy ( WEP ) A security method defined by 802.11. WEP uses a symmetric key stream cipher called RC4 to encrypt the data packets. 802.11n 802.11n builds upon previous 802.11 standards by adding MIMO (multiple-input multiple-output). MIMO uses multiple transmitter and receiver antennas to allow for increased data throughput through spatial multiplexing and increased range. Control/Extension Channel A single 802.11 channel is 20 MHz wide. 802.11n allows the use of channels of width 40 MHz by combining two 20 MHz channels. The channels are known as the primary or control channel and secondary or extension channel. Both the channels are used for transmission and reception of data. REFERENCE [1] Part 11 Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications. [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol. [3] Enhanced Wireless Consortium MAC Specification, v1.24. [4] Enhanced Wireless Consortium PHY Specification, v1.27.")
class CLApIfType(TextualConvention, Integer32):
    description = 'This textual convention defines the type of a wireless interface. The semantics are as follows: dot11bg - This value indicates that the radio interface follows 802.11b or 802.11g standard. dot11a - This value indicates that the radio interface follows 802.11a standard. dot11abgn - This value indicates that the radio interface is operating in XOR mode between 802.11a and 802.11bg. dot11ac - This value indicates that the radio interface follows 802.11ac standard. uwb - This value indicates that this is a Ultra Wideband Interface. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("dot11bg", 1), ("dot11a", 2), ("uwb", 3), ("dot11abgn", 4), ("dot11ac", 5), ("dot11b", 6), ("dot11g", 7), ("dot11n24", 8), ("dot11n5", 9), ("unknown", 10))

class CLDot11Channel(TextualConvention, Unsigned32):
    description = 'This textual convention defines the possible channel numbers in an 802.11 communication channel. The 802.11 radio interface of an Access Point operates in one of the possible channels at any point of time for wireless data communication with 802.11 based wireless clients. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(34, 34), ValueRangeConstraint(36, 36), ValueRangeConstraint(38, 38), ValueRangeConstraint(40, 40), ValueRangeConstraint(42, 42), ValueRangeConstraint(44, 44), ValueRangeConstraint(46, 46), ValueRangeConstraint(48, 48), ValueRangeConstraint(52, 52), ValueRangeConstraint(56, 56), ValueRangeConstraint(60, 60), ValueRangeConstraint(64, 64), ValueRangeConstraint(149, 149), ValueRangeConstraint(153, 153), ValueRangeConstraint(157, 157), ValueRangeConstraint(161, 161), ValueRangeConstraint(165, 165), ValueRangeConstraint(169, 169), ValueRangeConstraint(173, 173), )
class CLDot11ClientStatus(TextualConvention, Integer32):
    description = "This textual convention defines the states of an 802.11 client. The semantics are as follows: idle(1) - client is in idle mode. aaaPending(2) - client's authentication is pending. Request has been sent to AAA server for authentication. authenticated(3) - client has been authenticated. associated(4) - client is associated, but not authenticated. powersave(5) - client is in powersave mode. disassociated(6) - client has dissociated and not in any of the 802.11 networks managed by the controller. tobedeleted(7) - client is marked for deletion. probing(8) - state before association. The client will be removed if it does not associate. excluded(9) - client has been marked as excluded after fixed number of authentication failures."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("idle", 1), ("aaaPending", 2), ("authenticated", 3), ("associated", 4), ("powersave", 5), ("disassociated", 6), ("tobedeleted", 7), ("probing", 8), ("excluded", 9))

class CLEventFrames(TextualConvention, Bits):
    reference = 'Part 11 Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications, Section 7.1.3.1.2 - Type and Subtype fields'
    description = 'This textual convention defines the possible 802.11 management frame subtypes. cLAssocRequestFrm - 802.11 Association Request frame cLAssocResponseFrm - 802.11 Association Response frame cLReAssocRequestFrm - 802.11 Reassociation Request frame cLReAssocResponseFrm - 802.11 Reassociation Response frame cLProbeRequestFrm - 802.11 Probe Request frame cLProbeResponseFrm - 802.11 Probe Response frame cLReserved1 - Reserved for future use cLReserved2 - Reserved for future use cLBeaconFrm - 802.11 Beacon frame cLAtimFrm - 802.11 Adhoc Traffic Indication Map frame cLDissociationFrm - 802.11 Dissociation frame cLAuthenticationFrm - 802.11 Authentication frame cLDeAuthenticationFrm - 802.11 Deauthentication frame '
    status = 'current'
    namedValues = NamedValues(("cLAssocRequestFrm", 0), ("cLAssocResponseFrm", 1), ("cLReAssocRequestFrm", 2), ("cLReAssocResponseFrm", 3), ("cLProbeRequestFrm", 4), ("cLProbeResponseFrm", 5), ("cLReserved1", 6), ("cLReserved2", 7), ("cLBeaconFrm", 8), ("cLAtimFrm", 9), ("cLDissociationFrm", 10), ("cLAuthenticationFrm", 11), ("cLDeAuthenticationFrm", 12))

class CLMfpEventType(TextualConvention, Integer32):
    description = "The type of the MFP anomaly event. invalidMic - The MFP Validation has identified that the MIC carried by a particular management frame is invalid. invalidSeq - The MFP validation has identified that a particular management frame is carrying an invalid sequence number. Note that an invalid sequence number error can also be detected due to an incorrect timestamp in the MFP information element. The incorrect timestamp could possibly be due to the fact that the detecting AP's time window is not in synchronization with that of other APs in the MFP framework. noMic - The MFP validation has detected a management frame without the MFP information element. unexpectedMic - The MFP validation has detected a management frame as carrying a MIC value when protection is not enabled on the WLAN. ccmpDecryptError - An MFP frame that was apparently received from a client in an AES-CCMP encrypted session was rejected by the Access Point because it could not be decrypted. ccmpInvalidMhdrIe - An MFP frame that was apparently received from a client in an AES-CCMP encrypted session was rejected by the Access Point because it contained an invalid MHDR information element, or the MHDR information element was not present. ccmpInvalidReplayCtr - An MFP frame that was apparently received from a client in an AES-CCMP encrypted session was rejected by the Access Point because the replay counter was not valid. tkipInvalidIcv - An MFP frame that was apparently received from a client in a TKIP encrypted session was rejected by the Access Point because it contained an invalid Integrity Check Value. tkipInvalidMic - An MFP frame that was apparently received from a client in a TKIP encrypted session was rejected by the Access Point because the message integrity check failed. tkipInvalidMhdrIe - An MFP frame that was apparently received from a client in a TKIP encrypted session was rejected by the Access Point because it contained an invalid MHDR information element, or the MHDR information element was not present. tkipInvalidReplayCtr - An MFP frame that was apparently received from a client in a TKIP encrypted session was rejected by the Access Point because it the replay counter was not valid. bcastDisassociationFrameRcvd - The Access Point detected a broadcast disassociation frame. Broadcast disassociation frames are rejected by CCXv5 compliant devices. bcastDeauthenticationFrameRcvd - The Access Point detected a broadcast deauthentication frame. Broadcast deauthentication frames are rejected by CCXv5 compliant devices. bcastActionFrameRcvd - The Access Point detected a broadcast action frame. Broadcast action frames are rejected by CCXv5 compliant devices. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 16, 17, 19, 20, 21, 22, 23, 24, 32, 33, 34))
    namedValues = NamedValues(("invalidMic", 1), ("invalidSeq", 2), ("noMic", 3), ("unexpectedMic", 4), ("ccmpNoEncryptError", 16), ("ccmpDecryptError", 17), ("ccmpInvalidReplayCtr", 19), ("tkipNoEncryptError", 20), ("tkipInvalidIcv", 21), ("tkipInvalidMic", 22), ("tkipInvalidMhdrIe", 23), ("tkipInvalidReplayCtr", 24), ("bcastDisassociationFrameRcvd", 32), ("bcastDeauthenticationFrameRcvd", 33), ("bcastActionFrameRcvd", 34))

class CLMfpEventSource(TextualConvention, Integer32):
    description = 'The source of the MFP anomaly event. infrastructureMfp - The source of the MFP event is an infrastructure device that implements MFP. clientMfp - The source of the MFP event is a client device that implements MFP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("infrastructureMfp", 1), ("clientMfp", 2))

class CLMfpVersion(TextualConvention, Integer32):
    description = 'This textual convention lists the versions of the MFP protocol. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mfpv1", 1), ("mfpv2", 2))

class CLTimeBaseStatus(TextualConvention, Integer32):
    description = 'This textual convention is used to define the time synchronization of entities with their respective time bases. cTimeBaseInSync - This value indicates that the respective entity is in synchronization with its time base. cTimeBaseNotInSync - This value indicates that the respective entity is not in synchronization with its time base. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cTimeBaseInSync", 1), ("cTimeBaseNotInSync", 2))

class CLSecEncryptType(TextualConvention, Bits):
    description = 'This textual convention defines the type of encryption to be applied to a WLAN. The semantics are as follows: tkip - This value indicates that TKIP encryption is configured for data protection. aes - This value indicates that AES encryption is configured for data protection. '
    status = 'current'
    namedValues = NamedValues(("tkip", 0), ("aes", 1))

class CLSecKeyFormat(TextualConvention, Integer32):
    description = 'This textual convention defines the type of the key configured for encryption. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("hex", 2), ("ascii", 3))

class CLDot11RfParamMode(TextualConvention, Integer32):
    description = "This textual convention defines how the RF parameters used to manage roaming are chosen by the controller. default - controller reverts back to the default values specified for the RF parameters. auto - controller determines the RF parameters automatically without any input from the end user. custom - controller uses the RF parameters configured by the end user. User is allowed to configure the parameters only if the mode is set to 'custom'. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("custom", 2), ("auto", 3))

class CLTsmDot11CurrentPackets(TextualConvention, Gauge32):
    description = 'The number of packets received over a specified period of time. '
    status = 'current'

class CLCdpAdvtVersionType(TextualConvention, Integer32):
    description = 'This textual convention lists the versions of the CDP protocol in use in LWAPP APs and Controllers.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cdpv1", 1), ("cdpv2", 2))

class CLDot11ChannelBandwidth(TextualConvention, Integer32):
    description = 'This textual convention defines the channel bandwidth for 802.11n radio interfaces. The semantics are as follows: five - This value indicates that the bandwidth is 5 MHz. ten - This value indicates that the bandwidth is 10 MHz. twenty - This value indicates that the bandwidth is 20 MHz. aboveforty - This value indicates that the bandwidth is 40 MHz with the extension channel above the control channel. belowforty - This value indicates that the bandwidth is 40 MHz with the extension channel below the control channel.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("five", 1), ("ten", 2), ("twenty", 3), ("aboveforty", 4), ("belowforty", 5))

class CLDot11Band(TextualConvention, Integer32):
    description = 'This textual convention defines the 802.11 frequency band. The semantics are as follows: band2dot4 - This value indicates that the 2.4 GHz band is in use. band5 - This value indicates that the 5 GHz band is in use.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("band2dot4", 1), ("band5", 2))

class CLApAssocFailureReason(TextualConvention, Integer32):
    description = "This textual convention defines the possible reasons for an AP's failure to get associated to a controller. The semantics are as follows: unknown - The reason for the AP not being able to associate is unknown. notSupported - The AP is not supported for management by the controller."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unknown", 1), ("notSupported", 2))

class CLWebAuthType(TextualConvention, Integer32):
    description = 'Represents either one of the following web auth types internalDefault(1) - The default login page will be presented to the client for authentication. internalCustom(2) - The administrator has created and uploaded a custom login page and it will be presented to the clients for authentication. external(3) - This value indicates that the login page will be served from the external web server. Note that cLWAWebAuthType can be successfully set to this value when the cLWAExternalWebAuthURL object has been set to string with non-zero length.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("internalDefault", 1), ("internalCustom", 2), ("external", 3))

class CLClientPowerSaveMode(TextualConvention, Integer32):
    description = 'This textual convention defines power management mode of this client. The possible two modes are: active(1) - this client is not in power-save mode and it is actively sending or receiving data. powersave(2) - this client is in power-save mode and it wakes up once a while to check for pending data.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("powersave", 2))

class CLApEthernetIfStatus(TextualConvention, Integer32):
    description = 'This textual convention defines the status of an Ethernet interface of an AP joined to a controller. up(1) - The interface is operational and ready to transmit packets. down(2) - The interface is not operational.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class CLApDot11RadioSubband(TextualConvention, Integer32):
    description = 'This textual convention defines the possible values of subbands a radio can support. Currently, this information is applicable only to A radios. all(1) - This radio is a regular A radio that operates in the full A band spectrum in the frequency range 4940 Mhz - 5850 Mhz. sub49(2) - This is an A radio that operates only in the public safety (4.9 Ghz) sub band in the frequency range 4940 Mhz - 5100 Mhz. sub52(3) - This is an A radio that operates only in the 5.2 Ghz sub band in the frequency range 5250 Mhz - 5350 Mhz. sub54(4) - This is an A radio that operates only in the 5.4 Ghz sub band in the frequency range 5470 Mhz - 5725 Mhz. sub58(5) - This is an A radio that operates only in the 5.8 Ghz sub band in the frequency range 5725 Mhz - 5850 Mhz. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("all", 1), ("sub49", 2), ("sub52", 3), ("sub54", 4), ("sub58", 5))

class CLApDot11RadioRole(TextualConvention, Integer32):
    description = 'This textual convention defines the possible values of role a radio can support. shutdown(0) - This role states that the radio is shut. updownlink(1) - This radio will provide the both uplink and downlink access. uplink(2) - This role is applicable only for Ethernet ports. Defined here to maintain the types of role. downlink(3) - This radio will provide downlink access. downlink radio allows child APs to join. access(4) - This radio will provide the access to the clients. uplinkaccess(5) - This radio role states that the radio will provide the uplink access to the clients. downlinkaccess(6) - This radio role states that the radio will provide the downlink access to the clients. updownlinkaccess(7) - This radio role states that the radio will provide both uplink and downlink access to the clients. unknown(8) - This radio does not have role. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("shutdown", 0), ("updownlink", 1), ("uplink", 2), ("downlink", 3), ("access", 4), ("uplinkaccess", 5), ("downlinkaccess", 6), ("updownlinkaccess", 7), ("unknown", 8))

class CcxServiceVersion(TextualConvention, Integer32):
    description = 'This textual convention defines the service versions supported by a CCX Next client. The supported services include foundation, location, management and voice.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("version1", 2), ("version2", 3))

class CLApMode(TextualConvention, Integer32):
    description = 'This textual convention defines the working mode of the AP. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("local", 0), ("monitor", 1), ("remote", 2), ("roguedetector", 3), ("sniffer", 4), ("bridge", 5), ("seConnect", 6))

mibBuilder.exportSymbols("CISCO-LWAPP-TC-MIB", CLTimeBaseStatus=CLTimeBaseStatus, CLDot11RfParamMode=CLDot11RfParamMode, PYSNMP_MODULE_ID=ciscoLwappTextualConventions, CLMfpVersion=CLMfpVersion, CLWebAuthType=CLWebAuthType, CLMfpEventType=CLMfpEventType, CLSecEncryptType=CLSecEncryptType, CLDot11ChannelBandwidth=CLDot11ChannelBandwidth, CLClientPowerSaveMode=CLClientPowerSaveMode, CLDot11Channel=CLDot11Channel, CLCdpAdvtVersionType=CLCdpAdvtVersionType, CLSecKeyFormat=CLSecKeyFormat, CLDot11ClientStatus=CLDot11ClientStatus, CLTsmDot11CurrentPackets=CLTsmDot11CurrentPackets, CLDot11Band=CLDot11Band, CLApDot11RadioSubband=CLApDot11RadioSubband, CLMfpEventSource=CLMfpEventSource, CLApEthernetIfStatus=CLApEthernetIfStatus, CLApAssocFailureReason=CLApAssocFailureReason, CLApDot11RadioRole=CLApDot11RadioRole, CLEventFrames=CLEventFrames, ciscoLwappTextualConventions=ciscoLwappTextualConventions, CLApIfType=CLApIfType, CcxServiceVersion=CcxServiceVersion, CLApMode=CLApMode)
