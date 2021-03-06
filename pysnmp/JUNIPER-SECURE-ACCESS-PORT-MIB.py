#
# PySNMP MIB module JUNIPER-SECURE-ACCESS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SECURE-ACCESS-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
jnxExSecureAccessPort, = mibBuilder.importSymbols("JUNIPER-EX-SMI", "jnxExSecureAccessPort")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, iso, Counter64, IpAddress, Bits, Unsigned32, ModuleIdentity, Counter32, Gauge32, ObjectIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "iso", "Counter64", "IpAddress", "Bits", "Unsigned32", "ModuleIdentity", "Counter32", "Gauge32", "ObjectIdentity", "MibIdentifier", "NotificationType")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
jnxExSecureAccessPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1))
if mibBuilder.loadTexts: jnxExSecureAccessPortMIB.setLastUpdated('200705151000Z')
if mibBuilder.loadTexts: jnxExSecureAccessPortMIB.setOrganization('Juniper Networks, Inc.')
jnxSecAccessPortMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0))
jnxSecAccessPortMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1))
class JnxMacLimitExceededAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("drop", 2), ("alarm", 3), ("shutdown", 4))

jnxSecAccessPortVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1), )
if mibBuilder.loadTexts: jnxSecAccessPortVlanTable.setStatus('current')
jnxSecAccessPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1), ).setIndexNames((0, "JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessVlanName"))
if mibBuilder.loadTexts: jnxSecAccessPortVlanEntry.setStatus('current')
jnxSecAccessVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: jnxSecAccessVlanName.setStatus('current')
jnxSecAccessVlanDhcpSnoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessVlanDhcpSnoopStatus.setStatus('current')
jnxSecAccessVlanDAIStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessVlanDAIStatus.setStatus('current')
jnxSecAccessPortIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2), )
if mibBuilder.loadTexts: jnxSecAccessPortIfTable.setStatus('current')
jnxSecAccessPortIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxSecAccessPortIfEntry.setStatus('current')
jnxSecAccessdsIfTrustState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessdsIfTrustState.setStatus('current')
jnxSecAccessdsIfRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 2), Unsigned32()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessdsIfRateLimit.setStatus('current')
jnxSecAccessIfMacLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 3), Unsigned32().clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessIfMacLimit.setStatus('current')
jnxSecAccessIfMacLimitExceed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 4), JnxMacLimitExceededAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessIfMacLimitExceed.setStatus('current')
jnxSecAccessIfIpSrcGuardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessIfIpSrcGuardStatus.setStatus('current')
jnxSecAccessIfMacSrcGuardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSecAccessIfMacSrcGuardStatus.setStatus('current')
jnxStormCtlTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3), )
if mibBuilder.loadTexts: jnxStormCtlTable.setStatus('current')
jnxStormCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxStormCtlIfTrafficType"))
if mibBuilder.loadTexts: jnxStormCtlEntry.setStatus('current')
jnxStormCtlIfTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("broadcast", 1), ("multicast", 2), ("unicast", 3))))
if mibBuilder.loadTexts: jnxStormCtlIfTrafficType.setStatus('current')
jnxStormCtlRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 2), Integer32()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStormCtlRisingThreshold.setStatus('current')
jnxStormCtlFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 3), Integer32()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStormCtlFallingThreshold.setStatus('current')
jnxStormCtlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shutdown", 1), ("filter", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxStormCtlAction.setStatus('current')
jnxSecAccessdsRateLimitCrossed = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0, 1)).setObjects(("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessdsIfRateLimit"))
if mibBuilder.loadTexts: jnxSecAccessdsRateLimitCrossed.setStatus('current')
jnxSecAccessIfMacLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0, 2)).setObjects(("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessIfMacLimit"), ("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessIfMacLimitExceed"))
if mibBuilder.loadTexts: jnxSecAccessIfMacLimitExceeded.setStatus('current')
jnxStormEventNotification = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0, 3)).setObjects(("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxStormCtlRisingThreshold"))
if mibBuilder.loadTexts: jnxStormEventNotification.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-SECURE-ACCESS-PORT-MIB", jnxSecAccessPortMIBNotifications=jnxSecAccessPortMIBNotifications, jnxSecAccessVlanDhcpSnoopStatus=jnxSecAccessVlanDhcpSnoopStatus, jnxSecAccessIfMacLimitExceed=jnxSecAccessIfMacLimitExceed, jnxStormCtlFallingThreshold=jnxStormCtlFallingThreshold, jnxSecAccessIfIpSrcGuardStatus=jnxSecAccessIfIpSrcGuardStatus, jnxSecAccessPortIfTable=jnxSecAccessPortIfTable, JnxMacLimitExceededAction=JnxMacLimitExceededAction, jnxSecAccessIfMacSrcGuardStatus=jnxSecAccessIfMacSrcGuardStatus, jnxSecAccessPortMIBObjects=jnxSecAccessPortMIBObjects, jnxStormCtlAction=jnxStormCtlAction, jnxStormCtlEntry=jnxStormCtlEntry, jnxSecAccessdsIfTrustState=jnxSecAccessdsIfTrustState, jnxSecAccessdsRateLimitCrossed=jnxSecAccessdsRateLimitCrossed, jnxStormCtlIfTrafficType=jnxStormCtlIfTrafficType, jnxExSecureAccessPortMIB=jnxExSecureAccessPortMIB, jnxStormEventNotification=jnxStormEventNotification, jnxStormCtlRisingThreshold=jnxStormCtlRisingThreshold, jnxStormCtlTable=jnxStormCtlTable, jnxSecAccessPortVlanTable=jnxSecAccessPortVlanTable, jnxSecAccessdsIfRateLimit=jnxSecAccessdsIfRateLimit, jnxSecAccessIfMacLimit=jnxSecAccessIfMacLimit, jnxSecAccessVlanName=jnxSecAccessVlanName, jnxSecAccessPortVlanEntry=jnxSecAccessPortVlanEntry, jnxSecAccessPortIfEntry=jnxSecAccessPortIfEntry, jnxSecAccessVlanDAIStatus=jnxSecAccessVlanDAIStatus, PYSNMP_MODULE_ID=jnxExSecureAccessPortMIB, jnxSecAccessIfMacLimitExceeded=jnxSecAccessIfMacLimitExceeded)
