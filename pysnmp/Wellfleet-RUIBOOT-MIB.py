#
# PySNMP MIB module Wellfleet-RUIBOOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-RUIBOOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:34:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Gauge32, Bits, mib_2, Integer32, iso, NotificationType, Unsigned32, mgmt, Counter64, enterprises, Counter32, IpAddress, ModuleIdentity, Opaque, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Gauge32", "Bits", "mib-2", "Integer32", "iso", "NotificationType", "Unsigned32", "mgmt", "Counter64", "enterprises", "Counter32", "IpAddress", "ModuleIdentity", "Opaque", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfRuiBootGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfRuiBootGroup")
wfRuiBoot = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1))
wfRuiBootBaseDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRuiBootBaseDelete.setStatus('mandatory')
wfRuiBootBaseDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRuiBootBaseDisable.setStatus('mandatory')
wfRuiBootBaseState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpres", 4))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRuiBootBaseState.setStatus('mandatory')
wfRuiBootTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2), )
if mibBuilder.loadTexts: wfRuiBootTable.setStatus('mandatory')
wfRuiBootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1), ).setIndexNames((0, "Wellfleet-RUIBOOT-MIB", "wfRuiBootDateAndTime"))
if mibBuilder.loadTexts: wfRuiBootEntry.setStatus('mandatory')
wfRuiBootDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRuiBootDelete.setStatus('mandatory')
wfRuiBootDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRuiBootDisable.setStatus('mandatory')
wfRuiBootState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("scheduled", 1), ("aged", 2), ("time", 3), ("error", 4), ("initializing", 5))).clone('initializing')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRuiBootState.setStatus('mandatory')
wfRuiBootDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRuiBootDateAndTime.setStatus('mandatory')
wfRuiBootImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRuiBootImageName.setStatus('mandatory')
wfRuiBootConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRuiBootConfigName.setStatus('mandatory')
wfRuiBootErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("imagename", 2), ("configname", 3), ("imagefilenotfound", 4), ("configfilenotfound", 5), ("imagefilecorrupt", 6), ("filesystem", 7), ("invalidtime", 8))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRuiBootErrorCode.setStatus('mandatory')
wfRuiBootSystemErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 14, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRuiBootSystemErrorCode.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-RUIBOOT-MIB", wfRuiBootErrorCode=wfRuiBootErrorCode, wfRuiBootImageName=wfRuiBootImageName, wfRuiBootState=wfRuiBootState, wfRuiBootConfigName=wfRuiBootConfigName, wfRuiBootDateAndTime=wfRuiBootDateAndTime, wfRuiBootSystemErrorCode=wfRuiBootSystemErrorCode, wfRuiBootBaseDisable=wfRuiBootBaseDisable, wfRuiBootEntry=wfRuiBootEntry, wfRuiBootBaseDelete=wfRuiBootBaseDelete, wfRuiBootBaseState=wfRuiBootBaseState, wfRuiBoot=wfRuiBoot, wfRuiBootDisable=wfRuiBootDisable, wfRuiBootDelete=wfRuiBootDelete, wfRuiBootTable=wfRuiBootTable)
