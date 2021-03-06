#
# PySNMP MIB module BRIDGEEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BRIDGEEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bridgeExt, = mibBuilder.importSymbols("APENT-MIB", "bridgeExt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, TimeTicks, MibIdentifier, Unsigned32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, IpAddress, Counter32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "TimeTicks", "MibIdentifier", "Unsigned32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "IpAddress", "Counter32", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Timeout(Integer32):
    pass

apBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1))
apBridgeMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 1), Timeout().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeMaxAge.setReference('IEEE 802.1D-1990: Section 4.5.3.8')
if mibBuilder.loadTexts: apBridgeMaxAge.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgeMaxAge.setDescription('The value that all bridges use for MaxAge when this bridge is acting as the root. Note that 802.1D-1990 specifies that the range for this parameter is related to the value of dot1dStpBridgeHelloTime.')
apBridgeHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 2), Timeout().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeHelloTime.setReference('IEEE 802.1D-1990: Section 4.5.3.9')
if mibBuilder.loadTexts: apBridgeHelloTime.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgeHelloTime.setDescription('The value that all bridges use for HelloTime when this bridge is acting as the root.')
apBridgeForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 3), Timeout().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeForwardDelay.setReference('IEEE 802.1D-1990: Section 4.5.3.10')
if mibBuilder.loadTexts: apBridgeForwardDelay.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgeForwardDelay.setDescription('The value that all bridges use for ForwardDelay when this bridge is acting as the root. Note that 802.1D-1990 specifies that the range for this parameter is related to the value of dot1dStpBridgeMaxAge.')
apBridgePortTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4), )
if mibBuilder.loadTexts: apBridgePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgePortTable.setDescription('A table that contains generic information about every port that is associated with this bridge.')
apBridgePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1), ).setIndexNames((0, "BRIDGEEXT-MIB", "apBridgePort"))
if mibBuilder.loadTexts: apBridgePortEntry.setReference('IEEE 802.1D-1990: Section 6.4.2, 6.6.1')
if mibBuilder.loadTexts: apBridgePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgePortEntry.setDescription('A list of information for each port of the bridge.')
apBridgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBridgePort.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgePort.setDescription('The port number of the port for which this entry contains bridge management information.')
apBridgePortVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgePortVlan.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgePortVlan.setDescription('The virtual local area network number (VLAN) to associate with this port.')
apBridgeSpanningTreeState = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeSpanningTreeState.setStatus('mandatory')
if mibBuilder.loadTexts: apBridgeSpanningTreeState.setDescription('This allows spanning-tree to be enabled/disabled on the unit.')
mibBuilder.exportSymbols("BRIDGEEXT-MIB", Timeout=Timeout, apBridgeForwardDelay=apBridgeForwardDelay, apBridgePort=apBridgePort, apBridge=apBridge, apBridgeSpanningTreeState=apBridgeSpanningTreeState, apBridgeHelloTime=apBridgeHelloTime, apBridgePortTable=apBridgePortTable, apBridgePortVlan=apBridgePortVlan, apBridgePortEntry=apBridgePortEntry, apBridgeMaxAge=apBridgeMaxAge)
