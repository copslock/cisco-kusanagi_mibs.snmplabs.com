#
# PySNMP MIB module MPLS-LSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-LSR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:04:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressType, InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressIPv6", "InetAddressIPv4")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, experimental, Unsigned32, Counter32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, TimeTicks, NotificationType, ObjectIdentity, Gauge32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "experimental", "Unsigned32", "Counter32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "ObjectIdentity", "Gauge32", "IpAddress", "MibIdentifier")
DisplayString, RowStatus, StorageType, RowPointer, TimeStamp, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "RowPointer", "TimeStamp", "TextualConvention", "TruthValue")
mplsLsrMIB = ModuleIdentity((1, 3, 6, 1, 3, 96))
mplsLsrMIB.setRevisions(('2000-07-12 12:00', '2000-07-07 12:00', '2000-04-26 12:00', '2000-04-21 12:00', '2000-03-06 12:00', '2000-02-16 12:00', '1999-06-16 12:00',))
if mibBuilder.loadTexts: mplsLsrMIB.setLastUpdated('200007121200Z')
if mibBuilder.loadTexts: mplsLsrMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class MplsLSPID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class MplsLabel(TextualConvention, Integer32):
    reference = '1. MPLS Label Stack Encoding, Rosen et al, draft- ietf-mpls-label-encaps-07.txt, March 2000. 2. Use of Label Switching on Frame Relay Networks, Conta et al, draft-ietf-mpls-fr-03.txt, Nov. 1998. 3. MPLS using LDP and ATM VC switching, Davie et al, draft-ietf-mpls-atm-02.txt, April 1999.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class MplsBitRate(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsBurstSize(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsObjectOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("snmp", 2), ("ldp", 3), ("rsvp", 4), ("crldp", 5), ("policyAgent", 6), ("unknown", 7))

