#
# PySNMP MIB module XYPLEX-IEEE-HUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYPLEX-IEEE-HUB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:46:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, ObjectIdentity, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Bits, Counter64, Unsigned32, TimeTicks, ModuleIdentity, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "ObjectIdentity", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Bits", "Counter64", "Unsigned32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
ieeeHub = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001))
hmBasicCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1))
hmSelfTestCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 2))
hmPerfMonCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 3))
hmAddrTrackCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 4))
hmBadBitClockCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 5))
hmBasicHubTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1))
hmBasicHubEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1))
hubID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubID.setStatus('mandatory')
if mibBuilder.loadTexts: hubID.setDescription("The hub's Ethernet address.")
hubGroupCapacity = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubGroupCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: hubGroupCapacity.setDescription('The maximum number of groups the hub can have; a constant 1.')
hubGroupMap = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubGroupMap.setStatus('mandatory')
if mibBuilder.loadTexts: hubGroupMap.setDescription('A bit map of defined groups.')
hmBasicGroupTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2))
hmBasicGroupEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1))
groupHubID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupHubID.setStatus('mandatory')
if mibBuilder.loadTexts: groupHubID.setDescription("The hub's Ethernet address.")
groupID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupID.setStatus('mandatory')
if mibBuilder.loadTexts: groupID.setDescription("The identification number of the hub's only group; a constant 1.")
groupNumberOfPorts = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupNumberOfPorts.setStatus('mandatory')
if mibBuilder.loadTexts: groupNumberOfPorts.setDescription('The number of physical Ethernet ports on the hub.')
hmBasicPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3), )
if mibBuilder.loadTexts: hmBasicPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: hmBasicPortTable.setDescription('A list of basic hub Ethernet port entries.')
hmBasicPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1), ).setIndexNames((0, "XYPLEX-IEEE-HUB-MIB", "portHubBasicID"))
if mibBuilder.loadTexts: hmBasicPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hmBasicPortEntry.setDescription('Parameter values for a port.')
portHubBasicID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubBasicID.setStatus('mandatory')
if mibBuilder.loadTexts: portHubBasicID.setDescription("The hub's Ethernet address.")
portGroupBasicID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupBasicID.setStatus('mandatory')
if mibBuilder.loadTexts: portGroupBasicID.setDescription('Group number; a constant 1.')
portBasicID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portBasicID.setStatus('mandatory')
if mibBuilder.loadTexts: portBasicID.setDescription('A unique value for each Ethernet port. Its value ranges between 1 and the value of groupNumberOfPorts. The value for each port must remain constant at least from one re-initialization of the network management agent to the next.')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("repeater", 2), ("tenBASE-FAsync", 3), ("tenBASE-FSynch", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portType.setStatus('mandatory')
if mibBuilder.loadTexts: portType.setDescription('The port type, with the following meanings: other not listed here repeater 802.3 sec. 9 rptr port tenBASE-FAsync(3) async port on 10BASE-FA tenBASE-FSynch(4) sync port on 10BASE-FA ')
portAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: portAdminState.setDescription("Control over the port's ability to transmit and receive. Corresponds directly to PORT ENABLED/DISABLED and the value labeled 'State:' in the PORT display.")
portAutoPartitionState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("notAutoPartitioned", 2), ("autoPartitioned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAutoPartitionState.setStatus('mandatory')
if mibBuilder.loadTexts: portAutoPartitionState.setDescription("The port's status with regard to automatic partitioning. Corresponds directly to the value labeled 'Auto Partitioned:' in the PORT display.")
hmSelfTestHubTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1))
hmSelfTestHubEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1))
hubSelfTestID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubSelfTestID.setStatus('mandatory')
if mibBuilder.loadTexts: hubSelfTestID.setDescription("The hub's Ethernet address.")
hubResetTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubResetTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: hubResetTimeStamp.setDescription('The value of sysUpTime when the hub was last reset.')
hubHealthState = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubHealthState.setStatus('mandatory')
if mibBuilder.loadTexts: hubHealthState.setDescription('Indication of hub operational failure.')
hubHealthText = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubHealthText.setStatus('mandatory')
if mibBuilder.loadTexts: hubHealthText.setDescription('Free form text description of hub operational state.')
hubHealthData = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hubHealthData.setStatus('mandatory')
if mibBuilder.loadTexts: hubHealthData.setDescription('Free form binary data description of hub operational state.')
hubSystemResetting = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notResetting", 1), ("resetting", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hubSystemResetting.setStatus('mandatory')
if mibBuilder.loadTexts: hubSystemResetting.setDescription('Control to cause initialization of hub, reset of management counters, ad reset of hub parameters to defaults.')
hubResetting = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notResetting", 1), ("resetting", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hubResetting.setStatus('mandatory')
if mibBuilder.loadTexts: hubResetting.setDescription('Control to cause initialization of the relay and port counters and flags related to the auto-partition function. This does not affect hub management counters.')
hubExecutingSelfTest = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSelfTesting", 1), ("selfTesting", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hubExecutingSelfTest.setStatus('mandatory')
if mibBuilder.loadTexts: hubExecutingSelfTest.setDescription('Control to cause execution of a non-disruptive self test.')
hmPerfMonRelayTable = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1))
hmPerfMonRelayEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1))
relayHubPerfID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: relayHubPerfID.setStatus('mandatory')
if mibBuilder.loadTexts: relayHubPerfID.setDescription("The hub's Ethernet address.")
relayPerfID = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: relayPerfID.setStatus('mandatory')
if mibBuilder.loadTexts: relayPerfID.setDescription('Relay identification; a constant 1.')
relayTotalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 33, 10001, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relayTotalCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: relayTotalCollisions.setDescription('The number of times the hub transmitted and simultaneously detected external activity on one or more ports.')
hmPerfMonPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2), )
if mibBuilder.loadTexts: hmPerfMonPortTable.setStatus('mandatory')
hmPerfMonPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1), )
if mibBuilder.loadTexts: hmPerfMonPortEntry.setStatus('mandatory')
portHubPerfID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubPerfID.setStatus('mandatory')
if mibBuilder.loadTexts: portHubPerfID.setDescription("The hub's Ethernet address.")
portGroupPerfID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupPerfID.setStatus('mandatory')
if mibBuilder.loadTexts: portGroupPerfID.setDescription('The group number; a constant 1.')
portPerfID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPerfID.setStatus('mandatory')
if mibBuilder.loadTexts: portPerfID.setDescription('A unique value for each Ethernet port, identifying the same port as the equivalent value of portBasicID.')
portReadableFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portReadableFrames.setStatus('mandatory')
if mibBuilder.loadTexts: portReadableFrames.setDescription("Number of frames received with legal length and no corruption in transmission. Corresponds directly with the value labeled 'Received Frames:' in the PORT display.")
portReadableOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portReadableOctets.setStatus('mandatory')
if mibBuilder.loadTexts: portReadableOctets.setDescription('The number of data and padding bytes represented by portReadableFrames.')
portPygmys = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPygmys.setStatus('mandatory')
if mibBuilder.loadTexts: portPygmys.setDescription("Number of message fragments less than 64 +/- 10 bits long, possibly indicating external noise problems. Corresponds directly with the value labeled 'Fragments (Pygmy):' in the PORT display.")
portRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRunts.setStatus('mandatory')
if mibBuilder.loadTexts: portRunts.setDescription("Number of collision fragments longer than a pygmy but shorter than a legal message. These occur as a result of normal collision operation. Corresponds directly with the value labeled 'Short Frames (Runt):' in the PORT display.")
portFrameCheckSeqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFrameCheckSeqErrs.setStatus('mandatory')
if mibBuilder.loadTexts: portFrameCheckSeqErrs.setDescription("Number of frames received with integral bytes but invalid FCS. Corresponds directly with the value labeled 'Check Sequenct (CRC):' in the PORT display.")
portAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAlignmentErrors.setStatus('mandatory')
if mibBuilder.loadTexts: portAlignmentErrors.setDescription('Number of frames received with an incomplete bytes.')
portFramesTooLong = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFramesTooLong.setStatus('mandatory')
if mibBuilder.loadTexts: portFramesTooLong.setDescription("Number of frames received of length greater than 1518 bytes. Corresponds directly with the value labeled 'Long Frames (>1518):' in the PORT display.")
portAutoPartitionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAutoPartitionCount.setStatus('mandatory')
if mibBuilder.loadTexts: portAutoPartitionCount.setDescription("Number of times the repeater has automatically partitioned the port. Corresponds directly with the value labeled 'Auto Partitions:' in the PORT display.")
hmAddrTrackPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1), )
if mibBuilder.loadTexts: hmAddrTrackPortTable.setStatus('mandatory')
hmAddrTrackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1), )
if mibBuilder.loadTexts: hmAddrTrackPortEntry.setStatus('mandatory')
portHubAddrID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubAddrID.setStatus('mandatory')
if mibBuilder.loadTexts: portHubAddrID.setDescription("The hub's Ethernet address.")
portGroupAddrID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupAddrID.setStatus('mandatory')
if mibBuilder.loadTexts: portGroupAddrID.setDescription('The group number; a constant 1.')
portAddrID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAddrID.setStatus('mandatory')
if mibBuilder.loadTexts: portAddrID.setDescription('A unique value for each Ethernet port, identifying the same port as the equivalent value of portBasicID.')
portLastSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portLastSourceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: portLastSourceAddress.setDescription("Source address of the last readable frame received on the port. Corresponds directly with the value labeled 'Last Address:' in the PORT display.")
portSourceAddrChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSourceAddrChanges.setStatus('mandatory')
if mibBuilder.loadTexts: portSourceAddrChanges.setDescription("Number of times portLastSourceAddress has changed. Corresponds directly with the value labeled 'Address Changes:' in the PORT display.")
hmBadBitClockPortTable = MibTable((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1), )
if mibBuilder.loadTexts: hmBadBitClockPortTable.setStatus('mandatory')
hmBadBitClockPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1), )
if mibBuilder.loadTexts: hmBadBitClockPortEntry.setStatus('mandatory')
portHubClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portHubClockID.setStatus('mandatory')
if mibBuilder.loadTexts: portHubClockID.setDescription("The hub's Ethernet address.")
portGroupClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupClockID.setStatus('mandatory')
if mibBuilder.loadTexts: portGroupClockID.setDescription('The group number; a constant 1.')
portClockID = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portClockID.setStatus('mandatory')
if mibBuilder.loadTexts: portClockID.setDescription('A unique value for each Ethernet port, identifying the same port as the equivalent value of portBasicID.')
portOutOfSpecBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 10001, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOutOfSpecBitRate.setStatus('mandatory')
if mibBuilder.loadTexts: portOutOfSpecBitRate.setDescription("Number of received frames with the transmission frequency detectably out of specification. Corresponds directly with the value labeled 'Out of Spec. Bit Rate:' in the PORT display.")
mibBuilder.exportSymbols("XYPLEX-IEEE-HUB-MIB", hmPerfMonPortEntry=hmPerfMonPortEntry, hubID=hubID, portHubClockID=portHubClockID, hmBasicCapability=hmBasicCapability, portPygmys=portPygmys, groupNumberOfPorts=groupNumberOfPorts, hubGroupCapacity=hubGroupCapacity, hubGroupMap=hubGroupMap, hubSelfTestID=hubSelfTestID, hubHealthState=hubHealthState, portOutOfSpecBitRate=portOutOfSpecBitRate, hmPerfMonCapability=hmPerfMonCapability, hmBadBitClockPortTable=hmBadBitClockPortTable, portRunts=portRunts, hmSelfTestCapability=hmSelfTestCapability, portHubAddrID=portHubAddrID, hmBasicHubEntry=hmBasicHubEntry, portAutoPartitionCount=portAutoPartitionCount, hubResetting=hubResetting, portAlignmentErrors=portAlignmentErrors, hmBasicGroupTable=hmBasicGroupTable, groupHubID=groupHubID, hubHealthData=hubHealthData, hmBasicHubTable=hmBasicHubTable, portAutoPartitionState=portAutoPartitionState, hmSelfTestHubEntry=hmSelfTestHubEntry, xyplex=xyplex, portClockID=portClockID, portFrameCheckSeqErrs=portFrameCheckSeqErrs, hmBadBitClockPortEntry=hmBadBitClockPortEntry, portSourceAddrChanges=portSourceAddrChanges, relayTotalCollisions=relayTotalCollisions, hmBadBitClockCapability=hmBadBitClockCapability, hmPerfMonPortTable=hmPerfMonPortTable, hubSystemResetting=hubSystemResetting, hmAddrTrackPortTable=hmAddrTrackPortTable, hmAddrTrackPortEntry=hmAddrTrackPortEntry, portAddrID=portAddrID, relayHubPerfID=relayHubPerfID, portGroupBasicID=portGroupBasicID, portFramesTooLong=portFramesTooLong, hmBasicGroupEntry=hmBasicGroupEntry, hmSelfTestHubTable=hmSelfTestHubTable, hmPerfMonRelayEntry=hmPerfMonRelayEntry, portReadableOctets=portReadableOctets, hmAddrTrackCapability=hmAddrTrackCapability, hubExecutingSelfTest=hubExecutingSelfTest, portGroupPerfID=portGroupPerfID, hmPerfMonRelayTable=hmPerfMonRelayTable, portAdminState=portAdminState, hubHealthText=hubHealthText, portBasicID=portBasicID, portGroupAddrID=portGroupAddrID, portReadableFrames=portReadableFrames, hmBasicPortEntry=hmBasicPortEntry, portLastSourceAddress=portLastSourceAddress, portPerfID=portPerfID, groupID=groupID, portHubPerfID=portHubPerfID, portType=portType, hmBasicPortTable=hmBasicPortTable, portHubBasicID=portHubBasicID, relayPerfID=relayPerfID, ieeeHub=ieeeHub, portGroupClockID=portGroupClockID, hubResetTimeStamp=hubResetTimeStamp)
