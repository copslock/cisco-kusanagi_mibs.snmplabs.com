#
# PySNMP MIB module IBMIROCAUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMIROCAUTH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:40:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, NotificationType, Integer32, Counter32, TimeTicks, Gauge32, ModuleIdentity, enterprises, Unsigned32, IpAddress, iso, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "NotificationType", "Integer32", "Counter32", "TimeTicks", "Gauge32", "ModuleIdentity", "enterprises", "Unsigned32", "IpAddress", "iso", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TruthValue, DisplayString, RowStatus, TestAndIncr, TextualConvention, AutonomousType, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TestAndIncr", "TextualConvention", "AutonomousType", "PhysAddress")
ibmIROCconfigAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2))
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm2210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 72))
ibmIROC = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119))
ibmIROCconfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7))
ibmAuthTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 0))
ibmAuthMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1))
ibmAuthDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 2))
ibmAuthConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3))
ibmAuthGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 1))
authCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 1))
authGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 2))
class RowDefinition(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class Enabled(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class DateAndTime2(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 11)

class SecureOctetString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 65535)

class SecureDisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 65535)

class SecureRowDefinition(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 65535)

authUserProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2), )
if mibBuilder.loadTexts: authUserProfileTable.setStatus('mandatory')
authUserProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1), ).setIndexNames((1, "IBMIROCAUTH-MIB", "authUserProfileName"))
if mibBuilder.loadTexts: authUserProfileEntry.setStatus('mandatory')
authUserProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: authUserProfileName.setStatus('mandatory')
authUserProfileRowDefinition = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 2), SecureRowDefinition()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileRowDefinition.setStatus('mandatory')
authUserProfilePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 3), SecureDisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfilePassword.setStatus('mandatory')
authUserProfileType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="20")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileType.setStatus('mandatory')
authUserProfileMaxConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileMaxConnectTime.setStatus('mandatory')
authUserProfileCallbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("roaming", 1), ("required", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileCallbackType.setStatus('mandatory')
authUserProfileCallbackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileCallbackNum.setStatus('mandatory')
authUserProfileDialout = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 8), Enabled().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileDialout.setStatus('mandatory')
authUserProfileEncryptionKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 9), SecureOctetString().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileEncryptionKey.setStatus('mandatory')
authUserProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("locked", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileStatus.setStatus('mandatory')
authUserProfileExpirationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 11), DateAndTime2().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileExpirationDate.setStatus('mandatory')
authUserProfileGLoginAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileGLoginAllowed.setStatus('mandatory')
authUserProfileGLoginsAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserProfileGLoginsAttempts.setStatus('mandatory')
authUserProfileLoginAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserProfileLoginAttempts.setStatus('mandatory')
authUserProfileLoginFails = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserProfileLoginFails.setStatus('mandatory')
authUserProfileLoginLock = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: authUserProfileLoginLock.setStatus('mandatory')
authUserProfileIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4))).clone(namedValues=NamedValues(("disabled", 0), ("single", 1), ("networkDials", 3), ("singleDials", 4))).clone('single')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileIpType.setStatus('mandatory')
authUserProfileIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 18), IpAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileIpAddr.setStatus('mandatory')
authUserProfileIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 19), IpAddress().clone('255.255.255.255')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileIpMask.setStatus('mandatory')
authUserProfileHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileHostName.setStatus('mandatory')
authUserProfileSharedSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 21), SecureDisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileSharedSecurity.setStatus('mandatory')
authUserProfileTunneled = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 22), Enabled().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileTunneled.setStatus('mandatory')
authUserProfileTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3))).clone(namedValues=NamedValues(("l2tp", 3))).clone('l2tp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileTunnelType.setStatus('mandatory')
authUserProfileTunnelMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ip", 1))).clone('ip')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileTunnelMediumType.setStatus('mandatory')
authUserProfileTunnelServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileTunnelServer.setStatus('mandatory')
authUserProfileVcEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 26), Enabled().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileVcEnabled.setStatus('mandatory')
authUserProfileVcMaxSuspendTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileVcMaxSuspendTime.setStatus('mandatory')
authUserProfileVcIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 1, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authUserProfileVcIdleTime.setStatus('mandatory')
authUserProfileGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 2, 1))
authUserProfileCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 7, 2, 3, 1, 1))
mibBuilder.exportSymbols("IBMIROCAUTH-MIB", authUserProfileEncryptionKey=authUserProfileEncryptionKey, authUserProfileLoginFails=authUserProfileLoginFails, authUserProfileVcEnabled=authUserProfileVcEnabled, authUserProfilePassword=authUserProfilePassword, authUserProfileGLoginAllowed=authUserProfileGLoginAllowed, ibmAuthDomains=ibmAuthDomains, SecureOctetString=SecureOctetString, ibm2210=ibm2210, ibmIROCconfig=ibmIROCconfig, ibmIROC=ibmIROC, ibmAuthGeneral=ibmAuthGeneral, authUserProfileVcMaxSuspendTime=authUserProfileVcMaxSuspendTime, authUserProfileHostName=authUserProfileHostName, authUserProfileLoginLock=authUserProfileLoginLock, authUserProfileTable=authUserProfileTable, authUserProfileEntry=authUserProfileEntry, DateAndTime2=DateAndTime2, ibmProd=ibmProd, authUserProfileSharedSecurity=authUserProfileSharedSecurity, authUserProfileLoginAttempts=authUserProfileLoginAttempts, authUserProfileExpirationDate=authUserProfileExpirationDate, authUserProfileStatus=authUserProfileStatus, ibmAuthMIB=ibmAuthMIB, ibmIROCconfigAuth=ibmIROCconfigAuth, authUserProfileCallbackNum=authUserProfileCallbackNum, authUserProfileIpMask=authUserProfileIpMask, authUserProfileName=authUserProfileName, ibm=ibm, authUserProfileCallbackType=authUserProfileCallbackType, authUserProfileVcIdleTime=authUserProfileVcIdleTime, authUserProfileTunnelServer=authUserProfileTunnelServer, authUserProfileRowDefinition=authUserProfileRowDefinition, authUserProfileType=authUserProfileType, authUserProfileMaxConnectTime=authUserProfileMaxConnectTime, Enabled=Enabled, authCompliances=authCompliances, authGroups=authGroups, RowDefinition=RowDefinition, SecureDisplayString=SecureDisplayString, authUserProfileIpAddr=authUserProfileIpAddr, authUserProfileGroup=authUserProfileGroup, authUserProfileIpType=authUserProfileIpType, authUserProfileTunneled=authUserProfileTunneled, ibmAuthTraps=ibmAuthTraps, SecureRowDefinition=SecureRowDefinition, authUserProfileDialout=authUserProfileDialout, authUserProfileTunnelMediumType=authUserProfileTunnelMediumType, authUserProfileTunnelType=authUserProfileTunnelType, authUserProfileCompliance=authUserProfileCompliance, ibmAuthConformance=ibmAuthConformance, authUserProfileGLoginsAttempts=authUserProfileGLoginsAttempts)
