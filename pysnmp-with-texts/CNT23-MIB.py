#
# PySNMP MIB module CNT23-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CNT23-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
cnt2Snmp, = mibBuilder.importSymbols("CNT2-MIB", "cnt2Snmp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, ModuleIdentity, Unsigned32, Gauge32, Integer32, enterprises, NotificationType, iso, TimeTicks, Bits, IpAddress, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Gauge32", "Integer32", "enterprises", "NotificationType", "iso", "TimeTicks", "Bits", "IpAddress", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cnt2SubAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 333, 2, 3, 1))
cnt2RegistrationNum = MibScalar((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegistrationNum.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegistrationNum.setDescription('The number of registerations received from subagents.')
cnt2RegistrationTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2), )
if mibBuilder.loadTexts: cnt2RegistrationTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegistrationTable.setDescription('A list of registration entries. The number of registrations is given by the value of cnt2RegstrationNum.')
cnt2RegistrationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1), ).setIndexNames((0, "CNT23-MIB", "cnt2RegisterIndex"))
if mibBuilder.loadTexts: cnt2RegistrationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegistrationEntry.setDescription('A subagent entry containing objects known about the subagents by the master agent.')
cnt2RegisterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterIndex.setDescription('A unique value for each registration. Its value ranges between 1 and the value of cnt2RegistrationNum. The order in which entries exist in this table identifies the chronological order in which subagent registrations occurred.')
cnt2RegisterSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterSlot.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterSlot.setDescription('The slot number for this subagent if it is connected over the switch. If it is TCP or UDP connected, this value is 0.')
cnt2RegisterProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("dpiv2", 2), ("smux", 3), ("local", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterProtocol.setDescription('The protocol used to interface to this subagent.')
cnt2RegisterTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("switch", 1), ("tcp", 2), ("udp", 3), ("memory", 4), ("fl", 5), ("direct", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterTransport.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterTransport.setDescription('The transport method/protocol underlying the master/subagent protocol that is used to interface to this subagent.')
cnt2RegisterAgentDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterAgentDescr.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterAgentDescr.setDescription('A textual string containing a description of the registering subagent.')
cnt2RegisterGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterGroup.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterGroup.setDescription('The group object identifier used by the subagent to register. If the subagent registered a row, this will reflect the table identifier.')
cnt2RegisterMibVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterMibVersion.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterMibVersion.setDescription('A textual string containing a reference to the body administering the registered tree and the version of the registered tree. The string will be in one of the following forms: RFC xxxx - xxxx is the RFC number, CNT x.y - x is the major version, y is the minor version, IETF vv/mmm/yy - (IETF Draft), vv is the version, mmm is a three character month code, yy is the year, NAME vv/mmm/yy - NAME is a Standards Body name, vv is the version, mmm is a three character month code, yy is the year.')
cnt2RegisterUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterUpTime.setDescription('The time that the subagent has been registered, relative to the master agent.')
cnt2RegisterRowInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2RegisterRowInstance.setStatus('mandatory')
if mibBuilder.loadTexts: cnt2RegisterRowInstance.setDescription('A textual string containing the following format: *.x1[.x2.x3...xn], where * - the OID range registered by the subagent, xn - object idenifier representing instance OIDs registered by the subagent. when appended to cnt2RegisterGroup, the entire OID is the group and row registered by the subagent.')
mibBuilder.exportSymbols("CNT23-MIB", cnt2RegisterRowInstance=cnt2RegisterRowInstance, cnt2RegisterTransport=cnt2RegisterTransport, cnt2RegisterSlot=cnt2RegisterSlot, cnt2RegisterMibVersion=cnt2RegisterMibVersion, cnt2RegisterGroup=cnt2RegisterGroup, cnt2RegisterIndex=cnt2RegisterIndex, cnt2RegistrationNum=cnt2RegistrationNum, cnt2RegisterAgentDescr=cnt2RegisterAgentDescr, cnt2SubAgent=cnt2SubAgent, cnt2RegisterProtocol=cnt2RegisterProtocol, cnt2RegistrationTable=cnt2RegistrationTable, cnt2RegistrationEntry=cnt2RegistrationEntry, cnt2RegisterUpTime=cnt2RegisterUpTime)
