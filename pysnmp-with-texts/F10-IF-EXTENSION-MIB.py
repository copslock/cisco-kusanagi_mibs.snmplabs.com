#
# PySNMP MIB module F10-IF-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/F10-IF-EXTENSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
f10Mgmt, = mibBuilder.importSymbols("FORCE10-SMI", "f10Mgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Unsigned32, Integer32, Counter64, Bits, Gauge32, iso, TimeTicks, Counter32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Unsigned32", "Integer32", "Counter64", "Bits", "Gauge32", "iso", "TimeTicks", "Counter32", "MibIdentifier", "NotificationType")
TimeStamp, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "TextualConvention", "DisplayString")
f10IfExtensionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 11))
f10IfExtensionMib.setRevisions(('2014-08-12 12:00', '2012-03-06 12:00', '2010-08-11 12:00', '2010-08-10 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f10IfExtensionMib.setRevisionsDescriptions(('Added f10IfPortListBitPos.Removed f10IfDhcpAdminStatus and f10IfDhcpOperStatus.', 'Added DHCP Client attributes.', 'Add f10IfOutThrottles.', 'Initial version of this mib module.',))
if mibBuilder.loadTexts: f10IfExtensionMib.setLastUpdated('201203061200Z')
if mibBuilder.loadTexts: f10IfExtensionMib.setOrganization('Dell Inc')
if mibBuilder.loadTexts: f10IfExtensionMib.setContactInfo('http://www.force10networks.com/support')
if mibBuilder.loadTexts: f10IfExtensionMib.setDescription('Dell Networking OS IF Extenstion MIB. ')
f10IfExtensionMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1))
f10IfExtensionParams = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1))
f10IfExtensionStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2))
f10IfTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1), )
if mibBuilder.loadTexts: f10IfTable.setStatus('current')
if mibBuilder.loadTexts: f10IfTable.setDescription('Dell Networking OS Extension ifTable contains generic interface parameters.')
f10IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: f10IfEntry.setStatus('current')
if mibBuilder.loadTexts: f10IfEntry.setDescription(' A row defintion of Dell Networking OS Interface Extension parameters.')
f10IfIpMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(594, 9252))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfIpMtu.setStatus('current')
if mibBuilder.loadTexts: f10IfIpMtu.setDescription('The IP (Internet Protocol), Maximum Transmission Unit value.')
f10IfDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfDuplexMode.setStatus('current')
if mibBuilder.loadTexts: f10IfDuplexMode.setDescription('Duplex mode of the interface. This will be read-write only for s60')
f10IfQueueingStrategy = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfQueueingStrategy.setStatus('current')
if mibBuilder.loadTexts: f10IfQueueingStrategy.setDescription('Queueing strategy used for packets.')
f10IfRxFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfRxFlowCtrl.setStatus('current')
if mibBuilder.loadTexts: f10IfRxFlowCtrl.setDescription('Flow control receive. This will be read-write only for s60')
f10IfTxFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfTxFlowCtrl.setStatus('current')
if mibBuilder.loadTexts: f10IfTxFlowCtrl.setDescription('Flow Control transmit.This will be read-only only for s60')
f10IfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 241))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfDescr.setStatus('current')
if mibBuilder.loadTexts: f10IfDescr.setDescription('A textual string containing information about the interface. This will be read-write only for s60')
f10IfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfAdminStatus.setStatus('current')
if mibBuilder.loadTexts: f10IfAdminStatus.setDescription('A admin status of any interface. This will be read-write only for s60')
f10IfRateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 299))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfRateInterval.setStatus('current')
if mibBuilder.loadTexts: f10IfRateInterval.setDescription('The rate info interval for the interface. This will be read-write only for s60')
f10IfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 10, 100, 1000))).clone(namedValues=NamedValues(("auto", 1), ("tenMbps", 10), ("hundredMbps", 100), ("thousandMbps", 1000)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f10IfSpeed.setStatus('current')
if mibBuilder.loadTexts: f10IfSpeed.setDescription("The interface's current bandwidth in bits per second. This will be read-write only for s60")
f10IfPortListBitPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfPortListBitPos.setStatus('current')
if mibBuilder.loadTexts: f10IfPortListBitPos.setDescription('This is used for identifying the bit position in PortList Object for a given interface.')
f10IfStaticsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1), )
if mibBuilder.loadTexts: f10IfStaticsTable.setStatus('current')
if mibBuilder.loadTexts: f10IfStaticsTable.setDescription('The statistcs information of the interfaces for performance monitoring.')
f10IfStaticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: f10IfStaticsEntry.setStatus('current')
if mibBuilder.loadTexts: f10IfStaticsEntry.setDescription('A row defintion of Dell Networking OS Extension interface statistics.')
f10IfInVlanPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInVlanPkts.setStatus('current')
if mibBuilder.loadTexts: f10IfInVlanPkts.setDescription('The total number of valid VLAN Tagged frames received.')
f10IfIn64BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfIn64BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfIn64BytePkts.setDescription('The total number of frames (including bad frames) received that were 64 octets in length (excluding framing bits but in-cluding FCS octets).')
f10ifIn65To127BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10ifIn65To127BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10ifIn65To127BytePkts.setDescription('The total number of frames (including bad frames) received that were between 65 and 127 octets in length inclusive (ex-cluding framing bits but including FCS octets).')
f10IfIn128To255BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfIn128To255BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfIn128To255BytePkts.setDescription('The total number of frames (including bad frames) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets).')
f10IfIn256To511BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfIn256To511BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfIn256To511BytePkts.setDescription('The total number of frames (including bad frames) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets).')
f10IfIn512To1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfIn512To1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfIn512To1023BytePkts.setDescription('The total number of frames (including bad frames) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets).')
f10IfInOver1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInOver1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfInOver1023BytePkts.setDescription('The total number of frames received that were longer than 1023 (1025 Bytes in case of VLAN Tag) octets (excluding framing bits, but including FCS octets) and were otherwise well formed. This counter is not incremented for too long frames.')
f10IfInThrottles = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInThrottles.setStatus('current')
if mibBuilder.loadTexts: f10IfInThrottles.setDescription('This counter is incremented when a valid frame with a length or type field value equal to 0x8808 (Control Frame) is re-ceived.')
f10IfInRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInRunts.setStatus('current')
if mibBuilder.loadTexts: f10IfInRunts.setDescription('The total number of frames received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed.')
f10IfInGiants = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInGiants.setStatus('current')
if mibBuilder.loadTexts: f10IfInGiants.setDescription('The total number of frames received that were longer than 1518 (1522 Bytes in case of VLAN Tag) octets (excluding framing bits, but including FCS octets) and were otherwise well formed. This counter is not incremented for too long frames.')
f10IfInCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInCRC.setStatus('current')
if mibBuilder.loadTexts: f10IfInCRC.setDescription('The total number of frames received that had a length (ex-cluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad CRC.')
f10IfInOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInOverruns.setStatus('current')
if mibBuilder.loadTexts: f10IfInOverruns.setDescription('The total number of frames dropped because of buffer issue.')
f10IfOutVlanPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutVlanPkts.setStatus('current')
if mibBuilder.loadTexts: f10IfOutVlanPkts.setDescription('The Number of Good VLAN Tagged Frames sent successfully.')
f10IfOutUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutUnderruns.setStatus('current')
if mibBuilder.loadTexts: f10IfOutUnderruns.setDescription('The total number of frames dropped because of buffer underrun.')
f10IfOutUnicasts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutUnicasts.setStatus('current')
if mibBuilder.loadTexts: f10IfOutUnicasts.setDescription('The Number of Good Unicast Frames sent successfully.')
f10IfOutCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutCollisions.setStatus('current')
if mibBuilder.loadTexts: f10IfOutCollisions.setDescription('A count of the frames that due to excessive or late collisions are not transmitted successfully.')
f10IfOutWredDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutWredDrops.setStatus('current')
if mibBuilder.loadTexts: f10IfOutWredDrops.setDescription('A count of the frames that are dropped using WRED policy because of to excessive traffic.')
f10IfOut64BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOut64BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfOut64BytePkts.setDescription('The Number of Good Frames sent successfully whose size was 64 Bytes.')
f10IfOut65To127BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOut65To127BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfOut65To127BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 65 to 127 Bytes.')
f10IfOut128To255BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOut128To255BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfOut128To255BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 128 to 255 Bytes.')
f10IfOut256To511BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOut256To511BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfOut256To511BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 256 to 511 Bytes.')
f10IfOut512To1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOut512To1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfOut512To1023BytePkts.setDescription('The Number of Good Frames sent successfully whose size was in the range of 512 to 1023 Bytes.')
f10IfOutOver1023BytePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutOver1023BytePkts.setStatus('current')
if mibBuilder.loadTexts: f10IfOutOver1023BytePkts.setDescription('The Number of Good Frames sent successfully whose size was greater than 1023 Bytes.')
f10IfOutThrottles = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutThrottles.setStatus('current')
if mibBuilder.loadTexts: f10IfOutThrottles.setDescription('This counter is incremented when a valid frame with a length or type field value equal to 0x8808 (Control Frame) is sent.')
f10IfLastDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 25), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfLastDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: f10IfLastDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which this interface's counters suffered a discontinuity via a reset. If no such discontinuities have occurred since the last reinitialization of the local management subsystem, then this object contains a zero value.")
f10IfInCentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfInCentRate.setStatus('current')
if mibBuilder.loadTexts: f10IfInCentRate.setDescription('This is the ingress rate in percentage. This is an integer value which can go from 0 to 100.')
f10IfOutCentRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 11, 1, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f10IfOutCentRate.setStatus('current')
if mibBuilder.loadTexts: f10IfOutCentRate.setDescription('This is the egress rate in percentage. This is an integer value which can go from 0 to 100.')
f10IfExtensionMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2))
f10IfExtensionMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1))
f10IfExtensionMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2))
f10IfExtensionMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 1, 1)).setObjects(("F10-IF-EXTENSION-MIB", "f10IfParamsGroup"), ("F10-IF-EXTENSION-MIB", "f10IfStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10IfExtensionMibCompliance = f10IfExtensionMibCompliance.setStatus('current')
if mibBuilder.loadTexts: f10IfExtensionMibCompliance.setDescription('The compliance statement for Dell Networking OS IF Extension MIB.')
f10IfParamsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 1)).setObjects(("F10-IF-EXTENSION-MIB", "f10IfIpMtu"), ("F10-IF-EXTENSION-MIB", "f10IfDuplexMode"), ("F10-IF-EXTENSION-MIB", "f10IfQueueingStrategy"), ("F10-IF-EXTENSION-MIB", "f10IfRxFlowCtrl"), ("F10-IF-EXTENSION-MIB", "f10IfTxFlowCtrl"), ("F10-IF-EXTENSION-MIB", "f10IfDescr"), ("F10-IF-EXTENSION-MIB", "f10IfAdminStatus"), ("F10-IF-EXTENSION-MIB", "f10IfRateInterval"), ("F10-IF-EXTENSION-MIB", "f10IfSpeed"), ("F10-IF-EXTENSION-MIB", "f10IfPortListBitPos"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10IfParamsGroup = f10IfParamsGroup.setStatus('current')
if mibBuilder.loadTexts: f10IfParamsGroup.setDescription('A collection of objects providing the Dell Networking OS IF Extenstion parameters.')
f10IfStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 11, 2, 2, 2)).setObjects(("F10-IF-EXTENSION-MIB", "f10IfInVlanPkts"), ("F10-IF-EXTENSION-MIB", "f10IfIn64BytePkts"), ("F10-IF-EXTENSION-MIB", "f10ifIn65To127BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfIn128To255BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfIn256To511BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfIn512To1023BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfInOver1023BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfInThrottles"), ("F10-IF-EXTENSION-MIB", "f10IfInRunts"), ("F10-IF-EXTENSION-MIB", "f10IfInGiants"), ("F10-IF-EXTENSION-MIB", "f10IfInCRC"), ("F10-IF-EXTENSION-MIB", "f10IfInOverruns"), ("F10-IF-EXTENSION-MIB", "f10IfOutVlanPkts"), ("F10-IF-EXTENSION-MIB", "f10IfOutUnderruns"), ("F10-IF-EXTENSION-MIB", "f10IfOutUnicasts"), ("F10-IF-EXTENSION-MIB", "f10IfOutCollisions"), ("F10-IF-EXTENSION-MIB", "f10IfOutWredDrops"), ("F10-IF-EXTENSION-MIB", "f10IfOut64BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfOut65To127BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfOut128To255BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfOut256To511BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfOut512To1023BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfOutOver1023BytePkts"), ("F10-IF-EXTENSION-MIB", "f10IfOutThrottles"), ("F10-IF-EXTENSION-MIB", "f10IfLastDiscontinuityTime"), ("F10-IF-EXTENSION-MIB", "f10IfInCentRate"), ("F10-IF-EXTENSION-MIB", "f10IfOutCentRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10IfStatsGroup = f10IfStatsGroup.setStatus('current')
if mibBuilder.loadTexts: f10IfStatsGroup.setDescription('A collection of objects providing the interface statistics.')
mibBuilder.exportSymbols("F10-IF-EXTENSION-MIB", f10IfPortListBitPos=f10IfPortListBitPos, f10IfDescr=f10IfDescr, f10IfOutCollisions=f10IfOutCollisions, f10IfEntry=f10IfEntry, f10IfOutOver1023BytePkts=f10IfOutOver1023BytePkts, f10IfInOverruns=f10IfInOverruns, f10IfDuplexMode=f10IfDuplexMode, PYSNMP_MODULE_ID=f10IfExtensionMib, f10IfTxFlowCtrl=f10IfTxFlowCtrl, f10IfInGiants=f10IfInGiants, f10IfOut65To127BytePkts=f10IfOut65To127BytePkts, f10IfExtensionMibConformance=f10IfExtensionMibConformance, f10IfExtensionParams=f10IfExtensionParams, f10IfIn64BytePkts=f10IfIn64BytePkts, f10IfExtensionStats=f10IfExtensionStats, f10IfOutThrottles=f10IfOutThrottles, f10IfInOver1023BytePkts=f10IfInOver1023BytePkts, f10ifIn65To127BytePkts=f10ifIn65To127BytePkts, f10IfOutVlanPkts=f10IfOutVlanPkts, f10IfExtensionMibObject=f10IfExtensionMibObject, f10IfInVlanPkts=f10IfInVlanPkts, f10IfInThrottles=f10IfInThrottles, f10IfExtensionMib=f10IfExtensionMib, f10IfIn128To255BytePkts=f10IfIn128To255BytePkts, f10IfOutUnderruns=f10IfOutUnderruns, f10IfOut256To511BytePkts=f10IfOut256To511BytePkts, f10IfExtensionMibCompliances=f10IfExtensionMibCompliances, f10IfOutWredDrops=f10IfOutWredDrops, f10IfOutUnicasts=f10IfOutUnicasts, f10IfInCentRate=f10IfInCentRate, f10IfQueueingStrategy=f10IfQueueingStrategy, f10IfRxFlowCtrl=f10IfRxFlowCtrl, f10IfStaticsTable=f10IfStaticsTable, f10IfExtensionMibGroups=f10IfExtensionMibGroups, f10IfExtensionMibCompliance=f10IfExtensionMibCompliance, f10IfRateInterval=f10IfRateInterval, f10IfInCRC=f10IfInCRC, f10IfTable=f10IfTable, f10IfIn512To1023BytePkts=f10IfIn512To1023BytePkts, f10IfSpeed=f10IfSpeed, f10IfIn256To511BytePkts=f10IfIn256To511BytePkts, f10IfIpMtu=f10IfIpMtu, f10IfStaticsEntry=f10IfStaticsEntry, f10IfLastDiscontinuityTime=f10IfLastDiscontinuityTime, f10IfStatsGroup=f10IfStatsGroup, f10IfOutCentRate=f10IfOutCentRate, f10IfOut128To255BytePkts=f10IfOut128To255BytePkts, f10IfInRunts=f10IfInRunts, f10IfOut64BytePkts=f10IfOut64BytePkts, f10IfAdminStatus=f10IfAdminStatus, f10IfOut512To1023BytePkts=f10IfOut512To1023BytePkts, f10IfParamsGroup=f10IfParamsGroup)
