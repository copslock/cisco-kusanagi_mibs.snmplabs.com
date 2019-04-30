#
# PySNMP MIB module T3510-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T3510-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:07:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, ObjectIdentity, Gauge32, IpAddress, Counter64, Counter32, enterprises, Integer32, Bits, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Gauge32", "IpAddress", "Counter64", "Counter32", "enterprises", "Integer32", "Bits", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
t3510 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2))
readings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2))
readingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3))
settingsint = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6))
temperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('mandatory')
humidity = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidity.setStatus('mandatory')
computedValue = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: computedValue.setStatus('mandatory')
templow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: templow.setStatus('mandatory')
temphigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temphigh.setStatus('mandatory')
humiditylow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humiditylow.setStatus('mandatory')
humidityhigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityhigh.setStatus('mandatory')
cvlow = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlow.setStatus('mandatory')
cvhigh = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvhigh.setStatus('mandatory')
temptime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temptime.setStatus('mandatory')
humidityTime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityTime.setStatus('mandatory')
cvTime = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvTime.setStatus('mandatory')
tempHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHyst.setStatus('mandatory')
humidityHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityHyst.setStatus('mandatory')
cvHyst = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHyst.setStatus('mandatory')
temperaturei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperaturei.setStatus('mandatory')
humidityi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humidityi.setStatus('mandatory')
cvi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvi.setStatus('mandatory')
templowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: templowi.setStatus('mandatory')
temphighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temphighi.setStatus('mandatory')
humiditylowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humiditylowi.setStatus('mandatory')
humidityhighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityhighi.setStatus('mandatory')
cvlowi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvlowi.setStatus('mandatory')
cvhighi = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvhighi.setStatus('mandatory')
temptimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: temptimei.setStatus('mandatory')
humidityTimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityTimei.setStatus('mandatory')
cvTimei = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTimei.setStatus('mandatory')
tempHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tempHysti.setStatus('mandatory')
humidityHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: humidityHysti.setStatus('mandatory')
cvHysti = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2000, 6000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvHysti.setStatus('mandatory')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
alarmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTemperature.setStatus('mandatory')
alarmhumidity = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmhumidity.setStatus('mandatory')
alarmCv = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCv.setStatus('mandatory')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1), ).setIndexNames((0, "T3510-MIB", "histtemperature"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
histtemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histtemperature.setStatus('mandatory')
histhumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histhumidity.setStatus('mandatory')
histcomputedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histcomputedValue.setStatus('mandatory')
mibBuilder.exportSymbols("T3510-MIB", cvlow=cvlow, readingsint=readingsint, settings=settings, histcomputedValue=histcomputedValue, humidityhigh=humidityhigh, readings=readings, humidityi=humidityi, cvHyst=cvHyst, humidityTimei=humidityTimei, temphighi=temphighi, humidityhighi=humidityhighi, alarmhumidity=alarmhumidity, cvTime=cvTime, traps=traps, templowi=templowi, templow=templow, humidityTime=humidityTime, humidityHysti=humidityHysti, comet=comet, alarmTemperature=alarmTemperature, temperature=temperature, humiditylow=humiditylow, messageString=messageString, products=products, histtemperature=histtemperature, humidity=humidity, tempHysti=tempHysti, cvhigh=cvhigh, cvhighi=cvhighi, computedValue=computedValue, cvi=cvi, cvlowi=cvlowi, alarmCv=alarmCv, cvTimei=cvTimei, tempHyst=tempHyst, temperaturei=temperaturei, historyEntry=historyEntry, t3510=t3510, cvHysti=cvHysti, historyTable=historyTable, settingsint=settingsint, temptime=temptime, humiditylowi=humiditylowi, tables=tables, temphigh=temphigh, histhumidity=histhumidity, temptimei=temptimei, humidityHyst=humidityHyst, DisplayString=DisplayString)