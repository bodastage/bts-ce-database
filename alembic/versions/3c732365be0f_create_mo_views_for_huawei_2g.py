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
    t1."FileName",
    t1."varDateTime",
    t1."ne_xsitype",
    t1."netype",
    t1."neversion",
    t1."neid",
    t1."module_type",
    t1."module_remark",
    t1."module_productversion",
    t1."BSCFLAG",
    t1."CICNO",
    t1."DPCGIDX",
    t1."OPCIDX",
    t1."OPMODE",
    t1."PN",
    t1."SN",
    t1."SRN",
    t1."STCIC",
    t1."TSN",
    t1."TSTYPE"
FROM
huawei_nbi_gsm."AE1T1" t1

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
    t2."BSCFLAG",
    t2."CICNO",
    t2."DPCGIDX",
    t2."OPCIDX",
    t2."OPMODE",
    t2."PN",
    t2."SN",
    t2."SRN",
    t2."STCIC",
    t2."TSN",
    t2."TSTYPE"
FROM
huawei_gexport_gsm."AE1T1_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BSCFLAG",
    t3."CICNO",
    t3."DPCGIDX",
    t3."OPCIDX",
    t3."OPMODE",
    t3."PN",
    t3."SN",
    t3."SRN",
    t3."STCIC",
    t3."TSN",
    t3."TSTYPE"
FROM
huawei_gexport_gsm."AE1T1_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BSCFLAG",
    NULL,
    t4."DPCGIDX",
    t4."OPCIDX",
    NULL,
    t4."PN",
    t4."SN",
    t4."SRN",
    t4."STCIC",
    NULL,
    NULL
FROM
huawei_mml_gsm."AE1T1" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."CICNO",
    NULL,
    NULL,
    t5."OPMODE",
    t5."PN",
    t5."SN",
    t5."SRN",
    NULL,
    t5."TSN",
    t5."TSTYPE"
FROM
huawei_mml_gsm."AE1T1_MOD" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

AITFOTHPARA = ReplaceableObject(
    'huawei_cm_2g."AITFOTHPARA"',
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
    t1."AN4",
    t1."CHANNELRATECODE",
    t1."CIPHERINGOPTSW",
    t1."CNNODEIDX",
    t1."DECODECSFBIND",
    t1."DIRECTEDRETRYASSFAILSENDENABLE",
    t1."ENCRY_OPT_SWITCH",
    t1."ESTINDL3MSGTAFLAG",
    t1."FORCEQUEUEINASS",
    t1."INTRAHOAMRSETSTRATEGY",
    t1."MODIFYESPECICFAIL",
    t1."QUEFAILINASSMSGTYPE",
    t1."REVISIONLEVELFLAG",
    t1."SDCCHASSREQACKFLAG",
    t1."SENDCONFUSIONTOMSC",
    t1."SENDLOADINDICATIONTOMSC",
    t1."SPEECHVERSIONEXPAND",
    t1."SPEECHVERSTRATEGYINASS",
    t1."SPVERTDMSTRATEGY",
    t1."UCSPEECHVEROPTIINHO"
FROM
huawei_nbi_gsm."AITFOTHPARA" t1

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
    t2."AN4",
    t2."CHANNELRATECODE",
    t2."CIPHERINGOPTSW",
    t2."CNNODEIDX",
    t2."DECODECSFBIND",
    t2."DIRECTEDRETRYASSFAILSENDENABLE",
    t2."ENCRY_OPT_SWITCH",
    t2."ESTINDL3MSGTAFLAG",
    t2."FORCEQUEUEINASS",
    t2."INTRAHOAMRSETSTRATEGY",
    t2."MODIFYESPECICFAIL",
    t2."QUEFAILINASSMSGTYPE",
    t2."REVISIONLEVELFLAG",
    t2."SDCCHASSREQACKFLAG",
    t2."SENDCONFUSIONTOMSC",
    t2."SENDLOADINDICATIONTOMSC",
    t2."SPEECHVERSIONEXPAND",
    t2."SPEECHVERSTRATEGYINASS",
    t2."SPVERTDMSTRATEGY",
    t2."UCSPEECHVEROPTIINHO"
FROM
huawei_gexport_gsm."AITFOTHPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AN4",
    t3."CHANNELRATECODE",
    t3."CIPHERINGOPTSW",
    t3."CNNODEIDX",
    t3."DECODECSFBIND",
    t3."DIRECTEDRETRYASSFAILSENDENABLE",
    t3."ENCRY_OPT_SWITCH",
    t3."ESTINDL3MSGTAFLAG",
    t3."FORCEQUEUEINASS",
    t3."INTRAHOAMRSETSTRATEGY",
    t3."MODIFYESPECICFAIL",
    t3."QUEFAILINASSMSGTYPE",
    t3."REVISIONLEVELFLAG",
    t3."SDCCHASSREQACKFLAG",
    t3."SENDCONFUSIONTOMSC",
    t3."SENDLOADINDICATIONTOMSC",
    t3."SPEECHVERSIONEXPAND",
    t3."SPEECHVERSTRATEGYINASS",
    t3."SPVERTDMSTRATEGY",
    t3."UCSPEECHVEROPTIINHO"
FROM
huawei_gexport_gsm."AITFOTHPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AN4",
    t4."CHANNELRATECODE",
    t4."CIPHERINGOPTSW",
    t4."CNNODEIDX",
    t4."DECODECSFBIND",
    t4."DIRECTEDRETRYASSFAILSENDENABLE",
    t4."ENCRY_OPT_SWITCH",
    t4."ESTINDL3MSGTAFLAG",
    t4."FORCEQUEUEINASS",
    t4."INTRAHOAMRSETSTRATEGY",
    t4."MODIFYESPECICFAIL",
    t4."QUEFAILINASSMSGTYPE",
    t4."REVISIONLEVELFLAG",
    t4."SDCCHASSREQACKFLAG",
    t4."SENDCONFUSIONTOMSC",
    t4."SENDLOADINDICATIONTOMSC",
    t4."SPEECHVERSIONEXPAND",
    t4."SPEECHVERSTRATEGYINASS",
    t4."SPVERTDMSTRATEGY",
    t4."UCSPEECHVEROPTIINHO"
FROM
huawei_mml_gsm."AITFOTHPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

AITFREV = ReplaceableObject(
    'huawei_cm_2g."AITFREV"',
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
    t1."AITFRSVPARA1",
    t1."AITFRSVPARA2",
    t1."AITFRSVPARA3",
    t1."AITFRSVPARA4",
    t1."AITFRSVPARA5",
    t1."CNNODEIDX"
FROM
huawei_nbi_gsm."AITFREV" t1

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
    t2."AITFRSVPARA1",
    t2."AITFRSVPARA2",
    t2."AITFRSVPARA3",
    t2."AITFRSVPARA4",
    t2."AITFRSVPARA5",
    t2."CNNODEIDX"
FROM
huawei_gexport_gsm."AITFREV_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AITFRSVPARA1",
    t3."AITFRSVPARA2",
    t3."AITFRSVPARA3",
    t3."AITFRSVPARA4",
    t3."AITFRSVPARA5",
    t3."CNNODEIDX"
FROM
huawei_gexport_gsm."AITFREV_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AITFRSVPARA1",
    t4."AITFRSVPARA2",
    t4."AITFRSVPARA3",
    t4."AITFRSVPARA4",
    t4."AITFRSVPARA5",
    t4."CNNODEIDX"
FROM
huawei_mml_gsm."AITFREV" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALGCTRLPARA = ReplaceableObject(
    'huawei_cm_2g."ALGCTRLPARA"',
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
    t1."BRDTYPE",
    t1."PN",
    t1."PORTTYPE",
    t1."RLFWACSW",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."ALGCTRLPARA" t1

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
    t2."BRDTYPE",
    t2."PN",
    t2."PORTTYPE",
    t2."RLFWACSW",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."ALGCTRLPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BRDTYPE",
    t3."PN",
    t3."PORTTYPE",
    t3."RLFWACSW",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."ALGCTRLPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BRDTYPE",
    t4."PN",
    t4."PORTTYPE",
    t4."RLFWACSW",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."ALGCTRLPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMBLKPARA = ReplaceableObject(
    'huawei_cm_2g."ALMBLKPARA"',
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
    t1."AID",
    t1."BLKPRD",
    t1."CNTRISTHRD",
    t1."CNTSTLTHRD",
    t1."TMRISTHRD",
    t1."TMSTLTHRD"
FROM
huawei_nbi_gsm."ALMBLKPARA" t1

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
    t2."AID",
    t2."BLKPRD",
    t2."CNTRISTHRD",
    t2."CNTSTLTHRD",
    t2."TMRISTHRD",
    t2."TMSTLTHRD"
FROM
huawei_gexport_gsm."ALMBLKPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    t3."BLKPRD",
    t3."CNTRISTHRD",
    t3."CNTSTLTHRD",
    t3."TMRISTHRD",
    t3."TMSTLTHRD"
FROM
huawei_gexport_gsm."ALMBLKPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AID",
    t4."BLKPRD",
    t4."CNTRISTHRD",
    t4."CNTSTLTHRD",
    t4."TMRISTHRD",
    t4."TMSTLTHRD"
FROM
huawei_mml_gsm."ALMBLKPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMBLKSW = ReplaceableObject(
    'huawei_cm_2g."ALMBLKSW"',
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
    t1."BLKFILTERSW",
    t1."BLKSTATPRD",
    t1."BLKSTATSW"
FROM
huawei_nbi_gsm."ALMBLKSW" t1

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
    t2."BLKFILTERSW",
    t2."BLKSTATPRD",
    t2."BLKSTATSW"
FROM
huawei_gexport_gsm."ALMBLKSW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BLKFILTERSW",
    t3."BLKSTATPRD",
    t3."BLKSTATSW"
FROM
huawei_gexport_gsm."ALMBLKSW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BLKFILTERSW",
    t4."BLKSTATPRD",
    t4."BLKSTATSW"
FROM
huawei_mml_gsm."ALMBLKSW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMCAPACITY = ReplaceableObject(
    'huawei_cm_2g."ALMCAPACITY"',
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
    t1."MAXNUM",
    t1."SD"
FROM
huawei_nbi_gsm."ALMCAPACITY" t1

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
    t2."MAXNUM",
    t2."SD"
FROM
huawei_gexport_gsm."ALMCAPACITY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."MAXNUM",
    t3."SD"
FROM
huawei_gexport_gsm."ALMCAPACITY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."MAXNUM",
    t4."SD"
FROM
huawei_mml_gsm."ALMCAPACITY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMLVL = ReplaceableObject(
    'huawei_cm_2g."ALMLVL"',
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
    t1."AID",
    t1."ALVL"
FROM
huawei_nbi_gsm."ALMLVL" t1

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
    t2."AID",
    t2."ALVL"
FROM
huawei_gexport_gsm."ALMLVL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    t3."ALVL"
FROM
huawei_gexport_gsm."ALMLVL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

ALMML = ReplaceableObject(
    'huawei_cm_2g."ALMML"',
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
    t1."CMELEVEL"
FROM
huawei_nbi_gsm."ALMML" t1

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
huawei_gexport_gsm."ALMML_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."ALMML_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."ALMML" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMOSCISW = ReplaceableObject(
    'huawei_cm_2g."ALMOSCISW"',
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
    t1."SW"
FROM
huawei_nbi_gsm."ALMOSCISW" t1

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
    t2."SW"
FROM
huawei_gexport_gsm."ALMOSCISW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SW"
FROM
huawei_gexport_gsm."ALMOSCISW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SW"
FROM
huawei_mml_gsm."ALMOSCISW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMOSCITHRD = ReplaceableObject(
    'huawei_cm_2g."ALMOSCITHRD"',
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
    t1."AID",
    t1."INOSCPRD",
    t1."INOSCTHRD",
    t1."OUTOSCPRD",
    t1."OUTOSCTHRD"
FROM
huawei_nbi_gsm."ALMOSCITHRD" t1

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
    t2."AID",
    t2."INOSCPRD",
    t2."INOSCTHRD",
    t2."OUTOSCPRD",
    t2."OUTOSCTHRD"
FROM
huawei_gexport_gsm."ALMOSCITHRD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    t3."INOSCPRD",
    t3."INOSCTHRD",
    t3."OUTOSCPRD",
    t3."OUTOSCTHRD"
FROM
huawei_gexport_gsm."ALMOSCITHRD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AID",
    t4."INOSCPRD",
    t4."INOSCTHRD",
    t4."OUTOSCPRD",
    t4."OUTOSCTHRD"
FROM
huawei_mml_gsm."ALMOSCITHRD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMSCRN = ReplaceableObject(
    'huawei_cm_2g."ALMSCRN"',
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
    t1."ALVL"
FROM
huawei_nbi_gsm."ALMSCRN" t1

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
    t2."ALVL"
FROM
huawei_gexport_gsm."ALMSCRN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALVL"
FROM
huawei_gexport_gsm."ALMSCRN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALVL"
FROM
huawei_mml_gsm."ALMSCRN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ALMSHLD = ReplaceableObject(
    'huawei_cm_2g."ALMSHLD"',
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
    t1."AID",
    t1."SHLDFLG"
FROM
huawei_nbi_gsm."ALMSHLD" t1

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
    t2."AID",
    t2."SHLDFLG"
FROM
huawei_gexport_gsm."ALMSHLD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    t3."SHLDFLG"
FROM
huawei_gexport_gsm."ALMSHLD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AID",
    t4."SHLDFLG"
FROM
huawei_mml_gsm."ALMSHLD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

APPCERT = ReplaceableObject(
    'huawei_cm_2g."APPCERT"',
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
    t1."APPCERT",
    t1."APPTYPE"
FROM
huawei_nbi_gsm."APPCERT" t1

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
    t2."APPCERT",
    t2."APPTYPE"
FROM
huawei_gexport_gsm."APPCERT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."APPCERT",
    t3."APPTYPE"
FROM
huawei_gexport_gsm."APPCERT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

ATESTPARA = ReplaceableObject(
    'huawei_cm_2g."ATESTPARA"',
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
    t1."AINTFTESTENABLE"
FROM
huawei_nbi_gsm."ATESTPARA" t1

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
    t2."AINTFTESTENABLE"
FROM
huawei_gexport_gsm."ATESTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AINTFTESTENABLE"
FROM
huawei_gexport_gsm."ATESTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AINTFTESTENABLE"
FROM
huawei_mml_gsm."ATESTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BFDPROTOSW = ReplaceableObject(
    'huawei_cm_2g."BFDPROTOSW"',
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
    t1."SN",
    t1."SRN",
    t1."SWITCH"
FROM
huawei_nbi_gsm."BFDPROTOSW" t1

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
    t2."SN",
    t2."SRN",
    t2."SWITCH"
FROM
huawei_gexport_gsm."BFDPROTOSW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SN",
    t3."SRN",
    t3."SWITCH"
FROM
huawei_gexport_gsm."BFDPROTOSW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SN",
    t4."SRN",
    t4."SWITCH"
FROM
huawei_mml_gsm."BFDPROTOSW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BOXRPT = ReplaceableObject(
    'huawei_cm_2g."BOXRPT"',
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
    t1."AID",
    t1."BOXFLG"
FROM
huawei_nbi_gsm."BOXRPT" t1

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
    t2."AID",
    t2."BOXFLG"
FROM
huawei_gexport_gsm."BOXRPT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    t3."BOXFLG"
FROM
huawei_gexport_gsm."BOXRPT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

BRD = ReplaceableObject(
    'huawei_cm_2g."BRD"',
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
    t1."BRDCLASS",
    t1."BRDTYPE",
    t1."LGCAPPTYPE",
    t1."RED",
    t1."SN",
    t1."SRN",
    t1."MPUSLOT",
    t1."MPUSUBRACK",
    t1."AUTOADDSRCON",
    t1."ISTCBRD",
    t1."LGCUSAGETYPE"
FROM
huawei_nbi_gsm."BRD" t1

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
    NULL,
    t2."LGCAPPTYPE",
    t2."RED",
    t2."SN",
    t2."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."BRD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    NULL,
    t3."LGCAPPTYPE",
    t3."RED",
    t3."SN",
    t3."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."BRD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BRDCLASS",
    t4."BRDTYPE",
    t4."LGCAPPTYPE",
    t4."RED",
    t4."SN",
    t4."SRN",
    t4."MPUSLOT",
    t4."MPUSUBRACK",
    t4."AUTOADDSRCON",
    t4."ISTCBRD",
    NULL
FROM
huawei_mml_gsm."BRD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."BRDCLASS",
    t5."BRDTYPE",
    NULL,
    NULL,
    t5."SN",
    t5."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."BRD_MOD" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

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
    t6."SN",
    t6."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."BRD_UIN" t6
INNER JOIN huawei_mml_gsm."SYS" t61 ON t61."FileName" = t6."FileName"

"""
)

BSCAISS = ReplaceableObject(
    'huawei_cm_2g."BSCAISS"',
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
    t1."BSCSYMOFF"
FROM
huawei_nbi_gsm."BSCAISS" t1

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
    t2."BSCSYMOFF"
FROM
huawei_gexport_gsm."BSCAISS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BSCSYMOFF"
FROM
huawei_gexport_gsm."BSCAISS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BSCSYMOFF"
FROM
huawei_mml_gsm."BSCAISS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCAITFTMR = ReplaceableObject(
    'huawei_cm_2g."BSCAITFTMR"',
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
    t1."AT13",
    t1."AT17",
    t1."AT18",
    t1."AT4",
    t1."CNNODEIDX"
FROM
huawei_nbi_gsm."BSCAITFTMR" t1

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
    t2."AT13",
    t2."AT17",
    t2."AT18",
    t2."AT4",
    t2."CNNODEIDX"
FROM
huawei_gexport_gsm."BSCAITFTMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AT13",
    t3."AT17",
    t3."AT18",
    t3."AT4",
    t3."CNNODEIDX"
FROM
huawei_gexport_gsm."BSCAITFTMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AT13",
    t4."AT17",
    t4."AT18",
    t4."AT4",
    t4."CNNODEIDX"
FROM
huawei_mml_gsm."BSCAITFTMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCBASIC = ReplaceableObject(
    'huawei_cm_2g."BSCBASIC"',
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
    t1."ABISVER",
    t1."AIPCSDSRVRDNDLEV",
    t1."AMRHOCODECPOLICY",
    t1."AREACODE",
    t1."AVER",
    t1."BSCAVN",
    t1."BSCGLOBALIDENTITY",
    t1."BSCPVN",
    t1."CBPROTOCOLSPEC",
    t1."CC",
    t1."CICDMUTEDIFCNT",
    t1."CICDMUTEPERIOD",
    t1."CICDMUTESWITCH",
    t1."CICDMUTETHRE",
    t1."CICDMUTETIME",
    t1."CROCALTMTHRD",
    t1."CSPREHSCSDSECHANSW",
    t1."ENPREEMPTABISLVDSADMT",
    t1."ENPREEMPTISCADMT",
    t1."ENPREEMPTTRANSADMT",
    t1."ENQUETRANSADMT",
    t1."ENTCAUSE",
    t1."ENTSWITCH",
    t1."GCCHK",
    t1."GETBTSNETTBLTIMETHD",
    t1."GSMCSUSERHIGHPRILEV",
    t1."HIFREQBANDSUPPORT",
    t1."HSCSDCHANGEMODE",
    t1."ISCCONGALMCLRTH",
    t1."ISCCONGALMTH",
    t1."MSISDNPREFIX1",
    t1."MSISDNPREFIX2",
    t1."MSISDNPREFIX3",
    t1."MSISDNPREFIX4",
    t1."MSISDNPREFIX5",
    t1."MUTETESTLOGSTYLE",
    t1."SERVICEMODE",
    t1."SINGLEPASSEXCLUDEMSISDN1",
    t1."SINGLEPASSEXCLUDEMSISDN10",
    t1."SINGLEPASSEXCLUDEMSISDN11",
    t1."SINGLEPASSEXCLUDEMSISDN12",
    t1."SINGLEPASSEXCLUDEMSISDN13",
    t1."SINGLEPASSEXCLUDEMSISDN14",
    t1."SINGLEPASSEXCLUDEMSISDN15",
    t1."SINGLEPASSEXCLUDEMSISDN16",
    t1."SINGLEPASSEXCLUDEMSISDN17",
    t1."SINGLEPASSEXCLUDEMSISDN18",
    t1."SINGLEPASSEXCLUDEMSISDN19",
    t1."SINGLEPASSEXCLUDEMSISDN2",
    t1."SINGLEPASSEXCLUDEMSISDN20",
    t1."SINGLEPASSEXCLUDEMSISDN3",
    t1."SINGLEPASSEXCLUDEMSISDN4",
    t1."SINGLEPASSEXCLUDEMSISDN5",
    t1."SINGLEPASSEXCLUDEMSISDN6",
    t1."SINGLEPASSEXCLUDEMSISDN7",
    t1."SINGLEPASSEXCLUDEMSISDN8",
    t1."SINGLEPASSEXCLUDEMSISDN9",
    t1."SPEECHALMPERIOD",
    t1."SPEECHCHANALARMTHRES",
    t1."SPEECHCHANRESUMEALARMTHRES",
    t1."SPEECHCHNALMMUTESTATTYPE",
    t1."SPEECHERRORFORCEHOSWITCH",
    t1."SPTRANSHARING",
    t1."SUPPORTTFOCODECOPTIMIZE",
    t1."SYSMSG10ALLOWED",
    t1."TCCRCALLOWED",
    t1."TCHBUSYTHRESOPT",
    t1."UMCROSSDECTECTSWITCH",
    t1."UMVER"
FROM
huawei_nbi_gsm."BSCBASIC" t1

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
    t2."ABISVER",
    t2."AIPCSDSRVRDNDLEV",
    t2."AMRHOCODECPOLICY",
    t2."AREACODE",
    t2."AVER",
    t2."BSCAVN",
    t2."BSCGLOBALIDENTITY",
    t2."BSCPVN",
    t2."CBPROTOCOLSPEC",
    t2."CC",
    t2."CICDMUTEDIFCNT",
    t2."CICDMUTEPERIOD",
    t2."CICDMUTESWITCH",
    t2."CICDMUTETHRE",
    t2."CICDMUTETIME",
    t2."CROCALTMTHRD",
    t2."CSPREHSCSDSECHANSW",
    t2."ENPREEMPTABISLVDSADMT",
    t2."ENPREEMPTISCADMT",
    t2."ENPREEMPTTRANSADMT",
    t2."ENQUETRANSADMT",
    NULL,
    t2."ENTSWITCH",
    t2."GCCHK",
    t2."GETBTSNETTBLTIMETHD",
    t2."GSMCSUSERHIGHPRILEV",
    t2."HIFREQBANDSUPPORT",
    t2."HSCSDCHANGEMODE",
    t2."ISCCONGALMCLRTH",
    t2."ISCCONGALMTH",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."SERVICEMODE",
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
    t2."SPEECHALMPERIOD",
    t2."SPEECHCHANALARMTHRES",
    t2."SPEECHCHANRESUMEALARMTHRES",
    t2."SPEECHCHNALMMUTESTATTYPE",
    t2."SPEECHERRORFORCEHOSWITCH",
    t2."SPTRANSHARING",
    t2."SUPPORTTFOCODECOPTIMIZE",
    t2."SYSMSG10ALLOWED",
    t2."TCCRCALLOWED",
    t2."TCHBUSYTHRESOPT",
    t2."UMCROSSDECTECTSWITCH",
    t2."UMVER"
FROM
huawei_gexport_gsm."BSCBASIC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISVER",
    t3."AIPCSDSRVRDNDLEV",
    t3."AMRHOCODECPOLICY",
    t3."AREACODE",
    t3."AVER",
    t3."BSCAVN",
    t3."BSCGLOBALIDENTITY",
    t3."BSCPVN",
    t3."CBPROTOCOLSPEC",
    t3."CC",
    t3."CICDMUTEDIFCNT",
    t3."CICDMUTEPERIOD",
    t3."CICDMUTESWITCH",
    t3."CICDMUTETHRE",
    t3."CICDMUTETIME",
    t3."CROCALTMTHRD",
    t3."CSPREHSCSDSECHANSW",
    t3."ENPREEMPTABISLVDSADMT",
    t3."ENPREEMPTISCADMT",
    t3."ENPREEMPTTRANSADMT",
    t3."ENQUETRANSADMT",
    NULL,
    t3."ENTSWITCH",
    t3."GCCHK",
    t3."GETBTSNETTBLTIMETHD",
    t3."GSMCSUSERHIGHPRILEV",
    t3."HIFREQBANDSUPPORT",
    t3."HSCSDCHANGEMODE",
    t3."ISCCONGALMCLRTH",
    t3."ISCCONGALMTH",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."SERVICEMODE",
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
    t3."SPEECHALMPERIOD",
    t3."SPEECHCHANALARMTHRES",
    t3."SPEECHCHANRESUMEALARMTHRES",
    t3."SPEECHCHNALMMUTESTATTYPE",
    t3."SPEECHERRORFORCEHOSWITCH",
    t3."SPTRANSHARING",
    t3."SUPPORTTFOCODECOPTIMIZE",
    t3."SYSMSG10ALLOWED",
    t3."TCCRCALLOWED",
    t3."TCHBUSYTHRESOPT",
    t3."UMCROSSDECTECTSWITCH",
    t3."UMVER"
FROM
huawei_gexport_gsm."BSCBASIC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISVER",
    t4."AIPCSDSRVRDNDLEV",
    t4."AMRHOCODECPOLICY",
    t4."AREACODE",
    t4."AVER",
    t4."BSCAVN",
    t4."BSCGLOBALIDENTITY",
    t4."BSCPVN",
    t4."CBPROTOCOLSPEC",
    t4."CC",
    t4."CICDMUTEDIFCNT",
    t4."CICDMUTEPERIOD",
    t4."CICDMUTESWITCH",
    t4."CICDMUTETHRE",
    t4."CICDMUTETIME",
    t4."CROCALTMTHRD",
    t4."CSPREHSCSDSECHANSW",
    t4."ENPREEMPTABISLVDSADMT",
    t4."ENPREEMPTISCADMT",
    t4."ENPREEMPTTRANSADMT",
    t4."ENQUETRANSADMT",
    NULL,
    t4."ENTSWITCH",
    t4."GCCHK",
    t4."GETBTSNETTBLTIMETHD",
    t4."GSMCSUSERHIGHPRILEV",
    t4."HIFREQBANDSUPPORT",
    t4."HSCSDCHANGEMODE",
    t4."ISCCONGALMCLRTH",
    t4."ISCCONGALMTH",
    t4."MSISDNPREFIX1",
    t4."MSISDNPREFIX2",
    t4."MSISDNPREFIX3",
    t4."MSISDNPREFIX4",
    t4."MSISDNPREFIX5",
    NULL,
    t4."SERVICEMODE",
    t4."SINGLEPASSEXCLUDEMSISDN1",
    t4."SINGLEPASSEXCLUDEMSISDN10",
    t4."SINGLEPASSEXCLUDEMSISDN11",
    t4."SINGLEPASSEXCLUDEMSISDN12",
    t4."SINGLEPASSEXCLUDEMSISDN13",
    t4."SINGLEPASSEXCLUDEMSISDN14",
    t4."SINGLEPASSEXCLUDEMSISDN15",
    t4."SINGLEPASSEXCLUDEMSISDN16",
    t4."SINGLEPASSEXCLUDEMSISDN17",
    t4."SINGLEPASSEXCLUDEMSISDN18",
    t4."SINGLEPASSEXCLUDEMSISDN19",
    t4."SINGLEPASSEXCLUDEMSISDN2",
    t4."SINGLEPASSEXCLUDEMSISDN20",
    t4."SINGLEPASSEXCLUDEMSISDN3",
    t4."SINGLEPASSEXCLUDEMSISDN4",
    t4."SINGLEPASSEXCLUDEMSISDN5",
    t4."SINGLEPASSEXCLUDEMSISDN6",
    t4."SINGLEPASSEXCLUDEMSISDN7",
    t4."SINGLEPASSEXCLUDEMSISDN8",
    t4."SINGLEPASSEXCLUDEMSISDN9",
    t4."SPEECHALMPERIOD",
    t4."SPEECHCHANALARMTHRES",
    t4."SPEECHCHANRESUMEALARMTHRES",
    t4."SPEECHCHNALMMUTESTATTYPE",
    t4."SPEECHERRORFORCEHOSWITCH",
    t4."SPTRANSHARING",
    t4."SUPPORTTFOCODECOPTIMIZE",
    t4."SYSMSG10ALLOWED",
    t4."TCCRCALLOWED",
    t4."TCHBUSYTHRESOPT",
    t4."UMCROSSDECTECTSWITCH",
    t4."UMVER"
FROM
huawei_mml_gsm."BSCBASIC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCDSTPA = ReplaceableObject(
    'huawei_cm_2g."BSCDSTPA"',
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
    t1."BSCDYNSWITCHTRXPAALLOW",
    t1."TSTURNINGOFFENABLE",
    t1."RSVIDLECHANNUM"
FROM
huawei_nbi_gsm."BSCDSTPA" t1

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
    t2."BSCDYNSWITCHTRXPAALLOW",
    t2."TSTURNINGOFFENABLE",
    NULL
FROM
huawei_gexport_gsm."BSCDSTPA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BSCDYNSWITCHTRXPAALLOW",
    t3."TSTURNINGOFFENABLE",
    NULL
FROM
huawei_gexport_gsm."BSCDSTPA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BSCDYNSWITCHTRXPAALLOW",
    t4."TSTURNINGOFFENABLE",
    t4."RSVIDLECHANNUM"
FROM
huawei_mml_gsm."BSCDSTPA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCEXSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."BSCEXSOFTPARA"',
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
    t1."ABNORMSFORCSPEECHVERSW",
    t1."ABNORMSINBSCHOSTATPROSW",
    t1."ABNORRELBEFDIRECTSTATSW",
    t1."ABNORRELBEFHOSTATSW",
    t1."ABRKBARCELLOPTINTERVAL",
    t1."ABRKBARCELLSW",
    t1."AFTCONNRELSORTSTATSW",
    t1."AOIPRTPCONSW",
    t1."APPDATACHKGENSW",
    t1."APPDATACHKSW",
    t1."APPDATASELFHEALSW",
    t1."ASSFAILMSCCLDOPTSW",
    t1."BACDDETECTEN",
    t1."BSCLAYEREDPAGINGSW",
    t1."BSSLSOPTINDTMSW",
    t1."BTSUNAVAILALARMCHKSW",
    t1."CALLRELCROSSPROSW",
    t1."CCNACTIVEIECTRLSW",
    t1."CHANNELDYNADJUSTOPT",
    t1."CHRSIGMSGUSERIDENCRYPTSW",
    t1."CMPL3PROTOCOLCONSSW",
    t1."CROSSSEROCCUPYSTATSW",
    t1."CSCHOCCUPYSTATINLAUSW",
    t1."CSDTRANSRESOURCECTRLSWITCH",
    t1."CSFBACCCAUSESTATOPTSW",
    t1."CSFBPAGINGIDENTIFYSW",
    t1."DEACELLPERFSW",
    t1."DISCCLEARREQSTATSW",
    t1."DISCONNECTINHANDOVER",
    t1."DISCRELINDSTATSW",
    t1."DROPSORTSTATPOLICYSW",
    t1."DTMCHOCCUPYSUPPLYSTATSW",
    t1."DTMOPINDEXOPTSW",
    t1."DTMPSREROUTEPOLICY",
    t1."DYNPDCHSELFHEALSW",
    t1."ECSCOPTSW",
    t1."FASTRETURNSCRAMBLEINDSW",
    t1."FASTRETURNSERVICEHOSW",
    t1."FORCEUPDATEMSSI",
    t1."GHOFILTEROPT",
    t1."GLFRCSMTLAUMODE",
    t1."HISPRIOOPTSW",
    t1."HOCIPHERSW",
    t1."HOCMDTIMESTAMPADJUST",
    t1."HOFORBIDDENINLOCUPSW",
    t1."HOL2REBUILDTIMES",
    t1."HQIDEFINITION",
    t1."HSRPLCUSRIDNTMNGSW",
    t1."IBCAOUTBSCMSGSNDCTRLSW",
    t1."IGNORECONNFAILBEFHOCMPSW",
    t1."IMMASSUML3NULLPROPOLICY",
    t1."INTERBSCINHOSUCCSTATOPT",
    t1."INTERHOCM2IE",
    t1."INTERHOCM3LEN",
    t1."INTERRANHOEXPSW",
    t1."INTRABSCAMRHOCMDDELAYSW",
    t1."IUOFITEROPT",
    t1."JUDGERNCCIPHERSTATE",
    t1."LOADINDPROCON",
    t1."LOCKCELLSENDALMSW",
    t1."LOCREQCLASSMARK3INDSW",
    t1."MCPLOADOPTSWITCH",
    t1."MOCNCSWAITIDRSPTIMER",
    t1."MOCNQRYIMSISNDXIDSW",
    t1."MOCNREPLACEIMSISW",
    t1."MOCNREROUTEOPT",
    t1."MOCNROUTEPOLICYGETIMSIFAIL",
    t1."MOCNSELECTCNPOLICY",
    t1."MOCNTIMEOUTREROUTEPERMIT",
    t1."MOCNWAITIDRSPTIMER",
    t1."MRRXQUALSTATMODESW",
    t1."MSGBYTEORDERPROTPOLICY",
    t1."PDCHSTATOPTSW",
    t1."REASSFAILSTATSW",
    t1."REASSIGNINAOIPSW",
    t1."RECLAIMFAILPDRELSW",
    t1."RESENDIDREQSW",
    t1."RETURNOLDCHANOPTSW",
    t1."RXLEVSTATSORTSW",
    t1."SAICWHTMSIDENTALPHALWRTHLD",
    t1."SAICWHTMSIDENTALPHAUPTHLD",
    t1."SAICWHTMSIDENTREQTIMES",
    t1."SAICWHTMSIDENTSATTIMES",
    t1."SAVEUSERPAGINGTMR",
    t1."SECONDDIRECTHOREQSTATSW",
    t1."TRANIMTMALMPROTECTSW",
    t1."USERPRIORITYOPT",
    t1."USRPRITHRES1",
    t1."USRPRITHRES2",
    t1."UTRANCMDECSW",
    t1."UTRANPRIIECTRLSW",
    t1."VIPDTXFORBIDSW",
    t1."VIPPOWERAMP"
FROM
huawei_nbi_gsm."BSCEXSOFTPARA" t1

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
    t2."ABNORMSFORCSPEECHVERSW",
    t2."ABNORMSINBSCHOSTATPROSW",
    t2."ABNORRELBEFDIRECTSTATSW",
    t2."ABNORRELBEFHOSTATSW",
    t2."ABRKBARCELLOPTINTERVAL",
    t2."ABRKBARCELLSW",
    t2."AFTCONNRELSORTSTATSW",
    t2."AOIPRTPCONSW",
    t2."APPDATACHKGENSW",
    t2."APPDATACHKSW",
    t2."APPDATASELFHEALSW",
    t2."ASSFAILMSCCLDOPTSW",
    t2."BACDDETECTEN",
    t2."BSCLAYEREDPAGINGSW",
    t2."BSSLSOPTINDTMSW",
    t2."BTSUNAVAILALARMCHKSW",
    t2."CALLRELCROSSPROSW",
    t2."CCNACTIVEIECTRLSW",
    t2."CHANNELDYNADJUSTOPT",
    t2."CHRSIGMSGUSERIDENCRYPTSW",
    t2."CMPL3PROTOCOLCONSSW",
    t2."CROSSSEROCCUPYSTATSW",
    t2."CSCHOCCUPYSTATINLAUSW",
    t2."CSDTRANSRESOURCECTRLSWITCH",
    t2."CSFBACCCAUSESTATOPTSW",
    t2."CSFBPAGINGIDENTIFYSW",
    t2."DEACELLPERFSW",
    t2."DISCCLEARREQSTATSW",
    t2."DISCONNECTINHANDOVER",
    t2."DISCRELINDSTATSW",
    t2."DROPSORTSTATPOLICYSW",
    t2."DTMCHOCCUPYSUPPLYSTATSW",
    t2."DTMOPINDEXOPTSW",
    t2."DTMPSREROUTEPOLICY",
    t2."DYNPDCHSELFHEALSW",
    t2."ECSCOPTSW",
    t2."FASTRETURNSCRAMBLEINDSW",
    t2."FASTRETURNSERVICEHOSW",
    t2."FORCEUPDATEMSSI",
    t2."GHOFILTEROPT",
    NULL,
    t2."HISPRIOOPTSW",
    t2."HOCIPHERSW",
    t2."HOCMDTIMESTAMPADJUST",
    t2."HOFORBIDDENINLOCUPSW",
    t2."HOL2REBUILDTIMES",
    t2."HQIDEFINITION",
    t2."HSRPLCUSRIDNTMNGSW",
    t2."IBCAOUTBSCMSGSNDCTRLSW",
    t2."IGNORECONNFAILBEFHOCMPSW",
    t2."IMMASSUML3NULLPROPOLICY",
    t2."INTERBSCINHOSUCCSTATOPT",
    t2."INTERHOCM2IE",
    t2."INTERHOCM3LEN",
    t2."INTERRANHOEXPSW",
    t2."INTRABSCAMRHOCMDDELAYSW",
    t2."IUOFITEROPT",
    t2."JUDGERNCCIPHERSTATE",
    t2."LOADINDPROCON",
    t2."LOCKCELLSENDALMSW",
    t2."LOCREQCLASSMARK3INDSW",
    t2."MCPLOADOPTSWITCH",
    t2."MOCNCSWAITIDRSPTIMER",
    t2."MOCNQRYIMSISNDXIDSW",
    t2."MOCNREPLACEIMSISW",
    t2."MOCNREROUTEOPT",
    t2."MOCNROUTEPOLICYGETIMSIFAIL",
    t2."MOCNSELECTCNPOLICY",
    t2."MOCNTIMEOUTREROUTEPERMIT",
    t2."MOCNWAITIDRSPTIMER",
    t2."MRRXQUALSTATMODESW",
    NULL,
    t2."PDCHSTATOPTSW",
    t2."REASSFAILSTATSW",
    t2."REASSIGNINAOIPSW",
    t2."RECLAIMFAILPDRELSW",
    t2."RESENDIDREQSW",
    t2."RETURNOLDCHANOPTSW",
    t2."RXLEVSTATSORTSW",
    t2."SAICWHTMSIDENTALPHALWRTHLD",
    t2."SAICWHTMSIDENTALPHAUPTHLD",
    t2."SAICWHTMSIDENTREQTIMES",
    t2."SAICWHTMSIDENTSATTIMES",
    t2."SAVEUSERPAGINGTMR",
    t2."SECONDDIRECTHOREQSTATSW",
    t2."TRANIMTMALMPROTECTSW",
    t2."USERPRIORITYOPT",
    t2."USRPRITHRES1",
    t2."USRPRITHRES2",
    t2."UTRANCMDECSW",
    t2."UTRANPRIIECTRLSW",
    t2."VIPDTXFORBIDSW",
    t2."VIPPOWERAMP"
FROM
huawei_gexport_gsm."BSCEXSOFTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABNORMSFORCSPEECHVERSW",
    t3."ABNORMSINBSCHOSTATPROSW",
    t3."ABNORRELBEFDIRECTSTATSW",
    t3."ABNORRELBEFHOSTATSW",
    t3."ABRKBARCELLOPTINTERVAL",
    t3."ABRKBARCELLSW",
    t3."AFTCONNRELSORTSTATSW",
    t3."AOIPRTPCONSW",
    t3."APPDATACHKGENSW",
    t3."APPDATACHKSW",
    t3."APPDATASELFHEALSW",
    t3."ASSFAILMSCCLDOPTSW",
    t3."BACDDETECTEN",
    t3."BSCLAYEREDPAGINGSW",
    t3."BSSLSOPTINDTMSW",
    t3."BTSUNAVAILALARMCHKSW",
    t3."CALLRELCROSSPROSW",
    t3."CCNACTIVEIECTRLSW",
    t3."CHANNELDYNADJUSTOPT",
    t3."CHRSIGMSGUSERIDENCRYPTSW",
    t3."CMPL3PROTOCOLCONSSW",
    t3."CROSSSEROCCUPYSTATSW",
    t3."CSCHOCCUPYSTATINLAUSW",
    t3."CSDTRANSRESOURCECTRLSWITCH",
    t3."CSFBACCCAUSESTATOPTSW",
    t3."CSFBPAGINGIDENTIFYSW",
    t3."DEACELLPERFSW",
    t3."DISCCLEARREQSTATSW",
    t3."DISCONNECTINHANDOVER",
    t3."DISCRELINDSTATSW",
    t3."DROPSORTSTATPOLICYSW",
    t3."DTMCHOCCUPYSUPPLYSTATSW",
    t3."DTMOPINDEXOPTSW",
    t3."DTMPSREROUTEPOLICY",
    t3."DYNPDCHSELFHEALSW",
    t3."ECSCOPTSW",
    t3."FASTRETURNSCRAMBLEINDSW",
    t3."FASTRETURNSERVICEHOSW",
    t3."FORCEUPDATEMSSI",
    t3."GHOFILTEROPT",
    NULL,
    t3."HISPRIOOPTSW",
    t3."HOCIPHERSW",
    t3."HOCMDTIMESTAMPADJUST",
    t3."HOFORBIDDENINLOCUPSW",
    t3."HOL2REBUILDTIMES",
    t3."HQIDEFINITION",
    t3."HSRPLCUSRIDNTMNGSW",
    t3."IBCAOUTBSCMSGSNDCTRLSW",
    t3."IGNORECONNFAILBEFHOCMPSW",
    t3."IMMASSUML3NULLPROPOLICY",
    t3."INTERBSCINHOSUCCSTATOPT",
    t3."INTERHOCM2IE",
    t3."INTERHOCM3LEN",
    t3."INTERRANHOEXPSW",
    t3."INTRABSCAMRHOCMDDELAYSW",
    t3."IUOFITEROPT",
    t3."JUDGERNCCIPHERSTATE",
    t3."LOADINDPROCON",
    t3."LOCKCELLSENDALMSW",
    t3."LOCREQCLASSMARK3INDSW",
    t3."MCPLOADOPTSWITCH",
    t3."MOCNCSWAITIDRSPTIMER",
    t3."MOCNQRYIMSISNDXIDSW",
    t3."MOCNREPLACEIMSISW",
    t3."MOCNREROUTEOPT",
    t3."MOCNROUTEPOLICYGETIMSIFAIL",
    t3."MOCNSELECTCNPOLICY",
    t3."MOCNTIMEOUTREROUTEPERMIT",
    t3."MOCNWAITIDRSPTIMER",
    t3."MRRXQUALSTATMODESW",
    NULL,
    t3."PDCHSTATOPTSW",
    t3."REASSFAILSTATSW",
    t3."REASSIGNINAOIPSW",
    t3."RECLAIMFAILPDRELSW",
    t3."RESENDIDREQSW",
    t3."RETURNOLDCHANOPTSW",
    t3."RXLEVSTATSORTSW",
    t3."SAICWHTMSIDENTALPHALWRTHLD",
    t3."SAICWHTMSIDENTALPHAUPTHLD",
    t3."SAICWHTMSIDENTREQTIMES",
    t3."SAICWHTMSIDENTSATTIMES",
    t3."SAVEUSERPAGINGTMR",
    t3."SECONDDIRECTHOREQSTATSW",
    t3."TRANIMTMALMPROTECTSW",
    t3."USERPRIORITYOPT",
    t3."USRPRITHRES1",
    t3."USRPRITHRES2",
    t3."UTRANCMDECSW",
    t3."UTRANPRIIECTRLSW",
    t3."VIPDTXFORBIDSW",
    t3."VIPPOWERAMP"
FROM
huawei_gexport_gsm."BSCEXSOFTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABNORMSFORCSPEECHVERSW",
    t4."ABNORMSINBSCHOSTATPROSW",
    t4."ABNORRELBEFDIRECTSTATSW",
    t4."ABNORRELBEFHOSTATSW",
    t4."ABRKBARCELLOPTINTERVAL",
    t4."ABRKBARCELLSW",
    t4."AFTCONNRELSORTSTATSW",
    t4."AOIPRTPCONSW",
    t4."APPDATACHKGENSW",
    t4."APPDATACHKSW",
    t4."APPDATASELFHEALSW",
    t4."ASSFAILMSCCLDOPTSW",
    t4."BACDDETECTEN",
    t4."BSCLAYEREDPAGINGSW",
    t4."BSSLSOPTINDTMSW",
    t4."BTSUNAVAILALARMCHKSW",
    t4."CALLRELCROSSPROSW",
    t4."CCNACTIVEIECTRLSW",
    t4."CHANNELDYNADJUSTOPT",
    t4."CHRSIGMSGUSERIDENCRYPTSW",
    t4."CMPL3PROTOCOLCONSSW",
    t4."CROSSSEROCCUPYSTATSW",
    t4."CSCHOCCUPYSTATINLAUSW",
    t4."CSDTRANSRESOURCECTRLSWITCH",
    t4."CSFBACCCAUSESTATOPTSW",
    t4."CSFBPAGINGIDENTIFYSW",
    t4."DEACELLPERFSW",
    t4."DISCCLEARREQSTATSW",
    t4."DISCONNECTINHANDOVER",
    t4."DISCRELINDSTATSW",
    t4."DROPSORTSTATPOLICYSW",
    t4."DTMCHOCCUPYSUPPLYSTATSW",
    t4."DTMOPINDEXOPTSW",
    t4."DTMPSREROUTEPOLICY",
    t4."DYNPDCHSELFHEALSW",
    t4."ECSCOPTSW",
    t4."FASTRETURNSCRAMBLEINDSW",
    t4."FASTRETURNSERVICEHOSW",
    t4."FORCEUPDATEMSSI",
    t4."GHOFILTEROPT",
    NULL,
    t4."HISPRIOOPTSW",
    t4."HOCIPHERSW",
    t4."HOCMDTIMESTAMPADJUST",
    t4."HOFORBIDDENINLOCUPSW",
    t4."HOL2REBUILDTIMES",
    t4."HQIDEFINITION",
    t4."HSRPLCUSRIDNTMNGSW",
    t4."IBCAOUTBSCMSGSNDCTRLSW",
    t4."IGNORECONNFAILBEFHOCMPSW",
    t4."IMMASSUML3NULLPROPOLICY",
    t4."INTERBSCINHOSUCCSTATOPT",
    t4."INTERHOCM2IE",
    t4."INTERHOCM3LEN",
    t4."INTERRANHOEXPSW",
    t4."INTRABSCAMRHOCMDDELAYSW",
    t4."IUOFITEROPT",
    t4."JUDGERNCCIPHERSTATE",
    t4."LOADINDPROCON",
    t4."LOCKCELLSENDALMSW",
    t4."LOCREQCLASSMARK3INDSW",
    t4."MCPLOADOPTSWITCH",
    t4."MOCNCSWAITIDRSPTIMER",
    t4."MOCNQRYIMSISNDXIDSW",
    t4."MOCNREPLACEIMSISW",
    t4."MOCNREROUTEOPT",
    t4."MOCNROUTEPOLICYGETIMSIFAIL",
    t4."MOCNSELECTCNPOLICY",
    t4."MOCNTIMEOUTREROUTEPERMIT",
    t4."MOCNWAITIDRSPTIMER",
    t4."MRRXQUALSTATMODESW",
    NULL,
    t4."PDCHSTATOPTSW",
    t4."REASSFAILSTATSW",
    t4."REASSIGNINAOIPSW",
    t4."RECLAIMFAILPDRELSW",
    t4."RESENDIDREQSW",
    t4."RETURNOLDCHANOPTSW",
    t4."RXLEVSTATSORTSW",
    t4."SAICWHTMSIDENTALPHALWRTHLD",
    t4."SAICWHTMSIDENTALPHAUPTHLD",
    t4."SAICWHTMSIDENTREQTIMES",
    t4."SAICWHTMSIDENTSATTIMES",
    t4."SAVEUSERPAGINGTMR",
    t4."SECONDDIRECTHOREQSTATSW",
    t4."TRANIMTMALMPROTECTSW",
    t4."USERPRIORITYOPT",
    t4."USRPRITHRES1",
    t4."USRPRITHRES2",
    t4."UTRANCMDECSW",
    t4."UTRANPRIIECTRLSW",
    t4."VIPDTXFORBIDSW",
    t4."VIPPOWERAMP"
FROM
huawei_mml_gsm."BSCEXSOFTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCFCPARA = ReplaceableObject(
    'huawei_cm_2g."BSCFCPARA"',
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
    t1."AINTFCONGSTMINDISCARDRATIO",
    t1."AINTFCONGSTSTATPERIOD",
    t1."AINTFCRNUM",
    t1."AINTFFCDISCLUEN",
    t1."AINTFFCDISCMOCEN",
    t1."AINTFFCDISCMTCEN",
    t1."AINTFFCDISCOSEN",
    t1."AINTFFCEN",
    t1."AINTFFCMETHOD",
    t1."AINTFFCRSRATE1",
    t1."AINTFFCRSRATE2",
    t1."AINTFFCRSRATE3",
    t1."AINTFFCRSRATE4",
    t1."AINTFFCRSRATE5",
    t1."AINTFFCRSRATE6",
    t1."AINTFMSGTHRESHOLD",
    t1."AINTFOCCURATE",
    t1."ATERRSLFCCTRL",
    t1."CHREQCSMAXMSGNUMINPERIOD",
    t1."CHREQPSAVGMSGNUMINPERIOD",
    t1."CHREQSTATPERIOD",
    t1."GCBSFCCPUENDTHD",
    t1."GCBSFCCPUSTARTTHD",
    t1."GCBSFCMSGENDTHD",
    t1."GCBSFCMSGSTARTTHD",
    t1."GCBSFCSUBCPUCTRLTHD",
    t1."GCBSFCSW",
    t1."GCBSMAXMSGNUMINPERIOD",
    t1."GCBSSTATPERIOD",
    t1."LOADBALANCETHD",
    t1."LOCUPMAXMSGINPERIOD",
    t1."MOCACCESSCPURATE",
    t1."MPUFCCTRL",
    t1."MTCACCESSCPURATE",
    t1."P11",
    t1."P12",
    t1."P13",
    t1."P14",
    t1."PFREQCODEMODE",
    t1."PGCLASSIFINGALLOWED",
    t1."PGMAXMSGNUMINPERIOD",
    t1."PGMAXPSMSGNUMINPERIOD",
    t1."PGSTATPERIOD",
    t1."PRIFCEN",
    t1."PSDSPUSAGECTRL",
    t1."PSRESREQMSGNUMINPERIOD",
    t1."PSRESREQSTATPERIOD",
    t1."SCCPCONGSTTHRESHOLD",
    t1."SECONDPSPGFCCTRL",
    t1."SHAREINCPURATE",
    t1."STARTASIGCTRL",
    t1."STARTCBSHORTMSGFLOWCTRL",
    t1."STARTCHREQARRIVALCTRL",
    t1."STARTPGARRIVALCTRL",
    t1."STARTPSRESREQARRIVALCTRL",
    t1."VIPACCESSCPURATE",
    t1."VIPPRIORITY",
    t1."VIPSHAREINCPURATE"
FROM
huawei_nbi_gsm."BSCFCPARA" t1

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
    t2."AINTFCONGSTMINDISCARDRATIO",
    t2."AINTFCONGSTSTATPERIOD",
    t2."AINTFCRNUM",
    t2."AINTFFCDISCLUEN",
    t2."AINTFFCDISCMOCEN",
    t2."AINTFFCDISCMTCEN",
    t2."AINTFFCDISCOSEN",
    t2."AINTFFCEN",
    t2."AINTFFCMETHOD",
    t2."AINTFFCRSRATE1",
    t2."AINTFFCRSRATE2",
    t2."AINTFFCRSRATE3",
    t2."AINTFFCRSRATE4",
    t2."AINTFFCRSRATE5",
    t2."AINTFFCRSRATE6",
    t2."AINTFMSGTHRESHOLD",
    t2."AINTFOCCURATE",
    t2."ATERRSLFCCTRL",
    t2."CHREQCSMAXMSGNUMINPERIOD",
    t2."CHREQPSAVGMSGNUMINPERIOD",
    t2."CHREQSTATPERIOD",
    t2."GCBSFCCPUENDTHD",
    t2."GCBSFCCPUSTARTTHD",
    t2."GCBSFCMSGENDTHD",
    t2."GCBSFCMSGSTARTTHD",
    t2."GCBSFCSUBCPUCTRLTHD",
    t2."GCBSFCSW",
    t2."GCBSMAXMSGNUMINPERIOD",
    t2."GCBSSTATPERIOD",
    t2."LOADBALANCETHD",
    t2."LOCUPMAXMSGINPERIOD",
    t2."MOCACCESSCPURATE",
    t2."MPUFCCTRL",
    t2."MTCACCESSCPURATE",
    t2."P11",
    t2."P12",
    t2."P13",
    t2."P14",
    t2."PFREQCODEMODE",
    t2."PGCLASSIFINGALLOWED",
    t2."PGMAXMSGNUMINPERIOD",
    t2."PGMAXPSMSGNUMINPERIOD",
    t2."PGSTATPERIOD",
    t2."PRIFCEN",
    t2."PSDSPUSAGECTRL",
    t2."PSRESREQMSGNUMINPERIOD",
    t2."PSRESREQSTATPERIOD",
    t2."SCCPCONGSTTHRESHOLD",
    t2."SECONDPSPGFCCTRL",
    t2."SHAREINCPURATE",
    t2."STARTASIGCTRL",
    t2."STARTCBSHORTMSGFLOWCTRL",
    t2."STARTCHREQARRIVALCTRL",
    t2."STARTPGARRIVALCTRL",
    t2."STARTPSRESREQARRIVALCTRL",
    t2."VIPACCESSCPURATE",
    t2."VIPPRIORITY",
    t2."VIPSHAREINCPURATE"
FROM
huawei_gexport_gsm."BSCFCPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AINTFCONGSTMINDISCARDRATIO",
    t3."AINTFCONGSTSTATPERIOD",
    t3."AINTFCRNUM",
    t3."AINTFFCDISCLUEN",
    t3."AINTFFCDISCMOCEN",
    t3."AINTFFCDISCMTCEN",
    t3."AINTFFCDISCOSEN",
    t3."AINTFFCEN",
    t3."AINTFFCMETHOD",
    t3."AINTFFCRSRATE1",
    t3."AINTFFCRSRATE2",
    t3."AINTFFCRSRATE3",
    t3."AINTFFCRSRATE4",
    t3."AINTFFCRSRATE5",
    t3."AINTFFCRSRATE6",
    t3."AINTFMSGTHRESHOLD",
    t3."AINTFOCCURATE",
    t3."ATERRSLFCCTRL",
    t3."CHREQCSMAXMSGNUMINPERIOD",
    t3."CHREQPSAVGMSGNUMINPERIOD",
    t3."CHREQSTATPERIOD",
    t3."GCBSFCCPUENDTHD",
    t3."GCBSFCCPUSTARTTHD",
    t3."GCBSFCMSGENDTHD",
    t3."GCBSFCMSGSTARTTHD",
    t3."GCBSFCSUBCPUCTRLTHD",
    t3."GCBSFCSW",
    t3."GCBSMAXMSGNUMINPERIOD",
    t3."GCBSSTATPERIOD",
    t3."LOADBALANCETHD",
    t3."LOCUPMAXMSGINPERIOD",
    t3."MOCACCESSCPURATE",
    t3."MPUFCCTRL",
    t3."MTCACCESSCPURATE",
    t3."P11",
    t3."P12",
    t3."P13",
    t3."P14",
    t3."PFREQCODEMODE",
    t3."PGCLASSIFINGALLOWED",
    t3."PGMAXMSGNUMINPERIOD",
    t3."PGMAXPSMSGNUMINPERIOD",
    t3."PGSTATPERIOD",
    t3."PRIFCEN",
    t3."PSDSPUSAGECTRL",
    t3."PSRESREQMSGNUMINPERIOD",
    t3."PSRESREQSTATPERIOD",
    t3."SCCPCONGSTTHRESHOLD",
    t3."SECONDPSPGFCCTRL",
    t3."SHAREINCPURATE",
    t3."STARTASIGCTRL",
    t3."STARTCBSHORTMSGFLOWCTRL",
    t3."STARTCHREQARRIVALCTRL",
    t3."STARTPGARRIVALCTRL",
    t3."STARTPSRESREQARRIVALCTRL",
    t3."VIPACCESSCPURATE",
    t3."VIPPRIORITY",
    t3."VIPSHAREINCPURATE"
FROM
huawei_gexport_gsm."BSCFCPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AINTFCONGSTMINDISCARDRATIO",
    t4."AINTFCONGSTSTATPERIOD",
    t4."AINTFCRNUM",
    t4."AINTFFCDISCLUEN",
    t4."AINTFFCDISCMOCEN",
    t4."AINTFFCDISCMTCEN",
    t4."AINTFFCDISCOSEN",
    t4."AINTFFCEN",
    t4."AINTFFCMETHOD",
    t4."AINTFFCRSRATE1",
    t4."AINTFFCRSRATE2",
    t4."AINTFFCRSRATE3",
    t4."AINTFFCRSRATE4",
    t4."AINTFFCRSRATE5",
    t4."AINTFFCRSRATE6",
    t4."AINTFMSGTHRESHOLD",
    t4."AINTFOCCURATE",
    t4."ATERRSLFCCTRL",
    t4."CHREQCSMAXMSGNUMINPERIOD",
    t4."CHREQPSAVGMSGNUMINPERIOD",
    t4."CHREQSTATPERIOD",
    t4."GCBSFCCPUENDTHD",
    t4."GCBSFCCPUSTARTTHD",
    t4."GCBSFCMSGENDTHD",
    t4."GCBSFCMSGSTARTTHD",
    t4."GCBSFCSUBCPUCTRLTHD",
    t4."GCBSFCSW",
    t4."GCBSMAXMSGNUMINPERIOD",
    t4."GCBSSTATPERIOD",
    t4."LOADBALANCETHD",
    t4."LOCUPMAXMSGINPERIOD",
    t4."MOCACCESSCPURATE",
    t4."MPUFCCTRL",
    t4."MTCACCESSCPURATE",
    t4."P11",
    t4."P12",
    t4."P13",
    t4."P14",
    t4."PFREQCODEMODE",
    t4."PGCLASSIFINGALLOWED",
    t4."PGMAXMSGNUMINPERIOD",
    t4."PGMAXPSMSGNUMINPERIOD",
    t4."PGSTATPERIOD",
    t4."PRIFCEN",
    t4."PSDSPUSAGECTRL",
    t4."PSRESREQMSGNUMINPERIOD",
    t4."PSRESREQSTATPERIOD",
    t4."SCCPCONGSTTHRESHOLD",
    t4."SECONDPSPGFCCTRL",
    t4."SHAREINCPURATE",
    t4."STARTASIGCTRL",
    t4."STARTCBSHORTMSGFLOWCTRL",
    t4."STARTCHREQARRIVALCTRL",
    t4."STARTPGARRIVALCTRL",
    t4."STARTPSRESREQARRIVALCTRL",
    t4."VIPACCESSCPURATE",
    t4."VIPPRIORITY",
    t4."VIPSHAREINCPURATE"
FROM
huawei_mml_gsm."BSCFCPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCJBF = ReplaceableObject(
    'huawei_cm_2g."BSCJBF"',
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
    t1."IPOSATJTTTIME",
    t1."JTTADJMAX",
    t1."JTTADJMIN",
    t1."JTTLOSSCNT",
    t1."JTTLOSSPER",
    t1."JTTLOSSPERCALCPERIOD",
    t1."JTTTIME"
FROM
huawei_nbi_gsm."BSCJBF" t1

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
    t2."IPOSATJTTTIME",
    t2."JTTADJMAX",
    t2."JTTADJMIN",
    t2."JTTLOSSCNT",
    t2."JTTLOSSPER",
    t2."JTTLOSSPERCALCPERIOD",
    t2."JTTTIME"
FROM
huawei_gexport_gsm."BSCJBF_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IPOSATJTTTIME",
    t3."JTTADJMAX",
    t3."JTTADJMIN",
    t3."JTTLOSSCNT",
    t3."JTTLOSSPER",
    t3."JTTLOSSPERCALCPERIOD",
    t3."JTTTIME"
FROM
huawei_gexport_gsm."BSCJBF_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IPOSATJTTTIME",
    t4."JTTADJMAX",
    t4."JTTADJMIN",
    t4."JTTLOSSCNT",
    t4."JTTLOSSPER",
    t4."JTTLOSSPERCALCPERIOD",
    t4."JTTTIME"
FROM
huawei_mml_gsm."BSCJBF" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCNSPARA = ReplaceableObject(
    'huawei_cm_2g."BSCNSPARA"',
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
    t1."ALIVERETRY",
    t1."ALIVETIMER",
    t1."BLOCKRETRY",
    t1."BLOCKTIMER",
    t1."RESETRETRY",
    t1."RESETTIMER",
    t1."TESTTIMER",
    t1."UNBLOCKRETRY"
FROM
huawei_nbi_gsm."BSCNSPARA" t1

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
    t2."ALIVERETRY",
    t2."ALIVETIMER",
    t2."BLOCKRETRY",
    t2."BLOCKTIMER",
    t2."RESETRETRY",
    t2."RESETTIMER",
    t2."TESTTIMER",
    t2."UNBLOCKRETRY"
FROM
huawei_gexport_gsm."BSCNSPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALIVERETRY",
    t3."ALIVETIMER",
    t3."BLOCKRETRY",
    t3."BLOCKTIMER",
    t3."RESETRETRY",
    t3."RESETTIMER",
    t3."TESTTIMER",
    t3."UNBLOCKRETRY"
FROM
huawei_gexport_gsm."BSCNSPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALIVERETRY",
    t4."ALIVETIMER",
    t4."BLOCKRETRY",
    t4."BLOCKTIMER",
    t4."RESETRETRY",
    t4."RESETTIMER",
    t4."TESTTIMER",
    t4."UNBLOCKRETRY"
FROM
huawei_mml_gsm."BSCNSPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCPCUTYPE = ReplaceableObject(
    'huawei_cm_2g."BSCPCUTYPE"',
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
    t1."TYPE"
FROM
huawei_nbi_gsm."BSCPCUTYPE" t1

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
    t2."TYPE"
FROM
huawei_gexport_gsm."BSCPCUTYPE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."TYPE"
FROM
huawei_gexport_gsm."BSCPCUTYPE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TYPE"
FROM
huawei_mml_gsm."BSCPCUTYPE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCPSGBPARA = ReplaceableObject(
    'huawei_cm_2g."BSCPSGBPARA"',
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
    t1."DSCPSUPPORT",
    t1."ERRNRIRESUMEPOLICY",
    t1."LLCPDUREORDERTIME",
    t1."SENDRACAPUPDATE",
    t1."SIGERRNRIULMSGPOLICY",
    t1."SIZEFLOWSELFHEALTHD",
    t1."SUPRASTATUS",
    t1."USRULPDUTBITVALUE",
    t1."XIDPDULEN",
    t1."XIDPDUPROC"
FROM
huawei_nbi_gsm."BSCPSGBPARA" t1

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
    t2."DSCPSUPPORT",
    t2."ERRNRIRESUMEPOLICY",
    t2."LLCPDUREORDERTIME",
    t2."SENDRACAPUPDATE",
    t2."SIGERRNRIULMSGPOLICY",
    t2."SIZEFLOWSELFHEALTHD",
    t2."SUPRASTATUS",
    t2."USRULPDUTBITVALUE",
    t2."XIDPDULEN",
    t2."XIDPDUPROC"
FROM
huawei_gexport_gsm."BSCPSGBPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DSCPSUPPORT",
    t3."ERRNRIRESUMEPOLICY",
    t3."LLCPDUREORDERTIME",
    t3."SENDRACAPUPDATE",
    t3."SIGERRNRIULMSGPOLICY",
    t3."SIZEFLOWSELFHEALTHD",
    t3."SUPRASTATUS",
    t3."USRULPDUTBITVALUE",
    t3."XIDPDULEN",
    t3."XIDPDUPROC"
FROM
huawei_gexport_gsm."BSCPSGBPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DSCPSUPPORT",
    t4."ERRNRIRESUMEPOLICY",
    t4."LLCPDUREORDERTIME",
    t4."SENDRACAPUPDATE",
    t4."SIGERRNRIULMSGPOLICY",
    t4."SIZEFLOWSELFHEALTHD",
    t4."SUPRASTATUS",
    t4."USRULPDUTBITVALUE",
    t4."XIDPDULEN",
    t4."XIDPDUPROC"
FROM
huawei_mml_gsm."BSCPSGBPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCPSSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."BSCPSSOFTPARA"',
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
    t1."ABISIPPDCHRESYNSW",
    t1."ACTIVETBFBUFFRPTINTERVAL",
    t1."ADDTRANSBWINT",
    t1."ADDTRANSBWNUM",
    t1."ALLOWEDADAMULTIPLEX",
    t1."APPSLVABISAFTERPDALLOC",
    t1."AQMM",
    t1."AQMMAXTH",
    t1."AQMMINTH",
    t1."AQMNINIT",
    t1."AQMNLOWERBOUND",
    t1."AQMNUPBOUND",
    t1."AQMSWITCH",
    t1."AQMTARTH",
    t1."BADVESTDLTBF",
    t1."BSCPSRESERVEPARA2",
    t1."BSCPSRESERVEPARA3",
    t1."BSCPSRESERVEPARA4",
    t1."CELLDISTOPTSW",
    t1."CELLDISTPERSISTENTSW",
    t1."CELLDYNDISTOPT",
    t1."CELLDYNDISTSWITCH",
    t1."CELLMIGINPDCHRESVTHRES",
    t1."CELLMIGOUTPDCHFAILTHRES",
    t1."CELLRESELTRAFFICCONTINUE",
    t1."CHECKLVDSTHD",
    t1."CONVERTPDCHTRXPRISW",
    t1."DECGMMPDULIFETIME",
    t1."DLCOEFFICIENTTSRAPIDADJ",
    t1."DLFIRSTBLKPOLLING",
    t1."DLNONACCSTOPREROUTESW",
    t1."DTMIMMAPPLYSLAVEABIS",
    t1."EGPRSACCFAILASSGPRS",
    t1."FLOWCOUNTPERIODTICKS",
    t1."FLOWCOUNTPERIODTSRAPIDADJ",
    t1."FORBIDEDGU",
    t1."FORCE2PHASE",
    t1."FORCEMSTRAFFICCLASS",
    t1."FORCERELTBFDURATION",
    t1."GMMLOWCODESW",
    t1."GPRSDLRETRANRATESTAT",
    t1."IPCELLPDCHACTFAILPENSW",
    t1."LOADBROADCASTPERIOD",
    t1."MAXDLASSRETRYTIMES",
    t1."MAXDLESTRETRYNUM",
    t1."MAXPOLLINGRETRYTIMES",
    t1."MCBSPSELFHEALSW",
    t1."MCS3PASMCS3",
    t1."MOCNREJECTCAUSEPOLICY",
    t1."MSCONTEXTLIFETIME",
    t1."N3101OVERFLOWDEGRADECS",
    t1."NC2LOADRESEL",
    t1."NSLINKFAULTTRACESW",
    t1."PDCHACTCTRLSW",
    t1."PDCHACTFAILPENTIME",
    t1."PDCHAPPLYTIMEOUTRELSW",
    t1."PKTREASSPROTECTINTERVAL",
    t1."PMOADDFREQALLOW",
    t1."PSCELLDYNADJRATIO",
    t1."PSCELLDYNADJTIME",
    t1."PSCELLTABSELFHEALSW",
    t1."PSCHRIDREQTLLIPOLICY",
    t1."PSUPBRDMIXCELLDISTOPTSW",
    t1."PSUPSELFHEALACCNUMTHD",
    t1."PSUPSELFHEALACCSUCCTHD",
    t1."PSUPSELFHEALPERIOD",
    t1."READYTIMER",
    t1."REDUCETRANSBWINT",
    t1."REDUCETRANSBWNUM",
    t1."RELFLEXABISFORLDR",
    t1."RIMONECOSW",
    t1."RSTPSCELLPDCHCFGCHG",
    t1."RTTISCHED",
    t1."SENDDUMMYAFTERULASSSW",
    t1."SILENCETICKSOFRESREQ",
    t1."SPTDLTBFSCHEDOPTIMIZE",
    t1."SPTNACCRESGUARANTEE",
    t1."STALLNACKBLKPOLLING",
    t1."STOPPSLDRPOLICY",
    t1."SUPPORTDL5TS",
    t1."SUPPORTDLDCFORBE",
    t1."SUPPORTEDA",
    t1."TDMBCCHDTXSW",
    t1."TIMERLEADPDCHACTFAILSW",
    t1."TRAFFICCLASSDLCOEFFICIENT",
    t1."TRAFFICCLASSULCOEFFICIENT",
    t1."TRXRESRELSW",
    t1."TSRAPIDADJPERIOD",
    t1."TSRAPIDADJSWITCH",
    t1."ULBEPINTERPOLATION",
    t1."ULCOEFFICIENTTSRAPIDADJ",
    t1."ULCSADJFORABISREL",
    t1."ULDLACKFREQ",
    t1."ULDUMMYSTATSW",
    t1."ULEGPRSDLACKFREQ",
    t1."ULEGPRSULACKFREQ",
    t1."ULULACKFREQ",
    t1."USFDUMMYPCPOLICY",
    t1."USFGRAN4BLK",
    t1."WIFIINTERWORKINGSWITCH"
FROM
huawei_nbi_gsm."BSCPSSOFTPARA" t1

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
    t2."ABISIPPDCHRESYNSW",
    t2."ACTIVETBFBUFFRPTINTERVAL",
    t2."ADDTRANSBWINT",
    t2."ADDTRANSBWNUM",
    t2."ALLOWEDADAMULTIPLEX",
    t2."APPSLVABISAFTERPDALLOC",
    t2."AQMM",
    t2."AQMMAXTH",
    t2."AQMMINTH",
    t2."AQMNINIT",
    t2."AQMNLOWERBOUND",
    t2."AQMNUPBOUND",
    t2."AQMSWITCH",
    t2."AQMTARTH",
    t2."BADVESTDLTBF",
    t2."BSCPSRESERVEPARA2",
    t2."BSCPSRESERVEPARA3",
    t2."BSCPSRESERVEPARA4",
    t2."CELLDISTOPTSW",
    t2."CELLDISTPERSISTENTSW",
    t2."CELLDYNDISTOPT",
    t2."CELLDYNDISTSWITCH",
    t2."CELLMIGINPDCHRESVTHRES",
    t2."CELLMIGOUTPDCHFAILTHRES",
    t2."CELLRESELTRAFFICCONTINUE",
    t2."CHECKLVDSTHD",
    t2."CONVERTPDCHTRXPRISW",
    t2."DECGMMPDULIFETIME",
    t2."DLCOEFFICIENTTSRAPIDADJ",
    t2."DLFIRSTBLKPOLLING",
    t2."DLNONACCSTOPREROUTESW",
    t2."DTMIMMAPPLYSLAVEABIS",
    t2."EGPRSACCFAILASSGPRS",
    t2."FLOWCOUNTPERIODTICKS",
    t2."FLOWCOUNTPERIODTSRAPIDADJ",
    t2."FORBIDEDGU",
    t2."FORCE2PHASE",
    t2."FORCEMSTRAFFICCLASS",
    t2."FORCERELTBFDURATION",
    t2."GMMLOWCODESW",
    t2."GPRSDLRETRANRATESTAT",
    t2."IPCELLPDCHACTFAILPENSW",
    t2."LOADBROADCASTPERIOD",
    t2."MAXDLASSRETRYTIMES",
    t2."MAXDLESTRETRYNUM",
    t2."MAXPOLLINGRETRYTIMES",
    t2."MCBSPSELFHEALSW",
    t2."MCS3PASMCS3",
    NULL,
    t2."MSCONTEXTLIFETIME",
    t2."N3101OVERFLOWDEGRADECS",
    t2."NC2LOADRESEL",
    t2."NSLINKFAULTTRACESW",
    t2."PDCHACTCTRLSW",
    t2."PDCHACTFAILPENTIME",
    t2."PDCHAPPLYTIMEOUTRELSW",
    t2."PKTREASSPROTECTINTERVAL",
    t2."PMOADDFREQALLOW",
    t2."PSCELLDYNADJRATIO",
    t2."PSCELLDYNADJTIME",
    t2."PSCELLTABSELFHEALSW",
    t2."PSCHRIDREQTLLIPOLICY",
    t2."PSUPBRDMIXCELLDISTOPTSW",
    t2."PSUPSELFHEALACCNUMTHD",
    t2."PSUPSELFHEALACCSUCCTHD",
    t2."PSUPSELFHEALPERIOD",
    t2."READYTIMER",
    t2."REDUCETRANSBWINT",
    t2."REDUCETRANSBWNUM",
    t2."RELFLEXABISFORLDR",
    t2."RIMONECOSW",
    t2."RSTPSCELLPDCHCFGCHG",
    t2."RTTISCHED",
    t2."SENDDUMMYAFTERULASSSW",
    t2."SILENCETICKSOFRESREQ",
    t2."SPTDLTBFSCHEDOPTIMIZE",
    t2."SPTNACCRESGUARANTEE",
    t2."STALLNACKBLKPOLLING",
    t2."STOPPSLDRPOLICY",
    t2."SUPPORTDL5TS",
    t2."SUPPORTDLDCFORBE",
    t2."SUPPORTEDA",
    t2."TDMBCCHDTXSW",
    t2."TIMERLEADPDCHACTFAILSW",
    t2."TRAFFICCLASSDLCOEFFICIENT",
    t2."TRAFFICCLASSULCOEFFICIENT",
    t2."TRXRESRELSW",
    t2."TSRAPIDADJPERIOD",
    t2."TSRAPIDADJSWITCH",
    t2."ULBEPINTERPOLATION",
    t2."ULCOEFFICIENTTSRAPIDADJ",
    t2."ULCSADJFORABISREL",
    t2."ULDLACKFREQ",
    t2."ULDUMMYSTATSW",
    t2."ULEGPRSDLACKFREQ",
    t2."ULEGPRSULACKFREQ",
    t2."ULULACKFREQ",
    t2."USFDUMMYPCPOLICY",
    t2."USFGRAN4BLK",
    t2."WIFIINTERWORKINGSWITCH"
FROM
huawei_gexport_gsm."BSCPSSOFTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISIPPDCHRESYNSW",
    t3."ACTIVETBFBUFFRPTINTERVAL",
    t3."ADDTRANSBWINT",
    t3."ADDTRANSBWNUM",
    t3."ALLOWEDADAMULTIPLEX",
    t3."APPSLVABISAFTERPDALLOC",
    t3."AQMM",
    t3."AQMMAXTH",
    t3."AQMMINTH",
    t3."AQMNINIT",
    t3."AQMNLOWERBOUND",
    t3."AQMNUPBOUND",
    t3."AQMSWITCH",
    t3."AQMTARTH",
    t3."BADVESTDLTBF",
    t3."BSCPSRESERVEPARA2",
    t3."BSCPSRESERVEPARA3",
    t3."BSCPSRESERVEPARA4",
    t3."CELLDISTOPTSW",
    t3."CELLDISTPERSISTENTSW",
    t3."CELLDYNDISTOPT",
    t3."CELLDYNDISTSWITCH",
    t3."CELLMIGINPDCHRESVTHRES",
    t3."CELLMIGOUTPDCHFAILTHRES",
    t3."CELLRESELTRAFFICCONTINUE",
    t3."CHECKLVDSTHD",
    t3."CONVERTPDCHTRXPRISW",
    t3."DECGMMPDULIFETIME",
    t3."DLCOEFFICIENTTSRAPIDADJ",
    t3."DLFIRSTBLKPOLLING",
    t3."DLNONACCSTOPREROUTESW",
    t3."DTMIMMAPPLYSLAVEABIS",
    t3."EGPRSACCFAILASSGPRS",
    t3."FLOWCOUNTPERIODTICKS",
    t3."FLOWCOUNTPERIODTSRAPIDADJ",
    t3."FORBIDEDGU",
    t3."FORCE2PHASE",
    t3."FORCEMSTRAFFICCLASS",
    t3."FORCERELTBFDURATION",
    t3."GMMLOWCODESW",
    t3."GPRSDLRETRANRATESTAT",
    t3."IPCELLPDCHACTFAILPENSW",
    t3."LOADBROADCASTPERIOD",
    t3."MAXDLASSRETRYTIMES",
    t3."MAXDLESTRETRYNUM",
    t3."MAXPOLLINGRETRYTIMES",
    t3."MCBSPSELFHEALSW",
    t3."MCS3PASMCS3",
    NULL,
    t3."MSCONTEXTLIFETIME",
    t3."N3101OVERFLOWDEGRADECS",
    t3."NC2LOADRESEL",
    t3."NSLINKFAULTTRACESW",
    t3."PDCHACTCTRLSW",
    t3."PDCHACTFAILPENTIME",
    t3."PDCHAPPLYTIMEOUTRELSW",
    t3."PKTREASSPROTECTINTERVAL",
    t3."PMOADDFREQALLOW",
    t3."PSCELLDYNADJRATIO",
    t3."PSCELLDYNADJTIME",
    t3."PSCELLTABSELFHEALSW",
    t3."PSCHRIDREQTLLIPOLICY",
    t3."PSUPBRDMIXCELLDISTOPTSW",
    t3."PSUPSELFHEALACCNUMTHD",
    t3."PSUPSELFHEALACCSUCCTHD",
    t3."PSUPSELFHEALPERIOD",
    t3."READYTIMER",
    t3."REDUCETRANSBWINT",
    t3."REDUCETRANSBWNUM",
    t3."RELFLEXABISFORLDR",
    t3."RIMONECOSW",
    t3."RSTPSCELLPDCHCFGCHG",
    t3."RTTISCHED",
    t3."SENDDUMMYAFTERULASSSW",
    t3."SILENCETICKSOFRESREQ",
    t3."SPTDLTBFSCHEDOPTIMIZE",
    t3."SPTNACCRESGUARANTEE",
    t3."STALLNACKBLKPOLLING",
    t3."STOPPSLDRPOLICY",
    t3."SUPPORTDL5TS",
    t3."SUPPORTDLDCFORBE",
    t3."SUPPORTEDA",
    t3."TDMBCCHDTXSW",
    t3."TIMERLEADPDCHACTFAILSW",
    t3."TRAFFICCLASSDLCOEFFICIENT",
    t3."TRAFFICCLASSULCOEFFICIENT",
    t3."TRXRESRELSW",
    t3."TSRAPIDADJPERIOD",
    t3."TSRAPIDADJSWITCH",
    t3."ULBEPINTERPOLATION",
    t3."ULCOEFFICIENTTSRAPIDADJ",
    t3."ULCSADJFORABISREL",
    t3."ULDLACKFREQ",
    t3."ULDUMMYSTATSW",
    t3."ULEGPRSDLACKFREQ",
    t3."ULEGPRSULACKFREQ",
    t3."ULULACKFREQ",
    t3."USFDUMMYPCPOLICY",
    t3."USFGRAN4BLK",
    t3."WIFIINTERWORKINGSWITCH"
FROM
huawei_gexport_gsm."BSCPSSOFTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISIPPDCHRESYNSW",
    t4."ACTIVETBFBUFFRPTINTERVAL",
    t4."ADDTRANSBWINT",
    t4."ADDTRANSBWNUM",
    t4."ALLOWEDADAMULTIPLEX",
    t4."APPSLVABISAFTERPDALLOC",
    t4."AQMM",
    t4."AQMMAXTH",
    t4."AQMMINTH",
    t4."AQMNINIT",
    t4."AQMNLOWERBOUND",
    t4."AQMNUPBOUND",
    t4."AQMSWITCH",
    t4."AQMTARTH",
    t4."BADVESTDLTBF",
    t4."BSCPSRESERVEPARA2",
    t4."BSCPSRESERVEPARA3",
    t4."BSCPSRESERVEPARA4",
    t4."CELLDISTOPTSW",
    t4."CELLDISTPERSISTENTSW",
    t4."CELLDYNDISTOPT",
    t4."CELLDYNDISTSWITCH",
    t4."CELLMIGINPDCHRESVTHRES",
    t4."CELLMIGOUTPDCHFAILTHRES",
    t4."CELLRESELTRAFFICCONTINUE",
    t4."CHECKLVDSTHD",
    t4."CONVERTPDCHTRXPRISW",
    t4."DECGMMPDULIFETIME",
    t4."DLCOEFFICIENTTSRAPIDADJ",
    t4."DLFIRSTBLKPOLLING",
    t4."DLNONACCSTOPREROUTESW",
    t4."DTMIMMAPPLYSLAVEABIS",
    t4."EGPRSACCFAILASSGPRS",
    t4."FLOWCOUNTPERIODTICKS",
    t4."FLOWCOUNTPERIODTSRAPIDADJ",
    t4."FORBIDEDGU",
    t4."FORCE2PHASE",
    t4."FORCEMSTRAFFICCLASS",
    t4."FORCERELTBFDURATION",
    t4."GMMLOWCODESW",
    t4."GPRSDLRETRANRATESTAT",
    t4."IPCELLPDCHACTFAILPENSW",
    t4."LOADBROADCASTPERIOD",
    t4."MAXDLASSRETRYTIMES",
    t4."MAXDLESTRETRYNUM",
    t4."MAXPOLLINGRETRYTIMES",
    t4."MCBSPSELFHEALSW",
    t4."MCS3PASMCS3",
    NULL,
    t4."MSCONTEXTLIFETIME",
    t4."N3101OVERFLOWDEGRADECS",
    t4."NC2LOADRESEL",
    t4."NSLINKFAULTTRACESW",
    t4."PDCHACTCTRLSW",
    t4."PDCHACTFAILPENTIME",
    t4."PDCHAPPLYTIMEOUTRELSW",
    t4."PKTREASSPROTECTINTERVAL",
    t4."PMOADDFREQALLOW",
    t4."PSCELLDYNADJRATIO",
    t4."PSCELLDYNADJTIME",
    t4."PSCELLTABSELFHEALSW",
    t4."PSCHRIDREQTLLIPOLICY",
    t4."PSUPBRDMIXCELLDISTOPTSW",
    t4."PSUPSELFHEALACCNUMTHD",
    t4."PSUPSELFHEALACCSUCCTHD",
    t4."PSUPSELFHEALPERIOD",
    t4."READYTIMER",
    t4."REDUCETRANSBWINT",
    t4."REDUCETRANSBWNUM",
    t4."RELFLEXABISFORLDR",
    t4."RIMONECOSW",
    t4."RSTPSCELLPDCHCFGCHG",
    t4."RTTISCHED",
    t4."SENDDUMMYAFTERULASSSW",
    t4."SILENCETICKSOFRESREQ",
    t4."SPTDLTBFSCHEDOPTIMIZE",
    t4."SPTNACCRESGUARANTEE",
    t4."STALLNACKBLKPOLLING",
    t4."STOPPSLDRPOLICY",
    t4."SUPPORTDL5TS",
    t4."SUPPORTDLDCFORBE",
    t4."SUPPORTEDA",
    t4."TDMBCCHDTXSW",
    t4."TIMERLEADPDCHACTFAILSW",
    t4."TRAFFICCLASSDLCOEFFICIENT",
    t4."TRAFFICCLASSULCOEFFICIENT",
    t4."TRXRESRELSW",
    t4."TSRAPIDADJPERIOD",
    t4."TSRAPIDADJSWITCH",
    t4."ULBEPINTERPOLATION",
    t4."ULCOEFFICIENTTSRAPIDADJ",
    t4."ULCSADJFORABISREL",
    t4."ULDLACKFREQ",
    t4."ULDUMMYSTATSW",
    t4."ULEGPRSDLACKFREQ",
    t4."ULEGPRSULACKFREQ",
    t4."ULULACKFREQ",
    t4."USFDUMMYPCPOLICY",
    t4."USFGRAN4BLK",
    t4."WIFIINTERWORKINGSWITCH"
FROM
huawei_mml_gsm."BSCPSSOFTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCPSSTAT = ReplaceableObject(
    'huawei_cm_2g."BSCPSSTAT"',
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
    t1."DLTBFSTATINIPCELL",
    t1."DLTBFSTATINTDMCELL",
    t1."FAKEPDUSTAT",
    t1."LLCPDUBNUMSTATMODE",
    t1."LLCPDUTHRUPUTSTATMODE",
    t1."LLCTHRUPUTCALCPERIOD",
    t1."PSUSRAWAREDLBIGPKTTHD",
    t1."PSUSRAWAREFLOWCNTTHD",
    t1."PSUSRAWARERATETHD",
    t1."PSUSRAWARETBFABNINTTIME",
    t1."PSUSRAWARETBFNORINTTIME",
    t1."RLCBLOCKSTATMODE",
    t1."STATDLPACKINDELAYREL",
    t1."STATDMYPDUINDELAYREL",
    t1."STATFLUSHLLINABNTBFREL",
    t1."STATLLCTRANSDURA",
    t1."STATULBLKWHENDELAYREL",
    t1."TRANSINTSTATMODE",
    t1."ULTBFABNRELINACT"
FROM
huawei_nbi_gsm."BSCPSSTAT" t1

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
    t2."DLTBFSTATINIPCELL",
    t2."DLTBFSTATINTDMCELL",
    t2."FAKEPDUSTAT",
    t2."LLCPDUBNUMSTATMODE",
    t2."LLCPDUTHRUPUTSTATMODE",
    t2."LLCTHRUPUTCALCPERIOD",
    t2."PSUSRAWAREDLBIGPKTTHD",
    t2."PSUSRAWAREFLOWCNTTHD",
    t2."PSUSRAWARERATETHD",
    t2."PSUSRAWARETBFABNINTTIME",
    t2."PSUSRAWARETBFNORINTTIME",
    t2."RLCBLOCKSTATMODE",
    t2."STATDLPACKINDELAYREL",
    t2."STATDMYPDUINDELAYREL",
    t2."STATFLUSHLLINABNTBFREL",
    t2."STATLLCTRANSDURA",
    t2."STATULBLKWHENDELAYREL",
    t2."TRANSINTSTATMODE",
    t2."ULTBFABNRELINACT"
FROM
huawei_gexport_gsm."BSCPSSTAT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DLTBFSTATINIPCELL",
    t3."DLTBFSTATINTDMCELL",
    t3."FAKEPDUSTAT",
    t3."LLCPDUBNUMSTATMODE",
    t3."LLCPDUTHRUPUTSTATMODE",
    t3."LLCTHRUPUTCALCPERIOD",
    t3."PSUSRAWAREDLBIGPKTTHD",
    t3."PSUSRAWAREFLOWCNTTHD",
    t3."PSUSRAWARERATETHD",
    t3."PSUSRAWARETBFABNINTTIME",
    t3."PSUSRAWARETBFNORINTTIME",
    t3."RLCBLOCKSTATMODE",
    t3."STATDLPACKINDELAYREL",
    t3."STATDMYPDUINDELAYREL",
    t3."STATFLUSHLLINABNTBFREL",
    t3."STATLLCTRANSDURA",
    t3."STATULBLKWHENDELAYREL",
    t3."TRANSINTSTATMODE",
    t3."ULTBFABNRELINACT"
FROM
huawei_gexport_gsm."BSCPSSTAT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DLTBFSTATINIPCELL",
    t4."DLTBFSTATINTDMCELL",
    t4."FAKEPDUSTAT",
    t4."LLCPDUBNUMSTATMODE",
    t4."LLCPDUTHRUPUTSTATMODE",
    t4."LLCTHRUPUTCALCPERIOD",
    t4."PSUSRAWAREDLBIGPKTTHD",
    t4."PSUSRAWAREFLOWCNTTHD",
    t4."PSUSRAWARERATETHD",
    t4."PSUSRAWARETBFABNINTTIME",
    t4."PSUSRAWARETBFNORINTTIME",
    t4."RLCBLOCKSTATMODE",
    t4."STATDLPACKINDELAYREL",
    t4."STATDMYPDUINDELAYREL",
    t4."STATFLUSHLLINABNTBFREL",
    t4."STATLLCTRANSDURA",
    t4."STATULBLKWHENDELAYREL",
    t4."TRANSINTSTATMODE",
    t4."ULTBFABNRELINACT"
FROM
huawei_mml_gsm."BSCPSSTAT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCPSTCDSCPMAP = ReplaceableObject(
    'huawei_cm_2g."BSCPSTCDSCPMAP"',
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
    t1."BCDSCP",
    t1."CCDSCP",
    t1."ICTHP1DSCP",
    t1."ICTHP2DSCP",
    t1."ICTHP3DSCP",
    t1."SCDSCP",
    t1."SDSCP"
FROM
huawei_nbi_gsm."BSCPSTCDSCPMAP" t1

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
    t2."BCDSCP",
    t2."CCDSCP",
    t2."ICTHP1DSCP",
    t2."ICTHP2DSCP",
    t2."ICTHP3DSCP",
    t2."SCDSCP",
    t2."SDSCP"
FROM
huawei_gexport_gsm."BSCPSTCDSCPMAP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BCDSCP",
    t3."CCDSCP",
    t3."ICTHP1DSCP",
    t3."ICTHP2DSCP",
    t3."ICTHP3DSCP",
    t3."SCDSCP",
    t3."SDSCP"
FROM
huawei_gexport_gsm."BSCPSTCDSCPMAP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BCDSCP",
    t4."CCDSCP",
    t4."ICTHP1DSCP",
    t4."ICTHP2DSCP",
    t4."ICTHP3DSCP",
    t4."SCDSCP",
    t4."SDSCP"
FROM
huawei_mml_gsm."BSCPSTCDSCPMAP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCPSUMPARA = ReplaceableObject(
    'huawei_cm_2g."BSCPSUMPARA"',
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
    t1."ADDITIONALMSRACAP",
    t1."CONTENTIONRESOLUTIONOPT",
    t1."CONTENTRESOLUTPOLICY",
    t1."DLASSMSREACTIONTIME",
    t1."DLASSONULCHANSWITCHING",
    t1."DLIMMASSDELAYDRX",
    t1."DLIMMASSDELAYNONDRX",
    t1."DLIMMASSWITHP0SW",
    t1."DLRESREASSONRAUPDATE",
    t1."DLRESREASSQOSCHANGESW",
    t1."DLTBFADVESTONULONEBLK",
    t1."IGNOREPKTRESREQ",
    t1."IGRRESREQDURULRELSW",
    t1."PACCHDLESTSW",
    t1."PKTDLASSWITHULPWCTRL",
    t1."QUICKSTARTDLONIMMASSSW",
    t1."QUICKSTARTDLTBFONDL",
    t1."QUICKSTARTDLTBFONUL",
    t1."RESENDDLPACKETASS",
    t1."RESENDULPACKETASS",
    t1."SENDPKTULACCREJ",
    t1."SENDSINGLEASSCCCHOVLD",
    t1."SENDTBFREL",
    t1."SENDULREASS",
    t1."SETDLEGPRSTBFTORLCACKMODE",
    t1."SETDLGPRSTBFTORLCACKMODE",
    t1."SINGLEASSDELAY",
    t1."T3193ACCURATECALCSW",
    t1."T3193DLDELAYESTBINTERVAL",
    t1."TBFEXISTTIMEBEFORETS",
    t1."TLLIBLKCHANCOD",
    t1."TSINTERVAL",
    t1."ULABNORRESREQPROCSW",
    t1."ULASSMSREACTIONTIME",
    t1."ULIMMASSDELAY"
FROM
huawei_nbi_gsm."BSCPSUMPARA" t1

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
    t2."ADDITIONALMSRACAP",
    t2."CONTENTIONRESOLUTIONOPT",
    t2."CONTENTRESOLUTPOLICY",
    t2."DLASSMSREACTIONTIME",
    t2."DLASSONULCHANSWITCHING",
    t2."DLIMMASSDELAYDRX",
    t2."DLIMMASSDELAYNONDRX",
    t2."DLIMMASSWITHP0SW",
    t2."DLRESREASSONRAUPDATE",
    t2."DLRESREASSQOSCHANGESW",
    t2."DLTBFADVESTONULONEBLK",
    t2."IGNOREPKTRESREQ",
    t2."IGRRESREQDURULRELSW",
    t2."PACCHDLESTSW",
    t2."PKTDLASSWITHULPWCTRL",
    t2."QUICKSTARTDLONIMMASSSW",
    t2."QUICKSTARTDLTBFONDL",
    t2."QUICKSTARTDLTBFONUL",
    t2."RESENDDLPACKETASS",
    t2."RESENDULPACKETASS",
    t2."SENDPKTULACCREJ",
    t2."SENDSINGLEASSCCCHOVLD",
    t2."SENDTBFREL",
    t2."SENDULREASS",
    t2."SETDLEGPRSTBFTORLCACKMODE",
    t2."SETDLGPRSTBFTORLCACKMODE",
    t2."SINGLEASSDELAY",
    t2."T3193ACCURATECALCSW",
    t2."T3193DLDELAYESTBINTERVAL",
    t2."TBFEXISTTIMEBEFORETS",
    t2."TLLIBLKCHANCOD",
    t2."TSINTERVAL",
    t2."ULABNORRESREQPROCSW",
    t2."ULASSMSREACTIONTIME",
    t2."ULIMMASSDELAY"
FROM
huawei_gexport_gsm."BSCPSUMPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADDITIONALMSRACAP",
    t3."CONTENTIONRESOLUTIONOPT",
    t3."CONTENTRESOLUTPOLICY",
    t3."DLASSMSREACTIONTIME",
    t3."DLASSONULCHANSWITCHING",
    t3."DLIMMASSDELAYDRX",
    t3."DLIMMASSDELAYNONDRX",
    t3."DLIMMASSWITHP0SW",
    t3."DLRESREASSONRAUPDATE",
    t3."DLRESREASSQOSCHANGESW",
    t3."DLTBFADVESTONULONEBLK",
    t3."IGNOREPKTRESREQ",
    t3."IGRRESREQDURULRELSW",
    t3."PACCHDLESTSW",
    t3."PKTDLASSWITHULPWCTRL",
    t3."QUICKSTARTDLONIMMASSSW",
    t3."QUICKSTARTDLTBFONDL",
    t3."QUICKSTARTDLTBFONUL",
    t3."RESENDDLPACKETASS",
    t3."RESENDULPACKETASS",
    t3."SENDPKTULACCREJ",
    t3."SENDSINGLEASSCCCHOVLD",
    t3."SENDTBFREL",
    t3."SENDULREASS",
    t3."SETDLEGPRSTBFTORLCACKMODE",
    t3."SETDLGPRSTBFTORLCACKMODE",
    t3."SINGLEASSDELAY",
    t3."T3193ACCURATECALCSW",
    t3."T3193DLDELAYESTBINTERVAL",
    t3."TBFEXISTTIMEBEFORETS",
    t3."TLLIBLKCHANCOD",
    t3."TSINTERVAL",
    t3."ULABNORRESREQPROCSW",
    t3."ULASSMSREACTIONTIME",
    t3."ULIMMASSDELAY"
FROM
huawei_gexport_gsm."BSCPSUMPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADDITIONALMSRACAP",
    t4."CONTENTIONRESOLUTIONOPT",
    t4."CONTENTRESOLUTPOLICY",
    t4."DLASSMSREACTIONTIME",
    t4."DLASSONULCHANSWITCHING",
    t4."DLIMMASSDELAYDRX",
    t4."DLIMMASSDELAYNONDRX",
    t4."DLIMMASSWITHP0SW",
    t4."DLRESREASSONRAUPDATE",
    t4."DLRESREASSQOSCHANGESW",
    t4."DLTBFADVESTONULONEBLK",
    t4."IGNOREPKTRESREQ",
    t4."IGRRESREQDURULRELSW",
    t4."PACCHDLESTSW",
    t4."PKTDLASSWITHULPWCTRL",
    t4."QUICKSTARTDLONIMMASSSW",
    t4."QUICKSTARTDLTBFONDL",
    t4."QUICKSTARTDLTBFONUL",
    t4."RESENDDLPACKETASS",
    t4."RESENDULPACKETASS",
    t4."SENDPKTULACCREJ",
    t4."SENDSINGLEASSCCCHOVLD",
    t4."SENDTBFREL",
    t4."SENDULREASS",
    t4."SETDLEGPRSTBFTORLCACKMODE",
    t4."SETDLGPRSTBFTORLCACKMODE",
    t4."SINGLEASSDELAY",
    t4."T3193ACCURATECALCSW",
    t4."T3193DLDELAYESTBINTERVAL",
    t4."TBFEXISTTIMEBEFORETS",
    t4."TLLIBLKCHANCOD",
    t4."TSINTERVAL",
    t4."ULABNORRESREQPROCSW",
    t4."ULASSMSREACTIONTIME",
    t4."ULIMMASSDELAY"
FROM
huawei_mml_gsm."BSCPSUMPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCSIGTRC = ReplaceableObject(
    'huawei_cm_2g."BSCSIGTRC"',
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
    t1."ABISTIFMSGTYPE",
    t1."ATIFMSGTYPE",
    t1."LOGRPTPERIOD",
    t1."MRLOGNCELLTYPE",
    t1."TRCMSGIND"
FROM
huawei_nbi_gsm."BSCSIGTRC" t1

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
    NULL,
    t2."LOGRPTPERIOD",
    t2."MRLOGNCELLTYPE",
    t2."TRCMSGIND"
FROM
huawei_gexport_gsm."BSCSIGTRC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    NULL,
    t3."LOGRPTPERIOD",
    t3."MRLOGNCELLTYPE",
    t3."TRCMSGIND"
FROM
huawei_gexport_gsm."BSCSIGTRC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LOGRPTPERIOD",
    t4."MRLOGNCELLTYPE",
    t4."TRCMSGIND"
FROM
huawei_mml_gsm."BSCSIGTRC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCTESTPARA = ReplaceableObject(
    'huawei_cm_2g."BSCTESTPARA"',
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
    t1."DTMFLOOPSWITCH",
    t1."VOICEOPENTRACECELL",
    t1."VOICEOPENTRACENODE",
    t1."VOICEOPENTRACESPVER",
    t1."VOICEOPENTRACESSN",
    t1."VOICEOPENTRACETPYE"
FROM
huawei_nbi_gsm."BSCTESTPARA" t1

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
    t2."DTMFLOOPSWITCH",
    t2."VOICEOPENTRACECELL",
    NULL,
    NULL,
    t2."VOICEOPENTRACESSN",
    NULL
FROM
huawei_gexport_gsm."BSCTESTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DTMFLOOPSWITCH",
    t3."VOICEOPENTRACECELL",
    NULL,
    NULL,
    t3."VOICEOPENTRACESSN",
    NULL
FROM
huawei_gexport_gsm."BSCTESTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DTMFLOOPSWITCH",
    t4."VOICEOPENTRACECELL",
    NULL,
    NULL,
    t4."VOICEOPENTRACESSN",
    NULL
FROM
huawei_mml_gsm."BSCTESTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSCTMR = ReplaceableObject(
    'huawei_cm_2g."BSCTMR"',
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
    t1."ABISFCTIMER1",
    t1."ABISFCTIMER2",
    t1."AT1",
    t1."AT19",
    t1."AT20",
    t1."BMTCFCTIMERLEN",
    t1."CBNONMSGTIMER",
    t1."CBSHAKEHANDTIMER",
    t1."EXTCELLLOADINVALIDTIMER",
    t1."MSCCLRCMDTMR",
    t1."PROHIBTRPTCELLLOAD",
    t1."RELITFACONNTMR",
    t1."RESCHKSTARTTM",
    t1."RESCHKSTPTM",
    t1."RESINDPERIOD",
    t1."SDBACK2TCHJDG",
    t1."TCHSDDYNADJCHK",
    t1."TI_WAIT_SGSN_PRIVATE_MESSAGE",
    t1."TRBSS",
    t1."WAITCHNADJ"
FROM
huawei_nbi_gsm."BSCTMR" t1

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
    t2."ABISFCTIMER1",
    t2."ABISFCTIMER2",
    t2."AT1",
    t2."AT19",
    t2."AT20",
    t2."BMTCFCTIMERLEN",
    t2."CBNONMSGTIMER",
    t2."CBSHAKEHANDTIMER",
    t2."EXTCELLLOADINVALIDTIMER",
    t2."MSCCLRCMDTMR",
    t2."PROHIBTRPTCELLLOAD",
    t2."RELITFACONNTMR",
    t2."RESCHKSTARTTM",
    t2."RESCHKSTPTM",
    t2."RESINDPERIOD",
    t2."SDBACK2TCHJDG",
    t2."TCHSDDYNADJCHK",
    t2."TI_WAIT_SGSN_PRIVATE_MESSAGE",
    t2."TRBSS",
    t2."WAITCHNADJ"
FROM
huawei_gexport_gsm."BSCTMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISFCTIMER1",
    t3."ABISFCTIMER2",
    t3."AT1",
    t3."AT19",
    t3."AT20",
    t3."BMTCFCTIMERLEN",
    t3."CBNONMSGTIMER",
    t3."CBSHAKEHANDTIMER",
    t3."EXTCELLLOADINVALIDTIMER",
    t3."MSCCLRCMDTMR",
    t3."PROHIBTRPTCELLLOAD",
    t3."RELITFACONNTMR",
    t3."RESCHKSTARTTM",
    t3."RESCHKSTPTM",
    t3."RESINDPERIOD",
    t3."SDBACK2TCHJDG",
    t3."TCHSDDYNADJCHK",
    t3."TI_WAIT_SGSN_PRIVATE_MESSAGE",
    t3."TRBSS",
    t3."WAITCHNADJ"
FROM
huawei_gexport_gsm."BSCTMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISFCTIMER1",
    t4."ABISFCTIMER2",
    t4."AT1",
    t4."AT19",
    t4."AT20",
    t4."BMTCFCTIMERLEN",
    t4."CBNONMSGTIMER",
    t4."CBSHAKEHANDTIMER",
    t4."EXTCELLLOADINVALIDTIMER",
    t4."MSCCLRCMDTMR",
    t4."PROHIBTRPTCELLLOAD",
    t4."RELITFACONNTMR",
    t4."RESCHKSTARTTM",
    t4."RESCHKSTPTM",
    t4."RESINDPERIOD",
    t4."SDBACK2TCHJDG",
    t4."TCHSDDYNADJCHK",
    t4."TI_WAIT_SGSN_PRIVATE_MESSAGE",
    t4."TRBSS",
    t4."WAITCHNADJ"
FROM
huawei_mml_gsm."BSCTMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSSGPPARA = ReplaceableObject(
    'huawei_cm_2g."BSSGPPARA"',
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
    t1."BVCTF",
    t1."MSTF",
    t1."T1",
    t1."T2",
    t1."T3",
    t1."T4",
    t1."T5",
    t1."T6",
    t1."T8",
    t1."TC",
    t1."TH"
FROM
huawei_nbi_gsm."BSSGPPARA" t1

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
    t2."BVCTF",
    t2."MSTF",
    t2."T1",
    t2."T2",
    t2."T3",
    t2."T4",
    t2."T5",
    t2."T6",
    t2."T8",
    t2."TC",
    t2."TH"
FROM
huawei_gexport_gsm."BSSGPPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BVCTF",
    t3."MSTF",
    t3."T1",
    t3."T2",
    t3."T3",
    t3."T4",
    t3."T5",
    t3."T6",
    t3."T8",
    t3."TC",
    t3."TH"
FROM
huawei_gexport_gsm."BSSGPPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BVCTF",
    t4."MSTF",
    t4."T1",
    t4."T2",
    t4."T3",
    t4."T4",
    t4."T5",
    t4."T6",
    t4."T8",
    t4."TC",
    t4."TH"
FROM
huawei_mml_gsm."BSSGPPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BSSLS = ReplaceableObject(
    'huawei_cm_2g."BSSLS"',
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
    t1."BSSLSGENMODE",
    t1."MSISDNSEGLIST2AVOIDBSCLS1",
    t1."MSISDNSEGLIST2AVOIDBSCLS10",
    t1."MSISDNSEGLIST2AVOIDBSCLS2",
    t1."MSISDNSEGLIST2AVOIDBSCLS3",
    t1."MSISDNSEGLIST2AVOIDBSCLS4",
    t1."MSISDNSEGLIST2AVOIDBSCLS5",
    t1."MSISDNSEGLIST2AVOIDBSCLS6",
    t1."MSISDNSEGLIST2AVOIDBSCLS7",
    t1."MSISDNSEGLIST2AVOIDBSCLS8",
    t1."MSISDNSEGLIST2AVOIDBSCLS9",
    t1."MSISDNSEGLIST2AVOIDBTSLS1",
    t1."MSISDNSEGLIST2AVOIDBTSLS10",
    t1."MSISDNSEGLIST2AVOIDBTSLS2",
    t1."MSISDNSEGLIST2AVOIDBTSLS3",
    t1."MSISDNSEGLIST2AVOIDBTSLS4",
    t1."MSISDNSEGLIST2AVOIDBTSLS5",
    t1."MSISDNSEGLIST2AVOIDBTSLS6",
    t1."MSISDNSEGLIST2AVOIDBTSLS7",
    t1."MSISDNSEGLIST2AVOIDBTSLS8",
    t1."MSISDNSEGLIST2AVOIDBTSLS9"
FROM
huawei_nbi_gsm."BSSLS" t1

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
    t2."BSSLSGENMODE",
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
    NULL
FROM
huawei_gexport_gsm."BSSLS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BSSLSGENMODE",
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
    NULL
FROM
huawei_gexport_gsm."BSSLS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BSSLSGENMODE",
    t4."MSISDNSEGLIST2AVOIDBSCLS1",
    t4."MSISDNSEGLIST2AVOIDBSCLS10",
    t4."MSISDNSEGLIST2AVOIDBSCLS2",
    t4."MSISDNSEGLIST2AVOIDBSCLS3",
    t4."MSISDNSEGLIST2AVOIDBSCLS4",
    t4."MSISDNSEGLIST2AVOIDBSCLS5",
    t4."MSISDNSEGLIST2AVOIDBSCLS6",
    t4."MSISDNSEGLIST2AVOIDBSCLS7",
    t4."MSISDNSEGLIST2AVOIDBSCLS8",
    t4."MSISDNSEGLIST2AVOIDBSCLS9",
    t4."MSISDNSEGLIST2AVOIDBTSLS1",
    t4."MSISDNSEGLIST2AVOIDBTSLS10",
    t4."MSISDNSEGLIST2AVOIDBTSLS2",
    t4."MSISDNSEGLIST2AVOIDBTSLS3",
    t4."MSISDNSEGLIST2AVOIDBTSLS4",
    t4."MSISDNSEGLIST2AVOIDBTSLS5",
    t4."MSISDNSEGLIST2AVOIDBTSLS6",
    t4."MSISDNSEGLIST2AVOIDBTSLS7",
    t4."MSISDNSEGLIST2AVOIDBTSLS8",
    t4."MSISDNSEGLIST2AVOIDBTSLS9"
FROM
huawei_mml_gsm."BSSLS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTS = ReplaceableObject(
    'huawei_cm_2g."BTS"',
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
    t1."ABISBYPASSMODE",
    t1."ACTSTATUS",
    t1."BTSDESC",
    t1."BTSID",
    t1."BTSNAME",
    t1."BTSTYPE",
    t1."FLEXABISMODE",
    t1."HOSTTYPE",
    t1."INNBBULICSHAEN",
    t1."INTRABBPOOLSWITCH",
    t1."IPPHYTRANSTYPE",
    t1."ISCONFIGEDRING",
    t1."MAINBMPMODE",
    t1."MAINPORTNO",
    t1."MPMODE",
    t1."SEPERATEMODE",
    t1."SERVICEMODE",
    t1."SRANMODE",
    t1."WORKMODE",
    t1."TRANDETSWITCH",
    t1."TSASSIGNOPTISW"
FROM
huawei_nbi_gsm."BTS" t1

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
    t2."ABISBYPASSMODE",
    t2."ACTSTATUS",
    t2."BTSDESC",
    t2."BTSID",
    t2."BTSNAME",
    t2."BTSTYPE",
    t2."FLEXABISMODE",
    t2."HOSTTYPE",
    t2."INNBBULICSHAEN",
    t2."INTRABBPOOLSWITCH",
    NULL,
    t2."ISCONFIGEDRING",
    t2."MAINBMPMODE",
    t2."MAINPORTNO",
    t2."MPMODE",
    t2."SEPERATEMODE",
    t2."SERVICEMODE",
    NULL,
    t2."WORKMODE",
    t2."TRANDETSWITCH",
    t2."TSASSIGNOPTISW"
FROM
huawei_gexport_gsm."BTS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISBYPASSMODE",
    t3."ACTSTATUS",
    t3."BTSDESC",
    t3."BTSID",
    t3."BTSNAME",
    t3."BTSTYPE",
    t3."FLEXABISMODE",
    t3."HOSTTYPE",
    t3."INNBBULICSHAEN",
    t3."INTRABBPOOLSWITCH",
    NULL,
    t3."ISCONFIGEDRING",
    t3."MAINBMPMODE",
    t3."MAINPORTNO",
    t3."MPMODE",
    t3."SEPERATEMODE",
    t3."SERVICEMODE",
    NULL,
    t3."WORKMODE",
    t3."TRANDETSWITCH",
    t3."TSASSIGNOPTISW"
FROM
huawei_gexport_gsm."BTS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISBYPASSMODE",
    NULL,
    t4."BTSDESC",
    t4."BTSID",
    t4."BTSNAME",
    t4."BTSTYPE",
    t4."FLEXABISMODE",
    t4."HOSTTYPE",
    t4."INNBBULICSHAEN",
    t4."INTRABBPOOLSWITCH",
    NULL,
    t4."ISCONFIGEDRING",
    t4."MAINBMPMODE",
    t4."MAINPORTNO",
    t4."MPMODE",
    t4."SEPERATEMODE",
    t4."SERVICEMODE",
    t4."SRANMODE",
    t4."WORKMODE",
    t4."TRANDETSWITCH",
    t4."TSASSIGNOPTISW"
FROM
huawei_mml_gsm."BTS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."BTSID",
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
    NULL
FROM
huawei_mml_gsm."BTS_ACT" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

BTSABISMUXFLOW = ReplaceableObject(
    'huawei_cm_2g."BTSABISMUXFLOW"',
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
    t1."BTSID",
    t1."PKTLENTHRES",
    t1."SRVTYPE",
    t1."SUBFRAMETHRES",
    t1."TIMEOUT"
FROM
huawei_nbi_gsm."BTSABISMUXFLOW" t1

"""
)

BTSABISPRIMAP = ReplaceableObject(
    'huawei_cm_2g."BTSABISPRIMAP"',
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
    t1."BTSID",
    t1."EMLDSCP",
    t1."ESLDSCP",
    t1."OMLDSCP",
    t1."RSLDSCP",
    t1."TRANSTYPE",
    t1."VLANFLAG"
FROM
huawei_nbi_gsm."BTSABISPRIMAP" t1

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
    t2."BTSID",
    NULL,
    NULL,
    NULL,
    NULL,
    t2."TRANSTYPE",
    NULL
FROM
huawei_gexport_gsm."BTSABISPRIMAP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    NULL,
    NULL,
    NULL,
    NULL,
    t3."TRANSTYPE",
    NULL
FROM
huawei_gexport_gsm."BTSABISPRIMAP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

BTSABISTROP = ReplaceableObject(
    'huawei_cm_2g."BTSABISTROP"',
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
    t1."BTSID",
    t1."DETECTSWITCH",
    t1."PROTECTDELAYTIME"
FROM
huawei_nbi_gsm."BTSABISTROP" t1

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
    t2."BTSID",
    t2."DETECTSWITCH",
    NULL
FROM
huawei_gexport_gsm."BTSABISTROP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."DETECTSWITCH",
    NULL
FROM
huawei_gexport_gsm."BTSABISTROP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."DETECTSWITCH",
    NULL
FROM
huawei_mml_gsm."BTSABISTROP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSAISS = ReplaceableObject(
    'huawei_cm_2g."BTSAISS"',
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
    t1."BTSID",
    t1."SITESYNCZONE",
    t1."SYMOFFSET"
FROM
huawei_nbi_gsm."BTSAISS" t1

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
    t2."BTSID",
    t2."SITESYNCZONE",
    t2."SYMOFFSET"
FROM
huawei_gexport_gsm."BTSAISS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."SITESYNCZONE",
    t3."SYMOFFSET"
FROM
huawei_gexport_gsm."BTSAISS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."SITESYNCZONE",
    t4."SYMOFFSET"
FROM
huawei_mml_gsm."BTSAISS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSALM = ReplaceableObject(
    'huawei_cm_2g."BTSALM"',
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
    t1."BTSID",
    t1."BTSTYPE",
    t1."EXTFLAG"
FROM
huawei_nbi_gsm."BTSALM" t1

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
    t2."BTSID",
    t2."BTSTYPE",
    t2."EXTFLAG"
FROM
huawei_gexport_gsm."BTSALM_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."BTSTYPE",
    t3."EXTFLAG"
FROM
huawei_gexport_gsm."BTSALM_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."BTSTYPE",
    t4."EXTFLAG"
FROM
huawei_mml_gsm."BTSALM" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSALMFLASHTHD = ReplaceableObject(
    'huawei_cm_2g."BTSALMFLASHTHD"',
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
    t1."ALMID",
    t1."ALMOCCURACCUTIMEHTHD",
    t1."ALMOCCURACCUTIMELTHD",
    t1."ALMOCCURTIMESHTHD",
    t1."ALMOCCURTIMESLTHD",
    t1."FLASHALMCLRTHD",
    t1."FLASHALMOCCURTHD"
FROM
huawei_nbi_gsm."BTSALMFLASHTHD" t1

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
    t2."ALMID",
    t2."ALMOCCURACCUTIMEHTHD",
    t2."ALMOCCURACCUTIMELTHD",
    t2."ALMOCCURTIMESHTHD",
    t2."ALMOCCURTIMESLTHD",
    t2."FLASHALMCLRTHD",
    t2."FLASHALMOCCURTHD"
FROM
huawei_gexport_gsm."BTSALMFLASHTHD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALMID",
    t3."ALMOCCURACCUTIMEHTHD",
    t3."ALMOCCURACCUTIMELTHD",
    t3."ALMOCCURTIMESHTHD",
    t3."ALMOCCURTIMESLTHD",
    t3."FLASHALMCLRTHD",
    t3."FLASHALMOCCURTHD"
FROM
huawei_gexport_gsm."BTSALMFLASHTHD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALMID",
    t4."ALMOCCURACCUTIMEHTHD",
    t4."ALMOCCURACCUTIMELTHD",
    t4."ALMOCCURTIMESHTHD",
    t4."ALMOCCURTIMESLTHD",
    t4."FLASHALMCLRTHD",
    t4."FLASHALMOCCURTHD"
FROM
huawei_mml_gsm."BTSALMFLASHTHD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSALMFLASHTW = ReplaceableObject(
    'huawei_cm_2g."BTSALMFLASHTW"',
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
    t1."FLASHSTATISALMCLRTW",
    t1."FLASHSTATISALMOCCURTW"
FROM
huawei_nbi_gsm."BTSALMFLASHTW" t1

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
    t2."FLASHSTATISALMCLRTW",
    t2."FLASHSTATISALMOCCURTW"
FROM
huawei_gexport_gsm."BTSALMFLASHTW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FLASHSTATISALMCLRTW",
    t3."FLASHSTATISALMOCCURTW"
FROM
huawei_gexport_gsm."BTSALMFLASHTW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FLASHSTATISALMCLRTW",
    t4."FLASHSTATISALMOCCURTW"
FROM
huawei_mml_gsm."BTSALMFLASHTW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSALMPORT = ReplaceableObject(
    'huawei_cm_2g."BTSALMPORT"',
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
    t1."BTSID",
    t1."SWITCH"
FROM
huawei_nbi_gsm."BTSALMPORT" t1

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
    t2."BTSID",
    t2."SWITCH"
FROM
huawei_gexport_gsm."BTSALMPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."SWITCH"
FROM
huawei_gexport_gsm."BTSALMPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."SWITCH"
FROM
huawei_mml_gsm."BTSALMPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSAPMUBP = ReplaceableObject(
    'huawei_cm_2g."BTSAPMUBP"',
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
    t1."ADDR",
    t1."ALMENABLE",
    t1."ASSORXUCN",
    t1."ASSORXUSN",
    t1."ASSORXUSRN",
    t1."BASETEMPERATURE",
    t1."BC",
    t1."BCD",
    t1."BCLC",
    t1."BE",
    t1."BTPC",
    t1."BTSID",
    t1."BTSSHUTDNASW",
    t1."BTYPE",
    t1."CELLTEMP1THRESHOLDH",
    t1."CELLTEMP1THRESHOLDL",
    t1."CELLTEMPCOMPENABLED",
    t1."CFGFLAG",
    t1."CN",
    t1."HIGHTEMPLOADPWROFF",
    t1."HPVFLAG",
    t1."HTSDF",
    t1."HUMALAMRTHRESHOLDH",
    t1."HUMALAMRTHRESHOLDL",
    t1."MCN",
    t1."MPN",
    t1."MSRN",
    t1."PTYPE",
    t1."SAAF",
    t1."SBAF",
    t1."SDT",
    t1."SETDIESELENGINEENABLED",
    t1."SETENVPARAENABLED",
    t1."SETHUMPARAENABLED",
    t1."SN",
    t1."SRN",
    t1."TCC",
    t1."TEMPOFHIGHTEMPLOADPWROFF",
    t1."TLTHD",
    t1."TUTHD",
    t1."ACVLTHD",
    t1."ACVUTHD",
    t1."BCV",
    t1."DCVLTHD",
    t1."DCVUTHD",
    t1."FCV",
    t1."LOWTEMPLOADPWROFF",
    t1."LSDF",
    t1."LSDV",
    t1."LVSDF",
    t1."SDV",
    t1."TEMPOFLOWTEMPLOADPWROFF"
FROM
huawei_nbi_gsm."BTSAPMUBP" t1

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
    t2."ADDR",
    t2."ALMENABLE",
    t2."ASSORXUCN",
    t2."ASSORXUSN",
    t2."ASSORXUSRN",
    t2."BASETEMPERATURE",
    t2."BC",
    t2."BCD",
    t2."BCLC",
    t2."BE",
    t2."BTPC",
    t2."BTSID",
    t2."BTSSHUTDNASW",
    t2."BTYPE",
    t2."CELLTEMP1THRESHOLDH",
    t2."CELLTEMP1THRESHOLDL",
    t2."CELLTEMPCOMPENABLED",
    t2."CFGFLAG",
    t2."CN",
    t2."HIGHTEMPLOADPWROFF",
    t2."HPVFLAG",
    t2."HTSDF",
    NULL,
    NULL,
    t2."MCN",
    t2."MPN",
    t2."MSRN",
    t2."PTYPE",
    NULL,
    NULL,
    t2."SDT",
    t2."SETDIESELENGINEENABLED",
    t2."SETENVPARAENABLED",
    t2."SETHUMPARAENABLED",
    t2."SN",
    t2."SRN",
    t2."TCC",
    t2."TEMPOFHIGHTEMPLOADPWROFF",
    t2."TLTHD",
    t2."TUTHD",
    t2."ACVLTHD",
    t2."ACVUTHD",
    t2."BCV",
    t2."DCVLTHD",
    t2."DCVUTHD",
    t2."FCV",
    t2."LOWTEMPLOADPWROFF",
    t2."LSDF",
    t2."LSDV",
    t2."LVSDF",
    t2."SDV",
    t2."TEMPOFLOWTEMPLOADPWROFF"
FROM
huawei_gexport_gsm."BTSAPMUBP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADDR",
    t3."ALMENABLE",
    t3."ASSORXUCN",
    t3."ASSORXUSN",
    t3."ASSORXUSRN",
    t3."BASETEMPERATURE",
    t3."BC",
    t3."BCD",
    t3."BCLC",
    t3."BE",
    t3."BTPC",
    t3."BTSID",
    t3."BTSSHUTDNASW",
    t3."BTYPE",
    t3."CELLTEMP1THRESHOLDH",
    t3."CELLTEMP1THRESHOLDL",
    t3."CELLTEMPCOMPENABLED",
    t3."CFGFLAG",
    t3."CN",
    t3."HIGHTEMPLOADPWROFF",
    t3."HPVFLAG",
    t3."HTSDF",
    NULL,
    NULL,
    t3."MCN",
    t3."MPN",
    t3."MSRN",
    t3."PTYPE",
    NULL,
    NULL,
    t3."SDT",
    t3."SETDIESELENGINEENABLED",
    t3."SETENVPARAENABLED",
    t3."SETHUMPARAENABLED",
    t3."SN",
    t3."SRN",
    t3."TCC",
    t3."TEMPOFHIGHTEMPLOADPWROFF",
    t3."TLTHD",
    t3."TUTHD",
    t3."ACVLTHD",
    t3."ACVUTHD",
    t3."BCV",
    t3."DCVLTHD",
    t3."DCVUTHD",
    t3."FCV",
    t3."LOWTEMPLOADPWROFF",
    t3."LSDF",
    t3."LSDV",
    t3."LVSDF",
    t3."SDV",
    t3."TEMPOFLOWTEMPLOADPWROFF"
FROM
huawei_gexport_gsm."BTSAPMUBP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADDR",
    t4."ALMENABLE",
    t4."ASSORXUCN",
    t4."ASSORXUSN",
    t4."ASSORXUSRN",
    t4."BASETEMPERATURE",
    t4."BC",
    t4."BCD",
    t4."BCLC",
    t4."BE",
    t4."BTPC",
    t4."BTSID",
    t4."BTSSHUTDNASW",
    t4."BTYPE",
    t4."CELLTEMP1THRESHOLDH",
    t4."CELLTEMP1THRESHOLDL",
    t4."CELLTEMPCOMPENABLED",
    t4."CFGFLAG",
    t4."CN",
    t4."HIGHTEMPLOADPWROFF",
    t4."HPVFLAG",
    t4."HTSDF",
    t4."HUMALAMRTHRESHOLDH",
    t4."HUMALAMRTHRESHOLDL",
    t4."MCN",
    t4."MPN",
    t4."MSRN",
    t4."PTYPE",
    NULL,
    NULL,
    t4."SDT",
    t4."SETDIESELENGINEENABLED",
    t4."SETENVPARAENABLED",
    t4."SETHUMPARAENABLED",
    t4."SN",
    t4."SRN",
    t4."TCC",
    t4."TEMPOFHIGHTEMPLOADPWROFF",
    t4."TLTHD",
    t4."TUTHD",
    t4."ACVLTHD",
    t4."ACVUTHD",
    t4."BCV",
    t4."DCVLTHD",
    t4."DCVUTHD",
    t4."FCV",
    t4."LOWTEMPLOADPWROFF",
    t4."LSDF",
    t4."LSDV",
    t4."LVSDF",
    t4."SDV",
    t4."TEMPOFLOWTEMPLOADPWROFF"
FROM
huawei_mml_gsm."BTSAPMUBP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSAPPCERT = ReplaceableObject(
    'huawei_cm_2g."BTSAPPCERT"',
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
    t1."APPCERT",
    t1."APPTYPE",
    t1."BTSID"
FROM
huawei_nbi_gsm."BTSAPPCERT" t1

"""
)

BTSAUTODLDACTINFO = ReplaceableObject(
    'huawei_cm_2g."BTSAUTODLDACTINFO"',
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
    t1."ADLDACT",
    t1."ADMODE",
    t1."ADVER1",
    t1."ADVER2",
    t1."AUTOTYPE",
    t1."BTSID",
    t1."CVER",
    t1."PATCHNO1",
    t1."PV",
    t1."RVER",
    t1."STTYPE",
    t1."VVER"
FROM
huawei_nbi_gsm."BTSAUTODLDACTINFO" t1

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
    t2."ADLDACT",
    t2."ADMODE",
    t2."ADVER1",
    t2."ADVER2",
    t2."AUTOTYPE",
    t2."BTSID",
    t2."CVER",
    t2."PATCHNO1",
    t2."PV",
    t2."RVER",
    t2."STTYPE",
    t2."VVER"
FROM
huawei_gexport_gsm."BTSAUTODLDACTINFO_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADLDACT",
    t3."ADMODE",
    t3."ADVER1",
    t3."ADVER2",
    t3."AUTOTYPE",
    t3."BTSID",
    t3."CVER",
    t3."PATCHNO1",
    t3."PV",
    t3."RVER",
    t3."STTYPE",
    t3."VVER"
FROM
huawei_gexport_gsm."BTSAUTODLDACTINFO_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADLDACT",
    t4."ADMODE",
    t4."ADVER1",
    t4."ADVER2",
    t4."AUTOTYPE",
    t4."BTSID",
    t4."CVER",
    t4."PATCHNO1",
    t4."PV",
    t4."RVER",
    t4."STTYPE",
    t4."VVER"
FROM
huawei_mml_gsm."BTSAUTODLDACTINFO" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSBAKPWR = ReplaceableObject(
    'huawei_cm_2g."BTSBAKPWR"',
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
    t1."BAKPWRSAVMETHOD",
    t1."BTSID"
FROM
huawei_nbi_gsm."BTSBAKPWR" t1

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
    t2."BAKPWRSAVMETHOD",
    t2."BTSID"
FROM
huawei_gexport_gsm."BTSBAKPWR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BAKPWRSAVMETHOD",
    t3."BTSID"
FROM
huawei_gexport_gsm."BTSBAKPWR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BAKPWRSAVMETHOD",
    t4."BTSID"
FROM
huawei_mml_gsm."BTSBAKPWR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSBBMODE = ReplaceableObject(
    'huawei_cm_2g."BTSBBMODE"',
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
    t1."BBMODE",
    t1."BTSID"
FROM
huawei_nbi_gsm."BTSBBMODE" t1

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
    t2."BBMODE",
    t2."BTSID"
FROM
huawei_gexport_gsm."BTSBBMODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BBMODE",
    t3."BTSID"
FROM
huawei_gexport_gsm."BTSBBMODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BBMODE",
    t4."BTSID"
FROM
huawei_mml_gsm."BTSBBMODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSBINDLOCGRP = ReplaceableObject(
    'huawei_cm_2g."BTSBINDLOCGRP"',
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
    t1."ANTPASSNO",
    t1."BTSID",
    t1."CN",
    t1."MAINLOCGRPNO",
    t1."SLAVELOCGRPNO",
    t1."SN",
    t1."SRN",
    t1."TRXID",
    t1."TRXPN"
FROM
huawei_nbi_gsm."BTSBINDLOCGRP" t1

"""
)

BTSBRD = ReplaceableObject(
    'huawei_cm_2g."BTSBRD"',
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
    t1."BTSID",
    t1."CN",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSBRD" t1

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
    t2."BTSID",
    t2."CN",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."BTSBRD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CN",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."BTSBRD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    NULL
FROM
huawei_mml_gsm."BTSBRD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSBREAKPOINT = ReplaceableObject(
    'huawei_cm_2g."BTSBREAKPOINT"',
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
    t1."BP1",
    t1."BP2",
    t1."BTSID",
    t1."RCN"
FROM
huawei_nbi_gsm."BTSBREAKPOINT" t1

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
    t2."BP1",
    t2."BP2",
    t2."BTSID",
    t2."RCN"
FROM
huawei_gexport_gsm."BTSBREAKPOINT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BP1",
    t3."BP2",
    t3."BTSID",
    t3."RCN"
FROM
huawei_gexport_gsm."BTSBREAKPOINT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BP1",
    t4."BP2",
    t4."BTSID",
    t4."RCN"
FROM
huawei_mml_gsm."BTSBREAKPOINT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSBWPARA = ReplaceableObject(
    'huawei_cm_2g."BTSBWPARA"',
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
    t1."BTSID",
    t1."COMPRS",
    t1."OMLESLDL",
    t1."OMLESLUL",
    t1."RSLDL",
    t1."RSLUL",
    t1."TRANSTYPE"
FROM
huawei_nbi_gsm."BTSBWPARA" t1

"""
)

BTSCABINET = ReplaceableObject(
    'huawei_cm_2g."BTSCABINET"',
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
    t1."BBUSUBRACKTYPE",
    t1."BTSID",
    t1."CABINETDESC",
    t1."CN",
    t1."ISMAINCABINET",
    t1."SRANMODE",
    t1."TYPE"
FROM
huawei_nbi_gsm."BTSCABINET" t1

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
    t2."BBUSUBRACKTYPE",
    t2."BTSID",
    t2."CABINETDESC",
    t2."CN",
    NULL,
    t2."SRANMODE",
    t2."TYPE"
FROM
huawei_gexport_gsm."BTSCABINET_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BBUSUBRACKTYPE",
    t3."BTSID",
    t3."CABINETDESC",
    t3."CN",
    NULL,
    t3."SRANMODE",
    t3."TYPE"
FROM
huawei_gexport_gsm."BTSCABINET_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BBUSUBRACKTYPE",
    t4."BTSID",
    t4."CABINETDESC",
    t4."CN",
    t4."ISMAINCABINET",
    t4."SRANMODE",
    t4."TYPE"
FROM
huawei_mml_gsm."BTSCABINET" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCELLPATCHPARA = ReplaceableObject(
    'huawei_cm_2g."BTSCELLPATCHPARA"',
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
    t1."BTSID",
    t1."CELLID",
    t1."RSVDPARA1",
    t1."RSVDPARA10",
    t1."RSVDPARA11",
    t1."RSVDPARA12",
    t1."RSVDPARA13",
    t1."RSVDPARA14",
    t1."RSVDPARA15",
    t1."RSVDPARA16",
    t1."RSVDPARA17",
    t1."RSVDPARA18",
    t1."RSVDPARA19",
    t1."RSVDPARA2",
    t1."RSVDPARA20",
    t1."RSVDPARA21",
    t1."RSVDPARA22",
    t1."RSVDPARA23",
    t1."RSVDPARA24",
    t1."RSVDPARA25",
    t1."RSVDPARA3",
    t1."RSVDPARA4",
    t1."RSVDPARA5",
    t1."RSVDPARA6",
    t1."RSVDPARA7",
    t1."RSVDPARA8",
    t1."RSVDPARA9"
FROM
huawei_nbi_gsm."BTSCELLPATCHPARA" t1

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
    t2."BTSID",
    t2."CELLID",
    t2."RSVDPARA1",
    t2."RSVDPARA10",
    t2."RSVDPARA11",
    t2."RSVDPARA12",
    t2."RSVDPARA13",
    t2."RSVDPARA14",
    t2."RSVDPARA15",
    t2."RSVDPARA16",
    t2."RSVDPARA17",
    t2."RSVDPARA18",
    t2."RSVDPARA19",
    t2."RSVDPARA2",
    t2."RSVDPARA20",
    t2."RSVDPARA21",
    t2."RSVDPARA22",
    t2."RSVDPARA23",
    t2."RSVDPARA24",
    t2."RSVDPARA25",
    t2."RSVDPARA3",
    t2."RSVDPARA4",
    t2."RSVDPARA5",
    t2."RSVDPARA6",
    t2."RSVDPARA7",
    t2."RSVDPARA8",
    t2."RSVDPARA9"
FROM
huawei_gexport_gsm."BTSCELLPATCHPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CELLID",
    t3."RSVDPARA1",
    t3."RSVDPARA10",
    t3."RSVDPARA11",
    t3."RSVDPARA12",
    t3."RSVDPARA13",
    t3."RSVDPARA14",
    t3."RSVDPARA15",
    t3."RSVDPARA16",
    t3."RSVDPARA17",
    t3."RSVDPARA18",
    t3."RSVDPARA19",
    t3."RSVDPARA2",
    t3."RSVDPARA20",
    t3."RSVDPARA21",
    t3."RSVDPARA22",
    t3."RSVDPARA23",
    t3."RSVDPARA24",
    t3."RSVDPARA25",
    t3."RSVDPARA3",
    t3."RSVDPARA4",
    t3."RSVDPARA5",
    t3."RSVDPARA6",
    t3."RSVDPARA7",
    t3."RSVDPARA8",
    t3."RSVDPARA9"
FROM
huawei_gexport_gsm."BTSCELLPATCHPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CELLID",
    t4."RSVDPARA1",
    t4."RSVDPARA10",
    t4."RSVDPARA11",
    t4."RSVDPARA12",
    t4."RSVDPARA13",
    t4."RSVDPARA14",
    t4."RSVDPARA15",
    t4."RSVDPARA16",
    t4."RSVDPARA17",
    t4."RSVDPARA18",
    t4."RSVDPARA19",
    t4."RSVDPARA2",
    t4."RSVDPARA20",
    t4."RSVDPARA21",
    t4."RSVDPARA22",
    t4."RSVDPARA23",
    t4."RSVDPARA24",
    t4."RSVDPARA25",
    t4."RSVDPARA3",
    t4."RSVDPARA4",
    t4."RSVDPARA5",
    t4."RSVDPARA6",
    t4."RSVDPARA7",
    t4."RSVDPARA8",
    t4."RSVDPARA9"
FROM
huawei_mml_gsm."BTSCELLPATCHPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCERTCHKTSK = ReplaceableObject(
    'huawei_cm_2g."BTSCERTCHKTSK"',
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
    t1."ALMRNG",
    t1."BTSID",
    t1."ISENABLE",
    t1."PERIOD",
    t1."UPDATEMETHOD"
FROM
huawei_nbi_gsm."BTSCERTCHKTSK" t1

"""
)

BTSCERTDEPLOY = ReplaceableObject(
    'huawei_cm_2g."BTSCERTDEPLOY"',
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
    t1."BTSID",
    t1."DEPLOYTYPE"
FROM
huawei_nbi_gsm."BTSCERTDEPLOY" t1

"""
)

BTSCERTMK = ReplaceableObject(
    'huawei_cm_2g."BTSCERTMK"',
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
    t1."APPCERT",
    t1."BTSID"
FROM
huawei_nbi_gsm."BTSCERTMK" t1

"""
)

BTSCERTREQ = ReplaceableObject(
    'huawei_cm_2g."BTSCERTREQ"',
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
    t1."BTSID",
    t1."COMMNAME",
    t1."KEYSIZE",
    t1."KEYUSAGE",
    t1."LOCALIP",
    t1."SIGNALG"
FROM
huawei_nbi_gsm."BTSCERTREQ" t1

"""
)

BTSCHNFALLBACK = ReplaceableObject(
    'huawei_cm_2g."BTSCHNFALLBACK"',
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
    t1."BTSID",
    t1."CHNNO",
    t1."CHNTYPE",
    t1."GROUPCALLNUM1",
    t1."SPEECHVERMODE1",
    t1."SPEECHVERSION"
FROM
huawei_nbi_gsm."BTSCHNFALLBACK" t1

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
    t2."BTSID",
    t2."CHNNO",
    t2."CHNTYPE",
    t2."GROUPCALLNUM1",
    t2."SPEECHVERMODE1",
    t2."SPEECHVERSION"
FROM
huawei_gexport_gsm."BTSCHNFALLBACK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CHNNO",
    t3."CHNTYPE",
    t3."GROUPCALLNUM1",
    t3."SPEECHVERMODE1",
    t3."SPEECHVERSION"
FROM
huawei_gexport_gsm."BTSCHNFALLBACK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CHNNO",
    t4."CHNTYPE",
    t4."GROUPCALLNUM1",
    t4."SPEECHVERMODE1",
    t4."SPEECHVERSION"
FROM
huawei_mml_gsm."BTSCHNFALLBACK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCLK = ReplaceableObject(
    'huawei_cm_2g."BTSCLK"',
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
    t1."BTSID",
    t1."CLKTYPE",
    t1."CN",
    t1."FRAMEBITOFFSET",
    t1."FRAMESYNCSW",
    t1."PN",
    t1."SN",
    t1."SRN",
    t1."SSMSWICH",
    t1."TRANSTYPE",
    t1."TRCCLKRNGLMTSW",
    t1."TRCCLKRNGLMTTHD",
    t1."CLKSYNCMODE",
    t1."STANDARD"
FROM
huawei_nbi_gsm."BTSCLK" t1

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
    t2."BTSID",
    t2."CLKTYPE",
    NULL,
    t2."FRAMEBITOFFSET",
    t2."FRAMESYNCSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."TRCCLKRNGLMTSW",
    t2."TRCCLKRNGLMTTHD",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSCLK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CLKTYPE",
    NULL,
    t3."FRAMEBITOFFSET",
    t3."FRAMESYNCSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."TRCCLKRNGLMTSW",
    t3."TRCCLKRNGLMTTHD",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSCLK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CLKTYPE",
    NULL,
    t4."FRAMEBITOFFSET",
    t4."FRAMESYNCSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t4."TRCCLKRNGLMTSW",
    t4."TRCCLKRNGLMTTHD",
    NULL,
    NULL
FROM
huawei_mml_gsm."BTSCLK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCONNECT = ReplaceableObject(
    'huawei_cm_2g."BTSCONNECT"',
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
    t1."BTSID",
    t1."DESTNODE",
    t1."DXXINDEX",
    t1."DXXPN",
    t1."INCN",
    t1."INPN",
    t1."INSN",
    t1."INSRN",
    t1."OPNAME",
    t1."FCN",
    t1."FPN",
    t1."FSN",
    t1."FSRN",
    t1."UPBTSID",
    t1."PN",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSCONNECT" t1

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
    t2."BTSID",
    t2."DESTNODE",
    NULL,
    NULL,
    t2."INCN",
    t2."INPN",
    t2."INSN",
    t2."INSRN",
    t2."OPNAME",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."PN",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."BTSCONNECT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."DESTNODE",
    NULL,
    NULL,
    t3."INCN",
    t3."INPN",
    t3."INSN",
    t3."INSRN",
    t3."OPNAME",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."PN",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."BTSCONNECT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."DESTNODE",
    NULL,
    NULL,
    t4."INCN",
    t4."INPN",
    t4."INSN",
    t4."INSRN",
    t4."OPNAME",
    NULL,
    t4."FPN",
    NULL,
    NULL,
    t4."UPBTSID",
    t4."PN",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."BTSCONNECT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCPRIPORT = ReplaceableObject(
    'huawei_cm_2g."BTSCPRIPORT"',
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
    t1."ADMSTAT",
    t1."BTSID",
    t1."CN",
    t1."OPTN",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSCPRIPORT" t1

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
    t2."ADMSTAT",
    t2."BTSID",
    t2."CN",
    t2."OPTN",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."BTSCPRIPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADMSTAT",
    t3."BTSID",
    t3."CN",
    t3."OPTN",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."BTSCPRIPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADMSTAT",
    t4."BTSID",
    t4."CN",
    t4."OPTN",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."BTSCPRIPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCRC4 = ReplaceableObject(
    'huawei_cm_2g."BTSCRC4"',
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
    t1."BTSID",
    t1."CRC4CHK"
FROM
huawei_nbi_gsm."BTSCRC4" t1

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
    t2."BTSID",
    t2."CRC4CHK"
FROM
huawei_gexport_gsm."BTSCRC4_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CRC4CHK"
FROM
huawei_gexport_gsm."BTSCRC4_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CRC4CHK"
FROM
huawei_mml_gsm."BTSCRC4" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCRLPOLICY = ReplaceableObject(
    'huawei_cm_2g."BTSCRLPOLICY"',
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
    t1."BTSID",
    t1."CRLPOLICY"
FROM
huawei_nbi_gsm."BTSCRLPOLICY" t1

"""
)

BTSCTRLEX = ReplaceableObject(
    'huawei_cm_2g."BTSCTRLEX"',
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
    t1."BTSID",
    t1."CPUNO",
    t1."CTRLSN",
    t1."CTRLSRN"
FROM
huawei_nbi_gsm."BTSCTRLEX" t1

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
    t2."BTSID",
    t2."CPUNO",
    t2."CTRLSN",
    t2."CTRLSRN"
FROM
huawei_gexport_gsm."BTSCTRLEX_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CPUNO",
    t3."CTRLSN",
    t3."CTRLSRN"
FROM
huawei_gexport_gsm."BTSCTRLEX_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CPUNO",
    t4."CTRLSN",
    t4."CTRLSRN"
FROM
huawei_mml_gsm."BTSCTRLEX" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSCTRLLNK = ReplaceableObject(
    'huawei_cm_2g."BTSCTRLLNK"',
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
    t1."BTSID",
    t1."CN",
    t1."LN",
    t1."SN",
    t1."SRN",
    t1."UPCN",
    t1."UPPT",
    t1."UPSN",
    t1."UPSRN"
FROM
huawei_nbi_gsm."BTSCTRLLNK" t1

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
    t2."BTSID",
    t2."CN",
    t2."LN",
    t2."SN",
    t2."SRN",
    t2."UPCN",
    t2."UPPT",
    t2."UPSN",
    t2."UPSRN"
FROM
huawei_gexport_gsm."BTSCTRLLNK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CN",
    t3."LN",
    t3."SN",
    t3."SRN",
    t3."UPCN",
    t3."UPPT",
    t3."UPSN",
    t3."UPSRN"
FROM
huawei_gexport_gsm."BTSCTRLLNK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CN",
    t4."LN",
    t4."SN",
    t4."SRN",
    t4."UPCN",
    t4."UPPT",
    t4."UPSN",
    t4."UPSRN"
FROM
huawei_mml_gsm."BTSCTRLLNK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSDEVIP = ReplaceableObject(
    'huawei_cm_2g."BTSDEVIP"',
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
    t1."BTSID",
    t1."CN",
    t1."IP",
    t1."IPIDX",
    t1."ISINNERIP",
    t1."MASK",
    t1."PN",
    t1."PT",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSDEVIP" t1

"""
)

BTSDHCPSVRIP = ReplaceableObject(
    'huawei_cm_2g."BTSDHCPSVRIP"',
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
    t1."BTSID",
    t1."DHCPSRV"
FROM
huawei_nbi_gsm."BTSDHCPSVRIP" t1

"""
)

BTSDHEUBP = ReplaceableObject(
    'huawei_cm_2g."BTSDHEUBP"',
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
    t1."ADDR",
    t1."ALMPARACFGFLAG",
    t1."ASSORXUCN",
    t1."ASSORXUSN",
    t1."ASSORXUSRN",
    t1."BTSID",
    t1."CFGFLAG",
    t1."CN",
    t1."ISADDEDTMPCONTROL",
    t1."ISTMPCTRL",
    t1."MCN",
    t1."MPN",
    t1."MSRN",
    t1."SN",
    t1."SRN",
    t1."TCMODE",
    t1."TLTHD",
    t1."TUTHD",
    t1."DBD",
    t1."HTCP",
    t1."HTDO",
    t1."LTCP",
    t1."NTDI",
    t1."NTDO",
    t1."SBAF",
    t1."TLT",
    t1."ENDHEATTEMP",
    t1."STARTHEATTEMP"
FROM
huawei_nbi_gsm."BTSDHEUBP" t1

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
    t2."ADDR",
    t2."ALMPARACFGFLAG",
    t2."ASSORXUCN",
    t2."ASSORXUSN",
    t2."ASSORXUSRN",
    t2."BTSID",
    t2."CFGFLAG",
    t2."CN",
    t2."ISADDEDTMPCONTROL",
    t2."ISTMPCTRL",
    t2."MCN",
    t2."MPN",
    t2."MSRN",
    t2."SN",
    t2."SRN",
    t2."TCMODE",
    t2."TLTHD",
    t2."TUTHD",
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
huawei_gexport_gsm."BTSDHEUBP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADDR",
    t3."ALMPARACFGFLAG",
    t3."ASSORXUCN",
    t3."ASSORXUSN",
    t3."ASSORXUSRN",
    t3."BTSID",
    t3."CFGFLAG",
    t3."CN",
    t3."ISADDEDTMPCONTROL",
    t3."ISTMPCTRL",
    t3."MCN",
    t3."MPN",
    t3."MSRN",
    t3."SN",
    t3."SRN",
    t3."TCMODE",
    t3."TLTHD",
    t3."TUTHD",
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
huawei_gexport_gsm."BTSDHEUBP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADDR",
    t4."ALMPARACFGFLAG",
    t4."ASSORXUCN",
    t4."ASSORXUSN",
    t4."ASSORXUSRN",
    t4."BTSID",
    t4."CFGFLAG",
    t4."CN",
    t4."ISADDEDTMPCONTROL",
    t4."ISTMPCTRL",
    t4."MCN",
    t4."MPN",
    t4."MSRN",
    t4."SN",
    t4."SRN",
    t4."TCMODE",
    t4."TLTHD",
    t4."TUTHD",
    t4."DBD",
    t4."HTCP",
    t4."HTDO",
    t4."LTCP",
    t4."NTDI",
    t4."NTDO",
    NULL,
    t4."TLT",
    t4."ENDHEATTEMP",
    t4."STARTHEATTEMP"
FROM
huawei_mml_gsm."BTSDHEUBP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSDSCPMAP = ReplaceableObject(
    'huawei_cm_2g."BTSDSCPMAP"',
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
    t1."BTSID",
    t1."DSCP",
    t1."VLANPRI"
FROM
huawei_nbi_gsm."BTSDSCPMAP" t1

"""
)

BTSE1T1BER = ReplaceableObject(
    'huawei_cm_2g."BTSE1T1BER"',
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
    t1."BEROOSSWITCH",
    t1."BTL",
    t1."BTSID"
FROM
huawei_nbi_gsm."BTSE1T1BER" t1

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
    t2."BEROOSSWITCH",
    t2."BTL",
    t2."BTSID"
FROM
huawei_gexport_gsm."BTSE1T1BER_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BEROOSSWITCH",
    t3."BTL",
    t3."BTSID"
FROM
huawei_gexport_gsm."BTSE1T1BER_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BEROOSSWITCH",
    t4."BTL",
    t4."BTSID"
FROM
huawei_mml_gsm."BTSE1T1BER" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSEAMRC = ReplaceableObject(
    'huawei_cm_2g."BTSEAMRC"',
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
    t1."BTSID",
    t1."ENAMRCSWITCH",
    t1."LIMITRATETHR"
FROM
huawei_nbi_gsm."BTSEAMRC" t1

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
    t2."BTSID",
    t2."ENAMRCSWITCH",
    t2."LIMITRATETHR"
FROM
huawei_gexport_gsm."BTSEAMRC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."ENAMRCSWITCH",
    t3."LIMITRATETHR"
FROM
huawei_gexport_gsm."BTSEAMRC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."ENAMRCSWITCH",
    t4."LIMITRATETHR"
FROM
huawei_mml_gsm."BTSEAMRC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSENVALMPORT = ReplaceableObject(
    'huawei_cm_2g."BTSENVALMPORT"',
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
    t1."AID",
    t1."AVOL",
    t1."BTSID",
    t1."CN",
    t1."PN",
    t1."PT",
    t1."SN",
    t1."SRN",
    t1."SW"
FROM
huawei_nbi_gsm."BTSENVALMPORT" t1

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
    t2."AID",
    t2."AVOL",
    t2."BTSID",
    t2."CN",
    t2."PN",
    t2."PT",
    t2."SN",
    t2."SRN",
    t2."SW"
FROM
huawei_gexport_gsm."BTSENVALMPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    t3."AVOL",
    t3."BTSID",
    t3."CN",
    t3."PN",
    t3."PT",
    t3."SN",
    t3."SRN",
    t3."SW"
FROM
huawei_gexport_gsm."BTSENVALMPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AID",
    t4."AVOL",
    t4."BTSID",
    t4."CN",
    t4."PN",
    t4."PT",
    t4."SN",
    t4."SRN",
    t4."SW"
FROM
huawei_mml_gsm."BTSENVALMPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSEQUIPMENT = ReplaceableObject(
    'huawei_cm_2g."BTSEQUIPMENT"',
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
    t1."BTSID",
    t1."DEPLOYMENTID",
    t1."SITENAME"
FROM
huawei_nbi_gsm."BTSEQUIPMENT" t1

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
    t2."BTSID",
    t2."DEPLOYMENTID",
    t2."SITENAME"
FROM
huawei_gexport_gsm."BTSEQUIPMENT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."DEPLOYMENTID",
    t3."SITENAME"
FROM
huawei_gexport_gsm."BTSEQUIPMENT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."DEPLOYMENTID",
    t4."SITENAME"
FROM
huawei_mml_gsm."BTSEQUIPMENT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSESN = ReplaceableObject(
    'huawei_cm_2g."BTSESN"',
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
    t1."BTSID",
    t1."MAINDEVTAB",
    t1."OMBEARBOARD"
FROM
huawei_nbi_gsm."BTSESN" t1

"""
)

BTSETHOAM = ReplaceableObject(
    'huawei_cm_2g."BTSETHOAM"',
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
    t1."BTSID",
    t1."OAMTYPE"
FROM
huawei_nbi_gsm."BTSETHOAM" t1

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
    t2."BTSID",
    t2."OAMTYPE"
FROM
huawei_gexport_gsm."BTSETHOAM_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."OAMTYPE"
FROM
huawei_gexport_gsm."BTSETHOAM_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."OAMTYPE"
FROM
huawei_mml_gsm."BTSETHOAM" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSETHOAMAH = ReplaceableObject(
    'huawei_cm_2g."BTSETHOAMAH"',
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
    t1."BTSID",
    t1."CN",
    t1."ERFAMPARA",
    t1."ERFAMPRDPARA",
    t1."ERFAMPRDPRID",
    t1."ERFAMPRID",
    t1."ERFAMSCDPARA",
    t1."ERFAMSCDPRID",
    t1."PDUPRID",
    t1."PDUSIZE",
    t1."PN",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSETHOAMAH" t1

"""
)

BTSETHPORT = ReplaceableObject(
    'huawei_cm_2g."BTSETHPORT"',
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
    t1."BTSID",
    t1."CN",
    t1."FC",
    t1."IPEAAT",
    t1."IPEADT",
    t1."MACEAAT",
    t1."MACEADT",
    t1."MTU",
    t1."PN",
    t1."RATE",
    t1."RXBCPKTALMCLRTHD",
    t1."RXBCPKTALMOCRTHD",
    t1."SN",
    t1."SRN",
    t1."SWITCH3AH",
    t1."DUPLEX"
FROM
huawei_nbi_gsm."BTSETHPORT" t1

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
    t2."BTSID",
    t2."CN",
    t2."FC",
    t2."IPEAAT",
    t2."IPEADT",
    t2."MACEAAT",
    t2."MACEADT",
    t2."MTU",
    t2."PN",
    t2."RATE",
    t2."RXBCPKTALMCLRTHD",
    t2."RXBCPKTALMOCRTHD",
    t2."SN",
    t2."SRN",
    t2."SWITCH3AH",
    NULL
FROM
huawei_gexport_gsm."BTSETHPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CN",
    t3."FC",
    t3."IPEAAT",
    t3."IPEADT",
    t3."MACEAAT",
    t3."MACEADT",
    t3."MTU",
    t3."PN",
    t3."RATE",
    t3."RXBCPKTALMCLRTHD",
    t3."RXBCPKTALMOCRTHD",
    t3."SN",
    t3."SRN",
    t3."SWITCH3AH",
    NULL
FROM
huawei_gexport_gsm."BTSETHPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CN",
    t4."FC",
    t4."IPEAAT",
    t4."IPEADT",
    t4."MACEAAT",
    t4."MACEADT",
    t4."MTU",
    t4."PN",
    t4."RATE",
    t4."RXBCPKTALMCLRTHD",
    t4."RXBCPKTALMOCRTHD",
    t4."SN",
    t4."SRN",
    t4."SWITCH3AH",
    NULL
FROM
huawei_mml_gsm."BTSETHPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSFALLBACK = ReplaceableObject(
    'huawei_cm_2g."BTSFALLBACK"',
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
    t1."BTSID",
    t1."ENABLE"
FROM
huawei_nbi_gsm."BTSFALLBACK" t1

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
    t2."BTSID",
    t2."ENABLE"
FROM
huawei_gexport_gsm."BTSFALLBACK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."ENABLE"
FROM
huawei_gexport_gsm."BTSFALLBACK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."ENABLE"
FROM
huawei_mml_gsm."BTSFALLBACK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSFLEXABISPARA = ReplaceableObject(
    'huawei_cm_2g."BTSFLEXABISPARA"',
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
    t1."BTSID",
    t1."GROUPRELTSNUM",
    t1."PCUPREEMPTFLAG",
    t1."RSVTCHTSNUM"
FROM
huawei_nbi_gsm."BTSFLEXABISPARA" t1

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
    t2."BTSID",
    t2."GROUPRELTSNUM",
    t2."PCUPREEMPTFLAG",
    t2."RSVTCHTSNUM"
FROM
huawei_gexport_gsm."BTSFLEXABISPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."GROUPRELTSNUM",
    t3."PCUPREEMPTFLAG",
    t3."RSVTCHTSNUM"
FROM
huawei_gexport_gsm."BTSFLEXABISPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."GROUPRELTSNUM",
    t4."PCUPREEMPTFLAG",
    t4."RSVTCHTSNUM"
FROM
huawei_mml_gsm."BTSFLEXABISPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSFMUABP = ReplaceableObject(
    'huawei_cm_2g."BTSFMUABP"',
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
    t1."ADDR",
    t1."BTSID",
    t1."CFGFLAG",
    t1."CN",
    t1."FMUTYPE",
    t1."MCN",
    t1."MPN",
    t1."MSRN",
    t1."SBAF",
    t1."SN",
    t1."SPECIALSWITCHERLEVEL",
    t1."SRN",
    t1."STC",
    t1."TCMODE"
FROM
huawei_nbi_gsm."BTSFMUABP" t1

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
    t2."ADDR",
    t2."BTSID",
    t2."CFGFLAG",
    t2."CN",
    t2."FMUTYPE",
    t2."MCN",
    t2."MPN",
    t2."MSRN",
    NULL,
    t2."SN",
    NULL,
    t2."SRN",
    t2."STC",
    t2."TCMODE"
FROM
huawei_gexport_gsm."BTSFMUABP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADDR",
    t3."BTSID",
    t3."CFGFLAG",
    t3."CN",
    t3."FMUTYPE",
    t3."MCN",
    t3."MPN",
    t3."MSRN",
    NULL,
    t3."SN",
    NULL,
    t3."SRN",
    t3."STC",
    t3."TCMODE"
FROM
huawei_gexport_gsm."BTSFMUABP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADDR",
    t4."BTSID",
    t4."CFGFLAG",
    t4."CN",
    t4."FMUTYPE",
    t4."MCN",
    t4."MPN",
    t4."MSRN",
    NULL,
    t4."SN",
    NULL,
    t4."SRN",
    t4."STC",
    t4."TCMODE"
FROM
huawei_mml_gsm."BTSFMUABP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSGTRANSPARA = ReplaceableObject(
    'huawei_cm_2g."BTSGTRANSPARA"',
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
    t1."ARPAGINGTIME",
    t1."BTSID",
    t1."RATECFGTYPE",
    t1."ROUTINGBACKDELAYTIME"
FROM
huawei_nbi_gsm."BTSGTRANSPARA" t1

"""
)

BTSGUPWRSHRFP = ReplaceableObject(
    'huawei_cm_2g."BTSGUPWRSHRFP"',
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
    t1."BTSID",
    t1."CFGFLAG"
FROM
huawei_nbi_gsm."BTSGUPWRSHRFP" t1

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
    t2."BTSID",
    t2."CFGFLAG"
FROM
huawei_gexport_gsm."BTSGUPWRSHRFP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CFGFLAG"
FROM
huawei_gexport_gsm."BTSGUPWRSHRFP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CFGFLAG"
FROM
huawei_mml_gsm."BTSGUPWRSHRFP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSIDLETS = ReplaceableObject(
    'huawei_cm_2g."BTSIDLETS"',
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
    t1."BTSID",
    t1."CGN",
    t1."OPNAME",
    t1."TSCOUNT"
FROM
huawei_nbi_gsm."BTSIDLETS" t1

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
    t2."BTSID",
    t2."CGN",
    t2."OPNAME",
    t2."TSCOUNT"
FROM
huawei_gexport_gsm."BTSIDLETS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CGN",
    t3."OPNAME",
    t3."TSCOUNT"
FROM
huawei_gexport_gsm."BTSIDLETS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CGN",
    t4."OPNAME",
    t4."TSCOUNT"
FROM
huawei_mml_gsm."BTSIDLETS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSIKECFG = ReplaceableObject(
    'huawei_cm_2g."BTSIKECFG"',
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
    t1."BTSID",
    t1."DSCP",
    t1."IKEKLI",
    t1."IKEKLT",
    t1."NATKLI"
FROM
huawei_nbi_gsm."BTSIKECFG" t1

"""
)

BTSINTRXUSPEC = ReplaceableObject(
    'huawei_cm_2g."BTSINTRXUSPEC"',
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
    t1."RXUSPECENUMDESC",
    t1."RXUSPECENUMNAME",
    t1."RXUSPECENUMVALUE",
    t1."RXUSPECMODULENAME"
FROM
huawei_nbi_gsm."BTSINTRXUSPEC" t1

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
    t2."RXUSPECENUMDESC",
    t2."RXUSPECENUMNAME",
    t2."RXUSPECENUMVALUE",
    t2."RXUSPECMODULENAME"
FROM
huawei_gexport_gsm."BTSINTRXUSPEC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."RXUSPECENUMDESC",
    t3."RXUSPECENUMNAME",
    t3."RXUSPECENUMVALUE",
    t3."RXUSPECMODULENAME"
FROM
huawei_gexport_gsm."BTSINTRXUSPEC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

BTSIP = ReplaceableObject(
    'huawei_cm_2g."BTSIP"',
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
    t1."BSCIP",
    t1."BTSCOMTYPE",
    t1."BTSGWIPSWITCH",
    t1."BTSID",
    t1."BTSIP",
    t1."BTSMUTIP",
    t1."CFGFLAG",
    t1."GWIP",
    t1."HOSTTYPE",
    t1."LPN",
    t1."PEERBSCIP",
    t1."PEERBSCMASK",
    t1."RSCMNGMODE",
    t1."SN"
FROM
huawei_nbi_gsm."BTSIP" t1

"""
)

BTSIPCLKPARA = ReplaceableObject(
    'huawei_cm_2g."BTSIPCLKPARA"',
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
    t1."BTSID",
    t1."CLKPRTTYPE",
    t1."CLKTOPOMODE",
    t1."DN",
    t1."ISCLKREDUCY",
    t1."MASTERIPADDR",
    t1."PRFTYPE",
    t1."SER0PRI",
    t1."SYNMODE"
FROM
huawei_nbi_gsm."BTSIPCLKPARA" t1

"""
)

BTSIPGUARD = ReplaceableObject(
    'huawei_cm_2g."BTSIPGUARD"',
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
    t1."ARPLRNSTRICTSW",
    t1."ARPSPOOFCHKSW",
    t1."BTSID",
    t1."INVALIDPKTCHKSW",
    t1."IPSECREPLAYCHKSW"
FROM
huawei_nbi_gsm."BTSIPGUARD" t1

"""
)

BTSIPRT = ReplaceableObject(
    'huawei_cm_2g."BTSIPRT"',
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
    t1."BTSID",
    t1."CN",
    t1."DSTIP",
    t1."DSTMASK",
    t1."NEXTHOP",
    t1."PRI",
    t1."RTIDX",
    t1."RTTYPE",
    t1."SN",
    t1."SRN",
    t1."IFNO",
    t1."ITFTYPE"
FROM
huawei_nbi_gsm."BTSIPRT" t1

"""
)

BTSJBF = ReplaceableObject(
    'huawei_cm_2g."BTSJBF"',
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
    t1."BTSID",
    t1."JBF"
FROM
huawei_nbi_gsm."BTSJBF" t1

"""
)

BTSLAPDWS = ReplaceableObject(
    'huawei_cm_2g."BTSLAPDWS"',
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
    t1."BTSID",
    t1."OMLWS",
    t1."RSLWS",
    t1."UPOMLWS",
    t1."UPRSLWS"
FROM
huawei_nbi_gsm."BTSLAPDWS" t1

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
    t2."BTSID",
    t2."OMLWS",
    t2."RSLWS",
    t2."UPOMLWS",
    t2."UPRSLWS"
FROM
huawei_gexport_gsm."BTSLAPDWS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."OMLWS",
    t3."RSLWS",
    t3."UPOMLWS",
    t3."UPRSLWS"
FROM
huawei_gexport_gsm."BTSLAPDWS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."OMLWS",
    t4."RSLWS",
    t4."UPOMLWS",
    t4."UPRSLWS"
FROM
huawei_mml_gsm."BTSLAPDWS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSLLDPGLOBAL = ReplaceableObject(
    'huawei_cm_2g."BTSLLDPGLOBAL"',
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
    t1."BTSID",
    t1."DELAY",
    t1."HOLDMULTI",
    t1."NOTIFYINTERVAL",
    t1."NOTIFYSW",
    t1."RESTARTDELAY",
    t1."TXINTVAL"
FROM
huawei_nbi_gsm."BTSLLDPGLOBAL" t1

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
    t2."BTSID",
    t2."DELAY",
    t2."HOLDMULTI",
    t2."NOTIFYINTERVAL",
    t2."NOTIFYSW",
    t2."RESTARTDELAY",
    t2."TXINTVAL"
FROM
huawei_gexport_gsm."BTSLLDPGLOBAL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."DELAY",
    t3."HOLDMULTI",
    t3."NOTIFYINTERVAL",
    t3."NOTIFYSW",
    t3."RESTARTDELAY",
    t3."TXINTVAL"
FROM
huawei_gexport_gsm."BTSLLDPGLOBAL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."DELAY",
    t4."HOLDMULTI",
    t4."NOTIFYINTERVAL",
    t4."NOTIFYSW",
    t4."RESTARTDELAY",
    t4."TXINTVAL"
FROM
huawei_mml_gsm."BTSLLDPGLOBAL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSLNKBKATTR = ReplaceableObject(
    'huawei_cm_2g."BTSLNKBKATTR"',
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
    t1."BTSID",
    t1."DETECTCOUNT",
    t1."DETECTTXINT",
    t1."REVERTIVETYPE",
    t1."WTBS"
FROM
huawei_nbi_gsm."BTSLNKBKATTR" t1

"""
)

BTSLOCGRP = ReplaceableObject(
    'huawei_cm_2g."BTSLOCGRP"',
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
    t1."BTSID",
    t1."ISMAINLOCGRP",
    t1."LOCGRPNO",
    t1."OUTPUTPOWER",
    t1."OUTPUTPOWERUNIT",
    t1."PSRACJACCLEV",
    t1."RACJACCLEV"
FROM
huawei_nbi_gsm."BTSLOCGRP" t1

"""
)

BTSLOCKBCCH = ReplaceableObject(
    'huawei_cm_2g."BTSLOCKBCCH"',
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
    t1."BTSID",
    t1."BTSPOWEROFFLOCKBCCH"
FROM
huawei_nbi_gsm."BTSLOCKBCCH" t1

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
    t2."BTSID",
    t2."BTSPOWEROFFLOCKBCCH"
FROM
huawei_gexport_gsm."BTSLOCKBCCH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."BTSPOWEROFFLOCKBCCH"
FROM
huawei_gexport_gsm."BTSLOCKBCCH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."BTSPOWEROFFLOCKBCCH"
FROM
huawei_mml_gsm."BTSLOCKBCCH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSLR = ReplaceableObject(
    'huawei_cm_2g."BTSLR"',
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
    t1."BTSID",
    t1."CN",
    t1."LRSW",
    t1."PN",
    t1."PT",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSLR" t1

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
    t2."BTSID",
    t2."CN",
    t2."LRSW",
    t2."PN",
    t2."PT",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."BTSLR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CN",
    t3."LRSW",
    t3."PN",
    t3."PT",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."BTSLR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CN",
    t4."LRSW",
    t4."PN",
    t4."PT",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."BTSLR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSLSW = ReplaceableObject(
    'huawei_cm_2g."BTSLSW"',
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
    t1."BTSID",
    t1."ISSUPPORTBTSLSWITCH"
FROM
huawei_nbi_gsm."BTSLSW" t1

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
    t2."BTSID",
    t2."ISSUPPORTBTSLSWITCH"
FROM
huawei_gexport_gsm."BTSLSW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."ISSUPPORTBTSLSWITCH"
FROM
huawei_gexport_gsm."BTSLSW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."ISSUPPORTBTSLSWITCH"
FROM
huawei_mml_gsm."BTSLSW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSMNTMODE = ReplaceableObject(
    'huawei_cm_2g."BTSMNTMODE"',
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
    t1."BTSID",
    t1."MNTMODE",
    t1."ET",
    t1."ST"
FROM
huawei_nbi_gsm."BTSMNTMODE" t1

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
    t2."BTSID",
    t2."MNTMODE",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSMNTMODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."MNTMODE",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSMNTMODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."MNTMODE",
    NULL,
    NULL
FROM
huawei_mml_gsm."BTSMNTMODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSMPGRP = ReplaceableObject(
    'huawei_cm_2g."BTSMPGRP"',
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
    t1."ACFC",
    t1."AUTHTYPE",
    t1."BTSID",
    t1."CN",
    t1."IPEAAT",
    t1."IPEADT",
    t1."IPHC",
    t1."LOCALIP",
    t1."MASK",
    t1."MCCLASS",
    t1."MHF",
    t1."MPGRPEAAT",
    t1."MPGRPEADT",
    t1."MPGRPN",
    t1."MPSWITCH",
    t1."PEERIP",
    t1."PFC",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSMPGRP" t1

"""
)

BTSMPLNK = ReplaceableObject(
    'huawei_cm_2g."BTSMPLNK"',
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
    t1."BTSID",
    t1."CN",
    t1."MPGRPN",
    t1."MRU",
    t1."PN",
    t1."PPPLNKN",
    t1."RSTIME",
    t1."SN",
    t1."SRN",
    t1."TSBITMAP"
FROM
huawei_nbi_gsm."BTSMPLNK" t1

"""
)

BTSOMLBACKUP = ReplaceableObject(
    'huawei_cm_2g."BTSOMLBACKUP"',
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
    t1."BTSID",
    t1."OMLBKUP"
FROM
huawei_nbi_gsm."BTSOMLBACKUP" t1

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
    t2."BTSID",
    t2."OMLBKUP"
FROM
huawei_gexport_gsm."BTSOMLBACKUP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."OMLBKUP"
FROM
huawei_gexport_gsm."BTSOMLBACKUP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."OMLBKUP"
FROM
huawei_mml_gsm."BTSOMLBACKUP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSOMLDETECT = ReplaceableObject(
    'huawei_cm_2g."BTSOMLDETECT"',
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
    t1."BTSID",
    t1."OMLDETECTSWITCH",
    t1."BTSBARCODE"
FROM
huawei_nbi_gsm."BTSOMLDETECT" t1

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
    t2."BTSID",
    t2."OMLDETECTSWITCH",
    NULL
FROM
huawei_gexport_gsm."BTSOMLDETECT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."OMLDETECTSWITCH",
    NULL
FROM
huawei_gexport_gsm."BTSOMLDETECT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."OMLDETECTSWITCH",
    NULL
FROM
huawei_mml_gsm."BTSOMLDETECT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSOMLTS = ReplaceableObject(
    'huawei_cm_2g."BTSOMLTS"',
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
    t1."BTSID",
    t1."CN",
    t1."PN",
    t1."SN",
    t1."SRN",
    t1."SUBTS",
    t1."TS"
FROM
huawei_nbi_gsm."BTSOMLTS" t1

"""
)

BTSOTHPARA = ReplaceableObject(
    'huawei_cm_2g."BTSOTHPARA"',
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
    t1."ABISIDLETSALLOC",
    t1."ABISIDLETSCFGSWITCH",
    t1."AISSOP",
    t1."AMRTRANSBANDTHCOMPSW",
    t1."BATIMS",
    t1."BTSDBUS32KCFGSW",
    t1."BTSDETECTSWITCH",
    t1."BTSID",
    t1."CPRIFASTRING",
    t1."E1PORTFAILDELAY",
    t1."E1PORTSTAQUICKREPSW",
    t1."ECMP",
    t1."ENERGYMNG",
    t1."FASTTRXAIDSW",
    t1."HIGHMODPWRSW",
    t1."IPCLKSYNMODE",
    t1."ISSUPERBTS",
    t1."JITBUFDELAY",
    t1."MCPACUTPWRPRIPOLICY",
    t1."MTSTURNOFF",
    t1."PAADJVOL",
    t1."PDCHGBR",
    t1."PROBESEQ",
    t1."PSUTURNINGOFFENABLE",
    t1."PTRAUTSNSNEXTSW",
    t1."RESETTIME",
    t1."SDBBLSD",
    t1."SENDSAMBE",
    t1."SPRECM",
    t1."SPRTLU",
    t1."STPPWRCHK",
    t1."SUPPORTE1UNBA",
    t1."SYNCMETHOD",
    t1."TSSHTDOWNEN",
    t1."VSWRDETECTSENENHSW",
    t1."VSWRTHRESOPT",
    t1."PRIVATEPROBEFST",
    t1."PRIVATEPROBENUM",
    t1."PRIVATEPROBESND"
FROM
huawei_nbi_gsm."BTSOTHPARA" t1

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
    t2."ABISIDLETSALLOC",
    t2."ABISIDLETSCFGSWITCH",
    t2."AISSOP",
    t2."AMRTRANSBANDTHCOMPSW",
    t2."BATIMS",
    t2."BTSDBUS32KCFGSW",
    t2."BTSDETECTSWITCH",
    t2."BTSID",
    t2."CPRIFASTRING",
    t2."E1PORTFAILDELAY",
    t2."E1PORTSTAQUICKREPSW",
    t2."ECMP",
    t2."ENERGYMNG",
    t2."FASTTRXAIDSW",
    t2."HIGHMODPWRSW",
    t2."IPCLKSYNMODE",
    NULL,
    t2."JITBUFDELAY",
    t2."MCPACUTPWRPRIPOLICY",
    t2."MTSTURNOFF",
    NULL,
    t2."PDCHGBR",
    t2."PROBESEQ",
    t2."PSUTURNINGOFFENABLE",
    t2."PTRAUTSNSNEXTSW",
    t2."RESETTIME",
    t2."SDBBLSD",
    t2."SENDSAMBE",
    t2."SPRECM",
    t2."SPRTLU",
    t2."STPPWRCHK",
    t2."SUPPORTE1UNBA",
    t2."SYNCMETHOD",
    t2."TSSHTDOWNEN",
    t2."VSWRDETECTSENENHSW",
    t2."VSWRTHRESOPT",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSOTHPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISIDLETSALLOC",
    t3."ABISIDLETSCFGSWITCH",
    t3."AISSOP",
    t3."AMRTRANSBANDTHCOMPSW",
    t3."BATIMS",
    t3."BTSDBUS32KCFGSW",
    t3."BTSDETECTSWITCH",
    t3."BTSID",
    t3."CPRIFASTRING",
    t3."E1PORTFAILDELAY",
    t3."E1PORTSTAQUICKREPSW",
    t3."ECMP",
    t3."ENERGYMNG",
    t3."FASTTRXAIDSW",
    t3."HIGHMODPWRSW",
    t3."IPCLKSYNMODE",
    NULL,
    t3."JITBUFDELAY",
    t3."MCPACUTPWRPRIPOLICY",
    t3."MTSTURNOFF",
    NULL,
    t3."PDCHGBR",
    t3."PROBESEQ",
    t3."PSUTURNINGOFFENABLE",
    t3."PTRAUTSNSNEXTSW",
    t3."RESETTIME",
    t3."SDBBLSD",
    t3."SENDSAMBE",
    t3."SPRECM",
    t3."SPRTLU",
    t3."STPPWRCHK",
    t3."SUPPORTE1UNBA",
    t3."SYNCMETHOD",
    t3."TSSHTDOWNEN",
    t3."VSWRDETECTSENENHSW",
    t3."VSWRTHRESOPT",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSOTHPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISIDLETSALLOC",
    t4."ABISIDLETSCFGSWITCH",
    t4."AISSOP",
    t4."AMRTRANSBANDTHCOMPSW",
    t4."BATIMS",
    t4."BTSDBUS32KCFGSW",
    t4."BTSDETECTSWITCH",
    t4."BTSID",
    t4."CPRIFASTRING",
    t4."E1PORTFAILDELAY",
    t4."E1PORTSTAQUICKREPSW",
    t4."ECMP",
    t4."ENERGYMNG",
    t4."FASTTRXAIDSW",
    t4."HIGHMODPWRSW",
    t4."IPCLKSYNMODE",
    t4."ISSUPERBTS",
    t4."JITBUFDELAY",
    t4."MCPACUTPWRPRIPOLICY",
    t4."MTSTURNOFF",
    t4."PAADJVOL",
    t4."PDCHGBR",
    t4."PROBESEQ",
    t4."PSUTURNINGOFFENABLE",
    t4."PTRAUTSNSNEXTSW",
    t4."RESETTIME",
    t4."SDBBLSD",
    t4."SENDSAMBE",
    t4."SPRECM",
    t4."SPRTLU",
    t4."STPPWRCHK",
    t4."SUPPORTE1UNBA",
    t4."SYNCMETHOD",
    t4."TSSHTDOWNEN",
    t4."VSWRDETECTSENENHSW",
    t4."VSWRTHRESOPT",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."BTSOTHPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSPATCHPARA = ReplaceableObject(
    'huawei_cm_2g."BTSPATCHPARA"',
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
    t1."BTSID",
    t1."RSVDPARA1",
    t1."RSVDPARA10",
    t1."RSVDPARA11",
    t1."RSVDPARA12",
    t1."RSVDPARA13",
    t1."RSVDPARA14",
    t1."RSVDPARA15",
    t1."RSVDPARA16",
    t1."RSVDPARA17",
    t1."RSVDPARA18",
    t1."RSVDPARA19",
    t1."RSVDPARA2",
    t1."RSVDPARA20",
    t1."RSVDPARA3",
    t1."RSVDPARA4",
    t1."RSVDPARA5",
    t1."RSVDPARA6",
    t1."RSVDPARA7",
    t1."RSVDPARA8",
    t1."RSVDPARA9"
FROM
huawei_nbi_gsm."BTSPATCHPARA" t1

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
    t2."BTSID",
    t2."RSVDPARA1",
    t2."RSVDPARA10",
    t2."RSVDPARA11",
    t2."RSVDPARA12",
    t2."RSVDPARA13",
    t2."RSVDPARA14",
    t2."RSVDPARA15",
    t2."RSVDPARA16",
    t2."RSVDPARA17",
    t2."RSVDPARA18",
    t2."RSVDPARA19",
    t2."RSVDPARA2",
    t2."RSVDPARA20",
    t2."RSVDPARA3",
    t2."RSVDPARA4",
    t2."RSVDPARA5",
    t2."RSVDPARA6",
    t2."RSVDPARA7",
    t2."RSVDPARA8",
    t2."RSVDPARA9"
FROM
huawei_gexport_gsm."BTSPATCHPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."RSVDPARA1",
    t3."RSVDPARA10",
    t3."RSVDPARA11",
    t3."RSVDPARA12",
    t3."RSVDPARA13",
    t3."RSVDPARA14",
    t3."RSVDPARA15",
    t3."RSVDPARA16",
    t3."RSVDPARA17",
    t3."RSVDPARA18",
    t3."RSVDPARA19",
    t3."RSVDPARA2",
    t3."RSVDPARA20",
    t3."RSVDPARA3",
    t3."RSVDPARA4",
    t3."RSVDPARA5",
    t3."RSVDPARA6",
    t3."RSVDPARA7",
    t3."RSVDPARA8",
    t3."RSVDPARA9"
FROM
huawei_gexport_gsm."BTSPATCHPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."RSVDPARA1",
    t4."RSVDPARA10",
    t4."RSVDPARA11",
    t4."RSVDPARA12",
    t4."RSVDPARA13",
    t4."RSVDPARA14",
    t4."RSVDPARA15",
    t4."RSVDPARA16",
    t4."RSVDPARA17",
    t4."RSVDPARA18",
    t4."RSVDPARA19",
    t4."RSVDPARA2",
    t4."RSVDPARA20",
    t4."RSVDPARA3",
    t4."RSVDPARA4",
    t4."RSVDPARA5",
    t4."RSVDPARA6",
    t4."RSVDPARA7",
    t4."RSVDPARA8",
    t4."RSVDPARA9"
FROM
huawei_mml_gsm."BTSPATCHPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSPINGSW = ReplaceableObject(
    'huawei_cm_2g."BTSPINGSW"',
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
    t1."BTSID",
    t1."BTSPINGSWITCH"
FROM
huawei_nbi_gsm."BTSPINGSW" t1

"""
)

BTSPLRALM = ReplaceableObject(
    'huawei_cm_2g."BTSPLRALM"',
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
    t1."BTSID",
    t1."CFGFLAG"
FROM
huawei_nbi_gsm."BTSPLRALM" t1

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
    t2."BTSID",
    t2."CFGFLAG"
FROM
huawei_gexport_gsm."BTSPLRALM_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CFGFLAG"
FROM
huawei_gexport_gsm."BTSPLRALM_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CFGFLAG"
FROM
huawei_mml_gsm."BTSPLRALM" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSPSUFP = ReplaceableObject(
    'huawei_cm_2g."BTSPSUFP"',
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
    t1."BTSID",
    t1."CFGFLAG"
FROM
huawei_nbi_gsm."BTSPSUFP" t1

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
    t2."BTSID",
    t2."CFGFLAG"
FROM
huawei_gexport_gsm."BTSPSUFP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CFGFLAG"
FROM
huawei_gexport_gsm."BTSPSUFP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CFGFLAG"
FROM
huawei_mml_gsm."BTSPSUFP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSRELIALOGSWITCH = ReplaceableObject(
    'huawei_cm_2g."BTSRELIALOGSWITCH"',
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
    t1."BTSID",
    t1."RELIABILITYLOGSWITCH"
FROM
huawei_nbi_gsm."BTSRELIALOGSWITCH" t1

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
    t2."BTSID",
    t2."RELIABILITYLOGSWITCH"
FROM
huawei_gexport_gsm."BTSRELIALOGSWITCH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."RELIABILITYLOGSWITCH"
FROM
huawei_gexport_gsm."BTSRELIALOGSWITCH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."RELIABILITYLOGSWITCH"
FROM
huawei_mml_gsm."BTSRELIALOGSWITCH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSRET = ReplaceableObject(
    'huawei_cm_2g."BTSRET"',
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
    t1."BTSID",
    t1."CTRLPORTCN",
    t1."CTRLPORTNO",
    t1."CTRLPORTSN",
    t1."CTRLPORTSRN",
    t1."DEVICENAME",
    t1."DEVICENO",
    t1."POLARTYPE",
    t1."RETTYPE",
    t1."SCENARIO",
    t1."SERIALNO",
    t1."VENDORCODE"
FROM
huawei_nbi_gsm."BTSRET" t1

"""
)

BTSRETDEVICEDATA = ReplaceableObject(
    'huawei_cm_2g."BTSRETDEVICEDATA"',
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
    t1."BAND1",
    t1."BAND2",
    t1."BAND3",
    t1."BAND4",
    t1."BEARING",
    t1."BTSID",
    t1."DEVICENO",
    t1."SUBUNITNO",
    t1."TILT"
FROM
huawei_nbi_gsm."BTSRETDEVICEDATA" t1

"""
)

BTSRETSUBUNIT = ReplaceableObject(
    'huawei_cm_2g."BTSRETSUBUNIT"',
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
    t1."AER",
    t1."BTSID",
    t1."CELLID",
    t1."CONNCN1",
    t1."CONNCN2",
    t1."CONNPN1",
    t1."CONNPN2",
    t1."CONNSN1",
    t1."CONNSN2",
    t1."CONNSRN1",
    t1."CONNSRN2",
    t1."DEVICENO",
    t1."SUBUNITNO",
    t1."TILT"
FROM
huawei_nbi_gsm."BTSRETSUBUNIT" t1

"""
)

BTSRINGATTR = ReplaceableObject(
    'huawei_cm_2g."BTSRINGATTR"',
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
    t1."BTSID",
    t1."FASTCNETFLAG",
    t1."RINGNETDOUBLEDIRSWITCH",
    t1."TBS",
    t1."WTBS"
FROM
huawei_nbi_gsm."BTSRINGATTR" t1

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
    t2."BTSID",
    t2."FASTCNETFLAG",
    t2."RINGNETDOUBLEDIRSWITCH",
    t2."TBS",
    t2."WTBS"
FROM
huawei_gexport_gsm."BTSRINGATTR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."FASTCNETFLAG",
    t3."RINGNETDOUBLEDIRSWITCH",
    t3."TBS",
    t3."WTBS"
FROM
huawei_gexport_gsm."BTSRINGATTR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

BTSRSV = ReplaceableObject(
    'huawei_cm_2g."BTSRSV"',
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
    t1."BTSID",
    t1."RSVID",
    t1."RSVVALUE"
FROM
huawei_nbi_gsm."BTSRSV" t1

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
    t2."BTSID",
    t2."RSVID",
    t2."RSVVALUE"
FROM
huawei_gexport_gsm."BTSRSV_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."RSVID",
    t3."RSVVALUE"
FROM
huawei_gexport_gsm."BTSRSV_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    NULL,
    NULL
FROM
huawei_mml_gsm."BTSRSV" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSRXU2LOCGRP = ReplaceableObject(
    'huawei_cm_2g."BTSRXU2LOCGRP"',
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
    t1."BTSID",
    t1."CN",
    t1."LOCGRPNO",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."BTSRXU2LOCGRP" t1

"""
)

BTSRXUBP = ReplaceableObject(
    'huawei_cm_2g."BTSRXUBP"',
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
    t1."BTSID",
    t1."CN",
    t1."GUPWRSHARESWITCH",
    t1."GXPWRSHARERLTMOSW",
    t1."HAVETT1",
    t1."HAVETT2",
    t1."HAVETT3",
    t1."HAVETT4",
    t1."HAVETT5",
    t1."HAVETT6",
    t1."HAVETT7",
    t1."HAVETT8",
    t1."IFOFFSET",
    t1."LVL1VSWR",
    t1."LVL2VSWR",
    t1."MRRUATTENFACTOR1",
    t1."MRRUATTENFACTOR2",
    t1."MRRUATTENFACTOR3",
    t1."MRRUATTENFACTOR4",
    t1."MRRUATTENFACTOR5",
    t1."MRRUATTENFACTOR6",
    t1."MRRUATTENFACTOR7",
    t1."MRRUATTENFACTOR8",
    t1."PASHRMODE",
    t1."PWRSWITCHA",
    t1."PWRSWITCHB",
    t1."PWRSWITCHC",
    t1."PWRSWITCHD",
    t1."PWRSWITCHE",
    t1."PWRSWITCHF",
    t1."PWRSWITCHG",
    t1."PWRSWITCHH",
    t1."RELATEDMODFUNC",
    t1."RRCSWITCH",
    t1."RSSIALARMCFGSWITCH",
    t1."RXFREQBANDMUTUALSW",
    t1."RXUTYPE",
    t1."SN",
    t1."SNDRCVMODE3",
    t1."SPTSHARING",
    t1."SRN",
    t1."VSWRALMDISPOSE",
    t1."WORKINGSTANDARD",
    t1."TXAOPER1",
    t1."TXAOPER2",
    t1."TXAOPER3",
    t1."TXAOPER4",
    t1."TXBOPER1",
    t1."TXBOPER2",
    t1."TXBOPER3",
    t1."TXBOPER4",
    t1."TXCOPER1",
    t1."TXCOPER2",
    t1."TXCOPER3",
    t1."TXCOPER4",
    t1."TXDOPER1",
    t1."TXDOPER2",
    t1."TXDOPER3",
    t1."TXDOPER4",
    t1."TXEOPER1",
    t1."TXEOPER2",
    t1."TXEOPER3",
    t1."TXEOPER4",
    t1."TXFOPER1",
    t1."TXFOPER2",
    t1."TXFOPER3",
    t1."TXFOPER4",
    t1."TXGOPER1",
    t1."TXGOPER2",
    t1."TXGOPER3",
    t1."TXGOPER4",
    t1."TXHOPER1",
    t1."TXHOPER2",
    t1."TXHOPER3",
    t1."TXHOPER4",
    t1."ADEF",
    t1."LNA1",
    t1."LNA2",
    t1."PWRSWITCHRET",
    t1."SNDRCVMODE2",
    t1."OVERCURALMTHDRET",
    t1."OVERCURCLRTHDRET",
    t1."THRESHOLDTYPERET",
    t1."UNDERCURALMTHDRET",
    t1."UNDERCURCLRTHDRET",
    t1."CHKMODA",
    t1."CHKMODB",
    t1."OVERCURALMTHDA",
    t1."OVERCURALMTHDB",
    t1."OVERCURCLRTHDA",
    t1."OVERCURCLRTHDB",
    t1."UNDERCURALMTHDA",
    t1."UNDERCURALMTHDB",
    t1."UNDERCURCLRTHDA",
    t1."UNDERCURCLRTHDB",
    t1."RSSILOWTHRESHOLD",
    t1."RSSIUNBALANCEDTHRESHOLD"
FROM
huawei_nbi_gsm."BTSRXUBP" t1

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
    t2."BTSID",
    t2."CN",
    t2."GUPWRSHARESWITCH",
    t2."GXPWRSHARERLTMOSW",
    t2."HAVETT1",
    t2."HAVETT2",
    t2."HAVETT3",
    t2."HAVETT4",
    t2."HAVETT5",
    t2."HAVETT6",
    t2."HAVETT7",
    t2."HAVETT8",
    t2."IFOFFSET",
    t2."LVL1VSWR",
    t2."LVL2VSWR",
    t2."MRRUATTENFACTOR1",
    t2."MRRUATTENFACTOR2",
    t2."MRRUATTENFACTOR3",
    t2."MRRUATTENFACTOR4",
    t2."MRRUATTENFACTOR5",
    t2."MRRUATTENFACTOR6",
    t2."MRRUATTENFACTOR7",
    t2."MRRUATTENFACTOR8",
    t2."PASHRMODE",
    t2."PWRSWITCHA",
    t2."PWRSWITCHB",
    t2."PWRSWITCHC",
    t2."PWRSWITCHD",
    t2."PWRSWITCHE",
    t2."PWRSWITCHF",
    t2."PWRSWITCHG",
    t2."PWRSWITCHH",
    t2."RELATEDMODFUNC",
    t2."RRCSWITCH",
    t2."RSSIALARMCFGSWITCH",
    t2."RXFREQBANDMUTUALSW",
    t2."RXUTYPE",
    t2."SN",
    t2."SNDRCVMODE3",
    t2."SPTSHARING",
    t2."SRN",
    t2."VSWRALMDISPOSE",
    t2."WORKINGSTANDARD",
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
huawei_gexport_gsm."BTSRXUBP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CN",
    t3."GUPWRSHARESWITCH",
    t3."GXPWRSHARERLTMOSW",
    t3."HAVETT1",
    t3."HAVETT2",
    t3."HAVETT3",
    t3."HAVETT4",
    t3."HAVETT5",
    t3."HAVETT6",
    t3."HAVETT7",
    t3."HAVETT8",
    t3."IFOFFSET",
    t3."LVL1VSWR",
    t3."LVL2VSWR",
    t3."MRRUATTENFACTOR1",
    t3."MRRUATTENFACTOR2",
    t3."MRRUATTENFACTOR3",
    t3."MRRUATTENFACTOR4",
    t3."MRRUATTENFACTOR5",
    t3."MRRUATTENFACTOR6",
    t3."MRRUATTENFACTOR7",
    t3."MRRUATTENFACTOR8",
    t3."PASHRMODE",
    t3."PWRSWITCHA",
    t3."PWRSWITCHB",
    t3."PWRSWITCHC",
    t3."PWRSWITCHD",
    t3."PWRSWITCHE",
    t3."PWRSWITCHF",
    t3."PWRSWITCHG",
    t3."PWRSWITCHH",
    t3."RELATEDMODFUNC",
    t3."RRCSWITCH",
    t3."RSSIALARMCFGSWITCH",
    t3."RXFREQBANDMUTUALSW",
    t3."RXUTYPE",
    t3."SN",
    t3."SNDRCVMODE3",
    t3."SPTSHARING",
    t3."SRN",
    t3."VSWRALMDISPOSE",
    t3."WORKINGSTANDARD",
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
huawei_gexport_gsm."BTSRXUBP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CN",
    t4."GUPWRSHARESWITCH",
    t4."GXPWRSHARERLTMOSW",
    t4."HAVETT1",
    t4."HAVETT2",
    t4."HAVETT3",
    t4."HAVETT4",
    t4."HAVETT5",
    t4."HAVETT6",
    t4."HAVETT7",
    t4."HAVETT8",
    t4."IFOFFSET",
    t4."LVL1VSWR",
    t4."LVL2VSWR",
    t4."MRRUATTENFACTOR1",
    t4."MRRUATTENFACTOR2",
    t4."MRRUATTENFACTOR3",
    t4."MRRUATTENFACTOR4",
    t4."MRRUATTENFACTOR5",
    t4."MRRUATTENFACTOR6",
    t4."MRRUATTENFACTOR7",
    t4."MRRUATTENFACTOR8",
    t4."PASHRMODE",
    t4."PWRSWITCHA",
    t4."PWRSWITCHB",
    t4."PWRSWITCHC",
    t4."PWRSWITCHD",
    t4."PWRSWITCHE",
    t4."PWRSWITCHF",
    t4."PWRSWITCHG",
    t4."PWRSWITCHH",
    t4."RELATEDMODFUNC",
    t4."RRCSWITCH",
    t4."RSSIALARMCFGSWITCH",
    t4."RXFREQBANDMUTUALSW",
    t4."RXUTYPE",
    t4."SN",
    t4."SNDRCVMODE3",
    t4."SPTSHARING",
    t4."SRN",
    t4."VSWRALMDISPOSE",
    t4."WORKINGSTANDARD",
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
    t4."LNA1",
    t4."LNA2",
    t4."PWRSWITCHRET",
    t4."SNDRCVMODE2",
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
    NULL
FROM
huawei_mml_gsm."BTSRXUBP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSRXUBRD = ReplaceableObject(
    'huawei_cm_2g."BTSRXUBRD"',
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
    t1."BRDRXBW",
    t1."BRDTXBW",
    t1."BT",
    t1."BTSID",
    t1."CN",
    t1."ISCONFIGTHD",
    t1."PWRMODE",
    t1."RXUCHAINNO",
    t1."RXUNAME",
    t1."RXUPOS",
    t1."RXUSPEC",
    t1."SN",
    t1."SRN",
    t1."TRXNUM",
    t1."RXUSPECNAME"
FROM
huawei_nbi_gsm."BTSRXUBRD" t1

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
    NULL,
    t2."BT",
    t2."BTSID",
    t2."CN",
    t2."ISCONFIGTHD",
    NULL,
    t2."RXUCHAINNO",
    t2."RXUNAME",
    t2."RXUPOS",
    t2."RXUSPEC",
    t2."SN",
    t2."SRN",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSRXUBRD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    NULL,
    t3."BT",
    t3."BTSID",
    t3."CN",
    t3."ISCONFIGTHD",
    NULL,
    t3."RXUCHAINNO",
    t3."RXUNAME",
    t3."RXUPOS",
    t3."RXUSPEC",
    t3."SN",
    t3."SRN",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSRXUBRD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BRDRXBW",
    t4."BRDTXBW",
    t4."BT",
    t4."BTSID",
    t4."CN",
    t4."ISCONFIGTHD",
    t4."PWRMODE",
    t4."RXUCHAINNO",
    t4."RXUNAME",
    t4."RXUPOS",
    t4."RXUSPEC",
    t4."SN",
    t4."SRN",
    t4."TRXNUM",
    NULL
FROM
huawei_mml_gsm."BTSRXUBRD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSRXUCHAIN = ReplaceableObject(
    'huawei_cm_2g."BTSRXUCHAIN"',
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
    t1."BTSID",
    t1."CMEAT",
    t1."HCN",
    t1."HPN",
    t1."HSN",
    t1."HSRN",
    t1."RCN",
    t1."TT"
FROM
huawei_nbi_gsm."BTSRXUCHAIN" t1

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
    t2."BTSID",
    NULL,
    t2."HCN",
    t2."HPN",
    t2."HSN",
    t2."HSRN",
    t2."RCN",
    t2."TT"
FROM
huawei_gexport_gsm."BTSRXUCHAIN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    NULL,
    t3."HCN",
    t3."HPN",
    t3."HSN",
    t3."HSRN",
    t3."RCN",
    t3."TT"
FROM
huawei_gexport_gsm."BTSRXUCHAIN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    NULL,
    t4."HCN",
    t4."HPN",
    t4."HSN",
    t4."HSRN",
    t4."RCN",
    t4."TT"
FROM
huawei_mml_gsm."BTSRXUCHAIN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSSHARING = ReplaceableObject(
    'huawei_cm_2g."BTSSHARING"',
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
    t1."BTSID",
    t1."SHARINGALLOW",
    t1."SPTTRMSHARE"
FROM
huawei_nbi_gsm."BTSSHARING" t1

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
    t2."BTSID",
    t2."SHARINGALLOW",
    NULL
FROM
huawei_gexport_gsm."BTSSHARING_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."SHARINGALLOW",
    NULL
FROM
huawei_gexport_gsm."BTSSHARING_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."SHARINGALLOW",
    NULL
FROM
huawei_mml_gsm."BTSSHARING" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSTEMPLATERSC = ReplaceableObject(
    'huawei_cm_2g."BTSTEMPLATERSC"',
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
    t1."TEMPLATENAME"
FROM
huawei_nbi_gsm."BTSTEMPLATERSC" t1

"""
)

BTSTHEFTALM = ReplaceableObject(
    'huawei_cm_2g."BTSTHEFTALM"',
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
    t1."ANTITHEFTALLOW",
    t1."BTSID"
FROM
huawei_nbi_gsm."BTSTHEFTALM" t1

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
    t2."ANTITHEFTALLOW",
    t2."BTSID"
FROM
huawei_gexport_gsm."BTSTHEFTALM_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ANTITHEFTALLOW",
    t3."BTSID"
FROM
huawei_gexport_gsm."BTSTHEFTALM_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ANTITHEFTALLOW",
    t4."BTSID"
FROM
huawei_mml_gsm."BTSTHEFTALM" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSTMA = ReplaceableObject(
    'huawei_cm_2g."BTSTMA"',
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
    t1."BTSID",
    t1."CTRLPORTCN",
    t1."CTRLPORTSN",
    t1."CTRLPORTSRN",
    t1."DEVICENAME",
    t1."DEVICENO",
    t1."PWRSUPPLYTYPE",
    t1."SUBUNITNUM",
    t1."SERIALNO",
    t1."VENDORCODE"
FROM
huawei_nbi_gsm."BTSTMA" t1

"""
)

BTSTMADEVICEDATA = ReplaceableObject(
    'huawei_cm_2g."BTSTMADEVICEDATA"',
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
    t1."BAND1",
    t1."BAND2",
    t1."BAND3",
    t1."BAND4",
    t1."BEARING",
    t1."BTSID",
    t1."DEVICENO",
    t1."GAINRESOLUTION",
    t1."RXMAXFQ",
    t1."RXMINFQ",
    t1."SUBUNITNO",
    t1."SUBUNITTYPE",
    t1."TILT",
    t1."TXMAXFQ",
    t1."TXMINFQ"
FROM
huawei_nbi_gsm."BTSTMADEVICEDATA" t1

"""
)

BTSTMASUBUNIT = ReplaceableObject(
    'huawei_cm_2g."BTSTMASUBUNIT"',
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
    t1."BTSID",
    t1."CMEMODE",
    t1."CONNCN",
    t1."CONNPN",
    t1."CONNSN",
    t1."CONNSRN",
    t1."DEVICENO",
    t1."GAIN",
    t1."SUBUNITNO"
FROM
huawei_nbi_gsm."BTSTMASUBUNIT" t1

"""
)

BTSTRANS = ReplaceableObject(
    'huawei_cm_2g."BTSTRANS"',
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
    t1."BTSID",
    t1."TRANSMODE"
FROM
huawei_nbi_gsm."BTSTRANS" t1

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
    t2."BTSID",
    t2."TRANSMODE"
FROM
huawei_gexport_gsm."BTSTRANS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."TRANSMODE"
FROM
huawei_gexport_gsm."BTSTRANS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."TRANSMODE"
FROM
huawei_mml_gsm."BTSTRANS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSTRCMPR = ReplaceableObject(
    'huawei_cm_2g."BTSTRCMPR"',
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
    t1."BTSID",
    t1."BTSTRCMPRATE"
FROM
huawei_nbi_gsm."BTSTRCMPR" t1

"""
)

BTSTRUSTCERT = ReplaceableObject(
    'huawei_cm_2g."BTSTRUSTCERT"',
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
    t1."BTSID",
    t1."CERTNAME"
FROM
huawei_nbi_gsm."BTSTRUSTCERT" t1

"""
)

BTSTRXBACKUP = ReplaceableObject(
    'huawei_cm_2g."BTSTRXBACKUP"',
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
    t1."BTSID",
    t1."TRXBPSW"
FROM
huawei_nbi_gsm."BTSTRXBACKUP" t1

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
    t2."BTSID",
    t2."TRXBPSW"
FROM
huawei_gexport_gsm."BTSTRXBACKUP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."TRXBPSW"
FROM
huawei_gexport_gsm."BTSTRXBACKUP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."TRXBPSW"
FROM
huawei_mml_gsm."BTSTRXBACKUP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSVLAN = ReplaceableObject(
    'huawei_cm_2g."BTSVLAN"',
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
    t1."BTSID",
    t1."DSCP",
    t1."SERVICETYPE",
    t1."VLANID",
    t1."VLANPRI",
    t1."VLANSWITCH"
FROM
huawei_nbi_gsm."BTSVLAN" t1

"""
)

BTSXFC = ReplaceableObject(
    'huawei_cm_2g."BTSXFC"',
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
    t1."ABISSIGCTRLSWITCH",
    t1."ABISSIGTYPE",
    t1."BTSID",
    t1."BTSSIGCTRLHIGHTHRESHOLD",
    t1."BTSSIGCTRLSTARTTHRESHOLD"
FROM
huawei_nbi_gsm."BTSXFC" t1

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
    t2."ABISSIGCTRLSWITCH",
    t2."ABISSIGTYPE",
    t2."BTSID",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSXFC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISSIGCTRLSWITCH",
    t3."ABISSIGTYPE",
    t3."BTSID",
    NULL,
    NULL
FROM
huawei_gexport_gsm."BTSXFC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISSIGCTRLSWITCH",
    t4."ABISSIGTYPE",
    t4."BTSID",
    t4."BTSSIGCTRLHIGHTHRESHOLD",
    t4."BTSSIGCTRLSTARTTHRESHOLD"
FROM
huawei_mml_gsm."BTSXFC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

BTSXMUFP = ReplaceableObject(
    'huawei_cm_2g."BTSXMUFP"',
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
    t1."BTSID",
    t1."TRXPWRADJALLOW"
FROM
huawei_nbi_gsm."BTSXMUFP" t1

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
    t2."BTSID",
    t2."TRXPWRADJALLOW"
FROM
huawei_gexport_gsm."BTSXMUFP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."TRXPWRADJALLOW"
FROM
huawei_gexport_gsm."BTSXMUFP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."TRXPWRADJALLOW"
FROM
huawei_mml_gsm."BTSXMUFP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CAB = ReplaceableObject(
    'huawei_cm_2g."CAB"',
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
    t1."CABT",
    t1."CN",
    t1."PWRMODE"
FROM
huawei_nbi_gsm."CAB" t1

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
    t2."CABT",
    t2."CN",
    t2."PWRMODE"
FROM
huawei_gexport_gsm."CAB_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CABT",
    t3."CN",
    t3."PWRMODE"
FROM
huawei_gexport_gsm."CAB_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CABT",
    t4."CN",
    t4."PWRMODE"
FROM
huawei_mml_gsm."CAB" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."CN",
    t5."PWRMODE"
FROM
huawei_mml_gsm."CAB_MOD" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

CCGN = ReplaceableObject(
    'huawei_cm_2g."CCGN"',
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
    t1."CG"
FROM
huawei_nbi_gsm."CCGN" t1

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
    t2."CG"
FROM
huawei_gexport_gsm."CCGN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CG"
FROM
huawei_gexport_gsm."CCGN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CG"
FROM
huawei_mml_gsm."CCGN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CELLBIND2BTS = ReplaceableObject(
    'huawei_cm_2g."CELLBIND2BTS"',
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
    t1."BTSID",
    t1."CELLID"
FROM
huawei_nbi_gsm."CELLBIND2BTS" t1

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
    t2."BTSID",
    t2."CELLID"
FROM
huawei_gexport_gsm."CELLBIND2BTS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CELLID"
FROM
huawei_gexport_gsm."CELLBIND2BTS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CELLID"
FROM
huawei_mml_gsm."CELLBIND2BTS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CELLGLDSS = ReplaceableObject(
    'huawei_cm_2g."CELLGLDSS"',
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
    t1."GLDSSSW"
FROM
huawei_nbi_gsm."CELLGLDSS" t1

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
    t2."GLDSSSW"
FROM
huawei_gexport_gsm."CELLGLDSS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."GLDSSSW"
FROM
huawei_gexport_gsm."CELLGLDSS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GLDSSSW"
FROM
huawei_mml_gsm."CELLGLDSS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CERTCHKTSK = ReplaceableObject(
    'huawei_cm_2g."CERTCHKTSK"',
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
    t1."ALMRNG",
    t1."ISENABLE",
    t1."PERIOD",
    t1."UPDATEMETHOD"
FROM
huawei_nbi_gsm."CERTCHKTSK" t1

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
    t2."ALMRNG",
    t2."ISENABLE",
    t2."PERIOD",
    t2."UPDATEMETHOD"
FROM
huawei_gexport_gsm."CERTCHKTSK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALMRNG",
    t3."ISENABLE",
    t3."PERIOD",
    t3."UPDATEMETHOD"
FROM
huawei_gexport_gsm."CERTCHKTSK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALMRNG",
    t4."ISENABLE",
    t4."PERIOD",
    t4."UPDATEMETHOD"
FROM
huawei_mml_gsm."CERTCHKTSK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CERTMK = ReplaceableObject(
    'huawei_cm_2g."CERTMK"',
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
    t1."APPCERT"
FROM
huawei_nbi_gsm."CERTMK" t1

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
    t2."APPCERT"
FROM
huawei_gexport_gsm."CERTMK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."APPCERT"
FROM
huawei_gexport_gsm."CERTMK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

CERTREQ = ReplaceableObject(
    'huawei_cm_2g."CERTREQ"',
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
    t1."COMMNAME",
    t1."KEYSIZE",
    t1."KEYUSAGE",
    t1."LOCALIP",
    t1."LOCALNAME",
    t1."SIGNALG",
    t1."USERADDINFO"
FROM
huawei_nbi_gsm."CERTREQ" t1

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
    t2."COMMNAME",
    t2."KEYSIZE",
    NULL,
    t2."LOCALIP",
    t2."LOCALNAME",
    t2."SIGNALG",
    t2."USERADDINFO"
FROM
huawei_gexport_gsm."CERTREQ_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."COMMNAME",
    t3."KEYSIZE",
    NULL,
    t3."LOCALIP",
    t3."LOCALNAME",
    t3."SIGNALG",
    t3."USERADDINFO"
FROM
huawei_gexport_gsm."CERTREQ_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."COMMNAME",
    t4."KEYSIZE",
    NULL,
    t4."LOCALIP",
    t4."LOCALNAME",
    t4."SIGNALG",
    t4."USERADDINFO"
FROM
huawei_mml_gsm."CERTREQ_MOD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CLK = ReplaceableObject(
    'huawei_cm_2g."CLK"',
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
    t1."BACK8KCLKSW1",
    t1."BACK8KCLKSW2",
    t1."BT",
    t1."REF2MCLKSRC",
    t1."REF2MCLKSRCBAK",
    t1."REFUSELOCALCLK",
    t1."SN",
    t1."SRN",
    t1."SRT",
    t1."SUPPORTBAKCLKSRC"
FROM
huawei_nbi_gsm."CLK" t1

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
    t2."BACK8KCLKSW1",
    t2."BACK8KCLKSW2",
    t2."BT",
    t2."REF2MCLKSRC",
    NULL,
    NULL,
    t2."SN",
    t2."SRN",
    t2."SRT",
    NULL
FROM
huawei_gexport_gsm."CLK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BACK8KCLKSW1",
    t3."BACK8KCLKSW2",
    t3."BT",
    t3."REF2MCLKSRC",
    NULL,
    NULL,
    t3."SN",
    t3."SRN",
    t3."SRT",
    NULL
FROM
huawei_gexport_gsm."CLK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BACK8KCLKSW1",
    t4."BACK8KCLKSW2",
    t4."BT",
    t4."REF2MCLKSRC",
    NULL,
    NULL,
    t4."SN",
    t4."SRN",
    t4."SRT",
    NULL
FROM
huawei_mml_gsm."CLK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CLKMODE = ReplaceableObject(
    'huawei_cm_2g."CLKMODE"',
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
    t1."CMEMODE"
FROM
huawei_nbi_gsm."CLKMODE" t1

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
huawei_gexport_gsm."CLKMODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."CLKMODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."CLKMODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CLKSRC = ReplaceableObject(
    'huawei_cm_2g."CLKSRC"',
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
    t1."SRCGRD",
    t1."SRCT"
FROM
huawei_nbi_gsm."CLKSRC" t1

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
    t2."SRCGRD",
    t2."SRCT"
FROM
huawei_gexport_gsm."CLKSRC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SRCGRD",
    t3."SRCT"
FROM
huawei_gexport_gsm."CLKSRC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SRCGRD",
    t4."SRCT"
FROM
huawei_mml_gsm."CLKSRC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CONNTYPE = ReplaceableObject(
    'huawei_cm_2g."CONNTYPE"',
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
    t1."CONNTYPE"
FROM
huawei_nbi_gsm."CONNTYPE" t1

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
    t2."CONNTYPE"
FROM
huawei_gexport_gsm."CONNTYPE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CONNTYPE"
FROM
huawei_gexport_gsm."CONNTYPE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CONNTYPE"
FROM
huawei_mml_gsm."CONNTYPE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

COPTLNK = ReplaceableObject(
    'huawei_cm_2g."COPTLNK"',
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
    t1."E1T1PN",
    t1."J2MODE",
    t1."JAUTOADD",
    t1."PN",
    t1."PS",
    t1."SN",
    t1."SRN",
    t1."J2BYTE_FORMAT",
    t1."J2RXVALUE",
    t1."J2TXVALUE"
FROM
huawei_nbi_gsm."COPTLNK" t1

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
    t2."E1T1PN",
    t2."J2MODE",
    t2."JAUTOADD",
    NULL,
    t2."PS",
    t2."SN",
    t2."SRN",
    t2."J2BYTE_FORMAT",
    t2."J2RXVALUE",
    t2."J2TXVALUE"
FROM
huawei_gexport_gsm."COPTLNK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."E1T1PN",
    t3."J2MODE",
    t3."JAUTOADD",
    NULL,
    t3."PS",
    t3."SN",
    t3."SRN",
    t3."J2BYTE_FORMAT",
    t3."J2RXVALUE",
    t3."J2TXVALUE"
FROM
huawei_gexport_gsm."COPTLNK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."E1T1PN",
    t4."J2MODE",
    t4."JAUTOADD",
    NULL,
    t4."PS",
    t4."SN",
    t4."SRN",
    t4."J2BYTE_FORMAT",
    t4."J2RXVALUE",
    t4."J2TXVALUE"
FROM
huawei_mml_gsm."COPTLNK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CPUTHD = ReplaceableObject(
    'huawei_cm_2g."CPUTHD"',
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
    t1."BRDCLASS",
    t1."SSCPUAVEUSAGEALMTHD",
    t1."SSCPUMAXUSAGEALMTHD",
    t1."SSDSPAVEUSAGEALMTHD",
    t1."SSDSPMAXUSAGEALMTHD",
    t1."SSTHRUPUTAVEUSAGEALMTHD",
    t1."SSTHRUPUTMAXUSAGEALMTHD"
FROM
huawei_nbi_gsm."CPUTHD" t1

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
    t2."BRDCLASS",
    t2."SSCPUAVEUSAGEALMTHD",
    t2."SSCPUMAXUSAGEALMTHD",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."CPUTHD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BRDCLASS",
    t3."SSCPUAVEUSAGEALMTHD",
    t3."SSCPUMAXUSAGEALMTHD",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."CPUTHD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BRDCLASS",
    t4."SSCPUAVEUSAGEALMTHD",
    t4."SSCPUMAXUSAGEALMTHD",
    t4."SSDSPAVEUSAGEALMTHD",
    t4."SSDSPMAXUSAGEALMTHD",
    t4."SSTHRUPUTAVEUSAGEALMTHD",
    t4."SSTHRUPUTMAXUSAGEALMTHD"
FROM
huawei_mml_gsm."CPUTHD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CRLPOLICY = ReplaceableObject(
    'huawei_cm_2g."CRLPOLICY"',
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
    t1."CRLPOLICY"
FROM
huawei_nbi_gsm."CRLPOLICY" t1

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
    t2."CRLPOLICY"
FROM
huawei_gexport_gsm."CRLPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CRLPOLICY"
FROM
huawei_gexport_gsm."CRLPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CRLPOLICY"
FROM
huawei_mml_gsm."CRLPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

CSPRECTRL = ReplaceableObject(
    'huawei_cm_2g."CSPRECTRL"',
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
    t1."UCCSPREFCALLREESTPRIO",
    t1."UCCSPREFCSEMERGCALLPRIO",
    t1."UCCSPREFCSORGCALLPRIO",
    t1."UCCSPREFCSTERMCALLPRIO",
    t1."UCCSPREFINBSCHOPRIO",
    t1."UCCSPREFINTRABSCHOPRIO",
    t1."UCCSPREFOTHERPRIO",
    t1."UCCSPREFPSPRIO",
    t1."UCCSPREFSUPPLEPRIO",
    t1."UCCSPREFVBSPRIO",
    t1."UCCSPREFVGCSPRIO"
FROM
huawei_nbi_gsm."CSPRECTRL" t1

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
    t2."UCCSPREFCALLREESTPRIO",
    t2."UCCSPREFCSEMERGCALLPRIO",
    t2."UCCSPREFCSORGCALLPRIO",
    t2."UCCSPREFCSTERMCALLPRIO",
    t2."UCCSPREFINBSCHOPRIO",
    t2."UCCSPREFINTRABSCHOPRIO",
    t2."UCCSPREFOTHERPRIO",
    t2."UCCSPREFPSPRIO",
    t2."UCCSPREFSUPPLEPRIO",
    t2."UCCSPREFVBSPRIO",
    t2."UCCSPREFVGCSPRIO"
FROM
huawei_gexport_gsm."CSPRECTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."UCCSPREFCALLREESTPRIO",
    t3."UCCSPREFCSEMERGCALLPRIO",
    t3."UCCSPREFCSORGCALLPRIO",
    t3."UCCSPREFCSTERMCALLPRIO",
    t3."UCCSPREFINBSCHOPRIO",
    t3."UCCSPREFINTRABSCHOPRIO",
    t3."UCCSPREFOTHERPRIO",
    t3."UCCSPREFPSPRIO",
    t3."UCCSPREFSUPPLEPRIO",
    t3."UCCSPREFVBSPRIO",
    t3."UCCSPREFVGCSPRIO"
FROM
huawei_gexport_gsm."CSPRECTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

DEVIP = ReplaceableObject(
    'huawei_cm_2g."DEVIP"',
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
    t1."REMARK",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."DEVIP" t1

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
    t2."REMARK",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."DEVIP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."REMARK",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."DEVIP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."REMARK",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."DEVIP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

DEVRSVDPARA = ReplaceableObject(
    'huawei_cm_2g."DEVRSVDPARA"',
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
    t1."RSVDPARA1",
    t1."RSVDPARA10",
    t1."RSVDPARA11",
    t1."RSVDPARA12",
    t1."RSVDPARA13",
    t1."RSVDPARA14",
    t1."RSVDPARA15",
    t1."RSVDPARA16",
    t1."RSVDPARA17",
    t1."RSVDPARA18",
    t1."RSVDPARA19",
    t1."RSVDPARA2",
    t1."RSVDPARA20",
    t1."RSVDPARA21",
    t1."RSVDPARA22",
    t1."RSVDPARA23",
    t1."RSVDPARA24",
    t1."RSVDPARA25",
    t1."RSVDPARA26",
    t1."RSVDPARA27",
    t1."RSVDPARA28",
    t1."RSVDPARA29",
    t1."RSVDPARA3",
    t1."RSVDPARA30",
    t1."RSVDPARA31",
    t1."RSVDPARA32",
    t1."RSVDPARA33",
    t1."RSVDPARA34",
    t1."RSVDPARA35",
    t1."RSVDPARA36",
    t1."RSVDPARA37",
    t1."RSVDPARA38",
    t1."RSVDPARA39",
    t1."RSVDPARA4",
    t1."RSVDPARA40",
    t1."RSVDPARA5",
    t1."RSVDPARA6",
    t1."RSVDPARA7",
    t1."RSVDPARA8",
    t1."RSVDPARA9",
    t1."RSVDSW1",
    t1."RSVDSW2",
    t1."RSVDSW3",
    t1."RSVDSW4",
    t1."RSVDSW5",
    t1."RSVDSW6",
    t1."RSVDSW7",
    t1."RSVDSW8"
FROM
huawei_nbi_gsm."DEVRSVDPARA" t1

"""
)

DSCPMAP = ReplaceableObject(
    'huawei_cm_2g."DSCPMAP"',
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
    t1."VLANPRI"
FROM
huawei_nbi_gsm."DSCPMAP" t1

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
    t2."VLANPRI"
FROM
huawei_gexport_gsm."DSCPMAP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."VLANPRI"
FROM
huawei_gexport_gsm."DSCPMAP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."VLANPRI"
FROM
huawei_mml_gsm."DSCPMAP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

DSP = ReplaceableObject(
    'huawei_cm_2g."DSP"',
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
    t1."DSPN",
    t1."SN",
    t1."SRN",
    t1."TCTYPE",
    t1."TIMELEN"
FROM
huawei_nbi_gsm."DSP" t1

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
    t2."DSPN",
    t2."SN",
    t2."SRN",
    t2."TCTYPE",
    t2."TIMELEN"
FROM
huawei_gexport_gsm."DSP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DSPN",
    t3."SN",
    t3."SRN",
    t3."TCTYPE",
    t3."TIMELEN"
FROM
huawei_gexport_gsm."DSP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DSPN",
    t4."SN",
    t4."SRN",
    NULL,
    NULL
FROM
huawei_mml_gsm."DSP_UIN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

DSPLVDSMODE = ReplaceableObject(
    'huawei_cm_2g."DSPLVDSMODE"',
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
    t1."LVDS252DSPNUM",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."DSPLVDSMODE" t1

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
    t2."LVDS252DSPNUM",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."DSPLVDSMODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LVDS252DSPNUM",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."DSPLVDSMODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LVDS252DSPNUM",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."DSPLVDSMODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

DXX = ReplaceableObject(
    'huawei_cm_2g."DXX"',
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
    t1."DXXINDEX",
    t1."PORTNUM"
FROM
huawei_nbi_gsm."DXX" t1

"""
)

DXXCONNECT = ReplaceableObject(
    'huawei_cm_2g."DXXCONNECT"',
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
    t1."CIUSLOTNO",
    t1."CIUSUBRACKNO",
    t1."CONNECTPORTNO",
    t1."DXXINDEX",
    t1."PORTNO"
FROM
huawei_nbi_gsm."DXXCONNECT" t1

"""
)

DXXTSEXGRELATION = ReplaceableObject(
    'huawei_cm_2g."DXXTSEXGRELATION"',
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
    t1."DXXINDEX",
    t1."INPORTNO",
    t1."INTSNO",
    t1."OUTPORTNO",
    t1."OUTPORTTS"
FROM
huawei_nbi_gsm."DXXTSEXGRELATION" t1

"""
)

E1T1 = ReplaceableObject(
    'huawei_cm_2g."E1T1"',
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
    t1."BERAUTOISOSW",
    t1."BT",
    t1."LOOPSW",
    t1."PN",
    t1."PS",
    t1."PTRXT",
    t1."PTTXT",
    t1."REMARK",
    t1."SN",
    t1."SRN",
    t1."WORKMODE"
FROM
huawei_nbi_gsm."E1T1" t1

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
    t2."BERAUTOISOSW",
    t2."BT",
    t2."LOOPSW",
    t2."PN",
    t2."PS",
    t2."PTRXT",
    t2."PTTXT",
    t2."REMARK",
    t2."SN",
    t2."SRN",
    t2."WORKMODE"
FROM
huawei_gexport_gsm."E1T1_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BERAUTOISOSW",
    t3."BT",
    t3."LOOPSW",
    t3."PN",
    t3."PS",
    t3."PTRXT",
    t3."PTTXT",
    t3."REMARK",
    t3."SN",
    t3."SRN",
    t3."WORKMODE"
FROM
huawei_gexport_gsm."E1T1_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BERAUTOISOSW",
    t4."BT",
    t4."LOOPSW",
    t4."PN",
    t4."PS",
    t4."PTRXT",
    t4."PTTXT",
    t4."REMARK",
    t4."SN",
    t4."SRN",
    t4."WORKMODE"
FROM
huawei_mml_gsm."E1T1" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

EMSIP = ReplaceableObject(
    'huawei_cm_2g."EMSIP"',
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
huawei_nbi_gsm."EMSIP" t1

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
huawei_gexport_gsm."EMSIP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."EMSIP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."EMSIP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ENVALMPARA = ReplaceableObject(
    'huawei_cm_2g."ENVALMPARA"',
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
    t1."AID",
    t1."ALVL",
    t1."ANM",
    t1."ASS"
FROM
huawei_nbi_gsm."ENVALMPARA" t1

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
    t2."AID",
    t2."ALVL",
    t2."ANM",
    t2."ASS"
FROM
huawei_gexport_gsm."ENVALMPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    t3."ALVL",
    t3."ANM",
    t3."ASS"
FROM
huawei_gexport_gsm."ENVALMPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AID",
    t4."ALVL",
    t4."ANM",
    t4."ASS"
FROM
huawei_mml_gsm."ENVALMPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ETHIP = ReplaceableObject(
    'huawei_cm_2g."ETHIP"',
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
huawei_nbi_gsm."ETHIP" t1

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
    t2."PN",
    t2."REMARK",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."ETHIP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PN",
    t3."REMARK",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."ETHIP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PN",
    t4."REMARK",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."ETHIP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ETHPORT = ReplaceableObject(
    'huawei_cm_2g."ETHPORT"',
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
    t1."ARPBCPKTVLANFLAG",
    t1."AUTO",
    t1."BCPKTALARMCLRTHD",
    t1."BCPKTALARMTHD",
    t1."BRDTYPE",
    t1."CFMVER",
    t1."ERRDETECTSW",
    t1."FCINDEX",
    t1."FLOWCTRLSWITCH",
    t1."MTU",
    t1."OAMFLOWBW",
    t1."PN",
    t1."REMARK",
    t1."SN",
    t1."SRN",
    t1."TRMLOADTHINDEX",
    t1."FC",
    t1."PTYPE"
FROM
huawei_nbi_gsm."ETHPORT" t1

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
    t2."ARPBCPKTVLANFLAG",
    t2."AUTO",
    t2."BCPKTALARMCLRTHD",
    t2."BCPKTALARMTHD",
    t2."BRDTYPE",
    t2."CFMVER",
    t2."ERRDETECTSW",
    t2."FCINDEX",
    t2."FLOWCTRLSWITCH",
    t2."MTU",
    t2."OAMFLOWBW",
    t2."PN",
    t2."REMARK",
    t2."SN",
    t2."SRN",
    t2."TRMLOADTHINDEX",
    NULL,
    t2."PTYPE"
FROM
huawei_gexport_gsm."ETHPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ARPBCPKTVLANFLAG",
    t3."AUTO",
    t3."BCPKTALARMCLRTHD",
    t3."BCPKTALARMTHD",
    t3."BRDTYPE",
    t3."CFMVER",
    t3."ERRDETECTSW",
    t3."FCINDEX",
    t3."FLOWCTRLSWITCH",
    t3."MTU",
    t3."OAMFLOWBW",
    t3."PN",
    t3."REMARK",
    t3."SN",
    t3."SRN",
    t3."TRMLOADTHINDEX",
    NULL,
    t3."PTYPE"
FROM
huawei_gexport_gsm."ETHPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ARPBCPKTVLANFLAG",
    t4."AUTO",
    t4."BCPKTALARMCLRTHD",
    t4."BCPKTALARMTHD",
    t4."BRDTYPE",
    t4."CFMVER",
    t4."ERRDETECTSW",
    t4."FCINDEX",
    t4."FLOWCTRLSWITCH",
    t4."MTU",
    t4."OAMFLOWBW",
    t4."PN",
    t4."REMARK",
    t4."SN",
    t4."SRN",
    t4."TRMLOADTHINDEX",
    t4."FC",
    t4."PTYPE"
FROM
huawei_mml_gsm."ETHPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."ETHPORT_ACT" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

ETHREDPORT = ReplaceableObject(
    'huawei_cm_2g."ETHREDPORT"',
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
    t1."PN",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."ETHREDPORT" t1

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
    t2."PN",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."ETHREDPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PN",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."ETHREDPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PN",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."ETHREDPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ETHSWITCH = ReplaceableObject(
    'huawei_cm_2g."ETHSWITCH"',
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
    t1."BFTCHKSW",
    t1."FADETECTSW",
    t1."FAPOSTSW",
    t1."FLTDIAGSW1",
    t1."FLTDIAGSW2",
    t1."FLTDIAGSW3",
    t1."FLTDIAGSW4",
    t1."FLTDIAGSW5",
    t1."ISOLATEIOSW",
    t1."ISOLATESYSSW",
    t1."MPUMMUSW",
    t1."MSDETECTSW",
    t1."RESPARA1",
    t1."RESPARA2",
    t1."RESPARA5",
    t1."RESPARA63",
    t1."RESPARA64",
    t1."RESSW2",
    t1."RESSW3",
    t1."RESSW4",
    t1."RESSW5",
    t1."RESSW6"
FROM
huawei_nbi_gsm."ETHSWITCH" t1

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
    t2."BFTCHKSW",
    t2."FADETECTSW",
    t2."FAPOSTSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."ISOLATEIOSW",
    t2."ISOLATESYSSW",
    t2."MPUMMUSW",
    t2."MSDETECTSW",
    t2."RESPARA1",
    t2."RESPARA2",
    t2."RESPARA5",
    t2."RESPARA63",
    t2."RESPARA64",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."ETHSWITCH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BFTCHKSW",
    t3."FADETECTSW",
    t3."FAPOSTSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."ISOLATEIOSW",
    t3."ISOLATESYSSW",
    t3."MPUMMUSW",
    t3."MSDETECTSW",
    t3."RESPARA1",
    t3."RESPARA2",
    t3."RESPARA5",
    t3."RESPARA63",
    t3."RESPARA64",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."ETHSWITCH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BFTCHKSW",
    t4."FADETECTSW",
    t4."FAPOSTSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t4."ISOLATEIOSW",
    t4."ISOLATESYSSW",
    t4."MPUMMUSW",
    t4."MSDETECTSW",
    t4."RESPARA1",
    t4."RESPARA2",
    t4."RESPARA5",
    t4."RESPARA63",
    t4."RESPARA64",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."ETHSWITCH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

FACFG = ReplaceableObject(
    'huawei_cm_2g."FACFG"',
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
    t1."FAMLINKUNSTABLECHKSW",
    t1."INTVAL",
    t1."LOGSW",
    t1."PERIOD",
    t1."RESSW",
    t1."XPUASINGLEPEMSW"
FROM
huawei_nbi_gsm."FACFG" t1

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
    t2."FAMLINKUNSTABLECHKSW",
    t2."INTVAL",
    t2."LOGSW",
    t2."PERIOD",
    t2."RESSW",
    t2."XPUASINGLEPEMSW"
FROM
huawei_gexport_gsm."FACFG_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FAMLINKUNSTABLECHKSW",
    t3."INTVAL",
    t3."LOGSW",
    t3."PERIOD",
    t3."RESSW",
    t3."XPUASINGLEPEMSW"
FROM
huawei_gexport_gsm."FACFG_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FAMLINKUNSTABLECHKSW",
    t4."INTVAL",
    t4."LOGSW",
    t4."PERIOD",
    t4."RESSW",
    t4."XPUASINGLEPEMSW"
FROM
huawei_mml_gsm."FACFG" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

FANSPEED = ReplaceableObject(
    'huawei_cm_2g."FANSPEED"',
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
    t1."FANFLAG",
    t1."FANSPEEDMODE",
    t1."SRN"
FROM
huawei_nbi_gsm."FANSPEED" t1

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
    t2."FANFLAG",
    t2."FANSPEEDMODE",
    t2."SRN"
FROM
huawei_gexport_gsm."FANSPEED_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FANFLAG",
    t3."FANSPEEDMODE",
    t3."SRN"
FROM
huawei_gexport_gsm."FANSPEED_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FANFLAG",
    t4."FANSPEEDMODE",
    t4."SRN"
FROM
huawei_mml_gsm."FANSPEED" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

FCCOMMPARA = ReplaceableObject(
    'huawei_cm_2g."FCCOMMPARA"',
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
    t1."BRDCLASS",
    t1."CPUCTHD",
    t1."CPULOGCTHD",
    t1."CPULOGRTHD",
    t1."CPUPMCTHD",
    t1."CPUPMRTHD",
    t1."CPUPRINTCTHD",
    t1."CPUPRINTRTHD",
    t1."CPUSMWINDOW",
    t1."CPUTRACECTHD",
    t1."CPUTRACERTHD",
    t1."FCSW",
    t1."FDWINDOW",
    t1."LOGSW",
    t1."MSGCTHD",
    t1."MSGLOGCTHD",
    t1."MSGLOGRTHD",
    t1."MSGPMCTHD",
    t1."MSGPMRTHD",
    t1."MSGPRINTCTHD",
    t1."MSGPRINTRTHD",
    t1."MSGSMWINDOW",
    t1."MSGTRACECTHD",
    t1."MSGTRACERTHD",
    t1."PMSW",
    t1."PRINTSW",
    t1."TRACESW"
FROM
huawei_nbi_gsm."FCCOMMPARA" t1

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
    t2."BRDCLASS",
    t2."CPUCTHD",
    t2."CPULOGCTHD",
    t2."CPULOGRTHD",
    t2."CPUPMCTHD",
    t2."CPUPMRTHD",
    t2."CPUPRINTCTHD",
    t2."CPUPRINTRTHD",
    t2."CPUSMWINDOW",
    t2."CPUTRACECTHD",
    t2."CPUTRACERTHD",
    t2."FCSW",
    t2."FDWINDOW",
    t2."LOGSW",
    t2."MSGCTHD",
    t2."MSGLOGCTHD",
    t2."MSGLOGRTHD",
    t2."MSGPMCTHD",
    t2."MSGPMRTHD",
    t2."MSGPRINTCTHD",
    t2."MSGPRINTRTHD",
    t2."MSGSMWINDOW",
    t2."MSGTRACECTHD",
    t2."MSGTRACERTHD",
    t2."PMSW",
    t2."PRINTSW",
    t2."TRACESW"
FROM
huawei_gexport_gsm."FCCOMMPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BRDCLASS",
    t3."CPUCTHD",
    t3."CPULOGCTHD",
    t3."CPULOGRTHD",
    t3."CPUPMCTHD",
    t3."CPUPMRTHD",
    t3."CPUPRINTCTHD",
    t3."CPUPRINTRTHD",
    t3."CPUSMWINDOW",
    t3."CPUTRACECTHD",
    t3."CPUTRACERTHD",
    t3."FCSW",
    t3."FDWINDOW",
    t3."LOGSW",
    t3."MSGCTHD",
    t3."MSGLOGCTHD",
    t3."MSGLOGRTHD",
    t3."MSGPMCTHD",
    t3."MSGPMRTHD",
    t3."MSGPRINTCTHD",
    t3."MSGPRINTRTHD",
    t3."MSGSMWINDOW",
    t3."MSGTRACECTHD",
    t3."MSGTRACERTHD",
    t3."PMSW",
    t3."PRINTSW",
    t3."TRACESW"
FROM
huawei_gexport_gsm."FCCOMMPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BRDCLASS",
    t4."CPUCTHD",
    t4."CPULOGCTHD",
    t4."CPULOGRTHD",
    t4."CPUPMCTHD",
    t4."CPUPMRTHD",
    t4."CPUPRINTCTHD",
    t4."CPUPRINTRTHD",
    t4."CPUSMWINDOW",
    t4."CPUTRACECTHD",
    t4."CPUTRACERTHD",
    t4."FCSW",
    t4."FDWINDOW",
    t4."LOGSW",
    t4."MSGCTHD",
    t4."MSGLOGCTHD",
    t4."MSGLOGRTHD",
    t4."MSGPMCTHD",
    t4."MSGPMRTHD",
    t4."MSGPRINTCTHD",
    t4."MSGPRINTRTHD",
    t4."MSGSMWINDOW",
    t4."MSGTRACECTHD",
    t4."MSGTRACERTHD",
    t4."PMSW",
    t4."PRINTSW",
    t4."TRACESW"
FROM
huawei_mml_gsm."FCCOMMPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)
#
# FILEFOOTER = ReplaceableObject(
#     'huawei_cm_2g."FILEFOOTER"',
#     """
#
# SELECT
#     t1."FileName",
#     t1."datetime"
# FROM
# huawei_nbi_gsm."FILEFOOTER" t1
#
# """
# )

FTPCLTPORT = ReplaceableObject(
    'huawei_cm_2g."FTPCLTPORT"',
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
    t1."ENDPORT",
    t1."STARTPORT"
FROM
huawei_nbi_gsm."FTPCLTPORT" t1

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
    t2."ENDPORT",
    t2."STARTPORT"
FROM
huawei_gexport_gsm."FTPCLTPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ENDPORT",
    t3."STARTPORT"
FROM
huawei_gexport_gsm."FTPCLTPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ENDPORT",
    t4."STARTPORT"
FROM
huawei_mml_gsm."FTPCLTPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

FTPSCLT = ReplaceableObject(
    'huawei_cm_2g."FTPSCLT"',
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
    t1."ENCRYMODE",
    t1."SPTSTATEFWL",
    t1."SSLCERTAUTH"
FROM
huawei_nbi_gsm."FTPSCLT" t1

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
    t2."ENCRYMODE",
    t2."SPTSTATEFWL",
    NULL
FROM
huawei_gexport_gsm."FTPSCLT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ENCRYMODE",
    t3."SPTSTATEFWL",
    NULL
FROM
huawei_gexport_gsm."FTPSCLT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ENCRYMODE",
    t4."SPTSTATEFWL",
    t4."SSLCERTAUTH"
FROM
huawei_mml_gsm."FTPSCLT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

FTPSCLTDPORT = ReplaceableObject(
    'huawei_cm_2g."FTPSCLTDPORT"',
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
    t1."PORT",
    t1."SERVERIP"
FROM
huawei_nbi_gsm."FTPSCLTDPORT" t1

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
    t2."PORT",
    t2."SERVERIP"
FROM
huawei_gexport_gsm."FTPSCLTDPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PORT",
    t3."SERVERIP"
FROM
huawei_gexport_gsm."FTPSCLTDPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PORT",
    t4."SERVERIP"
FROM
huawei_mml_gsm."FTPSCLTDPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

FTPSRVSPD = ReplaceableObject(
    'huawei_cm_2g."FTPSRVSPD"',
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
    t1."FTPSPD"
FROM
huawei_nbi_gsm."FTPSRVSPD" t1

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
    t2."FTPSPD"
FROM
huawei_gexport_gsm."FTPSRVSPD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FTPSPD"
FROM
huawei_gexport_gsm."FTPSRVSPD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FTPSPD"
FROM
huawei_mml_gsm."FTPSRVSPD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

FTPSSRV = ReplaceableObject(
    'huawei_cm_2g."FTPSSRV"',
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
    t1."ACDPORTLWLT",
    t1."ACDPORTUPLT",
    t1."DFTPORTSWT",
    t1."ENCRYMODE"
FROM
huawei_nbi_gsm."FTPSSRV" t1

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
    t2."ACDPORTLWLT",
    t2."ACDPORTUPLT",
    t2."DFTPORTSWT",
    t2."ENCRYMODE"
FROM
huawei_gexport_gsm."FTPSSRV_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACDPORTLWLT",
    t3."ACDPORTUPLT",
    t3."DFTPORTSWT",
    t3."ENCRYMODE"
FROM
huawei_gexport_gsm."FTPSSRV_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACDPORTLWLT",
    t4."ACDPORTUPLT",
    t4."DFTPORTSWT",
    t4."ENCRYMODE"
FROM
huawei_mml_gsm."FTPSSRV" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

G2GNCELL = ReplaceableObject(
    'huawei_cm_2g."G2GNCELL"',
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
    t1."ADJHOOFFSET",
    t1."BETTERCELLLASTTIME",
    t1."BETTERCELLSTATTIME",
    t1."BQLASTTIME",
    t1."BQMARGIN",
    t1."BQNCELLABSTHRESSW",
    t1."BQSTATTIME",
    t1."CHAINNCELLTYPE",
    t1."DRHOLEVRANGE",
    t1."EDGEADJLASTTIME",
    t1."EDGEADJSTATTIME",
    t1."EDGEHOHYST",
    t1."EDOUTHOOFFSET",
    t1."GNCELLRANKPRI",
    t1."HCSLASTTIME",
    t1."HCSSTATTIME",
    t1."HOLASTTIME",
    t1."HOSTATICTIME",
    t1."HSRPNUSRNCTAG",
    t1."INTELEVHOHYST",
    t1."INTERCELLHYST",
    t1."ISCHAINNCELL",
    t1."LEVLAST",
    t1."LEVSTAT",
    t1."LOADHOPBGTMARGIN",
    t1."MINOFFSET",
    t1."NBR2GNCELLID",
    t1."NCELLPRI",
    t1."NCELLPUNEN",
    t1."NCELLPUNLEV",
    t1."NCELLPUNSTPTH",
    t1."NCELLPUNTM",
    t1."NCELLPWRCOMPVALUE",
    t1."NCELLTYPE",
    t1."PBGTLAST",
    t1."PBGTMARGIN",
    t1."PBGTSTAT",
    t1."SRC2GNCELLID",
    t1."SRCHOCTRLSWITCH",
    t1."TALASTTIME",
    t1."TASTATTIME",
    t1."ULBQLASTTIME",
    t1."ULBQSTATTIME"
FROM
huawei_nbi_gsm."G2GNCELL" t1

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
    t2."ADJHOOFFSET",
    t2."BETTERCELLLASTTIME",
    t2."BETTERCELLSTATTIME",
    t2."BQLASTTIME",
    t2."BQMARGIN",
    t2."BQNCELLABSTHRESSW",
    t2."BQSTATTIME",
    t2."CHAINNCELLTYPE",
    t2."DRHOLEVRANGE",
    t2."EDGEADJLASTTIME",
    t2."EDGEADJSTATTIME",
    t2."EDGEHOHYST",
    t2."EDOUTHOOFFSET",
    t2."GNCELLRANKPRI",
    t2."HCSLASTTIME",
    t2."HCSSTATTIME",
    t2."HOLASTTIME",
    t2."HOSTATICTIME",
    t2."HSRPNUSRNCTAG",
    t2."INTELEVHOHYST",
    t2."INTERCELLHYST",
    t2."ISCHAINNCELL",
    t2."LEVLAST",
    t2."LEVSTAT",
    t2."LOADHOPBGTMARGIN",
    t2."MINOFFSET",
    t2."NBR2GNCELLID",
    t2."NCELLPRI",
    t2."NCELLPUNEN",
    t2."NCELLPUNLEV",
    t2."NCELLPUNSTPTH",
    t2."NCELLPUNTM",
    t2."NCELLPWRCOMPVALUE",
    t2."NCELLTYPE",
    t2."PBGTLAST",
    t2."PBGTMARGIN",
    t2."PBGTSTAT",
    t2."SRC2GNCELLID",
    t2."SRCHOCTRLSWITCH",
    t2."TALASTTIME",
    t2."TASTATTIME",
    t2."ULBQLASTTIME",
    t2."ULBQSTATTIME"
FROM
huawei_gexport_gsm."G2GNCELL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADJHOOFFSET",
    t3."BETTERCELLLASTTIME",
    t3."BETTERCELLSTATTIME",
    t3."BQLASTTIME",
    t3."BQMARGIN",
    t3."BQNCELLABSTHRESSW",
    t3."BQSTATTIME",
    t3."CHAINNCELLTYPE",
    t3."DRHOLEVRANGE",
    t3."EDGEADJLASTTIME",
    t3."EDGEADJSTATTIME",
    t3."EDGEHOHYST",
    t3."EDOUTHOOFFSET",
    t3."GNCELLRANKPRI",
    t3."HCSLASTTIME",
    t3."HCSSTATTIME",
    t3."HOLASTTIME",
    t3."HOSTATICTIME",
    t3."HSRPNUSRNCTAG",
    t3."INTELEVHOHYST",
    t3."INTERCELLHYST",
    t3."ISCHAINNCELL",
    t3."LEVLAST",
    t3."LEVSTAT",
    t3."LOADHOPBGTMARGIN",
    t3."MINOFFSET",
    t3."NBR2GNCELLID",
    t3."NCELLPRI",
    t3."NCELLPUNEN",
    t3."NCELLPUNLEV",
    t3."NCELLPUNSTPTH",
    t3."NCELLPUNTM",
    t3."NCELLPWRCOMPVALUE",
    t3."NCELLTYPE",
    t3."PBGTLAST",
    t3."PBGTMARGIN",
    t3."PBGTSTAT",
    t3."SRC2GNCELLID",
    t3."SRCHOCTRLSWITCH",
    t3."TALASTTIME",
    t3."TASTATTIME",
    t3."ULBQLASTTIME",
    t3."ULBQSTATTIME"
FROM
huawei_gexport_gsm."G2GNCELL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADJHOOFFSET",
    t4."BETTERCELLLASTTIME",
    t4."BETTERCELLSTATTIME",
    t4."BQLASTTIME",
    t4."BQMARGIN",
    t4."BQNCELLABSTHRESSW",
    t4."BQSTATTIME",
    t4."CHAINNCELLTYPE",
    t4."DRHOLEVRANGE",
    t4."EDGEADJLASTTIME",
    t4."EDGEADJSTATTIME",
    t4."EDGEHOHYST",
    t4."EDOUTHOOFFSET",
    t4."GNCELLRANKPRI",
    t4."HCSLASTTIME",
    t4."HCSSTATTIME",
    t4."HOLASTTIME",
    t4."HOSTATICTIME",
    t4."HSRPNUSRNCTAG",
    t4."INTELEVHOHYST",
    t4."INTERCELLHYST",
    t4."ISCHAINNCELL",
    t4."LEVLAST",
    t4."LEVSTAT",
    t4."LOADHOPBGTMARGIN",
    t4."MINOFFSET",
    t4."NBR2GNCELLID",
    t4."NCELLPRI",
    t4."NCELLPUNEN",
    t4."NCELLPUNLEV",
    t4."NCELLPUNSTPTH",
    t4."NCELLPUNTM",
    t4."NCELLPWRCOMPVALUE",
    t4."NCELLTYPE",
    t4."PBGTLAST",
    t4."PBGTMARGIN",
    t4."PBGTSTAT",
    t4."SRC2GNCELLID",
    t4."SRCHOCTRLSWITCH",
    t4."TALASTTIME",
    t4."TASTATTIME",
    t4."ULBQLASTTIME",
    t4."ULBQSTATTIME"
FROM
huawei_mml_gsm."G2GNCELL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

G3GARFCN = ReplaceableObject(
    'huawei_cm_2g."G3GARFCN"',
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
    t1."INPUT3GARFCNEN"
FROM
huawei_nbi_gsm."G3GARFCN" t1

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
    t2."INPUT3GARFCNEN"
FROM
huawei_gexport_gsm."G3GARFCN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."INPUT3GARFCNEN"
FROM
huawei_gexport_gsm."G3GARFCN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."INPUT3GARFCNEN"
FROM
huawei_mml_gsm."G3GARFCN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

G3GNCELL = ReplaceableObject(
    'huawei_cm_2g."G3GNCELL"',
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
    t1."ECNOOFF",
    t1."HODURT3G",
    t1."HODURT3GTDD",
    t1."HOSTAT3G",
    t1."HOSTAT3GTDD",
    t1."NBR3GNCELLID",
    t1."NCELLPRI",
    t1."RSCPOFF",
    t1."SRC3GNCELLID"
FROM
huawei_nbi_gsm."G3GNCELL" t1

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
    t2."ECNOOFF",
    t2."HODURT3G",
    t2."HODURT3GTDD",
    t2."HOSTAT3G",
    t2."HOSTAT3GTDD",
    t2."NBR3GNCELLID",
    t2."NCELLPRI",
    t2."RSCPOFF",
    t2."SRC3GNCELLID"
FROM
huawei_gexport_gsm."G3GNCELL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ECNOOFF",
    t3."HODURT3G",
    t3."HODURT3GTDD",
    t3."HOSTAT3G",
    t3."HOSTAT3GTDD",
    t3."NBR3GNCELLID",
    t3."NCELLPRI",
    t3."RSCPOFF",
    t3."SRC3GNCELLID"
FROM
huawei_gexport_gsm."G3GNCELL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ECNOOFF",
    t4."HODURT3G",
    t4."HODURT3GTDD",
    t4."HOSTAT3G",
    t4."HOSTAT3GTDD",
    t4."NBR3GNCELLID",
    t4."NCELLPRI",
    t4."RSCPOFF",
    t4."SRC3GNCELLID"
FROM
huawei_mml_gsm."G3GNCELL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

G_ADJMAP = ReplaceableObject(
    'huawei_cm_2g."G_ADJMAP"',
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
    t1."TMIGLD"
FROM
huawei_nbi_gsm."G_ADJMAP" t1

"""
)

G_ADJNODE = ReplaceableObject(
    'huawei_cm_2g."G_ADJNODE"',
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
    t1."ISIPPOOL",
    t1."NAME",
    t1."NODET",
    t1."BTSID"
FROM
huawei_nbi_gsm."G_ADJNODE" t1

"""
)

GAFCALMPARA = ReplaceableObject(
    'huawei_cm_2g."GAFCALMPARA"',
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
    t1."AFCALARMCHECKTIME",
    t1."AFCALARMCLEARTHLD",
    t1."AFCALARMREPORTTHLD",
    t1."AFCALARMSW",
    t1."MINCRATMPTPERUNITTIME"
FROM
huawei_nbi_gsm."GAFCALMPARA" t1

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
    t2."AFCALARMCHECKTIME",
    t2."AFCALARMCLEARTHLD",
    t2."AFCALARMREPORTTHLD",
    t2."AFCALARMSW",
    t2."MINCRATMPTPERUNITTIME"
FROM
huawei_gexport_gsm."GAFCALMPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AFCALARMCHECKTIME",
    t3."AFCALARMCLEARTHLD",
    t3."AFCALARMREPORTTHLD",
    t3."AFCALARMSW",
    t3."MINCRATMPTPERUNITTIME"
FROM
huawei_gexport_gsm."GAFCALMPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AFCALARMCHECKTIME",
    t4."AFCALARMCLEARTHLD",
    t4."AFCALARMREPORTTHLD",
    t4."AFCALARMSW",
    t4."MINCRATMPTPERUNITTIME"
FROM
huawei_mml_gsm."GAFCALMPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GALLCELLBLKSTAT = ReplaceableObject(
    'huawei_cm_2g."GALLCELLBLKSTAT"',
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
    t1."ADMSTATOPTYPE",
    t1."STATOPTINTERVAL"
FROM
huawei_nbi_gsm."GALLCELLBLKSTAT" t1

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
    t2."ADMSTATOPTYPE",
    t2."STATOPTINTERVAL"
FROM
huawei_gexport_gsm."GALLCELLBLKSTAT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADMSTATOPTYPE",
    t3."STATOPTINTERVAL"
FROM
huawei_gexport_gsm."GALLCELLBLKSTAT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADMSTATOPTYPE",
    t4."STATOPTINTERVAL"
FROM
huawei_mml_gsm."GALLCELLBLKSTAT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GBSCREDGRP = ReplaceableObject(
    'huawei_cm_2g."GBSCREDGRP"',
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
    t1."BEATSENDINGDIS",
    t1."GROUPINDEX",
    t1."GROUPNAME",
    t1."LOCALBSCID",
    t1."PEERBSCID"
FROM
huawei_nbi_gsm."GBSCREDGRP" t1

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
    t2."BEATSENDINGDIS",
    t2."GROUPINDEX",
    t2."GROUPNAME",
    t2."LOCALBSCID",
    t2."PEERBSCID"
FROM
huawei_gexport_gsm."GBSCREDGRP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BEATSENDINGDIS",
    t3."GROUPINDEX",
    t3."GROUPNAME",
    t3."LOCALBSCID",
    t3."PEERBSCID"
FROM
huawei_gexport_gsm."GBSCREDGRP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BEATSENDINGDIS",
    t4."GROUPINDEX",
    t4."GROUPNAME",
    t4."LOCALBSCID",
    t4."PEERBSCID"
FROM
huawei_mml_gsm."GBSCREDGRP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."GROUPINDEX",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GBSCREDGRP_DEA" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

GCELL = ReplaceableObject(
    'huawei_cm_2g."GCELL"',
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
    t1."ADMSTAT",
    t1."BCC",
    t1."BSPAGBLKSRES",
    t1."BSPBCCHBLKS",
    t1."BSPRACHBLKS",
    t1."CELLID",
    t1."CELLNAME",
    t1."CI",
    t1."CSDSP",
    t1."CSVSP",
    t1."EXTTP",
    t1."FLEXMAIO",
    t1."GLOCELLID",
    t1."HYBHIFREQBANDSUPPORT",
    t1."IUOTP",
    t1."LAC",
    t1."MCC",
    t1."MNC",
    t1."MOCNCMCELL",
    t1."NCC",
    t1."OPNAME",
    t1."PSHPSP",
    t1."PSLPSVP",
    t1."REMARK",
    t1."TYPE",
    t1."VIPCELL",
    t1."DBFREQBCCHIUO",
    t1."ENIUO"
FROM
huawei_nbi_gsm."GCELL" t1

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
    t2."ADMSTAT",
    t2."BCC",
    t2."BSPAGBLKSRES",
    t2."BSPBCCHBLKS",
    t2."BSPRACHBLKS",
    t2."CELLID",
    t2."CELLNAME",
    t2."CI",
    t2."CSDSP",
    t2."CSVSP",
    t2."EXTTP",
    t2."FLEXMAIO",
    t2."GLOCELLID",
    t2."HYBHIFREQBANDSUPPORT",
    t2."IUOTP",
    t2."LAC",
    t2."MCC",
    t2."MNC",
    t2."MOCNCMCELL",
    t2."NCC",
    t2."OPNAME",
    t2."PSHPSP",
    t2."PSLPSVP",
    t2."REMARK",
    t2."TYPE",
    t2."VIPCELL",
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADMSTAT",
    t3."BCC",
    t3."BSPAGBLKSRES",
    t3."BSPBCCHBLKS",
    t3."BSPRACHBLKS",
    t3."CELLID",
    t3."CELLNAME",
    t3."CI",
    t3."CSDSP",
    t3."CSVSP",
    t3."EXTTP",
    t3."FLEXMAIO",
    t3."GLOCELLID",
    t3."HYBHIFREQBANDSUPPORT",
    t3."IUOTP",
    t3."LAC",
    t3."MCC",
    t3."MNC",
    t3."MOCNCMCELL",
    t3."NCC",
    t3."OPNAME",
    t3."PSHPSP",
    t3."PSLPSVP",
    t3."REMARK",
    t3."TYPE",
    t3."VIPCELL",
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BCC",
    t4."BSPAGBLKSRES",
    t4."BSPBCCHBLKS",
    t4."BSPRACHBLKS",
    t4."CELLID",
    t4."CELLNAME",
    t4."CI",
    t4."CSDSP",
    t4."CSVSP",
    t4."EXTTP",
    t4."FLEXMAIO",
    t4."GLOCELLID",
    t4."HYBHIFREQBANDSUPPORT",
    t4."IUOTP",
    t4."LAC",
    t4."MCC",
    t4."MNC",
    t4."MOCNCMCELL",
    t4."NCC",
    t4."OPNAME",
    t4."PSHPSP",
    t4."PSLPSVP",
    t4."REMARK",
    t4."TYPE",
    t4."VIPCELL",
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELL2GBA1 = ReplaceableObject(
    'huawei_cm_2g."GCELL2GBA1"',
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
    t1."CELL2GBA1BCCH",
    t1."CELL2GBA1OPTSW",
    t1."CELL2GBA1TAG",
    t1."CELLID",
    t1."ITEM",
    t1."ITEMVALID",
    t1."CELL2GBA1OPTENHSW"
FROM
huawei_nbi_gsm."GCELL2GBA1" t1

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
    t2."CELL2GBA1OPTSW",
    t2."CELL2GBA1TAG",
    t2."CELLID",
    t2."ITEM",
    t2."ITEMVALID",
    NULL
FROM
huawei_gexport_gsm."GCELL2GBA1_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CELL2GBA1OPTSW",
    t3."CELL2GBA1TAG",
    t3."CELLID",
    t3."ITEM",
    t3."ITEMVALID",
    NULL
FROM
huawei_gexport_gsm."GCELL2GBA1_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CELL2GBA1OPTSW",
    t4."CELL2GBA1TAG",
    t4."CELLID",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELL2GBA1" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELL3GARFCN = ReplaceableObject(
    'huawei_cm_2g."GCELL3GARFCN"',
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
    t1."INPUT3GARFCNEN"
FROM
huawei_nbi_gsm."GCELL3GARFCN" t1

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
    t2."INPUT3GARFCNEN"
FROM
huawei_gexport_gsm."GCELL3GARFCN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."INPUT3GARFCNEN"
FROM
huawei_gexport_gsm."GCELL3GARFCN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."INPUT3GARFCNEN"
FROM
huawei_mml_gsm."GCELL3GARFCN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLAMRQUL = ReplaceableObject(
    'huawei_cm_2g."GCELLAMRQUL"',
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
    t1."DLQUALIMITAMRFR",
    t1."DLQUALIMITAMRHR",
    t1."RXLEVOFF",
    t1."RXQUAL1",
    t1."RXQUAL10",
    t1."RXQUAL11",
    t1."RXQUAL12",
    t1."RXQUAL2",
    t1."RXQUAL3",
    t1."RXQUAL4",
    t1."RXQUAL5",
    t1."RXQUAL6",
    t1."RXQUAL7",
    t1."RXQUAL8",
    t1."RXQUAL9",
    t1."ULQUALIMITAMRFR",
    t1."ULQUALIMITAMRHR"
FROM
huawei_nbi_gsm."GCELLAMRQUL" t1

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
    t2."DLQUALIMITAMRFR",
    t2."DLQUALIMITAMRHR",
    t2."RXLEVOFF",
    t2."RXQUAL1",
    t2."RXQUAL10",
    t2."RXQUAL11",
    t2."RXQUAL12",
    t2."RXQUAL2",
    t2."RXQUAL3",
    t2."RXQUAL4",
    t2."RXQUAL5",
    t2."RXQUAL6",
    t2."RXQUAL7",
    t2."RXQUAL8",
    t2."RXQUAL9",
    t2."ULQUALIMITAMRFR",
    t2."ULQUALIMITAMRHR"
FROM
huawei_gexport_gsm."GCELLAMRQUL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DLQUALIMITAMRFR",
    t3."DLQUALIMITAMRHR",
    t3."RXLEVOFF",
    t3."RXQUAL1",
    t3."RXQUAL10",
    t3."RXQUAL11",
    t3."RXQUAL12",
    t3."RXQUAL2",
    t3."RXQUAL3",
    t3."RXQUAL4",
    t3."RXQUAL5",
    t3."RXQUAL6",
    t3."RXQUAL7",
    t3."RXQUAL8",
    t3."RXQUAL9",
    t3."ULQUALIMITAMRFR",
    t3."ULQUALIMITAMRHR"
FROM
huawei_gexport_gsm."GCELLAMRQUL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DLQUALIMITAMRFR",
    t4."DLQUALIMITAMRHR",
    t4."RXLEVOFF",
    t4."RXQUAL1",
    t4."RXQUAL10",
    t4."RXQUAL11",
    t4."RXQUAL12",
    t4."RXQUAL2",
    t4."RXQUAL3",
    t4."RXQUAL4",
    t4."RXQUAL5",
    t4."RXQUAL6",
    t4."RXQUAL7",
    t4."RXQUAL8",
    t4."RXQUAL9",
    t4."ULQUALIMITAMRFR",
    t4."ULQUALIMITAMRHR"
FROM
huawei_mml_gsm."GCELLAMRQUL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLBASICPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLBASICPARA"',
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
    t1."BTSADJUST",
    t1."CALLRESTABDIS",
    t1."CELL8PSKPOWERLEVEL",
    t1."CELLID",
    t1."CELLSCENARIO",
    t1."CMEPRIOR",
    t1."DIRECTRYEN",
    t1."DIVERT16QAMDELAY",
    t1."DIVERT32QAMDELAY",
    t1."DIVERT8PSKDELAY",
    t1."DNPCEN",
    t1."DYNOPENTRXPOWER",
    t1."ENCRY",
    t1."ENCRYPTIONALGORITHM1ST",
    t1."ENCRYPTIONALGORITHM2ND",
    t1."ENCRYPTIONALGORITHM3RD",
    t1."ENCRYPTIONALGORITHM4TH",
    t1."ENCRYPTIONALGORITHM5TH",
    t1."ENCRYPTIONALGORITHM6TH",
    t1."ENCRYPTIONALGORITHM7TH",
    t1."FASTCALLTCHTHRESHOLD",
    t1."FRDLDTX",
    t1."FRULDTX",
    t1."GMSKDELAY",
    t1."GMSKDELAYDYNADJSW",
    t1."HIGHMODPWREN",
    t1."HRDLDTX",
    t1."HRULDTX",
    t1."ICBALLOW",
    t1."IMMASSCBB",
    t1."IMMASSEN",
    t1."IMMTCHLOADTHRES",
    t1."LAYER",
    t1."LEVELRPT",
    t1."MAXTA",
    t1."MICCSWITCH",
    t1."NBAMRTFOSWITCH",
    t1."PDCH2SDEN",
    t1."POWERREDUCE16QAM",
    t1."POWERREDUCE32QAM",
    t1."RTPSWITCH",
    t1."RXMIN",
    t1."SDDYN",
    t1."SVHOCNGSTTHR",
    t1."SVHODTXDTCTIMER",
    t1."SVHOHODELAYTIMER",
    t1."SVHOSWITCH",
    t1."TIMESLOTVOLADJALLOW",
    t1."UMAISSWITCH",
    t1."UPPCEN"
FROM
huawei_nbi_gsm."GCELLBASICPARA" t1

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
    t2."BTSADJUST",
    t2."CALLRESTABDIS",
    t2."CELL8PSKPOWERLEVEL",
    t2."CELLID",
    t2."CELLSCENARIO",
    NULL,
    t2."DIRECTRYEN",
    t2."DIVERT16QAMDELAY",
    t2."DIVERT32QAMDELAY",
    t2."DIVERT8PSKDELAY",
    t2."DNPCEN",
    t2."DYNOPENTRXPOWER",
    NULL,
    t2."ENCRYPTIONALGORITHM1ST",
    t2."ENCRYPTIONALGORITHM2ND",
    t2."ENCRYPTIONALGORITHM3RD",
    t2."ENCRYPTIONALGORITHM4TH",
    t2."ENCRYPTIONALGORITHM5TH",
    t2."ENCRYPTIONALGORITHM6TH",
    t2."ENCRYPTIONALGORITHM7TH",
    t2."FASTCALLTCHTHRESHOLD",
    t2."FRDLDTX",
    t2."FRULDTX",
    t2."GMSKDELAY",
    t2."GMSKDELAYDYNADJSW",
    t2."HIGHMODPWREN",
    t2."HRDLDTX",
    t2."HRULDTX",
    t2."ICBALLOW",
    t2."IMMASSCBB",
    t2."IMMASSEN",
    t2."IMMTCHLOADTHRES",
    t2."LAYER",
    t2."LEVELRPT",
    t2."MAXTA",
    t2."MICCSWITCH",
    t2."NBAMRTFOSWITCH",
    t2."PDCH2SDEN",
    t2."POWERREDUCE16QAM",
    t2."POWERREDUCE32QAM",
    t2."RTPSWITCH",
    t2."RXMIN",
    t2."SDDYN",
    t2."SVHOCNGSTTHR",
    t2."SVHODTXDTCTIMER",
    t2."SVHOHODELAYTIMER",
    t2."SVHOSWITCH",
    t2."TIMESLOTVOLADJALLOW",
    t2."UMAISSWITCH",
    t2."UPPCEN"
FROM
huawei_gexport_gsm."GCELLBASICPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSADJUST",
    t3."CALLRESTABDIS",
    t3."CELL8PSKPOWERLEVEL",
    t3."CELLID",
    t3."CELLSCENARIO",
    NULL,
    t3."DIRECTRYEN",
    t3."DIVERT16QAMDELAY",
    t3."DIVERT32QAMDELAY",
    t3."DIVERT8PSKDELAY",
    t3."DNPCEN",
    t3."DYNOPENTRXPOWER",
    NULL,
    t3."ENCRYPTIONALGORITHM1ST",
    t3."ENCRYPTIONALGORITHM2ND",
    t3."ENCRYPTIONALGORITHM3RD",
    t3."ENCRYPTIONALGORITHM4TH",
    t3."ENCRYPTIONALGORITHM5TH",
    t3."ENCRYPTIONALGORITHM6TH",
    t3."ENCRYPTIONALGORITHM7TH",
    t3."FASTCALLTCHTHRESHOLD",
    t3."FRDLDTX",
    t3."FRULDTX",
    t3."GMSKDELAY",
    t3."GMSKDELAYDYNADJSW",
    t3."HIGHMODPWREN",
    t3."HRDLDTX",
    t3."HRULDTX",
    t3."ICBALLOW",
    t3."IMMASSCBB",
    t3."IMMASSEN",
    t3."IMMTCHLOADTHRES",
    t3."LAYER",
    t3."LEVELRPT",
    t3."MAXTA",
    t3."MICCSWITCH",
    t3."NBAMRTFOSWITCH",
    t3."PDCH2SDEN",
    t3."POWERREDUCE16QAM",
    t3."POWERREDUCE32QAM",
    t3."RTPSWITCH",
    t3."RXMIN",
    t3."SDDYN",
    t3."SVHOCNGSTTHR",
    t3."SVHODTXDTCTIMER",
    t3."SVHOHODELAYTIMER",
    t3."SVHOSWITCH",
    t3."TIMESLOTVOLADJALLOW",
    t3."UMAISSWITCH",
    t3."UPPCEN"
FROM
huawei_gexport_gsm."GCELLBASICPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSADJUST",
    t4."CALLRESTABDIS",
    t4."CELL8PSKPOWERLEVEL",
    t4."CELLID",
    t4."CELLSCENARIO",
    NULL,
    t4."DIRECTRYEN",
    t4."DIVERT16QAMDELAY",
    t4."DIVERT32QAMDELAY",
    t4."DIVERT8PSKDELAY",
    t4."DNPCEN",
    t4."DYNOPENTRXPOWER",
    NULL,
    t4."ENCRYPTIONALGORITHM1ST",
    t4."ENCRYPTIONALGORITHM2ND",
    t4."ENCRYPTIONALGORITHM3RD",
    t4."ENCRYPTIONALGORITHM4TH",
    t4."ENCRYPTIONALGORITHM5TH",
    t4."ENCRYPTIONALGORITHM6TH",
    t4."ENCRYPTIONALGORITHM7TH",
    t4."FASTCALLTCHTHRESHOLD",
    t4."FRDLDTX",
    t4."FRULDTX",
    t4."GMSKDELAY",
    t4."GMSKDELAYDYNADJSW",
    t4."HIGHMODPWREN",
    t4."HRDLDTX",
    t4."HRULDTX",
    t4."ICBALLOW",
    t4."IMMASSCBB",
    t4."IMMASSEN",
    t4."IMMTCHLOADTHRES",
    t4."LAYER",
    t4."LEVELRPT",
    t4."MAXTA",
    t4."MICCSWITCH",
    t4."NBAMRTFOSWITCH",
    t4."PDCH2SDEN",
    t4."POWERREDUCE16QAM",
    t4."POWERREDUCE32QAM",
    t4."RTPSWITCH",
    t4."RXMIN",
    t4."SDDYN",
    t4."SVHOCNGSTTHR",
    t4."SVHODTXDTCTIMER",
    t4."SVHOHODELAYTIMER",
    t4."SVHOSWITCH",
    t4."TIMESLOTVOLADJALLOW",
    t4."UMAISSWITCH",
    t4."UPPCEN"
FROM
huawei_mml_gsm."GCELLBASICPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLBTSSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLBTSSOFTPARA"',
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
    t1."BTSID",
    t1."CELLID",
    t1."CROCALCHKSW",
    t1."CSEHTYP",
    t1."DRFURXOPTSW",
    t1."HOTATHD",
    t1."HOTATHDSW",
    t1."IMMASSTBFRETXSW",
    t1."INTERFBANDEMG",
    t1."PAGINGOVERRPTTHRD",
    t1."RFCONNINSPECT",
    t1."RXCHANALMTHD",
    t1."SAICDETTYP",
    t1."TBFASSADJSW"
FROM
huawei_nbi_gsm."GCELLBTSSOFTPARA" t1

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
    t2."BTSID",
    t2."CELLID",
    t2."CROCALCHKSW",
    t2."CSEHTYP",
    t2."DRFURXOPTSW",
    t2."HOTATHD",
    t2."HOTATHDSW",
    t2."IMMASSTBFRETXSW",
    t2."INTERFBANDEMG",
    t2."PAGINGOVERRPTTHRD",
    t2."RFCONNINSPECT",
    t2."RXCHANALMTHD",
    t2."SAICDETTYP",
    t2."TBFASSADJSW"
FROM
huawei_gexport_gsm."GCELLBTSSOFTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."CELLID",
    t3."CROCALCHKSW",
    t3."CSEHTYP",
    t3."DRFURXOPTSW",
    t3."HOTATHD",
    t3."HOTATHDSW",
    t3."IMMASSTBFRETXSW",
    t3."INTERFBANDEMG",
    t3."PAGINGOVERRPTTHRD",
    t3."RFCONNINSPECT",
    t3."RXCHANALMTHD",
    t3."SAICDETTYP",
    t3."TBFASSADJSW"
FROM
huawei_gexport_gsm."GCELLBTSSOFTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."CELLID",
    t4."CROCALCHKSW",
    t4."CSEHTYP",
    t4."DRFURXOPTSW",
    t4."HOTATHD",
    t4."HOTATHDSW",
    t4."IMMASSTBFRETXSW",
    t4."INTERFBANDEMG",
    t4."PAGINGOVERRPTTHRD",
    t4."RFCONNINSPECT",
    t4."RXCHANALMTHD",
    t4."SAICDETTYP",
    t4."TBFASSADJSW"
FROM
huawei_mml_gsm."GCELLBTSSOFTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCCACCESS = ReplaceableObject(
    'huawei_cm_2g."GCELLCCACCESS"',
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
    t1."BHPREPOLICY",
    t1."CELLID",
    t1."CELLTCHREQARRRTCTRLSW",
    t1."CHREQCSMSGMAXNUMINPERIOD",
    t1."CHREQPSMSGMAXNUMINPERIOD",
    t1."LOCUPDMSGMAXNUMINPERIOD",
    t1."PSRACHACCLEV",
    t1."PWRDIV",
    t1."PWRDIVIND",
    t1."RACHACCLEV",
    t1."RANERRTHRED",
    t1."TRXAIDSWITCH",
    t1."VOICEVER"
FROM
huawei_nbi_gsm."GCELLCCACCESS" t1

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
    t2."BHPREPOLICY",
    t2."CELLID",
    NULL,
    t2."CHREQCSMSGMAXNUMINPERIOD",
    t2."CHREQPSMSGMAXNUMINPERIOD",
    t2."LOCUPDMSGMAXNUMINPERIOD",
    t2."PSRACHACCLEV",
    t2."PWRDIV",
    t2."PWRDIVIND",
    t2."RACHACCLEV",
    t2."RANERRTHRED",
    t2."TRXAIDSWITCH",
    NULL
FROM
huawei_gexport_gsm."GCELLCCACCESS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BHPREPOLICY",
    t3."CELLID",
    NULL,
    t3."CHREQCSMSGMAXNUMINPERIOD",
    t3."CHREQPSMSGMAXNUMINPERIOD",
    t3."LOCUPDMSGMAXNUMINPERIOD",
    t3."PSRACHACCLEV",
    t3."PWRDIV",
    t3."PWRDIVIND",
    t3."RACHACCLEV",
    t3."RANERRTHRED",
    t3."TRXAIDSWITCH",
    NULL
FROM
huawei_gexport_gsm."GCELLCCACCESS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BHPREPOLICY",
    t4."CELLID",
    NULL,
    t4."CHREQCSMSGMAXNUMINPERIOD",
    t4."CHREQPSMSGMAXNUMINPERIOD",
    t4."LOCUPDMSGMAXNUMINPERIOD",
    t4."PSRACHACCLEV",
    t4."PWRDIV",
    t4."PWRDIVIND",
    t4."RACHACCLEV",
    t4."RANERRTHRED",
    t4."TRXAIDSWITCH",
    NULL
FROM
huawei_mml_gsm."GCELLCCACCESS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCCAD = ReplaceableObject(
    'huawei_cm_2g."GCELLCCAD"',
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
    t1."ASSQUELEN",
    t1."ASSRETRYMAX",
    t1."CELLID",
    t1."CELLSELECTAFTERCALLREL",
    t1."DNSENDSMDIS",
    t1."EMCALLDIRRETRYOPT",
    t1."EMCPRILV",
    t1."FSTRTNTDDWITHOUTMR",
    t1."MAXTADROPCALLFILTER",
    t1."MAXTADROPCALLOPTSW",
    t1."MAXTADROPCALLSWITCH",
    t1."MAXTADROPCALLTHRESHOLD",
    t1."POSSI13",
    t1."PREEMPTIONPERMIT",
    t1."REASSFREQBAND",
    t1."TAADJINTV",
    t1."TAADJOPTSW",
    t1."UPSENDSMDIS"
FROM
huawei_nbi_gsm."GCELLCCAD" t1

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
    t2."ASSQUELEN",
    t2."ASSRETRYMAX",
    t2."CELLID",
    t2."CELLSELECTAFTERCALLREL",
    t2."DNSENDSMDIS",
    t2."EMCALLDIRRETRYOPT",
    t2."EMCPRILV",
    t2."FSTRTNTDDWITHOUTMR",
    t2."MAXTADROPCALLFILTER",
    t2."MAXTADROPCALLOPTSW",
    t2."MAXTADROPCALLSWITCH",
    t2."MAXTADROPCALLTHRESHOLD",
    t2."POSSI13",
    t2."PREEMPTIONPERMIT",
    t2."REASSFREQBAND",
    t2."TAADJINTV",
    t2."TAADJOPTSW",
    t2."UPSENDSMDIS"
FROM
huawei_gexport_gsm."GCELLCCAD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ASSQUELEN",
    t3."ASSRETRYMAX",
    t3."CELLID",
    t3."CELLSELECTAFTERCALLREL",
    t3."DNSENDSMDIS",
    t3."EMCALLDIRRETRYOPT",
    t3."EMCPRILV",
    t3."FSTRTNTDDWITHOUTMR",
    t3."MAXTADROPCALLFILTER",
    t3."MAXTADROPCALLOPTSW",
    t3."MAXTADROPCALLSWITCH",
    t3."MAXTADROPCALLTHRESHOLD",
    t3."POSSI13",
    t3."PREEMPTIONPERMIT",
    t3."REASSFREQBAND",
    t3."TAADJINTV",
    t3."TAADJOPTSW",
    t3."UPSENDSMDIS"
FROM
huawei_gexport_gsm."GCELLCCAD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ASSQUELEN",
    t4."ASSRETRYMAX",
    t4."CELLID",
    t4."CELLSELECTAFTERCALLREL",
    t4."DNSENDSMDIS",
    t4."EMCALLDIRRETRYOPT",
    t4."EMCPRILV",
    t4."FSTRTNTDDWITHOUTMR",
    t4."MAXTADROPCALLFILTER",
    t4."MAXTADROPCALLOPTSW",
    t4."MAXTADROPCALLSWITCH",
    t4."MAXTADROPCALLTHRESHOLD",
    t4."POSSI13",
    t4."PREEMPTIONPERMIT",
    t4."REASSFREQBAND",
    t4."TAADJINTV",
    t4."TAADJOPTSW",
    t4."UPSENDSMDIS"
FROM
huawei_mml_gsm."GCELLCCAD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCCAMR = ReplaceableObject(
    'huawei_cm_2g."GCELLCCAMR"',
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
    t1."ACSSETF",
    t1."ACSSETH",
    t1."ACTCDSETF",
    t1."ACTCDSETH",
    t1."ACTCDSETWB",
    t1."AMRDADTHAW",
    t1."AMRRATEADJOPTALG",
    t1."AMRUADTHAW",
    t1."CELLID",
    t1."DLHYSTF1",
    t1."DLHYSTF2",
    t1."DLHYSTF3",
    t1."DLHYSTH1",
    t1."DLHYSTH2",
    t1."DLHYSTH3",
    t1."DLHYSTWB1",
    t1."DLHYSTWB2",
    t1."DLLTFERLOWTH",
    t1."DLLTFERTGT",
    t1."DLLTFERUPTH",
    t1."DLLTTHADJFA",
    t1."DLTHF1",
    t1."DLTHF2",
    t1."DLTHF3",
    t1."DLTHH1",
    t1."DLTHH2",
    t1."DLTHH3",
    t1."DLTHWB1",
    t1."DLTHWB2",
    t1."INITCDMDF",
    t1."INITCDMDH",
    t1."INITCDMDWB",
    t1."LTFERLOWTH",
    t1."LTFERTGT",
    t1."LTFERUPTH",
    t1."LTTHADJFA",
    t1."RATECTRLSW",
    t1."RATSCCHENABLED",
    t1."ULHYSTF1",
    t1."ULHYSTF2",
    t1."ULHYSTF3",
    t1."ULHYSTH1",
    t1."ULHYSTH2",
    t1."ULHYSTH3",
    t1."ULHYSTWB1",
    t1."ULHYSTWB2",
    t1."ULTHF1",
    t1."ULTHF2",
    t1."ULTHF3",
    t1."ULTHH1",
    t1."ULTHH2",
    t1."ULTHH3",
    t1."ULTHWB1",
    t1."ULTHWB2"
FROM
huawei_nbi_gsm."GCELLCCAMR" t1

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
    NULL,
    NULL,
    NULL,
    NULL,
    t2."AMRDADTHAW",
    t2."AMRRATEADJOPTALG",
    t2."AMRUADTHAW",
    t2."CELLID",
    t2."DLHYSTF1",
    t2."DLHYSTF2",
    t2."DLHYSTF3",
    t2."DLHYSTH1",
    t2."DLHYSTH2",
    t2."DLHYSTH3",
    t2."DLHYSTWB1",
    t2."DLHYSTWB2",
    t2."DLLTFERLOWTH",
    t2."DLLTFERTGT",
    t2."DLLTFERUPTH",
    t2."DLLTTHADJFA",
    t2."DLTHF1",
    t2."DLTHF2",
    t2."DLTHF3",
    t2."DLTHH1",
    t2."DLTHH2",
    t2."DLTHH3",
    t2."DLTHWB1",
    t2."DLTHWB2",
    t2."INITCDMDF",
    t2."INITCDMDH",
    t2."INITCDMDWB",
    t2."LTFERLOWTH",
    t2."LTFERTGT",
    t2."LTFERUPTH",
    t2."LTTHADJFA",
    t2."RATECTRLSW",
    t2."RATSCCHENABLED",
    t2."ULHYSTF1",
    t2."ULHYSTF2",
    t2."ULHYSTF3",
    t2."ULHYSTH1",
    t2."ULHYSTH2",
    t2."ULHYSTH3",
    t2."ULHYSTWB1",
    t2."ULHYSTWB2",
    t2."ULTHF1",
    t2."ULTHF2",
    t2."ULTHF3",
    t2."ULTHH1",
    t2."ULTHH2",
    t2."ULTHH3",
    t2."ULTHWB1",
    t2."ULTHWB2"
FROM
huawei_gexport_gsm."GCELLCCAMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    NULL,
    NULL,
    NULL,
    NULL,
    t3."AMRDADTHAW",
    t3."AMRRATEADJOPTALG",
    t3."AMRUADTHAW",
    t3."CELLID",
    t3."DLHYSTF1",
    t3."DLHYSTF2",
    t3."DLHYSTF3",
    t3."DLHYSTH1",
    t3."DLHYSTH2",
    t3."DLHYSTH3",
    t3."DLHYSTWB1",
    t3."DLHYSTWB2",
    t3."DLLTFERLOWTH",
    t3."DLLTFERTGT",
    t3."DLLTFERUPTH",
    t3."DLLTTHADJFA",
    t3."DLTHF1",
    t3."DLTHF2",
    t3."DLTHF3",
    t3."DLTHH1",
    t3."DLTHH2",
    t3."DLTHH3",
    t3."DLTHWB1",
    t3."DLTHWB2",
    t3."INITCDMDF",
    t3."INITCDMDH",
    t3."INITCDMDWB",
    t3."LTFERLOWTH",
    t3."LTFERTGT",
    t3."LTFERUPTH",
    t3."LTTHADJFA",
    t3."RATECTRLSW",
    t3."RATSCCHENABLED",
    t3."ULHYSTF1",
    t3."ULHYSTF2",
    t3."ULHYSTF3",
    t3."ULHYSTH1",
    t3."ULHYSTH2",
    t3."ULHYSTH3",
    t3."ULHYSTWB1",
    t3."ULHYSTWB2",
    t3."ULTHF1",
    t3."ULTHF2",
    t3."ULTHF3",
    t3."ULTHH1",
    t3."ULTHH2",
    t3."ULTHH3",
    t3."ULTHWB1",
    t3."ULTHWB2"
FROM
huawei_gexport_gsm."GCELLCCAMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AMRDADTHAW",
    t4."AMRRATEADJOPTALG",
    t4."AMRUADTHAW",
    t4."CELLID",
    t4."DLHYSTF1",
    t4."DLHYSTF2",
    t4."DLHYSTF3",
    t4."DLHYSTH1",
    t4."DLHYSTH2",
    t4."DLHYSTH3",
    t4."DLHYSTWB1",
    t4."DLHYSTWB2",
    t4."DLLTFERLOWTH",
    t4."DLLTFERTGT",
    t4."DLLTFERUPTH",
    t4."DLLTTHADJFA",
    t4."DLTHF1",
    t4."DLTHF2",
    t4."DLTHF3",
    t4."DLTHH1",
    t4."DLTHH2",
    t4."DLTHH3",
    t4."DLTHWB1",
    t4."DLTHWB2",
    t4."INITCDMDF",
    t4."INITCDMDH",
    t4."INITCDMDWB",
    t4."LTFERLOWTH",
    t4."LTFERTGT",
    t4."LTFERUPTH",
    t4."LTTHADJFA",
    t4."RATECTRLSW",
    t4."RATSCCHENABLED",
    t4."ULHYSTF1",
    t4."ULHYSTF2",
    t4."ULHYSTF3",
    t4."ULHYSTH1",
    t4."ULHYSTH2",
    t4."ULHYSTH3",
    t4."ULHYSTWB1",
    t4."ULHYSTWB2",
    t4."ULTHF1",
    t4."ULTHF2",
    t4."ULTHF3",
    t4."ULTHH1",
    t4."ULTHH2",
    t4."ULTHH3",
    t4."ULTHWB1",
    t4."ULTHWB2"
FROM
huawei_mml_gsm."GCELLCCAMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCCBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLCCBASIC"',
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
    t1."ACCCTRLEN",
    t1."AFRDSBLCNT",
    t1."AFRSAMULFRM",
    t1."AHRDSBLCNT",
    t1."AHRSAMULFRM",
    t1."ASSLOADJUDGEEN",
    t1."CELLID",
    t1."COMMACC",
    t1."DTLOADTHRED",
    t1."ECSC",
    t1."EMLPPEN",
    t1."ERGCALLDIS",
    t1."MBR",
    t1."MSMAXRETRAN",
    t1."PAGTIMES",
    t1."RACHBUSYTHRED",
    t1."REASSEN",
    t1."REPEATDLFASET",
    t1."REPEATDLFATHRED",
    t1."REPEATSADLTHD",
    t1."REPEATSASET",
    t1."REPEATSAULTHD",
    t1."RLT",
    t1."SAMULFRM",
    t1."SATIMEROPTSW",
    t1."SPECACC",
    t1."UMSFRBERTHRESH",
    t1."UMSFRLLRFACTOR",
    t1."UMSFRLLRTHRESH",
    t1."UMSFRSWITCH"
FROM
huawei_nbi_gsm."GCELLCCBASIC" t1

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
    t2."ACCCTRLEN",
    t2."AFRDSBLCNT",
    t2."AFRSAMULFRM",
    t2."AHRDSBLCNT",
    t2."AHRSAMULFRM",
    t2."ASSLOADJUDGEEN",
    t2."CELLID",
    NULL,
    t2."DTLOADTHRED",
    t2."ECSC",
    t2."EMLPPEN",
    t2."ERGCALLDIS",
    t2."MBR",
    t2."MSMAXRETRAN",
    t2."PAGTIMES",
    t2."RACHBUSYTHRED",
    t2."REASSEN",
    t2."REPEATDLFASET",
    NULL,
    t2."REPEATSADLTHD",
    t2."REPEATSASET",
    t2."REPEATSAULTHD",
    t2."RLT",
    t2."SAMULFRM",
    t2."SATIMEROPTSW",
    NULL,
    t2."UMSFRBERTHRESH",
    t2."UMSFRLLRFACTOR",
    t2."UMSFRLLRTHRESH",
    t2."UMSFRSWITCH"
FROM
huawei_gexport_gsm."GCELLCCBASIC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACCCTRLEN",
    t3."AFRDSBLCNT",
    t3."AFRSAMULFRM",
    t3."AHRDSBLCNT",
    t3."AHRSAMULFRM",
    t3."ASSLOADJUDGEEN",
    t3."CELLID",
    NULL,
    t3."DTLOADTHRED",
    t3."ECSC",
    t3."EMLPPEN",
    t3."ERGCALLDIS",
    t3."MBR",
    t3."MSMAXRETRAN",
    t3."PAGTIMES",
    t3."RACHBUSYTHRED",
    t3."REASSEN",
    t3."REPEATDLFASET",
    NULL,
    t3."REPEATSADLTHD",
    t3."REPEATSASET",
    t3."REPEATSAULTHD",
    t3."RLT",
    t3."SAMULFRM",
    t3."SATIMEROPTSW",
    NULL,
    t3."UMSFRBERTHRESH",
    t3."UMSFRLLRFACTOR",
    t3."UMSFRLLRTHRESH",
    t3."UMSFRSWITCH"
FROM
huawei_gexport_gsm."GCELLCCBASIC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACCCTRLEN",
    t4."AFRDSBLCNT",
    t4."AFRSAMULFRM",
    t4."AHRDSBLCNT",
    t4."AHRSAMULFRM",
    t4."ASSLOADJUDGEEN",
    t4."CELLID",
    NULL,
    t4."DTLOADTHRED",
    t4."ECSC",
    t4."EMLPPEN",
    t4."ERGCALLDIS",
    t4."MBR",
    t4."MSMAXRETRAN",
    t4."PAGTIMES",
    t4."RACHBUSYTHRED",
    t4."REASSEN",
    t4."REPEATDLFASET",
    t4."REPEATDLFATHRED",
    t4."REPEATSADLTHD",
    t4."REPEATSASET",
    t4."REPEATSAULTHD",
    t4."RLT",
    t4."SAMULFRM",
    t4."SATIMEROPTSW",
    NULL,
    t4."UMSFRBERTHRESH",
    t4."UMSFRLLRFACTOR",
    t4."UMSFRLLRTHRESH",
    t4."UMSFRSWITCH"
FROM
huawei_mml_gsm."GCELLCCBASIC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCCCH = ReplaceableObject(
    'huawei_cm_2g."GCELLCCCH"',
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
    t1."ABISFCEN",
    t1."CANPC",
    t1."CCCHLOADINDPRD",
    t1."CCCHLOADTHRES",
    t1."CELLID",
    t1."DYNCCCHSWITCH",
    t1."FMSMAXOPCC",
    t1."HRATESPT",
    t1."OVERLOADINTV",
    t1."PAGINGOVLDPROCOPTSW",
    t1."PAGINGREORGLAGTM",
    t1."PAGINGREORGSTARTTHRD",
    t1."PAGINGREORGSTOPTHRD",
    t1."PAGINGREORGSW",
    t1."PCHMSGPRIORSW",
    t1."RACHLDAVERSLOT",
    t1."RACHLOADALM",
    t1."RFRESINDPRD"
FROM
huawei_nbi_gsm."GCELLCCCH" t1

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
    t2."ABISFCEN",
    t2."CANPC",
    t2."CCCHLOADINDPRD",
    t2."CCCHLOADTHRES",
    t2."CELLID",
    t2."DYNCCCHSWITCH",
    t2."FMSMAXOPCC",
    t2."HRATESPT",
    t2."OVERLOADINTV",
    t2."PAGINGOVLDPROCOPTSW",
    t2."PAGINGREORGLAGTM",
    t2."PAGINGREORGSTARTTHRD",
    t2."PAGINGREORGSTOPTHRD",
    t2."PAGINGREORGSW",
    t2."PCHMSGPRIORSW",
    t2."RACHLDAVERSLOT",
    t2."RACHLOADALM",
    t2."RFRESINDPRD"
FROM
huawei_gexport_gsm."GCELLCCCH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISFCEN",
    t3."CANPC",
    t3."CCCHLOADINDPRD",
    t3."CCCHLOADTHRES",
    t3."CELLID",
    t3."DYNCCCHSWITCH",
    t3."FMSMAXOPCC",
    t3."HRATESPT",
    t3."OVERLOADINTV",
    t3."PAGINGOVLDPROCOPTSW",
    t3."PAGINGREORGLAGTM",
    t3."PAGINGREORGSTARTTHRD",
    t3."PAGINGREORGSTOPTHRD",
    t3."PAGINGREORGSW",
    t3."PCHMSGPRIORSW",
    t3."RACHLDAVERSLOT",
    t3."RACHLOADALM",
    t3."RFRESINDPRD"
FROM
huawei_gexport_gsm."GCELLCCCH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISFCEN",
    t4."CANPC",
    t4."CCCHLOADINDPRD",
    t4."CCCHLOADTHRES",
    t4."CELLID",
    t4."DYNCCCHSWITCH",
    t4."FMSMAXOPCC",
    t4."HRATESPT",
    t4."OVERLOADINTV",
    t4."PAGINGOVLDPROCOPTSW",
    t4."PAGINGREORGLAGTM",
    t4."PAGINGREORGSTARTTHRD",
    t4."PAGINGREORGSTOPTHRD",
    t4."PAGINGREORGSW",
    t4."PCHMSGPRIORSW",
    t4."RACHLDAVERSLOT",
    t4."RACHLOADALM",
    t4."RFRESINDPRD"
FROM
huawei_mml_gsm."GCELLCCCH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCCTMR = ReplaceableObject(
    'huawei_cm_2g."GCELLCCTMR"',
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
    t1."IMMASSRESENDEN",
    t1."N200PARASWITCH",
    t1."T200FACCHF",
    t1."T200FACCHH",
    t1."T200SACCH3",
    t1."T200SACCHS",
    t1."T200SACCT0",
    t1."T200SDCCH",
    t1."T200SDCCH3",
    t1."N200ESTAB",
    t1."N200FFULL",
    t1."N200FHALF",
    t1."N200REL",
    t1."N200SACCH",
    t1."N200SDCCH"
FROM
huawei_nbi_gsm."GCELLCCTMR" t1

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
    t2."IMMASSRESENDEN",
    t2."N200PARASWITCH",
    t2."T200FACCHF",
    t2."T200FACCHH",
    t2."T200SACCH3",
    t2."T200SACCHS",
    t2."T200SACCT0",
    t2."T200SDCCH",
    t2."T200SDCCH3",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLCCTMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IMMASSRESENDEN",
    t3."N200PARASWITCH",
    t3."T200FACCHF",
    t3."T200FACCHH",
    t3."T200SACCH3",
    t3."T200SACCHS",
    t3."T200SACCT0",
    t3."T200SDCCH",
    t3."T200SDCCH3",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLCCTMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IMMASSRESENDEN",
    t4."N200PARASWITCH",
    t4."T200FACCHF",
    t4."T200FACCHH",
    t4."T200SACCH3",
    t4."T200SACCHS",
    t4."T200SACCT0",
    t4."T200SDCCH",
    t4."T200SDCCH3",
    t4."N200ESTAB",
    t4."N200FFULL",
    t4."N200FHALF",
    t4."N200REL",
    t4."N200SACCH",
    t4."N200SDCCH"
FROM
huawei_mml_gsm."GCELLCCTMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCCUTRANSYS = ReplaceableObject(
    'huawei_cm_2g."GCELLCCUTRANSYS"',
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
    t1."BESTTDDCELLNUM",
    t1."CELL1800OFF",
    t1."CELL1800THRED",
    t1."CELL900OFF",
    t1."CELL900THRED",
    t1."CELLID",
    t1."EMRMSCAPIDESWITCH",
    t1."EMRMSCAPPROSWITCH",
    t1."FDDCELLOFF",
    t1."FDDCELLTHRED",
    t1."FDDFREQCNUM",
    t1."FDDQMIN",
    t1."FDDQMINOFFSET",
    t1."FDDQOFF",
    t1."FDDREP",
    t1."FDDRPTTHRESHOLD2ECNO",
    t1."FDDRPTTHRESHOLD2RSCP",
    t1."FDDRSCPMIN",
    t1."FIRSTSI2QUATERMSGOPTSW",
    t1."GSMFREQCNUM",
    t1."INVALBSICEN",
    t1."MEASURETYPE",
    t1."MSCVER",
    t1."POS2QUATER",
    t1."QCI",
    t1."QI",
    t1."QP",
    t1."QSEARCHC",
    t1."SCALEORDER",
    t1."SEARCH3G",
    t1."SI2QUATEROPTIMIZEDALLOWED",
    t1."TDDCELLOFF",
    t1."TDDCELLRESELDIV",
    t1."TDDCELLTHRED",
    t1."TDDMIOPTIMIZEDALLOWED",
    t1."TDDMIPROHIBIT",
    t1."TDDSIOPTIMIZEDALLOWED"
FROM
huawei_nbi_gsm."GCELLCCUTRANSYS" t1

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
    t2."BESTTDDCELLNUM",
    t2."CELL1800OFF",
    t2."CELL1800THRED",
    t2."CELL900OFF",
    t2."CELL900THRED",
    t2."CELLID",
    t2."EMRMSCAPIDESWITCH",
    t2."EMRMSCAPPROSWITCH",
    t2."FDDCELLOFF",
    t2."FDDCELLTHRED",
    t2."FDDFREQCNUM",
    t2."FDDQMIN",
    t2."FDDQMINOFFSET",
    t2."FDDQOFF",
    t2."FDDREP",
    t2."FDDRPTTHRESHOLD2ECNO",
    t2."FDDRPTTHRESHOLD2RSCP",
    t2."FDDRSCPMIN",
    t2."FIRSTSI2QUATERMSGOPTSW",
    t2."GSMFREQCNUM",
    t2."INVALBSICEN",
    t2."MEASURETYPE",
    t2."MSCVER",
    t2."POS2QUATER",
    t2."QCI",
    t2."QI",
    t2."QP",
    t2."QSEARCHC",
    t2."SCALEORDER",
    t2."SEARCH3G",
    t2."SI2QUATEROPTIMIZEDALLOWED",
    t2."TDDCELLOFF",
    t2."TDDCELLRESELDIV",
    t2."TDDCELLTHRED",
    t2."TDDMIOPTIMIZEDALLOWED",
    t2."TDDMIPROHIBIT",
    t2."TDDSIOPTIMIZEDALLOWED"
FROM
huawei_gexport_gsm."GCELLCCUTRANSYS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BESTTDDCELLNUM",
    t3."CELL1800OFF",
    t3."CELL1800THRED",
    t3."CELL900OFF",
    t3."CELL900THRED",
    t3."CELLID",
    t3."EMRMSCAPIDESWITCH",
    t3."EMRMSCAPPROSWITCH",
    t3."FDDCELLOFF",
    t3."FDDCELLTHRED",
    t3."FDDFREQCNUM",
    t3."FDDQMIN",
    t3."FDDQMINOFFSET",
    t3."FDDQOFF",
    t3."FDDREP",
    t3."FDDRPTTHRESHOLD2ECNO",
    t3."FDDRPTTHRESHOLD2RSCP",
    t3."FDDRSCPMIN",
    t3."FIRSTSI2QUATERMSGOPTSW",
    t3."GSMFREQCNUM",
    t3."INVALBSICEN",
    t3."MEASURETYPE",
    t3."MSCVER",
    t3."POS2QUATER",
    t3."QCI",
    t3."QI",
    t3."QP",
    t3."QSEARCHC",
    t3."SCALEORDER",
    t3."SEARCH3G",
    t3."SI2QUATEROPTIMIZEDALLOWED",
    t3."TDDCELLOFF",
    t3."TDDCELLRESELDIV",
    t3."TDDCELLTHRED",
    t3."TDDMIOPTIMIZEDALLOWED",
    t3."TDDMIPROHIBIT",
    t3."TDDSIOPTIMIZEDALLOWED"
FROM
huawei_gexport_gsm."GCELLCCUTRANSYS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BESTTDDCELLNUM",
    t4."CELL1800OFF",
    t4."CELL1800THRED",
    t4."CELL900OFF",
    t4."CELL900THRED",
    t4."CELLID",
    t4."EMRMSCAPIDESWITCH",
    t4."EMRMSCAPPROSWITCH",
    t4."FDDCELLOFF",
    t4."FDDCELLTHRED",
    t4."FDDFREQCNUM",
    t4."FDDQMIN",
    t4."FDDQMINOFFSET",
    t4."FDDQOFF",
    t4."FDDREP",
    t4."FDDRPTTHRESHOLD2ECNO",
    t4."FDDRPTTHRESHOLD2RSCP",
    t4."FDDRSCPMIN",
    t4."FIRSTSI2QUATERMSGOPTSW",
    t4."GSMFREQCNUM",
    t4."INVALBSICEN",
    t4."MEASURETYPE",
    t4."MSCVER",
    t4."POS2QUATER",
    t4."QCI",
    t4."QI",
    t4."QP",
    t4."QSEARCHC",
    t4."SCALEORDER",
    t4."SEARCH3G",
    t4."SI2QUATEROPTIMIZEDALLOWED",
    t4."TDDCELLOFF",
    t4."TDDCELLRESELDIV",
    t4."TDDCELLTHRED",
    t4."TDDMIOPTIMIZEDALLOWED",
    t4."TDDMIPROHIBIT",
    t4."TDDSIOPTIMIZEDALLOWED"
FROM
huawei_mml_gsm."GCELLCCUTRANSYS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCHMGAD = ReplaceableObject(
    'huawei_cm_2g."GCELLCHMGAD"',
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
    t1."AMRLOADOPTEN",
    t1."AMRTCHHPRIORALLOW",
    t1."AMRTCHHPRIORLOAD",
    t1."ASSOLRXLEVOFFSET",
    t1."BTRXPRIORITYSWITCH",
    t1."CELLID",
    t1."CELLOPPWRGRP",
    t1."CHALLOCATIONOPTSWITCH",
    t1."CHANINTERMESALLOW",
    t1."CHPWRINSUFFALLOWED",
    t1."CIRESTVALUE",
    t1."DLINTERFLEVLIMIT",
    t1."DLINTERFQUALLIMIT",
    t1."FREQLOADSHARETRAFFTHRSH",
    t1."HALFRATEREPACKINGSWITCH",
    t1."HISPRIOALLOW",
    t1."HOOLRXLEVOFFSET",
    t1."HRIUOLDRATESELALLOW",
    t1."HSCSDBUSYTHRES",
    t1."IBCAAFRSOFTBLKTHRD",
    t1."IBCAAHRSOFTBLKTHRD",
    t1."IBCAALLOWED",
    t1."IBCAASSWAITMEASURERPTTIME",
    t1."IBCACALLINFOFILTERLEN",
    t1."IBCACALLSOFTBLOCKTHOFFSET",
    t1."IBCACALLTARGETCIROFFSET",
    t1."IBCACIRESTENHANCE",
    t1."IBCADLPATHLOSSOFF",
    t1."IBCAEHOASSWAITMEASURERPTTIME",
    t1."IBCAESTMTSCCOLLISIONALLOW",
    t1."IBCAFLEXTSCALLOWED",
    t1."IBCAFORCEDBTSSYNCALLOWED",
    t1."IBCAFREEBCCHCHANTHRSHOLD",
    t1."IBCAFREVLOPT",
    t1."IBCAFRSOFTBLKTHRD",
    t1."IBCAGETINTFSRCOPT",
    t1."IBCAHOASSWAITMEASURERPTTIME",
    t1."IBCAHOSOFTBLKTHRESHOLD",
    t1."IBCAHRSOFTBLKTHRD",
    t1."IBCAICDMRELEVOFFSET",
    t1."IBCAICDMSWITCH",
    t1."IBCAINITPCRXLEVDLOFFSET",
    t1."IBCAINITPCRXLEVULOFFSET",
    t1."IBCAINITPCRXQUALDLOFFSET",
    t1."IBCAINITPCRXQUALULOFFSET",
    t1."IBCAIUOPATHLOSSOFF",
    t1."IBCAMAIOUSMTD",
    t1."IBCAMAXINTFSRCNUM",
    t1."IBCANCELLPATHLOSSESTIMATE",
    t1."IBCANEWCALLCIROFFSET",
    t1."IBCANHOASSWAITMEASURERPTTIME",
    t1."IBCANONMEANCELLSTATNUM",
    t1."IBCAOPRREVISEFACTOR",
    t1."IBCAPATHLOSSOFF",
    t1."IBCAPDCHDYNTRANTMR",
    t1."IBCAPDDYNTRENHANCE",
    t1."IBCAPLFILTFACTOR",
    t1."IBCAQUEUEOPT",
    t1."IBCASCELLPATHLOSS",
    t1."IBCASOFTBLKSAICOFF",
    t1."IBCASOFTBLKSWITCH",
    t1."IBCASUBCHNHANDOVERALLOWED",
    t1."IBCATARGETCIRTHRSH",
    t1."IBCAUSEDIUOSUBLAY",
    t1."IBCAUSRDYNCMEASURENCELL",
    t1."IBCAWAFRSOFTBLKTHRD",
    t1."INNAMRTCHHPRIORLOAD",
    t1."INTERFPRIALLOW",
    t1."JUDGERXLEVWHENASSIGNHR",
    t1."LOADSHAREALLOW",
    t1."LOADSTATYPE",
    t1."LOOSESDCCHLOADTHRED",
    t1."LOWRXLEVOLFORBIDOPTSW",
    t1."LOWRXLEVOLFORBIDSWITCH",
    t1."MCPACHAPPOPT",
    t1."MCPALOWTRAFFICTH",
    t1."MCPAOPTALG",
    t1."MINRXLEVWHENASSIGNHR",
    t1."MTSTURNOFFALG",
    t1."MTSTURNOFFHYST",
    t1."MTSTURNOFFTH",
    t1."NAMRLFRMTRXALLOWED",
    t1."OUTAMRTCHHPRIORLOAD",
    t1."PWRPRIORALLOW",
    t1."QLENSD",
    t1."QLENSI",
    t1."QTRUDNPWRLASTTIME",
    t1."QTRUDNPWRSTATTIME",
    t1."QTRUPWRSHARE",
    t1."QUALHOPRIALLOW",
    t1."SCENELOADTYPE",
    t1."SSLENSD",
    t1."SSLENSI",
    t1."TCHBUSYTHRES",
    t1."TCHLOADOPTSWITCH",
    t1."TCHREQSUSPENDINTERVAL",
    t1."TCHTRIBUSYUNDERLAYTHR",
    t1."TCHTRICBUSYOVERLAYTHR",
    t1."TIGHTBCCHASSMAINBCCHLEV",
    t1."TIGHTBCCHASSMAINBCCHQUAL",
    t1."TIGHTSDCCHRXLEVTHRED",
    t1."TRXPRIALLOW",
    t1."TURNOFFLOADTYPE",
    t1."UPINTERFQUALLIMIT",
    t1."UPINTERLEVLIMIT",
    t1."UPRXLEVLASTTIME",
    t1."UPRXLEVSMOOTHPARA",
    t1."UPRXLEVSTATICTIME",
    t1."VAMOSAHSUSERDLSOFTBLOCKTHD",
    t1."WAITSDCCHIDLETIMER"
FROM
huawei_nbi_gsm."GCELLCHMGAD" t1

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
    t2."AMRLOADOPTEN",
    t2."AMRTCHHPRIORALLOW",
    t2."AMRTCHHPRIORLOAD",
    t2."ASSOLRXLEVOFFSET",
    t2."BTRXPRIORITYSWITCH",
    t2."CELLID",
    t2."CELLOPPWRGRP",
    t2."CHALLOCATIONOPTSWITCH",
    t2."CHANINTERMESALLOW",
    t2."CHPWRINSUFFALLOWED",
    t2."CIRESTVALUE",
    t2."DLINTERFLEVLIMIT",
    t2."DLINTERFQUALLIMIT",
    t2."FREQLOADSHARETRAFFTHRSH",
    t2."HALFRATEREPACKINGSWITCH",
    t2."HISPRIOALLOW",
    t2."HOOLRXLEVOFFSET",
    t2."HRIUOLDRATESELALLOW",
    t2."HSCSDBUSYTHRES",
    t2."IBCAAFRSOFTBLKTHRD",
    t2."IBCAAHRSOFTBLKTHRD",
    t2."IBCAALLOWED",
    t2."IBCAASSWAITMEASURERPTTIME",
    t2."IBCACALLINFOFILTERLEN",
    t2."IBCACALLSOFTBLOCKTHOFFSET",
    t2."IBCACALLTARGETCIROFFSET",
    t2."IBCACIRESTENHANCE",
    t2."IBCADLPATHLOSSOFF",
    t2."IBCAEHOASSWAITMEASURERPTTIME",
    t2."IBCAESTMTSCCOLLISIONALLOW",
    t2."IBCAFLEXTSCALLOWED",
    t2."IBCAFORCEDBTSSYNCALLOWED",
    t2."IBCAFREEBCCHCHANTHRSHOLD",
    t2."IBCAFREVLOPT",
    t2."IBCAFRSOFTBLKTHRD",
    t2."IBCAGETINTFSRCOPT",
    t2."IBCAHOASSWAITMEASURERPTTIME",
    t2."IBCAHOSOFTBLKTHRESHOLD",
    t2."IBCAHRSOFTBLKTHRD",
    t2."IBCAICDMRELEVOFFSET",
    t2."IBCAICDMSWITCH",
    t2."IBCAINITPCRXLEVDLOFFSET",
    t2."IBCAINITPCRXLEVULOFFSET",
    t2."IBCAINITPCRXQUALDLOFFSET",
    t2."IBCAINITPCRXQUALULOFFSET",
    t2."IBCAIUOPATHLOSSOFF",
    t2."IBCAMAIOUSMTD",
    t2."IBCAMAXINTFSRCNUM",
    t2."IBCANCELLPATHLOSSESTIMATE",
    t2."IBCANEWCALLCIROFFSET",
    t2."IBCANHOASSWAITMEASURERPTTIME",
    t2."IBCANONMEANCELLSTATNUM",
    t2."IBCAOPRREVISEFACTOR",
    t2."IBCAPATHLOSSOFF",
    t2."IBCAPDCHDYNTRANTMR",
    t2."IBCAPDDYNTRENHANCE",
    t2."IBCAPLFILTFACTOR",
    t2."IBCAQUEUEOPT",
    t2."IBCASCELLPATHLOSS",
    t2."IBCASOFTBLKSAICOFF",
    t2."IBCASOFTBLKSWITCH",
    t2."IBCASUBCHNHANDOVERALLOWED",
    t2."IBCATARGETCIRTHRSH",
    t2."IBCAUSEDIUOSUBLAY",
    t2."IBCAUSRDYNCMEASURENCELL",
    t2."IBCAWAFRSOFTBLKTHRD",
    t2."INNAMRTCHHPRIORLOAD",
    t2."INTERFPRIALLOW",
    t2."JUDGERXLEVWHENASSIGNHR",
    t2."LOADSHAREALLOW",
    t2."LOADSTATYPE",
    t2."LOOSESDCCHLOADTHRED",
    t2."LOWRXLEVOLFORBIDOPTSW",
    t2."LOWRXLEVOLFORBIDSWITCH",
    t2."MCPACHAPPOPT",
    t2."MCPALOWTRAFFICTH",
    t2."MCPAOPTALG",
    t2."MINRXLEVWHENASSIGNHR",
    t2."MTSTURNOFFALG",
    t2."MTSTURNOFFHYST",
    t2."MTSTURNOFFTH",
    t2."NAMRLFRMTRXALLOWED",
    t2."OUTAMRTCHHPRIORLOAD",
    t2."PWRPRIORALLOW",
    t2."QLENSD",
    t2."QLENSI",
    t2."QTRUDNPWRLASTTIME",
    t2."QTRUDNPWRSTATTIME",
    t2."QTRUPWRSHARE",
    t2."QUALHOPRIALLOW",
    NULL,
    t2."SSLENSD",
    t2."SSLENSI",
    t2."TCHBUSYTHRES",
    t2."TCHLOADOPTSWITCH",
    t2."TCHREQSUSPENDINTERVAL",
    t2."TCHTRIBUSYUNDERLAYTHR",
    t2."TCHTRICBUSYOVERLAYTHR",
    t2."TIGHTBCCHASSMAINBCCHLEV",
    t2."TIGHTBCCHASSMAINBCCHQUAL",
    t2."TIGHTSDCCHRXLEVTHRED",
    t2."TRXPRIALLOW",
    t2."TURNOFFLOADTYPE",
    t2."UPINTERFQUALLIMIT",
    t2."UPINTERLEVLIMIT",
    t2."UPRXLEVLASTTIME",
    t2."UPRXLEVSMOOTHPARA",
    t2."UPRXLEVSTATICTIME",
    t2."VAMOSAHSUSERDLSOFTBLOCKTHD",
    t2."WAITSDCCHIDLETIMER"
FROM
huawei_gexport_gsm."GCELLCHMGAD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AMRLOADOPTEN",
    t3."AMRTCHHPRIORALLOW",
    t3."AMRTCHHPRIORLOAD",
    t3."ASSOLRXLEVOFFSET",
    t3."BTRXPRIORITYSWITCH",
    t3."CELLID",
    t3."CELLOPPWRGRP",
    t3."CHALLOCATIONOPTSWITCH",
    t3."CHANINTERMESALLOW",
    t3."CHPWRINSUFFALLOWED",
    t3."CIRESTVALUE",
    t3."DLINTERFLEVLIMIT",
    t3."DLINTERFQUALLIMIT",
    t3."FREQLOADSHARETRAFFTHRSH",
    t3."HALFRATEREPACKINGSWITCH",
    t3."HISPRIOALLOW",
    t3."HOOLRXLEVOFFSET",
    t3."HRIUOLDRATESELALLOW",
    t3."HSCSDBUSYTHRES",
    t3."IBCAAFRSOFTBLKTHRD",
    t3."IBCAAHRSOFTBLKTHRD",
    t3."IBCAALLOWED",
    t3."IBCAASSWAITMEASURERPTTIME",
    t3."IBCACALLINFOFILTERLEN",
    t3."IBCACALLSOFTBLOCKTHOFFSET",
    t3."IBCACALLTARGETCIROFFSET",
    t3."IBCACIRESTENHANCE",
    t3."IBCADLPATHLOSSOFF",
    t3."IBCAEHOASSWAITMEASURERPTTIME",
    t3."IBCAESTMTSCCOLLISIONALLOW",
    t3."IBCAFLEXTSCALLOWED",
    t3."IBCAFORCEDBTSSYNCALLOWED",
    t3."IBCAFREEBCCHCHANTHRSHOLD",
    t3."IBCAFREVLOPT",
    t3."IBCAFRSOFTBLKTHRD",
    t3."IBCAGETINTFSRCOPT",
    t3."IBCAHOASSWAITMEASURERPTTIME",
    t3."IBCAHOSOFTBLKTHRESHOLD",
    t3."IBCAHRSOFTBLKTHRD",
    t3."IBCAICDMRELEVOFFSET",
    t3."IBCAICDMSWITCH",
    t3."IBCAINITPCRXLEVDLOFFSET",
    t3."IBCAINITPCRXLEVULOFFSET",
    t3."IBCAINITPCRXQUALDLOFFSET",
    t3."IBCAINITPCRXQUALULOFFSET",
    t3."IBCAIUOPATHLOSSOFF",
    t3."IBCAMAIOUSMTD",
    t3."IBCAMAXINTFSRCNUM",
    t3."IBCANCELLPATHLOSSESTIMATE",
    t3."IBCANEWCALLCIROFFSET",
    t3."IBCANHOASSWAITMEASURERPTTIME",
    t3."IBCANONMEANCELLSTATNUM",
    t3."IBCAOPRREVISEFACTOR",
    t3."IBCAPATHLOSSOFF",
    t3."IBCAPDCHDYNTRANTMR",
    t3."IBCAPDDYNTRENHANCE",
    t3."IBCAPLFILTFACTOR",
    t3."IBCAQUEUEOPT",
    t3."IBCASCELLPATHLOSS",
    t3."IBCASOFTBLKSAICOFF",
    t3."IBCASOFTBLKSWITCH",
    t3."IBCASUBCHNHANDOVERALLOWED",
    t3."IBCATARGETCIRTHRSH",
    t3."IBCAUSEDIUOSUBLAY",
    t3."IBCAUSRDYNCMEASURENCELL",
    t3."IBCAWAFRSOFTBLKTHRD",
    t3."INNAMRTCHHPRIORLOAD",
    t3."INTERFPRIALLOW",
    t3."JUDGERXLEVWHENASSIGNHR",
    t3."LOADSHAREALLOW",
    t3."LOADSTATYPE",
    t3."LOOSESDCCHLOADTHRED",
    t3."LOWRXLEVOLFORBIDOPTSW",
    t3."LOWRXLEVOLFORBIDSWITCH",
    t3."MCPACHAPPOPT",
    t3."MCPALOWTRAFFICTH",
    t3."MCPAOPTALG",
    t3."MINRXLEVWHENASSIGNHR",
    t3."MTSTURNOFFALG",
    t3."MTSTURNOFFHYST",
    t3."MTSTURNOFFTH",
    t3."NAMRLFRMTRXALLOWED",
    t3."OUTAMRTCHHPRIORLOAD",
    t3."PWRPRIORALLOW",
    t3."QLENSD",
    t3."QLENSI",
    t3."QTRUDNPWRLASTTIME",
    t3."QTRUDNPWRSTATTIME",
    t3."QTRUPWRSHARE",
    t3."QUALHOPRIALLOW",
    NULL,
    t3."SSLENSD",
    t3."SSLENSI",
    t3."TCHBUSYTHRES",
    t3."TCHLOADOPTSWITCH",
    t3."TCHREQSUSPENDINTERVAL",
    t3."TCHTRIBUSYUNDERLAYTHR",
    t3."TCHTRICBUSYOVERLAYTHR",
    t3."TIGHTBCCHASSMAINBCCHLEV",
    t3."TIGHTBCCHASSMAINBCCHQUAL",
    t3."TIGHTSDCCHRXLEVTHRED",
    t3."TRXPRIALLOW",
    t3."TURNOFFLOADTYPE",
    t3."UPINTERFQUALLIMIT",
    t3."UPINTERLEVLIMIT",
    t3."UPRXLEVLASTTIME",
    t3."UPRXLEVSMOOTHPARA",
    t3."UPRXLEVSTATICTIME",
    t3."VAMOSAHSUSERDLSOFTBLOCKTHD",
    t3."WAITSDCCHIDLETIMER"
FROM
huawei_gexport_gsm."GCELLCHMGAD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AMRLOADOPTEN",
    t4."AMRTCHHPRIORALLOW",
    t4."AMRTCHHPRIORLOAD",
    t4."ASSOLRXLEVOFFSET",
    t4."BTRXPRIORITYSWITCH",
    t4."CELLID",
    t4."CELLOPPWRGRP",
    t4."CHALLOCATIONOPTSWITCH",
    t4."CHANINTERMESALLOW",
    t4."CHPWRINSUFFALLOWED",
    t4."CIRESTVALUE",
    t4."DLINTERFLEVLIMIT",
    t4."DLINTERFQUALLIMIT",
    t4."FREQLOADSHARETRAFFTHRSH",
    t4."HALFRATEREPACKINGSWITCH",
    t4."HISPRIOALLOW",
    t4."HOOLRXLEVOFFSET",
    t4."HRIUOLDRATESELALLOW",
    t4."HSCSDBUSYTHRES",
    t4."IBCAAFRSOFTBLKTHRD",
    t4."IBCAAHRSOFTBLKTHRD",
    t4."IBCAALLOWED",
    t4."IBCAASSWAITMEASURERPTTIME",
    t4."IBCACALLINFOFILTERLEN",
    t4."IBCACALLSOFTBLOCKTHOFFSET",
    t4."IBCACALLTARGETCIROFFSET",
    t4."IBCACIRESTENHANCE",
    t4."IBCADLPATHLOSSOFF",
    t4."IBCAEHOASSWAITMEASURERPTTIME",
    t4."IBCAESTMTSCCOLLISIONALLOW",
    t4."IBCAFLEXTSCALLOWED",
    t4."IBCAFORCEDBTSSYNCALLOWED",
    t4."IBCAFREEBCCHCHANTHRSHOLD",
    t4."IBCAFREVLOPT",
    t4."IBCAFRSOFTBLKTHRD",
    t4."IBCAGETINTFSRCOPT",
    t4."IBCAHOASSWAITMEASURERPTTIME",
    t4."IBCAHOSOFTBLKTHRESHOLD",
    t4."IBCAHRSOFTBLKTHRD",
    t4."IBCAICDMRELEVOFFSET",
    t4."IBCAICDMSWITCH",
    t4."IBCAINITPCRXLEVDLOFFSET",
    t4."IBCAINITPCRXLEVULOFFSET",
    t4."IBCAINITPCRXQUALDLOFFSET",
    t4."IBCAINITPCRXQUALULOFFSET",
    t4."IBCAIUOPATHLOSSOFF",
    t4."IBCAMAIOUSMTD",
    t4."IBCAMAXINTFSRCNUM",
    t4."IBCANCELLPATHLOSSESTIMATE",
    t4."IBCANEWCALLCIROFFSET",
    t4."IBCANHOASSWAITMEASURERPTTIME",
    t4."IBCANONMEANCELLSTATNUM",
    t4."IBCAOPRREVISEFACTOR",
    t4."IBCAPATHLOSSOFF",
    t4."IBCAPDCHDYNTRANTMR",
    t4."IBCAPDDYNTRENHANCE",
    t4."IBCAPLFILTFACTOR",
    t4."IBCAQUEUEOPT",
    t4."IBCASCELLPATHLOSS",
    t4."IBCASOFTBLKSAICOFF",
    t4."IBCASOFTBLKSWITCH",
    t4."IBCASUBCHNHANDOVERALLOWED",
    t4."IBCATARGETCIRTHRSH",
    t4."IBCAUSEDIUOSUBLAY",
    t4."IBCAUSRDYNCMEASURENCELL",
    t4."IBCAWAFRSOFTBLKTHRD",
    t4."INNAMRTCHHPRIORLOAD",
    t4."INTERFPRIALLOW",
    t4."JUDGERXLEVWHENASSIGNHR",
    t4."LOADSHAREALLOW",
    t4."LOADSTATYPE",
    t4."LOOSESDCCHLOADTHRED",
    t4."LOWRXLEVOLFORBIDOPTSW",
    t4."LOWRXLEVOLFORBIDSWITCH",
    t4."MCPACHAPPOPT",
    t4."MCPALOWTRAFFICTH",
    t4."MCPAOPTALG",
    t4."MINRXLEVWHENASSIGNHR",
    t4."MTSTURNOFFALG",
    t4."MTSTURNOFFHYST",
    t4."MTSTURNOFFTH",
    t4."NAMRLFRMTRXALLOWED",
    t4."OUTAMRTCHHPRIORLOAD",
    t4."PWRPRIORALLOW",
    t4."QLENSD",
    t4."QLENSI",
    t4."QTRUDNPWRLASTTIME",
    t4."QTRUDNPWRSTATTIME",
    t4."QTRUPWRSHARE",
    t4."QUALHOPRIALLOW",
    NULL,
    t4."SSLENSD",
    t4."SSLENSI",
    t4."TCHBUSYTHRES",
    t4."TCHLOADOPTSWITCH",
    t4."TCHREQSUSPENDINTERVAL",
    t4."TCHTRIBUSYUNDERLAYTHR",
    t4."TCHTRICBUSYOVERLAYTHR",
    t4."TIGHTBCCHASSMAINBCCHLEV",
    t4."TIGHTBCCHASSMAINBCCHQUAL",
    t4."TIGHTSDCCHRXLEVTHRED",
    t4."TRXPRIALLOW",
    t4."TURNOFFLOADTYPE",
    t4."UPINTERFQUALLIMIT",
    t4."UPINTERLEVLIMIT",
    t4."UPRXLEVLASTTIME",
    t4."UPRXLEVSMOOTHPARA",
    t4."UPRXLEVSTATICTIME",
    t4."VAMOSAHSUSERDLSOFTBLOCKTHD",
    t4."WAITSDCCHIDLETIMER"
FROM
huawei_mml_gsm."GCELLCHMGAD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCHMGBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLCHMGBASIC"',
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
    t1."ALLOWAMRHALFRATEUSERPERC",
    t1."ALLOWHALFRATEUSERPERC",
    t1."CELLID",
    t1."CELLMAXSD",
    t1."CHALLOCSTRATEGY",
    t1."DIFFBANDSDCCHDYNADJ",
    t1."DIFFBANDSDCCHUSINGOPTIMIZE",
    t1."DYNPBTSUPPORTED",
    t1."ENTCHADJALLOW",
    t1."FACTORYMODE",
    t1."GRADEACCALLOW",
    t1."HIGHPRIUSERQUALFIRST",
    t1."IDLESDTHRES",
    t1."IMMASSDIFFBANDALLOCTCHSW",
    t1."INTOCELLRESVCHANNUM",
    t1."MAINBCCHSDCCHNUM",
    t1."MINRESTIMETCH",
    t1."RSVCHMFORECNUM",
    t1."SDBACKTOTCHPUNISHSWITCH",
    t1."SDCCHDYNADJTSNUM",
    t1."SDDYNADJRSVTCHNUM",
    t1."SDDYNADJRSVTCHSWITCH",
    t1."TIGHTBCCHSWITCH"
FROM
huawei_nbi_gsm."GCELLCHMGBASIC" t1

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
    t2."ALLOWAMRHALFRATEUSERPERC",
    t2."ALLOWHALFRATEUSERPERC",
    t2."CELLID",
    t2."CELLMAXSD",
    t2."CHALLOCSTRATEGY",
    t2."DIFFBANDSDCCHDYNADJ",
    t2."DIFFBANDSDCCHUSINGOPTIMIZE",
    t2."DYNPBTSUPPORTED",
    t2."ENTCHADJALLOW",
    t2."FACTORYMODE",
    t2."GRADEACCALLOW",
    t2."HIGHPRIUSERQUALFIRST",
    t2."IDLESDTHRES",
    t2."IMMASSDIFFBANDALLOCTCHSW",
    t2."INTOCELLRESVCHANNUM",
    t2."MAINBCCHSDCCHNUM",
    t2."MINRESTIMETCH",
    t2."RSVCHMFORECNUM",
    t2."SDBACKTOTCHPUNISHSWITCH",
    t2."SDCCHDYNADJTSNUM",
    t2."SDDYNADJRSVTCHNUM",
    t2."SDDYNADJRSVTCHSWITCH",
    t2."TIGHTBCCHSWITCH"
FROM
huawei_gexport_gsm."GCELLCHMGBASIC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALLOWAMRHALFRATEUSERPERC",
    t3."ALLOWHALFRATEUSERPERC",
    t3."CELLID",
    t3."CELLMAXSD",
    t3."CHALLOCSTRATEGY",
    t3."DIFFBANDSDCCHDYNADJ",
    t3."DIFFBANDSDCCHUSINGOPTIMIZE",
    t3."DYNPBTSUPPORTED",
    t3."ENTCHADJALLOW",
    t3."FACTORYMODE",
    t3."GRADEACCALLOW",
    t3."HIGHPRIUSERQUALFIRST",
    t3."IDLESDTHRES",
    t3."IMMASSDIFFBANDALLOCTCHSW",
    t3."INTOCELLRESVCHANNUM",
    t3."MAINBCCHSDCCHNUM",
    t3."MINRESTIMETCH",
    t3."RSVCHMFORECNUM",
    t3."SDBACKTOTCHPUNISHSWITCH",
    t3."SDCCHDYNADJTSNUM",
    t3."SDDYNADJRSVTCHNUM",
    t3."SDDYNADJRSVTCHSWITCH",
    t3."TIGHTBCCHSWITCH"
FROM
huawei_gexport_gsm."GCELLCHMGBASIC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALLOWAMRHALFRATEUSERPERC",
    t4."ALLOWHALFRATEUSERPERC",
    t4."CELLID",
    t4."CELLMAXSD",
    t4."CHALLOCSTRATEGY",
    t4."DIFFBANDSDCCHDYNADJ",
    t4."DIFFBANDSDCCHUSINGOPTIMIZE",
    t4."DYNPBTSUPPORTED",
    t4."ENTCHADJALLOW",
    t4."FACTORYMODE",
    t4."GRADEACCALLOW",
    t4."HIGHPRIUSERQUALFIRST",
    t4."IDLESDTHRES",
    t4."IMMASSDIFFBANDALLOCTCHSW",
    t4."INTOCELLRESVCHANNUM",
    t4."MAINBCCHSDCCHNUM",
    t4."MINRESTIMETCH",
    t4."RSVCHMFORECNUM",
    t4."SDBACKTOTCHPUNISHSWITCH",
    t4."SDCCHDYNADJTSNUM",
    t4."SDDYNADJRSVTCHNUM",
    t4."SDDYNADJRSVTCHSWITCH",
    t4."TIGHTBCCHSWITCH"
FROM
huawei_mml_gsm."GCELLCHMGBASIC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCONGACALGO = ReplaceableObject(
    'huawei_cm_2g."GCELLCONGACALGO"',
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
    t1."IACCSW"
FROM
huawei_nbi_gsm."GCELLCONGACALGO" t1

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
    t2."IACCSW"
FROM
huawei_gexport_gsm."GCELLCONGACALGO_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IACCSW"
FROM
huawei_gexport_gsm."GCELLCONGACALGO_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IACCSW"
FROM
huawei_mml_gsm."GCELLCONGACALGO" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLCSFBPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLCSFBPARA"',
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
    t1."CSFBFASTRETURNBASECFGSW",
    t1."UFCSFBSTATINTERRANHO",
    t1."ULTRAFLASHCSFBSAILAC",
    t1."ULTRAFLASHCSFBSAIMCC",
    t1."ULTRAFLASHCSFBSAIMNC",
    t1."ULTRAFLASHCSFBSAISAC",
    t1."ULTRAFLASHCSFBSW"
FROM
huawei_nbi_gsm."GCELLCSFBPARA" t1

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
    t2."CSFBFASTRETURNBASECFGSW",
    t2."UFCSFBSTATINTERRANHO",
    t2."ULTRAFLASHCSFBSAILAC",
    t2."ULTRAFLASHCSFBSAIMCC",
    t2."ULTRAFLASHCSFBSAIMNC",
    t2."ULTRAFLASHCSFBSAISAC",
    t2."ULTRAFLASHCSFBSW"
FROM
huawei_gexport_gsm."GCELLCSFBPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CSFBFASTRETURNBASECFGSW",
    t3."UFCSFBSTATINTERRANHO",
    t3."ULTRAFLASHCSFBSAILAC",
    t3."ULTRAFLASHCSFBSAIMCC",
    t3."ULTRAFLASHCSFBSAIMNC",
    t3."ULTRAFLASHCSFBSAISAC",
    t3."ULTRAFLASHCSFBSW"
FROM
huawei_gexport_gsm."GCELLCSFBPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CSFBFASTRETURNBASECFGSW",
    t4."UFCSFBSTATINTERRANHO",
    t4."ULTRAFLASHCSFBSAILAC",
    t4."ULTRAFLASHCSFBSAIMCC",
    t4."ULTRAFLASHCSFBSAIMNC",
    t4."ULTRAFLASHCSFBSAISAC",
    t4."ULTRAFLASHCSFBSW"
FROM
huawei_mml_gsm."GCELLCSFBPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLDYNTURNOFF = ReplaceableObject(
    'huawei_cm_2g."GCELLDYNTURNOFF"',
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
    t1."TURNOFFENABLE",
    t1."PROTECTTIME",
    t1."SAMECVGCELLID",
    t1."SAMECVGCELLLOADSTATTM",
    t1."SAMECVGCELLLOADTHRD",
    t1."TURNOFFCELLCHANNUM",
    t1."TURNOFFCELLSTPTIME",
    t1."TURNOFFCELLSTRTIME",
    t1."TURNONCELLLOADTHRD"
FROM
huawei_nbi_gsm."GCELLDYNTURNOFF" t1

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
    t2."TURNOFFENABLE",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLDYNTURNOFF_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."TURNOFFENABLE",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLDYNTURNOFF_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TURNOFFENABLE",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELLDYNTURNOFF" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLEGPRSPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLEGPRSPARA"',
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
    t1."ADJUSTULMCSTYPE",
    t1."BEPPERIOD",
    t1."CELLID",
    t1."CHOOSEBEPMAP",
    t1."DLPRIORITYDEGRADEULMCS",
    t1."DNDEFAULTMCS",
    t1."DNE2ADEFAULTMCS",
    t1."DNE2AFIXMCS",
    t1."DNFIXMCS",
    t1."EGPRSDLIRLAFLTMODE",
    t1."ESTULONDLCHOOSECS",
    t1."LQCMODE",
    t1."MSREACTIONADJULMCSSW",
    t1."NODATAREPORTBEP",
    t1."SELECTCSMAP",
    t1."ULCVBEPDEGRADELEVEL",
    t1."ULFIRSTBLKCHANGECS",
    t1."ULLQCAUTOADJSW",
    t1."ULMEANBEPDEGRADELEVEL",
    t1."UPDEFAULTMCS",
    t1."UPE2ADEFAULTMCS",
    t1."UPE2AFIXMCS",
    t1."UPFIXMCS",
    t1."USEHISTORYCS"
FROM
huawei_nbi_gsm."GCELLEGPRSPARA" t1

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
    t2."ADJUSTULMCSTYPE",
    t2."BEPPERIOD",
    t2."CELLID",
    t2."CHOOSEBEPMAP",
    t2."DLPRIORITYDEGRADEULMCS",
    t2."DNDEFAULTMCS",
    t2."DNE2ADEFAULTMCS",
    t2."DNE2AFIXMCS",
    t2."DNFIXMCS",
    t2."EGPRSDLIRLAFLTMODE",
    t2."ESTULONDLCHOOSECS",
    t2."LQCMODE",
    t2."MSREACTIONADJULMCSSW",
    t2."NODATAREPORTBEP",
    t2."SELECTCSMAP",
    t2."ULCVBEPDEGRADELEVEL",
    t2."ULFIRSTBLKCHANGECS",
    t2."ULLQCAUTOADJSW",
    t2."ULMEANBEPDEGRADELEVEL",
    t2."UPDEFAULTMCS",
    t2."UPE2ADEFAULTMCS",
    t2."UPE2AFIXMCS",
    t2."UPFIXMCS",
    t2."USEHISTORYCS"
FROM
huawei_gexport_gsm."GCELLEGPRSPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADJUSTULMCSTYPE",
    t3."BEPPERIOD",
    t3."CELLID",
    t3."CHOOSEBEPMAP",
    t3."DLPRIORITYDEGRADEULMCS",
    t3."DNDEFAULTMCS",
    t3."DNE2ADEFAULTMCS",
    t3."DNE2AFIXMCS",
    t3."DNFIXMCS",
    t3."EGPRSDLIRLAFLTMODE",
    t3."ESTULONDLCHOOSECS",
    t3."LQCMODE",
    t3."MSREACTIONADJULMCSSW",
    t3."NODATAREPORTBEP",
    t3."SELECTCSMAP",
    t3."ULCVBEPDEGRADELEVEL",
    t3."ULFIRSTBLKCHANGECS",
    t3."ULLQCAUTOADJSW",
    t3."ULMEANBEPDEGRADELEVEL",
    t3."UPDEFAULTMCS",
    t3."UPE2ADEFAULTMCS",
    t3."UPE2AFIXMCS",
    t3."UPFIXMCS",
    t3."USEHISTORYCS"
FROM
huawei_gexport_gsm."GCELLEGPRSPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADJUSTULMCSTYPE",
    t4."BEPPERIOD",
    t4."CELLID",
    t4."CHOOSEBEPMAP",
    t4."DLPRIORITYDEGRADEULMCS",
    t4."DNDEFAULTMCS",
    t4."DNE2ADEFAULTMCS",
    t4."DNE2AFIXMCS",
    t4."DNFIXMCS",
    t4."EGPRSDLIRLAFLTMODE",
    t4."ESTULONDLCHOOSECS",
    t4."LQCMODE",
    t4."MSREACTIONADJULMCSSW",
    t4."NODATAREPORTBEP",
    t4."SELECTCSMAP",
    t4."ULCVBEPDEGRADELEVEL",
    t4."ULFIRSTBLKCHANGECS",
    t4."ULLQCAUTOADJSW",
    t4."ULMEANBEPDEGRADELEVEL",
    t4."UPDEFAULTMCS",
    t4."UPE2ADEFAULTMCS",
    t4."UPE2AFIXMCS",
    t4."UPFIXMCS",
    t4."USEHISTORYCS"
FROM
huawei_mml_gsm."GCELLEGPRSPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLEXTMSRPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLEXTMSRPARA"',
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
    t1."EXTMEASORD",
    t1."EXTRPTPERIOD",
    t1."EXTRPTTYPE",
    t1."INTFREQUENCY",
    t1."NCCPERMITED"
FROM
huawei_nbi_gsm."GCELLEXTMSRPARA" t1

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
    t2."EXTMEASORD",
    t2."EXTRPTPERIOD",
    t2."EXTRPTTYPE",
    t2."INTFREQUENCY",
    t2."NCCPERMITED"
FROM
huawei_gexport_gsm."GCELLEXTMSRPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."EXTMEASORD",
    t3."EXTRPTPERIOD",
    t3."EXTRPTTYPE",
    t3."INTFREQUENCY",
    t3."NCCPERMITED"
FROM
huawei_gexport_gsm."GCELLEXTMSRPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."EXTMEASORD",
    t4."EXTRPTPERIOD",
    t4."EXTRPTTYPE",
    t4."INTFREQUENCY",
    t4."NCCPERMITED"
FROM
huawei_mml_gsm."GCELLEXTMSRPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLFREQ = ReplaceableObject(
    'huawei_cm_2g."GCELLFREQ"',
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
    t1."FREQ1",
    t1."FREQ2",
    t1."FREQ3",
    t1."FREQ4",
    t1."FREQ5",
    t1."FREQ6",
    t1."FREQ7",
    t1."FREQ8",
    t1."FREQ9",
    t1."FREQ10",
    t1."FREQ11"
FROM
huawei_nbi_gsm."GCELLFREQ" t1

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
    t2."FREQ1",
    t2."FREQ2",
    t2."FREQ3",
    t2."FREQ4",
    t2."FREQ5",
    t2."FREQ6",
    t2."FREQ7",
    t2."FREQ8",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLFREQ_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FREQ1",
    t3."FREQ2",
    t3."FREQ3",
    t3."FREQ4",
    t3."FREQ5",
    t3."FREQ6",
    t3."FREQ7",
    t3."FREQ8",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLFREQ_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FREQ1",
    t4."FREQ2",
    t4."FREQ3",
    t4."FREQ4",
    t4."FREQ5",
    t4."FREQ6",
    t4."FREQ7",
    t4."FREQ8",
    t4."FREQ9",
    t4."FREQ10",
    t4."FREQ11"
FROM
huawei_mml_gsm."GCELLFREQ" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLFREQSCAN = ReplaceableObject(
    'huawei_cm_2g."GCELLFREQSCAN"',
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
    t1."FREQLST",
    t1."LOCGRPNO",
    t1."STRTM",
    t1."TIME"
FROM
huawei_nbi_gsm."GCELLFREQSCAN" t1

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
    t2."FREQLST",
    t2."LOCGRPNO",
    t2."STRTM",
    t2."TIME"
FROM
huawei_gexport_gsm."GCELLFREQSCAN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FREQLST",
    t3."LOCGRPNO",
    t3."STRTM",
    t3."TIME"
FROM
huawei_gexport_gsm."GCELLFREQSCAN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FREQLST",
    t4."LOCGRPNO",
    t4."STRTM",
    t4."TIME"
FROM
huawei_mml_gsm."GCELLFREQSCAN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLGPRS = ReplaceableObject(
    'huawei_cm_2g."GCELLGPRS"',
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
    t1."DLDCSPT",
    t1."EDGE",
    t1."EGPRS2A",
    t1."ENACCSPT",
    t1."ENC2SPT",
    t1."GPRS",
    t1."NACCSPT",
    t1."NC2SPT",
    t1."PKTSI",
    t1."PSPAGINGCTRL",
    t1."RA",
    t1."SPTDPI",
    t1."SPTINTERRATINBSCPSHO",
    t1."SPTINTERRATOUTBSCPSHO",
    t1."SPTLTEINBSCPSHO",
    t1."SPTLTEOUTBSCPSHO",
    t1."SPTREDUCELATENCY",
    t1."SUPPORTDTM",
    t1."SUPPORTEDA",
    t1."DPIPARATRANMODE"
FROM
huawei_nbi_gsm."GCELLGPRS" t1

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
    t2."DLDCSPT",
    t2."EDGE",
    t2."EGPRS2A",
    t2."ENACCSPT",
    t2."ENC2SPT",
    t2."GPRS",
    t2."NACCSPT",
    t2."NC2SPT",
    t2."PKTSI",
    t2."PSPAGINGCTRL",
    t2."RA",
    t2."SPTDPI",
    t2."SPTINTERRATINBSCPSHO",
    t2."SPTINTERRATOUTBSCPSHO",
    t2."SPTLTEINBSCPSHO",
    t2."SPTLTEOUTBSCPSHO",
    t2."SPTREDUCELATENCY",
    t2."SUPPORTDTM",
    t2."SUPPORTEDA",
    NULL
FROM
huawei_gexport_gsm."GCELLGPRS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DLDCSPT",
    t3."EDGE",
    t3."EGPRS2A",
    t3."ENACCSPT",
    t3."ENC2SPT",
    t3."GPRS",
    t3."NACCSPT",
    t3."NC2SPT",
    t3."PKTSI",
    t3."PSPAGINGCTRL",
    t3."RA",
    t3."SPTDPI",
    t3."SPTINTERRATINBSCPSHO",
    t3."SPTINTERRATOUTBSCPSHO",
    t3."SPTLTEINBSCPSHO",
    t3."SPTLTEOUTBSCPSHO",
    t3."SPTREDUCELATENCY",
    t3."SUPPORTDTM",
    t3."SUPPORTEDA",
    NULL
FROM
huawei_gexport_gsm."GCELLGPRS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DLDCSPT",
    t4."EDGE",
    t4."EGPRS2A",
    t4."ENACCSPT",
    t4."ENC2SPT",
    t4."GPRS",
    t4."NACCSPT",
    t4."NC2SPT",
    t4."PKTSI",
    t4."PSPAGINGCTRL",
    t4."RA",
    t4."SPTDPI",
    t4."SPTINTERRATINBSCPSHO",
    t4."SPTINTERRATOUTBSCPSHO",
    t4."SPTLTEINBSCPSHO",
    t4."SPTLTEOUTBSCPSHO",
    t4."SPTREDUCELATENCY",
    t4."SUPPORTDTM",
    t4."SUPPORTEDA",
    NULL
FROM
huawei_mml_gsm."GCELLGPRS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLGSMR = ReplaceableObject(
    'huawei_cm_2g."GCELLGSMR"',
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
    t1."CRMSGRESENDINT",
    t1."CRMSGRESENDNUM",
    t1."DLTESTRESENDINT",
    t1."DLTESTRESENDNUM",
    t1."DTRTYPE",
    t1."EMLPPPRIORITY",
    t1."FACCHRESENDINT",
    t1."FACCHSENDNOTMSGIND",
    t1."FACCHSENDPGMSGIND",
    t1."GCSCHNASSULCHNEN",
    t1."GCSIMPREEMPTIONEN",
    t1."GSMRCSSENDNOTIFMODE",
    t1."GSMRPSSENDNOTIFMODE",
    t1."NCHOCBLOCKNUM",
    t1."NCHSTARTBLOCK",
    t1."NY2",
    t1."SENDFACCHNOTPRI",
    t1."SENDFACCHPAGPRI",
    t1."T3115",
    t1."TALKERINFINT",
    t1."UIC",
    t1."VGCSMAXNUM",
    t1."VGCSPREEMPT",
    t1."VGCSRSRVNUM"
FROM
huawei_nbi_gsm."GCELLGSMR" t1

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
    t2."CRMSGRESENDINT",
    t2."CRMSGRESENDNUM",
    t2."DLTESTRESENDINT",
    t2."DLTESTRESENDNUM",
    t2."DTRTYPE",
    t2."EMLPPPRIORITY",
    t2."FACCHRESENDINT",
    t2."FACCHSENDNOTMSGIND",
    t2."FACCHSENDPGMSGIND",
    t2."GCSCHNASSULCHNEN",
    t2."GCSIMPREEMPTIONEN",
    t2."GSMRCSSENDNOTIFMODE",
    t2."GSMRPSSENDNOTIFMODE",
    t2."NCHOCBLOCKNUM",
    t2."NCHSTARTBLOCK",
    t2."NY2",
    t2."SENDFACCHNOTPRI",
    t2."SENDFACCHPAGPRI",
    t2."T3115",
    t2."TALKERINFINT",
    t2."UIC",
    t2."VGCSMAXNUM",
    t2."VGCSPREEMPT",
    t2."VGCSRSRVNUM"
FROM
huawei_gexport_gsm."GCELLGSMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CRMSGRESENDINT",
    t3."CRMSGRESENDNUM",
    t3."DLTESTRESENDINT",
    t3."DLTESTRESENDNUM",
    t3."DTRTYPE",
    t3."EMLPPPRIORITY",
    t3."FACCHRESENDINT",
    t3."FACCHSENDNOTMSGIND",
    t3."FACCHSENDPGMSGIND",
    t3."GCSCHNASSULCHNEN",
    t3."GCSIMPREEMPTIONEN",
    t3."GSMRCSSENDNOTIFMODE",
    t3."GSMRPSSENDNOTIFMODE",
    t3."NCHOCBLOCKNUM",
    t3."NCHSTARTBLOCK",
    t3."NY2",
    t3."SENDFACCHNOTPRI",
    t3."SENDFACCHPAGPRI",
    t3."T3115",
    t3."TALKERINFINT",
    t3."UIC",
    t3."VGCSMAXNUM",
    t3."VGCSPREEMPT",
    t3."VGCSRSRVNUM"
FROM
huawei_gexport_gsm."GCELLGSMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CRMSGRESENDINT",
    t4."CRMSGRESENDNUM",
    t4."DLTESTRESENDINT",
    t4."DLTESTRESENDNUM",
    t4."DTRTYPE",
    t4."EMLPPPRIORITY",
    t4."FACCHRESENDINT",
    t4."FACCHSENDNOTMSGIND",
    t4."FACCHSENDPGMSGIND",
    t4."GCSCHNASSULCHNEN",
    t4."GCSIMPREEMPTIONEN",
    t4."GSMRCSSENDNOTIFMODE",
    t4."GSMRPSSENDNOTIFMODE",
    t4."NCHOCBLOCKNUM",
    t4."NCHSTARTBLOCK",
    t4."NY2",
    t4."SENDFACCHNOTPRI",
    t4."SENDFACCHPAGPRI",
    t4."T3115",
    t4."TALKERINFINT",
    t4."UIC",
    t4."VGCSMAXNUM",
    t4."VGCSPREEMPT",
    t4."VGCSRSRVNUM"
FROM
huawei_mml_gsm."GCELLGSMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHO2GBA2 = ReplaceableObject(
    'huawei_cm_2g."GCELLHO2GBA2"',
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
    t1."CELL2GBA2BCCH",
    t1."CELL2GBA2OPTSW",
    t1."CELL2GBA2TAG",
    t1."CELLID",
    t1."ITEM",
    t1."ITEMVALID",
    t1."CELL2GBA2OPTENHSW"
FROM
huawei_nbi_gsm."GCELLHO2GBA2" t1

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
    t2."CELL2GBA2OPTSW",
    t2."CELL2GBA2TAG",
    t2."CELLID",
    t2."ITEM",
    t2."ITEMVALID",
    NULL
FROM
huawei_gexport_gsm."GCELLHO2GBA2_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CELL2GBA2OPTSW",
    t3."CELL2GBA2TAG",
    t3."CELLID",
    t3."ITEM",
    t3."ITEMVALID",
    NULL
FROM
huawei_gexport_gsm."GCELLHO2GBA2_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CELL2GBA2BCCH",
    t4."CELL2GBA2OPTSW",
    t4."CELL2GBA2TAG",
    t4."CELLID",
    t4."ITEM",
    t4."ITEMVALID",
    NULL
FROM
huawei_mml_gsm."GCELLHO2GBA2" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOAD = ReplaceableObject(
    'huawei_cm_2g."GCELLHOAD"',
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
    t1."ABCDOWNQUALITY",
    t1."ABCUPQUALITY",
    t1."ABCWAITMAXTIME",
    t1."ACCTHRESLAYER",
    t1."ASSIGNBETTERCELLEN",
    t1."BANTIME",
    t1."CELLID",
    t1."CONTINTV",
    t1."HOTRYCNT",
    t1."INTERFEREDLEVOFF",
    t1."INTERFEREDLEVOFFOL",
    t1."INTERFEREDLQUALOFFOL",
    t1."INTERFEREDQUALOFF",
    t1."INTERFEREULEVOFF",
    t1."INTERFEREULEVOFFOL",
    t1."INTERFEREULQUALOFFOL",
    t1."INTERFEREUQUALOFF",
    t1."INTERFEROFFSWITCHOL",
    t1."KBIAS",
    t1."LAYHOLOADTH",
    t1."LOADACCTHRES",
    t1."LOADHOAD",
    t1."LOADHOHYSTADAPEN",
    t1."LOADHOPERIOD",
    t1."LOADHOSTEP",
    t1."LOADHOUSRRATIO",
    t1."LOADOFFSET",
    t1."MAXCNTNUM",
    t1."MAXRESEND",
    t1."OUTBSCLOADHOEN",
    t1."QCKSTATCNT",
    t1."QCKTIMETH",
    t1."QCKTRUECNT",
    t1."SDCCHWAITMREN",
    t1."SDCCHWAITMRTIMELEN",
    t1."SPEEDPUNISH",
    t1."SPEEDPUNISHT",
    t1."SYSFLOWLEV",
    t1."T3105",
    t1."TIGHTBCCHHOLOADTHRES",
    t1."TIGHTBCCHRXQUALTHRES",
    t1."TRIGTHRES",
    t1."TRIGTHRESLAYER"
FROM
huawei_nbi_gsm."GCELLHOAD" t1

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
    t2."ABCDOWNQUALITY",
    t2."ABCUPQUALITY",
    t2."ABCWAITMAXTIME",
    t2."ACCTHRESLAYER",
    t2."ASSIGNBETTERCELLEN",
    t2."BANTIME",
    t2."CELLID",
    t2."CONTINTV",
    t2."HOTRYCNT",
    t2."INTERFEREDLEVOFF",
    t2."INTERFEREDLEVOFFOL",
    t2."INTERFEREDLQUALOFFOL",
    t2."INTERFEREDQUALOFF",
    t2."INTERFEREULEVOFF",
    t2."INTERFEREULEVOFFOL",
    t2."INTERFEREULQUALOFFOL",
    t2."INTERFEREUQUALOFF",
    t2."INTERFEROFFSWITCHOL",
    t2."KBIAS",
    t2."LAYHOLOADTH",
    t2."LOADACCTHRES",
    t2."LOADHOAD",
    t2."LOADHOHYSTADAPEN",
    t2."LOADHOPERIOD",
    t2."LOADHOSTEP",
    t2."LOADHOUSRRATIO",
    t2."LOADOFFSET",
    t2."MAXCNTNUM",
    t2."MAXRESEND",
    t2."OUTBSCLOADHOEN",
    t2."QCKSTATCNT",
    t2."QCKTIMETH",
    t2."QCKTRUECNT",
    t2."SDCCHWAITMREN",
    t2."SDCCHWAITMRTIMELEN",
    t2."SPEEDPUNISH",
    t2."SPEEDPUNISHT",
    t2."SYSFLOWLEV",
    t2."T3105",
    t2."TIGHTBCCHHOLOADTHRES",
    t2."TIGHTBCCHRXQUALTHRES",
    t2."TRIGTHRES",
    t2."TRIGTHRESLAYER"
FROM
huawei_gexport_gsm."GCELLHOAD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABCDOWNQUALITY",
    t3."ABCUPQUALITY",
    t3."ABCWAITMAXTIME",
    t3."ACCTHRESLAYER",
    t3."ASSIGNBETTERCELLEN",
    t3."BANTIME",
    t3."CELLID",
    t3."CONTINTV",
    t3."HOTRYCNT",
    t3."INTERFEREDLEVOFF",
    t3."INTERFEREDLEVOFFOL",
    t3."INTERFEREDLQUALOFFOL",
    t3."INTERFEREDQUALOFF",
    t3."INTERFEREULEVOFF",
    t3."INTERFEREULEVOFFOL",
    t3."INTERFEREULQUALOFFOL",
    t3."INTERFEREUQUALOFF",
    t3."INTERFEROFFSWITCHOL",
    t3."KBIAS",
    t3."LAYHOLOADTH",
    t3."LOADACCTHRES",
    t3."LOADHOAD",
    t3."LOADHOHYSTADAPEN",
    t3."LOADHOPERIOD",
    t3."LOADHOSTEP",
    t3."LOADHOUSRRATIO",
    t3."LOADOFFSET",
    t3."MAXCNTNUM",
    t3."MAXRESEND",
    t3."OUTBSCLOADHOEN",
    t3."QCKSTATCNT",
    t3."QCKTIMETH",
    t3."QCKTRUECNT",
    t3."SDCCHWAITMREN",
    t3."SDCCHWAITMRTIMELEN",
    t3."SPEEDPUNISH",
    t3."SPEEDPUNISHT",
    t3."SYSFLOWLEV",
    t3."T3105",
    t3."TIGHTBCCHHOLOADTHRES",
    t3."TIGHTBCCHRXQUALTHRES",
    t3."TRIGTHRES",
    t3."TRIGTHRESLAYER"
FROM
huawei_gexport_gsm."GCELLHOAD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABCDOWNQUALITY",
    t4."ABCUPQUALITY",
    t4."ABCWAITMAXTIME",
    t4."ACCTHRESLAYER",
    t4."ASSIGNBETTERCELLEN",
    t4."BANTIME",
    t4."CELLID",
    t4."CONTINTV",
    t4."HOTRYCNT",
    t4."INTERFEREDLEVOFF",
    t4."INTERFEREDLEVOFFOL",
    t4."INTERFEREDLQUALOFFOL",
    t4."INTERFEREDQUALOFF",
    t4."INTERFEREULEVOFF",
    t4."INTERFEREULEVOFFOL",
    t4."INTERFEREULQUALOFFOL",
    t4."INTERFEREUQUALOFF",
    t4."INTERFEROFFSWITCHOL",
    t4."KBIAS",
    t4."LAYHOLOADTH",
    t4."LOADACCTHRES",
    t4."LOADHOAD",
    t4."LOADHOHYSTADAPEN",
    t4."LOADHOPERIOD",
    t4."LOADHOSTEP",
    t4."LOADHOUSRRATIO",
    t4."LOADOFFSET",
    t4."MAXCNTNUM",
    t4."MAXRESEND",
    t4."OUTBSCLOADHOEN",
    t4."QCKSTATCNT",
    t4."QCKTIMETH",
    t4."QCKTRUECNT",
    t4."SDCCHWAITMREN",
    t4."SDCCHWAITMRTIMELEN",
    t4."SPEEDPUNISH",
    t4."SPEEDPUNISHT",
    t4."SYSFLOWLEV",
    t4."T3105",
    t4."TIGHTBCCHHOLOADTHRES",
    t4."TIGHTBCCHRXQUALTHRES",
    t4."TRIGTHRES",
    t4."TRIGTHRESLAYER"
FROM
huawei_mml_gsm."GCELLHOAD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLHOBASIC"',
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
    t1."AMRF2HHOQUALTHFINE",
    t1."AMRFULLTOHALFHOALLOW",
    t1."AMRFULLTOHALFHOATCBADJSTEP",
    t1."AMRFULLTOHALFHOATCBTHRESH",
    t1."AMRFULLTOHALFHOPATHADJSTEP",
    t1."AMRFULLTOHALFHOPATHTHRESH",
    t1."AMRFULLTOHALFHOQUALTHRESH",
    t1."AMRFULLTOHALFHOTHRESH",
    t1."AMRH2FHOOPTSW",
    t1."AMRH2FHOQUALFINE",
    t1."AMRHALFTOFULLHOATCBTHRESH",
    t1."AMRHALFTOFULLHOPATHTHRESH",
    t1."AMRHALFTOFULLHOQUALALLOW",
    t1."AMRHALFTOFULLHOQUALTHRESH",
    t1."AMRHALFTOFULLHOTHRESH",
    t1."ATCBHOEN",
    t1."BADQUALHOOPTALLOW",
    t1."BQHOEN",
    t1."CELLID",
    t1."COBSCMSCADJEN",
    t1."CONHOEN",
    t1."DLEDGETHRES",
    t1."EDGEHOHYSTEN",
    t1."EDGELAST1",
    t1."EDGESTAT1",
    t1."EDOUTHOADEN",
    t1."F2HHOLOADSTFSWITCH",
    t1."FHGAINOFFSET",
    t1."FRINGEHOEN",
    t1."FULLTOHALFHOATCBOFFSET",
    t1."FULLTOHALFHODURATION",
    t1."FULLTOHALFHOLASTTIME",
    t1."FULLTOHALFHOLOADSTF",
    t1."FULLTOHALFHOPATHOFFSET",
    t1."FULLTOHALFHOPERIOD",
    t1."FULLTOHALFHOSTATTIME",
    t1."HALFTOFULLATCBOFFSET",
    t1."HALFTOFULLHODURATION",
    t1."HALFTOFULLHOLASTTIME",
    t1."HALFTOFULLHOPATHOFFSET",
    t1."HALFTOFULLHOSTATTIME",
    t1."HOCDCMINDWPWR",
    t1."HOCDCMINUPPWR",
    t1."HOCDCOVERLODEHOEN",
    t1."HOCTRLSWITCH",
    t1."HOPRIOMODEN",
    t1."HOTHRES",
    t1."INFHHOLAST",
    t1."INFHHOSTAT",
    t1."INHOF2HTH",
    t1."INHOH2FTH",
    t1."INTERFHOEN",
    t1."INTERHOOPTALLOW",
    t1."INTERRATCELLRESELEN",
    t1."INTERRATDIFFPROCSW",
    t1."INTERRATINBSCHOEN",
    t1."INTERRATIURGINBSCHOEN",
    t1."INTERRATIURGVOICECARRYEN",
    t1."INTERRATOUTBSCHOEN",
    t1."INTRACELLFHHOEN",
    t1."INTRACELLFHOPTSWITCH",
    t1."INTRACELLHOEN",
    t1."INTRACELLSINUSEREN",
    t1."LEVHOEN",
    t1."LEVHOHYST",
    t1."LOADHOEN",
    t1."LTECELLRESELEN",
    t1."LTESAILAC",
    t1."LTESAIMCC",
    t1."LTESAIMNC",
    t1."LTESAISAC",
    t1."MRINTRPLOPTSWITCH",
    t1."NOAMRF2HHOQUALTHFINE",
    t1."NOAMRFULLTOHALFHOALLOW",
    t1."NOAMRFULLTOHALFHOATCBADJSTEP",
    t1."NOAMRFULLTOHALFHOATCBTHRESH",
    t1."NOAMRFULLTOHALFHOPATHADJSTEP",
    t1."NOAMRFULLTOHALFHOPATHTHRESH",
    t1."NOAMRFULLTOHALFHOQUALTHRESH",
    t1."NOAMRFULLTOHALFTHRESH",
    t1."NOAMRH2FHOQUALFINE",
    t1."NOAMRHALFTOFULLHOATCBTHRESH",
    t1."NOAMRHALFTOFULLHOPATHTHRESH",
    t1."NOAMRHALFTOFULLHOQUALALLOW",
    t1."NOAMRHALFTOFULLHOQUALTHRESH",
    t1."NOAMRHALFTOFULLTHRESH",
    t1."PBGTHOEN",
    t1."QCKMVHOEN",
    t1."QUICKHOEN",
    t1."QUICKPBGTHOEN",
    t1."RXQCKFALLHOEN",
    t1."SIGCHANHOEN",
    t1."SRVCCHOEN",
    t1."TAHOEN",
    t1."TIGHTBCCHHOLASTTIME",
    t1."TIGHTBCCHHOSTATTIME",
    t1."ULEDGETHRES",
    t1."ULMCRITOPTSW",
    t1."BETTERCELLHOEN",
    t1."EDGELAST",
    t1."EDGESTAT",
    t1."INTERFERELASTTIME",
    t1."INTERFERESTATTIME",
    t1."PATHLOSSHOEN"
FROM
huawei_nbi_gsm."GCELLHOBASIC" t1

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
    t2."AMRF2HHOQUALTHFINE",
    t2."AMRFULLTOHALFHOALLOW",
    t2."AMRFULLTOHALFHOATCBADJSTEP",
    t2."AMRFULLTOHALFHOATCBTHRESH",
    t2."AMRFULLTOHALFHOPATHADJSTEP",
    t2."AMRFULLTOHALFHOPATHTHRESH",
    t2."AMRFULLTOHALFHOQUALTHRESH",
    t2."AMRFULLTOHALFHOTHRESH",
    t2."AMRH2FHOOPTSW",
    t2."AMRH2FHOQUALFINE",
    t2."AMRHALFTOFULLHOATCBTHRESH",
    t2."AMRHALFTOFULLHOPATHTHRESH",
    t2."AMRHALFTOFULLHOQUALALLOW",
    t2."AMRHALFTOFULLHOQUALTHRESH",
    t2."AMRHALFTOFULLHOTHRESH",
    t2."ATCBHOEN",
    t2."BADQUALHOOPTALLOW",
    t2."BQHOEN",
    t2."CELLID",
    t2."COBSCMSCADJEN",
    t2."CONHOEN",
    t2."DLEDGETHRES",
    t2."EDGEHOHYSTEN",
    t2."EDGELAST1",
    t2."EDGESTAT1",
    t2."EDOUTHOADEN",
    t2."F2HHOLOADSTFSWITCH",
    t2."FHGAINOFFSET",
    t2."FRINGEHOEN",
    t2."FULLTOHALFHOATCBOFFSET",
    t2."FULLTOHALFHODURATION",
    t2."FULLTOHALFHOLASTTIME",
    t2."FULLTOHALFHOLOADSTF",
    t2."FULLTOHALFHOPATHOFFSET",
    t2."FULLTOHALFHOPERIOD",
    t2."FULLTOHALFHOSTATTIME",
    t2."HALFTOFULLATCBOFFSET",
    t2."HALFTOFULLHODURATION",
    t2."HALFTOFULLHOLASTTIME",
    t2."HALFTOFULLHOPATHOFFSET",
    t2."HALFTOFULLHOSTATTIME",
    t2."HOCDCMINDWPWR",
    t2."HOCDCMINUPPWR",
    t2."HOCDCOVERLODEHOEN",
    t2."HOCTRLSWITCH",
    t2."HOPRIOMODEN",
    t2."HOTHRES",
    t2."INFHHOLAST",
    t2."INFHHOSTAT",
    t2."INHOF2HTH",
    t2."INHOH2FTH",
    t2."INTERFHOEN",
    t2."INTERHOOPTALLOW",
    t2."INTERRATCELLRESELEN",
    t2."INTERRATDIFFPROCSW",
    t2."INTERRATINBSCHOEN",
    t2."INTERRATIURGINBSCHOEN",
    t2."INTERRATIURGVOICECARRYEN",
    t2."INTERRATOUTBSCHOEN",
    t2."INTRACELLFHHOEN",
    t2."INTRACELLFHOPTSWITCH",
    t2."INTRACELLHOEN",
    t2."INTRACELLSINUSEREN",
    t2."LEVHOEN",
    t2."LEVHOHYST",
    t2."LOADHOEN",
    t2."LTECELLRESELEN",
    t2."LTESAILAC",
    t2."LTESAIMCC",
    t2."LTESAIMNC",
    t2."LTESAISAC",
    t2."MRINTRPLOPTSWITCH",
    t2."NOAMRF2HHOQUALTHFINE",
    t2."NOAMRFULLTOHALFHOALLOW",
    t2."NOAMRFULLTOHALFHOATCBADJSTEP",
    t2."NOAMRFULLTOHALFHOATCBTHRESH",
    t2."NOAMRFULLTOHALFHOPATHADJSTEP",
    t2."NOAMRFULLTOHALFHOPATHTHRESH",
    t2."NOAMRFULLTOHALFHOQUALTHRESH",
    t2."NOAMRFULLTOHALFTHRESH",
    t2."NOAMRH2FHOQUALFINE",
    t2."NOAMRHALFTOFULLHOATCBTHRESH",
    t2."NOAMRHALFTOFULLHOPATHTHRESH",
    t2."NOAMRHALFTOFULLHOQUALALLOW",
    t2."NOAMRHALFTOFULLHOQUALTHRESH",
    t2."NOAMRHALFTOFULLTHRESH",
    t2."PBGTHOEN",
    t2."QCKMVHOEN",
    t2."QUICKHOEN",
    t2."QUICKPBGTHOEN",
    t2."RXQCKFALLHOEN",
    t2."SIGCHANHOEN",
    t2."SRVCCHOEN",
    t2."TAHOEN",
    t2."TIGHTBCCHHOLASTTIME",
    t2."TIGHTBCCHHOSTATTIME",
    t2."ULEDGETHRES",
    t2."ULMCRITOPTSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLHOBASIC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AMRF2HHOQUALTHFINE",
    t3."AMRFULLTOHALFHOALLOW",
    t3."AMRFULLTOHALFHOATCBADJSTEP",
    t3."AMRFULLTOHALFHOATCBTHRESH",
    t3."AMRFULLTOHALFHOPATHADJSTEP",
    t3."AMRFULLTOHALFHOPATHTHRESH",
    t3."AMRFULLTOHALFHOQUALTHRESH",
    t3."AMRFULLTOHALFHOTHRESH",
    t3."AMRH2FHOOPTSW",
    t3."AMRH2FHOQUALFINE",
    t3."AMRHALFTOFULLHOATCBTHRESH",
    t3."AMRHALFTOFULLHOPATHTHRESH",
    t3."AMRHALFTOFULLHOQUALALLOW",
    t3."AMRHALFTOFULLHOQUALTHRESH",
    t3."AMRHALFTOFULLHOTHRESH",
    t3."ATCBHOEN",
    t3."BADQUALHOOPTALLOW",
    t3."BQHOEN",
    t3."CELLID",
    t3."COBSCMSCADJEN",
    t3."CONHOEN",
    t3."DLEDGETHRES",
    t3."EDGEHOHYSTEN",
    t3."EDGELAST1",
    t3."EDGESTAT1",
    t3."EDOUTHOADEN",
    t3."F2HHOLOADSTFSWITCH",
    t3."FHGAINOFFSET",
    t3."FRINGEHOEN",
    t3."FULLTOHALFHOATCBOFFSET",
    t3."FULLTOHALFHODURATION",
    t3."FULLTOHALFHOLASTTIME",
    t3."FULLTOHALFHOLOADSTF",
    t3."FULLTOHALFHOPATHOFFSET",
    t3."FULLTOHALFHOPERIOD",
    t3."FULLTOHALFHOSTATTIME",
    t3."HALFTOFULLATCBOFFSET",
    t3."HALFTOFULLHODURATION",
    t3."HALFTOFULLHOLASTTIME",
    t3."HALFTOFULLHOPATHOFFSET",
    t3."HALFTOFULLHOSTATTIME",
    t3."HOCDCMINDWPWR",
    t3."HOCDCMINUPPWR",
    t3."HOCDCOVERLODEHOEN",
    t3."HOCTRLSWITCH",
    t3."HOPRIOMODEN",
    t3."HOTHRES",
    t3."INFHHOLAST",
    t3."INFHHOSTAT",
    t3."INHOF2HTH",
    t3."INHOH2FTH",
    t3."INTERFHOEN",
    t3."INTERHOOPTALLOW",
    t3."INTERRATCELLRESELEN",
    t3."INTERRATDIFFPROCSW",
    t3."INTERRATINBSCHOEN",
    t3."INTERRATIURGINBSCHOEN",
    t3."INTERRATIURGVOICECARRYEN",
    t3."INTERRATOUTBSCHOEN",
    t3."INTRACELLFHHOEN",
    t3."INTRACELLFHOPTSWITCH",
    t3."INTRACELLHOEN",
    t3."INTRACELLSINUSEREN",
    t3."LEVHOEN",
    t3."LEVHOHYST",
    t3."LOADHOEN",
    t3."LTECELLRESELEN",
    t3."LTESAILAC",
    t3."LTESAIMCC",
    t3."LTESAIMNC",
    t3."LTESAISAC",
    t3."MRINTRPLOPTSWITCH",
    t3."NOAMRF2HHOQUALTHFINE",
    t3."NOAMRFULLTOHALFHOALLOW",
    t3."NOAMRFULLTOHALFHOATCBADJSTEP",
    t3."NOAMRFULLTOHALFHOATCBTHRESH",
    t3."NOAMRFULLTOHALFHOPATHADJSTEP",
    t3."NOAMRFULLTOHALFHOPATHTHRESH",
    t3."NOAMRFULLTOHALFHOQUALTHRESH",
    t3."NOAMRFULLTOHALFTHRESH",
    t3."NOAMRH2FHOQUALFINE",
    t3."NOAMRHALFTOFULLHOATCBTHRESH",
    t3."NOAMRHALFTOFULLHOPATHTHRESH",
    t3."NOAMRHALFTOFULLHOQUALALLOW",
    t3."NOAMRHALFTOFULLHOQUALTHRESH",
    t3."NOAMRHALFTOFULLTHRESH",
    t3."PBGTHOEN",
    t3."QCKMVHOEN",
    t3."QUICKHOEN",
    t3."QUICKPBGTHOEN",
    t3."RXQCKFALLHOEN",
    t3."SIGCHANHOEN",
    t3."SRVCCHOEN",
    t3."TAHOEN",
    t3."TIGHTBCCHHOLASTTIME",
    t3."TIGHTBCCHHOSTATTIME",
    t3."ULEDGETHRES",
    t3."ULMCRITOPTSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLHOBASIC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AMRF2HHOQUALTHFINE",
    t4."AMRFULLTOHALFHOALLOW",
    t4."AMRFULLTOHALFHOATCBADJSTEP",
    t4."AMRFULLTOHALFHOATCBTHRESH",
    t4."AMRFULLTOHALFHOPATHADJSTEP",
    t4."AMRFULLTOHALFHOPATHTHRESH",
    t4."AMRFULLTOHALFHOQUALTHRESH",
    t4."AMRFULLTOHALFHOTHRESH",
    t4."AMRH2FHOOPTSW",
    t4."AMRH2FHOQUALFINE",
    t4."AMRHALFTOFULLHOATCBTHRESH",
    t4."AMRHALFTOFULLHOPATHTHRESH",
    t4."AMRHALFTOFULLHOQUALALLOW",
    t4."AMRHALFTOFULLHOQUALTHRESH",
    t4."AMRHALFTOFULLHOTHRESH",
    t4."ATCBHOEN",
    t4."BADQUALHOOPTALLOW",
    t4."BQHOEN",
    t4."CELLID",
    t4."COBSCMSCADJEN",
    t4."CONHOEN",
    t4."DLEDGETHRES",
    t4."EDGEHOHYSTEN",
    t4."EDGELAST1",
    t4."EDGESTAT1",
    t4."EDOUTHOADEN",
    t4."F2HHOLOADSTFSWITCH",
    t4."FHGAINOFFSET",
    t4."FRINGEHOEN",
    t4."FULLTOHALFHOATCBOFFSET",
    t4."FULLTOHALFHODURATION",
    t4."FULLTOHALFHOLASTTIME",
    t4."FULLTOHALFHOLOADSTF",
    t4."FULLTOHALFHOPATHOFFSET",
    t4."FULLTOHALFHOPERIOD",
    t4."FULLTOHALFHOSTATTIME",
    t4."HALFTOFULLATCBOFFSET",
    t4."HALFTOFULLHODURATION",
    t4."HALFTOFULLHOLASTTIME",
    t4."HALFTOFULLHOPATHOFFSET",
    t4."HALFTOFULLHOSTATTIME",
    t4."HOCDCMINDWPWR",
    t4."HOCDCMINUPPWR",
    t4."HOCDCOVERLODEHOEN",
    t4."HOCTRLSWITCH",
    t4."HOPRIOMODEN",
    t4."HOTHRES",
    t4."INFHHOLAST",
    t4."INFHHOSTAT",
    t4."INHOF2HTH",
    t4."INHOH2FTH",
    t4."INTERFHOEN",
    t4."INTERHOOPTALLOW",
    t4."INTERRATCELLRESELEN",
    t4."INTERRATDIFFPROCSW",
    t4."INTERRATINBSCHOEN",
    t4."INTERRATIURGINBSCHOEN",
    t4."INTERRATIURGVOICECARRYEN",
    t4."INTERRATOUTBSCHOEN",
    t4."INTRACELLFHHOEN",
    t4."INTRACELLFHOPTSWITCH",
    t4."INTRACELLHOEN",
    t4."INTRACELLSINUSEREN",
    t4."LEVHOEN",
    t4."LEVHOHYST",
    t4."LOADHOEN",
    t4."LTECELLRESELEN",
    t4."LTESAILAC",
    t4."LTESAIMCC",
    t4."LTESAIMNC",
    t4."LTESAISAC",
    t4."MRINTRPLOPTSWITCH",
    t4."NOAMRF2HHOQUALTHFINE",
    t4."NOAMRFULLTOHALFHOALLOW",
    t4."NOAMRFULLTOHALFHOATCBADJSTEP",
    t4."NOAMRFULLTOHALFHOATCBTHRESH",
    t4."NOAMRFULLTOHALFHOPATHADJSTEP",
    t4."NOAMRFULLTOHALFHOPATHTHRESH",
    t4."NOAMRFULLTOHALFHOQUALTHRESH",
    t4."NOAMRFULLTOHALFTHRESH",
    t4."NOAMRH2FHOQUALFINE",
    t4."NOAMRHALFTOFULLHOATCBTHRESH",
    t4."NOAMRHALFTOFULLHOPATHTHRESH",
    t4."NOAMRHALFTOFULLHOQUALALLOW",
    t4."NOAMRHALFTOFULLHOQUALTHRESH",
    t4."NOAMRHALFTOFULLTHRESH",
    t4."PBGTHOEN",
    t4."QCKMVHOEN",
    t4."QUICKHOEN",
    t4."QUICKPBGTHOEN",
    t4."RXQCKFALLHOEN",
    t4."SIGCHANHOEN",
    t4."SRVCCHOEN",
    t4."TAHOEN",
    t4."TIGHTBCCHHOLASTTIME",
    t4."TIGHTBCCHHOSTATTIME",
    t4."ULEDGETHRES",
    t4."ULMCRITOPTSW",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELLHOBASIC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOCTRL = ReplaceableObject(
    'huawei_cm_2g."GCELLHOCTRL"',
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
    t1."BCCHHOPHOCOMPOPT",
    t1."BSMSPWRLEV",
    t1."BTSMESRPTPREPROC",
    t1."CELLID",
    t1."CONTHOMININTV",
    t1."INRBSCSDHOEN",
    t1."MINPWRLEVDIRTRY",
    t1."MRPREPROCFREQ",
    t1."NEWURGHOMININTV",
    t1."PENALTYEN",
    t1."PRIMMESPPT",
    t1."SDHOMININTV",
    t1."TCHHOMININTV",
    t1."ULRXLEVBOUNDPROTECTIONSW"
FROM
huawei_nbi_gsm."GCELLHOCTRL" t1

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
    t2."BCCHHOPHOCOMPOPT",
    t2."BSMSPWRLEV",
    t2."BTSMESRPTPREPROC",
    t2."CELLID",
    t2."CONTHOMININTV",
    t2."INRBSCSDHOEN",
    t2."MINPWRLEVDIRTRY",
    t2."MRPREPROCFREQ",
    t2."NEWURGHOMININTV",
    t2."PENALTYEN",
    t2."PRIMMESPPT",
    t2."SDHOMININTV",
    t2."TCHHOMININTV",
    t2."ULRXLEVBOUNDPROTECTIONSW"
FROM
huawei_gexport_gsm."GCELLHOCTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BCCHHOPHOCOMPOPT",
    t3."BSMSPWRLEV",
    t3."BTSMESRPTPREPROC",
    t3."CELLID",
    t3."CONTHOMININTV",
    t3."INRBSCSDHOEN",
    t3."MINPWRLEVDIRTRY",
    t3."MRPREPROCFREQ",
    t3."NEWURGHOMININTV",
    t3."PENALTYEN",
    t3."PRIMMESPPT",
    t3."SDHOMININTV",
    t3."TCHHOMININTV",
    t3."ULRXLEVBOUNDPROTECTIONSW"
FROM
huawei_gexport_gsm."GCELLHOCTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BCCHHOPHOCOMPOPT",
    t4."BSMSPWRLEV",
    t4."BTSMESRPTPREPROC",
    t4."CELLID",
    t4."CONTHOMININTV",
    t4."INRBSCSDHOEN",
    t4."MINPWRLEVDIRTRY",
    t4."MRPREPROCFREQ",
    t4."NEWURGHOMININTV",
    t4."PENALTYEN",
    t4."PRIMMESPPT",
    t4."SDHOMININTV",
    t4."TCHHOMININTV",
    t4."ULRXLEVBOUNDPROTECTIONSW"
FROM
huawei_mml_gsm."GCELLHOCTRL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOEDBPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLHOEDBPARA"',
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
    t1."ATCBHYST",
    t1."ATCBTHRED",
    t1."CELLID",
    t1."EDBDIRECTPUNISHSW",
    t1."EDBLASTTIME",
    t1."EDBSTATTIME",
    t1."EDBSYSFLOWLEV",
    t1."HOPENALTYTIME",
    t1."INNASSOPTEN",
    t1."INNCELLEDGEHOEN",
    t1."INNLOADHOEN",
    t1."INNLOADHOPERI",
    t1."INNLOADHOSTEP",
    t1."INNSERIOVERLDTHRED",
    t1."INTOINNREXLEVTHRED",
    t1."OUTASSOPTEN",
    t1."OUTGENOVERLDTHRED",
    t1."OUTINNREXLEVTHRED",
    t1."OUTLOADHOENABLE",
    t1."OUTLOADHOMODPERI",
    t1."OUTLOADHOPERIOD",
    t1."OUTLOADHOSTEP",
    t1."OUTLOWLOADTHRED",
    t1."OUTSERIOVERLDTHRED"
FROM
huawei_nbi_gsm."GCELLHOEDBPARA" t1

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
    t2."ATCBHYST",
    t2."ATCBTHRED",
    t2."CELLID",
    t2."EDBDIRECTPUNISHSW",
    t2."EDBLASTTIME",
    t2."EDBSTATTIME",
    t2."EDBSYSFLOWLEV",
    t2."HOPENALTYTIME",
    t2."INNASSOPTEN",
    t2."INNCELLEDGEHOEN",
    t2."INNLOADHOEN",
    t2."INNLOADHOPERI",
    t2."INNLOADHOSTEP",
    t2."INNSERIOVERLDTHRED",
    t2."INTOINNREXLEVTHRED",
    t2."OUTASSOPTEN",
    t2."OUTGENOVERLDTHRED",
    t2."OUTINNREXLEVTHRED",
    t2."OUTLOADHOENABLE",
    t2."OUTLOADHOMODPERI",
    t2."OUTLOADHOPERIOD",
    t2."OUTLOADHOSTEP",
    t2."OUTLOWLOADTHRED",
    t2."OUTSERIOVERLDTHRED"
FROM
huawei_gexport_gsm."GCELLHOEDBPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ATCBHYST",
    t3."ATCBTHRED",
    t3."CELLID",
    t3."EDBDIRECTPUNISHSW",
    t3."EDBLASTTIME",
    t3."EDBSTATTIME",
    t3."EDBSYSFLOWLEV",
    t3."HOPENALTYTIME",
    t3."INNASSOPTEN",
    t3."INNCELLEDGEHOEN",
    t3."INNLOADHOEN",
    t3."INNLOADHOPERI",
    t3."INNLOADHOSTEP",
    t3."INNSERIOVERLDTHRED",
    t3."INTOINNREXLEVTHRED",
    t3."OUTASSOPTEN",
    t3."OUTGENOVERLDTHRED",
    t3."OUTINNREXLEVTHRED",
    t3."OUTLOADHOENABLE",
    t3."OUTLOADHOMODPERI",
    t3."OUTLOADHOPERIOD",
    t3."OUTLOADHOSTEP",
    t3."OUTLOWLOADTHRED",
    t3."OUTSERIOVERLDTHRED"
FROM
huawei_gexport_gsm."GCELLHOEDBPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ATCBHYST",
    t4."ATCBTHRED",
    t4."CELLID",
    t4."EDBDIRECTPUNISHSW",
    t4."EDBLASTTIME",
    t4."EDBSTATTIME",
    t4."EDBSYSFLOWLEV",
    t4."HOPENALTYTIME",
    t4."INNASSOPTEN",
    t4."INNCELLEDGEHOEN",
    t4."INNLOADHOEN",
    t4."INNLOADHOPERI",
    t4."INNLOADHOSTEP",
    t4."INNSERIOVERLDTHRED",
    t4."INTOINNREXLEVTHRED",
    t4."OUTASSOPTEN",
    t4."OUTGENOVERLDTHRED",
    t4."OUTINNREXLEVTHRED",
    t4."OUTLOADHOENABLE",
    t4."OUTLOADHOMODPERI",
    t4."OUTLOADHOPERIOD",
    t4."OUTLOADHOSTEP",
    t4."OUTLOWLOADTHRED",
    t4."OUTSERIOVERLDTHRED"
FROM
huawei_mml_gsm."GCELLHOEDBPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOEMG = ReplaceableObject(
    'huawei_cm_2g."GCELLHOEMG"',
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
    t1."DLQUALIMIT",
    t1."FLTPARAA1",
    t1."FLTPARAA2",
    t1."FLTPARAA3",
    t1."FLTPARAA4",
    t1."FLTPARAA5",
    t1."FLTPARAA6",
    t1."FLTPARAA7",
    t1."FLTPARAA8",
    t1."FLTPARAB",
    t1."HOCTRLSWITCH",
    t1."NODLMRHOALLOWLIMIT",
    t1."NODLMRHOEN",
    t1."NODLMRHOLASTTIME",
    t1."NODLMRHOQUALLIMIT",
    t1."NODLMRHOSTATTIME",
    t1."TALIMIT",
    t1."ULQUALIMIT"
FROM
huawei_nbi_gsm."GCELLHOEMG" t1

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
    t2."DLQUALIMIT",
    t2."FLTPARAA1",
    t2."FLTPARAA2",
    t2."FLTPARAA3",
    t2."FLTPARAA4",
    t2."FLTPARAA5",
    t2."FLTPARAA6",
    t2."FLTPARAA7",
    t2."FLTPARAA8",
    t2."FLTPARAB",
    t2."HOCTRLSWITCH",
    t2."NODLMRHOALLOWLIMIT",
    t2."NODLMRHOEN",
    t2."NODLMRHOLASTTIME",
    t2."NODLMRHOQUALLIMIT",
    t2."NODLMRHOSTATTIME",
    t2."TALIMIT",
    t2."ULQUALIMIT"
FROM
huawei_gexport_gsm."GCELLHOEMG_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DLQUALIMIT",
    t3."FLTPARAA1",
    t3."FLTPARAA2",
    t3."FLTPARAA3",
    t3."FLTPARAA4",
    t3."FLTPARAA5",
    t3."FLTPARAA6",
    t3."FLTPARAA7",
    t3."FLTPARAA8",
    t3."FLTPARAB",
    t3."HOCTRLSWITCH",
    t3."NODLMRHOALLOWLIMIT",
    t3."NODLMRHOEN",
    t3."NODLMRHOLASTTIME",
    t3."NODLMRHOQUALLIMIT",
    t3."NODLMRHOSTATTIME",
    t3."TALIMIT",
    t3."ULQUALIMIT"
FROM
huawei_gexport_gsm."GCELLHOEMG_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DLQUALIMIT",
    t4."FLTPARAA1",
    t4."FLTPARAA2",
    t4."FLTPARAA3",
    t4."FLTPARAA4",
    t4."FLTPARAA5",
    t4."FLTPARAA6",
    t4."FLTPARAA7",
    t4."FLTPARAA8",
    t4."FLTPARAB",
    t4."HOCTRLSWITCH",
    t4."NODLMRHOALLOWLIMIT",
    t4."NODLMRHOEN",
    t4."NODLMRHOLASTTIME",
    t4."NODLMRHOQUALLIMIT",
    t4."NODLMRHOSTATTIME",
    t4."TALIMIT",
    t4."ULQUALIMIT"
FROM
huawei_mml_gsm."GCELLHOEMG" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOFAST = ReplaceableObject(
    'huawei_cm_2g."GCELLHOFAST"',
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
    t1."AFCHOLASTTIME",
    t1."AFCHOSTATTIME",
    t1."CELLID",
    t1."HODIRFORECASTEN",
    t1."HODIRLASTTIME",
    t1."HODIRSTATIME",
    t1."HODOWNTRIGE",
    t1."HOOFFSET",
    t1."HOPUNISHVALUE",
    t1."HOUPTRIGE",
    t1."IGNOREMRNUM",
    t1."MOVESPEEDTHRES",
    t1."MSLEVSTRQPBGT",
    t1."NCELLFILTER",
    t1."QUICKHOPUNISHSW",
    t1."SCELLFILTER",
    t1."TIMEPUNISH"
FROM
huawei_nbi_gsm."GCELLHOFAST" t1

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
    t2."AFCHOLASTTIME",
    t2."AFCHOSTATTIME",
    t2."CELLID",
    t2."HODIRFORECASTEN",
    t2."HODIRLASTTIME",
    t2."HODIRSTATIME",
    t2."HODOWNTRIGE",
    t2."HOOFFSET",
    t2."HOPUNISHVALUE",
    t2."HOUPTRIGE",
    t2."IGNOREMRNUM",
    t2."MOVESPEEDTHRES",
    t2."MSLEVSTRQPBGT",
    t2."NCELLFILTER",
    t2."QUICKHOPUNISHSW",
    t2."SCELLFILTER",
    t2."TIMEPUNISH"
FROM
huawei_gexport_gsm."GCELLHOFAST_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AFCHOLASTTIME",
    t3."AFCHOSTATTIME",
    t3."CELLID",
    t3."HODIRFORECASTEN",
    t3."HODIRLASTTIME",
    t3."HODIRSTATIME",
    t3."HODOWNTRIGE",
    t3."HOOFFSET",
    t3."HOPUNISHVALUE",
    t3."HOUPTRIGE",
    t3."IGNOREMRNUM",
    t3."MOVESPEEDTHRES",
    t3."MSLEVSTRQPBGT",
    t3."NCELLFILTER",
    t3."QUICKHOPUNISHSW",
    t3."SCELLFILTER",
    t3."TIMEPUNISH"
FROM
huawei_gexport_gsm."GCELLHOFAST_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AFCHOLASTTIME",
    t4."AFCHOSTATTIME",
    t4."CELLID",
    t4."HODIRFORECASTEN",
    t4."HODIRLASTTIME",
    t4."HODIRSTATIME",
    t4."HODOWNTRIGE",
    t4."HOOFFSET",
    t4."HOPUNISHVALUE",
    t4."HOUPTRIGE",
    t4."IGNOREMRNUM",
    t4."MOVESPEEDTHRES",
    t4."MSLEVSTRQPBGT",
    t4."NCELLFILTER",
    t4."QUICKHOPUNISHSW",
    t4."SCELLFILTER",
    t4."TIMEPUNISH"
FROM
huawei_mml_gsm."GCELLHOFAST" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOFDDBA2 = ReplaceableObject(
    'huawei_cm_2g."GCELLHOFDDBA2"',
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
    t1."DF",
    t1."DIVERSITY",
    t1."FDDBA2TAG",
    t1."ITEM",
    t1."ITEMVALID",
    t1."SCRAMBLE"
FROM
huawei_nbi_gsm."GCELLHOFDDBA2" t1

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
    t2."DF",
    t2."DIVERSITY",
    t2."FDDBA2TAG",
    t2."ITEM",
    t2."ITEMVALID",
    t2."SCRAMBLE"
FROM
huawei_gexport_gsm."GCELLHOFDDBA2_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DF",
    t3."DIVERSITY",
    t3."FDDBA2TAG",
    t3."ITEM",
    t3."ITEMVALID",
    t3."SCRAMBLE"
FROM
huawei_gexport_gsm."GCELLHOFDDBA2_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FDDBA2TAG",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELLHOFDDBA2" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOFITPEN = ReplaceableObject(
    'huawei_cm_2g."GCELLHOFITPEN"',
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
    t1."CBSIGNLEN",
    t1."CBTRAFFLEN",
    t1."CELLID",
    t1."DATAQUAFLTLEN",
    t1."DATASTRFLTLEN",
    t1."DATASTRUPFLTLEN",
    t1."DTXMEASUSED",
    t1."FAILSIGSTRPUNISH",
    t1."HOCTRLSWITCH",
    t1."INITUPFILEN",
    t1."LOADHOPUNISHINHERITSWITCH",
    t1."MBSIGNLEN",
    t1."MBTRAFFLEN",
    t1."MRMISSCOUNT",
    t1."NCELLFLTLEN",
    t1."NRBSDCCHFFLEN",
    t1."NRBTCHFFLEN",
    t1."PENALTYTIMER",
    t1."RQSIGNLEN",
    t1."RQTRAFFLEN",
    t1."RSCPENALTYTIMER",
    t1."SIGQUAFLTLEN",
    t1."SIGSTRFLTLEN",
    t1."SIGSTRUPFLTLEN",
    t1."SSBQPUNISH",
    t1."SSTAPUNISH",
    t1."TAFLTLEN",
    t1."TIMEAMRFHPUNISH",
    t1."TIMEBQPUNISH",
    t1."TIMETAPUNISH",
    t1."UMPENALTYTIMER",
    t1."INTERFEREHOPENTIME",
    t1."LOADHOPENTIME",
    t1."LOADHOPENVALUE",
    t1."NSIGSTRFLTLEN",
    t1."TASIGSTRFLTLEN"
FROM
huawei_nbi_gsm."GCELLHOFITPEN" t1

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
    t2."CBSIGNLEN",
    t2."CBTRAFFLEN",
    t2."CELLID",
    t2."DATAQUAFLTLEN",
    t2."DATASTRFLTLEN",
    t2."DATASTRUPFLTLEN",
    t2."DTXMEASUSED",
    t2."FAILSIGSTRPUNISH",
    t2."HOCTRLSWITCH",
    t2."INITUPFILEN",
    t2."LOADHOPUNISHINHERITSWITCH",
    t2."MBSIGNLEN",
    t2."MBTRAFFLEN",
    t2."MRMISSCOUNT",
    t2."NCELLFLTLEN",
    t2."NRBSDCCHFFLEN",
    t2."NRBTCHFFLEN",
    t2."PENALTYTIMER",
    t2."RQSIGNLEN",
    t2."RQTRAFFLEN",
    t2."RSCPENALTYTIMER",
    t2."SIGQUAFLTLEN",
    t2."SIGSTRFLTLEN",
    t2."SIGSTRUPFLTLEN",
    t2."SSBQPUNISH",
    t2."SSTAPUNISH",
    t2."TAFLTLEN",
    t2."TIMEAMRFHPUNISH",
    t2."TIMEBQPUNISH",
    t2."TIMETAPUNISH",
    t2."UMPENALTYTIMER",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLHOFITPEN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CBSIGNLEN",
    t3."CBTRAFFLEN",
    t3."CELLID",
    t3."DATAQUAFLTLEN",
    t3."DATASTRFLTLEN",
    t3."DATASTRUPFLTLEN",
    t3."DTXMEASUSED",
    t3."FAILSIGSTRPUNISH",
    t3."HOCTRLSWITCH",
    t3."INITUPFILEN",
    t3."LOADHOPUNISHINHERITSWITCH",
    t3."MBSIGNLEN",
    t3."MBTRAFFLEN",
    t3."MRMISSCOUNT",
    t3."NCELLFLTLEN",
    t3."NRBSDCCHFFLEN",
    t3."NRBTCHFFLEN",
    t3."PENALTYTIMER",
    t3."RQSIGNLEN",
    t3."RQTRAFFLEN",
    t3."RSCPENALTYTIMER",
    t3."SIGQUAFLTLEN",
    t3."SIGSTRFLTLEN",
    t3."SIGSTRUPFLTLEN",
    t3."SSBQPUNISH",
    t3."SSTAPUNISH",
    t3."TAFLTLEN",
    t3."TIMEAMRFHPUNISH",
    t3."TIMEBQPUNISH",
    t3."TIMETAPUNISH",
    t3."UMPENALTYTIMER",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLHOFITPEN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CBSIGNLEN",
    t4."CBTRAFFLEN",
    t4."CELLID",
    t4."DATAQUAFLTLEN",
    t4."DATASTRFLTLEN",
    t4."DATASTRUPFLTLEN",
    t4."DTXMEASUSED",
    t4."FAILSIGSTRPUNISH",
    t4."HOCTRLSWITCH",
    t4."INITUPFILEN",
    t4."LOADHOPUNISHINHERITSWITCH",
    t4."MBSIGNLEN",
    t4."MBTRAFFLEN",
    t4."MRMISSCOUNT",
    t4."NCELLFLTLEN",
    t4."NRBSDCCHFFLEN",
    t4."NRBTCHFFLEN",
    t4."PENALTYTIMER",
    t4."RQSIGNLEN",
    t4."RQTRAFFLEN",
    t4."RSCPENALTYTIMER",
    t4."SIGQUAFLTLEN",
    t4."SIGSTRFLTLEN",
    t4."SIGSTRUPFLTLEN",
    t4."SSBQPUNISH",
    t4."SSTAPUNISH",
    t4."TAFLTLEN",
    t4."TIMEAMRFHPUNISH",
    t4."TIMEBQPUNISH",
    t4."TIMETAPUNISH",
    t4."UMPENALTYTIMER",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELLHOFITPEN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOINTERRATLDB = ReplaceableObject(
    'huawei_cm_2g."GCELLHOINTERRATLDB"',
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
    t1."DLLDRTHRD2GCELL",
    t1."DLOLCTHRD2GCELL",
    t1."G2GLOADADJUSTCOEFF",
    t1."INTERRATCSSERVICELOADHOTHRD",
    t1."INTERRATLOADHOECNOBANDWIDTH",
    t1."INTERRATLOADHOECNOSTART",
    t1."INTERRATLOADHOECNOSTEP",
    t1."INTERRATLOADHORSCPBANDWIDTH",
    t1."INTERRATLOADHORSCPSTART",
    t1."INTERRATLOADHORSCPSTEP",
    t1."INTERRATSERVICELOADHOSWITCH",
    t1."INTRATLOADHOECNOTHR",
    t1."INTRATLOADHOPERIOD",
    t1."INTRATLOADHORSCPTHR",
    t1."OUTSYSLOADHOEN",
    t1."ULLDRTHRD2GCELL",
    t1."ULOLCTHRD2GCELL"
FROM
huawei_nbi_gsm."GCELLHOINTERRATLDB" t1

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
    t2."DLLDRTHRD2GCELL",
    t2."DLOLCTHRD2GCELL",
    t2."G2GLOADADJUSTCOEFF",
    t2."INTERRATCSSERVICELOADHOTHRD",
    t2."INTERRATLOADHOECNOBANDWIDTH",
    t2."INTERRATLOADHOECNOSTART",
    t2."INTERRATLOADHOECNOSTEP",
    t2."INTERRATLOADHORSCPBANDWIDTH",
    t2."INTERRATLOADHORSCPSTART",
    t2."INTERRATLOADHORSCPSTEP",
    t2."INTERRATSERVICELOADHOSWITCH",
    t2."INTRATLOADHOECNOTHR",
    t2."INTRATLOADHOPERIOD",
    t2."INTRATLOADHORSCPTHR",
    t2."OUTSYSLOADHOEN",
    t2."ULLDRTHRD2GCELL",
    t2."ULOLCTHRD2GCELL"
FROM
huawei_gexport_gsm."GCELLHOINTERRATLDB_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DLLDRTHRD2GCELL",
    t3."DLOLCTHRD2GCELL",
    t3."G2GLOADADJUSTCOEFF",
    t3."INTERRATCSSERVICELOADHOTHRD",
    t3."INTERRATLOADHOECNOBANDWIDTH",
    t3."INTERRATLOADHOECNOSTART",
    t3."INTERRATLOADHOECNOSTEP",
    t3."INTERRATLOADHORSCPBANDWIDTH",
    t3."INTERRATLOADHORSCPSTART",
    t3."INTERRATLOADHORSCPSTEP",
    t3."INTERRATSERVICELOADHOSWITCH",
    t3."INTRATLOADHOECNOTHR",
    t3."INTRATLOADHOPERIOD",
    t3."INTRATLOADHORSCPTHR",
    t3."OUTSYSLOADHOEN",
    t3."ULLDRTHRD2GCELL",
    t3."ULOLCTHRD2GCELL"
FROM
huawei_gexport_gsm."GCELLHOINTERRATLDB_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DLLDRTHRD2GCELL",
    t4."DLOLCTHRD2GCELL",
    t4."G2GLOADADJUSTCOEFF",
    t4."INTERRATCSSERVICELOADHOTHRD",
    t4."INTERRATLOADHOECNOBANDWIDTH",
    t4."INTERRATLOADHOECNOSTART",
    t4."INTERRATLOADHOECNOSTEP",
    t4."INTERRATLOADHORSCPBANDWIDTH",
    t4."INTERRATLOADHORSCPSTART",
    t4."INTERRATLOADHORSCPSTEP",
    t4."INTERRATSERVICELOADHOSWITCH",
    t4."INTRATLOADHOECNOTHR",
    t4."INTRATLOADHOPERIOD",
    t4."INTRATLOADHORSCPTHR",
    t4."OUTSYSLOADHOEN",
    t4."ULLDRTHRD2GCELL",
    t4."ULOLCTHRD2GCELL"
FROM
huawei_mml_gsm."GCELLHOINTERRATLDB" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOIUO = ReplaceableObject(
    'huawei_cm_2g."GCELLHOIUO"',
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
    t1."ACCESSOPTILAY",
    t1."CELLID",
    t1."ENGOVERLDTHRHYST",
    t1."ENGOVERLDTHRSH",
    t1."ENGOVERLDTHRSHOL",
    t1."ENLDHOPRD",
    t1."ENLDHOSTP",
    t1."ENLOWLDTHRSH",
    t1."ENSOVERLDTHRSH",
    t1."HOALGOPERMLAY",
    t1."HOCTRLSWITCH",
    t1."IMMASSTAALLOW",
    t1."IMMASSTATHRES",
    t1."IUOALLOCCHANTRAFALLOW",
    t1."IUOCHOSENINASS",
    t1."IUOHODURATIME",
    t1."IUOHOSTATIME",
    t1."IUOOLPOWERCOMPPOLICY",
    t1."OLTOULHOALLOW",
    t1."OLTOULHOLEVADJSW",
    t1."OPTILAYER",
    t1."OPTILEVTHRES",
    t1."OPTITATHRES",
    t1."OTOURECEIVETH",
    t1."PSIUODLINITONLYULSW",
    t1."PSOTOURECEIVETHRSH",
    t1."PSTAFORUOHOALLOW",
    t1."PSUTOORECEIVETHRSH",
    t1."RECEIVEQUALTHRSHAMRFR",
    t1."RECEIVEQUALTHRSHAMRHR",
    t1."RECLEVHYST",
    t1."RECLEVTHRES",
    t1."RECLEVUOHOALLOW",
    t1."RECQUALTH",
    t1."RECQUALUOHOALLOW",
    t1."SIGAMPTDIFF",
    t1."SIGAMPTDIFFOPTALLOW",
    t1."TAFORUOHOALLOW",
    t1."TAHYST",
    t1."TATHRES",
    t1."TIMEOTOUFAILPUN",
    t1."TIMEUTOOFAILPUN",
    t1."ULTOOLHOALLOW",
    t1."ULTOOLHOOVERLOADJUDGESW",
    t1."ULTOOLRXLEVSELSW",
    t1."UOLOADOPTSWITCH",
    t1."UTOOFAILMAXTIME",
    t1."UTOOHOPENTIME",
    t1."UTOORECTH",
    t1."UTOOTRAFHOALLOW",
    t1."UTOOTRAFHOOPTSW",
    t1."UTRAFHOPERIOD",
    t1."UTRAFHOSTEP",
    t1."ENUTOOLOADINILEV"
FROM
huawei_nbi_gsm."GCELLHOIUO" t1

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
    t2."ACCESSOPTILAY",
    t2."CELLID",
    t2."ENGOVERLDTHRHYST",
    t2."ENGOVERLDTHRSH",
    t2."ENGOVERLDTHRSHOL",
    t2."ENLDHOPRD",
    t2."ENLDHOSTP",
    t2."ENLOWLDTHRSH",
    t2."ENSOVERLDTHRSH",
    t2."HOALGOPERMLAY",
    t2."HOCTRLSWITCH",
    t2."IMMASSTAALLOW",
    t2."IMMASSTATHRES",
    t2."IUOALLOCCHANTRAFALLOW",
    t2."IUOCHOSENINASS",
    t2."IUOHODURATIME",
    t2."IUOHOSTATIME",
    t2."IUOOLPOWERCOMPPOLICY",
    t2."OLTOULHOALLOW",
    t2."OLTOULHOLEVADJSW",
    t2."OPTILAYER",
    t2."OPTILEVTHRES",
    t2."OPTITATHRES",
    t2."OTOURECEIVETH",
    t2."PSIUODLINITONLYULSW",
    t2."PSOTOURECEIVETHRSH",
    t2."PSTAFORUOHOALLOW",
    t2."PSUTOORECEIVETHRSH",
    t2."RECEIVEQUALTHRSHAMRFR",
    t2."RECEIVEQUALTHRSHAMRHR",
    t2."RECLEVHYST",
    t2."RECLEVTHRES",
    t2."RECLEVUOHOALLOW",
    t2."RECQUALTH",
    t2."RECQUALUOHOALLOW",
    t2."SIGAMPTDIFF",
    t2."SIGAMPTDIFFOPTALLOW",
    t2."TAFORUOHOALLOW",
    t2."TAHYST",
    t2."TATHRES",
    t2."TIMEOTOUFAILPUN",
    t2."TIMEUTOOFAILPUN",
    t2."ULTOOLHOALLOW",
    t2."ULTOOLHOOVERLOADJUDGESW",
    t2."ULTOOLRXLEVSELSW",
    t2."UOLOADOPTSWITCH",
    t2."UTOOFAILMAXTIME",
    t2."UTOOHOPENTIME",
    t2."UTOORECTH",
    t2."UTOOTRAFHOALLOW",
    t2."UTOOTRAFHOOPTSW",
    t2."UTRAFHOPERIOD",
    t2."UTRAFHOSTEP",
    NULL
FROM
huawei_gexport_gsm."GCELLHOIUO_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACCESSOPTILAY",
    t3."CELLID",
    t3."ENGOVERLDTHRHYST",
    t3."ENGOVERLDTHRSH",
    t3."ENGOVERLDTHRSHOL",
    t3."ENLDHOPRD",
    t3."ENLDHOSTP",
    t3."ENLOWLDTHRSH",
    t3."ENSOVERLDTHRSH",
    t3."HOALGOPERMLAY",
    t3."HOCTRLSWITCH",
    t3."IMMASSTAALLOW",
    t3."IMMASSTATHRES",
    t3."IUOALLOCCHANTRAFALLOW",
    t3."IUOCHOSENINASS",
    t3."IUOHODURATIME",
    t3."IUOHOSTATIME",
    t3."IUOOLPOWERCOMPPOLICY",
    t3."OLTOULHOALLOW",
    t3."OLTOULHOLEVADJSW",
    t3."OPTILAYER",
    t3."OPTILEVTHRES",
    t3."OPTITATHRES",
    t3."OTOURECEIVETH",
    t3."PSIUODLINITONLYULSW",
    t3."PSOTOURECEIVETHRSH",
    t3."PSTAFORUOHOALLOW",
    t3."PSUTOORECEIVETHRSH",
    t3."RECEIVEQUALTHRSHAMRFR",
    t3."RECEIVEQUALTHRSHAMRHR",
    t3."RECLEVHYST",
    t3."RECLEVTHRES",
    t3."RECLEVUOHOALLOW",
    t3."RECQUALTH",
    t3."RECQUALUOHOALLOW",
    t3."SIGAMPTDIFF",
    t3."SIGAMPTDIFFOPTALLOW",
    t3."TAFORUOHOALLOW",
    t3."TAHYST",
    t3."TATHRES",
    t3."TIMEOTOUFAILPUN",
    t3."TIMEUTOOFAILPUN",
    t3."ULTOOLHOALLOW",
    t3."ULTOOLHOOVERLOADJUDGESW",
    t3."ULTOOLRXLEVSELSW",
    t3."UOLOADOPTSWITCH",
    t3."UTOOFAILMAXTIME",
    t3."UTOOHOPENTIME",
    t3."UTOORECTH",
    t3."UTOOTRAFHOALLOW",
    t3."UTOOTRAFHOOPTSW",
    t3."UTRAFHOPERIOD",
    t3."UTRAFHOSTEP",
    NULL
FROM
huawei_gexport_gsm."GCELLHOIUO_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACCESSOPTILAY",
    t4."CELLID",
    t4."ENGOVERLDTHRHYST",
    t4."ENGOVERLDTHRSH",
    t4."ENGOVERLDTHRSHOL",
    t4."ENLDHOPRD",
    t4."ENLDHOSTP",
    t4."ENLOWLDTHRSH",
    t4."ENSOVERLDTHRSH",
    t4."HOALGOPERMLAY",
    t4."HOCTRLSWITCH",
    t4."IMMASSTAALLOW",
    t4."IMMASSTATHRES",
    t4."IUOALLOCCHANTRAFALLOW",
    t4."IUOCHOSENINASS",
    t4."IUOHODURATIME",
    t4."IUOHOSTATIME",
    t4."IUOOLPOWERCOMPPOLICY",
    t4."OLTOULHOALLOW",
    t4."OLTOULHOLEVADJSW",
    t4."OPTILAYER",
    t4."OPTILEVTHRES",
    t4."OPTITATHRES",
    t4."OTOURECEIVETH",
    t4."PSIUODLINITONLYULSW",
    t4."PSOTOURECEIVETHRSH",
    t4."PSTAFORUOHOALLOW",
    t4."PSUTOORECEIVETHRSH",
    t4."RECEIVEQUALTHRSHAMRFR",
    t4."RECEIVEQUALTHRSHAMRHR",
    t4."RECLEVHYST",
    t4."RECLEVTHRES",
    t4."RECLEVUOHOALLOW",
    t4."RECQUALTH",
    t4."RECQUALUOHOALLOW",
    t4."SIGAMPTDIFF",
    t4."SIGAMPTDIFFOPTALLOW",
    t4."TAFORUOHOALLOW",
    t4."TAHYST",
    t4."TATHRES",
    t4."TIMEOTOUFAILPUN",
    t4."TIMEUTOOFAILPUN",
    t4."ULTOOLHOALLOW",
    t4."ULTOOLHOOVERLOADJUDGESW",
    t4."ULTOOLRXLEVSELSW",
    t4."UOLOADOPTSWITCH",
    t4."UTOOFAILMAXTIME",
    t4."UTOOHOPENTIME",
    t4."UTOORECTH",
    t4."UTOOTRAFHOALLOW",
    t4."UTOOTRAFHOOPTSW",
    t4."UTRAFHOPERIOD",
    t4."UTRAFHOSTEP",
    NULL
FROM
huawei_mml_gsm."GCELLHOIUO" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOPANT = ReplaceableObject(
    'huawei_cm_2g."GCELLHOPANT"',
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
    t1."HPANTMODE"
FROM
huawei_nbi_gsm."GCELLHOPANT" t1

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
    t2."HPANTMODE"
FROM
huawei_gexport_gsm."GCELLHOPANT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."HPANTMODE"
FROM
huawei_gexport_gsm."GCELLHOPANT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."HPANTMODE"
FROM
huawei_mml_gsm."GCELLHOPANT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOPTP = ReplaceableObject(
    'huawei_cm_2g."GCELLHOPTP"',
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
    t1."FHMODE"
FROM
huawei_nbi_gsm."GCELLHOPTP" t1

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
    t2."FHMODE"
FROM
huawei_gexport_gsm."GCELLHOPTP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FHMODE"
FROM
huawei_gexport_gsm."GCELLHOPTP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FHMODE"
FROM
huawei_mml_gsm."GCELLHOPTP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOTDDBA2 = ReplaceableObject(
    'huawei_cm_2g."GCELLHOTDDBA2"',
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
    t1."ITEM",
    t1."ITEMVALID",
    t1."TDDBA2TAG"
FROM
huawei_nbi_gsm."GCELLHOTDDBA2" t1

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
    t2."ITEM",
    t2."ITEMVALID",
    t2."TDDBA2TAG"
FROM
huawei_gexport_gsm."GCELLHOTDDBA2_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ITEM",
    t3."ITEMVALID",
    t3."TDDBA2TAG"
FROM
huawei_gexport_gsm."GCELLHOTDDBA2_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TDDBA2TAG"
FROM
huawei_mml_gsm."GCELLHOTDDBA2" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOUTRANFDD = ReplaceableObject(
    'huawei_cm_2g."GCELLHOUTRANFDD"',
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
    t1."BET3GHOEN",
    t1."CELLID",
    t1."HOECNOTH3G",
    t1."HOOPTSEL",
    t1."HOPRETH2G",
    t1."HORSCPTH3G"
FROM
huawei_nbi_gsm."GCELLHOUTRANFDD" t1

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
    t2."BET3GHOEN",
    t2."CELLID",
    t2."HOECNOTH3G",
    t2."HOOPTSEL",
    t2."HOPRETH2G",
    t2."HORSCPTH3G"
FROM
huawei_gexport_gsm."GCELLHOUTRANFDD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BET3GHOEN",
    t3."CELLID",
    t3."HOECNOTH3G",
    t3."HOOPTSEL",
    t3."HOPRETH2G",
    t3."HORSCPTH3G"
FROM
huawei_gexport_gsm."GCELLHOUTRANFDD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BET3GHOEN",
    t4."CELLID",
    t4."HOECNOTH3G",
    t4."HOOPTSEL",
    t4."HOPRETH2G",
    t4."HORSCPTH3G"
FROM
huawei_mml_gsm."GCELLHOUTRANFDD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHOUTRANTDD = ReplaceableObject(
    'huawei_cm_2g."GCELLHOUTRANTDD"',
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
    t1."BET3GHOEN",
    t1."CELLID",
    t1."HOOPTSEL",
    t1."HOPRETH2G",
    t1."HORSCPTH3G"
FROM
huawei_nbi_gsm."GCELLHOUTRANTDD" t1

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
    t2."BET3GHOEN",
    t2."CELLID",
    t2."HOOPTSEL",
    t2."HOPRETH2G",
    t2."HORSCPTH3G"
FROM
huawei_gexport_gsm."GCELLHOUTRANTDD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BET3GHOEN",
    t3."CELLID",
    t3."HOOPTSEL",
    t3."HOPRETH2G",
    t3."HORSCPTH3G"
FROM
huawei_gexport_gsm."GCELLHOUTRANTDD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BET3GHOEN",
    t4."CELLID",
    t4."HOOPTSEL",
    t4."HOPRETH2G",
    t4."HORSCPTH3G"
FROM
huawei_mml_gsm."GCELLHOUTRANTDD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLHSRPLCUSRIDFMG = ReplaceableObject(
    'huawei_cm_2g."GCELLHSRPLCUSRIDFMG"',
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
    t1."HSRPLCUSRIDNTFSW"
FROM
huawei_nbi_gsm."GCELLHSRPLCUSRIDFMG" t1

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
    t2."HSRPLCUSRIDNTFSW"
FROM
huawei_gexport_gsm."GCELLHSRPLCUSRIDFMG_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."HSRPLCUSRIDNTFSW"
FROM
huawei_gexport_gsm."GCELLHSRPLCUSRIDFMG_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."HSRPLCUSRIDNTFSW"
FROM
huawei_mml_gsm."GCELLHSRPLCUSRIDFMG" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLIBCAII = ReplaceableObject(
    'huawei_cm_2g."GCELLIBCAII"',
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
    t1."IBCAIIALLOWED"
FROM
huawei_nbi_gsm."GCELLIBCAII" t1

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
    t2."IBCAIIALLOWED"
FROM
huawei_gexport_gsm."GCELLIBCAII_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IBCAIIALLOWED"
FROM
huawei_gexport_gsm."GCELLIBCAII_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IBCAIIALLOWED"
FROM
huawei_mml_gsm."GCELLIBCAII" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLIDLEAD = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLEAD"',
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
    t1."ACS",
    t1."CELLID",
    t1."CMETO",
    t1."PT"
FROM
huawei_nbi_gsm."GCELLIDLEAD" t1

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
    t2."ACS",
    t2."CELLID",
    NULL,
    t2."PT"
FROM
huawei_gexport_gsm."GCELLIDLEAD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACS",
    t3."CELLID",
    NULL,
    t3."PT"
FROM
huawei_gexport_gsm."GCELLIDLEAD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACS",
    t4."CELLID",
    NULL,
    t4."PT"
FROM
huawei_mml_gsm."GCELLIDLEAD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLIDLEBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLEBASIC"',
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
    t1."BSAGBLKSRES",
    t1."BSPAMFRAMS",
    t1."CBA",
    t1."CBQ",
    t1."CELLID",
    t1."CRH",
    t1."CRO",
    t1."DISCARDCHREQCBQSW",
    t1."NCCPERMIT",
    t1."PI",
    t1."T3212",
    t1."TX"
FROM
huawei_nbi_gsm."GCELLIDLEBASIC" t1

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
    t2."ATT",
    t2."BSAGBLKSRES",
    t2."BSPAMFRAMS",
    t2."CBA",
    t2."CBQ",
    t2."CELLID",
    t2."CRH",
    t2."CRO",
    t2."DISCARDCHREQCBQSW",
    NULL,
    t2."PI",
    t2."T3212",
    t2."TX"
FROM
huawei_gexport_gsm."GCELLIDLEBASIC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ATT",
    t3."BSAGBLKSRES",
    t3."BSPAMFRAMS",
    t3."CBA",
    t3."CBQ",
    t3."CELLID",
    t3."CRH",
    t3."CRO",
    t3."DISCARDCHREQCBQSW",
    NULL,
    t3."PI",
    t3."T3212",
    t3."TX"
FROM
huawei_gexport_gsm."GCELLIDLEBASIC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ATT",
    t4."BSAGBLKSRES",
    t4."BSPAMFRAMS",
    t4."CBA",
    t4."CBQ",
    t4."CELLID",
    t4."CRH",
    t4."CRO",
    t4."DISCARDCHREQCBQSW",
    NULL,
    t4."PI",
    t4."T3212",
    t4."TX"
FROM
huawei_mml_gsm."GCELLIDLEBASIC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLIDLEFDDBA1 = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLEFDDBA1"',
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
    t1."FDDBA1TAG",
    t1."FDDDIVERSITY",
    t1."FDDDLUARFAN",
    t1."FDDSCRAMBLE",
    t1."ITEM",
    t1."ITEMVALID"
FROM
huawei_nbi_gsm."GCELLIDLEFDDBA1" t1

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
    t2."FDDBA1TAG",
    NULL,
    NULL,
    NULL,
    t2."ITEM",
    t2."ITEMVALID"
FROM
huawei_gexport_gsm."GCELLIDLEFDDBA1_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FDDBA1TAG",
    NULL,
    NULL,
    NULL,
    t3."ITEM",
    t3."ITEMVALID"
FROM
huawei_gexport_gsm."GCELLIDLEFDDBA1_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FDDBA1TAG",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELLIDLEFDDBA1" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLIDLETDDBA1 = ReplaceableObject(
    'huawei_cm_2g."GCELLIDLETDDBA1"',
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
    t1."ITEM",
    t1."ITEMVALID",
    t1."TDDBA1TAG"
FROM
huawei_nbi_gsm."GCELLIDLETDDBA1" t1

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
    t2."ITEM",
    t2."ITEMVALID",
    t2."TDDBA1TAG"
FROM
huawei_gexport_gsm."GCELLIDLETDDBA1_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ITEM",
    t3."ITEMVALID",
    t3."TDDBA1TAG"
FROM
huawei_gexport_gsm."GCELLIDLETDDBA1_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TDDBA1TAG"
FROM
huawei_mml_gsm."GCELLIDLETDDBA1" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLLCS = ReplaceableObject(
    'huawei_cm_2g."GCELLLCS"',
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
    t1."ALTIDECI",
    t1."ALTITUDE",
    t1."ANTAANGLE",
    t1."CELLID",
    t1."INCLUDEANG",
    t1."INPUTMD",
    t1."LATIDECI",
    t1."LATIINT",
    t1."LONGIDECI",
    t1."LONGIINT",
    t1."NSLATI",
    t1."WELONGI"
FROM
huawei_nbi_gsm."GCELLLCS" t1

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
    t2."ALTIDECI",
    t2."ALTITUDE",
    t2."ANTAANGLE",
    t2."CELLID",
    t2."INCLUDEANG",
    t2."INPUTMD",
    t2."LATIDECI",
    t2."LATIINT",
    t2."LONGIDECI",
    t2."LONGIINT",
    t2."NSLATI",
    t2."WELONGI"
FROM
huawei_gexport_gsm."GCELLLCS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALTIDECI",
    t3."ALTITUDE",
    t3."ANTAANGLE",
    t3."CELLID",
    t3."INCLUDEANG",
    t3."INPUTMD",
    t3."LATIDECI",
    t3."LATIINT",
    t3."LONGIDECI",
    t3."LONGIINT",
    t3."NSLATI",
    t3."WELONGI"
FROM
huawei_gexport_gsm."GCELLLCS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALTIDECI",
    t4."ALTITUDE",
    t4."ANTAANGLE",
    t4."CELLID",
    t4."INCLUDEANG",
    t4."INPUTMD",
    t4."LATIDECI",
    t4."LATIINT",
    t4."LONGIDECI",
    t4."LONGIINT",
    t4."NSLATI",
    t4."WELONGI"
FROM
huawei_mml_gsm."GCELLLCS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLMAGRP = ReplaceableObject(
    'huawei_cm_2g."GCELLMAGRP"',
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
    t1."FREQ1",
    t1."HOPINDEX",
    t1."HOPMODE",
    t1."HSN",
    t1."TSC",
    t1."FREQ2",
    t1."FREQ3",
    t1."FREQ4",
    t1."FREQ5",
    t1."FREQ6",
    t1."FREQ7",
    t1."FREQ8",
    t1."FREQ9",
    t1."FREQ10"
FROM
huawei_nbi_gsm."GCELLMAGRP" t1

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
    t2."FREQ1",
    t2."HOPINDEX",
    t2."HOPMODE",
    t2."HSN",
    t2."TSC",
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
huawei_gexport_gsm."GCELLMAGRP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FREQ1",
    t3."HOPINDEX",
    t3."HOPMODE",
    t3."HSN",
    t3."TSC",
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
huawei_gexport_gsm."GCELLMAGRP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FREQ1",
    t4."HOPINDEX",
    t4."HOPMODE",
    t4."HSN",
    t4."TSC",
    t4."FREQ2",
    t4."FREQ3",
    t4."FREQ4",
    t4."FREQ5",
    t4."FREQ6",
    t4."FREQ7",
    t4."FREQ8",
    t4."FREQ9",
    t4."FREQ10"
FROM
huawei_mml_gsm."GCELLMAGRP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLMAIOPLAN = ReplaceableObject(
    'huawei_cm_2g."GCELLMAIOPLAN"',
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
    t1."HOPINDEX"
FROM
huawei_nbi_gsm."GCELLMAIOPLAN" t1

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
    t2."HOPINDEX"
FROM
huawei_gexport_gsm."GCELLMAIOPLAN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."HOPINDEX"
FROM
huawei_gexport_gsm."GCELLMAIOPLAN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

GCELLMOCN = ReplaceableObject(
    'huawei_cm_2g."GCELLMOCN"',
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
    t1."MOCNIISW",
    t1."MOCNINTERRATPOLICYSW"
FROM
huawei_nbi_gsm."GCELLMOCN" t1

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
    t2."MOCNIISW",
    t2."MOCNINTERRATPOLICYSW"
FROM
huawei_gexport_gsm."GCELLMOCN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."MOCNIISW",
    t3."MOCNINTERRATPOLICYSW"
FROM
huawei_gexport_gsm."GCELLMOCN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."MOCNIISW",
    t4."MOCNINTERRATPOLICYSW"
FROM
huawei_mml_gsm."GCELLMOCN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLNC2PARA = ReplaceableObject(
    'huawei_cm_2g."GCELLNC2PARA"',
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
    t1."ALLOWEDMEASRPTMISSEDNUM",
    t1."CELLID",
    t1."CELLRXQUALWORSENRATIOTHRSH",
    t1."EGPRSBEPLIMIT8PSK",
    t1."EGPRSBEPLIMITGMSK",
    t1."FILTERWNDSIZE",
    t1."GPRSRXQUALLIMIT",
    t1."LOADRESELALLOW",
    t1."LOADRESELMAXRXLEV",
    t1."LOADRESELRXTHRSH",
    t1."LOADRESELSTARTTHRSH",
    t1."MINACCRXLEV",
    t1."MSRXQUALSTATTHRSH",
    t1."NORMALRESELALLOW",
    t1."PENALTYLASTTM",
    t1."PENALTYRXLEV",
    t1."RESELHYST",
    t1."RESELINTERVAL",
    t1."RESELWATCHPERIOD",
    t1."RESELWORSENLEVTHRSH",
    t1."TRAFFICRESELALLOW",
    t1."URGENTRESELALLOW"
FROM
huawei_nbi_gsm."GCELLNC2PARA" t1

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
    t2."ALLOWEDMEASRPTMISSEDNUM",
    t2."CELLID",
    t2."CELLRXQUALWORSENRATIOTHRSH",
    t2."EGPRSBEPLIMIT8PSK",
    t2."EGPRSBEPLIMITGMSK",
    t2."FILTERWNDSIZE",
    t2."GPRSRXQUALLIMIT",
    t2."LOADRESELALLOW",
    t2."LOADRESELMAXRXLEV",
    t2."LOADRESELRXTHRSH",
    t2."LOADRESELSTARTTHRSH",
    t2."MINACCRXLEV",
    t2."MSRXQUALSTATTHRSH",
    t2."NORMALRESELALLOW",
    t2."PENALTYLASTTM",
    t2."PENALTYRXLEV",
    t2."RESELHYST",
    t2."RESELINTERVAL",
    t2."RESELWATCHPERIOD",
    t2."RESELWORSENLEVTHRSH",
    t2."TRAFFICRESELALLOW",
    t2."URGENTRESELALLOW"
FROM
huawei_gexport_gsm."GCELLNC2PARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALLOWEDMEASRPTMISSEDNUM",
    t3."CELLID",
    t3."CELLRXQUALWORSENRATIOTHRSH",
    t3."EGPRSBEPLIMIT8PSK",
    t3."EGPRSBEPLIMITGMSK",
    t3."FILTERWNDSIZE",
    t3."GPRSRXQUALLIMIT",
    t3."LOADRESELALLOW",
    t3."LOADRESELMAXRXLEV",
    t3."LOADRESELRXTHRSH",
    t3."LOADRESELSTARTTHRSH",
    t3."MINACCRXLEV",
    t3."MSRXQUALSTATTHRSH",
    t3."NORMALRESELALLOW",
    t3."PENALTYLASTTM",
    t3."PENALTYRXLEV",
    t3."RESELHYST",
    t3."RESELINTERVAL",
    t3."RESELWATCHPERIOD",
    t3."RESELWORSENLEVTHRSH",
    t3."TRAFFICRESELALLOW",
    t3."URGENTRESELALLOW"
FROM
huawei_gexport_gsm."GCELLNC2PARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALLOWEDMEASRPTMISSEDNUM",
    t4."CELLID",
    t4."CELLRXQUALWORSENRATIOTHRSH",
    t4."EGPRSBEPLIMIT8PSK",
    t4."EGPRSBEPLIMITGMSK",
    t4."FILTERWNDSIZE",
    t4."GPRSRXQUALLIMIT",
    t4."LOADRESELALLOW",
    t4."LOADRESELMAXRXLEV",
    t4."LOADRESELRXTHRSH",
    t4."LOADRESELSTARTTHRSH",
    t4."MINACCRXLEV",
    t4."MSRXQUALSTATTHRSH",
    t4."NORMALRESELALLOW",
    t4."PENALTYLASTTM",
    t4."PENALTYRXLEV",
    t4."RESELHYST",
    t4."RESELINTERVAL",
    t4."RESELWATCHPERIOD",
    t4."RESELWORSENLEVTHRSH",
    t4."TRAFFICRESELALLOW",
    t4."URGENTRESELALLOW"
FROM
huawei_mml_gsm."GCELLNC2PARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLNCRESELECTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLNCRESELECTPARA"',
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
    t1."GPRSPENALTYTIME",
    t1."GPRSTEMPOFFSET",
    t1."RSLCTOFFER"
FROM
huawei_nbi_gsm."GCELLNCRESELECTPARA" t1

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
    t2."GPRSPENALTYTIME",
    t2."GPRSTEMPOFFSET",
    t2."RSLCTOFFER"
FROM
huawei_gexport_gsm."GCELLNCRESELECTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."GPRSPENALTYTIME",
    t3."GPRSTEMPOFFSET",
    t3."RSLCTOFFER"
FROM
huawei_gexport_gsm."GCELLNCRESELECTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GPRSPENALTYTIME",
    t4."GPRSTEMPOFFSET",
    t4."RSLCTOFFER"
FROM
huawei_mml_gsm."GCELLNCRESELECTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLNONSTANDARDBW = ReplaceableObject(
    'huawei_cm_2g."GCELLNONSTANDARDBW"',
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
    t1."GUDEGRATEPWRCTRL"
FROM
huawei_nbi_gsm."GCELLNONSTANDARDBW" t1

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
    t2."GUDEGRATEPWRCTRL"
FROM
huawei_gexport_gsm."GCELLNONSTANDARDBW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."GUDEGRATEPWRCTRL"
FROM
huawei_gexport_gsm."GCELLNONSTANDARDBW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GUDEGRATEPWRCTRL"
FROM
huawei_mml_gsm."GCELLNONSTANDARDBW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLNWCTRLMSRPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLNWCTRLMSRPARA"',
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
    t1."NONDRXPERIOD",
    t1."RPTPERIODI",
    t1."RPTPERIODT"
FROM
huawei_nbi_gsm."GCELLNWCTRLMSRPARA" t1

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
    t2."NONDRXPERIOD",
    t2."RPTPERIODI",
    t2."RPTPERIODT"
FROM
huawei_gexport_gsm."GCELLNWCTRLMSRPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."NONDRXPERIOD",
    t3."RPTPERIODI",
    t3."RPTPERIODT"
FROM
huawei_gexport_gsm."GCELLNWCTRLMSRPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."NONDRXPERIOD",
    t4."RPTPERIODI",
    t4."RPTPERIODT"
FROM
huawei_mml_gsm."GCELLNWCTRLMSRPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLOPTREV = ReplaceableObject(
    'huawei_cm_2g."GCELLOPTREV"',
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
    t1."CELLOPTRSVPARA1",
    t1."CELLOPTRSVPARA3",
    t1."CELLOPTRSVPARA4"
FROM
huawei_nbi_gsm."GCELLOPTREV" t1

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
    t2."CELLOPTRSVPARA1",
    t2."CELLOPTRSVPARA3",
    t2."CELLOPTRSVPARA4"
FROM
huawei_gexport_gsm."GCELLOPTREV_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CELLOPTRSVPARA1",
    t3."CELLOPTRSVPARA3",
    t3."CELLOPTRSVPARA4"
FROM
huawei_gexport_gsm."GCELLOPTREV_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CELLOPTRSVPARA1",
    t4."CELLOPTRSVPARA3",
    t4."CELLOPTRSVPARA4"
FROM
huawei_mml_gsm."GCELLOPTREV" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLOSPMAP = ReplaceableObject(
    'huawei_cm_2g."GCELLOSPMAP"',
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
    t1."OPC"
FROM
huawei_nbi_gsm."GCELLOSPMAP" t1

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
    t2."OPC"
FROM
huawei_gexport_gsm."GCELLOSPMAP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."OPC"
FROM
huawei_gexport_gsm."GCELLOSPMAP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."OPC"
FROM
huawei_mml_gsm."GCELLOSPMAP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLOTHBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLOTHBASIC"',
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
    t1."FREQFILTBASEIRATMEASCFGSW",
    t1."GIMSIMMSW",
    t1."GSPIDMMSW",
    t1."HOPOWERBOOST",
    t1."LTEFASTRETURNFRQSENDOPTSW",
    t1."RPTVOICE"
FROM
huawei_nbi_gsm."GCELLOTHBASIC" t1

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
    t2."FREQFILTBASEIRATMEASCFGSW",
    t2."GIMSIMMSW",
    t2."GSPIDMMSW",
    t2."HOPOWERBOOST",
    t2."LTEFASTRETURNFRQSENDOPTSW",
    t2."RPTVOICE"
FROM
huawei_gexport_gsm."GCELLOTHBASIC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FREQFILTBASEIRATMEASCFGSW",
    t3."GIMSIMMSW",
    t3."GSPIDMMSW",
    t3."HOPOWERBOOST",
    t3."LTEFASTRETURNFRQSENDOPTSW",
    t3."RPTVOICE"
FROM
huawei_gexport_gsm."GCELLOTHBASIC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FREQFILTBASEIRATMEASCFGSW",
    t4."GIMSIMMSW",
    t4."GSPIDMMSW",
    t4."HOPOWERBOOST",
    t4."LTEFASTRETURNFRQSENDOPTSW",
    t4."RPTVOICE"
FROM
huawei_mml_gsm."GCELLOTHBASIC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLOTHEXT = ReplaceableObject(
    'huawei_cm_2g."GCELLOTHEXT"',
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
    t1."AUXTRXRSVSW",
    t1."BTSGRPFLEXABISLDRACTION",
    t1."CDRTTRYFBDTHRES",
    t1."CELLCOVERAGETYPE",
    t1."CELLID",
    t1."CELLOVERCVGRXLEVDLTH",
    t1."CELLOVERCVGTALTH",
    t1."CELLWEAKCVGRXLEVDLTH",
    t1."CELLWEAKCVGTALTH",
    t1."CSUPDATAABNMLCHKSW",
    t1."DATATRAFFSET",
    t1."DLFREQADJ",
    t1."DRFUVWSRSMMODE",
    t1."DRTAGCELLSEL",
    t1."DRXEN",
    t1."FERSTATTH1",
    t1."FERSTATTH2",
    t1."FERSTATTH3",
    t1."FERSTATTH4",
    t1."FERSTATTH5",
    t1."FERSTATTH6",
    t1."FERSTATTH7",
    t1."FRAMEOFFSET",
    t1."FREQADJ",
    t1."FREQADJVALUE",
    t1."HSCSDREADJUSTMENTSW",
    t1."HSCSDSCANPER",
    t1."HSCSDTRAFFSET",
    t1."IBCAINTFPUNISHTHR",
    t1."ICADPSCNIDENTOPTSW",
    t1."INTERFTHRES0",
    t1."INTERFTHRES1",
    t1."INTERFTHRES2",
    t1."INTERFTHRES3",
    t1."INTERFTHRES4",
    t1."INTERFTHRES5",
    t1."INTERPERIOD",
    t1."INTFBANDENHANCESW",
    t1."INTFFILTERPERIOD",
    t1."INTFREPROTPERIOD",
    t1."IURGINFOCTRL",
    t1."MAINBCCHPWRDTEN",
    t1."MTSPRITYPE",
    t1."PCHOCMPCON",
    t1."PODECTHRES",
    t1."POERRTHRES",
    t1."PREEMPTBBTHD",
    t1."PSULFREQADJ",
    t1."RELEASEBBTHD",
    t1."RESERVEDIDLECH",
    t1."RFMAXPWRDEC",
    t1."SDDROPSTATDLLEV",
    t1."SDDROPSTATDLQUAL",
    t1."SDDROPSTATULLEV",
    t1."SDDROPSTATULQUAL",
    t1."TCHDROPSTATDLFER",
    t1."TCHDROPSTATDLLEV",
    t1."TCHDROPSTATDLQUAL",
    t1."TCHDROPSTATULFER",
    t1."TCHDROPSTATULLEV",
    t1."TCHDROPSTATULQUAL",
    t1."TFRMSTARTTIME",
    t1."TRXPOOLALLOCTAFTH",
    t1."TRXPOOLPMTTAFTH",
    t1."TRXPOOLRELTAFTH",
    t1."VQILOWTHRD",
    t1."VSWRERRTHRES",
    t1."VSWRUNJUSTTHRES",
    t1."MAINBCCHPWDTACTCHEN",
    t1."MAINBCCHPWRDTETIME",
    t1."MAINBCCHPWRDTRANGE",
    t1."MAINBCCHPWRDTSTIME"
FROM
huawei_nbi_gsm."GCELLOTHEXT" t1

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
    t2."AUXTRXRSVSW",
    t2."BTSGRPFLEXABISLDRACTION",
    t2."CDRTTRYFBDTHRES",
    t2."CELLCOVERAGETYPE",
    t2."CELLID",
    t2."CELLOVERCVGRXLEVDLTH",
    t2."CELLOVERCVGTALTH",
    t2."CELLWEAKCVGRXLEVDLTH",
    t2."CELLWEAKCVGTALTH",
    NULL,
    NULL,
    t2."DLFREQADJ",
    t2."DRFUVWSRSMMODE",
    t2."DRTAGCELLSEL",
    t2."DRXEN",
    t2."FERSTATTH1",
    t2."FERSTATTH2",
    t2."FERSTATTH3",
    t2."FERSTATTH4",
    t2."FERSTATTH5",
    t2."FERSTATTH6",
    t2."FERSTATTH7",
    t2."FRAMEOFFSET",
    t2."FREQADJ",
    t2."FREQADJVALUE",
    t2."HSCSDREADJUSTMENTSW",
    t2."HSCSDSCANPER",
    t2."HSCSDTRAFFSET",
    t2."IBCAINTFPUNISHTHR",
    t2."ICADPSCNIDENTOPTSW",
    t2."INTERFTHRES0",
    t2."INTERFTHRES1",
    t2."INTERFTHRES2",
    t2."INTERFTHRES3",
    t2."INTERFTHRES4",
    t2."INTERFTHRES5",
    t2."INTERPERIOD",
    t2."INTFBANDENHANCESW",
    t2."INTFFILTERPERIOD",
    t2."INTFREPROTPERIOD",
    t2."IURGINFOCTRL",
    t2."MAINBCCHPWRDTEN",
    t2."MTSPRITYPE",
    t2."PCHOCMPCON",
    t2."PODECTHRES",
    t2."POERRTHRES",
    t2."PREEMPTBBTHD",
    t2."PSULFREQADJ",
    t2."RELEASEBBTHD",
    t2."RESERVEDIDLECH",
    t2."RFMAXPWRDEC",
    t2."SDDROPSTATDLLEV",
    t2."SDDROPSTATDLQUAL",
    t2."SDDROPSTATULLEV",
    t2."SDDROPSTATULQUAL",
    t2."TCHDROPSTATDLFER",
    t2."TCHDROPSTATDLLEV",
    t2."TCHDROPSTATDLQUAL",
    t2."TCHDROPSTATULFER",
    t2."TCHDROPSTATULLEV",
    t2."TCHDROPSTATULQUAL",
    t2."TFRMSTARTTIME",
    t2."TRXPOOLALLOCTAFTH",
    t2."TRXPOOLPMTTAFTH",
    t2."TRXPOOLRELTAFTH",
    t2."VQILOWTHRD",
    t2."VSWRERRTHRES",
    t2."VSWRUNJUSTTHRES",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLOTHEXT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AUXTRXRSVSW",
    t3."BTSGRPFLEXABISLDRACTION",
    t3."CDRTTRYFBDTHRES",
    t3."CELLCOVERAGETYPE",
    t3."CELLID",
    t3."CELLOVERCVGRXLEVDLTH",
    t3."CELLOVERCVGTALTH",
    t3."CELLWEAKCVGRXLEVDLTH",
    t3."CELLWEAKCVGTALTH",
    NULL,
    NULL,
    t3."DLFREQADJ",
    t3."DRFUVWSRSMMODE",
    t3."DRTAGCELLSEL",
    t3."DRXEN",
    t3."FERSTATTH1",
    t3."FERSTATTH2",
    t3."FERSTATTH3",
    t3."FERSTATTH4",
    t3."FERSTATTH5",
    t3."FERSTATTH6",
    t3."FERSTATTH7",
    t3."FRAMEOFFSET",
    t3."FREQADJ",
    t3."FREQADJVALUE",
    t3."HSCSDREADJUSTMENTSW",
    t3."HSCSDSCANPER",
    t3."HSCSDTRAFFSET",
    t3."IBCAINTFPUNISHTHR",
    t3."ICADPSCNIDENTOPTSW",
    t3."INTERFTHRES0",
    t3."INTERFTHRES1",
    t3."INTERFTHRES2",
    t3."INTERFTHRES3",
    t3."INTERFTHRES4",
    t3."INTERFTHRES5",
    t3."INTERPERIOD",
    t3."INTFBANDENHANCESW",
    t3."INTFFILTERPERIOD",
    t3."INTFREPROTPERIOD",
    t3."IURGINFOCTRL",
    t3."MAINBCCHPWRDTEN",
    t3."MTSPRITYPE",
    t3."PCHOCMPCON",
    t3."PODECTHRES",
    t3."POERRTHRES",
    t3."PREEMPTBBTHD",
    t3."PSULFREQADJ",
    t3."RELEASEBBTHD",
    t3."RESERVEDIDLECH",
    t3."RFMAXPWRDEC",
    t3."SDDROPSTATDLLEV",
    t3."SDDROPSTATDLQUAL",
    t3."SDDROPSTATULLEV",
    t3."SDDROPSTATULQUAL",
    t3."TCHDROPSTATDLFER",
    t3."TCHDROPSTATDLLEV",
    t3."TCHDROPSTATDLQUAL",
    t3."TCHDROPSTATULFER",
    t3."TCHDROPSTATULLEV",
    t3."TCHDROPSTATULQUAL",
    t3."TFRMSTARTTIME",
    t3."TRXPOOLALLOCTAFTH",
    t3."TRXPOOLPMTTAFTH",
    t3."TRXPOOLRELTAFTH",
    t3."VQILOWTHRD",
    t3."VSWRERRTHRES",
    t3."VSWRUNJUSTTHRES",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLOTHEXT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AUXTRXRSVSW",
    t4."BTSGRPFLEXABISLDRACTION",
    t4."CDRTTRYFBDTHRES",
    t4."CELLCOVERAGETYPE",
    t4."CELLID",
    t4."CELLOVERCVGRXLEVDLTH",
    t4."CELLOVERCVGTALTH",
    t4."CELLWEAKCVGRXLEVDLTH",
    t4."CELLWEAKCVGTALTH",
    NULL,
    NULL,
    t4."DLFREQADJ",
    t4."DRFUVWSRSMMODE",
    t4."DRTAGCELLSEL",
    t4."DRXEN",
    t4."FERSTATTH1",
    t4."FERSTATTH2",
    t4."FERSTATTH3",
    t4."FERSTATTH4",
    t4."FERSTATTH5",
    t4."FERSTATTH6",
    t4."FERSTATTH7",
    t4."FRAMEOFFSET",
    t4."FREQADJ",
    t4."FREQADJVALUE",
    t4."HSCSDREADJUSTMENTSW",
    t4."HSCSDSCANPER",
    t4."HSCSDTRAFFSET",
    t4."IBCAINTFPUNISHTHR",
    t4."ICADPSCNIDENTOPTSW",
    t4."INTERFTHRES0",
    t4."INTERFTHRES1",
    t4."INTERFTHRES2",
    t4."INTERFTHRES3",
    t4."INTERFTHRES4",
    t4."INTERFTHRES5",
    t4."INTERPERIOD",
    t4."INTFBANDENHANCESW",
    t4."INTFFILTERPERIOD",
    t4."INTFREPROTPERIOD",
    t4."IURGINFOCTRL",
    t4."MAINBCCHPWRDTEN",
    t4."MTSPRITYPE",
    t4."PCHOCMPCON",
    t4."PODECTHRES",
    t4."POERRTHRES",
    t4."PREEMPTBBTHD",
    t4."PSULFREQADJ",
    t4."RELEASEBBTHD",
    t4."RESERVEDIDLECH",
    t4."RFMAXPWRDEC",
    t4."SDDROPSTATDLLEV",
    t4."SDDROPSTATDLQUAL",
    t4."SDDROPSTATULLEV",
    t4."SDDROPSTATULQUAL",
    t4."TCHDROPSTATDLFER",
    t4."TCHDROPSTATDLLEV",
    t4."TCHDROPSTATDLQUAL",
    t4."TCHDROPSTATULFER",
    t4."TCHDROPSTATULLEV",
    t4."TCHDROPSTATULQUAL",
    t4."TFRMSTARTTIME",
    t4."TRXPOOLALLOCTAFTH",
    t4."TRXPOOLPMTTAFTH",
    t4."TRXPOOLRELTAFTH",
    t4."VQILOWTHRD",
    t4."VSWRERRTHRES",
    t4."VSWRUNJUSTTHRES",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."GCELLOTHEXT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLOTHPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLOTHPARA"',
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
    t1."AMRULCMRSENDMODE",
    t1."CELLID",
    t1."DRFUDLPWRCORRECTMODE",
    t1."DRRUDLPWRDECTMODE",
    t1."FIRSTMROPTSW",
    t1."IMMOCCUPYPCHOPTSW",
    t1."MULTRXBRDSTABMONITUNNSW",
    t1."MULTRXBRDUNSTABMONITUNNSW",
    t1."PCHFORBIDRPTLOADSW",
    t1."PTCCHPOWEROPTSW",
    t1."RPTRLTSW",
    t1."SDCONGESTBTSFLOWCTRLSW",
    t1."SPEECHBADFRAMEOPTSW",
    t1."SPEECHDELAYOPTSW"
FROM
huawei_nbi_gsm."GCELLOTHPARA" t1

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
    t2."AMRULCMRSENDMODE",
    t2."CELLID",
    t2."DRFUDLPWRCORRECTMODE",
    t2."DRRUDLPWRDECTMODE",
    t2."FIRSTMROPTSW",
    t2."IMMOCCUPYPCHOPTSW",
    t2."MULTRXBRDSTABMONITUNNSW",
    t2."MULTRXBRDUNSTABMONITUNNSW",
    t2."PCHFORBIDRPTLOADSW",
    t2."PTCCHPOWEROPTSW",
    t2."RPTRLTSW",
    t2."SDCONGESTBTSFLOWCTRLSW",
    t2."SPEECHBADFRAMEOPTSW",
    t2."SPEECHDELAYOPTSW"
FROM
huawei_gexport_gsm."GCELLOTHPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AMRULCMRSENDMODE",
    t3."CELLID",
    t3."DRFUDLPWRCORRECTMODE",
    t3."DRRUDLPWRDECTMODE",
    t3."FIRSTMROPTSW",
    t3."IMMOCCUPYPCHOPTSW",
    t3."MULTRXBRDSTABMONITUNNSW",
    t3."MULTRXBRDUNSTABMONITUNNSW",
    t3."PCHFORBIDRPTLOADSW",
    t3."PTCCHPOWEROPTSW",
    t3."RPTRLTSW",
    t3."SDCONGESTBTSFLOWCTRLSW",
    t3."SPEECHBADFRAMEOPTSW",
    t3."SPEECHDELAYOPTSW"
FROM
huawei_gexport_gsm."GCELLOTHPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AMRULCMRSENDMODE",
    t4."CELLID",
    t4."DRFUDLPWRCORRECTMODE",
    t4."DRRUDLPWRDECTMODE",
    t4."FIRSTMROPTSW",
    t4."IMMOCCUPYPCHOPTSW",
    t4."MULTRXBRDSTABMONITUNNSW",
    t4."MULTRXBRDUNSTABMONITUNNSW",
    t4."PCHFORBIDRPTLOADSW",
    t4."PTCCHPOWEROPTSW",
    t4."RPTRLTSW",
    t4."SDCONGESTBTSFLOWCTRLSW",
    t4."SPEECHBADFRAMEOPTSW",
    t4."SPEECHDELAYOPTSW"
FROM
huawei_mml_gsm."GCELLOTHPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPRACH = ReplaceableObject(
    'huawei_cm_2g."GCELLPRACH"',
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
    t1."ACCCONTROLCLASS",
    t1."CELLID",
    t1."MAXRETRANS1",
    t1."MAXRETRANS2",
    t1."MAXRETRANS3",
    t1."MAXRETRANS4",
    t1."PL1",
    t1."PL2",
    t1."PL3",
    t1."PL4",
    t1."SVALUE",
    t1."TXINT"
FROM
huawei_nbi_gsm."GCELLPRACH" t1

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
    t2."ACCCONTROLCLASS",
    t2."CELLID",
    t2."MAXRETRANS1",
    t2."MAXRETRANS2",
    t2."MAXRETRANS3",
    t2."MAXRETRANS4",
    t2."PL1",
    t2."PL2",
    t2."PL3",
    t2."PL4",
    t2."SVALUE",
    t2."TXINT"
FROM
huawei_gexport_gsm."GCELLPRACH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACCCONTROLCLASS",
    t3."CELLID",
    t3."MAXRETRANS1",
    t3."MAXRETRANS2",
    t3."MAXRETRANS3",
    t3."MAXRETRANS4",
    t3."PL1",
    t3."PL2",
    t3."PL3",
    t3."PL4",
    t3."SVALUE",
    t3."TXINT"
FROM
huawei_gexport_gsm."GCELLPRACH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACCCONTROLCLASS",
    t4."CELLID",
    t4."MAXRETRANS1",
    t4."MAXRETRANS2",
    t4."MAXRETRANS3",
    t4."MAXRETRANS4",
    t4."PL1",
    t4."PL2",
    t4."PL3",
    t4."PL4",
    t4."SVALUE",
    t4."TXINT"
FROM
huawei_mml_gsm."GCELLPRACH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPRIEUTRANSYS = ReplaceableObject(
    'huawei_cm_2g."GCELLPRIEUTRANSYS"',
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
    t1."BESTEUTRANCELLNUM",
    t1."CELLID",
    t1."EUTRANFREQCNUM",
    t1."EUTRANPRI",
    t1."EUTRANQRXLEVMIN",
    t1."FASTRETURNFILTERSW",
    t1."FASTRETURNMEASSPT",
    t1."FDDFASTRETURNRSRPTH",
    t1."FDDLTEOFFSET",
    t1."GERANPRI",
    t1."HPRIO",
    t1."QPEUTRAN",
    t1."SI2QUATEROPTFORLTESW",
    t1."TDDFASTRETURNRSRPTH",
    t1."TDDLTEOFFSET",
    t1."THREUTRANHIGH",
    t1."THREUTRANLOW",
    t1."THREUTRANRPT",
    t1."THRGSMLOW",
    t1."THRPRISEARCH",
    t1."THRUTRANHIGH",
    t1."THRUTRANLOW",
    t1."TRESEL",
    t1."UTRANPRI",
    t1."UTRANQRXLEVMIN"
FROM
huawei_nbi_gsm."GCELLPRIEUTRANSYS" t1

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
    t2."BESTEUTRANCELLNUM",
    t2."CELLID",
    t2."EUTRANFREQCNUM",
    t2."EUTRANPRI",
    t2."EUTRANQRXLEVMIN",
    NULL,
    t2."FASTRETURNMEASSPT",
    t2."FDDFASTRETURNRSRPTH",
    t2."FDDLTEOFFSET",
    t2."GERANPRI",
    t2."HPRIO",
    t2."QPEUTRAN",
    t2."SI2QUATEROPTFORLTESW",
    t2."TDDFASTRETURNRSRPTH",
    t2."TDDLTEOFFSET",
    t2."THREUTRANHIGH",
    t2."THREUTRANLOW",
    t2."THREUTRANRPT",
    t2."THRGSMLOW",
    t2."THRPRISEARCH",
    t2."THRUTRANHIGH",
    t2."THRUTRANLOW",
    t2."TRESEL",
    t2."UTRANPRI",
    t2."UTRANQRXLEVMIN"
FROM
huawei_gexport_gsm."GCELLPRIEUTRANSYS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BESTEUTRANCELLNUM",
    t3."CELLID",
    t3."EUTRANFREQCNUM",
    t3."EUTRANPRI",
    t3."EUTRANQRXLEVMIN",
    NULL,
    t3."FASTRETURNMEASSPT",
    t3."FDDFASTRETURNRSRPTH",
    t3."FDDLTEOFFSET",
    t3."GERANPRI",
    t3."HPRIO",
    t3."QPEUTRAN",
    t3."SI2QUATEROPTFORLTESW",
    t3."TDDFASTRETURNRSRPTH",
    t3."TDDLTEOFFSET",
    t3."THREUTRANHIGH",
    t3."THREUTRANLOW",
    t3."THREUTRANRPT",
    t3."THRGSMLOW",
    t3."THRPRISEARCH",
    t3."THRUTRANHIGH",
    t3."THRUTRANLOW",
    t3."TRESEL",
    t3."UTRANPRI",
    t3."UTRANQRXLEVMIN"
FROM
huawei_gexport_gsm."GCELLPRIEUTRANSYS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BESTEUTRANCELLNUM",
    t4."CELLID",
    t4."EUTRANFREQCNUM",
    t4."EUTRANPRI",
    t4."EUTRANQRXLEVMIN",
    NULL,
    t4."FASTRETURNMEASSPT",
    t4."FDDFASTRETURNRSRPTH",
    t4."FDDLTEOFFSET",
    t4."GERANPRI",
    t4."HPRIO",
    t4."QPEUTRAN",
    t4."SI2QUATEROPTFORLTESW",
    t4."TDDFASTRETURNRSRPTH",
    t4."TDDLTEOFFSET",
    t4."THREUTRANHIGH",
    t4."THREUTRANLOW",
    t4."THREUTRANRPT",
    t4."THRGSMLOW",
    t4."THRPRISEARCH",
    t4."THRUTRANHIGH",
    t4."THRUTRANLOW",
    t4."TRESEL",
    t4."UTRANPRI",
    t4."UTRANQRXLEVMIN"
FROM
huawei_mml_gsm."GCELLPRIEUTRANSYS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPRIVATEOPTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPRIVATEOPTPARA"',
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
    t1."ADVESTDLTBFRELDELAY",
    t1."BKGARP1DLRELDELAY",
    t1."BKGARP2DLRELDELAY",
    t1."BKGARP3DLRELDLAY",
    t1."CELLID",
    t1."CELLPSRESERVEPARA4",
    t1."DLASSRETRYTIMESMAX",
    t1."DLLIMITULPDALLOCSW",
    t1."DLRELDELAYACKOPT",
    t1."DLRELDELAYRLCUNACKMODE",
    t1."DLTBFESTDELAY",
    t1."DNTBFRELDELAY",
    t1."FIRSTBLKCV0INACTPERDPERMIT",
    t1."IMDLTBFRELDELAY",
    t1."POCRELDELAY",
    t1."POLLINGRETRYTIMESMAX",
    t1."PSDTX",
    t1."PSDTXPRDDUMMY",
    t1."PSUMENHANCESW",
    t1."QUICKSTARTDLASSRESNDOPTSW",
    t1."QUICKSTARTDLTBFRELOPTSW",
    t1."REASSIGNRESENDSW",
    t1."T3169",
    t1."T3191",
    t1."T3195",
    t1."THP1ARP1DLRELDELAY",
    t1."THP1ARP2DLRELDELAY",
    t1."THP1ARP3DLRELDELAY",
    t1."THP2ARP1DLRELDELAY",
    t1."THP2ARP2DLRELDELAY",
    t1."THP2ARP3DLRELDELAY",
    t1."THP3ARP1DLRELDELAY",
    t1."THP3ARP2DLRELDELAY",
    t1."THP3ARP3DLRELDELAY",
    t1."ULEXTERNACKOPT",
    t1."ULRELDELAYRLCUNACKMODE",
    t1."UPEXTTBFINACTDELAY",
    t1."UPTBFRELDELAY"
FROM
huawei_nbi_gsm."GCELLPRIVATEOPTPARA" t1

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
    t2."ADVESTDLTBFRELDELAY",
    t2."BKGARP1DLRELDELAY",
    t2."BKGARP2DLRELDELAY",
    t2."BKGARP3DLRELDLAY",
    t2."CELLID",
    t2."CELLPSRESERVEPARA4",
    t2."DLASSRETRYTIMESMAX",
    t2."DLLIMITULPDALLOCSW",
    t2."DLRELDELAYACKOPT",
    t2."DLRELDELAYRLCUNACKMODE",
    t2."DLTBFESTDELAY",
    t2."DNTBFRELDELAY",
    t2."FIRSTBLKCV0INACTPERDPERMIT",
    t2."IMDLTBFRELDELAY",
    t2."POCRELDELAY",
    t2."POLLINGRETRYTIMESMAX",
    t2."PSDTX",
    t2."PSDTXPRDDUMMY",
    NULL,
    t2."QUICKSTARTDLASSRESNDOPTSW",
    t2."QUICKSTARTDLTBFRELOPTSW",
    t2."REASSIGNRESENDSW",
    t2."T3169",
    t2."T3191",
    t2."T3195",
    t2."THP1ARP1DLRELDELAY",
    t2."THP1ARP2DLRELDELAY",
    t2."THP1ARP3DLRELDELAY",
    t2."THP2ARP1DLRELDELAY",
    t2."THP2ARP2DLRELDELAY",
    t2."THP2ARP3DLRELDELAY",
    t2."THP3ARP1DLRELDELAY",
    t2."THP3ARP2DLRELDELAY",
    t2."THP3ARP3DLRELDELAY",
    t2."ULEXTERNACKOPT",
    t2."ULRELDELAYRLCUNACKMODE",
    t2."UPEXTTBFINACTDELAY",
    t2."UPTBFRELDELAY"
FROM
huawei_gexport_gsm."GCELLPRIVATEOPTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADVESTDLTBFRELDELAY",
    t3."BKGARP1DLRELDELAY",
    t3."BKGARP2DLRELDELAY",
    t3."BKGARP3DLRELDLAY",
    t3."CELLID",
    t3."CELLPSRESERVEPARA4",
    t3."DLASSRETRYTIMESMAX",
    t3."DLLIMITULPDALLOCSW",
    t3."DLRELDELAYACKOPT",
    t3."DLRELDELAYRLCUNACKMODE",
    t3."DLTBFESTDELAY",
    t3."DNTBFRELDELAY",
    t3."FIRSTBLKCV0INACTPERDPERMIT",
    t3."IMDLTBFRELDELAY",
    t3."POCRELDELAY",
    t3."POLLINGRETRYTIMESMAX",
    t3."PSDTX",
    t3."PSDTXPRDDUMMY",
    NULL,
    t3."QUICKSTARTDLASSRESNDOPTSW",
    t3."QUICKSTARTDLTBFRELOPTSW",
    t3."REASSIGNRESENDSW",
    t3."T3169",
    t3."T3191",
    t3."T3195",
    t3."THP1ARP1DLRELDELAY",
    t3."THP1ARP2DLRELDELAY",
    t3."THP1ARP3DLRELDELAY",
    t3."THP2ARP1DLRELDELAY",
    t3."THP2ARP2DLRELDELAY",
    t3."THP2ARP3DLRELDELAY",
    t3."THP3ARP1DLRELDELAY",
    t3."THP3ARP2DLRELDELAY",
    t3."THP3ARP3DLRELDELAY",
    t3."ULEXTERNACKOPT",
    t3."ULRELDELAYRLCUNACKMODE",
    t3."UPEXTTBFINACTDELAY",
    t3."UPTBFRELDELAY"
FROM
huawei_gexport_gsm."GCELLPRIVATEOPTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ADVESTDLTBFRELDELAY",
    t4."BKGARP1DLRELDELAY",
    t4."BKGARP2DLRELDELAY",
    t4."BKGARP3DLRELDLAY",
    t4."CELLID",
    t4."CELLPSRESERVEPARA4",
    t4."DLASSRETRYTIMESMAX",
    t4."DLLIMITULPDALLOCSW",
    t4."DLRELDELAYACKOPT",
    t4."DLRELDELAYRLCUNACKMODE",
    t4."DLTBFESTDELAY",
    t4."DNTBFRELDELAY",
    t4."FIRSTBLKCV0INACTPERDPERMIT",
    t4."IMDLTBFRELDELAY",
    t4."POCRELDELAY",
    t4."POLLINGRETRYTIMESMAX",
    t4."PSDTX",
    t4."PSDTXPRDDUMMY",
    NULL,
    t4."QUICKSTARTDLASSRESNDOPTSW",
    t4."QUICKSTARTDLTBFRELOPTSW",
    t4."REASSIGNRESENDSW",
    t4."T3169",
    t4."T3191",
    t4."T3195",
    t4."THP1ARP1DLRELDELAY",
    t4."THP1ARP2DLRELDELAY",
    t4."THP1ARP3DLRELDELAY",
    t4."THP2ARP1DLRELDELAY",
    t4."THP2ARP2DLRELDELAY",
    t4."THP2ARP3DLRELDELAY",
    t4."THP3ARP1DLRELDELAY",
    t4."THP3ARP2DLRELDELAY",
    t4."THP3ARP3DLRELDELAY",
    t4."ULEXTERNACKOPT",
    t4."ULRELDELAYRLCUNACKMODE",
    t4."UPEXTTBFINACTDELAY",
    t4."UPTBFRELDELAY"
FROM
huawei_mml_gsm."GCELLPRIVATEOPTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSABISPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPSABISPARA"',
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
    t1."ABISIPMAXTRANSDELAY",
    t1."ABISIPPROTECTDURA",
    t1."CELLID",
    t1."JITTERBUFFERAUTOADJUST",
    t1."NORMALCELLTRANSDELAY"
FROM
huawei_nbi_gsm."GCELLPSABISPARA" t1

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
    t2."ABISIPMAXTRANSDELAY",
    t2."ABISIPPROTECTDURA",
    t2."CELLID",
    t2."JITTERBUFFERAUTOADJUST",
    t2."NORMALCELLTRANSDELAY"
FROM
huawei_gexport_gsm."GCELLPSABISPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISIPMAXTRANSDELAY",
    t3."ABISIPPROTECTDURA",
    t3."CELLID",
    t3."JITTERBUFFERAUTOADJUST",
    t3."NORMALCELLTRANSDELAY"
FROM
huawei_gexport_gsm."GCELLPSABISPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISIPMAXTRANSDELAY",
    t4."ABISIPPROTECTDURA",
    t4."CELLID",
    t4."JITTERBUFFERAUTOADJUST",
    t4."NORMALCELLTRANSDELAY"
FROM
huawei_mml_gsm."GCELLPSABISPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSBASE = ReplaceableObject(
    'huawei_cm_2g."GCELLPSBASE"',
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
    t1."ACCBURST",
    t1."ACCTECHREQSW",
    t1."BSCVMAX",
    t1."BSSPAGINGCOORDINATION",
    t1."CELLID",
    t1."CTRLACKTYPE",
    t1."DRXTIMERMAX",
    t1."EARLYTBFEST",
    t1."EGPRS11BITCHANREQ",
    t1."EXTUTBFNODATA",
    t1."INACTSCHPERIOD",
    t1."NCO",
    t1."NMO",
    t1."PANDEC",
    t1."PANINC",
    t1."PANMAX",
    t1."PRIACCTHR",
    t1."PSDTXLAOPTISWITCH",
    t1."RACOLOR",
    t1."SGSNR",
    t1."SPGCCCCHSUP",
    t1."T3168",
    t1."T3192",
    t1."T3192CONTENSOLUTSW",
    t1."UPDTXACKPERIOD"
FROM
huawei_nbi_gsm."GCELLPSBASE" t1

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
    t2."ACCBURST",
    t2."ACCTECHREQSW",
    t2."BSCVMAX",
    t2."BSSPAGINGCOORDINATION",
    t2."CELLID",
    t2."CTRLACKTYPE",
    t2."DRXTIMERMAX",
    t2."EARLYTBFEST",
    t2."EGPRS11BITCHANREQ",
    t2."EXTUTBFNODATA",
    t2."INACTSCHPERIOD",
    t2."NCO",
    t2."NMO",
    t2."PANDEC",
    t2."PANINC",
    t2."PANMAX",
    t2."PRIACCTHR",
    t2."PSDTXLAOPTISWITCH",
    t2."RACOLOR",
    t2."SGSNR",
    t2."SPGCCCCHSUP",
    t2."T3168",
    t2."T3192",
    t2."T3192CONTENSOLUTSW",
    t2."UPDTXACKPERIOD"
FROM
huawei_gexport_gsm."GCELLPSBASE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACCBURST",
    t3."ACCTECHREQSW",
    t3."BSCVMAX",
    t3."BSSPAGINGCOORDINATION",
    t3."CELLID",
    t3."CTRLACKTYPE",
    t3."DRXTIMERMAX",
    t3."EARLYTBFEST",
    t3."EGPRS11BITCHANREQ",
    t3."EXTUTBFNODATA",
    t3."INACTSCHPERIOD",
    t3."NCO",
    t3."NMO",
    t3."PANDEC",
    t3."PANINC",
    t3."PANMAX",
    t3."PRIACCTHR",
    t3."PSDTXLAOPTISWITCH",
    t3."RACOLOR",
    t3."SGSNR",
    t3."SPGCCCCHSUP",
    t3."T3168",
    t3."T3192",
    t3."T3192CONTENSOLUTSW",
    t3."UPDTXACKPERIOD"
FROM
huawei_gexport_gsm."GCELLPSBASE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACCBURST",
    t4."ACCTECHREQSW",
    t4."BSCVMAX",
    t4."BSSPAGINGCOORDINATION",
    t4."CELLID",
    t4."CTRLACKTYPE",
    t4."DRXTIMERMAX",
    t4."EARLYTBFEST",
    t4."EGPRS11BITCHANREQ",
    t4."EXTUTBFNODATA",
    t4."INACTSCHPERIOD",
    t4."NCO",
    t4."NMO",
    t4."PANDEC",
    t4."PANINC",
    t4."PANMAX",
    t4."PRIACCTHR",
    t4."PSDTXLAOPTISWITCH",
    t4."RACOLOR",
    t4."SGSNR",
    t4."SPGCCCCHSUP",
    t4."T3168",
    t4."T3192",
    t4."T3192CONTENSOLUTSW",
    t4."UPDTXACKPERIOD"
FROM
huawei_mml_gsm."GCELLPSBASE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSCHM = ReplaceableObject(
    'huawei_cm_2g."GCELLPSCHM"',
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
    t1."ABISTSFREETM",
    t1."ACTIVETBFSWITCH",
    t1."ALLOCSINGLEPDCHFORSIGNALLING",
    t1."APPLYMULTIABISTS",
    t1."AUTOGPRSCHPRI",
    t1."BEARP1PRIMAXPDCHNUM",
    t1."BEARP1PRIWEIGHT",
    t1."BEARP2PRIMAXPDCHNUM",
    t1."BEARP2PRIWEIGHT",
    t1."BEARP3PRIMAXPDCHNUM",
    t1."BEARP3PRIWEIGHT",
    t1."BKGARP1PDCHWEIGHT",
    t1."BKGARP1PRIMAXPDCHNUM",
    t1."BKGARP1PRIWEIGHT",
    t1."BKGARP2PDCHWEIGHT",
    t1."BKGARP2PRIMAXPDCHNUM",
    t1."BKGARP2PRIWEIGHT",
    t1."BKGARP3PDCHWEIGHT",
    t1."BKGARP3PRIMAXPDCHNUM",
    t1."BKGARP3PRIWEIGHT",
    t1."CELLID",
    t1."CHIDLHIGHTHR",
    t1."CHIDLLOWTHR",
    t1."CSBUSYPDAPPINTERVAL",
    t1."DEFAULTDYNPDCHPRETRANNUM",
    t1."DUTYCYCLEBASEDPDCHMAG",
    t1."DWNDYNCHNTRANLEV",
    t1."DYNCHFREETM",
    t1."DYNCHNPREEMPTLEV",
    t1."DYNCHTRANRESLEV",
    t1."ENPDADMINOPT",
    t1."GPRSLOADOPT",
    t1."IMARP1PRIMAXPDCHNUM",
    t1."IMARP1PRIWEIGHT",
    t1."IMARP2PRIMAXPDCHNUM",
    t1."IMARP2PRIWEIGHT",
    t1."IMARP3PRIMAXPDCHNUM",
    t1."IMARP3PRIWEIGHT",
    t1."IMOPTTHRSH",
    t1."IMPDCHMULTIPLEXWEIGHT",
    t1."IOUPDCHSWTICH",
    t1."IUOCHNTRAN",
    t1."IUOCHNTRANPOLICY",
    t1."MAXMULCLSPDCHCVTENSW",
    t1."MAXPDCHRATE",
    t1."MSRDMCSLEV",
    t1."MSRDPDCHLEV",
    t1."PDCHDWNLEV",
    t1."PDCHPOWERPLENT",
    t1."PDCHPOWERPLENTTHRES",
    t1."PDCHREFORMING",
    t1."PDCHUPLEV",
    t1."POWTUNIT",
    t1."PRECONNECTSLAVEABIS",
    t1."PSDUALTHROPTSW",
    t1."PSRESPREEMPT",
    t1."PSRESPREEMPTED",
    t1."PSSERVICEBUSYTHRESHOLD",
    t1."RADIORESADAADJDLLOADTHD",
    t1."RADIORESADAADJSWITCH",
    t1."RADIORESADAADJULLOADTHD",
    t1."RAMBCAP",
    t1."RESERVEDDYNPDCHPRETRANNUM",
    t1."RTTIPDCHMULTIPLEXTHRESH",
    t1."THP1ARP1PDCHWEIGHT",
    t1."THP1ARP1PRIMAXPDCHNUM",
    t1."THP1ARP1PRIWEIGHT",
    t1."THP1ARP2PDCHWEIGHT",
    t1."THP1ARP2PRIMAXPDCHNUM",
    t1."THP1ARP2PRIWEIGHT",
    t1."THP1ARP3PDCHWEIGHT",
    t1."THP1ARP3PRIMAXPDCHNUM",
    t1."THP1ARP3PRIWEIGHT",
    t1."THP2ARP1PDCHWEIGHT",
    t1."THP2ARP1PRIMAXPDCHNUM",
    t1."THP2ARP1PRIWEIGHT",
    t1."THP2ARP2PDCHWEIGHT",
    t1."THP2ARP2PRIMAXPDCHNUM",
    t1."THP2ARP2PRIWEIGHT",
    t1."THP2ARP3PDCHWEIGHT",
    t1."THP2ARP3PRIMAXPDCHNUM",
    t1."THP2ARP3PRIWEIGHT",
    t1."THP3ARP1PDCHWEIGHT",
    t1."THP3ARP1PRIMAXPDCHNUM",
    t1."THP3ARP1PRIWEIGHT",
    t1."THP3ARP2PDCHWEIGHT",
    t1."THP3ARP2PRIMAXPDCHNUM",
    t1."THP3ARP2PRIWEIGHT",
    t1."THP3ARP3PDCHWEIGHT",
    t1."THP3ARP3PRIMAXPDCHNUM",
    t1."THP3ARP3PRIWEIGHT",
    t1."TWOTHLDCNVTONOTHERTRXSW",
    t1."UPDYNCHNTRANLEV",
    t1."DWNDYNCHNRETRANLEV",
    t1."UPDYNCHNRETRANLEV",
    t1."ACTIVETBFDWNDYNCHNTRANLEV",
    t1."ACTIVETBFUPDYNCHNTRANLEV"
FROM
huawei_nbi_gsm."GCELLPSCHM" t1

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
    t2."ABISTSFREETM",
    t2."ACTIVETBFSWITCH",
    t2."ALLOCSINGLEPDCHFORSIGNALLING",
    t2."APPLYMULTIABISTS",
    t2."AUTOGPRSCHPRI",
    t2."BEARP1PRIMAXPDCHNUM",
    t2."BEARP1PRIWEIGHT",
    t2."BEARP2PRIMAXPDCHNUM",
    t2."BEARP2PRIWEIGHT",
    t2."BEARP3PRIMAXPDCHNUM",
    t2."BEARP3PRIWEIGHT",
    t2."BKGARP1PDCHWEIGHT",
    t2."BKGARP1PRIMAXPDCHNUM",
    t2."BKGARP1PRIWEIGHT",
    t2."BKGARP2PDCHWEIGHT",
    t2."BKGARP2PRIMAXPDCHNUM",
    t2."BKGARP2PRIWEIGHT",
    t2."BKGARP3PDCHWEIGHT",
    t2."BKGARP3PRIMAXPDCHNUM",
    t2."BKGARP3PRIWEIGHT",
    t2."CELLID",
    t2."CHIDLHIGHTHR",
    t2."CHIDLLOWTHR",
    t2."CSBUSYPDAPPINTERVAL",
    t2."DEFAULTDYNPDCHPRETRANNUM",
    t2."DUTYCYCLEBASEDPDCHMAG",
    t2."DWNDYNCHNTRANLEV",
    t2."DYNCHFREETM",
    t2."DYNCHNPREEMPTLEV",
    t2."DYNCHTRANRESLEV",
    t2."ENPDADMINOPT",
    t2."GPRSLOADOPT",
    t2."IMARP1PRIMAXPDCHNUM",
    t2."IMARP1PRIWEIGHT",
    t2."IMARP2PRIMAXPDCHNUM",
    t2."IMARP2PRIWEIGHT",
    t2."IMARP3PRIMAXPDCHNUM",
    t2."IMARP3PRIWEIGHT",
    t2."IMOPTTHRSH",
    t2."IMPDCHMULTIPLEXWEIGHT",
    t2."IOUPDCHSWTICH",
    t2."IUOCHNTRAN",
    t2."IUOCHNTRANPOLICY",
    t2."MAXMULCLSPDCHCVTENSW",
    t2."MAXPDCHRATE",
    t2."MSRDMCSLEV",
    t2."MSRDPDCHLEV",
    t2."PDCHDWNLEV",
    t2."PDCHPOWERPLENT",
    t2."PDCHPOWERPLENTTHRES",
    t2."PDCHREFORMING",
    t2."PDCHUPLEV",
    t2."POWTUNIT",
    t2."PRECONNECTSLAVEABIS",
    t2."PSDUALTHROPTSW",
    t2."PSRESPREEMPT",
    t2."PSRESPREEMPTED",
    t2."PSSERVICEBUSYTHRESHOLD",
    t2."RADIORESADAADJDLLOADTHD",
    t2."RADIORESADAADJSWITCH",
    t2."RADIORESADAADJULLOADTHD",
    t2."RAMBCAP",
    t2."RESERVEDDYNPDCHPRETRANNUM",
    t2."RTTIPDCHMULTIPLEXTHRESH",
    t2."THP1ARP1PDCHWEIGHT",
    t2."THP1ARP1PRIMAXPDCHNUM",
    t2."THP1ARP1PRIWEIGHT",
    t2."THP1ARP2PDCHWEIGHT",
    t2."THP1ARP2PRIMAXPDCHNUM",
    t2."THP1ARP2PRIWEIGHT",
    t2."THP1ARP3PDCHWEIGHT",
    t2."THP1ARP3PRIMAXPDCHNUM",
    t2."THP1ARP3PRIWEIGHT",
    t2."THP2ARP1PDCHWEIGHT",
    t2."THP2ARP1PRIMAXPDCHNUM",
    t2."THP2ARP1PRIWEIGHT",
    t2."THP2ARP2PDCHWEIGHT",
    t2."THP2ARP2PRIMAXPDCHNUM",
    t2."THP2ARP2PRIWEIGHT",
    t2."THP2ARP3PDCHWEIGHT",
    t2."THP2ARP3PRIMAXPDCHNUM",
    t2."THP2ARP3PRIWEIGHT",
    t2."THP3ARP1PDCHWEIGHT",
    t2."THP3ARP1PRIMAXPDCHNUM",
    t2."THP3ARP1PRIWEIGHT",
    t2."THP3ARP2PDCHWEIGHT",
    t2."THP3ARP2PRIMAXPDCHNUM",
    t2."THP3ARP2PRIWEIGHT",
    t2."THP3ARP3PDCHWEIGHT",
    t2."THP3ARP3PRIMAXPDCHNUM",
    t2."THP3ARP3PRIWEIGHT",
    t2."TWOTHLDCNVTONOTHERTRXSW",
    t2."UPDYNCHNTRANLEV",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLPSCHM_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISTSFREETM",
    t3."ACTIVETBFSWITCH",
    t3."ALLOCSINGLEPDCHFORSIGNALLING",
    t3."APPLYMULTIABISTS",
    t3."AUTOGPRSCHPRI",
    t3."BEARP1PRIMAXPDCHNUM",
    t3."BEARP1PRIWEIGHT",
    t3."BEARP2PRIMAXPDCHNUM",
    t3."BEARP2PRIWEIGHT",
    t3."BEARP3PRIMAXPDCHNUM",
    t3."BEARP3PRIWEIGHT",
    t3."BKGARP1PDCHWEIGHT",
    t3."BKGARP1PRIMAXPDCHNUM",
    t3."BKGARP1PRIWEIGHT",
    t3."BKGARP2PDCHWEIGHT",
    t3."BKGARP2PRIMAXPDCHNUM",
    t3."BKGARP2PRIWEIGHT",
    t3."BKGARP3PDCHWEIGHT",
    t3."BKGARP3PRIMAXPDCHNUM",
    t3."BKGARP3PRIWEIGHT",
    t3."CELLID",
    t3."CHIDLHIGHTHR",
    t3."CHIDLLOWTHR",
    t3."CSBUSYPDAPPINTERVAL",
    t3."DEFAULTDYNPDCHPRETRANNUM",
    t3."DUTYCYCLEBASEDPDCHMAG",
    t3."DWNDYNCHNTRANLEV",
    t3."DYNCHFREETM",
    t3."DYNCHNPREEMPTLEV",
    t3."DYNCHTRANRESLEV",
    t3."ENPDADMINOPT",
    t3."GPRSLOADOPT",
    t3."IMARP1PRIMAXPDCHNUM",
    t3."IMARP1PRIWEIGHT",
    t3."IMARP2PRIMAXPDCHNUM",
    t3."IMARP2PRIWEIGHT",
    t3."IMARP3PRIMAXPDCHNUM",
    t3."IMARP3PRIWEIGHT",
    t3."IMOPTTHRSH",
    t3."IMPDCHMULTIPLEXWEIGHT",
    t3."IOUPDCHSWTICH",
    t3."IUOCHNTRAN",
    t3."IUOCHNTRANPOLICY",
    t3."MAXMULCLSPDCHCVTENSW",
    t3."MAXPDCHRATE",
    t3."MSRDMCSLEV",
    t3."MSRDPDCHLEV",
    t3."PDCHDWNLEV",
    t3."PDCHPOWERPLENT",
    t3."PDCHPOWERPLENTTHRES",
    t3."PDCHREFORMING",
    t3."PDCHUPLEV",
    t3."POWTUNIT",
    t3."PRECONNECTSLAVEABIS",
    t3."PSDUALTHROPTSW",
    t3."PSRESPREEMPT",
    t3."PSRESPREEMPTED",
    t3."PSSERVICEBUSYTHRESHOLD",
    t3."RADIORESADAADJDLLOADTHD",
    t3."RADIORESADAADJSWITCH",
    t3."RADIORESADAADJULLOADTHD",
    t3."RAMBCAP",
    t3."RESERVEDDYNPDCHPRETRANNUM",
    t3."RTTIPDCHMULTIPLEXTHRESH",
    t3."THP1ARP1PDCHWEIGHT",
    t3."THP1ARP1PRIMAXPDCHNUM",
    t3."THP1ARP1PRIWEIGHT",
    t3."THP1ARP2PDCHWEIGHT",
    t3."THP1ARP2PRIMAXPDCHNUM",
    t3."THP1ARP2PRIWEIGHT",
    t3."THP1ARP3PDCHWEIGHT",
    t3."THP1ARP3PRIMAXPDCHNUM",
    t3."THP1ARP3PRIWEIGHT",
    t3."THP2ARP1PDCHWEIGHT",
    t3."THP2ARP1PRIMAXPDCHNUM",
    t3."THP2ARP1PRIWEIGHT",
    t3."THP2ARP2PDCHWEIGHT",
    t3."THP2ARP2PRIMAXPDCHNUM",
    t3."THP2ARP2PRIWEIGHT",
    t3."THP2ARP3PDCHWEIGHT",
    t3."THP2ARP3PRIMAXPDCHNUM",
    t3."THP2ARP3PRIWEIGHT",
    t3."THP3ARP1PDCHWEIGHT",
    t3."THP3ARP1PRIMAXPDCHNUM",
    t3."THP3ARP1PRIWEIGHT",
    t3."THP3ARP2PDCHWEIGHT",
    t3."THP3ARP2PRIMAXPDCHNUM",
    t3."THP3ARP2PRIWEIGHT",
    t3."THP3ARP3PDCHWEIGHT",
    t3."THP3ARP3PRIMAXPDCHNUM",
    t3."THP3ARP3PRIWEIGHT",
    t3."TWOTHLDCNVTONOTHERTRXSW",
    t3."UPDYNCHNTRANLEV",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLPSCHM_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISTSFREETM",
    t4."ACTIVETBFSWITCH",
    t4."ALLOCSINGLEPDCHFORSIGNALLING",
    t4."APPLYMULTIABISTS",
    t4."AUTOGPRSCHPRI",
    t4."BEARP1PRIMAXPDCHNUM",
    t4."BEARP1PRIWEIGHT",
    t4."BEARP2PRIMAXPDCHNUM",
    t4."BEARP2PRIWEIGHT",
    t4."BEARP3PRIMAXPDCHNUM",
    t4."BEARP3PRIWEIGHT",
    t4."BKGARP1PDCHWEIGHT",
    t4."BKGARP1PRIMAXPDCHNUM",
    t4."BKGARP1PRIWEIGHT",
    t4."BKGARP2PDCHWEIGHT",
    t4."BKGARP2PRIMAXPDCHNUM",
    t4."BKGARP2PRIWEIGHT",
    t4."BKGARP3PDCHWEIGHT",
    t4."BKGARP3PRIMAXPDCHNUM",
    t4."BKGARP3PRIWEIGHT",
    t4."CELLID",
    t4."CHIDLHIGHTHR",
    t4."CHIDLLOWTHR",
    t4."CSBUSYPDAPPINTERVAL",
    t4."DEFAULTDYNPDCHPRETRANNUM",
    t4."DUTYCYCLEBASEDPDCHMAG",
    t4."DWNDYNCHNTRANLEV",
    t4."DYNCHFREETM",
    t4."DYNCHNPREEMPTLEV",
    t4."DYNCHTRANRESLEV",
    t4."ENPDADMINOPT",
    t4."GPRSLOADOPT",
    t4."IMARP1PRIMAXPDCHNUM",
    t4."IMARP1PRIWEIGHT",
    t4."IMARP2PRIMAXPDCHNUM",
    t4."IMARP2PRIWEIGHT",
    t4."IMARP3PRIMAXPDCHNUM",
    t4."IMARP3PRIWEIGHT",
    t4."IMOPTTHRSH",
    t4."IMPDCHMULTIPLEXWEIGHT",
    t4."IOUPDCHSWTICH",
    t4."IUOCHNTRAN",
    t4."IUOCHNTRANPOLICY",
    t4."MAXMULCLSPDCHCVTENSW",
    t4."MAXPDCHRATE",
    t4."MSRDMCSLEV",
    t4."MSRDPDCHLEV",
    t4."PDCHDWNLEV",
    t4."PDCHPOWERPLENT",
    t4."PDCHPOWERPLENTTHRES",
    t4."PDCHREFORMING",
    t4."PDCHUPLEV",
    t4."POWTUNIT",
    t4."PRECONNECTSLAVEABIS",
    t4."PSDUALTHROPTSW",
    t4."PSRESPREEMPT",
    t4."PSRESPREEMPTED",
    t4."PSSERVICEBUSYTHRESHOLD",
    t4."RADIORESADAADJDLLOADTHD",
    t4."RADIORESADAADJSWITCH",
    t4."RADIORESADAADJULLOADTHD",
    t4."RAMBCAP",
    t4."RESERVEDDYNPDCHPRETRANNUM",
    t4."RTTIPDCHMULTIPLEXTHRESH",
    t4."THP1ARP1PDCHWEIGHT",
    t4."THP1ARP1PRIMAXPDCHNUM",
    t4."THP1ARP1PRIWEIGHT",
    t4."THP1ARP2PDCHWEIGHT",
    t4."THP1ARP2PRIMAXPDCHNUM",
    t4."THP1ARP2PRIWEIGHT",
    t4."THP1ARP3PDCHWEIGHT",
    t4."THP1ARP3PRIMAXPDCHNUM",
    t4."THP1ARP3PRIWEIGHT",
    t4."THP2ARP1PDCHWEIGHT",
    t4."THP2ARP1PRIMAXPDCHNUM",
    t4."THP2ARP1PRIWEIGHT",
    t4."THP2ARP2PDCHWEIGHT",
    t4."THP2ARP2PRIMAXPDCHNUM",
    t4."THP2ARP2PRIWEIGHT",
    t4."THP2ARP3PDCHWEIGHT",
    t4."THP2ARP3PRIMAXPDCHNUM",
    t4."THP2ARP3PRIWEIGHT",
    t4."THP3ARP1PDCHWEIGHT",
    t4."THP3ARP1PRIMAXPDCHNUM",
    t4."THP3ARP1PRIWEIGHT",
    t4."THP3ARP2PDCHWEIGHT",
    t4."THP3ARP2PRIMAXPDCHNUM",
    t4."THP3ARP2PRIWEIGHT",
    t4."THP3ARP3PDCHWEIGHT",
    t4."THP3ARP3PRIMAXPDCHNUM",
    t4."THP3ARP3PRIWEIGHT",
    t4."TWOTHLDCNVTONOTHERTRXSW",
    t4."UPDYNCHNTRANLEV",
    NULL,
    NULL,
    t4."ACTIVETBFDWNDYNCHNTRANLEV",
    t4."ACTIVETBFUPDYNCHNTRANLEV"
FROM
huawei_mml_gsm."GCELLPSCHM" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSCS = ReplaceableObject(
    'huawei_cm_2g."GCELLPSCS"',
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
    t1."DLCSADJOPTSW",
    t1."DNDEFAULTCS",
    t1."DNFIXCS",
    t1."DNTHDCSDEGRADE1",
    t1."DNTHDCSDEGRADE2",
    t1."DNTHDCSDEGRADE3",
    t1."DNTHDCSUPGRADE1",
    t1."DNTHDCSUPGRADE2",
    t1."DNTHDCSUPGRADE3",
    t1."UPDEFAULTCS",
    t1."UPFIXCS",
    t1."UPTHDCSDEGRADE1",
    t1."UPTHDCSDEGRADE2",
    t1."UPTHDCSDEGRADE3",
    t1."UPTHDCSUPGRADE1",
    t1."UPTHDCSUPGRADE2",
    t1."UPTHDCSUPGRADE3"
FROM
huawei_nbi_gsm."GCELLPSCS" t1

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
    t2."DLCSADJOPTSW",
    t2."DNDEFAULTCS",
    t2."DNFIXCS",
    t2."DNTHDCSDEGRADE1",
    t2."DNTHDCSDEGRADE2",
    t2."DNTHDCSDEGRADE3",
    t2."DNTHDCSUPGRADE1",
    t2."DNTHDCSUPGRADE2",
    t2."DNTHDCSUPGRADE3",
    t2."UPDEFAULTCS",
    t2."UPFIXCS",
    t2."UPTHDCSDEGRADE1",
    t2."UPTHDCSDEGRADE2",
    t2."UPTHDCSDEGRADE3",
    t2."UPTHDCSUPGRADE1",
    t2."UPTHDCSUPGRADE2",
    t2."UPTHDCSUPGRADE3"
FROM
huawei_gexport_gsm."GCELLPSCS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DLCSADJOPTSW",
    t3."DNDEFAULTCS",
    t3."DNFIXCS",
    t3."DNTHDCSDEGRADE1",
    t3."DNTHDCSDEGRADE2",
    t3."DNTHDCSDEGRADE3",
    t3."DNTHDCSUPGRADE1",
    t3."DNTHDCSUPGRADE2",
    t3."DNTHDCSUPGRADE3",
    t3."UPDEFAULTCS",
    t3."UPFIXCS",
    t3."UPTHDCSDEGRADE1",
    t3."UPTHDCSDEGRADE2",
    t3."UPTHDCSDEGRADE3",
    t3."UPTHDCSUPGRADE1",
    t3."UPTHDCSUPGRADE2",
    t3."UPTHDCSUPGRADE3"
FROM
huawei_gexport_gsm."GCELLPSCS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DLCSADJOPTSW",
    t4."DNDEFAULTCS",
    t4."DNFIXCS",
    t4."DNTHDCSDEGRADE1",
    t4."DNTHDCSDEGRADE2",
    t4."DNTHDCSDEGRADE3",
    t4."DNTHDCSUPGRADE1",
    t4."DNTHDCSUPGRADE2",
    t4."DNTHDCSUPGRADE3",
    t4."UPDEFAULTCS",
    t4."UPFIXCS",
    t4."UPTHDCSDEGRADE1",
    t4."UPTHDCSDEGRADE2",
    t4."UPTHDCSDEGRADE3",
    t4."UPTHDCSUPGRADE1",
    t4."UPTHDCSUPGRADE2",
    t4."UPTHDCSUPGRADE3"
FROM
huawei_mml_gsm."GCELLPSCS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSDIFFSERVICE = ReplaceableObject(
    'huawei_cm_2g."GCELLPSDIFFSERVICE"',
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
    t1."EMAILARP1MAXPDCHNUM",
    t1."EMAILARP1WEIGHT",
    t1."EMAILARP2MAXPDCHNUM",
    t1."EMAILARP2WEIGHT",
    t1."EMAILARP3MAXPDCHNUM",
    t1."EMAILARP3WEIGHT",
    t1."EMAILDLTBFRELDELAY",
    t1."EMAILOPT",
    t1."EMAILPDCHMULTIPLEXWEIGHT",
    t1."IMARP1MAXPDCHNUM",
    t1."IMARP1WEIGHT",
    t1."IMARP2MAXPDCHNUM",
    t1."IMARP2WEIGHT",
    t1."IMARP3MAXPDCHNUM",
    t1."IMARP3WEIGHT",
    t1."IMDLTBFRELDELAY",
    t1."IMOPT",
    t1."IMPDCHMULTIPLEXWEIGHT",
    t1."P2PARP1MAXPDCHNUM",
    t1."P2PARP1WEIGHT",
    t1."P2PARP2MAXPDCHNUM",
    t1."P2PARP2WEIGHT",
    t1."P2PARP3MAXPDCHNUM",
    t1."P2PARP3WEIGHT",
    t1."P2PDLTBFRELDELAY",
    t1."P2POPT",
    t1."P2PPDCHMULTIPLEXWEIGHT",
    t1."SERVTYPERTUPDATESW",
    t1."STREAMINGARP1MAXPDCHNUM",
    t1."STREAMINGARP1WEIGHT",
    t1."STREAMINGARP2MAXPDCHNUM",
    t1."STREAMINGARP2WEIGHT",
    t1."STREAMINGARP3MAXPDCHNUM",
    t1."STREAMINGARP3WEIGHT",
    t1."STREAMINGDLTBFRELDELAY",
    t1."STREAMINGOPT",
    t1."STREAMPDCHMULTIPLEXWEIGHT",
    t1."WEBARP1MAXPDCHNUM",
    t1."WEBARP1WEIGHT",
    t1."WEBARP2MAXPDCHNUM",
    t1."WEBARP2WEIGHT",
    t1."WEBARP3MAXPDCHNUM",
    t1."WEBARP3WEIGHT",
    t1."WEBDLTBFRELDELAY",
    t1."WEBOPT",
    t1."WEBPDCHMULTIPLEXWEIGHT"
FROM
huawei_nbi_gsm."GCELLPSDIFFSERVICE" t1

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
    t2."EMAILARP1MAXPDCHNUM",
    t2."EMAILARP1WEIGHT",
    t2."EMAILARP2MAXPDCHNUM",
    t2."EMAILARP2WEIGHT",
    t2."EMAILARP3MAXPDCHNUM",
    t2."EMAILARP3WEIGHT",
    t2."EMAILDLTBFRELDELAY",
    t2."EMAILOPT",
    t2."EMAILPDCHMULTIPLEXWEIGHT",
    t2."IMARP1MAXPDCHNUM",
    t2."IMARP1WEIGHT",
    t2."IMARP2MAXPDCHNUM",
    t2."IMARP2WEIGHT",
    t2."IMARP3MAXPDCHNUM",
    t2."IMARP3WEIGHT",
    t2."IMDLTBFRELDELAY",
    t2."IMOPT",
    t2."IMPDCHMULTIPLEXWEIGHT",
    t2."P2PARP1MAXPDCHNUM",
    t2."P2PARP1WEIGHT",
    t2."P2PARP2MAXPDCHNUM",
    t2."P2PARP2WEIGHT",
    t2."P2PARP3MAXPDCHNUM",
    t2."P2PARP3WEIGHT",
    t2."P2PDLTBFRELDELAY",
    t2."P2POPT",
    t2."P2PPDCHMULTIPLEXWEIGHT",
    t2."SERVTYPERTUPDATESW",
    t2."STREAMINGARP1MAXPDCHNUM",
    t2."STREAMINGARP1WEIGHT",
    t2."STREAMINGARP2MAXPDCHNUM",
    t2."STREAMINGARP2WEIGHT",
    t2."STREAMINGARP3MAXPDCHNUM",
    t2."STREAMINGARP3WEIGHT",
    t2."STREAMINGDLTBFRELDELAY",
    t2."STREAMINGOPT",
    t2."STREAMPDCHMULTIPLEXWEIGHT",
    t2."WEBARP1MAXPDCHNUM",
    t2."WEBARP1WEIGHT",
    t2."WEBARP2MAXPDCHNUM",
    t2."WEBARP2WEIGHT",
    t2."WEBARP3MAXPDCHNUM",
    t2."WEBARP3WEIGHT",
    t2."WEBDLTBFRELDELAY",
    t2."WEBOPT",
    t2."WEBPDCHMULTIPLEXWEIGHT"
FROM
huawei_gexport_gsm."GCELLPSDIFFSERVICE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."EMAILARP1MAXPDCHNUM",
    t3."EMAILARP1WEIGHT",
    t3."EMAILARP2MAXPDCHNUM",
    t3."EMAILARP2WEIGHT",
    t3."EMAILARP3MAXPDCHNUM",
    t3."EMAILARP3WEIGHT",
    t3."EMAILDLTBFRELDELAY",
    t3."EMAILOPT",
    t3."EMAILPDCHMULTIPLEXWEIGHT",
    t3."IMARP1MAXPDCHNUM",
    t3."IMARP1WEIGHT",
    t3."IMARP2MAXPDCHNUM",
    t3."IMARP2WEIGHT",
    t3."IMARP3MAXPDCHNUM",
    t3."IMARP3WEIGHT",
    t3."IMDLTBFRELDELAY",
    t3."IMOPT",
    t3."IMPDCHMULTIPLEXWEIGHT",
    t3."P2PARP1MAXPDCHNUM",
    t3."P2PARP1WEIGHT",
    t3."P2PARP2MAXPDCHNUM",
    t3."P2PARP2WEIGHT",
    t3."P2PARP3MAXPDCHNUM",
    t3."P2PARP3WEIGHT",
    t3."P2PDLTBFRELDELAY",
    t3."P2POPT",
    t3."P2PPDCHMULTIPLEXWEIGHT",
    t3."SERVTYPERTUPDATESW",
    t3."STREAMINGARP1MAXPDCHNUM",
    t3."STREAMINGARP1WEIGHT",
    t3."STREAMINGARP2MAXPDCHNUM",
    t3."STREAMINGARP2WEIGHT",
    t3."STREAMINGARP3MAXPDCHNUM",
    t3."STREAMINGARP3WEIGHT",
    t3."STREAMINGDLTBFRELDELAY",
    t3."STREAMINGOPT",
    t3."STREAMPDCHMULTIPLEXWEIGHT",
    t3."WEBARP1MAXPDCHNUM",
    t3."WEBARP1WEIGHT",
    t3."WEBARP2MAXPDCHNUM",
    t3."WEBARP2WEIGHT",
    t3."WEBARP3MAXPDCHNUM",
    t3."WEBARP3WEIGHT",
    t3."WEBDLTBFRELDELAY",
    t3."WEBOPT",
    t3."WEBPDCHMULTIPLEXWEIGHT"
FROM
huawei_gexport_gsm."GCELLPSDIFFSERVICE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."EMAILARP1MAXPDCHNUM",
    t4."EMAILARP1WEIGHT",
    t4."EMAILARP2MAXPDCHNUM",
    t4."EMAILARP2WEIGHT",
    t4."EMAILARP3MAXPDCHNUM",
    t4."EMAILARP3WEIGHT",
    t4."EMAILDLTBFRELDELAY",
    t4."EMAILOPT",
    t4."EMAILPDCHMULTIPLEXWEIGHT",
    t4."IMARP1MAXPDCHNUM",
    t4."IMARP1WEIGHT",
    t4."IMARP2MAXPDCHNUM",
    t4."IMARP2WEIGHT",
    t4."IMARP3MAXPDCHNUM",
    t4."IMARP3WEIGHT",
    t4."IMDLTBFRELDELAY",
    t4."IMOPT",
    t4."IMPDCHMULTIPLEXWEIGHT",
    t4."P2PARP1MAXPDCHNUM",
    t4."P2PARP1WEIGHT",
    t4."P2PARP2MAXPDCHNUM",
    t4."P2PARP2WEIGHT",
    t4."P2PARP3MAXPDCHNUM",
    t4."P2PARP3WEIGHT",
    t4."P2PDLTBFRELDELAY",
    t4."P2POPT",
    t4."P2PPDCHMULTIPLEXWEIGHT",
    t4."SERVTYPERTUPDATESW",
    t4."STREAMINGARP1MAXPDCHNUM",
    t4."STREAMINGARP1WEIGHT",
    t4."STREAMINGARP2MAXPDCHNUM",
    t4."STREAMINGARP2WEIGHT",
    t4."STREAMINGARP3MAXPDCHNUM",
    t4."STREAMINGARP3WEIGHT",
    t4."STREAMINGDLTBFRELDELAY",
    t4."STREAMINGOPT",
    t4."STREAMPDCHMULTIPLEXWEIGHT",
    t4."WEBARP1MAXPDCHNUM",
    t4."WEBARP1WEIGHT",
    t4."WEBARP2MAXPDCHNUM",
    t4."WEBARP2WEIGHT",
    t4."WEBARP3MAXPDCHNUM",
    t4."WEBARP3WEIGHT",
    t4."WEBDLTBFRELDELAY",
    t4."WEBOPT",
    t4."WEBPDCHMULTIPLEXWEIGHT"
FROM
huawei_mml_gsm."GCELLPSDIFFSERVICE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSI1 = ReplaceableObject(
    'huawei_cm_2g."GCELLPSI1"',
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
    t1."MEASORDER",
    t1."PSI1RPT",
    t1."PSISTATUSIND"
FROM
huawei_nbi_gsm."GCELLPSI1" t1

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
    t2."MEASORDER",
    t2."PSI1RPT",
    t2."PSISTATUSIND"
FROM
huawei_gexport_gsm."GCELLPSI1_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."MEASORDER",
    t3."PSI1RPT",
    t3."PSISTATUSIND"
FROM
huawei_gexport_gsm."GCELLPSI1_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."MEASORDER",
    t4."PSI1RPT",
    t4."PSISTATUSIND"
FROM
huawei_mml_gsm."GCELLPSI1" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSOTHERPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPSOTHERPARA"',
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
    t1."ABISIPDUMMYOPTSUP",
    t1."ACCSTASERVICETYPE",
    t1."CELLID",
    t1."DLGPRSINFOWAITSENDTIMELEN",
    t1."DLGPRSTBFEXPANDOP",
    t1."DLMINGUARANTEERATE",
    t1."DLPACKSENDPERIOD",
    t1."DUMMYPDULIFETIME",
    t1."EGPRSPRIWEIGHT",
    t1."ENGSMPSDLMACFLOWCTRL",
    t1."ENSUREPDCHRESORNOT",
    t1."EXTCELLTHRENH",
    t1."G3GNCELLFILTERMODE",
    t1."GBRQOS",
    t1."GMSKULSCHEDULEOPTSW",
    t1."GPRSCHOOSECSPOLICY",
    t1."GPRSPDCHSYNMODE",
    t1."GPSRRECORDFLTSW",
    t1."GSMTOTDALLOWED",
    t1."IMMASSDLSHIFT",
    t1."LINKADJACKCHECKSW",
    t1."LINKADJRESENDINTERVAL",
    t1."LLCDLRATESTATOPTSW",
    t1."LLCPDUREORDER",
    t1."LONGHOPFREQNUMLOWLMTSW",
    t1."MACSCHEDULETYPE",
    t1."MINTIMEDIFF",
    t1."MOCNWAITSGSNRSPTIMERLEN",
    t1."N3103STATMODE",
    t1."OCCUPYSTREAMINGSWITCH",
    t1."PACKASSDLSHIFT",
    t1."PDCHASYNNOTIFYBTSSW",
    t1."PFCSWITCH",
    t1."PKTIMMASSHOPCHANPLY",
    t1."POCDELAY",
    t1."POCGBRMAX",
    t1."POCGBRMIN",
    t1."POCSUP",
    t1."PSDIFSERVICESUP",
    t1."QOSOPT",
    t1."RATEFILTERTIMEWIN",
    t1."RDMFILLBYTESSUP",
    t1."REQREFFRAMENOFIXEDSW",
    t1."SINGLEBLKASSSTARTTIMEDLYSW",
    t1."SUSPENDDLTBFRELSTATSW",
    t1."USERPLANEDLFCPDCHBW",
    t1."USERPLANEDLFCPERIOD",
    t1."USERPLANEDLFCSTEP"
FROM
huawei_nbi_gsm."GCELLPSOTHERPARA" t1

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
    t2."ABISIPDUMMYOPTSUP",
    t2."ACCSTASERVICETYPE",
    t2."CELLID",
    t2."DLGPRSINFOWAITSENDTIMELEN",
    t2."DLGPRSTBFEXPANDOP",
    t2."DLMINGUARANTEERATE",
    t2."DLPACKSENDPERIOD",
    t2."DUMMYPDULIFETIME",
    t2."EGPRSPRIWEIGHT",
    t2."ENGSMPSDLMACFLOWCTRL",
    t2."ENSUREPDCHRESORNOT",
    t2."EXTCELLTHRENH",
    t2."G3GNCELLFILTERMODE",
    t2."GBRQOS",
    t2."GMSKULSCHEDULEOPTSW",
    t2."GPRSCHOOSECSPOLICY",
    t2."GPRSPDCHSYNMODE",
    t2."GPSRRECORDFLTSW",
    t2."GSMTOTDALLOWED",
    t2."IMMASSDLSHIFT",
    t2."LINKADJACKCHECKSW",
    t2."LINKADJRESENDINTERVAL",
    t2."LLCDLRATESTATOPTSW",
    t2."LLCPDUREORDER",
    t2."LONGHOPFREQNUMLOWLMTSW",
    t2."MACSCHEDULETYPE",
    t2."MINTIMEDIFF",
    t2."MOCNWAITSGSNRSPTIMERLEN",
    t2."N3103STATMODE",
    t2."OCCUPYSTREAMINGSWITCH",
    t2."PACKASSDLSHIFT",
    t2."PDCHASYNNOTIFYBTSSW",
    t2."PFCSWITCH",
    t2."PKTIMMASSHOPCHANPLY",
    t2."POCDELAY",
    t2."POCGBRMAX",
    t2."POCGBRMIN",
    t2."POCSUP",
    t2."PSDIFSERVICESUP",
    t2."QOSOPT",
    t2."RATEFILTERTIMEWIN",
    t2."RDMFILLBYTESSUP",
    t2."REQREFFRAMENOFIXEDSW",
    t2."SINGLEBLKASSSTARTTIMEDLYSW",
    t2."SUSPENDDLTBFRELSTATSW",
    t2."USERPLANEDLFCPDCHBW",
    t2."USERPLANEDLFCPERIOD",
    t2."USERPLANEDLFCSTEP"
FROM
huawei_gexport_gsm."GCELLPSOTHERPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISIPDUMMYOPTSUP",
    t3."ACCSTASERVICETYPE",
    t3."CELLID",
    t3."DLGPRSINFOWAITSENDTIMELEN",
    t3."DLGPRSTBFEXPANDOP",
    t3."DLMINGUARANTEERATE",
    t3."DLPACKSENDPERIOD",
    t3."DUMMYPDULIFETIME",
    t3."EGPRSPRIWEIGHT",
    t3."ENGSMPSDLMACFLOWCTRL",
    t3."ENSUREPDCHRESORNOT",
    t3."EXTCELLTHRENH",
    t3."G3GNCELLFILTERMODE",
    t3."GBRQOS",
    t3."GMSKULSCHEDULEOPTSW",
    t3."GPRSCHOOSECSPOLICY",
    t3."GPRSPDCHSYNMODE",
    t3."GPSRRECORDFLTSW",
    t3."GSMTOTDALLOWED",
    t3."IMMASSDLSHIFT",
    t3."LINKADJACKCHECKSW",
    t3."LINKADJRESENDINTERVAL",
    t3."LLCDLRATESTATOPTSW",
    t3."LLCPDUREORDER",
    t3."LONGHOPFREQNUMLOWLMTSW",
    t3."MACSCHEDULETYPE",
    t3."MINTIMEDIFF",
    t3."MOCNWAITSGSNRSPTIMERLEN",
    t3."N3103STATMODE",
    t3."OCCUPYSTREAMINGSWITCH",
    t3."PACKASSDLSHIFT",
    t3."PDCHASYNNOTIFYBTSSW",
    t3."PFCSWITCH",
    t3."PKTIMMASSHOPCHANPLY",
    t3."POCDELAY",
    t3."POCGBRMAX",
    t3."POCGBRMIN",
    t3."POCSUP",
    t3."PSDIFSERVICESUP",
    t3."QOSOPT",
    t3."RATEFILTERTIMEWIN",
    t3."RDMFILLBYTESSUP",
    t3."REQREFFRAMENOFIXEDSW",
    t3."SINGLEBLKASSSTARTTIMEDLYSW",
    t3."SUSPENDDLTBFRELSTATSW",
    t3."USERPLANEDLFCPDCHBW",
    t3."USERPLANEDLFCPERIOD",
    t3."USERPLANEDLFCSTEP"
FROM
huawei_gexport_gsm."GCELLPSOTHERPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISIPDUMMYOPTSUP",
    t4."ACCSTASERVICETYPE",
    t4."CELLID",
    t4."DLGPRSINFOWAITSENDTIMELEN",
    t4."DLGPRSTBFEXPANDOP",
    t4."DLMINGUARANTEERATE",
    t4."DLPACKSENDPERIOD",
    t4."DUMMYPDULIFETIME",
    t4."EGPRSPRIWEIGHT",
    t4."ENGSMPSDLMACFLOWCTRL",
    t4."ENSUREPDCHRESORNOT",
    t4."EXTCELLTHRENH",
    t4."G3GNCELLFILTERMODE",
    t4."GBRQOS",
    t4."GMSKULSCHEDULEOPTSW",
    t4."GPRSCHOOSECSPOLICY",
    t4."GPRSPDCHSYNMODE",
    t4."GPSRRECORDFLTSW",
    t4."GSMTOTDALLOWED",
    t4."IMMASSDLSHIFT",
    t4."LINKADJACKCHECKSW",
    t4."LINKADJRESENDINTERVAL",
    t4."LLCDLRATESTATOPTSW",
    t4."LLCPDUREORDER",
    t4."LONGHOPFREQNUMLOWLMTSW",
    t4."MACSCHEDULETYPE",
    t4."MINTIMEDIFF",
    t4."MOCNWAITSGSNRSPTIMERLEN",
    t4."N3103STATMODE",
    t4."OCCUPYSTREAMINGSWITCH",
    t4."PACKASSDLSHIFT",
    t4."PDCHASYNNOTIFYBTSSW",
    t4."PFCSWITCH",
    t4."PKTIMMASSHOPCHANPLY",
    t4."POCDELAY",
    t4."POCGBRMAX",
    t4."POCGBRMIN",
    t4."POCSUP",
    t4."PSDIFSERVICESUP",
    t4."QOSOPT",
    t4."RATEFILTERTIMEWIN",
    t4."RDMFILLBYTESSUP",
    t4."REQREFFRAMENOFIXEDSW",
    t4."SINGLEBLKASSSTARTTIMEDLYSW",
    t4."SUSPENDDLTBFRELSTATSW",
    t4."USERPLANEDLFCPDCHBW",
    t4."USERPLANEDLFCPERIOD",
    t4."USERPLANEDLFCSTEP"
FROM
huawei_mml_gsm."GCELLPSOTHERPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSPWPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLPSPWPARA"',
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
    t1."ALPHA",
    t1."CELLID",
    t1."DLPCINITPR",
    t1."DLPCSTARTTHR",
    t1."DUMMYPRGRAN",
    t1."EGPRSDLMRFLTGENE",
    t1."EGPRSINITATTTARGETLEVEL",
    t1."EGPRSSIGINITATTOFFSET",
    t1."EGPRSSIGPOWEROFFSET",
    t1."EGPRSULPCTARGETTHR",
    t1."GAMMA",
    t1."GPRSDLMRFLTGENE",
    t1."GPRSDLPCRELADJGENE",
    t1."GPRSDLPCRELTHR",
    t1."GPRSDLPCSTARTTHR",
    t1."GPRSINITATTTARGETLEVEL",
    t1."GPRSSIGINITATTOFFSET",
    t1."GPRSSIGPOWEROFFSET",
    t1."MAXPCSTEP",
    t1."MCSSTABTHR",
    t1."MCSSTATTHR",
    t1."NAVGI",
    t1."PB",
    t1."PCMEASCHAN",
    t1."PSPCPOLICY",
    t1."PSPCPRES",
    t1."SUPEGPRSDLPCMROPT",
    t1."SUPEGPRSULPC",
    t1."SUPGPRSDLPC",
    t1."SUPPSDLPC",
    t1."TAVGT",
    t1."TAVGW",
    t1."TGTCIROFFSET",
    t1."TGTCIRPOS",
    t1."USFDUMMYPCFACTOR"
FROM
huawei_nbi_gsm."GCELLPSPWPARA" t1

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
    t2."ALPHA",
    t2."CELLID",
    t2."DLPCINITPR",
    t2."DLPCSTARTTHR",
    t2."DUMMYPRGRAN",
    t2."EGPRSDLMRFLTGENE",
    t2."EGPRSINITATTTARGETLEVEL",
    t2."EGPRSSIGINITATTOFFSET",
    t2."EGPRSSIGPOWEROFFSET",
    t2."EGPRSULPCTARGETTHR",
    t2."GAMMA",
    t2."GPRSDLMRFLTGENE",
    t2."GPRSDLPCRELADJGENE",
    t2."GPRSDLPCRELTHR",
    t2."GPRSDLPCSTARTTHR",
    t2."GPRSINITATTTARGETLEVEL",
    t2."GPRSSIGINITATTOFFSET",
    t2."GPRSSIGPOWEROFFSET",
    t2."MAXPCSTEP",
    t2."MCSSTABTHR",
    t2."MCSSTATTHR",
    t2."NAVGI",
    t2."PB",
    t2."PCMEASCHAN",
    t2."PSPCPOLICY",
    t2."PSPCPRES",
    t2."SUPEGPRSDLPCMROPT",
    t2."SUPEGPRSULPC",
    t2."SUPGPRSDLPC",
    t2."SUPPSDLPC",
    t2."TAVGT",
    t2."TAVGW",
    t2."TGTCIROFFSET",
    t2."TGTCIRPOS",
    t2."USFDUMMYPCFACTOR"
FROM
huawei_gexport_gsm."GCELLPSPWPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALPHA",
    t3."CELLID",
    t3."DLPCINITPR",
    t3."DLPCSTARTTHR",
    t3."DUMMYPRGRAN",
    t3."EGPRSDLMRFLTGENE",
    t3."EGPRSINITATTTARGETLEVEL",
    t3."EGPRSSIGINITATTOFFSET",
    t3."EGPRSSIGPOWEROFFSET",
    t3."EGPRSULPCTARGETTHR",
    t3."GAMMA",
    t3."GPRSDLMRFLTGENE",
    t3."GPRSDLPCRELADJGENE",
    t3."GPRSDLPCRELTHR",
    t3."GPRSDLPCSTARTTHR",
    t3."GPRSINITATTTARGETLEVEL",
    t3."GPRSSIGINITATTOFFSET",
    t3."GPRSSIGPOWEROFFSET",
    t3."MAXPCSTEP",
    t3."MCSSTABTHR",
    t3."MCSSTATTHR",
    t3."NAVGI",
    t3."PB",
    t3."PCMEASCHAN",
    t3."PSPCPOLICY",
    t3."PSPCPRES",
    t3."SUPEGPRSDLPCMROPT",
    t3."SUPEGPRSULPC",
    t3."SUPGPRSDLPC",
    t3."SUPPSDLPC",
    t3."TAVGT",
    t3."TAVGW",
    t3."TGTCIROFFSET",
    t3."TGTCIRPOS",
    t3."USFDUMMYPCFACTOR"
FROM
huawei_gexport_gsm."GCELLPSPWPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALPHA",
    t4."CELLID",
    t4."DLPCINITPR",
    NULL,
    t4."DUMMYPRGRAN",
    NULL,
    t4."EGPRSINITATTTARGETLEVEL",
    t4."EGPRSSIGINITATTOFFSET",
    t4."EGPRSSIGPOWEROFFSET",
    t4."EGPRSULPCTARGETTHR",
    t4."GAMMA",
    NULL,
    NULL,
    NULL,
    NULL,
    t4."GPRSINITATTTARGETLEVEL",
    t4."GPRSSIGINITATTOFFSET",
    t4."GPRSSIGPOWEROFFSET",
    t4."MAXPCSTEP",
    t4."MCSSTABTHR",
    t4."MCSSTATTHR",
    t4."NAVGI",
    t4."PB",
    t4."PCMEASCHAN",
    t4."PSPCPOLICY",
    t4."PSPCPRES",
    NULL,
    t4."SUPEGPRSULPC",
    t4."SUPGPRSDLPC",
    t4."SUPPSDLPC",
    t4."TAVGT",
    t4."TAVGW",
    NULL,
    NULL,
    t4."USFDUMMYPCFACTOR"
FROM
huawei_mml_gsm."GCELLPSPWPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPSSMALLPKTRESBAL = ReplaceableObject(
    'huawei_cm_2g."GCELLPSSMALLPKTRESBAL"',
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
    t1."PSSMALLPKTRESBALSWITCH"
FROM
huawei_nbi_gsm."GCELLPSSMALLPKTRESBAL" t1

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
    t2."PSSMALLPKTRESBALSWITCH"
FROM
huawei_gexport_gsm."GCELLPSSMALLPKTRESBAL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PSSMALLPKTRESBALSWITCH"
FROM
huawei_gexport_gsm."GCELLPSSMALLPKTRESBAL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PSSMALLPKTRESBALSWITCH"
FROM
huawei_mml_gsm."GCELLPSSMALLPKTRESBAL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPWR2 = ReplaceableObject(
    'huawei_cm_2g."GCELLPWR2"',
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
    t1."AMRBTSPWRNUM",
    t1."AMRDLLEVFTLEN",
    t1."AMRDLPREDLEND",
    t1."AMRDLQHTHRED",
    t1."AMRDLQLTHRED",
    t1."AMRDLQUAFTLEN",
    t1."AMRDLQUALBADTRIG",
    t1."AMRDLQUALBADUPLEV",
    t1."AMRDLSSHTHRED",
    t1."AMRDLSSLTHRED",
    t1."AMRMAXADJPCVAL",
    t1."AMRMAXSTEP0",
    t1."AMRMAXSTEP1",
    t1."AMRMAXSTEP2",
    t1."AMRMAXVALADJRX",
    t1."AMRMRCOMPREG",
    t1."AMRPCADJPERIOD",
    t1."AMRQUALSTEP",
    t1."AMRULLEVFTLEN",
    t1."AMRULPREDLEND",
    t1."AMRULQHTHRED",
    t1."AMRULQLOWTHRED",
    t1."AMRULQUAFTLEN",
    t1."AMRULQUALBADTRIG",
    t1."AMRULQUALBADUPLEV",
    t1."AMRULSSHTHRED",
    t1."AMRULSSLTHRED",
    t1."BTSPWRNUM",
    t1."CELLID",
    t1."DLLEVFILTLEN",
    t1."DLPREDLEND",
    t1."DLQUAFILTLEN",
    t1."DLQUALBADTRIG",
    t1."DLQUALBADUPLEV",
    t1."MAXADJPCVAL",
    t1."MAXSTEP0",
    t1."MAXSTEP1",
    t1."MAXSTEP2",
    t1."MAXVALADJRX",
    t1."MRCOMPREG",
    t1."QUALSTEP",
    t1."SAICTHREDAPDTVALUE",
    t1."ULLEVFILTLEN",
    t1."ULPREDLEND",
    t1."ULQUAFILTLEN",
    t1."ULQUALBADTRIG",
    t1."ULQUALBADUPLEV"
FROM
huawei_nbi_gsm."GCELLPWR2" t1

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
    t2."AMRBTSPWRNUM",
    t2."AMRDLLEVFTLEN",
    t2."AMRDLPREDLEND",
    t2."AMRDLQHTHRED",
    t2."AMRDLQLTHRED",
    t2."AMRDLQUAFTLEN",
    t2."AMRDLQUALBADTRIG",
    t2."AMRDLQUALBADUPLEV",
    t2."AMRDLSSHTHRED",
    t2."AMRDLSSLTHRED",
    t2."AMRMAXADJPCVAL",
    t2."AMRMAXSTEP0",
    t2."AMRMAXSTEP1",
    t2."AMRMAXSTEP2",
    t2."AMRMAXVALADJRX",
    t2."AMRMRCOMPREG",
    t2."AMRPCADJPERIOD",
    t2."AMRQUALSTEP",
    t2."AMRULLEVFTLEN",
    t2."AMRULPREDLEND",
    t2."AMRULQHTHRED",
    t2."AMRULQLOWTHRED",
    t2."AMRULQUAFTLEN",
    t2."AMRULQUALBADTRIG",
    t2."AMRULQUALBADUPLEV",
    t2."AMRULSSHTHRED",
    t2."AMRULSSLTHRED",
    t2."BTSPWRNUM",
    t2."CELLID",
    t2."DLLEVFILTLEN",
    t2."DLPREDLEND",
    t2."DLQUAFILTLEN",
    t2."DLQUALBADTRIG",
    t2."DLQUALBADUPLEV",
    t2."MAXADJPCVAL",
    t2."MAXSTEP0",
    t2."MAXSTEP1",
    t2."MAXSTEP2",
    t2."MAXVALADJRX",
    t2."MRCOMPREG",
    t2."QUALSTEP",
    t2."SAICTHREDAPDTVALUE",
    t2."ULLEVFILTLEN",
    t2."ULPREDLEND",
    t2."ULQUAFILTLEN",
    t2."ULQUALBADTRIG",
    t2."ULQUALBADUPLEV"
FROM
huawei_gexport_gsm."GCELLPWR2_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AMRBTSPWRNUM",
    t3."AMRDLLEVFTLEN",
    t3."AMRDLPREDLEND",
    t3."AMRDLQHTHRED",
    t3."AMRDLQLTHRED",
    t3."AMRDLQUAFTLEN",
    t3."AMRDLQUALBADTRIG",
    t3."AMRDLQUALBADUPLEV",
    t3."AMRDLSSHTHRED",
    t3."AMRDLSSLTHRED",
    t3."AMRMAXADJPCVAL",
    t3."AMRMAXSTEP0",
    t3."AMRMAXSTEP1",
    t3."AMRMAXSTEP2",
    t3."AMRMAXVALADJRX",
    t3."AMRMRCOMPREG",
    t3."AMRPCADJPERIOD",
    t3."AMRQUALSTEP",
    t3."AMRULLEVFTLEN",
    t3."AMRULPREDLEND",
    t3."AMRULQHTHRED",
    t3."AMRULQLOWTHRED",
    t3."AMRULQUAFTLEN",
    t3."AMRULQUALBADTRIG",
    t3."AMRULQUALBADUPLEV",
    t3."AMRULSSHTHRED",
    t3."AMRULSSLTHRED",
    t3."BTSPWRNUM",
    t3."CELLID",
    t3."DLLEVFILTLEN",
    t3."DLPREDLEND",
    t3."DLQUAFILTLEN",
    t3."DLQUALBADTRIG",
    t3."DLQUALBADUPLEV",
    t3."MAXADJPCVAL",
    t3."MAXSTEP0",
    t3."MAXSTEP1",
    t3."MAXSTEP2",
    t3."MAXVALADJRX",
    t3."MRCOMPREG",
    t3."QUALSTEP",
    t3."SAICTHREDAPDTVALUE",
    t3."ULLEVFILTLEN",
    t3."ULPREDLEND",
    t3."ULQUAFILTLEN",
    t3."ULQUALBADTRIG",
    t3."ULQUALBADUPLEV"
FROM
huawei_gexport_gsm."GCELLPWR2_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AMRBTSPWRNUM",
    t4."AMRDLLEVFTLEN",
    t4."AMRDLPREDLEND",
    t4."AMRDLQHTHRED",
    t4."AMRDLQLTHRED",
    t4."AMRDLQUAFTLEN",
    t4."AMRDLQUALBADTRIG",
    t4."AMRDLQUALBADUPLEV",
    t4."AMRDLSSHTHRED",
    t4."AMRDLSSLTHRED",
    t4."AMRMAXADJPCVAL",
    t4."AMRMAXSTEP0",
    t4."AMRMAXSTEP1",
    t4."AMRMAXSTEP2",
    t4."AMRMAXVALADJRX",
    t4."AMRMRCOMPREG",
    t4."AMRPCADJPERIOD",
    t4."AMRQUALSTEP",
    t4."AMRULLEVFTLEN",
    t4."AMRULPREDLEND",
    t4."AMRULQHTHRED",
    t4."AMRULQLOWTHRED",
    t4."AMRULQUAFTLEN",
    t4."AMRULQUALBADTRIG",
    t4."AMRULQUALBADUPLEV",
    t4."AMRULSSHTHRED",
    t4."AMRULSSLTHRED",
    t4."BTSPWRNUM",
    t4."CELLID",
    t4."DLLEVFILTLEN",
    t4."DLPREDLEND",
    t4."DLQUAFILTLEN",
    t4."DLQUALBADTRIG",
    t4."DLQUALBADUPLEV",
    t4."MAXADJPCVAL",
    t4."MAXSTEP0",
    t4."MAXSTEP1",
    t4."MAXSTEP2",
    t4."MAXVALADJRX",
    t4."MRCOMPREG",
    t4."QUALSTEP",
    t4."SAICTHREDAPDTVALUE",
    t4."ULLEVFILTLEN",
    t4."ULPREDLEND",
    t4."ULQUAFILTLEN",
    t4."ULQUALBADTRIG",
    t4."ULQUALBADUPLEV"
FROM
huawei_mml_gsm."GCELLPWR2" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPWR3 = ReplaceableObject(
    'huawei_cm_2g."GCELLPWR3"',
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
    t1."AMRCALLPCALLOWED",
    t1."CELLID",
    t1."CIRUPDATESWITCH",
    t1."DLADJPRD",
    t1."DLAFSREXQUALHIGHTHRED",
    t1."DLAFSREXQUALLOWTHRED",
    t1."DLAHSREXQUALHIGHTHRED",
    t1."DLAHSREXQUALLOWTHRED",
    t1."DLFILTADJFACTOR",
    t1."DLFSREXQUALHIGHTHRED",
    t1."DLFSREXQUALLOWTHRED",
    t1."DLHSREXQUALHIGHTHRED",
    t1."DLHSREXQUALLOWTHRED",
    t1."DLMAXDOWNOPTISW",
    t1."DLMAXDOWNSTEP",
    t1."DLMAXUPSTEP",
    t1."DLPCSTEPOPTSWITCH",
    t1."DLREXLEVADJFCTR",
    t1."DLREXLEVEXPFLTLEN",
    t1."DLREXLEVHIGHTHRED",
    t1."DLREXLEVLOWTHRED",
    t1."DLREXLEVSLDWINDOW",
    t1."DLREXQUALADJFCTR",
    t1."DLREXQUALEXPFLTLEN",
    t1."DLREXQUALSLDWINDOW",
    t1."DLRXLEVPROTECTFACTOR",
    t1."DLRXQUALPROTECTFACTOR",
    t1."FINESTEPPCALLOWED",
    t1."MAXBTSPWRNUM",
    t1."MRMISSNUM",
    t1."NONAMRCALLPCALLOWED",
    t1."OLDLREXLEVTHREDOFF",
    t1."OLDLREXQUALTHREDOFF",
    t1."OLDLRXLEVPROTECTOFF",
    t1."OLDLRXQUALPROTECTOFF",
    t1."OLULREXLEVTHREDOFF",
    t1."OLULREXQUALTHREDOFF",
    t1."OLULRXLEVPROTECTOFF",
    t1."OLULRXQUALPROTECTOFF",
    t1."PCSTEPOPT",
    t1."PWRCTRLOPTIMIZEDEN",
    t1."PWRFINECTLOPTIMIZESWITCH",
    t1."SAICTHREDAPDTVALUE",
    t1."SDMRCUTNUM",
    t1."TCHMRCUTNUM",
    t1."ULADJPRD",
    t1."ULAFSREXQUALHIGHTHRED",
    t1."ULAFSREXQUALLOWTHRED",
    t1."ULAHSREXQUALHIGHTHRED",
    t1."ULAHSREXQUALLOWTHRED",
    t1."ULFILTADJFACTOR",
    t1."ULFSREXQUALHIGHTHRED",
    t1."ULFSREXQUALLOWTHRED",
    t1."ULHSREXQUALHIGHTHRED",
    t1."ULHSREXQUALLOWTHRED",
    t1."ULMAXDOWNSTEP",
    t1."ULMAXUPSTEP",
    t1."ULREXLEVADJFCTR",
    t1."ULREXLEVEXPFLTLEN",
    t1."ULREXLEVHIGHTHRED",
    t1."ULREXLEVLOWTHRED",
    t1."ULREXLEVSLDWINDOW",
    t1."ULREXQUALADJFCTR",
    t1."ULREXQUALEXPFLTLEN",
    t1."ULREXQUALSLDWINDOW",
    t1."ULRXLEVPROTECTFACTOR",
    t1."ULRXQUALPROTECTFACTOR"
FROM
huawei_nbi_gsm."GCELLPWR3" t1

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
    t2."AMRCALLPCALLOWED",
    t2."CELLID",
    t2."CIRUPDATESWITCH",
    t2."DLADJPRD",
    t2."DLAFSREXQUALHIGHTHRED",
    t2."DLAFSREXQUALLOWTHRED",
    t2."DLAHSREXQUALHIGHTHRED",
    t2."DLAHSREXQUALLOWTHRED",
    t2."DLFILTADJFACTOR",
    t2."DLFSREXQUALHIGHTHRED",
    t2."DLFSREXQUALLOWTHRED",
    t2."DLHSREXQUALHIGHTHRED",
    t2."DLHSREXQUALLOWTHRED",
    t2."DLMAXDOWNOPTISW",
    t2."DLMAXDOWNSTEP",
    t2."DLMAXUPSTEP",
    t2."DLPCSTEPOPTSWITCH",
    t2."DLREXLEVADJFCTR",
    t2."DLREXLEVEXPFLTLEN",
    t2."DLREXLEVHIGHTHRED",
    t2."DLREXLEVLOWTHRED",
    t2."DLREXLEVSLDWINDOW",
    t2."DLREXQUALADJFCTR",
    t2."DLREXQUALEXPFLTLEN",
    t2."DLREXQUALSLDWINDOW",
    t2."DLRXLEVPROTECTFACTOR",
    t2."DLRXQUALPROTECTFACTOR",
    t2."FINESTEPPCALLOWED",
    t2."MAXBTSPWRNUM",
    t2."MRMISSNUM",
    t2."NONAMRCALLPCALLOWED",
    t2."OLDLREXLEVTHREDOFF",
    t2."OLDLREXQUALTHREDOFF",
    t2."OLDLRXLEVPROTECTOFF",
    t2."OLDLRXQUALPROTECTOFF",
    t2."OLULREXLEVTHREDOFF",
    t2."OLULREXQUALTHREDOFF",
    t2."OLULRXLEVPROTECTOFF",
    t2."OLULRXQUALPROTECTOFF",
    t2."PCSTEPOPT",
    t2."PWRCTRLOPTIMIZEDEN",
    t2."PWRFINECTLOPTIMIZESWITCH",
    t2."SAICTHREDAPDTVALUE",
    t2."SDMRCUTNUM",
    t2."TCHMRCUTNUM",
    t2."ULADJPRD",
    t2."ULAFSREXQUALHIGHTHRED",
    t2."ULAFSREXQUALLOWTHRED",
    t2."ULAHSREXQUALHIGHTHRED",
    t2."ULAHSREXQUALLOWTHRED",
    t2."ULFILTADJFACTOR",
    t2."ULFSREXQUALHIGHTHRED",
    t2."ULFSREXQUALLOWTHRED",
    t2."ULHSREXQUALHIGHTHRED",
    t2."ULHSREXQUALLOWTHRED",
    t2."ULMAXDOWNSTEP",
    t2."ULMAXUPSTEP",
    t2."ULREXLEVADJFCTR",
    t2."ULREXLEVEXPFLTLEN",
    t2."ULREXLEVHIGHTHRED",
    t2."ULREXLEVLOWTHRED",
    t2."ULREXLEVSLDWINDOW",
    t2."ULREXQUALADJFCTR",
    t2."ULREXQUALEXPFLTLEN",
    t2."ULREXQUALSLDWINDOW",
    t2."ULRXLEVPROTECTFACTOR",
    t2."ULRXQUALPROTECTFACTOR"
FROM
huawei_gexport_gsm."GCELLPWR3_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AMRCALLPCALLOWED",
    t3."CELLID",
    t3."CIRUPDATESWITCH",
    t3."DLADJPRD",
    t3."DLAFSREXQUALHIGHTHRED",
    t3."DLAFSREXQUALLOWTHRED",
    t3."DLAHSREXQUALHIGHTHRED",
    t3."DLAHSREXQUALLOWTHRED",
    t3."DLFILTADJFACTOR",
    t3."DLFSREXQUALHIGHTHRED",
    t3."DLFSREXQUALLOWTHRED",
    t3."DLHSREXQUALHIGHTHRED",
    t3."DLHSREXQUALLOWTHRED",
    t3."DLMAXDOWNOPTISW",
    t3."DLMAXDOWNSTEP",
    t3."DLMAXUPSTEP",
    t3."DLPCSTEPOPTSWITCH",
    t3."DLREXLEVADJFCTR",
    t3."DLREXLEVEXPFLTLEN",
    t3."DLREXLEVHIGHTHRED",
    t3."DLREXLEVLOWTHRED",
    t3."DLREXLEVSLDWINDOW",
    t3."DLREXQUALADJFCTR",
    t3."DLREXQUALEXPFLTLEN",
    t3."DLREXQUALSLDWINDOW",
    t3."DLRXLEVPROTECTFACTOR",
    t3."DLRXQUALPROTECTFACTOR",
    t3."FINESTEPPCALLOWED",
    t3."MAXBTSPWRNUM",
    t3."MRMISSNUM",
    t3."NONAMRCALLPCALLOWED",
    t3."OLDLREXLEVTHREDOFF",
    t3."OLDLREXQUALTHREDOFF",
    t3."OLDLRXLEVPROTECTOFF",
    t3."OLDLRXQUALPROTECTOFF",
    t3."OLULREXLEVTHREDOFF",
    t3."OLULREXQUALTHREDOFF",
    t3."OLULRXLEVPROTECTOFF",
    t3."OLULRXQUALPROTECTOFF",
    t3."PCSTEPOPT",
    t3."PWRCTRLOPTIMIZEDEN",
    t3."PWRFINECTLOPTIMIZESWITCH",
    t3."SAICTHREDAPDTVALUE",
    t3."SDMRCUTNUM",
    t3."TCHMRCUTNUM",
    t3."ULADJPRD",
    t3."ULAFSREXQUALHIGHTHRED",
    t3."ULAFSREXQUALLOWTHRED",
    t3."ULAHSREXQUALHIGHTHRED",
    t3."ULAHSREXQUALLOWTHRED",
    t3."ULFILTADJFACTOR",
    t3."ULFSREXQUALHIGHTHRED",
    t3."ULFSREXQUALLOWTHRED",
    t3."ULHSREXQUALHIGHTHRED",
    t3."ULHSREXQUALLOWTHRED",
    t3."ULMAXDOWNSTEP",
    t3."ULMAXUPSTEP",
    t3."ULREXLEVADJFCTR",
    t3."ULREXLEVEXPFLTLEN",
    t3."ULREXLEVHIGHTHRED",
    t3."ULREXLEVLOWTHRED",
    t3."ULREXLEVSLDWINDOW",
    t3."ULREXQUALADJFCTR",
    t3."ULREXQUALEXPFLTLEN",
    t3."ULREXQUALSLDWINDOW",
    t3."ULRXLEVPROTECTFACTOR",
    t3."ULRXQUALPROTECTFACTOR"
FROM
huawei_gexport_gsm."GCELLPWR3_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AMRCALLPCALLOWED",
    t4."CELLID",
    t4."CIRUPDATESWITCH",
    t4."DLADJPRD",
    t4."DLAFSREXQUALHIGHTHRED",
    t4."DLAFSREXQUALLOWTHRED",
    t4."DLAHSREXQUALHIGHTHRED",
    t4."DLAHSREXQUALLOWTHRED",
    t4."DLFILTADJFACTOR",
    t4."DLFSREXQUALHIGHTHRED",
    t4."DLFSREXQUALLOWTHRED",
    t4."DLHSREXQUALHIGHTHRED",
    t4."DLHSREXQUALLOWTHRED",
    t4."DLMAXDOWNOPTISW",
    t4."DLMAXDOWNSTEP",
    t4."DLMAXUPSTEP",
    t4."DLPCSTEPOPTSWITCH",
    t4."DLREXLEVADJFCTR",
    t4."DLREXLEVEXPFLTLEN",
    t4."DLREXLEVHIGHTHRED",
    t4."DLREXLEVLOWTHRED",
    t4."DLREXLEVSLDWINDOW",
    t4."DLREXQUALADJFCTR",
    t4."DLREXQUALEXPFLTLEN",
    t4."DLREXQUALSLDWINDOW",
    t4."DLRXLEVPROTECTFACTOR",
    t4."DLRXQUALPROTECTFACTOR",
    t4."FINESTEPPCALLOWED",
    t4."MAXBTSPWRNUM",
    t4."MRMISSNUM",
    t4."NONAMRCALLPCALLOWED",
    t4."OLDLREXLEVTHREDOFF",
    t4."OLDLREXQUALTHREDOFF",
    t4."OLDLRXLEVPROTECTOFF",
    t4."OLDLRXQUALPROTECTOFF",
    t4."OLULREXLEVTHREDOFF",
    t4."OLULREXQUALTHREDOFF",
    t4."OLULRXLEVPROTECTOFF",
    t4."OLULRXQUALPROTECTOFF",
    t4."PCSTEPOPT",
    t4."PWRCTRLOPTIMIZEDEN",
    t4."PWRFINECTLOPTIMIZESWITCH",
    t4."SAICTHREDAPDTVALUE",
    t4."SDMRCUTNUM",
    t4."TCHMRCUTNUM",
    t4."ULADJPRD",
    t4."ULAFSREXQUALHIGHTHRED",
    t4."ULAFSREXQUALLOWTHRED",
    t4."ULAHSREXQUALHIGHTHRED",
    t4."ULAHSREXQUALLOWTHRED",
    t4."ULFILTADJFACTOR",
    t4."ULFSREXQUALHIGHTHRED",
    t4."ULFSREXQUALLOWTHRED",
    t4."ULHSREXQUALHIGHTHRED",
    t4."ULHSREXQUALLOWTHRED",
    t4."ULMAXDOWNSTEP",
    t4."ULMAXUPSTEP",
    t4."ULREXLEVADJFCTR",
    t4."ULREXLEVEXPFLTLEN",
    t4."ULREXLEVHIGHTHRED",
    t4."ULREXLEVLOWTHRED",
    t4."ULREXLEVSLDWINDOW",
    t4."ULREXQUALADJFCTR",
    t4."ULREXQUALEXPFLTLEN",
    t4."ULREXQUALSLDWINDOW",
    t4."ULRXLEVPROTECTFACTOR",
    t4."ULRXQUALPROTECTFACTOR"
FROM
huawei_mml_gsm."GCELLPWR3" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLPWRBASIC = ReplaceableObject(
    'huawei_cm_2g."GCELLPWRBASIC"',
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
    t1."AMRSADLUPGRADE",
    t1."BBFHPOWECTRLSWITCH",
    t1."CELLID",
    t1."COMBINERLOSS",
    t1."DLQHIGHTHRED",
    t1."DLQLOWTHRED",
    t1."DLSSHIGHTHRED",
    t1."DLSSLOWTHRED",
    t1."DOUBLEANTENNAGAIN",
    t1."EXPDLRXLEV",
    t1."EXPULRXLEV",
    t1."MSPOWERLEVELSWITCH",
    t1."PATHLOSS",
    t1."PCADJPERIOD",
    t1."POWERCTRLSTEPSWITCH",
    t1."PWRBCDALLOWD",
    t1."PWRBCDASSOFFSET",
    t1."PWRBCDHOOFFSET",
    t1."PWRBCDOPTIMIZESWITCH",
    t1."PWRBCDPROCOPTSW",
    t1."PWRCTLSAICOFFSETSWITCH",
    t1."PWRCTRLSW",
    t1."SAICALLOWED",
    t1."ULQHIGHTHRED",
    t1."ULQLOWTHRED",
    t1."ULSSHIGHTHRED",
    t1."ULSSLOWTHRED"
FROM
huawei_nbi_gsm."GCELLPWRBASIC" t1

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
    t2."AMRSADLUPGRADE",
    t2."BBFHPOWECTRLSWITCH",
    t2."CELLID",
    t2."COMBINERLOSS",
    t2."DLQHIGHTHRED",
    t2."DLQLOWTHRED",
    t2."DLSSHIGHTHRED",
    t2."DLSSLOWTHRED",
    t2."DOUBLEANTENNAGAIN",
    t2."EXPDLRXLEV",
    t2."EXPULRXLEV",
    t2."MSPOWERLEVELSWITCH",
    t2."PATHLOSS",
    t2."PCADJPERIOD",
    t2."POWERCTRLSTEPSWITCH",
    t2."PWRBCDALLOWD",
    t2."PWRBCDASSOFFSET",
    t2."PWRBCDHOOFFSET",
    t2."PWRBCDOPTIMIZESWITCH",
    t2."PWRBCDPROCOPTSW",
    t2."PWRCTLSAICOFFSETSWITCH",
    t2."PWRCTRLSW",
    t2."SAICALLOWED",
    t2."ULQHIGHTHRED",
    t2."ULQLOWTHRED",
    t2."ULSSHIGHTHRED",
    t2."ULSSLOWTHRED"
FROM
huawei_gexport_gsm."GCELLPWRBASIC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AMRSADLUPGRADE",
    t3."BBFHPOWECTRLSWITCH",
    t3."CELLID",
    t3."COMBINERLOSS",
    t3."DLQHIGHTHRED",
    t3."DLQLOWTHRED",
    t3."DLSSHIGHTHRED",
    t3."DLSSLOWTHRED",
    t3."DOUBLEANTENNAGAIN",
    t3."EXPDLRXLEV",
    t3."EXPULRXLEV",
    t3."MSPOWERLEVELSWITCH",
    t3."PATHLOSS",
    t3."PCADJPERIOD",
    t3."POWERCTRLSTEPSWITCH",
    t3."PWRBCDALLOWD",
    t3."PWRBCDASSOFFSET",
    t3."PWRBCDHOOFFSET",
    t3."PWRBCDOPTIMIZESWITCH",
    t3."PWRBCDPROCOPTSW",
    t3."PWRCTLSAICOFFSETSWITCH",
    t3."PWRCTRLSW",
    t3."SAICALLOWED",
    t3."ULQHIGHTHRED",
    t3."ULQLOWTHRED",
    t3."ULSSHIGHTHRED",
    t3."ULSSLOWTHRED"
FROM
huawei_gexport_gsm."GCELLPWRBASIC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AMRSADLUPGRADE",
    t4."BBFHPOWECTRLSWITCH",
    t4."CELLID",
    t4."COMBINERLOSS",
    t4."DLQHIGHTHRED",
    t4."DLQLOWTHRED",
    t4."DLSSHIGHTHRED",
    t4."DLSSLOWTHRED",
    t4."DOUBLEANTENNAGAIN",
    t4."EXPDLRXLEV",
    t4."EXPULRXLEV",
    t4."MSPOWERLEVELSWITCH",
    t4."PATHLOSS",
    t4."PCADJPERIOD",
    t4."POWERCTRLSTEPSWITCH",
    t4."PWRBCDALLOWD",
    t4."PWRBCDASSOFFSET",
    t4."PWRBCDHOOFFSET",
    t4."PWRBCDOPTIMIZESWITCH",
    t4."PWRBCDPROCOPTSW",
    t4."PWRCTLSAICOFFSETSWITCH",
    t4."PWRCTRLSW",
    t4."SAICALLOWED",
    t4."ULQHIGHTHRED",
    t4."ULQLOWTHRED",
    t4."ULSSHIGHTHRED",
    t4."ULSSLOWTHRED"
FROM
huawei_mml_gsm."GCELLPWRBASIC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLRESELECTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLRESELECTPARA"',
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
    t1."C31HYST",
    t1."C32QUAL",
    t1."CELLID",
    t1."GPRSCELLRESELECTHYESTERESIS",
    t1."RANDACCESSRETRY",
    t1."RARESELECTHYST",
    t1."TRESEL"
FROM
huawei_nbi_gsm."GCELLRESELECTPARA" t1

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
    t2."C31HYST",
    t2."C32QUAL",
    t2."CELLID",
    t2."GPRSCELLRESELECTHYESTERESIS",
    t2."RANDACCESSRETRY",
    t2."RARESELECTHYST",
    t2."TRESEL"
FROM
huawei_gexport_gsm."GCELLRESELECTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."C31HYST",
    t3."C32QUAL",
    t3."CELLID",
    t3."GPRSCELLRESELECTHYESTERESIS",
    t3."RANDACCESSRETRY",
    t3."RARESELECTHYST",
    t3."TRESEL"
FROM
huawei_gexport_gsm."GCELLRESELECTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."C31HYST",
    t4."C32QUAL",
    t4."CELLID",
    t4."GPRSCELLRESELECTHYESTERESIS",
    t4."RANDACCESSRETRY",
    t4."RARESELECTHYST",
    t4."TRESEL"
FROM
huawei_mml_gsm."GCELLRESELECTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLRESELECTUTRANTDD = ReplaceableObject(
    'huawei_cm_2g."GCELLRESELECTUTRANTDD"',
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
    t1."PSBESTTDDCELLNUM",
    t1."PSTDDCELLRPTOFF",
    t1."PSTDDCELLRPTTHD",
    t1."TDDNCELLLOADTHD",
    t1."TDDRESELTIMETHD"
FROM
huawei_nbi_gsm."GCELLRESELECTUTRANTDD" t1

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
    t2."PSBESTTDDCELLNUM",
    t2."PSTDDCELLRPTOFF",
    t2."PSTDDCELLRPTTHD",
    t2."TDDNCELLLOADTHD",
    t2."TDDRESELTIMETHD"
FROM
huawei_gexport_gsm."GCELLRESELECTUTRANTDD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PSBESTTDDCELLNUM",
    t3."PSTDDCELLRPTOFF",
    t3."PSTDDCELLRPTTHD",
    t3."TDDNCELLLOADTHD",
    t3."TDDRESELTIMETHD"
FROM
huawei_gexport_gsm."GCELLRESELECTUTRANTDD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PSBESTTDDCELLNUM",
    t4."PSTDDCELLRPTOFF",
    t4."PSTDDCELLRPTTHD",
    t4."TDDNCELLLOADTHD",
    t4."TDDRESELTIMETHD"
FROM
huawei_mml_gsm."GCELLRESELECTUTRANTDD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLRESELUTRANFDD = ReplaceableObject(
    'huawei_cm_2g."GCELLRESELUTRANFDD"',
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
    t1."FDDRESELTIMETHD",
    t1."GSMTOFDDFORCENC2",
    t1."PSBESTFDDCELLNUM",
    t1."PSFDDCELLRPTOFF",
    t1."PSFDDCELLRPTTHD",
    t1."PSFDDRPTTHR2ECNO",
    t1."PSFDDRPTTHR2RSCP",
    t1."SENDPMOWITHQPSW"
FROM
huawei_nbi_gsm."GCELLRESELUTRANFDD" t1

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
    t2."FDDRESELTIMETHD",
    t2."GSMTOFDDFORCENC2",
    t2."PSBESTFDDCELLNUM",
    t2."PSFDDCELLRPTOFF",
    t2."PSFDDCELLRPTTHD",
    t2."PSFDDRPTTHR2ECNO",
    t2."PSFDDRPTTHR2RSCP",
    t2."SENDPMOWITHQPSW"
FROM
huawei_gexport_gsm."GCELLRESELUTRANFDD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FDDRESELTIMETHD",
    t3."GSMTOFDDFORCENC2",
    t3."PSBESTFDDCELLNUM",
    t3."PSFDDCELLRPTOFF",
    t3."PSFDDCELLRPTTHD",
    t3."PSFDDRPTTHR2ECNO",
    t3."PSFDDRPTTHR2RSCP",
    t3."SENDPMOWITHQPSW"
FROM
huawei_gexport_gsm."GCELLRESELUTRANFDD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FDDRESELTIMETHD",
    t4."GSMTOFDDFORCENC2",
    t4."PSBESTFDDCELLNUM",
    t4."PSFDDCELLRPTOFF",
    t4."PSFDDCELLRPTTHD",
    t4."PSFDDRPTTHR2ECNO",
    t4."PSFDDRPTTHR2RSCP",
    t4."SENDPMOWITHQPSW"
FROM
huawei_mml_gsm."GCELLRESELUTRANFDD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLRSVPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLRSVPARA"',
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
    t1."GCELLCSDPARA1",
    t1."GCELLCSDPARA2",
    t1."GCELLCSDPARA3",
    t1."GCELLCSDPARA4",
    t1."GCELLCSDPARA5",
    t1."GCELLCSDPARA6",
    t1."GCELLCSDPARA7",
    t1."GCELLCSSWRSV0",
    t1."GCELLCSSWRSV1",
    t1."GCELLPSDPARA1",
    t1."GCELLPSDPARA11",
    t1."GCELLPSDPARA2",
    t1."GCELLPSSWRSV0",
    t1."GCELLPSSWRSV1"
FROM
huawei_nbi_gsm."GCELLRSVPARA" t1

"""
)

GCELLSBC = ReplaceableObject(
    'huawei_cm_2g."GCELLSBC"',
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
    t1."BROADCASTCONTENT",
    t1."BROADCASTINTERVAL",
    t1."CELLID",
    t1."CHANID",
    t1."GS",
    t1."SCHEME",
    t1."SUPPORTCELLBROADCAST"
FROM
huawei_nbi_gsm."GCELLSBC" t1

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
    t2."BROADCASTCONTENT",
    t2."BROADCASTINTERVAL",
    t2."CELLID",
    t2."CHANID",
    t2."GS",
    t2."SCHEME",
    t2."SUPPORTCELLBROADCAST"
FROM
huawei_gexport_gsm."GCELLSBC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BROADCASTCONTENT",
    t3."BROADCASTINTERVAL",
    t3."CELLID",
    t3."CHANID",
    t3."GS",
    t3."SCHEME",
    t3."SUPPORTCELLBROADCAST"
FROM
huawei_mml_gsm."GCELLSBC" t3
INNER JOIN huawei_mml_gsm."SYS" t31 ON t31."FileName" = t3."FileName"

"""
)

GCELLSERVPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLSERVPARA"',
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
    t1."CELLBARACCESS2",
    t1."CELLID",
    t1."EXCACC",
    t1."GPRSHCSTHR",
    t1."MSTXPWRMAX",
    t1."MULTIBANDREP",
    t1."PRIORCLASS",
    t1."RXLEVACCMIN"
FROM
huawei_nbi_gsm."GCELLSERVPARA" t1

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
    t2."CELLBARACCESS2",
    t2."CELLID",
    t2."EXCACC",
    t2."GPRSHCSTHR",
    t2."MSTXPWRMAX",
    t2."MULTIBANDREP",
    t2."PRIORCLASS",
    t2."RXLEVACCMIN"
FROM
huawei_gexport_gsm."GCELLSERVPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CELLBARACCESS2",
    t3."CELLID",
    t3."EXCACC",
    t3."GPRSHCSTHR",
    t3."MSTXPWRMAX",
    t3."MULTIBANDREP",
    t3."PRIORCLASS",
    t3."RXLEVACCMIN"
FROM
huawei_gexport_gsm."GCELLSERVPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CELLBARACCESS2",
    t4."CELLID",
    t4."EXCACC",
    t4."GPRSHCSTHR",
    t4."MSTXPWRMAX",
    t4."MULTIBANDREP",
    t4."PRIORCLASS",
    t4."RXLEVACCMIN"
FROM
huawei_mml_gsm."GCELLSERVPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLSOFT = ReplaceableObject(
    'huawei_cm_2g."GCELLSOFT"',
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
    t1."ABISFLTSTOPWAITRELINDSW",
    t1."ACTL2REEST",
    t1."ADAICADFLAG",
    t1."ADAICFLAG",
    t1."ADAPTASSIGNMENTFLOW",
    t1."AIDDELAYPROTECTTIME",
    t1."AOIPINTRAHOFAMRSETOPTSW",
    t1."ASSBETTERCELLCONGOPTSTSW",
    t1."BADELIVERYCTRL",
    t1."BADQUALDISCTHRES",
    t1."BANDINDICATOR1900",
    t1."BANDINDICATOR810",
    t1."BANDINDICATOR850",
    t1."BANDINDICATOR900",
    t1."BTSSAICPCADJSWITCH",
    t1."CALLDISCSTATOPTALLOWED",
    t1."CELLID",
    t1."CELLPAGINGOVERLOADCOUNTER",
    t1."CHANFAULTALMSWITCH",
    t1."CHNALLOCSTALOGSW",
    t1."CSFBIDENTIFYMOSW",
    t1."CSFBIDENTIFYMTSW",
    t1."CSFBIMMASSENSW",
    t1."CSFBPAGRSPBCSWITCH",
    t1."CSFBVOQULENSURSW",
    t1."CSIPPACKETCHECKSW",
    t1."CSPAGINGCTRL",
    t1."DETECTFRAMEPERIOD",
    t1."DIRMAGANSITEFLAG",
    t1."DLDTXPOLICY",
    t1."DLDTXUPDATESWITCH",
    t1."DROPCTRLABISCONNFAIL",
    t1."DROPCTRLAFTERCONN",
    t1."DROPCTRLCONNFAILHOACCFAIL",
    t1."DROPCTRLCONNFAILOM",
    t1."DROPCTRLCONNFAILOTHER",
    t1."DROPCTRLCONNFAILRLFAIL",
    t1."DROPCTRLCONNFAILRRNOTAVL",
    t1."DROPCTRLEQUIPFAIL",
    t1."DROPCTRLERRINDDMRSP",
    t1."DROPCTRLERRINDSEQERR",
    t1."DROPCTRLERRINDT200",
    t1."DROPCTRLFORCHOFAIL",
    t1."DROPCTRLINBSCHO",
    t1."DROPCTRLINTRABSCOUTHO",
    t1."DROPCTRLINTRACELLHO",
    t1."DROPCTRLNOMR",
    t1."DROPCTRLOUTBSCHOT8",
    t1."DROPCTRLRELIND",
    t1."DROPCTRLRESCHK",
    t1."DUMMYBITRANDSWITCH",
    t1."DXXMUTEDETECTPERIOD",
    t1."DXXMUTEDETECTSWITCH",
    t1."ENTSWITCH",
    t1."EXCEPFRAMETHRES",
    t1."FERRPTEN",
    t1."FLEXTSCSWITCH",
    t1."FORCEDCELLEFRSWITCH",
    t1."FORCEMSACCESS",
    t1."FREQSCANRLSTTYPE",
    t1."G900FREQCOMPOPTSW",
    t1."ICTYP",
    t1."IMMDEASACCHSW",
    t1."INTERBANDMEASURETYPE",
    t1."INTERBANDSTATALGO",
    t1."IRATSHUTDOWNSWITCH",
    t1."L2REBSUCSIGPROCSW",
    t1."MACODINGMOD",
    t1."MSCAPABLESTATSWITCH",
    t1."MUTECHECKCLASS1PERIOD",
    t1."MUTECHECKCLASS2SWITCH",
    t1."MUTECHECKPEIROD",
    t1."MUTEFORBITCALLTMINTVAL",
    t1."MUTERELCALLEN",
    t1."NOISEDETPRD",
    t1."NOISEDETSW",
    t1."NOISEDETTHD",
    t1."NOISEFUZZYSW",
    t1."NOISEPRELEVEL",
    t1."OUTSERVICEALM",
    t1."PAGINGAVGCAPACITYINPERIOD",
    t1."PAGINGLIFETIME",
    t1."PAGINGMAXCAPACITYINPERIOD",
    t1."PDCHPWRSAVEN",
    t1."PMI",
    t1."PMNUM",
    t1."PMOAFLAG",
    t1."PWRLOCATION",
    t1."QTRUCHANMANGSWITCH",
    t1."QUERYCMAFTERINBSCHO",
    t1."RACHFLTSWITCH",
    t1."RPTDLVQIALLOWED",
    t1."RSPCBITTRACESWITCH",
    t1."SDCONGSTATOPT",
    t1."SDFASTHOSWITCH",
    t1."SENDCBITTRACESWITCH",
    t1."SENDCMAFTERINBSCHO",
    t1."SI6RANDOMBIT",
    t1."STIRCALLOWED",
    t1."STOPSI5SWITCH",
    t1."SUPPORTCSFB",
    t1."TCH2SDPREEN",
    t1."TCHTIMEHOPERIOD",
    t1."TCHTIMEHOSWITCH",
    t1."TCMUTEDETECTFLAG",
    t1."TESTUSERTRACEFUN",
    t1."TMRBADQUALDISCSTAT",
    t1."TSCPLANEN",
    t1."U2GSRCMEASSW",
    t1."UMCROSSTALKOPTALLOWED",
    t1."UTRANCMDELAYFORCSFBSW",
    t1."CHANFAULTALMPDCHTH",
    t1."CHANFAULTALMTCHTH",
    t1."CHANPDOUTTIME",
    t1."LOWLEVSUBRESPREEMPTFLG",
    t1."SUBRESPREEMPTFLG"
FROM
huawei_nbi_gsm."GCELLSOFT" t1

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
    t2."ABISFLTSTOPWAITRELINDSW",
    t2."ACTL2REEST",
    t2."ADAICADFLAG",
    t2."ADAICFLAG",
    t2."ADAPTASSIGNMENTFLOW",
    t2."AIDDELAYPROTECTTIME",
    t2."AOIPINTRAHOFAMRSETOPTSW",
    t2."ASSBETTERCELLCONGOPTSTSW",
    t2."BADELIVERYCTRL",
    t2."BADQUALDISCTHRES",
    t2."BANDINDICATOR1900",
    t2."BANDINDICATOR810",
    t2."BANDINDICATOR850",
    t2."BANDINDICATOR900",
    t2."BTSSAICPCADJSWITCH",
    t2."CALLDISCSTATOPTALLOWED",
    t2."CELLID",
    t2."CELLPAGINGOVERLOADCOUNTER",
    t2."CHANFAULTALMSWITCH",
    t2."CHNALLOCSTALOGSW",
    NULL,
    NULL,
    NULL,
    t2."CSFBPAGRSPBCSWITCH",
    NULL,
    t2."CSIPPACKETCHECKSW",
    t2."CSPAGINGCTRL",
    t2."DETECTFRAMEPERIOD",
    t2."DIRMAGANSITEFLAG",
    t2."DLDTXPOLICY",
    t2."DLDTXUPDATESWITCH",
    t2."DROPCTRLABISCONNFAIL",
    t2."DROPCTRLAFTERCONN",
    t2."DROPCTRLCONNFAILHOACCFAIL",
    t2."DROPCTRLCONNFAILOM",
    t2."DROPCTRLCONNFAILOTHER",
    t2."DROPCTRLCONNFAILRLFAIL",
    t2."DROPCTRLCONNFAILRRNOTAVL",
    t2."DROPCTRLEQUIPFAIL",
    t2."DROPCTRLERRINDDMRSP",
    t2."DROPCTRLERRINDSEQERR",
    t2."DROPCTRLERRINDT200",
    t2."DROPCTRLFORCHOFAIL",
    t2."DROPCTRLINBSCHO",
    t2."DROPCTRLINTRABSCOUTHO",
    t2."DROPCTRLINTRACELLHO",
    t2."DROPCTRLNOMR",
    t2."DROPCTRLOUTBSCHOT8",
    t2."DROPCTRLRELIND",
    t2."DROPCTRLRESCHK",
    t2."DUMMYBITRANDSWITCH",
    t2."DXXMUTEDETECTPERIOD",
    t2."DXXMUTEDETECTSWITCH",
    t2."ENTSWITCH",
    t2."EXCEPFRAMETHRES",
    t2."FERRPTEN",
    t2."FLEXTSCSWITCH",
    t2."FORCEDCELLEFRSWITCH",
    t2."FORCEMSACCESS",
    t2."FREQSCANRLSTTYPE",
    t2."G900FREQCOMPOPTSW",
    t2."ICTYP",
    t2."IMMDEASACCHSW",
    t2."INTERBANDMEASURETYPE",
    t2."INTERBANDSTATALGO",
    t2."IRATSHUTDOWNSWITCH",
    t2."L2REBSUCSIGPROCSW",
    t2."MACODINGMOD",
    t2."MSCAPABLESTATSWITCH",
    t2."MUTECHECKCLASS1PERIOD",
    t2."MUTECHECKCLASS2SWITCH",
    t2."MUTECHECKPEIROD",
    t2."MUTEFORBITCALLTMINTVAL",
    t2."MUTERELCALLEN",
    t2."NOISEDETPRD",
    t2."NOISEDETSW",
    t2."NOISEDETTHD",
    t2."NOISEFUZZYSW",
    t2."NOISEPRELEVEL",
    t2."OUTSERVICEALM",
    t2."PAGINGAVGCAPACITYINPERIOD",
    t2."PAGINGLIFETIME",
    t2."PAGINGMAXCAPACITYINPERIOD",
    t2."PDCHPWRSAVEN",
    t2."PMI",
    t2."PMNUM",
    t2."PMOAFLAG",
    t2."PWRLOCATION",
    t2."QTRUCHANMANGSWITCH",
    t2."QUERYCMAFTERINBSCHO",
    t2."RACHFLTSWITCH",
    t2."RPTDLVQIALLOWED",
    t2."RSPCBITTRACESWITCH",
    t2."SDCONGSTATOPT",
    t2."SDFASTHOSWITCH",
    t2."SENDCBITTRACESWITCH",
    t2."SENDCMAFTERINBSCHO",
    t2."SI6RANDOMBIT",
    t2."STIRCALLOWED",
    t2."STOPSI5SWITCH",
    t2."SUPPORTCSFB",
    t2."TCH2SDPREEN",
    t2."TCHTIMEHOPERIOD",
    t2."TCHTIMEHOSWITCH",
    t2."TCMUTEDETECTFLAG",
    t2."TESTUSERTRACEFUN",
    t2."TMRBADQUALDISCSTAT",
    t2."TSCPLANEN",
    t2."U2GSRCMEASSW",
    t2."UMCROSSTALKOPTALLOWED",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLSOFT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISFLTSTOPWAITRELINDSW",
    t3."ACTL2REEST",
    t3."ADAICADFLAG",
    t3."ADAICFLAG",
    t3."ADAPTASSIGNMENTFLOW",
    t3."AIDDELAYPROTECTTIME",
    t3."AOIPINTRAHOFAMRSETOPTSW",
    t3."ASSBETTERCELLCONGOPTSTSW",
    t3."BADELIVERYCTRL",
    t3."BADQUALDISCTHRES",
    t3."BANDINDICATOR1900",
    t3."BANDINDICATOR810",
    t3."BANDINDICATOR850",
    t3."BANDINDICATOR900",
    t3."BTSSAICPCADJSWITCH",
    t3."CALLDISCSTATOPTALLOWED",
    t3."CELLID",
    t3."CELLPAGINGOVERLOADCOUNTER",
    t3."CHANFAULTALMSWITCH",
    t3."CHNALLOCSTALOGSW",
    NULL,
    NULL,
    NULL,
    t3."CSFBPAGRSPBCSWITCH",
    NULL,
    t3."CSIPPACKETCHECKSW",
    t3."CSPAGINGCTRL",
    t3."DETECTFRAMEPERIOD",
    t3."DIRMAGANSITEFLAG",
    t3."DLDTXPOLICY",
    t3."DLDTXUPDATESWITCH",
    t3."DROPCTRLABISCONNFAIL",
    t3."DROPCTRLAFTERCONN",
    t3."DROPCTRLCONNFAILHOACCFAIL",
    t3."DROPCTRLCONNFAILOM",
    t3."DROPCTRLCONNFAILOTHER",
    t3."DROPCTRLCONNFAILRLFAIL",
    t3."DROPCTRLCONNFAILRRNOTAVL",
    t3."DROPCTRLEQUIPFAIL",
    t3."DROPCTRLERRINDDMRSP",
    t3."DROPCTRLERRINDSEQERR",
    t3."DROPCTRLERRINDT200",
    t3."DROPCTRLFORCHOFAIL",
    t3."DROPCTRLINBSCHO",
    t3."DROPCTRLINTRABSCOUTHO",
    t3."DROPCTRLINTRACELLHO",
    t3."DROPCTRLNOMR",
    t3."DROPCTRLOUTBSCHOT8",
    t3."DROPCTRLRELIND",
    t3."DROPCTRLRESCHK",
    t3."DUMMYBITRANDSWITCH",
    t3."DXXMUTEDETECTPERIOD",
    t3."DXXMUTEDETECTSWITCH",
    t3."ENTSWITCH",
    t3."EXCEPFRAMETHRES",
    t3."FERRPTEN",
    t3."FLEXTSCSWITCH",
    t3."FORCEDCELLEFRSWITCH",
    t3."FORCEMSACCESS",
    t3."FREQSCANRLSTTYPE",
    t3."G900FREQCOMPOPTSW",
    t3."ICTYP",
    t3."IMMDEASACCHSW",
    t3."INTERBANDMEASURETYPE",
    t3."INTERBANDSTATALGO",
    t3."IRATSHUTDOWNSWITCH",
    t3."L2REBSUCSIGPROCSW",
    t3."MACODINGMOD",
    t3."MSCAPABLESTATSWITCH",
    t3."MUTECHECKCLASS1PERIOD",
    t3."MUTECHECKCLASS2SWITCH",
    t3."MUTECHECKPEIROD",
    t3."MUTEFORBITCALLTMINTVAL",
    t3."MUTERELCALLEN",
    t3."NOISEDETPRD",
    t3."NOISEDETSW",
    t3."NOISEDETTHD",
    t3."NOISEFUZZYSW",
    t3."NOISEPRELEVEL",
    t3."OUTSERVICEALM",
    t3."PAGINGAVGCAPACITYINPERIOD",
    t3."PAGINGLIFETIME",
    t3."PAGINGMAXCAPACITYINPERIOD",
    t3."PDCHPWRSAVEN",
    t3."PMI",
    t3."PMNUM",
    t3."PMOAFLAG",
    t3."PWRLOCATION",
    t3."QTRUCHANMANGSWITCH",
    t3."QUERYCMAFTERINBSCHO",
    t3."RACHFLTSWITCH",
    t3."RPTDLVQIALLOWED",
    t3."RSPCBITTRACESWITCH",
    t3."SDCONGSTATOPT",
    t3."SDFASTHOSWITCH",
    t3."SENDCBITTRACESWITCH",
    t3."SENDCMAFTERINBSCHO",
    t3."SI6RANDOMBIT",
    t3."STIRCALLOWED",
    t3."STOPSI5SWITCH",
    t3."SUPPORTCSFB",
    t3."TCH2SDPREEN",
    t3."TCHTIMEHOPERIOD",
    t3."TCHTIMEHOSWITCH",
    t3."TCMUTEDETECTFLAG",
    t3."TESTUSERTRACEFUN",
    t3."TMRBADQUALDISCSTAT",
    t3."TSCPLANEN",
    t3."U2GSRCMEASSW",
    t3."UMCROSSTALKOPTALLOWED",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLSOFT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISFLTSTOPWAITRELINDSW",
    t4."ACTL2REEST",
    t4."ADAICADFLAG",
    t4."ADAICFLAG",
    t4."ADAPTASSIGNMENTFLOW",
    t4."AIDDELAYPROTECTTIME",
    t4."AOIPINTRAHOFAMRSETOPTSW",
    t4."ASSBETTERCELLCONGOPTSTSW",
    t4."BADELIVERYCTRL",
    t4."BADQUALDISCTHRES",
    t4."BANDINDICATOR1900",
    t4."BANDINDICATOR810",
    t4."BANDINDICATOR850",
    t4."BANDINDICATOR900",
    t4."BTSSAICPCADJSWITCH",
    t4."CALLDISCSTATOPTALLOWED",
    t4."CELLID",
    t4."CELLPAGINGOVERLOADCOUNTER",
    t4."CHANFAULTALMSWITCH",
    t4."CHNALLOCSTALOGSW",
    NULL,
    NULL,
    NULL,
    t4."CSFBPAGRSPBCSWITCH",
    NULL,
    t4."CSIPPACKETCHECKSW",
    t4."CSPAGINGCTRL",
    t4."DETECTFRAMEPERIOD",
    t4."DIRMAGANSITEFLAG",
    t4."DLDTXPOLICY",
    t4."DLDTXUPDATESWITCH",
    t4."DROPCTRLABISCONNFAIL",
    t4."DROPCTRLAFTERCONN",
    t4."DROPCTRLCONNFAILHOACCFAIL",
    t4."DROPCTRLCONNFAILOM",
    t4."DROPCTRLCONNFAILOTHER",
    t4."DROPCTRLCONNFAILRLFAIL",
    t4."DROPCTRLCONNFAILRRNOTAVL",
    t4."DROPCTRLEQUIPFAIL",
    t4."DROPCTRLERRINDDMRSP",
    t4."DROPCTRLERRINDSEQERR",
    t4."DROPCTRLERRINDT200",
    t4."DROPCTRLFORCHOFAIL",
    t4."DROPCTRLINBSCHO",
    t4."DROPCTRLINTRABSCOUTHO",
    t4."DROPCTRLINTRACELLHO",
    t4."DROPCTRLNOMR",
    t4."DROPCTRLOUTBSCHOT8",
    t4."DROPCTRLRELIND",
    t4."DROPCTRLRESCHK",
    t4."DUMMYBITRANDSWITCH",
    t4."DXXMUTEDETECTPERIOD",
    t4."DXXMUTEDETECTSWITCH",
    t4."ENTSWITCH",
    t4."EXCEPFRAMETHRES",
    t4."FERRPTEN",
    t4."FLEXTSCSWITCH",
    t4."FORCEDCELLEFRSWITCH",
    t4."FORCEMSACCESS",
    t4."FREQSCANRLSTTYPE",
    t4."G900FREQCOMPOPTSW",
    t4."ICTYP",
    t4."IMMDEASACCHSW",
    t4."INTERBANDMEASURETYPE",
    t4."INTERBANDSTATALGO",
    t4."IRATSHUTDOWNSWITCH",
    t4."L2REBSUCSIGPROCSW",
    t4."MACODINGMOD",
    t4."MSCAPABLESTATSWITCH",
    t4."MUTECHECKCLASS1PERIOD",
    t4."MUTECHECKCLASS2SWITCH",
    t4."MUTECHECKPEIROD",
    t4."MUTEFORBITCALLTMINTVAL",
    t4."MUTERELCALLEN",
    t4."NOISEDETPRD",
    t4."NOISEDETSW",
    t4."NOISEDETTHD",
    t4."NOISEFUZZYSW",
    t4."NOISEPRELEVEL",
    t4."OUTSERVICEALM",
    t4."PAGINGAVGCAPACITYINPERIOD",
    t4."PAGINGLIFETIME",
    t4."PAGINGMAXCAPACITYINPERIOD",
    t4."PDCHPWRSAVEN",
    t4."PMI",
    t4."PMNUM",
    t4."PMOAFLAG",
    t4."PWRLOCATION",
    t4."QTRUCHANMANGSWITCH",
    t4."QUERYCMAFTERINBSCHO",
    t4."RACHFLTSWITCH",
    t4."RPTDLVQIALLOWED",
    t4."RSPCBITTRACESWITCH",
    t4."SDCONGSTATOPT",
    t4."SDFASTHOSWITCH",
    t4."SENDCBITTRACESWITCH",
    t4."SENDCMAFTERINBSCHO",
    t4."SI6RANDOMBIT",
    t4."STIRCALLOWED",
    t4."STOPSI5SWITCH",
    t4."SUPPORTCSFB",
    t4."TCH2SDPREEN",
    t4."TCHTIMEHOPERIOD",
    t4."TCHTIMEHOSWITCH",
    t4."TCMUTEDETECTFLAG",
    t4."TESTUSERTRACEFUN",
    t4."TMRBADQUALDISCSTAT",
    t4."TSCPLANEN",
    t4."U2GSRCMEASSW",
    t4."UMCROSSTALKOPTALLOWED",
    NULL,
    NULL,
    NULL,
    NULL,
    t4."LOWLEVSUBRESPREEMPTFLG",
    t4."SUBRESPREEMPTFLG"
FROM
huawei_mml_gsm."GCELLSOFT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLSON = ReplaceableObject(
    'huawei_cm_2g."GCELLSON"',
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
    t1."PAGINGOVLDCTRLSTTHLD",
    t1."TCHCONGCTRLSTTHLD"
FROM
huawei_nbi_gsm."GCELLSON" t1

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
    t2."PAGINGOVLDCTRLSTTHLD",
    t2."TCHCONGCTRLSTTHLD"
FROM
huawei_gexport_gsm."GCELLSON_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PAGINGOVLDCTRLSTTHLD",
    t3."TCHCONGCTRLSTTHLD"
FROM
huawei_gexport_gsm."GCELLSON_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PAGINGOVLDCTRLSTTHLD",
    t4."TCHCONGCTRLSTTHLD"
FROM
huawei_mml_gsm."GCELLSON" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLSRVCC = ReplaceableObject(
    'huawei_cm_2g."GCELLSRVCC"',
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
    t1."SRVCCBUSYTHRESOFFSET",
    t1."SRVCCPMTQUEUESW",
    t1."SRVCCRAPIDSELMEASOPTSW",
    t1."SRVCCRAPIDSELSW",
    t1."SRVCCSTATINTERRANHO",
    t1."SRVCCVAMOSCFGPOLICY"
FROM
huawei_nbi_gsm."GCELLSRVCC" t1

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
    t2."SRVCCBUSYTHRESOFFSET",
    t2."SRVCCPMTQUEUESW",
    t2."SRVCCRAPIDSELMEASOPTSW",
    t2."SRVCCRAPIDSELSW",
    t2."SRVCCSTATINTERRANHO",
    t2."SRVCCVAMOSCFGPOLICY"
FROM
huawei_gexport_gsm."GCELLSRVCC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SRVCCBUSYTHRESOFFSET",
    t3."SRVCCPMTQUEUESW",
    t3."SRVCCRAPIDSELMEASOPTSW",
    t3."SRVCCRAPIDSELSW",
    t3."SRVCCSTATINTERRANHO",
    t3."SRVCCVAMOSCFGPOLICY"
FROM
huawei_gexport_gsm."GCELLSRVCC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SRVCCBUSYTHRESOFFSET",
    t4."SRVCCPMTQUEUESW",
    t4."SRVCCRAPIDSELMEASOPTSW",
    t4."SRVCCRAPIDSELSW",
    t4."SRVCCSTATINTERRANHO",
    t4."SRVCCVAMOSCFGPOLICY"
FROM
huawei_mml_gsm."GCELLSRVCC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLSTANDARDOPTPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLSTANDARDOPTPARA"',
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
    t1."N3101",
    t1."N3103",
    t1."N3105"
FROM
huawei_nbi_gsm."GCELLSTANDARDOPTPARA" t1

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
    t2."N3101",
    t2."N3103",
    t2."N3105"
FROM
huawei_gexport_gsm."GCELLSTANDARDOPTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."N3101",
    t3."N3103",
    t3."N3105"
FROM
huawei_gexport_gsm."GCELLSTANDARDOPTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."N3101",
    t4."N3103",
    t4."N3105"
FROM
huawei_mml_gsm."GCELLSTANDARDOPTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLTA = ReplaceableObject(
    'huawei_cm_2g."GCELLTA"',
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
    t1."ESTINDTHD",
    t1."HIGHPRECISIONTA",
    t1."PSTATHD",
    t1."RACHTATHD",
    t1."SDCCHTATHD",
    t1."SDCCHTATHDOFFSET",
    t1."TCHTAFILTERLEN",
    t1."TCHTATHD"
FROM
huawei_nbi_gsm."GCELLTA" t1

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
    t2."ESTINDTHD",
    t2."HIGHPRECISIONTA",
    t2."PSTATHD",
    t2."RACHTATHD",
    t2."SDCCHTATHD",
    t2."SDCCHTATHDOFFSET",
    t2."TCHTAFILTERLEN",
    t2."TCHTATHD"
FROM
huawei_gexport_gsm."GCELLTA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ESTINDTHD",
    t3."HIGHPRECISIONTA",
    t3."PSTATHD",
    t3."RACHTATHD",
    t3."SDCCHTATHD",
    t3."SDCCHTATHDOFFSET",
    t3."TCHTAFILTERLEN",
    t3."TCHTATHD"
FROM
huawei_gexport_gsm."GCELLTA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ESTINDTHD",
    t4."HIGHPRECISIONTA",
    t4."PSTATHD",
    t4."RACHTATHD",
    t4."SDCCHTATHD",
    t4."SDCCHTATHDOFFSET",
    t4."TCHTAFILTERLEN",
    t4."TCHTATHD"
FROM
huawei_mml_gsm."GCELLTA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLTEMPLATERSC = ReplaceableObject(
    'huawei_cm_2g."GCELLTEMPLATERSC"',
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
    t1."TEMPLATENAME"
FROM
huawei_nbi_gsm."GCELLTEMPLATERSC" t1

"""
)

GCELLTMR = ReplaceableObject(
    'huawei_cm_2g."GCELLTMR"',
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
    t1."ASSTIMER",
    t1."CELLID",
    t1."CIPHERCOMPLETETMR",
    t1."DELAYSENDRFCHREL",
    t1."DIRECTHOWAIT3GNCELLTIMER",
    t1."ESTABINDTIMER",
    t1."GPRSRESUMEACKTMR",
    t1."IMMASSAINTERFTIMER",
    t1."IMMREJWAITINDTIMER",
    t1."INBSCHOTIMER",
    t1."INTRABSCCODECHOCMDTIMER",
    t1."INTRABSCHOTIMER",
    t1."INTRACELLHOTIMER",
    t1."MSIPFAILINDDELAY",
    t1."NORMALRELWAITFORRFCHRELACK",
    t1."OUTBSCHOCLEARTIMER",
    t1."OUTBSCHOCMDTIMER",
    t1."RLMODEMODTIMER",
    t1."SAIP3ESTABCONFERTMRMSIP",
    t1."TIQUEUINGTIMER",
    t1."TQHO",
    t1."ULDATAFWDTMR",
    t1."UMMODEMODITIMER",
    t1."WAITCRDLCBTSLPCNF",
    t1."WAITFORCHANACTACKMSG",
    t1."WAITFORRELIND",
    t1."WAITFORRELINDAMRFR",
    t1."WAITFORRELINDAMRHR",
    t1."WAITLOCALSWITCHFORHO",
    t1."WAITRESVCHANREFRESHTIMER",
    t1."WTSDFASTHOTRIGTMR"
FROM
huawei_nbi_gsm."GCELLTMR" t1

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
    t2."ASSTIMER",
    t2."CELLID",
    t2."CIPHERCOMPLETETMR",
    t2."DELAYSENDRFCHREL",
    t2."DIRECTHOWAIT3GNCELLTIMER",
    t2."ESTABINDTIMER",
    t2."GPRSRESUMEACKTMR",
    t2."IMMASSAINTERFTIMER",
    t2."IMMREJWAITINDTIMER",
    t2."INBSCHOTIMER",
    t2."INTRABSCCODECHOCMDTIMER",
    t2."INTRABSCHOTIMER",
    t2."INTRACELLHOTIMER",
    t2."MSIPFAILINDDELAY",
    t2."NORMALRELWAITFORRFCHRELACK",
    t2."OUTBSCHOCLEARTIMER",
    t2."OUTBSCHOCMDTIMER",
    t2."RLMODEMODTIMER",
    t2."SAIP3ESTABCONFERTMRMSIP",
    t2."TIQUEUINGTIMER",
    t2."TQHO",
    t2."ULDATAFWDTMR",
    t2."UMMODEMODITIMER",
    t2."WAITCRDLCBTSLPCNF",
    t2."WAITFORCHANACTACKMSG",
    t2."WAITFORRELIND",
    t2."WAITFORRELINDAMRFR",
    t2."WAITFORRELINDAMRHR",
    t2."WAITLOCALSWITCHFORHO",
    t2."WAITRESVCHANREFRESHTIMER",
    t2."WTSDFASTHOTRIGTMR"
FROM
huawei_gexport_gsm."GCELLTMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ASSTIMER",
    t3."CELLID",
    t3."CIPHERCOMPLETETMR",
    t3."DELAYSENDRFCHREL",
    t3."DIRECTHOWAIT3GNCELLTIMER",
    t3."ESTABINDTIMER",
    t3."GPRSRESUMEACKTMR",
    t3."IMMASSAINTERFTIMER",
    t3."IMMREJWAITINDTIMER",
    t3."INBSCHOTIMER",
    t3."INTRABSCCODECHOCMDTIMER",
    t3."INTRABSCHOTIMER",
    t3."INTRACELLHOTIMER",
    t3."MSIPFAILINDDELAY",
    t3."NORMALRELWAITFORRFCHRELACK",
    t3."OUTBSCHOCLEARTIMER",
    t3."OUTBSCHOCMDTIMER",
    t3."RLMODEMODTIMER",
    t3."SAIP3ESTABCONFERTMRMSIP",
    t3."TIQUEUINGTIMER",
    t3."TQHO",
    t3."ULDATAFWDTMR",
    t3."UMMODEMODITIMER",
    t3."WAITCRDLCBTSLPCNF",
    t3."WAITFORCHANACTACKMSG",
    t3."WAITFORRELIND",
    t3."WAITFORRELINDAMRFR",
    t3."WAITFORRELINDAMRHR",
    t3."WAITLOCALSWITCHFORHO",
    t3."WAITRESVCHANREFRESHTIMER",
    t3."WTSDFASTHOTRIGTMR"
FROM
huawei_gexport_gsm."GCELLTMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ASSTIMER",
    t4."CELLID",
    t4."CIPHERCOMPLETETMR",
    t4."DELAYSENDRFCHREL",
    t4."DIRECTHOWAIT3GNCELLTIMER",
    t4."ESTABINDTIMER",
    t4."GPRSRESUMEACKTMR",
    t4."IMMASSAINTERFTIMER",
    t4."IMMREJWAITINDTIMER",
    t4."INBSCHOTIMER",
    t4."INTRABSCCODECHOCMDTIMER",
    t4."INTRABSCHOTIMER",
    t4."INTRACELLHOTIMER",
    t4."MSIPFAILINDDELAY",
    t4."NORMALRELWAITFORRFCHRELACK",
    t4."OUTBSCHOCLEARTIMER",
    t4."OUTBSCHOCMDTIMER",
    t4."RLMODEMODTIMER",
    t4."SAIP3ESTABCONFERTMRMSIP",
    t4."TIQUEUINGTIMER",
    t4."TQHO",
    t4."ULDATAFWDTMR",
    t4."UMMODEMODITIMER",
    t4."WAITCRDLCBTSLPCNF",
    t4."WAITFORCHANACTACKMSG",
    t4."WAITFORRELIND",
    t4."WAITFORRELINDAMRFR",
    t4."WAITFORRELINDAMRHR",
    t4."WAITLOCALSWITCHFORHO",
    t4."WAITRESVCHANREFRESHTIMER",
    t4."WTSDFASTHOTRIGTMR"
FROM
huawei_mml_gsm."GCELLTMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLTRANPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLTRANPARA"',
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
    t1."JITTBUFFETHD",
    t1."JITTBUFSEQFETHD",
    t1."JITTBUFWNDDECPERIOD",
    t1."JITTBUFWNDMINPERIOD",
    t1."JITTBUFWNDSIZE"
FROM
huawei_nbi_gsm."GCELLTRANPARA" t1

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
    t2."JITTBUFFETHD",
    t2."JITTBUFSEQFETHD",
    t2."JITTBUFWNDDECPERIOD",
    t2."JITTBUFWNDMINPERIOD",
    t2."JITTBUFWNDSIZE"
FROM
huawei_gexport_gsm."GCELLTRANPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."JITTBUFFETHD",
    t3."JITTBUFSEQFETHD",
    t3."JITTBUFWNDDECPERIOD",
    t3."JITTBUFWNDMINPERIOD",
    t3."JITTBUFWNDSIZE"
FROM
huawei_gexport_gsm."GCELLTRANPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."JITTBUFFETHD",
    t4."JITTBUFSEQFETHD",
    t4."JITTBUFWNDDECPERIOD",
    t4."JITTBUFWNDMINPERIOD",
    t4."JITTBUFWNDSIZE"
FROM
huawei_mml_gsm."GCELLTRANPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLUNDPARA = ReplaceableObject(
    'huawei_cm_2g."GCELLUNDPARA"',
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
    t1."GUNBADQUALCHNUM",
    t1."GUNBADQUALCLRTHRD",
    t1."GUNBADQUALDETCTTHRD",
    t1."GUNBADQUALTHRD",
    t1."GUNBTSTATBASE",
    t1."GUNCHBADQUALSTATBASE",
    t1."GUNCHDROPBASE",
    t1."GUNCHDROPCLRTHRD",
    t1."GUNCHDROPDECTTHRD",
    t1."GUNFAULTDECTSW",
    t1."GUNRESETSW",
    t1."GUNRPDROPWNSW",
    t1."GUNRPDWBADQUALWNSW",
    t1."GUNRPFAULTINFO",
    t1."GUNRPUPBADQUALWNSW"
FROM
huawei_nbi_gsm."GCELLUNDPARA" t1

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
    t2."GUNBADQUALCHNUM",
    t2."GUNBADQUALCLRTHRD",
    t2."GUNBADQUALDETCTTHRD",
    t2."GUNBADQUALTHRD",
    t2."GUNBTSTATBASE",
    t2."GUNCHBADQUALSTATBASE",
    t2."GUNCHDROPBASE",
    t2."GUNCHDROPCLRTHRD",
    t2."GUNCHDROPDECTTHRD",
    t2."GUNFAULTDECTSW",
    t2."GUNRESETSW",
    t2."GUNRPDROPWNSW",
    t2."GUNRPDWBADQUALWNSW",
    t2."GUNRPFAULTINFO",
    t2."GUNRPUPBADQUALWNSW"
FROM
huawei_gexport_gsm."GCELLUNDPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."GUNBADQUALCHNUM",
    t3."GUNBADQUALCLRTHRD",
    t3."GUNBADQUALDETCTTHRD",
    t3."GUNBADQUALTHRD",
    t3."GUNBTSTATBASE",
    t3."GUNCHBADQUALSTATBASE",
    t3."GUNCHDROPBASE",
    t3."GUNCHDROPCLRTHRD",
    t3."GUNCHDROPDECTTHRD",
    t3."GUNFAULTDECTSW",
    t3."GUNRESETSW",
    t3."GUNRPDROPWNSW",
    t3."GUNRPDWBADQUALWNSW",
    t3."GUNRPFAULTINFO",
    t3."GUNRPUPBADQUALWNSW"
FROM
huawei_gexport_gsm."GCELLUNDPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GUNBADQUALCHNUM",
    t4."GUNBADQUALCLRTHRD",
    t4."GUNBADQUALDETCTTHRD",
    t4."GUNBADQUALTHRD",
    t4."GUNBTSTATBASE",
    t4."GUNCHBADQUALSTATBASE",
    t4."GUNCHDROPBASE",
    t4."GUNCHDROPCLRTHRD",
    t4."GUNCHDROPDECTTHRD",
    t4."GUNFAULTDECTSW",
    t4."GUNRESETSW",
    t4."GUNRPDROPWNSW",
    t4."GUNRPDWBADQUALWNSW",
    t4."GUNRPFAULTINFO",
    t4."GUNRPUPBADQUALWNSW"
FROM
huawei_mml_gsm."GCELLUNDPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLVAMOS = ReplaceableObject(
    'huawei_cm_2g."GCELLVAMOS"',
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
    t1."TSCUNIFYSW",
    t1."VAMOSSWITCH",
    t1."MULTALLOWBEFORECONN",
    t1."MUTESAICIDESWITCH",
    t1."MUTESAICSWITCH",
    t1."OPTVAMOSCHNMULALG",
    t1."SAICALPHAJUMPPRD",
    t1."SAICALPHAJUMPVALUE",
    t1."SAICPROMSIDESWITCH",
    t1."SAICPROMSSWITCH",
    t1."SPEMSIDEATCBTHD",
    t1."SPEMSIDEDLRXQUALTHD",
    t1."SPEMSIDELASTTIMES",
    t1."SPEMSIDELOAD",
    t1."SPEMSIDEMAXCALLS",
    t1."SPEMSIDESTATTIMES",
    t1."SPEMSIDEULRXQUALTHD",
    t1."UNKOWNSAICMULTSWITCH",
    t1."VAMOSASSDLRXLEVTHDOFFSET",
    t1."VAMOSASSLOADOFT",
    t1."VAMOSASSMULTATCBOFFSET",
    t1."VAMOSASSSWITCH",
    t1."VAMOSASSULQUALTHDOFFSET",
    t1."VAMOSDEPOLRXQUALOFT",
    t1."VAMOSINTRAHODLQUALTHD",
    t1."VAMOSINTRAHODLRXLEVTHD",
    t1."VAMOSINTRAHONONESAICATCBTHD",
    t1."VAMOSINTRAHOSAICATCBTHD",
    t1."VAMOSINTRAHOSWITCH",
    t1."VAMOSINTRAHOULQUALTHD",
    t1."VAMOSINTRAHOVAMOS1ATCBTHD",
    t1."VAMOSINTRAHOVAMOS2ATCBTHD",
    t1."VAMOSIUOINNERATCBTHD",
    t1."VAMOSIUOINNERLOADTHD",
    t1."VAMOSLOADREUSELOADTHD",
    t1."VAMOSLOADREUSESWITCH",
    t1."VAMOSMAINTSC",
    t1."VAMOSMULTLOADTHD",
    t1."VAMOSNONESAICALLOW",
    t1."VAMOSOLDCALLLASTTIMES",
    t1."VAMOSOLDCALLSTATTIMES",
    t1."VAMOSOLRXLEVOFT",
    t1."VAMOSOLRXQUALOFT",
    t1."VAMOSPATHLOSSMAXDIFFVALUE",
    t1."VAMOSQUALREUSEDOWNLINKQUALTHD",
    t1."VAMOSQUALREUSELASTTIMES",
    t1."VAMOSQUALREUSESTATTIMES",
    t1."VAMOSQUALREUSESWITCH",
    t1."VAMOSQUALREUSEUPLINKQUALTHD",
    t1."VAMOSQUALUNDOPNTSWITCH",
    t1."VAMOSSUBTSC"
FROM
huawei_nbi_gsm."GCELLVAMOS" t1

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
    t2."TSCUNIFYSW",
    t2."VAMOSSWITCH",
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
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLVAMOS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."TSCUNIFYSW",
    t3."VAMOSSWITCH",
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
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCELLVAMOS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TSCUNIFYSW",
    t4."VAMOSSWITCH",
    t4."MULTALLOWBEFORECONN",
    t4."MUTESAICIDESWITCH",
    t4."MUTESAICSWITCH",
    t4."OPTVAMOSCHNMULALG",
    t4."SAICALPHAJUMPPRD",
    t4."SAICALPHAJUMPVALUE",
    t4."SAICPROMSIDESWITCH",
    t4."SAICPROMSSWITCH",
    t4."SPEMSIDEATCBTHD",
    t4."SPEMSIDEDLRXQUALTHD",
    t4."SPEMSIDELASTTIMES",
    t4."SPEMSIDELOAD",
    t4."SPEMSIDEMAXCALLS",
    t4."SPEMSIDESTATTIMES",
    t4."SPEMSIDEULRXQUALTHD",
    t4."UNKOWNSAICMULTSWITCH",
    t4."VAMOSASSDLRXLEVTHDOFFSET",
    t4."VAMOSASSLOADOFT",
    t4."VAMOSASSMULTATCBOFFSET",
    t4."VAMOSASSSWITCH",
    t4."VAMOSASSULQUALTHDOFFSET",
    t4."VAMOSDEPOLRXQUALOFT",
    t4."VAMOSINTRAHODLQUALTHD",
    t4."VAMOSINTRAHODLRXLEVTHD",
    t4."VAMOSINTRAHONONESAICATCBTHD",
    t4."VAMOSINTRAHOSAICATCBTHD",
    t4."VAMOSINTRAHOSWITCH",
    t4."VAMOSINTRAHOULQUALTHD",
    t4."VAMOSINTRAHOVAMOS1ATCBTHD",
    t4."VAMOSINTRAHOVAMOS2ATCBTHD",
    t4."VAMOSIUOINNERATCBTHD",
    t4."VAMOSIUOINNERLOADTHD",
    NULL,
    t4."VAMOSLOADREUSESWITCH",
    t4."VAMOSMAINTSC",
    t4."VAMOSMULTLOADTHD",
    t4."VAMOSNONESAICALLOW",
    t4."VAMOSOLDCALLLASTTIMES",
    t4."VAMOSOLDCALLSTATTIMES",
    t4."VAMOSOLRXLEVOFT",
    t4."VAMOSOLRXQUALOFT",
    t4."VAMOSPATHLOSSMAXDIFFVALUE",
    NULL,
    NULL,
    NULL,
    t4."VAMOSQUALREUSESWITCH",
    NULL,
    NULL,
    t4."VAMOSSUBTSC"
FROM
huawei_mml_gsm."GCELLVAMOS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLVAMOSPWR = ReplaceableObject(
    'huawei_cm_2g."GCELLVAMOSPWR"',
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
    t1."ALPHAQPSKADJSCOPE",
    t1."ALPHAQPSKAMRFRRXQUALTHD",
    t1."ALPHAQPSKAMRHRRXQUALTHD",
    t1."ALPHAQPSKCTRLSWITCH",
    t1."ALPHAQPSKFRRXQUALTHD",
    t1."ALPHAQPSKHRRXQUALTHD",
    t1."ALPHAQPSKRXLVLADJFAC",
    t1."ALPHAQPSKRXLVLPROFAC",
    t1."ALPHAQPSKRXLVLTHD",
    t1."ALPHAQPSKRXQUALADJFAC",
    t1."ALPHAQPSKRXQUALPROFAC",
    t1."CELLID",
    t1."SICAMRFRRXQUALTHD",
    t1."SICAMRHRRXQUALTHD",
    t1."SICDIFFHIGHTHD",
    t1."SICFRRXQUALTHD",
    t1."SICHRRXQUALTHD",
    t1."SICPWRCTRLSWITCH",
    t1."SICRXLVLADJFAC",
    t1."SICRXLVLPROFAC",
    t1."SICRXLVLTHD",
    t1."SICRXQUALADJFAC",
    t1."SICRXQUALPROFAC",
    t1."VAMOSINITPCDLSIGTHR",
    t1."VAMOSINITPCULSIGTHR"
FROM
huawei_nbi_gsm."GCELLVAMOSPWR" t1

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
    t2."ALPHAQPSKADJSCOPE",
    t2."ALPHAQPSKAMRFRRXQUALTHD",
    t2."ALPHAQPSKAMRHRRXQUALTHD",
    t2."ALPHAQPSKCTRLSWITCH",
    t2."ALPHAQPSKFRRXQUALTHD",
    t2."ALPHAQPSKHRRXQUALTHD",
    t2."ALPHAQPSKRXLVLADJFAC",
    t2."ALPHAQPSKRXLVLPROFAC",
    t2."ALPHAQPSKRXLVLTHD",
    t2."ALPHAQPSKRXQUALADJFAC",
    t2."ALPHAQPSKRXQUALPROFAC",
    t2."CELLID",
    t2."SICAMRFRRXQUALTHD",
    t2."SICAMRHRRXQUALTHD",
    t2."SICDIFFHIGHTHD",
    t2."SICFRRXQUALTHD",
    t2."SICHRRXQUALTHD",
    t2."SICPWRCTRLSWITCH",
    t2."SICRXLVLADJFAC",
    t2."SICRXLVLPROFAC",
    t2."SICRXLVLTHD",
    t2."SICRXQUALADJFAC",
    t2."SICRXQUALPROFAC",
    t2."VAMOSINITPCDLSIGTHR",
    t2."VAMOSINITPCULSIGTHR"
FROM
huawei_gexport_gsm."GCELLVAMOSPWR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALPHAQPSKADJSCOPE",
    t3."ALPHAQPSKAMRFRRXQUALTHD",
    t3."ALPHAQPSKAMRHRRXQUALTHD",
    t3."ALPHAQPSKCTRLSWITCH",
    t3."ALPHAQPSKFRRXQUALTHD",
    t3."ALPHAQPSKHRRXQUALTHD",
    t3."ALPHAQPSKRXLVLADJFAC",
    t3."ALPHAQPSKRXLVLPROFAC",
    t3."ALPHAQPSKRXLVLTHD",
    t3."ALPHAQPSKRXQUALADJFAC",
    t3."ALPHAQPSKRXQUALPROFAC",
    t3."CELLID",
    t3."SICAMRFRRXQUALTHD",
    t3."SICAMRHRRXQUALTHD",
    t3."SICDIFFHIGHTHD",
    t3."SICFRRXQUALTHD",
    t3."SICHRRXQUALTHD",
    t3."SICPWRCTRLSWITCH",
    t3."SICRXLVLADJFAC",
    t3."SICRXLVLPROFAC",
    t3."SICRXLVLTHD",
    t3."SICRXQUALADJFAC",
    t3."SICRXQUALPROFAC",
    t3."VAMOSINITPCDLSIGTHR",
    t3."VAMOSINITPCULSIGTHR"
FROM
huawei_gexport_gsm."GCELLVAMOSPWR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALPHAQPSKADJSCOPE",
    t4."ALPHAQPSKAMRFRRXQUALTHD",
    t4."ALPHAQPSKAMRHRRXQUALTHD",
    t4."ALPHAQPSKCTRLSWITCH",
    t4."ALPHAQPSKFRRXQUALTHD",
    t4."ALPHAQPSKHRRXQUALTHD",
    t4."ALPHAQPSKRXLVLADJFAC",
    t4."ALPHAQPSKRXLVLPROFAC",
    t4."ALPHAQPSKRXLVLTHD",
    t4."ALPHAQPSKRXQUALADJFAC",
    t4."ALPHAQPSKRXQUALPROFAC",
    t4."CELLID",
    t4."SICAMRFRRXQUALTHD",
    t4."SICAMRHRRXQUALTHD",
    t4."SICDIFFHIGHTHD",
    t4."SICFRRXQUALTHD",
    t4."SICHRRXQUALTHD",
    t4."SICPWRCTRLSWITCH",
    t4."SICRXLVLADJFAC",
    t4."SICRXLVLPROFAC",
    t4."SICRXLVLTHD",
    t4."SICRXQUALADJFAC",
    t4."SICRXQUALPROFAC",
    t4."VAMOSINITPCDLSIGTHR",
    t4."VAMOSINITPCULSIGTHR"
FROM
huawei_mml_gsm."GCELLVAMOSPWR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCELLWLAN = ReplaceableObject(
    'huawei_cm_2g."GCELLWLAN"',
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
    t1."LOADTHRSTPWLAN",
    t1."LOADTHRTOWLAN",
    t1."STPWIFITMR",
    t1."WIFITMR",
    t1."WLANACCONN",
    t1."WLANCTRL"
FROM
huawei_nbi_gsm."GCELLWLAN" t1

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
    t2."LOADTHRSTPWLAN",
    t2."LOADTHRTOWLAN",
    t2."STPWIFITMR",
    t2."WIFITMR",
    t2."WLANACCONN",
    t2."WLANCTRL"
FROM
huawei_gexport_gsm."GCELLWLAN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LOADTHRSTPWLAN",
    t3."LOADTHRTOWLAN",
    t3."STPWIFITMR",
    t3."WIFITMR",
    t3."WLANACCONN",
    t3."WLANCTRL"
FROM
huawei_gexport_gsm."GCELLWLAN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LOADTHRSTPWLAN",
    t4."LOADTHRTOWLAN",
    t4."STPWIFITMR",
    t4."WIFITMR",
    t4."WLANACCONN",
    t4."WLANCTRL"
FROM
huawei_mml_gsm."GCELLWLAN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCNCFGALMTHD = ReplaceableObject(
    'huawei_cm_2g."GCNCFGALMTHD"',
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
    t1."CSNRIDIFFRATIOTHD",
    t1."CSTMSIREALLOCMINNUM",
    t1."PSNRIDIFFRATIOTHD",
    t1."PSPTMSIREALLOCMINNUM"
FROM
huawei_nbi_gsm."GCNCFGALMTHD" t1

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
    t2."CSNRIDIFFRATIOTHD",
    t2."CSTMSIREALLOCMINNUM",
    t2."PSNRIDIFFRATIOTHD",
    t2."PSPTMSIREALLOCMINNUM"
FROM
huawei_gexport_gsm."GCNCFGALMTHD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CSNRIDIFFRATIOTHD",
    t3."CSTMSIREALLOCMINNUM",
    t3."PSNRIDIFFRATIOTHD",
    t3."PSPTMSIREALLOCMINNUM"
FROM
huawei_gexport_gsm."GCNCFGALMTHD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CSNRIDIFFRATIOTHD",
    t4."CSTMSIREALLOCMINNUM",
    t4."PSNRIDIFFRATIOTHD",
    t4."PSPTMSIREALLOCMINNUM"
FROM
huawei_mml_gsm."GCNCFGALMTHD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCNNODE = ReplaceableObject(
    'huawei_cm_2g."GCNNODE"',
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
    t1."ATRANSMODE",
    t1."BSSLSMSCCOOP",
    t1."CNID",
    t1."CNNODEIDX",
    t1."CODECRPTFLG",
    t1."DFDPC",
    t1."DPCGIDX",
    t1."DPX",
    t1."FORBIDNO7FLASHDISC",
    t1."MSCCAP",
    t1."MSCSTATUE",
    t1."OPNAME",
    t1."RTCPBWRATIO",
    t1."RTCPSWITCH",
    t1."UNITED_FC_SWITCH",
    t1."SAGSMRMSC"
FROM
huawei_nbi_gsm."GCNNODE" t1

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
    t2."ATRANSMODE",
    t2."BSSLSMSCCOOP",
    t2."CNID",
    t2."CNNODEIDX",
    t2."CODECRPTFLG",
    t2."DFDPC",
    t2."DPCGIDX",
    t2."DPX",
    t2."FORBIDNO7FLASHDISC",
    t2."MSCCAP",
    t2."MSCSTATUE",
    t2."OPNAME",
    t2."RTCPBWRATIO",
    t2."RTCPSWITCH",
    t2."UNITED_FC_SWITCH",
    NULL
FROM
huawei_gexport_gsm."GCNNODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ATRANSMODE",
    t3."BSSLSMSCCOOP",
    t3."CNID",
    t3."CNNODEIDX",
    t3."CODECRPTFLG",
    t3."DFDPC",
    t3."DPCGIDX",
    t3."DPX",
    t3."FORBIDNO7FLASHDISC",
    t3."MSCCAP",
    t3."MSCSTATUE",
    t3."OPNAME",
    t3."RTCPBWRATIO",
    t3."RTCPSWITCH",
    t3."UNITED_FC_SWITCH",
    NULL
FROM
huawei_gexport_gsm."GCNNODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ATRANSMODE",
    t4."BSSLSMSCCOOP",
    t4."CNID",
    t4."CNNODEIDX",
    t4."CODECRPTFLG",
    t4."DFDPC",
    t4."DPCGIDX",
    t4."DPX",
    t4."FORBIDNO7FLASHDISC",
    t4."MSCCAP",
    t4."MSCSTATUE",
    t4."OPNAME",
    t4."RTCPBWRATIO",
    t4."RTCPSWITCH",
    t4."UNITED_FC_SWITCH",
    NULL
FROM
huawei_mml_gsm."GCNNODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCNOPERATOR = ReplaceableObject(
    'huawei_cm_2g."GCNOPERATOR"',
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
    t1."HOBTWNOTHOPALLOW",
    t1."LOADBALANCEALG",
    t1."MCC",
    t1."MNC",
    t1."MSCNRILEN",
    t1."MSCNULLNRI",
    t1."MSCPOOLALLOW",
    t1."OPERATORTYPE",
    t1."OPINDEX",
    t1."OPNAME",
    t1."SGSNNRILEN",
    t1."SGSNNULLNRI",
    t1."SGSNPOOLALLOW",
    t1."SPPRTCB",
    t1."TIIMSIPAGING",
    t1."TIWAITMSCMSG"
FROM
huawei_nbi_gsm."GCNOPERATOR" t1

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
    t2."HOBTWNOTHOPALLOW",
    NULL,
    t2."MCC",
    t2."MNC",
    NULL,
    NULL,
    t2."MSCPOOLALLOW",
    t2."OPERATORTYPE",
    t2."OPINDEX",
    t2."OPNAME",
    NULL,
    NULL,
    t2."SGSNPOOLALLOW",
    t2."SPPRTCB",
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCNOPERATOR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."HOBTWNOTHOPALLOW",
    NULL,
    t3."MCC",
    t3."MNC",
    NULL,
    NULL,
    t3."MSCPOOLALLOW",
    t3."OPERATORTYPE",
    t3."OPINDEX",
    t3."OPNAME",
    NULL,
    NULL,
    t3."SGSNPOOLALLOW",
    t3."SPPRTCB",
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCNOPERATOR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."HOBTWNOTHOPALLOW",
    NULL,
    t4."MCC",
    t4."MNC",
    NULL,
    NULL,
    t4."MSCPOOLALLOW",
    t4."OPERATORTYPE",
    t4."OPINDEX",
    t4."OPNAME",
    NULL,
    NULL,
    t4."SGSNPOOLALLOW",
    t4."SPPRTCB",
    NULL,
    NULL
FROM
huawei_mml_gsm."GCNOPERATOR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCNOPERATORREV = ReplaceableObject(
    'huawei_cm_2g."GCNOPERATORREV"',
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
    t1."OPERRSVPARA1",
    t1."OPERRSVPARA2",
    t1."OPERRSVPARA3",
    t1."OPERRSVPARA4",
    t1."OPERRSVPARA5",
    t1."OPINDEX"
FROM
huawei_nbi_gsm."GCNOPERATORREV" t1

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
    t2."OPERRSVPARA1",
    t2."OPERRSVPARA2",
    t2."OPERRSVPARA3",
    t2."OPERRSVPARA4",
    t2."OPERRSVPARA5",
    t2."OPINDEX"
FROM
huawei_gexport_gsm."GCNOPERATORREV_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."OPERRSVPARA1",
    t3."OPERRSVPARA2",
    t3."OPERRSVPARA3",
    t3."OPERRSVPARA4",
    t3."OPERRSVPARA5",
    t3."OPINDEX"
FROM
huawei_gexport_gsm."GCNOPERATORREV_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."OPERRSVPARA1",
    t4."OPERRSVPARA2",
    t4."OPERRSVPARA3",
    t4."OPERRSVPARA4",
    t4."OPERRSVPARA5",
    t4."OPINDEX"
FROM
huawei_mml_gsm."GCNOPERATORREV" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCSCHRCTRL = ReplaceableObject(
    'huawei_cm_2g."GCSCHRCTRL"',
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
    t1."CSADDTINFO",
    t1."CSALGORITHMINFO",
    t1."CSBQTHR",
    t1."CSCLTERMABNORM",
    t1."CSHOINFO",
    t1."CSMOCNCHRINFO",
    t1."CSMRBFCLR",
    t1."CSMRBFHO",
    t1."CSOUTMODE",
    t1."CSOUTRANGE",
    t1."CSRCDSW",
    t1."CSSIGINFO",
    t1."CSTRAFTYPE",
    t1."U2GMROSW",
    t1."CSCHRMR",
    t1."CSVOICEINFO"
FROM
huawei_nbi_gsm."GCSCHRCTRL" t1

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
    t2."CSALGORITHMINFO",
    t2."CSBQTHR",
    NULL,
    t2."CSHOINFO",
    t2."CSMOCNCHRINFO",
    t2."CSMRBFCLR",
    t2."CSMRBFHO",
    t2."CSOUTMODE",
    t2."CSOUTRANGE",
    t2."CSRCDSW",
    t2."CSSIGINFO",
    NULL,
    t2."U2GMROSW",
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCSCHRCTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CSALGORITHMINFO",
    t3."CSBQTHR",
    NULL,
    t3."CSHOINFO",
    t3."CSMOCNCHRINFO",
    t3."CSMRBFCLR",
    t3."CSMRBFHO",
    t3."CSOUTMODE",
    t3."CSOUTRANGE",
    t3."CSRCDSW",
    t3."CSSIGINFO",
    NULL,
    t3."U2GMROSW",
    NULL,
    NULL
FROM
huawei_gexport_gsm."GCSCHRCTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CSALGORITHMINFO",
    t4."CSBQTHR",
    NULL,
    t4."CSHOINFO",
    t4."CSMOCNCHRINFO",
    t4."CSMRBFCLR",
    t4."CSMRBFHO",
    t4."CSOUTMODE",
    t4."CSOUTRANGE",
    t4."CSRCDSW",
    t4."CSSIGINFO",
    NULL,
    t4."U2GMROSW",
    t4."CSCHRMR",
    t4."CSVOICEINFO"
FROM
huawei_mml_gsm."GCSCHRCTRL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCSCHRSCOPE = ReplaceableObject(
    'huawei_cm_2g."GCSCHRSCOPE"',
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
    t1."CHRCOLLECTSWITCH"
FROM
huawei_nbi_gsm."GCSCHRSCOPE" t1

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
    t2."CHRCOLLECTSWITCH"
FROM
huawei_gexport_gsm."GCSCHRSCOPE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CHRCOLLECTSWITCH"
FROM
huawei_gexport_gsm."GCSCHRSCOPE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CHRCOLLECTSWITCH"
FROM
huawei_mml_gsm."GCSCHRSCOPE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GCSFILE = ReplaceableObject(
    'huawei_cm_2g."GCSFILE"',
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
    t1."CMEMODE"
FROM
huawei_nbi_gsm."GCSFILE" t1

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
huawei_gexport_gsm."GCSFILE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."GCSFILE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."GCSFILE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GDSSPARA = ReplaceableObject(
    'huawei_cm_2g."GDSSPARA"',
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
    t1."BTSID",
    t1."DSSBAKDURTM",
    t1."DSSBAKIDLECHTH",
    t1."DSSBAKNORMPCTM",
    t1."DSSBAKSTATTM",
    t1."DSSBAKURGPCTM",
    t1."DSSENABLE",
    t1."DSSHANDSHAKE",
    t1."DSSSHFBTM",
    t1."DSSSHRIDLECHTH",
    t1."DSSSHSTATTM",
    t1."DSSWAITPSTM"
FROM
huawei_nbi_gsm."GDSSPARA" t1

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
    t2."BTSID",
    t2."DSSBAKDURTM",
    t2."DSSBAKIDLECHTH",
    t2."DSSBAKNORMPCTM",
    t2."DSSBAKSTATTM",
    t2."DSSBAKURGPCTM",
    t2."DSSENABLE",
    t2."DSSHANDSHAKE",
    t2."DSSSHFBTM",
    t2."DSSSHRIDLECHTH",
    t2."DSSSHSTATTM",
    t2."DSSWAITPSTM"
FROM
huawei_gexport_gsm."GDSSPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BTSID",
    t3."DSSBAKDURTM",
    t3."DSSBAKIDLECHTH",
    t3."DSSBAKNORMPCTM",
    t3."DSSBAKSTATTM",
    t3."DSSBAKURGPCTM",
    t3."DSSENABLE",
    t3."DSSHANDSHAKE",
    t3."DSSSHFBTM",
    t3."DSSSHRIDLECHTH",
    t3."DSSSHSTATTM",
    t3."DSSWAITPSTM"
FROM
huawei_gexport_gsm."GDSSPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BTSID",
    t4."DSSBAKDURTM",
    t4."DSSBAKIDLECHTH",
    t4."DSSBAKNORMPCTM",
    t4."DSSBAKSTATTM",
    t4."DSSBAKURGPCTM",
    t4."DSSENABLE",
    t4."DSSHANDSHAKE",
    t4."DSSSHFBTM",
    t4."DSSSHRIDLECHTH",
    t4."DSSSHSTATTM",
    t4."DSSWAITPSTM"
FROM
huawei_mml_gsm."GDSSPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GEXT2GCELL = ReplaceableObject(
    'huawei_cm_2g."GEXT2GCELL"',
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
    t1."BCC",
    t1."BCCH",
    t1."BSCIDX",
    t1."CI",
    t1."CMEPRIOR",
    t1."COMSC",
    t1."EXT2GCELLID",
    t1."EXT2GCELLNAME",
    t1."GCNOPGRPINDEX",
    t1."HOOFFSET",
    t1."HOPUNISHVALUE",
    t1."HOTHRES",
    t1."IBCAIIINTERBSCHOINFOSW",
    t1."ISEDGESUPPORT",
    t1."ISGPRSSUPPORT",
    t1."ISNC2SUPPORT",
    t1."LAC",
    t1."LAYER",
    t1."LOADACCTHRES",
    t1."LOADHOENEXT2G",
    t1."MCC",
    t1."MNC",
    t1."MSRXMIN",
    t1."NCC",
    t1."OPNAME",
    t1."RA",
    t1."SDPUNTIME",
    t1."SDPUNVAL",
    t1."TIMEPUNISH"
FROM
huawei_nbi_gsm."GEXT2GCELL" t1

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
    t2."BCC",
    t2."BCCH",
    t2."BSCIDX",
    t2."CI",
    NULL,
    t2."COMSC",
    t2."EXT2GCELLID",
    t2."EXT2GCELLNAME",
    t2."GCNOPGRPINDEX",
    t2."HOOFFSET",
    t2."HOPUNISHVALUE",
    t2."HOTHRES",
    t2."IBCAIIINTERBSCHOINFOSW",
    t2."ISEDGESUPPORT",
    t2."ISGPRSSUPPORT",
    t2."ISNC2SUPPORT",
    t2."LAC",
    t2."LAYER",
    t2."LOADACCTHRES",
    t2."LOADHOENEXT2G",
    t2."MCC",
    t2."MNC",
    t2."MSRXMIN",
    t2."NCC",
    t2."OPNAME",
    t2."RA",
    t2."SDPUNTIME",
    t2."SDPUNVAL",
    t2."TIMEPUNISH"
FROM
huawei_gexport_gsm."GEXT2GCELL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BCC",
    t3."BCCH",
    t3."BSCIDX",
    t3."CI",
    NULL,
    t3."COMSC",
    t3."EXT2GCELLID",
    t3."EXT2GCELLNAME",
    t3."GCNOPGRPINDEX",
    t3."HOOFFSET",
    t3."HOPUNISHVALUE",
    t3."HOTHRES",
    t3."IBCAIIINTERBSCHOINFOSW",
    t3."ISEDGESUPPORT",
    t3."ISGPRSSUPPORT",
    t3."ISNC2SUPPORT",
    t3."LAC",
    t3."LAYER",
    t3."LOADACCTHRES",
    t3."LOADHOENEXT2G",
    t3."MCC",
    t3."MNC",
    t3."MSRXMIN",
    t3."NCC",
    t3."OPNAME",
    t3."RA",
    t3."SDPUNTIME",
    t3."SDPUNVAL",
    t3."TIMEPUNISH"
FROM
huawei_gexport_gsm."GEXT2GCELL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BCC",
    t4."BCCH",
    t4."BSCIDX",
    t4."CI",
    NULL,
    t4."COMSC",
    t4."EXT2GCELLID",
    t4."EXT2GCELLNAME",
    t4."GCNOPGRPINDEX",
    t4."HOOFFSET",
    t4."HOPUNISHVALUE",
    t4."HOTHRES",
    t4."IBCAIIINTERBSCHOINFOSW",
    t4."ISEDGESUPPORT",
    t4."ISGPRSSUPPORT",
    t4."ISNC2SUPPORT",
    t4."LAC",
    t4."LAYER",
    t4."LOADACCTHRES",
    t4."LOADHOENEXT2G",
    t4."MCC",
    t4."MNC",
    t4."MSRXMIN",
    t4."NCC",
    t4."OPNAME",
    t4."RA",
    t4."SDPUNTIME",
    t4."SDPUNVAL",
    t4."TIMEPUNISH"
FROM
huawei_mml_gsm."GEXT2GCELL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GEXT3GCELL = ReplaceableObject(
    'huawei_cm_2g."GEXT3GCELL"',
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
    t1."CELLLAYER",
    t1."CI",
    t1."DF",
    t1."DIVERSITY",
    t1."ECNOTHRES",
    t1."EXT3GCELLID",
    t1."EXT3GCELLNAME",
    t1."FDDECQUALTHRSH",
    t1."FDDRSCPQUALTHRSH",
    t1."GCNOPGRPINDEX",
    t1."LAC",
    t1."LOADACCTHRES",
    t1."LOADHOENEXT3G",
    t1."MCC",
    t1."MINECNOTHRES",
    t1."MINRSCPTHRES",
    t1."MNC",
    t1."OPNAME",
    t1."RA",
    t1."RNCID",
    t1."RNCINDEX",
    t1."RSCPTHRES",
    t1."SCRAMBLE",
    t1."UTRANCELLTYPE"
FROM
huawei_nbi_gsm."GEXT3GCELL" t1

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
    t2."CELLLAYER",
    t2."CI",
    t2."DF",
    t2."DIVERSITY",
    t2."ECNOTHRES",
    t2."EXT3GCELLID",
    t2."EXT3GCELLNAME",
    t2."FDDECQUALTHRSH",
    t2."FDDRSCPQUALTHRSH",
    t2."GCNOPGRPINDEX",
    t2."LAC",
    t2."LOADACCTHRES",
    t2."LOADHOENEXT3G",
    t2."MCC",
    t2."MINECNOTHRES",
    t2."MINRSCPTHRES",
    t2."MNC",
    t2."OPNAME",
    t2."RA",
    t2."RNCID",
    t2."RNCINDEX",
    t2."RSCPTHRES",
    t2."SCRAMBLE",
    t2."UTRANCELLTYPE"
FROM
huawei_gexport_gsm."GEXT3GCELL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CELLLAYER",
    t3."CI",
    t3."DF",
    t3."DIVERSITY",
    t3."ECNOTHRES",
    t3."EXT3GCELLID",
    t3."EXT3GCELLNAME",
    t3."FDDECQUALTHRSH",
    t3."FDDRSCPQUALTHRSH",
    t3."GCNOPGRPINDEX",
    t3."LAC",
    t3."LOADACCTHRES",
    t3."LOADHOENEXT3G",
    t3."MCC",
    t3."MINECNOTHRES",
    t3."MINRSCPTHRES",
    t3."MNC",
    t3."OPNAME",
    t3."RA",
    t3."RNCID",
    t3."RNCINDEX",
    t3."RSCPTHRES",
    t3."SCRAMBLE",
    t3."UTRANCELLTYPE"
FROM
huawei_gexport_gsm."GEXT3GCELL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CELLLAYER",
    t4."CI",
    t4."DF",
    t4."DIVERSITY",
    t4."ECNOTHRES",
    t4."EXT3GCELLID",
    t4."EXT3GCELLNAME",
    t4."FDDECQUALTHRSH",
    t4."FDDRSCPQUALTHRSH",
    t4."GCNOPGRPINDEX",
    t4."LAC",
    t4."LOADACCTHRES",
    t4."LOADHOENEXT3G",
    t4."MCC",
    t4."MINECNOTHRES",
    t4."MINRSCPTHRES",
    t4."MNC",
    t4."OPNAME",
    t4."RA",
    t4."RNCID",
    t4."RNCINDEX",
    t4."RSCPTHRES",
    t4."SCRAMBLE",
    t4."UTRANCELLTYPE"
FROM
huawei_mml_gsm."GEXT3GCELL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GEXTLTECELL = ReplaceableObject(
    'huawei_cm_2g."GEXTLTECELL"',
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
    t1."CI",
    t1."ENODEBTYPE",
    t1."EUTRANTYPE",
    t1."EXTLTECELLID",
    t1."EXTLTECELLNAME",
    t1."FREQ",
    t1."GCNOPGRPINDEX",
    t1."MCC",
    t1."MNC",
    t1."OPNAME",
    t1."PCID",
    t1."TAC"
FROM
huawei_nbi_gsm."GEXTLTECELL" t1

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
    t2."CI",
    t2."ENODEBTYPE",
    t2."EUTRANTYPE",
    t2."EXTLTECELLID",
    t2."EXTLTECELLNAME",
    t2."FREQ",
    t2."GCNOPGRPINDEX",
    t2."MCC",
    t2."MNC",
    t2."OPNAME",
    t2."PCID",
    t2."TAC"
FROM
huawei_gexport_gsm."GEXTLTECELL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CI",
    t3."ENODEBTYPE",
    t3."EUTRANTYPE",
    t3."EXTLTECELLID",
    t3."EXTLTECELLNAME",
    t3."FREQ",
    t3."GCNOPGRPINDEX",
    t3."MCC",
    t3."MNC",
    t3."OPNAME",
    t3."PCID",
    t3."TAC"
FROM
huawei_gexport_gsm."GEXTLTECELL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

GFORCESWITCH = ReplaceableObject(
    'huawei_cm_2g."GFORCESWITCH"',
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
    t1."EVENTCSCHRSW",
    t1."EVENTMRSW",
    t1."EVENTPSCHRSW"
FROM
huawei_nbi_gsm."GFORCESWITCH" t1

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
    t2."EVENTCSCHRSW",
    t2."EVENTMRSW",
    t2."EVENTPSCHRSW"
FROM
huawei_gexport_gsm."GFORCESWITCH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."EVENTCSCHRSW",
    t3."EVENTMRSW",
    t3."EVENTPSCHRSW"
FROM
huawei_gexport_gsm."GFORCESWITCH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."EVENTCSCHRSW",
    t4."EVENTMRSW",
    t4."EVENTPSCHRSW"
FROM
huawei_mml_gsm."GFORCESWITCH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GHOSTSTATUS = ReplaceableObject(
    'huawei_cm_2g."GHOSTSTATUS"',
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
    t1."HOSTSTATUS",
    t1."HOSTTYPE"
FROM
huawei_nbi_gsm."GHOSTSTATUS" t1

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
    t2."HOSTSTATUS",
    t2."HOSTTYPE"
FROM
huawei_gexport_gsm."GHOSTSTATUS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."HOSTSTATUS",
    t3."HOSTTYPE"
FROM
huawei_gexport_gsm."GHOSTSTATUS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

G_IPPATH = ReplaceableObject(
    'huawei_cm_2g."G_IPPATH"',
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
    t1."ABISLNKBKFLAG",
    t1."ANI",
    t1."CNMNGMODE",
    t1."ISEGBTS",
    t1."ITFT",
    t1."PATHCHK",
    t1."PATHID",
    t1."PATHT",
    t1."REMARK",
    t1."RXBW",
    t1."TRMLOADTHINDEX",
    t1."TXBW",
    t1."VLANFLAG",
    t1."CHECKCOUNT",
    t1."CHECKT",
    t1."ICMPPKGLEN",
    t1."PERIOD",
    t1."CARRYFLAG",
    t1."IPADDR",
    t1."PEERIPADDR",
    t1."PEERMASK"
FROM
huawei_nbi_gsm."G_IPPATH" t1

"""
)

GKPIALMTHD = ReplaceableObject(
    'huawei_cm_2g."GKPIALMTHD"',
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
    t1."ASSMINNUM",
    t1."ASSSUCCRATIO",
    t1."IMMASSMINNUM",
    t1."IMMASSSUCCRATIO",
    t1."KPIALARMCHKTIMES",
    t1."KPIALARMSWITCH",
    t1."SVRCONNMINNUM",
    t1."SVRCONNSUCCRATIO"
FROM
huawei_nbi_gsm."GKPIALMTHD" t1

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
    t2."ASSMINNUM",
    t2."ASSSUCCRATIO",
    t2."IMMASSMINNUM",
    t2."IMMASSSUCCRATIO",
    t2."KPIALARMCHKTIMES",
    t2."KPIALARMSWITCH",
    t2."SVRCONNMINNUM",
    t2."SVRCONNSUCCRATIO"
FROM
huawei_gexport_gsm."GKPIALMTHD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ASSMINNUM",
    t3."ASSSUCCRATIO",
    t3."IMMASSMINNUM",
    t3."IMMASSSUCCRATIO",
    t3."KPIALARMCHKTIMES",
    t3."KPIALARMSWITCH",
    t3."SVRCONNMINNUM",
    t3."SVRCONNSUCCRATIO"
FROM
huawei_gexport_gsm."GKPIALMTHD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ASSMINNUM",
    t4."ASSSUCCRATIO",
    t4."IMMASSMINNUM",
    t4."IMMASSSUCCRATIO",
    t4."KPIALARMCHKTIMES",
    t4."KPIALARMSWITCH",
    t4."SVRCONNMINNUM",
    t4."SVRCONNSUCCRATIO"
FROM
huawei_mml_gsm."GKPIALMTHD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GLOBALROUTESW = ReplaceableObject(
    'huawei_cm_2g."GLOBALROUTESW"',
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
    t1."GLOBALROUTESW"
FROM
huawei_nbi_gsm."GLOBALROUTESW" t1

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
    t2."GLOBALROUTESW"
FROM
huawei_gexport_gsm."GLOBALROUTESW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."GLOBALROUTESW"
FROM
huawei_gexport_gsm."GLOBALROUTESW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GLOBALROUTESW"
FROM
huawei_mml_gsm."GLOBALROUTESW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GLTENCELL = ReplaceableObject(
    'huawei_cm_2g."GLTENCELL"',
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
    t1."NBRLTENCELLID",
    t1."NCELLPRI",
    t1."SPTBLINDHO",
    t1."SPTRAPIDSEL",
    t1."SPTRESEL",
    t1."SRCLTENCELLID"
FROM
huawei_nbi_gsm."GLTENCELL" t1

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
    t2."NBRLTENCELLID",
    t2."NCELLPRI",
    t2."SPTBLINDHO",
    t2."SPTRAPIDSEL",
    t2."SPTRESEL",
    t2."SRCLTENCELLID"
FROM
huawei_gexport_gsm."GLTENCELL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."NBRLTENCELLID",
    t3."NCELLPRI",
    t3."SPTBLINDHO",
    t3."SPTRAPIDSEL",
    t3."SPTRESEL",
    t3."SRCLTENCELLID"
FROM
huawei_gexport_gsm."GLTENCELL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

GMRCTRL = ReplaceableObject(
    'huawei_cm_2g."GMRCTRL"',
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
    t1."CALLIDTYPE",
    t1."MRLOGNCELLTYPE",
    t1."MRSWITCH",
    t1."PREMRSAMPLE",
    t1."RAWMRSAMPLE"
FROM
huawei_nbi_gsm."GMRCTRL" t1

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
    t2."CALLIDTYPE",
    t2."MRLOGNCELLTYPE",
    t2."MRSWITCH",
    t2."PREMRSAMPLE",
    t2."RAWMRSAMPLE"
FROM
huawei_gexport_gsm."GMRCTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CALLIDTYPE",
    t3."MRLOGNCELLTYPE",
    t3."MRSWITCH",
    t3."PREMRSAMPLE",
    t3."RAWMRSAMPLE"
FROM
huawei_gexport_gsm."GMRCTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CALLIDTYPE",
    t4."MRLOGNCELLTYPE",
    t4."MRSWITCH",
    t4."PREMRSAMPLE",
    t4."RAWMRSAMPLE"
FROM
huawei_mml_gsm."GMRCTRL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GMRSCOPE = ReplaceableObject(
    'huawei_cm_2g."GMRSCOPE"',
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
    t1."MRSCOPESWITCH"
FROM
huawei_nbi_gsm."GMRSCOPE" t1

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
    t2."MRSCOPESWITCH"
FROM
huawei_gexport_gsm."GMRSCOPE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."MRSCOPESWITCH"
FROM
huawei_gexport_gsm."GMRSCOPE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."MRSCOPESWITCH"
FROM
huawei_mml_gsm."GMRSCOPE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GNODEREDCFGCTRL = ReplaceableObject(
    'huawei_cm_2g."GNODEREDCFGCTRL"',
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
    t1."SYNCDATACFGMODE"
FROM
huawei_nbi_gsm."GNODEREDCFGCTRL" t1

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
    t2."SYNCDATACFGMODE"
FROM
huawei_gexport_gsm."GNODEREDCFGCTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SYNCDATACFGMODE"
FROM
huawei_gexport_gsm."GNODEREDCFGCTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SYNCDATACFGMODE"
FROM
huawei_mml_gsm."GNODEREDCFGCTRL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GNODEREDUNDANCY = ReplaceableObject(
    'huawei_cm_2g."GNODEREDUNDANCY"',
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
    t1."REDUNDANCYMODE"
FROM
huawei_nbi_gsm."GNODEREDUNDANCY" t1

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
    t2."REDUNDANCYMODE"
FROM
huawei_gexport_gsm."GNODEREDUNDANCY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."REDUNDANCYMODE"
FROM
huawei_gexport_gsm."GNODEREDUNDANCY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."REDUNDANCYMODE"
FROM
huawei_mml_gsm."GNODEREDUNDANCY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GPSCHRCTRL = ReplaceableObject(
    'huawei_cm_2g."GPSCHRCTRL"',
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
    t1."DIFFSERVTHR",
    t1."PSCHRABIS",
    t1."PSCHRABNORMAL",
    t1."PSCHREVENT",
    t1."PSCHRGB",
    t1."PSCHRIMEI",
    t1."PSCHRINNINFO",
    t1."PSCHRINNMSG",
    t1."PSCHRMR",
    t1."PSCHRMRNUM",
    t1."PSCHRRESELECT",
    t1."PSCHRSERVICETYPE",
    t1."PSCHRTRAFFIC",
    t1."PSCHRUM",
    t1."PSCHRWLAN",
    t1."PSMOCNCHRINFO",
    t1."PSOUTMODE",
    t1."PSRCDSW",
    t1."SPEEDPDURCVTHR",
    t1."SPEEDPDUSNDTHR",
    t1."TDSERVNORSPTHR",
    t1."TDSERVPDUINTERVALTHR",
    t1."TDSERVPDURCVTHR",
    t1."TDSERVPDUSNDTHR"
FROM
huawei_nbi_gsm."GPSCHRCTRL" t1

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
    t2."DIFFSERVTHR",
    t2."PSCHRABIS",
    t2."PSCHRABNORMAL",
    t2."PSCHREVENT",
    t2."PSCHRGB",
    t2."PSCHRIMEI",
    t2."PSCHRINNINFO",
    t2."PSCHRINNMSG",
    t2."PSCHRMR",
    t2."PSCHRMRNUM",
    t2."PSCHRRESELECT",
    t2."PSCHRSERVICETYPE",
    t2."PSCHRTRAFFIC",
    t2."PSCHRUM",
    t2."PSCHRWLAN",
    t2."PSMOCNCHRINFO",
    t2."PSOUTMODE",
    t2."PSRCDSW",
    t2."SPEEDPDURCVTHR",
    t2."SPEEDPDUSNDTHR",
    t2."TDSERVNORSPTHR",
    t2."TDSERVPDUINTERVALTHR",
    t2."TDSERVPDURCVTHR",
    t2."TDSERVPDUSNDTHR"
FROM
huawei_gexport_gsm."GPSCHRCTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DIFFSERVTHR",
    t3."PSCHRABIS",
    t3."PSCHRABNORMAL",
    t3."PSCHREVENT",
    t3."PSCHRGB",
    t3."PSCHRIMEI",
    t3."PSCHRINNINFO",
    t3."PSCHRINNMSG",
    t3."PSCHRMR",
    t3."PSCHRMRNUM",
    t3."PSCHRRESELECT",
    t3."PSCHRSERVICETYPE",
    t3."PSCHRTRAFFIC",
    t3."PSCHRUM",
    t3."PSCHRWLAN",
    t3."PSMOCNCHRINFO",
    t3."PSOUTMODE",
    t3."PSRCDSW",
    t3."SPEEDPDURCVTHR",
    t3."SPEEDPDUSNDTHR",
    t3."TDSERVNORSPTHR",
    t3."TDSERVPDUINTERVALTHR",
    t3."TDSERVPDURCVTHR",
    t3."TDSERVPDUSNDTHR"
FROM
huawei_gexport_gsm."GPSCHRCTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DIFFSERVTHR",
    t4."PSCHRABIS",
    t4."PSCHRABNORMAL",
    t4."PSCHREVENT",
    t4."PSCHRGB",
    t4."PSCHRIMEI",
    t4."PSCHRINNINFO",
    t4."PSCHRINNMSG",
    t4."PSCHRMR",
    t4."PSCHRMRNUM",
    t4."PSCHRRESELECT",
    t4."PSCHRSERVICETYPE",
    t4."PSCHRTRAFFIC",
    t4."PSCHRUM",
    t4."PSCHRWLAN",
    t4."PSMOCNCHRINFO",
    t4."PSOUTMODE",
    t4."PSRCDSW",
    t4."SPEEDPDURCVTHR",
    t4."SPEEDPDUSNDTHR",
    t4."TDSERVNORSPTHR",
    t4."TDSERVPDUINTERVALTHR",
    t4."TDSERVPDURCVTHR",
    t4."TDSERVPDUSNDTHR"
FROM
huawei_mml_gsm."GPSCHRCTRL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GPSCHRSCOPE = ReplaceableObject(
    'huawei_cm_2g."GPSCHRSCOPE"',
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
    t1."CHRCOLLECTSWITCH"
FROM
huawei_nbi_gsm."GPSCHRSCOPE" t1

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
    t2."CHRCOLLECTSWITCH"
FROM
huawei_gexport_gsm."GPSCHRSCOPE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CHRCOLLECTSWITCH"
FROM
huawei_gexport_gsm."GPSCHRSCOPE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CHRCOLLECTSWITCH"
FROM
huawei_mml_gsm."GPSCHRSCOPE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GPSKPIALMTHD = ReplaceableObject(
    'huawei_cm_2g."GPSKPIALMTHD"',
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
    t1."PSACCESSMINNUM",
    t1."PSACCESSSUCCRATIO",
    t1."PSBRDKPIALMSWITCH",
    t1."PSKPIALARMCHKTIMES",
    t1."PSKPIALARMSWITCH"
FROM
huawei_nbi_gsm."GPSKPIALMTHD" t1

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
    t2."PSACCESSMINNUM",
    t2."PSACCESSSUCCRATIO",
    t2."PSBRDKPIALMSWITCH",
    t2."PSKPIALARMCHKTIMES",
    t2."PSKPIALARMSWITCH"
FROM
huawei_gexport_gsm."GPSKPIALMTHD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PSACCESSMINNUM",
    t3."PSACCESSSUCCRATIO",
    t3."PSBRDKPIALMSWITCH",
    t3."PSKPIALARMCHKTIMES",
    t3."PSKPIALARMSWITCH"
FROM
huawei_gexport_gsm."GPSKPIALMTHD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PSACCESSMINNUM",
    t4."PSACCESSSUCCRATIO",
    t4."PSBRDKPIALMSWITCH",
    t4."PSKPIALARMCHKTIMES",
    t4."PSKPIALARMSWITCH"
FROM
huawei_mml_gsm."GPSKPIALMTHD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GREDGRPHOSTPOLICY = ReplaceableObject(
    'huawei_cm_2g."GREDGRPHOSTPOLICY"',
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
    t1."CNFAULTDELAY",
    t1."CNSTATEPOLICYFORGROUP",
    t1."MSTSERVACTDELAY",
    t1."REHOSTDELAYTIME",
    t1."REHOSTTYPE",
    t1."SLVSERVACTDELAY"
FROM
huawei_nbi_gsm."GREDGRPHOSTPOLICY" t1

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
    t2."CNFAULTDELAY",
    t2."CNSTATEPOLICYFORGROUP",
    t2."MSTSERVACTDELAY",
    t2."REHOSTDELAYTIME",
    t2."REHOSTTYPE",
    t2."SLVSERVACTDELAY"
FROM
huawei_gexport_gsm."GREDGRPHOSTPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CNFAULTDELAY",
    t3."CNSTATEPOLICYFORGROUP",
    t3."MSTSERVACTDELAY",
    t3."REHOSTDELAYTIME",
    t3."REHOSTTYPE",
    t3."SLVSERVACTDELAY"
FROM
huawei_gexport_gsm."GREDGRPHOSTPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CNFAULTDELAY",
    t4."CNSTATEPOLICYFORGROUP",
    t4."MSTSERVACTDELAY",
    t4."REHOSTDELAYTIME",
    t4."REHOSTTYPE",
    t4."SLVSERVACTDELAY"
FROM
huawei_mml_gsm."GREDGRPHOSTPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GRSVPARA = ReplaceableObject(
    'huawei_cm_2g."GRSVPARA"',
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
    t1."BSCCSDPARA1",
    t1."BSCCSDPARA2",
    t1."BSCCSDPARA3",
    t1."BSCCSDPARA4",
    t1."BSCCSDPARA5",
    t1."BSCCSDPARA6",
    t1."BSCCSDPARA7",
    t1."BSCCSDPARA8",
    t1."BSCCSSWRSV0",
    t1."BSCCSSWRSV1",
    t1."BSCCSSWRSV2",
    t1."BSCPSDPARA0",
    t1."BSCPSDPARA1",
    t1."BSCPSDPARA10",
    t1."BSCPSSWRSV0",
    t1."BSCPSSWRSV1"
FROM
huawei_nbi_gsm."GRSVPARA" t1

"""
)

GTRX = ReplaceableObject(
    'huawei_cm_2g."GTRX"',
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
    t1."ADMSTAT",
    t1."CELLID",
    t1."FREQ",
    t1."GTRXGROUPID",
    t1."ISMAINBCCH",
    t1."ISTMPTRX",
    t1."TRXID",
    t1."TRXNAME",
    t1."TRXNO"
FROM
huawei_nbi_gsm."GTRX" t1

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
    t2."ADMSTAT",
    t2."CELLID",
    t2."FREQ",
    t2."GTRXGROUPID",
    t2."ISMAINBCCH",
    t2."ISTMPTRX",
    t2."TRXID",
    t2."TRXNAME",
    t2."TRXNO"
FROM
huawei_gexport_gsm."GTRX_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADMSTAT",
    t3."CELLID",
    t3."FREQ",
    t3."GTRXGROUPID",
    t3."ISMAINBCCH",
    t3."ISTMPTRX",
    t3."TRXID",
    t3."TRXNAME",
    t3."TRXNO"
FROM
huawei_gexport_gsm."GTRX_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CELLID",
    t4."FREQ",
    t4."GTRXGROUPID",
    t4."ISMAINBCCH",
    t4."ISTMPTRX",
    t4."TRXID",
    t4."TRXNAME",
    t4."TRXNO"
FROM
huawei_mml_gsm."GTRX" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXBASE = ReplaceableObject(
    'huawei_cm_2g."GTRXBASE"',
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
    t1."MAXPDCHNUM",
    t1."MAXTSOCP",
    t1."TRXID"
FROM
huawei_nbi_gsm."GTRXBASE" t1

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
    t2."MAXPDCHNUM",
    t2."MAXTSOCP",
    t2."TRXID"
FROM
huawei_gexport_gsm."GTRXBASE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."MAXPDCHNUM",
    t3."MAXTSOCP",
    t3."TRXID"
FROM
huawei_gexport_gsm."GTRXBASE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

GTRXCHAN = ReplaceableObject(
    'huawei_cm_2g."GTRXCHAN"',
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
    t1."ADMSTAT",
    t1."CHANRSV",
    t1."CHNO",
    t1."CHTYPE",
    t1."GPRSCHPRI",
    t1."TRXID",
    t1."TSPRIORITY"
FROM
huawei_nbi_gsm."GTRXCHAN" t1

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
    t2."ADMSTAT",
    t2."CHANRSV",
    t2."CHNO",
    t2."CHTYPE",
    t2."GPRSCHPRI",
    t2."TRXID",
    t2."TSPRIORITY"
FROM
huawei_gexport_gsm."GTRXCHAN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ADMSTAT",
    t3."CHANRSV",
    t3."CHNO",
    t3."CHTYPE",
    t3."GPRSCHPRI",
    t3."TRXID",
    t3."TSPRIORITY"
FROM
huawei_gexport_gsm."GTRXCHAN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CHANRSV",
    t4."CHNO",
    t4."CHTYPE",
    t4."GPRSCHPRI",
    t4."TRXID",
    t4."TSPRIORITY"
FROM
huawei_mml_gsm."GTRXCHAN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXCHANHOP = ReplaceableObject(
    'huawei_cm_2g."GTRXCHANHOP"',
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
    t1."CHNO",
    t1."TRXDSSHOPINDEX",
    t1."TRXDSSMAIO",
    t1."TRXHOPINDEX",
    t1."TRXID",
    t1."TRXMAIO"
FROM
huawei_nbi_gsm."GTRXCHANHOP" t1

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
    t2."CHNO",
    t2."TRXDSSHOPINDEX",
    t2."TRXDSSMAIO",
    t2."TRXHOPINDEX",
    t2."TRXID",
    t2."TRXMAIO"
FROM
huawei_gexport_gsm."GTRXCHANHOP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CHNO",
    t3."TRXDSSHOPINDEX",
    t3."TRXDSSMAIO",
    t3."TRXHOPINDEX",
    t3."TRXID",
    t3."TRXMAIO"
FROM
huawei_gexport_gsm."GTRXCHANHOP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CHNO",
    t4."TRXDSSHOPINDEX",
    t4."TRXDSSMAIO",
    t4."TRXHOPINDEX",
    t4."TRXID",
    t4."TRXMAIO"
FROM
huawei_mml_gsm."GTRXCHANHOP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXDEV = ReplaceableObject(
    'huawei_cm_2g."GTRXDEV"',
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
    t1."CPS",
    t1."DSSTRXOFFLINE",
    t1."FREQREUSEMODE",
    t1."IBCATGTCIRMAIOFIXED",
    t1."INHOPWROVERLOADTHRESHOLD",
    t1."OPTL",
    t1."OUTHOPWROVERLOADTHRESHOLD",
    t1."PAOPTILEVEL",
    t1."PL16QAM",
    t1."PL32QAM",
    t1."PL8PSK",
    t1."POWL",
    t1."POWT",
    t1."POWTUNIT",
    t1."PWRSPNR",
    t1."RCVMD",
    t1."SDFLAG",
    t1."SNDMD",
    t1."TCHAJFLAG",
    t1."TRXID",
    t1."TRXLOGICLOCKSW",
    t1."TSPWRRESERVE"
FROM
huawei_nbi_gsm."GTRXDEV" t1

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
    t2."CPS",
    t2."DSSTRXOFFLINE",
    t2."FREQREUSEMODE",
    t2."IBCATGTCIRMAIOFIXED",
    t2."INHOPWROVERLOADTHRESHOLD",
    t2."OPTL",
    t2."OUTHOPWROVERLOADTHRESHOLD",
    t2."PAOPTILEVEL",
    t2."PL16QAM",
    t2."PL32QAM",
    t2."PL8PSK",
    t2."POWL",
    t2."POWT",
    t2."POWTUNIT",
    t2."PWRSPNR",
    t2."RCVMD",
    t2."SDFLAG",
    t2."SNDMD",
    t2."TCHAJFLAG",
    t2."TRXID",
    t2."TRXLOGICLOCKSW",
    t2."TSPWRRESERVE"
FROM
huawei_gexport_gsm."GTRXDEV_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CPS",
    t3."DSSTRXOFFLINE",
    t3."FREQREUSEMODE",
    t3."IBCATGTCIRMAIOFIXED",
    t3."INHOPWROVERLOADTHRESHOLD",
    t3."OPTL",
    t3."OUTHOPWROVERLOADTHRESHOLD",
    t3."PAOPTILEVEL",
    t3."PL16QAM",
    t3."PL32QAM",
    t3."PL8PSK",
    t3."POWL",
    t3."POWT",
    t3."POWTUNIT",
    t3."PWRSPNR",
    t3."RCVMD",
    t3."SDFLAG",
    t3."SNDMD",
    t3."TCHAJFLAG",
    t3."TRXID",
    t3."TRXLOGICLOCKSW",
    t3."TSPWRRESERVE"
FROM
huawei_gexport_gsm."GTRXDEV_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CPS",
    t4."DSSTRXOFFLINE",
    t4."FREQREUSEMODE",
    t4."IBCATGTCIRMAIOFIXED",
    t4."INHOPWROVERLOADTHRESHOLD",
    t4."OPTL",
    t4."OUTHOPWROVERLOADTHRESHOLD",
    t4."PAOPTILEVEL",
    t4."PL16QAM",
    t4."PL32QAM",
    t4."PL8PSK",
    t4."POWL",
    t4."POWT",
    t4."POWTUNIT",
    t4."PWRSPNR",
    t4."RCVMD",
    t4."SDFLAG",
    t4."SNDMD",
    t4."TCHAJFLAG",
    t4."TRXID",
    t4."TRXLOGICLOCKSW",
    t4."TSPWRRESERVE"
FROM
huawei_mml_gsm."GTRXDEV" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXFC = ReplaceableObject(
    'huawei_cm_2g."GTRXFC"',
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
    t1."CENDTHD",
    t1."CSTARTTHD",
    t1."FCETHD",
    t1."FCSTHD",
    t1."TRXID"
FROM
huawei_nbi_gsm."GTRXFC" t1

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
    t2."CENDTHD",
    t2."CSTARTTHD",
    t2."FCETHD",
    t2."FCSTHD",
    t2."TRXID"
FROM
huawei_gexport_gsm."GTRXFC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CENDTHD",
    t3."CSTARTTHD",
    t3."FCETHD",
    t3."FCSTHD",
    t3."TRXID"
FROM
huawei_gexport_gsm."GTRXFC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CENDTHD",
    t4."CSTARTTHD",
    t4."FCETHD",
    t4."FCSTHD",
    t4."TRXID"
FROM
huawei_mml_gsm."GTRXFC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXHOP = ReplaceableObject(
    'huawei_cm_2g."GTRXHOP"',
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
    t1."HOPTYPE",
    t1."TRXID"
FROM
huawei_nbi_gsm."GTRXHOP" t1

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
    t2."HOPTYPE",
    t2."TRXID"
FROM
huawei_gexport_gsm."GTRXHOP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."HOPTYPE",
    t3."TRXID"
FROM
huawei_gexport_gsm."GTRXHOP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."HOPTYPE",
    t4."TRXID"
FROM
huawei_mml_gsm."GTRXHOP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXIUO = ReplaceableObject(
    'huawei_cm_2g."GTRXIUO"',
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
    t1."IUO",
    t1."TRXID"
FROM
huawei_nbi_gsm."GTRXIUO" t1

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
    t2."IUO",
    t2."TRXID"
FROM
huawei_gexport_gsm."GTRXIUO_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IUO",
    t3."TRXID"
FROM
huawei_gexport_gsm."GTRXIUO_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IUO",
    t4."TRXID"
FROM
huawei_mml_gsm."GTRXIUO" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXRLALM = ReplaceableObject(
    'huawei_cm_2g."GTRXRLALM"',
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
    t1."TRXID",
    t1."WLNKALMFLAG"
FROM
huawei_nbi_gsm."GTRXRLALM" t1

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
    t2."TRXID",
    t2."WLNKALMFLAG"
FROM
huawei_gexport_gsm."GTRXRLALM_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."TRXID",
    t3."WLNKALMFLAG"
FROM
huawei_gexport_gsm."GTRXRLALM_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TRXID",
    t4."WLNKALMFLAG"
FROM
huawei_mml_gsm."GTRXRLALM" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

GTRXRSVPARA = ReplaceableObject(
    'huawei_cm_2g."GTRXRSVPARA"',
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
    t1."GTRXRSVPARA5",
    t1."GTRXRSVSW",
    t1."TRXID"
FROM
huawei_nbi_gsm."GTRXRSVPARA" t1

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
    t2."GTRXRSVPARA5",
    NULL,
    t2."TRXID"
FROM
huawei_gexport_gsm."GTRXRSVPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."GTRXRSVPARA5",
    NULL,
    t3."TRXID"
FROM
huawei_gexport_gsm."GTRXRSVPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GTRXRSVPARA5",
    NULL,
    t4."TRXID"
FROM
huawei_mml_gsm."GTRXRSVPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

HOSTLOGSPD = ReplaceableObject(
    'huawei_cm_2g."HOSTLOGSPD"',
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
    t1."LOGSPD"
FROM
huawei_nbi_gsm."HOSTLOGSPD" t1

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
    t2."LOGSPD"
FROM
huawei_gexport_gsm."HOSTLOGSPD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LOGSPD"
FROM
huawei_gexport_gsm."HOSTLOGSPD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LOGSPD"
FROM
huawei_mml_gsm."HOSTLOGSPD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

IDRQTEST = ReplaceableObject(
    'huawei_cm_2g."IDRQTEST"',
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
    t1."ENCRYID",
    t1."IDRQDURATION",
    t1."IDRQSEQSW",
    t1."IDRQSWITCH",
    t1."LUIDRQALLOW",
    t1."SENDMMNULLPERMIT",
    t1."USERIDTRACEMODE",
    t1."USERIDTRACETYPE"
FROM
huawei_nbi_gsm."IDRQTEST" t1

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
    t2."ENCRYID",
    NULL,
    t2."IDRQSEQSW",
    t2."IDRQSWITCH",
    t2."LUIDRQALLOW",
    t2."SENDMMNULLPERMIT",
    t2."USERIDTRACEMODE",
    t2."USERIDTRACETYPE"
FROM
huawei_gexport_gsm."IDRQTEST_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ENCRYID",
    NULL,
    t3."IDRQSEQSW",
    t3."IDRQSWITCH",
    t3."LUIDRQALLOW",
    t3."SENDMMNULLPERMIT",
    t3."USERIDTRACEMODE",
    t3."USERIDTRACETYPE"
FROM
huawei_gexport_gsm."IDRQTEST_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ENCRYID",
    t4."IDRQDURATION",
    t4."IDRQSEQSW",
    t4."IDRQSWITCH",
    t4."LUIDRQALLOW",
    t4."SENDMMNULLPERMIT",
    t4."USERIDTRACEMODE",
    t4."USERIDTRACETYPE"
FROM
huawei_mml_gsm."IDRQTEST" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

INFBRDRESCFG = ReplaceableObject(
    'huawei_cm_2g."INFBRDRESCFG"',
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
    t1."LOGSW",
    t1."RESSW",
    t1."RESTIMESPERDAY",
    t1."RESTYPE",
    t1."STATISTICUOIPLOOPFAULTTIME",
    t1."BRDFAULTBCRATE",
    t1."CONTINUOUSFAULTTIMES",
    t1."MERELOADCONTINUOUSFAULTTIMES",
    t1."BRDFAULTNSRATE",
    t1."NSRESSW"
FROM
huawei_nbi_gsm."INFBRDRESCFG" t1

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
    t2."LOGSW",
    t2."RESSW",
    t2."RESTIMESPERDAY",
    t2."RESTYPE",
    t2."STATISTICUOIPLOOPFAULTTIME",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."INFBRDRESCFG_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LOGSW",
    t3."RESSW",
    t3."RESTIMESPERDAY",
    t3."RESTYPE",
    t3."STATISTICUOIPLOOPFAULTTIME",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."INFBRDRESCFG_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LOGSW",
    t4."RESSW",
    t4."RESTIMESPERDAY",
    t4."RESTYPE",
    t4."STATISTICUOIPLOOPFAULTTIME",
    t4."BRDFAULTBCRATE",
    t4."CONTINUOUSFAULTTIMES",
    t4."MERELOADCONTINUOUSFAULTTIMES",
    t4."BRDFAULTNSRATE",
    t4."NSRESSW"
FROM
huawei_mml_gsm."INFBRDRESCFG" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

INTBRDPARA = ReplaceableObject(
    'huawei_cm_2g."INTBRDPARA"',
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
    t1."BRDCHIPSELFCURESW",
    t1."BT",
    t1."DHCPDSCP",
    t1."FCALMRTHD",
    t1."FCALMSW",
    t1."FCALMTHD",
    t1."MSPCHECKSW",
    t1."OPTBRDK1K2FCSW",
    t1."OPTCONNERRALMSW",
    t1."PPPBOARDCARSW",
    t1."SN",
    t1."SRN",
    t1."ARPEXPIRETIMEOPTIMIZESW",
    t1."ARPPKTSENDMODE",
    t1."ARPVLANPRI",
    t1."IPPROTOCOLCHECKSW",
    t1."OVERSIZEPKTSW",
    t1."PORTFCSWITCH",
    t1."RECPORTSWITCHOVERSW",
    t1."SIGPACKCTRLSW"
FROM
huawei_nbi_gsm."INTBRDPARA" t1

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
    t2."BT",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."OPTBRDK1K2FCSW",
    t2."OPTCONNERRALMSW",
    NULL,
    t2."SN",
    t2."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."INTBRDPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BT",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."OPTBRDK1K2FCSW",
    t3."OPTCONNERRALMSW",
    NULL,
    t3."SN",
    t3."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."INTBRDPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BRDCHIPSELFCURESW",
    t4."BT",
    t4."DHCPDSCP",
    t4."FCALMRTHD",
    t4."FCALMSW",
    t4."FCALMTHD",
    NULL,
    t4."OPTBRDK1K2FCSW",
    t4."OPTCONNERRALMSW",
    NULL,
    t4."SN",
    t4."SRN",
    t4."ARPEXPIRETIMEOPTIMIZESW",
    t4."ARPPKTSENDMODE",
    t4."ARPVLANPRI",
    t4."IPPROTOCOLCHECKSW",
    t4."OVERSIZEPKTSW",
    t4."PORTFCSWITCH",
    t4."RECPORTSWITCHOVERSW",
    t4."SIGPACKCTRLSW"
FROM
huawei_mml_gsm."INTBRDPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

IPCHK = ReplaceableObject(
    'huawei_cm_2g."IPCHK"',
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
    t1."ARPRETRY",
    t1."ARPTIMEOUT",
    t1."BAKIP",
    t1."BAKMASK",
    t1."CARRYT",
    t1."CHKN",
    t1."CHKTYPE",
    t1."CMEMODE",
    t1."PEERIP",
    t1."PN",
    t1."ROUTEASSOCIATEDFLAG",
    t1."SN",
    t1."SRN",
    t1."BFDDETECTCOUNT",
    t1."DSCP",
    t1."MINRXINT",
    t1."MINTXINT",
    t1."MYDISCRIMINATOR",
    t1."WHETHERAFFECTSWAP"
FROM
huawei_nbi_gsm."IPCHK" t1

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
    t2."ARPRETRY",
    t2."ARPTIMEOUT",
    NULL,
    NULL,
    t2."CARRYT",
    t2."CHKN",
    t2."CHKTYPE",
    NULL,
    t2."PEERIP",
    t2."PN",
    t2."ROUTEASSOCIATEDFLAG",
    t2."SN",
    t2."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."WHETHERAFFECTSWAP"
FROM
huawei_gexport_gsm."IPCHK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ARPRETRY",
    t3."ARPTIMEOUT",
    NULL,
    NULL,
    t3."CARRYT",
    t3."CHKN",
    t3."CHKTYPE",
    NULL,
    t3."PEERIP",
    t3."PN",
    t3."ROUTEASSOCIATEDFLAG",
    t3."SN",
    t3."SRN",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."WHETHERAFFECTSWAP"
FROM
huawei_gexport_gsm."IPCHK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

IPGUARD = ReplaceableObject(
    'huawei_cm_2g."IPGUARD"',
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
    t1."ARPANTICHEATSW",
    t1."ARPLRNSTRICTSW",
    t1."ARPREQALMCLRTHD",
    t1."ARPREQALMSW",
    t1."ARPREQALMTHD",
    t1."ARPRLYALMCLRTHD",
    t1."ARPRLYALMSW",
    t1."ARPRLYALMTHD",
    t1."BFDCTRLALMCLRTHD",
    t1."BFDCTRLALMSW",
    t1."BFDCTRLALMTHD",
    t1."BRDTYPE",
    t1."DHCPALMCLRTHD",
    t1."DHCPALMSW",
    t1."DHCPALMTHD",
    t1."ETHOAMALMCLRTHD",
    t1."ETHOAMALMSW",
    t1."ETHOAMALMTHD",
    t1."FWPKTTYPE",
    t1."ICMPALMRTHD",
    t1."ICMPALMSW",
    t1."ICMPALMTHD",
    t1."INVALIDMCASTALMRTHD",
    t1."INVALIDMCASTALMSW",
    t1."INVALIDMCASTALMTHD",
    t1."LACPALMCLRTHD",
    t1."LACPALMSW",
    t1."LACPALMTHD",
    t1."OMUFWFLAG",
    t1."SN",
    t1."SRN",
    t1."VALIDPKTCHKSW"
FROM
huawei_nbi_gsm."IPGUARD" t1

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
    t2."ARPANTICHEATSW",
    t2."ARPLRNSTRICTSW",
    t2."ARPREQALMCLRTHD",
    t2."ARPREQALMSW",
    t2."ARPREQALMTHD",
    t2."ARPRLYALMCLRTHD",
    t2."ARPRLYALMSW",
    t2."ARPRLYALMTHD",
    t2."BFDCTRLALMCLRTHD",
    t2."BFDCTRLALMSW",
    t2."BFDCTRLALMTHD",
    t2."BRDTYPE",
    t2."DHCPALMCLRTHD",
    t2."DHCPALMSW",
    t2."DHCPALMTHD",
    t2."ETHOAMALMCLRTHD",
    t2."ETHOAMALMSW",
    t2."ETHOAMALMTHD",
    t2."FWPKTTYPE",
    t2."ICMPALMRTHD",
    t2."ICMPALMSW",
    t2."ICMPALMTHD",
    t2."INVALIDMCASTALMRTHD",
    t2."INVALIDMCASTALMSW",
    t2."INVALIDMCASTALMTHD",
    t2."LACPALMCLRTHD",
    t2."LACPALMSW",
    t2."LACPALMTHD",
    t2."OMUFWFLAG",
    t2."SN",
    t2."SRN",
    t2."VALIDPKTCHKSW"
FROM
huawei_gexport_gsm."IPGUARD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ARPANTICHEATSW",
    t3."ARPLRNSTRICTSW",
    t3."ARPREQALMCLRTHD",
    t3."ARPREQALMSW",
    t3."ARPREQALMTHD",
    t3."ARPRLYALMCLRTHD",
    t3."ARPRLYALMSW",
    t3."ARPRLYALMTHD",
    t3."BFDCTRLALMCLRTHD",
    t3."BFDCTRLALMSW",
    t3."BFDCTRLALMTHD",
    t3."BRDTYPE",
    t3."DHCPALMCLRTHD",
    t3."DHCPALMSW",
    t3."DHCPALMTHD",
    t3."ETHOAMALMCLRTHD",
    t3."ETHOAMALMSW",
    t3."ETHOAMALMTHD",
    t3."FWPKTTYPE",
    t3."ICMPALMRTHD",
    t3."ICMPALMSW",
    t3."ICMPALMTHD",
    t3."INVALIDMCASTALMRTHD",
    t3."INVALIDMCASTALMSW",
    t3."INVALIDMCASTALMTHD",
    t3."LACPALMCLRTHD",
    t3."LACPALMSW",
    t3."LACPALMTHD",
    t3."OMUFWFLAG",
    t3."SN",
    t3."SRN",
    t3."VALIDPKTCHKSW"
FROM
huawei_gexport_gsm."IPGUARD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ARPANTICHEATSW",
    t4."ARPLRNSTRICTSW",
    t4."ARPREQALMCLRTHD",
    t4."ARPREQALMSW",
    t4."ARPREQALMTHD",
    t4."ARPRLYALMCLRTHD",
    t4."ARPRLYALMSW",
    t4."ARPRLYALMTHD",
    t4."BFDCTRLALMCLRTHD",
    t4."BFDCTRLALMSW",
    t4."BFDCTRLALMTHD",
    t4."BRDTYPE",
    t4."DHCPALMCLRTHD",
    t4."DHCPALMSW",
    t4."DHCPALMTHD",
    t4."ETHOAMALMCLRTHD",
    t4."ETHOAMALMSW",
    t4."ETHOAMALMTHD",
    t4."FWPKTTYPE",
    t4."ICMPALMRTHD",
    t4."ICMPALMSW",
    t4."ICMPALMTHD",
    t4."INVALIDMCASTALMRTHD",
    t4."INVALIDMCASTALMSW",
    t4."INVALIDMCASTALMTHD",
    t4."LACPALMCLRTHD",
    t4."LACPALMSW",
    t4."LACPALMTHD",
    t4."OMUFWFLAG",
    t4."SN",
    t4."SRN",
    t4."VALIDPKTCHKSW"
FROM
huawei_mml_gsm."IPGUARD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

IPLOGICPORT = ReplaceableObject(
    'huawei_cm_2g."IPLOGICPORT"',
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
    t1."BWADJ",
    t1."CARRYT",
    t1."CBS",
    t1."CIR",
    t1."FCINDEX",
    t1."FLOWCTRLSWITCH",
    t1."LPN",
    t1."LPNTYPE",
    t1."OAMFLOWBW",
    t1."OPSEPFLAG",
    t1."PN",
    t1."RSCMNGMODE",
    t1."SN",
    t1."SRN",
    t1."TRMLOADTHINDEX"
FROM
huawei_nbi_gsm."IPLOGICPORT" t1

"""
)

IPMUX = ReplaceableObject(
    'huawei_cm_2g."IPMUX"',
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
    t1."FPTIMER",
    t1."IPMUXINDEX",
    t1."ISQOSPATH",
    t1."MAXFRAMELEN",
    t1."MUXTYPE",
    t1."PATHID",
    t1."SUBFRAMELEN"
FROM
huawei_nbi_gsm."IPMUX" t1

"""
)

IPRT = ReplaceableObject(
    'huawei_cm_2g."IPRT"',
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
huawei_nbi_gsm."IPRT" t1

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
    t2."PRIORITY",
    t2."REMARK",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."IPRT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PRIORITY",
    t3."REMARK",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."IPRT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."IPRT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

ITWKPIALMTHD = ReplaceableObject(
    'huawei_cm_2g."ITWKPIALMTHD"',
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
    t1."ITWKPIALMSW"
FROM
huawei_nbi_gsm."ITWKPIALMTHD" t1

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
    t2."ITWKPIALMSW"
FROM
huawei_gexport_gsm."ITWKPIALMTHD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ITWKPIALMSW"
FROM
huawei_gexport_gsm."ITWKPIALMTHD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ITWKPIALMSW"
FROM
huawei_mml_gsm."ITWKPIALMTHD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

L2L3ROUTEPOLICY = ReplaceableObject(
    'huawei_cm_2g."L2L3ROUTEPOLICY"',
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
    t1."ROUTEPOLICY"
FROM
huawei_nbi_gsm."L2L3ROUTEPOLICY" t1

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
    t2."ROUTEPOLICY"
FROM
huawei_gexport_gsm."L2L3ROUTEPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ROUTEPOLICY"
FROM
huawei_gexport_gsm."L2L3ROUTEPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ROUTEPOLICY"
FROM
huawei_mml_gsm."L2L3ROUTEPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

LDR = ReplaceableObject(
    'huawei_cm_2g."LDR"',
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
    t1."LDRCONGSTATEJOINJUDGESW",
    t1."LDRFOUH",
    t1."LDRFST",
    t1."LDRHISTORYCONGSTATEREFSW",
    t1."LDRSND",
    t1."LSRTRD"
FROM
huawei_nbi_gsm."LDR" t1

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
    t2."LDRCONGSTATEJOINJUDGESW",
    t2."LDRFOUH",
    t2."LDRFST",
    t2."LDRHISTORYCONGSTATEREFSW",
    t2."LDRSND",
    t2."LSRTRD"
FROM
huawei_gexport_gsm."LDR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LDRCONGSTATEJOINJUDGESW",
    t3."LDRFOUH",
    t3."LDRFST",
    t3."LDRHISTORYCONGSTATEREFSW",
    t3."LDRSND",
    t3."LSRTRD"
FROM
huawei_gexport_gsm."LDR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LDRCONGSTATEJOINJUDGESW",
    t4."LDRFOUH",
    t4."LDRFST",
    t4."LDRHISTORYCONGSTATEREFSW",
    t4."LDRSND",
    t4."LSRTRD"
FROM
huawei_mml_gsm."LDR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

LICALMTHD = ReplaceableObject(
    'huawei_cm_2g."LICALMTHD"',
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
    t1."LICALMCTHD",
    t1."LICALMRTHD"
FROM
huawei_nbi_gsm."LICALMTHD" t1

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
    t2."LICALMCTHD",
    t2."LICALMRTHD"
FROM
huawei_gexport_gsm."LICALMTHD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LICALMCTHD",
    t3."LICALMRTHD"
FROM
huawei_gexport_gsm."LICALMTHD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LICALMCTHD",
    t4."LICALMRTHD"
FROM
huawei_mml_gsm."LICALMTHD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

LICPOLICY = ReplaceableObject(
    'huawei_cm_2g."LICPOLICY"',
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
    t1."LICUSAGESTATICMODE",
    t1."RVKMODE"
FROM
huawei_nbi_gsm."LICPOLICY" t1

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
    t2."LICUSAGESTATICMODE",
    t2."RVKMODE"
FROM
huawei_gexport_gsm."LICPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LICUSAGESTATICMODE",
    t3."RVKMODE"
FROM
huawei_gexport_gsm."LICPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LICUSAGESTATICMODE",
    t4."RVKMODE"
FROM
huawei_mml_gsm."LICPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

LODCTRL = ReplaceableObject(
    'huawei_cm_2g."LODCTRL"',
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
    t1."LODCTRL"
FROM
huawei_nbi_gsm."LODCTRL" t1

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
    t2."LODCTRL"
FROM
huawei_gexport_gsm."LODCTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LODCTRL"
FROM
huawei_gexport_gsm."LODCTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LODCTRL"
FROM
huawei_mml_gsm."LODCTRL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

LOGLIMIT = ReplaceableObject(
    'huawei_cm_2g."LOGLIMIT"',
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
    t1."CNTL",
    t1."LT",
    t1."TL"
FROM
huawei_nbi_gsm."LOGLIMIT" t1

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
    t2."CNTL",
    t2."LT",
    t2."TL"
FROM
huawei_gexport_gsm."LOGLIMIT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CNTL",
    t3."LT",
    t3."TL"
FROM
huawei_gexport_gsm."LOGLIMIT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CNTL",
    t4."LT",
    t4."TL"
FROM
huawei_mml_gsm."LOGLIMIT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

M3DE = ReplaceableObject(
    'huawei_cm_2g."M3DE"',
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
huawei_nbi_gsm."M3DE" t1

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
    t2."DENO",
    t2."DPX",
    t2."ENTITYT",
    t2."LENO",
    t2."NAME",
    t2."RTCONTEXT"
FROM
huawei_mml_gsm."M3DE" t2
INNER JOIN huawei_mml_gsm."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

M3LE = ReplaceableObject(
    'huawei_cm_2g."M3LE"',
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
huawei_nbi_gsm."M3LE" t1

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
    t2."ENTITYT",
    t2."LENO",
    t2."NAME",
    t2."RTCONTEXT",
    t2."SPX"
FROM
huawei_mml_gsm."M3LE" t2
INNER JOIN huawei_mml_gsm."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

M3LKS = ReplaceableObject(
    'huawei_cm_2g."M3LKS"',
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
    t1."M3UAHBSW",
    t1."NAME",
    t1."PDTMRVALUE",
    t1."SIGLKSX",
    t1."TRAMODE",
    t1."WKMODE"
FROM
huawei_nbi_gsm."M3LKS" t1

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
    t2."DENO",
    t2."LNKSLSMASK",
    NULL,
    t2."NAME",
    t2."PDTMRVALUE",
    t2."SIGLKSX",
    t2."TRAMODE",
    t2."WKMODE"
FROM
huawei_mml_gsm."M3LKS" t2
INNER JOIN huawei_mml_gsm."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

M3LNK = ReplaceableObject(
    'huawei_cm_2g."M3LNK"',
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
    t1."SCTPLNKN",
    t1."SIGLKSX",
    t1."SIGLNKID",
    t1."SN",
    t1."SRN",
    t1."SSN"
FROM
huawei_nbi_gsm."M3LNK" t1

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
    t2."LNKREDFLAG",
    t2."NAME",
    t2."PRIORITY",
    NULL,
    t2."SCTPLNKN",
    t2."SIGLKSX",
    t2."SIGLNKID",
    t2."SN",
    t2."SRN",
    t2."SSN"
FROM
huawei_mml_gsm."M3LNK" t2
INNER JOIN huawei_mml_gsm."SYS" t21 ON t21."FileName" = t2."FileName"

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
    t3."SIGLKSX",
    t3."SIGLNKID",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."M3LNK_ACT" t3
INNER JOIN huawei_mml_gsm."SYS" t31 ON t31."FileName" = t3."FileName"

"""
)

M3RT = ReplaceableObject(
    'huawei_cm_2g."M3RT"',
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
huawei_nbi_gsm."M3RT" t1

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
    t2."DENO",
    t2."NAME",
    t2."PRIORITY",
    t2."SIGLKSX"
FROM
huawei_mml_gsm."M3RT" t2
INNER JOIN huawei_mml_gsm."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

MDTLCS = ReplaceableObject(
    'huawei_cm_2g."MDTLCS"',
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
    t1."GMDTASKMODE",
    t1."GMDTASKSWITCH",
    t1."PERIOD",
    t1."PRECISIONMDT",
    t1."SMLCID"
FROM
huawei_nbi_gsm."MDTLCS" t1

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
    t2."GMDTASKMODE",
    t2."GMDTASKSWITCH",
    t2."PERIOD",
    t2."PRECISIONMDT",
    t2."SMLCID"
FROM
huawei_gexport_gsm."MDTLCS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."GMDTASKMODE",
    t3."GMDTASKSWITCH",
    t3."PERIOD",
    t3."PRECISIONMDT",
    t3."SMLCID"
FROM
huawei_gexport_gsm."MDTLCS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GMDTASKMODE",
    t4."GMDTASKSWITCH",
    t4."PERIOD",
    t4."PRECISIONMDT",
    t4."SMLCID"
FROM
huawei_mml_gsm."MDTLCS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

MNTMODE = ReplaceableObject(
    'huawei_cm_2g."MNTMODE"',
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
    t1."MNTMODE"
FROM
huawei_nbi_gsm."MNTMODE" t1

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
    t2."MNTMODE"
FROM
huawei_gexport_gsm."MNTMODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."MNTMODE"
FROM
huawei_gexport_gsm."MNTMODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."MNTMODE"
FROM
huawei_mml_gsm."MNTMODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

MOCNPARA = ReplaceableObject(
    'huawei_cm_2g."MOCNPARA"',
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
    t1."CSCNRESPTMR",
    t1."LTEUSESHASW",
    t1."PSCNRESPTMR"
FROM
huawei_nbi_gsm."MOCNPARA" t1

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
    t2."CSCNRESPTMR",
    t2."LTEUSESHASW",
    t2."PSCNRESPTMR"
FROM
huawei_gexport_gsm."MOCNPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CSCNRESPTMR",
    t3."LTEUSESHASW",
    t3."PSCNRESPTMR"
FROM
huawei_gexport_gsm."MOCNPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CSCNRESPTMR",
    t4."LTEUSESHASW",
    t4."PSCNRESPTMR"
FROM
huawei_mml_gsm."MOCNPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

MSGSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."MSGSOFTPARA"',
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
    t1."CELLLISTOPTIONSEND",
    t1."CHOSENCHINASSCMP",
    t1."CHOSENCHINHOPERFORM",
    t1."CHOSENCHINHOREQACK",
    t1."CHOSENENCRYPALGINCIPHCMP",
    t1."CHOSENENCRYPALGINHOPERFORM",
    t1."CHOSENENCRYPALOINASSCMP",
    t1."CHOSENENCRYPALOINHOREQACK",
    t1."CICPOOLINASSFAIL",
    t1."CICPOOLINHOFAIL",
    t1."CICPOOLLISTINASSFAIL",
    t1."CICPOOLLISTINHOFAIL",
    t1."CICPOOLNUM",
    t1."CICPOOLSENDFLAGINASSCMP",
    t1."CICPOOLSENDFLAGINHOACK",
    t1."CIPHERMODEINHOREQACK",
    t1."CNNODEIDX",
    t1."CURCHANNELINHORQD",
    t1."HOFAILINDIRECTRETRYSW",
    t1."HOSDCCHSPEECHVER",
    t1."SPEECHCODEINHOREQACK",
    t1."SPEECHVERINASSCMP",
    t1."SPEECHVERINHOPERFORM",
    t1."SPEECHVERINHOREQACK",
    t1."SPEECHVERINHORQD",
    t1."UCCTRLOFCICIE"
FROM
huawei_nbi_gsm."MSGSOFTPARA" t1

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
    t2."CELLLISTOPTIONSEND",
    t2."CHOSENCHINASSCMP",
    t2."CHOSENCHINHOPERFORM",
    t2."CHOSENCHINHOREQACK",
    t2."CHOSENENCRYPALGINCIPHCMP",
    t2."CHOSENENCRYPALGINHOPERFORM",
    t2."CHOSENENCRYPALOINASSCMP",
    t2."CHOSENENCRYPALOINHOREQACK",
    t2."CICPOOLINASSFAIL",
    t2."CICPOOLINHOFAIL",
    t2."CICPOOLLISTINASSFAIL",
    t2."CICPOOLLISTINHOFAIL",
    t2."CICPOOLNUM",
    t2."CICPOOLSENDFLAGINASSCMP",
    t2."CICPOOLSENDFLAGINHOACK",
    t2."CIPHERMODEINHOREQACK",
    t2."CNNODEIDX",
    t2."CURCHANNELINHORQD",
    t2."HOFAILINDIRECTRETRYSW",
    t2."HOSDCCHSPEECHVER",
    t2."SPEECHCODEINHOREQACK",
    t2."SPEECHVERINASSCMP",
    t2."SPEECHVERINHOPERFORM",
    t2."SPEECHVERINHOREQACK",
    t2."SPEECHVERINHORQD",
    t2."UCCTRLOFCICIE"
FROM
huawei_gexport_gsm."MSGSOFTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CELLLISTOPTIONSEND",
    t3."CHOSENCHINASSCMP",
    t3."CHOSENCHINHOPERFORM",
    t3."CHOSENCHINHOREQACK",
    t3."CHOSENENCRYPALGINCIPHCMP",
    t3."CHOSENENCRYPALGINHOPERFORM",
    t3."CHOSENENCRYPALOINASSCMP",
    t3."CHOSENENCRYPALOINHOREQACK",
    t3."CICPOOLINASSFAIL",
    t3."CICPOOLINHOFAIL",
    t3."CICPOOLLISTINASSFAIL",
    t3."CICPOOLLISTINHOFAIL",
    t3."CICPOOLNUM",
    t3."CICPOOLSENDFLAGINASSCMP",
    t3."CICPOOLSENDFLAGINHOACK",
    t3."CIPHERMODEINHOREQACK",
    t3."CNNODEIDX",
    t3."CURCHANNELINHORQD",
    t3."HOFAILINDIRECTRETRYSW",
    t3."HOSDCCHSPEECHVER",
    t3."SPEECHCODEINHOREQACK",
    t3."SPEECHVERINASSCMP",
    t3."SPEECHVERINHOPERFORM",
    t3."SPEECHVERINHOREQACK",
    t3."SPEECHVERINHORQD",
    t3."UCCTRLOFCICIE"
FROM
huawei_gexport_gsm."MSGSOFTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CELLLISTOPTIONSEND",
    t4."CHOSENCHINASSCMP",
    t4."CHOSENCHINHOPERFORM",
    t4."CHOSENCHINHOREQACK",
    t4."CHOSENENCRYPALGINCIPHCMP",
    t4."CHOSENENCRYPALGINHOPERFORM",
    t4."CHOSENENCRYPALOINASSCMP",
    t4."CHOSENENCRYPALOINHOREQACK",
    t4."CICPOOLINASSFAIL",
    t4."CICPOOLINHOFAIL",
    t4."CICPOOLLISTINASSFAIL",
    t4."CICPOOLLISTINHOFAIL",
    t4."CICPOOLNUM",
    t4."CICPOOLSENDFLAGINASSCMP",
    t4."CICPOOLSENDFLAGINHOACK",
    t4."CIPHERMODEINHOREQACK",
    t4."CNNODEIDX",
    t4."CURCHANNELINHORQD",
    t4."HOFAILINDIRECTRETRYSW",
    t4."HOSDCCHSPEECHVER",
    t4."SPEECHCODEINHOREQACK",
    t4."SPEECHVERINASSCMP",
    t4."SPEECHVERINHOPERFORM",
    t4."SPEECHVERINHOREQACK",
    t4."SPEECHVERINHORQD",
    t4."UCCTRLOFCICIE"
FROM
huawei_mml_gsm."MSGSOFTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

MSP = ReplaceableObject(
    'huawei_cm_2g."MSP"',
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
huawei_nbi_gsm."MSP" t1

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
    NULL
FROM
huawei_gexport_gsm."MSP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    NULL
FROM
huawei_gexport_gsm."MSP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    NULL
FROM
huawei_mml_gsm."MSP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
huawei_mml_gsm."MSP_ACT" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

MTP3LKS = ReplaceableObject(
    'huawei_cm_2g."MTP3LKS"',
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
    t1."EMERGENCY",
    t1."LNKSLSMASK",
    t1."NAME",
    t1."SIGLKSX"
FROM
huawei_nbi_gsm."MTP3LKS" t1

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
    t2."DPX",
    t2."EMERGENCY",
    t2."LNKSLSMASK",
    t2."NAME",
    t2."SIGLKSX"
FROM
huawei_gexport_gsm."MTP3LKS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DPX",
    t3."EMERGENCY",
    t3."LNKSLSMASK",
    t3."NAME",
    t3."SIGLKSX"
FROM
huawei_gexport_gsm."MTP3LKS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DPX",
    t4."EMERGENCY",
    t4."LNKSLSMASK",
    t4."NAME",
    t4."SIGLKSX"
FROM
huawei_mml_gsm."MTP3LKS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."SIGLKSX"
FROM
huawei_mml_gsm."MTP3LKS_ACT" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

MTP3LNK = ReplaceableObject(
    'huawei_cm_2g."MTP3LNK"',
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
    t1."APN",
    t1."ASN",
    t1."ASRN",
    t1."ATSMASK",
    t1."BEARTYPE",
    t1."CT1",
    t1."CT2",
    t1."CT3",
    t1."CT4E",
    t1."CT4N",
    t1."CT5",
    t1."CT6",
    t1."CT7",
    t1."CT9",
    t1."LKTATE",
    t1."MTP2LNKN",
    t1."NAME",
    t1."PRIORITY",
    t1."SIGLKSX",
    t1."SIGSLC",
    t1."SN",
    t1."SRN",
    t1."SSN",
    t1."STFLG",
    t1."TC",
    t1."TCLEN",
    t1."TCMODE"
FROM
huawei_nbi_gsm."MTP3LNK" t1

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
    t2."APN",
    t2."ASN",
    t2."ASRN",
    NULL,
    t2."BEARTYPE",
    t2."CT1",
    t2."CT2",
    t2."CT3",
    t2."CT4E",
    t2."CT4N",
    t2."CT5",
    t2."CT6",
    t2."CT7",
    t2."CT9",
    t2."LKTATE",
    t2."MTP2LNKN",
    t2."NAME",
    t2."PRIORITY",
    t2."SIGLKSX",
    t2."SIGSLC",
    t2."SN",
    t2."SRN",
    t2."SSN",
    t2."STFLG",
    t2."TC",
    t2."TCLEN",
    t2."TCMODE"
FROM
huawei_gexport_gsm."MTP3LNK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."APN",
    t3."ASN",
    t3."ASRN",
    NULL,
    t3."BEARTYPE",
    t3."CT1",
    t3."CT2",
    t3."CT3",
    t3."CT4E",
    t3."CT4N",
    t3."CT5",
    t3."CT6",
    t3."CT7",
    t3."CT9",
    t3."LKTATE",
    t3."MTP2LNKN",
    t3."NAME",
    t3."PRIORITY",
    t3."SIGLKSX",
    t3."SIGSLC",
    t3."SN",
    t3."SRN",
    t3."SSN",
    t3."STFLG",
    t3."TC",
    t3."TCLEN",
    t3."TCMODE"
FROM
huawei_gexport_gsm."MTP3LNK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."APN",
    t4."ASN",
    t4."ASRN",
    NULL,
    t4."BEARTYPE",
    t4."CT1",
    t4."CT2",
    t4."CT3",
    t4."CT4E",
    t4."CT4N",
    t4."CT5",
    t4."CT6",
    t4."CT7",
    t4."CT9",
    t4."LKTATE",
    t4."MTP2LNKN",
    t4."NAME",
    t4."PRIORITY",
    t4."SIGLKSX",
    t4."SIGSLC",
    t4."SN",
    t4."SRN",
    t4."SSN",
    t4."STFLG",
    t4."TC",
    t4."TCLEN",
    t4."TCMODE"
FROM
huawei_mml_gsm."MTP3LNK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."SIGLKSX",
    t5."SIGSLC",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."MTP3LNK_ACT" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

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
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t6."SIGLKSX",
    t6."SIGSLC",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."MTP3LNK_UIN" t6
INNER JOIN huawei_mml_gsm."SYS" t61 ON t61."FileName" = t6."FileName"

"""
)

MTP3RT = ReplaceableObject(
    'huawei_cm_2g."MTP3RT"',
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
    t1."NAME",
    t1."PRIORITY",
    t1."SIGLKSX"
FROM
huawei_nbi_gsm."MTP3RT" t1

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
    t2."DPX",
    t2."NAME",
    t2."PRIORITY",
    t2."SIGLKSX"
FROM
huawei_gexport_gsm."MTP3RT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DPX",
    t3."NAME",
    t3."PRIORITY",
    t3."SIGLKSX"
FROM
huawei_gexport_gsm."MTP3RT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DPX",
    t4."NAME",
    t4."PRIORITY",
    t4."SIGLKSX"
FROM
huawei_mml_gsm."MTP3RT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

MTP3TMR = ReplaceableObject(
    'huawei_cm_2g."MTP3TMR"',
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
huawei_nbi_gsm."MTP3TMR" t1

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
huawei_gexport_gsm."MTP3TMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."MTP3TMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."MTP3TMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

N7DPC = ReplaceableObject(
    'huawei_cm_2g."N7DPC"',
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
    t1."SSTTIMEOUTSTRA",
    t1."STP"
FROM
huawei_nbi_gsm."N7DPC" t1

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
    t2."SSTTIMEOUTSTRA",
    NULL
FROM
huawei_gexport_gsm."N7DPC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SSTTIMEOUTSTRA",
    NULL
FROM
huawei_gexport_gsm."N7DPC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SSTTIMEOUTSTRA",
    t4."STP"
FROM
huawei_mml_gsm."N7DPC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    NULL,
    NULL
FROM
huawei_mml_gsm."N7DPC_UIN" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

NRIMSCMAP = ReplaceableObject(
    'huawei_cm_2g."NRIMSCMAP"',
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
    t1."CNNODEIDX",
    t1."NRI"
FROM
huawei_nbi_gsm."NRIMSCMAP" t1

"""
)

NRISGSNMAP = ReplaceableObject(
    'huawei_cm_2g."NRISGSNMAP"',
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
    t1."NRI",
    t1."OPNAME"
FROM
huawei_nbi_gsm."NRISGSNMAP" t1

"""
)

NSE = ReplaceableObject(
    'huawei_cm_2g."NSE"',
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
    t1."ISNCMODE",
    t1."LCSSUP",
    t1."MOCNSUP",
    t1."NSEI",
    t1."OPNAME",
    t1."PFCSUP",
    t1."PSHOSUP",
    t1."PT",
    t1."RIMSUP",
    t1."SN",
    t1."SRN",
    t1."SVRIP",
    t1."SVRPORT"
FROM
huawei_nbi_gsm."NSE" t1

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
    t2."CNID",
    t2."ISNCMODE",
    t2."LCSSUP",
    t2."MOCNSUP",
    t2."NSEI",
    t2."OPNAME",
    t2."PFCSUP",
    t2."PSHOSUP",
    t2."PT",
    t2."RIMSUP",
    t2."SN",
    t2."SRN",
    t2."SVRIP",
    t2."SVRPORT"
FROM
huawei_gexport_gsm."NSE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CNID",
    t3."ISNCMODE",
    t3."LCSSUP",
    t3."MOCNSUP",
    t3."NSEI",
    t3."OPNAME",
    t3."PFCSUP",
    t3."PSHOSUP",
    t3."PT",
    t3."RIMSUP",
    t3."SN",
    t3."SRN",
    t3."SVRIP",
    t3."SVRPORT"
FROM
huawei_gexport_gsm."NSE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CNID",
    t4."ISNCMODE",
    t4."LCSSUP",
    t4."MOCNSUP",
    t4."NSEI",
    t4."OPNAME",
    t4."PFCSUP",
    t4."PSHOSUP",
    t4."PT",
    t4."RIMSUP",
    t4."SN",
    t4."SRN",
    t4."SVRIP",
    t4."SVRPORT"
FROM
huawei_mml_gsm."NSE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

NSVLLOCAL = ReplaceableObject(
    'huawei_cm_2g."NSVLLOCAL"',
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
    t1."IP",
    t1."LOCALNSVLI",
    t1."NSEI",
    t1."SIGLW",
    t1."SN",
    t1."SRN",
    t1."SRVLW",
    t1."UDPPN"
FROM
huawei_nbi_gsm."NSVLLOCAL" t1

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
    t2."IP",
    t2."LOCALNSVLI",
    t2."NSEI",
    t2."SIGLW",
    t2."SN",
    t2."SRN",
    t2."SRVLW",
    t2."UDPPN"
FROM
huawei_gexport_gsm."NSVLLOCAL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IP",
    t3."LOCALNSVLI",
    t3."NSEI",
    t3."SIGLW",
    t3."SN",
    t3."SRN",
    t3."SRVLW",
    t3."UDPPN"
FROM
huawei_gexport_gsm."NSVLLOCAL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IP",
    t4."LOCALNSVLI",
    t4."NSEI",
    t4."SIGLW",
    t4."SN",
    t4."SRN",
    t4."SRVLW",
    t4."UDPPN"
FROM
huawei_mml_gsm."NSVLLOCAL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OBJALMSHLD = ReplaceableObject(
    'huawei_cm_2g."OBJALMSHLD"',
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
    t1."AID",
    t1."AIDST",
    t1."DSPN",
    t1."OBJTP",
    t1."PN",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."OBJALMSHLD" t1

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
    t2."AID",
    NULL,
    NULL,
    t2."OBJTP",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."OBJALMSHLD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AID",
    NULL,
    NULL,
    t3."OBJTP",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."OBJALMSHLD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AID",
    NULL,
    NULL,
    t4."OBJTP",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."OBJALMSHLD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OBJAUTHSW = ReplaceableObject(
    'huawei_cm_2g."OBJAUTHSW"',
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
    t1."SW"
FROM
huawei_nbi_gsm."OBJAUTHSW" t1

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
    t2."SW"
FROM
huawei_gexport_gsm."OBJAUTHSW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SW"
FROM
huawei_gexport_gsm."OBJAUTHSW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SW"
FROM
huawei_mml_gsm."OBJAUTHSW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OMUCOMMSVCSW = ReplaceableObject(
    'huawei_cm_2g."OMUCOMMSVCSW"',
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
    t1."ALMBOXSVCSW"
FROM
huawei_nbi_gsm."OMUCOMMSVCSW" t1

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
    t2."ALMBOXSVCSW"
FROM
huawei_gexport_gsm."OMUCOMMSVCSW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALMBOXSVCSW"
FROM
huawei_gexport_gsm."OMUCOMMSVCSW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALMBOXSVCSW"
FROM
huawei_mml_gsm."OMUCOMMSVCSW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OMUETH = ReplaceableObject(
    'huawei_cm_2g."OMUETH"',
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
    t1."ALMSW"
FROM
huawei_nbi_gsm."OMUETH" t1

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
    t2."ALMSW"
FROM
huawei_gexport_gsm."OMUETH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALMSW"
FROM
huawei_gexport_gsm."OMUETH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALMSW"
FROM
huawei_mml_gsm."OMUETH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OMUPARA = ReplaceableObject(
    'huawei_cm_2g."OMUPARA"',
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
    t1."CAPMONLOGSW",
    t1."DISKFAULTSWAPSW",
    t1."FREEDISKSW",
    t1."HOSTLOGFCSW",
    t1."INTCHKFAILSTOPLOADSW"
FROM
huawei_nbi_gsm."OMUPARA" t1

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
    t2."CAPMONLOGSW",
    t2."DISKFAULTSWAPSW",
    t2."FREEDISKSW",
    t2."HOSTLOGFCSW",
    t2."INTCHKFAILSTOPLOADSW"
FROM
huawei_gexport_gsm."OMUPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CAPMONLOGSW",
    t3."DISKFAULTSWAPSW",
    t3."FREEDISKSW",
    t3."HOSTLOGFCSW",
    t3."INTCHKFAILSTOPLOADSW"
FROM
huawei_gexport_gsm."OMUPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CAPMONLOGSW",
    t4."DISKFAULTSWAPSW",
    t4."FREEDISKSW",
    t4."HOSTLOGFCSW",
    t4."INTCHKFAILSTOPLOADSW"
FROM
huawei_mml_gsm."OMUPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OMUPORT = ReplaceableObject(
    'huawei_cm_2g."OMUPORT"',
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
    t1."PORTTYPE",
    t1."SW"
FROM
huawei_nbi_gsm."OMUPORT" t1

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
    t2."PORTTYPE",
    t2."SW"
FROM
huawei_gexport_gsm."OMUPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PORTTYPE",
    t3."SW"
FROM
huawei_gexport_gsm."OMUPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PORTTYPE",
    t4."SW"
FROM
huawei_mml_gsm."OMUPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OPC = ReplaceableObject(
    'huawei_cm_2g."OPC"',
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
huawei_nbi_gsm."OPC" t1

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
huawei_gexport_gsm."OPC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."OPC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."OPC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OPLOCK = ReplaceableObject(
    'huawei_cm_2g."OPLOCK"',
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
    t1."LOCKST"
FROM
huawei_nbi_gsm."OPLOCK" t1

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
    t2."LOCKST"
FROM
huawei_gexport_gsm."OPLOCK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LOCKST"
FROM
huawei_gexport_gsm."OPLOCK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LOCKST"
FROM
huawei_mml_gsm."OPLOCK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OPSW = ReplaceableObject(
    'huawei_cm_2g."OPSW"',
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
    t1."SWOP"
FROM
huawei_nbi_gsm."OPSW" t1

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
    t2."SWOP"
FROM
huawei_gexport_gsm."OPSW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SWOP"
FROM
huawei_gexport_gsm."OPSW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SWOP"
FROM
huawei_mml_gsm."OPSW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OPT = ReplaceableObject(
    'huawei_cm_2g."OPT"',
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
    t1."AUTYPE",
    t1."B1B2SDTHRD",
    t1."B1B2SFTHRD",
    t1."B3SDTHRD",
    t1."B3SFTHRD",
    t1."BT",
    t1."J0TYPE",
    t1."J1TYPE",
    t1."JAUTOADD",
    t1."LNKNUMMODE",
    t1."OPTM",
    t1."PN",
    t1."PS",
    t1."S1VALUE",
    t1."SN",
    t1."SRN",
    t1."J0BYTE_FORMAT",
    t1."J0RXVALUE",
    t1."J0TXVALUE",
    t1."J1BYTE_FORMAT",
    t1."J1RXVALUE",
    t1."J1TXVALUE"
FROM
huawei_nbi_gsm."OPT" t1

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
    t2."B1B2SDTHRD",
    t2."B1B2SFTHRD",
    t2."B3SDTHRD",
    t2."B3SFTHRD",
    t2."BT",
    t2."J0TYPE",
    t2."J1TYPE",
    t2."JAUTOADD",
    t2."LNKNUMMODE",
    t2."OPTM",
    t2."PN",
    NULL,
    NULL,
    t2."SN",
    t2."SRN",
    t2."J0BYTE_FORMAT",
    t2."J0RXVALUE",
    t2."J0TXVALUE",
    t2."J1BYTE_FORMAT",
    t2."J1RXVALUE",
    t2."J1TXVALUE"
FROM
huawei_gexport_gsm."OPT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."B1B2SDTHRD",
    t3."B1B2SFTHRD",
    t3."B3SDTHRD",
    t3."B3SFTHRD",
    t3."BT",
    t3."J0TYPE",
    t3."J1TYPE",
    t3."JAUTOADD",
    t3."LNKNUMMODE",
    t3."OPTM",
    t3."PN",
    NULL,
    NULL,
    t3."SN",
    t3."SRN",
    t3."J0BYTE_FORMAT",
    t3."J0RXVALUE",
    t3."J0TXVALUE",
    t3."J1BYTE_FORMAT",
    t3."J1RXVALUE",
    t3."J1TXVALUE"
FROM
huawei_gexport_gsm."OPT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."B1B2SDTHRD",
    t4."B1B2SFTHRD",
    t4."B3SDTHRD",
    t4."B3SFTHRD",
    t4."BT",
    t4."J0TYPE",
    t4."J1TYPE",
    t4."JAUTOADD",
    t4."LNKNUMMODE",
    t4."OPTM",
    t4."PN",
    NULL,
    t4."S1VALUE",
    t4."SN",
    t4."SRN",
    t4."J0BYTE_FORMAT",
    t4."J0RXVALUE",
    t4."J0TXVALUE",
    t4."J1BYTE_FORMAT",
    t4."J1RXVALUE",
    t4."J1TXVALUE"
FROM
huawei_mml_gsm."OPT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OSPWDPOLICY = ReplaceableObject(
    'huawei_cm_2g."OSPWDPOLICY"',
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
    t1."ACTSW",
    t1."COMPLICACY",
    t1."COMPLICACYSW",
    t1."DICTCHKSW",
    t1."HISTORYPWDNUM",
    t1."MAXVALIDDATES",
    t1."PWDMINLEN"
FROM
huawei_nbi_gsm."OSPWDPOLICY" t1

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
    t2."ACTSW",
    NULL,
    t2."COMPLICACYSW",
    t2."DICTCHKSW",
    t2."HISTORYPWDNUM",
    t2."MAXVALIDDATES",
    t2."PWDMINLEN"
FROM
huawei_gexport_gsm."OSPWDPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACTSW",
    NULL,
    t3."COMPLICACYSW",
    t3."DICTCHKSW",
    t3."HISTORYPWDNUM",
    t3."MAXVALIDDATES",
    t3."PWDMINLEN"
FROM
huawei_gexport_gsm."OSPWDPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACTSW",
    NULL,
    t4."COMPLICACYSW",
    t4."DICTCHKSW",
    t4."HISTORYPWDNUM",
    t4."MAXVALIDDATES",
    t4."PWDMINLEN"
FROM
huawei_mml_gsm."OSPWDPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

OTHSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."OTHSOFTPARA"',
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
    t1."ABISLINKFAILCALLDROPOPT",
    t1."ABNORMALMOSTHRESHOLD",
    t1."ACCCAUSESTATOPT",
    t1."AINTFMSGUSINGTHRESHOLD",
    t1."AMRHRLICUPDOPTSW",
    t1."AN19",
    t1."ASSFAILSTATEOPT",
    t1."ASSFAILSTATISTICOPT",
    t1."ASSTHRES",
    t1."ATER8KSW",
    t1."ATERCONGHRFLAG",
    t1."ATERCONGSTRATIO",
    t1."AUTOGETBTSLOGFLAG",
    t1."BSCPMA",
    t1."BSCPMAIRAHO",
    t1."BSCPRICLASS",
    t1."BSCQAD",
    t1."BSCQADIRAHO",
    t1."BSCRESERVEDPARA20",
    t1."BSCRESERVEDPARA21",
    t1."BSCRESERVEDPARA3",
    t1."BSCRESERVEDPARA6",
    t1."BSCRESERVEDPARA8",
    t1."BTSCHRMSISDN",
    t1."CALLRSTDROPSTATOPT",
    t1."CAOPT",
    t1."CFGCHANCHANGEOPT",
    t1."CHECKINGBTSCONNECTION",
    t1."CHRMRNCELLTYPE",
    t1."CLASSMARK3FLAG",
    t1."CLASSMARKQUERY",
    t1."CMUPDATEOPTIMIZETYPE",
    t1."CSDOUTBSCFAILSTAT",
    t1."CSSCNIDHOFILTER",
    t1."DELAYSENDHOCMDSTIMER",
    t1."DELAYSENDHOCMDSWITCH",
    t1."DISCONNECTHANDOVERPROTECTTIMER",
    t1."DLDTMFPRCSW",
    t1."DTMCSHOOPTSW",
    t1."DTMUPDATEOPTITYPE",
    t1."EMLPPPRIORITY",
    t1."EMRPROMSREQTIMES",
    t1."EMRPROMSSATTIMES",
    t1."END2ENDTRACESTATE",
    t1."EQUIPFAILDROPOPT",
    t1."FASTRESELECTSW",
    t1."FLEXABISTSPREEMPTOPTSW",
    t1."FRSUPPORTWHENCELLCONGEST",
    t1."G2G3GLDBLCDELTATHRD",
    t1."GRPULCHK",
    t1."HALFRATEDATASUPPORT",
    t1."HIGHLEVPREEM",
    t1."HOPSINGLEFREQOPTSWITCH",
    t1."IBCAFLOWCTRLPERIOD",
    t1."IBCAFLOWCTRLTHRELD",
    t1."IBCAINBSCINFORPTPRD",
    t1."IBCAOUTBSCINFORPTPRD",
    t1."IMMTCHMOC",
    t1."IMMTCHMTC",
    t1."IMSIHOCTRL",
    t1."INBSCCLRCMDSTATOPT",
    t1."INHOEC",
    t1."INHOFAILSTATOPT",
    t1."INTERBSCHOPREEMPALLOWED",
    t1."INTERRATCELLRESELOPTEN",
    t1."IURGLOADCAPOPTSWITCH",
    t1."JITBUFSWITCH",
    t1."KCRIRESORTSWITCH",
    t1."MAXLOADBTSNUM",
    t1."MAXPBLINKCHKNUM",
    t1."MOCNCTRL",
    t1."MOCNXIDRSTPOLICY",
    t1."MODIFYATTREQNU",
    t1."MSCABNORMALRELSTATSDCCHDROP",
    t1."MSCABNORMALRELSTATTCHDROP",
    t1."MSCREASSOPTSW",
    t1."MUTESAICIDEALPHALTHD",
    t1."MUTESAICIDEALPHAUTHD",
    t1."MUTESAICIDEREQTIMES",
    t1."MUTESAICIDESATTIMES",
    t1."N3GCELLCOVERAGETH1",
    t1."N3GCELLCOVERAGETH2",
    t1."N3GCELLMEASURETH0",
    t1."N3GCELLMEASURETH1",
    t1."N3GCELLMEASURETH2",
    t1."NAVIGATION",
    t1."NCELLINTERFLEVELTHRES0",
    t1."NCELLINTERFLEVELTHRES1",
    t1."NCELLINTERFLEVELTHRES2",
    t1."NCELLINTERFLEVELTHRES3",
    t1."NCELLINTERFLEVELTHRES4",
    t1."NCELLINTERFLEVELTHRES5",
    t1."NCELLINTERFLEVELTHRES6",
    t1."NCELLINTERFLEVELTHRES7",
    t1."NCELLSTATOPTTIME",
    t1."NOCAIMMASSSTATOPT",
    t1."NONIBCADYNMEAEN",
    t1."NOTMSIALLCELLPAGINGLIMITFLAG",
    t1."NROFFDDCELLFLAG",
    t1."OMLDETECTTIME",
    t1."OUTBSCHOFAILSTATOPTSW",
    t1."OUTBSCHOREQSTATOPT",
    t1."OUTSYSSERVHOREASSIGNEN",
    t1."OUTSYSSERVICEHOEN",
    t1."PBMTNMSGRESEND",
    t1."PDCH2TCHOPTSWITCH",
    t1."PREEMFORHONOTREL",
    t1."PREEMFORHOPDCH",
    t1."PSSCNIDHOFILTER",
    t1."QUEINASSOPTSTAT",
    t1."RECORDDISCARDEDPAGINGINFOFLAG",
    t1."REDIRECTOPT",
    t1."RELCAUSENOTIRSP",
    t1."RELOCRATETYPECHG",
    t1."RESCHECKALLOWED",
    t1."RESETALMDELAYSWITCH",
    t1."RESETALMDELAYTIME",
    t1."RESPREQSEL",
    t1."RSSTHRES",
    t1."SAICPROMSIDEREQTIMES",
    t1."SAICPROMSIDESATTIMES",
    t1."SEND2QUTERFLAG",
    t1."SENDDOWNLINKMESSAGE",
    t1."SENDSI2TERFLAG",
    t1."SENDSI5TERFLAG",
    t1."SENDSPEECHVERSIONAHEAD",
    t1."SENDUTRANECSCFLAG",
    t1."SERV3GCELLIDOPT",
    t1."SHORTCALLTHRED",
    t1."SI2TERSWITCH",
    t1."SPTPBLAPDCHECK",
    t1."SPTPBRESCHECK",
    t1."SPTPBSGLPASSCHECK",
    t1."SPTPCICCHECK",
    t1."SUPPORTAPPLYUSEDCIC",
    t1."SUTMROPMODE",
    t1."TALIMITDROPSTATOPT",
    t1."TASATEABNORMALOPT",
    t1."TCHBUSYSATEOPTSWITCH",
    t1."TCHRATEMODIFY",
    t1."TCSTATISTICSW",
    t1."TCSTATISTICTYPE",
    t1."TER2INDICATOR",
    t1."TIMESTAMPERRORCMPSWITH",
    t1."TRXAVAILJUDGOPT",
    t1."UCISRAIFAULT",
    t1."ULTOOLLOWRXLEV",
    t1."VIPUSROUTBSCHOSWITCH",
    t1."VIPUSRSWITCH",
    t1."VIPUSRTCHTHRES",
    t1."VOICEOPENTRACESW",
    t1."WINADJSWITCH",
    t1."VAMOSACTPCDSWITCH"
FROM
huawei_nbi_gsm."OTHSOFTPARA" t1

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
    t2."ABISLINKFAILCALLDROPOPT",
    t2."ABNORMALMOSTHRESHOLD",
    t2."ACCCAUSESTATOPT",
    t2."AINTFMSGUSINGTHRESHOLD",
    t2."AMRHRLICUPDOPTSW",
    t2."AN19",
    t2."ASSFAILSTATEOPT",
    t2."ASSFAILSTATISTICOPT",
    t2."ASSTHRES",
    t2."ATER8KSW",
    t2."ATERCONGHRFLAG",
    t2."ATERCONGSTRATIO",
    t2."AUTOGETBTSLOGFLAG",
    t2."BSCPMA",
    t2."BSCPMAIRAHO",
    t2."BSCPRICLASS",
    t2."BSCQAD",
    t2."BSCQADIRAHO",
    t2."BSCRESERVEDPARA20",
    t2."BSCRESERVEDPARA21",
    t2."BSCRESERVEDPARA3",
    t2."BSCRESERVEDPARA6",
    t2."BSCRESERVEDPARA8",
    NULL,
    t2."CALLRSTDROPSTATOPT",
    t2."CAOPT",
    t2."CFGCHANCHANGEOPT",
    t2."CHECKINGBTSCONNECTION",
    t2."CHRMRNCELLTYPE",
    t2."CLASSMARK3FLAG",
    t2."CLASSMARKQUERY",
    t2."CMUPDATEOPTIMIZETYPE",
    t2."CSDOUTBSCFAILSTAT",
    t2."CSSCNIDHOFILTER",
    t2."DELAYSENDHOCMDSTIMER",
    t2."DELAYSENDHOCMDSWITCH",
    t2."DISCONNECTHANDOVERPROTECTTIMER",
    t2."DLDTMFPRCSW",
    t2."DTMCSHOOPTSW",
    t2."DTMUPDATEOPTITYPE",
    t2."EMLPPPRIORITY",
    t2."EMRPROMSREQTIMES",
    t2."EMRPROMSSATTIMES",
    t2."END2ENDTRACESTATE",
    t2."EQUIPFAILDROPOPT",
    t2."FASTRESELECTSW",
    t2."FLEXABISTSPREEMPTOPTSW",
    t2."FRSUPPORTWHENCELLCONGEST",
    t2."G2G3GLDBLCDELTATHRD",
    t2."GRPULCHK",
    t2."HALFRATEDATASUPPORT",
    t2."HIGHLEVPREEM",
    t2."HOPSINGLEFREQOPTSWITCH",
    t2."IBCAFLOWCTRLPERIOD",
    t2."IBCAFLOWCTRLTHRELD",
    t2."IBCAINBSCINFORPTPRD",
    t2."IBCAOUTBSCINFORPTPRD",
    t2."IMMTCHMOC",
    t2."IMMTCHMTC",
    t2."IMSIHOCTRL",
    t2."INBSCCLRCMDSTATOPT",
    t2."INHOEC",
    t2."INHOFAILSTATOPT",
    t2."INTERBSCHOPREEMPALLOWED",
    t2."INTERRATCELLRESELOPTEN",
    t2."IURGLOADCAPOPTSWITCH",
    t2."JITBUFSWITCH",
    t2."KCRIRESORTSWITCH",
    t2."MAXLOADBTSNUM",
    t2."MAXPBLINKCHKNUM",
    t2."MOCNCTRL",
    t2."MOCNXIDRSTPOLICY",
    t2."MODIFYATTREQNU",
    t2."MSCABNORMALRELSTATSDCCHDROP",
    t2."MSCABNORMALRELSTATTCHDROP",
    t2."MSCREASSOPTSW",
    t2."MUTESAICIDEALPHALTHD",
    t2."MUTESAICIDEALPHAUTHD",
    t2."MUTESAICIDEREQTIMES",
    t2."MUTESAICIDESATTIMES",
    t2."N3GCELLCOVERAGETH1",
    t2."N3GCELLCOVERAGETH2",
    t2."N3GCELLMEASURETH0",
    t2."N3GCELLMEASURETH1",
    t2."N3GCELLMEASURETH2",
    t2."NAVIGATION",
    t2."NCELLINTERFLEVELTHRES0",
    t2."NCELLINTERFLEVELTHRES1",
    t2."NCELLINTERFLEVELTHRES2",
    t2."NCELLINTERFLEVELTHRES3",
    t2."NCELLINTERFLEVELTHRES4",
    t2."NCELLINTERFLEVELTHRES5",
    t2."NCELLINTERFLEVELTHRES6",
    t2."NCELLINTERFLEVELTHRES7",
    t2."NCELLSTATOPTTIME",
    t2."NOCAIMMASSSTATOPT",
    t2."NONIBCADYNMEAEN",
    t2."NOTMSIALLCELLPAGINGLIMITFLAG",
    t2."NROFFDDCELLFLAG",
    t2."OMLDETECTTIME",
    t2."OUTBSCHOFAILSTATOPTSW",
    t2."OUTBSCHOREQSTATOPT",
    t2."OUTSYSSERVHOREASSIGNEN",
    t2."OUTSYSSERVICEHOEN",
    t2."PBMTNMSGRESEND",
    t2."PDCH2TCHOPTSWITCH",
    t2."PREEMFORHONOTREL",
    t2."PREEMFORHOPDCH",
    t2."PSSCNIDHOFILTER",
    t2."QUEINASSOPTSTAT",
    t2."RECORDDISCARDEDPAGINGINFOFLAG",
    t2."REDIRECTOPT",
    t2."RELCAUSENOTIRSP",
    t2."RELOCRATETYPECHG",
    t2."RESCHECKALLOWED",
    t2."RESETALMDELAYSWITCH",
    t2."RESETALMDELAYTIME",
    t2."RESPREQSEL",
    t2."RSSTHRES",
    t2."SAICPROMSIDEREQTIMES",
    t2."SAICPROMSIDESATTIMES",
    t2."SEND2QUTERFLAG",
    t2."SENDDOWNLINKMESSAGE",
    t2."SENDSI2TERFLAG",
    t2."SENDSI5TERFLAG",
    t2."SENDSPEECHVERSIONAHEAD",
    t2."SENDUTRANECSCFLAG",
    t2."SERV3GCELLIDOPT",
    t2."SHORTCALLTHRED",
    t2."SI2TERSWITCH",
    t2."SPTPBLAPDCHECK",
    t2."SPTPBRESCHECK",
    t2."SPTPBSGLPASSCHECK",
    t2."SPTPCICCHECK",
    t2."SUPPORTAPPLYUSEDCIC",
    t2."SUTMROPMODE",
    t2."TALIMITDROPSTATOPT",
    t2."TASATEABNORMALOPT",
    t2."TCHBUSYSATEOPTSWITCH",
    t2."TCHRATEMODIFY",
    t2."TCSTATISTICSW",
    NULL,
    t2."TER2INDICATOR",
    t2."TIMESTAMPERRORCMPSWITH",
    t2."TRXAVAILJUDGOPT",
    t2."UCISRAIFAULT",
    t2."ULTOOLLOWRXLEV",
    t2."VIPUSROUTBSCHOSWITCH",
    t2."VIPUSRSWITCH",
    t2."VIPUSRTCHTHRES",
    t2."VOICEOPENTRACESW",
    t2."WINADJSWITCH",
    NULL
FROM
huawei_gexport_gsm."OTHSOFTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISLINKFAILCALLDROPOPT",
    t3."ABNORMALMOSTHRESHOLD",
    t3."ACCCAUSESTATOPT",
    t3."AINTFMSGUSINGTHRESHOLD",
    t3."AMRHRLICUPDOPTSW",
    t3."AN19",
    t3."ASSFAILSTATEOPT",
    t3."ASSFAILSTATISTICOPT",
    t3."ASSTHRES",
    t3."ATER8KSW",
    t3."ATERCONGHRFLAG",
    t3."ATERCONGSTRATIO",
    t3."AUTOGETBTSLOGFLAG",
    t3."BSCPMA",
    t3."BSCPMAIRAHO",
    t3."BSCPRICLASS",
    t3."BSCQAD",
    t3."BSCQADIRAHO",
    t3."BSCRESERVEDPARA20",
    t3."BSCRESERVEDPARA21",
    t3."BSCRESERVEDPARA3",
    t3."BSCRESERVEDPARA6",
    t3."BSCRESERVEDPARA8",
    NULL,
    t3."CALLRSTDROPSTATOPT",
    t3."CAOPT",
    t3."CFGCHANCHANGEOPT",
    t3."CHECKINGBTSCONNECTION",
    t3."CHRMRNCELLTYPE",
    t3."CLASSMARK3FLAG",
    t3."CLASSMARKQUERY",
    t3."CMUPDATEOPTIMIZETYPE",
    t3."CSDOUTBSCFAILSTAT",
    t3."CSSCNIDHOFILTER",
    t3."DELAYSENDHOCMDSTIMER",
    t3."DELAYSENDHOCMDSWITCH",
    t3."DISCONNECTHANDOVERPROTECTTIMER",
    t3."DLDTMFPRCSW",
    t3."DTMCSHOOPTSW",
    t3."DTMUPDATEOPTITYPE",
    t3."EMLPPPRIORITY",
    t3."EMRPROMSREQTIMES",
    t3."EMRPROMSSATTIMES",
    t3."END2ENDTRACESTATE",
    t3."EQUIPFAILDROPOPT",
    t3."FASTRESELECTSW",
    t3."FLEXABISTSPREEMPTOPTSW",
    t3."FRSUPPORTWHENCELLCONGEST",
    t3."G2G3GLDBLCDELTATHRD",
    t3."GRPULCHK",
    t3."HALFRATEDATASUPPORT",
    t3."HIGHLEVPREEM",
    t3."HOPSINGLEFREQOPTSWITCH",
    t3."IBCAFLOWCTRLPERIOD",
    t3."IBCAFLOWCTRLTHRELD",
    t3."IBCAINBSCINFORPTPRD",
    t3."IBCAOUTBSCINFORPTPRD",
    t3."IMMTCHMOC",
    t3."IMMTCHMTC",
    t3."IMSIHOCTRL",
    t3."INBSCCLRCMDSTATOPT",
    t3."INHOEC",
    t3."INHOFAILSTATOPT",
    t3."INTERBSCHOPREEMPALLOWED",
    t3."INTERRATCELLRESELOPTEN",
    t3."IURGLOADCAPOPTSWITCH",
    t3."JITBUFSWITCH",
    t3."KCRIRESORTSWITCH",
    t3."MAXLOADBTSNUM",
    t3."MAXPBLINKCHKNUM",
    t3."MOCNCTRL",
    t3."MOCNXIDRSTPOLICY",
    t3."MODIFYATTREQNU",
    t3."MSCABNORMALRELSTATSDCCHDROP",
    t3."MSCABNORMALRELSTATTCHDROP",
    t3."MSCREASSOPTSW",
    t3."MUTESAICIDEALPHALTHD",
    t3."MUTESAICIDEALPHAUTHD",
    t3."MUTESAICIDEREQTIMES",
    t3."MUTESAICIDESATTIMES",
    t3."N3GCELLCOVERAGETH1",
    t3."N3GCELLCOVERAGETH2",
    t3."N3GCELLMEASURETH0",
    t3."N3GCELLMEASURETH1",
    t3."N3GCELLMEASURETH2",
    t3."NAVIGATION",
    t3."NCELLINTERFLEVELTHRES0",
    t3."NCELLINTERFLEVELTHRES1",
    t3."NCELLINTERFLEVELTHRES2",
    t3."NCELLINTERFLEVELTHRES3",
    t3."NCELLINTERFLEVELTHRES4",
    t3."NCELLINTERFLEVELTHRES5",
    t3."NCELLINTERFLEVELTHRES6",
    t3."NCELLINTERFLEVELTHRES7",
    t3."NCELLSTATOPTTIME",
    t3."NOCAIMMASSSTATOPT",
    t3."NONIBCADYNMEAEN",
    t3."NOTMSIALLCELLPAGINGLIMITFLAG",
    t3."NROFFDDCELLFLAG",
    t3."OMLDETECTTIME",
    t3."OUTBSCHOFAILSTATOPTSW",
    t3."OUTBSCHOREQSTATOPT",
    t3."OUTSYSSERVHOREASSIGNEN",
    t3."OUTSYSSERVICEHOEN",
    t3."PBMTNMSGRESEND",
    t3."PDCH2TCHOPTSWITCH",
    t3."PREEMFORHONOTREL",
    t3."PREEMFORHOPDCH",
    t3."PSSCNIDHOFILTER",
    t3."QUEINASSOPTSTAT",
    t3."RECORDDISCARDEDPAGINGINFOFLAG",
    t3."REDIRECTOPT",
    t3."RELCAUSENOTIRSP",
    t3."RELOCRATETYPECHG",
    t3."RESCHECKALLOWED",
    t3."RESETALMDELAYSWITCH",
    t3."RESETALMDELAYTIME",
    t3."RESPREQSEL",
    t3."RSSTHRES",
    t3."SAICPROMSIDEREQTIMES",
    t3."SAICPROMSIDESATTIMES",
    t3."SEND2QUTERFLAG",
    t3."SENDDOWNLINKMESSAGE",
    t3."SENDSI2TERFLAG",
    t3."SENDSI5TERFLAG",
    t3."SENDSPEECHVERSIONAHEAD",
    t3."SENDUTRANECSCFLAG",
    t3."SERV3GCELLIDOPT",
    t3."SHORTCALLTHRED",
    t3."SI2TERSWITCH",
    t3."SPTPBLAPDCHECK",
    t3."SPTPBRESCHECK",
    t3."SPTPBSGLPASSCHECK",
    t3."SPTPCICCHECK",
    t3."SUPPORTAPPLYUSEDCIC",
    t3."SUTMROPMODE",
    t3."TALIMITDROPSTATOPT",
    t3."TASATEABNORMALOPT",
    t3."TCHBUSYSATEOPTSWITCH",
    t3."TCHRATEMODIFY",
    t3."TCSTATISTICSW",
    NULL,
    t3."TER2INDICATOR",
    t3."TIMESTAMPERRORCMPSWITH",
    t3."TRXAVAILJUDGOPT",
    t3."UCISRAIFAULT",
    t3."ULTOOLLOWRXLEV",
    t3."VIPUSROUTBSCHOSWITCH",
    t3."VIPUSRSWITCH",
    t3."VIPUSRTCHTHRES",
    t3."VOICEOPENTRACESW",
    t3."WINADJSWITCH",
    NULL
FROM
huawei_gexport_gsm."OTHSOFTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISLINKFAILCALLDROPOPT",
    t4."ABNORMALMOSTHRESHOLD",
    t4."ACCCAUSESTATOPT",
    t4."AINTFMSGUSINGTHRESHOLD",
    t4."AMRHRLICUPDOPTSW",
    t4."AN19",
    t4."ASSFAILSTATEOPT",
    t4."ASSFAILSTATISTICOPT",
    t4."ASSTHRES",
    t4."ATER8KSW",
    t4."ATERCONGHRFLAG",
    t4."ATERCONGSTRATIO",
    t4."AUTOGETBTSLOGFLAG",
    t4."BSCPMA",
    t4."BSCPMAIRAHO",
    t4."BSCPRICLASS",
    t4."BSCQAD",
    t4."BSCQADIRAHO",
    t4."BSCRESERVEDPARA20",
    t4."BSCRESERVEDPARA21",
    t4."BSCRESERVEDPARA3",
    t4."BSCRESERVEDPARA6",
    t4."BSCRESERVEDPARA8",
    t4."BTSCHRMSISDN",
    t4."CALLRSTDROPSTATOPT",
    t4."CAOPT",
    t4."CFGCHANCHANGEOPT",
    t4."CHECKINGBTSCONNECTION",
    t4."CHRMRNCELLTYPE",
    t4."CLASSMARK3FLAG",
    t4."CLASSMARKQUERY",
    t4."CMUPDATEOPTIMIZETYPE",
    t4."CSDOUTBSCFAILSTAT",
    t4."CSSCNIDHOFILTER",
    t4."DELAYSENDHOCMDSTIMER",
    t4."DELAYSENDHOCMDSWITCH",
    t4."DISCONNECTHANDOVERPROTECTTIMER",
    t4."DLDTMFPRCSW",
    t4."DTMCSHOOPTSW",
    t4."DTMUPDATEOPTITYPE",
    t4."EMLPPPRIORITY",
    t4."EMRPROMSREQTIMES",
    t4."EMRPROMSSATTIMES",
    t4."END2ENDTRACESTATE",
    t4."EQUIPFAILDROPOPT",
    t4."FASTRESELECTSW",
    t4."FLEXABISTSPREEMPTOPTSW",
    t4."FRSUPPORTWHENCELLCONGEST",
    t4."G2G3GLDBLCDELTATHRD",
    t4."GRPULCHK",
    t4."HALFRATEDATASUPPORT",
    t4."HIGHLEVPREEM",
    t4."HOPSINGLEFREQOPTSWITCH",
    t4."IBCAFLOWCTRLPERIOD",
    t4."IBCAFLOWCTRLTHRELD",
    t4."IBCAINBSCINFORPTPRD",
    t4."IBCAOUTBSCINFORPTPRD",
    t4."IMMTCHMOC",
    t4."IMMTCHMTC",
    t4."IMSIHOCTRL",
    t4."INBSCCLRCMDSTATOPT",
    t4."INHOEC",
    t4."INHOFAILSTATOPT",
    t4."INTERBSCHOPREEMPALLOWED",
    t4."INTERRATCELLRESELOPTEN",
    t4."IURGLOADCAPOPTSWITCH",
    t4."JITBUFSWITCH",
    t4."KCRIRESORTSWITCH",
    t4."MAXLOADBTSNUM",
    t4."MAXPBLINKCHKNUM",
    t4."MOCNCTRL",
    t4."MOCNXIDRSTPOLICY",
    t4."MODIFYATTREQNU",
    t4."MSCABNORMALRELSTATSDCCHDROP",
    t4."MSCABNORMALRELSTATTCHDROP",
    t4."MSCREASSOPTSW",
    t4."MUTESAICIDEALPHALTHD",
    t4."MUTESAICIDEALPHAUTHD",
    t4."MUTESAICIDEREQTIMES",
    t4."MUTESAICIDESATTIMES",
    t4."N3GCELLCOVERAGETH1",
    t4."N3GCELLCOVERAGETH2",
    t4."N3GCELLMEASURETH0",
    t4."N3GCELLMEASURETH1",
    t4."N3GCELLMEASURETH2",
    t4."NAVIGATION",
    t4."NCELLINTERFLEVELTHRES0",
    t4."NCELLINTERFLEVELTHRES1",
    t4."NCELLINTERFLEVELTHRES2",
    t4."NCELLINTERFLEVELTHRES3",
    t4."NCELLINTERFLEVELTHRES4",
    t4."NCELLINTERFLEVELTHRES5",
    t4."NCELLINTERFLEVELTHRES6",
    t4."NCELLINTERFLEVELTHRES7",
    t4."NCELLSTATOPTTIME",
    t4."NOCAIMMASSSTATOPT",
    t4."NONIBCADYNMEAEN",
    t4."NOTMSIALLCELLPAGINGLIMITFLAG",
    t4."NROFFDDCELLFLAG",
    t4."OMLDETECTTIME",
    t4."OUTBSCHOFAILSTATOPTSW",
    t4."OUTBSCHOREQSTATOPT",
    t4."OUTSYSSERVHOREASSIGNEN",
    t4."OUTSYSSERVICEHOEN",
    t4."PBMTNMSGRESEND",
    t4."PDCH2TCHOPTSWITCH",
    t4."PREEMFORHONOTREL",
    t4."PREEMFORHOPDCH",
    t4."PSSCNIDHOFILTER",
    t4."QUEINASSOPTSTAT",
    t4."RECORDDISCARDEDPAGINGINFOFLAG",
    t4."REDIRECTOPT",
    t4."RELCAUSENOTIRSP",
    t4."RELOCRATETYPECHG",
    t4."RESCHECKALLOWED",
    t4."RESETALMDELAYSWITCH",
    t4."RESETALMDELAYTIME",
    t4."RESPREQSEL",
    t4."RSSTHRES",
    t4."SAICPROMSIDEREQTIMES",
    t4."SAICPROMSIDESATTIMES",
    t4."SEND2QUTERFLAG",
    t4."SENDDOWNLINKMESSAGE",
    t4."SENDSI2TERFLAG",
    t4."SENDSI5TERFLAG",
    t4."SENDSPEECHVERSIONAHEAD",
    t4."SENDUTRANECSCFLAG",
    t4."SERV3GCELLIDOPT",
    t4."SHORTCALLTHRED",
    t4."SI2TERSWITCH",
    t4."SPTPBLAPDCHECK",
    t4."SPTPBRESCHECK",
    t4."SPTPBSGLPASSCHECK",
    t4."SPTPCICCHECK",
    t4."SUPPORTAPPLYUSEDCIC",
    t4."SUTMROPMODE",
    t4."TALIMITDROPSTATOPT",
    t4."TASATEABNORMALOPT",
    t4."TCHBUSYSATEOPTSWITCH",
    t4."TCHRATEMODIFY",
    t4."TCSTATISTICSW",
    NULL,
    t4."TER2INDICATOR",
    t4."TIMESTAMPERRORCMPSWITH",
    t4."TRXAVAILJUDGOPT",
    t4."UCISRAIFAULT",
    t4."ULTOOLLOWRXLEV",
    t4."VIPUSROUTBSCHOSWITCH",
    t4."VIPUSRSWITCH",
    t4."VIPUSRTCHTHRES",
    t4."VOICEOPENTRACESW",
    t4."WINADJSWITCH",
    t4."VAMOSACTPCDSWITCH"
FROM
huawei_mml_gsm."OTHSOFTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PACKETFILTERALMPARA = ReplaceableObject(
    'huawei_cm_2g."PACKETFILTERALMPARA"',
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
    t1."PKTFILTERALMRTHD",
    t1."PKTFILTERALMTHD"
FROM
huawei_nbi_gsm."PACKETFILTERALMPARA" t1

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
    t2."PKTFILTERALMRTHD",
    t2."PKTFILTERALMTHD"
FROM
huawei_gexport_gsm."PACKETFILTERALMPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PKTFILTERALMRTHD",
    t3."PKTFILTERALMTHD"
FROM
huawei_gexport_gsm."PACKETFILTERALMPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PKTFILTERALMRTHD",
    t4."PKTFILTERALMTHD"
FROM
huawei_mml_gsm."PACKETFILTERALMPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PHBMAP = ReplaceableObject(
    'huawei_cm_2g."PHBMAP"',
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
huawei_nbi_gsm."PHBMAP" t1

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
huawei_gexport_gsm."PHBMAP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."PHBMAP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."PHBMAP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PORTFLOWCTRLPARA = ReplaceableObject(
    'huawei_cm_2g."PORTFLOWCTRLPARA"',
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
huawei_nbi_gsm."PORTFLOWCTRLPARA" t1

"""
)

PORTOSCCTRLPARA = ReplaceableObject(
    'huawei_cm_2g."PORTOSCCTRLPARA"',
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
    t1."SN",
    t1."SRN",
    t1."SUPPRESSSWITCH"
FROM
huawei_nbi_gsm."PORTOSCCTRLPARA" t1

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
    t2."SN",
    t2."SRN",
    t2."SUPPRESSSWITCH"
FROM
huawei_gexport_gsm."PORTOSCCTRLPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SN",
    t3."SRN",
    t3."SUPPRESSSWITCH"
FROM
huawei_gexport_gsm."PORTOSCCTRLPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SN",
    t4."SRN",
    t4."SUPPRESSSWITCH"
FROM
huawei_mml_gsm."PORTOSCCTRLPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PSPREFABISCONGCTRL = ReplaceableObject(
    'huawei_cm_2g."PSPREFABISCONGCTRL"',
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
    t1."UCPSPREFCALLREESTPRIO",
    t1."UCPSPREFCSEMERGCALLPRIO",
    t1."UCPSPREFCSORGCALLPRIO",
    t1."UCPSPREFCSTERMCALLPRIO",
    t1."UCPSPREFINBSCHOPRIO",
    t1."UCPSPREFINTRABSCHOPRIO",
    t1."UCPSPREFOTHERPRIO",
    t1."UCPSPREFPSPRIO",
    t1."UCPSPREFSUPPLEPRIO",
    t1."UCPSPREFVBSPRIO",
    t1."UCPSPREFVGCSPRIO"
FROM
huawei_nbi_gsm."PSPREFABISCONGCTRL" t1

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
    t2."UCPSPREFCALLREESTPRIO",
    t2."UCPSPREFCSEMERGCALLPRIO",
    t2."UCPSPREFCSORGCALLPRIO",
    t2."UCPSPREFCSTERMCALLPRIO",
    t2."UCPSPREFINBSCHOPRIO",
    t2."UCPSPREFINTRABSCHOPRIO",
    t2."UCPSPREFOTHERPRIO",
    t2."UCPSPREFPSPRIO",
    t2."UCPSPREFSUPPLEPRIO",
    t2."UCPSPREFVBSPRIO",
    t2."UCPSPREFVGCSPRIO"
FROM
huawei_gexport_gsm."PSPREFABISCONGCTRL_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."UCPSPREFCALLREESTPRIO",
    t3."UCPSPREFCSEMERGCALLPRIO",
    t3."UCPSPREFCSORGCALLPRIO",
    t3."UCPSPREFCSTERMCALLPRIO",
    t3."UCPSPREFINBSCHOPRIO",
    t3."UCPSPREFINTRABSCHOPRIO",
    t3."UCPSPREFOTHERPRIO",
    t3."UCPSPREFPSPRIO",
    t3."UCPSPREFSUPPLEPRIO",
    t3."UCPSPREFVBSPRIO",
    t3."UCPSPREFVGCSPRIO"
FROM
huawei_gexport_gsm."PSPREFABISCONGCTRL_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."UCPSPREFCALLREESTPRIO",
    t4."UCPSPREFCSEMERGCALLPRIO",
    t4."UCPSPREFCSORGCALLPRIO",
    t4."UCPSPREFCSTERMCALLPRIO",
    t4."UCPSPREFINBSCHOPRIO",
    t4."UCPSPREFINTRABSCHOPRIO",
    t4."UCPSPREFOTHERPRIO",
    t4."UCPSPREFPSPRIO",
    t4."UCPSPREFSUPPLEPRIO",
    t4."UCPSPREFVBSPRIO",
    t4."UCPSPREFVGCSPRIO"
FROM
huawei_mml_gsm."PSPREFABISCONGCTRL" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PSUSRRESBIND = ReplaceableObject(
    'huawei_cm_2g."PSUSRRESBIND"',
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
    t1."IDXTYPE"
FROM
huawei_nbi_gsm."PSUSRRESBIND" t1

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
    t2."IDXTYPE"
FROM
huawei_gexport_gsm."PSUSRRESBIND_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IDXTYPE"
FROM
huawei_gexport_gsm."PSUSRRESBIND_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IDXTYPE"
FROM
huawei_mml_gsm."PSUSRRESBIND" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PTPBVC = ReplaceableObject(
    'huawei_cm_2g."PTPBVC"',
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
    t1."BVCI",
    t1."CELLID",
    t1."NSEI"
FROM
huawei_nbi_gsm."PTPBVC" t1

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
    t2."BVCI",
    t2."CELLID",
    t2."NSEI"
FROM
huawei_gexport_gsm."PTPBVC_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BVCI",
    t3."CELLID",
    t3."NSEI"
FROM
huawei_gexport_gsm."PTPBVC_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BVCI",
    t4."CELLID",
    t4."NSEI"
FROM
huawei_mml_gsm."PTPBVC" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."BVCI",
    NULL,
    t5."NSEI"
FROM
huawei_mml_gsm."PTPBVC_UBL" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

PWDPOLICY = ReplaceableObject(
    'huawei_cm_2g."PWDPOLICY"',
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
    t1."AUTOUNLOCKTIME",
    t1."COMPLICACY",
    t1."DICTCHKSW",
    t1."FIRSTLOGINMUSTMODPWD",
    t1."HISTORYPWDNUM",
    t1."MAXMISSTIMES",
    t1."MAXPROMPTDATES",
    t1."MAXREPEATCHARTIMES",
    t1."MAXVALIDDATES",
    t1."MINVALIDINTERVAL",
    t1."PWDMINLEN",
    t1."RESETINTERVAL"
FROM
huawei_nbi_gsm."PWDPOLICY" t1

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
    t2."AUTOUNLOCKTIME",
    NULL,
    t2."DICTCHKSW",
    t2."FIRSTLOGINMUSTMODPWD",
    t2."HISTORYPWDNUM",
    t2."MAXMISSTIMES",
    t2."MAXPROMPTDATES",
    t2."MAXREPEATCHARTIMES",
    t2."MAXVALIDDATES",
    t2."MINVALIDINTERVAL",
    t2."PWDMINLEN",
    t2."RESETINTERVAL"
FROM
huawei_gexport_gsm."PWDPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AUTOUNLOCKTIME",
    NULL,
    t3."DICTCHKSW",
    t3."FIRSTLOGINMUSTMODPWD",
    t3."HISTORYPWDNUM",
    t3."MAXMISSTIMES",
    t3."MAXPROMPTDATES",
    t3."MAXREPEATCHARTIMES",
    t3."MAXVALIDDATES",
    t3."MINVALIDINTERVAL",
    t3."PWDMINLEN",
    t3."RESETINTERVAL"
FROM
huawei_gexport_gsm."PWDPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AUTOUNLOCKTIME",
    NULL,
    t4."DICTCHKSW",
    t4."FIRSTLOGINMUSTMODPWD",
    t4."HISTORYPWDNUM",
    t4."MAXMISSTIMES",
    t4."MAXPROMPTDATES",
    t4."MAXREPEATCHARTIMES",
    t4."MAXVALIDDATES",
    t4."MINVALIDINTERVAL",
    t4."PWDMINLEN",
    t4."RESETINTERVAL"
FROM
huawei_mml_gsm."PWDPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PWRALMSW = ReplaceableObject(
    'huawei_cm_2g."PWRALMSW"',
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
    t1."PWRALMSSW1",
    t1."PWRALMSSW2",
    t1."SRN"
FROM
huawei_nbi_gsm."PWRALMSW" t1

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
    NULL,
    t2."SRN"
FROM
huawei_gexport_gsm."PWRALMSW_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    NULL,
    t3."SRN"
FROM
huawei_gexport_gsm."PWRALMSW_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SRN"
FROM
huawei_mml_gsm."PWRALMSW" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

PWRPARA = ReplaceableObject(
    'huawei_cm_2g."PWRPARA"',
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
    t1."NO1M48ALMTHDDOWN",
    t1."NO1M48ALMTHDUP",
    t1."NO2M48ALMTHDDOWN",
    t1."NO2M48ALMTHDUP",
    t1."NO3M48ALMTHDDOWN",
    t1."NO3M48ALMTHDUP",
    t1."NO4M48ALMTHDDOWN",
    t1."NO4M48ALMTHDUP",
    t1."NO5M48ALMTHDDOWN",
    t1."NO5M48ALMTHDUP",
    t1."NO6M48ALMTHDDOWN",
    t1."NO6M48ALMTHDUP",
    t1."SRN"
FROM
huawei_nbi_gsm."PWRPARA" t1

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
    t2."NO1M48ALMTHDDOWN",
    t2."NO1M48ALMTHDUP",
    t2."NO2M48ALMTHDDOWN",
    t2."NO2M48ALMTHDUP",
    t2."NO3M48ALMTHDDOWN",
    t2."NO3M48ALMTHDUP",
    t2."NO4M48ALMTHDDOWN",
    t2."NO4M48ALMTHDUP",
    t2."NO5M48ALMTHDDOWN",
    t2."NO5M48ALMTHDUP",
    t2."NO6M48ALMTHDDOWN",
    t2."NO6M48ALMTHDUP",
    t2."SRN"
FROM
huawei_gexport_gsm."PWRPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."NO1M48ALMTHDDOWN",
    t3."NO1M48ALMTHDUP",
    t3."NO2M48ALMTHDDOWN",
    t3."NO2M48ALMTHDUP",
    t3."NO3M48ALMTHDDOWN",
    t3."NO3M48ALMTHDUP",
    t3."NO4M48ALMTHDDOWN",
    t3."NO4M48ALMTHDUP",
    t3."NO5M48ALMTHDDOWN",
    t3."NO5M48ALMTHDUP",
    t3."NO6M48ALMTHDDOWN",
    t3."NO6M48ALMTHDUP",
    t3."SRN"
FROM
huawei_gexport_gsm."PWRPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."NO1M48ALMTHDDOWN",
    t4."NO1M48ALMTHDUP",
    t4."NO2M48ALMTHDDOWN",
    t4."NO2M48ALMTHDUP",
    t4."NO3M48ALMTHDDOWN",
    t4."NO3M48ALMTHDUP",
    t4."NO4M48ALMTHDDOWN",
    t4."NO4M48ALMTHDUP",
    t4."NO5M48ALMTHDDOWN",
    t4."NO5M48ALMTHDUP",
    t4."NO6M48ALMTHDDOWN",
    t4."NO6M48ALMTHDUP",
    t4."SRN"
FROM
huawei_mml_gsm."PWRPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

QUEUEMAP = ReplaceableObject(
    'huawei_cm_2g."QUEUEMAP"',
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
huawei_nbi_gsm."QUEUEMAP" t1

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
huawei_gexport_gsm."QUEUEMAP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."QUEUEMAP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."QUEUEMAP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

RSVRES = ReplaceableObject(
    'huawei_cm_2g."RSVRES"',
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
    t1."BMDPUSLOTNO",
    t1."BMDPUSUBRACKNO",
    t1."BMDSPENDTS",
    t1."BMDSPNO",
    t1."BMDSPSTARTTS",
    t1."BSCTID",
    t1."BTCFLAG",
    t1."RESRESERVEDMINUTES"
FROM
huawei_nbi_gsm."RSVRES" t1

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
    t2."BMDPUSLOTNO",
    t2."BMDPUSUBRACKNO",
    t2."BMDSPENDTS",
    t2."BMDSPNO",
    t2."BMDSPSTARTTS",
    NULL,
    t2."BTCFLAG",
    t2."RESRESERVEDMINUTES"
FROM
huawei_gexport_gsm."RSVRES_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."BMDPUSLOTNO",
    t3."BMDPUSUBRACKNO",
    t3."BMDSPENDTS",
    t3."BMDSPNO",
    t3."BMDSPSTARTTS",
    NULL,
    t3."BTCFLAG",
    t3."RESRESERVEDMINUTES"
FROM
huawei_gexport_gsm."RSVRES_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."BMDPUSLOTNO",
    t4."BMDPUSUBRACKNO",
    t4."BMDSPENDTS",
    t4."BMDSPNO",
    t4."BMDSPSTARTTS",
    t4."BSCTID",
    t4."BTCFLAG",
    t4."RESRESERVEDMINUTES"
FROM
huawei_mml_gsm."RSVRES" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

RULELIBVER = ReplaceableObject(
    'huawei_cm_2g."RULELIBVER"',
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
    t1."VERIFYLIBVER"
FROM
huawei_nbi_gsm."RULELIBVER" t1

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
    t2."VERIFYLIBVER"
FROM
huawei_gexport_gsm."RULELIBVER_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."VERIFYLIBVER"
FROM
huawei_gexport_gsm."RULELIBVER_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

SAUCENTER = ReplaceableObject(
    'huawei_cm_2g."SAUCENTER"',
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
    t1."FTPCENTER",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."SAUCENTER" t1

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
    t2."FTPCENTER",
    NULL,
    NULL
FROM
huawei_gexport_gsm."SAUCENTER_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FTPCENTER",
    NULL,
    NULL
FROM
huawei_gexport_gsm."SAUCENTER_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."FTPCENTER",
    NULL,
    NULL
FROM
huawei_mml_gsm."SAUCENTER" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SCCPTMR = ReplaceableObject(
    'huawei_cm_2g."SCCPTMR"',
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
huawei_nbi_gsm."SCCPTMR" t1

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
huawei_gexport_gsm."SCCPTMR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."SCCPTMR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."SCCPTMR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SCTPLNK = ReplaceableObject(
    'huawei_cm_2g."SCTPLNK"',
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
    t1."CHKSUMRX",
    t1."CHKSUMTX",
    t1."CHKSUMTYPE",
    t1."CMEMODE",
    t1."CROSSIPFLAG",
    t1."DSCP",
    t1."HBINTER",
    t1."LOCIP1",
    t1."LOCIP2",
    t1."LOCPN",
    t1."LOGPORTFLAG",
    t1."MAXASSOCRETR",
    t1."MAXPATHRETR",
    t1."MTU",
    t1."PEERIP1",
    t1."PEERIP2",
    t1."PEERMULTIFASTRETRANFLAG",
    t1."PEERPN",
    t1."REMARK",
    t1."RTOALPHA",
    t1."RTOBETA",
    t1."RTOINIT",
    t1."RTOMAX",
    t1."RTOMIN",
    t1."SCTPLNKID",
    t1."SCTPLNKN",
    t1."SN",
    t1."SRN",
    t1."SWITCHBACKFLAG",
    t1."SWITCHBACKHBNUM",
    t1."TSACK",
    t1."VLANFLAG1",
    t1."VLANFLAG2"
FROM
huawei_nbi_gsm."SCTPLNK" t1

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
    t2."APP",
    t2."BUNDLINGFLAG",
    t2."CHKSUMRX",
    t2."CHKSUMTX",
    t2."CHKSUMTYPE",
    NULL,
    t2."CROSSIPFLAG",
    t2."DSCP",
    t2."HBINTER",
    t2."LOCIP1",
    t2."LOCIP2",
    t2."LOCPN",
    t2."LOGPORTFLAG",
    t2."MAXASSOCRETR",
    t2."MAXPATHRETR",
    t2."MTU",
    t2."PEERIP1",
    t2."PEERIP2",
    NULL,
    t2."PEERPN",
    NULL,
    t2."RTOALPHA",
    t2."RTOBETA",
    t2."RTOINIT",
    t2."RTOMAX",
    t2."RTOMIN",
    NULL,
    t2."SCTPLNKN",
    t2."SN",
    t2."SRN",
    t2."SWITCHBACKFLAG",
    t2."SWITCHBACKHBNUM",
    t2."TSACK",
    t2."VLANFLAG1",
    t2."VLANFLAG2"
FROM
huawei_mml_gsm."SCTPLNK" t2
INNER JOIN huawei_mml_gsm."SYS" t21 ON t21."FileName" = t2."FileName"

"""
)

SCTPPROF = ReplaceableObject(
    'huawei_cm_2g."SCTPPROF"',
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
    t1."CROSSIPFLAG",
    t1."HBINTER",
    t1."MAXASSOCRETR",
    t1."MAXPATHRETR",
    t1."MTU",
    t1."PEERMULTIFASTRETRANFLAG",
    t1."RTOALPHA",
    t1."RTOBETA",
    t1."RTOINIT",
    t1."RTOMAX",
    t1."RTOMIN",
    t1."SCTPPROFID",
    t1."SWITCHBACKFLAG",
    t1."SWITCHBACKHBNUM",
    t1."TSACK"
FROM
huawei_nbi_gsm."SCTPPROF" t1

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
    t2."CROSSIPFLAG",
    t2."HBINTER",
    t2."MAXASSOCRETR",
    t2."MAXPATHRETR",
    t2."MTU",
    t2."PEERMULTIFASTRETRANFLAG",
    t2."RTOALPHA",
    t2."RTOBETA",
    t2."RTOINIT",
    t2."RTOMAX",
    t2."RTOMIN",
    t2."SCTPPROFID",
    t2."SWITCHBACKFLAG",
    t2."SWITCHBACKHBNUM",
    t2."TSACK"
FROM
huawei_gexport_gsm."SCTPPROF_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CROSSIPFLAG",
    t3."HBINTER",
    t3."MAXASSOCRETR",
    t3."MAXPATHRETR",
    t3."MTU",
    t3."PEERMULTIFASTRETRANFLAG",
    t3."RTOALPHA",
    t3."RTOBETA",
    t3."RTOINIT",
    t3."RTOMAX",
    t3."RTOMIN",
    t3."SCTPPROFID",
    t3."SWITCHBACKFLAG",
    t3."SWITCHBACKHBNUM",
    t3."TSACK"
FROM
huawei_gexport_gsm."SCTPPROF_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

SCTPSRVPORT = ReplaceableObject(
    'huawei_cm_2g."SCTPSRVPORT"',
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
    t1."ABISCPSRVPN",
    t1."BBAPSRVPN",
    t1."M3UASRVPN",
    t1."NBAPSRVPN"
FROM
huawei_nbi_gsm."SCTPSRVPORT" t1

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
    t2."ABISCPSRVPN",
    t2."BBAPSRVPN",
    t2."M3UASRVPN",
    NULL
FROM
huawei_gexport_gsm."SCTPSRVPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISCPSRVPN",
    t3."BBAPSRVPN",
    t3."M3UASRVPN",
    NULL
FROM
huawei_gexport_gsm."SCTPSRVPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISCPSRVPN",
    t4."BBAPSRVPN",
    t4."M3UASRVPN",
    t4."NBAPSRVPN"
FROM
huawei_mml_gsm."SCTPSRVPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SCUPORT = ReplaceableObject(
    'huawei_cm_2g."SCUPORT"',
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
    t1."PN",
    t1."SN",
    t1."SRN",
    t1."SWITCH"
FROM
huawei_nbi_gsm."SCUPORT" t1

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
    t2."PN",
    t2."SN",
    t2."SRN",
    t2."SWITCH"
FROM
huawei_gexport_gsm."SCUPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PN",
    t3."SN",
    t3."SRN",
    t3."SWITCH"
FROM
huawei_gexport_gsm."SCUPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PN",
    t4."SN",
    t4."SRN",
    t4."SWITCH"
FROM
huawei_mml_gsm."SCUPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SGSN = ReplaceableObject(
    'huawei_cm_2g."SGSN"',
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
    t1."IPADDR1",
    t1."IPADDR2",
    t1."SGSNNAME"
FROM
huawei_nbi_gsm."SGSN" t1

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
    t2."IPADDR1",
    NULL,
    t2."SGSNNAME"
FROM
huawei_gexport_gsm."SGSN_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."IPADDR1",
    NULL,
    t3."SGSNNAME"
FROM
huawei_gexport_gsm."SGSN_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."IPADDR1",
    t4."IPADDR2",
    t4."SGSNNAME"
FROM
huawei_mml_gsm."SGSN" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SGSNNODE = ReplaceableObject(
    'huawei_cm_2g."SGSNNODE"',
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
    t1."OPNAME",
    t1."SGSNCAP",
    t1."SGSNSTATUS"
FROM
huawei_nbi_gsm."SGSNNODE" t1

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
    t2."CNID",
    t2."OPNAME",
    t2."SGSNCAP",
    t2."SGSNSTATUS"
FROM
huawei_gexport_gsm."SGSNNODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CNID",
    t3."OPNAME",
    t3."SGSNCAP",
    t3."SGSNSTATUS"
FROM
huawei_gexport_gsm."SGSNNODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CNID",
    t4."OPNAME",
    t4."SGSNCAP",
    t4."SGSNSTATUS"
FROM
huawei_mml_gsm."SGSNNODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SNTPCLTPARA = ReplaceableObject(
    'huawei_cm_2g."SNTPCLTPARA"',
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
    t1."SP"
FROM
huawei_nbi_gsm."SNTPCLTPARA" t1

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
    t2."SP"
FROM
huawei_gexport_gsm."SNTPCLTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SP"
FROM
huawei_gexport_gsm."SNTPCLTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SP"
FROM
huawei_mml_gsm."SNTPCLTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SNTPSRVINFO = ReplaceableObject(
    'huawei_cm_2g."SNTPSRVINFO"',
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
    t1."AUTHMODE",
    t1."IP",
    t1."PT"
FROM
huawei_nbi_gsm."SNTPSRVINFO" t1

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
    t2."AUTHMODE",
    t2."IP",
    t2."PT"
FROM
huawei_gexport_gsm."SNTPSRVINFO_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AUTHMODE",
    t3."IP",
    t3."PT"
FROM
huawei_gexport_gsm."SNTPSRVINFO_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AUTHMODE",
    t4."IP",
    t4."PT"
FROM
huawei_mml_gsm."SNTPSRVINFO" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SRCONPATH = ReplaceableObject(
    'huawei_cm_2g."SRCONPATH"',
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
    t1."SCPIDX",
    t1."SRN1",
    t1."SRN2",
    t1."TDMN1",
    t1."TDMN2"
FROM
huawei_nbi_gsm."SRCONPATH" t1

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
    t2."SCPIDX",
    t2."SRN1",
    t2."SRN2",
    t2."TDMN1",
    t2."TDMN2"
FROM
huawei_gexport_gsm."SRCONPATH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SCPIDX",
    t3."SRN1",
    t3."SRN2",
    t3."TDMN1",
    t3."TDMN2"
FROM
huawei_gexport_gsm."SRCONPATH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SCPIDX",
    t4."SRN1",
    t4."SRN2",
    t4."TDMN1",
    t4."TDMN2"
FROM
huawei_mml_gsm."SRCONPATH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SS7PATCHSWITCH = ReplaceableObject(
    'huawei_cm_2g."SS7PATCHSWITCH"',
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
    t1."SWITCHPARAMETER1",
    t1."SWITCHPARAMETER10",
    t1."SWITCHPARAMETER11",
    t1."SWITCHPARAMETER12",
    t1."SWITCHPARAMETER13",
    t1."SWITCHPARAMETER14",
    t1."SWITCHPARAMETER15",
    t1."SWITCHPARAMETER16",
    t1."SWITCHPARAMETER17",
    t1."SWITCHPARAMETER18",
    t1."SWITCHPARAMETER19",
    t1."SWITCHPARAMETER2",
    t1."SWITCHPARAMETER20",
    t1."SWITCHPARAMETER3",
    t1."SWITCHPARAMETER4",
    t1."SWITCHPARAMETER5",
    t1."SWITCHPARAMETER6",
    t1."SWITCHPARAMETER7",
    t1."SWITCHPARAMETER8",
    t1."SWITCHPARAMETER9"
FROM
huawei_nbi_gsm."SS7PATCHSWITCH" t1

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
    t2."SWITCHPARAMETER1",
    t2."SWITCHPARAMETER10",
    t2."SWITCHPARAMETER11",
    t2."SWITCHPARAMETER12",
    t2."SWITCHPARAMETER13",
    t2."SWITCHPARAMETER14",
    t2."SWITCHPARAMETER15",
    t2."SWITCHPARAMETER16",
    t2."SWITCHPARAMETER17",
    t2."SWITCHPARAMETER18",
    t2."SWITCHPARAMETER19",
    t2."SWITCHPARAMETER2",
    t2."SWITCHPARAMETER20",
    t2."SWITCHPARAMETER3",
    t2."SWITCHPARAMETER4",
    t2."SWITCHPARAMETER5",
    t2."SWITCHPARAMETER6",
    t2."SWITCHPARAMETER7",
    t2."SWITCHPARAMETER8",
    t2."SWITCHPARAMETER9"
FROM
huawei_gexport_gsm."SS7PATCHSWITCH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SWITCHPARAMETER1",
    t3."SWITCHPARAMETER10",
    t3."SWITCHPARAMETER11",
    t3."SWITCHPARAMETER12",
    t3."SWITCHPARAMETER13",
    t3."SWITCHPARAMETER14",
    t3."SWITCHPARAMETER15",
    t3."SWITCHPARAMETER16",
    t3."SWITCHPARAMETER17",
    t3."SWITCHPARAMETER18",
    t3."SWITCHPARAMETER19",
    t3."SWITCHPARAMETER2",
    t3."SWITCHPARAMETER20",
    t3."SWITCHPARAMETER3",
    t3."SWITCHPARAMETER4",
    t3."SWITCHPARAMETER5",
    t3."SWITCHPARAMETER6",
    t3."SWITCHPARAMETER7",
    t3."SWITCHPARAMETER8",
    t3."SWITCHPARAMETER9"
FROM
huawei_gexport_gsm."SS7PATCHSWITCH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SWITCHPARAMETER1",
    t4."SWITCHPARAMETER10",
    t4."SWITCHPARAMETER11",
    t4."SWITCHPARAMETER12",
    t4."SWITCHPARAMETER13",
    t4."SWITCHPARAMETER14",
    t4."SWITCHPARAMETER15",
    t4."SWITCHPARAMETER16",
    t4."SWITCHPARAMETER17",
    t4."SWITCHPARAMETER18",
    t4."SWITCHPARAMETER19",
    t4."SWITCHPARAMETER2",
    t4."SWITCHPARAMETER20",
    t4."SWITCHPARAMETER3",
    t4."SWITCHPARAMETER4",
    t4."SWITCHPARAMETER5",
    t4."SWITCHPARAMETER6",
    t4."SWITCHPARAMETER7",
    t4."SWITCHPARAMETER8",
    t4."SWITCHPARAMETER9"
FROM
huawei_mml_gsm."SS7PATCHSWITCH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SSLAUTHMODE = ReplaceableObject(
    'huawei_cm_2g."SSLAUTHMODE"',
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
    t1."AUTHMODE"
FROM
huawei_nbi_gsm."SSLAUTHMODE" t1

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
    t2."AUTHMODE"
FROM
huawei_gexport_gsm."SSLAUTHMODE_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."AUTHMODE"
FROM
huawei_gexport_gsm."SSLAUTHMODE_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."AUTHMODE"
FROM
huawei_mml_gsm."SSLAUTHMODE" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SSLCONF = ReplaceableObject(
    'huawei_cm_2g."SSLCONF"',
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
    t1."LOWESTCSLEVEL",
    t1."RENEGO",
    t1."RENEGOINTERVAL",
    t1."VERSION"
FROM
huawei_nbi_gsm."SSLCONF" t1

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
    t2."LOWESTCSLEVEL",
    t2."RENEGO",
    t2."RENEGOINTERVAL",
    t2."VERSION"
FROM
huawei_gexport_gsm."SSLCONF_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."LOWESTCSLEVEL",
    t3."RENEGO",
    t3."RENEGOINTERVAL",
    t3."VERSION"
FROM
huawei_gexport_gsm."SSLCONF_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."LOWESTCSLEVEL",
    t4."RENEGO",
    t4."RENEGOINTERVAL",
    NULL
FROM
huawei_mml_gsm."SSLCONF" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SSLCS = ReplaceableObject(
    'huawei_cm_2g."SSLCS"',
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
    t1."CSLEVEL",
    t1."CSNAME"
FROM
huawei_nbi_gsm."SSLCS" t1

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
    t2."CSLEVEL",
    t2."CSNAME"
FROM
huawei_gexport_gsm."SSLCS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CSLEVEL",
    t3."CSNAME"
FROM
huawei_gexport_gsm."SSLCS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CSLEVEL",
    t4."CSNAME"
FROM
huawei_mml_gsm."SSLCS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SUBNET = ReplaceableObject(
    'huawei_cm_2g."SUBNET"',
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
    t1."EXSUBNET",
    t1."SUBNET"
FROM
huawei_nbi_gsm."SUBNET" t1

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
    t2."EXSUBNET",
    t2."SUBNET"
FROM
huawei_gexport_gsm."SUBNET_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."EXSUBNET",
    t3."SUBNET"
FROM
huawei_gexport_gsm."SUBNET_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."EXSUBNET",
    t4."SUBNET"
FROM
huawei_mml_gsm."SUBNET" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SUBRACK = ReplaceableObject(
    'huawei_cm_2g."SUBRACK"',
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
    t1."CONNPWR",
    t1."SCUTYPE",
    t1."SRN",
    t1."SRNAME",
    t1."SRTTYPE",
    t1."TYPE",
    t1."WORKMODE"
FROM
huawei_nbi_gsm."SUBRACK" t1

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
    t2."CONNPWR",
    t2."SCUTYPE",
    t2."SRN",
    t2."SRNAME",
    t2."SRTTYPE",
    t2."TYPE",
    t2."WORKMODE"
FROM
huawei_gexport_gsm."SUBRACK_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CONNPWR",
    t3."SCUTYPE",
    t3."SRN",
    t3."SRNAME",
    t3."SRTTYPE",
    t3."TYPE",
    t3."WORKMODE"
FROM
huawei_gexport_gsm."SUBRACK_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CONNPWR",
    t4."SCUTYPE",
    t4."SRN",
    t4."SRNAME",
    t4."SRTTYPE",
    t4."TYPE",
    t4."WORKMODE"
FROM
huawei_mml_gsm."SUBRACK" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."CONNPWR",
    NULL,
    t5."SRN",
    t5."SRNAME",
    t5."SRTTYPE",
    NULL,
    NULL
FROM
huawei_mml_gsm."SUBRACK_MOD" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

SUBSESSION_NE = ReplaceableObject(
    'huawei_cm_2g."SUBSESSION_NE"',
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
huawei_nbi_gsm."SUBSESSION_NE" t1

"""
)

SYNSWITCH = ReplaceableObject(
    'huawei_cm_2g."SYNSWITCH"',
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
    t1."SYNSWITCH"
FROM
huawei_nbi_gsm."SYNSWITCH" t1

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
    t2."SYNSWITCH"
FROM
huawei_gexport_gsm."SYNSWITCH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."SYNSWITCH"
FROM
huawei_gexport_gsm."SYNSWITCH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."SYNSWITCH"
FROM
huawei_mml_gsm."SYNSWITCH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

SYS = ReplaceableObject(
    'huawei_cm_2g."SYS"',
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
huawei_nbi_gsm."SYS" t1

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
huawei_gexport_gsm."SYS_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
huawei_gexport_gsm."SYS_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
huawei_mml_gsm."SYS" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TCPARA = ReplaceableObject(
    'huawei_cm_2g."TCPARA"',
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
    t1."ABISUPSTRMCHECKSW",
    t1."ACLPENFLAG",
    t1."AECDEFAULTERL",
    t1."AECDETECTTHRESHOLD",
    t1."AECDETECTTIME",
    t1."AECENFLAG",
    t1."AECERLMODE",
    t1."AECFIRSTTH",
    t1."AECMODE",
    t1."AECPUREDELAY",
    t1."AECSTATLEN",
    t1."AECTAIL",
    t1."AIPCOMPHOENSW",
    t1."ALCADAPTMODE",
    t1."ALCENFLAG",
    t1."ALCFIXGAIN",
    t1."ALCFIXLEV",
    t1."ALCMAXGAIN",
    t1."ALCMAXLEV",
    t1."ALCMINLEV",
    t1."AMRHONOISEFLTSWITCH",
    t1."AMRSIDCMRSETMODE",
    t1."ANCENFLAG",
    t1."ANCMAXGAIN",
    t1."ANCSNRGATERS",
    t1."ANRBYPASSNSELEV",
    t1."ANRENFLAG",
    t1."ANRMODE",
    t1."ANRNSEREDUCTLEV",
    t1."ANRNSEREDUCTMODE",
    t1."C5SWITCH",
    t1."CSDRTPHOENSW",
    t1."DSPN",
    t1."DWCMRMODE",
    t1."ENCODEMODE",
    t1."EPLCMODE",
    t1."EPLCSWITCH",
    t1."EVADENFLAG",
    t1."FAULTDETECTSWITCH",
    t1."FORCE_LIMIT_TIME",
    t1."FRFLOWREDUCESWITCH",
    t1."G711_MODE",
    t1."HAMRTFO8P8MODSWITCH",
    t1."HRTOCSWITCH",
    t1."IDLE_CODE",
    t1."LASTWORDGETMODE",
    t1."NOISEAMPLITUDESWITCH",
    t1."NOISE_LIMIT_THRESHOLD",
    t1."PACKCONVERTMODE",
    t1."RESERVEPARA1",
    t1."RESERVEPARA2",
    t1."RESERVEPARA3",
    t1."RESERVEPARA4",
    t1."RTCPLOSTPKTHOCTRLPOLICY",
    t1."RTPJITTERTHDVAL",
    t1."RTPRTTTHDVAL",
    t1."RTPSNEXPANDOPTMODE",
    t1."RTPSNEXPANDOPTSW",
    t1."RTPSNINITIALTYPE",
    t1."RTPSTATOPTSW",
    t1."SELFHEALINGSWITCH",
    t1."SN",
    t1."SPLEVELLIMIT",
    t1."SRN",
    t1."SYNFRMWAITSWITCH",
    t1."TFOCNFFRMSENDMODE",
    t1."TFOFLOWCTRLTHREAD",
    t1."TFONEGOTIATEMSGTYPE",
    t1."TFOOPTSWITCH",
    t1."TIMEOUTRELTHD",
    t1."UPCMRCONTINUOUSSW",
    t1."VQEMODE"
FROM
huawei_nbi_gsm."TCPARA" t1

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
    t2."ABISUPSTRMCHECKSW",
    t2."ACLPENFLAG",
    t2."AECDEFAULTERL",
    t2."AECDETECTTHRESHOLD",
    t2."AECDETECTTIME",
    t2."AECENFLAG",
    t2."AECERLMODE",
    t2."AECFIRSTTH",
    t2."AECMODE",
    t2."AECPUREDELAY",
    t2."AECSTATLEN",
    t2."AECTAIL",
    t2."AIPCOMPHOENSW",
    t2."ALCADAPTMODE",
    t2."ALCENFLAG",
    t2."ALCFIXGAIN",
    t2."ALCFIXLEV",
    t2."ALCMAXGAIN",
    t2."ALCMAXLEV",
    t2."ALCMINLEV",
    t2."AMRHONOISEFLTSWITCH",
    t2."AMRSIDCMRSETMODE",
    t2."ANCENFLAG",
    t2."ANCMAXGAIN",
    t2."ANCSNRGATERS",
    t2."ANRBYPASSNSELEV",
    t2."ANRENFLAG",
    t2."ANRMODE",
    t2."ANRNSEREDUCTLEV",
    t2."ANRNSEREDUCTMODE",
    t2."C5SWITCH",
    t2."CSDRTPHOENSW",
    t2."DSPN",
    t2."DWCMRMODE",
    t2."ENCODEMODE",
    t2."EPLCMODE",
    t2."EPLCSWITCH",
    t2."EVADENFLAG",
    t2."FAULTDETECTSWITCH",
    t2."FORCE_LIMIT_TIME",
    t2."FRFLOWREDUCESWITCH",
    t2."G711_MODE",
    t2."HAMRTFO8P8MODSWITCH",
    t2."HRTOCSWITCH",
    t2."IDLE_CODE",
    t2."LASTWORDGETMODE",
    t2."NOISEAMPLITUDESWITCH",
    t2."NOISE_LIMIT_THRESHOLD",
    t2."PACKCONVERTMODE",
    t2."RESERVEPARA1",
    t2."RESERVEPARA2",
    t2."RESERVEPARA3",
    t2."RESERVEPARA4",
    t2."RTCPLOSTPKTHOCTRLPOLICY",
    t2."RTPJITTERTHDVAL",
    t2."RTPRTTTHDVAL",
    t2."RTPSNEXPANDOPTMODE",
    t2."RTPSNEXPANDOPTSW",
    t2."RTPSNINITIALTYPE",
    t2."RTPSTATOPTSW",
    NULL,
    t2."SN",
    t2."SPLEVELLIMIT",
    t2."SRN",
    t2."SYNFRMWAITSWITCH",
    t2."TFOCNFFRMSENDMODE",
    t2."TFOFLOWCTRLTHREAD",
    t2."TFONEGOTIATEMSGTYPE",
    t2."TFOOPTSWITCH",
    t2."TIMEOUTRELTHD",
    t2."UPCMRCONTINUOUSSW",
    t2."VQEMODE"
FROM
huawei_gexport_gsm."TCPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISUPSTRMCHECKSW",
    t3."ACLPENFLAG",
    t3."AECDEFAULTERL",
    t3."AECDETECTTHRESHOLD",
    t3."AECDETECTTIME",
    t3."AECENFLAG",
    t3."AECERLMODE",
    t3."AECFIRSTTH",
    t3."AECMODE",
    t3."AECPUREDELAY",
    t3."AECSTATLEN",
    t3."AECTAIL",
    t3."AIPCOMPHOENSW",
    t3."ALCADAPTMODE",
    t3."ALCENFLAG",
    t3."ALCFIXGAIN",
    t3."ALCFIXLEV",
    t3."ALCMAXGAIN",
    t3."ALCMAXLEV",
    t3."ALCMINLEV",
    t3."AMRHONOISEFLTSWITCH",
    t3."AMRSIDCMRSETMODE",
    t3."ANCENFLAG",
    t3."ANCMAXGAIN",
    t3."ANCSNRGATERS",
    t3."ANRBYPASSNSELEV",
    t3."ANRENFLAG",
    t3."ANRMODE",
    t3."ANRNSEREDUCTLEV",
    t3."ANRNSEREDUCTMODE",
    t3."C5SWITCH",
    t3."CSDRTPHOENSW",
    t3."DSPN",
    t3."DWCMRMODE",
    t3."ENCODEMODE",
    t3."EPLCMODE",
    t3."EPLCSWITCH",
    t3."EVADENFLAG",
    t3."FAULTDETECTSWITCH",
    t3."FORCE_LIMIT_TIME",
    t3."FRFLOWREDUCESWITCH",
    t3."G711_MODE",
    t3."HAMRTFO8P8MODSWITCH",
    t3."HRTOCSWITCH",
    t3."IDLE_CODE",
    t3."LASTWORDGETMODE",
    t3."NOISEAMPLITUDESWITCH",
    t3."NOISE_LIMIT_THRESHOLD",
    t3."PACKCONVERTMODE",
    t3."RESERVEPARA1",
    t3."RESERVEPARA2",
    t3."RESERVEPARA3",
    t3."RESERVEPARA4",
    t3."RTCPLOSTPKTHOCTRLPOLICY",
    t3."RTPJITTERTHDVAL",
    t3."RTPRTTTHDVAL",
    t3."RTPSNEXPANDOPTMODE",
    t3."RTPSNEXPANDOPTSW",
    t3."RTPSNINITIALTYPE",
    t3."RTPSTATOPTSW",
    NULL,
    t3."SN",
    t3."SPLEVELLIMIT",
    t3."SRN",
    t3."SYNFRMWAITSWITCH",
    t3."TFOCNFFRMSENDMODE",
    t3."TFOFLOWCTRLTHREAD",
    t3."TFONEGOTIATEMSGTYPE",
    t3."TFOOPTSWITCH",
    t3."TIMEOUTRELTHD",
    t3."UPCMRCONTINUOUSSW",
    t3."VQEMODE"
FROM
huawei_gexport_gsm."TCPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISUPSTRMCHECKSW",
    t4."ACLPENFLAG",
    t4."AECDEFAULTERL",
    t4."AECDETECTTHRESHOLD",
    t4."AECDETECTTIME",
    t4."AECENFLAG",
    t4."AECERLMODE",
    t4."AECFIRSTTH",
    t4."AECMODE",
    t4."AECPUREDELAY",
    t4."AECSTATLEN",
    t4."AECTAIL",
    t4."AIPCOMPHOENSW",
    t4."ALCADAPTMODE",
    t4."ALCENFLAG",
    t4."ALCFIXGAIN",
    t4."ALCFIXLEV",
    t4."ALCMAXGAIN",
    t4."ALCMAXLEV",
    t4."ALCMINLEV",
    t4."AMRHONOISEFLTSWITCH",
    t4."AMRSIDCMRSETMODE",
    t4."ANCENFLAG",
    t4."ANCMAXGAIN",
    t4."ANCSNRGATERS",
    t4."ANRBYPASSNSELEV",
    t4."ANRENFLAG",
    t4."ANRMODE",
    t4."ANRNSEREDUCTLEV",
    t4."ANRNSEREDUCTMODE",
    t4."C5SWITCH",
    t4."CSDRTPHOENSW",
    t4."DSPN",
    t4."DWCMRMODE",
    t4."ENCODEMODE",
    t4."EPLCMODE",
    t4."EPLCSWITCH",
    t4."EVADENFLAG",
    t4."FAULTDETECTSWITCH",
    t4."FORCE_LIMIT_TIME",
    t4."FRFLOWREDUCESWITCH",
    t4."G711_MODE",
    t4."HAMRTFO8P8MODSWITCH",
    t4."HRTOCSWITCH",
    t4."IDLE_CODE",
    t4."LASTWORDGETMODE",
    t4."NOISEAMPLITUDESWITCH",
    t4."NOISE_LIMIT_THRESHOLD",
    t4."PACKCONVERTMODE",
    t4."RESERVEPARA1",
    t4."RESERVEPARA2",
    t4."RESERVEPARA3",
    t4."RESERVEPARA4",
    t4."RTCPLOSTPKTHOCTRLPOLICY",
    t4."RTPJITTERTHDVAL",
    t4."RTPRTTTHDVAL",
    t4."RTPSNEXPANDOPTMODE",
    t4."RTPSNEXPANDOPTSW",
    t4."RTPSNINITIALTYPE",
    t4."RTPSTATOPTSW",
    NULL,
    t4."SN",
    t4."SPLEVELLIMIT",
    t4."SRN",
    t4."SYNFRMWAITSWITCH",
    t4."TFOCNFFRMSENDMODE",
    t4."TFOFLOWCTRLTHREAD",
    t4."TFONEGOTIATEMSGTYPE",
    t4."TFOOPTSWITCH",
    t4."TIMEOUTRELTHD",
    t4."UPCMRCONTINUOUSSW",
    t4."VQEMODE"
FROM
huawei_mml_gsm."TCPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TCRSVPARA = ReplaceableObject(
    'huawei_cm_2g."TCRSVPARA"',
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
    t1."TCRESERVEPARA1",
    t1."TCRESERVEPARA10",
    t1."TCRESERVEPARA11",
    t1."TCRESERVEPARA12",
    t1."TCRESERVEPARA13",
    t1."TCRESERVEPARA14",
    t1."TCRESERVEPARA2",
    t1."TCRESERVEPARA3",
    t1."TCRESERVEPARA4",
    t1."TCRESERVEPARA5",
    t1."TCRESERVEPARA6",
    t1."TCRESERVEPARA7",
    t1."TCRESERVEPARA8",
    t1."TCRESERVEPARA9"
FROM
huawei_nbi_gsm."TCRSVPARA" t1

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
    t2."TCRESERVEPARA10",
    t2."TCRESERVEPARA11",
    t2."TCRESERVEPARA12",
    t2."TCRESERVEPARA13",
    t2."TCRESERVEPARA14",
    t2."TCRESERVEPARA2",
    NULL,
    NULL,
    NULL,
    t2."TCRESERVEPARA6",
    t2."TCRESERVEPARA7",
    t2."TCRESERVEPARA8",
    t2."TCRESERVEPARA9"
FROM
huawei_gexport_gsm."TCRSVPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."TCRESERVEPARA10",
    t3."TCRESERVEPARA11",
    t3."TCRESERVEPARA12",
    t3."TCRESERVEPARA13",
    t3."TCRESERVEPARA14",
    t3."TCRESERVEPARA2",
    NULL,
    NULL,
    NULL,
    t3."TCRESERVEPARA6",
    t3."TCRESERVEPARA7",
    t3."TCRESERVEPARA8",
    t3."TCRESERVEPARA9"
FROM
huawei_gexport_gsm."TCRSVPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TCRESERVEPARA10",
    t4."TCRESERVEPARA11",
    t4."TCRESERVEPARA12",
    t4."TCRESERVEPARA13",
    t4."TCRESERVEPARA14",
    t4."TCRESERVEPARA2",
    NULL,
    NULL,
    NULL,
    t4."TCRESERVEPARA6",
    t4."TCRESERVEPARA7",
    t4."TCRESERVEPARA8",
    t4."TCRESERVEPARA9"
FROM
huawei_mml_gsm."TCRSVPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TNALMPARA = ReplaceableObject(
    'huawei_cm_2g."TNALMPARA"',
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
    t1."ALLOCTIMESPERPERIOD",
    t1."ALMCNTPERIOD",
    t1."ALMSWITCH",
    t1."FAULTTYPE",
    t1."KPIALMCLRTHD",
    t1."KPIALMTHD"
FROM
huawei_nbi_gsm."TNALMPARA" t1

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
    t2."ALLOCTIMESPERPERIOD",
    t2."ALMCNTPERIOD",
    t2."ALMSWITCH",
    t2."FAULTTYPE",
    t2."KPIALMCLRTHD",
    t2."KPIALMTHD"
FROM
huawei_gexport_gsm."TNALMPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ALLOCTIMESPERPERIOD",
    t3."ALMCNTPERIOD",
    t3."ALMSWITCH",
    t3."FAULTTYPE",
    t3."KPIALMCLRTHD",
    t3."KPIALMTHD"
FROM
huawei_gexport_gsm."TNALMPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ALLOCTIMESPERPERIOD",
    t4."ALMCNTPERIOD",
    t4."ALMSWITCH",
    t4."FAULTTYPE",
    t4."KPIALMCLRTHD",
    t4."KPIALMTHD"
FROM
huawei_mml_gsm."TNALMPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TNLOADBALANCEPARA = ReplaceableObject(
    'huawei_cm_2g."TNLOADBALANCEPARA"',
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
    t1."INTLOADDIFFTH",
    t1."INTLOADSHARETH",
    t1."INTPINGLOSTPKTPRITH",
    t1."INTSRLOADCOMPENSATETH",
    t1."INTSRLOADHOPSCOMPENSATETH",
    t1."MPULOADDIFFTH",
    t1."MPULOADDIFFTIMETH",
    t1."MPULOADSHARETH"
FROM
huawei_nbi_gsm."TNLOADBALANCEPARA" t1

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
    t2."INTLOADDIFFTH",
    t2."INTLOADSHARETH",
    t2."INTPINGLOSTPKTPRITH",
    t2."INTSRLOADCOMPENSATETH",
    t2."INTSRLOADHOPSCOMPENSATETH",
    t2."MPULOADDIFFTH",
    t2."MPULOADDIFFTIMETH",
    t2."MPULOADSHARETH"
FROM
huawei_gexport_gsm."TNLOADBALANCEPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."INTLOADDIFFTH",
    t3."INTLOADSHARETH",
    t3."INTPINGLOSTPKTPRITH",
    t3."INTSRLOADCOMPENSATETH",
    t3."INTSRLOADHOPSCOMPENSATETH",
    t3."MPULOADDIFFTH",
    t3."MPULOADDIFFTIMETH",
    t3."MPULOADSHARETH"
FROM
huawei_gexport_gsm."TNLOADBALANCEPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."INTLOADDIFFTH",
    t4."INTLOADSHARETH",
    t4."INTPINGLOSTPKTPRITH",
    t4."INTSRLOADCOMPENSATETH",
    t4."INTSRLOADHOPSCOMPENSATETH",
    t4."MPULOADDIFFTH",
    t4."MPULOADDIFFTIMETH",
    t4."MPULOADSHARETH"
FROM
huawei_mml_gsm."TNLOADBALANCEPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TNRSVDPARA = ReplaceableObject(
    'huawei_cm_2g."TNRSVDPARA"',
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
    t1."RSVDPARA3",
    t1."RSVDPARA4",
    t1."RSVDPARA5",
    t1."RSVDPARA6",
    t1."RSVDPARA7",
    t1."RSVDPARA8",
    t1."RSVDSW1",
    t1."RSVDSW2",
    t1."RSVDSW3"
FROM
huawei_nbi_gsm."TNRSVDPARA" t1

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
    t2."RSVDPARA3",
    t2."RSVDPARA4",
    t2."RSVDPARA5",
    t2."RSVDPARA6",
    t2."RSVDPARA7",
    t2."RSVDPARA8",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."TNRSVDPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."RSVDPARA3",
    t3."RSVDPARA4",
    t3."RSVDPARA5",
    t3."RSVDPARA6",
    t3."RSVDPARA7",
    t3."RSVDPARA8",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."TNRSVDPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."RSVDPARA3",
    t4."RSVDPARA4",
    t4."RSVDPARA5",
    t4."RSVDPARA6",
    t4."RSVDPARA7",
    t4."RSVDPARA8",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."TNRSVDPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TNSOFTPARA = ReplaceableObject(
    'huawei_cm_2g."TNSOFTPARA"',
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
    t1."ABISIPBALANCESWITCH",
    t1."ABISIPPREEMTOPTISW",
    t1."ABISMUXOPTISW",
    t1."ABISPATHFAULTPOLICY",
    t1."ABISUDPPINGFAULTPOLICY",
    t1."ACCANDCRFCSW",
    t1."ACREFCONGFCSW",
    t1."ADPCCONGFCSW",
    t1."APATHFAULTPOLICY",
    t1."ATERSLRELIABILITYSW",
    t1."AUTOFLOWSTATPKTINTRVL",
    t1."AUTOFLOWSTATSW",
    t1."CCCRRATIOTHRD",
    t1."CRMINNUM",
    t1."DIAGNOSESCTPFAULT",
    t1."DIPAGEDTIME",
    t1."DPUTOPTSCHKSW",
    t1."DSIDFLOWCTRLSWITCH",
    t1."EMERGENCYCALLADMITSW",
    t1."FCONITFBRD",
    t1."GLOBALALARMDELAYTIMER",
    t1."GLOBALALARMLOCPARASW",
    t1."INTBRDESTTHRD",
    t1."INTFCPERIOD",
    t1."INTFCTHRD",
    t1."IPPATHITFBOARDLOADSHARESW",
    t1."IURGPATHFAULTPOLICY",
    t1."LAPDAUTOTRACESWITCH",
    t1."LAPDDETECTBYERRPKGSW",
    t1."LAPDINTBRDPROTECTTIME",
    t1."LAPDOUTOFORDERPKTPROCPOL",
    t1."LAPDPORTPROTECTTIME",
    t1."LAPDRESUMEBYLOOP",
    t1."LINKRESELUNCONGDELAYTIMER",
    t1."M3UAFCSW",
    t1."M3UALOADOPTISW",
    t1."MAXCREFCONGFCLV",
    t1."MTP2RESUMESWITCH",
    t1."MTP3FCSW",
    t1."MTP3LOADOPTISW",
    t1."MTP3TXRATECONTROLSWITCH",
    t1."MTP3TXRATEFCSWITCH",
    t1."POOLIPPATHPINGFAULTALGOSW",
    t1."SCTPAUTOTRACESWITCH",
    t1."SCTPCONGCTRL",
    t1."SCTPPATHCHOVSW",
    t1."SCTPRECVFC",
    t1."SCTPRESUMEBYLOOP",
    t1."SCTPRWNDNONZEROSDSACKSW",
    t1."SCTPSENDFC",
    t1."SCTPSPAGINGTIME",
    t1."SCTPSPFCTHRD",
    t1."SCTPSPFILTERTIME",
    t1."SCTPSPPSFCTHRD",
    t1."SCTPSPPUNISHTIME",
    t1."SCTPSPUPTHRD",
    t1."SRCONPATHCHECKSW",
    t1."SRCONPATHCHECKSWITCH",
    t1."STORMCHECKSW",
    t1."TDMFLTDIAGSWITCH",
    t1."TDMINFTOPTSCHKSW",
    t1."TDMTSCONAUDITSW",
    t1."TNAPPDATAAUDITSWITCH"
FROM
huawei_nbi_gsm."TNSOFTPARA" t1

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
    t2."ABISIPBALANCESWITCH",
    t2."ABISIPPREEMTOPTISW",
    t2."ABISMUXOPTISW",
    t2."ABISPATHFAULTPOLICY",
    t2."ABISUDPPINGFAULTPOLICY",
    t2."ACCANDCRFCSW",
    t2."ACREFCONGFCSW",
    t2."ADPCCONGFCSW",
    t2."APATHFAULTPOLICY",
    t2."ATERSLRELIABILITYSW",
    t2."AUTOFLOWSTATPKTINTRVL",
    t2."AUTOFLOWSTATSW",
    t2."CCCRRATIOTHRD",
    t2."CRMINNUM",
    t2."DIAGNOSESCTPFAULT",
    t2."DIPAGEDTIME",
    t2."DPUTOPTSCHKSW",
    t2."DSIDFLOWCTRLSWITCH",
    t2."EMERGENCYCALLADMITSW",
    t2."FCONITFBRD",
    t2."GLOBALALARMDELAYTIMER",
    t2."GLOBALALARMLOCPARASW",
    t2."INTBRDESTTHRD",
    t2."INTFCPERIOD",
    t2."INTFCTHRD",
    t2."IPPATHITFBOARDLOADSHARESW",
    t2."IURGPATHFAULTPOLICY",
    t2."LAPDAUTOTRACESWITCH",
    t2."LAPDDETECTBYERRPKGSW",
    t2."LAPDINTBRDPROTECTTIME",
    t2."LAPDOUTOFORDERPKTPROCPOL",
    t2."LAPDPORTPROTECTTIME",
    t2."LAPDRESUMEBYLOOP",
    t2."LINKRESELUNCONGDELAYTIMER",
    t2."M3UAFCSW",
    t2."M3UALOADOPTISW",
    t2."MAXCREFCONGFCLV",
    t2."MTP2RESUMESWITCH",
    t2."MTP3FCSW",
    t2."MTP3LOADOPTISW",
    t2."MTP3TXRATECONTROLSWITCH",
    t2."MTP3TXRATEFCSWITCH",
    t2."POOLIPPATHPINGFAULTALGOSW",
    t2."SCTPAUTOTRACESWITCH",
    t2."SCTPCONGCTRL",
    t2."SCTPPATHCHOVSW",
    t2."SCTPRECVFC",
    t2."SCTPRESUMEBYLOOP",
    t2."SCTPRWNDNONZEROSDSACKSW",
    t2."SCTPSENDFC",
    t2."SCTPSPAGINGTIME",
    t2."SCTPSPFCTHRD",
    t2."SCTPSPFILTERTIME",
    t2."SCTPSPPSFCTHRD",
    t2."SCTPSPPUNISHTIME",
    t2."SCTPSPUPTHRD",
    t2."SRCONPATHCHECKSW",
    t2."SRCONPATHCHECKSWITCH",
    NULL,
    t2."TDMFLTDIAGSWITCH",
    t2."TDMINFTOPTSCHKSW",
    t2."TDMTSCONAUDITSW",
    t2."TNAPPDATAAUDITSWITCH"
FROM
huawei_gexport_gsm."TNSOFTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ABISIPBALANCESWITCH",
    t3."ABISIPPREEMTOPTISW",
    t3."ABISMUXOPTISW",
    t3."ABISPATHFAULTPOLICY",
    t3."ABISUDPPINGFAULTPOLICY",
    t3."ACCANDCRFCSW",
    t3."ACREFCONGFCSW",
    t3."ADPCCONGFCSW",
    t3."APATHFAULTPOLICY",
    t3."ATERSLRELIABILITYSW",
    t3."AUTOFLOWSTATPKTINTRVL",
    t3."AUTOFLOWSTATSW",
    t3."CCCRRATIOTHRD",
    t3."CRMINNUM",
    t3."DIAGNOSESCTPFAULT",
    t3."DIPAGEDTIME",
    t3."DPUTOPTSCHKSW",
    t3."DSIDFLOWCTRLSWITCH",
    t3."EMERGENCYCALLADMITSW",
    t3."FCONITFBRD",
    t3."GLOBALALARMDELAYTIMER",
    t3."GLOBALALARMLOCPARASW",
    t3."INTBRDESTTHRD",
    t3."INTFCPERIOD",
    t3."INTFCTHRD",
    t3."IPPATHITFBOARDLOADSHARESW",
    t3."IURGPATHFAULTPOLICY",
    t3."LAPDAUTOTRACESWITCH",
    t3."LAPDDETECTBYERRPKGSW",
    t3."LAPDINTBRDPROTECTTIME",
    t3."LAPDOUTOFORDERPKTPROCPOL",
    t3."LAPDPORTPROTECTTIME",
    t3."LAPDRESUMEBYLOOP",
    t3."LINKRESELUNCONGDELAYTIMER",
    t3."M3UAFCSW",
    t3."M3UALOADOPTISW",
    t3."MAXCREFCONGFCLV",
    t3."MTP2RESUMESWITCH",
    t3."MTP3FCSW",
    t3."MTP3LOADOPTISW",
    t3."MTP3TXRATECONTROLSWITCH",
    t3."MTP3TXRATEFCSWITCH",
    t3."POOLIPPATHPINGFAULTALGOSW",
    t3."SCTPAUTOTRACESWITCH",
    t3."SCTPCONGCTRL",
    t3."SCTPPATHCHOVSW",
    t3."SCTPRECVFC",
    t3."SCTPRESUMEBYLOOP",
    t3."SCTPRWNDNONZEROSDSACKSW",
    t3."SCTPSENDFC",
    t3."SCTPSPAGINGTIME",
    t3."SCTPSPFCTHRD",
    t3."SCTPSPFILTERTIME",
    t3."SCTPSPPSFCTHRD",
    t3."SCTPSPPUNISHTIME",
    t3."SCTPSPUPTHRD",
    t3."SRCONPATHCHECKSW",
    t3."SRCONPATHCHECKSWITCH",
    NULL,
    t3."TDMFLTDIAGSWITCH",
    t3."TDMINFTOPTSCHKSW",
    t3."TDMTSCONAUDITSW",
    t3."TNAPPDATAAUDITSWITCH"
FROM
huawei_gexport_gsm."TNSOFTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ABISIPBALANCESWITCH",
    t4."ABISIPPREEMTOPTISW",
    t4."ABISMUXOPTISW",
    t4."ABISPATHFAULTPOLICY",
    t4."ABISUDPPINGFAULTPOLICY",
    t4."ACCANDCRFCSW",
    t4."ACREFCONGFCSW",
    t4."ADPCCONGFCSW",
    t4."APATHFAULTPOLICY",
    t4."ATERSLRELIABILITYSW",
    t4."AUTOFLOWSTATPKTINTRVL",
    t4."AUTOFLOWSTATSW",
    t4."CCCRRATIOTHRD",
    t4."CRMINNUM",
    t4."DIAGNOSESCTPFAULT",
    t4."DIPAGEDTIME",
    t4."DPUTOPTSCHKSW",
    t4."DSIDFLOWCTRLSWITCH",
    t4."EMERGENCYCALLADMITSW",
    t4."FCONITFBRD",
    t4."GLOBALALARMDELAYTIMER",
    t4."GLOBALALARMLOCPARASW",
    t4."INTBRDESTTHRD",
    t4."INTFCPERIOD",
    t4."INTFCTHRD",
    t4."IPPATHITFBOARDLOADSHARESW",
    t4."IURGPATHFAULTPOLICY",
    t4."LAPDAUTOTRACESWITCH",
    t4."LAPDDETECTBYERRPKGSW",
    t4."LAPDINTBRDPROTECTTIME",
    t4."LAPDOUTOFORDERPKTPROCPOL",
    t4."LAPDPORTPROTECTTIME",
    t4."LAPDRESUMEBYLOOP",
    t4."LINKRESELUNCONGDELAYTIMER",
    t4."M3UAFCSW",
    t4."M3UALOADOPTISW",
    t4."MAXCREFCONGFCLV",
    t4."MTP2RESUMESWITCH",
    t4."MTP3FCSW",
    t4."MTP3LOADOPTISW",
    t4."MTP3TXRATECONTROLSWITCH",
    t4."MTP3TXRATEFCSWITCH",
    t4."POOLIPPATHPINGFAULTALGOSW",
    t4."SCTPAUTOTRACESWITCH",
    t4."SCTPCONGCTRL",
    t4."SCTPPATHCHOVSW",
    t4."SCTPRECVFC",
    t4."SCTPRESUMEBYLOOP",
    t4."SCTPRWNDNONZEROSDSACKSW",
    t4."SCTPSENDFC",
    t4."SCTPSPAGINGTIME",
    t4."SCTPSPFCTHRD",
    t4."SCTPSPFILTERTIME",
    t4."SCTPSPPSFCTHRD",
    t4."SCTPSPPUNISHTIME",
    t4."SCTPSPUPTHRD",
    t4."SRCONPATHCHECKSW",
    t4."SRCONPATHCHECKSWITCH",
    NULL,
    t4."TDMFLTDIAGSWITCH",
    t4."TDMINFTOPTSCHKSW",
    t4."TDMTSCONAUDITSW",
    t4."TNAPPDATAAUDITSWITCH"
FROM
huawei_mml_gsm."TNSOFTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TRANSPATCHPARA = ReplaceableObject(
    'huawei_cm_2g."TRANSPATCHPARA"',
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
    t1."RSVDPARA1",
    t1."RSVDPARA10",
    t1."RSVDPARA11",
    t1."RSVDPARA12",
    t1."RSVDPARA13",
    t1."RSVDPARA14",
    t1."RSVDPARA15",
    t1."RSVDPARA2",
    t1."RSVDPARA3",
    t1."RSVDPARA4",
    t1."RSVDPARA5",
    t1."RSVDPARA6",
    t1."RSVDPARA7",
    t1."RSVDPARA8",
    t1."RSVDPARA9",
    t1."SRN"
FROM
huawei_nbi_gsm."TRANSPATCHPARA" t1

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
    t2."RSVDPARA1",
    t2."RSVDPARA10",
    t2."RSVDPARA11",
    t2."RSVDPARA12",
    t2."RSVDPARA13",
    t2."RSVDPARA14",
    t2."RSVDPARA15",
    t2."RSVDPARA2",
    t2."RSVDPARA3",
    t2."RSVDPARA4",
    t2."RSVDPARA5",
    t2."RSVDPARA6",
    t2."RSVDPARA7",
    t2."RSVDPARA8",
    t2."RSVDPARA9",
    t2."SRN"
FROM
huawei_gexport_gsm."TRANSPATCHPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."RSVDPARA1",
    t3."RSVDPARA10",
    t3."RSVDPARA11",
    t3."RSVDPARA12",
    t3."RSVDPARA13",
    t3."RSVDPARA14",
    t3."RSVDPARA15",
    t3."RSVDPARA2",
    t3."RSVDPARA3",
    t3."RSVDPARA4",
    t3."RSVDPARA5",
    t3."RSVDPARA6",
    t3."RSVDPARA7",
    t3."RSVDPARA8",
    t3."RSVDPARA9",
    t3."SRN"
FROM
huawei_gexport_gsm."TRANSPATCHPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."RSVDPARA1",
    t4."RSVDPARA10",
    t4."RSVDPARA11",
    t4."RSVDPARA12",
    t4."RSVDPARA13",
    t4."RSVDPARA14",
    t4."RSVDPARA15",
    t4."RSVDPARA2",
    t4."RSVDPARA3",
    t4."RSVDPARA4",
    t4."RSVDPARA5",
    t4."RSVDPARA6",
    t4."RSVDPARA7",
    t4."RSVDPARA8",
    t4."RSVDPARA9",
    t4."SRN"
FROM
huawei_mml_gsm."TRANSPATCHPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TRANSPHYLNKPARA = ReplaceableObject(
    'huawei_cm_2g."TRANSPHYLNKPARA"',
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
    t1."ACTSTBYCONSCHKSW",
    t1."ARPDELAYAGINGSW",
    t1."AUTOTRCIPPKTCAPSW",
    t1."SIPMATCHDETECTSW",
    t1."TNUPORTTSCHKSW"
FROM
huawei_nbi_gsm."TRANSPHYLNKPARA" t1

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
    t2."ACTSTBYCONSCHKSW",
    t2."ARPDELAYAGINGSW",
    t2."AUTOTRCIPPKTCAPSW",
    t2."SIPMATCHDETECTSW",
    t2."TNUPORTTSCHKSW"
FROM
huawei_gexport_gsm."TRANSPHYLNKPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ACTSTBYCONSCHKSW",
    t3."ARPDELAYAGINGSW",
    t3."AUTOTRCIPPKTCAPSW",
    t3."SIPMATCHDETECTSW",
    t3."TNUPORTTSCHKSW"
FROM
huawei_gexport_gsm."TRANSPHYLNKPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ACTSTBYCONSCHKSW",
    t4."ARPDELAYAGINGSW",
    t4."AUTOTRCIPPKTCAPSW",
    t4."SIPMATCHDETECTSW",
    t4."TNUPORTTSCHKSW"
FROM
huawei_mml_gsm."TRANSPHYLNKPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TRANSRSVPARA = ReplaceableObject(
    'huawei_cm_2g."TRANSRSVPARA"',
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
    t1."RSVDPARA1",
    t1."RSVDPARA2",
    t1."RSVDPARA3",
    t1."RSVDPARA4",
    t1."RSVDPARA5",
    t1."RSVDPARA6",
    t1."RSVDSW1",
    t1."RSVDSW2",
    t1."RSVDSW3"
FROM
huawei_nbi_gsm."TRANSRSVPARA" t1

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
    t2."RSVDPARA1",
    t2."RSVDPARA2",
    t2."RSVDPARA3",
    t2."RSVDPARA4",
    t2."RSVDPARA5",
    t2."RSVDPARA6",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."TRANSRSVPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."RSVDPARA1",
    t3."RSVDPARA2",
    t3."RSVDPARA3",
    t3."RSVDPARA4",
    t3."RSVDPARA5",
    t3."RSVDPARA6",
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."TRANSRSVPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."RSVDPARA1",
    t4."RSVDPARA2",
    t4."RSVDPARA3",
    t4."RSVDPARA4",
    t4."RSVDPARA5",
    t4."RSVDPARA6",
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."TRANSRSVPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TRCLOGSPD = ReplaceableObject(
    'huawei_cm_2g."TRCLOGSPD"',
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
    t1."TRCSPD"
FROM
huawei_nbi_gsm."TRCLOGSPD" t1

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
    t2."TRCSPD"
FROM
huawei_gexport_gsm."TRCLOGSPD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."TRCSPD"
FROM
huawei_gexport_gsm."TRCLOGSPD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."TRCSPD"
FROM
huawei_mml_gsm."TRCLOGSPD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TRMFACTOR = ReplaceableObject(
    'huawei_cm_2g."TRMFACTOR"',
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
    t1."CSDATADL",
    t1."CSDATAUL",
    t1."CSVOICEDL",
    t1."CSVOICEUL",
    t1."FTI",
    t1."PSDATADL",
    t1."PSDATAUL",
    t1."REMARK"
FROM
huawei_nbi_gsm."TRMFACTOR" t1

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
    t2."CSDATADL",
    t2."CSDATAUL",
    t2."CSVOICEDL",
    t2."CSVOICEUL",
    t2."FTI",
    t2."PSDATADL",
    t2."PSDATAUL",
    t2."REMARK"
FROM
huawei_gexport_gsm."TRMFACTOR_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CSDATADL",
    t3."CSDATAUL",
    t3."CSVOICEDL",
    t3."CSVOICEUL",
    t3."FTI",
    t3."PSDATADL",
    t3."PSDATAUL",
    t3."REMARK"
FROM
huawei_gexport_gsm."TRMFACTOR_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CSDATADL",
    t4."CSDATAUL",
    t4."CSVOICEDL",
    t4."CSVOICEUL",
    t4."FTI",
    t4."PSDATADL",
    t4."PSDATAUL",
    t4."REMARK"
FROM
huawei_mml_gsm."TRMFACTOR" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."CSDATADL",
    t5."CSDATAUL",
    t5."CSVOICEDL",
    t5."CSVOICEUL",
    t5."FTI",
    t5."PSDATADL",
    t5."PSDATAUL",
    t5."REMARK"
FROM
huawei_mml_gsm."TRMFACTOR_MOD" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

TRMLOADTH = ReplaceableObject(
    'huawei_cm_2g."TRMLOADTH"',
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
    t1."GSMCSBWRATE",
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
    t1."FWDRESVHOTH",
    t1."TDMCONGCLRTH",
    t1."TDMCONGTH"
FROM
huawei_nbi_gsm."TRMLOADTH" t1

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
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t2."GSMCSBWRATE",
    NULL,
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
    t2."FWDRESVHOTH",
    NULL,
    NULL
FROM
huawei_gexport_gsm."TRMLOADTH_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    t3."GSMCSBWRATE",
    NULL,
    t3."TRANST",
    t3."TRMLOADTHINDEX",
    t3."BWDCONGCLRTH",
    t3."BWDCONGTH",
    t3."BWDOVLDCLRTH",
    t3."BWDOVLDTH",
    t3."BWDRESVHOTH",
    t3."FWDCONGCLRTH",
    t3."FWDCONGTH",
    t3."FWDOVLDCLRTH",
    t3."FWDOVLDTH",
    t3."FWDRESVHOTH",
    NULL,
    NULL
FROM
huawei_gexport_gsm."TRMLOADTH_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."GSMCSBWRATE",
    NULL,
    t4."TRANST",
    t4."TRMLOADTHINDEX",
    t4."BWDCONGCLRTH",
    t4."BWDCONGTH",
    t4."BWDOVLDCLRTH",
    t4."BWDOVLDTH",
    t4."BWDRESVHOTH",
    t4."FWDCONGCLRTH",
    t4."FWDCONGTH",
    t4."FWDOVLDCLRTH",
    t4."FWDOVLDTH",
    t4."FWDRESVHOTH",
    NULL,
    NULL
FROM
huawei_mml_gsm."TRMLOADTH" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TRMMAP = ReplaceableObject(
    'huawei_cm_2g."TRMMAP"',
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
    t1."CSDATAPRI",
    t1."CSVOICEPRI",
    t1."ITFT",
    t1."PSHPRIDATAPRI",
    t1."PSLPRIDATAPRI",
    t1."REMARK",
    t1."TMI",
    t1."TRANST",
    t1."CSDATAPATH",
    t1."CSVOICEPATH",
    t1."PSHPRIDATAPATH",
    t1."PSLPRIDATAPATH"
FROM
huawei_nbi_gsm."TRMMAP" t1

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
    t2."CSDATAPRI",
    t2."CSVOICEPRI",
    t2."ITFT",
    t2."PSHPRIDATAPRI",
    t2."PSLPRIDATAPRI",
    t2."REMARK",
    t2."TMI",
    t2."TRANST",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."TRMMAP_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CSDATAPRI",
    t3."CSVOICEPRI",
    t3."ITFT",
    t3."PSHPRIDATAPRI",
    t3."PSLPRIDATAPRI",
    t3."REMARK",
    t3."TMI",
    t3."TRANST",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_gexport_gsm."TRMMAP_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ITFT",
    NULL,
    NULL,
    t4."REMARK",
    t4."TMI",
    NULL,
    t4."CSDATAPATH",
    t4."CSVOICEPATH",
    NULL,
    NULL
FROM
huawei_mml_gsm."TRMMAP" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    t5."CSDATAPRI",
    t5."CSVOICEPRI",
    t5."ITFT",
    t5."PSHPRIDATAPRI",
    t5."PSLPRIDATAPRI",
    t5."REMARK",
    t5."TMI",
    t5."TRANST",
    NULL,
    NULL,
    NULL,
    NULL
FROM
huawei_mml_gsm."TRMMAP_MOD" t5
INNER JOIN huawei_mml_gsm."SYS" t51 ON t51."FileName" = t5."FileName"

"""
)

TRUSTCERT = ReplaceableObject(
    'huawei_cm_2g."TRUSTCERT"',
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
    t1."CERTNAME"
FROM
huawei_nbi_gsm."TRUSTCERT" t1

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
    t2."CERTNAME"
FROM
huawei_gexport_gsm."TRUSTCERT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CERTNAME"
FROM
huawei_gexport_gsm."TRUSTCERT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

TRXBIND2PHYBRD = ReplaceableObject(
    'huawei_cm_2g."TRXBIND2PHYBRD"',
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
    t1."ANTPASSNO",
    t1."BTSID",
    t1."CN",
    t1."SN",
    t1."SRN",
    t1."TRXID",
    t1."TRXPN",
    t1."TRXTP"
FROM
huawei_nbi_gsm."TRXBIND2PHYBRD" t1

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
    t2."ANTPASSNO",
    t2."BTSID",
    t2."CN",
    t2."SN",
    t2."SRN",
    t2."TRXID",
    t2."TRXPN",
    t2."TRXTP"
FROM
huawei_gexport_gsm."TRXBIND2PHYBRD_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."ANTPASSNO",
    t3."BTSID",
    t3."CN",
    t3."SN",
    t3."SRN",
    t3."TRXID",
    t3."TRXPN",
    t3."TRXTP"
FROM
huawei_gexport_gsm."TRXBIND2PHYBRD_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."ANTPASSNO",
    t4."BTSID",
    t4."CN",
    t4."SN",
    t4."SRN",
    t4."TRXID",
    t4."TRXPN",
    t4."TRXTP"
FROM
huawei_mml_gsm."TRXBIND2PHYBRD" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

TZ = ReplaceableObject(
    'huawei_cm_2g."TZ"',
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
    t1."CMETO",
    t1."DST",
    t1."EM",
    t1."EMONTH",
    t1."ET",
    t1."EWEEK",
    t1."EWSEQ",
    t1."SM",
    t1."SMONTH",
    t1."ST",
    t1."SWEEK",
    t1."SWSEQ",
    t1."ZONET"
FROM
huawei_nbi_gsm."TZ" t1

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
    t2."DST",
    t2."EM",
    t2."EMONTH",
    t2."ET",
    NULL,
    NULL,
    t2."SM",
    t2."SMONTH",
    t2."ST",
    NULL,
    NULL,
    t2."ZONET"
FROM
huawei_gexport_gsm."TZ_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."DST",
    t3."EM",
    t3."EMONTH",
    t3."ET",
    NULL,
    NULL,
    t3."SM",
    t3."SMONTH",
    t3."ST",
    NULL,
    NULL,
    t3."ZONET"
FROM
huawei_gexport_gsm."TZ_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."DST",
    t4."EM",
    t4."EMONTH",
    t4."ET",
    NULL,
    NULL,
    t4."SM",
    t4."SMONTH",
    t4."ST",
    NULL,
    NULL,
    t4."ZONET"
FROM
huawei_mml_gsm."TZ" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

UMTESTPARA = ReplaceableObject(
    'huawei_cm_2g."UMTESTPARA"',
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
    t1."UMTSTCELL",
    t1."UMTSTCHNNO",
    t1."UMTSTMSISDN",
    t1."UMTSTSITE",
    t1."UMTSTTRXID"
FROM
huawei_nbi_gsm."UMTESTPARA" t1

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
    t2."UMTSTCELL",
    NULL,
    NULL,
    t2."UMTSTSITE",
    t2."UMTSTTRXID"
FROM
huawei_gexport_gsm."UMTESTPARA_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."UMTSTCELL",
    NULL,
    NULL,
    t3."UMTSTSITE",
    t3."UMTSTTRXID"
FROM
huawei_gexport_gsm."UMTESTPARA_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."UMTSTCELL",
    NULL,
    t4."UMTSTMSISDN",
    t4."UMTSTSITE",
    t4."UMTSTTRXID"
FROM
huawei_mml_gsm."UMTESTPARA" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

USEREVTRTNPOLICY = ReplaceableObject(
    'huawei_cm_2g."USEREVTRTNPOLICY"',
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
    t1."CALLLOGDELPERIOD",
    t1."TRACEDELPERIOD"
FROM
huawei_nbi_gsm."USEREVTRTNPOLICY" t1

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
    t2."CALLLOGDELPERIOD",
    t2."TRACEDELPERIOD"
FROM
huawei_gexport_gsm."USEREVTRTNPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."CALLLOGDELPERIOD",
    t3."TRACEDELPERIOD"
FROM
huawei_gexport_gsm."USEREVTRTNPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."CALLLOGDELPERIOD",
    t4."TRACEDELPERIOD"
FROM
huawei_mml_gsm."USEREVTRTNPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

USRRESBIND = ReplaceableObject(
    'huawei_cm_2g."USRRESBIND"',
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
    t1."FIRSTUSERTYPE",
    t1."RESERVEDRESTYPE",
    t1."RESRESERVEDMINUTES",
    t1."SECONDUSERTYPE"
FROM
huawei_nbi_gsm."USRRESBIND" t1

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
    t2."FIRSTUSERTYPE",
    NULL,
    t2."RESRESERVEDMINUTES",
    t2."SECONDUSERTYPE"
FROM
huawei_gexport_gsm."USRRESBIND_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."FIRSTUSERTYPE",
    NULL,
    t3."RESRESERVEDMINUTES",
    t3."SECONDUSERTYPE"
FROM
huawei_gexport_gsm."USRRESBIND_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
"""
)

VLANID = ReplaceableObject(
    'huawei_cm_2g."VLANID"',
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
huawei_nbi_gsm."VLANID" t1

"""
)

WEBLOGINPOLICY = ReplaceableObject(
    'huawei_cm_2g."WEBLOGINPOLICY"',
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
    t1."POLICY"
FROM
huawei_nbi_gsm."WEBLOGINPOLICY" t1

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
    t2."POLICY"
FROM
huawei_gexport_gsm."WEBLOGINPOLICY_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."POLICY"
FROM
huawei_gexport_gsm."WEBLOGINPOLICY_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."POLICY"
FROM
huawei_mml_gsm."WEBLOGINPOLICY" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

"""
)

XPUPORT = ReplaceableObject(
    'huawei_cm_2g."XPUPORT"',
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
    t1."PN",
    t1."PORTSWITCH",
    t1."SN",
    t1."SRN"
FROM
huawei_nbi_gsm."XPUPORT" t1

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
    t2."PN",
    t2."PORTSWITCH",
    t2."SN",
    t2."SRN"
FROM
huawei_gexport_gsm."XPUPORT_BSC6900GSM" t2
INNER JOIN huawei_gexport_gsm."SYS_BSC6900GSM" t21 ON t21."FILENAME" = t2."FILENAME"
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
    t3."PN",
    t3."PORTSWITCH",
    t3."SN",
    t3."SRN"
FROM
huawei_gexport_gsm."XPUPORT_BSC6910GSM" t3
INNER JOIN huawei_gexport_gsm."SYS_BSC6910GSM" t31 ON t31."FILENAME" = t3."FILENAME"
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
    t4."PN",
    t4."PORTSWITCH",
    t4."SN",
    t4."SRN"
FROM
huawei_mml_gsm."XPUPORT" t4
INNER JOIN huawei_mml_gsm."SYS" t41 ON t41."FileName" = t4."FileName"

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
    # op.create_view(FILEFOOTER)
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
    op.drop_view(FILEFOOTER)
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

