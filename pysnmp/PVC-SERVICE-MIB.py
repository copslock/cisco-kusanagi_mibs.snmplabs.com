#
# PySNMP MIB module PVC-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PVC-SERVICE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
frCircuitIfIndex, frCircuitDlci = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "frCircuitIfIndex", "frCircuitDlci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, ModuleIdentity, Bits, iso, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier, IpAddress, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ModuleIdentity", "Bits", "iso", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, RowStatus, PhysAddress, DisplayString, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "PhysAddress", "DisplayString", "MacAddress", "TruthValue")
pgService = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 6))
if mibBuilder.loadTexts: pgService.setLastUpdated('9803030000Z')
if mibBuilder.loadTexts: pgService.setOrganization('PairGain Technology')
pgServiceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1))
class PgPvcServiceType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("ipoa", 2), ("lant", 3), ("ppp", 4), ("frame-relay", 5), ("null", 6), ("ramp1483", 7))

class PgXdslFrameType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("mac", 2))

pgXdslServiceTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1), )
if mibBuilder.loadTexts: pgXdslServiceTable.setStatus('current')
pgXdslServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgXdslServiceEntry.setStatus('current')
pgXdslServiceSubscriberName = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceSubscriberName.setStatus('current')
pgXdslServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 2), PgPvcServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceType.setStatus('current')
pgXdslServiceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceMacAddress.setStatus('current')
pgXdslServiceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceIpAddress.setStatus('current')
pgXdslServiceSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgXdslServiceSubnetMask.setStatus('current')
pgXdslServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgXdslServiceRowStatus.setStatus('current')
class PgPvcServiceEncapType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("vc-mux-iso", 2), ("vc-mux-ip", 3), ("vc-mux-8023", 4), ("llc-iso", 5), ("llc-ip", 6), ("llc-8023-crc", 7), ("llc-8023", 8), ("vc-mux-ppp", 9), ("llc-ppp", 10), ("vc-mux-ramp1483", 11))

pgPvcServiceTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2), )
if mibBuilder.loadTexts: pgPvcServiceTable.setStatus('current')
pgPvcServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1), ).setIndexNames((0, "PVC-SERVICE-MIB", "pgPvcServiceSarVpi"), (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVci"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgPvcServiceEntry.setStatus('current')
pgPvcServiceSarVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceSarVpi.setStatus('current')
pgPvcServiceSarVci = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceSarVci.setStatus('current')
pgPvcServiceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceIpAddress.setStatus('deprecated')
pgPvcServiceSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceSubnetMask.setStatus('deprecated')
pgPvcServiceEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 5), PgPvcServiceEncapType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgPvcServiceEncapType.setStatus('deprecated')
pgPvcServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgPvcServiceRowStatus.setStatus('current')
pgNextSarVciTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3), )
if mibBuilder.loadTexts: pgNextSarVciTable.setStatus('current')
pgNextSarVciEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgNextSarVciEntry.setStatus('current')
pgNextSarSlotVci = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1024, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgNextSarSlotVci.setStatus('current')
pgPvcFrServiceTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4), )
if mibBuilder.loadTexts: pgPvcFrServiceTable.setStatus('current')
pgPvcFrServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1), ).setIndexNames((0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"), (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"), (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVpi"), (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVci"))
if mibBuilder.loadTexts: pgPvcFrServiceEntry.setStatus('current')
pgPvcFrServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgPvcFrServiceRowStatus.setStatus('current')
pgPvcFrSubSystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 8))).clone(namedValues=NamedValues(("frf5", 5), ("frf8", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgPvcFrSubSystemType.setStatus('current')
mibBuilder.exportSymbols("PVC-SERVICE-MIB", pgXdslServiceSubnetMask=pgXdslServiceSubnetMask, pgPvcFrSubSystemType=pgPvcFrSubSystemType, pgXdslServiceMacAddress=pgXdslServiceMacAddress, pgNextSarSlotVci=pgNextSarSlotVci, pgPvcServiceEncapType=pgPvcServiceEncapType, pgNextSarVciTable=pgNextSarVciTable, pgPvcServiceRowStatus=pgPvcServiceRowStatus, pgPvcFrServiceTable=pgPvcFrServiceTable, pgPvcServiceTable=pgPvcServiceTable, pgService=pgService, PgPvcServiceType=PgPvcServiceType, pgPvcFrServiceRowStatus=pgPvcFrServiceRowStatus, pgPvcServiceIpAddress=pgPvcServiceIpAddress, PgXdslFrameType=PgXdslFrameType, pgXdslServiceRowStatus=pgXdslServiceRowStatus, pgXdslServiceType=pgXdslServiceType, pgPvcServiceEntry=pgPvcServiceEntry, pgXdslServiceIpAddress=pgXdslServiceIpAddress, PYSNMP_MODULE_ID=pgService, pgPvcFrServiceEntry=pgPvcFrServiceEntry, pgXdslServiceEntry=pgXdslServiceEntry, PgPvcServiceEncapType=PgPvcServiceEncapType, pgXdslServiceTable=pgXdslServiceTable, pgServiceObjects=pgServiceObjects, pgXdslServiceSubscriberName=pgXdslServiceSubscriberName, pgNextSarVciEntry=pgNextSarVciEntry, pgPvcServiceSarVpi=pgPvcServiceSarVpi, pgPvcServiceSubnetMask=pgPvcServiceSubnetMask, pgPvcServiceSarVci=pgPvcServiceSarVci)
