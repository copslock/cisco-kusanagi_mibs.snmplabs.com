#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-StateSummaryMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-StateSummaryMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:31:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
mscPassportMIBs, mscComponents = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs", "mscComponents")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Counter64, TimeTicks, Gauge32, NotificationType, ObjectIdentity, MibIdentifier, iso, Counter32, Integer32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Counter64", "TimeTicks", "Gauge32", "NotificationType", "ObjectIdentity", "MibIdentifier", "iso", "Counter32", "Integer32", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stateSummaryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 7))
if mibBuilder.loadTexts: stateSummaryMIB.setLastUpdated('9907300000Z')
if mibBuilder.loadTexts: stateSummaryMIB.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: stateSummaryMIB.setContactInfo(" Nortel Carrier Data Network Management Postal: P.O. Box 3511, Station C Ottawa, Ontario Canada K1Y 4H7 via the WEB: http://www.nortelnetworks.com select 'Contact Us' from the menu via phone: 1-800-4NORTEL")
if mibBuilder.loadTexts: stateSummaryMIB.setDescription('This MIB module specifies the variables used to implement the Nortel MsCarrier MscPassport state summary functionality.')
mscStateSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5))
mscTimeOfLastTableChange = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 1))
mscTimeOfLastStateSummTableChange = MibScalar((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeOfLastStateSummTableChange.setStatus('current')
if mibBuilder.loadTexts: mscTimeOfLastStateSummTableChange.setDescription('The value of sysUpTime at the time that an entry in the mscCompClassTable detected a change.')
mscCompClassTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2), )
if mibBuilder.loadTexts: mscCompClassTable.setStatus('current')
if mibBuilder.loadTexts: mscCompClassTable.setDescription('A list of component classes that have state information summaries.')
mscCompClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-StateSummaryMIB", "mscCompClass"))
if mibBuilder.loadTexts: mscCompClassEntry.setStatus('current')
if mibBuilder.loadTexts: mscCompClassEntry.setDescription('A component class entry.')
mscCompClass = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscCompClass.setStatus('current')
if mibBuilder.loadTexts: mscCompClass.setDescription('An object identifier which points to the SNMP Mib Arc for that particular component class. For example, a replication of 1.3.6.1.4.1.562.36.2.1.12 (iso.org.dod. internet.private.enterprises.nortel.mscCarrier.mscPassport. mscComponents.mscLp) corresponds to the Lp component class.')
mscCompName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscCompName.setStatus('current')
if mibBuilder.loadTexts: mscCompName.setDescription('The string representation of the component class object identifier. For example, 1.3.6.1.4.1.562.36.2.1.12 (iso.org. dod.internet.private.enterprises.nortel.mscCarrier.mscPassport. mscComponents.mscLp) is represented as the string, LogicalProcessor.')
mscTimeOfLastStateStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscTimeOfLastStateStatusChange.setStatus('current')
if mibBuilder.loadTexts: mscTimeOfLastStateStatusChange.setDescription('The value of sysUpTime when an OsiState or OsiStateStatus change was detected for the component class. Currently monitored attributes include: AdminState, OperationalState, AvailabilityStatus and AlarmStatus.')
mscNumberDown = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNumberDown.setStatus('current')
if mibBuilder.loadTexts: mscNumberDown.setDescription('The number of component instances that are down. A component is considered down when its administrative state is locked or its operational state is disabled. ')
mscNumberTroubled = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscNumberTroubled.setStatus('current')
if mibBuilder.loadTexts: mscNumberTroubled.setDescription('The number of component instances that are troubled. A component is considered troubled when its administrative status is shuttingDown or its alarm status is not empty or its availability status is degraded.')
stateSummaryGroupCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 7, 1, 1, 2, 2))
stateSummaryCapabilitiesCA01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 7, 3, 1, 2, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-StateSummaryMIB", stateSummaryGroupCA01A=stateSummaryGroupCA01A, mscNumberTroubled=mscNumberTroubled, mscTimeOfLastStateStatusChange=mscTimeOfLastStateStatusChange, mscStateSummary=mscStateSummary, stateSummaryCapabilitiesCA01A=stateSummaryCapabilitiesCA01A, PYSNMP_MODULE_ID=stateSummaryMIB, mscTimeOfLastTableChange=mscTimeOfLastTableChange, stateSummaryMIB=stateSummaryMIB, mscCompClassTable=mscCompClassTable, mscCompClass=mscCompClass, mscCompName=mscCompName, mscCompClassEntry=mscCompClassEntry, mscNumberDown=mscNumberDown, mscTimeOfLastStateSummTableChange=mscTimeOfLastStateSummTableChange)
