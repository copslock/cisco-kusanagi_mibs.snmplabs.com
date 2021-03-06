#
# PySNMP MIB module STN-IKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-IKE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:03:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, ObjectIdentity, NotificationType, IpAddress, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, Integer32, Counter64, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ObjectIdentity", "NotificationType", "IpAddress", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "Integer32", "Counter64", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
stnSystems, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnSystems")
stnIKE = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 8))
if mibBuilder.loadTexts: stnIKE.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnIKE.setOrganization('Spring Tide Networks, Inc.')
stnIkeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1))
stnIkeMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 8, 2))
stnIkePreferences = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1))
stnIkeSharedSecrets = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2))
stnIkeCertificates = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3))
stnIkePreferenceTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1), )
if mibBuilder.loadTexts: stnIkePreferenceTable.setStatus('current')
stnIkePreferenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1), ).setIndexNames((0, "STN-IKE-MIB", "stnIkePrefPeerAddress"), (0, "STN-IKE-MIB", "stnIkePrefTransform"))
if mibBuilder.loadTexts: stnIkePreferenceEntry.setStatus('current')
stnIkePrefPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefPeerAddress.setStatus('current')
stnIkePrefTransform = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefTransform.setStatus('current')
stnIkePrefPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 3), Integer32().clone(500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefPeerPort.setStatus('current')
stnIkePrefHash = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hmac-md5", 1), ("hmac-sha", 2))).clone('hmac-md5')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefHash.setStatus('current')
stnIkePrefEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("des-cbc", 1), ("idea-cbc", 2), ("blowfish-cbc", 3), ("rc5-r16-b64-cbc", 4), ("des3-cbc", 5))).clone('des-cbc')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefEncryption.setStatus('current')
stnIkePrefAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("shared", 1), ("dss-sig", 2), ("rsa-sig", 3), ("rsa-enc", 4))).clone('shared')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefAuthentication.setStatus('current')
stnIkePrefDHGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 7), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefDHGroup.setStatus('current')
stnIkePrefMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("main", 2), ("aggressive", 4))).clone('main')).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefMode.setStatus('current')
stnIkePrefLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefLifeTime.setStatus('current')
stnIkePrefLifeBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefLifeBytes.setStatus('current')
stnIkePrefCertAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefCertAlias.setStatus('current')
stnIkePrefServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkePrefServiceName.setStatus('current')
stnIkeSharedSecretTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1), )
if mibBuilder.loadTexts: stnIkeSharedSecretTable.setStatus('current')
stnIkeSharedSecretEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1, 1), ).setIndexNames((0, "STN-IKE-MIB", "stnIkeSSPeerAddress"))
if mibBuilder.loadTexts: stnIkeSharedSecretEntry.setStatus('current')
stnIkeSSPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkeSSPeerAddress.setStatus('current')
stnIkeSSSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024)))
if mibBuilder.loadTexts: stnIkeSSSecret.setStatus('current')
stnIkeCertificateTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1), )
if mibBuilder.loadTexts: stnIkeCertificateTable.setStatus('current')
stnIkeCertificateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1), ).setIndexNames((0, "STN-IKE-MIB", "stnIkeCertificateIndex"))
if mibBuilder.loadTexts: stnIkeCertificateEntry.setStatus('current')
stnIkeCertificateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkeCertificateIndex.setStatus('current')
stnIkeCertificateType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mine", 1), ("root", 2), ("crl", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkeCertificateType.setStatus('current')
stnIkeCertificateAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkeCertificateAlias.setStatus('current')
stnIkeCertificateDN = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkeCertificateDN.setStatus('current')
stnIkeCertificateAltName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkeCertificateAltName.setStatus('current')
stnIkeCertificateIssuer = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIkeCertificateIssuer.setStatus('current')
mibBuilder.exportSymbols("STN-IKE-MIB", stnIkePrefMode=stnIkePrefMode, stnIkeCertificateAltName=stnIkeCertificateAltName, stnIkeSharedSecrets=stnIkeSharedSecrets, stnIkePrefPeerPort=stnIkePrefPeerPort, stnIkeCertificateTable=stnIkeCertificateTable, stnIkePrefLifeTime=stnIkePrefLifeTime, stnIkePreferenceTable=stnIkePreferenceTable, stnIkeCertificateIssuer=stnIkeCertificateIssuer, stnIkeSharedSecretEntry=stnIkeSharedSecretEntry, stnIkeCertificates=stnIkeCertificates, stnIkePrefLifeBytes=stnIkePrefLifeBytes, stnIkePrefAuthentication=stnIkePrefAuthentication, stnIkePrefDHGroup=stnIkePrefDHGroup, stnIkeCertificateType=stnIkeCertificateType, stnIkeCertificateIndex=stnIkeCertificateIndex, stnIkePrefEncryption=stnIkePrefEncryption, stnIkeCertificateEntry=stnIkeCertificateEntry, stnIkeCertificateDN=stnIkeCertificateDN, stnIkePreferences=stnIkePreferences, stnIkePrefServiceName=stnIkePrefServiceName, stnIkePrefHash=stnIkePrefHash, stnIkeCertificateAlias=stnIkeCertificateAlias, stnIkePrefCertAlias=stnIkePrefCertAlias, stnIkePrefTransform=stnIkePrefTransform, stnIkePrefPeerAddress=stnIkePrefPeerAddress, stnIkePreferenceEntry=stnIkePreferenceEntry, stnIkeSSPeerAddress=stnIkeSSPeerAddress, stnIkeObjects=stnIkeObjects, stnIKE=stnIKE, stnIkeSharedSecretTable=stnIkeSharedSecretTable, stnIkeSSSecret=stnIkeSSSecret, PYSNMP_MODULE_ID=stnIKE, stnIkeMibConformance=stnIkeMibConformance)
