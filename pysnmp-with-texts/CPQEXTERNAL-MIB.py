#
# PySNMP MIB module CPQEXTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQEXTERNAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
compaq, = mibBuilder.importSymbols("CPQHOST-MIB", "compaq")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Unsigned32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, ObjectIdentity, Gauge32, enterprises, MibIdentifier, TimeTicks, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Unsigned32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "enterprises", "MibIdentifier", "TimeTicks", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpqExternalMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 17))
cpqExMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 17, 1))
cpqExComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 17, 2))
cpqExInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 17, 2, 1))
cpqExStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 17, 2, 2))
cpqExOsCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4))
cpqExMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 232, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExMibRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExMibRevMajor.setDescription('The Major Revision level of the MIB. A change in the major revision level represents a major change in the architecture of the MIB. A change in the major revision level may indicate a significant change in the information supported and/or the meaning of the supported information, correct interpretation of data may require a MIB document with the same major revision level.')
cpqExMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 232, 17, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExMibRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExMibRevMinor.setDescription('The Minor Revision level of the MIB. A change in the minor revision level may represent some minor additional support, no changes to any pre-existing information has occurred.')
cpqExMibCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExMibCondition.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExMibCondition.setDescription('The overall condition. This object represents the overall status of the external MIB management system represented by this MIB. This status is the aggregate of all external (non-Compaq enterprise) MIBs supported by this agent.')
cpqExOsCommonPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqExOsCommonPollFreq.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExOsCommonPollFreq.setDescription("The Insight Agent's polling frequency. The frequency, in seconds, at which the Insight Agent requests information from. A frequency of zero indicates that the Insight Agent retrieves the information upon request of a management station, it does not poll at a specific interval. If the poll frequency is zero (0) all attempts to write to this object will fail. If the poll frequency is non-zero, setting this value will change the polling frequency of the Insight Agent. Setting the poll frequency to zero will always fail, an agent may also choose to fail any request to change the poll frequency to a value that would severely impact system performance.")
cpqExOsCommonModuleTable = MibTable((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2), )
if mibBuilder.loadTexts: cpqExOsCommonModuleTable.setStatus('deprecated')
if mibBuilder.loadTexts: cpqExOsCommonModuleTable.setDescription('A table of software modules that provide an interface to the device this MIB describes.')
cpqExOsCommonModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1), ).setIndexNames((0, "CPQEXTERNAL-MIB", "cpqExOsCommonModuleIndex"))
if mibBuilder.loadTexts: cpqExOsCommonModuleEntry.setStatus('deprecated')
if mibBuilder.loadTexts: cpqExOsCommonModuleEntry.setDescription('A description of a software modules that provide an interface to the device this MIB describes.')
cpqExOsCommonModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExOsCommonModuleIndex.setStatus('deprecated')
if mibBuilder.loadTexts: cpqExOsCommonModuleIndex.setDescription('A unique index for this module description.')
cpqExOsCommonModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExOsCommonModuleName.setStatus('deprecated')
if mibBuilder.loadTexts: cpqExOsCommonModuleName.setDescription('The module name.')
cpqExOsCommonModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExOsCommonModuleVersion.setStatus('deprecated')
if mibBuilder.loadTexts: cpqExOsCommonModuleVersion.setDescription('The module version in XX.YY format. Where XX is the major version number and YY is the minor version number. This field will be a null (size 0) string if the agent cannot provide the module version.')
cpqExOsCommonModuleDate = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExOsCommonModuleDate.setStatus('deprecated')
if mibBuilder.loadTexts: cpqExOsCommonModuleDate.setDescription('The module date. field octets contents range ===== ====== ======= ===== 1 1-2 year 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minute 0..59 6 7 second 0..60 (use 60 for leap-second) This field will be set to year = 0 if the agent cannot provide the module date. The hour, minute, and second field will be set to zero (0) if they are not relevant. The year field is set with the most significant octet first.')
cpqExOsCommonModulePurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExOsCommonModulePurpose.setStatus('deprecated')
if mibBuilder.loadTexts: cpqExOsCommonModulePurpose.setDescription('The purpose of the module described in this entry.')
cpqExExternalCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalCondition.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalCondition.setDescription('The condition of the external mib status table as a whole.')
cpqExExternalStatusTable = MibTable((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2), )
if mibBuilder.loadTexts: cpqExExternalStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusTable.setDescription('A list of status entries for external MIBs.')
cpqExExternalStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1), ).setIndexNames((0, "CPQEXTERNAL-MIB", "cpqExExternalStatusIndex"))
if mibBuilder.loadTexts: cpqExExternalStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusEntry.setDescription('A list of status OIDs used to check external MIB status values. The table also lists how the values will be interpreted.')
cpqExExternalStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusIndex.setDescription('An index that uniquely identifies an entry in the cpqExExternalStatusTable table.')
cpqExExternalStatusInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusInterval.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusInterval.setDescription('The interval, in seconds, between consecutive samples of the data.')
cpqExExternalStatusVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusVariable.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusVariable.setDescription('The object identifier of the particular variable to be sampled. Only variables that resolve to an ASN.1 primitive type of INTEGER (INTEGER, Counter, Gauge, or TimeTicks) may be sampled.')
cpqExExternalStatusValid = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusValid.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusValid.setDescription('This value will be true(2) if the object identifier (cpqExExternalStatusVariable) was successfully retrieved during the last sampling period. If the object identifier was not available or could not be queried, the value will be false(1).')
cpqExExternalStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusValue.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusValue.setDescription('The value of the object identifier (cpqExExternalStatusVariable) during the last sampling period. The value during the current sampling period is not made available until the period is completed.')
cpqExExternalStatusCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusCondition.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusCondition.setDescription('The condition of the external mib status variable. If the value does not exist or was of an invalid data type, this will be set to other(1). The value will also be set to other(1) if the data returned does not match any of the defined values in the cpqExExternalStatusOkValues, cpqExExternalStatusDegradedValues, or cpqExExternalStatusFailedValues as defined.')
cpqExExternalStatusOkValues = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusOkValues.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusOkValues.setDescription('This is a textual list of possible values which can be compared to the actual value retrieved from cpqExExternalStatusVariable during the last sampling period. This string value will be composed of a comma separated list of signed integer values with an optional range indicated by two integers separated by two periods. Example: -1,2..4,11 The above would interpret the values -1, 2, 3, 4, and 11 as indicating an Ok condition.')
cpqExExternalStatusDegradedValues = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusDegradedValues.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusDegradedValues.setDescription('This is a textual list of possible values which can be compared to the actual value retrieved from cpqExExternalStatusVariable during the last sampling period. This string value will be composed of a comma separated list of signed integer values with an optional range indicated by two integers separated by two periods. Example: -1,2..4,11 The above would interpret the values -1, 2, 3, 4, and 11 as indicating a Degraded condition.')
cpqExExternalStatusFailedValues = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqExExternalStatusFailedValues.setStatus('mandatory')
if mibBuilder.loadTexts: cpqExExternalStatusFailedValues.setDescription('This is a textual list of possible values which can be compared to the actual value retrieved from cpqExExternalStatusVariable during the last sampling period. This string value will be composed of a comma separated list of signed integer values with an optional range indicated by two integers separated by two periods. Example: -1,2..4,11 The above would interpret the values -1, 2, 3, 4, and 11 as indicating a Failed condition.')
mibBuilder.exportSymbols("CPQEXTERNAL-MIB", cpqExOsCommonModuleName=cpqExOsCommonModuleName, cpqExOsCommon=cpqExOsCommon, cpqExMibCondition=cpqExMibCondition, cpqExExternalStatusIndex=cpqExExternalStatusIndex, cpqExStatus=cpqExStatus, cpqExOsCommonModuleEntry=cpqExOsCommonModuleEntry, cpqExMibRev=cpqExMibRev, cpqExternalMgmt=cpqExternalMgmt, cpqExExternalStatusFailedValues=cpqExExternalStatusFailedValues, cpqExMibRevMajor=cpqExMibRevMajor, cpqExExternalCondition=cpqExExternalCondition, cpqExExternalStatusCondition=cpqExExternalStatusCondition, cpqExOsCommonModuleVersion=cpqExOsCommonModuleVersion, cpqExExternalStatusOkValues=cpqExExternalStatusOkValues, cpqExInterface=cpqExInterface, cpqExExternalStatusValue=cpqExExternalStatusValue, cpqExOsCommonModuleTable=cpqExOsCommonModuleTable, cpqExExternalStatusInterval=cpqExExternalStatusInterval, cpqExExternalStatusDegradedValues=cpqExExternalStatusDegradedValues, cpqExExternalStatusValid=cpqExExternalStatusValid, cpqExMibRevMinor=cpqExMibRevMinor, cpqExOsCommonModuleDate=cpqExOsCommonModuleDate, cpqExExternalStatusEntry=cpqExExternalStatusEntry, cpqExComponent=cpqExComponent, cpqExExternalStatusTable=cpqExExternalStatusTable, cpqExOsCommonPollFreq=cpqExOsCommonPollFreq, cpqExOsCommonModuleIndex=cpqExOsCommonModuleIndex, cpqExExternalStatusVariable=cpqExExternalStatusVariable, cpqExOsCommonModulePurpose=cpqExOsCommonModulePurpose)
