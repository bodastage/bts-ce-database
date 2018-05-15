"""Create MO views for Huawei 3G

Revision ID: 316570e7ecab
Revises: 3c732365be0f
Create Date: 2018-05-15 10:32:15.099000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '316570e7ecab'
down_revision = '3c732365be0f'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext

AAL2PATH = ReplaceableObject(
    'huawei_cm_3g."AAL2PATH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AAL2PATHT",
        "ANI",
        "CARRYF",
        "CARRYNCOPTN",
        "CARRYSN",
        "CARRYT",
        "OWNERSHIP",
        "PATHID",
        "REMARK",
        "RXTRFX",
        "TIMERCU",
        "TRMLOADTHINDEX",
        "TXTRFX",
        "VCI",
        "VPI"
    FROM
    huawei_nbi_umts."AAL2PATH"

    """
)

AAL2TMR = ReplaceableObject(
    'huawei_cm_3g."AAL2TMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLOREQTMR",
        "ESTINDTMR",
        "ESTREQTMR",
        "MODINDTMR",
        "MODREQTMR",
        "RELINDTMR",
        "RELREQTMR",
        "RESREQTMR",
        "UBLREQTMR"
    FROM
    huawei_nbi_umts."AAL2TMR"

    """
)

ADJMAP = ReplaceableObject(
    'huawei_cm_3g."ADJMAP"',
    """

    SELECT 
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
        "TMIBRZ",
        "TMIGLD",
        "TMISLV",
        "TRANST"
    FROM
    huawei_nbi_umts."ADJMAP"

    """
)

ADJNODE = ReplaceableObject(
    'huawei_cm_3g."ADJNODE"',
    """

    SELECT 
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
        "CHECKCOUNT",
        "CNMNGMODE",
        "DSCP",
        "IPPOOLINDEX",
        "LOGICRNCID",
        "NAME",
        "NODEBID",
        "NODET",
        "PERIOD",
        "PINGCHKT",
        "PINGPKGLEN",
        "PINGSWITCH",
        "RXBW",
        "TRANST",
        "TRMLOADTHINDEX",
        "TXBW",
        "ISROOTNODE",
        "QAAL2VER",
        "SAALLNKN"
    FROM
    huawei_nbi_umts."ADJNODE"

    """
)

ATMTRF = ReplaceableObject(
    'huawei_cm_3g."ATMTRF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CDVT",
        "MCR",
        "PCR",
        "REMARK",
        "ST",
        "TRFX",
        "UT",
        "MBS",
        "SCR"
    FROM
    huawei_nbi_umts."ATMTRF"

    """
)

CELLCBS = ReplaceableObject(
    'huawei_cm_3g."CELLCBS"',
    """

    SELECT 
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
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."CELLCBS"

    """
)

CELLERACH = ReplaceableObject(
    'huawei_cm_3g."CELLERACH"',
    """

    SELECT 
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
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."CELLERACH"

    """
)

CELLMIMO = ReplaceableObject(
    'huawei_cm_3g."CELLMIMO"',
    """

    SELECT 
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
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."CELLMIMO"

    """
)

CELLTEMPLATERSC = ReplaceableObject(
    'huawei_cm_3g."CELLTEMPLATERSC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "NAME"
    FROM
    huawei_nbi_umts."CELLTEMPLATERSC"

    """
)

DEVIP = ReplaceableObject(
    'huawei_cm_3g."DEVIP"',
    """

    SELECT 
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
        "MASK",
        "MTU",
        "REMARK",
        "SN",
        "SRN"
    FROM
    huawei_nbi_umts."DEVIP"

    """
)

EMSIP = ReplaceableObject(
    'huawei_cm_3g."EMSIP"',
    """

    SELECT 
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
    huawei_nbi_umts."EMSIP"

    """
)

ETHIP = ReplaceableObject(
    'huawei_cm_3g."ETHIP"',
    """

    SELECT 
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
    huawei_nbi_umts."ETHIP"

    """
)

ETHPORT = ReplaceableObject(
    'huawei_cm_3g."ETHPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BCPKTALARMCLRTHD",
        "BCPKTALARMTHD",
        "BRDTYPE",
        "CFMVER",
        "ERRALARMTHD",
        "ERRDETECTSW",
        "FC",
        "FCINDEX",
        "FLOWCTRLSWITCH",
        "MTU",
        "OAMFLOWBW",
        "PN",
        "REMARK",
        "SN",
        "SRN",
        "AUTO"
    FROM
    huawei_nbi_umts."ETHPORT"

    """
)

ETHTRK = ReplaceableObject(
    'huawei_cm_3g."ETHTRK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CFMVER",
        "FCINDEX",
        "FLOWCTRLSWITCH",
        "LACPMODE",
        "MTU",
        "OAMFLOWBW",
        "RT",
        "SN",
        "SRN",
        "SYSPRI",
        "TRKN",
        "WORKMODE"
    FROM
    huawei_nbi_umts."ETHTRK"

    """
)

ETHTRKIP = ReplaceableObject(
    'huawei_cm_3g."ETHTRKIP"',
    """

    SELECT 
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
        "SN",
        "SRN",
        "TRKN"
    FROM
    huawei_nbi_umts."ETHTRKIP"

    """
)

ETHTRKLNK = ReplaceableObject(
    'huawei_cm_3g."ETHTRKLNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "PORTPRI",
        "SN",
        "SRN",
        "TRKLNKPN",
        "TRKLNKSN",
        "TRKN",
        "WORKMODE"
    FROM
    huawei_nbi_umts."ETHTRKLNK"

    """
)

filefooter = ReplaceableObject(
    'huawei_cm_3g."FILEFOOTER"',
    """

    SELECT 
        "FileName",
        "datetime"
    FROM
    huawei_nbi_umts."filefooter"

    """
)

IPOAPVC = ReplaceableObject(
    'huawei_cm_3g."IPOAPVC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CARRYNCOPTN",
        "CARRYT",
        "CARRYVCI",
        "CARRYVPI",
        "IPADDR",
        "PEERIPADDR",
        "PEERT",
        "REMARK",
        "RXTRFX",
        "TXTRFX"
    FROM
    huawei_nbi_umts."IPOAPVC"

    """
)

IPPOOL = ReplaceableObject(
    'huawei_cm_3g."IPPOOL"',
    """

    SELECT 
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
        "IPPOOLINDEX",
        "IPPOOLNAME"
    FROM
    huawei_nbi_umts."IPPOOL"

    """
)

IPPOOLIP = ReplaceableObject(
    'huawei_cm_3g."IPPOOLIP"',
    """

    SELECT 
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
        "IPPOOLINDEX",
        "SN",
        "SRN"
    FROM
    huawei_nbi_umts."IPPOOLIP"

    """
)

IPPOOLPM = ReplaceableObject(
    'huawei_cm_3g."IPPOOLPM"',
    """

    SELECT 
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
        "DR",
        "ITFT",
        "PHB",
        "SIPTYPE"
    FROM
    huawei_nbi_umts."IPPOOLPM"

    """
)

IPRT = ReplaceableObject(
    'huawei_cm_3g."IPRT"',
    """

    SELECT 
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
    huawei_nbi_umts."IPRT"

    """
)

IU_ADJMAP = ReplaceableObject(
    'huawei_cm_3g."IU_ADJMAP"',
    """

    SELECT 
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
        "TMIBRZ",
        "TMIGLD",
        "TMISLV"
    FROM
    huawei_nbi_umts."IU_ADJMAP"

    """
)

IU_ADJNODE = ReplaceableObject(
    'huawei_cm_3g."IU_ADJNODE"',
    """

    SELECT 
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
        "CHECKCOUNT",
        "CNMNGMODE",
        "DSCP",
        "IPPOOLINDEX",
        "LOGICRNCSHAREMODE",
        "NAME",
        "NODET",
        "PERIOD",
        "PINGPKGLEN",
        "PINGSWITCH",
        "TRANST",
        "DPX"
    FROM
    huawei_nbi_umts."IU_ADJNODE"

    """
)

M3DE = ReplaceableObject(
    'huawei_cm_3g."M3DE"',
    """

    SELECT 
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
    huawei_nbi_umts."M3DE"

    """
)

M3LE = ReplaceableObject(
    'huawei_cm_3g."M3LE"',
    """

    SELECT 
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
    huawei_nbi_umts."M3LE"

    """
)

M3LKS = ReplaceableObject(
    'huawei_cm_3g."M3LKS"',
    """

    SELECT 
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
        "MULTIRCSW",
        "NAME",
        "PDTMRVALUE",
        "SIGLKSX",
        "TRAMODE",
        "WKMODE"
    FROM
    huawei_nbi_umts."M3LKS"

    """
)

M3LNK = ReplaceableObject(
    'huawei_cm_3g."M3LNK"',
    """

    SELECT 
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
        "SIGLKSX",
        "SIGLNKID"
    FROM
    huawei_nbi_umts."M3LNK"

    """
)

M3RT = ReplaceableObject(
    'huawei_cm_3g."M3RT"',
    """

    SELECT 
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
    huawei_nbi_umts."M3RT"

    """
)

MSP = ReplaceableObject(
    'huawei_cm_3g."MSP"',
    """

    SELECT 
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
    huawei_nbi_umts."MSP"

    """
)

MTP3TMR = ReplaceableObject(
    'huawei_cm_3g."MTP3TMR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SAALTMR",
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
    huawei_nbi_umts."MTP3TMR"

    """
)

N7DPC = ReplaceableObject(
    'huawei_cm_3g."N7DPC"',
    """

    SELECT 
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
        "STP"
    FROM
    huawei_nbi_umts."N7DPC"

    """
)

NODEBEQUIPMENT = ReplaceableObject(
    'huawei_cm_3g."NODEBEQUIPMENT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "NODEBID",
        "NODEBNAME",
        "SERIES",
        "TEMPLATENAME",
        "VERSION"
    FROM
    huawei_nbi_umts."NODEBEQUIPMENT"

    """
)

NODEBTEMPLATERSC = ReplaceableObject(
    'huawei_cm_3g."NODEBTEMPLATERSC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SERIES",
        "TEMPLATENAME",
        "VERSION"
    FROM
    huawei_nbi_umts."NODEBTEMPLATERSC"

    """
)

OPC = ReplaceableObject(
    'huawei_cm_3g."OPC"',
    """

    SELECT 
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
    huawei_nbi_umts."OPC"

    """
)

OPT = ReplaceableObject(
    'huawei_cm_3g."OPT"',
    """

    SELECT 
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
        "FCINDEX",
        "FLOWCTRLSWITCH",
        "J0TYPE",
        "J1TYPE",
        "JAUTOADD",
        "OPTM",
        "PN",
        "PS",
        "S1VALUE",
        "SCRAMBLESW",
        "SN",
        "SRN",
        "WORKTYPE",
        "J0BYTE_FORMAT",
        "J0RXVALUE",
        "J0TXVALUE",
        "J1BYTE_FORMAT",
        "J1RXVALUE",
        "J1TXVALUE"
    FROM
    huawei_nbi_umts."OPT"

    """
)

PHBMAP = ReplaceableObject(
    'huawei_cm_3g."PHBMAP"',
    """

    SELECT 
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
    huawei_nbi_umts."PHBMAP"

    """
)

PORTFLOWCTRLPARA = ReplaceableObject(
    'huawei_cm_3g."PORTFLOWCTRLPARA"',
    """

    SELECT 
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
    huawei_nbi_umts."PORTFLOWCTRLPARA"

    """
)

QUEUEMAP = ReplaceableObject(
    'huawei_cm_3g."QUEUEMAP"',
    """

    SELECT 
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
    huawei_nbi_umts."QUEUEMAP"

    """
)

SAALLNK = ReplaceableObject(
    'huawei_cm_3g."SAALLNK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CARRYNCOPTN",
        "CARRYSN",
        "CARRYSRN",
        "CARRYT",
        "CARRYVCI",
        "CARRYVPI",
        "CCTMR",
        "IDLETMR",
        "KEEPTMR",
        "MAXCC",
        "MAXPD",
        "POLLTMR",
        "RSPTMR",
        "RXTRFX",
        "SAALLNKN",
        "SAALLNKT",
        "STATLEN",
        "TXTRFX",
        "WINDOWSIZE"
    FROM
    huawei_nbi_umts."SAALLNK"

    """
)

SCCPTMR = ReplaceableObject(
    'huawei_cm_3g."SCCPTMR"',
    """

    SELECT 
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
    huawei_nbi_umts."SCCPTMR"

    """
)

SCTPLNK = ReplaceableObject(
    'huawei_cm_3g."SCTPLNK"',
    """

    SELECT 
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
        "CMEMODE",
        "CROSSIPFLAG",
        "DSCP",
        "HBINTER",
        "LOCIP1",
        "LOCIP2",
        "LOGPORTFLAG",
        "MAXASSOCRETR",
        "MAXPATHRETR",
        "MTU",
        "PEERIP1",
        "PEERIP2",
        "PEERPN",
        "REMARK",
        "RTOALPHA",
        "RTOBETA",
        "RTOINIT",
        "RTOMAX",
        "RTOMIN",
        "SCTPLNKID",
        "SWITCHBACKFLAG",
        "SWITCHBACKHBNUM",
        "TSACK",
        "LOCIPDISTTYPE",
        "LOCPN"
    FROM
    huawei_nbi_umts."SCTPLNK"

    """
)

SCTPSRVPORT = ReplaceableObject(
    'huawei_cm_3g."SCTPSRVPORT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BBAPSRVPN",
        "M3UASRVPN",
        "NBAPSRVPN"
    FROM
    huawei_nbi_umts."SCTPSRVPORT"

    """
)

SRCIPRT = ReplaceableObject(
    'huawei_cm_3g."SRCIPRT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPTYPE",
        "NEXTHOP",
        "REMARK",
        "SN",
        "SRCIPADDR",
        "SRN",
        "STANDBYNEXTHOPSWITCH"
    FROM
    huawei_nbi_umts."SRCIPRT"

    """
)

SUBSESSION_NE = ReplaceableObject(
    'huawei_cm_3g."SUBSESSION_NE"',
    """

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
    huawei_nbi_umts."SUBSESSION_NE"

    """
)

SYS = ReplaceableObject(
    'huawei_cm_3g."SYS"',
    """

    SELECT 
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
    huawei_nbi_umts."SYS"

    """
)

TRMFACTOR = ReplaceableObject(
    'huawei_cm_3g."TRMFACTOR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSCONVDL",
        "CSCONVUL",
        "CSSTRMDL",
        "CSSTRMUL",
        "EFACHDL",
        "EPCHDL",
        "ERACHUL",
        "FTI",
        "GENCCHDL",
        "GENCCHUL",
        "HDBKGDL",
        "HDCONVDL",
        "HDINTERDL",
        "HDSIPDL",
        "HDSRBDL",
        "HDSTRMDL",
        "HDVOICEDL",
        "HUBKGUL",
        "HUCONVUL",
        "HUINTERUL",
        "HUSIPUL",
        "HUSRBUL",
        "HUSTRMUL",
        "HUVOICEUL",
        "PSBKGDL",
        "PSBKGUL",
        "PSCONVDL",
        "PSCONVUL",
        "PSINTERDL",
        "PSINTERUL",
        "PSSTRMDL",
        "PSSTRMUL",
        "REMARK",
        "SIPDL",
        "SIPUL",
        "SRBDL",
        "SRBUL",
        "VOICEDL",
        "VOICEUL"
    FROM
    huawei_nbi_umts."TRMFACTOR"

    """
)

TRMLOADTH = ReplaceableObject(
    'huawei_cm_3g."TRMLOADTH"',
    """

    SELECT 
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
        "FWDRESVHOTH"
    FROM
    huawei_nbi_umts."TRMLOADTH"

    """
)

TRMMAP = ReplaceableObject(
    'huawei_cm_3g."TRMMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CCHPRIPRI",
        "CCHSECPRI",
        "CSCONVPRIPRI",
        "CSCONVSECPRI",
        "CSSTRMPRIPRI",
        "CSSTRMSECPRI",
        "HDBKGPRIPRI",
        "HDBKGSECPRI",
        "HDCONVPRIPRI",
        "HDCONVSECPRI",
        "HDINTHGHPRIPRI",
        "HDINTHGHSECPRI",
        "HDINTLOWPRIPRI",
        "HDINTLOWSECPRI",
        "HDINTMIDPRIPRI",
        "HDINTMIDSECPRI",
        "HDSIPPRIPRI",
        "HDSIPSECPRI",
        "HDSRBPRIPRI",
        "HDSRBSECPRI",
        "HDSTRMPRIPRI",
        "HDSTRMSECPRI",
        "HDVOICEPRIPRI",
        "HDVOICESECPRI",
        "HUBKGPRIPRI",
        "HUBKGSECPRI",
        "HUCONVPRIPRI",
        "HUCONVSECPRI",
        "HUINTHGHPRIPRI",
        "HUINTHGHSECPRI",
        "HUINTLOWPRIPRI",
        "HUINTLOWSECPRI",
        "HUINTMIDPRIPRI",
        "HUINTMIDSECPRI",
        "HUSIPPRIPRI",
        "HUSIPSECPRI",
        "HUSRBPRIPRI",
        "HUSRBSECPRI",
        "HUSTRMPRIPRI",
        "HUSTRMSECPRI",
        "HUVOICEPRIPRI",
        "HUVOICESECPRI",
        "ITFT",
        "PSBKGPRIPRI",
        "PSBKGSECPRI",
        "PSCONVPRIPRI",
        "PSCONVSECPRI",
        "PSINTHGHPRIPRI",
        "PSINTHGHSECPRI",
        "PSINTLOWPRIPRI",
        "PSINTLOWSECPRI",
        "PSINTMIDPRIPRI",
        "PSINTMIDSECPRI",
        "PSSTRMPRIPRI",
        "PSSTRMSECPRI",
        "REMARK",
        "SIPPRIPRI",
        "SIPSECPRI",
        "SRBPRIPRI",
        "SRBSECPRI",
        "TMI",
        "TRANST",
        "VOICEPRIPRI",
        "VOICESECPRI"
    FROM
    huawei_nbi_umts."TRMMAP"

    """
)

U2GNCELL = ReplaceableObject(
    'huawei_cm_3g."U2GNCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHOFLAG",
        "CELLID",
        "CIOOFFSET",
        "DRDECN0THRESHHOLD",
        "GSMCELLINDEX",
        "HOPRIO",
        "INTERRATADJSQHCS",
        "MBDRFLAG",
        "MBDRPRIO",
        "NIRATOVERLAP",
        "NPRIO",
        "NPRIOFLAG",
        "QOFFSET1SN",
        "QRXLEVMIN",
        "RNCID",
        "SIB11IND",
        "SIB12IND",
        "SRVCCSWITCH",
        "TEMPOFFSET1",
        "TPENALTYHCSRESELECT",
        "U2GNCELLSRC"
    FROM
    huawei_nbi_umts."U2GNCELL"

    """
)

UACALGO = ReplaceableObject(
    'huawei_cm_3g."UACALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACRSTRCTSWITCH",
        "IUACINTERVALOFCELL"
    FROM
    huawei_nbi_umts."UACALGO"

    """
)

UADAPALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UADAPALGOSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADAPSTETRSPARONDATATRSSW",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UADAPALGOSWITCH"

    """
)

