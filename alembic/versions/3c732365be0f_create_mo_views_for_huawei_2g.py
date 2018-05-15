"""Create MO views for Huawei 2G

Revision ID: 3c732365be0f
Revises: 46c028cee28a
Create Date: 2018-05-15 10:17:41.467000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c732365be0f'
down_revision = '46c028cee28a'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext

AE1T1 = ReplaceableObject(
    'huawei_cm_2g."AE1T1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSCFLAG",
        "CICNO",
        "DPCGIDX",
        "OPCIDX",
        "OPMODE",
        "PN",
        "SN",
        "SRN",
        "STCIC",
        "TSN",
        "TSTYPE"
    FROM
    huawei_nbi_gsm."AE1T1"

    """
)

AITFOTHPARA = ReplaceableObject(
    'huawei_cm_2g."AITFOTHPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AN4",
        "CHANNELRATECODE",
        "CIPHERINGOPTSW",
        "CNNODEIDX",
        "DECODECSFBIND",
        "DIRECTEDRETRYASSFAILSENDENABLE",
        "ENCRY_OPT_SWITCH",
        "ESTINDL3MSGTAFLAG",
        "FORCEQUEUEINASS",
        "INTRAHOAMRSETSTRATEGY",
        "MODIFYESPECICFAIL",
        "QUEFAILINASSMSGTYPE",
        "REVISIONLEVELFLAG",
        "SDCCHASSREQACKFLAG",
        "SENDCONFUSIONTOMSC",
        "SENDLOADINDICATIONTOMSC",
        "SPEECHVERSIONEXPAND",
        "SPEECHVERSTRATEGYINASS",
        "SPVERTDMSTRATEGY",
        "UCSPEECHVEROPTIINHO"
    FROM
    huawei_nbi_gsm."AITFOTHPARA"

    """
)

AITFREV = ReplaceableObject(
    'huawei_cm_2g."AITFREV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AITFRSVPARA1",
        "AITFRSVPARA2",
        "AITFRSVPARA3",
        "AITFRSVPARA4",
        "AITFRSVPARA5",
        "CNNODEIDX"
    FROM
    huawei_nbi_gsm."AITFREV"

    """
)

ALGCTRLPARA = ReplaceableObject(
    'huawei_cm_2g."ALGCTRLPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BRDTYPE",
        "PN",
        "PORTTYPE",
        "RLFWACSW",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."ALGCTRLPARA"

    """
)

ALMBLKPARA = ReplaceableObject(
    'huawei_cm_2g."ALMBLKPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "BLKPRD",
        "CNTRISTHRD",
        "CNTSTLTHRD",
        "TMRISTHRD",
        "TMSTLTHRD"
    FROM
    huawei_nbi_gsm."ALMBLKPARA"

    """
)

ALMBLKSW = ReplaceableObject(
    'huawei_cm_2g."ALMBLKSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLKFILTERSW",
        "BLKSTATPRD",
        "BLKSTATSW"
    FROM
    huawei_nbi_gsm."ALMBLKSW"

    """
)

ALMCAPACITY = ReplaceableObject(
    'huawei_cm_2g."ALMCAPACITY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "MAXNUM",
        "SD"
    FROM
    huawei_nbi_gsm."ALMCAPACITY"

    """
)

ALMLVL = ReplaceableObject(
    'huawei_cm_2g."ALMLVL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "ALVL"
    FROM
    huawei_nbi_gsm."ALMLVL"

    """
)

ALMML = ReplaceableObject(
    'huawei_cm_2g."ALMML"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CMELEVEL"
    FROM
    huawei_nbi_gsm."ALMML"

    """
)

ALMOSCISW = ReplaceableObject(
    'huawei_cm_2g."ALMOSCISW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SW"
    FROM
    huawei_nbi_gsm."ALMOSCISW"

    """
)

ALMOSCITHRD = ReplaceableObject(
    'huawei_cm_2g."ALMOSCITHRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "INOSCPRD",
        "INOSCTHRD",
        "OUTOSCPRD",
        "OUTOSCTHRD"
    FROM
    huawei_nbi_gsm."ALMOSCITHRD"

    """
)

ALMSCRN = ReplaceableObject(
    'huawei_cm_2g."ALMSCRN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALVL"
    FROM
    huawei_nbi_gsm."ALMSCRN"

    """
)

ALMSHLD = ReplaceableObject(
    'huawei_cm_2g."ALMSHLD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "SHLDFLG"
    FROM
    huawei_nbi_gsm."ALMSHLD"

    """
)

APPCERT = ReplaceableObject(
    'huawei_cm_2g."APPCERT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APPCERT",
        "APPTYPE"
    FROM
    huawei_nbi_gsm."APPCERT"

    """
)

ATESTPARA = ReplaceableObject(
    'huawei_cm_2g."ATESTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AINTFTESTENABLE"
    FROM
    huawei_nbi_gsm."ATESTPARA"

    """
)

BFDPROTOSW = ReplaceableObject(
    'huawei_cm_2g."BFDPROTOSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SN",
        "SRN",
        "SWITCH"
    FROM
    huawei_nbi_gsm."BFDPROTOSW"

    """
)

BOXRPT = ReplaceableObject(
    'huawei_cm_2g."BOXRPT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "BOXFLG"
    FROM
    huawei_nbi_gsm."BOXRPT"

    """
)

BRD = ReplaceableObject(
    'huawei_cm_2g."BRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BRDCLASS",
        "BRDTYPE",
        "LGCAPPTYPE",
        "RED",
        "SN",
        "SRN",
        "MPUSLOT",
        "MPUSUBRACK",
        "AUTOADDSRCON",
        "ISTCBRD",
        "LGCUSAGETYPE"
    FROM
    huawei_nbi_gsm."BRD"

    """
)

BSCAISS = ReplaceableObject(
    'huawei_cm_2g."BSCAISS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSCSYMOFF"
    FROM
    huawei_nbi_gsm."BSCAISS"

    """
)

BSCAITFTMR = ReplaceableObject(
    'huawei_cm_2g."BSCAITFTMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AT13",
        "AT17",
        "AT18",
        "AT4",
        "CNNODEIDX"
    FROM
    huawei_nbi_gsm."BSCAITFTMR"

    """
)

BSCBASIC = ReplaceableObject(
    'huawei_cm_2g."BSCBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISVER",
        "AIPCSDSRVRDNDLEV",
        "AMRHOCODECPOLICY",
        "AREACODE",
        "AVER",
        "BSCAVN",
        "BSCGLOBALIDENTITY",
        "BSCPVN",
        "CBPROTOCOLSPEC",
        "CC",
        "CICDMUTEDIFCNT",
        "CICDMUTEPERIOD",
        "CICDMUTESWITCH",
        "CICDMUTETHRE",
        "CICDMUTETIME",
        "CROCALTMTHRD",
        "CSPREHSCSDSECHANSW",
        "ENPREEMPTABISLVDSADMT",
        "ENPREEMPTISCADMT",
        "ENPREEMPTTRANSADMT",
        "ENQUETRANSADMT",
        "ENTCAUSE",
        "ENTSWITCH",
        "GCCHK",
        "GETBTSNETTBLTIMETHD",
        "GSMCSUSERHIGHPRILEV",
        "HIFREQBANDSUPPORT",
        "HSCSDCHANGEMODE",
        "ISCCONGALMCLRTH",
        "ISCCONGALMTH",
        "MSISDNPREFIX1",
        "MSISDNPREFIX2",
        "MSISDNPREFIX3",
        "MSISDNPREFIX4",
        "MSISDNPREFIX5",
        "MUTETESTLOGSTYLE",
        "SERVICEMODE",
        "SINGLEPASSEXCLUDEMSISDN1",
        "SINGLEPASSEXCLUDEMSISDN10",
        "SINGLEPASSEXCLUDEMSISDN11",
        "SINGLEPASSEXCLUDEMSISDN12",
        "SINGLEPASSEXCLUDEMSISDN13",
        "SINGLEPASSEXCLUDEMSISDN14",
        "SINGLEPASSEXCLUDEMSISDN15",
        "SINGLEPASSEXCLUDEMSISDN16",
        "SINGLEPASSEXCLUDEMSISDN17",
        "SINGLEPASSEXCLUDEMSISDN18",
        "SINGLEPASSEXCLUDEMSISDN19",
        "SINGLEPASSEXCLUDEMSISDN2",
        "SINGLEPASSEXCLUDEMSISDN20",
        "SINGLEPASSEXCLUDEMSISDN3",
        "SINGLEPASSEXCLUDEMSISDN4",
        "SINGLEPASSEXCLUDEMSISDN5",
        "SINGLEPASSEXCLUDEMSISDN6",
        "SINGLEPASSEXCLUDEMSISDN7",
        "SINGLEPASSEXCLUDEMSISDN8",
        "SINGLEPASSEXCLUDEMSISDN9",
        "SPEECHALMPERIOD",
        "SPEECHCHANALARMTHRES",
        "SPEECHCHANRESUMEALARMTHRES",
        "SPEECHCHNALMMUTESTATTYPE",
        "SPEECHERRORFORCEHOSWITCH",
        "SPTRANSHARING",
        "SUPPORTTFOCODECOPTIMIZE",
        "SYSMSG10ALLOWED",
        "TCCRCALLOWED",
        "TCHBUSYTHRESOPT",
        "UMCROSSDECTECTSWITCH",
        "UMVER"
    FROM
    huawei_nbi_gsm."BSCBASIC"

    """
)

BSCDSTPA = ReplaceableObject(
    'huawei_cm_2g."BSCDSTPA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSCDYNSWITCHTRXPAALLOW",
        "TSTURNINGOFFENABLE",
        "RSVIDLECHANNUM"
    FROM
    huawei_nbi_gsm."BSCDSTPA"

    """
)

BSCEXSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."BSCEXSOFTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABNORMSFORCSPEECHVERSW",
        "ABNORMSINBSCHOSTATPROSW",
        "ABNORRELBEFDIRECTSTATSW",
        "ABNORRELBEFHOSTATSW",
        "ABRKBARCELLOPTINTERVAL",
        "ABRKBARCELLSW",
        "AFTCONNRELSORTSTATSW",
        "AOIPRTPCONSW",
        "APPDATACHKGENSW",
        "APPDATACHKSW",
        "APPDATASELFHEALSW",
        "ASSFAILMSCCLDOPTSW",
        "BACDDETECTEN",
        "BSCLAYEREDPAGINGSW",
        "BSSLSOPTINDTMSW",
        "BTSUNAVAILALARMCHKSW",
        "CALLRELCROSSPROSW",
        "CCNACTIVEIECTRLSW",
        "CHANNELDYNADJUSTOPT",
        "CHRSIGMSGUSERIDENCRYPTSW",
        "CMPL3PROTOCOLCONSSW",
        "CROSSSEROCCUPYSTATSW",
        "CSCHOCCUPYSTATINLAUSW",
        "CSDTRANSRESOURCECTRLSWITCH",
        "CSFBACCCAUSESTATOPTSW",
        "CSFBPAGINGIDENTIFYSW",
        "DEACELLPERFSW",
        "DISCCLEARREQSTATSW",
        "DISCONNECTINHANDOVER",
        "DISCRELINDSTATSW",
        "DROPSORTSTATPOLICYSW",
        "DTMCHOCCUPYSUPPLYSTATSW",
        "DTMOPINDEXOPTSW",
        "DTMPSREROUTEPOLICY",
        "DYNPDCHSELFHEALSW",
        "ECSCOPTSW",
        "FASTRETURNSCRAMBLEINDSW",
        "FASTRETURNSERVICEHOSW",
        "FORCEUPDATEMSSI",
        "GHOFILTEROPT",
        "GLFRCSMTLAUMODE",
        "HISPRIOOPTSW",
        "HOCIPHERSW",
        "HOCMDTIMESTAMPADJUST",
        "HOFORBIDDENINLOCUPSW",
        "HOL2REBUILDTIMES",
        "HQIDEFINITION",
        "HSRPLCUSRIDNTMNGSW",
        "IBCAOUTBSCMSGSNDCTRLSW",
        "IGNORECONNFAILBEFHOCMPSW",
        "IMMASSUML3NULLPROPOLICY",
        "INTERBSCINHOSUCCSTATOPT",
        "INTERHOCM2IE",
        "INTERHOCM3LEN",
        "INTERRANHOEXPSW",
        "INTRABSCAMRHOCMDDELAYSW",
        "IUOFITEROPT",
        "JUDGERNCCIPHERSTATE",
        "LOADINDPROCON",
        "LOCKCELLSENDALMSW",
        "LOCREQCLASSMARK3INDSW",
        "MCPLOADOPTSWITCH",
        "MOCNCSWAITIDRSPTIMER",
        "MOCNQRYIMSISNDXIDSW",
        "MOCNREPLACEIMSISW",
        "MOCNREROUTEOPT",
        "MOCNROUTEPOLICYGETIMSIFAIL",
        "MOCNSELECTCNPOLICY",
        "MOCNTIMEOUTREROUTEPERMIT",
        "MOCNWAITIDRSPTIMER",
        "MRRXQUALSTATMODESW",
        "MSGBYTEORDERPROTPOLICY",
        "PDCHSTATOPTSW",
        "REASSFAILSTATSW",
        "REASSIGNINAOIPSW",
        "RECLAIMFAILPDRELSW",
        "RESENDIDREQSW",
        "RETURNOLDCHANOPTSW",
        "RXLEVSTATSORTSW",
        "SAICWHTMSIDENTALPHALWRTHLD",
        "SAICWHTMSIDENTALPHAUPTHLD",
        "SAICWHTMSIDENTREQTIMES",
        "SAICWHTMSIDENTSATTIMES",
        "SAVEUSERPAGINGTMR",
        "SECONDDIRECTHOREQSTATSW",
        "TRANIMTMALMPROTECTSW",
        "USERPRIORITYOPT",
        "USRPRITHRES1",
        "USRPRITHRES2",
        "UTRANCMDECSW",
        "UTRANPRIIECTRLSW",
        "VIPDTXFORBIDSW",
        "VIPPOWERAMP"
    FROM
    huawei_nbi_gsm."BSCEXSOFTPARA"

    """
)

BSCFCPARA = ReplaceableObject(
    'huawei_cm_2g."BSCFCPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AINTFCONGSTMINDISCARDRATIO",
        "AINTFCONGSTSTATPERIOD",
        "AINTFCRNUM",
        "AINTFFCDISCLUEN",
        "AINTFFCDISCMOCEN",
        "AINTFFCDISCMTCEN",
        "AINTFFCDISCOSEN",
        "AINTFFCEN",
        "AINTFFCMETHOD",
        "AINTFFCRSRATE1",
        "AINTFFCRSRATE2",
        "AINTFFCRSRATE3",
        "AINTFFCRSRATE4",
        "AINTFFCRSRATE5",
        "AINTFFCRSRATE6",
        "AINTFMSGTHRESHOLD",
        "AINTFOCCURATE",
        "ATERRSLFCCTRL",
        "CHREQCSMAXMSGNUMINPERIOD",
        "CHREQPSAVGMSGNUMINPERIOD",
        "CHREQSTATPERIOD",
        "GCBSFCCPUENDTHD",
        "GCBSFCCPUSTARTTHD",
        "GCBSFCMSGENDTHD",
        "GCBSFCMSGSTARTTHD",
        "GCBSFCSUBCPUCTRLTHD",
        "GCBSFCSW",
        "GCBSMAXMSGNUMINPERIOD",
        "GCBSSTATPERIOD",
        "LOADBALANCETHD",
        "LOCUPMAXMSGINPERIOD",
        "MOCACCESSCPURATE",
        "MPUFCCTRL",
        "MTCACCESSCPURATE",
        "P11",
        "P12",
        "P13",
        "P14",
        "PFREQCODEMODE",
        "PGCLASSIFINGALLOWED",
        "PGMAXMSGNUMINPERIOD",
        "PGMAXPSMSGNUMINPERIOD",
        "PGSTATPERIOD",
        "PRIFCEN",
        "PSDSPUSAGECTRL",
        "PSRESREQMSGNUMINPERIOD",
        "PSRESREQSTATPERIOD",
        "SCCPCONGSTTHRESHOLD",
        "SECONDPSPGFCCTRL",
        "SHAREINCPURATE",
        "STARTASIGCTRL",
        "STARTCBSHORTMSGFLOWCTRL",
        "STARTCHREQARRIVALCTRL",
        "STARTPGARRIVALCTRL",
        "STARTPSRESREQARRIVALCTRL",
        "VIPACCESSCPURATE",
        "VIPPRIORITY",
        "VIPSHAREINCPURATE"
    FROM
    huawei_nbi_gsm."BSCFCPARA"

    """
)

BSCJBF = ReplaceableObject(
    'huawei_cm_2g."BSCJBF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPOSATJTTTIME",
        "JTTADJMAX",
        "JTTADJMIN",
        "JTTLOSSCNT",
        "JTTLOSSPER",
        "JTTLOSSPERCALCPERIOD",
        "JTTTIME"
    FROM
    huawei_nbi_gsm."BSCJBF"

    """
)

BSCNSPARA = ReplaceableObject(
    'huawei_cm_2g."BSCNSPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALIVERETRY",
        "ALIVETIMER",
        "BLOCKRETRY",
        "BLOCKTIMER",
        "RESETRETRY",
        "RESETTIMER",
        "TESTTIMER",
        "UNBLOCKRETRY"
    FROM
    huawei_nbi_gsm."BSCNSPARA"

    """
)

BSCPCUTYPE = ReplaceableObject(
    'huawei_cm_2g."BSCPCUTYPE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TYPE"
    FROM
    huawei_nbi_gsm."BSCPCUTYPE"

    """
)

BSCPSGBPARA = ReplaceableObject(
    'huawei_cm_2g."BSCPSGBPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DSCPSUPPORT",
        "ERRNRIRESUMEPOLICY",
        "LLCPDUREORDERTIME",
        "SENDRACAPUPDATE",
        "SIGERRNRIULMSGPOLICY",
        "SIZEFLOWSELFHEALTHD",
        "SUPRASTATUS",
        "USRULPDUTBITVALUE",
        "XIDPDULEN",
        "XIDPDUPROC"
    FROM
    huawei_nbi_gsm."BSCPSGBPARA"

    """
)

BSCPSSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."BSCPSSOFTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISIPPDCHRESYNSW",
        "ACTIVETBFBUFFRPTINTERVAL",
        "ADDTRANSBWINT",
        "ADDTRANSBWNUM",
        "ALLOWEDADAMULTIPLEX",
        "APPSLVABISAFTERPDALLOC",
        "AQMM",
        "AQMMAXTH",
        "AQMMINTH",
        "AQMNINIT",
        "AQMNLOWERBOUND",
        "AQMNUPBOUND",
        "AQMSWITCH",
        "AQMTARTH",
        "BADVESTDLTBF",
        "BSCPSRESERVEPARA2",
        "BSCPSRESERVEPARA3",
        "BSCPSRESERVEPARA4",
        "CELLDISTOPTSW",
        "CELLDISTPERSISTENTSW",
        "CELLDYNDISTOPT",
        "CELLDYNDISTSWITCH",
        "CELLMIGINPDCHRESVTHRES",
        "CELLMIGOUTPDCHFAILTHRES",
        "CELLRESELTRAFFICCONTINUE",
        "CHECKLVDSTHD",
        "CONVERTPDCHTRXPRISW",
        "DECGMMPDULIFETIME",
        "DLCOEFFICIENTTSRAPIDADJ",
        "DLFIRSTBLKPOLLING",
        "DLNONACCSTOPREROUTESW",
        "DTMIMMAPPLYSLAVEABIS",
        "EGPRSACCFAILASSGPRS",
        "FLOWCOUNTPERIODTICKS",
        "FLOWCOUNTPERIODTSRAPIDADJ",
        "FORBIDEDGU",
        "FORCE2PHASE",
        "FORCEMSTRAFFICCLASS",
        "FORCERELTBFDURATION",
        "GMMLOWCODESW",
        "GPRSDLRETRANRATESTAT",
        "IPCELLPDCHACTFAILPENSW",
        "LOADBROADCASTPERIOD",
        "MAXDLASSRETRYTIMES",
        "MAXDLESTRETRYNUM",
        "MAXPOLLINGRETRYTIMES",
        "MCBSPSELFHEALSW",
        "MCS3PASMCS3",
        "MOCNREJECTCAUSEPOLICY",
        "MSCONTEXTLIFETIME",
        "N3101OVERFLOWDEGRADECS",
        "NC2LOADRESEL",
        "NSLINKFAULTTRACESW",
        "PDCHACTCTRLSW",
        "PDCHACTFAILPENTIME",
        "PDCHAPPLYTIMEOUTRELSW",
        "PKTREASSPROTECTINTERVAL",
        "PMOADDFREQALLOW",
        "PSCELLDYNADJRATIO",
        "PSCELLDYNADJTIME",
        "PSCELLTABSELFHEALSW",
        "PSCHRIDREQTLLIPOLICY",
        "PSUPBRDMIXCELLDISTOPTSW",
        "PSUPSELFHEALACCNUMTHD",
        "PSUPSELFHEALACCSUCCTHD",
        "PSUPSELFHEALPERIOD",
        "READYTIMER",
        "REDUCETRANSBWINT",
        "REDUCETRANSBWNUM",
        "RELFLEXABISFORLDR",
        "RIMONECOSW",
        "RSTPSCELLPDCHCFGCHG",
        "RTTISCHED",
        "SENDDUMMYAFTERULASSSW",
        "SILENCETICKSOFRESREQ",
        "SPTDLTBFSCHEDOPTIMIZE",
        "SPTNACCRESGUARANTEE",
        "STALLNACKBLKPOLLING",
        "STOPPSLDRPOLICY",
        "SUPPORTDL5TS",
        "SUPPORTDLDCFORBE",
        "SUPPORTEDA",
        "TDMBCCHDTXSW",
        "TIMERLEADPDCHACTFAILSW",
        "TRAFFICCLASSDLCOEFFICIENT",
        "TRAFFICCLASSULCOEFFICIENT",
        "TRXRESRELSW",
        "TSRAPIDADJPERIOD",
        "TSRAPIDADJSWITCH",
        "ULBEPINTERPOLATION",
        "ULCOEFFICIENTTSRAPIDADJ",
        "ULCSADJFORABISREL",
        "ULDLACKFREQ",
        "ULDUMMYSTATSW",
        "ULEGPRSDLACKFREQ",
        "ULEGPRSULACKFREQ",
        "ULULACKFREQ",
        "USFDUMMYPCPOLICY",
        "USFGRAN4BLK",
        "WIFIINTERWORKINGSWITCH"
    FROM
    huawei_nbi_gsm."BSCPSSOFTPARA"

    """
)

BSCPSSTAT = ReplaceableObject(
    'huawei_cm_2g."BSCPSSTAT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DLTBFSTATINIPCELL",
        "DLTBFSTATINTDMCELL",
        "FAKEPDUSTAT",
        "LLCPDUBNUMSTATMODE",
        "LLCPDUTHRUPUTSTATMODE",
        "LLCTHRUPUTCALCPERIOD",
        "PSUSRAWAREDLBIGPKTTHD",
        "PSUSRAWAREFLOWCNTTHD",
        "PSUSRAWARERATETHD",
        "PSUSRAWARETBFABNINTTIME",
        "PSUSRAWARETBFNORINTTIME",
        "RLCBLOCKSTATMODE",
        "STATDLPACKINDELAYREL",
        "STATDMYPDUINDELAYREL",
        "STATFLUSHLLINABNTBFREL",
        "STATLLCTRANSDURA",
        "STATULBLKWHENDELAYREL",
        "TRANSINTSTATMODE",
        "ULTBFABNRELINACT"
    FROM
    huawei_nbi_gsm."BSCPSSTAT"

    """
)

BSCPSTCDSCPMAP = ReplaceableObject(
    'huawei_cm_2g."BSCPSTCDSCPMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BCDSCP",
        "CCDSCP",
        "ICTHP1DSCP",
        "ICTHP2DSCP",
        "ICTHP3DSCP",
        "SCDSCP",
        "SDSCP"
    FROM
    huawei_nbi_gsm."BSCPSTCDSCPMAP"

    """
)

BSCPSUMPARA = ReplaceableObject(
    'huawei_cm_2g."BSCPSUMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADDITIONALMSRACAP",
        "CONTENTIONRESOLUTIONOPT",
        "CONTENTRESOLUTPOLICY",
        "DLASSMSREACTIONTIME",
        "DLASSONULCHANSWITCHING",
        "DLIMMASSDELAYDRX",
        "DLIMMASSDELAYNONDRX",
        "DLIMMASSWITHP0SW",
        "DLRESREASSONRAUPDATE",
        "DLRESREASSQOSCHANGESW",
        "DLTBFADVESTONULONEBLK",
        "IGNOREPKTRESREQ",
        "IGRRESREQDURULRELSW",
        "PACCHDLESTSW",
        "PKTDLASSWITHULPWCTRL",
        "QUICKSTARTDLONIMMASSSW",
        "QUICKSTARTDLTBFONDL",
        "QUICKSTARTDLTBFONUL",
        "RESENDDLPACKETASS",
        "RESENDULPACKETASS",
        "SENDPKTULACCREJ",
        "SENDSINGLEASSCCCHOVLD",
        "SENDTBFREL",
        "SENDULREASS",
        "SETDLEGPRSTBFTORLCACKMODE",
        "SETDLGPRSTBFTORLCACKMODE",
        "SINGLEASSDELAY",
        "T3193ACCURATECALCSW",
        "T3193DLDELAYESTBINTERVAL",
        "TBFEXISTTIMEBEFORETS",
        "TLLIBLKCHANCOD",
        "TSINTERVAL",
        "ULABNORRESREQPROCSW",
        "ULASSMSREACTIONTIME",
        "ULIMMASSDELAY"
    FROM
    huawei_nbi_gsm."BSCPSUMPARA"

    """
)

BSCSIGTRC = ReplaceableObject(
    'huawei_cm_2g."BSCSIGTRC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISTIFMSGTYPE",
        "ATIFMSGTYPE",
        "LOGRPTPERIOD",
        "MRLOGNCELLTYPE",
        "TRCMSGIND"
    FROM
    huawei_nbi_gsm."BSCSIGTRC"

    """
)

BSCTESTPARA = ReplaceableObject(
    'huawei_cm_2g."BSCTESTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DTMFLOOPSWITCH",
        "VOICEOPENTRACECELL",
        "VOICEOPENTRACENODE",
        "VOICEOPENTRACESPVER",
        "VOICEOPENTRACESSN",
        "VOICEOPENTRACETPYE"
    FROM
    huawei_nbi_gsm."BSCTESTPARA"

    """
)

BSCTMR = ReplaceableObject(
    'huawei_cm_2g."BSCTMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISFCTIMER1",
        "ABISFCTIMER2",
        "AT1",
        "AT19",
        "AT20",
        "BMTCFCTIMERLEN",
        "CBNONMSGTIMER",
        "CBSHAKEHANDTIMER",
        "EXTCELLLOADINVALIDTIMER",
        "MSCCLRCMDTMR",
        "PROHIBTRPTCELLLOAD",
        "RELITFACONNTMR",
        "RESCHKSTARTTM",
        "RESCHKSTPTM",
        "RESINDPERIOD",
        "SDBACK2TCHJDG",
        "TCHSDDYNADJCHK",
        "TI_WAIT_SGSN_PRIVATE_MESSAGE",
        "TRBSS",
        "WAITCHNADJ"
    FROM
    huawei_nbi_gsm."BSCTMR"

    """
)

BSSGPPARA = ReplaceableObject(
    'huawei_cm_2g."BSSGPPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BVCTF",
        "MSTF",
        "T1",
        "T2",
        "T3",
        "T4",
        "T5",
        "T6",
        "T8",
        "TC",
        "TH"
    FROM
    huawei_nbi_gsm."BSSGPPARA"

    """
)

BSSLS = ReplaceableObject(
    'huawei_cm_2g."BSSLS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSSLSGENMODE",
        "MSISDNSEGLIST2AVOIDBSCLS1",
        "MSISDNSEGLIST2AVOIDBSCLS10",
        "MSISDNSEGLIST2AVOIDBSCLS2",
        "MSISDNSEGLIST2AVOIDBSCLS3",
        "MSISDNSEGLIST2AVOIDBSCLS4",
        "MSISDNSEGLIST2AVOIDBSCLS5",
        "MSISDNSEGLIST2AVOIDBSCLS6",
        "MSISDNSEGLIST2AVOIDBSCLS7",
        "MSISDNSEGLIST2AVOIDBSCLS8",
        "MSISDNSEGLIST2AVOIDBSCLS9",
        "MSISDNSEGLIST2AVOIDBTSLS1",
        "MSISDNSEGLIST2AVOIDBTSLS10",
        "MSISDNSEGLIST2AVOIDBTSLS2",
        "MSISDNSEGLIST2AVOIDBTSLS3",
        "MSISDNSEGLIST2AVOIDBTSLS4",
        "MSISDNSEGLIST2AVOIDBTSLS5",
        "MSISDNSEGLIST2AVOIDBTSLS6",
        "MSISDNSEGLIST2AVOIDBTSLS7",
        "MSISDNSEGLIST2AVOIDBTSLS8",
        "MSISDNSEGLIST2AVOIDBTSLS9"
    FROM
    huawei_nbi_gsm."BSSLS"

    """
)

BTS = ReplaceableObject(
    'huawei_cm_2g."BTS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISBYPASSMODE",
        "ACTSTATUS",
        "BTSDESC",
        "BTSID",
        "BTSNAME",
        "BTSTYPE",
        "FLEXABISMODE",
        "HOSTTYPE",
        "INNBBULICSHAEN",
        "INTRABBPOOLSWITCH",
        "IPPHYTRANSTYPE",
        "ISCONFIGEDRING",
        "MAINBMPMODE",
        "MAINPORTNO",
        "MPMODE",
        "SEPERATEMODE",
        "SERVICEMODE",
        "SRANMODE",
        "WORKMODE",
        "TRANDETSWITCH",
        "TSASSIGNOPTISW"
    FROM
    huawei_nbi_gsm."BTS"

    """
)

BTSABISMUXFLOW = ReplaceableObject(
    'huawei_cm_2g."BTSABISMUXFLOW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "PKTLENTHRES",
        "SRVTYPE",
        "SUBFRAMETHRES",
        "TIMEOUT"
    FROM
    huawei_nbi_gsm."BTSABISMUXFLOW"

    """
)

BTSABISPRIMAP = ReplaceableObject(
    'huawei_cm_2g."BTSABISPRIMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "EMLDSCP",
        "ESLDSCP",
        "OMLDSCP",
        "RSLDSCP",
        "TRANSTYPE",
        "VLANFLAG"
    FROM
    huawei_nbi_gsm."BTSABISPRIMAP"

    """
)

BTSABISTROP = ReplaceableObject(
    'huawei_cm_2g."BTSABISTROP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DETECTSWITCH",
        "PROTECTDELAYTIME"
    FROM
    huawei_nbi_gsm."BTSABISTROP"

    """
)

BTSAISS = ReplaceableObject(
    'huawei_cm_2g."BTSAISS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "SITESYNCZONE",
        "SYMOFFSET"
    FROM
    huawei_nbi_gsm."BTSAISS"

    """
)

BTSALM = ReplaceableObject(
    'huawei_cm_2g."BTSALM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "BTSTYPE",
        "EXTFLAG"
    FROM
    huawei_nbi_gsm."BTSALM"

    """
)

BTSALMFLASHTHD = ReplaceableObject(
    'huawei_cm_2g."BTSALMFLASHTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALMID",
        "ALMOCCURACCUTIMEHTHD",
        "ALMOCCURACCUTIMELTHD",
        "ALMOCCURTIMESHTHD",
        "ALMOCCURTIMESLTHD",
        "FLASHALMCLRTHD",
        "FLASHALMOCCURTHD"
    FROM
    huawei_nbi_gsm."BTSALMFLASHTHD"

    """
)

BTSALMFLASHTW = ReplaceableObject(
    'huawei_cm_2g."BTSALMFLASHTW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FLASHSTATISALMCLRTW",
        "FLASHSTATISALMOCCURTW"
    FROM
    huawei_nbi_gsm."BTSALMFLASHTW"

    """
)

BTSALMPORT = ReplaceableObject(
    'huawei_cm_2g."BTSALMPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "SWITCH"
    FROM
    huawei_nbi_gsm."BTSALMPORT"

    """
)

BTSAPMUBP = ReplaceableObject(
    'huawei_cm_2g."BTSAPMUBP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADDR",
        "ALMENABLE",
        "ASSORXUCN",
        "ASSORXUSN",
        "ASSORXUSRN",
        "BASETEMPERATURE",
        "BC",
        "BCD",
        "BCLC",
        "BE",
        "BTPC",
        "BTSID",
        "BTSSHUTDNASW",
        "BTYPE",
        "CELLTEMP1THRESHOLDH",
        "CELLTEMP1THRESHOLDL",
        "CELLTEMPCOMPENABLED",
        "CFGFLAG",
        "CN",
        "HIGHTEMPLOADPWROFF",
        "HPVFLAG",
        "HTSDF",
        "HUMALAMRTHRESHOLDH",
        "HUMALAMRTHRESHOLDL",
        "MCN",
        "MPN",
        "MSRN",
        "PTYPE",
        "SAAF",
        "SBAF",
        "SDT",
        "SETDIESELENGINEENABLED",
        "SETENVPARAENABLED",
        "SETHUMPARAENABLED",
        "SN",
        "SRN",
        "TCC",
        "TEMPOFHIGHTEMPLOADPWROFF",
        "TLTHD",
        "TUTHD",
        "ACVLTHD",
        "ACVUTHD",
        "BCV",
        "DCVLTHD",
        "DCVUTHD",
        "FCV",
        "LOWTEMPLOADPWROFF",
        "LSDF",
        "LSDV",
        "LVSDF",
        "SDV",
        "TEMPOFLOWTEMPLOADPWROFF"
    FROM
    huawei_nbi_gsm."BTSAPMUBP"

    """
)

