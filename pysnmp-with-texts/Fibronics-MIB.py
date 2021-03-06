#
# PySNMP MIB module Fibronics-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FIBRONICS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Unsigned32, Gauge32, TimeTicks, Counter32, iso, internet, Integer32, ModuleIdentity, NotificationType, IpAddress, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Unsigned32", "Gauge32", "TimeTicks", "Counter32", "iso", "internet", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MACAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class FddiTime(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PhivAddr(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

mgmt = MibIdentifier((1, 3, 6, 1, 2))
mib = MibIdentifier((1, 3, 6, 1, 2, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
fibronics = MibIdentifier((1, 3, 6, 1, 4, 1, 22))
fxrBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 61))
fxrMng = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 61, 1))
fxrSysId = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 12))).clone(namedValues=NamedValues(("fr9500", 8), ("fer2500", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrSysId.setStatus('mandatory')
if mibBuilder.loadTexts: fxrSysId.setDescription('Identification of an Fibronics device. The device type for each integer clarifies the sysObjectID in MIB - II.')
fxrAction = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("reset", 1), ("sendNetworkTab", 2), ("deleteNetworkTab", 3), ("sendRoutingTab", 4), ("deleteRoutinTab", 5), ("sendLanTab", 6), ("deleteLanTab", 7), ("deleteArpTab", 8), ("sendArpTab", 9), ("deleteRouteTab", 10), ("sendRouteTab", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrAction.setStatus('mandatory')
if mibBuilder.loadTexts: fxrAction.setDescription('This variable enables the operator to perform one of the specified actions on the tables maintained by the network device. Send actions require support of proprietery File exchange protocol.')
fxrFileName = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrFileName.setStatus('mandatory')
if mibBuilder.loadTexts: fxrFileName.setDescription('The name of the file used internally by Fibronics for transferring tables maintained by network devices, using a prorietary File exchange protocol.')
fxrDeviceParams = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 61, 2))
fxrBridgeType = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 31))).clone(namedValues=NamedValues(("fr9500", 8), ("fer2500", 31)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrBridgeType.setStatus('mandatory')
if mibBuilder.loadTexts: fxrBridgeType.setDescription('Identification of the Fibronics bridge type.')
fxrInactiveArpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrInactiveArpTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: fxrInactiveArpTimeOut.setDescription('This variable defines the maximum time period that can pass between ARP requests concerning an entry in the ARP table. After this time period, the entry is deleted from the table.')
fxrBridgeAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 61, 2, 3))
fxrErrorDesc = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrErrorDesc.setStatus('mandatory')
if mibBuilder.loadTexts: fxrErrorDesc.setDescription('A textual description of the enterprise-specific trap sent to the Network Management Station by the Fibronics managed device.')
fxrErrorSeverity = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 2, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrErrorSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: fxrErrorSeverity.setDescription('The severity type of the enterprise-specific trap sent to the Network Management Station by the Fibronics managed device.')
fxrBrgVersion = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrBrgVersion.setStatus('mandatory')
if mibBuilder.loadTexts: fxrBrgVersion.setDescription('The bridge version.')
fxrBrgFeatures = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrBrgFeatures.setStatus('mandatory')
if mibBuilder.loadTexts: fxrBrgFeatures.setDescription('A bit mask that defines the features supported by a particular configuration of this network element: __________________________________________ | Byte 1|Byte 2 |Byte 3 | ....|Byte 20 | |87654321| | 87654321| |________|_______________________________| Byte1 : bit1: TX Block mask bit2: Source Routing Encapulation bit3: SNA/SDLC bit4: Frame Relay bit5: SNMP bit6: LAN Manager bit7: High Performance Byte2 : bit1: DEC Router bit2: IPX Router ')
fxrMaskTab = MibTable((1, 3, 6, 1, 4, 1, 22, 61, 8), )
if mibBuilder.loadTexts: fxrMaskTab.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskTab.setDescription('Mask tables enable definition of routing restrictions and control of messages flow in the internetwork. Each entry in this table defines a mask statement consisting of up to three mask definitions and an action defined by fxrMaskOper. Different types of mask entries are supported, as defined by fxrMaskType.')
fxrMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22, 61, 8, 1), )
if mibBuilder.loadTexts: fxrMaskEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskEntry.setDescription('Defines the contents of each line in the mask table. Each line is composed of three mask definitions and the action to be taken. Each mask definition is composed of a Pattern, Active bit, Base, Offset and Condition.')
fxrMaskType = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("tx", 1), ("rx", 2), ("compress", 3), ("priority", 4), ("loadSharing", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrMaskType.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskType.setDescription('Defines the type of mask entry.')
fxrIfPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrIfPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: fxrIfPortNum.setDescription('Specifies the port number to which the mask is applied.')
fxrMaskNum = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskNum.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskNum.setDescription('The Mask entry number, defined by its line number in the mask table.')
fxrMaskDest = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unassigned-cond", 1), ("broadcast-msge", 2), ("multicast-msge", 3), ("all-msge", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskDest.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskDest.setDescription('Specifies the type of destination address carried by the frame to which the mask will be applied. Unassigned-condition deactivates the mask entry.')
fxrMaskPat1 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskPat1.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskPat1.setDescription('Describes the mask field which is either a 16 bit binary pattern, or four digit hexadecimal pattern.')
fxrMaskActiveBit1 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskActiveBit1.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskActiveBit1.setDescription('Specifies the positions of the wild card characters (*) in the fxrMaskPat1 field.')
fxrMaskFrom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mac", 1), ("llc", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskFrom1.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskFrom1.setDescription('Offset base of fxrMaskPat1 within the frame.')
fxrMaskOffset1 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskOffset1.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskOffset1.setDescription('Specifies the fxrMaskPat1 offset within the frame (in bytes) from the base defined in by fxrMaskForm1.The mask offset is an even decimal number in the range of 0 to 1518.')
fxrMaskCond1 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskCond1.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskCond1.setDescription('Specifies the logical condition of the mask pattern: true - Condition is valid if at the position specified by fxrMaskOffset1 the packet contains data that matches the content of fxrMaskPat1. false - Condition is valid if at the position specified by fxrMaskOffset1 the packet contains data that does not match the content of fxrMaskPat1.')
fxrMaskPat2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 10), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskPat2.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskPat2.setDescription('Describes the mask field which is either a 16 bit binary pattern, or four digit hexadecimal pattern.')
fxrMaskActiveBit2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 11), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskActiveBit2.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskActiveBit2.setDescription('Specifies the positions of the wild card characters (*) in the fxrMaskPat2 field.')
fxrMaskFrom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mac", 1), ("llc", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskFrom2.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskFrom2.setDescription('Offset base of fxrMaskPat2 within the frame.')
fxrMaskOffset2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskOffset2.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskOffset2.setDescription('Specifies the fxrMaskPat2 offset within the frame (in bytes) from the base defined in by fxrMaskForm2.The mask offset is an even decimal number in the range of 0 to 1518.')
fxrMaskCond2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskCond2.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskCond2.setDescription('Specifies the logical condition of the mask pattern: true - Condition is valid if at the position specified by fxrMaskOffset2 the packet contains data that matches the content of fxrMaskPat2. false - Condition is valid if at the position specified by fxrMaskOffset2 the packet contains data that does not match the content of fxrMaskPat2.')
fxrMaskPat3 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 15), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskPat3.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskPat3.setDescription('Describes the mask field which is either a 16 bit binary pattern, or four digit hexadecimal pattern.')
fxrMaskActiveBit3 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 16), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskActiveBit3.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskActiveBit3.setDescription('Specifies the positions of the wild card characters (*) in the fxrMaskPat3 field.')
fxrMaskFrom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mac", 1), ("llc", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskFrom3.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskFrom3.setDescription('Offset base of fxrMaskPat3 within the frame.')
fxrMaskOffset3 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskOffset3.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskOffset3.setDescription('Specifies the fxrMaskPat3 offset within the frame (in bytes) from the base defined in by fxrMaskForm3. The mask offset is an even decimal number in the range of 0 to 1518.')
fxrMaskCond3 = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskCond3.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskCond3.setDescription('Specifies the logical condition of the mask pattern: true - Condition is valid if at the position specified by fxrMaskOffset3 the packet contains data that matches the content of fxrMaskPat3 false - Condition is valid if at the position specified by fxrMaskOffset3 the packet contains data that does not match the content of fxrMaskPat3.')
fxrMaskCompFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mac", 1), ("llc", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskCompFrom.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskCompFrom.setDescription("This field is used only when the mask type is 'compress'. It specifies the offset base from which the offset specified by fxrMaskCompOffset is calculated")
fxrMaskCompOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskCompOffset.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskCompOffset.setDescription('This field is used for compression mask type only. It defines the truncation offset in bytes. The rage is 12 to 254 and it can assume only even values.')
fxrMaskOper = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 8, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("block", 1), ("forward", 2), ("route", 3), ("forward-route", 4), ("high-priority", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrMaskOper.setStatus('mandatory')
if mibBuilder.loadTexts: fxrMaskOper.setDescription('The type of action to be taken if the frame meets the conditions of the mask.')
fxrTR = MibIdentifier((1, 3, 6, 1, 4, 1, 22, 61, 13))
fxrTRIfTab = MibTable((1, 3, 6, 1, 4, 1, 22, 61, 13, 1), )
if mibBuilder.loadTexts: fxrTRIfTab.setStatus('mandatory')
if mibBuilder.loadTexts: fxrTRIfTab.setDescription('This table defines the configuration parameters for Token Ring support which are unique to Fibronics Token Ring bridges.')
fxrTRIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22, 61, 13, 1, 1), ).setIndexNames((0, "Fibronics-MIB", "fxrTRIfIndex"))
if mibBuilder.loadTexts: fxrTRIfEntry.setStatus('mandatory')
fxrTRIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 13, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fxrTRIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fxrTRIfIndex.setDescription('Index to the Token Ring Interface Table. The interface defined by a particular value of this index is the same interface as identified by the same value of ifIndex (MIBII).')
fxrTREarlyTokenRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 13, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrTREarlyTokenRelease.setStatus('mandatory')
if mibBuilder.loadTexts: fxrTREarlyTokenRelease.setDescription('This parameter controls the early token release. This paramenter is applicable only to 16 Mbps ring.')
fxrTRLocalAdminAddress = MibScalar((1, 3, 6, 1, 4, 1, 22, 61, 13, 1, 1, 3), MACAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrTRLocalAdminAddress.setStatus('mandatory')
if mibBuilder.loadTexts: fxrTRLocalAdminAddress.setDescription('A locally administered MAC Address of this interface.')
fxrTRLocalAdminAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22, 61, 13, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fxrTRLocalAdminAddressStatus.setStatus('mandatory')
if mibBuilder.loadTexts: fxrTRLocalAdminAddressStatus.setDescription('This parameter controls whether the bridge uses the locally administered MAC Address defined for this interface, when enable(1), or not , when disable(2).')
mibBuilder.exportSymbols("Fibronics-MIB", fxrMaskEntry=fxrMaskEntry, mib=mib, fxrTR=fxrTR, fxrDeviceParams=fxrDeviceParams, fxrBridgeType=fxrBridgeType, fxrTREarlyTokenRelease=fxrTREarlyTokenRelease, fxrFileName=fxrFileName, fxrMaskCond1=fxrMaskCond1, fxrMaskPat1=fxrMaskPat1, fxrIfPortNum=fxrIfPortNum, fxrMaskNum=fxrMaskNum, fxrTRIfTab=fxrTRIfTab, fxrTRLocalAdminAddress=fxrTRLocalAdminAddress, fxrTRLocalAdminAddressStatus=fxrTRLocalAdminAddressStatus, fxrAction=fxrAction, fxrMaskActiveBit2=fxrMaskActiveBit2, fxrBrgVersion=fxrBrgVersion, fxrErrorSeverity=fxrErrorSeverity, fxrBridge=fxrBridge, fxrMaskType=fxrMaskType, mgmt=mgmt, fxrBrgFeatures=fxrBrgFeatures, MACAddress=MACAddress, fxrMaskPat3=fxrMaskPat3, fxrSysId=fxrSysId, fxrMaskFrom1=fxrMaskFrom1, fxrInactiveArpTimeOut=fxrInactiveArpTimeOut, fxrMaskOffset1=fxrMaskOffset1, directory=directory, fxrMaskOffset3=fxrMaskOffset3, fxrTRIfEntry=fxrTRIfEntry, PhivAddr=PhivAddr, fxrErrorDesc=fxrErrorDesc, fxrMaskPat2=fxrMaskPat2, fxrMaskFrom2=fxrMaskFrom2, fxrTRIfIndex=fxrTRIfIndex, fxrMaskFrom3=fxrMaskFrom3, private=private, fxrBridgeAlarm=fxrBridgeAlarm, fxrMaskDest=fxrMaskDest, fxrMaskActiveBit3=fxrMaskActiveBit3, fxrMaskCompFrom=fxrMaskCompFrom, fxrMng=fxrMng, fxrMaskCond2=fxrMaskCond2, fxrMaskCond3=fxrMaskCond3, fxrMaskActiveBit1=fxrMaskActiveBit1, FddiTime=FddiTime, experimental=experimental, fxrMaskOffset2=fxrMaskOffset2, fxrMaskCompOffset=fxrMaskCompOffset, fibronics=fibronics, fxrMaskTab=fxrMaskTab, enterprises=enterprises, fxrMaskOper=fxrMaskOper)
