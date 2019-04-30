#
# PySNMP MIB module Nortel-Magellan-Passport-SoftwareMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-SoftwareMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:18:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
DisplayString, Unsigned32, RowStatus, StorageType = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "DisplayString", "Unsigned32", "RowStatus", "StorageType")
AsciiStringIndex, Link, AsciiString, NonReplicated = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "AsciiStringIndex", "Link", "AsciiString", "NonReplicated")
components, passportMIBs = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "components", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, IpAddress, Unsigned32, ObjectIdentity, MibIdentifier, TimeTicks, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "IpAddress", "Unsigned32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
softwareMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17))
sw = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14))
swRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1), )
if mibBuilder.loadTexts: swRowStatusTable.setStatus('mandatory')
swRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"))
if mibBuilder.loadTexts: swRowStatusEntry.setStatus('mandatory')
swRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRowStatus.setStatus('mandatory')
swComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swComponentName.setStatus('mandatory')
swStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStorageType.setStatus('mandatory')
swIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: swIndex.setStatus('mandatory')
swOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11), )
if mibBuilder.loadTexts: swOperTable.setStatus('mandatory')
swOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"))
if mibBuilder.loadTexts: swOperEntry.setStatus('mandatory')
swTidyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inactive", 0), ("inProgress", 1), ("querying", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTidyStatus.setStatus('mandatory')
swAvBeingTidied = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 11, 1, 421), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvBeingTidied.setStatus('mandatory')
swAvlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256), )
if mibBuilder.loadTexts: swAvlTable.setStatus('mandatory')
swAvlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvlValue"))
if mibBuilder.loadTexts: swAvlEntry.setStatus('mandatory')
swAvlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swAvlValue.setStatus('mandatory')
swAvlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 256, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swAvlRowStatus.setStatus('mandatory')
swAvListToTidyTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 422), )
if mibBuilder.loadTexts: swAvListToTidyTable.setStatus('mandatory')
swAvListToTidyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 422, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvListToTidyValue"))
if mibBuilder.loadTexts: swAvListToTidyEntry.setStatus('mandatory')
swAvListToTidyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 422, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvListToTidyValue.setStatus('mandatory')
swAvListTidiedTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 423), )
if mibBuilder.loadTexts: swAvListTidiedTable.setStatus('mandatory')
swAvListTidiedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 423, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvListTidiedValue"))
if mibBuilder.loadTexts: swAvListTidiedEntry.setStatus('mandatory')
swAvListTidiedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 423, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvListTidiedValue.setStatus('mandatory')
swPatlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436), )
if mibBuilder.loadTexts: swPatlTable.setStatus('mandatory')
swPatlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swPatlValue"))
if mibBuilder.loadTexts: swPatlEntry.setStatus('mandatory')
swPatlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPatlValue.setStatus('mandatory')
swPatlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 436, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swPatlRowStatus.setStatus('mandatory')
swDld = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2))
swDldRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1), )
if mibBuilder.loadTexts: swDldRowStatusTable.setStatus('mandatory')
swDldRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"))
if mibBuilder.loadTexts: swDldRowStatusEntry.setStatus('mandatory')
swDldRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDldRowStatus.setStatus('mandatory')
swDldComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDldComponentName.setStatus('mandatory')
swDldStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDldStorageType.setStatus('mandatory')
swDldIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: swDldIndex.setStatus('mandatory')
swDldOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10), )
if mibBuilder.loadTexts: swDldOperTable.setStatus('mandatory')
swDldOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"))
if mibBuilder.loadTexts: swDldOperEntry.setStatus('mandatory')
swDldAvBeingDownloaded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDldAvBeingDownloaded.setStatus('mandatory')
swDldStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inactive", 0), ("inProgress", 1), ("stopping", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDldStatus.setStatus('mandatory')
swDldFilesToTransfer = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDldFilesToTransfer.setStatus('mandatory')
swDldProcessorTargets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 10, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDldProcessorTargets.setStatus('mandatory')
swDldDldListTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260), )
if mibBuilder.loadTexts: swDldDldListTable.setStatus('mandatory')
swDldDldListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldDldListValue"))
if mibBuilder.loadTexts: swDldDldListEntry.setStatus('mandatory')
swDldDldListValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDldDldListValue.setStatus('mandatory')
swDldDldListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 260, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swDldDldListRowStatus.setStatus('mandatory')
swDldDownloadedAvListTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 261), )
if mibBuilder.loadTexts: swDldDownloadedAvListTable.setStatus('mandatory')
swDldDownloadedAvListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 261, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swDldDownloadedAvListValue"))
if mibBuilder.loadTexts: swDldDownloadedAvListEntry.setStatus('mandatory')
swDldDownloadedAvListValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 2, 261, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDldDownloadedAvListValue.setStatus('mandatory')
swAv = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3))
swAvRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1), )
if mibBuilder.loadTexts: swAvRowStatusTable.setStatus('mandatory')
swAvRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"))
if mibBuilder.loadTexts: swAvRowStatusEntry.setStatus('mandatory')
swAvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvRowStatus.setStatus('mandatory')
swAvComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvComponentName.setStatus('mandatory')
swAvStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvStorageType.setStatus('mandatory')
swAvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 30)))
if mibBuilder.loadTexts: swAvIndex.setStatus('mandatory')
swAvOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 10), )
if mibBuilder.loadTexts: swAvOperTable.setStatus('mandatory')
swAvOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"))
if mibBuilder.loadTexts: swAvOperEntry.setStatus('mandatory')
swAvProcessorTargets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 10, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvProcessorTargets.setStatus('mandatory')
swAvCompatibleAvListTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 259), )
if mibBuilder.loadTexts: swAvCompatibleAvListTable.setStatus('mandatory')
swAvCompatibleAvListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 259, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvCompatibleAvListValue"))
if mibBuilder.loadTexts: swAvCompatibleAvListEntry.setStatus('mandatory')
swAvCompatibleAvListValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 259, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvCompatibleAvListValue.setStatus('mandatory')
swAvFeat = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2))
swAvFeatRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1), )
if mibBuilder.loadTexts: swAvFeatRowStatusTable.setStatus('mandatory')
swAvFeatRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvFeatIndex"))
if mibBuilder.loadTexts: swAvFeatRowStatusEntry.setStatus('mandatory')
swAvFeatRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvFeatRowStatus.setStatus('mandatory')
swAvFeatComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvFeatComponentName.setStatus('mandatory')
swAvFeatStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvFeatStorageType.setStatus('mandatory')
swAvFeatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 2, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 25)))
if mibBuilder.loadTexts: swAvFeatIndex.setStatus('mandatory')
swAvPatch = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3))
swAvPatchRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1), )
if mibBuilder.loadTexts: swAvPatchRowStatusTable.setStatus('mandatory')
swAvPatchRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvPatchIndex"))
if mibBuilder.loadTexts: swAvPatchRowStatusEntry.setStatus('mandatory')
swAvPatchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvPatchRowStatus.setStatus('mandatory')
swAvPatchComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvPatchComponentName.setStatus('mandatory')
swAvPatchStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvPatchStorageType.setStatus('mandatory')
swAvPatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 30)))
if mibBuilder.loadTexts: swAvPatchIndex.setStatus('mandatory')
swAvPatchOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 10), )
if mibBuilder.loadTexts: swAvPatchOperTable.setStatus('mandatory')
swAvPatchOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swAvPatchIndex"))
if mibBuilder.loadTexts: swAvPatchOperEntry.setStatus('mandatory')
swAvPatchDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 3, 3, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAvPatchDescription.setStatus('mandatory')
swLpt = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4))
swLptRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1), )
if mibBuilder.loadTexts: swLptRowStatusTable.setStatus('mandatory')
swLptRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"))
if mibBuilder.loadTexts: swLptRowStatusEntry.setStatus('mandatory')
swLptRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLptRowStatus.setStatus('mandatory')
swLptComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLptComponentName.setStatus('mandatory')
swLptStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLptStorageType.setStatus('mandatory')
swLptIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 25)))
if mibBuilder.loadTexts: swLptIndex.setStatus('mandatory')
swLptProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10), )
if mibBuilder.loadTexts: swLptProvTable.setStatus('mandatory')
swLptProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"))
if mibBuilder.loadTexts: swLptProvEntry.setStatus('mandatory')
swLptCommentText = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLptCommentText.setStatus('mandatory')
swLptSystemConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("default", 0))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLptSystemConfig.setStatus('mandatory')
swLptFlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257), )
if mibBuilder.loadTexts: swLptFlTable.setStatus('mandatory')
swLptFlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptFlValue"))
if mibBuilder.loadTexts: swLptFlEntry.setStatus('mandatory')
swLptFlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLptFlValue.setStatus('mandatory')
swLptFlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 257, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swLptFlRowStatus.setStatus('mandatory')
swLptLogicalProcessorsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 258), )
if mibBuilder.loadTexts: swLptLogicalProcessorsTable.setStatus('mandatory')
swLptLogicalProcessorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 258, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-SoftwareMIB", "swIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptIndex"), (0, "Nortel-Magellan-Passport-SoftwareMIB", "swLptLogicalProcessorsValue"))
if mibBuilder.loadTexts: swLptLogicalProcessorsEntry.setStatus('mandatory')
swLptLogicalProcessorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 14, 4, 258, 1, 1), Link()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swLptLogicalProcessorsValue.setStatus('mandatory')
softwareGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1))
softwareGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1, 5))
softwareGroupBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1, 5, 2))
softwareGroupBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 1, 5, 2, 2))
softwareCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3))
softwareCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3, 5))
softwareCapabilitiesBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3, 5, 2))
softwareCapabilitiesBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 17, 3, 5, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-SoftwareMIB", softwareCapabilitiesBE01A=softwareCapabilitiesBE01A, swDldDldListRowStatus=swDldDldListRowStatus, swAvPatchOperEntry=swAvPatchOperEntry, swLptSystemConfig=swLptSystemConfig, swDldDownloadedAvListValue=swDldDownloadedAvListValue, swAvListToTidyTable=swAvListToTidyTable, swAvStorageType=swAvStorageType, swLptLogicalProcessorsEntry=swLptLogicalProcessorsEntry, softwareCapabilitiesBE01=softwareCapabilitiesBE01, swLptIndex=swLptIndex, softwareCapabilities=softwareCapabilities, swLptProvTable=swLptProvTable, swAvlTable=swAvlTable, swLptComponentName=swLptComponentName, swAvFeatIndex=swAvFeatIndex, swAvPatchRowStatusEntry=swAvPatchRowStatusEntry, swLpt=swLpt, swAvRowStatusTable=swAvRowStatusTable, swDldDldListEntry=swDldDldListEntry, swAvRowStatus=swAvRowStatus, swDldOperTable=swDldOperTable, swAvFeatRowStatus=swAvFeatRowStatus, swAvPatchOperTable=swAvPatchOperTable, swComponentName=swComponentName, swAvFeat=swAvFeat, swDldDownloadedAvListEntry=swDldDownloadedAvListEntry, swDldFilesToTransfer=swDldFilesToTransfer, swDldProcessorTargets=swDldProcessorTargets, swLptFlRowStatus=swLptFlRowStatus, swAvListToTidyValue=swAvListToTidyValue, swAvRowStatusEntry=swAvRowStatusEntry, swDldComponentName=swDldComponentName, swAvOperEntry=swAvOperEntry, swLptRowStatusTable=swLptRowStatusTable, swDldOperEntry=swDldOperEntry, swAvPatchDescription=swAvPatchDescription, sw=sw, swLptLogicalProcessorsTable=swLptLogicalProcessorsTable, swLptFlEntry=swLptFlEntry, swDldRowStatusEntry=swDldRowStatusEntry, swAvFeatRowStatusTable=swAvFeatRowStatusTable, swDldRowStatus=swDldRowStatus, swPatlValue=swPatlValue, swAvPatchComponentName=swAvPatchComponentName, swAvPatchStorageType=swAvPatchStorageType, swLptRowStatusEntry=swLptRowStatusEntry, swAvListTidiedEntry=swAvListTidiedEntry, swAvPatch=swAvPatch, softwareCapabilitiesBE=softwareCapabilitiesBE, swTidyStatus=swTidyStatus, swDldStorageType=swDldStorageType, swAvPatchRowStatus=swAvPatchRowStatus, swAvCompatibleAvListEntry=swAvCompatibleAvListEntry, swRowStatusEntry=swRowStatusEntry, swAvPatchIndex=swAvPatchIndex, swRowStatus=swRowStatus, swLptProvEntry=swLptProvEntry, softwareGroupBE01=softwareGroupBE01, swPatlEntry=swPatlEntry, swAvComponentName=swAvComponentName, swIndex=swIndex, swAvFeatRowStatusEntry=swAvFeatRowStatusEntry, swLptFlTable=swLptFlTable, swDldIndex=swDldIndex, swLptFlValue=swLptFlValue, swAvIndex=swAvIndex, swAvListTidiedValue=swAvListTidiedValue, swLptRowStatus=swLptRowStatus, swAvOperTable=swAvOperTable, swAvPatchRowStatusTable=swAvPatchRowStatusTable, swOperEntry=swOperEntry, swAvFeatStorageType=swAvFeatStorageType, swDldAvBeingDownloaded=swDldAvBeingDownloaded, softwareGroup=softwareGroup, swAvListTidiedTable=swAvListTidiedTable, swLptCommentText=swLptCommentText, swRowStatusTable=swRowStatusTable, swAvProcessorTargets=swAvProcessorTargets, softwareGroupBE01A=softwareGroupBE01A, swAvlEntry=swAvlEntry, swAvlRowStatus=swAvlRowStatus, swLptLogicalProcessorsValue=swLptLogicalProcessorsValue, swOperTable=swOperTable, swAv=swAv, swPatlTable=swPatlTable, swStorageType=swStorageType, swDldDldListValue=swDldDldListValue, swAvListToTidyEntry=swAvListToTidyEntry, softwareGroupBE=softwareGroupBE, swDld=swDld, swDldDownloadedAvListTable=swDldDownloadedAvListTable, swLptStorageType=swLptStorageType, swAvlValue=swAvlValue, swPatlRowStatus=swPatlRowStatus, swDldRowStatusTable=swDldRowStatusTable, swDldStatus=swDldStatus, swAvCompatibleAvListValue=swAvCompatibleAvListValue, swDldDldListTable=swDldDldListTable, swAvFeatComponentName=swAvFeatComponentName, softwareMIB=softwareMIB, swAvCompatibleAvListTable=swAvCompatibleAvListTable, swAvBeingTidied=swAvBeingTidied)