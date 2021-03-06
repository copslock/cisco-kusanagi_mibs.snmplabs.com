#
# PySNMP MIB module HUAWEI-TDM-PSN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TDM-PSN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
HWL2VpnVcEncapsType, = mibBuilder.importSymbols("HUAWEI-VPLS-EXT-MIB", "HWL2VpnVcEncapsType")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, Counter64, iso, TimeTicks, Unsigned32, Integer32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "Counter64", "iso", "TimeTicks", "Unsigned32", "Integer32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwTdmPsnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152))
if mibBuilder.loadTexts: hwTdmPsnMIB.setLastUpdated('200706270900Z')
if mibBuilder.loadTexts: hwTdmPsnMIB.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwTdmPsnMIB.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwTdmPsnMIB.setDescription('The HUAWEI-TDM-PSN-MIB contains objects to manage TDM.')
hwTdmPsnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1))
hwTdmPsnPerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1), )
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentTable.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentTable.setDescription('This table provides per TDM PW performance information.')
hwTdmPsnPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1), ).setIndexNames((0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentPwIdIndex"), (0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentPwTypeIndex"))
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentEntry.setDescription('An entry in hwTdmPsnPerfCurrentTable.')
hwTdmPsnPerfCurrentPwIdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentPwIdIndex.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentPwIdIndex.setDescription("Index for the conceptual row identifying a PW within this PW Emulation table.Used in the outgoing PW ID field within the 'Virtual Circuit FEC Element'.")
hwTdmPsnPerfCurrentPwTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 2), HWL2VpnVcEncapsType())
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentPwTypeIndex.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentPwTypeIndex.setDescription('The type of the Virtual Circuit.This value indicate the Service to be carried over this PW.')
hwTdmPsnPerfCurrentMissingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentMissingPkts.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentMissingPkts.setDescription('Number of missing packets (as detected via control word Sequence number gaps).')
hwTdmPsnPerfCurrentPktsReorder = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentPktsReorder.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentPktsReorder.setDescription('Number of packets detected out of sequence (via control word sequence number), but successfully re-ordered. Note: some implementations may not support this Feature.')
hwTdmPsnPerfCurrentJtrBfrUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentJtrBfrUnderruns.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentJtrBfrUnderruns.setDescription('Number of times a packet needed to be played out and the jitter buffer was empty.')
hwTdmPsnPerfCurrentMisorderDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentMisorderDropped.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentMisorderDropped.setDescription('Number of packets detected out of order(via control word Sequence numbers), and could not be re-ordered, or could not fit in the jitter buffer.')
hwTdmPsnPerfCurrentMalformedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentMalformedPkts.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentMalformedPkts.setDescription("Number of packets detected with unexpected size, or bad headers' stack.")
hwTdmPsnPerfCurrentErrorSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentErrorSeconds.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentErrorSeconds.setDescription('The counter associated with the number of Error Seconds encountered.Any malformed packet, seq. error and similar are considered as error second.')
hwTdmPsnPerfCurrentSeverelyErrorSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentSeverelyErrorSeconds.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentSeverelyErrorSeconds.setDescription('The counter associated with the number of Severely Error Seconds encountered.')
hwTdmPsnPerfCurrentUnavailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentUnavailableSeconds.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentUnavailableSeconds.setDescription('The counter associated with the number of Unavailable Seconds encountered. Any consequtive five seconds of SES are counted as one UAS.')
hwTdmPsnPerfCurrentFailureCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentFailureCounts.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentFailureCounts.setDescription('TDM Failure Counts (FC-TDM). The number of TDM failure events. A failure event begins when the LOPS failure is declared, and ends when the failure is cleared. A failure event that begins in one period and ends in another period is counted only in the period in which it begins.')
hwTdmPsnAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2), )
if mibBuilder.loadTexts: hwTdmPsnAlarmTable.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmTable.setDescription('This table provides per CEP PW Status information.')
hwTdmPsnAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1), ).setIndexNames((0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwIdIndex"), (0, "HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwTypeIndex"))
if mibBuilder.loadTexts: hwTdmPsnAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmEntry.setDescription('An entry in hwTdmPsnAlarmTable.')
hwTdmPsnAlarmPwIdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hwTdmPsnAlarmPwIdIndex.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmPwIdIndex.setDescription("Index for the conceptual row identifying a PW within this PW Emulation table.Used in the outgoing PW ID field within the 'Virtual Circuit FEC Element'.")
hwTdmPsnAlarmPwTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 2), HWL2VpnVcEncapsType())
if mibBuilder.loadTexts: hwTdmPsnAlarmPwTypeIndex.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmPwTypeIndex.setDescription('The type of the Virtual Circuit.This value indicate the Service to be carried over this PW.')
hwTdmPsnAlarmPwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnAlarmPwStatus.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmPwStatus.setDescription('This variable indicates the Line Status of the interface. It contains PW alarms information. The hwTdmPsnInfoPwStatus is a bit map represented as a Sum, therefore, it can represent multiple alarms simultaneously. PwNoAlarm must be set if and only if no other flag is set. The various bit positions are: 0 bit PwNoAlarm No alarm present 1 bit PwRAI Remote Alarm Indication 2 bit PwAIS Alarm Indication Signal ')
hwTdmPsnAlarmVcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 1, 2, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTdmPsnAlarmVcIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmVcIfIndex.setDescription('Index of E1 or T1 interface.')
hwTdmPsnMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 2))
hwTdmPsnAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 2, 1)).setObjects(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwStatus"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmVcIfIndex"))
if mibBuilder.loadTexts: hwTdmPsnAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmTrap.setDescription('A hwTdmPsnAlarmTrap trap is sent when the value of an instance hwTdmPsnAlarmPwStatus changes.')
hwTdmPsnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3))
hwTdmPsnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 1))
hwTdmPsnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 1, 1)).setObjects(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentGroup"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTdmPsnMIBCompliance = hwTdmPsnMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnMIBCompliance.setDescription('The compliance statement for TDM.')
hwTdmPsnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2))
hwTdmPsnPerfCurrentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2, 1)).setObjects(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentMissingPkts"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentPktsReorder"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentJtrBfrUnderruns"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentMisorderDropped"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentMalformedPkts"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentErrorSeconds"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentSeverelyErrorSeconds"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentUnavailableSeconds"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnPerfCurrentFailureCounts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTdmPsnPerfCurrentGroup = hwTdmPsnPerfCurrentGroup.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnPerfCurrentGroup.setDescription("The hwTdmPsnPerfCurrentTable's group.")
hwTdmPsnAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2, 2)).setObjects(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmPwStatus"), ("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmVcIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTdmPsnAlarmGroup = hwTdmPsnAlarmGroup.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnAlarmGroup.setDescription("The hwTdmPsnAlarmTable's group.")
hwTdmPsnNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 152, 3, 2, 3)).setObjects(("HUAWEI-TDM-PSN-MIB", "hwTdmPsnAlarmTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTdmPsnNotificationGroup = hwTdmPsnNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwTdmPsnNotificationGroup.setDescription("The TdmPsn's SVC Notification group.")
mibBuilder.exportSymbols("HUAWEI-TDM-PSN-MIB", hwTdmPsnPerfCurrentPktsReorder=hwTdmPsnPerfCurrentPktsReorder, hwTdmPsnPerfCurrentJtrBfrUnderruns=hwTdmPsnPerfCurrentJtrBfrUnderruns, hwTdmPsnPerfCurrentEntry=hwTdmPsnPerfCurrentEntry, hwTdmPsnPerfCurrentErrorSeconds=hwTdmPsnPerfCurrentErrorSeconds, hwTdmPsnPerfCurrentMisorderDropped=hwTdmPsnPerfCurrentMisorderDropped, hwTdmPsnPerfCurrentUnavailableSeconds=hwTdmPsnPerfCurrentUnavailableSeconds, hwTdmPsnAlarmTrap=hwTdmPsnAlarmTrap, hwTdmPsnPerfCurrentPwTypeIndex=hwTdmPsnPerfCurrentPwTypeIndex, hwTdmPsnPerfCurrentMissingPkts=hwTdmPsnPerfCurrentMissingPkts, hwTdmPsnAlarmPwStatus=hwTdmPsnAlarmPwStatus, hwTdmPsnMIBGroups=hwTdmPsnMIBGroups, hwTdmPsnMIBTraps=hwTdmPsnMIBTraps, hwTdmPsnPerfCurrentGroup=hwTdmPsnPerfCurrentGroup, hwTdmPsnAlarmPwTypeIndex=hwTdmPsnAlarmPwTypeIndex, hwTdmPsnAlarmVcIfIndex=hwTdmPsnAlarmVcIfIndex, hwTdmPsnMIB=hwTdmPsnMIB, hwTdmPsnPerfCurrentMalformedPkts=hwTdmPsnPerfCurrentMalformedPkts, hwTdmPsnMIBCompliance=hwTdmPsnMIBCompliance, hwTdmPsnPerfCurrentTable=hwTdmPsnPerfCurrentTable, hwTdmPsnAlarmGroup=hwTdmPsnAlarmGroup, hwTdmPsnPerfCurrentSeverelyErrorSeconds=hwTdmPsnPerfCurrentSeverelyErrorSeconds, hwTdmPsnAlarmEntry=hwTdmPsnAlarmEntry, hwTdmPsnMIBConformance=hwTdmPsnMIBConformance, hwTdmPsnMIBCompliances=hwTdmPsnMIBCompliances, hwTdmPsnPerfCurrentPwIdIndex=hwTdmPsnPerfCurrentPwIdIndex, PYSNMP_MODULE_ID=hwTdmPsnMIB, hwTdmPsnNotificationGroup=hwTdmPsnNotificationGroup, hwTdmPsnAlarmTable=hwTdmPsnAlarmTable, hwTdmPsnAlarmPwIdIndex=hwTdmPsnAlarmPwIdIndex, hwTdmPsnMIBObjects=hwTdmPsnMIBObjects, hwTdmPsnPerfCurrentFailureCounts=hwTdmPsnPerfCurrentFailureCounts)
