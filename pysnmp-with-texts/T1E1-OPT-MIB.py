#
# PySNMP MIB module T1E1-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T1E1-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:15:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, MibIdentifier, ModuleIdentity, Gauge32, Unsigned32, Integer32, enterprises, ObjectIdentity, iso, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "MibIdentifier", "ModuleIdentity", "Gauge32", "Unsigned32", "Integer32", "enterprises", "ObjectIdentity", "iso", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500PCTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
cdx6500PSTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25))
class DisplayString(OctetString):
    pass

class PhysicalPortNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(49, 50)

class VirtualPortNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(100, 255)

cdx6500VPCTT1E1PortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3), )
if mibBuilder.loadTexts: cdx6500VPCTT1E1PortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1PortTable.setDescription('This table contains the T1/E1 Virtual Port Mapping Table parameters.')
cdx6500VPCTT1E1PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1), ).setIndexNames((0, "T1E1-OPT-MIB", "cdx6500VPCTT1E1CfgIndex"))
if mibBuilder.loadTexts: cdx6500VPCTT1E1PortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1PortEntry.setDescription('A Virtual T1/E1 Port Mapping Table Entry.Each entry contains the configuration parameters for a single T1/E1 virtual port.')
cdx6500VPCTT1E1CfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPortNumber.setDescription('This is a T1/E1 virtual port number this channel is associated with. A value of 0 implies that this parameter was skipped during configuration.')
cdx6500VPCTT1E1CfgPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 100))).clone(namedValues=NamedValues(("voice", 1), ("data", 2), ("switchedVoice", 3), ("switchedData", 4), ("bypassVoice", 5), ("bypassData", 6), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPortType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPortType.setDescription('Specifies the type of virtual port. voice : The virtual voice port operates on a configured DS0. data : The virtual data port operates on a configured DS0. switchedVoice : The virtual voice port operates on a DS0 determined by the ISDN/QSIG D Channel. switchedData : The virtual data port operates on a DS0 determined by the ISDN/QSIG D Channel. nc : Skipped during configuration.')
cdx6500VPCTT1E1CfgPhyPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPhyPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPhyPortNumber.setDescription('This is the E1 or T1 port number this channel is associated with. A value of 0 implies that this parameter was skipped during configuration.')
cdx6500VPCTT1E1CfgTimeSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgTimeSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgTimeSlotNumber.setDescription('Time slot assignment for the logical channel. T1 ports have time slots in the range (1..24) while E1 ports have time slots in the range (1..31). In addition, Time Slot 16 is not allowed (invalid) for E1 ports. A value of 0 implies that this parameter was skipped during configuration.')
cdx6500VPCTT1E1CfgDS0Rate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("ds056k", 1), ("ds064k", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgDS0Rate.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgDS0Rate.setDescription("Specifies the number of valid data bits within each DS0 for this port. ds056k : 7 bits of the DS0 contains data information, the 8th bit is used for 1's density. ds064k : All 8 bits of the DS0 contain data information. DS0 Rate for ports configured with port type `voice' is always 64K, while for ports configured with port type `data', it is 56K or 64K, the default being 56K. nc : Skipped during configuration.")
cdx6500VPCTT1E1CfgAggregateType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("t1e1", 1), ("so", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgAggregateType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgAggregateType.setDescription('Selects the type of physical interface for the Virtual Port. t1e1 : The physical interface is a T1 or E1 card. so : The physical interface is a SO card. nc : Skipped during configuration.')
cdx6500VPCTT1E1CfgSOPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgSOPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgSOPortNumber.setDescription('This is the port number of the SO interface this virtual port is associated with. A value of 0 implies that this parameter was skipped during configuration.')
cdx6500VPCTT1E1CfgBChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgBChannel.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgBChannel.setDescription('This is the B-channel on the SO interface this virtual port is associated with. A value of 0 implies that this parameter was skipped during configuration.')
cdx6500VPCTT1E1CfgLocalSubscriberAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgLocalSubscriberAddress.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgLocalSubscriberAddress.setDescription("Specifies the Local Subscriber Address for this virtual port. For Incoming Call: The Called Party number received by the aggregate interface is compared to this parameter. For Outgoing Call: This will be passed as the outgoing Calling Party number. Enter a trailing asterisk(*) as a wild-card. Use the space bar to blank the parameter. 1 to 20 characters (valid characters are 0 through 9, '-', ',', '/', '(', ')', and '*'). The characters '-', ',', '(', ')', and '/' are allowed only for ease of reading.")
cdx6500VPCTT1E1CfgNetSpecCall = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 9, 17, 100))).clone(namedValues=NamedValues(("none", 1), ("attSdn", 2), ("attMc800", 3), ("attMc", 4), ("ntFx", 5), ("ntTieTrunk", 6), ("attAccunet", 7), ("attInt800", 9), ("attMq", 17), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgNetSpecCall.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgNetSpecCall.setDescription('Select the network specific call-by-call feature. none : No network-specific facility. attSdn : AT&T Software Defined Network or Northern Tel Private Net. attMc800 : AT&T Megacom800 or Northern Tel InWats. attMc : AT&T Megcom or Northern Tel OutWats. ntFx : Northern Tel Foreign Exchange. ntTieTrunk : Northern Tel Tie Trunk. attAccunet : AT&T Accunet. attInt800 : AT&T International 800 Service. attMq : AT&T MultiQuest or NT TRO call. nc : Skipped during configuration.')
cdx6500VPCTT1E1CfgPartyNumberType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 7, 100))).clone(namedValues=NamedValues(("unknown", 1), ("international", 2), ("national", 3), ("subscriber", 5), ("abbreviated", 7), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPartyNumberType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPartyNumberType.setDescription('This is the Calling/Called party Number Type as defined by ITU-T. unknown : Unknown number type. international : International number. national : National number. subscriber : Subscriber number. abbreviated : Abbreviated number. nc : Skipped during configuration.')
cdx6500VPCTT1E1CfgPartyNumberPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 10, 100))).clone(namedValues=NamedValues(("unknown", 1), ("isdn", 2), ("telephony", 3), ("private", 10), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPartyNumberPlan.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPartyNumberPlan.setDescription('This is the Calling/Called party Numbering Plan as defined by ITU-T. unknown : Unknown numbering plan. isdn : Recommendation E.164/E.163. telephony : Telephony numbering plan. private : Private numbering plan. nc : Skipped during configuration.')
cdx6500VPCTT1E1CfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgIndex.setDescription('This is the entry number in the Virtual Port Mapping Table.')
mibBuilder.exportSymbols("T1E1-OPT-MIB", cdx6500VPCTT1E1CfgAggregateType=cdx6500VPCTT1E1CfgAggregateType, cdx6500VPCTT1E1CfgSOPortNumber=cdx6500VPCTT1E1CfgSOPortNumber, VirtualPortNumber=VirtualPortNumber, cdx6500VPCTT1E1CfgNetSpecCall=cdx6500VPCTT1E1CfgNetSpecCall, cdx6500VPCTT1E1CfgPhyPortNumber=cdx6500VPCTT1E1CfgPhyPortNumber, cdx6500VPCTT1E1CfgPartyNumberType=cdx6500VPCTT1E1CfgPartyNumberType, cdx6500VPCTT1E1CfgPortNumber=cdx6500VPCTT1E1CfgPortNumber, cdx6500=cdx6500, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500VPCTT1E1CfgLocalSubscriberAddress=cdx6500VPCTT1E1CfgLocalSubscriberAddress, cdx6500VPCTT1E1CfgPortType=cdx6500VPCTT1E1CfgPortType, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500VPCTT1E1CfgBChannel=cdx6500VPCTT1E1CfgBChannel, cdx6500PCTT1E1PortTable=cdx6500PCTT1E1PortTable, cdx6500VPCTT1E1PortEntry=cdx6500VPCTT1E1PortEntry, cdx6500Configuration=cdx6500Configuration, DisplayString=DisplayString, cdx6500VPCTT1E1CfgTimeSlotNumber=cdx6500VPCTT1E1CfgTimeSlotNumber, cdx6500VPCTT1E1CfgPartyNumberPlan=cdx6500VPCTT1E1CfgPartyNumberPlan, cdx6500VPCTT1E1CfgIndex=cdx6500VPCTT1E1CfgIndex, PhysicalPortNumber=PhysicalPortNumber, cdx6500VPCTT1E1PortTable=cdx6500VPCTT1E1PortTable, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500PSTT1E1PortTable=cdx6500PSTT1E1PortTable, cdx6500VPCTT1E1CfgDS0Rate=cdx6500VPCTT1E1CfgDS0Rate, cdxProductSpecific=cdxProductSpecific, codex=codex, cdx6500Statistics=cdx6500Statistics)
