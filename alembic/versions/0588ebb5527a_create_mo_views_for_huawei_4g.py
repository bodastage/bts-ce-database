"""Create MO views for Huawei 4G

Revision ID: 0588ebb5527a
Revises: 316570e7ecab
Create Date: 2018-05-15 10:33:37.306000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0588ebb5527a'
down_revision = '316570e7ecab'
branch_labels = None
depends_on = None


class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


ALGODEFAULTPARA = ReplaceableObject(
    'huawei_cm_4g."ALGODEFAULTPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DEFDOPPLERLEVEL"
    FROM
    huawei_nbi_lte."ALGODEFAULTPARA"

    """
)

ANR = ReplaceableObject(
    'huawei_cm_4g."ANR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTIVEPCICONFLICTSWITCH",
        "ADDCELLTHD",
        "CAUECHOSEMODE",
        "DELCELLTHD",
        "EVENTANRMODE",
        "FASTANRCDMA1XRTTPILOTTHD",
        "FASTANRCDMAHRPDPILOTTHD",
        "FASTANRCHECKPERIOD",
        "FASTANRINTERRATMEASUENUM",
        "FASTANRINTERRATUENUMTHD",
        "FASTANRINTRARATMEASUENUM",
        "FASTANRINTRARATUENUMTHD",
        "FASTANRMODE",
        "FASTANRRPRTAMOUNT",
        "FASTANRRPRTINTERVAL",
        "FASTANRRSCPTHD",
        "FASTANRRSRPTHD",
        "FASTANRRSSITHD",
        "NCELLHOSTATNUM",
        "OPTMODE",
        "STARTTIME",
        "STATISTICNUMFORNRTDEL",
        "STATISTICPERIOD",
        "STATISTICPERIODFORNRTDEL",
        "STOPTIME"
    FROM
    huawei_nbi_lte."ANR"

    """
)

APPCERT = ReplaceableObject(
    'huawei_cm_4g."APPCERT"',
    """

    SELECT 
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
    huawei_nbi_lte."APPCERT"

    """
)

BASEBANDEQM = ReplaceableObject(
    'huawei_cm_4g."BASEBANDEQM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BASEBANDEQMID",
        "BASEBANDEQMTYPE",
        "UMTSDEMMODE"
    FROM
    huawei_nbi_lte."BASEBANDEQM"

    """
)

BASEBANDEQMBOARDREF = ReplaceableObject(
    'huawei_cm_4g."BASEBANDEQMBOARDREF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BASEBANDEQMID",
        "BASEBANDEQMTYPE",
        "CN",
        "SN",
        "SRN"
    FROM
    huawei_nbi_lte."BASEBANDEQMBOARDREF"

    """
)

BCCHCFG = ReplaceableObject(
    'huawei_cm_4g."BCCHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "MODIFYPERIODCOEFF"
    FROM
    huawei_nbi_lte."BCCHCFG"

    """
)

BFMIMOADAPTIVEPARACFG = ReplaceableObject(
    'huawei_cm_4g."BFMIMOADAPTIVEPARACFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BFMIMOADAPTIVESWITCH"
    FROM
    huawei_nbi_lte."BFMIMOADAPTIVEPARACFG"

    """
)

CAMGTCFG = ReplaceableObject(
    'huawei_cm_4g."CAMGTCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTIVEBUFFERDELAYTHD",
        "ACTIVEBUFFERLENTHD",
        "CARRAGGRA2THDRSRP",
        "CARRAGGRA4THDRSRP",
        "CARRIERMGTSWITCH",
        "DEACTIVEBUFFERLENTHD",
        "DEACTIVETHROUGHPUTTHD",
        "LOCALCELLID",
        "SCCCFGINTERVAL",
        "SCCDEACTCQITHD"
    FROM
    huawei_nbi_lte."CAMGTCFG"

    """
)

CELL = ReplaceableObject(
    'huawei_cm_4g."CELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADDITIONALSPECTRUMEMISSION",
        "AIRCELLFLAG",
        "CELLACTIVESTATE",
        "CELLADMINSTATE",
        "CELLID",
        "CELLNAME",
        "CELLRADIUS",
        "CELLSPECIFICOFFSET",
        "CNOPSHARINGGROUPID",
        "CPRICOMPRESSION",
        "CRSPORTNUM",
        "CSGIND",
        "CUSTOMIZEDBANDWIDTHCFGIND",
        "DLBANDWIDTH",
        "DLCYCLICPREFIX",
        "DLEARFCN",
        "EMERGENCYAREAIDCFGIND",
        "FDDTDDIND",
        "FREQBAND",
        "HIGHSPEEDFLAG",
        "LOCALCELLID",
        "MULTIRRUCELLFLAG",
        "PHYCELLID",
        "PREAMBLEFMT",
        "QOFFSETFREQ",
        "ROOTSEQUENCEIDX",
        "TXRXMODE",
        "UEPOWERMAX",
        "UEPOWERMAXCFGIND",
        "ULBANDWIDTH",
        "ULCYCLICPREFIX",
        "ULEARFCNCFGIND",
        "WORKMODE",
        "CUSTOMIZEDDLBANDWIDTH",
        "CUSTOMIZEDULBANDWIDTH"
    FROM
    huawei_nbi_lte."CELL"

    """
)

CELLACBAR = ReplaceableObject(
    'huawei_cm_4g."CELLACBAR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACBARRINGINFOCFGIND",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLACBAR"

    """
)

CELLACCESS = ReplaceableObject(
    'huawei_cm_4g."CELLACCESS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BROADCASTMODE",
        "CELLBARRED",
        "CELLRESERVEDEXT",
        "INTRAFREQRESEL",
        "LOCALCELLID",
        "REPTSYNCAVOIDIND",
        "REPTSYNCAVOIDTIME",
        "ROUNDPERIOD"
    FROM
    huawei_nbi_lte."CELLACCESS"

    """
)

CELLALGOSWITCH = ReplaceableObject(
    'huawei_cm_4g."CELLALGOSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACBARALGOSWITCH",
        "AQMALGOSWITCH",
        "AVOIDINTERFSWITCH",
        "BFALGOSWITCH",
        "CELLSCHSTRATEGYSWITCH",
        "COVBASEDINTERFREQHOMODE",
        "CQIADJALGOSWITCH",
        "DISTBASEDHOSWITCH",
        "DLCOMPSWITCH",
        "DLPCALGOSWITCH",
        "DLSCHSWITCH",
        "DYNADJVOLTSWITCH",
        "DYNDRXSWITCH",
        "DYNSPECTRUMSHARESWITCH",
        "EICICSWITCH",
        "ENHMIMOSWITCH",
        "FREQPRIORITYHOSWITCH",
        "GLPWRSHARE",
        "HIGHMOBITRIGIDLEMODESWITCH",
        "INTERFRANDSWITCH",
        "IRCSWITCH",
        "LOCALCELLID",
        "MLBALGOSWITCH",
        "MLBHOMODE",
        "MRCIRCADPTSWITCH",
        "MUBFALGOSWITCH",
        "MULTIFREQPRICONTROLSWITCH",
        "PRACHINTRFREJSWITCH",
        "PSICSWITCH",
        "PUCCHALGOSWITCH",
        "PUSCHIRCALGOSWITCH",
        "PUSCHMAXRBPUCCHADJSWITCH",
        "RACALGOSWITCH",
        "RACHALGOSWITCH",
        "RANSHAREMODESWITCH",
        "REPEATERSWITCH",
        "RESELECPRIADAPTSWITCH",
        "RLFDETECTALGOSWITCH",
        "SFNALGOSWITCH",
        "SFNDLSCHSWITCH",
        "SFNULSCHSWITCH",
        "SRSALGOSWITCH",
        "ULCOMPSWITCH",
        "ULPCALGOSWITCH",
        "ULSCHSWITCH",
        "UPLINKCOMPSWITCH"
    FROM
    huawei_nbi_lte."CELLALGOSWITCH"

    """
)

CELLBF = ReplaceableObject(
    'huawei_cm_4g."CELLBF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "MAXBFRANKPARA"
    FROM
    huawei_nbi_lte."CELLBF"

    """
)

CELLBFMIMOPARACFG = ReplaceableObject(
    'huawei_cm_4g."CELLBFMIMOPARACFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BFMIMOADAPTIVESWITCH",
        "BFMIMOADAPWITHOUTTM2",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLBFMIMOPARACFG"

    """
)

CELLCHPWRCFG = ReplaceableObject(
    'huawei_cm_4g."CELLCHPWRCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DBCHPWR",
        "LOCALCELLID",
        "PBCHPWR",
        "PCFICHPWR",
        "PCHPWR",
        "PRSPWR",
        "RARSPPWR",
        "SCHPWR"
    FROM
    huawei_nbi_lte."CELLCHPWRCFG"

    """
)

CELLCSPCPARA = ReplaceableObject(
    'huawei_cm_4g."CELLCSPCPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLCSPCSWITCH",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLCSPCPARA"

    """
)

CELLDLCOMPALGO = ReplaceableObject(
    'huawei_cm_4g."CELLDLCOMPALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DLCOMPA3OFFSET",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLDLCOMPALGO"

    """
)

CELLDLICIC = ReplaceableObject(
    'huawei_cm_4g."CELLDLICIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BANDMODE",
        "DLICICNOISEUSERRSRPTHD",
        "DLICICUSERATTRGFACTORTHD",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLDLICIC"

    """
)

CELLDLICICMCPARA = ReplaceableObject(
    'huawei_cm_4g."CELLDLICICMCPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "A3OFFSET",
        "A6OFFSET",
        "HYSTERESIS",
        "LOCALCELLID",
        "MAXREPORTCELLNUM",
        "REPORTAMOUNT",
        "REPORTINTERVAL",
        "REPORTQUANTITY",
        "TIMETOTRIGGER",
        "TRIGGERQUANTITY"
    FROM
    huawei_nbi_lte."CELLDLICICMCPARA"

    """
)

CELLDLPCPDCCH = ReplaceableObject(
    'huawei_cm_4g."CELLDLPCPDCCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DEDIDCIPWROFFSET",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLDLPCPDCCH"

    """
)

CELLDLPCPDSCH = ReplaceableObject(
    'huawei_cm_4g."CELLDLPCPDSCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CCUPA",
        "CEUPA",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLDLPCPDSCH"

    """
)

CELLDLPCPDSCHPA = ReplaceableObject(
    'huawei_cm_4g."CELLDLPCPDSCHPA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "PAPCOFF",
        "PDSCHPAADJSWITCH"
    FROM
    huawei_nbi_lte."CELLDLPCPDSCHPA"

    """
)

CELLDLPCPHICH = ReplaceableObject(
    'huawei_cm_4g."CELLDLPCPHICH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "PWROFFSET"
    FROM
    huawei_nbi_lte."CELLDLPCPHICH"

    """
)

CELLDLSCHALGO = ReplaceableObject(
    'huawei_cm_4g."CELLDLSCHALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BTSERVICEWEIGHT",
        "CASCCDOPMEAS",
        "CASCHSTRATEGY",
        "CELLEDGEUSERRBALLOCMODE",
        "DATATHDINPDCCHPDSCHBAL",
        "DLEPFCAPACITYFACTOR",
        "DLICICSCHMODE",
        "DLRANKDETECTSWITCH",
        "DLRANKOPTIMIZESWITCH",
        "DLSCHABNUETHD",
        "DLSCHSTRATEGY",
        "ENBINTERFRANDMOD",
        "FREEUSERDLRBUSEDRATIO",
        "LOCALCELLID",
        "MAXMIMORANKPARA",
        "NONGBRRESOURCERATIO",
        "OTHERSERVICEWEIGHT",
        "RARANDPAGINGCR",
        "RBGALLOCSTRATEGY",
        "RBPRIMCSSELECTRATIOTHD",
        "RBPRIMCSSELECTSTRATEGY",
        "TDDSPECSUBFSCHSWITCH",
        "UENUMTHDINPDCCHPDSCHBAL"
    FROM
    huawei_nbi_lte."CELLDLSCHALGO"

    """
)

