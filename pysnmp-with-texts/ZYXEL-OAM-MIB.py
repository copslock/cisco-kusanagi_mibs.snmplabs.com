#
# PySNMP MIB module ZYXEL-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-OAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, ObjectIdentity, IpAddress, Integer32, Gauge32, ModuleIdentity, TimeTicks, Counter64, Bits, Counter32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "ObjectIdentity", "IpAddress", "Integer32", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter64", "Bits", "Counter32", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56))
if mibBuilder.loadTexts: zyxelOam.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelOam.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelOam.setContactInfo('')
if mibBuilder.loadTexts: zyxelOam.setDescription('The subtree for Operations, Administration, and Maintenance (OAM)')
zyxelOamSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1))
zyOamState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOamState.setStatus('current')
if mibBuilder.loadTexts: zyOamState.setDescription('Enable/Disable administrative status on the switch.')
zyxelOamPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2), )
if mibBuilder.loadTexts: zyxelOamPortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelOamPortTable.setDescription('The table contains OAM (Operations, Administration, and Maintenance) port configuration. ')
zyxelOamPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyxelOamPortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelOamPortEntry.setDescription('An entry contains OAM port configuration.')
zyOamPortFunctionsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1, 1), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOamPortFunctionsSupported.setReference('[802.3ah], 30.3.6.1.6')
if mibBuilder.loadTexts: zyOamPortFunctionsSupported.setStatus('current')
if mibBuilder.loadTexts: zyOamPortFunctionsSupported.setDescription("The OAM functions supported on this Ethernet-like interface. OAM consists of separate functional sets beyond the basic discovery process that is always required. These functional groups can be supported independently by any implementation. These values are communicated to the peer via the local configuration field of Information OAMPDUs. Setting 'unidirectionalSupport(0)' indicates that the OA entity supports the transmission of OAMPDUs on links that are operating in unidirectional mode (traffic flowing in one direction only). Setting 'loopbackSupport(1)' indicates that the OAM entity can initiate and respond to loopback commands. Setting 'eventSupport(2)' indicates that the OAM entity can send and receive Event Notification OAMPDUs. Setting 'variableSupport(3)' indicates that the OAM entity can send and receive Variable Request and Response OAMPDUs. ")
mibBuilder.exportSymbols("ZYXEL-OAM-MIB", zyxelOamSetup=zyxelOamSetup, zyxelOam=zyxelOam, zyOamPortFunctionsSupported=zyOamPortFunctionsSupported, zyxelOamPortTable=zyxelOamPortTable, zyxelOamPortEntry=zyxelOamPortEntry, zyOamState=zyOamState, PYSNMP_MODULE_ID=zyxelOam)
