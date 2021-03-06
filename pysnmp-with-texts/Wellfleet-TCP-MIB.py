#
# PySNMP MIB module Wellfleet-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-TCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Integer32, TimeTicks, iso, Counter64, Unsigned32, Counter32, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Integer32", "TimeTicks", "iso", "Counter64", "Unsigned32", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfTcpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfTcpGroup")
wfTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1))
wfTcpDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTcpDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete TCP.')
wfTcpDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTcpDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpDisable.setDescription('Enable/Disable parameter. Default is enabled. Users perform a set operation on this object in order to enable/disable TCP.')
wfTcpState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpState.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpState.setDescription('The current state of the entire TCP.')
wfTcpRtoAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4))).clone('vanj')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpRtoAlgorithm.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpRtoAlgorithm.setDescription('The algorithm used to determine the timeout value used for retransmitting unacknowledged octets.')
wfTcpRtoMin = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 15000)).clone(250)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTcpRtoMin.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpRtoMin.setDescription('The minimum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout. In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the LBOUND quantity described in RFC 793.')
wfTcpRtoMax = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15000, 240000)).clone(240000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTcpRtoMax.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpRtoMax.setDescription('The maximum value permitted by a TCP implementation for the retransmission timeout, measured in milliseconds. More refined semantics for objects of this type depend upon the algorithm used to determine the retransmission timeout. In particular, when the timeout algorithm is rsre(3), an object of this type has the semantics of the UBOUND quantity described in RFC 793.')
wfTcpMaxConn = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpMaxConn.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpMaxConn.setDescription('The limit on the total number of TCP connections the entity can support. In entities where the maximum number of connections is dynamic, this object should contain the value -1.')
wfTcpActiveOpens = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpActiveOpens.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpActiveOpens.setDescription('The number of times TCP connections have made a direct transition to the SYN-SENT state from the CLOSED state.')
wfTcpPassiveOpens = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpPassiveOpens.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpPassiveOpens.setDescription('The number of times TCP connections have made a direct transition to the SYN-RCVD state from the LISTEN state.')
wfTcpAttemptFails = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpAttemptFails.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpAttemptFails.setDescription('The number of times TCP connections have made a direct transition to the CLOSED state from either the SYN-SENT state or the SYN-RCVD state, plus the number of times TCP connections have made a direct transition to the LISTEN state from the SYN-RCVD state.')
wfTcpEstabResets = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpEstabResets.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpEstabResets.setDescription('The number of times TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE-WAIT state.')
wfTcpCurrEstab = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpCurrEstab.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpCurrEstab.setDescription('The number of TCP connections for which the current state is either ESTABLISHED or CLOSE- WAIT.')
wfTcpInSegs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpInSegs.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpInSegs.setDescription('The total number of segments received, including those received in error. This count includes segments received on currently established connections.')
wfTcpOutSegs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpOutSegs.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpOutSegs.setDescription('The total number of segments sent, including those on current connections but excluding those containing only retransmitted octets.')
wfTcpRetransSegs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpRetransSegs.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpRetransSegs.setDescription('The total number of segments retransmitted - that is, the number of TCP segments transmitted containing one or more previously transmitted octets.')
wfTcpInErrs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpInErrs.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpInErrs.setDescription('The total number of segments received in error (e.g., bad TCP checksums).')
wfTcpOutRsts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpOutRsts.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpOutRsts.setDescription('The number of TCP segments sent containing the RST flag.')
wfTcpMaxWindow = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 65535)).clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTcpMaxWindow.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpMaxWindow.setDescription('The maximum transmit and receive window size TCP will allow for each connection measured in octets.')
wfTcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2), )
if mibBuilder.loadTexts: wfTcpConnTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnTable.setDescription("The TCP connection table contains information about this entity's existing TCP connections.")
wfTcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1), ).setIndexNames((0, "Wellfleet-TCP-MIB", "wfTcpConnLocalAddress"), (0, "Wellfleet-TCP-MIB", "wfTcpConnLocalPort"), (0, "Wellfleet-TCP-MIB", "wfTcpConnRemAddress"), (0, "Wellfleet-TCP-MIB", "wfTcpConnRemPort"))
if mibBuilder.loadTexts: wfTcpConnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnEntry.setDescription('A TCP Connection')
wfTcpConnDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTcpConnDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnDelete.setDescription('The Delete connection attribute. Users set this attribute to a value of TCP_CONN_STATE_DELETE to delete a TCP connection. This is the only value that can be written. The instance should never get created by a user writing to this attribute.')
wfTcpConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synsent", 3), ("synreceived", 4), ("established", 5), ("finwait1", 6), ("finwait2", 7), ("closewait", 8), ("lastack", 9), ("closing", 10), ("timewait", 11), ("deletetcb", 12))).clone('closed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnState.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnState.setDescription("The state of this TCP connection. The only value which may be set by a management station is deleteTCB(12). Accordingly, it is appropriate for an agent to return a `badValue' response if a management station attempts to set this object to any other value. If a management station sets this object to the value deleteTCB(12), then this has the effect of deleting the TCB (as defined in RFC 793) of the corresponding connection on the managed node, resulting in immediate termination of the connection. As an implementation-specific option, a RST segment may be sent from the managed node to the other TCP endpoint (note however that RST segments are not sent reliably).")
wfTcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnLocalAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnLocalAddress.setDescription('The local IP address for this TCP connection. In the case of a connection in the listen state which is willing to accept connections for any IP interface associated with the node, the value 0.0.0.0 is used.')
wfTcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnLocalPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnLocalPort.setDescription('The local port number for this TCP connection')
wfTcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnRemAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnRemAddress.setDescription('The remote IP address for this TCP connection.')
wfTcpConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnRemPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnRemPort.setDescription('The remote port number for this TCP connection.')
wfTcpConnKeepAliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnKeepAliveInterval.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnKeepAliveInterval.setDescription('The Interval(seconds) during which no packet has been received on a session. A PROBE packet is sent to elicit an ACK. Value passed by application in tcp_open or tcp_accept.')
wfTcpConnKeepAliveRto = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnKeepAliveRto.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnKeepAliveRto.setDescription('Keep Alive Retransmit timer (seconds) after which a PROBE packet is sent again if no response has been received. Value passed by application in tcp_open or tcp_accept.')
wfTcpConnKeepAliveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnKeepAliveCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnKeepAliveCount.setDescription('The current number of consecutive Keep-Alive PROBES sent.')
wfTcpConnMd5Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTcpConnMd5Errors.setStatus('mandatory')
if mibBuilder.loadTexts: wfTcpConnMd5Errors.setDescription('A count of the number of TCP packets dropped \\ due to MD5 authentication errors')
mibBuilder.exportSymbols("Wellfleet-TCP-MIB", wfTcpRtoAlgorithm=wfTcpRtoAlgorithm, wfTcpRtoMin=wfTcpRtoMin, wfTcpDisable=wfTcpDisable, wfTcp=wfTcp, wfTcpState=wfTcpState, wfTcpConnLocalPort=wfTcpConnLocalPort, wfTcpConnEntry=wfTcpConnEntry, wfTcpConnTable=wfTcpConnTable, wfTcpCurrEstab=wfTcpCurrEstab, wfTcpConnDelete=wfTcpConnDelete, wfTcpRetransSegs=wfTcpRetransSegs, wfTcpConnKeepAliveInterval=wfTcpConnKeepAliveInterval, wfTcpConnKeepAliveCount=wfTcpConnKeepAliveCount, wfTcpConnRemAddress=wfTcpConnRemAddress, wfTcpMaxConn=wfTcpMaxConn, wfTcpInErrs=wfTcpInErrs, wfTcpPassiveOpens=wfTcpPassiveOpens, wfTcpOutRsts=wfTcpOutRsts, wfTcpConnLocalAddress=wfTcpConnLocalAddress, wfTcpConnKeepAliveRto=wfTcpConnKeepAliveRto, wfTcpDelete=wfTcpDelete, wfTcpInSegs=wfTcpInSegs, wfTcpMaxWindow=wfTcpMaxWindow, wfTcpEstabResets=wfTcpEstabResets, wfTcpRtoMax=wfTcpRtoMax, wfTcpAttemptFails=wfTcpAttemptFails, wfTcpOutSegs=wfTcpOutSegs, wfTcpConnMd5Errors=wfTcpConnMd5Errors, wfTcpConnState=wfTcpConnState, wfTcpActiveOpens=wfTcpActiveOpens, wfTcpConnRemPort=wfTcpConnRemPort)
