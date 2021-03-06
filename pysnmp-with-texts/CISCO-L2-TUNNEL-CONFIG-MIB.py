#
# PySNMP MIB module CISCO-L2-TUNNEL-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L2-TUNNEL-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
QosLayer2Cos, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "QosLayer2Cos")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, IpAddress, TimeTicks, Bits, Gauge32, iso, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, MibIdentifier, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "TimeTicks", "Bits", "Gauge32", "iso", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "MibIdentifier", "NotificationType", "ModuleIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoL2TunnelConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 246))
ciscoL2TunnelConfigMIB.setRevisions(('2007-02-15 00:00', '2006-07-25 00:00', '2005-06-27 00:00', '2004-06-09 00:00', '2003-09-03 00:00', '2002-05-31 10:00', '2002-02-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2TunnelConfigMIB.setRevisionsDescriptions(("Modify the descriptions of cltcTunneledProtocolType and cltcTunnelShutdownThreshold. Add 'lldp(4)' to cltcTunneledProtocolType, 'lldp(6)' to cltcTunnelThresholdProtocolIndex and 'lldp(6)' to cltcTunneledProtocolIndex. Add new groups cltcTunnelTotalDropGroup, cltcTunnelSysDropNotifEnableGroup, cltcTunnelSysDropGroup, cltcTunnelSysDropNotifGroup.", 'Modify the descriptions of cltcTunneledProtocolType and cltcTunnelShutdownThreshold.', "Add 'eoam(3)' to cltcTunneledProtocolType, 'eoam(5)' to cltcTunnelThresholdProtocolIndex and 'eoam(5)' to cltcTunneledProtocolIndex.", 'Change the description for cltcTunnelThresholdProtocolIndex. Add the new groups cltcTunnelThresholdNotifsGroup and cltcNotifsEnableGroup.', 'Add a new object cltcTunnelDropStats. Remove the restriction for enabling cltcDot1qTunnelMode from the description.', 'Add SNMP support for 802.1q All Tagged (dot1q-all-tagged) Per Port feature. Dot1q-all-tagged feature is an enhancement to tag the packets on the native vlan to avoid any confusion in the ISP network, and to avoid vlan hopping when the native vlan for the trunk is as same as the vlan assigned for a customer. Before this enhancement, this feature can be enabled/disabled globally through the vlanTrunkPortsDot1qTag object in CISCO-VTP-MIB. With this enhacement, vlanTrunkPortsDot1qTag object in CISCO-VTP-MIB is deprecated and replaced by the dot1qAllTaggedEnabled object in this MIB. Additionally, dot1q-all-tag will be able to configure per port basis.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2TunnelConfigMIB.setLastUpdated('200702150000Z')
if mibBuilder.loadTexts: ciscoL2TunnelConfigMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoL2TunnelConfigMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2TunnelConfigMIB.setDescription('This MIB module is for layer 2 tunneling related configurations on a device. Tunneling allows separate local networks to be considered as a single VLAN. These separate networks are connected via an ISP, which will tunnel the packets from one network to another, making it appear as if the two networks are actually just one.')
cltcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 1))
cltcGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1))
cltcDot1qTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2))
cltcTunneledProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3))
cltcTunnelThreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4))
cltcTunnelStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5))
cltcDot1qAllTagged = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6))
cltcTunnelCos = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 1), QosLayer2Cos()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcTunnelCos.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelCos.setDescription('Specifies the user priority of the tunneled PDUs and applies to all ingress tunneling interfaces.')
cltcNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: cltcNotificationEnable.setDescription('This object indicates whether the system will generate the cltcTunnelDropThresholdExceeded and cltcTunnelShutdownThresholdExceeded notifications.')
cltcTunnelSysDropThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 3), Unsigned32()).setUnits('PDUs/sec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcTunnelSysDropThreshold.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelSysDropThreshold.setDescription('This object specifies the drop threshold at the system level. A value of zero indicates that system level rate limiting is disabled.')
cltcTunnelSysDropNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcTunnelSysDropNotifEnable.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelSysDropNotifEnable.setDescription('This object specifies whether the system will generate the cltcTunnelSysDropThresholdExceeded notification.')
cltcDot1qTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2, 1), )
if mibBuilder.loadTexts: cltcDot1qTunnelTable.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qTunnelTable.setDescription('This table contains information about the dot1q tunnel interfaces. Only dot1q tunneling capable interfaces are shown. 1Q-in-1Q will allow service providers to separate the traffic of various customers within their infrastructure while the customers appear to be on the same VLANs.')
cltcDot1qTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cltcDot1qTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qTunnelEntry.setDescription('Information about the dot1q tunnel. Only dot1q tunneling capable interfaces are shown.')
cltcDot1qTunnelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcDot1qTunnelMode.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qTunnelMode.setDescription("Indicates the dot1q tunnel mode of the interface. Setting the interface to dot1q tunnel 'disabled' mode causes the dot1q tunnel feature to be disabled on this interface. Setting the interface to dot1q tunnel 'enabled' mode causes the dot1q tunnel feature to be enabled on this interface.")
cltcTunneledProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3, 1), )
if mibBuilder.loadTexts: cltcTunneledProtocolTable.setStatus('current')
if mibBuilder.loadTexts: cltcTunneledProtocolTable.setDescription('This table contains information about the protocols being tunneled. Only tunneled protocol filtering capable interfaces are shown.')
cltcTunneledProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cltcTunneledProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: cltcTunneledProtocolEntry.setDescription('Information about the protocols being tunneled. Only tunneled protocol filtering capable interfaces are shown.')
cltcTunneledProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3, 1, 1, 1), Bits().clone(namedValues=NamedValues(("cdp", 0), ("vtp", 1), ("stp", 2), ("eoam", 3), ("lldp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcTunneledProtocolType.setStatus('current')
if mibBuilder.loadTexts: cltcTunneledProtocolType.setDescription("Indicates tunneled protocol of the interface. If a BIT is set, then the value of the corresponding protocol is tunneled. Specifically, if the 'cdp(0)' BIT is set, then the Cisco Discovery Protocol PDU is tunneled; if the 'vtp(1)' BIT is set, then the VLAN Trunking Protocol PDU is tunneled; if the 'stp(2)' BIT is set, then the Spanning Tree Protocol PDU is tunneled; if the 'eoam(3)' BIT is set, then the ethernet Operation, Administration and Maintenance PDU is tunneled; if the 'lldp(4)' BIT is set, then the Link Layer Discovery Protocol is tunneled. If the bit for a given protocol is set for an interface, then the statistics for that interface and protocol will start to be monitored.")
cltcTunnelThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1), )
if mibBuilder.loadTexts: cltcTunnelThresholdTable.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelThresholdTable.setDescription('This table contains information about the thresholds for protocol tunneling. Only tunneled protocol filtering capable interfaces are shown. The objects will be on a per interface, per protocol basis.')
cltcTunnelThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdProtocolIndex"))
if mibBuilder.loadTexts: cltcTunnelThresholdEntry.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelThresholdEntry.setDescription('Information about the thresholds for protocol tunneling. Only tunneled protocol filtering capable interfaces are shown. The entries will be on a per interface, per protocol basis')
cltcTunnelThresholdProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("all", 1), ("cdp", 2), ("vtp", 3), ("stp", 4), ("eoam", 5), ("lldp", 6))))
if mibBuilder.loadTexts: cltcTunnelThresholdProtocolIndex.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelThresholdProtocolIndex.setDescription('A tunneled protocol of an interface. - all(1) is supported for devices which allow the setting of thresholds on a per interface basis. This threshold is a combined threshold for the interface which includes all supported protocols. - cdp(2), vtp(3), stp(4), eoam(5) and lldp(6) are supported for devices which allow the setting of thresholds on a per interface, per protocol basis.')
cltcTunnelDropThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1, 2), Unsigned32()).setUnits('PDUs/sec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcTunnelDropThreshold.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelDropThreshold.setDescription('The drop threshold on an interface for a given protocol. After reaching this drop threshold, the interface will start dropping PDUs for the given protocol. This value cannot be greater than the value of cltcTunnelShutdownThreshold. A value of 0 indicates that no limit is set.')
cltcTunnelShutdownThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1, 3), Unsigned32()).setUnits('PDUs/sec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcTunnelShutdownThreshold.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelShutdownThreshold.setDescription('The shutdown threshold on an interface for a given protocol. After reaching the shutdown threshold, the interface will shutdown for the given protocol. This value cannot be less than the value of cltcTunnelDropThreshold. A value of 0 indicates that no limit is set.')
cltcTunnelStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1), )
if mibBuilder.loadTexts: cltcTunnelStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelStatisticsTable.setDescription('This table contains protocol tunneling statistics on the interface.')
cltcTunnelStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolIndex"))
if mibBuilder.loadTexts: cltcTunnelStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelStatisticsEntry.setDescription('Protocol tunneling statistics on the interface.')
cltcTunneledProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cdp", 2), ("vtp", 3), ("stp", 4), ("eoam", 5), ("lldp", 6))))
if mibBuilder.loadTexts: cltcTunneledProtocolIndex.setStatus('current')
if mibBuilder.loadTexts: cltcTunneledProtocolIndex.setDescription('A tunneled protocol of an interface.')
cltcTunnelEncapStats = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 2), Counter32()).setUnits('encapsulated PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cltcTunnelEncapStats.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelEncapStats.setDescription('The tunneled PDU encapsulation statistics of an interface. These statistics cover the number of tunneled ingress PDUs.')
cltcTunnelDeEncapStats = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 3), Counter32()).setUnits('de-encapsulated PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cltcTunnelDeEncapStats.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelDeEncapStats.setDescription('The tunneled PDU de-encapsulation statistics of an interface. These statistics cover the number of tunneled egress PDUs.')
cltcTunnelDropStats = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 4), Counter32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cltcTunnelDropStats.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelDropStats.setDescription('The number of PDUs dropped on an interface for a given protocol. The PDUs will be dropped when the cltcTunnelDropThreshold is reached.')
cltcTunnelDropStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 2), )
if mibBuilder.loadTexts: cltcTunnelDropStatTable.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelDropStatTable.setDescription('This table contains protocol tunneling drop statistics.')
cltcTunnelDropStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 2, 1), ).setIndexNames((0, "CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolIndex"))
if mibBuilder.loadTexts: cltcTunnelDropStatEntry.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelDropStatEntry.setDescription('Drop statistics for a tunneled protocol.')
cltcTunnelTotalDropStats = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 2, 1, 1), Counter32()).setUnits('encapsulated PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: cltcTunnelTotalDropStats.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelTotalDropStats.setDescription('The number of tunneled ingress PDUs that have been dropped.')
cltcDot1qAllTaggedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcDot1qAllTaggedEnabled.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qAllTaggedEnabled.setDescription('This object controls if dot1q-all-tagged feature is enabled in the managed system.')
cltcDot1qAllTaggedIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 2), )
if mibBuilder.loadTexts: cltcDot1qAllTaggedIfTable.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qAllTaggedIfTable.setDescription("This table contains information about the dot1q-all-tagged feature's configuration of capable interfaces in the system.")
cltcDot1qAllTaggedIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cltcDot1qAllTaggedIfEntry.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qAllTaggedIfEntry.setDescription('Configuration of dot1q-all-tagged feature on interfaces. Each entry is created for a dot1q-all-tagged capable interface in the system.')
cltcDot1qAllTaggedIfEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltcDot1qAllTaggedIfEnabled.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qAllTaggedIfEnabled.setDescription('This object specifies whether dot1q-all-tagged feature has been enabled on a specific interface.')
cltcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 2))
cltcMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0))
cltcTunnelDropThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0, 1)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropThreshold"))
if mibBuilder.loadTexts: cltcTunnelDropThresholdExceeded.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelDropThresholdExceeded.setDescription('This notification is generated when the cltcTunnelDropThreshold has been exceeded.')
cltcTunnelShutdownThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0, 2)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelShutdownThreshold"))
if mibBuilder.loadTexts: cltcTunnelShutdownThresholdExceeded.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelShutdownThresholdExceeded.setDescription('This notification is generated when the cltcTunnelShutdownThreshold has been exceeded.')
cltcTunnelSysDropThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0, 3)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropThreshold"))
if mibBuilder.loadTexts: cltcTunnelSysDropThresholdExceeded.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelSysDropThresholdExceeded.setDescription('This notification is generated when the cltcTunnelSysDropThreshold has been exceeded.')
cltcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 3))
cltcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1))
cltcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2))
cltcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 1)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qTunnelGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcMIBCompliance = cltcMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cltcMIBCompliance.setDescription('The compliance statement for the CISCO-L2-TUNNEL-CONFIG-MIB.')
cltcMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 2)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qTunnelGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelStatisticsGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcMIBCompliance2 = cltcMIBCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: cltcMIBCompliance2.setDescription('The compliance statement for the CISCO-L2-TUNNEL-CONFIG-MIB.')
cltcMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 3)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qTunnelGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelStatisticsGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcMIBCompliance3 = cltcMIBCompliance3.setStatus('deprecated')
if mibBuilder.loadTexts: cltcMIBCompliance3.setDescription('The compliance statement for the CISCO-L2-TUNNEL-CONFIG-MIB.')
cltcMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 4)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qTunnelGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelStatisticsGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropStatisticsGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcNotifsEnableGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcMIBCompliance4 = cltcMIBCompliance4.setStatus('deprecated')
if mibBuilder.loadTexts: cltcMIBCompliance4.setDescription('The compliance statement for the CISCO-L2-TUNNEL-CONFIG-MIB.')
cltcMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 5)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qTunnelGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelStatisticsGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropStatisticsGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelTotalDropGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcNotifsEnableGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdNotifsGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropNotifEnableGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropGroup"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcMIBCompliance5 = cltcMIBCompliance5.setStatus('current')
if mibBuilder.loadTexts: cltcMIBCompliance5.setDescription('The compliance statement for the CISCO-L2-TUNNEL-CONFIG-MIB.')
cltcDot1qTunnelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 1)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qTunnelMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcDot1qTunnelGroup = cltcDot1qTunnelGroup.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qTunnelGroup.setDescription('A collection of objects for configuring dot1q tunnneling.')
cltcTunneledProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 2)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolType"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelCos"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunneledProtocolGroup = cltcTunneledProtocolGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunneledProtocolGroup.setDescription('A collection of objects for configuring tunneled protocols.')
cltcTunnelThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 3)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropThreshold"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelShutdownThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelThresholdGroup = cltcTunnelThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelThresholdGroup.setDescription('A collection of objects for configuring the thresholds for protocol tunneling.')
cltcTunnelStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 4)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelEncapStats"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDeEncapStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelStatisticsGroup = cltcTunnelStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelStatisticsGroup.setDescription('A collection of objects which give the statistics regarding the tunneling interfaces.')
cltcDot1qAllTaggedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 5)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedEnabled"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedIfEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcDot1qAllTaggedGroup = cltcDot1qAllTaggedGroup.setStatus('current')
if mibBuilder.loadTexts: cltcDot1qAllTaggedGroup.setDescription('A collection of objects for configuring the dot1q-all-tagged feature in the system.')
cltcTunnelDropStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 6)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelDropStatisticsGroup = cltcTunnelDropStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelDropStatisticsGroup.setDescription('A collection of objects which give the statistics regarding dropped PDUs on the tunneling interfaces.')
cltcNotifsEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 7)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcNotifsEnableGroup = cltcNotifsEnableGroup.setStatus('current')
if mibBuilder.loadTexts: cltcNotifsEnableGroup.setDescription('A collections of objects used to enable notifications.')
cltcTunnelThresholdNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 8)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropThresholdExceeded"), ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelShutdownThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelThresholdNotifsGroup = cltcTunnelThresholdNotifsGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelThresholdNotifsGroup.setDescription('A collection of notifications used for the tunnel thresholds.')
cltcTunnelTotalDropGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 9)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelTotalDropStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelTotalDropGroup = cltcTunnelTotalDropGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelTotalDropGroup.setDescription('A collection of objects which give the statistics regarding total number of dropped PDUs per protocol type.')
cltcTunnelSysDropNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 10)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelSysDropNotifEnableGroup = cltcTunnelSysDropNotifEnableGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelSysDropNotifEnableGroup.setDescription('A collection of object to enable cltcTunnelSysDropThresholdExceeded notification.')
cltcTunnelSysDropGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 11)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelSysDropGroup = cltcTunnelSysDropGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelSysDropGroup.setDescription('A collection of object for configuring the system level rate limiting.')
cltcTunnelSysDropNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 12)).setObjects(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropThresholdExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cltcTunnelSysDropNotifGroup = cltcTunnelSysDropNotifGroup.setStatus('current')
if mibBuilder.loadTexts: cltcTunnelSysDropNotifGroup.setDescription('A collection of notification used for the system level rate limiting has been exceeded.')
mibBuilder.exportSymbols("CISCO-L2-TUNNEL-CONFIG-MIB", cltcTunnelShutdownThreshold=cltcTunnelShutdownThreshold, cltcNotifsEnableGroup=cltcNotifsEnableGroup, cltcMIBNotificationsPrefix=cltcMIBNotificationsPrefix, cltcTunnelDropStatisticsGroup=cltcTunnelDropStatisticsGroup, cltcTunnelDropThresholdExceeded=cltcTunnelDropThresholdExceeded, cltcMIBCompliance4=cltcMIBCompliance4, cltcTunnelDropStatTable=cltcTunnelDropStatTable, cltcMIBCompliance5=cltcMIBCompliance5, cltcTunneledProtocolGroup=cltcTunneledProtocolGroup, cltcDot1qAllTaggedIfEntry=cltcDot1qAllTaggedIfEntry, cltcTunnelTotalDropStats=cltcTunnelTotalDropStats, cltcTunnelThresholdTable=cltcTunnelThresholdTable, cltcTunneledProtocolTable=cltcTunneledProtocolTable, cltcTunnelThresholdProtocolIndex=cltcTunnelThresholdProtocolIndex, cltcDot1qTunnelEntry=cltcDot1qTunnelEntry, cltcTunnelDropStatEntry=cltcTunnelDropStatEntry, cltcTunnelThresholdEntry=cltcTunnelThresholdEntry, cltcDot1qTunnelGroup=cltcDot1qTunnelGroup, cltcTunnelSysDropNotifGroup=cltcTunnelSysDropNotifGroup, cltcTunnelSysDropNotifEnable=cltcTunnelSysDropNotifEnable, cltcMIBConformance=cltcMIBConformance, cltcTunnelDeEncapStats=cltcTunnelDeEncapStats, cltcNotificationEnable=cltcNotificationEnable, cltcTunnelStatisticsTable=cltcTunnelStatisticsTable, cltcDot1qTunnelMode=cltcDot1qTunnelMode, cltcTunnelSysDropThresholdExceeded=cltcTunnelSysDropThresholdExceeded, cltcTunneledProtocolEntry=cltcTunneledProtocolEntry, cltcDot1qAllTagged=cltcDot1qAllTagged, cltcGlobal=cltcGlobal, cltcTunnelSysDropGroup=cltcTunnelSysDropGroup, cltcDot1qTunnel=cltcDot1qTunnel, cltcTunnelTotalDropGroup=cltcTunnelTotalDropGroup, cltcMIBCompliance3=cltcMIBCompliance3, cltcMIBCompliance2=cltcMIBCompliance2, PYSNMP_MODULE_ID=ciscoL2TunnelConfigMIB, cltcDot1qAllTaggedIfTable=cltcDot1qAllTaggedIfTable, cltcDot1qTunnelTable=cltcDot1qTunnelTable, cltcMIBNotifications=cltcMIBNotifications, cltcMIBCompliance=cltcMIBCompliance, cltcDot1qAllTaggedGroup=cltcDot1qAllTaggedGroup, cltcTunnelThresholdGroup=cltcTunnelThresholdGroup, cltcTunnelDropStats=cltcTunnelDropStats, cltcTunnelSysDropNotifEnableGroup=cltcTunnelSysDropNotifEnableGroup, cltcTunnelThreshold=cltcTunnelThreshold, cltcTunnelStatisticsGroup=cltcTunnelStatisticsGroup, ciscoL2TunnelConfigMIB=ciscoL2TunnelConfigMIB, cltcTunneledProtocol=cltcTunneledProtocol, cltcTunneledProtocolType=cltcTunneledProtocolType, cltcTunnelSysDropThreshold=cltcTunnelSysDropThreshold, cltcTunnelStatisticsEntry=cltcTunnelStatisticsEntry, cltcDot1qAllTaggedEnabled=cltcDot1qAllTaggedEnabled, cltcMIBGroups=cltcMIBGroups, cltcTunnelThresholdNotifsGroup=cltcTunnelThresholdNotifsGroup, cltcDot1qAllTaggedIfEnabled=cltcDot1qAllTaggedIfEnabled, cltcTunnelEncapStats=cltcTunnelEncapStats, cltcTunneledProtocolIndex=cltcTunneledProtocolIndex, cltcTunnelShutdownThresholdExceeded=cltcTunnelShutdownThresholdExceeded, cltcMIBCompliances=cltcMIBCompliances, cltcTunnelDropThreshold=cltcTunnelDropThreshold, cltcTunnelStatistics=cltcTunnelStatistics, cltcMIBObjects=cltcMIBObjects, cltcTunnelCos=cltcTunnelCos)
