#
# PySNMP MIB module ATM-DXI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-DXI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Gauge32, NotificationType, Counter32, iso, IpAddress, enterprises, Unsigned32, Bits, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Gauge32", "NotificationType", "Counter32", "iso", "IpAddress", "enterprises", "Unsigned32", "Bits", "MibIdentifier", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmUniDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3))
class Dfa(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

atmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3, 2))
atmDxiConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 2), )
if mibBuilder.loadTexts: atmDxiConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfTable.setDescription('This table contains ATM DXI configuration information including information on the mode supported across the DXI.')
atmDxiConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiConfIfIndex"))
if mibBuilder.loadTexts: atmDxiConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfEntry.setDescription('This list contains ATM DXI configuration information.')
atmDxiConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiConfIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfIfIndex.setDescription('The value of this object identifies, for SNMP, the ATM DXI interface for which this entry contains management information. This is the same value as used to identify the IfEntry describing the DCE interface. Management uses and expects this value. In the proxy mode of operation, the DCE always treats this as 0, but preserves it in its response to the DTE. 0, the DXI value, means the interface over which the DXI LMI request was received.')
atmDxiConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiConfMode.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfMode.setDescription('This object identifies the dxi mode being used at the atm dxi port.')
atmDxiDFAConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 3), )
if mibBuilder.loadTexts: atmDxiDFAConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfTable.setDescription('This table contains configuration information about a particular DFA.')
atmDxiDFAConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiDFAConfIfIndex"), (0, "ATM-DXI-MIB", "atmDxiDFAConfDfaIndex"))
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setDescription('This list contains ATM DXI DFA configuration information.')
atmDxiDFAConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setDescription('The value of this object identifies, for SNMP, the ATM DXI interface for which this entry contains management information. This is the same value as used to identify the IfEntry describing the DCE interface. Management uses and expects this value. In the proxy mode of operation, the DCE always treats this as 0, but preserves it in its response to the DTE. 0, the DXI value, means the interface over which the DXI LMI request was received.')
atmDxiDFAConfDfaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 2), Dfa()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setDescription('This object identifies the DFA instance on the DXI identified by atmDxiDFAConfIfIndex.')
atmDxiDFAConfAALType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("aal34", 3), ("aal5", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setDescription('This object identifies the AAL type supported at this DFA. Note, if mode 2 is supported on the DXI identified by the corresponding instance of atmDxiDFAConfIfIndex and that instance of atmDxiDFAConfIfIndex identifies the DCE side of the DXI, then this object contains the AAL Type being run on the corresponding VPI/VCI on the corresponding ATM UNI interface.')
atmDxiEnterprise = MibScalar((1, 3, 6, 1, 4, 1, 353, 3, 2, 4), ObjectIdentifier())
if mibBuilder.loadTexts: atmDxiEnterprise.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiEnterprise.setDescription("This object is included as the first ID-Value pair in a Trap PDU for which the Generic Trap Type field has the value 'enterpriseSpecific'. The value of the object identifies the enterprise under whose authority the value of the Enterprise Trap Type field is defined.")
mibBuilder.exportSymbols("ATM-DXI-MIB", atmDxiDFAConfTable=atmDxiDFAConfTable, atmDxiEnterprise=atmDxiEnterprise, atmDxi=atmDxi, atmDxiConfTable=atmDxiConfTable, atmDxiConfEntry=atmDxiConfEntry, atmDxiDFAConfDfaIndex=atmDxiDFAConfDfaIndex, atmDxiConfMode=atmDxiConfMode, atmDxiConfIfIndex=atmDxiConfIfIndex, atmForum=atmForum, atmDxiDFAConfAALType=atmDxiDFAConfAALType, atmDxiDFAConfEntry=atmDxiDFAConfEntry, atmDxiDFAConfIfIndex=atmDxiDFAConfIfIndex, Dfa=Dfa, atmUniDxi=atmUniDxi)
