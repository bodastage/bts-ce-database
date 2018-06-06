"""Create ZTE 4G MO views

Revision ID: 9b8666957770
Revises: fe292ef150ae
Create Date: 2018-06-06 09:44:56.546000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b8666957770'
down_revision = 'fe292ef150ae'
branch_labels = None
depends_on = None


class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


ENBFunction = ReplaceableObject(
    'zte_cm_4g."ENBFunction"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."ENBFunction_id",
t1."x2BlackList",
t1."eNBId",
t1."userLabel",
t1."x2HOBlackList",
t1."x2WhiteList",
t2."vsDataENBFunction_id",
t2."holdoverTime",
t2."adminState",
t2."enbName",
t2."startUserStateTransThr",
t2."holdoverSwitch",
t2."scRecvPolicy",
t2."ewtsSendMed",
t2."sceneCfg",
t2."sib10StopTimerLen",
t2."rrcAdmitType",
t2."refPlmn",
t2."sib10StopMode",
t2."permitRRCNum",
t2."rsrpStatisticThd",
t2."shiftNumber",
t2."plmnEncodInd",
t2."dlSINRThd",
t2."decideNoDataTimer",
t2."maxScellNum",
t2."tarHeNBIDEncMeth",
t2."description",
t2."ulSINRThd"
FROM
zte_bulkcm_lte."ENBFunction" t1
INNER JOIN zte_bulkcm_lte."vsDataENBFunction" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."ENBFunction_id" = t2."ENBFunction_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."FileName" = t2."FileName" 

"""
)

EUtranCellFDD = ReplaceableObject(
    'zte_cm_4g."EUtranCellFDD"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."ENBFunction_id",
t1."EUtranCellFDD_id",
t1."maximumTransmissionPower",
t1."earfcnDl",
t1."cellSize",
t1."cellLocalId",
t1."cellResvInfo",
t1."userLabel",
t1."earfcnUl",
t1."pb",
t1."referenceSignalPower",
t1."pciList",
t1."plmnIdList",
t1."tac",
t1."pci",
t1."relatedAntennaList",
t1."allowedAccessClasses",
t2."vsDataEUtranCellFDD_id",
t2."offsetAngle",
t2."tm34T4RSwch",
t2."maxMCSDl",
t2."cpMerger",
t2."qam64DemSpIndUl",
t2."bandWidthUl",
t2."aggregationDl",
t2."maxMCSUl",
t2."coMPFlagUl",
t2."ratTarCarriFre_ratTarCarriFreTDD",
t2."csfbMethdofCDMA",
t2."aggregationUl",
t2."fullConfigSwch",
t2."ocs",
t2."testState",
t2."rd4ForCoverage",
t2."ratTarCarriFre_ratTarCarriFreCMA1xRTT",
t2."ratTarCarriFre_ratTarCarriFreUTRAFDD",
t2."radioMode",
t2."eai",
t2."voLTESwch",
t2."alias",
t2."ratioShared",
t2."refECellEquipmentFunction",
t2."upInterfFreqEffThr",
t2."rbSharMode",
t2."sampleRateCfg",
t2."ratTarCarriFre_ratTarCarriFreGERAN",
t2."cFI",
t2."siWindowLength",
t2."latitude",
t2."flagSwiModeUl",
t2."cellReservedForOptUse",
t2."csfbMethdofUMTS",
t2."ratioOperatorn",
t2."mumimoEnableUl",
t2."transmissionPower",
t2."adminState",
t2."ratTarCarriFre_ratTarCarriFreFDD",
t2."switchForGbrDrx",
t2."switchForNGbrDrx",
t2."cellRadius",
t2."matrixType",
t2."csfbMethodofGSM",
t2."cellRSPortNum",
t2."cceAdaptMod",
t2."phyChCPSel",
t2."maxUeRbNumDl",
t2."longitude",
t2."bfmumimoEnableDl",
t2."ceuccuSwitch",
t2."maxUeRbNumUl",
t2."ueTransMode",
t2."flagSwiMode",
t2."rlfSwitch",
t2."availStatus",
t2."ratTarCarriFre_ratTarCarriFreUTRATDD",
t2."loadtestSwitch",
t2."freqBandInd",
t2."minMCSDl",
t2."commCCENumDl",
t2."ratTarCarriFre_ratTarCarriFreCMAHRPD",
t2."addiSpecEmiss",
t2."minMCSUl",
t2."operState",
t2."rbInterferenceBitMapDl",
t2."timeAlignTimer",
t2."pullCardJudgeSwitch",
t2."rbInterferenceBitMapUl",
t2."bandWidthDl",
t2."description",
t2."energySavControl"
FROM
zte_bulkcm_lte."EUtranCellFDD" t1
INNER JOIN zte_bulkcm_lte."vsDataEUtranCellFDD" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."ENBFunction_id" = t2."ENBFunction_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."EUtranCellFDD_id" = t2."EUtranCellFDD_id" 

"""
)

EUtranRelation = ReplaceableObject(
    'zte_cm_4g."EUtranRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."ENBFunction_id",
t1."EUtranCellFDD_id",
t1."EUtranRelation_id",
t1."qOffset",
t1."adjacentCell",
t1."isHOAllowed",
t1."userLabel",
t1."isRemoveAllowed",
t1."cellIndividualOffset",
t2."vsDataEUtranRelation_id",
t2."nCelPriority",
t2."coperType",
t2."isAnrCreated",
t2."stateInd",
t2."switchonTimeWindow",
t2."isESCoveredBy",
t2."shareCover",
t2."resPRBUp",
t2."isX2HOAllowed",
t2."resPRBDown",
t2."coverESCell",
t2."lbIntraMeasureOffset",
t2."numRRCCntNumCov",
t2."s1DataFwdFlag",
t2."description"
FROM
zte_bulkcm_lte."EUtranRelation" t1
INNER JOIN zte_bulkcm_lte."vsDataEUtranRelation" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."ENBFunction_id" = t2."ENBFunction_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."EUtranCellFDD_id" = t2."EUtranCellFDD_id" 
 AND t1."EUtranRelation_id" = t2."EUtranRelation_id" 

"""
)

