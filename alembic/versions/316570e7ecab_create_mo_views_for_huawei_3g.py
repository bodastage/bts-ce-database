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
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AAL2PATHT",
    t1."ANI",
    t1."CARRYF",
    t1."CARRYNCOPTN",
    t1."CARRYSN",
    t1."CARRYT",
    t1."OWNERSHIP",
    t1."PATHID",
    t1."REMARK",
    t1."RXTRFX",
    t1."TIMERCU",
    t1."TRMLOADTHINDEX",
    t1."TXTRFX",
    t1."VCI",
    t1."VPI"
FROM
huawei_nbi_umts."AAL2PATH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AAL2PATHT",
    t2."ANI",
    t2."CARRYF",
    t2."CARRYNCOPTN",
    t2."CARRYSN",
    t2."CARRYT",
    t2."OWNERSHIP",
    t2."PATHID",
    t2."REMARK",
    t2."RXTRFX",
    t2."TIMERCU",
    t2."TRMLOADTHINDEX",
    t2."TXTRFX",
    t2."VCI",
    t2."VPI"
FROM
huawei_mml_umts."AAL2PATH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

AAL2TMR = ReplaceableObject(
    'huawei_cm_3g."AAL2TMR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLOREQTMR",
    t1."ESTINDTMR",
    t1."ESTREQTMR",
    t1."MODINDTMR",
    t1."MODREQTMR",
    t1."RELINDTMR",
    t1."RELREQTMR",
    t1."RESREQTMR",
    t1."UBLREQTMR"
FROM
huawei_nbi_umts."AAL2TMR" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BLOREQTMR",
    t2."ESTINDTMR",
    t2."ESTREQTMR",
    t2."MODINDTMR",
    t2."MODREQTMR",
    t2."RELINDTMR",
    t2."RELREQTMR",
    t2."RESREQTMR",
    t2."UBLREQTMR"
FROM
huawei_gexport_wcdma."AAL2TMR_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BLOREQTMR",
    t3."ESTINDTMR",
    t3."ESTREQTMR",
    t3."MODINDTMR",
    t3."MODREQTMR",
    t3."RELINDTMR",
    t3."RELREQTMR",
    t3."RESREQTMR",
    t3."UBLREQTMR"
FROM
huawei_gexport_wcdma."AAL2TMR_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BLOREQTMR",
    t4."ESTINDTMR",
    t4."ESTREQTMR",
    t4."MODINDTMR",
    t4."MODREQTMR",
    t4."RELINDTMR",
    t4."RELREQTMR",
    t4."RESREQTMR",
    t4."UBLREQTMR"
FROM
huawei_mml_umts."AAL2TMR" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ADJMAP = ReplaceableObject(
    'huawei_cm_3g."ADJMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ANI",
    t1."CNMNGMODE",
    t1."CNOPINDEX",
    t1."FTI",
    t1."ITFT",
    t1."TMIBRZ",
    t1."TMIGLD",
    t1."TMISLV",
    t1."TRANST"
FROM
huawei_nbi_umts."ADJMAP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ANI",
    t2."CNMNGMODE",
    NULL,
    t2."FTI",
    t2."ITFT",
    t2."TMIBRZ",
    t2."TMIGLD",
    t2."TMISLV",
    t2."TRANST"
FROM
huawei_gexport_wcdma."ADJMAP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ANI",
    t3."CNMNGMODE",
    NULL,
    t3."FTI",
    t3."ITFT",
    t3."TMIBRZ",
    t3."TMIGLD",
    t3."TMISLV",
    t3."TRANST"
FROM
huawei_gexport_wcdma."ADJMAP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."ANI",
    t4."CNMNGMODE",
    NULL,
    t4."FTI",
    t4."ITFT",
    t4."TMIBRZ",
    t4."TMIGLD",
    t4."TMISLV",
    t4."TRANST"
FROM
huawei_mml_umts."ADJMAP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ADJNODE = ReplaceableObject(
    'huawei_cm_3g."ADJNODE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ANI",
    t1."CHECKCOUNT",
    t1."CNMNGMODE",
    t1."DSCP",
    t1."IPPOOLINDEX",
    t1."LOGICRNCID",
    t1."NAME",
    t1."NODEBID",
    t1."NODET",
    t1."PERIOD",
    t1."PINGCHKT",
    t1."PINGPKGLEN",
    t1."PINGSWITCH",
    t1."RXBW",
    t1."TRANST",
    t1."TRMLOADTHINDEX",
    t1."TXBW",
    t1."ISROOTNODE",
    t1."QAAL2VER",
    t1."SAALLNKN"
FROM
huawei_nbi_umts."ADJNODE" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ANI",
    t2."CHECKCOUNT",
    t2."CNMNGMODE",
    t2."DSCP",
    t2."IPPOOLINDEX",
    t2."LOGICRNCID",
    t2."NAME",
    t2."NODEBID",
    t2."NODET",
    t2."PERIOD",
    t2."PINGCHKT",
    t2."PINGPKGLEN",
    t2."PINGSWITCH",
    t2."RXBW",
    t2."TRANST",
    t2."TRMLOADTHINDEX",
    t2."TXBW",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_wcdma."ADJNODE_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ANI",
    t3."CHECKCOUNT",
    t3."CNMNGMODE",
    t3."DSCP",
    t3."IPPOOLINDEX",
    t3."LOGICRNCID",
    t3."NAME",
    t3."NODEBID",
    t3."NODET",
    t3."PERIOD",
    t3."PINGCHKT",
    t3."PINGPKGLEN",
    t3."PINGSWITCH",
    t3."RXBW",
    t3."TRANST",
    t3."TRMLOADTHINDEX",
    t3."TXBW",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_wcdma."ADJNODE_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."ANI",
    t4."CHECKCOUNT",
    t4."CNMNGMODE",
    t4."DSCP",
    t4."IPPOOLINDEX",
    NULL,
    t4."NAME",
    t4."NODEBID",
    t4."NODET",
    t4."PERIOD",
    NULL,
    NULL,
    t4."PINGSWITCH",
    NULL,
    t4."TRANST",
    NULL,
    NULL,
    t4."ISROOTNODE",
    t4."QAAL2VER",
    t4."SAALLNKN"
FROM
huawei_mml_umts."ADJNODE" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ATMTRF = ReplaceableObject(
    'huawei_cm_3g."ATMTRF"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CDVT",
    t1."MCR",
    t1."PCR",
    t1."REMARK",
    t1."ST",
    t1."TRFX",
    t1."UT",
    t1."MBS",
    t1."SCR"
FROM
huawei_nbi_umts."ATMTRF" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CDVT",
    t2."MCR",
    t2."PCR",
    t2."REMARK",
    t2."ST",
    t2."TRFX",
    t2."UT",
    t2."MBS",
    t2."SCR"
FROM
huawei_mml_umts."ATMTRF" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

CELLCBS = ReplaceableObject(
    'huawei_cm_3g."CELLCBS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."CELLCBS" t1

"""
)

CELLERACH = ReplaceableObject(
    'huawei_cm_3g."CELLERACH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."CELLERACH" t1

"""
)

CELLMIMO = ReplaceableObject(
    'huawei_cm_3g."CELLMIMO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."CELLMIMO" t1

"""
)

CELLTEMPLATERSC = ReplaceableObject(
    'huawei_cm_3g."CELLTEMPLATERSC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."NAME"
FROM
huawei_nbi_umts."CELLTEMPLATERSC" t1

"""
)

DEVIP = ReplaceableObject(
    'huawei_cm_3g."DEVIP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DEVTYPE",
    t1."IPADDR",
    t1."MASK",
    t1."MTU",
    t1."REMARK",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_umts."DEVIP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."DEVTYPE",
    t2."IPADDR",
    NULL,
    NULL,
    t2."REMARK",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_wcdma."DEVIP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."DEVTYPE",
    t3."IPADDR",
    NULL,
    NULL,
    t3."REMARK",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_wcdma."DEVIP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."DEVTYPE",
    t4."IPADDR",
    t4."MASK",
    t4."MTU",
    t4."REMARK",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_umts."DEVIP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

EMSIP = ReplaceableObject(
    'huawei_cm_3g."EMSIP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."EMSIP",
    t1."MASK",
    t1."OMUIP",
    t1."OMUMASK"
FROM
huawei_nbi_umts."EMSIP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."EMSIP",
    t2."MASK",
    t2."OMUIP",
    t2."OMUMASK"
FROM
huawei_gexport_wcdma."EMSIP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."EMSIP",
    t3."MASK",
    t3."OMUIP",
    t3."OMUMASK"
FROM
huawei_gexport_wcdma."EMSIP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."EMSIP",
    t4."MASK",
    t4."OMUIP",
    t4."OMUMASK"
FROM
huawei_mml_umts."EMSIP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ETHIP = ReplaceableObject(
    'huawei_cm_3g."ETHIP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IPADDR",
    t1."IPINDEX",
    t1."MASK",
    t1."PN",
    t1."REMARK",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_umts."ETHIP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."IPADDR",
    t2."IPINDEX",
    t2."MASK",
    t2."PN",
    t2."REMARK",
    t2."SN",
    t2."SRN"
FROM
huawei_mml_umts."ETHIP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

ETHPORT = ReplaceableObject(
    'huawei_cm_3g."ETHPORT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BCPKTALARMCLRTHD",
    t1."BCPKTALARMTHD",
    t1."BRDTYPE",
    t1."CFMVER",
    t1."ERRALARMTHD",
    t1."ERRDETECTSW",
    t1."FC",
    t1."FCINDEX",
    t1."FLOWCTRLSWITCH",
    t1."MTU",
    t1."OAMFLOWBW",
    t1."PN",
    t1."REMARK",
    t1."SN",
    t1."SRN",
    t1."AUTO"
FROM
huawei_nbi_umts."ETHPORT" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BCPKTALARMCLRTHD",
    t2."BCPKTALARMTHD",
    t2."BRDTYPE",
    t2."CFMVER",
    t2."ERRALARMTHD",
    t2."ERRDETECTSW",
    NULL,
    t2."FCINDEX",
    t2."FLOWCTRLSWITCH",
    t2."MTU",
    t2."OAMFLOWBW",
    t2."PN",
    t2."REMARK",
    t2."SN",
    t2."SRN",
    t2."AUTO"
FROM
huawei_gexport_wcdma."ETHPORT_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BCPKTALARMCLRTHD",
    t3."BCPKTALARMTHD",
    t3."BRDTYPE",
    t3."CFMVER",
    t3."ERRALARMTHD",
    t3."ERRDETECTSW",
    NULL,
    t3."FCINDEX",
    t3."FLOWCTRLSWITCH",
    t3."MTU",
    t3."OAMFLOWBW",
    t3."PN",
    t3."REMARK",
    t3."SN",
    t3."SRN",
    t3."AUTO"
FROM
huawei_gexport_wcdma."ETHPORT_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BCPKTALARMCLRTHD",
    t4."BCPKTALARMTHD",
    t4."BRDTYPE",
    t4."CFMVER",
    t4."ERRALARMTHD",
    t4."ERRDETECTSW",
    t4."FC",
    t4."FCINDEX",
    t4."FLOWCTRLSWITCH",
    t4."MTU",
    t4."OAMFLOWBW",
    t4."PN",
    t4."REMARK",
    t4."SN",
    t4."SRN",
    t4."AUTO"
FROM
huawei_mml_umts."ETHPORT" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t5."PN",
    NULL,
    t5."SN",
    t5."SRN",
    NULL
FROM
huawei_mml_umts."ETHPORT_ACT" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

UNION
SELECT
    t6."FileName",
    t6."varDateTime",
    NULL,
    NULL,
    t6."BAM_VERSION" AS neversion,
    t61."SYSOBJECTID" AS neid,
    NULL,
    t6."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t6."PN",
    NULL,
    t6."SN",
    t6."SRN",
    NULL
FROM
huawei_mml_umts."ETHPORT_DEA" t6
INNER JOIN huawei_mml_umts."SYS" t61 ON t61."FileName" = t6."FileName"

"""
)

ETHTRK = ReplaceableObject(
    'huawei_cm_3g."ETHTRK"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CFMVER",
    t1."FCINDEX",
    t1."FLOWCTRLSWITCH",
    t1."LACPMODE",
    t1."MTU",
    t1."OAMFLOWBW",
    t1."RT",
    t1."SN",
    t1."SRN",
    t1."SYSPRI",
    t1."TRKN",
    t1."WORKMODE"
FROM
huawei_nbi_umts."ETHTRK" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CFMVER",
    t2."FCINDEX",
    t2."FLOWCTRLSWITCH",
    t2."LACPMODE",
    t2."MTU",
    t2."OAMFLOWBW",
    t2."RT",
    t2."SN",
    t2."SRN",
    t2."SYSPRI",
    t2."TRKN",
    t2."WORKMODE"
FROM
huawei_gexport_wcdma."ETHTRK_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CFMVER",
    t3."FCINDEX",
    t3."FLOWCTRLSWITCH",
    t3."LACPMODE",
    t3."MTU",
    t3."OAMFLOWBW",
    t3."RT",
    t3."SN",
    t3."SRN",
    t3."SYSPRI",
    t3."TRKN",
    t3."WORKMODE"
FROM
huawei_gexport_wcdma."ETHTRK_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CFMVER",
    t4."FCINDEX",
    t4."FLOWCTRLSWITCH",
    t4."LACPMODE",
    t4."MTU",
    t4."OAMFLOWBW",
    t4."RT",
    t4."SN",
    t4."SRN",
    t4."SYSPRI",
    t4."TRKN",
    t4."WORKMODE"
FROM
huawei_mml_umts."ETHTRK" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ETHTRKIP = ReplaceableObject(
    'huawei_cm_3g."ETHTRKIP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IPADDR",
    t1."IPINDEX",
    t1."MASK",
    t1."SN",
    t1."SRN",
    t1."TRKN"
FROM
huawei_nbi_umts."ETHTRKIP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."IPADDR",
    t2."IPINDEX",
    t2."MASK",
    t2."SN",
    t2."SRN",
    t2."TRKN"
FROM
huawei_gexport_wcdma."ETHTRKIP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."IPADDR",
    t3."IPINDEX",
    t3."MASK",
    t3."SN",
    t3."SRN",
    t3."TRKN"
FROM
huawei_gexport_wcdma."ETHTRKIP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."IPADDR",
    t4."IPINDEX",
    t4."MASK",
    t4."SN",
    t4."SRN",
    t4."TRKN"
FROM
huawei_mml_umts."ETHTRKIP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ETHTRKLNK = ReplaceableObject(
    'huawei_cm_3g."ETHTRKLNK"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."PORTPRI",
    t1."SN",
    t1."SRN",
    t1."TRKLNKPN",
    t1."TRKLNKSN",
    t1."TRKN",
    t1."WORKMODE"
FROM
huawei_nbi_umts."ETHTRKLNK" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."PORTPRI",
    t2."SN",
    t2."SRN",
    t2."TRKLNKPN",
    t2."TRKLNKSN",
    t2."TRKN",
    t2."WORKMODE"
FROM
huawei_gexport_wcdma."ETHTRKLNK_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."PORTPRI",
    t3."SN",
    t3."SRN",
    t3."TRKLNKPN",
    t3."TRKLNKSN",
    t3."TRKN",
    t3."WORKMODE"
FROM
huawei_gexport_wcdma."ETHTRKLNK_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."SN",
    t4."SRN",
    t4."TRKLNKPN",
    t4."TRKLNKSN",
    t4."TRKN",
    t4."WORKMODE"
FROM
huawei_mml_umts."ETHTRKLNK" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)


IPOAPVC = ReplaceableObject(
    'huawei_cm_3g."IPOAPVC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CARRYNCOPTN",
    t1."CARRYT",
    t1."CARRYVCI",
    t1."CARRYVPI",
    t1."IPADDR",
    t1."PEERIPADDR",
    t1."PEERT",
    t1."REMARK",
    t1."RXTRFX",
    t1."TXTRFX"
FROM
huawei_nbi_umts."IPOAPVC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."CARRYT",
    t2."CARRYVCI",
    t2."CARRYVPI",
    t2."IPADDR",
    t2."PEERIPADDR",
    t2."PEERT",
    t2."REMARK",
    t2."RXTRFX",
    t2."TXTRFX"
FROM
huawei_mml_umts."IPOAPVC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

IPPOOL = ReplaceableObject(
    'huawei_cm_3g."IPPOOL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CMEMODE",
    t1."IPPOOLINDEX",
    t1."IPPOOLNAME"
FROM
huawei_nbi_umts."IPPOOL" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."IPPOOLINDEX",
    t2."IPPOOLNAME"
FROM
huawei_gexport_wcdma."IPPOOL_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."IPPOOLINDEX",
    t3."IPPOOLNAME"
FROM
huawei_gexport_wcdma."IPPOOL_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."IPPOOLINDEX",
    t4."IPPOOLNAME"
FROM
huawei_mml_umts."IPPOOL" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

IPPOOLIP = ReplaceableObject(
    'huawei_cm_3g."IPPOOLIP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IPADDR",
    t1."IPPOOLINDEX",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_umts."IPPOOLIP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."IPADDR",
    t2."IPPOOLINDEX",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_wcdma."IPPOOLIP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."IPADDR",
    t3."IPPOOLINDEX",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_wcdma."IPPOOLIP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."IPADDR",
    t4."IPPOOLINDEX",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_umts."IPPOOLIP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    t5."IPADDR",
    t5."IPPOOLINDEX",
    NULL,
    NULL
FROM
huawei_mml_umts."IPPOOLIP_UBL" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

IPPOOLPM = ReplaceableObject(
    'huawei_cm_3g."IPPOOLPM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ANI",
    t1."DR",
    t1."ITFT",
    t1."PHB",
    t1."SIPTYPE"
FROM
huawei_nbi_umts."IPPOOLPM" t1

"""
)

IPRT = ReplaceableObject(
    'huawei_cm_3g."IPRT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DSTIP",
    t1."DSTMASK",
    t1."NEXTHOP",
    t1."NEXTHOPTYPE",
    t1."PRIORITY",
    t1."REMARK",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_umts."IPRT" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."DSTIP",
    t2."DSTMASK",
    t2."NEXTHOP",
    t2."NEXTHOPTYPE",
    NULL,
    t2."REMARK",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_wcdma."IPRT_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."DSTIP",
    t3."DSTMASK",
    t3."NEXTHOP",
    t3."NEXTHOPTYPE",
    NULL,
    t3."REMARK",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_wcdma."IPRT_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."DSTIP",
    t4."DSTMASK",
    t4."NEXTHOP",
    t4."NEXTHOPTYPE",
    t4."PRIORITY",
    t4."REMARK",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_umts."IPRT" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

IU_ADJMAP = ReplaceableObject(
    'huawei_cm_3g."IU_ADJMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ANI",
    t1."CNMNGMODE",
    t1."CNOPINDEX",
    t1."FTI",
    t1."ITFT",
    t1."TMIBRZ",
    t1."TMIGLD",
    t1."TMISLV"
FROM
huawei_nbi_umts."IU_ADJMAP" t1

"""
)

IU_ADJNODE = ReplaceableObject(
    'huawei_cm_3g."IU_ADJNODE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ANI",
    t1."CHECKCOUNT",
    t1."CNMNGMODE",
    t1."DSCP",
    t1."IPPOOLINDEX",
    t1."LOGICRNCSHAREMODE",
    t1."NAME",
    t1."NODET",
    t1."PERIOD",
    t1."PINGPKGLEN",
    t1."PINGSWITCH",
    t1."TRANST",
    t1."DPX"
FROM
huawei_nbi_umts."IU_ADJNODE" t1

"""
)

M3DE = ReplaceableObject(
    'huawei_cm_3g."M3DE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DENO",
    t1."DPX",
    t1."ENTITYT",
    t1."LENO",
    t1."NAME",
    t1."RTCONTEXT"
FROM
huawei_nbi_umts."M3DE" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."DENO",
    t2."DPX",
    t2."ENTITYT",
    t2."LENO",
    t2."NAME",
    t2."RTCONTEXT"
FROM
huawei_gexport_wcdma."M3DE_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."DENO",
    t3."DPX",
    t3."ENTITYT",
    t3."LENO",
    t3."NAME",
    t3."RTCONTEXT"
FROM
huawei_gexport_wcdma."M3DE_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."DENO",
    t4."DPX",
    t4."ENTITYT",
    t4."LENO",
    t4."NAME",
    t4."RTCONTEXT"
FROM
huawei_mml_umts."M3DE" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

M3LE = ReplaceableObject(
    'huawei_cm_3g."M3LE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ENTITYT",
    t1."LENO",
    t1."NAME",
    t1."RTCONTEXT",
    t1."SPX"
FROM
huawei_nbi_umts."M3LE" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ENTITYT",
    t2."LENO",
    t2."NAME",
    t2."RTCONTEXT",
    t2."SPX"
FROM
huawei_gexport_wcdma."M3LE_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ENTITYT",
    t3."LENO",
    t3."NAME",
    t3."RTCONTEXT",
    t3."SPX"
FROM
huawei_gexport_wcdma."M3LE_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."ENTITYT",
    t4."LENO",
    t4."NAME",
    t4."RTCONTEXT",
    t4."SPX"
FROM
huawei_mml_umts."M3LE" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

M3LKS = ReplaceableObject(
    'huawei_cm_3g."M3LKS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DENO",
    t1."LNKSLSMASK",
    t1."MULTIRCSW",
    t1."NAME",
    t1."PDTMRVALUE",
    t1."SIGLKSX",
    t1."TRAMODE",
    t1."WKMODE"
FROM
huawei_nbi_umts."M3LKS" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."DENO",
    t2."LNKSLSMASK",
    t2."MULTIRCSW",
    t2."NAME",
    t2."PDTMRVALUE",
    t2."SIGLKSX",
    t2."TRAMODE",
    t2."WKMODE"
FROM
huawei_gexport_wcdma."M3LKS_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."DENO",
    t3."LNKSLSMASK",
    t3."MULTIRCSW",
    t3."NAME",
    t3."PDTMRVALUE",
    t3."SIGLKSX",
    t3."TRAMODE",
    t3."WKMODE"
FROM
huawei_gexport_wcdma."M3LKS_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."DENO",
    t4."LNKSLSMASK",
    NULL,
    t4."NAME",
    t4."PDTMRVALUE",
    t4."SIGLKSX",
    t4."TRAMODE",
    t4."WKMODE"
FROM
huawei_mml_umts."M3LKS" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

M3LNK = ReplaceableObject(
    'huawei_cm_3g."M3LNK"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LNKREDFLAG",
    t1."NAME",
    t1."PRIORITY",
    t1."SCTPLNKID",
    t1."SIGLKSX",
    t1."SIGLNKID"
FROM
huawei_nbi_umts."M3LNK" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LNKREDFLAG",
    t2."NAME",
    t2."PRIORITY",
    t2."SCTPLNKID",
    t2."SIGLKSX",
    t2."SIGLNKID"
FROM
huawei_gexport_wcdma."M3LNK_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LNKREDFLAG",
    t3."NAME",
    t3."PRIORITY",
    t3."SCTPLNKID",
    t3."SIGLKSX",
    t3."SIGLNKID"
FROM
huawei_gexport_wcdma."M3LNK_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."LNKREDFLAG",
    t4."NAME",
    t4."PRIORITY",
    t4."SCTPLNKID",
    t4."SIGLKSX",
    t4."SIGLNKID"
FROM
huawei_mml_umts."M3LNK" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t5."SIGLKSX",
    t5."SIGLNKID"
FROM
huawei_mml_umts."M3LNK_ACT" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

UNION
SELECT
    t6."FileName",
    t6."varDateTime",
    NULL,
    NULL,
    t6."BAM_VERSION" AS neversion,
    t61."SYSOBJECTID" AS neid,
    NULL,
    t6."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t6."SIGLKSX",
    t6."SIGLNKID"
FROM
huawei_mml_umts."M3LNK_UIN" t6
INNER JOIN huawei_mml_umts."SYS" t61 ON t61."FileName" = t6."FileName"

"""
)

M3RT = ReplaceableObject(
    'huawei_cm_3g."M3RT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DENO",
    t1."NAME",
    t1."PRIORITY",
    t1."SIGLKSX"
FROM
huawei_nbi_umts."M3RT" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."DENO",
    t2."NAME",
    t2."PRIORITY",
    t2."SIGLKSX"
FROM
huawei_gexport_wcdma."M3RT_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."DENO",
    t3."NAME",
    t3."PRIORITY",
    t3."SIGLKSX"
FROM
huawei_gexport_wcdma."M3RT_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."DENO",
    t4."NAME",
    t4."PRIORITY",
    t4."SIGLKSX"
FROM
huawei_mml_umts."M3RT" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

MSP = ReplaceableObject(
    'huawei_cm_3g."MSP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CMEMODE",
    t1."K2MODE",
    t1."PN",
    t1."RT",
    t1."SDENABLE",
    t1."SDSFPRI",
    t1."SN",
    t1."SRN",
    t1."WTRT"
FROM
huawei_nbi_umts."MSP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."K2MODE",
    t2."PN",
    t2."RT",
    t2."SDENABLE",
    t2."SDSFPRI",
    t2."SN",
    t2."SRN",
    t2."WTRT"
FROM
huawei_gexport_wcdma."MSP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."K2MODE",
    t3."PN",
    t3."RT",
    t3."SDENABLE",
    t3."SDSFPRI",
    t3."SN",
    t3."SRN",
    t3."WTRT"
FROM
huawei_gexport_wcdma."MSP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."K2MODE",
    t4."PN",
    t4."RT",
    t4."SDENABLE",
    t4."SDSFPRI",
    t4."SN",
    t4."SRN",
    t4."WTRT"
FROM
huawei_mml_umts."MSP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    t5."PN",
    NULL,
    NULL,
    NULL,
    t5."SN",
    t5."SRN",
    NULL
FROM
huawei_mml_umts."MSP_ACT" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

MTP3TMR = ReplaceableObject(
    'huawei_cm_3g."MTP3TMR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."SAALTMR",
    t1."T10TMR",
    t1."T12TMR",
    t1."T13TMR",
    t1."T14TMR",
    t1."T17TMR",
    t1."T1TMR",
    t1."T22TMR",
    t1."T23TMR",
    t1."T2TMR",
    t1."T3TMR",
    t1."T4TMR",
    t1."T5TMR",
    t1."T8TMR",
    t1."TMT1TMR",
    t1."TMT2TMR"
FROM
huawei_nbi_umts."MTP3TMR" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."SAALTMR",
    t2."T10TMR",
    t2."T12TMR",
    t2."T13TMR",
    t2."T14TMR",
    t2."T17TMR",
    t2."T1TMR",
    t2."T22TMR",
    t2."T23TMR",
    t2."T2TMR",
    t2."T3TMR",
    t2."T4TMR",
    t2."T5TMR",
    t2."T8TMR",
    t2."TMT1TMR",
    t2."TMT2TMR"
FROM
huawei_gexport_wcdma."MTP3TMR_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."SAALTMR",
    t3."T10TMR",
    t3."T12TMR",
    t3."T13TMR",
    t3."T14TMR",
    t3."T17TMR",
    t3."T1TMR",
    t3."T22TMR",
    t3."T23TMR",
    t3."T2TMR",
    t3."T3TMR",
    t3."T4TMR",
    t3."T5TMR",
    t3."T8TMR",
    t3."TMT1TMR",
    t3."TMT2TMR"
FROM
huawei_gexport_wcdma."MTP3TMR_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."SAALTMR",
    t4."T10TMR",
    t4."T12TMR",
    t4."T13TMR",
    t4."T14TMR",
    t4."T17TMR",
    t4."T1TMR",
    t4."T22TMR",
    t4."T23TMR",
    t4."T2TMR",
    t4."T3TMR",
    t4."T4TMR",
    t4."T5TMR",
    t4."T8TMR",
    t4."TMT1TMR",
    t4."TMT2TMR"
FROM
huawei_mml_umts."MTP3TMR" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

N7DPC = ReplaceableObject(
    'huawei_cm_3g."N7DPC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BEARTYPE",
    t1."DPC",
    t1."DPCT",
    t1."DPX",
    t1."NAME",
    t1."NEIGHBOR",
    t1."PROT",
    t1."SLSMASK",
    t1."SPDF",
    t1."SPX",
    t1."STP"
FROM
huawei_nbi_umts."N7DPC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BEARTYPE",
    t2."DPC",
    t2."DPCT",
    t2."DPX",
    t2."NAME",
    t2."NEIGHBOR",
    t2."PROT",
    t2."SLSMASK",
    t2."SPDF",
    t2."SPX",
    t2."STP"
FROM
huawei_gexport_wcdma."N7DPC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BEARTYPE",
    t3."DPC",
    t3."DPCT",
    t3."DPX",
    t3."NAME",
    t3."NEIGHBOR",
    t3."PROT",
    t3."SLSMASK",
    t3."SPDF",
    t3."SPX",
    t3."STP"
FROM
huawei_gexport_wcdma."N7DPC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BEARTYPE",
    t4."DPC",
    t4."DPCT",
    t4."DPX",
    t4."NAME",
    t4."NEIGHBOR",
    t4."PROT",
    t4."SLSMASK",
    t4."SPDF",
    t4."SPX",
    t4."STP"
FROM
huawei_mml_umts."N7DPC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    t5."DPX",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."N7DPC_UIN" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

NODEBEQUIPMENT = ReplaceableObject(
    'huawei_cm_3g."NODEBEQUIPMENT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."NODEBID",
    t1."NODEBNAME",
    t1."SERIES",
    t1."TEMPLATENAME",
    t1."VERSION"
FROM
huawei_nbi_umts."NODEBEQUIPMENT" t1

"""
)

NODEBTEMPLATERSC = ReplaceableObject(
    'huawei_cm_3g."NODEBTEMPLATERSC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."SERIES",
    t1."TEMPLATENAME",
    t1."VERSION"
FROM
huawei_nbi_umts."NODEBTEMPLATERSC" t1

"""
)

OPC = ReplaceableObject(
    'huawei_cm_3g."OPC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."HOSTTYPE",
    t1."NAME",
    t1."NI",
    t1."RSTFUN",
    t1."SPC",
    t1."SPCBITS",
    t1."SPDF",
    t1."SPX"
FROM
huawei_nbi_umts."OPC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."HOSTTYPE",
    t2."NAME",
    t2."NI",
    t2."RSTFUN",
    t2."SPC",
    t2."SPCBITS",
    t2."SPDF",
    t2."SPX"
FROM
huawei_gexport_wcdma."OPC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."HOSTTYPE",
    t3."NAME",
    t3."NI",
    t3."RSTFUN",
    t3."SPC",
    t3."SPCBITS",
    t3."SPDF",
    t3."SPX"
FROM
huawei_gexport_wcdma."OPC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."HOSTTYPE",
    t4."NAME",
    t4."NI",
    t4."RSTFUN",
    t4."SPC",
    t4."SPCBITS",
    t4."SPDF",
    t4."SPX"
FROM
huawei_mml_umts."OPC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OPT = ReplaceableObject(
    'huawei_cm_3g."OPT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BT",
    t1."FCINDEX",
    t1."FLOWCTRLSWITCH",
    t1."J0TYPE",
    t1."J1TYPE",
    t1."JAUTOADD",
    t1."OPTM",
    t1."PN",
    t1."PS",
    t1."S1VALUE",
    t1."SCRAMBLESW",
    t1."SN",
    t1."SRN",
    t1."WORKTYPE",
    t1."J0BYTE_FORMAT",
    t1."J0RXVALUE",
    t1."J0TXVALUE",
    t1."J1BYTE_FORMAT",
    t1."J1RXVALUE",
    t1."J1TXVALUE"
FROM
huawei_nbi_umts."OPT" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BT",
    NULL,
    NULL,
    t2."J0TYPE",
    t2."J1TYPE",
    t2."JAUTOADD",
    t2."OPTM",
    t2."PN",
    t2."PS",
    t2."S1VALUE",
    NULL,
    t2."SN",
    t2."SRN",
    NULL,
    t2."J0BYTE_FORMAT",
    t2."J0RXVALUE",
    t2."J0TXVALUE",
    t2."J1BYTE_FORMAT",
    t2."J1RXVALUE",
    t2."J1TXVALUE"
FROM
huawei_gexport_wcdma."OPT_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BT",
    NULL,
    NULL,
    t3."J0TYPE",
    t3."J1TYPE",
    t3."JAUTOADD",
    t3."OPTM",
    t3."PN",
    t3."PS",
    t3."S1VALUE",
    NULL,
    t3."SN",
    t3."SRN",
    NULL,
    t3."J0BYTE_FORMAT",
    t3."J0RXVALUE",
    t3."J0TXVALUE",
    t3."J1BYTE_FORMAT",
    t3."J1RXVALUE",
    t3."J1TXVALUE"
FROM
huawei_gexport_wcdma."OPT_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BT",
    t4."FCINDEX",
    t4."FLOWCTRLSWITCH",
    t4."J0TYPE",
    t4."J1TYPE",
    t4."JAUTOADD",
    NULL,
    t4."PN",
    t4."PS",
    t4."S1VALUE",
    t4."SCRAMBLESW",
    t4."SN",
    t4."SRN",
    t4."WORKTYPE",
    t4."J0BYTE_FORMAT",
    t4."J0RXVALUE",
    t4."J0TXVALUE",
    t4."J1BYTE_FORMAT",
    t4."J1RXVALUE",
    t4."J1TXVALUE"
FROM
huawei_mml_umts."OPT" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PHBMAP = ReplaceableObject(
    'huawei_cm_3g."PHBMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DSCP",
    t1."PHB",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_umts."PHBMAP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."DSCP",
    t2."PHB",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_wcdma."PHBMAP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."DSCP",
    t3."PHB",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_wcdma."PHBMAP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."DSCP",
    t4."PHB",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_umts."PHBMAP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PORTFLOWCTRLPARA = ReplaceableObject(
    'huawei_cm_3g."PORTFLOWCTRLPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CONGCLRTHD0",
    t1."CONGCLRTHD1",
    t1."CONGCLRTHD2",
    t1."CONGCLRTHD3",
    t1."CONGCLRTHD4",
    t1."CONGCLRTHD5",
    t1."CONGTHD0",
    t1."CONGTHD1",
    t1."CONGTHD2",
    t1."CONGTHD3",
    t1."CONGTHD4",
    t1."CONGTHD5",
    t1."DROPPKTTHD0",
    t1."DROPPKTTHD1",
    t1."DROPPKTTHD2",
    t1."DROPPKTTHD3",
    t1."DROPPKTTHD4",
    t1."DROPPKTTHD5",
    t1."FCINDEX",
    t1."PORTPROTYPE",
    t1."PQNUM"
FROM
huawei_nbi_umts."PORTFLOWCTRLPARA" t1

"""
)

QUEUEMAP = ReplaceableObject(
    'huawei_cm_3g."QUEUEMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."OAMMINBWKEY",
    t1."Q0MINDSCP",
    t1."Q1MINDSCP",
    t1."Q2MINDSCP",
    t1."Q3MINDSCP",
    t1."Q4MINDSCP",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_umts."QUEUEMAP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."OAMMINBWKEY",
    t2."Q0MINDSCP",
    t2."Q1MINDSCP",
    t2."Q2MINDSCP",
    t2."Q3MINDSCP",
    t2."Q4MINDSCP",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_wcdma."QUEUEMAP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."OAMMINBWKEY",
    t3."Q0MINDSCP",
    t3."Q1MINDSCP",
    t3."Q2MINDSCP",
    t3."Q3MINDSCP",
    t3."Q4MINDSCP",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_wcdma."QUEUEMAP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."OAMMINBWKEY",
    t4."Q0MINDSCP",
    t4."Q1MINDSCP",
    t4."Q2MINDSCP",
    t4."Q3MINDSCP",
    t4."Q4MINDSCP",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_umts."QUEUEMAP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SAALLNK = ReplaceableObject(
    'huawei_cm_3g."SAALLNK"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CARRYNCOPTN",
    t1."CARRYSN",
    t1."CARRYSRN",
    t1."CARRYT",
    t1."CARRYVCI",
    t1."CARRYVPI",
    t1."CCTMR",
    t1."IDLETMR",
    t1."KEEPTMR",
    t1."MAXCC",
    t1."MAXPD",
    t1."POLLTMR",
    t1."RSPTMR",
    t1."RXTRFX",
    t1."SAALLNKN",
    t1."SAALLNKT",
    t1."STATLEN",
    t1."TXTRFX",
    t1."WINDOWSIZE"
FROM
huawei_nbi_umts."SAALLNK" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CARRYNCOPTN",
    t2."CARRYSN",
    t2."CARRYSRN",
    t2."CARRYT",
    t2."CARRYVCI",
    t2."CARRYVPI",
    t2."CCTMR",
    t2."IDLETMR",
    t2."KEEPTMR",
    t2."MAXCC",
    t2."MAXPD",
    t2."POLLTMR",
    t2."RSPTMR",
    t2."RXTRFX",
    t2."SAALLNKN",
    t2."SAALLNKT",
    t2."STATLEN",
    t2."TXTRFX",
    t2."WINDOWSIZE"
FROM
huawei_mml_umts."SAALLNK" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

SCCPTMR = ReplaceableObject(
    'huawei_cm_3g."SCCPTMR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CONNECTTMR",
    t1."COTMR",
    t1."EATMR",
    t1."FREEZENTMR",
    t1."GUARDTMR",
    t1."IARXTMR",
    t1."IATXTMR",
    t1."IGNORTMR",
    t1."INTTMR",
    t1."LRNTMR",
    t1."REASTMR",
    t1."RELEASETMR",
    t1."REPRELEASETMR",
    t1."RESETTMR",
    t1."STATTMR"
FROM
huawei_nbi_umts."SCCPTMR" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CONNECTTMR",
    t2."COTMR",
    t2."EATMR",
    t2."FREEZENTMR",
    t2."GUARDTMR",
    t2."IARXTMR",
    t2."IATXTMR",
    t2."IGNORTMR",
    t2."INTTMR",
    t2."LRNTMR",
    t2."REASTMR",
    t2."RELEASETMR",
    t2."REPRELEASETMR",
    t2."RESETTMR",
    t2."STATTMR"
FROM
huawei_gexport_wcdma."SCCPTMR_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CONNECTTMR",
    t3."COTMR",
    t3."EATMR",
    t3."FREEZENTMR",
    t3."GUARDTMR",
    t3."IARXTMR",
    t3."IATXTMR",
    t3."IGNORTMR",
    t3."INTTMR",
    t3."LRNTMR",
    t3."REASTMR",
    t3."RELEASETMR",
    t3."REPRELEASETMR",
    t3."RESETTMR",
    t3."STATTMR"
FROM
huawei_gexport_wcdma."SCCPTMR_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CONNECTTMR",
    t4."COTMR",
    t4."EATMR",
    t4."FREEZENTMR",
    t4."GUARDTMR",
    t4."IARXTMR",
    t4."IATXTMR",
    t4."IGNORTMR",
    t4."INTTMR",
    t4."LRNTMR",
    t4."REASTMR",
    t4."RELEASETMR",
    t4."REPRELEASETMR",
    t4."RESETTMR",
    t4."STATTMR"
FROM
huawei_mml_umts."SCCPTMR" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SCTPLNK = ReplaceableObject(
    'huawei_cm_3g."SCTPLNK"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."APP",
    t1."BUNDLINGFLAG",
    t1."CHKSUMTYPE",
    t1."CMEMODE",
    t1."CROSSIPFLAG",
    t1."DSCP",
    t1."HBINTER",
    t1."LOCIP1",
    t1."LOCIP2",
    t1."LOGPORTFLAG",
    t1."MAXASSOCRETR",
    t1."MAXPATHRETR",
    t1."MTU",
    t1."PEERIP1",
    t1."PEERIP2",
    t1."PEERPN",
    t1."REMARK",
    t1."RTOALPHA",
    t1."RTOBETA",
    t1."RTOINIT",
    t1."RTOMAX",
    t1."RTOMIN",
    t1."SCTPLNKID",
    t1."SWITCHBACKFLAG",
    t1."SWITCHBACKHBNUM",
    t1."TSACK",
    t1."LOCIPDISTTYPE",
    t1."LOCPN"
FROM
huawei_nbi_umts."SCTPLNK" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."APP",
    t2."BUNDLINGFLAG",
    t2."CHKSUMTYPE",
    NULL,
    t2."CROSSIPFLAG",
    t2."DSCP",
    t2."HBINTER",
    t2."LOCIP1",
    t2."LOCIP2",
    t2."LOGPORTFLAG",
    t2."MAXASSOCRETR",
    t2."MAXPATHRETR",
    t2."MTU",
    t2."PEERIP1",
    t2."PEERIP2",
    t2."PEERPN",
    t2."REMARK",
    t2."RTOALPHA",
    t2."RTOBETA",
    t2."RTOINIT",
    t2."RTOMAX",
    t2."RTOMIN",
    t2."SCTPLNKID",
    t2."SWITCHBACKFLAG",
    t2."SWITCHBACKHBNUM",
    t2."TSACK",
    NULL,
    NULL
FROM
huawei_gexport_wcdma."SCTPLNK_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."APP",
    t3."BUNDLINGFLAG",
    t3."CHKSUMTYPE",
    NULL,
    t3."CROSSIPFLAG",
    t3."DSCP",
    t3."HBINTER",
    t3."LOCIP1",
    t3."LOCIP2",
    t3."LOGPORTFLAG",
    t3."MAXASSOCRETR",
    t3."MAXPATHRETR",
    t3."MTU",
    t3."PEERIP1",
    t3."PEERIP2",
    t3."PEERPN",
    t3."REMARK",
    t3."RTOALPHA",
    t3."RTOBETA",
    t3."RTOINIT",
    t3."RTOMAX",
    t3."RTOMIN",
    t3."SCTPLNKID",
    t3."SWITCHBACKFLAG",
    t3."SWITCHBACKHBNUM",
    t3."TSACK",
    NULL,
    NULL
FROM
huawei_gexport_wcdma."SCTPLNK_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."APP",
    t4."BUNDLINGFLAG",
    t4."CHKSUMTYPE",
    NULL,
    t4."CROSSIPFLAG",
    t4."DSCP",
    t4."HBINTER",
    t4."LOCIP1",
    t4."LOCIP2",
    t4."LOGPORTFLAG",
    t4."MAXASSOCRETR",
    t4."MAXPATHRETR",
    t4."MTU",
    t4."PEERIP1",
    t4."PEERIP2",
    t4."PEERPN",
    t4."REMARK",
    t4."RTOALPHA",
    t4."RTOBETA",
    t4."RTOINIT",
    t4."RTOMAX",
    t4."RTOMIN",
    t4."SCTPLNKID",
    t4."SWITCHBACKFLAG",
    t4."SWITCHBACKHBNUM",
    t4."TSACK",
    t4."LOCIPDISTTYPE",
    t4."LOCPN"
FROM
huawei_mml_umts."SCTPLNK" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SCTPSRVPORT = ReplaceableObject(
    'huawei_cm_3g."SCTPSRVPORT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BBAPSRVPN",
    t1."M3UASRVPN",
    t1."NBAPSRVPN"
FROM
huawei_nbi_umts."SCTPSRVPORT" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."M3UASRVPN",
    t2."NBAPSRVPN"
FROM
huawei_gexport_wcdma."SCTPSRVPORT_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."M3UASRVPN",
    t3."NBAPSRVPN"
FROM
huawei_gexport_wcdma."SCTPSRVPORT_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BBAPSRVPN",
    t4."M3UASRVPN",
    t4."NBAPSRVPN"
FROM
huawei_mml_umts."SCTPSRVPORT" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SRCIPRT = ReplaceableObject(
    'huawei_cm_3g."SRCIPRT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IPTYPE",
    t1."NEXTHOP",
    t1."REMARK",
    t1."SN",
    t1."SRCIPADDR",
    t1."SRN",
    t1."STANDBYNEXTHOPSWITCH"
FROM
huawei_nbi_umts."SRCIPRT" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."IPTYPE",
    t2."NEXTHOP",
    t2."REMARK",
    t2."SN",
    t2."SRCIPADDR",
    t2."SRN",
    NULL
FROM
huawei_gexport_wcdma."SRCIPRT_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."IPTYPE",
    t3."NEXTHOP",
    t3."REMARK",
    t3."SN",
    t3."SRCIPADDR",
    t3."SRN",
    NULL
FROM
huawei_gexport_wcdma."SRCIPRT_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."IPTYPE",
    t4."NEXTHOP",
    t4."REMARK",
    t4."SN",
    t4."SRCIPADDR",
    t4."SRN",
    t4."STANDBYNEXTHOPSWITCH"
FROM
huawei_mml_umts."SRCIPRT" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SUBSESSION_NE = ReplaceableObject(
    'huawei_cm_3g."SUBSESSION_NE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion"
FROM
huawei_nbi_umts."SUBSESSION_NE" t1

"""
)

SYS = ReplaceableObject(
    'huawei_cm_3g."SYS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."SYSCONTACT",
    t1."SYSDESC",
    t1."SYSLOCATION",
    t1."SYSOBJECTID",
    t1."SYSSERVICES"
FROM
huawei_nbi_umts."SYS" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."SYSDESC",
    NULL,
    t2."SYSOBJECTID",
    NULL
FROM
huawei_gexport_wcdma."SYS_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."SYSDESC",
    NULL,
    t3."SYSOBJECTID",
    NULL
FROM
huawei_gexport_wcdma."SYS_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."SYSCONTACT",
    t4."SYSDESC",
    t4."SYSLOCATION",
    t4."SYSOBJECTID",
    t4."SYSSERVICES"
FROM
huawei_mml_umts."SYS" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TRMFACTOR = ReplaceableObject(
    'huawei_cm_3g."TRMFACTOR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CSCONVDL",
    t1."CSCONVUL",
    t1."CSSTRMDL",
    t1."CSSTRMUL",
    t1."EFACHDL",
    t1."EPCHDL",
    t1."ERACHUL",
    t1."FTI",
    t1."GENCCHDL",
    t1."GENCCHUL",
    t1."HDBKGDL",
    t1."HDCONVDL",
    t1."HDINTERDL",
    t1."HDSIPDL",
    t1."HDSRBDL",
    t1."HDSTRMDL",
    t1."HDVOICEDL",
    t1."HUBKGUL",
    t1."HUCONVUL",
    t1."HUINTERUL",
    t1."HUSIPUL",
    t1."HUSRBUL",
    t1."HUSTRMUL",
    t1."HUVOICEUL",
    t1."PSBKGDL",
    t1."PSBKGUL",
    t1."PSCONVDL",
    t1."PSCONVUL",
    t1."PSINTERDL",
    t1."PSINTERUL",
    t1."PSSTRMDL",
    t1."PSSTRMUL",
    t1."REMARK",
    t1."SIPDL",
    t1."SIPUL",
    t1."SRBDL",
    t1."SRBUL",
    t1."VOICEDL",
    t1."VOICEUL"
FROM
huawei_nbi_umts."TRMFACTOR" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CSCONVDL",
    t2."CSCONVUL",
    t2."CSSTRMDL",
    t2."CSSTRMUL",
    t2."EFACHDL",
    t2."EPCHDL",
    t2."ERACHUL",
    t2."FTI",
    t2."GENCCHDL",
    t2."GENCCHUL",
    t2."HDBKGDL",
    t2."HDCONVDL",
    t2."HDINTERDL",
    t2."HDSIPDL",
    t2."HDSRBDL",
    t2."HDSTRMDL",
    t2."HDVOICEDL",
    t2."HUBKGUL",
    t2."HUCONVUL",
    t2."HUINTERUL",
    t2."HUSIPUL",
    t2."HUSRBUL",
    t2."HUSTRMUL",
    t2."HUVOICEUL",
    t2."PSBKGDL",
    t2."PSBKGUL",
    t2."PSCONVDL",
    t2."PSCONVUL",
    t2."PSINTERDL",
    t2."PSINTERUL",
    t2."PSSTRMDL",
    t2."PSSTRMUL",
    t2."REMARK",
    t2."SIPDL",
    t2."SIPUL",
    t2."SRBDL",
    t2."SRBUL",
    t2."VOICEDL",
    t2."VOICEUL"
FROM
huawei_gexport_wcdma."TRMFACTOR_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CSCONVDL",
    t3."CSCONVUL",
    t3."CSSTRMDL",
    t3."CSSTRMUL",
    t3."EFACHDL",
    t3."EPCHDL",
    t3."ERACHUL",
    t3."FTI",
    t3."GENCCHDL",
    t3."GENCCHUL",
    t3."HDBKGDL",
    t3."HDCONVDL",
    t3."HDINTERDL",
    t3."HDSIPDL",
    t3."HDSRBDL",
    t3."HDSTRMDL",
    t3."HDVOICEDL",
    t3."HUBKGUL",
    t3."HUCONVUL",
    t3."HUINTERUL",
    t3."HUSIPUL",
    t3."HUSRBUL",
    t3."HUSTRMUL",
    t3."HUVOICEUL",
    t3."PSBKGDL",
    t3."PSBKGUL",
    t3."PSCONVDL",
    t3."PSCONVUL",
    t3."PSINTERDL",
    t3."PSINTERUL",
    t3."PSSTRMDL",
    t3."PSSTRMUL",
    t3."REMARK",
    t3."SIPDL",
    t3."SIPUL",
    t3."SRBDL",
    t3."SRBUL",
    t3."VOICEDL",
    t3."VOICEUL"
FROM
huawei_gexport_wcdma."TRMFACTOR_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CSCONVDL",
    t4."CSCONVUL",
    t4."CSSTRMDL",
    t4."CSSTRMUL",
    t4."EFACHDL",
    t4."EPCHDL",
    t4."ERACHUL",
    t4."FTI",
    t4."GENCCHDL",
    t4."GENCCHUL",
    t4."HDBKGDL",
    t4."HDCONVDL",
    t4."HDINTERDL",
    t4."HDSIPDL",
    t4."HDSRBDL",
    t4."HDSTRMDL",
    t4."HDVOICEDL",
    t4."HUBKGUL",
    t4."HUCONVUL",
    t4."HUINTERUL",
    t4."HUSIPUL",
    t4."HUSRBUL",
    t4."HUSTRMUL",
    t4."HUVOICEUL",
    t4."PSBKGDL",
    t4."PSBKGUL",
    t4."PSCONVDL",
    t4."PSCONVUL",
    t4."PSINTERDL",
    t4."PSINTERUL",
    t4."PSSTRMDL",
    t4."PSSTRMUL",
    t4."REMARK",
    t4."SIPDL",
    t4."SIPUL",
    t4."SRBDL",
    t4."SRBUL",
    t4."VOICEDL",
    t4."VOICEUL"
FROM
huawei_mml_umts."TRMFACTOR" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    t5."CSCONVDL",
    t5."CSCONVUL",
    t5."CSSTRMDL",
    t5."CSSTRMUL",
    t5."EFACHDL",
    t5."EPCHDL",
    t5."ERACHUL",
    t5."FTI",
    t5."GENCCHDL",
    t5."GENCCHUL",
    t5."HDBKGDL",
    t5."HDCONVDL",
    t5."HDINTERDL",
    t5."HDSIPDL",
    t5."HDSRBDL",
    t5."HDSTRMDL",
    t5."HDVOICEDL",
    t5."HUBKGUL",
    t5."HUCONVUL",
    t5."HUINTERUL",
    t5."HUSIPUL",
    t5."HUSRBUL",
    t5."HUSTRMUL",
    t5."HUVOICEUL",
    t5."PSBKGDL",
    t5."PSBKGUL",
    t5."PSCONVDL",
    t5."PSCONVUL",
    t5."PSINTERDL",
    t5."PSINTERUL",
    t5."PSSTRMDL",
    t5."PSSTRMUL",
    t5."REMARK",
    t5."SIPDL",
    t5."SIPUL",
    t5."SRBDL",
    t5."SRBUL",
    t5."VOICEDL",
    t5."VOICEUL"
FROM
huawei_mml_umts."TRMFACTOR_MOD" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

TRMLOADTH = ReplaceableObject(
    'huawei_cm_3g."TRMLOADTH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BWDCONGBW",
    t1."BWDCONGCLRBW",
    t1."BWDOVLDCLRRSVBW",
    t1."BWDOVLDRSVBW",
    t1."BWDRSVHOBW",
    t1."FWDCONGBW",
    t1."FWDCONGCLRBW",
    t1."FWDOVLDCLRRSVBW",
    t1."FWDOVLDRSVBW",
    t1."FWDRSVHOBW",
    t1."THTYPE",
    t1."TRANST",
    t1."TRMLOADTHINDEX",
    t1."BWDCONGCLRTH",
    t1."BWDCONGTH",
    t1."BWDOVLDCLRTH",
    t1."BWDOVLDTH",
    t1."BWDRESVHOTH",
    t1."FWDCONGCLRTH",
    t1."FWDCONGTH",
    t1."FWDOVLDCLRTH",
    t1."FWDOVLDTH",
    t1."FWDRESVHOTH"
FROM
huawei_nbi_umts."TRMLOADTH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."THTYPE",
    t2."TRANST",
    t2."TRMLOADTHINDEX",
    t2."BWDCONGCLRTH",
    t2."BWDCONGTH",
    t2."BWDOVLDCLRTH",
    t2."BWDOVLDTH",
    t2."BWDRESVHOTH",
    t2."FWDCONGCLRTH",
    t2."FWDCONGTH",
    t2."FWDOVLDCLRTH",
    t2."FWDOVLDTH",
    t2."FWDRESVHOTH"
FROM
huawei_mml_umts."TRMLOADTH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

TRMMAP = ReplaceableObject(
    'huawei_cm_3g."TRMMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CCHPRIPRI",
    t1."CCHSECPRI",
    t1."CSCONVPRIPRI",
    t1."CSCONVSECPRI",
    t1."CSSTRMPRIPRI",
    t1."CSSTRMSECPRI",
    t1."HDBKGPRIPRI",
    t1."HDBKGSECPRI",
    t1."HDCONVPRIPRI",
    t1."HDCONVSECPRI",
    t1."HDINTHGHPRIPRI",
    t1."HDINTHGHSECPRI",
    t1."HDINTLOWPRIPRI",
    t1."HDINTLOWSECPRI",
    t1."HDINTMIDPRIPRI",
    t1."HDINTMIDSECPRI",
    t1."HDSIPPRIPRI",
    t1."HDSIPSECPRI",
    t1."HDSRBPRIPRI",
    t1."HDSRBSECPRI",
    t1."HDSTRMPRIPRI",
    t1."HDSTRMSECPRI",
    t1."HDVOICEPRIPRI",
    t1."HDVOICESECPRI",
    t1."HUBKGPRIPRI",
    t1."HUBKGSECPRI",
    t1."HUCONVPRIPRI",
    t1."HUCONVSECPRI",
    t1."HUINTHGHPRIPRI",
    t1."HUINTHGHSECPRI",
    t1."HUINTLOWPRIPRI",
    t1."HUINTLOWSECPRI",
    t1."HUINTMIDPRIPRI",
    t1."HUINTMIDSECPRI",
    t1."HUSIPPRIPRI",
    t1."HUSIPSECPRI",
    t1."HUSRBPRIPRI",
    t1."HUSRBSECPRI",
    t1."HUSTRMPRIPRI",
    t1."HUSTRMSECPRI",
    t1."HUVOICEPRIPRI",
    t1."HUVOICESECPRI",
    t1."ITFT",
    t1."PSBKGPRIPRI",
    t1."PSBKGSECPRI",
    t1."PSCONVPRIPRI",
    t1."PSCONVSECPRI",
    t1."PSINTHGHPRIPRI",
    t1."PSINTHGHSECPRI",
    t1."PSINTLOWPRIPRI",
    t1."PSINTLOWSECPRI",
    t1."PSINTMIDPRIPRI",
    t1."PSINTMIDSECPRI",
    t1."PSSTRMPRIPRI",
    t1."PSSTRMSECPRI",
    t1."REMARK",
    t1."SIPPRIPRI",
    t1."SIPSECPRI",
    t1."SRBPRIPRI",
    t1."SRBSECPRI",
    t1."TMI",
    t1."TRANST",
    t1."VOICEPRIPRI",
    t1."VOICESECPRI"
FROM
huawei_nbi_umts."TRMMAP" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CCHPRIPRI",
    t2."CCHSECPRI",
    t2."CSCONVPRIPRI",
    t2."CSCONVSECPRI",
    t2."CSSTRMPRIPRI",
    t2."CSSTRMSECPRI",
    t2."HDBKGPRIPRI",
    t2."HDBKGSECPRI",
    t2."HDCONVPRIPRI",
    t2."HDCONVSECPRI",
    t2."HDINTHGHPRIPRI",
    t2."HDINTHGHSECPRI",
    t2."HDINTLOWPRIPRI",
    t2."HDINTLOWSECPRI",
    t2."HDINTMIDPRIPRI",
    t2."HDINTMIDSECPRI",
    t2."HDSIPPRIPRI",
    t2."HDSIPSECPRI",
    t2."HDSRBPRIPRI",
    t2."HDSRBSECPRI",
    t2."HDSTRMPRIPRI",
    t2."HDSTRMSECPRI",
    t2."HDVOICEPRIPRI",
    t2."HDVOICESECPRI",
    t2."HUBKGPRIPRI",
    t2."HUBKGSECPRI",
    t2."HUCONVPRIPRI",
    t2."HUCONVSECPRI",
    t2."HUINTHGHPRIPRI",
    t2."HUINTHGHSECPRI",
    t2."HUINTLOWPRIPRI",
    t2."HUINTLOWSECPRI",
    t2."HUINTMIDPRIPRI",
    t2."HUINTMIDSECPRI",
    t2."HUSIPPRIPRI",
    t2."HUSIPSECPRI",
    t2."HUSRBPRIPRI",
    t2."HUSRBSECPRI",
    t2."HUSTRMPRIPRI",
    t2."HUSTRMSECPRI",
    t2."HUVOICEPRIPRI",
    t2."HUVOICESECPRI",
    t2."ITFT",
    t2."PSBKGPRIPRI",
    t2."PSBKGSECPRI",
    t2."PSCONVPRIPRI",
    t2."PSCONVSECPRI",
    t2."PSINTHGHPRIPRI",
    t2."PSINTHGHSECPRI",
    t2."PSINTLOWPRIPRI",
    t2."PSINTLOWSECPRI",
    t2."PSINTMIDPRIPRI",
    t2."PSINTMIDSECPRI",
    t2."PSSTRMPRIPRI",
    t2."PSSTRMSECPRI",
    t2."REMARK",
    t2."SIPPRIPRI",
    t2."SIPSECPRI",
    t2."SRBPRIPRI",
    t2."SRBSECPRI",
    t2."TMI",
    t2."TRANST",
    t2."VOICEPRIPRI",
    t2."VOICESECPRI"
FROM
huawei_gexport_wcdma."TRMMAP_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CCHPRIPRI",
    t3."CCHSECPRI",
    t3."CSCONVPRIPRI",
    t3."CSCONVSECPRI",
    t3."CSSTRMPRIPRI",
    t3."CSSTRMSECPRI",
    t3."HDBKGPRIPRI",
    t3."HDBKGSECPRI",
    t3."HDCONVPRIPRI",
    t3."HDCONVSECPRI",
    t3."HDINTHGHPRIPRI",
    t3."HDINTHGHSECPRI",
    t3."HDINTLOWPRIPRI",
    t3."HDINTLOWSECPRI",
    t3."HDINTMIDPRIPRI",
    t3."HDINTMIDSECPRI",
    t3."HDSIPPRIPRI",
    t3."HDSIPSECPRI",
    t3."HDSRBPRIPRI",
    t3."HDSRBSECPRI",
    t3."HDSTRMPRIPRI",
    t3."HDSTRMSECPRI",
    t3."HDVOICEPRIPRI",
    t3."HDVOICESECPRI",
    t3."HUBKGPRIPRI",
    t3."HUBKGSECPRI",
    t3."HUCONVPRIPRI",
    t3."HUCONVSECPRI",
    t3."HUINTHGHPRIPRI",
    t3."HUINTHGHSECPRI",
    t3."HUINTLOWPRIPRI",
    t3."HUINTLOWSECPRI",
    t3."HUINTMIDPRIPRI",
    t3."HUINTMIDSECPRI",
    t3."HUSIPPRIPRI",
    t3."HUSIPSECPRI",
    t3."HUSRBPRIPRI",
    t3."HUSRBSECPRI",
    t3."HUSTRMPRIPRI",
    t3."HUSTRMSECPRI",
    t3."HUVOICEPRIPRI",
    t3."HUVOICESECPRI",
    t3."ITFT",
    t3."PSBKGPRIPRI",
    t3."PSBKGSECPRI",
    t3."PSCONVPRIPRI",
    t3."PSCONVSECPRI",
    t3."PSINTHGHPRIPRI",
    t3."PSINTHGHSECPRI",
    t3."PSINTLOWPRIPRI",
    t3."PSINTLOWSECPRI",
    t3."PSINTMIDPRIPRI",
    t3."PSINTMIDSECPRI",
    t3."PSSTRMPRIPRI",
    t3."PSSTRMSECPRI",
    t3."REMARK",
    t3."SIPPRIPRI",
    t3."SIPSECPRI",
    t3."SRBPRIPRI",
    t3."SRBSECPRI",
    t3."TMI",
    t3."TRANST",
    t3."VOICEPRIPRI",
    t3."VOICESECPRI"
FROM
huawei_gexport_wcdma."TRMMAP_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t4."ITFT",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t4."REMARK",
    NULL,
    NULL,
    NULL,
    NULL,
    t4."TMI",
    t4."TRANST",
    NULL,
    NULL
FROM
huawei_mml_umts."TRMMAP" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t5."ITFT",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t5."REMARK",
    NULL,
    NULL,
    NULL,
    NULL,
    t5."TMI",
    t5."TRANST",
    NULL,
    NULL
FROM
huawei_mml_umts."TRMMAP_MOD" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

U2GNCELL = ReplaceableObject(
    'huawei_cm_3g."U2GNCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLINDHOFLAG",
    t1."CELLID",
    t1."CIOOFFSET",
    t1."DRDECN0THRESHHOLD",
    t1."GSMCELLINDEX",
    t1."HOPRIO",
    t1."INTERRATADJSQHCS",
    t1."MBDRFLAG",
    t1."MBDRPRIO",
    t1."NIRATOVERLAP",
    t1."NPRIO",
    t1."NPRIOFLAG",
    t1."QOFFSET1SN",
    t1."QRXLEVMIN",
    t1."RNCID",
    t1."SIB11IND",
    t1."SIB12IND",
    t1."SRVCCSWITCH",
    t1."TEMPOFFSET1",
    t1."TPENALTYHCSRESELECT",
    t1."U2GNCELLSRC"
FROM
huawei_nbi_umts."U2GNCELL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BLINDHOFLAG",
    t2."CELLID",
    t2."CIOOFFSET",
    t2."DRDECN0THRESHHOLD",
    t2."GSMCELLINDEX",
    t2."HOPRIO",
    t2."INTERRATADJSQHCS",
    t2."MBDRFLAG",
    t2."MBDRPRIO",
    t2."NIRATOVERLAP",
    NULL,
    t2."NPRIOFLAG",
    t2."QOFFSET1SN",
    t2."QRXLEVMIN",
    t2."RNCID",
    t2."SIB11IND",
    t2."SIB12IND",
    t2."SRVCCSWITCH",
    t2."TEMPOFFSET1",
    t2."TPENALTYHCSRESELECT",
    t2."U2GNCELLSRC"
FROM
huawei_mml_umts."U2GNCELL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UACALGO = ReplaceableObject(
    'huawei_cm_3g."UACALGO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACRSTRCTSWITCH",
    t1."IUACINTERVALOFCELL"
FROM
huawei_nbi_umts."UACALGO" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ACRSTRCTSWITCH",
    t2."IUACINTERVALOFCELL"
FROM
huawei_mml_umts."UACALGO" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UADAPALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UADAPALGOSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ADAPSTETRSPARONDATATRSSW",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UADAPALGOSWITCH" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ADAPSTETRSPARONDATATRSSW",
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UADAPALGOSWITCH_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ADAPSTETRSPARONDATATRSSW",
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UADAPALGOSWITCH_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."ADAPSTETRSPARONDATATRSSW",
    NULL
FROM
huawei_mml_umts."UADAPALGOSWITCH" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UADMCTRL = ReplaceableObject(
    'huawei_cm_3g."UADMCTRL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AFSETOBJ",
    t1."DLSRBACTFACTOR",
    t1."LOGICRNCID",
    t1."ULSRBACTFACTOR",
    t1."DLAMRCONVAF",
    t1."DLBACKGROUNDAF",
    t1."DLINTERACTAF",
    t1."DLNONAMRCONVAF",
    t1."DLSTREAMAF",
    t1."HSDPABACKGROUNDAF",
    t1."HSDPACONVAF",
    t1."HSDPAINTERACTAF",
    t1."HSDPASTREAMAF",
    t1."HSUPABACKGROUNDAF",
    t1."HSUPACONVAF",
    t1."HSUPAINTERACTAF",
    t1."HSUPASTREAMAF",
    t1."ULAMRCONVAF",
    t1."ULBACKGROUNDAF",
    t1."ULINTERACTAF",
    t1."ULNONAMRCONVAF",
    t1."ULSTREAMAF"
FROM
huawei_nbi_umts."UADMCTRL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AFSETOBJ",
    t2."DLSRBACTFACTOR",
    NULL,
    t2."ULSRBACTFACTOR",
    t2."DLAMRCONVAF",
    t2."DLBACKGROUNDAF",
    t2."DLINTERACTAF",
    t2."DLNONAMRCONVAF",
    t2."DLSTREAMAF",
    t2."HSDPABACKGROUNDAF",
    t2."HSDPACONVAF",
    t2."HSDPAINTERACTAF",
    t2."HSDPASTREAMAF",
    t2."HSUPABACKGROUNDAF",
    t2."HSUPACONVAF",
    t2."HSUPAINTERACTAF",
    t2."HSUPASTREAMAF",
    t2."ULAMRCONVAF",
    t2."ULBACKGROUNDAF",
    t2."ULINTERACTAF",
    t2."ULNONAMRCONVAF",
    t2."ULSTREAMAF"
FROM
huawei_mml_umts."UADMCTRL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UAICH = ReplaceableObject(
    'huawei_cm_3g."UAICH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AICHTXTIMING",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PRACHPHYCHID",
    t1."STTDIND",
    t1."UAICHPHYCHID"
FROM
huawei_nbi_umts."UAICH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AICHTXTIMING",
    t2."CELLID",
    NULL,
    t2."PRACHPHYCHID",
    t2."STTDIND",
    NULL
FROM
huawei_mml_umts."UAICH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UAMRC = ReplaceableObject(
    'huawei_cm_3g."UAMRC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."COPPERMAXMODE",
    t1."DLMODECHANGETIMERLEN",
    t1."DLTHDE1",
    t1."DLTHDE2",
    t1."DLTHDF1",
    t1."DLTHDF2",
    t1."GOLDMAXMODE",
    t1."LOGICRNCID",
    t1."SILVERMAXMODE",
    t1."ULMODECHANGETIMERLEN"
FROM
huawei_nbi_umts."UAMRC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."COPPERMAXMODE",
    t2."DLMODECHANGETIMERLEN",
    t2."DLTHDE1",
    t2."DLTHDE2",
    t2."DLTHDF1",
    t2."DLTHDF2",
    t2."GOLDMAXMODE",
    NULL,
    t2."SILVERMAXMODE",
    t2."ULMODECHANGETIMERLEN"
FROM
huawei_mml_umts."UAMRC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UAMRCWB = ReplaceableObject(
    'huawei_cm_3g."UAMRCWB"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."COPPERMAXMODE",
    t1."DLMODECHANGETIMERLEN",
    t1."DLTHDE1",
    t1."DLTHDE2",
    t1."DLTHDF1",
    t1."DLTHDF2",
    t1."GOLDMAXMODE",
    t1."LOGICRNCID",
    t1."SILVERMAXMODE",
    t1."ULMODECHANGETIMERLEN"
FROM
huawei_nbi_umts."UAMRCWB" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."COPPERMAXMODE",
    t2."DLMODECHANGETIMERLEN",
    t2."DLTHDE1",
    t2."DLTHDE2",
    t2."DLTHDF1",
    t2."DLTHDF2",
    t2."GOLDMAXMODE",
    NULL,
    t2."SILVERMAXMODE",
    t2."ULMODECHANGETIMERLEN"
FROM
huawei_mml_umts."UAMRCWB" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UBCH = ReplaceableObject(
    'huawei_cm_3g."UBCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BCHPOWER",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."TRCHID"
FROM
huawei_nbi_umts."UBCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BCHPOWER",
    t2."CELLID",
    NULL,
    t2."TRCHID"
FROM
huawei_mml_umts."UBCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCACALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCACALGOSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CACSWITCH",
    t1."FACHUSERNUMRESERV",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCACALGOSWITCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."FACHUSERNUMRESERV",
    NULL
FROM
huawei_mml_umts."UCACALGOSWITCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCALLSHOCKCTRL = ReplaceableObject(
    'huawei_cm_3g."UCALLSHOCKCTRL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CALLSHOCKCTRLSWITCH",
    t1."CALLSHOCKJUDGEPERIOD",
    t1."CAPSFCBASEONCPUSWITCH",
    t1."CAPSFCCPURELTHD",
    t1."CAPSFCCPUTRIGTHD",
    t1."CELLAMRRRCNUM",
    t1."CELLHIGHPRIRRCNUM",
    t1."CELLTOTALRRCNUMTHD",
    t1."NBAMRRRCNUM",
    t1."NBHIGHPRIRRCNUM",
    t1."NBTOTALRRCNUMTHD",
    t1."REGBYFACHSWITCH",
    t1."RRCQUEUEFCSWITCH",
    t1."SYSAMRRRCNUM",
    t1."SYSHIGHPRIRRCNUM",
    t1."SYSRRCREJNUM",
    t1."SYSTOTALRRCNUMTHD"
FROM
huawei_nbi_umts."UCALLSHOCKCTRL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."CALLSHOCKJUDGEPERIOD",
    t2."CAPSFCBASEONCPUSWITCH",
    t2."CAPSFCCPURELTHD",
    t2."CAPSFCCPUTRIGTHD",
    t2."CELLAMRRRCNUM",
    t2."CELLHIGHPRIRRCNUM",
    t2."CELLTOTALRRCNUMTHD",
    t2."NBAMRRRCNUM",
    t2."NBHIGHPRIRRCNUM",
    t2."NBTOTALRRCNUMTHD",
    t2."REGBYFACHSWITCH",
    t2."RRCQUEUEFCSWITCH",
    t2."SYSAMRRRCNUM",
    t2."SYSHIGHPRIRRCNUM",
    t2."SYSRRCREJNUM",
    t2."SYSTOTALRRCNUMTHD"
FROM
huawei_mml_umts."UCALLSHOCKCTRL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCCP = ReplaceableObject(
    'huawei_cm_3g."UCCP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CARRYLNKT",
    t1."LOGICRNCID",
    t1."NODEBID",
    t1."PN",
    t1."SCTPLNKID",
    t1."SAALLNKN"
FROM
huawei_nbi_umts."UCCP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CARRYLNKT",
    NULL,
    t2."NODEBID",
    t2."PN",
    t2."SCTPLNKID",
    t2."SAALLNKN"
FROM
huawei_mml_umts."UCCP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCELL = ReplaceableObject(
    'huawei_cm_3g."UCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACTSTATUS",
    t1."BANDIND",
    t1."BLKSTATUS",
    t1."CCHCNOPINDEX",
    t1."CELLHETFLAG",
    t1."CELLID",
    t1."CELLNAME",
    t1."CFGRACIND",
    t1."CIO",
    t1."CNOPGRPINDEX",
    t1."DPGID",
    t1."DSSFLAG",
    t1."DSSSMALLCOVMAXTXPOWER",
    t1."LAC",
    t1."LOCELL",
    t1."LOGICRNCID",
    t1."MAXTXPOWER",
    t1."NINSYNCIND",
    t1."NODEBNAME",
    t1."NOUTSYNCIND",
    t1."PSCRAMBCODE",
    t1."RAC",
    t1."SAC",
    t1."SPGID",
    t1."TCELL",
    t1."TRLFAILURE",
    t1."TXDIVERSITYIND",
    t1."UARFCNDOWNLINK",
    t1."UARFCNUPLINK",
    t1."UARFCNUPLINKIND",
    t1."VPLIMITIND"
FROM
huawei_nbi_umts."UCELL" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ACTSTATUS",
    t2."BANDIND",
    t2."BLKSTATUS",
    t2."CCHCNOPINDEX",
    t2."CELLHETFLAG",
    t2."CELLID",
    t2."CELLNAME",
    t2."CFGRACIND",
    t2."CIO",
    t2."CNOPGRPINDEX",
    t2."DPGID",
    t2."DSSFLAG",
    t2."DSSSMALLCOVMAXTXPOWER",
    t2."LAC",
    t2."LOCELL",
    t2."LOGICRNCID",
    t2."MAXTXPOWER",
    t2."NINSYNCIND",
    t2."NODEBNAME",
    t2."NOUTSYNCIND",
    t2."PSCRAMBCODE",
    t2."RAC",
    t2."SAC",
    t2."SPGID",
    t2."TCELL",
    t2."TRLFAILURE",
    t2."TXDIVERSITYIND",
    t2."UARFCNDOWNLINK",
    t2."UARFCNUPLINK",
    t2."UARFCNUPLINKIND",
    t2."VPLIMITIND"
FROM
huawei_gexport_wcdma."UCELL_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ACTSTATUS",
    t3."BANDIND",
    t3."BLKSTATUS",
    t3."CCHCNOPINDEX",
    t3."CELLHETFLAG",
    t3."CELLID",
    t3."CELLNAME",
    t3."CFGRACIND",
    t3."CIO",
    t3."CNOPGRPINDEX",
    t3."DPGID",
    t3."DSSFLAG",
    t3."DSSSMALLCOVMAXTXPOWER",
    t3."LAC",
    t3."LOCELL",
    t3."LOGICRNCID",
    t3."MAXTXPOWER",
    t3."NINSYNCIND",
    t3."NODEBNAME",
    t3."NOUTSYNCIND",
    t3."PSCRAMBCODE",
    t3."RAC",
    t3."SAC",
    t3."SPGID",
    t3."TCELL",
    t3."TRLFAILURE",
    t3."TXDIVERSITYIND",
    t3."UARFCNDOWNLINK",
    t3."UARFCNUPLINK",
    t3."UARFCNUPLINKIND",
    t3."VPLIMITIND"
FROM
huawei_gexport_wcdma."UCELL_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t31."FileName" AS FileName,
    t31."varDateTime" AS varDateTime,
    NULL,
    NULL,
    t3."BAM_VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    t3."OMU_IP" AS module_remark,
    NULL,
    NULL, -- t3."ACTSTATUS",
    t3."BANDIND",
    NULL, -- t3."BLKSTATUS",
    t3."CCHCNOPINDEX",
    t3."CELLHETFLAG",
    t3."CELLID",
    t3."CELLNAME",
    t3."CFGRACIND",
    t3."CIO",
    t3."CNOPGRPINDEX",
    t3."DPGID",
    t3."DSSFLAG",
    t3."DSSSMALLCOVMAXTXPOWER",
    hex_to_int(REPLACE(t3."LAC",'H''',''))::varchar as "LAC",
    t3."LOCELL",
    t32."RNCID" AS "LOGICRNCID",
    t3."MAXTXPOWER",
    t3."NINSYNCIND",
    t3."NODEBNAME",
    t3."NOUTSYNCIND",
    t3."PSCRAMBCODE",
    hex_to_int(REPLACE(t3."RAC",'H''',''))::varchar as "RAC",
    hex_to_int(REPLACE(t3."SAC",'H''',''))::varchar as "SAC",
    t3."SPGID",
    t3."TCELL",
    t3."TRLFAILURE",
    t3."TXDIVERSITYIND",
    t3."UARFCNDOWNLINK",
    t3."UARFCNUPLINK",
    t3."UARFCNUPLINKIND",
    t3."VPLIMITIND"
FROM
huawei_mml_umts."UCELLSETUP" t3
INNER JOIN huawei_mml_umts."SYS" t31 ON t31."FileName" = t3."FileName"
INNER JOIN huawei_mml_umts."URNCBASIC" t32 ON t32."FileName" = t3."FileName"

"""
)

UCELLACCESSSTRICT = ReplaceableObject(
    'huawei_cm_3g."UCELLACCESSSTRICT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CELLRESERVATIONEXTENSION",
    t1."CELLRESERVEDFOROPERATORUSE",
    t1."CONNCELLBARRED",
    t1."DOMAINTYPE",
    t1."IDLECELLBARRED",
    t1."ISACCESSCLASS0BARRED",
    t1."ISACCESSCLASS10BARRED",
    t1."ISACCESSCLASS11BARRED",
    t1."ISACCESSCLASS12BARRED",
    t1."ISACCESSCLASS13BARRED",
    t1."ISACCESSCLASS14BARRED",
    t1."ISACCESSCLASS15BARRED",
    t1."ISACCESSCLASS1BARRED",
    t1."ISACCESSCLASS2BARRED",
    t1."ISACCESSCLASS3BARRED",
    t1."ISACCESSCLASS4BARRED",
    t1."ISACCESSCLASS5BARRED",
    t1."ISACCESSCLASS6BARRED",
    t1."ISACCESSCLASS7BARRED",
    t1."ISACCESSCLASS8BARRED",
    t1."ISACCESSCLASS9BARRED",
    t1."LOGICRNCID",
    t1."IDLEINTRAFREQRESELECTION",
    t1."IDLETBARRED"
FROM
huawei_nbi_umts."UCELLACCESSSTRICT" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."CELLRESERVATIONEXTENSION",
    t2."CELLRESERVEDFOROPERATORUSE",
    t2."CONNCELLBARRED",
    t2."DOMAINTYPE",
    t2."IDLECELLBARRED",
    t2."ISACCESSCLASS0BARRED",
    t2."ISACCESSCLASS10BARRED",
    t2."ISACCESSCLASS11BARRED",
    t2."ISACCESSCLASS12BARRED",
    t2."ISACCESSCLASS13BARRED",
    t2."ISACCESSCLASS14BARRED",
    t2."ISACCESSCLASS15BARRED",
    t2."ISACCESSCLASS1BARRED",
    t2."ISACCESSCLASS2BARRED",
    t2."ISACCESSCLASS3BARRED",
    t2."ISACCESSCLASS4BARRED",
    t2."ISACCESSCLASS5BARRED",
    t2."ISACCESSCLASS6BARRED",
    t2."ISACCESSCLASS7BARRED",
    t2."ISACCESSCLASS8BARRED",
    t2."ISACCESSCLASS9BARRED",
    t2."LOGICRNCID",
    NULL,
    NULL
FROM
huawei_gexport_wcdma."UCELLACCESSSTRICT_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."CELLRESERVATIONEXTENSION",
    t3."CELLRESERVEDFOROPERATORUSE",
    t3."CONNCELLBARRED",
    t3."DOMAINTYPE",
    t3."IDLECELLBARRED",
    t3."ISACCESSCLASS0BARRED",
    t3."ISACCESSCLASS10BARRED",
    t3."ISACCESSCLASS11BARRED",
    t3."ISACCESSCLASS12BARRED",
    t3."ISACCESSCLASS13BARRED",
    t3."ISACCESSCLASS14BARRED",
    t3."ISACCESSCLASS15BARRED",
    t3."ISACCESSCLASS1BARRED",
    t3."ISACCESSCLASS2BARRED",
    t3."ISACCESSCLASS3BARRED",
    t3."ISACCESSCLASS4BARRED",
    t3."ISACCESSCLASS5BARRED",
    t3."ISACCESSCLASS6BARRED",
    t3."ISACCESSCLASS7BARRED",
    t3."ISACCESSCLASS8BARRED",
    t3."ISACCESSCLASS9BARRED",
    t3."LOGICRNCID",
    NULL,
    NULL
FROM
huawei_gexport_wcdma."UCELLACCESSSTRICT_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."CELLRESERVATIONEXTENSION",
    t4."CELLRESERVEDFOROPERATORUSE",
    t4."CONNCELLBARRED",
    t4."DOMAINTYPE",
    t4."IDLECELLBARRED",
    t4."ISACCESSCLASS0BARRED",
    t4."ISACCESSCLASS10BARRED",
    t4."ISACCESSCLASS11BARRED",
    t4."ISACCESSCLASS12BARRED",
    t4."ISACCESSCLASS13BARRED",
    t4."ISACCESSCLASS14BARRED",
    t4."ISACCESSCLASS15BARRED",
    t4."ISACCESSCLASS1BARRED",
    t4."ISACCESSCLASS2BARRED",
    t4."ISACCESSCLASS3BARRED",
    t4."ISACCESSCLASS4BARRED",
    t4."ISACCESSCLASS5BARRED",
    t4."ISACCESSCLASS6BARRED",
    t4."ISACCESSCLASS7BARRED",
    t4."ISACCESSCLASS8BARRED",
    t4."ISACCESSCLASS9BARRED",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UCELLACCESSSTRICT" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCELLALGOSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ADAPALGOSWITCH",
    t1."BERATEREDUCEONFAIRNESSSWITCH",
    t1."CELLCALLSHOCKSWITCH",
    t1."CELLCAPACITYAUTOHANDLESWITCH",
    t1."CELLID",
    t1."CELLMOCNDEMARCSWITCH",
    t1."CELLOMENHSWITCH",
    t1."CSRABCACOPTSWITCH",
    t1."DLPWRLDCUESELSWITCH",
    t1."HSPAENHSWITCH",
    t1."HSPAPLUSSWITCH",
    t1."LOGICRNCID",
    t1."NBMCACALGOSWITCH",
    t1."NBMCACALGOSWITCH2",
    t1."NBMDLCACALGOSELSWITCH",
    t1."NBMLDCALGOSWITCH",
    t1."NBMLDCIRATUESELSWITCH",
    t1."NBMLDCUESELSWITCH",
    t1."NBMMACHSRESETALGOSELSWITCH",
    t1."NBMSFLDCUESELSWITCH",
    t1."NBMULCACALGOSELSWITCH",
    t1."RRCCACCHOICE",
    t1."RRCCECODECACCHOICE"
FROM
huawei_nbi_umts."UCELLALGOSWITCH" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."BERATEREDUCEONFAIRNESSSWITCH",
    t2."CELLCALLSHOCKSWITCH",
    NULL,
    t2."CELLID",
    NULL,
    t2."CELLOMENHSWITCH",
    t2."CSRABCACOPTSWITCH",
    t2."DLPWRLDCUESELSWITCH",
    t2."HSPAENHSWITCH",
    NULL,
    t2."LOGICRNCID",
    NULL,
    NULL,
    t2."NBMDLCACALGOSELSWITCH",
    NULL,
    t2."NBMLDCIRATUESELSWITCH",
    t2."NBMLDCUESELSWITCH",
    t2."NBMMACHSRESETALGOSELSWITCH",
    t2."NBMSFLDCUESELSWITCH",
    t2."NBMULCACALGOSELSWITCH",
    t2."RRCCACCHOICE",
    t2."RRCCECODECACCHOICE"
FROM
huawei_gexport_wcdma."UCELLALGOSWITCH_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."BERATEREDUCEONFAIRNESSSWITCH",
    t3."CELLCALLSHOCKSWITCH",
    NULL,
    t3."CELLID",
    NULL,
    t3."CELLOMENHSWITCH",
    t3."CSRABCACOPTSWITCH",
    t3."DLPWRLDCUESELSWITCH",
    t3."HSPAENHSWITCH",
    NULL,
    t3."LOGICRNCID",
    NULL,
    NULL,
    t3."NBMDLCACALGOSELSWITCH",
    NULL,
    t3."NBMLDCIRATUESELSWITCH",
    t3."NBMLDCUESELSWITCH",
    t3."NBMMACHSRESETALGOSELSWITCH",
    t3."NBMSFLDCUESELSWITCH",
    t3."NBMULCACALGOSELSWITCH",
    t3."RRCCACCHOICE",
    t3."RRCCECODECACCHOICE"
FROM
huawei_gexport_wcdma."UCELLALGOSWITCH_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."BERATEREDUCEONFAIRNESSSWITCH",
    t4."CELLCALLSHOCKSWITCH",
    NULL,
    t4."CELLID",
    NULL,
    t4."CELLOMENHSWITCH",
    t4."CSRABCACOPTSWITCH",
    t4."DLPWRLDCUESELSWITCH",
    t4."HSPAENHSWITCH",
    NULL,
    NULL,
    NULL,
    NULL,
    t4."NBMDLCACALGOSELSWITCH",
    NULL,
    t4."NBMLDCIRATUESELSWITCH",
    t4."NBMLDCUESELSWITCH",
    t4."NBMMACHSRESETALGOSELSWITCH",
    t4."NBMSFLDCUESELSWITCH",
    t4."NBMULCACALGOSELSWITCH",
    t4."RRCCACCHOICE",
    t4."RRCCECODECACCHOICE"
FROM
huawei_mml_umts."UCELLALGOSWITCH" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLCAC = ReplaceableObject(
    'huawei_cm_3g."UCELLCAC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BACKGROUNDNOISE",
    t1."BGNABNORMALTHD",
    t1."BGNADJUSTTIMELEN",
    t1."BGNENDTIME",
    t1."BGNEQUSERNUMTHD",
    t1."BGNOPTSWITCH",
    t1."BGNPERSISTSWITCH",
    t1."BGNSTARTTIME",
    t1."BGNSWITCH",
    t1."BGNULLOADTHD",
    t1."BGNUPDATETHD",
    t1."CELLENVTYPE",
    t1."CELLID",
    t1."CELLULEQUNUMCAPACITY",
    t1."DEFPCPICHECNO",
    t1."DLCCHLOADRSRVCOEFF",
    t1."DLCELLTOTALTHD",
    t1."DLCONVAMRTHD",
    t1."DLCONVNONAMRTHD",
    t1."DLHOCECODERESVSF",
    t1."DLHOTHD",
    t1."DLHSUPARSVDFACTOR",
    t1."DLNRTRRCCACCECODERESVSF",
    t1."DLOTHERRRCCACCECODERESVSF",
    t1."DLOTHERTHD",
    t1."DLRRCCECODERESVSF",
    t1."DLTOTALEQUSERNUM",
    t1."HSDPABEPBRTHD",
    t1."HSDPAMAXGBPTHD",
    t1."HSDPASTRMPBRTHD",
    t1."HSUPAEQUALPRIORITYUSERPBRTHD",
    t1."HSUPAHIGHPRIORITYUSERPBRTHD",
    t1."HSUPALOWPRIORITYUSERPBRTHD",
    t1."HSUPAMAXGBPTHD",
    t1."LOADBALANCERATIO",
    t1."LOGICRNCID",
    t1."MAXEFACHUSERNUM",
    t1."MAXERACHUSERNUM",
    t1."MAXHSDPAUSERNUM",
    t1."MAXHSUPAUSERNUM",
    t1."MAXULTXPOWERFORBAC",
    t1."MAXULTXPOWERFORCONV",
    t1."MAXULTXPOWERFORINT",
    t1."MAXULTXPOWERFORSTR",
    t1."NONHPWRFORGBPPREEMP",
    t1."NRTRRCCACTHDOFFSET",
    t1."OTHERRRCCACTHDOFFSET",
    t1."ROTCONTROLTARGET",
    t1."RTRRCCACTHDOFFSET",
    t1."TERMCONVUSINGHORESTHD",
    t1."ULCCHLOADFACTOR",
    t1."ULCELLTOTALTHD",
    t1."ULHOCERESVSF",
    t1."ULHSDPCCHRSVDFACTOR",
    t1."ULICLDCOPTSWITCH",
    t1."ULNONCTRLTHDFORAMR",
    t1."ULNONCTRLTHDFORHO",
    t1."ULNONCTRLTHDFORNONAMR",
    t1."ULNONCTRLTHDFOROTHER",
    t1."ULNRTRRCCACCERESVSF",
    t1."ULOTHERRRCCACCERESVSF",
    t1."ULRRCCERESVSF",
    t1."ULTOTALEQUSERNUM"
FROM
huawei_nbi_umts."UCELLCAC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BACKGROUNDNOISE",
    t2."BGNABNORMALTHD",
    t2."BGNADJUSTTIMELEN",
    t2."BGNENDTIME",
    t2."BGNEQUSERNUMTHD",
    t2."BGNOPTSWITCH",
    t2."BGNPERSISTSWITCH",
    t2."BGNSTARTTIME",
    t2."BGNSWITCH",
    NULL,
    t2."BGNUPDATETHD",
    t2."CELLENVTYPE",
    t2."CELLID",
    t2."CELLULEQUNUMCAPACITY",
    t2."DEFPCPICHECNO",
    t2."DLCCHLOADRSRVCOEFF",
    t2."DLCELLTOTALTHD",
    t2."DLCONVAMRTHD",
    t2."DLCONVNONAMRTHD",
    t2."DLHOCECODERESVSF",
    t2."DLHOTHD",
    t2."DLHSUPARSVDFACTOR",
    t2."DLNRTRRCCACCECODERESVSF",
    t2."DLOTHERRRCCACCECODERESVSF",
    t2."DLOTHERTHD",
    t2."DLRRCCECODERESVSF",
    t2."DLTOTALEQUSERNUM",
    t2."HSDPABEPBRTHD",
    t2."HSDPAMAXGBPTHD",
    t2."HSDPASTRMPBRTHD",
    t2."HSUPAEQUALPRIORITYUSERPBRTHD",
    t2."HSUPAHIGHPRIORITYUSERPBRTHD",
    t2."HSUPALOWPRIORITYUSERPBRTHD",
    t2."HSUPAMAXGBPTHD",
    t2."LOADBALANCERATIO",
    t2."LOGICRNCID",
    t2."MAXEFACHUSERNUM",
    t2."MAXERACHUSERNUM",
    t2."MAXHSDPAUSERNUM",
    t2."MAXHSUPAUSERNUM",
    t2."MAXULTXPOWERFORBAC",
    t2."MAXULTXPOWERFORCONV",
    t2."MAXULTXPOWERFORINT",
    t2."MAXULTXPOWERFORSTR",
    t2."NONHPWRFORGBPPREEMP",
    t2."NRTRRCCACTHDOFFSET",
    t2."OTHERRRCCACTHDOFFSET",
    t2."ROTCONTROLTARGET",
    t2."RTRRCCACTHDOFFSET",
    t2."TERMCONVUSINGHORESTHD",
    t2."ULCCHLOADFACTOR",
    t2."ULCELLTOTALTHD",
    t2."ULHOCERESVSF",
    t2."ULHSDPCCHRSVDFACTOR",
    t2."ULICLDCOPTSWITCH",
    t2."ULNONCTRLTHDFORAMR",
    t2."ULNONCTRLTHDFORHO",
    t2."ULNONCTRLTHDFORNONAMR",
    t2."ULNONCTRLTHDFOROTHER",
    t2."ULNRTRRCCACCERESVSF",
    t2."ULOTHERRRCCACCERESVSF",
    t2."ULRRCCERESVSF",
    t2."ULTOTALEQUSERNUM"
FROM
huawei_gexport_wcdma."UCELLCAC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BACKGROUNDNOISE",
    t3."BGNABNORMALTHD",
    t3."BGNADJUSTTIMELEN",
    t3."BGNENDTIME",
    t3."BGNEQUSERNUMTHD",
    t3."BGNOPTSWITCH",
    t3."BGNPERSISTSWITCH",
    t3."BGNSTARTTIME",
    t3."BGNSWITCH",
    NULL,
    t3."BGNUPDATETHD",
    t3."CELLENVTYPE",
    t3."CELLID",
    t3."CELLULEQUNUMCAPACITY",
    t3."DEFPCPICHECNO",
    t3."DLCCHLOADRSRVCOEFF",
    t3."DLCELLTOTALTHD",
    t3."DLCONVAMRTHD",
    t3."DLCONVNONAMRTHD",
    t3."DLHOCECODERESVSF",
    t3."DLHOTHD",
    t3."DLHSUPARSVDFACTOR",
    t3."DLNRTRRCCACCECODERESVSF",
    t3."DLOTHERRRCCACCECODERESVSF",
    t3."DLOTHERTHD",
    t3."DLRRCCECODERESVSF",
    t3."DLTOTALEQUSERNUM",
    t3."HSDPABEPBRTHD",
    t3."HSDPAMAXGBPTHD",
    t3."HSDPASTRMPBRTHD",
    t3."HSUPAEQUALPRIORITYUSERPBRTHD",
    t3."HSUPAHIGHPRIORITYUSERPBRTHD",
    t3."HSUPALOWPRIORITYUSERPBRTHD",
    t3."HSUPAMAXGBPTHD",
    t3."LOADBALANCERATIO",
    t3."LOGICRNCID",
    t3."MAXEFACHUSERNUM",
    t3."MAXERACHUSERNUM",
    t3."MAXHSDPAUSERNUM",
    t3."MAXHSUPAUSERNUM",
    t3."MAXULTXPOWERFORBAC",
    t3."MAXULTXPOWERFORCONV",
    t3."MAXULTXPOWERFORINT",
    t3."MAXULTXPOWERFORSTR",
    t3."NONHPWRFORGBPPREEMP",
    t3."NRTRRCCACTHDOFFSET",
    t3."OTHERRRCCACTHDOFFSET",
    t3."ROTCONTROLTARGET",
    t3."RTRRCCACTHDOFFSET",
    t3."TERMCONVUSINGHORESTHD",
    t3."ULCCHLOADFACTOR",
    t3."ULCELLTOTALTHD",
    t3."ULHOCERESVSF",
    t3."ULHSDPCCHRSVDFACTOR",
    t3."ULICLDCOPTSWITCH",
    t3."ULNONCTRLTHDFORAMR",
    t3."ULNONCTRLTHDFORHO",
    t3."ULNONCTRLTHDFORNONAMR",
    t3."ULNONCTRLTHDFOROTHER",
    t3."ULNRTRRCCACCERESVSF",
    t3."ULOTHERRRCCACCERESVSF",
    t3."ULRRCCERESVSF",
    t3."ULTOTALEQUSERNUM"
FROM
huawei_gexport_wcdma."UCELLCAC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BACKGROUNDNOISE",
    t4."BGNABNORMALTHD",
    t4."BGNADJUSTTIMELEN",
    t4."BGNENDTIME",
    t4."BGNEQUSERNUMTHD",
    t4."BGNOPTSWITCH",
    t4."BGNPERSISTSWITCH",
    t4."BGNSTARTTIME",
    t4."BGNSWITCH",
    NULL,
    t4."BGNUPDATETHD",
    t4."CELLENVTYPE",
    t4."CELLID",
    t4."CELLULEQUNUMCAPACITY",
    t4."DEFPCPICHECNO",
    t4."DLCCHLOADRSRVCOEFF",
    t4."DLCELLTOTALTHD",
    t4."DLCONVAMRTHD",
    t4."DLCONVNONAMRTHD",
    t4."DLHOCECODERESVSF",
    t4."DLHOTHD",
    t4."DLHSUPARSVDFACTOR",
    t4."DLNRTRRCCACCECODERESVSF",
    t4."DLOTHERRRCCACCECODERESVSF",
    t4."DLOTHERTHD",
    t4."DLRRCCECODERESVSF",
    t4."DLTOTALEQUSERNUM",
    t4."HSDPABEPBRTHD",
    t4."HSDPAMAXGBPTHD",
    t4."HSDPASTRMPBRTHD",
    t4."HSUPAEQUALPRIORITYUSERPBRTHD",
    t4."HSUPAHIGHPRIORITYUSERPBRTHD",
    t4."HSUPALOWPRIORITYUSERPBRTHD",
    t4."HSUPAMAXGBPTHD",
    t4."LOADBALANCERATIO",
    NULL,
    t4."MAXEFACHUSERNUM",
    t4."MAXERACHUSERNUM",
    t4."MAXHSDPAUSERNUM",
    t4."MAXHSUPAUSERNUM",
    t4."MAXULTXPOWERFORBAC",
    t4."MAXULTXPOWERFORCONV",
    t4."MAXULTXPOWERFORINT",
    t4."MAXULTXPOWERFORSTR",
    t4."NONHPWRFORGBPPREEMP",
    t4."NRTRRCCACTHDOFFSET",
    t4."OTHERRRCCACTHDOFFSET",
    t4."ROTCONTROLTARGET",
    t4."RTRRCCACTHDOFFSET",
    t4."TERMCONVUSINGHORESTHD",
    t4."ULCCHLOADFACTOR",
    t4."ULCELLTOTALTHD",
    t4."ULHOCERESVSF",
    t4."ULHSDPCCHRSVDFACTOR",
    t4."ULICLDCOPTSWITCH",
    t4."ULNONCTRLTHDFORAMR",
    t4."ULNONCTRLTHDFORHO",
    t4."ULNONCTRLTHDFORNONAMR",
    t4."ULNONCTRLTHDFOROTHER",
    t4."ULNRTRRCCACCERESVSF",
    t4."ULOTHERRRCCACCERESVSF",
    t4."ULRRCCERESVSF",
    t4."ULTOTALEQUSERNUM"
FROM
huawei_mml_umts."UCELLCAC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLCMCF = ReplaceableObject(
    'huawei_cm_3g."UCELLCMCF"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CMCFCELLTYPE",
    t1."DLSFTURNPOINT",
    t1."LOGICRNCID",
    t1."ULSFTURNPOINT"
FROM
huawei_nbi_umts."UCELLCMCF" t1

"""
)

UCELLDCCC = ReplaceableObject(
    'huawei_cm_3g."UCELLDCCC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BEPWRMARGIN",
    t1."CELLID",
    t1."COMBPWRMARGIN",
    t1."DLFULLCVRRATE",
    t1."LOGICRNCID",
    t1."ULFULLCVRRATE"
FROM
huawei_nbi_umts."UCELLDCCC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BEPWRMARGIN",
    t2."CELLID",
    t2."COMBPWRMARGIN",
    t2."DLFULLCVRRATE",
    t2."LOGICRNCID",
    t2."ULFULLCVRRATE"
FROM
huawei_gexport_wcdma."UCELLDCCC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BEPWRMARGIN",
    t3."CELLID",
    t3."COMBPWRMARGIN",
    t3."DLFULLCVRRATE",
    t3."LOGICRNCID",
    t3."ULFULLCVRRATE"
FROM
huawei_gexport_wcdma."UCELLDCCC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BEPWRMARGIN",
    t4."CELLID",
    t4."COMBPWRMARGIN",
    t4."DLFULLCVRRATE",
    NULL,
    t4."ULFULLCVRRATE"
FROM
huawei_mml_umts."UCELLDCCC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLDISTANCEREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UCELLDISTANCEREDIRECTION"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."INTERFREQREDIRDELAYTHD",
    t1."INTERFREQREDIRFACTOROFLDR",
    t1."INTERFREQREDIRFACTOROFNORM",
    t1."INTERFREQREDIRSWITCH",
    t1."LOGICRNCID",
    t1."REDIRBANDIND",
    t1."REDIRSWITCH",
    t1."REDIRUARFCNDOWNLINK",
    t1."REDIRUARFCNUPLINKIND",
    t1."DELAYTHS",
    t1."REDIRFACTOROFLDR",
    t1."REDIRFACTOROFNORM"
FROM
huawei_nbi_umts."UCELLDISTANCEREDIRECTION" t1

"""
)

UCELLDRD = ReplaceableObject(
    'huawei_cm_3g."UCELLDRD"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BASEDONMEASHRETRYDRDSWITCH",
    t1."BASEDUELOCDRDREMAINTHD",
    t1."BASEDUELOCDRDSWITCH",
    t1."CELLID",
    t1."CODEBALANCINGDRDCODERATETHD",
    t1."CODEBALANCINGDRDMINSFTHD",
    t1."CODEBALANCINGDRDSWITCH",
    t1."CONNECTFAILRRCREDIRSWITCH",
    t1."D2EDRDSWITCH",
    t1."DPGDRDSWITCH",
    t1."DRMAXGSMNUM",
    t1."HSPAPLUSSATISSWITCH",
    t1."LDBDRDCHOICE",
    t1."LDBDRDLOADREMAINTHDDCH",
    t1."LDBDRDLOADREMAINTHDHSDPA",
    t1."LDBDRDSWITCHDCH",
    t1."LDBDRDSWITCHHSDPA",
    t1."LOGICRNCID",
    t1."REDIRBANDIND",
    t1."RRCCELLLOADSORTSWITCH",
    t1."SECCELLLDBDRDCHOICE",
    t1."SECCELLREFBHFLAGSWITCH",
    t1."SERVICEDIFFDRDSWITCH",
    t1."TRAFFTYPEFORBASEDUELOC",
    t1."UELOCBASEDDRDFORC2DSWITCH",
    t1."ULLDBDRDLOADREMAINTHDDCHSDPA",
    t1."ULLDBDRDSWITCHDCHSDPA"
FROM
huawei_nbi_umts."UCELLDRD" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BASEDONMEASHRETRYDRDSWITCH",
    t2."BASEDUELOCDRDREMAINTHD",
    t2."BASEDUELOCDRDSWITCH",
    t2."CELLID",
    t2."CODEBALANCINGDRDCODERATETHD",
    t2."CODEBALANCINGDRDMINSFTHD",
    t2."CODEBALANCINGDRDSWITCH",
    t2."CONNECTFAILRRCREDIRSWITCH",
    t2."D2EDRDSWITCH",
    t2."DPGDRDSWITCH",
    t2."DRMAXGSMNUM",
    t2."HSPAPLUSSATISSWITCH",
    t2."LDBDRDCHOICE",
    t2."LDBDRDLOADREMAINTHDDCH",
    t2."LDBDRDLOADREMAINTHDHSDPA",
    t2."LDBDRDSWITCHDCH",
    t2."LDBDRDSWITCHHSDPA",
    t2."LOGICRNCID",
    t2."REDIRBANDIND",
    t2."RRCCELLLOADSORTSWITCH",
    t2."SECCELLLDBDRDCHOICE",
    t2."SECCELLREFBHFLAGSWITCH",
    t2."SERVICEDIFFDRDSWITCH",
    NULL,
    t2."UELOCBASEDDRDFORC2DSWITCH",
    t2."ULLDBDRDLOADREMAINTHDDCHSDPA",
    t2."ULLDBDRDSWITCHDCHSDPA"
FROM
huawei_gexport_wcdma."UCELLDRD_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BASEDONMEASHRETRYDRDSWITCH",
    t3."BASEDUELOCDRDREMAINTHD",
    t3."BASEDUELOCDRDSWITCH",
    t3."CELLID",
    t3."CODEBALANCINGDRDCODERATETHD",
    t3."CODEBALANCINGDRDMINSFTHD",
    t3."CODEBALANCINGDRDSWITCH",
    t3."CONNECTFAILRRCREDIRSWITCH",
    t3."D2EDRDSWITCH",
    t3."DPGDRDSWITCH",
    t3."DRMAXGSMNUM",
    t3."HSPAPLUSSATISSWITCH",
    t3."LDBDRDCHOICE",
    t3."LDBDRDLOADREMAINTHDDCH",
    t3."LDBDRDLOADREMAINTHDHSDPA",
    t3."LDBDRDSWITCHDCH",
    t3."LDBDRDSWITCHHSDPA",
    t3."LOGICRNCID",
    t3."REDIRBANDIND",
    t3."RRCCELLLOADSORTSWITCH",
    t3."SECCELLLDBDRDCHOICE",
    t3."SECCELLREFBHFLAGSWITCH",
    t3."SERVICEDIFFDRDSWITCH",
    NULL,
    t3."UELOCBASEDDRDFORC2DSWITCH",
    t3."ULLDBDRDLOADREMAINTHDDCHSDPA",
    t3."ULLDBDRDSWITCHDCHSDPA"
FROM
huawei_gexport_wcdma."UCELLDRD_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BASEDONMEASHRETRYDRDSWITCH",
    t4."BASEDUELOCDRDREMAINTHD",
    t4."BASEDUELOCDRDSWITCH",
    t4."CELLID",
    t4."CODEBALANCINGDRDCODERATETHD",
    t4."CODEBALANCINGDRDMINSFTHD",
    t4."CODEBALANCINGDRDSWITCH",
    t4."CONNECTFAILRRCREDIRSWITCH",
    t4."D2EDRDSWITCH",
    t4."DPGDRDSWITCH",
    t4."DRMAXGSMNUM",
    t4."HSPAPLUSSATISSWITCH",
    t4."LDBDRDCHOICE",
    t4."LDBDRDLOADREMAINTHDDCH",
    t4."LDBDRDLOADREMAINTHDHSDPA",
    t4."LDBDRDSWITCHDCH",
    t4."LDBDRDSWITCHHSDPA",
    NULL,
    t4."REDIRBANDIND",
    t4."RRCCELLLOADSORTSWITCH",
    t4."SECCELLLDBDRDCHOICE",
    t4."SECCELLREFBHFLAGSWITCH",
    t4."SERVICEDIFFDRDSWITCH",
    NULL,
    t4."UELOCBASEDDRDFORC2DSWITCH",
    t4."ULLDBDRDLOADREMAINTHDDCHSDPA",
    t4."ULLDBDRDSWITCHDCHSDPA"
FROM
huawei_mml_umts."UCELLDRD" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLDYNSHUTDOWN = ReplaceableObject(
    'huawei_cm_3g."UCELLDYNSHUTDOWN"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."DYNSHUTDOWNSWITCH",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCELLDYNSHUTDOWN" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    t2."DYNSHUTDOWNSWITCH",
    NULL
FROM
huawei_mml_umts."UCELLDYNSHUTDOWN" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCELLFRC = ReplaceableObject(
    'huawei_cm_3g."UCELLFRC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ALLOWEDSAVECODERESOURCE",
    t1."CELLID",
    t1."DLBETRAFFDECTHS",
    t1."ECN0EFFECTTIME",
    t1."ECN0THS",
    t1."LOGICRNCID",
    t1."RRCCAUSESIGCHTYPEIND",
    t1."ULBETRAFFDECTHS",
    t1."RRCCAUSESIGCHTYPEID"
FROM
huawei_nbi_umts."UCELLFRC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ALLOWEDSAVECODERESOURCE",
    t2."CELLID",
    t2."DLBETRAFFDECTHS",
    t2."ECN0EFFECTTIME",
    t2."ECN0THS",
    t2."LOGICRNCID",
    t2."RRCCAUSESIGCHTYPEIND",
    t2."ULBETRAFFDECTHS",
    NULL
FROM
huawei_gexport_wcdma."UCELLFRC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ALLOWEDSAVECODERESOURCE",
    t3."CELLID",
    t3."DLBETRAFFDECTHS",
    t3."ECN0EFFECTTIME",
    t3."ECN0THS",
    t3."LOGICRNCID",
    t3."RRCCAUSESIGCHTYPEIND",
    t3."ULBETRAFFDECTHS",
    NULL
FROM
huawei_gexport_wcdma."UCELLFRC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."ALLOWEDSAVECODERESOURCE",
    t4."CELLID",
    t4."DLBETRAFFDECTHS",
    t4."ECN0EFFECTTIME",
    t4."ECN0THS",
    NULL,
    t4."RRCCAUSESIGCHTYPEIND",
    t4."ULBETRAFFDECTHS",
    NULL
FROM
huawei_mml_umts."UCELLFRC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLHCS = ReplaceableObject(
    'huawei_cm_3g."UCELLHCS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."NONHCSCOMPATSWITCH",
    t1."SHCSRAT",
    t1."SSEARCHHCS",
    t1."USEOFHCS"
FROM
huawei_nbi_umts."UCELLHCS" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."LOGICRNCID",
    t2."NONHCSCOMPATSWITCH",
    t2."SHCSRAT",
    t2."SSEARCHHCS",
    t2."USEOFHCS"
FROM
huawei_gexport_wcdma."UCELLHCS_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."LOGICRNCID",
    t3."NONHCSCOMPATSWITCH",
    t3."SHCSRAT",
    t3."SSEARCHHCS",
    t3."USEOFHCS"
FROM
huawei_gexport_wcdma."UCELLHCS_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    NULL,
    t4."NONHCSCOMPATSWITCH",
    t4."SHCSRAT",
    t4."SSEARCHHCS",
    t4."USEOFHCS"
FROM
huawei_mml_umts."UCELLHCS" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLHOCOMM = ReplaceableObject(
    'huawei_cm_3g."UCELLHOCOMM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."COEXISTMEASTHDCHOICE",
    t1."CSSERVICEHOSWITCH",
    t1."FASTRETURNTOLTESWITCH",
    t1."HSPATIMERLEN",
    t1."INTERFREQRATSWITCH",
    t1."LOGICRNCID",
    t1."MACROMICRO1APREMEASSWITCH",
    t1."PSSERVICEHOSWITCH",
    t1."SPECUSERCSTHD2DECN0",
    t1."SPECUSERCSTHD2DRSCP",
    t1."SPECUSERCSTHD2FECN0",
    t1."SPECUSERCSTHD2FRSCP",
    t1."SPECUSERHYSTFOR2D",
    t1."U2LBLINDREDIRSWITCH",
    t1."U2LLTELOADSWITCH"
FROM
huawei_nbi_umts."UCELLHOCOMM" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."COEXISTMEASTHDCHOICE",
    t2."CSSERVICEHOSWITCH",
    NULL,
    t2."HSPATIMERLEN",
    t2."INTERFREQRATSWITCH",
    t2."LOGICRNCID",
    t2."MACROMICRO1APREMEASSWITCH",
    t2."PSSERVICEHOSWITCH",
    t2."SPECUSERCSTHD2DECN0",
    t2."SPECUSERCSTHD2DRSCP",
    t2."SPECUSERCSTHD2FECN0",
    t2."SPECUSERCSTHD2FRSCP",
    t2."SPECUSERHYSTFOR2D",
    t2."U2LBLINDREDIRSWITCH",
    NULL
FROM
huawei_gexport_wcdma."UCELLHOCOMM_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."COEXISTMEASTHDCHOICE",
    t3."CSSERVICEHOSWITCH",
    NULL,
    t3."HSPATIMERLEN",
    t3."INTERFREQRATSWITCH",
    t3."LOGICRNCID",
    t3."MACROMICRO1APREMEASSWITCH",
    t3."PSSERVICEHOSWITCH",
    t3."SPECUSERCSTHD2DECN0",
    t3."SPECUSERCSTHD2DRSCP",
    t3."SPECUSERCSTHD2FECN0",
    t3."SPECUSERCSTHD2FRSCP",
    t3."SPECUSERHYSTFOR2D",
    t3."U2LBLINDREDIRSWITCH",
    NULL
FROM
huawei_gexport_wcdma."UCELLHOCOMM_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."COEXISTMEASTHDCHOICE",
    t4."CSSERVICEHOSWITCH",
    NULL,
    t4."HSPATIMERLEN",
    t4."INTERFREQRATSWITCH",
    NULL,
    t4."MACROMICRO1APREMEASSWITCH",
    t4."PSSERVICEHOSWITCH",
    t4."SPECUSERCSTHD2DECN0",
    t4."SPECUSERCSTHD2DRSCP",
    t4."SPECUSERCSTHD2FECN0",
    t4."SPECUSERCSTHD2FRSCP",
    t4."SPECUSERHYSTFOR2D",
    t4."U2LBLINDREDIRSWITCH",
    NULL
FROM
huawei_mml_umts."UCELLHOCOMM" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLHSDPA = ReplaceableObject(
    'huawei_cm_3g."UCELLHSDPA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACTSTATUS",
    t1."ALLOCCODEMODE",
    t1."CELLID",
    t1."CODEADJFORHSDPASWITCH",
    t1."CODEADJFORHSDPAUSERNUMTHD",
    t1."DYNHSSCCHALLOCSWITCH",
    t1."HCODEADJPUNSHTIMERLENGTH",
    t1."HSDPCCHPREAMBLESWITCH",
    t1."HSPAPOWER",
    t1."HSPDSCHCODENUM",
    t1."HSPDSCHMPOCONSTENUM",
    t1."HSSCCHCODENUM",
    t1."LOGICRNCID",
    t1."MIMOMPOCONSTANT",
    t1."HSPDSCHMAXCODENUM",
    t1."HSPDSCHMINCODENUM"
FROM
huawei_nbi_umts."UCELLHSDPA" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ACTSTATUS",
    t2."ALLOCCODEMODE",
    t2."CELLID",
    t2."CODEADJFORHSDPASWITCH",
    t2."CODEADJFORHSDPAUSERNUMTHD",
    t2."DYNHSSCCHALLOCSWITCH",
    t2."HCODEADJPUNSHTIMERLENGTH",
    t2."HSDPCCHPREAMBLESWITCH",
    t2."HSPAPOWER",
    NULL,
    t2."HSPDSCHMPOCONSTENUM",
    t2."HSSCCHCODENUM",
    t2."LOGICRNCID",
    t2."MIMOMPOCONSTANT",
    t2."HSPDSCHMAXCODENUM",
    t2."HSPDSCHMINCODENUM"
FROM
huawei_gexport_wcdma."UCELLHSDPA_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ACTSTATUS",
    t3."ALLOCCODEMODE",
    t3."CELLID",
    t3."CODEADJFORHSDPASWITCH",
    t3."CODEADJFORHSDPAUSERNUMTHD",
    t3."DYNHSSCCHALLOCSWITCH",
    t3."HCODEADJPUNSHTIMERLENGTH",
    t3."HSDPCCHPREAMBLESWITCH",
    t3."HSPAPOWER",
    NULL,
    t3."HSPDSCHMPOCONSTENUM",
    t3."HSSCCHCODENUM",
    t3."LOGICRNCID",
    t3."MIMOMPOCONSTANT",
    t3."HSPDSCHMAXCODENUM",
    t3."HSPDSCHMINCODENUM"
FROM
huawei_gexport_wcdma."UCELLHSDPA_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."ALLOCCODEMODE",
    t4."CELLID",
    t4."CODEADJFORHSDPASWITCH",
    t4."CODEADJFORHSDPAUSERNUMTHD",
    t4."DYNHSSCCHALLOCSWITCH",
    t4."HCODEADJPUNSHTIMERLENGTH",
    t4."HSDPCCHPREAMBLESWITCH",
    t4."HSPAPOWER",
    NULL,
    t4."HSPDSCHMPOCONSTENUM",
    t4."HSSCCHCODENUM",
    NULL,
    t4."MIMOMPOCONSTANT",
    t4."HSPDSCHMAXCODENUM",
    t4."HSPDSCHMINCODENUM"
FROM
huawei_mml_umts."UCELLHSDPA" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    t5."CELLID",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UCELLHSDPA_ACT" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

UCELLHSDPCCH = ReplaceableObject(
    'huawei_cm_3g."UCELLHSDPCCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CQIFBCK",
    t1."CQIFBCKBASECELLLOAD",
    t1."CQIFBCKBASECOVERAGE",
    t1."CQIFBCKBASECSCOMBSERV",
    t1."CQIFBCKFORCONVER",
    t1."CQIFBCKFORDCMIMO",
    t1."CQIFBCKFORMIMO",
    t1."CQIFBCKFORSHO",
    t1."CQIPO",
    t1."CQIPOFORSHO",
    t1."CQIREF",
    t1."CQIREFFORSHO",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCELLHSDPCCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    t2."CQIFBCK",
    t2."CQIFBCKBASECELLLOAD",
    t2."CQIFBCKBASECOVERAGE",
    t2."CQIFBCKBASECSCOMBSERV",
    t2."CQIFBCKFORCONVER",
    t2."CQIFBCKFORDCMIMO",
    t2."CQIFBCKFORMIMO",
    t2."CQIFBCKFORSHO",
    t2."CQIPO",
    t2."CQIPOFORSHO",
    t2."CQIREF",
    t2."CQIREFFORSHO",
    NULL
FROM
huawei_mml_umts."UCELLHSDPCCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCELLHSUPA = ReplaceableObject(
    'huawei_cm_3g."UCELLHSUPA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACTSTATUS",
    t1."CELLID",
    t1."DYNTGTROTCTRLSWITCH",
    t1."EAGCHCODENUM",
    t1."ERGCHEHICHCODENUM",
    t1."LOGICRNCID",
    t1."MAXTARGETULLOADFACTOR",
    t1."NONSERVTOTOTALEDCHPWRRATIO"
FROM
huawei_nbi_umts."UCELLHSUPA" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."ACTSTATUS",
    t2."CELLID",
    t2."DYNTGTROTCTRLSWITCH",
    t2."EAGCHCODENUM",
    t2."ERGCHEHICHCODENUM",
    t2."LOGICRNCID",
    t2."MAXTARGETULLOADFACTOR",
    t2."NONSERVTOTOTALEDCHPWRRATIO"
FROM
huawei_gexport_wcdma."UCELLHSUPA_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."ACTSTATUS",
    t3."CELLID",
    t3."DYNTGTROTCTRLSWITCH",
    t3."EAGCHCODENUM",
    t3."ERGCHEHICHCODENUM",
    t3."LOGICRNCID",
    t3."MAXTARGETULLOADFACTOR",
    t3."NONSERVTOTOTALEDCHPWRRATIO"
FROM
huawei_gexport_wcdma."UCELLHSUPA_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."CELLID",
    t4."DYNTGTROTCTRLSWITCH",
    t4."EAGCHCODENUM",
    t4."ERGCHEHICHCODENUM",
    NULL,
    t4."MAXTARGETULLOADFACTOR",
    t4."NONSERVTOTOTALEDCHPWRRATIO"
FROM
huawei_mml_umts."UCELLHSUPA" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

UNION
SELECT
    t5."FileName",
    t5."varDateTime",
    NULL,
    NULL,
    t5."BAM_VERSION" AS neversion,
    t51."SYSOBJECTID" AS neid,
    NULL,
    t5."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t5."CELLID",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UCELLHSUPA_ACT" t5
INNER JOIN huawei_mml_umts."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

UCELLINTERFREQHOCOV = ReplaceableObject(
    'huawei_cm_3g."UCELLINTERFREQHOCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."HYSTFOR2D",
    t1."HYSTFOR2F",
    t1."HYSTFORPRDINTERFREQ",
    t1."INTERFREQCSTHD2DECN0",
    t1."INTERFREQCSTHD2DRSCP",
    t1."INTERFREQCSTHD2FECN0",
    t1."INTERFREQCSTHD2FRSCP",
    t1."INTERFREQFILTERCOEF",
    t1."INTERFREQHO2DEVENTTYPE",
    t1."INTERFREQHTHD2DECN0",
    t1."INTERFREQHTHD2DRSCP",
    t1."INTERFREQHTHD2FECN0",
    t1."INTERFREQHTHD2FRSCP",
    t1."INTERFREQMCMODE",
    t1."INTERFREQMEASTIME",
    t1."INTERFREQR99PSTHD2DECN0",
    t1."INTERFREQR99PSTHD2DRSCP",
    t1."INTERFREQR99PSTHD2FECN0",
    t1."INTERFREQR99PSTHD2FRSCP",
    t1."INTERFREQREPORTMODE",
    t1."LOGICRNCID",
    t1."PRDREPORTINTERVAL",
    t1."TARGETFREQCSTHDECN0",
    t1."TARGETFREQCSTHDRSCP",
    t1."TARGETFREQHTHDECN0",
    t1."TARGETFREQHTHDRSCP",
    t1."TARGETFREQR99PSTHDECN0",
    t1."TARGETFREQR99PSTHDRSCP",
    t1."TIMETOINTERFREQHO",
    t1."TIMETOTRIG2D",
    t1."TIMETOTRIG2F",
    t1."TIMETOTRIGFORPRDINTERFREQ",
    t1."USEDFREQCSTHDECN0",
    t1."USEDFREQCSTHDRSCP",
    t1."USEDFREQHTHDECN0",
    t1."USEDFREQHTHDRSCP",
    t1."USEDFREQR99PSTHDECN0",
    t1."USEDFREQR99PSTHDRSCP",
    t1."WEIGHTFORUSEDFREQ"
FROM
huawei_nbi_umts."UCELLINTERFREQHOCOV" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."HYSTFOR2D",
    t2."HYSTFOR2F",
    t2."HYSTFORPRDINTERFREQ",
    t2."INTERFREQCSTHD2DECN0",
    t2."INTERFREQCSTHD2DRSCP",
    t2."INTERFREQCSTHD2FECN0",
    t2."INTERFREQCSTHD2FRSCP",
    t2."INTERFREQFILTERCOEF",
    t2."INTERFREQHO2DEVENTTYPE",
    t2."INTERFREQHTHD2DECN0",
    t2."INTERFREQHTHD2DRSCP",
    t2."INTERFREQHTHD2FECN0",
    t2."INTERFREQHTHD2FRSCP",
    t2."INTERFREQMCMODE",
    t2."INTERFREQMEASTIME",
    t2."INTERFREQR99PSTHD2DECN0",
    t2."INTERFREQR99PSTHD2DRSCP",
    t2."INTERFREQR99PSTHD2FECN0",
    t2."INTERFREQR99PSTHD2FRSCP",
    t2."INTERFREQREPORTMODE",
    t2."LOGICRNCID",
    t2."PRDREPORTINTERVAL",
    t2."TARGETFREQCSTHDECN0",
    t2."TARGETFREQCSTHDRSCP",
    t2."TARGETFREQHTHDECN0",
    t2."TARGETFREQHTHDRSCP",
    t2."TARGETFREQR99PSTHDECN0",
    t2."TARGETFREQR99PSTHDRSCP",
    t2."TIMETOINTERFREQHO",
    t2."TIMETOTRIG2D",
    t2."TIMETOTRIG2F",
    t2."TIMETOTRIGFORPRDINTERFREQ",
    t2."USEDFREQCSTHDECN0",
    t2."USEDFREQCSTHDRSCP",
    t2."USEDFREQHTHDECN0",
    t2."USEDFREQHTHDRSCP",
    t2."USEDFREQR99PSTHDECN0",
    t2."USEDFREQR99PSTHDRSCP",
    t2."WEIGHTFORUSEDFREQ"
FROM
huawei_gexport_wcdma."UCELLINTERFREQHOCOV_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."HYSTFOR2D",
    t3."HYSTFOR2F",
    t3."HYSTFORPRDINTERFREQ",
    t3."INTERFREQCSTHD2DECN0",
    t3."INTERFREQCSTHD2DRSCP",
    t3."INTERFREQCSTHD2FECN0",
    t3."INTERFREQCSTHD2FRSCP",
    t3."INTERFREQFILTERCOEF",
    t3."INTERFREQHO2DEVENTTYPE",
    t3."INTERFREQHTHD2DECN0",
    t3."INTERFREQHTHD2DRSCP",
    t3."INTERFREQHTHD2FECN0",
    t3."INTERFREQHTHD2FRSCP",
    t3."INTERFREQMCMODE",
    t3."INTERFREQMEASTIME",
    t3."INTERFREQR99PSTHD2DECN0",
    t3."INTERFREQR99PSTHD2DRSCP",
    t3."INTERFREQR99PSTHD2FECN0",
    t3."INTERFREQR99PSTHD2FRSCP",
    t3."INTERFREQREPORTMODE",
    t3."LOGICRNCID",
    t3."PRDREPORTINTERVAL",
    t3."TARGETFREQCSTHDECN0",
    t3."TARGETFREQCSTHDRSCP",
    t3."TARGETFREQHTHDECN0",
    t3."TARGETFREQHTHDRSCP",
    t3."TARGETFREQR99PSTHDECN0",
    t3."TARGETFREQR99PSTHDRSCP",
    t3."TIMETOINTERFREQHO",
    t3."TIMETOTRIG2D",
    t3."TIMETOTRIG2F",
    t3."TIMETOTRIGFORPRDINTERFREQ",
    t3."USEDFREQCSTHDECN0",
    t3."USEDFREQCSTHDRSCP",
    t3."USEDFREQHTHDECN0",
    t3."USEDFREQHTHDRSCP",
    t3."USEDFREQR99PSTHDECN0",
    t3."USEDFREQR99PSTHDRSCP",
    t3."WEIGHTFORUSEDFREQ"
FROM
huawei_gexport_wcdma."UCELLINTERFREQHOCOV_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."HYSTFOR2D",
    t4."HYSTFOR2F",
    t4."HYSTFORPRDINTERFREQ",
    t4."INTERFREQCSTHD2DECN0",
    t4."INTERFREQCSTHD2DRSCP",
    t4."INTERFREQCSTHD2FECN0",
    t4."INTERFREQCSTHD2FRSCP",
    t4."INTERFREQFILTERCOEF",
    t4."INTERFREQHO2DEVENTTYPE",
    t4."INTERFREQHTHD2DECN0",
    t4."INTERFREQHTHD2DRSCP",
    t4."INTERFREQHTHD2FECN0",
    t4."INTERFREQHTHD2FRSCP",
    t4."INTERFREQMCMODE",
    t4."INTERFREQMEASTIME",
    t4."INTERFREQR99PSTHD2DECN0",
    t4."INTERFREQR99PSTHD2DRSCP",
    t4."INTERFREQR99PSTHD2FECN0",
    t4."INTERFREQR99PSTHD2FRSCP",
    t4."INTERFREQREPORTMODE",
    NULL,
    t4."PRDREPORTINTERVAL",
    t4."TARGETFREQCSTHDECN0",
    t4."TARGETFREQCSTHDRSCP",
    t4."TARGETFREQHTHDECN0",
    t4."TARGETFREQHTHDRSCP",
    t4."TARGETFREQR99PSTHDECN0",
    t4."TARGETFREQR99PSTHDRSCP",
    t4."TIMETOINTERFREQHO",
    t4."TIMETOTRIG2D",
    t4."TIMETOTRIG2F",
    t4."TIMETOTRIGFORPRDINTERFREQ",
    t4."USEDFREQCSTHDECN0",
    t4."USEDFREQCSTHDRSCP",
    t4."USEDFREQHTHDECN0",
    t4."USEDFREQHTHDRSCP",
    t4."USEDFREQR99PSTHDECN0",
    t4."USEDFREQR99PSTHDRSCP",
    t4."WEIGHTFORUSEDFREQ"
FROM
huawei_mml_umts."UCELLINTERFREQHOCOV" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLINTERRATHOCOV = ReplaceableObject(
    'huawei_cm_3g."UCELLINTERRATHOCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BSICVERIFY",
    t1."CELLID",
    t1."CSBSICVERIFYINDICATION",
    t1."FILTERCOEFOF2D2F",
    t1."HYSTFOR2D",
    t1."HYSTFOR2F",
    t1."HYSTFORINTERRAT",
    t1."INTERRATCSTHD2DECN0",
    t1."INTERRATCSTHD2DRSCP",
    t1."INTERRATCSTHD2FECN0",
    t1."INTERRATCSTHD2FRSCP",
    t1."INTERRATFILTERCOEF",
    t1."INTERRATHO2DEVENTTYPE",
    t1."INTERRATHTHD2DECN0",
    t1."INTERRATHTHD2DRSCP",
    t1."INTERRATHTHD2FECN0",
    t1."INTERRATHTHD2FRSCP",
    t1."INTERRATMEASTIME",
    t1."INTERRATPERIODREPORTINTERVAL",
    t1."INTERRATPHYCHFAILNUM",
    t1."INTERRATPINGPONGHYST",
    t1."INTERRATPINGPONGTIMER",
    t1."INTERRATR99PSTHD2DECN0",
    t1."INTERRATR99PSTHD2DRSCP",
    t1."INTERRATR99PSTHD2FECN0",
    t1."INTERRATR99PSTHD2FRSCP",
    t1."INTERRATREPORTMODE",
    t1."LOGICRNCID",
    t1."PENALTYTIMEFORPHYCHFAIL",
    t1."PSBSICVERIFYINDICATION",
    t1."TARGETRATCSTHD",
    t1."TARGETRATHTHD",
    t1."TARGETRATR99PSTHD",
    t1."TIMETOTRIGFORNONVERIFY",
    t1."TIMETOTRIGFORVERIFY",
    t1."TRIGTIME2D",
    t1."TRIGTIME2F",
    t1."WEIGHTFORUSEDFREQ"
FROM
huawei_nbi_umts."UCELLINTERRATHOCOV" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BSICVERIFY",
    t2."CELLID",
    t2."CSBSICVERIFYINDICATION",
    t2."FILTERCOEFOF2D2F",
    t2."HYSTFOR2D",
    t2."HYSTFOR2F",
    t2."HYSTFORINTERRAT",
    t2."INTERRATCSTHD2DECN0",
    t2."INTERRATCSTHD2DRSCP",
    t2."INTERRATCSTHD2FECN0",
    t2."INTERRATCSTHD2FRSCP",
    t2."INTERRATFILTERCOEF",
    t2."INTERRATHO2DEVENTTYPE",
    t2."INTERRATHTHD2DECN0",
    t2."INTERRATHTHD2DRSCP",
    t2."INTERRATHTHD2FECN0",
    t2."INTERRATHTHD2FRSCP",
    t2."INTERRATMEASTIME",
    t2."INTERRATPERIODREPORTINTERVAL",
    t2."INTERRATPHYCHFAILNUM",
    t2."INTERRATPINGPONGHYST",
    t2."INTERRATPINGPONGTIMER",
    t2."INTERRATR99PSTHD2DECN0",
    t2."INTERRATR99PSTHD2DRSCP",
    t2."INTERRATR99PSTHD2FECN0",
    t2."INTERRATR99PSTHD2FRSCP",
    t2."INTERRATREPORTMODE",
    t2."LOGICRNCID",
    t2."PENALTYTIMEFORPHYCHFAIL",
    t2."PSBSICVERIFYINDICATION",
    t2."TARGETRATCSTHD",
    t2."TARGETRATHTHD",
    t2."TARGETRATR99PSTHD",
    t2."TIMETOTRIGFORNONVERIFY",
    t2."TIMETOTRIGFORVERIFY",
    t2."TRIGTIME2D",
    t2."TRIGTIME2F",
    t2."WEIGHTFORUSEDFREQ"
FROM
huawei_gexport_wcdma."UCELLINTERRATHOCOV_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BSICVERIFY",
    t3."CELLID",
    t3."CSBSICVERIFYINDICATION",
    t3."FILTERCOEFOF2D2F",
    t3."HYSTFOR2D",
    t3."HYSTFOR2F",
    t3."HYSTFORINTERRAT",
    t3."INTERRATCSTHD2DECN0",
    t3."INTERRATCSTHD2DRSCP",
    t3."INTERRATCSTHD2FECN0",
    t3."INTERRATCSTHD2FRSCP",
    t3."INTERRATFILTERCOEF",
    t3."INTERRATHO2DEVENTTYPE",
    t3."INTERRATHTHD2DECN0",
    t3."INTERRATHTHD2DRSCP",
    t3."INTERRATHTHD2FECN0",
    t3."INTERRATHTHD2FRSCP",
    t3."INTERRATMEASTIME",
    t3."INTERRATPERIODREPORTINTERVAL",
    t3."INTERRATPHYCHFAILNUM",
    t3."INTERRATPINGPONGHYST",
    t3."INTERRATPINGPONGTIMER",
    t3."INTERRATR99PSTHD2DECN0",
    t3."INTERRATR99PSTHD2DRSCP",
    t3."INTERRATR99PSTHD2FECN0",
    t3."INTERRATR99PSTHD2FRSCP",
    t3."INTERRATREPORTMODE",
    t3."LOGICRNCID",
    t3."PENALTYTIMEFORPHYCHFAIL",
    t3."PSBSICVERIFYINDICATION",
    t3."TARGETRATCSTHD",
    t3."TARGETRATHTHD",
    t3."TARGETRATR99PSTHD",
    t3."TIMETOTRIGFORNONVERIFY",
    t3."TIMETOTRIGFORVERIFY",
    t3."TRIGTIME2D",
    t3."TRIGTIME2F",
    t3."WEIGHTFORUSEDFREQ"
FROM
huawei_gexport_wcdma."UCELLINTERRATHOCOV_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BSICVERIFY",
    t4."CELLID",
    t4."CSBSICVERIFYINDICATION",
    t4."FILTERCOEFOF2D2F",
    t4."HYSTFOR2D",
    t4."HYSTFOR2F",
    t4."HYSTFORINTERRAT",
    t4."INTERRATCSTHD2DECN0",
    t4."INTERRATCSTHD2DRSCP",
    t4."INTERRATCSTHD2FECN0",
    t4."INTERRATCSTHD2FRSCP",
    t4."INTERRATFILTERCOEF",
    t4."INTERRATHO2DEVENTTYPE",
    t4."INTERRATHTHD2DECN0",
    t4."INTERRATHTHD2DRSCP",
    t4."INTERRATHTHD2FECN0",
    t4."INTERRATHTHD2FRSCP",
    t4."INTERRATMEASTIME",
    t4."INTERRATPERIODREPORTINTERVAL",
    t4."INTERRATPHYCHFAILNUM",
    t4."INTERRATPINGPONGHYST",
    t4."INTERRATPINGPONGTIMER",
    t4."INTERRATR99PSTHD2DECN0",
    t4."INTERRATR99PSTHD2DRSCP",
    t4."INTERRATR99PSTHD2FECN0",
    t4."INTERRATR99PSTHD2FRSCP",
    t4."INTERRATREPORTMODE",
    NULL,
    t4."PENALTYTIMEFORPHYCHFAIL",
    t4."PSBSICVERIFYINDICATION",
    t4."TARGETRATCSTHD",
    t4."TARGETRATHTHD",
    t4."TARGETRATR99PSTHD",
    t4."TIMETOTRIGFORNONVERIFY",
    t4."TIMETOTRIGFORVERIFY",
    t4."TRIGTIME2D",
    t4."TRIGTIME2F",
    t4."WEIGHTFORUSEDFREQ"
FROM
huawei_mml_umts."UCELLINTERRATHOCOV" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLINTERRATHONCOV = ReplaceableObject(
    'huawei_cm_3g."UCELLINTERRATHONCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AMNTOFRPT3C",
    t1."BSICVERIFY",
    t1."CELLID",
    t1."CSHOOUT2GLOADTHD",
    t1."HYSTFOR3C",
    t1."INTERRATFILTERCOEF",
    t1."INTERRATHOATTEMPTS",
    t1."INTERRATMEASTIME",
    t1."INTERRATNCOVHOCSTHD",
    t1."INTERRATNCOVHOPSTHD",
    t1."INTERRATPHYCHFAILNUM",
    t1."LOGICRNCID",
    t1."PENALTYTIMEFORPHYCHFAIL",
    t1."PERIODFOR3C",
    t1."PSHOOUT2GLOADTHD",
    t1."TRIGTIME3C"
FROM
huawei_nbi_umts."UCELLINTERRATHONCOV" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AMNTOFRPT3C",
    t2."BSICVERIFY",
    t2."CELLID",
    t2."CSHOOUT2GLOADTHD",
    t2."HYSTFOR3C",
    t2."INTERRATFILTERCOEF",
    t2."INTERRATHOATTEMPTS",
    t2."INTERRATMEASTIME",
    t2."INTERRATNCOVHOCSTHD",
    t2."INTERRATNCOVHOPSTHD",
    t2."INTERRATPHYCHFAILNUM",
    NULL,
    t2."PENALTYTIMEFORPHYCHFAIL",
    t2."PERIODFOR3C",
    t2."PSHOOUT2GLOADTHD",
    t2."TRIGTIME3C"
FROM
huawei_mml_umts."UCELLINTERRATHONCOV" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCELLINTRAFREQHO = ReplaceableObject(
    'huawei_cm_3g."UCELLINTRAFREQHO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLINDHORSCP1FTHRESHOLD",
    t1."CELLID",
    t1."HYST1AOR1CTRIGSCC",
    t1."HYST1DJUDGETRIGSCC",
    t1."HYSTFOR1A",
    t1."HYSTFOR1B",
    t1."HYSTFOR1C",
    t1."HYSTFOR1D",
    t1."HYSTFOR1F",
    t1."HYSTFOR1J",
    t1."INTRAABLTHDFOR1FECNO",
    t1."INTRAFREQFILTERCOEF",
    t1."INTRAFREQMEASQUANTITY",
    t1."INTRARELTHDFOR1ACSNVP",
    t1."INTRARELTHDFOR1ACSVP",
    t1."INTRARELTHDFOR1APS",
    t1."INTRARELTHDFOR1BCSNVP",
    t1."INTRARELTHDFOR1BCSVP",
    t1."INTRARELTHDFOR1BPS",
    t1."LOGICRNCID",
    t1."MAXCELLINACTIVESET",
    t1."PERIODMRREPORTNUMFOR1A",
    t1."PERIODMRREPORTNUMFOR1C",
    t1."PERIODMRREPORTNUMFOR1J",
    t1."REPORTINTERVALFOR1A",
    t1."REPORTINTERVALFOR1C",
    t1."REPORTINTERVALFOR1J",
    t1."RNCID",
    t1."SHOQUALMIN",
    t1."TRIGTIME1A",
    t1."TRIGTIME1B",
    t1."TRIGTIME1C",
    t1."TRIGTIME1D",
    t1."TRIGTIME1F",
    t1."TRIGTIME1J",
    t1."WEIGHT"
FROM
huawei_nbi_umts."UCELLINTRAFREQHO" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BLINDHORSCP1FTHRESHOLD",
    t2."CELLID",
    t2."HYST1AOR1CTRIGSCC",
    t2."HYST1DJUDGETRIGSCC",
    t2."HYSTFOR1A",
    t2."HYSTFOR1B",
    t2."HYSTFOR1C",
    t2."HYSTFOR1D",
    t2."HYSTFOR1F",
    t2."HYSTFOR1J",
    t2."INTRAABLTHDFOR1FECNO",
    t2."INTRAFREQFILTERCOEF",
    t2."INTRAFREQMEASQUANTITY",
    t2."INTRARELTHDFOR1ACSNVP",
    t2."INTRARELTHDFOR1ACSVP",
    t2."INTRARELTHDFOR1APS",
    t2."INTRARELTHDFOR1BCSNVP",
    t2."INTRARELTHDFOR1BCSVP",
    t2."INTRARELTHDFOR1BPS",
    t2."LOGICRNCID",
    t2."MAXCELLINACTIVESET",
    t2."PERIODMRREPORTNUMFOR1A",
    t2."PERIODMRREPORTNUMFOR1C",
    t2."PERIODMRREPORTNUMFOR1J",
    t2."REPORTINTERVALFOR1A",
    t2."REPORTINTERVALFOR1C",
    t2."REPORTINTERVALFOR1J",
    t2."RNCID",
    t2."SHOQUALMIN",
    t2."TRIGTIME1A",
    t2."TRIGTIME1B",
    t2."TRIGTIME1C",
    t2."TRIGTIME1D",
    t2."TRIGTIME1F",
    t2."TRIGTIME1J",
    t2."WEIGHT"
FROM
huawei_gexport_wcdma."UCELLINTRAFREQHO_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BLINDHORSCP1FTHRESHOLD",
    t3."CELLID",
    t3."HYST1AOR1CTRIGSCC",
    t3."HYST1DJUDGETRIGSCC",
    t3."HYSTFOR1A",
    t3."HYSTFOR1B",
    t3."HYSTFOR1C",
    t3."HYSTFOR1D",
    t3."HYSTFOR1F",
    t3."HYSTFOR1J",
    t3."INTRAABLTHDFOR1FECNO",
    t3."INTRAFREQFILTERCOEF",
    t3."INTRAFREQMEASQUANTITY",
    t3."INTRARELTHDFOR1ACSNVP",
    t3."INTRARELTHDFOR1ACSVP",
    t3."INTRARELTHDFOR1APS",
    t3."INTRARELTHDFOR1BCSNVP",
    t3."INTRARELTHDFOR1BCSVP",
    t3."INTRARELTHDFOR1BPS",
    t3."LOGICRNCID",
    t3."MAXCELLINACTIVESET",
    t3."PERIODMRREPORTNUMFOR1A",
    t3."PERIODMRREPORTNUMFOR1C",
    t3."PERIODMRREPORTNUMFOR1J",
    t3."REPORTINTERVALFOR1A",
    t3."REPORTINTERVALFOR1C",
    t3."REPORTINTERVALFOR1J",
    t3."RNCID",
    t3."SHOQUALMIN",
    t3."TRIGTIME1A",
    t3."TRIGTIME1B",
    t3."TRIGTIME1C",
    t3."TRIGTIME1D",
    t3."TRIGTIME1F",
    t3."TRIGTIME1J",
    t3."WEIGHT"
FROM
huawei_gexport_wcdma."UCELLINTRAFREQHO_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BLINDHORSCP1FTHRESHOLD",
    t4."CELLID",
    t4."HYST1AOR1CTRIGSCC",
    t4."HYST1DJUDGETRIGSCC",
    t4."HYSTFOR1A",
    t4."HYSTFOR1B",
    t4."HYSTFOR1C",
    t4."HYSTFOR1D",
    t4."HYSTFOR1F",
    t4."HYSTFOR1J",
    t4."INTRAABLTHDFOR1FECNO",
    t4."INTRAFREQFILTERCOEF",
    t4."INTRAFREQMEASQUANTITY",
    t4."INTRARELTHDFOR1ACSNVP",
    t4."INTRARELTHDFOR1ACSVP",
    t4."INTRARELTHDFOR1APS",
    t4."INTRARELTHDFOR1BCSNVP",
    t4."INTRARELTHDFOR1BCSVP",
    t4."INTRARELTHDFOR1BPS",
    NULL,
    t4."MAXCELLINACTIVESET",
    t4."PERIODMRREPORTNUMFOR1A",
    t4."PERIODMRREPORTNUMFOR1C",
    t4."PERIODMRREPORTNUMFOR1J",
    t4."REPORTINTERVALFOR1A",
    t4."REPORTINTERVALFOR1C",
    t4."REPORTINTERVALFOR1J",
    t4."RNCID",
    t4."SHOQUALMIN",
    t4."TRIGTIME1A",
    t4."TRIGTIME1B",
    t4."TRIGTIME1C",
    t4."TRIGTIME1D",
    t4."TRIGTIME1F",
    t4."TRIGTIME1J",
    t4."WEIGHT"
FROM
huawei_mml_umts."UCELLINTRAFREQHO" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLLDB = ReplaceableObject(
    'huawei_cm_3g."UCELLLDB"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCELLLDB" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLLDB_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLLDB_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    NULL
FROM
huawei_mml_umts."UCELLLDB" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLLDM = ReplaceableObject(
    'huawei_cm_3g."UCELLLDM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."DCHUSERNUMCONGTHD",
    t1."DCHUSERNUMNORMALTHD",
    t1."DCHUSERNUMSTATRANSHYSTIME",
    t1."DLCONGSTATETRANSHYSTIME",
    t1."DLHEAVYTHD",
    t1."DLLDRRELTHD",
    t1."DLLDRTRIGTHD",
    t1."DLLDTRNSHYSTIME",
    t1."DLLOADEDTHD",
    t1."DLNONHLOADCONGSTATETHD",
    t1."DLNONHLOADNORMALSTATETHD",
    t1."DLNORMALTHD",
    t1."DLOLCRELTHD",
    t1."DLOLCTRIGTHD",
    t1."DLOVERLOADTHD",
    t1."DLPWRCSCLBRELTHD",
    t1."DLPWRCSCLBTRIGTHD",
    t1."DLPWRPSCLBRELTHD",
    t1."DLPWRPSCLBTRIGTHD",
    t1."DLSFDIV2CMVALIDCODETHD",
    t1."FAIRNESSTHD",
    t1."HSUPAURETRNSLDRELTHD",
    t1."HSUPAURETRNSLDTRIGTHD",
    t1."LOGICRNCID",
    t1."OFFLOADRELATIVETHD",
    t1."RELRATIOFORULRTWP",
    t1."RTWPLOADSTATETRANSHYSTIME",
    t1."SPECUSERPWRENDLPWRTRIGTHD",
    t1."TRIGRATIOFORULRTWP",
    t1."ULLDRRELTHD",
    t1."ULLDRTRIGTHD",
    t1."ULLDTRNSHYSTIME",
    t1."ULOLCRELTHD",
    t1."ULOLCTRIGTHD",
    t1."ULPWRCSCLBRELTHD",
    t1."ULPWRCSCLBTRIGTHD",
    t1."ULPWRPSCLBRELTHD",
    t1."ULPWRPSCLBTRIGTHD",
    t1."ULRTWPCONGTHD",
    t1."ULRTWPNORMALTHD"
FROM
huawei_nbi_umts."UCELLLDM" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."DCHUSERNUMCONGTHD",
    t2."DCHUSERNUMNORMALTHD",
    t2."DCHUSERNUMSTATRANSHYSTIME",
    t2."DLCONGSTATETRANSHYSTIME",
    t2."DLHEAVYTHD",
    t2."DLLDRRELTHD",
    t2."DLLDRTRIGTHD",
    t2."DLLDTRNSHYSTIME",
    t2."DLLOADEDTHD",
    t2."DLNONHLOADCONGSTATETHD",
    t2."DLNONHLOADNORMALSTATETHD",
    t2."DLNORMALTHD",
    t2."DLOLCRELTHD",
    t2."DLOLCTRIGTHD",
    t2."DLOVERLOADTHD",
    t2."DLPWRCSCLBRELTHD",
    t2."DLPWRCSCLBTRIGTHD",
    t2."DLPWRPSCLBRELTHD",
    t2."DLPWRPSCLBTRIGTHD",
    t2."DLSFDIV2CMVALIDCODETHD",
    t2."FAIRNESSTHD",
    t2."HSUPAURETRNSLDRELTHD",
    t2."HSUPAURETRNSLDTRIGTHD",
    t2."LOGICRNCID",
    t2."OFFLOADRELATIVETHD",
    t2."RELRATIOFORULRTWP",
    t2."RTWPLOADSTATETRANSHYSTIME",
    t2."SPECUSERPWRENDLPWRTRIGTHD",
    t2."TRIGRATIOFORULRTWP",
    t2."ULLDRRELTHD",
    t2."ULLDRTRIGTHD",
    t2."ULLDTRNSHYSTIME",
    t2."ULOLCRELTHD",
    t2."ULOLCTRIGTHD",
    t2."ULPWRCSCLBRELTHD",
    t2."ULPWRCSCLBTRIGTHD",
    t2."ULPWRPSCLBRELTHD",
    t2."ULPWRPSCLBTRIGTHD",
    t2."ULRTWPCONGTHD",
    t2."ULRTWPNORMALTHD"
FROM
huawei_gexport_wcdma."UCELLLDM_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."DCHUSERNUMCONGTHD",
    t3."DCHUSERNUMNORMALTHD",
    t3."DCHUSERNUMSTATRANSHYSTIME",
    t3."DLCONGSTATETRANSHYSTIME",
    t3."DLHEAVYTHD",
    t3."DLLDRRELTHD",
    t3."DLLDRTRIGTHD",
    t3."DLLDTRNSHYSTIME",
    t3."DLLOADEDTHD",
    t3."DLNONHLOADCONGSTATETHD",
    t3."DLNONHLOADNORMALSTATETHD",
    t3."DLNORMALTHD",
    t3."DLOLCRELTHD",
    t3."DLOLCTRIGTHD",
    t3."DLOVERLOADTHD",
    t3."DLPWRCSCLBRELTHD",
    t3."DLPWRCSCLBTRIGTHD",
    t3."DLPWRPSCLBRELTHD",
    t3."DLPWRPSCLBTRIGTHD",
    t3."DLSFDIV2CMVALIDCODETHD",
    t3."FAIRNESSTHD",
    t3."HSUPAURETRNSLDRELTHD",
    t3."HSUPAURETRNSLDTRIGTHD",
    t3."LOGICRNCID",
    t3."OFFLOADRELATIVETHD",
    t3."RELRATIOFORULRTWP",
    t3."RTWPLOADSTATETRANSHYSTIME",
    t3."SPECUSERPWRENDLPWRTRIGTHD",
    t3."TRIGRATIOFORULRTWP",
    t3."ULLDRRELTHD",
    t3."ULLDRTRIGTHD",
    t3."ULLDTRNSHYSTIME",
    t3."ULOLCRELTHD",
    t3."ULOLCTRIGTHD",
    t3."ULPWRCSCLBRELTHD",
    t3."ULPWRCSCLBTRIGTHD",
    t3."ULPWRPSCLBRELTHD",
    t3."ULPWRPSCLBTRIGTHD",
    t3."ULRTWPCONGTHD",
    t3."ULRTWPNORMALTHD"
FROM
huawei_gexport_wcdma."UCELLLDM_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."DCHUSERNUMCONGTHD",
    t4."DCHUSERNUMNORMALTHD",
    t4."DCHUSERNUMSTATRANSHYSTIME",
    t4."DLCONGSTATETRANSHYSTIME",
    t4."DLHEAVYTHD",
    t4."DLLDRRELTHD",
    t4."DLLDRTRIGTHD",
    t4."DLLDTRNSHYSTIME",
    t4."DLLOADEDTHD",
    t4."DLNONHLOADCONGSTATETHD",
    t4."DLNONHLOADNORMALSTATETHD",
    t4."DLNORMALTHD",
    t4."DLOLCRELTHD",
    t4."DLOLCTRIGTHD",
    t4."DLOVERLOADTHD",
    t4."DLPWRCSCLBRELTHD",
    t4."DLPWRCSCLBTRIGTHD",
    t4."DLPWRPSCLBRELTHD",
    t4."DLPWRPSCLBTRIGTHD",
    t4."DLSFDIV2CMVALIDCODETHD",
    t4."FAIRNESSTHD",
    t4."HSUPAURETRNSLDRELTHD",
    t4."HSUPAURETRNSLDTRIGTHD",
    NULL,
    t4."OFFLOADRELATIVETHD",
    t4."RELRATIOFORULRTWP",
    t4."RTWPLOADSTATETRANSHYSTIME",
    t4."SPECUSERPWRENDLPWRTRIGTHD",
    t4."TRIGRATIOFORULRTWP",
    t4."ULLDRRELTHD",
    t4."ULLDRTRIGTHD",
    t4."ULLDTRNSHYSTIME",
    t4."ULOLCRELTHD",
    t4."ULOLCTRIGTHD",
    t4."ULPWRCSCLBRELTHD",
    t4."ULPWRCSCLBTRIGTHD",
    t4."ULPWRPSCLBRELTHD",
    t4."ULPWRPSCLBTRIGTHD",
    t4."ULRTWPCONGTHD",
    t4."ULRTWPNORMALTHD"
FROM
huawei_mml_umts."UCELLLDM" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLLDR = ReplaceableObject(
    'huawei_cm_3g."UCELLLDR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CCCHCONGCTRLSWITCH",
    t1."CELLID",
    t1."CELLLDRSFRESTHD",
    t1."CODECONGHOENHANCEIND",
    t1."CODECONGSELINTERFREQHOIND",
    t1."DLCSINTERRATSHOULDBEHOUENUM",
    t1."DLCSINTERRATSHOULDNOTHOUENUM",
    t1."DLINTERFREQHOBWTHD",
    t1."DLINTERFREQHOCELLLOADSPACETHD",
    t1."DLLDRAMRRATEREDUCTIONRABNUM",
    t1."DLLDRBERATEREDUCTIONRABNUM",
    t1."DLLDREIGHTHACTION",
    t1."DLLDRELEVENTHACTION",
    t1."DLLDRFIFTHACTION",
    t1."DLLDRFIRSTACTION",
    t1."DLLDRFOURTHACTION",
    t1."DLLDRNINTHACTION",
    t1."DLLDRPSRTQOSRENEGRABNUM",
    t1."DLLDRSECONDACTION",
    t1."DLLDRSEVENTHACTION",
    t1."DLLDRSIXTHACTION",
    t1."DLLDRTENTHACTION",
    t1."DLLDRTHIRDACTION",
    t1."DLLDRTWELFTHACTION",
    t1."DLLDRWAMRSFRECFGUENUM",
    t1."DLPSINTERRATSHOULDBEHOUENUM",
    t1."DLPSINTERRATSHOULDNOTHOUENUM",
    t1."GOLDUSERLOADCONTROLSWITCH",
    t1."INTERFREQLDHOFORBIDENTC",
    t1."INTERFREQLDHOMETHODSELECTION",
    t1."LDRCODEPRIUSEIND",
    t1."LDRCODEUSEDSPACETHD",
    t1."LOGICRNCID",
    t1."MAXUSERNUMCODEADJ",
    t1."ULCSINTERRATSHOULDBEHOUENUM",
    t1."ULCSINTERRATSHOULDNOTHOUENUM",
    t1."ULINTERFREQHOBWTHD",
    t1."ULINTERFREQHOCELLLOADSPACETHD",
    t1."ULLDRAMRRATEREDUCTIONRABNUM",
    t1."ULLDRBERATEREDUCTIONRABNUM",
    t1."ULLDRCREDITSFRESTHD",
    t1."ULLDREIGHTHACTION",
    t1."ULLDRFIFTHACTION",
    t1."ULLDRFIRSTACTION",
    t1."ULLDRFOURTHACTION",
    t1."ULLDRNINTHACTION",
    t1."ULLDRPSRTQOSRENEGRABNUM",
    t1."ULLDRSECONDACTION",
    t1."ULLDRSEVENTHACTION",
    t1."ULLDRSIXTHACTION",
    t1."ULLDRTHIRDACTION",
    t1."ULPSINTERRATSHOULDBEHOUENUM",
    t1."ULPSINTERRATSHOULDNOTHOUENUM",
    t1."ULTTICREDITSFRESTHD"
FROM
huawei_nbi_umts."UCELLLDR" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CCCHCONGCTRLSWITCH",
    t2."CELLID",
    t2."CELLLDRSFRESTHD",
    t2."CODECONGHOENHANCEIND",
    t2."CODECONGSELINTERFREQHOIND",
    t2."DLCSINTERRATSHOULDBEHOUENUM",
    t2."DLCSINTERRATSHOULDNOTHOUENUM",
    t2."DLINTERFREQHOBWTHD",
    t2."DLINTERFREQHOCELLLOADSPACETHD",
    t2."DLLDRAMRRATEREDUCTIONRABNUM",
    t2."DLLDRBERATEREDUCTIONRABNUM",
    t2."DLLDREIGHTHACTION",
    t2."DLLDRELEVENTHACTION",
    t2."DLLDRFIFTHACTION",
    t2."DLLDRFIRSTACTION",
    t2."DLLDRFOURTHACTION",
    t2."DLLDRNINTHACTION",
    t2."DLLDRPSRTQOSRENEGRABNUM",
    t2."DLLDRSECONDACTION",
    t2."DLLDRSEVENTHACTION",
    t2."DLLDRSIXTHACTION",
    t2."DLLDRTENTHACTION",
    t2."DLLDRTHIRDACTION",
    t2."DLLDRTWELFTHACTION",
    t2."DLLDRWAMRSFRECFGUENUM",
    t2."DLPSINTERRATSHOULDBEHOUENUM",
    t2."DLPSINTERRATSHOULDNOTHOUENUM",
    t2."GOLDUSERLOADCONTROLSWITCH",
    NULL,
    t2."INTERFREQLDHOMETHODSELECTION",
    t2."LDRCODEPRIUSEIND",
    t2."LDRCODEUSEDSPACETHD",
    t2."LOGICRNCID",
    t2."MAXUSERNUMCODEADJ",
    t2."ULCSINTERRATSHOULDBEHOUENUM",
    t2."ULCSINTERRATSHOULDNOTHOUENUM",
    t2."ULINTERFREQHOBWTHD",
    t2."ULINTERFREQHOCELLLOADSPACETHD",
    t2."ULLDRAMRRATEREDUCTIONRABNUM",
    t2."ULLDRBERATEREDUCTIONRABNUM",
    t2."ULLDRCREDITSFRESTHD",
    t2."ULLDREIGHTHACTION",
    t2."ULLDRFIFTHACTION",
    t2."ULLDRFIRSTACTION",
    t2."ULLDRFOURTHACTION",
    t2."ULLDRNINTHACTION",
    t2."ULLDRPSRTQOSRENEGRABNUM",
    t2."ULLDRSECONDACTION",
    t2."ULLDRSEVENTHACTION",
    t2."ULLDRSIXTHACTION",
    t2."ULLDRTHIRDACTION",
    t2."ULPSINTERRATSHOULDBEHOUENUM",
    t2."ULPSINTERRATSHOULDNOTHOUENUM",
    t2."ULTTICREDITSFRESTHD"
FROM
huawei_gexport_wcdma."UCELLLDR_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CCCHCONGCTRLSWITCH",
    t3."CELLID",
    t3."CELLLDRSFRESTHD",
    t3."CODECONGHOENHANCEIND",
    t3."CODECONGSELINTERFREQHOIND",
    t3."DLCSINTERRATSHOULDBEHOUENUM",
    t3."DLCSINTERRATSHOULDNOTHOUENUM",
    t3."DLINTERFREQHOBWTHD",
    t3."DLINTERFREQHOCELLLOADSPACETHD",
    t3."DLLDRAMRRATEREDUCTIONRABNUM",
    t3."DLLDRBERATEREDUCTIONRABNUM",
    t3."DLLDREIGHTHACTION",
    t3."DLLDRELEVENTHACTION",
    t3."DLLDRFIFTHACTION",
    t3."DLLDRFIRSTACTION",
    t3."DLLDRFOURTHACTION",
    t3."DLLDRNINTHACTION",
    t3."DLLDRPSRTQOSRENEGRABNUM",
    t3."DLLDRSECONDACTION",
    t3."DLLDRSEVENTHACTION",
    t3."DLLDRSIXTHACTION",
    t3."DLLDRTENTHACTION",
    t3."DLLDRTHIRDACTION",
    t3."DLLDRTWELFTHACTION",
    t3."DLLDRWAMRSFRECFGUENUM",
    t3."DLPSINTERRATSHOULDBEHOUENUM",
    t3."DLPSINTERRATSHOULDNOTHOUENUM",
    t3."GOLDUSERLOADCONTROLSWITCH",
    NULL,
    t3."INTERFREQLDHOMETHODSELECTION",
    t3."LDRCODEPRIUSEIND",
    t3."LDRCODEUSEDSPACETHD",
    t3."LOGICRNCID",
    t3."MAXUSERNUMCODEADJ",
    t3."ULCSINTERRATSHOULDBEHOUENUM",
    t3."ULCSINTERRATSHOULDNOTHOUENUM",
    t3."ULINTERFREQHOBWTHD",
    t3."ULINTERFREQHOCELLLOADSPACETHD",
    t3."ULLDRAMRRATEREDUCTIONRABNUM",
    t3."ULLDRBERATEREDUCTIONRABNUM",
    t3."ULLDRCREDITSFRESTHD",
    t3."ULLDREIGHTHACTION",
    t3."ULLDRFIFTHACTION",
    t3."ULLDRFIRSTACTION",
    t3."ULLDRFOURTHACTION",
    t3."ULLDRNINTHACTION",
    t3."ULLDRPSRTQOSRENEGRABNUM",
    t3."ULLDRSECONDACTION",
    t3."ULLDRSEVENTHACTION",
    t3."ULLDRSIXTHACTION",
    t3."ULLDRTHIRDACTION",
    t3."ULPSINTERRATSHOULDBEHOUENUM",
    t3."ULPSINTERRATSHOULDNOTHOUENUM",
    t3."ULTTICREDITSFRESTHD"
FROM
huawei_gexport_wcdma."UCELLLDR_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CCCHCONGCTRLSWITCH",
    t4."CELLID",
    t4."CELLLDRSFRESTHD",
    t4."CODECONGHOENHANCEIND",
    t4."CODECONGSELINTERFREQHOIND",
    t4."DLCSINTERRATSHOULDBEHOUENUM",
    t4."DLCSINTERRATSHOULDNOTHOUENUM",
    t4."DLINTERFREQHOBWTHD",
    t4."DLINTERFREQHOCELLLOADSPACETHD",
    t4."DLLDRAMRRATEREDUCTIONRABNUM",
    t4."DLLDRBERATEREDUCTIONRABNUM",
    t4."DLLDREIGHTHACTION",
    t4."DLLDRELEVENTHACTION",
    t4."DLLDRFIFTHACTION",
    t4."DLLDRFIRSTACTION",
    t4."DLLDRFOURTHACTION",
    t4."DLLDRNINTHACTION",
    t4."DLLDRPSRTQOSRENEGRABNUM",
    t4."DLLDRSECONDACTION",
    t4."DLLDRSEVENTHACTION",
    t4."DLLDRSIXTHACTION",
    t4."DLLDRTENTHACTION",
    t4."DLLDRTHIRDACTION",
    t4."DLLDRTWELFTHACTION",
    t4."DLLDRWAMRSFRECFGUENUM",
    t4."DLPSINTERRATSHOULDBEHOUENUM",
    t4."DLPSINTERRATSHOULDNOTHOUENUM",
    t4."GOLDUSERLOADCONTROLSWITCH",
    NULL,
    t4."INTERFREQLDHOMETHODSELECTION",
    t4."LDRCODEPRIUSEIND",
    t4."LDRCODEUSEDSPACETHD",
    NULL,
    t4."MAXUSERNUMCODEADJ",
    t4."ULCSINTERRATSHOULDBEHOUENUM",
    t4."ULCSINTERRATSHOULDNOTHOUENUM",
    t4."ULINTERFREQHOBWTHD",
    t4."ULINTERFREQHOCELLLOADSPACETHD",
    t4."ULLDRAMRRATEREDUCTIONRABNUM",
    t4."ULLDRBERATEREDUCTIONRABNUM",
    t4."ULLDRCREDITSFRESTHD",
    t4."ULLDREIGHTHACTION",
    t4."ULLDRFIFTHACTION",
    t4."ULLDRFIRSTACTION",
    t4."ULLDRFOURTHACTION",
    t4."ULLDRNINTHACTION",
    t4."ULLDRPSRTQOSRENEGRABNUM",
    t4."ULLDRSECONDACTION",
    t4."ULLDRSEVENTHACTION",
    t4."ULLDRSIXTHACTION",
    t4."ULLDRTHIRDACTION",
    t4."ULPSINTERRATSHOULDBEHOUENUM",
    t4."ULPSINTERRATSHOULDNOTHOUENUM",
    t4."ULTTICREDITSFRESTHD"
FROM
huawei_mml_umts."UCELLLDR" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLLICENSE = ReplaceableObject(
    'huawei_cm_3g."UCELLLICENSE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."FUNCSWITCH1",
    t1."FUNCSWITCH2",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCELLLICENSE" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    NULL,
    NULL,
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLLICENSE_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    NULL,
    NULL,
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLLICENSE_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UCELLLICENSE" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLMEAS = ReplaceableObject(
    'huawei_cm_3g."UCELLMEAS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."FACHMEASIND",
    t1."INTERFREQINTERRATMEASIND",
    t1."INTRAFREQMEASIND",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCELLMEAS" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."FACHMEASIND",
    t2."INTERFREQINTERRATMEASIND",
    t2."INTRAFREQMEASIND",
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLMEAS_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."FACHMEASIND",
    t3."INTERFREQINTERRATMEASIND",
    t3."INTRAFREQMEASIND",
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLMEAS_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."FACHMEASIND",
    t4."INTERFREQINTERRATMEASIND",
    t4."INTRAFREQMEASIND",
    NULL
FROM
huawei_mml_umts."UCELLMEAS" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLNFREQPRIOINFO = ReplaceableObject(
    'huawei_cm_3g."UCELLNFREQPRIOINFO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLACKLSTCELLNUMBER",
    t1."CELLID",
    t1."EARFCN",
    t1."EDETECTIND",
    t1."EMEASBW",
    t1."EQRXLEVMIN",
    t1."LOGICRNCID",
    t1."NPRIORITY",
    t1."RSRQSWITCH",
    t1."SUPCNOPGRPINDEX",
    t1."THDTOHIGH",
    t1."THDTOLOW"
FROM
huawei_nbi_umts."UCELLNFREQPRIOINFO" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BLACKLSTCELLNUMBER",
    t2."CELLID",
    t2."EARFCN",
    t2."EDETECTIND",
    t2."EMEASBW",
    t2."EQRXLEVMIN",
    t2."LOGICRNCID",
    t2."NPRIORITY",
    t2."RSRQSWITCH",
    t2."SUPCNOPGRPINDEX",
    t2."THDTOHIGH",
    t2."THDTOLOW"
FROM
huawei_gexport_wcdma."UCELLNFREQPRIOINFO_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BLACKLSTCELLNUMBER",
    t3."CELLID",
    t3."EARFCN",
    t3."EDETECTIND",
    t3."EMEASBW",
    t3."EQRXLEVMIN",
    t3."LOGICRNCID",
    t3."NPRIORITY",
    t3."RSRQSWITCH",
    t3."SUPCNOPGRPINDEX",
    t3."THDTOHIGH",
    t3."THDTOLOW"
FROM
huawei_gexport_wcdma."UCELLNFREQPRIOINFO_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BLACKLSTCELLNUMBER",
    t4."CELLID",
    t4."EARFCN",
    t4."EDETECTIND",
    t4."EMEASBW",
    t4."EQRXLEVMIN",
    NULL,
    t4."NPRIORITY",
    t4."RSRQSWITCH",
    t4."SUPCNOPGRPINDEX",
    t4."THDTOHIGH",
    t4."THDTOLOW"
FROM
huawei_mml_umts."UCELLNFREQPRIOINFO" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLOLC = ReplaceableObject(
    'huawei_cm_3g."UCELLOLC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."DLOLCFTFRSTRCTRABNUM",
    t1."DLOLCFTFRSTRCTTIMES",
    t1."DLOLCTRAFFRELRABNUM",
    t1."FACHPWRREDUCEVALUE",
    t1."GOLDUSEREXECOLCSWITCH",
    t1."LOGICRNCID",
    t1."RATERECOVERTIMERLEN",
    t1."RATERSTRCTCOEF",
    t1."RATERSTRCTTIMERLEN",
    t1."RECOVERCOEF",
    t1."TRANSCCHUSERNUM",
    t1."ULOLCFTFRSTRCTRABNUM",
    t1."ULOLCFTFRSTRCTTIMES",
    t1."ULOLCTRAFFRELRABNUM"
FROM
huawei_nbi_umts."UCELLOLC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."DLOLCFTFRSTRCTRABNUM",
    t2."DLOLCFTFRSTRCTTIMES",
    t2."DLOLCTRAFFRELRABNUM",
    t2."FACHPWRREDUCEVALUE",
    t2."GOLDUSEREXECOLCSWITCH",
    t2."LOGICRNCID",
    t2."RATERECOVERTIMERLEN",
    t2."RATERSTRCTCOEF",
    t2."RATERSTRCTTIMERLEN",
    t2."RECOVERCOEF",
    t2."TRANSCCHUSERNUM",
    t2."ULOLCFTFRSTRCTRABNUM",
    t2."ULOLCFTFRSTRCTTIMES",
    t2."ULOLCTRAFFRELRABNUM"
FROM
huawei_gexport_wcdma."UCELLOLC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."DLOLCFTFRSTRCTRABNUM",
    t3."DLOLCFTFRSTRCTTIMES",
    t3."DLOLCTRAFFRELRABNUM",
    t3."FACHPWRREDUCEVALUE",
    t3."GOLDUSEREXECOLCSWITCH",
    t3."LOGICRNCID",
    t3."RATERECOVERTIMERLEN",
    t3."RATERSTRCTCOEF",
    t3."RATERSTRCTTIMERLEN",
    t3."RECOVERCOEF",
    t3."TRANSCCHUSERNUM",
    t3."ULOLCFTFRSTRCTRABNUM",
    t3."ULOLCFTFRSTRCTTIMES",
    t3."ULOLCTRAFFRELRABNUM"
FROM
huawei_gexport_wcdma."UCELLOLC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."DLOLCFTFRSTRCTRABNUM",
    t4."DLOLCFTFRSTRCTTIMES",
    t4."DLOLCTRAFFRELRABNUM",
    t4."FACHPWRREDUCEVALUE",
    t4."GOLDUSEREXECOLCSWITCH",
    NULL,
    t4."RATERECOVERTIMERLEN",
    t4."RATERSTRCTCOEF",
    t4."RATERSTRCTTIMERLEN",
    t4."RECOVERCOEF",
    t4."TRANSCCHUSERNUM",
    t4."ULOLCFTFRSTRCTRABNUM",
    t4."ULOLCFTFRSTRCTTIMES",
    t4."ULOLCTRAFFRELRABNUM"
FROM
huawei_mml_umts."UCELLOLC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLPUC = ReplaceableObject(
    'huawei_cm_3g."UCELLPUC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."OFFQOFFSET1HEAVY",
    t1."OFFQOFFSET1LIGHT",
    t1."OFFQOFFSET2HEAVY",
    t1."OFFQOFFSET2LIGHT",
    t1."OFFSINTERHEAVY",
    t1."OFFSINTERLIGHT",
    t1."SPUCHEAVY",
    t1."SPUCHYST",
    t1."SPUCLIGHT"
FROM
huawei_nbi_umts."UCELLPUC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."LOGICRNCID",
    t2."OFFQOFFSET1HEAVY",
    t2."OFFQOFFSET1LIGHT",
    t2."OFFQOFFSET2HEAVY",
    t2."OFFQOFFSET2LIGHT",
    t2."OFFSINTERHEAVY",
    t2."OFFSINTERLIGHT",
    t2."SPUCHEAVY",
    t2."SPUCHYST",
    t2."SPUCLIGHT"
FROM
huawei_gexport_wcdma."UCELLPUC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."LOGICRNCID",
    t3."OFFQOFFSET1HEAVY",
    t3."OFFQOFFSET1LIGHT",
    t3."OFFQOFFSET2HEAVY",
    t3."OFFQOFFSET2LIGHT",
    t3."OFFSINTERHEAVY",
    t3."OFFSINTERLIGHT",
    t3."SPUCHEAVY",
    t3."SPUCHYST",
    t3."SPUCLIGHT"
FROM
huawei_gexport_wcdma."UCELLPUC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    NULL,
    t4."OFFQOFFSET1HEAVY",
    t4."OFFQOFFSET1LIGHT",
    t4."OFFQOFFSET2HEAVY",
    t4."OFFQOFFSET2LIGHT",
    t4."OFFSINTERHEAVY",
    t4."OFFSINTERLIGHT",
    t4."SPUCHEAVY",
    t4."SPUCHYST",
    t4."SPUCLIGHT"
FROM
huawei_mml_umts."UCELLPUC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UCELLREDIRECTION"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."REDIRSWITCH",
    t1."TRAFFICTYPE"
FROM
huawei_nbi_umts."UCELLREDIRECTION" t1

"""
)

UCELLRLACTTIME = ReplaceableObject(
    'huawei_cm_3g."UCELLRLACTTIME"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCELLRLACTTIME" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLRLACTTIME_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLRLACTTIME_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    NULL
FROM
huawei_mml_umts."UCELLRLACTTIME" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLRLPWR = ReplaceableObject(
    'huawei_cm_3g."UCELLRLPWR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CNDOMAINID",
    t1."DLSF",
    t1."LOGICRNCID",
    t1."MAXBITRATE",
    t1."RLMAXDLPWR",
    t1."RLMINDLPWR",
    t1."SPECUSERRLMAXDLPWR"
FROM
huawei_nbi_umts."UCELLRLPWR" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."CNDOMAINID",
    t2."DLSF",
    t2."LOGICRNCID",
    t2."MAXBITRATE",
    t2."RLMAXDLPWR",
    t2."RLMINDLPWR",
    t2."SPECUSERRLMAXDLPWR"
FROM
huawei_gexport_wcdma."UCELLRLPWR_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."CNDOMAINID",
    t3."DLSF",
    t3."LOGICRNCID",
    t3."MAXBITRATE",
    t3."RLMAXDLPWR",
    t3."RLMINDLPWR",
    t3."SPECUSERRLMAXDLPWR"
FROM
huawei_gexport_wcdma."UCELLRLPWR_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."CNDOMAINID",
    t4."DLSF",
    NULL,
    t4."MAXBITRATE",
    t4."RLMAXDLPWR",
    t4."RLMINDLPWR",
    t4."SPECUSERRLMAXDLPWR"
FROM
huawei_mml_umts."UCELLRLPWR" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLSELRESEL = ReplaceableObject(
    'huawei_cm_3g."UCELLSELRESEL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CONNQHYST1S",
    t1."CONNQHYST2S",
    t1."CONNSINTERSEARCH",
    t1."CONNSINTRASEARCH",
    t1."IDLEQHYST1S",
    t1."IDLEQHYST2S",
    t1."IDLESINTERSEARCH",
    t1."IDLESINTRASEARCH",
    t1."INTERFREQTRESELSCALINGFACTOR",
    t1."INTERRATTRESELSCALINGFACTOR",
    t1."LOGICRNCID",
    t1."MAXALLOWEDULTXPOWER",
    t1."NONHCSIND",
    t1."PRIORESELECTSWITCH",
    t1."QHYST1SFACH",
    t1."QHYST1SPCH",
    t1."QHYST2SFACH",
    t1."QHYST2SPCH",
    t1."QQUALMIN",
    t1."QRXLEVMIN",
    t1."QRXLEVMINEXTSUP",
    t1."QUALMEAS",
    t1."SPEEDDEPENDENTSCALINGFACTOR",
    t1."SPRIORITY",
    t1."SSEARCHRAT",
    t1."THDPRIORITYSEARCH1",
    t1."THDPRIORITYSEARCH2",
    t1."THDSERVINGLOW",
    t1."THDSERVINGLOW2",
    t1."TRESELECTIONS",
    t1."TRESELECTIONSFACH",
    t1."TRESELECTIONSPCH"
FROM
huawei_nbi_umts."UCELLSELRESEL" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."CONNQHYST1S",
    t2."CONNQHYST2S",
    t2."CONNSINTERSEARCH",
    t2."CONNSINTRASEARCH",
    t2."IDLEQHYST1S",
    t2."IDLEQHYST2S",
    t2."IDLESINTERSEARCH",
    t2."IDLESINTRASEARCH",
    t2."INTERFREQTRESELSCALINGFACTOR",
    t2."INTERRATTRESELSCALINGFACTOR",
    t2."LOGICRNCID",
    t2."MAXALLOWEDULTXPOWER",
    t2."NONHCSIND",
    t2."PRIORESELECTSWITCH",
    t2."QHYST1SFACH",
    t2."QHYST1SPCH",
    t2."QHYST2SFACH",
    t2."QHYST2SPCH",
    t2."QQUALMIN",
    t2."QRXLEVMIN",
    t2."QRXLEVMINEXTSUP",
    t2."QUALMEAS",
    t2."SPEEDDEPENDENTSCALINGFACTOR",
    t2."SPRIORITY",
    t2."SSEARCHRAT",
    t2."THDPRIORITYSEARCH1",
    t2."THDPRIORITYSEARCH2",
    t2."THDSERVINGLOW",
    t2."THDSERVINGLOW2",
    t2."TRESELECTIONS",
    t2."TRESELECTIONSFACH",
    t2."TRESELECTIONSPCH"
FROM
huawei_gexport_wcdma."UCELLSELRESEL_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."CONNQHYST1S",
    t3."CONNQHYST2S",
    t3."CONNSINTERSEARCH",
    t3."CONNSINTRASEARCH",
    t3."IDLEQHYST1S",
    t3."IDLEQHYST2S",
    t3."IDLESINTERSEARCH",
    t3."IDLESINTRASEARCH",
    t3."INTERFREQTRESELSCALINGFACTOR",
    t3."INTERRATTRESELSCALINGFACTOR",
    t3."LOGICRNCID",
    t3."MAXALLOWEDULTXPOWER",
    t3."NONHCSIND",
    t3."PRIORESELECTSWITCH",
    t3."QHYST1SFACH",
    t3."QHYST1SPCH",
    t3."QHYST2SFACH",
    t3."QHYST2SPCH",
    t3."QQUALMIN",
    t3."QRXLEVMIN",
    t3."QRXLEVMINEXTSUP",
    t3."QUALMEAS",
    t3."SPEEDDEPENDENTSCALINGFACTOR",
    t3."SPRIORITY",
    t3."SSEARCHRAT",
    t3."THDPRIORITYSEARCH1",
    t3."THDPRIORITYSEARCH2",
    t3."THDSERVINGLOW",
    t3."THDSERVINGLOW2",
    t3."TRESELECTIONS",
    t3."TRESELECTIONSFACH",
    t3."TRESELECTIONSPCH"
FROM
huawei_gexport_wcdma."UCELLSELRESEL_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    t4."CONNQHYST1S",
    t4."CONNQHYST2S",
    t4."CONNSINTERSEARCH",
    t4."CONNSINTRASEARCH",
    t4."IDLEQHYST1S",
    t4."IDLEQHYST2S",
    t4."IDLESINTERSEARCH",
    t4."IDLESINTRASEARCH",
    t4."INTERFREQTRESELSCALINGFACTOR",
    t4."INTERRATTRESELSCALINGFACTOR",
    NULL,
    t4."MAXALLOWEDULTXPOWER",
    t4."NONHCSIND",
    t4."PRIORESELECTSWITCH",
    t4."QHYST1SFACH",
    t4."QHYST1SPCH",
    t4."QHYST2SFACH",
    t4."QHYST2SPCH",
    t4."QQUALMIN",
    t4."QRXLEVMIN",
    t4."QRXLEVMINEXTSUP",
    t4."QUALMEAS",
    t4."SPEEDDEPENDENTSCALINGFACTOR",
    t4."SPRIORITY",
    t4."SSEARCHRAT",
    t4."THDPRIORITYSEARCH1",
    t4."THDPRIORITYSEARCH2",
    t4."THDSERVINGLOW",
    t4."THDSERVINGLOW2",
    t4."TRESELECTIONS",
    t4."TRESELECTIONSFACH",
    t4."TRESELECTIONSPCH"
FROM
huawei_mml_umts."UCELLSELRESEL" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLSIBSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCELLSIBSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."SIBCFGBITMAP"
FROM
huawei_nbi_umts."UCELLSIBSWITCH" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."LOGICRNCID",
    NULL
FROM
huawei_gexport_wcdma."UCELLSIBSWITCH_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."LOGICRNCID",
    NULL
FROM
huawei_gexport_wcdma."UCELLSIBSWITCH_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    NULL,
    NULL
FROM
huawei_mml_umts."UCELLSIBSWITCH" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLUPDTCTRLSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCELLUPDTCTRLSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLUPDTCAUSE",
    t1."FACHPOWERCELLUPDTECNOTHD",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCELLUPDTCTRLSWITCH" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLUPDTCAUSE",
    t2."FACHPOWERCELLUPDTECNOTHD",
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLUPDTCTRLSWITCH_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLUPDTCAUSE",
    t3."FACHPOWERCELLUPDTECNOTHD",
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UCELLUPDTCTRLSWITCH_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLUPDTCAUSE",
    t4."FACHPOWERCELLUPDTECNOTHD",
    NULL
FROM
huawei_mml_umts."UCELLUPDTCTRLSWITCH" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCELLURA = ReplaceableObject(
    'huawei_cm_3g."UCELLURA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."URAID"
FROM
huawei_nbi_umts."UCELLURA" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CELLID",
    t2."LOGICRNCID",
    t2."URAID"
FROM
huawei_gexport_wcdma."UCELLURA_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CELLID",
    t3."LOGICRNCID",
    t3."URAID"
FROM
huawei_gexport_wcdma."UCELLURA_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CELLID",
    NULL,
    t4."URAID"
FROM
huawei_mml_umts."UCELLURA" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCHLQUALITYEVALUATE = ReplaceableObject(
    'huawei_cm_3g."UCHLQUALITYEVALUATE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BETTI10MSRSCPTHD",
    t1."BETTI10MSRSCPUPTHD",
    t1."BETTI2MSRSCPTHD",
    t1."BETTI2MSRSCPUPTHD",
    t1."LOGICRNCID",
    t1."RSCPEFFECTALGOSWITCH",
    t1."SRBH2DNONHLOADSTATE",
    t1."SRBH2DRABRSCPPERIODTIMER",
    t1."SRBOVERHSDPAECN0DOWNTHD",
    t1."SRBOVERHSDPAECN0UPTHD",
    t1."SRBOVERHSDPARSCPDOWNTHD",
    t1."SRBOVERHSDPARSCPUPTHD"
FROM
huawei_nbi_umts."UCHLQUALITYEVALUATE" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BETTI10MSRSCPTHD",
    t2."BETTI10MSRSCPUPTHD",
    t2."BETTI2MSRSCPTHD",
    t2."BETTI2MSRSCPUPTHD",
    t2."LOGICRNCID",
    NULL,
    t2."SRBH2DNONHLOADSTATE",
    t2."SRBH2DRABRSCPPERIODTIMER",
    t2."SRBOVERHSDPAECN0DOWNTHD",
    t2."SRBOVERHSDPAECN0UPTHD",
    t2."SRBOVERHSDPARSCPDOWNTHD",
    t2."SRBOVERHSDPARSCPUPTHD"
FROM
huawei_gexport_wcdma."UCHLQUALITYEVALUATE_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BETTI10MSRSCPTHD",
    t3."BETTI10MSRSCPUPTHD",
    t3."BETTI2MSRSCPTHD",
    t3."BETTI2MSRSCPUPTHD",
    t3."LOGICRNCID",
    NULL,
    t3."SRBH2DNONHLOADSTATE",
    t3."SRBH2DRABRSCPPERIODTIMER",
    t3."SRBOVERHSDPAECN0DOWNTHD",
    t3."SRBOVERHSDPAECN0UPTHD",
    t3."SRBOVERHSDPARSCPDOWNTHD",
    t3."SRBOVERHSDPARSCPUPTHD"
FROM
huawei_gexport_wcdma."UCHLQUALITYEVALUATE_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BETTI10MSRSCPTHD",
    t4."BETTI10MSRSCPUPTHD",
    t4."BETTI2MSRSCPTHD",
    t4."BETTI2MSRSCPUPTHD",
    NULL,
    NULL,
    t4."SRBH2DNONHLOADSTATE",
    t4."SRBH2DRABRSCPPERIODTIMER",
    t4."SRBOVERHSDPAECN0DOWNTHD",
    t4."SRBOVERHSDPAECN0UPTHD",
    t4."SRBOVERHSDPARSCPDOWNTHD",
    t4."SRBOVERHSDPARSCPUPTHD"
FROM
huawei_mml_umts."UCHLQUALITYEVALUATE" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCHPWROFFSET = ReplaceableObject(
    'huawei_cm_3g."UCHPWROFFSET"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AICHPOWEROFFSET",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PICHPOWEROFFSET"
FROM
huawei_nbi_umts."UCHPWROFFSET" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AICHPOWEROFFSET",
    t2."CELLID",
    NULL,
    t2."PICHPOWEROFFSET"
FROM
huawei_mml_umts."UCHPWROFFSET" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCIDCHG = ReplaceableObject(
    'huawei_cm_3g."UCIDCHG"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLIDCHGSWITCH",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCIDCHG" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLIDCHGSWITCH",
    NULL
FROM
huawei_mml_umts."UCIDCHG" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCLB = ReplaceableObject(
    'huawei_cm_3g."UCLB"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."PENALTYTIMEFORHLOAD3GCELL",
    t1."SEPRNCNCELLLOADESTSWITCH",
    t1."UMTSCELLIFHOFAILNUM",
    t1."UMTSCELLLOADESTSLIDWINDOW"
FROM
huawei_nbi_umts."UCLB" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID",
    t2."PENALTYTIMEFORHLOAD3GCELL",
    t2."SEPRNCNCELLLOADESTSWITCH",
    t2."UMTSCELLIFHOFAILNUM",
    t2."UMTSCELLLOADESTSLIDWINDOW"
FROM
huawei_gexport_wcdma."UCLB_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID",
    t3."PENALTYTIMEFORHLOAD3GCELL",
    t3."SEPRNCNCELLLOADESTSWITCH",
    t3."UMTSCELLIFHOFAILNUM",
    t3."UMTSCELLLOADESTSLIDWINDOW"
FROM
huawei_gexport_wcdma."UCLB_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."PENALTYTIMEFORHLOAD3GCELL",
    t4."SEPRNCNCELLLOADESTSWITCH",
    t4."UMTSCELLIFHOFAILNUM",
    t4."UMTSCELLLOADESTSLIDWINDOW"
FROM
huawei_mml_umts."UCLB" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCMCF = ReplaceableObject(
    'huawei_cm_3g."UCMCF"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CMCFCELLTYPE",
    t1."DLSFLIMITCMIND",
    t1."DLSFTURNPOINT",
    t1."EHSPACMPERMISSIONIND",
    t1."HSDPACMPERMISSIONIND",
    t1."HSUPACMPERMISSIONIND",
    t1."LOGICRNCID",
    t1."NCOVCMUSERNUMCTRLSWITCH",
    t1."ULSFTURNPOINT"
FROM
huawei_nbi_umts."UCMCF" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CMCFCELLTYPE",
    t2."DLSFLIMITCMIND",
    t2."DLSFTURNPOINT",
    t2."EHSPACMPERMISSIONIND",
    t2."HSDPACMPERMISSIONIND",
    t2."HSUPACMPERMISSIONIND",
    NULL,
    t2."NCOVCMUSERNUMCTRLSWITCH",
    t2."ULSFTURNPOINT"
FROM
huawei_mml_umts."UCMCF" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCNDOMAIN = ReplaceableObject(
    'huawei_cm_3g."UCNDOMAIN"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ATT",
    t1."CNDOMAINID",
    t1."DRXCYCLELENCOEF",
    t1."LOGICRNCID",
    t1."T3212",
    t1."NMO"
FROM
huawei_nbi_umts."UCNDOMAIN" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ATT",
    t2."CNDOMAINID",
    t2."DRXCYCLELENCOEF",
    NULL,
    t2."T3212",
    t2."NMO"
FROM
huawei_mml_umts."UCNDOMAIN" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCNNODE = ReplaceableObject(
    'huawei_cm_3g."UCNNODE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AVAILCAP",
    t1."CNDOMAINID",
    t1."CNID",
    t1."CNLOADSTATUS",
    t1."CNOPINDEX",
    t1."CNPROTCLVER",
    t1."DPX",
    t1."LOGICRNCID",
    t1."RTCPSWITCH",
    t1."SWITCH3GPP25415CR0125",
    t1."TNLBEARERTYPE",
    t1."CELLSTATERPTSWITCH",
    t1."DLE2EQOSSWITCH"
FROM
huawei_nbi_umts."UCNNODE" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AVAILCAP",
    t2."CNDOMAINID",
    t2."CNID",
    t2."CNLOADSTATUS",
    t2."CNOPINDEX",
    t2."CNPROTCLVER",
    t2."DPX",
    NULL,
    t2."RTCPSWITCH",
    t2."SWITCH3GPP25415CR0125",
    t2."TNLBEARERTYPE",
    t2."CELLSTATERPTSWITCH",
    t2."DLE2EQOSSWITCH"
FROM
huawei_mml_umts."UCNNODE" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCNOPERATOR = ReplaceableObject(
    'huawei_cm_3g."UCNOPERATOR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPERATORNAME",
    t1."CNOPINDEX",
    t1."LOGICRNCID",
    t1."MCC",
    t1."MNC",
    t1."OPERATORTYPE"
FROM
huawei_nbi_umts."UCNOPERATOR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNOPERATORNAME",
    t2."CNOPINDEX",
    NULL,
    t2."MCC",
    t2."MNC",
    t2."OPERATORTYPE"
FROM
huawei_mml_umts."UCNOPERATOR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCNOPERGROUP = ReplaceableObject(
    'huawei_cm_3g."UCNOPERGROUP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPGRPINDEX",
    t1."CNOPGRPNAME",
    t1."CNOPINDEX1",
    t1."CNOPNUM",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCNOPERGROUP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNOPGRPINDEX",
    t2."CNOPGRPNAME",
    t2."CNOPINDEX1",
    t2."CNOPNUM",
    NULL
FROM
huawei_mml_umts."UCNOPERGROUP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCNTCHK = ReplaceableObject(
    'huawei_cm_3g."UCNTCHK"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."COUNTERCHECKSWITCH",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UCNTCHK" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."COUNTERCHECKSWITCH",
    NULL
FROM
huawei_mml_umts."UCNTCHK" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCOIFTIMER = ReplaceableObject(
    'huawei_cm_3g."UCOIFTIMER"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ADAPRETRANPUNTIMER",
    t1."CHANNELRETRYHOTIMERLEN",
    t1."CHANNELRETRYTIMERLEN",
    t1."LOGICRNCID",
    t1."PARKINGRELTIMER",
    t1."RABMODIFYTIMERLEN",
    t1."ZERORATEUPFAILTORELTIMERLEN"
FROM
huawei_nbi_umts."UCOIFTIMER" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ADAPRETRANPUNTIMER",
    t2."CHANNELRETRYHOTIMERLEN",
    t2."CHANNELRETRYTIMERLEN",
    NULL,
    t2."PARKINGRELTIMER",
    t2."RABMODIFYTIMERLEN",
    t2."ZERORATEUPFAILTORELTIMERLEN"
FROM
huawei_mml_umts."UCOIFTIMER" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCONNMODETIMER = ReplaceableObject(
    'huawei_cm_3g."UCONNMODETIMER"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."N302",
    t1."N304",
    t1."N308",
    t1."N312",
    t1."N313",
    t1."N315",
    t1."N381",
    t1."T302",
    t1."T304",
    t1."T305",
    t1."T307",
    t1."T308",
    t1."T309",
    t1."T312",
    t1."T313",
    t1."T314",
    t1."T315",
    t1."T316",
    t1."T323",
    t1."T381"
FROM
huawei_nbi_umts."UCONNMODETIMER" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."N302",
    t2."N304",
    t2."N308",
    t2."N312",
    t2."N313",
    t2."N315",
    t2."N381",
    t2."T302",
    t2."T304",
    t2."T305",
    t2."T307",
    t2."T308",
    t2."T309",
    t2."T312",
    t2."T313",
    t2."T314",
    t2."T315",
    t2."T316",
    t2."T323",
    t2."T381"
FROM
huawei_mml_umts."UCONNMODETIMER" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UCORRMALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UCORRMALGOSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CFGSWITCH",
    t1."CMCFSWITCH",
    t1."CMPSWITCH",
    t1."CMPSWITCH2",
    t1."CSSWITCH",
    t1."DRASWITCH",
    t1."DRASWITCH2",
    t1."DRSWITCH",
    t1."HOSWITCH",
    t1."HOSWITCH1",
    t1."LOGICRNCID",
    t1."MAPSWITCH",
    t1."PCSWITCH",
    t1."PSSWITCH",
    t1."RESERVEDSWITCH0",
    t1."RESERVEDSWITCH1",
    t1."RESERVEDU32PARA0",
    t1."RESERVEDU8PARA0",
    t1."RESERVEDU8PARA1",
    t1."SRNSRSWITCH"
FROM
huawei_nbi_umts."UCORRMALGOSWITCH" t1

"""
)

UCORRMPARA = ReplaceableObject(
    'huawei_cm_3g."UCORRMPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."PERFENHANCESWITCH",
    t1."PERFENHANCESWITCH1",
    t1."PERFENHANCESWITCH2",
    t1."PERFENHANCESWITCH3",
    t1."PERFENHANCESWITCH4",
    t1."PERFENHANCESWITCH5",
    t1."RESERVEDSWITCH1"
FROM
huawei_nbi_umts."UCORRMPARA" t1

"""
)

UCSVOICEPPC = ReplaceableObject(
    'huawei_cm_3g."UCSVOICEPPC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."VOICEPPCSWITCH"
FROM
huawei_nbi_umts."UCSVOICEPPC" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID",
    t2."VOICEPPCSWITCH"
FROM
huawei_gexport_wcdma."UCSVOICEPPC_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID",
    t3."VOICEPPCSWITCH"
FROM
huawei_gexport_wcdma."UCSVOICEPPC_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."VOICEPPCSWITCH"
FROM
huawei_mml_umts."UCSVOICEPPC" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UCTRLPLNSHAREPARA = ReplaceableObject(
    'huawei_cm_3g."UCTRLPLNSHAREPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CTRLPLNSHARINGOUTOFFSET",
    t1."CTRLPLNSHARINGOUTTHD"
FROM
huawei_nbi_umts."UCTRLPLNSHAREPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CTRLPLNSHARINGOUTOFFSET",
    t2."CTRLPLNSHARINGOUTTHD"
FROM
huawei_mml_umts."UCTRLPLNSHAREPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UDCCC = ReplaceableObject(
    'huawei_cm_3g."UDCCC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BASECOVERD2E6ATHD",
    t1."BASECOVERD2E6BTHD",
    t1."BEPWRMARGIN",
    t1."CHANNELRETRYPENALTYNUM",
    t1."COMBPWRMARGIN",
    t1."DCCCSTG",
    t1."DCCCUPPENALTYLEN",
    t1."DCHTHROUMEASPERIOD",
    t1."DLDCCCRATETHD",
    t1."DLFULLCVRRATE",
    t1."DLMIDRATECALC",
    t1."DLMIDRATETHD",
    t1."DLRATEDNADJLEVEL",
    t1."DLRATEUPADJLEVEL",
    t1."E2DTHROU4BTHD",
    t1."FAILTIMETH",
    t1."HSUPABESHORATETHD",
    t1."HSUPADCCCSTG",
    t1."LITTLERATETHD",
    t1."LOGICRNCID",
    t1."MONITIMELEN",
    t1."ULDCCCRATETHD",
    t1."ULFULLCVRRATE",
    t1."ULMIDRATECALC",
    t1."ULMIDRATETHD",
    t1."ULRATEDNADJLEVEL",
    t1."ULRATEUPADJLEVEL"
FROM
huawei_nbi_umts."UDCCC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BASECOVERD2E6ATHD",
    t2."BASECOVERD2E6BTHD",
    t2."BEPWRMARGIN",
    t2."CHANNELRETRYPENALTYNUM",
    t2."COMBPWRMARGIN",
    t2."DCCCSTG",
    t2."DCCCUPPENALTYLEN",
    t2."DCHTHROUMEASPERIOD",
    t2."DLDCCCRATETHD",
    t2."DLFULLCVRRATE",
    t2."DLMIDRATECALC",
    t2."DLMIDRATETHD",
    t2."DLRATEDNADJLEVEL",
    t2."DLRATEUPADJLEVEL",
    t2."E2DTHROU4BTHD",
    t2."FAILTIMETH",
    t2."HSUPABESHORATETHD",
    t2."HSUPADCCCSTG",
    t2."LITTLERATETHD",
    NULL,
    t2."MONITIMELEN",
    t2."ULDCCCRATETHD",
    t2."ULFULLCVRRATE",
    t2."ULMIDRATECALC",
    t2."ULMIDRATETHD",
    t2."ULRATEDNADJLEVEL",
    t2."ULRATEUPADJLEVEL"
FROM
huawei_mml_umts."UDCCC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UDISTANCEREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UDISTANCEREDIRECTION"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DELAYTHS",
    t1."INTERFREQREDIRSWITCH",
    t1."LOGICRNCID",
    t1."REDIRFACTOROFLDR",
    t1."REDIRFACTOROFNORM",
    t1."REDIRSWITCH"
FROM
huawei_nbi_umts."UDISTANCEREDIRECTION" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."INTERFREQREDIRSWITCH",
    NULL,
    NULL,
    NULL,
    t2."REDIRSWITCH"
FROM
huawei_mml_umts."UDISTANCEREDIRECTION" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UDPUCFGDATA = ReplaceableObject(
    'huawei_cm_3g."UDPUCFGDATA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLCOUNTERSMEASOBJCTRLSWITCH",
    t1."EDCHIUBCONGCHECKSWITCH",
    t1."HSUPAIURCONGCTRLSWITCH",
    t1."HSUPATNLSWITCH",
    t1."IUBFPTWAITNODESYNCRSP",
    t1."IUBFPTWAITTRCHSYNCRSP",
    t1."IURFPTWAITNODESYNCRSP",
    t1."IURFPTWAITTRCHSYNCRSP",
    t1."LOWSIGNALPAGINGSWITCH",
    t1."MACCPAGEREPEATTIMES",
    t1."PAGINGSWITCH",
    t1."TPESWITCH",
    t1."WBAMRNOISECORRECTSWITCH"
FROM
huawei_nbi_umts."UDPUCFGDATA" t1

"""
)

UDRD = ReplaceableObject(
    'huawei_cm_3g."UDRD"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BASEDONMEASHRETRYDRDSWITCH",
    t1."BASEDUELOCDRDREMAINTHD",
    t1."BASEDUELOCDRDSWITCH",
    t1."CODEBALANCINGDRDCODERATETHD",
    t1."CODEBALANCINGDRDMINSFTHD",
    t1."CODEBALANCINGDRDSWITCH",
    t1."COMACROMICROIFREDIRSWITCH",
    t1."CONNECTFAILRRCREDIRSWITCH",
    t1."DELTACODEOCCUPIEDRATE",
    t1."DLSFTHDFORRRCDRDPRECAC",
    t1."DPGDRDSWITCH",
    t1."DRMAXGSMNUM",
    t1."HRTSERVICEDIFFDRDSWITCH",
    t1."HSDPALOADDRDOPTSWITCH",
    t1."HSPAPLUSSATISSWITCH",
    t1."LDBDRDCHOICE",
    t1."LDBDRDLOADREMAINTHDDCH",
    t1."LDBDRDLOADREMAINTHDHSDPA",
    t1."LDBDRDOFFSETDCH",
    t1."LDBDRDOFFSETHSDPA",
    t1."LDBDRDSWITCHDCH",
    t1."LDBDRDSWITCHHSDPA",
    t1."LDBDRDTOTALPWRPROTHD",
    t1."LOGICRNCID",
    t1."POWLOADDRDOPTSWITCH",
    t1."PWRTHDFORRRCDRDPRECAC",
    t1."REDIRBANDIND",
    t1."SECCELLLDBDRDCHOICE",
    t1."SECCELLREFBHFLAGSWITCH",
    t1."SERVICEDIFFDRDSWITCH",
    t1."TRAFFTYPEFORBASEDUELOC",
    t1."UELOCBASEDDRDFORC2DSWITCH",
    t1."ULCETHDFORRRCDRDPRECAC",
    t1."ULLDBDRDLOADREMAINTHDDCHSDPA",
    t1."ULLDBDRDOFFSETDCHSDPA",
    t1."ULLDBDRDSWITCHDCHSDPA"
FROM
huawei_nbi_umts."UDRD" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BASEDONMEASHRETRYDRDSWITCH",
    t2."BASEDUELOCDRDREMAINTHD",
    t2."BASEDUELOCDRDSWITCH",
    t2."CODEBALANCINGDRDCODERATETHD",
    t2."CODEBALANCINGDRDMINSFTHD",
    t2."CODEBALANCINGDRDSWITCH",
    t2."COMACROMICROIFREDIRSWITCH",
    t2."CONNECTFAILRRCREDIRSWITCH",
    t2."DELTACODEOCCUPIEDRATE",
    t2."DLSFTHDFORRRCDRDPRECAC",
    t2."DPGDRDSWITCH",
    t2."DRMAXGSMNUM",
    t2."HRTSERVICEDIFFDRDSWITCH",
    t2."HSDPALOADDRDOPTSWITCH",
    t2."HSPAPLUSSATISSWITCH",
    t2."LDBDRDCHOICE",
    t2."LDBDRDLOADREMAINTHDDCH",
    t2."LDBDRDLOADREMAINTHDHSDPA",
    t2."LDBDRDOFFSETDCH",
    t2."LDBDRDOFFSETHSDPA",
    t2."LDBDRDSWITCHDCH",
    t2."LDBDRDSWITCHHSDPA",
    t2."LDBDRDTOTALPWRPROTHD",
    NULL,
    t2."POWLOADDRDOPTSWITCH",
    t2."PWRTHDFORRRCDRDPRECAC",
    t2."REDIRBANDIND",
    t2."SECCELLLDBDRDCHOICE",
    t2."SECCELLREFBHFLAGSWITCH",
    t2."SERVICEDIFFDRDSWITCH",
    NULL,
    t2."UELOCBASEDDRDFORC2DSWITCH",
    t2."ULCETHDFORRRCDRDPRECAC",
    t2."ULLDBDRDLOADREMAINTHDDCHSDPA",
    t2."ULLDBDRDOFFSETDCHSDPA",
    t2."ULLDBDRDSWITCHDCHSDPA"
FROM
huawei_mml_umts."UDRD" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UDRDMIMO = ReplaceableObject(
    'huawei_cm_3g."UDRDMIMO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LEGACYHDRDSWITCHOFSTTD",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UDRDMIMO" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."LEGACYHDRDSWITCHOFSTTD",
    NULL
FROM
huawei_mml_umts."UDRDMIMO" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UDSACAUTOALGO = ReplaceableObject(
    'huawei_cm_3g."UDSACAUTOALGO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACINTERVALOFCELLS",
    t1."ACRANGE",
    t1."ACRSTRCTINTERVALLEN",
    t1."CSRESTRICTION",
    t1."DSACAUTOSWITCH",
    t1."LOGICRNCID",
    t1."NUMBEROFACS",
    t1."PSRESTRICTION"
FROM
huawei_nbi_umts."UDSACAUTOALGO" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."DSACAUTOSWITCH",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UDSACAUTOALGO" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UDTXDRXPARA = ReplaceableObject(
    'huawei_cm_3g."UDTXDRXPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CQIDTXTIMER",
    t1."CQIFBCKININDTXDRXMODE",
    t1."DPCCHBURST1",
    t1."DPCCHBURST2",
    t1."DRXCYCLE",
    t1."DRXGRANTMONITORING",
    t1."DRXVALID",
    t1."DTXCYCLE1",
    t1."DTXCYCLE2",
    t1."DTXLONGPREAMBLE",
    t1."DTXVALID",
    t1."EDCHTTITYPE",
    t1."INACTTHSFORCYCLE2",
    t1."INACTTHSFORDRXCYCLE",
    t1."INACTTHSFORGRANTMONITORING",
    t1."LOGICRNCID",
    t1."MACDTXCYCLE",
    t1."MACINACTIVETHRESHOLD",
    t1."TRAFFICCLASS"
FROM
huawei_nbi_umts."UDTXDRXPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CQIDTXTIMER",
    t2."CQIFBCKININDTXDRXMODE",
    t2."DPCCHBURST1",
    t2."DPCCHBURST2",
    t2."DRXCYCLE",
    t2."DRXGRANTMONITORING",
    t2."DRXVALID",
    t2."DTXCYCLE1",
    t2."DTXCYCLE2",
    t2."DTXLONGPREAMBLE",
    t2."DTXVALID",
    t2."EDCHTTITYPE",
    t2."INACTTHSFORCYCLE2",
    t2."INACTTHSFORDRXCYCLE",
    t2."INACTTHSFORGRANTMONITORING",
    NULL,
    t2."MACDTXCYCLE",
    t2."MACINACTIVETHRESHOLD",
    t2."TRAFFICCLASS"
FROM
huawei_mml_umts."UDTXDRXPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UEDCHRATEADJUSTSET = ReplaceableObject(
    'huawei_cm_3g."UEDCHRATEADJUSTSET"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."EDCHRATEADJUSTSET",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UEDCHRATEADJUSTSET" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UEDCHRATEADJUSTSET" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UEDCHTTIRECFG = ReplaceableObject(
    'huawei_cm_3g."UEDCHTTIRECFG"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AMREVENTATHD",
    t1."AMRTHD6A1",
    t1."AMRTHD6B1",
    t1."BETHD6A1",
    t1."BETHD6A2",
    t1."BETHD6B1",
    t1."BETHD6B2",
    t1."LOGICRNCID",
    t1."LOWRATIOFOR2MSTO10MS",
    t1."PRIORITYOPT",
    t1."RATIOFOR10MSTO2MS",
    t1."RESOURCEOPTION",
    t1."TTIEDCHTHROUMEASPERIOD",
    t1."UPRATIOFOR2MSTO10MSBASECE",
    t1."UPRATIOFOR2MSTO10MSBASERTWP",
    t1."VOICEPMRMCSWITCH",
    t1."VOIPEVENTATHD",
    t1."VOIPTHD6A1",
    t1."VOIPTHD6B1",
    t1."WAMREVENTATHD",
    t1."WAMRTHD6A1",
    t1."WAMRTHD6B1"
FROM
huawei_nbi_umts."UEDCHTTIRECFG" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AMREVENTATHD",
    t2."AMRTHD6A1",
    t2."AMRTHD6B1",
    t2."BETHD6A1",
    t2."BETHD6A2",
    t2."BETHD6B1",
    t2."BETHD6B2",
    NULL,
    t2."LOWRATIOFOR2MSTO10MS",
    t2."PRIORITYOPT",
    t2."RATIOFOR10MSTO2MS",
    NULL,
    t2."TTIEDCHTHROUMEASPERIOD",
    t2."UPRATIOFOR2MSTO10MSBASECE",
    t2."UPRATIOFOR2MSTO10MSBASERTWP",
    t2."VOICEPMRMCSWITCH",
    t2."VOIPEVENTATHD",
    t2."VOIPTHD6A1",
    t2."VOIPTHD6B1",
    t2."WAMREVENTATHD",
    t2."WAMRTHD6A1",
    t2."WAMRTHD6B1"
FROM
huawei_mml_umts."UEDCHTTIRECFG" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UEVQIPARA = ReplaceableObject(
    'huawei_cm_3g."UEVQIPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UEVQIPARA" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UEVQIPARA_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UEVQIPARA_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL
FROM
huawei_mml_umts."UEVQIPARA" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UEXT2GCELL = ReplaceableObject(
    'huawei_cm_3g."UEXT2GCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BANDIND",
    t1."BCC",
    t1."BCCHARFCN",
    t1."CFGRACIND",
    t1."CID",
    t1."CIO",
    t1."CNOPGRPINDEX",
    t1."GSMCELLINDEX",
    t1."GSMCELLNAME",
    t1."LAC",
    t1."LDPRDRPRTSWITCH",
    t1."LOGICRNCID",
    t1."MCC",
    t1."MNC",
    t1."NBSCINDEX",
    t1."NCC",
    t1."NCMODE",
    t1."RAC",
    t1."RATCELLTYPE",
    t1."SUPPPSHOFLAG",
    t1."SUPPRIMFLAG",
    t1."USEOFHCS"
FROM
huawei_nbi_umts."UEXT2GCELL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BANDIND",
    t2."BCC",
    t2."BCCHARFCN",
    t2."CFGRACIND",
    hex_to_int(REPLACE(t2."CID",'H''',''))::varchar as "CID",
    t2."CIO",
    t2."CNOPGRPINDEX",
    t2."GSMCELLINDEX",
    TRIM(t2."GSMCELLNAME") AS "GSMCELLNAME",
    hex_to_int(REPLACE(t2."LAC",'H''',''))::varchar as "LAC",
    t2."LDPRDRPRTSWITCH",
    NULL,
    t2."MCC",
    t2."MNC",
    t2."NBSCINDEX",
    t2."NCC",
    t2."NCMODE",
    hex_to_int(REPLACE(t2."RAC",'H''',''))::varchar as "RAC",
    t2."RATCELLTYPE",
    t2."SUPPPSHOFLAG",
    t2."SUPPRIMFLAG",
    t2."USEOFHCS"
FROM
huawei_mml_umts."UEXT2GCELL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UEXT3GCELL = ReplaceableObject(
    'huawei_cm_3g."UEXT3GCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."APFLAG",
    t1."BANDIND",
    t1."CELLCAPCONTAINERFDD",
    t1."CELLHOSTTYPE",
    t1."CELLID",
    t1."CELLNAME",
    t1."CFGRACIND",
    t1."CIO",
    t1."CNOPGRPINDEX",
    t1."CP1SUPIND",
    t1."DIVMODFORDCHSDPA",
    t1."DPCHDIVMODFORMIMO",
    t1."DPCHDIVMODFOROTHER",
    t1."EFACHSUPIND",
    t1."FDPCHDIVMODFORMIMO",
    t1."FDPCHDIVMODFOROTHER",
    t1."HARQPREACAP",
    t1."LAC",
    t1."LOGICRNCID",
    t1."MAXALLOWEDULTXPOWERIND",
    t1."NRNCID",
    t1."OVERLAYMOBILITYFLAG",
    t1."PSCRAMBCODE",
    t1."QQUALMININD",
    t1."QRXLEVMININD",
    t1."RAC",
    t1."STTDSUPIND",
    t1."SUPPDPCMODECHGFLAG",
    t1."TXDIVERSITYIND",
    t1."UARFCNDOWNLINK",
    t1."UARFCNUPLINKIND",
    t1."USEOFHCS",
    t1."VPLIMITIND",
    t1."UARFCNUPLINK",
    t1."MAXALLOWEDULTXPOWER",
    t1."QQUALMIN",
    t1."QRXLEVMIN",
    t1."QRXLEVMINEXTSUP"
FROM
huawei_nbi_umts."UEXT3GCELL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."APFLAG",
    t2."BANDIND",
    NULL,
    t2."CELLHOSTTYPE",
    t2."CELLID",
    TRIM(t2."CELLNAME") AS "CELLNAME",
    t2."CFGRACIND",
    t2."CIO",
    t2."CNOPGRPINDEX",
    t2."CP1SUPIND",
    t2."DIVMODFORDCHSDPA",
    t2."DPCHDIVMODFORMIMO",
    t2."DPCHDIVMODFOROTHER",
    t2."EFACHSUPIND",
    t2."FDPCHDIVMODFORMIMO",
    t2."FDPCHDIVMODFOROTHER",
    t2."HARQPREACAP",
    hex_to_int(REPLACE(t2."LAC",'H''',''))::varchar as "LAC",
    NULL,
    t2."MAXALLOWEDULTXPOWERIND",
    t2."NRNCID",
    t2."OVERLAYMOBILITYFLAG",
    t2."PSCRAMBCODE",
    t2."QQUALMININD",
    t2."QRXLEVMININD",
    hex_to_int(REPLACE(t2."RAC",'H''',''))::varchar as "RAC",
    t2."STTDSUPIND",
    t2."SUPPDPCMODECHGFLAG",
    t2."TXDIVERSITYIND",
    t2."UARFCNDOWNLINK",
    t2."UARFCNUPLINKIND",
    t2."USEOFHCS",
    t2."VPLIMITIND",
    t2."UARFCNUPLINK",
    t2."MAXALLOWEDULTXPOWER",
    t2."QQUALMIN",
    t2."QRXLEVMIN",
    t2."QRXLEVMINEXTSUP"
FROM
huawei_mml_umts."UEXT3GCELL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UEXT3GCELLINTRAFREQHO = ReplaceableObject(
    'huawei_cm_3g."UEXT3GCELLINTRAFREQHO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLINDHORSCP1FTHRESHOLD",
    t1."CELLID",
    t1."HYSTFOR1A",
    t1."HYSTFOR1B",
    t1."HYSTFOR1C",
    t1."HYSTFOR1D",
    t1."HYSTFOR1F",
    t1."HYSTFOR1J",
    t1."INTRAABLTHDFOR1FECNO",
    t1."INTRAFREQFILTERCOEF",
    t1."INTRAFREQMEASQUANTITY",
    t1."INTRARELTHDFOR1ACSNVP",
    t1."INTRARELTHDFOR1ACSVP",
    t1."INTRARELTHDFOR1APS",
    t1."INTRARELTHDFOR1BCSNVP",
    t1."INTRARELTHDFOR1BCSVP",
    t1."INTRARELTHDFOR1BPS",
    t1."LOGICRNCID",
    t1."MAXCELLINACTIVESET",
    t1."NRNCID",
    t1."PERIODMRREPORTNUMFOR1A",
    t1."PERIODMRREPORTNUMFOR1C",
    t1."PERIODMRREPORTNUMFOR1J",
    t1."REPORTINTERVALFOR1A",
    t1."REPORTINTERVALFOR1C",
    t1."REPORTINTERVALFOR1J",
    t1."SHOQUALMIN",
    t1."TRIGTIME1A",
    t1."TRIGTIME1B",
    t1."TRIGTIME1C",
    t1."TRIGTIME1D",
    t1."TRIGTIME1F",
    t1."TRIGTIME1J",
    t1."WEIGHT"
FROM
huawei_nbi_umts."UEXT3GCELLINTRAFREQHO" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."BLINDHORSCP1FTHRESHOLD",
    t2."CELLID",
    t2."HYSTFOR1A",
    t2."HYSTFOR1B",
    t2."HYSTFOR1C",
    t2."HYSTFOR1D",
    t2."HYSTFOR1F",
    t2."HYSTFOR1J",
    t2."INTRAABLTHDFOR1FECNO",
    t2."INTRAFREQFILTERCOEF",
    t2."INTRAFREQMEASQUANTITY",
    t2."INTRARELTHDFOR1ACSNVP",
    t2."INTRARELTHDFOR1ACSVP",
    t2."INTRARELTHDFOR1APS",
    t2."INTRARELTHDFOR1BCSNVP",
    t2."INTRARELTHDFOR1BCSVP",
    t2."INTRARELTHDFOR1BPS",
    t2."LOGICRNCID",
    t2."MAXCELLINACTIVESET",
    t2."NRNCID",
    t2."PERIODMRREPORTNUMFOR1A",
    t2."PERIODMRREPORTNUMFOR1C",
    t2."PERIODMRREPORTNUMFOR1J",
    t2."REPORTINTERVALFOR1A",
    t2."REPORTINTERVALFOR1C",
    t2."REPORTINTERVALFOR1J",
    t2."SHOQUALMIN",
    t2."TRIGTIME1A",
    t2."TRIGTIME1B",
    t2."TRIGTIME1C",
    t2."TRIGTIME1D",
    t2."TRIGTIME1F",
    t2."TRIGTIME1J",
    t2."WEIGHT"
FROM
huawei_gexport_wcdma."UEXT3GCELLINTRAFREQHO_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."BLINDHORSCP1FTHRESHOLD",
    t3."CELLID",
    t3."HYSTFOR1A",
    t3."HYSTFOR1B",
    t3."HYSTFOR1C",
    t3."HYSTFOR1D",
    t3."HYSTFOR1F",
    t3."HYSTFOR1J",
    t3."INTRAABLTHDFOR1FECNO",
    t3."INTRAFREQFILTERCOEF",
    t3."INTRAFREQMEASQUANTITY",
    t3."INTRARELTHDFOR1ACSNVP",
    t3."INTRARELTHDFOR1ACSVP",
    t3."INTRARELTHDFOR1APS",
    t3."INTRARELTHDFOR1BCSNVP",
    t3."INTRARELTHDFOR1BCSVP",
    t3."INTRARELTHDFOR1BPS",
    t3."LOGICRNCID",
    t3."MAXCELLINACTIVESET",
    t3."NRNCID",
    t3."PERIODMRREPORTNUMFOR1A",
    t3."PERIODMRREPORTNUMFOR1C",
    t3."PERIODMRREPORTNUMFOR1J",
    t3."REPORTINTERVALFOR1A",
    t3."REPORTINTERVALFOR1C",
    t3."REPORTINTERVALFOR1J",
    t3."SHOQUALMIN",
    t3."TRIGTIME1A",
    t3."TRIGTIME1B",
    t3."TRIGTIME1C",
    t3."TRIGTIME1D",
    t3."TRIGTIME1F",
    t3."TRIGTIME1J",
    t3."WEIGHT"
FROM
huawei_gexport_wcdma."UEXT3GCELLINTRAFREQHO_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."BLINDHORSCP1FTHRESHOLD",
    t4."CELLID",
    t4."HYSTFOR1A",
    t4."HYSTFOR1B",
    t4."HYSTFOR1C",
    t4."HYSTFOR1D",
    t4."HYSTFOR1F",
    t4."HYSTFOR1J",
    t4."INTRAABLTHDFOR1FECNO",
    t4."INTRAFREQFILTERCOEF",
    t4."INTRAFREQMEASQUANTITY",
    t4."INTRARELTHDFOR1ACSNVP",
    t4."INTRARELTHDFOR1ACSVP",
    t4."INTRARELTHDFOR1APS",
    t4."INTRARELTHDFOR1BCSNVP",
    t4."INTRARELTHDFOR1BCSVP",
    t4."INTRARELTHDFOR1BPS",
    NULL,
    t4."MAXCELLINACTIVESET",
    t4."NRNCID",
    t4."PERIODMRREPORTNUMFOR1A",
    t4."PERIODMRREPORTNUMFOR1C",
    t4."PERIODMRREPORTNUMFOR1J",
    t4."REPORTINTERVALFOR1A",
    t4."REPORTINTERVALFOR1C",
    t4."REPORTINTERVALFOR1J",
    t4."SHOQUALMIN",
    t4."TRIGTIME1A",
    t4."TRIGTIME1B",
    t4."TRIGTIME1C",
    t4."TRIGTIME1D",
    t4."TRIGTIME1F",
    t4."TRIGTIME1J",
    t4."WEIGHT"
FROM
huawei_mml_umts."UEXT3GCELLINTRAFREQHO" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UFACH = ReplaceableObject(
    'huawei_cm_3g."UFACH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CHCODINGTYPE",
    t1."CODINGRATE",
    t1."LOGICRNCID",
    t1."MAXCMCHPI",
    t1."MAXFACHPOWER",
    t1."MINCMCHPI",
    t1."OFFSETFACHPOWER",
    t1."PHYCHID",
    t1."RATEMATCHINGATTR",
    t1."SIGRBIND",
    t1."TOAWE",
    t1."TOAWS",
    t1."TRCHID"
FROM
huawei_nbi_umts."UFACH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    t2."CHCODINGTYPE",
    t2."CODINGRATE",
    NULL,
    t2."MAXCMCHPI",
    t2."MAXFACHPOWER",
    t2."MINCMCHPI",
    t2."OFFSETFACHPOWER",
    t2."PHYCHID",
    t2."RATEMATCHINGATTR",
    t2."SIGRBIND",
    t2."TOAWE",
    t2."TOAWS",
    t2."TRCHID"
FROM
huawei_mml_umts."UFACH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UFACHBANDWIDTH = ReplaceableObject(
    'huawei_cm_3g."UFACHBANDWIDTH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BANDWIDTHFORFACH",
    t1."LOGICRNCID",
    t1."TRAFFICCLASS",
    t1."USERPRIORITY"
FROM
huawei_nbi_umts."UFACHBANDWIDTH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BANDWIDTHFORFACH",
    NULL,
    t2."TRAFFICCLASS",
    t2."USERPRIORITY"
FROM
huawei_mml_umts."UFACHBANDWIDTH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UFACHDYNTFS = ReplaceableObject(
    'huawei_cm_3g."UFACHDYNTFS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."RLCSIZE",
    t1."TBNUMBER1",
    t1."TBNUMBER2",
    t1."TBNUMBER3",
    t1."TFSNUMBER",
    t1."TRCHID"
FROM
huawei_nbi_umts."UFACHDYNTFS" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."RLCSIZE",
    t2."TBNUMBER1",
    t2."TBNUMBER2",
    t2."TBNUMBER3",
    t2."TFSNUMBER",
    t2."TRCHID"
FROM
huawei_mml_umts."UFACHDYNTFS" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UFACHLOCH = ReplaceableObject(
    'huawei_cm_3g."UFACHLOCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."TRCHID"
FROM
huawei_nbi_umts."UFACHLOCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."TRCHID"
FROM
huawei_mml_umts."UFACHLOCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UFDPCHPARA = ReplaceableObject(
    'huawei_cm_3g."UFDPCHPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."FDPCHPO2",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UFDPCHPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."FDPCHPO2",
    NULL
FROM
huawei_mml_umts."UFDPCHPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UFDPCHRLPWR = ReplaceableObject(
    'huawei_cm_3g."UFDPCHRLPWR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."FDPCHMAXREFPWR",
    t1."FDPCHMINREFPWR",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UFDPCHRLPWR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."FDPCHMAXREFPWR",
    t2."FDPCHMINREFPWR",
    NULL
FROM
huawei_mml_umts."UFDPCHRLPWR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UFRC = ReplaceableObject(
    'huawei_cm_3g."UFRC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACTTIMEADJUSTQUALTHD",
    t1."BEHSUPA2MSTTIRATETHS",
    t1."CSFBSRBRATE",
    t1."CSVOICEHSPADLRELDELAY",
    t1."CSVOICEHSPAULRELDELAY",
    t1."CSVOICEHSUPATTI",
    t1."DCMIMOOR4CHSDPASWITCH",
    t1."DEFAULTCONSTANTVALUE",
    t1."DEFAULTSPIWEIGHT",
    t1."DLBEH2DINITIALRATE",
    t1."DLBETRAFFINITBITRATE",
    t1."DLDCHBEC2DBITRATEFORAMR",
    t1."DLDPCHPLSAVEMODE",
    t1."DLSAVECODERESOURCESWITCH",
    t1."DLSTRGBR",
    t1."DPCCHSLOTFMTFORHSPA",
    t1."DPCMODE",
    t1."DRXCYCLELENCOEF",
    t1."DTXDRXENABLINGDELAY",
    t1."ECN0EFFECTTIME",
    t1."ECN0THDFORBASECOVERE2D",
    t1."ECN0THS",
    t1."ECN0THSFOR2MSTO10MS",
    t1."EPCHDLEL2MAXRLCPDUSIZE",
    t1."ERACHMAXPDUSIZEFOREUL2",
    t1."ERACHMINPDUSIZEFOREUL2",
    t1."FDDTPCDLSTEPSIZE",
    t1."HSUPA10MSSCHPRDFORGRANT",
    t1."HSUPA10MSSCHPRDFORNONGRANT",
    t1."HSUPA2MSSCHPRDFORGRANT",
    t1."HSUPA2MSSCHPRDFORNONGRANT",
    t1."HSUPAINITIALRATE",
    t1."IMSBEARENHANCEDSWITCH",
    t1."L2USRVCCEMERCALLARP",
    t1."LOGICRNCID",
    t1."MACPDUMAXSIZEFORDLL2ENHANCE",
    t1."MACPDUMAXSIZEFOREFACH",
    t1."MBRTHDFORDLHIGHRATE",
    t1."MIMO64QAMORDCHSDPASWITCH",
    t1."MIMOOR64QAMSWITCH",
    t1."NRTINITRATEFORL2U",
    t1."PTTARPPREEMPTCAP",
    t1."PTTARPPREEMPTVULN",
    t1."PTTARPPRIORITYLEVEL",
    t1."PTTARPQUEUINGALLOWED",
    t1."PTTDRXCYCLELENCOEF",
    t1."PTTHSUPATTI",
    t1."PWRCTRLALG",
    t1."RETRYCAPABILITY",
    t1."RLCPDUMAXSIZEFORULL2ENHANCE",
    t1."RLCPDUMINSIZEFORULL2ENHANCE",
    t1."SECCELLHUSERNUMTHD",
    t1."SECCELLTCPTHD",
    t1."STREAMHSUPA2MSTTIRATETHS",
    t1."SYSINBEHSDPATODCHTHD",
    t1."SYSINBEHSUPATODCHTHD",
    t1."ULBETRAFFINITBITRATE",
    t1."ULDCHBEC2DBITRATEFORAMR",
    t1."ULIMSTRANSMODEONHSUPA",
    t1."ULPTTTRANSMODEONHSUPA",
    t1."ULSRBTRANSMODEONHSUPA",
    t1."ULSTRGBR",
    t1."ULSTRTRANSMODEONHSUPA",
    t1."ULTPCSTEPSIZE",
    t1."ULTRAFLASHCSFBSRBRATE",
    t1."VOIPHSUPATTI"
FROM
huawei_nbi_umts."UFRC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ACTTIMEADJUSTQUALTHD",
    t2."BEHSUPA2MSTTIRATETHS",
    t2."CSFBSRBRATE",
    t2."CSVOICEHSPADLRELDELAY",
    t2."CSVOICEHSPAULRELDELAY",
    t2."CSVOICEHSUPATTI",
    t2."DCMIMOOR4CHSDPASWITCH",
    t2."DEFAULTCONSTANTVALUE",
    t2."DEFAULTSPIWEIGHT",
    t2."DLBEH2DINITIALRATE",
    t2."DLBETRAFFINITBITRATE",
    t2."DLDCHBEC2DBITRATEFORAMR",
    t2."DLDPCHPLSAVEMODE",
    t2."DLSAVECODERESOURCESWITCH",
    t2."DLSTRGBR",
    t2."DPCCHSLOTFMTFORHSPA",
    t2."DPCMODE",
    t2."DRXCYCLELENCOEF",
    t2."DTXDRXENABLINGDELAY",
    t2."ECN0EFFECTTIME",
    t2."ECN0THDFORBASECOVERE2D",
    t2."ECN0THS",
    t2."ECN0THSFOR2MSTO10MS",
    t2."EPCHDLEL2MAXRLCPDUSIZE",
    t2."ERACHMAXPDUSIZEFOREUL2",
    t2."ERACHMINPDUSIZEFOREUL2",
    t2."FDDTPCDLSTEPSIZE",
    t2."HSUPA10MSSCHPRDFORGRANT",
    t2."HSUPA10MSSCHPRDFORNONGRANT",
    t2."HSUPA2MSSCHPRDFORGRANT",
    t2."HSUPA2MSSCHPRDFORNONGRANT",
    t2."HSUPAINITIALRATE",
    t2."IMSBEARENHANCEDSWITCH",
    t2."L2USRVCCEMERCALLARP",
    NULL,
    t2."MACPDUMAXSIZEFORDLL2ENHANCE",
    t2."MACPDUMAXSIZEFOREFACH",
    t2."MBRTHDFORDLHIGHRATE",
    t2."MIMO64QAMORDCHSDPASWITCH",
    t2."MIMOOR64QAMSWITCH",
    t2."NRTINITRATEFORL2U",
    t2."PTTARPPREEMPTCAP",
    t2."PTTARPPREEMPTVULN",
    t2."PTTARPPRIORITYLEVEL",
    t2."PTTARPQUEUINGALLOWED",
    t2."PTTDRXCYCLELENCOEF",
    t2."PTTHSUPATTI",
    t2."PWRCTRLALG",
    NULL,
    t2."RLCPDUMAXSIZEFORULL2ENHANCE",
    t2."RLCPDUMINSIZEFORULL2ENHANCE",
    t2."SECCELLHUSERNUMTHD",
    t2."SECCELLTCPTHD",
    t2."STREAMHSUPA2MSTTIRATETHS",
    t2."SYSINBEHSDPATODCHTHD",
    t2."SYSINBEHSUPATODCHTHD",
    t2."ULBETRAFFINITBITRATE",
    t2."ULDCHBEC2DBITRATEFORAMR",
    t2."ULIMSTRANSMODEONHSUPA",
    t2."ULPTTTRANSMODEONHSUPA",
    t2."ULSRBTRANSMODEONHSUPA",
    t2."ULSTRGBR",
    t2."ULSTRTRANSMODEONHSUPA",
    t2."ULTPCSTEPSIZE",
    t2."ULTRAFLASHCSFBSRBRATE",
    t2."VOIPHSUPATTI"
FROM
huawei_mml_umts."UFRC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UFRCCHLTYPEPARA = ReplaceableObject(
    'huawei_cm_3g."UFRCCHLTYPEPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CSVOICECHLTYPE",
    t1."CSVOICEDYNCHCONFDLPOWTHD",
    t1."CSVOICEDYNCHCONFUSERNUMTHD",
    t1."DLBETRAFFDECTHS",
    t1."DLBETRAFFTHSONHSDPA",
    t1."DLSTRTHSONHSDPA",
    t1."IMSCHLTYPE",
    t1."LOGICRNCID",
    t1."PTTCHLTYPE",
    t1."SRBCHLTYPE",
    t1."SRBCHLTYPERRCEFFECTFLAG",
    t1."ULBETRAFFDECTHS",
    t1."ULBETRAFFTHSONHSUPA",
    t1."ULSTRTHSONHSUPA",
    t1."VOIPCHLTYPE"
FROM
huawei_nbi_umts."UFRCCHLTYPEPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CSVOICECHLTYPE",
    t2."CSVOICEDYNCHCONFDLPOWTHD",
    t2."CSVOICEDYNCHCONFUSERNUMTHD",
    t2."DLBETRAFFDECTHS",
    t2."DLBETRAFFTHSONHSDPA",
    t2."DLSTRTHSONHSDPA",
    t2."IMSCHLTYPE",
    NULL,
    t2."PTTCHLTYPE",
    t2."SRBCHLTYPE",
    t2."SRBCHLTYPERRCEFFECTFLAG",
    t2."ULBETRAFFDECTHS",
    t2."ULBETRAFFTHSONHSUPA",
    t2."ULSTRTHSONHSUPA",
    t2."VOIPCHLTYPE"
FROM
huawei_mml_umts."UFRCCHLTYPEPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UHCSHO = ReplaceableObject(
    'huawei_cm_3g."UHCSHO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."NFASTSPDEST",
    t1."NSLOWSPDEST",
    t1."TCYCLESLOW",
    t1."TFASTSPDEST",
    t1."TRELATELENGTH",
    t1."TSLOWSPDEST"
FROM
huawei_nbi_umts."UHCSHO" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."NFASTSPDEST",
    t2."NSLOWSPDEST",
    t2."TCYCLESLOW",
    t2."TFASTSPDEST",
    t2."TRELATELENGTH",
    t2."TSLOWSPDEST"
FROM
huawei_mml_umts."UHCSHO" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UHOCOMM = ReplaceableObject(
    'huawei_cm_3g."UHOCOMM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."COEXISTMEASTHDCHOICE",
    t1."CSHOPRIOMEASTIMERLEN",
    t1."DIVCTRLFIELD",
    t1."HSPATIMERLEN",
    t1."IFANTIPINGPANGTIMERLENGTH",
    t1."LOGICRNCID",
    t1."MACROMICRO1APREMEASSWITCH",
    t1."MAXEDCHCELLINACTIVESET",
    t1."PSHOPRIOMEASTIMERLEN",
    t1."SPECUSERCSTHD2DECN0",
    t1."SPECUSERCSTHD2DRSCP",
    t1."SPECUSERCSTHD2FECN0",
    t1."SPECUSERCSTHD2FRSCP",
    t1."SPECUSERHYSTFOR2D",
    t1."WEAKCOVHSPAQUALTHDS"
FROM
huawei_nbi_umts."UHOCOMM" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."COEXISTMEASTHDCHOICE",
    t2."CSHOPRIOMEASTIMERLEN",
    t2."DIVCTRLFIELD",
    t2."HSPATIMERLEN",
    t2."IFANTIPINGPANGTIMERLENGTH",
    NULL,
    t2."MACROMICRO1APREMEASSWITCH",
    t2."MAXEDCHCELLINACTIVESET",
    t2."PSHOPRIOMEASTIMERLEN",
    t2."SPECUSERCSTHD2DECN0",
    t2."SPECUSERCSTHD2DRSCP",
    t2."SPECUSERCSTHD2FECN0",
    t2."SPECUSERCSTHD2FRSCP",
    t2."SPECUSERHYSTFOR2D",
    t2."WEAKCOVHSPAQUALTHDS"
FROM
huawei_mml_umts."UHOCOMM" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UHSSCCHLESSOPPARA = ReplaceableObject(
    'huawei_cm_3g."UHSSCCHLESSOPPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ALIGNMODE",
    t1."HSPDCCHSECONDCODESUPP1",
    t1."HSPDCCHSECONDCODESUPP2",
    t1."HSPDCCHSECONDCODESUPP3",
    t1."HSPDCCHSECONDCODESUPP4",
    t1."LOGICRNCID",
    t1."TBINDEXNUM",
    t1."TBSIZEINDEX1",
    t1."TBSIZEINDEX2",
    t1."TBSIZEINDEX3",
    t1."TBSIZEINDEX4",
    t1."TRAFFICCLASS",
    t1."USEMACEHS"
FROM
huawei_nbi_umts."UHSSCCHLESSOPPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ALIGNMODE",
    t2."HSPDCCHSECONDCODESUPP1",
    t2."HSPDCCHSECONDCODESUPP2",
    t2."HSPDCCHSECONDCODESUPP3",
    t2."HSPDCCHSECONDCODESUPP4",
    NULL,
    t2."TBINDEXNUM",
    t2."TBSIZEINDEX1",
    t2."TBSIZEINDEX2",
    t2."TBSIZEINDEX3",
    t2."TBSIZEINDEX4",
    t2."TRAFFICCLASS",
    t2."USEMACEHS"
FROM
huawei_mml_umts."UHSSCCHLESSOPPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UIDLEMODETIMER = ReplaceableObject(
    'huawei_cm_3g."UIDLEMODETIMER"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."N300",
    t1."N312",
    t1."T300",
    t1."T312"
FROM
huawei_nbi_umts."UIDLEMODETIMER" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."N300",
    t2."N312",
    t2."T300",
    t2."T312"
FROM
huawei_mml_umts."UIDLEMODETIMER" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UINTERFREQHOCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERFREQHOCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."HHOECNOMIN",
    t1."HHORSCPMIN",
    t1."HYSTFOR2D",
    t1."HYSTFOR2F",
    t1."HYSTFORPRDINTERFREQ",
    t1."INTERFREQCSTHD2DECN0",
    t1."INTERFREQCSTHD2DRSCP",
    t1."INTERFREQCSTHD2FECN0",
    t1."INTERFREQCSTHD2FRSCP",
    t1."INTERFREQFILTERCOEF",
    t1."INTERFREQHO2DEVENTTYPE",
    t1."INTERFREQHTHD2DECN0",
    t1."INTERFREQHTHD2DRSCP",
    t1."INTERFREQHTHD2FECN0",
    t1."INTERFREQHTHD2FRSCP",
    t1."INTERFREQMCMODE",
    t1."INTERFREQMEASTIME",
    t1."INTERFREQR99PSTHD2DECN0",
    t1."INTERFREQR99PSTHD2DRSCP",
    t1."INTERFREQR99PSTHD2FECN0",
    t1."INTERFREQR99PSTHD2FRSCP",
    t1."INTERFREQREPORTMODE",
    t1."LOGICRNCID",
    t1."PRDREPORTINTERVAL",
    t1."TARGETFREQCSTHDECN0",
    t1."TARGETFREQCSTHDRSCP",
    t1."TARGETFREQHTHDECN0",
    t1."TARGETFREQHTHDRSCP",
    t1."TARGETFREQR99PSTHDECN0",
    t1."TARGETFREQR99PSTHDRSCP",
    t1."TIMETOINTERFREQHO",
    t1."TIMETOTRIG2D",
    t1."TIMETOTRIG2F",
    t1."TIMETOTRIGFORPRDINTERFREQ",
    t1."USEDFREQCSTHDECN0",
    t1."USEDFREQCSTHDRSCP",
    t1."USEDFREQHTHDECN0",
    t1."USEDFREQHTHDRSCP",
    t1."USEDFREQLOWERTHDECNO",
    t1."USEDFREQR99PSTHDECN0",
    t1."USEDFREQR99PSTHDRSCP",
    t1."USEDFREQUPPERTHDECNO",
    t1."WEIGHTFORUSEDFREQ"
FROM
huawei_nbi_umts."UINTERFREQHOCOV" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."HHOECNOMIN",
    t2."HHORSCPMIN",
    t2."HYSTFOR2D",
    t2."HYSTFOR2F",
    t2."HYSTFORPRDINTERFREQ",
    t2."INTERFREQCSTHD2DECN0",
    t2."INTERFREQCSTHD2DRSCP",
    t2."INTERFREQCSTHD2FECN0",
    t2."INTERFREQCSTHD2FRSCP",
    t2."INTERFREQFILTERCOEF",
    t2."INTERFREQHO2DEVENTTYPE",
    t2."INTERFREQHTHD2DECN0",
    t2."INTERFREQHTHD2DRSCP",
    t2."INTERFREQHTHD2FECN0",
    t2."INTERFREQHTHD2FRSCP",
    t2."INTERFREQMCMODE",
    t2."INTERFREQMEASTIME",
    t2."INTERFREQR99PSTHD2DECN0",
    t2."INTERFREQR99PSTHD2DRSCP",
    t2."INTERFREQR99PSTHD2FECN0",
    t2."INTERFREQR99PSTHD2FRSCP",
    t2."INTERFREQREPORTMODE",
    NULL,
    t2."PRDREPORTINTERVAL",
    t2."TARGETFREQCSTHDECN0",
    t2."TARGETFREQCSTHDRSCP",
    t2."TARGETFREQHTHDECN0",
    t2."TARGETFREQHTHDRSCP",
    t2."TARGETFREQR99PSTHDECN0",
    t2."TARGETFREQR99PSTHDRSCP",
    t2."TIMETOINTERFREQHO",
    t2."TIMETOTRIG2D",
    t2."TIMETOTRIG2F",
    t2."TIMETOTRIGFORPRDINTERFREQ",
    t2."USEDFREQCSTHDECN0",
    t2."USEDFREQCSTHDRSCP",
    t2."USEDFREQHTHDECN0",
    t2."USEDFREQHTHDRSCP",
    t2."USEDFREQLOWERTHDECNO",
    t2."USEDFREQR99PSTHDECN0",
    t2."USEDFREQR99PSTHDRSCP",
    t2."USEDFREQUPPERTHDECNO",
    t2."WEIGHTFORUSEDFREQ"
FROM
huawei_mml_umts."UINTERFREQHOCOV" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UINTERFREQHONCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERFREQHONCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AMNTOFRPT2C",
    t1."HYSTFOR2C",
    t1."INTERFREQFILTERCOEF",
    t1."INTERFREQMEASTIME",
    t1."INTERFREQNCOVHOTHDECN0",
    t1."LOGICRNCID",
    t1."PERIODFOR2C",
    t1."TRIGTIME2C"
FROM
huawei_nbi_umts."UINTERFREQHONCOV" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AMNTOFRPT2C",
    t2."HYSTFOR2C",
    t2."INTERFREQFILTERCOEF",
    t2."INTERFREQMEASTIME",
    t2."INTERFREQNCOVHOTHDECN0",
    NULL,
    t2."PERIODFOR2C",
    t2."TRIGTIME2C"
FROM
huawei_mml_umts."UINTERFREQHONCOV" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UINTERFREQNCELL = ReplaceableObject(
    'huawei_cm_3g."UINTERFREQNCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLINDHOFLAG",
    t1."BLINDHOQUALITYCONDITION",
    t1."CELLID",
    t1."CIOOFFSET",
    t1."CLBFLAG",
    t1."DRDECN0THRESHHOLD",
    t1."DRDORLDRFLAG",
    t1."HOCOVPRIO",
    t1."IDLEQOFFSET1SN",
    t1."IDLEQOFFSET2SN",
    t1."INTERFREQADJSQHCS",
    t1."INTERNCELLQUALREQFLAG",
    t1."MBDRFLAG",
    t1."MBDRPRIO",
    t1."NCELLID",
    t1."NCELLRNCID",
    t1."NPRIOFLAG",
    t1."RNCID",
    t1."SIB11IND",
    t1."SIB12IND",
    t1."TPENALTYHCSRESELECT",
    t1."UINTERNCELLSRC",
    t1."NPRIO",
    t1."CONNQOFFSET1SN",
    t1."CONNQOFFSET2SN"
FROM
huawei_nbi_umts."UINTERFREQNCELL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BLINDHOFLAG",
    t2."BLINDHOQUALITYCONDITION",
    t2."CELLID",
    t2."CIOOFFSET",
    t2."CLBFLAG",
    t2."DRDECN0THRESHHOLD",
    t2."DRDORLDRFLAG",
    t2."HOCOVPRIO",
    t2."IDLEQOFFSET1SN",
    t2."IDLEQOFFSET2SN",
    t2."INTERFREQADJSQHCS",
    t2."INTERNCELLQUALREQFLAG",
    t2."MBDRFLAG",
    t2."MBDRPRIO",
    t2."NCELLID",
    t2."NCELLRNCID",
    t2."NPRIOFLAG",
    t2."RNCID",
    t2."SIB11IND",
    t2."SIB12IND",
    t2."TPENALTYHCSRESELECT",
    t2."UINTERNCELLSRC",
    t2."NPRIO",
    t2."CONNQOFFSET1SN",
    t2."CONNQOFFSET2SN"
FROM
huawei_mml_umts."UINTERFREQNCELL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UINTERRATHOCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERRATHOCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BSICVERIFY",
    t1."CSBSICVERIFYINDICATION",
    t1."FILTERCOEFOF2D2F",
    t1."HYSTFOR2D",
    t1."HYSTFOR2F",
    t1."HYSTFORINTERRAT",
    t1."INTERRATCSTHD2DECN0",
    t1."INTERRATCSTHD2DRSCP",
    t1."INTERRATCSTHD2FECN0",
    t1."INTERRATCSTHD2FRSCP",
    t1."INTERRATFILTERCOEF",
    t1."INTERRATHO2DEVENTTYPE",
    t1."INTERRATHTHD2DECN0",
    t1."INTERRATHTHD2DRSCP",
    t1."INTERRATHTHD2FECN0",
    t1."INTERRATHTHD2FRSCP",
    t1."INTERRATMEASTIME",
    t1."INTERRATPERIODREPORTINTERVAL",
    t1."INTERRATPHYCHFAILNUM",
    t1."INTERRATPINGPONGHYST",
    t1."INTERRATPINGPONGTIMER",
    t1."INTERRATR99PSTHD2DECN0",
    t1."INTERRATR99PSTHD2DRSCP",
    t1."INTERRATR99PSTHD2FECN0",
    t1."INTERRATR99PSTHD2FRSCP",
    t1."INTERRATREPORTMODE",
    t1."LOGICRNCID",
    t1."PENALTYTIMEFORPHYCHFAIL",
    t1."PSBSICVERIFYINDICATION",
    t1."TARGETRATCSTHD",
    t1."TARGETRATHTHD",
    t1."TARGETRATR99PSTHD",
    t1."TIMETOTRIGFORNONVERIFY",
    t1."TIMETOTRIGFORVERIFY",
    t1."TRIGTIME2D",
    t1."TRIGTIME2F",
    t1."WEIGHTFORUSEDFREQ"
FROM
huawei_nbi_umts."UINTERRATHOCOV" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BSICVERIFY",
    t2."CSBSICVERIFYINDICATION",
    t2."FILTERCOEFOF2D2F",
    t2."HYSTFOR2D",
    t2."HYSTFOR2F",
    t2."HYSTFORINTERRAT",
    t2."INTERRATCSTHD2DECN0",
    t2."INTERRATCSTHD2DRSCP",
    t2."INTERRATCSTHD2FECN0",
    t2."INTERRATCSTHD2FRSCP",
    t2."INTERRATFILTERCOEF",
    t2."INTERRATHO2DEVENTTYPE",
    t2."INTERRATHTHD2DECN0",
    t2."INTERRATHTHD2DRSCP",
    t2."INTERRATHTHD2FECN0",
    t2."INTERRATHTHD2FRSCP",
    t2."INTERRATMEASTIME",
    t2."INTERRATPERIODREPORTINTERVAL",
    t2."INTERRATPHYCHFAILNUM",
    t2."INTERRATPINGPONGHYST",
    t2."INTERRATPINGPONGTIMER",
    t2."INTERRATR99PSTHD2DECN0",
    t2."INTERRATR99PSTHD2DRSCP",
    t2."INTERRATR99PSTHD2FECN0",
    t2."INTERRATR99PSTHD2FRSCP",
    t2."INTERRATREPORTMODE",
    NULL,
    t2."PENALTYTIMEFORPHYCHFAIL",
    t2."PSBSICVERIFYINDICATION",
    t2."TARGETRATCSTHD",
    t2."TARGETRATHTHD",
    t2."TARGETRATR99PSTHD",
    t2."TIMETOTRIGFORNONVERIFY",
    t2."TIMETOTRIGFORVERIFY",
    t2."TRIGTIME2D",
    t2."TRIGTIME2F",
    t2."WEIGHTFORUSEDFREQ"
FROM
huawei_mml_umts."UINTERRATHOCOV" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UINTERRATHONCOV = ReplaceableObject(
    'huawei_cm_3g."UINTERRATHONCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AMNTOFRPT3C",
    t1."BSICVERIFY",
    t1."CSHOOUT2GLOADTHD",
    t1."HYSTFOR3C",
    t1."INTERRATFILTERCOEF",
    t1."INTERRATHOATTEMPTS",
    t1."INTERRATMEASTIME",
    t1."INTERRATNCOVHOCSTHD",
    t1."INTERRATNCOVHOPSTHD",
    t1."INTERRATPHYCHFAILNUM",
    t1."LOGICRNCID",
    t1."NCOVHOON2GLDIND",
    t1."PENALTYTIMEFORPHYCHFAIL",
    t1."PERIODFOR3C",
    t1."PSHOOUT2GLOADTHD",
    t1."SNDLDINFO2GSMIND",
    t1."TRIGTIME3C"
FROM
huawei_nbi_umts."UINTERRATHONCOV" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AMNTOFRPT3C",
    t2."BSICVERIFY",
    t2."CSHOOUT2GLOADTHD",
    t2."HYSTFOR3C",
    t2."INTERRATFILTERCOEF",
    t2."INTERRATHOATTEMPTS",
    t2."INTERRATMEASTIME",
    t2."INTERRATNCOVHOCSTHD",
    t2."INTERRATNCOVHOPSTHD",
    t2."INTERRATPHYCHFAILNUM",
    NULL,
    t2."NCOVHOON2GLDIND",
    t2."PENALTYTIMEFORPHYCHFAIL",
    t2."PERIODFOR3C",
    t2."PSHOOUT2GLOADTHD",
    t2."SNDLDINFO2GSMIND",
    t2."TRIGTIME3C"
FROM
huawei_mml_umts."UINTERRATHONCOV" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UINTRAFREQHO = ReplaceableObject(
    'huawei_cm_3g."UINTRAFREQHO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLINDHOINTRAFREQMRAMOUNT",
    t1."BLINDHOINTRAFREQMRINTERVAL",
    t1."BLINDHORSCP1FTHRESHOLD",
    t1."DCCCSHOPENALTYTIME",
    t1."FILTERCOEF",
    t1."HYST1AOR1CTRIGSCC",
    t1."HYST1DJUDGETRIGSCC",
    t1."HYSTFOR1A",
    t1."HYSTFOR1B",
    t1."HYSTFOR1C",
    t1."HYSTFOR1D",
    t1."HYSTFOR1F",
    t1."HYSTFOR1J",
    t1."INTRAABLTHDFOR1FECNO",
    t1."INTRAFREQMEASQUANTITY",
    t1."INTRARELTHDFOR1ACSNVP",
    t1."INTRARELTHDFOR1ACSVP",
    t1."INTRARELTHDFOR1APS",
    t1."INTRARELTHDFOR1BCSNVP",
    t1."INTRARELTHDFOR1BCSVP",
    t1."INTRARELTHDFOR1BPS",
    t1."LOGICRNCID",
    t1."MAXCELLINACTIVESET",
    t1."PERIODMRREPORTNUMFOR1A",
    t1."PERIODMRREPORTNUMFOR1C",
    t1."PERIODMRREPORTNUMFOR1J",
    t1."RELTHDFORDWNGRD",
    t1."REPORTINTERVALFOR1A",
    t1."REPORTINTERVALFOR1C",
    t1."REPORTINTERVALFOR1J",
    t1."SHOFAILNUMFORDWNGRD",
    t1."SHOFAILPERIOD",
    t1."SHOQUALMIN",
    t1."SOFTFAILD2FSWITCH",
    t1."SOFTFAILE2DSWITCH",
    t1."TRIGTIME1A",
    t1."TRIGTIME1B",
    t1."TRIGTIME1C",
    t1."TRIGTIME1D",
    t1."TRIGTIME1F",
    t1."TRIGTIME1J",
    t1."WEIGHT"
FROM
huawei_nbi_umts."UINTRAFREQHO" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BLINDHOINTRAFREQMRAMOUNT",
    t2."BLINDHOINTRAFREQMRINTERVAL",
    t2."BLINDHORSCP1FTHRESHOLD",
    t2."DCCCSHOPENALTYTIME",
    t2."FILTERCOEF",
    t2."HYST1AOR1CTRIGSCC",
    t2."HYST1DJUDGETRIGSCC",
    t2."HYSTFOR1A",
    t2."HYSTFOR1B",
    t2."HYSTFOR1C",
    t2."HYSTFOR1D",
    t2."HYSTFOR1F",
    t2."HYSTFOR1J",
    t2."INTRAABLTHDFOR1FECNO",
    t2."INTRAFREQMEASQUANTITY",
    t2."INTRARELTHDFOR1ACSNVP",
    t2."INTRARELTHDFOR1ACSVP",
    t2."INTRARELTHDFOR1APS",
    t2."INTRARELTHDFOR1BCSNVP",
    t2."INTRARELTHDFOR1BCSVP",
    t2."INTRARELTHDFOR1BPS",
    NULL,
    t2."MAXCELLINACTIVESET",
    t2."PERIODMRREPORTNUMFOR1A",
    t2."PERIODMRREPORTNUMFOR1C",
    t2."PERIODMRREPORTNUMFOR1J",
    t2."RELTHDFORDWNGRD",
    t2."REPORTINTERVALFOR1A",
    t2."REPORTINTERVALFOR1C",
    t2."REPORTINTERVALFOR1J",
    t2."SHOFAILNUMFORDWNGRD",
    t2."SHOFAILPERIOD",
    t2."SHOQUALMIN",
    t2."SOFTFAILD2FSWITCH",
    t2."SOFTFAILE2DSWITCH",
    t2."TRIGTIME1A",
    t2."TRIGTIME1B",
    t2."TRIGTIME1C",
    t2."TRIGTIME1D",
    t2."TRIGTIME1F",
    t2."TRIGTIME1J",
    t2."WEIGHT"
FROM
huawei_mml_umts."UINTRAFREQHO" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UINTRAFREQNCELL = ReplaceableObject(
    'huawei_cm_3g."UINTRAFREQNCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CELLSFORBIDDEN1A",
    t1."CELLSFORBIDDEN1B",
    t1."CIOOFFSET",
    t1."IDLEQOFFSET1SN",
    t1."IDLEQOFFSET2SN",
    t1."NCELLID",
    t1."NCELLRNCID",
    t1."NPRIOFLAG",
    t1."RNCID",
    t1."SIB11IND",
    t1."SIB12IND",
    t1."TPENALTYHCSRESELECT",
    t1."UINTRANCELLSRC",
    t1."NPRIO",
    t1."CONNQOFFSET1SN",
    t1."CONNQOFFSET2SN"
FROM
huawei_nbi_umts."UINTRAFREQNCELL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    t2."CELLSFORBIDDEN1A",
    t2."CELLSFORBIDDEN1B",
    t2."CIOOFFSET",
    t2."IDLEQOFFSET1SN",
    t2."IDLEQOFFSET2SN",
    t2."NCELLID",
    t2."NCELLRNCID",
    t2."NPRIOFLAG",
    t2."RNCID",
    t2."SIB11IND",
    t2."SIB12IND",
    t2."TPENALTYHCSRESELECT",
    t2."UINTRANCELLSRC",
    t2."NPRIO",
    t2."CONNQOFFSET1SN",
    t2."CONNQOFFSET2SN"
FROM
huawei_mml_umts."UINTRAFREQNCELL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UIPSERVICEQOS = ReplaceableObject(
    'huawei_cm_3g."UIPSERVICEQOS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPINDEX",
    t1."LOGICRNCID",
    t1."RECINDEX",
    t1."TRAFFICPRIORITY",
    t1."TRAFFICTYPE"
FROM
huawei_nbi_umts."UIPSERVICEQOS" t1

"""
)

UIURGCONN = ReplaceableObject(
    'huawei_cm_3g."UIURGCONN"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DPX",
    t1."INTRAMBSCIND",
    t1."LOGICRNCID",
    t1."NBSCINDEX"
FROM
huawei_nbi_umts."UIURGCONN" t1

"""
)

UIUTIMERANDNUM = ReplaceableObject(
    'huawei_cm_3g."UIUTIMERANDNUM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNID",
    t1."CNOPINDEX",
    t1."IGORTMR",
    t1."INTRTMR",
    t1."LOGICRNCID",
    t1."RAFCTMR",
    t1."RATCTMR",
    t1."RSTRSNDNUM",
    t1."STATEINDTMR"
FROM
huawei_nbi_umts."UIUTIMERANDNUM" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNID",
    t2."CNOPINDEX",
    t2."IGORTMR",
    t2."INTRTMR",
    NULL,
    t2."RAFCTMR",
    t2."RATCTMR",
    t2."RSTRSNDNUM",
    t2."STATEINDTMR"
FROM
huawei_mml_umts."UIUTIMERANDNUM" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UKPIALMTHD = ReplaceableObject(
    'huawei_cm_3g."UKPIALMTHD"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AMRRABABNORMRELRATIOTHD",
    t1."AMRRABESTABATTMINNUM",
    t1."AMRRABESTABSUCCRATIOTHD",
    t1."AMRRABRELMINNUM",
    t1."HSDPARABESTATTMINNUM",
    t1."HSDPARABESTSUCCRATIOTHD",
    t1."HSUPARABESTATTMINNUM",
    t1."HSUPARABESTSUCCRATIOTHD",
    t1."KPIALARMCHKTIMES",
    t1."KPIALARMSWITCH",
    t1."PSRABABNORMRELRATIOTHD",
    t1."PSRABESTATTMINNUM",
    t1."PSRABESTSUCCRATIOTHD",
    t1."PSRABRELMINNUM",
    t1."RRCCONNESTABATTMINNUM",
    t1."RRCCONNESTABSUCCRATIOTHD",
    t1."VPRABABNORMRELRATIOTHD",
    t1."VPRABESTATTMINNUM",
    t1."VPRABESTSUCCRATIOTHD",
    t1."VPRABRELMINNUM"
FROM
huawei_nbi_umts."UKPIALMTHD" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AMRRABABNORMRELRATIOTHD",
    t2."AMRRABESTABATTMINNUM",
    t2."AMRRABESTABSUCCRATIOTHD",
    t2."AMRRABRELMINNUM",
    t2."HSDPARABESTATTMINNUM",
    t2."HSDPARABESTSUCCRATIOTHD",
    t2."HSUPARABESTATTMINNUM",
    t2."HSUPARABESTSUCCRATIOTHD",
    t2."KPIALARMCHKTIMES",
    t2."KPIALARMSWITCH",
    t2."PSRABABNORMRELRATIOTHD",
    t2."PSRABESTATTMINNUM",
    t2."PSRABESTSUCCRATIOTHD",
    t2."PSRABRELMINNUM",
    t2."RRCCONNESTABATTMINNUM",
    t2."RRCCONNESTABSUCCRATIOTHD",
    t2."VPRABABNORMRELRATIOTHD",
    t2."VPRABESTATTMINNUM",
    t2."VPRABESTSUCCRATIOTHD",
    t2."VPRABRELMINNUM"
FROM
huawei_mml_umts."UKPIALMTHD" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

ULAC = ReplaceableObject(
    'huawei_cm_3g."ULAC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPINDEX",
    t1."LAC",
    t1."LOGICRNCID",
    t1."PLMNVALTAGMAX",
    t1."PLMNVALTAGMIN"
FROM
huawei_nbi_umts."ULAC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNOPINDEX",
    t2."LAC",
    NULL,
    t2."PLMNVALTAGMAX",
    t2."PLMNVALTAGMIN"
FROM
huawei_mml_umts."ULAC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

ULDCALGOPARA = ReplaceableObject(
    'huawei_cm_3g."ULDCALGOPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LDCSWITCH",
    t1."LDRFIRSTPRI",
    t1."LDRFOURTHPRI",
    t1."LDRSECONDPRI",
    t1."LDRTHIRDPRI",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."ULDCALGOPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."LDRFIRSTPRI",
    t2."LDRFOURTHPRI",
    t2."LDRSECONDPRI",
    t2."LDRTHIRDPRI",
    NULL
FROM
huawei_mml_umts."ULDCALGOPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

ULDCPERIOD = ReplaceableObject(
    'huawei_cm_3g."ULDCPERIOD"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CLBPERIODTIMERLEN",
    t1."FAIRNESSPERIODTIMERLEN",
    t1."INTRAFREQLDBPERIODTIMERLEN",
    t1."INTRAFREQULBPERIODTIMERLEN",
    t1."LDRPERIODTIMERLEN",
    t1."LOGICRNCID",
    t1."OLCPERIODTIMERLEN",
    t1."PUCPERIODTIMERLEN"
FROM
huawei_nbi_umts."ULDCPERIOD" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CLBPERIODTIMERLEN",
    t2."FAIRNESSPERIODTIMERLEN",
    t2."INTRAFREQLDBPERIODTIMERLEN",
    t2."INTRAFREQULBPERIODTIMERLEN",
    t2."LDRPERIODTIMERLEN",
    NULL,
    t2."OLCPERIODTIMERLEN",
    t2."PUCPERIODTIMERLEN"
FROM
huawei_mml_umts."ULDCPERIOD" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

ULDM = ReplaceableObject(
    'huawei_cm_3g."ULDM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CHOICERPRTUNITFORDLBASICMEAS",
    t1."CHOICERPRTUNITFORDLOLCMEAS",
    t1."CHOICERPRTUNITFORHSDPAPWRMEAS",
    t1."CHOICERPRTUNITFORHSDPARATEMEAS",
    t1."CHOICERPRTUNITFORHSUPARATEMEAS",
    t1."CHOICERPRTUNITFORULBASICMEAS",
    t1."CHOICERPRTUNITFORULOLCMEAS",
    t1."DLBASICCOMMMEASFILTERCOEFF",
    t1."DLCACAVGFILTERLEN",
    t1."DLLDRAVGFILTERLEN",
    t1."DLOLCAVGFILTERLEN",
    t1."DLOLCMEASFILTERCOEFF",
    t1."DLOLCTRIGHYST",
    t1."HSDPANEEDPWRFILTERLEN",
    t1."HSDPAPRVIDBITRATEFILTERLEN",
    t1."HSUPAPRVIDBITRATEFILTERLEN",
    t1."LDBAVGFILTERLEN",
    t1."LOADLEVELFORLTE",
    t1."LOGICRNCID",
    t1."MAXMEASCONTINVALIDTIMES",
    t1."PERIODPROTECTTIMERCOEFF",
    t1."PUCAVGFILTERLEN",
    t1."TENMSECFORDLBASICMEAS",
    t1."TENMSECFORDLOLCMEAS",
    t1."TENMSECFORHSDPAPRVIDRATEMEAS",
    t1."TENMSECFORHSDPAPWRMEAS",
    t1."TENMSECFORHSUPAPRVIDRATEMEAS",
    t1."TENMSECFORULBASICMEAS",
    t1."TENMSECFORULOLCMEAS",
    t1."ULBASICCOMMMEASFILTERCOEFF",
    t1."ULBAVGFILTERLEN",
    t1."ULCACAVGFILTERLEN",
    t1."ULLDRAVGFILTERLEN",
    t1."ULOLCAVGFILTERLEN",
    t1."ULOLCMEASFILTERCOEFF",
    t1."ULOLCTRIGHYST"
FROM
huawei_nbi_umts."ULDM" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CHOICERPRTUNITFORDLBASICMEAS",
    t2."CHOICERPRTUNITFORDLOLCMEAS",
    t2."CHOICERPRTUNITFORHSDPAPWRMEAS",
    t2."CHOICERPRTUNITFORHSDPARATEMEAS",
    t2."CHOICERPRTUNITFORHSUPARATEMEAS",
    t2."CHOICERPRTUNITFORULBASICMEAS",
    t2."CHOICERPRTUNITFORULOLCMEAS",
    t2."DLBASICCOMMMEASFILTERCOEFF",
    t2."DLCACAVGFILTERLEN",
    t2."DLLDRAVGFILTERLEN",
    t2."DLOLCAVGFILTERLEN",
    t2."DLOLCMEASFILTERCOEFF",
    t2."DLOLCTRIGHYST",
    t2."HSDPANEEDPWRFILTERLEN",
    t2."HSDPAPRVIDBITRATEFILTERLEN",
    t2."HSUPAPRVIDBITRATEFILTERLEN",
    t2."LDBAVGFILTERLEN",
    t2."LOADLEVELFORLTE",
    NULL,
    t2."MAXMEASCONTINVALIDTIMES",
    t2."PERIODPROTECTTIMERCOEFF",
    t2."PUCAVGFILTERLEN",
    t2."TENMSECFORDLBASICMEAS",
    t2."TENMSECFORDLOLCMEAS",
    t2."TENMSECFORHSDPAPRVIDRATEMEAS",
    t2."TENMSECFORHSDPAPWRMEAS",
    t2."TENMSECFORHSUPAPRVIDRATEMEAS",
    t2."TENMSECFORULBASICMEAS",
    t2."TENMSECFORULOLCMEAS",
    t2."ULBASICCOMMMEASFILTERCOEFF",
    t2."ULBAVGFILTERLEN",
    t2."ULCACAVGFILTERLEN",
    t2."ULLDRAVGFILTERLEN",
    t2."ULOLCAVGFILTERLEN",
    t2."ULOLCMEASFILTERCOEFF",
    t2."ULOLCTRIGHYST"
FROM
huawei_mml_umts."ULDM" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

ULOCELL = ReplaceableObject(
    'huawei_cm_3g."ULOCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOCELL",
    t1."LOGICRNCID",
    t1."NODEBID"
FROM
huawei_nbi_umts."ULOCELL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."LOCELL",
    NULL,
    t2."NODEBID"
FROM
huawei_mml_umts."ULOCELL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UMBSCCRRM = ReplaceableObject(
    'huawei_cm_3g."UMBSCCRRM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."COMMONMEASUREMENTPERIOD",
    t1."IRATCOMMONMEASSWITCH",
    t1."LOADHOON3G2GLDIND",
    t1."LOGICRNCID",
    t1."MBSC2GLOADADJUSTCOEFF",
    t1."MBSC3G2GLDBLCCSDELTATHRD",
    t1."MBSC3G2GLDBLCPSDELTATHRD",
    t1."MBSCLDRREDIRFACTOR",
    t1."MBSCNCOVHOON2GLDIND",
    t1."MBSCNONLDRREDIRFACTOR",
    t1."MBSCREQGERANINFOSWITCH",
    t1."MBSCSDIFFLDBPHASESWITCH",
    t1."MBSCSERVICEDIFFLDBSWITCH"
FROM
huawei_nbi_umts."UMBSCCRRM" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."COMMONMEASUREMENTPERIOD",
    t2."IRATCOMMONMEASSWITCH",
    t2."LOADHOON3G2GLDIND",
    t2."LOGICRNCID",
    t2."MBSC2GLOADADJUSTCOEFF",
    t2."MBSC3G2GLDBLCCSDELTATHRD",
    t2."MBSC3G2GLDBLCPSDELTATHRD",
    t2."MBSCLDRREDIRFACTOR",
    t2."MBSCNCOVHOON2GLDIND",
    t2."MBSCNONLDRREDIRFACTOR",
    t2."MBSCREQGERANINFOSWITCH",
    t2."MBSCSDIFFLDBPHASESWITCH",
    t2."MBSCSERVICEDIFFLDBSWITCH"
FROM
huawei_gexport_wcdma."UMBSCCRRM_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."COMMONMEASUREMENTPERIOD",
    t3."IRATCOMMONMEASSWITCH",
    t3."LOADHOON3G2GLDIND",
    t3."LOGICRNCID",
    t3."MBSC2GLOADADJUSTCOEFF",
    t3."MBSC3G2GLDBLCCSDELTATHRD",
    t3."MBSC3G2GLDBLCPSDELTATHRD",
    t3."MBSCLDRREDIRFACTOR",
    t3."MBSCNCOVHOON2GLDIND",
    t3."MBSCNONLDRREDIRFACTOR",
    t3."MBSCREQGERANINFOSWITCH",
    t3."MBSCSDIFFLDBPHASESWITCH",
    t3."MBSCSERVICEDIFFLDBSWITCH"
FROM
huawei_gexport_wcdma."UMBSCCRRM_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."COMMONMEASUREMENTPERIOD",
    t4."IRATCOMMONMEASSWITCH",
    t4."LOADHOON3G2GLDIND",
    NULL,
    t4."MBSC2GLOADADJUSTCOEFF",
    t4."MBSC3G2GLDBLCCSDELTATHRD",
    t4."MBSC3G2GLDBLCPSDELTATHRD",
    t4."MBSCLDRREDIRFACTOR",
    t4."MBSCNCOVHOON2GLDIND",
    t4."MBSCNONLDRREDIRFACTOR",
    t4."MBSCREQGERANINFOSWITCH",
    t4."MBSCSDIFFLDBPHASESWITCH",
    t4."MBSCSERVICEDIFFLDBSWITCH"
FROM
huawei_mml_umts."UMBSCCRRM" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UMCDRD = ReplaceableObject(
    'huawei_cm_3g."UMCDRD"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BLINDDRDEXCEPTHRETRYSWITCH",
    t1."DRDFAIPENALTYPERIODNUM",
    t1."HRETRYTIMERLENGTH",
    t1."LOGICRNCID",
    t1."PRDREPORTINTERVAL",
    t1."TARGETFREQTHDECN0",
    t1."TARGETFREQTHDRSCP",
    t1."UESPDOPTSWITCH"
FROM
huawei_nbi_umts."UMCDRD" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BLINDDRDEXCEPTHRETRYSWITCH",
    t2."DRDFAIPENALTYPERIODNUM",
    t2."HRETRYTIMERLENGTH",
    NULL,
    t2."PRDREPORTINTERVAL",
    t2."TARGETFREQTHDECN0",
    t2."TARGETFREQTHDRSCP",
    t2."UESPDOPTSWITCH"
FROM
huawei_mml_umts."UMCDRD" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UMCLDR = ReplaceableObject(
    'huawei_cm_3g."UMCLDR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."INTERFREQMEASTIME",
    t1."LOGICRNCID",
    t1."PRDREPORTINTERVAL",
    t1."TARGETFREQTHDECN0",
    t1."TARGETFREQTHDRSCP",
    t1."UESPDOPTSWITCH"
FROM
huawei_nbi_umts."UMCLDR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."INTERFREQMEASTIME",
    NULL,
    t2."PRDREPORTINTERVAL",
    t2."TARGETFREQTHDECN0",
    t2."TARGETFREQTHDRSCP",
    t2."UESPDOPTSWITCH"
FROM
huawei_mml_umts."UMCLDR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UMRSWITCH = ReplaceableObject(
    'huawei_cm_3g."UMRSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UMRSWITCH" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UMRSWITCH_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UMRSWITCH_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL
FROM
huawei_mml_umts."UMRSWITCH" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UMULTIRABHOCOV = ReplaceableObject(
    'huawei_cm_3g."UMULTIRABHOCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CSPSMRABTHD2DECN0",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UMULTIRABHOCOV" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CSPSMRABTHD2DECN0",
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UMULTIRABHOCOV_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CSPSMRABTHD2DECN0",
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UMULTIRABHOCOV_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CSPSMRABTHD2DECN0",
    NULL
FROM
huawei_mml_umts."UMULTIRABHOCOV" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UNBSC = ReplaceableObject(
    'huawei_cm_3g."UNBSC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."NBSCINDEX",
    t1."NBSCNAME"
FROM
huawei_nbi_umts."UNBSC" t1

"""
)

UNCELLDETECTSWITCH = ReplaceableObject(
    'huawei_cm_3g."UNCELLDETECTSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."INTERFREQNCELLDETECTSWITCH",
    t1."INTERRATNCELLDETECTSWITCH",
    t1."INTRAFREQNCELLDETECTSWITCH",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UNCELLDETECTSWITCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."INTERFREQNCELLDETECTSWITCH",
    t2."INTERRATNCELLDETECTSWITCH",
    t2."INTRAFREQNCELLDETECTSWITCH",
    NULL
FROM
huawei_mml_umts."UNCELLDETECTSWITCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UNCP = ReplaceableObject(
    'huawei_cm_3g."UNCP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CARRYLNKT",
    t1."LOGICRNCID",
    t1."NODEBID",
    t1."SCTPLNKID",
    t1."SAALLNKN"
FROM
huawei_nbi_umts."UNCP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CARRYLNKT",
    NULL,
    t2."NODEBID",
    t2."SCTPLNKID",
    t2."SAALLNKN"
FROM
huawei_mml_umts."UNCP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UNODEB = ReplaceableObject(
    'huawei_cm_3g."UNODEB"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACTSTATUS",
    t1."AUTOHOMINGFLAG",
    t1."CNOPINDEX",
    t1."DSSFLAG",
    t1."HOSTTYPE",
    t1."LOGICRNCID",
    t1."NODEBID",
    t1."NODEBNAME",
    t1."NODEBPROTCLVER",
    t1."NODEBTRACESWITCH",
    t1."RSCMNGMODE",
    t1."SATELLITEIND",
    t1."SHARINGTYPE",
    t1."TNLBEARERTYPE",
    t1."TRANSDELAY"
FROM
huawei_nbi_umts."UNODEB" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."AUTOHOMINGFLAG",
    t2."CNOPINDEX",
    t2."DSSFLAG",
    t2."HOSTTYPE",
    NULL,
    t2."NODEBID",
    t2."NODEBNAME",
    t2."NODEBPROTCLVER",
    t2."NODEBTRACESWITCH",
    t2."RSCMNGMODE",
    t2."SATELLITEIND",
    t2."SHARINGTYPE",
    t2."TNLBEARERTYPE",
    t2."TRANSDELAY"
FROM
huawei_mml_umts."UNODEB" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

UNION
SELECT
    t3."FileName",
    t3."varDateTime",
    NULL,
    NULL,
    t3."BAM_VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    t3."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."NODEBID",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UNODEB_BLK" t3
INNER JOIN huawei_mml_umts."SYS" t31 ON t31."FileName" = t3."FileName"

"""
)

UNODEBALGOPARA = ReplaceableObject(
    'huawei_cm_3g."UNODEBALGOPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."HSUPACECONSUMESELECTION",
    t1."LOGICRNCID",
    t1."NODEBHSDPAMAXUSERNUM",
    t1."NODEBHSUPAMAXUSERNUM",
    t1."NODEBID",
    t1."NODEBLDCALGOSWITCH"
FROM
huawei_nbi_umts."UNODEBALGOPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."HSUPACECONSUMESELECTION",
    NULL,
    t2."NODEBHSDPAMAXUSERNUM",
    t2."NODEBHSUPAMAXUSERNUM",
    t2."NODEBID",
    NULL
FROM
huawei_mml_umts."UNODEBALGOPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UNODEBIP = ReplaceableObject(
    'huawei_cm_3g."UNODEBIP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IPSN",
    t1."IPSRN",
    t1."LOGICRNCID",
    t1."NBIPOAMIP",
    t1."NBIPOAMMASK",
    t1."NBTRANTP",
    t1."NODEBID",
    t1."VLANFLAG",
    t1."ATMSN",
    t1."ATMSRN",
    t1."NBATMOAMIP",
    t1."NBATMOAMMASK",
    t1."NBCTRLSN"
FROM
huawei_nbi_umts."UNODEBIP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."IPSN",
    t2."IPSRN",
    NULL,
    t2."NBIPOAMIP",
    t2."NBIPOAMMASK",
    t2."NBTRANTP",
    t2."NODEBID",
    t2."VLANFLAG",
    t2."ATMSN",
    t2."ATMSRN",
    t2."NBATMOAMIP",
    t2."NBATMOAMMASK",
    t2."NBCTRLSN"
FROM
huawei_mml_umts."UNODEBIP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UNODEBLDR = ReplaceableObject(
    'huawei_cm_3g."UNODEBLDR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DLCSINTERRATSHOULDBEHOUENUM",
    t1."DLCSINTERRATSHOULDNOTHOUENUM",
    t1."DLLDRAMRRATEREDUCTIONRABNUM",
    t1."DLLDRBERATEREDUCTIONRABNUM",
    t1."DLLDRFIFTHACTION",
    t1."DLLDRFIRSTACTION",
    t1."DLLDRFOURTHACTION",
    t1."DLLDRPSRTQOSRENEGRABNUM",
    t1."DLLDRSECONDACTION",
    t1."DLLDRSEVENTHACTION",
    t1."DLLDRSIXTHACTION",
    t1."DLLDRTHIRDACTION",
    t1."DLPSINTERRATSHOULDBEHOUENUM",
    t1."DLPSINTERRATSHOULDNOTHOUENUM",
    t1."LOGICRNCID",
    t1."NODEBID",
    t1."ULCSINTERRATSHOULDBEHOUENUM",
    t1."ULCSINTERRATSHOULDNOTHOUENUM",
    t1."ULINTERFREQHOCELDRSPACETHD",
    t1."ULLDRAMRRATEREDUCTIONRABNUM",
    t1."ULLDRBERATEREDUCTIONRABNUM",
    t1."ULLDRCREDITSFRESTHD",
    t1."ULLDREIGHTHACTION",
    t1."ULLDRFIFTHACTION",
    t1."ULLDRFIRSTACTION",
    t1."ULLDRFOURTHACTION",
    t1."ULLDRPSRTQOSRENEGRABNUM",
    t1."ULLDRSECONDACTION",
    t1."ULLDRSEVENTHACTION",
    t1."ULLDRSIXTHACTION",
    t1."ULLDRTHIRDACTION",
    t1."ULPSINTERRATSHOULDBEHOUENUM",
    t1."ULPSINTERRATSHOULDNOTHOUENUM"
FROM
huawei_nbi_umts."UNODEBLDR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."DLCSINTERRATSHOULDBEHOUENUM",
    t2."DLCSINTERRATSHOULDNOTHOUENUM",
    t2."DLLDRAMRRATEREDUCTIONRABNUM",
    t2."DLLDRBERATEREDUCTIONRABNUM",
    t2."DLLDRFIFTHACTION",
    t2."DLLDRFIRSTACTION",
    t2."DLLDRFOURTHACTION",
    t2."DLLDRPSRTQOSRENEGRABNUM",
    t2."DLLDRSECONDACTION",
    t2."DLLDRSEVENTHACTION",
    t2."DLLDRSIXTHACTION",
    t2."DLLDRTHIRDACTION",
    t2."DLPSINTERRATSHOULDBEHOUENUM",
    t2."DLPSINTERRATSHOULDNOTHOUENUM",
    NULL,
    t2."NODEBID",
    t2."ULCSINTERRATSHOULDBEHOUENUM",
    t2."ULCSINTERRATSHOULDNOTHOUENUM",
    t2."ULINTERFREQHOCELDRSPACETHD",
    t2."ULLDRAMRRATEREDUCTIONRABNUM",
    t2."ULLDRBERATEREDUCTIONRABNUM",
    t2."ULLDRCREDITSFRESTHD",
    t2."ULLDREIGHTHACTION",
    t2."ULLDRFIFTHACTION",
    t2."ULLDRFIRSTACTION",
    t2."ULLDRFOURTHACTION",
    t2."ULLDRPSRTQOSRENEGRABNUM",
    t2."ULLDRSECONDACTION",
    t2."ULLDRSEVENTHACTION",
    t2."ULLDRSIXTHACTION",
    t2."ULLDRTHIRDACTION",
    t2."ULPSINTERRATSHOULDBEHOUENUM",
    t2."ULPSINTERRATSHOULDNOTHOUENUM"
FROM
huawei_mml_umts."UNODEBLDR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UNODEBMNTMODE = ReplaceableObject(
    'huawei_cm_3g."UNODEBMNTMODE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."MNTMODE",
    t1."NODEBID",
    t1."ET",
    t1."ST"
FROM
huawei_nbi_umts."UNODEBMNTMODE" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID",
    t2."MNTMODE",
    t2."NODEBID",
    NULL,
    NULL
FROM
huawei_gexport_wcdma."UNODEBMNTMODE_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID",
    t3."MNTMODE",
    t3."NODEBID",
    NULL,
    NULL
FROM
huawei_gexport_wcdma."UNODEBMNTMODE_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."MNTMODE",
    t4."NODEBID",
    NULL,
    NULL
FROM
huawei_mml_umts."UNODEBMNTMODE" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UNODEBOLC = ReplaceableObject(
    'huawei_cm_3g."UNODEBOLC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IUBDLOLCRELRABNUM",
    t1."IUBULOLCRELRABNUM",
    t1."LOGICRNCID",
    t1."NODEBID"
FROM
huawei_nbi_umts."UNODEBOLC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."IUBDLOLCRELRABNUM",
    t2."IUBULOLCRELRABNUM",
    NULL,
    t2."NODEBID"
FROM
huawei_mml_umts."UNODEBOLC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UNRIGLBCNIDMAP = ReplaceableObject(
    'huawei_cm_3g."UNRIGLBCNIDMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNID",
    t1."CNOPINDEX",
    t1."LOGICRNCID",
    t1."NRI"
FROM
huawei_nbi_umts."UNRIGLBCNIDMAP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNID",
    t2."CNOPINDEX",
    NULL,
    t2."NRI"
FROM
huawei_mml_umts."UNRIGLBCNIDMAP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UNRNC = ReplaceableObject(
    'huawei_cm_3g."UNRNC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CSVOICEOVERHSPASUPPIND",
    t1."DPX",
    t1."HHORELOCPROCSWITCH",
    t1."HHOTRIG",
    t1."IUBCPPRIVATEINTERFACESWITCH",
    t1."IUBUPPRIVATEINTERFACESWITCH",
    t1."IUREXISTIND",
    t1."IURHSDPASUPPIND",
    t1."IURHSUPASUPPIND",
    t1."LOGICRNCID",
    t1."NRNCID",
    t1."PROCESSSWITCH",
    t1."PSBEPROCTYPE",
    t1."RNCPROTCLVER",
    t1."SERVICEIND",
    t1."SHOTRIG",
    t1."STATEINDTMR",
    t1."SUPPIURCCH",
    t1."TNLBEARERTYPE",
    t1."WAMRSUPPIND"
FROM
huawei_nbi_umts."UNRNC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CSVOICEOVERHSPASUPPIND",
    t2."DPX",
    NULL,
    t2."HHOTRIG",
    t2."IUBCPPRIVATEINTERFACESWITCH",
    t2."IUBUPPRIVATEINTERFACESWITCH",
    t2."IUREXISTIND",
    t2."IURHSDPASUPPIND",
    t2."IURHSUPASUPPIND",
    NULL,
    t2."NRNCID",
    NULL,
    t2."PSBEPROCTYPE",
    t2."RNCPROTCLVER",
    t2."SERVICEIND",
    NULL,
    t2."STATEINDTMR",
    t2."SUPPIURCCH",
    t2."TNLBEARERTYPE",
    t2."WAMRSUPPIND"
FROM
huawei_mml_umts."UNRNC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UOPERATORCFGPARA = ReplaceableObject(
    'huawei_cm_3g."UOPERATORCFGPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPINDEX",
    t1."CSINFOUPDFLAG",
    t1."CSNRICFGMODE",
    t1."CSNRILENGTH",
    t1."LOGICRNCID",
    t1."NNSFTMR",
    t1."NULLNRI",
    t1."NULLNRIOPTSWITCH",
    t1."PSINFOUPDFLAG",
    t1."PSNRICFGMODE",
    t1."PSNRILENGTH"
FROM
huawei_nbi_umts."UOPERATORCFGPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNOPINDEX",
    t2."CSINFOUPDFLAG",
    t2."CSNRICFGMODE",
    t2."CSNRILENGTH",
    NULL,
    t2."NNSFTMR",
    t2."NULLNRI",
    t2."NULLNRIOPTSWITCH",
    t2."PSINFOUPDFLAG",
    t2."PSNRICFGMODE",
    t2."PSNRILENGTH"
FROM
huawei_mml_umts."UOPERATORCFGPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UOPERATORSHARINGMODE = ReplaceableObject(
    'huawei_cm_3g."UOPERATORSHARINGMODE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."INTERPLMNHOALLOWEDINTERRAT",
    t1."INTERPLMNHOALLOWEDINTRARAT",
    t1."INTERPLMNMULTICARRSWITCH",
    t1."LOGICRNCID",
    t1."MOCNSUPPORT",
    t1."RANSHARINGSUPPORT"
FROM
huawei_nbi_umts."UOPERATORSHARINGMODE" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."INTERPLMNHOALLOWEDINTERRAT",
    t2."INTERPLMNHOALLOWEDINTRARAT",
    t2."INTERPLMNMULTICARRSWITCH",
    NULL,
    t2."MOCNSUPPORT",
    t2."RANSHARINGSUPPORT"
FROM
huawei_mml_umts."UOPERATORSHARINGMODE" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPCCPCH = ReplaceableObject(
    'huawei_cm_3g."UPCCPCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PHYCHID"
FROM
huawei_nbi_umts."UPCCPCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."PHYCHID"
FROM
huawei_mml_umts."UPCCPCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPCH = ReplaceableObject(
    'huawei_cm_3g."UPCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PCHPOWER",
    t1."PHYCHID",
    t1."RATEMATCHINGATTR",
    t1."TOAWE",
    t1."TOAWS",
    t1."TRCHID"
FROM
huawei_nbi_umts."UPCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."PCHPOWER",
    t2."PHYCHID",
    t2."RATEMATCHINGATTR",
    t2."TOAWE",
    t2."TOAWS",
    t2."TRCHID"
FROM
huawei_mml_umts."UPCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPCHDYNTFS = ReplaceableObject(
    'huawei_cm_3g."UPCHDYNTFS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."RLCSIZE",
    t1."TBNUMBER1",
    t1."TBNUMBER2",
    t1."TFSNUMBER",
    t1."TRCHID"
FROM
huawei_nbi_umts."UPCHDYNTFS" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."RLCSIZE",
    t2."TBNUMBER1",
    t2."TBNUMBER2",
    t2."TFSNUMBER",
    t2."TRCHID"
FROM
huawei_mml_umts."UPCHDYNTFS" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPCPICH = ReplaceableObject(
    'huawei_cm_3g."UPCPICH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."DSSSMALLCOVPCPICHPOWER",
    t1."LOGICRNCID",
    t1."MAXPCPICHPOWER",
    t1."MINPCPICHPOWER",
    t1."PCPICHPOWER",
    t1."PHYCHID"
FROM
huawei_nbi_umts."UPCPICH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    t2."DSSSMALLCOVPCPICHPOWER",
    NULL,
    t2."MAXPCPICHPOWER",
    t2."MINPCPICHPOWER",
    t2."PCPICHPOWER",
    t2."PHYCHID"
FROM
huawei_mml_umts."UPCPICH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPICH = ReplaceableObject(
    'huawei_cm_3g."UPICH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PHYCHID",
    t1."PICHID",
    t1."PICHMODE",
    t1."STTDIND"
FROM
huawei_nbi_umts."UPICH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."PHYCHID",
    t2."PICHID",
    t2."PICHMODE",
    t2."STTDIND"
FROM
huawei_mml_umts."UPICH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPOOLLOADSHAREPARA = ReplaceableObject(
    'huawei_cm_3g."UPOOLLOADSHAREPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CPLOADSHARETYPE",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UPOOLLOADSHAREPARA" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CPLOADSHARETYPE",
    t2."LOGICRNCID"
FROM
huawei_gexport_wcdma."UPOOLLOADSHAREPARA_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CPLOADSHARETYPE",
    t3."LOGICRNCID"
FROM
huawei_gexport_wcdma."UPOOLLOADSHAREPARA_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CPLOADSHARETYPE",
    NULL
FROM
huawei_mml_umts."UPOOLLOADSHAREPARA" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UPOOLREDUNDANCY = ReplaceableObject(
    'huawei_cm_3g."UPOOLREDUNDANCY"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."REDUNDANCYMODE"
FROM
huawei_nbi_umts."UPOOLREDUNDANCY" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID",
    t2."REDUNDANCYMODE"
FROM
huawei_gexport_wcdma."UPOOLREDUNDANCY_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID",
    t3."REDUNDANCYMODE"
FROM
huawei_gexport_wcdma."UPOOLREDUNDANCY_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."REDUNDANCYMODE"
FROM
huawei_mml_umts."UPOOLREDUNDANCY" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UPRACHACTOASCMAP = ReplaceableObject(
    'huawei_cm_3g."UPRACHACTOASCMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AC09TOASC",
    t1."AC10TOASC",
    t1."AC11TOASC",
    t1."AC12TOASC",
    t1."AC13TOASC",
    t1."AC14TOASC",
    t1."AC15TOASC",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PHYCHID"
FROM
huawei_nbi_umts."UPRACHACTOASCMAP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AC09TOASC",
    t2."AC10TOASC",
    t2."AC11TOASC",
    t2."AC12TOASC",
    t2."AC13TOASC",
    t2."AC14TOASC",
    t2."AC15TOASC",
    t2."CELLID",
    NULL,
    t2."PHYCHID"
FROM
huawei_mml_umts."UPRACHACTOASCMAP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPRACHASC = ReplaceableObject(
    'huawei_cm_3g."UPRACHASC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACCESSSERVICECLASS",
    t1."AVAILABLESIGNATUREENDINDEX",
    t1."AVAILABLESIGNATURESTARTINDEX",
    t1."AVAILABLESUBCHANNELCTRLWORD",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PHYCHID"
FROM
huawei_nbi_umts."UPRACHASC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ACCESSSERVICECLASS",
    t2."AVAILABLESIGNATUREENDINDEX",
    t2."AVAILABLESIGNATURESTARTINDEX",
    t2."AVAILABLESUBCHANNELCTRLWORD",
    t2."CELLID",
    NULL,
    t2."PHYCHID"
FROM
huawei_mml_umts."UPRACHASC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPRACHBASIC = ReplaceableObject(
    'huawei_cm_3g."UPRACHBASIC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACTSTATUS",
    t1."CELLID",
    t1."CONSTANTVALUE",
    t1."CTFCSIZE",
    t1."LOGICRNCID",
    t1."PHYCHID",
    t1."POWERRAMPSTEP",
    t1."PREAMBLERETRANSMAX",
    t1."PREAMBLESIGNATURES",
    t1."RACHSUBCHNO"
FROM
huawei_nbi_umts."UPRACHBASIC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."CELLID",
    t2."CONSTANTVALUE",
    t2."CTFCSIZE",
    NULL,
    t2."PHYCHID",
    t2."POWERRAMPSTEP",
    t2."PREAMBLERETRANSMAX",
    NULL,
    NULL
FROM
huawei_mml_umts."UPRACHBASIC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPRACHSLOTFORMAT = ReplaceableObject(
    'huawei_cm_3g."UPRACHSLOTFORMAT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PHYCHID",
    t1."SLOTFORMAT1",
    t1."SLOTFORMAT2",
    t1."SLOTFORMAT3",
    t1."SLOTFORMAT4",
    t1."SLOTFORMATNUM"
FROM
huawei_nbi_umts."UPRACHSLOTFORMAT" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."PHYCHID",
    t2."SLOTFORMAT1",
    t2."SLOTFORMAT2",
    t2."SLOTFORMAT3",
    t2."SLOTFORMAT4",
    t2."SLOTFORMATNUM"
FROM
huawei_mml_umts."UPRACHSLOTFORMAT" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPRACHTFC = ReplaceableObject(
    'huawei_cm_3g."UPRACHTFC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CTFC",
    t1."GAINFACTORBETAC",
    t1."GAINFACTORBETAD",
    t1."LOGICRNCID",
    t1."PHYCHID",
    t1."POWEROFFSETPPM"
FROM
huawei_nbi_umts."UPRACHTFC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    t2."CTFC",
    t2."GAINFACTORBETAC",
    t2."GAINFACTORBETAD",
    NULL,
    t2."PHYCHID",
    t2."POWEROFFSETPPM"
FROM
huawei_mml_umts."UPRACHTFC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPSCH = ReplaceableObject(
    'huawei_cm_3g."UPSCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PHYCHID",
    t1."PSCHPOWER"
FROM
huawei_nbi_umts."UPSCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."PHYCHID",
    t2."PSCHPOWER"
FROM
huawei_mml_umts."UPSCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPSINACTTIMER = ReplaceableObject(
    'huawei_cm_3g."UPSINACTTIMER"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."PROTECTTMRFORBAC",
    t1."PROTECTTMRFORCON",
    t1."PROTECTTMRFORIMSSIG",
    t1."PROTECTTMRFORINT",
    t1."PROTECTTMRFORSTR",
    t1."PSINACTTMRFORBAC",
    t1."PSINACTTMRFORCON",
    t1."PSINACTTMRFORFSTDRMDCH",
    t1."PSINACTTMRFORFSTDRMFACH",
    t1."PSINACTTMRFORIMSSIG",
    t1."PSINACTTMRFORINT",
    t1."PSINACTTMRFORPREFSTDRM",
    t1."PSINACTTMRFORSTR"
FROM
huawei_nbi_umts."UPSINACTTIMER" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."PROTECTTMRFORBAC",
    t2."PROTECTTMRFORCON",
    t2."PROTECTTMRFORIMSSIG",
    t2."PROTECTTMRFORINT",
    t2."PROTECTTMRFORSTR",
    t2."PSINACTTMRFORBAC",
    t2."PSINACTTMRFORCON",
    t2."PSINACTTMRFORFSTDRMDCH",
    t2."PSINACTTMRFORFSTDRMFACH",
    t2."PSINACTTMRFORIMSSIG",
    t2."PSINACTTMRFORINT",
    t2."PSINACTTMRFORPREFSTDRM",
    t2."PSINACTTMRFORSTR"
FROM
huawei_mml_umts."UPSINACTTIMER" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UPTTSTATETRANS = ReplaceableObject(
    'huawei_cm_3g."UPTTSTATETRANS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."PTTCPC2EFACHSTATETRANSTIMER",
    t1."PTTCPC2FSTATETRANSTIMER",
    t1."PTTDH2EFACHSTATETRANSTIMER",
    t1."PTTDH2FSTATETRANSTIMER",
    t1."PTTDH2FTVMPTAT",
    t1."PTTDH2FTVMTHD",
    t1."PTTDH2FTVMTIMETOTRIG",
    t1."PTTE2FTHROUMEASPERIOD",
    t1."PTTE2FTHROUPTAT",
    t1."PTTE2FTHROUTHD",
    t1."PTTE2FTHROUTIMETOTRIG",
    t1."PTTEF2DHTVMTHD",
    t1."PTTEF2DHTVMTIMETOTRIG",
    t1."PTTF2DHTVMTHD",
    t1."PTTF2DHTVMTIMETOTRIG",
    t1."PTTF2PMCMODSWITCH",
    t1."PTTF2PSTATETRANSTIMER",
    t1."PTTF2PTVMPTAT",
    t1."PTTF2PTVMTHD",
    t1."PTTF2PTVMTIMETOTRIG"
FROM
huawei_nbi_umts."UPTTSTATETRANS" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."PTTCPC2EFACHSTATETRANSTIMER",
    t2."PTTCPC2FSTATETRANSTIMER",
    t2."PTTDH2EFACHSTATETRANSTIMER",
    t2."PTTDH2FSTATETRANSTIMER",
    t2."PTTDH2FTVMPTAT",
    t2."PTTDH2FTVMTHD",
    t2."PTTDH2FTVMTIMETOTRIG",
    t2."PTTE2FTHROUMEASPERIOD",
    t2."PTTE2FTHROUPTAT",
    t2."PTTE2FTHROUTHD",
    t2."PTTE2FTHROUTIMETOTRIG",
    t2."PTTEF2DHTVMTHD",
    t2."PTTEF2DHTVMTIMETOTRIG",
    t2."PTTF2DHTVMTHD",
    t2."PTTF2DHTVMTIMETOTRIG",
    t2."PTTF2PMCMODSWITCH",
    t2."PTTF2PSTATETRANSTIMER",
    t2."PTTF2PTVMPTAT",
    t2."PTTF2PTVMTHD",
    t2."PTTF2PTVMTIMETOTRIG"
FROM
huawei_mml_umts."UPTTSTATETRANS" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UQOSACT = ReplaceableObject(
    'huawei_cm_3g."UQOSACT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AMRQOSPERFORM",
    t1."BEDLACT1",
    t1."BEDLACT2",
    t1."BEDLACT3",
    t1."BEINTERIURRATEUPTIMER",
    t1."BEQOSPERFORM",
    t1."BEULACT1",
    t1."BEULACT2",
    t1."BEULACT3",
    t1."BEULEVTRIGIND",
    t1."BEULQOS5AMCSWITCH",
    t1."BEULQOS6A1MCSWITCH",
    t1."BEULQOS6DMCSWITCH",
    t1."BEULRATEADJTIMERLEN",
    t1."DRNCBEDLRLCQOSSWITCH",
    t1."LOGICRNCID",
    t1."SRNCBEDLRLCQOSSWITCH",
    t1."VPQOSPERFORM",
    t1."AMRULRATEADJTIMERLEN",
    t1."DLQOSAMRADJSWITCH",
    t1."DLQOSAMRINTERFREQHOSWITCH",
    t1."DLQOSAMRINTERRATHOSWITCH",
    t1."DLQOSWAMRADJSWITCH",
    t1."DLQOSWAMRINTERFREQHOSWITCH",
    t1."DLQOSWAMRINTERRATHOSWITCH",
    t1."ULQOSAMRADJSWITCH",
    t1."ULQOSAMRINTERFREQHOSWITCH",
    t1."ULQOSAMRINTERRATHOSWITCH",
    t1."ULQOSWAMRADJSWITCH",
    t1."ULQOSWAMRINTERFREQHOSWITCH",
    t1."ULQOSWAMRINTERRATHOSWITCH",
    t1."WAMRULRATEADJTIMERLEN"
FROM
huawei_nbi_umts."UQOSACT" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AMRQOSPERFORM",
    t2."BEDLACT1",
    t2."BEDLACT2",
    t2."BEDLACT3",
    t2."BEINTERIURRATEUPTIMER",
    t2."BEQOSPERFORM",
    t2."BEULACT1",
    t2."BEULACT2",
    t2."BEULACT3",
    t2."BEULEVTRIGIND",
    t2."BEULQOS5AMCSWITCH",
    t2."BEULQOS6A1MCSWITCH",
    t2."BEULQOS6DMCSWITCH",
    t2."BEULRATEADJTIMERLEN",
    t2."DRNCBEDLRLCQOSSWITCH",
    NULL,
    t2."SRNCBEDLRLCQOSSWITCH",
    t2."VPQOSPERFORM",
    t2."AMRULRATEADJTIMERLEN",
    t2."DLQOSAMRADJSWITCH",
    t2."DLQOSAMRINTERFREQHOSWITCH",
    t2."DLQOSAMRINTERRATHOSWITCH",
    t2."DLQOSWAMRADJSWITCH",
    t2."DLQOSWAMRINTERFREQHOSWITCH",
    t2."DLQOSWAMRINTERRATHOSWITCH",
    t2."ULQOSAMRADJSWITCH",
    t2."ULQOSAMRINTERFREQHOSWITCH",
    t2."ULQOSAMRINTERRATHOSWITCH",
    t2."ULQOSWAMRADJSWITCH",
    t2."ULQOSWAMRINTERFREQHOSWITCH",
    t2."ULQOSWAMRINTERRATHOSWITCH",
    t2."WAMRULRATEADJTIMERLEN"
FROM
huawei_mml_umts."UQOSACT" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UQOSALGOPARA = ReplaceableObject(
    'huawei_cm_3g."UQOSALGOPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."USERMATCHPRIORITY",
    t1."USERPOLICYSWITCH"
FROM
huawei_nbi_umts."UQOSALGOPARA" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID",
    NULL,
    t2."USERPOLICYSWITCH"
FROM
huawei_gexport_wcdma."UQOSALGOPARA_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID",
    NULL,
    t3."USERPOLICYSWITCH"
FROM
huawei_gexport_wcdma."UQOSALGOPARA_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."USERMATCHPRIORITY",
    t4."USERPOLICYSWITCH"
FROM
huawei_mml_umts."UQOSALGOPARA" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UQOSHO = ReplaceableObject(
    'huawei_cm_3g."UQOSHO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DLQOSMCTIMERLEN",
    t1."DLRSCPQOSHYST",
    t1."LOGICRNCID",
    t1."ULQOSMCTIMERLEN",
    t1."USEDFREQMEASQUANTITYFORQOS3A"
FROM
huawei_nbi_umts."UQOSHO" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."DLQOSMCTIMERLEN",
    t2."DLRSCPQOSHYST",
    NULL,
    t2."ULQOSMCTIMERLEN",
    t2."USEDFREQMEASQUANTITYFORQOS3A"
FROM
huawei_mml_umts."UQOSHO" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UQUALITYMEAS = ReplaceableObject(
    'huawei_cm_3g."UQUALITYMEAS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CHOICERPTUNITFORAMRE",
    t1."CHOICERPTUNITFORBEE",
    t1."CHOICERPTUNITFORBEF",
    t1."CHOICERPTUNITFORVPE",
    t1."DLAMRTRIGTIMEE",
    t1."DLBETRIGTIMEE",
    t1."DLBETRIGTIMEF",
    t1."DLMEASFILTERCOEF",
    t1."DLVPTRIGTIMEE",
    t1."LOGICRNCID",
    t1."TENMSECFORAMRE",
    t1."TENMSECFORBEE",
    t1."TENMSECFORBEF",
    t1."TENMSECFORVPE",
    t1."ULAMRTRIGTIME6A1",
    t1."ULAMRTRIGTIME6A2",
    t1."ULAMRTRIGTIME6B1",
    t1."ULAMRTRIGTIME6B2",
    t1."ULAMRTRIGTIME6D",
    t1."ULBETRIGTIME6A1",
    t1."ULBETRIGTIME6A2",
    t1."ULBETRIGTIME6B1",
    t1."ULBETRIGTIME6B2",
    t1."ULBETRIGTIME6D",
    t1."ULMEASFILTERCOEF",
    t1."ULVPTRIGTIME6A1",
    t1."ULVPTRIGTIME6B1",
    t1."ULVPTRIGTIME6D"
FROM
huawei_nbi_umts."UQUALITYMEAS" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CHOICERPTUNITFORAMRE",
    t2."CHOICERPTUNITFORBEE",
    t2."CHOICERPTUNITFORBEF",
    t2."CHOICERPTUNITFORVPE",
    t2."DLAMRTRIGTIMEE",
    t2."DLBETRIGTIMEE",
    t2."DLBETRIGTIMEF",
    t2."DLMEASFILTERCOEF",
    t2."DLVPTRIGTIMEE",
    NULL,
    t2."TENMSECFORAMRE",
    t2."TENMSECFORBEE",
    t2."TENMSECFORBEF",
    t2."TENMSECFORVPE",
    t2."ULAMRTRIGTIME6A1",
    t2."ULAMRTRIGTIME6A2",
    t2."ULAMRTRIGTIME6B1",
    t2."ULAMRTRIGTIME6B2",
    t2."ULAMRTRIGTIME6D",
    t2."ULBETRIGTIME6A1",
    t2."ULBETRIGTIME6A2",
    t2."ULBETRIGTIME6B1",
    t2."ULBETRIGTIME6B2",
    t2."ULBETRIGTIME6D",
    t2."ULMEASFILTERCOEF",
    t2."ULVPTRIGTIME6A1",
    t2."ULVPTRIGTIME6B1",
    t2."ULVPTRIGTIME6D"
FROM
huawei_mml_umts."UQUALITYMEAS" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UQUEUEPREEMPT = ReplaceableObject(
    'huawei_cm_3g."UQUEUEPREEMPT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CSP2DPREEMPTSWITCH",
    t1."EMCPREEREFVULNSWITCH",
    t1."LOGICRNCID",
    t1."MULTCODEPREEMPTALGOSWITCH",
    t1."PREEMPTALGOSWITCH",
    t1."PREEMPTENHSWITCH",
    t1."PREEMPTREFARPSWITCH",
    t1."PSBERRCPREEMPTVULNERABLE",
    t1."PTTPREEMPTALGOSWITCH",
    t1."PTUSERABSOLUTEPRIORITY",
    t1."QUEUEALGOSWITCH"
FROM
huawei_nbi_umts."UQUEUEPREEMPT" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CSP2DPREEMPTSWITCH",
    t2."EMCPREEREFVULNSWITCH",
    NULL,
    t2."MULTCODEPREEMPTALGOSWITCH",
    t2."PREEMPTALGOSWITCH",
    NULL,
    t2."PREEMPTREFARPSWITCH",
    t2."PSBERRCPREEMPTVULNERABLE",
    t2."PTTPREEMPTALGOSWITCH",
    t2."PTUSERABSOLUTEPRIORITY",
    t2."QUEUEALGOSWITCH"
FROM
huawei_mml_umts."UQUEUEPREEMPT" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URAC = ReplaceableObject(
    'huawei_cm_3g."URAC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPINDEX",
    t1."LAC",
    t1."LOGICRNCID",
    t1."PLMNVALTAGMAX",
    t1."PLMNVALTAGMIN",
    t1."RAC"
FROM
huawei_nbi_umts."URAC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNOPINDEX",
    t2."LAC",
    NULL,
    t2."PLMNVALTAGMAX",
    t2."PLMNVALTAGMIN",
    t2."RAC"
FROM
huawei_mml_umts."URAC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URACH = ReplaceableObject(
    'huawei_cm_3g."URACH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."MMAX",
    t1."NB01MAX",
    t1."NB01MIN",
    t1."PHYCHID",
    t1."RATEMATCHINGATTR",
    t1."TRCHID"
FROM
huawei_nbi_umts."URACH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."MMAX",
    t2."NB01MAX",
    t2."NB01MIN",
    t2."PHYCHID",
    t2."RATEMATCHINGATTR",
    t2."TRCHID"
FROM
huawei_mml_umts."URACH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URACHDYNTFS = ReplaceableObject(
    'huawei_cm_3g."URACHDYNTFS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."RLCSIZE",
    t1."TBNUMBER1",
    t1."TFSNUMBER",
    t1."TRCHID"
FROM
huawei_nbi_umts."URACHDYNTFS" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."RLCSIZE",
    t2."TBNUMBER1",
    t2."TFSNUMBER",
    t2."TRCHID"
FROM
huawei_mml_umts."URACHDYNTFS" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URACHMEASUREPARA = ReplaceableObject(
    'huawei_cm_3g."URACHMEASUREPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ECN0ADJSTEP",
    t1."ECN0ADJTIMERLEN",
    t1."ECN0MAXDOWNADJSTEP",
    t1."ECN0MAXUPADJSTEP",
    t1."LOGICRNCID",
    t1."MAXECN0VALUE",
    t1."MINECN0VALUE",
    t1."TAGETRLCRETRANS"
FROM
huawei_nbi_umts."URACHMEASUREPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ECN0ADJSTEP",
    t2."ECN0ADJTIMERLEN",
    t2."ECN0MAXDOWNADJSTEP",
    t2."ECN0MAXUPADJSTEP",
    NULL,
    t2."MAXECN0VALUE",
    t2."MINECN0VALUE",
    t2."TAGETRLCRETRANS"
FROM
huawei_mml_umts."URACHMEASUREPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UREDIRECTION = ReplaceableObject(
    'huawei_cm_3g."UREDIRECTION"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."REDIRSWITCH",
    t1."TRAFFICTYPE"
FROM
huawei_nbi_umts."UREDIRECTION" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."REDIRSWITCH",
    t2."TRAFFICTYPE"
FROM
huawei_mml_umts."UREDIRECTION" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URNCBASIC = ReplaceableObject(
    'huawei_cm_3g."URNCBASIC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOADSHARINGTYPE",
    t1."NSAP",
    t1."REDUNDANCYTYPE",
    t1."RNCID"
FROM
huawei_nbi_umts."URNCBASIC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."LOADSHARINGTYPE",
    t2."NSAP",
    t2."REDUNDANCYTYPE",
    t2."RNCID"
FROM
huawei_mml_umts."URNCBASIC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URNCCBPARA = ReplaceableObject(
    'huawei_cm_3g."URNCCBPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CBSWITCH",
    t1."CTCHSWITCH",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."URNCCBPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CBSWITCH",
    t2."CTCHSWITCH",
    NULL
FROM
huawei_mml_umts."URNCCBPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URNCCELLSHUTDOWNPARA = ReplaceableObject(
    'huawei_cm_3g."URNCCELLSHUTDOWNPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DYNCELLOPENJUDGETIMERLEN",
    t1."DYNCELLSHUTDOWNPROTECTTIMERLEN",
    t1."DYNCELLSHUTDOWNSWITCH",
    t1."IRATSHUTDOWNADJTIME",
    t1."IRATSWITCHONHYSTTIMELEN",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."URNCCELLSHUTDOWNPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."DYNCELLOPENJUDGETIMERLEN",
    t2."DYNCELLSHUTDOWNPROTECTTIMERLEN",
    t2."DYNCELLSHUTDOWNSWITCH",
    t2."IRATSHUTDOWNADJTIME",
    t2."IRATSWITCHONHYSTTIMELEN",
    NULL
FROM
huawei_mml_umts."URNCCELLSHUTDOWNPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URNCINPOOLRRMALGO = ReplaceableObject(
    'huawei_cm_3g."URNCINPOOLRRMALGO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."PARALLELDATASYNTHD"
FROM
huawei_nbi_umts."URNCINPOOLRRMALGO" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID",
    t2."PARALLELDATASYNTHD"
FROM
huawei_gexport_wcdma."URNCINPOOLRRMALGO_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID",
    t3."PARALLELDATASYNTHD"
FROM
huawei_gexport_wcdma."URNCINPOOLRRMALGO_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."PARALLELDATASYNTHD"
FROM
huawei_mml_umts."URNCINPOOLRRMALGO" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

URRCESTCAUSE = ReplaceableObject(
    'huawei_cm_3g."URRCESTCAUSE"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."EFACHSWITCH",
    t1."LOGICRNCID",
    t1."RRCCAUSE",
    t1."SIGCHTYPE"
FROM
huawei_nbi_umts."URRCESTCAUSE" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."EFACHSWITCH",
    NULL,
    t2."RRCCAUSE",
    t2."SIGCHTYPE"
FROM
huawei_mml_umts."URRCESTCAUSE" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

URRCTRLSWITCH = ReplaceableObject(
    'huawei_cm_3g."URRCTRLSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IUBPRIVATEINTERFACESWITCH",
    t1."LOGICRNCID",
    t1."PROCESSSWITCH",
    t1."PROCESSSWITCH2",
    t1."PROCESSSWITCH5"
FROM
huawei_nbi_umts."URRCTRLSWITCH" t1

"""
)

USAC = ReplaceableObject(
    'huawei_cm_3g."USAC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPINDEX",
    t1."LAC",
    t1."LOGICRNCID",
    t1."SAC"
FROM
huawei_nbi_umts."USAC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNOPINDEX",
    t2."LAC",
    NULL,
    t2."SAC"
FROM
huawei_mml_umts."USAC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USATLDCPERIOD = ReplaceableObject(
    'huawei_cm_3g."USATLDCPERIOD"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CLBPERIODTIMERLEN",
    t1."FAIRNESSPERIODTIMERLEN",
    t1."INTRAFREQLDBPERIODTIMERLEN",
    t1."INTRAFREQULBPERIODTIMERLEN",
    t1."LDRPERIODTIMERLEN",
    t1."LOGICRNCID",
    t1."OLCPERIODTIMERLEN",
    t1."PUCPERIODTIMERLEN"
FROM
huawei_nbi_umts."USATLDCPERIOD" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CLBPERIODTIMERLEN",
    t2."FAIRNESSPERIODTIMERLEN",
    t2."INTRAFREQLDBPERIODTIMERLEN",
    t2."INTRAFREQULBPERIODTIMERLEN",
    t2."LDRPERIODTIMERLEN",
    NULL,
    t2."OLCPERIODTIMERLEN",
    t2."PUCPERIODTIMERLEN"
FROM
huawei_mml_umts."USATLDCPERIOD" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USATLDM = ReplaceableObject(
    'huawei_cm_3g."USATLDM"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CHOICERPRTUNITFORDLBASICMEAS",
    t1."CHOICERPRTUNITFORDLOLCMEAS",
    t1."CHOICERPRTUNITFORHSDPAPWRMEAS",
    t1."CHOICERPRTUNITFORHSDPARATEMEAS",
    t1."CHOICERPRTUNITFORULBASICMEAS",
    t1."CHOICERPRTUNITFORULOLCMEAS",
    t1."DLBASICCOMMMEASFILTERCOEFF",
    t1."DLCACAVGFILTERLEN",
    t1."DLLDRAVGFILTERLEN",
    t1."DLOLCAVGFILTERLEN",
    t1."DLOLCMEASFILTERCOEFF",
    t1."DLOLCTRIGHYST",
    t1."HSDPANEEDPWRFILTERLEN",
    t1."HSDPAPRVIDBITRATEFILTERLEN",
    t1."LDBAVGFILTERLEN",
    t1."LOGICRNCID",
    t1."MAXMEASCONTINVALIDTIMES",
    t1."PERIODPROTECTTIMERCOEFF",
    t1."PUCAVGFILTERLEN",
    t1."TENMSECFORDLBASICMEAS",
    t1."TENMSECFORDLOLCMEAS",
    t1."TENMSECFORHSDPAPRVIDRATEMEAS",
    t1."TENMSECFORHSDPAPWRMEAS",
    t1."TENMSECFORULBASICMEAS",
    t1."TENMSECFORULOLCMEAS",
    t1."ULBASICCOMMMEASFILTERCOEFF",
    t1."ULBAVGFILTERLEN",
    t1."ULCACAVGFILTERLEN",
    t1."ULLDRAVGFILTERLEN",
    t1."ULOLCAVGFILTERLEN",
    t1."ULOLCMEASFILTERCOEFF",
    t1."ULOLCTRIGHYST"
FROM
huawei_nbi_umts."USATLDM" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CHOICERPRTUNITFORDLBASICMEAS",
    t2."CHOICERPRTUNITFORDLOLCMEAS",
    t2."CHOICERPRTUNITFORHSDPAPWRMEAS",
    t2."CHOICERPRTUNITFORHSDPARATEMEAS",
    t2."CHOICERPRTUNITFORULBASICMEAS",
    t2."CHOICERPRTUNITFORULOLCMEAS",
    t2."DLBASICCOMMMEASFILTERCOEFF",
    t2."DLCACAVGFILTERLEN",
    t2."DLLDRAVGFILTERLEN",
    t2."DLOLCAVGFILTERLEN",
    t2."DLOLCMEASFILTERCOEFF",
    t2."DLOLCTRIGHYST",
    t2."HSDPANEEDPWRFILTERLEN",
    t2."HSDPAPRVIDBITRATEFILTERLEN",
    t2."LDBAVGFILTERLEN",
    NULL,
    t2."MAXMEASCONTINVALIDTIMES",
    t2."PERIODPROTECTTIMERCOEFF",
    t2."PUCAVGFILTERLEN",
    t2."TENMSECFORDLBASICMEAS",
    t2."TENMSECFORDLOLCMEAS",
    t2."TENMSECFORHSDPAPRVIDRATEMEAS",
    t2."TENMSECFORHSDPAPWRMEAS",
    t2."TENMSECFORULBASICMEAS",
    t2."TENMSECFORULOLCMEAS",
    t2."ULBASICCOMMMEASFILTERCOEFF",
    t2."ULBAVGFILTERLEN",
    t2."ULCACAVGFILTERLEN",
    t2."ULLDRAVGFILTERLEN",
    t2."ULOLCAVGFILTERLEN",
    t2."ULOLCMEASFILTERCOEFF",
    t2."ULOLCTRIGHYST"
FROM
huawei_mml_umts."USATLDM" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USCCPCHBASIC = ReplaceableObject(
    'huawei_cm_3g."USCCPCHBASIC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ACTSTATUS",
    t1."CELLID",
    t1."CTFCSIZE",
    t1."LOGICRNCID",
    t1."PHYCHID",
    t1."SCCPCHOFFSET",
    t1."SCRAMBCODE",
    t1."SLOTFORMAT",
    t1."STTDIND",
    t1."TFCIPRESENCE"
FROM
huawei_nbi_umts."USCCPCHBASIC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."CELLID",
    t2."CTFCSIZE",
    NULL,
    t2."PHYCHID",
    t2."SCCPCHOFFSET",
    t2."SCRAMBCODE",
    t2."SLOTFORMAT",
    t2."STTDIND",
    t2."TFCIPRESENCE"
FROM
huawei_mml_umts."USCCPCHBASIC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USCCPCHTFC = ReplaceableObject(
    'huawei_cm_3g."USCCPCHTFC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."CTFC",
    t1."LOGICRNCID",
    t1."PHYCHID"
FROM
huawei_nbi_umts."USCCPCHTFC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    t2."CTFC",
    NULL,
    t2."PHYCHID"
FROM
huawei_mml_umts."USCCPCHTFC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USCHEDULEPRIOMAP = ReplaceableObject(
    'huawei_cm_3g."USCHEDULEPRIOMAP"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."SPI",
    t1."THPCLASS",
    t1."TRAFFICCLASS",
    t1."USERPRIORITY"
FROM
huawei_nbi_umts."USCHEDULEPRIOMAP" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."SPI",
    t2."THPCLASS",
    t2."TRAFFICCLASS",
    t2."USERPRIORITY"
FROM
huawei_mml_umts."USCHEDULEPRIOMAP" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USERVMEAPARA = ReplaceableObject(
    'huawei_cm_3g."USERVMEAPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."SERVMEATYPE"
FROM
huawei_nbi_umts."USERVMEAPARA" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_wcdma."USERVMEAPARA_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_wcdma."USERVMEAPARA_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL
FROM
huawei_mml_umts."USERVMEAPARA" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

USMLC = ReplaceableObject(
    'huawei_cm_3g."USMLC"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AGPSADDASSDATASENDFLAG",
    t1."AGPSMETHODTYPE",
    t1."CELLIDRTTMETHODTYPE",
    t1."EMERGLCSSWITCH",
    t1."FORCEDSHOSWITCH",
    t1."IUPCRSPTIMERLEN",
    t1."LCSWORKMODE",
    t1."LOGICRNCID",
    t1."MAXGPSSATS",
    t1."OPTIONALIESENDSWITCH",
    t1."OTDOAMETHODTYPE",
    t1."RESULTGEOTYPE",
    t1."SMLCMETHOD",
    t1."UEASSAGPSASSDATASWITCH",
    t1."UEBASAGPSASSDATASWITCH"
FROM
huawei_nbi_umts."USMLC" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AGPSADDASSDATASENDFLAG",
    t2."AGPSMETHODTYPE",
    t2."CELLIDRTTMETHODTYPE",
    t2."EMERGLCSSWITCH",
    t2."FORCEDSHOSWITCH",
    t2."IUPCRSPTIMERLEN",
    t2."LCSWORKMODE",
    NULL,
    t2."MAXGPSSATS",
    NULL,
    t2."OTDOAMETHODTYPE",
    t2."RESULTGEOTYPE",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."USMLC" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USMLCCELL = ReplaceableObject(
    'huawei_cm_3g."USMLCCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AGPSACTIVATEFLAG",
    t1."ANTENNAALTITUDEMETER",
    t1."ANTENNALATITUDEDEGREE",
    t1."ANTENNALONGITUDEDEGREE",
    t1."ANTENNAOPENING",
    t1."ANTENNAORIENTATION",
    t1."CELLAVERAGEHEIGHT",
    t1."CELLENVIRONMENT",
    t1."CELLHEIGHTSTD",
    t1."CELLID",
    t1."CELLIDRTTACTIVATEFLAG",
    t1."CELLLOCCFGTYPE",
    t1."GCDF",
    t1."LOGICRNCID",
    t1."MAXANTENNARANGE",
    t1."MTRLGY",
    t1."OTDOAACTIVATEFLAG",
    t1."RNCID"
FROM
huawei_nbi_umts."USMLCCELL" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."AGPSACTIVATEFLAG",
    t2."ANTENNAALTITUDEMETER",
    t2."ANTENNALATITUDEDEGREE",
    t2."ANTENNALONGITUDEDEGREE",
    t2."ANTENNAOPENING",
    t2."ANTENNAORIENTATION",
    t2."CELLAVERAGEHEIGHT",
    t2."CELLENVIRONMENT",
    t2."CELLHEIGHTSTD",
    t2."CELLID",
    t2."CELLIDRTTACTIVATEFLAG",
    t2."CELLLOCCFGTYPE",
    t2."GCDF",
    NULL,
    t2."MAXANTENNARANGE",
    t2."MTRLGY",
    t2."OTDOAACTIVATEFLAG",
    t2."RNCID"
FROM
huawei_mml_umts."USMLCCELL" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USMLCEXT3GCELL = ReplaceableObject(
    'huawei_cm_3g."USMLCEXT3GCELL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."AGPSACTIVATEFLAG",
    t1."ANTENNAALTITUDEMETER",
    t1."ANTENNALATITUDEDEGREE",
    t1."ANTENNALONGITUDEDEGREE",
    t1."ANTENNAOPENING",
    t1."ANTENNAORIENTATION",
    t1."CELLAVERAGEHEIGHT",
    t1."CELLENVIRONMENT",
    t1."CELLHEIGHTSTD",
    t1."CELLID",
    t1."CELLIDRTTACTIVATEFLAG",
    t1."CELLLOCCFGTYPE",
    t1."GCDF",
    t1."LOGICRNCID",
    t1."MAXANTENNARANGE",
    t1."MTRLGY",
    t1."NRNCID",
    t1."OTDOAACTIVATEFLAG",
    t1."RXTXCHANDELAY",
    t1."TXCHANDELAY"
FROM
huawei_nbi_umts."USMLCEXT3GCELL" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."AGPSACTIVATEFLAG",
    t2."ANTENNAALTITUDEMETER",
    t2."ANTENNALATITUDEDEGREE",
    t2."ANTENNALONGITUDEDEGREE",
    t2."ANTENNAOPENING",
    t2."ANTENNAORIENTATION",
    t2."CELLAVERAGEHEIGHT",
    t2."CELLENVIRONMENT",
    t2."CELLHEIGHTSTD",
    t2."CELLID",
    t2."CELLIDRTTACTIVATEFLAG",
    t2."CELLLOCCFGTYPE",
    t2."GCDF",
    t2."LOGICRNCID",
    t2."MAXANTENNARANGE",
    t2."MTRLGY",
    t2."NRNCID",
    t2."OTDOAACTIVATEFLAG",
    t2."RXTXCHANDELAY",
    t2."TXCHANDELAY"
FROM
huawei_gexport_wcdma."USMLCEXT3GCELL_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."AGPSACTIVATEFLAG",
    t3."ANTENNAALTITUDEMETER",
    t3."ANTENNALATITUDEDEGREE",
    t3."ANTENNALONGITUDEDEGREE",
    t3."ANTENNAOPENING",
    t3."ANTENNAORIENTATION",
    t3."CELLAVERAGEHEIGHT",
    t3."CELLENVIRONMENT",
    t3."CELLHEIGHTSTD",
    t3."CELLID",
    t3."CELLIDRTTACTIVATEFLAG",
    t3."CELLLOCCFGTYPE",
    t3."GCDF",
    t3."LOGICRNCID",
    t3."MAXANTENNARANGE",
    t3."MTRLGY",
    t3."NRNCID",
    t3."OTDOAACTIVATEFLAG",
    t3."RXTXCHANDELAY",
    t3."TXCHANDELAY"
FROM
huawei_gexport_wcdma."USMLCEXT3GCELL_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."AGPSACTIVATEFLAG",
    t4."ANTENNAALTITUDEMETER",
    t4."ANTENNALATITUDEDEGREE",
    t4."ANTENNALONGITUDEDEGREE",
    t4."ANTENNAOPENING",
    t4."ANTENNAORIENTATION",
    t4."CELLAVERAGEHEIGHT",
    t4."CELLENVIRONMENT",
    t4."CELLHEIGHTSTD",
    t4."CELLID",
    t4."CELLIDRTTACTIVATEFLAG",
    t4."CELLLOCCFGTYPE",
    t4."GCDF",
    NULL,
    t4."MAXANTENNARANGE",
    t4."MTRLGY",
    t4."NRNCID",
    t4."OTDOAACTIVATEFLAG",
    t4."RXTXCHANDELAY",
    t4."TXCHANDELAY"
FROM
huawei_mml_umts."USMLCEXT3GCELL" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

USPG = ReplaceableObject(
    'huawei_cm_3g."USPG"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."PRIORITYSERVICEFOREXTRAB",
    t1."PRIORITYSERVICEFORHSDPA",
    t1."PRIORITYSERVICEFORHSPART",
    t1."PRIORITYSERVICEFORHSUPA",
    t1."PRIORITYSERVICEFORR99NRT",
    t1."PRIORITYSERVICEFORR99RT",
    t1."SPGID"
FROM
huawei_nbi_umts."USPG" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."PRIORITYSERVICEFOREXTRAB",
    t2."PRIORITYSERVICEFORHSDPA",
    t2."PRIORITYSERVICEFORHSPART",
    t2."PRIORITYSERVICEFORHSUPA",
    t2."PRIORITYSERVICEFORR99NRT",
    t2."PRIORITYSERVICEFORR99RT",
    t2."SPGID"
FROM
huawei_mml_umts."USPG" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USPIWEIGHT = ReplaceableObject(
    'huawei_cm_3g."USPIWEIGHT"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."RATERANGESPIWEIGHTIND",
    t1."SPI",
    t1."SPIWEIGHT",
    t1."SPIWTFACTORFORHSUPASHO"
FROM
huawei_nbi_umts."USPIWEIGHT" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."RATERANGESPIWEIGHTIND",
    t2."SPI",
    t2."SPIWEIGHT",
    t2."SPIWTFACTORFORHSUPASHO"
FROM
huawei_mml_umts."USPIWEIGHT" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USRBRATECOVSEL = ReplaceableObject(
    'huawei_cm_3g."USRBRATECOVSEL"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CSP2DSRBRATEBADECNOTHD",
    t1."CSP2DSRBRATEGOODECNOTHD",
    t1."LOGICRNCID",
    t1."R6UESRBHIGHRATECFGSWITCH",
    t1."RRCSETSRBRATEBADECNOTHD",
    t1."RRCSETSRBRATEGOODECNOTHD",
    t1."RRCSETUPSRBRATESELSET",
    t1."SRBRATECOVSELSWITCH"
FROM
huawei_nbi_umts."USRBRATECOVSEL" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."CSP2DSRBRATEBADECNOTHD",
    t2."CSP2DSRBRATEGOODECNOTHD",
    t2."LOGICRNCID",
    t2."R6UESRBHIGHRATECFGSWITCH",
    t2."RRCSETSRBRATEBADECNOTHD",
    t2."RRCSETSRBRATEGOODECNOTHD",
    NULL,
    t2."SRBRATECOVSELSWITCH"
FROM
huawei_gexport_wcdma."USRBRATECOVSEL_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."CSP2DSRBRATEBADECNOTHD",
    t3."CSP2DSRBRATEGOODECNOTHD",
    t3."LOGICRNCID",
    t3."R6UESRBHIGHRATECFGSWITCH",
    t3."RRCSETSRBRATEBADECNOTHD",
    t3."RRCSETSRBRATEGOODECNOTHD",
    NULL,
    t3."SRBRATECOVSELSWITCH"
FROM
huawei_gexport_wcdma."USRBRATECOVSEL_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."CSP2DSRBRATEBADECNOTHD",
    t4."CSP2DSRBRATEGOODECNOTHD",
    NULL,
    t4."R6UESRBHIGHRATECFGSWITCH",
    t4."RRCSETSRBRATEBADECNOTHD",
    t4."RRCSETSRBRATEGOODECNOTHD",
    NULL,
    t4."SRBRATECOVSELSWITCH"
FROM
huawei_mml_umts."USRBRATECOVSEL" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

USRNSR = ReplaceableObject(
    'huawei_cm_3g."USRNSR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."SRNSRABCNDOMAINTYPE",
    t1."SRNSRDELAYOFFSET",
    t1."SRNSREXPIRYTIME",
    t1."SRNSRIURRESELECTTIMERLEN",
    t1."SRNSRSEPARATEDURATION",
    t1."SRNSRTRIGTIMER"
FROM
huawei_nbi_umts."USRNSR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."SRNSRABCNDOMAINTYPE",
    t2."SRNSRDELAYOFFSET",
    t2."SRNSREXPIRYTIME",
    t2."SRNSRIURRESELECTTIMERLEN",
    t2."SRNSRSEPARATEDURATION",
    t2."SRNSRTRIGTIMER"
FROM
huawei_mml_umts."USRNSR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USSCH = ReplaceableObject(
    'huawei_cm_3g."USSCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CELLID",
    t1."LOGICRNCID",
    t1."PHYCHID",
    t1."SSCHPOWER"
FROM
huawei_nbi_umts."USSCH" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CELLID",
    NULL,
    t2."PHYCHID",
    t2."SSCHPOWER"
FROM
huawei_mml_umts."USSCH" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

USTATETIMER = ReplaceableObject(
    'huawei_cm_3g."USTATETIMER"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CMCHRSRCRSPTMR",
    t1."CSFBUEDELAYRAUTIMER",
    t1."DRLAAL2ESTINDTMR",
    t1."DRLRECFGCMITTMR",
    t1."F2PDELRLCTMR",
    t1."HOASUTMR",
    t1."HOCELLUPDATERSPTMR",
    t1."HOPAGINGRSPTMR",
    t1."HOPHYCHRECFGTMR",
    t1."HORELOCREQTMR",
    t1."HOWTTRCHRECFGRSPTMR",
    t1."IUCSRELNORABTMR",
    t1."IUPSRELNORABTMR",
    t1."LOGICRNCID",
    t1."LOWRRCCONNREJWAITTMR",
    t1."RBRECFGRSPTMR",
    t1."RBRELRSPTMR",
    t1."RBSETUPRSPTMR",
    t1."RELOCANOTHERTMR",
    t1."RELOCCMDTMR",
    t1."RELOCCOMMITTMR",
    t1."RELOCDATAFWDTMR",
    t1."RELOCFAILIURELCMDTMR",
    t1."RELOCIURELCMDTMR",
    t1."RELOCMOBILCONFTMR",
    t1."RELOCPHYCHRECFGTMR",
    t1."RELOCUTRANHOCMPTMR",
    t1."RLRECFGREADYTMR",
    t1."RLRELRSPTMR",
    t1."RLRSTRTMR",
    t1."RLSETUPRSPTMR",
    t1."RRCCONNREJWAITTMR",
    t1."RRCINITDTTMR",
    t1."RRCIURELCMDTMR",
    t1."RRCPAINGTYPE1TMR",
    t1."RRCRELRETRANTMR",
    t1."RRCRLCACKCMPTMR",
    t1."RRCSECRTMODECMPTMR",
    t1."RRCUERSPTMR",
    t1."SYSHOPSRESUMETMR",
    t1."TTHDFORSFSTUSERIDENTIFY",
    t1."UECAPENQRSPTMR",
    t1."UECNTCHECKRSPTMR"
FROM
huawei_nbi_umts."USTATETIMER" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CMCHRSRCRSPTMR",
    t2."CSFBUEDELAYRAUTIMER",
    t2."DRLAAL2ESTINDTMR",
    t2."DRLRECFGCMITTMR",
    t2."F2PDELRLCTMR",
    t2."HOASUTMR",
    t2."HOCELLUPDATERSPTMR",
    t2."HOPAGINGRSPTMR",
    t2."HOPHYCHRECFGTMR",
    t2."HORELOCREQTMR",
    t2."HOWTTRCHRECFGRSPTMR",
    t2."IUCSRELNORABTMR",
    t2."IUPSRELNORABTMR",
    NULL,
    t2."LOWRRCCONNREJWAITTMR",
    t2."RBRECFGRSPTMR",
    t2."RBRELRSPTMR",
    t2."RBSETUPRSPTMR",
    t2."RELOCANOTHERTMR",
    t2."RELOCCMDTMR",
    t2."RELOCCOMMITTMR",
    t2."RELOCDATAFWDTMR",
    t2."RELOCFAILIURELCMDTMR",
    t2."RELOCIURELCMDTMR",
    t2."RELOCMOBILCONFTMR",
    t2."RELOCPHYCHRECFGTMR",
    t2."RELOCUTRANHOCMPTMR",
    t2."RLRECFGREADYTMR",
    t2."RLRELRSPTMR",
    t2."RLRSTRTMR",
    t2."RLSETUPRSPTMR",
    t2."RRCCONNREJWAITTMR",
    t2."RRCINITDTTMR",
    t2."RRCIURELCMDTMR",
    t2."RRCPAINGTYPE1TMR",
    t2."RRCRELRETRANTMR",
    t2."RRCRLCACKCMPTMR",
    t2."RRCSECRTMODECMPTMR",
    t2."RRCUERSPTMR",
    t2."SYSHOPSRESUMETMR",
    t2."TTHDFORSFSTUSERIDENTIFY",
    t2."UECAPENQRSPTMR",
    t2."UECNTCHECKRSPTMR"
FROM
huawei_mml_umts."USTATETIMER" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UTHPCLASS = ReplaceableObject(
    'huawei_cm_3g."UTHPCLASS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."THP10CLASS",
    t1."THP11CLASS",
    t1."THP12CLASS",
    t1."THP13CLASS",
    t1."THP14CLASS",
    t1."THP15CLASS",
    t1."THP1CLASS",
    t1."THP2CLASS",
    t1."THP3CLASS",
    t1."THP4CLASS",
    t1."THP5CLASS",
    t1."THP6CLASS",
    t1."THP7CLASS",
    t1."THP8CLASS",
    t1."THP9CLASS"
FROM
huawei_nbi_umts."UTHPCLASS" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."THP10CLASS",
    t2."THP11CLASS",
    t2."THP12CLASS",
    t2."THP13CLASS",
    t2."THP14CLASS",
    t2."THP15CLASS",
    t2."THP1CLASS",
    t2."THP2CLASS",
    t2."THP3CLASS",
    t2."THP4CLASS",
    t2."THP5CLASS",
    t2."THP6CLASS",
    t2."THP7CLASS",
    t2."THP8CLASS",
    t2."THP9CLASS"
FROM
huawei_mml_umts."UTHPCLASS" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UU2LTEHOCOV = ReplaceableObject(
    'huawei_cm_3g."UU2LTEHOCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."LTEPERIODREPORTINTERVAL",
    t1."LTEREPORTMODE",
    t1."PENALTYTIMEFORPHYCHFAIL",
    t1."TARGETRATTHDRSRP",
    t1."TARGETRATTHDRSRQ",
    t1."U2LPHYCHFAILNUM",
    t1."U2LTEHO2DEVENTTYPE",
    t1."U2LTEMEASTIME"
FROM
huawei_nbi_umts."UU2LTEHOCOV" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."LOGICRNCID",
    t2."LTEPERIODREPORTINTERVAL",
    t2."LTEREPORTMODE",
    t2."PENALTYTIMEFORPHYCHFAIL",
    t2."TARGETRATTHDRSRP",
    t2."TARGETRATTHDRSRQ",
    t2."U2LPHYCHFAILNUM",
    t2."U2LTEHO2DEVENTTYPE",
    t2."U2LTEMEASTIME"
FROM
huawei_gexport_wcdma."UU2LTEHOCOV_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."LOGICRNCID",
    t3."LTEPERIODREPORTINTERVAL",
    t3."LTEREPORTMODE",
    t3."PENALTYTIMEFORPHYCHFAIL",
    t3."TARGETRATTHDRSRP",
    t3."TARGETRATTHDRSRQ",
    t3."U2LPHYCHFAILNUM",
    t3."U2LTEHO2DEVENTTYPE",
    t3."U2LTEMEASTIME"
FROM
huawei_gexport_wcdma."UU2LTEHOCOV_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t4."LTEPERIODREPORTINTERVAL",
    t4."LTEREPORTMODE",
    t4."PENALTYTIMEFORPHYCHFAIL",
    t4."TARGETRATTHDRSRP",
    t4."TARGETRATTHDRSRQ",
    t4."U2LPHYCHFAILNUM",
    t4."U2LTEHO2DEVENTTYPE",
    t4."U2LTEMEASTIME"
FROM
huawei_mml_umts."UU2LTEHOCOV" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UU2LTEHONCOV = ReplaceableObject(
    'huawei_cm_3g."UU2LTEHONCOV"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ANTIPINPANLTEFDDREDRSWITCH",
    t1."BESTCELLTRIGLTEMEASSWITCH",
    t1."HYSTFOR3C",
    t1."LOGICRNCID",
    t1."LTEMEASQUANOF3C",
    t1."LTEMEASTYPOF3C",
    t1."PENALTYTIMEFORPHYCHFAIL",
    t1."TARGETRATTHDRSRP",
    t1."TARGETRATTHDRSRQ",
    t1."TRIGTIME3C",
    t1."U2LNCOVRSCPPRDTIMER",
    t1."U2LNCOVRSCPTHD",
    t1."U2LPHYCHFAILNUM",
    t1."U2LPUNISHSWITCH",
    t1."U2LPUNISHTIMER",
    t1."U2LSERVMCTIMEOUTPUNISHTIME",
    t1."U2LSERVPRDTRIGTIMERLEN",
    t1."U2LSERVTRIGSOURCE",
    t1."U2LTEFILTERCOEF",
    t1."U2LTEMEASTIME"
FROM
huawei_nbi_umts."UU2LTEHONCOV" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ANTIPINPANLTEFDDREDRSWITCH",
    t2."BESTCELLTRIGLTEMEASSWITCH",
    t2."HYSTFOR3C",
    NULL,
    t2."LTEMEASQUANOF3C",
    t2."LTEMEASTYPOF3C",
    t2."PENALTYTIMEFORPHYCHFAIL",
    t2."TARGETRATTHDRSRP",
    t2."TARGETRATTHDRSRQ",
    t2."TRIGTIME3C",
    t2."U2LNCOVRSCPPRDTIMER",
    t2."U2LNCOVRSCPTHD",
    t2."U2LPHYCHFAILNUM",
    t2."U2LPUNISHSWITCH",
    t2."U2LPUNISHTIMER",
    t2."U2LSERVMCTIMEOUTPUNISHTIME",
    t2."U2LSERVPRDTRIGTIMERLEN",
    NULL,
    t2."U2LTEFILTERCOEF",
    t2."U2LTEMEASTIME"
FROM
huawei_mml_umts."UU2LTEHONCOV" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUEA = ReplaceableObject(
    'huawei_cm_3g."UUEA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ENCRYPTIONALGO",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UUEA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_umts."UUEA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUESTATETRANS = ReplaceableObject(
    'huawei_cm_3g."UUESTATETRANS"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BASEDTIMEF2DPT",
    t1."BASEDTIMEF2DTHD",
    t1."BEEFACH2CPCTVMTHD",
    t1."BEEFACH2CPCTVMTIMETOTRIG",
    t1."BEEFACH2DTVMTHD",
    t1."BEEFACH2DTVMTIMETOTRIG",
    t1."BEEFACH2HTVMTHD",
    t1."BEEFACH2HTVMTIMETOTRIG",
    t1."BEERACH2CPCDLTVMTHD",
    t1."BEERACH2CPCULTVMTHD",
    t1."BEERACH2DTVMTHD",
    t1."BEERACH2EULTVMTHD",
    t1."BEERACH2HDLTVMTHD",
    t1."BEF2CPCETVMTHD",
    t1."BEF2CPCETVMTIMETOTRIG",
    t1."BEF2CPCHTVMTHD",
    t1."BEF2CPCHTVMTIMETOTRIG",
    t1."BEF2DHTVMTHDFORFACHCONG",
    t1."BEF2DTVMTHD",
    t1."BEF2DTVMTIMETOTRIG",
    t1."BEF2ETVMTHD",
    t1."BEF2ETVMTIMETOTRIG",
    t1."BEF2HTVMTHD",
    t1."BEF2HTVMTIMETOTRIG",
    t1."BEH2FTVMPTAT",
    t1."BEH2FTVMTHD",
    t1."BEH2FTVMTIMETOTRIG",
    t1."CELLRESELECTCOUNTER",
    t1."D2F2PTVMTHD",
    t1."D2FTVMPTAT",
    t1."D2FTVMTIMETOTRIG",
    t1."E2FTHROUMEASPERIOD",
    t1."E2FTHROUPTAT",
    t1."E2FTHROUTHD",
    t1."E2FTHROUTIMETOTRIG",
    t1."F2PTVMPTAT",
    t1."F2PTVMTIMETOTRIG",
    t1."FASTDORMANCYF2DHTVMTHD",
    t1."FDERACH2DULTVMTHD",
    t1."LOGICRNCID",
    t1."PARKINGBEF2DHTVMTHD",
    t1."PARKINGBEF2PTVMTHD",
    t1."PARKINGF2DHTVMPTAT",
    t1."PARKINGF2DHTVMTXIAT",
    t1."RTDH2FTVMPTAT",
    t1."RTDH2FTVMTHD",
    t1."RTDH2FTVMTIMETOTRIG",
    t1."RTEFACH2CPCTVMTHD",
    t1."RTEFACH2CPCTVMTIMETOTRIG",
    t1."RTEFACH2DHTVMTHD",
    t1."RTEFACH2DHTVMTIMETOTRIG",
    t1."RTF2CPCTVMTHD",
    t1."RTF2CPCTVMTIMETOTRIG",
    t1."RTF2DHTVMTHD",
    t1."RTF2DHTVMTIMETOTRIG",
    t1."TVMTHDFORSMARTP2D",
    t1."TXINTERRUPTAFTERTRIG"
FROM
huawei_nbi_umts."UUESTATETRANS" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BASEDTIMEF2DPT",
    t2."BASEDTIMEF2DTHD",
    t2."BEEFACH2CPCTVMTHD",
    t2."BEEFACH2CPCTVMTIMETOTRIG",
    t2."BEEFACH2DTVMTHD",
    t2."BEEFACH2DTVMTIMETOTRIG",
    t2."BEEFACH2HTVMTHD",
    t2."BEEFACH2HTVMTIMETOTRIG",
    t2."BEERACH2CPCDLTVMTHD",
    t2."BEERACH2CPCULTVMTHD",
    t2."BEERACH2DTVMTHD",
    t2."BEERACH2EULTVMTHD",
    t2."BEERACH2HDLTVMTHD",
    t2."BEF2CPCETVMTHD",
    t2."BEF2CPCETVMTIMETOTRIG",
    t2."BEF2CPCHTVMTHD",
    t2."BEF2CPCHTVMTIMETOTRIG",
    t2."BEF2DHTVMTHDFORFACHCONG",
    t2."BEF2DTVMTHD",
    t2."BEF2DTVMTIMETOTRIG",
    t2."BEF2ETVMTHD",
    t2."BEF2ETVMTIMETOTRIG",
    t2."BEF2HTVMTHD",
    t2."BEF2HTVMTIMETOTRIG",
    t2."BEH2FTVMPTAT",
    t2."BEH2FTVMTHD",
    t2."BEH2FTVMTIMETOTRIG",
    t2."CELLRESELECTCOUNTER",
    t2."D2F2PTVMTHD",
    t2."D2FTVMPTAT",
    t2."D2FTVMTIMETOTRIG",
    t2."E2FTHROUMEASPERIOD",
    t2."E2FTHROUPTAT",
    t2."E2FTHROUTHD",
    t2."E2FTHROUTIMETOTRIG",
    t2."F2PTVMPTAT",
    t2."F2PTVMTIMETOTRIG",
    t2."FASTDORMANCYF2DHTVMTHD",
    t2."FDERACH2DULTVMTHD",
    NULL,
    t2."PARKINGBEF2DHTVMTHD",
    t2."PARKINGBEF2PTVMTHD",
    t2."PARKINGF2DHTVMPTAT",
    t2."PARKINGF2DHTVMTXIAT",
    t2."RTDH2FTVMPTAT",
    t2."RTDH2FTVMTHD",
    t2."RTDH2FTVMTIMETOTRIG",
    t2."RTEFACH2CPCTVMTHD",
    t2."RTEFACH2CPCTVMTIMETOTRIG",
    t2."RTEFACH2DHTVMTHD",
    t2."RTEFACH2DHTVMTIMETOTRIG",
    t2."RTF2CPCTVMTHD",
    t2."RTF2CPCTVMTIMETOTRIG",
    t2."RTF2DHTVMTHD",
    t2."RTF2DHTVMTIMETOTRIG",
    t2."TVMTHDFORSMARTP2D",
    t2."TXINTERRUPTAFTERTRIG"
FROM
huawei_mml_umts."UUESTATETRANS" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUESTATETRANSTIMER = ReplaceableObject(
    'huawei_cm_3g."UUESTATETRANSTIMER"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BECPC2EFACHSTATETRANSTIMER",
    t1."BECPC2FSTATETRANSTIMER",
    t1."BED2EFACHSTATETRANSTIMER",
    t1."BED2FSTATETRANSTIMER",
    t1."BEE2FSTATETRANSTIMER",
    t1."BEF2PSTATETRANSTIMER",
    t1."BEH2EFACHSTATETRANSTIMER",
    t1."BEH2FSTATETRANSTIMER",
    t1."CELLRESELECTTIMER",
    t1."D2PPSINACTTIMER",
    t1."LOGICRNCID",
    t1."PARKING4ADISCARDTIMER",
    t1."RTCPC2EFACHSTATETRANSTIMER",
    t1."RTCPC2FSTATETRANSTIMER",
    t1."RTDH2EFACHSTATETRANSTIMER",
    t1."RTDH2FSTATETRANSTIMER"
FROM
huawei_nbi_umts."UUESTATETRANSTIMER" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BECPC2EFACHSTATETRANSTIMER",
    t2."BECPC2FSTATETRANSTIMER",
    t2."BED2EFACHSTATETRANSTIMER",
    t2."BED2FSTATETRANSTIMER",
    t2."BEE2FSTATETRANSTIMER",
    t2."BEF2PSTATETRANSTIMER",
    t2."BEH2EFACHSTATETRANSTIMER",
    t2."BEH2FSTATETRANSTIMER",
    t2."CELLRESELECTTIMER",
    t2."D2PPSINACTTIMER",
    NULL,
    t2."PARKING4ADISCARDTIMER",
    t2."RTCPC2EFACHSTATETRANSTIMER",
    t2."RTCPC2FSTATETRANSTIMER",
    t2."RTDH2EFACHSTATETRANSTIMER",
    t2."RTDH2FSTATETRANSTIMER"
FROM
huawei_mml_umts."UUESTATETRANSTIMER" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUIA = ReplaceableObject(
    'huawei_cm_3g."UUIA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."INTEGRITYPROTECTALGO",
    t1."LOGICRNCID"
FROM
huawei_nbi_umts."UUIA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."INTEGRITYPROTECTALGO",
    NULL
FROM
huawei_mml_umts."UUIA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUPALGOSWITCH = ReplaceableObject(
    'huawei_cm_3g."UUPALGOSWITCH"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."DPISOURCEPRIO",
    t1."LOGICRNCID",
    t1."QOSPOLICYSWITCH"
FROM
huawei_nbi_umts."UUPALGOSWITCH" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."DPISOURCEPRIO",
    t2."LOGICRNCID",
    NULL
FROM
huawei_gexport_wcdma."UUPALGOSWITCH_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."DPISOURCEPRIO",
    t3."LOGICRNCID",
    NULL
FROM
huawei_gexport_wcdma."UUPALGOSWITCH_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."DPISOURCEPRIO",
    NULL,
    NULL
FROM
huawei_mml_umts."UUPALGOSWITCH" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UURA = ReplaceableObject(
    'huawei_cm_3g."UURA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CNOPINDEX",
    t1."LOGICRNCID",
    t1."URAID"
FROM
huawei_nbi_umts."UURA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CNOPINDEX",
    NULL,
    t2."URAID"
FROM
huawei_mml_umts."UURA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUSERGBR = ReplaceableObject(
    'huawei_cm_3g."UUSERGBR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BEARTYPE",
    t1."DLGBR",
    t1."LOGICRNCID",
    t1."THPCLASS",
    t1."TRAFFICCLASS",
    t1."ULGBR",
    t1."USERPRIORITY"
FROM
huawei_nbi_umts."UUSERGBR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."BEARTYPE",
    t2."DLGBR",
    NULL,
    t2."THPCLASS",
    t2."TRAFFICCLASS",
    t2."ULGBR",
    t2."USERPRIORITY"
FROM
huawei_mml_umts."UUSERGBR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUSERHAPPYBR = ReplaceableObject(
    'huawei_cm_3g."UUSERHAPPYBR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."HAPPYBR",
    t1."LOGICRNCID",
    t1."THPCLASS",
    t1."TRAFFICCLASS",
    t1."USERPRIORITY"
FROM
huawei_nbi_umts."UUSERHAPPYBR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."HAPPYBR",
    NULL,
    t2."THPCLASS",
    t2."TRAFFICCLASS",
    t2."USERPRIORITY"
FROM
huawei_mml_umts."UUSERHAPPYBR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUSERMBR = ReplaceableObject(
    'huawei_cm_3g."UUSERMBR"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."CONVERDLMBR",
    t1."CONVERULMBR",
    t1."LOGICRNCID",
    t1."SINGALDLMBR",
    t1."SINGALULMBR",
    t1."STREAMDLMBR",
    t1."STREAMULMBR"
FROM
huawei_nbi_umts."UUSERMBR" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."CONVERDLMBR",
    t2."CONVERULMBR",
    NULL,
    t2."SINGALDLMBR",
    t2."SINGALULMBR",
    t2."STREAMDLMBR",
    t2."STREAMULMBR"
FROM
huawei_mml_umts."UUSERMBR" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUSERPLNSHAREPARA = ReplaceableObject(
    'huawei_cm_3g."UUSERPLNSHAREPARA"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."USERPLNCPUSHARINGOUTOFFSET",
    t1."USERPLNCPUSHARINGOUTTHD"
FROM
huawei_nbi_umts."UUSERPLNSHAREPARA" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."USERPLNCPUSHARINGOUTOFFSET",
    t2."USERPLNCPUSHARINGOUTTHD"
FROM
huawei_mml_umts."UUSERPLNSHAREPARA" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UUSERPRIORITY = ReplaceableObject(
    'huawei_cm_3g."UUSERPRIORITY"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."ARP10PRIORITY",
    t1."ARP11PRIORITY",
    t1."ARP12PRIORITY",
    t1."ARP13PRIORITY",
    t1."ARP14PRIORITY",
    t1."ARP15PRIORITY",
    t1."ARP1PRIORITY",
    t1."ARP2PRIORITY",
    t1."ARP3PRIORITY",
    t1."ARP4PRIORITY",
    t1."ARP5PRIORITY",
    t1."ARP6PRIORITY",
    t1."ARP7PRIORITY",
    t1."ARP8PRIORITY",
    t1."ARP9PRIORITY",
    t1."CARRIERTYPEPRIORIND",
    t1."LOGICRNCID",
    t1."PRIORITYREFERENCE"
FROM
huawei_nbi_umts."UUSERPRIORITY" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    t2."ARP10PRIORITY",
    t2."ARP11PRIORITY",
    t2."ARP12PRIORITY",
    t2."ARP13PRIORITY",
    t2."ARP14PRIORITY",
    t2."ARP15PRIORITY",
    t2."ARP1PRIORITY",
    t2."ARP2PRIORITY",
    t2."ARP3PRIORITY",
    t2."ARP4PRIORITY",
    t2."ARP5PRIORITY",
    t2."ARP6PRIORITY",
    t2."ARP7PRIORITY",
    t2."ARP8PRIORITY",
    t2."ARP9PRIORITY",
    t2."CARRIERTYPEPRIORIND",
    NULL,
    t2."PRIORITYREFERENCE"
FROM
huawei_mml_umts."UUSERPRIORITY" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

UVIPIMSI = ReplaceableObject(
    'huawei_cm_3g."UVIPIMSI"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."VIPIMSI"
FROM
huawei_nbi_umts."UVIPIMSI" t1

"""
)

UWPSALGO = ReplaceableObject(
    'huawei_cm_3g."UWPSALGO"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."LOGICRNCID",
    t1."NBMWPSALGORITHMSWITCH"
FROM
huawei_nbi_umts."UWPSALGO" t1

UNION
SELECT
    t2."FileName",
    t2."varDateTime",
    NULL,
    NULL,
    t2."BAM_VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    t2."OMU_IP" AS module_remark,
    NULL,
    NULL,
    t2."NBMWPSALGORITHMSWITCH"
FROM
huawei_mml_umts."UWPSALGO" t2
INNER JOIN huawei_mml_umts."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

VLANID = ReplaceableObject(
    'huawei_cm_3g."VLANID"',
    """

SELECT
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."IPADDR",
    t1."SN",
    t1."SRN",
    t1."VLANID"
FROM
huawei_nbi_umts."VLANID" t1

UNION
SELECT
    t21."FILENAME" AS FileName,
    t21."DATETIME" AS varDateTime,
    NULL,
    t21."NETYPE" AS ne_type,
    t21."VERSION" AS neversion,
    t21."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t2."IPADDR",
    t2."SN",
    t2."SRN",
    t2."VLANID"
FROM
huawei_gexport_wcdma."VLANID_BSC6900UMTS" t2
INNER JOIN huawei_gexport_wcdma."SYS_BSC6900UMTS" t21 ON t21."FILENAME" = t2."FILENAME"
UNION
SELECT
    t31."FILENAME" AS FileName,
    t31."DATETIME" AS varDateTime,
    NULL,
    t31."NETYPE" AS ne_type,
    t31."VERSION" AS neversion,
    t31."SYSOBJECTID" AS neid,
    NULL,
    NULL,
    NULL,
    t3."IPADDR",
    t3."SN",
    t3."SRN",
    t3."VLANID"
FROM
huawei_gexport_wcdma."VLANID_BSC6910UMTS" t3
INNER JOIN huawei_gexport_wcdma."SYS_BSC6910UMTS" t31 ON t31."FILENAME" = t3."FILENAME"
UNION
SELECT
    t4."FileName",
    t4."varDateTime",
    NULL,
    NULL,
    t4."BAM_VERSION" AS neversion,
    t41."SYSOBJECTID" AS neid,
    NULL,
    t4."OMU_IP" AS module_remark,
    NULL,
    t4."IPADDR",
    t4."SN",
    t4."SRN",
    t4."VLANID"
FROM
huawei_mml_umts."VLANID" t4
INNER JOIN huawei_mml_umts."SYS" t41 ON t41."FileName" = t4."FileName"

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
    op.drop_view(FILEFOOTER)
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
