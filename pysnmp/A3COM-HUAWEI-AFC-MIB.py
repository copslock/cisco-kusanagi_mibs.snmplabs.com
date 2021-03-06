#
# PySNMP MIB module A3COM-HUAWEI-AFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-AFC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:49:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, Counter64, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Bits, ModuleIdentity, IpAddress, iso, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Bits", "ModuleIdentity", "IpAddress", "iso", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cAFC = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85))
h3cAFC.setRevisions(('2008-07-23 00:00',))
if mibBuilder.loadTexts: h3cAFC.setLastUpdated('200807230000Z')
if mibBuilder.loadTexts: h3cAFC.setOrganization('H3C Technologies Co., Ltd.')
h3cAFCLeaf = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1))
h3cDDosAttackTargetIP = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDDosAttackTargetIP.setStatus('current')
h3cDDosAttackType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 18, 19, 20, 24, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 1024))).clone(namedValues=NamedValues(("land", 1), ("smurf", 2), ("fraggle", 3), ("winnuke", 4), ("synflood", 5), ("icmpflood", 6), ("udpflood", 7), ("icmpredirect", 8), ("icmpunreachable", 9), ("tracert", 11), ("tcpflag", 12), ("pingofdeath", 13), ("teardrop", 14), ("ipfragment", 15), ("largeicmp", 18), ("sourceroute", 19), ("routerecord", 20), ("fragflood", 24), ("scan", 27), ("appstreamalarm", 29), ("sessionstreamalarm", 30), ("tcpabnormal", 32), ("ipfragabnormal", 33), ("tftpabnormal", 34), ("dnsabnormal", 35), ("httpabnormal", 36), ("telnetabnormal", 37), ("ftpabnormal", 38), ("smtpabnormal", 39), ("pop3abnormal", 40), ("snmpabnormal", 41), ("ackabnormal", 42), ("cc", 43), ("otherabnormal", 1024)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDDosAttackType.setStatus('current')
h3cDDosAttackPolicy = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDDosAttackPolicy.setStatus('current')
h3cDDosAttackThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDDosAttackThreshold.setStatus('current')
h3cDDosAttackSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cDDosAttackSpeed.setStatus('current')
h3cAFCNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2))
h3cAFCNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0))
h3cDDosAttackStart = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0, 1)).setObjects(("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackTargetIP"), ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackType"), ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackPolicy"), ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackThreshold"), ("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackSpeed"))
if mibBuilder.loadTexts: h3cDDosAttackStart.setStatus('current')
h3cDDosAttackEnd = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 85, 2, 0, 2)).setObjects(("A3COM-HUAWEI-AFC-MIB", "h3cDDosAttackTargetIP"))
if mibBuilder.loadTexts: h3cDDosAttackEnd.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-AFC-MIB", h3cDDosAttackType=h3cDDosAttackType, h3cDDosAttackPolicy=h3cDDosAttackPolicy, h3cDDosAttackThreshold=h3cDDosAttackThreshold, h3cDDosAttackSpeed=h3cDDosAttackSpeed, h3cAFC=h3cAFC, h3cDDosAttackStart=h3cDDosAttackStart, h3cAFCLeaf=h3cAFCLeaf, h3cDDosAttackTargetIP=h3cDDosAttackTargetIP, h3cAFCNotify=h3cAFCNotify, h3cDDosAttackEnd=h3cDDosAttackEnd, h3cAFCNotifyPrefix=h3cAFCNotifyPrefix, PYSNMP_MODULE_ID=h3cAFC)
