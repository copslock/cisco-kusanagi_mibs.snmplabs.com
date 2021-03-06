#
# PySNMP MIB module ALCATEL-IND1-ETHERNET-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-ETHERNET-OAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1EthernetOam, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1EthernetOam")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
Dot1agCfmMepIdOrZero, dot1agCfmMaIndex, dot1agCfmMdIndex, dot1agCfmMepEntry, Dot1agCfmMepId, dot1agCfmMepIdentifier = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMepIdOrZero", "dot1agCfmMaIndex", "dot1agCfmMdIndex", "dot1agCfmMepEntry", "Dot1agCfmMepId", "dot1agCfmMepIdentifier")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ObjectIdentity, ModuleIdentity, IpAddress, MibIdentifier, Bits, NotificationType, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibIdentifier", "Bits", "NotificationType", "Counter64", "Unsigned32")
TextualConvention, DisplayString, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "MacAddress")
alcatelIND1EoamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1))
alcatelIND1EoamMIB.setRevisions(('2009-09-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1EoamMIB.setRevisionsDescriptions(('Conectivity Fault Management module for managing IEEE 802.1ag. This CFM MIB extends standard draft 802.1ag 8.1. The set of objects defined in this MIB, do not duplicate, nor conflict with any MIB object definitions defined in the 802.1ag 7.0 draft MIB.',))
if mibBuilder.loadTexts: alcatelIND1EoamMIB.setLastUpdated('200909080000Z')
if mibBuilder.loadTexts: alcatelIND1EoamMIB.setOrganization('Alcatel - Architects Of An Internet World')
if mibBuilder.loadTexts: alcatelIND1EoamMIB.setContactInfo('Please consult with Customer Service to insure the most appropriate version of this document is used with the products in question: Alcatel Internetworking, Incorporated (Division 1, Formerly XYLAN Corporation) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://www.ind.alcatel.com File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1EoamMIB.setDescription('This module describes an authoritative enterprise- specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): For the Birds Of Prey Product Line Ethernet OAM for the Connectivity Fault Management. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2002 Alcatel Internetworking, Incorporated ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1CfmMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1))
if mibBuilder.loadTexts: alcatelIND1CfmMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1CfmMIBObjects.setDescription('Branch For Connectivity Fault Management (Ethernet OAM) Objects.')
alaCfmBase = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1))
alaCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2))
alaCfmDelayResult = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3))
alaCfmGlobalClearStats = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaCfmGlobalClearStats.setStatus('current')
if mibBuilder.loadTexts: alaCfmGlobalClearStats.setDescription('Defines the global clear statistics control for Ethernet OAM. The value reset (1) indicates that Ethernet OAM should clear all statistic counters related to all MEPs in the system. By default, this object contains a zero value.')
alaCfmGlobalOWDClear = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaCfmGlobalOWDClear.setStatus('current')
if mibBuilder.loadTexts: alaCfmGlobalOWDClear.setDescription('Defines the global clear of one-way-delay entries control for Ethernet OAM. The value reset (1) indicates that Ethernet OAM should remove all the one-way-delay entries in the delay result table. By default, this object contains a zero value.')
alaCfmGlobalTWDClear = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaCfmGlobalTWDClear.setStatus('current')
if mibBuilder.loadTexts: alaCfmGlobalTWDClear.setDescription('Defines the global clear of two-way-delay entries control for Ethernet OAM. The value reset (1) indicates that Ethernet OAM should remove all the two-way-delay entries in the delay result table. By default, this object contains a zero value.')
alaCfmMepTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1), )
if mibBuilder.loadTexts: alaCfmMepTable.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepTable.setDescription('This table augments the MEP table for clearing statistics based on MdIndex/MaIndex/MEPId. This table also contains the objects for initiating 1DM and DMM.')
alaCfmMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1), )
dot1agCfmMepEntry.registerAugmentions(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepEntry"))
alaCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: alaCfmMepEntry.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepEntry.setDescription('Each row entry in the alaCfmMepTable represents additional column for proprietary extension to the existing MEP table. It provides the facility to clear the statistics based on uniquely identified MEP. It also provides the facility to intiate 1DM and DMM')
alaCfmMepClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("reset", 1))).clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepClearStats.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepClearStats.setDescription('Reset all statistics parameters corresponding to this MEP. By default, this objects contains a zero value.')
alaCfmMepOWDTMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 2), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepOWDTMacAddress.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepOWDTMacAddress.setDescription("Specifies the MAC address used as a target for the One-Way-Delay Test (OWDT). Setting this object will trigger a One-Way-Delay test to the specified MAC address. The number of messages transmitted per initiation will be 2. Upon completion of the test, the MacAddress will revert to it's default value, indicating that another test is possible.")
alaCfmMepOWDTRMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 3), Dot1agCfmMepId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepOWDTRMepIdentifier.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepOWDTRMepIdentifier.setDescription('Specifies the Mep-Id assigned to the Remote MEP.')
alaCfmMepOWDTPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepOWDTPriority.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepOWDTPriority.setDescription('Specifies the priority used in the generated test frame for the One-Way-Delay test.')
alaCfmMepTWDTMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 5), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepTWDTMacAddress.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepTWDTMacAddress.setDescription("Specifies the MAC address used as a target for the Two-Way-Delay Test (TWDT). Setting this object will trigger a Two-Way-Delay test to the specified MAC address. The number of messages transmitted per initiation will be 2. Upon completion of the test, the MacAddress will revert to it's default value, indicating that another test is possible.")
alaCfmMepTWDTRMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 6), Dot1agCfmMepId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepTWDTRMepIdentifier.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepTWDTRMepIdentifier.setDescription('Specifies the Mep-Id assigned to the Remote MEP.')
alaCfmMepTWDTPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepTWDTPriority.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepTWDTPriority.setDescription('Specifies the priority used in the generated test frame for the Two-Way-Delay test.')
alaCfmMepRFPEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepRFPEnabled.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepRFPEnabled.setDescription('If set to true, Remote Fault Propagation will be enabled on the MEP.')
alaCfmMepPortStatusTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 9), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepPortStatusTlv.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepPortStatusTlv.setDescription('If set to true, Port Status Tlv will be configured in CCM.')
alaCfmMepIfStatusTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaCfmMepIfStatusTlv.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepIfStatusTlv.setDescription('If set to true, Interface Status Tlv will be configured in CCM.')
alaCfmDelayResultTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1), )
if mibBuilder.loadTexts: alaCfmDelayResultTable.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultTable.setDescription('Indicates the results of all the One-Way/Two-Way Delay Tests from the originating MAC addresses. This table is not persistent over reboots of the chassis.')
alaCfmDelayResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultType"), (0, "ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultRMepMacAddress"))
if mibBuilder.loadTexts: alaCfmDelayResultEntry.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultEntry.setDescription('The MEP delay result table.')
alaCfmDelayResultType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oneWayTest", 1), ("twoWayTest", 2))))
if mibBuilder.loadTexts: alaCfmDelayResultType.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultType.setDescription('Indicates the type of test this row details.')
alaCfmDelayResultRMepMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: alaCfmDelayResultRMepMacAddress.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultRMepMacAddress.setDescription('Indicates the MAC address of the Remote MEP.')
alaCfmDelayResultRMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 3), Dot1agCfmMepIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaCfmDelayResultRMepIdentifier.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultRMepIdentifier.setDescription("Indicates the Mep-Id of the Remote MEP. Valid only in the case of two-way delay. When initiated for a target Mep-Id contains the Mep-Id of the target, else if two-way delay initiated for a target mac-address contains '0'.")
alaCfmDelayResultTestDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 4), Integer32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: alaCfmDelayResultTestDelay.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultTestDelay.setDescription('Indicates the amount of time, measured in microseconds, from when the test-frame was transmitted to the time it was received minus the local processing time taken by the remote system.')
alaCfmDelayResultVariation = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 5), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: alaCfmDelayResultVariation.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultVariation.setDescription('Indicates the amount of time delay variation, measured in microseconds, from the two most recent time delay measurements')
alaCfmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2))
alaCfmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1))
alaCfmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 2))
alaCfmBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmGlobalClearStats"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmGlobalOWDClear"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmGlobalTWDClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaCfmBaseGroup = alaCfmBaseGroup.setStatus('current')
if mibBuilder.loadTexts: alaCfmBaseGroup.setDescription('Mandatory objects for the Base group')
alaCfmMepGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepClearStats"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepOWDTMacAddress"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepOWDTRMepIdentifier"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepOWDTPriority"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepTWDTMacAddress"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepTWDTRMepIdentifier"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepTWDTPriority"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepRFPEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaCfmMepGroup = alaCfmMepGroup.setStatus('current')
if mibBuilder.loadTexts: alaCfmMepGroup.setDescription('Mandatory objects for the MEP group. Proprietary extension to support statistics clearing and one-way and two-way delay tests.')
alaCfmDelayResultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultRMepIdentifier"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultTestDelay"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultVariation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaCfmDelayResultGroup = alaCfmDelayResultGroup.setStatus('current')
if mibBuilder.loadTexts: alaCfmDelayResultGroup.setDescription('Mandatory objects for the Delay Result Group.')
alaTlvGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepPortStatusTlv"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepIfStatusTlv"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaTlvGroup = alaTlvGroup.setStatus('current')
if mibBuilder.loadTexts: alaTlvGroup.setDescription('optional group')
alaCfmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmBaseGroup"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepGroup"), ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaCfmCompliance = alaCfmCompliance.setStatus('current')
if mibBuilder.loadTexts: alaCfmCompliance.setDescription('The compliance statement for support of CFM.')
mibBuilder.exportSymbols("ALCATEL-IND1-ETHERNET-OAM-MIB", alaCfmMepTWDTRMepIdentifier=alaCfmMepTWDTRMepIdentifier, alaCfmDelayResultVariation=alaCfmDelayResultVariation, alaCfmGroups=alaCfmGroups, alaCfmGlobalTWDClear=alaCfmGlobalTWDClear, alaCfmCompliances=alaCfmCompliances, alaCfmMepTWDTMacAddress=alaCfmMepTWDTMacAddress, alaCfmMepPortStatusTlv=alaCfmMepPortStatusTlv, alaCfmMepIfStatusTlv=alaCfmMepIfStatusTlv, alaCfmMepGroup=alaCfmMepGroup, alaCfmDelayResultRMepIdentifier=alaCfmDelayResultRMepIdentifier, alaCfmGlobalClearStats=alaCfmGlobalClearStats, alaCfmMepOWDTRMepIdentifier=alaCfmMepOWDTRMepIdentifier, PYSNMP_MODULE_ID=alcatelIND1EoamMIB, alaCfmBaseGroup=alaCfmBaseGroup, alaCfmCompliance=alaCfmCompliance, alcatelIND1CfmMIBObjects=alcatelIND1CfmMIBObjects, alaCfmMepEntry=alaCfmMepEntry, alaTlvGroup=alaTlvGroup, alaCfmMep=alaCfmMep, alcatelIND1EoamMIB=alcatelIND1EoamMIB, alaCfmDelayResultEntry=alaCfmDelayResultEntry, alaCfmDelayResult=alaCfmDelayResult, alaCfmMepTable=alaCfmMepTable, alaCfmDelayResultTable=alaCfmDelayResultTable, alaCfmMepRFPEnabled=alaCfmMepRFPEnabled, alaCfmDelayResultTestDelay=alaCfmDelayResultTestDelay, alaCfmDelayResultType=alaCfmDelayResultType, alaCfmMepTWDTPriority=alaCfmMepTWDTPriority, alaCfmMepClearStats=alaCfmMepClearStats, alaCfmMepOWDTMacAddress=alaCfmMepOWDTMacAddress, alaCfmMepOWDTPriority=alaCfmMepOWDTPriority, alaCfmDelayResultGroup=alaCfmDelayResultGroup, alaCfmGlobalOWDClear=alaCfmGlobalOWDClear, alaCfmConformance=alaCfmConformance, alaCfmDelayResultRMepMacAddress=alaCfmDelayResultRMepMacAddress, alaCfmBase=alaCfmBase)
