#
# PySNMP MIB module STN-PPTP-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-PPTP-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Gauge32, IpAddress, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Integer32, Counter32, ModuleIdentity, Counter64, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "IpAddress", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Integer32", "Counter32", "ModuleIdentity", "Counter64", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stnNotification, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification")
stnEngineIndex, stnEngineSlot, stnEngineCpu = mibBuilder.importSymbols("STN-CHASSIS-MIB", "stnEngineIndex", "stnEngineSlot", "stnEngineCpu")
stnPptpTraps, = mibBuilder.importSymbols("STN-PPTP-MIB", "stnPptpTraps")
stnSubnetInterfaceIndex, stnRouterIndex = mibBuilder.importSymbols("STN-ROUTER-MIB", "stnSubnetInterfaceIndex", "stnRouterIndex")
stnPptpTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1))
if mibBuilder.loadTexts: stnPptpTrap.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnPptpTrap.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: stnPptpTrap.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: stnPptpTrap.setDescription('This MIB module describes the traps for Spring Tide Networks PPTP.')
stnPptpTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1))
stnPptpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2))
stnPptpNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0))
stnPptpTunnelLocalHostname = MibScalar((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPptpTunnelLocalHostname.setStatus('current')
if mibBuilder.loadTexts: stnPptpTunnelLocalHostname.setDescription('This object contains the host name supplied during the tunnel establishment phase to the PPTP peer.')
stnPptpTunnelLocalIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPptpTunnelLocalIpAddress.setStatus('current')
if mibBuilder.loadTexts: stnPptpTunnelLocalIpAddress.setDescription('This object contains the local IP address of the tunnel endpoint.')
stnPptpTunnelRemoteHostname = MibScalar((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPptpTunnelRemoteHostname.setStatus('current')
if mibBuilder.loadTexts: stnPptpTunnelRemoteHostname.setDescription('This object contains the host name as discovered during the tunnel establishment phase of the PPTP peer.')
stnPptpTunnelRemoteIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPptpTunnelRemoteIpAddress.setStatus('current')
if mibBuilder.loadTexts: stnPptpTunnelRemoteIpAddress.setDescription('This object contains the IP address of the remote tunnel endpoint.')
stnTunnelPptpAuthenFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 1)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteIpAddress"))
if mibBuilder.loadTexts: stnTunnelPptpAuthenFailure.setStatus('current')
if mibBuilder.loadTexts: stnTunnelPptpAuthenFailure.setDescription('A stnTunnelPptpAuthenFailure trap signifies that the agent entity has detected an attempt to establish a tunnel to a remote peer has failed authentication. The generation of this trap can be controlled by the PPTPTraps configuration object.')
stnTunnelPptpLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 2)).setObjects(("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"))
if mibBuilder.loadTexts: stnTunnelPptpLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: stnTunnelPptpLimitExceeded.setDescription('A stnTunnelPptpLimitExceeded trap signifies that the agent entity has detected that the number of PPTP tunnels allowed on the indicated slot/cpu has been exceeded. The generation of this trap can be controlled by the PPTPTraps configuration object.')
stnTunnelPacProvLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 3)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalIpAddress"))
if mibBuilder.loadTexts: stnTunnelPacProvLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: stnTunnelPacProvLimitExceeded.setDescription('A stnTunnelPacProvLimitExceeded trap signifies that the agent entity has detected that the number of PPTP locally initiated tunnels allowed by the provisioner has been exceeded for the indicated router. The generation of this trap can be controlled by the PPTPTraps configuration object.')
stnTunnelPnsProvLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 4)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalIpAddress"))
if mibBuilder.loadTexts: stnTunnelPnsProvLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: stnTunnelPnsProvLimitExceeded.setDescription('A stnTunnelPnsProvLimitExceeded trap signifies that the agent entity has detected that the number of PPTP remotely initiated tunnels allowed by the provisioner has been exceeded for the indicated router. The generation of this trap can be controlled by the PPTPTraps configuration object.')
stnCallPptpLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 5)).setObjects(("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"))
if mibBuilder.loadTexts: stnCallPptpLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: stnCallPptpLimitExceeded.setDescription('A stnCallPptpLimitExceeded trap signifies that the agent entity has detected that the number of PPTP calls allowed on the indicated slot/cpu has been exceeded. The generation of this trap can be controlled by the PPTPTraps configuration object.')
stnCallPacProvLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 6)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteIpAddress"))
if mibBuilder.loadTexts: stnCallPacProvLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: stnCallPacProvLimitExceeded.setDescription('A stnCallPacProvLimitExceeded trap signifies that the agent entity has detected that the number of PPTP locally initiated calls allowed by the provisioner has been exceeded for the indicated router. The generation of this trap can be controlled by the PPTPTraps configuration object.')
stnCallPnsProvLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3, 1, 2, 0, 7)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelLocalHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteHostname"), ("STN-PPTP-TRAP-MIB", "stnPptpTunnelRemoteIpAddress"))
if mibBuilder.loadTexts: stnCallPnsProvLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: stnCallPnsProvLimitExceeded.setDescription('A stnCallPnsProvLimitExceeded trap signifies that the agent entity has detected that the number of PPTP remotely initiated calls allowed by the provisioner has been exceeded for the indicated router. The generation of this trap can be controlled by the PPTPTraps configuration object.')
mibBuilder.exportSymbols("STN-PPTP-TRAP-MIB", stnPptpTunnelLocalHostname=stnPptpTunnelLocalHostname, stnTunnelPnsProvLimitExceeded=stnTunnelPnsProvLimitExceeded, stnPptpNotificationPrefix=stnPptpNotificationPrefix, stnPptpTunnelRemoteIpAddress=stnPptpTunnelRemoteIpAddress, PYSNMP_MODULE_ID=stnPptpTrap, stnTunnelPacProvLimitExceeded=stnTunnelPacProvLimitExceeded, stnTunnelPptpLimitExceeded=stnTunnelPptpLimitExceeded, stnPptpNotification=stnPptpNotification, stnCallPptpLimitExceeded=stnCallPptpLimitExceeded, stnTunnelPptpAuthenFailure=stnTunnelPptpAuthenFailure, stnPptpTrap=stnPptpTrap, stnCallPacProvLimitExceeded=stnCallPacProvLimitExceeded, stnCallPnsProvLimitExceeded=stnCallPnsProvLimitExceeded, stnPptpTrapVars=stnPptpTrapVars, stnPptpTunnelRemoteHostname=stnPptpTunnelRemoteHostname, stnPptpTunnelLocalIpAddress=stnPptpTunnelLocalIpAddress)
