"""Create ZTE 3G MO views

Revision ID: fe292ef150ae
Revises: a02559b135e6
Create Date: 2018-06-06 09:44:51.752000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe292ef150ae'
down_revision = 'a02559b135e6'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


EUtranRelation = ReplaceableObject(
    'zte_cm_3g."EUtranRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."UtranCellFDD_id",
t1."EUtranRelation_id",
t1."adjacentCell",
t2."vsDataEUtranRelation_id",
t2."userLabel",
t2."description"
FROM
zte_bulkcm_umts."EUtranRelation" t1
INNER JOIN zte_bulkcm_umts."vsDataEUtranRelation" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."UtranCellFDD_id" = t2."UtranCellFDD_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 
 AND t1."EUtranRelation_id" = t2."EUtranRelation_id" 

"""
)

ExternalENBFunction = ReplaceableObject(
    'zte_cm_3g."ExternalENBFunction"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."ExternalENBFunction_id",
t2."vsDataExternalENBFunction_id",
t2."rncid",
t2."eNodeBType",
t2."eNodeBId",
t2."userLabel",
t2."description"
FROM
zte_bulkcm_umts."ExternalENBFunction" t1
INNER JOIN zte_bulkcm_umts."vsDataExternalENBFunction" t2
 ON t1."ExternalENBFunction_id" = t2."ExternalENBFunction_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

ExternalEUtranCellFDD = ReplaceableObject(
    'zte_cm_3g."ExternalEUtranCellFDD"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."ExternalENBFunction_id",
t1."ExternalEUtranCellFDD_id",
t1."cellIdentity",
t1."earfcnUl",
t1."mnc",
t1."earfcnDl",
t1."pci",
t1."mncLength",
t1."plmnNum",
t1."mcc",
t2."vsDataExternalEUtranCellFDD_id",
t2."eutranDlLdThrd",
t2."sharingMNC",
t2."userLabel",
t2."sharingMNCLength",
t2."lac",
t2."eutranUlLdThrd",
t2."sharingMCC",
t2."rac",
t2."tac",
t2."eutranFreqBandInd",
t2."eUtranMeasBand",
t2."description"
FROM
zte_bulkcm_umts."ExternalEUtranCellFDD" t1
INNER JOIN zte_bulkcm_umts."vsDataExternalEUtranCellFDD" t2
 ON t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."ExternalEUtranCellFDD_id" = t2."ExternalEUtranCellFDD_id" 
 AND t1."ExternalENBFunction_id" = t2."ExternalENBFunction_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

ExternalGsmCell = ReplaceableObject(
    'zte_cm_3g."ExternalGsmCell"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."ExternalGsmCell_id",
t1."cellIdentity",
t1."mnc",
t1."bcc",
t1."rac",
t1."bcchFrequency",
t1."userLabel",
t1."mcc",
t1."lac",
t1."ncc",
t1."racc",
t2."vsDataExternalGsmCell_id",
t2."maximumAllowedUlTxPower",
t2."gsmDlLdThrd",
t2."snacNum",
t2."indoorCellInd",
t2."sharingMCC",
t2."deltaQrxlevminPr",
t2."gsmUlLdThrd",
t2."adjPhyGsmCId",
t2."deltaQrxlevminSib12",
t2."bandIndicator",
t2."geranCellInd",
t2."hcsPrio",
t2."qrxlevMinSib12",
t2."sharingMNC",
t2."mncLength",
t2."gsmDlRtLdThrd",
t2."sharingMNCLength",
t2."qrxlevMin",
t2."bscId",
t2."deltaQrxlevmin",
t2."gsmUlRtLdThrd",
t2."snacList",
t2."deltaQrxlevminSib12Pr",
t2."description",
t2."cellIndivOffset"
FROM
zte_bulkcm_umts."ExternalGsmCell" t1
INNER JOIN zte_bulkcm_umts."vsDataExternalGsmCell" t2
 ON t1."ExternalGsmCell_id" = t2."ExternalGsmCell_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

ExternalRncFunction = ReplaceableObject(
    'zte_cm_3g."ExternalRncFunction"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."ExternalRncFunction_id",
t1."rncId",
t1."mnc",
t1."userLabel",
t1."mcc",
t1."controlledCellList",
t2."vsDataExternalRncFunction_id",
t2."sharingMCC",
t2."divCtrlInd",
t2."sharingMNC",
t2."dIurCmbInd",
t2."description",
t2."refUIurLink"
FROM
zte_bulkcm_umts."ExternalRncFunction" t1
INNER JOIN zte_bulkcm_umts."vsDataExternalRncFunction" t2
 ON t1."FileName" = t2."FileName" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."ExternalRncFunction_id" = t2."ExternalRncFunction_id" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

ExternalUtranCellFDD = ReplaceableObject(
    'zte_cm_3g."ExternalUtranCellFDD"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."ExternalRncFunction_id",
t1."ExternalUtranCellFDD_id",
t1."hcsPrio",
t1."mnc",
t1."rncId",
t1."maximumAllowedUlTxPower",
t1."uarfcnUl",
t1."cellMode",
t1."primaryCpichPower",
t1."userLabel",
t1."qrxlevMin",
t1."mcc",
t1."lac",
t1."sttdSupportIndicator",
t1."qqualMin",
t1."uarfcnDl",
t1."controllingRnc",
t1."rac",
t1."deltaQrxlevmin",
t1."primaryScramblingCode",
t1."closedLoopMode1SuptInd",
t1."cId",
t2."vsDataExternalUtranCellFDD_id",
t2."offsetAngle",
t2."adjPreCodeResInd",
t2."adjCs64Switch",
t2."sharingMCC",
t2."dbSndCIdList",
t2."aResPara1",
t2."aResPara2",
t2."dCelDbMimoSupInd",
t2."aResPara3",
t2."edchHarqCombCap",
t2."aResPara4",
t2."aResPara5",
t2."gaRptType",
t2."aResPara6",
t2."aResPara7",
t2."aResPara8",
t2."aResPara9",
t2."qqualMinSib12",
t2."innerAngle",
t2."anteAltitude",
t2."cpcDtxDrxSuptInd",
t2."qrxlevMinSib12",
t2."adjPhyCId",
t2."iurDbHsdSuptInd",
t2."maxDtxCyc",
t2."polygonPointNum",
t2."polyLatitudeSign",
t2."iurDB4CMimoSptInd",
t2."nbrCodHsscch",
t2."iurMcHsdsSptInd",
t2."timeDelayJitter",
t2."adjClassZoneInd",
t2."polyLongitude",
t2."refUUtranRegArea",
t2."eFdpchSupInd",
t2."latitudeSign",
t2."pcpichPwrPre",
t2."anteAltitudeDir",
t2."maxNumofSndCell",
t2."edchSuptCgtDetInd",
t2."polyLatitude",
t2."mulEdchRestrt",
t2."aResPara10",
t2."cpcHslessSuptInd",
t2."dbSndSvrCelNum",
t2."iurDcHsuTrModInd",
t2."sharingMNC",
t2."mncLength",
t2."latitude",
t2."nrtMaxDlRateDchD",
t2."sndSvrCelIDList",
t2."backupAdjRncID",
t2."altitudeAcc",
t2."cellDescripType",
t2."iurDcHsuMulInd",
t2."adjImpUL2SuptInd",
t2."nrtMaxUlRateDchD",
t2."hspaSptMeth",
t2."snacNum",
t2."iurSB4CMimoSptInd",
t2."confidence",
t2."altitudeDir",
t2."edchTti2SuptInd",
t2."cellRadius",
t2."deltaQrxlevminPr",
t2."mimo64QamSuptInd",
t2."edchSfCap",
t2."ul16QamSuppInd",
t2."dpSttdPSMimoInd",
t2."altitude",
t2."rtMaxDlRateDchD",
t2."externalCellType",
t2."flexMacdSuptInd",
t2."hsdStat",
t2."longitude",
t2."utranGpsSptInd",
t2."rtMaxUlRateDchD",
t2."iurDcHsuSuptInd",
t2."timeDelay",
t2."hsdschSuptCgtDetInd",
t2."anteType",
t2."iurDcHsdsSuptInd",
t2."deltaQrxlevminSib12Pr",
t2."nbrCodHspdsch",
t2."fdpchSuptInd",
t2."anteLatitudeSign",
t2."uncertCode",
t2."nrtMaxRateEdchD",
t2."ePowBoostSuppInd",
t2."freqBandInd",
t2."dCelDcMimoSupInd",
t2."sac",
t2."deltaQrxlevminSib12",
t2."rtMaxRateEdchD",
t2."dl64QamSuptInd",
t2."backupAdjCellID",
t2."anteLatitude",
t2."sharingMNCLength",
t2."anteLongitude",
t2."snacList",
t2."mimoSuptInd",
t2."description",
t2."uncertAltitude"
FROM
zte_bulkcm_umts."ExternalUtranCellFDD" t1
INNER JOIN zte_bulkcm_umts."vsDataExternalUtranCellFDD" t2
 ON t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."ExternalRncFunction_id" = t2."ExternalRncFunction_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."ExternalUtranCellFDD_id" = t2."ExternalUtranCellFDD_id" 
 AND t1."FileName" = t2."FileName" 

"""
)

GsmRelation = ReplaceableObject(
    'zte_cm_3g."GsmRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."UtranCellFDD_id",
t1."GsmRelation_id",
t1."adjacentCell",
t1."userLabel",
t2."vsDataGsmRelation_id",
t2."blackListCellInd",
t2."ncToSelfPhyRnc",
t2."tempOffset1Sib11",
t2."tempOffset1Sib12",
t2."qoffset1SNSib11",
t2."qhcsSib11",
t2."qoffset1SNSib12",
t2."qhcsSib12",
t2."sib11orSib11bis",
t2."measPrio",
t2."gsmStateMode",
t2."whiteListCellInd",
t2."penaltyTimeSib11",
t2."penaltyTimeSib12",
t2."gsmShareCover",
t2."useOfHCS",
t2."description"
FROM
zte_bulkcm_umts."GsmRelation" t1
INNER JOIN zte_bulkcm_umts."vsDataGsmRelation" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."UtranCellFDD_id" = t2."UtranCellFDD_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."GsmRelation_id" = t2."GsmRelation_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 
 AND t1."FileName" = t2."FileName" 

"""
)

IubLink = ReplaceableObject(
    'zte_cm_3g."IubLink"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."IubLink_id",
t1."Bandwidth",
t1."iubLink-ATMChannelTerminationPoint",
t1."iubLinkUtranCell",
t1."iubLinkNodeBFunction",
t2."vsDataIubLink_id",
t2."NResPara2",
t2."NResPara3",
t2."NResPara4",
t2."NResPara5",
t2."NResPara6",
t2."NResPara7",
t2."NResPara8",
t2."NResPara9",
t2."NodeBInIPv4",
t2."CchIpDscp",
t2."Kpriadjust",
t2."NodeBInIPv6",
t2."NResPara10",
t2."NResPara11",
t2."NResPara12",
t2."NResPara13",
t2."NResPara14",
t2."NResPara15",
t2."InOrderInd",
t2."NResPara16",
t2."NResPara17",
t2."NResPara18",
t2."NResPara19",
t2."reservedByUUtranCellFDD",
t2."divContrlField",
t2."ceHighLdThr",
t2."sptDpiSpiChgInd",
t2."SrvBrsType",
t2."auditTimer",
t2."backupflag",
t2."NResPara20",
t2."ceShareSwitch",
t2."NResPara21",
t2."hsSharMethod",
t2."NResPara22",
t2."NResPara23",
t2."NResPara24",
t2."NResPara25",
t2."NResPara26",
t2."NResPara27",
t2."NResPara28",
t2."NResPara29",
t2."timeDelayJitter",
t2."reservedByUIpSlaExTask",
t2."NResPara30",
t2."NResPara31",
t2."NResPara32",
t2."NResPara33",
t2."edchSuptCgtDetInd",
t2."NResPara34",
t2."NResPara35",
t2."NResPara36",
t2."NResPara37",
t2."NResPara38",
t2."NResPara39",
t2."BandRelSwitch",
t2."MuxUdpPktMaxLen",
t2."oICSwitch",
t2."UdpMuxAMROverH",
t2."pmDlThptThreshClose",
t2."nodeBNo",
t2."reservedByUIpbm",
t2."NResPara40",
t2."pmUlThptThreshClose",
t2."InnerOmcbCliIPv4",
t2."InnerOmcbCliIPv6",
t2."PreCfgSwitch",
t2."NbapBrsType",
t2."IpSigRxBitRate",
t2."IpSigTxBitRate",
t2."DynamicBwCACSwit",
t2."IubPathProSwit",
t2."adjType",
t2."edchTdmSwch",
t2."pmUeNumThreshClose",
t2."MuxUdpSwitch",
t2."UdpMuxPort",
t2."NodeBBar",
t2."IubSigPathCongSwit",
t2."tIpRelLinkPro",
t2."CheckSumInd",
t2."tAtmRelLinkPro",
t2."backuprncId",
t2."FallbackDelay",
t2."DeMuxUdpSwitch",
t2."refAal2Ap",
t2."timeDelay",
t2."hsdschSuptCgtDetInd",
t2."Version",
t2."reservedByULogicalIubLink",
t2."celGrpCeChkSwch",
t2."ProVer",
t2."UdpMuxCS64OverH",
t2."nodeBType",
t2."noAuditRespTimes",
t2."FarEndBandAdjSwit",
t2."refModule",
t2."ceShareMode",
t2."userLabel",
t2."AneId",
t2."CchBrsType",
t2."tWaitNBReach",
t2."hsSharUptPrd",
t2."procInstancNo",
t2."description",
t2."UpQosMapType",
t2."NResPara1"
FROM
zte_bulkcm_umts."IubLink" t1
INNER JOIN zte_bulkcm_umts."vsDataIubLink" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 
 AND t1."IubLink_id" = t2."IubLink_id" 

"""
)

ManagedElement = ReplaceableObject(
    'zte_cm_3g."ManagedElement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "locationName",
        "ADMINISTRATIVESTATE",
        "userLabel",
        "MEADDR",
        "LATITUDE",
        "LONGITUDE",
        "userDefinedState",
        "vendorName",
        "swVersion",
        "PATCHINFO",
        "managedBy",
        "managedElementType",
        "LINKSTATE",
        "HARDWAREPLATFORM",
        "dnPrefix",
        "OPERATIONALSTATE"
    FROM
    zte_bulkcm_umts."ManagedElement"

    """
)

meContext = ReplaceableObject(
    'zte_cm_3g."meContext"',
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
    zte_bulkcm_umts."meContext"

    """
)

RncFunction = ReplaceableObject(
    'zte_cm_3g."RncFunction"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."mnc",
t1."rncid",
t1."userLabel",
t1."mcc",
t2."vsDataRncFunction_id",
t2."tRbRecfgCmpDtoF",
t2."fachToAWS",
t2."rncUlBlerHoSwch",
t2."tResndMeaCtrlRel",
t2."stopDsarCelInt",
t2."boardPwrOffHoTmr",
t2."mulEdchTrBearMod",
t2."nReTran",
t2."dnUdRecfgTimer",
t2."ueThdForEngCon",
t2."norDmpUserAcThd",
t2."nonCMinUlPduSize",
t2."pMCloseFunSwit",
t2."gResPara10",
t2."gResPara11",
t2."intraRatV1V2AmrCut",
t2."gResPara12",
t2."gResPara13",
t2."gResPara14",
t2."gResPara15",
t2."gResPara16",
t2."gResPara17",
t2."gResPara18",
t2."rncLcsOverIurSw",
t2."gResPara19",
t2."tWaitCelUpRlDact",
t2."tRrcSetupRetran",
t2."csNriBitNum",
t2."initRrcOnDch",
t2."gResPara20",
t2."utraSISwitch",
t2."plmnSelectMethod",
t2."maxCfgSatNum",
t2."sonTransRespNumThrd",
t2."cbsSwitch",
t2."berTargAdpTimer",
t2."tcnquery",
t2."n308",
t2."rncTxPwrHoSwch",
t2."tWaitActSetUpCmp",
t2."nonCMaxPduSize",
t2."intraHoRscpThrd",
t2."interRatV1V2AmrCut",
t2."numPeriodCreatCell",
t2."relocFastCfgInd",
t2."startDsarCelInt",
t2."sonTransReqPeriod",
t2."intraHoEcNoThrd",
t2."brdPwrOffWaitTim",
t2."celChgFastCfgInd",
t2."waitRbCompTimer",
t2."sirUpAddStep",
t2."gResPara41",
t2."gResPara42",
t2."reservedPsc",
t2."gResPara43",
t2."gResPara44",
t2."gResPara45",
t2."gResPara46",
t2."gResPara47",
t2."shaNetMaxInterNum",
t2."gResPara48",
t2."gResPara49",
t2."routeTypeUEBased",
t2."imeiBlackSwch",
t2."reservedByUPicoSonMeasCfg",
t2."rrcOnHsMc",
t2."coverMeaBalSwch",
t2."ueDrxInd",
t2."shaNetTarCelStra",
t2."hcsSupportInd",
t2."rabMeaBalStaSwch",
t2."gResPara50",
t2."gResPara51",
t2."gResPara52",
t2."gResPara53",
t2."gResPara54",
t2."gResPara55",
t2."maxCallCapability",
t2."gResPara56",
t2."gResPara57",
t2."gResPara58",
t2."ratCelInfoSwch",
t2."IucsIPCacInd",
t2."gResPara59",
t2."upUdRecfgTimer",
t2."pchToAWE",
t2."sonTransReqNumThrd",
t2."BscIurgSwitch",
t2."fastRetEUtranSwch",
t2."pchToAWS",
t2."norCmpUserAcThd",
t2."maxThroughput",
t2."partnerSrvPeriod",
t2."gResPara60",
t2."t4ShifIfLteGsmMea",
t2."psLoadCtlSwch",
t2."sharedNetMode",
t2."t321",
t2."partnerPendTime",
t2."tWaitCelUpUuExp",
t2."iuUlInSeqDlvInd",
t2."multicastSupInd",
t2."mnbThrdSelfOptm",
t2."uciuErrorOpSwch",
t2."fachLBSw",
t2."mulPlmnInMIBInd",
t2."ueThdForAttSwch",
t2."fastL1SyncSwch",
t2."dsarSwch",
t2."r99R4PchSwch",
t2."tWaitRlRestore",
t2."maxCsDelay",
t2."imeiPcFunSwitch",
t2."csThdForAttSwch",
t2."mscpoolBalanceNum",
t2."intRatHoMth",
t2."IupsCacInd",
t2."cMaxUlPduSize",
t2."deviceTypeInd",
t2."rrcSetupRetraNum",
t2."highPriAcSwch",
t2."gResPara1",
t2."emgCallRdtSwitch",
t2."gResPara2",
t2."rotAdjstSwch",
t2."gResPara3",
t2."gResPara4",
t2."gResPara5",
t2."gResPara6",
t2."gResPara7",
t2."gResPara8",
t2."gResPara9",
t2."measBalTimer",
t2."mbms128kRateSwitch",
t2."mbms32kRateSwitch",
t2."reservedByUCommEdch",
t2."vLacPaingInd",
t2."rncLdInPoolSwch",
t2."tiureldelay",
t2."dscrInCmnToDedSwch",
t2."csRrcOnFachSwch",
t2."maxRateWithNVHs",
t2."nonCMaxUlPduSize",
t2."parallelRrcSetup",
t2."mbms8kRateSwitch",
t2."discCNUpdReject",
t2."BscPsSwitch",
t2."tWaitRelCmd",
t2."mnbThrdSelfCfg",
t2."waitVoiceRbCompT",
t2."tWaitContextReq",
t2."rlFailureOpSwch",
t2."mbmsIurSupInd",
t2."tWaitDataFwd",
t2."cMaxPduSize",
t2."drxCycleLength",
t2."mbms64kRateSwitch",
t2."dpiPendingTime",
t2."locModeSwch",
t2."closeFreFunSwit",
t2."fltIncmpNbrCelSwit",
t2."reservedByUANR",
t2."iurPwrCtlReqSwch",
t2."bwOvldRelUeNum",
t2."tRrcConSetupExp",
t2."kUtran",
t2."gpsInfoRoot",
t2."paging1RspTimer",
t2."psL2USwchByCs",
t2."defPlmnInGwcnInd",
t2."BscDTMSwitch",
t2."reservedByURncInfo",
t2."dToHsDelayThr",
t2."mbms256kRateSwitch",
t2."onlyDnOnHB",
t2."fachCacToMinRate",
t2."partnerDataNum",
t2."totalDataNum",
t2."parallelSoftHO",
t2."heartBeatUeVerR4",
t2."heartBeatUeVerR5",
t2."heartBeatUeVerR6",
t2."heartBeatUeVerR7",
t2."heartBeatUeVerR8",
t2."stopDsarCelNum",
t2."interHoMth",
t2."mbms16kRateSwitch",
t2."appSrvDetcPrid",
t2."eBroadcastSupInd",
t2."cellLdInfoVldTim",
t2."heartBeatFreq",
t2."sgsnpoolBalanceNum",
t2."harqRvConfig",
t2."enhanceHoSwch",
t2."mnbSelfCfgSwch",
t2."ldBsdEutranHOInd",
t2."emiMeasInCDTSwch",
t2."amrGbrResInd",
t2."iurEcNoDelta",
t2."upaR99FarSwch",
t2."ProVer",
t2."tReCfgLevCmnStat",
t2."qChatSupportInd",
t2."cMinUlPduSize",
t2."sscopSmoothTime",
t2."rxBurstlength",
t2."validTimTbCovPrd",
t2."hsSrvChgUlStaJud",
t2."cdtOvdThd",
t2."dcRedirectStaSw",
t2."csThdForEngCon",
t2."reservedPscNum",
t2."loggedMDTSwitch",
t2."mnbSelfOptmSwch",
t2."reservedByUHspa",
t2."shareExLteSwch",
t2."fachToAWE",
t2."balFailOpSwch",
t2."sonTransRespSwitch",
t2."psNriBitNum",
t2."description",
t2."startDsarCelNum"
FROM
zte_bulkcm_umts."RncFunction" t1
INNER JOIN zte_bulkcm_umts."vsDataRncFunction" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 

"""
)

SubNetwork = ReplaceableObject(
    'zte_cm_3g."SubNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id"
    FROM
    zte_bulkcm_umts."SubNetwork"

    """
)

SubNetwork_2 = ReplaceableObject(
    'zte_cm_3g."SubNetwork_2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "setOfMcc",
        "userLabel",
        "userDefinedNetworkType",
        "dnPrefix"
    FROM
    zte_bulkcm_umts."SubNetwork_2"

    """
)

UtranCellFDD = ReplaceableObject(
    'zte_cm_3g."UtranCellFDD"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."UtranCellFDD_id",
t1."maximumTransmissionPower",
t1."maximumAllowedUlTxPower",
t1."pichPower",
t1."utranCellIubLink",
t1."cellIndividualOffset",
t1."lac",
t1."uarfcnDl",
t1."rac",
t1."sac",
t1."retAntennaFunctionList",
t1."closedLoopMode1SuptInd",
t1."cId",
t1."hcsPrio",
t1."secondarySchPower",
t1."uraList",
t1."uarfcnUl",
t1."cellMode",
t1."primaryCpichPower",
t1."localCellId",
t1."userLabel",
t1."restrictionStateIndicator",
t1."qrxlevMin",
t1."primarySchPower",
t1."pchPower",
t1."sttdSupportIndicator",
t1."qqualMin",
t1."deltaQrxlevmin",
t1."aichPower",
t1."primaryScramblingCode",
t1."bchPower",
t2."vsDataUtranCellFDD_id",
t2."offsetAngle",
t2."cs64Switch",
t2."refUUeIntMeasProfile",
t2."oCNSCode",
t2."bgNoiScene",
t2."hsTrafPrefInd",
t2."balanceScene",
t2."celDbMimoSupInd",
t2."ref1UAppPriMappingProfile",
t2."interHoTactic",
t2."innerAngle",
t2."pccpchInfSib6Pre",
t2."anteAltitude",
t2."sectorId",
t2."rscpQualThrd",
t2."r99PsTrafPrefInd",
t2."tutranGpsSptInd",
t2."suptMulUsDetInd",
t2."polygonPointNum",
t2."sharePichSwitch",
t2."hoCelSelScene",
t2."polyLatitudeSign",
t2."gARptType",
t2."useOfHCS",
t2."numOutSyncInd",
t2."hsuStat",
t2."dbHsdSuptInd",
t2."srvccCsRel2LteSw",
t2."refUSrvPcProfile",
t2."polyLongitude",
t2."refUInterMeasProfile",
t2."loadScene",
t2."qHcsEcNo",
t2."celMimo64QamInd",
t2."latitudeSign",
t2."tti2msSuptInd",
t2."celDbMcMimoSupInd",
t2."anteAltitudeDir",
t2."cellUniqueId",
t2."refUNbComMeasProfile",
t2."csHoRnReestSwitch",
t2."cellRadiusScene",
t2."polyLatitude",
t2."hsdschTrafLimit",
t2."csRsRnReestSwitch",
t2."backupCellID",
t2."psHoRnReestSwitch",
t2."efdpchSupInd",
t2."eutranNCblstSwch",
t2."reservedByUCelInfoFDD",
t2."ratHoTactic",
t2."psRsRnReestSwitch",
t2."refUSignalTraceCfg",
t2."refUTrvMeasProfile",
t2."latitude",
t2."nrtMaxDlRateDch",
t2."dlTpcN",
t2."rubRsvdCellInd",
t2."cellD2FLBSw",
t2."edchTrafLimit",
t2."prachSib6Pre",
t2."defSibSuptSwch",
t2."ref1UIntraMeasProfile",
t2."numInSyncInd",
t2."cellScen",
t2."cellP2FLBSw",
t2."nrtMaxUlRateDch",
t2."altitudeAcc",
t2."cellDescripType",
t2."csHoUeReestSwitch",
t2."pagingSendTimesCs",
t2."priRedirectRat",
t2."virtualLac",
t2."supt64QamInd",
t2."csRsUeReestSwitch",
t2."hspaSptMeth",
t2."psNumThrd2",
t2."csTrafPrefInd",
t2."sccpchCfgScene",
t2."confidence",
t2."altitudeDir",
t2."csfbCsRel2LteSw",
t2."refUSchPriMappingProfile",
t2."psHoUeReestSwitch",
t2."epchSpptInd",
t2."deltaQrxlevminPre",
t2."psRsUeReestSwitch",
t2."cellRadius",
t2."fourCHsdpaSptInd",
t2."reservedByULogicalCell",
t2."qHcsRSCP",
t2."sIB6Ind",
t2."csRcUeReestSwitch",
t2."ref2UIntraMeasProfile",
t2."refUDpiAppSrvProfile",
t2."csSsRnReestSwitch",
t2."celSbMcMimoSupInd",
t2."mbmsSuptInd",
t2."refUMPOProfile",
t2."detSetHoSwch",
t2."fDpchSuptInd",
t2."altitude",
t2."cpcSuptInd",
t2."psRcUeReestSwitch",
t2."psSsRnReestSwitch",
t2."fstCfgNum",
t2."hsupaIniEtti",
t2."hsdStat",
t2."longitude",
t2."sIB12Ind",
t2."ecNoQualThrd",
t2."ref2UAppPriMappingProfile",
t2."anteType",
t2."intraMeasQuan",
t2."cellType",
t2."ulBlerHoSwch",
t2."refUBPriAcProfile",
t2."refUServiceAreaBc",
t2."ulPwrHoSwch",
t2."anteLatitudeSign",
t2."sIB7Originator",
t2."csSsUeReestSwitch",
t2."freClosePri",
t2."rrcRdtSwch",
t2."dcHsupaSupptInd",
t2."uncertCode",
t2."freqBandInd",
t2."psSsUeReestSwitch",
t2."radioCapacity",
t2."sIB4Ind",
t2."refURatMeasProfile",
t2."tRlFailure",
t2."uLEFACHSupport",
t2."twait",
t2."scenarioType",
t2."anteLatitude",
t2."dcHsdschSupptInd",
t2."nonIntraMeasQuan",
t2."prachCfgScene",
t2."oCNSCodeNumber",
t2."mbmsStat",
t2."cellDcMimoSupInd",
t2."anteLongitude",
t2."dlPwrHoSwch",
t2."address",
t2."PagingSendTimesPs",
t2."penaltyTime",
t2."csNumThrd2",
t2."tCell",
t2."eFACHSpptInd",
t2."mimoSuptInd",
t2."classZoneInd",
t2."maxRateMD",
t2."description",
t2."celAvaSubCha",
t2."uncertAltitude"
FROM
zte_bulkcm_umts."UtranCellFDD" t1
INNER JOIN zte_bulkcm_umts."vsDataUtranCellFDD" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."UtranCellFDD_id" = t2."UtranCellFDD_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."FileName" = t2."FileName" 

"""
)

UtranRelation = ReplaceableObject(
    'zte_cm_3g."UtranRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."bulkCmConfigDataFile_schemaLocation",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."meContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."UtranCellFDD_id",
t1."UtranRelation_id",
t1."adjacentCell",
t1."userLabel",
t2."vsDataUtranRelation_id",
t2."tempOffset1Sib11",
t2."ncToSelfPhyRnc",
t2."tempOffset1Sib12",
t2."qoffset1SNSib11",
t2."qhcsEcN0Sib11",
t2."qoffset1SNSib12",
t2."qhcsEcN0Sib12",
t2."sb11orSib11bis",
t2."measPrio",
t2."stateMode",
t2."penaltyTimeSib11",
t2."qhcsRscpSib11",
t2."penaltyTimeSib12",
t2."shareCover",
t2."qhcsRscpSib12",
t2."blackListCellInd",
t2."tempOffset2Sib11",
t2."tempOffset2Sib12",
t2."qoffset2SNSib11",
t2."qoffset2SNSib12",
t2."whiteListCellInd",
t2."useOfHCS",
t2."description",
t2."cellIndivOffset"
FROM
zte_bulkcm_umts."UtranRelation" t1
INNER JOIN zte_bulkcm_umts."vsDataUtranRelation" t2
 ON t1."meContext_id" = t2."meContext_id" 
 AND t1."UtranCellFDD_id" = t2."UtranCellFDD_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."UtranRelation_id" = t2."UtranRelation_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 

"""
)

Aich = ReplaceableObject(
    'zte_cm_3g."Aich"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataAich_id",
        "aichTranTime",
        "userLabel",
        "commPhyChanelId",
        "description"
    FROM
    zte_bulkcm_umts."vsDataAich"

    """
)

AmrEvtTPUeInt = ReplaceableObject(
    'zte_cm_3g."AmrEvtTPUeInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "vsDataAmrEvtTPUeInt_id",
        "filterCoeff",
        "userLabel",
        "trigTime",
        "txPowerThres",
        "measEvtNum",
        "meaEvtId",
        "ueIntMCfgNo",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataAmrEvtTPUeInt"

    """
)

ANR = ReplaceableObject(
    'zte_cm_3g."ANR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataANR_id",
        "gsmRssiMinThrd",
        "anrMode",
        "cpichRscpMinThrd",
        "userLabel",
        "tWaitDelPicoNbrPrd",
        "tWaitDelMacNbrPrd",
        "cpichEcNoMinThrd",
        "description"
    FROM
    zte_bulkcm_umts."vsDataANR"

    """
)

AppPriMapping = ReplaceableObject(
    'zte_cm_3g."AppPriMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataAppPriMappingProfile_id",
        "vsDataAppPriMapping_id",
        "appPri",
        "userLabel",
        "basicPrio",
        "rateClass",
        "bearerType",
        "description",
        "direction"
    FROM
    zte_bulkcm_umts."vsDataAppPriMapping"

    """
)

AppPriMappingProfile = ReplaceableObject(
    'zte_cm_3g."AppPriMappingProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataAppPriMappingProfile_id",
        "intialAppPriUsingScene",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataAppPriMappingProfile"

    """
)

AppSrvType = ReplaceableObject(
    'zte_cm_3g."AppSrvType"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataAppSrvType_id",
        "arpQueuingAlowed",
        "dlGBR",
        "arpPremptionVul",
        "arpPremptionCap",
        "ulGBR",
        "arpPriorityLevel",
        "maxSduSize",
        "userLabel",
        "appSrvType",
        "basicPrio",
        "trafficClass",
        "description"
    FROM
    zte_bulkcm_umts."vsDataAppSrvType"

    """
)

BasPri = ReplaceableObject(
    'zte_cm_3g."BasPri"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataBasPri_id",
        "hspaEquHsUser",
        "hsNormBitRate",
        "userLabel",
        "dlNormBitRate",
        "maxUlDpchPO",
        "edchNormBitRate",
        "basicPrio",
        "ulNormBitRate",
        "maxDlDpchPO",
        "description"
    FROM
    zte_bulkcm_umts."vsDataBasPri"

    """
)

BasPriMapping = ReplaceableObject(
    'zte_cm_3g."BasPriMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataBasPriMapping_id",
        "basicPrio",
        "userLabel",
        "arpPL",
        "trafficClass",
        "description"
    FROM
    zte_bulkcm_umts."vsDataBasPriMapping"

    """
)

BPriAc = ReplaceableObject(
    'zte_cm_3g."BPriAc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataBPriAcProfile_id",
        "vsDataBPriAc_id",
        "hsdpaAcThresh",
        "dchDlAcThresh",
        "threshRefCount",
        "mbmsAcThresh",
        "dchUlAcThresh",
        "edchAcThresh",
        "userLabel",
        "ulEquUserCacThrd",
        "basicPrio",
        "codeTreeResRto",
        "description"
    FROM
    zte_bulkcm_umts."vsDataBPriAc"

    """
)

BPriAcProfile = ReplaceableObject(
    'zte_cm_3g."BPriAcProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataBPriAcProfile_id",
        "intialloadscene",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataBPriAcProfile"

    """
)

CelInfoFDD = ReplaceableObject(
    'zte_cm_3g."CelInfoFDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataCelInfoFDD_id",
        "highUserNumThr",
        "pORabHardHO",
        "dlHighLoadThr",
        "loggingDuration",
        "secTryBlidHoSw",
        "edchToDch6ASwch",
        "nbrCsNumThrd",
        "periodTriggerTime",
        "rtMaxRateEdch",
        "csPsbadCovRscp",
        "sfFLayerReference",
        "cellBarAcSwh",
        "pMUlCeMarginClose",
        "anrSelfCfgSwch",
        "dLEFACHUserNum",
        "pchCellSwch",
        "rsrvdBitRatePC",
        "eFachPchBandWidth",
        "uhpUsrRatTrigThd",
        "hsupaUhpJugTimes",
        "r99MaxPowerSwi",
        "simCompUserNum",
        "absPriReselSwch",
        "sAOffThs",
        "ulHighRateThr",
        "intMarginOpen",
        "rachMaxRptCell",
        "dlLowLoadThr",
        "freClsOpnTrigTm",
        "sAOffSuptInd",
        "nrtMaxRateEdch",
        "csPsbadCovEcN0",
        "plmnCodShaSwch",
        "r99PwrRatPlmnSwi",
        "hsdpaNumHigh",
        "badEdchCovEcNo",
        "pscValInd4SelfCfg",
        "ulCacSwitch",
        "startTimetoClsF",
        "psNumThrd1",
        "usedCnMngMDTSwch",
        "uhpUsrNumRecThd",
        "rtMaxUlRateDch",
        "sAOnThs",
        "nbrCeIIntactiveInd",
        "amrUlLdThrd",
        "csIntraEvtSwch",
        "pscSelfcfgSwch",
        "pMPowerMarginClose",
        "powerMarginClose",
        "ulLowLdThr",
        "forbTimAftOpnF",
        "openFreAlg",
        "csfbMulSrv2LteSw",
        "interNbrNumLimit",
        "pMIntMarginClose",
        "pcpiPwrDnTmWin",
        "codeMarginClose",
        "loggedMCUeAcqRto",
        "freCloseAllowedInd",
        "eNumMarginOpen",
        "addNRLSHOSwch",
        "choStraMulRatHo",
        "codeMarginOpen",
        "tcpOptSwitch",
        "anrValInd4SelfCfg",
        "pOReEstablish",
        "pathLoss",
        "sib18Ind",
        "epchPichNp",
        "anrSelfOptmSwch",
        "hsdpaNumLow",
        "defaultLoadLevel",
        "bmcSchMsgPrd",
        "ul16QamSwi",
        "ulRxGainTMA",
        "dlThrputSwitch",
        "rwaSwitch",
        "nodeBSafeThr",
        "cResPara1",
        "dpcchPcpLen",
        "cResPara2",
        "highRotThreshold",
        "cResPara3",
        "cResPara4",
        "cResPara5",
        "ueNumThreshCls",
        "cResPara6",
        "cResPara7",
        "cResPara8",
        "r99UlMinRat",
        "cResPara9",
        "intraRptQSib3",
        "pMCodeMarginClose",
        "servHoSwch",
        "interRatMIndPre",
        "nbrPsNumThrd",
        "pcpiPwrDnStepTm",
        "partnerCellSwch",
        "cellBarAcNum",
        "lowUserNumThr",
        "pMCloseGuardTime",
        "dlCtrlMBRSwitch",
        "traceId",
        "sccpchNp",
        "loggingInterval",
        "anrNbrCelRptRatio",
        "eNumMarginClose",
        "badEdchCovSwch",
        "pscSelfOptmSwch",
        "ulCeMarginOpen",
        "badCovRscp",
        "sATrigTime",
        "ulControledMBR",
        "sibSchuOptSwit",
        "eutranNbrCelHoRatio",
        "btnOfUptSIBCmp",
        "srbDelay",
        "cpichEcN0",
        "loggedMDTAreaType",
        "freClsCeEvaInd",
        "tcpStatSwitch",
        "coverPrd",
        "dpcchPoSecUlFre",
        "pMHsNumMarginClose",
        "bckNoiseAdjSwh",
        "cfnCompRscpThrd",
        "hsNumMarginClose",
        "pOSoftHO",
        "gsmNbrNumLimit",
        "cchFactor",
        "intMarginClose",
        "cfnCompEcNoThrd",
        "rtMaxDlRateDch",
        "dlCeMarginClose",
        "qpskInterpoCellSwch",
        "ulCtrlMBRSwitch",
        "tceId",
        "blerLoadSwitch",
        "qpskBoostCellSwch",
        "srvccMulSrv2LteSw",
        "dlLowLdThr",
        "cResPara10",
        "cResPara11",
        "cResPara12",
        "cResPara13",
        "cResPara14",
        "cResPara15",
        "cResPara16",
        "cResPara17",
        "cResPara18",
        "badCovEcN0",
        "cResPara19",
        "fddInterFMeasInd",
        "dch2FachRetLteSw",
        "pMENumMarginClose",
        "dlCacSwitch",
        "fachMeaOccaInfoInd",
        "intraNbrCelHoRatio",
        "cResPara20",
        "rrcSigUsrNumThr",
        "endTimetoClsF",
        "dlCeMarginOpen",
        "uhpUsrNumTrigThd",
        "lowRotThreshold",
        "dlControledMBR",
        "cbsFrameOffset",
        "amrDlLdThrd",
        "rsrvdBitRate",
        "ulCeMarginClose",
        "dlHighRateThr",
        "intraHardHoSw",
        "pcpiPwrDnStep",
        "pOSrbHardHO",
        "celLogMDTSwitch",
        "ettiRotThreshold",
        "rediNoMeasSw4E",
        "interHoMinThrdSw",
        "rediNoMeasSw4G",
        "maxR99DlPwrOffst",
        "closeFreAlg",
        "pOSetup",
        "syncRecfgCellSwch",
        "bmcSchMsgPrdPre",
        "dpiQosCellSwch",
        "ctchAllocPrd",
        "pMDlCeMarginClose",
        "cellSigMaxBR",
        "rediNoMeasSw4U",
        "userLabel",
        "badEdchCovRscp",
        "cellBarPollingSwh",
        "hsNumMarginOpen",
        "csNumThrd1",
        "ifOrRatHoSwch",
        "drxOnFachInd",
        "oriBckNoise",
        "gsmNbrCelHoRatio",
        "barInterval",
        "codeRsrvdCacSwch",
        "interNbrCelHoRatio",
        "description",
        "powerMarginOpen"
    FROM
    zte_bulkcm_umts."vsDataCelInfoFDD"

    """
)

CelSel = ReplaceableObject(
    'zte_cm_3g."CelSel"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataCelSel_id",
        "sHCSRat",
        "sHCSRatPre",
        "sSearchHCSPre",
        "cellRsvExt",
        "spSf",
        "sib3orSib4",
        "noHcsTCrMax",
        "cellBarredInd",
        "tReselectionFach",
        "tReselection",
        "noHcsNCr",
        "interRatSfPre",
        "sSearchRat",
        "qqulmnOffstPre",
        "sInterSearch",
        "sInterSearchPre",
        "tBarred",
        "tCrMaxHyst",
        "sIntraSearch",
        "qrxlvmnOffstPre",
        "qualMeas",
        "interFreqSfPre",
        "qHyst1SFach",
        "qHyst1S",
        "qqualminOffset",
        "hcsSrvCelInfoPre",
        "qHyst1SPch",
        "qHyst2SPch",
        "interRatSf",
        "sSearchHCS",
        "otherRATInfoPre",
        "acBarred",
        "tCrMax",
        "qHyst2SFach",
        "qHyst2S",
        "interFreqSf",
        "userLabel",
        "noHcsTCrMaxHyst",
        "tReselectionPch",
        "sIntraSearchPre",
        "spSfPre",
        "inFreqReselInd",
        "description",
        "nCr",
        "sLimitRat",
        "qrxlevminOffset"
    FROM
    zte_bulkcm_umts."vsDataCelSel"

    """
)

CfnOffset = ReplaceableObject(
    'zte_cm_3g."CfnOffset"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCfnOffset_id",
        "uuPktLenInd",
        "fstRecfgInd",
        "userLabel",
        "sigType",
        "description",
        "retranRate",
        "cfnOffset"
    FROM
    zte_bulkcm_umts."vsDataCfnOffset"

    """
)

CHspa = ReplaceableObject(
    'zte_cm_3g."CHspa"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataCHspa_id",
        "maxHspaPwrRto",
        "numofErgHich",
        "eRgHichUpThr",
        "hspdschPwr",
        "numofEagch",
        "codeUptHyA",
        "maxERgHichNum",
        "hsShareInd",
        "eCtrChCongIncSwh",
        "userNumPerEagch",
        "dpchCodeHy",
        "eAgchUpThr",
        "eRgHichDnThr",
        "rotAdjstlwrLmt",
        "nServToTotalPwr",
        "minNumofHspdsch",
        "ulDecHSDPARatSwch",
        "hspdschBitRate",
        "iurCdReAssDrop",
        "maxEAgchNum",
        "hspaPwrRatio",
        "numofHspdsch",
        "maxNumofHspdsch",
        "hsVsR99CdPriInd",
        "eAgchDnThr",
        "userLabel",
        "hsscchPwr",
        "rotAdjstUprLmt",
        "minHspaPwrRto",
        "dediComEAGCHSwi",
        "cEdchUserNum",
        "pcchTransNum",
        "cellUpaR99FarInd",
        "refUGbrResLimitProfile",
        "description",
        "numofHsscch",
        "hsNBAssInd",
        "maxRTWP"
    FROM
    zte_bulkcm_umts."vsDataCHspa"

    """
)

CMR = ReplaceableObject(
    'zte_cm_3g."CMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataCMR_id",
        "mrCellEdchPbrMeasSwit",
        "mrCellAppMeasSwit",
        "mrCellTcpMeasSwit",
        "mrCellTcpforHsMeasSwit",
        "userLabel",
        "mrCellGpsTimMeasSwit",
        "mrUeMeasSwit",
        "mrCelMRptIntCoef",
        "mrCellHsdschPbrMeasSwit",
        "mrCellNonServingRgdcMeasSwit",
        "mrCellRtwpMeasSwit",
        "description",
        "mrCellHsdschRpMeasSwit"
    FROM
    zte_bulkcm_umts."vsDataCMR"

    """
)

CnInfo = ReplaceableObject(
    'zte_cm_3g."CnInfo"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataCnInfo_id",
        "t3212Cs",
        "userLabel",
        "attIndCs",
        "kps",
        "cnDomain",
        "nmoPs",
        "kcs",
        "description",
        "mbmsModPrdCoeff"
    FROM
    zte_bulkcm_umts."vsDataCnInfo"

    """
)

ComEdchEvUpTrv = ReplaceableObject(
    'zte_cm_3g."ComEdchEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataComEdchEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataComEdchEvUpTrv"

    """
)

ComHsdschEvUpTrv = ReplaceableObject(
    'zte_cm_3g."ComHsdschEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataComHsdschEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataComHsdschEvUpTrv"

    """
)

CommEdch = ReplaceableObject(
    'zte_cm_3g."CommEdch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCommEdch_id",
        "ulEfachSF",
        "cqiPwrOffset",
        "cEdchHarqPOTti10",
        "scheInfoPOTti10",
        "cqiRepFactor",
        "cEchMxMcSizFix",
        "ettiComEdch",
        "nackPwrOffset",
        "scheInfoPOTti2",
        "cEdchHarqPOTti2",
        "userLabel",
        "happyBitDelCEdch",
        "ulLchTypeInd",
        "cqiCycle",
        "cEdchMaxRlcSize",
        "edchRefPO",
        "tpcErrTarget",
        "anackRepFactor",
        "edpcchPOTti10",
        "cEdchMultiSwi",
        "ackPwrOffset",
        "cEdchMaxRetrTti2",
        "cEdchMaxRetrTti10",
        "description",
        "edpcchPOTti2",
        "cEdchMinRlcSize"
    FROM
    zte_bulkcm_umts."vsDataCommEdch"

    """
)

CompressMode = ReplaceableObject(
    'zte_cm_3g."CompressMode"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCompressMode_id",
        "ulCMMethod",
        "ulDlMode",
        "K",
        "tgcfnOffset",
        "tgprc",
        "tgsn",
        "tgd",
        "deltaCFN",
        "deltaSIRafter1",
        "deltaSIRafter2",
        "dlFrameType",
        "tgpl1",
        "itp",
        "nidAbort",
        "userLabel",
        "deltaSIR1",
        "deltaSIR2",
        "rpp",
        "dlCMMethod",
        "tRecfgAbort",
        "measPurpose",
        "tgl1",
        "tgl2",
        "description"
    FROM
    zte_bulkcm_umts."vsDataCompressMode"

    """
)

CpuCtrlPri = ReplaceableObject(
    'zte_cm_3g."CpuCtrlPri"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCpuCtrlPri_id",
        "eventType",
        "userLabel",
        "description",
        "cpuLdCtrlPri",
        "serviceType"
    FROM
    zte_bulkcm_umts."vsDataCpuCtrlPri"

    """
)

DchEvUeTrv = ReplaceableObject(
    'zte_cm_3g."DchEvUeTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataDchEvUeTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres0",
        "rptThres1",
        "rptThres2",
        "rptThres3",
        "rptThres4",
        "rptThres5",
        "rptRlcBufInd",
        "rptThres6",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDchEvUeTrv"

    """
)

DchEvUpTrv = ReplaceableObject(
    'zte_cm_3g."DchEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataDchEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres0",
        "rptThres1",
        "rptThres2",
        "rptThres3",
        "rptThres4",
        "rptThres5",
        "rptRlcBufInd",
        "rptThres6",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDchEvUpTrv"

    """
)

DchPrdUeTrv = ReplaceableObject(
    'zte_cm_3g."DchPrdUeTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataDchPrdUeTrv_id",
        "ueTrvMCfgNo",
        "averageTime",
        "prdRptInterval",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "prdRptAmount",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDchPrdUeTrv"

    """
)

DedEdchEvUpTrv = ReplaceableObject(
    'zte_cm_3g."DedEdchEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataDedEdchEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDedEdchEvUpTrv"

    """
)

DedIBHsdschEvUpTrv = ReplaceableObject(
    'zte_cm_3g."DedIBHsdschEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataDedIBHsdschEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDedIBHsdschEvUpTrv"

    """
)

DedSHsdschEvUpTrv = ReplaceableObject(
    'zte_cm_3g."DedSHsdschEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataDedSHsdschEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDedSHsdschEvUpTrv"

    """
)

DedSrvTb = ReplaceableObject(
    'zte_cm_3g."DedSrvTb"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataDedSrvTbProfile_id",
        "vsDataDedSrvTb_id",
        "ipDscp",
        "tbType",
        "trafficCategory",
        "tbTypePara1",
        "userLabel",
        "tbTypePara2",
        "tbTypePara3",
        "tbTypePara4",
        "tbTypePara5",
        "tbTypePara6",
        "iBDlResBwd",
        "description",
        "iBUlResBwd"
    FROM
    zte_bulkcm_umts."vsDataDedSrvTb"

    """
)

DedSrvTbProfile = ReplaceableObject(
    'zte_cm_3g."DedSrvTbProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataDedSrvTbProfile_id",
        "intialTransportNetScene",
        "profileId",
        "templateType",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDedSrvTbProfile"

    """
)

DiamondUserGlobalPara = ReplaceableObject(
    'zte_cm_3g."DiamondUserGlobalPara"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDiamondUserGlobalPara_id",
        "dmdUeRrcSrb272Swch",
        "dmdOverBookPri",
        "mrBarSwch",
        "dmdPdcpDlBufLmt",
        "dmdUeRrcCongSwch",
        "userLabel",
        "dmdDlResBwd",
        "dmdUeLstSwitch",
        "dmdUserPwrOffset",
        "dmdOverBookPriSwch",
        "dmdExpPdcpBufSwch",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDiamondUserGlobalPara"

    """
)

DiamondUserImsiList = ReplaceableObject(
    'zte_cm_3g."DiamondUserImsiList"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDiamondUserImsiList_id",
        "csCgtSchPrio",
        "psHspaSchPrio",
        "imsiDgtNum",
        "psCgtSchPrio",
        "csAppPri",
        "imsiActiveInd",
        "csBasicPrio",
        "userLabel",
        "psAppPri",
        "psBasicPrio",
        "csHspaSchPrio",
        "imsiDgt",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDiamondUserImsiList"

    """
)

DiamondUserSrvPc = ReplaceableObject(
    'zte_cm_3g."DiamondUserSrvPc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSrvFunction_id",
        "vsDataDiamondUserSrvPc_id",
        "nhrThrDownTti10",
        "maxSirTargUpStep",
        "addiSIRDownStep",
        "blerAccpPeriod",
        "edchHarqPOFdd",
        "fpTargErrorTti10",
        "sirRapidConvSwi",
        "ulOlPcQESwchSil",
        "qePhyBerTarSil",
        "initBlerSIRTti10",
        "ulInitSIR",
        "ulSirStepTti10",
        "ulSirTargDnStep",
        "ulInitSIRTti2",
        "ulMinSIR",
        "berTargetDnThres",
        "fpTargErrorTti2",
        "nhrThrUpTti10",
        "ulMinSIRTti10",
        "nhrThrUpTti2",
        "ulMinSIRTti2",
        "ulSirTargUpStep",
        "berTargetUpThres",
        "ulSirStep",
        "nhrThrDownTti2",
        "ulInitSIRTti10",
        "initBlerSIR",
        "targetRetranNum",
        "ulMaxSIRTti10",
        "ulSirStepTti2",
        "dpcchPilotEbN0",
        "initBlerSIRTti2",
        "minDlDpchPwr",
        "swchAdaptiveStep",
        "ulMaxSIR",
        "srvType",
        "thrHarqFailTti10",
        "initSirAdd",
        "ulMaxSIRTti2",
        "thrHarqFailTti2",
        "initSirAddTti2",
        "errorThresh",
        "blerTarget",
        "userLabel",
        "maxDlDpchPwr",
        "maxSirTargDnStep",
        "berCntThres",
        "dwThrSampNumTti2",
        "initSirAddTti10",
        "upThrSampNumTti10",
        "qeCntThres",
        "upThrSampNumTti2",
        "description",
        "dwThrSampNumTti10",
        "maxUlDpchPwr"
    FROM
    zte_bulkcm_umts."vsDataDiamondUserSrvPc"

    """
)

Dpi = ReplaceableObject(
    'zte_cm_3g."Dpi"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDpi"

    """
)

DpiAlgParam = ReplaceableObject(
    'zte_cm_3g."DpiAlgParam"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "vsDataDpiAlgParam_id",
        "ref1UDpiProcMap",
        "VoipPaktDscdRto",
        "VideoImpSwitch",
        "VoipLwrQultSwitch",
        "VideoRateCoef",
        "VoipLwrQultUsrRto",
        "ref2UDpiProcMap",
        "userLabel",
        "refLocalPlmnGroup",
        "InitTransTimLnth",
        "P2pMaxRate",
        "P2pRateLmtSwitch",
        "description",
        "ref3UDpiProcMap"
    FROM
    zte_bulkcm_umts."vsDataDpiAlgParam"

    """
)

DpiAppSrv = ReplaceableObject(
    'zte_cm_3g."DpiAppSrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "vsDataDpiAppSrv_id",
        "AppSrvId",
        "AppSrvName",
        "reservedByUDpiDrbc",
        "userLabel",
        "reservedByUDpiAppSrvPri",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDpiAppSrv"

    """
)

DpiAppSrvPri = ReplaceableObject(
    'zte_cm_3g."DpiAppSrvPri"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "vsDataDpiAppSrvProfile_id",
        "vsDataDpiAppSrvPri_id",
        "refUDpiAppSrv",
        "AppSrvPri",
        "userLabel",
        "RprtDataRtoThr",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDpiAppSrvPri"

    """
)

DpiAppSrvProfile = ReplaceableObject(
    'zte_cm_3g."DpiAppSrvProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "vsDataDpiAppSrvProfile_id",
        "userLabel",
        "description",
        "APPCfgIndex"
    FROM
    zte_bulkcm_umts."vsDataDpiAppSrvProfile"

    """
)

DpiBasPriMapping = ReplaceableObject(
    'zte_cm_3g."DpiBasPriMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpiBasPriMapping_id",
        "BasicPrio",
        "userLabel",
        "AppSrvPriCls",
        "DpiBasicPrio",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDpiBasPriMapping"

    """
)

DpiDrbc = ReplaceableObject(
    'zte_cm_3g."DpiDrbc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataDpiDrbc_id",
        "refUDpiAppSrv",
        "refUDrbcProfile",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDpiDrbc"

    """
)

DpiPartnerIp = ReplaceableObject(
    'zte_cm_3g."DpiPartnerIp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "vsDataDpiPartnerName_id",
        "vsDataDpiPartnerIp_id",
        "PartnerIpAddr",
        "userLabel",
        "PartnerIpLenth",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDpiPartnerIp"

    """
)

DpiPartnerName = ReplaceableObject(
    'zte_cm_3g."DpiPartnerName"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "vsDataDpiPartnerName_id",
        "userLabel",
        "PartnerIndex",
        "refUDpiProcMap",
        "refPlmnGroup",
        "PartnerDomainName",
        "PartServiceType",
        "PriorityAdded",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDpiPartnerName"

    """
)

DpiProcMap = ReplaceableObject(
    'zte_cm_3g."DpiProcMap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDpi_id",
        "vsDataDpiProcMap_id",
        "ProcCounterId",
        "ProcName",
        "userLabel",
        "refUDpiAppSrv",
        "ProcId",
        "description",
        "DpiUsageType"
    FROM
    zte_bulkcm_umts."vsDataDpiProcMap"

    """
)

Drbc = ReplaceableObject(
    'zte_cm_3g."Drbc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDrbcProfile_id",
        "vsDataDrbc_id",
        "dxHsBo0E4bThd",
        "deltaNumE4B0Thd",
        "dchE4bThd",
        "fastToFtimesThr",
        "fachSwch",
        "ettiEbThd",
        "dtxdrxToFachThd",
        "dtcpEbThd",
        "pchHoldTimeThr",
        "dchE4aThd",
        "userLabel",
        "ettiEaThd",
        "dToFachThd",
        "dtcpEaThd",
        "dToPchThd",
        "fToIdleThd",
        "fToPchThd",
        "description",
        "dToIdleThd",
        "pchSwch",
        "fachE4aThd"
    FROM
    zte_bulkcm_umts."vsDataDrbc"

    """
)

DrbcProfile = ReplaceableObject(
    'zte_cm_3g."DrbcProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDrbcProfile_id",
        "profileId",
        "userLabel",
        "description",
        "drbcStragyName"
    FROM
    zte_bulkcm_umts."vsDataDrbcProfile"

    """
)

DtxDrx = ReplaceableObject(
    'zte_cm_3g."DtxDrx"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDtxDrxProfile_id",
        "vsDataDtxDrx_id",
        "dtxLongPreLegth",
        "dtxCyc2InactTrd10",
        "drxCycleTti10",
        "dtxCyc2InactTrd2",
        "gMonInactTrd2",
        "macDtxCycTti10",
        "burst2Tti10",
        "cqiDtxTimer",
        "drxGrantMon",
        "burst1Tti2",
        "dtxCyc2Tti10",
        "burst2Tti2",
        "drxCycInactTrd",
        "macDtxCycTti2",
        "macInaThre2",
        "drxCycleTti2",
        "userLabel",
        "macInaThre10",
        "dtxCyc1Tti2",
        "dtxCyc2Tti2",
        "burst1Tti10",
        "description",
        "dtxCyc1Tti10",
        "gMonInactTrd10"
    FROM
    zte_bulkcm_umts."vsDataDtxDrx"

    """
)

DtxDrxProfile = ReplaceableObject(
    'zte_cm_3g."DtxDrxProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDtxDrxProfile_id",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataDtxDrxProfile"

    """
)

EdchRcDch = ReplaceableObject(
    'zte_cm_3g."EdchRcDch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataEdchRcDchProfile_id",
        "vsDataEdchRcDch_id",
        "eplTti2T0",
        "rEtfcPO2T0QIp",
        "eplTti2T1",
        "eplTti2T2",
        "eplTti2T3",
        "rEtfcNumTti2T0",
        "rEtfcNumTti2T1",
        "rEtfcNumTti2T2",
        "rEtfcNumTti2T3",
        "rEtfci2T1QIp",
        "rEtfcNum2T1Qb",
        "rEtfciPOTti10T0",
        "rEtfciPOTti10T1",
        "rEtfcNumTti10T0",
        "rEtfcNumTti10T1",
        "rEtfcPO2T0Qb",
        "rEtfcNum10T1QIp",
        "rEtfci2T0Qb",
        "rEtfci2T0QIp",
        "rEtfciTti10T0",
        "rEtfciTti10T1",
        "rEtfcPO10T1QIp",
        "eplTti10T0",
        "eplTti10T1",
        "rEtfciPOTti2T0",
        "rEtfciTti2T0",
        "rEtfciPOTti2T1",
        "rEtfci10T1QIp",
        "rEtfcNum2T1QIp",
        "rEtfciPOTti2T2",
        "rEtfciTti2T1",
        "rEtfciPOTti2T3",
        "rEtfciTti2T2",
        "rEtfciTti2T3",
        "rEtfcNum10T0QIp",
        "rEtfcNum2T0Qb",
        "rEtfcPO10T0QIp",
        "rEtfcPO2T1Qb",
        "rEtfcPO2T1QIp",
        "userLabel",
        "etfciBstTti2T0",
        "etfciBstTti2T1",
        "etfciBstTti2T2",
        "etfciBstTti2T3",
        "rEtfci10T0QIp",
        "rEtfcNum2T0QIp",
        "rEtfci2T1Qb",
        "description"
    FROM
    zte_bulkcm_umts."vsDataEdchRcDch"

    """
)

EdchRcDchProfile = ReplaceableObject(
    'zte_cm_3g."EdchRcDchProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataEdchRcDchProfile_id",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataEdchRcDchProfile"

    """
)

EdchRcFach = ReplaceableObject(
    'zte_cm_3g."EdchRcFach"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataEdchRcFach_id",
        "eplTti10T0",
        "eplTti10T1",
        "eplTti2T0",
        "eplTti2T1",
        "rEtfcNumTti2T0",
        "rEtfcNumTti2T1",
        "rEtfciPOTti2T0",
        "rEtfciTti2T0",
        "rEtfciPOTti2T1",
        "rEtfciTti2T1",
        "rEtfciPOTti10T0",
        "rEtfciPOTti10T1",
        "rEtfcNumTti10T0",
        "rEtfcNumTti10T1",
        "userLabel",
        "rEtfciTti10T0",
        "rEtfciTti10T1",
        "description"
    FROM
    zte_bulkcm_umts."vsDataEdchRcFach"

    """
)

EdchtoDchUpTrv = ReplaceableObject(
    'zte_cm_3g."EdchtoDchUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataEdchtoDchUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "thoughThres",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataEdchtoDchUpTrv"

    """
)

EFach = ReplaceableObject(
    'zte_cm_3g."EFach"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataEFach_id",
        "pOPpe",
        "ulIntfCEdchInd",
        "tpcStepSizeEFach",
        "fdpchPwrEFach",
        "mPOEFach",
        "sirtargetCEdch",
        "maxEdchResCcch",
        "maxPeriCollResol",
        "addEdchTrBackOff",
        "edchTrConBackOff",
        "ackNackCqiSupInd",
        "userLabel",
        "ulIlPcAlgEFach",
        "ulEfachMaxrate",
        "commonEdchNum",
        "description",
        "maxBitRateCEdch"
    FROM
    zte_bulkcm_umts."vsDataEFach"

    """
)

EFachPch = ReplaceableObject(
    'zte_cm_3g."EFachPch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataEFachPch_id",
        "discardTimer",
        "dtCfgInd",
        "macehsQID",
        "mxMaccSizeFix",
        "treset",
        "chTypeInd",
        "userLabel",
        "spi",
        "mxMaccSizeFlx",
        "description",
        "macehsWinSize",
        "t1"
    FROM
    zte_bulkcm_umts."vsDataEFachPch"

    """
)

ETTIEdchEvUpTrv = ReplaceableObject(
    'zte_cm_3g."ETTIEdchEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataETTIEdchEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "thoughThres",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataETTIEdchEvUpTrv"

    """
)

EvtRttUeInt = ReplaceableObject(
    'zte_cm_3g."EvtRttUeInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "vsDataEvtRttUeInt_id",
        "filterCoeff",
        "userLabel",
        "trigTime",
        "measEvtNum",
        "txRxTDThres",
        "meaEvtId",
        "ueIntMCfgNo",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataEvtRttUeInt"

    """
)

FachEvUpTrv = ReplaceableObject(
    'zte_cm_3g."FachEvUpTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataFachEvUpTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataFachEvUpTrv"

    """
)

FTPInfoCfg = ReplaceableObject(
    'zte_cm_3g."FTPInfoCfg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataFullSignalTrace_id",
        "vsDataFTPInfoCfg_id",
        "NdsAsIPAddr",
        "userLabel",
        "NdsAsPort",
        "IpVersion",
        "UserName",
        "Password",
        "FtpType",
        "description"
    FROM
    zte_bulkcm_umts."vsDataFTPInfoCfg"

    """
)

FullSignalTrace = ReplaceableObject(
    'zte_cm_3g."FullSignalTrace"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataFullSignalTrace_id",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataFullSignalTrace"

    """
)

GbrResLimit = ReplaceableObject(
    'zte_cm_3g."GbrResLimit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataGbrResLimitProfile_id",
        "vsDataGbrResLimit_id",
        "hsGBRLev",
        "hsGBRLevNum",
        "userLabel",
        "description",
        "ueHsReqPwrUplim"
    FROM
    zte_bulkcm_umts."vsDataGbrResLimit"

    """
)

GbrResLimitProfile = ReplaceableObject(
    'zte_cm_3g."GbrResLimitProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataGbrResLimitProfile_id",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataGbrResLimitProfile"

    """
)

GloAc = ReplaceableObject(
    'zte_cm_3g."GloAc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataGloAc_id",
        "forcQueSwiAMR",
        "tTrueQForced",
        "userLabel",
        "forcQueSwiCS64",
        "tTrueQ",
        "qLength",
        "amrDnRateAcSwch",
        "description",
        "tTrueQReloc"
    FROM
    zte_bulkcm_umts."vsDataGloAc"

    """
)

HoEvtTPUeInt = ReplaceableObject(
    'zte_cm_3g."HoEvtTPUeInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "vsDataHoEvtTPUeInt_id",
        "filterCoeff",
        "userLabel",
        "trigTime",
        "txPowerThres",
        "measEvtNum",
        "meaEvtId",
        "ueIntMCfgNo",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataHoEvtTPUeInt"

    """
)

Hspa = ReplaceableObject(
    'zte_cm_3g."Hspa"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataHspa_id",
        "rncDlEnL2Ind",
        "interNackPwrOfst",
        "scheInfoPOTti10",
        "rncUlEnL2Ind",
        "codeUptPrdms",
        "interCqiPwrOfst",
        "rncMimo64QamInd",
        "interMacMicNackPO",
        "rtDtxSwch",
        "interMacMicAckPO",
        "ackPwrOffset",
        "rncHsR99CdPriInd",
        "rncMIMOInd",
        "rncSbMcMimoSupInd",
        "codeUptPrds",
        "cqiPwrOffset",
        "nrtDrxSwch",
        "poEhichSerRls10",
        "poEhichNoSerRl2",
        "dcOrDbHsdschSptInd",
        "rnc64QAMInd",
        "rangeofDpchTime",
        "scheInfoPOTti2",
        "hsdpaCmAssoMode",
        "rlcSizeSuptType",
        "poEhichNoSerRl10",
        "poEhichSerRls2",
        "anackRepFactor",
        "edpcchPOTti10",
        "hsupaCtrChUptPrd",
        "poErgchSerRls10",
        "hsdschTotPwrMeth",
        "edpcchPOTti2",
        "codeReAssPrd",
        "nrtDtxSwch",
        "poErgchNonSerRls",
        "dtxDrxSwch",
        "interAckPwrOfst",
        "codeUptPrdUnit",
        "ulRlcSizeSptType",
        "nackPwrOffset",
        "event1fHsInd",
        "nvHsscLessSwch",
        "rncEfdpchSupInd",
        "tpcErrTarget",
        "eagchPOUptSwch",
        "rncDcMimoSupInd",
        "poErgchSerRls2",
        "hsscLessSwch",
        "codeReAssInd",
        "rncFdpchSupInd",
        "t1d",
        "cqiRepFactor",
        "hsGBRLimitSwi",
        "chip256adjust",
        "hsdpaIurMBR",
        "interMacMicCqiPO",
        "userLabel",
        "rncDbMcMimoSupInd",
        "cqiCycle",
        "edchRefPO",
        "rtDrxSwch",
        "rncDbMimoSupInd",
        "hsupaCmAssoMode",
        "description"
    FROM
    zte_bulkcm_umts."vsDataHspa"

    """
)

InterEcNoEvMeasforE = ReplaceableObject(
    'zte_cm_3g."InterEcNoEvMeasforE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeaSrvSpec_id",
        "vsDataInterEcNoEvMeasforE_id",
        "trigTime",
        "measEvtNum",
        "wUsed",
        "meaEvtId",
        "interMeasCfgNo",
        "filterCoeff",
        "userLabel",
        "threshUsedFreq",
        "hysteresis",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterEcNoEvMeasforE"

    """
)

InterEcNoEvMeasforG = ReplaceableObject(
    'zte_cm_3g."InterEcNoEvMeasforG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeaSrvSpec_id",
        "vsDataInterEcNoEvMeasforG_id",
        "trigTime",
        "measEvtNum",
        "wUsed",
        "meaEvtId",
        "interMeasCfgNo",
        "filterCoeff",
        "userLabel",
        "threshUsedFreq",
        "hysteresis",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterEcNoEvMeasforG"

    """
)

InterEcNoEvMeasforU = ReplaceableObject(
    'zte_cm_3g."InterEcNoEvMeasforU"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeaSrvSpec_id",
        "vsDataInterEcNoEvMeasforU_id",
        "trigTime",
        "measEvtNum",
        "threshNoUsedFreq",
        "wUsed",
        "meaEvtId",
        "interMeasCfgNo",
        "filterCoeff",
        "userLabel",
        "threshUsedFreq",
        "wNoUsed",
        "hysteresis",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterEcNoEvMeasforU"

    """
)

InterEcNoPrdMeas = ReplaceableObject(
    'zte_cm_3g."InterEcNoPrdMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeasNoSrvSpec_id",
        "vsDataInterEcNoPrdMeas_id",
        "filterCoeff",
        "userLabel",
        "prdRptAmount",
        "prdRptInterval",
        "description",
        "interMeasCfgNo"
    FROM
    zte_bulkcm_umts."vsDataInterEcNoPrdMeas"

    """
)

InterMeasNoSrvSpec = ReplaceableObject(
    'zte_cm_3g."InterMeasNoSrvSpec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeasNoSrvSpec_id",
        "reservedByUInterEcNoPrdMeas",
        "reservedByUInterRscpPrdMeas",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterMeasNoSrvSpec"

    """
)

InterMeasProfile = ReplaceableObject(
    'zte_cm_3g."InterMeasProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "intialHoCelSelScene",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterMeasProfile"

    """
)

InterMeaSrvSpec = ReplaceableObject(
    'zte_cm_3g."InterMeaSrvSpec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeaSrvSpec_id",
        "userLabel",
        "reservedByUInterRscpEvMeasforE",
        "reservedByUInterEcNoEvMeasforU",
        "reservedByUInterRscpEvMeasforG",
        "srvCategory",
        "reservedByUInterRscpEvMeasforU",
        "description",
        "reservedByUInterEcNoEvMeasforE",
        "reservedByUInterEcNoEvMeasforG"
    FROM
    zte_bulkcm_umts."vsDataInterMeaSrvSpec"

    """
)

InterRscpEvMeasforE = ReplaceableObject(
    'zte_cm_3g."InterRscpEvMeasforE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeaSrvSpec_id",
        "vsDataInterRscpEvMeasforE_id",
        "trigTime",
        "measEvtNum",
        "wUsed",
        "meaEvtId",
        "interMeasCfgNo",
        "filterCoeff",
        "userLabel",
        "threshUsedFreq",
        "hysteresis",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterRscpEvMeasforE"

    """
)

InterRscpEvMeasforG = ReplaceableObject(
    'zte_cm_3g."InterRscpEvMeasforG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeaSrvSpec_id",
        "vsDataInterRscpEvMeasforG_id",
        "trigTime",
        "measEvtNum",
        "wUsed",
        "meaEvtId",
        "interMeasCfgNo",
        "filterCoeff",
        "userLabel",
        "threshUsedFreq",
        "hysteresis",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterRscpEvMeasforG"

    """
)

InterRscpEvMeasforU = ReplaceableObject(
    'zte_cm_3g."InterRscpEvMeasforU"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeaSrvSpec_id",
        "vsDataInterRscpEvMeasforU_id",
        "trigTime",
        "measEvtNum",
        "threshNoUsedFreq",
        "wUsed",
        "meaEvtId",
        "interMeasCfgNo",
        "filterCoeff",
        "userLabel",
        "threshUsedFreq",
        "wNoUsed",
        "hysteresis",
        "description"
    FROM
    zte_bulkcm_umts."vsDataInterRscpEvMeasforU"

    """
)

InterRscpPrdMeas = ReplaceableObject(
    'zte_cm_3g."InterRscpPrdMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataInterMeasProfile_id",
        "vsDataInterMeasNoSrvSpec_id",
        "vsDataInterRscpPrdMeas_id",
        "filterCoeff",
        "userLabel",
        "prdRptAmount",
        "prdRptInterval",
        "description",
        "interMeasCfgNo"
    FROM
    zte_bulkcm_umts."vsDataInterRscpPrdMeas"

    """
)

IntraEcNoEvMeas = ReplaceableObject(
    'zte_cm_3g."IntraEcNoEvMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasSrvSpec_id",
        "vsDataIntraEcNoEvMeas_id",
        "trigTime",
        "evtRptAmount",
        "measEvtNum",
        "meaEvtId",
        "intraMeasCfgNo",
        "filterCoeff",
        "rplcActThr",
        "rptDeactThr",
        "rptRange",
        "userLabel",
        "threshUsedFreq",
        "w",
        "hysteresis",
        "evtRptInterval",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIntraEcNoEvMeas"

    """
)

IntraEcNoEvMeasForD = ReplaceableObject(
    'zte_cm_3g."IntraEcNoEvMeasForD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasNoSrvSpec_id",
        "vsDataIntraEcNoEvMeasForD_id",
        "trigTime",
        "evtRptAmount",
        "intraMeasCfgNo",
        "filterCoeff",
        "rptDeactThr",
        "rptRange",
        "userLabel",
        "w",
        "hysteresis",
        "evtRptInterval",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIntraEcNoEvMeasForD"

    """
)

IntraEcNoPrdMeas = ReplaceableObject(
    'zte_cm_3g."IntraEcNoPrdMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasNoSrvSpec_id",
        "vsDataIntraEcNoPrdMeas_id",
        "filterCoeff",
        "userLabel",
        "prdRptAmount",
        "prdRptInterval",
        "description",
        "intraMeasCfgNo"
    FROM
    zte_bulkcm_umts."vsDataIntraEcNoPrdMeas"

    """
)

IntraMeasNoSrvSpec = ReplaceableObject(
    'zte_cm_3g."IntraMeasNoSrvSpec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasNoSrvSpec_id",
        "reservedByUIntraEcNoPrdMeas",
        "reservedByUIntraRscpPrdMeas",
        "userLabel",
        "description",
        "reservedByUIntraRscpEvMeasForD",
        "reservedByUIntraEcNoEvMeasForD"
    FROM
    zte_bulkcm_umts."vsDataIntraMeasNoSrvSpec"

    """
)

IntraMeasProfile = ReplaceableObject(
    'zte_cm_3g."IntraMeasProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "intialHoCelSelScene",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIntraMeasProfile"

    """
)

IntraMeasSrvSpec = ReplaceableObject(
    'zte_cm_3g."IntraMeasSrvSpec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasSrvSpec_id",
        "reservedByUIntraRscpEvMeas",
        "reservedByUIntraEcNoEvMeas",
        "srvCategory",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIntraMeasSrvSpec"

    """
)

IntraRscpEvMeas = ReplaceableObject(
    'zte_cm_3g."IntraRscpEvMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasSrvSpec_id",
        "vsDataIntraRscpEvMeas_id",
        "trigTime",
        "evtRptAmount",
        "measEvtNum",
        "meaEvtId",
        "intraMeasCfgNo",
        "filterCoeff",
        "rplcActThr",
        "rptDeactThr",
        "rptRange",
        "userLabel",
        "threshUsedFreq",
        "w",
        "hysteresis",
        "evtRptInterval",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIntraRscpEvMeas"

    """
)

IntraRscpEvMeasForD = ReplaceableObject(
    'zte_cm_3g."IntraRscpEvMeasForD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasNoSrvSpec_id",
        "vsDataIntraRscpEvMeasForD_id",
        "trigTime",
        "evtRptAmount",
        "intraMeasCfgNo",
        "filterCoeff",
        "rptDeactThr",
        "rptRange",
        "userLabel",
        "w",
        "hysteresis",
        "evtRptInterval",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIntraRscpEvMeasForD"

    """
)

IntraRscpPrdMeas = ReplaceableObject(
    'zte_cm_3g."IntraRscpPrdMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIntraMeasProfile_id",
        "vsDataIntraMeasNoSrvSpec_id",
        "vsDataIntraRscpPrdMeas_id",
        "filterCoeff",
        "userLabel",
        "prdRptAmount",
        "prdRptInterval",
        "description",
        "intraMeasCfgNo"
    FROM
    zte_bulkcm_umts."vsDataIntraRscpPrdMeas"

    """
)

Ipbm = ReplaceableObject(
    'zte_cm_3g."Ipbm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIpbm_id",
        "LostRefValue",
        "refUIupsLink",
        "refUIubLink",
        "BandIncPer",
        "MinRxBitRate",
        "MinTxBitRate",
        "BandIncQuickPer",
        "refUIurLink",
        "userLabel",
        "BandDecPer",
        "refUIucsLink",
        "description",
        "refUIurgLink"
    FROM
    zte_bulkcm_umts."vsDataIpbm"

    """
)

IpLicense = ReplaceableObject(
    'zte_cm_3g."IpLicense"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIpLicense_id",
        "userLabel",
        "IubIpFlag",
        "IurIpFlag",
        "description",
        "IucsIpFlag"
    FROM
    zte_bulkcm_umts."vsDataIpLicense"

    """
)

IpSlaExTask = ReplaceableObject(
    'zte_cm_3g."IpSlaExTask"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIpSlaExTask_id",
        "DestIpAgetime",
        "DstPort",
        "refUIupsLink",
        "DstIpVersion",
        "refUIubLink",
        "PktType",
        "refUIurLink",
        "TimeOut",
        "IpDscp",
        "Interval",
        "IpSlaMonitorInd",
        "userLabel",
        "DstIp",
        "refUPlmnSpecFunction",
        "MidFlag",
        "refUIucsLink",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIpSlaExTask"

    """
)

IubTrPath = ReplaceableObject(
    'zte_cm_3g."IubTrPath"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIubLink_id",
        "vsDataIubTrPath_id",
        "DestIpMaskLen",
        "NRtRxResRatio",
        "RxBitRate",
        "TxBitRate",
        "IpDomainNo",
        "SigRsvBandWidth",
        "DestIpVersion",
        "refSubTrPathGroup",
        "DestIpAddr",
        "refModule",
        "RTSelFactor",
        "userLabel",
        "RtTxResRatio",
        "NResPara",
        "RtRxResRatio",
        "refAal2PathTp",
        "description",
        "TrPathSeq",
        "TrPathType",
        "IpBandAdjSwitch",
        "NRtTxResRatio"
    FROM
    zte_bulkcm_umts."vsDataIubTrPath"

    """
)

IubTrPathCir = ReplaceableObject(
    'zte_cm_3g."IubTrPathCir"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIubLink_id",
        "vsDataIubTrPath_id",
        "vsDataIubTrPathCir_id",
        "RatioTrPathGroup",
        "userLabel",
        "refTrPathGroup",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIubTrPathCir"

    """
)

IuCnst = ReplaceableObject(
    'zte_cm_3g."IuCnst"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataIuCnst_id",
        "tRafc",
        "tRelocprep",
        "tResetDelay",
        "nRepeatrst",
        "tRelocoverall",
        "tinTR",
        "tDrRetryRelocDelay",
        "nRepeatresrst",
        "userLabel",
        "tResetwait",
        "tRatc",
        "tDatafwd",
        "tigOR",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIuCnst"

    """
)

IucsLink = ReplaceableObject(
    'zte_cm_3g."IucsLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIucsLink_id",
        "NResPara2",
        "NResPara3",
        "NResPara4",
        "NResPara5",
        "NResPara6",
        "RtpMuxCS64OverH",
        "reservedByULogicalMscLink",
        "NResPara7",
        "NResPara8",
        "NResPara9",
        "Kpriadjust",
        "AddDelayJitter",
        "NResPara10",
        "NResPara11",
        "NResPara12",
        "NResPara13",
        "NResPara14",
        "NResPara15",
        "InOrderInd",
        "NResPara16",
        "NResPara17",
        "NResPara18",
        "NResPara19",
        "SrvBrsType",
        "InitFrameNum",
        "NResPara20",
        "NResPara21",
        "NResPara22",
        "NResPara23",
        "RtcpInterval",
        "NResPara24",
        "AddTimeDelay",
        "NResPara25",
        "NResPara26",
        "NResPara27",
        "NResPara28",
        "NResPara29",
        "reservedByUIpSlaExTask",
        "NResPara30",
        "NResPara31",
        "NResPara32",
        "NResPara33",
        "NResPara34",
        "NResPara35",
        "NResPara36",
        "NResPara37",
        "NResPara38",
        "BandRelSwitch",
        "NResPara39",
        "MuxUdpPktMaxLen",
        "RtcpSwitch",
        "reservedByUIpbm",
        "NResPara40",
        "RTPMUXPLType",
        "DynamicBwCACSwit",
        "MuxUdpSwitch",
        "RtpMuxAMROverH",
        "CnLdRemoveInd",
        "CheckSumInd",
        "reservedByULogicalMgwLink",
        "DeMuxUdpSwitch",
        "refAal2Ap",
        "RtpPayloadType",
        "ProVer",
        "userLabel",
        "AneId",
        "refRemoteSp",
        "description",
        "NResPara1"
    FROM
    zte_bulkcm_umts."vsDataIucsLink"

    """
)

IupsLink = ReplaceableObject(
    'zte_cm_3g."IupsLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIupsLink_id",
        "NResPara2",
        "NResPara3",
        "NResPara4",
        "NResPara5",
        "NResPara6",
        "NResPara7",
        "NResPara8",
        "NResPara9",
        "Kpriadjust",
        "AddDelayJitter",
        "NResPara10",
        "NResPara11",
        "NResPara12",
        "NResPara13",
        "NResPara14",
        "NResPara15",
        "InOrderInd",
        "NResPara16",
        "NResPara17",
        "NResPara18",
        "NResPara19",
        "SrvBrsType",
        "NResPara20",
        "NResPara21",
        "NResPara22",
        "NResPara23",
        "NResPara24",
        "NResPara25",
        "AddTimeDelay",
        "NResPara26",
        "NResPara27",
        "NResPara28",
        "NResPara29",
        "reservedByUIpSlaExTask",
        "NResPara30",
        "NResPara31",
        "NResPara32",
        "NResPara33",
        "NResPara34",
        "NResPara35",
        "NResPara36",
        "NResPara37",
        "NResPara38",
        "BandRelSwitch",
        "NResPara39",
        "reservedByUIpbm",
        "NResPara40",
        "LteCellIdenFlag",
        "reservedByULogicalIupsLink",
        "DynamicBwCACSwit",
        "SupportDTSwitch",
        "CnLdRemoveInd",
        "CheckSumInd",
        "refAal2Ap",
        "ProVer",
        "userLabel",
        "AneId",
        "refRemoteSp",
        "description",
        "NResPara1"
    FROM
    zte_bulkcm_umts."vsDataIupsLink"

    """
)

IupsTrPath = ReplaceableObject(
    'zte_cm_3g."IupsTrPath"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIupsLinkGroup_id",
        "vsDataLogicalIupsLink_id",
        "vsDataIupsTrPath_id",
        "DestIpMaskLen",
        "NRtRxResRatio",
        "RxBitRate",
        "TxBitRate",
        "SigRsvBandWidth",
        "DestIpVersion",
        "refSubTrPathGroup",
        "DestIpAddr",
        "refModule",
        "RTSelFactor",
        "userLabel",
        "RtTxResRatio",
        "NResPara",
        "RtRxResRatio",
        "description",
        "TrPathSeq",
        "TrPathType",
        "NRtTxResRatio",
        "IpBandAdjSwitch"
    FROM
    zte_bulkcm_umts."vsDataIupsTrPath"

    """
)

IupsTrPathCir = ReplaceableObject(
    'zte_cm_3g."IupsTrPathCir"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIupsLinkGroup_id",
        "vsDataLogicalIupsLink_id",
        "vsDataIupsTrPath_id",
        "vsDataIupsTrPathCir_id",
        "refTrPathGroup",
        "userLabel",
        "RatioTrPathGroup",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIupsTrPathCir"

    """
)

IurgLink = ReplaceableObject(
    'zte_cm_3g."IurgLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIurgLink_id",
        "NResPara2",
        "NResPara3",
        "NResPara4",
        "NResPara5",
        "NResPara6",
        "NResPara7",
        "NResPara8",
        "NResPara9",
        "Kpriadjust",
        "NResPara10",
        "NResPara11",
        "NResPara12",
        "NResPara13",
        "NResPara14",
        "NResPara15",
        "InOrderInd",
        "NResPara16",
        "NResPara17",
        "NResPara18",
        "NResPara19",
        "CheckSumInd",
        "SrvBrsType",
        "reservedByULogicalIurgLink",
        "NResPara20",
        "NResPara21",
        "NResPara22",
        "NResPara23",
        "NResPara24",
        "NResPara25",
        "NResPara26",
        "NResPara27",
        "NResPara28",
        "NResPara29",
        "NResPara30",
        "NResPara31",
        "BSCDTMFeatSwitch",
        "NResPara32",
        "NResPara33",
        "NResPara34",
        "NResPara35",
        "NResPara36",
        "ProVer",
        "NResPara37",
        "NResPara38",
        "BandRelSwitch",
        "NResPara39",
        "IurgFeatSwitch",
        "reservedByUIpbm",
        "userLabel",
        "NResPara40",
        "AneId",
        "refRemoteSp",
        "BSCPSFeatSwitch",
        "description",
        "NResPara1"
    FROM
    zte_bulkcm_umts."vsDataIurgLink"

    """
)

IurLink = ReplaceableObject(
    'zte_cm_3g."IurLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIurLink_id",
        "NResPara2",
        "RncFeatSwitchBit11",
        "NResPara3",
        "RncFeatSwitchBit12",
        "NResPara4",
        "RncFeatSwitchBit13",
        "NResPara5",
        "RncFeatSwitchBit14",
        "NResPara6",
        "RncFeatSwitchBit15",
        "NResPara7",
        "PoolUpOverThd",
        "RncFeatSwitchBit16",
        "NResPara8",
        "RncFeatSwitchBit17",
        "NResPara9",
        "RncFeatSwitchBit18",
        "RncFeatSwitchBit19",
        "Kpriadjust",
        "NResPara10",
        "NResPara11",
        "NResPara12",
        "NResPara13",
        "NResPara14",
        "NResPara15",
        "InOrderInd",
        "NResPara16",
        "NResPara17",
        "NResPara18",
        "NResPara19",
        "RncFeatSwitchBit20",
        "RncFeatSwitchBit21",
        "RncFeatSwitchBit22",
        "RncFeatSwitchBit23",
        "RncFeatSwitchBit24",
        "RncFeatSwitchBit25",
        "RncFeatSwitchBit26",
        "RncFeatSwitchBit27",
        "SrvBrsType",
        "RncFeatSwitchBit28",
        "RncFeatSwitchBit29",
        "NResPara20",
        "NResPara21",
        "SptAal2Switch",
        "NResPara22",
        "NResPara23",
        "NResPara24",
        "NResPara25",
        "NResPara26",
        "NResPara27",
        "NResPara28",
        "NResPara29",
        "reservedByUIpSlaExTask",
        "RncLdValidTime",
        "NResPara30",
        "TransSyncFlag",
        "NResPara31",
        "RncFeatSwitchBit0",
        "NResPara32",
        "RncFeatSwitchBit1",
        "NResPara33",
        "RncFeatSwitchBit2",
        "NResPara34",
        "RncFeatSwitchBit3",
        "NResPara35",
        "RncFeatSwitchBit4",
        "NResPara36",
        "RncFeatSwitchBit5",
        "NResPara37",
        "RncFeatSwitchBit6",
        "DchIdOffset",
        "RncFeatSwitchBit7",
        "NResPara38",
        "BandRelSwitch",
        "RncFeatSwitchBit8",
        "NResPara39",
        "RncFeatSwitchBit9",
        "reservedByUExternalRncFunction",
        "reservedByUIpbm",
        "NResPara40",
        "DynamicBwCACSwit",
        "CheckSumInd",
        "iurLinkRncFunction",
        "refAal2Ap",
        "Version",
        "CsReDelayTimer",
        "reservedByULogicalIurLink",
        "ProVer",
        "PsReDelayTimer",
        "reservedByULogicalIurQos",
        "LdShareMethod",
        "NodeSyncFlag",
        "userLabel",
        "PoolCpOverThd",
        "AneId",
        "refRemoteSp",
        "UpQosMapType",
        "description",
        "NResPara1",
        "RncFeatSwitchBit10"
    FROM
    zte_bulkcm_umts."vsDataIurLink"

    """
)

IurTrPath = ReplaceableObject(
    'zte_cm_3g."IurTrPath"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnAdjFunction_id",
        "vsDataLogicalIurLink_id",
        "vsDataIurTrPath_id",
        "DestIpMaskLen",
        "NRtRxResRatio",
        "RxBitRate",
        "TxBitRate",
        "SigRsvBandWidth",
        "DestIpVersion",
        "refSubTrPathGroup",
        "DestIpAddr",
        "refModule",
        "RTSelFactor",
        "userLabel",
        "RtTxResRatio",
        "NResPara",
        "RtRxResRatio",
        "refAal2PathTp",
        "description",
        "TrPathSeq",
        "TrPathType",
        "NRtTxResRatio",
        "IpBandAdjSwitch"
    FROM
    zte_bulkcm_umts."vsDataIurTrPath"

    """
)

IurTrPathCir = ReplaceableObject(
    'zte_cm_3g."IurTrPathCir"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnAdjFunction_id",
        "vsDataLogicalIurLink_id",
        "vsDataIurTrPath_id",
        "vsDataIurTrPathCir_id",
        "RatioTrPathGroup",
        "userLabel",
        "refTrPathGroup",
        "description"
    FROM
    zte_bulkcm_umts."vsDataIurTrPathCir"

    """
)

LdCtrl = ReplaceableObject(
    'zte_cm_3g."LdCtrl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataLdCtrl_id",
        "aglLdDec",
        "ceLoadLowThd",
        "decRateSw",
        "tCPLoadHighThd",
        "mbmsUNumLowThd",
        "rtwpLoadHighThd",
        "swchFachDrbcHspa",
        "ulRecoverLdThr",
        "ulMaxForHoNum",
        "psDlLoadCtlThr",
        "dlMaxDrpUsrNum",
        "dlLdCtrlDropSw",
        "maxNumUeOfDecRat",
        "tCPLoadMidThd",
        "forceHoSw",
        "codeLoadMidThd",
        "sigUNumLowThd",
        "psDlRecoverLdThr",
        "dpaUNumMidThd",
        "ulMaxDecStg",
        "hsdschOverLdThr",
        "uPAUNumLowThd",
        "psUlLoadCtlThr",
        "rtwpLoadMidThd",
        "dlRecoverLdThr",
        "ceLoadMidThd",
        "dlMaxForHoNum",
        "switchToFachSw",
        "mbmsUNumMidThd",
        "ulMaxEttiSwiUrNum",
        "forceRabRelSw",
        "hsdschRecoverThr",
        "dlLdCtrlDecRateSw",
        "ulOverLdThr",
        "dlMaxDecStg",
        "forceRabtoFASw",
        "ulLdCtrlDecRateSw",
        "psLoadCtlSwch",
        "tCPLoadLowThd",
        "psLCDsarSwch",
        "dlAdjustMFPSw",
        "ulMaxDrpUsrNum",
        "dlOverLdThr",
        "ulLdCtrlDropSw",
        "codeLoadLowThd",
        "dlSeriousOverLdThr",
        "decGbrSw",
        "dpaUNumLowThd",
        "ulSeriousOverLdThr",
        "userLabel",
        "sigUNumMidThd",
        "dlLdCtrlForceHoSw",
        "ulEttiSwiSw",
        "nFach",
        "maxGbrDecNum",
        "description",
        "ulLdCtrlForceHoSw",
        "psUlRecoverLdThr",
        "rtwpLoadLowThd",
        "uPAUNumMidThd"
    FROM
    zte_bulkcm_umts."vsDataLdCtrl"

    """
)

LocationArea = ReplaceableObject(
    'zte_cm_3g."LocationArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataLocationArea_id",
        "reservedByUSnac",
        "userLabel",
        "description",
        "lac"
    FROM
    zte_bulkcm_umts."vsDataLocationArea"

    """
)

LogicalCell = ReplaceableObject(
    'zte_cm_3g."LogicalCell"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalCell_id",
        "accessPercent",
        "pSDsarSwh",
        "lar2SmlCovBHoCelSw",
        "csDsarSwh",
        "plmnCodShaRat",
        "commonPlmnInd",
        "pagingLocaBarSwh",
        "cSBarAcNum",
        "pSDsarPollingSwh",
        "refUUtranCellFDD",
        "userLabel",
        "r99PwrPercent",
        "PsACBarredOmcr",
        "csDsarPollingSwh",
        "pSBarAcNum",
        "description",
        "csACBarredOmcr"
    FROM
    zte_bulkcm_umts."vsDataLogicalCell"

    """
)

LogicalIubLink = ReplaceableObject(
    'zte_cm_3g."LogicalIubLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIubLink_id",
        "minCEPercent",
        "refUDedSrvTbProfile",
        "userLabel",
        "description",
        "refUIubLink",
        "refUTbTypeProfile"
    FROM
    zte_bulkcm_umts."vsDataLogicalIubLink"

    """
)

LogicalIupsLink = ReplaceableObject(
    'zte_cm_3g."LogicalIupsLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIupsLinkGroup_id",
        "vsDataLogicalIupsLink_id",
        "IpDscpForTHP6",
        "IpDscpForTHP7",
        "IpDscpForTHP8",
        "IpDscpForTHP9",
        "NumOfNri",
        "refUIupsLink",
        "PreferInd",
        "IpDscpForTHP10",
        "IpDscpForTHP11",
        "IpDscpForTHP12",
        "IpDscpForTHP13",
        "IpDscpForTHP14",
        "IpDscpForTHP15",
        "NriList",
        "SgsnId",
        "PsPoolId",
        "IpDscpForB",
        "IpDscpForC",
        "IpDscpForI",
        "userLabel",
        "IpDscpForS",
        "CapacityWeight",
        "IpDscpForTHP1",
        "IpDscpForTHP2",
        "description",
        "IpDscpForTHP3",
        "IpDscpForTHP4",
        "DefaultInd",
        "IpDscpForTHP5"
    FROM
    zte_bulkcm_umts."vsDataLogicalIupsLink"

    """
)

LogicalIupsLinkGroup = ReplaceableObject(
    'zte_cm_3g."LogicalIupsLinkGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIupsLinkGroup_id",
        "refULogicalIupsLink",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataLogicalIupsLinkGroup"

    """
)

LogicalIurgLink = ReplaceableObject(
    'zte_cm_3g."LogicalIurgLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnAdjFunction_id",
        "vsDataLogicalIurgLink_id",
        "userLabel",
        "description",
        "refUIurgLink",
        "BSCId"
    FROM
    zte_bulkcm_umts."vsDataLogicalIurgLink"

    """
)

LogicalIurLink = ReplaceableObject(
    'zte_cm_3g."LogicalIurLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnAdjFunction_id",
        "vsDataLogicalIurLink_id",
        "RncId",
        "userLabel",
        "description",
        "refUIurLink"
    FROM
    zte_bulkcm_umts."vsDataLogicalIurLink"

    """
)

LogicalIurQos = ReplaceableObject(
    'zte_cm_3g."LogicalIurQos"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalIurQos_id",
        "refUDedSrvTbProfile",
        "userLabel",
        "description",
        "refUIurLink",
        "refUTbTypeProfile"
    FROM
    zte_bulkcm_umts."vsDataLogicalIurQos"

    """
)

LogicalMgwLink = ReplaceableObject(
    'zte_cm_3g."LogicalMgwLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalMgwLink_id",
        "refUIucsLink",
        "MgwId",
        "userLabel",
        "description",
        "IpDscpForC"
    FROM
    zte_bulkcm_umts."vsDataLogicalMgwLink"

    """
)

LogicalMscLink = ReplaceableObject(
    'zte_cm_3g."LogicalMscLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalMscLinkGroup_id",
        "vsDataLogicalMscLink_id",
        "NriList",
        "CsPoolId",
        "NumOfNri",
        "PreferInd",
        "userLabel",
        "MscsId",
        "CapacityWeight",
        "refUIucsLink",
        "description",
        "DefaultInd"
    FROM
    zte_bulkcm_umts."vsDataLogicalMscLink"

    """
)

LogicalMscLinkGroup = ReplaceableObject(
    'zte_cm_3g."LogicalMscLinkGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalMscLinkGroup_id",
        "refULogicalMscLink",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataLogicalMscLinkGroup"

    """
)

LogicalRnc = ReplaceableObject(
    'zte_cm_3g."LogicalRnc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalRnc_id",
        "dtmSuppInd",
        "ettiUePwrSwch",
        "qosNegRenegSw",
        "agpsLcsMethodInd",
        "pchToOtherTVISw",
        "hsdpaEutraHoSw",
        "psConvTraSupInd",
        "nQchatRel4B0Times",
        "dynaUpdtPO2Sw",
        "cRateThrd",
        "amrNbMode7UseTag",
        "amrWbMode5UseTag",
        "dpiDrbcSwch",
        "punishUePchSwch",
        "rrach",
        "negGBRLevNum",
        "encryAlgUEA0",
        "encryAlgUEA1",
        "encryAlgUEA2",
        "fachPchTimeThr",
        "cdtRabRateSw",
        "rlRefTimeAjtSw",
        "amrNbMode4UseTag",
        "srbOnEdchSwch",
        "amrWbMode2UseTag",
        "dlPsRateLmtLowC",
        "cdtImeiAcqSw",
        "psInterSysHoSuppInd",
        "sChQSwch",
        "basedImsiHoInd",
        "hoToGsmPenTimer",
        "smartP2DtimesThr",
        "cChQSwch",
        "psNullNri",
        "r99RtIfHoSw",
        "cidLcsMethodInd",
        "hsupaIfHoSw",
        "csPsSceHsToDSwch",
        "amrNbMode1UseTag",
        "tNnsf",
        "ulPsRateLmtHighC",
        "dpiQoSSwitch",
        "nAmrInitialRate",
        "perferEncryAlg",
        "amrWbMode7UseTag",
        "srvBasedHoInd",
        "ulPsRateLmtLowC",
        "r99RtEutraHoSw",
        "hsupaRatHoSw",
        "fchPchUeCsPsSwch",
        "dlPsRateLmtHighC",
        "ettiRscpThres",
        "fourEChAllowedInd",
        "ulPwrDasf",
        "r99NrtIfHoSw",
        "r99NrtEtraHoSw",
        "mrSw",
        "amrRatHoSw",
        "amrNbMode6UseTag",
        "ulRateAdjLev",
        "compMdCfgStra",
        "amrRncAdjust",
        "rncPsHoLteSw",
        "r99NrtRatHoSw",
        "amrWbMode4UseTag",
        "ptpOverHSInd",
        "wAmrInitialRate",
        "perferEncryAlgSw",
        "nbrCellMonSupInd",
        "hoToEutraPenTimer",
        "nonQchatPsRelInd",
        "cs64RbModeSw",
        "dchAdjRateSwch",
        "dlRateAdjLevNum",
        "ldBsdIntSysHOInd",
        "rncPsRediLteSw",
        "amrNbMode3UseTag",
        "amrWbMode1UseTag",
        "integrityAlgUIA1",
        "integrityAlgUIA2",
        "csPlusPsSwch",
        "ulLowLimNegGBR",
        "iBChQSwch",
        "cdtNumThdPerRrc",
        "ackNackEncInd",
        "csPlusPsR5UeSwch",
        "dePriSwch",
        "ulRateAdjLevNum",
        "fastRecfgSptInd",
        "wAmrSupInd",
        "hsupaEutraHoSw",
        "amrNbMode0UseTag",
        "csPsSceDchRate",
        "ettiQualLoadSwi",
        "amrWbMode6UseTag",
        "smartD2FtimesThr",
        "psSigForImsInd",
        "cdtLastSigAcqSw",
        "csNullNri",
        "hsdpaIfHoSw",
        "smartD2FSwch",
        "ettiTraffVolSwch",
        "dlRateAdjLev",
        "csPsBadCovSwch",
        "smartP2DSwch",
        "dToHsDelaySwch",
        "cdtNasCallNoAcqSw",
        "amrNbMode5UseTag",
        "dlLowLimNegGBR",
        "amrWbMode3UseTag",
        "rncSrvccSw",
        "drbcSwch",
        "hsdpaRatHoSw",
        "ettiEcN0Thres",
        "naccSuppInd",
        "r6MulRabRcfgMeth",
        "rfach",
        "cdtNodebStaInfoAcqSw",
        "dlPwrDasf",
        "noDataPs00Swch",
        "refUDrbcProfile",
        "thpThresh",
        "cdtNasMsgSw",
        "amrNbMode2UseTag",
        "userLabel",
        "initialRateDl",
        "amrIfHoSw",
        "amrWbMode0UseTag",
        "dchSig68Swch",
        "throughputThr",
        "hsToDE4B0timeThr",
        "amrWbMode8UseTag",
        "cdtSw",
        "initialRateUl",
        "description",
        "r99RtRatHoSw",
        "amrOverHspaSwch"
    FROM
    zte_bulkcm_umts."vsDataLogicalRnc"

    """
)

MgwTrPath = ReplaceableObject(
    'zte_cm_3g."MgwTrPath"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalMgwLink_id",
        "vsDataMgwTrPath_id",
        "DestIpMaskLen",
        "NRtRxResRatio",
        "RxBitRate",
        "TxBitRate",
        "SigRsvBandWidth",
        "DestIpVersion",
        "refSubTrPathGroup",
        "DestIpAddr",
        "refModule",
        "RTSelFactor",
        "userLabel",
        "RtTxResRatio",
        "NResPara",
        "RtRxResRatio",
        "refAal2PathTp",
        "description",
        "TrPathSeq",
        "TrPathType",
        "NRtTxResRatio",
        "IpBandAdjSwitch"
    FROM
    zte_bulkcm_umts."vsDataMgwTrPath"

    """
)

MgwTrPathCir = ReplaceableObject(
    'zte_cm_3g."MgwTrPathCir"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataLogicalMgwLink_id",
        "vsDataMgwTrPath_id",
        "vsDataMgwTrPathCir_id",
        "RatioTrPathGroup",
        "userLabel",
        "refTrPathGroup",
        "description"
    FROM
    zte_bulkcm_umts."vsDataMgwTrPathCir"

    """
)

MPO = ReplaceableObject(
    'zte_cm_3g."MPO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataMPOProfile_id",
        "vsDataMPO_id",
        "appMimoInd",
        "app64QamInd",
        "measPwrOffset",
        "appDcHsdpaInd",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataMPO"

    """
)

MPOProfile = ReplaceableObject(
    'zte_cm_3g."MPOProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataMPOProfile_id",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataMPOProfile"

    """
)

MR = ReplaceableObject(
    'zte_cm_3g."MR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataMR_id",
        "mrUePrdInterRatMeasSw",
        "amrBlerPat",
        "mrUeAgpsPrdLocRa",
        "mrUePrdLocationMeasSw",
        "mrUePrdInternalMeasSw",
        "mrUeLocMeaRptInterval",
        "mrUeEvQualityMeasSw",
        "mrUeEvInternalMeasSw",
        "nonAmrBleErrCrc",
        "nonAmrBlerPat",
        "mrUeIniCallLocMode",
        "nonAmrBlerEvtSw",
        "mrServiceTypeCs",
        "iniMeasRptTrMod",
        "emiMeasInMRSwch",
        "mrUePrdIntraMeasSw",
        "mrUeAcqRatioCs",
        "mrAgpsNotEgh",
        "amrBleErrCrc",
        "mrRachMeasSw",
        "mrUeEvTrafficVolMeasSw",
        "amrBlerEvtSw",
        "mrServiceTypePs",
        "mrUeAcqRatioPs",
        "mrAgpsDataMiss",
        "mrUePrdInterFreqMeasSw",
        "mrRnluPrdQualityMeasSw",
        "mrUeInitialCallPosMeasSw",
        "mrOvdThd",
        "mrUeMeasRptInterval",
        "mrServiceTypeCsPs",
        "mrUePrdQualityMeasSw",
        "nonAmrBlerTotalCrc",
        "userLabel",
        "mrUeMeasRptTrMod",
        "amrBlerTotalCrc",
        "mrUeEvIntraInterIRatMeasSw",
        "mrUePrdLocMode",
        "description"
    FROM
    zte_bulkcm_umts."vsDataMR"

    """
)

NbapLink = ReplaceableObject(
    'zte_cm_3g."NbapLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "IubLink_id",
        "vsDataNbapLink_id",
        "link3BrsType",
        "ref3UniSaalTp",
        "link1BrsType",
        "ref1UniSaalTp",
        "ccpPortNum",
        "ref2SctpAssociation",
        "useType",
        "link2BrsType",
        "ref2UniSaalTp",
        "userLabel",
        "outStreamId",
        "ref3SctpAssociation",
        "ref1SctpAssociation",
        "description"
    FROM
    zte_bulkcm_umts."vsDataNbapLink"

    """
)

NbComMeas = ReplaceableObject(
    'zte_cm_3g."NbComMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataNbComMeasProfile_id",
        "vsDataNbComMeas_id",
        "comMeasType",
        "measObjType",
        "nbCMCfgNo",
        "userLabel",
        "rptPrd",
        "rptType",
        "rptPrdUnit",
        "measFilterCoeff",
        "nbCMCfgNote",
        "description"
    FROM
    zte_bulkcm_umts."vsDataNbComMeas"

    """
)

NbComMeasProfile = ReplaceableObject(
    'zte_cm_3g."NbComMeasProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataNbComMeasProfile_id",
        "intialloadscene",
        "reservedByUNbComMeas",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataNbComMeasProfile"

    """
)

NbDedMeas = ReplaceableObject(
    'zte_cm_3g."NbDedMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataNbDedMeasProfile_id",
        "vsDataNbDedMeas_id",
        "dedMeasType",
        "nbDMCfgNo",
        "rptPrd",
        "rptType",
        "evtAbcdefTime",
        "dlRateLevel",
        "evtEfSirEThrd1",
        "evtEfSirEThrd2",
        "evtAbTcpThrd",
        "userLabel",
        "rptPrdUnit",
        "measFilterCoeff",
        "nbDMCfgNote",
        "description"
    FROM
    zte_bulkcm_umts."vsDataNbDedMeas"

    """
)

NbDedMeasProfile = ReplaceableObject(
    'zte_cm_3g."NbDedMeasProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataNbDedMeasProfile_id",
        "reservedByUNbDedMeas",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataNbDedMeasProfile"

    """
)

PchEvUeTrv = ReplaceableObject(
    'zte_cm_3g."PchEvUeTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataPchEvUeTrv_id",
        "ueTrvMCfgNo",
        "userLabel",
        "averageTime",
        "measEvtNum",
        "measQuantity",
        "meaEvtId",
        "rptThres",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPchEvUeTrv"

    """
)

PicoSonMeasCfg = ReplaceableObject(
    'zte_cm_3g."PicoSonMeasCfg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPicoSonMeasCfg_id",
        "picoInterRptPrd",
        "picoIntraRptPrd",
        "picoMinUsrNumThrd",
        "picoGsmRptPrd",
        "userLabel",
        "picoMeaRptCriteria",
        "initialTimePoint1",
        "initialTimePoint2",
        "initTimePointNum",
        "initialTimePoint3",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPicoSonMeasCfg"

    """
)

PlBal = ReplaceableObject(
    'zte_cm_3g."PlBal"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataPlBal_id",
        "ldBalHsdPwrFacCho",
        "dulCarBalRscpThd",
        "dlPwrThdCs",
        "ldBalCeSwch",
        "extraCDeltaTrd",
        "ulLdThdCs4G",
        "extraDeltaHsuTrd",
        "ulLdBalPwrWeight",
        "dlLdBalPwrSwch",
        "rrcHsLdBaOnDchSw",
        "extraCDeltaTru",
        "hoHspaPlusBalSw",
        "rrcSigLowPriBalSta",
        "callHoldLBSw",
        "hoCalRestblSBSwch",
        "extraCDeltaCdTrd",
        "rrcDualCarrSw",
        "hspaPlusCapInd",
        "dlLdBalHsdWeight",
        "hspaPluBalCapPri",
        "dlCdThdCs4G",
        "dlCdThdR99Ps",
        "dlLdHsThdHsd",
        "dlLdBalPwrWeight",
        "utraUserNumOff",
        "drEcNoQualThrd",
        "deltaHsdUsrNumTd",
        "ulLdBalHsuWeight",
        "gsmCelCariNum",
        "ldBalHspaStrCho",
        "dlPwrThdCs4G",
        "csHo4MulRabSwch",
        "ldBalHsdCodFacCho",
        "dlCdThdCs",
        "ldBalHsuSwch",
        "rabAssSBSw",
        "initRrcSBSw",
        "coGsmUserNumOff",
        "ldBalBwSwch",
        "holdHspaPluBalSw",
        "gsmUserNumOff",
        "thdForUserNumofFach",
        "ldBalHsdBandWidFacCho",
        "ldBalCdSwch",
        "ulLdHsThdHsu",
        "ulLdThdR99Ps",
        "ulLdBalPwrSwch",
        "ldHsdUserNumThd",
        "mulRabBlSwch",
        "ldBalHsdNumSwch",
        "ldBalCdWeight",
        "u2EBalSwch",
        "callHoldSBSw",
        "ulLdThdCs",
        "drRscpQualThrd",
        "extraDeltaHsdTrd",
        "dulCarBalEcNoThd",
        "hoCalRestblLBSwch",
        "csBalSwch",
        "rabHspaPluBalSw",
        "dlPwrThdR99Ps",
        "rabAssLBSw",
        "userLabel",
        "ldBalHsdSwch",
        "initRrcLBSw",
        "dRWithoutLdComSwch",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPlBal"

    """
)

PlmnAdjFunction = ReplaceableObject(
    'zte_cm_3g."PlmnAdjFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnAdjFunction_id",
        "userLabel",
        "description",
        "refPlmnGroup"
    FROM
    zte_bulkcm_umts."vsDataPlmnAdjFunction"

    """
)

PlmnSpecFunction = ReplaceableObject(
    'zte_cm_3g."PlmnSpecFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "userLabel",
        "refLocalPlmnGroup",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPlmnSpecFunction"

    """
)

Prach = ReplaceableObject(
    'zte_cm_3g."Prach"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataAich_id",
        "vsDataPrach_id",
        "pSF",
        "psfNum",
        "availSubChanNum",
        "maxPreamRetrans",
        "pRStep",
        "asigEndIdx",
        "mmax",
        "rachCtcId",
        "ac2ASCMap",
        "prachType",
        "asubChNum",
        "permitMaxASC",
        "userLabel",
        "commPhyChanelId",
        "asigStIdx",
        "preamThs",
        "rachTti",
        "signature",
        "preamScraCode",
        "dynPstLevelInit",
        "description",
        "constVal"
    FROM
    zte_bulkcm_umts."vsDataPrach"

    """
)

PrdRttUeInt = ReplaceableObject(
    'zte_cm_3g."PrdRttUeInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "vsDataPrdRttUeInt_id",
        "filterCoeff",
        "userLabel",
        "prdRptAmount",
        "ueIntMCfgNo",
        "measRptTrMod",
        "prdRptInterval",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPrdRttUeInt"

    """
)

PriSel = ReplaceableObject(
    'zte_cm_3g."PriSel"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataPriSel_id",
        "qqualminEUTRA",
        "eutranHighThres2",
        "threshServingLow",
        "qrxlevminEUTRA",
        "allowMeasBand",
        "qrxlevminGSM",
        "eutranLowThresh",
        "servCelPriority",
        "eutranPriority",
        "eutranInterFNum",
        "threshRsrqInd",
        "gsmCellGroupNum",
        "eutraDetectionInd",
        "geranLowThresh",
        "eutranHighThresh",
        "eutranLowThresh2",
        "startARFCN",
        "utranHighThresh",
        "thresServingLow2",
        "dlEARFCN",
        "geranPriority",
        "utranUARFCN",
        "sPrioritySearch1",
        "sPrioritySearch2",
        "gsmBandIndicator",
        "geranHighThresh",
        "utranPriority",
        "userLabel",
        "utranLowThresh",
        "qqualminFDD",
        "qrxlevminFDD",
        "utranInterFNum",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPriSel"

    """
)

PsEvtTPUeInt = ReplaceableObject(
    'zte_cm_3g."PsEvtTPUeInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "vsDataPsEvtTPUeInt_id",
        "filterCoeff",
        "userLabel",
        "trigTime",
        "txPowerThres",
        "measEvtNum",
        "meaEvtId",
        "ueIntMCfgNo",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPsEvtTPUeInt"

    """
)

PwrLimTPUeInt = ReplaceableObject(
    'zte_cm_3g."PwrLimTPUeInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "vsDataPwrLimTPUeInt_id",
        "filterCoeff",
        "userLabel",
        "trigTime",
        "txPowerThres",
        "measEvtNum",
        "meaEvtId",
        "ueIntMCfgNo",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataPwrLimTPUeInt"

    """
)

QChat = ReplaceableObject(
    'zte_cm_3g."QChat"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQChat_id",
        "userLabel",
        "srbDelayQChat",
        "postVerifPeriQCh",
        "qChatDSCPValue",
        "qChatDRXCycleLen",
        "dpcchPcpLenQChat",
        "qChatUeMaxNum",
        "description",
        "nReleasedQChat",
        "tQchatdormancy"
    FROM
    zte_bulkcm_umts."vsDataQChat"

    """
)

QosFunction = ReplaceableObject(
    'zte_cm_3g."QosFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataQosFunction"

    """
)

RachEvtUeTrv = ReplaceableObject(
    'zte_cm_3g."RachEvtUeTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataRachEvtUeTrv_id",
        "ueTrvMCfgNo",
        "pendingTime",
        "trigTime",
        "averageTime",
        "measEvtNum",
        "meaEvtId",
        "rptThres",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "txInterruption",
        "rptRlcVarInd",
        "measQuantity",
        "txInterCfgPre",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRachEvtUeTrv"

    """
)

RachPrdUeTrv = ReplaceableObject(
    'zte_cm_3g."RachPrdUeTrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "vsDataRachPrdUeTrv_id",
        "ueTrvMCfgNo",
        "averageTime",
        "prdRptInterval",
        "rptRlcBufInd",
        "rptRlcAveInd",
        "userLabel",
        "rptRlcVarInd",
        "prdRptAmount",
        "measQuantity",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRachPrdUeTrv"

    """
)

RatEcNoEvMeasforE = ReplaceableObject(
    'zte_cm_3g."RatEcNoEvMeasforE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasSrvSpec_id",
        "vsDataRatEcNoEvMeasforE_id",
        "trigTime",
        "eventNum",
        "eventId",
        "interRatCfgNo",
        "filterCoeff",
        "eUtranFilterCoeff",
        "userLabel",
        "threshSys",
        "w",
        "hysteresis",
        "description",
        "thresh"
    FROM
    zte_bulkcm_umts."vsDataRatEcNoEvMeasforE"

    """
)

RatEcNoEvMeasforG = ReplaceableObject(
    'zte_cm_3g."RatEcNoEvMeasforG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasSrvSpec_id",
        "vsDataRatEcNoEvMeasforG_id",
        "trigTime",
        "eventNum",
        "eventId",
        "interRatCfgNo",
        "gsmFilterCoeff",
        "filterCoeff",
        "userLabel",
        "threshSys",
        "w",
        "hysteresis",
        "description",
        "thresh"
    FROM
    zte_bulkcm_umts."vsDataRatEcNoEvMeasforG"

    """
)

RatEcNoPrdMeas = ReplaceableObject(
    'zte_cm_3g."RatEcNoPrdMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasNoSrvSpec_id",
        "vsDataRatEcNoPrdMeas_id",
        "gsmFilterCoeff",
        "filterCoeff",
        "eUtranFilterCoeff",
        "userLabel",
        "prdRptAmount",
        "prdRptInterval",
        "interRatCfgNo",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRatEcNoPrdMeas"

    """
)

RatMeasNoSrvSpec = ReplaceableObject(
    'zte_cm_3g."RatMeasNoSrvSpec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasNoSrvSpec_id",
        "userLabel",
        "description",
        "reservedByURatEcNoPrdMeas",
        "reservedByURatRscpPrdMeas"
    FROM
    zte_bulkcm_umts."vsDataRatMeasNoSrvSpec"

    """
)

RatMeasProfile = ReplaceableObject(
    'zte_cm_3g."RatMeasProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "intialHoCelSelScene",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRatMeasProfile"

    """
)

RatMeasSrvSpec = ReplaceableObject(
    'zte_cm_3g."RatMeasSrvSpec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasSrvSpec_id",
        "reservedByURatEcNoEvMeasforE",
        "reservedByURatEcNoEvMeasforG",
        "userLabel",
        "reservedByURatRscpEvMeasforE",
        "srvCategory",
        "reservedByURatRscpEvMeasforG",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRatMeasSrvSpec"

    """
)

RatRscpEvMeasforE = ReplaceableObject(
    'zte_cm_3g."RatRscpEvMeasforE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasSrvSpec_id",
        "vsDataRatRscpEvMeasforE_id",
        "trigTime",
        "eventNum",
        "eventId",
        "interRatCfgNo",
        "filterCoeff",
        "eUtranFilterCoeff",
        "userLabel",
        "threshSys",
        "w",
        "hysteresis",
        "description",
        "thresh"
    FROM
    zte_bulkcm_umts."vsDataRatRscpEvMeasforE"

    """
)

RatRscpEvMeasforG = ReplaceableObject(
    'zte_cm_3g."RatRscpEvMeasforG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasSrvSpec_id",
        "vsDataRatRscpEvMeasforG_id",
        "trigTime",
        "eventNum",
        "eventId",
        "interRatCfgNo",
        "gsmFilterCoeff",
        "filterCoeff",
        "userLabel",
        "threshSys",
        "w",
        "hysteresis",
        "description",
        "thresh"
    FROM
    zte_bulkcm_umts."vsDataRatRscpEvMeasforG"

    """
)

RatRscpPrdMeas = ReplaceableObject(
    'zte_cm_3g."RatRscpPrdMeas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRatMeasProfile_id",
        "vsDataRatMeasNoSrvSpec_id",
        "vsDataRatRscpPrdMeas_id",
        "gsmFilterCoeff",
        "filterCoeff",
        "eUtranFilterCoeff",
        "userLabel",
        "prdRptAmount",
        "prdRptInterval",
        "interRatCfgNo",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRatRscpPrdMeas"

    """
)

RlEvtRttUeInt = ReplaceableObject(
    'zte_cm_3g."RlEvtRttUeInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "vsDataRlEvtRttUeInt_id",
        "filterCoeff",
        "userLabel",
        "trigTime",
        "measEvtNum",
        "txRxTDThres",
        "meaEvtId",
        "ueIntMCfgNo",
        "measRptTrMod",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRlEvtRttUeInt"

    """
)

RncInfo = ReplaceableObject(
    'zte_cm_3g."RncInfo"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRncInfo_id",
        "tWaitMNMeasRpt",
        "epchToAWE",
        "psLCUsrNumFiltCoef",
        "fillCnInfoSwch",
        "cfnOffsetComp",
        "epchToAWS",
        "ettiCongSwch",
        "defaultArpSeg",
        "waitRbStTimer",
        "e2DSHOSwch",
        "rxlevNecellInd",
        "srvccPsHo2LteMode",
        "rotAdjstPrd",
        "pchCsPageRsdTimer",
        "noEdchFpTimer",
        "rabSetupTimer",
        "cnInLocaMeasPeriod",
        "csfbPsHo2LteMode",
        "cpcRecovSwi",
        "qosLoadCtrolSwch",
        "berFilterCoeff",
        "cmpNumforPaging",
        "interHoRscpThrd",
        "rotLwRatTrigTim",
        "syncRecfgSwch",
        "iu16mIeSwch",
        "interHoEcNoThrd",
        "hoToIntraPenTimer",
        "eToD4BtimesThr",
        "forbidHsSirIncSwch",
        "lar2SmlCovBHoRncSw",
        "shieldPeriodSwch",
        "rotTrigTimes",
        "hsupaRteThdforRot",
        "cfnOffsetCompSwch",
        "edchMACdmulti",
        "noNHR13MulRlTimer",
        "nbrCellMonRscpThrd",
        "prePlmnConSw",
        "intraRlocAmrRtCtrl",
        "badCovRrcSwch",
        "CfnOfSigOnHspaSw",
        "intBrdRrcReqReSw",
        "conForbAmrSwit",
        "loadFilterCoeff",
        "intBrdRrcReqReThd",
        "rediNoMeaEcNoThd",
        "userNumFilterCoeff",
        "cqiFeedbaLoadSwi",
        "procLoadCtrolSwch",
        "r5PchRrcRelMode",
        "qNotEptyCacSwth",
        "arpBronzePc",
        "csmtIdentifySwch",
        "cheEutraCapiSw",
        "arpGoldPc",
        "initUEFiDAcSai",
        "pchCsPageRsdSwch",
        "blerArpSwitch",
        "dmpReSelTimes",
        "psHoLteMeasTimer",
        "olPcAlg",
        "csfbIdentifyTimer",
        "rediNoMeaRscpThd",
        "psDrbcProhSwch",
        "psDrbcProhTimer",
        "amrBadCovSwh",
        "sipOptSwch",
        "rotDcrsStep",
        "qpskBoostIurSwch",
        "modNasPlmnSwch",
        "hoToInterPenTimer",
        "recfgOptMacroDiv",
        "userLabel",
        "qpskInterpoIurSwch",
        "pchBarredUsrThd",
        "rncImpEulPwrSwi",
        "loadForAmrSwit",
        "secModeTimeoutOpSw",
        "olpcBerSwitch",
        "rotIncrsStep",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRncInfo"

    """
)

RncPool = ReplaceableObject(
    'zte_cm_3g."RncPool"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRncPool_id",
        "csRRelocRatio",
        "poolUpOverThd",
        "userLabel",
        "rncLdValidTime",
        "psRRelocRatio",
        "poolCpOverThd",
        "rncLdCheckPrd",
        "description",
        "rRelocDelayTimer"
    FROM
    zte_bulkcm_umts."vsDataRncPool"

    """
)

RnluCfg = ReplaceableObject(
    'zte_cm_3g."RnluCfg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRnluCfg_id",
        "CSThdForAttSwch",
        "TcpOptSwitch",
        "MaxPagSendTimer",
        "UEThdForEngCon",
        "RnluResPara70",
        "RnluResPara71",
        "RnluResPara72",
        "RnluResPara73",
        "RnluResPara74",
        "Cs64IuupDiscSwit",
        "RnluResPara75",
        "RnluResPara76",
        "RnluResPara77",
        "CDFThresInDTX",
        "RnluResPara78",
        "RnluResPara79",
        "BoardPwrOffHoTmr",
        "RnluResPara80",
        "BrdPwrOffWaitTime",
        "GeneralPQIAppType",
        "ULPQIStatThres",
        "RnluResPara10",
        "RnluResPara11",
        "RnluResPara12",
        "RnluResPara13",
        "RnluResPara14",
        "RnluResPara15",
        "RnluResPara16",
        "RnluResPara17",
        "RnluResPara18",
        "RnluResPara19",
        "LocalTcpAgtOptSwch",
        "RnluResPara20",
        "DLPQIStatThres1",
        "RnluResPara21",
        "DLPQIStatThres2",
        "RnluResPara22",
        "RnluResPara23",
        "RnluResPara24",
        "RnluResPara25",
        "RnluResPara26",
        "RnluResPara27",
        "RnluResPara28",
        "RnluResPara29",
        "GeneralPQISwch",
        "RnluResPara1",
        "RnluResPara2",
        "RnluResPara30",
        "RnluResPara3",
        "RnluResPara31",
        "RnluResPara4",
        "RnluResPara32",
        "RnluResPara5",
        "RnluResPara33",
        "RnluResPara6",
        "RnluResPara34",
        "RnluResPara7",
        "RnluResPara35",
        "RnluResPara8",
        "RnluResPara36",
        "RnluResPara9",
        "RnluResPara37",
        "RnluResPara38",
        "RnluResPara39",
        "Pch4APendingTime",
        "CellAssLogTrgNum",
        "TcpInterval",
        "RnluResPara40",
        "RnluResPara41",
        "RnluResPara42",
        "RnluResPara43",
        "RnluResPara44",
        "GeneralPQIUERatio",
        "RnluResPara45",
        "RnluResPara46",
        "RnluResPara47",
        "RnluResPara48",
        "UlTcpAckDupInd",
        "RnluResPara49",
        "RnluResPara50",
        "RnluResPara51",
        "RnluResPara52",
        "RnluResPara53",
        "RnluResPara54",
        "RnluResPara55",
        "RnluResPara56",
        "RnluResPara57",
        "RnluResPara58",
        "RnluResPara59",
        "MaxStatistFlowPUe",
        "UEThdForAttSwch",
        "userLabel",
        "CSThdForEngCon",
        "UlTcpAckSplitSwitch",
        "RnluResPara60",
        "DlTcpInSeqDeliverTmr",
        "DlLocalRetranSwitch",
        "RnluResPara61",
        "RnluResPara62",
        "RnluResPara63",
        "RnluResPara64",
        "RnluResPara65",
        "RnluResPara66",
        "description",
        "RnluResPara67",
        "RnluResPara68",
        "RnluResPara69"
    FROM
    zte_bulkcm_umts."vsDataRnluCfg"

    """
)

RoutingArea = ReplaceableObject(
    'zte_cm_3g."RoutingArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataLocationArea_id",
        "vsDataRoutingArea_id",
        "rac",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRoutingArea"

    """
)

RrcCategoryBasPriMapping = ReplaceableObject(
    'zte_cm_3g."RrcCategoryBasPriMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataRrcCategoryBasPriMapping_id",
        "bPforRrcCategory",
        "rrcSetupCategory",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRrcCategoryBasPriMapping"

    """
)

RrcCategoryMapping = ReplaceableObject(
    'zte_cm_3g."RrcCategoryMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataRrcCategoryMapping_id",
        "rrcSetupCategory",
        "userLabel",
        "description",
        "rrcSetupCause"
    FROM
    zte_bulkcm_umts."vsDataRrcCategoryMapping"

    """
)

RsvdUeGlobalPara = ReplaceableObject(
    'zte_cm_3g."RsvdUeGlobalPara"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRsvdUeGlobalPara_id",
        "dropForRsvdUeSwch",
        "rsvdUeLstSwitch",
        "rsvdUeNtfNbrPrio",
        "rrcNonRsvCsStra",
        "rsvDlResBwd",
        "rsvdUeEstNtfSwitch",
        "rsvExpPdcpBufSwch",
        "mrBarSwch",
        "rrcNonRsvPsStra",
        "rsvForcedHoSwch",
        "rsvSpecFreqSwch",
        "rubRsvdSwch",
        "rsvdDtxdrxCfgSwch",
        "rsvPdcpDlBufLmt",
        "rsvdUserPwrOffset",
        "rsvdLessCfgSwch",
        "rsvDlArfcnforCsInd",
        "rsvdUeEttiEcNoThd",
        "onlySrbRrcRelSwch",
        "rsvDlArfcnforPsInd",
        "rsvdUeRrcSrb272Swch",
        "rsvOverBookPriSwch",
        "rsvdUeSrbCfgSwch",
        "userLabel",
        "rsvdUeEttiCfgMeth",
        "rubRsvdNeedUEVer",
        "rsvdFastL1SyncSwch",
        "rsvOverBookPri",
        "vipTcpOptSwch",
        "rsvdUeStateChgSwch",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRsvdUeGlobalPara"

    """
)

RsvdUeImsiList = ReplaceableObject(
    'zte_cm_3g."RsvdUeImsiList"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRsvdUeImsiList_id",
        "csCgtSchPrio",
        "psHspaSchPrio",
        "imsiDgtNum",
        "psCgtSchPrio",
        "csAppPri",
        "rsvCsReDelayTimer",
        "imsiActiveInd",
        "csBasicPrio",
        "userLabel",
        "psAppPri",
        "rsvPsReDelayTimer",
        "psBasicPrio",
        "csHspaSchPrio",
        "imsiDgt",
        "description"
    FROM
    zte_bulkcm_umts."vsDataRsvdUeImsiList"

    """
)

RsvdUserSrvPc = ReplaceableObject(
    'zte_cm_3g."RsvdUserSrvPc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSrvFunction_id",
        "vsDataRsvdUserSrvPc_id",
        "nhrThrDownTti10",
        "maxSirTargUpStep",
        "addiSIRDownStep",
        "blerAccpPeriod",
        "edchHarqPOFDD",
        "fpTargErrorTti10",
        "sirRapidConvSwi",
        "ulOlPcQESwchSil",
        "qePhyBerTarSil",
        "initBlerSIRTti10",
        "ulInitSIR",
        "ulSirStepTti10",
        "ulSirTargDnStep",
        "ulInitSIRTti2",
        "ulMinSIR",
        "berTargetDnThres",
        "fpTargErrorTti2",
        "nhrThrUpTti10",
        "ulMinSIRTti10",
        "nhrThrUpTti2",
        "ulMinSIRTti2",
        "ulSirTargUpStep",
        "berTargetUpThres",
        "ulSirStep",
        "nhrThrDownTti2",
        "ulInitSIRTti10",
        "initBlerSIR",
        "targetRetranNum",
        "ulMaxSIRTti10",
        "ulSirStepTti2",
        "dpcchPilotEbN0",
        "initBlerSIRTti2",
        "minDlDpchPwr",
        "swchAdaptiveStep",
        "ulMaxSIR",
        "srvType",
        "thrHarqFailTti10",
        "initSirAdd",
        "ulMaxSIRTti2",
        "thrHarqFailTti2",
        "initSirAddTti2",
        "errorThresh",
        "blerTarget",
        "userLabel",
        "maxDlDpchPwr",
        "maxSirTargDnStep",
        "berCntThres",
        "dwThrSampNumTti2",
        "initSirAddTti10",
        "upThrSampNumTti10",
        "qeCntThres",
        "upThrSampNumTti2",
        "description",
        "dwThrSampNumTti10",
        "maxUlDpchPwr"
    FROM
    zte_bulkcm_umts."vsDataRsvdUserSrvPc"

    """
)

Sccpch = ReplaceableObject(
    'zte_cm_3g."Sccpch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCellFDD_id",
        "vsDataSccpch_id",
        "maxFachPwr",
        "commPhyChanelId",
        "userLabel",
        "po1",
        "po3",
        "sccpchOffset",
        "description",
        "sccpchUsage"
    FROM
    zte_bulkcm_umts."vsDataSccpch"

    """
)

SchPriMapping = ReplaceableObject(
    'zte_cm_3g."SchPriMapping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataSchPriMappingProfile_id",
        "vsDataSchPriMapping_id",
        "schPrio",
        "basicPrio",
        "userLabel",
        "bearerType",
        "description"
    FROM
    zte_bulkcm_umts."vsDataSchPriMapping"

    """
)

SchPriMappingProfile = ReplaceableObject(
    'zte_cm_3g."SchPriMappingProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataSchPriMappingProfile_id",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataSchPriMappingProfile"

    """
)

ServiceArea = ReplaceableObject(
    'zte_cm_3g."ServiceArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataLocationArea_id",
        "vsDataServiceArea_id",
        "sac",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataServiceArea"

    """
)

SignalTraceCfg = ReplaceableObject(
    'zte_cm_3g."SignalTraceCfg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataFullSignalTrace_id",
        "vsDataSignalTraceCfg_id",
        "TimeSegPerDay",
        "AllAccessCell",
        "StopTimeList",
        "MsgProtocolSwitchBit0",
        "StartDate",
        "MsgProtocolSwitchBit1",
        "MsgProtocolSwitchBit2",
        "MsgProtocolSwitchBit3",
        "IndexNo",
        "MsgProtocolSwitchBit6",
        "userLabel",
        "StartTimeList",
        "StopDate",
        "description"
    FROM
    zte_bulkcm_umts."vsDataSignalTraceCfg"

    """
)

SrvBasedHo = ReplaceableObject(
    'zte_cm_3g."SrvBasedHo"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnSpecFunction_id",
        "vsDataSrvBasedHo_id",
        "cs64SrvHoStra",
        "srvHoIndPsRT",
        "srvHoIndPsNRT",
        "psNrtSrvHoStra",
        "srvHoIndAmr",
        "amrSrvHoStra",
        "userLabel",
        "psRtSrvHoStra",
        "srvHoIndCs64",
        "srvHoComStra",
        "description"
    FROM
    zte_bulkcm_umts."vsDataSrvBasedHo"

    """
)

SrvDivPc = ReplaceableObject(
    'zte_cm_3g."SrvDivPc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSrvFunction_id",
        "vsDataSrvPcProfile_id",
        "vsDataSrvPc_id",
        "vsDataSrvDivPc_id",
        "dpchPO1",
        "dpchPO2",
        "dpchPO3",
        "ergchPOTti2",
        "initBlerSIRTti10",
        "ulInitSIR",
        "eagchPOTti10",
        "ehichPOTti10",
        "ulInitSIRTti2",
        "ulMinSIR",
        "ulMinSIRTti10",
        "ulMinSIRTti2",
        "ulInitSIRTti10",
        "initBlerSIR",
        "ulMaxSIRTti10",
        "dpcchPilotEbN0",
        "pwrForSglCell",
        "initBlerSIRTti2",
        "minDlDpchPwr",
        "ulMaxSIR",
        "ehichPOTti2",
        "txDivMod",
        "initSirAdd",
        "ulMaxSIRTti2",
        "initSirAddTti2",
        "userLabel",
        "pwrForHalfIsd",
        "ergchPOTti10",
        "maxDlDpchPwr",
        "initSirAddTti10",
        "eagchPOTti2",
        "description",
        "maxUlDpchPwr"
    FROM
    zte_bulkcm_umts."vsDataSrvDivPc"

    """
)

SrvFunction = ReplaceableObject(
    'zte_cm_3g."SrvFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSrvFunction_id",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataSrvFunction"

    """
)

SrvPc = ReplaceableObject(
    'zte_cm_3g."SrvPc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSrvFunction_id",
        "vsDataSrvPcProfile_id",
        "vsDataSrvPc_id",
        "nhrThrDownTti10",
        "maxSirTargUpStep",
        "addiSIRDownStep",
        "blerAccpPeriod",
        "outSirThresh",
        "shieldPeriod",
        "edchHarqPOFdd",
        "fpTargErrorTti10",
        "sirRapidConvSwi",
        "ulOlPcQESwchSil",
        "qePhyBerTarSil",
        "outSirTimWinSize",
        "ulSirStepTti10",
        "ulSirTargDnStep",
        "qePhyBerTarNorm",
        "berTargetDnThres",
        "berErrorTbThresh",
        "fpTargErrorTti2",
        "nhrThrUpTti10",
        "nhrThrUpTti2",
        "olPCPrioSwitch",
        "ulSirTargUpStep",
        "ulIlPcAlg",
        "ulSirStep",
        "nhrThrDownTti2",
        "berTargetUpThres",
        "targetRetranNum",
        "ulSirStepTti2",
        "tpcDlStep",
        "timWinSize",
        "swchAdaptiveStep",
        "minBerTarget",
        "srvType",
        "thrHarqFailTti10",
        "thrHarqFailTti2",
        "ttiNumThreshOpen",
        "errorThresh",
        "berTargDnStep",
        "blerTarget",
        "userLabel",
        "maxSirTargDnStep",
        "ttiNumThreshCls",
        "berCntThres",
        "dwThrSampNumTti2",
        "tpcStepSize",
        "upThrSampNumTti10",
        "qeCntThres",
        "addiSIRDownPeriod",
        "berTargUpStep",
        "berTbThresh",
        "upThrSampNumTti2",
        "maxBerTarget",
        "description",
        "dwThrSampNumTti10"
    FROM
    zte_bulkcm_umts."vsDataSrvPc"

    """
)

SrvPcProfile = ReplaceableObject(
    'zte_cm_3g."SrvPcProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSrvFunction_id",
        "vsDataSrvPcProfile_id",
        "intialloadscene",
        "profileId",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataSrvPcProfile"

    """
)

SubSrv = ReplaceableObject(
    'zte_cm_3g."SubSrv"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSrvFunction_id",
        "vsDataSubSrv_id",
        "domain",
        "eTTI",
        "maxBitRate",
        "ulEbN0Pc",
        "sEdchEbN0Pc",
        "srvType",
        "refUEdchRcDchProfile",
        "minBitRate",
        "ptmRlsPerm",
        "refUDtxDrxProfile",
        "srvInd",
        "userLabel",
        "deltaT2TPQpsk",
        "deltaT2TPQam",
        "maxRetransEdch",
        "trafficClass",
        "description",
        "direction"
    FROM
    zte_bulkcm_umts."vsDataSubSrv"

    """
)

TbType = ReplaceableObject(
    'zte_cm_3g."TbType"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataTbTypeProfile_id",
        "vsDataTbType_id",
        "ipDscp",
        "ulResBwd",
        "tbType",
        "userLabel",
        "basicPrio",
        "dlResBwd",
        "bearerType",
        "description"
    FROM
    zte_bulkcm_umts."vsDataTbType"

    """
)

TbTypeProfile = ReplaceableObject(
    'zte_cm_3g."TbTypeProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataQosFunction_id",
        "vsDataTbTypeProfile_id",
        "profileId",
        "intialTransportModeScene",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataTbTypeProfile"

    """
)

TrvMeasProfile = ReplaceableObject(
    'zte_cm_3g."TrvMeasProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrvMeasProfile_id",
        "reservedByUDchEvUeTrv",
        "reservedByURachEvtUeTrv",
        "reservedByUDchEvUpTrv",
        "reservedByUComHsdschEvUpTrv",
        "profileId",
        "reservedByUDedSHsdschEvUpTrv",
        "reservedByUDedIBHsdschEvUpTrv",
        "userLabel",
        "reservedByUEdchtoDchUpTrv",
        "reservedByUETTIEdchEvUpTrv",
        "reservedByURachPrdUeTrv",
        "reservedByUFachEvUpTrv",
        "reservedByUPchEvUeTrv",
        "reservedByUDchPrdUeTrv",
        "reservedByUDedEdchEvUpTrv",
        "description",
        "reservedByUComEdchEvUpTrv"
    FROM
    zte_bulkcm_umts."vsDataTrvMeasProfile"

    """
)

UeCnst = ReplaceableObject(
    'zte_cm_3g."UeCnst"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeCnst_id",
        "t323",
        "t302",
        "n312Connected",
        "t304",
        "t305",
        "n300",
        "t307",
        "t308",
        "n302",
        "t309",
        "t312Connected",
        "n304",
        "t312Idle",
        "n312Idle",
        "t313",
        "t314",
        "t315",
        "t316",
        "n313",
        "userLabel",
        "n315",
        "t323Swch",
        "description",
        "t300"
    FROM
    zte_bulkcm_umts."vsDataUeCnst"

    """
)

UeIntMeasProfile = ReplaceableObject(
    'zte_cm_3g."UeIntMeasProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeIntMeasProfile_id",
        "reservedByURlEvtRttUeInt",
        "profileId",
        "reservedByUPwrLimTPUeInt",
        "userLabel",
        "reservedByUAmrEvtTPUeInt",
        "reservedByUPrdRttUeInt",
        "reservedByUPsEvtTPUeInt",
        "reservedByUEvtRttUeInt",
        "description",
        "reservedByUHoEvtTPUeInt"
    FROM
    zte_bulkcm_umts."vsDataUeIntMeasProfile"

    """
)

UtranRegArea = ReplaceableObject(
    'zte_cm_3g."UtranRegArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "bulkCmConfigDataFile_schemaLocation",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "meContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUtranRegArea_id",
        "ura",
        "userLabel",
        "description"
    FROM
    zte_bulkcm_umts."vsDataUtranRegArea"

    """
)


def upgrade():
    op.create_view(EUtranRelation)
    op.create_view(ExternalENBFunction)
    op.create_view(ExternalEUtranCellFDD)
    op.create_view(ExternalGsmCell)
    op.create_view(ExternalRncFunction)
    op.create_view(ExternalUtranCellFDD)
    op.create_view(GsmRelation)
    op.create_view(IubLink)
    op.create_view(ManagedElement)
    op.create_view(meContext)
    op.create_view(RncFunction)
    op.create_view(SubNetwork)
    op.create_view(SubNetwork_2)
    op.create_view(UtranCellFDD)
    op.create_view(UtranRelation)
    op.create_view(Aich)
    op.create_view(AmrEvtTPUeInt)
    op.create_view(ANR)
    op.create_view(AppPriMapping)
    op.create_view(AppPriMappingProfile)
    op.create_view(AppSrvType)
    op.create_view(BasPri)
    op.create_view(BasPriMapping)
    op.create_view(BPriAc)
    op.create_view(BPriAcProfile)
    op.create_view(CelInfoFDD)
    op.create_view(CelSel)
    op.create_view(CfnOffset)
    op.create_view(CHspa)
    op.create_view(CMR)
    op.create_view(CnInfo)
    op.create_view(ComEdchEvUpTrv)
    op.create_view(ComHsdschEvUpTrv)
    op.create_view(CommEdch)
    op.create_view(CompressMode)
    op.create_view(CpuCtrlPri)
    op.create_view(DchEvUeTrv)
    op.create_view(DchEvUpTrv)
    op.create_view(DchPrdUeTrv)
    op.create_view(DedEdchEvUpTrv)
    op.create_view(DedIBHsdschEvUpTrv)
    op.create_view(DedSHsdschEvUpTrv)
    op.create_view(DedSrvTb)
    op.create_view(DedSrvTbProfile)
    op.create_view(DiamondUserGlobalPara)
    op.create_view(DiamondUserImsiList)
    op.create_view(DiamondUserSrvPc)
    op.create_view(Dpi)
    op.create_view(DpiAlgParam)
    op.create_view(DpiAppSrv)
    op.create_view(DpiAppSrvPri)
    op.create_view(DpiAppSrvProfile)
    op.create_view(DpiBasPriMapping)
    op.create_view(DpiDrbc)
    op.create_view(DpiPartnerIp)
    op.create_view(DpiPartnerName)
    op.create_view(DpiProcMap)
    op.create_view(Drbc)
    op.create_view(DrbcProfile)
    op.create_view(DtxDrx)
    op.create_view(DtxDrxProfile)
    op.create_view(EdchRcDch)
    op.create_view(EdchRcDchProfile)
    op.create_view(EdchRcFach)
    op.create_view(EdchtoDchUpTrv)
    op.create_view(EFach)
    op.create_view(EFachPch)
    op.create_view(ETTIEdchEvUpTrv)
    op.create_view(EvtRttUeInt)
    op.create_view(FachEvUpTrv)
    op.create_view(FTPInfoCfg)
    op.create_view(FullSignalTrace)
    op.create_view(GbrResLimit)
    op.create_view(GbrResLimitProfile)
    op.create_view(GloAc)
    op.create_view(HoEvtTPUeInt)
    op.create_view(Hspa)
    op.create_view(InterEcNoEvMeasforE)
    op.create_view(InterEcNoEvMeasforG)
    op.create_view(InterEcNoEvMeasforU)
    op.create_view(InterEcNoPrdMeas)
    op.create_view(InterMeasNoSrvSpec)
    op.create_view(InterMeasProfile)
    op.create_view(InterMeaSrvSpec)
    op.create_view(InterRscpEvMeasforE)
    op.create_view(InterRscpEvMeasforG)
    op.create_view(InterRscpEvMeasforU)
    op.create_view(InterRscpPrdMeas)
    op.create_view(IntraEcNoEvMeas)
    op.create_view(IntraEcNoEvMeasForD)
    op.create_view(IntraEcNoPrdMeas)
    op.create_view(IntraMeasNoSrvSpec)
    op.create_view(IntraMeasProfile)
    op.create_view(IntraMeasSrvSpec)
    op.create_view(IntraRscpEvMeas)
    op.create_view(IntraRscpEvMeasForD)
    op.create_view(IntraRscpPrdMeas)
    op.create_view(Ipbm)
    op.create_view(IpLicense)
    op.create_view(IpSlaExTask)
    op.create_view(IubTrPath)
    op.create_view(IubTrPathCir)
    op.create_view(IuCnst)
    op.create_view(IucsLink)
    op.create_view(IupsLink)
    op.create_view(IupsTrPath)
    op.create_view(IupsTrPathCir)
    op.create_view(IurgLink)
    op.create_view(IurLink)
    op.create_view(IurTrPath)
    op.create_view(IurTrPathCir)
    op.create_view(LdCtrl)
    op.create_view(LocationArea)
    op.create_view(LogicalCell)
    op.create_view(LogicalIubLink)
    op.create_view(LogicalIupsLink)
    op.create_view(LogicalIupsLinkGroup)
    op.create_view(LogicalIurgLink)
    op.create_view(LogicalIurLink)
    op.create_view(LogicalIurQos)
    op.create_view(LogicalMgwLink)
    op.create_view(LogicalMscLink)
    op.create_view(LogicalMscLinkGroup)
    op.create_view(LogicalRnc)
    op.create_view(MgwTrPath)
    op.create_view(MgwTrPathCir)
    op.create_view(MPO)
    op.create_view(MPOProfile)
    op.create_view(MR)
    op.create_view(NbapLink)
    op.create_view(NbComMeas)
    op.create_view(NbComMeasProfile)
    op.create_view(NbDedMeas)
    op.create_view(NbDedMeasProfile)
    op.create_view(PchEvUeTrv)
    op.create_view(PicoSonMeasCfg)
    op.create_view(PlBal)
    op.create_view(PlmnAdjFunction)
    op.create_view(PlmnSpecFunction)
    op.create_view(Prach)
    op.create_view(PrdRttUeInt)
    op.create_view(PriSel)
    op.create_view(PsEvtTPUeInt)
    op.create_view(PwrLimTPUeInt)
    op.create_view(QChat)
    op.create_view(QosFunction)
    op.create_view(RachEvtUeTrv)
    op.create_view(RachPrdUeTrv)
    op.create_view(RatEcNoEvMeasforE)
    op.create_view(RatEcNoEvMeasforG)
    op.create_view(RatEcNoPrdMeas)
    op.create_view(RatMeasNoSrvSpec)
    op.create_view(RatMeasProfile)
    op.create_view(RatMeasSrvSpec)
    op.create_view(RatRscpEvMeasforE)
    op.create_view(RatRscpEvMeasforG)
    op.create_view(RatRscpPrdMeas)
    op.create_view(RlEvtRttUeInt)
    op.create_view(RncInfo)
    op.create_view(RncPool)
    op.create_view(RnluCfg)
    op.create_view(RoutingArea)
    op.create_view(RrcCategoryBasPriMapping)
    op.create_view(RrcCategoryMapping)
    op.create_view(RsvdUeGlobalPara)
    op.create_view(RsvdUeImsiList)
    op.create_view(RsvdUserSrvPc)
    op.create_view(Sccpch)
    op.create_view(SchPriMapping)
    op.create_view(SchPriMappingProfile)
    op.create_view(ServiceArea)
    op.create_view(SignalTraceCfg)
    op.create_view(SrvBasedHo)
    op.create_view(SrvDivPc)
    op.create_view(SrvFunction)
    op.create_view(SrvPc)
    op.create_view(SrvPcProfile)
    op.create_view(SubSrv)
    op.create_view(TbType)
    op.create_view(TbTypeProfile)
    op.create_view(TrvMeasProfile)
    op.create_view(UeCnst)
    op.create_view(UeIntMeasProfile)
    op.create_view(UtranRegArea)


def downgrade():
    op.drop_view(EUtranRelation)
    op.drop_view(ExternalENBFunction)
    op.drop_view(ExternalEUtranCellFDD)
    op.drop_view(ExternalGsmCell)
    op.drop_view(ExternalRncFunction)
    op.drop_view(ExternalUtranCellFDD)
    op.drop_view(GsmRelation)
    op.drop_view(IubLink)
    op.drop_view(ManagedElement)
    op.drop_view(meContext)
    op.drop_view(RncFunction)
    op.drop_view(SubNetwork)
    op.drop_view(SubNetwork_2)
    op.drop_view(UtranCellFDD)
    op.drop_view(UtranRelation)
    op.drop_view(Aich)
    op.drop_view(AmrEvtTPUeInt)
    op.drop_view(ANR)
    op.drop_view(AppPriMapping)
    op.drop_view(AppPriMappingProfile)
    op.drop_view(AppSrvType)
    op.drop_view(BasPri)
    op.drop_view(BasPriMapping)
    op.drop_view(BPriAc)
    op.drop_view(BPriAcProfile)
    op.drop_view(CelInfoFDD)
    op.drop_view(CelSel)
    op.drop_view(CfnOffset)
    op.drop_view(CHspa)
    op.drop_view(CMR)
    op.drop_view(CnInfo)
    op.drop_view(ComEdchEvUpTrv)
    op.drop_view(ComHsdschEvUpTrv)
    op.drop_view(CommEdch)
    op.drop_view(CompressMode)
    op.drop_view(CpuCtrlPri)
    op.drop_view(DchEvUeTrv)
    op.drop_view(DchEvUpTrv)
    op.drop_view(DchPrdUeTrv)
    op.drop_view(DedEdchEvUpTrv)
    op.drop_view(DedIBHsdschEvUpTrv)
    op.drop_view(DedSHsdschEvUpTrv)
    op.drop_view(DedSrvTb)
    op.drop_view(DedSrvTbProfile)
    op.drop_view(DiamondUserGlobalPara)
    op.drop_view(DiamondUserImsiList)
    op.drop_view(DiamondUserSrvPc)
    op.drop_view(Dpi)
    op.drop_view(DpiAlgParam)
    op.drop_view(DpiAppSrv)
    op.drop_view(DpiAppSrvPri)
    op.drop_view(DpiAppSrvProfile)
    op.drop_view(DpiBasPriMapping)
    op.drop_view(DpiDrbc)
    op.drop_view(DpiPartnerIp)
    op.drop_view(DpiPartnerName)
    op.drop_view(DpiProcMap)
    op.drop_view(Drbc)
    op.drop_view(DrbcProfile)
    op.drop_view(DtxDrx)
    op.drop_view(DtxDrxProfile)
    op.drop_view(EdchRcDch)
    op.drop_view(EdchRcDchProfile)
    op.drop_view(EdchRcFach)
    op.drop_view(EdchtoDchUpTrv)
    op.drop_view(EFach)
    op.drop_view(EFachPch)
    op.drop_view(ETTIEdchEvUpTrv)
    op.drop_view(EvtRttUeInt)
    op.drop_view(FachEvUpTrv)
    op.drop_view(FTPInfoCfg)
    op.drop_view(FullSignalTrace)
    op.drop_view(GbrResLimit)
    op.drop_view(GbrResLimitProfile)
    op.drop_view(GloAc)
    op.drop_view(HoEvtTPUeInt)
    op.drop_view(Hspa)
    op.drop_view(InterEcNoEvMeasforE)
    op.drop_view(InterEcNoEvMeasforG)
    op.drop_view(InterEcNoEvMeasforU)
    op.drop_view(InterEcNoPrdMeas)
    op.drop_view(InterMeasNoSrvSpec)
    op.drop_view(InterMeasProfile)
    op.drop_view(InterMeaSrvSpec)
    op.drop_view(InterRscpEvMeasforE)
    op.drop_view(InterRscpEvMeasforG)
    op.drop_view(InterRscpEvMeasforU)
    op.drop_view(InterRscpPrdMeas)
    op.drop_view(IntraEcNoEvMeas)
    op.drop_view(IntraEcNoEvMeasForD)
    op.drop_view(IntraEcNoPrdMeas)
    op.drop_view(IntraMeasNoSrvSpec)
    op.drop_view(IntraMeasProfile)
    op.drop_view(IntraMeasSrvSpec)
    op.drop_view(IntraRscpEvMeas)
    op.drop_view(IntraRscpEvMeasForD)
    op.drop_view(IntraRscpPrdMeas)
    op.drop_view(Ipbm)
    op.drop_view(IpLicense)
    op.drop_view(IpSlaExTask)
    op.drop_view(IubTrPath)
    op.drop_view(IubTrPathCir)
    op.drop_view(IuCnst)
    op.drop_view(IucsLink)
    op.drop_view(IupsLink)
    op.drop_view(IupsTrPath)
    op.drop_view(IupsTrPathCir)
    op.drop_view(IurgLink)
    op.drop_view(IurLink)
    op.drop_view(IurTrPath)
    op.drop_view(IurTrPathCir)
    op.drop_view(LdCtrl)
    op.drop_view(LocationArea)
    op.drop_view(LogicalCell)
    op.drop_view(LogicalIubLink)
    op.drop_view(LogicalIupsLink)
    op.drop_view(LogicalIupsLinkGroup)
    op.drop_view(LogicalIurgLink)
    op.drop_view(LogicalIurLink)
    op.drop_view(LogicalIurQos)
    op.drop_view(LogicalMgwLink)
    op.drop_view(LogicalMscLink)
    op.drop_view(LogicalMscLinkGroup)
    op.drop_view(LogicalRnc)
    op.drop_view(MgwTrPath)
    op.drop_view(MgwTrPathCir)
    op.drop_view(MPO)
    op.drop_view(MPOProfile)
    op.drop_view(MR)
    op.drop_view(NbapLink)
    op.drop_view(NbComMeas)
    op.drop_view(NbComMeasProfile)
    op.drop_view(NbDedMeas)
    op.drop_view(NbDedMeasProfile)
    op.drop_view(PchEvUeTrv)
    op.drop_view(PicoSonMeasCfg)
    op.drop_view(PlBal)
    op.drop_view(PlmnAdjFunction)
    op.drop_view(PlmnSpecFunction)
    op.drop_view(Prach)
    op.drop_view(PrdRttUeInt)
    op.drop_view(PriSel)
    op.drop_view(PsEvtTPUeInt)
    op.drop_view(PwrLimTPUeInt)
    op.drop_view(QChat)
    op.drop_view(QosFunction)
    op.drop_view(RachEvtUeTrv)
    op.drop_view(RachPrdUeTrv)
    op.drop_view(RatEcNoEvMeasforE)
    op.drop_view(RatEcNoEvMeasforG)
    op.drop_view(RatEcNoPrdMeas)
    op.drop_view(RatMeasNoSrvSpec)
    op.drop_view(RatMeasProfile)
    op.drop_view(RatMeasSrvSpec)
    op.drop_view(RatRscpEvMeasforE)
    op.drop_view(RatRscpEvMeasforG)
    op.drop_view(RatRscpPrdMeas)
    op.drop_view(RlEvtRttUeInt)
    op.drop_view(RncInfo)
    op.drop_view(RncPool)
    op.drop_view(RnluCfg)
    op.drop_view(RoutingArea)
    op.drop_view(RrcCategoryBasPriMapping)
    op.drop_view(RrcCategoryMapping)
    op.drop_view(RsvdUeGlobalPara)
    op.drop_view(RsvdUeImsiList)
    op.drop_view(RsvdUserSrvPc)
    op.drop_view(Sccpch)
    op.drop_view(SchPriMapping)
    op.drop_view(SchPriMappingProfile)
    op.drop_view(ServiceArea)
    op.drop_view(SignalTraceCfg)
    op.drop_view(SrvBasedHo)
    op.drop_view(SrvDivPc)
    op.drop_view(SrvFunction)
    op.drop_view(SrvPc)
    op.drop_view(SrvPcProfile)
    op.drop_view(SubSrv)
    op.drop_view(TbType)
    op.drop_view(TbTypeProfile)
    op.drop_view(TrvMeasProfile)
    op.drop_view(UeCnst)
    op.drop_view(UeIntMeasProfile)
    op.drop_view(UtranRegArea)