UADMCTRL = ReplaceableObject(
    'huawei_cm_3g."UADMCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AFSETOBJ",
        "DLSRBACTFACTOR",
        "LOGICRNCID",
        "ULSRBACTFACTOR",
        "DLAMRCONVAF",
        "DLBACKGROUNDAF",
        "DLINTERACTAF",
        "DLNONAMRCONVAF",
        "DLSTREAMAF",
        "HSDPABACKGROUNDAF",
        "HSDPACONVAF",
        "HSDPAINTERACTAF",
        "HSDPASTREAMAF",
        "HSUPABACKGROUNDAF",
        "HSUPACONVAF",
        "HSUPAINTERACTAF",
        "HSUPASTREAMAF",
        "ULAMRCONVAF",
        "ULBACKGROUNDAF",
        "ULINTERACTAF",
        "ULNONAMRCONVAF",
        "ULSTREAMAF"
    FROM
    huawei_nbi_umts."UADMCTRL"

    """
)

UAICH = ReplaceableObject(
    'huawei_cm_3g."UAICH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AICHTXTIMING",
        "CELLID",
        "LOGICRNCID",
        "PRACHPHYCHID",
        "STTDIND",
        "UAICHPHYCHID"
    FROM
    huawei_nbi_umts."UAICH"

    """
)

UAMRC = ReplaceableObject(
    'huawei_cm_3g."UAMRC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COPPERMAXMODE",
        "DLMODECHANGETIMERLEN",
        "DLTHDE1",
        "DLTHDE2",
        "DLTHDF1",
        "DLTHDF2",
        "GOLDMAXMODE",
        "LOGICRNCID",
        "SILVERMAXMODE",
        "ULMODECHANGETIMERLEN"
    FROM
    huawei_nbi_umts."UAMRC"

    """
)

UAMRCWB = ReplaceableObject(
    'huawei_cm_3g."UAMRCWB"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COPPERMAXMODE",
        "DLMODECHANGETIMERLEN",
        "DLTHDE1",
        "DLTHDE2",
        "DLTHDF1",
        "DLTHDF2",
        "GOLDMAXMODE",
        "LOGICRNCID",
        "SILVERMAXMODE",
        "ULMODECHANGETIMERLEN"
    FROM
    huawei_nbi_umts."UAMRCWB"

    """
)

UBCH = ReplaceableObject(
    'huawei_cm_3g."UBCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BCHPOWER",
        "CELLID",
        "LOGICRNCID",
        "TRCHID"
    FROM
    huawei_nbi_umts."UBCH"

    """
)

UCACALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCACALGOSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CACSWITCH",
        "FACHUSERNUMRESERV",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCACALGOSWITCH"

    """
)

UCALLSHOCKCTRL = ReplaceableObject(
    'huawei_cm_3g."UCALLSHOCKCTRL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CALLSHOCKCTRLSWITCH",
        "CALLSHOCKJUDGEPERIOD",
        "CAPSFCBASEONCPUSWITCH",
        "CAPSFCCPURELTHD",
        "CAPSFCCPUTRIGTHD",
        "CELLAMRRRCNUM",
        "CELLHIGHPRIRRCNUM",
        "CELLTOTALRRCNUMTHD",
        "NBAMRRRCNUM",
        "NBHIGHPRIRRCNUM",
        "NBTOTALRRCNUMTHD",
        "REGBYFACHSWITCH",
        "RRCQUEUEFCSWITCH",
        "SYSAMRRRCNUM",
        "SYSHIGHPRIRRCNUM",
        "SYSRRCREJNUM",
        "SYSTOTALRRCNUMTHD"
    FROM
    huawei_nbi_umts."UCALLSHOCKCTRL"

    """
)

UCCP = ReplaceableObject(
    'huawei_cm_3g."UCCP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CARRYLNKT",
        "LOGICRNCID",
        "NODEBID",
        "PN",
        "SCTPLNKID",
        "SAALLNKN"
    FROM
    huawei_nbi_umts."UCCP"

    """
)

UCELL = ReplaceableObject(
    'huawei_cm_3g."UCELL"',
    """

    SELECT 
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
        "BANDIND",
        "BLKSTATUS",
        "CCHCNOPINDEX",
        "CELLHETFLAG",
        "CELLID",
        "CELLNAME",
        "CFGRACIND",
        "CIO",
        "CNOPGRPINDEX",
        "DPGID",
        "DSSFLAG",
        "DSSSMALLCOVMAXTXPOWER",
        "LAC",
        "LOCELL",
        "LOGICRNCID",
        "MAXTXPOWER",
        "NINSYNCIND",
        "NODEBNAME",
        "NOUTSYNCIND",
        "PSCRAMBCODE",
        "RAC",
        "SAC",
        "SPGID",
        "TCELL",
        "TRLFAILURE",
        "TXDIVERSITYIND",
        "UARFCNDOWNLINK",
        "UARFCNUPLINK",
        "UARFCNUPLINKIND",
        "VPLIMITIND"
    FROM
    huawei_nbi_umts."UCELL"

    """
)

UCELLACCESSSTRICT = ReplaceableObject(
    'huawei_cm_3g."UCELLACCESSSTRICT"',
    """

    SELECT 
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
        "CELLRESERVATIONEXTENSION",
        "CELLRESERVEDFOROPERATORUSE",
        "CONNCELLBARRED",
        "DOMAINTYPE",
        "IDLECELLBARRED",
        "ISACCESSCLASS0BARRED",
        "ISACCESSCLASS10BARRED",
        "ISACCESSCLASS11BARRED",
        "ISACCESSCLASS12BARRED",
        "ISACCESSCLASS13BARRED",
        "ISACCESSCLASS14BARRED",
        "ISACCESSCLASS15BARRED",
        "ISACCESSCLASS1BARRED",
        "ISACCESSCLASS2BARRED",
        "ISACCESSCLASS3BARRED",
        "ISACCESSCLASS4BARRED",
        "ISACCESSCLASS5BARRED",
        "ISACCESSCLASS6BARRED",
        "ISACCESSCLASS7BARRED",
        "ISACCESSCLASS8BARRED",
        "ISACCESSCLASS9BARRED",
        "LOGICRNCID",
        "IDLEINTRAFREQRESELECTION",
        "IDLETBARRED"
    FROM
    huawei_nbi_umts."UCELLACCESSSTRICT"

    """
)

UCELLALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCELLALGOSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADAPALGOSWITCH",
        "BERATEREDUCEONFAIRNESSSWITCH",
        "CELLCALLSHOCKSWITCH",
        "CELLCAPACITYAUTOHANDLESWITCH",
        "CELLID",
        "CELLMOCNDEMARCSWITCH",
        "CELLOMENHSWITCH",
        "CSRABCACOPTSWITCH",
        "DLPWRLDCUESELSWITCH",
        "HSPAENHSWITCH",
        "HSPAPLUSSWITCH",
        "LOGICRNCID",
        "NBMCACALGOSWITCH",
        "NBMCACALGOSWITCH2",
        "NBMDLCACALGOSELSWITCH",
        "NBMLDCALGOSWITCH",
        "NBMLDCIRATUESELSWITCH",
        "NBMLDCUESELSWITCH",
        "NBMMACHSRESETALGOSELSWITCH",
        "NBMSFLDCUESELSWITCH",
        "NBMULCACALGOSELSWITCH",
        "RRCCACCHOICE",
        "RRCCECODECACCHOICE"
    FROM
    huawei_nbi_umts."UCELLALGOSWITCH"

    """
)

UCELLCAC = ReplaceableObject(
    'huawei_cm_3g."UCELLCAC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BACKGROUNDNOISE",
        "BGNABNORMALTHD",
        "BGNADJUSTTIMELEN",
        "BGNENDTIME",
        "BGNEQUSERNUMTHD",
        "BGNOPTSWITCH",
        "BGNPERSISTSWITCH",
        "BGNSTARTTIME",
        "BGNSWITCH",
        "BGNULLOADTHD",
        "BGNUPDATETHD",
        "CELLENVTYPE",
        "CELLID",
        "CELLULEQUNUMCAPACITY",
        "DEFPCPICHECNO",
        "DLCCHLOADRSRVCOEFF",
        "DLCELLTOTALTHD",
        "DLCONVAMRTHD",
        "DLCONVNONAMRTHD",
        "DLHOCECODERESVSF",
        "DLHOTHD",
        "DLHSUPARSVDFACTOR",
        "DLNRTRRCCACCECODERESVSF",
        "DLOTHERRRCCACCECODERESVSF",
        "DLOTHERTHD",
        "DLRRCCECODERESVSF",
        "DLTOTALEQUSERNUM",
        "HSDPABEPBRTHD",
        "HSDPAMAXGBPTHD",
        "HSDPASTRMPBRTHD",
        "HSUPAEQUALPRIORITYUSERPBRTHD",
        "HSUPAHIGHPRIORITYUSERPBRTHD",
        "HSUPALOWPRIORITYUSERPBRTHD",
        "HSUPAMAXGBPTHD",
        "LOADBALANCERATIO",
        "LOGICRNCID",
        "MAXEFACHUSERNUM",
        "MAXERACHUSERNUM",
        "MAXHSDPAUSERNUM",
        "MAXHSUPAUSERNUM",
        "MAXULTXPOWERFORBAC",
        "MAXULTXPOWERFORCONV",
        "MAXULTXPOWERFORINT",
        "MAXULTXPOWERFORSTR",
        "NONHPWRFORGBPPREEMP",
        "NRTRRCCACTHDOFFSET",
        "OTHERRRCCACTHDOFFSET",
        "ROTCONTROLTARGET",
        "RTRRCCACTHDOFFSET",
        "TERMCONVUSINGHORESTHD",
        "ULCCHLOADFACTOR",
        "ULCELLTOTALTHD",
        "ULHOCERESVSF",
        "ULHSDPCCHRSVDFACTOR",
        "ULICLDCOPTSWITCH",
        "ULNONCTRLTHDFORAMR",
        "ULNONCTRLTHDFORHO",
        "ULNONCTRLTHDFORNONAMR",
        "ULNONCTRLTHDFOROTHER",
        "ULNRTRRCCACCERESVSF",
        "ULOTHERRRCCACCERESVSF",
        "ULRRCCERESVSF",
        "ULTOTALEQUSERNUM"
    FROM
    huawei_nbi_umts."UCELLCAC"

    """
)

UCELLCMCF = ReplaceableObject(
    'huawei_cm_3g."UCELLCMCF"',
    """

    SELECT 
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
        "CMCFCELLTYPE",
        "DLSFTURNPOINT",
        "LOGICRNCID",
        "ULSFTURNPOINT"
    FROM
    huawei_nbi_umts."UCELLCMCF"

    """
)

UCELLDCCC = ReplaceableObject(
    'huawei_cm_3g."UCELLDCCC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BEPWRMARGIN",
        "CELLID",
        "COMBPWRMARGIN",
        "DLFULLCVRRATE",
        "LOGICRNCID",
        "ULFULLCVRRATE"
    FROM
    huawei_nbi_umts."UCELLDCCC"

    """
)

UCELLDISTANCEREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UCELLDISTANCEREDIRECTION"',
    """

    SELECT 
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
        "INTERFREQREDIRDELAYTHD",
        "INTERFREQREDIRFACTOROFLDR",
        "INTERFREQREDIRFACTOROFNORM",
        "INTERFREQREDIRSWITCH",
        "LOGICRNCID",
        "REDIRBANDIND",
        "REDIRSWITCH",
        "REDIRUARFCNDOWNLINK",
        "REDIRUARFCNUPLINKIND",
        "DELAYTHS",
        "REDIRFACTOROFLDR",
        "REDIRFACTOROFNORM"
    FROM
    huawei_nbi_umts."UCELLDISTANCEREDIRECTION"

    """
)

UCELLDRD = ReplaceableObject(
    'huawei_cm_3g."UCELLDRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BASEDONMEASHRETRYDRDSWITCH",
        "BASEDUELOCDRDREMAINTHD",
        "BASEDUELOCDRDSWITCH",
        "CELLID",
        "CODEBALANCINGDRDCODERATETHD",
        "CODEBALANCINGDRDMINSFTHD",
        "CODEBALANCINGDRDSWITCH",
        "CONNECTFAILRRCREDIRSWITCH",
        "D2EDRDSWITCH",
        "DPGDRDSWITCH",
        "DRMAXGSMNUM",
        "HSPAPLUSSATISSWITCH",
        "LDBDRDCHOICE",
        "LDBDRDLOADREMAINTHDDCH",
        "LDBDRDLOADREMAINTHDHSDPA",
        "LDBDRDSWITCHDCH",
        "LDBDRDSWITCHHSDPA",
        "LOGICRNCID",
        "REDIRBANDIND",
        "RRCCELLLOADSORTSWITCH",
        "SECCELLLDBDRDCHOICE",
        "SECCELLREFBHFLAGSWITCH",
        "SERVICEDIFFDRDSWITCH",
        "TRAFFTYPEFORBASEDUELOC",
        "UELOCBASEDDRDFORC2DSWITCH",
        "ULLDBDRDLOADREMAINTHDDCHSDPA",
        "ULLDBDRDSWITCHDCHSDPA"
    FROM
    huawei_nbi_umts."UCELLDRD"

    """
)

UCELLDYNSHUTDOWN = ReplaceableObject(
    'huawei_cm_3g."UCELLDYNSHUTDOWN"',
    """

    SELECT 
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
        "DYNSHUTDOWNSWITCH",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCELLDYNSHUTDOWN"

    """
)

UCELLFRC = ReplaceableObject(
    'huawei_cm_3g."UCELLFRC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALLOWEDSAVECODERESOURCE",
        "CELLID",
        "DLBETRAFFDECTHS",
        "ECN0EFFECTTIME",
        "ECN0THS",
        "LOGICRNCID",
        "RRCCAUSESIGCHTYPEIND",
        "ULBETRAFFDECTHS",
        "RRCCAUSESIGCHTYPEID"
    FROM
    huawei_nbi_umts."UCELLFRC"

    """
)

UCELLHCS = ReplaceableObject(
    'huawei_cm_3g."UCELLHCS"',
    """

    SELECT 
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
        "LOGICRNCID",
        "NONHCSCOMPATSWITCH",
        "SHCSRAT",
        "SSEARCHHCS",
        "USEOFHCS"
    FROM
    huawei_nbi_umts."UCELLHCS"

    """
)

UCELLHOCOMM = ReplaceableObject(
    'huawei_cm_3g."UCELLHOCOMM"',
    """

    SELECT 
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
        "COEXISTMEASTHDCHOICE",
        "CSSERVICEHOSWITCH",
        "FASTRETURNTOLTESWITCH",
        "HSPATIMERLEN",
        "INTERFREQRATSWITCH",
        "LOGICRNCID",
        "MACROMICRO1APREMEASSWITCH",
        "PSSERVICEHOSWITCH",
        "SPECUSERCSTHD2DECN0",
        "SPECUSERCSTHD2DRSCP",
        "SPECUSERCSTHD2FECN0",
        "SPECUSERCSTHD2FRSCP",
        "SPECUSERHYSTFOR2D",
        "U2LBLINDREDIRSWITCH",
        "U2LLTELOADSWITCH"
    FROM
    huawei_nbi_umts."UCELLHOCOMM"

    """
)

UCELLHSDPA = ReplaceableObject(
    'huawei_cm_3g."UCELLHSDPA"',
    """

    SELECT 
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
        "ALLOCCODEMODE",
        "CELLID",
        "CODEADJFORHSDPASWITCH",
        "CODEADJFORHSDPAUSERNUMTHD",
        "DYNHSSCCHALLOCSWITCH",
        "HCODEADJPUNSHTIMERLENGTH",
        "HSDPCCHPREAMBLESWITCH",
        "HSPAPOWER",
        "HSPDSCHCODENUM",
        "HSPDSCHMPOCONSTENUM",
        "HSSCCHCODENUM",
        "LOGICRNCID",
        "MIMOMPOCONSTANT",
        "HSPDSCHMAXCODENUM",
        "HSPDSCHMINCODENUM"
    FROM
    huawei_nbi_umts."UCELLHSDPA"

    """
)

UCELLHSDPCCH = ReplaceableObject(
    'huawei_cm_3g."UCELLHSDPCCH"',
    """

    SELECT 
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
        "CQIFBCK",
        "CQIFBCKBASECELLLOAD",
        "CQIFBCKBASECOVERAGE",
        "CQIFBCKBASECSCOMBSERV",
        "CQIFBCKFORCONVER",
        "CQIFBCKFORDCMIMO",
        "CQIFBCKFORMIMO",
        "CQIFBCKFORSHO",
        "CQIPO",
        "CQIPOFORSHO",
        "CQIREF",
        "CQIREFFORSHO",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCELLHSDPCCH"

    """
)

UCELLHSUPA = ReplaceableObject(
    'huawei_cm_3g."UCELLHSUPA"',
    """

    SELECT 
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
        "CELLID",
        "DYNTGTROTCTRLSWITCH",
        "EAGCHCODENUM",
        "ERGCHEHICHCODENUM",
        "LOGICRNCID",
        "MAXTARGETULLOADFACTOR",
        "NONSERVTOTOTALEDCHPWRRATIO"
    FROM
    huawei_nbi_umts."UCELLHSUPA"

    """
)

UCELLINTERFREQHOCOV = ReplaceableObject(
    'huawei_cm_3g."UCELLINTERFREQHOCOV"',
    """

    SELECT 
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
        "HYSTFOR2D",
        "HYSTFOR2F",
        "HYSTFORPRDINTERFREQ",
        "INTERFREQCSTHD2DECN0",
        "INTERFREQCSTHD2DRSCP",
        "INTERFREQCSTHD2FECN0",
        "INTERFREQCSTHD2FRSCP",
        "INTERFREQFILTERCOEF",
        "INTERFREQHO2DEVENTTYPE",
        "INTERFREQHTHD2DECN0",
        "INTERFREQHTHD2DRSCP",
        "INTERFREQHTHD2FECN0",
        "INTERFREQHTHD2FRSCP",
        "INTERFREQMCMODE",
        "INTERFREQMEASTIME",
        "INTERFREQR99PSTHD2DECN0",
        "INTERFREQR99PSTHD2DRSCP",
        "INTERFREQR99PSTHD2FECN0",
        "INTERFREQR99PSTHD2FRSCP",
        "INTERFREQREPORTMODE",
        "LOGICRNCID",
        "PRDREPORTINTERVAL",
        "TARGETFREQCSTHDECN0",
        "TARGETFREQCSTHDRSCP",
        "TARGETFREQHTHDECN0",
        "TARGETFREQHTHDRSCP",
        "TARGETFREQR99PSTHDECN0",
        "TARGETFREQR99PSTHDRSCP",
        "TIMETOINTERFREQHO",
        "TIMETOTRIG2D",
        "TIMETOTRIG2F",
        "TIMETOTRIGFORPRDINTERFREQ",
        "USEDFREQCSTHDECN0",
        "USEDFREQCSTHDRSCP",
        "USEDFREQHTHDECN0",
        "USEDFREQHTHDRSCP",
        "USEDFREQR99PSTHDECN0",
        "USEDFREQR99PSTHDRSCP",
        "WEIGHTFORUSEDFREQ"
    FROM
    huawei_nbi_umts."UCELLINTERFREQHOCOV"

    """
)

UCELLINTERRATHOCOV = ReplaceableObject(
    'huawei_cm_3g."UCELLINTERRATHOCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSICVERIFY",
        "CELLID",
        "CSBSICVERIFYINDICATION",
        "FILTERCOEFOF2D2F",
        "HYSTFOR2D",
        "HYSTFOR2F",
        "HYSTFORINTERRAT",
        "INTERRATCSTHD2DECN0",
        "INTERRATCSTHD2DRSCP",
        "INTERRATCSTHD2FECN0",
        "INTERRATCSTHD2FRSCP",
        "INTERRATFILTERCOEF",
        "INTERRATHO2DEVENTTYPE",
        "INTERRATHTHD2DECN0",
        "INTERRATHTHD2DRSCP",
        "INTERRATHTHD2FECN0",
        "INTERRATHTHD2FRSCP",
        "INTERRATMEASTIME",
        "INTERRATPERIODREPORTINTERVAL",
        "INTERRATPHYCHFAILNUM",
        "INTERRATPINGPONGHYST",
        "INTERRATPINGPONGTIMER",
        "INTERRATR99PSTHD2DECN0",
        "INTERRATR99PSTHD2DRSCP",
        "INTERRATR99PSTHD2FECN0",
        "INTERRATR99PSTHD2FRSCP",
        "INTERRATREPORTMODE",
        "LOGICRNCID",
        "PENALTYTIMEFORPHYCHFAIL",
        "PSBSICVERIFYINDICATION",
        "TARGETRATCSTHD",
        "TARGETRATHTHD",
        "TARGETRATR99PSTHD",
        "TIMETOTRIGFORNONVERIFY",
        "TIMETOTRIGFORVERIFY",
        "TRIGTIME2D",
        "TRIGTIME2F",
        "WEIGHTFORUSEDFREQ"
    FROM
    huawei_nbi_umts."UCELLINTERRATHOCOV"

    """
)