CELLDRXPARA = ReplaceableObject(
    'huawei_cm_4g."CELLDRXPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CQIMASK",
        "DATAAMOUNTSTATTIMER",
        "DRXINACTIVITYTIMERUNSYNC",
        "DRXPOLICYMODE",
        "FDDENTERDRXTHD",
        "FDDEXITDRXTHD",
        "LOCALCELLID",
        "LONGDRXCYCLEUNSYNC",
        "ONDURATIONTIMERUNSYNC",
        "TDDENTERDRXTHDDL",
        "TDDENTERDRXTHDUL",
        "TDDEXITDRXTHDDL",
        "TDDEXITDRXTHDUL",
        "TDDPOWERSAVEMEASSWITCH"
    FROM
    huawei_nbi_lte."CELLDRXPARA"

    """
)

CELLDSS = ReplaceableObject(
    'huawei_cm_4g."CELLDSS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "A3OFFSET",
        "A6OFFSET",
        "FARAREASINRTHD",
        "HIGHFREQSHARERBNUM",
        "LOCALCELLID",
        "LOWFREQSHARERBNUM",
        "MIDDLEAREASINRTHD",
        "NEARAREASINRTHD"
    FROM
    huawei_nbi_lte."CELLDSS"

    """
)

CELLDYNACBARALGOPARA = ReplaceableObject(
    'huawei_cm_4g."CELLDYNACBARALGOPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DYNACBARCANCELTHD",
        "DYNACBARSTATPERIOD",
        "DYNACBARTRIGGERTHD",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLDYNACBARALGOPARA"

    """
)

CELLHOPARACFG = ReplaceableObject(
    'huawei_cm_4g."CELLHOPARACFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHOA1A2THDRSRP",
        "BLINDHOA1A2THDRSRQ",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLHOPARACFG"

    """
)

CELLIDPRDUPT = ReplaceableObject(
    'huawei_cm_4g."CELLIDPRDUPT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTIONTIME",
        "PERIOD",
        "PRDUPTSWITCH"
    FROM
    huawei_nbi_lte."CELLIDPRDUPT"

    """
)

CELLLOWPOWER = ReplaceableObject(
    'huawei_cm_4g."CELLLOWPOWER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLUSEDPWRRATIO",
        "CELLUSEDPWRREDUCETIMELEN",
        "ENTERTIMELEN",
        "LOCALCELLID",
        "LOWPWRSWITCH",
        "RFSHUTDOWNTIMELEN",
        "RSPWRADJOFFSET",
        "RSPWRREDUCETIMELEN"
    FROM
    huawei_nbi_lte."CELLLOWPOWER"

    """
)

CELLMBMSCFG = ReplaceableObject(
    'huawei_cm_4g."CELLMBMSCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "MBMSSWITCH"
    FROM
    huawei_nbi_lte."CELLMBMSCFG"

    """
)

CELLMCPARA = ReplaceableObject(
    'huawei_cm_4g."CELLMCPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "A3OFFSET",
        "A6OFFSET",
        "HYSTERESIS",
        "LOCALCELLID",
        "MAXREPORTCELLS",
        "REPORTAMOUNT",
        "REPORTINTERVAL",
        "REPORTQUANTITY",
        "TIMETOTRIGGER",
        "TRIGGERQUANTITY"
    FROM
    huawei_nbi_lte."CELLMCPARA"

    """
)

CELLMIMOPARACFG = ReplaceableObject(
    'huawei_cm_4g."CELLMIMOPARACFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INITIALMIMOTYPE",
        "LOCALCELLID",
        "MIMOADAPTIVESWITCH"
    FROM
    huawei_nbi_lte."CELLMIMOPARACFG"

    """
)

CELLMLB = ReplaceableObject(
    'huawei_cm_4g."CELLMLB"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DLDATAMLBMODE",
        "FREQSELECTSTRATEGY",
        "HOTSPOTUEMODE",
        "IDLEUESELFREQSCOPE",
        "INITVALIDPERIOD",
        "INTERFREQIDLEMLBMODE",
        "INTERFREQMLBTHD",
        "INTERFREQMLBUENUMTHD",
        "INTERRATMLBTHD",
        "INTERRATMLBUENUMTHD",
        "INTERRATMLBUESELSTRATEGY",
        "INTRAFREQMLBTHD",
        "LOADDIFFTHD",
        "LOADEXCHANGEPERIOD",
        "LOADOFFSET",
        "LOADTRANSFERFACTOR",
        "LOCALCELLID",
        "MLBMAXUENUM",
        "MLBMINUENUMOFFSET",
        "MLBMINUENUMTHD",
        "MLBTRIGGERMODE",
        "MLBUENUMOFFSET",
        "MLBUESELECTPRBTHD",
        "PRBLOADCALCMETHOD"
    FROM
    huawei_nbi_lte."CELLMLB"

    """
)

CELLMLBHO = ReplaceableObject(
    'huawei_cm_4g."CELLMLBHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IDLEUESELFREQSTRATEGY",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLMLBHO"

    """
)

CELLMRO = ReplaceableObject(
    'huawei_cm_4g."CELLMRO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CIOADJLIMITCFGIND",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLMRO"

    """
)

CELLNOACCESSALMPARA = ReplaceableObject(
    'huawei_cm_4g."CELLNOACCESSALMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "NOACCESSDETECTTIMER",
        "NOACCESSSTARTDETECTTIME",
        "NOACCESSSTOPDETECTTIME"
    FROM
    huawei_nbi_lte."CELLNOACCESSALMPARA"

    """
)

CELLOP = ReplaceableObject(
    'huawei_cm_4g."CELLOP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLRESERVEDFOROP",
        "LOCALCELLID",
        "OPDLRBUSEDRATIO",
        "OPUENUMRATIO",
        "OPULRBUSEDRATIO",
        "TRACKINGAREAID"
    FROM
    huawei_nbi_lte."CELLOP"

    """
)

CELLPCALGO = ReplaceableObject(
    'huawei_cm_4g."CELLPCALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "PUCCHCLOSELOOPPCTYPE",
        "SRSPCSTRATEGY"
    FROM
    huawei_nbi_lte."CELLPCALGO"

    """
)

CELLPDCCHALGO = ReplaceableObject(
    'huawei_cm_4g."CELLPDCCHALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CCERATIOADJSWITCH",
        "CCEUSERATIO",
        "COMSIGCONGREGLV",
        "INITPDCCHSYMNUM",
        "LOCALCELLID",
        "PDCCHAGGLVLCLADJUSTSWITCH",
        "PDCCHSYMNUMSWITCH",
        "SFNPDCCHDCSTHD",
        "VIRTUALLOADPRO"
    FROM
    huawei_nbi_lte."CELLPDCCHALGO"

    """
)

CELLPUCCHALGO = ReplaceableObject(
    'huawei_cm_4g."CELLPUCCHALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "SRILOWLOADTHD"
    FROM
    huawei_nbi_lte."CELLPUCCHALGO"

    """
)

CELLRACHALGO = ReplaceableObject(
    'huawei_cm_4g."CELLRACHALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "PRACHFALSEALARMDETRADTHD"
    FROM
    huawei_nbi_lte."CELLRACHALGO"

    """
)

CELLRACTHD = ReplaceableObject(
    'huawei_cm_4g."CELLRACTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACRESERVEDUSERNUMBER",
        "CONGRELOFFSET",
        "COPPERGBRCONGPROPORTION",
        "DLRBHIGHTHD",
        "DLRBLOWTHD",
        "GBRRBUSEDHIGHTHD",
        "GBRRBUSEDLOWTHD",
        "GOLDGBRCONGPROPORTION",
        "GOLDSERVICEARPTHD",
        "LDCMEAARPTHD",
        "LOCALCELLID",
        "MAXNONGBRBEARERNUM",
        "NEWCOPPERSERVICEOFFSET",
        "NEWGOLDSERVICEOFFSET",
        "NEWSILVERSERVICEOFFSET",
        "PREEMPTIONARPTHD",
        "QCI1CONGTHD",
        "QCI1HOTHD",
        "QCI2CONGTHD",
        "QCI2HOTHD",
        "QCI3CONGTHD",
        "QCI3HOTHD",
        "QCI4CONGTHD",
        "QCI4HOTHD",
        "SILVERGBRCONGPROPORTION",
        "SILVERSERVICEARPTHD",
        "ULRBHIGHTHD",
        "ULRBLOWTHD"
    FROM
    huawei_nbi_lte."CELLRACTHD"

    """
)

CELLRESEL = ReplaceableObject(
    'huawei_cm_4g."CELLRESEL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLRESELPRIORITY",
        "LOCALCELLID",
        "MEASBANDWIDTH",
        "MEASBANDWIDTHCFGIND",
        "NEIGHCELLCONFIG",
        "PMAXCFGIND",
        "PRESENCEANTENNAPORT1",
        "QHYST",
        "QQUALMIN",
        "QQUALMINCFGIND",
        "QRXLEVMIN",
        "SINTRASEARCH",
        "SINTRASEARCHCFGIND",
        "SINTRASEARCHQ",
        "SNONINTRASEARCH",
        "SNONINTRASEARCHCFGIND",
        "SNONINTRASEARCHQ",
        "SPEEDDEPRESELCFGIND",
        "SPEEDSTATESFCFGIND",
        "THRSHSERVLOW",
        "THRSHSERVLOWQCFGIND",
        "TRESELEUTRAN",
        "TRESELEUTRANSFHIGH",
        "TRESELEUTRANSFMEDIUM",
        "NCELLCHANGEHIGH",
        "NCELLCHANGEMEDIUM",
        "QHYSTSFHIGH",
        "QHYSTSFMEDIUM",
        "TEVALUATION",
        "THYSTNORMAL"
    FROM
    huawei_nbi_lte."CELLRESEL"

    """
)

CELLRESELGERAN = ReplaceableObject(
    'huawei_cm_4g."CELLRESELGERAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "SPEEDSTATESFCFGIND",
        "TRESELGERAN"
    FROM
    huawei_nbi_lte."CELLRESELGERAN"

    """
)

CELLRESELUTRAN = ReplaceableObject(
    'huawei_cm_4g."CELLRESELUTRAN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "SPEEDSTATESFCFGIND",
        "TRESELUTRAN"
    FROM
    huawei_nbi_lte."CELLRESELUTRAN"

    """
)

CELLRFSHUTDOWN = ReplaceableObject(
    'huawei_cm_4g."CELLRFSHUTDOWN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "RFSHUTDOWNSWITCH",
        "RSPWRADJOFFSET",
        "STARTTIME",
        "STOPTIME"
    FROM
    huawei_nbi_lte."CELLRFSHUTDOWN"

    """
)

CELLRICALGO = ReplaceableObject(
    'huawei_cm_4g."CELLRICALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "MUTEULSYM",
        "MUTEUPPTSSYMNUM",
        "RICALGOSWITCH"
    FROM
    huawei_nbi_lte."CELLRICALGO"

    """
)

CELLSEL = ReplaceableObject(
    'huawei_cm_4g."CELLSEL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "QQUALMIN",
        "QQUALMINOFFSETCFGIND",
        "QRXLEVMIN",
        "QRXLEVMINOFFSET"
    FROM
    huawei_nbi_lte."CELLSEL"

    """
)

CELLSERVICEDIFFCFG = ReplaceableObject(
    'huawei_cm_4g."CELLSERVICEDIFFCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "QUEUESERVICEWEIGHT0",
        "QUEUESERVICEWEIGHT1",
        "QUEUESERVICEWEIGHT2",
        "QUEUESERVICEWEIGHT3",
        "QUEUESERVICEWEIGHT4",
        "QUEUESERVICEWEIGHT5",
        "QUEUESERVICEWEIGHT6",
        "SERVICEDIFFSWITCH"
    FROM
    huawei_nbi_lte."CELLSERVICEDIFFCFG"

    """
)

CELLSHUTDOWN = ReplaceableObject(
    'huawei_cm_4g."CELLSHUTDOWN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLSHUTDOWNSWITCH",
        "DLPRBOFFSET",
        "DLPRBTHD",
        "LOCALCELLID",
        "STARTTIME",
        "STOPTIME",
        "ULPRBOFFSET",
        "ULPRBTHD"
    FROM
    huawei_nbi_lte."CELLSHUTDOWN"

    """
)

CELLSIMAP = ReplaceableObject(
    'huawei_cm_4g."CELLSIMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ETWSPNDURATION",
        "ETWSPNOVERLAPPOLICY",
        "ETWSSNOVERLAPPOLICY",
        "LOCALCELLID",
        "SIB10PERIOD",
        "SIB11PERIOD",
        "SIB2PERIOD",
        "SIB3PERIOD",
        "SIB4PERIOD",
        "SIB5PERIOD",
        "SIB6PERIOD",
        "SIB7PERIOD",
        "SIB8PERIOD",
        "SIMAPSWITCH"
    FROM
    huawei_nbi_lte."CELLSIMAP"

    """
)

