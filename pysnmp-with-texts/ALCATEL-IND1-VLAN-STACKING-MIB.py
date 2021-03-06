#
# PySNMP MIB module ALCATEL-IND1-VLAN-STACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-VLAN-STACKING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:20:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1VlanStackingMgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1VlanStackingMgt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, NotificationType, Unsigned32, TimeTicks, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ModuleIdentity, Counter32, Gauge32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "MibIdentifier")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
alcatelIND1VLANStackingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1))
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIB.setDescription('The parameters for configuration of the VLAN Stacking feature, including the association between ports and svlans. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2006 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1VLANStackingMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1))
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBObjects.setDescription('Branch For VLAN Stacking Managed Objects.')
alcatelIND1VLANStackingMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 2))
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBConformance.setDescription('Branch For VLAN Stacking Conformance Information.')
alcatelIND1VLANStackingMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBGroups.setDescription('Branch For VLAN Stacking Units Of Conformance.')
alcatelIND1VLANStackingMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBCompliances.setDescription('Branch For VLAN Stacking Compliance Statements.')
alaVlanStackingPort = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1))
alaVstkPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaVstkPortTable.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortTable.setDescription('A table that contains port-specific information for the VLAN Stacking feature. An entry in this table is created when a port is configured with VLAN stacking capability, OR when a port is configured with a specific vendor ethertype, a particular bridge protocol action.')
alaVstkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortNumber"))
if mibBuilder.loadTexts: alaVstkPortEntry.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortEntry.setDescription('A VLAN Stacking port entry.')
alaVstkPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVstkPortNumber.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortNumber.setDescription('The port ifindex of the port for which this entry contains VLAN Stacking management information. ')
alaVstkPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("userCustomer", 1), ("userProvider", 2), ("network", 3))).clone('userCustomer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortType.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortType.setDescription('The type of this VLAN Stacking port. User-customer (1) is a VLAN Stacking user port connected to customer network. User-provider (2) is a VLAN Stacking user port used to run provider management traffic. Network (2) indicates a network facing port.')
alaVstkPortVendorTpid = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 3), Integer32().clone(34984)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortVendorTpid.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortVendorTpid.setDescription('The TPID for this port. It is used for the incoming data traffic parsing and it is substituted to the 802.1Q standard Tpid for the outgoing data traffic. This is used for compatibility with other vendor equipment. The default value is the standard value 0x88a8.')
alaVstkPortBpduTreatment = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flooded", 1), ("dropped", 2))).clone('flooded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortBpduTreatment.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortBpduTreatment.setDescription("The customer bpdu treatment for this port. It defines the type of processing applied to the user's bridge protocol data unit. The bridge protocol treatment (flooded) floods any user's bridge protocol data unit to all user ports and network ports on the same SVLAN. The bridge protocol (dropped) drops any user's bridge protocol data unit.")
alaVstkPortAcceptFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tagged", 1), ("untagged", 2), ("all", 3))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortAcceptFrameType.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortAcceptFrameType.setDescription('The acceptable frame types on this port.')
alaVstkPortLookupMiss = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("default", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortLookupMiss.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortLookupMiss.setDescription('Treatment of tagged packets upon vlan lookup miss. Drop (1) means that on lookup miss the packets will be dropped. Default (2) means that on lookup miss the default SVLAN for that port will be used to tunnel the packets. This is significant only for user port.')
alaVstkPortDefaultSvlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortDefaultSvlan.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortDefaultSvlan.setDescription('The default svlan of this port.')
alaVstkPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortRowStatus.setDescription('The status of this table entry. The supported value supported for set are createAndGo (4) and destroy(6), to create or remove a vlan-stacking port.')
alaVstkPortLegacyStpBpdu = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkPortLegacyStpBpdu.setStatus('current')
if mibBuilder.loadTexts: alaVstkPortLegacyStpBpdu.setDescription('The legacy STP BPDU treatment for this port. It defines the type of processing applied to STP legacy BPDUs on network ports. Legacy BPDU refer to conventional/customer BPDUs with MAC address 01:80:c2:00:00:00 and its processing on network ports can be enabled/disabled by this object.By default the value is disabled i.e provider MAC BPDU with MAC address 01:80:c2:00:00:08 would be processed at network ports.')
alaVlanStackingSvlanPort = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2))
alaVstkSvlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2, 1), )
if mibBuilder.loadTexts: alaVstkSvlanPortTable.setStatus('current')
if mibBuilder.loadTexts: alaVstkSvlanPortTable.setDescription('A table that contains svlan/ipmvlan-port association for the VLAN Stacking feature.')
alaVstkSvlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortSvlanNumber"), (0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortPortNumber"), (0, "ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortCvlanNumber"))
if mibBuilder.loadTexts: alaVstkSvlanPortEntry.setStatus('current')
if mibBuilder.loadTexts: alaVstkSvlanPortEntry.setDescription('The svlan/ipmvlan-port association.')
alaVstkSvlanPortSvlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVstkSvlanPortSvlanNumber.setStatus('current')
if mibBuilder.loadTexts: alaVstkSvlanPortSvlanNumber.setDescription('Number identifying the svlan/ipmvlan.')
alaVstkSvlanPortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVstkSvlanPortPortNumber.setStatus('current')
if mibBuilder.loadTexts: alaVstkSvlanPortPortNumber.setDescription('The port ifindex of the port associated to the svlan/ipmvlan.')
alaVstkSvlanPortCvlanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVstkSvlanPortCvlanNumber.setStatus('current')
if mibBuilder.loadTexts: alaVstkSvlanPortCvlanNumber.setDescription('The customer vlan id associated to the svlan/ipmvlan.')
alaVstkSvlanPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("doubleTag", 1), ("translate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkSvlanPortMode.setStatus('current')
if mibBuilder.loadTexts: alaVstkSvlanPortMode.setDescription('The vlan stacking mode: double tagging (1) or vlan translation/mapping (2). Only translation mode is valid in case of IPM Vlans')
alaVstkSvlanPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVstkSvlanPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaVstkSvlanPortRowStatus.setDescription('The status of this table entry. The supported value for set are createAndGo (4) and destroy(6), to add or remove an svlan-port association.')
alcatelIND1VLANStackingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VLAN-STACKING-MIB", "vlanStackingPortGroup"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "vlanStackingSvlanPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1VLANStackingMIBCompliance = alcatelIND1VLANStackingMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VLANStackingMIBCompliance.setDescription('Compliance statement for VLAN Stacking.')
vlanStackingPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortNumber"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortType"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortVendorTpid"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortBpduTreatment"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortAcceptFrameType"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortLookupMiss"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortDefaultSvlan"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vlanStackingPortGroup = vlanStackingPortGroup.setStatus('current')
if mibBuilder.loadTexts: vlanStackingPortGroup.setDescription('Collection of objects for management of VLAN Stacking Ports.')
vlanStackingSvlanPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 37, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortSvlanNumber"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortPortNumber"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortCvlanNumber"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortMode"), ("ALCATEL-IND1-VLAN-STACKING-MIB", "alaVstkSvlanPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vlanStackingSvlanPortGroup = vlanStackingSvlanPortGroup.setStatus('current')
if mibBuilder.loadTexts: vlanStackingSvlanPortGroup.setDescription('Collection of objects for svlan-port associations.')
mibBuilder.exportSymbols("ALCATEL-IND1-VLAN-STACKING-MIB", vlanStackingPortGroup=vlanStackingPortGroup, alaVstkSvlanPortSvlanNumber=alaVstkSvlanPortSvlanNumber, alcatelIND1VLANStackingMIBGroups=alcatelIND1VLANStackingMIBGroups, alcatelIND1VLANStackingMIBCompliance=alcatelIND1VLANStackingMIBCompliance, PYSNMP_MODULE_ID=alcatelIND1VLANStackingMIB, alaVstkPortBpduTreatment=alaVstkPortBpduTreatment, alaVstkPortVendorTpid=alaVstkPortVendorTpid, alaVstkSvlanPortRowStatus=alaVstkSvlanPortRowStatus, vlanStackingSvlanPortGroup=vlanStackingSvlanPortGroup, alaVstkPortRowStatus=alaVstkPortRowStatus, alaVstkPortEntry=alaVstkPortEntry, alaVstkSvlanPortEntry=alaVstkSvlanPortEntry, alaVstkPortType=alaVstkPortType, alcatelIND1VLANStackingMIB=alcatelIND1VLANStackingMIB, alaVstkSvlanPortTable=alaVstkSvlanPortTable, alaVstkSvlanPortMode=alaVstkSvlanPortMode, alaVlanStackingPort=alaVlanStackingPort, alaVstkPortLookupMiss=alaVstkPortLookupMiss, alaVstkPortTable=alaVstkPortTable, alaVstkPortDefaultSvlan=alaVstkPortDefaultSvlan, alaVstkSvlanPortPortNumber=alaVstkSvlanPortPortNumber, alaVlanStackingSvlanPort=alaVlanStackingSvlanPort, alaVstkSvlanPortCvlanNumber=alaVstkSvlanPortCvlanNumber, alcatelIND1VLANStackingMIBConformance=alcatelIND1VLANStackingMIBConformance, alcatelIND1VLANStackingMIBCompliances=alcatelIND1VLANStackingMIBCompliances, alaVstkPortAcceptFrameType=alaVstkPortAcceptFrameType, alaVstkPortLegacyStpBpdu=alaVstkPortLegacyStpBpdu, alcatelIND1VLANStackingMIBObjects=alcatelIND1VLANStackingMIBObjects, alaVstkPortNumber=alaVstkPortNumber)