BTSAPPCERT = ReplaceableObject(
    'huawei_cm_2g."BTSAPPCERT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APPCERT",
        "APPTYPE",
        "BTSID"
    FROM
    huawei_nbi_gsm."BTSAPPCERT"

    """
)

BTSAUTODLDACTINFO = ReplaceableObject(
    'huawei_cm_2g."BTSAUTODLDACTINFO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADLDACT",
        "ADMODE",
        "ADVER1",
        "ADVER2",
        "AUTOTYPE",
        "BTSID",
        "CVER",
        "PATCHNO1",
        "PV",
        "RVER",
        "STTYPE",
        "VVER"
    FROM
    huawei_nbi_gsm."BTSAUTODLDACTINFO"

    """
)

BTSBAKPWR = ReplaceableObject(
    'huawei_cm_2g."BTSBAKPWR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BAKPWRSAVMETHOD",
        "BTSID"
    FROM
    huawei_nbi_gsm."BTSBAKPWR"

    """
)

BTSBBMODE = ReplaceableObject(
    'huawei_cm_2g."BTSBBMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BBMODE",
        "BTSID"
    FROM
    huawei_nbi_gsm."BTSBBMODE"

    """
)

BTSBINDLOCGRP = ReplaceableObject(
    'huawei_cm_2g."BTSBINDLOCGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANTPASSNO",
        "BTSID",
        "CN",
        "MAINLOCGRPNO",
        "SLAVELOCGRPNO",
        "SN",
        "SRN",
        "TRXID",
        "TRXPN"
    FROM
    huawei_nbi_gsm."BTSBINDLOCGRP"

    """
)

BTSBRD = ReplaceableObject(
    'huawei_cm_2g."BTSBRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BT",
        "BTSID",
        "CN",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSBRD"

    """
)

BTSBREAKPOINT = ReplaceableObject(
    'huawei_cm_2g."BTSBREAKPOINT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BP1",
        "BP2",
        "BTSID",
        "RCN"
    FROM
    huawei_nbi_gsm."BTSBREAKPOINT"

    """
)

BTSBWPARA = ReplaceableObject(
    'huawei_cm_2g."BTSBWPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "COMPRS",
        "OMLESLDL",
        "OMLESLUL",
        "RSLDL",
        "RSLUL",
        "TRANSTYPE"
    FROM
    huawei_nbi_gsm."BTSBWPARA"

    """
)

BTSCABINET = ReplaceableObject(
    'huawei_cm_2g."BTSCABINET"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BBUSUBRACKTYPE",
        "BTSID",
        "CABINETDESC",
        "CN",
        "ISMAINCABINET",
        "SRANMODE",
        "TYPE"
    FROM
    huawei_nbi_gsm."BTSCABINET"

    """
)

BTSCELLPATCHPARA = ReplaceableObject(
    'huawei_cm_2g."BTSCELLPATCHPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CELLID",
        "RSVDPARA1",
        "RSVDPARA10",
        "RSVDPARA11",
        "RSVDPARA12",
        "RSVDPARA13",
        "RSVDPARA14",
        "RSVDPARA15",
        "RSVDPARA16",
        "RSVDPARA17",
        "RSVDPARA18",
        "RSVDPARA19",
        "RSVDPARA2",
        "RSVDPARA20",
        "RSVDPARA21",
        "RSVDPARA22",
        "RSVDPARA23",
        "RSVDPARA24",
        "RSVDPARA25",
        "RSVDPARA3",
        "RSVDPARA4",
        "RSVDPARA5",
        "RSVDPARA6",
        "RSVDPARA7",
        "RSVDPARA8",
        "RSVDPARA9"
    FROM
    huawei_nbi_gsm."BTSCELLPATCHPARA"

    """
)

BTSCERTCHKTSK = ReplaceableObject(
    'huawei_cm_2g."BTSCERTCHKTSK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALMRNG",
        "BTSID",
        "ISENABLE",
        "PERIOD",
        "UPDATEMETHOD"
    FROM
    huawei_nbi_gsm."BTSCERTCHKTSK"

    """
)

BTSCERTDEPLOY = ReplaceableObject(
    'huawei_cm_2g."BTSCERTDEPLOY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DEPLOYTYPE"
    FROM
    huawei_nbi_gsm."BTSCERTDEPLOY"

    """
)

BTSCERTMK = ReplaceableObject(
    'huawei_cm_2g."BTSCERTMK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APPCERT",
        "BTSID"
    FROM
    huawei_nbi_gsm."BTSCERTMK"

    """
)

BTSCERTREQ = ReplaceableObject(
    'huawei_cm_2g."BTSCERTREQ"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "COMMNAME",
        "KEYSIZE",
        "KEYUSAGE",
        "LOCALIP",
        "SIGNALG"
    FROM
    huawei_nbi_gsm."BTSCERTREQ"

    """
)

BTSCHNFALLBACK = ReplaceableObject(
    'huawei_cm_2g."BTSCHNFALLBACK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CHNNO",
        "CHNTYPE",
        "GROUPCALLNUM1",
        "SPEECHVERMODE1",
        "SPEECHVERSION"
    FROM
    huawei_nbi_gsm."BTSCHNFALLBACK"

    """
)

BTSCLK = ReplaceableObject(
    'huawei_cm_2g."BTSCLK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CLKTYPE",
        "CN",
        "FRAMEBITOFFSET",
        "FRAMESYNCSW",
        "PN",
        "SN",
        "SRN",
        "SSMSWICH",
        "TRANSTYPE",
        "TRCCLKRNGLMTSW",
        "TRCCLKRNGLMTTHD",
        "CLKSYNCMODE",
        "STANDARD"
    FROM
    huawei_nbi_gsm."BTSCLK"

    """
)

BTSCONNECT = ReplaceableObject(
    'huawei_cm_2g."BTSCONNECT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DESTNODE",
        "DXXINDEX",
        "DXXPN",
        "INCN",
        "INPN",
        "INSN",
        "INSRN",
        "OPNAME",
        "FCN",
        "FPN",
        "FSN",
        "FSRN",
        "UPBTSID",
        "PN",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSCONNECT"

    """
)

BTSCPRIPORT = ReplaceableObject(
    'huawei_cm_2g."BTSCPRIPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADMSTAT",
        "BTSID",
        "CN",
        "OPTN",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSCPRIPORT"

    """
)

BTSCRC4 = ReplaceableObject(
    'huawei_cm_2g."BTSCRC4"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CRC4CHK"
    FROM
    huawei_nbi_gsm."BTSCRC4"

    """
)

BTSCRLPOLICY = ReplaceableObject(
    'huawei_cm_2g."BTSCRLPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CRLPOLICY"
    FROM
    huawei_nbi_gsm."BTSCRLPOLICY"

    """
)

BTSCTRLEX = ReplaceableObject(
    'huawei_cm_2g."BTSCTRLEX"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CPUNO",
        "CTRLSN",
        "CTRLSRN"
    FROM
    huawei_nbi_gsm."BTSCTRLEX"

    """
)

BTSCTRLLNK = ReplaceableObject(
    'huawei_cm_2g."BTSCTRLLNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "LN",
        "SN",
        "SRN",
        "UPCN",
        "UPPT",
        "UPSN",
        "UPSRN"
    FROM
    huawei_nbi_gsm."BTSCTRLLNK"

    """
)

BTSDEVIP = ReplaceableObject(
    'huawei_cm_2g."BTSDEVIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "IP",
        "IPIDX",
        "ISINNERIP",
        "MASK",
        "PN",
        "PT",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSDEVIP"

    """
)

BTSDHCPSVRIP = ReplaceableObject(
    'huawei_cm_2g."BTSDHCPSVRIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DHCPSRV"
    FROM
    huawei_nbi_gsm."BTSDHCPSVRIP"

    """
)

BTSDHEUBP = ReplaceableObject(
    'huawei_cm_2g."BTSDHEUBP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADDR",
        "ALMPARACFGFLAG",
        "ASSORXUCN",
        "ASSORXUSN",
        "ASSORXUSRN",
        "BTSID",
        "CFGFLAG",
        "CN",
        "ISADDEDTMPCONTROL",
        "ISTMPCTRL",
        "MCN",
        "MPN",
        "MSRN",
        "SN",
        "SRN",
        "TCMODE",
        "TLTHD",
        "TUTHD",
        "DBD",
        "HTCP",
        "HTDO",
        "LTCP",
        "NTDI",
        "NTDO",
        "SBAF",
        "TLT",
        "ENDHEATTEMP",
        "STARTHEATTEMP"
    FROM
    huawei_nbi_gsm."BTSDHEUBP"

    """
)

BTSDSCPMAP = ReplaceableObject(
    'huawei_cm_2g."BTSDSCPMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DSCP",
        "VLANPRI"
    FROM
    huawei_nbi_gsm."BTSDSCPMAP"

    """
)

BTSE1T1BER = ReplaceableObject(
    'huawei_cm_2g."BTSE1T1BER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BEROOSSWITCH",
        "BTL",
        "BTSID"
    FROM
    huawei_nbi_gsm."BTSE1T1BER"

    """
)

BTSEAMRC = ReplaceableObject(
    'huawei_cm_2g."BTSEAMRC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "ENAMRCSWITCH",
        "LIMITRATETHR"
    FROM
    huawei_nbi_gsm."BTSEAMRC"

    """
)

BTSENVALMPORT = ReplaceableObject(
    'huawei_cm_2g."BTSENVALMPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "AVOL",
        "BTSID",
        "CN",
        "PN",
        "PT",
        "SN",
        "SRN",
        "SW"
    FROM
    huawei_nbi_gsm."BTSENVALMPORT"

    """
)

BTSEQUIPMENT = ReplaceableObject(
    'huawei_cm_2g."BTSEQUIPMENT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DEPLOYMENTID",
        "SITENAME"
    FROM
    huawei_nbi_gsm."BTSEQUIPMENT"

    """
)

BTSESN = ReplaceableObject(
    'huawei_cm_2g."BTSESN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "MAINDEVTAB",
        "OMBEARBOARD"
    FROM
    huawei_nbi_gsm."BTSESN"

    """
)

BTSETHOAM = ReplaceableObject(
    'huawei_cm_2g."BTSETHOAM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "OAMTYPE"
    FROM
    huawei_nbi_gsm."BTSETHOAM"

    """
)

BTSETHOAMAH = ReplaceableObject(
    'huawei_cm_2g."BTSETHOAMAH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "ERFAMPARA",
        "ERFAMPRDPARA",
        "ERFAMPRDPRID",
        "ERFAMPRID",
        "ERFAMSCDPARA",
        "ERFAMSCDPRID",
        "PDUPRID",
        "PDUSIZE",
        "PN",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSETHOAMAH"

    """
)

BTSETHPORT = ReplaceableObject(
    'huawei_cm_2g."BTSETHPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "FC",
        "IPEAAT",
        "IPEADT",
        "MACEAAT",
        "MACEADT",
        "MTU",
        "PN",
        "RATE",
        "RXBCPKTALMCLRTHD",
        "RXBCPKTALMOCRTHD",
        "SN",
        "SRN",
        "SWITCH3AH",
        "DUPLEX"
    FROM
    huawei_nbi_gsm."BTSETHPORT"

    """
)

BTSFALLBACK = ReplaceableObject(
    'huawei_cm_2g."BTSFALLBACK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "ENABLE"
    FROM
    huawei_nbi_gsm."BTSFALLBACK"

    """
)

BTSFLEXABISPARA = ReplaceableObject(
    'huawei_cm_2g."BTSFLEXABISPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "GROUPRELTSNUM",
        "PCUPREEMPTFLAG",
        "RSVTCHTSNUM"
    FROM
    huawei_nbi_gsm."BTSFLEXABISPARA"

    """
)

BTSFMUABP = ReplaceableObject(
    'huawei_cm_2g."BTSFMUABP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADDR",
        "BTSID",
        "CFGFLAG",
        "CN",
        "FMUTYPE",
        "MCN",
        "MPN",
        "MSRN",
        "SBAF",
        "SN",
        "SPECIALSWITCHERLEVEL",
        "SRN",
        "STC",
        "TCMODE"
    FROM
    huawei_nbi_gsm."BTSFMUABP"

    """
)

BTSGTRANSPARA = ReplaceableObject(
    'huawei_cm_2g."BTSGTRANSPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ARPAGINGTIME",
        "BTSID",
        "RATECFGTYPE",
        "ROUTINGBACKDELAYTIME"
    FROM
    huawei_nbi_gsm."BTSGTRANSPARA"

    """
)

BTSGUPWRSHRFP = ReplaceableObject(
    'huawei_cm_2g."BTSGUPWRSHRFP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CFGFLAG"
    FROM
    huawei_nbi_gsm."BTSGUPWRSHRFP"

    """
)

BTSIDLETS = ReplaceableObject(
    'huawei_cm_2g."BTSIDLETS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CGN",
        "OPNAME",
        "TSCOUNT"
    FROM
    huawei_nbi_gsm."BTSIDLETS"

    """
)

BTSIKECFG = ReplaceableObject(
    'huawei_cm_2g."BTSIKECFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DSCP",
        "IKEKLI",
        "IKEKLT",
        "NATKLI"
    FROM
    huawei_nbi_gsm."BTSIKECFG"

    """
)

BTSINTRXUSPEC = ReplaceableObject(
    'huawei_cm_2g."BTSINTRXUSPEC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "RXUSPECENUMDESC",
        "RXUSPECENUMNAME",
        "RXUSPECENUMVALUE",
        "RXUSPECMODULENAME"
    FROM
    huawei_nbi_gsm."BTSINTRXUSPEC"

    """
)

BTSIP = ReplaceableObject(
    'huawei_cm_2g."BTSIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSCIP",
        "BTSCOMTYPE",
        "BTSGWIPSWITCH",
        "BTSID",
        "BTSIP",
        "BTSMUTIP",
        "CFGFLAG",
        "GWIP",
        "HOSTTYPE",
        "LPN",
        "PEERBSCIP",
        "PEERBSCMASK",
        "RSCMNGMODE",
        "SN"
    FROM
    huawei_nbi_gsm."BTSIP"

    """
)

BTSIPCLKPARA = ReplaceableObject(
    'huawei_cm_2g."BTSIPCLKPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CLKPRTTYPE",
        "CLKTOPOMODE",
        "DN",
        "ISCLKREDUCY",
        "MASTERIPADDR",
        "PRFTYPE",
        "SER0PRI",
        "SYNMODE"
    FROM
    huawei_nbi_gsm."BTSIPCLKPARA"

    """
)

BTSIPGUARD = ReplaceableObject(
    'huawei_cm_2g."BTSIPGUARD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ARPLRNSTRICTSW",
        "ARPSPOOFCHKSW",
        "BTSID",
        "INVALIDPKTCHKSW",
        "IPSECREPLAYCHKSW"
    FROM
    huawei_nbi_gsm."BTSIPGUARD"

    """
)

BTSIPRT = ReplaceableObject(
    'huawei_cm_2g."BTSIPRT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "DSTIP",
        "DSTMASK",
        "NEXTHOP",
        "PRI",
        "RTIDX",
        "RTTYPE",
        "SN",
        "SRN",
        "IFNO",
        "ITFTYPE"
    FROM
    huawei_nbi_gsm."BTSIPRT"

    """
)

BTSJBF = ReplaceableObject(
    'huawei_cm_2g."BTSJBF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "JBF"
    FROM
    huawei_nbi_gsm."BTSJBF"

    """
)

BTSLAPDWS = ReplaceableObject(
    'huawei_cm_2g."BTSLAPDWS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "OMLWS",
        "RSLWS",
        "UPOMLWS",
        "UPRSLWS"
    FROM
    huawei_nbi_gsm."BTSLAPDWS"

    """
)

BTSLLDPGLOBAL = ReplaceableObject(
    'huawei_cm_2g."BTSLLDPGLOBAL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DELAY",
        "HOLDMULTI",
        "NOTIFYINTERVAL",
        "NOTIFYSW",
        "RESTARTDELAY",
        "TXINTVAL"
    FROM
    huawei_nbi_gsm."BTSLLDPGLOBAL"

    """
)

BTSLNKBKATTR = ReplaceableObject(
    'huawei_cm_2g."BTSLNKBKATTR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DETECTCOUNT",
        "DETECTTXINT",
        "REVERTIVETYPE",
        "WTBS"
    FROM
    huawei_nbi_gsm."BTSLNKBKATTR"

    """
)

BTSLOCGRP = ReplaceableObject(
    'huawei_cm_2g."BTSLOCGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "ISMAINLOCGRP",
        "LOCGRPNO",
        "OUTPUTPOWER",
        "OUTPUTPOWERUNIT",
        "PSRACJACCLEV",
        "RACJACCLEV"
    FROM
    huawei_nbi_gsm."BTSLOCGRP"

    """
)

BTSLOCKBCCH = ReplaceableObject(
    'huawei_cm_2g."BTSLOCKBCCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "BTSPOWEROFFLOCKBCCH"
    FROM
    huawei_nbi_gsm."BTSLOCKBCCH"

    """
)

BTSLR = ReplaceableObject(
    'huawei_cm_2g."BTSLR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "LRSW",
        "PN",
        "PT",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSLR"

    """
)

BTSLSW = ReplaceableObject(
    'huawei_cm_2g."BTSLSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "ISSUPPORTBTSLSWITCH"
    FROM
    huawei_nbi_gsm."BTSLSW"

    """
)

BTSMNTMODE = ReplaceableObject(
    'huawei_cm_2g."BTSMNTMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "MNTMODE",
        "ET",
        "ST"
    FROM
    huawei_nbi_gsm."BTSMNTMODE"

    """
)

BTSMPGRP = ReplaceableObject(
    'huawei_cm_2g."BTSMPGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACFC",
        "AUTHTYPE",
        "BTSID",
        "CN",
        "IPEAAT",
        "IPEADT",
        "IPHC",
        "LOCALIP",
        "MASK",
        "MCCLASS",
        "MHF",
        "MPGRPEAAT",
        "MPGRPEADT",
        "MPGRPN",
        "MPSWITCH",
        "PEERIP",
        "PFC",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSMPGRP"

    """
)

BTSMPLNK = ReplaceableObject(
    'huawei_cm_2g."BTSMPLNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "MPGRPN",
        "MRU",
        "PN",
        "PPPLNKN",
        "RSTIME",
        "SN",
        "SRN",
        "TSBITMAP"
    FROM
    huawei_nbi_gsm."BTSMPLNK"

    """
)

BTSOMLBACKUP = ReplaceableObject(
    'huawei_cm_2g."BTSOMLBACKUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "OMLBKUP"
    FROM
    huawei_nbi_gsm."BTSOMLBACKUP"

    """
)

BTSOMLDETECT = ReplaceableObject(
    'huawei_cm_2g."BTSOMLDETECT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "OMLDETECTSWITCH",
        "BTSBARCODE"
    FROM
    huawei_nbi_gsm."BTSOMLDETECT"

    """
)

BTSOMLTS = ReplaceableObject(
    'huawei_cm_2g."BTSOMLTS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "PN",
        "SN",
        "SRN",
        "SUBTS",
        "TS"
    FROM
    huawei_nbi_gsm."BTSOMLTS"

    """
)

BTSOTHPARA = ReplaceableObject(
    'huawei_cm_2g."BTSOTHPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISIDLETSALLOC",
        "ABISIDLETSCFGSWITCH",
        "AISSOP",
        "AMRTRANSBANDTHCOMPSW",
        "BATIMS",
        "BTSDBUS32KCFGSW",
        "BTSDETECTSWITCH",
        "BTSID",
        "CPRIFASTRING",
        "E1PORTFAILDELAY",
        "E1PORTSTAQUICKREPSW",
        "ECMP",
        "ENERGYMNG",
        "FASTTRXAIDSW",
        "HIGHMODPWRSW",
        "IPCLKSYNMODE",
        "ISSUPERBTS",
        "JITBUFDELAY",
        "MCPACUTPWRPRIPOLICY",
        "MTSTURNOFF",
        "PAADJVOL",
        "PDCHGBR",
        "PROBESEQ",
        "PSUTURNINGOFFENABLE",
        "PTRAUTSNSNEXTSW",
        "RESETTIME",
        "SDBBLSD",
        "SENDSAMBE",
        "SPRECM",
        "SPRTLU",
        "STPPWRCHK",
        "SUPPORTE1UNBA",
        "SYNCMETHOD",
        "TSSHTDOWNEN",
        "VSWRDETECTSENENHSW",
        "VSWRTHRESOPT",
        "PRIVATEPROBEFST",
        "PRIVATEPROBENUM",
        "PRIVATEPROBESND"
    FROM
    huawei_nbi_gsm."BTSOTHPARA"

    """
)

BTSPATCHPARA = ReplaceableObject(
    'huawei_cm_2g."BTSPATCHPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "RSVDPARA1",
        "RSVDPARA10",
        "RSVDPARA11",
        "RSVDPARA12",
        "RSVDPARA13",
        "RSVDPARA14",
        "RSVDPARA15",
        "RSVDPARA16",
        "RSVDPARA17",
        "RSVDPARA18",
        "RSVDPARA19",
        "RSVDPARA2",
        "RSVDPARA20",
        "RSVDPARA3",
        "RSVDPARA4",
        "RSVDPARA5",
        "RSVDPARA6",
        "RSVDPARA7",
        "RSVDPARA8",
        "RSVDPARA9"
    FROM
    huawei_nbi_gsm."BTSPATCHPARA"

    """
)

BTSPINGSW = ReplaceableObject(
    'huawei_cm_2g."BTSPINGSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "BTSPINGSWITCH"
    FROM
    huawei_nbi_gsm."BTSPINGSW"

    """
)

BTSPLRALM = ReplaceableObject(
    'huawei_cm_2g."BTSPLRALM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CFGFLAG"
    FROM
    huawei_nbi_gsm."BTSPLRALM"

    """
)

BTSPSUFP = ReplaceableObject(
    'huawei_cm_2g."BTSPSUFP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CFGFLAG"
    FROM
    huawei_nbi_gsm."BTSPSUFP"

    """
)

BTSRELIALOGSWITCH = ReplaceableObject(
    'huawei_cm_2g."BTSRELIALOGSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "RELIABILITYLOGSWITCH"
    FROM
    huawei_nbi_gsm."BTSRELIALOGSWITCH"

    """
)

BTSRET = ReplaceableObject(
    'huawei_cm_2g."BTSRET"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CTRLPORTCN",
        "CTRLPORTNO",
        "CTRLPORTSN",
        "CTRLPORTSRN",
        "DEVICENAME",
        "DEVICENO",
        "POLARTYPE",
        "RETTYPE",
        "SCENARIO",
        "SERIALNO",
        "VENDORCODE"
    FROM
    huawei_nbi_gsm."BTSRET"

    """
)

BTSRETDEVICEDATA = ReplaceableObject(
    'huawei_cm_2g."BTSRETDEVICEDATA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BAND1",
        "BAND2",
        "BAND3",
        "BAND4",
        "BEARING",
        "BTSID",
        "DEVICENO",
        "SUBUNITNO",
        "TILT"
    FROM
    huawei_nbi_gsm."BTSRETDEVICEDATA"

    """
)

BTSRETSUBUNIT = ReplaceableObject(
    'huawei_cm_2g."BTSRETSUBUNIT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AER",
        "BTSID",
        "CELLID",
        "CONNCN1",
        "CONNCN2",
        "CONNPN1",
        "CONNPN2",
        "CONNSN1",
        "CONNSN2",
        "CONNSRN1",
        "CONNSRN2",
        "DEVICENO",
        "SUBUNITNO",
        "TILT"
    FROM
    huawei_nbi_gsm."BTSRETSUBUNIT"

    """
)

BTSRINGATTR = ReplaceableObject(
    'huawei_cm_2g."BTSRINGATTR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "FASTCNETFLAG",
        "RINGNETDOUBLEDIRSWITCH",
        "TBS",
        "WTBS"
    FROM
    huawei_nbi_gsm."BTSRINGATTR"

    """
)

BTSRSV = ReplaceableObject(
    'huawei_cm_2g."BTSRSV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "RSVID",
        "RSVVALUE"
    FROM
    huawei_nbi_gsm."BTSRSV"

    """
)

BTSRXU2LOCGRP = ReplaceableObject(
    'huawei_cm_2g."BTSRXU2LOCGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "LOCGRPNO",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."BTSRXU2LOCGRP"

    """
)

BTSRXUBP = ReplaceableObject(
    'huawei_cm_2g."BTSRXUBP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CN",
        "GUPWRSHARESWITCH",
        "GXPWRSHARERLTMOSW",
        "HAVETT1",
        "HAVETT2",
        "HAVETT3",
        "HAVETT4",
        "HAVETT5",
        "HAVETT6",
        "HAVETT7",
        "HAVETT8",
        "IFOFFSET",
        "LVL1VSWR",
        "LVL2VSWR",
        "MRRUATTENFACTOR1",
        "MRRUATTENFACTOR2",
        "MRRUATTENFACTOR3",
        "MRRUATTENFACTOR4",
        "MRRUATTENFACTOR5",
        "MRRUATTENFACTOR6",
        "MRRUATTENFACTOR7",
        "MRRUATTENFACTOR8",
        "PASHRMODE",
        "PWRSWITCHA",
        "PWRSWITCHB",
        "PWRSWITCHC",
        "PWRSWITCHD",
        "PWRSWITCHE",
        "PWRSWITCHF",
        "PWRSWITCHG",
        "PWRSWITCHH",
        "RELATEDMODFUNC",
        "RRCSWITCH",
        "RSSIALARMCFGSWITCH",
        "RXFREQBANDMUTUALSW",
        "RXUTYPE",
        "SN",
        "SNDRCVMODE3",
        "SPTSHARING",
        "SRN",
        "VSWRALMDISPOSE",
        "WORKINGSTANDARD",
        "TXAOPER1",
        "TXAOPER2",
        "TXAOPER3",
        "TXAOPER4",
        "TXBOPER1",
        "TXBOPER2",
        "TXBOPER3",
        "TXBOPER4",
        "TXCOPER1",
        "TXCOPER2",
        "TXCOPER3",
        "TXCOPER4",
        "TXDOPER1",
        "TXDOPER2",
        "TXDOPER3",
        "TXDOPER4",
        "TXEOPER1",
        "TXEOPER2",
        "TXEOPER3",
        "TXEOPER4",
        "TXFOPER1",
        "TXFOPER2",
        "TXFOPER3",
        "TXFOPER4",
        "TXGOPER1",
        "TXGOPER2",
        "TXGOPER3",
        "TXGOPER4",
        "TXHOPER1",
        "TXHOPER2",
        "TXHOPER3",
        "TXHOPER4",
        "ADEF",
        "LNA1",
        "LNA2",
        "PWRSWITCHRET",
        "SNDRCVMODE2",
        "OVERCURALMTHDRET",
        "OVERCURCLRTHDRET",
        "THRESHOLDTYPERET",
        "UNDERCURALMTHDRET",
        "UNDERCURCLRTHDRET",
        "CHKMODA",
        "CHKMODB",
        "OVERCURALMTHDA",
        "OVERCURALMTHDB",
        "OVERCURCLRTHDA",
        "OVERCURCLRTHDB",
        "UNDERCURALMTHDA",
        "UNDERCURALMTHDB",
        "UNDERCURCLRTHDA",
        "UNDERCURCLRTHDB",
        "RSSILOWTHRESHOLD",
        "RSSIUNBALANCEDTHRESHOLD"
    FROM
    huawei_nbi_gsm."BTSRXUBP"

    """
)

BTSRXUBRD = ReplaceableObject(
    'huawei_cm_2g."BTSRXUBRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BRDRXBW",
        "BRDTXBW",
        "BT",
        "BTSID",
        "CN",
        "ISCONFIGTHD",
        "PWRMODE",
        "RXUCHAINNO",
        "RXUNAME",
        "RXUPOS",
        "RXUSPEC",
        "SN",
        "SRN",
        "TRXNUM",
        "RXUSPECNAME"
    FROM
    huawei_nbi_gsm."BTSRXUBRD"

    """
)

BTSRXUCHAIN = ReplaceableObject(
    'huawei_cm_2g."BTSRXUCHAIN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CMEAT",
        "HCN",
        "HPN",
        "HSN",
        "HSRN",
        "RCN",
        "TT"
    FROM
    huawei_nbi_gsm."BTSRXUCHAIN"

    """
)

BTSSHARING = ReplaceableObject(
    'huawei_cm_2g."BTSSHARING"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "SHARINGALLOW",
        "SPTTRMSHARE"
    FROM
    huawei_nbi_gsm."BTSSHARING"

    """
)

BTSTEMPLATERSC = ReplaceableObject(
    'huawei_cm_2g."BTSTEMPLATERSC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TEMPLATENAME"
    FROM
    huawei_nbi_gsm."BTSTEMPLATERSC"

    """
)

BTSTHEFTALM = ReplaceableObject(
    'huawei_cm_2g."BTSTHEFTALM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANTITHEFTALLOW",
        "BTSID"
    FROM
    huawei_nbi_gsm."BTSTHEFTALM"

    """
)

BTSTMA = ReplaceableObject(
    'huawei_cm_2g."BTSTMA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CTRLPORTCN",
        "CTRLPORTSN",
        "CTRLPORTSRN",
        "DEVICENAME",
        "DEVICENO",
        "PWRSUPPLYTYPE",
        "SUBUNITNUM",
        "SERIALNO",
        "VENDORCODE"
    FROM
    huawei_nbi_gsm."BTSTMA"

    """
)

BTSTMADEVICEDATA = ReplaceableObject(
    'huawei_cm_2g."BTSTMADEVICEDATA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BAND1",
        "BAND2",
        "BAND3",
        "BAND4",
        "BEARING",
        "BTSID",
        "DEVICENO",
        "GAINRESOLUTION",
        "RXMAXFQ",
        "RXMINFQ",
        "SUBUNITNO",
        "SUBUNITTYPE",
        "TILT",
        "TXMAXFQ",
        "TXMINFQ"
    FROM
    huawei_nbi_gsm."BTSTMADEVICEDATA"

    """
)

BTSTMASUBUNIT = ReplaceableObject(
    'huawei_cm_2g."BTSTMASUBUNIT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CMEMODE",
        "CONNCN",
        "CONNPN",
        "CONNSN",
        "CONNSRN",
        "DEVICENO",
        "GAIN",
        "SUBUNITNO"
    FROM
    huawei_nbi_gsm."BTSTMASUBUNIT"

    """
)

BTSTRANS = ReplaceableObject(
    'huawei_cm_2g."BTSTRANS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "TRANSMODE"
    FROM
    huawei_nbi_gsm."BTSTRANS"

    """
)

BTSTRCMPR = ReplaceableObject(
    'huawei_cm_2g."BTSTRCMPR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "BTSTRCMPRATE"
    FROM
    huawei_nbi_gsm."BTSTRCMPR"

    """
)

BTSTRUSTCERT = ReplaceableObject(
    'huawei_cm_2g."BTSTRUSTCERT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CERTNAME"
    FROM
    huawei_nbi_gsm."BTSTRUSTCERT"

    """
)

BTSTRXBACKUP = ReplaceableObject(
    'huawei_cm_2g."BTSTRXBACKUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "TRXBPSW"
    FROM
    huawei_nbi_gsm."BTSTRXBACKUP"

    """
)

BTSVLAN = ReplaceableObject(
    'huawei_cm_2g."BTSVLAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DSCP",
        "SERVICETYPE",
        "VLANID",
        "VLANPRI",
        "VLANSWITCH"
    FROM
    huawei_nbi_gsm."BTSVLAN"

    """
)

BTSXFC = ReplaceableObject(
    'huawei_cm_2g."BTSXFC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISSIGCTRLSWITCH",
        "ABISSIGTYPE",
        "BTSID",
        "BTSSIGCTRLHIGHTHRESHOLD",
        "BTSSIGCTRLSTARTTHRESHOLD"
    FROM
    huawei_nbi_gsm."BTSXFC"

    """
)

BTSXMUFP = ReplaceableObject(
    'huawei_cm_2g."BTSXMUFP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "TRXPWRADJALLOW"
    FROM
    huawei_nbi_gsm."BTSXMUFP"

    """
)

CAB = ReplaceableObject(
    'huawei_cm_2g."CAB"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CABT",
        "CN",
        "PWRMODE"
    FROM
    huawei_nbi_gsm."CAB"

    """
)

CCGN = ReplaceableObject(
    'huawei_cm_2g."CCGN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CG"
    FROM
    huawei_nbi_gsm."CCGN"

    """
)

CELLBIND2BTS = ReplaceableObject(
    'huawei_cm_2g."CELLBIND2BTS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CELLID"
    FROM
    huawei_nbi_gsm."CELLBIND2BTS"

    """
)

CELLGLDSS = ReplaceableObject(
    'huawei_cm_2g."CELLGLDSS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "GLDSSSW"
    FROM
    huawei_nbi_gsm."CELLGLDSS"

    """
)

CERTCHKTSK = ReplaceableObject(
    'huawei_cm_2g."CERTCHKTSK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALMRNG",
        "ISENABLE",
        "PERIOD",
        "UPDATEMETHOD"
    FROM
    huawei_nbi_gsm."CERTCHKTSK"

    """
)

CERTMK = ReplaceableObject(
    'huawei_cm_2g."CERTMK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APPCERT"
    FROM
    huawei_nbi_gsm."CERTMK"

    """
)

CERTREQ = ReplaceableObject(
    'huawei_cm_2g."CERTREQ"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COMMNAME",
        "KEYSIZE",
        "KEYUSAGE",
        "LOCALIP",
        "LOCALNAME",
        "SIGNALG",
        "USERADDINFO"
    FROM
    huawei_nbi_gsm."CERTREQ"

    """
)

CLK = ReplaceableObject(
    'huawei_cm_2g."CLK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BACK8KCLKSW1",
        "BACK8KCLKSW2",
        "BT",
        "REF2MCLKSRC",
        "REF2MCLKSRCBAK",
        "REFUSELOCALCLK",
        "SN",
        "SRN",
        "SRT",
        "SUPPORTBAKCLKSRC"
    FROM
    huawei_nbi_gsm."CLK"

    """
)

