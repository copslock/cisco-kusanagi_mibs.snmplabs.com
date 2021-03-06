#
# PySNMP MIB module BAS-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-TRAPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:34:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
basTrapIclClass, basTrapCardType, basTraps, basTrapCmtsCmIpAddress, basTrapCmtsCmGwAddress, basTrapMgmtTwoIpAddress, basTrapIf, basTrapChassis, basTrapChassisNumber, basTrapCmtsCmMacAddress, basTrapCraftIpAddress, basTrapLPort, basTrapSlot, basTrapMgmtOneIpAddress, basTrapSubnetType = mibBuilder.importSymbols("BAS-MIB", "basTrapIclClass", "basTrapCardType", "basTraps", "basTrapCmtsCmIpAddress", "basTrapCmtsCmGwAddress", "basTrapMgmtTwoIpAddress", "basTrapIf", "basTrapChassis", "basTrapChassisNumber", "basTrapCmtsCmMacAddress", "basTrapCraftIpAddress", "basTrapLPort", "basTrapSlot", "basTrapMgmtOneIpAddress", "basTrapSubnetType")
basTraceLogLevel, basTraceLogNotifyComponentId, basTraceLogNotifyString = mibBuilder.importSymbols("BAS-TRACE-MIB", "basTraceLogLevel", "basTraceLogNotifyComponentId", "basTraceLogNotifyString")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, TimeTicks, Bits, IpAddress, Gauge32, iso, NotificationType, ObjectIdentity, Unsigned32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "TimeTicks", "Bits", "IpAddress", "Gauge32", "iso", "NotificationType", "ObjectIdentity", "Unsigned32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
basTrapsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1))
if mibBuilder.loadTexts: basTrapsMIB.setLastUpdated('9812080000Z')
if mibBuilder.loadTexts: basTrapsMIB.setOrganization('Broadband Access Systems, Inc.')
if mibBuilder.loadTexts: basTrapsMIB.setContactInfo(' Tech Support Broadband Access Systems, Inc. 201 Forest Street Marlborough, MA 01752 USA 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basTrapsMIB.setDescription('This MIB module defines the proprietary notifications for Broadband Access Systems, Inc. Network Management.')
basCardDown = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 1)).setObjects(("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"), ("BAS-MIB", "basTrapCardType"))
if mibBuilder.loadTexts: basCardDown.setStatus('current')
if mibBuilder.loadTexts: basCardDown.setDescription('A basCardDown notification indicates that a card with the BAS cluster has gone down.')
basCardUp = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 2)).setObjects(("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"), ("BAS-MIB", "basTrapCardType"))
if mibBuilder.loadTexts: basCardUp.setStatus('current')
if mibBuilder.loadTexts: basCardUp.setDescription('A basCardDown notification indicates that a card with the BAS cluster has gone down.')
basTraceLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 3)).setObjects(("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"), ("BAS-TRACE-MIB", "basTraceLogNotifyComponentId"), ("BAS-TRACE-MIB", "basTraceLogLevel"), ("BAS-TRACE-MIB", "basTraceLogNotifyString"))
if mibBuilder.loadTexts: basTraceLogTrap.setStatus('current')
if mibBuilder.loadTexts: basTraceLogTrap.setDescription('BAS internal use only.')
basCmtsCmUp = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 4)).setObjects(("IF-MIB", "ifIndex"), ("BAS-MIB", "basTrapCmtsCmMacAddress"), ("BAS-MIB", "basTrapCmtsCmIpAddress"))
if mibBuilder.loadTexts: basCmtsCmUp.setStatus('current')
if mibBuilder.loadTexts: basCmtsCmUp.setDescription('A basCmtsCmUp notification indicates that a cable modem has gone up.')
basCmtsCmDown = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 5)).setObjects(("IF-MIB", "ifIndex"), ("BAS-MIB", "basTrapCmtsCmMacAddress"), ("BAS-MIB", "basTrapCmtsCmIpAddress"))
if mibBuilder.loadTexts: basCmtsCmDown.setStatus('current')
if mibBuilder.loadTexts: basCmtsCmDown.setDescription('A basCmtsCmDown notification indicates that a cable modem has gone down.')
basBcmStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 6)).setObjects(("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"), ("BAS-MIB", "basTrapMgmtOneIpAddress"), ("BAS-MIB", "basTrapMgmtTwoIpAddress"), ("BAS-MIB", "basTrapCraftIpAddress"))
if mibBuilder.loadTexts: basBcmStateChange.setStatus('current')
if mibBuilder.loadTexts: basBcmStateChange.setDescription('A basBcmStateChange notification indicates a change in the IP addresses configuration.')
basIclStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 7)).setObjects(("IF-MIB", "ifIndex"), ("BAS-MIB", "basTrapIclClass"), ("BAS-MIB", "basTrapChassisNumber"), ("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"))
if mibBuilder.loadTexts: basIclStateChange.setStatus('current')
if mibBuilder.loadTexts: basIclStateChange.setDescription('A basIclStateChange notification indicates a change in the ICL link. Note that the FIA and Chassis number are information about the Peer.')
basSoftwareComponentUp = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 8)).setObjects(("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"), ("BAS-TRACE-MIB", "basTraceLogNotifyComponentId"))
if mibBuilder.loadTexts: basSoftwareComponentUp.setStatus('current')
if mibBuilder.loadTexts: basSoftwareComponentUp.setDescription('BAS internal use only.')
basSoftwareComponentDown = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 9)).setObjects(("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"), ("BAS-TRACE-MIB", "basTraceLogNotifyComponentId"))
if mibBuilder.loadTexts: basSoftwareComponentDown.setStatus('current')
if mibBuilder.loadTexts: basSoftwareComponentDown.setDescription('BAS internal use only.')
basCmtsCmAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 10)).setObjects(("BAS-MIB", "basTrapCmtsCmMacAddress"), ("BAS-MIB", "basTrapCmtsCmGwAddress"))
if mibBuilder.loadTexts: basCmtsCmAuthFailure.setStatus('current')
if mibBuilder.loadTexts: basCmtsCmAuthFailure.setDescription('A Cable Modem attempt to connect to the system without authorization.')
basDhcpRelayNotConfigured = NotificationType((1, 3, 6, 1, 4, 1, 3493, 3, 2, 1, 11)).setObjects(("BAS-MIB", "basTrapChassis"), ("BAS-MIB", "basTrapSlot"), ("BAS-MIB", "basTrapIf"), ("BAS-MIB", "basTrapLPort"), ("BAS-MIB", "basTrapSubnetType"))
if mibBuilder.loadTexts: basDhcpRelayNotConfigured.setStatus('current')
if mibBuilder.loadTexts: basDhcpRelayNotConfigured.setDescription('A DHCP configuration error.')
mibBuilder.exportSymbols("BAS-TRAPS-MIB", basSoftwareComponentUp=basSoftwareComponentUp, basSoftwareComponentDown=basSoftwareComponentDown, PYSNMP_MODULE_ID=basTrapsMIB, basCardUp=basCardUp, basCardDown=basCardDown, basCmtsCmDown=basCmtsCmDown, basTraceLogTrap=basTraceLogTrap, basCmtsCmAuthFailure=basCmtsCmAuthFailure, basDhcpRelayNotConfigured=basDhcpRelayNotConfigured, basCmtsCmUp=basCmtsCmUp, basTrapsMIB=basTrapsMIB, basBcmStateChange=basBcmStateChange, basIclStateChange=basIclStateChange)
