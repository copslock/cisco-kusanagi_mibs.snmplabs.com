#
# PySNMP MIB module NETBOTZ-PRD-CRL-MIB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETBOTZ-PRD-CRL-MIB2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
netBotz_prd_crawlers, = mibBuilder.importSymbols("NETBOTZ-PRODUCTS-MIB", "netBotz-prd-crawlers")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, iso, MibIdentifier, Integer32, NotificationType, Bits, Counter64, ModuleIdentity, Gauge32, Counter32, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "iso", "MibIdentifier", "Integer32", "NotificationType", "Bits", "Counter64", "ModuleIdentity", "Gauge32", "Counter32", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netbotz_crawlers = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528)).setLabel("netbotz-crawlers")
netBotz_prd_crl_mib2 = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1)).setLabel("netBotz-prd-crl-mib2")
netBotz_prd_crl_mib2if = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2)).setLabel("netBotz-prd-crl-mib2if")
netBotz_prd_crl_mib2_ping = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3), Integer32()).setLabel("netBotz-prd-crl-mib2-ping").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_ping.setReference('Netbotz Device Ping')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_ping.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_ping.setDescription('Netbotz device ping. This object indicates the status of a ping on a device monitored by a Netbotz device.')
netBotz_prd_crl_mib2_uptime = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 8), TimeTicks()).setLabel("netBotz-prd-crl-mib2-uptime").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_uptime.setReference('Netbotz Uptime')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_uptime.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_uptime.setDescription('The uptime of a device monitored by a Netbotz device.')
netBotz_prd_crl_mib2_snmpstatus = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9), DisplayString()).setLabel("netBotz-prd-crl-mib2-snmpstatus").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_snmpstatus.setReference('Netbotz SNMP Status')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_snmpstatus.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2_snmpstatus.setDescription('The SNMP status of a device monitored by a Netbotz device.')
netBotz_prd_crl_mib2if_opstatus = MibScalar((1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6), Integer32()).setLabel("netBotz-prd-crl-mib2if-opstatus").setMaxAccess("readonly")
if mibBuilder.loadTexts: netBotz_prd_crl_mib2if_opstatus.setReference('Netbotz Operational Status')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2if_opstatus.setStatus('mandatory')
if mibBuilder.loadTexts: netBotz_prd_crl_mib2if_opstatus.setDescription('The operational status of a device monitored by a Netbotz device.')
mibBuilder.exportSymbols("NETBOTZ-PRD-CRL-MIB2-MIB", netBotz_prd_crl_mib2_snmpstatus=netBotz_prd_crl_mib2_snmpstatus, netBotz_prd_crl_mib2_uptime=netBotz_prd_crl_mib2_uptime, netBotz_prd_crl_mib2=netBotz_prd_crl_mib2, netBotz_prd_crl_mib2_ping=netBotz_prd_crl_mib2_ping, netBotz_prd_crl_mib2if=netBotz_prd_crl_mib2if, netBotz_prd_crl_mib2if_opstatus=netBotz_prd_crl_mib2if_opstatus, netbotz_crawlers=netbotz_crawlers)
