#
# PySNMP MIB module HP-ICF-GPPC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-GPPC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, MibIdentifier, TimeTicks, Bits, ModuleIdentity, NotificationType, iso, Counter32, Gauge32, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "MibIdentifier", "TimeTicks", "Bits", "ModuleIdentity", "NotificationType", "iso", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hpicfGppcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41))
hpicfGppcMIB.setRevisions(('2009-12-15 01:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfGppcMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: hpicfGppcMIB.setLastUpdated('200912150105Z')
if mibBuilder.loadTexts: hpicfGppcMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfGppcMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfGppcMIB.setDescription('This MIB module is for HP proprietary General Purpose Packet Control (GPPC)')
class HpicfGppcPolicyName(TextualConvention, OctetString):
    description = 'Type definition for the name of a policy. A policy name is a printable string consisting of up to 64 characters from the ASCII character set.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

hpicfGppcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1))
hpicfGppcAppControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2), )
if mibBuilder.loadTexts: hpicfGppcAppControlTable.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAppControlTable.setDescription('The application control table. This keeps track of the applications that use GPPC, the policies set by these applications, and information on where/when/how to apply these policies. This information includes the interfaces and VLANs where the policy should be applied, whether it should be applied at ingress or egress, and when it should expire.')
hpicfGppcAppControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1), ).setIndexNames((0, "HP-ICF-GPPC-MIB", "hpicfGppcAcAppName"), (0, "HP-ICF-GPPC-MIB", "hpicfGppcAcAppInstance"), (0, "HP-ICF-GPPC-MIB", "hpicfGppcAcPolicyName"))
if mibBuilder.loadTexts: hpicfGppcAppControlEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAppControlEntry.setDescription('An entry in the application control table.')
hpicfGppcAcAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: hpicfGppcAcAppName.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcAppName.setDescription('Name of the application that last modified this row. All applications of the same type should use the same name and should use different instance identifiers to identify themselves uniquely. This is a printable string up to 16 bytes in size.')
hpicfGppcAcAppInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: hpicfGppcAcAppInstance.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcAppInstance.setDescription('Instance identifier of the application. This is used to distinguish between different instances of the same application. This is a printable string up to 16 bytes in size.')
hpicfGppcAcPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 3), HpicfGppcPolicyName())
if mibBuilder.loadTexts: hpicfGppcAcPolicyName.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcPolicyName.setDescription('Name of the policy. Each policy is uniquely identified by its name. It is possible to apply the same policy in different manners to different interfaces and VLANs. This is a printable string up to 64 characters in size.')
hpicfGppcAcIngressIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcIngressIfList.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcIngressIfList.setDescription('List of interfaces to which this policy applies at ingress.')
hpicfGppcAcIngressVlanMap1k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap1k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap1k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 0 through 1023. The first octet corresponds to VLANs with vlan index values of 0 through 7, the second octet to VLANs 8 through 15, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at ingress, the corresponding bit is set to '1'.")
hpicfGppcAcIngressVlanMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap2k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap2k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 1024 through 2047. The first octet corresponds to VLANs with vlan index values of 1024 through 1031, the second octet to VLANs 1032 through 1039, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at ingress, the corresponding bit is set to '1'.")
hpicfGppcAcIngressVlanMap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap3k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap3k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 2048 through 3071. The first octet corresponds to VLANs with vlan index values of 2048 through 2055, the second octet to VLANs 2056 through 2063, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at ingress, the corresponding bit is set to '1'.")
hpicfGppcAcIngressVlanMap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap4k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcIngressVlanMap4k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 3072 through 4095. The first octet corresponds to VLANs with vlan index values of 3072 through 3079, the second octet to VLANs 3080 through 3087, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at ingress, the corresponding bit is set to '1'.")
hpicfGppcAcEgressIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 9), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcEgressIfList.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcEgressIfList.setDescription('List of interfaces to which this policy applies at egress.')
hpicfGppcAcEgressVlanMap1k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap1k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap1k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 0 through 1023. The first octet corresponds to VLANs with vlan index values of 0 through 7, the second octet to VLANs 8 through 15, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at egress, the corresponding bit is set to '1'.")
hpicfGppcAcEgressVlanMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap2k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap2k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 1024 through 2047. The first octet corresponds to VLANs with vlan index values of 1024 through 1031, the second octet to VLANs 1032 through 1039, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at egress, the corresponding bit is set to '1'.")
hpicfGppcAcEgressVlanMap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap3k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap3k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 2048 through 3071. The first octet corresponds to VLANs with vlan index values of 2048 through 2055, the second octet to VLANs 2056 through 2063, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at egress, the corresponding bit is set to '1'.")
hpicfGppcAcEgressVlanMap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap4k.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcEgressVlanMap4k.setDescription("A string of octets containing one bit per VLAN for VLANS with vlan index values of 3072 through 4095. The first octet corresponds to VLANs with vlan index values of 3072 through 3079, the second octet to VLANs 3080 through 3087, etc. The most significant bit of each octet corresponds to the lowest vlan index value in that octet. For each VLAN that this policy should apply to at egress, the corresponding bit is set to '1'.")
hpicfGppcAcExpPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("permanent", 1), ("slot-down", 2), ("app-down", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcExpPolicy.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcExpPolicy.setDescription("Expiration policy. This indicates whether a policy should expire automatically. 'permanent' means a policy should never expire automatically.")
hpicfGppcAcExpString = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcExpString.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcExpString.setDescription("Expiration string. This is used in conjuntion with hpicfGppcAcExpPolicy to indicate when a policy should expire automatically. The value stored in this object is interpreted differently for different expiration policies. When the expiration policy is 'permanent', this value is ignored.")
hpicfGppcAcLastErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38, 50, 51, 52, 53, 54, 55, 56, 57, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85))).clone(namedValues=NamedValues(("no-error", 0), ("gppc-generic-error", 1), ("gppc-length-error", 2), ("gppc-name-error", 3), ("gppc-parameter-error", 4), ("gppc-not-implemented", 5), ("gppc-malloc-error", 6), ("gppc-too-many-apps", 7), ("gppc-too-many-policies", 8), ("gppc-already-reserved", 9), ("gppc-entry-not-found", 10), ("gppc-entry-exists", 11), ("gppc-platform-error", 12), ("gppc-app-using-policy", 13), ("gppc-invalid-policy-type", 14), ("gppc-not-reserved", 15), ("gppc-no-policy", 16), ("gppc-policy-not-active", 17), ("gppc-policy-has-rules", 18), ("gppc-rule-exists", 19), ("gppc-mac-mirror-mac-exists", 30), ("gppc-mac-mirror-dir-both-conflict", 31), ("gppc-mac-mirror-dir-src-conflict", 32), ("gppc-mac-mirror-dir-dst-conflict", 33), ("gppc-mac-mirror-invalid-session", 34), ("gppc-mac-mirror-invalid-direction", 35), ("gppc-mac-mirror-no-entry", 36), ("gppc-mac-mirror-convert-error", 37), ("gppc-mac-mirror-table-full", 38), ("gppc-cfg-generic-error", 50), ("gppc-cfg-entry-not-found", 51), ("gppc-cfg-set-error", 52), ("gppc-cfg-get-error", 53), ("gppc-cfg-no-record", 54), ("gppc-cfg-add-record-error", 55), ("gppc-cfg-invalid", 56), ("gppc-cfg-malloc-error", 57), ("gppcTrmodeErr", 70), ("gppcTrmodeInvalidZoneNumber", 71), ("gppcTrmodeOperationNotSupported", 72), ("gppcTrmodeZoneNameTooLong", 73), ("gppcTrmodeZoneNameNotFound", 74), ("gppcTrmodeZoneNameAlreadyExists", 75), ("gppcTrmodeTooManyZoneNames", 76), ("gppcTrmodeUnknownPort", 77), ("gppcTrmodeCannotDeleteDefaultZone", 78), ("gppcTrmodeCannotDeleteZoneWithRules", 79), ("gppcTrmodeInvalidFilterNumber", 80), ("gppcTrmodeCannotFilterTrafficWithinZone", 81), ("gppcTrmodeInvalidAction", 82), ("gppcTrmodeUnicastInterceptMacaddrRequired", 83), ("gppcTrmodeCannotAllocateMirrorSession", 84), ("gppcTrmodeCannotAllocateClassifierResources", 85)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfGppcAcLastErrorCode.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcLastErrorCode.setDescription('Error code of the last error that occurred. A non-zero value indicates that the last operation performed by this instance of the application on the named policy did not succeed. A detailed description of the error is available in hpicfGppcAcLastErrorString.')
hpicfGppcAcLastErrorString = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfGppcAcLastErrorString.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcLastErrorString.setDescription('Description of the last error that occurred. This is a printable ASCII string that describes the error in some detail.')
hpicfGppcAcRowAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcRowAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcRowAdminStatus.setDescription('Administrative status of this row. The named policy in this row is applied to the interfaces and/or VLANs by this instance of the application only when the administrative status is enabled. This is the main on/off switch for the row. The row status must be active for this switch to have an effect.')
hpicfGppcAcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcAcRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcAcRowStatus.setDescription('Status of this row. Row status must be active, and the admin status (see hpicfGppcAcRowAdminStatus) must be enabled for this row to be activated.')
hpicfGppcNamedPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3), )
if mibBuilder.loadTexts: hpicfGppcNamedPolicyTable.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcNamedPolicyTable.setDescription('The named policy table. This table lists the name and type of all policies that are applied via GPPC.')
hpicfGppcNamedPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1), ).setIndexNames((0, "HP-ICF-GPPC-MIB", "hpicfGppcNpPolicyName"))
if mibBuilder.loadTexts: hpicfGppcNamedPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcNamedPolicyEntry.setDescription('An entry in the named policy table.')
hpicfGppcNpPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1, 1), HpicfGppcPolicyName())
if mibBuilder.loadTexts: hpicfGppcNpPolicyName.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcNpPolicyName.setDescription('Name of the policy. The name of a policy is its unique identification. It is a printable string in ASCII characters. It can be up to 64 characters in length')
hpicfGppcNpPolicyType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mac-based-mirroring", 1), ("zone-intercept", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcNpPolicyType.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcNpPolicyType.setDescription("Type of the policy. A policy type of 'mac-based-mirroring' indicates that the policy is used to mirror traffic based on the MAC address of the source or destination.")
hpicfGppcNpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcNpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcNpRowStatus.setDescription('Status of this row. The named policy must be active before rules can be added to it or removed from it. A newly created policy will remain in notReady state until it is given a valid policy type (see hpicfGppcNpPolicyType). A row in the named policy table can not be deleted if the named policy is referenced by a row in the application control table. The application control entries that refer to this row must be deleted before this row can be deleted.')
hpicfGppcPolicyRulesTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4), )
if mibBuilder.loadTexts: hpicfGppcPolicyRulesTable.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcPolicyRulesTable.setDescription('The policy rules table. A policy can consist of multiple rules. All of the rules of a policy are listed in this table. Each rule consists of a string and a numeric identifier - the rule id.')
hpicfGppcPolicyRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1), ).setIndexNames((0, "HP-ICF-GPPC-MIB", "hpicfGppcNpPolicyName"), (0, "HP-ICF-GPPC-MIB", "hpicfGppcPrRuleId"))
if mibBuilder.loadTexts: hpicfGppcPolicyRulesEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcPolicyRulesEntry.setDescription('An entry in the policy rules table.')
hpicfGppcPrRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: hpicfGppcPrRuleId.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcPrRuleId.setDescription('Numeric identifier of the rule. The rules in a policy are processed sequentially in increasing order of their rule ids. These numeric ids are generated by the application that creates the policy. Rules within a policy have unique rule ids.')
hpicfGppcPrPolicyRule = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcPrPolicyRule.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcPrPolicyRule.setDescription('Rule string. This is a string that represents one rule in the policy. A policy can consist of one or many rules.')
hpicfGppcPrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfGppcPrRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcPrRowStatus.setDescription('Status of this row. A rule must have an active row status in order to take effect. Only active rules within the named policy are applied when an application applies the policy. It is possible to use this row status as an on/off switch for enabling or disabling selected rules within a policy. A newly created rule will remain in notReady state until it is given a valid rule string (see hpicfGppcPrPolicyRule).')
hpicfGppcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 1))
hpicfGppcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 2))
hpicfGppcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 1, 1)).setObjects(("HP-ICF-GPPC-MIB", "hpicfGppcGroup"), ("HP-ICF-GPPC-MIB", "hpicfGppcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGppcMIBCompliance = hpicfGppcMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcMIBCompliance.setDescription('The compliance statement for HP routers implementing the HP-ICF-GPPC-MIB.')
hpicfGppcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 2, 1)).setObjects(("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressIfList"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap1k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap2k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap3k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap4k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressIfList"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap1k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap2k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap3k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap4k"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcExpPolicy"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcExpString"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcLastErrorCode"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcLastErrorString"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcRowAdminStatus"), ("HP-ICF-GPPC-MIB", "hpicfGppcAcRowStatus"), ("HP-ICF-GPPC-MIB", "hpicfGppcNpPolicyType"), ("HP-ICF-GPPC-MIB", "hpicfGppcNpRowStatus"), ("HP-ICF-GPPC-MIB", "hpicfGppcPrPolicyRule"), ("HP-ICF-GPPC-MIB", "hpicfGppcPrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGppcGroup = hpicfGppcGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfGppcGroup.setDescription('A collection of HP proprietary objects to support GPPC.')
mibBuilder.exportSymbols("HP-ICF-GPPC-MIB", hpicfGppcMIBCompliances=hpicfGppcMIBCompliances, hpicfGppcAcAppInstance=hpicfGppcAcAppInstance, hpicfGppcAcEgressVlanMap1k=hpicfGppcAcEgressVlanMap1k, hpicfGppcAcLastErrorCode=hpicfGppcAcLastErrorCode, hpicfGppcMIB=hpicfGppcMIB, hpicfGppcMIBCompliance=hpicfGppcMIBCompliance, hpicfGppcAcEgressVlanMap3k=hpicfGppcAcEgressVlanMap3k, hpicfGppcAcExpString=hpicfGppcAcExpString, hpicfGppcAcRowStatus=hpicfGppcAcRowStatus, hpicfGppcAcEgressVlanMap4k=hpicfGppcAcEgressVlanMap4k, hpicfGppcAppControlEntry=hpicfGppcAppControlEntry, hpicfGppcNpPolicyName=hpicfGppcNpPolicyName, hpicfGppcNamedPolicyTable=hpicfGppcNamedPolicyTable, hpicfGppcAppControlTable=hpicfGppcAppControlTable, hpicfGppcAcIngressVlanMap1k=hpicfGppcAcIngressVlanMap1k, hpicfGppcPrPolicyRule=hpicfGppcPrPolicyRule, hpicfGppcNpPolicyType=hpicfGppcNpPolicyType, hpicfGppcGroup=hpicfGppcGroup, hpicfGppcAcAppName=hpicfGppcAcAppName, hpicfGppcConformance=hpicfGppcConformance, hpicfGppcAcExpPolicy=hpicfGppcAcExpPolicy, PYSNMP_MODULE_ID=hpicfGppcMIB, hpicfGppcNamedPolicyEntry=hpicfGppcNamedPolicyEntry, hpicfGppcNpRowStatus=hpicfGppcNpRowStatus, hpicfGppcPolicyRulesTable=hpicfGppcPolicyRulesTable, hpicfGppcPrRowStatus=hpicfGppcPrRowStatus, hpicfGppcAcEgressIfList=hpicfGppcAcEgressIfList, hpicfGppcAcPolicyName=hpicfGppcAcPolicyName, hpicfGppcAcLastErrorString=hpicfGppcAcLastErrorString, hpicfGppcPolicyRulesEntry=hpicfGppcPolicyRulesEntry, hpicfGppcAcIngressVlanMap4k=hpicfGppcAcIngressVlanMap4k, hpicfGppcAcIngressVlanMap2k=hpicfGppcAcIngressVlanMap2k, hpicfGppcAcEgressVlanMap2k=hpicfGppcAcEgressVlanMap2k, hpicfGppcPrRuleId=hpicfGppcPrRuleId, hpicfGppcAcIngressIfList=hpicfGppcAcIngressIfList, hpicfGppcMIBGroups=hpicfGppcMIBGroups, HpicfGppcPolicyName=HpicfGppcPolicyName, hpicfGppcAcRowAdminStatus=hpicfGppcAcRowAdminStatus, hpicfGppcAcIngressVlanMap3k=hpicfGppcAcIngressVlanMap3k)
