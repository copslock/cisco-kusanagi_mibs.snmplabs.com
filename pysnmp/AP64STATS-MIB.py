#
# PySNMP MIB module AP64STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AP64STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ap64Stats, = mibBuilder.importSymbols("APENT-MIB", "ap64Stats")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, TimeTicks, iso, Counter64, IpAddress, Integer32, Counter32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "TimeTicks", "iso", "Counter64", "IpAddress", "Integer32", "Counter32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ap64StatsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 44, 1))
if mibBuilder.loadTexts: ap64StatsMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: ap64StatsMib.setOrganization('ArrowPoint Communications Inc.')
class PhysAddress(OctetString):
    pass

class OwnerString(DisplayString):
    pass

class EntryStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4))

ap64dot3StatsTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2), )
if mibBuilder.loadTexts: ap64dot3StatsTable.setStatus('current')
ap64dot3StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1), ).setIndexNames((0, "AP64STATS-MIB", "ap64dot3StatsIndex"))
if mibBuilder.loadTexts: ap64dot3StatsEntry.setStatus('current')
ap64dot3StatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsIndex.setStatus('current')
ap64dot3StatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsAlignmentErrors.setStatus('current')
ap64dot3StatsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsFCSErrors.setStatus('current')
ap64dot3StatsSingleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsSingleCollisionFrames.setStatus('current')
ap64dot3StatsMultipleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsMultipleCollisionFrames.setStatus('current')
ap64dot3StatsSQETestErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsSQETestErrors.setStatus('current')
ap64dot3StatsDeferredTransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsDeferredTransmissions.setStatus('current')
ap64dot3StatsLateCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsLateCollisions.setStatus('current')
ap64dot3StatsExcessiveCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsExcessiveCollisions.setStatus('current')
ap64dot3StatsInternalMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsInternalMacTransmitErrors.setStatus('current')
ap64dot3StatsCarrierSenseErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsCarrierSenseErrors.setStatus('current')
ap64dot3StatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsFrameTooLongs.setStatus('current')
ap64dot3StatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsInternalMacReceiveErrors.setStatus('current')
ap64ifTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3), )
if mibBuilder.loadTexts: ap64ifTable.setStatus('current')
ap64ifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1), ).setIndexNames((0, "AP64STATS-MIB", "ap64ifIndex"))
if mibBuilder.loadTexts: ap64ifEntry.setStatus('current')
ap64ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifIndex.setStatus('current')
ap64ifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifDescr.setStatus('current')
ap64ifType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32))).clone(namedValues=NamedValues(("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddn-x25", 4), ("rfc877-x25", 5), ("ethernet-csmacd", 6), ("iso88023-csmacd", 7), ("iso88024-tokenBus", 8), ("iso88025-tokenRing", 9), ("iso88026-man", 10), ("starLan", 11), ("proteon-10Mbit", 12), ("proteon-80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet-3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frame-relay", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifType.setStatus('current')
ap64ifMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifMtu.setStatus('current')
ap64ifSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifSpeed.setStatus('current')
ap64ifPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifPhysAddress.setStatus('current')
ap64ifAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifAdminStatus.setStatus('current')
ap64ifOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOperStatus.setStatus('current')
ap64ifLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifLastChange.setStatus('current')
ap64ifInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInOctets.setStatus('current')
ap64ifInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInUcastPkts.setStatus('current')
ap64ifInNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInNUcastPkts.setStatus('current')
ap64ifInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInDiscards.setStatus('current')
ap64ifInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInErrors.setStatus('current')
ap64ifInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInUnknownProtos.setStatus('current')
ap64ifOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutOctets.setStatus('current')
ap64ifOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutUcastPkts.setStatus('current')
ap64ifOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutNUcastPkts.setStatus('current')
ap64ifOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutDiscards.setStatus('current')
ap64ifOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutErrors.setStatus('current')
ap64ifOutQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutQLen.setStatus('current')
ap64ifSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 22), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifSpecific.setStatus('current')
ap64etherStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4), )
if mibBuilder.loadTexts: ap64etherStatsTable.setStatus('current')
ap64etherStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1), ).setIndexNames((0, "AP64STATS-MIB", "ap64etherStatsIndex"))
if mibBuilder.loadTexts: ap64etherStatsEntry.setStatus('current')
ap64etherStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsIndex.setStatus('current')
ap64etherStatsDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsDataSource.setStatus('current')
ap64etherStatsDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsDropEvents.setStatus('current')
ap64etherStatsOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsOctets.setStatus('current')
ap64etherStatsPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts.setStatus('current')
ap64etherStatsBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsBroadcastPkts.setStatus('current')
ap64etherStatsMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsMulticastPkts.setStatus('current')
ap64etherStatsCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsCRCAlignErrors.setStatus('current')
ap64etherStatsUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsUndersizePkts.setStatus('current')
ap64etherStatsOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsOversizePkts.setStatus('current')
ap64etherStatsFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsFragments.setStatus('current')
ap64etherStatsJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsJabbers.setStatus('current')
ap64etherStatsCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsCollisions.setStatus('current')
ap64etherStatsPkts64Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts64Octets.setStatus('current')
ap64etherStatsPkts65to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts65to127Octets.setStatus('current')
ap64etherStatsPkts128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts128to255Octets.setStatus('current')
ap64etherStatsPkts256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts256to511Octets.setStatus('current')
ap64etherStatsPkts512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts512to1023Octets.setStatus('current')
ap64etherStatsPkts1024to1518Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts1024to1518Octets.setStatus('current')
ap64etherStatsOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 20), OwnerString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsOwner.setStatus('current')
ap64etherStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 21), EntryStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsStatus.setStatus('current')
mibBuilder.exportSymbols("AP64STATS-MIB", ap64etherStatsPkts64Octets=ap64etherStatsPkts64Octets, ap64etherStatsIndex=ap64etherStatsIndex, ap64etherStatsStatus=ap64etherStatsStatus, ap64etherStatsJabbers=ap64etherStatsJabbers, ap64ifInNUcastPkts=ap64ifInNUcastPkts, ap64etherStatsCollisions=ap64etherStatsCollisions, ap64dot3StatsInternalMacReceiveErrors=ap64dot3StatsInternalMacReceiveErrors, ap64dot3StatsExcessiveCollisions=ap64dot3StatsExcessiveCollisions, ap64ifLastChange=ap64ifLastChange, ap64ifOutDiscards=ap64ifOutDiscards, ap64ifMtu=ap64ifMtu, ap64ifInUcastPkts=ap64ifInUcastPkts, ap64ifInErrors=ap64ifInErrors, ap64dot3StatsIndex=ap64dot3StatsIndex, ap64etherStatsPkts=ap64etherStatsPkts, PYSNMP_MODULE_ID=ap64StatsMib, ap64etherStatsOwner=ap64etherStatsOwner, ap64dot3StatsSingleCollisionFrames=ap64dot3StatsSingleCollisionFrames, ap64ifInDiscards=ap64ifInDiscards, OwnerString=OwnerString, ap64etherStatsPkts128to255Octets=ap64etherStatsPkts128to255Octets, ap64ifSpecific=ap64ifSpecific, ap64etherStatsEntry=ap64etherStatsEntry, ap64ifType=ap64ifType, ap64ifOutOctets=ap64ifOutOctets, ap64etherStatsDropEvents=ap64etherStatsDropEvents, ap64etherStatsOversizePkts=ap64etherStatsOversizePkts, ap64StatsMib=ap64StatsMib, ap64ifAdminStatus=ap64ifAdminStatus, ap64ifOutErrors=ap64ifOutErrors, ap64dot3StatsLateCollisions=ap64dot3StatsLateCollisions, ap64etherStatsPkts512to1023Octets=ap64etherStatsPkts512to1023Octets, ap64dot3StatsTable=ap64dot3StatsTable, PhysAddress=PhysAddress, ap64ifOperStatus=ap64ifOperStatus, ap64dot3StatsMultipleCollisionFrames=ap64dot3StatsMultipleCollisionFrames, ap64ifEntry=ap64ifEntry, ap64dot3StatsAlignmentErrors=ap64dot3StatsAlignmentErrors, ap64ifOutNUcastPkts=ap64ifOutNUcastPkts, ap64ifSpeed=ap64ifSpeed, ap64dot3StatsFrameTooLongs=ap64dot3StatsFrameTooLongs, ap64etherStatsPkts1024to1518Octets=ap64etherStatsPkts1024to1518Octets, ap64dot3StatsSQETestErrors=ap64dot3StatsSQETestErrors, ap64dot3StatsInternalMacTransmitErrors=ap64dot3StatsInternalMacTransmitErrors, ap64etherStatsMulticastPkts=ap64etherStatsMulticastPkts, ap64etherStatsDataSource=ap64etherStatsDataSource, ap64ifDescr=ap64ifDescr, ap64etherStatsTable=ap64etherStatsTable, ap64etherStatsOctets=ap64etherStatsOctets, ap64etherStatsCRCAlignErrors=ap64etherStatsCRCAlignErrors, ap64etherStatsPkts65to127Octets=ap64etherStatsPkts65to127Octets, ap64ifOutUcastPkts=ap64ifOutUcastPkts, ap64etherStatsFragments=ap64etherStatsFragments, EntryStatus=EntryStatus, ap64dot3StatsDeferredTransmissions=ap64dot3StatsDeferredTransmissions, ap64ifInOctets=ap64ifInOctets, ap64etherStatsUndersizePkts=ap64etherStatsUndersizePkts, ap64dot3StatsFCSErrors=ap64dot3StatsFCSErrors, ap64dot3StatsCarrierSenseErrors=ap64dot3StatsCarrierSenseErrors, ap64ifTable=ap64ifTable, ap64ifOutQLen=ap64ifOutQLen, ap64etherStatsBroadcastPkts=ap64etherStatsBroadcastPkts, ap64ifPhysAddress=ap64ifPhysAddress, ap64etherStatsPkts256to511Octets=ap64etherStatsPkts256to511Octets, ap64dot3StatsEntry=ap64dot3StatsEntry, ap64ifInUnknownProtos=ap64ifInUnknownProtos, ap64ifIndex=ap64ifIndex)
