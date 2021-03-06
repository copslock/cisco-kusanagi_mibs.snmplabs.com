#
# PySNMP MIB module FCTR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FCTR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, enterprises, Bits, Counter64, ModuleIdentity, MibIdentifier, TimeTicks, IpAddress, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "Bits", "Counter64", "ModuleIdentity", "MibIdentifier", "TimeTicks", "IpAddress", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class RequestedFlowControlMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("auto", 3))

class GrantedFlowControlMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("flowControl", 2), ("backPressure", 3), ("other", 4))

nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
nbFctr = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 2))
nbFctrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1))
nbFctrMgmtType = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonControl", 1), ("perDeviceOnly", 2), ("perPort", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrMgmtType.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrMgmtType.setDescription('Describes type of Flow Controle of the device. The nbFctrPortsRunTable and nbFctrPortsPermTable tables may not be supported in the per-device-only(2) case. Set new value for nbFctrGlbReqRun and/or nbFctrGlbReqPerm in per-port (3) should change this value for all ports in nbFctrPortsRunTable and/or nbFctrPortsPermTable.')
nbFctrGlbReqRun = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 2), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrGlbReqRun.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrGlbReqRun.setDescription('Requested mode of the device immediately to be set.')
nbFctrGlbGrntdRun = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 3), GrantedFlowControlMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrGlbGrntdRun.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrGlbGrntdRun.setDescription('Actual mode of the device.')
nbFctrGlbReqPerm = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 4), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrGlbReqPerm.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrGlbReqPerm.setDescription('Requested mode of the device, will be implemented from begin after next reset/reboot.')
nbFctrPortsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2), )
if mibBuilder.loadTexts: nbFctrPortsTable.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrPortsTable.setDescription('Flow control per port configuration table.')
nbFctrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1), ).setIndexNames((0, "FCTR-MIB", "nbFctrPort"))
if mibBuilder.loadTexts: nbFctrPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrPortEntry.setDescription('Describes Flow control configuration of the port.')
nbFctrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrPort.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrPort.setDescription('Number of Port to be managed.')
nbFctrPortRunReqMode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 2), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrPortRunReqMode.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrPortRunReqMode.setDescription('Requested mode of the port immediately to be set.')
nbFctrPortRunGrntd = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 3), GrantedFlowControlMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrPortRunGrntd.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrPortRunGrntd.setDescription('Actual mode of the port.')
nbFctrPortPermReqMode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 4), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrPortPermReqMode.setStatus('mandatory')
if mibBuilder.loadTexts: nbFctrPortPermReqMode.setDescription('Requested mode of the port immediately to be set.')
mibBuilder.exportSymbols("FCTR-MIB", nbFctrGlbGrntdRun=nbFctrGlbGrntdRun, nbFctrGlbReqPerm=nbFctrGlbReqPerm, nbFctrInfo=nbFctrInfo, nbFctrPortEntry=nbFctrPortEntry, GrantedFlowControlMode=GrantedFlowControlMode, nbFctrPortRunGrntd=nbFctrPortRunGrntd, nbFctrPortPermReqMode=nbFctrPortPermReqMode, nbFctrPortsTable=nbFctrPortsTable, nbSwitchG1=nbSwitchG1, nbase=nbase, nbFctrPort=nbFctrPort, RequestedFlowControlMode=RequestedFlowControlMode, nbFctrGlbReqRun=nbFctrGlbReqRun, nbFctrMgmtType=nbFctrMgmtType, nbSwitchG1Il=nbSwitchG1Il, nbFctr=nbFctr, nbFctrPortRunReqMode=nbFctrPortRunReqMode)
