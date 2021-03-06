#
# PySNMP MIB module Juniper-DHCPv6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DHCPv6-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
Ipv6AddressPrefix, = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, TimeTicks, NotificationType, Integer32, Counter32, iso, Bits, Counter64, IpAddress, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "NotificationType", "Integer32", "Counter32", "iso", "Bits", "Counter64", "IpAddress", "Unsigned32", "Gauge32", "MibIdentifier")
TimeInterval, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TruthValue", "TextualConvention", "DisplayString")
juniDhcpv6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69))
juniDhcpv6MIB.setRevisions(('2003-05-08 17:15',))
if mibBuilder.loadTexts: juniDhcpv6MIB.setLastUpdated('200305081715Z')
if mibBuilder.loadTexts: juniDhcpv6MIB.setOrganization('Juniper Networks, Inc.')
class JuniDhcpv6LocalServerModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("localServerModeTypeEqualAccess", 1), ("localServerModeTypeStandalone", 2))

juniDhcpv6Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1))
juniDhcpv6LocalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1))
juniDhcpv6LocalServerStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1))
juniDhcpv6LocalServerAttributes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 2))
juniDhcpv6LocalServerBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3))
juniDhcpv6LocalServerMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerMemUsage.setStatus('current')
juniDhcpv6LocalServerNumBindings = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerNumBindings.setStatus('current')
juniDhcpv6LocalServerRxSolicits = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxSolicits.setStatus('current')
juniDhcpv6LocalServerRxAccepts = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxAccepts.setStatus('current')
juniDhcpv6LocalServerRxRenews = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxRenews.setStatus('current')
juniDhcpv6LocalServerRxDeclines = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxDeclines.setStatus('current')
juniDhcpv6LocalServerRxReleases = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxReleases.setStatus('current')
juniDhcpv6LocalServerRxInforms = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxInforms.setStatus('current')
juniDhcpv6LocalServerRxConfirms = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxConfirms.setStatus('current')
juniDhcpv6LocalServerRxRebinds = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerRxRebinds.setStatus('current')
juniDhcpv6LocalServerTxReconfigures = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerTxReconfigures.setStatus('current')
juniDhcpv6LocalServerTxAdvertises = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerTxAdvertises.setStatus('current')
juniDhcpv6LocalServerTxSuccessfulReplies = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerTxSuccessfulReplies.setStatus('current')
juniDhcpv6LocalServerTxFailedReplies = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerTxFailedReplies.setStatus('current')
juniDhcpv6LocalServerUnknownMessages = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerUnknownMessages.setStatus('current')
juniDhcpv6LocalServerBadMessages = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerBadMessages.setStatus('current')
juniDhcpv6LocalServerPacketsIn = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerPacketsIn.setStatus('current')
juniDhcpv6LocalServerPacketsOut = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerPacketsOut.setStatus('current')
juniDhcpv6LocalServerBindingsTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1), )
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsTable.setStatus('current')
juniDhcpv6LocalServerBindingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1), ).setIndexNames((0, "Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsPrefix"), (0, "Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsLength"))
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsEntry.setStatus('current')
juniDhcpv6LocalServerBindingsPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsPrefix.setStatus('current')
juniDhcpv6LocalServerBindingsLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)))
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsLength.setStatus('current')
juniDhcpv6LocalServerBindingsClientDuid = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 130))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsClientDuid.setStatus('current')
juniDhcpv6LocalServerBindingsInfinite = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsInfinite.setStatus('current')
juniDhcpv6LocalServerBindingsExpireTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 5), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsExpireTime.setStatus('current')
juniDhcpv6LocalServerBindingsIf = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 3, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerBindingsIf.setStatus('current')
juniDhcpv6LocalServerAttributesMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 1, 1, 2, 1), JuniDhcpv6LocalServerModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDhcpv6LocalServerAttributesMode.setStatus('current')
juniDhcpv6MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2))
juniDhcpv6MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 1))
juniDhcpv6MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 2))
juniDhcpv6Compliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 1, 1)).setObjects(("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpv6Compliance2 = juniDhcpv6Compliance2.setStatus('current')
juniDhcpv6LocalServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 69, 2, 2, 1)).setObjects(("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerMemUsage"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerNumBindings"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxSolicits"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxAccepts"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxRenews"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxDeclines"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxReleases"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxInforms"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxConfirms"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerRxRebinds"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxReconfigures"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxAdvertises"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxSuccessfulReplies"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerTxFailedReplies"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerUnknownMessages"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBadMessages"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerPacketsIn"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerPacketsOut"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsClientDuid"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsInfinite"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsExpireTime"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerBindingsIf"), ("Juniper-DHCPv6-MIB", "juniDhcpv6LocalServerAttributesMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpv6LocalServerGroup = juniDhcpv6LocalServerGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-DHCPv6-MIB", juniDhcpv6LocalServerStatistics=juniDhcpv6LocalServerStatistics, juniDhcpv6MIBCompliances=juniDhcpv6MIBCompliances, juniDhcpv6LocalServerBindingsIf=juniDhcpv6LocalServerBindingsIf, juniDhcpv6LocalServerMemUsage=juniDhcpv6LocalServerMemUsage, juniDhcpv6LocalServerPacketsOut=juniDhcpv6LocalServerPacketsOut, juniDhcpv6LocalServerNumBindings=juniDhcpv6LocalServerNumBindings, juniDhcpv6LocalServerBindingsPrefix=juniDhcpv6LocalServerBindingsPrefix, juniDhcpv6LocalServerRxRenews=juniDhcpv6LocalServerRxRenews, juniDhcpv6MIB=juniDhcpv6MIB, juniDhcpv6LocalServerRxAccepts=juniDhcpv6LocalServerRxAccepts, juniDhcpv6LocalServerBindingsEntry=juniDhcpv6LocalServerBindingsEntry, juniDhcpv6LocalServerBindings=juniDhcpv6LocalServerBindings, juniDhcpv6LocalServerUnknownMessages=juniDhcpv6LocalServerUnknownMessages, juniDhcpv6LocalServerBindingsLength=juniDhcpv6LocalServerBindingsLength, juniDhcpv6Objects=juniDhcpv6Objects, juniDhcpv6MIBConformance=juniDhcpv6MIBConformance, juniDhcpv6LocalServerTxSuccessfulReplies=juniDhcpv6LocalServerTxSuccessfulReplies, juniDhcpv6LocalServerPacketsIn=juniDhcpv6LocalServerPacketsIn, juniDhcpv6LocalServerBindingsClientDuid=juniDhcpv6LocalServerBindingsClientDuid, juniDhcpv6LocalServerRxRebinds=juniDhcpv6LocalServerRxRebinds, juniDhcpv6LocalServerBindingsTable=juniDhcpv6LocalServerBindingsTable, juniDhcpv6LocalServerBadMessages=juniDhcpv6LocalServerBadMessages, juniDhcpv6LocalServerTxReconfigures=juniDhcpv6LocalServerTxReconfigures, juniDhcpv6LocalServerTxAdvertises=juniDhcpv6LocalServerTxAdvertises, juniDhcpv6LocalServerRxConfirms=juniDhcpv6LocalServerRxConfirms, juniDhcpv6LocalServerAttributes=juniDhcpv6LocalServerAttributes, JuniDhcpv6LocalServerModeType=JuniDhcpv6LocalServerModeType, juniDhcpv6LocalServerRxDeclines=juniDhcpv6LocalServerRxDeclines, juniDhcpv6MIBGroups=juniDhcpv6MIBGroups, juniDhcpv6LocalServerBindingsExpireTime=juniDhcpv6LocalServerBindingsExpireTime, juniDhcpv6LocalServerAttributesMode=juniDhcpv6LocalServerAttributesMode, juniDhcpv6LocalServerGroup=juniDhcpv6LocalServerGroup, juniDhcpv6Compliance2=juniDhcpv6Compliance2, juniDhcpv6LocalServerTxFailedReplies=juniDhcpv6LocalServerTxFailedReplies, juniDhcpv6LocalServerRxReleases=juniDhcpv6LocalServerRxReleases, juniDhcpv6LocalServerRxSolicits=juniDhcpv6LocalServerRxSolicits, PYSNMP_MODULE_ID=juniDhcpv6MIB, juniDhcpv6LocalServerRxInforms=juniDhcpv6LocalServerRxInforms, juniDhcpv6LocalServerObjects=juniDhcpv6LocalServerObjects, juniDhcpv6LocalServerBindingsInfinite=juniDhcpv6LocalServerBindingsInfinite)
