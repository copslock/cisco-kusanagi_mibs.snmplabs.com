#
# PySNMP MIB module MP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
MmEndpointID, MmGlobalIdentifier, MmGatekeeperID, MmTAddressTag = mibBuilder.importSymbols("MULTI-MEDIA-MIB-TC", "MmEndpointID", "MmGlobalIdentifier", "MmGatekeeperID", "MmTAddressTag")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Gauge32, IpAddress, Counter32, TimeTicks, Integer32, iso, MibIdentifier, Unsigned32, Counter64, ObjectIdentity, enterprises, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Gauge32", "IpAddress", "Counter32", "TimeTicks", "Integer32", "iso", "MibIdentifier", "Unsigned32", "Counter64", "ObjectIdentity", "enterprises", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TruthValue, TextualConvention, TAddress, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "TAddress", "DateAndTime", "DisplayString")
media = MibIdentifier((1, 3, 6, 1, 4, 1, 3011, 2))
h323MP = ModuleIdentity((1, 3, 6, 1, 4, 1, 3011, 2, 2))
if mibBuilder.loadTexts: h323MP.setLastUpdated('9808062253Z')
if mibBuilder.loadTexts: h323MP.setOrganization('VideoServer')
if mibBuilder.loadTexts: h323MP.setContactInfo(' Irina Suconick Postal: Video Server 63 Third st. Burlington, MA 01803 Tel: (781)505-2155 E-Mail: isuconick@videoserver.com ')
if mibBuilder.loadTexts: h323MP.setDescription(' ')
mpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3011, 2, 2, 1))
mpConference = MibIdentifier((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2))
mpConfigMaxAudioMixCount = MibScalar((1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConfigMaxAudioMixCount.setStatus('current')
if mibBuilder.loadTexts: mpConfigMaxAudioMixCount.setDescription('Maximum number of participants allowed in the audio mix.')
mpConfigMaxVideoMixCount = MibScalar((1, 3, 6, 1, 4, 1, 3011, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConfigMaxVideoMixCount.setStatus('current')
if mibBuilder.loadTexts: mpConfigMaxVideoMixCount.setDescription('Maximum number of participants allowed in the video mix.')
mpConferenceTable = MibTable((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1), )
if mibBuilder.loadTexts: mpConferenceTable.setStatus('current')
if mibBuilder.loadTexts: mpConferenceTable.setDescription('This table contains information about running conferences. It is a list of conference entries. The number of entries equals to the number of running conferences.')
mpConferenceTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1), ).setIndexNames((0, "MP-MIB", "mpConferenceConferenceId"))
if mibBuilder.loadTexts: mpConferenceTableEntry.setStatus('current')
if mibBuilder.loadTexts: mpConferenceTableEntry.setDescription('It contains objects that describe a specific conference.')
mpConferenceConferenceId = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 1), MmGlobalIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceConferenceId.setStatus('current')
if mibBuilder.loadTexts: mpConferenceConferenceId.setDescription('The conference identifier as specified in ITU-T H.323V2 specification.')
mpConferenceAudioNoiseThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceAudioNoiseThreshold.setStatus('current')
if mibBuilder.loadTexts: mpConferenceAudioNoiseThreshold.setDescription('This value represents the audio power level above which the signal is detected as speech.')
mpConferenceLipSyncEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceLipSyncEnable.setStatus('current')
if mibBuilder.loadTexts: mpConferenceLipSyncEnable.setDescription('This value indicates rather the lip syncronization adjustments are performed.')
mpConferenceParticipantsTable = MibTable((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2), )
if mibBuilder.loadTexts: mpConferenceParticipantsTable.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsTable.setDescription('This table contains information about conference participants. It is a list of participant entries. The number of entries equals the number of participants for all conferences.')
mpConferenceParticipantsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1), ).setIndexNames((0, "MP-MIB", "mpConferenceConferenceId"), (0, "MP-MIB", "mpConferenceParticipantsTableIndex"))
if mibBuilder.loadTexts: mpConferenceParticipantsTableEntry.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsTableEntry.setDescription('It contains objects that describe a specific conference participant.')
mpConferenceParticipantsTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsTableIndex.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsTableIndex.setDescription('An arbitrary index to this table. This index is one for the first participant for every given conference. It is incremented by one for each subsequent participant of the same conference. The last index for a particular conference is equal to the number of participants for that conference.')
mpConferenceParticipantsEndpointId = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 2), MmEndpointID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsEndpointId.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsEndpointId.setDescription('The H.323 id of this participant as described in ITU-T H.323V2 specification.')
mpConferenceParticipantsTransmitAudioState = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("mute", 2), ("toneGeneration", 3), ("off", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsTransmitAudioState.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsTransmitAudioState.setDescription('This value indicates the state of transmitted audio: normal - transmit normal audio toneGeneration - transmit test tone mute - transmit silence audio off - no audio is transmitted')
mpConferenceParticipantsReceiveAudioState = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("loopBack", 2), ("block", 3), ("off", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsReceiveAudioState.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsReceiveAudioState.setDescription('This value indicates the state of received audio: normal - receive normal audio loopBack - received audio presented unchanged to the transmitter block - received audio is not part of the mix off - no audio is received')
mpConferenceParticipantsTransmitVideoState = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsTransmitVideoState.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsTransmitVideoState.setDescription('This value indicates the state of transmitted video: on - normal video is transmitted off - no video is transmitted.')
mpConferenceParticipantsReceiveVideoState = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("block", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsReceiveVideoState.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsReceiveVideoState.setDescription('This value indicates the state of transmitted video: normal - normal video is received block - received video is not displayed off - no video is transmitted.')
mpConferenceParticipantsLoudnessMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsLoudnessMeasurement.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsLoudnessMeasurement.setDescription('This is the current loudness measurement value in dB.')
mpConferenceParticipantsVoiceActivity = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsVoiceActivity.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsVoiceActivity.setDescription('This value is True when the speech is detected.')
mpConferenceParticipantsInputAudioGain = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsInputAudioGain.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsInputAudioGain.setDescription('This value reflects the current input volume adjustment in dB.')
mpConferenceParticipantsOutputAudioGain = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsOutputAudioGain.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsOutputAudioGain.setDescription('This value reflects the current output volume adjustment in dB.')
mpConferenceParticipantsMaxAudioEncoderPayloadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsMaxAudioEncoderPayloadSize.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsMaxAudioEncoderPayloadSize.setDescription('The maximum size of payload in ms.')
mpConferenceParticipantsMaxAudioDecoderPayloadSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsMaxAudioDecoderPayloadSize.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsMaxAudioDecoderPayloadSize.setDescription('The maximum size of payload in ms.')
mpConferenceParticipantsTotalPacketsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsTotalPacketsTransmitted.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsTotalPacketsTransmitted.setDescription('The total number of transmitted packets.')
mpConferenceParticipantsTotalPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsTotalPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsTotalPacketsReceived.setDescription('The total number of received packets.')
mpConferenceParticipantsInvalidPacketErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsInvalidPacketErrors.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsInvalidPacketErrors.setDescription('The total number of packets with invalid packet errors.')
mpConferenceParticipantsLateAudioPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsLateAudioPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsLateAudioPacketsDropped.setDescription('The total number of packets that arrived too late to be processed.')
mpConferenceParticipantsReceivedSilencePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsReceivedSilencePackets.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsReceivedSilencePackets.setDescription('The total number of silence packets that were received.')
mpConferenceParticipantsSilencePacketsGenerated = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsSilencePacketsGenerated.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsSilencePacketsGenerated.setDescription('The total number of silence packets that were generated.')
mpConferenceParticipantsVideoFrameRate = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsVideoFrameRate.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsVideoFrameRate.setDescription('This value represents the current measured frame rate received.')
mpConferenceParticipantsVideoResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("h263SubQCIF", 1), ("h263QCIF", 2), ("h263CIF", 3), ("h2634CIF", 4), ("h26316CIF", 5), ("h263Reserved", 6), ("h261QCIF", 7), ("h261CIF", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsVideoResolution.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsVideoResolution.setDescription('Received video resolution.')
mpConferenceParticipantsFullPictureCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceParticipantsFullPictureCounter.setStatus('current')
if mibBuilder.loadTexts: mpConferenceParticipantsFullPictureCounter.setDescription('This value represents the number of full image pictures received.')
mpConferenceGlobalAudioMixTable = MibTable((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3), )
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTable.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTable.setDescription('This table contains information about conference participants that are present in a global audio mix. It is a list of participant entries. The number of entries equals to the sum of all audio mix participants in all conferences.')
mpConferenceGlobalAudioMixTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3, 1), ).setIndexNames((0, "MP-MIB", "mpConferenceConferenceId"), (0, "MP-MIB", "mpConferenceGlobalAudioMixTableIndex"))
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTableEntry.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTableEntry.setDescription('It contains objects that describe the participants.')
mpConferenceGlobalAudioMixTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTableIndex.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTableIndex.setDescription('An arbitrary index to this table. This index is one for the first participant for every given conference. It is incremented by one for each subsequent participant of the same conference. The last index for a particular conference is equal to the number of participants for that conference.')
mpConferenceGlobalAudioMixTerminalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 3, 1, 2), MmEndpointID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTerminalIdentifier.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalAudioMixTerminalIdentifier.setDescription('The H.323 id of this participant as described in ITU-T H.323V2 specification.')
mpConferenceGlobalVideoMixTable = MibTable((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4), )
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTable.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTable.setDescription('This table contains information about conference participants that are present in a global video mix. It is a list of participant entries. The number of entries equals to the sum of all video mix participants in all conferences.')
mpConferenceGlobalVideoMixTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4, 1), ).setIndexNames((0, "MP-MIB", "mpConferenceConferenceId"), (0, "MP-MIB", "mpConferenceGlobalVideoMixTableIndex"))
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTableEntry.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTableEntry.setDescription('It contains objects that describe the participants.')
mpConferenceGlobalVideoMixTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTableIndex.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTableIndex.setDescription('An arbitrary index to this table. This index is one for the first participant for every given conference. It is incremented by one for each subsequent participant of the same conference. The last index for a particular conference is equal to the number of participants for that conference.')
mpConferenceGlobalVideoMixTerminalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3011, 2, 2, 2, 4, 1, 2), MmEndpointID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTerminalIdentifier.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGlobalVideoMixTerminalIdentifier.setDescription('The H.323 id of this participant as described in ITU-T H.323V2 specification.')
mpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3011, 2, 2, 3))
mpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 1))
mpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 1, 1)).setObjects(("MP-MIB", "mpConfigMaxAudioMixCount"), ("MP-MIB", "mpConfigMaxVideoMixCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpConfigGroup = mpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: mpConfigGroup.setDescription('.')
mpConferenceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 1, 2)).setObjects(("MP-MIB", "mpConferenceConferenceId"), ("MP-MIB", "mpConferenceAudioNoiseThreshold"), ("MP-MIB", "mpConferenceLipSyncEnable"), ("MP-MIB", "mpConferenceParticipantsTableIndex"), ("MP-MIB", "mpConferenceParticipantsEndpointId"), ("MP-MIB", "mpConferenceParticipantsTransmitAudioState"), ("MP-MIB", "mpConferenceParticipantsReceiveAudioState"), ("MP-MIB", "mpConferenceParticipantsTransmitVideoState"), ("MP-MIB", "mpConferenceParticipantsReceiveVideoState"), ("MP-MIB", "mpConferenceParticipantsLoudnessMeasurement"), ("MP-MIB", "mpConferenceParticipantsVoiceActivity"), ("MP-MIB", "mpConferenceParticipantsInputAudioGain"), ("MP-MIB", "mpConferenceParticipantsOutputAudioGain"), ("MP-MIB", "mpConferenceParticipantsMaxAudioEncoderPayloadSize"), ("MP-MIB", "mpConferenceParticipantsMaxAudioDecoderPayloadSize"), ("MP-MIB", "mpConferenceParticipantsTotalPacketsTransmitted"), ("MP-MIB", "mpConferenceParticipantsTotalPacketsReceived"), ("MP-MIB", "mpConferenceParticipantsLateAudioPacketsDropped"), ("MP-MIB", "mpConferenceParticipantsReceivedSilencePackets"), ("MP-MIB", "mpConferenceParticipantsSilencePacketsGenerated"), ("MP-MIB", "mpConferenceParticipantsVideoFrameRate"), ("MP-MIB", "mpConferenceParticipantsVideoResolution"), ("MP-MIB", "mpConferenceParticipantsFullPictureCounter"), ("MP-MIB", "mpConferenceGlobalAudioMixTableIndex"), ("MP-MIB", "mpConferenceGlobalAudioMixTerminalIdentifier"), ("MP-MIB", "mpConferenceGlobalVideoMixTableIndex"), ("MP-MIB", "mpConferenceGlobalVideoMixTerminalIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpConferenceGroup = mpConferenceGroup.setStatus('current')
if mibBuilder.loadTexts: mpConferenceGroup.setDescription('.')
mpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3011, 2, 2, 3, 2)).setObjects(("MP-MIB", "mpConfigGroup"), ("MP-MIB", "mpConferenceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpMIBCompliance = mpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: mpMIBCompliance.setDescription('The set of objects required for compliance.')
mibBuilder.exportSymbols("MP-MIB", mpConfigMaxAudioMixCount=mpConfigMaxAudioMixCount, mpConferenceParticipantsReceiveAudioState=mpConferenceParticipantsReceiveAudioState, mpConferenceParticipantsTableIndex=mpConferenceParticipantsTableIndex, h323MP=h323MP, mpConferenceParticipantsOutputAudioGain=mpConferenceParticipantsOutputAudioGain, mpConferenceParticipantsEndpointId=mpConferenceParticipantsEndpointId, mpConferenceParticipantsVideoFrameRate=mpConferenceParticipantsVideoFrameRate, mpConferenceGroup=mpConferenceGroup, mpConferenceGlobalVideoMixTerminalIdentifier=mpConferenceGlobalVideoMixTerminalIdentifier, mpConferenceParticipantsInvalidPacketErrors=mpConferenceParticipantsInvalidPacketErrors, mpConferenceGlobalAudioMixTableEntry=mpConferenceGlobalAudioMixTableEntry, mpConferenceTable=mpConferenceTable, mpConferenceParticipantsTotalPacketsTransmitted=mpConferenceParticipantsTotalPacketsTransmitted, mpConferenceTableEntry=mpConferenceTableEntry, mpConferenceAudioNoiseThreshold=mpConferenceAudioNoiseThreshold, mpConferenceParticipantsMaxAudioEncoderPayloadSize=mpConferenceParticipantsMaxAudioEncoderPayloadSize, mpConferenceParticipantsReceiveVideoState=mpConferenceParticipantsReceiveVideoState, mpMIBConformance=mpMIBConformance, mpConferenceParticipantsInputAudioGain=mpConferenceParticipantsInputAudioGain, mpConferenceParticipantsLoudnessMeasurement=mpConferenceParticipantsLoudnessMeasurement, mpConferenceParticipantsTransmitAudioState=mpConferenceParticipantsTransmitAudioState, mpConferenceParticipantsLateAudioPacketsDropped=mpConferenceParticipantsLateAudioPacketsDropped, mpConferenceParticipantsTransmitVideoState=mpConferenceParticipantsTransmitVideoState, media=media, mpConferenceLipSyncEnable=mpConferenceLipSyncEnable, mpConferenceParticipantsVoiceActivity=mpConferenceParticipantsVoiceActivity, mpConferenceParticipantsSilencePacketsGenerated=mpConferenceParticipantsSilencePacketsGenerated, mpConferenceParticipantsFullPictureCounter=mpConferenceParticipantsFullPictureCounter, mpConferenceGlobalVideoMixTableEntry=mpConferenceGlobalVideoMixTableEntry, mpConfigGroup=mpConfigGroup, mpConferenceParticipantsTotalPacketsReceived=mpConferenceParticipantsTotalPacketsReceived, PYSNMP_MODULE_ID=h323MP, mpConferenceParticipantsReceivedSilencePackets=mpConferenceParticipantsReceivedSilencePackets, mpConferenceGlobalVideoMixTable=mpConferenceGlobalVideoMixTable, mpConferenceGlobalVideoMixTableIndex=mpConferenceGlobalVideoMixTableIndex, mpConferenceParticipantsTableEntry=mpConferenceParticipantsTableEntry, mpConferenceParticipantsTable=mpConferenceParticipantsTable, mpConferenceParticipantsMaxAudioDecoderPayloadSize=mpConferenceParticipantsMaxAudioDecoderPayloadSize, mpConfig=mpConfig, mpMIBCompliance=mpMIBCompliance, mpConferenceParticipantsVideoResolution=mpConferenceParticipantsVideoResolution, mpMIBGroups=mpMIBGroups, mpConferenceGlobalAudioMixTable=mpConferenceGlobalAudioMixTable, mpConferenceGlobalAudioMixTerminalIdentifier=mpConferenceGlobalAudioMixTerminalIdentifier, mpConfigMaxVideoMixCount=mpConfigMaxVideoMixCount, mpConferenceConferenceId=mpConferenceConferenceId, mpConferenceGlobalAudioMixTableIndex=mpConferenceGlobalAudioMixTableIndex, mpConference=mpConference)