UCELLINTERRATHONCOV = ReplaceableObject(
    'huawei_cm_3g."UCELLINTERRATHONCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMNTOFRPT3C",
        "BSICVERIFY",
        "CELLID",
        "CSHOOUT2GLOADTHD",
        "HYSTFOR3C",
        "INTERRATFILTERCOEF",
        "INTERRATHOATTEMPTS",
        "INTERRATMEASTIME",
        "INTERRATNCOVHOCSTHD",
        "INTERRATNCOVHOPSTHD",
        "INTERRATPHYCHFAILNUM",
        "LOGICRNCID",
        "PENALTYTIMEFORPHYCHFAIL",
        "PERIODFOR3C",
        "PSHOOUT2GLOADTHD",
        "TRIGTIME3C"
    FROM
    huawei_nbi_umts."UCELLINTERRATHONCOV"

    """
)

UCELLINTRAFREQHO = ReplaceableObject(
    'huawei_cm_3g."UCELLINTRAFREQHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHORSCP1FTHRESHOLD",
        "CELLID",
        "HYST1AOR1CTRIGSCC",
        "HYST1DJUDGETRIGSCC",
        "HYSTFOR1A",
        "HYSTFOR1B",
        "HYSTFOR1C",
        "HYSTFOR1D",
        "HYSTFOR1F",
        "HYSTFOR1J",
        "INTRAABLTHDFOR1FECNO",
        "INTRAFREQFILTERCOEF",
        "INTRAFREQMEASQUANTITY",
        "INTRARELTHDFOR1ACSNVP",
        "INTRARELTHDFOR1ACSVP",
        "INTRARELTHDFOR1APS",
        "INTRARELTHDFOR1BCSNVP",
        "INTRARELTHDFOR1BCSVP",
        "INTRARELTHDFOR1BPS",
        "LOGICRNCID",
        "MAXCELLINACTIVESET",
        "PERIODMRREPORTNUMFOR1A",
        "PERIODMRREPORTNUMFOR1C",
        "PERIODMRREPORTNUMFOR1J",
        "REPORTINTERVALFOR1A",
        "REPORTINTERVALFOR1C",
        "REPORTINTERVALFOR1J",
        "RNCID",
        "SHOQUALMIN",
        "TRIGTIME1A",
        "TRIGTIME1B",
        "TRIGTIME1C",
        "TRIGTIME1D",
        "TRIGTIME1F",
        "TRIGTIME1J",
        "WEIGHT"
    FROM
    huawei_nbi_umts."UCELLINTRAFREQHO"

    """
)

UCELLLDB = ReplaceableObject(
    'huawei_cm_3g."UCELLLDB"',
    """

    SELECT 
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
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCELLLDB"

    """
)

UCELLLDM = ReplaceableObject(
    'huawei_cm_3g."UCELLLDM"',
    """

    SELECT 
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
        "DCHUSERNUMCONGTHD",
        "DCHUSERNUMNORMALTHD",
        "DCHUSERNUMSTATRANSHYSTIME",
        "DLCONGSTATETRANSHYSTIME",
        "DLHEAVYTHD",
        "DLLDRRELTHD",
        "DLLDRTRIGTHD",
        "DLLDTRNSHYSTIME",
        "DLLOADEDTHD",
        "DLNONHLOADCONGSTATETHD",
        "DLNONHLOADNORMALSTATETHD",
        "DLNORMALTHD",
        "DLOLCRELTHD",
        "DLOLCTRIGTHD",
        "DLOVERLOADTHD",
        "DLPWRCSCLBRELTHD",
        "DLPWRCSCLBTRIGTHD",
        "DLPWRPSCLBRELTHD",
        "DLPWRPSCLBTRIGTHD",
        "DLSFDIV2CMVALIDCODETHD",
        "FAIRNESSTHD",
        "HSUPAURETRNSLDRELTHD",
        "HSUPAURETRNSLDTRIGTHD",
        "LOGICRNCID",
        "OFFLOADRELATIVETHD",
        "RELRATIOFORULRTWP",
        "RTWPLOADSTATETRANSHYSTIME",
        "SPECUSERPWRENDLPWRTRIGTHD",
        "TRIGRATIOFORULRTWP",
        "ULLDRRELTHD",
        "ULLDRTRIGTHD",
        "ULLDTRNSHYSTIME",
        "ULOLCRELTHD",
        "ULOLCTRIGTHD",
        "ULPWRCSCLBRELTHD",
        "ULPWRCSCLBTRIGTHD",
        "ULPWRPSCLBRELTHD",
        "ULPWRPSCLBTRIGTHD",
        "ULRTWPCONGTHD",
        "ULRTWPNORMALTHD"
    FROM
    huawei_nbi_umts."UCELLLDM"

    """
)

UCELLLDR = ReplaceableObject(
    'huawei_cm_3g."UCELLLDR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CCCHCONGCTRLSWITCH",
        "CELLID",
        "CELLLDRSFRESTHD",
        "CODECONGHOENHANCEIND",
        "CODECONGSELINTERFREQHOIND",
        "DLCSINTERRATSHOULDBEHOUENUM",
        "DLCSINTERRATSHOULDNOTHOUENUM",
        "DLINTERFREQHOBWTHD",
        "DLINTERFREQHOCELLLOADSPACETHD",
        "DLLDRAMRRATEREDUCTIONRABNUM",
        "DLLDRBERATEREDUCTIONRABNUM",
        "DLLDREIGHTHACTION",
        "DLLDRELEVENTHACTION",
        "DLLDRFIFTHACTION",
        "DLLDRFIRSTACTION",
        "DLLDRFOURTHACTION",
        "DLLDRNINTHACTION",
        "DLLDRPSRTQOSRENEGRABNUM",
        "DLLDRSECONDACTION",
        "DLLDRSEVENTHACTION",
        "DLLDRSIXTHACTION",
        "DLLDRTENTHACTION",
        "DLLDRTHIRDACTION",
        "DLLDRTWELFTHACTION",
        "DLLDRWAMRSFRECFGUENUM",
        "DLPSINTERRATSHOULDBEHOUENUM",
        "DLPSINTERRATSHOULDNOTHOUENUM",
        "GOLDUSERLOADCONTROLSWITCH",
        "INTERFREQLDHOFORBIDENTC",
        "INTERFREQLDHOMETHODSELECTION",
        "LDRCODEPRIUSEIND",
        "LDRCODEUSEDSPACETHD",
        "LOGICRNCID",
        "MAXUSERNUMCODEADJ",
        "ULCSINTERRATSHOULDBEHOUENUM",
        "ULCSINTERRATSHOULDNOTHOUENUM",
        "ULINTERFREQHOBWTHD",
        "ULINTERFREQHOCELLLOADSPACETHD",
        "ULLDRAMRRATEREDUCTIONRABNUM",
        "ULLDRBERATEREDUCTIONRABNUM",
        "ULLDRCREDITSFRESTHD",
        "ULLDREIGHTHACTION",
        "ULLDRFIFTHACTION",
        "ULLDRFIRSTACTION",
        "ULLDRFOURTHACTION",
        "ULLDRNINTHACTION",
        "ULLDRPSRTQOSRENEGRABNUM",
        "ULLDRSECONDACTION",
        "ULLDRSEVENTHACTION",
        "ULLDRSIXTHACTION",
        "ULLDRTHIRDACTION",
        "ULPSINTERRATSHOULDBEHOUENUM",
        "ULPSINTERRATSHOULDNOTHOUENUM",
        "ULTTICREDITSFRESTHD"
    FROM
    huawei_nbi_umts."UCELLLDR"

    """
)

UCELLLICENSE = ReplaceableObject(
    'huawei_cm_3g."UCELLLICENSE"',
    """

    SELECT 
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
        "FUNCSWITCH1",
        "FUNCSWITCH2",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCELLLICENSE"

    """
)

UCELLMEAS = ReplaceableObject(
    'huawei_cm_3g."UCELLMEAS"',
    """

    SELECT 
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
        "FACHMEASIND",
        "INTERFREQINTERRATMEASIND",
        "INTRAFREQMEASIND",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCELLMEAS"

    """
)

UCELLNFREQPRIOINFO = ReplaceableObject(
    'huawei_cm_3g."UCELLNFREQPRIOINFO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLACKLSTCELLNUMBER",
        "CELLID",
        "EARFCN",
        "EDETECTIND",
        "EMEASBW",
        "EQRXLEVMIN",
        "LOGICRNCID",
        "NPRIORITY",
        "RSRQSWITCH",
        "SUPCNOPGRPINDEX",
        "THDTOHIGH",
        "THDTOLOW"
    FROM
    huawei_nbi_umts."UCELLNFREQPRIOINFO"

    """
)

UCELLOLC = ReplaceableObject(
    'huawei_cm_3g."UCELLOLC"',
    """

    SELECT 
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
        "DLOLCFTFRSTRCTRABNUM",
        "DLOLCFTFRSTRCTTIMES",
        "DLOLCTRAFFRELRABNUM",
        "FACHPWRREDUCEVALUE",
        "GOLDUSEREXECOLCSWITCH",
        "LOGICRNCID",
        "RATERECOVERTIMERLEN",
        "RATERSTRCTCOEF",
        "RATERSTRCTTIMERLEN",
        "RECOVERCOEF",
        "TRANSCCHUSERNUM",
        "ULOLCFTFRSTRCTRABNUM",
        "ULOLCFTFRSTRCTTIMES",
        "ULOLCTRAFFRELRABNUM"
    FROM
    huawei_nbi_umts."UCELLOLC"

    """
)

UCELLPUC = ReplaceableObject(
    'huawei_cm_3g."UCELLPUC"',
    """

    SELECT 
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
        "LOGICRNCID",
        "OFFQOFFSET1HEAVY",
        "OFFQOFFSET1LIGHT",
        "OFFQOFFSET2HEAVY",
        "OFFQOFFSET2LIGHT",
        "OFFSINTERHEAVY",
        "OFFSINTERLIGHT",
        "SPUCHEAVY",
        "SPUCHYST",
        "SPUCLIGHT"
    FROM
    huawei_nbi_umts."UCELLPUC"

    """
)

UCELLREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UCELLREDIRECTION"',
    """

    SELECT 
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
        "LOGICRNCID",
        "REDIRSWITCH",
        "TRAFFICTYPE"
    FROM
    huawei_nbi_umts."UCELLREDIRECTION"

    """
)

UCELLRLACTTIME = ReplaceableObject(
    'huawei_cm_3g."UCELLRLACTTIME"',
    """

    SELECT 
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
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCELLRLACTTIME"

    """
)

UCELLRLPWR = ReplaceableObject(
    'huawei_cm_3g."UCELLRLPWR"',
    """

    SELECT 
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
        "CNDOMAINID",
        "DLSF",
        "LOGICRNCID",
        "MAXBITRATE",
        "RLMAXDLPWR",
        "RLMINDLPWR",
        "SPECUSERRLMAXDLPWR"
    FROM
    huawei_nbi_umts."UCELLRLPWR"

    """
)

UCELLSELRESEL = ReplaceableObject(
    'huawei_cm_3g."UCELLSELRESEL"',
    """

    SELECT 
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
        "CONNQHYST1S",
        "CONNQHYST2S",
        "CONNSINTERSEARCH",
        "CONNSINTRASEARCH",
        "IDLEQHYST1S",
        "IDLEQHYST2S",
        "IDLESINTERSEARCH",
        "IDLESINTRASEARCH",
        "INTERFREQTRESELSCALINGFACTOR",
        "INTERRATTRESELSCALINGFACTOR",
        "LOGICRNCID",
        "MAXALLOWEDULTXPOWER",
        "NONHCSIND",
        "PRIORESELECTSWITCH",
        "QHYST1SFACH",
        "QHYST1SPCH",
        "QHYST2SFACH",
        "QHYST2SPCH",
        "QQUALMIN",
        "QRXLEVMIN",
        "QRXLEVMINEXTSUP",
        "QUALMEAS",
        "SPEEDDEPENDENTSCALINGFACTOR",
        "SPRIORITY",
        "SSEARCHRAT",
        "THDPRIORITYSEARCH1",
        "THDPRIORITYSEARCH2",
        "THDSERVINGLOW",
        "THDSERVINGLOW2",
        "TRESELECTIONS",
        "TRESELECTIONSFACH",
        "TRESELECTIONSPCH"
    FROM
    huawei_nbi_umts."UCELLSELRESEL"

    """
)

UCELLSIBSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCELLSIBSWITCH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "SIBCFGBITMAP"
    FROM
    huawei_nbi_umts."UCELLSIBSWITCH"

    """
)

UCELLUPDTCTRLSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCELLUPDTCTRLSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLUPDTCAUSE",
        "FACHPOWERCELLUPDTECNOTHD",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCELLUPDTCTRLSWITCH"

    """
)

UCELLURA = ReplaceableObject(
    'huawei_cm_3g."UCELLURA"',
    """

    SELECT 
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
        "LOGICRNCID",
        "URAID"
    FROM
    huawei_nbi_umts."UCELLURA"

    """
)

UCHLQUALITYEVALUATE = ReplaceableObject(
    'huawei_cm_3g."UCHLQUALITYEVALUATE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BETTI10MSRSCPTHD",
        "BETTI10MSRSCPUPTHD",
        "BETTI2MSRSCPTHD",
        "BETTI2MSRSCPUPTHD",
        "LOGICRNCID",
        "RSCPEFFECTALGOSWITCH",
        "SRBH2DNONHLOADSTATE",
        "SRBH2DRABRSCPPERIODTIMER",
        "SRBOVERHSDPAECN0DOWNTHD",
        "SRBOVERHSDPAECN0UPTHD",
        "SRBOVERHSDPARSCPDOWNTHD",
        "SRBOVERHSDPARSCPUPTHD"
    FROM
    huawei_nbi_umts."UCHLQUALITYEVALUATE"

    """
)

UCHPWROFFSET = ReplaceableObject(
    'huawei_cm_3g."UCHPWROFFSET"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AICHPOWEROFFSET",
        "CELLID",
        "LOGICRNCID",
        "PICHPOWEROFFSET"
    FROM
    huawei_nbi_umts."UCHPWROFFSET"

    """
)

UCIDCHG = ReplaceableObject(
    'huawei_cm_3g."UCIDCHG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLIDCHGSWITCH",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCIDCHG"

    """
)

UCLB = ReplaceableObject(
    'huawei_cm_3g."UCLB"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "PENALTYTIMEFORHLOAD3GCELL",
        "SEPRNCNCELLLOADESTSWITCH",
        "UMTSCELLIFHOFAILNUM",
        "UMTSCELLLOADESTSLIDWINDOW"
    FROM
    huawei_nbi_umts."UCLB"

    """
)

UCMCF = ReplaceableObject(
    'huawei_cm_3g."UCMCF"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CMCFCELLTYPE",
        "DLSFLIMITCMIND",
        "DLSFTURNPOINT",
        "EHSPACMPERMISSIONIND",
        "HSDPACMPERMISSIONIND",
        "HSUPACMPERMISSIONIND",
        "LOGICRNCID",
        "NCOVCMUSERNUMCTRLSWITCH",
        "ULSFTURNPOINT"
    FROM
    huawei_nbi_umts."UCMCF"

    """
)

UCNDOMAIN = ReplaceableObject(
    'huawei_cm_3g."UCNDOMAIN"',
    """

    SELECT 
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
        "CNDOMAINID",
        "DRXCYCLELENCOEF",
        "LOGICRNCID",
        "T3212",
        "NMO"
    FROM
    huawei_nbi_umts."UCNDOMAIN"

    """
)

UCNNODE = ReplaceableObject(
    'huawei_cm_3g."UCNNODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AVAILCAP",
        "CNDOMAINID",
        "CNID",
        "CNLOADSTATUS",
        "CNOPINDEX",
        "CNPROTCLVER",
        "DPX",
        "LOGICRNCID",
        "RTCPSWITCH",
        "SWITCH3GPP25415CR0125",
        "TNLBEARERTYPE",
        "CELLSTATERPTSWITCH",
        "DLE2EQOSSWITCH"
    FROM
    huawei_nbi_umts."UCNNODE"

    """
)

UCNOPERATOR = ReplaceableObject(
    'huawei_cm_3g."UCNOPERATOR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPERATORNAME",
        "CNOPINDEX",
        "LOGICRNCID",
        "MCC",
        "MNC",
        "OPERATORTYPE"
    FROM
    huawei_nbi_umts."UCNOPERATOR"

    """
)

UCNOPERGROUP = ReplaceableObject(
    'huawei_cm_3g."UCNOPERGROUP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPGRPINDEX",
        "CNOPGRPNAME",
        "CNOPINDEX1",
        "CNOPNUM",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCNOPERGROUP"

    """
)

UCNTCHK = ReplaceableObject(
    'huawei_cm_3g."UCNTCHK"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COUNTERCHECKSWITCH",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UCNTCHK"

    """
)

UCOIFTIMER = ReplaceableObject(
    'huawei_cm_3g."UCOIFTIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ADAPRETRANPUNTIMER",
        "CHANNELRETRYHOTIMERLEN",
        "CHANNELRETRYTIMERLEN",
        "LOGICRNCID",
        "PARKINGRELTIMER",
        "RABMODIFYTIMERLEN",
        "ZERORATEUPFAILTORELTIMERLEN"
    FROM
    huawei_nbi_umts."UCOIFTIMER"

    """
)

UCONNMODETIMER = ReplaceableObject(
    'huawei_cm_3g."UCONNMODETIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "N302",
        "N304",
        "N308",
        "N312",
        "N313",
        "N315",
        "N381",
        "T302",
        "T304",
        "T305",
        "T307",
        "T308",
        "T309",
        "T312",
        "T313",
        "T314",
        "T315",
        "T316",
        "T323",
        "T381"
    FROM
    huawei_nbi_umts."UCONNMODETIMER"

    """
)

UCORRMALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCORRMALGOSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CFGSWITCH",
        "CMCFSWITCH",
        "CMPSWITCH",
        "CMPSWITCH2",
        "CSSWITCH",
        "DRASWITCH",
        "DRASWITCH2",
        "DRSWITCH",
        "HOSWITCH",
        "HOSWITCH1",
        "LOGICRNCID",
        "MAPSWITCH",
        "PCSWITCH",
        "PSSWITCH",
        "RESERVEDSWITCH0",
        "RESERVEDSWITCH1",
        "RESERVEDU32PARA0",
        "RESERVEDU8PARA0",
        "RESERVEDU8PARA1",
        "SRNSRSWITCH"
    FROM
    huawei_nbi_umts."UCORRMALGOSWITCH"

    """
)

UCORRMPARA = ReplaceableObject(
    'huawei_cm_3g."UCORRMPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "PERFENHANCESWITCH",
        "PERFENHANCESWITCH1",
        "PERFENHANCESWITCH2",
        "PERFENHANCESWITCH3",
        "PERFENHANCESWITCH4",
        "PERFENHANCESWITCH5",
        "RESERVEDSWITCH1"
    FROM
    huawei_nbi_umts."UCORRMPARA"

    """
)

UCSVOICEPPC = ReplaceableObject(
    'huawei_cm_3g."UCSVOICEPPC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "VOICEPPCSWITCH"
    FROM
    huawei_nbi_umts."UCSVOICEPPC"

    """
)

