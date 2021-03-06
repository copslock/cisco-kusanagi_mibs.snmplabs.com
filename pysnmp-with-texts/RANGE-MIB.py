#
# PySNMP MIB module RANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RANGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:51:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, Gauge32, MibIdentifier, Integer32, Unsigned32, ModuleIdentity, NotificationType, TimeTicks, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "Gauge32", "MibIdentifier", "Integer32", "Unsigned32", "ModuleIdentity", "NotificationType", "TimeTicks", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rangeTestMIB = ModuleIdentity((1, 1, 1))
if mibBuilder.loadTexts: rangeTestMIB.setLastUpdated('9512090000Z')
if mibBuilder.loadTexts: rangeTestMIB.setOrganization('MIB Test Group')
if mibBuilder.loadTexts: rangeTestMIB.setContactInfo(' Test Dept MIB Test Group')
if mibBuilder.loadTexts: rangeTestMIB.setDescription('Range Test MIB')
rangeObj = MibIdentifier((1, 1, 2))
obj01 = MibScalar((1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj01.setStatus('current')
if mibBuilder.loadTexts: obj01.setDescription('description')
obj02 = MibScalar((1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj02.setStatus('current')
if mibBuilder.loadTexts: obj02.setDescription('description')
obj03 = MibScalar((1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2147483647, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj03.setStatus('current')
if mibBuilder.loadTexts: obj03.setDescription('description')
obj04 = MibScalar((1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, -1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj04.setStatus('current')
if mibBuilder.loadTexts: obj04.setDescription('description')
obj05 = MibScalar((1, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, -2147483648))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj05.setStatus('current')
if mibBuilder.loadTexts: obj05.setDescription('description')
obj06 = MibScalar((1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj06.setStatus('current')
if mibBuilder.loadTexts: obj06.setDescription('description')
obj07 = MibScalar((1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj07.setStatus('current')
if mibBuilder.loadTexts: obj07.setDescription('description')
obj08 = MibScalar((1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(10, 10), ValueRangeConstraint(0, 0), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj08.setStatus('current')
if mibBuilder.loadTexts: obj08.setDescription('description')
obj09 = MibScalar((1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 10), ValueRangeConstraint(2147483647, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj09.setStatus('current')
if mibBuilder.loadTexts: obj09.setDescription('description')
obj10 = MibScalar((1, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2147483647, 2147483647), ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj10.setStatus('current')
if mibBuilder.loadTexts: obj10.setDescription('description')
obj11 = MibScalar((1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(10, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj11.setStatus('current')
if mibBuilder.loadTexts: obj11.setDescription('description')
obj12 = MibScalar((1, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(10, 10), ValueRangeConstraint(-1, -1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj12.setStatus('current')
if mibBuilder.loadTexts: obj12.setDescription('description')
obj13 = MibScalar((1, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2147483648, -2147483648), ValueRangeConstraint(-1, -1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj13.setStatus('current')
if mibBuilder.loadTexts: obj13.setDescription('description')
obj14 = MibScalar((1, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj14.setStatus('current')
if mibBuilder.loadTexts: obj14.setDescription('description')
obj15 = MibScalar((1, 1, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2147483648, -2147483648), ValueRangeConstraint(-1, -1), ValueRangeConstraint(10, 10), ValueRangeConstraint(0, 0), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj15.setStatus('current')
if mibBuilder.loadTexts: obj15.setDescription('description')
obj21 = MibScalar((1, 1, 2, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj21.setStatus('current')
if mibBuilder.loadTexts: obj21.setDescription('description')
obj22 = MibScalar((1, 1, 2, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj22.setStatus('current')
if mibBuilder.loadTexts: obj22.setDescription('description')
obj23 = MibScalar((1, 1, 2, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj23.setStatus('current')
if mibBuilder.loadTexts: obj23.setDescription('description')
obj24 = MibScalar((1, 1, 2, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj24.setStatus('current')
if mibBuilder.loadTexts: obj24.setDescription('description')
obj25 = MibScalar((1, 1, 2, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, -1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj25.setStatus('current')
if mibBuilder.loadTexts: obj25.setDescription('description')
obj26 = MibScalar((1, 1, 2, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj26.setStatus('current')
if mibBuilder.loadTexts: obj26.setDescription('description')
obj27 = MibScalar((1, 1, 2, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-10, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj27.setStatus('current')
if mibBuilder.loadTexts: obj27.setDescription('description')
obj28 = MibScalar((1, 1, 2, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj28.setStatus('current')
if mibBuilder.loadTexts: obj28.setDescription('description')
obj31 = MibScalar((1, 1, 2, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj31.setStatus('current')
if mibBuilder.loadTexts: obj31.setDescription('description')
obj32 = MibScalar((1, 1, 2, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 10), ValueRangeConstraint(0, 0), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj32.setStatus('current')
if mibBuilder.loadTexts: obj32.setDescription('description')
obj33 = MibScalar((1, 1, 2, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2147483648, -1), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj33.setStatus('current')
if mibBuilder.loadTexts: obj33.setDescription('description')
obj34 = MibScalar((1, 1, 2, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 2147483647), ValueRangeConstraint(-2147483648, -1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj34.setStatus('current')
if mibBuilder.loadTexts: obj34.setDescription('description')
obj35 = MibScalar((1, 1, 2, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-100, -60), ValueRangeConstraint(-40, -5), ValueRangeConstraint(-1, 3), ValueRangeConstraint(5, 10), ValueRangeConstraint(100, 400), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj35.setStatus('current')
if mibBuilder.loadTexts: obj35.setDescription('description')
obj36 = MibScalar((1, 1, 2, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-200, -200), ValueRangeConstraint(200, 200), ValueRangeConstraint(-199, -199), ValueRangeConstraint(199, 199), ValueRangeConstraint(-198, -198), ValueRangeConstraint(198, 198), ValueRangeConstraint(-197, -197), ValueRangeConstraint(197, 197), ValueRangeConstraint(-196, -196), ValueRangeConstraint(196, 196), ValueRangeConstraint(-195, -195), ValueRangeConstraint(195, 195), ValueRangeConstraint(-194, -194), ValueRangeConstraint(194, 194), ValueRangeConstraint(-193, -193), ValueRangeConstraint(193, 193), ValueRangeConstraint(-192, -192), ValueRangeConstraint(192, 192), ValueRangeConstraint(-191, -191), ValueRangeConstraint(191, 191), ValueRangeConstraint(-190, -190), ValueRangeConstraint(190, 190), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj36.setStatus('current')
if mibBuilder.loadTexts: obj36.setDescription('description')
obj37 = MibScalar((1, 1, 2, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-200, -190), ValueRangeConstraint(190, 200), ValueRangeConstraint(-170, -160), ValueRangeConstraint(160, 170), ValueRangeConstraint(-150, -140), ValueRangeConstraint(140, 150), ValueRangeConstraint(-120, -100), ValueRangeConstraint(100, 120), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj37.setStatus('current')
if mibBuilder.loadTexts: obj37.setDescription('description')
mibBuilder.exportSymbols("RANGE-MIB", obj04=obj04, obj05=obj05, obj09=obj09, obj37=obj37, obj11=obj11, obj32=obj32, obj10=obj10, obj31=obj31, obj27=obj27, rangeTestMIB=rangeTestMIB, obj15=obj15, obj02=obj02, obj12=obj12, obj01=obj01, obj36=obj36, obj24=obj24, obj03=obj03, obj06=obj06, obj13=obj13, obj22=obj22, rangeObj=rangeObj, obj33=obj33, obj07=obj07, obj35=obj35, obj23=obj23, obj21=obj21, PYSNMP_MODULE_ID=rangeTestMIB, obj14=obj14, obj34=obj34, obj28=obj28, obj25=obj25, obj08=obj08, obj26=obj26)
