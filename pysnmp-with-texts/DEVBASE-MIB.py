#
# PySNMP MIB module DEVBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVBASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, Unsigned32, MibIdentifier, ModuleIdentity, Counter32, Counter64, ObjectIdentity, NotificationType, Bits, iso, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter32", "Counter64", "ObjectIdentity", "NotificationType", "Bits", "iso", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
aniDevBase = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 1))
if mibBuilder.loadTexts: aniDevBase.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevBase.setOrganization('Aperto Networks')
if mibBuilder.loadTexts: aniDevBase.setContactInfo(' Postal: Aperto Networks Inc 1637 S Main Street Milpitas, California 95035 Tel: +1 408 719 9977 ')
if mibBuilder.loadTexts: aniDevBase.setDescription('This group gives some basic information about the device (BSU or SU). All objects within this group are applicable to both the devices. ')
aniDevProductName = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevProductName.setStatus('current')
if mibBuilder.loadTexts: aniDevProductName.setDescription('The model number of the device. ')
aniDevLanIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevLanIpAddr.setStatus('current')
if mibBuilder.loadTexts: aniDevLanIpAddr.setDescription('The Lan IP Address of the device.')
aniDevLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevLanSubnetMask.setStatus('current')
if mibBuilder.loadTexts: aniDevLanSubnetMask.setDescription('The subnet mask of the device.')
aniDevDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevDefaultGateway.setStatus('current')
if mibBuilder.loadTexts: aniDevDefaultGateway.setDescription('The Gateway IP address. On BSU, this refers to the Lan Gateway address. On SU, this refers to the Wireless Gateway address. ')
aniDevMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevMacAddr.setStatus('current')
if mibBuilder.loadTexts: aniDevMacAddr.setDescription('The Mac Address of the device.')
mibBuilder.exportSymbols("DEVBASE-MIB", aniDevDefaultGateway=aniDevDefaultGateway, aniDevLanIpAddr=aniDevLanIpAddr, PYSNMP_MODULE_ID=aniDevBase, aniDevProductName=aniDevProductName, aniDevLanSubnetMask=aniDevLanSubnetMask, aniDevBase=aniDevBase, aniDevMacAddr=aniDevMacAddr)
