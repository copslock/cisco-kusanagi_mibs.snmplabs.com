#
# PySNMP MIB module Cajun-ROOT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Cajun-ROOT
# Produced by pysmi-0.3.4 at Wed May  1 11:24:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, iso, ModuleIdentity, TimeTicks, Unsigned32, Bits, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter64, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "iso", "ModuleIdentity", "TimeTicks", "Unsigned32", "Bits", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter64", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2))
cajunRtrProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 43))
cajunRtr = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 43))
if mibBuilder.loadTexts: cajunRtr.setLastUpdated('9904220000Z')
if mibBuilder.loadTexts: cajunRtr.setOrganization("Lucent's Concord Technology Center (CTC) ")
if mibBuilder.loadTexts: cajunRtr.setContactInfo('Erick M. Crowell -- ecrowell@lucent.com, Raj Duggal -- rduggal@lucent.com, Ira Steckler -- isteckler@lucent.com')
if mibBuilder.loadTexts: cajunRtr.setDescription('Cajun p550 / p660 / p880 Routing Private Mib top level Architecture.')
cjnSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 1))
cjnProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2))
cjnMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3))
cjnCli = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 1, 1))
cjnDload = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 1, 2))
cjnIpv4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 1))
cjnIpv6 = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 2))
cjnIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 3))
cjnAtalk = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 4))
cjnIpv4Serv = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5))
cjnIpv6Serv = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 6))
cjnIpxServ = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 7))
cjnAtalkServ = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 8))
cjnOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 9))
cjnRip = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10))
cjnIgmp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11))
cjnRtm = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 12))
cjnDvmrp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 13))
cjnPimSm = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 14))
cjnPimDm = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 15))
cjnRsvp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 16))
cjnSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 17))
cjnBgp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 18))
cjnLrrp = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 19))
cjnIpxRip = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20))
cjnIpxSap = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 21))
cjnIpIfMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1))
cjnIpxIfMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 2))
cjnAtalkIfMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 3))
cjnResourceMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 4))
cjnIpAListMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 5))
cjnIpForwardCtlMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 6))
cjnIpFwdMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 7))
mibBuilder.exportSymbols("Cajun-ROOT", cjnIpv6Serv=cjnIpv6Serv, cjnSystem=cjnSystem, cjnIpx=cjnIpx, cjnIpxServ=cjnIpxServ, cjnIpIfMgmt=cjnIpIfMgmt, PYSNMP_MODULE_ID=cajunRtr, cjnBgp=cjnBgp, cjnIpxRip=cjnIpxRip, cjnSnmp=cjnSnmp, cjnIpxSap=cjnIpxSap, cjnRsvp=cjnRsvp, cjnAtalkServ=cjnAtalkServ, cjnLrrp=cjnLrrp, cjnIpv4Serv=cjnIpv4Serv, cjnProtocol=cjnProtocol, cjnIpForwardCtlMgt=cjnIpForwardCtlMgt, cjnCli=cjnCli, cjnIgmp=cjnIgmp, cajunRtrProduct=cajunRtrProduct, mibs=mibs, cajunRtr=cajunRtr, cjnIpv6=cjnIpv6, cjnResourceMgr=cjnResourceMgr, cjnRip=cjnRip, cjnPimDm=cjnPimDm, cjnRtm=cjnRtm, cjnIpv4=cjnIpv4, cjnIpxIfMgmt=cjnIpxIfMgmt, cjnAtalkIfMgmt=cjnAtalkIfMgmt, cjnAtalk=cjnAtalk, cjnDload=cjnDload, cjnPimSm=cjnPimSm, cjnDvmrp=cjnDvmrp, cjnIpAListMgmt=cjnIpAListMgmt, lucent=lucent, products=products, cjnOspf=cjnOspf, cjnMgmt=cjnMgmt, cjnIpFwdMgmt=cjnIpFwdMgmt)
