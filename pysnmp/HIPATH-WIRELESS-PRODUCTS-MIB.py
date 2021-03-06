#
# PySNMP MIB module HIPATH-WIRELESS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HIPATH-WIRELESS-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:18:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hiPathWirelessModules, hiPathWirelessProducts = mibBuilder.importSymbols("HIPATH-WIRELESS-SMI", "hiPathWirelessModules", "hiPathWirelessProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, Counter32, Counter64, IpAddress, Bits, TimeTicks, Integer32, iso, NotificationType, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Counter32", "Counter64", "IpAddress", "Bits", "TimeTicks", "Integer32", "iso", "NotificationType", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hiPathWirelessProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 5, 1))
hiPathWirelessProductsMIB.setRevisions(('2016-08-05 15:56', '2016-07-19 22:21', '2016-02-23 18:26', '2015-09-21 12:02', '2015-08-13 11:02', '2014-11-06 16:54', '2014-10-28 16:00', '2014-06-30 15:55', '2014-04-03 15:53', '2013-11-12 15:53', '2013-11-06 14:45', '2013-03-06 15:53', '2012-08-20 15:53', '2012-06-19 11:06', '2012-02-13 15:33', '2011-07-14 13:45', '2011-04-25 14:20', '2011-01-13 11:10', '2010-04-29 17:44', '2009-01-20 15:43', '2008-11-19 10:21', '2007-08-07 13:57', '2006-09-11 18:03', '2005-07-21 14:50',))
if mibBuilder.loadTexts: hiPathWirelessProductsMIB.setLastUpdated('201608051556Z')
if mibBuilder.loadTexts: hiPathWirelessProductsMIB.setOrganization('Chantry Networks Inc.')
control = MibIdentifier((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1))
c10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 1))
if mibBuilder.loadTexts: c10.setStatus('current')
c100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 2))
if mibBuilder.loadTexts: c100.setStatus('current')
c1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 3))
if mibBuilder.loadTexts: c1000.setStatus('current')
hiPathWirelessManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 4))
if mibBuilder.loadTexts: hiPathWirelessManager.setStatus('current')
c2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 5))
if mibBuilder.loadTexts: c2000.setStatus('current')
c20 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 6))
if mibBuilder.loadTexts: c20.setStatus('current')
c20N = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 7))
if mibBuilder.loadTexts: c20N.setStatus('current')
crbt8110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 8))
if mibBuilder.loadTexts: crbt8110.setStatus('current')
crbt8210 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 9))
if mibBuilder.loadTexts: crbt8210.setStatus('current')
c5110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 10))
if mibBuilder.loadTexts: c5110.setStatus('current')
c4110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 11))
if mibBuilder.loadTexts: c4110.setStatus('current')
c25 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 12))
if mibBuilder.loadTexts: c25.setStatus('current')
v2110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 13))
if mibBuilder.loadTexts: v2110.setStatus('current')
c5210 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 14))
if mibBuilder.loadTexts: c5210.setStatus('current')
v2110H = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 15))
if mibBuilder.loadTexts: v2110H.setStatus('current')
c35 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 17))
if mibBuilder.loadTexts: c35.setStatus('current')
access = MibIdentifier((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2))
ap26xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 2))
if mibBuilder.loadTexts: ap26xx.setStatus('current')
ap2600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 3))
if mibBuilder.loadTexts: ap2600.setStatus('current')
ap2650 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 4))
if mibBuilder.loadTexts: ap2650.setStatus('current')
apW786 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 5))
if mibBuilder.loadTexts: apW786.setStatus('current')
apW788 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 6))
if mibBuilder.loadTexts: apW788.setStatus('current')
ap3610 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 7))
if mibBuilder.loadTexts: ap3610.setStatus('current')
ap2605 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 8))
if mibBuilder.loadTexts: ap2605.setStatus('current')
ap3630 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 9))
if mibBuilder.loadTexts: ap3630.setStatus('current')
ap3640 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 10))
if mibBuilder.loadTexts: ap3640.setStatus('current')
ap2650Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 11))
if mibBuilder.loadTexts: ap2650Rev1.setStatus('current')
apW786Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 12))
if mibBuilder.loadTexts: apW786Rev1.setStatus('current')
ap4102 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 13))
if mibBuilder.loadTexts: ap4102.setStatus('current')
ap4102c = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 14))
if mibBuilder.loadTexts: ap4102c.setStatus('current')
ap4102RevEU = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 15))
if mibBuilder.loadTexts: ap4102RevEU.setStatus('current')
ap4102cRevEU = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 16))
if mibBuilder.loadTexts: ap4102cRevEU.setStatus('current')
ap2600Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 17))
if mibBuilder.loadTexts: ap2600Rev1.setStatus('current')
ap3600Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 18))
if mibBuilder.loadTexts: ap3600Rev1.setStatus('current')
ap2650Rev2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 19))
if mibBuilder.loadTexts: ap2650Rev2.setStatus('current')
apW786Rev2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 20))
if mibBuilder.loadTexts: apW786Rev2.setStatus('current')
ap3600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 21))
if mibBuilder.loadTexts: ap3600.setStatus('current')
ap3605 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 22))
if mibBuilder.loadTexts: ap3605.setStatus('current')
ap3660 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 23))
if mibBuilder.loadTexts: ap3660.setStatus('current')
ap2660Rev2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 24))
if mibBuilder.loadTexts: ap2660Rev2.setStatus('current')
apW786Rev2PROe2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 25))
if mibBuilder.loadTexts: apW786Rev2PROe2.setStatus('current')
apW786Rev2PROeFO2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 26))
if mibBuilder.loadTexts: apW786Rev2PROeFO2.setStatus('current')
apW786Rev2PROiFO2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 27))
if mibBuilder.loadTexts: apW786Rev2PROiFO2.setStatus('current')
ap3630NAMInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 28))
if mibBuilder.loadTexts: ap3630NAMInternal.setStatus('current')
ap3640NAMExternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 29))
if mibBuilder.loadTexts: ap3640NAMExternal.setStatus('current')
ap3630ROWInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 30))
if mibBuilder.loadTexts: ap3630ROWInternal.setStatus('current')
ap3640ROWExternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 31))
if mibBuilder.loadTexts: ap3640ROWExternal.setStatus('current')
ap3630ILInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 32))
if mibBuilder.loadTexts: ap3630ILInternal.setStatus('current')
ap3640ILExternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 33))
if mibBuilder.loadTexts: ap3640ILExternal.setStatus('current')
apW786C2RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 34))
if mibBuilder.loadTexts: apW786C2RJ45.setStatus('current')
apW786C2IARJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 35))
if mibBuilder.loadTexts: apW786C2IARJ45.setStatus('current')
apW788C2RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 36))
if mibBuilder.loadTexts: apW788C2RJ45.setStatus('current')
apW788C2M12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 37))
if mibBuilder.loadTexts: apW788C2M12.setStatus('current')
ap3705 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 38))
if mibBuilder.loadTexts: ap3705.setStatus('obsolete')
ap3765i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 39))
if mibBuilder.loadTexts: ap3765i.setStatus('current')
ap3660Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 40))
if mibBuilder.loadTexts: ap3660Rev1.setStatus('current')
ap3765e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 41))
if mibBuilder.loadTexts: ap3765e.setStatus('current')
ap3767e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 42))
if mibBuilder.loadTexts: ap3767e.setStatus('current')
ap3705i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 43))
if mibBuilder.loadTexts: ap3705i.setStatus('current')
ap3710i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 44))
if mibBuilder.loadTexts: ap3710i.setStatus('current')
ap3710e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 45))
if mibBuilder.loadTexts: ap3710e.setStatus('current')
ap3725i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 46))
if mibBuilder.loadTexts: ap3725i.setStatus('current')
ap3725e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 47))
if mibBuilder.loadTexts: ap3725e.setStatus('current')
ap3715i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 48))
if mibBuilder.loadTexts: ap3715i.setStatus('current')
ap3715e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 49))
if mibBuilder.loadTexts: ap3715e.setStatus('current')
ap3630ROW1i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 50))
if mibBuilder.loadTexts: ap3630ROW1i.setStatus('current')
ap3640ROW1e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 51))
if mibBuilder.loadTexts: ap3640ROW1e.setStatus('current')
ap3715i_1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 52)).setLabel("ap3715i-1")
if mibBuilder.loadTexts: ap3715i_1.setStatus('current')
ap3825i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 53))
if mibBuilder.loadTexts: ap3825i.setStatus('current')
ap3825e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 54))
if mibBuilder.loadTexts: ap3825e.setStatus('current')
ap3865e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 55))
if mibBuilder.loadTexts: ap3865e.setStatus('current')
ap3805i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 56))
if mibBuilder.loadTexts: ap3805i.setStatus('current')
ap3805e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 57))
if mibBuilder.loadTexts: ap3805e.setStatus('current')
ap3801i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 58))
if mibBuilder.loadTexts: ap3801i.setStatus('current')
ap3935FCCe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 59))
if mibBuilder.loadTexts: ap3935FCCe.setStatus('current')
ap3965FCCe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 60))
if mibBuilder.loadTexts: ap3965FCCe.setStatus('current')
ap3935ROWe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 61))
if mibBuilder.loadTexts: ap3935ROWe.setStatus('current')
ap3965ROWe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 62))
if mibBuilder.loadTexts: ap3965ROWe.setStatus('current')
ap3935FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 63))
if mibBuilder.loadTexts: ap3935FCCi.setStatus('current')
ap3965FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 64))
if mibBuilder.loadTexts: ap3965FCCi.setStatus('current')
ap3935ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 65))
if mibBuilder.loadTexts: ap3935ROWi.setStatus('current')
ap3965ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 66))
if mibBuilder.loadTexts: ap3965ROWi.setStatus('current')
apW786C2SFP = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 67))
if mibBuilder.loadTexts: apW786C2SFP.setStatus('current')
ap3805FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 68))
if mibBuilder.loadTexts: ap3805FCCi.setStatus('current')
ap3805FCCe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 69))
if mibBuilder.loadTexts: ap3805FCCe.setStatus('current')
ap3805ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 70))
if mibBuilder.loadTexts: ap3805ROWi.setStatus('current')
ap3805ROWe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 71))
if mibBuilder.loadTexts: ap3805ROWe.setStatus('current')
ap3825i_1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 72)).setLabel("ap3825i-1")
if mibBuilder.loadTexts: ap3825i_1.setStatus('current')
ap3825e_1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 73)).setLabel("ap3825e-1")
if mibBuilder.loadTexts: ap3825e_1.setStatus('current')
apVMAPFCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 74))
if mibBuilder.loadTexts: apVMAPFCCi.setStatus('current')
apVMAPROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 75))
if mibBuilder.loadTexts: apVMAPROWi.setStatus('current')
ap3935i_IL = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 76)).setLabel("ap3935i-IL")
if mibBuilder.loadTexts: ap3935i_IL.setStatus('current')
ap3912FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 77))
if mibBuilder.loadTexts: ap3912FCCi.setStatus('current')
ap3912ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 78))
if mibBuilder.loadTexts: ap3912ROWi.setStatus('current')
mibBuilder.exportSymbols("HIPATH-WIRELESS-PRODUCTS-MIB", ap3965ROWe=ap3965ROWe, ap3725e=ap3725e, ap26xx=ap26xx, apW788C2RJ45=apW788C2RJ45, ap3825e_1=ap3825e_1, ap3805e=ap3805e, ap3935FCCi=ap3935FCCi, ap3825e=ap3825e, apW788C2M12=apW788C2M12, ap3965FCCi=ap3965FCCi, ap4102cRevEU=ap4102cRevEU, ap3640ROWExternal=ap3640ROWExternal, ap3805ROWi=ap3805ROWi, ap3935i_IL=ap3935i_IL, apW788=apW788, ap3640=ap3640, apW786Rev2PROiFO2=apW786Rev2PROiFO2, ap3805ROWe=ap3805ROWe, ap3965FCCe=ap3965FCCe, apW786Rev2=apW786Rev2, ap2660Rev2=ap2660Rev2, ap2650Rev2=ap2650Rev2, apW786Rev1=apW786Rev1, ap3630ROWInternal=ap3630ROWInternal, ap3630=ap3630, ap3705i=ap3705i, ap3715i=ap3715i, ap3715i_1=ap3715i_1, c4110=c4110, apW786C2SFP=apW786C2SFP, ap3865e=ap3865e, ap3640ILExternal=ap3640ILExternal, ap3710e=ap3710e, apW786Rev2PROe2=apW786Rev2PROe2, apVMAPROWi=apVMAPROWi, apW786=apW786, c35=c35, ap4102RevEU=ap4102RevEU, v2110H=v2110H, ap3765i=ap3765i, ap3715e=ap3715e, ap2600=ap2600, ap3710i=ap3710i, c1000=c1000, apW786Rev2PROeFO2=apW786Rev2PROeFO2, ap2650=ap2650, apW786C2IARJ45=apW786C2IARJ45, ap3935ROWi=ap3935ROWi, ap3912ROWi=ap3912ROWi, apW786C2RJ45=apW786C2RJ45, PYSNMP_MODULE_ID=hiPathWirelessProductsMIB, ap4102c=ap4102c, apVMAPFCCi=apVMAPFCCi, ap3825i_1=ap3825i_1, ap3660=ap3660, c25=c25, ap3805FCCe=ap3805FCCe, ap3935FCCe=ap3935FCCe, ap3605=ap3605, ap3767e=ap3767e, ap3805FCCi=ap3805FCCi, ap2605=ap2605, ap2600Rev1=ap2600Rev1, c20N=c20N, ap3600Rev1=ap3600Rev1, access=access, ap3765e=ap3765e, c5210=c5210, ap3705=ap3705, ap3965ROWi=ap3965ROWi, ap3610=ap3610, ap4102=ap4102, hiPathWirelessManager=hiPathWirelessManager, v2110=v2110, crbt8110=crbt8110, ap3630ILInternal=ap3630ILInternal, ap3640ROW1e=ap3640ROW1e, ap3935ROWe=ap3935ROWe, c2000=c2000, ap3912FCCi=ap3912FCCi, crbt8210=crbt8210, ap2650Rev1=ap2650Rev1, ap3805i=ap3805i, c100=c100, c20=c20, ap3600=ap3600, ap3640NAMExternal=ap3640NAMExternal, c5110=c5110, ap3725i=ap3725i, hiPathWirelessProductsMIB=hiPathWirelessProductsMIB, ap3630ROW1i=ap3630ROW1i, ap3825i=ap3825i, control=control, c10=c10, ap3660Rev1=ap3660Rev1, ap3801i=ap3801i, ap3630NAMInternal=ap3630NAMInternal)
