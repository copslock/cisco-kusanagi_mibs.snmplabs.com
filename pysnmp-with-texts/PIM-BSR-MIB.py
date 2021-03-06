#
# PySNMP MIB module PIM-BSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PIM-BSR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:10:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InetAddress, InetAddressPrefixLength, InetAddressType, InetZoneIndex = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType", "InetZoneIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Unsigned32, Integer32, IpAddress, MibIdentifier, Bits, Counter32, iso, ObjectIdentity, ModuleIdentity, TimeTicks, Counter64, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "Bits", "Counter32", "iso", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter64", "NotificationType", "Gauge32")
StorageType, TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
pimBsrMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 172))
pimBsrMIB.setRevisions(('2008-05-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pimBsrMIB.setRevisionsDescriptions(('Initial version, published as RFC 5240.',))
if mibBuilder.loadTexts: pimBsrMIB.setLastUpdated('200805280000Z')
if mibBuilder.loadTexts: pimBsrMIB.setOrganization('IETF Protocol Independent Multicast (PIM) Working Group')
if mibBuilder.loadTexts: pimBsrMIB.setContactInfo('Email: pim@ietf.org WG charter: http://www.ietf.org/html.charters/pim-charter.html')
if mibBuilder.loadTexts: pimBsrMIB.setDescription('The MIB module for management of the Bootstrap Router (BSR) mechanism for PIM routers. Copyright (C) The IETF Trust (2008). This version of this MIB module is part of RFC 5240; see the RFC itself for full legal notices.')
pimBsrNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 172, 0))
pimBsrObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 172, 1))
pimBsrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 172, 2))
pimBsrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 172, 2, 1))
pimBsrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 172, 2, 2))
pimBsrCandidateRPTable = MibTable((1, 3, 6, 1, 2, 1, 172, 1, 1), )
if mibBuilder.loadTexts: pimBsrCandidateRPTable.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPTable.setDescription('The (conceptual) table listing the IP multicast group prefixes for which the local router is to advertise itself as a Candidate-RP.')
pimBsrCandidateRPEntry = MibTableRow((1, 3, 6, 1, 2, 1, 172, 1, 1, 1), ).setIndexNames((0, "PIM-BSR-MIB", "pimBsrCandidateRPAddressType"), (0, "PIM-BSR-MIB", "pimBsrCandidateRPAddress"), (0, "PIM-BSR-MIB", "pimBsrCandidateRPGroupAddress"), (0, "PIM-BSR-MIB", "pimBsrCandidateRPGroupPrefixLength"))
if mibBuilder.loadTexts: pimBsrCandidateRPEntry.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPEntry.setDescription('An entry (conceptual row) in the pimBsrCandidateRPTable.')
pimBsrCandidateRPAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: pimBsrCandidateRPAddressType.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPAddressType.setDescription('The Inet address type of the Candidate-RP.')
pimBsrCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: pimBsrCandidateRPAddress.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPAddress.setDescription('The (unicast) address that will be advertised as a Candidate-RP. The InetAddressType is given by the pimBsrCandidateRPAddressType object.')
pimBsrCandidateRPGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: pimBsrCandidateRPGroupAddress.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPGroupAddress.setDescription('The IP multicast group address that, when combined with the corresponding value of pimBsrCandidateRPGroupPrefixLength, identifies a group prefix for which the local router will advertise itself as a Candidate-RP. The InetAddressType is given by the pimBsrCandidateRPAddressType object. This address object is only significant up to pimBsrCandidateRPGroupPrefixLength bits. The remainder of the address bits are zero. This is especially important for this field, which is part of the index of this entry. Any non-zero bits would signify an entirely different entry.')
pimBsrCandidateRPGroupPrefixLength = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 4), InetAddressPrefixLength().subtype(subtypeSpec=ValueRangeConstraint(4, 128)))
if mibBuilder.loadTexts: pimBsrCandidateRPGroupPrefixLength.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPGroupPrefixLength.setDescription('The multicast group address mask that, when combined with the corresponding value of pimBsrCandidateRPGroupAddress, identifies a group prefix for which the local router will advertise itself as a Candidate-RP. The InetAddressType is given by the pimBsrCandidateRPAddressType object.')
pimBsrCandidateRPBidir = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateRPBidir.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPBidir.setDescription('If this object is set to TRUE, this group range is advertised with this RP as a BIDIR-PIM group range. If it is set to FALSE, it is advertised as a PIM-SM group range.')
pimBsrCandidateRPAdvTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrCandidateRPAdvTimer.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPAdvTimer.setDescription('The time remaining before the local router next sends a Candidate-RP-Advertisement to the elected BSR for this zone.')
pimBsrCandidateRPPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateRPPriority.setReference('RFC 5059, section 3.2')
if mibBuilder.loadTexts: pimBsrCandidateRPPriority.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPPriority.setDescription('The priority for this Candidate-RP advertised in Candidate-RP-Advertisements.')
pimBsrCandidateRPAdvInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 26214)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateRPAdvInterval.setReference('RFC 5059, sections 3.2 and 5')
if mibBuilder.loadTexts: pimBsrCandidateRPAdvInterval.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPAdvInterval.setDescription('A Candidate-RP generates Candidate-RP-Advertisements periodically. This object represents the time interval in seconds between two consecutive advertisements.')
pimBsrCandidateRPHoldtime = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(150)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateRPHoldtime.setReference('RFC 5059, section 4.2')
if mibBuilder.loadTexts: pimBsrCandidateRPHoldtime.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPHoldtime.setDescription("Holdtime for this Candidate-RP. The amount of time (in seconds) this Candidate-RP entry is valid. This object's value can be zero only when this C-RP is shutting down.")
pimBsrCandidateRPStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateRPStatus.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table. This status object can be set to active(1) without setting any other columnar objects in this entry. All writable objects in this entry can be modified when the status of this entry is active(1).')
pimBsrCandidateRPStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 1, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateRPStorageType.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateRPStorageType.setDescription("The storage type for this row. Rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
pimBsrElectedBSRRPSetTable = MibTable((1, 3, 6, 1, 2, 1, 172, 1, 2), )
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetTable.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetTable.setDescription('The (conceptual) table listing BSR-specific information about PIM group mappings learned via C-RP advertisements or created locally using configurations. This table is maintained only on the Elected BSR. An Elected BSR uses this table to create Bootstrap messages after applying a local policy to include some or all of the group mappings in this table.')
pimBsrElectedBSRRPSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 172, 1, 2, 1), ).setIndexNames((0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingAddrType"), (0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingGrpAddr"), (0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingGrpPrefixLen"), (0, "PIM-BSR-MIB", "pimBsrElectedBSRGrpMappingRPAddr"))
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetEntry.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetEntry.setDescription('An entry (conceptual row) in the pimBsrElectedBSRRPSetTable.')
pimBsrElectedBSRGrpMappingAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingAddrType.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingAddrType.setDescription('The Inet address type of the IP multicast group prefix.')
pimBsrElectedBSRGrpMappingGrpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingGrpAddr.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingGrpAddr.setDescription('The IP multicast group address that, when combined with pimBsrElectedBSRGrpMappingGrpPrefixLen, gives the group prefix for this mapping. The InetAddressType is given by the pimBsrElectedBSRGrpMappingAddrType object. This address object is only significant up to pimBsrElectedBSRGrpMappingGrpPrefixLen bits. The remainder of the address bits are zero. This is especially important for this field, which is part of the index of this entry. Any non-zero bits would signify an entirely different entry.')
pimBsrElectedBSRGrpMappingGrpPrefixLen = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 4), InetAddressPrefixLength().subtype(subtypeSpec=ValueRangeConstraint(4, 128)))
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingGrpPrefixLen.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingGrpPrefixLen.setDescription("The multicast group prefix length that, when combined with pimBsrElectedBSRGrpMappingGrpAddr, gives the group prefix for this mapping. The InetAddressType is given by the pimBsrElectedBSRGrpMappingAddrType object. If pimBsrElectedBSRGrpMappingAddrType is 'ipv4' or 'ipv4z', this object must be in the range 4..32. If pimBsrElectedBSRGrpMappingAddrType is 'ipv6' or 'ipv6z', this object must be in the range 8..128.")
pimBsrElectedBSRGrpMappingRPAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 5), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingRPAddr.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRGrpMappingRPAddr.setDescription('The IP address of the RP to be used for groups within this group prefix. The InetAddressType is given by the pimBsrElectedBSRGrpMappingAddrType object.')
pimBsrElectedBSRRPSetPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetPriority.setReference('RFC 5059, section 4.1')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetPriority.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetPriority.setDescription('The priority for RP. Numerically higher values for this object indicate lower priorities, with the value zero denoting the highest priority.')
pimBsrElectedBSRRPSetHoldtime = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetHoldtime.setReference('RFC 5059, section 4.1')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetHoldtime.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetHoldtime.setDescription('The holdtime for RP')
pimBsrElectedBSRRPSetExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetExpiryTime.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetExpiryTime.setDescription('The minimum time remaining before this entry will be aged out. The value zero indicates that this entry will never be aged out.')
pimBsrElectedBSRRPSetGrpBidir = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetGrpBidir.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRRPSetGrpBidir.setDescription('If this object is TRUE, this group range with this RP is a BIDIR-PIM group range. If it is set to FALSE, it is a PIM-SM group range.')
pimBsrCandidateBSRTable = MibTable((1, 3, 6, 1, 2, 1, 172, 1, 3), )
if mibBuilder.loadTexts: pimBsrCandidateBSRTable.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRTable.setDescription('The (conceptual) table containing Candidate-BSR configuration for the local router. The table contains one row for each zone for which the local router is to advertise itself as a Candidate-BSR.')
pimBsrCandidateBSREntry = MibTableRow((1, 3, 6, 1, 2, 1, 172, 1, 3, 1), ).setIndexNames((0, "PIM-BSR-MIB", "pimBsrCandidateBSRZoneIndex"))
if mibBuilder.loadTexts: pimBsrCandidateBSREntry.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSREntry.setDescription('An entry (conceptual row) in the pimBsrCandidateBSRTable.')
pimBsrCandidateBSRZoneIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 1), InetZoneIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: pimBsrCandidateBSRZoneIndex.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRZoneIndex.setDescription('The zone index uniquely identifies the zone on a device to which this Candidate-BSR is attached. There is one entry for each zone in ipMcastZoneTable. Scope-level information for this zone can be extracted from ipMcastZoneTable in IP Multicast MIB [RFC5132]. Zero is a special value used to request the default zone for a given scope. Zero is not a valid value for this object.')
pimBsrCandidateBSRAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateBSRAddressType.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRAddressType.setDescription('The address type of the Candidate-BSR.')
pimBsrCandidateBSRAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateBSRAddress.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRAddress.setDescription('The (unicast) address that the local router will use to advertise itself as a Candidate-BSR. The InetAddressType is given by the pimBsrCandidateBSRAddressType object.')
pimBsrCandidateBSRPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateBSRPriority.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRPriority.setDescription('The priority value for the local router as a Candidate-BSR for this zone. Numerically higher values for this object indicate higher priorities.')
pimBsrCandidateBSRHashMaskLength = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateBSRHashMaskLength.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRHashMaskLength.setDescription("The hash mask length (used in the RP hash function) that the local router will advertise in its Bootstrap messages for this zone. This object defaults to 30 if pimBsrCandidateBSRAddressType is 'ipv4' or 'ipv4z' , and defaults to 126 if pimBsrCandidateBSRAddressType is 'ipv6' or 'ipv6z'.")
pimBsrCandidateBSRElectedBSR = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrCandidateBSRElectedBSR.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRElectedBSR.setDescription('Whether the local router is the elected BSR for this zone.')
pimBsrCandidateBSRBootstrapTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrCandidateBSRBootstrapTimer.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRBootstrapTimer.setDescription("The time remaining before the local router next originates a Bootstrap message for this zone. Value of this object is zero if pimBsrCandidateBSRElectedBSR is 'FALSE'.")
pimBsrCandidateBSRStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateBSRStatus.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRStatus.setDescription('The status of this row, by which new entries may be created or old entries deleted from this table. This status object can be set to active(1) without setting any other columnar objects in this entry. All writable objects in this entry can be modified when the status of this entry is active(1).')
pimBsrCandidateBSRStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 3, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimBsrCandidateBSRStorageType.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRStorageType.setDescription("The storage type for this row. Rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
pimBsrElectedBSRTable = MibTable((1, 3, 6, 1, 2, 1, 172, 1, 4), )
if mibBuilder.loadTexts: pimBsrElectedBSRTable.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRTable.setDescription('The (conceptual) table containing information about elected BSRs. The table contains one row for each zone for which there is an elected BSR.')
pimBsrElectedBSREntry = MibTableRow((1, 3, 6, 1, 2, 1, 172, 1, 4, 1), ).setIndexNames((0, "PIM-BSR-MIB", "pimBsrElectedBSRZoneIndex"))
if mibBuilder.loadTexts: pimBsrElectedBSREntry.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSREntry.setDescription('An entry (conceptual row) in the pimBsrElectedBSRTable.')
pimBsrElectedBSRZoneIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 1), InetZoneIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: pimBsrElectedBSRZoneIndex.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRZoneIndex.setDescription('The zone index uniquely identifies the zone on a device to which this Elected BSR is attached. There is one entry for each zone in ipMcastZoneTable. Scope-level information for this zone can be extracted from ipMcastZoneTable in IP Multicast MIB [RFC5132]. Zero is a special value used to request the default zone for a given scope. Zero is not a valid value for this object.')
pimBsrElectedBSRAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRAddressType.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRAddressType.setDescription('The address type of the elected BSR.')
pimBsrElectedBSRAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRAddress.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRAddress.setDescription('The (unicast) address of the elected BSR. The InetAddressType is given by the pimBsrElectedBSRAddressType object.')
pimBsrElectedBSRPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRPriority.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRPriority.setDescription('The priority value for the elected BSR for this address type. Numerically higher values for this object indicate higher priorities.')
pimBsrElectedBSRHashMaskLength = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRHashMaskLength.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRHashMaskLength.setDescription('The hash mask length (used in the RP hash function) advertised by the elected BSR for this zone.')
pimBsrElectedBSRExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 172, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimBsrElectedBSRExpiryTime.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRExpiryTime.setDescription('The minimum time remaining before the elected BSR for this zone will be declared down.')
pimBsrElectedBSRLostElection = NotificationType((1, 3, 6, 1, 2, 1, 172, 0, 1)).setObjects(("PIM-BSR-MIB", "pimBsrElectedBSRAddressType"), ("PIM-BSR-MIB", "pimBsrElectedBSRAddress"), ("PIM-BSR-MIB", "pimBsrElectedBSRPriority"))
if mibBuilder.loadTexts: pimBsrElectedBSRLostElection.setStatus('current')
if mibBuilder.loadTexts: pimBsrElectedBSRLostElection.setDescription('A pimBsrElectedBSRLostElection notification should be generated when current E-BSR lost election to a new Candidate-BSR. Only an E-BSR should generate this notification. This notification is generated when pimBsrCandidateBSRElectedBSR becomes FALSE.')
if mibBuilder.loadTexts: pimBsrElectedBSRLostElection.setReference('RFC 5059, section 3.1')
pimBsrCandidateBSRWinElection = NotificationType((1, 3, 6, 1, 2, 1, 172, 0, 2)).setObjects(("PIM-BSR-MIB", "pimBsrCandidateBSRElectedBSR"))
if mibBuilder.loadTexts: pimBsrCandidateBSRWinElection.setStatus('current')
if mibBuilder.loadTexts: pimBsrCandidateBSRWinElection.setDescription('A pimBsrCandidateBSRWinElection notification should be generated when a C-BSR wins BSR Election. Only an E-BSR should generate this notification. This notification is generated when pimBsrCandidateBSRElectedBSR becomes TRUE.')
if mibBuilder.loadTexts: pimBsrCandidateBSRWinElection.setReference('RFC 5059, section 3.1')
pimBsrCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 172, 2, 1, 1)).setObjects(("PIM-BSR-MIB", "pimBsrObjectGroup"), ("PIM-BSR-MIB", "pimBsrDiagnosticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimBsrCompliance = pimBsrCompliance.setStatus('current')
if mibBuilder.loadTexts: pimBsrCompliance.setDescription('The compliance statement for PIM routers that implement the Bootstrap Router (BSR) mechanism.')
pimBsrObjectGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 172, 2, 2, 1)).setObjects(("PIM-BSR-MIB", "pimBsrCandidateRPBidir"), ("PIM-BSR-MIB", "pimBsrCandidateRPAdvTimer"), ("PIM-BSR-MIB", "pimBsrCandidateRPPriority"), ("PIM-BSR-MIB", "pimBsrCandidateRPAdvInterval"), ("PIM-BSR-MIB", "pimBsrCandidateRPHoldtime"), ("PIM-BSR-MIB", "pimBsrCandidateRPStatus"), ("PIM-BSR-MIB", "pimBsrCandidateRPStorageType"), ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetPriority"), ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetHoldtime"), ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetExpiryTime"), ("PIM-BSR-MIB", "pimBsrElectedBSRRPSetGrpBidir"), ("PIM-BSR-MIB", "pimBsrCandidateBSRAddress"), ("PIM-BSR-MIB", "pimBsrCandidateBSRAddressType"), ("PIM-BSR-MIB", "pimBsrCandidateBSRPriority"), ("PIM-BSR-MIB", "pimBsrCandidateBSRHashMaskLength"), ("PIM-BSR-MIB", "pimBsrCandidateBSRElectedBSR"), ("PIM-BSR-MIB", "pimBsrCandidateBSRBootstrapTimer"), ("PIM-BSR-MIB", "pimBsrCandidateBSRStatus"), ("PIM-BSR-MIB", "pimBsrCandidateBSRStorageType"), ("PIM-BSR-MIB", "pimBsrElectedBSRAddress"), ("PIM-BSR-MIB", "pimBsrElectedBSRAddressType"), ("PIM-BSR-MIB", "pimBsrElectedBSRPriority"), ("PIM-BSR-MIB", "pimBsrElectedBSRHashMaskLength"), ("PIM-BSR-MIB", "pimBsrElectedBSRExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimBsrObjectGroup = pimBsrObjectGroup.setStatus('current')
if mibBuilder.loadTexts: pimBsrObjectGroup.setDescription('A collection of objects for managing the Bootstrap Router (BSR) mechanism for PIM routers.')
pimBsrDiagnosticsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 172, 2, 2, 2)).setObjects(("PIM-BSR-MIB", "pimBsrElectedBSRLostElection"), ("PIM-BSR-MIB", "pimBsrCandidateBSRWinElection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pimBsrDiagnosticsGroup = pimBsrDiagnosticsGroup.setStatus('current')
if mibBuilder.loadTexts: pimBsrDiagnosticsGroup.setDescription('Objects providing additional diagnostics related to the Bootstrap Router (BSR) mechanism for PIM routers.')
mibBuilder.exportSymbols("PIM-BSR-MIB", pimBsrObjectGroup=pimBsrObjectGroup, pimBsrMIB=pimBsrMIB, pimBsrElectedBSRGrpMappingGrpAddr=pimBsrElectedBSRGrpMappingGrpAddr, pimBsrElectedBSRGrpMappingGrpPrefixLen=pimBsrElectedBSRGrpMappingGrpPrefixLen, pimBsrCandidateBSRAddress=pimBsrCandidateBSRAddress, pimBsrConformance=pimBsrConformance, pimBsrElectedBSRRPSetHoldtime=pimBsrElectedBSRRPSetHoldtime, pimBsrCandidateRPAddress=pimBsrCandidateRPAddress, pimBsrCandidateRPBidir=pimBsrCandidateRPBidir, pimBsrCandidateBSRElectedBSR=pimBsrCandidateBSRElectedBSR, pimBsrCandidateRPGroupPrefixLength=pimBsrCandidateRPGroupPrefixLength, pimBsrElectedBSRAddress=pimBsrElectedBSRAddress, pimBsrElectedBSRRPSetTable=pimBsrElectedBSRRPSetTable, pimBsrElectedBSRRPSetGrpBidir=pimBsrElectedBSRRPSetGrpBidir, pimBsrCandidateBSRZoneIndex=pimBsrCandidateBSRZoneIndex, pimBsrElectedBSRGrpMappingAddrType=pimBsrElectedBSRGrpMappingAddrType, pimBsrElectedBSRExpiryTime=pimBsrElectedBSRExpiryTime, pimBsrCandidateBSRWinElection=pimBsrCandidateBSRWinElection, pimBsrCandidateRPTable=pimBsrCandidateRPTable, pimBsrElectedBSRRPSetPriority=pimBsrElectedBSRRPSetPriority, pimBsrElectedBSRGrpMappingRPAddr=pimBsrElectedBSRGrpMappingRPAddr, pimBsrCandidateBSRStorageType=pimBsrCandidateBSRStorageType, PYSNMP_MODULE_ID=pimBsrMIB, pimBsrCandidateRPAdvTimer=pimBsrCandidateRPAdvTimer, pimBsrCandidateBSRBootstrapTimer=pimBsrCandidateBSRBootstrapTimer, pimBsrCompliance=pimBsrCompliance, pimBsrCandidateBSREntry=pimBsrCandidateBSREntry, pimBsrCandidateRPEntry=pimBsrCandidateRPEntry, pimBsrCandidateRPGroupAddress=pimBsrCandidateRPGroupAddress, pimBsrCompliances=pimBsrCompliances, pimBsrElectedBSRPriority=pimBsrElectedBSRPriority, pimBsrGroups=pimBsrGroups, pimBsrCandidateRPAdvInterval=pimBsrCandidateRPAdvInterval, pimBsrCandidateRPHoldtime=pimBsrCandidateRPHoldtime, pimBsrCandidateBSRTable=pimBsrCandidateBSRTable, pimBsrCandidateRPPriority=pimBsrCandidateRPPriority, pimBsrCandidateRPStatus=pimBsrCandidateRPStatus, pimBsrElectedBSRRPSetEntry=pimBsrElectedBSRRPSetEntry, pimBsrCandidateBSRPriority=pimBsrCandidateBSRPriority, pimBsrCandidateBSRStatus=pimBsrCandidateBSRStatus, pimBsrElectedBSREntry=pimBsrElectedBSREntry, pimBsrCandidateBSRHashMaskLength=pimBsrCandidateBSRHashMaskLength, pimBsrElectedBSRHashMaskLength=pimBsrElectedBSRHashMaskLength, pimBsrNotifications=pimBsrNotifications, pimBsrElectedBSRZoneIndex=pimBsrElectedBSRZoneIndex, pimBsrCandidateRPStorageType=pimBsrCandidateRPStorageType, pimBsrCandidateBSRAddressType=pimBsrCandidateBSRAddressType, pimBsrObjects=pimBsrObjects, pimBsrElectedBSRLostElection=pimBsrElectedBSRLostElection, pimBsrElectedBSRRPSetExpiryTime=pimBsrElectedBSRRPSetExpiryTime, pimBsrCandidateRPAddressType=pimBsrCandidateRPAddressType, pimBsrElectedBSRAddressType=pimBsrElectedBSRAddressType, pimBsrDiagnosticsGroup=pimBsrDiagnosticsGroup, pimBsrElectedBSRTable=pimBsrElectedBSRTable)
