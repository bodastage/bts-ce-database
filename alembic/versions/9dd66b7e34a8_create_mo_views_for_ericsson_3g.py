"""Create MO views for Ericsson 3G

Revision ID: 9dd66b7e34a8
Revises: e8560bf05b12
Create Date: 2018-05-14 08:36:55.730000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9dd66b7e34a8'
down_revision = 'e8560bf05b12'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


AlarmIRP = ReplaceableObject(
    'ericsson_cm_3g."AlarmIRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "ManagementNode_id",
        "IRPAgent_id",
        "AlarmIRP_id",
        "irpVersion"
    FROM
    ericsson_bulkcm."AlarmIRP"

    """
)

BulkCmIRP = ReplaceableObject(
    'ericsson_cm_3g."BulkCmIRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "ManagementNode_id",
        "IRPAgent_id",
        "BulkCmIRP_id",
        "irpVersion"
    FROM
    ericsson_bulkcm."BulkCmIRP"

    """
)

ExternalGsmCell = ReplaceableObject(
    'ericsson_cm_3g."ExternalGsmCell"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."ExternalGsmCell_id",
t1."mnc",
t1."mcc",
t1."lac",
t1."bcchFrequency",
t1."ncc",
t1."bcc",
t1."userLabel",
t1."cellIdentity",
t2."vsDataExternalGsmCell_id",
t2."dtmSupport",
t2."maxTxPowerUl",
t2."qRxLevMin",
t2."individualOffset",
t2."bandIndicator",
t2."parentSystem",
t2."mncLength",
t2."rac",
t2."rimCapable"
FROM
ericsson_bulkcm."ExternalGsmCell" t1
INNER JOIN ericsson_bulkcm."vsDataExternalGsmCell" t2
 ON t1."ExternalGsmCell_id" = t2."ExternalGsmCell_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."FileName" = t2."FileName" 

"""
)

ExternalUtranCell = ReplaceableObject(
    'ericsson_cm_3g."ExternalUtranCell"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."ExternalUtranCell_id",
t1."rac",
t1."lac",
t1."primaryCpichPower",
t1."primaryScramblingCode",
t1."uarfcnDl",
t1."uarfcnUl",
t1."mnc",
t1."mcc",
t1."rncId",
t1."cId",
t1."userLabel",
t2."vsDataExternalUtranCell_id",
t2."individualOffset",
t2."maxTxPowerUl",
t2."qQualMin",
t2."qRxLevMin",
t2."agpsEnabled",
t2."cellCapability_hsdschSupport",
t2."cellCapability_edchSupport",
t2."cellCapability_edchTti2Support",
t2."cellCapability_enhancedL2Support",
t2."cellCapability_fdpchSupport",
t2."cellCapability_multiCarrierSupport",
t2."cellCapability_cpcSupport",
t2."cellCapability_qam64MimoSupport",
t2."transmissionScheme",
t2."parentSystem",
t2."mncLength",
t2."hsAqmCongCtrlSpiSupport",
t2."hsAqmCongCtrlSupport",
t2."srvccCapability",
t2."reportingRange1a",
t2."reportingRange1b",
t2."timeToTrigger1a",
t2."timeToTrigger1b",
t2."rimCapable",
t2."lbUtranCellOffloadCapacity",
t2."cellCapability"
FROM
ericsson_bulkcm."ExternalUtranCell" t1
INNER JOIN ericsson_bulkcm."vsDataExternalUtranCell" t2
 ON t1."ExternalUtranCell_id" = t2."ExternalUtranCell_id" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

GsmRelation = ReplaceableObject(
    'ericsson_cm_3g."GsmRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."UtranCell_id",
t1."GsmRelation_id",
t1."adjacentCell",
t2."vsDataGsmRelation_id",
t2."qOffset1sn",
t2."mobilityRelationType",
t2."selectionPriority"
FROM
ericsson_bulkcm."GsmRelation" t1
INNER JOIN ericsson_bulkcm."vsDataGsmRelation" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."UtranCell_id" = t2."UtranCell_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."GsmRelation_id" = t2."GsmRelation_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 
 AND t1."FileName" = t2."FileName" 

"""
)

IRPAgent = ReplaceableObject(
    'ericsson_cm_3g."IRPAgent"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "ManagementNode_id",
        "IRPAgent_id",
        "systemDN"
    FROM
    ericsson_bulkcm."IRPAgent"

    """
)

IubLink = ReplaceableObject(
    'ericsson_cm_3g."IubLink"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."IubLink_id",
t1."userLabel",
t1."iubLinkUtranCell",
t1."iubLinkNodeBFunction",
t2."vsDataIubLink_id",
t2."rbsId",
t2."dlHwAdm",
t2."ulHwAdm",
t2."rncModuleRef",
t2."userPlaneTransportOption_atm",
t2."userPlaneTransportOption_ipv4",
t2."controlPlaneTransportOption_atm",
t2."controlPlaneTransportOption_ipv4",
t2."userPlaneIpResourceRef",
t2."administrativeState",
t2."remoteCpIpAddress1",
t2."remoteCpIpAddress2",
t2."sctpRef",
t2."l2EstReqRetryTimeNbapC",
t2."l2EstReqRetryTimeNbapD",
t2."atmUserPlaneTermSubrackRef",
t2."cachedRemoteCpIpAddress1",
t2."cachedRemoteCpIpAddress2",
t2."userPlaneGbrAdmEnabled",
t2."userPlaneGbrAdmBandwidthDl",
t2."userPlaneGbrAdmBandwidthUl",
t2."userPlaneGbrAdmMarginDl",
t2."userPlaneGbrAdmMarginUl",
t2."softCongThreshGbrBwDl",
t2."softCongThreshGbrBwUl",
t2."spare",
t2."spareA",
t2."poolRedundancy",
t2."rncModulePreferredRef",
t2."rncModuleAllocWeight",
t2."linkType"
FROM
ericsson_bulkcm."IubLink" t1
INNER JOIN ericsson_bulkcm."vsDataIubLink" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 
 AND t1."IubLink_id" = t2."IubLink_id" 

"""
)

ManagedElement = ReplaceableObject(
    'ericsson_cm_3g."ManagedElement"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."ManagedElement_id",
t1."locationName",
t1."userDefinedState",
t1."vendorName",
t1."userLabel",
t1."managedElementType",
t1."swVersion",
t1."managedBy",
t1."dnPrefix",
t1."sourceType",
t1."release",
t1."siteRef",
t2."vsDataManagedElement_id",
t2."productType",
t2."productName",
t2."productNumber",
t2."productRevision",
t2."prodDesignation",
t2."logicalName",
t2."autoRestartRbs",
t2."generateAlarm",
t2."initCollectTraces",
t2."mirrorRelease",
t2."siteLocation",
t2."timeZone",
t2."dateTimeOffset",
t2."localDateTime"
FROM
ericsson_bulkcm."ManagedElement" t1
INNER JOIN ericsson_bulkcm."vsDataManagedElement" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 

"""
)

ManagementNode = ReplaceableObject(
    'ericsson_cm_3g."ManagementNode"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "ManagementNode_id",
        "manages",
        "userDefinedState",
        "locationName",
        "userLabel",
        "swVersion",
        "vendorName"
    FROM
    ericsson_bulkcm."ManagementNode"

    """
)

MeContext = ReplaceableObject(
    'ericsson_cm_3g."MeContext"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."dnPrefix",
t1."userLabel",
t1."ipAddress",
t1."segmentName",
t1."mimSwitchPolicy",
t1."neMIMversion",
t1."compatibilityOfMIMs",
t1."connectionStatus",
t1."mirrorMIBsynchStatus",
t1."mirrorMIBupdateStatus",
t1."generationCounter",
t1."neMIMName",
t1."neType",
t1."neCreationComplete",
t1."restartWarning",
t1."rollbackMirrorMIBname",
t1."neSecurityStatus",
t1."bcrLastChange",
t1."bctLastChange",
t1."telisLastChange",
t1."lostSynchronisation",
t1."nodeStartTime",
t1."pendingRestart",
t1."rbsGroupRef",
t2."vsDataMeContext_id",
t2."multiStandardRbs6k",
t2."mixedModeRadio",
t2."mirrorMIBversion",
t2."stnNodes",
t2."associatedNodes",
t2."associatedRadioNodes",
t2."associatedPicoNodes",
t2."rbsIubId",
t2."notificationsSupported",
t2."upgradeMethodCapability",
t2."createUpgradePackageCapability",
t2."lastProcessedEventTime",
t2."associatedRnc"
FROM
ericsson_bulkcm."MeContext" t1
INNER JOIN ericsson_bulkcm."vsDataMeContext" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."varDateTime" = t2."varDateTime" 

"""
)

NodeBFunction = ReplaceableObject(
    'ericsson_cm_3g."NodeBFunction"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."ManagedElement_id",
t1."NodeBFunction_id",
t1."nodeBFunctionIubLink",
t1."userLabel",
t1."nodeSCProfileID",
t1."eulNoReschUsers",
t1."eulTargetRate",
t1."eulMaxShoRate",
t1."eulSchedulingWeight",
t1."eulNonServHwRate",
t1."eulLowRate",
t1."eulMaxAllowedSchRate",
t2."vsDataNodeBFunction_id",
t2."toaeDch",
t2."branchDiffAbsTime",
t2."toaeCch",
t2."branchDiffMeasTime",
t2."steeredHsAllocation",
t2."ulLicFractBbPool2",
t2."dlLicFractBbPool2",
t2."iafAnrState",
t2."nbapDscp",
t2."analogUlAlignIsActive",
t2."sharedEquipmentController",
t2."featureStateStandardizedTma",
t2."featureStateStandardizedRet",
t2."featureStateDualStackIub",
t2."featureStateEul2msTti",
t2."featureStateDlPowerControlEul",
t2."featureStateGrake",
t2."featureStateMbmsIubEfficiency",
t2."featureState16Qam",
t2."featureState64Qam",
t2."featureStateHsdpaFlexibleScheduler",
t2."featureStateHsdpaImprovedLinkAdaptation",
t2."featureStateRetCascading",
t2."availableRbsChannelElementsDownlink",
t2."availableRbsChannelElementsUplink",
t2."licenseCapacityRbsChannelElementsDownlink",
t2."licenseCapacityRbsChannelElementsUplink",
t2."featureStateEulForLargeRbsConfig",
t2."featureStateIncrNumHsCodes",
t2."eul2msFirstSchedStep",
t2."featureStatePerHarqProcessGrant",
t2."featureStateDualTmaSupport",
t2."featureStateHsdpaMinBitRate",
t2."eulDchMaxAllowedSchRate",
t2."featureStateAbsoluteTimeSynch",
t2."featureStateMixedMode",
t2."featureStateHsdpaRbrQosProfiling",
t2."featureStateInterferenceSuppression",
t2."featureStatePsiCoverage",
t2."eulInactivityHighRateTime",
t2."eulInactivityLowRateTime",
t2."featureStateCeCapEul",
t2."featureStateHsAqmCongCtrl",
t2."featureStateRbsMpLoadSharing",
t2."licenseCapacityChannelElementDl",
t2."licenseCapacityChannelElementUl",
t2."spare",
t2."featureStateUlFcc",
t2."eulFachInitialRate",
t2."featureStateIntSuppEul10ms",
t2."technicianPresent",
t2."eulLowUsageTime",
t2."featureStateCeExtForEul",
t2."featureStateIncreasedHsCodeCap",
t2."alarmSuppressed",
t2."featureStateHsdpaMcInterDuSched",
t2."hsdpaMcInterDuSchedCapability",
t2."featureStateCombinedCell",
t2."featureStateImprovedDAgc",
t2."eulMaxTotalProtectedRate",
t2."licenseStateHsOlpc",
t2."featureStateIntSuppAllBearers",
t2."eulFachMaxDynAllocation",
t2."eulFachMinAllocation",
t2."featureStateCeEfficiencyEul",
t2."featureStateIncreasedCellCarrierSupport",
t2."ulLicFractBbPool",
t2."dlLicFractBbPool",
t2."featureStateUlCoMpReception",
t2."ulCoMpCapability",
t2."antennaDeviceScanStatus",
t2."featureStateEulLowLatencyPresched",
t2."stnNodes",
t2."release",
t2."dualBandSectorGroup1",
t2."dualBandSectorGroup2",
t2."dualBandSectorGroup3",
t2."dualBandSectorGroup4",
t2."dualBandSectorGroup5",
t2."dualBandSectorGroup6",
t2."featureStateMultiSectorPerRadio",
t2."featureStateUlSpectrumAnalyzer",
t2."nonEqPwrCommonPrecoderState"
FROM
ericsson_bulkcm."NodeBFunction" t1
INNER JOIN ericsson_bulkcm."vsDataNodeBFunction" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."NodeBFunction_id" = t2."NodeBFunction_id" 
 AND t1."FileName" = t2."FileName" 

"""
)

NotificationIRP = ReplaceableObject(
    'ericsson_cm_3g."NotificationIRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "ManagementNode_id",
        "IRPAgent_id",
        "NotificationIRP_id",
        "irpVersion"
    FROM
    ericsson_bulkcm."NotificationIRP"

    """
)

RncFunction = ReplaceableObject(
    'ericsson_cm_3g."RncFunction"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."userLabel",
t1."mcc",
t1."mnc",
t1."rncId",
t2."vsDataRncFunction_id",
t2."mncLength",
t2."emergencyCallRedirect",
t2."loadSharingDirRetryEnabled",
t2."hsCellChangeAllowed",
t2."hsOnlyBestCell",
t2."aliasPlmnIdentities_mcc",
t2."aliasPlmnIdentities_mnc",
t2."ctrFileSize",
t2."gpehDataLevel",
t2."gpehFileSize",
t2."loadSharingRrcEnabled",
t2."uetrFileSize",
t2."networkResourceIdentifierLengthCs",
t2."networkResourceIdentifierLengthPs",
t2."hsToDchTrigger_servHsChangeInterRnc",
t2."hsToDchTrigger_servHsChangeIntraRnc",
t2."hsToDchTrigger_changeOfBestCellIntraRnc",
t2."hsToDchTrigger_poorQualityDetected",
t2."hsToDchTrigger_changeOfBestCellInterRnc",
t2."ecLocationAttemptUmts",
t2."ecCnSbhoRequestIgnore",
t2."ecCnPriorityLevel",
t2."ecSbhoTimer",
t2."primaryCnOperatorRef",
t2."highPrioScanReserve",
t2."maxPowerOverloadHystTime",
t2."nbapDscp",
t2."mocnExternalNriMatching",
t2."maxAllowedGbrDlPsStream",
t2."nbapAuditInterval",
t2."pcapPositioningMode",
t2."iuSccpConRateMeasPeriod",
t2."iuSccpConRateThresh",
t2."intraNodeIpResourceRef",
t2."initialIuAccessRateMax",
t2."evolvedHsUePrioEnabled",
t2."evolvedHsUePrioLevel",
t2."evolvedHsUePrioLoadThresh",
t2."cyclicAcb_acbEnabled",
t2."cyclicAcb_rotationGroupSize",
t2."cyclicAcbCs_acbEnabled",
t2."cyclicAcbCs_rotationGroupSize",
t2."cyclicAcbPs_acbEnabled",
t2."cyclicAcbPs_rotationGroupSize",
t2."cyclicAcbRotationTime",
t2."spare",
t2."ctchAdmCtrl",
t2."hsFachEnabled",
t2."fastDormancyMethod",
t2."enhUeDrxEnabled",
t2."amrNbMmMrUlTfcRepeat",
t2."cbsFirstMsgDelayMargin",
t2."rimUtraSiRetries",
t2."rimUtraSiTimeout",
t2."rncType",
t2."spareA",
t2."spareB",
t2."spareC",
t2."eulFachEnabled",
t2."robustRwrEutraEnabled",
t2."offloadDedicPrioEutraTime",
t2."offloadDedicPrioEutraEnabled",
t2."mocnDedicPrioEutraEnabled",
t2."eulUsersAdmEulHsCcEnabled",
t2."nwInitCallReestTime",
t2."csPriorityRabSetupTime",
t2."aliasPlmnIdentities"
FROM
ericsson_bulkcm."RncFunction" t1
INNER JOIN ericsson_bulkcm."vsDataRncFunction" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 

"""
)

SubNetwork = ReplaceableObject(
    'ericsson_cm_3g."SubNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id"
    FROM
    ericsson_bulkcm."SubNetwork"

    """
)

SubNetwork_2 = ReplaceableObject(
    'ericsson_cm_3g."SubNetwork_2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "userDefinedNetworkType",
        "userLabel"
    FROM
    ericsson_bulkcm."SubNetwork_2"

    """
)

UtranCell = ReplaceableObject(
    'ericsson_cm_3g."UtranCell"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."UtranCell_id",
t1."localCellId",
t1."uarfcnUl",
t1."uarfcnDl",
t1."primaryScramblingCode",
t1."primaryCpichPower",
t1."maximumTransmissionPower",
t1."primarySchPower",
t1."cId",
t1."userLabel",
t1."secondarySchPower",
t1."bchPower",
t1."lac",
t1."rac",
t1."sac",
t1."utranCellIubLink",
t1."uraList",
t1."creationTime",
t2."vsDataUtranCell_id",
t2."lbUtranCellOffloadCapacity",
t2."tCell",
t2."cellReserved",
t2."anrBlackList",
t2."treSelection",
t2."qualMeasQuantity",
t2."qHyst1",
t2."qHyst2",
t2."qQualMin",
t2."qRxLevMin",
t2."individualOffset",
t2."pwrAdm",
t2."pwrOffset",
t2."pwrHyst",
t2."tmCongAction",
t2."releaseAseDl",
t2."aseDlAdm",
t2."dlCodeAdm",
t2."aseUlAdm",
t2."sf8Adm",
t2."sf32Adm",
t2."minPwrRl",
t2."maxRate",
t2."interRate",
t2."minimumRate",
t2."maxPwrMax",
t2."interPwrMax",
t2."minPwrMax",
t2."compModeAdm",
t2."iFHyst",
t2."iFCong",
t2."interFreqFddMeasIndicator",
t2."sRatSearch",
t2."sIntraSearch",
t2."sInterSearch",
t2."fachMeasOccaCycLenCoeff",
t2."accessClassNBarred",
t2."utranCellPosition",
t2."maxTxPowerUl",
t2."reservedBy",
t2."sib1PlmnScopeValueTag",
t2."sf16Adm",
t2."hoType",
t2."usedFreqThresh2dEcno",
t2."usedFreqThresh2dRscp",
t2."administrativeState",
t2."loadSharingGsmThreshold",
t2."loadSharingGsmFraction",
t2."snDirectedRetryTarget",
t2."rlFailureT",
t2."nOutSyncInd",
t2."sf4AdmUl",
t2."hardIfhoCorr",
t2."hsdpaUsersAdm",
t2."loadSharingMargin",
t2."sHcsRat",
t2."sf16gAdm",
t2."releaseAseDlNg",
t2."tmCongActionNg",
t2."tmInitialG",
t2."sf16AdmUl",
t2."sf8AdmUl",
t2."sf8gAdmUl",
t2."iubLinkRef",
t2."eulNonServingCellUsersAdm",
t2."eulServingCellUsersAdm",
t2."agpsEnabled",
t2."codeLoadThresholdDlSf128",
t2."pwrLoadThresholdDlSpeech_amr12200",
t2."pwrLoadThresholdDlSpeech_amr7950",
t2."pwrLoadThresholdDlSpeech_amr5900",
t2."pwrLoadThresholdDlSpeech_amrWb8850",
t2."pwrLoadThresholdDlSpeech_amrWb12650",
t2."aseLoadThresholdUlSpeech_amr12200",
t2."aseLoadThresholdUlSpeech_amr7950",
t2."aseLoadThresholdUlSpeech_amr5900",
t2."aseLoadThresholdUlSpeech_amrWb8850",
t2."aseLoadThresholdUlSpeech_amrWb12650",
t2."accessClassesBarredCs",
t2."accessClassesBarredPs",
t2."rateSelectionPsInteractive_channelType",
t2."rateSelectionPsInteractive_ulPrefRate",
t2."rateSelectionPsInteractive_dlPrefRate",
t2."hcsUsage_idleMode",
t2."hcsUsage_connectedMode",
t2."hcsSib3Config_hcsPrio",
t2."hcsSib3Config_qHcs",
t2."hcsSib3Config_sSearchHcs",
t2."amrWbRateUlMax",
t2."amrWbRateDlMax",
t2."antennaPosition_latitudeSign",
t2."antennaPosition_latitude",
t2."antennaPosition_longitude",
t2."mocnCellProfileRef",
t2."standAloneSrbSelector",
t2."amrNbSelector",
t2."eulServingCellUsersAdmTti2",
t2."cellBroadcastSac",
t2."ctchOccasionPeriod",
t2."transmissionScheme",
t2."loadBasedHoSupport",
t2."useId",
t2."cbsSchedulePeriodLength",
t2."fdpchSupport",
t2."ganHoEnabled",
t2."loadBasedHoType",
t2."serviceRestrictions_csVideoCalls",
t2."hsIflsThreshUsers",
t2."hsIflsMarginUsers",
t2."dchIflsThreshPower",
t2."dchIflsThreshCode",
t2."dchIflsMarginPower",
t2."dchIflsMarginCode",
t2."pathlossThreshold",
t2."iflsMode",
t2."cpcSupport",
t2."absPrioCellRes_cellReselectionPriority",
t2."absPrioCellRes_sPrioritySearch1",
t2."absPrioCellRes_sPrioritySearch2",
t2."absPrioCellRes_threshServingLow",
t2."absPrioCellRes_measIndFach",
t2."spare",
t2."secondaryCpichPower",
t2."ctchAdmMargin",
t2."rrcLcEnabled",
t2."mixedModeRadio",
t2."sf128Adm",
t2."sf64AdmUl",
t2."admBlockRedirection_gsmRrc",
t2."admBlockRedirection_rrc",
t2."admBlockRedirection_speech",
t2."dmcrEnabled",
t2."hsIflsHighLoadThresh",
t2."hsIflsSpeechMultiRabTrigg",
t2."cyclicAcb_acbEnabled",
t2."cyclicAcb_rotationGroupSize",
t2."cyclicAcbCs_acbEnabled",
t2."cyclicAcbCs_rotationGroupSize",
t2."cyclicAcbPs_acbEnabled",
t2."cyclicAcbPs_rotationGroupSize",
t2."releaseRedirect",
t2."releaseRedirectEutraTriggers_csFallbackCsRelease",
t2."releaseRedirectEutraTriggers_csFallbackDchToFach",
t2."releaseRedirectEutraTriggers_dchToFach",
t2."releaseRedirectEutraTriggers_fachToUra",
t2."releaseRedirectEutraTriggers_fastDormancy",
t2."releaseRedirectEutraTriggers_normalRelease",
t2."spareA",
t2."srbAdmExempt",
t2."reportingRange1a",
t2."reportingRange1b",
t2."timeToTrigger1a",
t2."timeToTrigger1b",
t2."downswitchTimer",
t2."hsdschInactivityTimer",
t2."hsdschInactivityTimerCpc",
t2."inactivityTimeMultiPsInteractive",
t2."inactivityTimer",
t2."inactivityTimerEnhUeDrx",
t2."inactivityTimerPch",
t2."redirectUarfcn",
t2."dnclEnabled",
t2."servDiffRrcAdmHighPrioProfile",
t2."anrIafUtranCellConfig_anrEnabled",
t2."anrIafUtranCellConfig_relationAddEnabled",
t2."dlCodeOffloadLimit",
t2."dlPowerOffloadLimit",
t2."hsdpaUsersOffloadLimit",
t2."hsIflsDownswitchTrigg_toFach",
t2."hsIflsDownswitchTrigg_toUra",
t2."hsIflsDownswitchTrigg_fastDormancy",
t2."hsIflsPowerLoadThresh",
t2."hsIflsRedirectLoadLimit",
t2."hsIflsTrigger_fromFach",
t2."hsIflsTrigger_fromUra",
t2."iflsCpichEcnoThresh",
t2."iflsRedirectUarfcn",
t2."releaseRedirectHsIfls",
t2."pagingPermAccessCtrl_locRegAcb",
t2."pagingPermAccessCtrl_locRegRestr",
t2."pagingPermAccessCtrl_pagingRespRestr",
t2."ueHsThpMeasSupport",
t2."updateLocator",
t2."autoAcbRcssrThresh",
t2."autoAcbRtwpThresh",
t2."autoAcbMinRcssrInput",
t2."autoAcbRcssrWeight",
t2."autoAcbMaxPsClassesToBar",
t2."autoAcbRtwpWeight",
t2."autoAcbEnabled",
t2."supportedCellType",
t2."rwrEutraCc",
t2."eulMcServingCellUsersAdmTti2",
t2."primaryTpsCell",
t2."tpsPowerLockState",
t2."tpsCellThresholds_tpsCellThreshEnabled",
t2."tpsCellThresholds_tpsLockThreshold",
t2."tpsCellThresholds_tpsUnlockThreshold",
t2."dlCodePowerCmEnabled",
t2."poolRedundancy",
t2."rachOverloadProtect",
t2."srvccCapability",
t2."rimCapable",
t2."ifIratHoPsIntHsEnabled",
t2."cellUpdateConfirmPsInitRepeat",
t2."cellUpdateConfirmCsInitRepeat"
FROM
ericsson_bulkcm."UtranCell" t1
INNER JOIN ericsson_bulkcm."vsDataUtranCell" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."UtranCell_id" = t2."UtranCell_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."FileName" = t2."FileName" 

"""
)

UtranRelation = ReplaceableObject(
    'ericsson_cm_3g."UtranRelation"',
    """

SELECT 
t1."FileName",
t1."varDateTime",
t1."configData_dnPrefix",
t1."SubNetwork_id",
t1."SubNetwork_2_id",
t1."MeContext_id",
t1."ManagedElement_id",
t1."RncFunction_id",
t1."UtranCell_id",
t1."UtranRelation_id",
t1."adjacentCell",
t2."vsDataUtranRelation_id",
t2."qOffset1sn",
t2."qOffset2sn",
t2."loadSharingCandidate",
t2."selectionPriority",
t2."frequencyRelationType",
t2."nodeRelationType",
t2."hcsSib11Config_hcsPrio",
t2."hcsSib11Config_qHcs",
t2."hcsSib11Config_penaltyTime",
t2."hcsSib11Config_temporaryOffset1",
t2."hcsSib11Config_temporaryOffset2",
t2."mobilityRelationType",
t2."createdBy",
t2."creationTime"
FROM
ericsson_bulkcm."UtranRelation" t1
INNER JOIN ericsson_bulkcm."vsDataUtranRelation" t2
 ON t1."MeContext_id" = t2."MeContext_id" 
 AND t1."UtranCell_id" = t2."UtranCell_id" 
 AND t1."SubNetwork_id" = t2."SubNetwork_id" 
 AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id" 
 AND t1."ManagedElement_id" = t2."ManagedElement_id" 
 AND t1."FileName" = t2."FileName" 
 AND t1."UtranRelation_id" = t2."UtranRelation_id" 
 AND t1."varDateTime" = t2."varDateTime" 
 AND t1."configData_dnPrefix" = t2."configData_dnPrefix" 
 AND t1."RncFunction_id" = t2."RncFunction_id" 

"""
)

Aal0TpVccTp = ReplaceableObject(
    'ericsson_cm_3g."Aal0TpVccTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal0TpVccTp_id",
        "alarmReport",
        "continuityCheck",
        "nomPmBlkSize",
        "processorId",
        "userLabel",
        "vclTpId",
        "counterMode"
    FROM
    ericsson_bulkcm."vsDataAal0TpVccTp"

    """
)

Aal2Ap = ReplaceableObject(
    'ericsson_cm_3g."Aal2Ap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal2Sp_id",
        "vsDataAal2Ap_id",
        "aal2QoSCodePointProfileId",
        "rpuId",
        "secondarySigLinkId",
        "sigLinkId",
        "timerErq",
        "timerRel",
        "userLabel",
        "allocationMode"
    FROM
    ericsson_bulkcm."vsDataAal2Ap"

    """
)

Aal2PathDistributionUnit = ReplaceableObject(
    'ericsson_cm_3g."Aal2PathDistributionUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal2Sp_id",
        "vsDataAal2Ap_id",
        "vsDataAal2PathDistributionUnit_id",
        "userLabel",
        "rpuId",
        "aal2PathVccTpList"
    FROM
    ericsson_bulkcm."vsDataAal2PathDistributionUnit"

    """
)

Aal2PathVccTp = ReplaceableObject(
    'ericsson_cm_3g."Aal2PathVccTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal2PathVccTp_id",
        "aal2PathOwner",
        "alarmReport",
        "nomPmBlocksize",
        "timerCu",
        "userLabel",
        "administrativeState",
        "continuityCheck",
        "aal2PathId",
        "vclTpId",
        "aal2QoSAvailableProfiles",
        "aal2QoSProfileId",
        "counterMode",
        "counterActivation"
    FROM
    ericsson_bulkcm."vsDataAal2PathVccTp"

    """
)

Aal2QosCodePointProfile = ReplaceableObject(
    'ericsson_cm_3g."Aal2QosCodePointProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal2QosCodePointProfile_id",
        "userLabel",
        "qualityOfServiceCodePointA",
        "qualityOfServiceCodePointB",
        "qualityOfServiceCodePointC",
        "qualityOfServiceCodePointD"
    FROM
    ericsson_bulkcm."vsDataAal2QosCodePointProfile"

    """
)

Aal2QosProfile = ReplaceableObject(
    'ericsson_cm_3g."Aal2QosProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal2QosProfile_id",
        "profileClassA_boundOnProbOfDelay",
        "profileClassA_boundOnProbOfLoss",
        "profileClassA_boundOnNodeDelay",
        "profileClassB_boundOnProbOfDelay",
        "profileClassB_boundOnProbOfLoss",
        "profileClassB_boundOnNodeDelay",
        "profileClassC_boundOnProbOfDelay",
        "profileClassC_boundOnProbOfLoss",
        "profileClassC_boundOnNodeDelay",
        "profileClassD_boundOnProbOfDelay",
        "profileClassD_boundOnProbOfLoss",
        "profileClassD_boundOnNodeDelay",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAal2QosProfile"

    """
)

Aal2RoutingCase = ReplaceableObject(
    'ericsson_cm_3g."Aal2RoutingCase"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal2RoutingCase_id",
        "userLabel",
        "numberDirection",
        "routeList",
        "routePriorityList"
    FROM
    ericsson_bulkcm."vsDataAal2RoutingCase"

    """
)

Aal2Sp = ReplaceableObject(
    'ericsson_cm_3g."Aal2Sp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal2Sp_id",
        "a2ea",
        "userLabel",
        "afi"
    FROM
    ericsson_bulkcm."vsDataAal2Sp"

    """
)

Aal5TpVccTp = ReplaceableObject(
    'ericsson_cm_3g."Aal5TpVccTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAal5TpVccTp_id",
        "alarmReport",
        "continuityCheck",
        "fromUserMaxSduSize",
        "nomPmBlkSize",
        "processorId",
        "toUserMaxSduSize",
        "userLabel",
        "vclTpId",
        "counterMode",
        "counterActivation"
    FROM
    ericsson_bulkcm."vsDataAal5TpVccTp"

    """
)

AccessControlList = ReplaceableObject(
    'ericsson_cm_3g."AccessControlList"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataAccessControlList_id",
        "aclEntries_localIpAddress",
        "aclEntries_remoteIpAddress",
        "aclEntries_localPortFiltering",
        "aclEntries_remotePortFiltering",
        "aclEntries_protocol",
        "aclEntries_aclAction",
        "aclEntries_localIpAddressMask",
        "aclEntries_localPort",
        "aclEntries_remoteIpAddressMask",
        "aclEntries_remotePort",
        "aclEntries_icmpType",
        "userLabel",
        "bypassNdpAndMld"
    FROM
    ericsson_bulkcm."vsDataAccessControlList"

    """
)

AddressIPv4 = ReplaceableObject(
    'ericsson_cm_3g."AddressIPv4"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataInterfaceIpv4_id",
        "vsDataAddressIpv4_id",
        "vsDataVrrpv3Interface_id",
        "address",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAddressIPv4"

    """
)

AdmissionControl = ReplaceableObject(
    'ericsson_cm_3g."AdmissionControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAdmissionControl_id",
        "dlTransNwBandwidth",
        "ulTransNwBandwidth",
        "paArpOverride",
        "arpBasedPreEmptionState",
        "resourceReservationForPAState",
        "zzzTemporary1",
        "zzzTemporary2",
        "zzzTemporary3",
        "zzzTemporary4",
        "zzzTemporary5",
        "zzzTemporary6",
        "zzzTemporary7",
        "zzzTemp1",
        "zzzTemp2",
        "zzzTemp3",
        "zzzTemp4",
        "zzzTemp5",
        "zzzTemp6",
        "zzzTemp7",
        "zzzTemp8",
        "zzzTemp9",
        "zzzTemp10",
        "zzzTemp11",
        "zzzTemp12",
        "zzzTemp13",
        "zzzTemp14",
        "zzzTemp15",
        "zzzTemp16",
        "zzzTemp17",
        "zzzTemp18",
        "zzzTemp19",
        "zzzTemp20",
        "zzzTemp21",
        "dlMbmsGbrRatio",
        "resourceReservationForDifferentiation",
        "dlAdmOverloadThr",
        "admNrRbDifferentiationThr",
        "nrOfRbReservationsPerPaConn",
        "dlAdmDifferentiationThr",
        "ulAdmDifferentiationThr",
        "nrOfPaConnReservationsPerCell",
        "ulAdmOverloadThr",
        "admNrRrcDifferentiationThr",
        "admResourceMinQciPrio",
        "zzzTemporary22",
        "zzzTemporary25",
        "zzzTemporary26",
        "zzzTemporary23",
        "zzzTemporary24",
        "lbAtoThresholdLevel2",
        "lbAtoThresholdLevel1",
        "maxVolteUe",
        "maxReservedUe",
        "maxActiveUe"
    FROM
    ericsson_bulkcm."vsDataAdmissionControl"

    """
)

AdvCellSup = ReplaceableObject(
    'ericsson_cm_3g."AdvCellSup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataAdvCellSup_id",
        "featureStateAdvCellSup",
        "keyIdAdvCellSup",
        "licenseStateAdvCellSup",
        "serviceStateAdvCellSup"
    FROM
    ericsson_bulkcm."vsDataAdvCellSup"

    """
)

AgpsPositioning = ReplaceableObject(
    'ericsson_cm_3g."AgpsPositioning"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUePositioning_id",
        "vsDataAgpsPositioning_id",
        "altitudeDirection",
        "altitude",
        "uncertaintyAltitude",
        "confidence",
        "polygonRadiusFactor",
        "utranRnsPosition_latitudeSign",
        "utranRnsPosition_latitude",
        "utranRnsPosition_longitude",
        "utranRnsUncertaintyRadius",
        "utranRnsConfidence",
        "elevationThreshold",
        "posQualities_responseTimeTypical",
        "posQualities_accuracyCodeTypical",
        "posQualities_verticalAccuracyCodeTypical",
        "posQualities_confidenceEstimate"
    FROM
    ericsson_bulkcm."vsDataAgpsPositioning"

    """
)

AiDevice = ReplaceableObject(
    'ericsson_cm_3g."AiDevice"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRruDeviceGroup_id",
        "vsDataAiDeviceSet_id",
        "vsDataAiDevice_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "vsDataDeviceGroup_id",
        "administrativeState",
        "reservedBy",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAiDevice"

    """
)

AiDeviceSet = ReplaceableObject(
    'ericsson_cm_3g."AiDeviceSet"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRruDeviceGroup_id",
        "vsDataAiDeviceSet_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "vsDataDeviceGroup_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAiDeviceSet"

    """
)

AirIfLoadGenerator = ReplaceableObject(
    'ericsson_cm_3g."AirIfLoadGenerator"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataAirIfLoadGenerator_id",
        "keyIdAilg",
        "featureStateAilg",
        "licenseStateAilg",
        "serviceStateAilg"
    FROM
    ericsson_bulkcm."vsDataAirIfLoadGenerator"

    """
)

AirIfLoadProfile = ReplaceableObject(
    'ericsson_cm_3g."AirIfLoadProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAirIfLoadProfile_id",
        "ailgHighPrio",
        "ailgLowPrioModType",
        "dlPrbLoadLevel",
        "noOfOcngPrbSeries",
        "ocngPrbSerie_pdschModType",
        "ocngPrbSerie_prbFirst",
        "ocngPrbSerie_prbLast",
        "ocngPrbSerie_usedSubFrameNo",
        "trafficModelPrb_bufferStatus",
        "trafficModelPrb_noOfArtificialUsers",
        "trafficModelPrb_qciDistSinrHigh",
        "trafficModelPrb_qciDistSinrMedium",
        "trafficModelPrb_qciDistSinrLow",
        "trafficModelPrb_ulDlRatioPerQci",
        "trafficModelPrb_bitRatePerQci",
        "userLabel",
        "zzzTemporary1",
        "zzzTemporary2",
        "zzzTemporary3",
        "zzzTemporary4",
        "zzzTemporary5",
        "zzzTemporary6",
        "zzzTemporary7",
        "ailgChangePeriod",
        "ailgLoadType",
        "minLoadLevelPdcch",
        "zzzTemporary9",
        "zzzTemporary8"
    FROM
    ericsson_bulkcm."vsDataAirIfLoadProfile"

    """
)

Aisgv2FwDownload = ReplaceableObject(
    'ericsson_cm_3g."Aisgv2FwDownload"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataAisgv2FwDownload_id",
        "keyIdAisgv2FwDownload",
        "featureStateAisgv2FwDownload",
        "licenseStateAisgv2FwDownload",
        "serviceStateAisgv2FwDownload"
    FROM
    ericsson_bulkcm."vsDataAisgv2FwDownload"

    """
)

AlarmPort = ReplaceableObject(
    'ericsson_cm_3g."AlarmPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataFieldReplaceableUnit_id",
        "vsDataAlarmPort_id",
        "availabilityStatus",
        "activeExternalAlarm",
        "normallyOpen",
        "alarmSlogan",
        "administrativeState",
        "perceivedSeverity",
        "operationalState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAlarmPort"

    """
)

AmoFunction = ReplaceableObject(
    'ericsson_cm_3g."AmoFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAmoFunction_id",
        "amoAllowedInterVendor"
    FROM
    ericsson_bulkcm."vsDataAmoFunction"

    """
)

Anr = ReplaceableObject(
    'ericsson_cm_3g."Anr"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataAnr_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "spare",
        "anrCellAddRelationMax",
        "anrPersistentStorageEnabled",
        "featureStateAnr",
        "keyIdAnr",
        "licenseStateAnr",
        "serviceStateAnr"
    FROM
    ericsson_bulkcm."vsDataAnr"

    """
)

AnrFunction = ReplaceableObject(
    'ericsson_cm_3g."AnrFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAnrFunction_id",
        "removeNcellTime",
        "removeNenbTime",
        "removeNrelTime",
        "zzzTemporary1",
        "zzzTemporary2",
        "zzzTemporary3",
        "zzzTemporary4",
        "zzzTemporary5",
        "zzzTemporary6",
        "zzzTemporary7",
        "prioHoRate",
        "prioHoSuccRate",
        "prioTime",
        "maxNoPciReportsEvent",
        "maxTimeEventBasedPciConf",
        "cellRelHoAttRateThreshold",
        "zzzTemporary9",
        "zzzTemporary8",
        "zzzTemporary10",
        "zzzTemporary11",
        "zzzTemporary12",
        "probCellDetectMedHoSuccTime",
        "probCellDetectLowHoSuccTime",
        "problematicCellPolicy",
        "probCellDetectMedHoSuccThres",
        "probCellDetectLowHoSuccThres",
        "plmnWhiteListEnabled",
        "perEcgiMeasPlmnWhiteList",
        "maxNoPciReportsInact",
        "nrHoNeededToAddCellRelation"
    FROM
    ericsson_bulkcm."vsDataAnrFunction"

    """
)

AnrFunctionCdma20001xRtt = ReplaceableObject(
    'ericsson_cm_3g."AnrFunctionCdma20001xRtt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAnrFunction_id",
        "vsDataAnrFunctionCdma20001xRtt_id",
        "excludeNid",
        "anrCdma20001xRttStatus",
        "cellAddThresholdDelta",
        "extendedCellRangeEnabled",
        "namingConvention"
    FROM
    ericsson_bulkcm."vsDataAnrFunctionCdma20001xRtt"

    """
)

AnrFunctionEUtran = ReplaceableObject(
    'ericsson_cm_3g."AnrFunctionEUtran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAnrFunction_id",
        "vsDataAnrFunctionEUtran_id",
        "anrInterFreqState",
        "anrIntraFreqState",
        "anrUesEUtraIntraFDecr",
        "anrUesEUtraIntraFIncrHo",
        "anrUesEUtraIntraFMax",
        "anrUesEUtraIntraFMin",
        "anrUesThreshInterFDecr",
        "anrUesThreshInterFIncrAnr",
        "anrUesThreshInterFIncrHo",
        "anrUesThreshInterFMax",
        "anrUesThreshInterFMin",
        "cellAddRsrpThresholdEutran",
        "cellAddRsrqThresholdEutran",
        "hoAllowedEutranPolicy",
        "x2SetupPolicy",
        "anrUesEUtraIntraFIncrAnr",
        "lbCellOffloadCapacityPolicy",
        "anrEutranInterFMeasReportMin",
        "anrEutranInterFMeasReportIncr",
        "anrEutranInterFMeasReportMax",
        "anrEutranInterFMeasReportDecr",
        "anrIntraFreqStatus",
        "anrInterFreqStatus"
    FROM
    ericsson_bulkcm."vsDataAnrFunctionEUtran"

    """
)

AnrFunctionGeran = ReplaceableObject(
    'ericsson_cm_3g."AnrFunctionGeran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAnrFunction_id",
        "vsDataAnrFunctionGeran_id",
        "anrStateGsm",
        "anrGeranMeasReportDecr",
        "anrGeranMeasReportIncr",
        "anrGeranMeasReportMax",
        "anrGeranMeasReportMin",
        "rimIntegrationEnabled",
        "anrGeranMeasReportRacIncr",
        "anrGeranRacMeasOn"
    FROM
    ericsson_bulkcm."vsDataAnrFunctionGeran"

    """
)

AnrFunctionUtran = ReplaceableObject(
    'ericsson_cm_3g."AnrFunctionUtran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAnrFunction_id",
        "vsDataAnrFunctionUtran_id",
        "anrStateUtran",
        "anrUtranMeasReportDecr",
        "anrUtranMeasReportIncr",
        "anrUtranMeasReportMax",
        "anrUtranMeasReportMin",
        "anrUtranAcMeasOn",
        "anrUtranMeasReportAcIncr",
        "hoAllowedUtranPolicy",
        "rimIntegrationEnabled",
        "cellAddEcNoThresholdUtranDelta",
        "cellAddRscpThresholdUtranDelta",
        "srvccPolicy"
    FROM
    ericsson_bulkcm."vsDataAnrFunctionUtran"

    """
)

AnrIafUtran = ReplaceableObject(
    'ericsson_cm_3g."AnrIafUtran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataAnr_id",
        "vsDataAnrIafUtran_id",
        "anrEnabled",
        "anrDsReportFilterEnabled",
        "anrCandidateUpperThresh",
        "anrCandidateExpirePeriod",
        "anrCandidateLowerThresh",
        "anrAddRelationEnabled",
        "anrCandidateAbsPropThresh",
        "anrDsReportFilterRscp",
        "anrDsReportFilterEcno",
        "anrAttRatioBadCrs"
    FROM
    ericsson_bulkcm."vsDataAnrIafUtran"

    """
)

AntennaBranch = ReplaceableObject(
    'ericsson_cm_3g."AntennaBranch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAntennaBranch_id",
        "branchName",
        "mechanicalAntennaTilt",
        "fqBandHighEdge",
        "antennaSupervisionThreshold",
        "fqBandLowEdge",
        "lowCurrentSupervision"
    FROM
    ericsson_bulkcm."vsDataAntennaBranch"

    """
)

AntennaNearUnit = ReplaceableObject(
    'ericsson_cm_3g."AntennaNearUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "vsDataAntennaNearUnit_id",
        "rfPortRef",
        "serialNumber",
        "uniqueId",
        "productNumber",
        "iuantDeviceType",
        "onUnitUniqueId",
        "administrativeState",
        "anuType",
        "softwareVersion",
        "hardwareVersion"
    FROM
    ericsson_bulkcm."vsDataAntennaNearUnit"

    """
)

AntennaSubunit = ReplaceableObject(
    'ericsson_cm_3g."AntennaSubunit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "vsDataAntennaUnit_id",
        "vsDataAntennaSubunit_id",
        "maxTotalTilt",
        "minTotalTilt",
        "retSubunitRef",
        "totalTilt",
        "azimuthHalfPowerBeamwidth",
        "commonChBeamfrmPortMap",
        "customComChBeamfrmWtsPhase",
        "customComChBeamfrmWtsAmplitude"
    FROM
    ericsson_bulkcm."vsDataAntennaSubunit"

    """
)

AntennaUnit = ReplaceableObject(
    'ericsson_cm_3g."AntennaUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "vsDataAntennaUnit_id",
        "mechanicalAntennaTilt"
    FROM
    ericsson_bulkcm."vsDataAntennaUnit"

    """
)

AntennaUnitGroup = ReplaceableObject(
    'ericsson_cm_3g."AntennaUnitGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "positionInformation",
        "positionRef"
    FROM
    ericsson_bulkcm."vsDataAntennaUnitGroup"

    """
)

AntFeederCable = ReplaceableObject(
    'ericsson_cm_3g."AntFeederCable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntFeederCable_id",
        "ulAttenuation",
        "dlAttenuation",
        "electricalUlDelay",
        "electricalDlDelay",
        "antennaBranchRef",
        "connectedToObjectARef",
        "objectAConnector"
    FROM
    ericsson_bulkcm."vsDataAntFeederCable"

    """
)

Areas = ReplaceableObject(
    'ericsson_cm_3g."Areas"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataAreas_id"
    FROM
    ericsson_bulkcm."vsDataAreas"

    """
)

ArpMap = ReplaceableObject(
    'ericsson_cm_3g."ArpMap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRabHandling_id",
        "vsDataArpQosClassProfile_id",
        "vsDataTrafficClass_id",
        "vsDataArpMap_id",
        "vsDataTrafficClassPsInt_id",
        "userLabel",
        "defaultArpQos_intPrio",
        "defaultArpQos_pci",
        "defaultArpQos_pvi",
        "externalArpMapping",
        "systemDefaultArpQos_intPrio",
        "systemDefaultArpQos_pci",
        "systemDefaultArpQos_pvi"
    FROM
    ericsson_bulkcm."vsDataArpMap"

    """
)

ArpQosClassProfile = ReplaceableObject(
    'ericsson_cm_3g."ArpQosClassProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRabHandling_id",
        "vsDataArpQosClassProfile_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataArpQosClassProfile"

    """
)

AtmConfService = ReplaceableObject(
    'ericsson_cm_3g."AtmConfService"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAtmConfService_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAtmConfService"

    """
)

AtmPort = ReplaceableObject(
    'ericsson_cm_3g."AtmPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAtmPort_id",
        "userLabel",
        "uses",
        "hecCorrectionMode",
        "loopbackDetection"
    FROM
    ericsson_bulkcm."vsDataAtmPort"

    """
)

AtmTrafficDescriptor = ReplaceableObject(
    'ericsson_cm_3g."AtmTrafficDescriptor"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAtmTrafficDescriptor_id",
        "egressAtmMcr",
        "egressAtmPcr",
        "egressAtmQos",
        "ingressAtmMcr",
        "ingressAtmPcr",
        "ingressAtmQos",
        "serviceCategory",
        "userLabel",
        "packetDiscard"
    FROM
    ericsson_bulkcm."vsDataAtmTrafficDescriptor"

    """
)

AuPort = ReplaceableObject(
    'ericsson_cm_3g."AuPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "vsDataAntennaUnit_id",
        "vsDataAntennaSubunit_id",
        "vsDataAuPort_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAuPort"

    """
)

AuthenticationOrder = ReplaceableObject(
    'ericsson_cm_3g."AuthenticationOrder"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataAuthenticationOrder_id",
        "authenticationMethodOrder_orderNumber",
        "authenticationMethodOrder_methodReference",
        "authenticationMethodOrder_userLabel",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAuthenticationOrder"

    """
)

AuthorizationOrder = ReplaceableObject(
    'ericsson_cm_3g."AuthorizationOrder"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataAuthorizationOrder_id",
        "authorizationMethodOrder_orderNumber",
        "authorizationMethodOrder_methodReference",
        "authorizationMethodOrder_userLabel",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataAuthorizationOrder"

    """
)

AutoCellCapEstFunction = ReplaceableObject(
    'ericsson_cm_3g."AutoCellCapEstFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataAutoCellCapEstFunction_id",
        "useEstimatedCellCap"
    FROM
    ericsson_bulkcm."vsDataAutoCellCapEstFunction"

    """
)

AutonomousMode = ReplaceableObject(
    'ericsson_cm_3g."AutonomousMode"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataAutonomousMode_id",
        "expiration",
        "activationState"
    FROM
    ericsson_bulkcm."vsDataAutonomousMode"

    """
)

AutoProvisioning = ReplaceableObject(
    'ericsson_cm_3g."AutoProvisioning"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "vsDataAutoProvisioning_id",
        "rbsConfigLevel"
    FROM
    ericsson_bulkcm."vsDataAutoProvisioning"

    """
)

AuxPlugInUnit = ReplaceableObject(
    'ericsson_cm_3g."AuxPlugInUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataSectorAntenna_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "administrativeState",
        "piuType",
        "position",
        "positionInformation",
        "positionRef",
        "productData_productionDate",
        "productData_productName",
        "productData_productNumber",
        "productData_productRevision",
        "productData_serialNumber",
        "unitType",
        "positionCoordinates_geoDatum",
        "positionCoordinates_altitude",
        "positionCoordinates_latitude",
        "positionCoordinates_longitude",
        "supportUnitRef",
        "uniqueHwId"
    FROM
    ericsson_bulkcm."vsDataAuxPlugInUnit"

    """
)

BatteryBackup = ReplaceableObject(
    'ericsson_cm_3g."BatteryBackup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipmentSupportFunction_id",
        "vsDataBatteryBackup_id",
        "batteryTestIsRunning",
        "batteryDisconnectTempCeaseOffset",
        "boostChargeTime",
        "boostChargeTriggerVoltage",
        "chargeMaxCurrent",
        "chargingMode",
        "equalizeChargeCyclicInterval",
        "equalizeChargeTime",
        "intermittentChargeConnectTime",
        "intermittentChargeConnectVoltage",
        "intermittentChargeDisconnectTime",
        "minimumBackupTime",
        "minimumStateOfHealth",
        "nominalTemp",
        "sharedBattery",
        "tempCompMaxVoltage",
        "tempCompMinVoltage",
        "tempCompVoltageSlope",
        "testMode",
        "testStartDay",
        "testStartMonths",
        "controlDomainRef",
        "extendedSoftwareControl",
        "floatChargeVoltage",
        "batteryDisconnectHighTemp",
        "elevatedChargeVoltage",
        "batteryDisconnectTemp",
        "batteryType",
        "chargingVoltage",
        "increasedChargeVoltage"
    FROM
    ericsson_bulkcm."vsDataBatteryBackup"

    """
)

BbProcessingResource = ReplaceableObject(
    'ericsson_cm_3g."BbProcessingResource"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataDeviceGroup_id",
        "vsDataBbProcessingResource_id",
        "vsDataFieldReplaceableUnit_id",
        "licCapDistr"
    FROM
    ericsson_bulkcm."vsDataBbProcessingResource"

    """
)

BestNeighborSI = ReplaceableObject(
    'ericsson_cm_3g."BestNeighborSI"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataBestNeighborSI_id",
        "featureStateBestNeighborSI",
        "keyIdBestNeighborSI",
        "licenseStateBestNeighborSI",
        "serviceStateBestNeighborSI"
    FROM
    ericsson_bulkcm."vsDataBestNeighborSI"

    """
)

BfdProfile = ReplaceableObject(
    'ericsson_cm_3g."BfdProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataBfdProfile_id",
        "detectionMultiplier",
        "desiredMinTxInterval",
        "requiredMinRxInterval",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataBfdProfile"

    """
)

BoundaryOrdinaryClock = ReplaceableObject(
    'ericsson_cm_3g."BoundaryOrdinaryClock"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataPtp_id",
        "vsDataBoundaryOrdinaryClock_id",
        "clockType",
        "domainNumber",
        "priority2",
        "priority1",
        "ptpProfile",
        "clockStatus",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataBoundaryOrdinaryClock"

    """
)

Bridge = ReplaceableObject(
    'ericsson_cm_3g."Bridge"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataBridge_id",
        "vsDataTransport_id",
        "operationalState",
        "mac_address",
        "port",
        "availabilityStatus",
        "macAddress",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataBridge"

    """
)

BrM = ReplaceableObject(
    'ericsson_cm_3g."BrM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "exportPackageLabelPrefix"
    FROM
    ericsson_bulkcm."vsDataBrM"

    """
)

BrmBackup = ReplaceableObject(
    'ericsson_cm_3g."BrmBackup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmBackup_id",
        "actionInProgress",
        "backupName",
        "creationTime",
        "progressReport",
        "status",
        "createdBy",
        "creatorJobId",
        "creationType",
        "swVersion_productName",
        "swVersion_productNumber",
        "swVersion_productRevision",
        "swVersion_productionDate",
        "swVersion_description",
        "swVersion_xossx_type",
        "progressReport_actionName",
        "progressReport_progressInfo",
        "progressReport_progressPercentage",
        "progressReport_xossx_result",
        "progressReport_resultInfo",
        "progressReport_state",
        "progressReport_actionId",
        "progressReport_timeActionStarted",
        "progressReport_timeActionCompleted",
        "progressReport_timeOfLastStatusUpdate"
    FROM
    ericsson_bulkcm."vsDataBrmBackup"

    """
)

BrmBackupHousekeeping = ReplaceableObject(
    'ericsson_cm_3g."BrmBackupHousekeeping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmBackupHousekeeping_id",
        "autoDelete",
        "maxStoredManualBackups"
    FROM
    ericsson_bulkcm."vsDataBrmBackupHousekeeping"

    """
)

BrmBackupLabelStore = ReplaceableObject(
    'ericsson_cm_3g."BrmBackupLabelStore"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmBackupLabelStore_id",
        "lastImportedBackup",
        "lastCreatedBackup",
        "lastExportedBackup",
        "restoreEscalationList",
        "lastRestoredBackup"
    FROM
    ericsson_bulkcm."vsDataBrmBackupLabelStore"

    """
)

BrmBackupManager = ReplaceableObject(
    'ericsson_cm_3g."BrmBackupManager"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "actionInProgress",
        "backupDomain",
        "backupType",
        "progressReport_actionName",
        "progressReport_progressInfo",
        "progressReport_progressPercentage",
        "progressReport_xossx_result",
        "progressReport_resultInfo",
        "progressReport_state",
        "progressReport_actionId",
        "progressReport_timeActionStarted",
        "progressReport_timeActionCompleted",
        "progressReport_timeOfLastStatusUpdate",
        "progressReport"
    FROM
    ericsson_bulkcm."vsDataBrmBackupManager"

    """
)

BrmBackupScheduler = ReplaceableObject(
    'ericsson_cm_3g."BrmBackupScheduler"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmBackupScheduler_id",
        "nextScheduledTime",
        "scheduledBackupName",
        "maxStoredScheduledBackups",
        "mostRecentlyCreatedAutoBackup",
        "progressReport_actionName",
        "progressReport_progressInfo",
        "progressReport_progressPercentage",
        "progressReport_xossx_result",
        "progressReport_resultInfo",
        "progressReport_state",
        "progressReport_actionId",
        "progressReport_timeActionStarted",
        "progressReport_timeActionCompleted",
        "progressReport_timeOfLastStatusUpdate",
        "adminState",
        "autoExportUri",
        "autoExport",
        "autoExportPassword",
        "progressReport"
    FROM
    ericsson_bulkcm."vsDataBrmBackupScheduler"

    """
)

BrmCalendarBasedPeriodicEvent = ReplaceableObject(
    'ericsson_cm_3g."BrmCalendarBasedPeriodicEvent"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmBackupScheduler_id",
        "vsDataBrmCalendarBasedPeriodicEvent_id",
        "startTime",
        "time",
        "dayOfWeekOccurrence",
        "dayOfMonth",
        "month",
        "dayOfWeek",
        "stopTime"
    FROM
    ericsson_bulkcm."vsDataBrmCalendarBasedPeriodicEvent"

    """
)

BrmFailsafeBackup = ReplaceableObject(
    'ericsson_cm_3g."BrmFailsafeBackup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmFailsafeBackup_id",
        "usageState",
        "backupName",
        "progressReport",
        "timeoutLength",
        "progressReport_actionName",
        "progressReport_progressInfo",
        "progressReport_progressPercentage",
        "progressReport_xossx_result",
        "progressReport_resultInfo",
        "progressReport_state",
        "progressReport_actionId",
        "progressReport_timeActionStarted",
        "progressReport_timeActionCompleted",
        "progressReport_timeOfLastStatusUpdate"
    FROM
    ericsson_bulkcm."vsDataBrmFailsafeBackup"

    """
)

BrmPeriodicEvent = ReplaceableObject(
    'ericsson_cm_3g."BrmPeriodicEvent"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmBackupScheduler_id",
        "vsDataBrmPeriodicEvent_id",
        "startTime",
        "minutes",
        "days",
        "hours",
        "weeks",
        "stopTime"
    FROM
    ericsson_bulkcm."vsDataBrmPeriodicEvent"

    """
)

BrmRollbackAtRestore = ReplaceableObject(
    'ericsson_cm_3g."BrmRollbackAtRestore"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmRollbackAtRestore_id",
        "timeRemainingBeforeRollback",
        "timeAllowedBeforeRollback"
    FROM
    ericsson_bulkcm."vsDataBrmRollbackAtRestore"

    """
)

BrmSingleEvent = ReplaceableObject(
    'ericsson_cm_3g."BrmSingleEvent"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataBrM_id",
        "vsDataBrmBackupManager_id",
        "vsDataBrmBackupScheduler_id",
        "vsDataBrmSingleEvent_id",
        "scheduledTime"
    FROM
    ericsson_bulkcm."vsDataBrmSingleEvent"

    """
)

Cabinet = ReplaceableObject(
    'ericsson_cm_3g."Cabinet"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataCabinet_id",
        "cabinetIdentifier",
        "productData_productionDate",
        "productData_productName",
        "productData_productNumber",
        "productData_productRevision",
        "productData_serialNumber",
        "climateSystem",
        "sharedCabinetIdentifier",
        "userLabel",
        "climateRegulationSystem",
        "productData"
    FROM
    ericsson_bulkcm."vsDataCabinet"

    """
)

CapacityChannelBandwidth = ReplaceableObject(
    'ericsson_cm_3g."CapacityChannelBandwidth"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityLicenses_id",
        "vsDataCapacityChannelBandwidth_id",
        "licenseCapacityChannelBandwidth",
        "capacityUnitChannelBandwidth",
        "keyIdChannelBandwidth",
        "licenseStateChannelBandwidth"
    FROM
    ericsson_bulkcm."vsDataCapacityChannelBandwidth"

    """
)

CapacityConnectedUsers = ReplaceableObject(
    'ericsson_cm_3g."CapacityConnectedUsers"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityLicenses_id",
        "vsDataCapacityConnectedUsers_id",
        "licenseCapacityConnectedUsers",
        "licenseStateConnectedUsers",
        "capacityUnitConnectedUsers",
        "keyIdConnectedUsers",
        "licConnectedUsersPercentileConf",
        "gracePeriodActive",
        "gracePeriodAvailable",
        "gracePeriodOriginalLicenseLimit",
        "gracePeriodTimeLeft"
    FROM
    ericsson_bulkcm."vsDataCapacityConnectedUsers"

    """
)

CapacityFeatureLicense = ReplaceableObject(
    'ericsson_cm_3g."CapacityFeatureLicense"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityFeatureLicense_id",
        "capacityType",
        "capacityUnit",
        "gracePeriod_startDate",
        "gracePeriod_originalLicenseLimit",
        "gracePeriod_isGracePeriodControlled",
        "gracePeriod_gracePeriodState",
        "gracePeriod_stopDate",
        "keyId",
        "licenseState",
        "currentCapacityLimit_noLimit",
        "currentCapacityLimit_value",
        "licensedCapacity_noLimit",
        "licensedCapacity_value"
    FROM
    ericsson_bulkcm."vsDataCapacityFeatureLicense"

    """
)

CapacityKey = ReplaceableObject(
    'ericsson_cm_3g."CapacityKey"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataCapacityKey_id",
        "shared",
        "licensedCapacityLimitReached",
        "grantedCapacityLevel",
        "expiration",
        "xossx_name",
        "validFrom",
        "licensedCapacityLimit_value",
        "licensedCapacityLimit_noLimit",
        "state",
        "keyId",
        "productType"
    FROM
    ericsson_bulkcm."vsDataCapacityKey"

    """
)

CapacityLicenses = ReplaceableObject(
    'ericsson_cm_3g."CapacityLicenses"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityLicenses_id"
    FROM
    ericsson_bulkcm."vsDataCapacityLicenses"

    """
)

CapacityState = ReplaceableObject(
    'ericsson_cm_3g."CapacityState"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataCapacityState_id",
        "licensedCapacityLimitReached",
        "grantedCapacityLevel",
        "capacityKey",
        "currentCapacityLimit_value",
        "currentCapacityLimit_noLimit",
        "description",
        "licenseState",
        "keyId",
        "serviceState",
        "featureState"
    FROM
    ericsson_bulkcm."vsDataCapacityState"

    """
)

Carrier = ReplaceableObject(
    'ericsson_cm_3g."Carrier"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataSector_id",
        "vsDataCarrier_id",
        "cqiErrors",
        "cqiErrorsAbsent",
        "cqiAdjustmentOn",
        "hsPowerMargin",
        "cellRange",
        "hsScchMinCodePower",
        "hsScchMaxCodePower",
        "queueSelectAlgorithm",
        "airRateTypeSelector",
        "qualityCheckPower",
        "frequencyPlane",
        "trDeviceRef",
        "dbccDeviceRef",
        "aiDeviceRef",
        "tpaDeviceRef",
        "schCongPeriodGbr",
        "schPrioForAbsResSharing",
        "schNoCongThreshGbr",
        "schCongThreshGbr",
        "schPowerDeltaCongGbr",
        "schNoCongPeriodGbr",
        "schCongThreshNonGbr",
        "schMinPowerNonGbrHsUsers",
        "schWeight",
        "schMaxDelay",
        "dpclDevicesRef",
        "numberOfTxBranches",
        "numberOfRxBranches",
        "ulBandwidth",
        "dlBandwidth",
        "ulFilterProfile",
        "dlFilterProfile",
        "hsdpaMcActivityBufferThreshold",
        "hsdpaMcInactivityTimer",
        "extraHsScchPowerForSrbOnHsdpa",
        "extraPowerForSrbOnHsdpa",
        "minBitRate",
        "minBitRateMinCqi",
        "defaultCqiHsFach",
        "extraCompForSigHsFach",
        "extraCompHsFach",
        "extraHsScchCompForSigHsFach",
        "extraHsScchCompHsFach",
        "throughputPqxHsFach",
        "extraCompEnhUeDrx",
        "extraHsScchCompEnhUeDrx",
        "chQualOffset",
        "maxDlPowerCapability",
        "minDlPowerCapability",
        "dlPowerOffsetCombinedCell",
        "eulLockedOptimalNoiseFloorEstimate",
        "eulMaxOwnUuLoad",
        "eulMaxRotCoverage",
        "eulOptimalNoiseFloorLock_eulNoiseFloorLock",
        "eulOptimalNoiseFloorLock_eulOptimalNoiseFloorEstimate",
        "eulSlidingWindowTime",
        "eulThermalLevelPrior",
        "fccRotMarginHigh",
        "fccRotMarginLow",
        "badBerFramesDtxHsOlpc",
        "badBerFramesHsOlpc",
        "numOfDtxHsOlpc",
        "periodDtxHsOlpc",
        "sirTargetStepHsOlpc",
        "downlinkBaseBandPoolRef",
        "txBranchesConfigured",
        "nbirFixedNotchPosition",
        "nbirAlgorithm"
    FROM
    ericsson_bulkcm."vsDataCarrier"

    """
)

CarrierAggregationFunction = ReplaceableObject(
    'ericsson_cm_3g."CarrierAggregationFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataCarrierAggregationFunction_id",
        "sCellActDeactDataThresHyst",
        "caUsageLimit",
        "caPreemptionThreshold",
        "sCellActDeactDataThres",
        "sCellScheduleSinrThres",
        "waitForCaOpportunity",
        "waitForBetterSCellRep",
        "waitForAdditionalSCellOpportunity",
        "caRateAdjustCoeff",
        "sCellActDeactUlDataThreshHyst",
        "sCellActDeactUlDataThresh",
        "sCellSelectionMode",
        "pdcchEnhancedLaForVolte",
        "sCellDeactOutOfCoverageTimer",
        "sCellDeactDelayTimer",
        "sCellActProhibitTimer",
        "sCellDeactProhibitTimer",
        "sCellActDeactProhibitTimer"
    FROM
    ericsson_bulkcm."vsDataCarrierAggregationFunction"

    """
)

CaxFanUnit = ReplaceableObject(
    'ericsson_cm_3g."CaxFanUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataCaxFanUnit_id",
        "administrativeState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataCaxFanUnit"

    """
)

Cbu = ReplaceableObject(
    'ericsson_cm_3g."Cbu"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataCbu_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataCbu"

    """
)

CchFrameSynch = ReplaceableObject(
    'ericsson_cm_3g."CchFrameSynch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCchFrameSynch_id",
        "dto",
        "doStep",
        "toAWS",
        "toAWE",
        "toAE",
        "reservedBy",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataCchFrameSynch"

    """
)

Cdma2000SessionContinuity = ReplaceableObject(
    'ericsson_cm_3g."Cdma2000SessionContinuity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataCdma2000SessionContinuity_id",
        "keyIdCdma2000SessionContinuity",
        "featureStateCdma2000SessionContinuity",
        "licenseStateCdma2000SessionContinuity",
        "serviceStateCdma2000SessionContinuity"
    FROM
    ericsson_bulkcm."vsDataCdma2000SessionContinuity"

    """
)

CellResources = ReplaceableObject(
    'ericsson_cm_3g."CellResources"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "vsDataCellResources_id",
        "numOfPcpich",
        "numOfPccpch",
        "availabilityStatus",
        "numOfPsch",
        "numOfScpich",
        "operationalState",
        "numOfSsch",
        "numOfBch"
    FROM
    ericsson_bulkcm."vsDataCellResources"

    """
)

CellSleepFunction = ReplaceableObject(
    'ericsson_cm_3g."CellSleepFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataCellSleepFunction_id",
        "covCellDlPrbWakeUpThreshold",
        "capCellDlPrbSleepThreshold",
        "sleepEndTime",
        "covCellRrcConnWakeUpThreshold",
        "sleepStartTime",
        "covCellWakeUpMonitorDurTimer",
        "capCellRrcConnSleepThreshold",
        "coverageCellDiscovery",
        "sleepState",
        "capCellSleepMonitorDurTimer",
        "sleepMode"
    FROM
    ericsson_bulkcm."vsDataCellSleepFunction"

    """
)

CellSleepNodeFunction = ReplaceableObject(
    'ericsson_cm_3g."CellSleepNodeFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataCellSleepNodeFunction_id",
        "csmEutranInterFMeasReportMax",
        "csmEutranInterFMeasReportDecr",
        "csmEutranInterFMeasReportIncr",
        "csmEutranInterFMeasReportMin"
    FROM
    ericsson_bulkcm."vsDataCellSleepNodeFunction"

    """
)

CertM = ReplaceableObject(
    'ericsson_cm_3g."CertM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "userLabel",
        "reportProgress_actionName",
        "reportProgress_progressInfo",
        "reportProgress_progressPercentage",
        "reportProgress_xossx_result",
        "reportProgress_resultInfo",
        "reportProgress_state",
        "reportProgress_actionId",
        "reportProgress_timeActionStarted",
        "reportProgress_timeActionCompleted",
        "reportProgress_timeOfLastStatusUpdate",
        "localFileStorePath"
    FROM
    ericsson_bulkcm."vsDataCertM"

    """
)

CertMCapabilities = ReplaceableObject(
    'ericsson_cm_3g."CertMCapabilities"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataCertMCapabilities_id"
    FROM
    ericsson_bulkcm."vsDataCertMCapabilities"

    """
)

ChannelSwitching = ReplaceableObject(
    'ericsson_cm_3g."ChannelSwitching"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataChannelSwitching_id",
        "dlRlcBufUpswitch",
        "ulRlcBufUpswitch",
        "downswitchThreshold",
        "downswitchTimerThreshold",
        "downswitchTimer",
        "dlRlcBufUpswitchMrab",
        "ulRlcBufUpswitchMrab",
        "upswitchTimer",
        "coverageTimer",
        "inactivityTimer",
        "downswitchPwrMargin",
        "upswitchPwrMargin",
        "downswitchTimerUp",
        "downswitchTimerSp",
        "hsdschInactivityTimer",
        "bandwidthMarginUl",
        "upswitchTimerUl",
        "bandwidthMargin",
        "dlDownswitchBandwidthMargin",
        "dlThroughputAllowUpswitchThreshold",
        "dlThroughputDownswitchTimer",
        "inactivityTimerPch",
        "ulThroughputAllowUpswitchThreshold",
        "ulThroughputDownswitchTimer",
        "ulDownswitchBandwidthMargin",
        "inactivityTimeMultiPsInteractive",
        "fachToHsDisabled",
        "hsdschInactivityTimerCpc",
        "dlRlcBufUpswitchHsFach",
        "inactivityTimerEnhUeDrx",
        "ulRlcBufUpswitchEulFach",
        "uraToDchEnabledDl"
    FROM
    ericsson_bulkcm."vsDataChannelSwitching"

    """
)

Climate = ReplaceableObject(
    'ericsson_cm_3g."Climate"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipmentSupportFunction_id",
        "vsDataClimate_id",
        "controlDomainRef",
        "climateControlMode",
        "availabilityStatus",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataClimate"

    """
)

CliSsh = ReplaceableObject(
    'ericsson_cm_3g."CliSsh"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataCliSsh_id",
        "administrativeState",
        "port"
    FROM
    ericsson_bulkcm."vsDataCliSsh"

    """
)

CliTls = ReplaceableObject(
    'ericsson_cm_3g."CliTls"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataCliTls_id",
        "administrativeState",
        "trustCategory",
        "nodeCredential",
        "port"
    FROM
    ericsson_bulkcm."vsDataCliTls"

    """
)

CnOperator = ReplaceableObject(
    'ericsson_cm_3g."CnOperator"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCnOperator_id",
        "userLabel",
        "plmnIdentity_mcc",
        "plmnIdentity_mnc",
        "plmnIdentity_mncLength",
        "iphoNetworkRefsUtran",
        "iphoNetworkRefsGsm",
        "equivalentPlmnIdentityGroupRef",
        "cnOperatorIndex",
        "iphoNetworkRefsEutran",
        "dchResourceShare",
        "u1LinkRef",
        "primarySharedCnOperatorRef"
    FROM
    ericsson_bulkcm."vsDataCnOperator"

    """
)

CombinedCell = ReplaceableObject(
    'ericsson_cm_3g."CombinedCell"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataCombinedCell_id",
        "featureStateCombinedCell",
        "keyIdCombinedCell",
        "licenseStateCombinedCell",
        "serviceStateCombinedCell"
    FROM
    ericsson_bulkcm."vsDataCombinedCell"

    """
)

CommonChannelResourcesDl = ReplaceableObject(
    'ericsson_cm_3g."CommonChannelResourcesDl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "vsDataCommonChannelResourcesDl_id",
        "availabilityStatus",
        "numOfSccpch",
        "operationalState",
        "numOfPich",
        "numOfPch",
        "numOfAich",
        "numOfFach"
    FROM
    ericsson_bulkcm."vsDataCommonChannelResourcesDl"

    """
)

CommonChannelResourcesUl = ReplaceableObject(
    'ericsson_cm_3g."CommonChannelResourcesUl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "vsDataNodeBSectorCarrier_id",
        "vsDataCommonChannelResourcesUl_id",
        "numOfPrach",
        "availabilityStatus",
        "numOfRach",
        "operationalState"
    FROM
    ericsson_bulkcm."vsDataCommonChannelResourcesUl"

    """
)

CommunicationContexts = ReplaceableObject(
    'ericsson_cm_3g."CommunicationContexts"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataCommunicationContexts_id",
        "noOfCommunicationContexts"
    FROM
    ericsson_bulkcm."vsDataCommunicationContexts"

    """
)

ConfigurationVersion = ReplaceableObject(
    'ericsson_cm_3g."ConfigurationVersion"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSwManagement_id",
        "vsDataConfigurationVersion_id",
        "currentUpgradePackage",
        "configAdmCountdown",
        "autoCreatedCVIsTurnedOn",
        "rollbackInitCounterValue",
        "rollbackInitTimerValue",
        "rollbackOn",
        "timeForAutoCreatedCV"
    FROM
    ericsson_bulkcm."vsDataConfigurationVersion"

    """
)

CoverageRelation = ReplaceableObject(
    'ericsson_cm_3g."CoverageRelation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCell_id",
        "vsDataCoverageRelation_id",
        "utranCellRef",
        "coverageIndicator",
        "hsPathlossThreshold",
        "relationCapability_hsCellSelection",
        "relationCapability_hsLoadSharing",
        "relationCapability_dchLoadSharing",
        "relationCapability_powerSave",
        "hsIflsDownswitch"
    FROM
    ericsson_bulkcm."vsDataCoverageRelation"

    """
)

CpriLinkSupervision = ReplaceableObject(
    'ericsson_cm_3g."CpriLinkSupervision"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "vsDataCpriLinkSupervision_id",
        "cpriLinkFilterTime"
    FROM
    ericsson_bulkcm."vsDataCpriLinkSupervision"

    """
)

CsfbForLimitedDualRadioUE = ReplaceableObject(
    'ericsson_cm_3g."CsfbForLimitedDualRadioUE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataCsfbForLimitedDualRadioUE_id",
        "keyIdCsfbForLimitedDualRadioUE",
        "featureStateCsfbForLimitedDualRadioUE",
        "licenseStateCsfbForLimitedDualRadioUE",
        "serviceStateCsfbForLimitedDualRadioUE"
    FROM
    ericsson_bulkcm."vsDataCsfbForLimitedDualRadioUE"

    """
)

CsfbToGeranUtran = ReplaceableObject(
    'ericsson_cm_3g."CsfbToGeranUtran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataCsfbToGeranUtran_id",
        "featureStateCsfbToGeranUtran",
        "keyIdCsfbToGeranUtran",
        "licenseStateCsfbToGeranUtran",
        "serviceStateCsfbToGeranUtran"
    FROM
    ericsson_bulkcm."vsDataCsfbToGeranUtran"

    """
)

DataCollectionGeneration = ReplaceableObject(
    'ericsson_cm_3g."DataCollectionGeneration"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataDataCollectionGeneration_id",
        "dcgState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataDataCollectionGeneration"

    """
)

DataRadioBearer = ReplaceableObject(
    'ericsson_cm_3g."DataRadioBearer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataRadioBearerTable_id",
        "vsDataDataRadioBearer_id",
        "tPollRetransmitDl",
        "dlMaxRetxThreshold",
        "ulMaxRetxThreshold",
        "tPollRetransmitUl"
    FROM
    ericsson_bulkcm."vsDataDataRadioBearer"

    """
)

DateAndTime = ReplaceableObject(
    'ericsson_cm_3g."DateAndTime"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataTimeM_id",
        "vsDataDateAndTime_id",
        "tzRevision",
        "dateTimeOffset",
        "timeZone",
        "localDateTime"
    FROM
    ericsson_bulkcm."vsDataDateAndTime"

    """
)

DBSAndSabe = ReplaceableObject(
    'ericsson_cm_3g."DBSAndSabe"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDBSAndSabe_id",
        "featureStateDBSAndSabe",
        "keyIdDBSAndSabe",
        "licenseStateDBSAndSabe",
        "serviceStateDBSAndSabe"
    FROM
    ericsson_bulkcm."vsDataDBSAndSabe"

    """
)

DchFrameSynch = ReplaceableObject(
    'ericsson_cm_3g."DchFrameSynch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataDchFrameSynch_id",
        "dto",
        "doStep",
        "toAWS",
        "toAWE",
        "toAE",
        "uto",
        "uoStep",
        "toAWEUl",
        "toAEUl",
        "userLabel",
        "toAWSUl"
    FROM
    ericsson_bulkcm."vsDataDchFrameSynch"

    """
)

DeviceGroup = ReplaceableObject(
    'ericsson_cm_3g."DeviceGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataDeviceGroup_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataPiuDevice_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id"
    FROM
    ericsson_bulkcm."vsDataDeviceGroup"

    """
)

Dhcp = ReplaceableObject(
    'ericsson_cm_3g."Dhcp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpOam_id",
        "vsDataDhcp_id",
        "userLabel",
        "dhcpServerAddresses"
    FROM
    ericsson_bulkcm."vsDataDhcp"

    """
)

DifferentiatedAdmissionControl = ReplaceableObject(
    'ericsson_cm_3g."DifferentiatedAdmissionControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDifferentiatedAdmissionControl_id",
        "featureStateDifferentiatedAdmissionControl",
        "keyIdDifferentiatedAdmissionControl",
        "licenseStateDifferentiatedAdmissionControl",
        "serviceStateDifferentiatedAdmissionControl"
    FROM
    ericsson_bulkcm."vsDataDifferentiatedAdmissionControl"

    """
)

DlBasebandCapacity = ReplaceableObject(
    'ericsson_cm_3g."DlBasebandCapacity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityLicenses_id",
        "vsDataDlBasebandCapacity_id",
        "licenseCapacityDlBbCapacity",
        "capacityUnitDlBbCapacity",
        "keyIdDlBbCapacity",
        "licDlBbPercentileConf",
        "licenseStateDlBbCapacity"
    FROM
    ericsson_bulkcm."vsDataDlBasebandCapacity"

    """
)

DlFss = ReplaceableObject(
    'ericsson_cm_3g."DlFss"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDlFss_id",
        "featureStateDlFss",
        "keyIdDlFss",
        "licenseStateDlFss",
        "serviceStateDlFss"
    FROM
    ericsson_bulkcm."vsDataDlFss"

    """
)

DlPrbCapacity = ReplaceableObject(
    'ericsson_cm_3g."DlPrbCapacity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityLicenses_id",
        "vsDataDlPrbCapacity_id",
        "capacityUnitDlPrbCapacity",
        "keyIdDlPrbCapacity",
        "licDlPrbPercentileConf",
        "licenseCapacityDlPrbCapacity",
        "licenseStateDlPrbCapacity"
    FROM
    ericsson_bulkcm."vsDataDlPrbCapacity"

    """
)

DnsClient = ReplaceableObject(
    'ericsson_cm_3g."DnsClient"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataRouter_id",
        "vsDataDnsClient_id",
        "vsDataHost_id",
        "serverAddress",
        "dscp",
        "localIpAddress",
        "reservedBy",
        "userLabel",
        "usedServerAddress",
        "configurationMode"
    FROM
    ericsson_bulkcm."vsDataDnsClient"

    """
)

DownlinkBaseBandPool = ReplaceableObject(
    'ericsson_cm_3g."DownlinkBaseBandPool"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataDownlinkBaseBandPool_id",
        "maxNumADchReservation",
        "numHsCodeResources"
    FROM
    ericsson_bulkcm."vsDataDownlinkBaseBandPool"

    """
)

Drx = ReplaceableObject(
    'ericsson_cm_3g."Drx"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDrx_id",
        "keyIdDrx",
        "featureStateDrx",
        "licenseStateDrx",
        "serviceStateDrx"
    FROM
    ericsson_bulkcm."vsDataDrx"

    """
)

DrxProfile = ReplaceableObject(
    'ericsson_cm_3g."DrxProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataDrxProfile_id",
        "drxInactivityTimer",
        "drxRetransmissionTimer",
        "longDrxCycle",
        "longDrxCycleOnly",
        "onDurationTimer",
        "shortDrxCycle",
        "shortDrxCycleTimer"
    FROM
    ericsson_bulkcm."vsDataDrxProfile"

    """
)

Dst = ReplaceableObject(
    'ericsson_cm_3g."Dst"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataRouter_id",
        "vsDataRouteTableIPv4Static_id",
        "vsDataDst_id",
        "vsDataHost_id",
        "dst"
    FROM
    ericsson_bulkcm."vsDataDst"

    """
)

DualAntDlPerfPkg = ReplaceableObject(
    'ericsson_cm_3g."DualAntDlPerfPkg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDualAntDlPerfPkg_id",
        "licenseStateDualAntDlPerfPkg",
        "keyIdDualAntDlPerfPkg",
        "featureStateDualAntDlPerfPkg",
        "serviceStateDualAntDlPerfPkg"
    FROM
    ericsson_bulkcm."vsDataDualAntDlPerfPkg"

    """
)

DualLayBeamfPerfPkg = ReplaceableObject(
    'ericsson_cm_3g."DualLayBeamfPerfPkg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDualLayBeamfPerfPkg_id",
        "featureStateDualLayBeamfPerfPkg",
        "keyIdDualLayBeamfPerfPkg",
        "licenseStateDualLayBeamfPerfPkg",
        "serviceStateDualLayBeamfPerfPkg"
    FROM
    ericsson_bulkcm."vsDataDualLayBeamfPerfPkg"

    """
)

DynamicGBRAdmCtrl = ReplaceableObject(
    'ericsson_cm_3g."DynamicGBRAdmCtrl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDynamicGBRAdmCtrl_id",
        "featureStateDynamicGBRAdmCtrl",
        "keyIdDynamicGBRAdmCtrl",
        "licenseStateDynamicGBRAdmCtrl",
        "serviceStateDynamicGBRAdmCtrl"
    FROM
    ericsson_bulkcm."vsDataDynamicGBRAdmCtrl"

    """
)

DynamicQoSModification = ReplaceableObject(
    'ericsson_cm_3g."DynamicQoSModification"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataDynamicQoSModification_id",
        "featureStateDynamicQoSModification",
        "keyIdDynamicQoSModification",
        "licenseStateDynamicQoSModification",
        "serviceStateDynamicQoSModification"
    FROM
    ericsson_bulkcm."vsDataDynamicQoSModification"

    """
)

E1PhysPathTerm = ReplaceableObject(
    'ericsson_cm_3g."E1PhysPathTerm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminal_id",
        "vsDataE1PhysPathTerm_id",
        "administrativeState",
        "userLabel",
        "lineNo",
        "loopback",
        "crc4Mode",
        "idlePattern",
        "degDegThr",
        "degDegM",
        "rdiReporting",
        "aisReporting",
        "shutDownTimeout"
    FROM
    ericsson_bulkcm."vsDataE1PhysPathTerm"

    """
)

EcBus = ReplaceableObject(
    'ericsson_cm_3g."EcBus"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataEcBus_id",
        "connectionType",
        "ecBusConnectorRef"
    FROM
    ericsson_bulkcm."vsDataEcBus"

    """
)

EcPort = ReplaceableObject(
    'ericsson_cm_3g."EcPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataFieldReplaceableUnit_id",
        "vsDataEcPort_id",
        "hubPosition",
        "cascadingOrder",
        "ecBusRef"
    FROM
    ericsson_bulkcm."vsDataEcPort"

    """
)

EcsCsfb = ReplaceableObject(
    'ericsson_cm_3g."EcsCsfb"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataEcsCsfb_id",
        "featureStateEcsCsfb",
        "keyIdEcsCsfb",
        "licenseStateEcsCsfb",
        "serviceStateEcsCsfb"
    FROM
    ericsson_bulkcm."vsDataEcsCsfb"

    """
)

EDchResources = ReplaceableObject(
    'ericsson_cm_3g."EDchResources"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "vsDataNodeBSectorCarrier_id",
        "vsDataEDchResources_id",
        "availabilityStatus",
        "operationalState"
    FROM
    ericsson_bulkcm."vsDataEDchResources"

    """
)

EmergencyUnlock = ReplaceableObject(
    'ericsson_cm_3g."EmergencyUnlock"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataEmergencyUnlock_id",
        "activationsLeft",
        "expiration",
        "activationState"
    FROM
    ericsson_bulkcm."vsDataEmergencyUnlock"

    """
)

EnergyMeter = ReplaceableObject(
    'ericsson_cm_3g."EnergyMeter"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataHwUnit_id",
        "vsDataEnergyMeter_id"
    FROM
    ericsson_bulkcm."vsDataEnergyMeter"

    """
)

EnhCellIdInTraces = ReplaceableObject(
    'ericsson_cm_3g."EnhCellIdInTraces"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataEnhCellIdInTraces_id",
        "featureStateEnhCellIdInTraces",
        "keyIdEnhCellIdInTraces",
        "licenseStateEnhCellIdInTraces",
        "serviceStateEnhCellIdInTraces"
    FROM
    ericsson_bulkcm."vsDataEnhCellIdInTraces"

    """
)

ENodeBFunction = ReplaceableObject(
    'ericsson_cm_3g."ENodeBFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "userLabel",
        "sctpRef",
        "dnsLookupTimer",
        "dscpLabel",
        "nodePCIProfileID",
        "dnsLookupOnTai",
        "eNBId",
        "eNodeBPlmnId_mcc",
        "eNodeBPlmnId_mnc",
        "eNodeBPlmnId_mncLength",
        "s1RetryTimer",
        "x2BlackList",
        "x2retryTimerMaxAuto",
        "x2retryTimerStart",
        "x2WhiteList",
        "ulSchedulerDynamicBWAllocationEnabled",
        "timeAndPhaseSynchCritical",
        "nnsfMode",
        "x2IpAddrViaS1Active",
        "rrcConnReestActive",
        "zzzTemporary1",
        "zzzTemporary2",
        "zzzTemporary3",
        "zzzTemporary4",
        "zzzTemporary5",
        "zzzTemporary6",
        "zzzTemporary7",
        "zzzTemporary8",
        "zzzTemporary9",
        "zzzTemporary10",
        "zzzTemporary11",
        "zzzTemporary12",
        "timePhaseMaxDeviation",
        "x2SetupTwoWayRelations",
        "licCapDistrMethod",
        "s1HODirDataPathAvail",
        "maxRandc",
        "minRandc",
        "randUpdateInterval",
        "zzzTemporary13",
        "zzzTemporary15",
        "zzzTemporary16",
        "zzzTemporary17",
        "upIpAddressRef",
        "mfbiSupport",
        "plmnBorderNode",
        "pwsPersistentStorage",
        "csfbMeasFromIdleMode",
        "forcedSiTunnelingActive",
        "zzzTemporary21",
        "zzzTemporary22",
        "zzzTemporary25",
        "zzzTemporary26",
        "zzzTemporary23",
        "zzzTemporary24",
        "zzzTemporary18",
        "initPreschedulingEnable",
        "tOutgoingHoExecCdma1xRtt",
        "biasThpWifiMobility",
        "releaseInactiveUesMpLoadLevel",
        "dnsSelectionS1X2Ref",
        "tS1HoCancelTimer",
        "combCellSectorSelectThreshRx",
        "combCellSectorSelectThreshTx",
        "releaseInactiveUesInactTime",
        "timePhaseMaxDeviationMbms",
        "timePhaseMaxDeviationOtdoa",
        "timePhaseMaxDeviationTdd",
        "timePhaseMaxDeviationSib16",
        "timeAndPhaseSynchAlignment",
        "timePhaseMaxDeviationCdma2000",
        "licUlBbPercentileConf",
        "licUlPrbPercentileConf",
        "licDlPrbPercentileConf",
        "mtRreWithoutNeighborActive",
        "licDlBbPercentileConf",
        "licConnectedUsersPercentileConf",
        "ulMaxWaitingTimeGlobal",
        "softLockRwRWaitTimerInternal",
        "enabledUlTrigMeas",
        "dlMaxWaitingTimeGlobal",
        "tddVoipDrxProfileId",
        "zzzTemporary29",
        "mfbiSupportPolicy",
        "zzzTemporary28",
        "measuringEcgiWithAgActive",
        "checkEmergencySoftLock",
        "softLockRwRWaitTimerOperator",
        "zzzTemporary30",
        "zzzTemporary31",
        "zzzTemporary32",
        "zzzTemporary33",
        "zzzTemporary34",
        "tRelocOverall",
        "alignTtiBundWUlTrigSinr",
        "bbVlanPortRef",
        "useBandPrioritiesInSCellEval",
        "prioritizeAdditionalBands",
        "caAwareMfbiIntraCellHo",
        "zzzTemporary40",
        "zzzTemporary38",
        "zzzTemporary39",
        "zzzTemporary35",
        "zzzTemporary36",
        "zzzTemporary37",
        "gtpuErrorIndicationDscp",
        "s1GtpuEchoFailureAction",
        "s1GtpuEchoEnable",
        "x2GtpuEchoDscp",
        "x2GtpuEchoEnable",
        "s1GtpuEchoDscp",
        "stnNodes",
        "tcuNodes",
        "release",
        "x2BlackList_mcc",
        "x2BlackList_mnc",
        "x2BlackList_mncLength",
        "x2BlackList_enbId",
        "x2WhiteList_mcc",
        "x2WhiteList_mnc",
        "x2WhiteList_mncLength",
        "x2WhiteList_enbId",
        "zzzTemporary14",
        "zzzTemporary20",
        "zzzTemporary27",
        "zzzTemporary19",
        "tRelocOverallValue",
        "releaseInactiveUesEnable",
        "csfbForDualRadioUE",
        "ipAddress",
        "thpWifiMobilityStatus"
    FROM
    ericsson_bulkcm."vsDataENodeBFunction"

    """
)

EnrollmentAuthority = ReplaceableObject(
    'ericsson_cm_3g."EnrollmentAuthority"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataEnrollmentAuthority_id",
        "enrollmentCaCertificate",
        "enrollmentCaFingerprint",
        "userLabel",
        "enrollmentAuthorityName"
    FROM
    ericsson_bulkcm."vsDataEnrollmentAuthority"

    """
)

EnrollmentServer = ReplaceableObject(
    'ericsson_cm_3g."EnrollmentServer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataEnrollmentServerGroup_id",
        "vsDataEnrollmentServer_id",
        "userLabel",
        "uri",
        "protocol"
    FROM
    ericsson_bulkcm."vsDataEnrollmentServer"

    """
)

EnrollmentServerGroup = ReplaceableObject(
    'ericsson_cm_3g."EnrollmentServerGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataEnrollmentServerGroup_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataEnrollmentServerGroup"

    """
)

Equipment = ReplaceableObject(
    'ericsson_cm_3g."Equipment"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSTN_id",
        "userLabel",
        "serialNumber",
        "productRevision",
        "productNumber",
        "manufacturingDate",
        "productName"
    FROM
    ericsson_bulkcm."vsDataEquipment"

    """
)

EquipmentClockReference = ReplaceableObject(
    'ericsson_cm_3g."EquipmentClockReference"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataRadioEquipmentClock_id",
        "vsDataEquipmentClockReference_id",
        "referenceStatus",
        "priority",
        "lockOut",
        "encapsulation"
    FROM
    ericsson_bulkcm."vsDataEquipmentClockReference"

    """
)

EquipmentDiscovery = ReplaceableObject(
    'ericsson_cm_3g."EquipmentDiscovery"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "vsDataEquipmentDiscovery_id",
        "antennaDeviceScanStatus"
    FROM
    ericsson_bulkcm."vsDataEquipmentDiscovery"

    """
)

EquipmentSupportFunction = ReplaceableObject(
    'ericsson_cm_3g."EquipmentSupportFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipmentSupportFunction_id",
        "supportSystemControl",
        "supportFunction",
        "release",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataEquipmentSupportFunction"

    """
)

EricssonFilter = ReplaceableObject(
    'ericsson_cm_3g."EricssonFilter"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataLdapAuthenticationMethod_id",
        "vsDataLdap_id",
        "vsDataEricssonFilter_id",
        "roleAliasesBaseDn",
        "targetBasedAccessControl",
        "version"
    FROM
    ericsson_bulkcm."vsDataEricssonFilter"

    """
)

EthernetBridgePort = ReplaceableObject(
    'ericsson_cm_3g."EthernetBridgePort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataEthernetSwitchModule_id",
        "vsDataEthernetBridgePort_id",
        "egressUntagVlanRef",
        "externalPort",
        "pbitQueueMap_queue",
        "pbitQueueMap_pbit",
        "physicalPortRef",
        "untaggedIngressPriority",
        "untaggedIngressVlanRef",
        "userLabel",
        "vlanRef"
    FROM
    ericsson_bulkcm."vsDataEthernetBridgePort"

    """
)

EthernetInterface = ReplaceableObject(
    'ericsson_cm_3g."EthernetInterface"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataEthernetInterface_id",
        "operationalState",
        "mac_address",
        "port",
        "mode",
        "currentMode",
        "sendLinkAlarmAllowed",
        "depTrafficManager",
        "portNumber",
        "flowControl",
        "ethMaxFrameSize",
        "ptpInterfaceGroup",
        "currentState"
    FROM
    ericsson_bulkcm."vsDataEthernetInterface"

    """
)

EthernetLink = ReplaceableObject(
    'ericsson_cm_3g."EthernetLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpOam_id",
        "vsDataIp_id",
        "vsDataEthernetLink_id",
        "macAddress",
        "mtuSize",
        "metric",
        "interfaceName",
        "userLabel",
        "ipv4Addresses_broadcastAddress",
        "ipv4Addresses_ipAddress",
        "ipv4Addresses_prefixLength",
        "ipv6Addresses",
        "ipAddress",
        "subnetMask",
        "broadcastAddress",
        "ipv4Addresses",
        "prefixLength"
    FROM
    ericsson_bulkcm."vsDataEthernetLink"

    """
)

EthernetPort = ReplaceableObject(
    'ericsson_cm_3g."EthernetPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "mtu",
        "availabilityStatus",
        "holdDownTimer",
        "autoNegEnable",
        "operationalState",
        "macAddress",
        "reservedBy",
        "operOperatingMode",
        "userLabel",
        "administrativeState",
        "admOperatingMode",
        "encapsulation",
        "egressQosClassification",
        "egressQosMarking",
        "egressQosQueueMap",
        "ingressQosMarking",
        "portNo",
        "ingressPolicing",
        "ingressPolicingBurst",
        "ingressPolicingRate",
        "masterMode",
        "operatingMode_autoNegotiation",
        "operatingMode_configuredSpeedDuplex",
        "shutDownTimeout",
        "trafficState"
    FROM
    ericsson_bulkcm."vsDataEthernetPort"

    """
)

EthernetSwitch = ReplaceableObject(
    'ericsson_cm_3g."EthernetSwitch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataEthernetSwitch_id",
        "pbitQueueMap_queue",
        "pbitQueueMap_pbit",
        "untaggedIngressPriority",
        "untaggedIngressVid",
        "vlanMembership_egressUntag",
        "vlanMembership_vid",
        "enableVlan",
        "userLabel",
        "macAddress",
        "linkAggLinkSelection"
    FROM
    ericsson_bulkcm."vsDataEthernetSwitch"

    """
)

EthernetSwitchFabric = ReplaceableObject(
    'ericsson_cm_3g."EthernetSwitchFabric"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEthernetSwitchFabric_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataEthernetSwitchFabric"

    """
)

EthernetSwitchingAdm = ReplaceableObject(
    'ericsson_cm_3g."EthernetSwitchingAdm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEthernetSwitchingAdm_id",
        "featureStateLinkAgg",
        "licenseStateLinkAgg",
        "userLabel",
        "featureStateL2gp",
        "l2gpPathCost",
        "l2gpRapidFailover",
        "licenseStateL2gp"
    FROM
    ericsson_bulkcm."vsDataEthernetSwitchingAdm"

    """
)

EthernetSwitchModule = ReplaceableObject(
    'ericsson_cm_3g."EthernetSwitchModule"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataEthernetSwitchModule_id",
        "userLabel",
        "macAddress",
        "linkAggLinkSelection"
    FROM
    ericsson_bulkcm."vsDataEthernetSwitchModule"

    """
)

EthernetSwitchModulePort = ReplaceableObject(
    'ericsson_cm_3g."EthernetSwitchModulePort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataEthernetSwitchModule_id",
        "vsDataEthernetSwitchModulePort_id",
        "portNo",
        "untaggedIngressPriority",
        "administrativeState",
        "pbitQueueMap_queue",
        "pbitQueueMap_pbit",
        "operatingMode_autoNegotiation",
        "operatingMode_configuredSpeedDuplex",
        "externalPort",
        "egressUntagVlanRef",
        "vlanRef",
        "untaggedIngressVlanRef",
        "userLabel",
        "lagRef",
        "trafficState",
        "remoteFaultIndication"
    FROM
    ericsson_bulkcm."vsDataEthernetSwitchModulePort"

    """
)

EthernetSwitchPort = ReplaceableObject(
    'ericsson_cm_3g."EthernetSwitchPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataEthernetSwitch_id",
        "vsDataEthernetSwitchPort_id",
        "portNo",
        "untaggedIngressPriority",
        "untaggedIngressVid",
        "vlanMembership_egressUntag",
        "vlanMembership_vid",
        "ingressPeakBitrate",
        "actualSpeedDuplex",
        "sfpInformation_sfpProductNumber",
        "sfpInformation_sfpType",
        "sfpInformation_sfpState",
        "sfpPort",
        "systemPort",
        "administrativeState",
        "userLabel",
        "pbitQueueMap_queue",
        "pbitQueueMap_pbit",
        "operatingMode_autoNegotiation",
        "operatingMode_configuredSpeedDuplex",
        "lagRef",
        "trafficState"
    FROM
    ericsson_bulkcm."vsDataEthernetSwitchPort"

    """
)

Etws = ReplaceableObject(
    'ericsson_cm_3g."Etws"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataEtws_id"
    FROM
    ericsson_bulkcm."vsDataEtws"

    """
)

Eul = ReplaceableObject(
    'ericsson_cm_3g."Eul"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCell_id",
        "vsDataHsdsch_id",
        "vsDataEul_id",
        "userLabel",
        "administrativeState",
        "numEagchCodes",
        "numEhichErgchCodes",
        "eulMaxTargetRtwp",
        "edchTti2Support",
        "eulDchBalancingEnabled",
        "eulDchBalancingLoad",
        "eulDchBalancingOverload",
        "eulDchBalancingReportPeriod",
        "eulDchBalancingSupport",
        "eulDchBalancingSuspendDownSw",
        "eulDchBalancingTimerNg",
        "releaseAseUlNg",
        "eulLoadTriggeredSoftCong",
        "eulTdSchedulingSupport",
        "improvedL2Support",
        "pathlossThresholdEulTti2",
        "threshEulTti2Ecno"
    FROM
    ericsson_bulkcm."vsDataEul"

    """
)

EUtranCellRelation = ReplaceableObject(
    'ericsson_cm_3g."EUtranCellRelation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataEUtranFreqRelation_id",
        "vsDataEUtranCellRelation_id",
        "cellIndividualOffsetEUtran",
        "isRemoveAllowed",
        "isHoAllowed",
        "qOffsetCellEUtran",
        "adjacentCell",
        "includeInSystemInformation",
        "coverageIndicator",
        "lastModification",
        "createdBy",
        "timeOfCreation",
        "timeOfLastModification",
        "loadBalancing",
        "sCellCandidate",
        "lbBnrAllowed",
        "incomingLoadBalancing",
        "lbCovIndicated",
        "sleepModeCovCellCandidate",
        "sleepModeCoverageCell",
        "sleepModeCapacityCell",
        "hoSuccLevel",
        "crsAssistanceInfoPriority",
        "amoAllowed",
        "amoState",
        "mobilityStatus_available",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataEUtranCellRelation"

    """
)

EUtraNetwork = ReplaceableObject(
    'ericsson_cm_3g."EUtraNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataEutraNetwork_id",
        "userLabel",
        "plmnIdentity_mcc",
        "plmnIdentity_mnc",
        "plmnIdentity_mncLength",
        "reservedBy",
        "aliasPlmnIdentities",
        "aliasPlmnIdentities_mcc",
        "aliasPlmnIdentities_mnc",
        "aliasPlmnIdentities_mncLength"
    FROM
    ericsson_bulkcm."vsDataEUtraNetwork"

    """
)

EUtranFreqRelation = ReplaceableObject(
    'ericsson_cm_3g."EUtranFreqRelation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataEUtranFreqRelation_id",
        "eutranFreqToQciProfileRelation",
        "blackListEntryIdleMode",
        "cellReselectionPriority",
        "pMax",
        "qRxLevMin",
        "tReselectionEutra",
        "tReselectionEutraSfHigh",
        "tReselectionEutraSfMedium",
        "userLabel",
        "allowedMeasBandwidth",
        "presenceAntennaPort1",
        "qOffsetFreq",
        "threshXHigh",
        "threshXLow",
        "allowedPlmnList_mcc",
        "allowedPlmnList_mnc",
        "allowedPlmnList_mncLength",
        "adjacentFreq",
        "connectedModeMobilityPrio",
        "createdBy",
        "lastModification",
        "mobilityAction",
        "timeOfCreation",
        "timeOfLastModification",
        "qQualMin",
        "threshXHighQ",
        "threshXLowQ",
        "neighCellConfig",
        "voicePrio",
        "blackListEntry",
        "interFreqMeasType",
        "lbBnrPolicy",
        "lbActivationThreshold",
        "anrMeasOn",
        "caTriggeredRedirectionActive",
        "arpPrio",
        "nonPlannedPhysCellIdRange",
        "nonPlannedPciTargetIdType",
        "nonPlannedPhysCellId",
        "nonPlannedPciCIO",
        "a5Thr1RsrqFreqOffset",
        "a5Thr1RsrpFreqOffset",
        "a5Thr2RsrpFreqOffset",
        "a5Thr2RsrqFreqOffset",
        "candNeighborRel",
        "atoAllowed",
        "cellSleepCovCellMeasOn",
        "hybridCsgPhysCellId",
        "hybridCsgPhysCellIdRange",
        "csgPhysCellId",
        "interFreqMeasTypeUlSinr",
        "csgPhysCellIdRange",
        "csgCellTargetIdType",
        "amoAllowed",
        "allowedPlmnList",
        "blackListEntry_physicalLayerCellIdGroup",
        "blackListEntry_physicalLayerSubCellId",
        "blackListEntry_range",
        "candNeighborRel_physicalLayerSubCellId",
        "candNeighborRel_physicalLayerCellIdGroup",
        "candNeighborRel_cellId",
        "candNeighborRel_enbId",
        "candNeighborRel_mcc",
        "candNeighborRel_mnc",
        "candNeighborRel_mncLength",
        "candNeighborRel_tac",
        "candNeighborRel_mobilityStatusReason",
        "eutranFreqToQciProfileRelation_lbA4ThresholdRsrpOffset",
        "eutranFreqToQciProfileRelation_lbQciProfileHandling",
        "eutranFreqToQciProfileRelation_qciProfileRef",
        "blackListEntryIdleMode_physicalLayerCellIdGroup",
        "blackListEntryIdleMode_physicalLayerSubCellId",
        "blackListEntryIdleMode_range"
    FROM
    ericsson_bulkcm."vsDataEUtranFreqRelation"

    """
)

EUtranFrequency = ReplaceableObject(
    'ericsson_cm_3g."EUtranFrequency"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataFreqManagement_id",
        "vsDataEUtranFrequency_id",
        "arfcnValueEUtranDl",
        "userLabel",
        "excludeAdditionalFreqBandList"
    FROM
    ericsson_bulkcm."vsDataEUtranFrequency"

    """
)

EventCapabilities = ReplaceableObject(
    'ericsson_cm_3g."EventCapabilities"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPmEventM_id",
        "vsDataEventProducer_id",
        "vsDataEventCapabilities_id",
        "maxNoOfJobs"
    FROM
    ericsson_bulkcm."vsDataEventCapabilities"

    """
)

EventProducer = ReplaceableObject(
    'ericsson_cm_3g."EventProducer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPmEventM_id",
        "vsDataEventProducer_id"
    FROM
    ericsson_bulkcm."vsDataEventProducer"

    """
)

ExchangeTerminal = ReplaceableObject(
    'ericsson_cm_3g."ExchangeTerminal"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminal_id",
        "vsDataCbu_id",
        "description_aal2LayerDescription",
        "description_atmLayerDescription",
        "description_etType",
        "description_physicalLayerDescription",
        "description_tdmSupport",
        "userLabel",
        "shuttingDownTimer"
    FROM
    ericsson_bulkcm."vsDataExchangeTerminal"

    """
)

ExchangeTerminalIp = ReplaceableObject(
    'ericsson_cm_3g."ExchangeTerminalIp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataPiuDevice_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataExchangeTerminalIp"

    """
)

ExternalENodeBFunction = ReplaceableObject(
    'ericsson_cm_3g."ExternalENodeBFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataExternalEUtranPlmn_id",
        "vsDataExternalENodeBFunction_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtraNetwork_id",
        "mfbiSupport",
        "eNodeBPlmnId_mcc",
        "eNodeBPlmnId_mnc",
        "eNodeBPlmnId_mncLength",
        "eNBId",
        "userLabel",
        "masterEnbFunctionId",
        "lastModification",
        "createdBy",
        "timeOfCreation",
        "timeOfLastModification",
        "ulTrigHoSupport"
    FROM
    ericsson_bulkcm."vsDataExternalENodeBFunction"

    """
)

ExternalEUtranCellFDD = ReplaceableObject(
    'ericsson_cm_3g."ExternalEUtranCellFDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataExternalEUtranPlmn_id",
        "vsDataExternalENodeBFunction_id",
        "vsDataExternalEUtranCellFDD_id",
        "localCellId",
        "physicalLayerCellIdGroup",
        "physicalLayerSubCellId",
        "userLabel",
        "tac",
        "activePlmnList_mcc",
        "activePlmnList_mnc",
        "activePlmnList_mncLength",
        "pciConflict",
        "pciConflictCell_enbId",
        "pciConflictCell_cellId",
        "pciConflictCell_mcc",
        "pciConflictCell_mnc",
        "pciConflictCell_mncLength",
        "pciDetectingCell_enbId",
        "pciDetectingCell_cellId",
        "pciDetectingCell_mcc",
        "pciDetectingCell_mnc",
        "pciDetectingCell_mncLength",
        "earfcndl",
        "lbEUtranCellOffloadCapacity",
        "pciConflictCell",
        "pciDetectingCell",
        "activePlmnList"
    FROM
    ericsson_bulkcm."vsDataExternalEUtranCellFDD"

    """
)

ExternalEutranFrequency = ReplaceableObject(
    'ericsson_cm_3g."ExternalEutranFrequency"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataFreqManagement_id",
        "vsDataExternalEutranFrequency_id",
        "userLabel",
        "earfcnDl",
        "plmnIdentity_mcc",
        "plmnIdentity_mnc",
        "plmnIdentity_mncLength"
    FROM
    ericsson_bulkcm."vsDataExternalEutranFrequency"

    """
)

ExternalEUtranPlmn = ReplaceableObject(
    'ericsson_cm_3g."ExternalEUtranPlmn"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataExternalEUtranPlmn_id",
        "plmnIdentity_mcc",
        "plmnIdentity_mnc",
        "plmnIdentity_mncLength",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataExternalEUtranPlmn"

    """
)

ExternalGsmFreq = ReplaceableObject(
    'ericsson_cm_3g."ExternalGsmFreq"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataFreqManagement_id",
        "vsDataExternalGsmFreq_id",
        "userLabel",
        "arfcnValueGeranDl",
        "bandIndicator",
        "externalGsmFreqGroupId"
    FROM
    ericsson_bulkcm."vsDataExternalGsmFreq"

    """
)

ExternalGsmFreqGroup = ReplaceableObject(
    'ericsson_cm_3g."ExternalGsmFreqGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataFreqManagement_id",
        "vsDataExternalGsmFreqGroup_id",
        "userLabel",
        "reservedBy",
        "frequencyGroupId"
    FROM
    ericsson_bulkcm."vsDataExternalGsmFreqGroup"

    """
)

ExternalGsmPlmn = ReplaceableObject(
    'ericsson_cm_3g."ExternalGsmPlmn"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataExternalGsmPlmn_id",
        "userLabel",
        "mcc",
        "mnc",
        "mncLength",
        "aliasPlmnIdentities"
    FROM
    ericsson_bulkcm."vsDataExternalGsmPlmn"

    """
)

ExternalNode = ReplaceableObject(
    'ericsson_cm_3g."ExternalNode"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataExternalNode_id",
        "logicalName",
        "fullDistinguishedName",
        "informationOnly",
        "radioAccessTechnology",
        "supportSystemControl"
    FROM
    ericsson_bulkcm."vsDataExternalNode"

    """
)

ExternalUtranFreq = ReplaceableObject(
    'ericsson_cm_3g."ExternalUtranFreq"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataFreqManagement_id",
        "vsDataExternalUtranFreq_id",
        "userLabel",
        "arfcnValueUtranDl"
    FROM
    ericsson_bulkcm."vsDataExternalUtranFreq"

    """
)

ExternalUtranPlmn = ReplaceableObject(
    'ericsson_cm_3g."ExternalUtranPlmn"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataExternalUtranPlmn_id",
        "userLabel",
        "mcc",
        "mnc",
        "mncLength",
        "aliasPlmnIdentities"
    FROM
    ericsson_bulkcm."vsDataExternalUtranPlmn"

    """
)

Fach = ReplaceableObject(
    'ericsson_cm_3g."Fach"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCell_id",
        "vsDataFach_id",
        "userLabel",
        "maxFach1Power",
        "maxFach2Power",
        "sccpchOffset",
        "pOffset1Fach",
        "pOffset3Fach",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataFach"

    """
)

FanGroup = ReplaceableObject(
    'ericsson_cm_3g."FanGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataCabinet_id",
        "vsDataFanGroup_id"
    FROM
    ericsson_bulkcm."vsDataFanGroup"

    """
)

FeatureKey = ReplaceableObject(
    'ericsson_cm_3g."FeatureKey"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataFeatureKey_id",
        "shared",
        "expiration",
        "xossx_name",
        "validFrom",
        "state",
        "keyId",
        "productType"
    FROM
    ericsson_bulkcm."vsDataFeatureKey"

    """
)

FeatureState = ReplaceableObject(
    'ericsson_cm_3g."FeatureState"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataFeatureState_id",
        "featureKey",
        "description",
        "licenseState",
        "serviceState",
        "keyId",
        "featureState"
    FROM
    ericsson_bulkcm."vsDataFeatureState"

    """
)

FieldReplaceableUnit = ReplaceableObject(
    'ericsson_cm_3g."FieldReplaceableUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataFieldReplaceableUnit_id",
        "hwTestResult_timeStamp",
        "hwTestResult_hwTestStatus",
        "administrativeState",
        "operationalState",
        "productData_productionDate",
        "productData_productName",
        "productData_productNumber",
        "productData_productRevision",
        "productData_serialNumber",
        "userLabel",
        "positionRef",
        "supportUnitRef",
        "positionInformation",
        "positionCoordinates",
        "hwTestResult",
        "productData",
        "positionCoordinates_altitude",
        "positionCoordinates_geoDatum",
        "positionCoordinates_latitude",
        "positionCoordinates_longitude"
    FROM
    ericsson_bulkcm."vsDataFieldReplaceableUnit"

    """
)

FilePullCapabilities = ReplaceableObject(
    'ericsson_cm_3g."FilePullCapabilities"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPmEventM_id",
        "vsDataEventProducer_id",
        "vsDataFilePullCapabilities_id",
        "supportedCompressionTypes",
        "finalROP",
        "alignedReportingPeriod",
        "outputDirectory",
        "supportedReportingPeriods"
    FROM
    ericsson_bulkcm."vsDataFilePullCapabilities"

    """
)

FileTPM = ReplaceableObject(
    'ericsson_cm_3g."FileTPM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataFileTPM_id"
    FROM
    ericsson_bulkcm."vsDataFileTPM"

    """
)

Filter = ReplaceableObject(
    'ericsson_cm_3g."Filter"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataLdapAuthenticationMethod_id",
        "vsDataLdap_id",
        "vsDataFilter_id",
        "xossx_type",
        "userLabel",
        "filter"
    FROM
    ericsson_bulkcm."vsDataFilter"

    """
)

Fm = ReplaceableObject(
    'ericsson_cm_3g."Fm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataFm_id",
        "lastSequenceNo",
        "sumCritical",
        "sumMajor",
        "sumMinor",
        "sumWarning",
        "totalActive",
        "lastChanged",
        "heartbeatInterval"
    FROM
    ericsson_bulkcm."vsDataFm"

    """
)

FmAlarmModel = ReplaceableObject(
    'ericsson_cm_3g."FmAlarmModel"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataFm_id",
        "vsDataFmAlarmModel_id"
    FROM
    ericsson_bulkcm."vsDataFmAlarmModel"

    """
)

FmAlarmType = ReplaceableObject(
    'ericsson_cm_3g."FmAlarmType"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataFm_id",
        "vsDataFmAlarmModel_id",
        "vsDataFmAlarmType_id",
        "majorType",
        "minorType",
        "specificProblem",
        "eventType",
        "probableCause",
        "isStateful",
        "additionalText",
        "configuredSeverity"
    FROM
    ericsson_bulkcm."vsDataFmAlarmType"

    """
)

FmSubscription = ReplaceableObject(
    'ericsson_cm_3g."FmSubscription"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataFmSubscription_id",
        "managerIpAddress",
        "destPortNumber",
        "adminState",
        "heartbeatInterval"
    FROM
    ericsson_bulkcm."vsDataFmSubscription"

    """
)

FreqManagement = ReplaceableObject(
    'ericsson_cm_3g."FreqManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataFreqManagement_id"
    FROM
    ericsson_bulkcm."vsDataFreqManagement"

    """
)

FrequencySyncIO = ReplaceableObject(
    'ericsson_cm_3g."FrequencySyncIO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataFrequencySyncIO_id",
        "availabilityStatus",
        "operationalState",
        "reservedBy",
        "encapsulation"
    FROM
    ericsson_bulkcm."vsDataFrequencySyncIO"

    """
)

FtpTls = ReplaceableObject(
    'ericsson_cm_3g."FtpTls"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataFileTPM_id",
        "vsDataFtpTls_id",
        "trustCategory",
        "nodeCredential"
    FROM
    ericsson_bulkcm."vsDataFtpTls"

    """
)

FtpTlsServer = ReplaceableObject(
    'ericsson_cm_3g."FtpTlsServer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataFileTPM_id",
        "vsDataFtpTls_id",
        "vsDataFtpTlsServer_id",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataFtpTlsServer"

    """
)

GeneralProcessorUnit = ReplaceableObject(
    'ericsson_cm_3g."GeneralProcessorUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataGeneralProcessorUnit_id",
        "vsDataCbu_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataGeneralProcessorUnit"

    """
)

GeranCellRelation = ReplaceableObject(
    'ericsson_cm_3g."GeranCellRelation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataGeranFreqGroupRelation_id",
        "vsDataGeranCellRelation_id",
        "createdBy",
        "timeOfCreation",
        "adjacentCell",
        "coverageIndicator",
        "isRemoveAllowed",
        "lastModification",
        "timeOfLastModification",
        "isHoAllowed",
        "extGeranCellRef"
    FROM
    ericsson_bulkcm."vsDataGeranCellRelation"

    """
)

GeraNetwork = ReplaceableObject(
    'ericsson_cm_3g."GeraNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataGeraNetwork_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataGeraNetwork"

    """
)

GeranFreqGroupRelation = ReplaceableObject(
    'ericsson_cm_3g."GeranFreqGroupRelation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataGeranFreqGroupRelation_id",
        "cellReselectionPriority",
        "nccPermitted",
        "pMaxGeran",
        "qRxLevMin",
        "threshXHigh",
        "threshXLow",
        "userLabel",
        "adjacentFreqGroup",
        "allowedPlmnList",
        "connectedModeMobilityPrio",
        "csFallbackPrio",
        "qOffsetFreq",
        "csFallbackPrioEC",
        "mobilityAction",
        "mobilityActionCsfb",
        "anrMeasOn",
        "voicePrio",
        "altCsfbTargetPrio",
        "altCsfbTargetPrioEc",
        "b2Thr1RsrqGeranFreqOffset",
        "b2Thr2GeranFreqOffset",
        "qciB2ThrOffsets",
        "b2Thr1RsrpGeranFreqOffset",
        "allowedPlmnList_mcc",
        "allowedPlmnList_mnc",
        "allowedPlmnList_mncLength"
    FROM
    ericsson_bulkcm."vsDataGeranFreqGroupRelation"

    """
)

GigaBitEthernet = ReplaceableObject(
    'ericsson_cm_3g."GigaBitEthernet"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataGigaBitEthernet_id",
        "vsDataPiuDevice_id",
        "macAddressLink1",
        "userLabel",
        "administrativeState",
        "dscpPbitMap_dscp",
        "dscpPbitMap_pbit",
        "frameFormat",
        "autoNegotiation",
        "shutDownTimeout",
        "statePropagationDelay",
        "portNo",
        "sfpInformation_sfpProductNumber",
        "sfpInformation_sfpType",
        "sfpInformation_sfpState",
        "sfpPort",
        "configuredSpeedDuplex",
        "masterMode",
        "configPbitArp",
        "macAddressLink2",
        "primaryLink",
        "protectiveMode",
        "switchBackTimer",
        "linkType",
        "defRoutersLinkSwitch"
    FROM
    ericsson_bulkcm."vsDataGigaBitEthernet"

    """
)

GnssInfo = ReplaceableObject(
    'ericsson_cm_3g."GnssInfo"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataTimeSyncIO_id",
        "vsDataGnssInfo_id"
    FROM
    ericsson_bulkcm."vsDataGnssInfo"

    """
)

Gpeh = ReplaceableObject(
    'ericsson_cm_3g."Gpeh"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataGpeh_id"
    FROM
    ericsson_bulkcm."vsDataGpeh"

    """
)

GpsOutSyncLink = ReplaceableObject(
    'ericsson_cm_3g."GpsOutSyncLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataTimingUnit_id",
        "vsDataGpsOutSyncLink_id",
        "administrativeState",
        "gpsCompensationDelay",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataGpsOutSyncLink"

    """
)

GpsSyncRef = ReplaceableObject(
    'ericsson_cm_3g."GpsSyncRef"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataTimingUnit_id",
        "vsDataGpsSyncRef_id",
        "administrativeState",
        "gpsCompensationDelay",
        "observationPoint",
        "userLabel",
        "latitude",
        "longitude",
        "altitude",
        "filterTimeGpsAlarm"
    FROM
    ericsson_bulkcm."vsDataGpsSyncRef"

    """
)

GracePeriod = ReplaceableObject(
    'ericsson_cm_3g."GracePeriod"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataCapacityState_id",
        "vsDataGracePeriod_id",
        "gracePeriodExpiration",
        "gracePeriodState"
    FROM
    ericsson_bulkcm."vsDataGracePeriod"

    """
)

GsmSessionContinuity = ReplaceableObject(
    'ericsson_cm_3g."GsmSessionContinuity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataGsmSessionContinuity_id",
        "keyIdGsmSessionContinuity",
        "featureStateGsmSessionContinuity",
        "licenseStateGsmSessionContinuity",
        "serviceStateGsmSessionContinuity"
    FROM
    ericsson_bulkcm."vsDataGsmSessionContinuity"

    """
)

GtpPath = ReplaceableObject(
    'ericsson_cm_3g."GtpPath"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataTermPointToSGW_id",
        "vsDataGtpPath_id"
    FROM
    ericsson_bulkcm."vsDataGtpPath"

    """
)

Handover = ReplaceableObject(
    'ericsson_cm_3g."Handover"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataHandover_id",
        "maxActiveSet",
        "fddGsmHOSupp",
        "selHoSup",
        "timeReleaseIuPs",
        "gsmAmountPropRepeat",
        "gsmPropRepeatInterval",
        "ifhoPropRepeatInterval",
        "ifhoAmountPropRepeat",
        "fddIfhoSupp",
        "releaseConnOffset",
        "maxGsmMonSubset",
        "maxIefMonSubset",
        "cnhhoSupp",
        "interFreqCnhhoPenaltyEcno",
        "interFreqCnhhoPenaltyRscp",
        "intraFreqCnhhoPenalty",
        "intraFreqCnhhoWeight",
        "tmStopGsmMeas",
        "lbhoMinSpeechUsers",
        "lbhoMaxTriggeredUsers",
        "lbhoMinTriggerTime",
        "ifLbhoMode",
        "iflsHyst",
        "cmSrbHsEnabled",
        "dchIflsFachTrigg",
        "hsIflsFirstUserTrigg",
        "hsIflsPrio_mc",
        "hsIflsPrio_dbMc",
        "hsIflsPrio_mimo",
        "hsIflsPrio_qam64",
        "hsIflsPrio_cpc",
        "hsIflsPrio_eul",
        "hsIflsPrio_eulMc",
        "hsIflsPrio_hsdpa3Mc",
        "hsIflsPrio_hsdpaDb3Mc",
        "blockRwrEutraTime",
        "timeRelocSecondCn",
        "blockEcRelRwrEutraTime",
        "blockEcRelEutra_rwrEutra",
        "eulMcSohoSupp",
        "rejCsfbPshoSrbOnDch"
    FROM
    ericsson_bulkcm."vsDataHandover"

    """
)

HighSpeedUE = ReplaceableObject(
    'ericsson_cm_3g."HighSpeedUE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataHighSpeedUE_id",
        "featureStateHighSpeedUE",
        "keyIdHighSpeedUE",
        "licenseStateHighSpeedUE",
        "serviceStateHighSpeedUE"
    FROM
    ericsson_bulkcm."vsDataHighSpeedUE"

    """
)

HoOscCtrlUE = ReplaceableObject(
    'ericsson_cm_3g."HoOscCtrlUE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataHoOscCtrlUE_id",
        "featureStateHoOscCtrlUE",
        "keyIdHoOscCtrlUE",
        "licenseStateHoOscCtrlUE",
        "serviceStateHoOscCtrlUE"
    FROM
    ericsson_bulkcm."vsDataHoOscCtrlUE"

    """
)

Host = ReplaceableObject(
    'ericsson_cm_3g."Host"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataHost_id",
        "userLabel",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataHost"

    """
)

HoWhiteList = ReplaceableObject(
    'ericsson_cm_3g."HoWhiteList"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataSubscriberProfileID_id",
        "vsDataHoWhiteList_id",
        "spidList",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataHoWhiteList"

    """
)

Hsdsch = ReplaceableObject(
    'ericsson_cm_3g."Hsdsch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCell_id",
        "vsDataHsdsch_id",
        "administrativeState",
        "userLabel",
        "numHsPdschCodes",
        "deltaAck1",
        "deltaNack1",
        "deltaAck2",
        "deltaNack2",
        "deltaCqi1",
        "deltaCqi2",
        "initialCqiRepetitionFactor",
        "initialAckNackRepetitionFactor",
        "cqiFeedbackCycle",
        "hsMeasurementPowerOffset",
        "codeThresholdPdu656",
        "numHsScchCodes",
        "enhancedL2Support",
        "qam64Support",
        "qam64MimoSupport",
        "hsFachSupport",
        "enhUeDrxSupport",
        "hsAqmCongCtrlSpiSupport",
        "hsAqmCongCtrlSupport"
    FROM
    ericsson_bulkcm."vsDataHsdsch"

    """
)

HsDschResources = ReplaceableObject(
    'ericsson_cm_3g."HsDschResources"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "vsDataHsDschResources_id",
        "availabilityStatus",
        "operationalState"
    FROM
    ericsson_bulkcm."vsDataHsDschResources"

    """
)

HttpM = ReplaceableObject(
    'ericsson_cm_3g."HttpM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataHttpM_id"
    FROM
    ericsson_bulkcm."vsDataHttpM"

    """
)

Https = ReplaceableObject(
    'ericsson_cm_3g."Https"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataHttpM_id",
        "vsDataHttps_id",
        "trustCategory",
        "nodeCredential"
    FROM
    ericsson_bulkcm."vsDataHttps"

    """
)

HwInventory = ReplaceableObject(
    'ericsson_cm_3g."HwInventory"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataHwInventory_id",
        "timeOfLatestInvChange"
    FROM
    ericsson_bulkcm."vsDataHwInventory"

    """
)

HwItem = ReplaceableObject(
    'ericsson_cm_3g."HwItem"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataHwInventory_id",
        "vsDataHwItem_id",
        "licMgmtMoRef",
        "vendorName",
        "swInvMoRef",
        "manualDataEntry",
        "serialNumber",
        "hwType",
        "hwModel",
        "hwUnitLocation",
        "hwCapability",
        "equipmentMoRef",
        "additionalInformation",
        "dateOfLastService",
        "hwName",
        "productData_productName",
        "productData_productNumber",
        "productData_productRevision",
        "productData_productionDate",
        "productData_description",
        "productData_xossx_type"
    FROM
    ericsson_bulkcm."vsDataHwItem"

    """
)

HwUnit = ReplaceableObject(
    'ericsson_cm_3g."HwUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataHwUnit_id",
        "position",
        "availabilityStatus",
        "unitType",
        "administrativeState",
        "operationalState",
        "productData_productionDate",
        "productData_productName",
        "productData_productNumber",
        "productData_productRevision",
        "productData_serialNumber",
        "positionInformation",
        "positionRef",
        "userLabel",
        "piuType",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataHwUnit"

    """
)

ImaGroup = ReplaceableObject(
    'ericsson_cm_3g."ImaGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataImaGroup_id",
        "userLabel",
        "physicalPortList",
        "requiredNumberOfLinks"
    FROM
    ericsson_bulkcm."vsDataImaGroup"

    """
)

ImaLink = ReplaceableObject(
    'ericsson_cm_3g."ImaLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataImaGroup_id",
        "vsDataImaLink_id",
        "userLabel",
        "uses"
    FROM
    ericsson_bulkcm."vsDataImaLink"

    """
)

ImeisvTable = ReplaceableObject(
    'ericsson_cm_3g."ImeisvTable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataImeisvTable_id",
        "listOfFeaturesDefaultOff",
        "listOfFeaturesDefaultOn"
    FROM
    ericsson_bulkcm."vsDataImeisvTable"

    """
)

IntegrationUnlock = ReplaceableObject(
    'ericsson_cm_3g."IntegrationUnlock"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataIntegrationUnlock_id",
        "activationsLeft",
        "expiration",
        "activationState"
    FROM
    ericsson_bulkcm."vsDataIntegrationUnlock"

    """
)

InterfaceIPv4 = ReplaceableObject(
    'ericsson_cm_3g."InterfaceIPv4"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataInterfaceIpv4_id",
        "mtu",
        "dscpPbitMap_dscp",
        "dscpPbitMap_pbit",
        "bfdProfileRef",
        "ethernetRef",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataInterfaceIPv4"

    """
)

InterFrequencyLoadBalancing = ReplaceableObject(
    'ericsson_cm_3g."InterFrequencyLoadBalancing"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataInterFrequencyLoadBalancing_id",
        "featureStateInterFrequencyLoadBalancing",
        "keyIdInterFrequencyLoadBalancing",
        "licenseStateInterFrequencyLoadBalancing",
        "serviceStateInterFrequencyLoadBalancing"
    FROM
    ericsson_bulkcm."vsDataInterFrequencyLoadBalancing"

    """
)

InterFrequencyLTEHandover = ReplaceableObject(
    'ericsson_cm_3g."InterFrequencyLTEHandover"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataInterFrequencyLTEHandover_id",
        "featureStateInterFrequencyLTEHandover",
        "keyIdInterFrequencyLTEHandover",
        "licenseStateInterFrequencyLTEHandover",
        "serviceStateInterFrequencyLTEHandover"
    FROM
    ericsson_bulkcm."vsDataInterFrequencyLTEHandover"

    """
)

InterFrequencySessionContinuity = ReplaceableObject(
    'ericsson_cm_3g."InterFrequencySessionContinuity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataInterFrequencySessionContinuity_id",
        "keyIdInterFrequencySessionContinuity",
        "featureStateInterFrequencySessionContinuity",
        "licenseStateInterFrequencySessionContinuity",
        "serviceStateInterFrequencySessionContinuity"
    FROM
    ericsson_bulkcm."vsDataInterFrequencySessionContinuity"

    """
)

InternalEthernetPort = ReplaceableObject(
    'ericsson_cm_3g."InternalEthernetPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataInternalEthernetPort_id",
        "dscpPbitMap_dscp",
        "dscpPbitMap_pbit",
        "ethernetSwitchRef",
        "frameFormat",
        "userLabel",
        "macAddress",
        "configPbitArp"
    FROM
    ericsson_bulkcm."vsDataInternalEthernetPort"

    """
)

IntraLTEHODataFwd = ReplaceableObject(
    'ericsson_cm_3g."IntraLTEHODataFwd"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataIntraLTEHODataFwd_id",
        "licenseStateIntraLTEHODataFwd",
        "keyIdIntraLTEHODataFwd",
        "featureStateIntraLTEHODataFwd",
        "serviceStateIntraLTEHODataFwd"
    FROM
    ericsson_bulkcm."vsDataIntraLTEHODataFwd"

    """
)

Ip = ReplaceableObject(
    'ericsson_cm_3g."Ip"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpOam_id",
        "vsDataIp_id",
        "isRecursiveSearch",
        "isSubDomainName",
        "userLabel",
        "retransInterval",
        "noOfRetrans",
        "isDefDomainName",
        "defDomainName",
        "useHostFile",
        "dscp",
        "icmpRedirect",
        "udpChecksumState",
        "workingMode",
        "dnsServerAddresses",
        "nodeInterfaceName",
        "nodeIpAddress",
        "ipAccessHostEtRef",
        "nodeIpv6Address",
        "nodeIpv6InterfaceName",
        "usedDnsServerAddresses",
        "dnsAutoConfigInterfaceRef",
        "connectionAttemptTimer",
        "maxRetransmissionAttempts"
    FROM
    ericsson_bulkcm."vsDataIp"

    """
)

IpAccessHostEt = ReplaceableObject(
    'ericsson_cm_3g."IpAccessHostEt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpAccessHostEt_id",
        "administrativeState",
        "ipAddress",
        "ipDefaultTtl",
        "ipInterfaceMoRef",
        "userLabel",
        "ntpDscp",
        "networkPrefixLength",
        "ntpServerMode"
    FROM
    ericsson_bulkcm."vsDataIpAccessHostEt"

    """
)

IpAccessHostGpb = ReplaceableObject(
    'ericsson_cm_3g."IpAccessHostGpb"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpAccessHostGpb_id",
        "userLabel",
        "administrativeState",
        "generalProcessorUnitId",
        "autoConfig",
        "autoConfigIdentity",
        "autoConfigIdentity2",
        "ipAddress1",
        "ipAddress2",
        "ipDefaultTtl",
        "interface1",
        "interface2",
        "reassemblyTimeout",
        "reservedByMos",
        "dnsClient2Ref",
        "dnsClient1Ref",
        "networkPrefixLength2",
        "networkPrefixLength1"
    FROM
    ericsson_bulkcm."vsDataIpAccessHostGpb"

    """
)

IpAccessHostPool = ReplaceableObject(
    'ericsson_cm_3g."IpAccessHostPool"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpAccessHostPool_id",
        "administrativeState",
        "ipAccessHostRef",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIpAccessHostPool"

    """
)

IpAccessHostSpb = ReplaceableObject(
    'ericsson_cm_3g."IpAccessHostSpb"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpAccessHostSpb_id",
        "userLabel",
        "administrativeState",
        "autoConfig",
        "autoConfigIdentity",
        "spmId",
        "ipAddress",
        "ipDefaultTtl",
        "autoConfigIdentity2",
        "interface2",
        "ipAddress2",
        "ipInterface",
        "reassemblyTimeout"
    FROM
    ericsson_bulkcm."vsDataIpAccessHostSpb"

    """
)

IpAccessSctp = ReplaceableObject(
    'ericsson_cm_3g."IpAccessSctp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpAccessSctp_id",
        "userLabel",
        "ipAccessHostEtRef1",
        "ipAccessHostEtRef2"
    FROM
    ericsson_bulkcm."vsDataIpAccessSctp"

    """
)

IpAtmLink = ReplaceableObject(
    'ericsson_cm_3g."IpAtmLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpOam_id",
        "vsDataIp_id",
        "vsDataIpAtmLink_id",
        "interfaceName",
        "ipAddress",
        "metric",
        "monitor",
        "monitorInterval",
        "monitorRetries",
        "mtuSize",
        "subnetMask",
        "userLabel",
        "aal5TpVccTpId"
    FROM
    ericsson_bulkcm."vsDataIpAtmLink"

    """
)

IpEthPacketDataRouter = ReplaceableObject(
    'ericsson_cm_3g."IpEthPacketDataRouter"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSpDevicePool_id",
        "vsDataPdrDevice_id",
        "vsDataIpEthPacketDataRouter_id",
        "userLabel",
        "administrativeState",
        "ipAccessHostSpbRef",
        "ipAddressSelection"
    FROM
    ericsson_bulkcm."vsDataIpEthPacketDataRouter"

    """
)

IpFlowMonitor = ReplaceableObject(
    'ericsson_cm_3g."IpFlowMonitor"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataGigaBitEthernet_id",
        "vsDataIpInterface_id",
        "vsDataIpFlowMonitor_id",
        "remoteIpAddress",
        "dscpValue",
        "samplingInterval",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIpFlowMonitor"

    """
)

IpHostLink = ReplaceableObject(
    'ericsson_cm_3g."IpHostLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpOam_id",
        "vsDataIp_id",
        "vsDataIpHostLink_id",
        "ipInterfaceMoRef",
        "userLabel",
        "interfaceName",
        "ipv4Addresses",
        "ipv6Addresses",
        "ipAddress"
    FROM
    ericsson_bulkcm."vsDataIpHostLink"

    """
)

IpInterface = ReplaceableObject(
    'ericsson_cm_3g."IpInterface"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataGigaBitEthernet_id",
        "vsDataIpInterface_id",
        "vsDataPiuDevice_id",
        "vsDataInternalEthernetPort_id",
        "logging",
        "userLabel",
        "vid",
        "vLan",
        "rps",
        "mtu",
        "networkPrefixLength",
        "defaultRouter0",
        "defaultRouter1",
        "defaultRouter2",
        "defaultRouterPingInterval",
        "maxWaitForPingReply",
        "maxNoOfFailedPings",
        "noOfPingsBeforeOk",
        "switchBackTimer",
        "ownIpAddressActive",
        "subnet",
        "trafficType",
        "accessControlListRef",
        "trafficSchedulerRef",
        "configurationMode",
        "dhcpClientIdentifier_clientIdentifier",
        "dhcpClientIdentifier_clientIdentifierType",
        "ownIpAddressPassive",
        "vlanRef"
    FROM
    ericsson_bulkcm."vsDataIpInterface"

    """
)

IpLicensing = ReplaceableObject(
    'ericsson_cm_3g."IpLicensing"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpLicensing_id",
        "featureStateIpFlowMonitoring",
        "userLabel",
        "licenseStateIpFlowMonitoring",
        "featureStateEthernetOamService",
        "licenseStateEthernetOamService"
    FROM
    ericsson_bulkcm."vsDataIpLicensing"

    """
)

IpOam = ReplaceableObject(
    'ericsson_cm_3g."IpOam"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpOam_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIpOam"

    """
)

Ippm = ReplaceableObject(
    'ericsson_cm_3g."Ippm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIppm_id",
        "userLabel",
        "featureStateTwampResponder",
        "licenseStateTwampResponder",
        "responderFeatureState",
        "responderLicenseState"
    FROM
    ericsson_bulkcm."vsDataIppm"

    """
)

IpRoute = ReplaceableObject(
    'ericsson_cm_3g."IpRoute"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataRoutingTable_id",
        "vsDataIpRoute_id",
        "active",
        "destIpSubnet",
        "nextHopIpAddress",
        "forwardingInterface",
        "routeType",
        "admDistance",
        "disableConnectivityCheck",
        "tagValue"
    FROM
    ericsson_bulkcm."vsDataIpRoute"

    """
)

IpRouter = ReplaceableObject(
    'ericsson_cm_3g."IpRouter"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "configPbitArp",
        "piuRef",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIpRouter"

    """
)

IpRouteSys = ReplaceableObject(
    'ericsson_cm_3g."IpRouteSys"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataRoutingTable_id",
        "vsDataIpRouteSys_id",
        "active",
        "destIpSubnet",
        "nextHopIpAddress",
        "forwardingInterface",
        "routeType",
        "admDistance"
    FROM
    ericsson_bulkcm."vsDataIpRouteSys"

    """
)

IpRoutingTable = ReplaceableObject(
    'ericsson_cm_3g."IpRoutingTable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpOam_id",
        "vsDataIp_id",
        "vsDataIpRoutingTable_id",
        "userLabel",
        "staticRoutes_indexOfStaticRoute",
        "staticRoutes_ipAddress",
        "staticRoutes_networkMask",
        "staticRoutes_nextHopIpAddr",
        "staticRoutes_redistribute",
        "staticRoutes_routeMetric"
    FROM
    ericsson_bulkcm."vsDataIpRoutingTable"

    """
)

IpSec = ReplaceableObject(
    'ericsson_cm_3g."IpSec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpSec_id",
        "certEnrollErrorMsg",
        "certEnrollState",
        "certExpirWarnTime",
        "certificate_issuer",
        "certificate_notValidAfter",
        "certificate_notValidBefore",
        "certificate_serialNumber",
        "certificate_subject",
        "certificate_fingerprint",
        "certificate_subjectAltName",
        "featureState",
        "installedTrustedCertificates",
        "licenseState",
        "trustedCertInstallErrorMsg",
        "trustedCertInstallState",
        "userLabel",
        "autoUpdateCertEnrollmentServer"
    FROM
    ericsson_bulkcm."vsDataIpSec"

    """
)

IpSyncRef = ReplaceableObject(
    'ericsson_cm_3g."IpSyncRef"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpAccessHostEt_id",
        "vsDataIpSyncRef_id",
        "cachedIpAddress",
        "ntpServerIpAddress",
        "userLabel",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataIpSyncRef"

    """
)

IpSystem = ReplaceableObject(
    'ericsson_cm_3g."IpSystem"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIpSystem"

    """
)

Ipv4DestNetwork = ReplaceableObject(
    'ericsson_cm_3g."Ipv4DestNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataIpv4StaticRouteTable_id",
        "vsDataIpv4DestNetwork_id",
        "userLabel",
        "ipv4Prefix"
    FROM
    ericsson_bulkcm."vsDataIpv4DestNetwork"

    """
)

Ipv4Peer = ReplaceableObject(
    'ericsson_cm_3g."Ipv4Peer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataIpv4Peer_id",
        "bfd",
        "userLabel",
        "ipAddress"
    FROM
    ericsson_bulkcm."vsDataIpv4Peer"

    """
)

Ipv4StaticRoute = ReplaceableObject(
    'ericsson_cm_3g."Ipv4StaticRoute"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataIpv4StaticRouteTable_id",
        "vsDataIpv4DestNetwork_id",
        "vsDataIpv4StaticRoute_id",
        "administrativeState",
        "ipv4StaticRouteNextHop",
        "metric",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIpv4StaticRoute"

    """
)

Ipv4StaticRouteTable = ReplaceableObject(
    'ericsson_cm_3g."Ipv4StaticRouteTable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataIpv4StaticRouteTable_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIpv4StaticRouteTable"

    """
)

IPv6RoutingTable = ReplaceableObject(
    'ericsson_cm_3g."IPv6RoutingTable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataIPv6RoutingTable_id"
    FROM
    ericsson_bulkcm."vsDataIPv6RoutingTable"

    """
)

Irc = ReplaceableObject(
    'ericsson_cm_3g."Irc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataIrc_id",
        "keyIdIrc",
        "featureStateIrc",
        "licenseStateIrc",
        "serviceStateIrc"
    FROM
    ericsson_bulkcm."vsDataIrc"

    """
)

Iub = ReplaceableObject(
    'ericsson_cm_3g."Iub"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataIub_id",
        "rbsId",
        "userLabel",
        "controlPlaneTransportOption_atm",
        "controlPlaneTransportOption_ipV4",
        "userPlaneTransportOption_atm",
        "userPlaneTransportOption_ipV4",
        "userPlaneIpResourceRef",
        "ipv4Address"
    FROM
    ericsson_bulkcm."vsDataIub"

    """
)

IubDataStreams = ReplaceableObject(
    'ericsson_cm_3g."IubDataStreams"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataIub_id",
        "vsDataIubDataStreams_id",
        "maxHsRate",
        "hsDataFrameDelayThreshold",
        "schHsFlowControlOnOff",
        "hsRbrWeight",
        "hsAqmCongCtrlSpiOnOff",
        "hsRbrDiscardProbability",
        "noOfCommonStreams",
        "userLabel",
        "noOfDedicatedStreams"
    FROM
    ericsson_bulkcm."vsDataIubDataStreams"

    """
)

IubEdch = ReplaceableObject(
    'ericsson_cm_3g."IubEdch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "IubLink_id",
        "vsDataIubEdch_id",
        "edchDataFrameDelayThreshold",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataIubEdch"

    """
)

IuLink = ReplaceableObject(
    'ericsson_cm_3g."IuLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCnOperator_id",
        "vsDataIuLink_id",
        "packetDataRouterRef",
        "userPlaneTransportOption_atm",
        "userPlaneTransportOption_ipv4",
        "userPlaneIpResourceRef",
        "userLabel",
        "atmUserPlaneTermSubrackRef",
        "spare",
        "spareA"
    FROM
    ericsson_bulkcm."vsDataIuLink"

    """
)

IurLink = ReplaceableObject(
    'ericsson_cm_3g."IurLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIurLink_id",
        "userLabel",
        "rncId",
        "utranNetworkRef",
        "cellCapabilityControl_hsdschSupport",
        "cellCapabilityControl_edchSupport",
        "cellCapabilityControl_edchTti2Support",
        "cellCapabilityControl_enhancedL2Support",
        "cellCapabilityControl_fdpchSupport",
        "cellCapabilityControl_multiCarrierSupport",
        "cellCapabilityControl_cpcSupport",
        "cellCapabilityControl_qam64MimoSupport",
        "hspaPathlossThreshold",
        "userPlaneTransportOption_atm",
        "userPlaneTransportOption_ipv4",
        "srncPmReporting",
        "userPlaneIpResourceRef",
        "edchDataFrameDelayThreshold",
        "iurArpGuaranteed",
        "iurArpNonguaranteed",
        "atmUserPlaneTermSubrackRef",
        "maxMacdPduSizeExtended",
        "ganHoEnabled",
        "spare",
        "cmDoubleFramesSupported",
        "releaseRedirect",
        "releaseRedirectEutraTriggers_csFallbackCsRelease",
        "releaseRedirectEutraTriggers_csFallbackDchToFach",
        "releaseRedirectEutraTriggers_dchToFach",
        "releaseRedirectEutraTriggers_fachToUra",
        "releaseRedirectEutraTriggers_fastDormancy",
        "releaseRedirectEutraTriggers_normalRelease",
        "spareA",
        "redirectUarfcn",
        "retainRlIurFailure",
        "eutraNeighborReportSrnc",
        "callReestablishmentEnabled",
        "delay",
        "dlCodePowerCmEnabled",
        "rwrEutraCc",
        "ifIratHoPsIntHsEnabled",
        "nwInitCallReestEnabled",
        "altIntraDrncHsccProcedure"
    FROM
    ericsson_bulkcm."vsDataIurLink"

    """
)

KeyFileInformation = ReplaceableObject(
    'ericsson_cm_3g."KeyFileInformation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataKeyFileManagement_id",
        "vsDataKeyFileInformation_id",
        "locatable",
        "installationTime",
        "sequenceNumber",
        "productType"
    FROM
    ericsson_bulkcm."vsDataKeyFileInformation"

    """
)

KeyFileManagement = ReplaceableObject(
    'ericsson_cm_3g."KeyFileManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "vsDataKeyFileManagement_id",
        "reportProgress_actionName",
        "reportProgress_progressInfo",
        "reportProgress_progressPercentage",
        "reportProgress_xossx_result",
        "reportProgress_resultInfo",
        "reportProgress_state",
        "reportProgress_actionId",
        "reportProgress_timeActionStarted",
        "reportProgress_timeActionCompleted",
        "reportProgress_timeOfLastStatusUpdate"
    FROM
    ericsson_bulkcm."vsDataKeyFileManagement"

    """
)

Lag = ReplaceableObject(
    'ericsson_cm_3g."Lag"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataEthernetSwitchModule_id",
        "vsDataLag_id",
        "aggregatedPortSpeed",
        "lacpMode",
        "masterPort",
        "userLabel",
        "requiredNumberOfLinks",
        "ethernetPortRef",
        "linkSelection",
        "linkSelectionMethod"
    FROM
    ericsson_bulkcm."vsDataLag"

    """
)

Ldap = ReplaceableObject(
    'ericsson_cm_3g."Ldap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataLdapAuthenticationMethod_id",
        "vsDataLdap_id",
        "bindDn",
        "baseDn",
        "bindPassword_cleartext",
        "bindPassword_password",
        "profileFilter",
        "ldapIpAddress",
        "tlsMode",
        "userLabel",
        "serverPort",
        "fallbackLdapIpAddress",
        "trustCategory",
        "useReferrals",
        "useTls",
        "nodeCredential"
    FROM
    ericsson_bulkcm."vsDataLdap"

    """
)

LdapAuthenticationMethod = ReplaceableObject(
    'ericsson_cm_3g."LdapAuthenticationMethod"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataLdapAuthenticationMethod_id",
        "administrativeState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataLdapAuthenticationMethod"

    """
)

Licensing = ReplaceableObject(
    'ericsson_cm_3g."Licensing"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "fingerprint"
    FROM
    ericsson_bulkcm."vsDataLicensing"

    """
)

LinkTransmissionProfile = ReplaceableObject(
    'ericsson_cm_3g."LinkTransmissionProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataLinkTransmissionProfile_id",
        "dchStreamingPsDataFrameSynchRef",
        "dchCsDataFrameSynchRef",
        "cchFrameSynchRef",
        "dchUeRrcTypeFrameSynchRef",
        "dchAmrWbSpeechFrameSynchRef",
        "dchAmrSpeechFrameSynchRef",
        "reservedBy",
        "iubLinkType",
        "dchStreamingCsDataFrameSynchRef",
        "dchPsDataFrameSynchRef",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataLinkTransmissionProfile"

    """
)

Lm = ReplaceableObject(
    'ericsson_cm_3g."Lm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLm_id",
        "fingerprint",
        "lmState",
        "lastInventoryChange",
        "fingerprintUpdateable",
        "referenceToLicenseServer",
        "lastLicenseInventoryRefresh"
    FROM
    ericsson_bulkcm."vsDataLm"

    """
)

LoadBalancingFunction = ReplaceableObject(
    'ericsson_cm_3g."LoadBalancingFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataLoadBalancingFunction_id",
        "lbCeiling",
        "lbThreshold",
        "lbUtranOffloadBackoffTime",
        "lbHitRateEUtranMeasUeThreshold",
        "lbCauseCodeS1SourceTriggersOffload",
        "lbCauseCodeS1TargetAcceptsOffload",
        "lbHitRateEUtranAddThreshold",
        "lbHitRateUtranRemoveThreshold",
        "lbCauseCodeX2SourceTriggersOffload",
        "lbHitRateUtranMeasUeThreshold",
        "lbHitRateUtranAddThreshold",
        "lbHitRateUtranMeasUeIntensity",
        "lbHitRateEUtranRemoveThreshold",
        "lbCauseCodeX2TargetAcceptsOffload",
        "lbEUtranOffloadBackoffTime",
        "lbHitRateEUtranMeasUeIntensity",
        "lbMeasScalingLimit",
        "txPwrForOverlaidCellDetect",
        "lbCaThreshold",
        "lbDiffCaOffset",
        "lbCaCapHysteresis",
        "lbRateOffsetCoefficient",
        "lbRateOffsetLoadThreshold",
        "lbUeEvaluationTimer",
        "ocdMinHighHitThresh",
        "ocdMaxNoHighHitRateCells",
        "isUlEvalAllowedAtTpLbHo",
        "isUlEvalAllowedAtCaTrHo"
    FROM
    ericsson_bulkcm."vsDataLoadBalancingFunction"

    """
)

LoadControl = ReplaceableObject(
    'ericsson_cm_3g."LoadControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataGeneralProcessorUnit_id",
        "vsDataLoadControl_id"
    FROM
    ericsson_bulkcm."vsDataLoadControl"

    """
)

LocationArea = ReplaceableObject(
    'ericsson_cm_3g."LocationArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataAreas_id",
        "vsDataPlmn_id",
        "vsDataLocationArea_id",
        "userLabel",
        "lac",
        "t3212",
        "att"
    FROM
    ericsson_bulkcm."vsDataLocationArea"

    """
)

Log = ReplaceableObject(
    'ericsson_cm_3g."Log"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLogM_id",
        "vsDataLog_id",
        "severityFilter",
        "progressReport",
        "progressReport_actionName",
        "progressReport_progressInfo",
        "progressReport_progressPercentage",
        "progressReport_xossx_result",
        "progressReport_resultInfo",
        "progressReport_state",
        "progressReport_actionId",
        "progressReport_timeActionStarted",
        "progressReport_timeActionCompleted",
        "progressReport_timeOfLastStatusUpdate"
    FROM
    ericsson_bulkcm."vsDataLog"

    """
)

LogicalChannelGroup = ReplaceableObject(
    'ericsson_cm_3g."LogicalChannelGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataQciTable_id",
        "vsDataLogicalChannelGroup_id",
        "userLabel",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataLogicalChannelGroup"

    """
)

LogM = ReplaceableObject(
    'ericsson_cm_3g."LogM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLogM_id",
        "progressReport_actionName",
        "progressReport_progressInfo",
        "progressReport_progressPercentage",
        "progressReport_xossx_result",
        "progressReport_resultInfo",
        "progressReport_state",
        "progressReport_actionId",
        "progressReport_timeActionStarted",
        "progressReport_timeActionCompleted",
        "progressReport_timeOfLastStatusUpdate",
        "trustCategory",
        "nodeCredential",
        "progressReport"
    FROM
    ericsson_bulkcm."vsDataLogM"

    """
)

LppaEcid = ReplaceableObject(
    'ericsson_cm_3g."LppaEcid"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataLppaEcid_id",
        "featureStateLppaEcid",
        "keyIdLppaEcid",
        "licenseStateLppaEcid",
        "serviceStateLppaEcid"
    FROM
    ericsson_bulkcm."vsDataLppaEcid"

    """
)

LsmEcs = ReplaceableObject(
    'ericsson_cm_3g."LsmEcs"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataLsmEcs_id",
        "featureStateLsmEcs",
        "keyIdLsmEcs",
        "licenseStateLsmEcs",
        "serviceStateLsmEcs"
    FROM
    ericsson_bulkcm."vsDataLsmEcs"

    """
)

M3uAssociation = ReplaceableObject(
    'ericsson_cm_3g."M3uAssociation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataMtp3bSpItu_id",
        "vsDataM3uAssociation_id",
        "userLabel",
        "role",
        "mtp3bSrsId",
        "sctpId",
        "dscp",
        "localPortNumber",
        "autoStartAssociation",
        "remotePortNumber",
        "remoteIpAddress1",
        "remoteIpAddress2",
        "localIpMask",
        "congestionAlarmThreshold"
    FROM
    ericsson_bulkcm."vsDataM3uAssociation"

    """
)

MACConfiguration = ReplaceableObject(
    'ericsson_cm_3g."MACConfiguration"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataRadioBearerTable_id",
        "vsDataMACConfiguration_id",
        "ulMaxHARQTx"
    FROM
    ericsson_bulkcm."vsDataMACConfiguration"

    """
)

MaintenanceUser = ReplaceableObject(
    'ericsson_cm_3g."MaintenanceUser"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataUserIdentity_id",
        "vsDataMaintenanceUser_id",
        "subjectName",
        "userName",
        "password"
    FROM
    ericsson_bulkcm."vsDataMaintenanceUser"

    """
)

MaintenanceUserSecurity = ReplaceableObject(
    'ericsson_cm_3g."MaintenanceUserSecurity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataUserIdentity_id",
        "vsDataMaintenanceUserSecurity_id"
    FROM
    ericsson_bulkcm."vsDataMaintenanceUserSecurity"

    """
)

ManagedElementData = ReplaceableObject(
    'ericsson_cm_3g."ManagedElementData"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataManagedElementData_id",
        "documentServerAddress",
        "logonServerAddress",
        "minimumHdVolumeCFreespace",
        "autoConfigurationAllowed",
        "piuGroupEscalationType",
        "hdVolumeCSizeExt",
        "ntpServerAddressPrimary",
        "ntpServerAddressSecondary",
        "ntpBurstFlagThird",
        "ntpMaxPollThird",
        "ntpMinPollThird",
        "ntpServiceActiveThird",
        "ntpBurstFlagSecondary",
        "ntpServiceActivePrimary",
        "ntpMinPollPrimary",
        "ntpServiceActiveSecondary",
        "ntpMaxPollPrimary",
        "ntpBurstFlagPrimary",
        "ntpMinPollSecondary",
        "ntpMaxPollSecondary"
    FROM
    ericsson_bulkcm."vsDataManagedElementData"

    """
)

MaximumCellRange = ReplaceableObject(
    'ericsson_cm_3g."MaximumCellRange"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataMaximumCellRange_id",
        "featureStateMaximumCellRange",
        "keyIdMaximumCellRange",
        "licenseStateMaximumCellRange",
        "serviceStateMaximumCellRange"
    FROM
    ericsson_bulkcm."vsDataMaximumCellRange"

    """
)

MbmsM3Based = ReplaceableObject(
    'ericsson_cm_3g."MbmsM3Based"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataMbmsM3Based_id",
        "featureStateMbmsM3Based",
        "keyIdMbmsM3Based",
        "licenseStateMbmsM3Based",
        "serviceStateMbmsM3Based"
    FROM
    ericsson_bulkcm."vsDataMbmsM3Based"

    """
)

MbmsServiceArea = ReplaceableObject(
    'ericsson_cm_3g."MbmsServiceArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataAreas_id",
        "vsDataPlmn_id",
        "vsDataMbmsServiceArea_id",
        "userLabel",
        "sac"
    FROM
    ericsson_bulkcm."vsDataMbmsServiceArea"

    """
)

MdtConfiguration = ReplaceableObject(
    'ericsson_cm_3g."MdtConfiguration"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataMdtConfiguration_id",
        "reportAmountMdt",
        "reportingTrigger",
        "positioningMethod",
        "reportIntervalMdt",
        "a2ThresholdRsrqMdt",
        "a2ThresholdRsrpMdt",
        "hysteresisA2Mdt",
        "triggerQuantityA2Mdt",
        "maxReportCellsA2Mdt",
        "reportQuantityA2Mdt",
        "timeToTriggerA2Mdt"
    FROM
    ericsson_bulkcm."vsDataMdtConfiguration"

    """
)

MeasurementDefinition = ReplaceableObject(
    'ericsson_cm_3g."MeasurementDefinition"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataMeasurementDefinition_id",
        "neIndex",
        "filePrefix",
        "granularityPeriod",
        "reportPeriod",
        "measurementActive"
    FROM
    ericsson_bulkcm."vsDataMeasurementDefinition"

    """
)

MediumAccessUnit = ReplaceableObject(
    'ericsson_cm_3g."MediumAccessUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataGeneralProcessorUnit_id",
        "vsDataMediumAccessUnit_id",
        "vsDataCbu_id",
        "userLabel",
        "connectorLabel"
    FROM
    ericsson_bulkcm."vsDataMediumAccessUnit"

    """
)

MibManager = ReplaceableObject(
    'ericsson_cm_3g."MibManager"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataMibManager_id",
        "userLabel",
        "dumpFile",
        "mibDumpState"
    FROM
    ericsson_bulkcm."vsDataMibManager"

    """
)

MimoSleepFunction = ReplaceableObject(
    'ericsson_cm_3g."MimoSleepFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataMimoSleepFunction_id",
        "switchDownMonitorDurTimer",
        "sleepEndTime",
        "sleepStartTime",
        "switchUpMonitorDurTimer",
        "switchUpPrbThreshold",
        "sleepState",
        "switchDownRrcConnThreshold",
        "switchUpRrcConnThreshold",
        "switchDownPrbThreshold",
        "sleepMode",
        "sleepPowerControl"
    FROM
    ericsson_bulkcm."vsDataMimoSleepFunction"

    """
)

MixedMode = ReplaceableObject(
    'ericsson_cm_3g."MixedMode"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataMixedMode_id",
        "featureStateMixedMode",
        "keyIdMixedMode",
        "licenseStateMixedMode",
        "serviceStateMixedMode"
    FROM
    ericsson_bulkcm."vsDataMixedMode"

    """
)

MobCtrlAtPoorCov = ReplaceableObject(
    'ericsson_cm_3g."MobCtrlAtPoorCov"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataMobCtrlAtPoorCov_id",
        "featureStateMobCtrlAtPoorCov",
        "keyIdMobCtrlAtPoorCov",
        "licenseStateMobCtrlAtPoorCov",
        "serviceStateMobCtrlAtPoorCov"
    FROM
    ericsson_bulkcm."vsDataMobCtrlAtPoorCov"

    """
)

MocnCellProfile = ReplaceableObject(
    'ericsson_cm_3g."MocnCellProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataMocnCellProfile_id",
        "commonPlmnRef",
        "userLabel",
        "multiplePlmnListRef",
        "spare",
        "useCommonPlmn"
    FROM
    ericsson_bulkcm."vsDataMocnCellProfile"

    """
)

MpClusterHandling = ReplaceableObject(
    'ericsson_cm_3g."MpClusterHandling"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "vsDataMpClusterHandling_id",
        "primaryCoreRef"
    FROM
    ericsson_bulkcm."vsDataMpClusterHandling"

    """
)

MpProcessingResource = ReplaceableObject(
    'ericsson_cm_3g."MpProcessingResource"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataDeviceGroup_id",
        "vsDataMpProcessingResource_id",
        "vsDataFieldReplaceableUnit_id"
    FROM
    ericsson_bulkcm."vsDataMpProcessingResource"

    """
)

Mtp3bAp = ReplaceableObject(
    'ericsson_cm_3g."Mtp3bAp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataMtp3bSpItu_id",
        "vsDataMtp3bAp_id",
        "userLabel",
        "routeSetId",
        "serviceInd"
    FROM
    ericsson_bulkcm."vsDataMtp3bAp"

    """
)

Mtp3bSlItu = ReplaceableObject(
    'ericsson_cm_3g."Mtp3bSlItu"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataMtp3bSpItu_id",
        "vsDataMtp3bSls_id",
        "vsDataMtp3bSlItu_id",
        "userLabel",
        "tpId",
        "signLinkCode",
        "autoStartLink",
        "prioBeforeSio"
    FROM
    ericsson_bulkcm."vsDataMtp3bSlItu"

    """
)

Mtp3bSls = ReplaceableObject(
    'ericsson_cm_3g."Mtp3bSls"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataMtp3bSpItu_id",
        "vsDataMtp3bSls_id",
        "userLabel",
        "mtp3bSrsId",
        "cLinkAnsi"
    FROM
    ericsson_bulkcm."vsDataMtp3bSls"

    """
)

Mtp3bSpItu = ReplaceableObject(
    'ericsson_cm_3g."Mtp3bSpItu"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataMtp3bSpItu_id",
        "userLabel",
        "networkInd",
        "signallingPointCode",
        "version",
        "nodeBehaviour",
        "noOfCongestLevelForNI",
        "routeSetCongestTestFlag",
        "resendTfcInterval",
        "maxSizeReroutBuf",
        "maxSizeChangeBuf",
        "transFrHandler",
        "sioSpare",
        "statusIndInterval",
        "testPatternSltm",
        "spPriority_prioSlt",
        "spPriority_prioCo",
        "spPriority_prioCb",
        "spPriority_prioEc",
        "spPriority_prioRst",
        "spPriority_prioTra",
        "spPriority_prioUpu",
        "spPriority_prioLink",
        "spPriority_prioTfc",
        "spTimer_timerT1",
        "spTimer_timerT2",
        "spTimer_timerT3",
        "spTimer_timerT4",
        "spTimer_timerT5",
        "spTimer_timerT6",
        "spTimer_timerT8",
        "spTimer_timerT10",
        "spTimer_timerT12",
        "spTimer_timerT13",
        "spTimer_timerT14",
        "spTimer_timerT17",
        "spTimer_timerTBsnt",
        "spTimer_timerTRetrieval",
        "spTimer_timerTStart",
        "spTimer_timerTc",
        "spTimer_timerT18",
        "spTimer_timerT19",
        "spTimer_timerT20",
        "spTimer_timerT21",
        "spTimer_timerT22",
        "spTimer_timerT23",
        "spTimer_timerSlta",
        "spTimer_timerSltm",
        "spTimer_timerT15",
        "spTimer_timerT16",
        "spTimer_timerTDlack",
        "spTimer_timerM3uaPeriodicAudit",
        "spTimer_timerM3uaT1",
        "spTimer_timerM3uaT3",
        "spTimer_timerM3uaT40",
        "spTimer_timerM3uaT41",
        "spTimer_timerM3uaT42",
        "spTimer_timerM3uaT6",
        "spTimer_timerM3uaT8",
        "spTimer_timerM3uaTack",
        "spTimer_timerM3uaTassocack",
        "spTimer_timerM3uaTc",
        "rpuId",
        "m3uaNoOfAttempsOfDauds",
        "noOfAttempsOfAssociationEstablishment"
    FROM
    ericsson_bulkcm."vsDataMtp3bSpItu"

    """
)

Mtp3bSr = ReplaceableObject(
    'ericsson_cm_3g."Mtp3bSr"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataMtp3bSpItu_id",
        "vsDataMtp3bSrs_id",
        "vsDataMtp3bSr_id",
        "userLabel",
        "linkSetM3uId",
        "priority"
    FROM
    ericsson_bulkcm."vsDataMtp3bSr"

    """
)

Mtp3bSrs = ReplaceableObject(
    'ericsson_cm_3g."Mtp3bSrs"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataMtp3bSpItu_id",
        "vsDataMtp3bSrs_id",
        "userLabel",
        "destPointCode",
        "preferredBearer"
    FROM
    ericsson_bulkcm."vsDataMtp3bSrs"

    """
)

MultiCarrier = ReplaceableObject(
    'ericsson_cm_3g."MultiCarrier"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCell_id",
        "vsDataHsdsch_id",
        "vsDataEul_id",
        "vsDataMultiCarrier_id",
        "cellRefsDl",
        "multiCarrierSupport",
        "dualBandMultiCarrierSupport",
        "multiCarrierMimoSupport",
        "eulMultiCarrierSupport",
        "cellRefsDlSecondBand",
        "hsdpaDb3McSupport",
        "hsdpa3McSupport"
    FROM
    ericsson_bulkcm."vsDataMultiCarrier"

    """
)

MulticastAntennaBranch = ReplaceableObject(
    'ericsson_cm_3g."MulticastAntennaBranch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "vsDataMulticastAntennaBranch_id",
        "availabilityStatus",
        "transceiverRef",
        "operationalState",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataMulticastAntennaBranch"

    """
)

MultiErabsPerUser = ReplaceableObject(
    'ericsson_cm_3g."MultiErabsPerUser"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataMultiErabsPerUser_id",
        "licenseStateMultiErabsPerUser",
        "keyIdMultiErabsPerUser",
        "featureStateMultiErabsPerUser",
        "serviceStateMultiErabsPerUser"
    FROM
    ericsson_bulkcm."vsDataMultiErabsPerUser"

    """
)

NbapCommon = ReplaceableObject(
    'ericsson_cm_3g."NbapCommon"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataIub_id",
        "vsDataNbapCommon_id",
        "RncFunction_id",
        "IubLink_id",
        "l2EstablishReqRetryT",
        "l2EstablishSupervisionT",
        "l3EstablishSupervisionT",
        "auditRetransmissionT",
        "uniSaalTpRef1",
        "uniSaalTpRef2",
        "userLabel",
        "sctpEndpointRef",
        "operationalState",
        "activeUniSaalTpRef",
        "standbyUniSaalTpRef",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataNbapCommon"

    """
)

NbapDedicated = ReplaceableObject(
    'ericsson_cm_3g."NbapDedicated"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataIub_id",
        "vsDataNbapDedicated_id",
        "RncFunction_id",
        "IubLink_id",
        "l2EstablishReqRetryT",
        "uniSaalTpRef2",
        "uniSaalTpRef1",
        "l2EstablishSupervisionT",
        "userLabel",
        "sctpEndpointRef",
        "operationalState",
        "activeUniSaalTpRef",
        "standbyUniSaalTpRef",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataNbapDedicated"

    """
)

NetconfSsh = ReplaceableObject(
    'ericsson_cm_3g."NetconfSsh"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataNetconfSsh_id",
        "administrativeState",
        "port"
    FROM
    ericsson_bulkcm."vsDataNetconfSsh"

    """
)

NetconfTls = ReplaceableObject(
    'ericsson_cm_3g."NetconfTls"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataNetconfTls_id",
        "administrativeState",
        "trustCategory",
        "nodeCredential",
        "port"
    FROM
    ericsson_bulkcm."vsDataNetconfTls"

    """
)

NextHop = ReplaceableObject(
    'ericsson_cm_3g."NextHop"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataRouter_id",
        "vsDataRouteTableIPv4Static_id",
        "vsDataDst_id",
        "vsDataNextHop_id",
        "vsDataHost_id",
        "address",
        "bfdMonitoring",
        "adminDistance",
        "reference",
        "discard"
    FROM
    ericsson_bulkcm."vsDataNextHop"

    """
)

NniSaalProfile = ReplaceableObject(
    'ericsson_cm_3g."NniSaalProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataNniSaalProfile_id",
        "userLabel",
        "profileData_timerPoll",
        "profileData_maxCC",
        "profileData_maxPD",
        "profileData_maxStat",
        "profileData_initialCredit",
        "profileData_timerKeepAlive",
        "profileData_timerNoResponse",
        "profileData_timerIdle",
        "profileData_timerCC",
        "profileData_mps",
        "profileData_congestionLevel1OnSet",
        "profileData_congestionLevel2OnSet",
        "profileData_congestionLevel3OnSet",
        "profileData_congestionLevel1Abatement",
        "profileData_congestionLevel2Abatement",
        "profileData_congestionLevel3Abatement",
        "profileData_nrOfPDUsDuringProving",
        "profileData_maxNRP",
        "profileData_timerNoCredit",
        "profileData_timerRepeatSrec",
        "profileData_timerT1",
        "profileData_timerT2",
        "profileData_timerT3",
        "profileData_discardMessagesLevel1",
        "profileData_discardMessagesLevel2",
        "profileData_discardMessagesLevel3"
    FROM
    ericsson_bulkcm."vsDataNniSaalProfile"

    """
)

NniSaalTp = ReplaceableObject(
    'ericsson_cm_3g."NniSaalTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataNniSaalTp_id",
        "userLabel",
        "nniSaalProfileId",
        "aal5TpVccTpId",
        "maxSduSize"
    FROM
    ericsson_bulkcm."vsDataNniSaalTp"

    """
)

NodeBLocalCell = ReplaceableObject(
    'ericsson_cm_3g."NodeBLocalCell"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "extraCompForSigHsFach",
        "extraHsScchCompHsFach",
        "hsScchMinCodePower",
        "uarfcnUl",
        "extraCompHsFach",
        "userLabel",
        "maxEAgchPowerDl",
        "uarfcnDl",
        "extraPowerForSrbOnHsdpa",
        "hsdpaMcInactivityTimer",
        "administrativeState",
        "schNoCongThreshGbr",
        "hsdpaMcActivityBufferThreshold",
        "qualityCheckPowerEHich",
        "queueSelectAlgorithm",
        "qualityCheckPower",
        "schCongThreshNonGbr",
        "schWeight",
        "extraCompEnhUeDrx",
        "schCongThreshGbr",
        "schCongPeriodGbr",
        "chQualOffset",
        "extraHsScchCompEnhUeDrx",
        "eHichMinCodePower",
        "schMinPowerNonGbrHsUsers",
        "schNoCongPeriodGbr",
        "defaultCqiHsFach",
        "minDlPowerCapability",
        "airRateTypeSelector",
        "maxUserEHichERgchPowerDl",
        "cqiAdjustmentOn",
        "operatingBand",
        "hsScchMaxCodePower",
        "extraHsScchCompForSigHsFach",
        "extraHsScchPowerForSrbOnHsdpa",
        "hsPowerMargin",
        "eulMaxNoSchEDch",
        "schPowerDeltaCongGbr",
        "eulMinMarginCoverage",
        "maxDlPowerCapability",
        "minBitRate",
        "schMaxDelay",
        "localCellId",
        "maxEAgchPowerDlTti2",
        "schPrioForAbsResSharing",
        "maxUserEHichPowerDlTti2",
        "cqiErrors",
        "cqiErrorsAbsent",
        "eulNoERgchGroups",
        "hsdpaMcCapability",
        "featCtrlHsdpaMc",
        "featCtrlEnhancedLayer2",
        "featCtrlHsdpaDynamicCodeAllocation",
        "featCtrlHsdpaIncrementalRedundancy",
        "availabilityStatus",
        "minSpreadingFactor",
        "operationalState",
        "usageState",
        "powerSharingMaxTransmissionPower",
        "maxNumEulUsers",
        "featCtrlHsdpaPowerSharing",
        "featCtrlImprovedLayer2",
        "maxNumHsdpaUsers",
        "featCtrlNbir",
        "maxNumHsPdschCodes",
        "featCtrlEnhUeDrx",
        "featCtrlFDpchSrbOnHsdpa",
        "featCtrlHsFach",
        "hsdpaPowerSharingCapability",
        "featCtrlHsdpaDbMc",
        "featCtrlHsdpaMcInactCtrl",
        "reservedBy",
        "hsdpaDbMcCapability",
        "throughputPqxHsdpaFach"
    FROM
    ericsson_bulkcm."vsDataNodeBLocalCell"

    """
)

NodeBLocalCellGroup = ReplaceableObject(
    'ericsson_cm_3g."NodeBLocalCellGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "administrativeState",
        "userLabel",
        "multiCarrierPair5",
        "multiCarrierPair6",
        "multiCarrierPair3",
        "multiCarrierPair4",
        "multiCarrierPair1",
        "multiCarrierPair2"
    FROM
    ericsson_bulkcm."vsDataNodeBLocalCellGroup"

    """
)

NodeBSectorCarrier = ReplaceableObject(
    'ericsson_cm_3g."NodeBSectorCarrier"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "vsDataNodeBSectorCarrier_id",
        "utranCellRef",
        "rfBranchTxRef",
        "bandwidthDl",
        "rfBranchRxRef",
        "maxDlPowerCapability",
        "eulNoiseFloorLock",
        "eulThermalLevelPrior",
        "cellRange",
        "eulMaxRotCoverage",
        "numOfRxAntennas",
        "numOfTxAntennas",
        "minDlPowerCapability",
        "bandwidthUl",
        "sectorEquipmentFunctionRef",
        "eulMaxOwnUuLoad",
        "eulLockedNoiseFloor",
        "fccRotMarginHigh",
        "fccRotMarginLow",
        "geoDatum",
        "latHemisphere",
        "height",
        "longitude",
        "latitude",
        "beamDirection",
        "availabilityStatus",
        "operationalState",
        "configuredMaxTxPower",
        "numOfBranchWithNbir"
    FROM
    ericsson_bulkcm."vsDataNodeBSectorCarrier"

    """
)

NodeCredential = ReplaceableObject(
    'ericsson_cm_3g."NodeCredential"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataNodeCredential_id",
        "userLabel",
        "subjectName",
        "enrollmentTimer",
        "enrollmentServerGroup",
        "keyInfo",
        "enrollmentProgress_actionName",
        "enrollmentProgress_progressInfo",
        "enrollmentProgress_progressPercentage",
        "enrollmentProgress_xossx_result",
        "enrollmentProgress_resultInfo",
        "enrollmentProgress_state",
        "enrollmentProgress_actionId",
        "enrollmentProgress_timeActionStarted",
        "enrollmentProgress_timeActionCompleted",
        "enrollmentProgress_timeOfLastStatusUpdate",
        "renewalMode",
        "certificateState",
        "certificateContent_version",
        "certificateContent_serialNumber",
        "certificateContent_signatureAlgorithm",
        "certificateContent_issuer",
        "certificateContent_validFrom",
        "certificateContent_validTo",
        "certificateContent_publicKey",
        "certificateContent_publicKeyAlgorithm",
        "certificateContent_keyUsage",
        "certificateContent_subject",
        "enrollmentAuthority",
        "expiryAlarmThreshold",
        "subjectAltName"
    FROM
    ericsson_bulkcm."vsDataNodeCredential"

    """
)

NodeFunction = ReplaceableObject(
    'ericsson_cm_3g."NodeFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeFunction_id",
        "alarmSuppressed",
        "oamIpAddress",
        "rbsConfigLevel"
    FROM
    ericsson_bulkcm."vsDataNodeFunction"

    """
)

NodeGroupSyncMember = ReplaceableObject(
    'ericsson_cm_3g."NodeGroupSyncMember"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataRadioEquipmentClock_id",
        "vsDataNodeGroupSyncMember_id",
        "administrativeState",
        "syncRiPortCandidate",
        "syncNodePriority",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataNodeGroupSyncMember"

    """
)

NodeManagementFunction = ReplaceableObject(
    'ericsson_cm_3g."NodeManagementFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeManagementFunction_id",
        "alarmSuppressed",
        "nodeTag",
        "antennaDeviceScanInBackground",
        "technicianPresent"
    FROM
    ericsson_bulkcm."vsDataNodeManagementFunction"

    """
)

NodeSupport = ReplaceableObject(
    'ericsson_cm_3g."NodeSupport"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "supportFunction",
        "release",
        "userLabel",
        "siteEquipment",
        "licenseHandling",
        "unlockRbsAfterIntegration",
        "siteInstallation",
        "siteBasic",
        "postIntegrationBulkfile_bulkCMURI",
        "postIntegrationBulkfile_userID",
        "postIntegrationBulkfile_activationScheme",
        "postIntegrationBulkfile_activationPolicy",
        "activateLicenses",
        "rbsSummary",
        "upgradePackage",
        "integrationSequence",
        "nodeContext_domain",
        "boundInstallation",
        "hwSerialNumber"
    FROM
    ericsson_bulkcm."vsDataNodeSupport"

    """
)

NodeSynch = ReplaceableObject(
    'ericsson_cm_3g."NodeSynch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "IubLink_id",
        "vsDataNodeSynch_id",
        "userLabel",
        "phaseDiffThreshold",
        "sampleIntervalInit",
        "fixedWindowSizeInit",
        "sampleIntervalSup",
        "fixedWindowSizeSup",
        "slidingWindowSize",
        "maxAllowedIubRtt",
        "transportDelayMeasDiscRatio"
    FROM
    ericsson_bulkcm."vsDataNodeSynch"

    """
)

NonPlannedPciDrxProfile = ReplaceableObject(
    'ericsson_cm_3g."NonPlannedPciDrxProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataNonPlannedPciDrxProfile_id",
        "nonPlannedPciOnDurationTimer",
        "nonPlannedPciLongDrxCycle",
        "nonPlannedPciDrxInactivityTimer"
    FROM
    ericsson_bulkcm."vsDataNonPlannedPciDrxProfile"

    """
)

Ntp = ReplaceableObject(
    'ericsson_cm_3g."Ntp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataNtp_id"
    FROM
    ericsson_bulkcm."vsDataNtp"

    """
)

NtpFrequencySync = ReplaceableObject(
    'ericsson_cm_3g."NtpFrequencySync"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataNtp_id",
        "vsDataNtpFrequencySync_id",
        "availabilityStatus",
        "cachedIpAddress",
        "dscp",
        "ingressUdpPort",
        "syncServerNtpIpAddress",
        "operationalState",
        "addressIPv4Reference",
        "reservedBy",
        "ntpFrequencySyncStatus"
    FROM
    ericsson_bulkcm."vsDataNtpFrequencySync"

    """
)

NtpServer = ReplaceableObject(
    'ericsson_cm_3g."NtpServer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataTimeSetting_id",
        "vsDataNtpServer_id",
        "serviceActive",
        "serverAddress",
        "serviceStatus",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataNtpServer"

    """
)

OamAccessPoint = ReplaceableObject(
    'ericsson_cm_3g."OamAccessPoint"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataOamAccessPoint_id",
        "accessPoint"
    FROM
    ericsson_bulkcm."vsDataOamAccessPoint"

    """
)

OamTrafficClass = ReplaceableObject(
    'ericsson_cm_3g."OamTrafficClass"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataOamTrafficClass_id",
        "dscp",
        "xossx_name"
    FROM
    ericsson_bulkcm."vsDataOamTrafficClass"

    """
)

OctAntUlPerfPkg = ReplaceableObject(
    'ericsson_cm_3g."OctAntUlPerfPkg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataOctAntUlPerfPkg_id",
        "featureStateOctAntUlPerfPkg",
        "keyIdOctAntUlPerfPkg",
        "licenseStateOctAntUlPerfPkg",
        "serviceStateOctAntUlPerfPkg"
    FROM
    ericsson_bulkcm."vsDataOctAntUlPerfPkg"

    """
)

OnSiteActivities = ReplaceableObject(
    'ericsson_cm_3g."OnSiteActivities"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "vsDataOnSiteActivities_id",
        "technicianPresent"
    FROM
    ericsson_bulkcm."vsDataOnSiteActivities"

    """
)

OperatorDefinedQci = ReplaceableObject(
    'ericsson_cm_3g."OperatorDefinedQci"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataOperatorDefinedQci_id",
        "featureStateOperatorDefinedQci",
        "keyIdOperatorDefinedQci",
        "licenseStateOperatorDefinedQci",
        "serviceStateOperatorDefinedQci"
    FROM
    ericsson_bulkcm."vsDataOperatorDefinedQci"

    """
)

OpProfiles = ReplaceableObject(
    'ericsson_cm_3g."OpProfiles"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataOpProfiles_id",
        "profileList_opProfileName",
        "profileList_isActive",
        "profileList_isAutomatic"
    FROM
    ericsson_bulkcm."vsDataOpProfiles"

    """
)

OptionalFeatureLicense = ReplaceableObject(
    'ericsson_cm_3g."OptionalFeatureLicense"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatureLicense_id",
        "featureState",
        "keyId",
        "licenseState",
        "serviceState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataOptionalFeatureLicense"

    """
)

OptionalFeatures = ReplaceableObject(
    'ericsson_cm_3g."OptionalFeatures"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id"
    FROM
    ericsson_bulkcm."vsDataOptionalFeatures"

    """
)

Os155SpiTtp = ReplaceableObject(
    'ericsson_cm_3g."Os155SpiTtp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminal_id",
        "vsDataOs155SpiTtp_id",
        "administrativeState",
        "userLabel",
        "lineNo",
        "standardMode",
        "shutDownTimeout",
        "muxMode",
        "msDegThreshold",
        "msDegM",
        "msRdiReporting",
        "msAisReporting",
        "loopBack",
        "poissonDegThreshold",
        "supervisionMode",
        "sfpInformation_sfpProductNumber",
        "sfpInformation_sfpType",
        "sfpInformation_sfpState",
        "sfpPort"
    FROM
    ericsson_bulkcm."vsDataOs155SpiTtp"

    """
)

OtdoaSupl = ReplaceableObject(
    'ericsson_cm_3g."OtdoaSupl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataOtdoaSupl_id",
        "keyIdOtdoaSupl",
        "featureStateOtdoaSupl",
        "licenseStateOtdoaSupl",
        "serviceStateOtdoaSupl"
    FROM
    ericsson_bulkcm."vsDataOtdoaSupl"

    """
)

PacketFrequencySyncRef = ReplaceableObject(
    'ericsson_cm_3g."PacketFrequencySyncRef"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataSynchronization_id",
        "vsDataPacketFrequencySyncRef_id",
        "administrativeState",
        "cachedIpAddress",
        "dscp",
        "ipAccessHostEtRef",
        "ptpDomain",
        "ptpOwnPortIdentity_clockIdentity",
        "ptpOwnPortIdentity_ptpPortNumber",
        "serverAddress",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataPacketFrequencySyncRef"

    """
)

Paging = ReplaceableObject(
    'ericsson_cm_3g."Paging"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataPaging_id",
        "RncFunction_id",
        "maxNoOfPagingRecords",
        "defaultPagingCycle",
        "nB",
        "pagingDiscardTimer",
        "noOfDefPagCyclPrim",
        "cnDrxCycleLengthCs",
        "cnDrxCycleLengthPs",
        "noOfPagingRecordTransm",
        "utranDrxCycleLength",
        "noOfPagingRecordTransmUtran"
    FROM
    ericsson_bulkcm."vsDataPaging"

    """
)

Pch = ReplaceableObject(
    'ericsson_cm_3g."Pch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCell_id",
        "vsDataPch_id",
        "userLabel",
        "pchPower",
        "pichPower",
        "sccpchOffset",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataPch"

    """
)

Pci = ReplaceableObject(
    'ericsson_cm_3g."Pci"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataPci_id",
        "featureStatePci",
        "keyIdPci",
        "licenseStatePci",
        "serviceStatePci"
    FROM
    ericsson_bulkcm."vsDataPci"

    """
)

PcpSetToQueue = ReplaceableObject(
    'ericsson_cm_3g."PcpSetToQueue"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataQueueSystem_id",
        "vsDataQoSClassifier_id",
        "vsDataPcpToQueueMap_id",
        "vsDataPcpSetToQueue_id",
        "queue",
        "pcpSet"
    FROM
    ericsson_bulkcm."vsDataPcpSetToQueue"

    """
)

PcpToQueueMap = ReplaceableObject(
    'ericsson_cm_3g."PcpToQueueMap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataQueueSystem_id",
        "vsDataQoSClassifier_id",
        "vsDataPcpToQueueMap_id",
        "defaultQueue",
        "userLabel",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataPcpToQueueMap"

    """
)

PdrDevice = ReplaceableObject(
    'ericsson_cm_3g."PdrDevice"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSpDevicePool_id",
        "vsDataPdrDevice_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataPdrDevice"

    """
)

PeerIPv4 = ReplaceableObject(
    'ericsson_cm_3g."PeerIPv4"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataHost_id",
        "vsDataPeerIPv4_id",
        "address"
    FROM
    ericsson_bulkcm."vsDataPeerIPv4"

    """
)

Pfs = ReplaceableObject(
    'ericsson_cm_3g."Pfs"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataPfs_id",
        "featureStatePfs",
        "keyIdPfs",
        "licenseStatePfs",
        "serviceStatePfs"
    FROM
    ericsson_bulkcm."vsDataPfs"

    """
)

PiuDevice = ReplaceableObject(
    'ericsson_cm_3g."PiuDevice"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataPiuDevice_id",
        "administrativeState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataPiuDevice"

    """
)

Plmn = ReplaceableObject(
    'ericsson_cm_3g."Plmn"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataAreas_id",
        "vsDataPlmn_id",
        "userLabel",
        "mcc",
        "mnc",
        "mncLength",
        "aliasPlmnIdentities"
    FROM
    ericsson_bulkcm."vsDataPlmn"

    """
)

PlmnIdentityGroup = ReplaceableObject(
    'ericsson_cm_3g."PlmnIdentityGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPlmnIdentityGroup_id",
        "plmn_mcc",
        "plmn_mnc",
        "plmn_mncLength",
        "userLabel",
        "plmn"
    FROM
    ericsson_bulkcm."vsDataPlmnIdentityGroup"

    """
)

PlugInUnit = ReplaceableObject(
    'ericsson_cm_3g."PlugInUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "administrativeState",
        "allowedSeqRestarts",
        "piuGroupNumber",
        "piuType",
        "productType",
        "userLabel",
        "unitType",
        "positionRef"
    FROM
    ericsson_bulkcm."vsDataPlugInUnit"

    """
)

Pm = ReplaceableObject(
    'ericsson_cm_3g."Pm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPm_id"
    FROM
    ericsson_bulkcm."vsDataPm"

    """
)

PmEventM = ReplaceableObject(
    'ericsson_cm_3g."PmEventM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPmEventM_id"
    FROM
    ericsson_bulkcm."vsDataPmEventM"

    """
)

PmEventService = ReplaceableObject(
    'ericsson_cm_3g."PmEventService"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataPmEventService_id",
        "cellTraceHighPrioReserve",
        "totalCellTraceStorageSize",
        "cellTraceFileSize",
        "totalEventStorageSize",
        "ueTraceFileSize",
        "totalUeTraceStorageSize",
        "streamPortPmUeTrace",
        "streamStatusPmCellTrace_traceReference",
        "streamStatusPmCellTrace_scannerId",
        "streamStatusPmCellTrace_ipAddress",
        "streamStatusPmCellTrace_portNumber",
        "streamStatusPmCellTrace_fileStatus",
        "streamStatusPmCellTrace_streamStatus",
        "streamStatusPmUeTrace_traceReference",
        "streamStatusPmUeTrace_scannerId",
        "streamStatusPmUeTrace_ipAddress",
        "streamStatusPmUeTrace_portNumber",
        "streamStatusPmUeTrace_fileStatus",
        "streamStatusPmUeTrace_streamStatus",
        "eventsExcludedFromUeTrace",
        "cellTracePeriodicReport",
        "streamStatusNotification"
    FROM
    ericsson_bulkcm."vsDataPmEventService"

    """
)

PmInitiatedUeMeasurements = ReplaceableObject(
    'ericsson_cm_3g."PmInitiatedUeMeasurements"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataPmInitiatedUeMeasurements_id",
        "featureStatePmInitiatedUeMeasurements",
        "keyIdPmInitiatedUeMeasurements",
        "licenseStatePmInitiatedUeMeasurements",
        "serviceStatePmInitiatedUeMeasurements"
    FROM
    ericsson_bulkcm."vsDataPmInitiatedUeMeasurements"

    """
)

PmMeasurementCapabilities = ReplaceableObject(
    'ericsson_cm_3g."PmMeasurementCapabilities"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPm_id",
        "vsDataPmMeasurementCapabilities_id",
        "alignedReportingPeriod",
        "fileLocation",
        "finalROP",
        "jobPrioritizationSupport",
        "jobStartStopSupport",
        "maxNoOfJobs",
        "maxNoOfMeasurements",
        "maxNoOfPmFiles",
        "measurementJobSupport",
        "realTimeJobSupport",
        "thresholdJobSupport",
        "fileRPSupported",
        "supportedCompressionTypes",
        "supportedThreshJobGps",
        "supportedRopPeriods",
        "supportedRtJobGps",
        "supportedMeasJobGps",
        "jobGroupingSupport",
        "producesUtcRopFiles"
    FROM
    ericsson_bulkcm."vsDataPmMeasurementCapabilities"

    """
)

PmService = ReplaceableObject(
    'ericsson_cm_3g."PmService"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPmService_id",
        "minorAlarmCeasingDelta",
        "warningAlarmLimitPercent",
        "warningAlarmCeasingDelta",
        "performanceDataVolume",
        "transactionTimeOut",
        "maxNoOfPmFiles",
        "maxNoOfCounters",
        "maxNoOfMonitors"
    FROM
    ericsson_bulkcm."vsDataPmService"

    """
)

PmSupport = ReplaceableObject(
    'ericsson_cm_3g."PmSupport"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "vsDataPmSupport_id",
        "ropFileHandling"
    FROM
    ericsson_bulkcm."vsDataPmSupport"

    """
)

PmUeMeasControl = ReplaceableObject(
    'ericsson_cm_3g."PmUeMeasControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataPmUeMeasControl_id",
        "ueMeasIntraFreq1_eutranFrequencyRef",
        "ueMeasIntraFreq1_reportConfigEUtraIntraFreqPmRef",
        "ueMeasIntraFreq2_eutranFrequencyRef",
        "ueMeasIntraFreq2_reportConfigEUtraIntraFreqPmRef",
        "measQuantityUtraFDDPm",
        "ueMeasInterFreq1_eutranFrequencyRef",
        "ueMeasInterFreq1_reportConfigEUtraInterFreqPmRef",
        "ueMeasInterFreq2_eutranFrequencyRef",
        "ueMeasInterFreq2_reportConfigEUtraInterFreqPmRef",
        "ueMeasInterRat1_geranFrequencyRef",
        "ueMeasInterRat1_utranFrequencyRef",
        "ueMeasInterRat1_reportConfigInterRatPmRef",
        "measGapAllowedPm",
        "ueMeasInterRat2_geranFrequencyRef",
        "ueMeasInterRat2_utranFrequencyRef",
        "ueMeasInterRat2_reportConfigInterRatPmRef"
    FROM
    ericsson_bulkcm."vsDataPmUeMeasControl"

    """
)

PmUlInterferenceReport = ReplaceableObject(
    'ericsson_cm_3g."PmUlInterferenceReport"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataSectorCarrier_id",
        "vsDataPmUlInterferenceReport_id",
        "rfBranchRxRef"
    FROM
    ericsson_bulkcm."vsDataPmUlInterferenceReport"

    """
)

PositioningServiceClass = ReplaceableObject(
    'ericsson_cm_3g."PositioningServiceClass"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUePositioning_id",
        "vsDataPositioningServiceClass_id",
        "userLabel",
        "firstAttemptResultQosCheck",
        "secondAttemptResultQosCheck",
        "firstAttemptCandidate",
        "secondAttemptMethod",
        "thirdAttemptMethod",
        "agpsMeasTimeMax",
        "fixedRespTimeMax",
        "lowDelayRespTimeMax",
        "delayTolerantRespTimeMax",
        "shapeConversionP",
        "shapeConversionEa",
        "shapeConversionEp",
        "shapeConversionEpuc",
        "shapeConversionEpue",
        "shapeConversionEpa",
        "shapeConversionEpaue",
        "reportedConfidenceLevel"
    FROM
    ericsson_bulkcm."vsDataPositioningServiceClass"

    """
)

PowerControl = ReplaceableObject(
    'ericsson_cm_3g."PowerControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataPowerControl_id",
        "cBackOff",
        "ulOuterLoopRegulator",
        "ulSirStep",
        "sirMin",
        "sirMax",
        "dlPcMethod",
        "cPO",
        "pO1",
        "pO2",
        "pO3",
        "ecNoPcpichDefault",
        "pcpichPowerDefault",
        "fixedPowerDl",
        "cNbifho",
        "fixedRefPower",
        "initShoPowerParam",
        "dlInitSirTarget",
        "ulInitSirTargetExtraHigh",
        "ulInitSirTargetHigh",
        "ulInitSirTargetLow",
        "ulInitSirTargetSrb",
        "transmissionTargetError",
        "ulInitSirTargetEdch",
        "transmissionTargetErrorTti2",
        "ulSirStepTti2",
        "ulInitSirTargetEdchTti2",
        "sirMaxTti2",
        "fdpchErrorRateTarget",
        "ulInitSirTargetEdchSrb",
        "rachMeasCompLimitHsFach",
        "hysteresisSiUpdateRimUtraSi",
        "hsOlpcCompFactorUlQual",
        "hsOlpcCpichImbalThresh",
        "hsOlpcMaxSirDelta",
        "ulInactSirTargetResetTimeEul",
        "ulInactSirTargetResetTti10",
        "ulInactSirTargetResetTti2",
        "ulSirStepTti10",
        "sirMaxTti10",
        "ulInactSirTargetReset",
        "ulInactSirTargetResetTime"
    FROM
    ericsson_bulkcm."vsDataPowerControl"

    """
)

PowerDistribution = ReplaceableObject(
    'ericsson_cm_3g."PowerDistribution"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipmentSupportFunction_id",
        "vsDataPowerDistribution_id",
        "mainLoadUndervoltageDisconnect",
        "priorityLoadUndervoltageDisconnect",
        "undervoltageDisconnectCeaseOffset",
        "controlDomainRef",
        "availabilityStatus"
    FROM
    ericsson_bulkcm."vsDataPowerDistribution"

    """
)

PowerSupply = ReplaceableObject(
    'ericsson_cm_3g."PowerSupply"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipmentSupportFunction_id",
        "vsDataPowerSupply_id",
        "nominalVoltage",
        "systemUndervoltageAlarmCeaseOffset",
        "systemUndervoltageAlarmLevel",
        "controlDomainRef",
        "multiplePowerSystem",
        "systemOvervoltageAlarmLevel",
        "availabilityStatus",
        "systemOvervoltageAlarmCeaseOffset"
    FROM
    ericsson_bulkcm."vsDataPowerSupply"

    """
)

PredefRbsScannerGpeh = ReplaceableObject(
    'ericsson_cm_3g."PredefRbsScannerGpeh"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataPredefRbsScannerGpeh_id",
        "maxStorageSize",
        "fileLocation"
    FROM
    ericsson_bulkcm."vsDataPredefRbsScannerGpeh"

    """
)

PreschedulingProfile = ReplaceableObject(
    'ericsson_cm_3g."PreschedulingProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataPreschedulingProfile_id",
        "preschedulingPeriod",
        "preschedulingDataSize",
        "preschedulingDuration"
    FROM
    ericsson_bulkcm."vsDataPreschedulingProfile"

    """
)

ProcessorLoad = ReplaceableObject(
    'ericsson_cm_3g."ProcessorLoad"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataGeneralProcessorUnit_id",
        "vsDataProcessorLoad_id",
        "vsDataRbsUnit_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataProcessorLoad"

    """
)

Ptp = ReplaceableObject(
    'ericsson_cm_3g."Ptp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataPtp_id"
    FROM
    ericsson_bulkcm."vsDataPtp"

    """
)

PtpBcOcPort = ReplaceableObject(
    'ericsson_cm_3g."PtpBcOcPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataPtp_id",
        "vsDataBoundaryOrdinaryClock_id",
        "vsDataPtpBcOcPort_id",
        "syncMessageInterval",
        "availabilityStatus",
        "asymmetryCompensation",
        "administrativeState",
        "operationalState",
        "announceMessageInterval",
        "transportInterface",
        "pBit",
        "ptpMulticastAddress",
        "durationField",
        "cachedIpAddress",
        "associatedGrandmaster",
        "dscp",
        "ptpPortStatus"
    FROM
    ericsson_bulkcm."vsDataPtpBcOcPort"

    """
)

Pws = ReplaceableObject(
    'ericsson_cm_3g."Pws"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataPws_id",
        "featureStatePws",
        "keyIdPws",
        "licenseStatePws",
        "serviceStatePws"
    FROM
    ericsson_bulkcm."vsDataPws"

    """
)

QciProfilePredefined = ReplaceableObject(
    'ericsson_cm_3g."QciProfilePredefined"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataQciTable_id",
        "vsDataQciProfilePredefined_id",
        "userLabel",
        "qci",
        "priority",
        "dscp",
        "logicalChannelGroupRef",
        "aqmMode",
        "dlMinBitRate",
        "resourceType",
        "rlcMode",
        "dataFwdPerQciEnabled",
        "absPrioOverride",
        "schedulingAlgorithm",
        "ulMinBitRate",
        "measReportConfigParams_a1ThresholdRsrpPrimOffset",
        "measReportConfigParams_a1ThresholdRsrpSecOffset",
        "measReportConfigParams_a1ThresholdRsrqPrimOffset",
        "measReportConfigParams_a1ThresholdRsrqSecOffset",
        "measReportConfigParams_a2ThresholdRsrpPrimOffset",
        "measReportConfigParams_a2ThresholdRsrpSecOffset",
        "measReportConfigParams_a2ThresholdRsrqPrimOffset",
        "measReportConfigParams_a2ThresholdRsrqSecOffset",
        "measReportConfigParams_a5Threshold1RsrpOffset",
        "measReportConfigParams_a5Threshold1RsrqOffset",
        "measReportConfigParams_a5Threshold2RsrpOffset",
        "measReportConfigParams_a5Threshold2RsrqOffset",
        "measReportConfigParams_b2Threshold1RsrpCdma2000Offset",
        "measReportConfigParams_b2Threshold1RsrqCdma2000Offset",
        "measReportConfigParams_b2Threshold2Cdma2000Offset",
        "measReportConfigParams_b2Threshold1RsrpGeranOffset",
        "measReportConfigParams_b2Threshold1RsrqGeranOffset",
        "measReportConfigParams_b2Threshold2GeranOffset",
        "measReportConfigParams_b2Threshold1RsrpUtraOffset",
        "measReportConfigParams_b2Threshold1RsrqUtraOffset",
        "measReportConfigParams_b2Threshold2EcNoUtraOffset",
        "measReportConfigParams_b2Threshold2RscpUtraOffset",
        "pdb",
        "qciACTuning",
        "qciSubscriptionQuanta",
        "resourceAllocationStrategy",
        "srsAllocationStrategy",
        "dlResourceAllocationStrategy",
        "relativePriority",
        "rohcEnabled",
        "drxPriority",
        "drxProfileRef",
        "serviceType",
        "counterActiveMode",
        "reservedBy",
        "rlfPriority",
        "rlfProfileRef",
        "rlcSNLength",
        "pdcpSNLength",
        "inactivityTimerOffset",
        "dlMaxWaitingTime",
        "ulMaxWaitingTime",
        "pdbOffset",
        "timerPriority",
        "timerProfileRef",
        "tReorderingUl"
    FROM
    ericsson_bulkcm."vsDataQciProfilePredefined"

    """
)

QciTable = ReplaceableObject(
    'ericsson_cm_3g."QciTable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataQciTable_id"
    FROM
    ericsson_bulkcm."vsDataQciTable"

    """
)

QosAwareScheduler = ReplaceableObject(
    'ericsson_cm_3g."QosAwareScheduler"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataQosAwareScheduler_id",
        "keyIdQosAwareScheduler",
        "featureStateQosAwareScheduler",
        "licenseStateQosAwareScheduler",
        "serviceStateQosAwareScheduler"
    FROM
    ericsson_bulkcm."vsDataQosAwareScheduler"

    """
)

QoSClassifier = ReplaceableObject(
    'ericsson_cm_3g."QoSClassifier"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataQueueSystem_id",
        "vsDataQoSClassifier_id"
    FROM
    ericsson_bulkcm."vsDataQoSClassifier"

    """
)

QosPolicy = ReplaceableObject(
    'ericsson_cm_3g."QosPolicy"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataQosPolicy_id",
        "dscp2pcp0",
        "dscp2pcp1",
        "dscp2pcp2",
        "dscp2pcp3",
        "dscp2pcp4",
        "dscp2pcp5",
        "dscp2pcp6",
        "dscp2pcp7",
        "dscp2pcp8",
        "dscp2pcp9",
        "dscp2pcp10",
        "dscp2pcp11",
        "dscp2pcp12",
        "dscp2pcp13",
        "dscp2pcp14",
        "dscp2pcp15",
        "dscp2pcp16",
        "dscp2pcp17",
        "dscp2pcp18",
        "dscp2pcp19",
        "dscp2pcp20",
        "dscp2pcp21",
        "dscp2pcp22",
        "dscp2pcp23",
        "dscp2pcp24",
        "dscp2pcp25",
        "dscp2pcp26",
        "dscp2pcp27",
        "dscp2pcp28",
        "dscp2pcp29",
        "dscp2pcp30",
        "dscp2pcp31",
        "dscp2pcp32",
        "dscp2pcp33",
        "dscp2pcp34",
        "dscp2pcp35",
        "dscp2pcp36",
        "dscp2pcp37",
        "dscp2pcp38",
        "dscp2pcp39",
        "dscp2pcp40",
        "dscp2pcp41",
        "dscp2pcp42",
        "dscp2pcp43",
        "dscp2pcp44",
        "dscp2pcp45",
        "dscp2pcp46",
        "dscp2pcp47",
        "dscp2pcp48",
        "dscp2pcp49",
        "dscp2pcp50",
        "dscp2pcp51",
        "dscp2pcp52",
        "dscp2pcp53",
        "dscp2pcp54",
        "dscp2pcp55",
        "dscp2pcp56",
        "dscp2pcp57",
        "dscp2pcp58",
        "dscp2pcp59",
        "dscp2pcp60",
        "dscp2pcp61",
        "dscp2pcp62",
        "dscp2pcp63",
        "dscp2q0",
        "dscp2q1",
        "dscp2q2",
        "dscp2q3",
        "dscp2q4",
        "dscp2q5",
        "dscp2q6",
        "dscp2q7",
        "dscp2q8",
        "dscp2q9",
        "dscp2q10",
        "dscp2q11",
        "dscp2q12",
        "dscp2q13",
        "dscp2q14",
        "dscp2q15",
        "dscp2q16",
        "dscp2q17",
        "dscp2q18",
        "dscp2q19",
        "dscp2q20",
        "dscp2q21",
        "dscp2q22",
        "dscp2q23",
        "dscp2q24",
        "dscp2q25",
        "dscp2q26",
        "dscp2q27",
        "dscp2q28",
        "dscp2q29",
        "dscp2q30",
        "dscp2q31",
        "dscp2q32",
        "dscp2q33",
        "dscp2q34",
        "dscp2q35",
        "dscp2q36",
        "dscp2q37",
        "dscp2q38",
        "dscp2q39",
        "dscp2q40",
        "dscp2q41",
        "dscp2q42",
        "dscp2q43",
        "dscp2q44",
        "dscp2q45",
        "dscp2q46",
        "dscp2q47",
        "dscp2q48",
        "dscp2q49",
        "dscp2q50",
        "dscp2q51",
        "dscp2q52",
        "dscp2q53",
        "dscp2q54",
        "dscp2q55",
        "dscp2q56",
        "dscp2q57",
        "dscp2q58",
        "dscp2q59",
        "dscp2q60",
        "dscp2q61",
        "dscp2q62",
        "dscp2q63",
        "l2qosmappingtype",
        "defaultPcp",
        "pcp2q0",
        "pcp2q1",
        "pcp2q2",
        "pcp2q3",
        "pcp2q4",
        "pcp2q5",
        "pcp2q6",
        "pcp2q7"
    FROM
    ericsson_bulkcm."vsDataQosPolicy"

    """
)

QosProfiles = ReplaceableObject(
    'ericsson_cm_3g."QosProfiles"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataQosProfiles_id"
    FROM
    ericsson_bulkcm."vsDataQosProfiles"

    """
)

QuadAntUlPerfPkg = ReplaceableObject(
    'ericsson_cm_3g."QuadAntUlPerfPkg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataQuadAntUlPerfPkg_id",
        "featureStateQuadAntUlPerfPkg",
        "keyIdQuadAntUlPerfPkg",
        "licenseStateQuadAntUlPerfPkg",
        "serviceStateQuadAntUlPerfPkg"
    FROM
    ericsson_bulkcm."vsDataQuadAntUlPerfPkg"

    """
)

Queue = ReplaceableObject(
    'ericsson_cm_3g."Queue"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataTrafficScheduler_id",
        "vsDataQueue_id"
    FROM
    ericsson_bulkcm."vsDataQueue"

    """
)

QueueSystem = ReplaceableObject(
    'ericsson_cm_3g."QueueSystem"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataQueueSystem_id"
    FROM
    ericsson_bulkcm."vsDataQueueSystem"

    """
)

RabHandling = ReplaceableObject(
    'ericsson_cm_3g."RabHandling"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRabHandling_id",
        "psStreamingInactivityTimer",
        "activeQueueMgmt",
        "amrNbMmUeRelease",
        "edchTti2SpeechEnabled",
        "tnResAllocSrbHspa",
        "enhUeDrxBurstLength",
        "enhUeDrxCycleLength",
        "enhUeDrxT321",
        "srbAdmExemptRrcFiltering",
        "state128_128Supported",
        "dynamicRlcDelayHyst",
        "dynamicRlcDelayThresh",
        "dynamicRlcParamCalc",
        "dynamicRlcHarqTransBasedReord",
        "amrIratRabConfig",
        "puncturingLimitUlTti2",
        "csStreamMaxRateInit"
    FROM
    ericsson_bulkcm."vsDataRabHandling"

    """
)

Rach = ReplaceableObject(
    'ericsson_cm_3g."Rach"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "UtranCell_id",
        "vsDataRach_id",
        "userLabel",
        "scramblingCodeWordNo",
        "preambleSignatures",
        "subChannelNo",
        "aichTransmissionTiming",
        "aichPower",
        "powerOffsetP0",
        "powerOffsetPpm",
        "preambleRetransMax",
        "maxPreambleCycle",
        "constantValueCprach",
        "spreadingFactor",
        "administrativeState",
        "increasedRachCoverageEnabled",
        "nb01Max",
        "nb01Min"
    FROM
    ericsson_bulkcm."vsDataRach"

    """
)

RadioBearerTable = ReplaceableObject(
    'ericsson_cm_3g."RadioBearerTable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataRadioBearerTable_id"
    FROM
    ericsson_bulkcm."vsDataRadioBearerTable"

    """
)

RadioEquipmentClock = ReplaceableObject(
    'ericsson_cm_3g."RadioEquipmentClock"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataRadioEquipmentClock_id",
        "selectionProcessMode",
        "minQualityLevel_qualityLevelValueOptionI",
        "minQualityLevel_qualityLevelValueOptionII",
        "minQualityLevel_qualityLevelValueOptionIII",
        "equipmentClockPriorityTable",
        "clockState"
    FROM
    ericsson_bulkcm."vsDataRadioEquipmentClock"

    """
)

RadioEquipmentClockReference = ReplaceableObject(
    'ericsson_cm_3g."RadioEquipmentClockReference"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataRadioEquipmentClock_id",
        "vsDataRadioEquipmentClockReference_id",
        "referenceStatus",
        "adminQualityLevel_qualityLevelValueOptionI",
        "adminQualityLevel_qualityLevelValueOptionII",
        "adminQualityLevel_qualityLevelValueOptionIII",
        "useQLFrom",
        "availabilityStatus",
        "waitToRestoreTime",
        "priority",
        "administrativeState",
        "syncRefType",
        "holdOffTime",
        "operationalState",
        "encapsulation",
        "receivedQualityLevel"
    FROM
    ericsson_bulkcm."vsDataRadioEquipmentClockReference"

    """
)

RadioLinks = ReplaceableObject(
    'ericsson_cm_3g."RadioLinks"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataNodeBLocalCellGroup_id",
        "vsDataNodeBLocalCell_id",
        "vsDataRadioLinks_id",
        "noOfRadioLinks"
    FROM
    ericsson_bulkcm."vsDataRadioLinks"

    """
)

RadioUnitCascading = ReplaceableObject(
    'ericsson_cm_3g."RadioUnitCascading"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRadioUnitCascading_id",
        "featureStateRUCascading",
        "keyIdRUCascading",
        "licenseStateRUCascading",
        "serviceStateRUCascading"
    FROM
    ericsson_bulkcm."vsDataRadioUnitCascading"

    """
)

Ranap = ReplaceableObject(
    'ericsson_cm_3g."Ranap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCnOperator_id",
        "vsDataIuLink_id",
        "vsDataRanap_id",
        "sccpDisabledT",
        "cnDomainInd",
        "noOfResetSendings",
        "userOutOfServiceT",
        "localSccpApRef",
        "remoteSccpApRef",
        "resetResendT",
        "resetAckGuardT",
        "userLabel",
        "cnId",
        "networkResourceIdentifier",
        "relativeCapacity",
        "maxResetResourceMessageSize",
        "ranapResetResourceMonitorPeriod",
        "ranapResetResourceMonitorThresh",
        "overloadCtrlEnabled",
        "overloadCtrlSupervision_msgIntervalTimeMin",
        "overloadCtrlSupervision_reductionStepHoldTime",
        "resetResourceMsgInterval"
    FROM
    ericsson_bulkcm."vsDataRanap"

    """
)

RateShaping = ReplaceableObject(
    'ericsson_cm_3g."RateShaping"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRateShaping_id",
        "featureStateRateShaping",
        "keyIdRateShaping",
        "licenseStateRateShaping",
        "serviceStateRateShaping"
    FROM
    ericsson_bulkcm."vsDataRateShaping"

    """
)

RbsEventStreamer = ReplaceableObject(
    'ericsson_cm_3g."RbsEventStreamer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRbsEventStreamer_id",
        "keyIdEventStreaming",
        "featureStateEventStreaming",
        "licenseStateEventStreaming",
        "serviceStateEventStreaming"
    FROM
    ericsson_bulkcm."vsDataRbsEventStreamer"

    """
)

RbsLocalCell = ReplaceableObject(
    'ericsson_cm_3g."RbsLocalCell"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataRbsLocalCell_id",
        "userLabel",
        "localCellId",
        "carrierRef",
        "carriersRef",
        "hsCodeResourceId",
        "cellRange",
        "maxNumHsPdschCodes",
        "eulMaxOwnUuLoad",
        "eulMaxRotCoverage",
        "maxUserEHichERgchPowerDl",
        "eulMaxNoSchEDch",
        "eulSlidingWindowTime",
        "eulMinMarginCoverage",
        "eulOptimalNoiseFloorLock_eulNoiseFloorLock",
        "eulOptimalNoiseFloorLock_eulOptimalNoiseFloorEstimate",
        "maxEAgchPowerDl",
        "eulThermalLevelPrior",
        "eulNoERgchGroups",
        "maxNumHsdpaUsers",
        "maxDlPowerCapability",
        "rbsSynchronizationRef",
        "minSpreadingFactor",
        "minDlPowerCapability",
        "hsdpaCapability",
        "eDchCapability",
        "eDch2msTtiCapability",
        "maxEAgchPowerDlTti2",
        "maxNumEulUsers",
        "maxUserEHichPowerDlTti2",
        "eHichMinCodePower",
        "qualityCheckPowerEHich",
        "featureStateEnhancedLayer2",
        "featureStateHsdpaDynamicCodeAllocation",
        "featureStateHsdpaIncrementalRedundancy",
        "featureStateMimo",
        "featureState4wayRxDiversity",
        "featureStateHsdpaMc",
        "featureStateHsdpaMcInactCtrl",
        "hsdpaMcCapability",
        "featureStateFDpchSrbOnHsdpa",
        "fDpchCapability",
        "featureStateCpc",
        "cpcCapability",
        "featureState64QamMimo",
        "ocnsIsActive",
        "ocnsIsConfigured",
        "featureStateHsdpaDbMc",
        "featureStateHsFach",
        "hsdpaDbMcCapability",
        "hsdpaMcMimoCapability",
        "featureStateHsdpaMcMimo",
        "featureStateDchEulBalancing",
        "featureStateEnhUeDrx",
        "eulMaxTdUsers",
        "eulTdSchedulingFactor",
        "featureStateEulTdScheduling",
        "featureStateImprovedLayer2",
        "fccRotMarginHigh",
        "fccRotMarginLow",
        "eulFachMaxDcchDtchTime",
        "eulFachNumOfDecoders",
        "featureStateEulFach",
        "airRateTypeSelector",
        "chQualOffset",
        "cqiAdjustmentOn",
        "cqiErrors",
        "cqiErrorsAbsent",
        "defaultCqiHsFach",
        "eulMcCapability",
        "extraCompEnhUeDrx",
        "extraCompForSigHsFach",
        "extraCompHsFach",
        "extraHsScchCompEnhUeDrx",
        "extraHsScchCompForSigHsFach",
        "extraHsScchCompHsFach",
        "extraHsScchPowerForSrbOnHsdpa",
        "extraPowerForSrbOnHsdpa",
        "featureStateEulMc",
        "hsdpaMcActivityBufferThreshold",
        "hsdpaMcInactivityTimer",
        "hsPowerMargin",
        "hsScchMaxCodePower",
        "hsScchMinCodePower",
        "minBitRate",
        "minBitRateMinCqi",
        "qualityCheckPower",
        "queueSelectAlgorithm",
        "schCongPeriodGbr",
        "schCongThreshGbr",
        "schCongThreshNonGbr",
        "schMaxDelay",
        "schMinPowerNonGbrHsUsers",
        "schNoCongPeriodGbr",
        "schNoCongThreshGbr",
        "schPowerDeltaCongGbr",
        "schPrioForAbsResSharing",
        "schWeight",
        "throughputPqxHsFach",
        "featureStateHsOlpc",
        "featureStateHsdpaPowerSharing",
        "powerSharingMaxTransmissionPower",
        "hsdpaPowerSharingCapability",
        "featureStateNbir",
        "eulMcActivationDelayTime",
        "hsdpaDb3McCapability",
        "hsdpa3McCapability",
        "featureStateHsdpa3Mc",
        "featureStateHsdpaDb3Mc",
        "mixedCellType",
        "featureStateHsAdaptiveBler",
        "featureStateHsdpaMixedModePowerSharing",
        "trafficAwarePwrSaveRadioRebiasing",
        "hsdpaMixedModePowerSharingCapability"
    FROM
    ericsson_bulkcm."vsDataRbsLocalCell"

    """
)

RbsMeasControl = ReplaceableObject(
    'ericsson_cm_3g."RbsMeasControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRbsMeasControl_id",
        "dlCodePwrThreshCmStopHsFdpch",
        "dlCodePwrThreshCmStartHsDpch",
        "dlCodePwrCmFilterCoeffHsDpch",
        "dlCodePwrThreshCmStopHsDpch",
        "dlCodePwrThreshCmStopDch",
        "dlCodePwrTimeTriggMeasDch",
        "dlCodePwrCmFilterCoeffDch",
        "dlCodePwrTimeTriggMeasHsDpch",
        "dlCodePwrRelThreshRscp",
        "dlCodePwrThreshCmStartHsFdpch",
        "dlCodePwrThreshCmStartDch",
        "dlCodePwrTimeTriggMeasHsFdpch",
        "dlCodePwrCmFilterCoeffHsFdpch"
    FROM
    ericsson_bulkcm."vsDataRbsMeasControl"

    """
)

RbsSlot = ReplaceableObject(
    'ericsson_cm_3g."RbsSlot"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id"
    FROM
    ericsson_bulkcm."vsDataRbsSlot"

    """
)

RbsSubrack = ReplaceableObject(
    'ericsson_cm_3g."RbsSubrack"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataRbsSubrack_id",
        "cabinetPosition",
        "noOfSlots",
        "subrackPosition"
    FROM
    ericsson_bulkcm."vsDataRbsSubrack"

    """
)

RbsSynchronization = ReplaceableObject(
    'ericsson_cm_3g."RbsSynchronization"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataRbsSynchronization_id",
        "plugInUnitRef1",
        "plugInUnitRef2",
        "timDeviceRef2",
        "timDeviceRef1",
        "masterTu"
    FROM
    ericsson_bulkcm."vsDataRbsSynchronization"

    """
)

RbsUnit = ReplaceableObject(
    'ericsson_cm_3g."RbsUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataRbsUnit_id",
        "productCode"
    FROM
    ericsson_bulkcm."vsDataRbsUnit"

    """
)

Rcs = ReplaceableObject(
    'ericsson_cm_3g."Rcs"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataRcs_id",
        "RncFunction_id",
        "tInactivityTimer",
        "rlcDlDeliveryFailureAction",
        "dchRcLostT",
        "cchWaitCuT",
        "hsDschRcLostT"
    FROM
    ericsson_bulkcm."vsDataRcs"

    """
)

RdiPort = ReplaceableObject(
    'ericsson_cm_3g."RdiPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRdiPort_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "availabilityStatus",
        "operationalState",
        "remoteRdiPortRef",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataRdiPort"

    """
)

RealTimeSecLog = ReplaceableObject(
    'ericsson_cm_3g."RealTimeSecLog"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecurity_id",
        "vsDataRealTimeSecLog_id",
        "connAttemptTimeOut",
        "extServerAppName",
        "extServerListConfig",
        "extServerLogLevel",
        "featureState",
        "licenseState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataRealTimeSecLog"

    """
)

RedirectWithNacc = ReplaceableObject(
    'ericsson_cm_3g."RedirectWithNacc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRedirectWithNacc_id",
        "featureStateRedirectWithNacc",
        "keyIdRedirectWithNacc",
        "licenseStateRedirectWithNacc",
        "serviceStateRedirectWithNacc"
    FROM
    ericsson_bulkcm."vsDataRedirectWithNacc"

    """
)

ReliableProgramUniter = ReplaceableObject(
    'ericsson_cm_3g."ReliableProgramUniter"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSwManagement_id",
        "vsDataReliableProgramUniter_id",
        "userLabel",
        "reliableProgramLabel",
        "admActiveSlot",
        "admPassiveSlot",
        "switchOver",
        "normalisation",
        "replication"
    FROM
    ericsson_bulkcm."vsDataReliableProgramUniter"

    """
)

ReportConfigA1 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA1_id",
        "timeToTriggerA1",
        "a1ThresholdRsrq",
        "a1ThresholdRsrp",
        "hysteresisA1"
    FROM
    ericsson_bulkcm."vsDataReportConfigA1"

    """
)

ReportConfigA1Prim = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA1Prim"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA1Prim_id",
        "a1ThresholdRsrpPrim",
        "a1ThresholdRsrqPrim",
        "hysteresisA1Prim",
        "timeToTriggerA1Prim"
    FROM
    ericsson_bulkcm."vsDataReportConfigA1Prim"

    """
)

ReportConfigA1Sec = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA1Sec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA1Sec_id",
        "a1ThresholdRsrpSec",
        "a1ThresholdRsrqSec",
        "hysteresisA1Sec",
        "timeToTriggerA1Sec"
    FROM
    ericsson_bulkcm."vsDataReportConfigA1Sec"

    """
)

ReportConfigA4 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA4"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA4_id",
        "a4ThresholdRsrp",
        "a4ThresholdRsrq",
        "hysteresisA4",
        "timeToTriggerA4",
        "triggerQuantityA4"
    FROM
    ericsson_bulkcm."vsDataReportConfigA4"

    """
)

ReportConfigA5 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA5"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA5_id",
        "a5Threshold1Rsrp",
        "a5Threshold1Rsrq",
        "a5Threshold2Rsrp",
        "a5Threshold2Rsrq",
        "hysteresisA5",
        "timeToTriggerA5",
        "triggerQuantityA5",
        "hysteresisA5RsrqOffset",
        "timeToTriggerA5Rsrq"
    FROM
    ericsson_bulkcm."vsDataReportConfigA5"

    """
)

ReportConfigA5Anr = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA5Anr"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA5_id",
        "vsDataReportConfigA5Anr_id",
        "a5Threshold1RsrpAnrDelta",
        "a5Threshold1RsrqAnrDelta",
        "a5Threshold2RsrpAnrDelta",
        "a5Threshold2RsrqAnrDelta",
        "hysteresisA5",
        "timeToTriggerA5"
    FROM
    ericsson_bulkcm."vsDataReportConfigA5Anr"

    """
)

ReportConfigA5DlComp = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA5DlComp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA5DlComp_id"
    FROM
    ericsson_bulkcm."vsDataReportConfigA5DlComp"

    """
)

ReportConfigA5SoftLock = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA5SoftLock"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA5SoftLock_id",
        "a5Threshold2Rsrp"
    FROM
    ericsson_bulkcm."vsDataReportConfigA5SoftLock"

    """
)

ReportConfigA5UlTrig = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigA5UlTrig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigA5UlTrig_id",
        "timeToTriggerA5",
        "hysteresisA5",
        "a5Threshold2Rsrp",
        "reportIntervalA5"
    FROM
    ericsson_bulkcm."vsDataReportConfigA5UlTrig"

    """
)

ReportConfigB1Geran = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB1Geran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB1Geran_id",
        "b1ThresholdGeran",
        "hysteresisB1",
        "timeToTriggerB1"
    FROM
    ericsson_bulkcm."vsDataReportConfigB1Geran"

    """
)

ReportConfigB1Utra = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB1Utra"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB1Utra_id",
        "b1ThresholdEcNoUtra",
        "hysteresisB1",
        "timeToTriggerB1",
        "b1ThresholdRscpUtra"
    FROM
    ericsson_bulkcm."vsDataReportConfigB1Utra"

    """
)

ReportConfigB2Cdma2000 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2Cdma2000"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2Cdma2000_id",
        "b2Threshold1Rsrp",
        "b2Threshold1Rsrq",
        "b2Threshold2Cdma2000",
        "hysteresisB2",
        "timeToTriggerB2",
        "triggerQuantityB2",
        "timeToTriggerB2Rsrq",
        "hysteresisB2RsrqOffset"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2Cdma2000"

    """
)

ReportConfigB2Cdma20001xRtt = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2Cdma20001xRtt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2Cdma20001xRtt_id",
        "b2Threshold1Rsrq",
        "b2Threshold1Rsrp",
        "b2Threshold2Cdma20001xRtt",
        "timeToTriggerB2",
        "hysteresisB2",
        "triggerQuantityB2",
        "timeToTriggerB2Rsrq",
        "hysteresisB2RsrqOffset"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2Cdma20001xRtt"

    """
)

ReportConfigB2CdmaRttUlTrig = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2CdmaRttUlTrig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2CdmaRttUlTrig_id",
        "b2Threshold2Cdma20001xRtt",
        "timeToTriggerB2",
        "reportIntervalB2",
        "hysteresisB2"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2CdmaRttUlTrig"

    """
)

ReportConfigB2CdmaUlTrig = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2CdmaUlTrig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2CdmaUlTrig_id",
        "b2Threshold2Cdma2000",
        "timeToTriggerB2",
        "reportIntervalB2",
        "hysteresisB2"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2CdmaUlTrig"

    """
)

ReportConfigB2Geran = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2Geran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2Geran_id",
        "b2Threshold1Rsrp",
        "b2Threshold1Rsrq",
        "b2Threshold2Geran",
        "hysteresisB2",
        "timeToTriggerB2",
        "triggerQuantityB2",
        "timeToTriggerB2Rsrq",
        "hysteresisB2RsrqOffset"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2Geran"

    """
)

ReportConfigB2GeranUlTrig = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2GeranUlTrig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2GeranUlTrig_id",
        "b2Threshold2Geran",
        "timeToTriggerB2",
        "reportIntervalB2",
        "hysteresisB2"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2GeranUlTrig"

    """
)

ReportConfigB2Utra = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2Utra"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2Utra_id",
        "b2Threshold1Rsrp",
        "b2Threshold1Rsrq",
        "b2Threshold2EcNoUtra",
        "b2Threshold2RscpUtra",
        "hysteresisB2",
        "timeToTriggerB2",
        "triggerQuantityB2",
        "timeToTriggerB2Rsrq",
        "hysteresisB2RsrqOffset"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2Utra"

    """
)

ReportConfigB2UtraUlTrig = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigB2UtraUlTrig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigB2UtraUlTrig_id",
        "b2Threshold2EcNoUtra",
        "b2Threshold2RscpUtra",
        "timeToTriggerB2",
        "reportIntervalB2",
        "hysteresisB2"
    FROM
    ericsson_bulkcm."vsDataReportConfigB2UtraUlTrig"

    """
)

ReportConfigCsfbCdma2000 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigCsfbCdma2000"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigCsfbCdma2000_id",
        "hysteresis",
        "thresholdCdma20001xRtt",
        "timeToTrigger"
    FROM
    ericsson_bulkcm."vsDataReportConfigCsfbCdma2000"

    """
)

ReportConfigCsfbGeran = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigCsfbGeran"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigCsfbGeran_id",
        "thresholdGeran",
        "hysteresis",
        "timeToTrigger"
    FROM
    ericsson_bulkcm."vsDataReportConfigCsfbGeran"

    """
)

ReportConfigCsfbUtra = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigCsfbUtra"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigCsfbUtra_id",
        "hysteresis",
        "thresholdRscp",
        "thresholdEcNo",
        "timeToTrigger"
    FROM
    ericsson_bulkcm."vsDataReportConfigCsfbUtra"

    """
)

ReportConfigCsg = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigCsg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigCsg_id",
        "hysteresisA5AltCsg",
        "a5Thr1RsrpAltCsgOffset",
        "a5Thr2RsrpAltCsgOffset",
        "timeToTriggerA5AltCsg"
    FROM
    ericsson_bulkcm."vsDataReportConfigCsg"

    """
)

ReportConfigEUtraBadCovPrim = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraBadCovPrim"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraBadCovPrim_id",
        "a2ThresholdRsrpPrim",
        "a2ThresholdRsrqPrim",
        "hysteresisA2Prim",
        "timeToTriggerA2Prim",
        "triggerQuantityA2Prim"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraBadCovPrim"

    """
)

ReportConfigEUtraBadCovSec = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraBadCovSec"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraBadCovSec_id",
        "a2ThresholdRsrpSec",
        "a2ThresholdRsrqSec",
        "hysteresisA2Sec",
        "timeToTriggerA2Sec",
        "triggerQuantityA2Sec"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraBadCovSec"

    """
)

ReportConfigEUtraBestCell = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraBestCell"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraBestCell_id",
        "a3offset",
        "hysteresisA3",
        "timeToTriggerA3",
        "triggerQuantityA3"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraBestCell"

    """
)

ReportConfigEUtraBestCellAnr = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraBestCellAnr"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraBestCell_id",
        "vsDataReportConfigEUtraBestCellAnr_id",
        "a3offsetAnrDelta",
        "hysteresisA3",
        "timeToTriggerA3"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraBestCellAnr"

    """
)

ReportConfigEUtraIFA3UlTrig = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraIFA3UlTrig"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraIFA3UlTrig_id",
        "hysteresisA3",
        "timeToTriggerA3",
        "reportIntervalA3",
        "a3Offset"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraIFA3UlTrig"

    """
)

ReportConfigEUtraIFBestCell = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraIFBestCell"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraIFBestCell_id",
        "a3offset",
        "hysteresisA3",
        "timeToTriggerA3",
        "triggerQuantityA3",
        "timeToTriggerA3Rsrq",
        "hysteresisA3RsrqOffset",
        "a3RsrqOffset"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraIFBestCell"

    """
)

ReportConfigEUtraInterFreqLb = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraInterFreqLb"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraInterFreqLb_id",
        "hysteresisA5",
        "a5Threshold2Rsrp",
        "a5Threshold2Rsrq",
        "a5Threshold1Rsrp",
        "a4ThresholdRsrp",
        "hysteresisA4"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraInterFreqLb"

    """
)

ReportConfigEUtraInterFreqMbms = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraInterFreqMbms"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraInterFreqMbms_id",
        "hysteresisA5",
        "a5ThresholdRsrp"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraInterFreqMbms"

    """
)

ReportConfigEUtraIntraFreqPm = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigEUtraIntraFreqPm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigEUtraIntraFreqPm_id",
        "a1ThresholdRsrpPm",
        "a1ThresholdRsrqPm",
        "a2ThresholdRsrpPm",
        "a2ThresholdRsrqPm",
        "a3OffsetPm",
        "a3ReportOnLeavePm",
        "a4ThresholdRsrpPm",
        "a4ThresholdRsrqPm",
        "a5ThresholdRsrpPm1",
        "a5ThresholdRsrpPm2",
        "a5ThresholdRsrqPm1",
        "a5ThresholdRsrqPm2",
        "hysteresisPm",
        "maxReportCellsPm",
        "measSelectionEUtraPm",
        "reportAmountPm",
        "reportIntervalPm",
        "reportQuantityPm",
        "timeToTriggerPm",
        "triggerQuantityPm"
    FROM
    ericsson_bulkcm."vsDataReportConfigEUtraIntraFreqPm"

    """
)

ReportConfigInterRatLb = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigInterRatLb"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigInterRatLb_id",
        "utranB1ThresholdRscp",
        "utranHysteresisB1",
        "utranB1ThresholdEcNo"
    FROM
    ericsson_bulkcm."vsDataReportConfigInterRatLb"

    """
)

ReportConfigSCellA1A2 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigSCellA1A2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigSCellA1A2_id",
        "hysteresisA1A2Rsrq",
        "timeToTriggerA1",
        "timeToTriggerA2",
        "hysteresisA1A2Rsrp",
        "a1a2ThresholdRsrp",
        "a1a2ThresholdRsrq",
        "triggerQuantityA1A2"
    FROM
    ericsson_bulkcm."vsDataReportConfigSCellA1A2"

    """
)

ReportConfigSCellA4 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigSCellA4"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigSCellA4_id",
        "hysteresisA4",
        "a4ThresholdRsrq",
        "timeToTriggerA4",
        "a4ThresholdRsrp",
        "triggerQuantityA4"
    FROM
    ericsson_bulkcm."vsDataReportConfigSCellA4"

    """
)

ReportConfigSCellA6 = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigSCellA6"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigSCellA6_id",
        "timeToTriggerA6",
        "triggerQuantityA6",
        "hysteresisA6",
        "a6offset"
    FROM
    ericsson_bulkcm."vsDataReportConfigSCellA6"

    """
)

ReportConfigSearch = ReplaceableObject(
    'ericsson_cm_3g."ReportConfigSearch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "vsDataReportConfigSearch_id",
        "a1a2SearchThresholdRsrp",
        "a1a2SearchThresholdRsrq",
        "a2CriticalThresholdRsrp",
        "a2CriticalThresholdRsrq",
        "hysteresisA1A2SearchRsrp",
        "hysteresisA1A2SearchRsrq",
        "hysteresisA2CriticalRsrp",
        "hysteresisA2CriticalRsrq",
        "timeToTriggerA1Search",
        "timeToTriggerA2Critical",
        "timeToTriggerA2Search",
        "qciA1A2ThrOffsets",
        "timeToTriggerA2CriticalRsrq",
        "timeToTriggerA2OutSearchRsrq",
        "hysteresisA2OuterSearchRsrq",
        "hysteresisA2OuterSearchRsrp",
        "a2CriticalThrQci1RsrpOffset",
        "a2OuterSearchThrRsrqOffset",
        "timeToTriggerA2OutSearch",
        "inhibitA2SearchConfig",
        "timeToTriggerA1SearchRsrq",
        "timeToTriggerA2SearchRsrq",
        "a2OuterSearchThrRsrpOffset",
        "a2CriticalThrQci1RsrqOffset",
        "qciA1A2UlThrOffsets",
        "hysteresisA2UlCritical",
        "timeToTriggerA2UlCritical",
        "a1a2UlSearchThreshold",
        "hysteresisA1A2UlSearch",
        "timeToTriggerA1UlSearch",
        "a2UlCriticalThreshold",
        "timeToTriggerA2UlSearch",
        "qciA1A2ThrOffsets_qciProfileRef",
        "qciA1A2ThrOffsets_a1a2ThrRsrpQciOffset",
        "qciA1A2ThrOffsets_a1a2ThrRsrqQciOffset"
    FROM
    ericsson_bulkcm."vsDataReportConfigSearch"

    """
)

ResMeasControl = ReplaceableObject(
    'ericsson_cm_3g."ResMeasControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataResMeasControl_id",
        "resMeasure1_service",
        "resMeasure1_rmq",
        "resMeasure2_service",
        "resMeasure2_rmq",
        "resMeasure3_service",
        "resMeasure3_rmq",
        "resMeasure4_service",
        "resMeasure4_rmq",
        "resMeasure5_service",
        "resMeasure5_rmq",
        "resMeasure6_service",
        "resMeasure6_rmq",
        "resMeasPeriodSpeech",
        "resMeasPeriodStreaming",
        "resMeasPeriodVideo",
        "resMeasPeriodInteractive",
        "resUeFraction",
        "resMeasure7_service",
        "resMeasure7_rmq",
        "resMeasure8_service",
        "resMeasure8_rmq",
        "resMeasure9_service",
        "resMeasure9_rmq",
        "resMeasure10_service",
        "resMeasure10_rmq",
        "resMeasure11_service",
        "resMeasure11_rmq",
        "resMeasure12_service",
        "resMeasure12_rmq"
    FROM
    ericsson_bulkcm."vsDataResMeasControl"

    """
)

ResourcePartitions = ReplaceableObject(
    'ericsson_cm_3g."ResourcePartitions"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataResourcePartitions_id"
    FROM
    ericsson_bulkcm."vsDataResourcePartitions"

    """
)

RetCascading = ReplaceableObject(
    'ericsson_cm_3g."RetCascading"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRetCascading_id",
        "keyIdRetCascading",
        "featureStateRetCascading",
        "licenseStateRetCascading",
        "serviceStateRetCascading"
    FROM
    ericsson_bulkcm."vsDataRetCascading"

    """
)

RetConfigurationMgt = ReplaceableObject(
    'ericsson_cm_3g."RetConfigurationMgt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRetConfigurationMgt_id",
        "keyIdRetConfigurationMgt",
        "featureStateRetConfigurationMgt",
        "licenseStateRetConfigurationMgt",
        "serviceStateRetConfigurationMgt"
    FROM
    ericsson_bulkcm."vsDataRetConfigurationMgt"

    """
)

RetDevice = ReplaceableObject(
    'ericsson_cm_3g."RetDevice"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRetuDeviceGroup_id",
        "vsDataRetDeviceSet_id",
        "vsDataRetDevice_id",
        "electricalAntennaTilt",
        "maxTilt",
        "minTilt",
        "userLabel",
        "aretDeviceData_antennaModelNumber",
        "aretDeviceData_antennaSerialNumber",
        "aretDeviceData_antennaOperatingBand",
        "aretDeviceData_beamwidthForBands",
        "aretDeviceData_gainForBands",
        "aretDeviceData_maxSupportedElectricalTilt",
        "aretDeviceData_installationDate",
        "aretDeviceData_installersId",
        "aretDeviceData_baseStationId",
        "aretDeviceData_sectorId",
        "aretDeviceData_antennaBearing",
        "aretDeviceData_installedMechTilt",
        "aretDeviceData_minSupportedElectricalTilt"
    FROM
    ericsson_bulkcm."vsDataRetDevice"

    """
)

RetDeviceSet = ReplaceableObject(
    'ericsson_cm_3g."RetDeviceSet"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRetuDeviceGroup_id",
        "vsDataRetDeviceSet_id",
        "productNumber",
        "revState",
        "retType"
    FROM
    ericsson_bulkcm."vsDataRetDeviceSet"

    """
)

RetSubUnit = ReplaceableObject(
    'ericsson_cm_3g."RetSubUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "vsDataAntennaNearUnit_id",
        "vsDataRetSubUnit_id",
        "iuantBaseStationId",
        "iuantInstallationDate",
        "iuantAntennaOperatingGain",
        "iuantAntennaSerialNumber",
        "electricalAntennaTilt",
        "subunitNumber",
        "iuantSectorId",
        "userLabel",
        "minTilt",
        "iuantAntennaOperatingBand",
        "iuantAntennaModelNumber",
        "maxTilt",
        "iuantAntennaBearing",
        "iuantInstallersId"
    FROM
    ericsson_bulkcm."vsDataRetSubUnit"

    """
)

RetSupport = ReplaceableObject(
    'ericsson_cm_3g."RetSupport"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRetSupport_id",
        "keyIdRetSupport",
        "featureStateRetSupport",
        "licenseStateRetSupport",
        "serviceStateRetSupport"
    FROM
    ericsson_bulkcm."vsDataRetSupport"

    """
)

RetuDeviceGroup = ReplaceableObject(
    'ericsson_cm_3g."RetuDeviceGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRetuDeviceGroup_id",
        "hwTestResult"
    FROM
    ericsson_bulkcm."vsDataRetuDeviceGroup"

    """
)

RfBranch = ReplaceableObject(
    'ericsson_cm_3g."RfBranch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAntennaUnitGroup_id",
        "vsDataRfBranch_id",
        "auPortRef",
        "dlAttenuation",
        "dlTrafficDelay",
        "tmaRef",
        "ulAttenuation",
        "ulTrafficDelay",
        "userLabel",
        "rfPortRef"
    FROM
    ericsson_bulkcm."vsDataRfBranch"

    """
)

RfPort = ReplaceableObject(
    'ericsson_cm_3g."RfPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataDeviceGroup_id",
        "vsDataRfPort_id",
        "vsDataFieldReplaceableUnit_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "administrativeState",
        "vswrSupervisionActive",
        "vswrSupervisionSensitivity",
        "userLabel",
        "ulFrequencyRanges",
        "dlFrequencyRanges",
        "nodeUniqueRfPortId"
    FROM
    ericsson_bulkcm."vsDataRfPort"

    """
)

RiLink = ReplaceableObject(
    'ericsson_cm_3g."RiLink"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataRiLink_id",
        "riPortRef1",
        "riPortRef2",
        "availabilityStatus",
        "operationalState",
        "linkTag",
        "transportType",
        "linkType"
    FROM
    ericsson_bulkcm."vsDataRiLink"

    """
)

RiPort = ReplaceableObject(
    'ericsson_cm_3g."RiPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRiPort_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataFieldReplaceableUnit_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "sfpData_manufacturerId",
        "sfpData_productNumber",
        "sfpData_productionDate",
        "sfpData_serialNumber",
        "sfpData_manufacturerDesignation",
        "sfpData_productRevision",
        "sfpData_negotiatedBitRate",
        "sfpData_manufacturerRevision",
        "sfpData"
    FROM
    ericsson_bulkcm."vsDataRiPort"

    """
)

RlcUm = ReplaceableObject(
    'ericsson_cm_3g."RlcUm"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRlcUm_id",
        "keyIdRlcUm",
        "featureStateRlcUm",
        "licenseStateRlcUm",
        "serviceStateRlcUm"
    FROM
    ericsson_bulkcm."vsDataRlcUm"

    """
)

RlfProfile = ReplaceableObject(
    'ericsson_cm_3g."RlfProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataRlfProfile_id",
        "t301",
        "n311",
        "n310",
        "reservedBy",
        "t310",
        "t311"
    FROM
    ericsson_bulkcm."vsDataRlfProfile"

    """
)

RncCapacity = ReplaceableObject(
    'ericsson_cm_3g."RncCapacity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataRncCapacity_id",
        "licensedCapacityLimit_noLimit",
        "licensedCapacityLimit_value",
        "keyId",
        "isLicensedControlled",
        "operatorCapacityLimit_noLimit",
        "operatorCapacityLimit_value",
        "currentCapacityLimit_noLimit",
        "currentCapacityLimit_value",
        "capacityUnit",
        "gracePeriod_isGracePeriodControlled",
        "gracePeriod_state",
        "gracePeriod_startDate",
        "gracePeriod_endDate",
        "length",
        "startLimit",
        "hwacCapabilityLimit_noLimit",
        "hwacCapabilityLimit_value",
        "minHwacLicensedLimit_noLimit",
        "minHwacLicensedLimit_value",
        "hwacKeyId"
    FROM
    ericsson_bulkcm."vsDataRncCapacity"

    """
)

RncConfigLimits = ReplaceableObject(
    'ericsson_cm_3g."RncConfigLimits"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRncConfigLimits_id",
        "ccDevicesLimit",
        "cellRelationsLimit",
        "dcDevicesLimit",
        "externalGsmCellsLimit",
        "externalUtranCellsLimit",
        "iubLinksLimit",
        "locationAreasLimit",
        "packetDataRoutersLimit",
        "pdrDevicesLimit",
        "rncModulesLimit",
        "routingAreasLimit",
        "serviceAreasLimit",
        "urasLimit",
        "utranCellsLimit"
    FROM
    ericsson_bulkcm."vsDataRncConfigLimits"

    """
)

RncFeature = ReplaceableObject(
    'ericsson_cm_3g."RncFeature"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataRncFeature_id",
        "featureState",
        "licenseState",
        "serviceState",
        "keyId",
        "isLicenseControlled",
        "reservedBy"
    FROM
    ericsson_bulkcm."vsDataRncFeature"

    """
)

RncModule = ReplaceableObject(
    'ericsson_cm_3g."RncModule"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRncModule_id",
        "userLabel",
        "programInstanceId",
        "supportedIubLinkType"
    FROM
    ericsson_bulkcm."vsDataRncModule"

    """
)

RnlQosClassProfile = ReplaceableObject(
    'ericsson_cm_3g."RnlQosClassProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCnOperator_id",
        "vsDataRnlQosClassProfile_id",
        "vsDataRabHandling_id",
        "tcPsBgQosRef",
        "userLabel",
        "tcPsBgArpSpiMapRef",
        "hsFachQueueSpi"
    FROM
    ericsson_bulkcm."vsDataRnlQosClassProfile"

    """
)

Rnsap = ReplaceableObject(
    'ericsson_cm_3g."Rnsap"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIurLink_id",
        "vsDataRnsap_id",
        "sccpDisabledT",
        "userOutOfServiceT",
        "localSccpApRef",
        "remoteSccpApRef",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataRnsap"

    """
)

ROHC = ReplaceableObject(
    'ericsson_cm_3g."ROHC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataROHC_id",
        "featureStateROHC",
        "keyIdROHC",
        "licenseStateROHC",
        "serviceStateROHC"
    FROM
    ericsson_bulkcm."vsDataROHC"

    """
)

Router = ReplaceableObject(
    'ericsson_cm_3g."Router"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataRouter_id",
        "ttl",
        "userLabel",
        "hopLimit"
    FROM
    ericsson_bulkcm."vsDataRouter"

    """
)

RouteTableIPv4Static = ReplaceableObject(
    'ericsson_cm_3g."RouteTableIPv4Static"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataRouter_id",
        "vsDataRouteTableIPv4Static_id",
        "vsDataHost_id"
    FROM
    ericsson_bulkcm."vsDataRouteTableIPv4Static"

    """
)

RoutingArea = ReplaceableObject(
    'ericsson_cm_3g."RoutingArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataAreas_id",
        "vsDataPlmn_id",
        "vsDataLocationArea_id",
        "vsDataRoutingArea_id",
        "userLabel",
        "rac",
        "nmo"
    FROM
    ericsson_bulkcm."vsDataRoutingArea"

    """
)

RoutingTable = ReplaceableObject(
    'ericsson_cm_3g."RoutingTable"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataRoutingTable_id"
    FROM
    ericsson_bulkcm."vsDataRoutingTable"

    """
)

Rps = ReplaceableObject(
    'ericsson_cm_3g."Rps"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataRps_id",
        "featureStateRps",
        "keyIdRps",
        "licenseStateRps",
        "serviceStateRps"
    FROM
    ericsson_bulkcm."vsDataRps"

    """
)

Rrc = ReplaceableObject(
    'ericsson_cm_3g."Rrc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataRrc_id",
        "RncFunction_id",
        "t300",
        "t301",
        "t304",
        "t320",
        "t311",
        "tRrcConnReest",
        "tWaitForRrcConnReest",
        "tRrcConnectionReconfiguration",
        "t305",
        "cfnOffsetMarginFirstRabEst",
        "cfnOffsetMarginSrbDchDl",
        "cfnOffsetMarginSrbHs",
        "rrcLcFilterDecr",
        "rrcLcFilterDecrThresh",
        "rrcLcFilterIncr",
        "rrcLcFilterIncrThresh",
        "rrcLcFilterMax",
        "rrcLcMonitorPeriod",
        "rrcLcRrcReqMin",
        "cfnOffsetMarginFirstRabEstSrbHs",
        "cfnOffsetMarginSrbDchDlCmStart",
        "cfnOffsetMarginSrbHsCmStart",
        "t323",
        "cfnOffsetMarginSrbDchDlCmStop",
        "cfnOffsetMarginSrbHsCmStop",
        "dchNonSynchReconfTime",
        "dchSynchReconfTime",
        "fachReconfTime",
        "n313",
        "n315",
        "rncMaxDatMarginCallReest",
        "rrcConnSetupTime",
        "t313",
        "t314",
        "t315",
        "highPrioProfileCustom1",
        "highPrioProfileCustom2",
        "highPrioProfileCustom3",
        "highPrioProfileSpeechOnly",
        "highPrioProfileSpeechSms",
        "highPrioProfileSpeechSmsNas",
        "rrcEarlyRejectAlarmHyst",
        "rrcEarlyRejectAlarmTriggThresh",
        "cfnOffsetMarginSrbDchDlInIratHo",
        "rrcLengthOptimizationSpeech",
        "rncRrcLcMonitorPeriod"
    FROM
    ericsson_bulkcm."vsDataRrc"

    """
)

RruDeviceGroup = ReplaceableObject(
    'ericsson_cm_3g."RruDeviceGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRruDeviceGroup_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id"
    FROM
    ericsson_bulkcm."vsDataRruDeviceGroup"

    """
)

RttPositioning = ReplaceableObject(
    'ericsson_cm_3g."RttPositioning"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUePositioning_id",
        "vsDataRttPositioning_id",
        "posQualities_responseTimeTypical",
        "posQualities_accuracyCodeTypical",
        "posQualities_verticalAccuracyCodeTypical",
        "posQualities_confidenceEstimate",
        "measTimeMaxUe",
        "measTimeMaxRbs",
        "propagationTimeUncertainty",
        "outlierFactor"
    FROM
    ericsson_bulkcm."vsDataRttPositioning"

    """
)

S1HODataFwd = ReplaceableObject(
    'ericsson_cm_3g."S1HODataFwd"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataS1HODataFwd_id",
        "featureStateS1HODataFwd",
        "keyIdS1HODataFwd",
        "licenseStateS1HODataFwd",
        "serviceStateS1HODataFwd"
    FROM
    ericsson_bulkcm."vsDataS1HODataFwd"

    """
)

SasPositioning = ReplaceableObject(
    'ericsson_cm_3g."SasPositioning"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSasPositioning_id",
        "enabledSasFeatures",
        "pcapSasRespTime"
    FROM
    ericsson_bulkcm."vsDataSasPositioning"

    """
)

SccpApLocal = ReplaceableObject(
    'ericsson_cm_3g."SccpApLocal"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataSccpSp_id",
        "vsDataSccpScrc_id",
        "vsDataSccpApLocal_id",
        "userLabel",
        "ssN",
        "maxConn",
        "useS1",
        "enablePoolProxyExtension"
    FROM
    ericsson_bulkcm."vsDataSccpApLocal"

    """
)

SccpApRemote = ReplaceableObject(
    'ericsson_cm_3g."SccpApRemote"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataSccpSp_id",
        "vsDataSccpScrc_id",
        "vsDataSccpApRemote_id",
        "userLabel",
        "mtp3bApId",
        "ssN",
        "longClSegments",
        "clSegmentationLimit"
    FROM
    ericsson_bulkcm."vsDataSccpApRemote"

    """
)

SccpScrc = ReplaceableObject(
    'ericsson_cm_3g."SccpScrc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataSccpSp_id",
        "vsDataSccpScrc_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSccpScrc"

    """
)

SccpSp = ReplaceableObject(
    'ericsson_cm_3g."SccpSp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataSccpSp_id",
        "userLabel",
        "mtp3bSpId",
        "prioSST",
        "prioIT",
        "prioRLSD",
        "prioGeneral",
        "upperConnThres",
        "lowerConnThres",
        "swapUDTPointer",
        "hopCounterSclc",
        "hopCounterScoc",
        "tconnEst",
        "tIas",
        "tIar",
        "tRel",
        "tCong",
        "tStatInfo",
        "tconnResp",
        "tReass",
        "smiValue",
        "useSCMG_sendSST",
        "useSCMG_sendSSA",
        "useSCMG_sendSSP",
        "useSCMG_useSST",
        "useSCMG_allowRemoteBroadcast",
        "useSCMG_initiateTimerTcon"
    FROM
    ericsson_bulkcm."vsDataSccpSp"

    """
)

SchedulerSp = ReplaceableObject(
    'ericsson_cm_3g."SchedulerSp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataQueueSystem_id",
        "vsDataShaper_id",
        "vsDataSchedulerSp_id",
        "order",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSchedulerSp"

    """
)

Schema = ReplaceableObject(
    'ericsson_cm_3g."Schema"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataSchema_id",
        "baseModelIdentifier",
        "baseModelVersion",
        "identifier",
        "version",
        "selectedModelOptions",
        "mirrorMIBversion",
        "neToMirrorMIBInfo"
    FROM
    ericsson_bulkcm."vsDataSchema"

    """
)

Sctp = ReplaceableObject(
    'ericsson_cm_3g."Sctp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataSctp_id",
        "vsDataTransport_id",
        "userLabel",
        "numberOfAssociations",
        "ipAccessHostGpbId",
        "minimumRto",
        "maximumRto",
        "initialRto",
        "rtoAlphaIndex",
        "rtoBetaIndex",
        "validCookieLife",
        "allowedIncrementCookieLife",
        "keyChangePeriod",
        "associationMaxRtx",
        "pathMaxRtx",
        "maxInitialRtrAtt",
        "maxShutDownRtrAtt",
        "heartbeatInterval",
        "heartbeatStatus",
        "maxIncomingStream",
        "maxOutgoingStream",
        "maxUserDataSize",
        "mBuffer",
        "nThreshold",
        "tSack",
        "initialAdRecWin",
        "intervalOobPkts",
        "maxBurst",
        "nPercentage",
        "bundlingActivated",
        "bundlingTimer",
        "rpuId",
        "ipAccessSctpRef",
        "heartbeatMaxBurst",
        "heartbeatPathProbingInterval",
        "pathSelection",
        "potentiallyFailedMaxRtx",
        "sctpAssocDeleteTimeout",
        "switchbackMaxThreshold",
        "switchbackMinThreshold",
        "switchbackMode"
    FROM
    ericsson_bulkcm."vsDataSctp"

    """
)

SctpAssociation = ReplaceableObject(
    'ericsson_cm_3g."SctpAssociation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSctpEndpoint_id",
        "vsDataSctpAssociation_id",
        "redundancyStatus",
        "associationState",
        "remotePrimaryAddress",
        "remoteIpAddress",
        "localIpAddress",
        "remotePortNumber",
        "localPrimaryAddress",
        "localPortNumber"
    FROM
    ericsson_bulkcm."vsDataSctpAssociation"

    """
)

SctpEndpoint = ReplaceableObject(
    'ericsson_cm_3g."SctpEndpoint"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSctpEndpoint_id",
        "portNumber",
        "sctpProfile",
        "localIpAddress",
        "reservedBy",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSctpEndpoint"

    """
)

SctpProfile = ReplaceableObject(
    'ericsson_cm_3g."SctpProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSctpProfile_id",
        "bundlingActivated",
        "minActivateThr",
        "initARWnd",
        "initRto",
        "incCookieLife",
        "maxSctpPduSize",
        "initialHeartbeatInterval",
        "cookieLife",
        "bundlingTimer",
        "pathMaxRtx",
        "sackTimer",
        "primaryPathAvoidance",
        "primaryPathMaxRtx",
        "maxOutStreams",
        "maxInStreams",
        "thrTransmitBufferCongCeased",
        "heartbeatInterval",
        "thrTransmitBuffer",
        "dscp",
        "maxShutdownRt",
        "hbMaxBurst",
        "maxActivateThr",
        "heartbeatActivated",
        "noSwitchback",
        "maxRto",
        "reservedBy",
        "assocMaxRtx",
        "maxInitRt",
        "alphaIndex",
        "betaIndex",
        "minRto",
        "maxBurst",
        "transmitBufferSize",
        "bundlingAdaptiveActivated",
        "volatileMode",
        "sctpPmtud"
    FROM
    ericsson_bulkcm."vsDataSctpProfile"

    """
)

SecM = ReplaceableObject(
    'ericsson_cm_3g."SecM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id"
    FROM
    ericsson_bulkcm."vsDataSecM"

    """
)

Sector = ReplaceableObject(
    'ericsson_cm_3g."Sector"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "NodeBFunction_id",
        "vsDataSector_id",
        "numberOfTxBranches",
        "latitude",
        "latHemisphere",
        "longitude",
        "geoDatum",
        "beamDirection",
        "height",
        "maxInternalUlGainOn",
        "userLabel",
        "band",
        "proceduralStatus",
        "tmaDeviceRef",
        "sectorAntennasRef",
        "retDevicesRef",
        "numberOfSectorAntennas",
        "lineRate",
        "radioBuildingBlock",
        "sectorGroup",
        "mixedModeRadio",
        "sectorConfiguration",
        "noiseFigure"
    FROM
    ericsson_bulkcm."vsDataSector"

    """
)

SectorAntenna = ReplaceableObject(
    'ericsson_cm_3g."SectorAntenna"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "antennaType",
        "beamDirection",
        "positionInformation",
        "positionRef"
    FROM
    ericsson_bulkcm."vsDataSectorAntenna"

    """
)

SectorCarrier = ReplaceableObject(
    'ericsson_cm_3g."SectorCarrier"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataSectorCarrier_id",
        "noOfRxAntennas",
        "noOfTxAntennas",
        "prsEnabled",
        "sectorFunctionRef",
        "maximumTransmissionPower",
        "reservedBy",
        "rfBranchTxRef",
        "rfBranchRxRef",
        "ulForcedTimingAdvanceCommand",
        "radioTransmitPerformanceMode",
        "txPowerPersistentLock",
        "configuredMaxTxPower",
        "partOfSectorPower"
    FROM
    ericsson_bulkcm."vsDataSectorCarrier"

    """
)

SectorEquipmentFunction = ReplaceableObject(
    'ericsson_cm_3g."SectorEquipmentFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSectorEquipmentFunction_id",
        "vsDataNodeSupport_id",
        "vsDataNodeFunction_id",
        "administrativeState",
        "userLabel",
        "rfBranchRef",
        "mixedModeRadio",
        "reservedBy",
        "eUtranFqBands",
        "fqBand",
        "utranFddFqBands",
        "availableSectorPower",
        "configuredOutputPower",
        "confOutputPower"
    FROM
    ericsson_bulkcm."vsDataSectorEquipmentFunction"

    """
)

Security = ReplaceableObject(
    'ericsson_cm_3g."Security"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecurity_id",
        "authorizationCacheTimeOut",
        "certExpirWarnTime",
        "autoUpdateCertEnrollmentServer",
        "crlEarlyUpdateInterval"
    FROM
    ericsson_bulkcm."vsDataSecurity"

    """
)

SecurityHandling = ReplaceableObject(
    'ericsson_cm_3g."SecurityHandling"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataSecurityHandling_id",
        "RncFunction_id",
        "countWrapSupervisionActive",
        "rbIdSupervisionActive",
        "cipheringAlgoPrio",
        "integrityProtectAlgoPrio",
        "ciphering",
        "multiRabSmcHandling"
    FROM
    ericsson_bulkcm."vsDataSecurityHandling"

    """
)

ServiceArea = ReplaceableObject(
    'ericsson_cm_3g."ServiceArea"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataAreas_id",
        "vsDataPlmn_id",
        "vsDataLocationArea_id",
        "vsDataServiceArea_id",
        "userLabel",
        "sac"
    FROM
    ericsson_bulkcm."vsDataServiceArea"

    """
)

ServiceSpecificDRX = ReplaceableObject(
    'ericsson_cm_3g."ServiceSpecificDRX"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataServiceSpecificDRX_id",
        "featureStateServiceSpecificDRX",
        "keyIdServiceSpecificDRX",
        "licenseStateServiceSpecificDRX",
        "serviceStateServiceSpecificDRX"
    FROM
    ericsson_bulkcm."vsDataServiceSpecificDRX"

    """
)

ServiceTriggeredMobility = ReplaceableObject(
    'ericsson_cm_3g."ServiceTriggeredMobility"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataServiceTriggeredMobility_id",
        "featureStateServiceTriggeredMobility",
        "keyIdServiceTriggeredMobility",
        "licenseStateServiceTriggeredMobility",
        "serviceStateServiceTriggeredMobility"
    FROM
    ericsson_bulkcm."vsDataServiceTriggeredMobility"

    """
)

SfpModule = ReplaceableObject(
    'ericsson_cm_3g."SfpModule"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataFieldReplaceableUnit_id",
        "vsDataSfpModule_id",
        "availabilityStatus",
        "administrativeState",
        "operationalState"
    FROM
    ericsson_bulkcm."vsDataSfpModule"

    """
)

Sftp = ReplaceableObject(
    'ericsson_cm_3g."Sftp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataFileTPM_id",
        "vsDataSftp_id"
    FROM
    ericsson_bulkcm."vsDataSftp"

    """
)

Shaper = ReplaceableObject(
    'ericsson_cm_3g."Shaper"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataQueueSystem_id",
        "vsDataShaper_id",
        "order",
        "committedBurstSize_bytes",
        "userLabel",
        "committedInformationRate_kbps"
    FROM
    ericsson_bulkcm."vsDataShaper"

    """
)

SharedNetworkSupport = ReplaceableObject(
    'ericsson_cm_3g."SharedNetworkSupport"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataSharedNetworkSupport_id",
        "keyIdSharedNetworkSupport",
        "featureStateSharedNetworkSupport",
        "licenseStateSharedNetworkSupport",
        "serviceStateSharedNetworkSupport"
    FROM
    ericsson_bulkcm."vsDataSharedNetworkSupport"

    """
)

Sid = ReplaceableObject(
    'ericsson_cm_3g."Sid"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSid_id",
        "updateCellReattsNo",
        "noOfMaxDrxCycles",
        "noOfMibValueTagRetrans",
        "sib1_sib1RepPeriod",
        "sib1_sib1StartPos",
        "sib11_sib11RepPeriod",
        "sib11_sib11StartPos",
        "sib12_sib12RepPeriod",
        "sib12_sib12StartPos",
        "sib3_sib3RepPeriod",
        "sib3_sib3StartPos",
        "sib5_sib5RepPeriod",
        "sib5_sib5StartPos",
        "sib7_sib7RepPeriod",
        "sib7_sib7StartPos",
        "sib7ExpirationTimeFactor",
        "sib2_sib2RepPeriod",
        "sib2_sib2StartPos",
        "schedulingBlockEnabled",
        "sb1_sb1RepPeriod",
        "sb1_sb1StartPos",
        "sib18_sib18RepPeriod",
        "sib18_sib18StartPos",
        "sib19_sib19RepPeriod",
        "sib19_sib19StartPos"
    FROM
    ericsson_bulkcm."vsDataSid"

    """
)

SignalingRadioBearer = ReplaceableObject(
    'ericsson_cm_3g."SignalingRadioBearer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataRadioBearerTable_id",
        "vsDataSignalingRadioBearer_id",
        "tPollRetransmitDl",
        "dlMaxRetxThreshold",
        "ulMaxRetxThreshold",
        "tPollRetransmitUl",
        "tReorderingUl"
    FROM
    ericsson_bulkcm."vsDataSignalingRadioBearer"

    """
)

SingLayBeamfPerfPkg = ReplaceableObject(
    'ericsson_cm_3g."SingLayBeamfPerfPkg"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataSingLayBeamfPerfPkg_id",
        "featureStateSingLayBeamfPerfPkg",
        "keyIdSingLayBeamfPerfPkg",
        "licenseStateSingLayBeamfPerfPkg",
        "serviceStateSingLayBeamfPerfPkg"
    FROM
    ericsson_bulkcm."vsDataSingLayBeamfPerfPkg"

    """
)

Site = ReplaceableObject(
    'ericsson_cm_3g."Site"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataSite_id",
        "userLabel",
        "location",
        "latitude",
        "longitude",
        "altitude",
        "timeZone",
        "freeText",
        "listOfNe",
        "datum",
        "worldTimeZoneId",
        "daylightSavingsAdjust"
    FROM
    ericsson_bulkcm."vsDataSite"

    """
)

Slot = ReplaceableObject(
    'ericsson_cm_3g."Slot"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "slotNumber",
        "activeSwAllocation"
    FROM
    ericsson_bulkcm."vsDataSlot"

    """
)

Snmp = ReplaceableObject(
    'ericsson_cm_3g."Snmp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataSnmp_id",
        "administrativeState",
        "agentAddress_host",
        "agentAddress_port",
        "agentAddressDtls",
        "trustCategory",
        "nodeCredential"
    FROM
    ericsson_bulkcm."vsDataSnmp"

    """
)

SnmpTargetV2C = ReplaceableObject(
    'ericsson_cm_3g."SnmpTargetV2C"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataSnmp_id",
        "vsDataSnmpTargetV2C_id",
        "community",
        "informRetryCount",
        "address",
        "port",
        "informTimeout",
        "transportMethod",
        "isMibWritable",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataSnmpTargetV2C"

    """
)

SnmpTargetV3 = ReplaceableObject(
    'ericsson_cm_3g."SnmpTargetV3"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataSnmp_id",
        "vsDataSnmpTargetV3_id",
        "user",
        "authProtocol",
        "privProtocol",
        "informRetryCount",
        "administrativeState",
        "address",
        "port",
        "informTimeout",
        "transportMethod",
        "snmpSecurityLevel",
        "privKey_cleartext",
        "privKey_password",
        "authKey_cleartext",
        "authKey_password",
        "isMibWritable"
    FROM
    ericsson_bulkcm."vsDataSnmpTargetV3"

    """
)

SpDevicePool = ReplaceableObject(
    'ericsson_cm_3g."SpDevicePool"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSpDevicePool_id"
    FROM
    ericsson_bulkcm."vsDataSpDevicePool"

    """
)

SpidHoWhiteList = ReplaceableObject(
    'ericsson_cm_3g."SpidHoWhiteList"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataSpidHoWhiteList_id",
        "featureStateSpidHoWhiteList",
        "keyIdSpidHoWhiteList",
        "licenseStateSpidHoWhiteList",
        "serviceStateSpidHoWhiteList"
    FROM
    ericsson_bulkcm."vsDataSpidHoWhiteList"

    """
)

SpidRATFreqPrio = ReplaceableObject(
    'ericsson_cm_3g."SpidRATFreqPrio"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataSpidRATFreqPrio_id",
        "featureStateSpidRATFreqPrio",
        "keyIdSpidRATFreqPrio",
        "licenseStateSpidRATFreqPrio",
        "serviceStateSpidRATFreqPrio"
    FROM
    ericsson_bulkcm."vsDataSpidRATFreqPrio"

    """
)

SpiQosClass = ReplaceableObject(
    'ericsson_cm_3g."SpiQosClass"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCnOperator_id",
        "vsDataRnlQosClassProfile_id",
        "vsDataSpiQosClass_id",
        "vsDataRabHandling_id",
        "flowControl",
        "userLabel",
        "hsFachQosLevel"
    FROM
    ericsson_bulkcm."vsDataSpiQosClass"

    """
)

SRVCCtoUTRAN = ReplaceableObject(
    'ericsson_cm_3g."SRVCCtoUTRAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataSRVCCtoUTRAN_id",
        "featureStateSRVCCtoUTRAN",
        "keyIdSRVCCtoUTRAN",
        "licenseStateSRVCCtoUTRAN",
        "serviceStateSRVCCtoUTRAN"
    FROM
    ericsson_bulkcm."vsDataSRVCCtoUTRAN"

    """
)

STN = ReplaceableObject(
    'ericsson_cm_3g."STN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "operationalState",
        "depIP_Interface",
        "wakeUpEventInterval",
        "sw_primaryproductnumber",
        "sw_primaryproductrevision",
        "sw_backupproductnumber",
        "sw_backupproductrevision",
        "cpu_load",
        "alarmSupervisionActive",
        "dscp_operationandmaintenance",
        "dscp_om_filetransfer",
        "stn_pgw_keepaliveperiod",
        "stn_pgw_l2tp_maxtransmissions",
        "stn_pgw_l2tp_retransmissioncap",
        "stn_pgw_l2tp_initialretransmissionperiod",
        "stn_name",
        "restartReason",
        "systemClockTimeServer",
        "stn_systemclockudp_port",
        "contactWithFileServer",
        "systemClockUDP_Port_General_PTP",
        "systemClockUDP_Port_Event_PTP",
        "systemClockTimeServerType",
        "depLocalRoutingPolicy",
        "userLabel",
        "promptPrefix",
        "arpPcp",
        "lastConfigChange",
        "systemClockPTPDomainNumber",
        "wakeUpDestination",
        "robustStnReconfigCountdownActivated",
        "arpRefreshAttemptsInterval",
        "arpRefreshNoOfAttempts",
        "arpMeanRefreshInterval",
        "robustRollbackTimer",
        "nodeAuthenticationSecret"
    FROM
    ericsson_bulkcm."vsDataSTN"

    """
)

StnFunction = ReplaceableObject(
    'ericsson_cm_3g."StnFunction"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataStnFunction_id",
        "actPmAfterIntegration",
        "postIntegrationBulkfile",
        "statusFm",
        "statusPm",
        "useContainerFile",
        "integrationSequence",
        "integrationDetails",
        "stnConfigLevel",
        "siteInstallation",
        "boundSiteInstallation",
        "softwareUpgrade"
    FROM
    ericsson_bulkcm."vsDataStnFunction"

    """
)

StreamingCapabilities = ReplaceableObject(
    'ericsson_cm_3g."StreamingCapabilities"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataPmEventM_id",
        "vsDataEventProducer_id",
        "vsDataStreamingCapabilities_id",
        "supportedCompressionTypes"
    FROM
    ericsson_bulkcm."vsDataStreamingCapabilities"

    """
)

Subrack = ReplaceableObject(
    'ericsson_cm_3g."Subrack"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "subrackPosition",
        "cabinetPosition",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSubrack"

    """
)

SubscriberProfileID = ReplaceableObject(
    'ericsson_cm_3g."SubscriberProfileID"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataSubscriberProfileID_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSubscriberProfileID"

    """
)

SubscrProfileIdHandling = ReplaceableObject(
    'ericsson_cm_3g."SubscrProfileIdHandling"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataSubscrProfileIdHandling_id",
        "spidPreventRwrEutra",
        "spidDedicPrioEutra"
    FROM
    ericsson_bulkcm."vsDataSubscrProfileIdHandling"

    """
)

Support12Cells = ReplaceableObject(
    'ericsson_cm_3g."Support12Cells"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataSupport12Cells_id",
        "featureStateSupport12Cells",
        "keyIdSupport12Cells",
        "licenseStateSupport12Cells",
        "serviceStateSupport12Cells"
    FROM
    ericsson_bulkcm."vsDataSupport12Cells"

    """
)

Support6Cells = ReplaceableObject(
    'ericsson_cm_3g."Support6Cells"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataSupport6Cells_id",
        "serviceStateSupport6Cells",
        "licenseStateSupport6Cells",
        "keyIdSupport6Cells",
        "featureStateSupport6Cells"
    FROM
    ericsson_bulkcm."vsDataSupport6Cells"

    """
)

SwAllocation = ReplaceableObject(
    'ericsson_cm_3g."SwAllocation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSwManagement_id",
        "vsDataSwAllocation_id",
        "role",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSwAllocation"

    """
)

SwInventory = ReplaceableObject(
    'ericsson_cm_3g."SwInventory"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSwInventory_id",
        "active",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSwInventory"

    """
)

SwitchCoreUnit = ReplaceableObject(
    'ericsson_cm_3g."SwitchCoreUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataSwitchCoreUnit_id",
        "administrativeStateSili",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSwitchCoreUnit"

    """
)

SwitchInternalLinkPort = ReplaceableObject(
    'ericsson_cm_3g."SwitchInternalLinkPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataSwitchCoreUnit_id",
        "vsDataSwitchInternalLinkPort_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSwitchInternalLinkPort"

    """
)

SwitchPortStp = ReplaceableObject(
    'ericsson_cm_3g."SwitchPortStp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataEthernetSwitchModule_id",
        "vsDataEthernetSwitchModulePort_id",
        "vsDataSwitchPortStp_id",
        "vsDataLag_id",
        "vsDataEthernetBridgePort_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataEthernetSwitch_id",
        "vsDataEthernetSwitchPort_id",
        "edgePortMode",
        "edgePortBpduGuardTimeOut",
        "priority",
        "manualPathCost",
        "configuredPathCost",
        "actualPathCost",
        "stpState",
        "stpRole",
        "remoteBridgeId",
        "userLabel",
        "rootPathCost",
        "protocolVersion",
        "settingsUsed",
        "l2gpActive",
        "l2gpBpduReceive",
        "l2gpPortPriority",
        "l2gpPseudoRootId"
    FROM
    ericsson_bulkcm."vsDataSwitchPortStp"

    """
)

SwitchStp = ReplaceableObject(
    'ericsson_cm_3g."SwitchStp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataEthernetSwitchModule_id",
        "vsDataSwitchStp_id",
        "vsDataExchangeTerminalIp_id",
        "vsDataEthernetSwitch_id",
        "administrativeState",
        "mode",
        "bridgePriority",
        "bridgeHelloTime",
        "bridgeMaxAge",
        "bridgeForwardDelay",
        "bridgeId",
        "rootBridgeId",
        "rootPortNumber",
        "userLabel",
        "transmitHoldCount"
    FROM
    ericsson_bulkcm."vsDataSwitchStp"

    """
)

SwItem = ReplaceableObject(
    'ericsson_cm_3g."SwItem"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSwInventory_id",
        "vsDataSwItem_id",
        "additionalInfo",
        "administrativeData_productName",
        "administrativeData_productNumber",
        "administrativeData_productRevision",
        "administrativeData_productionDate",
        "administrativeData_description",
        "administrativeData_xossx_type",
        "consistsOf",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSwItem"

    """
)

SwM = ReplaceableObject(
    'ericsson_cm_3g."SwM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSwM_id",
        "reportProgress",
        "actionInProgress",
        "localFileStorePath",
        "userLabel",
        "fallbackTimer",
        "reportProgress_actionName",
        "reportProgress_progressInfo",
        "reportProgress_progressPercentage",
        "reportProgress_xossx_result",
        "reportProgress_resultInfo",
        "reportProgress_state",
        "reportProgress_actionId",
        "reportProgress_timeActionStarted",
        "reportProgress_timeActionCompleted",
        "reportProgress_timeOfLastStatusUpdate"
    FROM
    ericsson_bulkcm."vsDataSwM"

    """
)

SwManagement = ReplaceableObject(
    'ericsson_cm_3g."SwManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSwManagement_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSwManagement"

    """
)

SwVersion = ReplaceableObject(
    'ericsson_cm_3g."SwVersion"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSwInventory_id",
        "vsDataSwVersion_id",
        "administrativeData_productName",
        "administrativeData_productNumber",
        "administrativeData_productRevision",
        "administrativeData_productionDate",
        "administrativeData_description",
        "administrativeData_xossx_type",
        "consistsOf",
        "timeOfActivation",
        "timeOfDeactivation",
        "timeOfInstallation",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSwVersion"

    """
)

Synchronization = ReplaceableObject(
    'ericsson_cm_3g."Synchronization"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataSynchronization_id",
        "vsDataSTN_id",
        "vsDataTransport_id",
        "degradationIsFault",
        "userLabel",
        "syncReference",
        "syncRefPriority",
        "fixedPosition",
        "sfnInitializationTime",
        "featureStatePtpFreq",
        "featureStatePtpTime",
        "featureStateSyncEth",
        "licenseStatePtpFreq",
        "licenseStatePtpTime",
        "licenseStateSyncEth",
        "telecomStandard",
        "useReceivedQl",
        "adminQuality",
        "selectionProcessMode",
        "minQualityLevel",
        "operQualityLevel",
        "freqHoldoverAlarmConfig_enable",
        "freqHoldoverAlarmConfig_filterTime",
        "timeHoldoverAlarmConfig_enable",
        "timeHoldoverAlarmConfig_filterTime",
        "ts_stn_synchstatus",
        "ts_usedtimeserver",
        "calibrationExpireDate",
        "synchType",
        "dscp_synchronization",
        "depIP_Interface",
        "usedSynchSource",
        "calibrationStatus",
        "ptpFreqFeatureState",
        "ptpFreqLicenseState",
        "ptpTimeFeatureState",
        "ptpTimeLicenseState",
        "operQuality",
        "dscp"
    FROM
    ericsson_bulkcm."vsDataSynchronization"

    """
)

SyncPort = ReplaceableObject(
    'ericsson_cm_3g."SyncPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataFieldReplaceableUnit_id",
        "vsDataSyncPort_id",
        "availabilityStatus",
        "operationalState",
        "reservedBy",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSyncPort"

    """
)

SyncServer = ReplaceableObject(
    'ericsson_cm_3g."SyncServer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataSyncServer_id",
        "protocol",
        "serverAddress",
        "administrativeState",
        "communicationMedia",
        "ptpSyncStatus",
        "domainNumber",
        "ptpAsymmetryCompensation"
    FROM
    ericsson_bulkcm."vsDataSyncServer"

    """
)

SysM = ReplaceableObject(
    'ericsson_cm_3g."SysM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataSysM"

    """
)

SystemFunctions = ReplaceableObject(
    'ericsson_cm_3g."SystemFunctions"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id"
    FROM
    ericsson_bulkcm."vsDataSystemFunctions"

    """
)

TCPOptimization = ReplaceableObject(
    'ericsson_cm_3g."TCPOptimization"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataTCPOptimization_id",
        "featureStateTCPOptimization",
        "keyIdTCPOptimization",
        "licenseStateTCPOptimization",
        "serviceStateTCPOptimization"
    FROM
    ericsson_bulkcm."vsDataTCPOptimization"

    """
)

TdScdmaSessionContinuity = ReplaceableObject(
    'ericsson_cm_3g."TdScdmaSessionContinuity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataTdScdmaSessionContinuity_id",
        "featureStateTdScdmaSessionContinuity",
        "keyIdTdScdmaSessionContinuity",
        "licenseStateTdScdmaSessionContinuity",
        "serviceStateTdScdmaSessionContinuity"
    FROM
    ericsson_bulkcm."vsDataTdScdmaSessionContinuity"

    """
)

TempSensor = ReplaceableObject(
    'ericsson_cm_3g."TempSensor"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataTempSensor_id",
        "currentTemp",
        "highTemp",
        "highTempDate",
        "lowTemp",
        "lowTempDate",
        "highDestructiveMeasure",
        "lowDestructiveMeasure",
        "inHighExtendedTemp",
        "inLowExtendedTemp"
    FROM
    ericsson_bulkcm."vsDataTempSensor"

    """
)

TermPointToENB = ReplaceableObject(
    'ericsson_cm_3g."TermPointToENB"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtraNetwork_id",
        "vsDataExternalENodeBFunction_id",
        "vsDataTermPointToENB_id",
        "ipAddress",
        "administrativeState",
        "domainName",
        "usedIpAddress",
        "ipv6Address",
        "lastModification",
        "createdBy",
        "timeOfCreation",
        "timeOfLastModification"
    FROM
    ericsson_bulkcm."vsDataTermPointToENB"

    """
)

TermPointToMme = ReplaceableObject(
    'ericsson_cm_3g."TermPointToMme"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataTermPointToMme_id",
        "mmeName",
        "domainName",
        "ipAddress1",
        "administrativeState",
        "ipAddress2",
        "usedIpAddress",
        "relativeMmeCapacity",
        "ipv6Address1",
        "ipv6Address2",
        "mmeCodeListLTERelated",
        "mmeCodeListOtherRATs",
        "mmeGIListLTERelated",
        "servedPlmnListLTERelated_mcc",
        "servedPlmnListLTERelated_mnc",
        "servedPlmnListLTERelated_mncLength",
        "servedPlmnListOtherRATs",
        "servedPlmnListLTERelated"
    FROM
    ericsson_bulkcm."vsDataTermPointToMme"

    """
)

TermPointToSGW = ReplaceableObject(
    'ericsson_cm_3g."TermPointToSGW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataTermPointToSGW_id"
    FROM
    ericsson_bulkcm."vsDataTermPointToSGW"

    """
)

TimeM = ReplaceableObject(
    'ericsson_cm_3g."TimeM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSysM_id",
        "vsDataTimeM_id"
    FROM
    ericsson_bulkcm."vsDataTimeM"

    """
)

TimeServer = ReplaceableObject(
    'ericsson_cm_3g."TimeServer"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataSynchronization_id",
        "vsDataTimeServer_id",
        "ts_priority",
        "ts_ip_address",
        "stn_ts_udp_port",
        "ts_udp_port_general_ptp",
        "ts_udp_port_event_ptp",
        "timeServerType",
        "domainNumber"
    FROM
    ericsson_bulkcm."vsDataTimeServer"

    """
)

TimeSetting = ReplaceableObject(
    'ericsson_cm_3g."TimeSetting"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataTimeSetting_id",
        "gpsToUtcLeapSeconds",
        "timeOffset",
        "daylightSavingTimeOffset",
        "gpsToUtcLeapSecondsChangeDate",
        "userLabel",
        "daylightSavingTimeOn",
        "daylightSavingTimeEndRule_dayRule",
        "daylightSavingTimeEndRule_month",
        "daylightSavingTimeEndRule_time",
        "daylightSavingTimeStartRule_dayRule",
        "daylightSavingTimeStartRule_month",
        "daylightSavingTimeStartRule_time",
        "daylightSavingTimeEndDate",
        "daylightSavingTimeStartDate",
        "daylightSavingTimeOffDate",
        "daylightSavingTimeOnDate"
    FROM
    ericsson_bulkcm."vsDataTimeSetting"

    """
)

TimeSettings = ReplaceableObject(
    'ericsson_cm_3g."TimeSettings"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataNodeSupport_id",
        "vsDataTimeSettings_id",
        "gpsToUtcLeapSeconds",
        "daylightSavingTimeEndDate",
        "timeOffset",
        "daylightSavingTimeOffset",
        "gpsToUtcLeapSecondsChangeDate",
        "daylightSavingTimeStartDate"
    FROM
    ericsson_bulkcm."vsDataTimeSettings"

    """
)

TimeSyncIO = ReplaceableObject(
    'ericsson_cm_3g."TimeSyncIO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataSynchronization_id",
        "vsDataTimeSyncIo_id",
        "altitude",
        "longitude",
        "gpsRefState",
        "latitude",
        "noOfSatellitesInView",
        "compensationDelay"
    FROM
    ericsson_bulkcm."vsDataTimeSyncIO"

    """
)

TimingUnit = ReplaceableObject(
    'ericsson_cm_3g."TimingUnit"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataTimingUnit_id",
        "vsDataCbu_id",
        "userLabel",
        "gpsOutEnabled",
        "hptsiOutEnabled"
    FROM
    ericsson_bulkcm."vsDataTimingUnit"

    """
)

Tls = ReplaceableObject(
    'ericsson_cm_3g."Tls"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataTls_id",
        "supportedCiphers_protocolVersion",
        "supportedCiphers_keyExchange",
        "supportedCiphers_authentication",
        "supportedCiphers_encryption",
        "supportedCiphers_mac",
        "supportedCiphers_export",
        "supportedCiphers_xossx_name",
        "cipherFilter",
        "enabledCiphers_protocolVersion",
        "enabledCiphers_keyExchange",
        "enabledCiphers_authentication",
        "enabledCiphers_encryption",
        "enabledCiphers_mac",
        "enabledCiphers_export",
        "enabledCiphers_xossx_name",
        "supportedCiphers",
        "enabledCiphers"
    FROM
    ericsson_bulkcm."vsDataTls"

    """
)

Tm7ModeSwitching = ReplaceableObject(
    'ericsson_cm_3g."Tm7ModeSwitching"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataTm7ModeSwitching_id",
        "featureStateTm7ModeSwitching",
        "keyIdTm7ModeSwitching",
        "licenseStateTm7ModeSwitching",
        "serviceStateTm7ModeSwitching"
    FROM
    ericsson_bulkcm."vsDataTm7ModeSwitching"

    """
)

TmaSupport = ReplaceableObject(
    'ericsson_cm_3g."TmaSupport"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataTmaSupport_id",
        "keyIdTmaSupport",
        "featureStateTmaSupport",
        "licenseStateTmaSupport",
        "serviceStateTmaSupport"
    FROM
    ericsson_bulkcm."vsDataTmaSupport"

    """
)

TnApplication = ReplaceableObject(
    'ericsson_cm_3g."TnApplication"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "vsDataTnApplication_id"
    FROM
    ericsson_bulkcm."vsDataTnApplication"

    """
)

TnlCchQosClassProfile = ReplaceableObject(
    'ericsson_cm_3g."TnlCchQosClassProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTnlCchQosClassProfile_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataTnlCchQosClassProfile"

    """
)

TnlDchQosClassProfile = ReplaceableObject(
    'ericsson_cm_3g."TnlDchQosClassProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRabHandling_id",
        "vsDataTnlDchQosClassProfile_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataTnlDchQosClassProfile"

    """
)

TnlHspaQosClassProfile = ReplaceableObject(
    'ericsson_cm_3g."TnlHspaQosClassProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRabHandling_id",
        "vsDataTnlHspaQosClassProfile_id",
        "userLabel",
        "eulFachSpi"
    FROM
    ericsson_bulkcm."vsDataTnlHspaQosClassProfile"

    """
)

TnlIuQosClassProfile = ReplaceableObject(
    'ericsson_cm_3g."TnlIuQosClassProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRabHandling_id",
        "vsDataTnlIuQosClassProfile_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataTnlIuQosClassProfile"

    """
)

TnlQosClass = ReplaceableObject(
    'ericsson_cm_3g."TnlQosClass"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataRabHandling_id",
        "vsDataTnlHspaQosClassProfile_id",
        "vsDataTnlQosClass_id",
        "vsDataTnlCchQosClassProfile_id",
        "vsDataTnlDchQosClassProfile_id",
        "aal2QosClass",
        "dscpEgress",
        "dscpIngress",
        "spi",
        "userLabel",
        "prefIubUserPlaneTransportOption_atm",
        "prefIubUserPlaneTransportOption_ipv4"
    FROM
    ericsson_bulkcm."vsDataTnlQosClass"

    """
)

TnPort = ReplaceableObject(
    'ericsson_cm_3g."TnPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataFieldReplaceableUnit_id",
        "vsDataTnPort_id",
        "reservedBy",
        "userLabel",
        "sfpModuleRef"
    FROM
    ericsson_bulkcm."vsDataTnPort"

    """
)

TpaDevice = ReplaceableObject(
    'ericsson_cm_3g."TpaDevice"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRruDeviceGroup_id",
        "vsDataTpaDeviceSet_id",
        "vsDataTpaDevice_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "vsDataDeviceGroup_id",
        "maxTotalOutputPower",
        "maxTotalOutputPowerLow",
        "txPowerPersistentLock",
        "extraPowerHsdpaMixedModePowerSharing"
    FROM
    ericsson_bulkcm."vsDataTpaDevice"

    """
)

TpaDeviceSet = ReplaceableObject(
    'ericsson_cm_3g."TpaDeviceSet"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSectorAntenna_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataRruDeviceGroup_id",
        "vsDataTpaDeviceSet_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "vsDataDeviceGroup_id"
    FROM
    ericsson_bulkcm."vsDataTpaDeviceSet"

    """
)

TrafficAwarePowerSave = ReplaceableObject(
    'ericsson_cm_3g."TrafficAwarePowerSave"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataTrafficAwarePowerSave_id",
        "tpsWaitTimeLock",
        "tpsUarfcnPriorityOrder",
        "tpsWaitTimeUnlock",
        "tpsContCovUarfcn",
        "tpsUnlockThreshold",
        "tpsLockThreshold",
        "tpsMultiCarrierAllowed"
    FROM
    ericsson_bulkcm."vsDataTrafficAwarePowerSave"

    """
)

TrafficClass = ReplaceableObject(
    'ericsson_cm_3g."TrafficClass"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCnOperator_id",
        "vsDataRnlQosClassProfile_id",
        "vsDataTrafficClass_id",
        "vsDataRabHandling_id",
        "vsDataArpQosClassProfile_id",
        "vsDataTnlDchQosClassProfile_id",
        "vsDataTnlIuQosClassProfile_id",
        "defaultQosRef",
        "tcInd",
        "cnInd",
        "serviceInd",
        "ssd",
        "userLabel",
        "arpSpiMapRef"
    FROM
    ericsson_bulkcm."vsDataTrafficClass"

    """
)

TrafficClassPsInt = ReplaceableObject(
    'ericsson_cm_3g."TrafficClassPsInt"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataCnOperator_id",
        "vsDataRnlQosClassProfile_id",
        "vsDataTrafficClassPsInt_id",
        "vsDataRabHandling_id",
        "vsDataArpQosClassProfile_id",
        "vsDataTnlIuQosClassProfile_id",
        "thp",
        "si",
        "qosRef",
        "userLabel",
        "arpSpiMapRef"
    FROM
    ericsson_bulkcm."vsDataTrafficClassPsInt"

    """
)

TrafficManagement = ReplaceableObject(
    'ericsson_cm_3g."TrafficManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataTrafficManagement_id",
        "featureState",
        "licenseState",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataTrafficManagement"

    """
)

TrafficManager = ReplaceableObject(
    'ericsson_cm_3g."TrafficManager"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataTrafficManager_id",
        "schedulerMeanRate",
        "schedulerMaxBurstSize",
        "diffServAlgDropQThreshold_1",
        "diffServMinRateRelative_1",
        "diffServAlgDropQThreshold_2",
        "diffServMinRateRelative_2",
        "diffServAlgDropQThreshold_3",
        "diffServMinRateRelative_3",
        "diffServAlgDropQThreshold_4",
        "diffServMinRateRelative_4",
        "diffServAlgDropQThreshold_5",
        "diffServMinRateRelative_5",
        "diffServAlgDropQThreshold_6",
        "diffServMinRateRelative_6",
        "diffServAlgDropQThreshold_7",
        "diffServMinRateRelative_7",
        "diffServAlgDropQThreshold_8",
        "diffServMinRateRelative_8",
        "depQosPolicy"
    FROM
    ericsson_bulkcm."vsDataTrafficManager"

    """
)

TrafficScheduler = ReplaceableObject(
    'ericsson_cm_3g."TrafficScheduler"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataEthernetPort_id",
        "vsDataTrafficScheduler_id",
        "wifiDLPolicingFactor",
        "egressCir",
        "trafficShapingProfile",
        "egressCbs",
        "rbsULPolicingFactor"
    FROM
    ericsson_bulkcm."vsDataTrafficScheduler"

    """
)

Transceiver = ReplaceableObject(
    'ericsson_cm_3g."Transceiver"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataDeviceGroup_id",
        "vsDataTransceiver_id",
        "availabilityStatus",
        "operationalState",
        "reservedBy",
        "requestedRelativeOutputPower"
    FROM
    ericsson_bulkcm."vsDataTransceiver"

    """
)

Transport = ReplaceableObject(
    'ericsson_cm_3g."Transport"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id"
    FROM
    ericsson_bulkcm."vsDataTransport"

    """
)

TransportNetwork = ReplaceableObject(
    'ericsson_cm_3g."TransportNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataTransportNetwork"

    """
)

TrustCategory = ReplaceableObject(
    'ericsson_cm_3g."TrustCategory"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataTrustCategory_id",
        "userLabel",
        "trustedCertificates"
    FROM
    ericsson_bulkcm."vsDataTrustCategory"

    """
)

TrustedCertificate = ReplaceableObject(
    'ericsson_cm_3g."TrustedCertificate"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataTrustedCertificate_id",
        "managedState",
        "certificateState",
        "certificateContent_version",
        "certificateContent_serialNumber",
        "certificateContent_signatureAlgorithm",
        "certificateContent_issuer",
        "certificateContent_validFrom",
        "certificateContent_validTo",
        "certificateContent_publicKey",
        "certificateContent_publicKeyAlgorithm",
        "certificateContent_keyUsage",
        "certificateContent_subject"
    FROM
    ericsson_bulkcm."vsDataTrustedCertificate"

    """
)

TtiBundling = ReplaceableObject(
    'ericsson_cm_3g."TtiBundling"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataTtiBundling_id",
        "featureStateTtiBundling",
        "keyIdTtiBundling",
        "licenseStateTtiBundling",
        "serviceStateTtiBundling"
    FROM
    ericsson_bulkcm."vsDataTtiBundling"

    """
)

TuSyncRef = ReplaceableObject(
    'ericsson_cm_3g."TuSyncRef"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataTimingUnit_id",
        "vsDataTuSyncRef_id",
        "vsDataCbu_id",
        "userLabel",
        "administrativeState"
    FROM
    ericsson_bulkcm."vsDataTuSyncRef"

    """
)

TwampResponder = ReplaceableObject(
    'ericsson_cm_3g."TwampResponder"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIppm_id",
        "vsDataTwampResponder_id",
        "vsDataSTN_id",
        "vsDataTransport_id",
        "vsDataRouter_id",
        "administrativeState",
        "ipAccessHostEtRef",
        "udpPort",
        "userLabel",
        "actualModes",
        "timeout",
        "depIP_Interface",
        "remoteIpAddress",
        "responderType",
        "ipAddress"
    FROM
    ericsson_bulkcm."vsDataTwampResponder"

    """
)

TxDataCloning = ReplaceableObject(
    'ericsson_cm_3g."TxDataCloning"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataTxDataCloning_id",
        "featureStateTxDataCloning",
        "keyIdTxDataCloning",
        "licenseStateTxDataCloning",
        "serviceStateTxDataCloning"
    FROM
    ericsson_bulkcm."vsDataTxDataCloning"

    """
)

TxDeviceGroup = ReplaceableObject(
    'ericsson_cm_3g."TxDeviceGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataPiuDevice_id",
        "vsDataTxDeviceGroup_id",
        "numHsCodeResources",
        "numEulResources"
    FROM
    ericsson_bulkcm."vsDataTxDeviceGroup"

    """
)

UeMeasControl = ReplaceableObject(
    'ericsson_cm_3g."UeMeasControl"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUeMeasControl_id",
        "RncFunction_id",
        "sMeasure",
        "filterCoefficientEUtraRsrp",
        "filterCoefficientEUtraRsrq",
        "a5B2MobilityTimer",
        "maxMeasCdma2000eHrpd",
        "maxMeasEUtraOther",
        "maxMeasGeran",
        "maxMeasInterFreqEUtra",
        "maxMeasUtraFdd",
        "ueMeasurementsActive",
        "measQuantityUtraFDD",
        "zzzTemporary1",
        "zzzTemporary2",
        "zzzTemporary3",
        "zzzTemporary4",
        "zzzTemporary5",
        "zzzTemporary6",
        "zzzTemporary7",
        "maxMeasUtraTdd",
        "maxUtranCellsToMeasure",
        "csfbHoTargetSearchTimer",
        "maxMeasCdma20001xRtt",
        "allowReleaseQci1",
        "ueMeasurementsActiveCDMA2000",
        "ueMeasurementsActiveGERAN",
        "ueMeasurementsActiveIF",
        "ueMeasurementsActiveUTRAN",
        "searchEffortTime",
        "servOrPrioIFHoTimer",
        "ueMeasurementsActiveCDMA20001xRtt",
        "inhibitB2RsrqConfig",
        "bothA5RsrpRsrqCheck",
        "zzzTemporary9",
        "zzzTemporary8",
        "lowPrioMeasThresh",
        "excludeInterFreqAtCritical",
        "zzzTemporary20",
        "zzzTemporary10",
        "zzzTemporary11",
        "zzzTemporary12",
        "zzzTemporary13",
        "zzzTemporary14",
        "zzzTemporary15",
        "zzzTemporary16",
        "zzzTemporary17",
        "zzzTemporary18",
        "zzzTemporary19",
        "filterCoefficientEUtraUlSinrMax",
        "maxNoMeasReportsInact",
        "filterCoefficientEUtraNI",
        "ulSinrOffset",
        "targetA2UlSearchOffset",
        "a3SuspendCsgTimer",
        "zzzTemporary21",
        "zzzTemporary22",
        "zzzTemporary25",
        "zzzTemporary23",
        "zzzTemporary24",
        "userLabel",
        "reportingRange1a",
        "reportingRange1b",
        "hysteresis1c",
        "hysteresis1d",
        "hysteresis2d",
        "hysteresis2f",
        "gsmThresh3a",
        "hysteresis3a",
        "measQuantity1",
        "ueTxPowerThresh6b",
        "usedFreqThresh2dEcnoDrnc",
        "usedFreqThresh2dRscpDrnc",
        "usedFreqRelThresh2fEcno",
        "usedFreqRelThresh2fRscp",
        "hyst4_2b",
        "nonUsedFreqThresh4_2bEcno",
        "nonUsedFreqThresh4_2bRscp",
        "timeToTrigger1a",
        "hysteresis1a",
        "timeToTrigger1b",
        "hysteresis1b",
        "timeToTrigger1c",
        "timeToTrigger1d",
        "timeToTrigger3a",
        "reportingInterval1a",
        "reportingInterval1c",
        "timeTrigg6b",
        "timeTrigg4_2b",
        "hsHysteresis1d",
        "hsQualityEstimate",
        "hsTimeToTrigger1d",
        "filterCoefficient1",
        "filterCoefficient2",
        "utranFilterCoefficient3",
        "gsmFilterCoefficient3",
        "filterCoeff6",
        "filterCoeff4_2b",
        "w1a",
        "w1b",
        "usedFreqW2d",
        "usedFreqW2f",
        "usedFreqW4_2b",
        "utranW3a",
        "nonUsedFreqW4_2b",
        "timeToTrigger2dEcno",
        "timeToTrigger2fEcno",
        "utranRelThresh3aEcno",
        "utranRelThresh3aRscp",
        "usedFreqRelThresh4_2bEcno",
        "usedFreqRelThresh4_2bRscp",
        "timeToTrigger2dRscp",
        "timeToTrigger2fRscp",
        "utranRelThreshRscp",
        "event1dRncThreshold",
        "event1dRncOffset",
        "timeToTrigger6d",
        "txPowerConnQualMonEnabled",
        "usedFreqGanThreshEcNo",
        "gsmThresh3aLbho",
        "nonUsedFreqThresh4_2bEcnoLbho",
        "timeToTrigger2dRwr",
        "timeToTrigger2fRwr",
        "relThresh2fRwr",
        "reportingRange1aOffsetSecondary",
        "connRelEmptyBufTimeoutDelay",
        "nonUsedFreqRelThresh4_2bEcno",
        "nonUsedFreqRelThresh4_2bRscp",
        "badCoverageMeasSelection",
        "nrCandFreqToMeas"
    FROM
    ericsson_bulkcm."vsDataUeMeasControl"

    """
)

UePosCellId = ReplaceableObject(
    'ericsson_cm_3g."UePosCellId"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataUePosCellId_id",
        "keyIdCellId",
        "featureStateCellId",
        "licenseStateCellId",
        "serviceStateCellId"
    FROM
    ericsson_bulkcm."vsDataUePosCellId"

    """
)

UePositioning = ReplaceableObject(
    'ericsson_cm_3g."UePositioning"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUePositioning_id",
        "enabledPositioningFeatures",
        "clientTypeMapping_valueAddedServices",
        "clientTypeMapping_plmnOperServices",
        "clientTypeMapping_lawfulInterceptServices",
        "clientTypeMapping_plmnOperBroadcastServices",
        "clientTypeMapping_plmnOperOm",
        "clientTypeMapping_plmnOperAnonymousStatistics",
        "clientTypeMapping_plmnOperTargetMsServiceSupport",
        "cellIdPosQualities_responseTimeTypical",
        "cellIdPosQualities_accuracyCodeTypical",
        "cellIdPosQualities_verticalAccuracyCodeTypical",
        "cellIdPosQualities_confidenceEstimate"
    FROM
    ericsson_bulkcm."vsDataUePositioning"

    """
)

UeRabType = ReplaceableObject(
    'ericsson_cm_3g."UeRabType"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeRabType_id",
        "dchFrameSynchRef"
    FROM
    ericsson_bulkcm."vsDataUeRabType"

    """
)

UeRc = ReplaceableObject(
    'ericsson_cm_3g."UeRc"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeRc_id",
        "userLabel",
        "serviceOffset2dEcno",
        "serviceOffset2dRscp",
        "spare",
        "ifhoSupport",
        "gsmHoSupport"
    FROM
    ericsson_bulkcm."vsDataUeRc"

    """
)

UeRcEdchFlow = ReplaceableObject(
    'ericsson_cm_3g."UeRcEdchFlow"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeRc_id",
        "vsDataUeRcEdchFlow_id",
        "harqTransmUlMax",
        "tti"
    FROM
    ericsson_bulkcm."vsDataUeRcEdchFlow"

    """
)

UeRcPhyChEdch = ReplaceableObject(
    'ericsson_cm_3g."UeRcPhyChEdch"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeRc_id",
        "vsDataUeRcPhyChEdch_id",
        "eulHarqRv"
    FROM
    ericsson_bulkcm."vsDataUeRcPhyChEdch"

    """
)

UeRcRab = ReplaceableObject(
    'ericsson_cm_3g."UeRcRab"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeRc_id",
        "vsDataUeRcRab_id",
        "fcState"
    FROM
    ericsson_bulkcm."vsDataUeRcRab"

    """
)

UeRcTrCh = ReplaceableObject(
    'ericsson_cm_3g."UeRcTrCh"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeRc_id",
        "vsDataUeRcTrCh_id",
        "blerQualityTargetDl",
        "blerQualityTargetUl"
    FROM
    ericsson_bulkcm."vsDataUeRcTrCh"

    """
)

UeRrcType = ReplaceableObject(
    'ericsson_cm_3g."UeRrcType"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeRrcType_id",
        "dchFrameSynchRef"
    FROM
    ericsson_bulkcm."vsDataUeRrcType"

    """
)

UeTac = ReplaceableObject(
    'ericsson_cm_3g."UeTac"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUeTac_id",
        "maxSvn",
        "minSvn",
        "rncFeatureRef",
        "tac",
        "tacParams",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataUeTac"

    """
)

UlBasebandCapacity = ReplaceableObject(
    'ericsson_cm_3g."UlBasebandCapacity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityLicenses_id",
        "vsDataUlBasebandCapacity_id",
        "licenseCapacityUlBbCapacity",
        "capacityUnitUlBbCapacity",
        "keyIdUlBbCapacity",
        "licUlBbPercentileConf",
        "licenseStateUlBbCapacity"
    FROM
    ericsson_bulkcm."vsDataUlBasebandCapacity"

    """
)

UlCompGroup = ReplaceableObject(
    'ericsson_cm_3g."UlCompGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataUlCompGroup_id",
        "sectorCarrierRef",
        "administrativeState",
        "availabilityStatus",
        "operationalState"
    FROM
    ericsson_bulkcm."vsDataUlCompGroup"

    """
)

UlFss = ReplaceableObject(
    'ericsson_cm_3g."UlFss"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataUlFss_id",
        "featureStateUlFss",
        "keyIdUlFss",
        "licenseStateUlFss",
        "serviceStateUlFss"
    FROM
    ericsson_bulkcm."vsDataUlFss"

    """
)

UlPrbCapacity = ReplaceableObject(
    'ericsson_cm_3g."UlPrbCapacity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataCapacityLicenses_id",
        "vsDataUlPrbCapacity_id",
        "capacityUnitUlPrbCapacity",
        "keyIdUlPrbCapacity",
        "licUlPrbPercentileConf",
        "licenseCapacityUlPrbCapacity",
        "licenseStateUlPrbCapacity"
    FROM
    ericsson_bulkcm."vsDataUlPrbCapacity"

    """
)

UniSaalProfile = ReplaceableObject(
    'ericsson_cm_3g."UniSaalProfile"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataUniSaalProfile_id",
        "userLabel",
        "profileData_maxPD",
        "profileData_maxStat",
        "profileData_initialCredit",
        "profileData_timerKeepAlive",
        "profileData_timerNoResponse",
        "profileData_timerIdle",
        "profileData_timerCC",
        "profileData_timerPoll",
        "profileData_maxCC",
        "profileData_congestionOnSet",
        "profileData_congestionAbatement"
    FROM
    ericsson_bulkcm."vsDataUniSaalProfile"

    """
)

UniSaalTp = ReplaceableObject(
    'ericsson_cm_3g."UniSaalTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataUniSaalTp_id",
        "aal5TpVccTpId",
        "maxSduSize",
        "uniSaalProfileId",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataUniSaalTp"

    """
)

UpgradeTrace = ReplaceableObject(
    'ericsson_cm_3g."UpgradeTrace"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSwManagement_id",
        "vsDataUpgradeTrace_id",
        "fileSize",
        "flushInterval",
        "outputMode",
        "sendLogsAsNotifications"
    FROM
    ericsson_bulkcm."vsDataUpgradeTrace"

    """
)

Ura = ReplaceableObject(
    'ericsson_cm_3g."Ura"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUra_id",
        "userLabel",
        "uraIdentity"
    FROM
    ericsson_bulkcm."vsDataUra"

    """
)

UserIdentity = ReplaceableObject(
    'ericsson_cm_3g."UserIdentity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "vsDataUserIdentity_id",
        "userName"
    FROM
    ericsson_bulkcm."vsDataUserIdentity"

    """
)

UserManagement = ReplaceableObject(
    'ericsson_cm_3g."UserManagement"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataUserManagement_id",
        "targetType",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataUserManagement"

    """
)

UtranCellRelation = ReplaceableObject(
    'ericsson_cm_3g."UtranCellRelation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUtranFreqRelation_id",
        "vsDataUtranCellRelation_id",
        "createdBy",
        "timeOfCreation",
        "adjacentCell",
        "coverageIndicator",
        "isHoAllowed",
        "isRemoveAllowed",
        "lastModification",
        "timeOfLastModification",
        "loadBalancing",
        "lbBnrAllowed",
        "lbCovIndicated"
    FROM
    ericsson_bulkcm."vsDataUtranCellRelation"

    """
)

UtraNetwork = ReplaceableObject(
    'ericsson_cm_3g."UtraNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataUtraNetwork_id",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataUtraNetwork"

    """
)

UtranFreqRelation = ReplaceableObject(
    'ericsson_cm_3g."UtranFreqRelation"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataENodeBFunction_id",
        "vsDataEUtranCellFDD_id",
        "vsDataUtranFreqRelation_id",
        "cellReselectionPriority",
        "pMaxUtra",
        "qQualMin",
        "qRxLevMin",
        "threshXHigh",
        "threshXLow",
        "userLabel",
        "adjacentFreq",
        "allowedPlmnList_mcc",
        "allowedPlmnList_mnc",
        "allowedPlmnList_mncLength",
        "connectedModeMobilityPrio",
        "csFallbackPrio",
        "qOffsetFreq",
        "csFallbackPrioEC",
        "mobilityAction",
        "mobilityActionCsfb",
        "threshXHighQ",
        "threshXLowQ",
        "voicePrio",
        "anrMeasOn",
        "utranFreqToQciProfileRelation",
        "maxNrUtranCellRelations",
        "lbBnrPolicy",
        "altCsfbTargetPrioEc",
        "altCsfbTargetPrio",
        "b2Thr1RsrqUtraFreqOffset",
        "b2Thr2RscpUtraFreqOffset",
        "b2Thr1RsrpUtraFreqOffset",
        "b2Thr2EcNoUtraFreqOffset",
        "atoAllowed",
        "allowedPlmnList",
        "utranFreqToQciProfileRelation_lbUtranB1ThresholdRscpOffset",
        "utranFreqToQciProfileRelation_lbQciProfileHandling",
        "utranFreqToQciProfileRelation_qciProfileRef"
    FROM
    ericsson_bulkcm."vsDataUtranFreqRelation"

    """
)

UtranNetwork = ReplaceableObject(
    'ericsson_cm_3g."UtranNetwork"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataUtranNetwork_id",
        "userLabel",
        "aliasPlmnIdentities_mcc",
        "aliasPlmnIdentities_mnc",
        "aliasPlmnIdentities_mncLength",
        "plmnIdentity_mcc",
        "plmnIdentity_mnc",
        "plmnIdentity_mncLength",
        "aliasPlmnIdentities"
    FROM
    ericsson_bulkcm."vsDataUtranNetwork"

    """
)

Vc4Ttp = ReplaceableObject(
    'ericsson_cm_3g."Vc4Ttp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "vsDataExchangeTerminal_id",
        "vsDataOs155SpiTtp_id",
        "vsDataVc4Ttp_id",
        "userLabel",
        "pathTraceFormat",
        "transmittedPathTrace",
        "expectedPathTrace",
        "timConsequentAction",
        "vcDegThreshold",
        "vcDegM",
        "auAisReporting",
        "vcRdiReporting"
    FROM
    ericsson_bulkcm."vsDataVc4Ttp"

    """
)

VclTp = ReplaceableObject(
    'ericsson_cm_3g."VclTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAtmPort_id",
        "vsDataVplTp_id",
        "vsDataVpcTp_id",
        "vsDataVclTp_id",
        "atmTrafficDescriptorId",
        "externalVci",
        "userLabel",
        "counterActivation"
    FROM
    ericsson_bulkcm."vsDataVclTp"

    """
)

VendorCredential = ReplaceableObject(
    'ericsson_cm_3g."VendorCredential"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataSecM_id",
        "vsDataCertM_id",
        "vsDataVendorCredential_id",
        "certificateState",
        "certificateContent_version",
        "certificateContent_serialNumber",
        "certificateContent_signatureAlgorithm",
        "certificateContent_issuer",
        "certificateContent_validFrom",
        "certificateContent_validTo",
        "certificateContent_publicKey",
        "certificateContent_publicKeyAlgorithm",
        "certificateContent_keyUsage",
        "certificateContent_subject"
    FROM
    ericsson_bulkcm."vsDataVendorCredential"

    """
)

VLAN = ReplaceableObject(
    'ericsson_cm_3g."VLAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEthernetSwitchFabric_id",
        "vsDataVlan_id",
        "userLabel",
        "vid",
        "vlanType"
    FROM
    ericsson_bulkcm."vsDataVLAN"

    """
)

VLANGroup = ReplaceableObject(
    'ericsson_cm_3g."VLANGroup"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataVLANGroup_id",
        "operationalState",
        "depLinkLayer"
    FROM
    ericsson_bulkcm."vsDataVLANGroup"

    """
)

VlanPort = ReplaceableObject(
    'ericsson_cm_3g."VlanPort"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransport_id",
        "vsDataVlanPort_id",
        "vsDataEquipment_id",
        "vsDataSubrack_id",
        "vsDataSlot_id",
        "vsDataPlugInUnit_id",
        "isTagged",
        "reservedBy",
        "vlanId",
        "userLabel",
        "encapsulation",
        "egressQosClassification",
        "egressQosMarking",
        "egressQosQueueMap",
        "ingressQosMarking",
        "portRef",
        "vid"
    FROM
    ericsson_bulkcm."vsDataVlanPort"

    """
)

VpcTp = ReplaceableObject(
    'ericsson_cm_3g."VpcTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAtmPort_id",
        "vsDataVplTp_id",
        "vsDataVpcTp_id",
        "alarmReport",
        "continuityCheck",
        "nomPmBlkSize",
        "userLabel",
        "counterMode"
    FROM
    ericsson_bulkcm."vsDataVpcTp"

    """
)

VplTp = ReplaceableObject(
    'ericsson_cm_3g."VplTp"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataTransportNetwork_id",
        "vsDataAtmPort_id",
        "vsDataVplTp_id",
        "atmTrafficDescriptor",
        "externalVpi",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataVplTp"

    """
)

VRF = ReplaceableObject(
    'ericsson_cm_3g."VRF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSTN_id",
        "vsDataVRF_id",
        "inUse",
        "vrfDescription"
    FROM
    ericsson_bulkcm."vsDataVRF"

    """
)

Vrrpv3Interface = ReplaceableObject(
    'ericsson_cm_3g."Vrrpv3Interface"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataVrrpv3Interface_id",
        "vrIdentity",
        "preemptHoldTime",
        "preemptMode",
        "advertiseInterval",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataVrrpv3Interface"

    """
)

Vrrpv3Session = ReplaceableObject(
    'ericsson_cm_3g."Vrrpv3Session"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataIpSystem_id",
        "vsDataIpRouter_id",
        "vsDataInterfaceIpv4_id",
        "vsDataVrrpv3Session_id",
        "prioritizedSession",
        "administrativeState",
        "vrrpv3InterfaceRef",
        "userLabel"
    FROM
    ericsson_bulkcm."vsDataVrrpv3Session"

    """
)

VswrSupervision = ReplaceableObject(
    'ericsson_cm_3g."VswrSupervision"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataVswrSupervision_id",
        "keyIdVswrSupervision",
        "featureStateVswrSupervision",
        "licenseStateVswrSupervision",
        "serviceStateVswrSupervision"
    FROM
    ericsson_bulkcm."vsDataVswrSupervision"

    """
)

WcdmaCarrier = ReplaceableObject(
    'ericsson_cm_3g."WcdmaCarrier"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataIurLink_id",
        "vsDataWcdmaCarrier_id",
        "userLabel",
        "defaultHoType",
        "freqBand",
        "sib5bisEnabled",
        "uarfcnDl",
        "thresh2dRwrDrnc",
        "barredCnOperatorRef"
    FROM
    ericsson_bulkcm."vsDataWcdmaCarrier"

    """
)

WcdmaHandover = ReplaceableObject(
    'ericsson_cm_3g."WcdmaHandover"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataWcdmaHandover_id",
        "featureStateWcdmaHandover",
        "keyIdWcdmaHandover",
        "licenseStateWcdmaHandover",
        "serviceStateWcdmaHandover"
    FROM
    ericsson_bulkcm."vsDataWcdmaHandover"

    """
)

WcdmaSessionContinuity = ReplaceableObject(
    'ericsson_cm_3g."WcdmaSessionContinuity"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataSystemFunctions_id",
        "vsDataLicensing_id",
        "vsDataOptionalFeatures_id",
        "vsDataWcdmaSessionContinuity_id",
        "keyIdWcdmaSessionContinuity",
        "featureStateWcdmaSessionContinuity",
        "licenseStateWcdmaSessionContinuity",
        "serviceStateWcdmaSessionContinuity"
    FROM
    ericsson_bulkcm."vsDataWcdmaSessionContinuity"

    """
)

WifiMobility = ReplaceableObject(
    'ericsson_cm_3g."WifiMobility"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "RncFunction_id",
        "vsDataWifiMobility_id",
        "thpBias",
        "apMax"
    FROM
    ericsson_bulkcm."vsDataWifiMobility"

    """
)

WifiModule = ReplaceableObject(
    'ericsson_cm_3g."WifiModule"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataRbsUnit_id",
        "vsDataWifiModule_id",
        "administrativeState",
        "encapsulation",
        "operationalState"
    FROM
    ericsson_bulkcm."vsDataWifiModule"

    """
)

XpProgram = ReplaceableObject(
    'ericsson_cm_3g."XpProgram"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "configData_dnPrefix",
        "SubNetwork_id",
        "SubNetwork_2_id",
        "MeContext_id",
        "ManagedElement_id",
        "vsDataEquipment_id",
        "vsDataAuxPlugInUnit_id",
        "vsDataDeviceGroup_id",
        "vsDataXpProgram_id",
        "vsDataRbsSubrack_id",
        "vsDataRbsSlot_id",
        "startState"
    FROM
    ericsson_bulkcm."vsDataXpProgram"

    """
)


def upgrade():
    op.create_view(AlarmIRP)
    op.create_view(BulkCmIRP)
    op.create_view(ExternalGsmCell)
    op.create_view(ExternalUtranCell)
    op.create_view(GsmRelation)
    op.create_view(IRPAgent)
    op.create_view(IubLink)
    op.create_view(ManagedElement)
    op.create_view(ManagementNode)
    op.create_view(MeContext)
    op.create_view(NodeBFunction)
    op.create_view(NotificationIRP)
    op.create_view(RncFunction)
    op.create_view(SubNetwork)
    op.create_view(SubNetwork_2)
    op.create_view(UtranCell)
    op.create_view(UtranRelation)
    op.create_view(Aal0TpVccTp)
    op.create_view(Aal2Ap)
    op.create_view(Aal2PathDistributionUnit)
    op.create_view(Aal2PathVccTp)
    op.create_view(Aal2QosCodePointProfile)
    op.create_view(Aal2QosProfile)
    op.create_view(Aal2RoutingCase)
    op.create_view(Aal2Sp)
    op.create_view(Aal5TpVccTp)
    op.create_view(AccessControlList)
    op.create_view(AddressIPv4)
    op.create_view(AdmissionControl)
    op.create_view(AdvCellSup)
    op.create_view(AgpsPositioning)
    op.create_view(AiDevice)
    op.create_view(AiDeviceSet)
    op.create_view(AirIfLoadGenerator)
    op.create_view(AirIfLoadProfile)
    op.create_view(Aisgv2FwDownload)
    op.create_view(AlarmPort)
    op.create_view(AmoFunction)
    op.create_view(Anr)
    op.create_view(AnrFunction)
    op.create_view(AnrFunctionCdma20001xRtt)
    op.create_view(AnrFunctionEUtran)
    op.create_view(AnrFunctionGeran)
    op.create_view(AnrFunctionUtran)
    op.create_view(AnrIafUtran)
    op.create_view(AntennaBranch)
    op.create_view(AntennaNearUnit)
    op.create_view(AntennaSubunit)
    op.create_view(AntennaUnit)
    op.create_view(AntennaUnitGroup)
    op.create_view(AntFeederCable)
    op.create_view(Areas)
    op.create_view(ArpMap)
    op.create_view(ArpQosClassProfile)
    op.create_view(AtmConfService)
    op.create_view(AtmPort)
    op.create_view(AtmTrafficDescriptor)
    op.create_view(AuPort)
    op.create_view(AuthenticationOrder)
    op.create_view(AuthorizationOrder)
    op.create_view(AutoCellCapEstFunction)
    op.create_view(AutonomousMode)
    op.create_view(AutoProvisioning)
    op.create_view(AuxPlugInUnit)
    op.create_view(BatteryBackup)
    op.create_view(BbProcessingResource)
    op.create_view(BestNeighborSI)
    op.create_view(BfdProfile)
    op.create_view(BoundaryOrdinaryClock)
    op.create_view(Bridge)
    op.create_view(BrM)
    op.create_view(BrmBackup)
    op.create_view(BrmBackupHousekeeping)
    op.create_view(BrmBackupLabelStore)
    op.create_view(BrmBackupManager)
    op.create_view(BrmBackupScheduler)
    op.create_view(BrmCalendarBasedPeriodicEvent)
    op.create_view(BrmFailsafeBackup)
    op.create_view(BrmPeriodicEvent)
    op.create_view(BrmRollbackAtRestore)
    op.create_view(BrmSingleEvent)
    op.create_view(Cabinet)
    op.create_view(CapacityChannelBandwidth)
    op.create_view(CapacityConnectedUsers)
    op.create_view(CapacityFeatureLicense)
    op.create_view(CapacityKey)
    op.create_view(CapacityLicenses)
    op.create_view(CapacityState)
    op.create_view(Carrier)
    op.create_view(CarrierAggregationFunction)
    op.create_view(CaxFanUnit)
    op.create_view(Cbu)
    op.create_view(CchFrameSynch)
    op.create_view(Cdma2000SessionContinuity)
    op.create_view(CellResources)
    op.create_view(CellSleepFunction)
    op.create_view(CellSleepNodeFunction)
    op.create_view(CertM)
    op.create_view(CertMCapabilities)
    op.create_view(ChannelSwitching)
    op.create_view(Climate)
    op.create_view(CliSsh)
    op.create_view(CliTls)
    op.create_view(CnOperator)
    op.create_view(CombinedCell)
    op.create_view(CommonChannelResourcesDl)
    op.create_view(CommonChannelResourcesUl)
    op.create_view(CommunicationContexts)
    op.create_view(ConfigurationVersion)
    op.create_view(CoverageRelation)
    op.create_view(CpriLinkSupervision)
    op.create_view(CsfbForLimitedDualRadioUE)
    op.create_view(CsfbToGeranUtran)
    op.create_view(DataCollectionGeneration)
    op.create_view(DataRadioBearer)
    op.create_view(DateAndTime)
    op.create_view(DBSAndSabe)
    op.create_view(DchFrameSynch)
    op.create_view(DeviceGroup)
    op.create_view(Dhcp)
    op.create_view(DifferentiatedAdmissionControl)
    op.create_view(DlBasebandCapacity)
    op.create_view(DlFss)
    op.create_view(DlPrbCapacity)
    op.create_view(DnsClient)
    op.create_view(DownlinkBaseBandPool)
    op.create_view(Drx)
    op.create_view(DrxProfile)
    op.create_view(Dst)
    op.create_view(DualAntDlPerfPkg)
    op.create_view(DualLayBeamfPerfPkg)
    op.create_view(DynamicGBRAdmCtrl)
    op.create_view(DynamicQoSModification)
    op.create_view(E1PhysPathTerm)
    op.create_view(EcBus)
    op.create_view(EcPort)
    op.create_view(EcsCsfb)
    op.create_view(EDchResources)
    op.create_view(EmergencyUnlock)
    op.create_view(EnergyMeter)
    op.create_view(EnhCellIdInTraces)
    op.create_view(ENodeBFunction)
    op.create_view(EnrollmentAuthority)
    op.create_view(EnrollmentServer)
    op.create_view(EnrollmentServerGroup)
    op.create_view(Equipment)
    op.create_view(EquipmentClockReference)
    op.create_view(EquipmentDiscovery)
    op.create_view(EquipmentSupportFunction)
    op.create_view(EricssonFilter)
    op.create_view(EthernetBridgePort)
    op.create_view(EthernetInterface)
    op.create_view(EthernetLink)
    op.create_view(EthernetPort)
    op.create_view(EthernetSwitch)
    op.create_view(EthernetSwitchFabric)
    op.create_view(EthernetSwitchingAdm)
    op.create_view(EthernetSwitchModule)
    op.create_view(EthernetSwitchModulePort)
    op.create_view(EthernetSwitchPort)
    op.create_view(Etws)
    op.create_view(Eul)
    op.create_view(EUtranCellRelation)
    op.create_view(EUtraNetwork)
    op.create_view(EUtranFreqRelation)
    op.create_view(EUtranFrequency)
    op.create_view(EventCapabilities)
    op.create_view(EventProducer)
    op.create_view(ExchangeTerminal)
    op.create_view(ExchangeTerminalIp)
    op.create_view(ExternalENodeBFunction)
    op.create_view(ExternalEUtranCellFDD)
    op.create_view(ExternalEutranFrequency)
    op.create_view(ExternalEUtranPlmn)
    op.create_view(ExternalGsmFreq)
    op.create_view(ExternalGsmFreqGroup)
    op.create_view(ExternalGsmPlmn)
    op.create_view(ExternalNode)
    op.create_view(ExternalUtranFreq)
    op.create_view(ExternalUtranPlmn)
    op.create_view(Fach)
    op.create_view(FanGroup)
    op.create_view(FeatureKey)
    op.create_view(FeatureState)
    op.create_view(FieldReplaceableUnit)
    op.create_view(FilePullCapabilities)
    op.create_view(FileTPM)
    op.create_view(Filter)
    op.create_view(Fm)
    op.create_view(FmAlarmModel)
    op.create_view(FmAlarmType)
    op.create_view(FmSubscription)
    op.create_view(FreqManagement)
    op.create_view(FrequencySyncIO)
    op.create_view(FtpTls)
    op.create_view(FtpTlsServer)
    op.create_view(GeneralProcessorUnit)
    op.create_view(GeranCellRelation)
    op.create_view(GeraNetwork)
    op.create_view(GeranFreqGroupRelation)
    op.create_view(GigaBitEthernet)
    op.create_view(GnssInfo)
    op.create_view(Gpeh)
    op.create_view(GpsOutSyncLink)
    op.create_view(GpsSyncRef)
    op.create_view(GracePeriod)
    op.create_view(GsmSessionContinuity)
    op.create_view(GtpPath)
    op.create_view(Handover)
    op.create_view(HighSpeedUE)
    op.create_view(HoOscCtrlUE)
    op.create_view(Host)
    op.create_view(HoWhiteList)
    op.create_view(Hsdsch)
    op.create_view(HsDschResources)
    op.create_view(HttpM)
    op.create_view(Https)
    op.create_view(HwInventory)
    op.create_view(HwItem)
    op.create_view(HwUnit)
    op.create_view(ImaGroup)
    op.create_view(ImaLink)
    op.create_view(ImeisvTable)
    op.create_view(IntegrationUnlock)
    op.create_view(InterfaceIPv4)
    op.create_view(InterFrequencyLoadBalancing)
    op.create_view(InterFrequencyLTEHandover)
    op.create_view(InterFrequencySessionContinuity)
    op.create_view(InternalEthernetPort)
    op.create_view(IntraLTEHODataFwd)
    op.create_view(Ip)
    op.create_view(IpAccessHostEt)
    op.create_view(IpAccessHostGpb)
    op.create_view(IpAccessHostPool)
    op.create_view(IpAccessHostSpb)
    op.create_view(IpAccessSctp)
    op.create_view(IpAtmLink)
    op.create_view(IpEthPacketDataRouter)
    op.create_view(IpFlowMonitor)
    op.create_view(IpHostLink)
    op.create_view(IpInterface)
    op.create_view(IpLicensing)
    op.create_view(IpOam)
    op.create_view(Ippm)
    op.create_view(IpRoute)
    op.create_view(IpRouter)
    op.create_view(IpRouteSys)
    op.create_view(IpRoutingTable)
    op.create_view(IpSec)
    op.create_view(IpSyncRef)
    op.create_view(IpSystem)
    op.create_view(Ipv4DestNetwork)
    op.create_view(Ipv4Peer)
    op.create_view(Ipv4StaticRoute)
    op.create_view(Ipv4StaticRouteTable)
    op.create_view(IPv6RoutingTable)
    op.create_view(Irc)
    op.create_view(Iub)
    op.create_view(IubDataStreams)
    op.create_view(IubEdch)
    op.create_view(IuLink)
    op.create_view(IurLink)
    op.create_view(KeyFileInformation)
    op.create_view(KeyFileManagement)
    op.create_view(Lag)
    op.create_view(Ldap)
    op.create_view(LdapAuthenticationMethod)
    op.create_view(Licensing)
    op.create_view(LinkTransmissionProfile)
    op.create_view(Lm)
    op.create_view(LoadBalancingFunction)
    op.create_view(LoadControl)
    op.create_view(LocationArea)
    op.create_view(Log)
    op.create_view(LogicalChannelGroup)
    op.create_view(LogM)
    op.create_view(LppaEcid)
    op.create_view(LsmEcs)
    op.create_view(M3uAssociation)
    op.create_view(MACConfiguration)
    op.create_view(MaintenanceUser)
    op.create_view(MaintenanceUserSecurity)
    op.create_view(ManagedElementData)
    op.create_view(MaximumCellRange)
    op.create_view(MbmsM3Based)
    op.create_view(MbmsServiceArea)
    op.create_view(MdtConfiguration)
    op.create_view(MeasurementDefinition)
    op.create_view(MediumAccessUnit)
    op.create_view(MibManager)
    op.create_view(MimoSleepFunction)
    op.create_view(MixedMode)
    op.create_view(MobCtrlAtPoorCov)
    op.create_view(MocnCellProfile)
    op.create_view(MpClusterHandling)
    op.create_view(MpProcessingResource)
    op.create_view(Mtp3bAp)
    op.create_view(Mtp3bSlItu)
    op.create_view(Mtp3bSls)
    op.create_view(Mtp3bSpItu)
    op.create_view(Mtp3bSr)
    op.create_view(Mtp3bSrs)
    op.create_view(MultiCarrier)
    op.create_view(MulticastAntennaBranch)
    op.create_view(MultiErabsPerUser)
    op.create_view(NbapCommon)
    op.create_view(NbapDedicated)
    op.create_view(NetconfSsh)
    op.create_view(NetconfTls)
    op.create_view(NextHop)
    op.create_view(NniSaalProfile)
    op.create_view(NniSaalTp)
    op.create_view(NodeBLocalCell)
    op.create_view(NodeBLocalCellGroup)
    op.create_view(NodeBSectorCarrier)
    op.create_view(NodeCredential)
    op.create_view(NodeFunction)
    op.create_view(NodeGroupSyncMember)
    op.create_view(NodeManagementFunction)
    op.create_view(NodeSupport)
    op.create_view(NodeSynch)
    op.create_view(NonPlannedPciDrxProfile)
    op.create_view(Ntp)
    op.create_view(NtpFrequencySync)
    op.create_view(NtpServer)
    op.create_view(OamAccessPoint)
    op.create_view(OamTrafficClass)
    op.create_view(OctAntUlPerfPkg)
    op.create_view(OnSiteActivities)
    op.create_view(OperatorDefinedQci)
    op.create_view(OpProfiles)
    op.create_view(OptionalFeatureLicense)
    op.create_view(OptionalFeatures)
    op.create_view(Os155SpiTtp)
    op.create_view(OtdoaSupl)
    op.create_view(PacketFrequencySyncRef)
    op.create_view(Paging)
    op.create_view(Pch)
    op.create_view(Pci)
    op.create_view(PcpSetToQueue)
    op.create_view(PcpToQueueMap)
    op.create_view(PdrDevice)
    op.create_view(PeerIPv4)
    op.create_view(Pfs)
    op.create_view(PiuDevice)
    op.create_view(Plmn)
    op.create_view(PlmnIdentityGroup)
    op.create_view(PlugInUnit)
    op.create_view(Pm)
    op.create_view(PmEventM)
    op.create_view(PmEventService)
    op.create_view(PmInitiatedUeMeasurements)
    op.create_view(PmMeasurementCapabilities)
    op.create_view(PmService)
    op.create_view(PmSupport)
    op.create_view(PmUeMeasControl)
    op.create_view(PmUlInterferenceReport)
    op.create_view(PositioningServiceClass)
    op.create_view(PowerControl)
    op.create_view(PowerDistribution)
    op.create_view(PowerSupply)
    op.create_view(PredefRbsScannerGpeh)
    op.create_view(PreschedulingProfile)
    op.create_view(ProcessorLoad)
    op.create_view(Ptp)
    op.create_view(PtpBcOcPort)
    op.create_view(Pws)
    op.create_view(QciProfilePredefined)
    op.create_view(QciTable)
    op.create_view(QosAwareScheduler)
    op.create_view(QoSClassifier)
    op.create_view(QosPolicy)
    op.create_view(QosProfiles)
    op.create_view(QuadAntUlPerfPkg)
    op.create_view(Queue)
    op.create_view(QueueSystem)
    op.create_view(RabHandling)
    op.create_view(Rach)
    op.create_view(RadioBearerTable)
    op.create_view(RadioEquipmentClock)
    op.create_view(RadioEquipmentClockReference)
    op.create_view(RadioLinks)
    op.create_view(RadioUnitCascading)
    op.create_view(Ranap)
    op.create_view(RateShaping)
    op.create_view(RbsEventStreamer)
    op.create_view(RbsLocalCell)
    op.create_view(RbsMeasControl)
    op.create_view(RbsSlot)
    op.create_view(RbsSubrack)
    op.create_view(RbsSynchronization)
    op.create_view(RbsUnit)
    op.create_view(Rcs)
    op.create_view(RdiPort)
    op.create_view(RealTimeSecLog)
    op.create_view(RedirectWithNacc)
    op.create_view(ReliableProgramUniter)
    op.create_view(ReportConfigA1)
    op.create_view(ReportConfigA1Prim)
    op.create_view(ReportConfigA1Sec)
    op.create_view(ReportConfigA4)
    op.create_view(ReportConfigA5)
    op.create_view(ReportConfigA5Anr)
    op.create_view(ReportConfigA5DlComp)
    op.create_view(ReportConfigA5SoftLock)
    op.create_view(ReportConfigA5UlTrig)
    op.create_view(ReportConfigB1Geran)
    op.create_view(ReportConfigB1Utra)
    op.create_view(ReportConfigB2Cdma2000)
    op.create_view(ReportConfigB2Cdma20001xRtt)
    op.create_view(ReportConfigB2CdmaRttUlTrig)
    op.create_view(ReportConfigB2CdmaUlTrig)
    op.create_view(ReportConfigB2Geran)
    op.create_view(ReportConfigB2GeranUlTrig)
    op.create_view(ReportConfigB2Utra)
    op.create_view(ReportConfigB2UtraUlTrig)
    op.create_view(ReportConfigCsfbCdma2000)
    op.create_view(ReportConfigCsfbGeran)
    op.create_view(ReportConfigCsfbUtra)
    op.create_view(ReportConfigCsg)
    op.create_view(ReportConfigEUtraBadCovPrim)
    op.create_view(ReportConfigEUtraBadCovSec)
    op.create_view(ReportConfigEUtraBestCell)
    op.create_view(ReportConfigEUtraBestCellAnr)
    op.create_view(ReportConfigEUtraIFA3UlTrig)
    op.create_view(ReportConfigEUtraIFBestCell)
    op.create_view(ReportConfigEUtraInterFreqLb)
    op.create_view(ReportConfigEUtraInterFreqMbms)
    op.create_view(ReportConfigEUtraIntraFreqPm)
    op.create_view(ReportConfigInterRatLb)
    op.create_view(ReportConfigSCellA1A2)
    op.create_view(ReportConfigSCellA4)
    op.create_view(ReportConfigSCellA6)
    op.create_view(ReportConfigSearch)
    op.create_view(ResMeasControl)
    op.create_view(ResourcePartitions)
    op.create_view(RetCascading)
    op.create_view(RetConfigurationMgt)
    op.create_view(RetDevice)
    op.create_view(RetDeviceSet)
    op.create_view(RetSubUnit)
    op.create_view(RetSupport)
    op.create_view(RetuDeviceGroup)
    op.create_view(RfBranch)
    op.create_view(RfPort)
    op.create_view(RiLink)
    op.create_view(RiPort)
    op.create_view(RlcUm)
    op.create_view(RlfProfile)
    op.create_view(RncCapacity)
    op.create_view(RncConfigLimits)
    op.create_view(RncFeature)
    op.create_view(RncModule)
    op.create_view(RnlQosClassProfile)
    op.create_view(Rnsap)
    op.create_view(ROHC)
    op.create_view(Router)
    op.create_view(RouteTableIPv4Static)
    op.create_view(RoutingArea)
    op.create_view(RoutingTable)
    op.create_view(Rps)
    op.create_view(Rrc)
    op.create_view(RruDeviceGroup)
    op.create_view(RttPositioning)
    op.create_view(S1HODataFwd)
    op.create_view(SasPositioning)
    op.create_view(SccpApLocal)
    op.create_view(SccpApRemote)
    op.create_view(SccpScrc)
    op.create_view(SccpSp)
    op.create_view(SchedulerSp)
    op.create_view(Schema)
    op.create_view(Sctp)
    op.create_view(SctpAssociation)
    op.create_view(SctpEndpoint)
    op.create_view(SctpProfile)
    op.create_view(SecM)
    op.create_view(Sector)
    op.create_view(SectorAntenna)
    op.create_view(SectorCarrier)
    op.create_view(SectorEquipmentFunction)
    op.create_view(Security)
    op.create_view(SecurityHandling)
    op.create_view(ServiceArea)
    op.create_view(ServiceSpecificDRX)
    op.create_view(ServiceTriggeredMobility)
    op.create_view(SfpModule)
    op.create_view(Sftp)
    op.create_view(Shaper)
    op.create_view(SharedNetworkSupport)
    op.create_view(Sid)
    op.create_view(SignalingRadioBearer)
    op.create_view(SingLayBeamfPerfPkg)
    op.create_view(Site)
    op.create_view(Slot)
    op.create_view(Snmp)
    op.create_view(SnmpTargetV2C)
    op.create_view(SnmpTargetV3)
    op.create_view(SpDevicePool)
    op.create_view(SpidHoWhiteList)
    op.create_view(SpidRATFreqPrio)
    op.create_view(SpiQosClass)
    op.create_view(SRVCCtoUTRAN)
    op.create_view(STN)
    op.create_view(StnFunction)
    op.create_view(StreamingCapabilities)
    op.create_view(Subrack)
    op.create_view(SubscriberProfileID)
    op.create_view(SubscrProfileIdHandling)
    op.create_view(Support12Cells)
    op.create_view(Support6Cells)
    op.create_view(SwAllocation)
    op.create_view(SwInventory)
    op.create_view(SwitchCoreUnit)
    op.create_view(SwitchInternalLinkPort)
    op.create_view(SwitchPortStp)
    op.create_view(SwitchStp)
    op.create_view(SwItem)
    op.create_view(SwM)
    op.create_view(SwManagement)
    op.create_view(SwVersion)
    op.create_view(Synchronization)
    op.create_view(SyncPort)
    op.create_view(SyncServer)
    op.create_view(SysM)
    op.create_view(SystemFunctions)
    op.create_view(TCPOptimization)
    op.create_view(TdScdmaSessionContinuity)
    op.create_view(TempSensor)
    op.create_view(TermPointToENB)
    op.create_view(TermPointToMme)
    op.create_view(TermPointToSGW)
    op.create_view(TimeM)
    op.create_view(TimeServer)
    op.create_view(TimeSetting)
    op.create_view(TimeSettings)
    op.create_view(TimeSyncIO)
    op.create_view(TimingUnit)
    op.create_view(Tls)
    op.create_view(Tm7ModeSwitching)
    op.create_view(TmaSupport)
    op.create_view(TnApplication)
    op.create_view(TnlCchQosClassProfile)
    op.create_view(TnlDchQosClassProfile)
    op.create_view(TnlHspaQosClassProfile)
    op.create_view(TnlIuQosClassProfile)
    op.create_view(TnlQosClass)
    op.create_view(TnPort)
    op.create_view(TpaDevice)
    op.create_view(TpaDeviceSet)
    op.create_view(TrafficAwarePowerSave)
    op.create_view(TrafficClass)
    op.create_view(TrafficClassPsInt)
    op.create_view(TrafficManagement)
    op.create_view(TrafficManager)
    op.create_view(TrafficScheduler)
    op.create_view(Transceiver)
    op.create_view(Transport)
    op.create_view(TransportNetwork)
    op.create_view(TrustCategory)
    op.create_view(TrustedCertificate)
    op.create_view(TtiBundling)
    op.create_view(TuSyncRef)
    op.create_view(TwampResponder)
    op.create_view(TxDataCloning)
    op.create_view(TxDeviceGroup)
    op.create_view(UeMeasControl)
    op.create_view(UePosCellId)
    op.create_view(UePositioning)
    op.create_view(UeRabType)
    op.create_view(UeRc)
    op.create_view(UeRcEdchFlow)
    op.create_view(UeRcPhyChEdch)
    op.create_view(UeRcRab)
    op.create_view(UeRcTrCh)
    op.create_view(UeRrcType)
    op.create_view(UeTac)
    op.create_view(UlBasebandCapacity)
    op.create_view(UlCompGroup)
    op.create_view(UlFss)
    op.create_view(UlPrbCapacity)
    op.create_view(UniSaalProfile)
    op.create_view(UniSaalTp)
    op.create_view(UpgradeTrace)
    op.create_view(Ura)
    op.create_view(UserIdentity)
    op.create_view(UserManagement)
    op.create_view(UtranCellRelation)
    op.create_view(UtraNetwork)
    op.create_view(UtranFreqRelation)
    op.create_view(UtranNetwork)
    op.create_view(Vc4Ttp)
    op.create_view(VclTp)
    op.create_view(VendorCredential)
    op.create_view(VLAN)
    op.create_view(VLANGroup)
    op.create_view(VlanPort)
    op.create_view(VpcTp)
    op.create_view(VplTp)
    op.create_view(VRF)
    op.create_view(Vrrpv3Interface)
    op.create_view(Vrrpv3Session)
    op.create_view(VswrSupervision)
    op.create_view(WcdmaCarrier)
    op.create_view(WcdmaHandover)
    op.create_view(WcdmaSessionContinuity)
    op.create_view(WifiMobility)
    op.create_view(WifiModule)
    op.create_view(XpProgram)


def downgrade():
    op.drop_view(AlarmIRP)
    op.drop_view(BulkCmIRP)
    op.drop_view(ExternalGsmCell)
    op.drop_view(ExternalUtranCell)
    op.drop_view(GsmRelation)
    op.drop_view(IRPAgent)
    op.drop_view(IubLink)
    op.drop_view(ManagedElement)
    op.drop_view(ManagementNode)
    op.drop_view(MeContext)
    op.drop_view(NodeBFunction)
    op.drop_view(NotificationIRP)
    op.drop_view(RncFunction)
    op.drop_view(SubNetwork)
    op.drop_view(SubNetwork_2)
    op.drop_view(UtranCell)
    op.drop_view(UtranRelation)
    op.drop_view(Aal0TpVccTp)
    op.drop_view(Aal2Ap)
    op.drop_view(Aal2PathDistributionUnit)
    op.drop_view(Aal2PathVccTp)
    op.drop_view(Aal2QosCodePointProfile)
    op.drop_view(Aal2QosProfile)
    op.drop_view(Aal2RoutingCase)
    op.drop_view(Aal2Sp)
    op.drop_view(Aal5TpVccTp)
    op.drop_view(AccessControlList)
    op.drop_view(AddressIPv4)
    op.drop_view(AdmissionControl)
    op.drop_view(AdvCellSup)
    op.drop_view(AgpsPositioning)
    op.drop_view(AiDevice)
    op.drop_view(AiDeviceSet)
    op.drop_view(AirIfLoadGenerator)
    op.drop_view(AirIfLoadProfile)
    op.drop_view(Aisgv2FwDownload)
    op.drop_view(AlarmPort)
    op.drop_view(AmoFunction)
    op.drop_view(Anr)
    op.drop_view(AnrFunction)
    op.drop_view(AnrFunctionCdma20001xRtt)
    op.drop_view(AnrFunctionEUtran)
    op.drop_view(AnrFunctionGeran)
    op.drop_view(AnrFunctionUtran)
    op.drop_view(AnrIafUtran)
    op.drop_view(AntennaBranch)
    op.drop_view(AntennaNearUnit)
    op.drop_view(AntennaSubunit)
    op.drop_view(AntennaUnit)
    op.drop_view(AntennaUnitGroup)
    op.drop_view(AntFeederCable)
    op.drop_view(Areas)
    op.drop_view(ArpMap)
    op.drop_view(ArpQosClassProfile)
    op.drop_view(AtmConfService)
    op.drop_view(AtmPort)
    op.drop_view(AtmTrafficDescriptor)
    op.drop_view(AuPort)
    op.drop_view(AuthenticationOrder)
    op.drop_view(AuthorizationOrder)
    op.drop_view(AutoCellCapEstFunction)
    op.drop_view(AutonomousMode)
    op.drop_view(AutoProvisioning)
    op.drop_view(AuxPlugInUnit)
    op.drop_view(BatteryBackup)
    op.drop_view(BbProcessingResource)
    op.drop_view(BestNeighborSI)
    op.drop_view(BfdProfile)
    op.drop_view(BoundaryOrdinaryClock)
    op.drop_view(Bridge)
    op.drop_view(BrM)
    op.drop_view(BrmBackup)
    op.drop_view(BrmBackupHousekeeping)
    op.drop_view(BrmBackupLabelStore)
    op.drop_view(BrmBackupManager)
    op.drop_view(BrmBackupScheduler)
    op.drop_view(BrmCalendarBasedPeriodicEvent)
    op.drop_view(BrmFailsafeBackup)
    op.drop_view(BrmPeriodicEvent)
    op.drop_view(BrmRollbackAtRestore)
    op.drop_view(BrmSingleEvent)
    op.drop_view(Cabinet)
    op.drop_view(CapacityChannelBandwidth)
    op.drop_view(CapacityConnectedUsers)
    op.drop_view(CapacityFeatureLicense)
    op.drop_view(CapacityKey)
    op.drop_view(CapacityLicenses)
    op.drop_view(CapacityState)
    op.drop_view(Carrier)
    op.drop_view(CarrierAggregationFunction)
    op.drop_view(CaxFanUnit)
    op.drop_view(Cbu)
    op.drop_view(CchFrameSynch)
    op.drop_view(Cdma2000SessionContinuity)
    op.drop_view(CellResources)
    op.drop_view(CellSleepFunction)
    op.drop_view(CellSleepNodeFunction)
    op.drop_view(CertM)
    op.drop_view(CertMCapabilities)
    op.drop_view(ChannelSwitching)
    op.drop_view(Climate)
    op.drop_view(CliSsh)
    op.drop_view(CliTls)
    op.drop_view(CnOperator)
    op.drop_view(CombinedCell)
    op.drop_view(CommonChannelResourcesDl)
    op.drop_view(CommonChannelResourcesUl)
    op.drop_view(CommunicationContexts)
    op.drop_view(ConfigurationVersion)
    op.drop_view(CoverageRelation)
    op.drop_view(CpriLinkSupervision)
    op.drop_view(CsfbForLimitedDualRadioUE)
    op.drop_view(CsfbToGeranUtran)
    op.drop_view(DataCollectionGeneration)
    op.drop_view(DataRadioBearer)
    op.drop_view(DateAndTime)
    op.drop_view(DBSAndSabe)
    op.drop_view(DchFrameSynch)
    op.drop_view(DeviceGroup)
    op.drop_view(Dhcp)
    op.drop_view(DifferentiatedAdmissionControl)
    op.drop_view(DlBasebandCapacity)
    op.drop_view(DlFss)
    op.drop_view(DlPrbCapacity)
    op.drop_view(DnsClient)
    op.drop_view(DownlinkBaseBandPool)
    op.drop_view(Drx)
    op.drop_view(DrxProfile)
    op.drop_view(Dst)
    op.drop_view(DualAntDlPerfPkg)
    op.drop_view(DualLayBeamfPerfPkg)
    op.drop_view(DynamicGBRAdmCtrl)
    op.drop_view(DynamicQoSModification)
    op.drop_view(E1PhysPathTerm)
    op.drop_view(EcBus)
    op.drop_view(EcPort)
    op.drop_view(EcsCsfb)
    op.drop_view(EDchResources)
    op.drop_view(EmergencyUnlock)
    op.drop_view(EnergyMeter)
    op.drop_view(EnhCellIdInTraces)
    op.drop_view(ENodeBFunction)
    op.drop_view(EnrollmentAuthority)
    op.drop_view(EnrollmentServer)
    op.drop_view(EnrollmentServerGroup)
    op.drop_view(Equipment)
    op.drop_view(EquipmentClockReference)
    op.drop_view(EquipmentDiscovery)
    op.drop_view(EquipmentSupportFunction)
    op.drop_view(EricssonFilter)
    op.drop_view(EthernetBridgePort)
    op.drop_view(EthernetInterface)
    op.drop_view(EthernetLink)
    op.drop_view(EthernetPort)
    op.drop_view(EthernetSwitch)
    op.drop_view(EthernetSwitchFabric)
    op.drop_view(EthernetSwitchingAdm)
    op.drop_view(EthernetSwitchModule)
    op.drop_view(EthernetSwitchModulePort)
    op.drop_view(EthernetSwitchPort)
    op.drop_view(Etws)
    op.drop_view(Eul)
    op.drop_view(EUtranCellRelation)
    op.drop_view(EUtraNetwork)
    op.drop_view(EUtranFreqRelation)
    op.drop_view(EUtranFrequency)
    op.drop_view(EventCapabilities)
    op.drop_view(EventProducer)
    op.drop_view(ExchangeTerminal)
    op.drop_view(ExchangeTerminalIp)
    op.drop_view(ExternalENodeBFunction)
    op.drop_view(ExternalEUtranCellFDD)
    op.drop_view(ExternalEutranFrequency)
    op.drop_view(ExternalEUtranPlmn)
    op.drop_view(ExternalGsmFreq)
    op.drop_view(ExternalGsmFreqGroup)
    op.drop_view(ExternalGsmPlmn)
    op.drop_view(ExternalNode)
    op.drop_view(ExternalUtranFreq)
    op.drop_view(ExternalUtranPlmn)
    op.drop_view(Fach)
    op.drop_view(FanGroup)
    op.drop_view(FeatureKey)
    op.drop_view(FeatureState)
    op.drop_view(FieldReplaceableUnit)
    op.drop_view(FilePullCapabilities)
    op.drop_view(FileTPM)
    op.drop_view(Filter)
    op.drop_view(Fm)
    op.drop_view(FmAlarmModel)
    op.drop_view(FmAlarmType)
    op.drop_view(FmSubscription)
    op.drop_view(FreqManagement)
    op.drop_view(FrequencySyncIO)
    op.drop_view(FtpTls)
    op.drop_view(FtpTlsServer)
    op.drop_view(GeneralProcessorUnit)
    op.drop_view(GeranCellRelation)
    op.drop_view(GeraNetwork)
    op.drop_view(GeranFreqGroupRelation)
    op.drop_view(GigaBitEthernet)
    op.drop_view(GnssInfo)
    op.drop_view(Gpeh)
    op.drop_view(GpsOutSyncLink)
    op.drop_view(GpsSyncRef)
    op.drop_view(GracePeriod)
    op.drop_view(GsmSessionContinuity)
    op.drop_view(GtpPath)
    op.drop_view(Handover)
    op.drop_view(HighSpeedUE)
    op.drop_view(HoOscCtrlUE)
    op.drop_view(Host)
    op.drop_view(HoWhiteList)
    op.drop_view(Hsdsch)
    op.drop_view(HsDschResources)
    op.drop_view(HttpM)
    op.drop_view(Https)
    op.drop_view(HwInventory)
    op.drop_view(HwItem)
    op.drop_view(HwUnit)
    op.drop_view(ImaGroup)
    op.drop_view(ImaLink)
    op.drop_view(ImeisvTable)
    op.drop_view(IntegrationUnlock)
    op.drop_view(InterfaceIPv4)
    op.drop_view(InterFrequencyLoadBalancing)
    op.drop_view(InterFrequencyLTEHandover)
    op.drop_view(InterFrequencySessionContinuity)
    op.drop_view(InternalEthernetPort)
    op.drop_view(IntraLTEHODataFwd)
    op.drop_view(Ip)
    op.drop_view(IpAccessHostEt)
    op.drop_view(IpAccessHostGpb)
    op.drop_view(IpAccessHostPool)
    op.drop_view(IpAccessHostSpb)
    op.drop_view(IpAccessSctp)
    op.drop_view(IpAtmLink)
    op.drop_view(IpEthPacketDataRouter)
    op.drop_view(IpFlowMonitor)
    op.drop_view(IpHostLink)
    op.drop_view(IpInterface)
    op.drop_view(IpLicensing)
    op.drop_view(IpOam)
    op.drop_view(Ippm)
    op.drop_view(IpRoute)
    op.drop_view(IpRouter)
    op.drop_view(IpRouteSys)
    op.drop_view(IpRoutingTable)
    op.drop_view(IpSec)
    op.drop_view(IpSyncRef)
    op.drop_view(IpSystem)
    op.drop_view(Ipv4DestNetwork)
    op.drop_view(Ipv4Peer)
    op.drop_view(Ipv4StaticRoute)
    op.drop_view(Ipv4StaticRouteTable)
    op.drop_view(IPv6RoutingTable)
    op.drop_view(Irc)
    op.drop_view(Iub)
    op.drop_view(IubDataStreams)
    op.drop_view(IubEdch)
    op.drop_view(IuLink)
    op.drop_view(IurLink)
    op.drop_view(KeyFileInformation)
    op.drop_view(KeyFileManagement)
    op.drop_view(Lag)
    op.drop_view(Ldap)
    op.drop_view(LdapAuthenticationMethod)
    op.drop_view(Licensing)
    op.drop_view(LinkTransmissionProfile)
    op.drop_view(Lm)
    op.drop_view(LoadBalancingFunction)
    op.drop_view(LoadControl)
    op.drop_view(LocationArea)
    op.drop_view(Log)
    op.drop_view(LogicalChannelGroup)
    op.drop_view(LogM)
    op.drop_view(LppaEcid)
    op.drop_view(LsmEcs)
    op.drop_view(M3uAssociation)
    op.drop_view(MACConfiguration)
    op.drop_view(MaintenanceUser)
    op.drop_view(MaintenanceUserSecurity)
    op.drop_view(ManagedElementData)
    op.drop_view(MaximumCellRange)
    op.drop_view(MbmsM3Based)
    op.drop_view(MbmsServiceArea)
    op.drop_view(MdtConfiguration)
    op.drop_view(MeasurementDefinition)
    op.drop_view(MediumAccessUnit)
    op.drop_view(MibManager)
    op.drop_view(MimoSleepFunction)
    op.drop_view(MixedMode)
    op.drop_view(MobCtrlAtPoorCov)
    op.drop_view(MocnCellProfile)
    op.drop_view(MpClusterHandling)
    op.drop_view(MpProcessingResource)
    op.drop_view(Mtp3bAp)
    op.drop_view(Mtp3bSlItu)
    op.drop_view(Mtp3bSls)
    op.drop_view(Mtp3bSpItu)
    op.drop_view(Mtp3bSr)
    op.drop_view(Mtp3bSrs)
    op.drop_view(MultiCarrier)
    op.drop_view(MulticastAntennaBranch)
    op.drop_view(MultiErabsPerUser)
    op.drop_view(NbapCommon)
    op.drop_view(NbapDedicated)
    op.drop_view(NetconfSsh)
    op.drop_view(NetconfTls)
    op.drop_view(NextHop)
    op.drop_view(NniSaalProfile)
    op.drop_view(NniSaalTp)
    op.drop_view(NodeBLocalCell)
    op.drop_view(NodeBLocalCellGroup)
    op.drop_view(NodeBSectorCarrier)
    op.drop_view(NodeCredential)
    op.drop_view(NodeFunction)
    op.drop_view(NodeGroupSyncMember)
    op.drop_view(NodeManagementFunction)
    op.drop_view(NodeSupport)
    op.drop_view(NodeSynch)
    op.drop_view(NonPlannedPciDrxProfile)
    op.drop_view(Ntp)
    op.drop_view(NtpFrequencySync)
    op.drop_view(NtpServer)
    op.drop_view(OamAccessPoint)
    op.drop_view(OamTrafficClass)
    op.drop_view(OctAntUlPerfPkg)
    op.drop_view(OnSiteActivities)
    op.drop_view(OperatorDefinedQci)
    op.drop_view(OpProfiles)
    op.drop_view(OptionalFeatureLicense)
    op.drop_view(OptionalFeatures)
    op.drop_view(Os155SpiTtp)
    op.drop_view(OtdoaSupl)
    op.drop_view(PacketFrequencySyncRef)
    op.drop_view(Paging)
    op.drop_view(Pch)
    op.drop_view(Pci)
    op.drop_view(PcpSetToQueue)
    op.drop_view(PcpToQueueMap)
    op.drop_view(PdrDevice)
    op.drop_view(PeerIPv4)
    op.drop_view(Pfs)
    op.drop_view(PiuDevice)
    op.drop_view(Plmn)
    op.drop_view(PlmnIdentityGroup)
    op.drop_view(PlugInUnit)
    op.drop_view(Pm)
    op.drop_view(PmEventM)
    op.drop_view(PmEventService)
    op.drop_view(PmInitiatedUeMeasurements)
    op.drop_view(PmMeasurementCapabilities)
    op.drop_view(PmService)
    op.drop_view(PmSupport)
    op.drop_view(PmUeMeasControl)
    op.drop_view(PmUlInterferenceReport)
    op.drop_view(PositioningServiceClass)
    op.drop_view(PowerControl)
    op.drop_view(PowerDistribution)
    op.drop_view(PowerSupply)
    op.drop_view(PredefRbsScannerGpeh)
    op.drop_view(PreschedulingProfile)
    op.drop_view(ProcessorLoad)
    op.drop_view(Ptp)
    op.drop_view(PtpBcOcPort)
    op.drop_view(Pws)
    op.drop_view(QciProfilePredefined)
    op.drop_view(QciTable)
    op.drop_view(QosAwareScheduler)
    op.drop_view(QoSClassifier)
    op.drop_view(QosPolicy)
    op.drop_view(QosProfiles)
    op.drop_view(QuadAntUlPerfPkg)
    op.drop_view(Queue)
    op.drop_view(QueueSystem)
    op.drop_view(RabHandling)
    op.drop_view(Rach)
    op.drop_view(RadioBearerTable)
    op.drop_view(RadioEquipmentClock)
    op.drop_view(RadioEquipmentClockReference)
    op.drop_view(RadioLinks)
    op.drop_view(RadioUnitCascading)
    op.drop_view(Ranap)
    op.drop_view(RateShaping)
    op.drop_view(RbsEventStreamer)
    op.drop_view(RbsLocalCell)
    op.drop_view(RbsMeasControl)
    op.drop_view(RbsSlot)
    op.drop_view(RbsSubrack)
    op.drop_view(RbsSynchronization)
    op.drop_view(RbsUnit)
    op.drop_view(Rcs)
    op.drop_view(RdiPort)
    op.drop_view(RealTimeSecLog)
    op.drop_view(RedirectWithNacc)
    op.drop_view(ReliableProgramUniter)
    op.drop_view(ReportConfigA1)
    op.drop_view(ReportConfigA1Prim)
    op.drop_view(ReportConfigA1Sec)
    op.drop_view(ReportConfigA4)
    op.drop_view(ReportConfigA5)
    op.drop_view(ReportConfigA5Anr)
    op.drop_view(ReportConfigA5DlComp)
    op.drop_view(ReportConfigA5SoftLock)
    op.drop_view(ReportConfigA5UlTrig)
    op.drop_view(ReportConfigB1Geran)
    op.drop_view(ReportConfigB1Utra)
    op.drop_view(ReportConfigB2Cdma2000)
    op.drop_view(ReportConfigB2Cdma20001xRtt)
    op.drop_view(ReportConfigB2CdmaRttUlTrig)
    op.drop_view(ReportConfigB2CdmaUlTrig)
    op.drop_view(ReportConfigB2Geran)
    op.drop_view(ReportConfigB2GeranUlTrig)
    op.drop_view(ReportConfigB2Utra)
    op.drop_view(ReportConfigB2UtraUlTrig)
    op.drop_view(ReportConfigCsfbCdma2000)
    op.drop_view(ReportConfigCsfbGeran)
    op.drop_view(ReportConfigCsfbUtra)
    op.drop_view(ReportConfigCsg)
    op.drop_view(ReportConfigEUtraBadCovPrim)
    op.drop_view(ReportConfigEUtraBadCovSec)
    op.drop_view(ReportConfigEUtraBestCell)
    op.drop_view(ReportConfigEUtraBestCellAnr)
    op.drop_view(ReportConfigEUtraIFA3UlTrig)
    op.drop_view(ReportConfigEUtraIFBestCell)
    op.drop_view(ReportConfigEUtraInterFreqLb)
    op.drop_view(ReportConfigEUtraInterFreqMbms)
    op.drop_view(ReportConfigEUtraIntraFreqPm)
    op.drop_view(ReportConfigInterRatLb)
    op.drop_view(ReportConfigSCellA1A2)
    op.drop_view(ReportConfigSCellA4)
    op.drop_view(ReportConfigSCellA6)
    op.drop_view(ReportConfigSearch)
    op.drop_view(ResMeasControl)
    op.drop_view(ResourcePartitions)
    op.drop_view(RetCascading)
    op.drop_view(RetConfigurationMgt)
    op.drop_view(RetDevice)
    op.drop_view(RetDeviceSet)
    op.drop_view(RetSubUnit)
    op.drop_view(RetSupport)
    op.drop_view(RetuDeviceGroup)
    op.drop_view(RfBranch)
    op.drop_view(RfPort)
    op.drop_view(RiLink)
    op.drop_view(RiPort)
    op.drop_view(RlcUm)
    op.drop_view(RlfProfile)
    op.drop_view(RncCapacity)
    op.drop_view(RncConfigLimits)
    op.drop_view(RncFeature)
    op.drop_view(RncModule)
    op.drop_view(RnlQosClassProfile)
    op.drop_view(Rnsap)
    op.drop_view(ROHC)
    op.drop_view(Router)
    op.drop_view(RouteTableIPv4Static)
    op.drop_view(RoutingArea)
    op.drop_view(RoutingTable)
    op.drop_view(Rps)
    op.drop_view(Rrc)
    op.drop_view(RruDeviceGroup)
    op.drop_view(RttPositioning)
    op.drop_view(S1HODataFwd)
    op.drop_view(SasPositioning)
    op.drop_view(SccpApLocal)
    op.drop_view(SccpApRemote)
    op.drop_view(SccpScrc)
    op.drop_view(SccpSp)
    op.drop_view(SchedulerSp)
    op.drop_view(Schema)
    op.drop_view(Sctp)
    op.drop_view(SctpAssociation)
    op.drop_view(SctpEndpoint)
    op.drop_view(SctpProfile)
    op.drop_view(SecM)
    op.drop_view(Sector)
    op.drop_view(SectorAntenna)
    op.drop_view(SectorCarrier)
    op.drop_view(SectorEquipmentFunction)
    op.drop_view(Security)
    op.drop_view(SecurityHandling)
    op.drop_view(ServiceArea)
    op.drop_view(ServiceSpecificDRX)
    op.drop_view(ServiceTriggeredMobility)
    op.drop_view(SfpModule)
    op.drop_view(Sftp)
    op.drop_view(Shaper)
    op.drop_view(SharedNetworkSupport)
    op.drop_view(Sid)
    op.drop_view(SignalingRadioBearer)
    op.drop_view(SingLayBeamfPerfPkg)
    op.drop_view(Site)
    op.drop_view(Slot)
    op.drop_view(Snmp)
    op.drop_view(SnmpTargetV2C)
    op.drop_view(SnmpTargetV3)
    op.drop_view(SpDevicePool)
    op.drop_view(SpidHoWhiteList)
    op.drop_view(SpidRATFreqPrio)
    op.drop_view(SpiQosClass)
    op.drop_view(SRVCCtoUTRAN)
    op.drop_view(STN)
    op.drop_view(StnFunction)
    op.drop_view(StreamingCapabilities)
    op.drop_view(Subrack)
    op.drop_view(SubscriberProfileID)
    op.drop_view(SubscrProfileIdHandling)
    op.drop_view(Support12Cells)
    op.drop_view(Support6Cells)
    op.drop_view(SwAllocation)
    op.drop_view(SwInventory)
    op.drop_view(SwitchCoreUnit)
    op.drop_view(SwitchInternalLinkPort)
    op.drop_view(SwitchPortStp)
    op.drop_view(SwitchStp)
    op.drop_view(SwItem)
    op.drop_view(SwM)
    op.drop_view(SwManagement)
    op.drop_view(SwVersion)
    op.drop_view(Synchronization)
    op.drop_view(SyncPort)
    op.drop_view(SyncServer)
    op.drop_view(SysM)
    op.drop_view(SystemFunctions)
    op.drop_view(TCPOptimization)
    op.drop_view(TdScdmaSessionContinuity)
    op.drop_view(TempSensor)
    op.drop_view(TermPointToENB)
    op.drop_view(TermPointToMme)
    op.drop_view(TermPointToSGW)
    op.drop_view(TimeM)
    op.drop_view(TimeServer)
    op.drop_view(TimeSetting)
    op.drop_view(TimeSettings)
    op.drop_view(TimeSyncIO)
    op.drop_view(TimingUnit)
    op.drop_view(Tls)
    op.drop_view(Tm7ModeSwitching)
    op.drop_view(TmaSupport)
    op.drop_view(TnApplication)
    op.drop_view(TnlCchQosClassProfile)
    op.drop_view(TnlDchQosClassProfile)
    op.drop_view(TnlHspaQosClassProfile)
    op.drop_view(TnlIuQosClassProfile)
    op.drop_view(TnlQosClass)
    op.drop_view(TnPort)
    op.drop_view(TpaDevice)
    op.drop_view(TpaDeviceSet)
    op.drop_view(TrafficAwarePowerSave)
    op.drop_view(TrafficClass)
    op.drop_view(TrafficClassPsInt)
    op.drop_view(TrafficManagement)
    op.drop_view(TrafficManager)
    op.drop_view(TrafficScheduler)
    op.drop_view(Transceiver)
    op.drop_view(Transport)
    op.drop_view(TransportNetwork)
    op.drop_view(TrustCategory)
    op.drop_view(TrustedCertificate)
    op.drop_view(TtiBundling)
    op.drop_view(TuSyncRef)
    op.drop_view(TwampResponder)
    op.drop_view(TxDataCloning)
    op.drop_view(TxDeviceGroup)
    op.drop_view(UeMeasControl)
    op.drop_view(UePosCellId)
    op.drop_view(UePositioning)
    op.drop_view(UeRabType)
    op.drop_view(UeRc)
    op.drop_view(UeRcEdchFlow)
    op.drop_view(UeRcPhyChEdch)
    op.drop_view(UeRcRab)
    op.drop_view(UeRcTrCh)
    op.drop_view(UeRrcType)
    op.drop_view(UeTac)
    op.drop_view(UlBasebandCapacity)
    op.drop_view(UlCompGroup)
    op.drop_view(UlFss)
    op.drop_view(UlPrbCapacity)
    op.drop_view(UniSaalProfile)
    op.drop_view(UniSaalTp)
    op.drop_view(UpgradeTrace)
    op.drop_view(Ura)
    op.drop_view(UserIdentity)
    op.drop_view(UserManagement)
    op.drop_view(UtranCellRelation)
    op.drop_view(UtraNetwork)
    op.drop_view(UtranFreqRelation)
    op.drop_view(UtranNetwork)
    op.drop_view(Vc4Ttp)
    op.drop_view(VclTp)
    op.drop_view(VendorCredential)
    op.drop_view(VLAN)
    op.drop_view(VLANGroup)
    op.drop_view(VlanPort)
    op.drop_view(VpcTp)
    op.drop_view(VplTp)
    op.drop_view(VRF)
    op.drop_view(Vrrpv3Interface)
    op.drop_view(Vrrpv3Session)
    op.drop_view(VswrSupervision)
    op.drop_view(WcdmaCarrier)
    op.drop_view(WcdmaHandover)
    op.drop_view(WcdmaSessionContinuity)
    op.drop_view(WifiMobility)
    op.drop_view(WifiModule)
    op.drop_view(XpProgram)