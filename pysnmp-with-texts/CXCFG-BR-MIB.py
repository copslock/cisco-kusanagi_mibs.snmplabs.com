#
# PySNMP MIB module CXCFG-BR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXCFG-BR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
cxCfgDot1dBase, Alias, cxCfgSrBase = mibBuilder.importSymbols("CXProduct-SMI", "cxCfgDot1dBase", "Alias", "cxCfgSrBase")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, IpAddress, Integer32, Counter32, MibIdentifier, iso, ObjectIdentity, Counter64, Gauge32, Unsigned32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "IpAddress", "Integer32", "Counter32", "MibIdentifier", "iso", "ObjectIdentity", "Counter64", "Gauge32", "Unsigned32", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxCfgDot1dBaseNumOfDBFilterEntries = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDot1dBaseNumOfDBFilterEntries.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBaseNumOfDBFilterEntries.setDescription('Determines the number of entries in the filtering database. Available RAM is the parameter. Range of Values: None Default Value: None Configuration Changed: Administrative')
cxCfgDot1dBaseNumOfStaticDBFilterEntries = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDot1dBaseNumOfStaticDBFilterEntries.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBaseNumOfStaticDBFilterEntries.setDescription('Determines the number of static entries in the filtering database. Available RAM is the parameter. Range of Values: None Default Value: None Configuration Changed: Administrative')
cxCfgDot1dBasePortTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3), )
if mibBuilder.loadTexts: cxCfgDot1dBasePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePortTable.setDescription('A table that contains basic information about every port that is associated with this bridge.')
cxCfgDot1dBasePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1), ).setIndexNames((0, "CXCFG-BR-MIB", "cxCfgDot1dBasePort"))
if mibBuilder.loadTexts: cxCfgDot1dBasePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePortEntry.setDescription('Contains configuration information for each port of the bridge.')
cxCfgDot1dBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgDot1dBasePort.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePort.setDescription("Displays the port number. Options: The acceptable values depend on the type of device that you are configuring. In the CX900 architecture: 11, 21, 31, 41, 51, 61 or 71. The first digit identifies the slot number the I/O board resides in, the second digit identifies the number of the port on the I/O board. In the CX1000 architecture: Accepts only the value '1'. The LAN module only supports 1 port per I/O board. You distinguish between multiple I/O boards by specifying the slot number of the I/O board using another object. Default Value: 1")
cxCfgDot1dBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgDot1dBasePortIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePortIfIndex.setDescription("Displays the table row that contains configuration or monitoring objects for a specific type of physical interface. Range of Values: From 1 to the total number of entries in the Interface Table. Default Value: '0' indicates there is no corresponding entry in the Interface Table for this port. ")
cxCfgDot1dBasePortSubnetworkSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDot1dBasePortSubnetworkSapAlias.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePortSubnetworkSapAlias.setDescription("Specifies a name (alias) for the physical or convergence port to which this port binds in order to establish a circuit for transmission. This value must match a physical or convergence port's alias, as defined by the cxLanIoPortAlias object in the cxLanIoPortTable or by the object cxConvPortAlias in the cxConvTable. Range of Values: From 1 to 32 alphanumeric characters. You can use any combination of letters and numbers however, you cannot use blank spaces. Use a dash or underscore as a delimiter. Default Value: LAN-PORT1 Configuration Changed: Administrative")
cxCfgDot1dBasePortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDot1dBasePortRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePortRowStatus.setDescription('Determines the status of the objects in a table row. Options: invalid (1): Row is flagged; after the next reset the values will be disabled and the row will be deleted from the table). valid (2): Values are enabled. Default value: valid (2) Configuration Changed: Administrative')
cxCfgDot1dBasePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("onether", 3), ("ontoken", 4))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDot1dBasePortState.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePortState.setDescription('Determines the state of the STP port. Options: On (1): The STP port is set to on. Off (2): The STP port is set to off. OnEther (3): The Ethernet STP port will bind to IP. OnToken (4): The Token Ring STP port will bind to IP. Default value: On (1) Configuration Changed: Administrative')
cxCfgDot1dBasePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discard", 1), ("forward", 2), ("priority-low", 3), ("priority-high", 4))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDot1dBasePortPriority.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBasePortPriority.setDescription('Determines the filtering/forwarding action and the forwarding priority for data sent from the STP bridge. Options: discard (1): Do not forward the data. forward (2): Forward the data. priority-low (3): Forward with a low priority (Frame Relay only). priority-high (4): Forward with a high priority (Frame Relay only). Default Value: forward (2) Configuration Changed: Administrative')
cxCfgSrBasePortTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1), )
if mibBuilder.loadTexts: cxCfgSrBasePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePortTable.setDescription('A table that contains basic information about every port that is associated with this SR bridge.')
cxCfgSrBasePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1), ).setIndexNames((0, "CXCFG-BR-MIB", "cxCfgSrBasePort"))
if mibBuilder.loadTexts: cxCfgSrBasePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePortEntry.setDescription('Configuration information for each port of the SR bridge.')
cxCfgSrBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgSrBasePort.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePort.setDescription("Displays the port number. Options: The acceptable values depend on the type of device that you are configuring. In the CX 900 architecture: 11, 21, 31, 41, 51, 61 or 71. The first digit identifies the slot number the I/O board resides in, the second digit identifies the number of the port on the I/O board. In the CX 1000 architecture: Accepts only the value '1'. The LAN module only supports 1 port per I/O board. You distinguish between multiple I/O boards by specifying the slot number of the I/O board using another object. Default Value: 1 ")
cxCfgSrBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgSrBasePortIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePortIfIndex.setDescription("Displays the table row that contains configuration or monitoring objects for a specific type of physical interface. Range of Values: From 1 to the total number of entries in the Interface Table. Default Value: '0' indicates there is no corresponding entry in the Interface Table for this port.")
cxCfgSrBasePortSubnetworkSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgSrBasePortSubnetworkSapAlias.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePortSubnetworkSapAlias.setDescription("Specifies a name (alias) for the physical or convergence port to which this SR port binds in order to establish a circuit for transmission. This value must match a physical or convergence port's alias as defined by the object cxLanIoPortAlias of the cxLanIoPortTable or by the object cxConvPortAlias of the cxConvTable. Range of Values: From 1 to 32 alphanumeric characters. You can use any combination of letters and numbers however, you cannot use blank spaces. Use a dash or underscore as a delimiter. Default Value: LAN-PORT1 Configuration Changed: Administrative")
cxCfgSrBasePortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgSrBasePortRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePortRowStatus.setDescription('Determines the status of the objects in a table row. Options: invalid (1): Row is flagged. After the next reset the values will be disabled and the row will be deleted from the table. valid (2): Values are enabled. Default Value: (2) Configuration Changed: Administrative')
cxCfgSrBasePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("ontoken", 3))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgSrBasePortState.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePortState.setDescription('Determines the state of the SR port. You can control activity at the port by changing this value. Options: on (1): The SR port is set to on. off (2): The SR port is set to off. OnToken (4): The Token Ring SR port will bind to IP. Default Value: (1) Configuration Changed: Administrative')
cxCfgSrBasePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discard", 1), ("forward", 2), ("priority-low", 3), ("priority-high", 4))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgSrBasePortPriority.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgSrBasePortPriority.setDescription('Determines the filtering/forwarding action and the forwarding priority for data sent from the SR bridge. Options: discard (1): Do not forward the data. forward (2): Forward the data. priority-low (3): Forward with a low priority (Frame Relay only). priority-high (4): Forward with a high priority (Frame Relay only). Default value: (2) Configuration Changed: Administrative')
cxCfgDot1dBaseMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgDot1dBaseMibLevel.setStatus('mandatory')
if mibBuilder.loadTexts: cxCfgDot1dBaseMibLevel.setDescription('Used to determine current MIB module release supported by the agent. Object is in decimal.')
mibBuilder.exportSymbols("CXCFG-BR-MIB", cxCfgDot1dBasePortState=cxCfgDot1dBasePortState, cxCfgDot1dBaseNumOfStaticDBFilterEntries=cxCfgDot1dBaseNumOfStaticDBFilterEntries, cxCfgDot1dBasePortPriority=cxCfgDot1dBasePortPriority, cxCfgDot1dBasePortIfIndex=cxCfgDot1dBasePortIfIndex, cxCfgDot1dBasePortSubnetworkSapAlias=cxCfgDot1dBasePortSubnetworkSapAlias, cxCfgSrBasePortIfIndex=cxCfgSrBasePortIfIndex, cxCfgDot1dBasePortRowStatus=cxCfgDot1dBasePortRowStatus, cxCfgSrBasePortEntry=cxCfgSrBasePortEntry, cxCfgSrBasePortPriority=cxCfgSrBasePortPriority, cxCfgDot1dBasePortTable=cxCfgDot1dBasePortTable, cxCfgDot1dBasePortEntry=cxCfgDot1dBasePortEntry, cxCfgSrBasePort=cxCfgSrBasePort, cxCfgSrBasePortTable=cxCfgSrBasePortTable, cxCfgSrBasePortRowStatus=cxCfgSrBasePortRowStatus, cxCfgDot1dBaseNumOfDBFilterEntries=cxCfgDot1dBaseNumOfDBFilterEntries, cxCfgSrBasePortSubnetworkSapAlias=cxCfgSrBasePortSubnetworkSapAlias, cxCfgSrBasePortState=cxCfgSrBasePortState, cxCfgDot1dBaseMibLevel=cxCfgDot1dBaseMibLevel, cxCfgDot1dBasePort=cxCfgDot1dBasePort)
