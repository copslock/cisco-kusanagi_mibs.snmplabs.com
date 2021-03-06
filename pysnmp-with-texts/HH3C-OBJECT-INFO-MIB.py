#
# PySNMP MIB module HH3C-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-OBJECT-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, TimeTicks, NotificationType, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, ModuleIdentity, Bits, Counter64, Unsigned32, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "NotificationType", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "ModuleIdentity", "Bits", "Counter64", "Unsigned32", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 55))
hh3cObjectInfo.setRevisions(('2004-12-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cObjectInfo.setRevisionsDescriptions((' The initial revision of this MIB module. ',))
if mibBuilder.loadTexts: hh3cObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: hh3cObjectInfo.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cObjectInfo.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cObjectInfo.setDescription(' This MIB is used to acquire information from the agent. Before a NMS takes some actions, it is not sure whether the agent supports it or not. This MIB is used to solve this problem. ')
hh3cObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1))
hh3cObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1), )
if mibBuilder.loadTexts: hh3cObjectInfoTable.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoTable.setDescription(' MIB objects information query table. ')
hh3cObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1), ).setIndexNames((0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoOID"), (0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoType"), (0, "HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoTypeExtension"))
if mibBuilder.loadTexts: hh3cObjectInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoEntry.setDescription(' The entry of hh3cObjectInfoTable. ')
hh3cObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: hh3cObjectInfoOID.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoOID.setDescription(' The OID of the MIB object which is queried. If the user has no privilege accessing to the object referred by this OID, get operation on hh3cObjectInfoValue will be failed. ')
hh3cObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: hh3cObjectInfoType.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoType.setDescription(" The object's properties type to be queried. The queried result will be returned by hh3cObjectInfoValue. The format of the result will be different according to different hh3cObjectInfoType. ")
hh3cObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hh3cObjectInfoTypeExtension.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoTypeExtension.setDescription(" The object's property type extension to be queried. This object's value is relative to the value of hh3cObjectInfoType. ")
hh3cObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cObjectInfoValue.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoValue.setDescription(" Return property value of the queried object. Zero length string is the default value of this object which means no value is returned. If the request is invalid, then the result should be the default value. If the value of hh3cObjectInfoType is accessType, the rules below should be followed. 1) The returned value must have prefix 'A', and followed by some nonnegative integers. The format is like 'A2'. 2) The nonnegative integers and the meaning of them are as follow: 0 means 'not-accessible'. 1 means 'notification'. 2 means 'read-only'. 3 means 'read-write'. 4 means 'read-create'. 5 means 'write-only'. 6 means 'accessible-for-notify'. 7 means 'error'. --the above values are defined by standard protocol 101 means 'not implemented'. -- The queried node is not implemented by agent. 102 means 'unknown error'. -- Query failed for unknown reason. If the value of hh3cObjectInfoType is dataType, the rules below should be followed. 1) The returned value must have prefix 'T', and followed by string which has format like 2), such as 'T1', the character '1' means INTEGER. 2) The following data types are defined in standard protocol, the values in brackets will be returned to indicate these data types. INTEGER(1) Integer32(2) Unsigned32(4) Gauge(6) Counter(7) Counter32(8) Counter64(9) TimeTicks(10) OCTET STRING(11) OBJECT IDENTIFIER(12) IpAddress(13) NetworkAddress(14) Opaque(15) BITS(16) If the value of hh3cObjectInfoType is dataRange, the rules below should be followed. 1) The returned value must have prefix 'R', and followed by string which has the format like 2) to 5), such as 'R[1,1]'. 2) If hh3cObjectInfoValue returns Integer32, the format is as followed. Suppose A is a MIB object. If SYNTAX of A is 'Integer32{1|2|3|5|6|7}', the format is 'R[1,3],[5,7]'. If SYNTAX of A is 'Integer32{1|3}', the format is 'R[1,1],[3,3]'. If SYNTAX of A is 'Integer32', the format is 'R[]' which means the default value range of Integer32 between -2147483648 and 2147483647. 3) The process of Counter, Counter32, Counter64, Unsigned32, Gauge32, INTEGER is the same as that of Integer32. 4) If SYNTAX of A is other types such as OCTET STRING, then this object returns default value 'R[]'. 5) If SYNTAX of A is 'BITS{a(0),b(1)}', the format is 'R[0,0],[1,1]'. If the value of hh3cObjectInfoType is dataLength, the rules below should be followed. 1) The returned value must have prefix 'L', and followed by string which has the format like 2) to 4), such as 'L[6,6]'. 2) If SYNTAX of A is 'OCTET STRING(SIZE (6|10..255))', the format is 'L[6,6],[10,255]'. If SYNTAX of A is 'OCTET STRING', the format is like 'L[]' which means the default length of OCTET STRING between 0 and 65535. 3) If SYNTAX of A is BITS, the format of it is the same as OCTET STIRNG. But its unit is in bit, not in byte. 4) If SYNTAX of A is other types such as INTEGER and IpAddress, this object returns 'L[]'. ")
hh3cObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2))
hh3cObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 1))
hh3cObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 1, 1)).setObjects(("HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cObjectInfoMIBCompliance = hh3cObjectInfoMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoMIBCompliance.setDescription(' The compliance statement for implementing ObjectInfo MIB. ')
hh3cObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 2))
hh3cObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 55, 2, 2, 1)).setObjects(("HH3C-OBJECT-INFO-MIB", "hh3cObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cObjectInfoTableGroup = hh3cObjectInfoTableGroup.setStatus('current')
if mibBuilder.loadTexts: hh3cObjectInfoTableGroup.setDescription(' The basic collection of hh3cObjectInfo table objects. ')
mibBuilder.exportSymbols("HH3C-OBJECT-INFO-MIB", hh3cObjectInfoTableGroup=hh3cObjectInfoTableGroup, hh3cObjectInfoMIBGroups=hh3cObjectInfoMIBGroups, hh3cObjectInfoType=hh3cObjectInfoType, hh3cObjectInfoValue=hh3cObjectInfoValue, hh3cObjectInfoMIBCompliances=hh3cObjectInfoMIBCompliances, PYSNMP_MODULE_ID=hh3cObjectInfo, hh3cObjectInfoTable=hh3cObjectInfoTable, hh3cObjectInfoOID=hh3cObjectInfoOID, hh3cObjectInfoMIBCompliance=hh3cObjectInfoMIBCompliance, hh3cObjectInfo=hh3cObjectInfo, hh3cObjectInfoEntry=hh3cObjectInfoEntry, hh3cObjectInfoTypeExtension=hh3cObjectInfoTypeExtension, hh3cObjectInformation=hh3cObjectInformation, hh3cObjectInfoMIBConformance=hh3cObjectInfoMIBConformance)
