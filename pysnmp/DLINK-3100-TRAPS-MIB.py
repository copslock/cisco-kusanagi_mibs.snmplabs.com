#
# PySNMP MIB module DLINK-3100-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:34:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
rldot1dStpTrapVrblVID, rldot1dStpTrapVrblifIndex = mibBuilder.importSymbols("DLINK-3100-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID", "rldot1dStpTrapVrblifIndex")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
rndNotifications, = mibBuilder.importSymbols("DLINK-3100-MIB", "rndNotifications")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, Integer32, NotificationType, Bits, Counter64, Counter32, Gauge32, ModuleIdentity, IpAddress, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Integer32", "NotificationType", "Bits", "Counter64", "Counter32", "Gauge32", "ModuleIdentity", "IpAddress", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rxOverflowHWFault = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 3)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rxOverflowHWFault.setStatus('current')
txOverflowHWFault = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 4)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: txOverflowHWFault.setStatus('current')
routeTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 5)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: routeTableOverflow.setStatus('current')
resetRequired = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 10)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: resetRequired.setStatus('current')
endTftp = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 12)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: endTftp.setStatus('current')
abortTftp = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 13)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: abortTftp.setStatus('current')
startTftp = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 14)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: startTftp.setStatus('current')
faultBackUp = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 23)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: faultBackUp.setStatus('current')
mainLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 24)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: mainLinkUp.setStatus('current')
ipxRipTblOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 36)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: ipxRipTblOverflow.setStatus('current')
ipxSapTblOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 37)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: ipxSapTblOverflow.setStatus('current')
facsAccessVoilation = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 49)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: facsAccessVoilation.setStatus('current')
autoConfigurationCompleted = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 50)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: autoConfigurationCompleted.setStatus('current')
forwardingTabOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 51)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: forwardingTabOverflow.setStatus('current')
framRelaySwitchConnectionUp = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 53)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: framRelaySwitchConnectionUp.setStatus('current')
framRelaySwitchConnectionDown = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 54)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: framRelaySwitchConnectionDown.setStatus('current')
errorsDuringInit = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 61)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: errorsDuringInit.setStatus('current')
vlanDynPortAdded = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 66)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynPortAdded.setStatus('current')
vlanDynPortRemoved = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 67)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynPortRemoved.setStatus('current')
rsSDclientsTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 68)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsSDclientsTableOverflow.setStatus('current')
rsSDinactiveServer = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 69)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsSDinactiveServer.setStatus('current')
rsIpZhrConnectionsTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 70)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrConnectionsTableOverflow.setStatus('current')
rsIpZhrReqStaticConnNotAccepted = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 71)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrReqStaticConnNotAccepted.setStatus('current')
rsIpZhrVirtualIpAsSource = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 72)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrVirtualIpAsSource.setStatus('current')
rsIpZhrNotAllocVirtualIp = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 73)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsIpZhrNotAllocVirtualIp.setStatus('current')
rsSnmpSetRequestInSpecialCfgState = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 74)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsSnmpSetRequestInSpecialCfgState.setStatus('current')
rsPingCompletion = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 136)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsPingCompletion.setStatus('current')
pppSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 137)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: pppSecurityViolation.setStatus('current')
frDLCIStatudChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 138)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: frDLCIStatudChange.setStatus('current')
papFailedCommunication = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 139)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: papFailedCommunication.setStatus('current')
chapFailedCommunication = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 140)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: chapFailedCommunication.setStatus('current')
rsWSDRedundancySwitch = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 141)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsWSDRedundancySwitch.setStatus('current')
rsDhcpAllocationFailure = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 142)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rsDhcpAllocationFailure.setStatus('current')
rlIpFftStnOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 145)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpFftStnOverflow.setStatus('current')
rlIpFftSubOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 146)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpFftSubOverflow.setStatus('current')
rlIpxFftStnOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 147)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpxFftStnOverflow.setStatus('current')
rlIpxFftSubOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 148)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpxFftSubOverflow.setStatus('current')
rlIpmFftOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 149)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIpmFftOverflow.setStatus('current')
rlPhysicalDescriptionChanged = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 150)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlPhysicalDescriptionChanged.setStatus('current')
rldot1dStpPortStateForwarding = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 151)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("DLINK-3100-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"), ("DLINK-3100-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
if mibBuilder.loadTexts: rldot1dStpPortStateForwarding.setStatus('current')
rldot1dStpPortStateNotForwarding = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 152)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("DLINK-3100-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"), ("DLINK-3100-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
if mibBuilder.loadTexts: rldot1dStpPortStateNotForwarding.setStatus('current')
rlPolicyDropPacketTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 153)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlPolicyDropPacketTrap.setStatus('current')
rlPolicyForwardPacketTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 154)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlPolicyForwardPacketTrap.setStatus('current')
rlIgmpProxyTableOverflow = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 156)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIgmpProxyTableOverflow.setStatus('current')
rlIgmpV1MsgReceived = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 157)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlIgmpV1MsgReceived.setStatus('current')
rlVrrpEntriesDeleted = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 158)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlVrrpEntriesDeleted.setStatus('current')
rlHotSwapTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 159)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlHotSwapTrap.setStatus('current')
rlTrunkPortAddedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 160)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlTrunkPortAddedTrap.setStatus('current')
rlTrunkPortRemovedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 161)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlTrunkPortRemovedTrap.setStatus('current')
rlTrunkPortNotCapableTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 162)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlTrunkPortNotCapableTrap.setStatus('current')
rlLockPortTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 170)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlLockPortTrap.setStatus('current')
vlanDynVlanAdded = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 171)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynVlanAdded.setStatus('current')
vlanDynVlanRemoved = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 172)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynVlanRemoved.setStatus('current')
vlanDynamicToStatic = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 173)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanDynamicToStatic.setStatus('current')
vlanStaticToDynamic = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 174)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: vlanStaticToDynamic.setStatus('current')
dstrSysLog = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 175)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: dstrSysLog.setStatus('current')
rlEnvMonFanStateChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 176)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEnvMonFanStateChange.setStatus('current')
rlEnvMonPowerSupplyStateChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 177)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEnvMonPowerSupplyStateChange.setStatus('current')
rlStackStateChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 178)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackStateChange.setStatus('current')
rlEnvMonTemperatureRisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 179)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlEnvMonTemperatureRisingAlarm.setStatus('current')
rlBrgMacAddFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 183)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlBrgMacAddFailedTrap.setStatus('current')
rldot1xPortStatusAuthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 184)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xPortStatusAuthorizedTrap.setStatus('current')
rldot1xPortStatusUnauthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 185)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xPortStatusUnauthorizedTrap.setStatus('current')
swIfTablePortLock = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 192)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: swIfTablePortLock.setStatus('current')
swIfTablePortUnLock = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 193)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: swIfTablePortUnLock.setStatus('current')
rlAAAUserLocked = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 194)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlAAAUserLocked.setStatus('current')
bpduGuardPortSuspended = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 202)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: bpduGuardPortSuspended.setStatus('current')
rldot1xSupplicantMacAuthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 203)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xSupplicantMacAuthorizedTrap.setStatus('current')
rldot1xSupplicantMacUnauthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 204)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rldot1xSupplicantMacUnauthorizedTrap.setStatus('current')
stpLoopbackDetection = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 205)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: stpLoopbackDetection.setStatus('current')
stpLoopbackDetectionResolved = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 206)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: stpLoopbackDetectionResolved.setStatus('current')
loopbackDetectionPortSuspended = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 207)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: loopbackDetectionPortSuspended.setStatus('current')
rlSwStormControlSuspend = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 0, 213)).setObjects(("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorDesc"), ("DLINK-3100-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlSwStormControlSuspend.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-TRAPS-MIB", resetRequired=resetRequired, rldot1xPortStatusUnauthorizedTrap=rldot1xPortStatusUnauthorizedTrap, loopbackDetectionPortSuspended=loopbackDetectionPortSuspended, endTftp=endTftp, ipxRipTblOverflow=ipxRipTblOverflow, rxOverflowHWFault=rxOverflowHWFault, txOverflowHWFault=txOverflowHWFault, vlanDynPortRemoved=vlanDynPortRemoved, vlanDynVlanRemoved=vlanDynVlanRemoved, rldot1dStpPortStateNotForwarding=rldot1dStpPortStateNotForwarding, vlanDynamicToStatic=vlanDynamicToStatic, rlIgmpV1MsgReceived=rlIgmpV1MsgReceived, rlSwStormControlSuspend=rlSwStormControlSuspend, vlanDynVlanAdded=vlanDynVlanAdded, forwardingTabOverflow=forwardingTabOverflow, rlBrgMacAddFailedTrap=rlBrgMacAddFailedTrap, bpduGuardPortSuspended=bpduGuardPortSuspended, papFailedCommunication=papFailedCommunication, rlIpFftStnOverflow=rlIpFftStnOverflow, rlLockPortTrap=rlLockPortTrap, stpLoopbackDetectionResolved=stpLoopbackDetectionResolved, swIfTablePortUnLock=swIfTablePortUnLock, rsDhcpAllocationFailure=rsDhcpAllocationFailure, stpLoopbackDetection=stpLoopbackDetection, rlTrunkPortAddedTrap=rlTrunkPortAddedTrap, rlEnvMonFanStateChange=rlEnvMonFanStateChange, rsIpZhrReqStaticConnNotAccepted=rsIpZhrReqStaticConnNotAccepted, rsSDinactiveServer=rsSDinactiveServer, rlPolicyDropPacketTrap=rlPolicyDropPacketTrap, rldot1xSupplicantMacUnauthorizedTrap=rldot1xSupplicantMacUnauthorizedTrap, rsWSDRedundancySwitch=rsWSDRedundancySwitch, ipxSapTblOverflow=ipxSapTblOverflow, vlanDynPortAdded=vlanDynPortAdded, rldot1xSupplicantMacAuthorizedTrap=rldot1xSupplicantMacAuthorizedTrap, rsPingCompletion=rsPingCompletion, rlStackStateChange=rlStackStateChange, rlIgmpProxyTableOverflow=rlIgmpProxyTableOverflow, vlanStaticToDynamic=vlanStaticToDynamic, autoConfigurationCompleted=autoConfigurationCompleted, framRelaySwitchConnectionDown=framRelaySwitchConnectionDown, rlIpxFftStnOverflow=rlIpxFftStnOverflow, rlTrunkPortNotCapableTrap=rlTrunkPortNotCapableTrap, dstrSysLog=dstrSysLog, swIfTablePortLock=swIfTablePortLock, rlIpmFftOverflow=rlIpmFftOverflow, rlPhysicalDescriptionChanged=rlPhysicalDescriptionChanged, framRelaySwitchConnectionUp=framRelaySwitchConnectionUp, rlIpxFftSubOverflow=rlIpxFftSubOverflow, facsAccessVoilation=facsAccessVoilation, startTftp=startTftp, rlHotSwapTrap=rlHotSwapTrap, frDLCIStatudChange=frDLCIStatudChange, routeTableOverflow=routeTableOverflow, rsIpZhrVirtualIpAsSource=rsIpZhrVirtualIpAsSource, rsSDclientsTableOverflow=rsSDclientsTableOverflow, errorsDuringInit=errorsDuringInit, abortTftp=abortTftp, mainLinkUp=mainLinkUp, rsSnmpSetRequestInSpecialCfgState=rsSnmpSetRequestInSpecialCfgState, rsIpZhrConnectionsTableOverflow=rsIpZhrConnectionsTableOverflow, rlVrrpEntriesDeleted=rlVrrpEntriesDeleted, faultBackUp=faultBackUp, rlEnvMonTemperatureRisingAlarm=rlEnvMonTemperatureRisingAlarm, rlEnvMonPowerSupplyStateChange=rlEnvMonPowerSupplyStateChange, rsIpZhrNotAllocVirtualIp=rsIpZhrNotAllocVirtualIp, rldot1dStpPortStateForwarding=rldot1dStpPortStateForwarding, rlPolicyForwardPacketTrap=rlPolicyForwardPacketTrap, rlTrunkPortRemovedTrap=rlTrunkPortRemovedTrap, chapFailedCommunication=chapFailedCommunication, rlAAAUserLocked=rlAAAUserLocked, pppSecurityViolation=pppSecurityViolation, rldot1xPortStatusAuthorizedTrap=rldot1xPortStatusAuthorizedTrap, rlIpFftSubOverflow=rlIpFftSubOverflow)
