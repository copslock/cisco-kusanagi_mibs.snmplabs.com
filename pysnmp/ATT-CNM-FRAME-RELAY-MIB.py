#
# PySNMP MIB module ATT-CNM-FRAME-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATT-CNM-FRAME-RELAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, NotificationType, MibIdentifier, enterprises, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, Unsigned32, IpAddress, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "NotificationType", "MibIdentifier", "enterprises", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "Unsigned32", "IpAddress", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
att_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 74)).setLabel("att-2")
att_products = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1)).setLabel("att-products")
att_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2)).setLabel("att-mgmt")
att_cnmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 1, 9)).setLabel("att-cnmAgent")
att_cnm = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15)).setLabel("att-cnm")
att_cnm_fr = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 15, 7)).setLabel("att-cnm-fr")
attCNMfrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1), )
if mibBuilder.loadTexts: attCNMfrConfigTable.setStatus('mandatory')
attCNMfrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1), ).setIndexNames((0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrConfigIndex"))
if mibBuilder.loadTexts: attCNMfrConfigEntry.setStatus('mandatory')
attCNMfrConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrConfigIndex.setStatus('mandatory')
attCNMfrMeasMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrMeasMaxIntervals.setStatus('mandatory')
attCNMfrMeasIntervalLen = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrMeasIntervalLen.setStatus('mandatory')
attCNMfrPVCMeasMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCMeasMaxIntervals.setStatus('mandatory')
attCNMfrPVCMeasIntervalLen = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCMeasIntervalLen.setStatus('mandatory')
attCNMfrMeasTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2), )
if mibBuilder.loadTexts: attCNMfrMeasTable.setStatus('mandatory')
attCNMfrMeasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1), ).setIndexNames((0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrMeasIndex"), (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrMeasInterval"))
if mibBuilder.loadTexts: attCNMfrMeasEntry.setStatus('mandatory')
attCNMfrMeasIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrMeasIndex.setStatus('mandatory')
attCNMfrMeasInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrMeasInterval.setStatus('mandatory')
attCNMfrMeasTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrMeasTimeStamp.setStatus('mandatory')
attCNMfrMeasLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrMeasLocalTime.setStatus('mandatory')
attCNMfrReceivedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrReceivedOctets.setStatus('mandatory')
attCNMfrSentOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrSentOctets.setStatus('mandatory')
attCNMfrReceivedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrReceivedFrames.setStatus('mandatory')
attCNMfrSentFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrSentFrames.setStatus('mandatory')
attCNMfrBadFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrBadFrames.setStatus('mandatory')
attCNMfrReceiverOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrReceiverOverruns.setStatus('mandatory')
attCNMfrPVCMeasTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3), )
if mibBuilder.loadTexts: attCNMfrPVCMeasTable.setStatus('mandatory')
attCNMfrPVCMeasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1), ).setIndexNames((0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCMeasIfIndex"), (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCMeasIndex"), (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCMeasInterval"))
if mibBuilder.loadTexts: attCNMfrPVCMeasEntry.setStatus('mandatory')
attCNMfrPVCMeasIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCMeasIfIndex.setStatus('mandatory')
attCNMfrPVCMeasIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCMeasIndex.setStatus('mandatory')
attCNMfrPVCMeasInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCMeasInterval.setStatus('mandatory')
attCNMfrPVCMeasTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCMeasTimeStamp.setStatus('mandatory')
attCNMfrPVCMeasLocalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCMeasLocalTime.setStatus('mandatory')
attCNMfrCongestionAtIngress = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrCongestionAtIngress.setStatus('mandatory')
attCNMfrCongestionAtEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrCongestionAtEgress.setStatus('mandatory')
attCNMfrPVCStatusTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4), )
if mibBuilder.loadTexts: attCNMfrPVCStatusTable.setStatus('mandatory')
attCNMfrPVCStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1), ).setIndexNames((0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCStatusIfIndex"), (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCStatusIndex"))
if mibBuilder.loadTexts: attCNMfrPVCStatusEntry.setStatus('mandatory')
attCNMfrPVCStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCStatusIfIndex.setStatus('mandatory')
attCNMfrPVCStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCStatusIndex.setStatus('mandatory')
attCNMfrPVCAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCAdminStatus.setStatus('mandatory')
attCNMfrPVCOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: attCNMfrPVCOperStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ATT-CNM-FRAME-RELAY-MIB", attCNMfrMeasIntervalLen=attCNMfrMeasIntervalLen, attCNMfrConfigEntry=attCNMfrConfigEntry, attCNMfrPVCMeasIfIndex=attCNMfrPVCMeasIfIndex, attCNMfrConfigTable=attCNMfrConfigTable, att_cnm_fr=att_cnm_fr, attCNMfrSentFrames=attCNMfrSentFrames, attCNMfrPVCOperStatus=attCNMfrPVCOperStatus, att_products=att_products, attCNMfrReceiverOverruns=attCNMfrReceiverOverruns, att_2=att_2, att_cnm=att_cnm, att_cnmAgent=att_cnmAgent, attCNMfrCongestionAtEgress=attCNMfrCongestionAtEgress, attCNMfrPVCAdminStatus=attCNMfrPVCAdminStatus, attCNMfrPVCMeasIntervalLen=attCNMfrPVCMeasIntervalLen, attCNMfrMeasTable=attCNMfrMeasTable, attCNMfrBadFrames=attCNMfrBadFrames, attCNMfrPVCStatusIndex=attCNMfrPVCStatusIndex, attCNMfrMeasInterval=attCNMfrMeasInterval, attCNMfrPVCMeasIndex=attCNMfrPVCMeasIndex, attCNMfrSentOctets=attCNMfrSentOctets, attCNMfrPVCStatusTable=attCNMfrPVCStatusTable, attCNMfrPVCMeasInterval=attCNMfrPVCMeasInterval, attCNMfrPVCStatusEntry=attCNMfrPVCStatusEntry, attCNMfrReceivedOctets=attCNMfrReceivedOctets, attCNMfrPVCMeasTimeStamp=attCNMfrPVCMeasTimeStamp, att_mgmt=att_mgmt, attCNMfrPVCMeasTable=attCNMfrPVCMeasTable, attCNMfrPVCStatusIfIndex=attCNMfrPVCStatusIfIndex, attCNMfrCongestionAtIngress=attCNMfrCongestionAtIngress, attCNMfrPVCMeasMaxIntervals=attCNMfrPVCMeasMaxIntervals, attCNMfrMeasMaxIntervals=attCNMfrMeasMaxIntervals, attCNMfrPVCMeasEntry=attCNMfrPVCMeasEntry, attCNMfrMeasEntry=attCNMfrMeasEntry, attCNMfrPVCMeasLocalTime=attCNMfrPVCMeasLocalTime, attCNMfrMeasTimeStamp=attCNMfrMeasTimeStamp, attCNMfrReceivedFrames=attCNMfrReceivedFrames, attCNMfrConfigIndex=attCNMfrConfigIndex, attCNMfrMeasLocalTime=attCNMfrMeasLocalTime, attCNMfrMeasIndex=attCNMfrMeasIndex)