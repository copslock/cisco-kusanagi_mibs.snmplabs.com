#
# PySNMP MIB module PDN-SPECTRUMMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-SPECTRUMMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifType, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifType", "ifIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Bits, Gauge32, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, IpAddress, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "IpAddress", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnSpectrumMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19))
pdnSpectrumMgmt.setRevisions(('2003-01-15 13:00', '2003-01-09 15:00', '1901-05-16 15:30', '1901-05-08 05:50',))
if mibBuilder.loadTexts: pdnSpectrumMgmt.setLastUpdated('200212091500Z')
if mibBuilder.loadTexts: pdnSpectrumMgmt.setOrganization('Paradyne Corp MIB Working Group')
pdnSpecMgmtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1))
pdnNewSpecMgmtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2))
newSpectrumMgmtGeneralConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1), )
if mibBuilder.loadTexts: newSpectrumMgmtGeneralConfigTable.setStatus('current')
newSpectrumMgmtGeneralConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "IF-MIB", "ifType"))
if mibBuilder.loadTexts: newSpectrumMgmtGeneralConfigEntry.setStatus('current')
newSpectrumMgmtSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: newSpectrumMgmtSelection.setStatus('current')
newSpectrumMgmtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enableOnly", 1), ("disableOnly", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtMode.setStatus('current')
newSpectrumMgmtLoopMeasurementMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("loopLength", 2), ("ewl", 3), ("quadMode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtLoopMeasurementMethod.setStatus('current')
newSpectrumMgmtEWLUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("feet", 2), ("meters", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtEWLUnits.setStatus('current')
newSpectrumMgmtConfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2), )
if mibBuilder.loadTexts: newSpectrumMgmtConfTable.setStatus('current')
newSpectrumMgmtConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: newSpectrumMgmtConfEntry.setStatus('current')
newSpectrumMgmtConfEWL = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: newSpectrumMgmtConfEWL.setStatus('current')
newSpectrumMgmtConfLoopLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("short", 1), ("medium", 2), ("long", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: newSpectrumMgmtConfLoopLength.setStatus('current')
newSpectrumMgmtConfQuadMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sameQuad", 1), ("segregatedQuadUpto3km", 2), ("segregatedQuadAbove3km", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: newSpectrumMgmtConfQuadMode.setStatus('current')
newSpectrumMgmtLineInfoTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3), )
if mibBuilder.loadTexts: newSpectrumMgmtLineInfoTable.setStatus('current')
newSpectrumMgmtLineInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: newSpectrumMgmtLineInfoEntry.setStatus('current')
newSpectrumMgmtXtucMax1TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 1), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXtucMax1TxRate.setStatus('current')
newSpectrumMgmtXtucMin1TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 2), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXtucMin1TxRate.setStatus('current')
newSpectrumMgmtXtucMax2TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 3), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXtucMax2TxRate.setStatus('current')
newSpectrumMgmtXtucMin2TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 4), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXtucMin2TxRate.setStatus('current')
newSpectrumMgmtXtucMaxTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 120))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXtucMaxTxPower.setStatus('current')
newSpectrumMgmtXturMax1TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 6), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXturMax1TxRate.setStatus('current')
newSpectrumMgmtXturMin1TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 7), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXturMin1TxRate.setStatus('current')
newSpectrumMgmtXturMax2TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 8), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXturMax2TxRate.setStatus('current')
newSpectrumMgmtXturMin2TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 9), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXturMin2TxRate.setStatus('current')
newSpectrumMgmtXturMaxTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 120))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtXturMaxTxPower.setStatus('current')
newSpectrumMgmtMinEWL = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtMinEWL.setStatus('current')
newSpectrumMgmtMaxEWL = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newSpectrumMgmtMaxEWL.setStatus('current')
spectrumMgmtCountryCode = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usa", 1), ("uk", 2))).clone('usa')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spectrumMgmtCountryCode.setStatus('deprecated')
spectrumMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3), )
if mibBuilder.loadTexts: spectrumMgmtTable.setStatus('deprecated')
spectrumMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: spectrumMgmtEntry.setStatus('deprecated')
spectrumMgmtEWL = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spectrumMgmtEWL.setStatus('deprecated')
spectrumMgmtAllowedSpeedsMin1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spectrumMgmtAllowedSpeedsMin1.setStatus('deprecated')
spectrumMgmtAllowedSpeedsMax1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spectrumMgmtAllowedSpeedsMax1.setStatus('deprecated')
spectrumMgmtAllowedSpeedsMin2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spectrumMgmtAllowedSpeedsMin2.setStatus('deprecated')
spectrumMgmtAllowedSpeedsMax2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spectrumMgmtAllowedSpeedsMax2.setStatus('deprecated')
spectrumMgmtLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("short", 1), ("medium", 2), ("long", 3))).clone('short')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spectrumMgmtLineLength.setStatus('deprecated')
pdnSpecMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3))
pdnSpecMgmtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1))
pdnSpecMgmtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 2))
pdnSpecMgmtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 2, 1)).setObjects(("PDN-SPECTRUMMGMT-MIB", "pdnGeneralConfigGroup"), ("PDN-SPECTRUMMGMT-MIB", "pdnLineInfoGroup"), ("PDN-SPECTRUMMGMT-MIB", "pdnEWLModeGroup"), ("PDN-SPECTRUMMGMT-MIB", "pdnLoopLengthModeGroup"), ("PDN-SPECTRUMMGMT-MIB", "pdnQuadModeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnSpecMgmtCompliance = pdnSpecMgmtCompliance.setStatus('current')
pdnGeneralConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 1)).setObjects(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtSelection"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMode"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtLoopMeasurementMethod"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtEWLUnits"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnGeneralConfigGroup = pdnGeneralConfigGroup.setStatus('current')
pdnLineInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 2)).setObjects(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMax1TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMin1TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMax2TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMin2TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMaxTxPower"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMax1TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMin1TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMax2TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMin2TxRate"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMaxTxPower"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMinEWL"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMaxEWL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnLineInfoGroup = pdnLineInfoGroup.setStatus('current')
pdnEWLModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 3)).setObjects(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtConfEWL"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMinEWL"), ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMaxEWL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEWLModeGroup = pdnEWLModeGroup.setStatus('current')
pdnLoopLengthModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 4)).setObjects(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtConfLoopLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnLoopLengthModeGroup = pdnLoopLengthModeGroup.setStatus('current')
pdnQuadModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 5)).setObjects(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtConfQuadMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnQuadModeGroup = pdnQuadModeGroup.setStatus('current')
pdnSpectrumMgmtDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 7)).setObjects(("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtCountryCode"), ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtEWL"), ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtLineLength"), ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMin1"), ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMax1"), ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMin2"), ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMax2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnSpectrumMgmtDeprecatedGroup = pdnSpectrumMgmtDeprecatedGroup.setStatus('deprecated')
mibBuilder.exportSymbols("PDN-SPECTRUMMGMT-MIB", spectrumMgmtEWL=spectrumMgmtEWL, spectrumMgmtAllowedSpeedsMax2=spectrumMgmtAllowedSpeedsMax2, spectrumMgmtCountryCode=spectrumMgmtCountryCode, newSpectrumMgmtConfEntry=newSpectrumMgmtConfEntry, newSpectrumMgmtXturMaxTxPower=newSpectrumMgmtXturMaxTxPower, newSpectrumMgmtGeneralConfigTable=newSpectrumMgmtGeneralConfigTable, newSpectrumMgmtConfEWL=newSpectrumMgmtConfEWL, pdnGeneralConfigGroup=pdnGeneralConfigGroup, pdnSpecMgmtObjects=pdnSpecMgmtObjects, spectrumMgmtEntry=spectrumMgmtEntry, newSpectrumMgmtLineInfoTable=newSpectrumMgmtLineInfoTable, newSpectrumMgmtMinEWL=newSpectrumMgmtMinEWL, newSpectrumMgmtMaxEWL=newSpectrumMgmtMaxEWL, newSpectrumMgmtLoopMeasurementMethod=newSpectrumMgmtLoopMeasurementMethod, pdnSpecMgmtCompliance=pdnSpecMgmtCompliance, pdnSpecMgmtCompliances=pdnSpecMgmtCompliances, newSpectrumMgmtLineInfoEntry=newSpectrumMgmtLineInfoEntry, newSpectrumMgmtXtucMin2TxRate=newSpectrumMgmtXtucMin2TxRate, newSpectrumMgmtXturMax1TxRate=newSpectrumMgmtXturMax1TxRate, spectrumMgmtAllowedSpeedsMin2=spectrumMgmtAllowedSpeedsMin2, spectrumMgmtAllowedSpeedsMin1=spectrumMgmtAllowedSpeedsMin1, spectrumMgmtAllowedSpeedsMax1=spectrumMgmtAllowedSpeedsMax1, pdnSpecMgmtConformance=pdnSpecMgmtConformance, pdnSpecMgmtGroups=pdnSpecMgmtGroups, newSpectrumMgmtConfQuadMode=newSpectrumMgmtConfQuadMode, pdnSpectrumMgmt=pdnSpectrumMgmt, newSpectrumMgmtSelection=newSpectrumMgmtSelection, newSpectrumMgmtXtucMin1TxRate=newSpectrumMgmtXtucMin1TxRate, newSpectrumMgmtConfLoopLength=newSpectrumMgmtConfLoopLength, newSpectrumMgmtEWLUnits=newSpectrumMgmtEWLUnits, newSpectrumMgmtConfTable=newSpectrumMgmtConfTable, pdnQuadModeGroup=pdnQuadModeGroup, newSpectrumMgmtXturMax2TxRate=newSpectrumMgmtXturMax2TxRate, newSpectrumMgmtGeneralConfigEntry=newSpectrumMgmtGeneralConfigEntry, newSpectrumMgmtXturMin1TxRate=newSpectrumMgmtXturMin1TxRate, newSpectrumMgmtXtucMax2TxRate=newSpectrumMgmtXtucMax2TxRate, newSpectrumMgmtXturMin2TxRate=newSpectrumMgmtXturMin2TxRate, newSpectrumMgmtXtucMax1TxRate=newSpectrumMgmtXtucMax1TxRate, newSpectrumMgmtMode=newSpectrumMgmtMode, PYSNMP_MODULE_ID=pdnSpectrumMgmt, newSpectrumMgmtXtucMaxTxPower=newSpectrumMgmtXtucMaxTxPower, pdnEWLModeGroup=pdnEWLModeGroup, pdnSpectrumMgmtDeprecatedGroup=pdnSpectrumMgmtDeprecatedGroup, spectrumMgmtTable=spectrumMgmtTable, pdnLoopLengthModeGroup=pdnLoopLengthModeGroup, spectrumMgmtLineLength=spectrumMgmtLineLength, pdnLineInfoGroup=pdnLineInfoGroup, pdnNewSpecMgmtObjects=pdnNewSpecMgmtObjects)