mplsLsrObjects = MibIdentifier((1, 3, 6, 1, 3, 96, 1))
mplsLsrNotifications = MibIdentifier((1, 3, 6, 1, 3, 96, 2))
mplsLsrNotifyPrefix = MibIdentifier((1, 3, 6, 1, 3, 96, 2, 0))
mplsLsrConformance = MibIdentifier((1, 3, 6, 1, 3, 96, 3))
mplsInterfaceConfTable = MibTable((1, 3, 6, 1, 3, 96, 1, 1), )
if mibBuilder.loadTexts: mplsInterfaceConfTable.setStatus('current')
mplsInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-MIB", "mplsInterfaceConfIndex"))
if mibBuilder.loadTexts: mplsInterfaceConfEntry.setStatus('current')
mplsInterfaceConfIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: mplsInterfaceConfIndex.setStatus('current')
mplsInterfaceLabelMinIn = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 2), MplsLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceLabelMinIn.setStatus('current')
mplsInterfaceLabelMaxIn = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 3), MplsLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceLabelMaxIn.setStatus('current')
mplsInterfaceLabelMinOut = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 4), MplsLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceLabelMinOut.setStatus('current')
mplsInterfaceLabelMaxOut = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 5), MplsLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceLabelMaxOut.setStatus('current')
mplsInterfaceTotalBandwidth = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 6), MplsBitRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceTotalBandwidth.setStatus('current')
mplsInterfaceAvailableBandwidth = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 7), MplsBitRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceAvailableBandwidth.setStatus('current')
mplsInterfaceLabelParticipationType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 8), Bits().clone(namedValues=NamedValues(("perPlatform", 0), ("perInterface", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceLabelParticipationType.setStatus('current')
mplsInterfaceConfStorageType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 1, 1, 9), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsInterfaceConfStorageType.setStatus('current')
mplsInterfacePerfTable = MibTable((1, 3, 6, 1, 3, 96, 1, 2), )
if mibBuilder.loadTexts: mplsInterfacePerfTable.setStatus('current')
mplsInterfacePerfEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 2, 1), )
mplsInterfaceConfEntry.registerAugmentions(("MPLS-LSR-MIB", "mplsInterfacePerfEntry"))
mplsInterfacePerfEntry.setIndexNames(*mplsInterfaceConfEntry.getIndexNames())
if mibBuilder.loadTexts: mplsInterfacePerfEntry.setStatus('current')
mplsInterfaceInLabelsUsed = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceInLabelsUsed.setStatus('current')
mplsInterfaceFailedLabelLookup = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceFailedLabelLookup.setStatus('current')
mplsInterfaceOutLabelsUsed = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceOutLabelsUsed.setStatus('current')
mplsInterfaceOutFragments = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInterfaceOutFragments.setStatus('current')
mplsInSegmentTable = MibTable((1, 3, 6, 1, 3, 96, 1, 3), )
if mibBuilder.loadTexts: mplsInSegmentTable.setStatus('current')
mplsInSegmentEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 3, 1), ).setIndexNames((0, "MPLS-LSR-MIB", "mplsInSegmentIfIndex"), (0, "MPLS-LSR-MIB", "mplsInSegmentLabel"))
if mibBuilder.loadTexts: mplsInSegmentEntry.setStatus('current')
mplsInSegmentIfIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 1), InterfaceIndexOrZero()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsInSegmentIfIndex.setStatus('current')
mplsInSegmentLabel = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 2), MplsLabel()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsInSegmentLabel.setStatus('current')
mplsInSegmentNPop = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsInSegmentNPop.setStatus('current')
mplsInSegmentAddrFamily = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 4), AddressFamilyNumbers().clone('other')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsInSegmentAddrFamily.setStatus('current')
mplsInSegmentXCIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInSegmentXCIndex.setStatus('current')
mplsInSegmentOwner = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 6), MplsObjectOwner().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsInSegmentOwner.setStatus('current')
mplsInSegmentTrafficParamPtr = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 7), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsInSegmentTrafficParamPtr.setStatus('current')
mplsInSegmentRowStatus = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsInSegmentRowStatus.setStatus('current')
mplsInSegmentStorageType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 3, 1, 9), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsInSegmentStorageType.setStatus('current')
mplsInSegmentPerfTable = MibTable((1, 3, 6, 1, 3, 96, 1, 4), )
if mibBuilder.loadTexts: mplsInSegmentPerfTable.setStatus('current')
mplsInSegmentPerfEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 4, 1), )
mplsInSegmentEntry.registerAugmentions(("MPLS-LSR-MIB", "mplsInSegmentPerfEntry"))
mplsInSegmentPerfEntry.setIndexNames(*mplsInSegmentEntry.getIndexNames())
if mibBuilder.loadTexts: mplsInSegmentPerfEntry.setStatus('current')
mplsInSegmentOctets = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInSegmentOctets.setStatus('current')
mplsInSegmentPackets = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInSegmentPackets.setStatus('current')
mplsInSegmentErrors = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInSegmentErrors.setStatus('current')
mplsInSegmentDiscards = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInSegmentDiscards.setStatus('current')
mplsInSegmentHCOctets = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInSegmentHCOctets.setStatus('current')
mplsInSegmentPerfDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 4, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsInSegmentPerfDiscontinuityTime.setStatus('current')
mplsOutSegmentIndexNext = MibScalar((1, 3, 6, 1, 3, 96, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentIndexNext.setStatus('current')
mplsOutSegmentTable = MibTable((1, 3, 6, 1, 3, 96, 1, 6), )
if mibBuilder.loadTexts: mplsOutSegmentTable.setStatus('current')
mplsOutSegmentEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 6, 1), ).setIndexNames((0, "MPLS-LSR-MIB", "mplsOutSegmentIndex"))
if mibBuilder.loadTexts: mplsOutSegmentEntry.setStatus('current')
mplsOutSegmentIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsOutSegmentIndex.setStatus('current')
mplsOutSegmentIfIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentIfIndex.setStatus('current')
mplsOutSegmentPushTopLabel = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentPushTopLabel.setStatus('current')
mplsOutSegmentTopLabel = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 4), MplsLabel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentTopLabel.setStatus('current')
mplsOutSegmentNextHopIpAddrType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 5), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentNextHopIpAddrType.setStatus('current')
mplsOutSegmentNextHopIpv4Addr = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentNextHopIpv4Addr.setStatus('current')
mplsOutSegmentNextHopIpv6Addr = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 7), InetAddressIPv6()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentNextHopIpv6Addr.setStatus('current')
mplsOutSegmentXCIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentXCIndex.setStatus('current')
mplsOutSegmentOwner = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 9), MplsObjectOwner().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentOwner.setStatus('current')
mplsOutSegmentTrafficParamPtr = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 10), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentTrafficParamPtr.setStatus('current')
mplsOutSegmentRowStatus = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentRowStatus.setStatus('current')
mplsOutSegmentStorageType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 6, 1, 12), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsOutSegmentStorageType.setStatus('current')
mplsOutSegmentPerfTable = MibTable((1, 3, 6, 1, 3, 96, 1, 7), )
if mibBuilder.loadTexts: mplsOutSegmentPerfTable.setStatus('current')
mplsOutSegmentPerfEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 7, 1), )
mplsOutSegmentEntry.registerAugmentions(("MPLS-LSR-MIB", "mplsOutSegmentPerfEntry"))
mplsOutSegmentPerfEntry.setIndexNames(*mplsOutSegmentEntry.getIndexNames())
if mibBuilder.loadTexts: mplsOutSegmentPerfEntry.setStatus('current')
mplsOutSegmentOctets = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 7, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentOctets.setStatus('current')
mplsOutSegmentPackets = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentPackets.setStatus('current')
mplsOutSegmentErrors = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentErrors.setStatus('current')
mplsOutSegmentDiscards = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentDiscards.setStatus('current')
mplsOutSegmentHCOctets = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 7, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentHCOctets.setStatus('current')
mplsOutSegmentPerfDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 7, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsOutSegmentPerfDiscontinuityTime.setStatus('current')
mplsXCIndexNext = MibScalar((1, 3, 6, 1, 3, 96, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsXCIndexNext.setStatus('current')
mplsXCTable = MibTable((1, 3, 6, 1, 3, 96, 1, 9), )
if mibBuilder.loadTexts: mplsXCTable.setStatus('current')
mplsXCEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 9, 1), ).setIndexNames((0, "MPLS-LSR-MIB", "mplsXCIndex"), (0, "MPLS-LSR-MIB", "mplsInSegmentIfIndex"), (0, "MPLS-LSR-MIB", "mplsInSegmentLabel"), (0, "MPLS-LSR-MIB", "mplsOutSegmentIndex"))
if mibBuilder.loadTexts: mplsXCEntry.setStatus('current')
mplsXCIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsXCIndex.setStatus('current')
mplsXCLspId = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 2), MplsLSPID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCLspId.setStatus('current')
mplsXCLabelStackIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCLabelStackIndex.setStatus('current')
mplsXCIsPersistent = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCIsPersistent.setStatus('current')
mplsXCOwner = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 5), MplsObjectOwner()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCOwner.setStatus('current')
mplsXCRowStatus = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCRowStatus.setStatus('current')
mplsXCStorageType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 7), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCStorageType.setStatus('current')
mplsXCAdminStatus = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCAdminStatus.setStatus('current')
mplsXCOperStatus = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsXCOperStatus.setStatus('current')
mplsMaxLabelStackDepth = MibScalar((1, 3, 6, 1, 3, 96, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsMaxLabelStackDepth.setStatus('current')
mplsLabelStackIndexNext = MibScalar((1, 3, 6, 1, 3, 96, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLabelStackIndexNext.setStatus('current')
mplsLabelStackTable = MibTable((1, 3, 6, 1, 3, 96, 1, 12), )
if mibBuilder.loadTexts: mplsLabelStackTable.setStatus('current')
mplsLabelStackEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 12, 1), ).setIndexNames((0, "MPLS-LSR-MIB", "mplsLabelStackIndex"), (0, "MPLS-LSR-MIB", "mplsLabelStackLabelIndex"))
if mibBuilder.loadTexts: mplsLabelStackEntry.setStatus('current')
mplsLabelStackIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsLabelStackIndex.setStatus('current')
mplsLabelStackLabelIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsLabelStackLabelIndex.setStatus('current')
mplsLabelStackLabel = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 12, 1, 3), MplsLabel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLabelStackLabel.setStatus('current')
mplsLabelStackRowStatus = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 12, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLabelStackRowStatus.setStatus('current')
mplsLabelStackStorageType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 12, 1, 5), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLabelStackStorageType.setStatus('current')
mplsTrafficParamIndexNext = MibScalar((1, 3, 6, 1, 3, 96, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTrafficParamIndexNext.setStatus('current')
mplsTrafficParamTable = MibTable((1, 3, 6, 1, 3, 96, 1, 14), )
if mibBuilder.loadTexts: mplsTrafficParamTable.setStatus('current')
mplsTrafficParamEntry = MibTableRow((1, 3, 6, 1, 3, 96, 1, 14, 1), ).setIndexNames((0, "MPLS-LSR-MIB", "mplsTrafficParamIndex"))
if mibBuilder.loadTexts: mplsTrafficParamEntry.setStatus('current')
mplsTrafficParamIndex = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTrafficParamIndex.setStatus('current')
mplsTrafficParamMaxRate = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 14, 1, 2), MplsBitRate()).setUnits('kilobits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTrafficParamMaxRate.setStatus('current')
mplsTrafficParamMeanRate = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 14, 1, 3), MplsBitRate()).setUnits('kilobits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTrafficParamMeanRate.setStatus('current')
mplsTrafficParamMaxBurstSize = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 14, 1, 4), MplsBurstSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTrafficParamMaxBurstSize.setStatus('current')
mplsTrafficParamRowStatus = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 14, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTrafficParamRowStatus.setStatus('current')
mplsTrafficParamStorageType = MibTableColumn((1, 3, 6, 1, 3, 96, 1, 14, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTrafficParamStorageType.setStatus('current')
mplsXCTrapEnable = MibScalar((1, 3, 6, 1, 3, 96, 1, 15), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsXCTrapEnable.setStatus('current')
mplsXCUp = NotificationType((1, 3, 6, 1, 3, 96, 2, 0, 1)).setObjects(("MPLS-LSR-MIB", "mplsXCIndex"), ("MPLS-LSR-MIB", "mplsInSegmentIfIndex"), ("MPLS-LSR-MIB", "mplsInSegmentLabel"), ("MPLS-LSR-MIB", "mplsOutSegmentIndex"), ("MPLS-LSR-MIB", "mplsXCAdminStatus"), ("MPLS-LSR-MIB", "mplsXCOperStatus"))
if mibBuilder.loadTexts: mplsXCUp.setStatus('current')
mplsXCDown = NotificationType((1, 3, 6, 1, 3, 96, 2, 0, 2)).setObjects(("MPLS-LSR-MIB", "mplsXCIndex"), ("MPLS-LSR-MIB", "mplsInSegmentIfIndex"), ("MPLS-LSR-MIB", "mplsInSegmentLabel"), ("MPLS-LSR-MIB", "mplsOutSegmentIndex"), ("MPLS-LSR-MIB", "mplsXCAdminStatus"), ("MPLS-LSR-MIB", "mplsXCOperStatus"))
if mibBuilder.loadTexts: mplsXCDown.setStatus('current')
mplsLsrGroups = MibIdentifier((1, 3, 6, 1, 3, 96, 3, 1))
mplsLsrCompliances = MibIdentifier((1, 3, 6, 1, 3, 96, 3, 2))
mplsLsrModuleCompliance = ModuleCompliance((1, 3, 6, 1, 3, 96, 3, 2, 1)).setObjects(("MPLS-LSR-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-MIB", "mplsXCGroup"), ("MPLS-LSR-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-MIB", "mplsPerfGroup"), ("MPLS-LSR-MIB", "mplsSegmentDiscontinuityGroup"), ("MPLS-LSR-MIB", "mplsHCInSegmentPerfGroup"), ("MPLS-LSR-MIB", "mplsHCOutSegmentPerfGroup"), ("MPLS-LSR-MIB", "mplsTrafficParamGroup"), ("MPLS-LSR-MIB", "mplsXCIsPersistentGroup"), ("MPLS-LSR-MIB", "mplsXCIsNotPersistentGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrModuleCompliance = mplsLsrModuleCompliance.setStatus('current')
mplsInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 1)).setObjects(("MPLS-LSR-MIB", "mplsInterfaceLabelMinIn"), ("MPLS-LSR-MIB", "mplsInterfaceLabelMaxIn"), ("MPLS-LSR-MIB", "mplsInterfaceLabelMinOut"), ("MPLS-LSR-MIB", "mplsInterfaceLabelMaxOut"), ("MPLS-LSR-MIB", "mplsInterfaceTotalBandwidth"), ("MPLS-LSR-MIB", "mplsInterfaceAvailableBandwidth"), ("MPLS-LSR-MIB", "mplsInterfaceLabelParticipationType"), ("MPLS-LSR-MIB", "mplsInterfaceConfStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsInterfaceGroup = mplsInterfaceGroup.setStatus('current')
mplsInSegmentGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 2)).setObjects(("MPLS-LSR-MIB", "mplsInSegmentNPop"), ("MPLS-LSR-MIB", "mplsInSegmentAddrFamily"), ("MPLS-LSR-MIB", "mplsInSegmentXCIndex"), ("MPLS-LSR-MIB", "mplsInSegmentOctets"), ("MPLS-LSR-MIB", "mplsInSegmentDiscards"), ("MPLS-LSR-MIB", "mplsInSegmentOwner"), ("MPLS-LSR-MIB", "mplsInSegmentRowStatus"), ("MPLS-LSR-MIB", "mplsInSegmentStorageType"), ("MPLS-LSR-MIB", "mplsInSegmentTrafficParamPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsInSegmentGroup = mplsInSegmentGroup.setStatus('current')
mplsOutSegmentGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 3)).setObjects(("MPLS-LSR-MIB", "mplsOutSegmentIndexNext"), ("MPLS-LSR-MIB", "mplsOutSegmentIfIndex"), ("MPLS-LSR-MIB", "mplsOutSegmentPushTopLabel"), ("MPLS-LSR-MIB", "mplsOutSegmentTopLabel"), ("MPLS-LSR-MIB", "mplsOutSegmentNextHopIpAddrType"), ("MPLS-LSR-MIB", "mplsOutSegmentNextHopIpv4Addr"), ("MPLS-LSR-MIB", "mplsOutSegmentNextHopIpv6Addr"), ("MPLS-LSR-MIB", "mplsOutSegmentXCIndex"), ("MPLS-LSR-MIB", "mplsOutSegmentOwner"), ("MPLS-LSR-MIB", "mplsOutSegmentOctets"), ("MPLS-LSR-MIB", "mplsOutSegmentDiscards"), ("MPLS-LSR-MIB", "mplsOutSegmentErrors"), ("MPLS-LSR-MIB", "mplsOutSegmentRowStatus"), ("MPLS-LSR-MIB", "mplsOutSegmentStorageType"), ("MPLS-LSR-MIB", "mplsOutSegmentTrafficParamPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsOutSegmentGroup = mplsOutSegmentGroup.setStatus('current')
mplsXCGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 4)).setObjects(("MPLS-LSR-MIB", "mplsXCIndexNext"), ("MPLS-LSR-MIB", "mplsXCLabelStackIndex"), ("MPLS-LSR-MIB", "mplsXCOwner"), ("MPLS-LSR-MIB", "mplsXCAdminStatus"), ("MPLS-LSR-MIB", "mplsXCOperStatus"), ("MPLS-LSR-MIB", "mplsXCRowStatus"), ("MPLS-LSR-MIB", "mplsXCTrapEnable"), ("MPLS-LSR-MIB", "mplsXCStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCGroup = mplsXCGroup.setStatus('current')
mplsXCOptionalGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 5)).setObjects(("MPLS-LSR-MIB", "mplsXCLspId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCOptionalGroup = mplsXCOptionalGroup.setStatus('current')
mplsPerfGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 6)).setObjects(("MPLS-LSR-MIB", "mplsInSegmentOctets"), ("MPLS-LSR-MIB", "mplsInSegmentPackets"), ("MPLS-LSR-MIB", "mplsInSegmentErrors"), ("MPLS-LSR-MIB", "mplsInSegmentDiscards"), ("MPLS-LSR-MIB", "mplsOutSegmentOctets"), ("MPLS-LSR-MIB", "mplsOutSegmentPackets"), ("MPLS-LSR-MIB", "mplsOutSegmentDiscards"), ("MPLS-LSR-MIB", "mplsInterfaceInLabelsUsed"), ("MPLS-LSR-MIB", "mplsInterfaceFailedLabelLookup"), ("MPLS-LSR-MIB", "mplsInterfaceOutFragments"), ("MPLS-LSR-MIB", "mplsInterfaceOutLabelsUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsPerfGroup = mplsPerfGroup.setStatus('current')
mplsHCInSegmentPerfGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 7)).setObjects(("MPLS-LSR-MIB", "mplsInSegmentHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsHCInSegmentPerfGroup = mplsHCInSegmentPerfGroup.setStatus('current')
mplsHCOutSegmentPerfGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 8)).setObjects(("MPLS-LSR-MIB", "mplsOutSegmentHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsHCOutSegmentPerfGroup = mplsHCOutSegmentPerfGroup.setStatus('current')
mplsTrafficParamGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 9)).setObjects(("MPLS-LSR-MIB", "mplsTrafficParamIndexNext"), ("MPLS-LSR-MIB", "mplsTrafficParamMaxRate"), ("MPLS-LSR-MIB", "mplsTrafficParamMeanRate"), ("MPLS-LSR-MIB", "mplsTrafficParamMaxBurstSize"), ("MPLS-LSR-MIB", "mplsTrafficParamRowStatus"), ("MPLS-LSR-MIB", "mplsTrafficParamStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTrafficParamGroup = mplsTrafficParamGroup.setStatus('current')
mplsXCIsPersistentGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 10)).setObjects(("MPLS-LSR-MIB", "mplsXCIsPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCIsPersistentGroup = mplsXCIsPersistentGroup.setStatus('current')
mplsXCIsNotPersistentGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 11)).setObjects(("MPLS-LSR-MIB", "mplsXCIsPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCIsNotPersistentGroup = mplsXCIsNotPersistentGroup.setStatus('current')
mplsLabelStackGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 12)).setObjects(("MPLS-LSR-MIB", "mplsLabelStackLabel"), ("MPLS-LSR-MIB", "mplsLabelStackRowStatus"), ("MPLS-LSR-MIB", "mplsLabelStackStorageType"), ("MPLS-LSR-MIB", "mplsMaxLabelStackDepth"), ("MPLS-LSR-MIB", "mplsLabelStackIndexNext"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLabelStackGroup = mplsLabelStackGroup.setStatus('current')
mplsSegmentDiscontinuityGroup = ObjectGroup((1, 3, 6, 1, 3, 96, 3, 1, 13)).setObjects(("MPLS-LSR-MIB", "mplsInSegmentPerfDiscontinuityTime"), ("MPLS-LSR-MIB", "mplsOutSegmentPerfDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsSegmentDiscontinuityGroup = mplsSegmentDiscontinuityGroup.setStatus('current')
mplsLsrNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 96, 3, 1, 14)).setObjects(("MPLS-LSR-MIB", "mplsXCUp"), ("MPLS-LSR-MIB", "mplsXCDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrNotificationGroup = mplsLsrNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LSR-MIB", mplsOutSegmentTopLabel=mplsOutSegmentTopLabel, mplsInterfaceLabelMaxOut=mplsInterfaceLabelMaxOut, mplsOutSegmentTable=mplsOutSegmentTable, mplsLabelStackIndexNext=mplsLabelStackIndexNext, mplsHCOutSegmentPerfGroup=mplsHCOutSegmentPerfGroup, mplsInSegmentStorageType=mplsInSegmentStorageType, MplsLSPID=MplsLSPID, mplsInterfaceConfIndex=mplsInterfaceConfIndex, MplsBitRate=MplsBitRate, mplsInSegmentXCIndex=mplsInSegmentXCIndex, mplsLsrGroups=mplsLsrGroups, mplsTrafficParamMaxRate=mplsTrafficParamMaxRate, mplsOutSegmentPushTopLabel=mplsOutSegmentPushTopLabel, mplsInSegmentTrafficParamPtr=mplsInSegmentTrafficParamPtr, mplsTrafficParamIndexNext=mplsTrafficParamIndexNext, mplsInterfacePerfEntry=mplsInterfacePerfEntry, mplsOutSegmentEntry=mplsOutSegmentEntry, mplsHCInSegmentPerfGroup=mplsHCInSegmentPerfGroup, mplsInSegmentErrors=mplsInSegmentErrors, mplsOutSegmentGroup=mplsOutSegmentGroup, mplsOutSegmentErrors=mplsOutSegmentErrors, mplsOutSegmentIndexNext=mplsOutSegmentIndexNext, mplsXCIsNotPersistentGroup=mplsXCIsNotPersistentGroup, mplsInSegmentPerfTable=mplsInSegmentPerfTable, mplsXCLabelStackIndex=mplsXCLabelStackIndex, mplsLsrNotifyPrefix=mplsLsrNotifyPrefix, mplsInterfaceLabelMaxIn=mplsInterfaceLabelMaxIn, mplsLsrNotifications=mplsLsrNotifications, MplsBurstSize=MplsBurstSize, mplsInSegmentPackets=mplsInSegmentPackets, mplsOutSegmentOctets=mplsOutSegmentOctets, mplsOutSegmentStorageType=mplsOutSegmentStorageType, mplsOutSegmentPerfEntry=mplsOutSegmentPerfEntry, mplsInSegmentTable=mplsInSegmentTable, mplsInterfacePerfTable=mplsInterfacePerfTable, mplsInterfaceInLabelsUsed=mplsInterfaceInLabelsUsed, PYSNMP_MODULE_ID=mplsLsrMIB, mplsOutSegmentPerfDiscontinuityTime=mplsOutSegmentPerfDiscontinuityTime, mplsInterfaceLabelParticipationType=mplsInterfaceLabelParticipationType, mplsInSegmentAddrFamily=mplsInSegmentAddrFamily, mplsXCIsPersistentGroup=mplsXCIsPersistentGroup, mplsOutSegmentTrafficParamPtr=mplsOutSegmentTrafficParamPtr, mplsInterfaceLabelMinIn=mplsInterfaceLabelMinIn, mplsXCTrapEnable=mplsXCTrapEnable, mplsInterfaceConfEntry=mplsInterfaceConfEntry, mplsTrafficParamStorageType=mplsTrafficParamStorageType, mplsInSegmentGroup=mplsInSegmentGroup, mplsLabelStackLabel=mplsLabelStackLabel, mplsXCTable=mplsXCTable, mplsInterfaceConfStorageType=mplsInterfaceConfStorageType, mplsXCDown=mplsXCDown, mplsOutSegmentNextHopIpAddrType=mplsOutSegmentNextHopIpAddrType, mplsLabelStackGroup=mplsLabelStackGroup, mplsSegmentDiscontinuityGroup=mplsSegmentDiscontinuityGroup, mplsInSegmentHCOctets=mplsInSegmentHCOctets, mplsInterfaceTotalBandwidth=mplsInterfaceTotalBandwidth, mplsInSegmentNPop=mplsInSegmentNPop, mplsXCIndexNext=mplsXCIndexNext, mplsInterfaceOutFragments=mplsInterfaceOutFragments, mplsXCAdminStatus=mplsXCAdminStatus, mplsPerfGroup=mplsPerfGroup, mplsLabelStackLabelIndex=mplsLabelStackLabelIndex, mplsXCOptionalGroup=mplsXCOptionalGroup, mplsInSegmentEntry=mplsInSegmentEntry, mplsLsrMIB=mplsLsrMIB, mplsInSegmentRowStatus=mplsInSegmentRowStatus, mplsOutSegmentOwner=mplsOutSegmentOwner, mplsLabelStackStorageType=mplsLabelStackStorageType, mplsInSegmentOctets=mplsInSegmentOctets, mplsOutSegmentIfIndex=mplsOutSegmentIfIndex, mplsOutSegmentNextHopIpv6Addr=mplsOutSegmentNextHopIpv6Addr, mplsInterfaceConfTable=mplsInterfaceConfTable, mplsTrafficParamEntry=mplsTrafficParamEntry, mplsTrafficParamGroup=mplsTrafficParamGroup, mplsXCIndex=mplsXCIndex, mplsOutSegmentPerfTable=mplsOutSegmentPerfTable, mplsXCLspId=mplsXCLspId, mplsXCGroup=mplsXCGroup, mplsInSegmentIfIndex=mplsInSegmentIfIndex, mplsXCIsPersistent=mplsXCIsPersistent, mplsInSegmentPerfDiscontinuityTime=mplsInSegmentPerfDiscontinuityTime, mplsOutSegmentRowStatus=mplsOutSegmentRowStatus, mplsOutSegmentIndex=mplsOutSegmentIndex, mplsInterfaceOutLabelsUsed=mplsInterfaceOutLabelsUsed, mplsOutSegmentNextHopIpv4Addr=mplsOutSegmentNextHopIpv4Addr, mplsLabelStackRowStatus=mplsLabelStackRowStatus, mplsXCEntry=mplsXCEntry, mplsXCStorageType=mplsXCStorageType, mplsTrafficParamTable=mplsTrafficParamTable, mplsOutSegmentDiscards=mplsOutSegmentDiscards, MplsObjectOwner=MplsObjectOwner, mplsInterfaceLabelMinOut=mplsInterfaceLabelMinOut, mplsLsrNotificationGroup=mplsLsrNotificationGroup, mplsTrafficParamIndex=mplsTrafficParamIndex, mplsInSegmentOwner=mplsInSegmentOwner, mplsTrafficParamMeanRate=mplsTrafficParamMeanRate, mplsOutSegmentXCIndex=mplsOutSegmentXCIndex, MplsLabel=MplsLabel, mplsLabelStackEntry=mplsLabelStackEntry, mplsLsrModuleCompliance=mplsLsrModuleCompliance, mplsXCUp=mplsXCUp, mplsInterfaceAvailableBandwidth=mplsInterfaceAvailableBandwidth, mplsLabelStackTable=mplsLabelStackTable, mplsLsrConformance=mplsLsrConformance, mplsLabelStackIndex=mplsLabelStackIndex, mplsTrafficParamRowStatus=mplsTrafficParamRowStatus, mplsXCOwner=mplsXCOwner, mplsInSegmentLabel=mplsInSegmentLabel, mplsInterfaceGroup=mplsInterfaceGroup, mplsMaxLabelStackDepth=mplsMaxLabelStackDepth, mplsOutSegmentHCOctets=mplsOutSegmentHCOctets, mplsLsrCompliances=mplsLsrCompliances, mplsInterfaceFailedLabelLookup=mplsInterfaceFailedLabelLookup, mplsOutSegmentPackets=mplsOutSegmentPackets, mplsTrafficParamMaxBurstSize=mplsTrafficParamMaxBurstSize, mplsXCOperStatus=mplsXCOperStatus, mplsXCRowStatus=mplsXCRowStatus, mplsInSegmentDiscards=mplsInSegmentDiscards, mplsInSegmentPerfEntry=mplsInSegmentPerfEntry, mplsLsrObjects=mplsLsrObjects)
