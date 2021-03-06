#
# PySNMP MIB module JUNIPER-LSYSSP-NATSRCRULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LSYSSP-NATSRCRULE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
jnxLsysSpNATsrcrule, = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATsrcrule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Bits, Counter64, ModuleIdentity, Counter32, Gauge32, TimeTicks, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "Counter64", "ModuleIdentity", "Counter32", "Gauge32", "TimeTicks", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxLsysSpNATsrcruleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1))
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMIB.setLastUpdated('201005191644Z')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMIB.setDescription('This module defines the NAT-source-rule-specific MIB for Juniper Enterprise Logical-System (LSYS) security profiles. Juniper documentation is recommended as the reference. The LSYS security profile provides various static and dynamic resource management by observing resource quota limits. Security NAT-source-rule resource is the focus in this MIB. ')
jnxLsysSpNATsrcruleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1))
jnxLsysSpNATsrcruleSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2))
jnxLsysSpNATsrcruleTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleTable.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleTable.setDescription('LSYSPROFILE NAT-source-rule objects for NAT-source-rule resource consumption per LSYS.')
jnxLsysSpNATsrcruleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LSYSSP-NATSRCRULE-MIB", "jnxLsysSpNATsrcruleLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleEntry.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleEntry.setDescription('An entry in NAT-source-rule resource table.')
jnxLsysSpNATsrcruleLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLsysName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLsysName.setDescription('The name of the logical system for which NAT-source-rule resource information is retrieved. ')
jnxLsysSpNATsrcruleProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleProfileName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleProfileName.setDescription('The security profile name string for the LSYS.')
jnxLsysSpNATsrcruleUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleUsage.setDescription('The current resource usage count for the LSYS.')
jnxLsysSpNATsrcruleReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleReserved.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleReserved.setDescription('The reserved resource count for the LSYS.')
jnxLsysSpNATsrcruleMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMaximum.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMaximum.setDescription('The maximum allowed resource usage count for the LSYS.')
jnxLsysSpNATsrcruleUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleUsedAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleUsedAmount.setDescription('The NAT-source-rule resource consumption over all LSYS.')
jnxLsysSpNATsrcruleMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMaxQuota.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMaxQuota.setDescription('The NAT-source-rule resource maximum quota for the whole device for all LSYS.')
jnxLsysSpNATsrcruleAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleAvailableAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleAvailableAmount.setDescription('The NAT-source-rule resource available in the whole device.')
jnxLsysSpNATsrcruleHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleHeaviestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleHeaviestUsage.setDescription('The most amount of NAT-source-rule resource consumed of a LSYS.')
jnxLsysSpNATsrcruleHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleHeaviestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleHeaviestUser.setDescription('The LSYS name that consume the most NAT-source-rule resource.')
jnxLsysSpNATsrcruleLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLightestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLightestUsage.setDescription('The least amount of NAT-source-rule resource consumed of a LSYS.')
jnxLsysSpNATsrcruleLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLightestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLightestUser.setDescription('The LSYS name that consume the least NAT-source-rule resource.')
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCRULE-MIB", jnxLsysSpNATsrcruleUsedAmount=jnxLsysSpNATsrcruleUsedAmount, PYSNMP_MODULE_ID=jnxLsysSpNATsrcruleMIB, jnxLsysSpNATsrcruleMIB=jnxLsysSpNATsrcruleMIB, jnxLsysSpNATsrcruleEntry=jnxLsysSpNATsrcruleEntry, jnxLsysSpNATsrcruleUsage=jnxLsysSpNATsrcruleUsage, jnxLsysSpNATsrcruleMaximum=jnxLsysSpNATsrcruleMaximum, jnxLsysSpNATsrcruleLsysName=jnxLsysSpNATsrcruleLsysName, jnxLsysSpNATsrcruleLightestUsage=jnxLsysSpNATsrcruleLightestUsage, jnxLsysSpNATsrcruleSummary=jnxLsysSpNATsrcruleSummary, jnxLsysSpNATsrcruleReserved=jnxLsysSpNATsrcruleReserved, jnxLsysSpNATsrcruleAvailableAmount=jnxLsysSpNATsrcruleAvailableAmount, jnxLsysSpNATsrcruleMaxQuota=jnxLsysSpNATsrcruleMaxQuota, jnxLsysSpNATsrcruleProfileName=jnxLsysSpNATsrcruleProfileName, jnxLsysSpNATsrcruleHeaviestUsage=jnxLsysSpNATsrcruleHeaviestUsage, jnxLsysSpNATsrcruleLightestUser=jnxLsysSpNATsrcruleLightestUser, jnxLsysSpNATsrcruleHeaviestUser=jnxLsysSpNATsrcruleHeaviestUser, jnxLsysSpNATsrcruleObjects=jnxLsysSpNATsrcruleObjects, jnxLsysSpNATsrcruleTable=jnxLsysSpNATsrcruleTable)
