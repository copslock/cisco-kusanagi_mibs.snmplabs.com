#
# PySNMP MIB module IBMBNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMBNA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity, Counter32, Integer32, Gauge32, MibIdentifier, IpAddress, enterprises, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter32", "Integer32", "Gauge32", "MibIdentifier", "IpAddress", "enterprises", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmArchitecture = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5))
ibmBna = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 21))
ibmBnaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 21, 1))
ibmBnaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 21, 2))
ibmBnaLocalTgTable = MibTable((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1), )
if mibBuilder.loadTexts: ibmBnaLocalTgTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaLocalTgTable.setDescription('Table of objects that identify the branch uplinks and downlinks for an APPN node implementing the APPN Branch Network Architecture. This table is effectively an extension to the appnLocalTgTable defined in the APPN MIB (RFC nnnn). If an implementation that supports the architecture has its branch network node support disabled, then this table is empty. Conversely, if a Management Station determines that there are entries present in this table, then by implication the agent where the table resides currently has its branch network node functionality enabled.')
ibmBnaLocalTgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1), ).setIndexNames((0, "IBMBNA-MIB", "ibmBnaLocalTgDest"), (0, "IBMBNA-MIB", "ibmBnaLocalTgNum"))
if mibBuilder.loadTexts: ibmBnaLocalTgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaLocalTgEntry.setDescription('This table is indexed by the destination CP name and the TG number.')
ibmBnaLocalTgDest = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaLocalTgDest.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaLocalTgDest.setDescription('Administratively assigned name of the destination node for this TG. This is the fully qualified name of a network node, end node, LEN node, or virtual routing node.')
ibmBnaLocalTgNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaLocalTgNum.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaLocalTgNum.setDescription('Number associated with this transmission group.')
ibmBnaLocalTgLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("other", 1), ("uplink", 2), ("downlink", 3), ("downlinkToBranchNetworkNode", 4), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaLocalTgLinkType.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaLocalTgLinkType.setDescription("Branch link type of this TG: other(1) = the agent has determined the TG's branch link type to be a value other than branch uplink or branch downlink. This is the value used for a connection network TG owned by a node that implements the APPN Branch Network Architecture. uplink(2) = the TG is a branch uplink. downlink(3) = the TG is a branch downlink to an end node. downlinkToBranchNetworkNode(4) = the TG is a branch downlink to a cascaded branch network node. unknown(255) = the agent cannot determine the branch link type of the TG.")
ibmBnaNnTopologyFRTable = MibTable((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2), )
if mibBuilder.loadTexts: ibmBnaNnTopologyFRTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTopologyFRTable.setDescription('Table of objects that identify which of the network nodes in an APPN topology subnet support branch awareness. This table is effectively an extension to the appnNnTopologyFRTable defined in the APPN MIB (RFC nnnn).')
ibmBnaNnTopologyFREntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1), ).setIndexNames((0, "IBMBNA-MIB", "ibmBnaNnNodeFRFrsn"), (0, "IBMBNA-MIB", "ibmBnaNnNodeFRName"))
if mibBuilder.loadTexts: ibmBnaNnTopologyFREntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTopologyFREntry.setDescription('This table is indexed by FRSN and by fully qualified node name.')
ibmBnaNnNodeFRFrsn = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnNodeFRFrsn.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnNodeFRFrsn.setDescription('Flow reduction sequence numbers (FRSNs) are associated with Topology Database Updates (TDUs) and are unique only within each APPN network node. A TDU can be associated with multiple APPN resources. This FRSN indicates the last relative time this resource was updated at the agent node.')
ibmBnaNnNodeFRName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnNodeFRName.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnNodeFRName.setDescription('Administratively assigned network name that is locally defined at each network node in the format NetId.CpName.')
ibmBnaNnNodeFRBranchAwareness = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnNodeFRBranchAwareness.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnNodeFRBranchAwareness.setDescription('Indicates whether this node supports branch awareness. This object corresponds to cv4580, byte 8, bit 4.')
ibmBnaNnTgTopologyFRTable = MibTable((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3), )
if mibBuilder.loadTexts: ibmBnaNnTgTopologyFRTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTgTopologyFRTable.setDescription('Table of objects that identify which of the TGs owned by network nodes in an APPN topology subnet are branch TGs. This table is effectively an extension to the appnNnTgTopologyFRTable defined in the APPN MIB (RFC nnnn).')
ibmBnaNnTgTopologyFREntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1), ).setIndexNames((0, "IBMBNA-MIB", "ibmBnaNnTgFRFrsn"), (0, "IBMBNA-MIB", "ibmBnaNnTgFROwner"), (0, "IBMBNA-MIB", "ibmBnaNnTgFRDest"), (0, "IBMBNA-MIB", "ibmBnaNnTgFRNum"))
if mibBuilder.loadTexts: ibmBnaNnTgTopologyFREntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTgTopologyFREntry.setDescription('This table is indexed by four columns: FRSN, TG owner fully qualified node name, TG destination fully qualified node name, and TG number.')
ibmBnaNnTgFRFrsn = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnTgFRFrsn.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTgFRFrsn.setDescription('Flow reduction sequence numbers (FRSNs) are associated with Topology Database Updates (TDUs) and are unique only within each APPN network node. A TDU can be associated with multiple APPN resources. This FRSN indicates the last time this resource was updated at this node.')
ibmBnaNnTgFROwner = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnTgFROwner.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTgFROwner.setDescription('Administratively assigned name for the originating node for this TG. The format is NetId.CpName and is the same name specified in the node table.')
ibmBnaNnTgFRDest = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnTgFRDest.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTgFRDest.setDescription('Administratively assigned fully qualified network name for the destination node for this TG.')
ibmBnaNnTgFRNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnTgFRNum.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTgFRNum.setDescription('Number associated with this transmission group. Range is 0-255.')
ibmBnaNnTgFRBranchTg = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaNnTgFRBranchTg.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaNnTgFRBranchTg.setDescription('Indicates whether the transmission group is a branch TG (equivalently, whether the destination of the transmission group is a node supporting the APPN Branch Network Architecture). This object corresponds to cv4680, byte m+1, bit 1.')
ibmBnaDirTable = MibTable((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4), )
if mibBuilder.loadTexts: ibmBnaDirTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaDirTable.setDescription('Table of objects that identify the apparent owning control point for an LU below a node that supports the APPN Branch Network Architecture. This table is effectively an extension to the appnDirTable defined in the APPN MIB (RFC nnnn).')
ibmBnaDirEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4, 1), ).setIndexNames((0, "IBMBNA-MIB", "ibmBnaDirLuName"))
if mibBuilder.loadTexts: ibmBnaDirEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaDirEntry.setDescription('This table is indexed by the LU name.')
ibmBnaDirLuName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaDirLuName.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaDirLuName.setDescription("Fully qualified network LU name in the domain of the serving network node. Entries take one of three forms: - Explicit entries do not contain the character '*'. - Partial wildcard entries have the form 'ccc*', where 'c' represents a character in a legal SNA LuName. - A full wildcard entry consists of the single character '*'.")
ibmBnaDirApparentLuOwnerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 5, 21, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 17), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmBnaDirApparentLuOwnerName.setStatus('mandatory')
if mibBuilder.loadTexts: ibmBnaDirApparentLuOwnerName.setDescription("Fully qualified CP name of the node at which the LU appears to be located. This object and the appnDirLuOwnerName object in the APPN MIB are related as follows: Implementations that support this object save in their directory database information about an LU's owning control point that was communicated in two control vectors: - an Associated Resource Entry (X'3C') CV with resource type X'00F4' (ENCP) - a Real Owning Control Point (X'4A') CV. The X'4A' CV is created by a branch network node to preserve the name of the real owning control point for an LU below the branch network node, before it overwrites this name with its own name in the X'3C' CV. The X'4A' CV is not present for LUs that are not below branch network nodes. If the information a node has about an LU's owning CP came only in a X'3C' CV, then the name from the X'3C' is returned in the appnDirLuOwnerName object, and a null string is returned in this object. If the information a node has about an LU's owning CP came in both X'3C' and X'4A' CVs, then the name from the X'4A' is returned in the appnDirLuOwnerName object, and the name from the X'3C' (which will be the branch network node's name) is returned in this object.")
ibmBnaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 21, 2, 1))
ibmBnaConfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 21, 2, 2))
mibBuilder.exportSymbols("IBMBNA-MIB", ibmBnaNnTopologyFREntry=ibmBnaNnTopologyFREntry, ibmBnaConfGroups=ibmBnaConfGroups, ibmBna=ibmBna, ibmBnaLocalTgNum=ibmBnaLocalTgNum, ibmBnaNnTgFRNum=ibmBnaNnTgFRNum, ibmBnaNnTgFRFrsn=ibmBnaNnTgFRFrsn, ibmArchitecture=ibmArchitecture, ibmBnaDirLuName=ibmBnaDirLuName, ibmBnaLocalTgLinkType=ibmBnaLocalTgLinkType, ibmBnaNnTgTopologyFREntry=ibmBnaNnTgTopologyFREntry, ibmBnaLocalTgTable=ibmBnaLocalTgTable, ibmBnaNnTopologyFRTable=ibmBnaNnTopologyFRTable, ibm=ibm, ibmBnaNnNodeFRBranchAwareness=ibmBnaNnNodeFRBranchAwareness, ibmBnaDirEntry=ibmBnaDirEntry, ibmBnaLocalTgDest=ibmBnaLocalTgDest, ibmBnaLocalTgEntry=ibmBnaLocalTgEntry, ibmBnaNnNodeFRName=ibmBnaNnNodeFRName, ibmBnaCompliances=ibmBnaCompliances, ibmBnaNnTgFROwner=ibmBnaNnTgFROwner, TruthValue=TruthValue, ibmBnaNnTgFRBranchTg=ibmBnaNnTgFRBranchTg, ibmBnaNnTgTopologyFRTable=ibmBnaNnTgTopologyFRTable, ibmBnaNnTgFRDest=ibmBnaNnTgFRDest, ibmBnaNnNodeFRFrsn=ibmBnaNnNodeFRFrsn, ibmBnaObjects=ibmBnaObjects, ibmBnaDirTable=ibmBnaDirTable, ibmBnaConformance=ibmBnaConformance, ibmBnaDirApparentLuOwnerName=ibmBnaDirApparentLuOwnerName)