CLKMODE = ReplaceableObject(
    'huawei_cm_2g."CLKMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CMEMODE"
    FROM
    huawei_nbi_gsm."CLKMODE"

    """
)

CLKSRC = ReplaceableObject(
    'huawei_cm_2g."CLKSRC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SRCGRD",
        "SRCT"
    FROM
    huawei_nbi_gsm."CLKSRC"

    """
)

CONNTYPE = ReplaceableObject(
    'huawei_cm_2g."CONNTYPE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CONNTYPE"
    FROM
    huawei_nbi_gsm."CONNTYPE"

    """
)

COPTLNK = ReplaceableObject(
    'huawei_cm_2g."COPTLNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BT",
        "E1T1PN",
        "J2MODE",
        "JAUTOADD",
        "PN",
        "PS",
        "SN",
        "SRN",
        "J2BYTE_FORMAT",
        "J2RXVALUE",
        "J2TXVALUE"
    FROM
    huawei_nbi_gsm."COPTLNK"

    """
)

CPUTHD = ReplaceableObject(
    'huawei_cm_2g."CPUTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BRDCLASS",
        "SSCPUAVEUSAGEALMTHD",
        "SSCPUMAXUSAGEALMTHD",
        "SSDSPAVEUSAGEALMTHD",
        "SSDSPMAXUSAGEALMTHD",
        "SSTHRUPUTAVEUSAGEALMTHD",
        "SSTHRUPUTMAXUSAGEALMTHD"
    FROM
    huawei_nbi_gsm."CPUTHD"

    """
)

CRLPOLICY = ReplaceableObject(
    'huawei_cm_2g."CRLPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CRLPOLICY"
    FROM
    huawei_nbi_gsm."CRLPOLICY"

    """
)

CSPRECTRL = ReplaceableObject(
    'huawei_cm_2g."CSPRECTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "UCCSPREFCALLREESTPRIO",
        "UCCSPREFCSEMERGCALLPRIO",
        "UCCSPREFCSORGCALLPRIO",
        "UCCSPREFCSTERMCALLPRIO",
        "UCCSPREFINBSCHOPRIO",
        "UCCSPREFINTRABSCHOPRIO",
        "UCCSPREFOTHERPRIO",
        "UCCSPREFPSPRIO",
        "UCCSPREFSUPPLEPRIO",
        "UCCSPREFVBSPRIO",
        "UCCSPREFVGCSPRIO"
    FROM
    huawei_nbi_gsm."CSPRECTRL"

    """
)

DEVIP = ReplaceableObject(
    'huawei_cm_2g."DEVIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DEVTYPE",
        "IPADDR",
        "REMARK",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."DEVIP"

    """
)

DEVRSVDPARA = ReplaceableObject(
    'huawei_cm_2g."DEVRSVDPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "RSVDPARA1",
        "RSVDPARA10",
        "RSVDPARA11",
        "RSVDPARA12",
        "RSVDPARA13",
        "RSVDPARA14",
        "RSVDPARA15",
        "RSVDPARA16",
        "RSVDPARA17",
        "RSVDPARA18",
        "RSVDPARA19",
        "RSVDPARA2",
        "RSVDPARA20",
        "RSVDPARA21",
        "RSVDPARA22",
        "RSVDPARA23",
        "RSVDPARA24",
        "RSVDPARA25",
        "RSVDPARA26",
        "RSVDPARA27",
        "RSVDPARA28",
        "RSVDPARA29",
        "RSVDPARA3",
        "RSVDPARA30",
        "RSVDPARA31",
        "RSVDPARA32",
        "RSVDPARA33",
        "RSVDPARA34",
        "RSVDPARA35",
        "RSVDPARA36",
        "RSVDPARA37",
        "RSVDPARA38",
        "RSVDPARA39",
        "RSVDPARA4",
        "RSVDPARA40",
        "RSVDPARA5",
        "RSVDPARA6",
        "RSVDPARA7",
        "RSVDPARA8",
        "RSVDPARA9",
        "RSVDSW1",
        "RSVDSW2",
        "RSVDSW3",
        "RSVDSW4",
        "RSVDSW5",
        "RSVDSW6",
        "RSVDSW7",
        "RSVDSW8"
    FROM
    huawei_nbi_gsm."DEVRSVDPARA"

    """
)

DSCPMAP = ReplaceableObject(
    'huawei_cm_2g."DSCPMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DSCP",
        "VLANPRI"
    FROM
    huawei_nbi_gsm."DSCPMAP"

    """
)

DSP = ReplaceableObject(
    'huawei_cm_2g."DSP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DSPN",
        "SN",
        "SRN",
        "TCTYPE",
        "TIMELEN"
    FROM
    huawei_nbi_gsm."DSP"

    """
)

DSPLVDSMODE = ReplaceableObject(
    'huawei_cm_2g."DSPLVDSMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LVDS252DSPNUM",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."DSPLVDSMODE"

    """
)

DXX = ReplaceableObject(
    'huawei_cm_2g."DXX"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DXXINDEX",
        "PORTNUM"
    FROM
    huawei_nbi_gsm."DXX"

    """
)

DXXCONNECT = ReplaceableObject(
    'huawei_cm_2g."DXXCONNECT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CIUSLOTNO",
        "CIUSUBRACKNO",
        "CONNECTPORTNO",
        "DXXINDEX",
        "PORTNO"
    FROM
    huawei_nbi_gsm."DXXCONNECT"

    """
)

DXXTSEXGRELATION = ReplaceableObject(
    'huawei_cm_2g."DXXTSEXGRELATION"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DXXINDEX",
        "INPORTNO",
        "INTSNO",
        "OUTPORTNO",
        "OUTPORTTS"
    FROM
    huawei_nbi_gsm."DXXTSEXGRELATION"

    """
)

E1T1 = ReplaceableObject(
    'huawei_cm_2g."E1T1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BERAUTOISOSW",
        "BT",
        "LOOPSW",
        "PN",
        "PS",
        "PTRXT",
        "PTTXT",
        "REMARK",
        "SN",
        "SRN",
        "WORKMODE"
    FROM
    huawei_nbi_gsm."E1T1"

    """
)

EMSIP = ReplaceableObject(
    'huawei_cm_2g."EMSIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EMSIP",
        "MASK",
        "OMUIP",
        "OMUMASK"
    FROM
    huawei_nbi_gsm."EMSIP"

    """
)

ENVALMPARA = ReplaceableObject(
    'huawei_cm_2g."ENVALMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "ALVL",
        "ANM",
        "ASS"
    FROM
    huawei_nbi_gsm."ENVALMPARA"

    """
)

ETHIP = ReplaceableObject(
    'huawei_cm_2g."ETHIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPADDR",
        "IPINDEX",
        "MASK",
        "PN",
        "REMARK",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."ETHIP"

    """
)

ETHPORT = ReplaceableObject(
    'huawei_cm_2g."ETHPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ARPBCPKTVLANFLAG",
        "AUTO",
        "BCPKTALARMCLRTHD",
        "BCPKTALARMTHD",
        "BRDTYPE",
        "CFMVER",
        "ERRDETECTSW",
        "FCINDEX",
        "FLOWCTRLSWITCH",
        "MTU",
        "OAMFLOWBW",
        "PN",
        "REMARK",
        "SN",
        "SRN",
        "TRMLOADTHINDEX",
        "FC",
        "PTYPE"
    FROM
    huawei_nbi_gsm."ETHPORT"

    """
)

ETHREDPORT = ReplaceableObject(
    'huawei_cm_2g."ETHREDPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PN",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."ETHREDPORT"

    """
)

ETHSWITCH = ReplaceableObject(
    'huawei_cm_2g."ETHSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BFTCHKSW",
        "FADETECTSW",
        "FAPOSTSW",
        "FLTDIAGSW1",
        "FLTDIAGSW2",
        "FLTDIAGSW3",
        "FLTDIAGSW4",
        "FLTDIAGSW5",
        "ISOLATEIOSW",
        "ISOLATESYSSW",
        "MPUMMUSW",
        "MSDETECTSW",
        "RESPARA1",
        "RESPARA2",
        "RESPARA5",
        "RESPARA63",
        "RESPARA64",
        "RESSW2",
        "RESSW3",
        "RESSW4",
        "RESSW5",
        "RESSW6"
    FROM
    huawei_nbi_gsm."ETHSWITCH"

    """
)

FACFG = ReplaceableObject(
    'huawei_cm_2g."FACFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FAMLINKUNSTABLECHKSW",
        "INTVAL",
        "LOGSW",
        "PERIOD",
        "RESSW",
        "XPUASINGLEPEMSW"
    FROM
    huawei_nbi_gsm."FACFG"

    """
)

FANSPEED = ReplaceableObject(
    'huawei_cm_2g."FANSPEED"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FANFLAG",
        "FANSPEEDMODE",
        "SRN"
    FROM
    huawei_nbi_gsm."FANSPEED"

    """
)

FCCOMMPARA = ReplaceableObject(
    'huawei_cm_2g."FCCOMMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BRDCLASS",
        "CPUCTHD",
        "CPULOGCTHD",
        "CPULOGRTHD",
        "CPUPMCTHD",
        "CPUPMRTHD",
        "CPUPRINTCTHD",
        "CPUPRINTRTHD",
        "CPUSMWINDOW",
        "CPUTRACECTHD",
        "CPUTRACERTHD",
        "FCSW",
        "FDWINDOW",
        "LOGSW",
        "MSGCTHD",
        "MSGLOGCTHD",
        "MSGLOGRTHD",
        "MSGPMCTHD",
        "MSGPMRTHD",
        "MSGPRINTCTHD",
        "MSGPRINTRTHD",
        "MSGSMWINDOW",
        "MSGTRACECTHD",
        "MSGTRACERTHD",
        "PMSW",
        "PRINTSW",
        "TRACESW"
    FROM
    huawei_nbi_gsm."FCCOMMPARA"

    """
)

filefooter = ReplaceableObject(
    'huawei_cm_2g."FILEFOOTER"',
    """

    SELECT 
        "FileName",
        "datetime"
    FROM
    huawei_nbi_gsm."filefooter"

    """
)

FTPCLTPORT = ReplaceableObject(
    'huawei_cm_2g."FTPCLTPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENDPORT",
        "STARTPORT"
    FROM
    huawei_nbi_gsm."FTPCLTPORT"

    """
)

FTPSCLT = ReplaceableObject(
    'huawei_cm_2g."FTPSCLT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENCRYMODE",
        "SPTSTATEFWL",
        "SSLCERTAUTH"
    FROM
    huawei_nbi_gsm."FTPSCLT"

    """
)

FTPSCLTDPORT = ReplaceableObject(
    'huawei_cm_2g."FTPSCLTDPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PORT",
        "SERVERIP"
    FROM
    huawei_nbi_gsm."FTPSCLTDPORT"

    """
)

FTPSRVSPD = ReplaceableObject(
    'huawei_cm_2g."FTPSRVSPD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FTPSPD"
    FROM
    huawei_nbi_gsm."FTPSRVSPD"

    """
)

FTPSSRV = ReplaceableObject(
    'huawei_cm_2g."FTPSSRV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACDPORTLWLT",
        "ACDPORTUPLT",
        "DFTPORTSWT",
        "ENCRYMODE"
    FROM
    huawei_nbi_gsm."FTPSSRV"

    """
)

G2GNCELL = ReplaceableObject(
    'huawei_cm_2g."G2GNCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADJHOOFFSET",
        "BETTERCELLLASTTIME",
        "BETTERCELLSTATTIME",
        "BQLASTTIME",
        "BQMARGIN",
        "BQNCELLABSTHRESSW",
        "BQSTATTIME",
        "CHAINNCELLTYPE",
        "DRHOLEVRANGE",
        "EDGEADJLASTTIME",
        "EDGEADJSTATTIME",
        "EDGEHOHYST",
        "EDOUTHOOFFSET",
        "GNCELLRANKPRI",
        "HCSLASTTIME",
        "HCSSTATTIME",
        "HOLASTTIME",
        "HOSTATICTIME",
        "HSRPNUSRNCTAG",
        "INTELEVHOHYST",
        "INTERCELLHYST",
        "ISCHAINNCELL",
        "LEVLAST",
        "LEVSTAT",
        "LOADHOPBGTMARGIN",
        "MINOFFSET",
        "NBR2GNCELLID",
        "NCELLPRI",
        "NCELLPUNEN",
        "NCELLPUNLEV",
        "NCELLPUNSTPTH",
        "NCELLPUNTM",
        "NCELLPWRCOMPVALUE",
        "NCELLTYPE",
        "PBGTLAST",
        "PBGTMARGIN",
        "PBGTSTAT",
        "SRC2GNCELLID",
        "SRCHOCTRLSWITCH",
        "TALASTTIME",
        "TASTATTIME",
        "ULBQLASTTIME",
        "ULBQSTATTIME"
    FROM
    huawei_nbi_gsm."G2GNCELL"

    """
)

G3GARFCN = ReplaceableObject(
    'huawei_cm_2g."G3GARFCN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INPUT3GARFCNEN"
    FROM
    huawei_nbi_gsm."G3GARFCN"

    """
)

G3GNCELL = ReplaceableObject(
    'huawei_cm_2g."G3GNCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ECNOOFF",
        "HODURT3G",
        "HODURT3GTDD",
        "HOSTAT3G",
        "HOSTAT3GTDD",
        "NBR3GNCELLID",
        "NCELLPRI",
        "RSCPOFF",
        "SRC3GNCELLID"
    FROM
    huawei_nbi_gsm."G3GNCELL"

    """
)

G_ADJMAP = ReplaceableObject(
    'huawei_cm_2g."G_ADJMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANI",
        "CNMNGMODE",
        "CNOPINDEX",
        "FTI",
        "ITFT",
        "TMIGLD"
    FROM
    huawei_nbi_gsm."G_ADJMAP"

    """
)

G_ADJNODE = ReplaceableObject(
    'huawei_cm_2g."G_ADJNODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANI",
        "ISIPPOOL",
        "NAME",
        "NODET",
        "BTSID"
    FROM
    huawei_nbi_gsm."G_ADJNODE"

    """
)

GAFCALMPARA = ReplaceableObject(
    'huawei_cm_2g."GAFCALMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AFCALARMCHECKTIME",
        "AFCALARMCLEARTHLD",
        "AFCALARMREPORTTHLD",
        "AFCALARMSW",
        "MINCRATMPTPERUNITTIME"
    FROM
    huawei_nbi_gsm."GAFCALMPARA"

    """
)

GALLCELLBLKSTAT = ReplaceableObject(
    'huawei_cm_2g."GALLCELLBLKSTAT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADMSTATOPTYPE",
        "STATOPTINTERVAL"
    FROM
    huawei_nbi_gsm."GALLCELLBLKSTAT"

    """
)

GBSCREDGRP = ReplaceableObject(
    'huawei_cm_2g."GBSCREDGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BEATSENDINGDIS",
        "GROUPINDEX",
        "GROUPNAME",
        "LOCALBSCID",
        "PEERBSCID"
    FROM
    huawei_nbi_gsm."GBSCREDGRP"

    """
)

GCELL = ReplaceableObject(
    'huawei_cm_2g."GCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTSTATUS",
        "ADMSTAT",
        "BCC",
        "BSPAGBLKSRES",
        "BSPBCCHBLKS",
        "BSPRACHBLKS",
        "CELLID",
        "CELLNAME",
        "CI",
        "CSDSP",
        "CSVSP",
        "EXTTP",
        "FLEXMAIO",
        "GLOCELLID",
        "HYBHIFREQBANDSUPPORT",
        "IUOTP",
        "LAC",
        "MCC",
        "MNC",
        "MOCNCMCELL",
        "NCC",
        "OPNAME",
        "PSHPSP",
        "PSLPSVP",
        "REMARK",
        "TYPE",
        "VIPCELL",
        "DBFREQBCCHIUO",
        "ENIUO"
    FROM
    huawei_nbi_gsm."GCELL"

    """
)

GCELL2GBA1 = ReplaceableObject(
    'huawei_cm_2g."GCELL2GBA1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELL2GBA1BCCH",
        "CELL2GBA1OPTSW",
        "CELL2GBA1TAG",
        "CELLID",
        "ITEM",
        "ITEMVALID",
        "CELL2GBA1OPTENHSW"
    FROM
    huawei_nbi_gsm."GCELL2GBA1"

    """
)

GCELL3GARFCN = ReplaceableObject(
    'huawei_cm_2g."GCELL3GARFCN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "INPUT3GARFCNEN"
    FROM
    huawei_nbi_gsm."GCELL3GARFCN"

    """
)

GCELLAMRQUL = ReplaceableObject(
    'huawei_cm_2g."GCELLAMRQUL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "DLQUALIMITAMRFR",
        "DLQUALIMITAMRHR",
        "RXLEVOFF",
        "RXQUAL1",
        "RXQUAL10",
        "RXQUAL11",
        "RXQUAL12",
        "RXQUAL2",
        "RXQUAL3",
        "RXQUAL4",
        "RXQUAL5",
        "RXQUAL6",
        "RXQUAL7",
        "RXQUAL8",
        "RXQUAL9",
        "ULQUALIMITAMRFR",
        "ULQUALIMITAMRHR"
    FROM
    huawei_nbi_gsm."GCELLAMRQUL"

    """
)

GCELLBASICPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLBASICPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSADJUST",
        "CALLRESTABDIS",
        "CELL8PSKPOWERLEVEL",
        "CELLID",
        "CELLSCENARIO",
        "CMEPRIOR",
        "DIRECTRYEN",
        "DIVERT16QAMDELAY",
        "DIVERT32QAMDELAY",
        "DIVERT8PSKDELAY",
        "DNPCEN",
        "DYNOPENTRXPOWER",
        "ENCRY",
        "ENCRYPTIONALGORITHM1ST",
        "ENCRYPTIONALGORITHM2ND",
        "ENCRYPTIONALGORITHM3RD",
        "ENCRYPTIONALGORITHM4TH",
        "ENCRYPTIONALGORITHM5TH",
        "ENCRYPTIONALGORITHM6TH",
        "ENCRYPTIONALGORITHM7TH",
        "FASTCALLTCHTHRESHOLD",
        "FRDLDTX",
        "FRULDTX",
        "GMSKDELAY",
        "GMSKDELAYDYNADJSW",
        "HIGHMODPWREN",
        "HRDLDTX",
        "HRULDTX",
        "ICBALLOW",
        "IMMASSCBB",
        "IMMASSEN",
        "IMMTCHLOADTHRES",
        "LAYER",
        "LEVELRPT",
        "MAXTA",
        "MICCSWITCH",
        "NBAMRTFOSWITCH",
        "PDCH2SDEN",
        "POWERREDUCE16QAM",
        "POWERREDUCE32QAM",
        "RTPSWITCH",
        "RXMIN",
        "SDDYN",
        "SVHOCNGSTTHR",
        "SVHODTXDTCTIMER",
        "SVHOHODELAYTIMER",
        "SVHOSWITCH",
        "TIMESLOTVOLADJALLOW",
        "UMAISSWITCH",
        "UPPCEN"
    FROM
    huawei_nbi_gsm."GCELLBASICPARA"

    """
)

GCELLBTSSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLBTSSOFTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "CELLID",
        "CROCALCHKSW",
        "CSEHTYP",
        "DRFURXOPTSW",
        "HOTATHD",
        "HOTATHDSW",
        "IMMASSTBFRETXSW",
        "INTERFBANDEMG",
        "PAGINGOVERRPTTHRD",
        "RFCONNINSPECT",
        "RXCHANALMTHD",
        "SAICDETTYP",
        "TBFASSADJSW"
    FROM
    huawei_nbi_gsm."GCELLBTSSOFTPARA"

    """
)

GCELLCCACCESS = ReplaceableObject(
    'huawei_cm_2g."GCELLCCACCESS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BHPREPOLICY",
        "CELLID",
        "CELLTCHREQARRRTCTRLSW",
        "CHREQCSMSGMAXNUMINPERIOD",
        "CHREQPSMSGMAXNUMINPERIOD",
        "LOCUPDMSGMAXNUMINPERIOD",
        "PSRACHACCLEV",
        "PWRDIV",
        "PWRDIVIND",
        "RACHACCLEV",
        "RANERRTHRED",
        "TRXAIDSWITCH",
        "VOICEVER"
    FROM
    huawei_nbi_gsm."GCELLCCACCESS"

    """
)

GCELLCCAD = ReplaceableObject(
    'huawei_cm_2g."GCELLCCAD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ASSQUELEN",
        "ASSRETRYMAX",
        "CELLID",
        "CELLSELECTAFTERCALLREL",
        "DNSENDSMDIS",
        "EMCALLDIRRETRYOPT",
        "EMCPRILV",
        "FSTRTNTDDWITHOUTMR",
        "MAXTADROPCALLFILTER",
        "MAXTADROPCALLOPTSW",
        "MAXTADROPCALLSWITCH",
        "MAXTADROPCALLTHRESHOLD",
        "POSSI13",
        "PREEMPTIONPERMIT",
        "REASSFREQBAND",
        "TAADJINTV",
        "TAADJOPTSW",
        "UPSENDSMDIS"
    FROM
    huawei_nbi_gsm."GCELLCCAD"

    """
)

GCELLCCAMR = ReplaceableObject(
    'huawei_cm_2g."GCELLCCAMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACSSETF",
        "ACSSETH",
        "ACTCDSETF",
        "ACTCDSETH",
        "ACTCDSETWB",
        "AMRDADTHAW",
        "AMRRATEADJOPTALG",
        "AMRUADTHAW",
        "CELLID",
        "DLHYSTF1",
        "DLHYSTF2",
        "DLHYSTF3",
        "DLHYSTH1",
        "DLHYSTH2",
        "DLHYSTH3",
        "DLHYSTWB1",
        "DLHYSTWB2",
        "DLLTFERLOWTH",
        "DLLTFERTGT",
        "DLLTFERUPTH",
        "DLLTTHADJFA",
        "DLTHF1",
        "DLTHF2",
        "DLTHF3",
        "DLTHH1",
        "DLTHH2",
        "DLTHH3",
        "DLTHWB1",
        "DLTHWB2",
        "INITCDMDF",
        "INITCDMDH",
        "INITCDMDWB",
        "LTFERLOWTH",
        "LTFERTGT",
        "LTFERUPTH",
        "LTTHADJFA",
        "RATECTRLSW",
        "RATSCCHENABLED",
        "ULHYSTF1",
        "ULHYSTF2",
        "ULHYSTF3",
        "ULHYSTH1",
        "ULHYSTH2",
        "ULHYSTH3",
        "ULHYSTWB1",
        "ULHYSTWB2",
        "ULTHF1",
        "ULTHF2",
        "ULTHF3",
        "ULTHH1",
        "ULTHH2",
        "ULTHH3",
        "ULTHWB1",
        "ULTHWB2"
    FROM
    huawei_nbi_gsm."GCELLCCAMR"

    """
)

GCELLCCBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLCCBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACCCTRLEN",
        "AFRDSBLCNT",
        "AFRSAMULFRM",
        "AHRDSBLCNT",
        "AHRSAMULFRM",
        "ASSLOADJUDGEEN",
        "CELLID",
        "COMMACC",
        "DTLOADTHRED",
        "ECSC",
        "EMLPPEN",
        "ERGCALLDIS",
        "MBR",
        "MSMAXRETRAN",
        "PAGTIMES",
        "RACHBUSYTHRED",
        "REASSEN",
        "REPEATDLFASET",
        "REPEATDLFATHRED",
        "REPEATSADLTHD",
        "REPEATSASET",
        "REPEATSAULTHD",
        "RLT",
        "SAMULFRM",
        "SATIMEROPTSW",
        "SPECACC",
        "UMSFRBERTHRESH",
        "UMSFRLLRFACTOR",
        "UMSFRLLRTHRESH",
        "UMSFRSWITCH"
    FROM
    huawei_nbi_gsm."GCELLCCBASIC"

    """
)

GCELLCCCH = ReplaceableObject(
    'huawei_cm_2g."GCELLCCCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISFCEN",
        "CANPC",
        "CCCHLOADINDPRD",
        "CCCHLOADTHRES",
        "CELLID",
        "DYNCCCHSWITCH",
        "FMSMAXOPCC",
        "HRATESPT",
        "OVERLOADINTV",
        "PAGINGOVLDPROCOPTSW",
        "PAGINGREORGLAGTM",
        "PAGINGREORGSTARTTHRD",
        "PAGINGREORGSTOPTHRD",
        "PAGINGREORGSW",
        "PCHMSGPRIORSW",
        "RACHLDAVERSLOT",
        "RACHLOADALM",
        "RFRESINDPRD"
    FROM
    huawei_nbi_gsm."GCELLCCCH"

    """
)

GCELLCCTMR = ReplaceableObject(
    'huawei_cm_2g."GCELLCCTMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "IMMASSRESENDEN",
        "N200PARASWITCH",
        "T200FACCHF",
        "T200FACCHH",
        "T200SACCH3",
        "T200SACCHS",
        "T200SACCT0",
        "T200SDCCH",
        "T200SDCCH3",
        "N200ESTAB",
        "N200FFULL",
        "N200FHALF",
        "N200REL",
        "N200SACCH",
        "N200SDCCH"
    FROM
    huawei_nbi_gsm."GCELLCCTMR"

    """
)

GCELLCCUTRANSYS = ReplaceableObject(
    'huawei_cm_2g."GCELLCCUTRANSYS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BESTTDDCELLNUM",
        "CELL1800OFF",
        "CELL1800THRED",
        "CELL900OFF",
        "CELL900THRED",
        "CELLID",
        "EMRMSCAPIDESWITCH",
        "EMRMSCAPPROSWITCH",
        "FDDCELLOFF",
        "FDDCELLTHRED",
        "FDDFREQCNUM",
        "FDDQMIN",
        "FDDQMINOFFSET",
        "FDDQOFF",
        "FDDREP",
        "FDDRPTTHRESHOLD2ECNO",
        "FDDRPTTHRESHOLD2RSCP",
        "FDDRSCPMIN",
        "FIRSTSI2QUATERMSGOPTSW",
        "GSMFREQCNUM",
        "INVALBSICEN",
        "MEASURETYPE",
        "MSCVER",
        "POS2QUATER",
        "QCI",
        "QI",
        "QP",
        "QSEARCHC",
        "SCALEORDER",
        "SEARCH3G",
        "SI2QUATEROPTIMIZEDALLOWED",
        "TDDCELLOFF",
        "TDDCELLRESELDIV",
        "TDDCELLTHRED",
        "TDDMIOPTIMIZEDALLOWED",
        "TDDMIPROHIBIT",
        "TDDSIOPTIMIZEDALLOWED"
    FROM
    huawei_nbi_gsm."GCELLCCUTRANSYS"

    """
)

GCELLCHMGAD = ReplaceableObject(
    'huawei_cm_2g."GCELLCHMGAD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRLOADOPTEN",
        "AMRTCHHPRIORALLOW",
        "AMRTCHHPRIORLOAD",
        "ASSOLRXLEVOFFSET",
        "BTRXPRIORITYSWITCH",
        "CELLID",
        "CELLOPPWRGRP",
        "CHALLOCATIONOPTSWITCH",
        "CHANINTERMESALLOW",
        "CHPWRINSUFFALLOWED",
        "CIRESTVALUE",
        "DLINTERFLEVLIMIT",
        "DLINTERFQUALLIMIT",
        "FREQLOADSHARETRAFFTHRSH",
        "HALFRATEREPACKINGSWITCH",
        "HISPRIOALLOW",
        "HOOLRXLEVOFFSET",
        "HRIUOLDRATESELALLOW",
        "HSCSDBUSYTHRES",
        "IBCAAFRSOFTBLKTHRD",
        "IBCAAHRSOFTBLKTHRD",
        "IBCAALLOWED",
        "IBCAASSWAITMEASURERPTTIME",
        "IBCACALLINFOFILTERLEN",
        "IBCACALLSOFTBLOCKTHOFFSET",
        "IBCACALLTARGETCIROFFSET",
        "IBCACIRESTENHANCE",
        "IBCADLPATHLOSSOFF",
        "IBCAEHOASSWAITMEASURERPTTIME",
        "IBCAESTMTSCCOLLISIONALLOW",
        "IBCAFLEXTSCALLOWED",
        "IBCAFORCEDBTSSYNCALLOWED",
        "IBCAFREEBCCHCHANTHRSHOLD",
        "IBCAFREVLOPT",
        "IBCAFRSOFTBLKTHRD",
        "IBCAGETINTFSRCOPT",
        "IBCAHOASSWAITMEASURERPTTIME",
        "IBCAHOSOFTBLKTHRESHOLD",
        "IBCAHRSOFTBLKTHRD",
        "IBCAICDMRELEVOFFSET",
        "IBCAICDMSWITCH",
        "IBCAINITPCRXLEVDLOFFSET",
        "IBCAINITPCRXLEVULOFFSET",
        "IBCAINITPCRXQUALDLOFFSET",
        "IBCAINITPCRXQUALULOFFSET",
        "IBCAIUOPATHLOSSOFF",
        "IBCAMAIOUSMTD",
        "IBCAMAXINTFSRCNUM",
        "IBCANCELLPATHLOSSESTIMATE",
        "IBCANEWCALLCIROFFSET",
        "IBCANHOASSWAITMEASURERPTTIME",
        "IBCANONMEANCELLSTATNUM",
        "IBCAOPRREVISEFACTOR",
        "IBCAPATHLOSSOFF",
        "IBCAPDCHDYNTRANTMR",
        "IBCAPDDYNTRENHANCE",
        "IBCAPLFILTFACTOR",
        "IBCAQUEUEOPT",
        "IBCASCELLPATHLOSS",
        "IBCASOFTBLKSAICOFF",
        "IBCASOFTBLKSWITCH",
        "IBCASUBCHNHANDOVERALLOWED",
        "IBCATARGETCIRTHRSH",
        "IBCAUSEDIUOSUBLAY",
        "IBCAUSRDYNCMEASURENCELL",
        "IBCAWAFRSOFTBLKTHRD",
        "INNAMRTCHHPRIORLOAD",
        "INTERFPRIALLOW",
        "JUDGERXLEVWHENASSIGNHR",
        "LOADSHAREALLOW",
        "LOADSTATYPE",
        "LOOSESDCCHLOADTHRED",
        "LOWRXLEVOLFORBIDOPTSW",
        "LOWRXLEVOLFORBIDSWITCH",
        "MCPACHAPPOPT",
        "MCPALOWTRAFFICTH",
        "MCPAOPTALG",
        "MINRXLEVWHENASSIGNHR",
        "MTSTURNOFFALG",
        "MTSTURNOFFHYST",
        "MTSTURNOFFTH",
        "NAMRLFRMTRXALLOWED",
        "OUTAMRTCHHPRIORLOAD",
        "PWRPRIORALLOW",
        "QLENSD",
        "QLENSI",
        "QTRUDNPWRLASTTIME",
        "QTRUDNPWRSTATTIME",
        "QTRUPWRSHARE",
        "QUALHOPRIALLOW",
        "SCENELOADTYPE",
        "SSLENSD",
        "SSLENSI",
        "TCHBUSYTHRES",
        "TCHLOADOPTSWITCH",
        "TCHREQSUSPENDINTERVAL",
        "TCHTRIBUSYUNDERLAYTHR",
        "TCHTRICBUSYOVERLAYTHR",
        "TIGHTBCCHASSMAINBCCHLEV",
        "TIGHTBCCHASSMAINBCCHQUAL",
        "TIGHTSDCCHRXLEVTHRED",
        "TRXPRIALLOW",
        "TURNOFFLOADTYPE",
        "UPINTERFQUALLIMIT",
        "UPINTERLEVLIMIT",
        "UPRXLEVLASTTIME",
        "UPRXLEVSMOOTHPARA",
        "UPRXLEVSTATICTIME",
        "VAMOSAHSUSERDLSOFTBLOCKTHD",
        "WAITSDCCHIDLETIMER"
    FROM
    huawei_nbi_gsm."GCELLCHMGAD"

    """
)

GCELLCHMGBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLCHMGBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALLOWAMRHALFRATEUSERPERC",
        "ALLOWHALFRATEUSERPERC",
        "CELLID",
        "CELLMAXSD",
        "CHALLOCSTRATEGY",
        "DIFFBANDSDCCHDYNADJ",
        "DIFFBANDSDCCHUSINGOPTIMIZE",
        "DYNPBTSUPPORTED",
        "ENTCHADJALLOW",
        "FACTORYMODE",
        "GRADEACCALLOW",
        "HIGHPRIUSERQUALFIRST",
        "IDLESDTHRES",
        "IMMASSDIFFBANDALLOCTCHSW",
        "INTOCELLRESVCHANNUM",
        "MAINBCCHSDCCHNUM",
        "MINRESTIMETCH",
        "RSVCHMFORECNUM",
        "SDBACKTOTCHPUNISHSWITCH",
        "SDCCHDYNADJTSNUM",
        "SDDYNADJRSVTCHNUM",
        "SDDYNADJRSVTCHSWITCH",
        "TIGHTBCCHSWITCH"
    FROM
    huawei_nbi_gsm."GCELLCHMGBASIC"

    """
)

GCELLCONGACALGO = ReplaceableObject(
    'huawei_cm_2g."GCELLCONGACALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "IACCSW"
    FROM
    huawei_nbi_gsm."GCELLCONGACALGO"

    """
)

GCELLCSFBPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLCSFBPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "CSFBFASTRETURNBASECFGSW",
        "UFCSFBSTATINTERRANHO",
        "ULTRAFLASHCSFBSAILAC",
        "ULTRAFLASHCSFBSAIMCC",
        "ULTRAFLASHCSFBSAIMNC",
        "ULTRAFLASHCSFBSAISAC",
        "ULTRAFLASHCSFBSW"
    FROM
    huawei_nbi_gsm."GCELLCSFBPARA"

    """
)

GCELLDYNTURNOFF = ReplaceableObject(
    'huawei_cm_2g."GCELLDYNTURNOFF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "TURNOFFENABLE",
        "PROTECTTIME",
        "SAMECVGCELLID",
        "SAMECVGCELLLOADSTATTM",
        "SAMECVGCELLLOADTHRD",
        "TURNOFFCELLCHANNUM",
        "TURNOFFCELLSTPTIME",
        "TURNOFFCELLSTRTIME",
        "TURNONCELLLOADTHRD"
    FROM
    huawei_nbi_gsm."GCELLDYNTURNOFF"

    """
)

GCELLEGPRSPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLEGPRSPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADJUSTULMCSTYPE",
        "BEPPERIOD",
        "CELLID",
        "CHOOSEBEPMAP",
        "DLPRIORITYDEGRADEULMCS",
        "DNDEFAULTMCS",
        "DNE2ADEFAULTMCS",
        "DNE2AFIXMCS",
        "DNFIXMCS",
        "EGPRSDLIRLAFLTMODE",
        "ESTULONDLCHOOSECS",
        "LQCMODE",
        "MSREACTIONADJULMCSSW",
        "NODATAREPORTBEP",
        "SELECTCSMAP",
        "ULCVBEPDEGRADELEVEL",
        "ULFIRSTBLKCHANGECS",
        "ULLQCAUTOADJSW",
        "ULMEANBEPDEGRADELEVEL",
        "UPDEFAULTMCS",
        "UPE2ADEFAULTMCS",
        "UPE2AFIXMCS",
        "UPFIXMCS",
        "USEHISTORYCS"
    FROM
    huawei_nbi_gsm."GCELLEGPRSPARA"

    """
)

GCELLEXTMSRPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLEXTMSRPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "EXTMEASORD",
        "EXTRPTPERIOD",
        "EXTRPTTYPE",
        "INTFREQUENCY",
        "NCCPERMITED"
    FROM
    huawei_nbi_gsm."GCELLEXTMSRPARA"

    """
)

GCELLFREQ = ReplaceableObject(
    'huawei_cm_2g."GCELLFREQ"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "FREQ1",
        "FREQ2",
        "FREQ3",
        "FREQ4",
        "FREQ5",
        "FREQ6",
        "FREQ7",
        "FREQ8",
        "FREQ9",
        "FREQ10",
        "FREQ11"
    FROM
    huawei_nbi_gsm."GCELLFREQ"

    """
)

GCELLFREQSCAN = ReplaceableObject(
    'huawei_cm_2g."GCELLFREQSCAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "FREQLST",
        "LOCGRPNO",
        "STRTM",
        "TIME"
    FROM
    huawei_nbi_gsm."GCELLFREQSCAN"

    """
)

GCELLGPRS = ReplaceableObject(
    'huawei_cm_2g."GCELLGPRS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "DLDCSPT",
        "EDGE",
        "EGPRS2A",
        "ENACCSPT",
        "ENC2SPT",
        "GPRS",
        "NACCSPT",
        "NC2SPT",
        "PKTSI",
        "PSPAGINGCTRL",
        "RA",
        "SPTDPI",
        "SPTINTERRATINBSCPSHO",
        "SPTINTERRATOUTBSCPSHO",
        "SPTLTEINBSCPSHO",
        "SPTLTEOUTBSCPSHO",
        "SPTREDUCELATENCY",
        "SUPPORTDTM",
        "SUPPORTEDA",
        "DPIPARATRANMODE"
    FROM
    huawei_nbi_gsm."GCELLGPRS"

    """
)

GCELLGSMR = ReplaceableObject(
    'huawei_cm_2g."GCELLGSMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "CRMSGRESENDINT",
        "CRMSGRESENDNUM",
        "DLTESTRESENDINT",
        "DLTESTRESENDNUM",
        "DTRTYPE",
        "EMLPPPRIORITY",
        "FACCHRESENDINT",
        "FACCHSENDNOTMSGIND",
        "FACCHSENDPGMSGIND",
        "GCSCHNASSULCHNEN",
        "GCSIMPREEMPTIONEN",
        "GSMRCSSENDNOTIFMODE",
        "GSMRPSSENDNOTIFMODE",
        "NCHOCBLOCKNUM",
        "NCHSTARTBLOCK",
        "NY2",
        "SENDFACCHNOTPRI",
        "SENDFACCHPAGPRI",
        "T3115",
        "TALKERINFINT",
        "UIC",
        "VGCSMAXNUM",
        "VGCSPREEMPT",
        "VGCSRSRVNUM"
    FROM
    huawei_nbi_gsm."GCELLGSMR"

    """
)

GCELLHO2GBA2 = ReplaceableObject(
    'huawei_cm_2g."GCELLHO2GBA2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELL2GBA2BCCH",
        "CELL2GBA2OPTSW",
        "CELL2GBA2TAG",
        "CELLID",
        "ITEM",
        "ITEMVALID",
        "CELL2GBA2OPTENHSW"
    FROM
    huawei_nbi_gsm."GCELLHO2GBA2"

    """
)

GCELLHOAD = ReplaceableObject(
    'huawei_cm_2g."GCELLHOAD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABCDOWNQUALITY",
        "ABCUPQUALITY",
        "ABCWAITMAXTIME",
        "ACCTHRESLAYER",
        "ASSIGNBETTERCELLEN",
        "BANTIME",
        "CELLID",
        "CONTINTV",
        "HOTRYCNT",
        "INTERFEREDLEVOFF",
        "INTERFEREDLEVOFFOL",
        "INTERFEREDLQUALOFFOL",
        "INTERFEREDQUALOFF",
        "INTERFEREULEVOFF",
        "INTERFEREULEVOFFOL",
        "INTERFEREULQUALOFFOL",
        "INTERFEREUQUALOFF",
        "INTERFEROFFSWITCHOL",
        "KBIAS",
        "LAYHOLOADTH",
        "LOADACCTHRES",
        "LOADHOAD",
        "LOADHOHYSTADAPEN",
        "LOADHOPERIOD",
        "LOADHOSTEP",
        "LOADHOUSRRATIO",
        "LOADOFFSET",
        "MAXCNTNUM",
        "MAXRESEND",
        "OUTBSCLOADHOEN",
        "QCKSTATCNT",
        "QCKTIMETH",
        "QCKTRUECNT",
        "SDCCHWAITMREN",
        "SDCCHWAITMRTIMELEN",
        "SPEEDPUNISH",
        "SPEEDPUNISHT",
        "SYSFLOWLEV",
        "T3105",
        "TIGHTBCCHHOLOADTHRES",
        "TIGHTBCCHRXQUALTHRES",
        "TRIGTHRES",
        "TRIGTHRESLAYER"
    FROM
    huawei_nbi_gsm."GCELLHOAD"

    """
)

GCELLHOBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLHOBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRF2HHOQUALTHFINE",
        "AMRFULLTOHALFHOALLOW",
        "AMRFULLTOHALFHOATCBADJSTEP",
        "AMRFULLTOHALFHOATCBTHRESH",
        "AMRFULLTOHALFHOPATHADJSTEP",
        "AMRFULLTOHALFHOPATHTHRESH",
        "AMRFULLTOHALFHOQUALTHRESH",
        "AMRFULLTOHALFHOTHRESH",
        "AMRH2FHOOPTSW",
        "AMRH2FHOQUALFINE",
        "AMRHALFTOFULLHOATCBTHRESH",
        "AMRHALFTOFULLHOPATHTHRESH",
        "AMRHALFTOFULLHOQUALALLOW",
        "AMRHALFTOFULLHOQUALTHRESH",
        "AMRHALFTOFULLHOTHRESH",
        "ATCBHOEN",
        "BADQUALHOOPTALLOW",
        "BQHOEN",
        "CELLID",
        "COBSCMSCADJEN",
        "CONHOEN",
        "DLEDGETHRES",
        "EDGEHOHYSTEN",
        "EDGELAST1",
        "EDGESTAT1",
        "EDOUTHOADEN",
        "F2HHOLOADSTFSWITCH",
        "FHGAINOFFSET",
        "FRINGEHOEN",
        "FULLTOHALFHOATCBOFFSET",
        "FULLTOHALFHODURATION",
        "FULLTOHALFHOLASTTIME",
        "FULLTOHALFHOLOADSTF",
        "FULLTOHALFHOPATHOFFSET",
        "FULLTOHALFHOPERIOD",
        "FULLTOHALFHOSTATTIME",
        "HALFTOFULLATCBOFFSET",
        "HALFTOFULLHODURATION",
        "HALFTOFULLHOLASTTIME",
        "HALFTOFULLHOPATHOFFSET",
        "HALFTOFULLHOSTATTIME",
        "HOCDCMINDWPWR",
        "HOCDCMINUPPWR",
        "HOCDCOVERLODEHOEN",
        "HOCTRLSWITCH",
        "HOPRIOMODEN",
        "HOTHRES",
        "INFHHOLAST",
        "INFHHOSTAT",
        "INHOF2HTH",
        "INHOH2FTH",
        "INTERFHOEN",
        "INTERHOOPTALLOW",
        "INTERRATCELLRESELEN",
        "INTERRATDIFFPROCSW",
        "INTERRATINBSCHOEN",
        "INTERRATIURGINBSCHOEN",
        "INTERRATIURGVOICECARRYEN",
        "INTERRATOUTBSCHOEN",
        "INTRACELLFHHOEN",
        "INTRACELLFHOPTSWITCH",
        "INTRACELLHOEN",
        "INTRACELLSINUSEREN",
        "LEVHOEN",
        "LEVHOHYST",
        "LOADHOEN",
        "LTECELLRESELEN",
        "LTESAILAC",
        "LTESAIMCC",
        "LTESAIMNC",
        "LTESAISAC",
        "MRINTRPLOPTSWITCH",
        "NOAMRF2HHOQUALTHFINE",
        "NOAMRFULLTOHALFHOALLOW",
        "NOAMRFULLTOHALFHOATCBADJSTEP",
        "NOAMRFULLTOHALFHOATCBTHRESH",
        "NOAMRFULLTOHALFHOPATHADJSTEP",
        "NOAMRFULLTOHALFHOPATHTHRESH",
        "NOAMRFULLTOHALFHOQUALTHRESH",
        "NOAMRFULLTOHALFTHRESH",
        "NOAMRH2FHOQUALFINE",
        "NOAMRHALFTOFULLHOATCBTHRESH",
        "NOAMRHALFTOFULLHOPATHTHRESH",
        "NOAMRHALFTOFULLHOQUALALLOW",
        "NOAMRHALFTOFULLHOQUALTHRESH",
        "NOAMRHALFTOFULLTHRESH",
        "PBGTHOEN",
        "QCKMVHOEN",
        "QUICKHOEN",
        "QUICKPBGTHOEN",
        "RXQCKFALLHOEN",
        "SIGCHANHOEN",
        "SRVCCHOEN",
        "TAHOEN",
        "TIGHTBCCHHOLASTTIME",
        "TIGHTBCCHHOSTATTIME",
        "ULEDGETHRES",
        "ULMCRITOPTSW",
        "BETTERCELLHOEN",
        "EDGELAST",
        "EDGESTAT",
        "INTERFERELASTTIME",
        "INTERFERESTATTIME",
        "PATHLOSSHOEN"
    FROM
    huawei_nbi_gsm."GCELLHOBASIC"

    """
)

GCELLHOCTRL = ReplaceableObject(
    'huawei_cm_2g."GCELLHOCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BCCHHOPHOCOMPOPT",
        "BSMSPWRLEV",
        "BTSMESRPTPREPROC",
        "CELLID",
        "CONTHOMININTV",
        "INRBSCSDHOEN",
        "MINPWRLEVDIRTRY",
        "MRPREPROCFREQ",
        "NEWURGHOMININTV",
        "PENALTYEN",
        "PRIMMESPPT",
        "SDHOMININTV",
        "TCHHOMININTV",
        "ULRXLEVBOUNDPROTECTIONSW"
    FROM
    huawei_nbi_gsm."GCELLHOCTRL"

    """
)

GCELLHOEDBPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLHOEDBPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ATCBHYST",
        "ATCBTHRED",
        "CELLID",
        "EDBDIRECTPUNISHSW",
        "EDBLASTTIME",
        "EDBSTATTIME",
        "EDBSYSFLOWLEV",
        "HOPENALTYTIME",
        "INNASSOPTEN",
        "INNCELLEDGEHOEN",
        "INNLOADHOEN",
        "INNLOADHOPERI",
        "INNLOADHOSTEP",
        "INNSERIOVERLDTHRED",
        "INTOINNREXLEVTHRED",
        "OUTASSOPTEN",
        "OUTGENOVERLDTHRED",
        "OUTINNREXLEVTHRED",
        "OUTLOADHOENABLE",
        "OUTLOADHOMODPERI",
        "OUTLOADHOPERIOD",
        "OUTLOADHOSTEP",
        "OUTLOWLOADTHRED",
        "OUTSERIOVERLDTHRED"
    FROM
    huawei_nbi_gsm."GCELLHOEDBPARA"

    """
)

GCELLHOEMG = ReplaceableObject(
    'huawei_cm_2g."GCELLHOEMG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "DLQUALIMIT",
        "FLTPARAA1",
        "FLTPARAA2",
        "FLTPARAA3",
        "FLTPARAA4",
        "FLTPARAA5",
        "FLTPARAA6",
        "FLTPARAA7",
        "FLTPARAA8",
        "FLTPARAB",
        "HOCTRLSWITCH",
        "NODLMRHOALLOWLIMIT",
        "NODLMRHOEN",
        "NODLMRHOLASTTIME",
        "NODLMRHOQUALLIMIT",
        "NODLMRHOSTATTIME",
        "TALIMIT",
        "ULQUALIMIT"
    FROM
    huawei_nbi_gsm."GCELLHOEMG"

    """
)

GCELLHOFAST = ReplaceableObject(
    'huawei_cm_2g."GCELLHOFAST"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AFCHOLASTTIME",
        "AFCHOSTATTIME",
        "CELLID",
        "HODIRFORECASTEN",
        "HODIRLASTTIME",
        "HODIRSTATIME",
        "HODOWNTRIGE",
        "HOOFFSET",
        "HOPUNISHVALUE",
        "HOUPTRIGE",
        "IGNOREMRNUM",
        "MOVESPEEDTHRES",
        "MSLEVSTRQPBGT",
        "NCELLFILTER",
        "QUICKHOPUNISHSW",
        "SCELLFILTER",
        "TIMEPUNISH"
    FROM
    huawei_nbi_gsm."GCELLHOFAST"

    """
)

GCELLHOFDDBA2 = ReplaceableObject(
    'huawei_cm_2g."GCELLHOFDDBA2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "DF",
        "DIVERSITY",
        "FDDBA2TAG",
        "ITEM",
        "ITEMVALID",
        "SCRAMBLE"
    FROM
    huawei_nbi_gsm."GCELLHOFDDBA2"

    """
)

GCELLHOFITPEN = ReplaceableObject(
    'huawei_cm_2g."GCELLHOFITPEN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CBSIGNLEN",
        "CBTRAFFLEN",
        "CELLID",
        "DATAQUAFLTLEN",
        "DATASTRFLTLEN",
        "DATASTRUPFLTLEN",
        "DTXMEASUSED",
        "FAILSIGSTRPUNISH",
        "HOCTRLSWITCH",
        "INITUPFILEN",
        "LOADHOPUNISHINHERITSWITCH",
        "MBSIGNLEN",
        "MBTRAFFLEN",
        "MRMISSCOUNT",
        "NCELLFLTLEN",
        "NRBSDCCHFFLEN",
        "NRBTCHFFLEN",
        "PENALTYTIMER",
        "RQSIGNLEN",
        "RQTRAFFLEN",
        "RSCPENALTYTIMER",
        "SIGQUAFLTLEN",
        "SIGSTRFLTLEN",
        "SIGSTRUPFLTLEN",
        "SSBQPUNISH",
        "SSTAPUNISH",
        "TAFLTLEN",
        "TIMEAMRFHPUNISH",
        "TIMEBQPUNISH",
        "TIMETAPUNISH",
        "UMPENALTYTIMER",
        "INTERFEREHOPENTIME",
        "LOADHOPENTIME",
        "LOADHOPENVALUE",
        "NSIGSTRFLTLEN",
        "TASIGSTRFLTLEN"
    FROM
    huawei_nbi_gsm."GCELLHOFITPEN"

    """
)

GCELLHOINTERRATLDB = ReplaceableObject(
    'huawei_cm_2g."GCELLHOINTERRATLDB"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "DLLDRTHRD2GCELL",
        "DLOLCTHRD2GCELL",
        "G2GLOADADJUSTCOEFF",
        "INTERRATCSSERVICELOADHOTHRD",
        "INTERRATLOADHOECNOBANDWIDTH",
        "INTERRATLOADHOECNOSTART",
        "INTERRATLOADHOECNOSTEP",
        "INTERRATLOADHORSCPBANDWIDTH",
        "INTERRATLOADHORSCPSTART",
        "INTERRATLOADHORSCPSTEP",
        "INTERRATSERVICELOADHOSWITCH",
        "INTRATLOADHOECNOTHR",
        "INTRATLOADHOPERIOD",
        "INTRATLOADHORSCPTHR",
        "OUTSYSLOADHOEN",
        "ULLDRTHRD2GCELL",
        "ULOLCTHRD2GCELL"
    FROM
    huawei_nbi_gsm."GCELLHOINTERRATLDB"

    """
)

GCELLHOIUO = ReplaceableObject(
    'huawei_cm_2g."GCELLHOIUO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACCESSOPTILAY",
        "CELLID",
        "ENGOVERLDTHRHYST",
        "ENGOVERLDTHRSH",
        "ENGOVERLDTHRSHOL",
        "ENLDHOPRD",
        "ENLDHOSTP",
        "ENLOWLDTHRSH",
        "ENSOVERLDTHRSH",
        "HOALGOPERMLAY",
        "HOCTRLSWITCH",
        "IMMASSTAALLOW",
        "IMMASSTATHRES",
        "IUOALLOCCHANTRAFALLOW",
        "IUOCHOSENINASS",
        "IUOHODURATIME",
        "IUOHOSTATIME",
        "IUOOLPOWERCOMPPOLICY",
        "OLTOULHOALLOW",
        "OLTOULHOLEVADJSW",
        "OPTILAYER",
        "OPTILEVTHRES",
        "OPTITATHRES",
        "OTOURECEIVETH",
        "PSIUODLINITONLYULSW",
        "PSOTOURECEIVETHRSH",
        "PSTAFORUOHOALLOW",
        "PSUTOORECEIVETHRSH",
        "RECEIVEQUALTHRSHAMRFR",
        "RECEIVEQUALTHRSHAMRHR",
        "RECLEVHYST",
        "RECLEVTHRES",
        "RECLEVUOHOALLOW",
        "RECQUALTH",
        "RECQUALUOHOALLOW",
        "SIGAMPTDIFF",
        "SIGAMPTDIFFOPTALLOW",
        "TAFORUOHOALLOW",
        "TAHYST",
        "TATHRES",
        "TIMEOTOUFAILPUN",
        "TIMEUTOOFAILPUN",
        "ULTOOLHOALLOW",
        "ULTOOLHOOVERLOADJUDGESW",
        "ULTOOLRXLEVSELSW",
        "UOLOADOPTSWITCH",
        "UTOOFAILMAXTIME",
        "UTOOHOPENTIME",
        "UTOORECTH",
        "UTOOTRAFHOALLOW",
        "UTOOTRAFHOOPTSW",
        "UTRAFHOPERIOD",
        "UTRAFHOSTEP",
        "ENUTOOLOADINILEV"
    FROM
    huawei_nbi_gsm."GCELLHOIUO"

    """
)

GCELLHOPANT = ReplaceableObject(
    'huawei_cm_2g."GCELLHOPANT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "HPANTMODE"
    FROM
    huawei_nbi_gsm."GCELLHOPANT"

    """
)

GCELLHOPTP = ReplaceableObject(
    'huawei_cm_2g."GCELLHOPTP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "FHMODE"
    FROM
    huawei_nbi_gsm."GCELLHOPTP"

    """
)

GCELLHOTDDBA2 = ReplaceableObject(
    'huawei_cm_2g."GCELLHOTDDBA2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "ITEM",
        "ITEMVALID",
        "TDDBA2TAG"
    FROM
    huawei_nbi_gsm."GCELLHOTDDBA2"

    """
)

GCELLHOUTRANFDD = ReplaceableObject(
    'huawei_cm_2g."GCELLHOUTRANFDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BET3GHOEN",
        "CELLID",
        "HOECNOTH3G",
        "HOOPTSEL",
        "HOPRETH2G",
        "HORSCPTH3G"
    FROM
    huawei_nbi_gsm."GCELLHOUTRANFDD"

    """
)

GCELLHOUTRANTDD = ReplaceableObject(
    'huawei_cm_2g."GCELLHOUTRANTDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BET3GHOEN",
        "CELLID",
        "HOOPTSEL",
        "HOPRETH2G",
        "HORSCPTH3G"
    FROM
    huawei_nbi_gsm."GCELLHOUTRANTDD"

    """
)

GCELLHSRPLCUSRIDFMG = ReplaceableObject(
    'huawei_cm_2g."GCELLHSRPLCUSRIDFMG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "HSRPLCUSRIDNTFSW"
    FROM
    huawei_nbi_gsm."GCELLHSRPLCUSRIDFMG"

    """
)

GCELLIBCAII = ReplaceableObject(
    'huawei_cm_2g."GCELLIBCAII"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "IBCAIIALLOWED"
    FROM
    huawei_nbi_gsm."GCELLIBCAII"

    """
)

GCELLIDLEAD = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLEAD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACS",
        "CELLID",
        "CMETO",
        "PT"
    FROM
    huawei_nbi_gsm."GCELLIDLEAD"

    """
)

GCELLIDLEBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLEBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ATT",
        "BSAGBLKSRES",
        "BSPAMFRAMS",
        "CBA",
        "CBQ",
        "CELLID",
        "CRH",
        "CRO",
        "DISCARDCHREQCBQSW",
        "NCCPERMIT",
        "PI",
        "T3212",
        "TX"
    FROM
    huawei_nbi_gsm."GCELLIDLEBASIC"

    """
)

GCELLIDLEFDDBA1 = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLEFDDBA1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "FDDBA1TAG",
        "FDDDIVERSITY",
        "FDDDLUARFAN",
        "FDDSCRAMBLE",
        "ITEM",
        "ITEMVALID"
    FROM
    huawei_nbi_gsm."GCELLIDLEFDDBA1"

    """
)

GCELLIDLETDDBA1 = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLETDDBA1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "ITEM",
        "ITEMVALID",
        "TDDBA1TAG"
    FROM
    huawei_nbi_gsm."GCELLIDLETDDBA1"

    """
)

GCELLLCS = ReplaceableObject(
    'huawei_cm_2g."GCELLLCS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALTIDECI",
        "ALTITUDE",
        "ANTAANGLE",
        "CELLID",
        "INCLUDEANG",
        "INPUTMD",
        "LATIDECI",
        "LATIINT",
        "LONGIDECI",
        "LONGIINT",
        "NSLATI",
        "WELONGI"
    FROM
    huawei_nbi_gsm."GCELLLCS"

    """
)

GCELLMAGRP = ReplaceableObject(
    'huawei_cm_2g."GCELLMAGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "FREQ1",
        "HOPINDEX",
        "HOPMODE",
        "HSN",
        "TSC",
        "FREQ2",
        "FREQ3",
        "FREQ4",
        "FREQ5",
        "FREQ6",
        "FREQ7",
        "FREQ8",
        "FREQ9",
        "FREQ10"
    FROM
    huawei_nbi_gsm."GCELLMAGRP"

    """
)

GCELLMAIOPLAN = ReplaceableObject(
    'huawei_cm_2g."GCELLMAIOPLAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "HOPINDEX"
    FROM
    huawei_nbi_gsm."GCELLMAIOPLAN"

    """
)

GCELLMOCN = ReplaceableObject(
    'huawei_cm_2g."GCELLMOCN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "MOCNIISW",
        "MOCNINTERRATPOLICYSW"
    FROM
    huawei_nbi_gsm."GCELLMOCN"

    """
)

GCELLNC2PARA = ReplaceableObject(
    'huawei_cm_2g."GCELLNC2PARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALLOWEDMEASRPTMISSEDNUM",
        "CELLID",
        "CELLRXQUALWORSENRATIOTHRSH",
        "EGPRSBEPLIMIT8PSK",
        "EGPRSBEPLIMITGMSK",
        "FILTERWNDSIZE",
        "GPRSRXQUALLIMIT",
        "LOADRESELALLOW",
        "LOADRESELMAXRXLEV",
        "LOADRESELRXTHRSH",
        "LOADRESELSTARTTHRSH",
        "MINACCRXLEV",
        "MSRXQUALSTATTHRSH",
        "NORMALRESELALLOW",
        "PENALTYLASTTM",
        "PENALTYRXLEV",
        "RESELHYST",
        "RESELINTERVAL",
        "RESELWATCHPERIOD",
        "RESELWORSENLEVTHRSH",
        "TRAFFICRESELALLOW",
        "URGENTRESELALLOW"
    FROM
    huawei_nbi_gsm."GCELLNC2PARA"

    """
)

GCELLNCRESELECTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLNCRESELECTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "GPRSPENALTYTIME",
        "GPRSTEMPOFFSET",
        "RSLCTOFFER"
    FROM
    huawei_nbi_gsm."GCELLNCRESELECTPARA"

    """
)

GCELLNONSTANDARDBW = ReplaceableObject(
    'huawei_cm_2g."GCELLNONSTANDARDBW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "GUDEGRATEPWRCTRL"
    FROM
    huawei_nbi_gsm."GCELLNONSTANDARDBW"

    """
)

GCELLNWCTRLMSRPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLNWCTRLMSRPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "NONDRXPERIOD",
        "RPTPERIODI",
        "RPTPERIODT"
    FROM
    huawei_nbi_gsm."GCELLNWCTRLMSRPARA"

    """
)

GCELLOPTREV = ReplaceableObject(
    'huawei_cm_2g."GCELLOPTREV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "CELLOPTRSVPARA1",
        "CELLOPTRSVPARA3",
        "CELLOPTRSVPARA4"
    FROM
    huawei_nbi_gsm."GCELLOPTREV"

    """
)

GCELLOSPMAP = ReplaceableObject(
    'huawei_cm_2g."GCELLOSPMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "OPC"
    FROM
    huawei_nbi_gsm."GCELLOSPMAP"

    """
)

GCELLOTHBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLOTHBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "FREQFILTBASEIRATMEASCFGSW",
        "GIMSIMMSW",
        "GSPIDMMSW",
        "HOPOWERBOOST",
        "LTEFASTRETURNFRQSENDOPTSW",
        "RPTVOICE"
    FROM
    huawei_nbi_gsm."GCELLOTHBASIC"

    """
)

GCELLOTHEXT = ReplaceableObject(
    'huawei_cm_2g."GCELLOTHEXT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AUXTRXRSVSW",
        "BTSGRPFLEXABISLDRACTION",
        "CDRTTRYFBDTHRES",
        "CELLCOVERAGETYPE",
        "CELLID",
        "CELLOVERCVGRXLEVDLTH",
        "CELLOVERCVGTALTH",
        "CELLWEAKCVGRXLEVDLTH",
        "CELLWEAKCVGTALTH",
        "CSUPDATAABNMLCHKSW",
        "DATATRAFFSET",
        "DLFREQADJ",
        "DRFUVWSRSMMODE",
        "DRTAGCELLSEL",
        "DRXEN",
        "FERSTATTH1",
        "FERSTATTH2",
        "FERSTATTH3",
        "FERSTATTH4",
        "FERSTATTH5",
        "FERSTATTH6",
        "FERSTATTH7",
        "FRAMEOFFSET",
        "FREQADJ",
        "FREQADJVALUE",
        "HSCSDREADJUSTMENTSW",
        "HSCSDSCANPER",
        "HSCSDTRAFFSET",
        "IBCAINTFPUNISHTHR",
        "ICADPSCNIDENTOPTSW",
        "INTERFTHRES0",
        "INTERFTHRES1",
        "INTERFTHRES2",
        "INTERFTHRES3",
        "INTERFTHRES4",
        "INTERFTHRES5",
        "INTERPERIOD",
        "INTFBANDENHANCESW",
        "INTFFILTERPERIOD",
        "INTFREPROTPERIOD",
        "IURGINFOCTRL",
        "MAINBCCHPWRDTEN",
        "MTSPRITYPE",
        "PCHOCMPCON",
        "PODECTHRES",
        "POERRTHRES",
        "PREEMPTBBTHD",
        "PSULFREQADJ",
        "RELEASEBBTHD",
        "RESERVEDIDLECH",
        "RFMAXPWRDEC",
        "SDDROPSTATDLLEV",
        "SDDROPSTATDLQUAL",
        "SDDROPSTATULLEV",
        "SDDROPSTATULQUAL",
        "TCHDROPSTATDLFER",
        "TCHDROPSTATDLLEV",
        "TCHDROPSTATDLQUAL",
        "TCHDROPSTATULFER",
        "TCHDROPSTATULLEV",
        "TCHDROPSTATULQUAL",
        "TFRMSTARTTIME",
        "TRXPOOLALLOCTAFTH",
        "TRXPOOLPMTTAFTH",
        "TRXPOOLRELTAFTH",
        "VQILOWTHRD",
        "VSWRERRTHRES",
        "VSWRUNJUSTTHRES",
        "MAINBCCHPWDTACTCHEN",
        "MAINBCCHPWRDTETIME",
        "MAINBCCHPWRDTRANGE",
        "MAINBCCHPWRDTSTIME"
    FROM
    huawei_nbi_gsm."GCELLOTHEXT"

    """
)

GCELLOTHPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLOTHPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRULCMRSENDMODE",
        "CELLID",
        "DRFUDLPWRCORRECTMODE",
        "DRRUDLPWRDECTMODE",
        "FIRSTMROPTSW",
        "IMMOCCUPYPCHOPTSW",
        "MULTRXBRDSTABMONITUNNSW",
        "MULTRXBRDUNSTABMONITUNNSW",
        "PCHFORBIDRPTLOADSW",
        "PTCCHPOWEROPTSW",
        "RPTRLTSW",
        "SDCONGESTBTSFLOWCTRLSW",
        "SPEECHBADFRAMEOPTSW",
        "SPEECHDELAYOPTSW"
    FROM
    huawei_nbi_gsm."GCELLOTHPARA"

    """
)

GCELLPRACH = ReplaceableObject(
    'huawei_cm_2g."GCELLPRACH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACCCONTROLCLASS",
        "CELLID",
        "MAXRETRANS1",
        "MAXRETRANS2",
        "MAXRETRANS3",
        "MAXRETRANS4",
        "PL1",
        "PL2",
        "PL3",
        "PL4",
        "SVALUE",
        "TXINT"
    FROM
    huawei_nbi_gsm."GCELLPRACH"

    """
)

GCELLPRIEUTRANSYS = ReplaceableObject(
    'huawei_cm_2g."GCELLPRIEUTRANSYS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BESTEUTRANCELLNUM",
        "CELLID",
        "EUTRANFREQCNUM",
        "EUTRANPRI",
        "EUTRANQRXLEVMIN",
        "FASTRETURNFILTERSW",
        "FASTRETURNMEASSPT",
        "FDDFASTRETURNRSRPTH",
        "FDDLTEOFFSET",
        "GERANPRI",
        "HPRIO",
        "QPEUTRAN",
        "SI2QUATEROPTFORLTESW",
        "TDDFASTRETURNRSRPTH",
        "TDDLTEOFFSET",
        "THREUTRANHIGH",
        "THREUTRANLOW",
        "THREUTRANRPT",
        "THRGSMLOW",
        "THRPRISEARCH",
        "THRUTRANHIGH",
        "THRUTRANLOW",
        "TRESEL",
        "UTRANPRI",
        "UTRANQRXLEVMIN"
    FROM
    huawei_nbi_gsm."GCELLPRIEUTRANSYS"

    """
)

GCELLPRIVATEOPTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPRIVATEOPTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADVESTDLTBFRELDELAY",
        "BKGARP1DLRELDELAY",
        "BKGARP2DLRELDELAY",
        "BKGARP3DLRELDLAY",
        "CELLID",
        "CELLPSRESERVEPARA4",
        "DLASSRETRYTIMESMAX",
        "DLLIMITULPDALLOCSW",
        "DLRELDELAYACKOPT",
        "DLRELDELAYRLCUNACKMODE",
        "DLTBFESTDELAY",
        "DNTBFRELDELAY",
        "FIRSTBLKCV0INACTPERDPERMIT",
        "IMDLTBFRELDELAY",
        "POCRELDELAY",
        "POLLINGRETRYTIMESMAX",
        "PSDTX",
        "PSDTXPRDDUMMY",
        "PSUMENHANCESW",
        "QUICKSTARTDLASSRESNDOPTSW",
        "QUICKSTARTDLTBFRELOPTSW",
        "REASSIGNRESENDSW",
        "T3169",
        "T3191",
        "T3195",
        "THP1ARP1DLRELDELAY",
        "THP1ARP2DLRELDELAY",
        "THP1ARP3DLRELDELAY",
        "THP2ARP1DLRELDELAY",
        "THP2ARP2DLRELDELAY",
        "THP2ARP3DLRELDELAY",
        "THP3ARP1DLRELDELAY",
        "THP3ARP2DLRELDELAY",
        "THP3ARP3DLRELDELAY",
        "ULEXTERNACKOPT",
        "ULRELDELAYRLCUNACKMODE",
        "UPEXTTBFINACTDELAY",
        "UPTBFRELDELAY"
    FROM
    huawei_nbi_gsm."GCELLPRIVATEOPTPARA"

    """
)

GCELLPSABISPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPSABISPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISIPMAXTRANSDELAY",
        "ABISIPPROTECTDURA",
        "CELLID",
        "JITTERBUFFERAUTOADJUST",
        "NORMALCELLTRANSDELAY"
    FROM
    huawei_nbi_gsm."GCELLPSABISPARA"

    """
)

GCELLPSBASE = ReplaceableObject(
    'huawei_cm_2g."GCELLPSBASE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACCBURST",
        "ACCTECHREQSW",
        "BSCVMAX",
        "BSSPAGINGCOORDINATION",
        "CELLID",
        "CTRLACKTYPE",
        "DRXTIMERMAX",
        "EARLYTBFEST",
        "EGPRS11BITCHANREQ",
        "EXTUTBFNODATA",
        "INACTSCHPERIOD",
        "NCO",
        "NMO",
        "PANDEC",
        "PANINC",
        "PANMAX",
        "PRIACCTHR",
        "PSDTXLAOPTISWITCH",
        "RACOLOR",
        "SGSNR",
        "SPGCCCCHSUP",
        "T3168",
        "T3192",
        "T3192CONTENSOLUTSW",
        "UPDTXACKPERIOD"
    FROM
    huawei_nbi_gsm."GCELLPSBASE"

    """
)

