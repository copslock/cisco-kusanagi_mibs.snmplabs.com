#
# PySNMP MIB module CISCOSB-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SSH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, Counter64, iso, Counter32, ModuleIdentity, TimeTicks, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Counter64", "iso", "Counter32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ObjectIdentity", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlSsh = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78))
rlSsh.setRevisions(('2003-01-03 00:24', '2003-09-21 00:24',))
if mibBuilder.loadTexts: rlSsh.setLastUpdated('200209300024Z')
if mibBuilder.loadTexts: rlSsh.setOrganization('Cisco Small Business')
class RlSshPublicKeyAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 999))
    namedValues = NamedValues(("rsa1", 0), ("rsa", 1), ("dsa", 2), ("none", 999))

class RlSshPublicKeyDigestFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("hex", 0), ("bubbleBabble", 1))

rlSshMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshMibVersion.setStatus('current')
rlSshServer = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2))
rlSshServerHostPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 1), )
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTable.setStatus('current')
rlSshServerHostPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 1, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshServerHostPublicKeyAlgorithm"), (0, "CISCOSB-SSH-MIB", "rlSshServerHostPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTableEntry.setStatus('current')
rlSshServerHostPublicKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 1, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyAlgorithm.setStatus('current')
rlSshServerHostPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentId.setStatus('current')
rlSshServerHostPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentText.setStatus('current')
rlSshServerHostPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 2), )
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTable.setStatus('current')
rlSshServerHostPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 2, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshServerHostPublicKeyFingerprintAlgorithm"), (0, "CISCOSB-SSH-MIB", "rlSshServerHostPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTableEntry.setStatus('current')
rlSshServerHostPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 2, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintAlgorithm.setStatus('current')
rlSshServerHostPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 2, 1, 2), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintDigestFormat.setStatus('current')
rlSshServerHostPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprint.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 3), )
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTable.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 3, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshServerAuthorizedUserName"), (0, "CISCOSB-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTableEntry.setStatus('current')
rlSshServerAuthorizedUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserName.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentId.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentText.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFragmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 3, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentStatus.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 5), )
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTable.setStatus('current')
rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 5, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshServerAuthorizedUserFingerprintName"), (0, "CISCOSB-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry.setStatus('current')
rlSshServerAuthorizedUserFingerprintName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserFingerprintName.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 5, 1, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 5, 1, 3), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat.setStatus('current')
rlSshServerAuthorizedUserPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprint.setStatus('current')
rlSshServerSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6), )
if mibBuilder.loadTexts: rlSshServerSessionTable.setStatus('current')
rlSshServerSessionTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshServerSessionIdentifier"))
if mibBuilder.loadTexts: rlSshServerSessionTableEntry.setStatus('current')
rlSshServerSessionIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionIdentifier.setStatus('current')
rlSshServerSessionPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerAddress.setStatus('current')
rlSshServerSessionPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerPort.setStatus('current')
rlSshServerSessionPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerVersion.setStatus('current')
rlSshServerSessionUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionUsername.setStatus('current')
rlSshServerSessionCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionCipher.setStatus('current')
rlSshServerSessionHMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionHMAC.setStatus('current')
rlSshServerSessionInetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7), )
if mibBuilder.loadTexts: rlSshServerSessionInetTable.setStatus('current')
rlSshServerSessionInetTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshServerSessionInetIdentifier"))
if mibBuilder.loadTexts: rlSshServerSessionInetTableEntry.setStatus('current')
rlSshServerSessionInetIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetIdentifier.setStatus('current')
rlSshServerSessionInetPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetPeerAddressType.setStatus('current')
rlSshServerSessionInetPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetPeerAddress.setStatus('current')
rlSshServerSessionInetPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetPeerPort.setStatus('current')
rlSshServerSessionInetPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetPeerVersion.setStatus('current')
rlSshServerSessionInetUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetUsername.setStatus('current')
rlSshServerSessionInetCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetCipher.setStatus('current')
rlSshServerSessionInetHMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 7, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionInetHMAC.setStatus('current')
rlSshServerImportExportSelfKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 8), )
if mibBuilder.loadTexts: rlSshServerImportExportSelfKeyTable.setStatus('current')
rlSshServerImportExportSelfKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 8, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshServerImportExportSelfKeyAlgorithm"), (0, "CISCOSB-SSH-MIB", "rlSshServerImportExportSelfKeyFormat"), (0, "CISCOSB-SSH-MIB", "rlSshServerImportExportSelfKeyFragmentId"))
if mibBuilder.loadTexts: rlSshServerImportExportSelfKeyEntry.setStatus('current')
rlSshServerImportExportSelfKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 8, 1, 1), RlSshPublicKeyAlgorithm())
if mibBuilder.loadTexts: rlSshServerImportExportSelfKeyAlgorithm.setStatus('current')
rlSshServerImportExportSelfKeyFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("uuencoded-format", 1))))
if mibBuilder.loadTexts: rlSshServerImportExportSelfKeyFormat.setStatus('current')
rlSshServerImportExportSelfKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 8, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSshServerImportExportSelfKeyFragmentId.setStatus('current')
rlSshServerImportExportSelfKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 8, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerImportExportSelfKeyFragmentText.setStatus('current')
rlSshServerPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 101), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerPort.setStatus('current')
rlSshServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 102), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnable.setStatus('current')
rlSshServerEnablePublicKeyAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 103), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnablePublicKeyAuthentication.setStatus('current')
rlSshServerRegenerateHostKey = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 104), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerRegenerateHostKey.setStatus('current')
rlSshServerDefaultKeyFlag = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 105), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("rsa", 1), ("dsa", 2), ("all", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerDefaultKeyFlag.setStatus('current')
rlSshServerDeleteSelfKey = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 106), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerDeleteSelfKey.setStatus('current')
rlSshServerEnablePublicKeyAuthAutoLogin = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 107), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnablePublicKeyAuthAutoLogin.setStatus('current')
rlSshServerEnablePasswordAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 2, 108), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnablePasswordAuthentication.setStatus('current')
rlSshClient = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3))
rlSshClientUserName = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 70)).clone('anonymous')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientUserName.setStatus('current')
rlSshClientRegenerateSelfKey = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientRegenerateSelfKey.setStatus('current')
rlSshClientSelfPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 3), )
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTable.setStatus('current')
rlSshClientSelfPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 3, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshClientSelfPublicKeyAlgorithm"), (0, "CISCOSB-SSH-MIB", "rlSshClientSelfPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTableEntry.setStatus('current')
rlSshClientSelfPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentId.setStatus('current')
rlSshClientSelfPublicKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 3, 1, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyAlgorithm.setStatus('current')
rlSshClientSelfPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentText.setStatus('current')
rlSshClientSelfPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 4), )
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTable.setStatus('current')
rlSshClientSelfPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 4, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintAlgorithm"), (0, "CISCOSB-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTableEntry.setStatus('current')
rlSshClientSelfPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 4, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintAlgorithm.setStatus('current')
rlSshClientSelfPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 4, 1, 2), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintDigestFormat.setStatus('current')
rlSshClientSelfPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprint.setStatus('current')
rlSshClientAuthenticationMethod = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("public-key-rsa", 1), ("public-key-dsa", 2), ("password", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientAuthenticationMethod.setStatus('current')
rlSshClientPassword = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 70))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientPassword.setStatus('current')
rlSshClientPasswordChangeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7), )
if mibBuilder.loadTexts: rlSshClientPasswordChangeTable.setStatus('current')
rlSshClientPasswordChangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshClientPasswordChangeInetAddrType"), (0, "CISCOSB-SSH-MIB", "rlSshClientPasswordChangeInetAddr"))
if mibBuilder.loadTexts: rlSshClientPasswordChangeEntry.setStatus('current')
rlSshClientPasswordChangeInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlSshClientPasswordChangeInetAddrType.setStatus('current')
rlSshClientPasswordChangeInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1, 2), InetAddress())
if mibBuilder.loadTexts: rlSshClientPasswordChangeInetAddr.setStatus('current')
rlSshClientPasswordChangeUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 70))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientPasswordChangeUsername.setStatus('current')
rlSshClientPasswordChangeOldPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 70))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientPasswordChangeOldPassword.setStatus('current')
rlSshClientPasswordChangeNewPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 70))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientPasswordChangeNewPassword.setStatus('current')
rlSshClientPasswordChangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("succeeded", 2), ("failed", 3), ("noData", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientPasswordChangeStatus.setStatus('current')
rlSshClientPasswordChangeFailureReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 7, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientPasswordChangeFailureReason.setStatus('current')
rlSshClientDeleteSelfKey = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 8), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientDeleteSelfKey.setStatus('current')
rlSshClientImportExportSelfKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 9), )
if mibBuilder.loadTexts: rlSshClientImportExportSelfKeyTable.setStatus('current')
rlSshClientImportExportSelfKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 9, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshClientImportExportSelfKeyAlgorithm"), (0, "CISCOSB-SSH-MIB", "rlSshClientImportExportSelfKeyFormat"), (0, "CISCOSB-SSH-MIB", "rlSshClientImportExportSelfKeyFragmentId"))
if mibBuilder.loadTexts: rlSshClientImportExportSelfKeyEntry.setStatus('current')
rlSshClientImportExportSelfKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 9, 1, 1), RlSshPublicKeyAlgorithm())
if mibBuilder.loadTexts: rlSshClientImportExportSelfKeyAlgorithm.setStatus('current')
rlSshClientImportExportSelfKeyFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("uuencoded-format", 1))))
if mibBuilder.loadTexts: rlSshClientImportExportSelfKeyFormat.setStatus('current')
rlSshClientImportExportSelfKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 9, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSshClientImportExportSelfKeyFragmentId.setStatus('current')
rlSshClientImportExportSelfKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 9, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientImportExportSelfKeyFragmentText.setStatus('current')
rlSshClientRemoteServerPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 10), )
if mibBuilder.loadTexts: rlSshClientRemoteServerPublicKeyFingerprintTable.setStatus('current')
rlSshClientRemoteServerPublicKeyFingerprintEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 10, 1), ).setIndexNames((0, "CISCOSB-SSH-MIB", "rlSshClientRemoteServerFingerprintInetAddrType"), (0, "CISCOSB-SSH-MIB", "rlSshClientRemoteServerFingerprintInetAddr"), (0, "CISCOSB-SSH-MIB", "rlSshClientRemoteServerFingerprint"))
if mibBuilder.loadTexts: rlSshClientRemoteServerPublicKeyFingerprintEntry.setStatus('current')
rlSshClientRemoteServerFingerprintInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 10, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlSshClientRemoteServerFingerprintInetAddrType.setStatus('current')
rlSshClientRemoteServerFingerprintInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 10, 1, 2), InetAddress())
if mibBuilder.loadTexts: rlSshClientRemoteServerFingerprintInetAddr.setStatus('current')
rlSshClientRemoteServerFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 10, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSshClientRemoteServerFingerprint.setStatus('current')
rlSshClientRemoteServerFingerprintStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSshClientRemoteServerFingerprintStatus.setStatus('current')
rlSshClientRemoteServersAuthenticationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientRemoteServersAuthenticationEnable.setStatus('current')
rlSshClientDefaultKeyFlag = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78, 3, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("rsa", 1), ("dsa", 2), ("all", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientDefaultKeyFlag.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SSH-MIB", rlSshServerHostPublicKeyFingerprintTableEntry=rlSshServerHostPublicKeyFingerprintTableEntry, rlSshClientRemoteServerFingerprint=rlSshClientRemoteServerFingerprint, rlSshServerAuthorizedUserFingerprintName=rlSshServerAuthorizedUserFingerprintName, rlSshClientImportExportSelfKeyAlgorithm=rlSshClientImportExportSelfKeyAlgorithm, rlSshClientRemoteServerFingerprintInetAddrType=rlSshClientRemoteServerFingerprintInetAddrType, rlSshClientPasswordChangeFailureReason=rlSshClientPasswordChangeFailureReason, PYSNMP_MODULE_ID=rlSsh, rlSshServerSessionCipher=rlSshServerSessionCipher, rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm=rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm, rlSshServerSessionInetPeerAddress=rlSshServerSessionInetPeerAddress, rlSshServerImportExportSelfKeyEntry=rlSshServerImportExportSelfKeyEntry, rlSshClientSelfPublicKeyFragmentId=rlSshClientSelfPublicKeyFragmentId, rlSshServerSessionInetUsername=rlSshServerSessionInetUsername, rlSshServerEnablePublicKeyAuthAutoLogin=rlSshServerEnablePublicKeyAuthAutoLogin, rlSshClientPasswordChangeEntry=rlSshClientPasswordChangeEntry, rlSshServerEnablePasswordAuthentication=rlSshServerEnablePasswordAuthentication, rlSshServerSessionPeerVersion=rlSshServerSessionPeerVersion, rlSshServer=rlSshServer, rlSshServerSessionHMAC=rlSshServerSessionHMAC, rlSshClientImportExportSelfKeyFragmentId=rlSshClientImportExportSelfKeyFragmentId, rlSshServerSessionInetPeerVersion=rlSshServerSessionInetPeerVersion, rlSshClientPasswordChangeInetAddrType=rlSshClientPasswordChangeInetAddrType, rlSshServerSessionInetIdentifier=rlSshServerSessionInetIdentifier, rlSshMibVersion=rlSshMibVersion, rlSshClientRemoteServerFingerprintInetAddr=rlSshClientRemoteServerFingerprintInetAddr, rlSshClientUserName=rlSshClientUserName, rlSshServerSessionTableEntry=rlSshServerSessionTableEntry, rlSshServerImportExportSelfKeyFormat=rlSshServerImportExportSelfKeyFormat, rlSshClientImportExportSelfKeyFragmentText=rlSshClientImportExportSelfKeyFragmentText, rlSshServerHostPublicKeyFingerprintTable=rlSshServerHostPublicKeyFingerprintTable, rlSshServerSessionInetPeerAddressType=rlSshServerSessionInetPeerAddressType, rlSshServerEnablePublicKeyAuthentication=rlSshServerEnablePublicKeyAuthentication, rlSshClientSelfPublicKeyTableEntry=rlSshClientSelfPublicKeyTableEntry, rlSshServerAuthorizedUserPublicKeyFragmentText=rlSshServerAuthorizedUserPublicKeyFragmentText, rlSshClientPasswordChangeNewPassword=rlSshClientPasswordChangeNewPassword, rlSshServerAuthorizedUserName=rlSshServerAuthorizedUserName, rlSshClientRemoteServerPublicKeyFingerprintTable=rlSshClientRemoteServerPublicKeyFingerprintTable, rlSshClientRemoteServerFingerprintStatus=rlSshClientRemoteServerFingerprintStatus, RlSshPublicKeyDigestFormat=RlSshPublicKeyDigestFormat, rlSshServerAuthorizedUsersPublicKeyTable=rlSshServerAuthorizedUsersPublicKeyTable, rlSshClientImportExportSelfKeyEntry=rlSshClientImportExportSelfKeyEntry, rlSshClientPasswordChangeOldPassword=rlSshClientPasswordChangeOldPassword, rlSshClientSelfPublicKeyFingerprintDigestFormat=rlSshClientSelfPublicKeyFingerprintDigestFormat, rlSshClientPasswordChangeTable=rlSshClientPasswordChangeTable, rlSshServerSessionInetHMAC=rlSshServerSessionInetHMAC, rlSshServerHostPublicKeyFingerprint=rlSshServerHostPublicKeyFingerprint, rlSshClientDeleteSelfKey=rlSshClientDeleteSelfKey, rlSshServerAuthorizedUserPublicKeyFragmentId=rlSshServerAuthorizedUserPublicKeyFragmentId, rlSshServerImportExportSelfKeyFragmentText=rlSshServerImportExportSelfKeyFragmentText, rlSshServerHostPublicKeyFingerprintAlgorithm=rlSshServerHostPublicKeyFingerprintAlgorithm, rlSshServerHostPublicKeyFingerprintDigestFormat=rlSshServerHostPublicKeyFingerprintDigestFormat, RlSshPublicKeyAlgorithm=RlSshPublicKeyAlgorithm, rlSshServerAuthorizedUsersPublicKeyTableEntry=rlSshServerAuthorizedUsersPublicKeyTableEntry, rlSshClientDefaultKeyFlag=rlSshClientDefaultKeyFlag, rlSshServerHostPublicKeyFragmentId=rlSshServerHostPublicKeyFragmentId, rlSshServerPort=rlSshServerPort, rlSshServerImportExportSelfKeyTable=rlSshServerImportExportSelfKeyTable, rlSshClientPassword=rlSshClientPassword, rlSshClientAuthenticationMethod=rlSshClientAuthenticationMethod, rlSshClientSelfPublicKeyFragmentText=rlSshClientSelfPublicKeyFragmentText, rlSshServerRegenerateHostKey=rlSshServerRegenerateHostKey, rlSshClient=rlSshClient, rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry=rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry, rlSshServerEnable=rlSshServerEnable, rlSshServerImportExportSelfKeyAlgorithm=rlSshServerImportExportSelfKeyAlgorithm, rlSsh=rlSsh, rlSshServerSessionIdentifier=rlSshServerSessionIdentifier, rlSshServerSessionInetTableEntry=rlSshServerSessionInetTableEntry, rlSshServerDefaultKeyFlag=rlSshServerDefaultKeyFlag, rlSshServerAuthorizedUserPublicKeyFingerprint=rlSshServerAuthorizedUserPublicKeyFingerprint, rlSshClientSelfPublicKeyTable=rlSshClientSelfPublicKeyTable, rlSshClientRemoteServerPublicKeyFingerprintEntry=rlSshClientRemoteServerPublicKeyFingerprintEntry, rlSshClientSelfPublicKeyAlgorithm=rlSshClientSelfPublicKeyAlgorithm, rlSshServerHostPublicKeyFragmentText=rlSshServerHostPublicKeyFragmentText, rlSshServerSessionInetTable=rlSshServerSessionInetTable, rlSshClientRegenerateSelfKey=rlSshClientRegenerateSelfKey, rlSshClientPasswordChangeUsername=rlSshClientPasswordChangeUsername, rlSshClientSelfPublicKeyFingerprintAlgorithm=rlSshClientSelfPublicKeyFingerprintAlgorithm, rlSshServerSessionTable=rlSshServerSessionTable, rlSshServerDeleteSelfKey=rlSshServerDeleteSelfKey, rlSshServerImportExportSelfKeyFragmentId=rlSshServerImportExportSelfKeyFragmentId, rlSshClientPasswordChangeInetAddr=rlSshClientPasswordChangeInetAddr, rlSshClientPasswordChangeStatus=rlSshClientPasswordChangeStatus, rlSshClientSelfPublicKeyFingerprint=rlSshClientSelfPublicKeyFingerprint, rlSshClientImportExportSelfKeyTable=rlSshClientImportExportSelfKeyTable, rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat=rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat, rlSshServerAuthorizedUsersPublicKeyFingerprintTable=rlSshServerAuthorizedUsersPublicKeyFingerprintTable, rlSshServerSessionUsername=rlSshServerSessionUsername, rlSshServerHostPublicKeyTableEntry=rlSshServerHostPublicKeyTableEntry, rlSshServerSessionInetPeerPort=rlSshServerSessionInetPeerPort, rlSshClientSelfPublicKeyFingerprintTableEntry=rlSshClientSelfPublicKeyFingerprintTableEntry, rlSshClientSelfPublicKeyFingerprintTable=rlSshClientSelfPublicKeyFingerprintTable, rlSshServerHostPublicKeyTable=rlSshServerHostPublicKeyTable, rlSshServerHostPublicKeyAlgorithm=rlSshServerHostPublicKeyAlgorithm, rlSshServerSessionPeerAddress=rlSshServerSessionPeerAddress, rlSshServerSessionInetCipher=rlSshServerSessionInetCipher, rlSshServerSessionPeerPort=rlSshServerSessionPeerPort, rlSshClientRemoteServersAuthenticationEnable=rlSshClientRemoteServersAuthenticationEnable, rlSshClientImportExportSelfKeyFormat=rlSshClientImportExportSelfKeyFormat, rlSshServerAuthorizedUserPublicKeyFragmentStatus=rlSshServerAuthorizedUserPublicKeyFragmentStatus)
