#
# PySNMP MIB module UAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:28:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, enterprises, IpAddress, Integer32, iso, Unsigned32, Bits, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, TimeTicks, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "IpAddress", "Integer32", "iso", "Unsigned32", "Bits", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "TimeTicks", "Gauge32", "Counter64")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
zxUasMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1006, 1))
if mibBuilder.loadTexts: zxUasMib.setLastUpdated('200503081500Z')
if mibBuilder.loadTexts: zxUasMib.setOrganization('ZTE Co.')
if mibBuilder.loadTexts: zxUasMib.setContactInfo('')
if mibBuilder.loadTexts: zxUasMib.setDescription('This mib defines management information objects for uas')
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxUas = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1006))
zxUasMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1))
zxUasTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 2))
zxUasSystemGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 1))
zxUasServiceMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2))
zxUasStaticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3))
zxUasPppStatics = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1))
zxUasInterfaceIPPoolTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1), )
if mibBuilder.loadTexts: zxUasInterfaceIPPoolTable.setStatus('current')
if mibBuilder.loadTexts: zxUasInterfaceIPPoolTable.setDescription('This table contains IP Pool entry')
zxUasInterfaceIPPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1), ).setIndexNames((0, "UAS-MIB", "zxUasIPPoolName"), (0, "UAS-MIB", "zxUasIPPoolVirtualRouteField"), (0, "UAS-MIB", "zxUasIPPoolInterfaceName"), (0, "UAS-MIB", "zxUasIPPoolID"), (0, "UAS-MIB", "zxUasIPPoolStartIPAddr"), (0, "UAS-MIB", "zxUasIPPoolEndIPAddr"))
if mibBuilder.loadTexts: zxUasInterfaceIPPoolEntry.setStatus('current')
if mibBuilder.loadTexts: zxUasInterfaceIPPoolEntry.setDescription('This list contains IP Pool parameters and is indexed by zxUasIPPoolName')
zxUasIPPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolName.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolName.setDescription('IP Pool name.')
zxUasIPPoolVirtualRouteField = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolVirtualRouteField.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolVirtualRouteField.setDescription('IP pool virtual route field name.')
zxUasIPPoolInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolInterfaceName.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolInterfaceName.setDescription('VBUI global port.')
zxUasIPPoolID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolID.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolID.setDescription('IP Pool ID.')
zxUasIPPoolStartIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolStartIPAddr.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolStartIPAddr.setDescription('start IP address.')
zxUasIPPoolEndIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolEndIPAddr.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolEndIPAddr.setDescription('end IP Address.')
zxUasIPPoolFreeIPNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolFreeIPNum.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolFreeIPNum.setDescription('free IP Num.')
zxUasIPPoolUsedIPNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolUsedIPNum.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolUsedIPNum.setDescription('used IP Num.')
zxUasIPPoolUnavailableIPNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolUnavailableIPNum.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolUnavailableIPNum.setDescription('unavailable IP Num.')
zxUasIPPoolBindToDomainFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unreserved", 1), ("reserved", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasIPPoolBindToDomainFlag.setStatus('current')
if mibBuilder.loadTexts: zxUasIPPoolBindToDomainFlag.setDescription('this flag is used for binding to domain.')
zxUasActiveSubscriberTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2), )
if mibBuilder.loadTexts: zxUasActiveSubscriberTable.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberTable.setDescription('This table contains active subscriber entry')
zxUasActiveSubscriberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1), ).setIndexNames((0, "UAS-MIB", "zxUasActiveSubscriberVirtualRouteField"), (0, "UAS-MIB", "zxUasActiveSubscriberIPAddr"), (0, "UAS-MIB", "zxUasActiveSubscriberType"), (0, "UAS-MIB", "zxUasActiveSubscriberPPPID"))
if mibBuilder.loadTexts: zxUasActiveSubscriberEntry.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberEntry.setDescription('This list contains active subscriber parameters and is indexed by zxUasActiveSubscriberIndex ')
zxUasActiveSubscriberVirtualRouteField = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberVirtualRouteField.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberVirtualRouteField.setDescription('active subscriber virtual route field name.')
zxUasActiveSubscriberIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberIPAddr.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberIPAddr.setDescription('active subscriber IP address.')
zxUasActiveSubscriberType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ppp", 1), ("ipdhcp", 2), ("remotedhcp", 3), ("ipdhcprelay", 4), ("iphost", 5), ("remotehost", 6), ("vpn", 7), ("brg", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberType.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberType.setDescription('active subscriber type.')
zxUasActiveSubscriberPPPID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberPPPID.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberPPPID.setDescription('PPP active subscriber ID.')
zxUasActiveSubscriberName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberName.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberName.setDescription('active subscriber name.')
zxUasActiveSubscriberInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberInterfaceName.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberInterfaceName.setDescription('active subscriber VBUI global port.')
zxUasActiveSubscriberDoaminID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberDoaminID.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberDoaminID.setDescription('active subscriber domain ID.')
zxUasActiveSubscriberSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberSlot.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberSlot.setDescription('active subscriber slot.')
zxUasActiveSubscriberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberPort.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberPort.setDescription('active subscriber port.')
zxUasActiveSubscriberVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberVlanId.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberVlanId.setDescription('active subscriber VlanId.')
zxUasActiveSubscriberVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberVpi.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberVpi.setDescription('active subscriber vpi value.')
zxUasActiveSubscriberVci = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberVci.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberVci.setDescription('active subscriber vci value.')
zxUasActiveSubscriberMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 13), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberMACAddr.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberMACAddr.setDescription('active subscriber host MAC address.')
zxUasActiveSubscriberUpOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberUpOctets.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberUpOctets.setDescription('active subscriber up flow.')
zxUasActiveSubscriberUpGigaOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberUpGigaOctets.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberUpGigaOctets.setDescription('active subscriber up flow extend.')
zxUasActiveSubscriberDownOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberDownOctets.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberDownOctets.setDescription('active subscriber down flow.')
zxUasActiveSubscriberDownGigaOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberDownGigaOctets.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberDownGigaOctets.setDescription('active subscriber down flow extend.')
zxUasActiveDhcpSubscriberAuthFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveDhcpSubscriberAuthFlag.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveDhcpSubscriberAuthFlag.setDescription('DHCP subscriber authentication status.')
zxUasActiveSubscriberUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 19), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberUpTime.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberUpTime.setDescription('active subscriber create time.')
zxUasTail = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("true", 1), ("false", 0))))
if mibBuilder.loadTexts: zxUasTail.setStatus('current')
if mibBuilder.loadTexts: zxUasTail.setDescription(' null node')
zxUasPppCallCount = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasPppCallCount.setStatus('current')
if mibBuilder.loadTexts: zxUasPppCallCount.setDescription('ppp calling counts.')
zxUasPppCallFailedCount = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasPppCallFailedCount.setStatus('current')
if mibBuilder.loadTexts: zxUasPppCallFailedCount.setDescription('ppp calling failed counts.')
zxUasPppLinkBreakFailedCount = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasPppLinkBreakFailedCount.setStatus('current')
if mibBuilder.loadTexts: zxUasPppLinkBreakFailedCount.setDescription('ppp linkbreak failed counts.')
zxUasPppAbnormalCloseCount = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasPppAbnormalCloseCount.setStatus('current')
if mibBuilder.loadTexts: zxUasPppAbnormalCloseCount.setDescription('abnormal close counts.')
zxUasActiveSubscriberStaticsTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 2), )
if mibBuilder.loadTexts: zxUasActiveSubscriberStaticsTable.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberStaticsTable.setDescription('This table contains active subscriber statics Entry')
zxUasActiveSubscriberStaticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 2, 1), ).setIndexNames((0, "UAS-MIB", "zxUasActiveSubscriberType"))
if mibBuilder.loadTexts: zxUasActiveSubscriberStaticsEntry.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberStaticsEntry.setDescription('This list contains active subscriber statics parameters and is indexed by zxUasActiveSubscriberType')
zxUasActiveSubscriberNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasActiveSubscriberNum.setStatus('current')
if mibBuilder.loadTexts: zxUasActiveSubscriberNum.setDescription('ppp users num,iphost users num,dhcp users num and vpn users num.')
zxUasMaxSubscriberOnlineCount = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasMaxSubscriberOnlineCount.setStatus('current')
if mibBuilder.loadTexts: zxUasMaxSubscriberOnlineCount.setDescription('The subscriber peak online in the history')
zxUasMaxSubscriberOnlineClear = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxUasMaxSubscriberOnlineClear.setStatus('current')
if mibBuilder.loadTexts: zxUasMaxSubscriberOnlineClear.setDescription('Clear subscriber peak online in the history')
zxUasMaxSubscriberOnlineTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxUasMaxSubscriberOnlineTime.setStatus('current')
if mibBuilder.loadTexts: zxUasMaxSubscriberOnlineTime.setDescription('The time which the max subscriber occured.')
mibBuilder.exportSymbols("UAS-MIB", zxUasActiveSubscriberNum=zxUasActiveSubscriberNum, zxUasMibObjects=zxUasMibObjects, zxUasIPPoolUnavailableIPNum=zxUasIPPoolUnavailableIPNum, zxUas=zxUas, zxUasActiveSubscriberName=zxUasActiveSubscriberName, zxUasActiveSubscriberStaticsTable=zxUasActiveSubscriberStaticsTable, zxUasActiveSubscriberUpOctets=zxUasActiveSubscriberUpOctets, zxUasActiveSubscriberVpi=zxUasActiveSubscriberVpi, zxUasPppCallCount=zxUasPppCallCount, zxUasActiveSubscriberVirtualRouteField=zxUasActiveSubscriberVirtualRouteField, zxUasSystemGroup=zxUasSystemGroup, zxUasMaxSubscriberOnlineClear=zxUasMaxSubscriberOnlineClear, zxUasActiveSubscriberEntry=zxUasActiveSubscriberEntry, zxUasActiveSubscriberIPAddr=zxUasActiveSubscriberIPAddr, zxUasServiceMgmtGroup=zxUasServiceMgmtGroup, zxUasActiveSubscriberPPPID=zxUasActiveSubscriberPPPID, zxUasActiveSubscriberDoaminID=zxUasActiveSubscriberDoaminID, zxUasInterfaceIPPoolTable=zxUasInterfaceIPPoolTable, zxUasActiveSubscriberTable=zxUasActiveSubscriberTable, zxUasIPPoolVirtualRouteField=zxUasIPPoolVirtualRouteField, zxUasActiveSubscriberInterfaceName=zxUasActiveSubscriberInterfaceName, zte=zte, zxUasIPPoolInterfaceName=zxUasIPPoolInterfaceName, zxUasActiveSubscriberVlanId=zxUasActiveSubscriberVlanId, PYSNMP_MODULE_ID=zxUasMib, zxUasActiveDhcpSubscriberAuthFlag=zxUasActiveDhcpSubscriberAuthFlag, zxUasActiveSubscriberSlot=zxUasActiveSubscriberSlot, zxUasMaxSubscriberOnlineCount=zxUasMaxSubscriberOnlineCount, zxUasActiveSubscriberUpTime=zxUasActiveSubscriberUpTime, zxUasPppAbnormalCloseCount=zxUasPppAbnormalCloseCount, zxUasActiveSubscriberMACAddr=zxUasActiveSubscriberMACAddr, zxUasIPPoolID=zxUasIPPoolID, zxUasActiveSubscriberPort=zxUasActiveSubscriberPort, zxUasStaticsGroup=zxUasStaticsGroup, zxUasActiveSubscriberUpGigaOctets=zxUasActiveSubscriberUpGigaOctets, zxUasMaxSubscriberOnlineTime=zxUasMaxSubscriberOnlineTime, zxUasActiveSubscriberType=zxUasActiveSubscriberType, zxUasMib=zxUasMib, zxUasTraps=zxUasTraps, zxUasInterfaceIPPoolEntry=zxUasInterfaceIPPoolEntry, zxUasIPPoolName=zxUasIPPoolName, zxUasIPPoolEndIPAddr=zxUasIPPoolEndIPAddr, zxUasActiveSubscriberVci=zxUasActiveSubscriberVci, zxUasActiveSubscriberDownOctets=zxUasActiveSubscriberDownOctets, zxUasIPPoolStartIPAddr=zxUasIPPoolStartIPAddr, zxUasActiveSubscriberDownGigaOctets=zxUasActiveSubscriberDownGigaOctets, zxUasIPPoolBindToDomainFlag=zxUasIPPoolBindToDomainFlag, zxUasPppCallFailedCount=zxUasPppCallFailedCount, zxUasPppLinkBreakFailedCount=zxUasPppLinkBreakFailedCount, zxUasActiveSubscriberStaticsEntry=zxUasActiveSubscriberStaticsEntry, zxUasIPPoolUsedIPNum=zxUasIPPoolUsedIPNum, zxUasIPPoolFreeIPNum=zxUasIPPoolFreeIPNum, zxUasPppStatics=zxUasPppStatics, zxUasTail=zxUasTail)
