#
# PySNMP MIB module REDSTONE-IP-TEMPLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-IP-TEMPLATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
RsEnable, RsName = mibBuilder.importSymbols("REDSTONE-TC", "RsEnable", "RsName")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Counter64, MibIdentifier, IpAddress, Integer32, iso, Unsigned32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "MibIdentifier", "IpAddress", "Integer32", "iso", "Unsigned32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Gauge32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rsIpTemplateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 26))
rsIpTemplateMIB.setRevisions(('1999-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsIpTemplateMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: rsIpTemplateMIB.setLastUpdated('9908250000Z')
if mibBuilder.loadTexts: rsIpTemplateMIB.setOrganization('Redstone Communications Inc.')
if mibBuilder.loadTexts: rsIpTemplateMIB.setContactInfo(' Redstone Communications, Inc. 5 Carlisle Road Westford MA 01886 USA Tel: +1-978-692-1999 Email: mib@redstonecom.com ')
if mibBuilder.loadTexts: rsIpTemplateMIB.setDescription('The IP Template MIB for the Redstone Communications Inc. enterprise.')
rsIpTemplateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1))
rsIpTemplate = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1))
rsIpTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1), )
if mibBuilder.loadTexts: rsIpTemplateTable.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateTable.setDescription('The entries in this table describe templates for configuring IP interfaces.')
rsIpTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1), ).setIndexNames((0, "REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateId"))
if mibBuilder.loadTexts: rsIpTemplateEntry.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateEntry.setDescription('A template describing configuration of an IP interface.')
rsIpTemplateId = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rsIpTemplateId.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateId.setDescription('The integer identifier associated with this template. A value for this identifier is determined by locating or creating a template name in the rsTemplateNameTable.')
rsIpTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateRowStatus.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateRowStatus.setDescription("Controls creation/deletion of entries in this table. Only the values 'createAndGo' and 'destroy' may be SET. The value of rsIpTemplateId must match that of a template name configured in rsTemplateNameTable.")
rsIpTemplateRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 3), RsName().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateRouterName.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateRouterName.setDescription('The virtual router to which an IP interface configured by this template will be assigned, if other mechanisms do not otherwise specify a virtual router assignment.')
rsIpTemplateIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateIpAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateIpAddr.setDescription('An IP address to be used by an IP interface configured by this template. This object will have a value of 0.0.0.0 for an unnumbered interface.')
rsIpTemplateIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateIpMask.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateIpMask.setDescription('An IP address mask to be used by an IP interface configured by this template. This object will have a value of 0.0.0.0 for an unnumbered interface.')
rsIpTemplateDirectedBcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 6), RsEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateDirectedBcastEnable.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateDirectedBcastEnable.setDescription('Enable/disable forwarding of directed broadcasts on this IP network interface.')
rsIpTemplateIcmpRedirectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 7), RsEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateIcmpRedirectEnable.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateIcmpRedirectEnable.setDescription('Enable/disable transmission of ICMP Redirect messages on this IP network interface.')
rsIpTemplateAccessRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 8), RsEnable().clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateAccessRoute.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateAccessRoute.setDescription('Enable/disable whether a host route is automatically created for a remote host attached to an IP interface that is configured using this template.')
rsIpTemplateMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(512, 10240), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateMtu.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateMtu.setDescription('The configured MTU size for this IP network interface. If set to zero, the default MTU size, as determined by the underlying network media, is used.')
rsIpTemplateLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpTemplateLoopbackIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateLoopbackIfIndex.setDescription('For unnumbered interfaces, the IfIndex of the IP loopback interface whose IP address is used as the source address for transmitted IP packets. A value of zero means the loopback interface is unspecified (e.g., when the interface is numbered).')
rsIpTemplateMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 26, 4))
rsIpTemplateMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 1))
rsIpTemplateMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 2))
rsIpTemplateCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 1, 1)).setObjects(("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIpTemplateCompliance = rsIpTemplateCompliance.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateCompliance.setDescription('The compliance statement for systems supporting IP configuration templates.')
rsIpTemplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 2, 1)).setObjects(("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateRowStatus"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateRouterName"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateIpAddr"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateIpMask"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateDirectedBcastEnable"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateIcmpRedirectEnable"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateAccessRoute"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateMtu"), ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateLoopbackIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIpTemplateGroup = rsIpTemplateGroup.setStatus('current')
if mibBuilder.loadTexts: rsIpTemplateGroup.setDescription('The basic collection of objects providing management of IP Template functionality in a Redstone product.')
mibBuilder.exportSymbols("REDSTONE-IP-TEMPLATE-MIB", PYSNMP_MODULE_ID=rsIpTemplateMIB, rsIpTemplateIpMask=rsIpTemplateIpMask, rsIpTemplateGroup=rsIpTemplateGroup, rsIpTemplateDirectedBcastEnable=rsIpTemplateDirectedBcastEnable, rsIpTemplateMIB=rsIpTemplateMIB, rsIpTemplateTable=rsIpTemplateTable, rsIpTemplateAccessRoute=rsIpTemplateAccessRoute, rsIpTemplateId=rsIpTemplateId, rsIpTemplateCompliance=rsIpTemplateCompliance, rsIpTemplateIpAddr=rsIpTemplateIpAddr, rsIpTemplateLoopbackIfIndex=rsIpTemplateLoopbackIfIndex, rsIpTemplate=rsIpTemplate, rsIpTemplateRouterName=rsIpTemplateRouterName, rsIpTemplateIcmpRedirectEnable=rsIpTemplateIcmpRedirectEnable, rsIpTemplateMIBCompliances=rsIpTemplateMIBCompliances, rsIpTemplateEntry=rsIpTemplateEntry, rsIpTemplateObjects=rsIpTemplateObjects, rsIpTemplateRowStatus=rsIpTemplateRowStatus, rsIpTemplateMIBConformance=rsIpTemplateMIBConformance, rsIpTemplateMIBGroups=rsIpTemplateMIBGroups, rsIpTemplateMtu=rsIpTemplateMtu)
