#
# PySNMP MIB module SSHDEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SSHDEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
sshdExt, = mibBuilder.importSymbols("APENT-MIB", "sshdExt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, TimeTicks, Unsigned32, iso, Bits, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "TimeTicks", "Unsigned32", "iso", "Bits", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter32", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apSshdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 43, 1))
if mibBuilder.loadTexts: apSshdMib.setLastUpdated('0004031500Z')
if mibBuilder.loadTexts: apSshdMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apSshdMib.setContactInfo('Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apSshdMib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for SSHD')
apSshdKeepAlive = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdKeepAlive.setStatus('current')
if mibBuilder.loadTexts: apSshdKeepAlive.setDescription('Specifies whether the system should send keepalives to the other side')
apSshdKeyRegenerationInterval = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdKeyRegenerationInterval.setStatus('current')
if mibBuilder.loadTexts: apSshdKeyRegenerationInterval.setDescription('Automatically regenerate server key after this many minutes (if it has been used.)')
apSshdPort = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(22, 65535)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdPort.setStatus('current')
if mibBuilder.loadTexts: apSshdPort.setDescription('Specifies the port number that server listens on')
apSshdServerKeyBits = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 43, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 65535)).clone(768)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSshdServerKeyBits.setStatus('current')
if mibBuilder.loadTexts: apSshdServerKeyBits.setDescription('Defines the number of bits in the server key')
mibBuilder.exportSymbols("SSHDEXT-MIB", PYSNMP_MODULE_ID=apSshdMib, apSshdServerKeyBits=apSshdServerKeyBits, apSshdKeyRegenerationInterval=apSshdKeyRegenerationInterval, apSshdMib=apSshdMib, apSshdPort=apSshdPort, apSshdKeepAlive=apSshdKeepAlive)
