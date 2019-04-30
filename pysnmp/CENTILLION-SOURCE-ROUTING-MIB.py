#
# PySNMP MIB module CENTILLION-SOURCE-ROUTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-SOURCE-ROUTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
cndot1dSr, = mibBuilder.importSymbols("CENTILLION-BRIDGE-MIB", "cndot1dSr")
EnableIndicator, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "EnableIndicator")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, Unsigned32, NotificationType, Counter64, ModuleIdentity, Integer32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "Unsigned32", "NotificationType", "Counter64", "ModuleIdentity", "Integer32", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cndot1dSrPortTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1), )
if mibBuilder.loadTexts: cndot1dSrPortTable.setStatus('mandatory')
cndot1dSrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1), ).setIndexNames((0, "CENTILLION-SOURCE-ROUTING-MIB", "cndot1dSrPort"))
if mibBuilder.loadTexts: cndot1dSrPortEntry.setStatus('mandatory')
cndot1dSrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndot1dSrPort.setStatus('mandatory')
cndot1dSrPortAREHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cndot1dSrPortAREHopCount.setStatus('mandatory')
cndot1dSrPortSTEHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cndot1dSrPortSTEHopCount.setStatus('mandatory')
cndot1dSrExplorerProxy = MibScalar((1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 3), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cndot1dSrExplorerProxy.setStatus('mandatory')
cndot1dSrBridgeNum = MibScalar((1, 3, 6, 1, 4, 1, 930, 3, 17, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cndot1dSrBridgeNum.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-SOURCE-ROUTING-MIB", cndot1dSrPortTable=cndot1dSrPortTable, cndot1dSrPortAREHopCount=cndot1dSrPortAREHopCount, cndot1dSrExplorerProxy=cndot1dSrExplorerProxy, cndot1dSrPortEntry=cndot1dSrPortEntry, cndot1dSrPortSTEHopCount=cndot1dSrPortSTEHopCount, cndot1dSrPort=cndot1dSrPort, cndot1dSrBridgeNum=cndot1dSrBridgeNum)