UCTRLPLNSHAREPARA = ReplaceableObject(
    'huawei_cm_3g."UCTRLPLNSHAREPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CTRLPLNSHARINGOUTOFFSET",
        "CTRLPLNSHARINGOUTTHD"
    FROM
    huawei_nbi_umts."UCTRLPLNSHAREPARA"

    """
)

UDCCC = ReplaceableObject(
    'huawei_cm_3g."UDCCC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BASECOVERD2E6ATHD",
        "BASECOVERD2E6BTHD",
        "BEPWRMARGIN",
        "CHANNELRETRYPENALTYNUM",
        "COMBPWRMARGIN",
        "DCCCSTG",
        "DCCCUPPENALTYLEN",
        "DCHTHROUMEASPERIOD",
        "DLDCCCRATETHD",
        "DLFULLCVRRATE",
        "DLMIDRATECALC",
        "DLMIDRATETHD",
        "DLRATEDNADJLEVEL",
        "DLRATEUPADJLEVEL",
        "E2DTHROU4BTHD",
        "FAILTIMETH",
        "HSUPABESHORATETHD",
        "HSUPADCCCSTG",
        "LITTLERATETHD",
        "LOGICRNCID",
        "MONITIMELEN",
        "ULDCCCRATETHD",
        "ULFULLCVRRATE",
        "ULMIDRATECALC",
        "ULMIDRATETHD",
        "ULRATEDNADJLEVEL",
        "ULRATEUPADJLEVEL"
    FROM
    huawei_nbi_umts."UDCCC"

    """
)

UDISTANCEREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UDISTANCEREDIRECTION"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DELAYTHS",
        "INTERFREQREDIRSWITCH",
        "LOGICRNCID",
        "REDIRFACTOROFLDR",
        "REDIRFACTOROFNORM",
        "REDIRSWITCH"
    FROM
    huawei_nbi_umts."UDISTANCEREDIRECTION"

    """
)

UDPUCFGDATA = ReplaceableObject(
    'huawei_cm_3g."UDPUCFGDATA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CELLCOUNTERSMEASOBJCTRLSWITCH",
        "EDCHIUBCONGCHECKSWITCH",
        "HSUPAIURCONGCTRLSWITCH",
        "HSUPATNLSWITCH",
        "IUBFPTWAITNODESYNCRSP",
        "IUBFPTWAITTRCHSYNCRSP",
        "IURFPTWAITNODESYNCRSP",
        "IURFPTWAITTRCHSYNCRSP",
        "LOWSIGNALPAGINGSWITCH",
        "MACCPAGEREPEATTIMES",
        "PAGINGSWITCH",
        "TPESWITCH",
        "WBAMRNOISECORRECTSWITCH"
    FROM
    huawei_nbi_umts."UDPUCFGDATA"

    """
)

UDRD = ReplaceableObject(
    'huawei_cm_3g."UDRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BASEDONMEASHRETRYDRDSWITCH",
        "BASEDUELOCDRDREMAINTHD",
        "BASEDUELOCDRDSWITCH",
        "CODEBALANCINGDRDCODERATETHD",
        "CODEBALANCINGDRDMINSFTHD",
        "CODEBALANCINGDRDSWITCH",
        "COMACROMICROIFREDIRSWITCH",
        "CONNECTFAILRRCREDIRSWITCH",
        "DELTACODEOCCUPIEDRATE",
        "DLSFTHDFORRRCDRDPRECAC",
        "DPGDRDSWITCH",
        "DRMAXGSMNUM",
        "HRTSERVICEDIFFDRDSWITCH",
        "HSDPALOADDRDOPTSWITCH",
        "HSPAPLUSSATISSWITCH",
        "LDBDRDCHOICE",
        "LDBDRDLOADREMAINTHDDCH",
        "LDBDRDLOADREMAINTHDHSDPA",
        "LDBDRDOFFSETDCH",
        "LDBDRDOFFSETHSDPA",
        "LDBDRDSWITCHDCH",
        "LDBDRDSWITCHHSDPA",
        "LDBDRDTOTALPWRPROTHD",
        "LOGICRNCID",
        "POWLOADDRDOPTSWITCH",
        "PWRTHDFORRRCDRDPRECAC",
        "REDIRBANDIND",
        "SECCELLLDBDRDCHOICE",
        "SECCELLREFBHFLAGSWITCH",
        "SERVICEDIFFDRDSWITCH",
        "TRAFFTYPEFORBASEDUELOC",
        "UELOCBASEDDRDFORC2DSWITCH",
        "ULCETHDFORRRCDRDPRECAC",
        "ULLDBDRDLOADREMAINTHDDCHSDPA",
        "ULLDBDRDOFFSETDCHSDPA",
        "ULLDBDRDSWITCHDCHSDPA"
    FROM
    huawei_nbi_umts."UDRD"

    """
)

UDRDMIMO = ReplaceableObject(
    'huawei_cm_3g."UDRDMIMO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LEGACYHDRDSWITCHOFSTTD",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UDRDMIMO"

    """
)

UDSACAUTOALGO = ReplaceableObject(
    'huawei_cm_3g."UDSACAUTOALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACINTERVALOFCELLS",
        "ACRANGE",
        "ACRSTRCTINTERVALLEN",
        "CSRESTRICTION",
        "DSACAUTOSWITCH",
        "LOGICRNCID",
        "NUMBEROFACS",
        "PSRESTRICTION"
    FROM
    huawei_nbi_umts."UDSACAUTOALGO"

    """
)

UDTXDRXPARA = ReplaceableObject(
    'huawei_cm_3g."UDTXDRXPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CQIDTXTIMER",
        "CQIFBCKININDTXDRXMODE",
        "DPCCHBURST1",
        "DPCCHBURST2",
        "DRXCYCLE",
        "DRXGRANTMONITORING",
        "DRXVALID",
        "DTXCYCLE1",
        "DTXCYCLE2",
        "DTXLONGPREAMBLE",
        "DTXVALID",
        "EDCHTTITYPE",
        "INACTTHSFORCYCLE2",
        "INACTTHSFORDRXCYCLE",
        "INACTTHSFORGRANTMONITORING",
        "LOGICRNCID",
        "MACDTXCYCLE",
        "MACINACTIVETHRESHOLD",
        "TRAFFICCLASS"
    FROM
    huawei_nbi_umts."UDTXDRXPARA"

    """
)

UEDCHRATEADJUSTSET = ReplaceableObject(
    'huawei_cm_3g."UEDCHRATEADJUSTSET"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EDCHRATEADJUSTSET",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UEDCHRATEADJUSTSET"

    """
)

UEDCHTTIRECFG = ReplaceableObject(
    'huawei_cm_3g."UEDCHTTIRECFG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMREVENTATHD",
        "AMRTHD6A1",
        "AMRTHD6B1",
        "BETHD6A1",
        "BETHD6A2",
        "BETHD6B1",
        "BETHD6B2",
        "LOGICRNCID",
        "LOWRATIOFOR2MSTO10MS",
        "PRIORITYOPT",
        "RATIOFOR10MSTO2MS",
        "RESOURCEOPTION",
        "TTIEDCHTHROUMEASPERIOD",
        "UPRATIOFOR2MSTO10MSBASECE",
        "UPRATIOFOR2MSTO10MSBASERTWP",
        "VOICEPMRMCSWITCH",
        "VOIPEVENTATHD",
        "VOIPTHD6A1",
        "VOIPTHD6B1",
        "WAMREVENTATHD",
        "WAMRTHD6A1",
        "WAMRTHD6B1"
    FROM
    huawei_nbi_umts."UEDCHTTIRECFG"

    """
)

UEVQIPARA = ReplaceableObject(
    'huawei_cm_3g."UEVQIPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UEVQIPARA"

    """
)

UEXT2GCELL = ReplaceableObject(
    'huawei_cm_3g."UEXT2GCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BANDIND",
        "BCC",
        "BCCHARFCN",
        "CFGRACIND",
        "CID",
        "CIO",
        "CNOPGRPINDEX",
        "GSMCELLINDEX",
        "GSMCELLNAME",
        "LAC",
        "LDPRDRPRTSWITCH",
        "LOGICRNCID",
        "MCC",
        "MNC",
        "NBSCINDEX",
        "NCC",
        "NCMODE",
        "RAC",
        "RATCELLTYPE",
        "SUPPPSHOFLAG",
        "SUPPRIMFLAG",
        "USEOFHCS"
    FROM
    huawei_nbi_umts."UEXT2GCELL"

    """
)

UEXT3GCELL = ReplaceableObject(
    'huawei_cm_3g."UEXT3GCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "APFLAG",
        "BANDIND",
        "CELLCAPCONTAINERFDD",
        "CELLHOSTTYPE",
        "CELLID",
        "CELLNAME",
        "CFGRACIND",
        "CIO",
        "CNOPGRPINDEX",
        "CP1SUPIND",
        "DIVMODFORDCHSDPA",
        "DPCHDIVMODFORMIMO",
        "DPCHDIVMODFOROTHER",
        "EFACHSUPIND",
        "FDPCHDIVMODFORMIMO",
        "FDPCHDIVMODFOROTHER",
        "HARQPREACAP",
        "LAC",
        "LOGICRNCID",
        "MAXALLOWEDULTXPOWERIND",
        "NRNCID",
        "OVERLAYMOBILITYFLAG",
        "PSCRAMBCODE",
        "QQUALMININD",
        "QRXLEVMININD",
        "RAC",
        "STTDSUPIND",
        "SUPPDPCMODECHGFLAG",
        "TXDIVERSITYIND",
        "UARFCNDOWNLINK",
        "UARFCNUPLINKIND",
        "USEOFHCS",
        "VPLIMITIND",
        "UARFCNUPLINK",
        "MAXALLOWEDULTXPOWER",
        "QQUALMIN",
        "QRXLEVMIN",
        "QRXLEVMINEXTSUP"
    FROM
    huawei_nbi_umts."UEXT3GCELL"

    """
)

UEXT3GCELLINTRAFREQHO = ReplaceableObject(
    'huawei_cm_3g."UEXT3GCELLINTRAFREQHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHORSCP1FTHRESHOLD",
        "CELLID",
        "HYSTFOR1A",
        "HYSTFOR1B",
        "HYSTFOR1C",
        "HYSTFOR1D",
        "HYSTFOR1F",
        "HYSTFOR1J",
        "INTRAABLTHDFOR1FECNO",
        "INTRAFREQFILTERCOEF",
        "INTRAFREQMEASQUANTITY",
        "INTRARELTHDFOR1ACSNVP",
        "INTRARELTHDFOR1ACSVP",
        "INTRARELTHDFOR1APS",
        "INTRARELTHDFOR1BCSNVP",
        "INTRARELTHDFOR1BCSVP",
        "INTRARELTHDFOR1BPS",
        "LOGICRNCID",
        "MAXCELLINACTIVESET",
        "NRNCID",
        "PERIODMRREPORTNUMFOR1A",
        "PERIODMRREPORTNUMFOR1C",
        "PERIODMRREPORTNUMFOR1J",
        "REPORTINTERVALFOR1A",
        "REPORTINTERVALFOR1C",
        "REPORTINTERVALFOR1J",
        "SHOQUALMIN",
        "TRIGTIME1A",
        "TRIGTIME1B",
        "TRIGTIME1C",
        "TRIGTIME1D",
        "TRIGTIME1F",
        "TRIGTIME1J",
        "WEIGHT"
    FROM
    huawei_nbi_umts."UEXT3GCELLINTRAFREQHO"

    """
)

UFACH = ReplaceableObject(
    'huawei_cm_3g."UFACH"',
    """

    SELECT 
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
        "CHCODINGTYPE",
        "CODINGRATE",
        "LOGICRNCID",
        "MAXCMCHPI",
        "MAXFACHPOWER",
        "MINCMCHPI",
        "OFFSETFACHPOWER",
        "PHYCHID",
        "RATEMATCHINGATTR",
        "SIGRBIND",
        "TOAWE",
        "TOAWS",
        "TRCHID"
    FROM
    huawei_nbi_umts."UFACH"

    """
)

UFACHBANDWIDTH = ReplaceableObject(
    'huawei_cm_3g."UFACHBANDWIDTH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BANDWIDTHFORFACH",
        "LOGICRNCID",
        "TRAFFICCLASS",
        "USERPRIORITY"
    FROM
    huawei_nbi_umts."UFACHBANDWIDTH"

    """
)

UFACHDYNTFS = ReplaceableObject(
    'huawei_cm_3g."UFACHDYNTFS"',
    """

    SELECT 
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
        "LOGICRNCID",
        "RLCSIZE",
        "TBNUMBER1",
        "TBNUMBER2",
        "TBNUMBER3",
        "TFSNUMBER",
        "TRCHID"
    FROM
    huawei_nbi_umts."UFACHDYNTFS"

    """
)

UFACHLOCH = ReplaceableObject(
    'huawei_cm_3g."UFACHLOCH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "TRCHID"
    FROM
    huawei_nbi_umts."UFACHLOCH"

    """
)

UFDPCHPARA = ReplaceableObject(
    'huawei_cm_3g."UFDPCHPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FDPCHPO2",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UFDPCHPARA"

    """
)

UFDPCHRLPWR = ReplaceableObject(
    'huawei_cm_3g."UFDPCHRLPWR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "FDPCHMAXREFPWR",
        "FDPCHMINREFPWR",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UFDPCHRLPWR"

    """
)

UFRC = ReplaceableObject(
    'huawei_cm_3g."UFRC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACTTIMEADJUSTQUALTHD",
        "BEHSUPA2MSTTIRATETHS",
        "CSFBSRBRATE",
        "CSVOICEHSPADLRELDELAY",
        "CSVOICEHSPAULRELDELAY",
        "CSVOICEHSUPATTI",
        "DCMIMOOR4CHSDPASWITCH",
        "DEFAULTCONSTANTVALUE",
        "DEFAULTSPIWEIGHT",
        "DLBEH2DINITIALRATE",
        "DLBETRAFFINITBITRATE",
        "DLDCHBEC2DBITRATEFORAMR",
        "DLDPCHPLSAVEMODE",
        "DLSAVECODERESOURCESWITCH",
        "DLSTRGBR",
        "DPCCHSLOTFMTFORHSPA",
        "DPCMODE",
        "DRXCYCLELENCOEF",
        "DTXDRXENABLINGDELAY",
        "ECN0EFFECTTIME",
        "ECN0THDFORBASECOVERE2D",
        "ECN0THS",
        "ECN0THSFOR2MSTO10MS",
        "EPCHDLEL2MAXRLCPDUSIZE",
        "ERACHMAXPDUSIZEFOREUL2",
        "ERACHMINPDUSIZEFOREUL2",
        "FDDTPCDLSTEPSIZE",
        "HSUPA10MSSCHPRDFORGRANT",
        "HSUPA10MSSCHPRDFORNONGRANT",
        "HSUPA2MSSCHPRDFORGRANT",
        "HSUPA2MSSCHPRDFORNONGRANT",
        "HSUPAINITIALRATE",
        "IMSBEARENHANCEDSWITCH",
        "L2USRVCCEMERCALLARP",
        "LOGICRNCID",
        "MACPDUMAXSIZEFORDLL2ENHANCE",
        "MACPDUMAXSIZEFOREFACH",
        "MBRTHDFORDLHIGHRATE",
        "MIMO64QAMORDCHSDPASWITCH",
        "MIMOOR64QAMSWITCH",
        "NRTINITRATEFORL2U",
        "PTTARPPREEMPTCAP",
        "PTTARPPREEMPTVULN",
        "PTTARPPRIORITYLEVEL",
        "PTTARPQUEUINGALLOWED",
        "PTTDRXCYCLELENCOEF",
        "PTTHSUPATTI",
        "PWRCTRLALG",
        "RETRYCAPABILITY",
        "RLCPDUMAXSIZEFORULL2ENHANCE",
        "RLCPDUMINSIZEFORULL2ENHANCE",
        "SECCELLHUSERNUMTHD",
        "SECCELLTCPTHD",
        "STREAMHSUPA2MSTTIRATETHS",
        "SYSINBEHSDPATODCHTHD",
        "SYSINBEHSUPATODCHTHD",
        "ULBETRAFFINITBITRATE",
        "ULDCHBEC2DBITRATEFORAMR",
        "ULIMSTRANSMODEONHSUPA",
        "ULPTTTRANSMODEONHSUPA",
        "ULSRBTRANSMODEONHSUPA",
        "ULSTRGBR",
        "ULSTRTRANSMODEONHSUPA",
        "ULTPCSTEPSIZE",
        "ULTRAFLASHCSFBSRBRATE",
        "VOIPHSUPATTI"
    FROM
    huawei_nbi_umts."UFRC"

    """
)

UFRCCHLTYPEPARA = ReplaceableObject(
    'huawei_cm_3g."UFRCCHLTYPEPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSVOICECHLTYPE",
        "CSVOICEDYNCHCONFDLPOWTHD",
        "CSVOICEDYNCHCONFUSERNUMTHD",
        "DLBETRAFFDECTHS",
        "DLBETRAFFTHSONHSDPA",
        "DLSTRTHSONHSDPA",
        "IMSCHLTYPE",
        "LOGICRNCID",
        "PTTCHLTYPE",
        "SRBCHLTYPE",
        "SRBCHLTYPERRCEFFECTFLAG",
        "ULBETRAFFDECTHS",
        "ULBETRAFFTHSONHSUPA",
        "ULSTRTHSONHSUPA",
        "VOIPCHLTYPE"
    FROM
    huawei_nbi_umts."UFRCCHLTYPEPARA"

    """
)

UHCSHO = ReplaceableObject(
    'huawei_cm_3g."UHCSHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "NFASTSPDEST",
        "NSLOWSPDEST",
        "TCYCLESLOW",
        "TFASTSPDEST",
        "TRELATELENGTH",
        "TSLOWSPDEST"
    FROM
    huawei_nbi_umts."UHCSHO"

    """
)

UHOCOMM = ReplaceableObject(
    'huawei_cm_3g."UHOCOMM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COEXISTMEASTHDCHOICE",
        "CSHOPRIOMEASTIMERLEN",
        "DIVCTRLFIELD",
        "HSPATIMERLEN",
        "IFANTIPINGPANGTIMERLENGTH",
        "LOGICRNCID",
        "MACROMICRO1APREMEASSWITCH",
        "MAXEDCHCELLINACTIVESET",
        "PSHOPRIOMEASTIMERLEN",
        "SPECUSERCSTHD2DECN0",
        "SPECUSERCSTHD2DRSCP",
        "SPECUSERCSTHD2FECN0",
        "SPECUSERCSTHD2FRSCP",
        "SPECUSERHYSTFOR2D",
        "WEAKCOVHSPAQUALTHDS"
    FROM
    huawei_nbi_umts."UHOCOMM"

    """
)

UHSSCCHLESSOPPARA = ReplaceableObject(
    'huawei_cm_3g."UHSSCCHLESSOPPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ALIGNMODE",
        "HSPDCCHSECONDCODESUPP1",
        "HSPDCCHSECONDCODESUPP2",
        "HSPDCCHSECONDCODESUPP3",
        "HSPDCCHSECONDCODESUPP4",
        "LOGICRNCID",
        "TBINDEXNUM",
        "TBSIZEINDEX1",
        "TBSIZEINDEX2",
        "TBSIZEINDEX3",
        "TBSIZEINDEX4",
        "TRAFFICCLASS",
        "USEMACEHS"
    FROM
    huawei_nbi_umts."UHSSCCHLESSOPPARA"

    """
)

UIDLEMODETIMER = ReplaceableObject(
    'huawei_cm_3g."UIDLEMODETIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "N300",
        "N312",
        "T300",
        "T312"
    FROM
    huawei_nbi_umts."UIDLEMODETIMER"

    """
)

UINTERFREQHOCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERFREQHOCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HHOECNOMIN",
        "HHORSCPMIN",
        "HYSTFOR2D",
        "HYSTFOR2F",
        "HYSTFORPRDINTERFREQ",
        "INTERFREQCSTHD2DECN0",
        "INTERFREQCSTHD2DRSCP",
        "INTERFREQCSTHD2FECN0",
        "INTERFREQCSTHD2FRSCP",
        "INTERFREQFILTERCOEF",
        "INTERFREQHO2DEVENTTYPE",
        "INTERFREQHTHD2DECN0",
        "INTERFREQHTHD2DRSCP",
        "INTERFREQHTHD2FECN0",
        "INTERFREQHTHD2FRSCP",
        "INTERFREQMCMODE",
        "INTERFREQMEASTIME",
        "INTERFREQR99PSTHD2DECN0",
        "INTERFREQR99PSTHD2DRSCP",
        "INTERFREQR99PSTHD2FECN0",
        "INTERFREQR99PSTHD2FRSCP",
        "INTERFREQREPORTMODE",
        "LOGICRNCID",
        "PRDREPORTINTERVAL",
        "TARGETFREQCSTHDECN0",
        "TARGETFREQCSTHDRSCP",
        "TARGETFREQHTHDECN0",
        "TARGETFREQHTHDRSCP",
        "TARGETFREQR99PSTHDECN0",
        "TARGETFREQR99PSTHDRSCP",
        "TIMETOINTERFREQHO",
        "TIMETOTRIG2D",
        "TIMETOTRIG2F",
        "TIMETOTRIGFORPRDINTERFREQ",
        "USEDFREQCSTHDECN0",
        "USEDFREQCSTHDRSCP",
        "USEDFREQHTHDECN0",
        "USEDFREQHTHDRSCP",
        "USEDFREQLOWERTHDECNO",
        "USEDFREQR99PSTHDECN0",
        "USEDFREQR99PSTHDRSCP",
        "USEDFREQUPPERTHDECNO",
        "WEIGHTFORUSEDFREQ"
    FROM
    huawei_nbi_umts."UINTERFREQHOCOV"

    """
)

UINTERFREQHONCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERFREQHONCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMNTOFRPT2C",
        "HYSTFOR2C",
        "INTERFREQFILTERCOEF",
        "INTERFREQMEASTIME",
        "INTERFREQNCOVHOTHDECN0",
        "LOGICRNCID",
        "PERIODFOR2C",
        "TRIGTIME2C"
    FROM
    huawei_nbi_umts."UINTERFREQHONCOV"

    """
)

UINTERFREQNCELL = ReplaceableObject(
    'huawei_cm_3g."UINTERFREQNCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHOFLAG",
        "BLINDHOQUALITYCONDITION",
        "CELLID",
        "CIOOFFSET",
        "CLBFLAG",
        "DRDECN0THRESHHOLD",
        "DRDORLDRFLAG",
        "HOCOVPRIO",
        "IDLEQOFFSET1SN",
        "IDLEQOFFSET2SN",
        "INTERFREQADJSQHCS",
        "INTERNCELLQUALREQFLAG",
        "MBDRFLAG",
        "MBDRPRIO",
        "NCELLID",
        "NCELLRNCID",
        "NPRIOFLAG",
        "RNCID",
        "SIB11IND",
        "SIB12IND",
        "TPENALTYHCSRESELECT",
        "UINTERNCELLSRC",
        "NPRIO",
        "CONNQOFFSET1SN",
        "CONNQOFFSET2SN"
    FROM
    huawei_nbi_umts."UINTERFREQNCELL"

    """
)

UINTERRATHOCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERRATHOCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BSICVERIFY",
        "CSBSICVERIFYINDICATION",
        "FILTERCOEFOF2D2F",
        "HYSTFOR2D",
        "HYSTFOR2F",
        "HYSTFORINTERRAT",
        "INTERRATCSTHD2DECN0",
        "INTERRATCSTHD2DRSCP",
        "INTERRATCSTHD2FECN0",
        "INTERRATCSTHD2FRSCP",
        "INTERRATFILTERCOEF",
        "INTERRATHO2DEVENTTYPE",
        "INTERRATHTHD2DECN0",
        "INTERRATHTHD2DRSCP",
        "INTERRATHTHD2FECN0",
        "INTERRATHTHD2FRSCP",
        "INTERRATMEASTIME",
        "INTERRATPERIODREPORTINTERVAL",
        "INTERRATPHYCHFAILNUM",
        "INTERRATPINGPONGHYST",
        "INTERRATPINGPONGTIMER",
        "INTERRATR99PSTHD2DECN0",
        "INTERRATR99PSTHD2DRSCP",
        "INTERRATR99PSTHD2FECN0",
        "INTERRATR99PSTHD2FRSCP",
        "INTERRATREPORTMODE",
        "LOGICRNCID",
        "PENALTYTIMEFORPHYCHFAIL",
        "PSBSICVERIFYINDICATION",
        "TARGETRATCSTHD",
        "TARGETRATHTHD",
        "TARGETRATR99PSTHD",
        "TIMETOTRIGFORNONVERIFY",
        "TIMETOTRIGFORVERIFY",
        "TRIGTIME2D",
        "TRIGTIME2F",
        "WEIGHTFORUSEDFREQ"
    FROM
    huawei_nbi_umts."UINTERRATHOCOV"

    """
)

UINTERRATHONCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERRATHONCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMNTOFRPT3C",
        "BSICVERIFY",
        "CSHOOUT2GLOADTHD",
        "HYSTFOR3C",
        "INTERRATFILTERCOEF",
        "INTERRATHOATTEMPTS",
        "INTERRATMEASTIME",
        "INTERRATNCOVHOCSTHD",
        "INTERRATNCOVHOPSTHD",
        "INTERRATPHYCHFAILNUM",
        "LOGICRNCID",
        "NCOVHOON2GLDIND",
        "PENALTYTIMEFORPHYCHFAIL",
        "PERIODFOR3C",
        "PSHOOUT2GLOADTHD",
        "SNDLDINFO2GSMIND",
        "TRIGTIME3C"
    FROM
    huawei_nbi_umts."UINTERRATHONCOV"

    """
)

UINTRAFREQHO = ReplaceableObject(
    'huawei_cm_3g."UINTRAFREQHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDHOINTRAFREQMRAMOUNT",
        "BLINDHOINTRAFREQMRINTERVAL",
        "BLINDHORSCP1FTHRESHOLD",
        "DCCCSHOPENALTYTIME",
        "FILTERCOEF",
        "HYST1AOR1CTRIGSCC",
        "HYST1DJUDGETRIGSCC",
        "HYSTFOR1A",
        "HYSTFOR1B",
        "HYSTFOR1C",
        "HYSTFOR1D",
        "HYSTFOR1F",
        "HYSTFOR1J",
        "INTRAABLTHDFOR1FECNO",
        "INTRAFREQMEASQUANTITY",
        "INTRARELTHDFOR1ACSNVP",
        "INTRARELTHDFOR1ACSVP",
        "INTRARELTHDFOR1APS",
        "INTRARELTHDFOR1BCSNVP",
        "INTRARELTHDFOR1BCSVP",
        "INTRARELTHDFOR1BPS",
        "LOGICRNCID",
        "MAXCELLINACTIVESET",
        "PERIODMRREPORTNUMFOR1A",
        "PERIODMRREPORTNUMFOR1C",
        "PERIODMRREPORTNUMFOR1J",
        "RELTHDFORDWNGRD",
        "REPORTINTERVALFOR1A",
        "REPORTINTERVALFOR1C",
        "REPORTINTERVALFOR1J",
        "SHOFAILNUMFORDWNGRD",
        "SHOFAILPERIOD",
        "SHOQUALMIN",
        "SOFTFAILD2FSWITCH",
        "SOFTFAILE2DSWITCH",
        "TRIGTIME1A",
        "TRIGTIME1B",
        "TRIGTIME1C",
        "TRIGTIME1D",
        "TRIGTIME1F",
        "TRIGTIME1J",
        "WEIGHT"
    FROM
    huawei_nbi_umts."UINTRAFREQHO"

    """
)

UINTRAFREQNCELL = ReplaceableObject(
    'huawei_cm_3g."UINTRAFREQNCELL"',
    """

    SELECT 
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
        "CELLSFORBIDDEN1A",
        "CELLSFORBIDDEN1B",
        "CIOOFFSET",
        "IDLEQOFFSET1SN",
        "IDLEQOFFSET2SN",
        "NCELLID",
        "NCELLRNCID",
        "NPRIOFLAG",
        "RNCID",
        "SIB11IND",
        "SIB12IND",
        "TPENALTYHCSRESELECT",
        "UINTRANCELLSRC",
        "NPRIO",
        "CONNQOFFSET1SN",
        "CONNQOFFSET2SN"
    FROM
    huawei_nbi_umts."UINTRAFREQNCELL"

    """
)

UIPSERVICEQOS = ReplaceableObject(
    'huawei_cm_3g."UIPSERVICEQOS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPINDEX",
        "LOGICRNCID",
        "RECINDEX",
        "TRAFFICPRIORITY",
        "TRAFFICTYPE"
    FROM
    huawei_nbi_umts."UIPSERVICEQOS"

    """
)

UIURGCONN = ReplaceableObject(
    'huawei_cm_3g."UIURGCONN"',
    """

    SELECT 
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
        "INTRAMBSCIND",
        "LOGICRNCID",
        "NBSCINDEX"
    FROM
    huawei_nbi_umts."UIURGCONN"

    """
)

UIUTIMERANDNUM = ReplaceableObject(
    'huawei_cm_3g."UIUTIMERANDNUM"',
    """

    SELECT 
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
        "CNOPINDEX",
        "IGORTMR",
        "INTRTMR",
        "LOGICRNCID",
        "RAFCTMR",
        "RATCTMR",
        "RSTRSNDNUM",
        "STATEINDTMR"
    FROM
    huawei_nbi_umts."UIUTIMERANDNUM"

    """
)

UKPIALMTHD = ReplaceableObject(
    'huawei_cm_3g."UKPIALMTHD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRRABABNORMRELRATIOTHD",
        "AMRRABESTABATTMINNUM",
        "AMRRABESTABSUCCRATIOTHD",
        "AMRRABRELMINNUM",
        "HSDPARABESTATTMINNUM",
        "HSDPARABESTSUCCRATIOTHD",
        "HSUPARABESTATTMINNUM",
        "HSUPARABESTSUCCRATIOTHD",
        "KPIALARMCHKTIMES",
        "KPIALARMSWITCH",
        "PSRABABNORMRELRATIOTHD",
        "PSRABESTATTMINNUM",
        "PSRABESTSUCCRATIOTHD",
        "PSRABRELMINNUM",
        "RRCCONNESTABATTMINNUM",
        "RRCCONNESTABSUCCRATIOTHD",
        "VPRABABNORMRELRATIOTHD",
        "VPRABESTATTMINNUM",
        "VPRABESTSUCCRATIOTHD",
        "VPRABRELMINNUM"
    FROM
    huawei_nbi_umts."UKPIALMTHD"

    """
)

ULAC = ReplaceableObject(
    'huawei_cm_3g."ULAC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPINDEX",
        "LAC",
        "LOGICRNCID",
        "PLMNVALTAGMAX",
        "PLMNVALTAGMIN"
    FROM
    huawei_nbi_umts."ULAC"

    """
)

ULDCALGOPARA = ReplaceableObject(
    'huawei_cm_3g."ULDCALGOPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LDCSWITCH",
        "LDRFIRSTPRI",
        "LDRFOURTHPRI",
        "LDRSECONDPRI",
        "LDRTHIRDPRI",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."ULDCALGOPARA"

    """
)

ULDCPERIOD = ReplaceableObject(
    'huawei_cm_3g."ULDCPERIOD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CLBPERIODTIMERLEN",
        "FAIRNESSPERIODTIMERLEN",
        "INTRAFREQLDBPERIODTIMERLEN",
        "INTRAFREQULBPERIODTIMERLEN",
        "LDRPERIODTIMERLEN",
        "LOGICRNCID",
        "OLCPERIODTIMERLEN",
        "PUCPERIODTIMERLEN"
    FROM
    huawei_nbi_umts."ULDCPERIOD"

    """
)

ULDM = ReplaceableObject(
    'huawei_cm_3g."ULDM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CHOICERPRTUNITFORDLBASICMEAS",
        "CHOICERPRTUNITFORDLOLCMEAS",
        "CHOICERPRTUNITFORHSDPAPWRMEAS",
        "CHOICERPRTUNITFORHSDPARATEMEAS",
        "CHOICERPRTUNITFORHSUPARATEMEAS",
        "CHOICERPRTUNITFORULBASICMEAS",
        "CHOICERPRTUNITFORULOLCMEAS",
        "DLBASICCOMMMEASFILTERCOEFF",
        "DLCACAVGFILTERLEN",
        "DLLDRAVGFILTERLEN",
        "DLOLCAVGFILTERLEN",
        "DLOLCMEASFILTERCOEFF",
        "DLOLCTRIGHYST",
        "HSDPANEEDPWRFILTERLEN",
        "HSDPAPRVIDBITRATEFILTERLEN",
        "HSUPAPRVIDBITRATEFILTERLEN",
        "LDBAVGFILTERLEN",
        "LOADLEVELFORLTE",
        "LOGICRNCID",
        "MAXMEASCONTINVALIDTIMES",
        "PERIODPROTECTTIMERCOEFF",
        "PUCAVGFILTERLEN",
        "TENMSECFORDLBASICMEAS",
        "TENMSECFORDLOLCMEAS",
        "TENMSECFORHSDPAPRVIDRATEMEAS",
        "TENMSECFORHSDPAPWRMEAS",
        "TENMSECFORHSUPAPRVIDRATEMEAS",
        "TENMSECFORULBASICMEAS",
        "TENMSECFORULOLCMEAS",
        "ULBASICCOMMMEASFILTERCOEFF",
        "ULBAVGFILTERLEN",
        "ULCACAVGFILTERLEN",
        "ULLDRAVGFILTERLEN",
        "ULOLCAVGFILTERLEN",
        "ULOLCMEASFILTERCOEFF",
        "ULOLCTRIGHYST"
    FROM
    huawei_nbi_umts."ULDM"

    """
)

ULOCELL = ReplaceableObject(
    'huawei_cm_3g."ULOCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOCELL",
        "LOGICRNCID",
        "NODEBID"
    FROM
    huawei_nbi_umts."ULOCELL"

    """
)

UMBSCCRRM = ReplaceableObject(
    'huawei_cm_3g."UMBSCCRRM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "COMMONMEASUREMENTPERIOD",
        "IRATCOMMONMEASSWITCH",
        "LOADHOON3G2GLDIND",
        "LOGICRNCID",
        "MBSC2GLOADADJUSTCOEFF",
        "MBSC3G2GLDBLCCSDELTATHRD",
        "MBSC3G2GLDBLCPSDELTATHRD",
        "MBSCLDRREDIRFACTOR",
        "MBSCNCOVHOON2GLDIND",
        "MBSCNONLDRREDIRFACTOR",
        "MBSCREQGERANINFOSWITCH",
        "MBSCSDIFFLDBPHASESWITCH",
        "MBSCSERVICEDIFFLDBSWITCH"
    FROM
    huawei_nbi_umts."UMBSCCRRM"

    """
)

UMCDRD = ReplaceableObject(
    'huawei_cm_3g."UMCDRD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BLINDDRDEXCEPTHRETRYSWITCH",
        "DRDFAIPENALTYPERIODNUM",
        "HRETRYTIMERLENGTH",
        "LOGICRNCID",
        "PRDREPORTINTERVAL",
        "TARGETFREQTHDECN0",
        "TARGETFREQTHDRSCP",
        "UESPDOPTSWITCH"
    FROM
    huawei_nbi_umts."UMCDRD"

    """
)

UMCLDR = ReplaceableObject(
    'huawei_cm_3g."UMCLDR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERFREQMEASTIME",
        "LOGICRNCID",
        "PRDREPORTINTERVAL",
        "TARGETFREQTHDECN0",
        "TARGETFREQTHDRSCP",
        "UESPDOPTSWITCH"
    FROM
    huawei_nbi_umts."UMCLDR"

    """
)

UMRSWITCH = ReplaceableObject(
    'huawei_cm_3g."UMRSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UMRSWITCH"

    """
)

UMULTIRABHOCOV = ReplaceableObject(
    'huawei_cm_3g."UMULTIRABHOCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSPSMRABTHD2DECN0",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UMULTIRABHOCOV"

    """
)

UNBSC = ReplaceableObject(
    'huawei_cm_3g."UNBSC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "NBSCINDEX",
        "NBSCNAME"
    FROM
    huawei_nbi_umts."UNBSC"

    """
)

UNCELLDETECTSWITCH = ReplaceableObject(
    'huawei_cm_3g."UNCELLDETECTSWITCH"',
    """

    SELECT 
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
        "INTERFREQNCELLDETECTSWITCH",
        "INTERRATNCELLDETECTSWITCH",
        "INTRAFREQNCELLDETECTSWITCH",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UNCELLDETECTSWITCH"

    """
)

UNCP = ReplaceableObject(
    'huawei_cm_3g."UNCP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CARRYLNKT",
        "LOGICRNCID",
        "NODEBID",
        "SCTPLNKID",
        "SAALLNKN"
    FROM
    huawei_nbi_umts."UNCP"

    """
)

UNODEB = ReplaceableObject(
    'huawei_cm_3g."UNODEB"',
    """

    SELECT 
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
        "AUTOHOMINGFLAG",
        "CNOPINDEX",
        "DSSFLAG",
        "HOSTTYPE",
        "LOGICRNCID",
        "NODEBID",
        "NODEBNAME",
        "NODEBPROTCLVER",
        "NODEBTRACESWITCH",
        "RSCMNGMODE",
        "SATELLITEIND",
        "SHARINGTYPE",
        "TNLBEARERTYPE",
        "TRANSDELAY"
    FROM
    huawei_nbi_umts."UNODEB"

    """
)

UNODEBALGOPARA = ReplaceableObject(
    'huawei_cm_3g."UNODEBALGOPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HSUPACECONSUMESELECTION",
        "LOGICRNCID",
        "NODEBHSDPAMAXUSERNUM",
        "NODEBHSUPAMAXUSERNUM",
        "NODEBID",
        "NODEBLDCALGOSWITCH"
    FROM
    huawei_nbi_umts."UNODEBALGOPARA"

    """
)

UNODEBIP = ReplaceableObject(
    'huawei_cm_3g."UNODEBIP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IPSN",
        "IPSRN",
        "LOGICRNCID",
        "NBIPOAMIP",
        "NBIPOAMMASK",
        "NBTRANTP",
        "NODEBID",
        "VLANFLAG",
        "ATMSN",
        "ATMSRN",
        "NBATMOAMIP",
        "NBATMOAMMASK",
        "NBCTRLSN"
    FROM
    huawei_nbi_umts."UNODEBIP"

    """
)

