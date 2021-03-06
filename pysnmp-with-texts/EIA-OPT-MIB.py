#
# PySNMP MIB module EIA-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EIA-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Counter64, TimeTicks, Unsigned32, MibIdentifier, Bits, iso, Integer32, ModuleIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Counter64", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "iso", "Integer32", "ModuleIdentity", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatOtherStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class DisplayString(OctetString):
    pass

cdx6500StatEIATable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7), )
if mibBuilder.loadTexts: cdx6500StatEIATable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIATable.setDescription('This table contains EIA Summary Statistics of a port')
cdx6500StatEIAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1), ).setIndexNames((0, "EIA-OPT-MIB", "cdx6500StatEIAEntryPortNumber"))
if mibBuilder.loadTexts: cdx6500StatEIAEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIAEntry.setDescription('A list of objects for EIA Summary statistics.')
cdx6500StatEIAEntryPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatEIAEntryPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIAEntryPortNumber.setDescription('Port number of this port.')
cdx6500StatEIAEntryDimType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 50))).clone(namedValues=NamedValues(("dimTypeNone", 0), ("dimTypeNotInstalled", 1), ("dimTypeEia232d", 2), ("dimTypeX21", 3), ("dimTypeV35", 4), ("dimTypeV36", 5), ("dimTypeV11", 6), ("dimTypeEia530", 7), ("dimTypeDsu", 8), ("dimTypeI430", 10), ("newvalDimTypeNone", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatEIAEntryDimType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIAEntryDimType.setDescription("The DIM Type for the port. dimTypeNone : DIM type is none. dimTypeNotInstalled : DIM type is not installed. dimTypeEia232d : DIM type is EIA-232-D. dimTypeX21 : DIM type is X-21. dimTypeV35 : DIM type is V.35. dimTypeV36 : DIM type is V.36. dimTypeV11 : DIM type is V.11. dimTypeEia530 : DIM type is EIA-530. dimTypeDsu : DIM type is DSU. dimTypeI430 : DIM type is I 430. newvalDimTypeNone : same as 'dimTypeNone', new enumeration added for RFC1155 compatibility.")
cdx6500StatEIAEntryDimCfgn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("dimCfgnDte", 0), ("dimCfgnDce", 1), ("newvalDimCfgnDte", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatEIAEntryDimCfgn.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIAEntryDimCfgn.setDescription("The DIM Configuration for the port. dimCfgnDte : DIM Configuration is DTE. dimCfgnDce : DIM Configuration is DCE. newvalDimCfgnNone : same functionality as 'dimTypeNone', new enumeration added for RFC1155 compatibility.")
cdx6500StatEIAEntryEiaState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatEIAEntryEiaState.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIAEntryEiaState.setDescription('The EIA State for the port.')
cdx6500StatEIAEntryConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatEIAEntryConnType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIAEntryConnType.setDescription('The EIA Connection Type.')
cdx6500StatEIAEntrySignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 7, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatEIAEntrySignalStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatEIAEntrySignalStatus.setDescription('The Status of the EIA Signal levels for the port with that combination of DIMTYPE and DIMCFGN.')
isgVGIsdnEIAStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8), )
if mibBuilder.loadTexts: isgVGIsdnEIAStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatTable.setDescription('This table contains EIA Summary Statistics of a port.')
isgVGIsdnEIAStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1), ).setIndexNames((0, "EIA-OPT-MIB", "isgVGIsdnEIAStatPortNum"))
if mibBuilder.loadTexts: isgVGIsdnEIAStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatEntry.setDescription('A list of objects for ISDN EIA Summary statistics.')
isgVGIsdnEIAStatPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatPortNum.setDescription('Port number of this port.')
isgVGIsdnEIAStatDimType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(9))).clone(namedValues=NamedValues(("dimTypeIsdn", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatDimType.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatDimType.setDescription('The DIM Type for the port.')
isgVGIsdnEIAStatDimCfgn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 50))).clone(namedValues=NamedValues(("dimIsdnST", 0), ("dimIsdnU", 1), ("newvalDimIsdnST", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatDimCfgn.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatDimCfgn.setDescription("The DIM Configuration for the port. dimIsdnST : ISDN ST interface. dimIsdnU : ISDN U interface. newvalDimIsdnST : same as 'dimIsdnST', new enumeration added for RFC1155 compatibility.")
isgVGIsdnEIAStatTEI = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatTEI.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatTEI.setDescription('The Terminal Endpoint Indicator for the port.')
isgVGIsdnEIAStatSPBU = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 50))).clone(namedValues=NamedValues(("main", 0), ("backup", 1), ("disabled", 2), ("newvalMain", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatSPBU.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatSPBU.setDescription("The Same Port Backup feature for the port. newvalMain : same functionality as 'main', new enumeration added for RFC1155 compatibility.")
isgVGIsdnEIAStatL1State = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 50))).clone(namedValues=NamedValues(("l1Setup", 0), ("l1Deactive", 1), ("l1Active", 2), ("l1B1Loop", 3), ("l1B2Loop", 4), ("l1B1B2Loop", 5), ("l12BDLoop", 6), ("unknownState", 7), ("newvalL1Setup", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatL1State.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatL1State.setDescription("The Level 1 State for the port. l1Setup : Setup State. l1Deactive : Inactive State. l1Active : Active State. l1B1Loop : Loop Test State. l1B2Loop : Loop Test State. l1B1B2Loop : Loop Test State. l12BDLoop : Loop Test State. newvalL1Setup : same functionality as 'l1Setup', new enumeration added for RFC1155 compatibility.")
isgVGIsdnEIAStatChanType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 50))).clone(namedValues=NamedValues(("error", 0), ("isdnD", 1), ("isdnB1", 2), ("isdnB2", 3), ("isdn2B", 4), ("isdnB", 5), ("newvalError", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatChanType.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatChanType.setDescription("ISDN Channel Type. newvalError : same functionaliy as 'error', new enumeration added for RFC1155 compatibility.")
isgVGIsdnEIAStatAccType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 50))).clone(namedValues=NamedValues(("permanent", 0), ("cktMode", 1), ("pktMode", 2), ("dPckEnabled", 3), ("dPckDisabled", 4), ("notConnected", 5), ("newvalPermanent", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isgVGIsdnEIAStatAccType.setStatus('mandatory')
if mibBuilder.loadTexts: isgVGIsdnEIAStatAccType.setDescription("ISDN Channel Access Type. Value not available for D Channels. permanent : Access type permanent. cktMode : Access type circuit mode. pktMode : Access type packet mode. dPckEnabled : Access type D packet enabled. dPckDisabled : Access type D packet disabled. notConnected : Not connected. newvalPermanent : same functionality as 'permanent', new enumeration added for RFC1155 compatibility.")
mibBuilder.exportSymbols("EIA-OPT-MIB", isgVGIsdnEIAStatDimType=isgVGIsdnEIAStatDimType, isgVGIsdnEIAStatTable=isgVGIsdnEIAStatTable, cdx6500Controls=cdx6500Controls, cdx6500StatEIAEntryConnType=cdx6500StatEIAEntryConnType, cdx6500=cdx6500, isgVGIsdnEIAStatChanType=isgVGIsdnEIAStatChanType, cdxProductSpecific=cdxProductSpecific, isgVGIsdnEIAStatAccType=isgVGIsdnEIAStatAccType, cdx6500StatOtherStatsGroup=cdx6500StatOtherStatsGroup, DisplayString=DisplayString, isgVGIsdnEIAStatEntry=isgVGIsdnEIAStatEntry, cdx6500StatEIATable=cdx6500StatEIATable, codex=codex, isgVGIsdnEIAStatSPBU=isgVGIsdnEIAStatSPBU, cdx6500StatEIAEntryPortNumber=cdx6500StatEIAEntryPortNumber, isgVGIsdnEIAStatL1State=isgVGIsdnEIAStatL1State, isgVGIsdnEIAStatTEI=isgVGIsdnEIAStatTEI, isgVGIsdnEIAStatDimCfgn=isgVGIsdnEIAStatDimCfgn, cdx6500StatEIAEntrySignalStatus=cdx6500StatEIAEntrySignalStatus, isgVGIsdnEIAStatPortNum=isgVGIsdnEIAStatPortNum, cdx6500StatEIAEntryDimType=cdx6500StatEIAEntryDimType, cdx6500StatEIAEntryDimCfgn=cdx6500StatEIAEntryDimCfgn, cdx6500Statistics=cdx6500Statistics, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, cdx6500StatEIAEntryEiaState=cdx6500StatEIAEntryEiaState, cdx6500Configuration=cdx6500Configuration, cdx6500StatEIAEntry=cdx6500StatEIAEntry)
