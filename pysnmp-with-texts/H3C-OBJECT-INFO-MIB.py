#
# PySNMP MIB module H3C-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-OBJECT-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Unsigned32, Counter64, NotificationType, Bits, Integer32, ModuleIdentity, TimeTicks, iso, Gauge32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Unsigned32", "Counter64", "NotificationType", "Bits", "Integer32", "ModuleIdentity", "TimeTicks", "iso", "Gauge32", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55))
h3cObjectInfo.setRevisions(('2004-12-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cObjectInfo.setRevisionsDescriptions((' The initial revision of this MIB module. ',))
if mibBuilder.loadTexts: h3cObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: h3cObjectInfo.setOrganization(' Huawei 3Com Technologies Co., Ltd. ')
if mibBuilder.loadTexts: h3cObjectInfo.setContactInfo(' Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085 ')
if mibBuilder.loadTexts: h3cObjectInfo.setDescription(' This MIB is used to acquire information from the agent. Before a NMS takes some actions, it is not sure whether the agent supports it or not. This MIB is used to solve this problem. ')
h3cObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1))
h3cObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1), )
if mibBuilder.loadTexts: h3cObjectInfoTable.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoTable.setDescription(' MIB objects information query table. ')
h3cObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1), ).setIndexNames((0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoOID"), (0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoType"), (0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoTypeExtension"))
if mibBuilder.loadTexts: h3cObjectInfoEntry.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoEntry.setDescription(' The entry of h3cObjectInfoTable. ')
h3cObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: h3cObjectInfoOID.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoOID.setDescription(' The OID of the MIB object which is queried. If the user has no privilege accessing to the object referred by this OID, get operation on h3cObjectInfoValue will be failed. ')
h3cObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: h3cObjectInfoType.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoType.setDescription(" The object's properties type to be queried. The queried result will be returned by h3cObjectInfoValue. The format of the result will be different according to different h3cObjectInfoType. ")
h3cObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: h3cObjectInfoTypeExtension.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoTypeExtension.setDescription(" The object's property type extension to be queried. This object's value is relative to the value of h3cObjectInfoType. ")
h3cObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cObjectInfoValue.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoValue.setDescription(" Return property value of the queried object. Zero length string is the default value of this object which means no value is returned. If the request is invalid, then the result should be the default value. If the value of h3cObjectInfoType is accessType, the rules below should be followed. 1) The returned value must have prefix 'A', and followed by some nonnegative integers. The format is like 'A2'. 2) The nonnegative integers and the meaning of them are as follow: 0 means 'not-accessible'. 1 means 'notification'. 2 means 'read-only'. 3 means 'read-write'. 4 means 'read-create'. 5 means 'write-only'. 6 means 'accessible-for-notify'. 7 means 'error'. --the above values are defined by standard protocol 101 means 'not implemented'. -- The queried node is not implemented by agent. 102 means 'unknown error'. -- Query failed for unknown reason. If the value of h3cObjectInfoType is dataType, the rules below should be followed. 1) The returned value must have prefix 'T', and followed by string which has format like 2), such as 'T1', the character '1' means INTEGER. 2) The following data types are defined in standard protocol, the values in brackets will be returned to indicate these data types. INTEGER(1) Integer32(2) Unsigned32(4) Gauge(6) Counter(7) Counter32(8) Counter64(9) TimeTicks(10) OCTET STRING(11) OBJECT IDENTIFIER(12) IpAddress(13) NetworkAddress(14) Opaque(15) BITS(16) If the value of h3cObjectInfoType is dataRange, the rules below should be followed. 1) The returned value must have prefix 'R', and followed by string which has the format like 2) to 5), such as 'R[1,1]'. 2) If h3cObjectInfoValue returns Integer32, the format is as followed. Suppose A is a MIB object. If SYNTAX of A is 'Integer32{1|2|3|5|6|7}', the format is 'R[1,3],[5,7]'. If SYNTAX of A is 'Integer32{1|3}', the format is 'R[1,1],[3,3]'. If SYNTAX of A is 'Integer32', the format is 'R[]' which means the default value range of Integer32 between -2147483648 and 2147483647. 3) The process of Counter, Counter32, Counter64, Unsigned32, Gauge32, INTEGER is the same as that of Integer32. 4) If SYNTAX of A is other types such as OCTET STRING, then this object returns default value 'R[]'. 5) If SYNTAX of A is 'BITS{a(0),b(1)}', the format is 'R[0,0],[1,1]'. If the value of h3cObjectInfoType is dataLength, the rules below should be followed. 1) The returned value must have prefix 'L', and followed by string which has the format like 2) to 4), such as 'L[6,6]'. 2) If SYNTAX of A is 'OCTET STRING(SIZE (6|10..255))', the format is 'L[6,6],[10,255]'. If SYNTAX of A is 'OCTET STRING', the format is like 'L[]' which means the default length of OCTET STRING between 0 and 65535. 3) If SYNTAX of A is BITS, the format of it is the same as OCTET STIRNG. But its unit is in bit, not in byte. 4) If SYNTAX of A is other types such as INTEGER and IpAddress, this object returns 'L[]'. ")
h3cObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2))
h3cObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 1))
h3cObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 1, 1)).setObjects(("H3C-OBJECT-INFO-MIB", "h3cObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoMIBCompliance = h3cObjectInfoMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoMIBCompliance.setDescription(' The compliance statement for implementing ObjectInfo MIB. ')
h3cObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 2))
h3cObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 2, 1)).setObjects(("H3C-OBJECT-INFO-MIB", "h3cObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoTableGroup = h3cObjectInfoTableGroup.setStatus('current')
if mibBuilder.loadTexts: h3cObjectInfoTableGroup.setDescription(' The basic collection of h3cObjectInfo table objects. ')
mibBuilder.exportSymbols("H3C-OBJECT-INFO-MIB", h3cObjectInformation=h3cObjectInformation, h3cObjectInfoEntry=h3cObjectInfoEntry, h3cObjectInfoType=h3cObjectInfoType, h3cObjectInfoMIBConformance=h3cObjectInfoMIBConformance, h3cObjectInfoMIBCompliance=h3cObjectInfoMIBCompliance, h3cObjectInfoMIBGroups=h3cObjectInfoMIBGroups, h3cObjectInfoMIBCompliances=h3cObjectInfoMIBCompliances, h3cObjectInfoTypeExtension=h3cObjectInfoTypeExtension, h3cObjectInfo=h3cObjectInfo, PYSNMP_MODULE_ID=h3cObjectInfo, h3cObjectInfoValue=h3cObjectInfoValue, h3cObjectInfoTable=h3cObjectInfoTable, h3cObjectInfoOID=h3cObjectInfoOID, h3cObjectInfoTableGroup=h3cObjectInfoTableGroup)
