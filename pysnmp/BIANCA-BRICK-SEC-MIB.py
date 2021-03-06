#
# PySNMP MIB module BIANCA-BRICK-SEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-SEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, TimeTicks, NotificationType, Bits, IpAddress, ModuleIdentity, iso, Gauge32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "TimeTicks", "NotificationType", "Bits", "IpAddress", "ModuleIdentity", "iso", "Gauge32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bintecsec = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 254))
biboAdmAdminCommunity = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmAdminCommunity.setStatus('mandatory')
biboAdmReadCommunity = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmReadCommunity.setStatus('mandatory')
biboAdmWriteCommunity = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmWriteCommunity.setStatus('mandatory')
biboAdmLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 272, 254, 4), )
if mibBuilder.loadTexts: biboAdmLicenseTable.setStatus('mandatory')
biboAdmLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 254, 4, 1), ).setIndexNames((0, "BIANCA-BRICK-SEC-MIB", "biboAdmLicenseKey"))
if mibBuilder.loadTexts: biboAdmLicenseEntry.setStatus('mandatory')
biboAdmLicenseSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLicenseSerialNumber.setStatus('mandatory')
biboAdmLicenseMask = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLicenseMask.setStatus('mandatory')
biboAdmLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLicenseKey.setStatus('mandatory')
biboAdmLicenseState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ok", 1), ("not-ok", 2), ("delete", 3), ("internal-ok", 4), ("internal-erase", 5), ("not-supported", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLicenseState.setStatus('mandatory')
biboAdmLicenseSerialId = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLicenseSerialId.setStatus('mandatory')
biboAdmLicenseHwSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicenseHwSerial.setStatus('mandatory')
biboAdmLicenseLicType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 33, 128, 129, 130, 131, 132))).clone(namedValues=NamedValues(("ip", 1), ("capi", 2), ("bridge", 3), ("x25", 4), ("ipx", 5), ("stac", 6), ("frame-relay", 7), ("tapi", 8), ("ospf", 9), ("extended-lan", 10), ("tunneling", 11), ("taf", 12), ("extended-wan", 13), ("leased-line", 14), ("ipsec", 33), ("ethernet", 128), ("bri", 129), ("g703", 130), ("pri", 131), ("modem", 132)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLicenseLicType.setStatus('mandatory')
biboAdmRadiusSecret = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmRadiusSecret.setStatus('mandatory')
biboAdmHttpPassword = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmHttpPassword.setStatus('mandatory')
biboAdmLoginTable = MibTable((1, 3, 6, 1, 4, 1, 272, 254, 7), )
if mibBuilder.loadTexts: biboAdmLoginTable.setStatus('mandatory')
biboAdmLoginEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 254, 7, 1), ).setIndexNames((0, "BIANCA-BRICK-SEC-MIB", "biboAdmLoginUser"))
if mibBuilder.loadTexts: biboAdmLoginEntry.setStatus('mandatory')
biboAdmLoginUser = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLoginUser.setStatus('mandatory')
biboAdmLoginPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLoginPassword.setStatus('mandatory')
biboAdmLoginCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLoginCommand.setStatus('mandatory')
biboAdmLoginState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("valid", 1), ("delete", 2), ("invalid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLoginState.setStatus('mandatory')
biboAdmPublicKey = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmPublicKey.setStatus('mandatory')
biboAdmPrivateKey = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 11), OctetString())
if mibBuilder.loadTexts: biboAdmPrivateKey.setStatus('mandatory')
biboAdmActMonPassword = MibScalar((1, 3, 6, 1, 4, 1, 272, 254, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmActMonPassword.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-SEC-MIB", biboAdmRadiusSecret=biboAdmRadiusSecret, biboAdmLicenseSerialNumber=biboAdmLicenseSerialNumber, biboAdmLicenseMask=biboAdmLicenseMask, bintec=bintec, biboAdmLoginState=biboAdmLoginState, private=private, org=org, biboAdmReadCommunity=biboAdmReadCommunity, biboAdmLicenseLicType=biboAdmLicenseLicType, biboAdmLoginEntry=biboAdmLoginEntry, biboAdmLoginPassword=biboAdmLoginPassword, biboAdmLoginTable=biboAdmLoginTable, biboAdmLicenseKey=biboAdmLicenseKey, biboAdmLoginUser=biboAdmLoginUser, biboAdmLicenseHwSerial=biboAdmLicenseHwSerial, biboAdmPrivateKey=biboAdmPrivateKey, biboAdmLicenseState=biboAdmLicenseState, biboAdmLicenseEntry=biboAdmLicenseEntry, biboAdmHttpPassword=biboAdmHttpPassword, biboAdmLicenseSerialId=biboAdmLicenseSerialId, enterprises=enterprises, biboAdmPublicKey=biboAdmPublicKey, biboAdmActMonPassword=biboAdmActMonPassword, bintecsec=bintecsec, biboAdmLoginCommand=biboAdmLoginCommand, biboAdmAdminCommunity=biboAdmAdminCommunity, internet=internet, biboAdmWriteCommunity=biboAdmWriteCommunity, dod=dod, biboAdmLicenseTable=biboAdmLicenseTable)