CELLSTANDARDQCI = ReplaceableObject(
    'huawei_cm_4g."CELLSTANDARDQCI"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DRXPARAGROUPID",
        "INTERFREQHOGROUPID",
        "INTERRATHOCDMA1XRTTGROUPID",
        "INTERRATHOCDMAHRPDGROUPID",
        "INTERRATHOCOMMGROUPID",
        "INTERRATHOGERANGROUPID",
        "INTERRATHOUTRANGROUPID",
        "INTRAFREQHOGROUPID",
        "LOCALCELLID",
        "PREALLOCATIONPARAGROUPID",
        "QCI",
        "QCIPRIORITYFORDRX",
        "RLFTIMERCONSTCFGIND",
        "SRIPERIOD",
        "TRAFFICRELDELAY",
        "MLBQCIGROUPID"
    FROM
    huawei_nbi_lte."CELLSTANDARDQCI"

    """
)

CELLULCOMPALGO = ReplaceableObject(
    'huawei_cm_4g."CELLULCOMPALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "ULCOMPA3OFFSET"
    FROM
    huawei_nbi_lte."CELLULCOMPALGO"

    """
)

CELLULICIC = ReplaceableObject(
    'huawei_cm_4g."CELLULICIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BANDMODE",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CELLULICIC"

    """
)

CELLULICICMCPARA = ReplaceableObject(
    'huawei_cm_4g."CELLULICICMCPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "A3OFFSET",
        "HYSTERESIS",
        "LOCALCELLID",
        "MAXREPORTCELLNUM",
        "REPORTAMOUNT",
        "REPORTINTERVAL",
        "REPORTQUANTITY",
        "TIMETOTRIGGER",
        "TRIGGERQUANTITY"
    FROM
    huawei_nbi_lte."CELLULICICMCPARA"

    """
)

CELLULPCCOMM = ReplaceableObject(
    'huawei_cm_4g."CELLULPCCOMM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DELTAFPUCCHFORMAT1",
        "DELTAFPUCCHFORMAT1B",
        "DELTAFPUCCHFORMAT2",
        "DELTAFPUCCHFORMAT2A",
        "DELTAFPUCCHFORMAT2B",
        "DELTAPREAMBLEMSG3",
        "LOCALCELLID",
        "P0NOMINALPUCCH",
        "P0NOMINALPUSCH",
        "PASSLOSSCOEFF"
    FROM
    huawei_nbi_lte."CELLULPCCOMM"

    """
)

CELLULPCDEDIC = ReplaceableObject(
    'huawei_cm_4g."CELLULPCDEDIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DELTAMCSENABLED",
        "FILTERRSRP",
        "LOCALCELLID",
        "PSRSOFFSETDELTAMCSDISABLE",
        "PSRSOFFSETDELTAMCSENABLE"
    FROM
    huawei_nbi_lte."CELLULPCDEDIC"

    """
)

CELLULSCHALGO = ReplaceableObject(
    'huawei_cm_4g."CELLULSCHALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADAPTHARQSWITCH",
        "FREEUSERULRBUSEDRATIO",
        "LOCALCELLID",
        "PREALLOCATIONBANDWIDTHRATIO",
        "PREALLOCATIONMINPERIOD",
        "PREALLOCATIONSIZE",
        "SINRADJUSTTARGETIBLER",
        "SMARTPREALLOCATIONDURATION",
        "SMARTPREALLOCDURAFORSPARSE",
        "SPSRELTHD",
        "SRIFALSEDETTHDSWITCH",
        "ULDELAYSCHSTRATEGY",
        "ULEPFCAPACITYFACTOR",
        "ULHOPPINGTYPE",
        "ULRBALLOCATIONSTRATEGY",
        "ULSCHABNUETHD",
        "ULSCHSTRATEGY",
        "ULSRSCHDATELEN"
    FROM
    huawei_nbi_lte."CELLULSCHALGO"

    """
)

CERTCHKTSK = ReplaceableObject(
    'huawei_cm_4g."CERTCHKTSK"',
    """

    SELECT 
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
    huawei_nbi_lte."CERTCHKTSK"

    """
)

CERTDEPLOY = ReplaceableObject(
    'huawei_cm_4g."CERTDEPLOY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DEPLOYTYPE"
    FROM
    huawei_nbi_lte."CERTDEPLOY"

    """
)

CERTMK = ReplaceableObject(
    'huawei_cm_4g."CERTMK"',
    """

    SELECT 
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
    huawei_nbi_lte."CERTMK"

    """
)

CERTREQ = ReplaceableObject(
    'huawei_cm_4g."CERTREQ"',
    """

    SELECT 
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
        "SIGNALG",
        "USERADDINFO"
    FROM
    huawei_nbi_lte."CERTREQ"

    """
)

CNOPERATOR = ReplaceableObject(
    'huawei_cm_4g."CNOPERATOR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "CNOPERATORNAME",
        "CNOPERATORTYPE",
        "MCC",
        "MNC"
    FROM
    huawei_nbi_lte."CNOPERATOR"

    """
)

CNOPERATORHOCFG = ReplaceableObject(
    'huawei_cm_4g."CNOPERATORHOCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "FDDIFHOA2THDRSRPOFFSET",
        "FIRSTRATPRI",
        "GERANA2THDRSRPOFFSET",
        "SECONDRATPRI",
        "UTRANA2THDRSRPOFFSET"
    FROM
    huawei_nbi_lte."CNOPERATORHOCFG"

    """
)

CNOPERATORIPPATH = ReplaceableObject(
    'huawei_cm_4g."CNOPERATORIPPATH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "IPPATHID"
    FROM
    huawei_nbi_lte."CNOPERATORIPPATH"

    """
)

CNOPERATORSTANDARDQCI = ReplaceableObject(
    'huawei_cm_4g."CNOPERATORSTANDARDQCI"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "QCI",
        "SERVICEHOBEARERPOLICY",
        "SERVICEIFHOCFGGROUPID",
        "SERVICEIRHOCFGGROUPID"
    FROM
    huawei_nbi_lte."CNOPERATORSTANDARDQCI"

    """
)

CNOPERATORTA = ReplaceableObject(
    'huawei_cm_4g."CNOPERATORTA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "TAC",
        "TRACKINGAREAID"
    FROM
    huawei_nbi_lte."CNOPERATORTA"

    """
)

COUNTERCHECKPARA = ReplaceableObject(
    'huawei_cm_4g."COUNTERCHECKPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COUNTERCHECKCOUNTNUM",
        "COUNTERCHECKTIMER",
        "COUNTERCHECKUSERRELSWITCH"
    FROM
    huawei_nbi_lte."COUNTERCHECKPARA"

    """
)

CPBEARER = ReplaceableObject(
    'huawei_cm_4g."CPBEARER"',
    """

    SELECT 
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
        "CPBEARID",
        "FLAG",
        "LINKNO"
    FROM
    huawei_nbi_lte."CPBEARER"

    """
)

CQIADAPTIVECFG = ReplaceableObject(
    'huawei_cm_4g."CQIADAPTIVECFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CQIPERIODADAPTIVE",
        "HOAPERIODICCQICFGSWITCH",
        "PUCCHPERIODICCQIOPTSWITCH"
    FROM
    huawei_nbi_lte."CQIADAPTIVECFG"

    """
)

CRLPOLICY = ReplaceableObject(
    'huawei_cm_4g."CRLPOLICY"',
    """

    SELECT 
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
    huawei_nbi_lte."CRLPOLICY"

    """
)

CSFALLBACKBLINDHOCFG = ReplaceableObject(
    'huawei_cm_4g."CSFALLBACKBLINDHOCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CDMALCSCAP",
        "CNOPERATORID",
        "GERANLCSCAP",
        "IDLECSFBHIGHESTPRI",
        "IDLECSFBLOWESTPRI",
        "IDLECSFBSECONDPRI",
        "INTERRATHIGHESTPRI",
        "INTERRATLOWESTPRI",
        "INTERRATSECONDPRI",
        "UTRANLCSCAP"
    FROM
    huawei_nbi_lte."CSFALLBACKBLINDHOCFG"

    """
)

CSFALLBACKHO = ReplaceableObject(
    'huawei_cm_4g."CSFALLBACKHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHOA1THDRSRP",
        "CSFBHOCDMAB1THDPS",
        "CSFBHOCDMATIMETOTRIG",
        "CSFBHOGERANB1THD",
        "CSFBHOGERANTIMETOTRIG",
        "CSFBHOUTRANB1THDECN0",
        "CSFBHOUTRANB1THDRSCP",
        "CSFBHOUTRANTIMETOTRIG",
        "CSFBPROTECTIONTIMER",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."CSFALLBACKHO"

    """
)

CSFALLBACKPOLICYCFG = ReplaceableObject(
    'huawei_cm_4g."CSFALLBACKPOLICYCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSFBHOPOLICYCFG",
        "CSFBUSERARPCFGSWITCH",
        "IDLEMODECSFBHOPOLICYCFG"
    FROM
    huawei_nbi_lte."CSFALLBACKPOLICYCFG"

    """
)

CSPCALGOPARA = ReplaceableObject(
    'huawei_cm_4g."CSPCALGOPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSPCALGOSWITCH"
    FROM
    huawei_nbi_lte."CSPCALGOPARA"

    """
)

DEVIP = ReplaceableObject(
    'huawei_cm_4g."DEVIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CN",
        "IP",
        "MASK",
        "PN",
        "PT",
        "SBT",
        "SN",
        "SRN",
        "VRFIDX"
    FROM
    huawei_nbi_lte."DEVIP"

    """
)

DHCPRELAYSWITCH = ReplaceableObject(
    'huawei_cm_4g."DHCPRELAYSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ES"
    FROM
    huawei_nbi_lte."DHCPRELAYSWITCH"

    """
)

DIFPRI = ReplaceableObject(
    'huawei_cm_4g."DIFPRI"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPCLKPRI",
        "OMHIGHPRI",
        "OMLOWPRI",
        "PRIRULE",
        "SIGPRI"
    FROM
    huawei_nbi_lte."DIFPRI"

    """
)

DISTBASEDHO = ReplaceableObject(
    'huawei_cm_4g."DISTBASEDHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DISTBASEDHOTHD",
        "DISTBASEDMEASOBJTYPE",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."DISTBASEDHO"

    """
)

DRX = ReplaceableObject(
    'huawei_cm_4g."DRX"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DRXALGSWITCH",
        "DRXINACTIVITYTIMERSPECIAL",
        "LONGDRXCYCLEFORANR",
        "LONGDRXCYCLEFORIRATANR",
        "LONGDRXCYCLESPECIAL",
        "ONDURATIONTIMERSPECIAL",
        "SHORTDRXSWITCH",
        "SUPPORTSHORTDRXSPECIAL"
    FROM
    huawei_nbi_lte."DRX"

    """
)

DRXPARAGROUP = ReplaceableObject(
    'huawei_cm_4g."DRXPARAGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DRXPARAGROUPID",
        "ENTERDRXSWITCH",
        "LOCALCELLID",
        "DRXINACTIVITYTIMER",
        "DRXRETXTIMER",
        "LONGDRXCYCLE",
        "ONDURATIONTIMER",
        "SUPPORTSHORTDRX",
        "DRXSHORTCYCLETIMER",
        "SHORTDRXCYCLE"
    FROM
    huawei_nbi_lte."DRXPARAGROUP"

    """
)

DSCPMAP = ReplaceableObject(
    'huawei_cm_4g."DSCPMAP"',
    """

    SELECT 
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
        "VLANPRIO",
        "VRFIDX"
    FROM
    huawei_nbi_lte."DSCPMAP"

    """
)

EMC = ReplaceableObject(
    'huawei_cm_4g."EMC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "EMCENABLE"
    FROM
    huawei_nbi_lte."EMC"

    """
)

