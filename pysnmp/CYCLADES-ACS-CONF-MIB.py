#
# PySNMP MIB module CYCLADES-ACS-CONF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYCLADES-ACS-CONF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
cyACSMgmt, = mibBuilder.importSymbols("CYCLADES-ACS-MIB", "cyACSMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Gauge32, Counter32, Unsigned32, MibIdentifier, NotificationType, IpAddress, iso, Integer32, TimeTicks, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Gauge32", "Counter32", "Unsigned32", "MibIdentifier", "NotificationType", "IpAddress", "iso", "Integer32", "TimeTicks", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyACSConf = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 2))
cyACSConf.setRevisions(('2005-08-29 00:00', '2003-06-30 00:00', '2003-01-17 00:00', '2002-10-20 00:00', '2002-09-20 00:00',))
if mibBuilder.loadTexts: cyACSConf.setLastUpdated('200508290000Z')
if mibBuilder.loadTexts: cyACSConf.setOrganization('Cyclades Corporation')
cyHostName = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyHostName.setStatus('current')
cyConsoleBanner = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyConsoleBanner.setStatus('current')
cyMotd = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyMotd.setStatus('current')
cyEthItf = ObjectIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 2, 4))
if mibBuilder.loadTexts: cyEthItf.setStatus('current')
cyEthDhcpc = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1), ("restore", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyEthDhcpc.setStatus('current')
cyEthIPaddr = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyEthIPaddr.setStatus('current')
cyEthIPmask = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyEthIPmask.setStatus('current')
cyEthMTU = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyEthMTU.setStatus('current')
cyEthIPaddr2 = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyEthIPaddr2.setStatus('current')
cyEthIPmask2 = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 4, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyEthIPmask2.setStatus('current')
cyNameService = ObjectIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 2, 5))
if mibBuilder.loadTexts: cyNameService.setStatus('current')
cyResolverOrder = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyResolverOrder.setStatus('current')
cyMultipleIP = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyMultipleIP.setStatus('current')
cyDNSserv = ObjectIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3))
if mibBuilder.loadTexts: cyDNSserv.setStatus('current')
cyDNSpriserv = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyDNSpriserv.setStatus('current')
cyDNSsecserv = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyDNSsecserv.setStatus('current')
cyDNSdomain = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 5, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyDNSdomain.setStatus('current')
cySerialPortConf = ObjectIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6))
if mibBuilder.loadTexts: cySerialPortConf.setStatus('current')
cySerialGlobal = ObjectIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1))
if mibBuilder.loadTexts: cySerialGlobal.setStatus('current')
cySerialInclude = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialInclude.setStatus('current')
cySerialNFS = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialNFS.setStatus('current')
cySerialLockDir = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialLockDir.setStatus('current')
cySerialRlogin = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialRlogin.setStatus('current')
cySerialPppd = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialPppd.setStatus('current')
cySerialTelnet = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialTelnet.setStatus('current')
cySerialSsh = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialSsh.setStatus('current')
cySerialLocalLogins = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialLocalLogins.setStatus('current')
cySerialFacility = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialFacility.setStatus('current')
cySerialDBFacility = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySerialDBFacility.setStatus('current')
cySerialGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11), )
if mibBuilder.loadTexts: cySerialGroupTable.setStatus('current')
cygroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1), ).setIndexNames((0, "CYCLADES-ACS-CONF-MIB", "cyGroupIndex"))
if mibBuilder.loadTexts: cygroupEntry.setStatus('current')
cyGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyGroupIndex.setStatus('current')
cyGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyGroupName.setStatus('current')
cyGroupUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 1, 11, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyGroupUsers.setStatus('current')
cySerialSpec = ObjectIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2))
if mibBuilder.loadTexts: cySerialSpec.setStatus('current')
cySerialPortTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1), )
if mibBuilder.loadTexts: cySerialPortTable.setStatus('current')
cysportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1), ).setIndexNames((0, "CYCLADES-ACS-CONF-MIB", "cySPortNumber"))
if mibBuilder.loadTexts: cysportEntry.setStatus('current')
cySPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cySPortNumber.setStatus('current')
cySPortTty = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortTty.setStatus('current')
cySPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortName.setStatus('current')
cySPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200, 230400, 460800))).clone(namedValues=NamedValues(("s50bps", 50), ("s75bps", 75), ("s110bps", 110), ("s134bps", 134), ("s150bps", 150), ("s200bps", 200), ("s300bps", 300), ("s600bps", 600), ("s1200bps", 1200), ("s1800bps", 1800), ("s2400bps", 2400), ("s4800bps", 4800), ("s9600bps", 9600), ("s14400bps", 14400), ("s19200bps", 19200), ("s28800bps", 28800), ("s38400bps", 38400), ("s57600bps", 57600), ("s115200bps", 115200), ("s230400bps", 230400), ("s460800bps", 460800)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSpeed.setStatus('current')
cySPortDataSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDataSize.setStatus('current')
cySPortStopBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortStopBits.setStatus('current')
cySPortParity = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortParity.setStatus('current')
cySPortFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortFlowCtrl.setStatus('current')
cySPortDTRdelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDTRdelay.setStatus('current')
cySPortDCDCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notctrl", 0), ("control", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDCDCtrl.setStatus('current')
cySPortLogUtmp = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortLogUtmp.setStatus('current')
cySPortLogWtmp = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortLogWtmp.setStatus('current')
cySPortLogform = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortLogform.setStatus('current')
cySPortAuthtype = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthtype.setStatus('current')
cySPortAuthSrv1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthSrv1.setStatus('current')
cySPortAccSrv1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAccSrv1.setStatus('current')
cySPortAuthTmo = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthTmo.setStatus('current')
cySPortAuthRetr = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthRetr.setStatus('current')
cySPortAuthSrv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 19), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthSrv2.setStatus('current')
cySPortAccSrv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAccSrv2.setStatus('current')
cySPortAuthSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthSecret.setStatus('current')
cySPortAuthRadP = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthRadP.setStatus('current')
cySPortAuthAcc = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAuthAcc.setStatus('current')
cySPortProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortProtocol.setStatus('current')
cySPortRemoteIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortRemoteIP.setStatus('current')
cySPortSocketPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSocketPort.setStatus('current')
cySPortRemHost = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 27), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortRemHost.setStatus('current')
cySPortBanner = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 250))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortBanner.setStatus('current')
cySPortPrompt = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 250))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPrompt.setStatus('current')
cySPortTermType = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortTermType.setStatus('current')
cySPortAutomUsr = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAutomUsr.setStatus('current')
cySPortNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 32), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortNetMask.setStatus('current')
cySPortPppMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 33), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPppMtu.setStatus('current')
cySPortPppMru = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 34), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPppMru.setStatus('current')
cySPortPppOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 35), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPppOptions.setStatus('current')
cySPortPppFoption = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 36), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPppFoption.setStatus('current')
cySPortModemChat = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 37), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortModemChat.setStatus('current')
cySPortSttyCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 38), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 180))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSttyCmd.setStatus('current')
cySPortSockTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 39), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSockTx.setStatus('current')
cySPortSockPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 40), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSockPoll.setStatus('current')
cySPortSockIdle = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 41), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSockIdle.setStatus('current')
cySPortDBsize = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 42), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDBsize.setStatus('current')
cySPortDBtime = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDBtime.setStatus('current')
cySPortDBmode = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 44), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDBmode.setStatus('current')
cySPortDBsyslog = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 45), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDBsyslog.setStatus('current')
cySPortDBmenu = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 46), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("displayMenu", 0), ("inactive", 1), ("displayDB", 2), ("displayParc", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDBmenu.setStatus('current')
cySPortDBalarm = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 47), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortDBalarm.setStatus('current')
cySPortSSHbreak = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 48), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSSHbreak.setStatus('current')
cySPortSniffSess = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 49), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSniffSess.setStatus('current')
cySPortSniffAdm = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 50), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSniffAdm.setStatus('current')
cySPortSniffEsc = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 51), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSniffEsc.setStatus('current')
cySPortSniffMsess = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 52), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSniffMsess.setStatus('current')
cySPortTelnetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 53), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("text", 0), ("binary", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortTelnetMode.setStatus('current')
cySPortSysBufSess = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("yes", 0), ("no", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortSysBufSess.setStatus('current')
cySPortLFSuppress = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 55), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortLFSuppress.setStatus('current')
cySPortAutoInput = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 56), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAutoInput.setStatus('current')
cySPortAutoOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 57), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortAutoOutput.setStatus('current')
cySPortPmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 58), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPmType.setStatus('current')
cySPortPmUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 59), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPmUsers.setStatus('current')
cySPortPmOutlet = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 60), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPmOutlet.setStatus('current')
cySPortPmKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 61), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPmKey.setStatus('current')
cySPortPmNOutlets = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 62), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortPmNOutlets.setStatus('current')
cySPortBreakInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 2, 6, 2, 1, 1, 63), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cySPortBreakInterval.setStatus('current')
mibBuilder.exportSymbols("CYCLADES-ACS-CONF-MIB", cySPortDataSize=cySPortDataSize, cySerialLockDir=cySerialLockDir, cyACSConf=cyACSConf, cySPortDTRdelay=cySPortDTRdelay, cySPortAuthtype=cySPortAuthtype, cyResolverOrder=cyResolverOrder, cyGroupName=cyGroupName, cySPortPppMru=cySPortPppMru, cySPortLogform=cySPortLogform, cySPortSpeed=cySPortSpeed, cySPortModemChat=cySPortModemChat, cySPortSysBufSess=cySPortSysBufSess, cySPortPmNOutlets=cySPortPmNOutlets, cyEthIPmask=cyEthIPmask, cySPortFlowCtrl=cySPortFlowCtrl, cySPortLogUtmp=cySPortLogUtmp, cySerialGroupTable=cySerialGroupTable, cySPortAuthTmo=cySPortAuthTmo, cySPortTelnetMode=cySPortTelnetMode, cySPortParity=cySPortParity, cySPortAccSrv1=cySPortAccSrv1, cySerialPppd=cySerialPppd, cyEthDhcpc=cyEthDhcpc, cySPortPmOutlet=cySPortPmOutlet, cySerialRlogin=cySerialRlogin, cySPortPmUsers=cySPortPmUsers, cySPortNetMask=cySPortNetMask, cySPortSSHbreak=cySPortSSHbreak, cyMultipleIP=cyMultipleIP, cyDNSsecserv=cyDNSsecserv, cySPortSttyCmd=cySPortSttyCmd, cySPortDBsize=cySPortDBsize, cySPortAuthAcc=cySPortAuthAcc, cySPortName=cySPortName, cyDNSserv=cyDNSserv, PYSNMP_MODULE_ID=cyACSConf, cyConsoleBanner=cyConsoleBanner, cyGroupUsers=cyGroupUsers, cyHostName=cyHostName, cySPortTty=cySPortTty, cySPortRemoteIP=cySPortRemoteIP, cySPortPmType=cySPortPmType, cygroupEntry=cygroupEntry, cySPortSockPoll=cySPortSockPoll, cySPortSockIdle=cySPortSockIdle, cySPortAutoOutput=cySPortAutoOutput, cySerialFacility=cySerialFacility, cySerialLocalLogins=cySerialLocalLogins, cyGroupIndex=cyGroupIndex, cySPortSocketPort=cySPortSocketPort, cySPortDBalarm=cySPortDBalarm, cySPortSockTx=cySPortSockTx, cyEthItf=cyEthItf, cySPortAuthRetr=cySPortAuthRetr, cySPortAutomUsr=cySPortAutomUsr, cySPortPrompt=cySPortPrompt, cyNameService=cyNameService, cyEthMTU=cyEthMTU, cySPortSniffSess=cySPortSniffSess, cySerialNFS=cySerialNFS, cySPortDCDCtrl=cySPortDCDCtrl, cyDNSdomain=cyDNSdomain, cySPortAuthSrv2=cySPortAuthSrv2, cySerialDBFacility=cySerialDBFacility, cySPortSniffAdm=cySPortSniffAdm, cySPortLFSuppress=cySPortLFSuppress, cySPortSniffEsc=cySPortSniffEsc, cyMotd=cyMotd, cySerialGlobal=cySerialGlobal, cyEthIPmask2=cyEthIPmask2, cySPortSniffMsess=cySPortSniffMsess, cySerialPortTable=cySerialPortTable, cySPortAuthSecret=cySPortAuthSecret, cySPortDBsyslog=cySPortDBsyslog, cySPortRemHost=cySPortRemHost, cySPortAuthRadP=cySPortAuthRadP, cySPortLogWtmp=cySPortLogWtmp, cySPortAccSrv2=cySPortAccSrv2, cySerialSsh=cySerialSsh, cySPortAuthSrv1=cySPortAuthSrv1, cySPortAutoInput=cySPortAutoInput, cySPortDBtime=cySPortDBtime, cySPortPppMtu=cySPortPppMtu, cySPortTermType=cySPortTermType, cySPortBreakInterval=cySPortBreakInterval, cySPortPppOptions=cySPortPppOptions, cysportEntry=cysportEntry, cySPortDBmenu=cySPortDBmenu, cySerialTelnet=cySerialTelnet, cySPortDBmode=cySPortDBmode, cySPortPppFoption=cySPortPppFoption, cySPortPmKey=cySPortPmKey, cyDNSpriserv=cyDNSpriserv, cyEthIPaddr2=cyEthIPaddr2, cySerialInclude=cySerialInclude, cySPortStopBits=cySPortStopBits, cySPortBanner=cySPortBanner, cySerialPortConf=cySerialPortConf, cySerialSpec=cySerialSpec, cySPortProtocol=cySPortProtocol, cyEthIPaddr=cyEthIPaddr, cySPortNumber=cySPortNumber)