#
# PySNMP MIB module MITEL-VOICE-MAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-VOICE-MAIL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, IpAddress, NotificationType, iso, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "IpAddress", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelVoiceMail = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 10))
mitelVoiceMail.setRevisions(('2002-03-24 11:49', '2002-04-02 00:00',))
if mibBuilder.loadTexts: mitelVoiceMail.setLastUpdated('200204020000Z')
if mibBuilder.loadTexts: mitelVoiceMail.setOrganization('MITEL Networks Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1))
mitelIdCallServers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2))
mitelIdCsIpera1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4))
mitelVoiceMailFaultTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 10, 1), )
if mibBuilder.loadTexts: mitelVoiceMailFaultTable.setStatus('current')
mitelVoiceMailFaultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1), ).setIndexNames((0, "MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultTblIndex"))
if mibBuilder.loadTexts: mitelVoiceMailFaultEntry.setStatus('current')
mitelVoiceMailFaultTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelVoiceMailFaultTblIndex.setStatus('current')
mitelVoiceMailFaultId = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("voiceMailDiskNearlyFull", 1), ("voiceMailDiskFull", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelVoiceMailFaultId.setStatus('current')
mitelVoiceMailFaultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("set", 1), ("clear", 2), ("message", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelVoiceMailFaultStatus.setStatus('current')
mitelVoiceMailFaultOccur = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 10, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelVoiceMailFaultOccur.setStatus('current')
mitelIpera1000Notifications = NotificationGroup((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)).setObjects(("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailDiskNearlyFullNotif"), ("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailDiskFullNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelIpera1000Notifications = mitelIpera1000Notifications.setStatus('current')
mitelVoiceMailDiskNearlyFullNotif = NotificationType((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 408)).setObjects(("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultStatus"), ("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultOccur"))
if mibBuilder.loadTexts: mitelVoiceMailDiskNearlyFullNotif.setStatus('current')
mitelVoiceMailDiskFullNotif = NotificationType((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 409)).setObjects(("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultStatus"), ("MITEL-VOICE-MAIL-MIB", "mitelVoiceMailFaultOccur"))
if mibBuilder.loadTexts: mitelVoiceMailDiskFullNotif.setStatus('current')
mibBuilder.exportSymbols("MITEL-VOICE-MAIL-MIB", PYSNMP_MODULE_ID=mitelVoiceMail, mitelVoiceMail=mitelVoiceMail, mitelVoiceMailFaultStatus=mitelVoiceMailFaultStatus, mitelVoiceMailFaultEntry=mitelVoiceMailFaultEntry, mitelVoiceMailFaultId=mitelVoiceMailFaultId, mitelVoiceMailFaultOccur=mitelVoiceMailFaultOccur, mitelVoiceMailDiskNearlyFullNotif=mitelVoiceMailDiskNearlyFullNotif, mitelVoiceMailDiskFullNotif=mitelVoiceMailDiskFullNotif, mitel=mitel, mitelIdCallServers=mitelIdCallServers, mitelProprietary=mitelProprietary, mitelVoiceMailFaultTable=mitelVoiceMailFaultTable, mitelIpera1000Notifications=mitelIpera1000Notifications, mitelVoiceMailFaultTblIndex=mitelVoiceMailFaultTblIndex, mitelIdentification=mitelIdentification, mitelIdCsIpera1000=mitelIdCsIpera1000)
