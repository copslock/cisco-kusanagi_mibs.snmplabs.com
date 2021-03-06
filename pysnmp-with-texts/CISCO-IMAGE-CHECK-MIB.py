#
# PySNMP MIB module CISCO-IMAGE-CHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMAGE-CHECK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter32, TimeTicks, Bits, Counter64, NotificationType, ObjectIdentity, Gauge32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter32", "TimeTicks", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "iso", "Unsigned32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
ciscoImageCheckMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99990))
if mibBuilder.loadTexts: ciscoImageCheckMIB.setLastUpdated('200305150000Z')
if mibBuilder.loadTexts: ciscoImageCheckMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImageCheckMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoImageCheckMIB.setDescription('Initial version of Image Check MIB.')
ciscoImageCheckMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1))
ciscoImageCheck = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1))
ciscoImageCheckOpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoImageCheckOpTable.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckOpTable.setDescription('A table of Image check operation entries. Each entry represents an Image check operation that has been initiated. ')
ciscoImageCheckOpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckSerialNum"))
if mibBuilder.loadTexts: ciscoImageCheckOpEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckOpEntry.setDescription('An Image check operation entry. Each entry consists of an image name, current status of the check operation and a row status. A management station wishing to create an entry should first generate a pseudo-random serial number to be used as the index to this sparse table. The station should then create the associated instance of the row status object. It must also, create the associated instance of the image name. This image is checked for compatibility with the image already running on the active supervisor. Once the appropriate instances of all the mandatory objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo. Once an operation has been activated, it cannot be stopped. Once the operation completes, the management station should retrieve the value of the status object and delete the entry. In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing. ')
ciscoImageCheckSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ciscoImageCheckSerialNum.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckSerialNum.setDescription('Object which specifies a unique entry in the table. A management station wishing to initiate a check operation should use a pseudo-random value for this object when creating or modifying an instance of a ciscoImageCheckOpEntry. ')
ciscoImageCheckImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoImageCheckImageName.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckImageName.setDescription('Image file name that needs the verification. If the Image name is NULL then it is assumed that the image check is to be done with the image on standby supervisor. ')
ciscoImageCheckStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("inCompatLoose", 3), ("inCompatStrict", 4), ("compatible", 5), ("noStandby", 6), ("pssErr", 7), ("extractFail", 8), ("fileParseErr", 9), ("getIncompatErr", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImageCheckStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckStatus.setDescription('The current status of the image check operation. If the status is inCompatLoose(3) or inCompatStrict(4), one can look at the detail reasons of incompatibilities by looking at ciscoImgChkResultsTable described below. If the status is compatible, then there is no need to look at the ciscoImgChkResultsTable. If the status is noStandby(6), pssErr(7), extractFail(8), fileParseErr(9) or getIncompatErr(10), there is some internal error in even starting the check compatibility process, and hence the ciscoImgChkResultsTable should not be read for any details. inProgress(2) - Image check is in progress inCompatLoose(3) - Loose incompatibility inCompatStrict(4) - Strict incompatibility compatible(5) - images are compatible noStandby(6) - standby supervisor is absent pssErr(7) - internal error extractFail(8) - Could not extract image fileParseErr(9) - Could not parse image getIncompatErr(10) - internal error in determining incompatibilities. ')
ciscoImageCheckEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoImageCheckEntryStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckEntryStatus.setDescription('The status of this table entry.')
ciscoImgChkResultsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2), )
if mibBuilder.loadTexts: ciscoImgChkResultsTable.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkResultsTable.setDescription('This table lists the features and capabilities that are incompatible for the request that was made corresponding to the instance of ciscoImgChkFeatureIndex in the ciscoImageCheckOpTable.')
ciscoImgChkResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckSerialNum"), (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImgChkFeatureIndex"), (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabIndex"))
if mibBuilder.loadTexts: ciscoImgChkResultsEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkResultsEntry.setDescription('An entry of ciscoImgChkResultsTable. ')
ciscoImgChkFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ciscoImgChkFeatureIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkFeatureIndex.setDescription('The index of the incompatible feature.')
ciscoImgChkCapabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ciscoImgChkCapabIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkCapabIndex.setDescription('The index of the incompatible capability.')
ciscoImgChkFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkFeatureName.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkFeatureName.setDescription('The name of the incompatible feature. The list of features is subject to implementation in a given software release. The current list of features is as follows - fspf - FSPF Routing Protocol Application fcmpls - Multi-Protocol Label Switching fib - FIB Manager flogi - F Port Server rscn - RSCN Module fcns - Name Server fcdomain - Domain Manager fc-tunnel - FC MPLS tunnel ipfc - Ipfc Manager ipconf - IP Configuration Manager ips - IPS Manager port - Port Manager port-channel - Port Channel Manager span - Switch Port Analyzer sysmgr-ver - System Manager version controller vrrp-cfg - VRRP Configuration vsan - VSAN manager zone - Zone Server ')
ciscoImgChkCapabilityName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkCapabilityName.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkCapabilityName.setDescription('The name of the incompatible capability. The list of capabilities is subject to implementation in a given software release. The current list of capabilities is as follows - CAP_FEATURE_SPAN_FCFWD_STBY_POP_ENABLED CAP_FEATURE_SPAN_IF_VSAN_SRC_MIX_NOT_ALLOWED CAP_FEATURE_SPAN_IF_SRC_VSAN_FILTER_NOT_ALLOWED CAP_FEATURE_SPAN_FC_TUNNEL_CFG CAP_FEATURE_SPAN_ST_PORT_CFG CAP_FEATURE_SPAN_FCIP_SRC_CFG CAP_FEATURE_SPAN_ISCSI_SRC_CFG CAP_FEATURE_ZS_READ_ONLY_ZONING CAP_FEATURE_ZS_LUN_ZONING CAP_FEATURE_PORT_MODE_ST_CFG CAP_FEATURE_FC_TUNNEL_CFG CAP_FEATURE_PORT_PERFORMANCE_BUF ')
ciscoImgChkCapabilityReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("loose", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkCapabilityReq.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkCapabilityReq.setDescription('Whether capability check is strict or loose. ')
ciscoImgChkInCompDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImgChkInCompDescr.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkInCompDescr.setDescription("Description of the incompatibilty. For example, if the name of the incompatibilty (the instance of ciscoImgChkCapabilityName) is CAP_FEATURE_ZS_READ_ONLY_ZONING, then the description will be - 'Zone Server - Read-only zoning configured'. For each incompatibility name that appears in ciscoImgChkCapabilityName, there will be a corresponding description described by the instance of this object. ")
ciscoImageCheckMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2))
ciscoImageCheckMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 1))
ciscoImageCheckMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2))
ciscoImageCheckMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 1, 1)).setObjects(("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckOpGroup"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkResultsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCheckMIBCompliance = ciscoImageCheckMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-IMAGE-CHECK-MIB.')
ciscoImageCheckOpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2, 1)).setObjects(("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckImageName"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckStatus"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCheckOpGroup = ciscoImageCheckOpGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoImageCheckOpGroup.setDescription('A collection of objects for Image Check Operations group.')
ciscoImgChkResultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2, 2)).setObjects(("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkFeatureName"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabilityName"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabilityReq"), ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkInCompDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImgChkResultsGroup = ciscoImgChkResultsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoImgChkResultsGroup.setDescription('A collection of objects for Image check results group.')
mibBuilder.exportSymbols("CISCO-IMAGE-CHECK-MIB", PYSNMP_MODULE_ID=ciscoImageCheckMIB, ciscoImgChkResultsTable=ciscoImgChkResultsTable, ciscoImageCheckMIBObjects=ciscoImageCheckMIBObjects, ciscoImgChkFeatureName=ciscoImgChkFeatureName, ciscoImageCheckOpTable=ciscoImageCheckOpTable, ciscoImageCheckOpEntry=ciscoImageCheckOpEntry, ciscoImgChkInCompDescr=ciscoImgChkInCompDescr, ciscoImageCheckStatus=ciscoImageCheckStatus, ciscoImageCheckMIBConformance=ciscoImageCheckMIBConformance, ciscoImgChkResultsGroup=ciscoImgChkResultsGroup, ciscoImgChkCapabilityName=ciscoImgChkCapabilityName, ciscoImageCheckMIBCompliances=ciscoImageCheckMIBCompliances, ciscoImgChkResultsEntry=ciscoImgChkResultsEntry, ciscoImgChkFeatureIndex=ciscoImgChkFeatureIndex, ciscoImgChkCapabilityReq=ciscoImgChkCapabilityReq, ciscoImageCheckSerialNum=ciscoImageCheckSerialNum, ciscoImageCheckImageName=ciscoImageCheckImageName, ciscoImgChkCapabIndex=ciscoImgChkCapabIndex, ciscoImageCheckMIB=ciscoImageCheckMIB, ciscoImageCheckMIBGroups=ciscoImageCheckMIBGroups, ciscoImageCheckMIBCompliance=ciscoImageCheckMIBCompliance, ciscoImageCheckEntryStatus=ciscoImageCheckEntryStatus, ciscoImageCheck=ciscoImageCheck, ciscoImageCheckOpGroup=ciscoImageCheckOpGroup)
