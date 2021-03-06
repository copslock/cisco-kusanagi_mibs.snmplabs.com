#
# PySNMP MIB module Wellfleet-IPACCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IPACCT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, TimeTicks, ModuleIdentity, MibIdentifier, Bits, iso, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Bits", "iso", "Gauge32", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfAccountingGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfAccountingGroup")
wfIpAcctGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1))
wfIpAcctBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1))
wfIpAcctBaseCreate = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctBaseCreate.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete IP_ACCT.')
wfIpAcctBaseEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctBaseEnable.setDescription('Enable/Disable parameter. Default is enabled. Users perform a set operation on this object in order to enable/disable IP_ACCT.')
wfIpAcctBaseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10240)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctBaseThreshold.setDescription('The max number of entries in the IP accounting table')
wfIpAcctBaseTransitCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10240)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseTransitCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctBaseTransitCount.setDescription('Number of transit entries to be accounted for that do not match the access-list src-dest pairs')
wfIpAcctBaseTrapPercent = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctBaseTrapPercent.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctBaseTrapPercent.setDescription('When this % of table entries are counted a trap is sent to the TI console')
wfIpAcctAge = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctAge.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctAge.setDescription('Number of ticks (seconds) since the 1st entry in the accounting table')
wfIpCkAcctFlag = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpCkAcctFlag.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctFlag.setDescription('This is set when user wants to make a snapshot of the active table into the checkpoint table')
wfIpCkAcctAge = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctAge.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctAge.setDescription('Number of clock ticks since the first entry in the checkpoint accounting table')
wfIpAcctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2), )
if mibBuilder.loadTexts: wfIpAcctTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctTable.setDescription('A list of elements in the IP accounting table')
wfIpAcctTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1), ).setIndexNames((0, "Wellfleet-IPACCT-MIB", "wfIpAcctTableSrcAddr"), (0, "Wellfleet-IPACCT-MIB", "wfIpAcctTableDestAddr"))
if mibBuilder.loadTexts: wfIpAcctTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctTableEntry.setDescription('A src-dest based entry in the table')
wfIpAcctTableSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTableSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctTableSrcAddr.setDescription('Source IP address of Packet')
wfIpAcctTableDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTableDestAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctTableDestAddr.setDescription('Dest IP address of Packet')
wfIpAcctTablePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTablePkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctTablePkts.setDescription('Number of pkts with this src-dest address pair')
wfIpAcctTableBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctTableBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctTableBytes.setDescription('Number of bytes with this src-dest address pair')
wfIpAcctCctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3), )
if mibBuilder.loadTexts: wfIpAcctCctTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctCctTable.setDescription('List of interfaces - circuits configured with IP accounting')
wfIpAcctCctTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1), ).setIndexNames((0, "Wellfleet-IPACCT-MIB", "wfIpAcctCctNum"))
if mibBuilder.loadTexts: wfIpAcctCctTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctCctTableEntry.setDescription('An IP accounting circuit definition')
wfIpAcctCctDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctCctDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctCctDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete an IP accounting interface.')
wfIpAcctCctDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpAcctCctDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctCctDisable.setDescription('Enable/Disable parameter. Default is enabled. Users perform a set operation on this object in order to enable/disable an IP accounting on an interface.')
wfIpAcctCctNum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpAcctCctNum.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpAcctCctNum.setDescription('The Circuit Number that this interface runs over')
wfIpCkAcctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4), )
if mibBuilder.loadTexts: wfIpCkAcctTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctTable.setDescription('A list of elements in the IP checkpoint accounting table')
wfIpCkAcctTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1), ).setIndexNames((0, "Wellfleet-IPACCT-MIB", "wfIpCkAcctTableSrcAddr"), (0, "Wellfleet-IPACCT-MIB", "wfIpCkAcctTableDestAddr"))
if mibBuilder.loadTexts: wfIpCkAcctTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctTableEntry.setDescription('A src-dest based entry in the checkpoint table')
wfIpCkAcctTableSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTableSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctTableSrcAddr.setDescription('Source IP address of Packet in checkpoint table')
wfIpCkAcctTableDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTableDestAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctTableDestAddr.setDescription('Dest IP address of Packet in checkpoint table')
wfIpCkAcctTablePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTablePkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctTablePkts.setDescription('Number of pkts with this src-dest address pair in checkpoint table')
wfIpCkAcctTableBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 20, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIpCkAcctTableBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wfIpCkAcctTableBytes.setDescription('Number of bytes with this src-dest address pair in checkpoint table')
mibBuilder.exportSymbols("Wellfleet-IPACCT-MIB", wfIpAcctBaseThreshold=wfIpAcctBaseThreshold, wfIpCkAcctTableSrcAddr=wfIpCkAcctTableSrcAddr, wfIpCkAcctTablePkts=wfIpCkAcctTablePkts, wfIpCkAcctTableEntry=wfIpCkAcctTableEntry, wfIpAcctGroup=wfIpAcctGroup, wfIpAcctTableDestAddr=wfIpAcctTableDestAddr, wfIpAcctBaseCreate=wfIpAcctBaseCreate, wfIpAcctBaseEnable=wfIpAcctBaseEnable, wfIpAcctTable=wfIpAcctTable, wfIpCkAcctAge=wfIpCkAcctAge, wfIpAcctTableSrcAddr=wfIpAcctTableSrcAddr, wfIpAcctBaseTransitCount=wfIpAcctBaseTransitCount, wfIpAcctCctTableEntry=wfIpAcctCctTableEntry, wfIpAcctCctDelete=wfIpAcctCctDelete, wfIpAcctBase=wfIpAcctBase, wfIpAcctTableBytes=wfIpAcctTableBytes, wfIpAcctCctTable=wfIpAcctCctTable, wfIpAcctCctDisable=wfIpAcctCctDisable, wfIpCkAcctTableBytes=wfIpCkAcctTableBytes, wfIpAcctAge=wfIpAcctAge, wfIpCkAcctFlag=wfIpCkAcctFlag, wfIpAcctCctNum=wfIpAcctCctNum, wfIpCkAcctTableDestAddr=wfIpCkAcctTableDestAddr, wfIpCkAcctTable=wfIpCkAcctTable, wfIpAcctTableEntry=wfIpAcctTableEntry, wfIpAcctBaseTrapPercent=wfIpAcctBaseTrapPercent, wfIpAcctTablePkts=wfIpAcctTablePkts)