UNODEBLDR = ReplaceableObject(
    'huawei_cm_3g."UNODEBLDR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DLCSINTERRATSHOULDBEHOUENUM",
        "DLCSINTERRATSHOULDNOTHOUENUM",
        "DLLDRAMRRATEREDUCTIONRABNUM",
        "DLLDRBERATEREDUCTIONRABNUM",
        "DLLDRFIFTHACTION",
        "DLLDRFIRSTACTION",
        "DLLDRFOURTHACTION",
        "DLLDRPSRTQOSRENEGRABNUM",
        "DLLDRSECONDACTION",
        "DLLDRSEVENTHACTION",
        "DLLDRSIXTHACTION",
        "DLLDRTHIRDACTION",
        "DLPSINTERRATSHOULDBEHOUENUM",
        "DLPSINTERRATSHOULDNOTHOUENUM",
        "LOGICRNCID",
        "NODEBID",
        "ULCSINTERRATSHOULDBEHOUENUM",
        "ULCSINTERRATSHOULDNOTHOUENUM",
        "ULINTERFREQHOCELDRSPACETHD",
        "ULLDRAMRRATEREDUCTIONRABNUM",
        "ULLDRBERATEREDUCTIONRABNUM",
        "ULLDRCREDITSFRESTHD",
        "ULLDREIGHTHACTION",
        "ULLDRFIFTHACTION",
        "ULLDRFIRSTACTION",
        "ULLDRFOURTHACTION",
        "ULLDRPSRTQOSRENEGRABNUM",
        "ULLDRSECONDACTION",
        "ULLDRSEVENTHACTION",
        "ULLDRSIXTHACTION",
        "ULLDRTHIRDACTION",
        "ULPSINTERRATSHOULDBEHOUENUM",
        "ULPSINTERRATSHOULDNOTHOUENUM"
    FROM
    huawei_nbi_umts."UNODEBLDR"

    """
)

UNODEBMNTMODE = ReplaceableObject(
    'huawei_cm_3g."UNODEBMNTMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "MNTMODE",
        "NODEBID",
        "ET",
        "ST"
    FROM
    huawei_nbi_umts."UNODEBMNTMODE"

    """
)

UNODEBOLC = ReplaceableObject(
    'huawei_cm_3g."UNODEBOLC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IUBDLOLCRELRABNUM",
        "IUBULOLCRELRABNUM",
        "LOGICRNCID",
        "NODEBID"
    FROM
    huawei_nbi_umts."UNODEBOLC"

    """
)

UNRIGLBCNIDMAP = ReplaceableObject(
    'huawei_cm_3g."UNRIGLBCNIDMAP"',
    """

    SELECT 
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
        "CNOPINDEX",
        "LOGICRNCID",
        "NRI"
    FROM
    huawei_nbi_umts."UNRIGLBCNIDMAP"

    """
)

UNRNC = ReplaceableObject(
    'huawei_cm_3g."UNRNC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSVOICEOVERHSPASUPPIND",
        "DPX",
        "HHORELOCPROCSWITCH",
        "HHOTRIG",
        "IUBCPPRIVATEINTERFACESWITCH",
        "IUBUPPRIVATEINTERFACESWITCH",
        "IUREXISTIND",
        "IURHSDPASUPPIND",
        "IURHSUPASUPPIND",
        "LOGICRNCID",
        "NRNCID",
        "PROCESSSWITCH",
        "PSBEPROCTYPE",
        "RNCPROTCLVER",
        "SERVICEIND",
        "SHOTRIG",
        "STATEINDTMR",
        "SUPPIURCCH",
        "TNLBEARERTYPE",
        "WAMRSUPPIND"
    FROM
    huawei_nbi_umts."UNRNC"

    """
)

UOPERATORCFGPARA = ReplaceableObject(
    'huawei_cm_3g."UOPERATORCFGPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPINDEX",
        "CSINFOUPDFLAG",
        "CSNRICFGMODE",
        "CSNRILENGTH",
        "LOGICRNCID",
        "NNSFTMR",
        "NULLNRI",
        "NULLNRIOPTSWITCH",
        "PSINFOUPDFLAG",
        "PSNRICFGMODE",
        "PSNRILENGTH"
    FROM
    huawei_nbi_umts."UOPERATORCFGPARA"

    """
)

UOPERATORSHARINGMODE = ReplaceableObject(
    'huawei_cm_3g."UOPERATORSHARINGMODE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTERPLMNHOALLOWEDINTERRAT",
        "INTERPLMNHOALLOWEDINTRARAT",
        "INTERPLMNMULTICARRSWITCH",
        "LOGICRNCID",
        "MOCNSUPPORT",
        "RANSHARINGSUPPORT"
    FROM
    huawei_nbi_umts."UOPERATORSHARINGMODE"

    """
)

UPCCPCH = ReplaceableObject(
    'huawei_cm_3g."UPCCPCH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "PHYCHID"
    FROM
    huawei_nbi_umts."UPCCPCH"

    """
)

UPCH = ReplaceableObject(
    'huawei_cm_3g."UPCH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "PCHPOWER",
        "PHYCHID",
        "RATEMATCHINGATTR",
        "TOAWE",
        "TOAWS",
        "TRCHID"
    FROM
    huawei_nbi_umts."UPCH"

    """
)

UPCHDYNTFS = ReplaceableObject(
    'huawei_cm_3g."UPCHDYNTFS"',
    """

    SELECT 
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
        "LOGICRNCID",
        "RLCSIZE",
        "TBNUMBER1",
        "TBNUMBER2",
        "TFSNUMBER",
        "TRCHID"
    FROM
    huawei_nbi_umts."UPCHDYNTFS"

    """
)

UPCPICH = ReplaceableObject(
    'huawei_cm_3g."UPCPICH"',
    """

    SELECT 
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
        "DSSSMALLCOVPCPICHPOWER",
        "LOGICRNCID",
        "MAXPCPICHPOWER",
        "MINPCPICHPOWER",
        "PCPICHPOWER",
        "PHYCHID"
    FROM
    huawei_nbi_umts."UPCPICH"

    """
)

UPICH = ReplaceableObject(
    'huawei_cm_3g."UPICH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "PHYCHID",
        "PICHID",
        "PICHMODE",
        "STTDIND"
    FROM
    huawei_nbi_umts."UPICH"

    """
)

UPOOLLOADSHAREPARA = ReplaceableObject(
    'huawei_cm_3g."UPOOLLOADSHAREPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CPLOADSHARETYPE",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UPOOLLOADSHAREPARA"

    """
)

UPOOLREDUNDANCY = ReplaceableObject(
    'huawei_cm_3g."UPOOLREDUNDANCY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "REDUNDANCYMODE"
    FROM
    huawei_nbi_umts."UPOOLREDUNDANCY"

    """
)

UPRACHACTOASCMAP = ReplaceableObject(
    'huawei_cm_3g."UPRACHACTOASCMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AC09TOASC",
        "AC10TOASC",
        "AC11TOASC",
        "AC12TOASC",
        "AC13TOASC",
        "AC14TOASC",
        "AC15TOASC",
        "CELLID",
        "LOGICRNCID",
        "PHYCHID"
    FROM
    huawei_nbi_umts."UPRACHACTOASCMAP"

    """
)

UPRACHASC = ReplaceableObject(
    'huawei_cm_3g."UPRACHASC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ACCESSSERVICECLASS",
        "AVAILABLESIGNATUREENDINDEX",
        "AVAILABLESIGNATURESTARTINDEX",
        "AVAILABLESUBCHANNELCTRLWORD",
        "CELLID",
        "LOGICRNCID",
        "PHYCHID"
    FROM
    huawei_nbi_umts."UPRACHASC"

    """
)

UPRACHBASIC = ReplaceableObject(
    'huawei_cm_3g."UPRACHBASIC"',
    """

    SELECT 
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
        "CELLID",
        "CONSTANTVALUE",
        "CTFCSIZE",
        "LOGICRNCID",
        "PHYCHID",
        "POWERRAMPSTEP",
        "PREAMBLERETRANSMAX",
        "PREAMBLESIGNATURES",
        "RACHSUBCHNO"
    FROM
    huawei_nbi_umts."UPRACHBASIC"

    """
)

UPRACHSLOTFORMAT = ReplaceableObject(
    'huawei_cm_3g."UPRACHSLOTFORMAT"',
    """

    SELECT 
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
        "LOGICRNCID",
        "PHYCHID",
        "SLOTFORMAT1",
        "SLOTFORMAT2",
        "SLOTFORMAT3",
        "SLOTFORMAT4",
        "SLOTFORMATNUM"
    FROM
    huawei_nbi_umts."UPRACHSLOTFORMAT"

    """
)

UPRACHTFC = ReplaceableObject(
    'huawei_cm_3g."UPRACHTFC"',
    """

    SELECT 
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
        "CTFC",
        "GAINFACTORBETAC",
        "GAINFACTORBETAD",
        "LOGICRNCID",
        "PHYCHID",
        "POWEROFFSETPPM"
    FROM
    huawei_nbi_umts."UPRACHTFC"

    """
)

UPSCH = ReplaceableObject(
    'huawei_cm_3g."UPSCH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "PHYCHID",
        "PSCHPOWER"
    FROM
    huawei_nbi_umts."UPSCH"

    """
)

UPSINACTTIMER = ReplaceableObject(
    'huawei_cm_3g."UPSINACTTIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "PROTECTTMRFORBAC",
        "PROTECTTMRFORCON",
        "PROTECTTMRFORIMSSIG",
        "PROTECTTMRFORINT",
        "PROTECTTMRFORSTR",
        "PSINACTTMRFORBAC",
        "PSINACTTMRFORCON",
        "PSINACTTMRFORFSTDRMDCH",
        "PSINACTTMRFORFSTDRMFACH",
        "PSINACTTMRFORIMSSIG",
        "PSINACTTMRFORINT",
        "PSINACTTMRFORPREFSTDRM",
        "PSINACTTMRFORSTR"
    FROM
    huawei_nbi_umts."UPSINACTTIMER"

    """
)

UPTTSTATETRANS = ReplaceableObject(
    'huawei_cm_3g."UPTTSTATETRANS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "PTTCPC2EFACHSTATETRANSTIMER",
        "PTTCPC2FSTATETRANSTIMER",
        "PTTDH2EFACHSTATETRANSTIMER",
        "PTTDH2FSTATETRANSTIMER",
        "PTTDH2FTVMPTAT",
        "PTTDH2FTVMTHD",
        "PTTDH2FTVMTIMETOTRIG",
        "PTTE2FTHROUMEASPERIOD",
        "PTTE2FTHROUPTAT",
        "PTTE2FTHROUTHD",
        "PTTE2FTHROUTIMETOTRIG",
        "PTTEF2DHTVMTHD",
        "PTTEF2DHTVMTIMETOTRIG",
        "PTTF2DHTVMTHD",
        "PTTF2DHTVMTIMETOTRIG",
        "PTTF2PMCMODSWITCH",
        "PTTF2PSTATETRANSTIMER",
        "PTTF2PTVMPTAT",
        "PTTF2PTVMTHD",
        "PTTF2PTVMTIMETOTRIG"
    FROM
    huawei_nbi_umts."UPTTSTATETRANS"

    """
)

UQOSACT = ReplaceableObject(
    'huawei_cm_3g."UQOSACT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AMRQOSPERFORM",
        "BEDLACT1",
        "BEDLACT2",
        "BEDLACT3",
        "BEINTERIURRATEUPTIMER",
        "BEQOSPERFORM",
        "BEULACT1",
        "BEULACT2",
        "BEULACT3",
        "BEULEVTRIGIND",
        "BEULQOS5AMCSWITCH",
        "BEULQOS6A1MCSWITCH",
        "BEULQOS6DMCSWITCH",
        "BEULRATEADJTIMERLEN",
        "DRNCBEDLRLCQOSSWITCH",
        "LOGICRNCID",
        "SRNCBEDLRLCQOSSWITCH",
        "VPQOSPERFORM",
        "AMRULRATEADJTIMERLEN",
        "DLQOSAMRADJSWITCH",
        "DLQOSAMRINTERFREQHOSWITCH",
        "DLQOSAMRINTERRATHOSWITCH",
        "DLQOSWAMRADJSWITCH",
        "DLQOSWAMRINTERFREQHOSWITCH",
        "DLQOSWAMRINTERRATHOSWITCH",
        "ULQOSAMRADJSWITCH",
        "ULQOSAMRINTERFREQHOSWITCH",
        "ULQOSAMRINTERRATHOSWITCH",
        "ULQOSWAMRADJSWITCH",
        "ULQOSWAMRINTERFREQHOSWITCH",
        "ULQOSWAMRINTERRATHOSWITCH",
        "WAMRULRATEADJTIMERLEN"
    FROM
    huawei_nbi_umts."UQOSACT"

    """
)

UQOSALGOPARA = ReplaceableObject(
    'huawei_cm_3g."UQOSALGOPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "USERMATCHPRIORITY",
        "USERPOLICYSWITCH"
    FROM
    huawei_nbi_umts."UQOSALGOPARA"

    """
)

UQOSHO = ReplaceableObject(
    'huawei_cm_3g."UQOSHO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DLQOSMCTIMERLEN",
        "DLRSCPQOSHYST",
        "LOGICRNCID",
        "ULQOSMCTIMERLEN",
        "USEDFREQMEASQUANTITYFORQOS3A"
    FROM
    huawei_nbi_umts."UQOSHO"

    """
)

UQUALITYMEAS = ReplaceableObject(
    'huawei_cm_3g."UQUALITYMEAS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CHOICERPTUNITFORAMRE",
        "CHOICERPTUNITFORBEE",
        "CHOICERPTUNITFORBEF",
        "CHOICERPTUNITFORVPE",
        "DLAMRTRIGTIMEE",
        "DLBETRIGTIMEE",
        "DLBETRIGTIMEF",
        "DLMEASFILTERCOEF",
        "DLVPTRIGTIMEE",
        "LOGICRNCID",
        "TENMSECFORAMRE",
        "TENMSECFORBEE",
        "TENMSECFORBEF",
        "TENMSECFORVPE",
        "ULAMRTRIGTIME6A1",
        "ULAMRTRIGTIME6A2",
        "ULAMRTRIGTIME6B1",
        "ULAMRTRIGTIME6B2",
        "ULAMRTRIGTIME6D",
        "ULBETRIGTIME6A1",
        "ULBETRIGTIME6A2",
        "ULBETRIGTIME6B1",
        "ULBETRIGTIME6B2",
        "ULBETRIGTIME6D",
        "ULMEASFILTERCOEF",
        "ULVPTRIGTIME6A1",
        "ULVPTRIGTIME6B1",
        "ULVPTRIGTIME6D"
    FROM
    huawei_nbi_umts."UQUALITYMEAS"

    """
)

UQUEUEPREEMPT = ReplaceableObject(
    'huawei_cm_3g."UQUEUEPREEMPT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSP2DPREEMPTSWITCH",
        "EMCPREEREFVULNSWITCH",
        "LOGICRNCID",
        "MULTCODEPREEMPTALGOSWITCH",
        "PREEMPTALGOSWITCH",
        "PREEMPTENHSWITCH",
        "PREEMPTREFARPSWITCH",
        "PSBERRCPREEMPTVULNERABLE",
        "PTTPREEMPTALGOSWITCH",
        "PTUSERABSOLUTEPRIORITY",
        "QUEUEALGOSWITCH"
    FROM
    huawei_nbi_umts."UQUEUEPREEMPT"

    """
)

URAC = ReplaceableObject(
    'huawei_cm_3g."URAC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPINDEX",
        "LAC",
        "LOGICRNCID",
        "PLMNVALTAGMAX",
        "PLMNVALTAGMIN",
        "RAC"
    FROM
    huawei_nbi_umts."URAC"

    """
)

URACH = ReplaceableObject(
    'huawei_cm_3g."URACH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "MMAX",
        "NB01MAX",
        "NB01MIN",
        "PHYCHID",
        "RATEMATCHINGATTR",
        "TRCHID"
    FROM
    huawei_nbi_umts."URACH"

    """
)

URACHDYNTFS = ReplaceableObject(
    'huawei_cm_3g."URACHDYNTFS"',
    """

    SELECT 
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
        "LOGICRNCID",
        "RLCSIZE",
        "TBNUMBER1",
        "TFSNUMBER",
        "TRCHID"
    FROM
    huawei_nbi_umts."URACHDYNTFS"

    """
)

URACHMEASUREPARA = ReplaceableObject(
    'huawei_cm_3g."URACHMEASUREPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ECN0ADJSTEP",
        "ECN0ADJTIMERLEN",
        "ECN0MAXDOWNADJSTEP",
        "ECN0MAXUPADJSTEP",
        "LOGICRNCID",
        "MAXECN0VALUE",
        "MINECN0VALUE",
        "TAGETRLCRETRANS"
    FROM
    huawei_nbi_umts."URACHMEASUREPARA"

    """
)

UREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UREDIRECTION"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "REDIRSWITCH",
        "TRAFFICTYPE"
    FROM
    huawei_nbi_umts."UREDIRECTION"

    """
)

URNCBASIC = ReplaceableObject(
    'huawei_cm_3g."URNCBASIC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOADSHARINGTYPE",
        "NSAP",
        "REDUNDANCYTYPE",
        "RNCID"
    FROM
    huawei_nbi_umts."URNCBASIC"

    """
)

URNCCBPARA = ReplaceableObject(
    'huawei_cm_3g."URNCCBPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CBSWITCH",
        "CTCHSWITCH",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."URNCCBPARA"

    """
)

URNCCELLSHUTDOWNPARA = ReplaceableObject(
    'huawei_cm_3g."URNCCELLSHUTDOWNPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DYNCELLOPENJUDGETIMERLEN",
        "DYNCELLSHUTDOWNPROTECTTIMERLEN",
        "DYNCELLSHUTDOWNSWITCH",
        "IRATSHUTDOWNADJTIME",
        "IRATSWITCHONHYSTTIMELEN",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."URNCCELLSHUTDOWNPARA"

    """
)

URNCINPOOLRRMALGO = ReplaceableObject(
    'huawei_cm_3g."URNCINPOOLRRMALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "PARALLELDATASYNTHD"
    FROM
    huawei_nbi_umts."URNCINPOOLRRMALGO"

    """
)

URRCESTCAUSE = ReplaceableObject(
    'huawei_cm_3g."URRCESTCAUSE"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "EFACHSWITCH",
        "LOGICRNCID",
        "RRCCAUSE",
        "SIGCHTYPE"
    FROM
    huawei_nbi_umts."URRCESTCAUSE"

    """
)

URRCTRLSWITCH = ReplaceableObject(
    'huawei_cm_3g."URRCTRLSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "IUBPRIVATEINTERFACESWITCH",
        "LOGICRNCID",
        "PROCESSSWITCH",
        "PROCESSSWITCH2",
        "PROCESSSWITCH5"
    FROM
    huawei_nbi_umts."URRCTRLSWITCH"

    """
)

USAC = ReplaceableObject(
    'huawei_cm_3g."USAC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPINDEX",
        "LAC",
        "LOGICRNCID",
        "SAC"
    FROM
    huawei_nbi_umts."USAC"

    """
)

USATLDCPERIOD = ReplaceableObject(
    'huawei_cm_3g."USATLDCPERIOD"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CLBPERIODTIMERLEN",
        "FAIRNESSPERIODTIMERLEN",
        "INTRAFREQLDBPERIODTIMERLEN",
        "INTRAFREQULBPERIODTIMERLEN",
        "LDRPERIODTIMERLEN",
        "LOGICRNCID",
        "OLCPERIODTIMERLEN",
        "PUCPERIODTIMERLEN"
    FROM
    huawei_nbi_umts."USATLDCPERIOD"

    """
)

USATLDM = ReplaceableObject(
    'huawei_cm_3g."USATLDM"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CHOICERPRTUNITFORDLBASICMEAS",
        "CHOICERPRTUNITFORDLOLCMEAS",
        "CHOICERPRTUNITFORHSDPAPWRMEAS",
        "CHOICERPRTUNITFORHSDPARATEMEAS",
        "CHOICERPRTUNITFORULBASICMEAS",
        "CHOICERPRTUNITFORULOLCMEAS",
        "DLBASICCOMMMEASFILTERCOEFF",
        "DLCACAVGFILTERLEN",
        "DLLDRAVGFILTERLEN",
        "DLOLCAVGFILTERLEN",
        "DLOLCMEASFILTERCOEFF",
        "DLOLCTRIGHYST",
        "HSDPANEEDPWRFILTERLEN",
        "HSDPAPRVIDBITRATEFILTERLEN",
        "LDBAVGFILTERLEN",
        "LOGICRNCID",
        "MAXMEASCONTINVALIDTIMES",
        "PERIODPROTECTTIMERCOEFF",
        "PUCAVGFILTERLEN",
        "TENMSECFORDLBASICMEAS",
        "TENMSECFORDLOLCMEAS",
        "TENMSECFORHSDPAPRVIDRATEMEAS",
        "TENMSECFORHSDPAPWRMEAS",
        "TENMSECFORULBASICMEAS",
        "TENMSECFORULOLCMEAS",
        "ULBASICCOMMMEASFILTERCOEFF",
        "ULBAVGFILTERLEN",
        "ULCACAVGFILTERLEN",
        "ULLDRAVGFILTERLEN",
        "ULOLCAVGFILTERLEN",
        "ULOLCMEASFILTERCOEFF",
        "ULOLCTRIGHYST"
    FROM
    huawei_nbi_umts."USATLDM"

    """
)

