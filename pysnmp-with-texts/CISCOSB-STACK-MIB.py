#
# PySNMP MIB module CISCOSB-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-STACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:23:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter64, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, Unsigned32, NotificationType, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "NotificationType", "iso", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rlStack = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107))
rlStack.setRevisions(('2005-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlStack.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlStack.setLastUpdated('200504140000Z')
if mibBuilder.loadTexts: rlStack.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlStack.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlStack.setDescription('The private MIB module definition for stack.')
class StackMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("standalone", 1), ("native", 2), ("basic-hybrid", 3), ("advanced-hybrid", 4), ("advanced-hybrid-XG", 5))

class PortsPair(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("pair-s1s2", 1), ("pair-s3s4", 2), ("pair-s1s25G", 3), ("pair-s1s2Xg", 4), ("pair-lionXg", 5))

class HybridStackPortSpeed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("port-speed-1G", 1), ("port-speed-5G", 2), ("port-speed-10G", 3), ("port-speed-auto", 4), ("port-speed-down", 5))

class HybridStackDeviceMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mode-L2", 1), ("mode-L3", 2))

rlStackActiveUnitIdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1), )
if mibBuilder.loadTexts: rlStackActiveUnitIdTable.setStatus('current')
if mibBuilder.loadTexts: rlStackActiveUnitIdTable.setDescription(' The table listing the active unit id of the requested unit.')
rlStackActiveUnitIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1), ).setIndexNames((0, "CISCOSB-STACK-MIB", "rlStackCurrentUnitId"))
if mibBuilder.loadTexts: rlStackActiveUnitIdEntry.setStatus('current')
if mibBuilder.loadTexts: rlStackActiveUnitIdEntry.setDescription(' An entry in the rlStackActiveUnitIdTable.')
rlStackCurrentUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rlStackCurrentUnitId.setStatus('current')
if mibBuilder.loadTexts: rlStackCurrentUnitId.setDescription('The unit number device, which is the active unit id')
rlStackActiveUnitIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackActiveUnitIdAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackActiveUnitIdAfterReset.setDescription('Indicates the unit id that will be after reset.')
rlStackUnitModeAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackUnitModeAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackUnitModeAfterReset.setDescription('set unit type that will be after reset, standalone or stack.')
rlStackUnitMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackUnitMode.setStatus('current')
if mibBuilder.loadTexts: rlStackUnitMode.setDescription('show unit type standalone or stack.')
rlStackUnitMacAddressAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackUnitMacAddressAfterReset.setReference('IEEE 802.1D-1990: Sections 6.4.1.1.3 and 3.12.5')
if mibBuilder.loadTexts: rlStackUnitMacAddressAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackUnitMacAddressAfterReset.setDescription('The MAC address used by this bridge after rest.')
rlStackHybridTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5), )
if mibBuilder.loadTexts: rlStackHybridTable.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridTable.setDescription(' The table listing information required for hybrid stack.')
rlStackHybridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1), ).setIndexNames((0, "CISCOSB-STACK-MIB", "rlStackHybridUnitId"))
if mibBuilder.loadTexts: rlStackHybridEntry.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridEntry.setDescription(' An entry in the rlStackActiveUnitIdTable.')
rlStackHybridUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: rlStackHybridUnitId.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridUnitId.setDescription('The unit number device, which is the active unit id')
rlStackHybridStackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 2), StackMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackHybridStackMode.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridStackMode.setDescription('Indicates the unit stack mode.')
rlStackHybridPortsPair = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 3), PortsPair()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackHybridPortsPair.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridPortsPair.setDescription('Indicates the PortsPair.')
rlStackHybridPortNo1speed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 4), HybridStackPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackHybridPortNo1speed.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridPortNo1speed.setDescription('Indicates the rlStackHybridPortNo1speed.')
rlStackHybridPortNo2speed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 5), HybridStackPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackHybridPortNo2speed.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridPortNo2speed.setDescription('Indicates the rlStackHybridPortNo2speed.')
rlStackHybridUnitIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridUnitIdAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridUnitIdAfterReset.setDescription('Indicates the unit id that will be after reset.')
rlStackHybridStackModeAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 7), StackMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridStackModeAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridStackModeAfterReset.setDescription('Indicates the unit stack mode that will be after reset.')
rlStackHybridPortsPairAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 8), PortsPair()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridPortsPairAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridPortsPairAfterReset.setDescription('Indicates the PortsPair that will be after reset.')
rlStackHybridPortNo1speedAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 9), HybridStackPortSpeed()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridPortNo1speedAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridPortNo1speedAfterReset.setDescription('Indicates the HybridStackPortSpeed that will be after reset.')
rlStackHybridPortNo2speedAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 10), HybridStackPortSpeed()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridPortNo2speedAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridPortNo2speedAfterReset.setDescription('Indicates the HybridStackPortSpeed that will be after reset.')
rlStackHybridDeleteStartupAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackHybridDeleteStartupAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridDeleteStartupAfterReset.setDescription('Indicates whether the startup configuration is deleted after reset.')
rlStackHybridDeviceModeAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 12), HybridStackDeviceMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridDeviceModeAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridDeviceModeAfterReset.setDescription('Indicates Device mode (Layer2 or Layer3) after reset.')
rlStackHybridXgPortNo1Num = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackHybridXgPortNo1Num.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridXgPortNo1Num.setDescription('Indicates the 1st stack cascade active port number.')
rlStackHybridXgPortNo1NumAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridXgPortNo1NumAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridXgPortNo1NumAfterReset.setDescription('Indicates the 1st stack cascade port number that will be after reset.')
rlStackHybridXgPortNo2Num = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackHybridXgPortNo2Num.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridXgPortNo2Num.setDescription('Indicates the 2nd stack cascade active port number.')
rlStackHybridXgPortNo2NumAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107, 5, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackHybridXgPortNo2NumAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlStackHybridXgPortNo2NumAfterReset.setDescription('Indicates the 2nd stack cascade port number that will be after reset.')
mibBuilder.exportSymbols("CISCOSB-STACK-MIB", rlStackHybridPortNo1speed=rlStackHybridPortNo1speed, rlStackUnitMode=rlStackUnitMode, rlStackHybridStackModeAfterReset=rlStackHybridStackModeAfterReset, rlStackActiveUnitIdTable=rlStackActiveUnitIdTable, rlStackHybridPortNo1speedAfterReset=rlStackHybridPortNo1speedAfterReset, rlStackHybridDeviceModeAfterReset=rlStackHybridDeviceModeAfterReset, rlStack=rlStack, PortsPair=PortsPair, rlStackHybridPortNo2speed=rlStackHybridPortNo2speed, rlStackHybridXgPortNo1NumAfterReset=rlStackHybridXgPortNo1NumAfterReset, rlStackActiveUnitIdAfterReset=rlStackActiveUnitIdAfterReset, rlStackHybridTable=rlStackHybridTable, rlStackHybridUnitId=rlStackHybridUnitId, rlStackHybridPortsPairAfterReset=rlStackHybridPortsPairAfterReset, rlStackHybridEntry=rlStackHybridEntry, rlStackHybridXgPortNo2NumAfterReset=rlStackHybridXgPortNo2NumAfterReset, rlStackHybridStackMode=rlStackHybridStackMode, rlStackHybridPortNo2speedAfterReset=rlStackHybridPortNo2speedAfterReset, HybridStackDeviceMode=HybridStackDeviceMode, rlStackUnitModeAfterReset=rlStackUnitModeAfterReset, PYSNMP_MODULE_ID=rlStack, HybridStackPortSpeed=HybridStackPortSpeed, rlStackHybridDeleteStartupAfterReset=rlStackHybridDeleteStartupAfterReset, rlStackHybridXgPortNo2Num=rlStackHybridXgPortNo2Num, rlStackCurrentUnitId=rlStackCurrentUnitId, rlStackActiveUnitIdEntry=rlStackActiveUnitIdEntry, rlStackHybridPortsPair=rlStackHybridPortsPair, rlStackHybridXgPortNo1Num=rlStackHybridXgPortNo1Num, rlStackHybridUnitIdAfterReset=rlStackHybridUnitIdAfterReset, rlStackUnitMacAddressAfterReset=rlStackUnitMacAddressAfterReset, StackMode=StackMode)
