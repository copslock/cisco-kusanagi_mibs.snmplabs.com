#
# PySNMP MIB module ENTERASYS-POWER-ETHERNET-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-POWER-ETHERNET-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
pethPsePortEntry, pethMainPseEntry = mibBuilder.importSymbols("POWER-ETHERNET-MIB", "pethPsePortEntry", "pethMainPseEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, ObjectIdentity, Unsigned32, NotificationType, Integer32, Bits, iso, IpAddress, Counter32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "NotificationType", "Integer32", "Bits", "iso", "IpAddress", "Counter32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysPowerEthernetMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50))
etsysPowerEthernetMibExtMIB.setRevisions(('2009-08-27 20:31', '2005-01-10 16:30', '2004-08-17 22:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysPowerEthernetMibExtMIB.setRevisionsDescriptions(('Adding objects to support IEEE Std. 802.3at functionality. Changes to etsysPsePortPowerManagementTable: - Increased max etsysPsePortPowerLimit range to 34000. - Added etsysPsePortCapability, etsysPsePortCapabilitySelect, and etsysPsePortDetectionStatus objects.', 'Added the power management functionality.', 'The initial version of this MIB module',))
if mibBuilder.loadTexts: etsysPowerEthernetMibExtMIB.setLastUpdated('200908272031Z')
if mibBuilder.loadTexts: etsysPowerEthernetMibExtMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysPowerEthernetMibExtMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysPowerEthernetMibExtMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Enterasys Networks enterprise OID pertaining to the allocation of power in a Pse chassis.')
etsysPowerEthernetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1))
etsysPseChassisPowerAllocation = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1))
etsysPseSlotPowerAllocation = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2))
etsysPseChassisPowerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3))
etsysPseSlotPowerManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4))
etsysPsePortPowerManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5))
etsysPsePowerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0))
etsysPseChassisPowerAllocationMode = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseChassisPowerAllocationMode.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerAllocationMode.setDescription('In auto mode, a Pse Power Management Algorithm handles the allocation of power to all the modules. In manual mode, power is manually allocated to the modules via the etsysPseSlotPowerAllocationTable. The value of etsysPseChassisPowerAllocationAvailable is used to determine the power available for allocation in this chassis in both auto and manual mode. Maintaining the value of this object across agent reboots is REQUIRED.')
etsysPseChassisPowerSnmpNotification = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseChassisPowerSnmpNotification.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerSnmpNotification.setDescription('The current state of the SNMP Notification functionality for Pse. enabled (1) - The Pse will generate SNMP Notifications for potentially adverse Pse power conditions. The generation of these notifications are NOT dependant upon the state of etsysPseChassisPowerAllocationMode. disabled (2) - The SNMP Notifications defined in this MIB will NOT be generated under any conditions. Agents are not required to generate SNMP Notifications for conditions that exist when this object is set to enabled. Maintaining the value of this object across agent reboots is REQUIRED.')
etsysPseChassisPowerAvailableMaximum = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseChassisPowerAvailableMaximum.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerAvailableMaximum.setDescription('The maximum percentage of power from the Pse Power Supply that this chassis can use. The default value should be 100 percent, meaning the chassis can use all the power detected from Pse Power Supply. Maintaining the value of this object across agent reboots is REQUIRED.')
etsysPseSlotPowerAllocationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1), )
if mibBuilder.loadTexts: etsysPseSlotPowerAllocationTable.setStatus('current')
if mibBuilder.loadTexts: etsysPseSlotPowerAllocationTable.setDescription('Power allocation management information for all slots.')
etsysPseSlotPowerAllocationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: etsysPseSlotPowerAllocationEntry.setStatus('current')
if mibBuilder.loadTexts: etsysPseSlotPowerAllocationEntry.setDescription('Power allocation management information for an entPhysicalEntry that has an entPhysicalClass of container(5) and represents a slot in the chassis that could be occupied by a Pse module.')
etsysPseSlotPowerMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1, 1), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseSlotPowerMaximum.setStatus('current')
if mibBuilder.loadTexts: etsysPseSlotPowerMaximum.setDescription("The maximum power that can be consumed by the module in this slot, based on the module's characteristics. For slots without Pse modules this object MUST return zero.")
etsysPseSlotPowerAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1, 2), Unsigned32()).setUnits('Watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseSlotPowerAssigned.setStatus('current')
if mibBuilder.loadTexts: etsysPseSlotPowerAssigned.setDescription('The power that will be allocated to this slot in manual mode. In auto mode, this object has no effect. Maintaining the value of this object across agent reboots is REQUIRED.')
etsysPseChassisPowerDetected = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 1), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerDetected.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerDetected.setDescription('The total power detected by the chassis from Pse Power Supply.')
etsysPseChassisPowerAvailable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 2), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerAvailable.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerAvailable.setDescription('The total power available for this chassis. This is ( etsysPseChassisPowerDetected * ( etsysPseChassisPowerAvailableMaximum / 100 ) ).')
etsysPseChassisPowerConsumable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 3), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerConsumable.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerConsumable.setDescription('The total power that could be consumed by all of the Pse modules in the chassis. This is the summation of the values of all of the etsysPseSlotPowerMaximum objects.')
etsysPseChassisPowerAssigned = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 4), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerAssigned.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerAssigned.setDescription('The total power assigned to the slots in the chassis. This is the summation of the values of all of the etsysPseSlotPowerAssigned objects.')
etsysPseChassisPowerRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("redundant", 1), ("notRedundant", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerRedundancy.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerRedundancy.setDescription('Denotes whether or not the Pse power system has redundant capacity.')
etsysPseModulePowerManagementTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1), )
if mibBuilder.loadTexts: etsysPseModulePowerManagementTable.setStatus('current')
if mibBuilder.loadTexts: etsysPseModulePowerManagementTable.setDescription('This table augments the pethMainPseTable of the PowerEthernetMIB (rfc3621). It provides objects that are used to budget power.')
etsysPseModulePowerManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1), )
pethMainPseEntry.registerAugmentions(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerManagementEntry"))
etsysPseModulePowerManagementEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
if mibBuilder.loadTexts: etsysPseModulePowerManagementEntry.setStatus('current')
if mibBuilder.loadTexts: etsysPseModulePowerManagementEntry.setDescription('A set of objects that display, control, and calculate the power consumption of a PSE.')
etsysPseModulePowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("realtime", 1), ("class", 2))).clone('realtime')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseModulePowerMode.setStatus('current')
if mibBuilder.loadTexts: etsysPseModulePowerMode.setDescription('This object controls the power management of the PSE. It also controls how etsysPseModulePowerClassBudget, etsysPseModulePowerUsage and etsysPsePortPowerLimit are utilized. In realtime mode, the power is managed based on the actual power consumption of the ports. etsysPseModulePowerClassBudget is sum of power consumed by all ports, measured in real-time. The etsysPseModulePowerUsage is ratio of pethMainPseConsumptionPower over pethMainPsePower, expressed in percents. In class mode, the power is managed based on the IEEE 802.3af definition of the class upper limit, except classes 0 & 4 for which the actual power consumption is used. etsysPseModulePowerClassBudget is sum of all ports power according to their class upper bound, except classes 0 & 4 for which the actual power consumption is accounted. The etsysPseModulePowerUsage is ratio of etsysPseModulePowerClassBudget over pethMainPsePower, expressed in percents. The effect of etsysPseModulePowerMode to etsysPsePortPowerLimit is described in etsysPsePortPowerLimit definition. Maintaining the value of this object across agent reboots is REQUIRED.')
etsysPseModulePowerClassBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 2), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseModulePowerClassBudget.setStatus('current')
if mibBuilder.loadTexts: etsysPseModulePowerClassBudget.setDescription('In class mode, this is sum of all ports power according to their class upper bound, except classes 0 & 4 for which the actual power consumption is accounted. In realtime mode, this is sum of power consumed by all ports, measured in real-time.')
etsysPseModulePowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseModulePowerUsage.setStatus('current')
if mibBuilder.loadTexts: etsysPseModulePowerUsage.setDescription('In class mode, this is ratio of etsysPseModulePowerClassBudget over pethMainPsePower, expressed in percents. In realtime mode, this is ratio of pethMainPseConsumptionPower over pethMainPsePower, expressed in percents.')
etsysPsePortPowerManagementTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1), )
if mibBuilder.loadTexts: etsysPsePortPowerManagementTable.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortPowerManagementTable.setDescription('This table augments the pethPsePortTable of the PowerEthernetMIB (rfc3621). It provides objects that are used to budget power.')
etsysPsePortPowerManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1), )
pethPsePortEntry.registerAugmentions(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerManagementEntry"))
etsysPsePortPowerManagementEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysPsePortPowerManagementEntry.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortPowerManagementEntry.setDescription('A set of objects that display and control the power consumption of a PSE, at the port level.')
etsysPsePortPowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 34000)).clone(15400)).setUnits('milliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPsePortPowerLimit.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortPowerLimit.setDescription("This object sets the maximum power allowed on this port. If the port exceeds its power limit, it will be shut down. This object has effect only when its module is in realtime mode (specified by etsysPseModulePowerMode). In class mode, the power limit of a port is defined by port's class upper bound, according to the IEEE standard selected in etsysPsePortCapabilitySelect.")
etsysPsePortPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 2), Gauge32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortPowerUsage.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortPowerUsage.setDescription('Actual power consumption measured in real-time.')
etsysPsePortPDType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("legacy", 1), ("ieee8023af", 2), ("other", 3), ("ieee8023", 4), ("ieee8023at", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortPDType.setReference('IEEE Std 802.3af IEEE Std 802.3at')
if mibBuilder.loadTexts: etsysPsePortPDType.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortPDType.setDescription('Describes the detected PD type on this port. A value of legacy(1) - indicates that the PD is using a capacitive signature, which is pre-IEEE standard. A value of ieee8023af(2)- indicates that the PD is using a resistive signature and is compliant with the IEEE Std 802.3af. A value of other(3) - indicates that the PD type could not be determined. A value of ieee8023(4)- indicates that the PD is using a resistive signature and is compliant with the IEEE Std 802.3af and/or IEEE Std 802.3at specifications. A value of ieee8023at(5)- indicates that the PD is using a resistive signature and is compliant with the IEEE Std 802.3at.')
etsysPsePortCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 4), Bits().clone(namedValues=NamedValues(("other", 0), ("ieee8023afCapable", 1), ("ieee8023atCapable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortCapability.setReference('IEEE Std 802.3af IEEE Std 802.3at')
if mibBuilder.loadTexts: etsysPsePortCapability.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortCapability.setDescription('This object indicates the IEEE Power over Ethernet standard this port supports.')
etsysPsePortCapabilitySelect = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ieee8023af", 1), ("ieee8023at", 2))).clone('ieee8023af')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPsePortCapabilitySelect.setReference('IEEE Std 802.3af IEEE Std 802.3at')
if mibBuilder.loadTexts: etsysPsePortCapabilitySelect.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortCapabilitySelect.setDescription("This object sets the port's power management capabilities based on the IEEE standard. ieee8023af (1) : IEEE Std 802.3af ieee8023at (2) : IEEE Std 802.3at Attempting to set this value to a capability that is not supported, as indicated by etsysPsePortCapability, will result in an inconsistentValue error.")
etsysPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 3), ("fault", 4), ("test", 5), ("otherFault", 6), ("requestingPower", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortDetectionStatus.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortDetectionStatus.setDescription("Describes the operational status of the port PD detection. A value of disabled(1)- indicates that the PSE State diagram is in the state DISABLED. A value of deliveringPower(3) - indicates that the PSE State diagram is in the state POWER_ON for a duration greater than tlim max. A value of fault(4) - indicates that the PSE State diagram is in the state TEST_ERROR. A value of test(5) - indicates that the PSE State diagram is in the state TEST_MODE. A value of otherFault(6) - indicates that the PSE State diagram is in the state IDLE due to the variable error_conditions. A value of searching(2)- indicates the PSE State diagram is in a state other than those listed above. A value of requestingPower(7) - indicates the PSE State diagram is in the state IDLE after transitioning from the state POWER_DENIED due to insufficient PSE power being available to satisfy the PD's requirements.")
etsysPsePowerSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6), )
if mibBuilder.loadTexts: etsysPsePowerSupplyStatusTable.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerSupplyStatusTable.setDescription('Status information for all of the Pse power supply modules.')
etsysPsePowerSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1), ).setIndexNames((0, "ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleNumber"))
if mibBuilder.loadTexts: etsysPsePowerSupplyStatusEntry.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerSupplyStatusEntry.setDescription('Status information for an individual Pse power supply module.')
etsysPsePowerSupplyModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleNumber.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleNumber.setDescription("A unique number that identifies the Pse power supply and is relative to the module's physical location.")
etsysPsePowerSupplyModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("infoNotAvailable", 1), ("notInstalled", 2), ("installedAndOperating", 3), ("installedAndNotOperating", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleStatus.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleStatus.setDescription("Denotes the power supply's status.")
etsysPseChassisPowerRedundant = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 1)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected"))
if mibBuilder.loadTexts: etsysPseChassisPowerRedundant.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerRedundant.setDescription('Pse chassis power is in redundant state. At least 500 msec must elapse between notifications being emitted by the same object instance.')
etsysPseChassisPowerNonRedundant = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 2)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected"))
if mibBuilder.loadTexts: etsysPseChassisPowerNonRedundant.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerNonRedundant.setDescription('Pse chassis power is in non-redundant state. At least 500 msec must elapse between notifications being emitted by the same object instance.')
etsysPsePowerSupplyModuleStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 3)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatus"))
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleStatusChange.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleStatusChange.setDescription('A Pse Power Supply module has changed state. At least 500 msec must elapse between notifications being emitted by the same object instance.')
etsysPsePowerAllocationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2))
etsysPsePowerAllocationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1))
etsysPsePowerAllocationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2))
etsysPsePowerAllocationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 1)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAllocationMode"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerSnmpNotification"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAvailableMaximum"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseSlotPowerMaximum"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseSlotPowerAssigned"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationControlGroup = etsysPsePowerAllocationControlGroup.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerAllocationControlGroup.setDescription('Power over Ethernet Power Allocation Control group.')
etsysPseChassisPowerStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 2)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAvailable"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerConsumable"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAssigned"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerRedundancy"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPseChassisPowerStatusGroup = etsysPseChassisPowerStatusGroup.setStatus('current')
if mibBuilder.loadTexts: etsysPseChassisPowerStatusGroup.setDescription('Power over Ethernet Power Supply group.')
etsysPsePowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 3)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerRedundant"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerNonRedundant"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerNotificationGroup = etsysPsePowerNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerNotificationGroup.setDescription('Power over Ethernet Power Redundancy Notifications group.')
etsysPseModulePowerManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 4)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerMode"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerClassBudget"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPseModulePowerManagementGroup = etsysPseModulePowerManagementGroup.setStatus('current')
if mibBuilder.loadTexts: etsysPseModulePowerManagementGroup.setDescription('Power over Ethernet Module Power Budget Management group.')
etsysPsePortPowerManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 5)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerLimit"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerUsage"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPDType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePortPowerManagementGroup = etsysPsePortPowerManagementGroup.setStatus('deprecated')
if mibBuilder.loadTexts: etsysPsePortPowerManagementGroup.setDescription('Power over Ethernet Port Power Budget Management group.')
etsysPsePortPowerManagementGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 6)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerLimit"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerUsage"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPDType"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortCapability"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortCapabilitySelect"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortDetectionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePortPowerManagementGroupRev2 = etsysPsePortPowerManagementGroupRev2.setStatus('current')
if mibBuilder.loadTexts: etsysPsePortPowerManagementGroupRev2.setDescription('Power over Ethernet Port Power Budget Management group.')
etsysPsePowerAllocationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 1)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerAllocationControlGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerStatusGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationCompliance = etsysPsePowerAllocationCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerAllocationCompliance.setDescription('The compliance statement for devices that support manual power allocation.')
etsysPsePowerAllocationCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 2)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerAllocationControlGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerStatusGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerNotificationGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerManagementGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerManagementGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationCompliance2 = etsysPsePowerAllocationCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: etsysPsePowerAllocationCompliance2.setDescription('The compliance statement for devices that support power budgets.')
etsysPsePowerAllocationCompliance2Rev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 3)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerAllocationControlGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerStatusGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerNotificationGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerManagementGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerManagementGroupRev2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationCompliance2Rev2 = etsysPsePowerAllocationCompliance2Rev2.setStatus('current')
if mibBuilder.loadTexts: etsysPsePowerAllocationCompliance2Rev2.setDescription('The compliance statement for devices that support power budgets.')
mibBuilder.exportSymbols("ENTERASYS-POWER-ETHERNET-EXT-MIB", etsysPseChassisPowerAvailable=etsysPseChassisPowerAvailable, etsysPseChassisPowerRedundancy=etsysPseChassisPowerRedundancy, etsysPsePortPowerManagementTable=etsysPsePortPowerManagementTable, etsysPseSlotPowerAllocationTable=etsysPseSlotPowerAllocationTable, etsysPseSlotPowerAssigned=etsysPseSlotPowerAssigned, etsysPseModulePowerManagementGroup=etsysPseModulePowerManagementGroup, etsysPowerEthernetMibExtMIB=etsysPowerEthernetMibExtMIB, etsysPseSlotPowerManagement=etsysPseSlotPowerManagement, etsysPseSlotPowerAllocation=etsysPseSlotPowerAllocation, etsysPseModulePowerManagementTable=etsysPseModulePowerManagementTable, etsysPsePortDetectionStatus=etsysPsePortDetectionStatus, etsysPseChassisPowerAssigned=etsysPseChassisPowerAssigned, etsysPsePowerSupplyModuleStatusChange=etsysPsePowerSupplyModuleStatusChange, etsysPsePowerAllocationConformance=etsysPsePowerAllocationConformance, etsysPsePortPDType=etsysPsePortPDType, etsysPsePowerSupplyModuleStatus=etsysPsePowerSupplyModuleStatus, etsysPsePortPowerManagementGroup=etsysPsePortPowerManagementGroup, etsysPsePowerSupplyModuleNumber=etsysPsePowerSupplyModuleNumber, etsysPsePowerAllocationGroups=etsysPsePowerAllocationGroups, etsysPowerEthernetObjects=etsysPowerEthernetObjects, etsysPsePortPowerLimit=etsysPsePortPowerLimit, etsysPsePortPowerManagementEntry=etsysPsePortPowerManagementEntry, etsysPseChassisPowerAllocationMode=etsysPseChassisPowerAllocationMode, etsysPsePowerAllocationCompliance2Rev2=etsysPsePowerAllocationCompliance2Rev2, etsysPseChassisPowerConsumable=etsysPseChassisPowerConsumable, etsysPsePowerSupplyStatusEntry=etsysPsePowerSupplyStatusEntry, etsysPseChassisPowerStatus=etsysPseChassisPowerStatus, etsysPsePowerAllocationControlGroup=etsysPsePowerAllocationControlGroup, etsysPseModulePowerClassBudget=etsysPseModulePowerClassBudget, etsysPsePowerAllocationCompliance2=etsysPsePowerAllocationCompliance2, etsysPseChassisPowerAvailableMaximum=etsysPseChassisPowerAvailableMaximum, etsysPseChassisPowerDetected=etsysPseChassisPowerDetected, etsysPsePortPowerUsage=etsysPsePortPowerUsage, etsysPsePowerSupplyStatusTable=etsysPsePowerSupplyStatusTable, etsysPseChassisPowerNonRedundant=etsysPseChassisPowerNonRedundant, etsysPseChassisPowerAllocation=etsysPseChassisPowerAllocation, etsysPseModulePowerUsage=etsysPseModulePowerUsage, etsysPseSlotPowerMaximum=etsysPseSlotPowerMaximum, etsysPsePowerAllocationCompliances=etsysPsePowerAllocationCompliances, etsysPsePortCapabilitySelect=etsysPsePortCapabilitySelect, etsysPseChassisPowerStatusGroup=etsysPseChassisPowerStatusGroup, etsysPsePowerAllocationCompliance=etsysPsePowerAllocationCompliance, etsysPseModulePowerManagementEntry=etsysPseModulePowerManagementEntry, etsysPsePortCapability=etsysPsePortCapability, etsysPseSlotPowerAllocationEntry=etsysPseSlotPowerAllocationEntry, etsysPsePowerNotification=etsysPsePowerNotification, etsysPseChassisPowerRedundant=etsysPseChassisPowerRedundant, etsysPsePortPowerManagementGroupRev2=etsysPsePortPowerManagementGroupRev2, etsysPseModulePowerMode=etsysPseModulePowerMode, etsysPsePortPowerManagement=etsysPsePortPowerManagement, PYSNMP_MODULE_ID=etsysPowerEthernetMibExtMIB, etsysPseChassisPowerSnmpNotification=etsysPseChassisPowerSnmpNotification, etsysPsePowerNotificationGroup=etsysPsePowerNotificationGroup)
