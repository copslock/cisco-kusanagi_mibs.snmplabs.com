#
# PySNMP MIB module HPN-ICF-SMLK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-SMLK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:41:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, TimeTicks, iso, Counter64, Integer32, Bits, ModuleIdentity, IpAddress, ObjectIdentity, NotificationType, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "TimeTicks", "iso", "Counter64", "Integer32", "Bits", "ModuleIdentity", "IpAddress", "ObjectIdentity", "NotificationType", "Counter32", "MibIdentifier")
RowStatus, TextualConvention, DateAndTime, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DateAndTime", "MacAddress", "DisplayString")
hpnicfSmlk = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147))
hpnicfSmlk.setRevisions(('2014-07-23 15:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfSmlk.setRevisionsDescriptions(('Initial revision of the Smart Link MIB module.',))
if mibBuilder.loadTexts: hpnicfSmlk.setLastUpdated('201407231503Z')
if mibBuilder.loadTexts: hpnicfSmlk.setOrganization('')
if mibBuilder.loadTexts: hpnicfSmlk.setContactInfo('')
if mibBuilder.loadTexts: hpnicfSmlk.setDescription('This MIB defines objects for managing Smart Link. Smart Link is a feature developed to address the slow convergence issue with STP. It provides link redundancy and fast convergence in a dual uplink network, allowing the backup link to take over quickly when the primary link fails.')
hpnicfSmlkObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1))
hpnicfSmlkGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1), )
if mibBuilder.loadTexts: hpnicfSmlkGroupTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkGroupTable.setDescription('A list of entries of a smart link group.')
hpnicfSmlkGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkGroupID"))
if mibBuilder.loadTexts: hpnicfSmlkGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkGroupEntry.setDescription('A list of parameters that describe a smart link group.')
hpnicfSmlkGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSmlkGroupID.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkGroupID.setDescription('An index that uniquely identifies an entry in the smart link group table.')
hpnicfSmlkDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSmlkDeviceID.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkDeviceID.setDescription('Device ID of a smart link group. The device ID is the bridge MAC of the device.')
hpnicfSmlkPreemptionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("role", 2), ("speed", 3))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkPreemptionMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPreemptionMode.setDescription('Preemption mode of a smart link group.')
hpnicfSmlkSpeedThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkSpeedThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkSpeedThreshold.setDescription("Speed threshold for a smart link group in speed mode. This object is valid only when the value of hpnicfSmlkPreemptionMode is 'speed'.")
hpnicfSmlkPreemptionDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkPreemptionDelay.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPreemptionDelay.setDescription('Preemption delay for a smart link group, in the range of 0 to 300 seconds.')
hpnicfSmlkControlVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(65535, 65535), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkControlVlanID.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkControlVlanID.setDescription('Index of the control VLAN specified for a smart link group. The value 65535 indicates that the control VLAN has not been configured.')
hpnicfSmlkInstanceListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkInstanceListLow.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkInstanceListLow.setDescription("Each octet contained in this value specifies an eight-instance group, with the first octet specifying instances 0 through 7, the second octet specifying instances 8 through 15, and so on. Within each octet, the most significant bit represents the highest numbered instance, and the least significant bit represents the lowest numbered instance. Each instance to which the protected VLANs of a smart link group are mapped corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the VLANs mapped to the instance are protected VLANs of the smart link group. The VLANs mapped to the instance are not protected VLANs if the corresponding bit has a value of '0'. The value of this object must be set with hpnicfSmlkInstanceListHigh at the same time when a SET operation is performed.")
hpnicfSmlkInstanceListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkInstanceListHigh.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkInstanceListHigh.setDescription("Each octet contained in this value specifies an eight-instance group, with the first octet specifying instances 2048 through 2055, the second octet specifying instances 2056 through 2063, and so on. Within each octet, the most significant bit represents the highest numbered instance, and the least significant bit represents the lowest numbered instance. The most significant bit of the last octet is invalid. Each instance to which the protected VLANs of a smart link group are mapped corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the VLANs mapped to the instance are protected VLANs of the smart link group. The VLANs mapped to the instance are not protected VLANs if the corresponding bit has a value of '0'. The value of this object must be set with hpnicfSmlkInstanceListLow at the same time when a SET operation is performed.")
hpnicfSmlkGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkGroupRowStatus.setDescription('This object is responsible for managing creation, deletion, and modification of rows. The rows support active status, CreatAndGo, and destroy operations.')
hpnicfSmlkPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2), )
if mibBuilder.loadTexts: hpnicfSmlkPortTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPortTable.setDescription('A list of port entries of a smart link group.')
hpnicfSmlkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkGroupID"), (0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkPortIfIndex"))
if mibBuilder.loadTexts: hpnicfSmlkPortEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPortEntry.setDescription('A list of parameters that describe a port to be added to a smart link group.')
hpnicfSmlkPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfSmlkPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPortIfIndex.setDescription('IfIndex of a port in a smart link group.')
hpnicfSmlkPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkPortRole.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPortRole.setDescription('Role of a port in a smart link group.')
hpnicfSmlkPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSmlkPortStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPortStatus.setDescription('Status of a port in a smart link group.')
hpnicfSmlkFlushCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSmlkFlushCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkFlushCount.setDescription('Number of transmitted flush messages.')
hpnicfSmlkLastFlushTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSmlkLastFlushTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkLastFlushTime.setDescription('Time when the last flush message was transmitted.')
hpnicfSmlkPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfSmlkPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkPortRowStatus.setDescription('This object is responsible for managing creation, deletion, and modification of rows. The rows support active status, CreatAndGo, and destroy operations.')
hpnicfSmlkFlushEnableTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3), )
if mibBuilder.loadTexts: hpnicfSmlkFlushEnableTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkFlushEnableTable.setDescription('A list of ports on which flush message receiving is enabled.')
hpnicfSmlkFlushEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-SMLK-MIB", "hpnicfSmlkIfIndex"))
if mibBuilder.loadTexts: hpnicfSmlkFlushEnableEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkFlushEnableEntry.setDescription('A list of parameters that describe a port on which flush message receiving is enabled.')
hpnicfSmlkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpnicfSmlkIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkIfIndex.setDescription('IfIndex of a port on which flush message receiving is enabled.')
hpnicfSmlkControlVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSmlkControlVlanListLow.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkControlVlanListLow.setDescription('Specifies the control VLANs used for receiving flush messages. The VLAN ID range, described by bitmap, is from 1 to 2048. The length of bitmap is 256 in bytes. Each octet within this value specifies a set of eight VLANs, with the first octet specifying VLANs 1 through 8, the second octet specifying VLANs 9 through 16, and so on. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN.')
hpnicfSmlkControlVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfSmlkControlVlanListHigh.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkControlVlanListHigh.setDescription('Specifies the control VLANs used for receiving flush messages. The VLAN ID range, described by bitmap, is from 2049 to 4094. The length of bitmap is 256 in bytes. Each octet within this value specifies a set of eight VLANs, with the first octet specifying VLANs 2049 through 2056, the second octet specifying VLANs 2057 through 2064, and so on. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN.')
hpnicfSmlkTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 2))
hpnicfSmlkTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 2, 0))
hpnicfSmlkGroupLinkActive = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 147, 2, 0, 1)).setObjects(("HPN-ICF-SMLK-MIB", "hpnicfSmlkGroupID"), ("HPN-ICF-SMLK-MIB", "hpnicfSmlkPortIfIndex"))
if mibBuilder.loadTexts: hpnicfSmlkGroupLinkActive.setStatus('current')
if mibBuilder.loadTexts: hpnicfSmlkGroupLinkActive.setDescription('A trap message is generated when the status of a port in a smart link group changes to active.')
mibBuilder.exportSymbols("HPN-ICF-SMLK-MIB", hpnicfSmlkTrapPrefix=hpnicfSmlkTrapPrefix, hpnicfSmlkPreemptionDelay=hpnicfSmlkPreemptionDelay, hpnicfSmlkFlushEnableTable=hpnicfSmlkFlushEnableTable, hpnicfSmlkPreemptionMode=hpnicfSmlkPreemptionMode, hpnicfSmlkDeviceID=hpnicfSmlkDeviceID, hpnicfSmlkControlVlanListLow=hpnicfSmlkControlVlanListLow, hpnicfSmlkSpeedThreshold=hpnicfSmlkSpeedThreshold, hpnicfSmlkFlushCount=hpnicfSmlkFlushCount, hpnicfSmlkGroupLinkActive=hpnicfSmlkGroupLinkActive, hpnicfSmlkGroupID=hpnicfSmlkGroupID, hpnicfSmlkInstanceListHigh=hpnicfSmlkInstanceListHigh, hpnicfSmlkGroupRowStatus=hpnicfSmlkGroupRowStatus, hpnicfSmlkPortTable=hpnicfSmlkPortTable, hpnicfSmlkPortEntry=hpnicfSmlkPortEntry, hpnicfSmlkControlVlanListHigh=hpnicfSmlkControlVlanListHigh, hpnicfSmlkControlVlanID=hpnicfSmlkControlVlanID, hpnicfSmlkGroupEntry=hpnicfSmlkGroupEntry, PYSNMP_MODULE_ID=hpnicfSmlk, hpnicfSmlkPortStatus=hpnicfSmlkPortStatus, hpnicfSmlkIfIndex=hpnicfSmlkIfIndex, hpnicfSmlkLastFlushTime=hpnicfSmlkLastFlushTime, hpnicfSmlkFlushEnableEntry=hpnicfSmlkFlushEnableEntry, hpnicfSmlkPortIfIndex=hpnicfSmlkPortIfIndex, hpnicfSmlkObject=hpnicfSmlkObject, hpnicfSmlkPortRowStatus=hpnicfSmlkPortRowStatus, hpnicfSmlkGroupTable=hpnicfSmlkGroupTable, hpnicfSmlkTrap=hpnicfSmlkTrap, hpnicfSmlkInstanceListLow=hpnicfSmlkInstanceListLow, hpnicfSmlkPortRole=hpnicfSmlkPortRole, hpnicfSmlk=hpnicfSmlk)