GCELLPSCHM = ReplaceableObject(
    'huawei_cm_2g."GCELLPSCHM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISTSFREETM",
        "ACTIVETBFSWITCH",
        "ALLOCSINGLEPDCHFORSIGNALLING",
        "APPLYMULTIABISTS",
        "AUTOGPRSCHPRI",
        "BEARP1PRIMAXPDCHNUM",
        "BEARP1PRIWEIGHT",
        "BEARP2PRIMAXPDCHNUM",
        "BEARP2PRIWEIGHT",
        "BEARP3PRIMAXPDCHNUM",
        "BEARP3PRIWEIGHT",
        "BKGARP1PDCHWEIGHT",
        "BKGARP1PRIMAXPDCHNUM",
        "BKGARP1PRIWEIGHT",
        "BKGARP2PDCHWEIGHT",
        "BKGARP2PRIMAXPDCHNUM",
        "BKGARP2PRIWEIGHT",
        "BKGARP3PDCHWEIGHT",
        "BKGARP3PRIMAXPDCHNUM",
        "BKGARP3PRIWEIGHT",
        "CELLID",
        "CHIDLHIGHTHR",
        "CHIDLLOWTHR",
        "CSBUSYPDAPPINTERVAL",
        "DEFAULTDYNPDCHPRETRANNUM",
        "DUTYCYCLEBASEDPDCHMAG",
        "DWNDYNCHNTRANLEV",
        "DYNCHFREETM",
        "DYNCHNPREEMPTLEV",
        "DYNCHTRANRESLEV",
        "ENPDADMINOPT",
        "GPRSLOADOPT",
        "IMARP1PRIMAXPDCHNUM",
        "IMARP1PRIWEIGHT",
        "IMARP2PRIMAXPDCHNUM",
        "IMARP2PRIWEIGHT",
        "IMARP3PRIMAXPDCHNUM",
        "IMARP3PRIWEIGHT",
        "IMOPTTHRSH",
        "IMPDCHMULTIPLEXWEIGHT",
        "IOUPDCHSWTICH",
        "IUOCHNTRAN",
        "IUOCHNTRANPOLICY",
        "MAXMULCLSPDCHCVTENSW",
        "MAXPDCHRATE",
        "MSRDMCSLEV",
        "MSRDPDCHLEV",
        "PDCHDWNLEV",
        "PDCHPOWERPLENT",
        "PDCHPOWERPLENTTHRES",
        "PDCHREFORMING",
        "PDCHUPLEV",
        "POWTUNIT",
        "PRECONNECTSLAVEABIS",
        "PSDUALTHROPTSW",
        "PSRESPREEMPT",
        "PSRESPREEMPTED",
        "PSSERVICEBUSYTHRESHOLD",
        "RADIORESADAADJDLLOADTHD",
        "RADIORESADAADJSWITCH",
        "RADIORESADAADJULLOADTHD",
        "RAMBCAP",
        "RESERVEDDYNPDCHPRETRANNUM",
        "RTTIPDCHMULTIPLEXTHRESH",
        "THP1ARP1PDCHWEIGHT",
        "THP1ARP1PRIMAXPDCHNUM",
        "THP1ARP1PRIWEIGHT",
        "THP1ARP2PDCHWEIGHT",
        "THP1ARP2PRIMAXPDCHNUM",
        "THP1ARP2PRIWEIGHT",
        "THP1ARP3PDCHWEIGHT",
        "THP1ARP3PRIMAXPDCHNUM",
        "THP1ARP3PRIWEIGHT",
        "THP2ARP1PDCHWEIGHT",
        "THP2ARP1PRIMAXPDCHNUM",
        "THP2ARP1PRIWEIGHT",
        "THP2ARP2PDCHWEIGHT",
        "THP2ARP2PRIMAXPDCHNUM",
        "THP2ARP2PRIWEIGHT",
        "THP2ARP3PDCHWEIGHT",
        "THP2ARP3PRIMAXPDCHNUM",
        "THP2ARP3PRIWEIGHT",
        "THP3ARP1PDCHWEIGHT",
        "THP3ARP1PRIMAXPDCHNUM",
        "THP3ARP1PRIWEIGHT",
        "THP3ARP2PDCHWEIGHT",
        "THP3ARP2PRIMAXPDCHNUM",
        "THP3ARP2PRIWEIGHT",
        "THP3ARP3PDCHWEIGHT",
        "THP3ARP3PRIMAXPDCHNUM",
        "THP3ARP3PRIWEIGHT",
        "TWOTHLDCNVTONOTHERTRXSW",
        "UPDYNCHNTRANLEV",
        "DWNDYNCHNRETRANLEV",
        "UPDYNCHNRETRANLEV",
        "ACTIVETBFDWNDYNCHNTRANLEV",
        "ACTIVETBFUPDYNCHNTRANLEV"
    FROM
    huawei_nbi_gsm."GCELLPSCHM"

    """
)

GCELLPSCS = ReplaceableObject(
    'huawei_cm_2g."GCELLPSCS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "DLCSADJOPTSW",
        "DNDEFAULTCS",
        "DNFIXCS",
        "DNTHDCSDEGRADE1",
        "DNTHDCSDEGRADE2",
        "DNTHDCSDEGRADE3",
        "DNTHDCSUPGRADE1",
        "DNTHDCSUPGRADE2",
        "DNTHDCSUPGRADE3",
        "UPDEFAULTCS",
        "UPFIXCS",
        "UPTHDCSDEGRADE1",
        "UPTHDCSDEGRADE2",
        "UPTHDCSDEGRADE3",
        "UPTHDCSUPGRADE1",
        "UPTHDCSUPGRADE2",
        "UPTHDCSUPGRADE3"
    FROM
    huawei_nbi_gsm."GCELLPSCS"

    """
)

GCELLPSDIFFSERVICE = ReplaceableObject(
    'huawei_cm_2g."GCELLPSDIFFSERVICE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "EMAILARP1MAXPDCHNUM",
        "EMAILARP1WEIGHT",
        "EMAILARP2MAXPDCHNUM",
        "EMAILARP2WEIGHT",
        "EMAILARP3MAXPDCHNUM",
        "EMAILARP3WEIGHT",
        "EMAILDLTBFRELDELAY",
        "EMAILOPT",
        "EMAILPDCHMULTIPLEXWEIGHT",
        "IMARP1MAXPDCHNUM",
        "IMARP1WEIGHT",
        "IMARP2MAXPDCHNUM",
        "IMARP2WEIGHT",
        "IMARP3MAXPDCHNUM",
        "IMARP3WEIGHT",
        "IMDLTBFRELDELAY",
        "IMOPT",
        "IMPDCHMULTIPLEXWEIGHT",
        "P2PARP1MAXPDCHNUM",
        "P2PARP1WEIGHT",
        "P2PARP2MAXPDCHNUM",
        "P2PARP2WEIGHT",
        "P2PARP3MAXPDCHNUM",
        "P2PARP3WEIGHT",
        "P2PDLTBFRELDELAY",
        "P2POPT",
        "P2PPDCHMULTIPLEXWEIGHT",
        "SERVTYPERTUPDATESW",
        "STREAMINGARP1MAXPDCHNUM",
        "STREAMINGARP1WEIGHT",
        "STREAMINGARP2MAXPDCHNUM",
        "STREAMINGARP2WEIGHT",
        "STREAMINGARP3MAXPDCHNUM",
        "STREAMINGARP3WEIGHT",
        "STREAMINGDLTBFRELDELAY",
        "STREAMINGOPT",
        "STREAMPDCHMULTIPLEXWEIGHT",
        "WEBARP1MAXPDCHNUM",
        "WEBARP1WEIGHT",
        "WEBARP2MAXPDCHNUM",
        "WEBARP2WEIGHT",
        "WEBARP3MAXPDCHNUM",
        "WEBARP3WEIGHT",
        "WEBDLTBFRELDELAY",
        "WEBOPT",
        "WEBPDCHMULTIPLEXWEIGHT"
    FROM
    huawei_nbi_gsm."GCELLPSDIFFSERVICE"

    """
)

GCELLPSI1 = ReplaceableObject(
    'huawei_cm_2g."GCELLPSI1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "MEASORDER",
        "PSI1RPT",
        "PSISTATUSIND"
    FROM
    huawei_nbi_gsm."GCELLPSI1"

    """
)

GCELLPSOTHERPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPSOTHERPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISIPDUMMYOPTSUP",
        "ACCSTASERVICETYPE",
        "CELLID",
        "DLGPRSINFOWAITSENDTIMELEN",
        "DLGPRSTBFEXPANDOP",
        "DLMINGUARANTEERATE",
        "DLPACKSENDPERIOD",
        "DUMMYPDULIFETIME",
        "EGPRSPRIWEIGHT",
        "ENGSMPSDLMACFLOWCTRL",
        "ENSUREPDCHRESORNOT",
        "EXTCELLTHRENH",
        "G3GNCELLFILTERMODE",
        "GBRQOS",
        "GMSKULSCHEDULEOPTSW",
        "GPRSCHOOSECSPOLICY",
        "GPRSPDCHSYNMODE",
        "GPSRRECORDFLTSW",
        "GSMTOTDALLOWED",
        "IMMASSDLSHIFT",
        "LINKADJACKCHECKSW",
        "LINKADJRESENDINTERVAL",
        "LLCDLRATESTATOPTSW",
        "LLCPDUREORDER",
        "LONGHOPFREQNUMLOWLMTSW",
        "MACSCHEDULETYPE",
        "MINTIMEDIFF",
        "MOCNWAITSGSNRSPTIMERLEN",
        "N3103STATMODE",
        "OCCUPYSTREAMINGSWITCH",
        "PACKASSDLSHIFT",
        "PDCHASYNNOTIFYBTSSW",
        "PFCSWITCH",
        "PKTIMMASSHOPCHANPLY",
        "POCDELAY",
        "POCGBRMAX",
        "POCGBRMIN",
        "POCSUP",
        "PSDIFSERVICESUP",
        "QOSOPT",
        "RATEFILTERTIMEWIN",
        "RDMFILLBYTESSUP",
        "REQREFFRAMENOFIXEDSW",
        "SINGLEBLKASSSTARTTIMEDLYSW",
        "SUSPENDDLTBFRELSTATSW",
        "USERPLANEDLFCPDCHBW",
        "USERPLANEDLFCPERIOD",
        "USERPLANEDLFCSTEP"
    FROM
    huawei_nbi_gsm."GCELLPSOTHERPARA"

    """
)

GCELLPSPWPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPSPWPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALPHA",
        "CELLID",
        "DLPCINITPR",
        "DLPCSTARTTHR",
        "DUMMYPRGRAN",
        "EGPRSDLMRFLTGENE",
        "EGPRSINITATTTARGETLEVEL",
        "EGPRSSIGINITATTOFFSET",
        "EGPRSSIGPOWEROFFSET",
        "EGPRSULPCTARGETTHR",
        "GAMMA",
        "GPRSDLMRFLTGENE",
        "GPRSDLPCRELADJGENE",
        "GPRSDLPCRELTHR",
        "GPRSDLPCSTARTTHR",
        "GPRSINITATTTARGETLEVEL",
        "GPRSSIGINITATTOFFSET",
        "GPRSSIGPOWEROFFSET",
        "MAXPCSTEP",
        "MCSSTABTHR",
        "MCSSTATTHR",
        "NAVGI",
        "PB",
        "PCMEASCHAN",
        "PSPCPOLICY",
        "PSPCPRES",
        "SUPEGPRSDLPCMROPT",
        "SUPEGPRSULPC",
        "SUPGPRSDLPC",
        "SUPPSDLPC",
        "TAVGT",
        "TAVGW",
        "TGTCIROFFSET",
        "TGTCIRPOS",
        "USFDUMMYPCFACTOR"
    FROM
    huawei_nbi_gsm."GCELLPSPWPARA"

    """
)

GCELLPSSMALLPKTRESBAL = ReplaceableObject(
    'huawei_cm_2g."GCELLPSSMALLPKTRESBAL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "PSSMALLPKTRESBALSWITCH"
    FROM
    huawei_nbi_gsm."GCELLPSSMALLPKTRESBAL"

    """
)

GCELLPWR2 = ReplaceableObject(
    'huawei_cm_2g."GCELLPWR2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRBTSPWRNUM",
        "AMRDLLEVFTLEN",
        "AMRDLPREDLEND",
        "AMRDLQHTHRED",
        "AMRDLQLTHRED",
        "AMRDLQUAFTLEN",
        "AMRDLQUALBADTRIG",
        "AMRDLQUALBADUPLEV",
        "AMRDLSSHTHRED",
        "AMRDLSSLTHRED",
        "AMRMAXADJPCVAL",
        "AMRMAXSTEP0",
        "AMRMAXSTEP1",
        "AMRMAXSTEP2",
        "AMRMAXVALADJRX",
        "AMRMRCOMPREG",
        "AMRPCADJPERIOD",
        "AMRQUALSTEP",
        "AMRULLEVFTLEN",
        "AMRULPREDLEND",
        "AMRULQHTHRED",
        "AMRULQLOWTHRED",
        "AMRULQUAFTLEN",
        "AMRULQUALBADTRIG",
        "AMRULQUALBADUPLEV",
        "AMRULSSHTHRED",
        "AMRULSSLTHRED",
        "BTSPWRNUM",
        "CELLID",
        "DLLEVFILTLEN",
        "DLPREDLEND",
        "DLQUAFILTLEN",
        "DLQUALBADTRIG",
        "DLQUALBADUPLEV",
        "MAXADJPCVAL",
        "MAXSTEP0",
        "MAXSTEP1",
        "MAXSTEP2",
        "MAXVALADJRX",
        "MRCOMPREG",
        "QUALSTEP",
        "SAICTHREDAPDTVALUE",
        "ULLEVFILTLEN",
        "ULPREDLEND",
        "ULQUAFILTLEN",
        "ULQUALBADTRIG",
        "ULQUALBADUPLEV"
    FROM
    huawei_nbi_gsm."GCELLPWR2"

    """
)

GCELLPWR3 = ReplaceableObject(
    'huawei_cm_2g."GCELLPWR3"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRCALLPCALLOWED",
        "CELLID",
        "CIRUPDATESWITCH",
        "DLADJPRD",
        "DLAFSREXQUALHIGHTHRED",
        "DLAFSREXQUALLOWTHRED",
        "DLAHSREXQUALHIGHTHRED",
        "DLAHSREXQUALLOWTHRED",
        "DLFILTADJFACTOR",
        "DLFSREXQUALHIGHTHRED",
        "DLFSREXQUALLOWTHRED",
        "DLHSREXQUALHIGHTHRED",
        "DLHSREXQUALLOWTHRED",
        "DLMAXDOWNOPTISW",
        "DLMAXDOWNSTEP",
        "DLMAXUPSTEP",
        "DLPCSTEPOPTSWITCH",
        "DLREXLEVADJFCTR",
        "DLREXLEVEXPFLTLEN",
        "DLREXLEVHIGHTHRED",
        "DLREXLEVLOWTHRED",
        "DLREXLEVSLDWINDOW",
        "DLREXQUALADJFCTR",
        "DLREXQUALEXPFLTLEN",
        "DLREXQUALSLDWINDOW",
        "DLRXLEVPROTECTFACTOR",
        "DLRXQUALPROTECTFACTOR",
        "FINESTEPPCALLOWED",
        "MAXBTSPWRNUM",
        "MRMISSNUM",
        "NONAMRCALLPCALLOWED",
        "OLDLREXLEVTHREDOFF",
        "OLDLREXQUALTHREDOFF",
        "OLDLRXLEVPROTECTOFF",
        "OLDLRXQUALPROTECTOFF",
        "OLULREXLEVTHREDOFF",
        "OLULREXQUALTHREDOFF",
        "OLULRXLEVPROTECTOFF",
        "OLULRXQUALPROTECTOFF",
        "PCSTEPOPT",
        "PWRCTRLOPTIMIZEDEN",
        "PWRFINECTLOPTIMIZESWITCH",
        "SAICTHREDAPDTVALUE",
        "SDMRCUTNUM",
        "TCHMRCUTNUM",
        "ULADJPRD",
        "ULAFSREXQUALHIGHTHRED",
        "ULAFSREXQUALLOWTHRED",
        "ULAHSREXQUALHIGHTHRED",
        "ULAHSREXQUALLOWTHRED",
        "ULFILTADJFACTOR",
        "ULFSREXQUALHIGHTHRED",
        "ULFSREXQUALLOWTHRED",
        "ULHSREXQUALHIGHTHRED",
        "ULHSREXQUALLOWTHRED",
        "ULMAXDOWNSTEP",
        "ULMAXUPSTEP",
        "ULREXLEVADJFCTR",
        "ULREXLEVEXPFLTLEN",
        "ULREXLEVHIGHTHRED",
        "ULREXLEVLOWTHRED",
        "ULREXLEVSLDWINDOW",
        "ULREXQUALADJFCTR",
        "ULREXQUALEXPFLTLEN",
        "ULREXQUALSLDWINDOW",
        "ULRXLEVPROTECTFACTOR",
        "ULRXQUALPROTECTFACTOR"
    FROM
    huawei_nbi_gsm."GCELLPWR3"

    """
)

GCELLPWRBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLPWRBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRSADLUPGRADE",
        "BBFHPOWECTRLSWITCH",
        "CELLID",
        "COMBINERLOSS",
        "DLQHIGHTHRED",
        "DLQLOWTHRED",
        "DLSSHIGHTHRED",
        "DLSSLOWTHRED",
        "DOUBLEANTENNAGAIN",
        "EXPDLRXLEV",
        "EXPULRXLEV",
        "MSPOWERLEVELSWITCH",
        "PATHLOSS",
        "PCADJPERIOD",
        "POWERCTRLSTEPSWITCH",
        "PWRBCDALLOWD",
        "PWRBCDASSOFFSET",
        "PWRBCDHOOFFSET",
        "PWRBCDOPTIMIZESWITCH",
        "PWRBCDPROCOPTSW",
        "PWRCTLSAICOFFSETSWITCH",
        "PWRCTRLSW",
        "SAICALLOWED",
        "ULQHIGHTHRED",
        "ULQLOWTHRED",
        "ULSSHIGHTHRED",
        "ULSSLOWTHRED"
    FROM
    huawei_nbi_gsm."GCELLPWRBASIC"

    """
)

GCELLRESELECTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLRESELECTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "C31HYST",
        "C32QUAL",
        "CELLID",
        "GPRSCELLRESELECTHYESTERESIS",
        "RANDACCESSRETRY",
        "RARESELECTHYST",
        "TRESEL"
    FROM
    huawei_nbi_gsm."GCELLRESELECTPARA"

    """
)

GCELLRESELECTUTRANTDD = ReplaceableObject(
    'huawei_cm_2g."GCELLRESELECTUTRANTDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "PSBESTTDDCELLNUM",
        "PSTDDCELLRPTOFF",
        "PSTDDCELLRPTTHD",
        "TDDNCELLLOADTHD",
        "TDDRESELTIMETHD"
    FROM
    huawei_nbi_gsm."GCELLRESELECTUTRANTDD"

    """
)

GCELLRESELUTRANFDD = ReplaceableObject(
    'huawei_cm_2g."GCELLRESELUTRANFDD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "FDDRESELTIMETHD",
        "GSMTOFDDFORCENC2",
        "PSBESTFDDCELLNUM",
        "PSFDDCELLRPTOFF",
        "PSFDDCELLRPTTHD",
        "PSFDDRPTTHR2ECNO",
        "PSFDDRPTTHR2RSCP",
        "SENDPMOWITHQPSW"
    FROM
    huawei_nbi_gsm."GCELLRESELUTRANFDD"

    """
)

GCELLRSVPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLRSVPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "GCELLCSDPARA1",
        "GCELLCSDPARA2",
        "GCELLCSDPARA3",
        "GCELLCSDPARA4",
        "GCELLCSDPARA5",
        "GCELLCSDPARA6",
        "GCELLCSDPARA7",
        "GCELLCSSWRSV0",
        "GCELLCSSWRSV1",
        "GCELLPSDPARA1",
        "GCELLPSDPARA11",
        "GCELLPSDPARA2",
        "GCELLPSSWRSV0",
        "GCELLPSSWRSV1"
    FROM
    huawei_nbi_gsm."GCELLRSVPARA"

    """
)

GCELLSBC = ReplaceableObject(
    'huawei_cm_2g."GCELLSBC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BROADCASTCONTENT",
        "BROADCASTINTERVAL",
        "CELLID",
        "CHANID",
        "GS",
        "SCHEME",
        "SUPPORTCELLBROADCAST"
    FROM
    huawei_nbi_gsm."GCELLSBC"

    """
)

GCELLSERVPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLSERVPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLBARACCESS2",
        "CELLID",
        "EXCACC",
        "GPRSHCSTHR",
        "MSTXPWRMAX",
        "MULTIBANDREP",
        "PRIORCLASS",
        "RXLEVACCMIN"
    FROM
    huawei_nbi_gsm."GCELLSERVPARA"

    """
)

GCELLSOFT = ReplaceableObject(
    'huawei_cm_2g."GCELLSOFT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISFLTSTOPWAITRELINDSW",
        "ACTL2REEST",
        "ADAICADFLAG",
        "ADAICFLAG",
        "ADAPTASSIGNMENTFLOW",
        "AIDDELAYPROTECTTIME",
        "AOIPINTRAHOFAMRSETOPTSW",
        "ASSBETTERCELLCONGOPTSTSW",
        "BADELIVERYCTRL",
        "BADQUALDISCTHRES",
        "BANDINDICATOR1900",
        "BANDINDICATOR810",
        "BANDINDICATOR850",
        "BANDINDICATOR900",
        "BTSSAICPCADJSWITCH",
        "CALLDISCSTATOPTALLOWED",
        "CELLID",
        "CELLPAGINGOVERLOADCOUNTER",
        "CHANFAULTALMSWITCH",
        "CHNALLOCSTALOGSW",
        "CSFBIDENTIFYMOSW",
        "CSFBIDENTIFYMTSW",
        "CSFBIMMASSENSW",
        "CSFBPAGRSPBCSWITCH",
        "CSFBVOQULENSURSW",
        "CSIPPACKETCHECKSW",
        "CSPAGINGCTRL",
        "DETECTFRAMEPERIOD",
        "DIRMAGANSITEFLAG",
        "DLDTXPOLICY",
        "DLDTXUPDATESWITCH",
        "DROPCTRLABISCONNFAIL",
        "DROPCTRLAFTERCONN",
        "DROPCTRLCONNFAILHOACCFAIL",
        "DROPCTRLCONNFAILOM",
        "DROPCTRLCONNFAILOTHER",
        "DROPCTRLCONNFAILRLFAIL",
        "DROPCTRLCONNFAILRRNOTAVL",
        "DROPCTRLEQUIPFAIL",
        "DROPCTRLERRINDDMRSP",
        "DROPCTRLERRINDSEQERR",
        "DROPCTRLERRINDT200",
        "DROPCTRLFORCHOFAIL",
        "DROPCTRLINBSCHO",
        "DROPCTRLINTRABSCOUTHO",
        "DROPCTRLINTRACELLHO",
        "DROPCTRLNOMR",
        "DROPCTRLOUTBSCHOT8",
        "DROPCTRLRELIND",
        "DROPCTRLRESCHK",
        "DUMMYBITRANDSWITCH",
        "DXXMUTEDETECTPERIOD",
        "DXXMUTEDETECTSWITCH",
        "ENTSWITCH",
        "EXCEPFRAMETHRES",
        "FERRPTEN",
        "FLEXTSCSWITCH",
        "FORCEDCELLEFRSWITCH",
        "FORCEMSACCESS",
        "FREQSCANRLSTTYPE",
        "G900FREQCOMPOPTSW",
        "ICTYP",
        "IMMDEASACCHSW",
        "INTERBANDMEASURETYPE",
        "INTERBANDSTATALGO",
        "IRATSHUTDOWNSWITCH",
        "L2REBSUCSIGPROCSW",
        "MACODINGMOD",
        "MSCAPABLESTATSWITCH",
        "MUTECHECKCLASS1PERIOD",
        "MUTECHECKCLASS2SWITCH",
        "MUTECHECKPEIROD",
        "MUTEFORBITCALLTMINTVAL",
        "MUTERELCALLEN",
        "NOISEDETPRD",
        "NOISEDETSW",
        "NOISEDETTHD",
        "NOISEFUZZYSW",
        "NOISEPRELEVEL",
        "OUTSERVICEALM",
        "PAGINGAVGCAPACITYINPERIOD",
        "PAGINGLIFETIME",
        "PAGINGMAXCAPACITYINPERIOD",
        "PDCHPWRSAVEN",
        "PMI",
        "PMNUM",
        "PMOAFLAG",
        "PWRLOCATION",
        "QTRUCHANMANGSWITCH",
        "QUERYCMAFTERINBSCHO",
        "RACHFLTSWITCH",
        "RPTDLVQIALLOWED",
        "RSPCBITTRACESWITCH",
        "SDCONGSTATOPT",
        "SDFASTHOSWITCH",
        "SENDCBITTRACESWITCH",
        "SENDCMAFTERINBSCHO",
        "SI6RANDOMBIT",
        "STIRCALLOWED",
        "STOPSI5SWITCH",
        "SUPPORTCSFB",
        "TCH2SDPREEN",
        "TCHTIMEHOPERIOD",
        "TCHTIMEHOSWITCH",
        "TCMUTEDETECTFLAG",
        "TESTUSERTRACEFUN",
        "TMRBADQUALDISCSTAT",
        "TSCPLANEN",
        "U2GSRCMEASSW",
        "UMCROSSTALKOPTALLOWED",
        "UTRANCMDELAYFORCSFBSW",
        "CHANFAULTALMPDCHTH",
        "CHANFAULTALMTCHTH",
        "CHANPDOUTTIME",
        "LOWLEVSUBRESPREEMPTFLG",
        "SUBRESPREEMPTFLG"
    FROM
    huawei_nbi_gsm."GCELLSOFT"

    """
)

GCELLSON = ReplaceableObject(
    'huawei_cm_2g."GCELLSON"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "PAGINGOVLDCTRLSTTHLD",
        "TCHCONGCTRLSTTHLD"
    FROM
    huawei_nbi_gsm."GCELLSON"

    """
)

GCELLSRVCC = ReplaceableObject(
    'huawei_cm_2g."GCELLSRVCC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "SRVCCBUSYTHRESOFFSET",
        "SRVCCPMTQUEUESW",
        "SRVCCRAPIDSELMEASOPTSW",
        "SRVCCRAPIDSELSW",
        "SRVCCSTATINTERRANHO",
        "SRVCCVAMOSCFGPOLICY"
    FROM
    huawei_nbi_gsm."GCELLSRVCC"

    """
)

GCELLSTANDARDOPTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLSTANDARDOPTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "N3101",
        "N3103",
        "N3105"
    FROM
    huawei_nbi_gsm."GCELLSTANDARDOPTPARA"

    """
)

GCELLTA = ReplaceableObject(
    'huawei_cm_2g."GCELLTA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "ESTINDTHD",
        "HIGHPRECISIONTA",
        "PSTATHD",
        "RACHTATHD",
        "SDCCHTATHD",
        "SDCCHTATHDOFFSET",
        "TCHTAFILTERLEN",
        "TCHTATHD"
    FROM
    huawei_nbi_gsm."GCELLTA"

    """
)

GCELLTEMPLATERSC = ReplaceableObject(
    'huawei_cm_2g."GCELLTEMPLATERSC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TEMPLATENAME"
    FROM
    huawei_nbi_gsm."GCELLTEMPLATERSC"

    """
)

GCELLTMR = ReplaceableObject(
    'huawei_cm_2g."GCELLTMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ASSTIMER",
        "CELLID",
        "CIPHERCOMPLETETMR",
        "DELAYSENDRFCHREL",
        "DIRECTHOWAIT3GNCELLTIMER",
        "ESTABINDTIMER",
        "GPRSRESUMEACKTMR",
        "IMMASSAINTERFTIMER",
        "IMMREJWAITINDTIMER",
        "INBSCHOTIMER",
        "INTRABSCCODECHOCMDTIMER",
        "INTRABSCHOTIMER",
        "INTRACELLHOTIMER",
        "MSIPFAILINDDELAY",
        "NORMALRELWAITFORRFCHRELACK",
        "OUTBSCHOCLEARTIMER",
        "OUTBSCHOCMDTIMER",
        "RLMODEMODTIMER",
        "SAIP3ESTABCONFERTMRMSIP",
        "TIQUEUINGTIMER",
        "TQHO",
        "ULDATAFWDTMR",
        "UMMODEMODITIMER",
        "WAITCRDLCBTSLPCNF",
        "WAITFORCHANACTACKMSG",
        "WAITFORRELIND",
        "WAITFORRELINDAMRFR",
        "WAITFORRELINDAMRHR",
        "WAITLOCALSWITCHFORHO",
        "WAITRESVCHANREFRESHTIMER",
        "WTSDFASTHOTRIGTMR"
    FROM
    huawei_nbi_gsm."GCELLTMR"

    """
)

GCELLTRANPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLTRANPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "JITTBUFFETHD",
        "JITTBUFSEQFETHD",
        "JITTBUFWNDDECPERIOD",
        "JITTBUFWNDMINPERIOD",
        "JITTBUFWNDSIZE"
    FROM
    huawei_nbi_gsm."GCELLTRANPARA"

    """
)

GCELLUNDPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLUNDPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "GUNBADQUALCHNUM",
        "GUNBADQUALCLRTHRD",
        "GUNBADQUALDETCTTHRD",
        "GUNBADQUALTHRD",
        "GUNBTSTATBASE",
        "GUNCHBADQUALSTATBASE",
        "GUNCHDROPBASE",
        "GUNCHDROPCLRTHRD",
        "GUNCHDROPDECTTHRD",
        "GUNFAULTDECTSW",
        "GUNRESETSW",
        "GUNRPDROPWNSW",
        "GUNRPDWBADQUALWNSW",
        "GUNRPFAULTINFO",
        "GUNRPUPBADQUALWNSW"
    FROM
    huawei_nbi_gsm."GCELLUNDPARA"

    """
)

GCELLVAMOS = ReplaceableObject(
    'huawei_cm_2g."GCELLVAMOS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "TSCUNIFYSW",
        "VAMOSSWITCH",
        "MULTALLOWBEFORECONN",
        "MUTESAICIDESWITCH",
        "MUTESAICSWITCH",
        "OPTVAMOSCHNMULALG",
        "SAICALPHAJUMPPRD",
        "SAICALPHAJUMPVALUE",
        "SAICPROMSIDESWITCH",
        "SAICPROMSSWITCH",
        "SPEMSIDEATCBTHD",
        "SPEMSIDEDLRXQUALTHD",
        "SPEMSIDELASTTIMES",
        "SPEMSIDELOAD",
        "SPEMSIDEMAXCALLS",
        "SPEMSIDESTATTIMES",
        "SPEMSIDEULRXQUALTHD",
        "UNKOWNSAICMULTSWITCH",
        "VAMOSASSDLRXLEVTHDOFFSET",
        "VAMOSASSLOADOFT",
        "VAMOSASSMULTATCBOFFSET",
        "VAMOSASSSWITCH",
        "VAMOSASSULQUALTHDOFFSET",
        "VAMOSDEPOLRXQUALOFT",
        "VAMOSINTRAHODLQUALTHD",
        "VAMOSINTRAHODLRXLEVTHD",
        "VAMOSINTRAHONONESAICATCBTHD",
        "VAMOSINTRAHOSAICATCBTHD",
        "VAMOSINTRAHOSWITCH",
        "VAMOSINTRAHOULQUALTHD",
        "VAMOSINTRAHOVAMOS1ATCBTHD",
        "VAMOSINTRAHOVAMOS2ATCBTHD",
        "VAMOSIUOINNERATCBTHD",
        "VAMOSIUOINNERLOADTHD",
        "VAMOSLOADREUSELOADTHD",
        "VAMOSLOADREUSESWITCH",
        "VAMOSMAINTSC",
        "VAMOSMULTLOADTHD",
        "VAMOSNONESAICALLOW",
        "VAMOSOLDCALLLASTTIMES",
        "VAMOSOLDCALLSTATTIMES",
        "VAMOSOLRXLEVOFT",
        "VAMOSOLRXQUALOFT",
        "VAMOSPATHLOSSMAXDIFFVALUE",
        "VAMOSQUALREUSEDOWNLINKQUALTHD",
        "VAMOSQUALREUSELASTTIMES",
        "VAMOSQUALREUSESTATTIMES",
        "VAMOSQUALREUSESWITCH",
        "VAMOSQUALREUSEUPLINKQUALTHD",
        "VAMOSQUALUNDOPNTSWITCH",
        "VAMOSSUBTSC"
    FROM
    huawei_nbi_gsm."GCELLVAMOS"

    """
)

GCELLVAMOSPWR = ReplaceableObject(
    'huawei_cm_2g."GCELLVAMOSPWR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALPHAQPSKADJSCOPE",
        "ALPHAQPSKAMRFRRXQUALTHD",
        "ALPHAQPSKAMRHRRXQUALTHD",
        "ALPHAQPSKCTRLSWITCH",
        "ALPHAQPSKFRRXQUALTHD",
        "ALPHAQPSKHRRXQUALTHD",
        "ALPHAQPSKRXLVLADJFAC",
        "ALPHAQPSKRXLVLPROFAC",
        "ALPHAQPSKRXLVLTHD",
        "ALPHAQPSKRXQUALADJFAC",
        "ALPHAQPSKRXQUALPROFAC",
        "CELLID",
        "SICAMRFRRXQUALTHD",
        "SICAMRHRRXQUALTHD",
        "SICDIFFHIGHTHD",
        "SICFRRXQUALTHD",
        "SICHRRXQUALTHD",
        "SICPWRCTRLSWITCH",
        "SICRXLVLADJFAC",
        "SICRXLVLPROFAC",
        "SICRXLVLTHD",
        "SICRXQUALADJFAC",
        "SICRXQUALPROFAC",
        "VAMOSINITPCDLSIGTHR",
        "VAMOSINITPCULSIGTHR"
    FROM
    huawei_nbi_gsm."GCELLVAMOSPWR"

    """
)

GCELLWLAN = ReplaceableObject(
    'huawei_cm_2g."GCELLWLAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "LOADTHRSTPWLAN",
        "LOADTHRTOWLAN",
        "STPWIFITMR",
        "WIFITMR",
        "WLANACCONN",
        "WLANCTRL"
    FROM
    huawei_nbi_gsm."GCELLWLAN"

    """
)

