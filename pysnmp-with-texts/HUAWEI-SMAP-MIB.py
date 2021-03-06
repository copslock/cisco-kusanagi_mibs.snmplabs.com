#
# PySNMP MIB module HUAWEI-SMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SMAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, ObjectIdentity, MibIdentifier, Unsigned32, IpAddress, TimeTicks, Gauge32, iso, NotificationType, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "TimeTicks", "Gauge32", "iso", "NotificationType", "Bits", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hwSMAP = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14))
if mibBuilder.loadTexts: hwSMAP.setLastUpdated('200303201150Z')
if mibBuilder.loadTexts: hwSMAP.setOrganization(' HAUWEI MIB Standard community ')
if mibBuilder.loadTexts: hwSMAP.setContactInfo(' R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwSMAP.setDescription(' V1.00 The SMAP mib is for all datacomm product. ')
hwSmapMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1))
hwSmapTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1), )
if mibBuilder.loadTexts: hwSmapTable.setStatus('current')
if mibBuilder.loadTexts: hwSmapTable.setDescription(' The Port-Application Map table. ')
hwSmapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1), ).setIndexNames((0, "HUAWEI-SMAP-MIB", "hwSmapUserPort"), (0, "HUAWEI-SMAP-MIB", "hwSmapAcl"))
if mibBuilder.loadTexts: hwSmapEntry.setStatus('current')
if mibBuilder.loadTexts: hwSmapEntry.setDescription(' The Port-Application Map table struct. ')
hwSmapUserPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmapUserPort.setStatus('current')
if mibBuilder.loadTexts: hwSmapUserPort.setDescription(' The new port defined by user. This item is index.')
hwSmapAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2999), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSmapAcl.setStatus('current')
if mibBuilder.loadTexts: hwSmapAcl.setDescription(' The SMAP function is used for which data flow. 0 means thie item is used for all data flow. This item is index. ')
hwSmapAppSysPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmapAppSysPort.setStatus('current')
if mibBuilder.loadTexts: hwSmapAppSysPort.setDescription(' The application port defined by rfc. Now only support: ftp 21 smtp 25 http 80 rtsp 554 h323 1720 ')
hwSmapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSmapStatus.setStatus('current')
if mibBuilder.loadTexts: hwSmapStatus.setDescription(' Only support CreateAndGo and Destroy. ')
hwSmapMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 2))
hwSmapMibGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 2, 1))
hwSmapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 14, 2, 1, 1)).setObjects(("HUAWEI-SMAP-MIB", "hwSmapUserPort"), ("HUAWEI-SMAP-MIB", "hwSmapAcl"), ("HUAWEI-SMAP-MIB", "hwSmapAppSysPort"), ("HUAWEI-SMAP-MIB", "hwSmapStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSmapGroup = hwSmapGroup.setStatus('current')
if mibBuilder.loadTexts: hwSmapGroup.setDescription(' The SMAP table member. ')
mibBuilder.exportSymbols("HUAWEI-SMAP-MIB", hwSmapEntry=hwSmapEntry, hwSmapUserPort=hwSmapUserPort, hwSmapMibConformance=hwSmapMibConformance, hwSmapMibGroup=hwSmapMibGroup, hwSmapAppSysPort=hwSmapAppSysPort, hwSmapMibObjects=hwSmapMibObjects, PYSNMP_MODULE_ID=hwSMAP, hwSmapGroup=hwSmapGroup, hwSmapStatus=hwSmapStatus, hwSmapAcl=hwSmapAcl, hwSmapTable=hwSmapTable, hwSMAP=hwSMAP)