USCCPCHBASIC = ReplaceableObject(
    'huawei_cm_3g."USCCPCHBASIC"',
    """

    SELECT 
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
        "CELLID",
        "CTFCSIZE",
        "LOGICRNCID",
        "PHYCHID",
        "SCCPCHOFFSET",
        "SCRAMBCODE",
        "SLOTFORMAT",
        "STTDIND",
        "TFCIPRESENCE"
    FROM
    huawei_nbi_umts."USCCPCHBASIC"

    """
)

USCCPCHTFC = ReplaceableObject(
    'huawei_cm_3g."USCCPCHTFC"',
    """

    SELECT 
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
        "CTFC",
        "LOGICRNCID",
        "PHYCHID"
    FROM
    huawei_nbi_umts."USCCPCHTFC"

    """
)

USCHEDULEPRIOMAP = ReplaceableObject(
    'huawei_cm_3g."USCHEDULEPRIOMAP"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "SPI",
        "THPCLASS",
        "TRAFFICCLASS",
        "USERPRIORITY"
    FROM
    huawei_nbi_umts."USCHEDULEPRIOMAP"

    """
)

USERVMEAPARA = ReplaceableObject(
    'huawei_cm_3g."USERVMEAPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "SERVMEATYPE"
    FROM
    huawei_nbi_umts."USERVMEAPARA"

    """
)

USMLC = ReplaceableObject(
    'huawei_cm_3g."USMLC"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AGPSADDASSDATASENDFLAG",
        "AGPSMETHODTYPE",
        "CELLIDRTTMETHODTYPE",
        "EMERGLCSSWITCH",
        "FORCEDSHOSWITCH",
        "IUPCRSPTIMERLEN",
        "LCSWORKMODE",
        "LOGICRNCID",
        "MAXGPSSATS",
        "OPTIONALIESENDSWITCH",
        "OTDOAMETHODTYPE",
        "RESULTGEOTYPE",
        "SMLCMETHOD",
        "UEASSAGPSASSDATASWITCH",
        "UEBASAGPSASSDATASWITCH"
    FROM
    huawei_nbi_umts."USMLC"

    """
)

USMLCCELL = ReplaceableObject(
    'huawei_cm_3g."USMLCCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AGPSACTIVATEFLAG",
        "ANTENNAALTITUDEMETER",
        "ANTENNALATITUDEDEGREE",
        "ANTENNALONGITUDEDEGREE",
        "ANTENNAOPENING",
        "ANTENNAORIENTATION",
        "CELLAVERAGEHEIGHT",
        "CELLENVIRONMENT",
        "CELLHEIGHTSTD",
        "CELLID",
        "CELLIDRTTACTIVATEFLAG",
        "CELLLOCCFGTYPE",
        "GCDF",
        "LOGICRNCID",
        "MAXANTENNARANGE",
        "MTRLGY",
        "OTDOAACTIVATEFLAG",
        "RNCID"
    FROM
    huawei_nbi_umts."USMLCCELL"

    """
)

USMLCEXT3GCELL = ReplaceableObject(
    'huawei_cm_3g."USMLCEXT3GCELL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "AGPSACTIVATEFLAG",
        "ANTENNAALTITUDEMETER",
        "ANTENNALATITUDEDEGREE",
        "ANTENNALONGITUDEDEGREE",
        "ANTENNAOPENING",
        "ANTENNAORIENTATION",
        "CELLAVERAGEHEIGHT",
        "CELLENVIRONMENT",
        "CELLHEIGHTSTD",
        "CELLID",
        "CELLIDRTTACTIVATEFLAG",
        "CELLLOCCFGTYPE",
        "GCDF",
        "LOGICRNCID",
        "MAXANTENNARANGE",
        "MTRLGY",
        "NRNCID",
        "OTDOAACTIVATEFLAG",
        "RXTXCHANDELAY",
        "TXCHANDELAY"
    FROM
    huawei_nbi_umts."USMLCEXT3GCELL"

    """
)

USPG = ReplaceableObject(
    'huawei_cm_3g."USPG"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "PRIORITYSERVICEFOREXTRAB",
        "PRIORITYSERVICEFORHSDPA",
        "PRIORITYSERVICEFORHSPART",
        "PRIORITYSERVICEFORHSUPA",
        "PRIORITYSERVICEFORR99NRT",
        "PRIORITYSERVICEFORR99RT",
        "SPGID"
    FROM
    huawei_nbi_umts."USPG"

    """
)

USPIWEIGHT = ReplaceableObject(
    'huawei_cm_3g."USPIWEIGHT"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "RATERANGESPIWEIGHTIND",
        "SPI",
        "SPIWEIGHT",
        "SPIWTFACTORFORHSUPASHO"
    FROM
    huawei_nbi_umts."USPIWEIGHT"

    """
)

USRBRATECOVSEL = ReplaceableObject(
    'huawei_cm_3g."USRBRATECOVSEL"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CSP2DSRBRATEBADECNOTHD",
        "CSP2DSRBRATEGOODECNOTHD",
        "LOGICRNCID",
        "R6UESRBHIGHRATECFGSWITCH",
        "RRCSETSRBRATEBADECNOTHD",
        "RRCSETSRBRATEGOODECNOTHD",
        "RRCSETUPSRBRATESELSET",
        "SRBRATECOVSELSWITCH"
    FROM
    huawei_nbi_umts."USRBRATECOVSEL"

    """
)

USRNSR = ReplaceableObject(
    'huawei_cm_3g."USRNSR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "SRNSRABCNDOMAINTYPE",
        "SRNSRDELAYOFFSET",
        "SRNSREXPIRYTIME",
        "SRNSRIURRESELECTTIMERLEN",
        "SRNSRSEPARATEDURATION",
        "SRNSRTRIGTIMER"
    FROM
    huawei_nbi_umts."USRNSR"

    """
)

USSCH = ReplaceableObject(
    'huawei_cm_3g."USSCH"',
    """

    SELECT 
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
        "LOGICRNCID",
        "PHYCHID",
        "SSCHPOWER"
    FROM
    huawei_nbi_umts."USSCH"

    """
)

USTATETIMER = ReplaceableObject(
    'huawei_cm_3g."USTATETIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CMCHRSRCRSPTMR",
        "CSFBUEDELAYRAUTIMER",
        "DRLAAL2ESTINDTMR",
        "DRLRECFGCMITTMR",
        "F2PDELRLCTMR",
        "HOASUTMR",
        "HOCELLUPDATERSPTMR",
        "HOPAGINGRSPTMR",
        "HOPHYCHRECFGTMR",
        "HORELOCREQTMR",
        "HOWTTRCHRECFGRSPTMR",
        "IUCSRELNORABTMR",
        "IUPSRELNORABTMR",
        "LOGICRNCID",
        "LOWRRCCONNREJWAITTMR",
        "RBRECFGRSPTMR",
        "RBRELRSPTMR",
        "RBSETUPRSPTMR",
        "RELOCANOTHERTMR",
        "RELOCCMDTMR",
        "RELOCCOMMITTMR",
        "RELOCDATAFWDTMR",
        "RELOCFAILIURELCMDTMR",
        "RELOCIURELCMDTMR",
        "RELOCMOBILCONFTMR",
        "RELOCPHYCHRECFGTMR",
        "RELOCUTRANHOCMPTMR",
        "RLRECFGREADYTMR",
        "RLRELRSPTMR",
        "RLRSTRTMR",
        "RLSETUPRSPTMR",
        "RRCCONNREJWAITTMR",
        "RRCINITDTTMR",
        "RRCIURELCMDTMR",
        "RRCPAINGTYPE1TMR",
        "RRCRELRETRANTMR",
        "RRCRLCACKCMPTMR",
        "RRCSECRTMODECMPTMR",
        "RRCUERSPTMR",
        "SYSHOPSRESUMETMR",
        "TTHDFORSFSTUSERIDENTIFY",
        "UECAPENQRSPTMR",
        "UECNTCHECKRSPTMR"
    FROM
    huawei_nbi_umts."USTATETIMER"

    """
)

UTHPCLASS = ReplaceableObject(
    'huawei_cm_3g."UTHPCLASS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "THP10CLASS",
        "THP11CLASS",
        "THP12CLASS",
        "THP13CLASS",
        "THP14CLASS",
        "THP15CLASS",
        "THP1CLASS",
        "THP2CLASS",
        "THP3CLASS",
        "THP4CLASS",
        "THP5CLASS",
        "THP6CLASS",
        "THP7CLASS",
        "THP8CLASS",
        "THP9CLASS"
    FROM
    huawei_nbi_umts."UTHPCLASS"

    """
)

UU2LTEHOCOV = ReplaceableObject(
    'huawei_cm_3g."UU2LTEHOCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "LTEPERIODREPORTINTERVAL",
        "LTEREPORTMODE",
        "PENALTYTIMEFORPHYCHFAIL",
        "TARGETRATTHDRSRP",
        "TARGETRATTHDRSRQ",
        "U2LPHYCHFAILNUM",
        "U2LTEHO2DEVENTTYPE",
        "U2LTEMEASTIME"
    FROM
    huawei_nbi_umts."UU2LTEHOCOV"

    """
)

UU2LTEHONCOV = ReplaceableObject(
    'huawei_cm_3g."UU2LTEHONCOV"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ANTIPINPANLTEFDDREDRSWITCH",
        "BESTCELLTRIGLTEMEASSWITCH",
        "HYSTFOR3C",
        "LOGICRNCID",
        "LTEMEASQUANOF3C",
        "LTEMEASTYPOF3C",
        "PENALTYTIMEFORPHYCHFAIL",
        "TARGETRATTHDRSRP",
        "TARGETRATTHDRSRQ",
        "TRIGTIME3C",
        "U2LNCOVRSCPPRDTIMER",
        "U2LNCOVRSCPTHD",
        "U2LPHYCHFAILNUM",
        "U2LPUNISHSWITCH",
        "U2LPUNISHTIMER",
        "U2LSERVMCTIMEOUTPUNISHTIME",
        "U2LSERVPRDTRIGTIMERLEN",
        "U2LSERVTRIGSOURCE",
        "U2LTEFILTERCOEF",
        "U2LTEMEASTIME"
    FROM
    huawei_nbi_umts."UU2LTEHONCOV"

    """
)

UUEA = ReplaceableObject(
    'huawei_cm_3g."UUEA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ENCRYPTIONALGO",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UUEA"

    """
)

UUESTATETRANS = ReplaceableObject(
    'huawei_cm_3g."UUESTATETRANS"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BASEDTIMEF2DPT",
        "BASEDTIMEF2DTHD",
        "BEEFACH2CPCTVMTHD",
        "BEEFACH2CPCTVMTIMETOTRIG",
        "BEEFACH2DTVMTHD",
        "BEEFACH2DTVMTIMETOTRIG",
        "BEEFACH2HTVMTHD",
        "BEEFACH2HTVMTIMETOTRIG",
        "BEERACH2CPCDLTVMTHD",
        "BEERACH2CPCULTVMTHD",
        "BEERACH2DTVMTHD",
        "BEERACH2EULTVMTHD",
        "BEERACH2HDLTVMTHD",
        "BEF2CPCETVMTHD",
        "BEF2CPCETVMTIMETOTRIG",
        "BEF2CPCHTVMTHD",
        "BEF2CPCHTVMTIMETOTRIG",
        "BEF2DHTVMTHDFORFACHCONG",
        "BEF2DTVMTHD",
        "BEF2DTVMTIMETOTRIG",
        "BEF2ETVMTHD",
        "BEF2ETVMTIMETOTRIG",
        "BEF2HTVMTHD",
        "BEF2HTVMTIMETOTRIG",
        "BEH2FTVMPTAT",
        "BEH2FTVMTHD",
        "BEH2FTVMTIMETOTRIG",
        "CELLRESELECTCOUNTER",
        "D2F2PTVMTHD",
        "D2FTVMPTAT",
        "D2FTVMTIMETOTRIG",
        "E2FTHROUMEASPERIOD",
        "E2FTHROUPTAT",
        "E2FTHROUTHD",
        "E2FTHROUTIMETOTRIG",
        "F2PTVMPTAT",
        "F2PTVMTIMETOTRIG",
        "FASTDORMANCYF2DHTVMTHD",
        "FDERACH2DULTVMTHD",
        "LOGICRNCID",
        "PARKINGBEF2DHTVMTHD",
        "PARKINGBEF2PTVMTHD",
        "PARKINGF2DHTVMPTAT",
        "PARKINGF2DHTVMTXIAT",
        "RTDH2FTVMPTAT",
        "RTDH2FTVMTHD",
        "RTDH2FTVMTIMETOTRIG",
        "RTEFACH2CPCTVMTHD",
        "RTEFACH2CPCTVMTIMETOTRIG",
        "RTEFACH2DHTVMTHD",
        "RTEFACH2DHTVMTIMETOTRIG",
        "RTF2CPCTVMTHD",
        "RTF2CPCTVMTIMETOTRIG",
        "RTF2DHTVMTHD",
        "RTF2DHTVMTIMETOTRIG",
        "TVMTHDFORSMARTP2D",
        "TXINTERRUPTAFTERTRIG"
    FROM
    huawei_nbi_umts."UUESTATETRANS"

    """
)

UUESTATETRANSTIMER = ReplaceableObject(
    'huawei_cm_3g."UUESTATETRANSTIMER"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "BECPC2EFACHSTATETRANSTIMER",
        "BECPC2FSTATETRANSTIMER",
        "BED2EFACHSTATETRANSTIMER",
        "BED2FSTATETRANSTIMER",
        "BEE2FSTATETRANSTIMER",
        "BEF2PSTATETRANSTIMER",
        "BEH2EFACHSTATETRANSTIMER",
        "BEH2FSTATETRANSTIMER",
        "CELLRESELECTTIMER",
        "D2PPSINACTTIMER",
        "LOGICRNCID",
        "PARKING4ADISCARDTIMER",
        "RTCPC2EFACHSTATETRANSTIMER",
        "RTCPC2FSTATETRANSTIMER",
        "RTDH2EFACHSTATETRANSTIMER",
        "RTDH2FSTATETRANSTIMER"
    FROM
    huawei_nbi_umts."UUESTATETRANSTIMER"

    """
)

UUIA = ReplaceableObject(
    'huawei_cm_3g."UUIA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "INTEGRITYPROTECTALGO",
        "LOGICRNCID"
    FROM
    huawei_nbi_umts."UUIA"

    """
)

UUPALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UUPALGOSWITCH"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "DPISOURCEPRIO",
        "LOGICRNCID",
        "QOSPOLICYSWITCH"
    FROM
    huawei_nbi_umts."UUPALGOSWITCH"

    """
)

UURA = ReplaceableObject(
    'huawei_cm_3g."UURA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CNOPINDEX",
        "LOGICRNCID",
        "URAID"
    FROM
    huawei_nbi_umts."UURA"

    """
)

UUSERGBR = ReplaceableObject(
    'huawei_cm_3g."UUSERGBR"',
    """

    SELECT 
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
        "DLGBR",
        "LOGICRNCID",
        "THPCLASS",
        "TRAFFICCLASS",
        "ULGBR",
        "USERPRIORITY"
    FROM
    huawei_nbi_umts."UUSERGBR"

    """
)

UUSERHAPPYBR = ReplaceableObject(
    'huawei_cm_3g."UUSERHAPPYBR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "HAPPYBR",
        "LOGICRNCID",
        "THPCLASS",
        "TRAFFICCLASS",
        "USERPRIORITY"
    FROM
    huawei_nbi_umts."UUSERHAPPYBR"

    """
)

UUSERMBR = ReplaceableObject(
    'huawei_cm_3g."UUSERMBR"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "CONVERDLMBR",
        "CONVERULMBR",
        "LOGICRNCID",
        "SINGALDLMBR",
        "SINGALULMBR",
        "STREAMDLMBR",
        "STREAMULMBR"
    FROM
    huawei_nbi_umts."UUSERMBR"

    """
)

UUSERPLNSHAREPARA = ReplaceableObject(
    'huawei_cm_3g."UUSERPLNSHAREPARA"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "USERPLNCPUSHARINGOUTOFFSET",
        "USERPLNCPUSHARINGOUTTHD"
    FROM
    huawei_nbi_umts."UUSERPLNSHAREPARA"

    """
)

UUSERPRIORITY = ReplaceableObject(
    'huawei_cm_3g."UUSERPRIORITY"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "ARP10PRIORITY",
        "ARP11PRIORITY",
        "ARP12PRIORITY",
        "ARP13PRIORITY",
        "ARP14PRIORITY",
        "ARP15PRIORITY",
        "ARP1PRIORITY",
        "ARP2PRIORITY",
        "ARP3PRIORITY",
        "ARP4PRIORITY",
        "ARP5PRIORITY",
        "ARP6PRIORITY",
        "ARP7PRIORITY",
        "ARP8PRIORITY",
        "ARP9PRIORITY",
        "CARRIERTYPEPRIORIND",
        "LOGICRNCID",
        "PRIORITYREFERENCE"
    FROM
    huawei_nbi_umts."UUSERPRIORITY"

    """
)

UVIPIMSI = ReplaceableObject(
    'huawei_cm_3g."UVIPIMSI"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "VIPIMSI"
    FROM
    huawei_nbi_umts."UVIPIMSI"

    """
)

UWPSALGO = ReplaceableObject(
    'huawei_cm_3g."UWPSALGO"',
    """

    SELECT 
        "FileName",
        "varDateTime",
        "ne_xsitype",
        "netype",
        "neversion",
        "neid",
        "module_type",
        "module_remark",
        "module_productversion",
        "LOGICRNCID",
        "NBMWPSALGORITHMSWITCH"
    FROM
    huawei_nbi_umts."UWPSALGO"

    """
)

VLANID = ReplaceableObject(
    'huawei_cm_3g."VLANID"',
    """

    SELECT 
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
    huawei_nbi_umts."VLANID"

    """
)