ENODEBALGOSWITCH = ReplaceableObject(
    'huawei_cm_4g."ENODEBALGOSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANRSWITCH",
        "BLINDNCELLOPTSWITCH",
        "CAALGOSWITCH",
        "CLUSTERPARTITIONNODEFLAG",
        "CMASSWITCH",
        "DLICICSWITCH",
        "FREQLAYERSWTICH",
        "HIGHLOADNETOPTSWITCH",
        "HIGHSPEEDROOTSEQCSSWITCH",
        "HOALGOSWITCH",
        "HOCOMMOPTSWITCH",
        "HOMODESWITCH",
        "HOSIGNALINGOPTSWITCH",
        "LCSSWITCH",
        "MLBALGOSWITCH",
        "MROSWITCH",
        "OVERBBUSSWITCH",
        "PCICONFLICTALMSWITCH",
        "POWERSAVESWITCH",
        "RANSHARINGANRSWITCH",
        "REDIRECTSWITCH",
        "RIMONECOSWITCH",
        "RIMSWITCH",
        "SCHOPTSWITCH",
        "TPESWITCH",
        "TRMSWITCH",
        "UENUMPREEMPTSWITCH",
        "ULICICFREQSWITCH",
        "ULICICTIMESWITCH",
        "VQMALGOSWITCH"
    FROM
    huawei_nbi_lte."ENODEBALGOSWITCH"

    """
)

ENODEBAUTOPOWEROFF = ReplaceableObject(
    'huawei_cm_4g."ENODEBAUTOPOWEROFF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AUTOPOWEROFFSWITCH"
    FROM
    huawei_nbi_lte."ENODEBAUTOPOWEROFF"

    """
)

ENODEBCIPHERCAP = ReplaceableObject(
    'huawei_cm_4g."ENODEBCIPHERCAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FOURTHCIPHERALGO",
        "PRIMARYCIPHERALGO",
        "SECONDCIPHERALGO",
        "THIRDCIPHERALGO"
    FROM
    huawei_nbi_lte."ENODEBCIPHERCAP"

    """
)

ENODEBCONNSTATETIMER = ReplaceableObject(
    'huawei_cm_4g."ENODEBCONNSTATETIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENDMARKERTIMER",
        "FIRSTFORWARDPACKETTIMER",
        "S1MESSAGEWAITINGTIMER",
        "SECCMPWAITINGTIMER",
        "UPUECAPINFOWAITINGTIMER",
        "UUMESSAGEWAITINGTIMER",
        "WAITRRCCONNSETUPCMPTIMER",
        "X2MESSAGEWAITINGTIMER"
    FROM
    huawei_nbi_lte."ENODEBCONNSTATETIMER"

    """
)

ENODEBFUNCTION = ReplaceableObject(
    'huawei_cm_4g."ENODEBFUNCTION"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENODEBFUNCTIONNAME",
        "ENODEBID"
    FROM
    huawei_nbi_lte."ENODEBFUNCTION"

    """
)

ENODEBINTEGRITYCAP = ReplaceableObject(
    'huawei_cm_4g."ENODEBINTEGRITYCAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "NULLALGO",
        "PRIMARYINTEGRITYALGO",
        "SECONDINTEGRITYALGO",
        "THIRDINTEGRITYALGO"
    FROM
    huawei_nbi_lte."ENODEBINTEGRITYCAP"

    """
)

ENODEBMLB = ReplaceableObject(
    'huawei_cm_4g."ENODEBMLB"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERFREQIDLEMLBMODE"
    FROM
    huawei_nbi_lte."ENODEBMLB"

    """
)

ENODEBPATH = ReplaceableObject(
    'huawei_cm_4g."ENODEBPATH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APPTYPE",
        "IPPATHID",
        "S1INTERFACEID",
        "X2INTERFACEID"
    FROM
    huawei_nbi_lte."ENODEBPATH"

    """
)

ENODEBSHARINGMODE = ReplaceableObject(
    'huawei_cm_4g."ENODEBSHARINGMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENODEBSHARINGMODE"
    FROM
    huawei_nbi_lte."ENODEBSHARINGMODE"

    """
)

EPGROUP = ReplaceableObject(
    'huawei_cm_4g."EPGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EPGROUPID",
        "PACKETFILTERSWITCH",
        "USERLABEL",
        "VRFIDX"
    FROM
    huawei_nbi_lte."EPGROUP"

    """
)

ETHPORT = ReplaceableObject(
    'huawei_cm_4g."ETHPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CN",
        "DUPLEX",
        "MTU",
        "PA",
        "PN",
        "SBT",
        "SN",
        "SPEED",
        "SRN"
    FROM
    huawei_nbi_lte."ETHPORT"

    """
)

EUCELLSECTOREQM = ReplaceableObject(
    'huawei_cm_4g."EUCELLSECTOREQM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "REFERENCESIGNALPWR",
        "REFERENCESIGNALPWRMARGIN",
        "SECTORCPRICOMPRESSION",
        "SECTOREQMID"
    FROM
    huawei_nbi_lte."EUCELLSECTOREQM"

    """
)

EUCOSCHCFG = ReplaceableObject(
    'huawei_cm_4g."EUCOSCHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PRTNODEBASEBANDEQMID"
    FROM
    huawei_nbi_lte."EUCOSCHCFG"

    """
)

EUTRANEXTERNALCELL = ReplaceableObject(
    'huawei_cm_4g."EUTRANEXTERNALCELL"',
    """

    SELECT 
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
        "CTRLMODE",
        "DLEARFCN",
        "ENODEBID",
        "MCC",
        "MNC",
        "PHYCELLID",
        "TAC",
        "ULEARFCNCFGIND",
        "CELLNAME"
    FROM
    huawei_nbi_lte."EUTRANEXTERNALCELL"

    """
)

EUTRANINTRAFREQNCELL = ReplaceableObject(
    'huawei_cm_4g."EUTRANINTRAFREQNCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANRFLAG",
        "CELLID",
        "CELLINDIVIDUALOFFSET",
        "CELLQOFFSET",
        "CTRLMODE",
        "ENODEBID",
        "LOCALCELLID",
        "MCC",
        "MNC",
        "NOHOFLAG",
        "NORMVFLAG",
        "LOCALCELLNAME",
        "NEIGHBOURCELLNAME"
    FROM
    huawei_nbi_lte."EUTRANINTRAFREQNCELL"

    """
)

FDDRESMODE = ReplaceableObject(
    'huawei_cm_4g."FDDRESMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BBCAPABILITYMODE",
        "SFNCAPABILITYMODE"
    FROM
    huawei_nbi_lte."FDDRESMODE"

    """
)

filefooter = ReplaceableObject(
    'huawei_cm_4g."FILEFOOTER"',
    """

    SELECT 
        "FileName",
        "datetime"
    FROM
    huawei_nbi_lte."filefooter"

    """
)

GERANEXTERNALCELL = ReplaceableObject(
    'huawei_cm_4g."GERANEXTERNALCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BANDINDICATOR",
        "BASESTATIONCOLOURCODE",
        "CELLNAME",
        "CSPSHOIND",
        "CTRLMODE",
        "DTMIND",
        "GERANARFCN",
        "GERANCELLID",
        "LAC",
        "MCC",
        "MNC",
        "NETWORKCOLOURCODE",
        "RACCFGIND",
        "RAC"
    FROM
    huawei_nbi_lte."GERANEXTERNALCELL"

    """
)

GERANINTERFCFG = ReplaceableObject(
    'huawei_cm_4g."GERANINTERFCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DLGERANINTEFRBNUM",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."GERANINTERFCFG"

    """
)

GERANNCELL = ReplaceableObject(
    'huawei_cm_4g."GERANNCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANRFLAG",
        "BLINDHOPRIORITY",
        "CTRLMODE",
        "GERANCELLID",
        "LAC",
        "LOCALCELLID",
        "LOCALCELLNAME",
        "MCC",
        "MNC",
        "NEIGHBOURCELLNAME",
        "NOHOFLAG",
        "NORMVFLAG",
        "OVERLAPIND"
    FROM
    huawei_nbi_lte."GERANNCELL"

    """
)

GERANNFREQGROUP = ReplaceableObject(
    'huawei_cm_4g."GERANNFREQGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BANDINDICATOR",
        "BCCHGROUPID",
        "CELLRESELPRIORITY",
        "CELLRESELPRIORITYCFGIND",
        "CONNFREQPRIORITY",
        "GERANVERSION",
        "LOCALCELLID",
        "NCCPERMITTED",
        "OFFSETFREQ",
        "PMAXGERANCFGIND",
        "QRXLEVMIN",
        "STARTINGARFCN",
        "THRESHXHIGH",
        "THRESHXLOW"
    FROM
    huawei_nbi_lte."GERANNFREQGROUP"

    """
)

GERANNFREQGROUPARFCN = ReplaceableObject(
    'huawei_cm_4g."GERANNFREQGROUPARFCN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BCCHGROUPID",
        "GERANARFCN",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."GERANNFREQGROUPARFCN"

    """
)

GLOBALPROCSWITCH = ReplaceableObject(
    'huawei_cm_4g."GLOBALPROCSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENHANCEDPHRRPTCTRLSW",
        "EUTRANLOADTRANSSWITCH",
        "L2GUHOWITHLCAPSWITCH",
        "LCGPROFILE",
        "MMESELECTPROCSWITCH",
        "PREFERSIGEXTEND",
        "RIMCODINGPOLICY",
        "RNCPOOLHORIMSWITCH",
        "RRCREESTPROTECTTHD",
        "S1DEFAULTPAGINGDRXSELECT",
        "S1HOINDATAFWDSWITCH",
        "SRIADAPTIVESWITCH",
        "TARGETOPBASEDX2SWITCH",
        "UELINKABNORMALDETECTSWITCH",
        "UTRANLOADTRANSCHAN",
        "UUMSGSIMULSENDSWITCH",
        "X2BASEDDELNCELLCFGSWITCH",
        "X2BASEDUPTENODEBCFGSWITCH",
        "X2SONDELETEHOINNUMTHD",
        "X2SONDELETEHOOUTNUMTHD",
        "X2SONDELETESWITCH",
        "X2SONDELETETIMER",
        "X2SONDELETETIMERFORX2FAULT",
        "X2SONDELETETIMERFORX2USAGE",
        "X2SONLINKSETUPTYPE",
        "X2SONSETUPSWITCH",
        "X2SONTNLSELECTMODE"
    FROM
    huawei_nbi_lte."GLOBALPROCSWITCH"

    """
)

GTPU = ReplaceableObject(
    'huawei_cm_4g."GTPU"',
    """

    SELECT 
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
        "STATICCHK",
        "TIMEOUTCNT",
        "TIMEOUTTH"
    FROM
    huawei_nbi_lte."GTPU"

    """
)

GTRANSPARA = ReplaceableObject(
    'huawei_cm_4g."GTRANSPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BYPASSSWITCH",
        "LPSCHSW",
        "OMCHSWITCHBACK",
        "RATECFGTYPE",
        "SBTIME",
        "SCTPRTRPTSW"
    FROM
    huawei_nbi_lte."GTRANSPARA"

    """
)

HOMEASCOMM = ReplaceableObject(
    'huawei_cm_4g."HOMEASCOMM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EUTRANFILTERCOEFFRSRP",
        "EUTRANFILTERCOEFFRSRQ",
        "GAPPATTERNTYPE",
        "GERANFILTERCOEFF",
        "OPTHOPREFAILPUNISHTIMER",
        "SMEASUREIND",
        "SPEEDDEPPARAIND",
        "UTRANFILTERCOEFFECN0",
        "UTRANFILTERCOEFFRSCP"
    FROM
    huawei_nbi_lte."HOMEASCOMM"

    """
)

IKECFG = ReplaceableObject(
    'huawei_cm_4g."IKECFG"',
    """

    SELECT 
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
        "IKEKLI",
        "IKEKLT"
    FROM
    huawei_nbi_lte."IKECFG"

    """
)

INTERFREQHOGROUP = ReplaceableObject(
    'huawei_cm_4g."INTERFREQHOGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "A3INTERFREQHOA1THDRSRP",
        "A3INTERFREQHOA2THDRSRP",
        "FREQPRIINTERFREQHOA1THDRSRP",
        "FREQPRIINTERFREQHOA1THDRSRQ",
        "FREQPRIINTERFREQHOA2THDRSRP",
        "FREQPRIINTERFREQHOA2THDRSRQ",
        "INTERFREQHOA1A2HYST",
        "INTERFREQHOA1A2TIMETOTRIG",
        "INTERFREQHOA1THDRSRP",
        "INTERFREQHOA1THDRSRQ",
        "INTERFREQHOA2THDRSRP",
        "INTERFREQHOA2THDRSRQ",
        "INTERFREQHOA3OFFSET",
        "INTERFREQHOA4HYST",
        "INTERFREQHOA4THDRSRP",
        "INTERFREQHOA4THDRSRQ",
        "INTERFREQHOA4TIMETOTRIG",
        "INTERFREQHOGROUPID",
        "INTERFREQLOADBASEDHOA4THDRSRP",
        "INTERFREQLOADBASEDHOA4THDRSRQ",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."INTERFREQHOGROUP"

    """
)

