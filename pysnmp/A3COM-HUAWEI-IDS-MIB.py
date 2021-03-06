#
# PySNMP MIB module A3COM-HUAWEI-IDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-IDS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, TimeTicks, ObjectIdentity, iso, Integer32, ModuleIdentity, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "TimeTicks", "ObjectIdentity", "iso", "Integer32", "ModuleIdentity", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cIDSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1))
if mibBuilder.loadTexts: h3cIDSMib.setLastUpdated('200507141942Z')
if mibBuilder.loadTexts: h3cIDSMib.setOrganization('Huawei-3com Technologies Co., Ltd.')
h3cIds = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47))
h3cIDSTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1))
h3cIDSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1))
h3cIDSTrapIPFragmentQueueLen = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapIPFragmentQueueLen.setStatus('current')
h3cIDSTrapStatSessionTabLen = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapStatSessionTabLen.setStatus('current')
h3cIDSTrapIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapIPAddressType.setStatus('current')
h3cIDSTrapIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapIPAddress.setStatus('current')
h3cIDSTrapUserName = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapUserName.setStatus('current')
h3cIDSTrapLoginType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("telnet", 1), ("ssh", 2), ("web", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapLoginType.setStatus('current')
h3cIDSTrapUpgradeType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("programme", 1), ("crb", 2), ("vrb", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapUpgradeType.setStatus('current')
h3cIDSTrapCRLName = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapCRLName.setStatus('current')
h3cIDSTrapCertName = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapCertName.setStatus('current')
h3cIDSTrapDetectRuleID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 10), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapDetectRuleID.setStatus('current')
h3cIDSTrapEngineID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapEngineID.setStatus('current')
h3cIDSTrapFileName = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapFileName.setStatus('current')
h3cIDSTrapCfgLineInFile = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 13), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapCfgLineInFile.setStatus('current')
h3cIDSTrapReasonForError = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cIDSTrapReasonForError.setStatus('current')
h3cIDSTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2))
h3cIDSTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0))
h3cIDSTrapIPFragQueueFull = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 1)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPFragmentQueueLen"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapIPFragQueueFull.setStatus('current')
h3cIDSTrapStatSessTabFull = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 2)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapStatSessionTabLen"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapStatSessTabFull.setStatus('current')
h3cIDSTrapDetectRuleParseFail = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 3)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapDetectRuleID"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapEngineID"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapDetectRuleParseFail.setStatus('current')
h3cIDSTrapDBConnLost = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 4)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddressType"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddress"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapDBConnLost.setStatus('current')
h3cIDSTrapCRLNeedUpdate = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 5)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapCRLName"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapCRLNeedUpdate.setStatus('current')
h3cIDSTrapCertOverdue = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 6)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapCertName"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapCertOverdue.setStatus('current')
h3cIDSTrapTooManyLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 7)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapUserName"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddressType"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddress"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapLoginType"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapTooManyLoginFail.setStatus('current')
h3cIDSTrapUpgradeError = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 8)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapUpgradeType"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapUpgradeError.setStatus('current')
h3cIDSTrapFileAccessError = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 9)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapFileName"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapFileAccessError.setStatus('current')
h3cIDSTrapConsArithMemLow = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 10)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapConsArithMemLow.setStatus('current')
h3cIDSTrapSSRAMOperFail = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 11)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapSSRAMOperFail.setStatus('current')
h3cIDSTrapPacketProcessDisorder = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 12)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: h3cIDSTrapPacketProcessDisorder.setStatus('current')
h3cIDSTrapCfgFileFormatError = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 13)).setObjects(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapFileName"), ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapCfgLineInFile"))
if mibBuilder.loadTexts: h3cIDSTrapCfgFileFormatError.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-IDS-MIB", h3cIDSTrapReasonForError=h3cIDSTrapReasonForError, h3cIDSTrapIPAddressType=h3cIDSTrapIPAddressType, h3cIDSTrapFileAccessError=h3cIDSTrapFileAccessError, h3cIDSTrapUpgradeError=h3cIDSTrapUpgradeError, h3cIDSTrapPacketProcessDisorder=h3cIDSTrapPacketProcessDisorder, PYSNMP_MODULE_ID=h3cIDSMib, h3cIDSTrapIPAddress=h3cIDSTrapIPAddress, h3cIDSTrapUpgradeType=h3cIDSTrapUpgradeType, h3cIDSTrapIPFragQueueFull=h3cIDSTrapIPFragQueueFull, h3cIDSTrapCertName=h3cIDSTrapCertName, h3cIDSTrapLoginType=h3cIDSTrapLoginType, h3cIDSTrapCertOverdue=h3cIDSTrapCertOverdue, h3cIDSTrapCRLNeedUpdate=h3cIDSTrapCRLNeedUpdate, h3cIDSTrapGroup=h3cIDSTrapGroup, h3cIDSTrapDetectRuleID=h3cIDSTrapDetectRuleID, h3cIDSTrapPrefix=h3cIDSTrapPrefix, h3cIDSTrap=h3cIDSTrap, h3cIDSTrapConsArithMemLow=h3cIDSTrapConsArithMemLow, h3cIDSTrapIPFragmentQueueLen=h3cIDSTrapIPFragmentQueueLen, h3cIDSTrapTooManyLoginFail=h3cIDSTrapTooManyLoginFail, h3cIDSTrapCRLName=h3cIDSTrapCRLName, h3cIDSTrapCfgFileFormatError=h3cIDSTrapCfgFileFormatError, h3cIDSTrapDetectRuleParseFail=h3cIDSTrapDetectRuleParseFail, h3cIDSMib=h3cIDSMib, h3cIDSTrapStatSessTabFull=h3cIDSTrapStatSessTabFull, h3cIDSTrapCfgLineInFile=h3cIDSTrapCfgLineInFile, h3cIDSTrapFileName=h3cIDSTrapFileName, h3cIDSTrapDBConnLost=h3cIDSTrapDBConnLost, h3cIDSTrapEngineID=h3cIDSTrapEngineID, h3cIDSTrapSSRAMOperFail=h3cIDSTrapSSRAMOperFail, h3cIDSTrapStatSessionTabLen=h3cIDSTrapStatSessionTabLen, h3cIDSTrapUserName=h3cIDSTrapUserName, h3cIds=h3cIds, h3cIDSTrapInfo=h3cIDSTrapInfo)
