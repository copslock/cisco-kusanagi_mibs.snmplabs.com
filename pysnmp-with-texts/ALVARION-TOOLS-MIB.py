#
# PySNMP MIB module ALVARION-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-TOOLS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionNotificationEnable, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionNotificationEnable")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Counter32, MibIdentifier, ModuleIdentity, IpAddress, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Counter64, Bits, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibIdentifier", "ModuleIdentity", "IpAddress", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Counter64", "Bits", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12))
if mibBuilder.loadTexts: alvarionToolsMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionToolsMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionToolsMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionToolsMIB.setDescription('Alvarion Tools MIB module.')
alvarionToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1))
traceToolConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1))
traceInterface = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceInterface.setStatus('current')
if mibBuilder.loadTexts: traceInterface.setDescription('Specifies the interface to apply the trace to.')
traceCaptureDestination = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureDestination.setStatus('current')
if mibBuilder.loadTexts: traceCaptureDestination.setDescription("Specifies if the traces shall be stored locally on the device or remotely on a distant system. 'local': Stores the traces locally on the device. 'remote': Stores the traces in a remote file specified by traceCaptureDestinationURL.")
traceCaptureDestinationURL = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureDestinationURL.setStatus('current')
if mibBuilder.loadTexts: traceCaptureDestinationURL.setDescription('Specifies the URL of the file that trace data will be sent to. If a valid URL is not defined, the trace data cannot be sent and will be discarded.')
traceTimeout = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999)).clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceTimeout.setStatus('current')
if mibBuilder.loadTexts: traceTimeout.setDescription('Specifies the amount of time the trace will capture data. Once this limit is reached, the trace automatically stops.')
traceNumberOfPackets = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999)).clone(100)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceNumberOfPackets.setStatus('current')
if mibBuilder.loadTexts: traceNumberOfPackets.setDescription('Specifies the maximum number of packets (IP datagrams) the trace should capture. Once this limit is reached, the trace automatically stops.')
tracePacketSize = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(68, 4096)).clone(128)).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tracePacketSize.setStatus('current')
if mibBuilder.loadTexts: tracePacketSize.setDescription('Specifies the maximum number of bytes to capture for each packet. The remaining data is discarded.')
traceCaptureFilter = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureFilter.setStatus('current')
if mibBuilder.loadTexts: traceCaptureFilter.setDescription('Specifies the packet filter to use to capture data. The filter expression has the same format and behavior as the expression parameter used by the well-known TCPDUMP command.')
traceCaptureStatus = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2))).clone('stop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureStatus.setStatus('current')
if mibBuilder.loadTexts: traceCaptureStatus.setDescription("IP Trace tool action trigger. 'stop': Stops the trace tool from functioning. If any capture was previously started it will end up. if no capture was started, 'stop' has no effect. 'start': Starts to capture the packets following the critera specified in the management tool and in this MIB.")
traceNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 1, 1, 9), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: traceNotificationEnabled.setDescription('Specifies if IP trace notifications are generated.')
alvarionToolsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 2))
alvarionToolsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 2, 0))
traceStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 2, 0, 1)).setObjects(("ALVARION-TOOLS-MIB", "traceCaptureStatus"))
if mibBuilder.loadTexts: traceStatusNotification.setStatus('current')
if mibBuilder.loadTexts: traceStatusNotification.setDescription('Sent when the user triggers the IP Trace tool either by starting a new trace or stopping an existing session.')
alvarionToolsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3))
alvarionToolsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 1))
alvarionToolsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 2))
alvarionToolsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 1, 1)).setObjects(("ALVARION-TOOLS-MIB", "alvarionToolsMIBGroup"), ("ALVARION-TOOLS-MIB", "alvarionToolsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionToolsMIBCompliance = alvarionToolsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionToolsMIBCompliance.setDescription('The compliance statement for entities which implement the Alvarion Tools MIB.')
alvarionToolsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 2, 1)).setObjects(("ALVARION-TOOLS-MIB", "traceInterface"), ("ALVARION-TOOLS-MIB", "traceCaptureDestination"), ("ALVARION-TOOLS-MIB", "traceCaptureDestinationURL"), ("ALVARION-TOOLS-MIB", "traceTimeout"), ("ALVARION-TOOLS-MIB", "traceNumberOfPackets"), ("ALVARION-TOOLS-MIB", "tracePacketSize"), ("ALVARION-TOOLS-MIB", "traceCaptureFilter"), ("ALVARION-TOOLS-MIB", "traceCaptureStatus"), ("ALVARION-TOOLS-MIB", "traceNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionToolsMIBGroup = alvarionToolsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionToolsMIBGroup.setDescription('A collection of objects providing the Tools MIB capability.')
alvarionToolsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 12, 3, 2, 2)).setObjects(("ALVARION-TOOLS-MIB", "traceStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionToolsNotificationGroup = alvarionToolsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionToolsNotificationGroup.setDescription('A collection of supported notifications.')
mibBuilder.exportSymbols("ALVARION-TOOLS-MIB", traceInterface=traceInterface, alvarionToolsMIBNotifications=alvarionToolsMIBNotifications, traceCaptureStatus=traceCaptureStatus, alvarionToolsMIB=alvarionToolsMIB, traceCaptureFilter=traceCaptureFilter, alvarionToolsMIBObjects=alvarionToolsMIBObjects, traceNotificationEnabled=traceNotificationEnabled, alvarionToolsMIBCompliance=alvarionToolsMIBCompliance, alvarionToolsMIBNotificationPrefix=alvarionToolsMIBNotificationPrefix, alvarionToolsMIBCompliances=alvarionToolsMIBCompliances, tracePacketSize=tracePacketSize, traceStatusNotification=traceStatusNotification, alvarionToolsNotificationGroup=alvarionToolsNotificationGroup, traceNumberOfPackets=traceNumberOfPackets, PYSNMP_MODULE_ID=alvarionToolsMIB, alvarionToolsMIBConformance=alvarionToolsMIBConformance, traceCaptureDestinationURL=traceCaptureDestinationURL, alvarionToolsMIBGroup=alvarionToolsMIBGroup, alvarionToolsMIBGroups=alvarionToolsMIBGroups, traceCaptureDestination=traceCaptureDestination, traceToolConfig=traceToolConfig, traceTimeout=traceTimeout)