GCNCFGALMTHD = ReplaceableObject(
    'huawei_cm_2g."GCNCFGALMTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSNRIDIFFRATIOTHD",
        "CSTMSIREALLOCMINNUM",
        "PSNRIDIFFRATIOTHD",
        "PSPTMSIREALLOCMINNUM"
    FROM
    huawei_nbi_gsm."GCNCFGALMTHD"

    """
)

GCNNODE = ReplaceableObject(
    'huawei_cm_2g."GCNNODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ATRANSMODE",
        "BSSLSMSCCOOP",
        "CNID",
        "CNNODEIDX",
        "CODECRPTFLG",
        "DFDPC",
        "DPCGIDX",
        "DPX",
        "FORBIDNO7FLASHDISC",
        "MSCCAP",
        "MSCSTATUE",
        "OPNAME",
        "RTCPBWRATIO",
        "RTCPSWITCH",
        "UNITED_FC_SWITCH",
        "SAGSMRMSC"
    FROM
    huawei_nbi_gsm."GCNNODE"

    """
)

GCNOPERATOR = ReplaceableObject(
    'huawei_cm_2g."GCNOPERATOR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HOBTWNOTHOPALLOW",
        "LOADBALANCEALG",
        "MCC",
        "MNC",
        "MSCNRILEN",
        "MSCNULLNRI",
        "MSCPOOLALLOW",
        "OPERATORTYPE",
        "OPINDEX",
        "OPNAME",
        "SGSNNRILEN",
        "SGSNNULLNRI",
        "SGSNPOOLALLOW",
        "SPPRTCB",
        "TIIMSIPAGING",
        "TIWAITMSCMSG"
    FROM
    huawei_nbi_gsm."GCNOPERATOR"

    """
)

GCNOPERATORREV = ReplaceableObject(
    'huawei_cm_2g."GCNOPERATORREV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "OPERRSVPARA1",
        "OPERRSVPARA2",
        "OPERRSVPARA3",
        "OPERRSVPARA4",
        "OPERRSVPARA5",
        "OPINDEX"
    FROM
    huawei_nbi_gsm."GCNOPERATORREV"

    """
)

GCSCHRCTRL = ReplaceableObject(
    'huawei_cm_2g."GCSCHRCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSADDTINFO",
        "CSALGORITHMINFO",
        "CSBQTHR",
        "CSCLTERMABNORM",
        "CSHOINFO",
        "CSMOCNCHRINFO",
        "CSMRBFCLR",
        "CSMRBFHO",
        "CSOUTMODE",
        "CSOUTRANGE",
        "CSRCDSW",
        "CSSIGINFO",
        "CSTRAFTYPE",
        "U2GMROSW",
        "CSCHRMR",
        "CSVOICEINFO"
    FROM
    huawei_nbi_gsm."GCSCHRCTRL"

    """
)

GCSCHRSCOPE = ReplaceableObject(
    'huawei_cm_2g."GCSCHRSCOPE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "CHRCOLLECTSWITCH"
    FROM
    huawei_nbi_gsm."GCSCHRSCOPE"

    """
)

GCSFILE = ReplaceableObject(
    'huawei_cm_2g."GCSFILE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CMEMODE"
    FROM
    huawei_nbi_gsm."GCSFILE"

    """
)

GDSSPARA = ReplaceableObject(
    'huawei_cm_2g."GDSSPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSID",
        "DSSBAKDURTM",
        "DSSBAKIDLECHTH",
        "DSSBAKNORMPCTM",
        "DSSBAKSTATTM",
        "DSSBAKURGPCTM",
        "DSSENABLE",
        "DSSHANDSHAKE",
        "DSSSHFBTM",
        "DSSSHRIDLECHTH",
        "DSSSHSTATTM",
        "DSSWAITPSTM"
    FROM
    huawei_nbi_gsm."GDSSPARA"

    """
)

GEXT2GCELL = ReplaceableObject(
    'huawei_cm_2g."GEXT2GCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BCC",
        "BCCH",
        "BSCIDX",
        "CI",
        "CMEPRIOR",
        "COMSC",
        "EXT2GCELLID",
        "EXT2GCELLNAME",
        "GCNOPGRPINDEX",
        "HOOFFSET",
        "HOPUNISHVALUE",
        "HOTHRES",
        "IBCAIIINTERBSCHOINFOSW",
        "ISEDGESUPPORT",
        "ISGPRSSUPPORT",
        "ISNC2SUPPORT",
        "LAC",
        "LAYER",
        "LOADACCTHRES",
        "LOADHOENEXT2G",
        "MCC",
        "MNC",
        "MSRXMIN",
        "NCC",
        "OPNAME",
        "RA",
        "SDPUNTIME",
        "SDPUNVAL",
        "TIMEPUNISH"
    FROM
    huawei_nbi_gsm."GEXT2GCELL"

    """
)

GEXT3GCELL = ReplaceableObject(
    'huawei_cm_2g."GEXT3GCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLLAYER",
        "CI",
        "DF",
        "DIVERSITY",
        "ECNOTHRES",
        "EXT3GCELLID",
        "EXT3GCELLNAME",
        "FDDECQUALTHRSH",
        "FDDRSCPQUALTHRSH",
        "GCNOPGRPINDEX",
        "LAC",
        "LOADACCTHRES",
        "LOADHOENEXT3G",
        "MCC",
        "MINECNOTHRES",
        "MINRSCPTHRES",
        "MNC",
        "OPNAME",
        "RA",
        "RNCID",
        "RNCINDEX",
        "RSCPTHRES",
        "SCRAMBLE",
        "UTRANCELLTYPE"
    FROM
    huawei_nbi_gsm."GEXT3GCELL"

    """
)

GEXTLTECELL = ReplaceableObject(
    'huawei_cm_2g."GEXTLTECELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CI",
        "ENODEBTYPE",
        "EUTRANTYPE",
        "EXTLTECELLID",
        "EXTLTECELLNAME",
        "FREQ",
        "GCNOPGRPINDEX",
        "MCC",
        "MNC",
        "OPNAME",
        "PCID",
        "TAC"
    FROM
    huawei_nbi_gsm."GEXTLTECELL"

    """
)

GFORCESWITCH = ReplaceableObject(
    'huawei_cm_2g."GFORCESWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EVENTCSCHRSW",
        "EVENTMRSW",
        "EVENTPSCHRSW"
    FROM
    huawei_nbi_gsm."GFORCESWITCH"

    """
)

GHOSTSTATUS = ReplaceableObject(
    'huawei_cm_2g."GHOSTSTATUS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HOSTSTATUS",
        "HOSTTYPE"
    FROM
    huawei_nbi_gsm."GHOSTSTATUS"

    """
)

G_IPPATH = ReplaceableObject(
    'huawei_cm_2g."G_IPPATH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISLNKBKFLAG",
        "ANI",
        "CNMNGMODE",
        "ISEGBTS",
        "ITFT",
        "PATHCHK",
        "PATHID",
        "PATHT",
        "REMARK",
        "RXBW",
        "TRMLOADTHINDEX",
        "TXBW",
        "VLANFLAG",
        "CHECKCOUNT",
        "CHECKT",
        "ICMPPKGLEN",
        "PERIOD",
        "CARRYFLAG",
        "IPADDR",
        "PEERIPADDR",
        "PEERMASK"
    FROM
    huawei_nbi_gsm."G_IPPATH"

    """
)

GKPIALMTHD = ReplaceableObject(
    'huawei_cm_2g."GKPIALMTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ASSMINNUM",
        "ASSSUCCRATIO",
        "IMMASSMINNUM",
        "IMMASSSUCCRATIO",
        "KPIALARMCHKTIMES",
        "KPIALARMSWITCH",
        "SVRCONNMINNUM",
        "SVRCONNSUCCRATIO"
    FROM
    huawei_nbi_gsm."GKPIALMTHD"

    """
)

GLOBALROUTESW = ReplaceableObject(
    'huawei_cm_2g."GLOBALROUTESW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "GLOBALROUTESW"
    FROM
    huawei_nbi_gsm."GLOBALROUTESW"

    """
)

GLTENCELL = ReplaceableObject(
    'huawei_cm_2g."GLTENCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "NBRLTENCELLID",
        "NCELLPRI",
        "SPTBLINDHO",
        "SPTRAPIDSEL",
        "SPTRESEL",
        "SRCLTENCELLID"
    FROM
    huawei_nbi_gsm."GLTENCELL"

    """
)

GMRCTRL = ReplaceableObject(
    'huawei_cm_2g."GMRCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CALLIDTYPE",
        "MRLOGNCELLTYPE",
        "MRSWITCH",
        "PREMRSAMPLE",
        "RAWMRSAMPLE"
    FROM
    huawei_nbi_gsm."GMRCTRL"

    """
)

GMRSCOPE = ReplaceableObject(
    'huawei_cm_2g."GMRSCOPE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "MRSCOPESWITCH"
    FROM
    huawei_nbi_gsm."GMRSCOPE"

    """
)

GNODEREDCFGCTRL = ReplaceableObject(
    'huawei_cm_2g."GNODEREDCFGCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SYNCDATACFGMODE"
    FROM
    huawei_nbi_gsm."GNODEREDCFGCTRL"

    """
)

GNODEREDUNDANCY = ReplaceableObject(
    'huawei_cm_2g."GNODEREDUNDANCY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "REDUNDANCYMODE"
    FROM
    huawei_nbi_gsm."GNODEREDUNDANCY"

    """
)

GPSCHRCTRL = ReplaceableObject(
    'huawei_cm_2g."GPSCHRCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DIFFSERVTHR",
        "PSCHRABIS",
        "PSCHRABNORMAL",
        "PSCHREVENT",
        "PSCHRGB",
        "PSCHRIMEI",
        "PSCHRINNINFO",
        "PSCHRINNMSG",
        "PSCHRMR",
        "PSCHRMRNUM",
        "PSCHRRESELECT",
        "PSCHRSERVICETYPE",
        "PSCHRTRAFFIC",
        "PSCHRUM",
        "PSCHRWLAN",
        "PSMOCNCHRINFO",
        "PSOUTMODE",
        "PSRCDSW",
        "SPEEDPDURCVTHR",
        "SPEEDPDUSNDTHR",
        "TDSERVNORSPTHR",
        "TDSERVPDUINTERVALTHR",
        "TDSERVPDURCVTHR",
        "TDSERVPDUSNDTHR"
    FROM
    huawei_nbi_gsm."GPSCHRCTRL"

    """
)

GPSCHRSCOPE = ReplaceableObject(
    'huawei_cm_2g."GPSCHRSCOPE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "CHRCOLLECTSWITCH"
    FROM
    huawei_nbi_gsm."GPSCHRSCOPE"

    """
)

GPSKPIALMTHD = ReplaceableObject(
    'huawei_cm_2g."GPSKPIALMTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PSACCESSMINNUM",
        "PSACCESSSUCCRATIO",
        "PSBRDKPIALMSWITCH",
        "PSKPIALARMCHKTIMES",
        "PSKPIALARMSWITCH"
    FROM
    huawei_nbi_gsm."GPSKPIALMTHD"

    """
)

GREDGRPHOSTPOLICY = ReplaceableObject(
    'huawei_cm_2g."GREDGRPHOSTPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNFAULTDELAY",
        "CNSTATEPOLICYFORGROUP",
        "MSTSERVACTDELAY",
        "REHOSTDELAYTIME",
        "REHOSTTYPE",
        "SLVSERVACTDELAY"
    FROM
    huawei_nbi_gsm."GREDGRPHOSTPOLICY"

    """
)

GRSVPARA = ReplaceableObject(
    'huawei_cm_2g."GRSVPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSCCSDPARA1",
        "BSCCSDPARA2",
        "BSCCSDPARA3",
        "BSCCSDPARA4",
        "BSCCSDPARA5",
        "BSCCSDPARA6",
        "BSCCSDPARA7",
        "BSCCSDPARA8",
        "BSCCSSWRSV0",
        "BSCCSSWRSV1",
        "BSCCSSWRSV2",
        "BSCPSDPARA0",
        "BSCPSDPARA1",
        "BSCPSDPARA10",
        "BSCPSSWRSV0",
        "BSCPSSWRSV1"
    FROM
    huawei_nbi_gsm."GRSVPARA"

    """
)

GTRX = ReplaceableObject(
    'huawei_cm_2g."GTRX"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTSTATUS",
        "ADMSTAT",
        "CELLID",
        "FREQ",
        "GTRXGROUPID",
        "ISMAINBCCH",
        "ISTMPTRX",
        "TRXID",
        "TRXNAME",
        "TRXNO"
    FROM
    huawei_nbi_gsm."GTRX"

    """
)

GTRXBASE = ReplaceableObject(
    'huawei_cm_2g."GTRXBASE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "MAXPDCHNUM",
        "MAXTSOCP",
        "TRXID"
    FROM
    huawei_nbi_gsm."GTRXBASE"

    """
)

GTRXCHAN = ReplaceableObject(
    'huawei_cm_2g."GTRXCHAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADMSTAT",
        "CHANRSV",
        "CHNO",
        "CHTYPE",
        "GPRSCHPRI",
        "TRXID",
        "TSPRIORITY"
    FROM
    huawei_nbi_gsm."GTRXCHAN"

    """
)

GTRXCHANHOP = ReplaceableObject(
    'huawei_cm_2g."GTRXCHANHOP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CHNO",
        "TRXDSSHOPINDEX",
        "TRXDSSMAIO",
        "TRXHOPINDEX",
        "TRXID",
        "TRXMAIO"
    FROM
    huawei_nbi_gsm."GTRXCHANHOP"

    """
)

GTRXDEV = ReplaceableObject(
    'huawei_cm_2g."GTRXDEV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CPS",
        "DSSTRXOFFLINE",
        "FREQREUSEMODE",
        "IBCATGTCIRMAIOFIXED",
        "INHOPWROVERLOADTHRESHOLD",
        "OPTL",
        "OUTHOPWROVERLOADTHRESHOLD",
        "PAOPTILEVEL",
        "PL16QAM",
        "PL32QAM",
        "PL8PSK",
        "POWL",
        "POWT",
        "POWTUNIT",
        "PWRSPNR",
        "RCVMD",
        "SDFLAG",
        "SNDMD",
        "TCHAJFLAG",
        "TRXID",
        "TRXLOGICLOCKSW",
        "TSPWRRESERVE"
    FROM
    huawei_nbi_gsm."GTRXDEV"

    """
)

GTRXFC = ReplaceableObject(
    'huawei_cm_2g."GTRXFC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CENDTHD",
        "CSTARTTHD",
        "FCETHD",
        "FCSTHD",
        "TRXID"
    FROM
    huawei_nbi_gsm."GTRXFC"

    """
)

GTRXHOP = ReplaceableObject(
    'huawei_cm_2g."GTRXHOP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HOPTYPE",
        "TRXID"
    FROM
    huawei_nbi_gsm."GTRXHOP"

    """
)

GTRXIUO = ReplaceableObject(
    'huawei_cm_2g."GTRXIUO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IUO",
        "TRXID"
    FROM
    huawei_nbi_gsm."GTRXIUO"

    """
)

GTRXRLALM = ReplaceableObject(
    'huawei_cm_2g."GTRXRLALM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TRXID",
        "WLNKALMFLAG"
    FROM
    huawei_nbi_gsm."GTRXRLALM"

    """
)

GTRXRSVPARA = ReplaceableObject(
    'huawei_cm_2g."GTRXRSVPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "GTRXRSVPARA5",
        "GTRXRSVSW",
        "TRXID"
    FROM
    huawei_nbi_gsm."GTRXRSVPARA"

    """
)

HOSTLOGSPD = ReplaceableObject(
    'huawei_cm_2g."HOSTLOGSPD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGSPD"
    FROM
    huawei_nbi_gsm."HOSTLOGSPD"

    """
)

IDRQTEST = ReplaceableObject(
    'huawei_cm_2g."IDRQTEST"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENCRYID",
        "IDRQDURATION",
        "IDRQSEQSW",
        "IDRQSWITCH",
        "LUIDRQALLOW",
        "SENDMMNULLPERMIT",
        "USERIDTRACEMODE",
        "USERIDTRACETYPE"
    FROM
    huawei_nbi_gsm."IDRQTEST"

    """
)

INFBRDRESCFG = ReplaceableObject(
    'huawei_cm_2g."INFBRDRESCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGSW",
        "RESSW",
        "RESTIMESPERDAY",
        "RESTYPE",
        "STATISTICUOIPLOOPFAULTTIME",
        "BRDFAULTBCRATE",
        "CONTINUOUSFAULTTIMES",
        "MERELOADCONTINUOUSFAULTTIMES",
        "BRDFAULTNSRATE",
        "NSRESSW"
    FROM
    huawei_nbi_gsm."INFBRDRESCFG"

    """
)

INTBRDPARA = ReplaceableObject(
    'huawei_cm_2g."INTBRDPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BRDCHIPSELFCURESW",
        "BT",
        "DHCPDSCP",
        "FCALMRTHD",
        "FCALMSW",
        "FCALMTHD",
        "MSPCHECKSW",
        "OPTBRDK1K2FCSW",
        "OPTCONNERRALMSW",
        "PPPBOARDCARSW",
        "SN",
        "SRN",
        "ARPEXPIRETIMEOPTIMIZESW",
        "ARPPKTSENDMODE",
        "ARPVLANPRI",
        "IPPROTOCOLCHECKSW",
        "OVERSIZEPKTSW",
        "PORTFCSWITCH",
        "RECPORTSWITCHOVERSW",
        "SIGPACKCTRLSW"
    FROM
    huawei_nbi_gsm."INTBRDPARA"

    """
)

IPCHK = ReplaceableObject(
    'huawei_cm_2g."IPCHK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ARPRETRY",
        "ARPTIMEOUT",
        "BAKIP",
        "BAKMASK",
        "CARRYT",
        "CHKN",
        "CHKTYPE",
        "CMEMODE",
        "PEERIP",
        "PN",
        "ROUTEASSOCIATEDFLAG",
        "SN",
        "SRN",
        "BFDDETECTCOUNT",
        "DSCP",
        "MINRXINT",
        "MINTXINT",
        "MYDISCRIMINATOR",
        "WHETHERAFFECTSWAP"
    FROM
    huawei_nbi_gsm."IPCHK"

    """
)

IPGUARD = ReplaceableObject(
    'huawei_cm_2g."IPGUARD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ARPANTICHEATSW",
        "ARPLRNSTRICTSW",
        "ARPREQALMCLRTHD",
        "ARPREQALMSW",
        "ARPREQALMTHD",
        "ARPRLYALMCLRTHD",
        "ARPRLYALMSW",
        "ARPRLYALMTHD",
        "BFDCTRLALMCLRTHD",
        "BFDCTRLALMSW",
        "BFDCTRLALMTHD",
        "BRDTYPE",
        "DHCPALMCLRTHD",
        "DHCPALMSW",
        "DHCPALMTHD",
        "ETHOAMALMCLRTHD",
        "ETHOAMALMSW",
        "ETHOAMALMTHD",
        "FWPKTTYPE",
        "ICMPALMRTHD",
        "ICMPALMSW",
        "ICMPALMTHD",
        "INVALIDMCASTALMRTHD",
        "INVALIDMCASTALMSW",
        "INVALIDMCASTALMTHD",
        "LACPALMCLRTHD",
        "LACPALMSW",
        "LACPALMTHD",
        "OMUFWFLAG",
        "SN",
        "SRN",
        "VALIDPKTCHKSW"
    FROM
    huawei_nbi_gsm."IPGUARD"

    """
)

IPLOGICPORT = ReplaceableObject(
    'huawei_cm_2g."IPLOGICPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BT",
        "BWADJ",
        "CARRYT",
        "CBS",
        "CIR",
        "FCINDEX",
        "FLOWCTRLSWITCH",
        "LPN",
        "LPNTYPE",
        "OAMFLOWBW",
        "OPSEPFLAG",
        "PN",
        "RSCMNGMODE",
        "SN",
        "SRN",
        "TRMLOADTHINDEX"
    FROM
    huawei_nbi_gsm."IPLOGICPORT"

    """
)

IPMUX = ReplaceableObject(
    'huawei_cm_2g."IPMUX"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANI",
        "FPTIMER",
        "IPMUXINDEX",
        "ISQOSPATH",
        "MAXFRAMELEN",
        "MUXTYPE",
        "PATHID",
        "SUBFRAMELEN"
    FROM
    huawei_nbi_gsm."IPMUX"

    """
)

IPRT = ReplaceableObject(
    'huawei_cm_2g."IPRT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DSTIP",
        "DSTMASK",
        "NEXTHOP",
        "NEXTHOPTYPE",
        "PRIORITY",
        "REMARK",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."IPRT"

    """
)

ITWKPIALMTHD = ReplaceableObject(
    'huawei_cm_2g."ITWKPIALMTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ITWKPIALMSW"
    FROM
    huawei_nbi_gsm."ITWKPIALMTHD"

    """
)

L2L3ROUTEPOLICY = ReplaceableObject(
    'huawei_cm_2g."L2L3ROUTEPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ROUTEPOLICY"
    FROM
    huawei_nbi_gsm."L2L3ROUTEPOLICY"

    """
)

LDR = ReplaceableObject(
    'huawei_cm_2g."LDR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LDRCONGSTATEJOINJUDGESW",
        "LDRFOUH",
        "LDRFST",
        "LDRHISTORYCONGSTATEREFSW",
        "LDRSND",
        "LSRTRD"
    FROM
    huawei_nbi_gsm."LDR"

    """
)

LICALMTHD = ReplaceableObject(
    'huawei_cm_2g."LICALMTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LICALMCTHD",
        "LICALMRTHD"
    FROM
    huawei_nbi_gsm."LICALMTHD"

    """
)

LICPOLICY = ReplaceableObject(
    'huawei_cm_2g."LICPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LICUSAGESTATICMODE",
        "RVKMODE"
    FROM
    huawei_nbi_gsm."LICPOLICY"

    """
)

LODCTRL = ReplaceableObject(
    'huawei_cm_2g."LODCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LODCTRL"
    FROM
    huawei_nbi_gsm."LODCTRL"

    """
)

LOGLIMIT = ReplaceableObject(
    'huawei_cm_2g."LOGLIMIT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNTL",
        "LT",
        "TL"
    FROM
    huawei_nbi_gsm."LOGLIMIT"

    """
)

M3DE = ReplaceableObject(
    'huawei_cm_2g."M3DE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DENO",
        "DPX",
        "ENTITYT",
        "LENO",
        "NAME",
        "RTCONTEXT"
    FROM
    huawei_nbi_gsm."M3DE"

    """
)

M3LE = ReplaceableObject(
    'huawei_cm_2g."M3LE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENTITYT",
        "LENO",
        "NAME",
        "RTCONTEXT",
        "SPX"
    FROM
    huawei_nbi_gsm."M3LE"

    """
)

M3LKS = ReplaceableObject(
    'huawei_cm_2g."M3LKS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DENO",
        "LNKSLSMASK",
        "M3UAHBSW",
        "NAME",
        "PDTMRVALUE",
        "SIGLKSX",
        "TRAMODE",
        "WKMODE"
    FROM
    huawei_nbi_gsm."M3LKS"

    """
)

M3LNK = ReplaceableObject(
    'huawei_cm_2g."M3LNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LNKREDFLAG",
        "NAME",
        "PRIORITY",
        "SCTPLNKID",
        "SCTPLNKN",
        "SIGLKSX",
        "SIGLNKID",
        "SN",
        "SRN",
        "SSN"
    FROM
    huawei_nbi_gsm."M3LNK"

    """
)

M3RT = ReplaceableObject(
    'huawei_cm_2g."M3RT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DENO",
        "NAME",
        "PRIORITY",
        "SIGLKSX"
    FROM
    huawei_nbi_gsm."M3RT"

    """
)

MDTLCS = ReplaceableObject(
    'huawei_cm_2g."MDTLCS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLID",
        "GMDTASKMODE",
        "GMDTASKSWITCH",
        "PERIOD",
        "PRECISIONMDT",
        "SMLCID"
    FROM
    huawei_nbi_gsm."MDTLCS"

    """
)

MNTMODE = ReplaceableObject(
    'huawei_cm_2g."MNTMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "MNTMODE"
    FROM
    huawei_nbi_gsm."MNTMODE"

    """
)

MOCNPARA = ReplaceableObject(
    'huawei_cm_2g."MOCNPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSCNRESPTMR",
        "LTEUSESHASW",
        "PSCNRESPTMR"
    FROM
    huawei_nbi_gsm."MOCNPARA"

    """
)

MSGSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."MSGSOFTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLLISTOPTIONSEND",
        "CHOSENCHINASSCMP",
        "CHOSENCHINHOPERFORM",
        "CHOSENCHINHOREQACK",
        "CHOSENENCRYPALGINCIPHCMP",
        "CHOSENENCRYPALGINHOPERFORM",
        "CHOSENENCRYPALOINASSCMP",
        "CHOSENENCRYPALOINHOREQACK",
        "CICPOOLINASSFAIL",
        "CICPOOLINHOFAIL",
        "CICPOOLLISTINASSFAIL",
        "CICPOOLLISTINHOFAIL",
        "CICPOOLNUM",
        "CICPOOLSENDFLAGINASSCMP",
        "CICPOOLSENDFLAGINHOACK",
        "CIPHERMODEINHOREQACK",
        "CNNODEIDX",
        "CURCHANNELINHORQD",
        "HOFAILINDIRECTRETRYSW",
        "HOSDCCHSPEECHVER",
        "SPEECHCODEINHOREQACK",
        "SPEECHVERINASSCMP",
        "SPEECHVERINHOPERFORM",
        "SPEECHVERINHOREQACK",
        "SPEECHVERINHORQD",
        "UCCTRLOFCICIE"
    FROM
    huawei_nbi_gsm."MSGSOFTPARA"

    """
)

MSP = ReplaceableObject(
    'huawei_cm_2g."MSP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CMEMODE",
        "K2MODE",
        "PN",
        "RT",
        "SDENABLE",
        "SDSFPRI",
        "SN",
        "SRN",
        "WTRT"
    FROM
    huawei_nbi_gsm."MSP"

    """
)

MTP3LKS = ReplaceableObject(
    'huawei_cm_2g."MTP3LKS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DPX",
        "EMERGENCY",
        "LNKSLSMASK",
        "NAME",
        "SIGLKSX"
    FROM
    huawei_nbi_gsm."MTP3LKS"

    """
)

MTP3LNK = ReplaceableObject(
    'huawei_cm_2g."MTP3LNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APN",
        "ASN",
        "ASRN",
        "ATSMASK",
        "BEARTYPE",
        "CT1",
        "CT2",
        "CT3",
        "CT4E",
        "CT4N",
        "CT5",
        "CT6",
        "CT7",
        "CT9",
        "LKTATE",
        "MTP2LNKN",
        "NAME",
        "PRIORITY",
        "SIGLKSX",
        "SIGSLC",
        "SN",
        "SRN",
        "SSN",
        "STFLG",
        "TC",
        "TCLEN",
        "TCMODE"
    FROM
    huawei_nbi_gsm."MTP3LNK"

    """
)

MTP3RT = ReplaceableObject(
    'huawei_cm_2g."MTP3RT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DPX",
        "NAME",
        "PRIORITY",
        "SIGLKSX"
    FROM
    huawei_nbi_gsm."MTP3RT"

    """
)

MTP3TMR = ReplaceableObject(
    'huawei_cm_2g."MTP3TMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "T10TMR",
        "T12TMR",
        "T13TMR",
        "T14TMR",
        "T17TMR",
        "T1TMR",
        "T22TMR",
        "T23TMR",
        "T2TMR",
        "T3TMR",
        "T4TMR",
        "T5TMR",
        "T8TMR",
        "TMT1TMR",
        "TMT2TMR"
    FROM
    huawei_nbi_gsm."MTP3TMR"

    """
)

N7DPC = ReplaceableObject(
    'huawei_cm_2g."N7DPC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BEARTYPE",
        "DPC",
        "DPCT",
        "DPX",
        "NAME",
        "NEIGHBOR",
        "PROT",
        "SLSMASK",
        "SPDF",
        "SPX",
        "SSTTIMEOUTSTRA",
        "STP"
    FROM
    huawei_nbi_gsm."N7DPC"

    """
)

NRIMSCMAP = ReplaceableObject(
    'huawei_cm_2g."NRIMSCMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNNODEIDX",
        "NRI"
    FROM
    huawei_nbi_gsm."NRIMSCMAP"

    """
)

NRISGSNMAP = ReplaceableObject(
    'huawei_cm_2g."NRISGSNMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNID",
        "NRI",
        "OPNAME"
    FROM
    huawei_nbi_gsm."NRISGSNMAP"

    """
)

NSE = ReplaceableObject(
    'huawei_cm_2g."NSE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNID",
        "ISNCMODE",
        "LCSSUP",
        "MOCNSUP",
        "NSEI",
        "OPNAME",
        "PFCSUP",
        "PSHOSUP",
        "PT",
        "RIMSUP",
        "SN",
        "SRN",
        "SVRIP",
        "SVRPORT"
    FROM
    huawei_nbi_gsm."NSE"

    """
)

NSVLLOCAL = ReplaceableObject(
    'huawei_cm_2g."NSVLLOCAL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IP",
        "LOCALNSVLI",
        "NSEI",
        "SIGLW",
        "SN",
        "SRN",
        "SRVLW",
        "UDPPN"
    FROM
    huawei_nbi_gsm."NSVLLOCAL"

    """
)

OBJALMSHLD = ReplaceableObject(
    'huawei_cm_2g."OBJALMSHLD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AID",
        "AIDST",
        "DSPN",
        "OBJTP",
        "PN",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."OBJALMSHLD"

    """
)

OBJAUTHSW = ReplaceableObject(
    'huawei_cm_2g."OBJAUTHSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SW"
    FROM
    huawei_nbi_gsm."OBJAUTHSW"

    """
)

OMUCOMMSVCSW = ReplaceableObject(
    'huawei_cm_2g."OMUCOMMSVCSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALMBOXSVCSW"
    FROM
    huawei_nbi_gsm."OMUCOMMSVCSW"

    """
)

OMUETH = ReplaceableObject(
    'huawei_cm_2g."OMUETH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALMSW"
    FROM
    huawei_nbi_gsm."OMUETH"

    """
)

OMUPARA = ReplaceableObject(
    'huawei_cm_2g."OMUPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CAPMONLOGSW",
        "DISKFAULTSWAPSW",
        "FREEDISKSW",
        "HOSTLOGFCSW",
        "INTCHKFAILSTOPLOADSW"
    FROM
    huawei_nbi_gsm."OMUPARA"

    """
)

OMUPORT = ReplaceableObject(
    'huawei_cm_2g."OMUPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PORTTYPE",
        "SW"
    FROM
    huawei_nbi_gsm."OMUPORT"

    """
)

OPC = ReplaceableObject(
    'huawei_cm_2g."OPC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HOSTTYPE",
        "NAME",
        "NI",
        "RSTFUN",
        "SPC",
        "SPCBITS",
        "SPDF",
        "SPX"
    FROM
    huawei_nbi_gsm."OPC"

    """
)

OPLOCK = ReplaceableObject(
    'huawei_cm_2g."OPLOCK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCKST"
    FROM
    huawei_nbi_gsm."OPLOCK"

    """
)

OPSW = ReplaceableObject(
    'huawei_cm_2g."OPSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SWOP"
    FROM
    huawei_nbi_gsm."OPSW"

    """
)

OPT = ReplaceableObject(
    'huawei_cm_2g."OPT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AUTYPE",
        "B1B2SDTHRD",
        "B1B2SFTHRD",
        "B3SDTHRD",
        "B3SFTHRD",
        "BT",
        "J0TYPE",
        "J1TYPE",
        "JAUTOADD",
        "LNKNUMMODE",
        "OPTM",
        "PN",
        "PS",
        "S1VALUE",
        "SN",
        "SRN",
        "J0BYTE_FORMAT",
        "J0RXVALUE",
        "J0TXVALUE",
        "J1BYTE_FORMAT",
        "J1RXVALUE",
        "J1TXVALUE"
    FROM
    huawei_nbi_gsm."OPT"

    """
)

OSPWDPOLICY = ReplaceableObject(
    'huawei_cm_2g."OSPWDPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTSW",
        "COMPLICACY",
        "COMPLICACYSW",
        "DICTCHKSW",
        "HISTORYPWDNUM",
        "MAXVALIDDATES",
        "PWDMINLEN"
    FROM
    huawei_nbi_gsm."OSPWDPOLICY"

    """
)

OTHSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."OTHSOFTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISLINKFAILCALLDROPOPT",
        "ABNORMALMOSTHRESHOLD",
        "ACCCAUSESTATOPT",
        "AINTFMSGUSINGTHRESHOLD",
        "AMRHRLICUPDOPTSW",
        "AN19",
        "ASSFAILSTATEOPT",
        "ASSFAILSTATISTICOPT",
        "ASSTHRES",
        "ATER8KSW",
        "ATERCONGHRFLAG",
        "ATERCONGSTRATIO",
        "AUTOGETBTSLOGFLAG",
        "BSCPMA",
        "BSCPMAIRAHO",
        "BSCPRICLASS",
        "BSCQAD",
        "BSCQADIRAHO",
        "BSCRESERVEDPARA20",
        "BSCRESERVEDPARA21",
        "BSCRESERVEDPARA3",
        "BSCRESERVEDPARA6",
        "BSCRESERVEDPARA8",
        "BTSCHRMSISDN",
        "CALLRSTDROPSTATOPT",
        "CAOPT",
        "CFGCHANCHANGEOPT",
        "CHECKINGBTSCONNECTION",
        "CHRMRNCELLTYPE",
        "CLASSMARK3FLAG",
        "CLASSMARKQUERY",
        "CMUPDATEOPTIMIZETYPE",
        "CSDOUTBSCFAILSTAT",
        "CSSCNIDHOFILTER",
        "DELAYSENDHOCMDSTIMER",
        "DELAYSENDHOCMDSWITCH",
        "DISCONNECTHANDOVERPROTECTTIMER",
        "DLDTMFPRCSW",
        "DTMCSHOOPTSW",
        "DTMUPDATEOPTITYPE",
        "EMLPPPRIORITY",
        "EMRPROMSREQTIMES",
        "EMRPROMSSATTIMES",
        "END2ENDTRACESTATE",
        "EQUIPFAILDROPOPT",
        "FASTRESELECTSW",
        "FLEXABISTSPREEMPTOPTSW",
        "FRSUPPORTWHENCELLCONGEST",
        "G2G3GLDBLCDELTATHRD",
        "GRPULCHK",
        "HALFRATEDATASUPPORT",
        "HIGHLEVPREEM",
        "HOPSINGLEFREQOPTSWITCH",
        "IBCAFLOWCTRLPERIOD",
        "IBCAFLOWCTRLTHRELD",
        "IBCAINBSCINFORPTPRD",
        "IBCAOUTBSCINFORPTPRD",
        "IMMTCHMOC",
        "IMMTCHMTC",
        "IMSIHOCTRL",
        "INBSCCLRCMDSTATOPT",
        "INHOEC",
        "INHOFAILSTATOPT",
        "INTERBSCHOPREEMPALLOWED",
        "INTERRATCELLRESELOPTEN",
        "IURGLOADCAPOPTSWITCH",
        "JITBUFSWITCH",
        "KCRIRESORTSWITCH",
        "MAXLOADBTSNUM",
        "MAXPBLINKCHKNUM",
        "MOCNCTRL",
        "MOCNXIDRSTPOLICY",
        "MODIFYATTREQNU",
        "MSCABNORMALRELSTATSDCCHDROP",
        "MSCABNORMALRELSTATTCHDROP",
        "MSCREASSOPTSW",
        "MUTESAICIDEALPHALTHD",
        "MUTESAICIDEALPHAUTHD",
        "MUTESAICIDEREQTIMES",
        "MUTESAICIDESATTIMES",
        "N3GCELLCOVERAGETH1",
        "N3GCELLCOVERAGETH2",
        "N3GCELLMEASURETH0",
        "N3GCELLMEASURETH1",
        "N3GCELLMEASURETH2",
        "NAVIGATION",
        "NCELLINTERFLEVELTHRES0",
        "NCELLINTERFLEVELTHRES1",
        "NCELLINTERFLEVELTHRES2",
        "NCELLINTERFLEVELTHRES3",
        "NCELLINTERFLEVELTHRES4",
        "NCELLINTERFLEVELTHRES5",
        "NCELLINTERFLEVELTHRES6",
        "NCELLINTERFLEVELTHRES7",
        "NCELLSTATOPTTIME",
        "NOCAIMMASSSTATOPT",
        "NONIBCADYNMEAEN",
        "NOTMSIALLCELLPAGINGLIMITFLAG",
        "NROFFDDCELLFLAG",
        "OMLDETECTTIME",
        "OUTBSCHOFAILSTATOPTSW",
        "OUTBSCHOREQSTATOPT",
        "OUTSYSSERVHOREASSIGNEN",
        "OUTSYSSERVICEHOEN",
        "PBMTNMSGRESEND",
        "PDCH2TCHOPTSWITCH",
        "PREEMFORHONOTREL",
        "PREEMFORHOPDCH",
        "PSSCNIDHOFILTER",
        "QUEINASSOPTSTAT",
        "RECORDDISCARDEDPAGINGINFOFLAG",
        "REDIRECTOPT",
        "RELCAUSENOTIRSP",
        "RELOCRATETYPECHG",
        "RESCHECKALLOWED",
        "RESETALMDELAYSWITCH",
        "RESETALMDELAYTIME",
        "RESPREQSEL",
        "RSSTHRES",
        "SAICPROMSIDEREQTIMES",
        "SAICPROMSIDESATTIMES",
        "SEND2QUTERFLAG",
        "SENDDOWNLINKMESSAGE",
        "SENDSI2TERFLAG",
        "SENDSI5TERFLAG",
        "SENDSPEECHVERSIONAHEAD",
        "SENDUTRANECSCFLAG",
        "SERV3GCELLIDOPT",
        "SHORTCALLTHRED",
        "SI2TERSWITCH",
        "SPTPBLAPDCHECK",
        "SPTPBRESCHECK",
        "SPTPBSGLPASSCHECK",
        "SPTPCICCHECK",
        "SUPPORTAPPLYUSEDCIC",
        "SUTMROPMODE",
        "TALIMITDROPSTATOPT",
        "TASATEABNORMALOPT",
        "TCHBUSYSATEOPTSWITCH",
        "TCHRATEMODIFY",
        "TCSTATISTICSW",
        "TCSTATISTICTYPE",
        "TER2INDICATOR",
        "TIMESTAMPERRORCMPSWITH",
        "TRXAVAILJUDGOPT",
        "UCISRAIFAULT",
        "ULTOOLLOWRXLEV",
        "VIPUSROUTBSCHOSWITCH",
        "VIPUSRSWITCH",
        "VIPUSRTCHTHRES",
        "VOICEOPENTRACESW",
        "WINADJSWITCH",
        "VAMOSACTPCDSWITCH"
    FROM
    huawei_nbi_gsm."OTHSOFTPARA"

    """
)

PACKETFILTERALMPARA = ReplaceableObject(
    'huawei_cm_2g."PACKETFILTERALMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PKTFILTERALMRTHD",
        "PKTFILTERALMTHD"
    FROM
    huawei_nbi_gsm."PACKETFILTERALMPARA"

    """
)

PHBMAP = ReplaceableObject(
    'huawei_cm_2g."PHBMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DSCP",
        "PHB",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."PHBMAP"

    """
)

PORTFLOWCTRLPARA = ReplaceableObject(
    'huawei_cm_2g."PORTFLOWCTRLPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CONGCLRTHD0",
        "CONGCLRTHD1",
        "CONGCLRTHD2",
        "CONGCLRTHD3",
        "CONGCLRTHD4",
        "CONGCLRTHD5",
        "CONGTHD0",
        "CONGTHD1",
        "CONGTHD2",
        "CONGTHD3",
        "CONGTHD4",
        "CONGTHD5",
        "DROPPKTTHD0",
        "DROPPKTTHD1",
        "DROPPKTTHD2",
        "DROPPKTTHD3",
        "DROPPKTTHD4",
        "DROPPKTTHD5",
        "FCINDEX",
        "PORTPROTYPE",
        "PQNUM"
    FROM
    huawei_nbi_gsm."PORTFLOWCTRLPARA"

    """
)

PORTOSCCTRLPARA = ReplaceableObject(
    'huawei_cm_2g."PORTOSCCTRLPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SN",
        "SRN",
        "SUPPRESSSWITCH"
    FROM
    huawei_nbi_gsm."PORTOSCCTRLPARA"

    """
)

PSPREFABISCONGCTRL = ReplaceableObject(
    'huawei_cm_2g."PSPREFABISCONGCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "UCPSPREFCALLREESTPRIO",
        "UCPSPREFCSEMERGCALLPRIO",
        "UCPSPREFCSORGCALLPRIO",
        "UCPSPREFCSTERMCALLPRIO",
        "UCPSPREFINBSCHOPRIO",
        "UCPSPREFINTRABSCHOPRIO",
        "UCPSPREFOTHERPRIO",
        "UCPSPREFPSPRIO",
        "UCPSPREFSUPPLEPRIO",
        "UCPSPREFVBSPRIO",
        "UCPSPREFVGCSPRIO"
    FROM
    huawei_nbi_gsm."PSPREFABISCONGCTRL"

    """
)

PSUSRRESBIND = ReplaceableObject(
    'huawei_cm_2g."PSUSRRESBIND"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IDXTYPE"
    FROM
    huawei_nbi_gsm."PSUSRRESBIND"

    """
)

PTPBVC = ReplaceableObject(
    'huawei_cm_2g."PTPBVC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BVCI",
        "CELLID",
        "NSEI"
    FROM
    huawei_nbi_gsm."PTPBVC"

    """
)

PWDPOLICY = ReplaceableObject(
    'huawei_cm_2g."PWDPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AUTOUNLOCKTIME",
        "COMPLICACY",
        "DICTCHKSW",
        "FIRSTLOGINMUSTMODPWD",
        "HISTORYPWDNUM",
        "MAXMISSTIMES",
        "MAXPROMPTDATES",
        "MAXREPEATCHARTIMES",
        "MAXVALIDDATES",
        "MINVALIDINTERVAL",
        "PWDMINLEN",
        "RESETINTERVAL"
    FROM
    huawei_nbi_gsm."PWDPOLICY"

    """
)

PWRALMSW = ReplaceableObject(
    'huawei_cm_2g."PWRALMSW"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PWRALMSSW1",
        "PWRALMSSW2",
        "SRN"
    FROM
    huawei_nbi_gsm."PWRALMSW"

    """
)

PWRPARA = ReplaceableObject(
    'huawei_cm_2g."PWRPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "NO1M48ALMTHDDOWN",
        "NO1M48ALMTHDUP",
        "NO2M48ALMTHDDOWN",
        "NO2M48ALMTHDUP",
        "NO3M48ALMTHDDOWN",
        "NO3M48ALMTHDUP",
        "NO4M48ALMTHDDOWN",
        "NO4M48ALMTHDUP",
        "NO5M48ALMTHDDOWN",
        "NO5M48ALMTHDUP",
        "NO6M48ALMTHDDOWN",
        "NO6M48ALMTHDUP",
        "SRN"
    FROM
    huawei_nbi_gsm."PWRPARA"

    """
)

QUEUEMAP = ReplaceableObject(
    'huawei_cm_2g."QUEUEMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "OAMMINBWKEY",
        "Q0MINDSCP",
        "Q1MINDSCP",
        "Q2MINDSCP",
        "Q3MINDSCP",
        "Q4MINDSCP",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."QUEUEMAP"

    """
)

RSVRES = ReplaceableObject(
    'huawei_cm_2g."RSVRES"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BMDPUSLOTNO",
        "BMDPUSUBRACKNO",
        "BMDSPENDTS",
        "BMDSPNO",
        "BMDSPSTARTTS",
        "BSCTID",
        "BTCFLAG",
        "RESRESERVEDMINUTES"
    FROM
    huawei_nbi_gsm."RSVRES"

    """
)

RULELIBVER = ReplaceableObject(
    'huawei_cm_2g."RULELIBVER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "VERIFYLIBVER"
    FROM
    huawei_nbi_gsm."RULELIBVER"

    """
)

SAUCENTER = ReplaceableObject(
    'huawei_cm_2g."SAUCENTER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FTPCENTER",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."SAUCENTER"

    """
)

SCCPTMR = ReplaceableObject(
    'huawei_cm_2g."SCCPTMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CONNECTTMR",
        "COTMR",
        "EATMR",
        "FREEZENTMR",
        "GUARDTMR",
        "IARXTMR",
        "IATXTMR",
        "IGNORTMR",
        "INTTMR",
        "LRNTMR",
        "REASTMR",
        "RELEASETMR",
        "REPRELEASETMR",
        "RESETTMR",
        "STATTMR"
    FROM
    huawei_nbi_gsm."SCCPTMR"

    """
)

SCTPLNK = ReplaceableObject(
    'huawei_cm_2g."SCTPLNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APP",
        "BUNDLINGFLAG",
        "CHKSUMRX",
        "CHKSUMTX",
        "CHKSUMTYPE",
        "CMEMODE",
        "CROSSIPFLAG",
        "DSCP",
        "HBINTER",
        "LOCIP1",
        "LOCIP2",
        "LOCPN",
        "LOGPORTFLAG",
        "MAXASSOCRETR",
        "MAXPATHRETR",
        "MTU",
        "PEERIP1",
        "PEERIP2",
        "PEERMULTIFASTRETRANFLAG",
        "PEERPN",
        "REMARK",
        "RTOALPHA",
        "RTOBETA",
        "RTOINIT",
        "RTOMAX",
        "RTOMIN",
        "SCTPLNKID",
        "SCTPLNKN",
        "SN",
        "SRN",
        "SWITCHBACKFLAG",
        "SWITCHBACKHBNUM",
        "TSACK",
        "VLANFLAG1",
        "VLANFLAG2"
    FROM
    huawei_nbi_gsm."SCTPLNK"

    """
)

SCTPPROF = ReplaceableObject(
    'huawei_cm_2g."SCTPPROF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APP",
        "BUNDLINGFLAG",
        "CHKSUMTYPE",
        "CROSSIPFLAG",
        "HBINTER",
        "MAXASSOCRETR",
        "MAXPATHRETR",
        "MTU",
        "PEERMULTIFASTRETRANFLAG",
        "RTOALPHA",
        "RTOBETA",
        "RTOINIT",
        "RTOMAX",
        "RTOMIN",
        "SCTPPROFID",
        "SWITCHBACKFLAG",
        "SWITCHBACKHBNUM",
        "TSACK"
    FROM
    huawei_nbi_gsm."SCTPPROF"

    """
)

SCTPSRVPORT = ReplaceableObject(
    'huawei_cm_2g."SCTPSRVPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISCPSRVPN",
        "BBAPSRVPN",
        "M3UASRVPN",
        "NBAPSRVPN"
    FROM
    huawei_nbi_gsm."SCTPSRVPORT"

    """
)

SCUPORT = ReplaceableObject(
    'huawei_cm_2g."SCUPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PN",
        "SN",
        "SRN",
        "SWITCH"
    FROM
    huawei_nbi_gsm."SCUPORT"

    """
)

SGSN = ReplaceableObject(
    'huawei_cm_2g."SGSN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPADDR1",
        "IPADDR2",
        "SGSNNAME"
    FROM
    huawei_nbi_gsm."SGSN"

    """
)

SGSNNODE = ReplaceableObject(
    'huawei_cm_2g."SGSNNODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNID",
        "OPNAME",
        "SGSNCAP",
        "SGSNSTATUS"
    FROM
    huawei_nbi_gsm."SGSNNODE"

    """
)

SNTPCLTPARA = ReplaceableObject(
    'huawei_cm_2g."SNTPCLTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SP"
    FROM
    huawei_nbi_gsm."SNTPCLTPARA"

    """
)

SNTPSRVINFO = ReplaceableObject(
    'huawei_cm_2g."SNTPSRVINFO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AUTHMODE",
        "IP",
        "PT"
    FROM
    huawei_nbi_gsm."SNTPSRVINFO"

    """
)

SRCONPATH = ReplaceableObject(
    'huawei_cm_2g."SRCONPATH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SCPIDX",
        "SRN1",
        "SRN2",
        "TDMN1",
        "TDMN2"
    FROM
    huawei_nbi_gsm."SRCONPATH"

    """
)

SS7PATCHSWITCH = ReplaceableObject(
    'huawei_cm_2g."SS7PATCHSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SWITCHPARAMETER1",
        "SWITCHPARAMETER10",
        "SWITCHPARAMETER11",
        "SWITCHPARAMETER12",
        "SWITCHPARAMETER13",
        "SWITCHPARAMETER14",
        "SWITCHPARAMETER15",
        "SWITCHPARAMETER16",
        "SWITCHPARAMETER17",
        "SWITCHPARAMETER18",
        "SWITCHPARAMETER19",
        "SWITCHPARAMETER2",
        "SWITCHPARAMETER20",
        "SWITCHPARAMETER3",
        "SWITCHPARAMETER4",
        "SWITCHPARAMETER5",
        "SWITCHPARAMETER6",
        "SWITCHPARAMETER7",
        "SWITCHPARAMETER8",
        "SWITCHPARAMETER9"
    FROM
    huawei_nbi_gsm."SS7PATCHSWITCH"

    """
)

SSLAUTHMODE = ReplaceableObject(
    'huawei_cm_2g."SSLAUTHMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AUTHMODE"
    FROM
    huawei_nbi_gsm."SSLAUTHMODE"

    """
)

SSLCONF = ReplaceableObject(
    'huawei_cm_2g."SSLCONF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOWESTCSLEVEL",
        "RENEGO",
        "RENEGOINTERVAL",
        "VERSION"
    FROM
    huawei_nbi_gsm."SSLCONF"

    """
)

SSLCS = ReplaceableObject(
    'huawei_cm_2g."SSLCS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSLEVEL",
        "CSNAME"
    FROM
    huawei_nbi_gsm."SSLCS"

    """
)

SUBNET = ReplaceableObject(
    'huawei_cm_2g."SUBNET"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EXSUBNET",
        "SUBNET"
    FROM
    huawei_nbi_gsm."SUBNET"

    """
)

SUBRACK = ReplaceableObject(
    'huawei_cm_2g."SUBRACK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CONNPWR",
        "SCUTYPE",
        "SRN",
        "SRNAME",
        "SRTTYPE",
        "TYPE",
        "WORKMODE"
    FROM
    huawei_nbi_gsm."SUBRACK"

    """
)

SUBSESSION_NE = ReplaceableObject(
    'huawei_cm_2g."SUBSESSION_NE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion"
    FROM
    huawei_nbi_gsm."SUBSESSION_NE"

    """
)

SYNSWITCH = ReplaceableObject(
    'huawei_cm_2g."SYNSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SYNSWITCH"
    FROM
    huawei_nbi_gsm."SYNSWITCH"

    """
)

SYS = ReplaceableObject(
    'huawei_cm_2g."SYS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SYSCONTACT",
        "SYSDESC",
        "SYSLOCATION",
        "SYSOBJECTID",
        "SYSSERVICES"
    FROM
    huawei_nbi_gsm."SYS"

    """
)

TCPARA = ReplaceableObject(
    'huawei_cm_2g."TCPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISUPSTRMCHECKSW",
        "ACLPENFLAG",
        "AECDEFAULTERL",
        "AECDETECTTHRESHOLD",
        "AECDETECTTIME",
        "AECENFLAG",
        "AECERLMODE",
        "AECFIRSTTH",
        "AECMODE",
        "AECPUREDELAY",
        "AECSTATLEN",
        "AECTAIL",
        "AIPCOMPHOENSW",
        "ALCADAPTMODE",
        "ALCENFLAG",
        "ALCFIXGAIN",
        "ALCFIXLEV",
        "ALCMAXGAIN",
        "ALCMAXLEV",
        "ALCMINLEV",
        "AMRHONOISEFLTSWITCH",
        "AMRSIDCMRSETMODE",
        "ANCENFLAG",
        "ANCMAXGAIN",
        "ANCSNRGATERS",
        "ANRBYPASSNSELEV",
        "ANRENFLAG",
        "ANRMODE",
        "ANRNSEREDUCTLEV",
        "ANRNSEREDUCTMODE",
        "C5SWITCH",
        "CSDRTPHOENSW",
        "DSPN",
        "DWCMRMODE",
        "ENCODEMODE",
        "EPLCMODE",
        "EPLCSWITCH",
        "EVADENFLAG",
        "FAULTDETECTSWITCH",
        "FORCE_LIMIT_TIME",
        "FRFLOWREDUCESWITCH",
        "G711_MODE",
        "HAMRTFO8P8MODSWITCH",
        "HRTOCSWITCH",
        "IDLE_CODE",
        "LASTWORDGETMODE",
        "NOISEAMPLITUDESWITCH",
        "NOISE_LIMIT_THRESHOLD",
        "PACKCONVERTMODE",
        "RESERVEPARA1",
        "RESERVEPARA2",
        "RESERVEPARA3",
        "RESERVEPARA4",
        "RTCPLOSTPKTHOCTRLPOLICY",
        "RTPJITTERTHDVAL",
        "RTPRTTTHDVAL",
        "RTPSNEXPANDOPTMODE",
        "RTPSNEXPANDOPTSW",
        "RTPSNINITIALTYPE",
        "RTPSTATOPTSW",
        "SELFHEALINGSWITCH",
        "SN",
        "SPLEVELLIMIT",
        "SRN",
        "SYNFRMWAITSWITCH",
        "TFOCNFFRMSENDMODE",
        "TFOFLOWCTRLTHREAD",
        "TFONEGOTIATEMSGTYPE",
        "TFOOPTSWITCH",
        "TIMEOUTRELTHD",
        "UPCMRCONTINUOUSSW",
        "VQEMODE"
    FROM
    huawei_nbi_gsm."TCPARA"

    """
)

TCRSVPARA = ReplaceableObject(
    'huawei_cm_2g."TCRSVPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TCRESERVEPARA1",
        "TCRESERVEPARA10",
        "TCRESERVEPARA11",
        "TCRESERVEPARA12",
        "TCRESERVEPARA13",
        "TCRESERVEPARA14",
        "TCRESERVEPARA2",
        "TCRESERVEPARA3",
        "TCRESERVEPARA4",
        "TCRESERVEPARA5",
        "TCRESERVEPARA6",
        "TCRESERVEPARA7",
        "TCRESERVEPARA8",
        "TCRESERVEPARA9"
    FROM
    huawei_nbi_gsm."TCRSVPARA"

    """
)

TNALMPARA = ReplaceableObject(
    'huawei_cm_2g."TNALMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALLOCTIMESPERPERIOD",
        "ALMCNTPERIOD",
        "ALMSWITCH",
        "FAULTTYPE",
        "KPIALMCLRTHD",
        "KPIALMTHD"
    FROM
    huawei_nbi_gsm."TNALMPARA"

    """
)

TNLOADBALANCEPARA = ReplaceableObject(
    'huawei_cm_2g."TNLOADBALANCEPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTLOADDIFFTH",
        "INTLOADSHARETH",
        "INTPINGLOSTPKTPRITH",
        "INTSRLOADCOMPENSATETH",
        "INTSRLOADHOPSCOMPENSATETH",
        "MPULOADDIFFTH",
        "MPULOADDIFFTIMETH",
        "MPULOADSHARETH"
    FROM
    huawei_nbi_gsm."TNLOADBALANCEPARA"

    """
)

TNRSVDPARA = ReplaceableObject(
    'huawei_cm_2g."TNRSVDPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "RSVDPARA3",
        "RSVDPARA4",
        "RSVDPARA5",
        "RSVDPARA6",
        "RSVDPARA7",
        "RSVDPARA8",
        "RSVDSW1",
        "RSVDSW2",
        "RSVDSW3"
    FROM
    huawei_nbi_gsm."TNRSVDPARA"

    """
)

TNSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."TNSOFTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ABISIPBALANCESWITCH",
        "ABISIPPREEMTOPTISW",
        "ABISMUXOPTISW",
        "ABISPATHFAULTPOLICY",
        "ABISUDPPINGFAULTPOLICY",
        "ACCANDCRFCSW",
        "ACREFCONGFCSW",
        "ADPCCONGFCSW",
        "APATHFAULTPOLICY",
        "ATERSLRELIABILITYSW",
        "AUTOFLOWSTATPKTINTRVL",
        "AUTOFLOWSTATSW",
        "CCCRRATIOTHRD",
        "CRMINNUM",
        "DIAGNOSESCTPFAULT",
        "DIPAGEDTIME",
        "DPUTOPTSCHKSW",
        "DSIDFLOWCTRLSWITCH",
        "EMERGENCYCALLADMITSW",
        "FCONITFBRD",
        "GLOBALALARMDELAYTIMER",
        "GLOBALALARMLOCPARASW",
        "INTBRDESTTHRD",
        "INTFCPERIOD",
        "INTFCTHRD",
        "IPPATHITFBOARDLOADSHARESW",
        "IURGPATHFAULTPOLICY",
        "LAPDAUTOTRACESWITCH",
        "LAPDDETECTBYERRPKGSW",
        "LAPDINTBRDPROTECTTIME",
        "LAPDOUTOFORDERPKTPROCPOL",
        "LAPDPORTPROTECTTIME",
        "LAPDRESUMEBYLOOP",
        "LINKRESELUNCONGDELAYTIMER",
        "M3UAFCSW",
        "M3UALOADOPTISW",
        "MAXCREFCONGFCLV",
        "MTP2RESUMESWITCH",
        "MTP3FCSW",
        "MTP3LOADOPTISW",
        "MTP3TXRATECONTROLSWITCH",
        "MTP3TXRATEFCSWITCH",
        "POOLIPPATHPINGFAULTALGOSW",
        "SCTPAUTOTRACESWITCH",
        "SCTPCONGCTRL",
        "SCTPPATHCHOVSW",
        "SCTPRECVFC",
        "SCTPRESUMEBYLOOP",
        "SCTPRWNDNONZEROSDSACKSW",
        "SCTPSENDFC",
        "SCTPSPAGINGTIME",
        "SCTPSPFCTHRD",
        "SCTPSPFILTERTIME",
        "SCTPSPPSFCTHRD",
        "SCTPSPPUNISHTIME",
        "SCTPSPUPTHRD",
        "SRCONPATHCHECKSW",
        "SRCONPATHCHECKSWITCH",
        "STORMCHECKSW",
        "TDMFLTDIAGSWITCH",
        "TDMINFTOPTSCHKSW",
        "TDMTSCONAUDITSW",
        "TNAPPDATAAUDITSWITCH"
    FROM
    huawei_nbi_gsm."TNSOFTPARA"

    """
)

TRANSPATCHPARA = ReplaceableObject(
    'huawei_cm_2g."TRANSPATCHPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "RSVDPARA1",
        "RSVDPARA10",
        "RSVDPARA11",
        "RSVDPARA12",
        "RSVDPARA13",
        "RSVDPARA14",
        "RSVDPARA15",
        "RSVDPARA2",
        "RSVDPARA3",
        "RSVDPARA4",
        "RSVDPARA5",
        "RSVDPARA6",
        "RSVDPARA7",
        "RSVDPARA8",
        "RSVDPARA9",
        "SRN"
    FROM
    huawei_nbi_gsm."TRANSPATCHPARA"

    """
)

TRANSPHYLNKPARA = ReplaceableObject(
    'huawei_cm_2g."TRANSPHYLNKPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTSTBYCONSCHKSW",
        "ARPDELAYAGINGSW",
        "AUTOTRCIPPKTCAPSW",
        "SIPMATCHDETECTSW",
        "TNUPORTTSCHKSW"
    FROM
    huawei_nbi_gsm."TRANSPHYLNKPARA"

    """
)

TRANSRSVPARA = ReplaceableObject(
    'huawei_cm_2g."TRANSRSVPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "RSVDPARA1",
        "RSVDPARA2",
        "RSVDPARA3",
        "RSVDPARA4",
        "RSVDPARA5",
        "RSVDPARA6",
        "RSVDSW1",
        "RSVDSW2",
        "RSVDSW3"
    FROM
    huawei_nbi_gsm."TRANSRSVPARA"

    """
)

TRCLOGSPD = ReplaceableObject(
    'huawei_cm_2g."TRCLOGSPD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TRCSPD"
    FROM
    huawei_nbi_gsm."TRCLOGSPD"

    """
)

TRMFACTOR = ReplaceableObject(
    'huawei_cm_2g."TRMFACTOR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSDATADL",
        "CSDATAUL",
        "CSVOICEDL",
        "CSVOICEUL",
        "FTI",
        "PSDATADL",
        "PSDATAUL",
        "REMARK"
    FROM
    huawei_nbi_gsm."TRMFACTOR"

    """
)

TRMLOADTH = ReplaceableObject(
    'huawei_cm_2g."TRMLOADTH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BWDCONGBW",
        "BWDCONGCLRBW",
        "BWDOVLDCLRRSVBW",
        "BWDOVLDRSVBW",
        "BWDRSVHOBW",
        "FWDCONGBW",
        "FWDCONGCLRBW",
        "FWDOVLDCLRRSVBW",
        "FWDOVLDRSVBW",
        "FWDRSVHOBW",
        "GSMCSBWRATE",
        "THTYPE",
        "TRANST",
        "TRMLOADTHINDEX",
        "BWDCONGCLRTH",
        "BWDCONGTH",
        "BWDOVLDCLRTH",
        "BWDOVLDTH",
        "BWDRESVHOTH",
        "FWDCONGCLRTH",
        "FWDCONGTH",
        "FWDOVLDCLRTH",
        "FWDOVLDTH",
        "FWDRESVHOTH",
        "TDMCONGCLRTH",
        "TDMCONGTH"
    FROM
    huawei_nbi_gsm."TRMLOADTH"

    """
)

TRMMAP = ReplaceableObject(
    'huawei_cm_2g."TRMMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSDATAPRI",
        "CSVOICEPRI",
        "ITFT",
        "PSHPRIDATAPRI",
        "PSLPRIDATAPRI",
        "REMARK",
        "TMI",
        "TRANST",
        "CSDATAPATH",
        "CSVOICEPATH",
        "PSHPRIDATAPATH",
        "PSLPRIDATAPATH"
    FROM
    huawei_nbi_gsm."TRMMAP"

    """
)

TRUSTCERT = ReplaceableObject(
    'huawei_cm_2g."TRUSTCERT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CERTNAME"
    FROM
    huawei_nbi_gsm."TRUSTCERT"

    """
)

TRXBIND2PHYBRD = ReplaceableObject(
    'huawei_cm_2g."TRXBIND2PHYBRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANTPASSNO",
        "BTSID",
        "CN",
        "SN",
        "SRN",
        "TRXID",
        "TRXPN",
        "TRXTP"
    FROM
    huawei_nbi_gsm."TRXBIND2PHYBRD"

    """
)

TZ = ReplaceableObject(
    'huawei_cm_2g."TZ"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CMETO",
        "DST",
        "EM",
        "EMONTH",
        "ET",
        "EWEEK",
        "EWSEQ",
        "SM",
        "SMONTH",
        "ST",
        "SWEEK",
        "SWSEQ",
        "ZONET"
    FROM
    huawei_nbi_gsm."TZ"

    """
)

UMTESTPARA = ReplaceableObject(
    'huawei_cm_2g."UMTESTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "UMTSTCELL",
        "UMTSTCHNNO",
        "UMTSTMSISDN",
        "UMTSTSITE",
        "UMTSTTRXID"
    FROM
    huawei_nbi_gsm."UMTESTPARA"

    """
)

USEREVTRTNPOLICY = ReplaceableObject(
    'huawei_cm_2g."USEREVTRTNPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CALLLOGDELPERIOD",
        "TRACEDELPERIOD"
    FROM
    huawei_nbi_gsm."USEREVTRTNPOLICY"

    """
)

USRRESBIND = ReplaceableObject(
    'huawei_cm_2g."USRRESBIND"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FIRSTUSERTYPE",
        "RESERVEDRESTYPE",
        "RESRESERVEDMINUTES",
        "SECONDUSERTYPE"
    FROM
    huawei_nbi_gsm."USRRESBIND"

    """
)

VLANID = ReplaceableObject(
    'huawei_cm_2g."VLANID"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPADDR",
        "SN",
        "SRN",
        "VLANID"
    FROM
    huawei_nbi_gsm."VLANID"

    """
)

WEBLOGINPOLICY = ReplaceableObject(
    'huawei_cm_2g."WEBLOGINPOLICY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "POLICY"
    FROM
    huawei_nbi_gsm."WEBLOGINPOLICY"

    """
)

XPUPORT = ReplaceableObject(
    'huawei_cm_2g."XPUPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PN",
        "PORTSWITCH",
        "SN",
        "SRN"
    FROM
    huawei_nbi_gsm."XPUPORT"

    """
)