ExternalEUtranCellFDD = ReplaceableObject(
    'zte_cm_4g."ExternalEUtranCellFDD"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."ExternalEUtranCellFDD_id",
t1."earfcnUl",
t1."earfcnDl",
t1."cellLocalId",
t1."eNBId",
t1."pci",
t1."plmnIdList",
t1."userLabel",
t2."vsDataExternalEUtranCellFDD_id",
t2."bandWidthUl",
t2."switchSurportTrunking",
t2."mcc",
t2."freqBandInd",
t2."coMPFlagUl",
t2."tac",
t2."mnc",
t2."antPort1",
t2."bandWidthDl",
t2."description",
t2."cellType"
FROM
zte_bulkcm_lte."ExternalEUtranCellFDD" t1
INNER JOIN zte_bulkcm_lte."vsDataExternalEUtranCellFDD" t2
 ON t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."ExternalEUtranCellFDD_id" = t2."ExternalEUtranCellFDD_id" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

ExternalGsmCell = ReplaceableObject(
    'zte_cm_4g."ExternalGsmCell"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."ExternalGsmCell_id",
t1."cellIdentity",
t1."bcc",
t1."mnc",
t1."rac",
t1."bcchFrequency",
t1."userLabel",
t1."mcc",
t1."ncc",
t1."lac",
t2."vsDataExternalGsmCell_id",
t2."plmnIdList_mcc",
t2."isSupportVoIP",
t2."freqBand",
t2."isSupportPSHO",
t2."isSupportDTM",
t2."plmnIdList_mnc",
t2."bandIndicator",
t2."description"
FROM
zte_bulkcm_lte."ExternalGsmCell" t1
INNER JOIN zte_bulkcm_lte."vsDataExternalGsmCell" t2
 ON t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."ExternalGsmCell_id" = t2."ExternalGsmCell_id" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

ExternalUtranCellFDD = ReplaceableObject(
    'zte_cm_4g."ExternalUtranCellFDD"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."ExternalUtranCellFDD_id",
t1."mnc",
t1."rncId",
t1."uarfcnUl",
t1."uarfcnDl",
t1."rac",
t1."hsFlag",
t1."userLabel",
t1."primaryScramblingCode",
t1."mcc",
t1."cId",
t1."lac",
t2."vsDataExternalUtranCellFDD_id",
t2."plmnIdList_mcc",
t2."isSupportVoIP",
t2."isSupportPSHO",
t2."freqBandInd",
t2."plmnIdList_mnc",
t2."description"
FROM
zte_bulkcm_lte."ExternalUtranCellFDD" t1
INNER JOIN zte_bulkcm_lte."vsDataExternalUtranCellFDD" t2
 ON t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."ExternalUtranCellFDD_id" = t2."ExternalUtranCellFDD_id" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

GsmRelation = ReplaceableObject(
    'zte_cm_4g."GsmRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."ENBFunction_id",
t1."EUtranCellFDD_id",
t1."GsmRelation_id",
t1."adjacentCell",
t1."isHOAllowed",
t1."userLabel",
t2."vsDataGsmRelation_id",
t2."isRemoveAllowed",
t2."description",
t2."ratShareCover"
FROM
zte_bulkcm_lte."GsmRelation" t1
INNER JOIN zte_bulkcm_lte."vsDataGsmRelation" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."GsmRelation_id" = t2."GsmRelation_id" 
 AND t1."ENBFunction_id" = t2."ENBFunction_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."EUtranCellFDD_id" = t2."EUtranCellFDD_id" 
 AND t1."FileName" = t2."FileName" 

"""
)

ManagedElement = ReplaceableObject(
    'zte_cm_4g."ManagedElement"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."locationName",
t1."vendorName",
t1."userDefinedState",
t1."swVersion",
t1."managedElementType",
t1."userLabel",
t2."vsDataManagedElement_id",
t2."ADMINISTRATIVESTATE",
t2."maintainstatusGSM",
t2."maintainstatusTDS",
t2."CutoverStatus",
t2."MEADDR",
t2."RUNMODE",
t2."ADMINISTRATIVESTATE1",
t2."TRNCID",
t2."LONGITUDE",
t2."MESPAREADDR",
t2."vendorPlannedId",
t2."NODEBID",
t2."RUNRADIOMODE1",
t2."LMTMODIFYSTATUS",
t2."MESPAREADDR1",
t2."SITEID",
t2."PRIORITY",
t2."MEMASTERADDR1",
t2."LINKSTATE",
t2."operatorPlannedId",
t2."MAINTAINSTATUS",
t2."GBSCID",
t2."SERVICESTATUS",
t2."MEADDR1",
t2."CBSCID",
t2."BBUTYPE",
t2."ExtendField1",
t2."maintainstatusUMTS",
t2."operatorPlannedId1",
t2."LINKSTATE1",
t2."enableWLMode",
t2."RNCID",
t2."maintainstatusLTEFDD",
t2."enableUnCfgCcSlot",
t2."MEMASTERADDR",
t2."Scene",
t2."LATITUDE",
t2."USERDEFINEDMEID",
t2."maintainstatusCDMA",
t2."CABINETTYPE",
t2."LMTMODIFYSTATUS1",
t2."NOTE",
t2."RUNRADIOMODE",
t2."maintainstatusLTETDD",
t2."autoGetGeographicPos",
t2."vendorPlannedId1",
t2."RADIOMODE"
FROM
zte_bulkcm_lte."ManagedElement" t1
INNER JOIN zte_bulkcm_lte."vsDataManagedElement" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."FileName" = t2."FileName" 

"""
)

meContext = ReplaceableObject(
    'zte_cm_4g."meContext"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "meContextId",
        "dnPrefix"
    FROM
    zte_bulkcm_lte."meContext"

    """
)

SubNetwork = ReplaceableObject(
    'zte_cm_4g."SubNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id"
    FROM
    zte_bulkcm_lte."SubNetwork"

    """
)

SubNetwork_2 = ReplaceableObject(
    'zte_cm_4g."SubNetwork_2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "userLabel",
        "userDefinedNetworkType"
    FROM
    zte_bulkcm_lte."SubNetwork_2"

    """
)

UtranRelation = ReplaceableObject(
    'zte_cm_4g."UtranRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."ENBFunction_id",
t1."EUtranCellFDD_id",
t1."UtranRelation_id",
t1."adjacentCell",
t1."isHOAllowed",
t1."userLabel",
t2."vsDataUtranRelation_id",
t2."isRatESCoveredBy",
t2."isRemoveAllowed",
t2."description",
t2."ratShareCover"
FROM
zte_bulkcm_lte."UtranRelation" t1
INNER JOIN zte_bulkcm_lte."vsDataUtranRelation" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."ENBFunction_id" = t2."ENBFunction_id" 
 AND t1."UtranRelation_id" = t2."UtranRelation_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."EUtranCellFDD_id" = t2."EUtranCellFDD_id" 

"""
)

AC = ReplaceableObject(
    'zte_cm_4g."AC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataAC_id",
        "SwitchForUeNum",
        "switchForS1Gbr",
        "SwitchforEMC",
        "switchForConCtl",
        "switchForPower",
        "proRejThrdDl",
        "ueNumThrd",
        "proRejThrdUl",
        "reservedHO",
        "preemMaxNumOfGBR",
        "swtchOfCsfbHPAdmit",
        "swchProRejAC",
        "switchForS1NGBR",
        "switchForNGBR",
        "switchForGbr",
        "factorProRej",
        "switchForQueuing",
        "rabThrd",
        "switchForNGBRDl",
        "switchForGbrDl",
        "switchForNGBRUl",
        "acReport",
        "switchForGbrUl",
        "swchOfRedi4ACFail",
        "premptQciRank1",
        "description",
        "premptQciRank2",
        "SwitchForRAB"
    FROM
    zte_bulkcm_lte."vsDataAC"

    """
)

CDMA2000Reselection = ReplaceableObject(
    'zte_cm_4g."CDMA2000Reselection"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataCDMA2000Reselection_id",
        "preRegistrationZoneId",
        "oneXrttHomeReg",
        "oneXrttMultNID",
        "cdmaHRPDPara_hrpdReselPrio",
        "cdmaHRPDPara_hrpdThrdXLow",
        "oneXrttSID",
        "acBarMsg",
        "oneXrttPowerDownRegInd",
        "secPreRegistrationZoneId",
        "csfbSuptDualRx",
        "cdmaOneXRTTPara_oneXrttARFCN",
        "oneXrttRegAllow",
        "isPreRegistAllowed",
        "oneXrttRegZone",
        "acBarReg",
        "cdmaOneXRTTPara_oneXrttReselPrio",
        "oneXrttForeNIDReg",
        "cdmaHRPDPara_hrpdThrdXHigh",
        "cdmaOneXRTTPara_oneXrttThrdXLow",
        "reselHrpdSFH",
        "reselHrpdSFM",
        "oneXrttRegPeriod",
        "cdmaHRPDPara_hrpdBandClass",
        "searchWindowSize",
        "oneXrttZoneTimer",
        "tResel1XrttSFH",
        "cdmaHRPDPara_hrpdARNFCN",
        "oneXrttMultSID",
        "oneXrttForeSIDReg",
        "tResel1XrttSFM",
        "reselHrpd",
        "cdmaOneXRTTPara_oneXrttThrdXHigh",
        "userLabel",
        "oneXrttNID",
        "acBarEmg",
        "hrpdBdClassNum",
        "acBar10",
        "oneXrttTotalZone",
        "oneXrttBdClassNum",
        "acBar11",
        "acBar12",
        "acBar13",
        "acBar14",
        "oneXrttParaReg",
        "powerUpReg",
        "acBar15",
        "cdmaOneXRTTPara_oneXrttBandClass",
        "tResel1Xrtt",
        "description",
        "acBar0to9"
    FROM
    zte_bulkcm_lte."vsDataCDMA2000Reselection"

    """
)

CellMeasGroup = ReplaceableObject(
    'zte_cm_4g."CellMeasGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataCellMeasGroup_id",
        "interRatGSMPeriodMeasCfg",
        "interRatUTRANPeriodMeasCfg",
        "gsmLBMeasCfg",
        "interFHOMeasCfg",
        "rptCGIMeasCfg",
        "intraFHOMeasCfg",
        "openRatFMeasCfg",
        "anrMeasCfg",
        "cdma2K1xCSFBMeasCfg",
        "macroSmallMeasCfg",
        "opeRatVoiceMeasCfg",
        "tdMeasCfg",
        "cdmaANRMeasCfg",
        "measCfg4movUE",
        "wcdmaLBMeasCfg",
        "tdVoiceMeasCfg",
        "tdsLBMeasCfg",
        "wcdmaCSFBMeasCfg",
        "rsrpEventMeasCfgIdDl",
        "cdma2K1xMeasCfg",
        "openInterFMeasCfg",
        "intraLBMeasCfg",
        "modScellMeasCfg",
        "geranVoiceMeasCfg",
        "gsmCSFBMeasCfg",
        "cdma2KHRPDMeasCfg",
        "openRedMeasCfg",
        "utranANRMeasCfg",
        "rsrpPeriodMeasCfgIdDl",
        "rmvScellMeasCfg",
        "eICICMeasCfg",
        "closedInterFMeasCfg",
        "icicMeasCfg",
        "addScellMeasCfg",
        "userLabel",
        "ueRxTxTimeDiffPeriodMeasCfg",
        "wcdmaMeasCfg",
        "interFPeriodMeasCfg",
        "meaGroupId",
        "intraFPeriodMeasCfg",
        "wcdmaVoiceMeasCfg",
        "geranANRMeasCfg",
        "geranMeasCfg",
        "description",
        "tdCSFBMeasCfg"
    FROM
    zte_bulkcm_lte."vsDataCellMeasGroup"

    """
)

ControlPlaneTimer = ReplaceableObject(
    'zte_cm_4g."ControlPlaneTimer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataControlPlaneTimer_id",
        "ueCapaTimer",
        "ueCtxRelReqTimer",
        "pathSwitchTimer",
        "x2RsndUptDftTmr",
        "x2ResetAckTimer",
        "s1UptAckTimer",
        "rrcReCfgTimer",
        "rimResndReqTmr",
        "x2ResStatusRspT",
        "rimStopAckTmr",
        "rimInitRptTmr",
        "s1RsndUptDftTmr",
        "s1ResetAckTimer",
        "x2HoRelTimer",
        "rrcReEstTimer",
        "x2SetupRspTimer",
        "cdmaHoPrepareTimer",
        "rrcConnRelTimer",
        "rrcSetupTimer",
        "anrReportTimer",
        "csfbMeasTimer",
        "initialUETimer",
        "s1SetupRspTimer",
        "ccoRelTimer",
        "x2HoPrePareTimer",
        "s1RsdSetupDftTmr",
        "s1HoPrepareTimer",
        "rimEndResndTmr",
        "ueSetupFailTimer",
        "x2UptAckTimer",
        "x2RsdSetupDftTmr",
        "description",
        "s1HoOverAllTimer"
    FROM
    zte_bulkcm_lte."vsDataControlPlaneTimer"

    """
)

CSIRSConfig = ReplaceableObject(
    'zte_cm_4g."CSIRSConfig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataCSIRSConfig_id",
        "csiRSSWCH",
        "csiPeriod",
        "description",
        "csiRSResCfgIdx"
    FROM
    zte_bulkcm_lte."vsDataCSIRSConfig"

    """
)

ECellEquipmentFunction = ReplaceableObject(
    'zte_cm_4g."ECellEquipmentFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataECellEquipmentFunction_id",
        "cellMod",
        "cpTransPwr",
        "aasTiltDl",
        "anttoPortMap",
        "refRfDevice",
        "antMapDl",
        "rruCarrierNo",
        "aasTiltUl",
        "cpTransTime",
        "cpId",
        "slaveRRUFlag",
        "antMapUl",
        "cpSpeRefSigPwr",
        "maxCPTransPwr",
        "refBpDevice",
        "refSdrDeviceGroup",
        "description",
        "upActAntBitmap",
        "bplPort"
    FROM
    zte_bulkcm_lte."vsDataECellEquipmentFunction"

    """
)

EMLP = ReplaceableObject(
    'zte_cm_4g."EMLP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataEMLP_id",
        "delayRWeight",
        "serviceWeight",
        "gBRWeight",
        "qCiQueue",
        "alpha",
        "schedulerAlg",
        "eMLPIndex",
        "pFWeight",
        "lchDirection",
        "qCIWeight",
        "qCINum",
        "beta",
        "aMBRWeight",
        "aRPWeight",
        "description"
    FROM
    zte_bulkcm_lte."vsDataEMLP"

    """
)

ENBServicePrior = ReplaceableObject(
    'zte_cm_4g."ENBServicePrior"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataENBServicePrior_id",
        "srvPriLvUl",
        "srvPriLvDl",
        "qci",
        "description",
        "arp"
    FROM
    zte_bulkcm_lte."vsDataENBServicePrior"

    """
)

EUtranCellMeasurement = ReplaceableObject(
    'zte_cm_4g."EUtranCellMeasurement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataEUtranCellMeasurement_id",
        "geranMeasParas_nCCpermitted",
        "CDMA2000MeasParas_cdmaARFCN",
        "interFandInterR",
        "gsmLBMeasCfg",
        "multiPLMNLocSt4RdSwch",
        "intraFPeriodMeasSwitch",
        "filterCoeffUtra",
        "geranMeasParas_geranFreqRdPriority",
        "utranMeasParas_utranOffFreq",
        "cdmaANRMeasCfg",
        "tarNeighCellRsrqThr",
        "pingPongThres4Macro2Small",
        "utranMeasParas_utranFreqRdPriority",
        "offFreqPriorityPara_offFreqPriority1",
        "offFreqPriorityPara_offFreqPriority2",
        "offFreqPriorityPara_offFreqPriority3",
        "geranMeasParas_geranOffFreq",
        "offFreqPriorityPara_offFreqPriority4",
        "offFreqPriorityPara_offFreqPriority5",
        "geranMeasParas_geranBand",
        "offFreqPriorityPara_offFreqPriority6",
        "offFreqPriorityPara_offFreqPriority7",
        "CDMA2000MeasParas_cdmaFreqRdPriority",
        "gapDelay",
        "cdma2KHRPDMeasCfg",
        "filCoeUtran",
        "openRedMeasCfg",
        "CDMA2000MeasParas_searchWindowPresent",
        "timeOfShortHO",
        "eICICMeasCfg",
        "eutranMeasParas_freqBandInd",
        "servCellRsrqThr",
        "utranMeasParas_utranFreqBandInd",
        "utranMeasParas_utranFreqBandIndTDD",
        "intraFPeriodMeasCfg",
        "multiPLMNLocSt4ReestabSwch",
        "cSFBbaseLAI",
        "CDMA2000MeasParas_cdmaType",
        "geranMeasCfg",
        "csfbMethdofUMTS",
        "eutranMeasParas_interFMeasBW",
        "ratPriorityPara_ratPriority1",
        "ratPriorityPara_ratPriority2",
        "ratPriorityPara_ratPriority3",
        "ratPriorityPara_ratPriority4",
        "ratPriorityPara_ratPriority5",
        "ratPriorityPara_ratPriority6",
        "ratPriorityPara_ratPriority7",
        "CDMA2000MeasParas_cdmaOffFreq",
        "quantityFddUtra",
        "intraFHOMeasCfg",
        "rptCGIMeasCfg",
        "filterCoeffGera",
        "geranMeasParas_geranFreqCsfbPriority",
        "csfbMeasure",
        "anrMeasCfg",
        "utranMeasParas_utranArfcn",
        "lbMaxHOCell",
        "cdma2K1xCSFBMeasCfg",
        "csfbMethodofGSM",
        "measBaseVoiceSwch",
        "hoTarCellPRBThrd",
        "utranMeasParas_utranFreqCsfbPriority",
        "geranMeasParas_geranARFCN",
        "cdmaCarriFreqNum",
        "wcdmaLBMeasCfg",
        "cdma2K1xMeasCfg",
        "geranMeasParas_geranFreqANRInd",
        "lbIntraFreqPriority",
        "CDMA2000MeasParas_searchWinSize",
        "hoCandCelNum",
        "interRatGsmPeriodMeasSwitch",
        "utranMeasParas_utranFreqANRInd",
        "tdCSFBMeasCfg",
        "eutranMeasParas_lbInterFreqOfn",
        "CDMA2000MeasParas_cdmaFreqANRInd",
        "csfbMethdofCDMA",
        "ocs",
        "intraRATHObasedLoadSwch",
        "multiPLMNLocSt4PSSwch",
        "dualMeasSwitch",
        "measureThresh",
        "eutranMeasParas_offsetFreq",
        "filterCoeffRsrp",
        "tdsLBMeasCfg",
        "filterCoeffRsrq",
        "wcdmaCSFBMeasCfg",
        "intraLBMeasCfg",
        "interFPeriodMeasSwitch",
        "ratPriIdPara_ratPriIdleCSFB1",
        "ratPriIdPara_ratPriIdleCSFB2",
        "ratPriIdPara_ratPriIdleCSFB3",
        "ratPriIdPara_ratPriIdleCSFB4",
        "interRatUtranPeriodMeasSwitch",
        "rsrpPeriodMeasCfgIdDl",
        "eutranMeasParas_interFreqANRInd",
        "netWorkControlOrder",
        "ratPriCnPara_ratPriCnCSFB1",
        "ratPriCnPara_ratPriCnCSFB2",
        "intraFMeasBW",
        "ratPriCnPara_ratPriCnCSFB3",
        "ratPriCnPara_ratPriCnCSFB4",
        "macroSmallIntraFreqMeasSwch",
        "interFreqNum",
        "geranMeasParas_startARFCN",
        "utranMeasParas_utranArfcnTDD",
        "geranCarriFreqNum",
        "interFHOMeasCfg",
        "minStayTimeInSC",
        "openRatFMeasCfg",
        "neighCellConfig",
        "eutranMeasParas_eutranFreqRdPriority",
        "trigQuaofTarCellOrder",
        "macrotSmallForbidTime",
        "utranCarriFreqNum",
        "tdMeasCfg",
        "explicitARFCN",
        "multiPLMNLocStCSFB",
        "eutranMeasParas_interCarriFreq",
        "voiceMeasReCfgThrd",
        "refCellMeasGroup",
        "rsrpEventMeasCfgIdDl",
        "CDMA2000MeasParas_cdmaBandClass",
        "pingPongHoSwitch",
        "CDMA2000MeasParas_cdmaFreqCsfbPriority",
        "openInterFMeasCfg",
        "geranMeasParas_expliARFCNNum",
        "gsmCSFBMeasCfg",
        "utranANRMeasCfg",
        "utranMeasParas_duplexMode",
        "closedInterFMeasCfg",
        "icicMeasCfg",
        "wcdmaMeasCfg",
        "eutranMeasParas_lbInterFreqPriority",
        "geranANRMeasCfg",
        "description"
    FROM
    zte_bulkcm_lte."vsDataEUtranCellMeasurement"

    """
)

EUtranReselection = ReplaceableObject(
    'zte_cm_4g."EUtranReselection"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataEUtranReselection_id",
        "acBarringForSpecialACtOrig",
        "qQualminoffset",
        "intraFreqQqualMin",
        "iIntraPmax",
        "sfIntraHigh",
        "acBarringTimeOrig",
        "selQrxLevMin",
        "cellReselPrioBaseSpid",
        "sfIntraMedium",
        "qhyst",
        "csfbBarringFactor",
        "isIntraFreqReselection",
        "r9SNintraSrchP",
        "tCrMaxHyst",
        "sIntraSearch",
        "videoBarringFactor",
        "threshSrvLowQ",
        "eutranRslPara_sfInterHigh",
        "acBarringFactorOrig",
        "nCellChangeMedium",
        "eutranRslPara_interCarriFreq",
        "r9SIntraSrchP",
        "csfbBarringTime",
        "eutranRslPara_interThrdXHigh",
        "intraPmax",
        "interFreqNum",
        "eutranRslPara_interFreqQqualMin",
        "sNintraSrchPre",
        "eutranRslPara_interQrxLevMin",
        "nCellChangeHigh",
        "eutranRslPara_freqBandInd",
        "sNintraSrchQ",
        "threshSrvLowQSwitch",
        "videoBarForSpecAC",
        "intraQrxLevMin",
        "eutranRslPara_sfInterMedium",
        "qHystSFHigh",
        "voiceBarringTime",
        "cellBarred",
        "eutranRslPara_interThreshXHighQ",
        "intraPmaxOffset",
        "intraSearch",
        "acBarringForEmergency",
        "cellSelQqualMin",
        "isAllowedHOIn",
        "eutranRslPara_tReselectionInterEUTRA",
        "eutranRslPara_interThreshXLowQ",
        "eutranRslPara_qOffsetFreq",
        "acBarringTime",
        "eutranRslPara_interPresenceAntPort1",
        "acBarringForSpecialAC",
        "csgIndication",
        "videoBarringTime",
        "tReselectionIntraEUTRA",
        "preBlockTimer",
        "cellReselectionPriority",
        "csfbBarForSpecAC",
        "threshSvrLow",
        "eutranRslPara_interReselPrio",
        "intraPresenceAntPort1",
        "voiceBarForSpecAC",
        "snonintrasearch",
        "tEvaluation",
        "voiceBarringFactor",
        "eutranRslPara_interPmax",
        "sIntraSrchQ",
        "qrxLevMinOfst",
        "userLabel",
        "qHystSFMedium",
        "eutranRslPara_interThrdXLow",
        "acBarringFactor",
        "reselParaBaseSpeedFlag",
        "description",
        "iIntraPmaxOffset"
    FROM
    zte_bulkcm_lte."vsDataEUtranReselection"

    """
)

ExpConNtf = ReplaceableObject(
    'zte_cm_4g."ExpConNtf"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataExpConNtf_id",
        "memThresholdUl",
        "drbThresholdUl",
        "ecnPeriod",
        "recQueThresholdUl",
        "queThresholdDl",
        "ecnEnable",
        "retQueThresholdDl",
        "rlcQueThresholdDl",
        "description",
        "drbThresholdDl"
    FROM
    zte_bulkcm_lte."vsDataExpConNtf"

    """
)

GlobalQoS = ReplaceableObject(
    'zte_cm_4g."GlobalQoS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataGlobalQoS_id",
        "gbrDelayTh",
        "ngbrDelaySegNum",
        "ngbrDelayTh",
        "arpSegNum",
        "arpForEMC",
        "pktLsRtThrd4NGBR",
        "arpThresh",
        "description",
        "gbrDelaySegNum"
    FROM
    zte_bulkcm_lte."vsDataGlobalQoS"

    """
)

GlobleSwitchInformation = ReplaceableObject(
    'zte_cm_4g."GlobleSwitchInformation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataGlobleSwitchInformation_id",
        "glPsHoSwitch",
        "cmasSwch",
        "switchForMMELB",
        "clPsHoSwitch",
        "spidSwitch",
        "cnUbFtpEnable",
        "swchOfMtcACRest",
        "ulCOMPCloudIrcSwch",
        "swicthForHoPartCac",
        "sib8SysTimeSwch",
        "periodicANRSwitch",
        "gsmLBSwch",
        "cCOSwitch",
        "enableMroAlarm",
        "userStateTransSwch",
        "tmsiCodecSwch",
        "ueCa5Sch",
        "ewtsSendMed",
        "switchForUserInactivity",
        "cdmaSrvccSwitch",
        "signalBasedMdtSwch",
        "sib10StopTimerLen",
        "enablePaIVDA",
        "enablePciAlarm",
        "deRohcSch",
        "cpuLoadMngSwch",
        "macro2SmallPingPSwch",
        "interPlmnHOSwch",
        "ulBaseStationFDS",
        "x2PassProcSwch",
        "compJESwchUL",
        "swichForCpuAC",
        "etwsRepetitionCheck",
        "cdmCsfbSwitch",
        "ueRecordIdSwitch",
        "sib10StopMode",
        "tcpOrderEnable",
        "cicSwitch",
        "tcpFluidCtrlSwch",
        "rsrpStatisticThd",
        "etwsSwitch",
        "gsmCsfbSwitch",
        "erabSwitch",
        "fddTddHoSwitch",
        "ueCat4Sch",
        "gsmSrvccSwitch",
        "utranSrvccSwitch",
        "plmnEncodInd",
        "dlSINRThd",
        "ranSharSwch",
        "dedCarrierSharSwitch",
        "extendedQCISwitch",
        "voIPSwitch",
        "manageBasedMdtSwch",
        "dlBaseStationFDS",
        "cnUbFtpAddr",
        "description",
        "ulSINRThd",
        "utranLBSwch"
    FROM
    zte_bulkcm_lte."vsDataGlobleSwitchInformation"

    """
)

GsmReselection = ReplaceableObject(
    'zte_cm_4g."GsmReselection"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataGsmReselection_id",
        "gsmRslPara_geranThreshXLow",
        "gsmRslPara_followARFCNNum",
        "gsmRslPara_geranReselectionPriority",
        "gsmRslPara_startARFCN",
        "gsmRslPara_pMaxGERAN",
        "tReselectionGERAN",
        "gsmRslPara_followARFCNInd",
        "gsmRslPara_bandIndicator",
        "pmaxPresent",
        "userLabel",
        "gsmRslPara_nccPermitInd",
        "gsmRslPara_expliARFCNNum",
        "explicitARFCN",
        "sfHighGERAN",
        "geranFreqNum",
        "gsmRslPara_geranThreshXHigh",
        "gsmRslPara_qRxLevMin",
        "gsmRslPara_arfcnSpacing",
        "sfMediumGERAN",
        "description"
    FROM
    zte_bulkcm_lte."vsDataGsmReselection"

    """
)

HetNeteICICConfig = ReplaceableObject(
    'zte_cm_4g."HetNeteICICConfig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataHetNeteICICConfig_id",
        "connBias4CRE",
        "description",
        "absFuncCfg",
        "absProviderIndex"
    FROM
    zte_bulkcm_lte."vsDataHetNeteICICConfig"

    """
)

ICIC = ReplaceableObject(
    'zte_cm_4g."ICIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataICIC_id",
        "oiThrlLowUl",
        "centBorrFreqDlBitMap",
        "icicMap4MacroMicroDl",
        "rbByteMapDl",
        "cellResource",
        "centBorrFreqUlBitMap",
        "centFreqDlBitMap",
        "rbByteMapUl",
        "icicMap4MacroMicroUl",
        "fICIC4MacroMicroEnableDl",
        "fICICModeSelDl",
        "centFreqUlBitMap",
        "rbByteMapDlFB0",
        "edgeFreqDlBitMap",
        "fICIC4MacroMicroEnableUl",
        "icicEnabled",
        "icicDownCCUPA",
        "fICICModeSelUl",
        "paIndexCcu",
        "edgeFreqUlBitMap",
        "description",
        "oiThrHighUl"
    FROM
    zte_bulkcm_lte."vsDataICIC"

    """
)

LoadManagement = ReplaceableObject(
    'zte_cm_4g."LoadManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataLoadManagement_id",
        "numDrpSvc",
        "cellLdPreestSwch",
        "dlPRBLBExeThrd",
        "cellLoadLogSwitch",
        "lbRATPriority",
        "clbFreqNum",
        "ulPRBLBExeThrd",
        "gbrCompressLCSwch",
        "prbDlrecoveryThrd",
        "intraLBFreqPriorSwch",
        "prbDlovldThrd",
        "ulIntraNeiLdRelaThrd",
        "interCLBSwitch",
        "prbUlrecoveryThrd",
        "prbUlovldThrd",
        "targCellTypeInd",
        "prbLBExeThrdNZDl",
        "ldPreestimEna",
        "lbSwch",
        "lcSwch",
        "prbLBExeThrdZDl",
        "interNeighborLoadThrdDl",
        "dlIntraNeiLdRelaThrd",
        "intraNeighborLoadThrdDl",
        "prbLBExeThrdNZUl",
        "ldPreestimSwch",
        "prbLBExeThrdZUl",
        "interNeighborLoadThrdUl",
        "intraNeighborLoadThrdUl",
        "timePrtUE",
        "interManuLBSwch",
        "description",
        "clbExeThrd"
    FROM
    zte_bulkcm_lte."vsDataLoadManagement"

    """
)

MobileSpeedHO = ReplaceableObject(
    'zte_cm_4g."MobileSpeedHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataMobileSpeedHO_id",
        "mshoSwitch",
        "tHoMax",
        "ftTrgSFHigh",
        "speedJudgNum",
        "hiSpeedThr",
        "tHomaxhyst",
        "lCellRadius",
        "mCellRadius",
        "ftTrgSFMedium",
        "sCellRadius",
        "nHoHighSpeed",
        "vsCellRadius",
        "hoParaBaseSpeedFlag",
        "description",
        "nHoMediumSpeed"
    FROM
    zte_bulkcm_lte."vsDataMobileSpeedHO"

    """
)

MobilityManagement = ReplaceableObject(
    'zte_cm_4g."MobilityManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataMobilityManagement_id",
        "switchForNacc",
        "switchGeranRim",
        "switchUtranRim",
        "description"
    FROM
    zte_bulkcm_lte."vsDataMobilityManagement"

    """
)

Paging = ReplaceableObject(
    'zte_cm_4g."Paging"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataPaging_id",
        "pagingRepeatTime",
        "nB",
        "defaultPagingCycle",
        "modificationPeriodCoeff",
        "description"
    FROM
    zte_bulkcm_lte."vsDataPaging"

    """
)

PciSection = ReplaceableObject(
    'zte_cm_4g."PciSection"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataPciSection_id",
        "commonPCIEnd",
        "csgPCIStart",
        "csgPCINum",
        "commonPCIStart",
        "hybridPCIStart",
        "hybridPCINum",
        "description"
    FROM
    zte_bulkcm_lte."vsDataPciSection"

    """
)

PDCP = ReplaceableObject(
    'zte_cm_4g."PDCP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataPDCP_id",
        "profile257",
        "profile258",
        "profile259",
        "qCI",
        "profile260",
        "profile1",
        "profile2",
        "profile3",
        "profile4",
        "profile6",
        "maxCid",
        "description",
        "pdcpStatRptInd"
    FROM
    zte_bulkcm_lte."vsDataPDCP"

    """
)

PhyChannel = ReplaceableObject(
    'zte_cm_4g."PhyChannel"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataPhyChannel_id",
        "srsSubFrameCfg",
        "pucchSrNum",
        "nPucch1bP1",
        "dlDisRsAllSpInd",
        "pucchNcsAn",
        "numPucch1b",
        "dlRandMode",
        "prbRandomSwchDl",
        "puschCqiFbMethd",
        "pucchBlankNum",
        "srsEnable",
        "maxUserPucchfmt1",
        "puschhoppingOffset",
        "ttiBundSinrOut",
        "prbRandomSwchUl",
        "srsIniBW",
        "pucchSemiAnNum",
        "psThreshold",
        "ttiBundBlerThrd",
        "extendedBSRSwch",
        "prbRandNumberDl",
        "nd",
        "ng",
        "freqSelectDl",
        "pucchBlankFlag",
        "swchTTIBundling",
        "ackSrsTraSptInd",
        "aperiodicSRSSwch",
        "srTrCHNum",
        "cidofCoMP",
        "prbRandNumberUl",
        "pucchSORTDEnable",
        "phichDuration",
        "puschNsb",
        "srsHopBW",
        "freqSelectUl",
        "ttiBundSinrIn",
        "swchDAdjCqiMode",
        "compCellThreshold",
        "srsBWCfg",
        "pucchDeltaShf",
        "cqiRptPeriod",
        "pucchCqiRBNum",
        "srTrPeriod",
        "pucch3RB",
        "pucchAckRepNum",
        "cqiRptTTINum",
        "tansAntenSel",
        "description",
        "hoppingMode",
        "dsrTransMax"
    FROM
    zte_bulkcm_lte."vsDataPhyChannel"

    """
)

PositionConfig = ReplaceableObject(
    'zte_cm_4g."PositionConfig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataPositionConfig_id",
        "prsMutiInfoBitStr",
        "prsBandwidth",
        "ecidPosiSwchUl",
        "prsConfigId",
        "otdoaPosiSwch",
        "purposeCellPos",
        "lenPRSMutiBitStr",
        "prsNumDLFrames",
        "prsPwrOfst",
        "maxMeaRSTDCells",
        "description"
    FROM
    zte_bulkcm_lte."vsDataPositionConfig"

    """
)

PowerControlDL = ReplaceableObject(
    'zte_cm_4g."PowerControlDL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataPowerControlDL_id",
        "paForMSG2",
        "paForDTCH",
        "paForPCCH",
        "description",
        "paForDCCH",
        "paForCCCH",
        "paForBCCH"
    FROM
    zte_bulkcm_lte."vsDataPowerControlDL"

    """
)

PowerControlUL = ReplaceableObject(
    'zte_cm_4g."PowerControlUL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataPowerControlUL_id",
        "rsrpEventMeasSwitchDl",
        "switchForDCI3A3Pusch",
        "powerOffsetOfSRS",
        "poNominalPUCCH",
        "swithForPHR",
        "ueTransPowerCeiling",
        "switchForCLPCofPUCCH",
        "deltaFPucchFormat1b",
        "filterCoeffRSRP",
        "oiSwitchOfClosePc",
        "p0UePucchPub",
        "deltaMsg3",
        "switchForCLPCofPUSCH",
        "deltaPreambleMsg3",
        "lenofNIWindow",
        "deltaFPucchFormat2a",
        "deltaFPucchFormat2b",
        "targetIOT",
        "dCI3A3SelPucch",
        "rsrpPeriodMeasSwitchDl",
        "dCI3A3SelPusch",
        "p0NominalPUSCH",
        "poNominalPUSCH1",
        "alpha",
        "deltaFPucchFormat1",
        "deltaFPucchFormat2",
        "ks",
        "p0UePusch1Pub",
        "switchForDCI3A3Pucch",
        "ueTransMcsTarget",
        "puschPCAdjType",
        "description"
    FROM
    zte_bulkcm_lte."vsDataPowerControlUL"

    """
)

PrachFDD = ReplaceableObject(
    'zte_cm_4g."PrachFDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataPrachFDD_id",
        "raResponseWindowSize",
        "macNonContenPreamble",
        "ueAvgSpeed",
        "macContResTimer",
        "groupBEnable",
        "numContRA",
        "prachConfigIndex",
        "pathlossThrd",
        "rootSequenceIndex",
        "prachFreqOffset",
        "highSpeedFlag",
        "maxHarqMsg3Tx",
        "numContFreeRA",
        "numberOfRAPreambles",
        "prachFreqOffsetFlag",
        "ueSpeedThrd",
        "ncs",
        "sizeOfRAPreamblesGroupA",
        "preambleTransMax",
        "messageSizeGroupA",
        "preambleIniReceivedPower",
        "raCollProb",
        "messagePowerOffsetGroupB",
        "powerRampingStep",
        "description"
    FROM
    zte_bulkcm_lte."vsDataPrachFDD"

    """
)

PubFunctionPara = ReplaceableObject(
    'zte_cm_4g."PubFunctionPara"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataPubFunctionPara_id",
        "rssiPowerLsFactor",
        "rssiAlmThresh1",
        "rssiAlmThresh2",
        "rssiAlmRaiseTimes1",
        "rssiAlmClearTimes1",
        "rssiAlmRaiseTimes2",
        "rssiAlmClearTimes2",
        "rssiPowerDiffAlmClrCnt",
        "rssiPowerDiffAlmThr",
        "rssiPowerDiffAlmCnt",
        "description"
    FROM
    zte_bulkcm_lte."vsDataPubFunctionPara"

    """
)

QoS = ReplaceableObject(
    'zte_cm_4g."QoS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataQoS_id",
        "weightSRVUl",
        "weightSRVDl",
        "weightARP",
        "description"
    FROM
    zte_bulkcm_lte."vsDataQoS"

    """
)

QoSDSCPMapping = ReplaceableObject(
    'zte_cm_4g."QoSDSCPMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataQoSDSCPMapping_id",
        "arpSegID",
        "dscpValue",
        "qCI",
        "description"
    FROM
    zte_bulkcm_lte."vsDataQoSDSCPMapping"

    """
)

QoSPBRMapping = ReplaceableObject(
    'zte_cm_4g."QoSPBRMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataQoSPBRMapping_id",
        "pbrValue",
        "arpSegID",
        "qCI",
        "description",
        "lchDirection"
    FROM
    zte_bulkcm_lte."vsDataQoSPBRMapping"

    """
)

QoSPRIMapping = ReplaceableObject(
    'zte_cm_4g."QoSPRIMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataQoSPRIMapping_id",
        "qosBasicPrio",
        "arpSegID",
        "qosSrvClass",
        "description"
    FROM
    zte_bulkcm_lte."vsDataQoSPRIMapping"

    """
)

QoSServiceClass = ReplaceableObject(
    'zte_cm_4g."QoSServiceClass"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataQoSServiceClass_id",
        "discardTimer",
        "phtPhrTimer",
        "srvBearerType",
        "srvPrior",
        "qCI",
        "meaGRP",
        "sequenceNumType",
        "sequenNumLenth",
        "srvPacketLoss",
        "spsIntervalDL",
        "srvPacketDelay",
        "dlPathlossChgTh",
        "rlcMode",
        "srvClassName",
        "prdPhrTimer",
        "spsIntervalUL",
        "description",
        "factorForQCI"
    FROM
    zte_bulkcm_lte."vsDataQoSServiceClass"

    """
)

S1Ap = ReplaceableObject(
    'zte_cm_4g."S1Ap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataS1Ap_id",
        "adminState",
        "operState",
        "priority",
        "userLabel",
        "globalUniqueMmeId",
        "description",
        "refSctp"
    FROM
    zte_bulkcm_lte."vsDataS1Ap"

    """
)

SecurityManagement = ReplaceableObject(
    'zte_cm_4g."SecurityManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataSecurityManagement_id",
        "encrypAlgPriority",
        "integProtAlg",
        "integProtAlgPriority",
        "encryptionAlg",
        "description"
    FROM
    zte_bulkcm_lte."vsDataSecurityManagement"

    """
)

ServiceDrx = ReplaceableObject(
    'zte_cm_4g."ServiceDrx"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataServiceDrx_id",
        "shortDrxCycInd",
        "drxInactTimer",
        "onDuratTimer",
        "shortDrxCycT",
        "qCI",
        "description",
        "drxRetranTimer",
        "longDrxCyc",
        "shortDrxCyc"
    FROM
    zte_bulkcm_lte."vsDataServiceDrx"

    """
)

ServiceMAC = ReplaceableObject(
    'zte_cm_4g."ServiceMAC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataServiceMAC_id",
        "prdBsrTimer",
        "pCellPRBRatioActThrDl",
        "pCellPRBRatioDeActThrDl",
        "sCellPRBRatioActThrDl",
        "sCellPRBRatioDeActThrDl",
        "harqMaxTxNum",
        "retxBsrTimer",
        "description"
    FROM
    zte_bulkcm_lte."vsDataServiceMAC"

    """
)

SIScheduling = ReplaceableObject(
    'zte_cm_4g."SIScheduling"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataSIScheduling_id",
        "siId",
        "sib2",
        "sib3",
        "sib4",
        "sib30",
        "sib5",
        "sib31",
        "sib6",
        "sib10",
        "sib7",
        "sib11",
        "sib8",
        "sib12",
        "sib9",
        "periodicity",
        "description"
    FROM
    zte_bulkcm_lte."vsDataSIScheduling"

    """
)

SonCellPolicy = ReplaceableObject(
    'zte_cm_4g."SonCellPolicy"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataSonCellPolicy_id",
        "refSonPolicyPci",
        "refSonPolicySCH",
        "refSonPolicyRo",
        "sonFuncId",
        "refSonPolicyMlb",
        "refSonPolicyAnr",
        "refSonPolicyMro",
        "description",
        "refSonPolicyCco",
        "refSonPolicyEs"
    FROM
    zte_bulkcm_lte."vsDataSonCellPolicy"

    """
)

SonControl = ReplaceableObject(
    'zte_cm_4g."SonControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataSonControl_id",
        "sonFuncId",
        "sonSwitch",
        "description"
    FROM
    zte_bulkcm_lte."vsDataSonControl"

    """
)

SoneNBPolicy = ReplaceableObject(
    'zte_cm_4g."SoneNBPolicy"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataSoneNBPolicy_id",
        "refSonPolicyPci",
        "refSonPolicySCH",
        "refSonPolicyX2",
        "refSonPolicyRo",
        "sonFuncId",
        "refSonPolicyMlb",
        "refSonPolicyAnr",
        "refSonPolicyMro",
        "description",
        "refSonPolicyCco",
        "refSonPolicyEs"
    FROM
    zte_bulkcm_lte."vsDataSoneNBPolicy"

    """
)

SonPolicyAnr = ReplaceableObject(
    'zte_cm_4g."SonPolicyAnr"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataSonPolicyAnr_id",
        "sonMeasObjChoiceCounter",
        "sonEnableUtraANR",
        "sonReferPointPolicy_sonIsBreakPoint",
        "sonEnableNbrDel",
        "reportSwitch",
        "enableShAnr",
        "sonHoSuccThreshold",
        "sonEnableGsmNbrDel",
        "noHoStatisticTimer",
        "sonPolicyId",
        "staticTimerGrade",
        "anrAppointRptSwch",
        "sonNbrReportThreshold",
        "hoTimesThreshold",
        "anrAppointRptEndTime",
        "operLowHoSuccRate",
        "sonEnableUtraNbrDel",
        "sonFuncId",
        "anrAppointRptStartTime",
        "enableNoHoMod",
        "sonEnableGsmANR",
        "nbrDelHoCntThrd",
        "nbrDelCnt",
        "selfLearnSwch",
        "hoFailureRatio",
        "sonReferPointPolicy_sonTimeOutPolicy",
        "selfDelStatisticTimer",
        "statisticTimer",
        "grade",
        "sonReferPointPolicy_sonTimeOutPeriod",
        "sonMinDRXCycle",
        "sonRunMode",
        "twoWayFlg",
        "enableCdmaNbrDel",
        "enableCdmaANR",
        "selfDeleteNbrCellThrd",
        "sonEnableANR",
        "sonReferPointPolicy_sonReferPointID",
        "sonReferPointPolicy_sonReferPointAlias",
        "description"
    FROM
    zte_bulkcm_lte."vsDataSonPolicyAnr"

    """
)

SonPolicyX2 = ReplaceableObject(
    'zte_cm_4g."SonPolicyX2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataSonPolicyX2_id",
        "sonReferPointPolicy_sonIsBreakPoint",
        "reportSwitch",
        "x2SelfSetupSwitch",
        "sonReferPointPolicy_sonTimeOutPolicy",
        "statisticTimer",
        "grade",
        "x2SelfDelSwitch",
        "sonReferPointPolicy_sonTimeOutPeriod",
        "sonRunMode",
        "sonPolicyId",
        "sonS1HoSuccThrd",
        "sonX2DelCheckThreshold",
        "x2SelfLearnSwch",
        "sonFuncId",
        "sonReferPointPolicy_sonReferPointID",
        "sonReferPointPolicy_sonReferPointAlias",
        "sonX2HoSuccThrd",
        "description"
    FROM
    zte_bulkcm_lte."vsDataSonPolicyX2"

    """
)

SPSConfig = ReplaceableObject(
    'zte_cm_4g."SPSConfig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataSPSConfig_id",
        "spsMcsLowThrUl",
        "spsMcsLowThrDl",
        "spsMcsHighThrUl",
        "description",
        "spsMcsHighThrDl",
        "spsUseBandPerUl",
        "spsUseBandPerDl"
    FROM
    zte_bulkcm_lte."vsDataSPSConfig"

    """
)

UeEUtranMeasurement = ReplaceableObject(
    'zte_cm_4g."UeEUtranMeasurement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataUeEUtranMeasurement_id",
        "reportOnLeave",
        "prdRptRurpose",
        "eventId",
        "reportInterval",
        "prdReportInterval",
        "measCfgFunc",
        "reportQuantity",
        "thresholdOfRSRP",
        "thresholdOfRSRQ",
        "triggerQuantity",
        "measCfgIdx",
        "a3Offset",
        "a6Offset",
        "reportAmount",
        "maxReportCellNum",
        "prdReportAmount",
        "timeToTrigger",
        "a5Threshold2OfRSRP",
        "a5Threshold2OfRSRQ",
        "reportCriteria",
        "hysteresis",
        "description"
    FROM
    zte_bulkcm_lte."vsDataUeEUtranMeasurement"

    """
)

UeRATMeasurement = ReplaceableObject(
    'zte_cm_4g."UeRATMeasurement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataUeRATMeasurement_id",
        "cdmaSysNbrTrd",
        "trigTime",
        "naxReportCellNum",
        "rsrpSrvTrd",
        "rsrqSrvTrd",
        "eventId",
        "prdReportInterval",
        "evtReportInterval",
        "measCfgFunc",
        "rscpSysNbrTrd",
        "ratMeasCfgIdx",
        "geranNbrTrd",
        "prdReportAmount",
        "evtReportAmount",
        "eutranMeasQuantity",
        "reportCriteria",
        "hysterisis",
        "ecNoSysNbrTrd",
        "description",
        "utraFddReportQuan"
    FROM
    zte_bulkcm_lte."vsDataUeRATMeasurement"

    """
)

UeTimer = ReplaceableObject(
    'zte_cm_4g."UeTimer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataUeTimer_id",
        "t301",
        "t302",
        "t304",
        "tUserInacforMobile",
        "tUserInac",
        "t311_Ue",
        "n310",
        "n311",
        "t310_Ue",
        "t304_Cco",
        "description",
        "t320",
        "t300"
    FROM
    zte_bulkcm_lte."vsDataUeTimer"

    """
)

UtranCellReselectionFDD = ReplaceableObject(
    'zte_cm_4g."UtranCellReselectionFDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataUtranCellReselectionFDD_id",
        "reselUtranSFM",
        "reselUtran",
        "reselUtranSFH",
        "description"
    FROM
    zte_bulkcm_lte."vsDataUtranCellReselectionFDD"

    """
)

UtranReselectionFDD = ReplaceableObject(
    'zte_cm_4g."UtranReselectionFDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataUtranReselectionFDD_id",
        "utranRslPara_qQualMin",
        "utranRslPara_threshXLow",
        "utranRslPara_pMaxUTRA",
        "utranRslPara_utranCarriFreq",
        "utranRslPara_utranThrXLowQFdd",
        "userLabel",
        "utranRslPara_threshXHigh",
        "utranThreshXLowQFdd",
        "utranFreqNum",
        "utranThreshXHighQFdd",
        "utranRslPara_qRxLevMin",
        "description",
        "utranRslPara_utranThrXHighQFdd",
        "utranRslPara_utranReselPriority"
    FROM
    zte_bulkcm_lte."vsDataUtranReselectionFDD"

    """
)

UtranReselectionTDD = ReplaceableObject(
    'zte_cm_4g."UtranReselectionTDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "EUtranCellFDD_id",
        "vsDataUtranReselectionTDD_id",
        "utranTDDRslPara_utranTDDCarriFreq",
        "utranTDDFreqNum",
        "userLabel",
        "utranTDDRslPara_utranTDDReselPriority",
        "utranTDDRslPara_pMaxUtranTDD",
        "utranTDDRslPara_qRxLevMinTDD",
        "utranTDDRslPara_threshXLowTDD",
        "description",
        "utranTDDRslPara_threshXHighTDD"
    FROM
    zte_bulkcm_lte."vsDataUtranReselectionTDD"

    """
)

X2Ap = ReplaceableObject(
    'zte_cm_4g."X2Ap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "ENBFunction_id",
        "vsDataX2Ap_id",
        "userLabel",
        "description",
        "refSctp"
    FROM
    zte_bulkcm_lte."vsDataX2Ap"

    """
)


def upgrade():
    op.create_view(ENBFunction)
    op.create_view(EUtranCellFDD)
    op.create_view(EUtranRelation)
    op.create_view(ExternalEUtranCellFDD)
    op.create_view(ExternalGsmCell)
    op.create_view(ExternalUtranCellFDD)
    op.create_view(GsmRelation)
    op.create_view(ManagedElement)
    op.create_view(meContext)
    op.create_view(SubNetwork)
    op.create_view(SubNetwork_2)
    op.create_view(UtranRelation)
    op.create_view(AC)
    op.create_view(CDMA2000Reselection)
    op.create_view(CellMeasGroup)
    op.create_view(ControlPlaneTimer)
    op.create_view(CSIRSConfig)
    op.create_view(ECellEquipmentFunction)
    op.create_view(EMLP)
    op.create_view(ENBServicePrior)
    op.create_view(EUtranCellMeasurement)
    op.create_view(EUtranReselection)
    op.create_view(ExpConNtf)
    op.create_view(GlobalQoS)
    op.create_view(GlobleSwitchInformation)
    op.create_view(GsmReselection)
    op.create_view(HetNeteICICConfig)
    op.create_view(ICIC)
    op.create_view(LoadManagement)
    op.create_view(MobileSpeedHO)
    op.create_view(MobilityManagement)
    op.create_view(Paging)
    op.create_view(PciSection)
    op.create_view(PDCP)
    op.create_view(PhyChannel)
    op.create_view(PositionConfig)
    op.create_view(PowerControlDL)
    op.create_view(PowerControlUL)
    op.create_view(PrachFDD)
    op.create_view(PubFunctionPara)
    op.create_view(QoS)
    op.create_view(QoSDSCPMapping)
    op.create_view(QoSPBRMapping)
    op.create_view(QoSPRIMapping)
    op.create_view(QoSServiceClass)
    op.create_view(S1Ap)
    op.create_view(SecurityManagement)
    op.create_view(ServiceDrx)
    op.create_view(ServiceMAC)
    op.create_view(SIScheduling)
    op.create_view(SonCellPolicy)
    op.create_view(SonControl)
    op.create_view(SoneNBPolicy)
    op.create_view(SonPolicyAnr)
    op.create_view(SonPolicyX2)
    op.create_view(SPSConfig)
    op.create_view(UeEUtranMeasurement)
    op.create_view(UeRATMeasurement)
    op.create_view(UeTimer)
    op.create_view(UtranCellReselectionFDD)
    op.create_view(UtranReselectionFDD)
    op.create_view(UtranReselectionTDD)
    op.create_view(X2Ap)


def downgrade():
    op.drop_view(ENBFunction)
    op.drop_view(EUtranCellFDD)
    op.drop_view(EUtranRelation)
    op.drop_view(ExternalEUtranCellFDD)
    op.drop_view(ExternalGsmCell)
    op.drop_view(ExternalUtranCellFDD)
    op.drop_view(GsmRelation)
    op.drop_view(ManagedElement)
    op.drop_view(meContext)
    op.drop_view(SubNetwork)
    op.drop_view(SubNetwork_2)
    op.drop_view(UtranRelation)
    op.drop_view(AC)
    op.drop_view(CDMA2000Reselection)
    op.drop_view(CellMeasGroup)
    op.drop_view(ControlPlaneTimer)
    op.drop_view(CSIRSConfig)
    op.drop_view(ECellEquipmentFunction)
    op.drop_view(EMLP)
    op.drop_view(ENBServicePrior)
    op.drop_view(EUtranCellMeasurement)
    op.drop_view(EUtranReselection)
    op.drop_view(ExpConNtf)
    op.drop_view(GlobalQoS)
    op.drop_view(GlobleSwitchInformation)
    op.drop_view(GsmReselection)
    op.drop_view(HetNeteICICConfig)
    op.drop_view(ICIC)
    op.drop_view(LoadManagement)
    op.drop_view(MobileSpeedHO)
    op.drop_view(MobilityManagement)
    op.drop_view(Paging)
    op.drop_view(PciSection)
    op.drop_view(PDCP)
    op.drop_view(PhyChannel)
    op.drop_view(PositionConfig)
    op.drop_view(PowerControlDL)
    op.drop_view(PowerControlUL)
    op.drop_view(PrachFDD)
    op.drop_view(PubFunctionPara)
    op.drop_view(QoS)
    op.drop_view(QoSDSCPMapping)
    op.drop_view(QoSPBRMapping)
    op.drop_view(QoSPRIMapping)
    op.drop_view(QoSServiceClass)
    op.drop_view(S1Ap)
    op.drop_view(SecurityManagement)
    op.drop_view(ServiceDrx)
    op.drop_view(ServiceMAC)
    op.drop_view(SIScheduling)
    op.drop_view(SonCellPolicy)
    op.drop_view(SonControl)
    op.drop_view(SoneNBPolicy)
    op.drop_view(SonPolicyAnr)
    op.drop_view(SonPolicyX2)
    op.drop_view(SPSConfig)
    op.drop_view(UeEUtranMeasurement)
    op.drop_view(UeRATMeasurement)
    op.drop_view(UeTimer)
    op.drop_view(UtranCellReselectionFDD)
    op.drop_view(UtranReselectionFDD)
    op.drop_view(UtranReselectionTDD)
    op.drop_view(X2Ap)