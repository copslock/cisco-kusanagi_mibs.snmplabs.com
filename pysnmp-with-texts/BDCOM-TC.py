#
# PySNMP MIB module BDCOM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BDCOM-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:36:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
bdcomModules, = mibBuilder.importSymbols("BDCOM-SMI", "bdcomModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, IpAddress, Integer32, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Unsigned32, ModuleIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "IpAddress", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Unsigned32", "ModuleIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bdcomTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320, 12, 1))
bdcomTextualConventions.setRevisions(('2003-10-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bdcomTextualConventions.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: bdcomTextualConventions.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: bdcomTextualConventions.setOrganization('BDCOM, Inc.')
if mibBuilder.loadTexts: bdcomTextualConventions.setContactInfo(' Tel: +86-21-50800666 Postal: No.123,Juli RD,Zhangjiang Hitech Park, Shanghai Baud Data Communication Corporation Inc, Shanghai City 201203, P.R.C ')
if mibBuilder.loadTexts: bdcomTextualConventions.setDescription('This module defines textual conventions used throughout bdcom enterprise mibs.')
class BDCOMNetworkProtocol(TextualConvention, Integer32):
    description = 'Represents the different types of network layer protocols.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 65535))
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("ipv6", 20), ("cdm", 21), ("nbf", 22), ("bpxIgx", 23), ("clnsPfx", 24), ("http", 25), ("unknown", 65535))

class BDCOMNetworkAddress(TextualConvention, OctetString):
    description = 'Represents a network layer address. The length and format of the address is protocol dependent as follows: ip 4 octets decnet 2 octets pup obsolete chaos 2 octets xns 10 octets first 4 octets are the net number last 6 octets are the host number x121 appletalk 3 octets first 2 octets are the net number last octet is the host number clns lat vines 6 octets first 4 octets are the net number last 2 octets are the host number cons apollo 10 octets first 4 octets are the net number last 6 octets are the host number stun 8 octets novell 10 octets first 4 octets are the net number last 6 octets are the host number qllc 6 octets bstun 1 octet - bi-sync serial tunnel snapshot 1 octet atmIlmi 4 octets x25 pvc 2 octets (12 bits) ipv6 16 octets cdm nbf bgpIgx clnsPfx upto 20 octets http upto 70 octets first 4 octets are the IPv4 host address next 2 octets are the TCP port number remaining(1 upto 64) octets are the URI '
    status = 'current'
    displayHint = '1x:'

class Unsigned64(TextualConvention, Counter64):
    description = 'An unsigned 64 bit integer. We use SYNTAX Counter64 for the encoding rules.'
    status = 'current'

class InterfaceIndexOrZero(TextualConvention, Integer32):
    description = 'Either the value 0, or the ifIndex value of an interface in the ifTable.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class SAPType(TextualConvention, Integer32):
    description = 'Service Access Point - is a term that denotes the means by which a user entity in layer n+1 accesses a service of a provider entity in layer n.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 254)

class CountryCode(TextualConvention, OctetString):
    description = 'Represents a case-insensitive 2-letter country code taken from ISO-3166. Unrecognized countries are represented as empty string.'
    status = 'current'
    displayHint = '2a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class CountryCodeITU(TextualConvention, Unsigned32):
    reference = 'ITU-T T.35 - Section 3.1 Country Code'
    description = 'This textual convention represents a country or area code for non-standard facilities in telematic services.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of entPhysicalIndex. If non-zero, the object is an entPhysicalIndex. If zero, no appropriate entPhysicalIndex exists. Any additional semantics are object specific.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BDCOMRowOperStatus(TextualConvention, Integer32):
    description = "Represents the operational status of an table entry. This textual convention allows explicitly representing the states of rows dependent on rows in other tables. active(1) - Indicates this entry's RowStatus is active and the RowStatus for each dependency is active. activeDependencies(2) - Indicates that the RowStatus for each dependency is active, but the entry's RowStatus is not active. inactiveDependency(3) - Indicates that the RowStatus for at least one dependency is not active. missingDependency(4) - Indicates that at least one dependency does not exist in it's table. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4))

class BDCOMPort(TextualConvention, Integer32):
    reference = 'Transmission Control Protocol. J. Postel. RFC793, User Datagram Protocol. J. Postel. RFC768'
    description = 'The TCP or UDP port number range.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class BDCOMIpProtocol(TextualConvention, Integer32):
    reference = 'Internet Protocol. J. Postel. RFC791'
    description = 'IP protocol number range.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class BDCOMLocationClass(TextualConvention, Integer32):
    description = 'An enumerated value which provides an indication of the general location type of a particular physical and/or logical interface. chassis - a system framework for mounting one or more shelves/slots/cards. shelf - a cabinet that holds one or more slots. slot - card or subSlot holder. subSlot - daughter-card holder. port - a physical port (e.g., a DS1 or DS3 physical port). subPort - a logical port on a physical port (e.g., a DS1 subPort on a DS3 physical port). channel - a logical interface (e.g., a DS0 channel, signalling channel, ATM port, other virtual interfaces). subChannel - a sub-channel on a logical interface. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("chassis", 1), ("shelf", 2), ("slot", 3), ("subSlot", 4), ("port", 5), ("subPort", 6), ("channel", 7), ("subChannel", 8))

class BDCOMLocationSpecifier(TextualConvention, OctetString):
    reference = 'RFC2234, Augmented BNF for syntax specifications: ABNF'
    description = "Use this TC to define objects that indicate the physical entity and/or logical interface location of a managed entity on a managed device. In SNMP, a standard mechanism for indicating the physical location of entities is via the ENTITY-MIB. However, that approach is not satisfactory in some cases because: 1. The entity requiring a location-based naming may be associated with an entity which can not be represented as a physical entity in the ENTITY-MIB, 2. NMS applications may desire a more direct name/representation of a physical entity than is available via the ENTITY-MIB, e.g., a physical entity which is named via a hierarchy of levels in the ENTITY-MIB. The value of an object defined using this TC is an ASCII string consisting of zero or more elements separated by commas. Each element is of the form <tag> = <value>. An example of this syntax is 'slot=5,port=3'. The syntax of the string is formally specified using ABNF notation (with one exception, noted below), as follows: location-specifier = elem *(',' elem) ; subject to ; size restriction specified in the SYNTAX ; clause below elem = loctype '=' number number = %x00-FFFFFFFF / %d0-4294967295 loctype = 1*32VCHAR It is recommended that loctype use one of the enumerated labels defined for BDCOMLocationClass. (NOTE: To conform to ABNF notation as defined in RFC2234, substitute the single-quote symbol with a double-quote symbol in the above rules.) A zero length of BDCOMLocationSpecifier is object-specific and must be defined as part of the description of any object which uses this syntax. "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class BDCOMInetAddressMask(TextualConvention, Unsigned32):
    reference = 'RFC2851, Textual Conventions for Internet Network Addresses.'
    description = "Denotes a generic Internet subnet address mask. The Internet subnet address mask is represented as the number of contiguous 1-bit from MSB (most significant bit) of the Internet subnet address mask. A BDCOMInetAddressMask value is always interpreted within the context of an InetAddressType value. The InetAddressType only object or InetAddressType with InetAddress objects which define the context must be registered immediately before the object which uses the BDCOMInetAddressMask textual convention. In other words, the object identifiers for the InetAddressType object and the BDCOMInetAddressMask object MUST have the same length and the last sub-identifier of the InetAddressType object MUST be 1 less than the last sub-identifier of the BDCOMInetAddressMask object and MUST be 2 less than the last sub-identifier of the BDCOMInetAddressMask object if an InetAddress object is defined between InetAddressType and BDCOMInetAddressMask objects. The maximum value of the BDCOMInetAddressMask TC is 32 for the value 'ipv4(1)' in InetAddressType object and 128 for the value 'ipv6(2)' in InetAddressType object. The value zero is object-specific and must therefore be defined as part of the description of any object which uses this syntax. Examples of the usage of zero might include situations where Internet subnet mask was unknown, or when none subnet masks need to be referenced."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 128)

class BDCOMAbsZeroBasedCounter32(TextualConvention, Gauge32):
    description = 'This TC describes an object which counts events with the following semantics: objects of this type will be set to zero(0) on creation and will thereafter count appropriate events, it locks at the maximum value of 4,294,967,295 if the counter overflows. This TC may be used only in situations where wrapping is not possible or extremely unlikely situation.'
    status = 'current'

class BDCOMSnapShotAbsCounter32(TextualConvention, Unsigned32):
    description = 'This TC describes an object which stores a snap-shot value with the following semantics: objects of this type will take a snap-shot value from their associated BDCOMAbsZeroBasedCounter32 type objects on creation.'
    status = 'current'

class BDCOMAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    description = 'Represents the perceived alarm severity associated with a service or safety affecting condition and/or event. These are based on ITU severities, except that info(7) is added. cleared(1) - Indicates a previous alarm condition has been cleared. It is not required (unless specifically stated elsewhere on a case by case basis) that an alarm condition that has been cleared will produce a notification or other event containing an alarm severity with this value. indeterminate(2) - Indicates that the severity level cannot be determined. critical(3) - Indicates that a service or safety affecting condition has occurred and an immediate corrective action is required. major(4) - Indicates that a service affecting condition has occurred and an urgent corrective action is required. minor(5) - Indicates the existence of a non-service affecting condition and that corrective action should be taken in order to prevent a more serious (for example, service or safety affecting) condition. warning(6) - Indicates the detection of a potential or impending service or safety affecting condition, before any significant effects have been felt. info(7) - Indicates an alarm condition that does not meet any other severity definition. This can include important, but non-urgent, notices or informational events. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7))

class PerfHighIntervalCount(TextualConvention, Counter64):
    reference = 'RFC 2856(HCNUM-TC MIB). RFC 2493(PerfHist-TC-MIB).'
    description = "A 64 bit counter associated with a performance measurement in a previous 15 minute measurement interval. In the case where the agent has no valid data available for a particular interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchName error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation). In a system supporting a history of n intervals with IntervalCount(1) and IntervalCount(n) the most and least recent intervals respectively, the following applies at the end of a 15 minute interval: - discard the value of IntervalCount(n) - the value of IntervalCount(i) becomes that of IntervalCount(i-1) for n >= i > 1 - the value of IntervalCount(1) becomes that of CurrentCount - the TotalCount, if supported, is adjusted. This definition is based on CounterBasedGauge64 TEXTUAL CONVENTION defined in RFC2856. The PerfHighIntervalCount type represents a non-negative integer, which may increase or decrease, but shall never exceed a maximum value, nor fall below a minimum value. The maximum value can not be greater than 2^64-1 (18446744073709551615 decimal), and the minimum value can not be smaller than 0. The value of a PerfHighIntervalCount, has its maximum value whenever the information being modeled is greater than or equal to its maximum value, and has its minimum value whenever the information being modeled is smaller than or equal to its minimum value. If the information being modeled subsequently decreases below (increases above) the maximum (minimum) value, the PerfHighIntervalCount also decreases (increases). Note that this TC is not strictly supported in SMIv2, because the 'always increasing' and 'counter wrap' semantics associated with the Counter64 base type are not preserved. It is possible that management applications which rely solely upon the (Counter64) ASN.1 tag to determine object semantics will mistakenly operate upon objects of this type as they would for Counter64 objects. This textual convention represents a limited and short-term solution, and may be deprecated as a long term solution is defined and deployed to replace it."
    status = 'current'

class ConfigIterator(TextualConvention, Unsigned32):
    description = "This object type is a control object type which applies to writable objects in the same SNMP PDU related to the same table containing those objects. It controls an operation which repeatedly applies the specified configuration data to more than one rows in a table. The operation starts from the row specified by the index of the instance and repeats for the number of rows as the value of the object. ConfigIterator object needs to be accompanied by one set of writable objects which are of the same instance to apply to. For example, a SNMP PDU contains { objectA.10 = 1, objectB.10 = 'E1', objectC.10 = 44, objectRepetition.10 = 100 } The SYNTAX of objectRepetition is ConfigIterator. This will apply value 1 to objectA, value 'E1' to objectB, value 44 to objectC in the table starting from row 10 repeatedly for 100 rows. The iteration is based on the number of rows, not based on the value of the index. For sparse tables, the index 10, 20, 30, 110, and 120 counts for 5 rows, the operation will go beyond index 100 in the previous SNMP PDU example. The iteration will stop prematurely when it comes to the following situations: (1) When the number of the rows in the table is less than the designated row indicated by the ConfigIterator object. (2) When it encounters the first error in any row, the operation won't continue to next row. The operation of ConfigIterator object applies only to the writable objects having the same index as the ConfigIterator object in one SNMP PDU. For example, a SNMP PDU contains { objectD.5 = 38, objectE.6 = 'T1', objectF.5 = 'false', objectIterator.5 = 10 } The SYNTAX of objectIterator is ConfigIterator. This will apply value 38 to objectD, value 'false' to objectF in the table starting from row 5 repeatedly for 10 rows. Since the object objectE.6 has different index (6) from the index of objectIterator, the repetition won't be applied to it. However the value of objectE in the row 6 will be set to 'T1' according to regular SNMP SET orperation. If there is row overlapping of the iteration in a SNMP PDU, it will be operated as they are in two different SNMP PDUs. For example, a SNMP PDU contains { objectD.5 = 38, objectD.6 = 40, objectE.6 = 'T1', objectF.5 = 'false', objectIterator.5 = 10 objectIterator.6 = 10 } This will apply value 38 to objectD, value 'false' to objectF starting from row 5 repeatedly for 10 rows, and apply value 40 to objectD, value 'T1' to objectE starting from row 6 repeatedly for 10 rows. The final value of objectD.6 can be 38 or 40, it depends on the SNMP stack of the system starts SNMP SET for the row 5 before the row 6 or the other way around. The object defined as ConfigIterator will be set to value 1 after the iteration operation is kick-off regardless the system has completed the operation to the designated rows or not. Therefore retrieving the value of this object is meaningless. It acts as the one time operation for bulk configuration. The object defined as ConfigIterator has no meaning by itself, it has to be combined with one or more than one writable objects from the same table and within the same SNMP PDU for the repetition operation. For example, a SNMP PDU contains { objectG.2 = 49, objectH.2 = 'AE'h objectIterator.4 = 20 } The SYNTAX of objectIterator is ConfigIterator. Since there are no objects having the same index as the index of objectIterator in the PDU, the result of this SNMP operation will set value 49 to objectG and value 0xAE to objectH of the row 2 only as regular SNMP SET operation. The index of the instance indicates the starting row for the iteration. The order of the iteration depends, for instance, on: (1) physical hardware position, or (2) logical index. It depends on the characters of the table which contains the ConfigIterator object. Iteration can be done through some or all the components of the index for a table. The description of the iterator object in that table should describe which part of the index the iteration is applied to. The operation for this object type is based on the best effort. When the agent receives a SNMP PDU containing this data type, the return status of the SNMP request reflects only the result of the SET operation has applied to the starting row. It may return a SNMP response with SUCCESS status regardless the number of rows for the data actually been deployed later on. Therefore it is possible the data might not be completely deployed to the number of rows designated by the ConfigIterator and the operation stops prematurely due to an error it first encounters after n rows (n < the value of ConfigIterator object). Usually the error report mechanism for this type of operation is accomplished by combining this type of object with the other two objects in the same table: (1) An OwnerString object (2) An object indicates the result of the operation. When issuing this bulk configuration request, the SNMP manager should provide its identifier in (1) object. After issuing the request, it should check the value of (1) object if it is the same with it own name. If they are the same, then the value of the object presents in (2) is the result from the previous operation from this manager. Otherwise, another SNMP manager might issue the bulk configuration to the same table before the previous bulk operation has been completed. These two objects will represent the last bulk operation in the table. "
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BulkConfigResult(TextualConvention, OctetString):
    description = "This textual convention defines the format of the displayable textual result from the bulk configuration operation specified as ConfigIterator type. The format should be: 'COMPLETION=<number of rows had completed before any error occured>/<number of rows was designated>, ERROR=<error code>/<index where the error occured>: <error text>' For example: 'COMPLETION=22/100,ERROR=38/44:Invalid Ds1 line coding for the line type' "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ListIndex(TextualConvention, Integer32):
    description = 'A unique value greater than zero, for each of the list that is defined. The object using this convention should give all the object specific details including the list type.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ListIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the ListIndex. In addition to the ListIndex range, this also includes 0 in its range of values. This value could be object specific and should be given the description of that object. In most cases, a value 0 means that the it does not represent any lists.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class TimeIntervalSec(TextualConvention, Unsigned32):
    description = 'A period of time, measured in units of 1 second.'
    status = 'current'

class TimeIntervalMin(TextualConvention, Unsigned32):
    description = 'A period of time, measured in units of 1 minute.'
    status = 'current'

class BDCOMMilliSeconds(TextualConvention, Unsigned32):
    description = 'Represents time unit value in milliseconds.'
    status = 'current'

class MicroSeconds(TextualConvention, Unsigned32):
    description = 'Represents time unit value in microseconds.'
    status = 'current'

mibBuilder.exportSymbols("BDCOM-TC", BDCOMIpProtocol=BDCOMIpProtocol, BDCOMLocationSpecifier=BDCOMLocationSpecifier, BDCOMNetworkProtocol=BDCOMNetworkProtocol, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, ListIndex=ListIndex, TimeIntervalSec=TimeIntervalSec, BDCOMAlarmSeverity=BDCOMAlarmSeverity, BDCOMAbsZeroBasedCounter32=BDCOMAbsZeroBasedCounter32, ListIndexOrZero=ListIndexOrZero, Unsigned64=Unsigned64, CountryCode=CountryCode, BDCOMLocationClass=BDCOMLocationClass, bdcomTextualConventions=bdcomTextualConventions, BDCOMRowOperStatus=BDCOMRowOperStatus, ConfigIterator=ConfigIterator, MicroSeconds=MicroSeconds, InterfaceIndexOrZero=InterfaceIndexOrZero, BDCOMNetworkAddress=BDCOMNetworkAddress, SAPType=SAPType, BDCOMMilliSeconds=BDCOMMilliSeconds, TimeIntervalMin=TimeIntervalMin, BDCOMPort=BDCOMPort, PerfHighIntervalCount=PerfHighIntervalCount, BDCOMSnapShotAbsCounter32=BDCOMSnapShotAbsCounter32, PYSNMP_MODULE_ID=bdcomTextualConventions, BDCOMInetAddressMask=BDCOMInetAddressMask, CountryCodeITU=CountryCodeITU, BulkConfigResult=BulkConfigResult)
