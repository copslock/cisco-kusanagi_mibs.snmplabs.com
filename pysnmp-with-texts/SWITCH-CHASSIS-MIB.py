#
# PySNMP MIB module SWITCH-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEFINITIONS
# Produced by pysmi-0.3.4 at Wed May  1 12:37:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ModuleIdentity, iso, TimeTicks, NotificationType, Bits, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ModuleIdentity", "iso", "TimeTicks", "NotificationType", "Bits", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "IpAddress", "Integer32")
TimeStamp, DisplayString, TextualConvention, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention", "RowStatus", "MacAddress")
switchChassis, = mibBuilder.importSymbols("TELESYN-ATI-TC", "switchChassis")
switchChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1))
switchChassisMib.setRevisions(('1997-04-29 20:00', '1997-01-14 20:00', '1996-12-19 22:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: switchChassisMib.setRevisionsDescriptions(('Changed the status of the objects in ipParams group to obsolete. The objects in this group are defined elsewhere or not applicable.', 'Redefined the TFTP objects in TftpGroup for executing a file transfer between the chassis and the TFTP server. Deprecated the Console objects.', 'Initial Release.',))
if mibBuilder.loadTexts: switchChassisMib.setLastUpdated('9704292000Z')
if mibBuilder.loadTexts: switchChassisMib.setOrganization('')
if mibBuilder.loadTexts: switchChassisMib.setContactInfo('')
if mibBuilder.loadTexts: switchChassisMib.setDescription('The MIB module for SWITCH chassis entity.')
class HostNameOrIpAddr(DisplayString):
    description = 'The DNS, NIS (or equivalent name), or the ip address (in dotted quad notation) of the host.'
    status = 'current'

class HwIdentifier(TextualConvention, OctetString):
    description = 'The hardware identifier consists of 2 16 bit values, called major and minor. The first 2 octets contain the major number; the second 2 octets contain the minor number.'
    status = 'current'
    displayHint = '2d.2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class SwVersionId(TextualConvention, OctetString):
    description = 'The software version id consists of 3 16 bit values. The first 2 octets contain the major number; the octets 3, 4 contain the minor number, octets 5,6 contain a release number.'
    status = 'current'
    displayHint = '2d.2d.2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

chassisParams = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1))
ipParams = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3))
sysConfigParams = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4))
snmpParams = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6))
consoleParams = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7))
logParams = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8))
bootParams = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9))
chassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNumber.setStatus('current')
if mibBuilder.loadTexts: chassisSerialNumber.setDescription('The serial number of the chassis.')
chassisHwId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 2), HwIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisHwId.setStatus('current')
if mibBuilder.loadTexts: chassisHwId.setDescription('A version number for the motherboard - first 16 bits is the major number, second 16 bits is the minor number.')
chassisOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisOSVersion.setStatus('current')
if mibBuilder.loadTexts: chassisOSVersion.setDescription(' Software version of the operating system kernel.')
chassisFwVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFwVersion.setStatus('current')
if mibBuilder.loadTexts: chassisFwVersion.setDescription('The chassis firmware version. ')
chassisLastChanges = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisLastChanges.setStatus('current')
if mibBuilder.loadTexts: chassisLastChanges.setDescription('Counts the number of times the system config file has been written to flash since last reboot.')
chassisBaseMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisBaseMacAddress.setStatus('current')
if mibBuilder.loadTexts: chassisBaseMacAddress.setDescription("This object is the 6-byte 'base' MAC address for this chassis.")
chassisFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("slowOrStopped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFanStatus.setStatus('current')
if mibBuilder.loadTexts: chassisFanStatus.setDescription("The operational status of fan. 'slowOrStopped' indicates the fan rpm is lower than a minimum required value.")
chassisBoardSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisBoardSerialNumber.setStatus('current')
if mibBuilder.loadTexts: chassisBoardSerialNumber.setDescription('The serial number of the mother board.')
ipAddr = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipAddr.setStatus('obsolete')
if mibBuilder.loadTexts: ipAddr.setDescription("The IP address that the device will use after a restart. The device's active IP address can be determined by examining the appropriate instance of the ipAdEntAddr attribute of the MIB-II IP address table.")
ipNetMask = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipNetMask.setStatus('obsolete')
if mibBuilder.loadTexts: ipNetMask.setDescription("The subnet mask that the device will use after a restart. The device's active subnet mask can be determined by examining the appropriate instance of the ipAdEntNetMask attribute of the MIB-II IP address table.")
ipBcastForm = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allOnes", 1), ("allZeros", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipBcastForm.setStatus('obsolete')
if mibBuilder.loadTexts: ipBcastForm.setDescription("The type of IP broadcast address that the device will use after a restart: the Internet standard all-ones broadcast address or the non- standard all zeros broadcast address. The device's active broadcast address type can be determined by examining the appropriate instance of the ipAdEntBcastAddr attribute of the MIB-II IP address table.")
ipEncap = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8022", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipEncap.setStatus('obsolete')
if mibBuilder.loadTexts: ipEncap.setDescription("The type of IP datagram encapsulation that the device will use after a restart: Ethernet or IEEE802.2. The active type of IP datagram encapsulation can be determined by examining the appropriate instance of the ifType attribute of the MIB-II interfaces table entry for the device's Ethernet interface. If the value of that instance of ifType is ethernet-csmacd(6), then the active type of IP datagram encapsulation is Ethernet; if the value of that instance of ifType is iso88023-csmacd(7), then the active type of IP datagram encapsulation is IEEE802.2.")
ipDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDefaultGateway.setStatus('obsolete')
if mibBuilder.loadTexts: ipDefaultGateway.setDescription("The default gateway IP address that the device will use after a restart. The device's operational default gateway IP address can be determined by examining the value of the ipRouteNextHop.0.0.0.0 attribute of the MIB-II IP routing table.")
ipDomainName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDomainName.setStatus('obsolete')
if mibBuilder.loadTexts: ipDomainName.setDescription("The device's domain name.")
bootFlag = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 16, 32, 48, 64, 128, 192))).clone(namedValues=NamedValues(("bootSystem", 0), ("skipPost", 1), ("runMonitor", 2), ("useBackupBoot", 4), ("loopPost", 8), ("bootLoader", 16), ("bootNetwork", 32), ("bootDiag", 48), ("networkEth0", 64), ("networkEth1", 128), ("networkCom0", 192)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bootFlag.setStatus('deprecated')
if mibBuilder.loadTexts: bootFlag.setDescription(' Boot flags to define the startup parameters')
dramSize = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dramSize.setStatus('current')
if mibBuilder.loadTexts: dramSize.setDescription('DRAM size in bytes')
cpuVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 3), HwIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuVer.setStatus('current')
if mibBuilder.loadTexts: cpuVer.setDescription(' Hardware identifier of the processor.')
iscVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 4), HwIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iscVer.setStatus('current')
if mibBuilder.loadTexts: iscVer.setDescription(' Hardware identifier of the Galileo chip.')
pigVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 5), HwIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pigVer.setStatus('current')
if mibBuilder.loadTexts: pigVer.setDescription('Hardware identifier of the PIG chip.')
postVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 6), SwVersionId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: postVer.setStatus('current')
if mibBuilder.loadTexts: postVer.setDescription('Software version of the POST diagnostic.')
isdVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 7), SwVersionId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdVer.setStatus('current')
if mibBuilder.loadTexts: isdVer.setDescription(' Software version of the ISD diagnostic.')
bootVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 8), SwVersionId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootVer.setStatus('current')
if mibBuilder.loadTexts: bootVer.setDescription('Software version of the boot prom.')
qmuMemSize = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qmuMemSize.setStatus('current')
if mibBuilder.loadTexts: qmuMemSize.setDescription('QME memory size')
segBusTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10), )
if mibBuilder.loadTexts: segBusTable.setStatus('current')
if mibBuilder.loadTexts: segBusTable.setDescription('A table of attributes associated with segBus.')
segBusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1), ).setIndexNames((0, "SWITCH-CHASSIS-MIB", "segBusIndex"))
if mibBuilder.loadTexts: segBusEntry.setStatus('current')
if mibBuilder.loadTexts: segBusEntry.setDescription('A list of attributes associated with a segBus.')
segBusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: segBusIndex.setStatus('current')
if mibBuilder.loadTexts: segBusIndex.setDescription('SegBus number')
segBusPmiuId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1, 2), HwIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segBusPmiuId.setStatus('current')
if mibBuilder.loadTexts: segBusPmiuId.setDescription('Hardware identifier of the Port Manager Interface Unit (PMIU) chip ')
segBusQmuId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1, 3), HwIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segBusQmuId.setStatus('current')
if mibBuilder.loadTexts: segBusQmuId.setDescription('Hardware identifier of the Queue Management Unit (QMU) chip ')
snmpIpTrapRcvrTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1), )
if mibBuilder.loadTexts: snmpIpTrapRcvrTable.setStatus('current')
if mibBuilder.loadTexts: snmpIpTrapRcvrTable.setDescription('A list of entries containing information about network management stations with Ip addresses that are to receive traps generated by this device over UDP.')
snmpIpTrapRcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1), ).setIndexNames((0, "SWITCH-CHASSIS-MIB", "snmpIpTrapRcvrIpAddress"))
if mibBuilder.loadTexts: snmpIpTrapRcvrEntry.setStatus('current')
if mibBuilder.loadTexts: snmpIpTrapRcvrEntry.setDescription('An entry containing information about a single network management station with an Ip address that is to receive traps generated by this device over UDP.')
snmpIpTrapRcvrIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: snmpIpTrapRcvrIpAddress.setStatus('current')
if mibBuilder.loadTexts: snmpIpTrapRcvrIpAddress.setDescription('The Ip address of this trap receiver.')
snmpIpTrapRcvrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpIpTrapRcvrPort.setStatus('current')
if mibBuilder.loadTexts: snmpIpTrapRcvrPort.setDescription('The UDP port number for the Trap receiver.')
snmpIpTrapRcvrCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)).clone('public')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpIpTrapRcvrCommunity.setStatus('current')
if mibBuilder.loadTexts: snmpIpTrapRcvrCommunity.setDescription('The community string to be specified in traps sent to this ip trap receiver.')
snmpIpTrapRcvrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpIpTrapRcvrStatus.setStatus('current')
if mibBuilder.loadTexts: snmpIpTrapRcvrStatus.setDescription('This object is used to create or delete entries in the snmpIpTrapRcvrTable.')
snmpUnAuthIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnAuthIpAddr.setStatus('current')
if mibBuilder.loadTexts: snmpUnAuthIpAddr.setDescription('The IP address of the last management station that attempted to access this agent with an invalid community string. This object is used as a variable binding in an Authentication Failure Trap-PDU.')
snmpUnAuthCommunity = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnAuthCommunity.setStatus('current')
if mibBuilder.loadTexts: snmpUnAuthCommunity.setDescription('The community string specified by the most recent unauthenticated attempt to access this agent. This object is used as a variable binding in an Authentication Failure Trap-PDU.')
consolePortSpeed = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: consolePortSpeed.setStatus('deprecated')
if mibBuilder.loadTexts: consolePortSpeed.setDescription('The speed of the console port in bits per second.')
consolePortDataBits = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(7, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: consolePortDataBits.setStatus('deprecated')
if mibBuilder.loadTexts: consolePortDataBits.setDescription("The console port's number of data bits.")
consolePortStopBits = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("onePointFive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: consolePortStopBits.setStatus('deprecated')
if mibBuilder.loadTexts: consolePortStopBits.setDescription("The console port's number of stop bits.")
consolePortParity = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("odd", 2), ("even", 3), ("mark", 4), ("space", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: consolePortParity.setStatus('deprecated')
if mibBuilder.loadTexts: consolePortParity.setDescription("The console port's parity setting.")
eventLogEnable = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventLogEnable.setStatus('current')
if mibBuilder.loadTexts: eventLogEnable.setDescription('The value of this object indicates whether or not system event logging is currently enabled. Changes to this object take effect immediately.')
eventLogSize = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogSize.setStatus('current')
if mibBuilder.loadTexts: eventLogSize.setDescription('The maximum number of entries retrievable from the system event log. If the value of this object is greater than the value of the eventLogCount object, then only eventLogCount entries have been logged and can be retrieved.')
eventLogCount = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogCount.setStatus('current')
if mibBuilder.loadTexts: eventLogCount.setDescription("The total number of events logged to the system event log. If the value of this object exceeds the value of the eventLogSize object, only the most recent eventLogSize entries can be retrieved. Setting the value of this object to zero clears the device's system event log.")
eventLogTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4), )
if mibBuilder.loadTexts: eventLogTable.setStatus('current')
if mibBuilder.loadTexts: eventLogTable.setDescription('A list of system event log entries.')
eventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1), ).setIndexNames((0, "SWITCH-CHASSIS-MIB", "eventLogIndex"))
if mibBuilder.loadTexts: eventLogEntry.setStatus('current')
if mibBuilder.loadTexts: eventLogEntry.setDescription('A single system event log entry.')
eventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: eventLogIndex.setStatus('current')
if mibBuilder.loadTexts: eventLogIndex.setDescription('A unique value for each entry in the event log. Its value is between 1 and the minimum of the value of the eventLogSize and eventLogCount objects. The oldest event in the log corresponds to index 1.')
eventLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogTime.setStatus('current')
if mibBuilder.loadTexts: eventLogTime.setDescription('The time (according to the system clock) in human-readable form at which this system event log entry was logged.')
eventLogDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogDescr.setStatus('current')
if mibBuilder.loadTexts: eventLogDescr.setDescription('A human-readable string describing the event represented by this system event log entry.')
eventLogDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogDetail.setStatus('current')
if mibBuilder.loadTexts: eventLogDetail.setDescription('A human-readable string providing more detailed information about the event respresented by this system event log entry.')
eventLogRawEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogRawEntry.setStatus('current')
if mibBuilder.loadTexts: eventLogRawEntry.setDescription('The first 255 octets of raw, unformatted system event log entry as it appears internally.')
deviceReset = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceReset.setStatus('current')
if mibBuilder.loadTexts: deviceReset.setDescription('The value of this object returned in response to an SNMP Get or Get-Next request is always noOp(1). Changing the value of this object to reset(2) will cause the device to be reset.')
tftpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4))
tftpServerName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 1), HostNameOrIpAddr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpServerName.setStatus('current')
if mibBuilder.loadTexts: tftpServerName.setDescription("The name of the TFTP server from which to read or write the device's configuration files or from which to read a firmware image. The value of this object can be a fully- or partially-qualified domain name system (dns) name, or it can be an ip address in the familiar 'dotted-quad' notation. If the value of this object is a fully- or partially-qualified dns name, the device will attempt to use the Domain Name System to convert the name to an ip address before initiating a transaction with this TFTP server. This object may be set only if tftpAdminStatus has the value 'configure'.")
tftpUserName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpUserName.setStatus('current')
if mibBuilder.loadTexts: tftpUserName.setDescription("The user name that makes the TFTP request. This object may be set only if tftpAdminStatus has the value 'configure'.")
tftpRemoteFileName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpRemoteFileName.setStatus('current')
if mibBuilder.loadTexts: tftpRemoteFileName.setDescription("The file name of the file on the remote TFTP server. This object may be set only if tftpAdminStatus has the value 'configure'.")
tftpLocalFileName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpLocalFileName.setStatus('current')
if mibBuilder.loadTexts: tftpLocalFileName.setDescription("The local file name of the file which is copied to or from the remote server. If this string is a 0 length string, then the value of tftpRemoteFileName shall also be used as the local file name. This object may be set only if tftpAdminStatus has the value 'configure'.")
tftpOperation = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("putFile", 1), ("getFile", 2), ("getFirmware", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpOperation.setStatus('current')
if mibBuilder.loadTexts: tftpOperation.setDescription("When tftpOperation has the value putFile(1) when tftpAdminStatus is set to 'execute', the device attempts to copy the file identified by tftpLocalFileName to the file tfptRemoteFileName. When tftpOperation has the value getFile(2) when tftpAdminStatus is set to 'execute', the device attempts to copy the file identified by tftpRemoteFileName on the remote tftp server to the file identified by tftpLocalFileName. When tftpOperation has the value getFirmware(3) when tftpAdminStatus is set to 'execute', the device attempts to replace its firmware image with the file identified by tftpRemoteFileName. This firmware file will be used the next time the system is reset. When tftpOperation has the value putConfig(1) when tftpAdminStatus is set to 'execute', the device attempts to copy the file identified by tftpLocalFileName to the file tfptRemoteFileName. When tftpOperation has the value getConfig(2) when tftpAdminStatus is set to 'execute', the device attempts to copy the file identified by tftpRemoteFileName on the remote tftp server to the file identified by tftpLocalFileName. ")
tftpAdminState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configure", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpAdminState.setStatus('current')
if mibBuilder.loadTexts: tftpAdminState.setDescription("This object is used to initiate a file transfer using the TFTP protocol between the local system and a remote TFTP server identified by tftpServerAddr. The file name on the remote server is identified by tftpRemoteFileName and the local file name is identified by tftpLocalFileName. The tftp operation is identified by the valu of tftpOperation. The objects tftpServerName, tftpUserName, tftpLocalFileName, tftpRemoteFileName, and tftpOperation may only be set when tftpAdminState has the value 'configure'. When tftpAdminState is set to 'execute', the operation identified by tftpOperation shall be started and the state of the operation is reflected in tftpOperationState. Setting this attribute to 'execute' when tftpOperationState is not 'inactive' has no effect on the operational state. Under normal operation tftpAdminState should only be set to 'configure' if tftpOperationState is not 'executing'. If tftpOperationState is 'executing' then the system may attempt to abort the current opertion and change the operation state to 'inactive' or not permitting the set to occur by returning the snmp error 'inconsistentValue'.")
tftpOperationState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("inactive", 1), ("executing", 2), ("succeeded", 3), ("localFileProblem", 4), ("unknownHost", 5), ("timedOut", 6), ("remoteFileProblem", 7), ("otherFailure", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpOperationState.setStatus('current')
if mibBuilder.loadTexts: tftpOperationState.setDescription("The value 'executing' reflects a transition of tftpAdminState from 'configure' to 'execute'. In the 'executing' state, the TFTP operation identified by the value of tftpOperation shall begin with the values for the objects tftpServerName, tftpUserName, tftpRemoteFileName, and tftpLocalFileName. When the TFTP operation has completed successfully, the value of tftpOperation shall be set to 'succeeded'. If the operation failed, the value shall be set to one of 'localFileProblem', 'unknownHost', 'timedOut', 'remoteFileProblem', or 'otherFailure'. Any state transition shall result in setting the tftpOperationStateChange object.")
tftpOperationStateChange = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpOperationStateChange.setStatus('current')
if mibBuilder.loadTexts: tftpOperationStateChange.setDescription('This is the value of sysUpTime when the value of tftpOperationState changes.')
tftpErrorMessage = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpErrorMessage.setStatus('current')
if mibBuilder.loadTexts: tftpErrorMessage.setDescription('An error message giving a brief description of the error if the tftpOperation did not succeed.')
mibBuilder.exportSymbols("SWITCH-CHASSIS-MIB", eventLogDescr=eventLogDescr, ipNetMask=ipNetMask, chassisLastChanges=chassisLastChanges, SwVersionId=SwVersionId, chassisSerialNumber=chassisSerialNumber, segBusTable=segBusTable, snmpIpTrapRcvrIpAddress=snmpIpTrapRcvrIpAddress, eventLogCount=eventLogCount, chassisOSVersion=chassisOSVersion, bootVer=bootVer, eventLogEnable=eventLogEnable, segBusPmiuId=segBusPmiuId, consolePortDataBits=consolePortDataBits, isdVer=isdVer, eventLogTable=eventLogTable, consolePortSpeed=consolePortSpeed, eventLogEntry=eventLogEntry, switchChassisMib=switchChassisMib, snmpIpTrapRcvrPort=snmpIpTrapRcvrPort, ipDomainName=ipDomainName, tftpUserName=tftpUserName, chassisFwVersion=chassisFwVersion, segBusQmuId=segBusQmuId, consoleParams=consoleParams, iscVer=iscVer, HostNameOrIpAddr=HostNameOrIpAddr, snmpIpTrapRcvrTable=snmpIpTrapRcvrTable, tftpGroup=tftpGroup, qmuMemSize=qmuMemSize, cpuVer=cpuVer, deviceReset=deviceReset, tftpServerName=tftpServerName, tftpLocalFileName=tftpLocalFileName, ipDefaultGateway=ipDefaultGateway, ipBcastForm=ipBcastForm, consolePortStopBits=consolePortStopBits, tftpOperation=tftpOperation, chassisParams=chassisParams, snmpUnAuthIpAddr=snmpUnAuthIpAddr, sysConfigParams=sysConfigParams, postVer=postVer, eventLogRawEntry=eventLogRawEntry, tftpAdminState=tftpAdminState, tftpRemoteFileName=tftpRemoteFileName, logParams=logParams, chassisBoardSerialNumber=chassisBoardSerialNumber, chassisBaseMacAddress=chassisBaseMacAddress, ipParams=ipParams, snmpIpTrapRcvrCommunity=snmpIpTrapRcvrCommunity, PYSNMP_MODULE_ID=switchChassisMib, ipAddr=ipAddr, chassisHwId=chassisHwId, ipEncap=ipEncap, eventLogIndex=eventLogIndex, tftpOperationState=tftpOperationState, chassisFanStatus=chassisFanStatus, segBusIndex=segBusIndex, eventLogSize=eventLogSize, eventLogTime=eventLogTime, tftpErrorMessage=tftpErrorMessage, tftpOperationStateChange=tftpOperationStateChange, snmpParams=snmpParams, pigVer=pigVer, bootParams=bootParams, snmpIpTrapRcvrEntry=snmpIpTrapRcvrEntry, segBusEntry=segBusEntry, dramSize=dramSize, snmpIpTrapRcvrStatus=snmpIpTrapRcvrStatus, consolePortParity=consolePortParity, HwIdentifier=HwIdentifier, bootFlag=bootFlag, snmpUnAuthCommunity=snmpUnAuthCommunity, eventLogDetail=eventLogDetail)
