#
# PySNMP MIB module APERTUS-UA-FALLBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APERTUS-UA-FALLBACK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, mib_2, ObjectIdentity, NotificationType, MibIdentifier, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, IpAddress, Counter64, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "mib-2", "ObjectIdentity", "NotificationType", "MibIdentifier", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "IpAddress", "Counter64", "Unsigned32", "Integer32", "TimeTicks")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
apertus = MibIdentifier((1, 3, 6, 1, 4, 1, 543))
isg = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3))
aperua = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3))
aperfallback = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3))
aperFallbackMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1))
aperFallbackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1))
aperFallbackConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1))
aperFallbackDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2))
aperFallbackNode = MibIdentifier((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3))
aperFallbackConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ready", 1), ("loading", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackConfigStatus.setStatus('mandatory')
aperFallbackConfigUpTime = MibScalar((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackConfigUpTime.setStatus('mandatory')
aperFallbackDomainTable = MibTable((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1), )
if mibBuilder.loadTexts: aperFallbackDomainTable.setStatus('mandatory')
aperFallbackDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1), ).setIndexNames((0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackDomainName"))
if mibBuilder.loadTexts: aperFallbackDomainEntry.setStatus('mandatory')
aperFallbackDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackDomainName.setStatus('mandatory')
aperFallbackDomainUpServers = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackDomainUpServers.setStatus('mandatory')
aperFallbackDomainDownServers = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackDomainDownServers.setStatus('mandatory')
aperFallbackNodeTable = MibTable((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1), )
if mibBuilder.loadTexts: aperFallbackNodeTable.setStatus('mandatory')
aperFallbackNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1), ).setIndexNames((0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackNodeName"), (0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackNodeIP"))
if mibBuilder.loadTexts: aperFallbackNodeEntry.setStatus('mandatory')
aperFallbackNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeName.setStatus('mandatory')
aperFallbackNodeIP = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeIP.setStatus('mandatory')
aperFallbackNodeHostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeHostIndex.setStatus('mandatory')
aperFallbackNodePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodePoolIndex.setStatus('mandatory')
aperFallbackNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notqueried", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeStatus.setStatus('mandatory')
aperFallbackNodeResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aperFallbackNodeResponseTime.setStatus('mandatory')
mibBuilder.exportSymbols("APERTUS-UA-FALLBACK-MIB", isg=isg, aperFallbackNodeStatus=aperFallbackNodeStatus, aperFallbackNodeResponseTime=aperFallbackNodeResponseTime, aperua=aperua, internet=internet, private=private, aperFallbackNodePoolIndex=aperFallbackNodePoolIndex, aperfallback=aperfallback, enterprises=enterprises, aperFallbackMIB=aperFallbackMIB, aperFallbackNodeEntry=aperFallbackNodeEntry, aperFallbackConfig=aperFallbackConfig, aperFallbackNodeTable=aperFallbackNodeTable, apertus=apertus, aperFallbackDomainEntry=aperFallbackDomainEntry, aperFallbackDomainDownServers=aperFallbackDomainDownServers, aperFallbackDomainUpServers=aperFallbackDomainUpServers, aperFallbackNodeName=aperFallbackNodeName, aperFallbackMIBObjects=aperFallbackMIBObjects, aperFallbackConfigUpTime=aperFallbackConfigUpTime, aperFallbackConfigStatus=aperFallbackConfigStatus, directory=directory, mgmt=mgmt, aperFallbackDomain=aperFallbackDomain, aperFallbackNodeHostIndex=aperFallbackNodeHostIndex, aperFallbackNodeIP=aperFallbackNodeIP, aperFallbackNode=aperFallbackNode, aperFallbackDomainTable=aperFallbackDomainTable, aperFallbackDomainName=aperFallbackDomainName, experimental=experimental)
