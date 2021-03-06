#
# PySNMP MIB module MICOM-NAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOM-NAC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
micom_oscar, = mibBuilder.importSymbols("MICOM-OSCAR-MIB", "micom-oscar")
mcmSysAsciiTimeOfDay, = mibBuilder.importSymbols("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Gauge32, ModuleIdentity, Unsigned32, MibIdentifier, Counter64, Counter32, Integer32, NotificationType, ObjectIdentity, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Gauge32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter64", "Counter32", "Integer32", "NotificationType", "ObjectIdentity", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
micom_nac = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 15)).setLabel("micom-nac")
nac_configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1)).setLabel("nac-configuration")
nac_statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2)).setLabel("nac-statistics")
nacCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1))
nacCfgAddressResolutionTriesNumber = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacCfgAddressResolutionTriesNumber.setStatus('mandatory')
nacCfgAddressResolutionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacCfgAddressResolutionTimeout.setStatus('mandatory')
nacCfgCacheStatus = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("flush", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacCfgCacheStatus.setStatus('mandatory')
nacCfgNumberOfCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacCfgNumberOfCacheEntries.setStatus('mandatory')
nacCfgCounterReset = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("other", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nacCfgCounterReset.setStatus('obsolete')
nacCfgCustomerId = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacCfgCustomerId.setStatus('mandatory')
nacCacheTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2), )
if mibBuilder.loadTexts: nacCacheTable.setStatus('mandatory')
nacCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1), ).setIndexNames((0, "MICOM-NAC-MIB", "nacCacheEgressString"))
if mibBuilder.loadTexts: nacCacheEntry.setStatus('mandatory')
nacCacheEgressString = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacCacheEgressString.setStatus('mandatory')
nacCacheServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacCacheServerIpAddress.setStatus('mandatory')
nacCacheDnaAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 34))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacCacheDnaAddress.setStatus('mandatory')
nacCacheEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("learnt", 1), ("static", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacCacheEntryType.setStatus('mandatory')
nacCacheNumberOfHits = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacCacheNumberOfHits.setStatus('mandatory')
nacCacheEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("active", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacCacheEntryStatus.setStatus('mandatory')
nacServerTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3), )
if mibBuilder.loadTexts: nacServerTable.setStatus('mandatory')
nacServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1), ).setIndexNames((0, "MICOM-NAC-MIB", "nacServerIpAddress"))
if mibBuilder.loadTexts: nacServerEntry.setStatus('mandatory')
nacServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacServerIpAddress.setStatus('mandatory')
nacServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacServerName.setStatus('mandatory')
nacServerAvailStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("available", 1), ("transition", 2), ("notAvailable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerAvailStatus.setStatus('mandatory')
nacServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacServerStatus.setStatus('mandatory')
nacServerHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 180)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacServerHelloTime.setStatus('mandatory')
nacServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nacServerType.setStatus('mandatory')
nacServerRegistrationCount = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerRegistrationCount.setStatus('mandatory')
nacServerHello1Count = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerHello1Count.setStatus('mandatory')
nacServerHello2Count = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerHello2Count.setStatus('mandatory')
nacServerHello3Count = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerHello3Count.setStatus('mandatory')
nacServerRequestCount = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerRequestCount.setStatus('mandatory')
nacServerResolvedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerResolvedCount.setStatus('mandatory')
nacServerNoNumberCount = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerNoNumberCount.setStatus('mandatory')
nacServerTimeoutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacServerTimeoutCount.setStatus('mandatory')
nvmNacCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4))
nvmNacCfgAddressResolutionTriesNumber = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacCfgAddressResolutionTriesNumber.setStatus('mandatory')
nvmNacCfgAddressResolutionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacCfgAddressResolutionTimeout.setStatus('mandatory')
nvmNacCfgCacheStatus = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacCfgCacheStatus.setStatus('mandatory')
nvmNacCfgNumberOfCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmNacCfgNumberOfCacheEntries.setStatus('mandatory')
nvmNacCfgCustomerId = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmNacCfgCustomerId.setStatus('mandatory')
nvmNacCacheTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5), )
if mibBuilder.loadTexts: nvmNacCacheTable.setStatus('mandatory')
nvmNacCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1), ).setIndexNames((0, "MICOM-NAC-MIB", "nvmNacCacheEgressNumber"))
if mibBuilder.loadTexts: nvmNacCacheEntry.setStatus('mandatory')
nvmNacCacheEgressNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacCacheEgressNumber.setStatus('mandatory')
nvmNacCacheServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacCacheServerIpAddress.setStatus('mandatory')
nvmNacCacheDnaAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 34))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacCacheDnaAddress.setStatus('mandatory')
nvmNacServerTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6), )
if mibBuilder.loadTexts: nvmNacServerTable.setStatus('mandatory')
nvmNacServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1), ).setIndexNames((0, "MICOM-NAC-MIB", "nvmNacServerIpAddress"))
if mibBuilder.loadTexts: nvmNacServerEntry.setStatus('mandatory')
nvmNacServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacServerIpAddress.setStatus('mandatory')
nvmNacServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacServerName.setStatus('mandatory')
nvmNacServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacServerStatus.setStatus('mandatory')
nvmNacServerHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 180))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacServerHelloTime.setStatus('mandatory')
nvmNacServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmNacServerType.setStatus('mandatory')
nacStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1))
nacStatisticsCacheCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsCacheCount.setStatus('mandatory')
nacStatisticsStaticCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsStaticCount.setStatus('mandatory')
nacStatisticsRequestAllCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsRequestAllCount.setStatus('mandatory')
nacStatisticsLocalResolvedCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsLocalResolvedCount.setStatus('mandatory')
nacStatisticsPurgeCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsPurgeCount.setStatus('mandatory')
nacStatisticsVoiceRegCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsVoiceRegCount.setStatus('mandatory')
nacStatisticsDNAChangeCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsDNAChangeCount.setStatus('mandatory')
nacStatisticsServerCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsServerCount.setStatus('mandatory')
nacStatisticsServerRequestCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsServerRequestCount.setStatus('mandatory')
nacStatisticsServerResolvedCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsServerResolvedCount.setStatus('mandatory')
nacStatisticsServerNoNumberCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsServerNoNumberCount.setStatus('mandatory')
nacStatisticsTimeoutCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsTimeoutCount.setStatus('mandatory')
nacStatisticsHello1Count = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsHello1Count.setStatus('mandatory')
nacStatisticsHello2Count = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsHello2Count.setStatus('mandatory')
nacStatisticsHello3Count = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsHello3Count.setStatus('mandatory')
nacStatisticsRegistrationCount = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 15, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nacStatisticsRegistrationCount.setStatus('mandatory')
mcmAlarmNacFailedToLocateNAS = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 15) + (0,1)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"))
mcmAlarmNacNASIsDown = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 15) + (0,2)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-NAC-MIB", "nacServerIpAddress"))
mcmAlarmNacNASIsUp = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 15) + (0,3)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-NAC-MIB", "nacServerIpAddress"))
mibBuilder.exportSymbols("MICOM-NAC-MIB", nvmNacServerIpAddress=nvmNacServerIpAddress, micom_nac=micom_nac, nvmNacCacheServerIpAddress=nvmNacCacheServerIpAddress, nacStatisticsServerRequestCount=nacStatisticsServerRequestCount, nacServerHello2Count=nacServerHello2Count, nacStatisticsServerNoNumberCount=nacStatisticsServerNoNumberCount, nacCacheServerIpAddress=nacCacheServerIpAddress, mcmAlarmNacFailedToLocateNAS=mcmAlarmNacFailedToLocateNAS, nvmNacCacheEgressNumber=nvmNacCacheEgressNumber, nac_statistics=nac_statistics, nvmNacServerStatus=nvmNacServerStatus, nacServerHelloTime=nacServerHelloTime, nacStatisticsVoiceRegCount=nacStatisticsVoiceRegCount, nacCacheEntry=nacCacheEntry, nacServerHello1Count=nacServerHello1Count, nacServerNoNumberCount=nacServerNoNumberCount, mcmAlarmNacNASIsDown=mcmAlarmNacNASIsDown, nacServerStatus=nacServerStatus, nvmNacCfgAddressResolutionTriesNumber=nvmNacCfgAddressResolutionTriesNumber, nacStatisticsCacheCount=nacStatisticsCacheCount, nacStatisticsHello2Count=nacStatisticsHello2Count, nacCacheEntryType=nacCacheEntryType, nacServerEntry=nacServerEntry, nacStatisticsStaticCount=nacStatisticsStaticCount, nvmNacServerType=nvmNacServerType, nacStatisticsLocalResolvedCount=nacStatisticsLocalResolvedCount, nacCfgCustomerId=nacCfgCustomerId, mcmAlarmNacNASIsUp=mcmAlarmNacNASIsUp, nacServerIpAddress=nacServerIpAddress, nacServerHello3Count=nacServerHello3Count, nvmNacCfgGroup=nvmNacCfgGroup, nacServerTimeoutCount=nacServerTimeoutCount, nvmNacServerHelloTime=nvmNacServerHelloTime, nacStatisticsRequestAllCount=nacStatisticsRequestAllCount, nvmNacCacheEntry=nvmNacCacheEntry, nacCfgGroup=nacCfgGroup, nacCacheDnaAddress=nacCacheDnaAddress, nvmNacCacheTable=nvmNacCacheTable, nacStatisticsGroup=nacStatisticsGroup, nvmNacServerTable=nvmNacServerTable, nacServerRegistrationCount=nacServerRegistrationCount, nacStatisticsHello3Count=nacStatisticsHello3Count, nacCfgCacheStatus=nacCfgCacheStatus, nacCfgNumberOfCacheEntries=nacCfgNumberOfCacheEntries, nacCfgAddressResolutionTriesNumber=nacCfgAddressResolutionTriesNumber, nacCacheEntryStatus=nacCacheEntryStatus, nacServerAvailStatus=nacServerAvailStatus, nacStatisticsServerResolvedCount=nacStatisticsServerResolvedCount, nvmNacCfgCacheStatus=nvmNacCfgCacheStatus, nvmNacServerName=nvmNacServerName, nacStatisticsHello1Count=nacStatisticsHello1Count, nacCacheEgressString=nacCacheEgressString, nvmNacCfgNumberOfCacheEntries=nvmNacCfgNumberOfCacheEntries, nacServerRequestCount=nacServerRequestCount, nacCacheTable=nacCacheTable, nacServerName=nacServerName, nvmNacCacheDnaAddress=nvmNacCacheDnaAddress, nacStatisticsPurgeCount=nacStatisticsPurgeCount, nvmNacCfgAddressResolutionTimeout=nvmNacCfgAddressResolutionTimeout, nacCacheNumberOfHits=nacCacheNumberOfHits, nacCfgAddressResolutionTimeout=nacCfgAddressResolutionTimeout, nacCfgCounterReset=nacCfgCounterReset, nacServerResolvedCount=nacServerResolvedCount, nac_configuration=nac_configuration, nacServerTable=nacServerTable, nacStatisticsServerCount=nacStatisticsServerCount, nvmNacCfgCustomerId=nvmNacCfgCustomerId, nvmNacServerEntry=nvmNacServerEntry, nacStatisticsRegistrationCount=nacStatisticsRegistrationCount, nacServerType=nacServerType, nacStatisticsTimeoutCount=nacStatisticsTimeoutCount, nacStatisticsDNAChangeCount=nacStatisticsDNAChangeCount)
