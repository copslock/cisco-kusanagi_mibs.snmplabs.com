#
# PySNMP MIB module NEOTERIS-IVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NEOTERIS-IVE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, TimeTicks, Counter32, ModuleIdentity, Unsigned32, Integer32, MibIdentifier, Bits, Gauge32, enterprises, ObjectIdentity, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "TimeTicks", "Counter32", "ModuleIdentity", "Unsigned32", "Integer32", "MibIdentifier", "Bits", "Gauge32", "enterprises", "ObjectIdentity", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
neoteris = ModuleIdentity((1, 3, 6, 1, 4, 1, 12532))
neoteris.setRevisions(('2002-03-25 00:00',))
if mibBuilder.loadTexts: neoteris.setLastUpdated('200203250000Z')
if mibBuilder.loadTexts: neoteris.setOrganization('Juniper')
logFullPercent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logFullPercent.setStatus('current')
signedInWebUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInWebUsers.setStatus('current')
signedInMailUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInMailUsers.setStatus('current')
blockedIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: blockedIP.setStatus('current')
authServerName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authServerName.setStatus('current')
productName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
productVersion = MibScalar((1, 3, 6, 1, 4, 1, 12532, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productVersion.setStatus('current')
fileName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileName.setStatus('current')
meetingUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meetingUserCount.setStatus('current')
iveCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveCpuUtil.setStatus('current')
iveMemoryUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveMemoryUtil.setStatus('current')
iveConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveConcurrentUsers.setStatus('current')
clusterConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterConcurrentUsers.setStatus('current')
iveTotalHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTotalHits.setStatus('current')
iveFileHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveFileHits.setStatus('current')
iveWebHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveWebHits.setStatus('current')
iveAppletHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveAppletHits.setStatus('current')
ivetermHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ivetermHits.setStatus('current')
iveSAMHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSAMHits.setStatus('current')
iveNCHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveNCHits.setStatus('current')
meetingHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meetingHits.setStatus('current')
iveTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 251))
iveLogNearlyFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 4)).setObjects(("NEOTERIS-IVE-MIB", "logFullPercent"))
if mibBuilder.loadTexts: iveLogNearlyFull.setStatus('current')
iveLogFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 5))
if mibBuilder.loadTexts: iveLogFull.setStatus('current')
iveMaxConcurrentUsersSignedIn = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 6))
if mibBuilder.loadTexts: iveMaxConcurrentUsersSignedIn.setStatus('current')
iveTooManyFailedLoginAttempts = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 7)).setObjects(("NEOTERIS-IVE-MIB", "blockedIP"))
if mibBuilder.loadTexts: iveTooManyFailedLoginAttempts.setStatus('current')
externalAuthServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 8)).setObjects(("NEOTERIS-IVE-MIB", "authServerName"))
if mibBuilder.loadTexts: externalAuthServerUnreachable.setStatus('current')
iveStart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 9))
if mibBuilder.loadTexts: iveStart.setStatus('current')
iveShutdown = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 10))
if mibBuilder.loadTexts: iveShutdown.setStatus('current')
iveReboot = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 11))
if mibBuilder.loadTexts: iveReboot.setStatus('current')
archiveServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 12))
if mibBuilder.loadTexts: archiveServerUnreachable.setStatus('current')
archiveServerLoginFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 13))
if mibBuilder.loadTexts: archiveServerLoginFailed.setStatus('current')
archiveFileTransferFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 14)).setObjects(("NEOTERIS-IVE-MIB", "fileName"))
if mibBuilder.loadTexts: archiveFileTransferFailed.setStatus('current')
meetingUserLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 15)).setObjects(("NEOTERIS-IVE-MIB", "meetingUserCount"))
if mibBuilder.loadTexts: meetingUserLimit.setStatus('current')
iveRestart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 16))
if mibBuilder.loadTexts: iveRestart.setStatus('current')
mibBuilder.exportSymbols("NEOTERIS-IVE-MIB", iveShutdown=iveShutdown, iveAppletHits=iveAppletHits, archiveServerUnreachable=archiveServerUnreachable, signedInMailUsers=signedInMailUsers, signedInWebUsers=signedInWebUsers, archiveFileTransferFailed=archiveFileTransferFailed, iveConcurrentUsers=iveConcurrentUsers, productVersion=productVersion, iveWebHits=iveWebHits, iveTotalHits=iveTotalHits, iveStart=iveStart, fileName=fileName, blockedIP=blockedIP, iveCpuUtil=iveCpuUtil, externalAuthServerUnreachable=externalAuthServerUnreachable, meetingUserLimit=meetingUserLimit, productName=productName, meetingHits=meetingHits, iveLogFull=iveLogFull, iveMaxConcurrentUsersSignedIn=iveMaxConcurrentUsersSignedIn, logFullPercent=logFullPercent, iveMemoryUtil=iveMemoryUtil, iveReboot=iveReboot, iveNCHits=iveNCHits, neoteris=neoteris, iveFileHits=iveFileHits, archiveServerLoginFailed=archiveServerLoginFailed, iveSAMHits=iveSAMHits, PYSNMP_MODULE_ID=neoteris, iveTooManyFailedLoginAttempts=iveTooManyFailedLoginAttempts, iveTraps=iveTraps, clusterConcurrentUsers=clusterConcurrentUsers, ivetermHits=ivetermHits, meetingUserCount=meetingUserCount, authServerName=authServerName, iveRestart=iveRestart, iveLogNearlyFull=iveLogNearlyFull)
