#
# PySNMP MIB module PDN-DS1EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DS1EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ent_ds1, = mibBuilder.importSymbols("PDN-HEADER-MIB", "ent-ds1")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Counter64, TimeTicks, Unsigned32, ModuleIdentity, Integer32, NotificationType, Gauge32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "TimeTicks", "Unsigned32", "ModuleIdentity", "Integer32", "NotificationType", "Gauge32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnDs1Ext = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5))
if mibBuilder.loadTexts: pdnDs1Ext.setLastUpdated('200204050000Z')
if mibBuilder.loadTexts: pdnDs1Ext.setOrganization('Paradyne Corp MIB Working Group')
if mibBuilder.loadTexts: pdnDs1Ext.setContactInfo('Paradyne Networks, Inc. 8545, 126th Ave. N., Largo, FL 33779 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editors: Vic Sperry')
if mibBuilder.loadTexts: pdnDs1Ext.setDescription('The Paradyne enterprise DS1/G.703 extension MIB. This MIB provides additional DS1 and G.703 (E1) configuration objects not provided by rfc2495.')
pdnDs1ExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1))
pdnDs1ExtConfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1), )
if mibBuilder.loadTexts: pdnDs1ExtConfTable.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtConfTable.setDescription('The Paradyne DS1/G.703 extension configuration table. This table is used for configuring extensions to DS1 and G.703 interfaces.')
pdnDs1ExtConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnDs1ExtConfEntry.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtConfEntry.setDescription('An entry in the Paradyne DS1/G.703 extension configuration table. Note: The objects used depend on the type of interface. For DS1: use pdnDs1ExtConfLineLengthType and one of (pdnDs1ExtConfLineLength or pdnDs1ExtConfLineBuildOut) For G.703: use pdnDs1ExtConfLineLengthType and pdnDs1ExtConfConnector ')
pdnDs1ExtConfLineLengthType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shortHaul", 1), ("longHaul", 2))).clone('longHaul')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineLengthType.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtConfLineLengthType.setDescription('This entry specifies the type of loop length for the interface. short-haul is intended for intra-building use. long-haul is intended for inter-building use.')
pdnDs1ExtConfLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("feet000To133", 1), ("feet134To266", 2), ("feet267To399", 3), ("feet400To533", 4), ("feet534To655", 5))).clone('feet000To133')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineLength.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtConfLineLength.setDescription('This entry specifies the loop length, in feet, for a short-haul DS1 line. This object only applies to DS1 interfaces. Note: This object shares a mutually exclusive relationship with the pdnDs1ExtConfLineBuildOut object i.e. only one of the two can be used for configuration at one time, based on the pdnDs1ExtConfLineLengthType object.')
pdnDs1ExtConfLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dB0Pnt0", 1), ("dB7Pnt5", 2), ("dB15Pnt0", 3), ("dB22Pnt5", 4))).clone('dB0Pnt0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineBuildOut.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtConfLineBuildOut.setDescription('This entry specifies the line build out, in decibels, for a long-haul DS1 line. dB0Pnt0 = 0.0 dB dB7Pnt5 = -7.5 dB dB15Pnt0 = -15.0 dB dB22Pnt5 = -22.5 dB This object only applies to DS1 interfaces. Note: This object shares a mutually exclusive relationship with the pdnDs1ExtConfLineLength object i.e. only one of the two can be used for configuration at one time, based on the pdnDs1ExtConfLineLengthType object.')
pdnDs1ExtConfConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bnc", 1), ("rj48", 2))).clone('rj48')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfConnector.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtConfConnector.setDescription('This entry specifies the type of connector to be used. This object only applies to G.703 interfaces. bnc: 75-Ohm connector supporting only short-haul. rj48: 120-Ohm connector supporting both short-haul and long-haul.')
pdnDs1ExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2))
pdnDs1ExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1))
pdnDs1ExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2))
pdnDs1ExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 1)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtT1ConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtCompliance = pdnDs1ExtCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtCompliance.setDescription('Compliance statement for using this MIB for configuring DS1 interfaces.')
pdnDs1ExtG703Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 2)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtE1ConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtG703Compliance = pdnDs1ExtG703Compliance.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtG703Compliance.setDescription('Compliance statement for using this MIB for configuring G.703 interfaces.')
pdnDs1ExtT1ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 1)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLength"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineBuildOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtT1ConfigGroup = pdnDs1ExtT1ConfigGroup.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtT1ConfigGroup.setDescription('A collection of configuration objects required for configuring a T1 interface.')
pdnDs1ExtE1ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 2)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfConnector"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtE1ConfigGroup = pdnDs1ExtE1ConfigGroup.setStatus('current')
if mibBuilder.loadTexts: pdnDs1ExtE1ConfigGroup.setDescription('A collection of configuration objects required for configuring a G.703 (E1) interface.')
mibBuilder.exportSymbols("PDN-DS1EXT-MIB", pdnDs1ExtE1ConfigGroup=pdnDs1ExtE1ConfigGroup, pdnDs1ExtConfLineLengthType=pdnDs1ExtConfLineLengthType, pdnDs1ExtT1ConfigGroup=pdnDs1ExtT1ConfigGroup, PYSNMP_MODULE_ID=pdnDs1Ext, pdnDs1ExtGroups=pdnDs1ExtGroups, pdnDs1ExtConfLineLength=pdnDs1ExtConfLineLength, pdnDs1ExtObjects=pdnDs1ExtObjects, pdnDs1ExtConformance=pdnDs1ExtConformance, pdnDs1ExtCompliances=pdnDs1ExtCompliances, pdnDs1ExtCompliance=pdnDs1ExtCompliance, pdnDs1ExtConfTable=pdnDs1ExtConfTable, pdnDs1ExtConfLineBuildOut=pdnDs1ExtConfLineBuildOut, pdnDs1ExtConfConnector=pdnDs1ExtConfConnector, pdnDs1ExtG703Compliance=pdnDs1ExtG703Compliance, pdnDs1ExtConfEntry=pdnDs1ExtConfEntry, pdnDs1Ext=pdnDs1Ext)
