#
# PySNMP MIB module JUNIPER-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/JUNIPER-LICENSE-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:32:25 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
jnxLicenseMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxLicenseMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, Gauge32, MibIdentifier, Integer32, Bits, NotificationType, Unsigned32, IpAddress, Counter32, iso, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "Bits", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "iso", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1))
jnxLicenseMIB.setRevisions(('2010-07-09 00:00',))
if mibBuilder.loadTexts: jnxLicenseMIB.setLastUpdated('201007090000Z')
if mibBuilder.loadTexts: jnxLicenseMIB.setOrganization('Juniper Networks, Inc.')
jnxLicenseNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0))
jnxLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1))
jnxLicenseInstallObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1))
jnxLicenseSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2))
jnxLicenseInstallTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLicenseInstallTable.setStatus('current')
jnxLicenseInstallEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LICENSE-MIB", "jnxLicenseId"))
if mibBuilder.loadTexts: jnxLicenseInstallEntry.setStatus('current')
jnxLicenseId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: jnxLicenseId.setStatus('current')
jnxLicenseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseVersion.setStatus('current')
jnxLicenseDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseDeviceId.setStatus('current')
jnxLicenseType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("invalid", 0), ("count-down", 1), ("date-based", 2), ("permanent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseType.setStatus('current')
jnxLicenseKeys = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseKeys.setStatus('current')
jnxLicenseFeatureListTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2), )
if mibBuilder.loadTexts: jnxLicenseFeatureListTable.setStatus('current')
jnxLicenseFeatureListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1), ).setIndexNames((0, "JUNIPER-LICENSE-MIB", "jnxLicenseFeatureId"))
if mibBuilder.loadTexts: jnxLicenseFeatureListEntry.setStatus('current')
jnxLicenseFeatureId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: jnxLicenseFeatureId.setStatus('current')
jnxLicenseFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureName.setStatus('current')
jnxLicenseFeatureDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureDescr.setStatus('current')
jnxLicenseFeatureLicenseId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseId.setStatus('current')
jnxLicenseFeatureLicenseUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseUsed.setStatus('current')
jnxLicenseFeatureLicenseInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseInstalled.setStatus('current')
jnxLicenseFeatureLicenseNeeded = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseFeatureLicenseNeeded.setStatus('current')
jnxLicenseRenewBeforExpiration = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseRenewBeforExpiration.setStatus('current')
jnxLicenseRenewInterval = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseRenewInterval.setStatus('current')
jnxLicenseAutoUpdate = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLicenseAutoUpdate.setStatus('current')
jnxLicenseGraceExpired = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 1)).setObjects(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"))
if mibBuilder.loadTexts: jnxLicenseGraceExpired.setStatus('current')
jnxLicenseGraceAboutToExpire = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 2)).setObjects(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"))
if mibBuilder.loadTexts: jnxLicenseGraceAboutToExpire.setStatus('current')
jnxLicenseAboutToExpire = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 3)).setObjects(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"))
if mibBuilder.loadTexts: jnxLicenseAboutToExpire.setStatus('current')
jnxLicenseInfringeCumulative = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 4)).setObjects(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"))
if mibBuilder.loadTexts: jnxLicenseInfringeCumulative.setStatus('current')
jnxLicenseInfringeSingle = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 63, 1, 0, 5)).setObjects(("JUNIPER-LICENSE-MIB", "jnxLicenseFeatureName"))
if mibBuilder.loadTexts: jnxLicenseInfringeSingle.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-LICENSE-MIB", jnxLicenseInstallObjects=jnxLicenseInstallObjects, jnxLicenseAboutToExpire=jnxLicenseAboutToExpire, jnxLicenseGraceExpired=jnxLicenseGraceExpired, jnxLicenseFeatureLicenseUsed=jnxLicenseFeatureLicenseUsed, jnxLicenseNotifications=jnxLicenseNotifications, jnxLicenseFeatureDescr=jnxLicenseFeatureDescr, jnxLicenseMIB=jnxLicenseMIB, jnxLicenseFeatureId=jnxLicenseFeatureId, jnxLicenseFeatureListEntry=jnxLicenseFeatureListEntry, jnxLicenseRenewBeforExpiration=jnxLicenseRenewBeforExpiration, PYSNMP_MODULE_ID=jnxLicenseMIB, jnxLicenseObjects=jnxLicenseObjects, jnxLicenseDeviceId=jnxLicenseDeviceId, jnxLicenseId=jnxLicenseId, jnxLicenseVersion=jnxLicenseVersion, jnxLicenseAutoUpdate=jnxLicenseAutoUpdate, jnxLicenseInfringeCumulative=jnxLicenseInfringeCumulative, jnxLicenseType=jnxLicenseType, jnxLicenseFeatureName=jnxLicenseFeatureName, jnxLicenseFeatureLicenseId=jnxLicenseFeatureLicenseId, jnxLicenseSettings=jnxLicenseSettings, jnxLicenseGraceAboutToExpire=jnxLicenseGraceAboutToExpire, jnxLicenseInstallEntry=jnxLicenseInstallEntry, jnxLicenseKeys=jnxLicenseKeys, jnxLicenseFeatureListTable=jnxLicenseFeatureListTable, jnxLicenseRenewInterval=jnxLicenseRenewInterval, jnxLicenseFeatureLicenseInstalled=jnxLicenseFeatureLicenseInstalled, jnxLicenseFeatureLicenseNeeded=jnxLicenseFeatureLicenseNeeded, jnxLicenseInfringeSingle=jnxLicenseInfringeSingle, jnxLicenseInstallTable=jnxLicenseInstallTable)
