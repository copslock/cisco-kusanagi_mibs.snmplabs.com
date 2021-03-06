#
# PySNMP MIB module CYCLADES-ACS-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYCLADES-ACS-PM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
cyACSMgmt, = mibBuilder.importSymbols("CYCLADES-ACS-MIB", "cyACSMgmt")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, NotificationType, ObjectIdentity, MibIdentifier, Integer32, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter64, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter64", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyPM = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 5))
cyPM.setRevisions(('2005-08-29 00:00', '2003-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cyPM.setRevisionsDescriptions(('Changed the Contact-Info', 'First Draft',))
if mibBuilder.loadTexts: cyPM.setLastUpdated('200508290000Z')
if mibBuilder.loadTexts: cyPM.setOrganization('Cyclades Corporation')
if mibBuilder.loadTexts: cyPM.setContactInfo('postal : Cyclades Corporation 3541 Gateway Boulevard Fremont, CA 94538, USA e-mail : Technical Support support@cyclades.com')
if mibBuilder.loadTexts: cyPM.setDescription('This module defines objects of the Proxy for PM ')
cyNumberOfPM = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyNumberOfPM.setStatus('current')
if mibBuilder.loadTexts: cyNumberOfPM.setDescription("The total number of PM's connected on the unit")
cyPMTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2), )
if mibBuilder.loadTexts: cyPMTable.setStatus('current')
if mibBuilder.loadTexts: cyPMTable.setDescription('Allows to read information about each connected PM')
cyPMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1), ).setIndexNames((0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"))
if mibBuilder.loadTexts: cyPMEntry.setStatus('current')
if mibBuilder.loadTexts: cyPMEntry.setDescription('Information about the connected PM')
cyPMSerialPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMSerialPortNumber.setStatus('current')
if mibBuilder.loadTexts: cyPMSerialPortNumber.setDescription('The number of the serial port when the PM is connected.')
cyPMNumberOutlets = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMNumberOutlets.setStatus('current')
if mibBuilder.loadTexts: cyPMNumberOutlets.setDescription('Number of outlets.')
cyPMNumberUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMNumberUnits.setStatus('current')
if mibBuilder.loadTexts: cyPMNumberUnits.setDescription('Total number of PM unists that are accessed by this serial port.')
cyPMCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMCurrent.setStatus('current')
if mibBuilder.loadTexts: cyPMCurrent.setDescription('Current reading for the PM.')
cyPMVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMVersion.setStatus('current')
if mibBuilder.loadTexts: cyPMVersion.setDescription('The software version of the PM.')
cyPMTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMTemperature.setStatus('current')
if mibBuilder.loadTexts: cyPMTemperature.setDescription('The PM temperature.')
cyPMCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyPMCommand.setStatus('current')
if mibBuilder.loadTexts: cyPMCommand.setDescription("A character string for the user to send commands to PM. He can use it to does the save command. Or to list the outlets that need to be turned off, or turned on , or cycled or locked or unlocked as a group. The command is the first word and is followed by a space and the outlet list (otulets commands). Valid commands are 'on', 'off', 'cycle', 'lock', 'unlock', 'save'.")
cyPMUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3), )
if mibBuilder.loadTexts: cyPMUnitTable.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitTable.setDescription('Allow operations on specific PM unit connected')
cyPMUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1), ).setIndexNames((0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"), (0, "CYCLADES-ACS-PM-MIB", "cyPMUnitNumber"))
if mibBuilder.loadTexts: cyPMUnitEntry.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitEntry.setDescription('Allow operations on outlet')
cyPMUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cyPMUnitNumber.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitNumber.setDescription('The number of the PM unit in the daisy-chained mode.')
cyPMUnitVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitVersion.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitVersion.setDescription('The software version of this PM unit.')
cyPMUnitOutlets = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitOutlets.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitOutlets.setDescription('Number of outlets of this PM unit.')
cyPMUnitFirstOutlet = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitFirstOutlet.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitFirstOutlet.setDescription('Number of the first outlet of this PM unit.')
cyPMUnitCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitCurrent.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitCurrent.setDescription('Current of this PM unit in AMP. The value of this object is the actual current in AMP * 10. You need to translate the readed value (Ex. : value is 5, the current is 0.5 AMP.)')
cyPMUnitMaxCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitMaxCurrent.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitMaxCurrent.setDescription('Maximum current of this PM unit in AMP. The value of this object is the maximum current in AMP * 10. You need to translate the readed value (Ex. : value is 5, the maximum current is 0.5 AMP.)')
cyPMUnitTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitTemperature.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitTemperature.setDescription('Temperature of this PM unit in Celsius degrees. The value of this object is the actual temperature in degrees C * 10. You need to translate the readed value (Ex. : value is 240, the temperature is 24 Celsius.) If the temperature measurement is not installed this value will be 0. Valid values are 5 to 999 ( 0.5 to 99.9 Celsius).')
cyPMUnitMaxTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyPMUnitMaxTemperature.setStatus('current')
if mibBuilder.loadTexts: cyPMUnitMaxTemperature.setDescription('Maximum temperature value of this PM unit in Celsius degrees. The value of this object is the maximum temperature in degrees C * 10. You need to translate the readed value(Ex. : value is 240, the maximum temperature is 24 Celsius). If the temperature measurement is not installed this value will be 0. Valid values are 5 to 999 ( 0.5 to 99.9 Celsius).')
cyOutletTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4), )
if mibBuilder.loadTexts: cyOutletTable.setStatus('current')
if mibBuilder.loadTexts: cyOutletTable.setDescription('Allow operations on outlet')
cyOutletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1), ).setIndexNames((0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"), (0, "CYCLADES-ACS-PM-MIB", "cyOutletNumber"))
if mibBuilder.loadTexts: cyOutletEntry.setStatus('current')
if mibBuilder.loadTexts: cyOutletEntry.setDescription('Allow operations on outlet')
cyOutletNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cyOutletNumber.setStatus('current')
if mibBuilder.loadTexts: cyOutletNumber.setDescription('The outlet number on the PM. Zero is ALL outlets.')
cyOutletName = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletName.setStatus('current')
if mibBuilder.loadTexts: cyOutletName.setDescription('The name given to a particular outlet Maximum size is 8 characters.')
cyOutletServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyOutletServer.setStatus('current')
if mibBuilder.loadTexts: cyOutletServer.setDescription('Alias of the Server connected to this outlet .')
cyOutletPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cycle", 2), ("unknow", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletPower.setStatus('current')
if mibBuilder.loadTexts: cyOutletPower.setDescription('Getting this object will return the power state of the outlet. Valid return states are UNKNOW, OFF and ON. Setting this object will change the power state of the outlet.')
cyOutletLock = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unlock", 0), ("lock", 1), ("unknow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletLock.setStatus('current')
if mibBuilder.loadTexts: cyOutletLock.setDescription('Getting this object will return the lock state of the outlet. Setting this object will change the lock state of the outlet.')
cyOutletPUInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletPUInterval.setStatus('current')
if mibBuilder.loadTexts: cyOutletPUInterval.setDescription('The power unit interval of this outlet in seconds. The value of this object is the actual interval in seconds * 10. You need to translate the readed value (Ex. : value is 5, the interval is 0.5 seconds.)')
mibBuilder.exportSymbols("CYCLADES-ACS-PM-MIB", cyPMUnitTemperature=cyPMUnitTemperature, cyPMUnitEntry=cyPMUnitEntry, cyPMNumberOutlets=cyPMNumberOutlets, PYSNMP_MODULE_ID=cyPM, cyPMCommand=cyPMCommand, cyOutletName=cyOutletName, cyOutletPUInterval=cyOutletPUInterval, cyOutletLock=cyOutletLock, cyOutletTable=cyOutletTable, cyPMUnitFirstOutlet=cyPMUnitFirstOutlet, cyPM=cyPM, cyPMUnitTable=cyPMUnitTable, cyPMUnitCurrent=cyPMUnitCurrent, cyPMNumberUnits=cyPMNumberUnits, cyPMTable=cyPMTable, cyOutletServer=cyOutletServer, cyPMUnitOutlets=cyPMUnitOutlets, cyOutletEntry=cyOutletEntry, cyNumberOfPM=cyNumberOfPM, cyPMCurrent=cyPMCurrent, cyPMUnitMaxCurrent=cyPMUnitMaxCurrent, cyPMVersion=cyPMVersion, cyPMUnitMaxTemperature=cyPMUnitMaxTemperature, cyOutletPower=cyOutletPower, cyPMSerialPortNumber=cyPMSerialPortNumber, cyPMUnitVersion=cyPMUnitVersion, cyPMEntry=cyPMEntry, cyOutletNumber=cyOutletNumber, cyPMUnitNumber=cyPMUnitNumber, cyPMTemperature=cyPMTemperature)
