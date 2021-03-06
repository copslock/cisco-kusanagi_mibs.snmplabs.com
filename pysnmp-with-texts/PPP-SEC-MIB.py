#
# PySNMP MIB module PPP-SEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PPP-SEC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:41:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ppp, = mibBuilder.importSymbols("PPP-LCP-MIB", "ppp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Unsigned32, Counter64, IpAddress, ModuleIdentity, Bits, TimeTicks, Integer32, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Unsigned32", "Counter64", "IpAddress", "ModuleIdentity", "Bits", "TimeTicks", "Integer32", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pppSecurity = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2))
pppSecurityProtocols = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1))
pppSecurityPapProtocol = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 1))
pppSecurityChapMD5Protocol = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 2))
pppSecurityConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 2, 2), )
if mibBuilder.loadTexts: pppSecurityConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecurityConfigTable.setDescription('Table containing the configuration and preference parameters for PPP Security.')
pppSecurityConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1), ).setIndexNames((0, "PPP-SEC-MIB", "pppSecurityConfigLink"), (0, "PPP-SEC-MIB", "pppSecurityConfigPreference"))
if mibBuilder.loadTexts: pppSecurityConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecurityConfigEntry.setDescription('Security configuration information for a particular PPP link.')
pppSecurityConfigLink = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigLink.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecurityConfigLink.setDescription("The value of ifIndex that identifies the entry in the interface table that is associated with the local PPP entity's link for which this particular security algorithm shall be attempted. A value of 0 indicates the default algorithm - i.e., this entry applies to all links for which explicit entries in the table do not exist.")
pppSecurityConfigPreference = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigPreference.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecurityConfigPreference.setDescription('The relative preference of the security protocol identified by pppSecurityConfigProtocol. Security protocols with lower values of pppSecurityConfigPreference are tried before protocols with higher values of pppSecurityConfigPreference.')
pppSecurityConfigProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecurityConfigProtocol.setDescription('Identifies the security protocol to be attempted on the link identified by pppSecurityConfigLink at the preference level identified by pppSecurityConfigPreference. ')
pppSecurityConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecurityConfigStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecurityConfigStatus.setDescription('Setting this object to the value invalid(1) has the effect of invalidating the corresponding entry in the pppSecurityConfigTable. It is an implementation-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant pppSecurityConfigStatus object.')
pppSecuritySecretsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 2, 3), )
if mibBuilder.loadTexts: pppSecuritySecretsTable.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsTable.setDescription('Table containing the identities and secrets used by the PPP authentication protocols. As this table contains secret information, it is expected that access to this table be limited to those SNMP Party-Pairs for which a privacy protocol is in use for all SNMP messages that the parties exchange. This table contains both the ID and secret pair(s) that the local PPP entity will advertise to the remote entity and the pair(s) that the local entity will expect from the remote entity. This table allows for multiple id/secret password pairs to be specified for a particular link by using the pppSecuritySecretsIdIndex object.')
pppSecuritySecretsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1), ).setIndexNames((0, "PPP-SEC-MIB", "pppSecuritySecretsLink"), (0, "PPP-SEC-MIB", "pppSecuritySecretsIdIndex"))
if mibBuilder.loadTexts: pppSecuritySecretsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsEntry.setDescription('Secret information.')
pppSecuritySecretsLink = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppSecuritySecretsLink.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsLink.setDescription('The link to which this ID/Secret pair applies. By convention, if the value of this object is 0 then the ID/Secret pair applies to all links.')
pppSecuritySecretsIdIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppSecuritySecretsIdIndex.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsIdIndex.setDescription('A unique value for each ID/Secret pair that has been defined for use on this link. This allows multiple ID/Secret pairs to be defined for each link. How the local entity selects which pair to use is a local implementation decision.')
pppSecuritySecretsDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local-to-remote", 1), ("remote-to-local", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsDirection.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsDirection.setDescription('This object defines the direction in which a particular ID/Secret pair is valid. If this object is local-to-remote then the local PPP entity will use the ID/Secret pair when attempting to authenticate the local PPP entity to the remote PPP entity. If this object is remote-to-local then the local PPP entity will expect the ID/Secret pair to be used by the remote PPP entity when the remote PPP entity attempts to authenticate itself to the local PPP entity.')
pppSecuritySecretsProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsProtocol.setDescription('The security protocol (e.g. CHAP or PAP) to which this ID/Secret pair applies.')
pppSecuritySecretsIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsIdentity.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsIdentity.setDescription('The Identity of the ID/Secret pair. The actual format, semantics, and use of pppSecuritySecretsIdentity depends on the actual security protocol used. For example, if pppSecuritySecretsProtocol is pppSecurityPapProtocol then this object will contain a PAP Peer-ID. If pppSecuritySecretsProtocol is pppSecurityChapMD5Protocol then this object would contain the CHAP NAME parameter.')
pppSecuritySecretsSecret = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsSecret.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsSecret.setDescription('The secret of the ID/Secret pair. The actual format, semantics, and use of pppSecuritySecretsSecret depends on the actual security protocol used. For example, if pppSecuritySecretsProtocol is pppSecurityPapProtocol then this object will contain a PAP Password. If pppSecuritySecretsProtocol is pppSecurityChapMD5Protocol then this object would contain the CHAP MD5 Secret.')
pppSecuritySecretsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppSecuritySecretsStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pppSecuritySecretsStatus.setDescription('Setting this object to the value invalid(1) has the effect of invalidating the corresponding entry in the pppSecuritySecretsTable. It is an implementation-specific matter as to whether the agent removes an invalidated entry from the table. Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use. Proper interpretation of such entries requires examination of the relevant pppSecuritySecretsStatus object.')
mibBuilder.exportSymbols("PPP-SEC-MIB", pppSecurityConfigPreference=pppSecurityConfigPreference, pppSecurity=pppSecurity, pppSecuritySecretsStatus=pppSecuritySecretsStatus, pppSecurityConfigLink=pppSecurityConfigLink, pppSecuritySecretsProtocol=pppSecuritySecretsProtocol, pppSecurityChapMD5Protocol=pppSecurityChapMD5Protocol, pppSecuritySecretsLink=pppSecuritySecretsLink, pppSecuritySecretsSecret=pppSecuritySecretsSecret, pppSecuritySecretsIdentity=pppSecuritySecretsIdentity, pppSecuritySecretsDirection=pppSecuritySecretsDirection, pppSecurityPapProtocol=pppSecurityPapProtocol, pppSecuritySecretsTable=pppSecuritySecretsTable, pppSecuritySecretsEntry=pppSecuritySecretsEntry, pppSecurityConfigProtocol=pppSecurityConfigProtocol, pppSecurityConfigStatus=pppSecurityConfigStatus, pppSecurityConfigEntry=pppSecurityConfigEntry, pppSecurityConfigTable=pppSecurityConfigTable, pppSecuritySecretsIdIndex=pppSecuritySecretsIdIndex, pppSecurityProtocols=pppSecurityProtocols)
