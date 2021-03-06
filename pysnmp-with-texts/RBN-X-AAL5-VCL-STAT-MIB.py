#
# PySNMP MIB module RBN-X-AAL5-VCL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-X-AAL5-VCL-STAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnExperiment, = mibBuilder.importSymbols("RBN-SMI", "rbnExperiment")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, Bits, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, Integer32, NotificationType, ObjectIdentity, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "Integer32", "NotificationType", "ObjectIdentity", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnXAal5VclStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 3, 1))
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setLastUpdated('9804171645Z')
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setOrganization('RedBack Networks, Inc.')
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setContactInfo(' RedBack Networks, Inc. Postal: 1389 Moffett Park Drive Sunnyvale, CA 94089-1134 USA Phone: +1 408 548 3500 Fax: +1 408 548 3599 E-mail: mib-info@RedBackNetworks.com')
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setDescription('The MIB for instrumenting statistics associated with an ATM VCL. This MIB is positioned in the RedBack Networks experimental MIB space because it mirrors MIB objects currently being developed by the IETF atommib Working Group, namely the atmAal5VclStatTable objects found in the ATM2-MIB (draft-ietf-atommib-atm2-XX.txt). At such time as the ATM2-MIB is placed on the IETF standards track, this MIB will be obsoleted in favor of the IETF one')
rbnXAal5VclStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1))
rbnXAtmAal5VclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1), )
if mibBuilder.loadTexts: rbnXAtmAal5VclStatTable.setStatus('current')
if mibBuilder.loadTexts: rbnXAtmAal5VclStatTable.setDescription('This table provides a collection of objects providing AAL5 configuration and performance statistics of a VCL.')
rbnXAtmAal5VclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: rbnXAtmAal5VclStatEntry.setStatus('current')
if mibBuilder.loadTexts: rbnXAtmAal5VclStatEntry.setDescription('Each entry in this table represents a VCL.')
rbnXAtmAal5VclInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclInPkts.setStatus('current')
if mibBuilder.loadTexts: rbnXAtmAal5VclInPkts.setDescription('The number of AAL5 CPCS PDUs received on the AAL5 VCC at the interface identified by the ifIndex.')
rbnXAtmAal5VclOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclOutPkts.setStatus('current')
if mibBuilder.loadTexts: rbnXAtmAal5VclOutPkts.setDescription('The number of AAL5 CPCS PDUs transmitted on the AAL5 VCC at the interface identified by the ifIndex.')
rbnXAtmAal5VclInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclInOctets.setStatus('current')
if mibBuilder.loadTexts: rbnXAtmAal5VclInOctets.setDescription('The number of octets contained in AAL5 CPCS PDUs received on the AAL5 VCC at the interface identified by the ifIndex.')
rbnXAtmAal5VclOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclOutOctets.setStatus('current')
if mibBuilder.loadTexts: rbnXAtmAal5VclOutOctets.setDescription('The number of octets contained in AAL5 CPCS PDUs transmitted on the AAL5 VCC at the interface identified by the ifIndex.')
rbnXAal5VclStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2))
rbnXAal5VclStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1))
rbnXAal5VclStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2))
rbnXAal5VclStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2, 1)).setObjects(("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAal5VclStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAal5VclStatMIBCompliance = rbnXAal5VclStatMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnXAal5VclStatMIBCompliance.setDescription('The compliance statement for RedBack Networks SNMP entities which represent AAL5 VCL statistics')
rbnXAal5VclStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1, 1)).setObjects(("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInPkts"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutPkts"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInOctets"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAal5VclStatGroup = rbnXAal5VclStatGroup.setStatus('current')
if mibBuilder.loadTexts: rbnXAal5VclStatGroup.setDescription('A collection of objects providing supplemental AAL5 VCL information beyond that supplied by IETF standards-track MIBs')
mibBuilder.exportSymbols("RBN-X-AAL5-VCL-STAT-MIB", rbnXAtmAal5VclOutOctets=rbnXAtmAal5VclOutOctets, rbnXAtmAal5VclStatEntry=rbnXAtmAal5VclStatEntry, rbnXAal5VclStatMIB=rbnXAal5VclStatMIB, rbnXAtmAal5VclOutPkts=rbnXAtmAal5VclOutPkts, rbnXAtmAal5VclInPkts=rbnXAtmAal5VclInPkts, rbnXAtmAal5VclInOctets=rbnXAtmAal5VclInOctets, rbnXAal5VclStatMIBGroups=rbnXAal5VclStatMIBGroups, rbnXAal5VclStatMIBObjects=rbnXAal5VclStatMIBObjects, rbnXAal5VclStatMIBCompliances=rbnXAal5VclStatMIBCompliances, rbnXAal5VclStatMIBConformance=rbnXAal5VclStatMIBConformance, rbnXAal5VclStatMIBCompliance=rbnXAal5VclStatMIBCompliance, rbnXAal5VclStatGroup=rbnXAal5VclStatGroup, rbnXAtmAal5VclStatTable=rbnXAtmAal5VclStatTable, PYSNMP_MODULE_ID=rbnXAal5VclStatMIB)
