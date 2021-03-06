#
# PySNMP MIB module ZYXEL-TRTCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-TRTCM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:52:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Gauge32, MibIdentifier, NotificationType, Integer32, Unsigned32, Bits, iso, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Unsigned32", "Bits", "iso", "ModuleIdentity", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelTrtcm = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85))
if mibBuilder.loadTexts: zyxelTrtcm.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelTrtcm.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelTrtcm.setContactInfo('')
if mibBuilder.loadTexts: zyxelTrtcm.setDescription('The subtree for Two Rate Three Color Marker (trTCM)')
zyxelTrtcmSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1))
zyTctcmState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTctcmState.setStatus('current')
if mibBuilder.loadTexts: zyTctcmState.setDescription('Enable/Disable TRTCM (Two-rate three color marker) on the switch. The switch evaluates and marks the packets based on the TRTCM settings. Note: You must also enable DiffServ on the switch and the individual ports for the switch to drop red (high loss priority) colored packets.')
zyTrtcmMode = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("colorAware", 0), ("colorBlind", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTrtcmMode.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmMode.setDescription('Enter colorBlind to have the switch treat all incoming packets as uncolored. All incoming packets are evaluated against the CIR and PIR. Enter colorAware to treat the packets as marked by some preceding entity. Incoming packets are evaluated based on their existing color. Incoming packets that are not marked proceed through the switch.')
zyxelTrtcmPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3), )
if mibBuilder.loadTexts: zyxelTrtcmPortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelTrtcmPortTable.setDescription('The table contains TRTCM port configuration.')
zyxelTrtcmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelTrtcmPortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelTrtcmPortEntry.setDescription('An entry contains TRTCM port configuration.')
zyTrtcmPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 1), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyTrtcmPortState.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmPortState.setDescription('Enable/Disable TRTCM on the port.')
zyTrtcmPortCir = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTrtcmPortCir.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmPortCir.setDescription('Specify the Commit Information Rate (CIR) for this port.')
zyTrtcmPortPir = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTrtcmPortPir.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmPortPir.setDescription('Specify the Peak Information Rate (PIR) for this port.')
zyTrtcmPortDscpProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTrtcmPortDscpProfile.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmPortDscpProfile.setDescription('The name of trtcm dscp profile with specifed CIR and PIR setting on the port.')
zyTrtcmMaxNumberOfDscpProfiles = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyTrtcmMaxNumberOfDscpProfiles.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmMaxNumberOfDscpProfiles.setDescription('The maximum number of TRTCM DSCP profile that can be created.')
zyxelTrtcmDscpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5), )
if mibBuilder.loadTexts: zyxelTrtcmDscpProfileTable.setStatus('current')
if mibBuilder.loadTexts: zyxelTrtcmDscpProfileTable.setDescription('AThe talbe contains TRTCM profile configuration.')
zyxelTrtcmDscpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1), ).setIndexNames((0, "ZYXEL-TRTCM-MIB", "zyTrtcmDscpProfileName"))
if mibBuilder.loadTexts: zyxelTrtcmDscpProfileEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelTrtcmDscpProfileEntry.setDescription('An entry contains TRTCM profile configuration.')
zyTrtcmDscpProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyTrtcmDscpProfileName.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmDscpProfileName.setDescription('The name of TRTCM DSCP profile.')
zyTrtcmDscpProfileDscpGreen = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTrtcmDscpProfileDscpGreen.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmDscpProfileDscpGreen.setDescription('Specify the DSCP Green value to use for packets with low packet loss priority.')
zyTrtcmDscpProfileDscpYellow = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTrtcmDscpProfileDscpYellow.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmDscpProfileDscpYellow.setDescription('Specify the DSCP Yellow value to use for packets with medium packet loss priority. ')
zyTrtcmDscpProfileDscpRed = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyTrtcmDscpProfileDscpRed.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmDscpProfileDscpRed.setDescription('Specify the DSCP red value to use for packets with high packet loss priority.')
zyTrtcmDscpProfileRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyTrtcmDscpProfileRowstatus.setStatus('current')
if mibBuilder.loadTexts: zyTrtcmDscpProfileRowstatus.setDescription('This object allows to create and delete a TRTCM DSCP profile entry.')
mibBuilder.exportSymbols("ZYXEL-TRTCM-MIB", PYSNMP_MODULE_ID=zyxelTrtcm, zyxelTrtcm=zyxelTrtcm, zyTrtcmDscpProfileDscpRed=zyTrtcmDscpProfileDscpRed, zyTrtcmDscpProfileDscpYellow=zyTrtcmDscpProfileDscpYellow, zyTrtcmPortState=zyTrtcmPortState, zyxelTrtcmSetup=zyxelTrtcmSetup, zyTrtcmDscpProfileDscpGreen=zyTrtcmDscpProfileDscpGreen, zyTrtcmPortDscpProfile=zyTrtcmPortDscpProfile, zyxelTrtcmPortTable=zyxelTrtcmPortTable, zyxelTrtcmDscpProfileEntry=zyxelTrtcmDscpProfileEntry, zyTrtcmMaxNumberOfDscpProfiles=zyTrtcmMaxNumberOfDscpProfiles, zyTrtcmMode=zyTrtcmMode, zyTrtcmPortCir=zyTrtcmPortCir, zyxelTrtcmPortEntry=zyxelTrtcmPortEntry, zyTctcmState=zyTctcmState, zyTrtcmPortPir=zyTrtcmPortPir, zyxelTrtcmDscpProfileTable=zyxelTrtcmDscpProfileTable, zyTrtcmDscpProfileName=zyTrtcmDscpProfileName, zyTrtcmDscpProfileRowstatus=zyTrtcmDscpProfileRowstatus)
