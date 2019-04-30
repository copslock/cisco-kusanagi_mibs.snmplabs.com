#
# PySNMP MIB module MY-PROCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-PROCESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, MibIdentifier, TimeTicks, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter64, NotificationType, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter64", "NotificationType", "Unsigned32", "IpAddress", "iso")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
myProcessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36))
myProcessMIB.setRevisions(('2003-10-14 00:00',))
if mibBuilder.loadTexts: myProcessMIB.setLastUpdated('200310140000Z')
if mibBuilder.loadTexts: myProcessMIB.setOrganization('D-Link Crop.')
class Percent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

myCPUMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1))
myCpuGeneralMibsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1))
myCPUUtilization5Sec = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 1), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization5Sec.setStatus('current')
myCPUUtilization1Min = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 2), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization1Min.setStatus('current')
myCPUUtilization5Min = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization5Min.setStatus('current')
myCPUUtilizationWarning = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 4), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCPUUtilizationWarning.setStatus('current')
myCPUUtilizationCritical = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 5), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCPUUtilizationCritical.setStatus('current')
myNodeCPUTotalTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2), )
if mibBuilder.loadTexts: myNodeCPUTotalTable.setStatus('current')
myNodeCPUTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1), ).setIndexNames((0, "MY-PROCESS-MIB", "myNodeCPUTotalIndex"))
if mibBuilder.loadTexts: myNodeCPUTotalEntry.setStatus('current')
myNodeCPUTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotalIndex.setStatus('current')
myNodeCPUTotalName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotalName.setStatus('current')
myNodeCPUTotal5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal5sec.setStatus('current')
myNodeCPUTotal1min = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal1min.setStatus('current')
myNodeCPUTotal5min = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal5min.setStatus('current')
myNodeCPUTotalWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 6), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeCPUTotalWarning.setStatus('current')
myNodeCPUTotalCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 7), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeCPUTotalCritical.setStatus('current')
myProcessMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2))
myProcessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1))
myProcessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2))
myProcessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1, 1)).setObjects(("MY-PROCESS-MIB", "myCPUUtilizationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myProcessMIBCompliance = myProcessMIBCompliance.setStatus('current')
myCPUUtilizationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 1)).setObjects(("MY-PROCESS-MIB", "myCPUUtilization5Sec"), ("MY-PROCESS-MIB", "myCPUUtilization1Min"), ("MY-PROCESS-MIB", "myCPUUtilization5Min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myCPUUtilizationMIBGroup = myCPUUtilizationMIBGroup.setStatus('current')
myNodeCPUTotalGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 2)).setObjects(("MY-PROCESS-MIB", "myNodeCPUTotalIndex"), ("MY-PROCESS-MIB", "myNodeCPUTotalName"), ("MY-PROCESS-MIB", "myNodeCPUTotal5sec"), ("MY-PROCESS-MIB", "myNodeCPUTotal1min"), ("MY-PROCESS-MIB", "myNodeCPUTotal5min"), ("MY-PROCESS-MIB", "myNodeCPUTotalWarning"), ("MY-PROCESS-MIB", "myNodeCPUTotalCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNodeCPUTotalGroups = myNodeCPUTotalGroups.setStatus('current')
mibBuilder.exportSymbols("MY-PROCESS-MIB", myCPUMIBObjects=myCPUMIBObjects, myCPUUtilizationWarning=myCPUUtilizationWarning, myProcessMIBCompliances=myProcessMIBCompliances, myCPUUtilization5Sec=myCPUUtilization5Sec, Percent=Percent, myNodeCPUTotalEntry=myNodeCPUTotalEntry, myNodeCPUTotal5min=myNodeCPUTotal5min, myNodeCPUTotal5sec=myNodeCPUTotal5sec, myCpuGeneralMibsGroup=myCpuGeneralMibsGroup, myNodeCPUTotalCritical=myNodeCPUTotalCritical, myCPUUtilizationCritical=myCPUUtilizationCritical, myNodeCPUTotalWarning=myNodeCPUTotalWarning, myProcessMIBConformance=myProcessMIBConformance, myCPUUtilization1Min=myCPUUtilization1Min, myCPUUtilization5Min=myCPUUtilization5Min, PYSNMP_MODULE_ID=myProcessMIB, myNodeCPUTotalTable=myNodeCPUTotalTable, myProcessMIBCompliance=myProcessMIBCompliance, myNodeCPUTotalGroups=myNodeCPUTotalGroups, myNodeCPUTotalIndex=myNodeCPUTotalIndex, myProcessMIB=myProcessMIB, myProcessMIBGroups=myProcessMIBGroups, myCPUUtilizationMIBGroup=myCPUUtilizationMIBGroup, myNodeCPUTotalName=myNodeCPUTotalName, myNodeCPUTotal1min=myNodeCPUTotal1min)