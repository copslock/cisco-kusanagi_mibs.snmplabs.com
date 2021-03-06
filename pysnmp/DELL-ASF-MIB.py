#
# PySNMP MIB module DELL-ASF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-ASF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, IpAddress, Counter32, Integer32, iso, ModuleIdentity, NotificationType, Gauge32, Unsigned32, Bits, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "IpAddress", "Counter32", "Integer32", "iso", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "Bits", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wiredformgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 3183))
pet = MibIdentifier((1, 3, 6, 1, 4, 1, 3183, 1))
asfPetEvts = MibIdentifier((1, 3, 6, 1, 4, 1, 3183, 1, 1))
asfTrapIPMIAlertTest = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1001))
asfTrapFanSpeedWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,262400))
asfTrapFanSPeedWarningCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,262528))
asfTrapFanSpeedProblem = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,262402))
asfTrapFanSPeedProblemCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,262530))
asfTrapBatteryLowWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2715392))
asfTrapBatteryLowWarningCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2715520))
asfTrapBatteryFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2715393))
asfTrapBatteryFailCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2715521))
asfTrapUnderVoltageWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131328))
asfTrapUnderVoltageWarningCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131456))
asfTrapUnderVoltage = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131330))
asfTrapUnderVoltageCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131458))
asfTrapOverVoltageWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131335))
asfTrapOverVoltageWarningCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131463))
asfTrapOverVoltage = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131337))
asfTrapVoltageCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131465))
asfTrapCriticalDiscreteVoltage = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131841))
asfTrapCriticalDiscreteVoltageCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131840))
asfTrapUnderTemperatureWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65792))
asfTrapUnderTemperatureWarningCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65920))
asfTrapUnderTemperature = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65794))
asfTrapUnderTemperatureCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65922))
asfTrapOverTemperatureWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65799))
asfTrapOverTemperatureWarningCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65927))
asfTrapOverTemperature = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65801))
asfTrapOverTemperatureCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65929))
asfTrapCaseIntrusion = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356096))
asfTrapCaseIntrusionCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356224))
asfTrapFanRedundancyDegraded = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,264962))
asfTrapFanRedundancyLost = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,264961))
asfTrapFanFullRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,264960))
asfTrapPSRedundancyDegraded = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,527106))
asfTrapPSRedundancyLost = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,527105))
asfTrapPSFullRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,527104))
asfTrapCpuThermalTrip = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487169))
asfTrapCpuThermalTripCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487297))
asfTrapCpuBistError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487170))
asfTrapCpuBistErrorCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487298))
asfTrapCpuIErr = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487168))
asfTrapCpuIErrCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487296))
asfTrapCpuConfigError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487173))
asfTrapCpuDisabled = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487176))
asfTrapCpuEnabled = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487304))
asfTrapCpuConfigErrorCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487301))
asfTrapCpuPresence = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487175))
asfTrapCpuNotPresent = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487303))
asfTrapCpuThrottle = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487178))
asfTrapCpuThrottleCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487306))
asfTrapPsPresenceDeteced = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552704))
asfTrapPsPresenceRemoved = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552832))
asfTrapPsFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552705))
asfTrapPsFailureCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552833))
asfTrapPsPredictiveFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552706))
asfTrapPsPredictiveFailureCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552834))
asfTrapPsAcLost = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552707))
asfTrapPsAcBack = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552835))
asfTrapSelCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1076994))
asfTrapSelFull = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1076996))
asfTrapASRTimeout = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322176))
asfTrapASROsReset = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322177))
asfTrapASRPowerDown = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322178))
asfTrapASRPowerCycle = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322179))
asfTrapOverSystemPowerWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322180))
asfTrapOverSystemPowerWarningCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322181))
asfTrapOverSystemPowerCritical = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322182))
asfTrapOverSystemPowerCriticalCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322183))
asfTrapPSUMismatch = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552710))
asfTrapPSUMismatchNormal = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552838))
asfTrapSystemPowerExceedsWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552711))
asfTrapSystemPowerNormal = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552839))
asfTrapSystemPowerExceedsError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,12611334))
asfTrapSystemPowerExceedsCleared = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,12611462))
asfTrapModuleSDCardFailedError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1404932))
asfTrapModuleSDWriteProtectWarning = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1404935))
asfTrapModuleSDCardPresence = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1405056))
asfTrapModuleSDCardNotPresent = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1404928))
asfTrapSDRedundancyDegraded = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1379074))
asfTrapSDRedundancyLost = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1379073))
asfTrapSDFullRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1379072))
asfTrapInternalDualSDModulePresent = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201152))
asfTrapInternalDualSDModuleAbsent = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201280))
asfTrapInternalDualSDModuleOffline = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201153))
asfTrapInternalDualSDModuleOnline = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201281))
asfTrapInternalDualSDModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201154))
asfTrapInternalDualSDModuleNormal = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201282))
asfTrapInternalDualSDModuleWriteProtected = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201155))
asfTrapInternalDualSDModuleWriteable = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13201283))
asfTrapInternalDualSDModuleRedundant = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13175552))
asfTrapInternalDualSDModuleRedundancyLost = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13175553))
asfTrapInternalDualSDModuleNotRedundant = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,13175555))
mibBuilder.exportSymbols("DELL-ASF-MIB", asfTrapUnderTemperatureWarningCleared=asfTrapUnderTemperatureWarningCleared, asfTrapOverTemperatureWarning=asfTrapOverTemperatureWarning, asfTrapFanRedundancyDegraded=asfTrapFanRedundancyDegraded, asfTrapBatteryFailure=asfTrapBatteryFailure, asfTrapCpuNotPresent=asfTrapCpuNotPresent, asfTrapCpuBistError=asfTrapCpuBistError, asfTrapSDRedundancyDegraded=asfTrapSDRedundancyDegraded, asfTrapSDRedundancyLost=asfTrapSDRedundancyLost, asfTrapPsPredictiveFailureCleared=asfTrapPsPredictiveFailureCleared, asfTrapPsFailure=asfTrapPsFailure, asfTrapSystemPowerExceedsError=asfTrapSystemPowerExceedsError, asfTrapFanSpeedWarning=asfTrapFanSpeedWarning, asfTrapCpuThrottleCleared=asfTrapCpuThrottleCleared, asfTrapInternalDualSDModuleAbsent=asfTrapInternalDualSDModuleAbsent, asfTrapPSRedundancyDegraded=asfTrapPSRedundancyDegraded, asfTrapInternalDualSDModuleNotRedundant=asfTrapInternalDualSDModuleNotRedundant, asfTrapUnderVoltageWarning=asfTrapUnderVoltageWarning, asfTrapPsAcLost=asfTrapPsAcLost, asfTrapSelFull=asfTrapSelFull, asfTrapOverVoltage=asfTrapOverVoltage, asfTrapPsAcBack=asfTrapPsAcBack, asfTrapFanSPeedProblemCleared=asfTrapFanSPeedProblemCleared, asfTrapBatteryLowWarning=asfTrapBatteryLowWarning, asfTrapInternalDualSDModuleRedundancyLost=asfTrapInternalDualSDModuleRedundancyLost, asfTrapUnderVoltageWarningCleared=asfTrapUnderVoltageWarningCleared, asfTrapCpuIErr=asfTrapCpuIErr, asfTrapCpuThermalTripCleared=asfTrapCpuThermalTripCleared, asfTrapOverSystemPowerCriticalCleared=asfTrapOverSystemPowerCriticalCleared, asfTrapSDFullRedundancy=asfTrapSDFullRedundancy, asfTrapASRTimeout=asfTrapASRTimeout, asfTrapInternalDualSDModuleOnline=asfTrapInternalDualSDModuleOnline, asfTrapPSUMismatchNormal=asfTrapPSUMismatchNormal, asfTrapFanRedundancyLost=asfTrapFanRedundancyLost, asfTrapInternalDualSDModuleWriteProtected=asfTrapInternalDualSDModuleWriteProtected, asfTrapFanSPeedWarningCleared=asfTrapFanSPeedWarningCleared, pet=pet, asfTrapModuleSDCardNotPresent=asfTrapModuleSDCardNotPresent, asfTrapOverTemperatureCleared=asfTrapOverTemperatureCleared, asfTrapCpuEnabled=asfTrapCpuEnabled, asfTrapCpuPresence=asfTrapCpuPresence, asfTrapOverVoltageWarningCleared=asfTrapOverVoltageWarningCleared, asfTrapASRPowerDown=asfTrapASRPowerDown, asfTrapOverSystemPowerWarningCleared=asfTrapOverSystemPowerWarningCleared, asfTrapOverVoltageWarning=asfTrapOverVoltageWarning, asfTrapModuleSDWriteProtectWarning=asfTrapModuleSDWriteProtectWarning, asfTrapInternalDualSDModulePresent=asfTrapInternalDualSDModulePresent, asfTrapCpuThermalTrip=asfTrapCpuThermalTrip, asfTrapASRPowerCycle=asfTrapASRPowerCycle, asfTrapOverSystemPowerCritical=asfTrapOverSystemPowerCritical, asfTrapCaseIntrusionCleared=asfTrapCaseIntrusionCleared, asfTrapPsFailureCleared=asfTrapPsFailureCleared, asfTrapCpuIErrCleared=asfTrapCpuIErrCleared, asfTrapInternalDualSDModuleFailure=asfTrapInternalDualSDModuleFailure, asfTrapBatteryFailCleared=asfTrapBatteryFailCleared, asfTrapFanFullRedundancy=asfTrapFanFullRedundancy, asfTrapUnderVoltageCleared=asfTrapUnderVoltageCleared, asfTrapPSFullRedundancy=asfTrapPSFullRedundancy, asfTrapUnderTemperatureWarning=asfTrapUnderTemperatureWarning, asfTrapCpuThrottle=asfTrapCpuThrottle, asfTrapUnderTemperature=asfTrapUnderTemperature, asfTrapInternalDualSDModuleRedundant=asfTrapInternalDualSDModuleRedundant, asfTrapSystemPowerExceedsWarning=asfTrapSystemPowerExceedsWarning, asfTrapUnderTemperatureCleared=asfTrapUnderTemperatureCleared, asfTrapIPMIAlertTest=asfTrapIPMIAlertTest, asfTrapPSRedundancyLost=asfTrapPSRedundancyLost, asfTrapOverTemperature=asfTrapOverTemperature, asfTrapInternalDualSDModuleWriteable=asfTrapInternalDualSDModuleWriteable, asfTrapModuleSDCardFailedError=asfTrapModuleSDCardFailedError, asfTrapCaseIntrusion=asfTrapCaseIntrusion, asfTrapInternalDualSDModuleNormal=asfTrapInternalDualSDModuleNormal, asfTrapUnderVoltage=asfTrapUnderVoltage, wiredformgmt=wiredformgmt, asfTrapPsPresenceDeteced=asfTrapPsPresenceDeteced, asfTrapCpuBistErrorCleared=asfTrapCpuBistErrorCleared, asfTrapOverTemperatureWarningCleared=asfTrapOverTemperatureWarningCleared, asfTrapPsPresenceRemoved=asfTrapPsPresenceRemoved, asfTrapSystemPowerExceedsCleared=asfTrapSystemPowerExceedsCleared, asfTrapPsPredictiveFailure=asfTrapPsPredictiveFailure, asfTrapInternalDualSDModuleOffline=asfTrapInternalDualSDModuleOffline, asfTrapSystemPowerNormal=asfTrapSystemPowerNormal, asfTrapCriticalDiscreteVoltageCleared=asfTrapCriticalDiscreteVoltageCleared, asfTrapBatteryLowWarningCleared=asfTrapBatteryLowWarningCleared, asfTrapCpuConfigErrorCleared=asfTrapCpuConfigErrorCleared, asfTrapCriticalDiscreteVoltage=asfTrapCriticalDiscreteVoltage, asfTrapCpuConfigError=asfTrapCpuConfigError, asfTrapPSUMismatch=asfTrapPSUMismatch, asfTrapASROsReset=asfTrapASROsReset, asfTrapFanSpeedProblem=asfTrapFanSpeedProblem, asfTrapSelCleared=asfTrapSelCleared, asfTrapVoltageCleared=asfTrapVoltageCleared, asfTrapOverSystemPowerWarning=asfTrapOverSystemPowerWarning, asfTrapCpuDisabled=asfTrapCpuDisabled, asfPetEvts=asfPetEvts, asfTrapModuleSDCardPresence=asfTrapModuleSDCardPresence)
