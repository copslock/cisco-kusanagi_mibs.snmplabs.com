#
# PySNMP MIB module AIILINKTABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AIILINKTABLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Bits, Counter64, iso, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, TimeTicks, ModuleIdentity, enterprises, Unsigned32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Counter64", "iso", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSLC2 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16))
aiLink = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 16, 2))
if mibBuilder.loadTexts: aiLink.setLastUpdated('9912101700Z')
if mibBuilder.loadTexts: aiLink.setOrganization('Applied Innovation Inc.')
class AIIifType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 6, 18, 19, 22, 23, 28, 32, 37, 38, 40, 48, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033))
    namedValues = NamedValues(("other", 1), ("ethernet-csmacd", 6), ("ds1", 18), ("e1", 19), ("propPointToPointSerial", 22), ("ppp", 23), ("slip", 28), ("frameRelay", 32), ("atm", 37), ("miox25", 38), ("x25ple", 40), ("modem", 48), ("tl1", 1024), ("ttl1", 1025), ("e2a", 1026), ("tbos", 1027), ("tabs", 1028), ("asyncTl1", 1029), ("bridge", 1030), ("sm100BaseFX", 1031), ("gasp", 1032), ("pppAsynchronous", 1033))

aiLinkTable = MibTable((1, 3, 6, 1, 4, 1, 539, 16, 2, 1), )
if mibBuilder.loadTexts: aiLinkTable.setStatus('current')
aiLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1), ).setIndexNames((0, "AIILINKTABLE-MIB", "aiLinkIndex"))
if mibBuilder.loadTexts: aiLinkEntry.setStatus('current')
aiLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkIndex.setStatus('current')
aiLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 2), AIIifType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkType.setStatus('current')
aiLinkDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkDescr.setStatus('current')
aiLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 4), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkIfIndex.setStatus('current')
aiLinkIfIndex1 = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 5), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkIfIndex1.setStatus('current')
aiLinkIfIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 6), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkIfIndex2.setStatus('current')
aiLinkIfIndex3 = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 7), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkIfIndex3.setStatus('current')
aiLinkIfIndex4 = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 8), IfIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkIfIndex4.setStatus('current')
aiLinkPhysIf = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("rs232", 1), ("rs530", 2), ("v35", 3), ("ethernet-csmacd", 4), ("ds1", 5), ("e1", 6), ("fiber", 7), ("rs530m", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkPhysIf.setStatus('current')
aiLinkX25Table = MibTable((1, 3, 6, 1, 4, 1, 539, 16, 2, 2), )
if mibBuilder.loadTexts: aiLinkX25Table.setStatus('current')
aiLinkX25Entry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1), ).setIndexNames((0, "AIILINKTABLE-MIB", "aiLinkX25Index"))
if mibBuilder.loadTexts: aiLinkX25Entry.setStatus('current')
aiLinkX25Index = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkX25Index.setStatus('current')
aiLinkX25Negotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkX25Negotiation.setStatus('current')
aiLinkX25LinkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("passive", 2), ("extended", 3))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkX25LinkMode.setStatus('current')
aiLinkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 2, 3))
aiLinkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 1))
aiLinkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 2))
aiLinkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 2, 1)).setObjects(("AIILINKTABLE-MIB", "aiLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aiLinkCompliance = aiLinkCompliance.setStatus('current')
aiLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 1, 1)).setObjects(("AIILINKTABLE-MIB", "aiLinkIndex"), ("AIILINKTABLE-MIB", "aiLinkType"), ("AIILINKTABLE-MIB", "aiLinkDescr"), ("AIILINKTABLE-MIB", "aiLinkIfIndex"), ("AIILINKTABLE-MIB", "aiLinkIfIndex1"), ("AIILINKTABLE-MIB", "aiLinkIfIndex2"), ("AIILINKTABLE-MIB", "aiLinkIfIndex3"), ("AIILINKTABLE-MIB", "aiLinkIfIndex4"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aiLinkGroup = aiLinkGroup.setStatus('current')
aiLinkT1Table = MibTable((1, 3, 6, 1, 4, 1, 539, 16, 2, 4), )
if mibBuilder.loadTexts: aiLinkT1Table.setStatus('current')
aiLinkT1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1), ).setIndexNames((0, "AIILINKTABLE-MIB", "aiLinkT1Index"))
if mibBuilder.loadTexts: aiLinkT1Entry.setStatus('current')
aiLinkT1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkT1Index.setStatus('current')
aiLinkT1LineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("lbo0to133ft", 1), ("lbo133to266ft", 2), ("lbo266to399ft", 3), ("lbo399to533ft", 4), ("lbo533to655ft", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkT1LineBuildOut.setStatus('current')
aiLinkT1TimeslotSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tss56K", 1), ("tss64K", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkT1TimeslotSpeed.setStatus('current')
aiLinkT1TimeslotsString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkT1TimeslotsString.setStatus('current')
aiLinkT1Timeslots = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkT1Timeslots.setStatus('current')
aiLinkE1Table = MibTable((1, 3, 6, 1, 4, 1, 539, 16, 2, 5), )
if mibBuilder.loadTexts: aiLinkE1Table.setStatus('current')
aiLinkE1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1), ).setIndexNames((0, "AIILINKTABLE-MIB", "aiLinkE1Index"))
if mibBuilder.loadTexts: aiLinkE1Entry.setStatus('current')
aiLinkE1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkE1Index.setStatus('current')
aiLinkE1TimeslotSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tss56K", 1), ("tss64K", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkE1TimeslotSpeed.setStatus('current')
aiLinkE1TimeslotsString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLinkE1TimeslotsString.setStatus('current')
aiLinkE1Timeslots = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLinkE1Timeslots.setStatus('current')
mibBuilder.exportSymbols("AIILINKTABLE-MIB", aiLinkGroup=aiLinkGroup, aiLinkIfIndex1=aiLinkIfIndex1, aiLinkX25Index=aiLinkX25Index, aii=aii, aiLinkT1Entry=aiLinkT1Entry, aiLinkCompliance=aiLinkCompliance, aiLinkDescr=aiLinkDescr, aiLinkT1Timeslots=aiLinkT1Timeslots, aiLinkIfIndex3=aiLinkIfIndex3, aiLinkT1Index=aiLinkT1Index, aiLinkX25Entry=aiLinkX25Entry, aiLinkTable=aiLinkTable, aiLinkConformance=aiLinkConformance, aiLinkEntry=aiLinkEntry, aiLinkE1Table=aiLinkE1Table, aiLinkIndex=aiLinkIndex, aiLinkIfIndex4=aiLinkIfIndex4, aiLinkE1Index=aiLinkE1Index, aiLinkE1Timeslots=aiLinkE1Timeslots, PositiveInteger=PositiveInteger, aiLinkT1TimeslotSpeed=aiLinkT1TimeslotSpeed, aiSLC2=aiSLC2, aiLinkE1TimeslotsString=aiLinkE1TimeslotsString, aiLinkType=aiLinkType, aiLinkT1TimeslotsString=aiLinkT1TimeslotsString, aiLinkX25Negotiation=aiLinkX25Negotiation, IfIndexType=IfIndexType, PYSNMP_MODULE_ID=aiLink, aiLinkIfIndex2=aiLinkIfIndex2, aiLinkT1Table=aiLinkT1Table, aiLinkGroups=aiLinkGroups, aiLinkE1Entry=aiLinkE1Entry, aiLinkX25LinkMode=aiLinkX25LinkMode, aiLinkCompliances=aiLinkCompliances, aiLinkPhysIf=aiLinkPhysIf, aiLink=aiLink, aiLinkE1TimeslotSpeed=aiLinkE1TimeslotSpeed, aiLinkIfIndex=aiLinkIfIndex, aiLinkT1LineBuildOut=aiLinkT1LineBuildOut, aiLinkX25Table=aiLinkX25Table, AIIifType=AIIifType)
