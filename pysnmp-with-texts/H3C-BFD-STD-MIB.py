#
# PySNMP MIB module H3C-BFD-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-BFD-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
mib_2, NotificationType, Bits, Counter32, MibIdentifier, Integer32, Gauge32, Unsigned32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "NotificationType", "Bits", "Counter32", "MibIdentifier", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter64", "TimeTicks")
TextualConvention, TimeStamp, StorageType, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "StorageType", "DisplayString", "TruthValue", "RowStatus")
h3cBfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72))
h3cBfdMIB.setRevisions(('2006-05-16 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cBfdMIB.setRevisionsDescriptions(('The first version. ',))
if mibBuilder.loadTexts: h3cBfdMIB.setLastUpdated('200605081200Z')
if mibBuilder.loadTexts: h3cBfdMIB.setOrganization('H3C')
if mibBuilder.loadTexts: h3cBfdMIB.setContactInfo('huawei-3com, Inc. Email: huanglina@huawei-3com.com')
if mibBuilder.loadTexts: h3cBfdMIB.setDescription('Bidirectional Forwarding Management Information Base.')
h3cBfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 0))
h3cBfdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1))
h3cBfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 2))
h3cBfdGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1))
class BfdSessIndexTC(TextualConvention, Unsigned32):
    description = 'An index used to uniquely identify BFD sessions.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdInterval(TextualConvention, Unsigned32):
    description = 'A time interval delay in microseconds, which is used by the BFD.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdDiag(TextualConvention, Integer32):
    description = "The diagnostic code is used by the BFD specifying the local system's reason for the last session state change, and must be initialized to zero(No Diagnostic). The 'noDiagnostic' means the session keeps state up. The 'controlDetectionTimeExpired' indicates the reason the session enters state down from state up is that the control detection time expires. The 'echoFunctionFailed' indicates the reason the session enters state down from state up is that Echo Function fails. The 'neighborSignaledSessionDown' indicates the reason the session enters state down from state up is that neighbor signals session Down. The 'forwardingPlaneReset' indicates the reason the session enters state down from state up is that the Forwarding Plane resets. The 'pathDown' indicates the reason the session enters state down from state up is that the path state is down. The 'concatenatedPathDown' indicates the reason the session enters state down from state up is that the concatenated path state is down. The 'administrativelyDown' indicates the reason the session enters state down from state up is that the session is kept administratively down by entering the AdminDown state. The 'reverseConcatenatedPathDown' indicates the reason the session enters state down from state up is that reverse concatenated path state is down. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noDiagnostic", 1), ("controlDetectionTimeExpired", 2), ("echoFunctionFailed", 3), ("neighborSignaledSessionDown", 4), ("forwardingPlaneReset", 5), ("pathDown", 6), ("concatenatedPathDown", 7), ("administrativelyDown", 8), ("reverseConcatenatedPathDown", 9))

