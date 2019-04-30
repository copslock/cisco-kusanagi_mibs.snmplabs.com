#
# PySNMP MIB module CXProduct-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXProduct-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
cxProduct, = mibBuilder.importSymbols("MEMOTEC-SMI", "cxProduct")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Bits, TimeTicks, Counter32, Counter64, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, NotificationType, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Bits", "TimeTicks", "Counter32", "Counter64", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "NotificationType", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SapIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class Alias(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class ThruputClass(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("bps75", 3), ("bps150", 4), ("bps300", 5), ("bps600", 6), ("bps1200", 7), ("bps2400", 8), ("bps4800", 9), ("bps9600", 10), ("bps19200", 11), ("bps48000", 12), ("bps64000", 13))

cxMc600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 1))
cxPx600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 2))
cxViewing = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 3))
cxChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 4))
cxSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5))
cxApplication = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6))
cxRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7))
cxPrivate = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8))
cxChassis2 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 9))
cxRegChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1))
cxRegChasCX1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1))
cxRegChasCX900 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 2))
cxRegChasCX950 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 3))
cxRegSubSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2))
cxRegSubSysMC600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 1))
cxRegSubSysAC600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 2))
cxRegSubSysPX600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 3))
cxRegSubSysFR600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 4))
cxRegSubSysCL600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 5))
cxRegSubSysLF600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 6))
cxRegSubSysDI600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 7))
cxRegSubSysFX600 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 2, 8))
cxModuleHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 1))
cxIoHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 2))
cxFileServer = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3))
cxSecurityLevel = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 4))
cxOperatingSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 5))
cxConsoleDriver = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6))
cxInterApplicationModule = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 7))
cxUserInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 8))
cxTokenBus = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9))
cxLanIoPort = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10))
cxSubSysInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 11))
cxIoHwInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 12))
cxSystemManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 13))
cxCommonConsole = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 14))
cxPmb = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 15))
cxPortManager = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16))
cxEventManager = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 17))
cxDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 18))
cxBitOrientedProtocolDriver = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 1))
cxFrameRelayInterfaceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 2))
cxFrameRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3))
cxSdxi = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 4))
cxGwMux = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5))
cxIf = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 6))
cxTransmission = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 7))
cxConv = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8))
cxDot1dBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 9))
cxIp = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 10))
cxIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 11))
cxUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 12))
cxIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13))
cxCfgDot1dBase = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 14))
cxCfgIpSap = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 15))
cxCfgIp = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16))
cxCfgSrBase = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 17))
cxGwFr = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18))
cxGwX25 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 19))
cxPppAsyncDriver = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 20))
cxFltIp = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 21))
cxFltIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22))
cxAdxi = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 23))
cxCompression = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 24))
cxEthernetDriver = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 25))
cxPpp = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 26))
cxLapBD = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27))
cxLapBConv = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28))
cxX25 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 29))
cxAsync = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 30))
cxSNA = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 31))
cxISDN = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32))
cxLlcFrConv = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33))
cxLlcim = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 34))
cxSnalc = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35))
cxBOPIO = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 36))
cxSDLC = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37))
cxQLLC = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38))
cxDds = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39))
cxUTst = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40))
cxUDrv = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 41))
cxV34 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42))
cxOSP = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 43))
cxAsyncIo = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44))
cxEthIo = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45))
cxDial = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46))
cxLlcLanConv = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47))
cxBCM = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48))
cxMLPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49))
cxVR = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 50))
cxTrdIo = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51))
cxDSX1 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 52))
cxDSX1Ext = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53))
cxGim = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55))
cxBsc = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56))
cxDsp = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57))
cxAtmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58))
cxCAS = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59))
cxST = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60))
cxAtmPhy = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61))
cxAtmExt = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 62))
cxPCM = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63))
cxACTE = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 1))
cxT1E1 = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2))
cxDataScope = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 3))
cxBri = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4))
mibBuilder.exportSymbols("CXProduct-SMI", cxRegSubSysFX600=cxRegSubSysFX600, cxSnalc=cxSnalc, cxMc600=cxMc600, cxAdxi=cxAdxi, cxDownload=cxDownload, cxMLPPP=cxMLPPP, cxDSX1Ext=cxDSX1Ext, cxSystemManagement=cxSystemManagement, cxPortManager=cxPortManager, cxDsp=cxDsp, cxPppAsyncDriver=cxPppAsyncDriver, cxISDN=cxISDN, cxIoHwInfo=cxIoHwInfo, cxApplication=cxApplication, cxVR=cxVR, cxRegChasCX950=cxRegChasCX950, cxIoHardware=cxIoHardware, cxUserInterface=cxUserInterface, cxSNA=cxSNA, cxPx600=cxPx600, cxAtmExt=cxAtmExt, cxBri=cxBri, cxUTst=cxUTst, cxInterApplicationModule=cxInterApplicationModule, cxST=cxST, cxPpp=cxPpp, cxUdp=cxUdp, cxRegChasCX900=cxRegChasCX900, cxCfgDot1dBase=cxCfgDot1dBase, cxV34=cxV34, cxTrdIo=cxTrdIo, cxFileServer=cxFileServer, cxX25=cxX25, cxFltIp=cxFltIp, cxCompression=cxCompression, cxRegSubSysFR600=cxRegSubSysFR600, cxRegSubSysLF600=cxRegSubSysLF600, cxBOPIO=cxBOPIO, cxFrameRelayInterfaceModule=cxFrameRelayInterfaceModule, cxSDLC=cxSDLC, cxLlcLanConv=cxLlcLanConv, cxIcmp=cxIcmp, cxLlcFrConv=cxLlcFrConv, cxRegSubSysCL600=cxRegSubSysCL600, cxGwMux=cxGwMux, ThruputClass=ThruputClass, cxGwFr=cxGwFr, cxViewing=cxViewing, cxRegSubSysMC600=cxRegSubSysMC600, cxConv=cxConv, cxLlcim=cxLlcim, cxIf=cxIf, cxCAS=cxCAS, cxPmb=cxPmb, cxDataScope=cxDataScope, cxAsyncIo=cxAsyncIo, cxSdxi=cxSdxi, cxCommonConsole=cxCommonConsole, cxQLLC=cxQLLC, cxRegSubSysDI600=cxRegSubSysDI600, cxRegChassis=cxRegChassis, cxRegSubSysPX600=cxRegSubSysPX600, cxCfgSrBase=cxCfgSrBase, cxLapBD=cxLapBD, cxT1E1=cxT1E1, cxACTE=cxACTE, cxFltIpx=cxFltIpx, cxEthIo=cxEthIo, cxOSP=cxOSP, cxBsc=cxBsc, cxPrivate=cxPrivate, cxFrameRelay=cxFrameRelay, cxBCM=cxBCM, cxIpx=cxIpx, SapIndex=SapIndex, cxSystem=cxSystem, cxCfgIpSap=cxCfgIpSap, cxEthernetDriver=cxEthernetDriver, cxLanIoPort=cxLanIoPort, cxSubSysInfo=cxSubSysInfo, cxDds=cxDds, cxBitOrientedProtocolDriver=cxBitOrientedProtocolDriver, cxIp=cxIp, cxLapBConv=cxLapBConv, cxConsoleDriver=cxConsoleDriver, cxGim=cxGim, cxSecurityLevel=cxSecurityLevel, cxTokenBus=cxTokenBus, cxUDrv=cxUDrv, cxChassis=cxChassis, cxRegSubSysAC600=cxRegSubSysAC600, cxRegistration=cxRegistration, cxAsync=cxAsync, cxDot1dBridge=cxDot1dBridge, Alias=Alias, cxRegChasCX1000=cxRegChasCX1000, cxGwX25=cxGwX25, cxCfgIp=cxCfgIp, cxDSX1=cxDSX1, cxAtmPhy=cxAtmPhy, cxTransmission=cxTransmission, cxRegSubSystem=cxRegSubSystem, cxChassis2=cxChassis2, cxDial=cxDial, cxAtmDxi=cxAtmDxi, cxPCM=cxPCM, cxOperatingSystem=cxOperatingSystem, cxEventManager=cxEventManager, cxModuleHardware=cxModuleHardware)