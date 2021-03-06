#
# PySNMP MIB module JUNIPER-JS-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-POLICY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
jnxJsPolicies, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsPolicies")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Gauge32, Integer32, Bits, MibIdentifier, TimeTicks, NotificationType, ModuleIdentity, Counter32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Gauge32", "Integer32", "Bits", "MibIdentifier", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
jnxJsSecPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1))
jnxJsSecPolicyMIB.setRevisions(('2006-12-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxJsSecPolicyMIB.setRevisionsDescriptions(('Creation Date',))
if mibBuilder.loadTexts: jnxJsSecPolicyMIB.setLastUpdated('200705071840Z')
if mibBuilder.loadTexts: jnxJsSecPolicyMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxJsSecPolicyMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxJsSecPolicyMIB.setDescription('This module defines the mib for policy monitoring. A security policy, which can be configured from the user interface controls the traffic flow from one zone to another zone by defining the kind(s) of traffic permitted from specified IP sources to specified IP destinations at scheduled times. Juniper security device enforce the security policies rules for the transit traffic in terms of which traffic can pass through the firewall, and the actions taken on the traffic as it passes through the firewall. ')
jnxJsPolicyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 0))
jnxJsPolicyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1))
jnxJsPolicyTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 2))
jnxJsPolicyNumber = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyNumber.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyNumber.setDescription('The number of policies (regardless of their current state) present on this system.')
jnxJsPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2), )
if mibBuilder.loadTexts: jnxJsPolicyTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyTable.setDescription('The table exposes the security policy entries. Security devices/routers provide a network boundary with a single point of entry and exit point, which allows the screening and directing of traffic through the implementation of access policies. The access policies can permit, deny, encrypt, authenticate, prioirtize, schedule and monitor the traffic flow through the firewall. This table lists entries of policy. The number of policies are given by jnxJsPolicyNumber.')
jnxJsPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1), ).setIndexNames((0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyFromZone"), (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyToZone"), (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyName"))
if mibBuilder.loadTexts: jnxJsPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyEntry.setDescription('An entry contains a security policy. The security policies are configured under from-zone, to-zone direction. Under a specific zone direction, each security policy contains name, match-criteria, action, and other options.')
jnxJsPolicyFromZone = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)))
if mibBuilder.loadTexts: jnxJsPolicyFromZone.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyFromZone.setDescription('The attribute displays the from zone name.')
jnxJsPolicyToZone = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)))
if mibBuilder.loadTexts: jnxJsPolicyToZone.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyToZone.setDescription('The attribute exposes the to-zone name.')
jnxJsPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)))
if mibBuilder.loadTexts: jnxJsPolicyName.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyName.setDescription('The name of the policy defined. It consists of up to 256 ascii characters and uniquely identifies the policy entry.')
jnxJsPolicySequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicySequenceNumber.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicySequenceNumber.setDescription('The attribute indicates the policy sequence order of the policy within a specific from-zone and to-zone pair. Policies are matched in a sequence where the ordering is specified by this number.')
jnxJsPolicyAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2), ("reject", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyAction.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyAction.setDescription('The attribute indicates the actions performed when the criteria is matched. The action permit, deny and reject are used configured policies.')
jnxJsPolicyScheduler = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyScheduler.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyScheduler.setDescription('The name of the schedule attached to this policy. Certain schedule has a specified duration and this may effect the status of the policy.')
jnxJsPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("unavailable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyState.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyState.setDescription('The state of this policy: active, inactive, or unavailable. The state can be effected by the scheduler if the scheduler has a specified duration.')
jnxJsPolicyStatsAvailability = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsAvailability.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsAvailability.setDescription('The statistics availability of this policy. The attribute indicates whether the statistics counters are available and are actively updated. If available, there would exists a matching jnxJsPolicyStatsEntry for the policy.')
jnxJsPolicyPerSecBytesThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyPerSecBytesThreshold.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyPerSecBytesThreshold.setDescription('The attribute indicates the threshold value of bytes per second.')
jnxJsPolicyPerMinKbytesThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyPerMinKbytesThreshold.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyPerMinKbytesThreshold.setDescription('The attribute indicates the threshold value of kbyte per min.')
jnxJsPolicyStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3), )
if mibBuilder.loadTexts: jnxJsPolicyStatsTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsTable.setDescription('The table exposes the security policy statistics entries. These statistics can be enabled and disabled by configuration on a per policy basis.')
jnxJsPolicyStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1), ).setIndexNames((0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyFromZone"), (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyToZone"), (0, "JUNIPER-JS-POLICY-MIB", "jnxJsPolicyName"))
if mibBuilder.loadTexts: jnxJsPolicyStatsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsEntry.setDescription('An entry contains a security policy. The security policies are configured under from-zone, to-zone direction. Under a specific zone direction, each security policy contains name, match-criteria, action, and other options.')
jnxJsPolicyStatsCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsCreationTime.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsCreationTime.setDescription('The creation timestamp of the policy statistics entry. The timestamp is modified during the creation and deletion of the policy statistics entry. When the timestamp changes, the policy entry statistics is assumed to be a new statistics entry and not associated with previous statistic entry of the same indices.')
jnxJsPolicyStatsInputBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsInputBytes.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsInputBytes.setDescription('The number of input bytes enters the FW through this policy.')
jnxJsPolicyStatsInputByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsInputByteRate.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsInputByteRate.setDescription('The number of input bytes per second or the rate that enters the FW through this policy.')
jnxJsPolicyStatsOutputBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputBytes.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputBytes.setDescription('The number of output bytes associated with this policy.')
jnxJsPolicyStatsOutputByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputByteRate.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputByteRate.setDescription('The number of output bytes per second or the rate associated with this policy.')
jnxJsPolicyStatsInputPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsInputPackets.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsInputPackets.setDescription('The number of input packets enters the FW through this policy.')
jnxJsPolicyStatsInputPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsInputPacketRate.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsInputPacketRate.setDescription('The number of input packets per second or the input packet rate of the FW through this policy.')
jnxJsPolicyStatsOutputPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputPackets.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputPackets.setDescription('The number of output packets associated with this policy.')
jnxJsPolicyStatsOutputPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputPacketRate.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsOutputPacketRate.setDescription('The number of output packets per second or the rate associated with this policy.')
jnxJsPolicyStatsNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsNumSessions.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsNumSessions.setDescription('The number of sessions associated with this policy.')
jnxJsPolicyStatsSessionRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsSessionRate.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsSessionRate.setDescription('The rate of the sessions associated with this policy.')
jnxJsPolicyStatsSessionDeleted = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsSessionDeleted.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsSessionDeleted.setDescription('The number of sessions associated with this policy.')
jnxJsPolicyStatsLookups = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsLookups.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsLookups.setDescription('The number of policy lookups performed.')
jnxJsPolicyStatsCountAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsPolicyStatsCountAlarm.setStatus('current')
if mibBuilder.loadTexts: jnxJsPolicyStatsCountAlarm.setDescription('The number of alarm counted when the traffic exceeds certain threshold configuration.')
mibBuilder.exportSymbols("JUNIPER-JS-POLICY-MIB", jnxJsPolicyNotifications=jnxJsPolicyNotifications, jnxJsPolicyAction=jnxJsPolicyAction, jnxJsPolicyStatsAvailability=jnxJsPolicyStatsAvailability, jnxJsPolicyStatsOutputPacketRate=jnxJsPolicyStatsOutputPacketRate, jnxJsPolicyObjects=jnxJsPolicyObjects, jnxJsPolicyStatsNumSessions=jnxJsPolicyStatsNumSessions, jnxJsPolicyStatsLookups=jnxJsPolicyStatsLookups, jnxJsPolicyName=jnxJsPolicyName, jnxJsPolicyStatsTable=jnxJsPolicyStatsTable, jnxJsPolicyStatsInputBytes=jnxJsPolicyStatsInputBytes, jnxJsPolicyTrapVars=jnxJsPolicyTrapVars, jnxJsPolicyStatsInputByteRate=jnxJsPolicyStatsInputByteRate, jnxJsPolicyStatsOutputPackets=jnxJsPolicyStatsOutputPackets, jnxJsPolicyStatsInputPacketRate=jnxJsPolicyStatsInputPacketRate, jnxJsPolicyStatsOutputByteRate=jnxJsPolicyStatsOutputByteRate, jnxJsPolicyStatsCountAlarm=jnxJsPolicyStatsCountAlarm, jnxJsPolicyPerSecBytesThreshold=jnxJsPolicyPerSecBytesThreshold, jnxJsPolicyTable=jnxJsPolicyTable, jnxJsPolicyEntry=jnxJsPolicyEntry, jnxJsPolicyNumber=jnxJsPolicyNumber, jnxJsPolicySequenceNumber=jnxJsPolicySequenceNumber, jnxJsPolicyPerMinKbytesThreshold=jnxJsPolicyPerMinKbytesThreshold, jnxJsPolicyState=jnxJsPolicyState, jnxJsPolicyFromZone=jnxJsPolicyFromZone, jnxJsPolicyToZone=jnxJsPolicyToZone, jnxJsPolicyStatsOutputBytes=jnxJsPolicyStatsOutputBytes, jnxJsPolicyScheduler=jnxJsPolicyScheduler, PYSNMP_MODULE_ID=jnxJsSecPolicyMIB, jnxJsPolicyStatsEntry=jnxJsPolicyStatsEntry, jnxJsPolicyStatsCreationTime=jnxJsPolicyStatsCreationTime, jnxJsPolicyStatsSessionRate=jnxJsPolicyStatsSessionRate, jnxJsPolicyStatsSessionDeleted=jnxJsPolicyStatsSessionDeleted, jnxJsPolicyStatsInputPackets=jnxJsPolicyStatsInputPackets, jnxJsSecPolicyMIB=jnxJsSecPolicyMIB)
