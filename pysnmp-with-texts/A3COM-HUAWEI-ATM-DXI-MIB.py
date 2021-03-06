#
# PySNMP MIB module A3COM-HUAWEI-ATM-DXI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-ATM-DXI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:03:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, NotificationType, ObjectIdentity, Gauge32, Unsigned32, IpAddress, Bits, Counter32, MibIdentifier, Counter64, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ObjectIdentity", "Gauge32", "Unsigned32", "IpAddress", "Bits", "Counter32", "MibIdentifier", "Counter64", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
h3cAtmDxi = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49))
h3cAtmDxi.setRevisions(('2005-04-14 15:18',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cAtmDxi.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cAtmDxi.setLastUpdated('200504141518Z')
if mibBuilder.loadTexts: h3cAtmDxi.setOrganization('Huawei-3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cAtmDxi.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cAtmDxi.setDescription('This MIB contains objects to manage configuration of ATM-DXI. There are no constraints on this MIB.')
h3cAtmDxiScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 1))
h3cAtmDxiConfMode = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAtmDxiConfMode.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiConfMode.setDescription('This node identifies the ATM-DXI mode being used at the ATM-DXI port.')
h3cAtmDxiIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2))
h3cAtmDxiPvcTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1), )
if mibBuilder.loadTexts: h3cAtmDxiPvcTable.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcTable.setDescription('This table describes information of PVC in ATM-DXI interface.')
h3cAtmDxiPvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiPvcVpi"), (0, "A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiPvcVci"))
if mibBuilder.loadTexts: h3cAtmDxiPvcEntry.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcEntry.setDescription('The entry of h3cAtmDxiPvcTable.')
h3cAtmDxiPvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: h3cAtmDxiPvcVpi.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcVpi.setDescription("The value of VPI. It can't be 0 if h3cAtmDxiPvcVci is 0.")
h3cAtmDxiPvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: h3cAtmDxiPvcVci.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcVci.setDescription("The value of VCI. It can't be 0 if h3cAtmDxiPvcVpi is 0.")
h3cAtmDxiPvcDFA = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAtmDxiPvcDFA.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcDFA.setDescription('The index of PVC. It is equal with vci and VPI. And this node value is correlate with h3cAtmDxiPvcVpi and h3cAtmDxiPvcVci. ')
h3cAtmDxiPvcEncType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("snap", 1), ("nlpid", 2), ("mux", 3))).clone('snap')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAtmDxiPvcEncType.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcEncType.setDescription('Encapsulation type of the frame.')
h3cAtmDxiPvcMapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAtmDxiPvcMapCount.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcMapCount.setDescription('The number of map. One map can only associate with one PVC, but one PVC can associate with 32 maps. This node is the map count which one PVC associated with.')
h3cAtmDxiPvcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAtmDxiPvcRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiPvcRowStatus.setDescription("Only support 'destroy' 'createAndGo' and 'active'.")
h3cAtmDxiMapTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2), )
if mibBuilder.loadTexts: h3cAtmDxiMapTable.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapTable.setDescription('This table describes PVC map information.')
h3cAtmDxiMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapPeerIpType"), (0, "A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapPeerIp"), (0, "A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapPvcVpi"), (0, "A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapPvcVci"), (0, "A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapType"))
if mibBuilder.loadTexts: h3cAtmDxiMapEntry.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapEntry.setDescription('The entry of h3cAtmDxiMapTable.')
h3cAtmDxiMapPeerIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: h3cAtmDxiMapPeerIpType.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapPeerIpType.setDescription('The type of ip address: IPv4 or IPv6.')
h3cAtmDxiMapPeerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: h3cAtmDxiMapPeerIp.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapPeerIp.setDescription('The peer ip address. This ip address is the peer ip address which the frame will arrive.')
h3cAtmDxiMapPvcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: h3cAtmDxiMapPvcVpi.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapPvcVpi.setDescription("The VPI of PVC. It can't be 0 if h3cAtmDxiMapPvcVci is 0.")
h3cAtmDxiMapPvcVci = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: h3cAtmDxiMapPvcVci.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapPvcVci.setDescription("The VCI of PVC. It can't be 0 if h3cAtmDxiMapPvcVpi is 0.")
h3cAtmDxiMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("address", 1), ("inarp", 2), ("default", 3))))
if mibBuilder.loadTexts: h3cAtmDxiMapType.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapType.setDescription('Pvc map type.')
h3cAtmDxiMapInarpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 10), )).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAtmDxiMapInarpTime.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapInarpTime.setDescription("The interval time of inarp request. This node describes the interval time inarp request frame sent. If the h3cAtmDxiMapType isn't inarp, this value is 0. Its unit is minute.")
h3cAtmDxiMapBroEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAtmDxiMapBroEnable.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapBroEnable.setDescription('Whether ATM-DXI map enable broadcast or not.')
h3cAtmDxiMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 2, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cAtmDxiMapRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiMapRowStatus.setDescription("Only support 'destroy', 'createAndGo' and 'active'.")
h3cAtmDxiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 3))
h3cAtmDxiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 3, 1))
h3cAtmDxiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 3, 1, 1)).setObjects(("A3COM-HUAWEI-ATM-DXI-MIB", "h3cPVCMAPGroup"), ("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cAtmDxiCompliance = h3cAtmDxiCompliance.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiCompliance.setDescription('The compliance statement.')
h3cAtmDxiGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 3, 2))
h3cPVCMAPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 3, 2, 1)).setObjects(("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiPvcDFA"), ("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiPvcEncType"), ("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiPvcMapCount"), ("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiPvcRowStatus"), ("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapBroEnable"), ("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapInarpTime"), ("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiMapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cPVCMAPGroup = h3cPVCMAPGroup.setStatus('current')
if mibBuilder.loadTexts: h3cPVCMAPGroup.setDescription('This group includes nodes which are associated with interface.')
h3cAtmDxiGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 49, 3, 2, 2)).setObjects(("A3COM-HUAWEI-ATM-DXI-MIB", "h3cAtmDxiConfMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cAtmDxiGeneralGroup = h3cAtmDxiGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: h3cAtmDxiGeneralGroup.setDescription('This group includes the general nodes about ATM-DXI.')
mibBuilder.exportSymbols("A3COM-HUAWEI-ATM-DXI-MIB", h3cAtmDxiPvcRowStatus=h3cAtmDxiPvcRowStatus, h3cAtmDxiPvcEntry=h3cAtmDxiPvcEntry, h3cAtmDxiPvcTable=h3cAtmDxiPvcTable, h3cAtmDxiMapPeerIpType=h3cAtmDxiMapPeerIpType, h3cAtmDxiScalarGroup=h3cAtmDxiScalarGroup, h3cAtmDxiPvcDFA=h3cAtmDxiPvcDFA, h3cAtmDxiMapTable=h3cAtmDxiMapTable, h3cAtmDxiMapEntry=h3cAtmDxiMapEntry, h3cAtmDxiGroup=h3cAtmDxiGroup, h3cAtmDxiMapPeerIp=h3cAtmDxiMapPeerIp, h3cAtmDxiPvcEncType=h3cAtmDxiPvcEncType, h3cAtmDxiMapBroEnable=h3cAtmDxiMapBroEnable, h3cAtmDxiPvcVci=h3cAtmDxiPvcVci, h3cAtmDxiCompliances=h3cAtmDxiCompliances, h3cAtmDxiMapPvcVci=h3cAtmDxiMapPvcVci, h3cPVCMAPGroup=h3cPVCMAPGroup, h3cAtmDxiIfObjects=h3cAtmDxiIfObjects, h3cAtmDxiGeneralGroup=h3cAtmDxiGeneralGroup, h3cAtmDxiCompliance=h3cAtmDxiCompliance, h3cAtmDxiConformance=h3cAtmDxiConformance, h3cAtmDxiMapPvcVpi=h3cAtmDxiMapPvcVpi, h3cAtmDxiMapRowStatus=h3cAtmDxiMapRowStatus, h3cAtmDxiMapType=h3cAtmDxiMapType, PYSNMP_MODULE_ID=h3cAtmDxi, h3cAtmDxiPvcVpi=h3cAtmDxiPvcVpi, h3cAtmDxiPvcMapCount=h3cAtmDxiPvcMapCount, h3cAtmDxi=h3cAtmDxi, h3cAtmDxiMapInarpTime=h3cAtmDxiMapInarpTime, h3cAtmDxiConfMode=h3cAtmDxiConfMode)
