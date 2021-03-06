#
# PySNMP MIB module SECURITYMGREXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SECURITYMGREXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
securityMgrExt, = mibBuilder.importSymbols("APENT-MIB", "securityMgrExt")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, iso, Counter64, Bits, Integer32, Counter32, Unsigned32, IpAddress, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "iso", "Counter64", "Bits", "Integer32", "Counter32", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
securityMgrExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 13, 1))
if mibBuilder.loadTexts: securityMgrExtMib.setLastUpdated('9707202000Z')
if mibBuilder.loadTexts: securityMgrExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: securityMgrExtMib.setContactInfo(' Steve Colby Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: securityMgrExtMib.setDescription('This MIB module describes the ArrowPoint Communications MIB objects for Network Security.')
apSecurityMgrConsoleAuthType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 13, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("enable", 1), ("radius", 2), ("none", 3), ("radius-enable", 4), ("enable-radius", 5), ("enable-none", 6), ("radius-none", 7), ("radius-enable-none", 8), ("enable-radius-none", 9))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSecurityMgrConsoleAuthType.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrConsoleAuthType.setDescription('This variable specifies the type of authentication used to for console users.')
apSecurityMgrVirtualAuthType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 13, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("enable", 1), ("radius", 2), ("none", 3), ("radius-enable", 4), ("enable-radius", 5), ("enable-none", 6), ("radius-none", 7), ("radius-enable-none", 8), ("enable-radius-none", 9), ("disallowed", 10))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSecurityMgrVirtualAuthType.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrVirtualAuthType.setDescription('This variable specifies the type of authentication used to for console users.')
apSecurityMgrUsernameTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 13, 4), )
if mibBuilder.loadTexts: apSecurityMgrUsernameTable.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrUsernameTable.setDescription('This is the table of username and password pairs used for local authentication.')
apSecurityMgrUsernameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1), ).setIndexNames((0, "SECURITYMGREXT-MIB", "apSecurityMgrUsername"))
if mibBuilder.loadTexts: apSecurityMgrUsernameEntry.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrUsernameEntry.setDescription('The Username table is indexed by username.')
apSecurityMgrUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSecurityMgrUsername.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrUsername.setDescription('The local username.')
apSecurityMgrPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSecurityMgrPassword.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrPassword.setDescription('The local password.')
apSecurityMgrEncryptedPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSecurityMgrEncryptedPassword.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrEncryptedPassword.setDescription('The encrypted local password.')
apSecurityMgrUserPriviledgeLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("non-priviledge", 1), ("priviledge", 2))).clone('priviledge')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSecurityMgrUserPriviledgeLevel.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrUserPriviledgeLevel.setDescription('The priviledge level for this user.')
apSecurityMgrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 13, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSecurityMgrStatus.setStatus('current')
if mibBuilder.loadTexts: apSecurityMgrStatus.setDescription('This object is used to create and destroy a local username entry. This rowstatus object only supports CreateAndGo and Destroy.')
mibBuilder.exportSymbols("SECURITYMGREXT-MIB", apSecurityMgrUsernameTable=apSecurityMgrUsernameTable, apSecurityMgrVirtualAuthType=apSecurityMgrVirtualAuthType, apSecurityMgrUsernameEntry=apSecurityMgrUsernameEntry, apSecurityMgrPassword=apSecurityMgrPassword, apSecurityMgrConsoleAuthType=apSecurityMgrConsoleAuthType, PYSNMP_MODULE_ID=securityMgrExtMib, securityMgrExtMib=securityMgrExtMib, apSecurityMgrEncryptedPassword=apSecurityMgrEncryptedPassword, apSecurityMgrUserPriviledgeLevel=apSecurityMgrUserPriviledgeLevel, apSecurityMgrUsername=apSecurityMgrUsername, apSecurityMgrStatus=apSecurityMgrStatus)
