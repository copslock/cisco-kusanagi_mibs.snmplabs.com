#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:29:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mscDataSigChan, mscDataSigChanIndex = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChan", "mscDataSigChanIndex")
Unsigned32, StorageType, RowStatus, DisplayString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "Unsigned32", "StorageType", "RowStatus", "DisplayString")
NonReplicated, Link = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "NonReplicated", "Link")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Gauge32, Counter64, ObjectIdentity, Bits, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, iso, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Gauge32", "Counter64", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "iso", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
disdnJapanInsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118))
mscDataSigChanIns = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11))
mscDataSigChanInsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1), )
if mibBuilder.loadTexts: mscDataSigChanInsRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsRowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanIns components.')
mscDataSigChanInsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsRowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanIns component.')
mscDataSigChanInsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanIns components. These components can be added and deleted.')
mscDataSigChanInsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanInsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsStorageType.setDescription('This variable represents the storage type value for the mscDataSigChanIns tables.')
mscDataSigChanInsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanInsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsIndex.setDescription('This variable represents the index for the mscDataSigChanIns tables.')
mscDataSigChanInsL2Table = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11), )
if mibBuilder.loadTexts: mscDataSigChanInsL2Table.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsL2Table.setDescription('This group represents the provisionable Layer 2 attributes of the Q931 CCITT protocol.')
mscDataSigChanInsL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsL2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsL2Entry.setDescription('An entry in the mscDataSigChanInsL2Table.')
mscDataSigChanInsT23 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsT23.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsT23.setDescription('This attribute specifies the layer2 enable request timer.')
mscDataSigChanInsT200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsT200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsT200.setDescription('This attribute specifies the maximum time between a layer 2 frame and its acknowledgement')
mscDataSigChanInsN200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsN200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsN200.setDescription('This attribute specifies the maximum number of re-transmissions of a layer2 frame.')
mscDataSigChanInsT203 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 40)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsT203.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsT203.setDescription('This attribute specifies the maximum time that a no layer 2 traffic situation can last. Expiry triggers a check on whether the far end is a live.')
mscDataSigChanInsN201 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 260)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsN201.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsN201.setDescription('This attribute specifies the maximum number of octets in an information field.')
mscDataSigChanInsCircuitSwitchedK = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 632)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsCircuitSwitchedK.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsCircuitSwitchedK.setDescription('This attribute specifies the maximum number of frames for B channel use.')
mscDataSigChanInsProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 13), )
if mibBuilder.loadTexts: mscDataSigChanInsProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsProvTable.setDescription('This group defines the general options of the d-channel signalling link.')
mscDataSigChanInsProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsProvEntry.setDescription('An entry in the mscDataSigChanInsProvTable.')
mscDataSigChanInsSide = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2))).clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsSide.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsSide.setDescription('This attribute specifies whether the layer 2 HDLC interface is the network or user side of the connection.')
mscDataSigChanInsOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15), )
if mibBuilder.loadTexts: mscDataSigChanInsOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsOperTable.setDescription('This group provides the operational attributes for the signalling protocol.')
mscDataSigChanInsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsOperEntry.setDescription('An entry in the mscDataSigChanInsOperTable.')
mscDataSigChanInsActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsActiveChannels.setDescription('This attribute indicates the number of currently active channels. This includes data and voice channels.')
mscDataSigChanInsPeakActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsPeakActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsPeakActiveChannels.setDescription('This attribute indicates the maximum number of channels that have been active on this signalling channel during the last polling period.')
mscDataSigChanInsDChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("outOfService", 0), ("establishing", 1), ("established", 2), ("enabling", 3), ("inService", 4), ("restarting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsDChanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsDChanStatus.setDescription('This attribute indicates the state of the D-channel. outOfService means that there is no layer 2 or layer 3 connectivity to the PBX. establishing means that the signalling channel is attempting to stage the layer 2. established means that the layer 2 is enabled. If the signalling channel stays in the established state, then it is waiting for a restart from the PBX. enabling means that the resources for processing calls are being initialized. If the signalling channel stays in the enabling state then it is waiting for a restart acknowledgement from the PBX. inService means that the resources for processing calls are available. restarting means that the resources for call processing are being rei- initialized.')
mscDataSigChanInsToolsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 16), )
if mibBuilder.loadTexts: mscDataSigChanInsToolsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsToolsTable.setDescription('This group contains a series of operational attributes which turn on and off several kinds of tracing.')
mscDataSigChanInsToolsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 16, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsToolsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsToolsEntry.setDescription('An entry in the mscDataSigChanInsToolsTable.')
mscDataSigChanInsTracing = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsTracing.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsTracing.setDescription('This attribute defines which types of tracing are active for this signalling channel. The tracing messages are sent to the debug stream. To see the messages the agentQueue attribute in Col/debug must be greater than 0 and a Telnet NMIS session must list the debug stream in in its data streams (ex. set nmis telnet session/1 dataStreams debug). Different types of tracing can be enabled simultaneously. Note that tracing consumes additional CPU resources and will slow down call processing on a heavily loaded card. If there is message block exhaustion tracing will be suspended for a period and then automatically reenabled. An alarm is generated on tracing suspension and resumption. This mechanism protects the function processor against excessive numbers of tracing messages. Types of tracing include: protocolErrors - get details of any protocol errors which are occuring. Protocol errors are also reported in summary form as alarms. q931Summary - Summary of the Q.931 messages on the signalling link, including certain call details (calling number, called number, release codes). q931Hex - Q.931 messages displayed in hex format. Useful to determine protocol compliance in case of errors reported on local or remote ends. q931Symbolic - Q.931 messages parsed to give maximum detail. Useful for understanding content of messages flowing on the link. portHex - Messages in hex format being sent and received on the link. Description of bits: protocolErrors(0) q931Summary(1) q931Hex(2) q931Symbolic(3) portHex(4)')
mscDataSigChanInsFramer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2))
mscDataSigChanInsFramerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1), )
if mibBuilder.loadTexts: mscDataSigChanInsFramerRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerRowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanInsFramer components.')
mscDataSigChanInsFramerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsFramerRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerRowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanInsFramer component.')
mscDataSigChanInsFramerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanInsFramer components. These components cannot be added nor deleted.')
mscDataSigChanInsFramerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanInsFramerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerStorageType.setDescription('This variable represents the storage type value for the mscDataSigChanInsFramer tables.')
mscDataSigChanInsFramerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanInsFramerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerIndex.setDescription('This variable represents the index for the mscDataSigChanInsFramer tables.')
mscDataSigChanInsFramerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 10), )
if mibBuilder.loadTexts: mscDataSigChanInsFramerProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerProvTable.setDescription('This group contains the base provisioning data for the Framer component. Application or hardware interface specific provisioning data is contained in other provisionable Framer groups.')
mscDataSigChanInsFramerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsFramerProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerProvEntry.setDescription('An entry in the mscDataSigChanInsFramerProvTable.')
mscDataSigChanInsFramerInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanInsFramerInterfaceName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerInterfaceName.setDescription("This attribute contains a hardware component name. The attribute associates the application with a specific link. This defines the module processor on which Framer's parent component (as well as Framer itself) will run.")
mscDataSigChanInsFramerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12), )
if mibBuilder.loadTexts: mscDataSigChanInsFramerStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscDataSigChanInsFramerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsFramerStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerStateEntry.setDescription('An entry in the mscDataSigChanInsFramerStateTable.')
mscDataSigChanInsFramerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscDataSigChanInsFramerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscDataSigChanInsFramerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscDataSigChanInsFramerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13), )
if mibBuilder.loadTexts: mscDataSigChanInsFramerStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerStatsTable.setDescription('This group contains the operational statistics data for a Framer component.')
mscDataSigChanInsFramerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanInsFramerStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerStatsEntry.setDescription('An entry in the mscDataSigChanInsFramerStatsTable.')
mscDataSigChanInsFramerFrmToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerFrmToIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerFrmToIf.setDescription('This attribute counts the number of frames transmitted to the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerFrmFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerFrmFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerFrmFromIf.setDescription('This attribute counts the number of frames received from the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerOctetFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerOctetFromIf.setDescription('The number of bytes received from the link interface by Framer.')
mscDataSigChanInsFramerAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerAborts.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerAborts.setDescription('This attribute counts the total number of aborts received. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerCrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerCrcErrors.setDescription('This attribute counts the total number of frames with CRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerLrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerLrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerLrcErrors.setDescription('This attribute counts the total number of frames with LRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerNonOctetErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerNonOctetErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerNonOctetErrors.setDescription('This attribute counts the total number of frames that were non octet aligned. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerOverruns.setDescription('This attribute counts the total number of frames received from the link for which overruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerUnderruns.setDescription('This attribute counts the total number of frames transmitted to the link for which underruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanInsFramerLargeFrmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanInsFramerLargeFrmErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanInsFramerLargeFrmErrors.setDescription('This attribute counts the total number of frames received which were too large. The frame was longer than 500 bytes. This count wraps to zero after reaching its maximum value.')
disdnJapanInsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1))
disdnJapanInsGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1, 1))
disdnJapanInsGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1, 1, 3))
disdnJapanInsGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1, 1, 3, 2))
disdnJapanInsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3))
disdnJapanInsCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3, 1))
disdnJapanInsCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3, 1, 3))
disdnJapanInsCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", disdnJapanInsCapabilities=disdnJapanInsCapabilities, mscDataSigChanInsFramerFrmToIf=mscDataSigChanInsFramerFrmToIf, mscDataSigChanInsProvTable=mscDataSigChanInsProvTable, mscDataSigChanInsOperTable=mscDataSigChanInsOperTable, mscDataSigChanIns=mscDataSigChanIns, mscDataSigChanInsComponentName=mscDataSigChanInsComponentName, mscDataSigChanInsL2Table=mscDataSigChanInsL2Table, mscDataSigChanInsFramerIndex=mscDataSigChanInsFramerIndex, mscDataSigChanInsFramerInterfaceName=mscDataSigChanInsFramerInterfaceName, mscDataSigChanInsSide=mscDataSigChanInsSide, mscDataSigChanInsRowStatus=mscDataSigChanInsRowStatus, mscDataSigChanInsN200=mscDataSigChanInsN200, disdnJapanInsMIB=disdnJapanInsMIB, mscDataSigChanInsFramerProvEntry=mscDataSigChanInsFramerProvEntry, mscDataSigChanInsFramerProvTable=mscDataSigChanInsFramerProvTable, mscDataSigChanInsCircuitSwitchedK=mscDataSigChanInsCircuitSwitchedK, mscDataSigChanInsFramerCrcErrors=mscDataSigChanInsFramerCrcErrors, mscDataSigChanInsT203=mscDataSigChanInsT203, mscDataSigChanInsFramer=mscDataSigChanInsFramer, mscDataSigChanInsFramerComponentName=mscDataSigChanInsFramerComponentName, disdnJapanInsCapabilitiesCA02A=disdnJapanInsCapabilitiesCA02A, mscDataSigChanInsIndex=mscDataSigChanInsIndex, mscDataSigChanInsFramerNonOctetErrors=mscDataSigChanInsFramerNonOctetErrors, mscDataSigChanInsToolsEntry=mscDataSigChanInsToolsEntry, disdnJapanInsGroupCA02=disdnJapanInsGroupCA02, mscDataSigChanInsFramerRowStatus=mscDataSigChanInsFramerRowStatus, disdnJapanInsCapabilitiesCA=disdnJapanInsCapabilitiesCA, mscDataSigChanInsTracing=mscDataSigChanInsTracing, mscDataSigChanInsT23=mscDataSigChanInsT23, mscDataSigChanInsFramerStateTable=mscDataSigChanInsFramerStateTable, mscDataSigChanInsFramerRowStatusEntry=mscDataSigChanInsFramerRowStatusEntry, mscDataSigChanInsToolsTable=mscDataSigChanInsToolsTable, mscDataSigChanInsOperEntry=mscDataSigChanInsOperEntry, mscDataSigChanInsActiveChannels=mscDataSigChanInsActiveChannels, mscDataSigChanInsFramerUnderruns=mscDataSigChanInsFramerUnderruns, mscDataSigChanInsFramerRowStatusTable=mscDataSigChanInsFramerRowStatusTable, disdnJapanInsGroupCA=disdnJapanInsGroupCA, disdnJapanInsGroupCA02A=disdnJapanInsGroupCA02A, mscDataSigChanInsStorageType=mscDataSigChanInsStorageType, mscDataSigChanInsFramerOctetFromIf=mscDataSigChanInsFramerOctetFromIf, mscDataSigChanInsFramerLargeFrmErrors=mscDataSigChanInsFramerLargeFrmErrors, mscDataSigChanInsFramerAborts=mscDataSigChanInsFramerAborts, mscDataSigChanInsN201=mscDataSigChanInsN201, mscDataSigChanInsDChanStatus=mscDataSigChanInsDChanStatus, mscDataSigChanInsFramerStatsTable=mscDataSigChanInsFramerStatsTable, mscDataSigChanInsProvEntry=mscDataSigChanInsProvEntry, mscDataSigChanInsFramerAdminState=mscDataSigChanInsFramerAdminState, mscDataSigChanInsFramerOperationalState=mscDataSigChanInsFramerOperationalState, mscDataSigChanInsFramerLrcErrors=mscDataSigChanInsFramerLrcErrors, mscDataSigChanInsFramerStorageType=mscDataSigChanInsFramerStorageType, mscDataSigChanInsPeakActiveChannels=mscDataSigChanInsPeakActiveChannels, mscDataSigChanInsFramerFrmFromIf=mscDataSigChanInsFramerFrmFromIf, mscDataSigChanInsFramerStatsEntry=mscDataSigChanInsFramerStatsEntry, mscDataSigChanInsFramerOverruns=mscDataSigChanInsFramerOverruns, mscDataSigChanInsRowStatusEntry=mscDataSigChanInsRowStatusEntry, mscDataSigChanInsT200=mscDataSigChanInsT200, mscDataSigChanInsRowStatusTable=mscDataSigChanInsRowStatusTable, disdnJapanInsGroup=disdnJapanInsGroup, mscDataSigChanInsFramerUsageState=mscDataSigChanInsFramerUsageState, disdnJapanInsCapabilitiesCA02=disdnJapanInsCapabilitiesCA02, mscDataSigChanInsFramerStateEntry=mscDataSigChanInsFramerStateEntry, mscDataSigChanInsL2Entry=mscDataSigChanInsL2Entry)
