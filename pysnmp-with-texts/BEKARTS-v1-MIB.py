#
# PySNMP MIB module BEKARTS-v1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BEKARTS-v1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:37:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Gauge32, NotificationType, enterprises, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, IpAddress, Counter32, TimeTicks, Counter64, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Gauge32", "NotificationType", "enterprises", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "IpAddress", "Counter32", "TimeTicks", "Counter64", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bekarts = MibIdentifier((1, 3, 6, 1, 4, 1, 18514))
bekarts_software = MibIdentifier((1, 3, 6, 1, 4, 1, 18514, 20)).setLabel("bekarts-software")
bekarts_hardware = MibIdentifier((1, 3, 6, 1, 4, 1, 18514, 100)).setLabel("bekarts-hardware")
bekarts_mailshappy = MibIdentifier((1, 3, 6, 1, 4, 1, 18514, 20, 1)).setLabel("bekarts-mailshappy")
bekarts_mailshappy_on = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,1)).setLabel("bekarts-mailshappy-on")
if mibBuilder.loadTexts: bekarts_mailshappy_on.setDescription('BekArts Mails Happy has been started up.')
if mibBuilder.loadTexts: bekarts_mailshappy_on.setReference('BekArts On Trap')
bekarts_mailshappy_off = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,2)).setLabel("bekarts-mailshappy-off")
if mibBuilder.loadTexts: bekarts_mailshappy_off.setDescription('BekArts Mails Happy has been shut down.')
if mibBuilder.loadTexts: bekarts_mailshappy_off.setReference('BekArts Off Trap')
bekarts_mailshappy_active = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,3)).setLabel("bekarts-mailshappy-active")
if mibBuilder.loadTexts: bekarts_mailshappy_active.setDescription('BekArts Mails Happy has been Activated.')
if mibBuilder.loadTexts: bekarts_mailshappy_active.setReference('BekArts Active Trap')
bekarts_mailshappy_deactive = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,4)).setLabel("bekarts-mailshappy-deactive")
if mibBuilder.loadTexts: bekarts_mailshappy_deactive.setDescription('BekArts Mails Happy has been De-Activated.')
if mibBuilder.loadTexts: bekarts_mailshappy_deactive.setReference('BekArts De-Activated Trap')
bekarts_mailshappy_warning = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,5)).setLabel("bekarts-mailshappy-warning")
if mibBuilder.loadTexts: bekarts_mailshappy_warning.setDescription('BekArts Mails Happy has reached a warning state.')
if mibBuilder.loadTexts: bekarts_mailshappy_warning.setReference('BekArts Warning Trap')
bekarts_mailshappy_clear_warning = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,6)).setLabel("bekarts-mailshappy-clear-warning")
if mibBuilder.loadTexts: bekarts_mailshappy_clear_warning.setDescription('BekArts Mails Happy has cleared a warning state.')
if mibBuilder.loadTexts: bekarts_mailshappy_clear_warning.setReference('BekArts Warning Cleared Trap')
bekarts_mailshappy_critical = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,7)).setLabel("bekarts-mailshappy-critical")
if mibBuilder.loadTexts: bekarts_mailshappy_critical.setDescription('BekArts Mails Happy has reached a critical state.')
if mibBuilder.loadTexts: bekarts_mailshappy_critical.setReference('BekArts Critical Trap')
bekarts_mailshappy_clear_critical = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,8)).setLabel("bekarts-mailshappy-clear-critical")
if mibBuilder.loadTexts: bekarts_mailshappy_clear_critical.setDescription('BekArts Mails Happy has cleared a critical state.')
if mibBuilder.loadTexts: bekarts_mailshappy_clear_critical.setReference('BekArts Critical Cleared Trap')
bekarts_mailshappy_test = NotificationType((1, 3, 6, 1, 4, 1, 18514, 20, 1) + (0,9)).setLabel("bekarts-mailshappy-test")
if mibBuilder.loadTexts: bekarts_mailshappy_test.setDescription('BekArts Mails Happy has sent a test trap.')
if mibBuilder.loadTexts: bekarts_mailshappy_test.setReference('BekArts Test Trap')
mibBuilder.exportSymbols("BEKARTS-v1-MIB", bekarts_mailshappy=bekarts_mailshappy, bekarts_mailshappy_off=bekarts_mailshappy_off, bekarts_hardware=bekarts_hardware, bekarts=bekarts, bekarts_mailshappy_deactive=bekarts_mailshappy_deactive, bekarts_mailshappy_active=bekarts_mailshappy_active, bekarts_mailshappy_warning=bekarts_mailshappy_warning, bekarts_mailshappy_clear_warning=bekarts_mailshappy_clear_warning, bekarts_mailshappy_on=bekarts_mailshappy_on, bekarts_software=bekarts_software, bekarts_mailshappy_clear_critical=bekarts_mailshappy_clear_critical, bekarts_mailshappy_test=bekarts_mailshappy_test, bekarts_mailshappy_critical=bekarts_mailshappy_critical)
