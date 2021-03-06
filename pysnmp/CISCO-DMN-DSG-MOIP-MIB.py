#
# PySNMP MIB module CISCO-DMN-DSG-MOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-MOIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, IpAddress, ObjectIdentity, iso, NotificationType, Counter32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, TimeTicks, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "ObjectIdentity", "iso", "NotificationType", "Counter32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "TimeTicks", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGMOIP = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35))
ciscoDSGMOIP.setRevisions(('2012-03-20 11:00', '2010-08-24 07:30',))
if mibBuilder.loadTexts: ciscoDSGMOIP.setLastUpdated('201203201100Z')
if mibBuilder.loadTexts: ciscoDSGMOIP.setOrganization('Cisco Systems, Inc.')
moipIPOTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1))
moipIPOConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1), )
if mibBuilder.loadTexts: moipIPOConfigTable.setStatus('current')
moipIPOConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-MOIP-MIB", "moipIPOConfigID"))
if mibBuilder.loadTexts: moipIPOConfigEntry.setStatus('current')
moipIPOConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOConfigID.setStatus('current')
moipIPOConfigOutputEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("no", 1), ("yes", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigOutputEnabled.setStatus('current')
moipIPOConfigInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigInstanceName.setStatus('current')
moipIPOConfigTPProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("udp", 1), ("rtp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigTPProtocol.setStatus('current')
moipIPOConfigIPVer = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOConfigIPVer.setStatus('current')
moipIPOConfigDestIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigDestIPAddr.setStatus('current')
moipIPOConfigSAPMulticastIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigSAPMulticastIPAddr.setStatus('current')
moipIPOConfigDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigDestPort.setStatus('current')
moipIPOConfigSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigSrcPort.setStatus('current')
moipIPOConfigMinIPPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigMinIPPerSec.setStatus('current')
moipIPOConfigPCRAddition = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigPCRAddition.setStatus('current')
moipIPOConfigPCRStartNewPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigPCRStartNewPkt.setStatus('current')
moipIPOConfigSendSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("rfc2327", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigSendSAP.setStatus('current')
moipIPOConfigUseSAPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("userString", 1), ("sdtChName", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigUseSAPStr.setStatus('current')
moipIPOConfigMaxTransPktPerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigMaxTransPktPerIP.setStatus('current')
moipIPOConfigSAPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigSAPStr.setStatus('current')
moipIPOConfigInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("data1", 2), ("data2", 3), ("both", 4), ("redundancy", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigInterfaceMode.setStatus('current')
moipIPOConfigBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 206000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigBitRate.setStatus('current')
moipIPOConfigTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigTOS.setStatus('current')
moipIPOConfigTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigTTL.setStatus('current')
moipIPOConfigSAPDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOConfigSAPDestPort.setStatus('current')
moipIPOFECMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("oneD", 2), ("twoD", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOFECMode.setStatus('current')
moipIPOFECColDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOFECColDepth.setStatus('current')
moipIPOFECRowWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOFECRowWidth.setStatus('current')
moipIPOAnnexType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("annexA", 1), ("annexB", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOAnnexType.setStatus('current')
moipIPOFEC1UDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 65534))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOFEC1UDPPort.setStatus('current')
moipIPOFEC2UDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 65534))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moipIPOFEC2UDPPort.setStatus('current')
moipIPOStreamStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2), )
if mibBuilder.loadTexts: moipIPOStreamStatusTable.setStatus('current')
moipIPOStreamStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-MOIP-MIB", "moipIPOStreamStatusID"))
if mibBuilder.loadTexts: moipIPOStreamStatusEntry.setStatus('current')
moipIPOStreamStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStreamStatusID.setStatus('current')
moipIPOStreamStatusIntf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notInit", 1), ("stopped", 2), ("suspended", 3), ("muted", 4), ("active", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStreamStatusIntf1.setStatus('current')
moipIPOStreamStatusIntf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notInit", 1), ("stopped", 2), ("suspended", 3), ("muted", 4), ("active", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStreamStatusIntf2.setStatus('current')
moipIPOStreamStatusContentOvfl = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStreamStatusContentOvfl.setStatus('current')
moipIPOStreamStatusLinkOvfl = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStreamStatusLinkOvfl.setStatus('current')
moipIPOInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2))
moipIPOStatsHWGlobalError = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStatsHWGlobalError.setStatus('current')
moipIPOStatsStreamError = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStatsStreamError.setStatus('current')
moipIPOStatsBandwidthConf = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStatsBandwidthConf.setStatus('current')
moipIPOStatsBandwidthActIntf1 = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStatsBandwidthActIntf1.setStatus('current')
moipIPOStatsBandwidthActIntf2 = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moipIPOStatsBandwidthActIntf2.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-MOIP-MIB", PYSNMP_MODULE_ID=ciscoDSGMOIP, moipIPOStatsBandwidthActIntf2=moipIPOStatsBandwidthActIntf2, moipIPOStreamStatusLinkOvfl=moipIPOStreamStatusLinkOvfl, moipIPOConfigID=moipIPOConfigID, moipIPOConfigTPProtocol=moipIPOConfigTPProtocol, moipIPOConfigMaxTransPktPerIP=moipIPOConfigMaxTransPktPerIP, moipIPOConfigTTL=moipIPOConfigTTL, moipIPOStatsStreamError=moipIPOStatsStreamError, moipIPOConfigDestIPAddr=moipIPOConfigDestIPAddr, moipIPOStreamStatusIntf2=moipIPOStreamStatusIntf2, moipIPOConfigEntry=moipIPOConfigEntry, moipIPOConfigInstanceName=moipIPOConfigInstanceName, moipIPOFEC2UDPPort=moipIPOFEC2UDPPort, moipIPOTable=moipIPOTable, moipIPOAnnexType=moipIPOAnnexType, moipIPOConfigUseSAPStr=moipIPOConfigUseSAPStr, moipIPOFECColDepth=moipIPOFECColDepth, moipIPOStreamStatusContentOvfl=moipIPOStreamStatusContentOvfl, moipIPOConfigPCRStartNewPkt=moipIPOConfigPCRStartNewPkt, moipIPOFEC1UDPPort=moipIPOFEC1UDPPort, moipIPOStatsBandwidthActIntf1=moipIPOStatsBandwidthActIntf1, moipIPOConfigTable=moipIPOConfigTable, moipIPOConfigMinIPPerSec=moipIPOConfigMinIPPerSec, moipIPOConfigSrcPort=moipIPOConfigSrcPort, moipIPOStreamStatusEntry=moipIPOStreamStatusEntry, moipIPOStatsHWGlobalError=moipIPOStatsHWGlobalError, moipIPOConfigSAPStr=moipIPOConfigSAPStr, moipIPOConfigSAPDestPort=moipIPOConfigSAPDestPort, moipIPOStreamStatusIntf1=moipIPOStreamStatusIntf1, moipIPOConfigDestPort=moipIPOConfigDestPort, moipIPOInfo=moipIPOInfo, moipIPOFECMode=moipIPOFECMode, moipIPOConfigIPVer=moipIPOConfigIPVer, moipIPOStatsBandwidthConf=moipIPOStatsBandwidthConf, moipIPOConfigTOS=moipIPOConfigTOS, moipIPOConfigOutputEnabled=moipIPOConfigOutputEnabled, moipIPOStreamStatusID=moipIPOStreamStatusID, moipIPOConfigSendSAP=moipIPOConfigSendSAP, moipIPOConfigBitRate=moipIPOConfigBitRate, moipIPOConfigSAPMulticastIPAddr=moipIPOConfigSAPMulticastIPAddr, moipIPOConfigPCRAddition=moipIPOConfigPCRAddition, ciscoDSGMOIP=ciscoDSGMOIP, moipIPOFECRowWidth=moipIPOFECRowWidth, moipIPOConfigInterfaceMode=moipIPOConfigInterfaceMode, moipIPOStreamStatusTable=moipIPOStreamStatusTable)
