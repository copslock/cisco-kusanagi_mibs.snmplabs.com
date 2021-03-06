#
# PySNMP MIB module Unisphere-Data-Registry (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Registry
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, TimeTicks, ObjectIdentity, Counter32, Counter64, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "TimeTicks", "ObjectIdentity", "Counter32", "Counter64", "iso", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usAdmin, = mibBuilder.importSymbols("Unisphere-SMI", "usAdmin")
usDataAdmin = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2))
usDataAdmin.setRevisions(('2001-09-25 15:25', '2001-06-01 21:18',))
if mibBuilder.loadTexts: usDataAdmin.setLastUpdated('200109251525Z')
if mibBuilder.loadTexts: usDataAdmin.setOrganization('Unisphere Networks, Inc.')
usDataRegistry = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 1))
if mibBuilder.loadTexts: usDataRegistry.setStatus('current')
usdErxRegistry = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2))
usdMrxRegistry = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2, 3))
usDataEntPhysicalType = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1))
usdPcmciaFlashCard = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1))
if mibBuilder.loadTexts: usdPcmciaFlashCard.setStatus('current')
usd85MegT2FlashCard = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 1))
if mibBuilder.loadTexts: usd85MegT2FlashCard.setStatus('current')
usd220MegT2FlashCard = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 2))
if mibBuilder.loadTexts: usd220MegT2FlashCard.setStatus('current')
usdTraceRouteImplementationTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 2))
usdTraceRouteUsingIcmpProbe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 2, 1))
if mibBuilder.loadTexts: usdTraceRouteUsingIcmpProbe.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Registry", usDataAdmin=usDataAdmin, usd220MegT2FlashCard=usd220MegT2FlashCard, usdErxRegistry=usdErxRegistry, usd85MegT2FlashCard=usd85MegT2FlashCard, usdPcmciaFlashCard=usdPcmciaFlashCard, PYSNMP_MODULE_ID=usDataAdmin, usdMrxRegistry=usdMrxRegistry, usDataRegistry=usDataRegistry, usdTraceRouteImplementationTypes=usdTraceRouteImplementationTypes, usDataEntPhysicalType=usDataEntPhysicalType, usdTraceRouteUsingIcmpProbe=usdTraceRouteUsingIcmpProbe)
