#
# PySNMP MIB module FCIP-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FCIP-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
FcNameIdOrZero, = mibBuilder.importSymbols("FC-MGMT-MIB", "FcNameIdOrZero")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, IpAddress, Unsigned32, NotificationType, ModuleIdentity, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, MibIdentifier, Gauge32, mib_2, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Unsigned32", "NotificationType", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "MibIdentifier", "Gauge32", "mib-2", "Bits")
DisplayString, RowStatus, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")
fcipMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 224))
fcipMIB.setRevisions(('2006-02-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fcipMIB.setRevisionsDescriptions(('Initial version of this module, published as RFC 4404.',))
if mibBuilder.loadTexts: fcipMIB.setLastUpdated('200602060000Z')
if mibBuilder.loadTexts: fcipMIB.setOrganization('IETF IPFC Working Group')
if mibBuilder.loadTexts: fcipMIB.setContactInfo('Anil Rijhsinghani Accton Technology Corporation 5 Mount Royal Ave Marlboro, MA 01752 USA. Ravi Natarajan F5 Networks 2460 North First Street, Suite 100 San Jose, CA 95131 USA.')
if mibBuilder.loadTexts: fcipMIB.setDescription('The module defines management information specific to FCIP devices. Copyright(C) The Internet Society (2006). This version of this MIB module is part of RFC 4404; see the RFC itself for full legal notices.')
fcipObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 224, 1))
fcipConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 224, 2))
fcipConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 224, 1, 1))
class FcipDomainIdInOctetForm(TextualConvention, OctetString):
    reference = 'FC-SW-3 section 4.8'
    description = 'The Domain ID of a FC entity in octet form to support the concatenation(000000h||Domain_ID) format defined in the FSPF routing protocol.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class FcipEntityMode(TextualConvention, Integer32):
    reference = 'FC-BB, rev 4.7, 2 May 1997, section 3.'
    description = 'The type of port mode provided by an FCIP Entity for an FCIP Link. An FCIP Entity can be an E-Port mode for one of its FCIP Link Endpoints or a B-Port mode for another of its FCIP Link Endpoints.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ePortMode", 1), ("bPortMode", 2))

class FcipEntityId(TextualConvention, OctetString):
    reference = 'RFC 3821, Section 7.1, FCIP Special Frame Format'
    description = 'The FCIP entity identifier as defined in RFC 3821.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

