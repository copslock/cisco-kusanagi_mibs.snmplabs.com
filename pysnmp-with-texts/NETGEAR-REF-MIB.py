#
# PySNMP MIB module NETGEAR-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETGEAR-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:19:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, iso, MibIdentifier, IpAddress, Integer32, Counter32, Unsigned32, Gauge32, ObjectIdentity, Counter64, TimeTicks, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "iso", "MibIdentifier", "IpAddress", "Integer32", "Counter32", "Unsigned32", "Gauge32", "ObjectIdentity", "Counter64", "TimeTicks", "enterprises", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netgear = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526))
netgear.setRevisions(('2005-02-23 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netgear.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: netgear.setLastUpdated('200502231200Z')
if mibBuilder.loadTexts: netgear.setOrganization('Netgear')
if mibBuilder.loadTexts: netgear.setContactInfo('')
if mibBuilder.loadTexts: netgear.setDescription('')
managedSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1))
fsm726s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 1))
fsm750s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 2))
gsm712 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 3))
fsm726 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 4))
gsm712f = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 5))
fsm726v3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 10))
gsm7312 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 6))
gsm7324 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 7))
gsm7224 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 8))
fsm7326p = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 9))
ng7000Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10))
ng700Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 11))
ngrouter = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 12))
ngfirewall = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 13))
ngap = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 14))
ngwlan = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 15))
ng9000chassisswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 16))
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100))
stackswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1))
l2switch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2))
l3switch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3))
smartswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5))
firewall = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 6))
accesspoint = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 7))
wirelessLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 8))
chassisswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 9))
fsm7328s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 1))
fsm7352s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 2))
gsm7328s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 3))
gsm7352s = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 4))
fsm7352sp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 5))
fsm7328sp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 1, 6))
gsm7312v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 1))
gsm7324v2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 2))
xsm7312 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 3))
gsm7324p = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 3, 4))
gsm7248 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2, 1))
gsm7212 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 2, 2))
gcm9600 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 9, 1))
gs748t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 1))
fs726t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 2))
gs716t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 3))
fs750t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 4))
gs724t = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 4, 5))
fvx538 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5, 1))
fvs338 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 5, 2))
fwag114 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 6, 3))
wag302 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 7, 1))
wapc538 = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 100, 8, 1))
class AgentPortMask(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0' When setting this value, the system will ignore configuration for ports not between the first and last valid ports. Configuration of any port numbers between this range that are not valid ports return a failure message, but will still apply configuration for valid ports."
    status = 'current'

mibBuilder.exportSymbols("NETGEAR-REF-MIB", gsm7224=gsm7224, fsm7326p=fsm7326p, router=router, wapc538=wapc538, fsm726=fsm726, smartswitch=smartswitch, chassisswitch=chassisswitch, gs724t=gs724t, fsm750s=fsm750s, gsm712=gsm712, gsm7352s=gsm7352s, gcm9600=gcm9600, productID=productID, xsm7312=xsm7312, fsm7352s=fsm7352s, stackswitch=stackswitch, l2switch=l2switch, ngwlan=ngwlan, ng9000chassisswitch=ng9000chassisswitch, fwag114=fwag114, accesspoint=accesspoint, fsm7328s=fsm7328s, gsm7248=gsm7248, gsm7312=gsm7312, fs750t=fs750t, gsm7324=gsm7324, gsm7312v2=gsm7312v2, firewall=firewall, fsm726s=fsm726s, wirelessLAN=wirelessLAN, netgear=netgear, fsm726v3=fsm726v3, ngap=ngap, gsm7328s=gsm7328s, ng700Switch=ng700Switch, fsm7352sp=fsm7352sp, fvs338=fvs338, l3switch=l3switch, managedSwitch=managedSwitch, gs716t=gs716t, AgentPortMask=AgentPortMask, ngfirewall=ngfirewall, gsm7212=gsm7212, gsm7324v2=gsm7324v2, fs726t=fs726t, fvx538=fvx538, fsm7328sp=fsm7328sp, wag302=wag302, gsm712f=gsm712f, ng7000Switch=ng7000Switch, PYSNMP_MODULE_ID=netgear, ngrouter=ngrouter, gs748t=gs748t, gsm7324p=gsm7324p)