INTERRATCELLSHUTDOWN = ReplaceableObject(
    'huawei_cm_4g."INTERRATCELLSHUTDOWN"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BEARNUMTHD",
        "DLPRBTHD",
        "FORCESHUTDOWNSWITCH",
        "LOCALCELLID",
        "SHUTDOWNTYPE",
        "STARTTIME",
        "STOPTIME",
        "ULPRBTHD"
    FROM
    huawei_nbi_lte."INTERRATCELLSHUTDOWN"

    """
)

INTERRATHOCDMA1XRTTGROUP = ReplaceableObject(
    'huawei_cm_4g."INTERRATHOCDMA1XRTTGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERRATHOCDMA1XRTTGROUPID",
        "INTERRATHOCDMAB1HYST",
        "INTERRATHOCDMAB1THDPS",
        "INTERRATHOCDMAB1TIMETOTRIG",
        "LDSVBASEDHOCDMAB1THDPS",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."INTERRATHOCDMA1XRTTGROUP"

    """
)

INTERRATHOCDMAHRPDGROUP = ReplaceableObject(
    'huawei_cm_4g."INTERRATHOCDMAHRPDGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERRATHOCDMAB1HYST",
        "INTERRATHOCDMAB1THDPS",
        "INTERRATHOCDMAB1TIMETOTRIG",
        "INTERRATHOCDMAHRPDGROUPID",
        "LDSVBASEDHOCDMAB1THDPS",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."INTERRATHOCDMAHRPDGROUP"

    """
)

INTERRATHOCOMM = ReplaceableObject(
    'huawei_cm_4g."INTERRATHOCOMM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLINFOMAXGERANCELLNUM",
        "CELLINFOMAXUTRANCELLNUM",
        "GERANCELLNUMFOREMCREDIRECT",
        "INTERRATCDMA1XRTTRPRTINTERVAL",
        "INTERRATCDMAHRPDRPRTINTERVAL",
        "INTERRATHOA1A2TRIGQUAN",
        "INTERRATHOCDMA1XRTTB1MEASQUAN",
        "INTERRATHOCDMAHRPDB1MEASQUAN",
        "INTERRATHOEVENTTYPE",
        "INTERRATHOGERANRPRTINTERVAL",
        "INTERRATHOMAXRPRTCELL",
        "INTERRATHORPRTAMOUNT",
        "INTERRATHOUTRANB1MEASQUAN",
        "INTERRATHOUTRANRPRTINTERVAL",
        "UTRANCELLNUMFOREMCREDIRECT"
    FROM
    huawei_nbi_lte."INTERRATHOCOMM"

    """
)

INTERRATHOCOMMGROUP = ReplaceableObject(
    'huawei_cm_4g."INTERRATHOCOMMGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHOA2THDOFFSET",
        "INTERRATHOA1A2HYST",
        "INTERRATHOA1A2TIMETOTRIG",
        "INTERRATHOA1THDRSRP",
        "INTERRATHOA1THDRSRQ",
        "INTERRATHOA2THDRSRP",
        "INTERRATHOA2THDRSRQ",
        "INTERRATHOCOMMGROUPID",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."INTERRATHOCOMMGROUP"

    """
)

INTERRATHOGERANGROUP = ReplaceableObject(
    'huawei_cm_4g."INTERRATHOGERANGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERRATHOGERANB1HYST",
        "INTERRATHOGERANB1THD",
        "INTERRATHOGERANB1TIMETOTRIG",
        "INTERRATHOGERANGROUPID",
        "LDSVBASEDHOGERANB1THD",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."INTERRATHOGERANGROUP"

    """
)

INTERRATHOUTRANGROUP = ReplaceableObject(
    'huawei_cm_4g."INTERRATHOUTRANGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERRATHOUTRANB1HYST",
        "INTERRATHOUTRANB1THDECN0",
        "INTERRATHOUTRANB1THDRSCP",
        "INTERRATHOUTRANB1TIMETOTRIG",
        "INTERRATHOUTRANGROUPID",
        "LDSVBASEDHOUTRANB1THDECN0",
        "LDSVBASEDHOUTRANB1THDRSCP",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."INTERRATHOUTRANGROUP"

    """
)

INTERRATPOLICYCFGGROUP = ReplaceableObject(
    'huawei_cm_4g."INTERRATPOLICYCFGGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CDMA1XRTTHOCFG",
        "CDMAHRPDHOCFG",
        "GERANGPRSEDGEHOCFG",
        "GERANGSMHOCFG",
        "INTERRATPOLICYCFGGROUPID",
        "NOFASTANRFLAG",
        "NOHOFLAG",
        "UTRANHOCFG"
    FROM
    huawei_nbi_lte."INTERRATPOLICYCFGGROUP"

    """
)

INTRAFREQHOGROUP = ReplaceableObject(
    'huawei_cm_4g."INTRAFREQHOGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTRAFREQHOA3HYST",
        "INTRAFREQHOA3OFFSET",
        "INTRAFREQHOA3TIMETOTRIG",
        "INTRAFREQHOGROUPID",
        "LOCALCELLID"
    FROM
    huawei_nbi_lte."INTRAFREQHOGROUP"

    """
)

INTRARATHOCOMM = ReplaceableObject(
    'huawei_cm_4g."INTRARATHOCOMM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COVBASEDIFHOWAITINGTIMER",
        "FREQPRIINTERFREQHOA1TRIGQUAN",
        "INTERFREQHOA1A2TRIGQUAN",
        "INTERFREQHOA4RPRTQUAN",
        "INTERFREQHOA4TRIGQUAN",
        "INTERFREQHORPRTINTERVAL",
        "INTRAFREQHOA3RPRTQUAN",
        "INTRAFREQHOA3TRIGQUAN",
        "INTRAFREQHORPRTINTERVAL",
        "INTRARATHOMAXRPRTCELL",
        "INTRARATHORPRTAMOUNT"
    FROM
    huawei_nbi_lte."INTRARATHOCOMM"

    """
)

IPGUARD = ReplaceableObject(
    'huawei_cm_4g."IPGUARD"',
    """

    SELECT 
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
        "INVALIDPKTCHKSW",
        "IPSECREPLAYCHKSW"
    FROM
    huawei_nbi_lte."IPGUARD"

    """
)

IPPATH = ReplaceableObject(
    'huawei_cm_4g."IPPATH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CN",
        "DESCRI",
        "JNRSCGRP",
        "LOCALIP",
        "PATHCHK",
        "PATHID",
        "PATHTYPE",
        "PEERIP",
        "PN",
        "PT",
        "QT",
        "SBT",
        "SN",
        "SRN",
        "VRFIDX"
    FROM
    huawei_nbi_lte."IPPATH"

    """
)

IPRT = ReplaceableObject(
    'huawei_cm_4g."IPRT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CN",
        "DESCRI",
        "DSTIP",
        "DSTMASK",
        "NEXTHOP",
        "PREF",
        "RTIDX",
        "RTTYPE",
        "SBT",
        "SN",
        "SRN",
        "VRFIDX"
    FROM
    huawei_nbi_lte."IPRT"

    """
)

LOCATION = ReplaceableObject(
    'huawei_cm_4g."LOCATION"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALTITUDE",
        "GCDF",
        "LATITUDEDEGFORMAT",
        "LOCATIONID",
        "LOCATIONNAME",
        "LONGITUDEDEGFORMAT",
        "PRECISE",
        "RANGE",
        "USERLABEL",
        "CITY"
    FROM
    huawei_nbi_lte."LOCATION"

    """
)

MIMOADAPTIVEPARACFG = ReplaceableObject(
    'huawei_cm_4g."MIMOADAPTIVEPARACFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INITIALMIMOTYPE",
        "MIMOADAPTIVESWITCH"
    FROM
    huawei_nbi_lte."MIMOADAPTIVEPARACFG"

    """
)

MMEFEATURECFG = ReplaceableObject(
    'huawei_cm_4g."MMEFEATURECFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "MDTENABLE",
        "S1INTERFACEID"
    FROM
    huawei_nbi_lte."MMEFEATURECFG"

    """
)

MRO = ReplaceableObject(
    'huawei_cm_4g."MRO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COVERABNORMALTHD",
        "NCELLOPTTHD",
        "NEIGHBORRSRPTHD",
        "OPTPERIOD",
        "PINGPONGRATIOTHD",
        "PINGPONGTIMETHD",
        "SERVINGRSRPTHD",
        "STATNUMTHD",
        "UEPINGPONGNUMTHD"
    FROM
    huawei_nbi_lte."MRO"

    """
)

NE = ReplaceableObject(
    'huawei_cm_4g."NE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DID",
        "LOCATION",
        "NENAME",
        "PRODUCTVERSION",
        "SITENAME"
    FROM
    huawei_nbi_lte."NE"

    """
)

NODE = ReplaceableObject(
    'huawei_cm_4g."NODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PRODUCTTYPE",
        "WM"
    FROM
    huawei_nbi_lte."NODE"

    """
)

OMCH = ReplaceableObject(
    'huawei_cm_4g."OMCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BEAR",
        "BRT",
        "CHECKTYPE",
        "FLAG",
        "IP",
        "MASK",
        "PEERIP",
        "PEERMASK"
    FROM
    huawei_nbi_lte."OMCH"

    """
)

PCCHCFG = ReplaceableObject(
    'huawei_cm_4g."PCCHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DEFAULTPAGINGCYCLE",
        "LOCALCELLID",
        "MAXPAGINGRECORDSNUM",
        "NB",
        "PAGINGSENTNUM"
    FROM
    huawei_nbi_lte."PCCHCFG"

    """
)

PDCPROHCPARA = ReplaceableObject(
    'huawei_cm_4g."PDCPROHCPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HIGHESTMODE",
        "PROFILES",
        "ROHCSWITCH"
    FROM
    huawei_nbi_lte."PDCPROHCPARA"

    """
)

PDSCHCFG = ReplaceableObject(
    'huawei_cm_4g."PDSCHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "PB",
        "REFERENCESIGNALPWR",
        "REFERENCESIGNALPWRMARGIN"
    FROM
    huawei_nbi_lte."PDSCHCFG"

    """
)

PHICHCFG = ReplaceableObject(
    'huawei_cm_4g."PHICHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "PHICHDURATION",
        "PHICHRESOURCE"
    FROM
    huawei_nbi_lte."PHICHCFG"

    """
)

PUCCHCFG = ReplaceableObject(
    'huawei_cm_4g."PUCCHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CQIRBNUM",
        "DELTASHIFT",
        "LOCALCELLID",
        "NASRICHNUM",
        "PUCCHEXTENDEDRBNUM"
    FROM
    huawei_nbi_lte."PUCCHCFG"

    """
)

PUSCHCFG = ReplaceableObject(
    'huawei_cm_4g."PUSCHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CYCLICSHIFT",
        "GROUPASSIGNPUSCH",
        "GROUPHOPPINGENABLED",
        "HOPPINGMODE",
        "HOPPINGOFFSET",
        "LOCALCELLID",
        "NSB",
        "QAM64ENABLED",
        "SEQHOPPINGENABLED"
    FROM
    huawei_nbi_lte."PUSCHCFG"

    """
)

PUSCHPARAM = ReplaceableObject(
    'huawei_cm_4g."PUSCHPARAM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DELTAOFFSETACKINDEX",
        "DELTAOFFSETCQIINDEX",
        "DELTAOFFSETRIINDEX"
    FROM
    huawei_nbi_lte."PUSCHPARAM"

    """
)

RACHCFG = ReplaceableObject(
    'huawei_cm_4g."RACHCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CONTENTIONRESOLUTIONTIMER",
        "LOCALCELLID",
        "MAXHARQMSG3TX",
        "MESSAGESIZEGROUPA",
        "PRACHCONFIGINDEXCFGIND",
        "PRACHFREQOFFSET",
        "PREAMBINITRCVTARGETPWR",
        "PREAMBLETRANSMAX",
        "PWRRAMPINGSTEP"
    FROM
    huawei_nbi_lte."RACHCFG"

    """
)

RET = ReplaceableObject(
    'huawei_cm_4g."RET"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CTRLCN",
        "CTRLSN",
        "CTRLSRN",
        "DEVICENAME",
        "DEVICENO",
        "POLARTYPE",
        "RETTYPE",
        "SCENARIO",
        "SERIALNO",
        "SUBUNITNUM",
        "VENDORCODE"
    FROM
    huawei_nbi_lte."RET"

    """
)

RETDEVICEDATA = ReplaceableObject(
    'huawei_cm_4g."RETDEVICEDATA"',
    """

    SELECT 
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
        "DEVICENO",
        "SUBUNITNO",
        "TILT"
    FROM
    huawei_nbi_lte."RETDEVICEDATA"

    """
)

