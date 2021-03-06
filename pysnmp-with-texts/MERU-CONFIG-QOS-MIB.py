#
# PySNMP MIB module MERU-CONFIG-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlQosRulesMatchClass, MwlQosAction, MwlQosCodec, MwlOnOffSwitch, MwlAdmissionControl, MwlQosCodecProtocol, MwlQosRulesMatchClassBits, MwlDscpType, MwlQosProtocol, MwlDropPolicy = mibBuilder.importSymbols("MERU-TC", "MwlQosRulesMatchClass", "MwlQosAction", "MwlQosCodec", "MwlOnOffSwitch", "MwlAdmissionControl", "MwlQosCodecProtocol", "MwlQosRulesMatchClassBits", "MwlDscpType", "MwlQosProtocol", "MwlDropPolicy")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, TimeTicks, NotificationType, MibIdentifier, ObjectIdentity, iso, Counter32, Unsigned32, Gauge32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "TimeTicks", "NotificationType", "MibIdentifier", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "Integer32")
TimeStamp, TruthValue, MacAddress, DateAndTime, TextualConvention, RowStatus, TimeInterval, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "MacAddress", "DateAndTime", "TextualConvention", "RowStatus", "TimeInterval", "DisplayString")
mwConfigQoS = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8))
if mibBuilder.loadTexts: mwConfigQoS.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigQoS.setOrganization('Meru Networks')
if mibBuilder.loadTexts: mwConfigQoS.setContactInfo('support@merunetworks.com')
if mibBuilder.loadTexts: mwConfigQoS.setDescription('This MIB defines all the managed objects used to manage the Meru WLAN Quality-of-Service Configuration infrastructure')
mwQosVars = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1))
mwQosVarsQosOnOff = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 1), MwlOnOffSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosOnOff.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosOnOff.setDescription('This object describes On/Off')
mwQosVarsQosAdmissionControl = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 2), MwlAdmissionControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosAdmissionControl.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosAdmissionControl.setDescription('This object describes Admission Control')
mwQosVarsQosDropPolicy = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 3), MwlDropPolicy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosDropPolicy.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosDropPolicy.setDescription('This object describes Drop Policy')
mwQosVarsQosDefaultTimeToLive = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosDefaultTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosDefaultTimeToLive.setDescription('This object describes Default Time-to-live (seconds)')
mwQosVarsQosUdpTimeToLive = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosUdpTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosUdpTimeToLive.setDescription('This object describes UDP Time-to-live (seconds)')
mwQosVarsQosTcpTimeToLive = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosTcpTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosTcpTimeToLive.setDescription('This object describes TCP Time-to-live (seconds)')
mwQosVarsPercentBWScaling = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsPercentBWScaling.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsPercentBWScaling.setDescription('This object describes Bandwidth Scaling (percent)')
mwQosVarsQosMaxCallsPerAp = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerAp.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerAp.setDescription('This object describes Maximum Calls Per AP')
mwQosVarsQosMaxCallsPerInterfRegion = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerInterfRegion.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerInterfRegion.setDescription('This object describes Maximum Calls Per Interference Region')
mwQosVarsQosLoadBalanceMaxStationsPerAp = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceMaxStationsPerAp.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceMaxStationsPerAp.setDescription('This object describes Maximum Stations Per Radio')
mwQosVarsQosLoadBalanceMaxStationsPerBssid = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceMaxStationsPerBssid.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceMaxStationsPerBssid.setDescription('This object describes Maximum Stations Per BSSID')
mwQosVarsQosLoadBalanceOverflow = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 12), MwlOnOffSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceOverflow.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosLoadBalanceOverflow.setDescription('This object describes Load Balance Overflow')
mwQosVarsQosMaxCallsPerBssid = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 13), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerBssid.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosMaxCallsPerBssid.setDescription('This object describes Maximum Calls Per BSSID')
mwQosVarsQosCacDeauth = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 14), MwlOnOffSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosCacDeauth.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosCacDeauth.setDescription('This object describes CAC Deauth')
mwQosVarsQosStationAssignAge = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 15), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosStationAssignAge.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosStationAssignAge.setDescription('This object describes Station Assignment Aging Time (seconds)')
mwQosVarsQosSipIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 16), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwQosVarsQosSipIdleTimeout.setStatus('current')
if mibBuilder.loadTexts: mwQosVarsQosSipIdleTimeout.setDescription('This object describes SIP Idle Timeout (seconds)')
mwQosRuleTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2), )
if mibBuilder.loadTexts: mwQosRuleTable.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleTable.setDescription('This object describes QoS and Firewall Rules ')
mwQosRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1), ).setIndexNames((0, "MERU-CONFIG-QOS-MIB", "mwQosRuleTableIndex"))
if mibBuilder.loadTexts: mwQosRuleEntry.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleEntry.setDescription('This object describes QoS and Firewall Rules ')
mwQosRuleTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mwQosRuleTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleTableIndex.setDescription('The index value of the table ')
mwQosRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleId.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleId.setDescription('This object describes ID')
mwQosRuleDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 3), MwlDscpType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDscp.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDscp.setDescription('This object describes DiffServ Codepoint')
mwQosRuleDstIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstIp.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDstIp.setDescription('This object describes Destination IP')
mwQosRuleSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcIp.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleSrcIp.setDescription('This object describes Source IP')
mwQosRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 6), MwlQosAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleAction.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleAction.setDescription('This object describes Action')
mwQosRuleDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstMask.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDstMask.setDescription('This object describes Destination Netmask')
mwQosRuleDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstPort.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDstPort.setDescription('This object describes Destination Port')
mwQosRuleSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcMask.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleSrcMask.setDescription('This object describes Source Netmask')
mwQosRuleSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcPort.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleSrcPort.setDescription('This object describes Source Port')
mwQosRuleProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 11), MwlQosProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleProtocol.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleProtocol.setDescription('This object describes QoS Protocol')
mwQosRulePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePriority.setStatus('current')
if mibBuilder.loadTexts: mwQosRulePriority.setDescription('This object describes Priority')
mwQosRuleIdUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 13), MwlQosRulesMatchClass()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleIdUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleIdUfcFlag.setDescription('This object describes Id Class flow class')
mwQosRuleDstIpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 14), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstIpFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDstIpFlag.setDescription('This object describes Destination IP match')
mwQosRuleSrcIpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 15), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcIpFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleSrcIpFlag.setDescription('This object describes Source IP match')
mwQosRuleL4Protocol = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleL4Protocol.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleL4Protocol.setDescription('This object describes Network Protocol')
mwQosRuleDstPortFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 18), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstPortFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDstPortFlag.setDescription('This object describes Destination Port match')
mwQosRuleSrcPortFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 19), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcPortFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleSrcPortFlag.setDescription('This object describes Source Port match')
mwQosRuleDstIpUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 20), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstIpUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDstIpUfcFlag.setDescription('This object describes Destination IP flow class')
mwQosRuleSrcIpUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 21), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcIpUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleSrcIpUfcFlag.setDescription('This object describes Source IP flow class')
mwQosRuleAvgPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 22), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleAvgPacketRate.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleAvgPacketRate.setDescription('This object describes Average Packet Rate')
mwQosRuleDstPortUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 23), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleDstPortUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleDstPortUfcFlag.setDescription('This object describes Destination Port flow class')
mwQosRuleSrcPortUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 24), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleSrcPortUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleSrcPortUfcFlag.setDescription('This object describes Source Port flow class')
mwQosRuleL4ProtocolFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 25), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleL4ProtocolFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleL4ProtocolFlag.setDescription('This object describes Network Protocol match')
mwQosRuleTrafficControl = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 26), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleTrafficControl.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleTrafficControl.setDescription('This object describes Traffic Control')
mwQosRuleLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 27), MwlOnOffSwitch()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleLogging.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleLogging.setDescription('This object describes Qos Rule Logging')
mwQosRulePacketMinLength = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 28), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMinLength.setStatus('current')
if mibBuilder.loadTexts: mwQosRulePacketMinLength.setDescription('This object describes Packet minimum length')
mwQosRulePacketMaxLength = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 29), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMaxLength.setStatus('current')
if mibBuilder.loadTexts: mwQosRulePacketMaxLength.setDescription('This object describes Packet maximum length')
mwQosRuleTokenBucketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 30), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleTokenBucketRate.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleTokenBucketRate.setDescription('This object describes Token Bucket Rate')
mwQosRuleFirewallFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleFirewallFilterId.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleFirewallFilterId.setDescription('This object describes Firewall Filter ID')
mwQosRuleL4ProtocolUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 32), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleL4ProtocolUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleL4ProtocolUfcFlag.setDescription('This object describes Network Protocol flow class')
mwQosRulePacketMinLengthFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 33), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMinLengthFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRulePacketMinLengthFlag.setDescription('This object describes Packet Length match')
mwQosRuleFirewallFilterIdFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 34), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleFirewallFilterIdFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleFirewallFilterIdFlag.setDescription('This object describes Filter Id match')
mwQosRulePacketMinLengthUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 35), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRulePacketMinLengthUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRulePacketMinLengthUfcFlag.setDescription('This object describes Packet Length flow class')
mwQosRuleFirewallFilterIdUfcFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 36), MwlQosRulesMatchClassBits()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleFirewallFilterIdUfcFlag.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleFirewallFilterIdUfcFlag.setDescription('This object describes Filter Id Flow Class')
mwQosRuleLoggingFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 37), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleLoggingFrequency.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleLoggingFrequency.setDescription('This object describes Qos Rule Logging Frequency')
mwQosRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 40), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: mwQosRuleRowStatus.setDescription('This object is used to create and delete rows in the table')
mwQosCodecTranslRuleTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3), )
if mibBuilder.loadTexts: mwQosCodecTranslRuleTable.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleTable.setDescription('This object describes QoS Codec Rules ')
mwQosCodecTranslRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1), ).setIndexNames((0, "MERU-CONFIG-QOS-MIB", "mwQosCodecTranslRuleTableIndex"))
if mibBuilder.loadTexts: mwQosCodecTranslRuleEntry.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleEntry.setDescription('This object describes QoS Codec Rules ')
mwQosCodecTranslRuleTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: mwQosCodecTranslRuleTableIndex.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleTableIndex.setDescription('The index value of the table ')
mwQosCodecTranslRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleId.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleId.setDescription('This object describes ID')
mwQosCodecTranslRuleQosCtrProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 3), MwlQosCodecProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrProtocol.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrProtocol.setDescription('This object describes QoS Protocol')
mwQosCodecTranslRuleQosCtrCodecEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 4), MwlQosCodec()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrCodecEnum.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrCodecEnum.setDescription('This object describes Codec')
mwQosCodecTranslRuleQosCtrRspecRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrRspecRate.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrRspecRate.setDescription('This object describes Reservation Rate (0-1,000,000 bytes/second)')
mwQosCodecTranslRuleQosCtrRspecSlack = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrRspecSlack.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrRspecSlack.setDescription('This object describes Reservation Slack (0-1,000,000 microseconds)')
mwQosCodecTranslRuleQosCtrSampleRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrSampleRate.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrSampleRate.setDescription('This object describes Packet Rate (0-200 packets/second)')
mwQosCodecTranslRuleQosCtrTspecPeakRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecPeakRate.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecPeakRate.setDescription('This object describes Peak Rate (0-1,000,000 bytes/second)')
mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit.setDescription('This object describes Minimum Policed Unit (0-1,500 bytes)')
mwQosCodecTranslRuleQosCtrTspecTokenBucketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecTokenBucketRate.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecTokenBucketRate.setDescription('This object describes Token Bucket Rate (0-1,000,000 bytes/second)')
mwQosCodecTranslRuleQosCtrTspecTokenBucketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecTokenBucketSize.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecTokenBucketSize.setDescription('This object describes Token Bucket Size (0-16,000 bytes)')
mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 12), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize.setDescription('This object describes Maximum Packet Size (0-1,500 bytes)')
mwQosCodecTranslRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwQosCodecTranslRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: mwQosCodecTranslRuleRowStatus.setDescription('This object is used to create and delete rows in the table')
mibBuilder.exportSymbols("MERU-CONFIG-QOS-MIB", mwQosVarsQosOnOff=mwQosVarsQosOnOff, mwQosRuleRowStatus=mwQosRuleRowStatus, mwQosRuleDstIp=mwQosRuleDstIp, mwQosCodecTranslRuleQosCtrRspecRate=mwQosCodecTranslRuleQosCtrRspecRate, mwQosRuleTrafficControl=mwQosRuleTrafficControl, mwQosRuleTableIndex=mwQosRuleTableIndex, mwQosRuleLogging=mwQosRuleLogging, mwQosRuleDstPort=mwQosRuleDstPort, mwQosCodecTranslRuleQosCtrTspecPeakRate=mwQosCodecTranslRuleQosCtrTspecPeakRate, mwQosCodecTranslRuleQosCtrTspecTokenBucketSize=mwQosCodecTranslRuleQosCtrTspecTokenBucketSize, mwQosVarsQosMaxCallsPerInterfRegion=mwQosVarsQosMaxCallsPerInterfRegion, mwQosRuleSrcIp=mwQosRuleSrcIp, mwQosRuleL4ProtocolFlag=mwQosRuleL4ProtocolFlag, mwQosVarsQosStationAssignAge=mwQosVarsQosStationAssignAge, mwQosVarsQosLoadBalanceOverflow=mwQosVarsQosLoadBalanceOverflow, mwQosRuleProtocol=mwQosRuleProtocol, mwQosRuleDstIpUfcFlag=mwQosRuleDstIpUfcFlag, mwQosRuleAvgPacketRate=mwQosRuleAvgPacketRate, mwQosCodecTranslRuleQosCtrRspecSlack=mwQosCodecTranslRuleQosCtrRspecSlack, mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit=mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit, mwQosVarsQosAdmissionControl=mwQosVarsQosAdmissionControl, mwQosVarsQosMaxCallsPerAp=mwQosVarsQosMaxCallsPerAp, mwQosRuleFirewallFilterId=mwQosRuleFirewallFilterId, mwQosCodecTranslRuleTable=mwQosCodecTranslRuleTable, mwQosVarsQosDropPolicy=mwQosVarsQosDropPolicy, mwQosRulePacketMinLengthFlag=mwQosRulePacketMinLengthFlag, mwQosCodecTranslRuleQosCtrCodecEnum=mwQosCodecTranslRuleQosCtrCodecEnum, mwQosVarsQosDefaultTimeToLive=mwQosVarsQosDefaultTimeToLive, mwQosRuleSrcPortFlag=mwQosRuleSrcPortFlag, mwQosVarsPercentBWScaling=mwQosVarsPercentBWScaling, mwQosRuleSrcMask=mwQosRuleSrcMask, mwQosRulePacketMaxLength=mwQosRulePacketMaxLength, mwQosRulePacketMinLength=mwQosRulePacketMinLength, mwQosCodecTranslRuleEntry=mwQosCodecTranslRuleEntry, mwConfigQoS=mwConfigQoS, mwQosRulePriority=mwQosRulePriority, mwQosVarsQosMaxCallsPerBssid=mwQosVarsQosMaxCallsPerBssid, mwQosRuleSrcPortUfcFlag=mwQosRuleSrcPortUfcFlag, mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize=mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize, mwQosRuleAction=mwQosRuleAction, mwQosRuleFirewallFilterIdFlag=mwQosRuleFirewallFilterIdFlag, mwQosRuleDstPortUfcFlag=mwQosRuleDstPortUfcFlag, mwQosRuleDstPortFlag=mwQosRuleDstPortFlag, mwQosRuleDstIpFlag=mwQosRuleDstIpFlag, mwQosRuleL4ProtocolUfcFlag=mwQosRuleL4ProtocolUfcFlag, mwQosCodecTranslRuleTableIndex=mwQosCodecTranslRuleTableIndex, mwQosVarsQosUdpTimeToLive=mwQosVarsQosUdpTimeToLive, mwQosRuleTable=mwQosRuleTable, mwQosVarsQosCacDeauth=mwQosVarsQosCacDeauth, mwQosRuleId=mwQosRuleId, PYSNMP_MODULE_ID=mwConfigQoS, mwQosRuleDscp=mwQosRuleDscp, mwQosRuleDstMask=mwQosRuleDstMask, mwQosVarsQosLoadBalanceMaxStationsPerAp=mwQosVarsQosLoadBalanceMaxStationsPerAp, mwQosRuleSrcPort=mwQosRuleSrcPort, mwQosRuleIdUfcFlag=mwQosRuleIdUfcFlag, mwQosVarsQosSipIdleTimeout=mwQosVarsQosSipIdleTimeout, mwQosRuleSrcIpUfcFlag=mwQosRuleSrcIpUfcFlag, mwQosRulePacketMinLengthUfcFlag=mwQosRulePacketMinLengthUfcFlag, mwQosRuleL4Protocol=mwQosRuleL4Protocol, mwQosRuleEntry=mwQosRuleEntry, mwQosRuleFirewallFilterIdUfcFlag=mwQosRuleFirewallFilterIdUfcFlag, mwQosCodecTranslRuleId=mwQosCodecTranslRuleId, mwQosVarsQosTcpTimeToLive=mwQosVarsQosTcpTimeToLive, mwQosVarsQosLoadBalanceMaxStationsPerBssid=mwQosVarsQosLoadBalanceMaxStationsPerBssid, mwQosCodecTranslRuleQosCtrSampleRate=mwQosCodecTranslRuleQosCtrSampleRate, mwQosCodecTranslRuleRowStatus=mwQosCodecTranslRuleRowStatus, mwQosCodecTranslRuleQosCtrTspecTokenBucketRate=mwQosCodecTranslRuleQosCtrTspecTokenBucketRate, mwQosRuleSrcIpFlag=mwQosRuleSrcIpFlag, mwQosVars=mwQosVars, mwQosRuleLoggingFrequency=mwQosRuleLoggingFrequency, mwQosRuleTokenBucketRate=mwQosRuleTokenBucketRate, mwQosCodecTranslRuleQosCtrProtocol=mwQosCodecTranslRuleQosCtrProtocol)
