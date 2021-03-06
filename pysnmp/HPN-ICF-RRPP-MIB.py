#
# PySNMP MIB module HPN-ICF-RRPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-RRPP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Integer32, TimeTicks, IpAddress, Gauge32, MibIdentifier, Bits, iso, ObjectIdentity, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "iso", "ObjectIdentity", "NotificationType", "Unsigned32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hpnicfRrpp = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45))
if mibBuilder.loadTexts: hpnicfRrpp.setLastUpdated('200412020000Z')
if mibBuilder.loadTexts: hpnicfRrpp.setOrganization('')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hpnicfRrppScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1))
hpnicfRrppEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRrppEnableStatus.setStatus('current')
hpnicfRrppPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone(hexValue="303030464532303346443735")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRrppPassword.setStatus('current')
hpnicfRrppPasswordType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfRrppPasswordType.setStatus('current')
hpnicfRrppProtectVlanConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("instance", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppProtectVlanConfigMode.setStatus('current')
hpnicfRrppTable = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2))
hpnicfRrppDomainTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1), )
if mibBuilder.loadTexts: hpnicfRrppDomainTable.setStatus('current')
hpnicfRrppDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"))
if mibBuilder.loadTexts: hpnicfRrppDomainEntry.setStatus('current')
hpnicfRrppDomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfRrppDomainID.setStatus('current')
hpnicfRrppDomainControlVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 4094), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainControlVlanID.setStatus('current')
hpnicfRrppDomainHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainHelloTime.setStatus('current')
hpnicfRrppDomainFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainFailTime.setStatus('current')
hpnicfRrppDomainRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainRowStatus.setStatus('current')
hpnicfRrppDomainInstanceListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainInstanceListLow.setStatus('current')
hpnicfRrppDomainInstanceListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainInstanceListHigh.setStatus('current')
hpnicfRrppDomainProtectVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainProtectVlanListLow.setStatus('current')
hpnicfRrppDomainProtectVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppDomainProtectVlanListHigh.setStatus('current')
hpnicfRrppRingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2), )
if mibBuilder.loadTexts: hpnicfRrppRingTable.setStatus('current')
hpnicfRrppRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"), (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
if mibBuilder.loadTexts: hpnicfRrppRingEntry.setStatus('current')
hpnicfRrppRingID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfRrppRingID.setStatus('current')
hpnicfRrppRingEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 2), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppRingEnableStatus.setStatus('current')
hpnicfRrppRingActive = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppRingActive.setStatus('current')
hpnicfRrppRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("health", 2), ("fault", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppRingState.setStatus('current')
hpnicfRrppRingNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("master", 1), ("transit", 2), ("edge", 3), ("assistantEdge", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppRingNodeMode.setStatus('current')
hpnicfRrppRingPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppRingPrimaryPort.setStatus('current')
hpnicfRrppRingSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppRingSecondaryPort.setStatus('current')
hpnicfRrppRingLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("majorRing", 1), ("subRing", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppRingLevel.setStatus('current')
hpnicfRrppRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRrppRingRowStatus.setStatus('current')
hpnicfRrppPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3), )
if mibBuilder.loadTexts: hpnicfRrppPortTable.setStatus('current')
hpnicfRrppPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"), (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"), (0, "HPN-ICF-RRPP-MIB", "hpnicfRrppPortID"))
if mibBuilder.loadTexts: hpnicfRrppPortEntry.setStatus('current')
hpnicfRrppPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfRrppPortID.setStatus('current')
hpnicfRrppPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("common", 3), ("edge", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRole.setStatus('current')
hpnicfRrppPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("unblocked", 2), ("blocked", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortState.setStatus('current')
hpnicfRrppPortRXError = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXError.setStatus('current')
hpnicfRrppPortRXHello = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXHello.setStatus('current')
hpnicfRrppPortRXLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXLinkUp.setStatus('current')
hpnicfRrppPortRXLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXLinkDown.setStatus('current')
hpnicfRrppPortRXCommonFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXCommonFlush.setStatus('current')
hpnicfRrppPortRXCompleteFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXCompleteFlush.setStatus('current')
hpnicfRrppPortTXHello = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortTXHello.setStatus('current')
hpnicfRrppPortTXLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortTXLinkUp.setStatus('current')
hpnicfRrppPortTXLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortTXLinkDown.setStatus('current')
hpnicfRrppPortTXCommonFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortTXCommonFlush.setStatus('current')
hpnicfRrppPortTXCompleteFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortTXCompleteFlush.setStatus('current')
hpnicfRrppPortRXEdgeHello = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXEdgeHello.setStatus('current')
hpnicfRrppPortRXMajorFault = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortRXMajorFault.setStatus('current')
hpnicfRrppPortTXEdgeHello = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortTXEdgeHello.setStatus('current')
hpnicfRrppPortTXMajorFault = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRrppPortTXMajorFault.setStatus('current')
hpnicfRrppNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3))
hpnicfRrppRingRecover = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 1)).setObjects(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"), ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
if mibBuilder.loadTexts: hpnicfRrppRingRecover.setStatus('current')
hpnicfRrppRingFail = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 2)).setObjects(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"), ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
if mibBuilder.loadTexts: hpnicfRrppRingFail.setStatus('current')
hpnicfRrppMultiMaster = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 3)).setObjects(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"), ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
if mibBuilder.loadTexts: hpnicfRrppMultiMaster.setStatus('current')
hpnicfRrppMajorFault = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45, 3, 4)).setObjects(("HPN-ICF-RRPP-MIB", "hpnicfRrppDomainID"), ("HPN-ICF-RRPP-MIB", "hpnicfRrppRingID"))
if mibBuilder.loadTexts: hpnicfRrppMajorFault.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-RRPP-MIB", hpnicfRrppRingID=hpnicfRrppRingID, hpnicfRrppRingActive=hpnicfRrppRingActive, hpnicfRrppPortRXMajorFault=hpnicfRrppPortRXMajorFault, hpnicfRrppDomainFailTime=hpnicfRrppDomainFailTime, hpnicfRrppPortRXError=hpnicfRrppPortRXError, hpnicfRrppPortTXMajorFault=hpnicfRrppPortTXMajorFault, hpnicfRrppRingSecondaryPort=hpnicfRrppRingSecondaryPort, hpnicfRrppRingNodeMode=hpnicfRrppRingNodeMode, hpnicfRrppPortRXHello=hpnicfRrppPortRXHello, hpnicfRrppDomainRowStatus=hpnicfRrppDomainRowStatus, hpnicfRrppRingRowStatus=hpnicfRrppRingRowStatus, hpnicfRrppPortTXCompleteFlush=hpnicfRrppPortTXCompleteFlush, hpnicfRrppProtectVlanConfigMode=hpnicfRrppProtectVlanConfigMode, hpnicfRrpp=hpnicfRrpp, hpnicfRrppRingEnableStatus=hpnicfRrppRingEnableStatus, hpnicfRrppRingLevel=hpnicfRrppRingLevel, hpnicfRrppPortTable=hpnicfRrppPortTable, hpnicfRrppRingFail=hpnicfRrppRingFail, hpnicfRrppPortTXLinkDown=hpnicfRrppPortTXLinkDown, hpnicfRrppNotifications=hpnicfRrppNotifications, hpnicfRrppRingTable=hpnicfRrppRingTable, hpnicfRrppDomainHelloTime=hpnicfRrppDomainHelloTime, hpnicfRrppRingPrimaryPort=hpnicfRrppRingPrimaryPort, hpnicfRrppDomainInstanceListLow=hpnicfRrppDomainInstanceListLow, hpnicfRrppTable=hpnicfRrppTable, hpnicfRrppDomainProtectVlanListHigh=hpnicfRrppDomainProtectVlanListHigh, hpnicfRrppDomainInstanceListHigh=hpnicfRrppDomainInstanceListHigh, hpnicfRrppRingRecover=hpnicfRrppRingRecover, hpnicfRrppMultiMaster=hpnicfRrppMultiMaster, hpnicfRrppPortRXLinkDown=hpnicfRrppPortRXLinkDown, hpnicfRrppPortState=hpnicfRrppPortState, hpnicfRrppPasswordType=hpnicfRrppPasswordType, hpnicfRrppEnableStatus=hpnicfRrppEnableStatus, hpnicfRrppDomainControlVlanID=hpnicfRrppDomainControlVlanID, hpnicfRrppPortID=hpnicfRrppPortID, hpnicfRrppPortRXLinkUp=hpnicfRrppPortRXLinkUp, hpnicfRrppPortTXEdgeHello=hpnicfRrppPortTXEdgeHello, EnabledStatus=EnabledStatus, PYSNMP_MODULE_ID=hpnicfRrpp, hpnicfRrppRingState=hpnicfRrppRingState, hpnicfRrppPortTXHello=hpnicfRrppPortTXHello, hpnicfRrppDomainID=hpnicfRrppDomainID, hpnicfRrppPortRXCommonFlush=hpnicfRrppPortRXCommonFlush, hpnicfRrppDomainTable=hpnicfRrppDomainTable, hpnicfRrppDomainEntry=hpnicfRrppDomainEntry, hpnicfRrppPortTXCommonFlush=hpnicfRrppPortTXCommonFlush, hpnicfRrppRingEntry=hpnicfRrppRingEntry, hpnicfRrppPortTXLinkUp=hpnicfRrppPortTXLinkUp, hpnicfRrppPortEntry=hpnicfRrppPortEntry, hpnicfRrppPortRole=hpnicfRrppPortRole, hpnicfRrppPortRXEdgeHello=hpnicfRrppPortRXEdgeHello, hpnicfRrppMajorFault=hpnicfRrppMajorFault, hpnicfRrppPortRXCompleteFlush=hpnicfRrppPortRXCompleteFlush, hpnicfRrppScalarGroup=hpnicfRrppScalarGroup, hpnicfRrppPassword=hpnicfRrppPassword, hpnicfRrppDomainProtectVlanListLow=hpnicfRrppDomainProtectVlanListLow)