RETSUBUNIT = ReplaceableObject(
    'huawei_cm_4g."RETSUBUNIT"',
    """

    SELECT 
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
        "CONNCN1",
        "CONNCN2",
        "CONNPN1",
        "CONNPN2",
        "DEVICENO",
        "SUBNAME",
        "SUBUNITNO",
        "TILT"
    FROM
    huawei_nbi_lte."RETSUBUNIT"

    """
)

RLCPDCPPARAGROUP = ReplaceableObject(
    'huawei_cm_4g."RLCPDCPPARAGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DISCARDTIMER",
        "DLRLCSNSIZE",
        "ENODEBUMREORDERINGTIMER",
        "PDCPSNSIZE",
        "RLCMODE",
        "RLCPDCPPARAGROUPID",
        "UEUMREORDERINGTIMER",
        "ULRLCSNSIZE",
        "ENODEBAMREORDERINGTIMER",
        "ENODEBMAXRETXTHRESHOLD",
        "ENODEBPOLLBYTE",
        "ENODEBPOLLPDU",
        "ENODEBPOLLRETRANSMITTIMER",
        "ENODEBSTATUSPROHIBITTIMER",
        "PDCPSTATUSRPTREQ",
        "RLCPARAADAPTSWITCH",
        "UEAMREORDERINGTIMER",
        "UEMAXRETXTHRESHOLD",
        "UEPOLLBYTE",
        "UEPOLLPDU",
        "UEPOLLRETRANSMITTIMER",
        "UESTATUSPROHIBITTIMER"
    FROM
    huawei_nbi_lte."RLCPDCPPARAGROUP"

    """
)

RRCCONNSTATETIMER = ReplaceableObject(
    'huawei_cm_4g."RRCCONNSTATETIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FILTERREPTRRCCONNREQTIMER",
        "T302",
        "T304FOREUTRAN",
        "T304FORGERAN",
        "T320FORLOADBALANCE",
        "T320FOROTHER",
        "UEINACTIVETIMER",
        "UEINACTIVITYTIMERDYNDRX",
        "ULSYNTIMER",
        "ULSYNTIMERDYNDRX"
    FROM
    huawei_nbi_lte."RRCCONNSTATETIMER"

    """
)

RRUJOINTCALPARACFG = ReplaceableObject(
    'huawei_cm_4g."RRUJOINTCALPARACFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "TXCHNCALSWITCH"
    FROM
    huawei_nbi_lte."RRUJOINTCALPARACFG"

    """
)

S1 = ReplaceableObject(
    'huawei_cm_4g."S1"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "CNOPSHARINGGROUPID",
        "CPEPGROUPID",
        "EPGROUPCFGFLAG",
        "MMERELEASE",
        "PRIORITY",
        "S1ID",
        "UPEPGROUPID",
        "USERLABEL"
    FROM
    huawei_nbi_lte."S1"

    """
)

S1INTERFACE = ReplaceableObject(
    'huawei_cm_4g."S1INTERFACE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "CNOPSHARINGGROUPID",
        "MMERELEASE",
        "PRIORITY",
        "S1CPBEARERID",
        "S1INTERFACEID",
        "S1INTERFACEISBLOCK"
    FROM
    huawei_nbi_lte."S1INTERFACE"

    """
)

S1REESTTIMER = ReplaceableObject(
    'huawei_cm_4g."S1REESTTIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "S1REESTMAXTIMER",
        "S1REESTMINTIMER"
    FROM
    huawei_nbi_lte."S1REESTTIMER"

    """
)

SCTPHOST = ReplaceableObject(
    'huawei_cm_4g."SCTPHOST"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPVERSION",
        "PN",
        "SCTPHOSTID",
        "SCTPTEMPLATEID",
        "SIGIP1SECSWITCH",
        "SIGIP1V4",
        "SIGIP2SECSWITCH",
        "SIGIP2V4",
        "USERLABEL",
        "VRFIDX"
    FROM
    huawei_nbi_lte."SCTPHOST"

    """
)

SCTPHOSTREF = ReplaceableObject(
    'huawei_cm_4g."SCTPHOSTREF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EPGROUPID",
        "SCTPHOSTID"
    FROM
    huawei_nbi_lte."SCTPHOSTREF"

    """
)

SCTPLNK = ReplaceableObject(
    'huawei_cm_4g."SCTPLNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AUTOSWITCH",
        "CN",
        "DESCRI",
        "HBINTER",
        "LOCIP",
        "LOCPORT",
        "MAXASSOCRETR",
        "MAXPATHRETR",
        "PEERIP",
        "PEERPORT",
        "SCTPNO",
        "SECLOCIP",
        "SECPEERIP",
        "SN",
        "SRN",
        "SWITCHBACKHBNUM",
        "VRFIDX"
    FROM
    huawei_nbi_lte."SCTPLNK"

    """
)

SCTPPEER = ReplaceableObject(
    'huawei_cm_4g."SCTPPEER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPVERSION",
        "PN",
        "SCTPPEERID",
        "SIGIP1SECSWITCH",
        "SIGIP1V4",
        "SIGIP2SECSWITCH",
        "SIGIP2V4",
        "USERLABEL",
        "VRFIDX"
    FROM
    huawei_nbi_lte."SCTPPEER"

    """
)

SCTPPEERREF = ReplaceableObject(
    'huawei_cm_4g."SCTPPEERREF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EPGROUPID",
        "SCTPPEERID"
    FROM
    huawei_nbi_lte."SCTPPEERREF"

    """
)

SECTOR = ReplaceableObject(
    'huawei_cm_4g."SECTOR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCATIONNAME",
        "SECNAME",
        "SECTORID",
        "USERLABEL"
    FROM
    huawei_nbi_lte."SECTOR"

    """
)

SECTORANTENNAREF = ReplaceableObject(
    'huawei_cm_4g."SECTORANTENNAREF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANTN",
        "CN",
        "SECTORID",
        "SN",
        "SRN"
    FROM
    huawei_nbi_lte."SECTORANTENNAREF"

    """
)

SECTOREQM = ReplaceableObject(
    'huawei_cm_4g."SECTOREQM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SECTOREQMID",
        "SECTORID"
    FROM
    huawei_nbi_lte."SECTOREQM"

    """
)

SECTOREQMANTENNAREF = ReplaceableObject(
    'huawei_cm_4g."SECTOREQMANTENNAREF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANTN",
        "ANTTYPE",
        "CN",
        "SECTOREQMID",
        "SN",
        "SRN",
        "TXBKPMODE"
    FROM
    huawei_nbi_lte."SECTOREQMANTENNAREF"

    """
)

SERVICEIFDLEARFCNGRP = ReplaceableObject(
    'huawei_cm_4g."SERVICEIFDLEARFCNGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "DLEARFCN",
        "DLEARFCNINDEX",
        "SERVICEIFHOCFGGROUPID"
    FROM
    huawei_nbi_lte."SERVICEIFDLEARFCNGRP"

    """
)

SERVICEIFHOCFGGROUP = ReplaceableObject(
    'huawei_cm_4g."SERVICEIFHOCFGGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "A4RPTWAITINGTIMER",
        "A4TIMETOTRIGER",
        "CNOPERATORID",
        "DLEARFCN",
        "INTERFREQHOSTATE",
        "SERVICEIFHOCFGGROUPID"
    FROM
    huawei_nbi_lte."SERVICEIFHOCFGGROUP"

    """
)

SERVICEIRHOCFGGROUP = ReplaceableObject(
    'huawei_cm_4g."SERVICEIRHOCFGGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "INTERRATHOSTATE",
        "SERVICEIRHOCFGGROUPID",
        "SERVICEIRMEASMODE"
    FROM
    huawei_nbi_lte."SERVICEIRHOCFGGROUP"

    """
)

SIMULOAD = ReplaceableObject(
    'huawei_cm_4g."SIMULOAD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FREQSELSWITCH",
        "SIMULOADCFGINDEX",
        "SIMULOADPWRTHD",
        "SIMULOADRBTHD",
        "SIMULOADREPORTPERIOD",
        "SIMULOADSTATPERIOD"
    FROM
    huawei_nbi_lte."SIMULOAD"

    """
)

SRSADAPTIVECFG = ReplaceableObject(
    'huawei_cm_4g."SRSADAPTIVECFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SRSPERIODADAPTIVE"
    FROM
    huawei_nbi_lte."SRSADAPTIVECFG"

    """
)

SRSCFG = ReplaceableObject(
    'huawei_cm_4g."SRSCFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANSRSSIMUTRANS",
        "FDDSRSCFGMODE",
        "LOCALCELLID",
        "SRSCFGIND",
        "SRSSUBFRAMECFG",
        "TDDSRSCFGMODE"
    FROM
    huawei_nbi_lte."SRSCFG"

    """
)

STANDARDQCI = ReplaceableObject(
    'huawei_cm_4g."STANDARDQCI"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERRATPOLICYCFGGROUPID",
        "PREALLOCATIONWEIGHT",
        "QCI",
        "RLCPDCPPARAGROUPID",
        "PRIORITISEDBITRATE",
        "FLOWCTRLTYPE",
        "DLMINGBR",
        "DLSCHPRIORITYFACTOR",
        "LOGICALCHANNELPRIORITY",
        "ULMINGBR",
        "ULSCHPRIORITYFACTOR"
    FROM
    huawei_nbi_lte."STANDARDQCI"

    """
)

SUBSESSION_NE = ReplaceableObject(
    'huawei_cm_4g."SUBSESSION_NE"',
    """

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
    huawei_nbi_lte."SUBSESSION_NE"

    """
)

TACALG = ReplaceableObject(
    'huawei_cm_4g."TACALG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EMCTACPSW",
        "PORTDLCACSW",
        "PORTDLOBSW",
        "PORTULCACSW",
        "PORTULOBSW",
        "RSCGRPDLCACSWITCH",
        "RSCGRPULCACSWITCH",
        "TRMDLBRONZECACTH",
        "TRMDLGBRCACTH",
        "TRMDLGOLDCACTH",
        "TRMDLHOCACTH",
        "TRMDLPRESW",
        "TRMDLSILVERCACTH",
        "TRMULBRONZECACTH",
        "TRMULGBRCACTH",
        "TRMULGOLDCACTH",
        "TRMULHOCACTH",
        "TRMULPRESW",
        "TRMULSILVERCACTH"
    FROM
    huawei_nbi_lte."TACALG"

    """
)

TCEIPMAPPING = ReplaceableObject(
    'huawei_cm_4g."TCEIPMAPPING"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPMODE",
        "TCEID",
        "TCEIPV4ADDR"
    FROM
    huawei_nbi_lte."TCEIPMAPPING"

    """
)

TCPACKCTRLALGO = ReplaceableObject(
    'huawei_cm_4g."TCPACKCTRLALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACKCTRLSWITCH",
        "CTRLTIMERLENGTH",
        "DLMAXTHROUGHPUT"
    FROM
    huawei_nbi_lte."TCPACKCTRLALGO"

    """
)

TCPACKLIMITALG = ReplaceableObject(
    'huawei_cm_4g."TCPACKLIMITALG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TCPACKLIMITSWITCH"
    FROM
    huawei_nbi_lte."TCPACKLIMITALG"

    """
)

TCPMSSCTRL = ReplaceableObject(
    'huawei_cm_4g."TCPMSSCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TCPMSSCTRLSWITCH",
        "TCPMSSTHD"
    FROM
    huawei_nbi_lte."TCPMSSCTRL"

    """
)

TDDFRAMEOFFSET = ReplaceableObject(
    'huawei_cm_4g."TDDFRAMEOFFSET"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TIMEOFFSET"
    FROM
    huawei_nbi_lte."TDDFRAMEOFFSET"

    """
)

TDDRESMODESWITCH = ReplaceableObject(
    'huawei_cm_4g."TDDRESMODESWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BBRESEXCLUSIVESWITCH",
        "CLKRESEXCLUDESWITCH"
    FROM
    huawei_nbi_lte."TDDRESMODESWITCH"

    """
)

TIMEALIGNMENTTIMER = ReplaceableObject(
    'huawei_cm_4g."TIMEALIGNMENTTIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "TIMEALIGNMENTTIMER"
    FROM
    huawei_nbi_lte."TIMEALIGNMENTTIMER"

    """
)