h3cBfdVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1, 1), Unsigned32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdVersionNumber.setReference('BFD Version 1 (draft-ietf-bfd-base-04.txt)')
if mibBuilder.loadTexts: h3cBfdVersionNumber.setStatus('current')
if mibBuilder.loadTexts: h3cBfdVersionNumber.setDescription("It indicates the BFD session's current version number.")
h3cBfdSysInitMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("passive", 2))).clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBfdSysInitMode.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSysInitMode.setDescription("A system may take either an active role or a passive role in session initialization. A system taking the active role must send BFD control packets for a particular session, regardless of whether it has received any BFD packets for that session. A system taking the passive role must not begin sending BFD packets for a particular session until it has received a BFD packet for that session, and thus has learned the remote system's discriminator value.")
h3cBfdIfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2), )
if mibBuilder.loadTexts: h3cBfdIfTable.setStatus('current')
if mibBuilder.loadTexts: h3cBfdIfTable.setDescription('This Table describes the BFD interface specific information.')
h3cBfdIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1), ).setIndexNames((0, "H3C-BFD-STD-MIB", "h3cBfdIfIndex"))
if mibBuilder.loadTexts: h3cBfdIfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cBfdIfEntry.setDescription('This Entry describes the BFD interface specific information.')
h3cBfdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cBfdIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cBfdIfIndex.setDescription('This variable contains an index that represents a unique BFD interface on this device.')
h3cBfdIfDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 2), BfdInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBfdIfDesiredMinTxInterval.setStatus('current')
if mibBuilder.loadTexts: h3cBfdIfDesiredMinTxInterval.setDescription('This variable defines the minimum interval, in microseconds, that the interface would like to use when transmitting BFD Control packets.')
h3cBfdIfDesiredMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 3), BfdInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBfdIfDesiredMinRxInterval.setStatus('current')
if mibBuilder.loadTexts: h3cBfdIfDesiredMinRxInterval.setDescription('This variable defines the minimum interval, in, microseconds, between received BFD Control packets the local system is capable of supporting.')
h3cBfdIfDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBfdIfDetectMult.setStatus('current')
if mibBuilder.loadTexts: h3cBfdIfDetectMult.setDescription('The desired detect time multiplier for BFD control packets. The negotiated control packet transmission interval, multiplied by this variable, will be the detection time for this session (as seen by the remote system.) The variable must be a nonzero integer.')
h3cBfdIfAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("simple", 2), ("md5", 3), ("mmd5", 4), ("sha1", 5), ("msha1", 6))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdIfAuthType.setStatus('current')
if mibBuilder.loadTexts: h3cBfdIfAuthType.setDescription("The Authentication Type used for this interface. This field is valid only when the Authentication Present bit is set. The 'none' indicates the session doesn't support authentication. The 'simple' indicates the session supports simple password authentication. The 'md5' indicates the session supports Keyed MD5 authentication. The 'mmd5' indicates the session supports Meticulous Keyed MD5 authentication. The 'sha1' indicates the session supports Keyed SHA1 authentication. The 'msha1' indicates the session supports Meticulous Keyed SHA1 authentication. ")
h3cBfdSessTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3), )
if mibBuilder.loadTexts: h3cBfdSessTable.setReference('BFD Version 1 (draft-ietf-bfd-base-04.txt)')
if mibBuilder.loadTexts: h3cBfdSessTable.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessTable.setDescription('This table describes the BFD sessions.')
h3cBfdSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1), ).setIndexNames((0, "H3C-BFD-STD-MIB", "h3cBfdSessIfIndex"), (0, "H3C-BFD-STD-MIB", "h3cBfdSessIndex"))
if mibBuilder.loadTexts: h3cBfdSessEntry.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessEntry.setDescription('This Entry describes the BFD sessions.')
h3cBfdSessIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cBfdSessIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessIfIndex.setDescription("This variable contains an interface's index under which the BFD session runs.")
h3cBfdSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 2), BfdSessIndexTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cBfdSessIndex.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessIndex.setDescription('This variable contains an index which represents a unique BFD session on this device.')
h3cBfdSessAppSupportId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 3), Bits().clone(namedValues=NamedValues(("none", 0), ("ospf", 1), ("isis", 2), ("bgp", 3), ("mpls", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessAppSupportId.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessAppSupportId.setDescription('This variable contains an ID used to indicate a local application which owns or maintains this BFD session. Note, a BFD session can support several route protocols. This is a bit-map of possible conditions. The corresponding bit positions are: |0 |none | |1 |ospf | |2 |isis | |3 |bgp | |4 |mpls | ')
h3cBfdSessLocalDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessLocalDiscr.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessLocalDiscr.setDescription('This variable defines the local discriminator for this BFD session, used to uniquely identify it.')
h3cBfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessRemoteDiscr.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessRemoteDiscr.setDescription('This variable defines the session discriminator chosen by the remote system for this BFD session.')
h3cBfdSessDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 6), InetPortNumber().clone(3784)).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessDstPort.setReference('BFD Version 1 (draft-ietf-bfd-base-04.txt)')
if mibBuilder.loadTexts: h3cBfdSessDstPort.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessDstPort.setDescription('The UDP Port for BFD. The default value is the well-known value for this port.')
h3cBfdSessOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("asynchModeWOEchoFun", 1), ("demandModeWOEchoFunction", 2), ("asyncModeWEchoFun", 3), ("demandModeWEchoFunction", 4))).clone('asynchModeWOEchoFun')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessOperMode.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessOperMode.setDescription("This variable defines current operating mode that BFD session is running in. The primary mode which the BFD session runs in is known as Asynchronous mode. In this mode, the systems periodically send BFD Control packets to one another, and if a number of those packets in a row are not received by the other system, the session is declared to be down. The second mode is known as Demand mode. In this mode, it is assumed that each system has an independent way of verifying that it has connectivity to the other system. Once a BFD session is established, the systems stop sending BFD Control packets, except when either system feels the need to verify connectivity explicitly, in which case a short sequence of BFD Control packets is sent, and then the protocol quiesces. An adjunct to both modes is the Echo function. When the Echo function is active, a stream of BFD Echo packets is transmitted in such a way as to have the other system loop them back through its forwarding path. If a number of packets of the echoed data stream are not received, the session is declared to be down. The Echo function may be used with either Asynchronous or Demand modes. The 'asynchModeWOEchoFun' indicates this BFD session operates in the Asynchronous mode, and doesn't support the Echo Function. The 'demandModeWOEchoFunction' indicates this BFD session operates in the Demand mode, and doesn't support the Echo Function. The 'asyncModeWEchoFun' indicates this BFD session operates in the Asynchronous mode, and also supports the Echo Function. The 'demandModeWEchoFunction' indicates this BFD session operates in the Demand mode, and also supports the Echo Function. ")
h3cBfdSessAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 8), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessAddrType.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessAddrType.setDescription('This object defines IP address type of the interface associated with this BFD session. Only values unknown(0), ipv4(1) or ipv6(2) have to be supported. A value of unknown(0) is allowed only when the outgoing interface is of type point-to-point, or when the BFD session is not associated with a specific interface. If any other unsupported values are attempted in a set operation, the agent must return an inconsistentValue error. ')
h3cBfdSessLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 9), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessLocalAddr.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessLocalAddr.setDescription('This variable defines IP address of the local interface from which the BFD packets is transmitted. It can also be used to enabled BFD on a specific interface. The value is set to zero when BFD session is not associated with a specific interface.')
h3cBfdSessRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessRemoteAddr.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessRemoteAddr.setDescription('This variable defines IP address of the remote interface from which the BFD packets is transmitted. It can also be used to enabled BFD on a specific interface. The value is set to zero when BFD session is not associated with a specific interface. ')
h3cBfdSessLocalDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 11), BfdDiag().clone('noDiagnostic')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessLocalDiag.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessLocalDiag.setDescription('The BFD diagnostic code for the BFD session was down with the neighbor. If no such event happens this object contains a zero value.')
h3cBfdSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("adminDown", 0), ("down", 1), ("init", 2), ("up", 3))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessState.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessState.setDescription('The state of the running BFD session. There are three states through which a session normally proceeds, two for establishing a session (Init and Up) and one for tearing down a session (Down.) This allows a three-way handshake for both session establishment and session teardown (assuring that both systems are aware of all session state changes.) A fourth state (AdminDown) exists so that a session can be administratively put down indefinitely. The Down state means that the session is down (or has just been created.) A session remains in Down state until the remote system indicates that it agrees that the session is down by sending a BFD Control packet with the State field set to anything other than Up. If that packet signals Down state, the session advances to Init state; if that packet signals Init state, the session advances to Up state. Init state means that the remote system is 0communicating, and the local system desires to bring the session up, but the remote system does not yet realize it. A session will remain in Init state until either a BFD Control Packet is received that is signaling Init or Up state (in which case the session advances to Up state) or until the detection time expires, meaning that communication with the remote system has been lost (in which case the session advances to Down state.) Up state means that the BFD session has successfully been established, and implies that connectivity between the systems is working. The session will remain in the Up state until either connectivity fails, or the session is taken down administratively. If either the remote system signals Down state, or the detection time expires, the session advances to Down state. AdminDown state means that the session is being held administratively down. This causes the remote system to enter Down state, and remain there until the local system exits AdminDown state. ')
h3cBfdSessControlPlanIndepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 13), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessControlPlanIndepFlag.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessControlPlanIndepFlag.setDescription('This variable indicates whether the local system can continue to work while the control plane is out of work. Specifically, it is set to true(1) if the local system is independent of the control plane. Otherwise, the value is set to false(0)')
h3cBfdSessAuthFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 14), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessAuthFlag.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessAuthFlag.setDescription('This variable indicates that the local system wants to use Authentication. Specifically, it is set to true(1) if the local system wishes the session to be authenticated or false(0) if not.')
h3cBfdSessDemandModeFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 3, 1, 15), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessDemandModeFlag.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessDemandModeFlag.setDescription('This variable indicates that the local system wants to use Demand mode. Specifically, it is set to true(1) if the local system wishes to use Demand mode or false(0) if not')
h3cBfdSessStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4), )
if mibBuilder.loadTexts: h3cBfdSessStatTable.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStatTable.setDescription('The table defines BFD session state.')
h3cBfdSessStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1), )
h3cBfdSessEntry.registerAugmentions(("H3C-BFD-STD-MIB", "h3cBfdSessStatEntry"))
h3cBfdSessStatEntry.setIndexNames(*h3cBfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: h3cBfdSessStatEntry.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStatEntry.setDescription('An entry in this table is created by a BFD-enabled node for every BFD Session. It defines BFD session statistics.')
h3cBfdSessStatPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessStatPktInHC.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStatPktInHC.setDescription('The total number of BFD messages received by this BFD session.')
h3cBfdSessStatPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessStatPktOutHC.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStatPktOutHC.setDescription('The total number of BFD messages sent by this BFD session.')
h3cBfdSessStatDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessStatDownCount.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStatDownCount.setDescription('The number of times this session has gone into the Down state since the router last rebooted.')
h3cBfdSessStatPktDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessStatPktDiscard.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStatPktDiscard.setDescription('The number of packets the local system has discarded since the router last rebooted.')
h3cBfdSessStatPktLost = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessStatPktLost.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStatPktLost.setDescription('The number of packets the local system has failed to transmit since the router last rebooted.')
h3cBfdSessPerfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5), )
if mibBuilder.loadTexts: h3cBfdSessPerfTable.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessPerfTable.setDescription('The table defines BFD session performance.')
h3cBfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1), )
h3cBfdSessEntry.registerAugmentions(("H3C-BFD-STD-MIB", "h3cBfdSessPerfEntry"))
h3cBfdSessPerfEntry.setIndexNames(*h3cBfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: h3cBfdSessPerfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessPerfEntry.setDescription('An entry in this table is created by a BFD-enabled node for every BFD session. It defines BFD Session performance.')
h3cBfdSessPerfCreatTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessPerfCreatTime.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessPerfCreatTime.setDescription('The value of sysUpTime when the session was created. If no such create event exists this object contains a zero value.')
h3cBfdSessPerfLastUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessPerfLastUpTime.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessPerfLastUpTime.setDescription('The value of sysUpTime when the last time communication was lost. If no such up event exists this variable contains a zero value.')
h3cBfdSessPerfLastDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBfdSessPerfLastDownTime.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessPerfLastDownTime.setDescription('The value of sysUpTime when the last time communication was lost with the neighbor. If no such event exist this variable contains a zero value.')
h3cBfdSessNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBfdSessNotificationsEnable.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessNotificationsEnable.setDescription('This variable enables the emission of h3cBfdSessStateChange and h3cBfdSessAuthFail notifications if this variable is set to true(1); otherwise these notifications are not emitted.')
h3cBfdSessStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 0, 1)).setObjects(("H3C-BFD-STD-MIB", "h3cBfdSessIfIndex"), ("H3C-BFD-STD-MIB", "h3cBfdSessIndex"), ("H3C-BFD-STD-MIB", "h3cBfdSessState"))
if mibBuilder.loadTexts: h3cBfdSessStateChange.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessStateChange.setDescription("A notification sent when an session changes state, entering state up or entering state down. The session will enter state up finishing three times handshakes , and will enter state down when the communication path is out of work. When the h3cBfdSessState's value is state up, the session enters state up, and the session enters state down when the h3cBfdSessState's value is state down. The h3cBfdSessIfIndex contains an interface's index under which the BFD session runs. The h3cBfdSessIndex contains an index which represents a unique BFD session on this device. The h3cBfdSessState is the state of the running BFD session. ")
h3cBfdSessAuthFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 72, 0, 2)).setObjects(("H3C-BFD-STD-MIB", "h3cBfdIfIndex"))
if mibBuilder.loadTexts: h3cBfdSessAuthFail.setStatus('current')
if mibBuilder.loadTexts: h3cBfdSessAuthFail.setDescription('A notification sent when receiving a session with an authentication fail. The h3cBfdIfIndex is an index which represents a unique BFD interface on this device. ')
mibBuilder.exportSymbols("H3C-BFD-STD-MIB", h3cBfdSessState=h3cBfdSessState, h3cBfdSessLocalAddr=h3cBfdSessLocalAddr, h3cBfdSessIndex=h3cBfdSessIndex, h3cBfdIfEntry=h3cBfdIfEntry, h3cBfdSessRemoteDiscr=h3cBfdSessRemoteDiscr, h3cBfdSessStatEntry=h3cBfdSessStatEntry, h3cBfdSessDstPort=h3cBfdSessDstPort, h3cBfdSessPerfCreatTime=h3cBfdSessPerfCreatTime, h3cBfdSessPerfEntry=h3cBfdSessPerfEntry, h3cBfdObjects=h3cBfdObjects, h3cBfdSessControlPlanIndepFlag=h3cBfdSessControlPlanIndepFlag, h3cBfdSessAuthFlag=h3cBfdSessAuthFlag, h3cBfdSessStateChange=h3cBfdSessStateChange, h3cBfdGlobalObjects=h3cBfdGlobalObjects, h3cBfdSessStatPktLost=h3cBfdSessStatPktLost, BfdSessIndexTC=BfdSessIndexTC, h3cBfdSessStatPktDiscard=h3cBfdSessStatPktDiscard, h3cBfdSessOperMode=h3cBfdSessOperMode, h3cBfdConformance=h3cBfdConformance, h3cBfdSessStatDownCount=h3cBfdSessStatDownCount, h3cBfdSessPerfTable=h3cBfdSessPerfTable, h3cBfdSessIfIndex=h3cBfdSessIfIndex, h3cBfdSessLocalDiag=h3cBfdSessLocalDiag, h3cBfdSessRemoteAddr=h3cBfdSessRemoteAddr, h3cBfdSessLocalDiscr=h3cBfdSessLocalDiscr, h3cBfdSessPerfLastUpTime=h3cBfdSessPerfLastUpTime, h3cBfdNotifications=h3cBfdNotifications, BfdDiag=BfdDiag, PYSNMP_MODULE_ID=h3cBfdMIB, h3cBfdIfDesiredMinTxInterval=h3cBfdIfDesiredMinTxInterval, h3cBfdIfDetectMult=h3cBfdIfDetectMult, h3cBfdSessStatTable=h3cBfdSessStatTable, h3cBfdSessStatPktOutHC=h3cBfdSessStatPktOutHC, h3cBfdSessStatPktInHC=h3cBfdSessStatPktInHC, h3cBfdIfDesiredMinRxInterval=h3cBfdIfDesiredMinRxInterval, h3cBfdSessPerfLastDownTime=h3cBfdSessPerfLastDownTime, h3cBfdSessAddrType=h3cBfdSessAddrType, h3cBfdIfTable=h3cBfdIfTable, h3cBfdSessAuthFail=h3cBfdSessAuthFail, h3cBfdSessEntry=h3cBfdSessEntry, h3cBfdSessDemandModeFlag=h3cBfdSessDemandModeFlag, h3cBfdSessNotificationsEnable=h3cBfdSessNotificationsEnable, h3cBfdSessTable=h3cBfdSessTable, BfdInterval=BfdInterval, h3cBfdIfIndex=h3cBfdIfIndex, h3cBfdSessAppSupportId=h3cBfdSessAppSupportId, h3cBfdIfAuthType=h3cBfdIfAuthType, h3cBfdVersionNumber=h3cBfdVersionNumber, h3cBfdMIB=h3cBfdMIB, h3cBfdSysInitMode=h3cBfdSysInitMode)
