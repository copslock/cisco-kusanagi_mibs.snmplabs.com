#
# PySNMP MIB module HPN-ICF-LswTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswTRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfLswFrameIndex, hpnicfLswSlotIndex, hpnicfLswSubslotIndex = mibBuilder.importSymbols("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex", "hpnicfLswSlotIndex", "hpnicfLswSubslotIndex")
hpnicfDevMPowerNum, hpnicfDevMFanNum, hpnicfDevMFirstTrapTime = mibBuilder.importSymbols("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum", "hpnicfDevMFanNum", "hpnicfDevMFirstTrapTime")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, ModuleIdentity, MibIdentifier, Bits, NotificationType, IpAddress, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ModuleIdentity", "MibIdentifier", "Bits", "NotificationType", "IpAddress", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfLswTrapMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12))
hpnicfLswTrapMib.setRevisions(('2011-11-26 00:00',))
if mibBuilder.loadTexts: hpnicfLswTrapMib.setLastUpdated('201111260000Z')
if mibBuilder.loadTexts: hpnicfLswTrapMib.setOrganization('')
hpnicfsLswTRAPMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1))
hpnicfpowerfailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 1)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"), ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFirstTrapTime"))
if mibBuilder.loadTexts: hpnicfpowerfailure.setStatus('current')
hpnicfPowerNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 2)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"), ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFirstTrapTime"))
if mibBuilder.loadTexts: hpnicfPowerNormal.setStatus('current')
hpnicfMasterPowerNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 3)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfMasterPowerNormal.setStatus('current')
hpnicfSlavePowerNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 4)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfSlavePowerNormal.setStatus('current')
hpnicfPowerRemoved = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 5)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfPowerRemoved.setStatus('current')
hpnicffanfailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 6)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFanNum"))
if mibBuilder.loadTexts: hpnicffanfailure.setStatus('current')
hpnicfFanNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 7)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFanNum"))
if mibBuilder.loadTexts: hpnicfFanNormal.setStatus('current')
hpnicfBoardRemoved = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 8)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardRemoved.setStatus('current')
hpnicfBoardInserted = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 9)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardInserted.setStatus('current')
hpnicfBoardFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 10)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardFailure.setStatus('current')
hpnicfBoardNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 11)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardNormal.setStatus('current')
hpnicfSubcardRemove = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 12)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSubslotIndex"))
if mibBuilder.loadTexts: hpnicfSubcardRemove.setStatus('current')
hpnicfSubcardInsert = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 13)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSubslotIndex"))
if mibBuilder.loadTexts: hpnicfSubcardInsert.setStatus('current')
hpnicfBoardTemperatureLower = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 14)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureLower.setStatus('current')
hpnicfBoardTemperatureFromLowerToNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 15)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureFromLowerToNormal.setStatus('current')
hpnicfBoardTemperatureHigher = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 16)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureHigher.setStatus('current')
hpnicfBoardTemperatureFormHigherToNormal = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 17)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBoardTemperatureFormHigherToNormal.setStatus('current')
hpnicfRequestLoading = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 18)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfRequestLoading.setStatus('current')
hpnicfLoadFailure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 19)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfLoadFailure.setStatus('current')
hpnicfLoadFinished = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 20)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfLoadFinished.setStatus('current')
hpnicfBackBoardModeSetFuilure = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 21)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"))
if mibBuilder.loadTexts: hpnicfBackBoardModeSetFuilure.setStatus('current')
hpnicfBackBoardModeSetOK = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 22)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"))
if mibBuilder.loadTexts: hpnicfBackBoardModeSetOK.setStatus('current')
hpnicfPowerInserted = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 23)).setObjects(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"))
if mibBuilder.loadTexts: hpnicfPowerInserted.setStatus('current')
hpnicfBootImageUpdated = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 24)).setObjects(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"), ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
if mibBuilder.loadTexts: hpnicfBootImageUpdated.setStatus('current')
hpnicfNetworkHealthMonitorFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 98))
hpnicfNetworkHealthMonitorNormal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 99))
mibBuilder.exportSymbols("HPN-ICF-LswTRAP-MIB", hpnicfPowerNormal=hpnicfPowerNormal, hpnicfLoadFailure=hpnicfLoadFailure, hpnicfBoardInserted=hpnicfBoardInserted, hpnicfSubcardRemove=hpnicfSubcardRemove, hpnicfBoardTemperatureFromLowerToNormal=hpnicfBoardTemperatureFromLowerToNormal, hpnicfPowerInserted=hpnicfPowerInserted, hpnicffanfailure=hpnicffanfailure, hpnicfMasterPowerNormal=hpnicfMasterPowerNormal, hpnicfLoadFinished=hpnicfLoadFinished, PYSNMP_MODULE_ID=hpnicfLswTrapMib, hpnicfRequestLoading=hpnicfRequestLoading, hpnicfFanNormal=hpnicfFanNormal, hpnicfLswTrapMib=hpnicfLswTrapMib, hpnicfBoardNormal=hpnicfBoardNormal, hpnicfBoardFailure=hpnicfBoardFailure, hpnicfBoardRemoved=hpnicfBoardRemoved, hpnicfBoardTemperatureFormHigherToNormal=hpnicfBoardTemperatureFormHigherToNormal, hpnicfBackBoardModeSetOK=hpnicfBackBoardModeSetOK, hpnicfNetworkHealthMonitorFailure=hpnicfNetworkHealthMonitorFailure, hpnicfBackBoardModeSetFuilure=hpnicfBackBoardModeSetFuilure, hpnicfBoardTemperatureHigher=hpnicfBoardTemperatureHigher, hpnicfpowerfailure=hpnicfpowerfailure, hpnicfsLswTRAPMibObject=hpnicfsLswTRAPMibObject, hpnicfSlavePowerNormal=hpnicfSlavePowerNormal, hpnicfSubcardInsert=hpnicfSubcardInsert, hpnicfBootImageUpdated=hpnicfBootImageUpdated, hpnicfBoardTemperatureLower=hpnicfBoardTemperatureLower, hpnicfNetworkHealthMonitorNormal=hpnicfNetworkHealthMonitorNormal, hpnicfPowerRemoved=hpnicfPowerRemoved)
