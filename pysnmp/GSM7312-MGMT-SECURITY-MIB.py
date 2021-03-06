#
# PySNMP MIB module GSM7312-MGMT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7312-MGMT-SECURITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
gsm7312, = mibBuilder.importSymbols("GSM7312-REF-MIB", "gsm7312")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, Counter64, MibIdentifier, TimeTicks, Gauge32, NotificationType, IpAddress, Counter32, Unsigned32, Bits, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter64", "MibIdentifier", "TimeTicks", "Gauge32", "NotificationType", "IpAddress", "Counter32", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gsm7312MgmtSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11))
gsm7312MgmtSecurity.setRevisions(('2003-11-21 00:00',))
if mibBuilder.loadTexts: gsm7312MgmtSecurity.setLastUpdated('200311210000Z')
if mibBuilder.loadTexts: gsm7312MgmtSecurity.setOrganization('Netgear')
agentSSLConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1))
agentSSLAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLAdminMode.setStatus('current')
agentSSLSecurePort = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSecurePort.setStatus('current')
agentSSLProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssl30", 1), ("tls10", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLProtocolLevel.setStatus('current')
agentSSHConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2))
agentSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHAdminMode.setStatus('current')
agentSSHProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssh10", 1), ("ssh20", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHProtocolLevel.setStatus('current')
agentSSHSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 11, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHSessionsCount.setStatus('current')
mibBuilder.exportSymbols("GSM7312-MGMT-SECURITY-MIB", agentSSLConfigGroup=agentSSLConfigGroup, agentSSHProtocolLevel=agentSSHProtocolLevel, agentSSHConfigGroup=agentSSHConfigGroup, agentSSHSessionsCount=agentSSHSessionsCount, agentSSLProtocolLevel=agentSSLProtocolLevel, gsm7312MgmtSecurity=gsm7312MgmtSecurity, agentSSHAdminMode=agentSSHAdminMode, agentSSLAdminMode=agentSSLAdminMode, agentSSLSecurePort=agentSSLSecurePort, PYSNMP_MODULE_ID=gsm7312MgmtSecurity)