def upgrade():
    op.create_view(AAL2PATH)
    op.create_view(AAL2TMR)
    op.create_view(ADJMAP)
    op.create_view(ADJNODE)
    op.create_view(ATMTRF)
    op.create_view(CELLCBS)
    op.create_view(CELLERACH)
    op.create_view(CELLMIMO)
    op.create_view(CELLTEMPLATERSC)
    op.create_view(DEVIP)
    op.create_view(EMSIP)
    op.create_view(ETHIP)
    op.create_view(ETHPORT)
    op.create_view(ETHTRK)
    op.create_view(ETHTRKIP)
    op.create_view(ETHTRKLNK)
    op.create_view(filefooter)
    op.create_view(IPOAPVC)
    op.create_view(IPPOOL)
    op.create_view(IPPOOLIP)
    op.create_view(IPPOOLPM)
    op.create_view(IPRT)
    op.create_view(IU_ADJMAP)
    op.create_view(IU_ADJNODE)
    op.create_view(M3DE)
    op.create_view(M3LE)
    op.create_view(M3LKS)
    op.create_view(M3LNK)
    op.create_view(M3RT)
    op.create_view(MSP)
    op.create_view(MTP3TMR)
    op.create_view(N7DPC)
    op.create_view(NODEBEQUIPMENT)
    op.create_view(NODEBTEMPLATERSC)
    op.create_view(OPC)
    op.create_view(OPT)
    op.create_view(PHBMAP)
    op.create_view(PORTFLOWCTRLPARA)
    op.create_view(QUEUEMAP)
    op.create_view(SAALLNK)
    op.create_view(SCCPTMR)
    op.create_view(SCTPLNK)
    op.create_view(SCTPSRVPORT)
    op.create_view(SRCIPRT)
    op.create_view(SUBSESSION_NE)
    op.create_view(SYS)
    op.create_view(TRMFACTOR)
    op.create_view(TRMLOADTH)
    op.create_view(TRMMAP)
    op.create_view(U2GNCELL)
    op.create_view(UACALGO)
    op.create_view(UADAPALGOSWITCH)
    op.create_view(UADMCTRL)
    op.create_view(UAICH)
    op.create_view(UAMRC)
    op.create_view(UAMRCWB)
    op.create_view(UBCH)
    op.create_view(UCACALGOSWITCH)
    op.create_view(UCALLSHOCKCTRL)
    op.create_view(UCCP)
    op.create_view(UCELL)
    op.create_view(UCELLACCESSSTRICT)
    op.create_view(UCELLALGOSWITCH)
    op.create_view(UCELLCAC)
    op.create_view(UCELLCMCF)
    op.create_view(UCELLDCCC)
    op.create_view(UCELLDISTANCEREDIRECTION)
    op.create_view(UCELLDRD)
    op.create_view(UCELLDYNSHUTDOWN)
    op.create_view(UCELLFRC)
    op.create_view(UCELLHCS)
    op.create_view(UCELLHOCOMM)
    op.create_view(UCELLHSDPA)
    op.create_view(UCELLHSDPCCH)
    op.create_view(UCELLHSUPA)
    op.create_view(UCELLINTERFREQHOCOV)
    op.create_view(UCELLINTERRATHOCOV)
    op.create_view(UCELLINTERRATHONCOV)
    op.create_view(UCELLINTRAFREQHO)
    op.create_view(UCELLLDB)
    op.create_view(UCELLLDM)
    op.create_view(UCELLLDR)
    op.create_view(UCELLLICENSE)
    op.create_view(UCELLMEAS)
    op.create_view(UCELLNFREQPRIOINFO)
    op.create_view(UCELLOLC)
    op.create_view(UCELLPUC)
    op.create_view(UCELLREDIRECTION)
    op.create_view(UCELLRLACTTIME)
    op.create_view(UCELLRLPWR)
    op.create_view(UCELLSELRESEL)
    op.create_view(UCELLSIBSWITCH)
    op.create_view(UCELLUPDTCTRLSWITCH)
    op.create_view(UCELLURA)
    op.create_view(UCHLQUALITYEVALUATE)
    op.create_view(UCHPWROFFSET)
    op.create_view(UCIDCHG)
    op.create_view(UCLB)
    op.create_view(UCMCF)
    op.create_view(UCNDOMAIN)
    op.create_view(UCNNODE)
    op.create_view(UCNOPERATOR)
    op.create_view(UCNOPERGROUP)
    op.create_view(UCNTCHK)
    op.create_view(UCOIFTIMER)
    op.create_view(UCONNMODETIMER)
    op.create_view(UCORRMALGOSWITCH)
    op.create_view(UCORRMPARA)
    op.create_view(UCSVOICEPPC)
    op.create_view(UCTRLPLNSHAREPARA)
    op.create_view(UDCCC)
    op.create_view(UDISTANCEREDIRECTION)
    op.create_view(UDPUCFGDATA)
    op.create_view(UDRD)
    op.create_view(UDRDMIMO)
    op.create_view(UDSACAUTOALGO)
    op.create_view(UDTXDRXPARA)
    op.create_view(UEDCHRATEADJUSTSET)
    op.create_view(UEDCHTTIRECFG)
    op.create_view(UEVQIPARA)
    op.create_view(UEXT2GCELL)
    op.create_view(UEXT3GCELL)
    op.create_view(UEXT3GCELLINTRAFREQHO)
    op.create_view(UFACH)
    op.create_view(UFACHBANDWIDTH)
    op.create_view(UFACHDYNTFS)
    op.create_view(UFACHLOCH)
    op.create_view(UFDPCHPARA)
    op.create_view(UFDPCHRLPWR)
    op.create_view(UFRC)
    op.create_view(UFRCCHLTYPEPARA)
    op.create_view(UHCSHO)
    op.create_view(UHOCOMM)
    op.create_view(UHSSCCHLESSOPPARA)
    op.create_view(UIDLEMODETIMER)
    op.create_view(UINTERFREQHOCOV)
    op.create_view(UINTERFREQHONCOV)
    op.create_view(UINTERFREQNCELL)
    op.create_view(UINTERRATHOCOV)
    op.create_view(UINTERRATHONCOV)
    op.create_view(UINTRAFREQHO)
    op.create_view(UINTRAFREQNCELL)
    op.create_view(UIPSERVICEQOS)
    op.create_view(UIURGCONN)
    op.create_view(UIUTIMERANDNUM)
    op.create_view(UKPIALMTHD)
    op.create_view(ULAC)
    op.create_view(ULDCALGOPARA)
    op.create_view(ULDCPERIOD)
    op.create_view(ULDM)
    op.create_view(ULOCELL)
    op.create_view(UMBSCCRRM)
    op.create_view(UMCDRD)
    op.create_view(UMCLDR)
    op.create_view(UMRSWITCH)
    op.create_view(UMULTIRABHOCOV)
    op.create_view(UNBSC)
    op.create_view(UNCELLDETECTSWITCH)
    op.create_view(UNCP)
    op.create_view(UNODEB)
    op.create_view(UNODEBALGOPARA)
    op.create_view(UNODEBIP)
    op.create_view(UNODEBLDR)
    op.create_view(UNODEBMNTMODE)
    op.create_view(UNODEBOLC)
    op.create_view(UNRIGLBCNIDMAP)
    op.create_view(UNRNC)
    op.create_view(UOPERATORCFGPARA)
    op.create_view(UOPERATORSHARINGMODE)
    op.create_view(UPCCPCH)
    op.create_view(UPCH)
    op.create_view(UPCHDYNTFS)
    op.create_view(UPCPICH)
    op.create_view(UPICH)
    op.create_view(UPOOLLOADSHAREPARA)
    op.create_view(UPOOLREDUNDANCY)
    op.create_view(UPRACHACTOASCMAP)
    op.create_view(UPRACHASC)
    op.create_view(UPRACHBASIC)
    op.create_view(UPRACHSLOTFORMAT)
    op.create_view(UPRACHTFC)
    op.create_view(UPSCH)
    op.create_view(UPSINACTTIMER)
    op.create_view(UPTTSTATETRANS)
    op.create_view(UQOSACT)
    op.create_view(UQOSALGOPARA)
    op.create_view(UQOSHO)
    op.create_view(UQUALITYMEAS)
    op.create_view(UQUEUEPREEMPT)
    op.create_view(URAC)
    op.create_view(URACH)
    op.create_view(URACHDYNTFS)
    op.create_view(URACHMEASUREPARA)
    op.create_view(UREDIRECTION)
    op.create_view(URNCBASIC)
    op.create_view(URNCCBPARA)
    op.create_view(URNCCELLSHUTDOWNPARA)
    op.create_view(URNCINPOOLRRMALGO)
    op.create_view(URRCESTCAUSE)
    op.create_view(URRCTRLSWITCH)
    op.create_view(USAC)
    op.create_view(USATLDCPERIOD)
    op.create_view(USATLDM)
    op.create_view(USCCPCHBASIC)
    op.create_view(USCCPCHTFC)
    op.create_view(USCHEDULEPRIOMAP)
    op.create_view(USERVMEAPARA)
    op.create_view(USMLC)
    op.create_view(USMLCCELL)
    op.create_view(USMLCEXT3GCELL)
    op.create_view(USPG)
    op.create_view(USPIWEIGHT)
    op.create_view(USRBRATECOVSEL)
    op.create_view(USRNSR)
    op.create_view(USSCH)
    op.create_view(USTATETIMER)
    op.create_view(UTHPCLASS)
    op.create_view(UU2LTEHOCOV)
    op.create_view(UU2LTEHONCOV)
    op.create_view(UUEA)
    op.create_view(UUESTATETRANS)
    op.create_view(UUESTATETRANSTIMER)
    op.create_view(UUIA)
    op.create_view(UUPALGOSWITCH)
    op.create_view(UURA)
    op.create_view(UUSERGBR)
    op.create_view(UUSERHAPPYBR)
    op.create_view(UUSERMBR)
    op.create_view(UUSERPLNSHAREPARA)
    op.create_view(UUSERPRIORITY)
    op.create_view(UVIPIMSI)
    op.create_view(UWPSALGO)
    op.create_view(VLANID)


def downgrade():
    op.drop_view(AAL2PATH)
    op.drop_view(AAL2TMR)
    op.drop_view(ADJMAP)
    op.drop_view(ADJNODE)
    op.drop_view(ATMTRF)
    op.drop_view(CELLCBS)
    op.drop_view(CELLERACH)
    op.drop_view(CELLMIMO)
    op.drop_view(CELLTEMPLATERSC)
    op.drop_view(DEVIP)
    op.drop_view(EMSIP)
    op.drop_view(ETHIP)
    op.drop_view(ETHPORT)
    op.drop_view(ETHTRK)
    op.drop_view(ETHTRKIP)
    op.drop_view(ETHTRKLNK)
    op.drop_view(filefooter)
    op.drop_view(IPOAPVC)
    op.drop_view(IPPOOL)
    op.drop_view(IPPOOLIP)
    op.drop_view(IPPOOLPM)
    op.drop_view(IPRT)
    op.drop_view(IU_ADJMAP)
    op.drop_view(IU_ADJNODE)
    op.drop_view(M3DE)
    op.drop_view(M3LE)
    op.drop_view(M3LKS)
    op.drop_view(M3LNK)
    op.drop_view(M3RT)
    op.drop_view(MSP)
    op.drop_view(MTP3TMR)
    op.drop_view(N7DPC)
    op.drop_view(NODEBEQUIPMENT)
    op.drop_view(NODEBTEMPLATERSC)
    op.drop_view(OPC)
    op.drop_view(OPT)
    op.drop_view(PHBMAP)
    op.drop_view(PORTFLOWCTRLPARA)
    op.drop_view(QUEUEMAP)
    op.drop_view(SAALLNK)
    op.drop_view(SCCPTMR)
    op.drop_view(SCTPLNK)
    op.drop_view(SCTPSRVPORT)
    op.drop_view(SRCIPRT)
    op.drop_view(SUBSESSION_NE)
    op.drop_view(SYS)
    op.drop_view(TRMFACTOR)
    op.drop_view(TRMLOADTH)
    op.drop_view(TRMMAP)
    op.drop_view(U2GNCELL)
    op.drop_view(UACALGO)
    op.drop_view(UADAPALGOSWITCH)
    op.drop_view(UADMCTRL)
    op.drop_view(UAICH)
    op.drop_view(UAMRC)
    op.drop_view(UAMRCWB)
    op.drop_view(UBCH)
    op.drop_view(UCACALGOSWITCH)
    op.drop_view(UCALLSHOCKCTRL)
    op.drop_view(UCCP)
    op.drop_view(UCELL)
    op.drop_view(UCELLACCESSSTRICT)
    op.drop_view(UCELLALGOSWITCH)
    op.drop_view(UCELLCAC)
    op.drop_view(UCELLCMCF)
    op.drop_view(UCELLDCCC)
    op.drop_view(UCELLDISTANCEREDIRECTION)
    op.drop_view(UCELLDRD)
    op.drop_view(UCELLDYNSHUTDOWN)
    op.drop_view(UCELLFRC)
    op.drop_view(UCELLHCS)
    op.drop_view(UCELLHOCOMM)
    op.drop_view(UCELLHSDPA)
    op.drop_view(UCELLHSDPCCH)
    op.drop_view(UCELLHSUPA)
    op.drop_view(UCELLINTERFREQHOCOV)
    op.drop_view(UCELLINTERRATHOCOV)
    op.drop_view(UCELLINTERRATHONCOV)
    op.drop_view(UCELLINTRAFREQHO)
    op.drop_view(UCELLLDB)
    op.drop_view(UCELLLDM)
    op.drop_view(UCELLLDR)
    op.drop_view(UCELLLICENSE)
    op.drop_view(UCELLMEAS)
    op.drop_view(UCELLNFREQPRIOINFO)
    op.drop_view(UCELLOLC)
    op.drop_view(UCELLPUC)
    op.drop_view(UCELLREDIRECTION)
    op.drop_view(UCELLRLACTTIME)
    op.drop_view(UCELLRLPWR)
    op.drop_view(UCELLSELRESEL)
    op.drop_view(UCELLSIBSWITCH)
    op.drop_view(UCELLUPDTCTRLSWITCH)
    op.drop_view(UCELLURA)
    op.drop_view(UCHLQUALITYEVALUATE)
    op.drop_view(UCHPWROFFSET)
    op.drop_view(UCIDCHG)
    op.drop_view(UCLB)
    op.drop_view(UCMCF)
    op.drop_view(UCNDOMAIN)
    op.drop_view(UCNNODE)
    op.drop_view(UCNOPERATOR)
    op.drop_view(UCNOPERGROUP)
    op.drop_view(UCNTCHK)
    op.drop_view(UCOIFTIMER)
    op.drop_view(UCONNMODETIMER)
    op.drop_view(UCORRMALGOSWITCH)
    op.drop_view(UCORRMPARA)
    op.drop_view(UCSVOICEPPC)
    op.drop_view(UCTRLPLNSHAREPARA)
    op.drop_view(UDCCC)
    op.drop_view(UDISTANCEREDIRECTION)
    op.drop_view(UDPUCFGDATA)
    op.drop_view(UDRD)
    op.drop_view(UDRDMIMO)
    op.drop_view(UDSACAUTOALGO)
    op.drop_view(UDTXDRXPARA)
    op.drop_view(UEDCHRATEADJUSTSET)
    op.drop_view(UEDCHTTIRECFG)
    op.drop_view(UEVQIPARA)
    op.drop_view(UEXT2GCELL)
    op.drop_view(UEXT3GCELL)
    op.drop_view(UEXT3GCELLINTRAFREQHO)
    op.drop_view(UFACH)
    op.drop_view(UFACHBANDWIDTH)
    op.drop_view(UFACHDYNTFS)
    op.drop_view(UFACHLOCH)
    op.drop_view(UFDPCHPARA)
    op.drop_view(UFDPCHRLPWR)
    op.drop_view(UFRC)
    op.drop_view(UFRCCHLTYPEPARA)
    op.drop_view(UHCSHO)
    op.drop_view(UHOCOMM)
    op.drop_view(UHSSCCHLESSOPPARA)
    op.drop_view(UIDLEMODETIMER)
    op.drop_view(UINTERFREQHOCOV)
    op.drop_view(UINTERFREQHONCOV)
    op.drop_view(UINTERFREQNCELL)
    op.drop_view(UINTERRATHOCOV)
    op.drop_view(UINTERRATHONCOV)
    op.drop_view(UINTRAFREQHO)
    op.drop_view(UINTRAFREQNCELL)
    op.drop_view(UIPSERVICEQOS)
    op.drop_view(UIURGCONN)
    op.drop_view(UIUTIMERANDNUM)
    op.drop_view(UKPIALMTHD)
    op.drop_view(ULAC)
    op.drop_view(ULDCALGOPARA)
    op.drop_view(ULDCPERIOD)
    op.drop_view(ULDM)
    op.drop_view(ULOCELL)
    op.drop_view(UMBSCCRRM)
    op.drop_view(UMCDRD)
    op.drop_view(UMCLDR)
    op.drop_view(UMRSWITCH)
    op.drop_view(UMULTIRABHOCOV)
    op.drop_view(UNBSC)
    op.drop_view(UNCELLDETECTSWITCH)
    op.drop_view(UNCP)
    op.drop_view(UNODEB)
    op.drop_view(UNODEBALGOPARA)
    op.drop_view(UNODEBIP)
    op.drop_view(UNODEBLDR)
    op.drop_view(UNODEBMNTMODE)
    op.drop_view(UNODEBOLC)
    op.drop_view(UNRIGLBCNIDMAP)
    op.drop_view(UNRNC)
    op.drop_view(UOPERATORCFGPARA)
    op.drop_view(UOPERATORSHARINGMODE)
    op.drop_view(UPCCPCH)
    op.drop_view(UPCH)
    op.drop_view(UPCHDYNTFS)
    op.drop_view(UPCPICH)
    op.drop_view(UPICH)
    op.drop_view(UPOOLLOADSHAREPARA)
    op.drop_view(UPOOLREDUNDANCY)
    op.drop_view(UPRACHACTOASCMAP)
    op.drop_view(UPRACHASC)
    op.drop_view(UPRACHBASIC)
    op.drop_view(UPRACHSLOTFORMAT)
    op.drop_view(UPRACHTFC)
    op.drop_view(UPSCH)
    op.drop_view(UPSINACTTIMER)
    op.drop_view(UPTTSTATETRANS)
    op.drop_view(UQOSACT)
    op.drop_view(UQOSALGOPARA)
    op.drop_view(UQOSHO)
    op.drop_view(UQUALITYMEAS)
    op.drop_view(UQUEUEPREEMPT)
    op.drop_view(URAC)
    op.drop_view(URACH)
    op.drop_view(URACHDYNTFS)
    op.drop_view(URACHMEASUREPARA)
    op.drop_view(UREDIRECTION)
    op.drop_view(URNCBASIC)
    op.drop_view(URNCCBPARA)
    op.drop_view(URNCCELLSHUTDOWNPARA)
    op.drop_view(URNCINPOOLRRMALGO)
    op.drop_view(URRCESTCAUSE)
    op.drop_view(URRCTRLSWITCH)
    op.drop_view(USAC)
    op.drop_view(USATLDCPERIOD)
    op.drop_view(USATLDM)
    op.drop_view(USCCPCHBASIC)
    op.drop_view(USCCPCHTFC)
    op.drop_view(USCHEDULEPRIOMAP)
    op.drop_view(USERVMEAPARA)
    op.drop_view(USMLC)
    op.drop_view(USMLCCELL)
    op.drop_view(USMLCEXT3GCELL)
    op.drop_view(USPG)
    op.drop_view(USPIWEIGHT)
    op.drop_view(USRBRATECOVSEL)
    op.drop_view(USRNSR)
    op.drop_view(USSCH)
    op.drop_view(USTATETIMER)
    op.drop_view(UTHPCLASS)
    op.drop_view(UU2LTEHOCOV)
    op.drop_view(UU2LTEHONCOV)
    op.drop_view(UUEA)
    op.drop_view(UUESTATETRANS)
    op.drop_view(UUESTATETRANSTIMER)
    op.drop_view(UUIA)
    op.drop_view(UUPALGOSWITCH)
    op.drop_view(UURA)
    op.drop_view(UUSERGBR)
    op.drop_view(UUSERHAPPYBR)
    op.drop_view(UUSERMBR)
    op.drop_view(UUSERPLNSHAREPARA)
    op.drop_view(UUSERPRIORITY)
    op.drop_view(UVIPIMSI)
    op.drop_view(UWPSALGO)
    op.drop_view(VLANID)