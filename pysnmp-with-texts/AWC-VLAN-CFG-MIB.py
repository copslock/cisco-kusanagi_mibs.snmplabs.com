#
# PySNMP MIB module AWC-VLAN-CFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AWC-VLAN-CFG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
WEPKeytype128, AwcDot11MicAlgorithm, AwcPolId, awcVx, AwcVlanId, AwcDot11WEPKeyPermuteAlgorithm, AwcPfPriority = mibBuilder.importSymbols("AWCVX-MIB", "WEPKeytype128", "AwcDot11MicAlgorithm", "AwcPolId", "awcVx", "AwcVlanId", "AwcDot11WEPKeyPermuteAlgorithm", "AwcPfPriority")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Gauge32, TimeTicks, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Bits, ObjectIdentity, ModuleIdentity, Counter64, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "Counter64", "Integer32", "MibIdentifier")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
awcVlanCfgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 522, 3, 21))
awcVlanCfgMIB.setRevisions(('2001-07-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: awcVlanCfgMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: awcVlanCfgMIB.setLastUpdated('200209060000Z')
if mibBuilder.loadTexts: awcVlanCfgMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: awcVlanCfgMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aironet@cisco.com')
if mibBuilder.loadTexts: awcVlanCfgMIB.setDescription('Aironet products VLAN Configuration MIB.')
awcVlanCfgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 522, 3, 21, 1))
class AwcVlanIndex(TextualConvention, Unsigned32):
    description = 'A value used to index per-VLAN tables. Represents an IEEE 802.1Q VLAN-ID with global scope within a given bridged domain (see AwcVlanId textual convention). The value 4095 indicates that the conceptual row applies to non-VLAN-tagged frames (though it would be more directly representative of the packet format, 0 can not be used for this purpose, per SNMP conventions).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4095)

class AwcVlanEncapType(TextualConvention, Integer32):
    description = 'The 802.1Q encapsulation mode. Valid values are: dot1qDisabled (1), Disabled dot1qPriority (2) 802.1Q Priority Tagging dot1qHybrid (3), 802.1Q VLAN Hybrid Trunk dot1qTrunk (4) 802.1Q VLAN Trunk The default value is normally Disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dot1qDisabled", 1), ("dot1qPriority", 2), ("dot1qHybrid", 3), ("dot1qTrunk", 4))

