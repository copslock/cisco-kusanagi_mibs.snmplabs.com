#
# PySNMP MIB module IPAD-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPAD-ROUTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:55:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, ModuleIdentity, Bits, TimeTicks, Counter64, NotificationType, Gauge32, Unsigned32, enterprises, Counter32, IpAddress, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "ModuleIdentity", "Bits", "TimeTicks", "Counter64", "NotificationType", "Gauge32", "Unsigned32", "enterprises", "Counter32", "IpAddress", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
verilink = MibIdentifier((1, 3, 6, 1, 4, 1, 321))
hbu = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100))
ipad = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1))
ipadFrPort = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 1))
ipadService = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 2))
ipadChannel = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 3))
ipadDLCI = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 4))
ipadEndpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 5))
ipadUser = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 6))
ipadPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 7))
ipadModem = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 8))
ipadSvcAware = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 9))
ipadPktSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 10))
ipadTrapDest = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 11))
ipadMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 12))
ipadRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 13))
ipadCircuitParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1))
ipadRIPParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2))
ipadCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1), )
if mibBuilder.loadTexts: ipadCircuitTable.setStatus('optional')
if mibBuilder.loadTexts: ipadCircuitTable.setDescription('Table of Circuit parameters.')
ipadCircuitTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadCircuitIndex"))
if mibBuilder.loadTexts: ipadCircuitTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitTableEntry.setDescription('An entry in the ipad Circuit parameter table.')
ipadCircuitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadCircuitIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitIndex.setDescription('The index into the Circuit table.')
ipadCircuitEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEndpoint.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitEndpoint.setDescription('An entry in the endpoint table.')
ipadCircuitIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitIpAddress.setDescription('The IP Address of the Circuit.')
ipadCircuitIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitIpMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitIpMask.setDescription('The IP Mask of this Circuit IP address.')
ipadCircuitMaxTransmitUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitMaxTransmitUnit.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitMaxTransmitUnit.setDescription('The Maximum packet size carried by this Circuit.')
ipadCircuitCost = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitCost.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitCost.setDescription('The cost (delay) of this Circuit.')
ipadCircuitEnableRIP = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEnableRIP.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitEnableRIP.setDescription('To enable or disable RIP for this Circuit.')
ipadCircuitEnableOSPF = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEnableOSPF.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitEnableOSPF.setDescription('To enable or disable OSPF for this Circuit.')
ipadCircuitEnableMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEnableMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitEnableMulticast.setDescription('To allow multicast adressing for this Circuit.')
ipadCircuitAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitAdd.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitAdd.setDescription('Writing addnew(2) to this field causes a new (blank) route to be appended to the Circuit Table.')
ipadCircuitDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitDelete.setStatus('mandatory')
if mibBuilder.loadTexts: ipadCircuitDelete.setDescription('Writing the index of an entry in the Circuit table causes that entry to be deleted.')
ipadRIPEnable = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPEnable.setDescription('Determines if RIP routing is enabled.')
ipadRIPTrustNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPTrustNeighbors.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPTrustNeighbors.setDescription('Determines if RIP Neighbors should be trusted.')
ipadRIPInterval = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPInterval.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPInterval.setDescription('Specifies the RIP interval in seconds.')
ipadRIPDomain = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPDomain.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPDomain.setDescription('Specifies the RIP Domain.')
ipadRIPStaticARPTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5), )
if mibBuilder.loadTexts: ipadRIPStaticARPTable.setStatus('optional')
if mibBuilder.loadTexts: ipadRIPStaticARPTable.setDescription('Table of RIP Static ARP parameters.')
ipadRIPStaticARPTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadRIPStaticARPIndex"))
if mibBuilder.loadTexts: ipadRIPStaticARPTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPTableEntry.setDescription('An entry in the ipad RIP Static ARP parameter table.')
ipadRIPStaticARPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPStaticARPIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPIndex.setDescription('The index into the RIP Static ARP table.')
ipadRIPStaticARPEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPEndpoint.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPEndpoint.setDescription('An entry in the endpoint table.')
ipadRIPStaticARPIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPIpAddress.setDescription('This is the IP address of the device we will associate the MAC or DLCI address.')
ipadRIPStaticARPMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPMacAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPMacAddress.setDescription('MAC address of the device.')
ipadRIPStaticARPDLCIAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPDLCIAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPDLCIAddress.setDescription('DLCI address of the device.')
ipadRIPStaticARPEnableARP = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPEnableARP.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPEnableARP.setDescription('Enable that Static ARP Entry.')
ipadRIPStaticARPAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPAdd.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPAdd.setDescription('Writing addnew(2) to this field causes a new (blank) route to be appended to the Static ARP Table.')
ipadRIPStaticARPDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPDelete.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticARPDelete.setDescription('Writing the index of an entry in the Static ARP table causes that entry to be deleted.')
ipadRIPStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8), )
if mibBuilder.loadTexts: ipadRIPStaticRouteTable.setStatus('optional')
if mibBuilder.loadTexts: ipadRIPStaticRouteTable.setDescription('Table of RIP Static Route parameters.')
ipadRIPStaticRouteTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadRIPStaticRouteIndex"))
if mibBuilder.loadTexts: ipadRIPStaticRouteTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteTableEntry.setDescription('An entry in the ipad RIP Static Route parameter table.')
ipadRIPStaticRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPStaticRouteIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteIndex.setDescription('The index into the RIP Static Route table.')
ipadRIPStaticRouteEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteEndpoint.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteEndpoint.setDescription('An entry in the endpoint table.')
ipadRIPStaticRouteTargetIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteTargetIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteTargetIpAddress.setDescription('')
ipadRIPStaticRouteTargetIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteTargetIpMask.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteTargetIpMask.setDescription('IP Mask of the IP address.')
ipadRIPStaticRouteNextHopIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteNextHopIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteNextHopIpAddress.setDescription('Next Hop IP address to reach the remote Network.')
ipadRIPStaticRouteCost = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteCost.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteCost.setDescription('Cost to reach that remote Network.')
ipadRIPStaticRouteEnableRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteEnableRouter.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteEnableRouter.setDescription('Enable or Not this static route.')
ipadRIPStaticRouteAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteAdd.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteAdd.setDescription('Writing addnew(2) to this field causes a new (blank) route to be appended to the Static Route Table.')
ipadRIPStaticRouteDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteDelete.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPStaticRouteDelete.setDescription('Writing the index of an entry in the Static Route table causes that entry to be deleted.')
ipadRIPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11), )
if mibBuilder.loadTexts: ipadRIPNeighborTable.setStatus('optional')
if mibBuilder.loadTexts: ipadRIPNeighborTable.setDescription('Table of RIP trusted neighbors.')
ipadRIPNeighborTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadRIPNeighborIndex"))
if mibBuilder.loadTexts: ipadRIPNeighborTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPNeighborTableEntry.setDescription('An entry in the ipad RIP trusted neighbor table.')
ipadRIPNeighborIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPNeighborIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPNeighborIndex.setDescription('The index into the ipadRIPNeighborTable.')
ipadRIPNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPNeighborAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPNeighborAddress.setDescription('A RIP trusted neighbor.')
ipadRIPNeighborAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPNeighborAdd.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPNeighborAdd.setDescription('Writing an IP address to this object adds the IP address to the ipad RIP Trusted Neighbor table.')
ipadRIPNeighborDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPNeighborDelete.setStatus('mandatory')
if mibBuilder.loadTexts: ipadRIPNeighborDelete.setDescription('Writing an IP address to this object removes the IP address from the ipad RIP Trusted Neighbor table.')
mibBuilder.exportSymbols("IPAD-ROUTER-MIB", ipadRIPStaticRouteTargetIpMask=ipadRIPStaticRouteTargetIpMask, ipadRIPNeighborTableEntry=ipadRIPNeighborTableEntry, ipadCircuitEnableMulticast=ipadCircuitEnableMulticast, ipadRIPStaticRouteIndex=ipadRIPStaticRouteIndex, ipadService=ipadService, ipadRIPStaticARPDelete=ipadRIPStaticARPDelete, ipadRIPStaticARPIpAddress=ipadRIPStaticARPIpAddress, ipadRIPStaticRouteEndpoint=ipadRIPStaticRouteEndpoint, ipadRIPStaticRouteTargetIpAddress=ipadRIPStaticRouteTargetIpAddress, ipadCircuitDelete=ipadCircuitDelete, ipadMisc=ipadMisc, ipadRIPNeighborDelete=ipadRIPNeighborDelete, ipadCircuitEndpoint=ipadCircuitEndpoint, ipad=ipad, ipadRIPDomain=ipadRIPDomain, ipadRIPStaticARPTableEntry=ipadRIPStaticARPTableEntry, ipadRIPStaticRouteEnableRouter=ipadRIPStaticRouteEnableRouter, ipadPPP=ipadPPP, ipadRIPStaticARPIndex=ipadRIPStaticARPIndex, ipadCircuitEnableOSPF=ipadCircuitEnableOSPF, ipadCircuitAdd=ipadCircuitAdd, ipadRIPStaticARPAdd=ipadRIPStaticARPAdd, ipadRIPNeighborTable=ipadRIPNeighborTable, ipadRIPStaticARPTable=ipadRIPStaticARPTable, ipadRIPStaticARPDLCIAddress=ipadRIPStaticARPDLCIAddress, hbu=hbu, ipadDLCI=ipadDLCI, ipadCircuitEnableRIP=ipadCircuitEnableRIP, verilink=verilink, ipadEndpoint=ipadEndpoint, ipadRIPStaticRouteTable=ipadRIPStaticRouteTable, ipadRIPNeighborAddress=ipadRIPNeighborAddress, ipadCircuitIpMask=ipadCircuitIpMask, ipadRouter=ipadRouter, ipadRIPStaticARPEndpoint=ipadRIPStaticARPEndpoint, ipadCircuitParms=ipadCircuitParms, ipadRIPStaticARPEnableARP=ipadRIPStaticARPEnableARP, ipadSvcAware=ipadSvcAware, ipadRIPStaticRouteCost=ipadRIPStaticRouteCost, ipadRIPParms=ipadRIPParms, ipadRIPStaticRouteAdd=ipadRIPStaticRouteAdd, ipadRIPNeighborAdd=ipadRIPNeighborAdd, ipadRIPStaticRouteDelete=ipadRIPStaticRouteDelete, ipadRIPStaticARPMacAddress=ipadRIPStaticARPMacAddress, ipadCircuitMaxTransmitUnit=ipadCircuitMaxTransmitUnit, ipadCircuitTableEntry=ipadCircuitTableEntry, ipadUser=ipadUser, ipadRIPStaticRouteTableEntry=ipadRIPStaticRouteTableEntry, ipadRIPNeighborIndex=ipadRIPNeighborIndex, ipadModem=ipadModem, ipadCircuitIndex=ipadCircuitIndex, ipadFrPort=ipadFrPort, ipadRIPEnable=ipadRIPEnable, ipadRIPTrustNeighbors=ipadRIPTrustNeighbors, ipadTrapDest=ipadTrapDest, ipadCircuitTable=ipadCircuitTable, ipadCircuitCost=ipadCircuitCost, ipadCircuitIpAddress=ipadCircuitIpAddress, ipadRIPStaticRouteNextHopIpAddress=ipadRIPStaticRouteNextHopIpAddress, ipadChannel=ipadChannel, ipadRIPInterval=ipadRIPInterval, ipadPktSwitch=ipadPktSwitch)
