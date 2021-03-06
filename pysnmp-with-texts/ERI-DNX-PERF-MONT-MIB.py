#
# PySNMP MIB module ERI-DNX-PERF-MONT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-PERF-MONT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
dnx, LinkPortAddress = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "dnx", "LinkPortAddress")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Unsigned32, Integer32, Counter64, TimeTicks, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Unsigned32", "Integer32", "Counter64", "TimeTicks", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter32", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eriDNXLinkPMStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 7))
if mibBuilder.loadTexts: eriDNXLinkPMStatsMIB.setLastUpdated('200204110000Z')
if mibBuilder.loadTexts: eriDNXLinkPMStatsMIB.setOrganization('Eastern Research, Inc.')
if mibBuilder.loadTexts: eriDNXLinkPMStatsMIB.setContactInfo('Customer Service Postal: Eastern Research, Inc. 225 Executive Drive Moorestown, NJ 08057 Phone: +1-800-337-4374 Email: support@erinc.com')
if mibBuilder.loadTexts: eriDNXLinkPMStatsMIB.setDescription('The ERI Enterprise MIB Module for the DNX DSx1 Performance Monitoring.')
performanceMonitoring = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 4))
dsx1Esf = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1))
dsx1G826 = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2))
dsx1EsfCurrTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1), )
if mibBuilder.loadTexts: dsx1EsfCurrTable.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrTable.setDescription('This is the DS1/E1 ESF Current Statistics table which consists of an entry for each DS1 link in the system that is configured for T1 ESF lines. This table provides the counters for the current 15 minute time interval.')
dsx1EsfCurrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1), ).setIndexNames((0, "ERI-DNX-PERF-MONT-MIB", "dsx1EsfCurrLinkAddr"))
if mibBuilder.loadTexts: dsx1EsfCurrEntry.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrEntry.setDescription('The conceptual row of the DS1/E1 ESF Statistics table. A row in this table cannot be added, deleted, or modified directly. Rows may be removed or added by configuring the DS1 line type via the appropriate Device Provisioning table.')
dsx1EsfCurrLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrLinkAddr.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrLinkAddr.setDescription('This number uniquely identifies an DS1/E1 link resource. This number will be used throughout the system to identify a unique link. The format is represented using an IP address syntax (4 byte string). Note that the maximum valid link number will vary depending on the specified carrier and framing options. For example, an octal T1/E1 device has 8 DS1 links however the DS3 has 28 DS1 links. The 1st byte is reserved for future Nest Number use The 2nd byte represents the Slot Number (1-11) The 3rd byte represents the Link Number (1-84) The 4th byte is reserved for future use ')
dsx1EsfCurrResrcId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrResrcId.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrResrcId.setDescription('Uniquely identifies a link in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
dsx1EsfCurrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrESs.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrESs.setDescription('This is the number of errored seconds that have occurred on the link during the current interval. This is not incremented during an Unavailable Second. For ESF links an Errored Second is a second with the occurrence of a Loss of Frame or a CRC6 error in a one-second period.')
dsx1EsfCurrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrUASs.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrUASs.setDescription('This is the number of failed seconds (UAS) that have occurred on the link during the current interval. Unavailable Seconds (UAS) are calculated by counting the number of seconds that the interface is unavailable. Each second period during the occurrence of a Failed Signal State (ten consecutive SES) is known as a failed/unavailable second.')
dsx1EsfCurrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrSESs.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrSESs.setDescription('This is the number of severely errored seconds that have occurred on the link during the current interval. Controlled slips are not included in this parameter. This is not incremented during an Unavailable Second. A Severely Errored Second for ESF signals is a second period with 320 or more CRC6 errors.')
dsx1EsfCurrBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrBESs.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrBESs.setDescription('This is the number of bursty errored seconds that have occurred on the T1 link during the current interval. This is not incremented during an Unavailable Second and applies to ESF signals only. A Bursty Errored Second is a second period with more than one but less than 320 CRC6 errors.')
dsx1EsfCurrLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrLOFs.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrLOFs.setDescription('This is the number of loss of frames that have occurred on the link during the current interval. A loss of frame occurs when either network equipment or the DTE senses errors in the framing pattern. Depending upon the equipment, this occurs when any 2 of 4, 2 of 5, or 3 of 5 consecutive terminal framing bits received contain bit errors in the framing pattern.')
dsx1EsfCurrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrSeconds.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrSeconds.setDescription('The total number of seconds in the current interval.')
dsx1EsfCurrIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrIntervals.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrIntervals.setDescription('The total number of valid 15 minute intervals counted since the link has been up and running.')
dsx1EsfCurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1EsfCurrStatus.setStatus('current')
if mibBuilder.loadTexts: dsx1EsfCurrStatus.setDescription("This defines the status of the DS1/E1 link using an 8 character code which can contain numbers or letters. The codes are interpreted as follows: character #1 - 'F' or zero where 'F' indicates Failed Signal Status (FSS) if 'U' or 'L' are present. character #2 - 'U' or zero where 'U' indicates an unavailable signal state. character #3 through #6 are always zero. character #7 - 'L' or zero where 'L' indicates that the T1 line is in loop. character #8 - always zero.")
dsx1Esf24HrTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2), )
if mibBuilder.loadTexts: dsx1Esf24HrTable.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrTable.setDescription('This is the DS1/E1 24 Hour ESF Statistics table which consists of an entry for each DS1/E1 link in the system that is configured for T1 ESF lines. This table provides the total counters accumulated for last 24 hour period.')
dsx1Esf24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1), ).setIndexNames((0, "ERI-DNX-PERF-MONT-MIB", "dsx1Esf24HrLinkAddr"))
if mibBuilder.loadTexts: dsx1Esf24HrEntry.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrEntry.setDescription('The conceptual row of the DS1/E1 24 Hour ESF Statistics table. A row in this table cannot be added, deleted, or modified directly. Rows may be removed or added by configuring the DS1 line type via the appropriate Device Provisioning table.')
dsx1Esf24HrLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf24HrLinkAddr.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrLinkAddr.setDescription('This number uniquely identifies an DS1/E1 link resource. This number will be used throughout the system to identify a unique link. The format is represented using an IP address syntax (4 byte string). Note that the maximum valid link number will vary depending on the specified carrier and framing options. For example, an octal T1/E1 device has 8 DS1 links but the DS3 has 28 DS1 links. The 1st byte is reserved for future Nest Number use The 2nd byte represents the Slot Number (1-11) The 3rd byte represents the Link Number (1-84) The 4th byte is reserved for future use ')
dsx1Esf24HrResrcId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf24HrResrcId.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrResrcId.setDescription('Uniquely identifies a link in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
dsx1Esf24HrESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf24HrESs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrESs.setDescription('This is the number of errored seconds that have occurred on the link during the past 24 hours.')
dsx1Esf24HrUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf24HrUASs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrUASs.setDescription('This is the number of Unavailable Seconds (UAS) that have occurred on the T1 link during the past 24 hours.')
dsx1Esf24HrSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf24HrSESs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrSESs.setDescription('This is the number of severely errored seconds that have occurred on the T1 link during the past 24 hours.')
dsx1Esf24HrBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf24HrBESs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrBESs.setDescription('This is the number of bursty errored seconds that have occurred on the T1 link during the past 24 hours.')
dsx1Esf24HrLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 2, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf24HrLOFs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf24HrLOFs.setDescription('This is the number of loss of frames that have occurred on the T1 link during the past 24 hours.')
dsx1Esf96RegTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3), )
if mibBuilder.loadTexts: dsx1Esf96RegTable.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegTable.setDescription('This table is the ESF 96 Registers Table. It displays the 96 15 minute performance registers for each link on a card')
dsx1Esf96RegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1), ).setIndexNames((0, "ERI-DNX-PERF-MONT-MIB", "dsx1Esf96RegLinkAddr"), (0, "ERI-DNX-PERF-MONT-MIB", "dsx1Esf96RegInterval"))
if mibBuilder.loadTexts: dsx1Esf96RegEntry.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegEntry.setDescription('The conceptual row of the DS1/E1 ESF 96 Registers table. A row in this table cannot be added, deleted, or modified directly. Rows may be removed or added by configuring the DS1 line type via the appropriate Device Provisioning table.')
dsx1Esf96RegLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf96RegLinkAddr.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegLinkAddr.setDescription('Uniquely identifies a link in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
dsx1Esf96RegInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf96RegInterval.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegInterval.setDescription('Specifies the interval Number On a particular link')
dsx1Esf96RegESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf96RegESs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegESs.setDescription('The number of Errored Seconds for a particular interval on a particular link')
dsx1Esf96RegUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf96RegUASs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegUASs.setDescription('The number of Unavailable Seconds for a particular interval on a particular link')
dsx1Esf96RegSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf96RegSESs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegSESs.setDescription('The number of Severely Errored Seconds for a particular interval on a particular link')
dsx1Esf96RegBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 1, 3, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1Esf96RegBESs.setStatus('current')
if mibBuilder.loadTexts: dsx1Esf96RegBESs.setDescription('The number of Bursty Errored Seconds for a particular interval on a particular link')
dsx1G826Table = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1), )
if mibBuilder.loadTexts: dsx1G826Table.setStatus('current')
if mibBuilder.loadTexts: dsx1G826Table.setDescription('This is the DS1/E1 G.826 Statistics table which consists of an entry for each DS1/E1 link in the system. This table provides the total counters accumulated since the link has been up or since the last time the counts were cleared. The counters are calculated in accordance with the ITU-T G.826 Error performance parameters, November 1993.')
dsx1G826Entry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1), ).setIndexNames((0, "ERI-DNX-PERF-MONT-MIB", "dsx1G826LinkAddr"))
if mibBuilder.loadTexts: dsx1G826Entry.setStatus('current')
if mibBuilder.loadTexts: dsx1G826Entry.setDescription('The conceptual row of the DS1/E1 G.826 Statistics table. A row in this table cannot be added or deleted directly but the counter time period can be reset to zero. Rows may be removed or added by configuring the DS1/E1 line type via the appropriate Device Provisioning tables.')
dsx1G826LinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826LinkAddr.setStatus('current')
if mibBuilder.loadTexts: dsx1G826LinkAddr.setDescription('This number uniquely identifies an DS1/E1 link resource. This number will be used throughout the system to identify a unique link. The format is represented using an IP address syntax (4 byte string). Note that the maximum valid link number will vary depending on the specified carrier and framing options. For example, an octal T1/E1 device has 8 DS1 links but the DS3 has 28 DS1 links. The 1st byte is reserved for future Nest Number use The 2nd byte represents the Slot Number (1-11) The 3rd byte represents the Link Number (1-84) The 4th byte is reserved for future use ')
dsx1G826ResrcId = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826ResrcId.setStatus('current')
if mibBuilder.loadTexts: dsx1G826ResrcId.setDescription('Uniquely identifies a link in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
dsx1G826TotalTime = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1G826TotalTime.setStatus('current')
if mibBuilder.loadTexts: dsx1G826TotalTime.setDescription('This the total number of seconds the G.826 data has been collected. Resetting this to zero will clear the counters for specific link.')
dsx1G826ESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826ESs.setStatus('current')
if mibBuilder.loadTexts: dsx1G826ESs.setDescription('This is the total number of errored seconds that have occurred since the link has been up or since the G.826 counters have been reset. An Errored Second for G.826 is a one second period with one or more errored blocks or at least one defect.')
dsx1G826ErrFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826ErrFSs.setStatus('current')
if mibBuilder.loadTexts: dsx1G826ErrFSs.setDescription('This is the total number of error free seconds since the link has been up or since the G.826 counters have been reset.')
dsx1G826SESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826SESs.setStatus('current')
if mibBuilder.loadTexts: dsx1G826SESs.setDescription('This is the total number of severely errored seconds that have occurred since the link has been up or since the G.826 counters have been reset. A Severely Errored Second for G.826 is a one second period that contains 30% or more errored blocks OR at least one defect. This is a subset of ES.')
dsx1G826ConsecSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826ConsecSESs.setStatus('current')
if mibBuilder.loadTexts: dsx1G826ConsecSESs.setDescription('This is the total number of continuous occurrences of SES, in a one second intervals, since the link has been up or since the G.826 counters have been reset.')
dsx1G826ConsecErrFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826ConsecErrFSs.setStatus('current')
if mibBuilder.loadTexts: dsx1G826ConsecErrFSs.setDescription('This is the total number of consecutive seconds one second period intervals that did not have defects or errors since the link has been up or since the G.826 counters have been reset.')
dsx1G826BGErrBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826BGErrBlocks.setStatus('current')
if mibBuilder.loadTexts: dsx1G826BGErrBlocks.setDescription('This is the total number of background errored blocks that have occurred since the link has been up or since the G.826 counters have been reset. A Background Block Error for G.826 is an errored block not occurring as part of an SES.')
dsx1G826ESRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826ESRatio.setStatus('current')
if mibBuilder.loadTexts: dsx1G826ESRatio.setDescription('This is the ratio of ES to total seconds in available time during a fixed measurement interval rounded to 2 decimals.')
dsx1G826SESRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826SESRatio.setStatus('current')
if mibBuilder.loadTexts: dsx1G826SESRatio.setDescription('This is the ratio of SES to total seconds in available time during a fixed measurement interval rounded to 2 decimals.')
dsx1G826BgBERRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826BgBERRatio.setStatus('current')
if mibBuilder.loadTexts: dsx1G826BgBERRatio.setDescription('This is the ratio of background block errors to total blocks in available time during a fixed measurement interval rounded to 2 decimals. This total block count excludes all blocks during SES.')
dsx1G826UASs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 4, 2, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1G826UASs.setStatus('current')
if mibBuilder.loadTexts: dsx1G826UASs.setDescription('This is the total number of Unavailable Seconds (UAS) that have occurred since the link has been up or since the G.826 counters have been reset.')
mibBuilder.exportSymbols("ERI-DNX-PERF-MONT-MIB", dsx1EsfCurrUASs=dsx1EsfCurrUASs, dsx1Esf24HrLOFs=dsx1Esf24HrLOFs, dsx1Esf24HrESs=dsx1Esf24HrESs, dsx1G826Entry=dsx1G826Entry, dsx1EsfCurrIntervals=dsx1EsfCurrIntervals, dsx1G826ErrFSs=dsx1G826ErrFSs, dsx1G826BGErrBlocks=dsx1G826BGErrBlocks, dsx1G826=dsx1G826, dsx1G826UASs=dsx1G826UASs, performanceMonitoring=performanceMonitoring, dsx1G826ConsecSESs=dsx1G826ConsecSESs, dsx1G826TotalTime=dsx1G826TotalTime, dsx1Esf96RegEntry=dsx1Esf96RegEntry, dsx1G826LinkAddr=dsx1G826LinkAddr, dsx1G826SESs=dsx1G826SESs, dsx1EsfCurrSeconds=dsx1EsfCurrSeconds, dsx1Esf24HrEntry=dsx1Esf24HrEntry, dsx1EsfCurrESs=dsx1EsfCurrESs, dsx1Esf24HrTable=dsx1Esf24HrTable, dsx1EsfCurrLOFs=dsx1EsfCurrLOFs, dsx1EsfCurrSESs=dsx1EsfCurrSESs, dsx1Esf24HrLinkAddr=dsx1Esf24HrLinkAddr, dsx1EsfCurrBESs=dsx1EsfCurrBESs, dsx1Esf24HrUASs=dsx1Esf24HrUASs, dsx1Esf96RegLinkAddr=dsx1Esf96RegLinkAddr, dsx1Esf96RegESs=dsx1Esf96RegESs, dsx1Esf96RegInterval=dsx1Esf96RegInterval, eriDNXLinkPMStatsMIB=eriDNXLinkPMStatsMIB, dsx1G826ESs=dsx1G826ESs, dsx1EsfCurrTable=dsx1EsfCurrTable, dsx1G826ResrcId=dsx1G826ResrcId, dsx1G826ConsecErrFSs=dsx1G826ConsecErrFSs, dsx1G826SESRatio=dsx1G826SESRatio, dsx1EsfCurrEntry=dsx1EsfCurrEntry, dsx1G826ESRatio=dsx1G826ESRatio, PYSNMP_MODULE_ID=eriDNXLinkPMStatsMIB, dsx1Esf96RegUASs=dsx1Esf96RegUASs, dsx1Esf96RegSESs=dsx1Esf96RegSESs, dsx1EsfCurrResrcId=dsx1EsfCurrResrcId, dsx1Esf24HrBESs=dsx1Esf24HrBESs, dsx1G826BgBERRatio=dsx1G826BgBERRatio, dsx1Esf96RegBESs=dsx1Esf96RegBESs, dsx1Esf24HrResrcId=dsx1Esf24HrResrcId, dsx1EsfCurrStatus=dsx1EsfCurrStatus, dsx1EsfCurrLinkAddr=dsx1EsfCurrLinkAddr, dsx1Esf=dsx1Esf, dsx1Esf96RegTable=dsx1Esf96RegTable, dsx1G826Table=dsx1G826Table, dsx1Esf24HrSESs=dsx1Esf24HrSESs)
