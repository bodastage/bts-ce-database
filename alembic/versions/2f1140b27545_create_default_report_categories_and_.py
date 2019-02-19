"""Create default report categories and reports

Revision ID: 2f1140b27545
Revises: 0c50cea7ffd3
Create Date: 2019-02-20 01:29:13.231781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f1140b27545'
down_revision = '0c50cea7ffd3'
branch_labels = None
depends_on = None


def upgrade():
    report_categories = sa.Table(
        'report_categories',
        sa.MetaData(),
        sa.Column('pk', sa.Integer, sa.Sequence('seq_report_categories_pk', schema='reports'), primary_key=True, nullable=False),
        sa.Column('name', sa.String(100), nullable=False, unique=True),
        sa.Column('notes', sa.Text),
        sa.Column('parent_pk', sa.Integer, default=0),
        sa.Column('modified_by', sa.Integer, default=0),
        sa.Column('added_by', sa.Integer, default=0),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'reports'
    )

    op.bulk_insert(report_categories, [
        {'name': 'Key Parameters', 'notes': 'Key Parameters'},
        {'name': 'Network Inventory', 'notes': 'Network Inventory'},
        {'name': 'Network Entities', 'notes': 'Network Entities'},
    ])


    reports = sa.Table(
        'reports',
        sa.MetaData(),
        sa.Column('pk', sa.Integer, sa.Sequence('seq_reports_pk', schema='reports'), primary_key=True, nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('query', sa.Text, nullable=False),
        sa.Column('db_connector_pk', sa.Integer),
        sa.Column('options', sa.Text), #JSON
        sa.Column('category_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'reports'
    )



    connection = op.get_bind()
    r = connection.execute(report_categories.select().where(report_categories.c.name == 'Key Parameters'))

    category_pk = 0
    for row in r:  category_pk = row['pk']

    op.bulk_insert(reports, [
        {'name': 'Ericsson 2G Parameters',
         'notes': 'Ericsson 2G Parameters',
         'options': '{}',
         'category_pk': category_pk,
         'query': """
            WITH QRY_CHANNEL_GROUP_TRX AS (
                SELECT T1."BSC_NAME" AS "NENAME", t1."CELL_NAME" AS "CELLNAME", COUNT(t1."CHGR_NAME") AS NumberOfTRX
                FROM ericsson_cm."CHANNEL_GROUP" t1
                GROUP BY t1."BSC_NAME", t1."CELL_NAME"
            )
            SELECT
               t1."DATETIME",
               'VIVO' AS "REGIONAL",
               'ERICSSON' AS "VENDOR",
               '2G' AS "TECHNOLOGY",
               'BSC' AS "NETYPE",
               t1."BSC_NAME" AS "NENAME",
               '' AS "MGW",
            --    REPLACE("MODE", " - ACTIVE", "") AS MGC,
               '' AS "MGC_NUM",
               '' AS "CARR",
               SUBSTRING(t1."CELL_NAME", 2, 3) AS "SITEPROP",
               SUBSTRING(LPAD(t1."CI", 5, '0'),0, 4) AS "SITEID",
               SUBSTRING(t1."CELL_NAME", 0, 5) AS "SITENAME",
               t1."CI" AS "CELLID",
               t1."CELL_NAME" AS "CELLNAME",
               REPLACE(t1."CELL_STATE", '"', '') AS "ACTSTATUS",
               '' AS BLKSTATUS,
               REPLACE(t1."C_SYS_TYPE", 'GSM', '') AS "DLF",
               REPLACE(t1."C_SYS_TYPE", 'GSM', '') AS "ULF",
               '' AS "DLBANDWIDTH",
               REPLACE(t1."C_SYS_TYPE", 'GSM', '') AS "BAND",
               t1."MCC",
               t1."MNC",
               t1."LAC",
               '' AS "RAC",		
               t1."BCCHNO",
               t1."BCC",
               t1."NCC",
               t1."CI",
               CONCAT(t1."BCC", t1."NCC") AS "BSIC",
               CONCAT(t1."MCC", ' - ', LPAD(t1."MNC", 2, '0'), ' - ', LPAD(t1."LAC",5 ,'0'), ' - ', LPAD(t1."CI", 5,'0')) AS "CGI",
               CONCAT(t1."MCC", ' - ', t1."MNC", ' - ', t1."LAC", ' - ', t1."CI") AS CGI_Raw,
               '' AS "CGI_HEX",
               t3.NumberOfTRX AS TRX_NUM 
                FROM ericsson_cm."INTERNAL_CELL" t1 
                INNER JOIN ericsson_cm."BSC" t2 ON t1."BSC_NAME" = t2."BSC_NAME"
                  LEFT JOIN QRY_CHANNEL_GROUP_TRX t3
                  ON t1."CELL_NAME" = t3."CELLNAME"
                  AND t1."BSC_NAME" = t3."NENAME"
            """, },
        {'name': 'Ericsson 3G Parameters',
         'notes': 'Ericsson 3G Parameters',
         'options': '{}',
         'category_pk': category_pk,
         'query': """
                SELECT t1."DATETIME" AS "DATETIME",
                       'ERICSSON' AS "VENDOR",
                       '3G' AS "TECHNOLOGY",
                       t1."SubNetwork_2_id" AS "NENAME",
                       t2."cId" AS "CELLID",
                       t2."userLabel" AS "CELLNAME",
                --        t3."CELLNAME_SC",
                       SUBSTRING(t2."userLabel", 2, 3) AS "SITEPROP",
                       SUBSTRING(LPAD(t2."cId", 5, '0'),0, 4) AS "SITEID",
                       t3."MeContext_id" as "SITENAME",
                       t1."plmnIdentity_mcc" AS "MCC",
                       t1."plmnIdentity_mnc" AS "MNC",
                       t2."lac" AS "LAC",
                       t2."rac" AS "RAC",
                       t2."uarfcnDl" AS "DLF",
                       t2."uarfcnUl" AS "ULF",
                       CASE WHEN t2."administrativeState" = '1' THEN 'UNLOCKED'
                            WHEN t2."administrativeState" = '0' THEN 'LOCKED'
                            ELSE 'SHUTTING_DOWN'
                       END
                       AS "ACTSTATUS",
                       '' AS "BLKSTATUS",
                       t2."primaryScramblingCode" AS "PSC",
                       t2."cId" AS "CID",
                       t2."cId" AS "CI",
                       CONCAT(t1."plmnIdentity_mcc", '-', LPAD(t1."plmnIdentity_mnc", 2, '0'), '-',LPAD(t2."lac",5, '0'), '-', LPAD(t2."cId",5, '0')) AS CGI,
                       CONCAT(t1."plmnIdentity_mcc", '-', t1."plmnIdentity_mnc", '-', t2."lac", '-', t2."cId") AS "CGI_RAW",
                       '' AS "CGI_HEX"
                FROM ericsson_cm."UtranNetwork" t1
                    INNER JOIN ericsson_cm."UtranCell"  t2 ON t2."SubNetwork_2_id" = t1."SubNetwork_2_id" 
                    LEFT JOIN ericsson_cm."RbsLocalCell" t3 ON t2."SubNetwork_2_id" = t1."SubNetwork_2_id" 
                        AND t2."cId" = t3."localCellId"
        """, },
        {'name': 'Ericsson 4G Parameters',
         'notes': 'Ericsson 4G Parameters',
         'options': '{}',
         'category_pk': category_pk,
         'query': """
                SELECT t1."DATETIME" AS "DATETIME",
                       'ERICSSON' AS "VENDOR",
                       '4G' AS "TECHNOLOGY",
                       t1."SubNetwork_2_id" AS "NENAME",
                       '' AS "NEID",
                       SUBSTRING(t2."MeContext_id",2, 3) AS "SITEPROP",
                       t2."eNBId" AS "SITEID",
                       t2."MeContext_id" AS "SITENAME",
                       t1."cellId" AS "CELLID",
                       t1."userLabel" AS "CELLNAME",
                       256*t2."eNBId"::integer + t1."cellId"::integer AS "CI",
                       CASE WHEN t1."administrativeState" = '1' THEN 'UNLOCKED'
                            WHEN t1."administrativeState" = '0' THEN 'LOCKED'
                            ELSE 'SHUTTING_DOWN'
                       END
                       AS "ACTSTATUS",
                       '' AS "BLKSTATUS",
                       t1."dlChannelBandwidth" AS "DLBANDWIDTH",
                --        t1.[BAND],
                       '' AS "CARR",
                       t1."earfcndl" AS "DLF",
                       t1."earfcnul" AS "ULF",
                       t1."mcc" AS "MCC",
                       t1."mnc" AS "MNC",
                       '' AS "LAC",
                       '' AS "RAC",
                       CONCAT(t1."mcc",'-', t1."mnc", '-', LPAD(t1."MeContext_id", 5,'0'), '-',LPAD(t1."cellId", 3, '0')) AS "CGI",
                       t1."physicalLayerCellIdGroup" AS "PCI",
                       t1."tac" AS  "TAC",
                       t1."rachRootSequence"  AS "ROOTSEQ"
                FROM ericsson_cm."EUtranCellFDD" t1
                INNER JOIN ericsson_cm."ENodeBFunction" t2 ON t2."SubNetwork_2_id" = t1."SubNetwork_2_id"
    
    
        """, },
        {'name': 'Huawei 2G Parameters',
         'notes': 'Huawei 2G Parameters',
         'options': '{}',
         'category_pk': category_pk,
         'query': """
                SELECT
                t1."DATETIME" AS "DATETIME",
                t2."SYSOBJECTID" as "NENAME",
                'HUAWEI' AS "VENDOR",
                '2G' AS "TECHNOLOGY",
                t3."BTSNAME" AS "SITENAME",
                t3."BTSID" AS "SITEID",
                t1."CELLNAME" AS "CELLNAME",
                t1."ACTSTATUS" AS "ACTSTATUS",
                t1."ADMSTAT" AS "BLKSTATUS",
                t1."MCC" AS "MCC",
                t1."MNC" AS "MNC",
                t1."LAC" AS "LAC",
                t1."CI" AS "CI",
                t1."BCCHNO" AS "BCCHNO",
                t1."NCC" AS "NCC",
                t1."BCC" AS "BCC",
                CONCAT(t1."NCC", t1."BCC") AS "BSIC",
                CONCAT(t1."MCC", '-', t1."MNC", '-', t1."LAC", '-', t1."CI") AS "CGI_RAW",
                CONCAT(t1."MCC", '-', t1."MNC", '-', LPAD(t1."LAC",5,'0'), '-', t1."CI") AS "CGI"
                FROM huawei_cm."GCELL" t1
                INNER JOIN huawei_cm."SYS" t2 ON t1."FILENAME" = t2."FILENAME"
                INNER JOIN huawei_cm."BTS" t3 ON t3."BTSID" = t1."BTSID" AND t1."FILENAME" = t3."FILENAME"
                INNER JOIN huawei_cm."GCELLGPRS" t4 ON t4."FILENAME" = t1."FILENAME" AND T4."CELLID" = t1."CELLID"
        """, },
        {'name': 'Huawei 3G Parameters',
         'notes': 'Huawei 3G Parameters',
         'options': '{}',
         'category_pk': category_pk,
         'query': """
                SELECT
                t1."DATETIME" AS "DATETIME",
                t2."SYSOBJECTID" as "NENAME",
                'HUAWEI' AS "VENDOR",
                '3G' AS "TECHNOLOGY",
                '' AS "NEID",
                t4."NODEBFUNCTIONNAME" AS "SITENAME",
                t4."NODEBID" AS "SITEID",
                t1."CELLNAME" AS "CELLNAME",
                t1."ACTSTATUS" AS "ACTSTATUS",
                -- t1."ADMSTAT" AS "BLKSTATUS",
                t5."MCC" AS "MCC",
                t5."MNC" AS "MNC",
                t1."LAC" AS "LAC",
                t1."RAC" AS "RAC",
                t1."SAC" AS "SAC",
                t1."LOCELL" AS "CI",
                t1."UARFCNDOWNLINK" AS "DLF",
                t1."UARFCNUPLINK" AS "ULF",
                t1."PSCRAMBCODE" AS "PSCRAMBCODE",
                CONCAT(t5."MCC", '-', t5."MNC", '-', t1."LAC", '-', t1."LOCELL") AS "CGI_RAW",
                CONCAT(t5."MCC", '-', t5."MNC", '-', LPAD(t1."LAC",5,'0'), '-', t1."LOCELL") AS "CGI"
                FROM huawei_cm."UCELL" t1
                INNER JOIN huawei_cm."SYS" t2 ON t1."FILENAME" = t2."FILENAME"
                INNER JOIN huawei_cm."URNCBASIC" t3 ON t3."RNCID" = t1."LOGICRNCID" AND t1."FILENAME" = t3."FILENAME"
                INNER JOIN huawei_cm."NODEBFUNCTION" t4 ON t1."FILENAME" = t1."FILENAME"
                INNER JOIN huawei_cm."UCNOPERATOR" t5 ON t5."FILENAME" = t1."FILENAME"
        """, },
        {'name': 'Huawei 4G Parameters',
         'notes': 'Huawei 4G Parameters',
         'options': '{}',
         'category_pk': category_pk,
         'query': """
                SELECT
                t1."DATETIME" AS "DATETIME",
                t2."SYSOBJECTID" as "NENAME",
                'HUAWEI' AS "VENDOR",
                '4G' AS "TECHNOLOGY",
                '' AS "NEID",
                t1."ENODEBFUNCTIONNAME" AS "SITENAME",
                t4."ENODEBID" AS "SITEID",
                t1."CELLNAME" AS "CELLNAME",
                t1."CELLACTIVESTATE" AS "ACTSTATUS",
                -- t1."ADMSTAT" AS "BLKSTATUS",
                t5."MCC" AS "MCC",
                t5."MNC" AS "MNC",
                t6."TAC" AS "TAC",
                t1."CELLID" AS "CI",
                t1."PHYCELLID" AS "PCI",
                t1."DLBANDWIDTH" AS "UARFCNDOWNLINK",
                t1."DLEARFCN" AS "DLF",
                t1."ULEARFCN" AS "ULF",
                CONCAT(t5."MCC", '-', t5."MNC", '-', t4."ENODEBID", '-', t1."LOCALCELLID") AS "CGI_RAW",
                CONCAT(t5."MCC", '-', t5."MNC", '-', LPAD(t4."ENODEBID",5,'0'), '-', t1."LOCALCELLID") AS "CGI"
                FROM huawei_cm."CELL" t1
                INNER JOIN huawei_cm."SYS" t2 ON t1."FILENAME" = t2."FILENAME"
                INNER JOIN huawei_cm."ENODEBFUNCTION" t4 ON t1."FILENAME" = t1."FILENAME"
                INNER JOIN huawei_cm."UCNOPERATOR" t5 ON t5."FILENAME" = t1."FILENAME"
                INNER JOIN huawei_cm."CNOPERATORTA" t6 ON t6."FILENAME" = t1."FILENAME"
        """, },
    ])


def downgrade():
    op.execute('TRUNCATE table reports.reports')
    op.execute('TRUNCATE table reports.report_categories')
