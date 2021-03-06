#
# PySNMP MIB module CISCO-ENTITY-SENSOR-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-SENSOR-HISTORY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
EntitySensorValue, = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, Gauge32, NotificationType, Bits, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Counter32, IpAddress, iso, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "NotificationType", "Bits", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Counter32", "IpAddress", "iso", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
ciscoEntitySensorHistoryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 768))
ciscoEntitySensorHistoryMIB.setRevisions(('2011-03-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntitySensorHistoryMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntitySensorHistoryMIB.setLastUpdated('201103040000Z')
if mibBuilder.loadTexts: ciscoEntitySensorHistoryMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntitySensorHistoryMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntitySensorHistoryMIB.setDescription('This MIB module defines objects that describe collections and measurement information for each sensor supporting historical data collection. The sensor measurement either represents a measured value or a SMA (Simple Moving Average) value for a specified interval rate over a period of time. This MIB module defines two tables relating to sensor measured value, including: o ceshCollectionTable - contains data describing a collection of historic data for a sensor. o ceshCollectionIntervalTable - contains zero or more rows containing historic data for a sensor The figure below illustrates the relationship between these two tables. +----------------------------------------------+ | ceshCollectionTable | | +------------------------------------------+ | | | ceshCollectionEntry | | | | entPhysicalIndex = 3 | | | | ceshCollectionIntervalTime = 60 | | | | ceshCollectionIntervals = 60 | | | | ceshCollectionInvalidIntervals = 0 |-----+ | | ceshCollectionMaxIntervals = 60 | | | | | ceshCollectionElapsedTime = 20 | | | | | ceshCollectionAlgorithm = 3 | | | | +------------------------------------------+ | | | +------------------------------------------+ | | | | ceshCollectionEntry | | | | | entPhysicalIndex = 3 | | | | | ceshCollectionIntervalTime = 3660 | | | | | ceshCollectionIntervals = 2 |------------+ | | ceshCollectionInvalidIntervals = 0 | | | | | | ceshCollectionMaxIntervals = 60 | | | | | | ceshCollectionElapsedTime = 20 | | | | | | ceshCollectionAlgorithm = 4 | | | | | +------------------------------------------+ | | | +----------------------------------------------+ | | | | +----------------------------------------------+ | | | ceshCollectionIntervalTable | | | | +------------------------------------------+ | | | | | ceshCollectionIntervalEntry | | | | | | entPhysicalIndex = 3 |<----+ | | | ceshCollectionIntervalTime = 60 | | | | | | ceshCollectionIntervalNumber = 1 | | | | | | ceshCollectionIntervalSensorValue = 54 | | | | | | ceshCollectionIntervalTimeStamp = 1 | | | | | +------------------------------------------+ | | | | .................... <----+ | | skipped 58 entries <----+ | | .................... <----+ | | | | | | +------------------------------------------+ | | | | | ceshCollectionIntervalEntry | | | | | | entPhysicalIndex = 3 |<----+ | | | ceshCollectionIntervalTime = 60 | | | | | ceshCollectionIntervalNumber = 60 | | | | | ceshCollectionIntervalSensorValue = 54 | | | | | ceshCollectionIntervalTimeStamp = 60 | | | | +------------------------------------------+ | | | | | | +------------------------------------------+ | | | | ceshCollectionIntervalEntry | | | | | entPhysicalIndex = 3 |<-----------+ | | ceshCollectionIntervalTime = 3660 | | | | ceshCollectionIntervalNumber = 1 | | | | ceshCollectionIntervalSensorValue = 54 | | | | ceshCollectionIntervalTimeStamp = 60 | | | +------------------------------------------+ | +----------------------------------------------+ If the system samples a sensor every minute for one collection and every hour for another, then the ceshCollectionTable contains two entries describing the two collections.')
class SensorHistoryCollectionAlgorithm(TextualConvention, Integer32):
    description = "This textual convention denotes an enumerated integer-value that describing the method used to collect historic data for a sensor. 'other' - The implementation of the MIB module using this textual convention does not recognize the historic data collection algorithm. 'unknown' - The system is not able to ascertain the historic data collection algorithm. 'measured' - A raw value. 'simpleAverage' - The system collects a simple moving average of the values sampled from the sensor."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("measured", 3), ("algoSMA", 4))

ciscoEntitySensorHistoryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 0))
ciscoEntitySensorHistoryMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 1))
ceshCollectionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1), )
if mibBuilder.loadTexts: ceshCollectionTable.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionTable.setDescription('This table lists each collection of historic data maintained by the system for each supported sensor. This table has an expansion dependent relationship on the ceshCollectionIntervalTable, containing zero or more rows for each corresponding collection.')
ceshCollectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTime"))
if mibBuilder.loadTexts: ceshCollectionEntry.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionEntry.setDescription('Each entry in the ceshCollectionTable contains collection attributes describing the collection. For each supported sensor, the system creates a row for each prescribed collection. This creation process happens at startup and following the insertion of a FRU containing sensors. The system destroys a row when it destroys the corresponding row in the entPhysicalTable, which can happen as the result of the removal of the FRU containing the sensor.')
ceshCollectionIntervalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('seconds')
if mibBuilder.loadTexts: ceshCollectionIntervalTime.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervalTime.setDescription('This object indicates the length of the sampling interval for the collection.')
ceshCollectionIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 2), Gauge32()).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionIntervals.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervals.setDescription('This object indicates the number of intervals for which data has been collected.')
ceshCollectionInvalidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 3), Gauge32()).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionInvalidIntervals.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionInvalidIntervals.setDescription("This object indicates the number of intervals in the range of '0' to the value of the corresponding instance of ceshCollectionIntervals, for which no data is available. The value of this column will typically be '0', except in certain circumstances when some intervals are not available.")
ceshCollectionMaxIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionMaxIntervals.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionMaxIntervals.setDescription('This object indicates the maximum number of intervals maintained for the collection.')
ceshCollectionElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 5), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionElapsedTime.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionElapsedTime.setDescription('This object indicates the time that has elapsed since the beginning of the current interval.')
ceshCollectionAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 1, 1, 6), SensorHistoryCollectionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionAlgorithm.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionAlgorithm.setDescription('This object indicates the algorithm used in collecting historic data from the corresponding sensor.')
ceshCollectionIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2), )
if mibBuilder.loadTexts: ceshCollectionIntervalTable.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervalTable.setDescription('This table contains the historic data for each collection maintained by the system. This table has an expansion dependent relationship on the ceshCollectionTable, containing zero or more rows for each corresponding collection.')
ceshCollectionIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTime"), (0, "CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalNumber"))
if mibBuilder.loadTexts: ceshCollectionIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervalEntry.setDescription('An entry describes the data collected for an interval. The system creates a row in the ceshCollectionIntervalTable after it has sampled a sample for a given collection. The maximum allowable entries for a collection should be less than or equal to the value specified by ceshCollectionMaxIntervals instance. Once number of entries is equal to ceshCollectionMaxIntervals, then the system destroys the lease recent row from the collection before creating a new one. An agent destroys all conceptual entries corresponding to a physical entity upon removal of the physical entity.')
ceshCollectionIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ceshCollectionIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervalNumber.setDescription("This object indicates the interval number identifying the interval. The interval identified by the value '1' represents the most recent interval, and the interval identified by the value (n) represents the interval immediately preceding the interval identified by the value (n-1).")
ceshCollectionIntervalSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionIntervalSensorValue.setReference('RFC3433')
if mibBuilder.loadTexts: ceshCollectionIntervalSensorValue.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervalSensorValue.setDescription("This object indicates the sensor value for the corresponding physical entity during the interval. To correctly display or interpret this variable's value, you must also know the sensor's type, scale, and precision indicated by the corresponding entry in the entPhySensorTable (defined by the ENTITY-SENSOR-MIB) or entSensorValueTable (defined by the CISCO-ENTITY-SENSOR-MIB).")
ceshCollectionIntervalTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 768, 0, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceshCollectionIntervalTimeStamp.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervalTimeStamp.setDescription('This object indicates the value of sysUpTime when the system sampled the corresponding sensor.')
ciscoEntitySensorHistoryMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 1))
ciscoEntitySensorHistoryMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2))
ciscoEntitySensorHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionGroup"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntitySensorHistoryCompliance = ciscoEntitySensorHistoryCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoEntitySensorHistoryCompliance.setDescription('Describes the requirements for conformance to the Entity Sensor History Collection MIB module.')
ceshCollectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionElapsedTime"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervals"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionInvalidIntervals"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionAlgorithm"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionMaxIntervals"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceshCollectionGroup = ceshCollectionGroup.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionGroup.setDescription('This group contains collection of attribute objects related to entity sensor history collection')
ceshCollectionIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 768, 1, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalTimeStamp"), ("CISCO-ENTITY-SENSOR-HISTORY-MIB", "ceshCollectionIntervalSensorValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceshCollectionIntervalGroup = ceshCollectionIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: ceshCollectionIntervalGroup.setDescription('This group contains collection of interval objects related to entity sensor history collection')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-HISTORY-MIB", ciscoEntitySensorHistoryMIB=ciscoEntitySensorHistoryMIB, ciscoEntitySensorHistoryMIBObjects=ciscoEntitySensorHistoryMIBObjects, ceshCollectionIntervalTable=ceshCollectionIntervalTable, ceshCollectionIntervals=ceshCollectionIntervals, ceshCollectionTable=ceshCollectionTable, SensorHistoryCollectionAlgorithm=SensorHistoryCollectionAlgorithm, ciscoEntitySensorHistoryCompliance=ciscoEntitySensorHistoryCompliance, ceshCollectionElapsedTime=ceshCollectionElapsedTime, ceshCollectionIntervalTimeStamp=ceshCollectionIntervalTimeStamp, ceshCollectionIntervalSensorValue=ceshCollectionIntervalSensorValue, ciscoEntitySensorHistoryMIBGroups=ciscoEntitySensorHistoryMIBGroups, ceshCollectionAlgorithm=ceshCollectionAlgorithm, ciscoEntitySensorHistoryMIBCompliances=ciscoEntitySensorHistoryMIBCompliances, ceshCollectionGroup=ceshCollectionGroup, ceshCollectionIntervalNumber=ceshCollectionIntervalNumber, ceshCollectionInvalidIntervals=ceshCollectionInvalidIntervals, ceshCollectionIntervalTime=ceshCollectionIntervalTime, ciscoEntitySensorHistoryMIBConform=ciscoEntitySensorHistoryMIBConform, ceshCollectionIntervalGroup=ceshCollectionIntervalGroup, PYSNMP_MODULE_ID=ciscoEntitySensorHistoryMIB, ceshCollectionMaxIntervals=ceshCollectionMaxIntervals, ceshCollectionEntry=ceshCollectionEntry, ceshCollectionIntervalEntry=ceshCollectionIntervalEntry)