fcipDynIpConfType = MibScalar((1, 3, 6, 1, 2, 1, 224, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("slpv2", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcipDynIpConfType.setStatus('current')
if mibBuilder.loadTexts: fcipDynIpConfType.setDescription('The type of discovery protocol used to discover remote FCIP entities. The value of this object is persistent across system restarts.')
fcipDeviceWWN = MibScalar((1, 3, 6, 1, 2, 1, 224, 1, 1, 2), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipDeviceWWN.setStatus('current')
if mibBuilder.loadTexts: fcipDeviceWWN.setDescription('The World Wide Name of this FCIP device.')
fcipEntitySACKOption = MibScalar((1, 3, 6, 1, 2, 1, 224, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipEntitySACKOption.setReference('The Selective Ack option is defined in RFC 2883.')
if mibBuilder.loadTexts: fcipEntitySACKOption.setStatus('current')
if mibBuilder.loadTexts: fcipEntitySACKOption.setDescription('Indication of whether the TCP Selective Acknowledgement Option is enabled at this FCIP device to let the receiver acknowledge multiple lost packets in a single ACK for faster recovery.')
fcipEntityInstanceTable = MibTable((1, 3, 6, 1, 2, 1, 224, 1, 1, 4), )
if mibBuilder.loadTexts: fcipEntityInstanceTable.setReference('RFC 3821, Section 5.4, FCIP Entity')
if mibBuilder.loadTexts: fcipEntityInstanceTable.setStatus('current')
if mibBuilder.loadTexts: fcipEntityInstanceTable.setDescription("Information about this FCIP device's existing instances of FCIP entities.")
fcipEntityInstanceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1), ).setIndexNames((0, "FCIP-MGMT-MIB", "fcipEntityId"))
if mibBuilder.loadTexts: fcipEntityInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: fcipEntityInstanceEntry.setDescription('A conceptual row of the FCIP entity table with information about a particular FCIP entity. Once a row has been created, it is non-volatile across agent restarts until it is deleted.')
fcipEntityId = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 1), FcipEntityId())
if mibBuilder.loadTexts: fcipEntityId.setReference('RFC 3821, Section 7.1, FCIP Special Frame Format')
if mibBuilder.loadTexts: fcipEntityId.setStatus('current')
if mibBuilder.loadTexts: fcipEntityId.setDescription('The FCIP entity identifier.')
fcipEntityName = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipEntityName.setStatus('current')
if mibBuilder.loadTexts: fcipEntityName.setDescription('An administratively-assigned name for this FCIP entity.')
fcipEntityAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipEntityAddressType.setStatus('current')
if mibBuilder.loadTexts: fcipEntityAddressType.setDescription('The type of Internet address by which the entity is reachable. Only address types IPv4 and IPv6 are supported.')
fcipEntityAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipEntityAddress.setStatus('current')
if mibBuilder.loadTexts: fcipEntityAddress.setDescription('The Internet address for the entity, if configured. The format of this address is determined by the value of the fcipEntityAddressType object.')
fcipEntityTcpConnPort = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 5), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipEntityTcpConnPort.setStatus('current')
if mibBuilder.loadTexts: fcipEntityTcpConnPort.setDescription('A TCP port other than the FCIP Well-Known port on which the FCIP entity listens for new TCP connection requests. It contains the value zero(0) if the FCIP Entity only listens on the Well-Known port.')
fcipEntitySeqNumWrap = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipEntitySeqNumWrap.setReference('The PAWS option is defined in RFC 1323.')
if mibBuilder.loadTexts: fcipEntitySeqNumWrap.setStatus('current')
if mibBuilder.loadTexts: fcipEntitySeqNumWrap.setDescription('An indication of whether the FCIP Entity supports protection against sequence number wrap.')
fcipEntityPHBSupport = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipEntityPHBSupport.setReference('Per hop behavior is defined in RFC 2474, definition of the Differentiated Services Field.')
if mibBuilder.loadTexts: fcipEntityPHBSupport.setStatus('current')
if mibBuilder.loadTexts: fcipEntityPHBSupport.setDescription('An indication of whether the FCIP Entity supports PHB IP quality of service (QoS).')
fcipEntityStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipEntityStatus.setStatus('current')
if mibBuilder.loadTexts: fcipEntityStatus.setDescription('This object specifies the operational status of the row. When a management station sets the status to active(1), then the values for the objects fcipEntityName, fcipEntityAddressType, and fcipEntityAddress should be supplied as part of the set request. The values of the objects fcipEntityName, fcipEntityAddressType, and fcipEntityAddress can be changed if the row status is in active state. The object fcipEntityTcpConnPort takes the default value zero(0), if no value is supplied at the time of row creation. Setting the status to destroy(6) deletes the specified FCIP entity instance row from the table. It also deletes all the rows corresponding to the specified FCIP entity from the fcipLinkTable and fcipTcpConnTable tables.')
fcipLinkTable = MibTable((1, 3, 6, 1, 2, 1, 224, 1, 1, 5), )
if mibBuilder.loadTexts: fcipLinkTable.setStatus('current')
if mibBuilder.loadTexts: fcipLinkTable.setDescription('Information about FCIP links that exist on this device.')
fcipLinkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1), ).setIndexNames((0, "FCIP-MGMT-MIB", "fcipEntityId"), (0, "FCIP-MGMT-MIB", "fcipLinkIndex"))
if mibBuilder.loadTexts: fcipLinkEntry.setStatus('current')
if mibBuilder.loadTexts: fcipLinkEntry.setDescription('A conceptual row of the FCIP link table containing information about a particular FCIP link. The values of the read-create objects in this table are persistent across system restarts.')
fcipLinkIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: fcipLinkIndex.setStatus('current')
if mibBuilder.loadTexts: fcipLinkIndex.setDescription('An arbitrary integer that uniquely identifies one FCIP link within an FCIP entity.')
fcipLinkIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkIfIndex.setStatus('current')
if mibBuilder.loadTexts: fcipLinkIfIndex.setDescription('The ifIndex value of the virtual interface corresponding to the FCIP Link running over TCP/IP.')
fcipLinkCost = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkCost.setStatus('current')
if mibBuilder.loadTexts: fcipLinkCost.setDescription('The FSPF cost associated with this FCIP Link.')
fcipLinkLocalFcipEntityMode = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 4), FcipEntityMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkLocalFcipEntityMode.setStatus('current')
if mibBuilder.loadTexts: fcipLinkLocalFcipEntityMode.setDescription('The mode of the local end of the FCIP link.')
fcipLinkLocalFcipEntityAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkLocalFcipEntityAddressType.setStatus('current')
if mibBuilder.loadTexts: fcipLinkLocalFcipEntityAddressType.setDescription('The type of Internet address contained in the corresponding instance of fcipLinkLocalFcipEntityAddress. Only address types IPv4 and IPv6 are supported.')
fcipLinkLocalFcipEntityAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkLocalFcipEntityAddress.setStatus('current')
if mibBuilder.loadTexts: fcipLinkLocalFcipEntityAddress.setDescription('The Internet address for the local end of this FCIP Link. The format of this object is determined by the value of the fcipLinkLocalFcipEntityAddressType object.')
fcipLinkRemFcipEntityWWN = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 7), FcNameIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkRemFcipEntityWWN.setReference('RFC 3821, Section 7.1, FCIP Special Frame Format')
if mibBuilder.loadTexts: fcipLinkRemFcipEntityWWN.setStatus('current')
if mibBuilder.loadTexts: fcipLinkRemFcipEntityWWN.setDescription('The World Wide Name of the remote FC Fabric Entity.')
fcipLinkRemFcipEntityId = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 8), FcipEntityId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkRemFcipEntityId.setReference('RFC 3821, Section 7.1, FCIP Special Frame Format')
if mibBuilder.loadTexts: fcipLinkRemFcipEntityId.setStatus('current')
if mibBuilder.loadTexts: fcipLinkRemFcipEntityId.setDescription("The remote FCIP entity's identifier.")
fcipLinkRemFcipEntityAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 9), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkRemFcipEntityAddressType.setStatus('current')
if mibBuilder.loadTexts: fcipLinkRemFcipEntityAddressType.setDescription('The type of Internet address contained in the corresponding instance of fcipLinkRemFcipEntityAddress. Only address types IPv4 and IPv6 are supported.')
fcipLinkRemFcipEntityAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 10), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkRemFcipEntityAddress.setStatus('current')
if mibBuilder.loadTexts: fcipLinkRemFcipEntityAddress.setDescription('The Internet address for the remote end of this FCIP Link. The format of this object is determined by the value of the fcipLinkRemFcipEntityAddressType object.')
fcipLinkStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipLinkStatus.setStatus('current')
if mibBuilder.loadTexts: fcipLinkStatus.setDescription('This object specifies the operational status of the row. The values of objects fcipLinkLocalFcipEntityAddressType, fcipLinkLocalFcipEntityAddress, fcipLinkRemFcipEntityWWN, fcipLinkRemFcipEntityId, fcipLinkRemFcipEntityAddressType, and fcipLinkRemFcipEntityAddress can be changed if the row is in active(1) state. The object fcipLinkCost is set to the value zero(0) if no value is supplied at the time of row creation. Setting the status to destroy(6) deletes the specified FCIP link from the table. It also deletes all rows corresponding to the specified FCIP link from the fcipTcpConnTable table.')
fcipLinkCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkCreateTime.setStatus('current')
if mibBuilder.loadTexts: fcipLinkCreateTime.setDescription('The value of sysUpTime when this entry was last created.')
fcipTcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 224, 1, 1, 6), )
if mibBuilder.loadTexts: fcipTcpConnTable.setStatus('current')
if mibBuilder.loadTexts: fcipTcpConnTable.setDescription('Information about existing TCP connections. Each FCIP link within an FCIP entity manages one or more TCP connections. The FCIP entity employs a Data Engine for each TCP connection for handling FC frame encapsulation, de-encapsulation, and transmission of FCIP frames on the connection.')
fcipTcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1), ).setIndexNames((0, "FCIP-MGMT-MIB", "fcipEntityId"), (0, "FCIP-MGMT-MIB", "fcipLinkIndex"), (0, "FCIP-MGMT-MIB", "fcipTcpConnLocalPort"), (0, "FCIP-MGMT-MIB", "fcipTcpConnRemPort"))
if mibBuilder.loadTexts: fcipTcpConnEntry.setStatus('current')
if mibBuilder.loadTexts: fcipTcpConnEntry.setDescription('A conceptual row of the FCIP TCP Connection table containing information about a particular TCP connection.')
fcipTcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 1), InetPortNumber())
if mibBuilder.loadTexts: fcipTcpConnLocalPort.setStatus('current')
if mibBuilder.loadTexts: fcipTcpConnLocalPort.setDescription('The local port number for this TCP connection.')
fcipTcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 2), InetPortNumber())
if mibBuilder.loadTexts: fcipTcpConnRemPort.setStatus('current')
if mibBuilder.loadTexts: fcipTcpConnRemPort.setDescription('The remote port number for this TCP connection.')
fcipTcpConnRWSize = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipTcpConnRWSize.setStatus('current')
if mibBuilder.loadTexts: fcipTcpConnRWSize.setDescription('The default maximum TCP Receiver Window size for this TCP connection.')
fcipTcpConnMSS = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipTcpConnMSS.setStatus('current')
if mibBuilder.loadTexts: fcipTcpConnMSS.setDescription('The TCP Maximum Segment Size (MSS) for this TCP connection.')
fcipDynamicRouteTable = MibTable((1, 3, 6, 1, 2, 1, 224, 1, 1, 7), )
if mibBuilder.loadTexts: fcipDynamicRouteTable.setStatus('current')
if mibBuilder.loadTexts: fcipDynamicRouteTable.setDescription('Information about dynamically discovered routing information. The FCIP device may use the SLPv2 protocol in conjunction with other protocols (say, FSPF) for dynamically discovering other FCIP entities and may populate this table with FCIP link information for each Destination Address Identifier.')
fcipDynamicRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 224, 1, 1, 7, 1), ).setIndexNames((0, "FCIP-MGMT-MIB", "fcipEntityId"), (0, "FCIP-MGMT-MIB", "fcipDynamicRouteDID"))
if mibBuilder.loadTexts: fcipDynamicRouteEntry.setStatus('current')
if mibBuilder.loadTexts: fcipDynamicRouteEntry.setDescription('A conceptual row of the FCIP Dynamic Route Table containing information about a particular FCIP route.')
fcipDynamicRouteDID = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 7, 1, 1), FcipDomainIdInOctetForm())
if mibBuilder.loadTexts: fcipDynamicRouteDID.setStatus('current')
if mibBuilder.loadTexts: fcipDynamicRouteDID.setDescription('8-bit ID of a Fibre Channel Domain that is reachable from this FCIP device.')
fcipDynamicRouteLinkIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipDynamicRouteLinkIndex.setStatus('current')
if mibBuilder.loadTexts: fcipDynamicRouteLinkIndex.setDescription('The FCIP Link used to reach the domain specified by the corresponding instance of fcipDynamicRouteDID. The link identified by a value of this object is the same FCIP link as identified by the same value of fcipLinkIndex for the same FCIP entity.')
fcipStaticRouteTable = MibTable((1, 3, 6, 1, 2, 1, 224, 1, 1, 8), )
if mibBuilder.loadTexts: fcipStaticRouteTable.setStatus('current')
if mibBuilder.loadTexts: fcipStaticRouteTable.setDescription('Information about static route entries configured by the Network Admin. In the absence of dynamic discovery of remote FCIP entities, the Network Manager will figure out all remote FCIP devices that are reachable from this device and populate this table with FCIP link information for each Domain ID. At any time, both static and dynamic routing can be active, and an entry in the static route table for a given DID takes precedence over the entry in the dynamic route table for the same Domain ID.')
fcipStaticRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1), ).setIndexNames((0, "FCIP-MGMT-MIB", "fcipEntityId"), (0, "FCIP-MGMT-MIB", "fcipStaticRouteDID"))
if mibBuilder.loadTexts: fcipStaticRouteEntry.setStatus('current')
if mibBuilder.loadTexts: fcipStaticRouteEntry.setDescription('A conceptual row of the FCIP Static Route Table containing information about a particular FCIP route. The values of the read-create objects in this table are persistent across system restarts.')
fcipStaticRouteDID = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1, 1), FcipDomainIdInOctetForm())
if mibBuilder.loadTexts: fcipStaticRouteDID.setStatus('current')
if mibBuilder.loadTexts: fcipStaticRouteDID.setDescription('8-bit ID of a Fibre Channel Domain that is reachable from this FCIP device.')
fcipStaticRouteLinkIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipStaticRouteLinkIndex.setStatus('current')
if mibBuilder.loadTexts: fcipStaticRouteLinkIndex.setDescription('The FCIP Link used to reach the domain specified by the corresponding instance of fcipStaticRouteDID. The link identified by a value of this object is the same FCIP link as identified by the same value of fcipLinkIndex for the same FCIP entity.')
fcipStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fcipStaticRouteStatus.setStatus('current')
if mibBuilder.loadTexts: fcipStaticRouteStatus.setDescription('This object specifies the operational status of the row. When a management station sets the status to active(1), the values for the object fcipStaticRouteLinkIndex should be supplied as part of the set request. Setting the status to destroy(6) deletes the specified FCIP static route entry from the table.')
fcipDiscoveryDomainTable = MibTable((1, 3, 6, 1, 2, 1, 224, 1, 1, 9), )
if mibBuilder.loadTexts: fcipDiscoveryDomainTable.setStatus('current')
if mibBuilder.loadTexts: fcipDiscoveryDomainTable.setDescription('Information about FCIP Discovery Domains. Each FCIP Discovery Domain is associated with one or more FCIP entities.')
fcipDiscoveryDomainEntry = MibTableRow((1, 3, 6, 1, 2, 1, 224, 1, 1, 9, 1), ).setIndexNames((0, "FCIP-MGMT-MIB", "fcipEntityId"), (0, "FCIP-MGMT-MIB", "fcipDiscoveryDomainIndex"))
if mibBuilder.loadTexts: fcipDiscoveryDomainEntry.setStatus('current')
if mibBuilder.loadTexts: fcipDiscoveryDomainEntry.setDescription('A conceptual row of the FCIP Discovery Domain Table containing information about a particular FCIP Discovery Domain that is associated with one or more FCIP entities. The values of the read-write object fcipDiscoveryDomainName are persistent across system restarts.')
fcipDiscoveryDomainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: fcipDiscoveryDomainIndex.setStatus('current')
if mibBuilder.loadTexts: fcipDiscoveryDomainIndex.setDescription('An integer that uniquely identifies an FCIP Discovery Domain associated with this FCIP entity.')
fcipDiscoveryDomainName = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 9, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcipDiscoveryDomainName.setReference('RFC 3822, Section 4.1.1, FCIP Discovery Domains')
if mibBuilder.loadTexts: fcipDiscoveryDomainName.setStatus('current')
if mibBuilder.loadTexts: fcipDiscoveryDomainName.setDescription('The name of this FCIP Discovery Domain.')
fcipLinkErrorsTable = MibTable((1, 3, 6, 1, 2, 1, 224, 1, 1, 10), )
if mibBuilder.loadTexts: fcipLinkErrorsTable.setReference('RFC 3821, Section 5.2, FCIP Link')
if mibBuilder.loadTexts: fcipLinkErrorsTable.setStatus('current')
if mibBuilder.loadTexts: fcipLinkErrorsTable.setDescription('A list of error counters for FCIP Links. Each counter records the number of times a particular error happened that caused a TCP connection to close down.')
fcipLinkErrorsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1), ).setIndexNames((0, "FCIP-MGMT-MIB", "fcipEntityId"), (0, "FCIP-MGMT-MIB", "fcipLinkIndex"))
if mibBuilder.loadTexts: fcipLinkErrorsEntry.setStatus('current')
if mibBuilder.loadTexts: fcipLinkErrorsEntry.setDescription('A conceptual row of the FCIP Link Errors Table containing error counters for an FCIP Link.')
fcipLinkFcipLossofFcSynchs = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipLossofFcSynchs.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipLossofFcSynchs.setDescription('The number of times FC synchronization was lost on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipEncapErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipEncapErrors.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipEncapErrors.setDescription('The number of FCIP frames received with encapsulation errors such as improper header, format, or length. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipNotReceivedSfResps = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipNotReceivedSfResps.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipNotReceivedSfResps.setDescription('The number of times an FCIP Special Frame Response was expected but not received on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipSfRespMismatches = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipSfRespMismatches.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipSfRespMismatches.setDescription('The number of times FCIP Special Frame Bytes mismatch happened on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipSfInvalidNonces = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipSfInvalidNonces.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipSfInvalidNonces.setDescription('The number of times FCIP Special Frame Invalid Connection Nonce happened on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipReceivedSfDuplicates = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipReceivedSfDuplicates.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipReceivedSfDuplicates.setDescription('The number of times duplicate FCIP Special Frames were received on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipSfInvalidWWNs = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipSfInvalidWWNs.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipSfInvalidWWNs.setDescription('The number of times FCIP Special Frames with invalid destination FC Fabric Entity WWN were received on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipBB2LkaTimeOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipBB2LkaTimeOuts.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipBB2LkaTimeOuts.setDescription('The number of FC Keep Alive Time-outs that occurred on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkFcipSntpExpiredTimeStamps = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkFcipSntpExpiredTimeStamps.setStatus('current')
if mibBuilder.loadTexts: fcipLinkFcipSntpExpiredTimeStamps.setDescription('The number of frames discarded due to an expired Simple Network Time Protocol (SNTP) timestamp on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkTcpTooManyErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkTcpTooManyErrors.setStatus('current')
if mibBuilder.loadTexts: fcipLinkTcpTooManyErrors.setDescription('The number of TCP connections that closed down on this FCIP Link due to too many errors on the connection. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkTcpExcessiveDroppedDatagrams = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkTcpExcessiveDroppedDatagrams.setStatus('current')
if mibBuilder.loadTexts: fcipLinkTcpExcessiveDroppedDatagrams.setDescription('The number of TCP connections that closed down on this FCIP Link due to an excessive number of dropped FCIP packets. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipLinkTcpSaParamMismatches = MibTableColumn((1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcipLinkTcpSaParamMismatches.setReference('RFC 3821, Section 9.4.2, TCP Connection Security Associations (SAs)')
if mibBuilder.loadTexts: fcipLinkTcpSaParamMismatches.setStatus('current')
if mibBuilder.loadTexts: fcipLinkTcpSaParamMismatches.setDescription('The number of times TCP connections with Security Association parameter mismatches were closed down on this FCIP Link. The last discontinuity of this counter is indicated by fcipLinkCreateTime.')
fcipCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 224, 2, 1))
fcipGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 224, 2, 2))
fcipCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 224, 2, 1, 1)).setObjects(("FCIP-MGMT-MIB", "fcipEntityScalarGroup"), ("FCIP-MGMT-MIB", "fcipEntityInstanceGroup"), ("FCIP-MGMT-MIB", "fcipLinkGroup"), ("FCIP-MGMT-MIB", "fcipTcpConnGroup"), ("FCIP-MGMT-MIB", "fcipDiscoveryDomainGroup"), ("FCIP-MGMT-MIB", "fcipLinkErrorsGroup"), ("FCIP-MGMT-MIB", "fcipDynamicRouteGroup"), ("FCIP-MGMT-MIB", "fcipStaticRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipCompliance = fcipCompliance.setStatus('current')
if mibBuilder.loadTexts: fcipCompliance.setDescription('Compliance statement for FCIP MIB.')
fcipEntityScalarGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 1)).setObjects(("FCIP-MGMT-MIB", "fcipDynIpConfType"), ("FCIP-MGMT-MIB", "fcipDeviceWWN"), ("FCIP-MGMT-MIB", "fcipEntitySACKOption"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipEntityScalarGroup = fcipEntityScalarGroup.setStatus('current')
if mibBuilder.loadTexts: fcipEntityScalarGroup.setDescription('Collection of scalar objects applicable to all FCIP instances.')
fcipEntityInstanceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 2)).setObjects(("FCIP-MGMT-MIB", "fcipEntityName"), ("FCIP-MGMT-MIB", "fcipEntityAddressType"), ("FCIP-MGMT-MIB", "fcipEntityAddress"), ("FCIP-MGMT-MIB", "fcipEntityTcpConnPort"), ("FCIP-MGMT-MIB", "fcipEntitySeqNumWrap"), ("FCIP-MGMT-MIB", "fcipEntityPHBSupport"), ("FCIP-MGMT-MIB", "fcipEntityStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipEntityInstanceGroup = fcipEntityInstanceGroup.setStatus('current')
if mibBuilder.loadTexts: fcipEntityInstanceGroup.setDescription('A collection of objects providing information about FCIP instances.')
fcipLinkGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 3)).setObjects(("FCIP-MGMT-MIB", "fcipLinkIfIndex"), ("FCIP-MGMT-MIB", "fcipLinkCost"), ("FCIP-MGMT-MIB", "fcipLinkLocalFcipEntityMode"), ("FCIP-MGMT-MIB", "fcipLinkLocalFcipEntityAddressType"), ("FCIP-MGMT-MIB", "fcipLinkLocalFcipEntityAddress"), ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityWWN"), ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityId"), ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityAddressType"), ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityAddress"), ("FCIP-MGMT-MIB", "fcipLinkStatus"), ("FCIP-MGMT-MIB", "fcipLinkCreateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipLinkGroup = fcipLinkGroup.setStatus('current')
if mibBuilder.loadTexts: fcipLinkGroup.setDescription('A collection of objects providing information about FCIP Links.')
fcipTcpConnGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 4)).setObjects(("FCIP-MGMT-MIB", "fcipTcpConnRWSize"), ("FCIP-MGMT-MIB", "fcipTcpConnMSS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipTcpConnGroup = fcipTcpConnGroup.setStatus('current')
if mibBuilder.loadTexts: fcipTcpConnGroup.setDescription('A collection of objects providing information about FCIP TCP connections.')
fcipDiscoveryDomainGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 5)).setObjects(("FCIP-MGMT-MIB", "fcipDiscoveryDomainName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipDiscoveryDomainGroup = fcipDiscoveryDomainGroup.setStatus('current')
if mibBuilder.loadTexts: fcipDiscoveryDomainGroup.setDescription('A collection of objects providing information about FCIP Discovery Domains.')
fcipLinkErrorsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 6)).setObjects(("FCIP-MGMT-MIB", "fcipLinkFcipLossofFcSynchs"), ("FCIP-MGMT-MIB", "fcipLinkFcipEncapErrors"), ("FCIP-MGMT-MIB", "fcipLinkFcipNotReceivedSfResps"), ("FCIP-MGMT-MIB", "fcipLinkFcipSfRespMismatches"), ("FCIP-MGMT-MIB", "fcipLinkFcipSfInvalidNonces"), ("FCIP-MGMT-MIB", "fcipLinkFcipReceivedSfDuplicates"), ("FCIP-MGMT-MIB", "fcipLinkFcipSfInvalidWWNs"), ("FCIP-MGMT-MIB", "fcipLinkFcipBB2LkaTimeOuts"), ("FCIP-MGMT-MIB", "fcipLinkFcipSntpExpiredTimeStamps"), ("FCIP-MGMT-MIB", "fcipLinkTcpTooManyErrors"), ("FCIP-MGMT-MIB", "fcipLinkTcpExcessiveDroppedDatagrams"), ("FCIP-MGMT-MIB", "fcipLinkTcpSaParamMismatches"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipLinkErrorsGroup = fcipLinkErrorsGroup.setStatus('current')
if mibBuilder.loadTexts: fcipLinkErrorsGroup.setDescription('A collection of objects providing information about FCIP link errors.')
fcipDynamicRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 7)).setObjects(("FCIP-MGMT-MIB", "fcipDynamicRouteLinkIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipDynamicRouteGroup = fcipDynamicRouteGroup.setStatus('current')
if mibBuilder.loadTexts: fcipDynamicRouteGroup.setDescription('A collection of objects providing information about FCIP dynamic routes.')
fcipStaticRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 224, 2, 2, 8)).setObjects(("FCIP-MGMT-MIB", "fcipStaticRouteLinkIndex"), ("FCIP-MGMT-MIB", "fcipStaticRouteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcipStaticRouteGroup = fcipStaticRouteGroup.setStatus('current')
if mibBuilder.loadTexts: fcipStaticRouteGroup.setDescription('A collection of objects providing information about FCIP static routes.')
mibBuilder.exportSymbols("FCIP-MGMT-MIB", fcipConformance=fcipConformance, fcipLinkErrorsTable=fcipLinkErrorsTable, fcipLinkFcipNotReceivedSfResps=fcipLinkFcipNotReceivedSfResps, fcipTcpConnGroup=fcipTcpConnGroup, fcipLinkRemFcipEntityAddressType=fcipLinkRemFcipEntityAddressType, fcipEntityTcpConnPort=fcipEntityTcpConnPort, fcipLinkLocalFcipEntityAddressType=fcipLinkLocalFcipEntityAddressType, fcipEntityPHBSupport=fcipEntityPHBSupport, fcipLinkIndex=fcipLinkIndex, fcipLinkCreateTime=fcipLinkCreateTime, fcipCompliances=fcipCompliances, FcipEntityMode=FcipEntityMode, fcipLinkFcipReceivedSfDuplicates=fcipLinkFcipReceivedSfDuplicates, fcipTcpConnTable=fcipTcpConnTable, fcipDiscoveryDomainTable=fcipDiscoveryDomainTable, fcipLinkFcipSfInvalidNonces=fcipLinkFcipSfInvalidNonces, fcipStaticRouteGroup=fcipStaticRouteGroup, fcipGroups=fcipGroups, fcipDiscoveryDomainName=fcipDiscoveryDomainName, fcipDeviceWWN=fcipDeviceWWN, fcipLinkErrorsEntry=fcipLinkErrorsEntry, fcipLinkRemFcipEntityId=fcipLinkRemFcipEntityId, fcipLinkRemFcipEntityAddress=fcipLinkRemFcipEntityAddress, fcipLinkFcipSfInvalidWWNs=fcipLinkFcipSfInvalidWWNs, fcipLinkLocalFcipEntityMode=fcipLinkLocalFcipEntityMode, fcipStaticRouteDID=fcipStaticRouteDID, fcipLinkFcipEncapErrors=fcipLinkFcipEncapErrors, fcipStaticRouteEntry=fcipStaticRouteEntry, fcipTcpConnRemPort=fcipTcpConnRemPort, fcipDynamicRouteDID=fcipDynamicRouteDID, fcipDiscoveryDomainGroup=fcipDiscoveryDomainGroup, fcipEntityInstanceGroup=fcipEntityInstanceGroup, fcipEntitySeqNumWrap=fcipEntitySeqNumWrap, fcipLinkFcipBB2LkaTimeOuts=fcipLinkFcipBB2LkaTimeOuts, fcipDynamicRouteEntry=fcipDynamicRouteEntry, fcipMIB=fcipMIB, fcipDynIpConfType=fcipDynIpConfType, fcipLinkStatus=fcipLinkStatus, fcipEntityInstanceEntry=fcipEntityInstanceEntry, PYSNMP_MODULE_ID=fcipMIB, fcipEntityAddressType=fcipEntityAddressType, fcipEntityInstanceTable=fcipEntityInstanceTable, fcipLinkEntry=fcipLinkEntry, fcipStaticRouteLinkIndex=fcipStaticRouteLinkIndex, fcipLinkFcipSntpExpiredTimeStamps=fcipLinkFcipSntpExpiredTimeStamps, fcipLinkTcpSaParamMismatches=fcipLinkTcpSaParamMismatches, fcipEntityName=fcipEntityName, fcipLinkGroup=fcipLinkGroup, fcipDynamicRouteGroup=fcipDynamicRouteGroup, fcipStaticRouteStatus=fcipStaticRouteStatus, fcipLinkRemFcipEntityWWN=fcipLinkRemFcipEntityWWN, fcipStaticRouteTable=fcipStaticRouteTable, fcipConfig=fcipConfig, fcipObjects=fcipObjects, fcipEntityScalarGroup=fcipEntityScalarGroup, fcipDiscoveryDomainEntry=fcipDiscoveryDomainEntry, fcipLinkFcipSfRespMismatches=fcipLinkFcipSfRespMismatches, fcipLinkLocalFcipEntityAddress=fcipLinkLocalFcipEntityAddress, fcipEntitySACKOption=fcipEntitySACKOption, fcipLinkIfIndex=fcipLinkIfIndex, fcipLinkCost=fcipLinkCost, fcipEntityStatus=fcipEntityStatus, fcipEntityAddress=fcipEntityAddress, fcipLinkTcpExcessiveDroppedDatagrams=fcipLinkTcpExcessiveDroppedDatagrams, fcipDynamicRouteLinkIndex=fcipDynamicRouteLinkIndex, fcipLinkErrorsGroup=fcipLinkErrorsGroup, fcipLinkTable=fcipLinkTable, fcipDiscoveryDomainIndex=fcipDiscoveryDomainIndex, fcipLinkTcpTooManyErrors=fcipLinkTcpTooManyErrors, fcipTcpConnLocalPort=fcipTcpConnLocalPort, fcipTcpConnEntry=fcipTcpConnEntry, fcipTcpConnRWSize=fcipTcpConnRWSize, fcipTcpConnMSS=fcipTcpConnMSS, fcipDynamicRouteTable=fcipDynamicRouteTable, fcipLinkFcipLossofFcSynchs=fcipLinkFcipLossofFcSynchs, fcipCompliance=fcipCompliance, fcipEntityId=fcipEntityId, FcipEntityId=FcipEntityId, FcipDomainIdInOctetForm=FcipDomainIdInOctetForm)
