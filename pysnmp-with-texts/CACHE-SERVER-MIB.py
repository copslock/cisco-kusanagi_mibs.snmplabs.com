#
# PySNMP MIB module CACHE-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CACHE-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:44:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, Integer32, enterprises, TimeTicks, NotificationType, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter32, iso, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Integer32", "enterprises", "TimeTicks", "NotificationType", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter32", "iso", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibmCacheServer = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8))
ibmcacheserverCore = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 1))
ibmcacheserverPartition = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2))
ibmcacheserverURL = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3))
ibmcacheserverProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4))
ibmcacheserverCoreActivePartitions = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverCoreActivePartitions.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverCoreActivePartitions.setDescription('Number of active partitions.')
ibmcacheserverCoreECCPort = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverCoreECCPort.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverCoreECCPort.setDescription('The ECC port number.')
ibmcacheserverPartitionTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1), )
if mibBuilder.loadTexts: ibmcacheserverPartitionTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionTable.setDescription('Table of information pertaining to an individual partition.')
ibmcacheserverPartitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1), ).setIndexNames((0, "CACHE-SERVER-MIB", "ibmcacheserverPartitionIndex"))
if mibBuilder.loadTexts: ibmcacheserverPartitionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionEntry.setDescription('An entry containing objects for a particular partition.')
ibmcacheserverPartitionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ibmcacheserverPartitionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionIndex.setDescription('A unique value for each partition.')
ibmcacheserverPartitionCacheControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheControl.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheControl.setDescription('Global cache control.')
ibmcacheserverPartitionCacheTransparent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheTransparent.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheTransparent.setDescription('Transparent cache control.')
ibmcacheserverPartitionUseHTTPCacheHdrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionUseHTTPCacheHdrs.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionUseHTTPCacheHdrs.setDescription('Use HTTP cache control directive')
ibmcacheserverPartitionCacheDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheDynamic.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheDynamic.setDescription('Cache dynamic items (e.g. - /cgi-bin/) control')
ibmcacheserverPartitionCacheDynamicURL = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheDynamicURL.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheDynamicURL.setDescription('Cache dynamic items URL')
ibmcacheserverPartitionCacheImage = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheImage.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheImage.setDescription('Cache image items (.gif, .jpg) control')
ibmcacheserverPartitionCacheStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheStatic.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionCacheStatic.setDescription('Cache static items control')
ibmcacheserverPartitionMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionMaxSize.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionMaxSize.setDescription('Maximum partition size in MegaBytes')
ibmcacheserverPartitionMaxObjects = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionMaxObjects.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionMaxObjects.setDescription('Max number of objects in partition')
ibmcacheserverPartitionMaxObjectSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionMaxObjectSize.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionMaxObjectSize.setDescription('Max size of object allowed in partition')
ibmcacheserverPartitionDynamicDefaultLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionDynamicDefaultLifetime.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionDynamicDefaultLifetime.setDescription('Default lifetime for dynamic items')
ibmcacheserverPartitionImageDefaultLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionImageDefaultLifetime.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionImageDefaultLifetime.setDescription('Default lifetime for image items')
ibmcacheserverPartitionStaticDefaultLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionStaticDefaultLifetime.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionStaticDefaultLifetime.setDescription('Default lifetime for static items')
ibmcacheserverPartitionCachePurgeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionCachePurgeInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionCachePurgeInterval.setDescription('Time between garbage collection')
ibmcacheserverPartitionNumBytesCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNumBytesCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNumBytesCurrent.setDescription('Current number of bytes in partition')
ibmcacheserverPartitionNumBytesHiWater = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNumBytesHiWater.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNumBytesHiWater.setDescription('High water mark for number of bytes in partition')
ibmcacheserverPartitionNumObjectsCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNumObjectsCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNumObjectsCurrent.setDescription('Current number of objects in partition')
ibmcacheserverPartitionNumObjectsHiWater = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNumObjectsHiWater.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNumObjectsHiWater.setDescription('High water mark for number of objects in partition')
ibmcacheserverPartitionHitTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionHitTotal.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionHitTotal.setDescription('Total number of cache retrieval attempts in which item found in cache')
ibmcacheserverPartitionMissTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionMissTotal.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionMissTotal.setDescription('Total number of cache retrieval attempts in which item not found in cache')
ibmcacheserverPartitionAddInclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionAddInclude.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionAddInclude.setDescription('Items added explicitly via INCLUDE')
ibmcacheserverPartitionNotAddCacheOff = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddCacheOff.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddCacheOff.setDescription('Items not added to partition due to caching turned off')
ibmcacheserverPartitionNotAddTooLarge = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddTooLarge.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddTooLarge.setDescription('Items not added to partition due to item larger than max allowed')
ibmcacheserverPartitionNotAddHTTPHdr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddHTTPHdr.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddHTTPHdr.setDescription('Items not added to partition due to HTTP header specifying DO NOT CACHE')
ibmcacheserverPartitionNotAddExclude = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddExclude.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddExclude.setDescription('Items not added to partition due to item URL explicitly excluded')
ibmcacheserverPartitionNotAddExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddExpire.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddExpire.setDescription('Items not added to partition due to item already expired')
ibmcacheserverPartitionNotAddImage = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddImage.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddImage.setDescription('Items not added to partition due to image items explicitly not cached')
ibmcacheserverPartitionNotAddStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddStatic.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddStatic.setDescription('Items not added to partition due to static items explicitly not cached')
ibmcacheserverPartitionNotAddDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddDynamic.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionNotAddDynamic.setDescription('Items not added to partition due to dynamic items explicitly not cached')
ibmcacheserverPartitionPurgeCacheFull = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionPurgeCacheFull.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionPurgeCacheFull.setDescription('Items deleted from partition due to cache full')
ibmcacheserverPartitionPurgeItemStale = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionPurgeItemStale.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionPurgeItemStale.setDescription('Items deleted from partition due to item stale since expire time reached')
ibmcacheserverPartitionPurgeItemExplicit = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 2, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverPartitionPurgeItemExplicit.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverPartitionPurgeItemExplicit.setDescription('Items deleted from partition due to request for deletion')
ibmcacheserverURLTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1), )
if mibBuilder.loadTexts: ibmcacheserverURLTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverURLTable.setDescription('Table of information pertaining to cache policies (URLs)')
ibmcacheserverURLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1), ).setIndexNames((0, "CACHE-SERVER-MIB", "ibmcacheserverPartitionIndex"), (0, "CACHE-SERVER-MIB", "ibmcacheserverURLIndex"))
if mibBuilder.loadTexts: ibmcacheserverURLEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverURLEntry.setDescription('An entry containing objects for a particular cache policy (URLs)')
ibmcacheserverURLIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ibmcacheserverURLIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverURLIndex.setDescription('A unique value for each URL related to a particular partition. In this implementation, this index is a data structure pointer and therefore, may appear a bit odd looking. However, it is a valid, unique index value.')
ibmcacheserverURLContent = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverURLContent.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverURLContent.setDescription('Indication of whether URL is to be cached or excluded.')
ibmcacheserverURLMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverURLMask.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverURLMask.setDescription('URL string for this policy')
ibmcacheserverProxyTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1), )
if mibBuilder.loadTexts: ibmcacheserverProxyTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyTable.setDescription('Table of information pertaining to HTTP proxy support')
ibmcacheserverProxyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1), ).setIndexNames((0, "CACHE-SERVER-MIB", "ibmcacheserverProxyClusterAddr"), (0, "CACHE-SERVER-MIB", "ibmcacheserverProxyPort"))
if mibBuilder.loadTexts: ibmcacheserverProxyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyEntry.setDescription('An entry containing objects for a particular HTTP proxy socket')
ibmcacheserverProxyClusterAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: ibmcacheserverProxyClusterAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyClusterAddr.setDescription('Cluster IP address')
ibmcacheserverProxyPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ibmcacheserverProxyPort.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyPort.setDescription('Cluster IP port number')
ibmcacheserverProxyPartition = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyPartition.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyPartition.setDescription('The partition identifier that this HTTP proxy is related to.')
ibmcacheserverProxyClientCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyClientCount.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyClientCount.setDescription('Current number of TCP connections to clients')
ibmcacheserverProxyServerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyServerCount.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyServerCount.setDescription('Current number of TCP connections to servers')
ibmcacheserverProxyClientMaxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyClientMaxCount.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyClientMaxCount.setDescription('Highwater max number of TCP connections to clients')
ibmcacheserverProxyServerMaxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyServerMaxCount.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyServerMaxCount.setDescription('Highwater max number of TCP connections to servers')
ibmcacheserverProxyCacheHits = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyCacheHits.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyCacheHits.setDescription('Number of cache hits for this proxy')
ibmcacheserverProxyCacheMissMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissMethod.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissMethod.setDescription('Cache miss for this proxy due to method not being GET or HEAD.')
ibmcacheserverProxyCacheMissStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissStorage.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissStorage.setDescription('Cache miss for this proxy due to lack of storage to generate a response.')
ibmcacheserverProxyCacheMissNotInCache = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissNotInCache.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissNotInCache.setDescription('Cache miss for this proxy due to not being in cache.')
ibmcacheserverProxyCacheMissHeaders = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 8, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissHeaders.setStatus('mandatory')
if mibBuilder.loadTexts: ibmcacheserverProxyCacheMissHeaders.setDescription('Cache miss for this proxy due to headers on request cache not being used.')
mibBuilder.exportSymbols("CACHE-SERVER-MIB", ibmcacheserverPartitionPurgeItemStale=ibmcacheserverPartitionPurgeItemStale, ibmcacheserverProxyCacheMissMethod=ibmcacheserverProxyCacheMissMethod, ibmcacheserverPartitionNumObjectsCurrent=ibmcacheserverPartitionNumObjectsCurrent, ibmcacheserverPartitionCacheDynamicURL=ibmcacheserverPartitionCacheDynamicURL, ibmcacheserverPartitionNotAddExclude=ibmcacheserverPartitionNotAddExclude, ibmcacheserverProxyTable=ibmcacheserverProxyTable, ibmcacheserverCoreActivePartitions=ibmcacheserverCoreActivePartitions, ibmcacheserverPartitionCacheControl=ibmcacheserverPartitionCacheControl, ibmcacheserverProxyPartition=ibmcacheserverProxyPartition, ibmcacheserverProxyCacheMissNotInCache=ibmcacheserverProxyCacheMissNotInCache, ibmcacheserverPartitionTable=ibmcacheserverPartitionTable, ibmcacheserverPartitionMaxObjects=ibmcacheserverPartitionMaxObjects, ibmcacheserverPartitionNotAddStatic=ibmcacheserverPartitionNotAddStatic, ibmcacheserverPartitionCacheDynamic=ibmcacheserverPartitionCacheDynamic, ibmcacheserverCoreECCPort=ibmcacheserverCoreECCPort, ibmcacheserverProxyEntry=ibmcacheserverProxyEntry, ibmcacheserverProxyClientMaxCount=ibmcacheserverProxyClientMaxCount, ibmcacheserverProxyServerCount=ibmcacheserverProxyServerCount, ibmcacheserverPartitionCachePurgeInterval=ibmcacheserverPartitionCachePurgeInterval, ibmcacheserverPartitionHitTotal=ibmcacheserverPartitionHitTotal, ibmcacheserverPartitionCacheStatic=ibmcacheserverPartitionCacheStatic, ibmcacheserverPartitionCacheImage=ibmcacheserverPartitionCacheImage, ibmcacheserverPartitionImageDefaultLifetime=ibmcacheserverPartitionImageDefaultLifetime, ibmcacheserverURLContent=ibmcacheserverURLContent, ibmcacheserverURLMask=ibmcacheserverURLMask, ibmcacheserverPartitionAddInclude=ibmcacheserverPartitionAddInclude, ibmcacheserverProxyPort=ibmcacheserverProxyPort, ibmcacheserverPartitionUseHTTPCacheHdrs=ibmcacheserverPartitionUseHTTPCacheHdrs, ibmcacheserverPartitionPurgeItemExplicit=ibmcacheserverPartitionPurgeItemExplicit, ibmcacheserverPartitionNumObjectsHiWater=ibmcacheserverPartitionNumObjectsHiWater, ibmcacheserverPartitionMaxObjectSize=ibmcacheserverPartitionMaxObjectSize, ibmcacheserverProxyClusterAddr=ibmcacheserverProxyClusterAddr, ibmcacheserverURLEntry=ibmcacheserverURLEntry, ibmcacheserverPartitionNotAddTooLarge=ibmcacheserverPartitionNotAddTooLarge, ibmcacheserverProxyServerMaxCount=ibmcacheserverProxyServerMaxCount, ibmcacheserverPartitionMaxSize=ibmcacheserverPartitionMaxSize, ibmcacheserverPartitionNotAddImage=ibmcacheserverPartitionNotAddImage, ibmcacheserverPartitionEntry=ibmcacheserverPartitionEntry, ibmcacheserverURLIndex=ibmcacheserverURLIndex, ibmcacheserverProxyCacheMissStorage=ibmcacheserverProxyCacheMissStorage, ibmCacheServer=ibmCacheServer, ibmcacheserverPartition=ibmcacheserverPartition, ibmcacheserverPartitionIndex=ibmcacheserverPartitionIndex, ibmcacheserverPartitionNotAddExpire=ibmcacheserverPartitionNotAddExpire, ibmcacheserverPartitionStaticDefaultLifetime=ibmcacheserverPartitionStaticDefaultLifetime, ibmcacheserverPartitionPurgeCacheFull=ibmcacheserverPartitionPurgeCacheFull, ibmcacheserverProxy=ibmcacheserverProxy, ibmcacheserverPartitionNotAddDynamic=ibmcacheserverPartitionNotAddDynamic, ibmcacheserverURL=ibmcacheserverURL, ibmcacheserverURLTable=ibmcacheserverURLTable, ibmcacheserverPartitionMissTotal=ibmcacheserverPartitionMissTotal, ibmcacheserverPartitionNotAddHTTPHdr=ibmcacheserverPartitionNotAddHTTPHdr, ibmcacheserverProxyCacheHits=ibmcacheserverProxyCacheHits, ibmcacheserverPartitionNotAddCacheOff=ibmcacheserverPartitionNotAddCacheOff, ibmcacheserverProxyClientCount=ibmcacheserverProxyClientCount, ibmcacheserverProxyCacheMissHeaders=ibmcacheserverProxyCacheMissHeaders, ibmcacheserverPartitionNumBytesCurrent=ibmcacheserverPartitionNumBytesCurrent, ibmcacheserverPartitionNumBytesHiWater=ibmcacheserverPartitionNumBytesHiWater, ibmcacheserverPartitionCacheTransparent=ibmcacheserverPartitionCacheTransparent, ibmcacheserverCore=ibmcacheserverCore, ibmcacheserverPartitionDynamicDefaultLifetime=ibmcacheserverPartitionDynamicDefaultLifetime)