awcMaxVlanIds = MibScalar((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: awcMaxVlanIds.setStatus('current')
if mibBuilder.loadTexts: awcMaxVlanIds.setDescription('The Maximum number of discrete VLAN IDs supported. The VLAN IDs need not be consecutive.')
awcVlanEncapMode = MibScalar((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 2), AwcVlanEncapType().clone('dot1qDisabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: awcVlanEncapMode.setStatus('current')
if mibBuilder.loadTexts: awcVlanEncapMode.setDescription('The encapsulation mode setting controls transmit tagging logic for all ports. The value of this object is derived from other settings within the VLAN MIB.')
awcNativeVlanId = MibScalar((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 3), AwcVlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awcNativeVlanId.setStatus('current')
if mibBuilder.loadTexts: awcNativeVlanId.setDescription('Native VLAN ID for the device. The default Native VLAN ID is 0, for no VLAN ID. If the device is attached to an Ethernet bridge/switch VLAN port then a non-zero Native VLAN ID must match the Port VLAN ID of the bridge/switch port. The Native VLAN ID is the default VLAN ID for frames that are not otherwise associated with a VLAN ID.')
awcVlanAllowEncrypted = MibScalar((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awcVlanAllowEncrypted.setStatus('current')
if mibBuilder.loadTexts: awcVlanAllowEncrypted.setDescription('When this attribute is true, the STA shall indicate at the MAC service interface received MSDUs regardless of the setting of the WEP subfield of the Frame Control field, so long as no other VLAN parameters necessitate use of encryption. The default value of this attribute shall be true. The general use for awcVlanAllowEncrypted to be true even when no static WEP keys are set for a VLAN is to allow a station to utilize EAP authentication to encrypt directed packets, even while multicast packets are unencrypted.')
awcVlanAnyEnabled = MibScalar((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awcVlanAnyEnabled.setStatus('current')
if mibBuilder.loadTexts: awcVlanAnyEnabled.setDescription('When this attribute is true, VLAN operation of the system is enabled when any awcVlanEnabled value is true. When this attribute is false, VLAN operation is disabled. The awcVlanAnyEnabled thus acts as a master switch to enable or disable VLAN operation.')
awcVlanCfgTable = MibTable((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6), )
if mibBuilder.loadTexts: awcVlanCfgTable.setStatus('current')
if mibBuilder.loadTexts: awcVlanCfgTable.setDescription('A table used for configuring and managing VLANS.')
awcVlanCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1), ).setIndexNames((0, "AWC-VLAN-CFG-MIB", "awcVlanIndex"))
if mibBuilder.loadTexts: awcVlanCfgEntry.setStatus('current')
if mibBuilder.loadTexts: awcVlanCfgEntry.setDescription('VLAN table entry containing parameters for configuring and managing a particular VLAN.')
awcVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 1), AwcVlanIndex())
if mibBuilder.loadTexts: awcVlanIndex.setStatus('current')
if mibBuilder.loadTexts: awcVlanIndex.setDescription('VLAN ID to which the parameters in this conceptual row shall be applied. If 4095, the parameters in this conceptual row shall be applied to non-VLAN-tagged frames.')
awcVlanPolId = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 2), AwcPolId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanPolId.setStatus('current')
if mibBuilder.loadTexts: awcVlanPolId.setDescription('Default Policy Group Identifier for hosts occupying this VLAN.')
awcVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanEnabled.setStatus('current')
if mibBuilder.loadTexts: awcVlanEnabled.setDescription('If true, this VLAN is enabled on all trunk and hybrid ports. If false, this VLAN is disabled on all ports.')
awcVlanNUcastKeyRotationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000000))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanNUcastKeyRotationInterval.setStatus('current')
if mibBuilder.loadTexts: awcVlanNUcastKeyRotationInterval.setDescription('WEP key rotation period. 0 indicates no key rotation.')
awcVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: awcVlanRowStatus.setDescription('Used for creating/deleting conceptual rows in this table.')
awcVlanMicAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 6), AwcDot11MicAlgorithm().clone('micNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanMicAlgorithm.setStatus('current')
if mibBuilder.loadTexts: awcVlanMicAlgorithm.setDescription('Auxiliary Message Integrity Check (MIC) calculated on WEP-encoded packets of stations assigned to this VLAN. This object is not applicable for the reserved VLAN 4095.')
awcVlanWEPKeyPermuteAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 7), AwcDot11WEPKeyPermuteAlgorithm().clone('wepPermuteNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanWEPKeyPermuteAlgorithm.setStatus('current')
if mibBuilder.loadTexts: awcVlanWEPKeyPermuteAlgorithm.setDescription('Function through which the WEP encryption key is permuted between key renewal periods for stations assigned to this VLAN. This object is not applicable for the reserved VLAN 4095.')
awcVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 8), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanName.setStatus('current')
if mibBuilder.loadTexts: awcVlanName.setDescription('Descriptive textual name for the VLAN.')
awcVlanDefaultUserPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 9), AwcPfPriority().clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanDefaultUserPriority.setStatus('current')
if mibBuilder.loadTexts: awcVlanDefaultUserPriority.setDescription('Designation of the priority assigned to packets transmitted over this VLAN, if no other filter or classification rule has yet assigned a priority.')
awcVlanAlert = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: awcVlanAlert.setStatus('current')
if mibBuilder.loadTexts: awcVlanAlert.setDescription('Should an alert be registered when a packet on this VLAN is observed?')
awcVlanNUcastKeyTable = MibTable((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7), )
if mibBuilder.loadTexts: awcVlanNUcastKeyTable.setStatus('current')
if mibBuilder.loadTexts: awcVlanNUcastKeyTable.setDescription('Default Shared WEP Keys for all 802.11 packets transmitted and received as non-VLAN-tagged frames over a port with the Port VLAN ID specified as awcVlanIndex. If WEP encryption is enabled for transmitted 802.11 frames, then the set of 1 to 4 default shared WEP keys are used to encrypt transmitted 802.11 broadcast/multicast frames associated with the Port VLAN ID. The shared WEP keys are also used to encrypt/decrypt unicast frames, associated with the Port VLAN ID, if an individual session key is not defined for the target station address.')
awcVlanNUcastKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1), ).setIndexNames((0, "AWC-VLAN-CFG-MIB", "awcVlanIndex"), (0, "AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyIndex"))
if mibBuilder.loadTexts: awcVlanNUcastKeyEntry.setStatus('current')
if mibBuilder.loadTexts: awcVlanNUcastKeyEntry.setDescription('An entry in the awcVlanNUcastKeyTable table.')
awcVlanNUcastKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: awcVlanNUcastKeyIndex.setStatus('current')
if mibBuilder.loadTexts: awcVlanNUcastKeyIndex.setDescription('802.11 WEP Key Index, + 1, used when transmitting or receiving frames with this key.')
awcVlanNUcastKeyLen = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awcVlanNUcastKeyLen.setStatus('current')
if mibBuilder.loadTexts: awcVlanNUcastKeyLen.setDescription('Length in octets of awcVlanNUcastKeyValue. Common values are 5 for 40-bit WEP and 13 for 128-bit WEP. A value of 0 means that the key is not set.')
awcVlanNUcastKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1, 3), WEPKeytype128()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awcVlanNUcastKeyValue.setStatus('current')
if mibBuilder.loadTexts: awcVlanNUcastKeyValue.setDescription('A WEP default secret key value. The value is write-only (attempt to read will result in return of zero-length string).')
awcVlanAllowUnencryptedVlanId = MibScalar((1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 8), AwcVlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: awcVlanAllowUnencryptedVlanId.setStatus('current')
if mibBuilder.loadTexts: awcVlanAllowUnencryptedVlanId.setDescription('Single VLAN ID on which unencrypted packets are allowed. The default Unencrypted VLAN ID is 0, meaning that all VLANs require full encryption.')
awcVlanCfgNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 522, 3, 21, 2))
awcVlanCfgConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 522, 3, 21, 3))
awcVlanCfgCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 1))
awcVlanCfgGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 2))
awcVlanCfgCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 1, 1)).setObjects(("AWC-VLAN-CFG-MIB", "awcVlanCfgObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    awcVlanCfgCompliance = awcVlanCfgCompliance.setStatus('current')
if mibBuilder.loadTexts: awcVlanCfgCompliance.setDescription('The compliance statement for the awcVlanCfgMIB group.')
awcVlanCfgObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 2, 1)).setObjects(("AWC-VLAN-CFG-MIB", "awcMaxVlanIds"), ("AWC-VLAN-CFG-MIB", "awcVlanEncapMode"), ("AWC-VLAN-CFG-MIB", "awcNativeVlanId"), ("AWC-VLAN-CFG-MIB", "awcVlanAllowEncrypted"), ("AWC-VLAN-CFG-MIB", "awcVlanPolId"), ("AWC-VLAN-CFG-MIB", "awcVlanEnabled"), ("AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyRotationInterval"), ("AWC-VLAN-CFG-MIB", "awcVlanRowStatus"), ("AWC-VLAN-CFG-MIB", "awcVlanMicAlgorithm"), ("AWC-VLAN-CFG-MIB", "awcVlanWEPKeyPermuteAlgorithm"), ("AWC-VLAN-CFG-MIB", "awcVlanName"), ("AWC-VLAN-CFG-MIB", "awcVlanDefaultUserPriority"), ("AWC-VLAN-CFG-MIB", "awcVlanAlert"), ("AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyLen"), ("AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyValue"), ("AWC-VLAN-CFG-MIB", "awcVlanAllowUnencryptedVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    awcVlanCfgObjectsGroup = awcVlanCfgObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: awcVlanCfgObjectsGroup.setDescription('')
mibBuilder.exportSymbols("AWC-VLAN-CFG-MIB", awcVlanAllowEncrypted=awcVlanAllowEncrypted, awcVlanCfgEntry=awcVlanCfgEntry, awcVlanCfgMIB=awcVlanCfgMIB, awcVlanCfgNotifications=awcVlanCfgNotifications, awcVlanNUcastKeyTable=awcVlanNUcastKeyTable, AwcVlanEncapType=AwcVlanEncapType, PYSNMP_MODULE_ID=awcVlanCfgMIB, awcVlanNUcastKeyIndex=awcVlanNUcastKeyIndex, awcVlanCfgGroups=awcVlanCfgGroups, awcVlanRowStatus=awcVlanRowStatus, awcVlanAnyEnabled=awcVlanAnyEnabled, awcVlanWEPKeyPermuteAlgorithm=awcVlanWEPKeyPermuteAlgorithm, awcVlanDefaultUserPriority=awcVlanDefaultUserPriority, awcVlanNUcastKeyLen=awcVlanNUcastKeyLen, awcVlanEnabled=awcVlanEnabled, awcVlanNUcastKeyRotationInterval=awcVlanNUcastKeyRotationInterval, awcVlanIndex=awcVlanIndex, awcVlanCfgCompliance=awcVlanCfgCompliance, awcVlanPolId=awcVlanPolId, awcVlanAllowUnencryptedVlanId=awcVlanAllowUnencryptedVlanId, awcVlanMicAlgorithm=awcVlanMicAlgorithm, awcVlanEncapMode=awcVlanEncapMode, awcVlanCfgCompliances=awcVlanCfgCompliances, awcMaxVlanIds=awcMaxVlanIds, awcVlanNUcastKeyValue=awcVlanNUcastKeyValue, awcNativeVlanId=awcNativeVlanId, awcVlanAlert=awcVlanAlert, awcVlanCfgObjects=awcVlanCfgObjects, awcVlanCfgObjectsGroup=awcVlanCfgObjectsGroup, awcVlanName=awcVlanName, awcVlanCfgTable=awcVlanCfgTable, awcVlanNUcastKeyEntry=awcVlanNUcastKeyEntry, awcVlanCfgConformance=awcVlanCfgConformance, AwcVlanIndex=AwcVlanIndex)
