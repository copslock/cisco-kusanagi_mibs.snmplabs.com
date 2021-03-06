#
# PySNMP MIB module MITEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, NotificationType, Counter32, Counter64, TimeTicks, ModuleIdentity, iso, Bits, Gauge32, IpAddress, internet, MibIdentifier, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "NotificationType", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "iso", "Bits", "Gauge32", "IpAddress", "internet", "MibIdentifier", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
snmpV2 = MibIdentifier((1, 3, 6, 1, 6))
snmpDomains = MibIdentifier((1, 3, 6, 1, 6, 1))
snmpUDPDomain = MibIdentifier((1, 3, 6, 1, 6, 1, 1))
class InterfaceIndex(Integer32):
    pass

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class TimeStamp(TimeTicks):
    pass

class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mitelIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1))
mitelExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 2))
mitelExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 3))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5))
mitelIdMgmtPlatforms = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 1))
mitelIdCallServers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2))
mitelIdTerminals = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 3))
mitelIdInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 4))
mitelIdCtiPlatforms = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 5))
mitelIdMgmtOpsMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 1, 1))
mitelIdCsMc2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 1))
mitelIdCs2000Light = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 2))
mitelExtInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 3, 2))
mitelPropApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1))
mitelPropTransmission = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 2))
mitelPropProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 3))
mitelPropUtilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 4))
mitelPropHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 5))
mitelPropNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 6))
mitelPropReset = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 7))
mitelAppCallServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1))
mitelNotifTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 6, 1))
mitelConfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 1))
mitelConfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2))
mitelGrpCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1))
mitelGrpOpsMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 2))
mitelGrpCs2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3))
mitelConfAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 3))
class TDomain(ObjectIdentifier):
    pass

class TAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class MitelIfType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("dnic", 1))

class MitelNotifyTransportType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mitelNotifTransV1Trap", 1), ("mitelNotifTransV2Trap", 2), ("mitelNotifTransInform", 3))

mitelIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 1027, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mitelIfNumber.setDescription('The number of MITEL proprietary interfaces (regardless of their current state) present on this system.')
mitelIfTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2), )
if mibBuilder.loadTexts: mitelIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelIfTable.setDescription('A list of interface entries. The number of entries is given by the value of mitelIfNumber. The table consists of one row for each MITEL-specific interface, and is indexed by the ifIndex value of the corresponding row in the MIB-II ifTable.')
mitelIfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mitelIfTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mitelIfTableEntry.setDescription('An entry containing management information applicable to a particular interface.')
mitelIfTblType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1, 1), MitelIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfTblType.setStatus('mandatory')
if mibBuilder.loadTexts: mitelIfTblType.setDescription('The type of interface. Additional values for mitelIfTblType are assigned by the Standards Group, through updating the syntax of the MitelIfType textual convention. This row is deleted automatically when the corresponding ifTable row is deleted.')
mitelResetReason = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("shutdown", 1), ("coldStart", 2), ("warmStart", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelResetReason.setStatus('mandatory')
if mibBuilder.loadTexts: mitelResetReason.setDescription('Indicates the reason for the last mitelTrapsReset notification generated. The shutdown(1) is only visible in a mitelTrapsReset notification, and indicates that the agent is shutting down, to be followed at an unspecified time by a coldStart. It is expected that agents may want to expand the syntax in an agent-specific manner (e.g. to identify specific components).')
mitelResetPlatform = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 7, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelResetPlatform.setStatus('mandatory')
if mibBuilder.loadTexts: mitelResetPlatform.setDescription('Write true(1) to this object to reset the agent platform (coldStart). This object always reads as false.')
mitelResetAgent = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 7, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelResetAgent.setStatus('mandatory')
if mibBuilder.loadTexts: mitelResetAgent.setDescription('Write true(1) to this object to reset the agent itself (warmStart). This object always reads as false.')
mitelNotifCount = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifCount.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifCount.setDescription('The number of MITEL-defined notifications supported by this agent.')
mitelNotifEnableTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3), )
if mibBuilder.loadTexts: mitelNotifEnableTable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnableTable.setDescription('A list of the MITEL-defined notifications supported by this agent. The number of entries in the table is defined by mitelNotifCount. This table is maintained in non-volatile memory, and is re-built upon agent restart.')
mitelNotifEnableTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifEnblTblIndex"))
if mibBuilder.loadTexts: mitelNotifEnableTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnableTableEntry.setDescription('An entry containing notification information.')
mitelNotifEnblTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnblTblIndex.setDescription('The index of this row. A unique value, greater than zero, for each row. This value is sent as the specific-trap value when an SNMPv1 Trap-PDU is used. For this reason, the notification OID must always map to the same value on every platform.')
mitelNotifEnblTblOid = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblOid.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnblTblOid.setDescription('The OID value of the notification. This is the value of the corresponding NOTIFICATION-TYPE macro. For SNMPv1 agents, this is implemented as zeroDotZero (from RFC1442).')
mitelNotifEnblTblEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifEnblTblEnable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnblTblEnable.setDescription('True if the generation of this notification (to all registered managers) is enabled.')
mitelNotifEnblTblAck = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifEnblTblAck.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnblTblAck.setDescription('True if the notification is to be acknowledged by at least one manager. A false setting indicates that the mitelNotifMgrTblTimeout and mitelNotifMgrTblRetries values are ignored.')
mitelNotifEnblTblOccurrences = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblOccurrences.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnblTblOccurrences.setDescription('A count of the number of times the conditions that would generate this trap have been detected at this agent since the last reset, regardless of whether the trap is enabled or not.')
mitelNotifEnblTblDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifEnblTblDescr.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifEnblTblDescr.setDescription('Textual description of this notification.')
mitelNotifManagerTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4), )
if mibBuilder.loadTexts: mitelNotifManagerTable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifManagerTable.setDescription('A list of the managers that are receiving notifications from this agent. This table is kept in non-volatile memory, and is rebuilt upon agent restart.')
mitelNotifManagerTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifMgrTblIndex"))
if mibBuilder.loadTexts: mitelNotifManagerTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifManagerTableEntry.setDescription('An entry containing manager information.')
mitelNotifMgrTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifMgrTblIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblIndex.setDescription('The index of this row. A unique value, greater than zero, for each row. It is recommended that values are assigned contiguously starting from 1.')
mitelNotifMgrTblStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 2), RowStatus().clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblStatus.setDescription('The status column used for creating, modifying, and deleting instances of the columnar objects in the manager table.')
mitelNotifMgrTblTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 3), MitelNotifyTransportType().clone('mitelNotifTransV1Trap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblTransport.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblTransport.setDescription('Defines how notifications are sent to this manager (either InformRequest or Trap).')
mitelNotifMgrTblDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 4), TDomain().clone((1, 3, 6, 1, 6, 1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblDomain.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblDomain.setDescription('The transport domain of this manager.')
mitelNotifMgrTblAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 5), TAddress().clone(hexValue="c00002000489")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblAddress.setDescription('The transport domain address at which to send the notification.')
mitelNotifMgrTblTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 6), TimeInterval().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblTimeout.setDescription('Number of 1/100ths of a second until a trap confirmation from this manager is deemed to have failed. This only applies for traps in mitelNotifEnableTable where mitelNotifEnblTblAck is true.')
mitelNotifMgrTblRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblRetries.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblRetries.setDescription('Number of times the agent will attempt to retry sending a trap when the confirmation is not received. If the trap is not confirmed on the last retry, the mitelNotifHistTblConfirmed object will be false. This only applies for traps in mitelNotifEnableTable where mitelNotifEnblTblAck is true.')
mitelNotifMgrTblLife = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 8), TimeInterval().clone(8640000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblLife.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblLife.setDescription('Number of 1/100ths of a second until this row is deleted. If initially set to 0, this row will exist forever. Normal use of this field is to set it to a long timeout (e.g. 1 day) and then reset it at a shorter interval (e.g. every 12 hours).')
mitelNotifMgrTblCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 9), OctetString().clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblCommunity.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblCommunity.setDescription('The community string to send in the notification.')
mitelNotifMgrTblName = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 10), DisplayString().clone('None specified.')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifMgrTblName.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifMgrTblName.setDescription('The administrative name of this manager.')
mitelNotifHistoryMax = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 5), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifHistoryMax.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistoryMax.setDescription('The maximum size of the notification history table. Must be greater than or equal to zero... zero indicating the table is not used.')
mitelNotifHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistorySize.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistorySize.setDescription('The current size of the notification history table.')
mitelNotifHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7), )
if mibBuilder.loadTexts: mitelNotifHistoryTable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistoryTable.setDescription('A history of the recent notifications originated from this agent. One entry is generated per notification, regardless of the number of managers registered to receive the notification. The number of entries is given by mitelNotifHistorySize. The table cannot grow beyond mitelNotifHistoryMax... older entries are bumped off once the table reaches the maximum size.')
mitelNotifHistoryTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifHistTblIndex"))
if mibBuilder.loadTexts: mitelNotifHistoryTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistoryTableEntry.setDescription('An entry containing notification information.')
mitelNotifHistTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistTblIndex.setDescription('The index of this row. A unique value, greater than zero, for each row. It is recommended that values are assigned contiguously starting from 1.')
mitelNotifHistTblId = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblId.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistTblId.setDescription('The index value of the corresponding notification entry in mitelNotifEnableTable (i.e. mitelNotifEnblTblIndex).')
mitelNotifHistTblTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblTime.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistTblTime.setDescription('The time the notification was sent.')
mitelNotifHistTblIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistTblIfIndex.setDescription('The ifIndex value corresponding to the ifTable entry of the originating interface (if any). Value is 0 if the notification is not associated with an ifTable entry.')
mitelNotifHistTblConfirmed = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifHistTblConfirmed.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifHistTblConfirmed.setDescription('Indicates whether or not this notification was confirmed by at least one manager. Note this object is only applicable when the corresponding row of mitelNotifEnableTable has mitelNotifEnblTblAck set to true.')
mitelNotifUnackTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8), )
if mibBuilder.loadTexts: mitelNotifUnackTable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifUnackTable.setDescription("A list of notifications sent from this agent that are expected to be acknowledged, but have not yet received the acknowledgement. One entry is created for each acknowledgable notification transmitted from this agent. Managers are expected to delete the rows in this table to acknowledge receipt of the notification. To do so, the index is provided in the notification sent to the manager. Any unacknowledged notifications are removed at the agent's discretion. This table is kept in volatile memory.")
mitelNotifUnackTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1), ).setIndexNames((0, "MITEL-MIB", "mitelNotifUnackTblIndex"))
if mibBuilder.loadTexts: mitelNotifUnackTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifUnackTableEntry.setDescription('An entry containing unacknowledged notification information.')
mitelNotifUnackTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifUnackTblIndex.setDescription('The index of this row. A unique value, greater than zero, for each row. It is recommended that values are assigned contiguously starting from 1, and that they are not re-used (to allow for duplicated Set Requests for destruction of the row).')
mitelNotifUnackTblStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("destory", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelNotifUnackTblStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifUnackTblStatus.setDescription('The status of this row. A status of active indicates that an acknowledgement is still expected. Write a destroy(6) here to acknowledge this notification. A status of notInService indicates that no acknowledgement is expected.')
mitelNotifUnackTblHistory = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblHistory.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifUnackTblHistory.setDescription('The index into the mitelNotifHistoryTable that identifies this notification. If 0, the mitelNotifHistoryTable entry was not created or has been deleted.')
mitelNotifUnackTblManager = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblManager.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifUnackTblManager.setDescription('The index into the mitelNotifManagerTable that identifies this notification. If 0, the mitelNotifManagerTable entry has been deleted.')
mitelNotifUnackTblRetriesLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifUnackTblRetriesLeft.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifUnackTblRetriesLeft.setDescription('The number of retransmission retries left to attempt. This starts at the mitelNotifMgrTblRetries value for the corresponding manager. If 0 is reached, the last retry has been attempted.')
mitelNotifAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 6, 9), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelNotifAgentAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mitelNotifAgentAddress.setDescription('The domain address of this agent, used only in notifications to identify the sending agent. In SNMPv1 implementations, this maps to the agent-addr field of the SNMPv1-Trap PDU.')
mitelTrapsCommLost = NotificationType((1, 3, 6, 1, 4, 1, 1027, 4, 6, 1) + (0,1)).setObjects(("MITEL-MIB", "mitelNotifUnackTblStatus"), ("MITEL-MIB", "mitelNotifMgrTblDomain"), ("MITEL-MIB", "mitelNotifMgrTblAddress"))
if mibBuilder.loadTexts: mitelTrapsCommLost.setDescription('This notification is generated whenever the agent detects the final timeout of a row in the mitelNotifUnackTable. When this occurs, the row corresponding to the manager in mitelNotifManagerTable is set to a RowStatus value of notInService(2), and no further notifications will be sent to the manager until the RowStatus is set back to active(1).')
mitelTrapsReset = NotificationType((1, 3, 6, 1, 4, 1, 1027, 4, 6, 1) + (0,2)).setObjects(("MITEL-MIB", "mitelNotifUnackTblStatus"), ("MITEL-MIB", "mitelResetReason"))
if mibBuilder.loadTexts: mitelTrapsReset.setDescription('This notification is generated whenever the agent detects a reset, either from coldStart, warmStart, or a reset of some part of the hardware. The nature of the reset is provided in mitelResetReason. This notification does not preclude simultaneous generation of a warm/coldStart trap.')
mitelGrpCmnNotifBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 2))
mitelGrpCmnNotifManagers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 3))
mitelGrpCmnNotifHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 4))
mitelGrpCmnNotifAck = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 5))
mitelGrpCmnInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 6))
mitelGrpCmnReset = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 7))
mitelComplMitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 1, 1))
mibBuilder.exportSymbols("MITEL-MIB", mitelNotifMgrTblRetries=mitelNotifMgrTblRetries, mitelGrpCmnInterfaces=mitelGrpCmnInterfaces, mitelPropHardware=mitelPropHardware, mitelExtInterfaces=mitelExtInterfaces, mitelNotifMgrTblTransport=mitelNotifMgrTblTransport, mitelNotifAgentAddress=mitelNotifAgentAddress, mitelNotifMgrTblCommunity=mitelNotifMgrTblCommunity, mitelNotifHistTblIfIndex=mitelNotifHistTblIfIndex, TimeStamp=TimeStamp, mitelNotifEnblTblEnable=mitelNotifEnblTblEnable, mitelConformance=mitelConformance, mitelNotifUnackTableEntry=mitelNotifUnackTableEntry, mitelGrpCommon=mitelGrpCommon, mitelAppCallServer=mitelAppCallServer, mitelNotifEnblTblIndex=mitelNotifEnblTblIndex, mitelGrpCmnNotifAck=mitelGrpCmnNotifAck, mitelNotifHistTblConfirmed=mitelNotifHistTblConfirmed, MitelNotifyTransportType=MitelNotifyTransportType, mitelNotifUnackTable=mitelNotifUnackTable, mitelNotifEnblTblOccurrences=mitelNotifEnblTblOccurrences, mitelNotifCount=mitelNotifCount, mitelNotifHistTblId=mitelNotifHistTblId, mitelConfGroups=mitelConfGroups, mitelNotifMgrTblStatus=mitelNotifMgrTblStatus, TDomain=TDomain, mitelNotifHistoryMax=mitelNotifHistoryMax, InterfaceIndex=InterfaceIndex, mitelNotifManagerTable=mitelNotifManagerTable, mitelNotifHistoryTableEntry=mitelNotifHistoryTableEntry, mitelNotifManagerTableEntry=mitelNotifManagerTableEntry, mitelNotifMgrTblAddress=mitelNotifMgrTblAddress, mitelResetReason=mitelResetReason, mitelNotifHistTblIndex=mitelNotifHistTblIndex, RowStatus=RowStatus, mitelGrpOpsMgr=mitelGrpOpsMgr, mitelPropNotifications=mitelPropNotifications, snmpUDPDomain=snmpUDPDomain, mitelNotifEnblTblOid=mitelNotifEnblTblOid, mitelNotifEnableTableEntry=mitelNotifEnableTableEntry, mitelNotifMgrTblDomain=mitelNotifMgrTblDomain, mitelNotifHistoryTable=mitelNotifHistoryTable, mitelGrpCmnNotifBasic=mitelGrpCmnNotifBasic, mitelTrapsReset=mitelTrapsReset, mitelGrpCs2000=mitelGrpCs2000, mitelExtensions=mitelExtensions, mitelPropReset=mitelPropReset, mitelGrpCmnReset=mitelGrpCmnReset, mitelPropTransmission=mitelPropTransmission, mitelIdMgmtPlatforms=mitelIdMgmtPlatforms, mitelIdTerminals=mitelIdTerminals, mitelGrpCmnNotifHistory=mitelGrpCmnNotifHistory, mitelComplMitel=mitelComplMitel, mitelPropApplications=mitelPropApplications, mitelIdentification=mitelIdentification, mitelTrapsCommLost=mitelTrapsCommLost, mitelNotifUnackTblStatus=mitelNotifUnackTblStatus, mitelNotifHistorySize=mitelNotifHistorySize, mitelNotifUnackTblRetriesLeft=mitelNotifUnackTblRetriesLeft, mitelPropProtocols=mitelPropProtocols, mitelResetPlatform=mitelResetPlatform, MitelIfType=MitelIfType, mitelIdMgmtOpsMgr=mitelIdMgmtOpsMgr, mitelNotifMgrTblTimeout=mitelNotifMgrTblTimeout, snmpV2=snmpV2, mitelPropUtilities=mitelPropUtilities, mitelIfTableEntry=mitelIfTableEntry, mitelIfTblType=mitelIfTblType, mitelIdCtiPlatforms=mitelIdCtiPlatforms, mitelIfNumber=mitelIfNumber, mitelExperimental=mitelExperimental, mitelIfTable=mitelIfTable, mitelProprietary=mitelProprietary, mitelConfAgents=mitelConfAgents, mitelNotifUnackTblIndex=mitelNotifUnackTblIndex, mitelNotifHistTblTime=mitelNotifHistTblTime, mitelResetAgent=mitelResetAgent, mitelIdCallServers=mitelIdCallServers, mitelNotifUnackTblHistory=mitelNotifUnackTblHistory, snmpDomains=snmpDomains, mitelNotifEnblTblDescr=mitelNotifEnblTblDescr, TAddress=TAddress, mitelNotifMgrTblName=mitelNotifMgrTblName, mitelNotifEnblTblAck=mitelNotifEnblTblAck, mitelNotifUnackTblManager=mitelNotifUnackTblManager, mitelNotifEnableTable=mitelNotifEnableTable, mitel=mitel, TimeInterval=TimeInterval, mitelIdCsMc2=mitelIdCsMc2, mitelIdInterfaces=mitelIdInterfaces, mitelIdCs2000Light=mitelIdCs2000Light, mitelNotifMgrTblLife=mitelNotifMgrTblLife, TruthValue=TruthValue, mitelNotifMgrTblIndex=mitelNotifMgrTblIndex, mitelConfCompliances=mitelConfCompliances, mitelNotifTraps=mitelNotifTraps, mitelGrpCmnNotifManagers=mitelGrpCmnNotifManagers)
