#
# PySNMP MIB module CISCO-SCAS-BB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SCAS-BB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
spvIndex, pmoduleIndex, linkIndex, linkModuleIndex = mibBuilder.importSymbols("PCUBE-SE-MIB", "spvIndex", "pmoduleIndex", "linkIndex", "linkModuleIndex")
pcubeWorkgroup, pcubeModules = mibBuilder.importSymbols("PCUBE-SMI", "pcubeWorkgroup", "pcubeModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Bits, Integer32, Gauge32, iso, Counter64, NotificationType, ModuleIdentity, Counter32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Bits", "Integer32", "Gauge32", "iso", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcubeEngageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 2, 4))
pcubeEngageMIB.setRevisions(('2006-05-10 00:00', '2004-12-21 00:00', '2004-07-01 00:00', '2002-07-03 20:00',))
if mibBuilder.loadTexts: pcubeEngageMIB.setLastUpdated('200605100000Z')
if mibBuilder.loadTexts: pcubeEngageMIB.setOrganization('Cisco Systems, Inc.')
pcubeEngageObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 4, 2))
pcubeEngageConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3))
pcubeEngageGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1))
pcubeEngageCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 2))
serviceGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 4, 2, 1))
linkGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2))
packageGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3))
subscriberGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4))
serviceCounterGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5))
serviceTable = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 4, 2, 1, 1))
linkServiceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1), )
if mibBuilder.loadTexts: linkServiceUsageTable.setStatus('current')
linkServiceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1), ).setIndexNames((0, "PCUBE-SE-MIB", "linkModuleIndex"), (0, "PCUBE-SE-MIB", "linkIndex"), (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"))
if mibBuilder.loadTexts: linkServiceUsageEntry.setStatus('current')
linkServiceUsageUpVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 1), Counter32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUsageUpVolume.setStatus('current')
linkServiceUsageDownVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 2), Counter32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUsageDownVolume.setStatus('current')
linkServiceUsageNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 3), Counter32()).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUsageNumSessions.setStatus('current')
linkServiceUsageDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUsageDuration.setStatus('current')
linkServiceUsageConcurrentSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 5), Counter32()).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUsageConcurrentSessions.setStatus('current')
linkServiceUsageActiveSubscribers = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 6), Counter32()).setUnits('subscribers').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUsageActiveSubscribers.setStatus('current')
linkServiceUpDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUpDroppedPackets.setStatus('current')
linkServiceDownDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceDownDroppedPackets.setStatus('current')
linkServiceUpDroppedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 9), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceUpDroppedBytes.setStatus('current')
linkServiceDownDroppedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 10), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: linkServiceDownDroppedBytes.setStatus('current')
packageCounterTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1), )
if mibBuilder.loadTexts: packageCounterTable.setStatus('current')
packageCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1), ).setIndexNames((0, "PCUBE-SE-MIB", "pmoduleIndex"), (0, "CISCO-SCAS-BB-MIB", "packageCounterIndex"))
if mibBuilder.loadTexts: packageCounterEntry.setStatus('current')
packageCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: packageCounterIndex.setStatus('current')
packageCounterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: packageCounterStatus.setStatus('current')
packageCounterName = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packageCounterName.setStatus('current')
packageCounterActiveSubscribers = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packageCounterActiveSubscribers.setStatus('current')
packageServiceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2), )
if mibBuilder.loadTexts: packageServiceUsageTable.setStatus('current')
packageServiceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1), ).setIndexNames((0, "PCUBE-SE-MIB", "pmoduleIndex"), (0, "CISCO-SCAS-BB-MIB", "packageCounterIndex"), (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"))
if mibBuilder.loadTexts: packageServiceUsageEntry.setStatus('current')
packageServiceUsageUpVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 1), Counter32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUsageUpVolume.setStatus('current')
packageServiceUsageDownVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 2), Counter32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUsageDownVolume.setStatus('current')
packageServiceUsageNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 3), Counter32()).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUsageNumSessions.setStatus('current')
packageServiceUsageDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUsageDuration.setStatus('current')
packageServiceUsageConcurrentSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 5), Counter32()).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUsageConcurrentSessions.setStatus('current')
packageServiceUsageActiveSubscribers = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 6), Counter32()).setUnits('subscribers').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUsageActiveSubscribers.setStatus('current')
packageServiceUpDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUpDroppedPackets.setStatus('current')
packageServiceDownDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceDownDroppedPackets.setStatus('current')
packageServiceUpDroppedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 9), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceUpDroppedBytes.setStatus('current')
packageServiceDownDroppedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 10), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: packageServiceDownDroppedBytes.setStatus('current')
subscribersTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1), )
if mibBuilder.loadTexts: subscribersTable.setStatus('current')
subscribersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1, 1), ).setIndexNames((0, "PCUBE-SE-MIB", "pmoduleIndex"), (0, "PCUBE-SE-MIB", "spvIndex"))
if mibBuilder.loadTexts: subscribersEntry.setStatus('current')
subscriberPackageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberPackageIndex.setStatus('current')
subscriberServiceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2), )
if mibBuilder.loadTexts: subscriberServiceUsageTable.setStatus('current')
subscriberServiceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1), ).setIndexNames((0, "PCUBE-SE-MIB", "pmoduleIndex"), (0, "PCUBE-SE-MIB", "spvIndex"), (0, "CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterIndex"))
if mibBuilder.loadTexts: subscriberServiceUsageEntry.setStatus('current')
subscriberServiceUsageUpVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 1), Counter32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberServiceUsageUpVolume.setStatus('current')
subscriberServiceUsageDownVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 2), Counter32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberServiceUsageDownVolume.setStatus('current')
subscriberServiceUsageNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberServiceUsageNumSessions.setStatus('current')
subscriberServiceUsageDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberServiceUsageDuration.setStatus('current')
globalScopeServiceCounterTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1), )
if mibBuilder.loadTexts: globalScopeServiceCounterTable.setStatus('current')
globalScopeServiceCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1), ).setIndexNames((0, "PCUBE-SE-MIB", "pmoduleIndex"), (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"))
if mibBuilder.loadTexts: globalScopeServiceCounterEntry.setStatus('current')
globalScopeServiceCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: globalScopeServiceCounterIndex.setStatus('current')
globalScopeServiceCounterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalScopeServiceCounterStatus.setStatus('current')
globalScopeServiceCounterName = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalScopeServiceCounterName.setStatus('current')
subscriberScopeServiceCounterTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2), )
if mibBuilder.loadTexts: subscriberScopeServiceCounterTable.setStatus('current')
subscriberScopeServiceCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1), ).setIndexNames((0, "PCUBE-SE-MIB", "pmoduleIndex"), (0, "CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterIndex"))
if mibBuilder.loadTexts: subscriberScopeServiceCounterEntry.setStatus('current')
subscriberScopeServiceCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: subscriberScopeServiceCounterIndex.setStatus('current')
subscriberScopeServiceCounterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberScopeServiceCounterStatus.setStatus('current')
subscriberScopeServiceCounterName = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subscriberScopeServiceCounterName.setStatus('current')
pcubeEngageCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 2, 1)).setObjects(("CISCO-SCAS-BB-MIB", "pcubeLinkGroup"), ("CISCO-SCAS-BB-MIB", "pcubePackageGroup"), ("CISCO-SCAS-BB-MIB", "pcubeSubscriberGroup"), ("CISCO-SCAS-BB-MIB", "pcubeServiceCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeEngageCompliance = pcubeEngageCompliance.setStatus('current')
pcubeLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 2)).setObjects(("CISCO-SCAS-BB-MIB", "linkServiceUsageUpVolume"), ("CISCO-SCAS-BB-MIB", "linkServiceUsageDownVolume"), ("CISCO-SCAS-BB-MIB", "linkServiceUsageNumSessions"), ("CISCO-SCAS-BB-MIB", "linkServiceUsageDuration"), ("CISCO-SCAS-BB-MIB", "linkServiceUsageConcurrentSessions"), ("CISCO-SCAS-BB-MIB", "linkServiceUsageActiveSubscribers"), ("CISCO-SCAS-BB-MIB", "linkServiceUpDroppedPackets"), ("CISCO-SCAS-BB-MIB", "linkServiceDownDroppedPackets"), ("CISCO-SCAS-BB-MIB", "linkServiceUpDroppedBytes"), ("CISCO-SCAS-BB-MIB", "linkServiceDownDroppedBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeLinkGroup = pcubeLinkGroup.setStatus('current')
pcubePackageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 3)).setObjects(("CISCO-SCAS-BB-MIB", "packageCounterStatus"), ("CISCO-SCAS-BB-MIB", "packageCounterName"), ("CISCO-SCAS-BB-MIB", "packageCounterActiveSubscribers"), ("CISCO-SCAS-BB-MIB", "packageServiceUsageUpVolume"), ("CISCO-SCAS-BB-MIB", "packageServiceUsageDownVolume"), ("CISCO-SCAS-BB-MIB", "packageServiceUsageNumSessions"), ("CISCO-SCAS-BB-MIB", "packageServiceUsageDuration"), ("CISCO-SCAS-BB-MIB", "packageServiceUsageConcurrentSessions"), ("CISCO-SCAS-BB-MIB", "packageServiceUsageActiveSubscribers"), ("CISCO-SCAS-BB-MIB", "packageServiceUpDroppedPackets"), ("CISCO-SCAS-BB-MIB", "packageServiceDownDroppedPackets"), ("CISCO-SCAS-BB-MIB", "packageServiceUpDroppedBytes"), ("CISCO-SCAS-BB-MIB", "packageServiceDownDroppedBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubePackageGroup = pcubePackageGroup.setStatus('current')
pcubeSubscriberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 4)).setObjects(("CISCO-SCAS-BB-MIB", "subscriberPackageIndex"), ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageUpVolume"), ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageDownVolume"), ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageNumSessions"), ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeSubscriberGroup = pcubeSubscriberGroup.setStatus('current')
pcubeServiceCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 5)).setObjects(("CISCO-SCAS-BB-MIB", "globalScopeServiceCounterStatus"), ("CISCO-SCAS-BB-MIB", "globalScopeServiceCounterName"), ("CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterStatus"), ("CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeServiceCounterGroup = pcubeServiceCounterGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SCAS-BB-MIB", packageCounterStatus=packageCounterStatus, pcubeEngageObjs=pcubeEngageObjs, subscriberGrp=subscriberGrp, subscriberServiceUsageTable=subscriberServiceUsageTable, linkServiceUsageUpVolume=linkServiceUsageUpVolume, subscriberScopeServiceCounterTable=subscriberScopeServiceCounterTable, pcubeSubscriberGroup=pcubeSubscriberGroup, subscriberScopeServiceCounterName=subscriberScopeServiceCounterName, linkServiceUsageNumSessions=linkServiceUsageNumSessions, packageCounterEntry=packageCounterEntry, packageServiceUsageNumSessions=packageServiceUsageNumSessions, packageServiceUsageActiveSubscribers=packageServiceUsageActiveSubscribers, subscriberScopeServiceCounterStatus=subscriberScopeServiceCounterStatus, packageServiceUpDroppedPackets=packageServiceUpDroppedPackets, packageCounterTable=packageCounterTable, serviceGrp=serviceGrp, linkGrp=linkGrp, linkServiceUpDroppedPackets=linkServiceUpDroppedPackets, linkServiceUpDroppedBytes=linkServiceUpDroppedBytes, subscriberServiceUsageDuration=subscriberServiceUsageDuration, packageServiceDownDroppedPackets=packageServiceDownDroppedPackets, subscriberServiceUsageDownVolume=subscriberServiceUsageDownVolume, linkServiceUsageConcurrentSessions=linkServiceUsageConcurrentSessions, subscriberServiceUsageNumSessions=subscriberServiceUsageNumSessions, linkServiceUsageActiveSubscribers=linkServiceUsageActiveSubscribers, packageServiceUpDroppedBytes=packageServiceUpDroppedBytes, packageGrp=packageGrp, packageServiceUsageEntry=packageServiceUsageEntry, subscriberScopeServiceCounterEntry=subscriberScopeServiceCounterEntry, PYSNMP_MODULE_ID=pcubeEngageMIB, linkServiceUsageTable=linkServiceUsageTable, pcubeEngageGroups=pcubeEngageGroups, linkServiceDownDroppedPackets=linkServiceDownDroppedPackets, linkServiceUsageDuration=linkServiceUsageDuration, globalScopeServiceCounterIndex=globalScopeServiceCounterIndex, packageServiceUsageUpVolume=packageServiceUsageUpVolume, packageServiceUsageDuration=packageServiceUsageDuration, pcubeEngageMIB=pcubeEngageMIB, pcubePackageGroup=pcubePackageGroup, serviceCounterGrp=serviceCounterGrp, subscribersTable=subscribersTable, packageCounterIndex=packageCounterIndex, globalScopeServiceCounterName=globalScopeServiceCounterName, subscriberScopeServiceCounterIndex=subscriberScopeServiceCounterIndex, packageCounterActiveSubscribers=packageCounterActiveSubscribers, subscriberPackageIndex=subscriberPackageIndex, subscribersEntry=subscribersEntry, packageServiceUsageConcurrentSessions=packageServiceUsageConcurrentSessions, packageServiceUsageTable=packageServiceUsageTable, subscriberServiceUsageEntry=subscriberServiceUsageEntry, packageServiceUsageDownVolume=packageServiceUsageDownVolume, subscriberServiceUsageUpVolume=subscriberServiceUsageUpVolume, globalScopeServiceCounterTable=globalScopeServiceCounterTable, pcubeServiceCounterGroup=pcubeServiceCounterGroup, globalScopeServiceCounterEntry=globalScopeServiceCounterEntry, serviceTable=serviceTable, linkServiceUsageEntry=linkServiceUsageEntry, linkServiceUsageDownVolume=linkServiceUsageDownVolume, packageCounterName=packageCounterName, packageServiceDownDroppedBytes=packageServiceDownDroppedBytes, globalScopeServiceCounterStatus=globalScopeServiceCounterStatus, pcubeLinkGroup=pcubeLinkGroup, pcubeEngageConformance=pcubeEngageConformance, pcubeEngageCompliance=pcubeEngageCompliance, pcubeEngageCompliances=pcubeEngageCompliances, linkServiceDownDroppedBytes=linkServiceDownDroppedBytes)
