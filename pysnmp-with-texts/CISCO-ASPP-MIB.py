#
# PySNMP MIB module CISCO-ASPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ASPP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, IpAddress, ModuleIdentity, NotificationType, Counter32, Counter64, iso, Integer32, Unsigned32, Bits, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "IpAddress", "ModuleIdentity", "NotificationType", "Counter32", "Counter64", "iso", "Integer32", "Unsigned32", "Bits", "MibIdentifier", "ObjectIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoAsppMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 55))
ciscoAsppMIB.setRevisions(('2003-02-10 00:00', '1995-08-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAsppMIB.setRevisionsDescriptions(('Added Asynchronous Point of Sale(POS) to IP conversion support. The APOS protocol utilizes asynchrounous communications with 1 start, 1 stop and 7 data bits with even parity. The connection to the POS terminal will always be an asynchronous leased line. The protocol has many characteristics of BSC except it is simplified to minimize overhead on the point to point connection. The added APOS traffic will be locally acknowledged unlike the other polled asynchronous protocol which function in passthrough mode. The LRC/VRC will be verified and any necessary recovery will be done by the router. This is necessary since we are converting the protocol so the data can be passed to an IP attached host.', 'Initial mib for async security polled protocols.',))
if mibBuilder.loadTexts: ciscoAsppMIB.setLastUpdated('200302100000Z')
if mibBuilder.loadTexts: ciscoAsppMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAsppMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-poll-async@cisco.com')
if mibBuilder.loadTexts: ciscoAsppMIB.setDescription("The ASPP MIB provides the configuration and operational information on asynchronous polled protocols such as the asynchronous security protocols that alarm monitoring companies use. The protocols are handled in passthrough mode. ASPP will handle the receiving and sending of the asychronous blocks. It will not perform any error checking. It is the responsibilty of the end-station to perform any required error recovery. A generic protocol has been created to support asychronous protocols. In some situations this doesn't work for all types since there is no alarm protocol standard. Specific vendor support has been included for the following vendor's alarm equipment and protocols: * adplex * adt - PollSelect - VariPoll * diebold * mdi * mosec (mosler) * gddb (Guang Dong Development Bank) - This protocol is similar to Burroughs Poll/Select The following example configuration shows how the ASPP MIB returns ASPP information, from either CISCO A or CISCO B. Security == ASP == Cisco == IP == Cisco == ASP == Alarm control A Network B Panel station The following entities are managed: 1) ASPP ports (serial interfaces) The ASPP ports are identified by the interface index, and additional information about this interface can be obtained from the Cisco Serial Interface MIB.")
asppObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 55, 1))
asppPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1))
asppPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1), )
if mibBuilder.loadTexts: asppPortTable.setStatus('current')
if mibBuilder.loadTexts: asppPortTable.setDescription('A list of asynchronous interfaces which have been configured to support an asynchronous security protocol (ASP) BSTUN group.')
asppPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: asppPortEntry.setStatus('current')
if mibBuilder.loadTexts: asppPortEntry.setDescription('Current ASP configuration settings for an asynchronous port.')
asppPortProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("adplex", 1), ("adtPollSelect", 2), ("adtVariPoll", 3), ("diebold", 4), ("asyncGeneric", 5), ("mdi", 6), ("mosec", 7), ("gddb", 8), ("apos", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortProtocol.setStatus('current')
if mibBuilder.loadTexts: asppPortProtocol.setDescription("Specifies type of asynchronous security protocol being used. These protocols are implemented by individual security alarm manufacturers. There is no standard protocol for alarm communications over RS-232 interfaces. asyncGeneric(5)- provides generic polled asynchronous support Specific vendor support has been included for the following vendor's alarm equipment and protocols: * adplex(1) * ADT - adtPollSelect(2) - adtVariPoll(3) * diebold(4) * mdi(6) * mosec(7) - mosler equipment * gddb(8) - Guang Dong Development Bank The protocol is similar to Burroughs Poll/Select. apos(9) - Protocol support for asynchronous POS devices for provide credit and debit card authorizations to an IP attached host.")
asppPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortRole.setStatus('current')
if mibBuilder.loadTexts: asppPortRole.setDescription("Specifies the router's protocol role. primary(1) - Indicates we are attaching to the terminal or alarm panel. secondary(2) - Indicates we are attaching to the host or alarm console..")
asppPortReceiveInterFrameTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortReceiveInterFrameTimeout.setStatus('current')
if mibBuilder.loadTexts: asppPortReceiveInterFrameTimeout.setDescription('Specifies the receive inter-frame-timeout period, used to delimit frames. Since all the protocols are implemented over RS-232 3-wire circuits (ie TX, RX and GND), the only general method for start-end frame detection is to monitor the time between received characters. If this time period exceeds the inter-frame timeout value, then frame end-start is detected.')
asppPortDeviceAddressOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortDeviceAddressOffset.setReference('CISCO-BSTUN-MIB')
if mibBuilder.loadTexts: asppPortDeviceAddressOffset.setStatus('current')
if mibBuilder.loadTexts: asppPortDeviceAddressOffset.setDescription('Specifies the byte offset within a frame, which contains the device address. This is used when the asynchronous interface is configured to use the async generic protocol handler. Because no knowledge of the protocol is built-in to the IOS, it must be told where the address field lives within the frame. That way IOS can correctly route the frames for this protocol.')
asppPortEOFCharacter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortEOFCharacter.setStatus('current')
if mibBuilder.loadTexts: asppPortEOFCharacter.setDescription('Specifies the protocol character to use to delimit the end of a frame. The valid character is 0-255 and 256 indicates the object is not configured.')
asppPortSOFCharacter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortSOFCharacter.setStatus('current')
if mibBuilder.loadTexts: asppPortSOFCharacter.setDescription('Specifies the protocol character to use to delimit the beginning of a frame. The valid character is 0-255 and 256 indicates the object is not configured.')
asppPortIgnoreSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortIgnoreSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: asppPortIgnoreSequenceNumber.setDescription("Specifies whether the asp sequence numbers used to synchronize aspp traffic between head-end and tail-end routers should be ignored. This is enabled if there isn't a one to one correlation between commands and responses between the two routers.")
asppPortRspTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortRspTimer.setStatus('current')
if mibBuilder.loadTexts: asppPortRspTimer.setDescription('Specifies the amount of time the router will wait for a response to a packet before retransmission.')
asppPortRxTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortRxTimer.setStatus('current')
if mibBuilder.loadTexts: asppPortRxTimer.setDescription('Specifies the maximum amount of time the router will wait for a complete packet to be received. It starts when an STX character is received.')
asppPortHostTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 120))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortHostTimer.setStatus('current')
if mibBuilder.loadTexts: asppPortHostTimer.setDescription('Specifies the maximum amount of time the router will wait for a response to a terminal request from the host. It starts when a terminal request is forwarded to the host.')
asppPortConnectTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortConnectTimer.setStatus('current')
if mibBuilder.loadTexts: asppPortConnectTimer.setDescription('Specifies the maximum amount of time the router will wait for the activation of the tunnel connection to the host to complete. It starts when a terminal requests a session with host.')
asppPortRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortRetryCount.setStatus('current')
if mibBuilder.loadTexts: asppPortRetryCount.setDescription('Specifies the maximum number of timers a packet will be retransmitted before the connection with the terminal will be disconnected.')
asppPortDelayEnq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortDelayEnq.setStatus('current')
if mibBuilder.loadTexts: asppPortDelayEnq.setDescription('Specifies the amount of time to wait after sending a connect packet to the the terminal before sending the ENQ to initiate a session')
asppPortDisableEnq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortDisableEnq.setStatus('current')
if mibBuilder.loadTexts: asppPortDisableEnq.setDescription('Specifies whether sending of ENQ to initiate a session with the terminal is disabled.')
asppPortSendAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortSendAck.setStatus('current')
if mibBuilder.loadTexts: asppPortSendAck.setDescription('Specifies whether the router will send an ACK to acknowledge packets.')
asppPortDirect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortDirect.setStatus('current')
if mibBuilder.loadTexts: asppPortDirect.setDescription('Specifies whether the line mode is direct or dialed. If in direct the router will immediately send ENQ without waiting for AT commands')
asppPortDCDAlways = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: asppPortDCDAlways.setStatus('current')
if mibBuilder.loadTexts: asppPortDCDAlways.setDescription('Specifies whether DCD should always be asserted or asserted only when the connection is active.')
asppMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 55, 3))
asppMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 1))
asppMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2))
asppMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 1, 1)).setObjects(("CISCO-ASPP-MIB", "asppPortsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asppMibCompliance = asppMibCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: asppMibCompliance.setDescription('The compliance statement for ASP.')
asppMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 1, 2)).setObjects(("CISCO-ASPP-MIB", "asppPortsGroup"), ("CISCO-ASPP-MIB", "asppPortsGenericGroup"), ("CISCO-ASPP-MIB", "asppPortsAposGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asppMibComplianceRev1 = asppMibComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: asppMibComplianceRev1.setDescription('The compliance statement for ASP.')
asppPortsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2, 1)).setObjects(("CISCO-ASPP-MIB", "asppPortProtocol"), ("CISCO-ASPP-MIB", "asppPortRole"), ("CISCO-ASPP-MIB", "asppPortReceiveInterFrameTimeout"), ("CISCO-ASPP-MIB", "asppPortDeviceAddressOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asppPortsGroup = asppPortsGroup.setStatus('current')
if mibBuilder.loadTexts: asppPortsGroup.setDescription('A collection of objects providing information about interfaces that run asynchronous security protocols.')
asppPortsGenericGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2, 2)).setObjects(("CISCO-ASPP-MIB", "asppPortEOFCharacter"), ("CISCO-ASPP-MIB", "asppPortSOFCharacter"), ("CISCO-ASPP-MIB", "asppPortIgnoreSequenceNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asppPortsGenericGroup = asppPortsGenericGroup.setStatus('current')
if mibBuilder.loadTexts: asppPortsGenericGroup.setDescription('A collection of objects providing information about interfaces that run asynchronous generic protocols.')
asppPortsAposGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2, 3)).setObjects(("CISCO-ASPP-MIB", "asppPortRspTimer"), ("CISCO-ASPP-MIB", "asppPortRxTimer"), ("CISCO-ASPP-MIB", "asppPortHostTimer"), ("CISCO-ASPP-MIB", "asppPortConnectTimer"), ("CISCO-ASPP-MIB", "asppPortRetryCount"), ("CISCO-ASPP-MIB", "asppPortDelayEnq"), ("CISCO-ASPP-MIB", "asppPortDisableEnq"), ("CISCO-ASPP-MIB", "asppPortSendAck"), ("CISCO-ASPP-MIB", "asppPortDirect"), ("CISCO-ASPP-MIB", "asppPortDCDAlways"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asppPortsAposGroup = asppPortsAposGroup.setStatus('current')
if mibBuilder.loadTexts: asppPortsAposGroup.setDescription('A collection of objects providing information about interfaces that run asynchronous protocol to communicate to Point of Sale protocols.')
mibBuilder.exportSymbols("CISCO-ASPP-MIB", asppPortDelayEnq=asppPortDelayEnq, asppPortDCDAlways=asppPortDCDAlways, ciscoAsppMIB=ciscoAsppMIB, asppPortHostTimer=asppPortHostTimer, asppMibGroups=asppMibGroups, asppPortRxTimer=asppPortRxTimer, asppPortRspTimer=asppPortRspTimer, asppMibConformance=asppMibConformance, asppPortIgnoreSequenceNumber=asppPortIgnoreSequenceNumber, asppMibCompliances=asppMibCompliances, asppPortDeviceAddressOffset=asppPortDeviceAddressOffset, asppPortDirect=asppPortDirect, asppPortEOFCharacter=asppPortEOFCharacter, asppObjects=asppObjects, asppPortEntry=asppPortEntry, asppPortsAposGroup=asppPortsAposGroup, asppPortConnectTimer=asppPortConnectTimer, asppPortSendAck=asppPortSendAck, asppPortsGenericGroup=asppPortsGenericGroup, asppPortRetryCount=asppPortRetryCount, asppPortTable=asppPortTable, asppMibCompliance=asppMibCompliance, asppPortDisableEnq=asppPortDisableEnq, asppPortsGroup=asppPortsGroup, asppPortRole=asppPortRole, asppPortProtocol=asppPortProtocol, asppPorts=asppPorts, asppPortSOFCharacter=asppPortSOFCharacter, PYSNMP_MODULE_ID=ciscoAsppMIB, asppPortReceiveInterFrameTimeout=asppPortReceiveInterFrameTimeout, asppMibComplianceRev1=asppMibComplianceRev1)
