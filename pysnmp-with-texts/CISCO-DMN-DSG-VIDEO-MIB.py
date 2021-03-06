#
# PySNMP MIB module CISCO-DMN-DSG-VIDEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-VIDEO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Integer32, TimeTicks, NotificationType, iso, Bits, ObjectIdentity, ModuleIdentity, Counter32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "iso", "Bits", "ObjectIdentity", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGVideo = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14))
ciscoDSGVideo.setRevisions(('2010-10-13 08:00', '2010-08-30 11:00', '2010-03-22 05:00', '2010-02-12 12:00', '2009-12-07 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGVideo.setRevisionsDescriptions(('V01.00.04 2010-10-13 Updated videoPVFormat options for migrating D985X/D9865 to generic logic.', 'V01.00.03 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.02 2010-03-22 The Syntax of Unsigned32 MIB objects whose range is within the range of Integer32, is updated to Integer32.', 'V01.00.01 2010-02-12 The Syntax of read-only objects is updated to DisplayString.', 'V01.00.00 2009-12-07 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGVideo.setLastUpdated('201010130800Z')
if mibBuilder.loadTexts: ciscoDSGVideo.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGVideo.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGVideo.setDescription('Cisco DSG Video MIB.')
videoCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1), )
if mibBuilder.loadTexts: videoCtrlTable.setStatus('current')
if mibBuilder.loadTexts: videoCtrlTable.setDescription('Video Control Table.')
videoCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-VIDEO-MIB", "videoCtrlInstance"))
if mibBuilder.loadTexts: videoCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: videoCtrlEntry.setDescription('Entry for Video Control Table.')
videoCtrlInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: videoCtrlInstance.setStatus('current')
if mibBuilder.loadTexts: videoCtrlInstance.setDescription('Instance for Video Control Table.')
videoPVFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("hd1080i", 2), ("hd720p", 3), ("sd", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: videoPVFormat.setStatus('current')
if mibBuilder.loadTexts: videoPVFormat.setDescription('Primary Video Format: 1080i/720p/SD/Auto.')
videoSDFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("auto", 1), ("ntsc", 2), ("palBG", 3), ("palD", 4), ("palI", 5), ("palM", 6), ("palNAR", 7), ("ntscJ", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: videoSDFormat.setStatus('current')
if mibBuilder.loadTexts: videoSDFormat.setDescription('Standard Definition Video Format: PAL-B/G /PAL-D/PAL-I/PAL-M/ PAL-N(AR)/NTSC/NTSC-J/AUTO.')
videoTriSynch = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: videoTriSynch.setStatus('current')
if mibBuilder.loadTexts: videoTriSynch.setDescription('Component Tri-Sync Enabled/Disabled.')
videoCutoff = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: videoCutoff.setStatus('current')
if mibBuilder.loadTexts: videoCutoff.setDescription('Enable/Disable cutting video when an alarm occurs.')
aspectRatioSD = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fourThird", 1), ("sixteenNinth", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aspectRatioSD.setStatus('current')
if mibBuilder.loadTexts: aspectRatioSD.setDescription('Standard Definition Aspect Ratio: 4:3/16:9.')
aspectRatioSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("auto", 2), ("autoAFD", 3), ("sixteenByNineLetterBox", 4), ("fourByThreePillarBox", 5), ("fourteenByNine", 6), ("fourByThreeCCO", 7), ("sixteenByNineSCALE", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aspectRatioSelection.setStatus('current')
if mibBuilder.loadTexts: aspectRatioSelection.setDescription('Aspect Ratio Selection.')
closedCaptionPrefMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("auto", 1), ("saCustom", 2), ("eia708", 3), ("type3", 4), ("type4SA", 5), ("type4ATSC", 6), ("reserved", 7), ("dvs157", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: closedCaptionPrefMode.setStatus('current')
if mibBuilder.loadTexts: closedCaptionPrefMode.setDescription('Preferred Closed Captioning Mode if multiple in stream.')
videoStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2), )
if mibBuilder.loadTexts: videoStatusTable.setStatus('current')
if mibBuilder.loadTexts: videoStatusTable.setDescription('Video Status Table.')
videoStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-VIDEO-MIB", "videoStatusInstance"))
if mibBuilder.loadTexts: videoStatusEntry.setStatus('current')
if mibBuilder.loadTexts: videoStatusEntry.setDescription('Entry for Video Status Table.')
videoStatusInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: videoStatusInstance.setStatus('current')
if mibBuilder.loadTexts: videoStatusInstance.setDescription('Instance for Video Status Table.')
videoStream = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("sd480i2997", 1), ("sd480i3000", 2), ("sd576i2500", 3), ("hd720p5000", 4), ("hd720p5994", 5), ("hd720p6000", 6), ("hd1080i2500", 7), ("hd1080i2997", 8), ("hd1080i3000", 9), ("unknown", 10), ("unsupported", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoStream.setStatus('current')
if mibBuilder.loadTexts: videoStream.setDescription('Video Stream Format.')
videoPVOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hd1080i", 1), ("hd720p", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoPVOutput.setStatus('current')
if mibBuilder.loadTexts: videoPVOutput.setDescription('Primary Video Actual Output Format.')
videoSDOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("ntsc", 1), ("palBG", 2), ("palD", 3), ("palI", 4), ("palM", 5), ("palNAR", 6), ("ntscJ", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoSDOutput.setStatus('current')
if mibBuilder.loadTexts: videoSDOutput.setDescription('Standard Definition Actual Video Output Format.')
videoBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoBitRate.setStatus('current')
if mibBuilder.loadTexts: videoBitRate.setDescription('Video Bitrate in Mbps.The range is from 0.0 to 4294.967295 Mbps in steps of 0.000001 Mbps.')
video32PullDown = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("yes", 1), ("no", 2), ("recent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: video32PullDown.setStatus('current')
if mibBuilder.loadTexts: video32PullDown.setDescription('3:2 Pulldown: Yes/No/Recent.')
videoFPS = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoFPS.setStatus('current')
if mibBuilder.loadTexts: videoFPS.setDescription('Frames per Second ( fps ).The range is from 0.0 to 4294967.295 fps.')
videoSynchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoSynchMode.setStatus('current')
if mibBuilder.loadTexts: videoSynchMode.setDescription('Synchronization Mode: Auto/Manual.')
videoEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("mpeg1", 2), ("mpeg2", 3), ("h264", 4), ("vc1", 5), ("mpeg4p2", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoEncoding.setStatus('current')
if mibBuilder.loadTexts: videoEncoding.setDescription('Encoding format of the incoming video stream.')
aspectRatioConversion = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("none", 1), ("fourByThreeLetterBox", 2), ("fourByThreePillarBox", 3), ("fourteenByNineLetterBox", 4), ("fourteenByNinePillarBox", 5), ("fourByThreeCCO", 6), ("sixteenByNineCCO", 7), ("sixteenByNineLBToFourteenByNineLB", 8), ("fourByThreePBToFourteenByNinePB", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aspectRatioConversion.setStatus('current')
if mibBuilder.loadTexts: aspectRatioConversion.setDescription('Actual Aspect Ratio Conversion.')
aspectRatioStreamAR = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("fourByThree", 1), ("sixteenByNine", 2), ("twoTwentyOneByHundred", 3), ("square", 4), ("unavailable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aspectRatioStreamAR.setStatus('current')
if mibBuilder.loadTexts: aspectRatioStreamAR.setDescription('Actual Video Stream Aspect Ratio.')
aspectRatioWSSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("passthrough", 1), ("suppress", 2), ("autoModify", 3), ("autoCreate", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aspectRatioWSSMode.setStatus('current')
if mibBuilder.loadTexts: aspectRatioWSSMode.setDescription('Widescreen Signalling Mode.')
aspectRatioWSSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("fourByThreeFullFormat", 1), ("sixteenByNineLetterBoxCentre", 2), ("sixteenByNineLetterBoxTop", 3), ("greaterThanSixteenByNineLetterBoxCentre", 4), ("fourteenByNineLetterBoxCentre", 5), ("fourteenByNineLetterBoxTop", 6), ("fourteenByNineFullFormatCentre", 7), ("sixteenByNineFullFormat", 8), ("undefined", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aspectRatioWSSStatus.setStatus('current')
if mibBuilder.loadTexts: aspectRatioWSSStatus.setDescription('Widescreen Signalling Status.')
closedCaptionActOP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("auto", 1), ("saCustom", 2), ("eia708", 3), ("type3", 4), ("type4SA", 5), ("type4ATSC", 6), ("reserved", 7), ("dvs157", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: closedCaptionActOP.setStatus('current')
if mibBuilder.loadTexts: closedCaptionActOP.setDescription('Actual Closed Captioning Output Mode.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-VIDEO-MIB", videoEncoding=videoEncoding, videoSDFormat=videoSDFormat, videoSynchMode=videoSynchMode, PYSNMP_MODULE_ID=ciscoDSGVideo, video32PullDown=video32PullDown, videoCtrlInstance=videoCtrlInstance, videoStream=videoStream, videoCtrlTable=videoCtrlTable, aspectRatioWSSStatus=aspectRatioWSSStatus, aspectRatioConversion=aspectRatioConversion, videoPVFormat=videoPVFormat, videoPVOutput=videoPVOutput, videoBitRate=videoBitRate, aspectRatioStreamAR=aspectRatioStreamAR, closedCaptionPrefMode=closedCaptionPrefMode, ciscoDSGVideo=ciscoDSGVideo, videoSDOutput=videoSDOutput, videoCutoff=videoCutoff, videoStatusTable=videoStatusTable, videoFPS=videoFPS, aspectRatioWSSMode=aspectRatioWSSMode, aspectRatioSD=aspectRatioSD, aspectRatioSelection=aspectRatioSelection, videoCtrlEntry=videoCtrlEntry, videoStatusInstance=videoStatusInstance, videoTriSynch=videoTriSynch, videoStatusEntry=videoStatusEntry, closedCaptionActOP=closedCaptionActOP)
