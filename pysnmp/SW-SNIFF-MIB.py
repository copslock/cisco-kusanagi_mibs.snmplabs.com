#
# PySNMP MIB module SW-SNIFF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW-SNIFF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, iso, Gauge32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, NotificationType, IpAddress, enterprises, Bits, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "iso", "Gauge32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "NotificationType", "IpAddress", "enterprises", "Bits", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
marconi = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
external = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
dlinkcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
es2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
marconi_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("marconi-mgmt")
es2000Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28))
swL2Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2))
swPortSniff = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 5))
swSniffCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 5, 1), )
if mibBuilder.loadTexts: swSniffCtrlTable.setStatus('mandatory')
swSniffCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 5, 1, 1), ).setIndexNames((0, "SW-SNIFF-MIB", "swSniffIndex"))
if mibBuilder.loadTexts: swSniffCtrlEntry.setStatus('mandatory')
swSniffIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSniffIndex.setStatus('mandatory')
swSniffSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSniffSourcePort.setStatus('mandatory')
swSniffTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSniffTargetPort.setStatus('mandatory')
swSniffState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSniffState.setStatus('mandatory')
mibBuilder.exportSymbols("SW-SNIFF-MIB", external=external, es2000=es2000, golfcommon=golfcommon, systems=systems, marconi=marconi, es2000Mgmt=es2000Mgmt, swSniffState=swSniffState, swPortSniff=swPortSniff, swSniffIndex=swSniffIndex, golfproducts=golfproducts, dlinkcommon=dlinkcommon, golf=golf, swSniffCtrlTable=swSniffCtrlTable, swSniffCtrlEntry=swSniffCtrlEntry, marconi_mgmt=marconi_mgmt, swSniffTargetPort=swSniffTargetPort, dlink=dlink, swSniffSourcePort=swSniffSourcePort, swL2Mgmt=swL2Mgmt)
