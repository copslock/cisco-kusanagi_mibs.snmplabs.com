#
# PySNMP MIB module Wellfleet-IREDUND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IREDUND-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, Bits, IpAddress, Integer32, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Bits", "IpAddress", "Integer32", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfIRedundGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfIRedundGroup")
wfIRedundIfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1), )
if mibBuilder.loadTexts: wfIRedundIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfTable.setDescription('WF_IREDUND_INTERFACE_TABLE - Interface REDUNDANCY This tabulates the interfaces within an interface redundancy group. All interfaces are indexed according to their physical slot and connector designation. All interfaces in the same circuit act as redundant (hot stand-by) interfaces for that circuit. At any given time, one hot stand-by interface is chosen to be the active interface for a circuit. The active interface is the only interface that is reading and writing data to/from the media.')
wfIRedundIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1), ).setIndexNames((0, "Wellfleet-IREDUND-MIB", "wfIRedundIfSlot"), (0, "Wellfleet-IREDUND-MIB", "wfIRedundIfPort"))
if mibBuilder.loadTexts: wfIRedundIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfEntry.setDescription('Redundant interface entries.')
wfIRedundIfDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIRedundIfDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfDelete.setDescription('Creation and deletion flag for this record. When set, it will cause this entry to be deleted from the MIB.')
wfIRedundIfDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIRedundIfDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfDisable.setDescription('Enable/Disable parameter. A disabled interface will never be selected as the active interface for a circuit.')
wfIRedundIfCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIRedundIfCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfCct.setDescription('The circuit number of the circuit to which the interface belongs. This interface will either act as the active interface for the the circuit or as a hot stand-by.')
wfIRedundIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIRedundIfSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfSlot.setDescription('Slot ID of the interface, used as instance ID')
wfIRedundIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 44))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIRedundIfPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfPort.setDescription('Port ID of the interface, used as instance ID')
wfIRedundIfPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("nonprimary", 2))).clone('nonprimary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIRedundIfPrimary.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfPrimary.setDescription('Primary flag, indicates if this has been chosen as the primary interface. Only one interface in any circuit can be selected as a PRIMARY interface. The PRIMARY interface will have priority when an active interface is selected for a circuit. In general, if a PRIMARY circuit is available at active interface selection time, it will be chosen as the active interface.')
wfIRedundIfActive = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notavailable", 1), ("standby", 2), ("active", 3))).clone('notavailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIRedundIfActive.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfActive.setDescription('Active flag, indicates if this interface is the current active interface for the Interface Redundancy Group, or a standby interface, or not available to be used as active interface.')
wfIRedundIfMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 10, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIRedundIfMACAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIRedundIfMACAddr.setDescription('MAC Address being used by Interface Redundancy as Primary MAC Address.')
mibBuilder.exportSymbols("Wellfleet-IREDUND-MIB", wfIRedundIfPort=wfIRedundIfPort, wfIRedundIfActive=wfIRedundIfActive, wfIRedundIfTable=wfIRedundIfTable, wfIRedundIfDelete=wfIRedundIfDelete, wfIRedundIfCct=wfIRedundIfCct, wfIRedundIfMACAddr=wfIRedundIfMACAddr, wfIRedundIfPrimary=wfIRedundIfPrimary, wfIRedundIfEntry=wfIRedundIfEntry, wfIRedundIfSlot=wfIRedundIfSlot, wfIRedundIfDisable=wfIRedundIfDisable)
