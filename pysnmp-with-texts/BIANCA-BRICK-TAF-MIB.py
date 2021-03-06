#
# PySNMP MIB module BIANCA-BRICK-TAF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-TAF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
Date, = mibBuilder.importSymbols("BIANCA-BRICK-PPP-MIB", "Date")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Counter64, MibIdentifier, Counter32, IpAddress, ObjectIdentity, Gauge32, Unsigned32, Bits, NotificationType, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter64", "MibIdentifier", "Counter32", "IpAddress", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "NotificationType", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bintecsec = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 254))
taf = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 254, 9))
tafServerTable = MibTable((1, 3, 6, 1, 4, 1, 272, 254, 9, 1), )
if mibBuilder.loadTexts: tafServerTable.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerTable.setDescription('The tafServerTable contains information about the servers that are used for the token authentication firewall.')
tafServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-TAF-MIB", "tafServerType"))
if mibBuilder.loadTexts: tafServerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerEntry.setDescription('')
tafServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ace", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerType.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerType.setDescription('Type of authentication server.')
tafServerNodeSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerNodeSecret.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerNodeSecret.setDescription('The shared secret between TAF server and Brick.')
tafServerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerVersion.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerVersion.setDescription('Version of the protocol between TAF server and Brick.')
tafServerRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerRetries.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerRetries.setDescription('The number of retries sent for each request')
tafServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerTimeout.setDescription('The amount of seconds waiting for an outstanding request.')
tafServerEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdi", 1), ("des", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerEncryption.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerEncryption.setDescription('The encryption algorithm that is used for the communication between ACE server and Brick')
tafServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerAddress.setDescription('The IP Address of the TAF server .')
tafServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerPort.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerPort.setDescription('The TAF server UDP port.')
tafServerClientPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerClientPort.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerClientPort.setDescription('The TAF client UDP port.')
tafServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerPriority.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerPriority.setDescription('The TAF server with the lowest priority is the first used for request. Use the value 0 for the master server and the value 1 for the slave server.')
tafServerState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("disabled", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerState.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerState.setDescription("The entry is ignored, if the value of this field is `disabled'. Set this field to `delete' to delete this entry")
tafServerCheckInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dont-verify", 1), ("verify", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tafServerCheckInterface.setStatus('mandatory')
if mibBuilder.loadTexts: tafServerCheckInterface.setDescription('')
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
ipTafTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 17), )
if mibBuilder.loadTexts: ipTafTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipTafTable.setDescription('The ipTafTable contains information about IP partners that sent packets to an interface that has authentication enabled.')
ipTafEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1), ).setIndexNames((0, "BIANCA-BRICK-TAF-MIB", "ipTafIfIndex"))
if mibBuilder.loadTexts: ipTafEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipTafEntry.setDescription('')
ipTafIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipTafIfIndex.setDescription('Interface Index.')
ipTafAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipTafAddress.setDescription('IP address of the partner')
ipTafState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("authenticating", 2), ("xfer", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafState.setStatus('mandatory')
if mibBuilder.loadTexts: ipTafState.setDescription('This object shows the authentication state of the partner. Packets are only routed if the state is xfer. If the state is authenticating a response from an authentication server is expected. Entries in state idle are deleted automatically after a timeout.')
ipTafAuthTime = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 4), Date()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipTafAuthTime.setStatus('mandatory')
if mibBuilder.loadTexts: ipTafAuthTime.setDescription('Time of the last successful authentication.')
ipTafTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipTafTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipTafTimeout.setDescription('This object gives the number of seconds till the authentication expires.')
mibBuilder.exportSymbols("BIANCA-BRICK-TAF-MIB", enterprises=enterprises, dod=dod, taf=taf, tafServerClientPort=tafServerClientPort, tafServerNodeSecret=tafServerNodeSecret, bintec=bintec, ipTafAddress=ipTafAddress, internet=internet, tafServerTimeout=tafServerTimeout, ipTafIfIndex=ipTafIfIndex, ipTafAuthTime=ipTafAuthTime, tafServerCheckInterface=tafServerCheckInterface, tafServerVersion=tafServerVersion, biboip=biboip, tafServerState=tafServerState, tafServerType=tafServerType, private=private, ipTafEntry=ipTafEntry, ipTafTimeout=ipTafTimeout, tafServerPort=tafServerPort, bibo=bibo, ipTafState=ipTafState, tafServerAddress=tafServerAddress, tafServerEncryption=tafServerEncryption, bintecsec=bintecsec, tafServerEntry=tafServerEntry, tafServerRetries=tafServerRetries, org=org, tafServerPriority=tafServerPriority, ipTafTable=ipTafTable, tafServerTable=tafServerTable)
