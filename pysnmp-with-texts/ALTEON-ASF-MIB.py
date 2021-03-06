#
# PySNMP MIB module ALTEON-ASF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTEON-ASF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:20:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
firewall, = mibBuilder.importSymbols("ALTEON-ROOT-MIB", "firewall")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, MibIdentifier, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ModuleIdentity, Integer32, TimeTicks, Counter64, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ModuleIdentity", "Integer32", "TimeTicks", "Counter64", "IpAddress", "NotificationType")
TextualConvention, TruthValue, MacAddress, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "MacAddress", "TimeStamp", "DisplayString")
alteonAsfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1))
alteonAsfMIB.setRevisions(('1902-03-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alteonAsfMIB.setRevisionsDescriptions(('Added port statistics and iSD session statistics.',))
if mibBuilder.loadTexts: alteonAsfMIB.setLastUpdated('0203140000Z')
if mibBuilder.loadTexts: alteonAsfMIB.setOrganization('Alteon WebSystems')
if mibBuilder.loadTexts: alteonAsfMIB.setContactInfo(' ')
if mibBuilder.loadTexts: alteonAsfMIB.setDescription('MIB for Alteon Switched Firewall.')
asfStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9))
if mibBuilder.loadTexts: asfStatistics.setStatus('current')
if mibBuilder.loadTexts: asfStatistics.setDescription('Objects under this branch provide statistics.')
asfNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12))
if mibBuilder.loadTexts: asfNotifications.setStatus('current')
if mibBuilder.loadTexts: asfNotifications.setDescription('This group lists various notifications sent by the ASF system when it encounters defined exceptional conditions.')
asfEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1))
if mibBuilder.loadTexts: asfEvents.setStatus('current')
if mibBuilder.loadTexts: asfEvents.setDescription('This group lists events generated by iSDs in the cluster.')
asfAlarms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2))
if mibBuilder.loadTexts: asfAlarms.setStatus('current')
if mibBuilder.loadTexts: asfAlarms.setDescription('This group lists alarms generates by iSDs in the cluster. An alarm is a special form of event which represents a fault in the system that needs to be reported.')
asfNotificationObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13))
if mibBuilder.loadTexts: asfNotificationObjs.setStatus('current')
if mibBuilder.loadTexts: asfNotificationObjs.setDescription('This branch consists of objects used to model traps sent to the management station.')
deviceIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: deviceIpAddress.setStatus('current')
if mibBuilder.loadTexts: deviceIpAddress.setDescription('The IP address of the iSD/accelerator emitting the notification.')
deviceTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 2), TimeStamp()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: deviceTimeStamp.setStatus('current')
if mibBuilder.loadTexts: deviceTimeStamp.setDescription('The value of the sysUpTime object (which defines when a specific occurrence happened).')
infoString = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: infoString.setStatus('current')
if mibBuilder.loadTexts: infoString.setDescription('When applicable, a brief description about the notification.')
memoryUsed = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: memoryUsed.setStatus('current')
if mibBuilder.loadTexts: memoryUsed.setDescription("The amount of disk space or memory consumed by the hard disk/RAM. This value can be absolute or a percentage of total (determined by 'memoryUsageType'). If the memoryUsageType is 'absolute' (1) then the value of this object is defined by the unit specified by the memoryUsageUnit.")
memoryUsageType = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absolute", 1), ("percentage", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: memoryUsageType.setStatus('current')
if mibBuilder.loadTexts: memoryUsageType.setDescription("The type of the value contained in 'memoryUsed' (which can be an 'absolute' value or a 'percentage' of the total value).")
memoryUsageUnit = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("kb", 1), ("mb", 2), ("gb", 3), ("none", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: memoryUsageUnit.setStatus('current')
if mibBuilder.loadTexts: memoryUsageUnit.setDescription("The unit of measurement for the value contained in 'memoryUsed'. If the value of 'memoryUsageType' is 'absolute', then this object will have one of the first three values. If the value of 'memoryUsageType' contains 'percentage', then this object will have the value of 'none'.")
alarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmSeverity.setDescription('These provide an indication of how the capability of the iSD/Switch has been affected. These severity levels, which represent service affecting conditions, are ordered from most severe to least severe (ss defined in X.733 standard).')
deviceMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 8), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: deviceMACAddress.setStatus('current')
if mibBuilder.loadTexts: deviceMACAddress.setDescription('The MAC address of the iSD/switch emitting the notification.')
asfAcceleratorAddedTrap = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 1)).setObjects(("ALTEON-ASF-MIB", "deviceMACAddress"))
if mibBuilder.loadTexts: asfAcceleratorAddedTrap.setStatus('current')
if mibBuilder.loadTexts: asfAcceleratorAddedTrap.setDescription('Trap sent when an accelerator is added to the cluster.')
asfAcceleratorRemovedTrap = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 2)).setObjects(("ALTEON-ASF-MIB", "deviceMACAddress"))
if mibBuilder.loadTexts: asfAcceleratorRemovedTrap.setStatus('current')
if mibBuilder.loadTexts: asfAcceleratorRemovedTrap.setDescription('Trap sent when an accelerator is removed from the cluster.')
asfExtraAcceleratorDetected = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 3)).setObjects(("ALTEON-ASF-MIB", "deviceMACAddress"))
if mibBuilder.loadTexts: asfExtraAcceleratorDetected.setStatus('current')
if mibBuilder.loadTexts: asfExtraAcceleratorDetected.setDescription('Trap sent when an extra accelerator is detected in the cluster. This trap contains the MAC address of the extra accelerator.')
asfAcceleratorConnEstablished = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 4)).setObjects(("ALTEON-ASF-MIB", "deviceMACAddress"))
if mibBuilder.loadTexts: asfAcceleratorConnEstablished.setStatus('current')
if mibBuilder.loadTexts: asfAcceleratorConnEstablished.setDescription('Trap sent when a connection has been established with the accelerator. This trap contains the MAC address of the accelerator.')
asfConfigUpdateSuccess = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 8)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"), ("ALTEON-ASF-MIB", "deviceMACAddress"))
if mibBuilder.loadTexts: asfConfigUpdateSuccess.setStatus('current')
if mibBuilder.loadTexts: asfConfigUpdateSuccess.setDescription('Informative trap sent conveying that the configuration update request is successfully completed. This trap sends the IP address and MAC address of the device whose update succeeded.')
asfConfigUpdateFail = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 9)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"), ("ALTEON-ASF-MIB", "deviceMACAddress"))
if mibBuilder.loadTexts: asfConfigUpdateFail.setStatus('current')
if mibBuilder.loadTexts: asfConfigUpdateFail.setDescription('Informative trap sent conveying that the configuration update request failed. This trap sends the IP address and MAC address of the device whose update failed.')
asfFirewallStarted = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 10)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"))
if mibBuilder.loadTexts: asfFirewallStarted.setStatus('current')
if mibBuilder.loadTexts: asfFirewallStarted.setDescription('Trap sent when the firewall has started running. This trap contains the IP address of relevant iSD.')
asfIsdFirewallFail = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 1)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"))
if mibBuilder.loadTexts: asfIsdFirewallFail.setStatus('current')
if mibBuilder.loadTexts: asfIsdFirewallFail.setDescription('Trap sent when the firewall on one of the iSDs in the cluster is stopped. This trap contains the IP address of the affected iSD.')
asfWebServerFail = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 2)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"))
if mibBuilder.loadTexts: asfWebServerFail.setStatus('current')
if mibBuilder.loadTexts: asfWebServerFail.setDescription('Trap sent when webserver is stopped. This trap contains the IP address of the affected iSD.')
asfWebServerStart = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 3)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"))
if mibBuilder.loadTexts: asfWebServerStart.setStatus('current')
if mibBuilder.loadTexts: asfWebServerStart.setDescription('Trap sent when webserver is started after failing. This trap contains the IP address of the affected iSD.')
asfFileSystemWarning = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 5)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"), ("ALTEON-ASF-MIB", "infoString"), ("ALTEON-ASF-MIB", "memoryUsed"))
if mibBuilder.loadTexts: asfFileSystemWarning.setStatus('current')
if mibBuilder.loadTexts: asfFileSystemWarning.setDescription('Trap sent when file system usage crosses 75% level. For example, if level crosses 75% for 1 GB hard disk on iSD with IP address 123.45.67.89, then a trap is sent when usage of hard disk is reaches 750 MB. The following objects will be in the trap: 123.45.67.89, bytes (used), bytes (available).')
asfFileSystemCritical = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 6)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"), ("ALTEON-ASF-MIB", "infoString"), ("ALTEON-ASF-MIB", "memoryUsed"))
if mibBuilder.loadTexts: asfFileSystemCritical.setStatus('current')
if mibBuilder.loadTexts: asfFileSystemCritical.setDescription('Trap sent when file system usage crosses 90% level. For example, if level crosses 90% for 1 GB hard disk on iSD with IP address 123.45.67.89, then a trap is sent when usage of hard disk reaches 900 MB. The following objects will be in the trap: 123.45.67.89, bytes (used), bytes (available).')
asfMemoryWarning = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 7)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"), ("ALTEON-ASF-MIB", "memoryUsed"))
if mibBuilder.loadTexts: asfMemoryWarning.setStatus('current')
if mibBuilder.loadTexts: asfMemoryWarning.setDescription('Trap sent when memory usage crosses 75% level. The following objects will be in the trap: iSD IP address, 75% used, % memory available.')
asfMemoryCritical = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 8)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"), ("ALTEON-ASF-MIB", "memoryUsed"))
if mibBuilder.loadTexts: asfMemoryCritical.setStatus('current')
if mibBuilder.loadTexts: asfMemoryCritical.setDescription('Trap sent when memory usage crosses 90% level. The following objects will be in the trap: iSD IP address, 90% used, % memory available.')
asfIsdStateDown = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 9)).setObjects(("ALTEON-ASF-MIB", "deviceIpAddress"))
if mibBuilder.loadTexts: asfIsdStateDown.setStatus('current')
if mibBuilder.loadTexts: asfIsdStateDown.setDescription("Trap sent when the iSD's state is down. This trap contains the IP address of the affected iSD.")
asfPortStats = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1))
if mibBuilder.loadTexts: asfPortStats.setStatus('current')
if mibBuilder.loadTexts: asfPortStats.setDescription('This group contains the byteCount and packet count statistics per port.')
asfPortNetStatsTime = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortNetStatsTime.setStatus('current')
if mibBuilder.loadTexts: asfPortNetStatsTime.setDescription('The current time at the accelerator.')
asfPortNetStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2), )
if mibBuilder.loadTexts: asfPortNetStatsTable.setStatus('current')
if mibBuilder.loadTexts: asfPortNetStatsTable.setDescription('Each row in the table gives the information about an individual port.')
asfPortNetStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1), ).setIndexNames((0, "ALTEON-ASF-MIB", "asfPortCountIndex"))
if mibBuilder.loadTexts: asfPortNetStatsEntry.setStatus('current')
if mibBuilder.loadTexts: asfPortNetStatsEntry.setDescription('The isd information about the row selected.')
asfPortCountIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortCountIndex.setStatus('current')
if mibBuilder.loadTexts: asfPortCountIndex.setDescription('The index of the portStatsTable which specifies the individual port.')
asfPortInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInBytes.setStatus('current')
if mibBuilder.loadTexts: asfPortInBytes.setDescription('The number of bytes ingressing the port.')
asfPortOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortOutBytes.setStatus('current')
if mibBuilder.loadTexts: asfPortOutBytes.setDescription('The number of bytes egressing the port.')
asfPortInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortInPackets.setDescription('The number of packets ingressing the port. This is the sum of ingressing unicast, broadcast, multicast, discarded, unknown, and error packets.')
asfPortOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortOutPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortOutPackets.setDescription('The number of packets egressing the port. This is the sum of egressing unicast, broadcast, multicast, discarded, and unknown packets.')
asfPortInUcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInUcastPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortInUcastPackets.setDescription('The number of unicast packets ingressing the port.')
asfPortOutUcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortOutUcastPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortOutUcastPackets.setDescription('The number of unicast packets egressing the port.')
asfPortInBcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInBcastPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortInBcastPackets.setDescription('The number of broadcast packets ingressing the port.')
asfPortOutBcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortOutBcastPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortOutBcastPackets.setDescription('The number of broadcast packets egressing the port.')
asfPortInMcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInMcastPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortInMcastPackets.setDescription('The number of multicast packets ingressing the port.')
asfPortOutMcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortOutMcastPackets.setStatus('current')
if mibBuilder.loadTexts: asfPortOutMcastPackets.setDescription('The number of multicast packets egressing the port.')
asfPortInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInDiscards.setStatus('current')
if mibBuilder.loadTexts: asfPortInDiscards.setDescription('The number of ingressing packets discarded.')
asfPortOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortOutDiscards.setStatus('current')
if mibBuilder.loadTexts: asfPortOutDiscards.setDescription('The number of egressing packets discarded.')
asfPortInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInErrors.setStatus('current')
if mibBuilder.loadTexts: asfPortInErrors.setDescription('The number of ingressing packets with errors.')
asfPortOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortOutErrors.setStatus('current')
if mibBuilder.loadTexts: asfPortOutErrors.setDescription('The number of egressing packets with errors.')
asfPortInUnknowns = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfPortInUnknowns.setStatus('current')
if mibBuilder.loadTexts: asfPortInUnknowns.setDescription('The number of unknown ingressing packets.')
asfIsdStats = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2))
if mibBuilder.loadTexts: asfIsdStats.setStatus('current')
if mibBuilder.loadTexts: asfIsdStats.setDescription('This group contains the session count statistics per isd.')
asfIsdSessStatsTime = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfIsdSessStatsTime.setStatus('current')
if mibBuilder.loadTexts: asfIsdSessStatsTime.setDescription('The current time at the accelerator.')
asfIsdSessStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2), )
if mibBuilder.loadTexts: asfIsdSessStatsTable.setStatus('current')
if mibBuilder.loadTexts: asfIsdSessStatsTable.setDescription('Each row in the table gives the information about the session count on the isd which is per isd .')
asfIsdSessStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1), ).setIndexNames((0, "ALTEON-ASF-MIB", "asfIsdCountIndex"))
if mibBuilder.loadTexts: asfIsdSessStatsEntry.setStatus('current')
if mibBuilder.loadTexts: asfIsdSessStatsEntry.setDescription('The isd information about the row selected.')
asfIsdCountIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfIsdCountIndex.setStatus('current')
if mibBuilder.loadTexts: asfIsdCountIndex.setDescription('The index of the isdStatsTable which specifies the isd.')
asfIsdIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfIsdIPAddress.setStatus('current')
if mibBuilder.loadTexts: asfIsdIPAddress.setDescription('The IP address of the isd.')
asfNoOfSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asfNoOfSessions.setStatus('current')
if mibBuilder.loadTexts: asfNoOfSessions.setDescription('The number of sessions on this isd.')
mibBuilder.exportSymbols("ALTEON-ASF-MIB", alarmSeverity=alarmSeverity, asfPortOutMcastPackets=asfPortOutMcastPackets, memoryUsed=memoryUsed, asfMemoryCritical=asfMemoryCritical, deviceTimeStamp=deviceTimeStamp, memoryUsageType=memoryUsageType, asfWebServerStart=asfWebServerStart, asfPortOutErrors=asfPortOutErrors, asfIsdStats=asfIsdStats, asfIsdSessStatsTime=asfIsdSessStatsTime, asfPortOutDiscards=asfPortOutDiscards, asfStatistics=asfStatistics, asfIsdStateDown=asfIsdStateDown, asfPortInBcastPackets=asfPortInBcastPackets, alteonAsfMIB=alteonAsfMIB, deviceIpAddress=deviceIpAddress, PYSNMP_MODULE_ID=alteonAsfMIB, asfAlarms=asfAlarms, deviceMACAddress=deviceMACAddress, asfEvents=asfEvents, asfIsdFirewallFail=asfIsdFirewallFail, asfWebServerFail=asfWebServerFail, asfPortInUcastPackets=asfPortInUcastPackets, asfPortInDiscards=asfPortInDiscards, asfIsdIPAddress=asfIsdIPAddress, asfPortStats=asfPortStats, asfPortInBytes=asfPortInBytes, asfPortNetStatsTime=asfPortNetStatsTime, asfPortOutUcastPackets=asfPortOutUcastPackets, asfMemoryWarning=asfMemoryWarning, asfAcceleratorConnEstablished=asfAcceleratorConnEstablished, asfPortOutBytes=asfPortOutBytes, asfExtraAcceleratorDetected=asfExtraAcceleratorDetected, asfPortOutPackets=asfPortOutPackets, asfPortCountIndex=asfPortCountIndex, asfIsdCountIndex=asfIsdCountIndex, asfIsdSessStatsEntry=asfIsdSessStatsEntry, asfPortInUnknowns=asfPortInUnknowns, asfConfigUpdateFail=asfConfigUpdateFail, memoryUsageUnit=memoryUsageUnit, asfPortInErrors=asfPortInErrors, asfIsdSessStatsTable=asfIsdSessStatsTable, asfPortNetStatsEntry=asfPortNetStatsEntry, asfPortInMcastPackets=asfPortInMcastPackets, asfAcceleratorAddedTrap=asfAcceleratorAddedTrap, asfConfigUpdateSuccess=asfConfigUpdateSuccess, asfFileSystemWarning=asfFileSystemWarning, asfPortNetStatsTable=asfPortNetStatsTable, asfAcceleratorRemovedTrap=asfAcceleratorRemovedTrap, asfNotifications=asfNotifications, asfFileSystemCritical=asfFileSystemCritical, asfNoOfSessions=asfNoOfSessions, asfPortInPackets=asfPortInPackets, asfFirewallStarted=asfFirewallStarted, asfPortOutBcastPackets=asfPortOutBcastPackets, infoString=infoString, asfNotificationObjs=asfNotificationObjs)