def upgrade():
    op.create_view(AE1T1)
    op.create_view(AITFOTHPARA)
    op.create_view(AITFREV)
    op.create_view(ALGCTRLPARA)
    op.create_view(ALMBLKPARA)
    op.create_view(ALMBLKSW)
    op.create_view(ALMCAPACITY)
    op.create_view(ALMLVL)
    op.create_view(ALMML)
    op.create_view(ALMOSCISW)
    op.create_view(ALMOSCITHRD)
    op.create_view(ALMSCRN)
    op.create_view(ALMSHLD)
    op.create_view(APPCERT)
    op.create_view(ATESTPARA)
    op.create_view(BFDPROTOSW)
    op.create_view(BOXRPT)
    op.create_view(BRD)
    op.create_view(BSCAISS)
    op.create_view(BSCAITFTMR)
    op.create_view(BSCBASIC)
    op.create_view(BSCDSTPA)
    op.create_view(BSCEXSOFTPARA)
    op.create_view(BSCFCPARA)
    op.create_view(BSCJBF)
    op.create_view(BSCNSPARA)
    op.create_view(BSCPCUTYPE)
    op.create_view(BSCPSGBPARA)
    op.create_view(BSCPSSOFTPARA)
    op.create_view(BSCPSSTAT)
    op.create_view(BSCPSTCDSCPMAP)
    op.create_view(BSCPSUMPARA)
    op.create_view(BSCSIGTRC)
    op.create_view(BSCTESTPARA)
    op.create_view(BSCTMR)
    op.create_view(BSSGPPARA)
    op.create_view(BSSLS)
    op.create_view(BTS)
    op.create_view(BTSABISMUXFLOW)
    op.create_view(BTSABISPRIMAP)
    op.create_view(BTSABISTROP)
    op.create_view(BTSAISS)
    op.create_view(BTSALM)
    op.create_view(BTSALMFLASHTHD)
    op.create_view(BTSALMFLASHTW)
    op.create_view(BTSALMPORT)
    op.create_view(BTSAPMUBP)
    op.create_view(BTSAPPCERT)
    op.create_view(BTSAUTODLDACTINFO)
    op.create_view(BTSBAKPWR)
    op.create_view(BTSBBMODE)
    op.create_view(BTSBINDLOCGRP)
    op.create_view(BTSBRD)
    op.create_view(BTSBREAKPOINT)
    op.create_view(BTSBWPARA)
    op.create_view(BTSCABINET)
    op.create_view(BTSCELLPATCHPARA)
    op.create_view(BTSCERTCHKTSK)
    op.create_view(BTSCERTDEPLOY)
    op.create_view(BTSCERTMK)
    op.create_view(BTSCERTREQ)
    op.create_view(BTSCHNFALLBACK)
    op.create_view(BTSCLK)
    op.create_view(BTSCONNECT)
    op.create_view(BTSCPRIPORT)
    op.create_view(BTSCRC4)
    op.create_view(BTSCRLPOLICY)
    op.create_view(BTSCTRLEX)
    op.create_view(BTSCTRLLNK)
    op.create_view(BTSDEVIP)
    op.create_view(BTSDHCPSVRIP)
    op.create_view(BTSDHEUBP)
    op.create_view(BTSDSCPMAP)
    op.create_view(BTSE1T1BER)
    op.create_view(BTSEAMRC)
    op.create_view(BTSENVALMPORT)
    op.create_view(BTSEQUIPMENT)
    op.create_view(BTSESN)
    op.create_view(BTSETHOAM)
    op.create_view(BTSETHOAMAH)
    op.create_view(BTSETHPORT)
    op.create_view(BTSFALLBACK)
    op.create_view(BTSFLEXABISPARA)
    op.create_view(BTSFMUABP)
    op.create_view(BTSGTRANSPARA)
    op.create_view(BTSGUPWRSHRFP)
    op.create_view(BTSIDLETS)
    op.create_view(BTSIKECFG)
    op.create_view(BTSINTRXUSPEC)
    op.create_view(BTSIP)
    op.create_view(BTSIPCLKPARA)
    op.create_view(BTSIPGUARD)
    op.create_view(BTSIPRT)
    op.create_view(BTSJBF)
    op.create_view(BTSLAPDWS)
    op.create_view(BTSLLDPGLOBAL)
    op.create_view(BTSLNKBKATTR)
    op.create_view(BTSLOCGRP)
    op.create_view(BTSLOCKBCCH)
    op.create_view(BTSLR)
    op.create_view(BTSLSW)
    op.create_view(BTSMNTMODE)
    op.create_view(BTSMPGRP)
    op.create_view(BTSMPLNK)
    op.create_view(BTSOMLBACKUP)
    op.create_view(BTSOMLDETECT)
    op.create_view(BTSOMLTS)
    op.create_view(BTSOTHPARA)
    op.create_view(BTSPATCHPARA)
    op.create_view(BTSPINGSW)
    op.create_view(BTSPLRALM)
    op.create_view(BTSPSUFP)
    op.create_view(BTSRELIALOGSWITCH)
    op.create_view(BTSRET)
    op.create_view(BTSRETDEVICEDATA)
    op.create_view(BTSRETSUBUNIT)
    op.create_view(BTSRINGATTR)
    op.create_view(BTSRSV)
    op.create_view(BTSRXU2LOCGRP)
    op.create_view(BTSRXUBP)
    op.create_view(BTSRXUBRD)
    op.create_view(BTSRXUCHAIN)
    op.create_view(BTSSHARING)
    op.create_view(BTSTEMPLATERSC)
    op.create_view(BTSTHEFTALM)
    op.create_view(BTSTMA)
    op.create_view(BTSTMADEVICEDATA)
    op.create_view(BTSTMASUBUNIT)
    op.create_view(BTSTRANS)
    op.create_view(BTSTRCMPR)
    op.create_view(BTSTRUSTCERT)
    op.create_view(BTSTRXBACKUP)
    op.create_view(BTSVLAN)
    op.create_view(BTSXFC)
    op.create_view(BTSXMUFP)
    op.create_view(CAB)
    op.create_view(CCGN)
    op.create_view(CELLBIND2BTS)
    op.create_view(CELLGLDSS)
    op.create_view(CERTCHKTSK)
    op.create_view(CERTMK)
    op.create_view(CERTREQ)
    op.create_view(CLK)
    op.create_view(CLKMODE)
    op.create_view(CLKSRC)
    op.create_view(CONNTYPE)
    op.create_view(COPTLNK)
    op.create_view(CPUTHD)
    op.create_view(CRLPOLICY)
    op.create_view(CSPRECTRL)
    op.create_view(DEVIP)
    op.create_view(DEVRSVDPARA)
    op.create_view(DSCPMAP)
    op.create_view(DSP)
    op.create_view(DSPLVDSMODE)
    op.create_view(DXX)
    op.create_view(DXXCONNECT)
    op.create_view(DXXTSEXGRELATION)
    op.create_view(E1T1)
    op.create_view(EMSIP)
    op.create_view(ENVALMPARA)
    op.create_view(ETHIP)
    op.create_view(ETHPORT)
    op.create_view(ETHREDPORT)
    op.create_view(ETHSWITCH)
    op.create_view(FACFG)
    op.create_view(FANSPEED)
    op.create_view(FCCOMMPARA)
    op.create_view(filefooter)
    op.create_view(FTPCLTPORT)
    op.create_view(FTPSCLT)
    op.create_view(FTPSCLTDPORT)
    op.create_view(FTPSRVSPD)
    op.create_view(FTPSSRV)
    op.create_view(G2GNCELL)
    op.create_view(G3GARFCN)
    op.create_view(G3GNCELL)
    op.create_view(G_ADJMAP)
    op.create_view(G_ADJNODE)
    op.create_view(GAFCALMPARA)
    op.create_view(GALLCELLBLKSTAT)
    op.create_view(GBSCREDGRP)
    op.create_view(GCELL)
    op.create_view(GCELL2GBA1)
    op.create_view(GCELL3GARFCN)
    op.create_view(GCELLAMRQUL)
    op.create_view(GCELLBASICPARA)
    op.create_view(GCELLBTSSOFTPARA)
    op.create_view(GCELLCCACCESS)
    op.create_view(GCELLCCAD)
    op.create_view(GCELLCCAMR)
    op.create_view(GCELLCCBASIC)
    op.create_view(GCELLCCCH)
    op.create_view(GCELLCCTMR)
    op.create_view(GCELLCCUTRANSYS)
    op.create_view(GCELLCHMGAD)
    op.create_view(GCELLCHMGBASIC)
    op.create_view(GCELLCONGACALGO)
    op.create_view(GCELLCSFBPARA)
    op.create_view(GCELLDYNTURNOFF)
    op.create_view(GCELLEGPRSPARA)
    op.create_view(GCELLEXTMSRPARA)
    op.create_view(GCELLFREQ)
    op.create_view(GCELLFREQSCAN)
    op.create_view(GCELLGPRS)
    op.create_view(GCELLGSMR)
    op.create_view(GCELLHO2GBA2)
    op.create_view(GCELLHOAD)
    op.create_view(GCELLHOBASIC)
    op.create_view(GCELLHOCTRL)
    op.create_view(GCELLHOEDBPARA)
    op.create_view(GCELLHOEMG)
    op.create_view(GCELLHOFAST)
    op.create_view(GCELLHOFDDBA2)
    op.create_view(GCELLHOFITPEN)
    op.create_view(GCELLHOINTERRATLDB)
    op.create_view(GCELLHOIUO)
    op.create_view(GCELLHOPANT)
    op.create_view(GCELLHOPTP)
    op.create_view(GCELLHOTDDBA2)
    op.create_view(GCELLHOUTRANFDD)
    op.create_view(GCELLHOUTRANTDD)
    op.create_view(GCELLHSRPLCUSRIDFMG)
    op.create_view(GCELLIBCAII)
    op.create_view(GCELLIDLEAD)
    op.create_view(GCELLIDLEBASIC)
    op.create_view(GCELLIDLEFDDBA1)
    op.create_view(GCELLIDLETDDBA1)
    op.create_view(GCELLLCS)
    op.create_view(GCELLMAGRP)
    op.create_view(GCELLMAIOPLAN)
    op.create_view(GCELLMOCN)
    op.create_view(GCELLNC2PARA)
    op.create_view(GCELLNCRESELECTPARA)
    op.create_view(GCELLNONSTANDARDBW)
    op.create_view(GCELLNWCTRLMSRPARA)
    op.create_view(GCELLOPTREV)
    op.create_view(GCELLOSPMAP)
    op.create_view(GCELLOTHBASIC)
    op.create_view(GCELLOTHEXT)
    op.create_view(GCELLOTHPARA)
    op.create_view(GCELLPRACH)
    op.create_view(GCELLPRIEUTRANSYS)
    op.create_view(GCELLPRIVATEOPTPARA)
    op.create_view(GCELLPSABISPARA)
    op.create_view(GCELLPSBASE)
    op.create_view(GCELLPSCHM)
    op.create_view(GCELLPSCS)
    op.create_view(GCELLPSDIFFSERVICE)
    op.create_view(GCELLPSI1)
    op.create_view(GCELLPSOTHERPARA)
    op.create_view(GCELLPSPWPARA)
    op.create_view(GCELLPSSMALLPKTRESBAL)
    op.create_view(GCELLPWR2)
    op.create_view(GCELLPWR3)
    op.create_view(GCELLPWRBASIC)
    op.create_view(GCELLRESELECTPARA)
    op.create_view(GCELLRESELECTUTRANTDD)
    op.create_view(GCELLRESELUTRANFDD)
    op.create_view(GCELLRSVPARA)
    op.create_view(GCELLSBC)
    op.create_view(GCELLSERVPARA)
    op.create_view(GCELLSOFT)
    op.create_view(GCELLSON)
    op.create_view(GCELLSRVCC)
    op.create_view(GCELLSTANDARDOPTPARA)
    op.create_view(GCELLTA)
    op.create_view(GCELLTEMPLATERSC)
    op.create_view(GCELLTMR)
    op.create_view(GCELLTRANPARA)
    op.create_view(GCELLUNDPARA)
    op.create_view(GCELLVAMOS)
    op.create_view(GCELLVAMOSPWR)
    op.create_view(GCELLWLAN)
    op.create_view(GCNCFGALMTHD)
    op.create_view(GCNNODE)
    op.create_view(GCNOPERATOR)
    op.create_view(GCNOPERATORREV)
    op.create_view(GCSCHRCTRL)
    op.create_view(GCSCHRSCOPE)
    op.create_view(GCSFILE)
    op.create_view(GDSSPARA)
    op.create_view(GEXT2GCELL)
    op.create_view(GEXT3GCELL)
    op.create_view(GEXTLTECELL)
    op.create_view(GFORCESWITCH)
    op.create_view(GHOSTSTATUS)
    op.create_view(G_IPPATH)
    op.create_view(GKPIALMTHD)
    op.create_view(GLOBALROUTESW)
    op.create_view(GLTENCELL)
    op.create_view(GMRCTRL)
    op.create_view(GMRSCOPE)
    op.create_view(GNODEREDCFGCTRL)
    op.create_view(GNODEREDUNDANCY)
    op.create_view(GPSCHRCTRL)
    op.create_view(GPSCHRSCOPE)
    op.create_view(GPSKPIALMTHD)
    op.create_view(GREDGRPHOSTPOLICY)
    op.create_view(GRSVPARA)
    op.create_view(GTRX)
    op.create_view(GTRXBASE)
    op.create_view(GTRXCHAN)
    op.create_view(GTRXCHANHOP)
    op.create_view(GTRXDEV)
    op.create_view(GTRXFC)
    op.create_view(GTRXHOP)
    op.create_view(GTRXIUO)
    op.create_view(GTRXRLALM)
    op.create_view(GTRXRSVPARA)
    op.create_view(HOSTLOGSPD)
    op.create_view(IDRQTEST)
    op.create_view(INFBRDRESCFG)
    op.create_view(INTBRDPARA)
    op.create_view(IPCHK)
    op.create_view(IPGUARD)
    op.create_view(IPLOGICPORT)
    op.create_view(IPMUX)
    op.create_view(IPRT)
    op.create_view(ITWKPIALMTHD)
    op.create_view(L2L3ROUTEPOLICY)
    op.create_view(LDR)
    op.create_view(LICALMTHD)
    op.create_view(LICPOLICY)
    op.create_view(LODCTRL)
    op.create_view(LOGLIMIT)
    op.create_view(M3DE)
    op.create_view(M3LE)
    op.create_view(M3LKS)
    op.create_view(M3LNK)
    op.create_view(M3RT)
    op.create_view(MDTLCS)
    op.create_view(MNTMODE)
    op.create_view(MOCNPARA)
    op.create_view(MSGSOFTPARA)
    op.create_view(MSP)
    op.create_view(MTP3LKS)
    op.create_view(MTP3LNK)
    op.create_view(MTP3RT)
    op.create_view(MTP3TMR)
    op.create_view(N7DPC)
    op.create_view(NRIMSCMAP)
    op.create_view(NRISGSNMAP)
    op.create_view(NSE)
    op.create_view(NSVLLOCAL)
    op.create_view(OBJALMSHLD)
    op.create_view(OBJAUTHSW)
    op.create_view(OMUCOMMSVCSW)
    op.create_view(OMUETH)
    op.create_view(OMUPARA)
    op.create_view(OMUPORT)
    op.create_view(OPC)
    op.create_view(OPLOCK)
    op.create_view(OPSW)
    op.create_view(OPT)
    op.create_view(OSPWDPOLICY)
    op.create_view(OTHSOFTPARA)
    op.create_view(PACKETFILTERALMPARA)
    op.create_view(PHBMAP)
    op.create_view(PORTFLOWCTRLPARA)
    op.create_view(PORTOSCCTRLPARA)
    op.create_view(PSPREFABISCONGCTRL)
    op.create_view(PSUSRRESBIND)
    op.create_view(PTPBVC)
    op.create_view(PWDPOLICY)
    op.create_view(PWRALMSW)
    op.create_view(PWRPARA)
    op.create_view(QUEUEMAP)
    op.create_view(RSVRES)
    op.create_view(RULELIBVER)
    op.create_view(SAUCENTER)
    op.create_view(SCCPTMR)
    op.create_view(SCTPLNK)
    op.create_view(SCTPPROF)
    op.create_view(SCTPSRVPORT)
    op.create_view(SCUPORT)
    op.create_view(SGSN)
    op.create_view(SGSNNODE)
    op.create_view(SNTPCLTPARA)
    op.create_view(SNTPSRVINFO)
    op.create_view(SRCONPATH)
    op.create_view(SS7PATCHSWITCH)
    op.create_view(SSLAUTHMODE)
    op.create_view(SSLCONF)
    op.create_view(SSLCS)
    op.create_view(SUBNET)
    op.create_view(SUBRACK)
    op.create_view(SUBSESSION_NE)
    op.create_view(SYNSWITCH)
    op.create_view(SYS)
    op.create_view(TCPARA)
    op.create_view(TCRSVPARA)
    op.create_view(TNALMPARA)
    op.create_view(TNLOADBALANCEPARA)
    op.create_view(TNRSVDPARA)
    op.create_view(TNSOFTPARA)
    op.create_view(TRANSPATCHPARA)
    op.create_view(TRANSPHYLNKPARA)
    op.create_view(TRANSRSVPARA)
    op.create_view(TRCLOGSPD)
    op.create_view(TRMFACTOR)
    op.create_view(TRMLOADTH)
    op.create_view(TRMMAP)
    op.create_view(TRUSTCERT)
    op.create_view(TRXBIND2PHYBRD)
    op.create_view(TZ)
    op.create_view(UMTESTPARA)
    op.create_view(USEREVTRTNPOLICY)
    op.create_view(USRRESBIND)
    op.create_view(VLANID)
    op.create_view(WEBLOGINPOLICY)
    op.create_view(XPUPORT)


def downgrade():
    op.drop_view(AE1T1)
    op.drop_view(AITFOTHPARA)
    op.drop_view(AITFREV)
    op.drop_view(ALGCTRLPARA)
    op.drop_view(ALMBLKPARA)
    op.drop_view(ALMBLKSW)
    op.drop_view(ALMCAPACITY)
    op.drop_view(ALMLVL)
    op.drop_view(ALMML)
    op.drop_view(ALMOSCISW)
    op.drop_view(ALMOSCITHRD)
    op.drop_view(ALMSCRN)
    op.drop_view(ALMSHLD)
    op.drop_view(APPCERT)
    op.drop_view(ATESTPARA)
    op.drop_view(BFDPROTOSW)
    op.drop_view(BOXRPT)
    op.drop_view(BRD)
    op.drop_view(BSCAISS)
    op.drop_view(BSCAITFTMR)
    op.drop_view(BSCBASIC)
    op.drop_view(BSCDSTPA)
    op.drop_view(BSCEXSOFTPARA)
    op.drop_view(BSCFCPARA)
    op.drop_view(BSCJBF)
    op.drop_view(BSCNSPARA)
    op.drop_view(BSCPCUTYPE)
    op.drop_view(BSCPSGBPARA)
    op.drop_view(BSCPSSOFTPARA)
    op.drop_view(BSCPSSTAT)
    op.drop_view(BSCPSTCDSCPMAP)
    op.drop_view(BSCPSUMPARA)
    op.drop_view(BSCSIGTRC)
    op.drop_view(BSCTESTPARA)
    op.drop_view(BSCTMR)
    op.drop_view(BSSGPPARA)
    op.drop_view(BSSLS)
    op.drop_view(BTS)
    op.drop_view(BTSABISMUXFLOW)
    op.drop_view(BTSABISPRIMAP)
    op.drop_view(BTSABISTROP)
    op.drop_view(BTSAISS)
    op.drop_view(BTSALM)
    op.drop_view(BTSALMFLASHTHD)
    op.drop_view(BTSALMFLASHTW)
    op.drop_view(BTSALMPORT)
    op.drop_view(BTSAPMUBP)
    op.drop_view(BTSAPPCERT)
    op.drop_view(BTSAUTODLDACTINFO)
    op.drop_view(BTSBAKPWR)
    op.drop_view(BTSBBMODE)
    op.drop_view(BTSBINDLOCGRP)
    op.drop_view(BTSBRD)
    op.drop_view(BTSBREAKPOINT)
    op.drop_view(BTSBWPARA)
    op.drop_view(BTSCABINET)
    op.drop_view(BTSCELLPATCHPARA)
    op.drop_view(BTSCERTCHKTSK)
    op.drop_view(BTSCERTDEPLOY)
    op.drop_view(BTSCERTMK)
    op.drop_view(BTSCERTREQ)
    op.drop_view(BTSCHNFALLBACK)
    op.drop_view(BTSCLK)
    op.drop_view(BTSCONNECT)
    op.drop_view(BTSCPRIPORT)
    op.drop_view(BTSCRC4)
    op.drop_view(BTSCRLPOLICY)
    op.drop_view(BTSCTRLEX)
    op.drop_view(BTSCTRLLNK)
    op.drop_view(BTSDEVIP)
    op.drop_view(BTSDHCPSVRIP)
    op.drop_view(BTSDHEUBP)
    op.drop_view(BTSDSCPMAP)
    op.drop_view(BTSE1T1BER)
    op.drop_view(BTSEAMRC)
    op.drop_view(BTSENVALMPORT)
    op.drop_view(BTSEQUIPMENT)
    op.drop_view(BTSESN)
    op.drop_view(BTSETHOAM)
    op.drop_view(BTSETHOAMAH)
    op.drop_view(BTSETHPORT)
    op.drop_view(BTSFALLBACK)
    op.drop_view(BTSFLEXABISPARA)
    op.drop_view(BTSFMUABP)
    op.drop_view(BTSGTRANSPARA)
    op.drop_view(BTSGUPWRSHRFP)
    op.drop_view(BTSIDLETS)
    op.drop_view(BTSIKECFG)
    op.drop_view(BTSINTRXUSPEC)
    op.drop_view(BTSIP)
    op.drop_view(BTSIPCLKPARA)
    op.drop_view(BTSIPGUARD)
    op.drop_view(BTSIPRT)
    op.drop_view(BTSJBF)
    op.drop_view(BTSLAPDWS)
    op.drop_view(BTSLLDPGLOBAL)
    op.drop_view(BTSLNKBKATTR)
    op.drop_view(BTSLOCGRP)
    op.drop_view(BTSLOCKBCCH)
    op.drop_view(BTSLR)
    op.drop_view(BTSLSW)
    op.drop_view(BTSMNTMODE)
    op.drop_view(BTSMPGRP)
    op.drop_view(BTSMPLNK)
    op.drop_view(BTSOMLBACKUP)
    op.drop_view(BTSOMLDETECT)
    op.drop_view(BTSOMLTS)
    op.drop_view(BTSOTHPARA)
    op.drop_view(BTSPATCHPARA)
    op.drop_view(BTSPINGSW)
    op.drop_view(BTSPLRALM)
    op.drop_view(BTSPSUFP)
    op.drop_view(BTSRELIALOGSWITCH)
    op.drop_view(BTSRET)
    op.drop_view(BTSRETDEVICEDATA)
    op.drop_view(BTSRETSUBUNIT)
    op.drop_view(BTSRINGATTR)
    op.drop_view(BTSRSV)
    op.drop_view(BTSRXU2LOCGRP)
    op.drop_view(BTSRXUBP)
    op.drop_view(BTSRXUBRD)
    op.drop_view(BTSRXUCHAIN)
    op.drop_view(BTSSHARING)
    op.drop_view(BTSTEMPLATERSC)
    op.drop_view(BTSTHEFTALM)
    op.drop_view(BTSTMA)
    op.drop_view(BTSTMADEVICEDATA)
    op.drop_view(BTSTMASUBUNIT)
    op.drop_view(BTSTRANS)
    op.drop_view(BTSTRCMPR)
    op.drop_view(BTSTRUSTCERT)
    op.drop_view(BTSTRXBACKUP)
    op.drop_view(BTSVLAN)
    op.drop_view(BTSXFC)
    op.drop_view(BTSXMUFP)
    op.drop_view(CAB)
    op.drop_view(CCGN)
    op.drop_view(CELLBIND2BTS)
    op.drop_view(CELLGLDSS)
    op.drop_view(CERTCHKTSK)
    op.drop_view(CERTMK)
    op.drop_view(CERTREQ)
    op.drop_view(CLK)
    op.drop_view(CLKMODE)
    op.drop_view(CLKSRC)
    op.drop_view(CONNTYPE)
    op.drop_view(COPTLNK)
    op.drop_view(CPUTHD)
    op.drop_view(CRLPOLICY)
    op.drop_view(CSPRECTRL)
    op.drop_view(DEVIP)
    op.drop_view(DEVRSVDPARA)
    op.drop_view(DSCPMAP)
    op.drop_view(DSP)
    op.drop_view(DSPLVDSMODE)
    op.drop_view(DXX)
    op.drop_view(DXXCONNECT)
    op.drop_view(DXXTSEXGRELATION)
    op.drop_view(E1T1)
    op.drop_view(EMSIP)
    op.drop_view(ENVALMPARA)
    op.drop_view(ETHIP)
    op.drop_view(ETHPORT)
    op.drop_view(ETHREDPORT)
    op.drop_view(ETHSWITCH)
    op.drop_view(FACFG)
    op.drop_view(FANSPEED)
    op.drop_view(FCCOMMPARA)
    op.drop_view(filefooter)
    op.drop_view(FTPCLTPORT)
    op.drop_view(FTPSCLT)
    op.drop_view(FTPSCLTDPORT)
    op.drop_view(FTPSRVSPD)
    op.drop_view(FTPSSRV)
    op.drop_view(G2GNCELL)
    op.drop_view(G3GARFCN)
    op.drop_view(G3GNCELL)
    op.drop_view(G_ADJMAP)
    op.drop_view(G_ADJNODE)
    op.drop_view(GAFCALMPARA)
    op.drop_view(GALLCELLBLKSTAT)
    op.drop_view(GBSCREDGRP)
    op.drop_view(GCELL)
    op.drop_view(GCELL2GBA1)
    op.drop_view(GCELL3GARFCN)
    op.drop_view(GCELLAMRQUL)
    op.drop_view(GCELLBASICPARA)
    op.drop_view(GCELLBTSSOFTPARA)
    op.drop_view(GCELLCCACCESS)
    op.drop_view(GCELLCCAD)
    op.drop_view(GCELLCCAMR)
    op.drop_view(GCELLCCBASIC)
    op.drop_view(GCELLCCCH)
    op.drop_view(GCELLCCTMR)
    op.drop_view(GCELLCCUTRANSYS)
    op.drop_view(GCELLCHMGAD)
    op.drop_view(GCELLCHMGBASIC)
    op.drop_view(GCELLCONGACALGO)
    op.drop_view(GCELLCSFBPARA)
    op.drop_view(GCELLDYNTURNOFF)
    op.drop_view(GCELLEGPRSPARA)
    op.drop_view(GCELLEXTMSRPARA)
    op.drop_view(GCELLFREQ)
    op.drop_view(GCELLFREQSCAN)
    op.drop_view(GCELLGPRS)
    op.drop_view(GCELLGSMR)
    op.drop_view(GCELLHO2GBA2)
    op.drop_view(GCELLHOAD)
    op.drop_view(GCELLHOBASIC)
    op.drop_view(GCELLHOCTRL)
    op.drop_view(GCELLHOEDBPARA)
    op.drop_view(GCELLHOEMG)
    op.drop_view(GCELLHOFAST)
    op.drop_view(GCELLHOFDDBA2)
    op.drop_view(GCELLHOFITPEN)
    op.drop_view(GCELLHOINTERRATLDB)
    op.drop_view(GCELLHOIUO)
    op.drop_view(GCELLHOPANT)
    op.drop_view(GCELLHOPTP)
    op.drop_view(GCELLHOTDDBA2)
    op.drop_view(GCELLHOUTRANFDD)
    op.drop_view(GCELLHOUTRANTDD)
    op.drop_view(GCELLHSRPLCUSRIDFMG)
    op.drop_view(GCELLIBCAII)
    op.drop_view(GCELLIDLEAD)
    op.drop_view(GCELLIDLEBASIC)
    op.drop_view(GCELLIDLEFDDBA1)
    op.drop_view(GCELLIDLETDDBA1)
    op.drop_view(GCELLLCS)
    op.drop_view(GCELLMAGRP)
    op.drop_view(GCELLMAIOPLAN)
    op.drop_view(GCELLMOCN)
    op.drop_view(GCELLNC2PARA)
    op.drop_view(GCELLNCRESELECTPARA)
    op.drop_view(GCELLNONSTANDARDBW)
    op.drop_view(GCELLNWCTRLMSRPARA)
    op.drop_view(GCELLOPTREV)
    op.drop_view(GCELLOSPMAP)
    op.drop_view(GCELLOTHBASIC)
    op.drop_view(GCELLOTHEXT)
    op.drop_view(GCELLOTHPARA)
    op.drop_view(GCELLPRACH)
    op.drop_view(GCELLPRIEUTRANSYS)
    op.drop_view(GCELLPRIVATEOPTPARA)
    op.drop_view(GCELLPSABISPARA)
    op.drop_view(GCELLPSBASE)
    op.drop_view(GCELLPSCHM)
    op.drop_view(GCELLPSCS)
    op.drop_view(GCELLPSDIFFSERVICE)
    op.drop_view(GCELLPSI1)
    op.drop_view(GCELLPSOTHERPARA)
    op.drop_view(GCELLPSPWPARA)
    op.drop_view(GCELLPSSMALLPKTRESBAL)
    op.drop_view(GCELLPWR2)
    op.drop_view(GCELLPWR3)
    op.drop_view(GCELLPWRBASIC)
    op.drop_view(GCELLRESELECTPARA)
    op.drop_view(GCELLRESELECTUTRANTDD)
    op.drop_view(GCELLRESELUTRANFDD)
    op.drop_view(GCELLRSVPARA)
    op.drop_view(GCELLSBC)
    op.drop_view(GCELLSERVPARA)
    op.drop_view(GCELLSOFT)
    op.drop_view(GCELLSON)
    op.drop_view(GCELLSRVCC)
    op.drop_view(GCELLSTANDARDOPTPARA)
    op.drop_view(GCELLTA)
    op.drop_view(GCELLTEMPLATERSC)
    op.drop_view(GCELLTMR)
    op.drop_view(GCELLTRANPARA)
    op.drop_view(GCELLUNDPARA)
    op.drop_view(GCELLVAMOS)
    op.drop_view(GCELLVAMOSPWR)
    op.drop_view(GCELLWLAN)
    op.drop_view(GCNCFGALMTHD)
    op.drop_view(GCNNODE)
    op.drop_view(GCNOPERATOR)
    op.drop_view(GCNOPERATORREV)
    op.drop_view(GCSCHRCTRL)
    op.drop_view(GCSCHRSCOPE)
    op.drop_view(GCSFILE)
    op.drop_view(GDSSPARA)
    op.drop_view(GEXT2GCELL)
    op.drop_view(GEXT3GCELL)
    op.drop_view(GEXTLTECELL)
    op.drop_view(GFORCESWITCH)
    op.drop_view(GHOSTSTATUS)
    op.drop_view(G_IPPATH)
    op.drop_view(GKPIALMTHD)
    op.drop_view(GLOBALROUTESW)
    op.drop_view(GLTENCELL)
    op.drop_view(GMRCTRL)
    op.drop_view(GMRSCOPE)
    op.drop_view(GNODEREDCFGCTRL)
    op.drop_view(GNODEREDUNDANCY)
    op.drop_view(GPSCHRCTRL)
    op.drop_view(GPSCHRSCOPE)
    op.drop_view(GPSKPIALMTHD)
    op.drop_view(GREDGRPHOSTPOLICY)
    op.drop_view(GRSVPARA)
    op.drop_view(GTRX)
    op.drop_view(GTRXBASE)
    op.drop_view(GTRXCHAN)
    op.drop_view(GTRXCHANHOP)
    op.drop_view(GTRXDEV)
    op.drop_view(GTRXFC)
    op.drop_view(GTRXHOP)
    op.drop_view(GTRXIUO)
    op.drop_view(GTRXRLALM)
    op.drop_view(GTRXRSVPARA)
    op.drop_view(HOSTLOGSPD)
    op.drop_view(IDRQTEST)
    op.drop_view(INFBRDRESCFG)
    op.drop_view(INTBRDPARA)
    op.drop_view(IPCHK)
    op.drop_view(IPGUARD)
    op.drop_view(IPLOGICPORT)
    op.drop_view(IPMUX)
    op.drop_view(IPRT)
    op.drop_view(ITWKPIALMTHD)
    op.drop_view(L2L3ROUTEPOLICY)
    op.drop_view(LDR)
    op.drop_view(LICALMTHD)
    op.drop_view(LICPOLICY)
    op.drop_view(LODCTRL)
    op.drop_view(LOGLIMIT)
    op.drop_view(M3DE)
    op.drop_view(M3LE)
    op.drop_view(M3LKS)
    op.drop_view(M3LNK)
    op.drop_view(M3RT)
    op.drop_view(MDTLCS)
    op.drop_view(MNTMODE)
    op.drop_view(MOCNPARA)
    op.drop_view(MSGSOFTPARA)
    op.drop_view(MSP)
    op.drop_view(MTP3LKS)
    op.drop_view(MTP3LNK)
    op.drop_view(MTP3RT)
    op.drop_view(MTP3TMR)
    op.drop_view(N7DPC)
    op.drop_view(NRIMSCMAP)
    op.drop_view(NRISGSNMAP)
    op.drop_view(NSE)
    op.drop_view(NSVLLOCAL)
    op.drop_view(OBJALMSHLD)
    op.drop_view(OBJAUTHSW)
    op.drop_view(OMUCOMMSVCSW)
    op.drop_view(OMUETH)
    op.drop_view(OMUPARA)
    op.drop_view(OMUPORT)
    op.drop_view(OPC)
    op.drop_view(OPLOCK)
    op.drop_view(OPSW)
    op.drop_view(OPT)
    op.drop_view(OSPWDPOLICY)
    op.drop_view(OTHSOFTPARA)
    op.drop_view(PACKETFILTERALMPARA)
    op.drop_view(PHBMAP)
    op.drop_view(PORTFLOWCTRLPARA)
    op.drop_view(PORTOSCCTRLPARA)
    op.drop_view(PSPREFABISCONGCTRL)
    op.drop_view(PSUSRRESBIND)
    op.drop_view(PTPBVC)
    op.drop_view(PWDPOLICY)
    op.drop_view(PWRALMSW)
    op.drop_view(PWRPARA)
    op.drop_view(QUEUEMAP)
    op.drop_view(RSVRES)
    op.drop_view(RULELIBVER)
    op.drop_view(SAUCENTER)
    op.drop_view(SCCPTMR)
    op.drop_view(SCTPLNK)
    op.drop_view(SCTPPROF)
    op.drop_view(SCTPSRVPORT)
    op.drop_view(SCUPORT)
    op.drop_view(SGSN)
    op.drop_view(SGSNNODE)
    op.drop_view(SNTPCLTPARA)
    op.drop_view(SNTPSRVINFO)
    op.drop_view(SRCONPATH)
    op.drop_view(SS7PATCHSWITCH)
    op.drop_view(SSLAUTHMODE)
    op.drop_view(SSLCONF)
    op.drop_view(SSLCS)
    op.drop_view(SUBNET)
    op.drop_view(SUBRACK)
    op.drop_view(SUBSESSION_NE)
    op.drop_view(SYNSWITCH)
    op.drop_view(SYS)
    op.drop_view(TCPARA)
    op.drop_view(TCRSVPARA)
    op.drop_view(TNALMPARA)
    op.drop_view(TNLOADBALANCEPARA)
    op.drop_view(TNRSVDPARA)
    op.drop_view(TNSOFTPARA)
    op.drop_view(TRANSPATCHPARA)
    op.drop_view(TRANSPHYLNKPARA)
    op.drop_view(TRANSRSVPARA)
    op.drop_view(TRCLOGSPD)
    op.drop_view(TRMFACTOR)
    op.drop_view(TRMLOADTH)
    op.drop_view(TRMMAP)
    op.drop_view(TRUSTCERT)
    op.drop_view(TRXBIND2PHYBRD)
    op.drop_view(TZ)
    op.drop_view(UMTESTPARA)
    op.drop_view(USEREVTRTNPOLICY)
    op.drop_view(USRRESBIND)
    op.drop_view(VLANID)
    op.drop_view(WEBLOGINPOLICY)
    op.drop_view(XPUPORT)

