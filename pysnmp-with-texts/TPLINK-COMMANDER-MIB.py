#
# PySNMP MIB module TPLINK-COMMANDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-COMMANDER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, ModuleIdentity, ObjectIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, MibIdentifier, IpAddress, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "MibIdentifier", "IpAddress", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clusterManage, = mibBuilder.importSymbols("TPLINK-CLUSTER-MIB", "clusterManage")
clusterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2))
commanderConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4))
clusterName = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterName.setStatus('current')
if mibBuilder.loadTexts: clusterName.setDescription('This object indicates the name of the cluster if the role of the switch is commander. The minimum length is 1, maximum length is 16. The cluster name can not contain any of the char ,&<>\\.')
clusterHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterHoldTime.setStatus('current')
if mibBuilder.loadTexts: clusterHoldTime.setDescription('This object indicates the time that the cluster infomation will keep in the commander switch. The mininum value is 1, maximum value is 255.')
clusterIntervalTime = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterIntervalTime.setStatus('current')
if mibBuilder.loadTexts: clusterIntervalTime.setDescription('This object indicates the interval time of the switch in second to periodical send out handshake packet. The minimum valus is 1, maximum value is 255.')
commanderClusterName = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commanderClusterName.setStatus('current')
if mibBuilder.loadTexts: commanderClusterName.setDescription('This object use to set the cluster name when building the cluster. The minimum length is 1, maximum length is 16. The cluster name can not contain any of the char ,&<>\\.')
clusterIp = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterIp.setStatus('current')
if mibBuilder.loadTexts: clusterIp.setDescription('This object use to set the cluster ip pool when building the cluster.')
clusterIpMask = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterIpMask.setStatus('current')
if mibBuilder.loadTexts: clusterIpMask.setDescription('This object use to set the cluster ip mask when building the cluster.')
clusterCommit = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("commit", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clusterCommit.setStatus('current')
if mibBuilder.loadTexts: clusterCommit.setDescription('This object use to commit the data to build the cluster.')
mibBuilder.exportSymbols("TPLINK-COMMANDER-MIB", clusterIp=clusterIp, clusterHoldTime=clusterHoldTime, clusterIntervalTime=clusterIntervalTime, commanderClusterName=commanderClusterName, clusterIpMask=clusterIpMask, commanderConfig=commanderConfig, clusterCommit=clusterCommit, clusterConfig=clusterConfig, clusterName=clusterName)
