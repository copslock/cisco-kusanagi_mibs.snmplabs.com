#
# PySNMP MIB module QLASP-Statistics-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QLASP-Statistics-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:35:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, Counter32, iso, enterprises, Integer32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "Counter32", "iso", "enterprises", "Integer32", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qlogic = MibIdentifier((1, 3, 6, 1, 4, 1, 3873))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1))
qlasp = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2))
qlaspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2))
qlaspTeamStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1))
qlaspPhyAdapterStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2))
qlaspVirAdapterStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3))
btsTeamNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsTeamNumber.setStatus('mandatory')
btsTeamTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2), )
if mibBuilder.loadTexts: btsTeamTable.setStatus('mandatory')
btsTeamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1), ).setIndexNames((0, "QLASP-Statistics-MIB", "btsTeamIndex"))
if mibBuilder.loadTexts: btsTeamEntry.setStatus('mandatory')
btsTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btsTeamIndex.setStatus('mandatory')
btsTeamName = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsTeamName.setStatus('mandatory')
btsPhyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPhyNumber.setStatus('mandatory')
btsVirNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsVirNumber.setStatus('mandatory')
btsPacketSends = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketSends.setStatus('mandatory')
btsPacketSendDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketSendDiscardeds.setStatus('mandatory')
btsPacketSendQueueds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketSendQueueds.setStatus('mandatory')
btsPacketRecvs = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketRecvs.setStatus('mandatory')
btsPacketRecvDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPacketRecvDiscardeds.setStatus('mandatory')
btsLinkPacketsSents = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsLinkPacketsSents.setStatus('mandatory')
btsLinkPacketsRetrieds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsLinkPacketsRetrieds.setStatus('mandatory')
btsPhyAdapterNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsPhyAdapterNumber.setStatus('mandatory')
btsPhyAdapterStatTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2), )
if mibBuilder.loadTexts: btsPhyAdapterStatTable.setStatus('mandatory')
btsPhyAdapterStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1), ).setIndexNames((0, "QLASP-Statistics-MIB", "btspTeamIndex"), (0, "QLASP-Statistics-MIB", "btspAdapterIndex"))
if mibBuilder.loadTexts: btsPhyAdapterStatEntry.setStatus('mandatory')
btspTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btspTeamIndex.setStatus('mandatory')
btspAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btspAdapterIndex.setStatus('mandatory')
btspAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspAdapterDesc.setStatus('mandatory')
btspPacketSends = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketSends.setStatus('mandatory')
btspPacketSendDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketSendDiscardeds.setStatus('mandatory')
btspPacketRecvs = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketRecvs.setStatus('mandatory')
btspPacketRecvDiscardeds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspPacketRecvDiscardeds.setStatus('mandatory')
btspLinkPacketsSents = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspLinkPacketsSents.setStatus('mandatory')
btspLinkPacketsRetrieds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btspLinkPacketsRetrieds.setStatus('mandatory')
btsVirAdapterNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsVirAdapterNumber.setStatus('mandatory')
btsVirAdapterStatTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2), )
if mibBuilder.loadTexts: btsVirAdapterStatTable.setStatus('mandatory')
btsVirAdapterStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2, 1), ).setIndexNames((0, "QLASP-Statistics-MIB", "btsvTeamIndex"), (0, "QLASP-Statistics-MIB", "btsvAdapterIndex"))
if mibBuilder.loadTexts: btsVirAdapterStatEntry.setStatus('mandatory')
btsvTeamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btsvTeamIndex.setStatus('mandatory')
btsvAdapterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: btsvAdapterIndex.setStatus('mandatory')
btsvAdapterDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvAdapterDesc.setStatus('mandatory')
btsvPacketSends = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvPacketSends.setStatus('mandatory')
btsvPacketSendQueueds = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvPacketSendQueueds.setStatus('mandatory')
btsvPacketRecvs = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: btsvPacketRecvs.setStatus('mandatory')
mibBuilder.exportSymbols("QLASP-Statistics-MIB", btspPacketRecvs=btspPacketRecvs, qlaspStat=qlaspStat, btspTeamIndex=btspTeamIndex, qlasp=qlasp, btsTeamEntry=btsTeamEntry, btsPacketSends=btsPacketSends, btspPacketSendDiscardeds=btspPacketSendDiscardeds, btsPhyAdapterNumber=btsPhyAdapterNumber, btsPhyAdapterStatEntry=btsPhyAdapterStatEntry, btsvPacketSends=btsvPacketSends, btsLinkPacketsSents=btsLinkPacketsSents, btsvTeamIndex=btsvTeamIndex, btsPacketSendDiscardeds=btsPacketSendDiscardeds, btsPhyAdapterStatTable=btsPhyAdapterStatTable, btspLinkPacketsSents=btspLinkPacketsSents, btsTeamIndex=btsTeamIndex, btsvAdapterIndex=btsvAdapterIndex, btsvAdapterDesc=btsvAdapterDesc, qlaspVirAdapterStat=qlaspVirAdapterStat, btsVirAdapterNumber=btsVirAdapterNumber, btsTeamNumber=btsTeamNumber, btsTeamName=btsTeamName, btsLinkPacketsRetrieds=btsLinkPacketsRetrieds, enet=enet, btsPhyNumber=btsPhyNumber, btspAdapterDesc=btspAdapterDesc, btsPacketSendQueueds=btsPacketSendQueueds, btspPacketRecvDiscardeds=btspPacketRecvDiscardeds, btsvPacketSendQueueds=btsvPacketSendQueueds, btsVirNumber=btsVirNumber, btsVirAdapterStatEntry=btsVirAdapterStatEntry, btsTeamTable=btsTeamTable, qlaspPhyAdapterStat=qlaspPhyAdapterStat, btsVirAdapterStatTable=btsVirAdapterStatTable, qlogic=qlogic, qlaspTeamStat=qlaspTeamStat, btsvPacketRecvs=btsvPacketRecvs, btsPacketRecvDiscardeds=btsPacketRecvDiscardeds, btspAdapterIndex=btspAdapterIndex, btspLinkPacketsRetrieds=btspLinkPacketsRetrieds, btspPacketSends=btspPacketSends, btsPacketRecvs=btsPacketRecvs)