TOLCALG = ReplaceableObject(
    'huawei_cm_4g."TOLCALG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "TRMDLOLCRELTH",
        "TRMDLOLCSWITCH",
        "TRMDLOLCTRIGTH",
        "TRMOLCRELBEARERNUM",
        "TRMULOLCRELTH",
        "TRMULOLCSWITCH",
        "TRMULOLCTRIGTH"
    FROM
    huawei_nbi_lte."TOLCALG"

    """
)

TPEALGO = ReplaceableObject(
    'huawei_cm_4g."TPEALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PORT1",
        "PORT2",
        "PORT3",
        "PORTLISTNUM"
    FROM
    huawei_nbi_lte."TPEALGO"

    """
)

TRUSTCERT = ReplaceableObject(
    'huawei_cm_4g."TRUSTCERT"',
    """

    SELECT 
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
    huawei_nbi_lte."TRUSTCERT"

    """
)

TYPDRBBSR = ReplaceableObject(
    'huawei_cm_4g."TYPDRBBSR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "QCI",
        "RETXBSRTIMER",
        "TPERODICBSRTIMER"
    FROM
    huawei_nbi_lte."TYPDRBBSR"

    """
)

UDT = ReplaceableObject(
    'huawei_cm_4g."UDT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "UDTNO",
        "UDTPARAGRPID"
    FROM
    huawei_nbi_lte."UDT"

    """
)

UDTPARAGRP = ReplaceableObject(
    'huawei_cm_4g."UDTPARAGRP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTFACTOR",
        "PRI",
        "PRIM2SECPTLOADRATH",
        "PRIMPTLOADTH",
        "PRIMTRANRSCTYPE",
        "PRIRULE",
        "UDTPARAGRPID"
    FROM
    huawei_nbi_lte."UDTPARAGRP"

    """
)

UETIMERCONST = ReplaceableObject(
    'huawei_cm_4g."UETIMERCONST"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCALCELLID",
        "N310",
        "N311",
        "T300",
        "T301",
        "T310",
        "T311"
    FROM
    huawei_nbi_lte."UETIMERCONST"

    """
)

USERPLANEHOST = ReplaceableObject(
    'huawei_cm_4g."USERPLANEHOST"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPSECSWITCH",
        "IPVERSION",
        "LOCIPV4",
        "UPHOSTID",
        "USERLABEL",
        "VRFIDX"
    FROM
    huawei_nbi_lte."USERPLANEHOST"

    """
)

USERPLANEHOSTREF = ReplaceableObject(
    'huawei_cm_4g."USERPLANEHOSTREF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EPGROUPID",
        "UPHOSTID"
    FROM
    huawei_nbi_lte."USERPLANEHOSTREF"

    """
)

USERPLANEPEER = ReplaceableObject(
    'huawei_cm_4g."USERPLANEPEER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPSECSWITCH",
        "IPVERSION",
        "PEERIPV4",
        "UPPEERID",
        "USERLABEL",
        "VRFIDX"
    FROM
    huawei_nbi_lte."USERPLANEPEER"

    """
)

USERPLANEPEERREF = ReplaceableObject(
    'huawei_cm_4g."USERPLANEPEERREF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EPGROUPID",
        "UPPEERID"
    FROM
    huawei_nbi_lte."USERPLANEPEERREF"

    """
)

UTRANEXTERNALCELL = ReplaceableObject(
    'huawei_cm_4g."UTRANEXTERNALCELL"',
    """

    SELECT 
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
        "CELLNAME",
        "CSPSHOIND",
        "CTRLMODE",
        "LAC",
        "MCC",
        "MNC",
        "PSCRAMBCODE",
        "RAC",
        "RACCFGIND",
        "RNCID",
        "UTRANDLARFCN",
        "UTRANFDDTDDTYPE",
        "UTRANULARFCNCFGIND"
    FROM
    huawei_nbi_lte."UTRANEXTERNALCELL"

    """
)

UTRANNCELL = ReplaceableObject(
    'huawei_cm_4g."UTRANNCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANRFLAG",
        "BLINDHOPRIORITY",
        "CELLID",
        "CTRLMODE",
        "LOCALCELLID",
        "MCC",
        "MNC",
        "NOHOFLAG",
        "NORMVFLAG",
        "OVERLAPIND",
        "RNCID",
        "NEIGHBOURCELLNAME",
        "LOCALCELLNAME"
    FROM
    huawei_nbi_lte."UTRANNCELL"

    """
)

UTRANNFREQ = ReplaceableObject(
    'huawei_cm_4g."UTRANNFREQ"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLRESELPRIORITY",
        "CELLRESELPRIORITYCFGIND",
        "CONNFREQPRIORITY",
        "CSPRIORITY",
        "CSPSMIXEDPRIORITY",
        "LOCALCELLID",
        "OFFSETFREQ",
        "PMAXUTRAN",
        "PSPRIORITY",
        "QQUALMIN",
        "QRXLEVMIN",
        "THRESHXHIGH",
        "THRESHXHIGHQ",
        "THRESHXLOW",
        "THRESHXLOWQ",
        "UTRANDLARFCN",
        "UTRANFDDTDDTYPE",
        "UTRANULARFCNCFGIND",
        "UTRANVERSION"
    FROM
    huawei_nbi_lte."UTRANNFREQ"

    """
)

VLANMAP = ReplaceableObject(
    'huawei_cm_4g."VLANMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "MASK",
        "NEXTHOPIP",
        "SETPRIO",
        "VLANID",
        "VLANMODE",
        "VRFIDX"
    FROM
    huawei_nbi_lte."VLANMAP"

    """
)

VQMALGO = ReplaceableObject(
    'huawei_cm_4g."VQMALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ULDELAYJITTER"
    FROM
    huawei_nbi_lte."VQMALGO"

    """
)

VRF = ReplaceableObject(
    'huawei_cm_4g."VRF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "VRFIDX"
    FROM
    huawei_nbi_lte."VRF"

    """
)

X2 = ReplaceableObject(
    'huawei_cm_4g."X2"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "CNOPSHARINGGROUPID",
        "CPEPGROUPID",
        "EPGROUPCFGFLAG",
        "TARGETENODEBRELEASE",
        "UPEPGROUPID",
        "X2ID",
        "USERLABEL"
    FROM
    huawei_nbi_lte."X2"

    """
)

X2BLACKWHITELIST = ReplaceableObject(
    'huawei_cm_4g."X2BLACKWHITELIST"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENODEBID",
        "MCC",
        "MNC",
        "X2LISTTYPE"
    FROM
    huawei_nbi_lte."X2BLACKWHITELIST"

    """
)

X2INTERFACE = ReplaceableObject(
    'huawei_cm_4g."X2INTERFACE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORID",
        "CNOPSHARINGGROUPID",
        "CTRLMODE",
        "NOAUTORMVFLAG",
        "TARGETENODEBRELEASE",
        "X2CPBEARERID",
        "X2INTERFACEID"
    FROM
    huawei_nbi_lte."X2INTERFACE"

    """
)


def upgrade():
    op.create_view(ALGODEFAULTPARA)
    op.create_view(ANR)
    op.create_view(APPCERT)
    op.create_view(BASEBANDEQM)
    op.create_view(BASEBANDEQMBOARDREF)
    op.create_view(BCCHCFG)
    op.create_view(BFMIMOADAPTIVEPARACFG)
    op.create_view(CAMGTCFG)
    op.create_view(CELL)
    op.create_view(CELLACBAR)
    op.create_view(CELLACCESS)
    op.create_view(CELLALGOSWITCH)
    op.create_view(CELLBF)
    op.create_view(CELLBFMIMOPARACFG)
    op.create_view(CELLCHPWRCFG)
    op.create_view(CELLCSPCPARA)
    op.create_view(CELLDLCOMPALGO)
    op.create_view(CELLDLICIC)
    op.create_view(CELLDLICICMCPARA)
    op.create_view(CELLDLPCPDCCH)
    op.create_view(CELLDLPCPDSCH)
    op.create_view(CELLDLPCPDSCHPA)
    op.create_view(CELLDLPCPHICH)
    op.create_view(CELLDLSCHALGO)
    op.create_view(CELLDRXPARA)
    op.create_view(CELLDSS)
    op.create_view(CELLDYNACBARALGOPARA)
    op.create_view(CELLHOPARACFG)
    op.create_view(CELLIDPRDUPT)
    op.create_view(CELLLOWPOWER)
    op.create_view(CELLMBMSCFG)
    op.create_view(CELLMCPARA)
    op.create_view(CELLMIMOPARACFG)
    op.create_view(CELLMLB)
    op.create_view(CELLMLBHO)
    op.create_view(CELLMRO)
    op.create_view(CELLNOACCESSALMPARA)
    op.create_view(CELLOP)
    op.create_view(CELLPCALGO)
    op.create_view(CELLPDCCHALGO)
    op.create_view(CELLPUCCHALGO)
    op.create_view(CELLRACHALGO)
    op.create_view(CELLRACTHD)
    op.create_view(CELLRESEL)
    op.create_view(CELLRESELGERAN)
    op.create_view(CELLRESELUTRAN)
    op.create_view(CELLRFSHUTDOWN)
    op.create_view(CELLRICALGO)
    op.create_view(CELLSEL)
    op.create_view(CELLSERVICEDIFFCFG)
    op.create_view(CELLSHUTDOWN)
    op.create_view(CELLSIMAP)
    op.create_view(CELLSTANDARDQCI)
    op.create_view(CELLULCOMPALGO)
    op.create_view(CELLULICIC)
    op.create_view(CELLULICICMCPARA)
    op.create_view(CELLULPCCOMM)
    op.create_view(CELLULPCDEDIC)
    op.create_view(CELLULSCHALGO)
    op.create_view(CERTCHKTSK)
    op.create_view(CERTDEPLOY)
    op.create_view(CERTMK)
    op.create_view(CERTREQ)
    op.create_view(CNOPERATOR)
    op.create_view(CNOPERATORHOCFG)
    op.create_view(CNOPERATORIPPATH)
    op.create_view(CNOPERATORSTANDARDQCI)
    op.create_view(CNOPERATORTA)
    op.create_view(COUNTERCHECKPARA)
    op.create_view(CPBEARER)
    op.create_view(CQIADAPTIVECFG)
    op.create_view(CRLPOLICY)
    op.create_view(CSFALLBACKBLINDHOCFG)
    op.create_view(CSFALLBACKHO)
    op.create_view(CSFALLBACKPOLICYCFG)
    op.create_view(CSPCALGOPARA)
    op.create_view(DEVIP)
    op.create_view(DHCPRELAYSWITCH)
    op.create_view(DIFPRI)
    op.create_view(DISTBASEDHO)
    op.create_view(DRX)
    op.create_view(DRXPARAGROUP)
    op.create_view(DSCPMAP)
    op.create_view(EMC)
    op.create_view(ENODEBALGOSWITCH)
    op.create_view(ENODEBAUTOPOWEROFF)
    op.create_view(ENODEBCIPHERCAP)
    op.create_view(ENODEBCONNSTATETIMER)
    op.create_view(ENODEBFUNCTION)
    op.create_view(ENODEBINTEGRITYCAP)
    op.create_view(ENODEBMLB)
    op.create_view(ENODEBPATH)
    op.create_view(ENODEBSHARINGMODE)
    op.create_view(EPGROUP)
    op.create_view(ETHPORT)
    op.create_view(EUCELLSECTOREQM)
    op.create_view(EUCOSCHCFG)
    op.create_view(EUTRANEXTERNALCELL)
    op.create_view(EUTRANINTRAFREQNCELL)
    op.create_view(FDDRESMODE)
    op.create_view(filefooter)
    op.create_view(GERANEXTERNALCELL)
    op.create_view(GERANINTERFCFG)
    op.create_view(GERANNCELL)
    op.create_view(GERANNFREQGROUP)
    op.create_view(GERANNFREQGROUPARFCN)
    op.create_view(GLOBALPROCSWITCH)
    op.create_view(GTPU)
    op.create_view(GTRANSPARA)
    op.create_view(HOMEASCOMM)
    op.create_view(IKECFG)
    op.create_view(INTERFREQHOGROUP)
    op.create_view(INTERRATCELLSHUTDOWN)
    op.create_view(INTERRATHOCDMA1XRTTGROUP)
    op.create_view(INTERRATHOCDMAHRPDGROUP)
    op.create_view(INTERRATHOCOMM)
    op.create_view(INTERRATHOCOMMGROUP)
    op.create_view(INTERRATHOGERANGROUP)
    op.create_view(INTERRATHOUTRANGROUP)
    op.create_view(INTERRATPOLICYCFGGROUP)
    op.create_view(INTRAFREQHOGROUP)
    op.create_view(INTRARATHOCOMM)
    op.create_view(IPGUARD)
    op.create_view(IPPATH)
    op.create_view(IPRT)
    op.create_view(LOCATION)
    op.create_view(MIMOADAPTIVEPARACFG)
    op.create_view(MMEFEATURECFG)
    op.create_view(MRO)
    op.create_view(NE)
    op.create_view(NODE)
    op.create_view(OMCH)
    op.create_view(PCCHCFG)
    op.create_view(PDCPROHCPARA)
    op.create_view(PDSCHCFG)
    op.create_view(PHICHCFG)
    op.create_view(PUCCHCFG)
    op.create_view(PUSCHCFG)
    op.create_view(PUSCHPARAM)
    op.create_view(RACHCFG)
    op.create_view(RET)
    op.create_view(RETDEVICEDATA)
    op.create_view(RETSUBUNIT)
    op.create_view(RLCPDCPPARAGROUP)
    op.create_view(RRCCONNSTATETIMER)
    op.create_view(RRUJOINTCALPARACFG)
    op.create_view(S1)
    op.create_view(S1INTERFACE)
    op.create_view(S1REESTTIMER)
    op.create_view(SCTPHOST)
    op.create_view(SCTPHOSTREF)
    op.create_view(SCTPLNK)
    op.create_view(SCTPPEER)
    op.create_view(SCTPPEERREF)
    op.create_view(SECTOR)
    op.create_view(SECTORANTENNAREF)
    op.create_view(SECTOREQM)
    op.create_view(SECTOREQMANTENNAREF)
    op.create_view(SERVICEIFDLEARFCNGRP)
    op.create_view(SERVICEIFHOCFGGROUP)
    op.create_view(SERVICEIRHOCFGGROUP)
    op.create_view(SIMULOAD)
    op.create_view(SRSADAPTIVECFG)
    op.create_view(SRSCFG)
    op.create_view(STANDARDQCI)
    op.create_view(SUBSESSION_NE)
    op.create_view(TACALG)
    op.create_view(TCEIPMAPPING)
    op.create_view(TCPACKCTRLALGO)
    op.create_view(TCPACKLIMITALG)
    op.create_view(TCPMSSCTRL)
    op.create_view(TDDFRAMEOFFSET)
    op.create_view(TDDRESMODESWITCH)
    op.create_view(TIMEALIGNMENTTIMER)
    op.create_view(TOLCALG)
    op.create_view(TPEALGO)
    op.create_view(TRUSTCERT)
    op.create_view(TYPDRBBSR)
    op.create_view(UDT)
    op.create_view(UDTPARAGRP)
    op.create_view(UETIMERCONST)
    op.create_view(USERPLANEHOST)
    op.create_view(USERPLANEHOSTREF)
    op.create_view(USERPLANEPEER)
    op.create_view(USERPLANEPEERREF)
    op.create_view(UTRANEXTERNALCELL)
    op.create_view(UTRANNCELL)
    op.create_view(UTRANNFREQ)
    op.create_view(VLANMAP)
    op.create_view(VQMALGO)
    op.create_view(VRF)
    op.create_view(X2)
    op.create_view(X2BLACKWHITELIST)
    op.create_view(X2INTERFACE)


