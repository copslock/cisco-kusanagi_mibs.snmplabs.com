#
# PySNMP MIB module SIP-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-DS1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:04:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, snmpModules, enterprises, ObjectIdentity, IpAddress, TimeTicks, Counter32, Unsigned32, ModuleIdentity, Integer32, Bits, Counter64, ObjectName, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "snmpModules", "enterprises", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "ObjectName", "Gauge32")
TextualConvention, TruthValue, DisplayString, RowStatus, TimeStamp, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus", "TimeStamp", "TestAndIncr")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
sipDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5))
sipDS1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1))
if mibBuilder.loadTexts: sipDS1.setLastUpdated('240701')
if mibBuilder.loadTexts: sipDS1.setOrganization('Lucent Technologies')
if mibBuilder.loadTexts: sipDS1.setContactInfo('')
if mibBuilder.loadTexts: sipDS1.setDescription('The MIB module for entities implementing the xxxx protocol.')
sipSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1))
dsInfo = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsInfo.setStatus('current')
if mibBuilder.loadTexts: dsInfo.setDescription('Device Server information. This value should include the full name and version identification and/or manufacturer information. It is mandatory that this contains only printable ASCII characters')
dsProtocolInfo = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsProtocolInfo.setStatus('current')
if mibBuilder.loadTexts: dsProtocolInfo.setDescription('Device Server H323/SIP stack information. This value should include the full name and version identification and/or manufacturer information of the H323/SIP Stack used in the device server implementation. It is mandatory that this contains only printable ASCII characters')
logLevel = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logLevel.setStatus('current')
if mibBuilder.loadTexts: logLevel.setDescription('Device Server Log Level. A minimum logging level is always set for the device servers, which logs errors and warnings. If still more verbosity is required, that can be done by setting this parameter to a required level. 1. Error 2. Warning 3. Info')
succeededCalls = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: succeededCalls.setStatus('current')
if mibBuilder.loadTexts: succeededCalls.setDescription('Total number of calls successfully made since the last uptime of this device server.')
activeCalls = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: activeCalls.setStatus('current')
if mibBuilder.loadTexts: activeCalls.setDescription('Number of calls which are still progressing at this time by this device server')
failedCalls = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: failedCalls.setStatus('current')
if mibBuilder.loadTexts: failedCalls.setDescription('Total Number of calls failed since the last uptime of this device server')
reloadConfig = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reloadConfig.setStatus('current')
if mibBuilder.loadTexts: reloadConfig.setDescription("This is to tell the device server to load it's configuration again. This is done when some configuration parameters need to be updated in the system ")
resetLog = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resetLog.setStatus('current')
if mibBuilder.loadTexts: resetLog.setDescription('To discard previous log and to start logging afresh resetLog would be used ')
mibBuilder.exportSymbols("SIP-DS1-MIB", dsInfo=dsInfo, products=products, lucent=lucent, resetLog=resetLog, logLevel=logLevel, softSwitch=softSwitch, sipDeviceServer=sipDeviceServer, succeededCalls=succeededCalls, reloadConfig=reloadConfig, dsProtocolInfo=dsProtocolInfo, sipDS1=sipDS1, PYSNMP_MODULE_ID=sipDS1, sipSystem=sipSystem, failedCalls=failedCalls, activeCalls=activeCalls)
