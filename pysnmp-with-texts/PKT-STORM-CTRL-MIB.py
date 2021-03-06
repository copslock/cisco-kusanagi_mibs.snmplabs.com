#
# PySNMP MIB module PKT-STORM-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PKT-STORM-CTRL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:40:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, NotificationType, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "NotificationType", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32")
TextualConvention, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString")
swPktStormMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 25))
if mibBuilder.loadTexts: swPktStormMIB.setLastUpdated('0809030000Z')
if mibBuilder.loadTexts: swPktStormMIB.setOrganization(' ')
if mibBuilder.loadTexts: swPktStormMIB.setContactInfo(' ')
if mibBuilder.loadTexts: swPktStormMIB.setDescription('The Structure of packet storm control management for the proprietary enterprise.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swPktStormCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 25, 1))
swPktStormInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 25, 2))
swPktStormMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 25, 3))
swPktStormNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 25, 5))
swPktStormTrapCtrl = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 25, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("stormOccurred", 2), ("stormCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormTrapCtrl.setStatus('current')
if mibBuilder.loadTexts: swPktStormTrapCtrl.setDescription('This object controls when a storm control notification will be generated. If the object is set to none (1): No notifications will be generated. stormOccurred(2): stormCleared(3):A notification will be generated when a storm event is detected or cleared respectively. both (4): A notification will be generated both when a storm event is detected and cleared. NOTE:The default value of this object is none(1). ')
swPktStormCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1), )
if mibBuilder.loadTexts: swPktStormCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlTable.setDescription('A table that contains information about packet storm control. A S/W mechanism is provided to monitor the traffic rate in addition to the H/W storm control mechanism. If the traffic rate is too high, this port will be shut down.')
swPktStormCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1), ).setIndexNames((0, "PKT-STORM-CTRL-MIB", "swPktStormCtrlPortIndex"))
if mibBuilder.loadTexts: swPktStormCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlEntry.setDescription('A list of information for each port of the device.')
swPktStormCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPktStormCtrlPortIndex.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlPortIndex.setDescription("This object indicates the device's port number.(1..Max port number in the device).It is used to specify a range of ports to be configured.")
swPktStormCtrlthreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormCtrlthreshold.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlthreshold.setDescription('This object is the upper threshold at which the specified storm control will turn on.')
swPktStormCtrlBroadcastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormCtrlBroadcastStatus.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlBroadcastStatus.setDescription('This object indicates whether the broadcast storm control is enabled or disabled.')
swPktStormCtrlMulticastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormCtrlMulticastStatus.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlMulticastStatus.setDescription('This object indicates whether the multicast storm control is enabled or disabled.')
swPktStormCtrlUnicastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormCtrlUnicastStatus.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlUnicastStatus.setDescription('This object indicates whether the unicast (Destination Loopback Fail) storm control is enabled or disabled.')
swPktStormCtrlActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shutdown", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormCtrlActionStatus.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlActionStatus.setDescription('There are two actions to take for storm control, shutdown and drop. The former is implemented in S/W, and the latter is implemented in H/W. If a user chooses shutdown, they will need to configure both the back_off and the time_interval.')
swPktStormCtrlCountDown = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormCtrlCountDown.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlCountDown.setDescription("If a packet storm has been encountered continuously on a given port for a long period of time (indicated by the value of this object), the port will be shut down forever until it's recovered manually.The range of the countdown time is 5 to 30 minutes. A user can configure the countdown to 0 to disable the function of shutdown forever. If this value is set from 1 to 4, a 'bad value' return code will be indicated")
swPktStormCtrlTimeinterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 25, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPktStormCtrlTimeinterval.setStatus('current')
if mibBuilder.loadTexts: swPktStormCtrlTimeinterval.setDescription('This object is the sampling interval of received packet counts. The possible value will be from 5 to 30 seconds.')
swPktStormNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 25, 5, 0))
swPktStormOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 25, 5, 0, 1)).setObjects(("PKT-STORM-CTRL-MIB", "swPktStormCtrlPortIndex"))
if mibBuilder.loadTexts: swPktStormOccurred.setStatus('current')
if mibBuilder.loadTexts: swPktStormOccurred.setDescription('This trap is sent when a packet storm is detected by a packet storm mechanism and a shutdown action is taken. ')
swPktStormCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 25, 5, 0, 2)).setObjects(("PKT-STORM-CTRL-MIB", "swPktStormCtrlPortIndex"))
if mibBuilder.loadTexts: swPktStormCleared.setStatus('current')
if mibBuilder.loadTexts: swPktStormCleared.setDescription('The trap is sent when the packet storm is cleared by the packet storm mechanism.')
mibBuilder.exportSymbols("PKT-STORM-CTRL-MIB", swPktStormCtrlPortIndex=swPktStormCtrlPortIndex, swPktStormOccurred=swPktStormOccurred, swPktStormCtrlActionStatus=swPktStormCtrlActionStatus, swPktStormCtrlUnicastStatus=swPktStormCtrlUnicastStatus, swPktStormCtrlTable=swPktStormCtrlTable, swPktStormTrapCtrl=swPktStormTrapCtrl, PYSNMP_MODULE_ID=swPktStormMIB, swPktStormMgmt=swPktStormMgmt, swPktStormCleared=swPktStormCleared, swPktStormCtrlTimeinterval=swPktStormCtrlTimeinterval, swPktStormNotify=swPktStormNotify, swPktStormCtrl=swPktStormCtrl, swPktStormCtrlBroadcastStatus=swPktStormCtrlBroadcastStatus, swPktStormNotifyPrefix=swPktStormNotifyPrefix, swPktStormMIB=swPktStormMIB, swPktStormCtrlEntry=swPktStormCtrlEntry, swPktStormCtrlCountDown=swPktStormCtrlCountDown, swPktStormCtrlthreshold=swPktStormCtrlthreshold, swPktStormCtrlMulticastStatus=swPktStormCtrlMulticastStatus, swPktStormInfo=swPktStormInfo, PortList=PortList)
