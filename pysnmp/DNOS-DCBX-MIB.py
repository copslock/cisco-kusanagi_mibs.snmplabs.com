#
# PySNMP MIB module DNOS-DCBX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-DCBX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Unsigned32, Integer32, Counter64, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, NotificationType, ObjectIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Unsigned32", "Integer32", "Counter64", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32")
RowStatus, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TextualConvention")
fastPathDCBX = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58))
fastPathDCBX.setRevisions(('2011-04-20 00:00',))
if mibBuilder.loadTexts: fastPathDCBX.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathDCBX.setOrganization('Dell, Inc.')
class DcbxPortRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("manual", 1), ("autoup", 2), ("autodown", 3), ("configSource", 4))

class DcbxVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("ieee", 2), ("cin", 3), ("cee", 4))

agentDcbxGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1))
agentDcbxTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1), )
if mibBuilder.loadTexts: agentDcbxTable.setStatus('current')
agentDcbxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1), ).setIndexNames((0, "DNOS-DCBX-MIB", "agentDcbxIntfIndex"))
if mibBuilder.loadTexts: agentDcbxEntry.setStatus('current')
agentDcbxIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: agentDcbxIntfIndex.setStatus('current')
agentDcbxAutoCfgPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 2), DcbxPortRole().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDcbxAutoCfgPortRole.setStatus('current')
agentDcbxVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 3), DcbxVersion().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDcbxVersion.setStatus('deprecated')
agentDcbxSupportedTLVs = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 4), Bits().clone(namedValues=NamedValues(("pfc", 0), ("etsConfig", 1), ("etsRecom", 2), ("applicationPriority", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxSupportedTLVs.setStatus('current')
agentDcbxConfigTLVsTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 1, 1, 5), Bits().clone(namedValues=NamedValues(("pfc", 0), ("etsConfig", 1), ("etsRecom", 2), ("applicationPriority", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDcbxConfigTLVsTxEnable.setStatus('current')
agentDcbxStatusTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2), )
if mibBuilder.loadTexts: agentDcbxStatusTable.setStatus('current')
agentDcbxStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1), ).setIndexNames((0, "DNOS-DCBX-MIB", "agentDcbxIntfIndex"))
if mibBuilder.loadTexts: agentDcbxStatusEntry.setStatus('current')
agentDcbxOperVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 2), DcbxVersion().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxOperVersion.setStatus('current')
agentDcbxPeerMACaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxPeerMACaddress.setStatus('current')
agentDcbxCfgSource = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("true", 1), ("false", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxCfgSource.setStatus('current')
agentDcbxMultiplePeerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxMultiplePeerCount.setStatus('current')
agentDcbxPeerRemovedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxPeerRemovedCount.setStatus('current')
agentDcbxPeerOperVersionNum = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxPeerOperVersionNum.setStatus('current')
agentDcbxPeerMaxVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxPeerMaxVersion.setStatus('current')
agentDcbxSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxSeqNum.setStatus('current')
agentDcbxAckNum = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxAckNum.setStatus('current')
agentDcbxPeerRcvdAckNum = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxPeerRcvdAckNum.setStatus('current')
agentDcbxTxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxTxCount.setStatus('current')
agentDcbxRxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxRxCount.setStatus('current')
agentDcbxErrorFramesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxErrorFramesCount.setStatus('current')
agentDcbxUnknownTLVsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDcbxUnknownTLVsCount.setStatus('current')
agentDcbxGroupGlobalConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 3))
agentDcbxGlobalConfVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 58, 1, 3, 1), DcbxVersion().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDcbxGlobalConfVersion.setStatus('current')
mibBuilder.exportSymbols("DNOS-DCBX-MIB", DcbxVersion=DcbxVersion, agentDcbxAckNum=agentDcbxAckNum, agentDcbxSupportedTLVs=agentDcbxSupportedTLVs, agentDcbxUnknownTLVsCount=agentDcbxUnknownTLVsCount, agentDcbxStatusTable=agentDcbxStatusTable, agentDcbxPeerMaxVersion=agentDcbxPeerMaxVersion, agentDcbxRxCount=agentDcbxRxCount, agentDcbxPeerOperVersionNum=agentDcbxPeerOperVersionNum, agentDcbxAutoCfgPortRole=agentDcbxAutoCfgPortRole, PYSNMP_MODULE_ID=fastPathDCBX, agentDcbxSeqNum=agentDcbxSeqNum, agentDcbxPeerMACaddress=agentDcbxPeerMACaddress, DcbxPortRole=DcbxPortRole, agentDcbxOperVersion=agentDcbxOperVersion, agentDcbxConfigTLVsTxEnable=agentDcbxConfigTLVsTxEnable, agentDcbxStatusEntry=agentDcbxStatusEntry, agentDcbxErrorFramesCount=agentDcbxErrorFramesCount, agentDcbxIntfIndex=agentDcbxIntfIndex, fastPathDCBX=fastPathDCBX, agentDcbxVersion=agentDcbxVersion, agentDcbxPeerRcvdAckNum=agentDcbxPeerRcvdAckNum, agentDcbxPeerRemovedCount=agentDcbxPeerRemovedCount, agentDcbxGroup=agentDcbxGroup, agentDcbxGroupGlobalConfGroup=agentDcbxGroupGlobalConfGroup, agentDcbxMultiplePeerCount=agentDcbxMultiplePeerCount, agentDcbxGlobalConfVersion=agentDcbxGlobalConfVersion, agentDcbxEntry=agentDcbxEntry, agentDcbxTable=agentDcbxTable, agentDcbxCfgSource=agentDcbxCfgSource, agentDcbxTxCount=agentDcbxTxCount)