def downgrade():
    op.drop_view(ALGODEFAULTPARA)
    op.drop_view(ANR)
    op.drop_view(APPCERT)
    op.drop_view(BASEBANDEQM)
    op.drop_view(BASEBANDEQMBOARDREF)
    op.drop_view(BCCHCFG)
    op.drop_view(BFMIMOADAPTIVEPARACFG)
    op.drop_view(CAMGTCFG)
    op.drop_view(CELL)
    op.drop_view(CELLACBAR)
    op.drop_view(CELLACCESS)
    op.drop_view(CELLALGOSWITCH)
    op.drop_view(CELLBF)
    op.drop_view(CELLBFMIMOPARACFG)
    op.drop_view(CELLCHPWRCFG)
    op.drop_view(CELLCSPCPARA)
    op.drop_view(CELLDLCOMPALGO)
    op.drop_view(CELLDLICIC)
    op.drop_view(CELLDLICICMCPARA)
    op.drop_view(CELLDLPCPDCCH)
    op.drop_view(CELLDLPCPDSCH)
    op.drop_view(CELLDLPCPDSCHPA)
    op.drop_view(CELLDLPCPHICH)
    op.drop_view(CELLDLSCHALGO)
    op.drop_view(CELLDRXPARA)
    op.drop_view(CELLDSS)
    op.drop_view(CELLDYNACBARALGOPARA)
    op.drop_view(CELLHOPARACFG)
    op.drop_view(CELLIDPRDUPT)
    op.drop_view(CELLLOWPOWER)
    op.drop_view(CELLMBMSCFG)
    op.drop_view(CELLMCPARA)
    op.drop_view(CELLMIMOPARACFG)
    op.drop_view(CELLMLB)
    op.drop_view(CELLMLBHO)
    op.drop_view(CELLMRO)
    op.drop_view(CELLNOACCESSALMPARA)
    op.drop_view(CELLOP)
    op.drop_view(CELLPCALGO)
    op.drop_view(CELLPDCCHALGO)
    op.drop_view(CELLPUCCHALGO)
    op.drop_view(CELLRACHALGO)
    op.drop_view(CELLRACTHD)
    op.drop_view(CELLRESEL)
    op.drop_view(CELLRESELGERAN)
    op.drop_view(CELLRESELUTRAN)
    op.drop_view(CELLRFSHUTDOWN)
    op.drop_view(CELLRICALGO)
    op.drop_view(CELLSEL)
    op.drop_view(CELLSERVICEDIFFCFG)
    op.drop_view(CELLSHUTDOWN)
    op.drop_view(CELLSIMAP)
    op.drop_view(CELLSTANDARDQCI)
    op.drop_view(CELLULCOMPALGO)
    op.drop_view(CELLULICIC)
    op.drop_view(CELLULICICMCPARA)
    op.drop_view(CELLULPCCOMM)
    op.drop_view(CELLULPCDEDIC)
    op.drop_view(CELLULSCHALGO)
    op.drop_view(CERTCHKTSK)
    op.drop_view(CERTDEPLOY)
    op.drop_view(CERTMK)
    op.drop_view(CERTREQ)
    op.drop_view(CNOPERATOR)
    op.drop_view(CNOPERATORHOCFG)
    op.drop_view(CNOPERATORIPPATH)
    op.drop_view(CNOPERATORSTANDARDQCI)
    op.drop_view(CNOPERATORTA)
    op.drop_view(COUNTERCHECKPARA)
    op.drop_view(CPBEARER)
    op.drop_view(CQIADAPTIVECFG)
    op.drop_view(CRLPOLICY)
    op.drop_view(CSFALLBACKBLINDHOCFG)
    op.drop_view(CSFALLBACKHO)
    op.drop_view(CSFALLBACKPOLICYCFG)
    op.drop_view(CSPCALGOPARA)
    op.drop_view(DEVIP)
    op.drop_view(DHCPRELAYSWITCH)
    op.drop_view(DIFPRI)
    op.drop_view(DISTBASEDHO)
    op.drop_view(DRX)
    op.drop_view(DRXPARAGROUP)
    op.drop_view(DSCPMAP)
    op.drop_view(EMC)
    op.drop_view(ENODEBALGOSWITCH)
    op.drop_view(ENODEBAUTOPOWEROFF)
    op.drop_view(ENODEBCIPHERCAP)
    op.drop_view(ENODEBCONNSTATETIMER)
    op.drop_view(ENODEBFUNCTION)
    op.drop_view(ENODEBINTEGRITYCAP)
    op.drop_view(ENODEBMLB)
    op.drop_view(ENODEBPATH)
    op.drop_view(ENODEBSHARINGMODE)
    op.drop_view(EPGROUP)
    op.drop_view(ETHPORT)
    op.drop_view(EUCELLSECTOREQM)
    op.drop_view(EUCOSCHCFG)
    op.drop_view(EUTRANEXTERNALCELL)
    op.drop_view(EUTRANINTRAFREQNCELL)
    op.drop_view(FDDRESMODE)
    op.drop_view(filefooter)
    op.drop_view(GERANEXTERNALCELL)
    op.drop_view(GERANINTERFCFG)
    op.drop_view(GERANNCELL)
    op.drop_view(GERANNFREQGROUP)
    op.drop_view(GERANNFREQGROUPARFCN)
    op.drop_view(GLOBALPROCSWITCH)
    op.drop_view(GTPU)
    op.drop_view(GTRANSPARA)
    op.drop_view(HOMEASCOMM)
    op.drop_view(IKECFG)
    op.drop_view(INTERFREQHOGROUP)
    op.drop_view(INTERRATCELLSHUTDOWN)
    op.drop_view(INTERRATHOCDMA1XRTTGROUP)
    op.drop_view(INTERRATHOCDMAHRPDGROUP)
    op.drop_view(INTERRATHOCOMM)
    op.drop_view(INTERRATHOCOMMGROUP)
    op.drop_view(INTERRATHOGERANGROUP)
    op.drop_view(INTERRATHOUTRANGROUP)
    op.drop_view(INTERRATPOLICYCFGGROUP)
    op.drop_view(INTRAFREQHOGROUP)
    op.drop_view(INTRARATHOCOMM)
    op.drop_view(IPGUARD)
    op.drop_view(IPPATH)
    op.drop_view(IPRT)
    op.drop_view(LOCATION)
    op.drop_view(MIMOADAPTIVEPARACFG)
    op.drop_view(MMEFEATURECFG)
    op.drop_view(MRO)
    op.drop_view(NE)
    op.drop_view(NODE)
    op.drop_view(OMCH)
    op.drop_view(PCCHCFG)
    op.drop_view(PDCPROHCPARA)
    op.drop_view(PDSCHCFG)
    op.drop_view(PHICHCFG)
    op.drop_view(PUCCHCFG)
    op.drop_view(PUSCHCFG)
    op.drop_view(PUSCHPARAM)
    op.drop_view(RACHCFG)
    op.drop_view(RET)
    op.drop_view(RETDEVICEDATA)
    op.drop_view(RETSUBUNIT)
    op.drop_view(RLCPDCPPARAGROUP)
    op.drop_view(RRCCONNSTATETIMER)
    op.drop_view(RRUJOINTCALPARACFG)
    op.drop_view(S1)
    op.drop_view(S1INTERFACE)
    op.drop_view(S1REESTTIMER)
    op.drop_view(SCTPHOST)
    op.drop_view(SCTPHOSTREF)
    op.drop_view(SCTPLNK)
    op.drop_view(SCTPPEER)
    op.drop_view(SCTPPEERREF)
    op.drop_view(SECTOR)
    op.drop_view(SECTORANTENNAREF)
    op.drop_view(SECTOREQM)
    op.drop_view(SECTOREQMANTENNAREF)
    op.drop_view(SERVICEIFDLEARFCNGRP)
    op.drop_view(SERVICEIFHOCFGGROUP)
    op.drop_view(SERVICEIRHOCFGGROUP)
    op.drop_view(SIMULOAD)
    op.drop_view(SRSADAPTIVECFG)
    op.drop_view(SRSCFG)
    op.drop_view(STANDARDQCI)
    op.drop_view(SUBSESSION_NE)
    op.drop_view(TACALG)
    op.drop_view(TCEIPMAPPING)
    op.drop_view(TCPACKCTRLALGO)
    op.drop_view(TCPACKLIMITALG)
    op.drop_view(TCPMSSCTRL)
    op.drop_view(TDDFRAMEOFFSET)
    op.drop_view(TDDRESMODESWITCH)
    op.drop_view(TIMEALIGNMENTTIMER)
    op.drop_view(TOLCALG)
    op.drop_view(TPEALGO)
    op.drop_view(TRUSTCERT)
    op.drop_view(TYPDRBBSR)
    op.drop_view(UDT)
    op.drop_view(UDTPARAGRP)
    op.drop_view(UETIMERCONST)
    op.drop_view(USERPLANEHOST)
    op.drop_view(USERPLANEHOSTREF)
    op.drop_view(USERPLANEPEER)
    op.drop_view(USERPLANEPEERREF)
    op.drop_view(UTRANEXTERNALCELL)
    op.drop_view(UTRANNCELL)
    op.drop_view(UTRANNFREQ)
    op.drop_view(VLANMAP)
    op.drop_view(VQMALGO)
    op.drop_view(VRF)
    op.drop_view(X2)
    op.drop_view(X2BLACKWHITELIST)
    op.drop_view(X2INTERFACE)