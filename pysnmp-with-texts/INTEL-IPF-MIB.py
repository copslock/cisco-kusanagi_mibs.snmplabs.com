#
# PySNMP MIB module INTEL-IPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-IPF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, NotificationType, iso, IpAddress, ObjectIdentity, Counter64, Unsigned32, Counter32, Bits, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "NotificationType", "iso", "IpAddress", "ObjectIdentity", "Counter64", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipf = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34))
ipfUGs = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 1))
ipfL3UGM = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 2))
ipfL4UGM = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 3))
ipfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 34, 4))
class UserGroupSet(OctetString):
    pass

ipfUGsTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1), )
if mibBuilder.loadTexts: ipfUGsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipfUGsTable.setDescription('Numbers and Names of UserGroups')
ipfUGsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1), ).setIndexNames((0, "INTEL-IPF-MIB", "ipfUGsNumber"))
if mibBuilder.loadTexts: ipfUGsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipfUGsEntry.setDescription('')
ipfUGsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfUGsNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipfUGsNumber.setDescription('')
ipfUGsName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfUGsName.setStatus('mandatory')
if mibBuilder.loadTexts: ipfUGsName.setDescription('')
ipfL3UGMTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1), )
if mibBuilder.loadTexts: ipfL3UGMTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL3UGMTable.setDescription('UserGroup membership for prefices of IP-addresses')
ipfL3UGMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1), ).setIndexNames((0, "INTEL-IPF-MIB", "ipfL3UGMIpAddress"))
if mibBuilder.loadTexts: ipfL3UGMEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL3UGMEntry.setDescription('')
ipfL3UGMIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfL3UGMIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL3UGMIpAddress.setDescription('')
ipfL3UGMSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfL3UGMSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL3UGMSubnetMask.setDescription('')
ipfL3UGMUserGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 2, 1, 1, 3), UserGroupSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfL3UGMUserGroups.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL3UGMUserGroups.setDescription('Group membership assigned to packets matching IpAddress AND SubnetMask')
ipfL4UGMTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1), )
if mibBuilder.loadTexts: ipfL4UGMTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL4UGMTable.setDescription('UserGroup membership for layer-4 port numbers')
ipfL4UGMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1), ).setIndexNames((0, "INTEL-IPF-MIB", "ipfL4UGMPortNumber"))
if mibBuilder.loadTexts: ipfL4UGMEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL4UGMEntry.setDescription('')
ipfL4UGMPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfL4UGMPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL4UGMPortNumber.setDescription('')
ipfL4UGMUserGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 34, 3, 1, 1, 2), UserGroupSet()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfL4UGMUserGroups.setStatus('mandatory')
if mibBuilder.loadTexts: ipfL4UGMUserGroups.setDescription('Group membership assigned to packets matching PortNumber')
ipfInfoL3Rejects = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoL3Rejects.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoL3Rejects.setDescription('Packets rejected when exposed to L3 filter')
ipfInfoL4Rejects = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoL4Rejects.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoL4Rejects.setDescription('Packets rejected when exposed to L3 filter')
ipfInfoMostRecentChange = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoMostRecentChange.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoMostRecentChange.setDescription('')
ipfInfoOnOffSwitch = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoOnOffSwitch.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoOnOffSwitch.setDescription('')
ipfInfoDeleteUserGroup = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoDeleteUserGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoDeleteUserGroup.setDescription('Write the number of the UG to delete here.')
ipfInfoDeleteL3UGM = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoDeleteL3UGM.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoDeleteL3UGM.setDescription('Write the IP-address of the L3-entry to delete here.')
ipfInfoDeleteL4UGM = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipfInfoDeleteL4UGM.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoDeleteL4UGM.setDescription('Write the port number of theL4-entry to delete here.')
ipfInfoCreateDeleteStatus = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 34, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("createTableFull", 2), ("deleteNotFound", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfInfoCreateDeleteStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ipfInfoCreateDeleteStatus.setDescription('Completion status of most recent create/delete operation.')
mibBuilder.exportSymbols("INTEL-IPF-MIB", ipfL4UGM=ipfL4UGM, ipfInfoDeleteL4UGM=ipfInfoDeleteL4UGM, ipfL4UGMPortNumber=ipfL4UGMPortNumber, ipfInfoCreateDeleteStatus=ipfInfoCreateDeleteStatus, ipf=ipf, ipfInfoDeleteUserGroup=ipfInfoDeleteUserGroup, UserGroupSet=UserGroupSet, ipfInfoDeleteL3UGM=ipfInfoDeleteL3UGM, ipfUGsName=ipfUGsName, ipfL3UGMTable=ipfL3UGMTable, ipfL3UGMEntry=ipfL3UGMEntry, ipfL3UGMIpAddress=ipfL3UGMIpAddress, ipfL3UGM=ipfL3UGM, ipfUGsNumber=ipfUGsNumber, ipfL4UGMTable=ipfL4UGMTable, ipfL3UGMUserGroups=ipfL3UGMUserGroups, ipfInfoL4Rejects=ipfInfoL4Rejects, ipfInfo=ipfInfo, ipfInfoL3Rejects=ipfInfoL3Rejects, ipfL4UGMEntry=ipfL4UGMEntry, ipfUGsEntry=ipfUGsEntry, ipfInfoOnOffSwitch=ipfInfoOnOffSwitch, ipfUGsTable=ipfUGsTable, ipfL3UGMSubnetMask=ipfL3UGMSubnetMask, ipfUGs=ipfUGs, ipfInfoMostRecentChange=ipfInfoMostRecentChange, ipfL4UGMUserGroups=ipfL4UGMUserGroups)
