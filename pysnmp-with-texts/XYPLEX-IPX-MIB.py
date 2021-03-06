#
# PySNMP MIB module XYPLEX-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYPLEX-IPX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:46:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, Gauge32, ModuleIdentity, Counter64, iso, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Unsigned32, ObjectIdentity, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Gauge32", "ModuleIdentity", "Counter64", "iso", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Unsigned32", "ObjectIdentity", "enterprises", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
ipx = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15))
ipxSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 1))
ipxIf = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 2))
ipxNetbios = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 3))
ipxRip = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 4))
ipxSap = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 15, 5))
ipxRouting = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxRouting.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRouting.setDescription('Control for IPX routing services.')
ipxIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 2, 1), )
if mibBuilder.loadTexts: ipxIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfTable.setDescription('A list of IPX interface entries.')
ipxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxIfIndex"))
if mibBuilder.loadTexts: ipxIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfEntry.setDescription('IPX interface parameters and counters.')
ipxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfIndex.setDescription('An index value that uniquely identifies an IPX interface. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
ipxIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfState.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfState.setDescription('Control for IPX routing services for this interface.')
ipxIfNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetwork.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfNetwork.setDescription('The IPX network number of the network to which this interface is attached.')
ipxIfFrameStyle = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8022", 2))).clone('ieee8022')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfFrameStyle.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfFrameStyle.setDescription('Control for the CSMA/CD frame style to use on this interface.')
ipxIfFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfFramesIn.setDescription('The number of IPX frames received on this interface.')
ipxIfFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfFramesOut.setDescription('The number of IPX frames sent on this interface.')
ipxIfErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfErrors.setDescription('The number of IPX errors seen on this interface.')
ipxIfTransitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfTransitDelay.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfTransitDelay.setDescription('The number of 55 millisecond ticks it takes for a packet to travel from one destination to another on the interface. A value of 0 means that the system will calculate this value based on the measured speed of the interface.')
ipxIfTransitDelayActual = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfTransitDelayActual.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfTransitDelayActual.setDescription('The number of 55 millisecond ticks it takes for a packet to travel from one destination to another on the interface.')
ipxNetbiosHopLimit = MibScalar((1, 3, 6, 1, 4, 1, 33, 15, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxNetbiosHopLimit.setStatus('mandatory')
if mibBuilder.loadTexts: ipxNetbiosHopLimit.setDescription('Maximum number of hops that an IPX Netbios packet may make.')
ipxNetbiosIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 3, 2), )
if mibBuilder.loadTexts: ipxNetbiosIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxNetbiosIfTable.setDescription('A list of IPX interface entries.')
ipxNetbiosIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxNetbiosIfIndex"))
if mibBuilder.loadTexts: ipxNetbiosIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxNetbiosIfEntry.setDescription('IPX interface parameters and counters.')
ipxNetbiosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxNetbiosIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipxNetbiosIfIndex.setDescription('An index value that uniquely identifies an IPX interface. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
ipxIfNetbiosForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfNetbiosForwarding.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfNetbiosForwarding.setDescription('Control whether Netbios packet will be forwarded in or out on this interface.')
ipxIfNetbiosIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfNetbiosIn.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfNetbiosIn.setDescription('The number of IPX Netbios frames received on this interface.')
ipxIfNetbiosOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfNetbiosOut.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfNetbiosOut.setDescription('The number of IPX Netbios frames sent on this interface.')
ipxRipIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 4, 1), )
if mibBuilder.loadTexts: ipxRipIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipIfTable.setDescription('A list of IPX interface entries.')
ipxRipIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxRipIfIndex"))
if mibBuilder.loadTexts: ipxRipIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipIfEntry.setDescription('IPX interface parameters and counters.')
ipxRipIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipIfIndex.setDescription('An index value that uniquely identifies an IPX interface. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
ipxIfRipBcst = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcst.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfRipBcst.setDescription('Control whether RIP packets will be broadcasted out this interface.')
ipxIfRipBcstDiscardTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 3), Integer32().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcstDiscardTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfRipBcstDiscardTimeout.setDescription('The number of seconds to wait before discarding information learned from a RIP broadcast.')
ipxIfRipBcstTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 4), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfRipBcstTimer.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfRipBcstTimer.setDescription('The number of seconds to wait between sending out RIP broadcasts.')
ipxIfRipIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipIn.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfRipIn.setDescription('The number of RIP broadcasts received on this interface.')
ipxIfRipOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipOut.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfRipOut.setDescription('The number of RIP broadcasts sent on this interface.')
ipxIfRipAgedOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfRipAgedOut.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfRipAgedOut.setDescription('The number of entries timed out and discarded on this interface.')
ipxRipTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 4, 2), )
if mibBuilder.loadTexts: ipxRipTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipTable.setDescription('A list of RIP entries.')
ipxRipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxRipNetwork"))
if mibBuilder.loadTexts: ipxRipEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipEntry.setDescription('IPX interface parameters and counters.')
ipxRipNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipNetwork.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipNetwork.setDescription('An IPX network number to which this router knows a path.')
ipxRipRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipRouter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipRouter.setDescription('The Ethernet address of an IPX router on this network.')
ipxRipInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipInterface.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipInterface.setDescription('The interface to reach the router. A value of ifIndex.')
ipxRipHops = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipHops.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipHops.setDescription('The number of hops to reach the router.')
ipxRipTransTime = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipTransTime.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipTransTime.setDescription('The number of 55 millisecond ticks it takes for a packet to travel to the router.')
ipxRipAge = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxRipAge.setStatus('mandatory')
if mibBuilder.loadTexts: ipxRipAge.setDescription('The age of the RIP entry in seconds.')
ipxSapIfTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 5, 1), )
if mibBuilder.loadTexts: ipxSapIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapIfTable.setDescription('A list of IPX interface entries.')
ipxSapIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxSapIfIndex"))
if mibBuilder.loadTexts: ipxSapIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapIfEntry.setDescription('IPX interface parameters and counters.')
ipxSapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapIfIndex.setDescription('An index value that uniquely identifies an IPX interface. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
ipxIfSapBcst = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcst.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfSapBcst.setDescription('Control whether SAP packets will be broadcasted out this interface.')
ipxIfSapBcstDiscardTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 3), Integer32().clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcstDiscardTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfSapBcstDiscardTimeout.setDescription('The number of seconds to wait before discarding information learned from a SAP broadcast.')
ipxIfSapBcstTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 4), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxIfSapBcstTimer.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfSapBcstTimer.setDescription('The number of seconds to wait between sending out SAP broadcasts.')
ipxIfSapIn = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapIn.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfSapIn.setDescription('The number SAP broadcasts received on this interface.')
ipxIfSapOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapOut.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfSapOut.setDescription('The number SAP broadcasts sent on this interface.')
ipxIfSapAgedOut = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxIfSapAgedOut.setStatus('mandatory')
if mibBuilder.loadTexts: ipxIfSapAgedOut.setDescription('The number entries for this interface discarded due to aging timeout.')
ipxSapTable = MibTable((1, 3, 6, 1, 4, 1, 33, 15, 5, 2), )
if mibBuilder.loadTexts: ipxSapTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapTable.setDescription('A list of SAP entries.')
ipxSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1), ).setIndexNames((0, "XYPLEX-IPX-MIB", "ipxSapName"), (0, "XYPLEX-IPX-MIB", "ipxSapType"))
if mibBuilder.loadTexts: ipxSapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapEntry.setDescription('IPX interface parameters and counters.')
ipxSapName = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(48, 48)).setFixedLength(48)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapName.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapName.setDescription('The name of the service, null filled.')
ipxSapNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapNetwork.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapNetwork.setDescription("The IPX network number on which the service's host resides.")
ipxSapHost = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapHost.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapHost.setDescription('The Ethernet address of the IPX host of the service.')
ipxSapSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapSocket.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapSocket.setDescription('The socket number of the service on the host.')
ipxSapInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapInterface.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapInterface.setDescription('The interface of the router in the direction of the service. A value of ifIndex.')
ipxSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("user", 1), ("userGroup", 2), ("printQueue", 3), ("novellFileServer", 4), ("jobServer", 5), ("gateway1", 6), ("printServer", 7), ("archiveQueue", 8), ("archiveServer", 9), ("jobQueue", 10), ("administration", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapType.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapType.setDescription('The type of the service.')
ipxSapAge = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxSapAge.setStatus('mandatory')
if mibBuilder.loadTexts: ipxSapAge.setDescription('The age of the Sap entry in seconds.')
mibBuilder.exportSymbols("XYPLEX-IPX-MIB", ipxSap=ipxSap, ipxSapNetwork=ipxSapNetwork, ipxSapAge=ipxSapAge, ipxRipTransTime=ipxRipTransTime, ipxIfNetbiosOut=ipxIfNetbiosOut, ipxRip=ipxRip, ipxIfNetwork=ipxIfNetwork, ipxIfRipIn=ipxIfRipIn, ipxSapTable=ipxSapTable, ipxNetbios=ipxNetbios, ipxIfTable=ipxIfTable, ipx=ipx, ipxIfTransitDelayActual=ipxIfTransitDelayActual, ipxSapName=ipxSapName, ipxSapEntry=ipxSapEntry, ipxIfRipAgedOut=ipxIfRipAgedOut, ipxIfSapAgedOut=ipxIfSapAgedOut, ipxIfSapIn=ipxIfSapIn, ipxIfFramesOut=ipxIfFramesOut, ipxIfErrors=ipxIfErrors, ipxRipIfTable=ipxRipIfTable, ipxRipRouter=ipxRipRouter, ipxIfFrameStyle=ipxIfFrameStyle, ipxSapIfIndex=ipxSapIfIndex, xyplex=xyplex, ipxIfIndex=ipxIfIndex, ipxRipInterface=ipxRipInterface, ipxRipAge=ipxRipAge, ipxSapIfEntry=ipxSapIfEntry, ipxIfSapOut=ipxIfSapOut, ipxSapSocket=ipxSapSocket, ipxIfRipBcstDiscardTimeout=ipxIfRipBcstDiscardTimeout, ipxIfNetbiosForwarding=ipxIfNetbiosForwarding, ipxIfRipBcst=ipxIfRipBcst, ipxIfFramesIn=ipxIfFramesIn, ipxRipEntry=ipxRipEntry, ipxSapIfTable=ipxSapIfTable, ipxNetbiosIfEntry=ipxNetbiosIfEntry, ipxIfSapBcstTimer=ipxIfSapBcstTimer, ipxNetbiosIfTable=ipxNetbiosIfTable, ipxIfTransitDelay=ipxIfTransitDelay, ipxRipNetwork=ipxRipNetwork, ipxIfState=ipxIfState, ipxIfSapBcstDiscardTimeout=ipxIfSapBcstDiscardTimeout, ipxIfSapBcst=ipxIfSapBcst, ipxIf=ipxIf, ipxRouting=ipxRouting, ipxNetbiosHopLimit=ipxNetbiosHopLimit, ipxSapHost=ipxSapHost, ipxRipTable=ipxRipTable, ipxIfRipBcstTimer=ipxIfRipBcstTimer, ipxRipIfIndex=ipxRipIfIndex, ipxRipIfEntry=ipxRipIfEntry, ipxIfEntry=ipxIfEntry, ipxRipHops=ipxRipHops, ipxSystem=ipxSystem, ipxNetbiosIfIndex=ipxNetbiosIfIndex, ipxIfNetbiosIn=ipxIfNetbiosIn, ipxIfRipOut=ipxIfRipOut, ipxSapInterface=ipxSapInterface, ipxSapType=ipxSapType)
